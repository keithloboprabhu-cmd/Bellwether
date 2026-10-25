/** Deterministic terrain geometry and event-driven Canvas 2D renderer.
 * Impacts are fractions. A=tanh(impact/0.15), fixed across scenarios.
 * Compact supports exclude neighboring anchors. A normalized partition bounds the
 * interpolated terrain by its node values, with h(anchor)=A and no noise contribution.
 */
export type FieldNode = {id:string; impact:number|null};
export type Anchor = {id:string; x:number; y:number; radius:number};
export const BAYER = [0,8,2,10,12,4,14,6,3,11,1,9,15,7,13,5];
/** Map a fractional EPS impact to elevation on the shared, fixed scale. */
export function mappedImpact(impact:number|null):number {return impact===null?0:Math.tanh(impact/.15);}
function hash(s:string):number {let h=2166136261; for(const c of s) h=Math.imul(h^c.charCodeAt(0),16777619);return h>>>0;}
/** Place a configured entity set independently of sorting or shock magnitude. */
export function anchorsFor(nodes:FieldNode[],seed=256):Anchor[] {
  const sorted=[...nodes].sort((a,b)=>hash(a.id+seed)-hash(b.id+seed)||a.id.localeCompare(b.id));
  const cols=Math.ceil(Math.sqrt(sorted.length*1.5)),rows=Math.ceil(sorted.length/cols);
  return sorted.map((n,i)=>({id:n.id,x:(i%cols+.5)/cols,y:(Math.floor(i/cols)+.5)/rows,radius:Math.min(1/cols,1/rows)*.8}));
}
/** Evaluate bounded geometry while preserving each node's exact mapped height. */
export function heightAt(x:number,y:number,nodes:FieldNode[],anchors:Anchor[]):number {
  let h=0,weight=0;
  for(const a of anchors){const n=nodes.find(n=>n.id===a.id);if(!n || n.impact===null)continue;
    const d=Math.hypot(x-a.x,y-a.y)/a.radius;
    if(d<1){const w=Math.pow(1-d*d,2);h+=mappedImpact(n.impact)*w;weight+=w;}
  }return h/Math.max(1,weight);
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
    const w=canvas.clientWidth,h=canvas.clientHeight,dpr=Math.min(devicePixelRatio||1,1.5);
    if(!w || !h)return;
    canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);ctx!.setTransform(dpr,0,0,dpr,0,0);
    function drawSelection(){
      if(selection){const a=anchors.find(a=>a.id===selection);if(a){ctx!.strokeStyle=colors.ink;ctx!.lineWidth=1;ctx!.beginPath();ctx!.arc(a.x*w,a.y*h,13,0,Math.PI*2);ctx!.stroke();}}
    }
    const key=JSON.stringify([w,h,dpr,illustrative,nodes]);
    if(cachedKey===key){ctx!.drawImage(cached,0,0,w,h);drawSelection();return;}
    ctx!.fillStyle=colors.plate;ctx!.fillRect(0,0,w,h);
    const step=5, nx=Math.ceil(w/step),ny=Math.ceil(h/step),values=new Float32Array((nx+1)*(ny+1));
    const elevation=(u:number,v:number)=>illustrative?
      .43*Math.exp(-((u-.48)**2/.08+(v-.52)**2/.13))+.24*Math.sin(u*13+v*5)*Math.exp(-((v-.5)**2/.3)):
      heightAt(u,v,nodes,anchors);
    // Low-resolution ordered dither buffer; no stochastic contribution to heights.
    const buffer=document.createElement('canvas');buffer.width=nx;buffer.height=ny;
    const b=buffer.getContext('2d');if(!b)return;
    for(let y=0;y<=ny;y++)for(let x=0;x<=nx;x++)values[y*(nx+1)+x]=elevation(x/nx,y/ny);
    for(let y=0;y<ny;y++)for(let x=0;x<nx;x++){
      const z=values[y*(nx+1)+x], threshold=BAYER[(y%4)*4+x%4]/16;
      if(Math.abs(z)*.8+(illustrative?.025:0)>threshold && (illustrative||z!==0)){
        b.globalAlpha=illustrative?.10:.75;
        b.fillStyle=illustrative?colors.gold:z>0?colors.gain:z<0?colors.loss:colors.gold;
        if(z<0&&!illustrative){if((x+y)%4===0)b.fillRect(x,y,1,1);}
        else b.fillRect(x,y,1,1);
      }
    }
    ctx!.imageSmoothingEnabled=false;ctx!.drawImage(buffer,0,0,w,h);
    // Fourteen marching-squares contours, fixed signed levels; stronger fifth indices.
    const levels=illustrative?Array.from({length:14},(_,i)=>(i+1)*.045):Array.from({length:28},(_,i)=>(i<14?i-14:i-13)/14);
    levels.forEach((level,index)=>{
      ctx!.beginPath();ctx!.lineWidth=index%5===0?1.1:.65;
      ctx!.strokeStyle=colors.gold;ctx!.globalAlpha=illustrative?(index%5===0?.33:.16):(index%5===0?.5:.26);
      for(let y=0;y<ny;y++)for(let x=0;x<nx;x++){
        const p=[[x*step,y*step],[(x+1)*step,y*step],[(x+1)*step,(y+1)*step],[x*step,(y+1)*step]];
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
