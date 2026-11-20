"""Writes report.md from results.json and parameters.json (called by build_bench.py)."""
import json
import math
from pathlib import Path

# Figures of earlier runs, quoted only to show what changed (run 1: commit 41c8c98).
RUN1 = dict(slat="4.45 kg (oak 38)", wood=22.2, boltset="0.74 kg (galvanised, M8 x 60)", frame=13.42, net=49.86, parcels="14.5 / 15.3 / 22.9",
            bundle="1,810 x 295 x 86", gross=52.69, pallet="716 mm; 210.8 / 238.9 kg", load=5.94, steel="26.8 (with fasteners)", stainless="–",
            poured=48.9, util="0.95", util30="–", sag=17.0, sag3=9.4, n_items=17)
RUN2 = dict(slat="3.58 kg (modified ash 38)", wood=17.9, boltset="0.72 kg (A2, M8 x 60)", frame=13.42, net=45.45, parcels="14.5 / 15.3 / 18.5",
            bundle="1,810 x 295 x 86", gross=48.29, pallet="716 mm; 193.2 / 221.3 kg", load=5.51, steel="26.1", stainless="0.70",
            poured=48.9, util="0.88", util30="1.02", sag=14.4, sag3=7.9, n_items=20)
RUN3 = dict(slat="4.24 kg (ash 45)", boltset="0.76 kg (A2, M8 x 65)", frame_cast=13.07, frame=13.44, net=48.83, parcels="14.5 / 15.3 / 21.8",
            gross=51.64, pallet="744 mm; 206.6 / 234.7 kg", load=5.84, steel="26.1", poured=47.7, util="0.64", sag=8.7, n_items=19)
RUN4 = dict(frame="10.40 / 11.09 kg", boltset_kg=0.761, net=44.13, parcels="12.2 / 13.0 / 21.8", gross=46.94, pallet="744 mm; 187.8 / 215.9 kg",
            load=5.36, n_items=20)


def n(x, nd=1):
    return f"{x:,.{nd}f}" if isinstance(x, (int, float)) else str(x)


def footprint(FM, net_liquid):
    """The bench's footprint per stage with the scrap share (O225): the iron's part of the published all-ore figures,
    from the stated factors, scaled to the hot metal, plus the scrap's sourcing and melting."""
    F, raw = FM["footprint"], FM["raw_per_t_liquid"]
    sh = FM["scrap_share_pct"] / 100
    per_kg_hot = (raw["iron_ore_kg"] * F["ore_sourcing_kg_per_kg_ore"] + raw["reductant_kg"] * F["reductant_sourcing_kg_per_kg"]
                  + raw["limestone_kg"] * F["limestone_sourcing_kg_per_kg"]) / 1000
    pub = F["published_all_ore"]
    iron_a12_old = net_liquid * per_kg_hot
    iron_a3_old = net_liquid * F["hot_metal_kg_per_kg"]
    hot, scrap = net_liquid * (1 - sh), net_liquid * sh
    a12 = pub["A1_A2"] - iron_a12_old + hot * per_kg_hot + scrap * F["scrap_sourcing_kg_per_kg"]
    a3 = pub["A3"] - iron_a3_old + hot * F["hot_metal_kg_per_kg"] + scrap * F["scrap_melt_kwh_per_kg"] * F["grid_kg_per_kwh"]
    return dict(F=F, pub=pub, iron_a12_old=iron_a12_old, iron_a3_old=iron_a3_old, a12=a12, a3=a3,
                a12_r=round(a12), a3_r=round(a3), hot=hot, scrap=scrap)


