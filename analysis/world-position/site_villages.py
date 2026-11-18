"""Site the villages of the map between the towns (O152, owner 2026-11-18): writes world/map.json "villages".

The villages are on the map only: no parties, no documents. Each has a reason for its site, a living, a founding
consistent with the history (O153), a population band and the way its people farm the land round it ("farming",
which tools/land_use.py turns into the land use the model and both maps draw). About 45 larger ones have names,
given below (NAMED) with their story; the rest are unnamed dots, their reason and living read from their site.

Method:
  * the land per square of 3.5 km from the terrain (tools/terrain_lib.py, recomputed here for the rain, which the
    committed terrain does not keep): height, slope, rain, cover, the streams and their confluences, the river,
    the coast and its shelter, the foot of the hills (a spring line), the roads and railways already laid;
  * a region per square: the wet west and the river valley (old Urvanian farming land: villages about 10 to 11 km
    apart), the drier Urvanian hills (about 12.5 km), Bayvarra's wheat-and-sheep land (about 19 km) and its dry
    east and plateau (the British-era stations, about 30 km), the large forests (about 25 km), Lisavu's lee side
    and its wet windward side; none in the mountains (over 850 m or steep) or the marsh;
  * a village may not stand on a way, a party, an airport's approach, a bridge or its approach, the managed
    forest, within 2 squares of a pipeline (its built-up area keeps 1 square from the right of way), or in or
    next to a town's built-up area;
  * the named villages are placed first; then the best squares (farmland, water, a confluence, the river, a
    sheltered cove, a road or a railway beside it) are taken in turn, each keeping its region's spacing from the
    villages already placed (Poisson-disc sampling).
The minor roads to the villages are laid by tools/lay_routes.py.

Needs numpy, scipy, numba and Pillow (as tools/terrain.py). Usage, from the repository root:
    python3 -I analysis/world-position/site_villages.py           write world/map.json "villages"
Then: python3 tools/lay_routes.py (the minor roads), python3 tools/world_model.py (the checks).
"""
import importlib.util
import json
import math
import os
import sys

import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

CTY = {"U": "XU", "B": "XB", "L": "XL"}
# how strongly each region draws settlement (the chance a well-watered square of good soil is settled), and the
# least distance between two places (squares of 3.5 km)
REGION_PULL = {"valley": 1.6, "west": 1.0, "hills": .45, "wheat": .09, "pastoral": .03, "forest": .05, "lee": .9,
               "windward": .5}
MIN_GAP = {"valley": 1.4, "west": 1.4, "hills": 1.9, "wheat": 2.8, "pastoral": 4.3, "forest": 3.0, "lee": 1.4,
           "windward": 2.0}
FARMING = {"valley": "valley", "west": "mixed", "hills": "dryland", "wheat": "wheat-sheep", "pastoral": "pastoral",
           "forest": "forestry", "lee": "cotton", "windward": "gardens"}
# the population (owner, 2026-11-18): per country the total, the rural population outside the towns of the map
# (villages, hamlets and the dispersed farms and homesteads, which are too small to draw and have no dot), the part
# of it living dispersed, and the number of places to draw. The towns of the map ("towns", "localities") and the
# country towns and small towns below (PEOPLE) come on top of the rural population.
POPULATION = {
    "XU": {"total": 1_200_000, "rural": 450_000, "dispersed": 160_000, "places": 430},
    "XB": {"total": 800_000, "rural": 210_000, "dispersed": 80_000, "places": 160},
    "XL": {"total": 60_000, "rural": 30_000, "dispersed": 8_000, "places": 17},
}
# the population bands (people): the band's range and its name
BANDS = [("hamlet", 0, 200), ("village", 200, 1000), ("large village", 1000, 3000), ("small town", 3000, 10000),
         ("country town", 10000, 50000)]
DENSITY = {"hamlet": 1200, "village": 1500, "large village": 1800, "small town": 2000, "country town": 2000}   # people a km2 built up
# the country towns of Urvania (10,000 to 30,000 people, about 150,000 together) and the railway and coast towns of
# Bayvarra (3,000 to 15,000, about 70,000): their people (the other named places get theirs from their site)
PEOPLE = {(68, 116): 28000, (87, 110): 26000, (92, 146): 25000, (29, 106): 22000, (61, 46): 20000, (74, 105): 15000,
          (94, 121): 14000,
          (108, 120): 12000, (139, 116): 9000, (130, 117): 8000, (145, 107): 7000, (152, 89): 6000, (103, 51): 6000,
          (115, 85): 6000, (85, 44): 6000, (96, 105): 5000, (148, 98): 5000}
