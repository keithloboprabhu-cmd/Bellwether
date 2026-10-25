/** Dense simulation panels built only from returned engine values and filed history. */
import {useEffect,useState} from 'react';
import type {Catalog,Company,Projection,Result} from './types';
import {Field} from './FieldView';
import {bps,inputValue,money,percent,signClass} from './format';

/** Dollar/share formatting never reuses the engine's millions-of-dollars formatter. */
export function dollars(n:number|null,signed=false):string {
  if(n===null||!Number.isFinite(n))return '—';
  return `${n<0?'−':signed&&n>0?'+':''}$${Math.abs(n).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}`;
}
const amount=(n:number|null)=>money(n).replace(/^\+/,'');
const ticker=(c:Company)=>c.display_ticker||c.id;

/** Actual request state and elapsed time; no invented stages or progress percentage. */
export function ExecutionTrace({busy,ready,error}:{busy:boolean;ready:boolean;error:boolean}){
  const [elapsed,setElapsed]=useState(0);
  useEffect(()=>{if(!busy)return;const start=Date.now();setElapsed(0);const t=setInterval(()=>setElapsed((Date.now()-start)/1000),100);return()=>clearInterval(t);},[busy]);
  return <div className={`execution-trace ${busy?'is-running':''}`} role="status"><span className="signal-dot"/><span>{error?'Request failed':busy?'Engine request pending':ready?'Result loaded':'Awaiting command'}</span>{busy&&<time>{elapsed.toFixed(1)}s</time>}<span className="execution-line"/></div>;
}

/** Compact model totals retain the engine's sample/company aggregation semantics. */
export function MetricStrip({result}:{result:Result}){
  const metrics=[[result.mode==='company'?'Company EPS Δ':'Sample earnings Δ',percent(result.totals.d_eps_pct),result.totals.d_eps_pct],['Net-income change',money(result.totals.d_ni),result.totals.d_ni],['Revenue change',money(result.totals.d_revenue),result.totals.d_revenue],['Margin change',bps(result.totals.d_margin_bps),result.totals.d_margin_bps],['Implied value change',money(result.totals.d_mcap),result.totals.d_mcap]] as const;
  return <div className="metric-strip">{metrics.map(([label,value,number],i)=><div key={label}><span>{label}</span><strong className={signClass(number)}>{value}</strong>{i===0&&<small>{percent(result.range[0])} / {percent(result.range[1])} bounds</small>}</div>)}</div>;
}

/** Annual filed EPS history, preserving missing observations as separate segments. */
export function Sparkline({company}:{company:Company}){
  const h=company.history,valid=h.filter(p=>p.eps!==null);
  if(valid.length<2)return <span className="no-history">No history</span>;
  const lo=Math.min(...valid.map(p=>p.eps!)),hi=Math.max(...valid.map(p=>p.eps!)),span=hi-lo||1;
  let segments:string[]=[],segment:string[]=[];
  h.forEach((p,i)=>{if(p.eps===null){if(segment.length)segments.push(segment.join(' '));segment=[];}else segment.push(`${3+i/(h.length-1)*76},${23-(p.eps-lo)/span*19}`);});
  if(segment.length)segments.push(segment.join(' '));
  return <svg className="eps-sparkline" viewBox="0 0 82 28" role="img" aria-label={`${company.name}: filed EPS history, ${h.map(p=>`${p.year}: ${p.eps===null?'unavailable':dollars(p.eps)}`).join('; ')}`}><line x1="2" x2="80" y1="25" y2="25" className="plot-grid"/>{segments.map((s,i)=><polyline key={i} points={s} className="spark-path"/>)}</svg>;
}

/** Inline scenario whisker uses an explicitly shared, symmetric output scale. */
function Interval({company,extent}:{company:Company;extent:number}){
  const c=company,x=(v:number)=>50+v/extent*46;
  return <div className="interval-cell"><svg viewBox="0 0 124 22" aria-hidden="true"><line x1="62" x2="62" y1="2" y2="20" className="plot-zero"/>{c.low!==null&&c.high!==null&&<><line x1={x(c.low)*1.24} x2={x(c.high)*1.24} y1="11" y2="11" className="interval-line"/><path d={`M${x(c.low)*1.24} 6v10 M${x(c.high)*1.24} 6v10`} className="interval-line"/></>}{c.eps!==null&&<circle cx={x(c.eps)*1.24} cy="11" r="3" className="interval-dot"/>}</svg><small>{percent(c.low)} / {percent(c.high)}</small></div>;
}

