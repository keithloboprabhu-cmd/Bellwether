/** Value-only policies must remain visible without fabricating earnings effects. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {preferredMetric,impactValue,impactBounds,neutralImpactLabel} from './impact.ts';
import type {Company,Result} from './types';
const company={eps:0,dNI:0,value:-.04,low:0,high:0,value_low:-.08,value_high:-.02} as Company;
const result=(type:string,companies=[company])=>({policy:{channels:[{type}]},companies}) as Result;
test('CET1 and cash-tax timing default to valuation, including missing quotes',()=>{
 for(const type of ['bank_capital','tax_timing','reit_nav']){
  assert.equal(preferredMetric(result(type)),'value');
  assert.equal(preferredMetric(result(type,[{...company,value:null}])),'value');
 }
});
test('price axis uses valuation bounds and keeps real EPS unchanged',()=>{
 assert.equal(impactValue(company,'value'),-.04);
 assert.deepEqual(impactBounds(company,'value'),[-.08,-.02]);
 assert.equal(impactValue(company,'eps'),0);
 assert.deepEqual(impactBounds(company,'eps'),[0,0]);
});
test('earnings policies retain earnings axis and unavailable valuation remains missing',()=>{
 assert.equal(preferredMetric(result('price',[{...company,eps:-.02,dNI:-1}])),'eps');
 assert.equal(impactValue({...company,value:null},'value'),null);
 assert.deepEqual(impactBounds({...company,value_low:undefined,value_high:undefined},'value'),[null,null]);
});
test('zero labels distinguish business scope, data gaps and valuation effects',()=>{
 assert.equal(neutralImpactLabel({...company,coverage:{status:'outside_scope',reason:'Insurer, not an insured bank'}},'eps'),'Out of scope');
 assert.equal(neutralImpactLabel({...company,coverage:{status:'unquantified',reason:'No qualifying base'}},'eps'),'No estimate');
 assert.equal(neutralImpactLabel({...company,coverage:{status:'value_only',reason:'CET1'}},'eps'),'Value only');
 assert.equal(neutralImpactLabel({...company,coverage:{status:'nonbinding',reason:'Cap above fee'}},'eps'),'Not binding');
});