# what the country towns and the railway and coast towns live on (their size outgrew the village's living)
TOWN_LIVES = {
    (68, 116): "The market of the upper valley and its wine, food works, workshops; commuters to Ferrano.",
    (87, 110): "The cattle fair and the meat works, the market of the plateau's farms, schools and the hospital of the hills.",
    (92, 146): "The south coast's fishing harbour and cannery, its market, summer visitors.",
    (29, 106): "The market and services of the wet west, dairy works, a small harbour at the river mouth.",
    (61, 46): "The north-west's harbour: fishing, fish processing, the coastal shipping, the market of the inlet's farms.",
    (74, 105): "Brick works and workshops by the railway, the valley's farms; commuters to Ferrano.",
    (94, 121): "The border crossing: customs agents, hauliers and warehouses, the railway, the valley's farms.",
    (108, 120): "The stock sales and the railway, the market of the wheat and sheep land, the border crossing.",
    (139, 116): "Oysters and fishing, market gardens for Lumeport, and its commuters.",
    (130, 117): "Its station and the road, the farms round it, joinery for Marrowdale's furniture trade.",
    (145, 107): "The coast road's trade, the farms and sheep runs behind it.",
    (152, 89): "Shearing sheds and wool stores by the station, sheep runs.",
    (103, 51): "The north coast's small harbour, fishing, salt-meadow lamb, the market of the coast's farms.",
    (115, 85): "The market of the plateau's sheep runs and wheat farms.",
    (85, 44): "The market of the north coast's barley and sheep farms.",
    (96, 105): "The market of the western wheat land.",
    (148, 98): "The station's stock yards and grain store, the sheep and cattle runs.",
}
# the growth of the country towns: districts as the towns' (map "towns", "districts"): name, period, years,
# character, offset from the centre (squares), relative size (km), note
GROWTH = {
    (68, 116): [("Borgo del Porto", "urvanian", "before 1600", "core", (0, 0), .9, "The Urvanian carters' and boatmen's village at the head of the rapids, round the landing."),
                ("Via Nuova", "italian", "1850s to 1930s", "residential", (.45, -.35), .9, "The Italian street to Ferrano along the portage road, with the church and the school."),
                ("Quartiere della Diga", "independence", "after 1962", "suburb", (-.4, .4), 1.1, "Housing and workshops by the weir built across the tributary after independence.")],
    (87, 110): [("La Fiera", "urvanian", "before 1600", "core", (0, 0), .9, "The old fair ground at the confluence and the lanes round it."),
                ("Borgo Stazione", "italian", "1880s to 1930s", "residential", (-.45, .3), .9, "The Italian quarter towards Ferrano: the cattle market's offices and the inns."),
                ("Fieravecchia Nuova", "independence", "after 1962", "suburb", (.45, -.4), 1.2, "Housing and the meat works on the terrace above the confluence.")],
    (92, 146): [("Marina", "urvanian", "before 1600", "port", (0, 0), .9, "The fishermen's quarter round the old landing in the bay."),
                ("Il Faro", "italian", "1890s to 1930s", "administration", (.4, .3), .8, "The Italian harbour works: the light, the jetty, the customs house and the promenade."),
                ("Lanternino Alta", "independence", "after 1962", "suburb", (-.35, -.45), 1.2, "Housing on the slope above the bay and the fish cannery.")],
    (29, 106): [("Ponte Vecchio", "urvanian", "before 1600", "core", (0, 0), .9, "The old town at the bridge where the two rivers meet."),
                ("Corso Sardo", "italian", "1840s to 1900", "administration", (.4, -.3), .9, "The Sardinian and Italian main street with the court and the barracks."),
                ("Duefiumi Mare", "independence", "after 1962", "suburb", (-.45, .35), 1.1, "Housing and the dairy works down the valley towards the coast.")],
    (61, 46): [("Il Molo", "urvanian", "before 1600", "port", (0, 0), .9, "The fishermen's town round the harbour at the head of the inlet."),
               ("Riparo Italiano", "italian", "1860s to 1930s", "administration", (.4, .35), .8, "The Italian naval station's quarter: quays, stores and the harbour office."),
               ("Riparo Alto", "independence", "after 1962", "suburb", (-.4, .4), 1.1, "Housing on the hill above the harbour, the fish processing.")],
    (74, 105): [("Pietramiglia Vecchia", "urvanian", "before 1600", "core", (0, 0), .8, "The Urvanian village on the valley road."),
                ("La Stazione", "italian", "1880s to 1930s", "industry", (.4, .3), .8, "The station, the carters' yards and the brick works by the railway."),
                ("Pietramiglia Nuova", "independence", "after 1962", "suburb", (-.35, -.4), 1.1, "Houses for Ferrano's commuters along the valley road.")],
    (94, 121): [("Il Forte", "italian", "about 1842", "core", (0, 0), .8, "The Sardinian fort in the angle of the two rivers and the garrison village round it."),
                ("Borgo della Dogana", "italian", "1857 to 1941", "administration", (-.4, -.3), .8, "The customs house and the traders' street that grew after the boundary convention."),
                ("Forte Nuovo", "independence", "after 1962", "industry", (-.45, .1), 1.1, "Warehouses, the hauliers and housing of the Accord's border trade.")],
}

