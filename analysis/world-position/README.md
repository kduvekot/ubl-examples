# The position of the world on the real ocean

Where the fictional countries lie in the South Atlantic, and why: decision D19 in `analysis/worklist-decisions.md`
(2026-11-16), with what changed later. The map is now leading (O152, owner 2026-11-18), so the extents below come
from the drawn land, not from D19's box.

- **Squares and coordinates:** a map square is 3.5 km each way (256 × 192 squares; `km_per_tile` in
  `world/countries.json`). Coordinates keep that scale on both axes around the centre of each area: a degree of
  latitude is 111.0 km, a degree of longitude 111.32 km × cos(latitude of the area's centre)
  (`coordinate()` in `tools/build_examples.py`; the rule is repeated at the head of `analysis/place-list.md`).
- **The mainland** is centred on 30.0° South, 15.0° West (square 91.5/94), the middle of D19's box. Its land
  reaches about 28.2° to 31.8° South and 17.9° to 12.0° West (with a few islets just beyond: 28.18° to 31.87° S,
  18.02° to 12.05° W), 550 × 411 km and about 159,500 km².
- **Lisavu** is drawn nearer on the map, as an inset (O92, O151), but its squares are placed around its true centre,
  33.0° South, 2.65° West (square 225/112), on a seamount of the Walvis Ridge: about 116 × 85 km and 7,160 km²,
  32.57° to 33.42° S, 3.30° to 1.85° W. Lumeport to Selanu is about 1,080 km in a straight line.
- **The decisions:**
  - **D19** (2026-11-16) put the world on the high seas astride the Mid-Atlantic Ridge, after the first proposal on
    the Rio Grande Rise was withdrawn because Brazil claims that plateau. Its square of 14 km and its box of 28.1° to
    31.9° S, 17.7° to 12.3° W are replaced by the 3.5 km grid and the extents above (O92, 2026-11-18).
  - **O152** "the map is leading" (owner, 2026-11-18): the land is generated from its geology (`tools/terrain.py`),
    and distances, positions and the place list follow the map.
  - **O151** (owner, 2026-11-18): the printed map is an A3 landscape sheet at 1 : 2,500,000, in two panels of
    style C, the mainland and Lisavu at the same scale, with the note that Lisavu lies about 1,100 km east of Lumeport.
  - **O55** (open point): the check against real zones, claims and licences. Done here; see "Sources and limits".

| File | What it is |
|---|---|
| `world-position.png` | The current base: the mainland and Lisavu drawn from the terrain at their positions in WGS 84, on the sea floor of the South Atlantic, with the real 200-nautical-mile zones and extended-shelf claims (Marine Regions) and the shortest gaps to the nearest limits. |
| `plot_world_position.py` | Draws it. |
| `world_outline.py` | The world's land and coast in WGS 84, from the terrain and the coordinate rule; used by the two scripts. |
| `check_maritime_claims.py` | The check of O55: whether any part of the world, or any coordinate in the examples, lies inside a zone, a claim or a sea-bed contract area, and the distances to each and to real land. |
| `world-position-rio-grande-rise-withdrawn.png` | The first proposal, on the Rio Grande Rise. Withdrawn: Brazil has claimed that plateau as continental shelf since 7 December 2018. Kept so that the reason stays visible. |
| `plot_world_position_rio_grande_rise.py` | Draws it. |
| `refine_map.py` | Draws the printed map sheet (O151): A3 landscape at 1 : 2,500,000 and 300 dpi (4,961 × 3,508 pixels), the mainland and Lisavu in two panels. The site build draws it from the world data at every build and publishes it as `map-sheet.png` (owner, 2026-11-19), so it is not committed; its earlier versions are in the history of `world-roadmap.png`. It can also draw a road map, top-down from the 3D tile model and the terrain's fine rasters: relief, land cover, rivers, the towns' built-up areas, villages, roads, rail and pipelines. |
| `site_villages.py` | Sites the villages between the towns (O152) and writes `world/map.json` "villages". |

## How to redraw

    pip install numpy matplotlib pillow shapely pyproj      (in a virtual environment)
    python3 -I analysis/world-position/check_maritime_claims.py
    python3 -I analysis/world-position/plot_world_position.py

The scripts fetch their data once into `.review/geo/`, which is not committed: the depth grid from NOAA
(`etopo.csv`), the Marine Regions layers (`mr-*.json`, `land-south-atlantic.json`) and the UN documents read with
`pdftotext` (poppler-utils), which is optional.

The map sheet, from the repository root (`refine_map.py` needs numpy and Pillow, and the DejaVu fonts):

    python3 tools/world_model.py model.json
    python3 -I analysis/world-position/refine_map.py model.json world/map.json map-sheet.png 5 0 sheet

The fourth argument is the number of relief levels, the fifth the pixels per square (the sheet computes its own,
16.5 at 300 dpi); `sheet periods` colours the towns' built-up areas by the period of their districts, and
`... out.png 5 6 roadmap` draws a road map instead. The villages, which need numpy, scipy, numba and Pillow:

    python3 -I analysis/world-position/site_villages.py
    python3 tools/lay_routes.py
    python3 tools/world_model.py

## Sources and limits

### O55: the check against real zones, claims and licences (2026-11-19)

**Verdict: both areas lie on the high seas, outside every 200-nautical-mile zone, every extended continental shelf
claim and every International Seabed Authority (ISA) exploration area.** No shift is needed. The same holds for the
seven coordinates the examples state (the offshore platform at 27.51° S, 15.49° W is the northernmost). Every land
cell of both areas lies inside Marine Regions' "high seas" polygon.

**What was checked:**

- **200-nautical-mile zones:** every zone in the South Atlantic in Marine Regions' World EEZ v12, and, for the
  British islands, the official outer limits the United Kingdom deposited with the UN Secretary-General: Tristan da
  Cunha (with Gough), St Helena and Ascension (Legal Notices 1, 16 and 2 of 2017; deposit M.Z.N.150.2019.LOS of
  6 December 2019, coordinates in WGS 84). Brazil's zone around Trindade and Martim Vaz, Namibia's, South Africa's
  and every other zone from Marine Regions.
- **Extended continental shelf:**
  - every submission, recommendation and deposit in Marine Regions' World Extended Continental Shelves v2;
  - Brazil's partial revised submission for the Oriental and Meridional Margins of 7 December 2018, which takes in
    the Rio Grande Rise, in the amended executive summary of 12 March 2025 (2,173 outer-limit points, read from the
    UN document); the CLCS has not yet made recommendations on it;
  - the United Kingdom: its only South Atlantic submission for the St Helena dependencies was for Ascension
    (9 May 2008), and the CLCS recommended on 15 April 2010 that the United Kingdom not establish outer limits
    beyond 200 nautical miles there. The UK made no submission and filed no preliminary information for St Helena
    or Tristan da Cunha; its submission of 11 May 2009 for the Falkland Islands, South Georgia and the South Sandwich
    Islands was stated to be its last before the deadline of 13 May 2009;
  - Namibia (submission of 12 May 2009, no recommendations yet), South Africa (recommendations of 17 March 2017 on
    its mainland submission), Argentina (outer limit in Law 27.557 of 2020, deposited), Uruguay, Angola and Norway
    (Bouvetøya).
- **ISA exploration contracts** (ISA list read 2026-11-19): the three polymetallic-sulphide contracts on the
  Mid-Atlantic Ridge all lie in the North Atlantic (Russian Federation 12.8° to 20.9° N; Ifremer, France, 21.0° to
  26.2° N; Poland 26.2° to 32.8° N). The only South Atlantic contract, CPRM's (Brazil) for cobalt-rich crusts on the
  Rio Grande Rise (29.8° to 32.0° S, 36.5° to 32.8° W, signed 9 November 2015), was voluntarily terminated with
  effect from 27 June 2022.

**The distances** (geodesic on WGS 84, from the nearest point of each area's coast; the positions are good to about
2 km):

| From | To | km | nautical miles |
|---|---|---:|---:|
| Mainland (south coast, 31.85° S, 13.61° W) | 200-nautical-mile limit of Tristan da Cunha (official deposit) | 220 | 119 |
| Mainland | Tristan da Cunha, land | 591 | 319 |
| Mainland (west coast) | Brazil's claimed outer limit on the Rio Grande Rise (2025 amended summary) | 861 | 465 |
| Mainland | Gough Island, land | 990 | 535 |
| Mainland | 200-nautical-mile limit of Trindade and Martim Vaz (Brazil) | 1,066 | 576 |
| Mainland | Namibia's claimed outer limit (2009 submission) | 1,192 | 643 |
| Mainland | 200-nautical-mile limit of St Helena (official deposit) | 1,205 | 651 |
| Mainland | ISA area on the Rio Grande Rise (terminated) | 1,430 | 772 |
| Mainland | Trindade and Martim Vaz, land | 1,435 | 775 |
| Mainland | St Helena, land | 1,575 | 850 |
| Mainland | 200-nautical-mile limit of Ascension (official deposit) | 1,864 | 1,007 |
| Mainland | South America, nearest land (Abrolhos, Brazil) | 2,433 | 1,314 |
| Mainland | Africa, nearest land | 2,736 | 1,477 |
| Lisavu (east coast, 32.74° S, 1.85° W) | Namibia's claimed outer limit (2009 submission), at 0.15° E | 188 | 101 |
| Lisavu (west coast) | 200-nautical-mile limit of Tristan da Cunha (official deposit) | 552 | 298 |
| Lisavu | Tristan da Cunha, land | 920 | 497 |
| Lisavu | Gough Island, land | 977 | 527 |
| Lisavu | South Africa's recommended outer limit | 1,194 | 645 |
| Lisavu | 200-nautical-mile limit of St Helena (official deposit) | 1,481 | 800 |
| Lisavu | Africa, nearest land (Namibia) | 1,758 | 949 |
| Lisavu | St Helena, land | 1,852 | 1,000 |
| Lisavu | Brazil's claimed outer limit (2025 amended summary) | 2,210 | 1,193 |

The ISA's sulphide areas in the North Atlantic are more than 5,400 km from the mainland. The nearest coordinate in
the examples to any limit is the Port of Selanu, 217 km (117 nautical miles) from Namibia's claimed outer limit; the
nearest on the mainland, Lumeport's, 298 km (161 nautical miles) from Tristan da Cunha's zone.

**Worth knowing:** Lisavu stands on the Walvis Ridge, and Namibia's submission claims the ridge as its continental
shelf out to about 0.15° E, 188 km east of the island. The island is clear of the claim, which can only shrink
when the CLCS makes its recommendations, but it is the same ridge. If the owner wants more room, the smallest shift
that doubles the gap is to move Lisavu's centre about 1.9° west (to about 33.0° S, 4.5° W: about 175 km, which
shortens the crossing from Lumeport by about as much and stays about 380 km clear of Tristan da Cunha's zone).
Not proposed as needed.

**Sources** (all read on 2026-11-19 unless stated):

- Marine Regions (Flanders Marine Institute, VLIZ), downloads and versions: https://marineregions.org/downloads.php;
  the layers read through its web feature service, https://geo.vliz.be/geoserver/MarineRegions/wfs (World EEZ v12
  of 2023-10-25, World Extended Continental Shelves v2 and World High Seas v2 of 2024-10-10, land polygons);
  the zones' records, for example Tristan da Cunha https://marineregions.org/eezdetails.php?mrgid=8382 and Saint
  Helena https://marineregions.org/eezdetails.php?mrgid=8380.