def write(r, here):
    here = Path(here)
    r = json.loads(json.dumps(r))          # same key types as results.json
    P = json.load(open(here / "parameters.json", encoding="utf-8"))
    W = P["world_figures"]
    wa = P["woods"][r["main_wood"]]
    m, d, fr, c, sl = r["mass"], r["dims"], r["frame"], r["casting"], r["slats"]
    pk, pa, ta = r["packaging"], r["parcels"], r["transport"]
    f = P["frame"]
    FMk = r["frame_material"]
    FM = P["materials"]["frame_materials"][FMk]
    f["t_web"] = f["t_flange"] = FM["design_wall_mm"]          # as apply_frame_material() in build_bench.py
    f["feet"]["thickness"] = FM["feet_thickness"]
    P["casting"]["melt_loss_pct"] = FM.get("melt_loss_pct", P["casting"]["melt_loss_pct"])
    MC = r["material_comparison"]
    T = P["slats"]["thickness"] if False else wa["slat_thickness"]
    bolt_len = wa["bolt_length"]
    cast_bench = 2 * (m["frame_bare"] + m["frame_draft"])
    melt_loss = c["poured"] * P["casting"]["melt_loss_pct"] / 100
    fettle = 2 * P["casting"]["fettling_loss_kg_per_frame"]
    net_liquid = cast_bench + melt_loss + fettle
    blank_l = 1830 * 101 * (T + 6) / 1e6
    fcases = fr["cases"]
    co, ci, bu, fb = pk["carton_outer"], pk["carton_inner"], pk["bundle"], pk["frame_bbox"]
    wall = r["frame_mass_by_wall"]
    arm_extra = (f["x_centre"] - f["armrest"]["flange_width"] / 2) * f["t_flange"] * 547 * FM["density"] / 1e9
    world_net_check = 2 * W["frame_mass"] + 5 * W["slat_mass"] + W["bolt_set_mass"]
    URK, SVK, ENC = ("UR-SF-0450 (450 kg over the seat)", "Three adults of 80 kg, one per seat (service)",
                     "EN 581-2 contract, 2000 N on the centre seat")
    ua, sv, en = sl["cases"][URK], sl["cases"][SVK], sl["cases"][ENC]
    util_sc2 = 1.5 * ua["sigma"] / sl["f_md_sc2"]
    f_mk30 = wa["f_mk_base"] * 0.70
    util30 = 1.5 * ua["sigma"] / (f_mk30 * wa["k_mod_short"] * sl["k_h"] / wa["gamma_M"])
    trk = r["sawmill_truck"]
    beta = math.radians(d["beta"])
    up_rear_clear = (d["P"][1] + P["slats"]["back_slat_u"][1] * math.cos(beta) - T * math.sin(beta)) - (d["seat_front"] + P["ergonomics"]["armrest_above_seat"])
    mc_out = (1 + sum(wa["mc_outdoor"]) / 200) / (1 + wa["mc_delivery"] / 100) - 1

    L = []
    A = L.append
    A("# Serra 180 park bench: parametric model, drawings and check of the world's figures")
    A("")
    A(f"*Valdara Industries, Ferrano (Urvania), item VI-B180, datasheet VI-DS-B180. Open point O149 (feeds O25 and C69). Run 5 (final) of 2026-11-18, with the owner's last answers (tariff, lengths, slat finish): side frames of "
      f"{FM['name']} {FM['grade']}, galvanised and powder-coated; slats of thermally modified ash 1,800 x 95 x {T} mm made by Marrowdale; stainless A4 fixings. "
      "Generated by `build_bench.py` from `parameters.json`; every number below is computed, except the figures of runs 1 to 4 quoted for comparison.*")
    A("")
    A("## 1. Summary")
    A("")
    A("- **What was made:** a parametric solid model (two identical side frames of ductile cast iron EN-GJS-400-15, hot-dip galvanised and powder-coated; "
      "five slats of thermally modified ash; 20 stainless A4 M8 carriage bolts), STEP files of the assembly and each part, GLB files, eight dimensioned SVG "
      "drawings (VI-DWG-B180-001 to 008, revision E), five PNG renders, the mould with gating, the parcels and the pallet, and this report; all figures are in `results.json`.")
    A(f"- **The bench:** {n(d['length'], 0)} mm over the slats, **{n(d['over_armrests'], 0)} mm over the armrests**, {n(d['depth'], 0)} mm deep, "
      f"{n(d['height'], 0)} mm high; seat {n(d['seat_front'], 0)} mm at the front edge (440–460 on the anchors' levelling nuts); 3 seat and 2 back slats; two side frames.")
    A(f"- **Key figures:** side frame {n(m['frame_bare'] + m['frame_draft'], 1)} kg cast, **{n(m['frame'], 1)} kg finished** (world 10.0 + 0.2); slat {n(m['slat'], 2)} kg; "
      f"bolt set {n(m['boltset'], 2)} kg; bench **net {n(m['net'], 1)} kg** (world 43.5), **gross {n(pa['gross'], 1)} kg** (world 44.4) in parcels of {n(pa['carton1'], 1)}, "
      f"{n(pa['carton2'], 1)} and {n(pa['bundle'], 1)} kg; pallet of four {n(ta['pallet_dims'][0], 0)} x {n(ta['pallet_dims'][1], 0)} x {n(ta['pallet_dims'][2], 0)} mm, "
      f"{n(ta['pallet_gross_kg'], 0)} kg (world 200); 24 + 1 pallets {n(ta['load_kg'] / 1000, 2)} t; metal poured {n(c['poured'], 1)} kg per bench at "
      f"**{n(100 * c['yield_'], 0)} % yield** (world 34 kg at 60 %).")
    A(f"- **Strength:** frame at most {n(max(v['sigma_max'] for v in fcases.values()), 0)} MPa against Rp0.2 = {FM['Rp02']} MPa (EN 1563), utilisation "
      f"{n(max(v['util_uls'] for v in fcases.values()), 2)} with γQ = 1.5; slats σ = {n(ua['sigma'], 1)} MPa, utilisation {n(ua['util_d'], 2)} ({n(util30, 2)} in the 30 % case), "
      f"sag {n(ua['w_span'], 1)} mm under 450 kg.")
    A(f"- **Handling (ISO 11228-1):** frame cartons {n(pa['carton1'], 1)} and {n(pa['carton2'], 1)} kg, one person; slat bundle {n(pa['bundle'], 1)} kg, two people because of its length.")
    A("- **Inconsistencies:** @@N@@ remain in section 8 (run 4: 20), all with a recommendation and none needing an owner's decision; the decisions are in "
      "the list of world texts to change (section 2.2).")
    A("")
    A("## 2. Changes in this run")
    A("")
    A("**Owner's decisions (run 5):** stainless **A4** fixings (A4-70 bolts and nuts, A4 washers) for every bench, one bolt set; the frame is ductile cast "
      "iron EN-GJS-400-15, galvanised and powder-coated, and no text calls it steel; Marrowdale Sawmill modifies the ash itself in a thermal modification kiln "
      "and sells the finished modified slat; the slat item, the sawmill delivery (O66) and decision O119 are rewritten for 45 mm thermally modified ash; "
      "galvanising plus powder coat; the modified slats are proved by a type test under UR-SF-0450 and yearly samples. No design change.")
    A("")
    A(f"**What changed:** the bolt set is A4 (EN 1.4401, density 8,000 kg/m³ against 7,930 for A2): {n(m['boltset'], 3)} kg instead of {RUN4['boltset_kg']} kg; the "
      "bill of materials, the drawings (revision E after the maintenance note on drawing 004) and the parameters say A4; the parameters and the drawings no longer call the frame steel (the frame "
      "holes are 'frame holes', the safety factor 'γM0 frame'; cast steel remains only as an alternative in the comparison of section 9). Masses change by "
      "a few grams.")
    A("")
    A("| Figure | World now | Run 1 (oak 38, steel) | Run 2 (ash 38, steel) | Run 3 (ash 45, steel) | Run 4 (ash 45, ductile iron, A2) | Run 5 (A4, final) |")
    A("|---|---|---|---|---|---|---|")
    rows = [
        ("Side frame, cast / finished", "10.0 / 10.2 kg", "– / 13.42 kg", "– / 13.42 kg", f"{RUN3['frame_cast']} / {RUN3['frame']} kg", RUN4["frame"], f"{n(m['frame_bare'] + m['frame_draft'], 2)} / {n(m['frame'], 2)} kg"),
        ("Zinc per frame", "0.2 kg", "0.38 kg", "0.32 kg", "0.32 kg", "0.64 kg", f"{n(m['zinc_typ'], 2)} kg"),
        ("Slat", "4.5 kg", RUN1["slat"], RUN2["slat"], RUN3["slat"], "4.24 kg", f"{n(m['slat'], 2)} kg"),
        ("Bolt set", "1.0 kg", RUN1["boltset"], RUN2["boltset"], RUN3["boltset"], f"{RUN4['boltset_kg']} kg (A2)", f"{n(m['boltset'], 2)} kg (A4, M8 x {bolt_len})"),
        ("Bench net", "43.5 kg", f"{RUN1['net']} kg", f"{RUN2['net']} kg", f"{RUN3['net']} kg", f"{RUN4['net']} kg", f"{n(m['net'], 2)} kg"),
        ("Parcels 1 / 2 / 3", "10.2 / 11.2 / 23.0 kg", f"{RUN1['parcels']} kg", f"{RUN2['parcels']} kg", f"{RUN3['parcels']} kg", f"{RUN4['parcels']} kg", f"{n(pa['carton1'], 1)} / {n(pa['carton2'], 1)} / {n(pa['bundle'], 1)} kg"),
        ("Bench gross", "44.4 kg", f"{RUN1['gross']} kg", f"{RUN2['gross']} kg", f"{RUN3['gross']} kg", f"{RUN4['gross']} kg", f"{n(pa['gross'], 2)} kg"),
        ("Pallet of four: height; goods / gross", "750 mm; 178 / 200 kg", RUN1["pallet"], RUN2["pallet"], RUN3["pallet"], RUN4["pallet"], f"{n(ta['pallet_dims'][2], 0)} mm; {n(ta['pallet_goods_kg'], 1)} / {n(ta['pallet_gross_kg'], 1)} kg"),
        ("24 bench pallets + castings pallet", "about 4.3 t + 0.5 t", f"{RUN1['load']} t", f"{RUN2['load']} t", f"{RUN3['load']} t", f"{RUN4['load']} t", f"{n(ta['load_kg'] / 1000, 2)} t"),
        ("Metal in the frames", "about 21 kg steel", f"{RUN1['steel']} kg steel", f"{RUN2['steel']} kg steel", f"{RUN3['steel']} kg steel", "20.8 kg ductile iron", f"{n(m['metal_in_product'], 1)} kg ductile iron"),
        ("Stainless steel (fixings)", "–", "–", "0.70 kg A2", "0.74 kg A2", "0.74 kg A2", f"{n(m['stainless_fixings'], 2)} kg A4"),
        ("Metal poured / yield", "34 kg / 60 %", "48.9 kg / 52 %", "48.9 kg / 52 %", f"{RUN3['poured']} kg / 54 %", "24.0 kg / 85 %", f"{n(c['poured'], 1)} kg / {n(100 * c['yield_'], 0)} %"),
        ("Frame utilisation (worst case)", "–", "0.32", "0.32", "0.33", "0.35", f"{n(max(v['util_uls'] for v in fcases.values()), 2)}"),
        ("Slat utilisation / sag, 450 kg", "–", f"{RUN1['util']} / {RUN1['sag']} mm", f"{RUN2['util']} / {RUN2['sag']} mm", f"{RUN3['util']} / {RUN3['sag']} mm", "0.64 / 8.7 mm", f"{n(ua['util_d'], 2)} / {n(ua['w_span'], 1)} mm"),
    ]
    for row in rows:
        A("| " + " | ".join(row) + " |")
    A("")
    A(f"The sawmill truck is unchanged: {n(trk['total_kg'] / 1000, 2)} t against {n(trk['payload_kg'] / 1000, 1)} t; {trk['floor']} floor positions, two high.")
    A("")
    A("### 2.1 The run-4 design change for ductile iron (kept)")
    A("")
    A(f"- **Wall thickness {f['t_web']} mm** (8 mm in steel). Sources for sand-cast ductile iron disagree: foundry guides give 5–6 mm in green sand "
      "(Minncast; casting-china.org), 5–7 mm as practical minima (metal-castings.com), and Farrar recommends at least 0.300 in (7.6 mm); Bralla's *Design for "
      "Manufacturability Handbook* (via an NPTEL course) makes the minimum depend on length: 5 mm up to 300 mm, 13 mm up to 1.2 m. The members are 240–550 mm "
      "long between junctions: interpolating Bralla at 550 mm gives about 7 mm, which is chosen.")
    A(f"- **Feet {f['feet']['thickness']} mm** (were 10 mm), so that no section's modulus exceeds 4 mm, the limit for green-sand ductile iron without risers "
      f"(QIT/Karsay); foot modulus {n(c['M_foot'], 1)} mm. Fillets R{f['fillet_concave']} inside, R{f['round_convex']} outside (≥ 3 mm, Farrar). Sections otherwise unchanged; "
      f"bolt stack 45 + {f['t_flange']} + 1.6 + 6.8 + 2.5 mm → M8 x {bolt_len}.")
    A("")
    A("### 2.2 World texts that must change (owner's decisions)")
    A("")
    A("| Where | Now | Change to |")
    A("|---|---|---|")
    A("| items.json, bench `description` | 'Park bench, 1800 mm, frame of cast and galvanised steel, five hardwood slats, for bolting to the ground.' | 'Park bench, 1800 mm, frame of galvanised and powder-coated ductile cast iron, five slats of thermally modified ash, for bolting to the ground.' |")
    A("| items.json, property 'Frame material' | 'Cast steel, hot-dip galvanised' | 'Ductile cast iron EN-GJS-400-15, hot-dip galvanised and powder-coated' |")
    A("| items.json, property 'Slat wood' | 'Kiln-dried hardwood' | 'Thermally modified ash' |")
    A(f"| items.json, circularity resource | 'STEEL 34 KGM, Steel made from Serravona ore in Urvania' | two iron lines (O225): 'IRON {n(net_liquid * (1 - FM['scrap_share_pct'] / 100), 1)} KGM' ore-based and 'IRON {n(net_liquid * FM['scrap_share_pct'] / 100, 1)} KGM' recycled, {FM['scrap_share_pct']} % of the frames' iron, the net liquid iron; and a stainless line ({n(m['stainless_fixings'], 2)} kg A4) if wanted |")
    A(f"| items.json, circularity resource | 'HARDWOOD 22.5 KGM, slats from Upland State, Bayvarra' | about {n(m['wood_bench'], 1)} kg of thermally modified ash (or the {n(5 * blank_l * wa['untreated_density'] / 1000, 0)} kg of ash before modification, as O25 decides) |")
    A(f"| items.json, weights | bench 38.0 / 41.5 kg; spare frame 9.5 / 10.2 kg | bench {n(m['net'], 1)} / {n(pa['gross'], 1)} kg; spare frame {n(m['frame'], 1)} / {n(pa['carton1'], 1)} kg |")
    A("| items.json, slat item (slat-1800) | 1,800 x 95 x 38 mm hardwood, kiln-dried 12 %, 4.5 kg | 1,800 x 95 x 45 mm thermally modified ash, about 5 % moisture, " + n(m['slat'], 2) + " kg, made by Marrowdale |")
    A("| 03-world.md, 'The park bench' and the Valdara story | 'cast and galvanised steel side frames', Valdara 'makes its own steel' | 'ductile cast iron side frames, galvanised and powder-coated'; Valdara makes iron from Serravona ore and casts it in its own foundry |")
    A(f"| decisions: D20 parts and parcels, O66 truck, O119 woods | 10.0 kg frames, 1.0 kg bolts, 23.0 kg bundle; 21.6 t of slats at 4.5 kg; oak now, ash from May | the figures of this report; {n(trk['total_kg'] / 1000, 1)} t per sawmill truck; one wood (thermally modified ash, 45 mm) |")
    A("| maintenance text | 'tighten the slat bolts and touch up the coating once a year' | 'once a year: tighten the slat bolts, touch up the frame coating, clean the slats and check them for splits' |")
    A("| datasheet VI-DS-B180 | – | 'The slats are left untreated and turn silver-grey; only the end grain is sealed before delivery.' |")
    A(f"| items.json, dimensions | LENGTH 1,800 'Over the armrests' | LENGTH 1,800 'Over the slats' and a second length {n(d['over_armrests'], 0)} 'Over the armrests' |")
    A("| items.json, spare frame `hs` | 7325.99 | 9401.99 (part of a seat); national tariff line to match |")
    A("")
    A("**Decided by the owner (final):**")
    A("")
    A("- **Tariff:** the spare side frame VI-C180 is a part of a seat, **HS 9401.99**, as the story says: it is identifiable as made only for the bench, and "
      "heading 94.01 with its Explanatory Note covers identifiable parts of seats. The bench stays **9401.79** (other seats with metal frames); bolts and "
      "ground anchors stay in the metal chapters (Chapter 73). Sources named by the owner: WCO heading 94.01 and its Explanatory Note; US rulings NY N343523 and "
      "NY N339989 (not read here). The question 7325.10 against 7325.99 for ductile iron (US ruling HQ 959352 against the UK guidance) no longer arises.")
    A(f"- **Length:** both lengths are stated, on drawing 001 and here: **1,800 mm over the slats** (overall length, slat end to slat end) and "
      f"**{n(d['over_armrests'], 0)} mm over the armrests** (outer edges of the two armrest pads).")
    A("- **Slats:** left untreated to grey; only the end grain is sealed at Marrowdale. The datasheet says they turn silver-grey. Yearly maintenance: tighten "
      "the slat bolts, touch up the frame coating, clean the slats and check them for splits (drawing 004, revision E).")
    A("")
    A("## 3. Files")
    A("")
    A("| Path | Content |")
    A("|---|---|")
    A("| `parameters.json` | single source of truth: dimensions, frame materials (`frame_material` selects one), the slat wood, loads, packaging, the world's figures |")
    A("| `build_bench.py`, `report.py`, `render.js` | generator (geometry, analysis, STEP/GLB/SVG, material comparison), this report, the renders; see `README.md` |")
    A("| `results.json` | every derived figure, including `material_comparison` and `sawmill_truck` |")
    A("| `step/` | `VI-B180_assembly.step`, `VI-C180_side_frame.step`, `VI-B180-03_slat.step`, `VI-B180-04_fixing_M8.step`, `VI-C180_mould_cluster.step`, `VI-B180_pallet.step` |")
    A("| `glb/` | `serra180_GRY.glb`, `serra180_GRN.glb`, `serra180_parcels.glb`, `serra180_pallet.glb` (metres, Y up) |")
    A("| `drawings/` | 001 general arrangement, 002 side frame, 003 slat, 004 exploded assembly, 005 bill of materials, 006 parcels, 007 pallet and loading, 008 casting method |")
    A("| `renders/` | modified ash in Ferro grey and Moss green, frame and slat detail, the three parcels, the pallet of four |")
    A("")
    A(f"Render colours are approximations: Ferro grey as RAL 7011 (about #555D61), Moss green as RAL 6005 (about #114232), the modified ash dark brown "
      f"({wa['colour']}); the wood greys outdoors without a finish.")
    A("")
    A("## 4. The design and the reasons for it")
    A("")
    A("### 4.1 Ergonomics and overall form")
    A("")
    A("- **Seat height 450 mm** at the front edge, frames 10 mm above the plinth on the anchors' levelling nuts (0–20 mm gives 440–460 mm), grouted after "
      "levelling. Inclusive Mobility (2021, p. 102) asks 470–480 mm for most seats; the 2010 ADA Standards (903.5) allow 430–485 mm.")
    A(f"- **Armrests 200 mm above the seat** (Inclusive Mobility); seat width between the armrests {n(d['between_armrests'], 0)} mm = 3 x {n(d['seat_width_per_person'], 0)} mm.")
    A(f"- **Seat tilt {P['ergonomics']['seat_tilt_deg']}°, seat-to-back {P['ergonomics']['seat_back_angle_deg']}°** (back {n(d['beta'], 0)}° from vertical), within the "
      "usual 0–5° and 100–110° (Pheasant and Haslegrave, *Bodyspace*, from general knowledge).")
    A(f"- **Seat depth {P['ergonomics']['seat_depth']} mm**: {n(d['seat_surface_depth'], 0)} mm of slat surface and a {n(d['throat'], 0)} mm open throat. **Back:** "
      f"slats at {n(d['back_rel_P'][0], 0)}–{n(d['back_rel_P'][1], 0)} and {n(d['back_rel_P'][2], 0)}–{n(d['back_rel_P'][3], 0)} mm above the seat-back junction; "
      f"top {n(d['back_height_above_seat'], 0)} mm above the seat front.")
    A("")
    A("### 4.2 Side frame: ductile cast iron")
    A("")
    A(f"- One symmetric casting for both sides (VI-C180), T-sections with the flange centred on the web, parting at the web mid-plane, no cores. Members: "
      f"front post ({f['front_post']['depth']} mm, flange {f['front_post']['flange_width']}), armrest ({f['armrest']['depth']}, pad {f['armrest']['flange_width']}), "
      f"seat rail ({f['seat_rail']['depth']}, flange {f['seat_rail']['flange_width']}), back rail ({f['back_rail']['depth']}, flange {f['back_rail']['flange_width']}), "
      f"rear leg ({f['rear_leg']['depth']}, flange {f['rear_leg']['flange_width']}); feet {f['feet']['width']} x 120 x {f['feet']['thickness']} mm with one "
      f"Ø{f['feet']['hole_diameter']} anchor hole each. Walls {f['t_web']} mm; pattern shrinkage {FM['pattern_shrinkage_pct']} % (metal-castings.com gives 1.0–1.2 % for ductile iron).")
    A(f"- **Material:** {FM['grade']}: Rp0.2 ≥ {FM['Rp02']} MPa, Rm ≥ {FM['Rm_min']} MPa, elongation ≥ {FM['elongation_pct']} % for walls up to 30 mm; density "
      f"taken as {FM['density']} kg/m³ (EN 1563 summary; foundries quote 7,100–7,300); E about {FM['E'] // 1000} GPa. Heat treatment: {FM['heat_treatment']} "
      "(thin walls cool fast and can form carbides; general knowledge).")
    A("- **Corrosion protection:** EN ISO 1461 applies to castings (≥ 6 mm: at least 80 µm, 575 g/m² mean). Ductile iron holds about 2–3 % silicon, far "
      "above the low-reactivity windows of steel (below 0.04 % or 0.15–0.22 % Si, AGA); silicon and phosphorus speed up the growth of the zinc-iron layers, "
      "so coatings on cast iron come out thicker and rougher (AGA, 'Galvanizing castings'). The galvanizers' association notes that high-silicon steel reaches "
      f"about 200 µm nominal. The model therefore takes **about {FM['zinc_um_typ']} µm**: {n(m['zinc_typ'], 2)} kg per frame (minimum by EN ISO 1461: "
      f"{n(m['zinc_min'], 2)} kg). Such thick, mostly alloy-layer coatings are more brittle at edges (general knowledge). ISO 14713-2's own text was not accessible here.")
    A("- **Pre-treatment:** chemical cleaning at the galvanizer does not remove moulding sand and surface graphite; the castings are grit- or shot-blasted "
      "first (AGA). After galvanising, a sweep-blast or a suitable pre-treatment before the duplex polyester powder coat "
      f"({P['materials']['powder_coat']['thickness_um']} µm, {n(m['powder'], 2)} kg) (general knowledge for duplex systems).")
    A("")
    A("### 4.3 Fixings")
    A("")
    A(f"- Stainless **A4** for every bench (owner's decision): A4-70 carriage bolts **M8 x {bolt_len}** (ISO 8677), A4-70 nuts, A4 washers (EN 1.4401, "
      "8,000 kg/m³). Thermally modified timber is acidic (pH about 4) and its producers' handbook asks for stainless A2 or acid-resistant A4 fasteners; A4 also "
      "resists the chlorides of coastal sites and salted roads (Lisavu, harbour towns), so one bolt set serves every bench.")
    A("- Stainless bolts on a galvanised frame form a bimetallic contact; acceptable in rural and urban air, with isolating washers at coastal sites "
      "(general knowledge).")
    A(f"- Holes pre-drilled (Ø9 in the slats, Ø10 in the flanges); end distance 80 mm = 10 d, edge distance 47.5 mm = 5.9 d (EN 1995-1-1 minima max(7d; 80 mm) "
      f"and 3d, from general knowledge); square neck seat pre-formed (8.2 mm, 5 mm deep); torque {P['bolts']['torque_Nm']['tm_ash']} N m. Masses: bolt "
      f"{n(1000 * m['bolt'], 1)} g, washer {n(1000 * m['washer'], 1)} g, nut {n(1000 * m['nut'], 1)} g; 20 sets {n(m['stainless_fixings'], 2)} kg, with the bag {n(m['boltset'], 2)} kg.")
    A("")
    A("### 4.4 Slats: thermally modified ash, 45 mm")
    A("")
    A("| Property | Value | Source / basis |")
    A("|---|---|---|")
    A(f"| Size | 1,800 x 95 x {T} mm, planed, chamfers 3 mm, four Ø9 holes | owner's decision |")
    A(f"| Grade before modification | European ash LS13 (DIN 4074-5) → EN 338 D40 via EN 1912 | TU München; EN 1912 covers ash from Germany, Austria, Switzerland |")
    A(f"| Bending strength used | f_m,k = 40 x {wa['strength_ratio']} = {n(sl['f_mk'], 1)} MPa | handbook small clears 112.0 → 90.6 MPa (an assumption that the ratio applies to graded timber) |")
    A(f"| Stiffness used | E = {n(sl['E_d'], 0)} MPa | D40 (EN 338:2016, from general knowledge); handbook small clears show +10 % |")
    A(f"| Density, delivered | {wa['density']} kg/m³ (untreated ash {wa['untreated_density']}) | handbook Table 4, 20 °C / 65 % RH |")
    A(f"| Moisture | about {wa['mc_delivery']} % delivered (4–7 %), about {wa['mc_outdoor'][0]}–{wa['mc_outdoor'][1]} % outdoors (judged; about +{n(100 * mc_out, 0)} % in mass) | handbook: equilibrium moisture 'significantly below 20 %' |")
    A(f"| Durability, use | {wa['durability']} | handbook Table 9 |")
    A("| Other | more brittle: impact strength about −25 %, splitting strength −30 to −40 %; not strength-graded by its producers, who say it 'must not be used for load-bearing structures' | handbook 4.5.2, 4.5.6, 4.5.8 |")
    A(f"| Section, depth factor | W = {n(sl['W'], 0)} mm³, I = {n(sl['I'], 0)} mm⁴, k_h = {n(sl['k_h'], 2)} | |")
    A(f"| **Slat mass** | **{n(m['slat'], 2)} kg** (modelled with holes and chamfers) | |")
    A("")
    A(f"**Supply:** {wa['supply']}. Marrowdale saws and kiln-dries the ash, modifies it at about 212 °C in its "
      "own thermal modification kiln, planes it and delivers the finished slat to Valdara (owner's decision). "
      "*Note (O150, O197, 2026-11-20):* in its summer season, October to March, when its own kiln is full, the "
      "sawmill has the slats modified, planed and end-sealed under contract at Tostara Wood Modification, Conciaro; "
      "the February delivery of the examples is such a job.")
    A("")
    A("**Proof plan (owner's decision):** because thermally modified timber is not strength-graded and Eurocode 5 does not cover it, the slat is proved by "
      "a **type test** of the bench under UR-SF-0450 (450 kg over the seat, one hour, no lasting deformation) and by **yearly samples** from production; "
      f"the ash is graded LS13 before modification. The model's assumed design value gives a utilisation of {n(ua['util_d'], 2)} ({n(util30, 2)} if the "
      "modification costs 30 % of the graded strength), so the test is expected to pass with margin.")
    A("")
    A("### 4.5 Casting process (ductile iron)")
    A("")
    A(f"- **Melting:** {FM['melt']}. Ductile iron needs a low-sulphur base iron; blast-furnace hot metal is a usual base after desulphurisation (general knowledge).")
    A(f"- **Treatment:** {FM['treatment']} (general knowledge; typical practice, not from a source checked here).")
    A(f"- **Mould:** {FM['mould']}. **Pouring temperature {FM['pour_temp_C'][0]}–{FM['pour_temp_C'][1]} °C**, held within ±14 °C, as directly applied "
      "risering requires (QIT/Karsay notes: pouring temperature for DAR depends on the modulus; thin sections need it high).")
    A(f"- **Risering:** graphite expansion during solidification compensates the shrinkage, so ductile iron needs much smaller risers than steel. The "
      f"QIT/Karsay rules: in a weak (green sand) mould, a casting whose significant modulus is at most 4 mm is made by **directly applied risering**, the "
      f"gating or sprue feeding only the liquid contraction; above 4 mm, pressure-control risers; riserless only in rigid moulds above 25 mm. Here the "
      f"significant modulus is {n(c['M_S'], 1)} mm (bars {n(c['M_wall'], 1)} mm, feet {n(c['M_foot'], 1)} mm), so **no risers**. Gates of 4 MN x 4 MN = "
      f"{n(c['gate_w'], 0)} x {n(c['gate_t'], 0)} mm with the contact modulus MN = {n(c['M_N'], 1)} mm (0.7 MS, read from the QIT chart's trend; an assumption), "
      f"at least 5 times as long as thick ({n(c['gate_len'], 0)} mm). Sprue Ø{n(c['d_sprue'], 0)} mm, runner {n(c['run_w'], 0)} x {n(c['run_h'], 0)} mm, pour "
      f"{n(c['W_guess'], 0)} kg in about {n(c['t_pour'], 0)} s.")
    A(f"- **Result:** castings {n(2 * c['casting_kg'], 1)} kg per mould, gating and basin {n(c['gating_kg'], 1)} kg: **poured {n(c['poured'], 1)} kg, yield "
      f"{n(100 * c['yield_'], 0)} %**. Junctions that are thicker than the bars (the main junction J) rely on graphite expansion in a mould that holds; "
      "a foundry would confirm with a trial casting or simulation.")
    A("")
    A("### 4.6 Packaging and transport")
    A("")
    A(f"- Frame carton {n(co[0], 0)} x {n(co[1], 0)} x {n(co[2], 0)} mm (frame {n(fb[2], 0)} x {n(fb[1], 0)} x {n(fb[0], 0)} mm), tray and lid, {n(pk['carton_kg'], 2)} kg. "
      f"Slat bundle 3 + 2, {n(bu[0], 0)} x {n(bu[1], 0)} x {n(bu[2], 0)} mm, packing {n(pk['bundle_pack_kg'], 2)} kg. Pallet {P['packaging']['pallet']['length']} x "
      f"{P['packaging']['pallet']['width']} x {n(pk['pallet_h'], 0)} mm, {n(pk['pallet_kg'], 1)} kg; loaded {n(ta['pallet_dims'][0], 0)} x {n(ta['pallet_dims'][1], 0)} x "
      f"{n(ta['pallet_dims'][2], 0)} mm. Trailer / 40-foot / 45-foot: {ta['trailer']['floor']} / {ta['container_40']['floor']} / {ta['container_45']['floor']} floor positions, "
      f"{ta['trailer']['layers_fit']} / {ta['container_40']['layers_fit']} / {ta['container_45']['layers_fit']} layers by height; 25 pallets need {ta['floor_needed']} positions in two layers; "
      f"load {n(ta['load_kg'] / 1000, 2)} t, within every payload.")
    A("")
    A("## 5. Figures for the footprint (O25), per bench")
    A("")
    raw = FM["raw_per_t_liquid"]
    A("| Figure | Value | Note |")
    A("|---|---|---|")
    A(f"| Cast iron in the product (2 frames with draft allowance, without zinc) | {n(m['metal_in_product'], 2)} kg | EN-GJS-400-15, volume x {FM['density']} kg/m³ + 2 % |")
    A(f"| Metal poured | {n(c['poured'], 1)} kg | yield {n(100 * c['yield_'], 0)} %; returns {n(c['poured'] - 2 * c['casting_kg'], 1)} kg remelted |")
    A(f"| Liquid iron consumed net | {n(net_liquid, 1)} kg | castings + melt loss {P['casting']['melt_loss_pct']} % of poured + fettling (assumed rates) |")
    A(f"| Zinc (2 frames) | {n(m['zinc_bench'], 2)} kg | about {FM['zinc_um_typ']} µm on reactive iron; EN ISO 1461 minimum {n(m['zinc_bench_min'], 2)} kg |")
    A(f"| Powder coat (2 frames) | {n(m['powder_bench'], 2)} kg | {P['materials']['powder_coat']['thickness_um']} µm polyester |")
    A(f"| Stainless steel A4 (20 bolts, nuts, washers) | {n(m['stainless_fixings'], 2)} kg | EN 1.4401, every bench |")
    A(f"| Wood in the product (5 slats) | {n(m['wood_bench'], 2)} kg | thermally modified ash, about {wa['mc_delivery']} % moisture |")
    A(f"| Wood input before modification | {n(5 * blank_l * wa['untreated_density'] / 1000, 1)} kg | untreated ash blanks 1,830 x 101 x {T + 6} mm (assumed) |")
    A(f"| Packaging | {n(pa['packaging'], 2)} kg | cartons {n(2 * pk['carton_kg'], 2)} kg, bundle {n(pk['bundle_pack_kg'], 2)} kg |")
    A(f"| Pallet share | {n((pk['pallet_kg'] + ta['pallet_extra_kg']) / 4, 2)} kg | block pallet {n(pk['pallet_kg'], 1)} kg + {n(ta['pallet_extra_kg'], 1)} kg, per 4 benches |")
    A("")
    A("**Raw materials for the iron** (per tonne of liquid iron, then per bench for the net liquid iron):")
    A("")
    sh = FM["scrap_share_pct"] / 100
    hot = net_liquid * (1 - sh)
    scrap = net_liquid * sh
    A(f"The iron is {n(100 * (1 - sh), 0)} % blast-furnace hot metal from Serravona ore and {n(100 * sh, 0)} % steel and iron scrap "
      "(owner, O225), melted together with the returns in the induction furnace; the ore, the reductant and the limestone go only into the hot metal. "
      f"Per bench: {n(hot, 1)} kg ore-based iron and {n(scrap, 1)} kg recycled iron, {n(net_liquid, 1)} kg in all.")
    A("")
    A("| Input | per t liquid iron | per bench | Basis |")
    A("|---|---|---|---|")
    A(f"| Iron ore (about 62–65 % Fe) | {n(raw['iron_ore_kg'] * (1 - sh), 0)} kg | {n(raw['iron_ore_kg'] * hot / 1000, 1)} kg | {raw['iron_ore_kg']} kg per t hot metal: worldsteel gives 1,370 kg of ore per t of crude steel by the blast furnace route (with 125 kg scrap); per t of iron at about 93 % Fe from 63 % ore about 1,450 kg (own estimate) |")
    A(f"| Steel and iron scrap | {n(1000 * sh, 0)} kg | {n(scrap, 1)} kg | the scrap share of the charge (O225); its melt loss is in the net liquid iron |")
    A(f"| Reductant (coke and injected coal) | about {n(raw['reductant_kg'] * (1 - sh), 0)} kg | {n(raw['reductant_kg'] * hot / 1000, 1)} kg | {raw['reductant_kg']} kg per t hot metal: general knowledge (300–350 kg coke + 150–200 kg coal per t hot metal); worldsteel: 780 kg metallurgical coal per t crude steel |")
    A(f"| Limestone | {n(raw['limestone_kg'] * (1 - sh), 0)} kg | {n(raw['limestone_kg'] * hot / 1000, 1)} kg | {raw['limestone_kg']} kg per t hot metal: worldsteel, per t crude steel (taken as the same) |")
    A(f"| FeSiMg (treatment of all poured iron) | {raw['FeSiMg_kg']} kg | {n(raw['FeSiMg_kg'] * c['poured'] / 1000, 2)} kg | about 1.3 % addition (general knowledge) |")
    A(f"| Inoculant FeSi | {raw['inoculant_kg']} kg | {n(raw['inoculant_kg'] * c['poured'] / 1000, 2)} kg | about 0.2 % (general knowledge) |")
    A("")
    fp = footprint(FM, net_liquid)
    A("**The footprint with the scrap share** (O225; kg CO2e a bench). The published figures of the all-ore iron are split with the factors below; "
      "the iron's part is scaled to the hot metal, and the scrap adds its own sourcing and melting. Cut-off approach as in EN 15804: scrap carries no burden "
      "of its first life. The factors are stated, not sourced (`parameters.json`, `footprint`).")
    A("")
    A("| Stage | All ore | Of it the iron | With 35 % scrap | Factors |")
    A("|---|---|---|---|---|")
    A(f"| Sourcing, A1–A2 | {fp['pub']['A1_A2']} | {n(fp['iron_a12_old'], 1)} | {n(fp['a12'], 1)} → **{fp['a12_r']}** | ore {fp['F']['ore_sourcing_kg_per_kg_ore']}, reductant {fp['F']['reductant_sourcing_kg_per_kg']}, limestone {fp['F']['limestone_sourcing_kg_per_kg']} kg CO2e/kg on the hot metal's inputs; scrap {fp['F']['scrap_sourcing_kg_per_kg']} kg CO2e/kg |")
    A(f"| Manufacturing, A3 | {fp['pub']['A3']} | {n(fp['iron_a3_old'], 1)} | {n(fp['a3'], 1)} → **{fp['a3_r']}** | hot metal {fp['F']['hot_metal_kg_per_kg']} kg CO2e/kg; scrap melting {fp['F']['scrap_melt_kwh_per_kg']} kWh/kg at {fp['F']['grid_kg_per_kwh']} kg CO2e/kWh |")
    A(f"| From the mine to the gate | {fp['pub']['A1_A2'] + fp['pub']['A3']} | | **{fp['a12_r'] + fp['a3_r']}** | |")
    A("")
    A("## 6. Derived figures")
    A("")
    A("### 6.1 Masses")
    A("")
    A("| Part | Mass |")
    A("|---|---|")
    A(f"| Side frame, cast ({n(m['frame_volume_l'], 3)} l) + draft {f['draft_mass_allowance_pct']} % | {n(m['frame_bare'] + m['frame_draft'], 2)} kg |")
    A(f"| Zinc typical / powder coat, per frame | {n(m['zinc_typ'], 2)} / {n(m['powder'], 2)} kg |")
    A(f"| **Side frame, finished (each)** | **{n(m['frame'], 2)} kg** |")
    A(f"| Slat (each) | {n(m['slat'], 2)} kg |")
    A(f"| Bolt set | {n(m['boltset'], 2)} kg |")
    A(f"| **Bench net** | **{n(m['net'], 2)} kg** |")
    A(f"| Centre of gravity (x, y, z) | {', '.join(n(v, 0) for v in m['bench_cg'])} mm |")
    A("")
    A("### 6.2 Parcels and pallet")
    A("")
    A("| Unit | Size (mm) | Gross | Handling |")
    A("|---|---|---|---|")
    A(f"| Parcel 1: frame carton | {n(co[0], 0)} x {n(co[1], 0)} x {n(co[2], 0)} | {n(pa['carton1'], 1)} kg | one person |")
    A(f"| Parcel 2: frame carton with bolt set | same | {n(pa['carton2'], 1)} kg | one person |")
    A(f"| Parcel 3: slat bundle | {n(bu[0], 0)} x {n(bu[1], 0)} x {n(bu[2], 0)} | {n(pa['bundle'], 1)} kg | two people (length) |")
    A(f"| Bench gross | | **{n(pa['gross'], 1)} kg** | |")
    A(f"| Pallet of four (goods / gross) | {n(ta['pallet_dims'][0], 0)} x {n(ta['pallet_dims'][1], 0)} x {n(ta['pallet_dims'][2], 0)} | {n(ta['pallet_goods_kg'], 1)} / {n(ta['pallet_gross_kg'], 1)} kg | fork-lift |")
    A(f"| Castings pallet (12 frame cartons) | 1,850 x 700 x {n(ta['castings_pallet_h'], 0)} | {n(ta['castings_pallet_kg'], 1)} kg | fork-lift |")
    A(f"| 24 bench pallets + castings pallet | | {n(ta['load_kg'] / 1000, 2)} t | |")
    A("")
    A("### 6.3 Strength and deflection")
    A("")
    A("**Load cases.** UR-SF-0450: 450 kg over the seat between the armrests, equal on the three seat slats, one hour. EN 581-2 contract use (preview values; "
      "methods in EN 1728): seat 2,000 N with 750 N on the other seats, back 560 N, arm 900 N, front edge 1,300 N; seat pad 300 mm long (assumption).")
    A("")
    A(f"**Safety factors.** γQ = 1.5 (EN 1990); f_m,d = f_m,k · k_mod · k_h / γM = {n(sl['f_mk'], 1)} x 0.70 x {n(sl['k_h'], 2)} / 1.3 = {n(sl['f_md'], 1)} MPa "
      "(EN 1995-1-1, short-term, service class 3; from general knowledge). Eurocode 5 has no values for thermally modified timber; the design value is the "
      f"model's assumption. Frame against Rp0.2 / γM = {FM['Rp02']} / {FM['gamma_M']} MPa.")
    A("")
    A(f"**Slats** (span 1,600 mm, overhangs 100 mm):")
    A("")
    A("| Load case | σ (MPa) | 1.5σ / f_m,d | Sag (mm) | span / sag |")
    A("|---|---|---|---|---|")
    for k, v in sl["cases"].items():
        A(f"| {k} | {n(v['sigma'], 1)} | {n(v['util_d'], 2)} | {n(v['w_span'], 1)} | {n(v['L_over_w'], 0)} |")
    A("")
    A(f"**Sensitivity (450 kg test):** modification costing 30 % of the graded strength (f_m,k {n(f_mk30, 0)} MPa): utilisation **{n(util30, 2)}**; "
      f"service class 2 (k_mod 0.90, arguable because the wood stays below 20 % moisture): {n(util_sc2, 2)}.")
    A("")
    A("**Side frame** (plane-frame model, pinned feet):")
    A("")
    A("| Load case | σ max (MPa) | in | 1.5 σ / (Rp0.2/γM) | foot reactions front / rear (N) |")
    A("|---|---|---|---|---|")
    for k, v in fcases.items():
        A(f"| {k} | {n(v['sigma_max'], 1)} | {v['member']} | {n(v['util_uls'], 2)} | {n(v['R_front'], 0)} / {n(v['R_rear'], 0)} |")
    A("")
    A("## 7. The world's figures against the model")
    A("")
    A("| Figure | World now | Model | If adopted |")
    A("|---|---|---|---|")
    rows = [
        ("Length over the armrests", "1,800 mm", f"{n(d['over_armrests'], 0)} mm (1,800 over the slats)", "LENGTH qualified 'over the slats'"),
        ("Depth / height / seat height", "620 / 780 / 450 (440–460)", f"{n(d['depth'], 0)} / {n(d['height'], 0)} / {n(d['seat_front'], 0)} (440–460)", "no change"),
        ("Slats", "5 hardwood, 1,800 x 95 x 38, kiln-dried 12 %, 4.5 kg", f"5 thermally modified ash, 1,800 x 95 x {T}, about 5 %, {n(m['slat'], 2)} kg", "slat item, sawmill delivery, bench weights"),
        ("Side frame", "10.0 + 0.2 kg, cast steel", f"{n(m['frame_bare'] + m['frame_draft'], 1)} kg cast, {n(m['frame'], 2)} kg finished, ductile iron", "frame weights; material"),
        ("Bolt set", "1.0 kg", f"{n(m['boltset'], 2)} kg stainless A4, M8 x {bolt_len}", "material and length"),
        ("Bench net / gross", "43.5 / 44.4 kg", f"{n(m['net'], 1)} / {n(pa['gross'], 1)} kg", "weights in about 50 documents"),
        ("Parcels", "10.2 / 11.2 / 23.0 kg", f"{n(pa['carton1'], 1)} / {n(pa['carton2'], 1)} / {n(pa['bundle'], 1)} kg", "parcel weights"),
        ("Frame carton", "820 x 620 x 80", f"{n(co[0], 0)} x {n(co[1], 0)} x {n(co[2], 0)}", "parcel size"),
        ("Pallet of four", "1,850 x 650 x 750; 178 / 200 kg", f"1,850 x 700 x {n(ta['pallet_dims'][2], 0)}; {n(ta['pallet_goods_kg'], 0)} / {n(ta['pallet_gross_kg'], 0)} kg", "pallet size and weights"),
        ("Floor positions", "21 / 18 / (45')", f"{ta['trailer']['floor']} / {ta['container_40']['floor']} / {ta['container_45']['floor']}", "no change"),
        ("Metal poured / yield", "34 kg / 60 %", f"{n(c['poured'], 1)} kg iron / {n(100 * c['yield_'], 0)} %", "O25"),
        ("Metal in the product", "about 21 kg steel", f"{n(m['metal_in_product'], 1)} kg cast iron + {n(m['stainless_fixings'], 2)} kg stainless", "O25"),
        ("Hardwood consumption", "22.5 kg", f"{n(m['wood_bench'], 1)} kg in the product", "O25"),
        ("Sawmill truck", "21.6 t of slats", f"{n(trk['total_kg'] / 1000, 1)} t with pallets", "O66 text"),
        ("Carbon footprint, mine to gate", "69 kg CO2e (26 + 43, all ore)",
         f"{footprint(FM, net_liquid)['a12_r']} + {footprint(FM, net_liquid)['a3_r']} kg CO2e with {FM['scrap_share_pct']} % scrap "
         "(stated factors)", "O225"),
    ]
    for row in rows:
        A("| " + " | ".join(row) + " |")
    A("")
    A("## 8. Inconsistencies found")
    A("")
    A("**Decided in the final round:** the two lengths (1,800 mm over the slats, " + n(d['over_armrests'], 0) + " mm over the armrests), the spare frame's "
      "tariff line (9401.99) and the slats' finish and maintenance (untreated, end grain sealed, yearly cleaning and split check); see section 2.2.")
    A("**Resolved or turned into decisions since run 4:** the word 'steel' in the world's data, the steel figures for O25 and the slat story (now the "
      "change list of section 2.2); A2 at the coast (A4 everywhere); the thick zinc on reactive iron (galvanising plus powder coat decided, with blast "
      "cleaning and an agreed thickness range); the slat's design value (type test and yearly samples decided). Earlier: cast steel for bench ends, the "
      "slats' margin, ash and beech outdoors, the centre support.")
    A("")
    items = [
        ("Side frame 10.0 kg + 0.2 kg zinc",
         f"The ductile-iron casting weighs {n(m['frame_bare'] + m['frame_draft'], 2)} kg, close to the world's 10.0 kg; the zinc on reactive iron is about "
         f"{n(m['zinc_typ'], 2)} kg and the powder coat {n(m['powder'], 2)} kg: finished {n(m['frame'], 2)} kg, not 10.2.",
         f"(a) {n(m['frame_bare'] + m['frame_draft'], 1)} kg cast, {n(m['frame'], 1)} kg finished.", "(a); in the texts of section 2.2."),
        ("Net 43.5 kg leaves out the zinc, and the parcels have weightless cartons",
         f"D20: 2 x 10.0 + 5 x 4.5 + 1.0 = {n(world_net_check, 1)} kg without zinc; the 10.2 kg frame carton is frame plus zinc. A carton weighs {n(pk['carton_kg'], 1)} kg.",
         f"(a) net {n(m['net'], 1)}, gross {n(pa['gross'], 1)} kg.", "(a)."),
        ("Frame carton 820 x 620 x 80 mm", f"The frame is {n(fb[2], 0)} x {n(fb[1], 0)} x {n(fb[0], 0)} mm; the carton {n(co[0], 0)} x {n(co[1], 0)} x {n(co[2], 0)} mm.",
         "(a) about 790 x 680 x 100 mm.", "(a)."),
        ("Pallet of four 1,850 x 650 x 750 mm",
         f"A {n(co[1], 0)} mm carton does not fit a 650 mm pallet; on 700 mm the load is {n(ta['pallet_dims'][2], 0)} mm high. Vehicle counts hold.",
         "(a) 1,850 x 700 x about 745 mm.", "(a)."),
        ("Pallet weights 178 / 200 kg and 4.3 t for 96 benches",
         f"Model: {n(ta['pallet_goods_kg'], 1)} / {n(ta['pallet_gross_kg'], 1)} kg; 24 + 1 pallets {n(ta['load_kg'] / 1000, 2)} t.", "(a) adopt.", "(a)."),
        ("Metal poured 34 kg per bench at about 60 %",
         f"The iron castings weigh {n(2 * c['casting_kg'], 1)} kg and need no risers: {n(c['poured'], 1)} kg poured at {n(100 * c['yield_'], 0)} %.",
         f"(a) {n(c['poured'], 0)} kg at {n(100 * c['yield_'], 0)} %; net liquid iron about {n(net_liquid, 0)} kg.", "(a)."),
        ("Slat bundle 1,800 x 200 x 120 mm", "200 x 120 holds five slats only with a hole; 1,800 mm leaves no end protection.",
         f"(a) 3 + 2, {n(bu[0], 0)} x {n(bu[1], 0)} x {n(bu[2], 0)} mm.", "(a)."),
        ("Seat height 450 mm against the UK's 470–480 mm", "Below Inclusive Mobility's range; inside the ADA's 430–485 mm.", "(a) keep; (b) 470 with an 800 mm back.", "(a)."),
        ("The carriage bolt's square neck in brittle wood", "A square neck pulled into a round hole can split the modified wood.",
         "(a) pre-formed seat, 10 N m (on drawings 003 and 004).", "(a)."),
        ("Stainless A4 bolts on galvanised frames",
         "A4 resists the acid wood and chlorides; stainless and zinc still form a bimetallic contact, which matters most in coastal air.",
         "(a) isolating washers (nylon or EPDM) under the stainless washers at coastal sites; (b) everywhere.", "(a)."),
        ("Handling by a shopper",
         f"ISO 11228-1's 25 kg is for the adult working population; for the general domestic population it gives 10 kg. The cartons ({n(pa['carton1'], 1)}, "
         f"{n(pa['carton2'], 1)} kg) are below 15 kg but above 10 kg; the bundle ({n(pa['bundle'], 1)} kg) is above both.",
         "(a) shoppers' parcels carried to the car or delivered.", "(a)."),
    ]
    L[:] = [x.replace("@@N@@", str(len(items))) for x in L]
    for i, (title, why, opts, rec) in enumerate(items, 1):
        A(f"**{i}. {title}.** {why}")
        A(f"*Options:* {opts} *Recommendation:* {rec}")
        A("")
    A("Figures that **hold**: depth 620, height 780, seat height 450 (440–460); four anchors; 20 bolts; the load test UR-SF-0450 (frame and slats with margin); "
      "repairability; 21 / 18 floor positions and two layers; the parcels within the handling limits; fork-lift pallets stacking two or three high (by height).")
    A("")
    A("## 9. Frame material comparison (for reference; the owner chose ductile iron)")
    A("")
    A("Run 3 compared the three materials for this geometry; the owner has chosen ductile iron. The table is kept, recomputed with the 8 mm feet of revision C "
      "(stresses scaled from the iron frame model by the seat rail's section modulus, deflections by stiffness). `materials.frame_material` still switches the model.")
    A("")
    A("| Material | Wall | Frame mass, cast (kg) | Zinc (kg) | σ max (MPa) | 1.5 σ / (Rp0.2/γM) | max. deflection (mm) |")
    A("|---|---|---|---|---|---|---|")
    for k in ("cast_steel", "ductile_iron", "aluminium"):
        x = MC["materials"][k]
        for t, v in sorted(x["walls"].items(), key=lambda kv: int(kv[0])):
            A(f"| {x['name']} | {t} mm | {n(v['mass'], 1)} | {n(v['zinc'], 2) if v['zinc'] else '–'} | {n(v['sigma'], 0)} | {n(v['util'], 2)} | {n(v['disp'], 2)} |")
    A("")
    A("(The zinc column uses the EN ISO 1461 minimum x 1.25 for all galvanisable materials; on ductile iron about 200 µm is expected, section 4.2.)")
    A("")
    A("## 10. Handling check (ISO 11228-1)")
    A("")
    A("| Parcel | Mass | Length | ISO 11228-1 reference masses | Verdict |")
    A("|---|---|---|---|---|")
    A(f"| Frame carton | {n(pa['carton1'], 1)} kg | {n(co[0], 0)} mm | 25 kg adult working population; 15 kg general working population; 10 kg domestic | one person (professional); a shopper is helped |")
    A(f"| Frame carton with bolts | {n(pa['carton2'], 1)} kg | {n(co[0], 0)} mm | same | one person (professional) |")
    A(f"| Slat bundle | {n(pa['bundle'], 1)} kg | {n(bu[0], 0)} mm | same; two people: about 2/3 of combined capacity (world rule, about 33 kg) | two people, because of the length |")
    A(f"| Pallet of four | {n(ta['pallet_gross_kg'], 0)} kg | 1,850 mm | – | fork-lift |")
    A("")
    A("## 11. Questions for the owner")
    A("")
    A("All questions are answered and applied: frame of ductile iron; A4 for every bench; the slat item, O66 and O119 rewritten for 45 mm thermally "
      "modified ash; galvanising plus powder coat; type test plus yearly samples for the slats; the spare frame as a part of a seat (9401.99); both lengths "
      "stated; slats untreated with the end grain sealed and the new yearly maintenance. No question is open.")
    A("")
    A("## 12. Limits of the model")
    A("")
    A("- The design values of the thermally modified ash are an assumption. The DAR contact modulus (0.7 MS) is read from the trend of the QIT chart, not "
      "its values; the junctions rely on graphite expansion in green sand. Magnesium treatment, inoculation, pouring speed, melt loss and fettling are typical "
      "values (general knowledge).")
    A("- The zinc thickness on ductile iron (about 200 µm) is an estimate from the galvanizers' statements about reactive (high-silicon) material; it "
      "depends on the iron's silicon and the galvanizer's practice. ISO 14713-2 itself was not accessible.")
    A("- Frame: plane-frame model, in-plane bending of T-sections; draft as a mass allowance.")
    A("- Read in previews or summaries only: EN 581-2, EN 1563, EN 338, EN 350, EN 1912, EN 1706, ISO 11228-1. From general knowledge: EN 1995-1-1, EN 1990, "
      "EN 1993-1-4, EN 1176-1, D40's E0,mean, fastener dimensions, FEFCO 0320, ISPM 15, ISO 668, *Bodyspace*, the reductant rate.")
    A("")
    A("## 13. Sources")
    A("")
    src = [
        ("WCO, Harmonized System heading 94.01 and its Explanatory Note (identifiable parts of seats); US rulings NY N343523 and NY N339989 (named by the owner, not read here)", "https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2022-edition.aspx"),
        ("US Customs and Border Protection, ruling HQ 959352 (1996): ductile cast iron is malleable as first cast; ductile-iron castings in 7325.99, not 7325.10", "https://www.customsmobile.com/rulings/docview?doc_id=959352"),
        ("Classifying iron and steel for import and export (GOV.UK guidance, mirror): spheroidal graphite cast iron is not malleable cast iron", "https://s3.amazonaws.com/thegovernmentsays-files/content/179/1792326.html"),
        ("QIT (Karsay), Risering System Design: DAR for green sand when the significant modulus ≤ 4 mm, PCR above, riserless in rigid moulds above 25 mm; gate 4 MN x 4 MN, length ≥ 5x; pouring temperatures", "https://old.foundrygate.com/upload/artigos/U6KRY5BjXASjloDHwCa2bK59hOC8.pdf"),
        ("NPTEL course on sand casting (after Bralla): ductile iron minimum section 5 mm up to 300 mm, 13 mm up to 1.2 m; section ratio < 2:1, 4:1 taper", "https://archive.nptel.ac.in/content/storage2/courses/107103012/module2/lec1.pdf"),
        ("Farrar Corporation, How to design for ductile iron (minimum 0.300 in, inside radius 1/8 in)", "https://farrarusa.com/how-to-design-for-ductile-iron-tips-for-engineers-and-oems/"),
        ("Minncast, thin-walled sand castings (ductile iron 0.200–0.250 in)", "https://minncast.com/manufacturing-of-thin-walled-sand-castings/"),
        ("Sand casting design guidelines (ductile iron 5–7 mm in green sand; shrinkage 1.0–1.2 %)", "https://metal-castings.com/sand-casting-design-guidelines-draft-angles-wall-thickness-tolerances/"),
        ("American Galvanizers Association, Galvanizing castings (cast and ductile iron: 2–3 % Si, thicker and rougher coatings, blast cleaning first)", "https://galvanizeit.org/knowledgebase/article/galvanizing-castings"),
        ("worldsteel, Steel and raw materials fact sheet (1,370 kg ore, 780 kg coal, 270 kg limestone per t crude steel, BF-BOF)", "https://worldsteel.org/wp-content/uploads/Fact-sheet-raw-materials-2023-1.pdf"),
        ("Producers' handbook on thermal modification (2025): ash at 212 °C, density 625 → 554 kg/m³, bending 112.0 → 90.6 MPa, MOE 12,056 → 13,320 MPa, 4–7 % moisture, pH about 4, A2/A4 fasteners, impact −25 %, splitting −30 to −40 %, not for load-bearing structures, use class 3", "https://thermowood.fi/dataflow/thermowood/files/media/thermowood_handbook_2025_web_17.pdf"),
        ("Ehrhart, Strength grading of hardwoods (TU München): ash LS13 in D40 under EN 1912", "https://mediatum.ub.tum.de/doc/1695273/1695273.pdf"),
        ("Shear tests on European ash glulam (LS13 = D40)", "https://www.researchgate.net/publication/371558301_Shear_tests_on_full-scale_European_ash_glued_laminated_timber_beams"),
        ("Moisture-dependent strength of thermally modified ash (brittleness)", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7178349/"),
        ("EN 1563 EN-GJS-400-15 properties (H2ABC, citing EN 1563:2018)", "https://www.h2abc.com/material/detail.php?mid=azhlNWIxMjY4MjQ%3D"),
        ("EN 1563 summary (SteelNumber)", "http://www.steelnumber.com/en/steel_composition_eu.php?name_id=1520"),
        ("EN AC-42100 datasheet citing EN 1706:2020 (Raffmetal)", "https://www.raffmetal.com/wp-content/uploads/sites/4/EN-42100-AlSi7Mg03-1.pdf"),
        ("EN AC-42100 (SteelNumber, citing EN 1706)", "http://www.steelnumber.com/en/steel_alloy_composition_eu.php?name_id=1225"),
        ("American Galvanizers Association, design guide (cast and ductile iron can be galvanized)", "https://galvanizeit.org/uploads/publications/Design-Guide-AGA-2023-reduced-size_2024-09-10-171216_zgwg.pdf"),
        ("Galvanizers Association datasheet 4a (2024): EN ISO 1461 castings, silicon and reactivity, grit blasting", "https://www.wedge-galv.co.uk/wp-content/uploads/2024/10/4a-Specifying-Hot-Dip-Galvanized-steel-2024.pdf"),
        ("EN 581-2 (iTeh preview) and SIST EN 581-2:2016 sample", "https://cdn.standards.iteh.ai/samples/40324/2427b153643540bf81ea9c3c997ea884/SIST-EN-581-2-2016.pdf"),
        ("Department for Transport, Inclusive Mobility (2021), p. 102", "https://assets.publishing.service.gov.uk/media/61d32bb7d3bf7f1f72b5ffd2/inclusive-mobility-a-guide-to-best-practice-on-access-to-pedestrian-and-transport-infrastructure.pdf"),
        ("U.S. Access Board, 2010 ADA Standards, 903 Benches", "https://www.access-board.gov/ada/#ada-903"),
        ("EN 10293 property table (Olbersdorfer Guss)", "http://www.olbersdorfer-guss.de/en/werkstoffe/stahlguss-din-en-10293.html"),
        ("SFSA, Ordering Steel Castings (6 mm minimum section)", "https://www.sfsa.org/subject-areas/education/ordering-steel-castings/"),
        ("Carlson and Beckermann, feeding rules for steel castings", "https://beckermann.lab.uiowa.edu/sites/beckermann.lab.uiowa.edu/files/2023-10/2000-2.1%20Application%20of%20New%20Feeding%20Rules.pdf"),
        ("Galvanizers Association, EN ISO 1461", "https://galvanizing.org.uk/galvanizing-standards/iso-1461/"),
        ("USDA FPL, Wood Handbook FPL-GTR-282, chapter 5", "https://research.fs.usda.gov/download/treesearch/62244.pdf"),
        ("ISO 11228-1:2021 sample (reference masses)", "https://cdn.standards.iteh.ai/samples/76820/f0ddadd06e294d45838da9dce4820fa5/ISO-11228-1-2021.pdf"),
    ]
    for a_, b_ in src:
        A(f"- {a_}: <{b_}>")
    A("")
    A("The handbook is published by the producers' association of thermally modified timber; its trade and class names are not used in the world.")
    A("")
    (here / "report.md").write_text("\n".join(L), encoding="utf-8")