# The named villages: square -> name (English; the Italian name in Urvania), the word(s) of its name in Urvanian
# or Lisavan (made by tools/lexicon.py; the name is the word, capitalised), founded, why, lives on, a size (no longer
# used: the people come from POPULATION and PEOPLE above), farming.
# Names checked against GeoNames (Italy, the UK, Ireland, the US, Canada, Australia, New Zealand, South Africa,
# and every place of 500 people or more): none is a real place.
NAMED = {
    # ---- Urvania: the valley
    (68, 116): ("Portaggio", "portage", "Urvanian, before 1600",
                "At the head of the rapids above Ruldraz (Ferrano), where a large tributary joins the river: boats "
                "coming down from the upper valley were unloaded here and their loads carried round the rapids.",
                "Once the portage and its carters; now fields and market gardens on the valley floor, vines on the "
                "slope that faces the sun, and Ferrano's market.", "town", "valley"),
    (62, 109): ("San Ranieri del Guado", "ford", "Tuscan, about 1611 (the friars' chapel); the Urvanian hamlet older",
                "At an old ford of the upper river, a day's walk above the rapids: friars of the Tuscan voyage of "
                "1609-10 built a chapel to Pisa's saint beside the Urvanian hamlet at the ford; the chapel outlasted "
                "the trading post.", "Fields on the valley floor, vineyards and orchards, a little pilgrimage to the "
                "chapel.", "large", "valley"),
    (59, 106): ("Gradinella", "terrace", "Urvanian, before 1600",
                "On a terrace of the upper valley above the river's floodplain, at the foot of the slope, where "
                "springs rise.", "Vineyards and orchards on terraced slopes, fields below.", "large", "valley"),
    (74, 105): ("Pietramiglia", "milestone", "Urvanian, before 1600; named under Italian rule",
                "On the valley road from Ruldraz up to the hills of Serravona, beside the railway, at a "
                "stone the Sardinian road builders set at the tenth mile.",
                "Fields and orchards, a carters' inn, and the commuters to Ferrano.", "town", "valley"),
    (80, 111): ("Pomarella", "orchard", "Urvanian, before 1600",
                "On the gentle slope above Ferrano's northern edge, on the road and the railway north, on "
                "well-drained ground facing the sun.", "Orchards and market gardens for Ferrano's markets.",
                "town", "valley"),
    (78, 125): ("Grancelle", "granary", "Urvanian, before 1600",
                "At the end of Ferrano's farm road south across the river bridge, where the grain of the southern "
                "hills was stored before it went down to the town.", "Wheat and barley, the granaries, and Ferrano's "
                "commuters.", "town", "dryland"),
    (83, 113): ("Conciaro", "tannery", "Urvanian, before 1600",
                "On a stream east of Ferrano, on the main road to the border: the hides of the cattle markets were "
                "tanned here, downwind of the town.", "Farming, a leather works that grew from the tanneries.",
                "large", "dryland"),
    (87, 110): ("Fieravecchia", "market", "Urvanian, before 1600",
                "Where two large rivers of the plateau meet north-east of Ferrano, on the drovers' way down from "
                "the hills: the old cattle fair of the region.", "The yearly fair, cattle and sheep, wheat on the "
                "terraces.", "town", "dryland"),
    (85, 102): ("Salicora", "willow", "Urvanian, before 1600",
                "On the floodplain where two streams meet, among willows (cut for baskets and hurdles).",
                "Wheat, willow-growing and baskets, sheep on the hills.", "large", "dryland"),
    (88, 100): ("Fontebrina", "spring", "Urvanian, before 1600",
                "At the foot of the hills where springs rise along a line of harder rock, beside a confluence.",
                "Wheat and sheep, the springs bottled since the Italian period.", "large", "dryland"),
    (94, 121): ("Forte Carlo Alberto", "stronghold", "Sardinian, about 1842 (the fort); the village after it",
                "On the north bank in the angle between the main river and the largest plateau river, just above "
                "their confluence, where the land border meets the river: the Sardinian protectorate built a fort "
                "here to watch the river and the British settlers beyond the plateau river; the boundary convention "
                "of about 1857 made that river and the watershed the border.",
                "The border crossing's traffic, the railway, fields on the valley floor.", "town", "valley"),
    (114, 124): ("Vignalunga", "vineyard", "Urvanian, before 1600",
                 "On the south bank of the lower valley, below a long slope that faces north, to the sun.",
                 "Vineyards along the slope, fields on the floodplain.", "large", "valley"),
    (140, 136): ("Passobarca", "ferry", "Sardinian, about 1845",
                 "On the south shore of the estuary opposite Lumeport, where the ferry lands.",
                 "The ferry to Lumeport, fishing, market gardens for the capital across the water.", "large",
                 "fishing"),
    # ---- Urvania: the wet west and the hills
    (54, 89): ("Fucinalta", "smithy", "Urvanian, before 1600",
               "Just below Serravona on the road up from the valley, where iron ore came out of the "
               "hillsides and charcoal from the woods: the Urvanians' smithies (the iron that named Ferrano).",
               "Mixed farming, chestnut woods, a forge that still makes tools.", "large", "mixed"),
    (29, 68): ("Faggiorna", "beech", "Urvanian, before 1600",
               "High on the wet western hills, on a shelf below the beech woods where two streams meet.",
               "Dairy cattle and hay meadows, beech wood and charcoal.", "village", "mixed"),
    (29, 106): ("Duefiumi", "confluence", "Urvanian, before 1600",
                "Where two rivers of the western hills meet, a few kilometres from the coast.",
                "Mixed farming: small fields, meadows and dairy cattle, chestnut woods.", "town", "mixed"),
    (28, 118): ("Ontanella", "alder", "Urvanian, before 1600",
                "On a confluence in the western hills, among alder woods along the streams.",
                "Mixed farming, alder and chestnut wood.", "large", "mixed"),
    (60, 125): ("Castagnoro", "chestnut", "Urvanian, before 1600",
                "At a confluence in the hills south-west of Ferrano, among chestnut woods.",
                "Chestnuts, small fields and meadows, pigs.", "large", "mixed"),
    (65, 52): ("Mandria Nova", "cattle", "Italian, 1880s",
               "On the plain of a large river near the north coast, where an Italian land company settled farmers "
               "from the valley on a cattle estate.", "Cattle and hay meadows, wheat.", "large", "dryland"),
    (61, 46): ("Porto Riparo", "haven", "Urvanian, before 1600",
               "At the head of a long inlet on the north-west coast, the most sheltered anchorage of Urvania's "
               "coast, where a river comes in.", "Fishing, the small harbour, mixed farming behind it.", "large",
               "mixed"),
    # ---- Urvania: the south coast
    (92, 146): ("Lanternino", "jetty", "Urvanian, before 1600; the harbour light Italian, 1890s",
                "In a sheltered bay of the south coast, where the Italian administration put a harbour light and a "
                "jetty.", "Fishing, small fields and meadows.", "large", "fishing"),
    (118, 153): ("Saline Brune", "saltpan", "Urvanian, before 1600",
                 "On a flat stretch of the south coast where a stream comes down to a lagoon: salt pans.",
                 "Salt, fishing, wheat and vines behind the shore.", "large", "fishing"),
    (124, 153): ("Piccionara", "dovecote", "Urvanian, before 1600",
                 "At a stream mouth on the south coast, its farms known for their dovecotes.",
                 "Wheat, vines and olives, pigeons, fishing.", "village", "dryland"),
    (132, 151): ("Marina Ligure", "cove", "Sardinian, 1840s",
                 "In a cove of the south coast where a stream comes down: Ligurian fishermen from the Sardinian "
                 "kingdom's colony on the Plata settled here under the protectorate.",
                 "Fishing, boatbuilding, gardens behind the shore.", "large", "fishing"),
    # ---- Bayvarra
    (108, 120): ("Tallowford", None, "British settlers, 1840s",
                 "At the ford of the main river where the largest plateau river joins it, the drovers' crossing "
                 "between the plateau and the south; the railway and the border crossing came later.",
                 "Stock sales, the railway, wheat and sheep.", "town", "wheat-sheep"),
    (130, 117): ("Brackenmere", None, "British settlers, 1840s",
                 "Between Marrowdale and Lumeport on the road and the railway, by a spring-fed pond (the mere) in "
                 "bracken-covered ground: a stage on the road down to the capital.",
                 "Sheep and wheat, the road; its joiners went to Marrowdale's furniture trade.", "large",
                 "wheat-sheep"),
    (145, 107): ("Stockmans Rest", None, "British settlers, 1830s",
                 "On the coast road from Larkmouth to Lumeport, where it crosses a stream at a confluence: an inn "
                 "where drovers rested their stock.", "The road, sheep and cattle runs.", "large", "pastoral"),
    (152, 89): ("Fleecewell", None, "British settlers, 1830s; the station 19th century",
                "Just south of Larkmouth on the coast road and the wool line, at a well where the flocks were "
                "watered and washed before shearing.", "Shearing sheds and wool, the station, sheep runs.",
                "large", "pastoral"),
    (148, 98): ("Hartsedge", None, "British, 19th century (the station)",
                "At a station on the wool line between Marrowdale and Larkmouth, on the edge of a rise.",
                "The station's stock yards, sheep and cattle runs.", "village", "pastoral"),
    (137, 72): ("Ewesbridge", None, "British settlers, 1830s",
                "On the road north from Larkmouth over the dry east, at a bridge over a creek.",
                "A sheep station's village: wool, the road.", "village", "pastoral"),
    (115, 85): ("Wethercote", None, "British settlers, 1840s",
                "Where two rivers of the plateau meet, the homestead of one of the first sheep runs.",
                "Sheep (wethers, for wool), hay.", "large", "pastoral"),
    (96, 105): ("Harrowmead", None, "British settlers, 1850s",
                "On the plateau near the border, on a confluence in the wetter western part of Bayvarra.",
                "Wheat and sheep.", "large", "wheat-sheep"),
    (139, 116): ("Wadebank", None, "British settlers, 1840s",
                 "On the north shore of Lumeport's bay, on the road north, where the shore shelves gently.",
                 "Oysters and fishing, market gardens for Lumeport.", "large", "fishing"),
    (161, 102): ("Ternhaven", None, "British settlers, 1830s",
                 "At a creek mouth on the east coast, behind a spit where terns nest.",
                 "Fishing, sheep on the runs behind.", "village", "fishing"),
    (103, 51): ("Saltmere", None, "British settlers, 1830s",
                "On a sheltered creek of the north coast among salt meadows, where a river comes in, on the road "
                "along the coast.", "Fishing, salt-meadow lamb, a small harbour.", "large", "fishing"),
    (92, 47): ("Shinglebeck", None, "British settlers, 1830s",
               "Where a stream comes down to a shingle shore of the north coast, on the coast road.",
               "Sheep and fishing.", "village", "pastoral"),
    (124, 53): ("Ploverness", None, "British settlers, 1840s",
                "On a low point of the north coast at a stream mouth.", "Fishing and sheep.", "village", "fishing"),
    (85, 44): ("Barleycombe", None, "British settlers, 1840s",
               "In a valley near the north coast, on the road, where the rain is enough for barley.",
               "Barley and sheep.", "large", "wheat-sheep"),
    # ---- Lisavu
    (227, 122): ("Linukaha", "rivermouth", "Lisavan, old",
                 "At the mouth of the largest stream of the south coast, where two streams meet.",
                 "Fishing, gardens and cotton on the coastal flat.", "town", "cotton"),
    (230, 106): ("Natahoma", "anchorage", "Lisavan, old",
                 "In the most sheltered bay of the north coast, where a stream comes in.",
                 "Fishing and canoe building, gardens.", "large", "fishing"),
    (234, 106): ("Lintwell", "cottonfield", "English settlers, 19th century (a cotton estate)",
                 "On the dry north-eastern plain on the road north of the town, at a well dug for an English "
                 "settler's cotton estate.", "Cotton.", "large", "cotton"),
    (239, 105): ("Bollworth", "landing", "English settlers, 19th century",
                 "On the coast of the cotton plain north of Selanu, where the estates landed their bales for the "
                 "ships.", "Cotton, fishing.", "village", "cotton"),
    (220, 101): ("Setahu", "headland", "Lisavan, old",
                 "On the north coast west of the cotton plain, under a headland that keeps off the westerly swell: "
                 "the last landing before the cliffs of the windward side.",
                 "Fishing, gardens below the forest.", "village", "gardens"),
    (218, 123): ("Nihekemo", "waterfall", "Lisavan, old",
                 "On the south-west coast where a stream falls from the cliffs to the shore.",
                 "Gardens and fishing.", "village", "gardens"),
    (211, 106): ("Felulaka", "landslide", "Lisavan, old",
                 "On a flat of old landslide debris at the foot of the west cliffs (a faja), reached by a "
                 "track down the cliff.", "Gardens, fruit and fishing.", "village", "gardens"),
}
ENGLISH_ON_LISAVU = {(234, 106), (239, 105)}         # settlers' names: English first, the Lisavan name beside it


