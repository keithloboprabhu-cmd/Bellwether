/** Deterministic terrain geometry and event-driven Canvas 2D renderer.
 * Impacts are fractions. A=tanh(impact/0.15), fixed across scenarios.
 * Smooth anisotropic interpolation joins companies into one continuous terrain.
 * Positive normalized weights bound the surface by its anchors, with h(anchor)=A.
 */
export type FieldNode = {id:string; impact:number|null};
export type Anchor = {id:string; x:number; y:number; radius:number};
/** Fixed density scale: a 9.2% impact has about six times the center density of 1.4%. */
export function dotDensity(height:number):number {return Math.min(.92,Math.abs(height)*1.2);}
/** Stable spatial dithering gives both signs the same density without diagonal masks. */
export function dotThreshold(x:number,y:number):number {
  let h=Math.imul(x+1,374761393)^Math.imul(y+1,668265263);
  h=Math.imul(h^(h>>>13),1274126177);
  return ((h^(h>>>16))>>>0)/4294967296;
}
/** Map a fractional EPS impact to elevation on the shared, fixed scale. */
export function mappedImpact(impact:number|null):number {return impact===null?0:Math.tanh(impact/.15);}
function hash(s:string):number {let h=2166136261; for(const c of s) h=Math.imul(h^c.charCodeAt(0),16777619);return h>>>0;}
/** Place a configured entity set independently of sorting or shock magnitude. */
export function anchorsFor(nodes:FieldNode[],seed=256):Anchor[] {
  const sorted=[...nodes].sort((a,b)=>hash(a.id+seed)-hash(b.id+seed)||a.id.localeCompare(b.id));
  const cols=Math.ceil(Math.sqrt(sorted.length*1.5)),rows=Math.ceil(sorted.length/cols);
  return sorted.map((n,i)=>({id:n.id,x:(i%cols+.5)/cols,y:(Math.floor(i/cols)+.5)/rows,radius:Math.min(1/cols,1/rows)*.8}));
}
type Peak=Anchor&{height:number};
function terrainPeaks(nodes:FieldNode[],anchors:Anchor[]):Peak[] {
  const impacts=new Map(nodes.map(n=>[n.id,n.impact]));
  return anchors.map(a=>({...a,height:mappedImpact(impacts.get(a.id)??null)}));
}
function terrainHeight(x:number,y:number,peaks:Peak[]):number {
  let height=0,weight=0;
  for(const a of peaks){
    const dx=(x-a.x)/a.radius,dy=(y-a.y)/a.radius;
    const along=dx*.8+dy*.6,across=-dx*.6+dy*.8;
    const distance=along*along*.55+across*across*1.65;
    if(distance<1e-14)return a.height;
    const w=1/(distance*distance);
    height+=a.height*w;weight+=w;
  }
  return weight?height/weight:0;
}
/** Interpolate a bounded flowing surface with exact heights at company anchors. */
export function heightAt(x:number,y:number,nodes:FieldNode[],anchors:Anchor[]):number {
  return terrainHeight(x,y,terrainPeaks(nodes,anchors));
}
export type FieldColors = {gold:string; gain:string; loss:string; plate:string; ink:string};
/** Attach the event-driven renderer and return its small update/cleanup lifecycle. */
export function createField(canvas:HTMLCanvasElement,colors:FieldColors) {
  let nodes:FieldNode[]=[], anchors:Anchor[]=[], illustrative=false, selection:string|null=null;
  let destroyed=false,visible=true;
  let cachedKey='';const cached=document.createElement('canvas');
  const ctx=canvas.getContext('2d');
  if(!ctx)throw new Error('Canvas 2D is unavailable. Exact results remain in the table.');
  function render(){
    if(destroyed || document.hidden || !visible)return;
    const w=canvas.clientWidth,h=canvas.clientHeight,dpr=Math.min(devicePixelRatio||1,2);
    if(!w || !h)return;
    canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx!.setTransform(dpr,0,0,dpr,0,0);
    function drawSelection(){
      if(selection){const a=anchors.find(a=>a.id===selection);if(a){ctx!.strokeStyle=colors.ink;ctx!.lineWidth=1;ctx!.beginPath();ctx!.arc(a.x*w,a.y*h,13,0,Math.PI*2);ctx!.stroke();}}
    }
    const key=JSON.stringify([w,h,dpr,illustrative,nodes]);
    if(cachedKey===key){ctx!.drawImage(cached,0,0,w,h);drawSelection();return;}
    ctx!.fillStyle=colors.plate;ctx!.fillRect(0,0,w,h);
    const step=3, nx=Math.ceil(w/step),ny=Math.ceil(h/step),values=new Float32Array((nx+1)*(ny+1));
    const peaks=terrainPeaks(nodes,anchors);
    const elevation=(u:number,v:number)=>illustrative?
      .43*Math.exp(-((u-.48)**2/.08+(v-.52)**2/.13))+.24*Math.sin(u*13+v*5)*Math.exp(-((v-.5)**2/.3)):
      terrainHeight(u,v,peaks);
    let minHeight=Infinity,maxHeight=-Infinity;
    for(let y=0;y<=ny;y++)for(let x=0;x<=nx;x++){
      const value=elevation(x/nx,y/ny);values[y*(nx+1)+x]=value;
      minHeight=Math.min(minHeight,value);maxHeight=Math.max(maxHeight,value);
    }
    // A very dim continuous light layer makes the halftone read as elevation,
    // rather than disconnected confetti. It uses the same signed data surface.
    const light=document.createElement('canvas');light.width=nx+1;light.height=ny+1;
    const lightCtx=light.getContext('2d');
    function rgb(color:string){const hex=color.trim().replace('#','');return [0,2,4].map(i=>parseInt(hex.slice(i,i+2),16));}
    const gain=rgb(colors.gain),loss=rgb(colors.loss);
    if(lightCtx&&!illustrative){
      const pixels=lightCtx.createImageData(nx+1,ny+1);
      for(let i=0;i<values.length;i++){
        const z=values[i],magnitude=Math.abs(z),signed=z>0?gain:loss;
        for(let c=0;c<3;c++)pixels.data[i*4+c]=signed[c];
        pixels.data[i*4+3]=Math.min(.16,magnitude*.24)*255;
      }
      lightCtx.putImageData(pixels,0,0);ctx!.imageSmoothingEnabled=true;ctx!.drawImage(light,0,0,w,h);
    }
    // Fine screen-space dots are independent of the coarser contour mesh. Stronger
    // shocks add points on the same stable grid; tiny shocks have no Bayer floor.
    const pitch=2, dotSize=1.25;
    for(let y=0;y*pitch<h;y++)for(let x=0;x*pitch<w;x++){
      const px=(x+.5)*pitch,py=(y+.5)*pitch;
      const z=elevation(px/w,py/h);
      const density=illustrative?dotDensity(z)*.8+.018:dotDensity(z);
      if(density>dotThreshold(x,y)){
        const magnitude=Math.min(1,Math.abs(z));
        ctx!.globalAlpha=illustrative?.14:.18+magnitude*.75;
        ctx!.fillStyle=illustrative?colors.gold:z>0?colors.gain:colors.loss;
        ctx!.fillRect(Math.round(px*dpr)/dpr,Math.round(py*dpr)/dpr,dotSize,dotSize);
      }
    }
    ctx!.globalAlpha=1;
    // Fine fixed-height contour intervals expose gradients even in small shocks.
    const levels=illustrative?Array.from({length:14},(_,i)=>(i+1)*.045):Array.from({length:80},(_,i)=>(i<40?i-40:i-39)*.025);
    levels.forEach((level,index)=>{
      if(level<=minHeight||level>=maxHeight)return;
      const major=Math.round(Math.abs(level)/.025)%5===0;
      ctx!.beginPath();ctx!.lineWidth=illustrative?(index%5===0?1.1:.65):(major?1:.55);
      ctx!.strokeStyle=illustrative?colors.gold:level>0?colors.gain:colors.loss;ctx!.globalAlpha=illustrative?(index%5===0?.33:.16):(major?.46:.18+Math.abs(level)*.25);
      for(let y=0;y<ny;y++)for(let x=0;x<nx;x++){
        const p=[[x/nx*w,y/ny*h],[(x+1)/nx*w,y/ny*h],[(x+1)/nx*w,(y+1)/ny*h],[x/nx*w,(y+1)/ny*h]];
        const v=[values[y*(nx+1)+x],values[y*(nx+1)+x+1],values[(y+1)*(nx+1)+x+1],values[(y+1)*(nx+1)+x]];
        const hits:number[][]=[];
        for(let e=0;e<4;e++){const j=(e+1)%4;if((v[e]>level)!==(v[j]>level)){const t=(level-v[e])/(v[j]-v[e]);hits.push([p[e][0]+t*(p[j][0]-p[e][0]),p[e][1]+t*(p[j][1]-p[e][1])]);}}
        for(let k=0;k+1<hits.length;k+=2){ctx!.moveTo(...hits[k] as [number,number]);ctx!.lineTo(...hits[k+1] as [number,number]);}
      }ctx!.stroke();
    });
    ctx!.globalAlpha=1;
    cached.width=canvas.width;cached.height=canvas.height;cached.getContext('2d')?.drawImage(canvas,0,0);cachedKey=key;
    drawSelection();
  }
  const observer=new ResizeObserver(render);observer.observe(canvas);
  const intersection=new IntersectionObserver(entries=>{visible=entries[0]?.isIntersecting??false;if(visible)render();});intersection.observe(canvas);
  document.addEventListener('visibilitychange',render);
  return {
    setNodes(next:FieldNode[],isIllustrative=false){nodes=next;anchors=anchorsFor(next);illustrative=isIllustrative;render();},
    setSelection(id:string|null){selection=id;render();},
    destroy(){destroyed=true;observer.disconnect();intersection.disconnect();document.removeEventListener('visibilitychange',render);},
  };
}
