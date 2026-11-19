# The place list (O91)

Made by `python3 tools/place_list.py` from the world data (`world/map.json`, `world/parties.json`, `world/terrain.json`, `world/countries.json`, `world/documents.json`); do not edit it by hand. `python3 tools/place_list.py --check` (run by `tools/check_world.py`) says whether it is current.

It replaces the place list of 2026-11-18 written for the 14 km grid and D19's positions. The rules it follows:

- **The map is leading** (owner, 2026-11-18, O152): a distance is the length of the route on the map, square by square (3.5 km a side, 4.95 km a diagonal), as `tools/lay_routes.py --report` measures it.
- **Positions** are WGS 84 as the documents state them (`coordinate()` in `tools/build_examples.py`): 3.5 km squares on both axes around the mainland's centre (30.0° S, 15.0° W at square 91.5/94) and, for Lisavu, drawn nearer as an inset, around its own centre (33.0° S, 2.65° W at square 225/112); a degree of latitude is 111.0 km, of longitude 111.32 km × cos(latitude of the area's centre). The minutes are those the documents print.
- **Straight lines** on land are measured on the map (squares × 3.5 km); between the mainland and Lisavu they are great-circle distances between the stated positions, since the inset is not at its true distance.
- **Heights** are the natural ground of the square (`world/terrain.json`, the mean of its four corners, metres above the sea); the 3D map fits what is built to the land, a built square's corners within 80 m of each other and quays at the water, so it may show a town lower (section 6).
- **The map is a diagram inside the towns** (O82): a party takes a whole 3.5 km square, so the parties of a town spread over two to five times its built-up width (O92, open). Distances inside and around a town are therefore longer on the map than on the ground; section 3 flags them.

## 1. Places

Every town, the 4 localities of parties (villages and the two sides of the road border crossing), and every named village of the map (54 places). Names in brackets are the place's name in the national language. Population: the decided figure, or the band for a locality.

