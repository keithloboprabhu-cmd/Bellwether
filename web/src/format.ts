/** Shared model-unit formatting: percentage inputs differ from fractional outputs. */
/** Show calendar dates without timezone shifts, and timestamps in the viewer's local time. */
export function observationDate(value:string|null|undefined,missing='—'):string {
  if(!value)return missing;
  const parsed=new Date(value);
  if(!Number.isFinite(parsed.getTime()))return missing;
  const calendarOnly=/^\d{4}-\d{2}-\d{2}$/.test(value);
  return parsed.toLocaleString('en-US',{year:'numeric',month:'short',day:'numeric',...(calendarOnly?{timeZone:'UTC'}:{hour:'numeric',minute:'2-digit',timeZoneName:'short'})});
}
/** Semantic sign without equating missing values with zero. */
export const signClass = (n:number|null) => n === null ? 'missing' : n > 0 ? 'gain' : n < 0 ? 'loss' : 'neutral';
const sign = (n:number) => n < 0 ? '−' : n > 0 ? '+' : '';
/** Convert fractional model output to a signed, readable percentage. */
export function percent(n:number|null, signed=true):string {
  if (n === null || !Number.isFinite(n)) return '—';
  if (n === 0) return '0.0%';
  return (signed ? sign(n) : n < 0 ? '−' : '') + (Math.abs(n) < .001 ? '<0.1%' : `${(Math.abs(n)*100).toFixed(1)}%`);
}
/** Display model dollars in millions using explicit M/B/T suffixes. */
export function money(n:number|null):string {
  if(n===null || !Number.isFinite(n)) return '—';
  const a=Math.abs(n), scale=a>=1e6?1e6:a>=1e3?1e3:1;
  return `${sign(n)}$${(a/scale).toLocaleString('en-US',{maximumFractionDigits:1})}${scale===1e6?'T':scale===1e3?'B':'M'}`;
}
/** Display an already-converted basis-point margin change. */
export function bps(n:number|null):string {
  if(n===null || !Number.isFinite(n)) return '—';
  return `${sign(n)}${Math.abs(n)<.1 && n!==0?'<0.1':Math.abs(n).toLocaleString('en-US',{maximumFractionDigits:1})} bps`;
}
/** Retain the policy configuration's own input units. */
export function inputValue(n:number,unit:string):string {
  if(unit==='fraction') return percent(n,false);
  return `${n.toLocaleString('en-US',{maximumFractionDigits:4}).replace('-','−')} ${unit==='percent'?'%':unit}`;
}
/** Quote CSV fields and neutralize executable spreadsheet formula strings. */
export function csvCell(value:unknown):string {
  let s=value===null||value===undefined?'':String(value);
  if(/^[=+@\t\r]/.test(s) || /^-\D/.test(s)) s="'"+s;
  return `"${s.replaceAll('"','""')}"`;
}
