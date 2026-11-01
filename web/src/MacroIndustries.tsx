/** Compare all industry aggregates before drilling into their underlying companies. */
import type {IndustryImpact,Result} from './types';
import type {ImpactMetric} from './impact';
import {csvCell,money,percent,signClass} from './format';

export function MacroIndustries({result,metric,selected,onSelect}:{result:Result;metric:ImpactMetric;selected:string;onSelect:(id:string)=>void}){
  const value=(i:IndustryImpact)=>i.totals[metric==='value'?'d_mcap_pct':'d_eps_pct'];
  const industries=[...(result.industries||[])].sort((a,b)=>(value(b)??-Infinity)-(value(a)??-Infinity));
  const extent=Math.max(.001,...industries.map(i=>Math.abs(value(i)??0)));
  const label=metric==='value'?'Implied value change':'Earnings change';
  function exportIndustries(){
    const header=['Industry','Companies','Affected companies','Unquantified companies','Unavailable valuations','Revenue baseline ($M)','Revenue projected ($M)','Revenue delta ($M)','Revenue change (fraction)','Model NI baseline ($M)','Model NI projected ($M)','NI delta ($M)','Earnings change (fraction)','Market value delta ($M)','Market value change (fraction)','Macro policy','Inputs','Model version','Data version'];
    const rows=[header,...industries.map(i=>[i.name,i.count,i.affected,i.unquantified,i.valuation_unavailable,i.totals.revenue,(i.totals.revenue??0)+(i.totals.d_revenue??0),i.totals.d_revenue,i.totals.d_revenue_pct,i.net_income_baseline,i.net_income_projected,i.totals.d_ni,i.totals.d_eps_pct,i.totals.d_mcap,i.totals.d_mcap_pct,result.policy.id,JSON.stringify(result.inputs),result.versions.model,result.versions.data])];
    const url=URL.createObjectURL(new Blob([rows.map(r=>r.map(csvCell).join(',')).join('\r\n')],{type:'text/csv;charset=utf-8'}));
    const link=document.createElement('a');link.href=url;link.download=`bellwether-${result.policy.id}-industries.csv`;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
  }
  return <section className="macro-industries hud-panel" aria-label="Macro impact across industries">
    <div className="panel-header"><h2>Industry impact</h2><span>{industries.length} industries / {result.companies.length} companies</span><button className="text-button" onClick={exportIndustries}>Industry CSV ↓</button></div>
    <div className="macro-comparison">
      <div className="macro-bars" aria-label={`${label} by industry, ranked highest to lowest`}>
        <div className="macro-chart-heading"><span>{label}</span><span>− / +</span></div>
        {industries.map(i=>{const v=value(i),size=Math.abs(v??0)/extent*50;return <button key={i.id} className={`macro-bar-row ${selected===i.id?'is-selected':''}`} aria-pressed={selected===i.id} onClick={()=>onSelect(i.id)} title={i.reason}><span>{i.name}</span><span className="macro-bar-track" aria-hidden="true"><i className={signClass(v)} style={{left:`${v!==null&&v<0?50-size:50}%`,width:`${size}%`}}/></span><strong className={signClass(v)}>{percent(v)}</strong></button>;})}
      </div>
      <div className="macro-readout"><span className="eyebrow">Cross-industry scenario</span><h3>{result.policy.name}</h3><p>{result.policy.description}</p><label>Company drilldown<select aria-label="Macro industry drilldown" value={selected} onChange={e=>onSelect(e.target.value)}><option value="all">All industries</option>{industries.map(i=><option key={i.id} value={i.id}>{i.name}</option>)}</select></label><p className="panel-note">Industry earnings % = total net-income change ÷ model starting earnings. Headline EPS is cap-weighted. This is the configured-company sample.</p></div>
    </div>
    <div className="table-scroll" role="region" tabIndex={0} aria-label="Industry financial impact table"><table className="macro-impact-table"><caption className="sr-only">Projected industry revenue and model earnings, absolute changes and percentage changes. Select an industry to inspect its companies.</caption><thead><tr><th scope="col">Industry</th><th scope="col">Affected</th><th scope="col">Revenue after</th><th scope="col">Revenue Δ</th><th scope="col">Revenue Δ %</th><th scope="col">Model NI after</th><th scope="col">NI Δ</th><th scope="col">Earnings Δ %</th><th scope="col">Value Δ</th><th scope="col">Value Δ %</th></tr></thead><tbody>{industries.map(i=><tr key={i.id} className={selected===i.id?'selected-row':''}><th scope="row"><button className="company-button" aria-pressed={selected===i.id} onClick={()=>onSelect(i.id)}><strong>{i.name}</strong><small>{[i.unquantified?`${i.unquantified} unquantified`:'',i.valuation_unavailable?`${i.valuation_unavailable} valuations unavailable`:''].filter(Boolean).join(' · ')}</small></button></th><td>{i.affected}/{i.count}</td><td>{money((i.totals.revenue??0)+(i.totals.d_revenue??0))}</td><td className={signClass(i.totals.d_revenue)}>{money(i.totals.d_revenue)}</td><td className={signClass(i.totals.d_revenue_pct)}>{percent(i.totals.d_revenue_pct)}</td><td>{money(i.net_income_projected)}</td><td className={signClass(i.totals.d_ni)}>{money(i.totals.d_ni)}</td><td className={signClass(i.totals.d_eps_pct)}>{percent(i.totals.d_eps_pct)}</td><td className={signClass(i.totals.d_mcap)}>{money(i.totals.d_mcap)}</td><td className={signClass(i.totals.d_mcap_pct)}>{percent(i.totals.d_mcap_pct)}</td></tr>)}</tbody></table></div>
    <p className="panel-note macro-coverage-note">Value totals include available valuations only; unavailable companies are counted above. Unquantified effects are not measured zeros. Macro transmission includes estimated assumptions.</p>
  </section>;
}