/** A real policy exposure on X and modeled EPS change on Y, linked to selection. */
function ExposurePlot({result,catalog,selected,onSelect}:{result:Result;catalog:Catalog;selected:string|null;onSelect:(id:string)=>void}){
  const [key,setKey]=useState(result.policy.exposure_keys[0]||'');
  const actual=result.policy.exposure_keys.includes(key)?key:result.policy.exposure_keys[0];
  const def=catalog.exposure_definitions[actual];
  const points=result.companies.flatMap(c=>{const e=c.exposures.find(e=>e.key===actual);return e&&e.applicable!==false&&c.eps!==null?[{c,x:e.value!,y:c.eps}]:[];});
  const xmin=Math.min(0,...points.map(p=>p.x)),xmax=Math.max(.001,...points.map(p=>p.x));
  const ymax=Math.max(.01,...points.map(p=>Math.abs(p.y)))*1.15;
  const x=(v:number)=>44+(v-xmin)/(xmax-xmin)*258,y=(v:number)=>110-v/ymax*82;
  const xv=(v:number)=>def?inputValue(v,def.unit).replace('usd_m','$M'):String(v);
  return <section className="hud-panel exposure-plot"><div className="panel-header"><h2>Exposure / impact</h2><span>{points.length}/{result.companies.length}</span></div>{def?<><label className="plot-key"><span className="sr-only">Scatter plot exposure</span><select value={actual} onChange={e=>setKey(e.target.value)}>{result.policy.exposure_keys.map(k=><option key={k} value={k}>{catalog.exposure_definitions[k].label}</option>)}</select></label><div className="scatter-surface"><svg viewBox="0 0 330 224" role="img" aria-label={`Exposure scatter: ${def.label} against EPS change. Exact values in company inspection and telemetry.`}>{[-1,0,1].map(t=><g key={t}><line x1="44" x2="306" y1={y(t*ymax)} y2={y(t*ymax)} className={t===0?'plot-zero':'plot-grid'}/><text x="38" y={y(t*ymax)+4} textAnchor="end">{percent(t*ymax,false)}</text></g>)}{[0,.5,1].map(t=><g key={t}><line x1={44+t*258} x2={44+t*258} y1="28" y2="192" className="plot-grid"/><text x={44+t*258} y="210" textAnchor="middle">{xv(xmin+t*(xmax-xmin))}</text></g>)}<text x="44" y="15">ΔEPS %</text>{points.map(({c,x:ex,y:ey})=><g key={c.id} className={signClass(c.eps)}><circle cx={x(ex)} cy={y(ey)} r={selected===c.id?6:3.8} className={selected===c.id?'scatter-dot selected':'scatter-dot'} onClick={()=>onSelect(c.id)}><title>{ticker(c)}: {xv(ex)}, EPS {percent(ey)}</title></circle>{selected===c.id&&<text x={Math.min(275,x(ex)+9)} y={y(ey)-8} className="scatter-label">{ticker(c)}</text>}</g>)}</svg></div><p className="panel-note">X: {def.unit==='fraction'?'Exposure (%)':`Exposure (${def.unit.replace('usd_m','$M')})`} · Y: ΔEPS · select via grid or inspector{points.length<result.companies.length?` · ${result.companies.length-points.length} undefined / N/A`:''}</p></>:<p className="panel-empty">This policy has no company exposure axis.</p>}</section>;
}

/** Selected-company data and provenance remain adjacent to both visualization panels. */
function Inspector({result,selected,onSelect}:{result:Result;selected:string|null;onSelect:(id:string)=>void}){
  const c=result.companies.find(c=>c.id===selected)||result.companies.find(c=>c.is_custom)||result.companies[0];
  const m=c.metrics;
  return <section className="hud-panel entity-inspector"><div className="panel-header"><h2>Company inspector</h2><span>{c.is_custom?'Custom':'Reference'}</span></div><label className="entity-picker"><span className="sr-only">Inspect company</span><select value={c.id} onChange={e=>onSelect(e.target.value)}>{result.companies.map(c=><option key={c.id} value={c.id}>{ticker(c)} / {c.name}</option>)}</select></label><p className="entity-name">{c.name}</p><div className="inspector-headline"><strong className={signClass(c.eps)}>{percent(c.eps)}</strong><span>ΔEPS<br/>{dollars(c.dEPS,true)}</span></div><dl className="inspector-facts"><div><dt>Projected EPS</dt><dd>{dollars(m.eps.projected)}</dd></div><div><dt>Model NI</dt><dd>{amount(m.net_income.projected)}</dd></div><div><dt>Scenario bounds</dt><dd>{percent(c.low)} / {percent(c.high)}</dd></div><div><dt>Fiscal year / price date</dt><dd>{c.baseline.fiscal_year||'User'} / {c.baseline.price_date||'—'}</dd></div></dl><p className="entity-driver">{c.reason}</p><div className="inspector-links">{c.baseline.filing_url&&<a href={c.baseline.filing_url} target="_blank" rel="noreferrer">SEC filing ↗</a>}<span>{c.exposures.some(e=>e.source==='estimate')?'Exposure estimates':'Configured exposures'}</span></div></section>;
}

