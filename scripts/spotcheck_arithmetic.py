"""Independently recompute ten stratified random scenarios and show all arithmetic.

This audit-only calculator does not call run_channel, aggregate, or the valuation
helper. It reuses parsed expressions to capture the actual configured inputs,
then independently computes dollars, taxes, EPS and duration-specific value.
"""
from pathlib import Path
import json,math,random,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from policyshock.config import ROOT,load_universe
from policyshock.engine.simulate import build_runner
from policyshock.engine.expressions import evaluate
from policyshock.engine.model import BASELINE_FIELDS
from policyshock.engine.channels import CHANNELS
from policyshock.policies.loader import registry

SEED=20261031


def calculate_channel(kind: str,b: dict,p: dict) -> tuple[dict,list[str]]:
    """Independent closed-form calculation, with a written numerical working trail."""
    z=dict(R=0.,C=0.,O=0.,E=0.,I=0.,T=0.,N=0.,PV=0.,V=0.)
    R,C,cm=b['revenue'],b['cost_of_revenue'],b['contribution_margin'];steps=[]
    if kind=='cost':
        D=C*p['exposed_cost_share']*p['shock_pct']+p['dcost_musd'];dp=p['pass_through']*D/R if R else 0;dq=-p['elasticity']*dp
        z.update(R=R*((1+dp)*(1+dq)-1),C=C*p['exposed_cost_share']*p['shock_pct']*(1+dq)+C*p['variable_cost_share']*dq,O=p['dcost_musd']*(1+dq))
        z['E']=z['R']-z['C']-z['O'];steps=[f'Initial cost shock = {C:.10g} × {p["exposed_cost_share"]:.10g} × {p["shock_pct"]:.10g} + {p["dcost_musd"]:.10g} = {D:.10g}',f'Price fraction = pass-through × cost / revenue = {dp:.10g}; volume fraction = −elasticity × price fraction = {dq:.10g}',f'ΔR = R[(1+price)(1+volume)−1] = {z["R"]:.10g}; ΔC = exposed shock × (1+volume) + variable costs × volume = {z["C"]:.10g}; ΔOpex = {z["O"]:.10g}']
    elif kind=='domestic_uplift':
        z['R']=R*p['domestic_sales_share']*p['price_uplift'];z['C']=z['R']*(1-p['flow_through']);z['E']=z['R']-z['C'];steps=[f'ΔR = {R:.10g} × {p["domestic_sales_share"]:.10g} × {p["price_uplift"]:.10g} = {z["R"]:.10g}; ΔC = ΔR × (1−{p["flow_through"]:.10g}) = {z["C"]:.10g}']
    elif kind=='tax_rate':z['T']=p['d_statutory_rate']*p['domestic_income_share'];steps=[f'Δtax rate = {p["d_statutory_rate"]:.10g} × {p["domestic_income_share"]:.10g} = {z["T"]:.10g}']
    elif kind=='tax_credit':z['N']=p['credit_rate']*p['base_musd'];steps=[f'Direct after-tax ΔNI = {p["credit_rate"]:.10g} × {p["base_musd"]:.10g} = {z["N"]:.10g}']
    elif kind=='tax_revenue':z['O']=R*p['in_scope_share']*p['rate'];z['E']=-z['O'];steps=[f'Tax expense = {R:.10g} × {p["in_scope_share"]:.10g} × {p["rate"]:.10g} = {z["O"]:.10g}']
    elif kind=='tax_timing':
        X=p['capex_musd']*p['expensed_share'];n=int(p['recovery_years']);af=sum((1+p['discount_rate'])**(-k) for k in range(1,n+1));z['PV']=p['statutory_rate']*X*(1-af/n);steps=[f'Eligible capex = {X:.10g}; AF({n},{p["discount_rate"]}) = {af:.10g}; direct value = tax × capex × (1−AF/n) = {z["PV"]:.10g}; GAAP ΔNI = 0']
    elif kind in ('demand_volume','demand_price','demand_transfer'):
        if kind=='demand_volume':z['R']=R*p['exposed_revenue_share']*p['d_volume'];steps=[f'ΔR = {R:.10g} × {p["exposed_revenue_share"]:.10g} × {p["d_volume"]:.10g} = {z["R"]:.10g}']
        elif kind=='demand_price':z['R']=R*p['exposed_revenue_share']*(-p['elasticity']*p['dp_consumer']);steps=[f'ΔR = R × share × (−elasticity × price) = {z["R"]:.10g}']
        else:z['R']=p['total_transfer_musd']*p['mpc']*p['capture_share']*p['tilt'];steps=[f'ΔR = {p["total_transfer_musd"]:.10g} × {p["mpc"]:.10g} × {p["capture_share"]:.10g} × {p["tilt"]:.10g} = {z["R"]:.10g}']
        z['E']=z['R']*cm;steps.append(f'ΔEBIT = ΔR × contribution margin {cm:.10g} = {z["E"]:.10g}')
    elif kind=='price':z['R']=R*p['exposed_revenue_share']*p['d_price'];z['E']=z['R']*(1-p['offset_share']);steps=[f'ΔR = {R:.10g} × {p["exposed_revenue_share"]:.10g} × {p["d_price"]:.10g} = {z["R"]:.10g}; ΔEBIT = ΔR × (1−{p["offset_share"]:.10g}) = {z["E"]:.10g}']
    elif kind=='financing_debt':z['I']=(b.get('total_debt') or 0)*min(1,p['floating_share']+p['maturing_share'])*p['d_rate_bps']/10000;steps=[f'Δinterest = debt × min(1,floating+maturing) × bps/10,000 = {z["I"]:.10g}']
    elif kind=='bank_nii':z['R']=z['E']=(b.get('net_interest_income') or 0)*p['nii_sensitivity_per_100bp']*p['d_rate_bps']/100;steps=[f'ΔNII = {b.get("net_interest_income"):.10g} × {p["nii_sensitivity_per_100bp"]:.10g} × {p["d_rate_bps"]:.10g}/100 = {z["R"]:.10g}; ΔEBIT = ΔNII']
    elif kind=='bank_capital':z['V']=(p['cet1_ratio']/(p['cet1_ratio']+p['d_ratio'])-1)*(1-p['mm_offset']);steps=[f'Direct equity fraction = [{p["cet1_ratio"]:.10g}/({p["cet1_ratio"]:.10g}+{p["d_ratio"]:.10g})−1] × (1−{p["mm_offset"]:.10g}) = {z["V"]:.10g}; ΔNI=0']
    elif kind=='reit_nav':z['V']=-p['cap_rate_beta']*p['d_10y_bps']/10000/p['cap_rate'];steps=[f'Direct equity fraction = −{p["cap_rate_beta"]:.10g} × {p["d_10y_bps"]:.10g}/10,000 / {p["cap_rate"]:.10g} = {z["V"]:.10g}']
    elif kind in ('gov_budget','gov_shutdown','gov_cr'):
        if kind=='gov_budget':z['R']=R*p['gov_revenue_share']*p['program_relevance']*p['d_budget_pct']
        elif kind=='gov_shutdown':z['R']=-R*p['gov_revenue_share']*p['affected_share']*p['days']/365*(1-p['recovery_share'])
        else:z['R']=-R*p['gov_revenue_share']*p['new_award_share']*p['months_delayed']/12
        z['E']=z['R']*cm*p['fixed_cost_absorption'];steps=[f'Government channel {kind}, evaluated parameters below: ΔR={z["R"]:.10g}; ΔEBIT=ΔR × margin {cm:.10g} × absorption {p["fixed_cost_absorption"]:.10g} = {z["E"]:.10g}']
    else:raise ValueError('Unsupported independent channel: '+kind)
    return z,steps


