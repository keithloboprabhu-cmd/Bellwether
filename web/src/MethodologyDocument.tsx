/** Guided, model-only reading experience sourced from METHODOLOGY.md. */
import {useMemo,useRef,useState} from 'react';
import type {KeyboardEvent,ReactNode} from 'react';
import './methodology.css';

type Section={title:string;body:string};
type Chapter={title:string;summary:string;sections:Section[]};
const steps=[{id:'data',label:'Data & baselines',hint:'What the model starts with'}, {id:'transmission',label:'Policy transmission',hint:'Which firms are affected'}, {id:'earnings',label:'Earnings & value',hint:'How the impact is calculated'}, {id:'ranges',label:'Ranges & sensitivity',hint:'What changes the estimate'}, {id:'validation',label:'Validation & limits',hint:'How to interpret the result'}];

function Inline({text}:{text:string}){
  return <>{text.split(/(`[^`]+`|\*\*[^*]+\*\*|\[[^\]]+\]\((?:https?:\/\/|\/)[^)]+\))/g).map((part,i)=>{
    if(part.startsWith('`'))return <code key={i}>{part.slice(1,-1)}</code>;
    if(part.startsWith('**'))return <strong key={i}>{part.slice(2,-2)}</strong>;
    const link=part.match(/^\[([^\]]+)\]\(((?:https?:\/\/|\/)[^)]+)\)$/);
    return link?<a key={i} href={link[2]} {...(link[2].startsWith('http')?{target:'_blank',rel:'noreferrer'}:{})}>{link[1]}</a>:part;
  })}</>;
}

function tableRows(text:string):string[][] {
  return text.split('\n').filter(l=>l.trim().startsWith('|')).map(l=>l.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim())).filter(row=>!row.every(c=>/^:?-+:?$/.test(c)));
}