- UN DOALOS, the United Kingdom's maritime zones (legal notices of 2017 and the deposit M.Z.N.150.2019.LOS):
  https://www.un.org/depts/los/LEGISLATIONANDTREATIES/STATEFILES/GBR.htm; the deposit:
  https://www.un.org/depts/los/LEGISLATIONANDTREATIES/STATEFILES/GBR_Deposit_MZN150.html; the coordinate lists, for
  example https://www.un.org/depts/los/LEGISLATIONANDTREATIES/PDFFILES/DEPOSIT/GBR_Tristan_da_Cunha_EEZ_geographical_coordinates.pdf
  and https://www.un.org/depts/los/LEGISLATIONANDTREATIES/PDFFILES/DEPOSIT/GBR_St_Helena_EEZ_geographical_coordinates.pdf.
- UN DOALOS, Brazil's maritime zones (Law 8.617 of 1993, the EEZ outer limit deposited in 2004):
  https://www.un.org/depts/los/LEGISLATIONANDTREATIES/STATEFILES/BRA.htm.
- CLCS, the list of submissions: https://www.un.org/depts/los/clcs_new/commission_submissions.htm; preliminary
  information: https://www.un.org/depts/los/clcs_new/commission_preliminary.htm.
- CLCS, Brazil's Oriental and Meridional Margins (2018) and the amended executive summary of 12 March 2025:
  https://www.un.org/depts/los/clcs_new/submissions_files/submission_bra_rev3.htm,
  https://www.un.org/depts/los/clcs_new/submissions_files/bra02_rev18/BR-OMM-2ndVER-ExecutiveSummary.pdf.