| Place | Kind | Country, state | Square | Position (WGS 84) | Height | People | Why it is there |
|---|---|---|---|---|---|---|---|
| **Ferrano** | capital | XU, Province of Ferrano | 77/116 | 30.6937 S 15.5264 W (30° 41.62′ S, 15° 31.59′ W) | 195 m | 600,000 | The Urvanian town on the terrace of the north bank where the northern valley meets the river below the rapids: its lanes, the market and the old bridgehead. |
| **Serravona** | village (locality) | XU, Province of Ferrano | 56/87 | 29.7793 S 16.2888 W (29° 46.76′ S, 16° 17.33′ W) | 458 m | 1,000–3,000 | The mining village at the ore mine. |
| **Valico Euridice (Menbaz)** | village (locality) | XU, Province of Ferrano | 96/120 | 30.8198 S 14.8366 W (30° 49.19′ S, 14° 50.20′ W) | 153 m | 100–500 | The Urvanian side of the road border crossing, named after Forte Euridice, the town 8 km down the road. |
| **Duefiumi (Krakgaz)** | country town | XU, Province of Ferrano | 29/106 | 30.3784 S 17.2691 W (30° 22.70′ S, 17° 16.14′ W) | 302 m | 22,000 | Where two rivers of the western hills meet, a few kilometres from the coast. |
| **Fierabruna (Hihek)** | country town | XU, Province of Ferrano | 87/110 | 30.5045 S 15.1634 W (30° 30.27′ S, 15° 09.80′ W) | 272 m | 26,000 | Where two large rivers of the plateau meet north-east of Ferrano, on the drovers' way down from the hills: the old cattle fair of the region. |
| **Forte Euridice (Girkul)** | country town | XU, Province of Ferrano | 94/121 | 30.8514 S 14.9092 W (30° 51.08′ S, 14° 54.55′ W) | 145 m | 14,000 | On the north bank in the angle between the main river and the largest plateau river, just above their confluence, where the land border meets the river. |
| **Lanternino (Bikran)** | country town | XU, Province of Ferrano | 92/146 | 31.6396 S 14.9818 W (31° 38.38′ S, 14° 58.91′ W) | 28 m | 25,000 | In a sheltered bay of the south coast, where the Italian administration put a harbour light and a jetty. |
| **Pietramiglia (Rekhir)** | country town | XU, Province of Ferrano | 74/105 | 30.3468 S 15.6353 W (30° 20.81′ S, 15° 38.12′ W) | 322 m | 15,000 | On the valley road from Ruldraz up to the hills of Serravona, beside the railway, at a stone the Sardinian road builders set at the tenth mile. |
| **Portaggio (Trenzir)** | country town | XU, Province of Ferrano | 68/116 | 30.6937 S 15.8532 W (30° 41.62′ S, 15° 51.19′ W) | 209 m | 28,000 | At the head of the rapids above Ruldraz (Ferrano), where a large tributary joins the river. |
| **Porto Riparo (Metir)** | country town | XU, Province of Ferrano | 61/46 | 28.4865 S 16.1073 W (28° 29.19′ S, 16° 06.44′ W) | 58 m | 20,000 | At the head of a long inlet on the north-west coast, the most sheltered anchorage of Urvania's coast, where a river comes in. |
| **Castagnoro (Kritran)** | small town | XU, Province of Ferrano | 60/125 | 30.9775 S 16.1436 W (30° 58.65′ S, 16° 08.62′ W) | 291 m | 4,500 | At a confluence in the hills south-west of Ferrano, among chestnut woods. |
| **Faggiorna (Vidraz)** | small town | XU, Province of Ferrano | 29/68 | 29.1802 S 17.2691 W (29° 10.81′ S, 17° 16.14′ W) | 709 m | 3,410 | High on the wet western hills, on a shelf below the beech woods where two streams meet. |
| **Fontebrina (Zhazsan)** | small town | XU, Province of Ferrano | 88/100 | 30.1892 S 15.1271 W (30° 11.35′ S, 15° 07.62′ W) | 338 m | 4,370 | At the foot of the hills where springs rise along a line of harder rock, beside a confluence. |
| **Mandria Nova (Belzhan)** | small town | XU, Province of Ferrano | 65/52 | 28.6757 S 15.9621 W (28° 40.54′ S, 15° 57.72′ W) | 179 m | 4,420 | On the plain of a large river near the north coast, where an Italian land company settled farmers from the valley on a cattle estate. |
| **Salicora (Stagir)** | small town | XU, Province of Ferrano | 85/102 | 30.2523 S 15.2360 W (30° 15.14′ S, 15° 14.16′ W) | 342 m | 4,500 | On the floodplain where two streams meet, among willows (cut for baskets and hurdles). |
| **Saline Brune (Vaknan)** | small town | XU, Province of Ferrano | 118/153 | 31.8604 S 14.0379 W (31° 51.62′ S, 14° 02.28′ W) | 5 m | 4,500 | On a flat stretch of the south coast where a stream comes down to a lagoon: salt pans. |
| **Conciaro (Zhildir)** | large village | XU, Province of Ferrano | 83/113 | 30.5991 S 15.3086 W (30° 35.95′ S, 15° 18.52′ W) | 328 m | 1,000 | On a stream east of Ferrano, on the main road to the border: the hides of the cattle markets were tanned here, downwind of the town. |
| **Gradinella (Skazhaz)** | large village | XU, Province of Ferrano | 59/106 | 30.3784 S 16.1799 W (30° 22.70′ S, 16° 10.79′ W) | 325 m | 2,900 | On a terrace of the upper valley above the river's floodplain, at the foot of the slope, where springs rise. |
| **Grancelle (Triznaz)** | large village | XU, Province of Ferrano | 78/125 | 30.9775 S 15.4901 W (30° 58.65′ S, 15° 29.41′ W) | 332 m | 1,560 | At the end of Ferrano's farm road south across the river bridge, where the grain of the southern hills was stored before it went down to the town. |
| **Marina Ligure (Gizaz)** | large village | XU, Province of Ferrano | 132/151 | 31.7973 S 13.5297 W (31° 47.84′ S, 13° 31.78′ W) | 1 m | 1,730 | In a cove of the south coast where a stream comes down: Ligurian fishermen from the Sardinian kingdom's colony on the Plata settled here under the protectorate. |
| **Ontanella (Skegek)** | large village | XU, Province of Ferrano | 28/118 | 30.7568 S 17.3054 W (30° 45.41′ S, 17° 18.32′ W) | 224 m | 1,750 | On a confluence in the western hills, among alder woods along the streams. |
| **Passobarca (Krezvir)** | large village | XU, Province of Ferrano | 140/136 | 31.3243 S 13.2392 W (31° 19.46′ S, 13° 14.35′ W) | 6 m | 1,000 | On the south shore of the estuary opposite Lumeport, where the ferry lands. |
| **Pomarella (Sizgul)** | large village | XU, Province of Ferrano | 80/111 | 30.5360 S 15.4175 W (30° 32.16′ S, 15° 25.05′ W) | 274 m | 1,650 | On the gentle slope above Ferrano's northern edge, on the road and the railway north, on well-drained ground facing the sun. |
| **San Ranieri del Guado (Malzhan)** | large village | XU, Province of Ferrano | 62/109 | 30.4730 S 16.0710 W (30° 28.38′ S, 16° 04.26′ W) | 261 m | 1,680 | At an old ford of the upper river, a day's walk above the rapids. |
| **Torre Colombina (Gitir)** | large village | XU, Province of Ferrano | 124/153 | 31.8604 S 13.8201 W (31° 51.62′ S, 13° 49.21′ W) | 0 m | 1,000 | At a stream mouth on the south coast, its farms known for their dovecotes. |
| **Vignacorta (Hulbir)** | large village | XU, Province of Ferrano | 114/124 | 30.9459 S 14.1831 W (30° 56.76′ S, 14° 10.99′ W) | 71 m | 1,000 | On the south bank of the lower valley, below a short, steep slope that faces north, to the sun. |
| **Fucinalta (Trazvul)** | village | XU, Province of Ferrano | 54/89 | 29.8423 S 16.3614 W (29° 50.54′ S, 16° 21.69′ W) | 482 m | 900 | Just below Serravona on the road up from the valley, where iron ore came out of the hillsides and charcoal from the woods. |
| **Lumeport** | capital | XB, Coastal State | 138/126 | 31.0090 S 13.3118 W (31° 00.54′ S, 13° 18.71′ W) | 118 m | 400,000 | The settlers' company town of about 1840 by the mouth of the brook (its first fresh water) on the shore of the bay, commanding the narrows. |
| **Larkmouth** | town | XB, Coastal State | 154/85 | 29.7162 S 12.7309 W (29° 42.97′ S, 12° 43.86′ W) | 51 m (3D map 28 m) | 80,000 | Bayvarra's first town and first capital (O153). |
| **Marrowdale** | town | XB, Upland State | 123/112 | 30.5676 S 13.8564 W (30° 34.05′ S, 13° 51.38′ W) | 286 m | 40,000 | An inland town in Upland State, near the border: the distributor with its rail siding, the sawmill, the furniture maker and the engineering works. |
| **Euridice Crossing** | village (locality) | XB, Upland State | 97/120 | 30.8198 S 14.8003 W (30° 49.19′ S, 14° 48.02′ W) | 134 m | 100–500 | The Bayvarran side of the road border crossing, known like the Urvanian side by the fort town across the border, as the crossing has been since the boundary convention. |
| **Gullhaven** | village (locality) | XB, Northern Territory | 73/39 | 28.2658 S 15.6716 W (28° 15.95′ S, 15° 40.30′ W) | 91 m | 1,000–3,000 | A fishing village on Bayvarra's north coast, by the gas plant. |
| **Tallowford** | country town | XB, Upland State | 108/120 | 30.8198 S 14.4010 W (30° 49.19′ S, 14° 24.06′ W) | 80 m | 12,000 | On the north bank of the main river, where the drove road down the valley forded the second plateau river (about 5,500 km²) some 5 km above its mouth, about 40 km downstream of the border crossing and Forte Euridice. |
| **Barleycombe** | small town | XB, Upland State | 103/111 | 30.5360 S 14.5825 W (30° 32.16′ S, 14° 34.95′ W) | 243 m | 6,000 | In a valley of the western wheat land between Marrowdale and the border, where two streams meet. |
| **Brackenmere** | small town | XB, Upland State | 130/117 | 30.7252 S 13.6023 W (30° 43.51′ S, 13° 36.14′ W) | 171 m | 8,000 | Between Marrowdale and Lumeport on the road and the railway, by a spring-fed pond (the mere) in bracken-covered ground: a stage on the road down to the capital. |
| **Drovers Halt** | small town | XB, Coastal State | 145/107 | 30.4099 S 13.0577 W (30° 24.59′ S, 13° 03.46′ W) | 82 m | 7,000 | On the coast road from Larkmouth to Lumeport, where it crosses a stream at a confluence: an inn where drovers rested their stock. |
| **Fleecewell** | small town | XB, Coastal State | 152/89 | 29.8423 S 12.8036 W (29° 50.54′ S, 12° 48.21′ W) | 74 m | 6,000 | Just south of Larkmouth on the coast road and the wool line, at a well where the flocks were watered and washed before shearing. |
| **Harrowmead** | small town | XB, Upland State | 96/105 | 30.3468 S 14.8366 W (30° 20.81′ S, 14° 50.20′ W) | 326 m | 5,000 | On the plateau near the border, on a confluence in the wetter western part of Bayvarra. |
| **Hartsedge** | small town | XB, Coastal State | 148/98 | 30.1261 S 12.9488 W (30° 07.57′ S, 12° 56.93′ W) | 206 m | 5,000 | At a station on the wool line between Marrowdale and Larkmouth, on the edge of a rise. |
| **Saltmere** | small town | XB, Coastal State | 155/109 | 30.4730 S 12.6946 W (30° 28.38′ S, 12° 41.68′ W) | 14 m | 6,000 | On a sheltered creek of the east coast between Larkmouth and Lumeport, among salt meadows behind the shore, a few kilometres off the coast road. |
| **Wadebank** | small town | XB, Coastal State | 139/116 | 30.6937 S 13.2755 W (30° 41.62′ S, 13° 16.53′ W) | 57 m | 9,000 | On the north shore of Lumeport's bay, on the road north, where the shore shelves gently. |
| **Wetherholme** | small town | XB, Upland State | 115/85 | 29.7162 S 14.1468 W (29° 42.97′ S, 14° 08.81′ W) | 216 m | 6,000 | Where two rivers of the plateau meet, the homestead of one of the first sheep runs. |
| **Ewesbridge** | large village | XB, Coastal State | 137/72 | 29.3063 S 13.3481 W (29° 18.38′ S, 13° 20.89′ W) | 143 m | 1,000 | On the road north from Larkmouth over the dry east, at a bridge over a creek. |
| **Ternhaven** | large village | XB, Coastal State | 161/102 | 30.2523 S 12.4768 W (30° 15.14′ S, 12° 28.61′ W) | 8 m | 1,260 | At a creek mouth on the east coast, behind a spit where terns nest. |
| **Ploverness** | village | XB, Northern Territory | 124/53 | 28.7072 S 13.8201 W (28° 42.43′ S, 13° 49.21′ W) | 15 m | 250 | On a low point of the north coast at a stream mouth. |
| **Shinglebeck** | village | XB, Northern Territory | 92/47 | 28.5180 S 14.9818 W (28° 31.08′ S, 14° 58.91′ W) | 11 m | 250 | Where a stream comes down to a shingle shore of the north coast, on the coast road. |
| **Selanu** | capital | XL, - | 237/112 | 33.0000 S 2.2001 W (33° 00.00′ S, 2° 12.01′ W) | 121 m (3D map 88 m) | 30,000 | The Lisavan village on the sheltered bay of the east-south-east coast, which gave the town its name. |
| **Bollworth (Pakesa)** | large village | XL, - | 239/105 | 32.7793 S 2.1252 W (32° 46.76′ S, 2° 07.51′ W) | 32 m | 1,000 | On the coast of the cotton plain north of Selanu, where the estates landed their bales for the ships. |
| **Felulaka** | large village | XL, - | 211/106 | 32.8108 S 3.1748 W (32° 48.65′ S, 3° 10.49′ W) | 10 m | 2,500 | On a flat of old landslide debris at the foot of the west cliffs (a faja), reached by a track down the cliff. |
| **Lintwell (Kefalasa)** | large village | XL, - | 234/106 | 32.8108 S 2.3126 W (32° 48.65′ S, 2° 18.76′ W) | 142 m | 1,740 | On the dry north-eastern plain on the road north of the town, at a well dug for an English settler's cotton estate. |
| **Linukaha** | large village | XL, - | 227/122 | 33.3153 S 2.5750 W (33° 18.92′ S, 2° 34.50′ W) | 48 m | 2,140 | At the mouth of the largest stream of the south coast, where two streams meet. |
| **Natahoma** | large village | XL, - | 230/106 | 32.8108 S 2.4626 W (32° 48.65′ S, 2° 27.75′ W) | 119 m | 2,500 | In the most sheltered bay of the north coast, where a stream comes in. |
| **Nihekemo** | large village | XL, - | 218/123 | 33.3468 S 2.9124 W (33° 20.81′ S, 2° 54.75′ W) | 22 m | 1,000 | On the south-west coast where a stream falls from the cliffs to the shore. |
| **Setahu** | large village | XL, - | 220/101 | 32.6532 S 2.8374 W (32° 39.19′ S, 2° 50.25′ W) | 123 m | 2,500 | On the north coast west of the cotton plain, under a headland that keeps off the westerly swell: the last landing before the cliffs of the windward side. |

