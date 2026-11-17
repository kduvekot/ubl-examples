#!/usr/bin/env node
// Product renders of the Serra 180 (PNG) with three.js in headless Chromium (Playwright).
// Usage: node render.js <world/bench directory>
// Needs: Playwright with its Chromium (pre-installed), and three.js from a local npm install;
// set THREE_DIR to the 'three' package directory (default: resolved from the current directory).
'use strict';
const fs = require('fs');
const path = require('path');
const http = require('http');
const { execSync } = require('child_process');

function req(name) {
  try { return require(name); } catch (e) {
    const g = execSync('npm root -g').toString().trim();
    return require(path.join(g, name));
  }
}
const { chromium } = req('playwright');

const BENCH = path.resolve(process.argv[2] || __dirname);
let THREE_DIR = process.env.THREE_DIR;
if (!THREE_DIR) {
  try { THREE_DIR = path.dirname(require.resolve('three/package.json', { paths: [process.cwd()] })); }
  catch (e) { console.error('three.js not found: set THREE_DIR'); process.exit(1); }
}
const P = JSON.parse(fs.readFileSync(path.join(BENCH, 'parameters.json'), 'utf8'));
const OUT = path.join(BENCH, 'renders');
fs.mkdirSync(OUT, { recursive: true });

const PAGE = `<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;background:#dfe6ea;overflow:hidden}canvas{display:block}</style>
<script type="importmap">{"imports":{"three":"/three/build/three.module.js","three/addons/":"/three/examples/jsm/"}}</script>
</head><body><script type="module">
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const W = innerWidth, H = innerHeight;
const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(devicePixelRatio);
renderer.setSize(W, H);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.body.appendChild(renderer.domElement);
const pmrem = new THREE.PMREMGenerator(renderer);
const envTex = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;

function rand(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

function woodTexture(seed, wood) {
  const c = document.createElement('canvas'); c.width = 2048; c.height = 256;
  const g = c.getContext('2d'); const r = rand(seed);
  g.fillStyle = wood.colour; g.fillRect(0, 0, c.width, c.height);
  for (let i = 0; i < 260; i++) {
    const y = r() * c.height, a = 0.04 + r() * 0.12, w = 0.6 + r() * 2.6;
    g.strokeStyle = r() < 0.5 ? 'rgba(' + wood.grain_dark + ',' + a + ')' : 'rgba(' + wood.grain_light + ',' + a + ')';
    g.lineWidth = w; g.beginPath(); g.moveTo(0, y);
    for (let x = 0; x <= c.width; x += 64) g.lineTo(x, y + Math.sin(x / (180 + r() * 200) + i) * (2 + r() * 5));
    g.stroke();
  }
  for (let i = 0; i < 40; i++) { // medullary rays of oak
    g.fillStyle = 'rgba(' + wood.grain_light + ',0.18)';
    g.fillRect(r() * c.width, r() * c.height, 8 + r() * 30, 1.5);
  }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; return t;
}
function paving() {
  const c = document.createElement('canvas'); c.width = 1024; c.height = 1024;
  const g = c.getContext('2d'); const r = rand(7);
  g.fillStyle = '#9a9890'; g.fillRect(0, 0, 1024, 1024);
  const n = 8, s = 1024 / n;
  for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) {
    const v = 158 + Math.floor(r() * 10);
    g.fillStyle = 'rgb(' + v + ',' + (v - 2) + ',' + (v - 8) + ')';
    g.fillRect(i * s + 3, j * s + 3, s - 6, s - 6);
    for (let k = 0; k < 120; k++) { g.fillStyle = 'rgba(60,60,55,' + (r() * 0.08) + ')'; g.fillRect(i * s + r() * s, j * s + r() * s, 2, 2); }
  }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
  t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(10, 10); t.anisotropy = 8; return t;
}
function labelTexture(lines) {
  const c = document.createElement('canvas'); c.width = 1024; c.height = 512;
  const g = c.getContext('2d');
  g.fillStyle = '#f4f1e8'; g.fillRect(0, 0, 1024, 512);
  g.strokeStyle = '#333'; g.lineWidth = 6; g.strokeRect(12, 12, 1000, 488);
  g.fillStyle = '#1d1d1d'; g.font = 'bold 92px sans-serif'; g.fillText(lines[0], 48, 130);
  g.font = '56px sans-serif';
  for (let i = 1; i < lines.length; i++) g.fillText(lines[i], 48, 130 + i * 86);
  for (let i = 0; i < 60; i++) g.fillRect(620 + i * 6 + (i % 3), 330, (i % 4) + 2, 130); // barcode
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
}
function boxUV(geo, along) { // planar UVs: u along the given axis, v across
  const p = geo.attributes.position, n = p.count, uv = new Float32Array(2 * n);
  for (let i = 0; i < n; i++) {
    const x = p.getX(i), y = p.getY(i), z = p.getZ(i);
    const a = along === 'x' ? x : along === 'y' ? y : z;
    const b = along === 'x' ? y + z : x + z;
    uv[2 * i] = a / 1.8; uv[2 * i + 1] = b / 0.2;
  }
  geo.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
}

async function load(url) {
  const gltf = await new GLTFLoader().loadAsync(url);
  const root = gltf.scene;
  root.updateMatrixWorld(true);
  let box = new THREE.Box3().setFromObject(root), size = box.getSize(new THREE.Vector3());
  if (Math.max(size.x, size.y, size.z) > 50) { root.scale.setScalar(0.001); root.updateMatrixWorld(true); }
  box = new THREE.Box3().setFromObject(root); size = box.getSize(new THREE.Vector3());
  return root;
}
function named(o) { let n = o; while (n) { if (n.name && !/^mesh|^Mesh|^$/.test(n.name)) return n.name; n = n.parent; } return ''; }

window.renderScene = async function (cfg) {
  const scene = new THREE.Scene();
  scene.environment = envTex;
  scene.background = new THREE.Color(cfg.bg || '#dfe6ea');
  const hemi = new THREE.HemisphereLight(0xeef4ff, 0x8a8576, 0.55); scene.add(hemi);
  const sun = new THREE.DirectionalLight(0xfff4e2, 2.6);
  sun.position.set(-2.5, 4.5, 3.2); sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048); sun.shadow.bias = -0.0003; sun.shadow.normalBias = 0.01;
  const sc = sun.shadow.camera; sc.left = -3; sc.right = 3; sc.top = 3; sc.bottom = -3; sc.near = 0.5; sc.far = 12;
  scene.add(sun);
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.MeshStandardMaterial({ map: paving(), roughness: 0.95, metalness: 0 }));
  ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
  const root = await load(cfg.glb);
  const frameMat = new THREE.MeshStandardMaterial({ color: new THREE.Color(cfg.frame || '#555D61'), metalness: 0.0, roughness: 0.5, envMapIntensity: 0.7 });
  const zinc = new THREE.MeshStandardMaterial({ color: 0xc9ccd0, metalness: 0.9, roughness: 0.3 }); // stainless A2
  const kraft = new THREE.MeshStandardMaterial({ color: 0xb98e5c, roughness: 0.9, metalness: 0 });
  const strap = new THREE.MeshStandardMaterial({ color: 0x24508c, roughness: 0.5 });
  const palletMat = new THREE.MeshStandardMaterial({ color: 0xd2b98d, roughness: 0.85 });
  let seed = 3;
  const cartons = new Map();
  root.traverse(o => {
    if (!o.isMesh) return;
    o.castShadow = true; o.receiveShadow = true;
    const n = named(o);
    if (/frame/.test(n)) o.material = frameMat;
    else if (/slat/.test(n)) { boxUV(o.geometry, 'x'); o.material = new THREE.MeshStandardMaterial({ map: woodTexture(seed++, cfg.wood), roughness: 0.72, metalness: 0 }); }
    else if (/bolt|nut|washer/.test(n)) o.material = zinc;
    else if (/carton/.test(n)) { o.material = kraft; const k = n.match(/carton_[0-9]+/)[0]; if (!cartons.has(k)) cartons.set(k, []); cartons.get(k).push(o); }
    else if (/bundle/.test(n)) { boxUV(o.geometry, 'x'); o.material = new THREE.MeshStandardMaterial({ map: woodTexture(seed++, cfg.wood), roughness: 0.72 }); }
    else if (/strap/.test(n)) o.material = strap;
    else if (/pallet/.test(n)) o.material = palletMat;
  });
  // the GLB root node already turns the Z-up model to glTF's Y-up, in metres
  root.updateMatrixWorld(true);
  scene.add(root);
  if (cfg.labels) for (const [n, os] of cartons) { // label on the top face of each frame carton
    const b = new THREE.Box3(); for (const o of os) b.expandByObject(o);
    const s = b.getSize(new THREE.Vector3()), c = b.getCenter(new THREE.Vector3());
    const no = parseInt(n.split('_')[1], 10);
    const lab = new THREE.Mesh(new THREE.PlaneGeometry(0.30, 0.15), new THREE.MeshStandardMaterial({ map: labelTexture(['Serra 180', 'VI-B180  parcel ' + no + ' of 3', no === 2 ? 'side frame + bolt set' : 'side frame']), roughness: 0.8 }));
    lab.rotation.x = -Math.PI / 2; lab.position.set(c.x + s.x * 0.18, b.max.y + 0.0012, c.z + s.z * 0.12); scene.add(lab);
  }
  const box = new THREE.Box3().setFromObject(root);
  const ctr = box.getCenter(new THREE.Vector3());
  const cam = new THREE.PerspectiveCamera(cfg.fov || 30, W / H, 0.05, 50);
  cam.position.set(...cfg.cam);
  cam.lookAt(new THREE.Vector3(...(cfg.target || [ctr.x, ctr.y, ctr.z])));
  renderer.render(scene, cam);
  return true;
};
window.ready = true;
</script></body></html>`;