function parseDocument(text:string):{intro:string;chapters:Chapter[]} {
  const parts=text.split(/^## /m),intro=parts.shift()!.replace(/^# .*\n/m,'').trim();
  return {intro,chapters:parts.map(part=>{
    const [heading,...rest]=part.split('\n'),sections=rest.join('\n').split(/^### /m);
    const summary=sections.shift()!.trim();
    return {title:heading.replace(/^\d+\.\s*/,''),summary,sections:sections.map(s=>{const [title,...body]=s.split('\n');return {title,body:body.join('\n').trim()};})};
  })};
}

function Body({text}:{text:string}){
  const blocks:ReactNode[]=[],lines=text.split('\n');let i=0;
  while(i<lines.length){
    const line=lines[i].trim();if(!line){i++;continue;}
    if(line.startsWith('|')){const start=i,table:string[]=[];while(i<lines.length&&lines[i].trim().startsWith('|'))table.push(lines[i++]);const [headers,...rows]=tableRows(table.join('\n'));blocks.push(<div className="method-table-wrap" key={start} tabIndex={0} role="region" aria-label={headers.join(', ')}><table><thead><tr>{headers.map(h=><th scope="col" key={h}><Inline text={h}/></th>)}</tr></thead><tbody>{rows.map((r,j)=><tr key={j}>{r.map((v,k)=><td key={k}><Inline text={v}/></td>)}</tr>)}</tbody></table></div>);continue;}
    if(/^[-*] /.test(line)){const start=i,items:string[]=[];while(i<lines.length&&/^[-*] /.test(lines[i].trim()))items.push(lines[i++].trim().slice(2));blocks.push(<ul key={start}>{items.map((v,j)=><li key={j}><Inline text={v}/></li>)}</ul>);continue;}
    const start=i,p:string[]=[];while(i<lines.length&&lines[i].trim()&&!/^(\||[-*] )/.test(lines[i].trim()))p.push(lines[i++].trim());blocks.push(<p key={start}><Inline text={p.join(' ')}/></p>);
  }
  return <>{blocks}</>;
}

function Reading({section,className=''}:{section:Section;className?:string}){
  return <section className={`method-reading ${className}`}><h3>{section.title}</h3><Body text={section.body}/></section>;
}
function More({section}:{section:Section}){
  return <details className="method-disclosure"><summary>{section.title}<span aria-hidden="true"/></summary><div><Body text={section.body}/></div></details>;
}
function take(chapter:Chapter,title:string):Section {
  return chapter.sections.find(s=>s.title===title)||{title,body:''};
}
function DataChapter({chapter}:{chapter:Chapter}){
  const [headers,...sources]=tableRows(take(chapter,'Data sources').body);
  return <><section className="method-source-ledger" aria-label="Data sources"><div className="method-source-labels" aria-hidden="true">{headers.map(h=><span key={h}>{h}</span>)}</div>{sources.map(([source,role,timing])=><div className="method-source-row" key={source}><h3>{source}</h3><p>{role}</p><span><span className="sr-only">Refresh checks: </span>{timing}</span></div>)}</section><div className="method-evidence-split"><Reading section={take(chapter,'Reported figures')}/><Reading section={take(chapter,'Estimated exposures')}/></div><More section={take(chapter,'Data quality & timing')}/><a className="method-related" href="/data">Inspect current data and sources <span aria-hidden="true">↗</span></a></>;
}
function ChannelExplorer({section}:{section:Section}){
  const [choice,setChoice]=useState(1),rows=tableRows(section.body).slice(1),selected=rows[choice]||rows[0];
  return <section className="method-channels" aria-label="Explore policy transmission channels"><div className="method-channel-options" role="group" aria-label="Transmission channel">{rows.map(([name],i)=><button key={name} type="button" aria-pressed={i===choice} onClick={()=>setChoice(i)}>{name}</button>)}</div>{selected&&<div className="method-channel-detail" key={selected[0]}><h3>{selected[0]}</h3><p>{selected[1]}</p><div><span>Example policies</span><p>{selected[2]}</p></div></div>}</section>;
}
function TransmissionChapter({chapter}:{chapter:Chapter}){
  return <><ChannelExplorer section={take(chapter,'Transmission channels')}/><Reading section={take(chapter,'Company scope')} className="method-scope"/><More section={take(chapter,'Assumptions & responses')}/><More section={take(chapter,'Consumer spending')}/></>;
}
function EarningsChapter({chapter}:{chapter:Chapter}){
  const example=take(chapter,'An illustrative calculation'),rows=tableRows(example.body).slice(1),valuation=tableRows(take(chapter,'Valuation rules').body).slice(1);
  return <><section className="method-example"><div className="method-example-header"><h3>{example.title}</h3><span>USD millions, except per-share figures</span></div><ol className="method-calculation">{rows.map(([step,calculation,result],i)=><li key={step}><span className="method-calc-step">{step}</span><span className="method-calc-formula">{calculation}</span><strong className={i===0?'method-cost':'method-decrease'}>{result}</strong></li>)}</ol><p className="method-example-note">{take(chapter,'Example assumptions').body}</p></section><section className="method-valuation"><h3>Value depends on duration</h3><dl>{valuation.map(([duration,rule])=><div key={duration}><dt>{duration}</dt><dd>{rule}</dd></div>)}</dl></section><Reading section={take(chapter,'Earnings can stay unchanged')} className="method-scope"/><More section={take(chapter,'Accounting details')}/></>;
}
function RangesChapter({chapter}:{chapter:Chapter}){
  return <><div className="method-range-flow" aria-label="Input ranges are tested one driver at a time and oriented for each company"><div><span>Start with</span><strong>Low / base / high inputs</strong></div><span aria-hidden="true">→</span><div><span>Test</span><strong>One driver at a time</strong></div><span aria-hidden="true">→</span><div><span>Build</span><strong>Company downside / upside</strong></div></div><div className="method-evidence-split"><Reading section={take(chapter,'One driver at a time')}/><Reading section={take(chapter,'Company-specific bounds')}/></div><Reading section={take(chapter,'What the range means')} className="method-scope"/><More section={take(chapter,'Comparing companies')}/></>;
}
function ValidationChapter({chapter}:{chapter:Chapter}){
  return <><div className="method-validation-split"><Reading section={take(chapter,'Policy checks')}/><Reading section={take(chapter,'Historical comparisons')}/></div><Reading section={take(chapter,'Interpreting backtests')} className="method-scope"/><More section={take(chapter,'Model boundaries')}/><a className="method-related" href="/backtests">Review historical comparisons <span aria-hidden="true">↗</span></a></>;
}
const panels=[DataChapter,TransmissionChapter,EarningsChapter,RangesChapter,ValidationChapter];

/** Teach one modeling stage at a time; the Markdown remains the content source. */
export function MethodologyDocument({text}:{text:string}){
  const doc=useMemo(()=>parseDocument(text),[text]),[active,setActive]=useState(0),tabs=useRef<HTMLDivElement>(null),panel=useRef<HTMLElement>(null);
  const step=steps[active],chapter=doc.chapters[active],Panel=panels[active];
  function selectChapter(next:number){
    setActive(next);
    if(panel.current&&panel.current.getBoundingClientRect().top<0)panel.current.scrollIntoView({block:'start'});
  }
  function onKeys(event:KeyboardEvent<HTMLDivElement>){
    const keys=['ArrowRight','ArrowDown','ArrowLeft','ArrowUp','Home','End'];if(!keys.includes(event.key))return;
    event.preventDefault();const next=event.key==='Home'?0:event.key==='End'?steps.length-1:(active+(event.key==='ArrowLeft'||event.key==='ArrowUp'?-1:1)+steps.length)%steps.length;
    selectChapter(next);tabs.current?.querySelectorAll<HTMLButtonElement>('[role=tab]')[next].focus();
  }
  function advance(next:number){selectChapter(next);tabs.current?.querySelectorAll<HTMLButtonElement>('[role=tab]')[next].focus();}
  return <div className="methodology-guide"><header className="methodology-header"><h1>Methodology</h1><p>{doc.intro}</p></header><div className="method-overview" aria-label="Modeling process"><div><strong>Company data</strong><span>Filings, prices & economic data</span></div><span aria-hidden="true">→</span><div><strong>Policy × company exposure</strong><span>Covered business & response assumptions</span></div><span aria-hidden="true">→</span><div><strong>Earnings & equity value</strong><span>Financial changes & scenario ranges</span></div></div><div className="methodology-layout"><div className="methodology-navigation" ref={tabs} role="tablist" aria-label="Methodology chapters" onKeyDown={onKeys}>{steps.map((s,i)=><button key={s.id} type="button" id={`method-tab-${s.id}`} role="tab" aria-selected={active===i} aria-controls={`method-panel-${s.id}`} tabIndex={active===i?0:-1} onClick={()=>selectChapter(i)}><span className="method-step-number" aria-hidden="true">{String(i+1).padStart(2,'0')}</span><span><strong>{s.label}</strong><small>{s.hint}</small></span><span className="method-step-arrow" aria-hidden="true">↗</span></button>)}</div><section ref={panel} className="methodology-panel" role="tabpanel" id={`method-panel-${step.id}`} aria-labelledby={`method-tab-${step.id}`} tabIndex={0}><header className="method-panel-header"><span aria-hidden="true">{String(active+1).padStart(2,'0')}</span><div><h2>{chapter?.title||step.label}</h2><p>{chapter?.summary}</p></div></header><div className="method-panel-content" key={step.id}>{chapter&&<Panel chapter={chapter}/>}</div><footer className="method-chapter-footer"><span>{active+1} / {steps.length}</span><div>{active>0&&<button type="button" className="method-previous" onClick={()=>advance(active-1)}>← Previous</button>}{active<steps.length-1?<button type="button" className="method-next" onClick={()=>advance(active+1)}>{steps[active+1].label} <span aria-hidden="true">→</span></button>:<a className="method-next" href="/">Run a policy scenario <span aria-hidden="true">↗</span></a>}</div></footer></section>{steps.filter(s=>s.id!==step.id).map(s=><section key={s.id} role="tabpanel" id={`method-panel-${s.id}`} aria-labelledby={`method-tab-${s.id}`} hidden/>)}</div></div>;
}