**Other places the documents use:**

| Place | Country | Square | Position (WGS 84) | Height | What it is |
|---|---|---|---|---|---|
| Gas platform (Kelpstone Gas) | offshore, XB's shelf | 78/15 | 27.5090 S 15.4901 W (27° 30.54′ S, 15° 29.41′ W) | sea | The gas field's production platform, offshore: it has no name or address in the documents, only its place in the world's map grid and its WGS 84 coordinates. Offshore block 19/03. |
| Border metering station (gas pipeline) | XB, Northern Territory | 72/52 | 28.6757 S 15.7079 W (28° 40.54′ S, 15° 42.48′ W) | 297 m | The border metering station of the gas pipeline, on Bayvarra's side of the border: it measures the gas that crosses into Urvania. |
| Road border crossing (route `road`) | XU/XB | 96/120 → 97/120 | 30.8198 S 14.8003 W (30° 49.19′ S, 14° 48.02′ W) | 134 m | Where the main road from Ferrano to Marrowdale passes from Urvania into Bayvarra. |
| The border's river point (terrain "crossing") | XU/XB | 97.38/123.12 | 30.9182 S 14.7865 W (30° 55.09′ S, 14° 47.19′ W) | river | Where the land border meets the main river, at the confluence of the largest plateau tributary; below it the river is the border. |

## 2. Parties

Every party on the map with its place (the town of its address), the district of that town nearest to it, its distance and direction from the place's centre, and the position its documents state. "Built-up" is the world model's verdict: inside the town's built-up area, at its edge, or outside it.