/** The Field, exposure scatter and linked inspector form the operational overview. */
export function Overview({result,catalog,selected,onSelect}:{result:Result;catalog:Catalog;selected:string|null;onSelect:(id:string|null)=>void}){
  const [pane,setPane]=useState('field');
  return <><div className="mobile-overview-tabs" aria-label="Overview panels">{['field','exposure','company'].map(p=><button key={p} aria-pressed={pane===p} onClick={()=>setPane(p)}>{p==='field'?'The Field':p==='exposure'?'Exposure plot':'Company inspector'}</button>)}</div><div className="analysis-deck" data-pane={pane}><Field companies={result.companies} selected={selected} onSelect={onSelect}/><ExposurePlot result={result} catalog={catalog} selected={selected} onSelect={onSelect}/><Inspector result={result} selected={selected} onSelect={onSelect}/></div></>;
}

/** High-density, sortable financial grid pairs absolute projections with percent changes. */
export function TelemetryGrid({companies,selected,onSelect}:{companies:Company[];selected:string|null;onSelect:(id:string)=>void}){
  const [query,setQuery]=useState(''),[sort,setSort]=useState('impact'),[affected,setAffected]=useState(false);
  const rows=companies.filter(c=>(!affected||c.dNI!==0||c.revenue!==0||(c.value!==null&&c.value!==0))&&`${c.name} ${ticker(c)}`.toLowerCase().includes(query.toLowerCase())).sort((a,b)=>sort==='name'?ticker(a).localeCompare(ticker(b)):sort==='ni'?Math.abs(b.dNI)-Math.abs(a.dNI):Math.abs(b.eps??0)-Math.abs(a.eps??0));
  const extent=Math.max(.01,...companies.flatMap(c=>[Math.abs(c.low??0),Math.abs(c.high??0),Math.abs(c.eps??0)]));
  return <section className="telemetry-panel"><div className="telemetry-toolbar"><h2>Impact telemetry <span>{rows.length}/{companies.length}</span></h2><div><label><span className="sr-only">Filter companies</span><input type="search" placeholder="Filter ticker / company" value={query} onChange={e=>setQuery(e.target.value)}/></label><label className="check-label"><input type="checkbox" checked={affected} onChange={e=>setAffected(e.target.checked)}/>Affected only</label><label><span className="sr-only">Sort telemetry</span><select value={sort} onChange={e=>setSort(e.target.value)}><option value="impact">Sort: absolute EPS %</option><option value="ni">Sort: absolute ΔNI</option><option value="name">Sort: ticker A–Z</option></select></label></div></div><div className="telemetry-scroll" tabIndex={0} role="region" aria-label="Financial impact telemetry; scroll for all columns and companies"><table className="telemetry-table"><caption className="sr-only">Projected values and changes. EPS starts from reported EPS; net income starts from model baseline. Bounds are scenarios, not confidence intervals.</caption><thead><tr className="column-groups"><th rowSpan={2} scope="col">Company</th><th rowSpan={2} scope="col">Filed EPS<br/>annual history</th><th colSpan={3} scope="colgroup">EPS · $/share</th><th rowSpan={2} scope="col">Scenario bounds<br/>ΔEPS %</th><th colSpan={2} scope="colgroup">Revenue</th><th colSpan={2} scope="colgroup">Model net income</th><th colSpan={2} scope="colgroup">Implied share price</th></tr><tr><th scope="col">Projected</th><th scope="col">Δ $/share</th><th scope="col">Δ %</th><th scope="col">Projected</th><th scope="col">Δ %</th><th scope="col">Projected</th><th scope="col">Δ %</th><th scope="col">Projected</th><th scope="col">Δ %</th></tr></thead><tbody>{rows.map(c=><tr key={c.id} className={`${selected===c.id?'selected-row':''} ${c.is_custom?'custom-row':''}`}><th scope="row"><button className="company-button" onClick={()=>onSelect(c.id)} aria-pressed={selected===c.id} title={c.name}><strong>{ticker(c)}{c.is_custom&&<span className="custom-marker"> □</span>}</strong><small>{c.name}</small></button></th><td><Sparkline company={c}/></td><td>{dollars(c.metrics.eps.projected)}</td><td className={signClass(c.dEPS)}>{dollars(c.dEPS,true)}</td><td className={signClass(c.eps)}>{percent(c.eps)}</td><td className={signClass(c.eps)}><Interval company={c} extent={extent}/></td><td>{amount(c.metrics.revenue.projected)}</td><td className={signClass(c.metrics.revenue.percent)}>{percent(c.metrics.revenue.percent)}</td><td>{amount(c.metrics.net_income.projected)}</td><td className={signClass(c.metrics.net_income.percent)}>{percent(c.metrics.net_income.percent)}</td><td>{dollars(c.metrics.price.projected)}</td><td className={signClass(c.value)}>{percent(c.value)}</td></tr>)}</tbody></table>{rows.length===0&&<div className="panel-empty">No companies match. Clear the filter or turn off “Affected only”.</div>}</div><div className="grid-footnote"><span>Projected = starting value + modeled Δ · M/B = million/billion USD</span><span>EPS: reported base · NI: model base · price: channel persistence · — undefined</span></div></section>;
}