def load_fields():
    here = os.path.join(ROOT, "tools")
    spec = importlib.util.spec_from_file_location("terrain_lib", os.path.join(here, "terrain_lib.py"))
    T = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(T)
    inp = json.load(open(os.path.join(ROOT, "world", "terrain-inputs.json")))
    return {"mainland": T.mainland(inp, lambda s: None), "lisavu": T.lisavu(inp, lambda s: None)}


def features_per_square(terr, fields):
    out = {}
    for name, d in fields.items():
        r = terr["rasters"][name]
        S, x0, y0 = r["cells_per_square"], r["x0"], r["y0"]
        cov = np.array(Image.open(os.path.join(ROOT, r["cover"])))
        z, rain, sea = d["z"], d["rain"], d["sea"]
        gy, gx = np.gradient(z, r["cell_m"])
        sl = np.hypot(gx, gy)
        ny, nx = z.shape
        for a in range(ny // S):
            for b in range(nx // S):
                blk = (slice(a * S, a * S + S), slice(b * S, b * S + S))
                land = ~sea[blk]
                if land.mean() < .5:
                    continue
                c = cov[blk][land]
                out[(x0 + b, y0 + a)] = dict(z=float(z[blk][land].mean()), zr=float(np.ptp(z[blk][land])),
                                             rain=float(rain[blk].mean()), slope=float(sl[blk][land].mean()),
                                             fr={k: float((c == q).mean()) for q, k in enumerate("swdfghrm")})
    for key in ("mainland", "lisavu"):
        for s in terr["streams"][key]:
            for x, y, a in s:
                q = (int(x), int(y))
                if q in out:
                    out[q]["stream"] = max(out[q].get("stream", 0), a)
            x, y, a = s[-1]
            q = (int(x), int(y))
            if q in out:
                out[q]["conf"] = max(out[q].get("conf", 0), a)
    return out


def main():
    fields = load_fields()                  # first: tools/ holds a coverage.py that would shadow numba's import
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import world_data
    import world_model as wm
    terr = json.load(open(os.path.join(ROOT, "world", "terrain.json")))
    mp = json.load(open(world_data.path("map"), encoding="utf-8"))
    world = world_data.load()
    world["villages"] = []
    world["routes"] = [r for r in world["routes"] if not r["id"].startswith("village-")]
    model, problems = wm.build(world)
    T = model["tiles"]
    F = features_per_square(terr, fields)
    river = {(x, y) for x, y, _ in terr["river"]}
    est = {tuple(q) for q in terr["estuary"]}
    pipes = {tuple(q) for r in world["routes"] if r["mode"] == "pipeline" for q in r["pts"]}
    managed = {(i, j) for f in terr["managed_forests"] for i, j, _ in f["squares"]}
    towns = world["towns"] + world["localities"]
    lex = world["languages"]
    # the two main landmasses (the mainland and Lisavu), 4-connected over land and river squares
    seen, comps = set(), []
    for q0 in F:
        if q0 in seen or T[q0[0]][q0[1]]["k"] == "s":
            continue
        comp, st = {q0}, [q0]
        seen.add(q0)
        while st:
            x = st.pop()
            for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                y = (x[0] + a, x[1] + b)
                if y in F and y not in seen and T[y[0]][y[1]]["k"] != "s":
                    seen.add(y)
                    comp.add(y)
                    st.append(y)
        comps.append(comp)
    comps.sort(key=len, reverse=True)
    main_land = comps[0] | comps[1]

    def region(q):
        f, c = F[q], terr["country"][q[1]][q[0]]
        if f["z"] > 850 or f["slope"] > .2 or f["fr"]["m"] > .4:
            return None
        if c == "L":
            return "lee" if f["rain"] < 1150 else "windward"
        if f["fr"]["f"] > .7:
            return "forest"
        if c == "U":
            if f["z"] < 400 and min(math.hypot(q[0] - x, q[1] - y) for x, y in river) <= 3:
                return "valley"
            return "west" if f["rain"] >= 880 else "hills"
        return "wheat" if f["rain"] >= 720 else "pastoral"

    def free(q):
        t = T[q[0]][q[1]]
        if t["k"] in ("s", "w") or any(k in t for k in ("rd", "rl", "b", "az", "br", "ab", "um", "ms", "hb", "hs", "dk")):
            return False
        if q in managed or any((q[0] + a, q[1] + b) in pipes for a in range(-2, 3) for b in range(-2, 3)):
            return False
        for tw in towns:
            if math.hypot(q[0] - tw["c"][0], q[1] - tw["c"][1]) < tw["built_km"] / 7 + (3.2 if tw["built_km"] > 2 else 2):
                return False
        if any(k in T[q[0] + a][q[1] + b] for a in range(-3, 4) for b in range(-3, 4) for k in ("br", "ab", "tn")):
            return False                                 # 3 squares from a bridge or a tunnel: its ground is fitted to it
        if q not in main_land:
            return False                                 # not on an islet: no road could reach it
        if not any(T[q[0] + a][q[1] + b]["k"] not in ("s", "w") and "rl" not in T[q[0] + a][q[1] + b]
                   and (q[0] + a, q[1] + b) not in pipes for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            return False                                 # no side a road could come in by
        return not any(k in T[q[0] + a][q[1] + b] for a in (-1, 0, 1) for b in (-1, 0, 1) for k in ("b", "az", "ab", "br", "hb"))

    def feats(q):
        f, out = F[q], {}
        nb4 = [(q[0] + a, q[1] + b) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))]
        nb8 = [(q[0] + a, q[1] + b) for a in (-1, 0, 1) for b in (-1, 0, 1) if a or b]
        if any(n in river for n in nb8):
            out["river"] = 1
        if f.get("conf", 0) > 300 and f.get("stream", 0) > 600:
            out["confluence"] = 1
        if f.get("stream", 0) > 250:
            out["stream"] = 1
        if any(T[n[0]][n[1]]["k"] == "s" and n not in est for n in nb8):
            ring = [(q[0] + a, q[1] + b) for a in range(-3, 4) for b in range(-3, 4)]
            out["coast"] = sum(1 for n in ring if T[n[0]][n[1]]["k"] == "s") / len(ring)
        if any(n in est for n in nb8):
            out["estuary"] = 1
        if any("rd" in T[n[0]][n[1]] for n in nb4):
            out["road"] = 1
        if any("rl" in T[n[0]][n[1]] for n in nb8):
            out["rail"] = 1
        ring2 = [(q[0] + a, q[1] + b) for a in range(-2, 3) for b in range(-2, 3) if (a or b) and (q[0] + a, q[1] + b) in F]
        if f["slope"] < .06 and ring2 and max(F[n]["z"] for n in ring2) - f["z"] > 120:
            out["foot"] = 1
        if ring2 and sum(F[n]["fr"]["f"] for n in ring2) / len(ring2) > .45:
            out["forest"] = 1
        return out

    def score(q, ft, reg):
        f = F[q]
        s = 1.2 * (f["fr"]["d"] + .6 * f["fr"]["g"]) - 6 * max(0, f["slope"] - .04) - f["zr"] / 400
        s += .9 * ("confluence" in ft) + .7 * ("river" in ft) + .3 * ("stream" in ft) + .4 * ("foot" in ft)
        s += .6 * ("road" in ft) + (1.0 if reg in ("wheat", "pastoral") else .3) * ("rail" in ft)
        if "coast" in ft:
            s += .9 - ft["coast"]
        return s

    def hsh(x, y, salt):
        h = (x * 374761393 + y * 668265263 + salt * 1442695041) & 0xFFFFFFFF
        h = ((h ^ (h >> 13)) * 1274126177) & 0xFFFFFFFF
        return ((h ^ (h >> 16)) & 0xFFFFFFFF) / 4294967295

    def pull(q, ft, reg):
        """How strongly a square draws settlement: water (the river, a confluence, a sheltered cove, a spring line,
        a stream), soil (level open land), the routes, the region's way of life."""
        f = F[q]
        water = .08
        for k, w in (("river", 1.0), ("confluence", 1.0), ("estuary", .8), ("foot", .55), ("stream", .45)):
            if k in ft:
                water = max(water, w)
        if "coast" in ft:
            water = max(water, .9 if ft["coast"] < .4 else .4)
        soil = (f["fr"]["d"] + .5 * f["fr"]["g"]) * max(0., 1 - f["slope"] / .15)
        route = .6 * ("road" in ft) + .5 * ("rail" in ft)
        return REGION_PULL[reg] * water * (.2 + soil) * (1 + route)

    acc = []
    for q in NAMED:
        if q not in F or not free(q) or not region(q):
            sys.exit(f"named village at {q}: the square is not free or not habitable")
        acc.append((99.0, q, region(q), feats(q)))
    # 1. the railway stations of Bayvarra's lines: about every 20 km along the line where it crosses the open land
    #    (a station village beside the line; the named places on the line count as stations)
    taken = {a[1] for a in acc}
    stations = []
    rails = [r for r in world["routes"] if r["mode"] == "rail"]
    for r in rails:
        run = 0.0
        path = [tuple(q) for q in r["pts"]]
        for k in range(1, len(path)):
            run += math.dist(path[k - 1], path[k])
            q = path[k]
            if terr["country"][q[1]][q[0]] != "B":
                continue
            if any(math.dist(q, t) < 3 for t in taken | set(stations)) or any(
                    math.dist(q, tw["c"]) < tw["built_km"] / 7 + 3 for tw in towns):
                run = min(run, 0.0) if any(math.dist(q, t) < 2 for t in taken) else run
                continue
            if run < 5.5:
                continue
            side = [(q[0] + a, q[1] + b) for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))]
            side = [y for y in side if y in F and free(y) and region(y)]
            if side:
                y = max(side, key=lambda y: (F[y]["fr"]["d"] + F[y]["fr"]["g"] - F[y]["slope"], y))
                stations.append(y)
                acc.append((50.0, y, region(y), dict(feats(y), station=r["id"])))
                run = 0.0
    # 2. the villages and hamlets: each square draws settlement by its site (pull); a square is settled with that
    #    chance (a hash of the square, so the pattern is fixed), the strongest first, and two places keep at least
    #    their region's distance (a square apart in the farmland, 15 km between the stations of the dry east). The
    #    chance is high along the rivers, the valley floors, the spring lines, the coves and the old roads, low on
    #    dry or steep land: strings of villages along the valleys, close pairs, isolated hamlets, empty country.
    #    The chance is scaled per country (SCALE, found by bisection) so that each country gets its number of places
    #    (POPULATION "places").
    base = list(acc)
    pool = []
    for q in F:
        if q in NAMED or q in stations or not free(q):
            continue
        reg = region(q)
        if not reg:
            continue
        ft = feats(q)
        pool.append((pull(q, ft, reg), q, reg, ft, CTY[terr["country"][q[1]][q[0]]]))

    def place(SCALE):
        cands = [(lam * SCALE[c] * (.6 + .8 * hsh(q[0], q[1], 8)), q, reg, ft) for lam, q, reg, ft, c in pool
                 if hsh(q[0], q[1], 7) < min(.95, lam * SCALE[c])]
        cands.sort(key=lambda c: (-c[0], c[1]))
        got = list(base)
        for c in cands:
            if all(math.dist(c[1], a[1]) >= max(MIN_GAP[c[2]], MIN_GAP[a[2]]) for a in got):
                got.append(c)
        return got

    SCALE = {"XU": 1.0, "XB": 1.0, "XL": 1.0}
    count = lambda got, c: sum(1 for a in got if CTY[terr["country"][a[1][1]][a[1][0]]] == c)
    for c in ("XU", "XB", "XL"):
        lo, hi = -4.0, 4.0                                # log2 of the scale
        for _ in range(16):
            SCALE[c] = 2 ** ((lo + hi) / 2)
            if count(place(SCALE), c) < POPULATION[c]["places"]:
                lo = (lo + hi) / 2
            else:
                hi = (lo + hi) / 2
        SCALE[c] = 2 ** hi
    acc = place(SCALE)
    print("scale of the chance per country:", {c: round(v, 3) for c, v in SCALE.items()},
          {c: count(acc, c) for c in SCALE})
    # 3. the people: the fixed towns (PEOPLE); the rest of each country's rural population living in places (not
    #    dispersed, not in the localities) shared out by the strength of the site, a named place's three times, with
    #    a fixed noise; a named place has at least 1,000, no village more than 4,500
    people = {}
    for c in ("XU", "XB", "XL"):
        mine = [(s_, q, reg, ft) for s_, q, reg, ft in acc if CTY[terr["country"][q[1]][q[0]]] == c and q not in PEOPLE]
        local = sum(2000 for t in world["localities"] if t["country"] == c)
        share = POPULATION[c]["rural"] - POPULATION[c]["dispersed"] - local
        wt = {q: (pull(q, ft, reg) + .05) ** 1.2 * (.15 + 1.7 * hsh(q[0], q[1], 9) ** 2) * (3 if q in NAMED else 1.5 if "station" in ft else 1)
              for s_, q, reg, ft in mine}
        fixed = {}
        for _ in range(20):
            k = (share - sum(fixed.values())) / sum(w for q, w in wt.items() if q not in fixed)
            low = {q for q in wt if q in NAMED and q not in fixed and wt[q] * k < 1000}
            high = {q for q in wt if q not in fixed and wt[q] * k > 4500}
            if not low and not high:
                break
            fixed.update({q: 1000 for q in low})
            fixed.update({q: 4500 for q in high})
        for q, w in wt.items():
            people[q] = fixed.get(q) or max(30, int(round(w * k / 10) * 10))
    people.update(PEOPLE)
    out = []
    for s, q, reg, ft in acc:
        c = CTY[terr["country"][q[1]][q[0]]]
        if q in NAMED:
            name, word, founded, why, lives, band, farming = NAMED[q]
            v = {"name": name}
            if c == "XU":
                v["names"] = {"en": name, "qau": lex["qau"]["lexicon"][word].capitalize()}
                v["name_from"] = {"qau": word}
            elif c == "XL":
                own = lex["qal"]["lexicon"][word].capitalize()
                if q in ENGLISH_ON_LISAVU:
                    v["names"] = {"en": name, "qal": own}
                else:
                    v["name"] = own
                    v["names"] = {"qal": own}
                v["name_from"] = {"qal": word}
            else:
                v["names"] = {"en": name}
        else:
            farming = "fishing" if "coast" in ft and ft["coast"] < .5 and reg not in ("lee",) else FARMING[reg]
            founded, why, lives = story(c, reg, ft, F[q])
            v = {"name": None}
        n = people[q]
        lives = TOWN_LIVES.get(q, lives)
        band, lo, hi = next(b for b in BANDS if b[1] <= n < b[2])
        v.update({"c": list(q), "country": c, "region": reg, "founded": founded, "why": why, "lives_on": lives,
                  "people": n, "population": [lo, hi], "band": band,
                  "built_km": round(max(.45, 2 * math.sqrt(n / DENSITY[band] / math.pi)), 2), "farming": farming})
        if q in GROWTH:
            v["districts"] = [{"name": dn, "period": pe, "years": ye, "character": ch,
                               "at": [round(q[0] + o[0], 2), round(q[1] + o[1], 2)], "r_km": rk, "note": no}
                              for dn, pe, ye, ch, o, rk, no in GROWTH[q]]
        out.append(v)
    out.sort(key=lambda v: (v["name"] is None, v["country"], v["c"]))
    mp["villages"] = out
    world_data.save("map", mp)
    # the population per country, with its parts, into world/countries.json
    cj = json.load(open(world_data.path("countries"), encoding="utf-8"))
    for c, P in POPULATION.items():
        towns_ = sum(t["population"] for t in world["towns"] if t["country"] == c)
        loc = sum(2000 for t in world["localities"] if t["country"] == c)
        mine = [v for v in out if v["country"] == c]
        ct = sum(v["people"] for v in mine if tuple(v["c"]) in PEOPLE)
        vil = sum(v["people"] for v in mine if tuple(v["c"]) not in PEOPLE) + loc
        cj["countries"][c]["population"] = {
            "total": towns_ + ct + vil + P["dispersed"], "towns": towns_, "country_towns": ct, "villages": vil,
            "largest_village": max(v["people"] for v in mine if tuple(v["c"]) not in PEOPLE),
            "dispersed": P["dispersed"], "places_drawn": len(mine),
            "note": "The population (owner, 2026-11-18): the towns of the map (towns), the country towns of Urvania and "
                    "the railway and coast towns of Bayvarra (country_towns), the villages and hamlets (world/map.json \"villages\" and \"localities\", each with its people) and the "
                    "dispersed farms and homesteads, too small to draw. Made by analysis/world-position/site_villages.py."}
        print(c, cj["countries"][c]["population"])
    world_data.save("countries", cj)
    from collections import Counter
    print(len(out), "villages:", dict(Counter((v["country"], v["name"] is not None) for v in out)))