| Party | Address: street, city (quarter) | Place | District nearest | From the centre | Built-up | Square | Position (WGS 84) | Height |
|---|---|---|---|---|---|---|---|---|
| Serravona Mining (4-xu) | Strada della Miniera, Fucinalta | Fucinalta | - | 25.2 km NW | - | 48/85 | 29.7162 S 16.5793 W (29° 42.97′ S, 16° 34.76′ W) | 723 m |
| Valdara Industries (5-xu) | Via delle Officine, Ferrano | Ferrano | Quartiere Est (suburb, 4.2 km) | 9.9 km NE | edge | 79/114 | 30.6306 S 15.4538 W (30° 37.84′ S, 15° 27.23′ W) | 270 m |
| Castrano Logistics (8-xu) | Via del Magazzino, Conciaro | Conciaro | - | 7.8 km SW | - | 82/115 | 30.6622 S 15.3449 W (30° 39.73′ S, 15° 20.69′ W) | 310 m |
| Rinova Recovery (7-xu) | Via del Riciclo, Ferrano | Ferrano | Oltreponte (suburb, 1.7 km) | 7.0 km S | inside | 77/118 | 30.7568 S 15.5264 W (30° 45.41′ S, 15° 31.59′ W) | 181 m (3D map 71 m) |
| Ferrano Rail Cargo (14-xu) | Viale della Stazione, Serravona | Serravona | - | 7.0 km S | outside | 56/89 | 29.8423 S 16.2888 W (29° 50.54′ S, 16° 17.33′ W) | 473 m |
| Trasvia Haulage (13-xu) | Via dei Trasporti, Ferrano | Ferrano | Zona Industriale (industry, 5.2 km) | 10.5 km E | inside | 80/116 | 30.6937 S 15.4175 W (30° 41.62′ S, 15° 25.05′ W) | 259 m (3D map 206 m) |
| Fiumella Barges (15-xu) | Banchina del Fiume, Ferrano | Ferrano | Borgo Nord (suburb, 11.1 km) | 14.0 km W | outside | 73/116 | 30.6937 S 15.6716 W (30° 41.62′ S, 15° 40.30′ W) | 190 m (3D map 91 m) |
| Ferrano Intermodal Hub (18-xu) | Via del Terminal, Ferrano | Ferrano | Zona Industriale (industry, 6.1 km) | 9.9 km SE | inside | 79/118 | 30.7568 S 15.4538 W (30° 45.41′ S, 15° 27.23′ W) | 180 m (3D map 131 m) |
| Crevalto Bank (23-xu) | Piazza della Banca, Ferrano | Ferrano | Villaggio Inglese (residential, 0.9 km) | 4.9 km NW | inside | 76/115 | 30.6622 S 15.5627 W (30° 39.73′ S, 15° 33.76′ W) | 228 m |
| Ferrano Chamber of Commerce (20-xu) | Piazza del Mercato, Ferrano | Ferrano | Scalo (industry, 1.7 km) | 4.9 km NE | inside | 78/115 | 30.6622 S 15.4901 W (30° 39.73′ S, 15° 29.41′ W) | 240 m |
| Customs Administration of Urvania (19-xu) | Strada del Confine, Valico Euridice | Valico Euridice | - | at the centre | inside | 96/120 | 30.8198 S 14.8366 W (30° 49.19′ S, 14° 50.20′ W) | 153 m |
| Codana Identification Agency (31-xu) | Via dei Codici, Ferrano | Ferrano | Oltreponte (suburb, 5.2 km) | 4.9 km SW | edge | 76/117 | 30.7252 S 15.5627 W (30° 43.51′ S, 15° 33.76′ W) | 192 m (3D map 131 m) |
| Customs and Border Service of Bayvarra (19-xb) | Border Road, Euridice Crossing | Euridice Crossing | - | at the centre | inside | 97/120 | 30.8198 S 14.8003 W (30° 49.19′ S, 14° 48.02′ W) | 134 m |
| Lumeway Distribution (6-xb) | Distribution Drive, Marrowdale | Marrowdale | Depot Road (industry, 2.7 km) | 4.9 km SE | inside | 124/113 | 30.5991 S 13.8201 W (30° 35.95′ S, 13° 49.21′ W) | 280 m |
| Brightmarket Stores (26-xb) | Market Street, Lumeport (Old Town) | Lumeport | Westside (industry, 2.7 km) | 4.9 km NW | inside | 137/125 | 30.9775 S 13.3481 W (30° 58.65′ S, 13° 20.89′ W) | 128 m (3D map 93 m) |
| Robin Ashdale (c-xb) | Gull Lane, Lumeport (Riverside) | Lumeport | Dockside (port, 7.0 km) | 9.9 km SW | edge | 136/128 | 31.0721 S 13.3844 W (31° 04.32′ S, 13° 23.07′ W) | 19 m |
| Lumeport Public Works Department (2-xb) | Civic Square, Lumeport (Government Hill) | Lumeport | Government Hill (administration, 3.2 km) | 4.9 km SE | inside | 139/127 | 31.0405 S 13.2755 W (31° 02.43′ S, 13° 16.53′ W) | 88 m |
| Saltmere Engineering (27-xb) | Foundry Road, Marrowdale | Marrowdale | Market Square (core, 7.7 km) | 7.8 km NE | edge | 125/111 | 30.5360 S 13.7838 W (30° 32.16′ S, 13° 47.03′ W) | 299 m |
| Procurement Review Board of Bayvarra (28-xb) | Justice Row, Lumeport (Government Hill) | Lumeport | Government Hill (administration, 6.2 km) | 7.8 km SE | edge | 140/127 | 31.0405 S 13.2392 W (31° 02.43′ S, 13° 14.35′ W) | 66 m |
| Bayvarra Information Service (21-xb) | Civic Square, Lumeport (Government Hill) | Lumeport | Northshore (suburb, 4.8 km) | 7.8 km NE | edge | 140/125 | 30.9775 S 13.2392 W (30° 58.65′ S, 13° 14.35′ W) | 64 m |
| Lumeport Trade Accord Council (32-xb) | Exchange Street, Lumeport (Old Town) | Lumeport | Northshore (suburb, 2.0 km) | 7.8 km NE | inside | 139/124 | 30.9459 S 13.2755 W (30° 56.76′ S, 13° 16.53′ W) | 58 m |
| Harbourline Factoring (24-xb) | Exchange Street, Lumeport (Old Town) | Lumeport | Northshore (suburb, 2.0 km) | 4.9 km NE | inside | 139/125 | 30.9775 S 13.2755 W (30° 58.65′ S, 13° 16.53′ W) | 97 m |
| Bank of Lumeport (25-xb) | Exchange Street, Lumeport (Old Town) | Lumeport | Dockside (port, 2.3 km) | 4.9 km SW | inside | 137/127 | 31.0405 S 13.3481 W (31° 02.43′ S, 13° 20.89′ W) | 85 m |
| Wavesure Cargo Insurance (29-xb) | Beacon Avenue, Lumeport (Dockside) | Lumeport | Dockside (port, 6.2 km) | 7.8 km SE | edge | 139/128 | 31.0721 S 13.2755 W (31° 04.32′ S, 13° 16.53′ W) | 39 m |
| Bayforth Forwarding (10-xb) | Dockside Way, Lumeport (Dockside) | Lumeport | Westside (industry, 3.0 km) | 7.8 km NW | inside | 136/125 | 30.9775 S 13.3844 W (30° 58.65′ S, 13° 23.07′ W) | 113 m |
| Port of Lumeport (16-xb) | Harbour Road, Lumeport (Dockside) | Lumeport | Dockside (port, 9.4 km) | 12.6 km SW | edge | 136/129 | 31.1036 S 13.3844 W (31° 06.22′ S, 13° 23.07′ W) | 9 m |
| Tidewell Ocean Lines (11-xb) | Harbour Road, Lumeport (Dockside) | Lumeport | Dockside (port, 9.2 km) | 9.9 km SE | edge | 140/128 | 31.0721 S 13.2392 W (31° 04.32′ S, 13° 14.35′ W) | 24 m |
| Lumeport Airport Cargo Terminal (17-xb) | Airport Road, Lumeport | Lumeport | Northshore (suburb, 12.9 km) | 15.7 km NW | outside | 136/122 | 30.8829 S 13.3844 W (30° 52.97′ S, 13° 23.07′ W) | 149 m (3D map 110 m) |
| Port of Selanu (16-xl) | Wharf Road, Selanu | Selanu | Port Wrenfield (port, 6.7 km) | 7.8 km NE | edge | 238/110 | 32.9369 S 2.1626 W (32° 56.22′ S, 2° 09.76′ W) | 45 m (3D map 0 m) |
| Selanu Airport Cargo (17-xl) | Airfield Road, Lintwell | Lintwell | - | 12.6 km SE | - | 236/109 | 32.9054 S 2.2376 W (32° 54.32′ S, 2° 14.26′ W) | 123 m (3D map 30 m) |
| Kelaro Air Cargo (12-xl) | Airfield Road, Lintwell | Lintwell | - | 7.8 km SE | - | 235/108 | 32.8739 S 2.2751 W (32° 52.43′ S, 2° 16.51′ W) | 100 m |
| Island Customs Service (19-xl) | Wharf Road, Selanu | Selanu | Port Wrenfield (port, 5.9 km) | 7.0 km N | outside | 237/110 | 32.9369 S 2.2001 W (32° 56.22′ S, 2° 12.01′ W) | 103 m (3D map 25 m) |
| Tevaro Customs Brokers (3-xl) | Wharf Road, Selanu | Selanu | Agreement Quarter (industry, 2.7 km) | 4.9 km SW | inside | 236/113 | 33.0315 S 2.2376 W (33° 01.89′ S, 2° 14.26′ W) | 130 m |
| Nalevi Warehousing (9-xl) | Lagoon Road, Selanu | Selanu | Agreement Quarter (industry, 5.8 km) | 7.8 km SW | edge | 235/113 | 33.0315 S 2.2751 W (33° 01.89′ S, 2° 16.51′ W) | 210 m (3D map 140 m) |
| Velumi Trading (1-xl) | Reef Street, Selanu | Selanu | Port Wrenfield (port, 4.4 km) | 4.9 km NW | edge | 236/111 | 32.9685 S 2.2376 W (32° 58.11′ S, 2° 14.26′ W) | 130 m |
| Bank of Selanu (22-xl) | Reef Street, Selanu | Selanu | Selanu (core, 4.2 km) | 4.9 km SE | edge | 238/113 | 33.0315 S 2.1626 W (33° 01.89′ S, 2° 09.76′ W) | 40 m |
| Selanu Chamber of Commerce (20-xl) | Reef Street, Selanu | Selanu | Agreement Quarter (industry, 5.8 km) | 7.8 km SW | edge | 236/114 | 33.0631 S 2.2376 W (33° 03.78′ S, 2° 14.26′ W) | 88 m (3D map 60 m) |
| Maritime Administration of Lisavu (30-xl) | Wharf Road, Selanu | Selanu | Agreement Quarter (industry, 7.4 km) | 7.8 km NW | edge | 235/111 | 32.9685 S 2.2751 W (32° 58.11′ S, 2° 16.51′ W) | 164 m |
| Department of Agriculture of Lisavu (45-xl) | Reef Street, Selanu | Selanu | Selanu (core, 3.1 km) | 3.5 km E | edge | 238/112 | 33.0000 S 2.1626 W (33° 00.00′ S, 2° 09.76′ W) | 82 m (3D map 34 m) |
| Ferrano Energy (33-xu) | Corso della Repubblica, Ferrano | Ferrano | Zona Industriale (industry, 3.0 km) | 4.9 km SE | inside | 78/117 | 30.7252 S 15.4901 W (30° 43.51′ S, 15° 29.41′ W) | 198 m (3D map 131 m) |
| Coastal State Water Company (34-xb) | Reservoir Road, Lumeport | Lumeport | Westside (industry, 9.2 km) | 14.4 km W | outside | 134/125 | 30.9775 S 13.4570 W (30° 58.65′ S, 13° 27.42′ W) | 37 m |
| Selanu Telecom (35-xl) | Mast Hill Road, Selanu | Selanu | Agreement Quarter (industry, 19.5 km) | 21.3 km W | outside | 231/113 | 33.0315 S 2.4251 W (33° 01.89′ S, 2° 25.50′ W) | 638 m |
| Marrowdale Sawmill (36-xb) | Timber Lane, Marrowdale | Marrowdale | Market Square (core, 10.0 km) | 9.9 km SW | edge | 121/114 | 30.6306 S 13.9290 W (30° 37.84′ S, 13° 55.74′ W) | 232 m |
| Brackenmere Furniture (37-xb) | Joiners Row, Marrowdale | Marrowdale | Market Square (core, 7.7 km) | 7.8 km NW | outside | 121/111 | 30.5360 S 13.9290 W (30° 32.16′ S, 13° 55.74′ W) | 290 m |
| Lumeport Textile Mill (40-xb) | Mill Street, Lumeport (Mill Quarter) | Lumeport | Northshore (suburb, 5.3 km) | 11.1 km N | edge | 139/123 | 30.9144 S 13.2755 W (30° 54.86′ S, 13° 16.53′ W) | 20 m |
| Rivermouth Packaging (41-xb) | Estuary Road, Lumeport | Lumeport | Westside (industry, 12.7 km) | 17.8 km W | outside | 133/125 | 30.9775 S 13.4933 W (30° 58.65′ S, 13° 29.60′ W) | 8 m |
| Lisavu Cotton Farm (38-xl) | Plantation Road, Lintwell | Lintwell | - | 7.8 km NE | - | 235/104 | 32.7477 S 2.2751 W (32° 44.86′ S, 2° 16.51′ W) | 166 m |
| Selanu Cotton Ginnery (39-xl) | Gin Yard Road, Bollworth | Bollworth | - | 7.0 km S | - | 239/107 | 32.8423 S 2.1252 W (32° 50.54′ S, 2° 07.51′ W) | 14 m |
| Kelpstone Gas (42-xb) | Shoreline Road, Gullhaven | Gullhaven | - | 10.5 km E | outside | 76/39 | 28.2658 S 15.5627 W (28° 15.95′ S, 15° 33.76′ W) | 20 m |
| Montebrio Power (43-xu) | Via della Centrale, Serravona | Serravona | - | 17.8 km N | outside | 57/82 | 29.6216 S 16.2525 W (29° 37.30′ S, 16° 15.15′ W) | 561 m |
| Ferrano Grid (44-xu) | Via della Rete, Ferrano | Ferrano | Borgo Nord (suburb, 16.0 km) | 22.4 km NW | outside | 72/112 | 30.5676 S 15.7079 W (30° 34.05′ S, 15° 42.48′ W) | 273 m |
| Environment Agency of Urvania (46-xu) | Via delle Acque, Ferrano | Ferrano | Borgo Nord (suburb, 6.5 km) | 11.1 km W | edge | 74/115 | 30.6622 S 15.6353 W (30° 39.73′ S, 15° 38.12′ W) | 205 m (3D map 151 m) |

