// Optional local simulation; no project runtime dependencies. See docs/mobile-simulation.md.
import {createRequire} from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const [deps, chromium, output] = process.argv.slice(2);
if (!deps || !chromium || !output) throw new Error('Usage: node scripts/check_mobile.mjs <temporary npm directory> <chromium executable> <output directory>');
const require = createRequire(path.resolve(deps, 'package.json'));
const puppeteer = require('puppeteer');
const {marked} = require('marked');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
fs.mkdirSync(output, {recursive:true});
const read = name => fs.readFileSync(path.join(root, name),'utf8');
const diagrams = [...read('docs/workflow.md').matchAll(/```mermaid\n([\s\S]*?)```/g)].map(m=>m[1]);
if (diagrams.length !== 2) throw new Error('Expected two Mermaid diagrams');
const css = 'body{margin:0;font:16px/1.5 Arial,sans-serif;color:#1f2328}article{padding:16px;overflow-wrap:break-word}h1{font-size:28px}h2{font-size:24px}h3{font-size:20px}ul{padding-left:24px}pre{overflow:auto}code{font-size:85%}img,svg{max-width:100%}';
const versions={mermaid:require('mermaid/package.json').version,marked:require('marked/package.json').version,puppeteer:require('puppeteer/package.json').version};
const browser = await puppeteer.launch({executablePath:chromium,args:['--no-sandbox'],headless:true});
const results=[];
try {
 const page = await browser.newPage();
 versions.chromium=await browser.version();
 for (const width of [320,375,390,430]) {
  await page.setViewport({width,height:812,deviceScaleFactor:1});
  for (const name of ['README.md','README.zh-CN.md']) {
   await page.setContent(`<style>${css}</style><article>${marked.parse(read(name),{gfm:true})}</article>`);
   const result=await page.evaluate(()=>{
    const article=document.querySelector('article');
    const start=article.querySelector('a[href="docs/portable-starter.md"]');
    const roles=article.querySelectorAll('h3');
    return {pageWidth:document.documentElement.scrollWidth,starterY:start?.getBoundingClientRect().top,starterWidth:start?.getBoundingClientRect().right,tables:article.querySelectorAll('table').length,roles:roles.length};
   });
   if (result.pageWidth>width || !Number.isFinite(result.starterY) || result.starterY>=812 || result.starterY<0 || result.starterWidth>width || result.tables!==0 || result.roles!==5) throw new Error(JSON.stringify({name,width,...result}));
   await page.screenshot({path:path.join(output,`${name}-${width}.png`),fullPage:true});
   results.push({name,width,...result,result:'PASS'});
  }
  for (const [index,source] of diagrams.entries()) {
   await page.setContent(`<style>${css}</style><article id="diagram"></article>`);
   await page.addScriptTag({content:fs.readFileSync(require.resolve('mermaid/dist/mermaid.min.js'),'utf8')});
   const result=await page.evaluate(async source=>{
    mermaid.initialize({startOnLoad:false,securityLevel:'strict'});
    const parsed=await mermaid.parse(source);
    const {svg}=await mermaid.render('diagramSvg',source);
    document.getElementById('diagram').innerHTML=svg;
    const el=document.querySelector('svg');
    const rect=el.getBoundingClientRect();
    const effectiveFont=Math.min(...[...el.querySelectorAll('.nodeLabel')].map(n=>parseFloat(getComputedStyle(n).fontSize)))*rect.width/el.viewBox.baseVal.width;
    return {type:parsed.diagramType,pageWidth:document.documentElement.scrollWidth,svgWidth:rect.width,nativeWidth:el.viewBox.baseVal.width,effectiveFont};
   },source);
   if (result.pageWidth>width || result.svgWidth>width-32+1 || !Number.isFinite(result.effectiveFont) || result.effectiveFont<12) throw new Error(JSON.stringify({index,width,...result}));
   await page.screenshot({path:path.join(output,`flow${index+1}-${width}.png`),fullPage:true});
   results.push({name:`flow${index+1}`,width,...result,result:'PASS'});
  }
 }
} finally {await browser.close();}
fs.writeFileSync(path.join(output,'results.json'),JSON.stringify({versions,results},null,2));
console.log(JSON.stringify({versions,results},null,2));