def main() -> None:
    """Draw one affected scenario per industry and check EPS/price to the cent."""
    rng=random.Random(SEED);reg=registry();checks=[];lines=['# Ten stratified random arithmetic checks','',f'Seed: {SEED}. One affected reference-company scenario per industry, using default user inputs. Draws are independent of whether the arithmetic passes. This audit-only calculator separately implements channel arithmetic, aggregation and duration valuation; it does not call the engine calculation functions. Configured expressions are reused to capture the exact parameters, and are printed for manual review. These checks validate arithmetic, not the truth of an exposure or a forecast. USD millions except EPS, price and share counts (millions).','']
    for industry in load_universe().industries:
        pool=[]
        for policy in reg.industry_policies(industry.slug):
            runner=build_runner(industry.slug,policy.id);result=runner.run()
            pool.extend((runner,c) for c in result.companies if abs(c.dNI)>1e-8 or abs(c.dP or 0)>1e-8)
        runner,c=rng.choice(pool);pol=runner.policy;b=c.baseline
        ctx=dict(input=runner.inputs,assumption={k:v[1] for k,v in runner.assumption_ranges.items()},exposure={k:reg.exposure(c.ticker,k).value if reg.exposure(c.ticker,k).applicable else 0 for k in pol.exposure_keys},baseline={k:b.get(k) for k in BASELINE_FIELDS},macro=runner.macro or {},derived={},role=dict(is_importer=c.role=='importer',is_domestic_producer=c.role=='domestic_producer',is_neutral=c.role=='neutral'))
        for k,expr in pol.derived.items():ctx['derived'][k]=evaluate(expr,ctx)
        pieces=[];working=[]
        for spec in pol.channels:
            if spec.roles and c.role not in spec.roles:continue
            if spec.company_kinds is not None and b['kind'] not in spec.company_kinds:continue
            params={**CHANNELS[spec.type].default_params,**{k:float(evaluate(v,ctx)) for k,v in spec.params.items()}}
            delta,steps=calculate_channel(spec.type,b,params);pieces.append((delta,spec.persistence or pol.persistence));working.append((spec.type,params,spec.params,steps))
        tax=sum(d['T'] for d,_ in pieces);tn=min(1,max(0,b['effective_tax_rate']+tax));ps=b.get('parent_share',1)
        total=sum(((d['E']-d['I'])*(1-tn)+d['N']+b['pretax_income']*(b['effective_tax_rate']-tn)*(d['T']/tax if tax else 0))*ps for d,_ in pieces)
        eps=total/b['diluted_shares'];raw=0.
        for d,duration in pieces:
            ni=((d['E']-d['I'])*(1-tn)+d['N']+b['pretax_income']*(b['effective_tax_rate']-tn)*(d['T']/tax if tax else 0))*ps
            multiple=(b.get('valuation_pe') if duration=='permanent' else 1 if duration=='one_time' else sum(1.09**(-k) for k in range(1,int(duration.split(':')[1])+1)))
            if ni and multiple is None:raw=None;break
            raw+=(ni/b['diluted_shares']*(multiple or 0))+d['PV']/(b.get('shares_outstanding') or b['diluted_shares'])+d['V']*(b.get('price') or 0)
        price=None if raw is None or b.get('price') is None else max(-b['price'],raw)
        assert math.isclose(total,c.dNI,rel_tol=1e-9,abs_tol=1e-7),(pol.id,c.ticker,total,c.dNI)
        assert math.isclose(eps,c.dEPS,rel_tol=1e-9,abs_tol=1e-9)
        assert price is None and c.dP is None or price is not None and c.dP is not None and math.isclose(price,c.dP,rel_tol=1e-9,abs_tol=1e-7),(pol.id,c.ticker,price,c.dP)
        lines += [f'## {len(checks)+1}. {industry.name} / {pol.id} / {c.ticker}','',f'Inputs: `{json.dumps(runner.inputs)}`. Role: `{c.role}`. Annual source: {b.get("filing_url")}.','',f'Baseline R={b["revenue"]:.10g}; C={b["cost_of_revenue"]:.10g}; PTI={b["pretax_income"]:.10g}; tax={b["effective_tax_rate"]:.10g}; parent share={ps:.10g}; diluted shares={b["diluted_shares"]:.10g}; price={b.get("price")}; valuation P/E={b.get("valuation_pe")} ({b.get("valuation_method")}).','']
        for kind,params,expressions,steps in working:
            lines += [f'**{kind}**: configured expressions `{json.dumps(expressions)}`.','',f'Evaluated parameters: `{json.dumps(params,sort_keys=True)}`.','']
            lines += ['- '+s for s in steps];lines.append('')
        lines += [f'Combined forward tax rate = clip({b["effective_tax_rate"]:.10g} + {tax:.10g},0,1) = {tn:.10g}.', '',f'ΔNI = sum[(ΔEBIT−Δinterest) × (1−tax new) + direct after-tax items + PTI × tax-rate change] × parent share = **{total:.10g}M**.', '',f'ΔEPS = {total:.10g} / {b["diluted_shares"]:.10g} = **${eps:.10g}** (engine ${c.dEPS:.10g}).','',f'Valuation: each channel uses its own duration (permanent: supported P/E; one-time: 1; fixed years: annual discount factors at 9%), plus direct value per economic share and direct value percentage × price. Raw Δprice={raw}; floor-adjusted Δprice={price}; engine Δprice={c.dP}.','',f'Cent comparison: EPS {round(eps,2):.2f} = {round(c.dEPS,2):.2f}; price '+('both unavailable' if price is None else f'{round(price,2):.2f} = {round(c.dP,2):.2f}')+'. **PASS arithmetic**.','']
        checks.append(dict(policy=industry.slug+'/'+pol.id,ticker=c.ticker,inputs=runner.inputs,independent_dNI=total,engine_dNI=c.dNI,independent_dEPS=eps,engine_dEPS=c.dEPS,independent_dP=price,engine_dP=c.dP,pass_arithmetic=True))
    (ROOT/'reports/spotchecks.md').write_text('\n'.join(lines)+'\n');(ROOT/'reports/spotchecks.json').write_text(json.dumps(dict(seed=SEED,checks=checks),indent=2)+'\n')
    print('10/10 independent arithmetic checks passed')


if __name__=='__main__':main()