## 3. Distances along the routes

### 3.1 The named routes

Every road, railway and pipeline of the map except the villages' minor roads and the parties' access roads, with its length along its squares, the straight line between its ends and the detour factor (length ÷ straight line). The ends are named after the nearest place or party.

| Route | Mode | What it is | From → to | Length | Straight | Factor | Earlier (old list; D19/D44) |
|---|---|---|---|---|---|---|---|
| `ore` | rail | Ore by rail (domestic XU) | Serravona Mining → Valdara Industries | **165.7 km** | 148.6 km | 1.12 | 154; about 154 |
| `rail-x` | rail | Containers from Ferrano past the border hub to the distributor's siding | Ferrano (12.6 km SE) → Lumeway Distribution | **179.8 km** | 155.0 km | 1.16 | - |
| `factory-siding` | rail | The factory's second siding, for outgoing loads | Pomarella (10.5 km S) → Ferrano Intermodal Hub | **15.4 km** | 14.4 km | 1.07 | - |
| `road` | main road | Finished goods by road, across the border (XU → XB) | Ferrano → Marrowdale | **192.0 km** | 161.6 km | 1.19 | 182; 182 (documents 186) |
| `road-b` | main road | Distributor to retailer (domestic XB) | Marrowdale → Lumeport (3.5 km W) | **77.5 km** | 69.3 km | 1.12 | - |
| `road-port` | main road | Lumeport's centre to the port | Lumeport (3.5 km W) → Lumeport (11.1 km S) | **15.4 km** | 10.5 km | 1.47 | - |
| `road-c` | minor road | Port to buyer (domestic XL) | Selanu (10.5 km N) → Selanu | **10.5 km** | 10.5 km | 1.00 | - |
| `road-farm` | main road | Ferrano to the farms (domestic XU) | Ferrano → Grancelle (11.1 km S) | **44.9 km** | 42.0 km | 1.07 | - |
| `gas` | pipeline | Gas pipeline from the gas plant across the border to the power station (XB → XU) | Gullhaven (14.4 km E) → Serravona (17.5 km NE) | **206.6 km** | 163.2 km | 1.27 | about 255 (via the metering station); about 196 (D44) |
| `gas-grid` | pipeline | Branch of the gas pipeline to the grid operator's city gate (XU) | Serravona (24.5 km E) → Pietramiglia (22.1 km S) | **97.0 km** | 89.7 km | 1.08 | about 210; about 98 (D44) |
| `gas-field` | pipeline | Subsea pipeline from the offshore platform to the gas plant | the gas platform → Gullhaven (11.1 km E) | **83.4 km** | 80.8 km | 1.03 | about 38; about 80 (D44); documents: four kilometres |
| `rail-lark` | rail | The wool line from Marrowdale down to Larkmouth's harbour | Marrowdale (7.8 km SE) → Larkmouth (3.5 km E) | **160.8 km** | 148.6 km | 1.08 | - |
| `rail-port` | rail | The port line from Marrowdale down to the quays of the Port of Lumeport | Marrowdale (7.8 km SE) → Lumeport (11.1 km S) | **82.4 km** | 69.5 km | 1.19 | - |
| `road-lark` | main road | Larkmouth down the coast to Lumeport (domestic XB) | Larkmouth (3.5 km W) → Lumeport (3.5 km W) | **178.6 km** | 154.0 km | 1.16 | - |
| `road-wool` | main road | Larkmouth inland to Marrowdale (domestic XB) | Larkmouth (3.5 km W) → Marrowdale | **177.8 km** | 141.3 km | 1.26 | - |
| `road-serra` | main road | Ferrano up the valley to Serravona and across the river to the mine (domestic XU) | Ferrano → Serravona Mining | **178.0 km** | 148.6 km | 1.20 | - |
| `road-north` | minor road | Larkmouth north-west to Gullhaven on the north coast (domestic XB) | Larkmouth (3.5 km W) → Gullhaven | **346.7 km** | 323.0 km | 1.07 | - |
| `waste` | minor road | Production waste | Valdara Industries → Rinova Recovery | **18.9 km** | 15.7 km | 1.21 | - |