/** Compact, exact channel attribution and one-driver sensitivity variance bars. */
export function DriverPanels({result}:{result:Result}){
  const extent=Math.max(.001,...result.tornado.flatMap(t=>[Math.abs(t.result_low_input),Math.abs(t.result_high_input)]));
  const format=(n:number)=>result.tornado_metric==='d_eps'?dollars(n,true):percent(n);
  const maxChannel=Math.max(1,...result.channels.map(c=>Math.abs(c.dNI)));
  return <div className="driver-panels"><section className="hud-panel"><div className="panel-header"><h2>Channel attribution</h2><span>ΔNI</span></div>{result.channels.map(c=><div className="channel-row" key={c.label}><span>{c.label}</span><strong className={signClass(c.dNI)}>{money(c.dNI)}</strong><i className={signClass(c.dNI)} style={{width:`${Math.abs(c.dNI)/maxChannel*100}%`}}/></div>)}</section><section className="hud-panel"><div className="panel-header"><h2>One-driver sensitivity</h2><span>{result.tornado_metric==='d_eps'?'ΔEPS $':'Output %'}</span></div><p className="panel-note">One driver low → high; others held at base.</p>{result.tornado.map(t=>{const a=t.result_low_input,b=t.result_high_input;return <div className="variance-row" key={t.key}><span>{t.label}</span><div className="variance-track"><i style={{left:`${50+Math.min(a,b)/extent*48}%`,width:`${Math.max(.4,Math.abs(b-a)/extent*48)}%`}}/></div><strong>{format(a)} / {format(b)}</strong></div>;})}</section></div>;
}

/** Initial console exposes actual universe coverage while awaiting a command. */
export function Standby({catalog,industry,onIndustry}:{catalog:Catalog;industry:string;onIndustry:(id:string)=>void}){
  const ind=catalog.industries.find(i=>i.id===industry);
  return <div className="standby-deck"><div className="standby-field"><Field illustrative/><div className="standby-overlay"><span className="reticle"/><h2>Awaiting simulation</h2><p>Select industry / policy / parameters</p><span>{catalog.company_count} issuers / {catalog.industries.length} industries</span></div></div><section className="hud-panel universe-panel"><div className="panel-header"><h2>{ind?'Selected universe':'Industry universe'}</h2><span>{ind?.count||catalog.company_count}</span></div>{ind?<><h3>{ind.name}</h3><div className="universe-tickers">{ind.companies.map(c=><span key={c.ticker} title={c.name}>{c.ticker}</span>)}</div><p className="panel-note">SEC annual filings · policy exposures may be estimates</p></>:catalog.industries.map(i=><button className="universe-row" key={i.id} onClick={()=>onIndustry(i.id)}><span>{i.name}</span><strong>{i.count}</strong></button>)}</section></div>;
}
