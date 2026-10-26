/** Select one explicitly labeled impact axis without changing engine earnings. */
import type {Company,Result} from './types';

export type ImpactMetric = 'eps'|'value';
export const impactLabel=(metric:ImpactMetric)=>metric==='value'?'Implied price Δ':'EPS Δ';
export const impactValue=(company:Company,metric:ImpactMetric)=>metric==='value'?company.value:company.eps;
export const impactBounds=(company:Company,metric:ImpactMetric):[number|null,number|null]=>metric==='value'?[company.value_low??null,company.value_high??null]:[company.low,company.high];

/** Distinguish a policy boundary or missing estimate from a calculated zero. */
export function neutralImpactLabel(company:Company,metric:ImpactMetric):string {
  if(company.coverage?.status==='outside_scope')return 'Out of scope';
  if(company.coverage?.status==='unquantified')return 'No estimate';
  if(company.coverage?.status==='nonbinding')return 'Not binding';
  if(metric==='eps'&&company.coverage?.status==='value_only')return 'Value only';
  return impactValue(company,metric)===null?'Unavailable':'No change';
}

/** Direct valuation channels default to price even when quotes are unavailable. */
export function preferredMetric(result:Result):ImpactMetric {
  const direct=new Set(['bank_capital','tax_timing','reit_nav']);
  if(result.policy.channels?.length&&result.policy.channels.every(c=>direct.has(c.type)))return 'value';
  return result.companies.every(c=>Math.abs(c.dNI)<1e-10)&&result.companies.some(c=>c.value!==null&&Math.abs(c.value)>1e-10)?'value':'eps';
}
