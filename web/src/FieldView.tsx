/** Accessible selection controls and table fallback surround the independent renderer. */
import {useEffect,useRef,useState} from 'react';
import {anchorsFor,createField} from './field';
import {percent,signClass} from './format';
import type {CSSProperties} from 'react';
import type {Company} from './types';

/** Pair visual terrain with keyboard/touch selection and an exact data alternative. */
export function Field({companies=[],selected=null,onSelect,illustrative=false}:{companies?:Company[];selected?:string|null;onSelect?:(id:string|null)=>void;illustrative?:boolean}) {
  const canvas=useRef<HTMLCanvasElement>(null),renderer=useRef<ReturnType<typeof createField>|null>(null);
  const [failed,setFailed]=useState(false),[table,setTable]=useState(false);
  const nodes=companies.map(c=>({id:c.id,impact:c.eps})), anchors=anchorsFor(nodes);
  const cols=Math.ceil(Math.sqrt(companies.length*1.5)),rows=Math.ceil(companies.length/cols);
  const expanded=!illustrative&&companies.length>10;
  const active=companies.find(c=>c.id===selected);
  useEffect(()=>{
    if(!canvas.current)return;
    const css=getComputedStyle(document.documentElement);
    try{renderer.current=createField(canvas.current,{gold:css.getPropertyValue('--gold'),gain:css.getPropertyValue('--gain'),loss:css.getPropertyValue('--loss'),plate:css.getPropertyValue('--plate'),ink:css.getPropertyValue('--ink')});}
    catch{setFailed(true);}
    return()=>renderer.current?.destroy();
  },[]);
  useEffect(()=>{renderer.current?.setNodes(companies.map(c=>({id:c.id,impact:c.eps})),illustrative);},[companies,illustrative]);
  useEffect(()=>{renderer.current?.setSelection(selected);},[selected]);
  return <section className={`field-frame ${illustrative?'illustrative':''}`} onKeyDown={e=>{if(e.key==='Escape')onSelect?.(null);}} aria-label={illustrative?'Illustrative contour terrain':'The Field: modeled company earnings changes'}>
    <div className="field-heading"><span className="eyebrow">{illustrative?'The Field / standby':'The Field'}</span><span className="micro">{illustrative?'Illustrative terrain':'EPS Δ / fixed scale'}</span></div>
    <div className="field-pan" tabIndex={expanded?0:undefined} role={expanded?'region':undefined} aria-label={expanded?'Company landscape; scroll horizontally to inspect all companies':undefined}><div className={`field-surface ${expanded?'field-expanded':''}`} style={expanded?{'--field-cols':cols,'--field-rows':rows} as CSSProperties:undefined}>
      <canvas ref={canvas} aria-hidden="true"/>
      {!illustrative && !failed && anchors.map(a=>{const c=companies.find(c=>c.id===a.id)!;return <button key={c.id} className={`field-label ${signClass(c.eps)} ${selected===c.id?'selected':''} ${c.is_custom?'is-custom':''}`} style={{left:`${a.x*100}%`,top:`${a.y*100}%`}} aria-pressed={selected===c.id} aria-label={`${c.display_ticker||c.id} ${c.eps===0?'No change':c.eps===null?'Unavailable':percent(c.eps)} · ${c.name}. Select to inspect.`} onClick={()=>onSelect?.(c.id)} onPointerEnter={e=>{if(e.pointerType==='mouse')onSelect?.(c.id);}} onFocus={()=>onSelect?.(c.id)}><span className="node-ring"/><span>{c.display_ticker||c.id}<small>{c.eps===0?'No change':c.eps===null?'Unavailable':percent(c.eps)}</small></span></button>;})}
      {illustrative && <div className="field-caption"><span>Policy in.</span><span>Earnings impact out.</span></div>}
    </div></div>
    {expanded&&<p className="micro field-pan-hint">Pan horizontally for all companies.</p>}
    {failed && <p role="status" className="field-fallback">Terrain is unavailable in this browser. Exact results are available below.</p>}
    {!illustrative && <>
      <div className="field-selection" aria-live="polite">{active?<><strong>{active.name}</strong><span>EPS {percent(active.eps)} · Range {percent(active.low)} to {percent(active.high)} · Implied price {percent(active.value)}</span><button className="text-button selection-dismiss" aria-label="Dismiss selection" onClick={()=>onSelect?.(null)}>Dismiss</button></>:<span>Select a company to inspect its estimate and range.</span>}</div>
      <div className="field-legend"><span><i className="pattern gain-pattern"/>Modeled increase</span><span><i className="pattern loss-pattern"/>Modeled decrease</span><span>○ No change</span>{companies.some(c=>c.is_custom)&&<span>□ Your company</span>}</div>
      <p className="micro field-note">Fixed scale / schematic positions <button className="text-button" onClick={()=>setTable(!table)} aria-expanded={table||failed}>{table?'Hide data':'Exact data'}</button></p>
      {(table||failed)&&<div className="table-scroll" tabIndex={0} role="region" aria-label="Field equivalent data"><table><caption>Company earnings changes · scenario bounds</caption><thead><tr><th scope="col">Company</th><th scope="col">Base</th><th scope="col">Low</th><th scope="col">High</th></tr></thead><tbody>{companies.map(c=><tr key={c.id}><th scope="row">{c.name}</th><td>{c.eps===0?'No change':c.eps===null?'Unavailable':percent(c.eps)}</td><td>{percent(c.low)}</td><td>{percent(c.high)}</td></tr>)}</tbody></table></div>}
    </>}
  </section>;
}
