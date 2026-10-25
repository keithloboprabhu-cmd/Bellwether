/** Validate financial units, zero, missing values and CSV escaping. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {percent,money,bps,csvCell} from './format.ts';
test('zero is not missing and negative zero is normalized',()=>{assert.equal(percent(-0),'0.0%');assert.equal(percent(null),'—');assert.equal(bps(-0),'0 bps');});
test('tiny values do not round to zero',()=>{assert.equal(percent(-.0001),'−<0.1%');assert.equal(percent(.0001),'+<0.1%');});
test('output units remain explicit',()=>{assert.equal(percent(-.0522),'−5.2%');assert.equal(money(-6755.66),'−$6.8B');assert.equal(bps(-21.11),'−21.1 bps');});
test('CSV quotes fields and neutralizes formula strings',()=>{assert.equal(csvCell('A,"B"'),'"A,""B"""');assert.equal(csvCell('=1+1'),'"\'=1+1"');assert.equal(csvCell(-.2),'"-0.2"');});