### 3.2 Between the towns by road

The shortest way on the road network between the centres (the road square nearest each centre), as `tools/lay_routes.py --report` gives it, with the main routes it uses.

| Between | By road | Routes | Straight | Factor | Earlier (old list; D19) |
|---|---|---|---|---|---|
| Ferrano – Marrowdale | **192 km** | `road`, `waste` | 162 km | 1.19 | 182; 182 (documents 186) |
| Marrowdale – Lumeport | **81 km** | `road-b`, `road-wool`, `road-lark` | 72 km | 1.13 | 84; 84 (documents 38) |
| Ferrano – Lumeport | **273 km** | `road`, `waste`, `road-b`, `road-wool`, `road-lark` | 216 km | 1.26 | - |
| Lumeport – Larkmouth | **182 km** | `road-b`, `road-lark`, `road-wool` | 154 km | 1.18 | - |
| Larkmouth – Marrowdale | **175 km** | `road-lark`, `road-wool`, `road-b` | 144 km | 1.22 | - |
| Ferrano – Serravona | **144 km** | `road-serra` | 125 km | 1.15 | - |
| Larkmouth – Gullhaven | **347 km** | `road-north` | 326 km | 1.06 | - |
| Ferrano – Gullhaven | **714 km** | `road`, `waste`, `road-b`, `road-wool`, `road-lark`, `road-north` | 270 km | 2.64 | - |

### 3.3 The transport legs of the flows