- CLCS, the United Kingdom for Ascension Island and the summary of recommendations (2010):
  https://www.un.org/depts/los/clcs_new/submissions_files/submission_gbr.htm,
  https://www.un.org/depts/los/clcs_new/submissions_files/gbr08/gbr_asc_isl_rec_summ.pdf; the Falkland Islands,
  South Georgia and the South Sandwich Islands (2009):
  https://www.un.org/depts/los/clcs_new/submissions_files/submission_gbr_45_2009.htm.
- CLCS, Namibia (2009): https://www.un.org/depts/los/clcs_new/submissions_files/submission_nam_50_2009.htm;
  South Africa (2009, recommendations 2017):
  https://www.un.org/depts/los/clcs_new/submissions_files/submission_zaf_31_2009.htm.
- Argentina, Law 27.557 (outer limit of the continental shelf), official text:
  https://www.argentina.gob.ar/normativa/nacional/ley-27557-341415/texto; as deposited with the UN:
  https://www.un.org/depts/los/LEGISLATIONANDTREATIES/PDFFILES/DEPOSIT/ARGLey27557.pdf.
- ISA, exploration contracts: https://isa.org.jm/exploration-contracts/; sulphides:
  https://isa.org.jm/exploration-contracts/polymetallic-sulphides/; cobalt-rich crusts (CPRM terminated):
  https://isa.org.jm/exploration-contracts/cobalt-rich-ferromanganese-crusts/; the block coordinates of CPRM:
  https://www.isa.org.jm/wp-content/uploads/2022/10/CPRMTemplate_Final4_0.pdf; Ifremer:
  https://www.isa.org.jm/wp-content/uploads/2022/10/Public-information-on-contracts-Ifremer_PMS.pdf; the Russian
  Federation (ISBA/17/C/12): https://www.isa.org.jm/wp-content/uploads/2022/06/isba-17c-12_0.pdf; Poland
  (ISBA/23/C/11): https://isa.org.jm/wp-content/uploads/2022/06/isba-23c-11_1.pdf.