function serve() {
  const types = { '.js': 'text/javascript', '.glb': 'model/gltf-binary', '.html': 'text/html', '.json': 'application/json' };
  const srv = http.createServer((q, r) => {
    const u = decodeURIComponent(q.url.split('?')[0]);
    let f;
    if (u === '/' || u === '/index.html') { r.writeHead(200, { 'Content-Type': 'text/html' }); return r.end(PAGE); }
    if (u.startsWith('/three/')) f = path.join(THREE_DIR, u.slice(7));
    else if (u.startsWith('/glb/')) f = path.join(BENCH, 'glb', path.basename(u));
    if (!f || !fs.existsSync(f)) { r.writeHead(404); return r.end(); }
    r.writeHead(200, { 'Content-Type': types[path.extname(f)] || 'application/octet-stream' });
    fs.createReadStream(f).pipe(r);
  });
  return new Promise(res => srv.listen(0, '127.0.0.1', () => res(srv)));
}

(async () => {
  const srv = await serve();
  const port = srv.address().port;
  const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const page = await browser.newPage({ viewport: { width: 1000, height: 625 }, deviceScaleFactor: 2 });
  page.on('console', m => { if (m.type() === 'error') console.error('page:', m.text()); });
  await page.goto(`http://127.0.0.1:${port}/`);
  await page.waitForFunction('window.ready === true');
  const col = P.materials.colours;
  // three.js coordinates after rotation: x = bench length, y = up, z = -depth (front of the bench at z = 0)
  const W = P.woods;
  for (const f of fs.readdirSync(OUT)) if (f.endsWith('.png')) fs.unlinkSync(path.join(OUT, f));
  const ash = W[W.main_wood], oak = W[W.comparison_wood];
  const jobs = [
    { out: 'serra180_GRY_tm-ash_three-quarter.png', glb: '/glb/serra180_GRY.glb', frame: col.GRY.srgb_approx, wood: ash, cam: [-0.95, 1.25, 2.55], target: [0.85, 0.36, -0.33] },
    { out: 'serra180_GRN_tm-ash_three-quarter.png', glb: '/glb/serra180_GRN.glb', frame: col.GRN.srgb_approx, wood: ash, cam: [-0.95, 1.25, 2.55], target: [0.85, 0.36, -0.33] },
    { out: 'serra180_GRY_oak_three-quarter.png', glb: '/glb/serra180_GRY_oak38.glb', frame: col.GRY.srgb_approx, wood: oak, cam: [-0.95, 1.25, 2.55], target: [0.85, 0.36, -0.33] },
    { out: 'serra180_detail_frame_and_slats_tm-ash.png', glb: '/glb/serra180_GRY.glb', frame: col.GRY.srgb_approx, wood: ash, cam: [-0.42, 0.86, 0.62], target: [0.12, 0.47, -0.30], fov: 34 },
    { out: 'serra180_parcels_knocked_down.png', glb: '/glb/serra180_parcels.glb', wood: ash, cam: [-0.75, 1.55, 1.75], target: [0.9, 0.03, -0.15], fov: 34, labels: true },
    { out: 'serra180_pallet_of_four.png', glb: '/glb/serra180_pallet.glb', wood: ash, cam: [-1.35, 1.75, 2.6], target: [0.92, 0.33, -0.35], fov: 32 },
  ];
  for (const j of jobs) {
    const t0 = Date.now();
    await page.evaluate(cfg => window.renderScene(cfg), j);
    console.log('  rendered in', Date.now() - t0, 'ms');
    await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(OUT, j.out), timeout: 180000 });
    console.log('render', j.out);
  }
  await browser.close();
  srv.close();
})().catch(e => { console.error(e); process.exit(1); });