Every leg of `world/documents.json` as the world model lays it on the map, party to party (the way the map's vehicles drive: the fewest squares from building to building), and for road legs also the shortest way in kilometres on the road network, with the routes used, the straight line, the detour factor and the time the distance takes at the mode's usual average (truck 60–70 km/h with breaks, freight train 40–60 km/h, barge 10–12 km/h). Sea and air legs are in section 4.

| Flow | Mode | From → to | On the map | Shortest | Routes | Straight | Factor | Time at usual speed | transit_days |
|---|---|---|---|---|---|---|---|---|---|
| ore | rail | Serravona Mining (4-xu) → Valdara Industries (5-xu) | **158.7 km** | - | `ore` | 148.6 km | 1.07 | 2 h 39 – 3 h 58 | 0 |
| road | road | Castrano Logistics (8-xu) → Lumeway Distribution (6-xb) | **174.3 km** | 174.3 km | `road` | 147.2 km | 1.18 | 2 h 29 – 2 h 54 | 2 |
| rail | road | Castrano Logistics (8-xu) → Ferrano Intermodal Hub (18-xu) | **45.7 km** | 45.7 km | `road`, `waste`, `road-farm` | 14.8 km | 3.08 | 0 h 39 – 0 h 46 | - |
| rail | rail | Ferrano Intermodal Hub (18-xu) → Lumeway Distribution (6-xb) | **172.8 km** | - | `rail-x` | 158.5 km | 1.09 | 2 h 53 – 4 h 19 | - |
| plastics | river | Rinova Recovery (7-xu) → Rivermouth Packaging (41-xb) | **253.4 km** | - | the river's course and the estuary | 197.5 km | 1.28 | 21 h 07 – 25 h 21 | 3 |
| retail | road | Lumeway Distribution (6-xb) → Brightmarket Stores (26-xb) | **72.5 km** | 72.5 km | `road-b` | 61.9 km | 1.17 | 1 h 02 – 1 h 13 | - |
| retail | road | Brightmarket Stores (26-xb) → Robin Ashdale (c-xb) | **14.0 km** | 14.0 km | `road-port` | 11.1 km | 1.26 | 0 h 12 – 0 h 14 | - |
| sea | road | Lumeway Distribution (6-xb) → Port of Lumeport (16-xb) | **82.4 km** | 82.4 km | `road-b`, `road-port` | 70.0 km | 1.18 | 1 h 11 – 1 h 22 | - |
| sea | road | Port of Selanu (16-xl) → Nalevi Warehousing (9-xl) | **17.5 km** | 17.5 km | town streets, minor roads | 14.8 km | 1.18 | 0 h 15 – 0 h 18 | - |
| air | road | Lumeway Distribution (6-xb) → Lumeport Airport Cargo Terminal (17-xb) | **58.5 km** | 58.5 km | `road-b` | 52.5 km | 1.12 | 0 h 50 – 0 h 59 | - |
| air | road | Selanu Airport Cargo (17-xl) → Nalevi Warehousing (9-xl) | **21.0 km** | 21.0 km | `road-c` | 14.4 km | 1.46 | 0 h 18 – 0 h 21 | - |
| tender | road | Castrano Logistics (8-xu) → Lumeport Public Works Department (2-xb) | **255.3 km** | 255.3 km | `road`, `road-b`, `road-wool`, `road-lark` | 203.9 km | 1.25 | 3 h 39 – 4 h 15 | - |
| carnet | road | Valdara Industries (5-xu) → Lumeport Airport Cargo Terminal (17-xb) | **244.2 km** | 244.2 km | `road`, `road-b`, `road-wool` | 201.5 km | 1.21 | 3 h 29 – 4 h 04 | - |
| carnet | road | Selanu Airport Cargo (17-xl) → Selanu Chamber of Commerce (20-xl) | **21.0 km** | 21.0 km | `road-c` | 17.5 km | 1.20 | 0 h 18 – 0 h 21 | - |
| carnet | road | Selanu Chamber of Commerce (20-xl) → Selanu Airport Cargo (17-xl) | **21.0 km** | 21.0 km | `road-c` | 17.5 km | 1.20 | 0 h 18 – 0 h 21 | - |
| carnet | road | Lumeport Airport Cargo Terminal (17-xb) → Valdara Industries (5-xu) | **244.2 km** | 244.2 km | `road-b`, `road-wool`, `road` | 201.5 km | 1.21 | 3 h 29 – 4 h 04 | - |
| waste | road | Valdara Industries (5-xu) → Rinova Recovery (7-xu) | **18.9 km** | 18.9 km | `road`, `waste` | 15.7 km | 1.21 | 0 h 16 – 0 h 19 | - |
| wood | road | Marrowdale Sawmill (36-xb) → Valdara Industries (5-xu) | **185.6 km** | 185.6 km | `road` | 147.0 km | 1.26 | 2 h 39 – 3 h 06 | 0 |
| wood | road | Marrowdale Sawmill (36-xb) → Brackenmere Furniture (37-xb) | **14.0 km** | 14.0 km | town streets, minor roads | 10.5 km | 1.33 | 0 h 12 – 0 h 14 | - |
| furniture | road | Brackenmere Furniture (37-xb) → Brightmarket Stores (26-xb) | **86.5 km** | 86.5 km | `road`, `road-b`, `road-wool` | 74.4 km | 1.16 | 1 h 14 – 1 h 27 | - |
| furniture | road | Brightmarket Stores (26-xb) → Brackenmere Furniture (37-xb) | **86.5 km** | 86.5 km | `road-b`, `road-wool`, `road` | 74.4 km | 1.16 | 1 h 14 – 1 h 27 | - |
| furniture | road | Brackenmere Furniture (37-xb) → Lumeport Public Works Department (2-xb) | **98.5 km** | 98.5 km | `road`, `road-b`, `road-wool`, `road-lark` | 84.3 km | 1.17 | 1 h 24 – 1 h 38 | - |
| cotton | road | Lisavu Cotton Farm (38-xl) → Selanu Cotton Ginnery (39-xl) | **42.2 km** | 42.2 km | town streets, minor roads | 17.5 km | 2.41 | 0 h 36 – 0 h 42 | - |
| cotton | road | Selanu Cotton Ginnery (39-xl) → Port of Selanu (16-xl) | **11.9 km** | 11.9 km | town streets, minor roads | 11.1 km | 1.08 | 0 h 10 – 0 h 12 | - |
| cotton | road | Port of Lumeport (16-xb) → Lumeport Textile Mill (40-xb) | **35.8 km** | 35.8 km | `road-port`, `road-lark` | 23.5 km | 1.53 | 0 h 31 – 0 h 36 | - |
| packaging | road | Rivermouth Packaging (41-xb) → Valdara Industries (5-xu) | **258.2 km** | 258.2 km | `road-b`, `road-wool`, `road` | 192.9 km | 1.34 | 3 h 41 – 4 h 18 | - |
| packaging | road | Rivermouth Packaging (41-xb) → Lumeport Textile Mill (40-xb) | **28.0 km** | 28.0 km | `road-lark` | 22.1 km | 1.26 | 0 h 24 – 0 h 28 | - |
| packaging | road | Lumeport Textile Mill (40-xb) → Brightmarket Stores (26-xb) | **14.0 km** | 14.0 km | `road-lark` | 9.9 km | 1.41 | 0 h 12 – 0 h 14 | - |
| mast | road | Saltmere Engineering (27-xb) → Lumeport Airport Cargo Terminal (17-xb) | **58.5 km** | 58.5 km | `road-b` | 54.4 km | 1.08 | 0 h 50 – 0 h 59 | - |
| mast | road | Selanu Airport Cargo (17-xl) → Selanu Telecom (35-xl) | **32.9 km** | 32.9 km | `road-c` | 22.4 km | 1.47 | 0 h 28 – 0 h 33 | - |
| energy | pipeline | Kelpstone Gas (42-xb) → Montebrio Power (43-xu) | **206.6 km** | - | `gas` | 164.5 km | 1.26 | - | - |
| energy | pipeline | Kelpstone Gas (42-xb) → Ferrano Grid (44-xu) | **281.8 km** | - | `gas`, `gas-grid` | 255.9 km | 1.10 | - | - |

**Legs inside one town or its surroundings** (the diagram's party squares make them longer than on the ground; O82, O92):

- retail: Brightmarket Stores (26-xb) → Robin Ashdale (c-xb), both in Lumeport: 14.0 km on the map.
- sea: Port of Selanu (16-xl) → Nalevi Warehousing (9-xl), both in Selanu: 17.5 km on the map.
- waste: Valdara Industries (5-xu) → Rinova Recovery (7-xu), both in Ferrano: 18.9 km on the map.
- wood: Marrowdale Sawmill (36-xb) → Brackenmere Furniture (37-xb), both in Marrowdale: 14.0 km on the map.
- cotton: Port of Lumeport (16-xb) → Lumeport Textile Mill (40-xb), both in Lumeport: 35.8 km on the map.
- packaging: Rivermouth Packaging (41-xb) → Lumeport Textile Mill (40-xb), both in Lumeport: 28.0 km on the map.
- packaging: Lumeport Textile Mill (40-xb) → Brightmarket Stores (26-xb), both in Lumeport: 14.0 km on the map.

## 4. The long distances: Lumeport – Selanu

The sea route `sea` of the map, measured on the real ocean: its squares on the mainland side (Lumeport's port out through the estuary and the bay) and on Lisavu's side (from the open sea south-west of the island round its south-eastern cape and up the lee coast to the port) along the map, and the open ocean between them as the great circle between the stated positions.

| | Distance | Nautical miles | Time |
|---|---|---|---|
| Lumeport port – Selanu port, straight line (great circle) | 1,077 km | 581 nm | |
| Sea route: Lumeport port to the open sea | 56 km | 30 nm | |
| Sea route: open ocean, 150/136 to 200/132 | 908 km | 490 nm | |
| Sea route: round the cape to Selanu port | 232 km | 125 nm | |
| **Sea route, in all** | **1,196 km** | **646 nm** | **47 h 50 at 13.5 knots** (factor 1.11) |
| **Lumeport airport – Selanu airport, great circle** | **1,076 km** | **581 nm** | 2 h 27 gate to gate in still air (taxi 10 min, climb and descent 20 min over about 100 km, cruise at 500 km/h) |

**Against the decisions:**

- D19: "about 1,050 km by sea", "about 570 nautical miles, 42 hours at 13.5 knots"; the old place list: about 1,150 km, 620 nm, 46 hours. The map's route: **1,196 km, 646 nm, 47 h 50**. O53 asks for one passage time (the documents have 38 to 43 hours); O123 for the crossing of about 42–46 hours.
- D19 as corrected with D36: the flight about 1,100 km, about 2 h 30 gate to gate in still air, about 2 h 15–2 h 20 eastbound with the westerlies, 2 h 45 westbound; block times 2 h 45 east and 3 h 00 west. The positions now give **1,076 km** and **2 h 27** in still air: the block times keep their margin. The island's clocks are an hour ahead (D27).
- The straight line port to port is 1,077 km (D19: about 1,000 km).

## 5. What changed against the old place list and D19/D44

| | Old place list | D19 / D44 | Now (the map) |
|---|---|---|---|
| Ferrano | 30.60° S 15.90° W (proposed; D19 16.4° W) | 30.6° S 16.4° W | 30.6937 S 15.5264 W (30° 41.62′ S, 15° 31.59′ W) |
| Lumeport | 31.40° S 13.80° W | 31.4° S 13.8° W | 31.0090 S 13.3118 W (31° 00.54′ S, 13° 18.71′ W) |
| Selanu | 33.05° S 2.22° W | near 33.0° S 2.65° W (island centre) | 33.0000 S 2.2001 W (33° 00.00′ S, 2° 12.01′ W) |
| Marrowdale | 31.01° S 14.41° W | - | 30.5676 S 13.8564 W (30° 34.05′ S, 13° 51.38′ W) |
| Ferrano – Marrowdale by road | 182 km | 182 km (documents 186) | 192.0 km (`road`) |
| Marrowdale – Lumeport by road | 84 km | 84 km (documents 38) | 81 km centre to centre; 77.5 km along `road-b` |
| Mine – works by rail | 154 | about 154 | 165.7 km (`ore`) |
| Gas pipeline, plant to power station | about 255 (via the metering station) | about 196 (D44) | 206.6 km (`gas`) |
| Branch to the city gate | about 210 | about 98 (D44) | 97.0 km (`gas-grid`) |
| Gas field line | about 38 | about 80 (D44); documents: four kilometres | 83.4 km (`gas-field`) |
| River, Rinova's quay – Rivermouth's quay | about 285 km | - | 253.4 km |
| Lumeport – Selanu by sea | about 1,150 km, 46 h | about 1,050 km, 42 h | 1,196 km, 47 h 50 |
| Lumeport – Selanu by air | 1,107 km | about 1,100 km | 1,076 km |
| Lumeport airport from the centre | 17 km SW | 10–15 km (O91) | 15.7 km NW |
| Selanu airport from the town | 10 km NW | about 10 km (O91) | 11.1 km N |

The old list's five questions are settled by the map: Ferrano and Lumeport stand at their natural sites (O152 stage 1), the river below the crossing is the border with Urvania on its south bank (option A, O152), the land is resized to D19 and the routes are laid over the terrain (O152 stage 3), and the sea crossing is measured here. The decided distances of O152 ("the map is leading") are those of section 3.1.

## 6. Gaps and doubts for the owner

Found by the generator (each from the data above):

- Ferrano Rail Cargo (14-xu) lies outside Serravona's built-up area (7.0 km from the centre; the town is about 1 km across).
- Fiumella Barges (15-xu) lies outside Ferrano's built-up area (14.0 km from the centre; the town is about 15 km across).
- Lumeport Airport Cargo Terminal (17-xb) lies outside Lumeport's built-up area (15.7 km from the centre; the town is about 12 km across).
- Island Customs Service (19-xl) lies outside Selanu's built-up area (7.0 km from the centre; the town is about 4 km across).
- Coastal State Water Company (34-xb) lies outside Lumeport's built-up area (14.4 km from the centre; the town is about 12 km across).
- Selanu Telecom (35-xl) lies outside Selanu's built-up area (21.3 km from the centre; the town is about 4 km across).
- Brackenmere Furniture (37-xb) lies outside Marrowdale's built-up area (7.8 km from the centre; the town is about 5 km across).
- Rivermouth Packaging (41-xb) lies outside Lumeport's built-up area (17.8 km from the centre; the town is about 12 km across).
- Kelpstone Gas (42-xb) lies outside Gullhaven's built-up area (10.5 km from the centre; the town is about 1 km across).
- Montebrio Power (43-xu) lies outside Serravona's built-up area (17.8 km from the centre; the town is about 1 km across).
- Ferrano Grid (44-xu) lies outside Ferrano's built-up area (22.4 km from the centre; the town is about 15 km across).
- Customs Administration of Urvania (19-xu) stands 3.5 km from where the road `road` crosses the border (97/120).
- Customs and Border Service of Bayvarra (19-xb) stands 0.0 km from where the road `road` crosses the border (97/120).
- Gullhaven (Kelpstone Gas) is reached by road only from Larkmouth (`road-north`): Ferrano – Gullhaven is 714 km by road against 270 km in a straight line. The lpg flow (D48, a road tanker from the gas plant) needs this settled.
- Ferrano – Marrowdale: the decided figure is the route `road` centre to centre, 192.0 km; the road flow's truck leg from Castrano Logistics to Lumeway is 174.3 km on the map. The waybill and the freight invoice state the leg's 174 km, the kilometres driven (owner, 2026-11-18, O152).