- Background on Brazil's claim to the Rio Grande Rise, in Portuguese (Ipea, Texto para Discussão 3157, 2025):
  https://repositorio.ipea.gov.br/entities/publication/931e9828-61f9-42af-974b-1113be196b92.

### Limits and what is still open

- **Sea floor:** NOAA ETOPO1, one value every 10 arc-minutes, from NOAA's ERDDAP server (the address is in the
  script), fetched 2026-11-19. At that spacing (about 18 km) small islands do not show; the coasts on the map are
  Marine Regions' land polygons.
- **The zones** are those published by Marine Regions and, for the British islands, the official deposit; the two
  agree to within 3 km. Marine Regions' extended-shelf layer has Brazil's 2018 line; the 2025 amended line lies
  about 25 km nearer the mainland and is used for the distance. The ISA areas are measured to the box round their
  blocks, which is nearer than the blocks themselves.
- **Still open, for the owner:** a nautical chart for both areas (none was available here; the depth grid and the
  land polygons show no land in either area, but a chart, for example the UK Hydrographic
  Office's small-scale charts of the South Atlantic, would confirm it); winds and climate from a source (still from
  general knowledge, D19). Claims change: Namibia's and Brazil's submissions are still before the CLCS, and new
  ISA applications appear on its list, so the check should be run again before the position is cited anywhere
  outside the world.
