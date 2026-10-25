/** Numeric invariants protect terrain truthfulness independently of rendering. */
import test from 'node:test';
import assert from 'node:assert/strict';
import {anchorsFor,heightAt,mappedImpact} from './field.ts';
test('anchors are unchanged by table sorting',()=>{const n=[{id:'HUM',impact:-.6},{id:'UNH',impact:-.1},{id:'PFE',impact:0}];assert.deepEqual(anchorsFor(n),anchorsFor([...n].reverse()));});
test('mapping is fixed and monotonic in fractions',()=>{const values=[-.8,-.1,-.001,0,.001,.1,.8].map(mappedImpact);for(let i=1;i<values.length;i++)assert.ok(values[i]>values[i-1]);assert.equal(mappedImpact(.15),Math.tanh(1));});
test('every node center retains exact signed height with neighbors',()=>{const n=[{id:'A',impact:-.62},{id:'B',impact:.02},{id:'C',impact:0},{id:'D',impact:null},{id:'E',impact:1},{id:'F',impact:-.01}];const anchors=anchorsFor(n);for(const a of anchors){const v=n.find(n=>n.id===a.id)!.impact;assert.ok(Math.abs(heightAt(a.x,a.y,n,anchors)-mappedImpact(v))<1e-12);}});
test('changing a shock never rearranges anchors',()=>{assert.deepEqual(anchorsFor([{id:'A',impact:-.1}]),anchorsFor([{id:'A',impact:.8}]));});
test('interpolation never invents an effect larger than any input',()=>{const n=[{id:'A',impact:.1},{id:'B',impact:.1},{id:'C',impact:-.1},{id:'D',impact:0},{id:'E',impact:null},{id:'F',impact:.1}];const a=anchorsFor(n);for(let x=0;x<=1;x+=.01)for(let y=0;y<=1;y+=.01)assert.ok(Math.abs(heightAt(x,y,n,a))<=mappedImpact(.1)+1e-12);});