def story(c, reg, ft, f):
    """The reason, the living and the founding of an unnamed village, read from its site."""
    if "station" in ft:
        why = "At a station on the railway, where the line crosses the open land: stock yards and a store."
    elif "estuary" in ft:
        why = "On the estuary shore, at a landing for boats."
    elif "coast" in ft:
        why = "In a sheltered cove of the coast." if ft["coast"] < .4 else "On the open coast, above a landing beach."
    elif "confluence" in ft:
        why = "Where two streams meet, on dry ground above their floodplain."
    elif "river" in ft:
        why = "On the valley floor beside the river, above the floods."
    elif "rail" in ft and c == "XB":
        why = "At a station on the railway."
    elif "road" in ft:
        why = "On the road, at a crossing of ways."
    elif "foot" in ft:
        why = "At the foot of the hills, where springs rise."
    elif "stream" in ft:
        why = "On a stream, in the floor of its valley."
    elif "forest" in ft or reg == "forest":
        why = "In a clearing at the edge of the forest."
    else:
        why = "On level ground among its fields, with a well."
    lives = {"valley": "Fields on the valley floor, vineyards and orchards on the slopes that face the sun.",
             "west": "Mixed farming: small fields, hay meadows and dairy cattle, orchards, chestnut woods.",
             "hills": "Wheat and barley, olives and vines on the sunny slopes, sheep.",
             "wheat": "Wheat and sheep.", "pastoral": "A sheep and cattle station: wool and meat from big paddocks.",
             "forest": "Timber and charcoal, gardens in the clearing.", "lee": "Cotton, gardens and pasture.",
             "windward": "Fruit and vegetable gardens, the forest."}[reg]
    if "coast" in ft or "estuary" in ft:
        lives = "Fishing; " + lives[0].lower() + lives[1:]
    if c == "XU":
        founded = "Urvanian, before 1600" if reg in ("valley", "west") or f["rain"] >= 800 or "coast" in ft else \
            "Urvanian, 17th to 18th century, from the valley"
        if reg == "forest":
            founded = "Italian, about 1900 (a forest village)"
    elif c == "XB":
        founded = "British settlers, 1830s to 1860s"
        if "station" in ft or ("rail" in ft and reg in ("wheat", "pastoral")):
            founded = "British, late 19th century, at the railway's station"
        if reg == "forest":
            founded = "British, about 1900 (a forest village)"
    else:
        founded = "Lisavan, old"
    return founded, why, lives


if __name__ == "__main__":
    main()
