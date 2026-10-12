/** Build web aislado: React -> HTML estático. No modifica dist/ ni el PDF. */
import { build } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, resolve, join, relative } from 'node:path';
import { mkdtemp, mkdir, rm, readFile, writeFile, copyFile, rename } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import * as data from '../src/data.js';

const project = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const target = join(project, 'web-dist');
const staging = await mkdtemp(join(project, '.web-stage-'));
const renderDir = await mkdtemp(join(project, '.web-render-'));
const protectedFiles = ['src/App.jsx','src/styles.css','src/data.js','src/main.jsx','generate_pdf.py'];
async function hashes() {
  return Object.fromEntries(await Promise.all(protectedFiles.map(async f => [f, createHash('sha256').update(await readFile(join(project,f))).digest('hex')])));
}
const before = await hashes();
try {
  await build({ root: project, configFile: false, plugins: [react()], publicDir: false, logLevel: 'warn',
    build: { ssr: join(project, 'src/web/App.jsx'), outDir: renderDir, emptyOutDir: true, sourcemap: false,
      rollupOptions: { output: { entryFileNames: 'render.mjs' } } } });
  const { renderDocument } = await import(pathToFileURL(join(renderDir,'render.mjs')).href);
  const isPreview = process.env.VERCEL_ENV !== 'production' && !process.argv.includes('--production');
  const html = renderDocument({ preview: isPreview });
  for (const privateValue of [data.profile.phone, data.profile.email, 'CONTACTO.vcf', 'CONTACTO.jpg', 'CONTACTO.png']) {
    if (privateValue && html.includes(privateValue)) throw new Error('Un dato privado se filtró en el HTML público.');
  }
  const expected = [data.profile.title,data.profile.summary,
    ...data.trayectoria.flatMap(h=>[h.role,h.institution,h.sub,h.desc]),
    ...data.toolGroups.flatMap(g=>g.items)];
  const unescape = s => s.replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#x27;/g,"'");
  const missing = expected.filter(s => !unescape(html).includes(s));
  if (missing.length) throw new Error(`Falta contenido: ${missing.join(' | ')}`);
  await mkdir(join(staging,'assets'),{recursive:true});
  await writeFile(join(staging,'index.html'),html,'utf8');
  await copyFile(join(project,'src/web/styles.css'),join(staging,'assets/web.css'));
  await copyFile(join(project,'src/web/enhance.js'),join(staging,'assets/enhance.js'));
  await copyFile(join(project,'src/web/ux.css'),join(staging,'assets/ux.css'));
  const assets = [...new Set([...html.matchAll(/<img[^>]+src="([^"]+)"/g)].map(m=>m[1]))];
  for (const asset of assets) {
    if (!asset.startsWith('/img/') || asset.includes('..')) throw new Error(`Ruta no autorizada: ${asset}`);
    const local = asset.slice(1);
    await mkdir(dirname(join(staging,local)),{recursive:true});
    await copyFile(join(project,'public',local),join(staging,local));
  }
  // Solo web-dist se publica: no respaldos, node_modules, PDF privado ni vCard.
  const legacy = { 'experiencia':'experiencia','habilidades':'habilidades','educacion':'educacion',
    'contacto':'contacto','competencias':'areas','equipamiento':'contacto','referencias':'contacto' };
  for (const [file,anchor] of Object.entries(legacy)) {
    await writeFile(join(staging,`${file}.html`),`<!doctype html><html lang="es"><head><meta charset="UTF-8"><meta http-equiv="refresh" content="0;url=/#${anchor}"><title>Alexi Burgos</title></head><body><a href="/#${anchor}">Continuar al CV</a></body></html>`);
  }
  await writeFile(join(staging,'robots.txt'),isPreview ? 'User-agent: *\nDisallow: /\n' : 'User-agent: *\nAllow: /\nSitemap: https://cv-alexi.vercel.app/sitemap.xml\n');
  await writeFile(join(staging,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://cv-alexi.vercel.app/</loc></url></urlset>');
  const after = await hashes();
  if (JSON.stringify(before)!==JSON.stringify(after)) throw new Error('Se modificó un archivo del CV/PDF.');
  await rm(target,{recursive:true,force:true});
  await rename(staging,target);
  const manifest={ preview:isPreview,output:relative(project,target),sourceDataSHA256:before['src/data.js'],
    kpis:data.kpis.length,experiences:data.trayectoria.length,tools:data.toolGroups.flatMap(g=>g.items).length,
    checkedPhrases:expected.length,missing:[],assets,pdfSourcesUnchanged:true,protectedFiles:after,
    publicContact:'LinkedIn únicamente',privatePDFPublished:false };
  await writeFile(join(project,'WEB_BUILD_REPORT.json'),JSON.stringify(manifest,null,2)+'\n');
  console.log(`Web generada: ${target}\n${manifest.kpis} indicadores | ${manifest.experiences} experiencias | ${manifest.tools} herramientas\nFuente CV/PDF: sin modificaciones. Contacto público: LinkedIn.`);
} finally {
  await rm(renderDir,{recursive:true,force:true});
  await rm(staging,{recursive:true,force:true});
}
