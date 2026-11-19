# The UBL example world

This section describes the world as decided on 18 November 2026. The
examples are being brought into line with it, and until that work is done
some of them still differ from what is written here; where they do,
`analysis/worklist.md` and `analysis/worklist-decisions.md` say what is to be
done.

All examples take place in one fictional world. It is built in layers.
Each layer adds one kind of data, is kept in its own file, and is checked
before the next layer builds on it.

| Layer | File | What it holds |
|---|---|---|
| Countries | `world/countries.json` | names, currencies, tax schemes, identifier and address schemes |
| Parties | `world/parties.json` | the organisations: place on the map, role, identity |
| Map | `world/map.json` | routes, towns and localities |
| Documents | `world/documents.json` | the flows of documents between the parties |
| Items | `world/items.json` | what the parties sell: goods and services, with prices |
| UBL model | `world/ubl-model.json` | extracted from the UBL 2.5 semantic model |
| Code lists | `world/codelists/` | the world's code lists, and which code element uses which |
| Specifications | `world/specifications.json` | the transactions, national and community specifications and process profiles the documents claim |
| UBL versions | `world/ubl-versions.json` | the first UBL 2 version of each element, from the published models of UBL 2.0 to 2.5 |

## Countries

The world has three countries: Urvania, Bayvarra and Lisavu, whose
initials spell UBL. Two share a land border on the mainland; the third is
an island overseas. They differ on purpose, so that the
examples show how UBL carries different national arrangements in the same
structure:

- **Urvania (XU)** has a value added tax in the style of the EU VAT:
  charged at every stage, deducted by businesses, not charged on exports.
- **Bayvarra (XB)** is a federal country whose states levy a retail sales
  tax, charged once, on the sale to the final consumer. Sales for resale,
  exports and sales to public bodies are exempt.
- **Lisavu (XL)** has no general sales tax. Customs collects an import
  consumption tax on every import when goods enter the island, and a
  customs duty on goods from outside the Trade Accord.

The tax schemes are identified with UN/EDIFACT 5153 codes: `VAT`, `STT`
(state or provincial sales tax), `CUD` (customs duty) and `IMP` (import
tax). Because 5153 has no code for a national sales tax, Bayvarra levies
its sales tax at state level, which also gives the state in its addresses a
purpose. Bayvarra has two states and a federal territory. Upland State lies
inland, on the plateau in the west, with Marrowdale and the wheat land;
Coastal State lies along the east coast, with Lumeport and Larkmouth. The
Northern Territory, on the low north coast, is thinly populated: the fishing
village of Gullhaven, where the gas plant stands, two fishing hamlets
(Shinglebeck and Ploverness) and a few sheep stations, on land used only for
grazing. The territory levies its own rate of the same sales tax: 4 %,
against 5 % in Upland State and 6.5 % in Coastal State. Which state a place
is in follows from its place on the map.

XU, XB and XL are ISO 3166-1 user-assigned codes, which exist for exactly
this purpose; each follows the initial of its country's name. ISO 4217 has
no such range for currencies. The world's currencies follow the ISO 4217
convention of the country code plus the initial of the currency's name:
the ferra of Urvania (`XUF`), the lume of Bayvarra (`XBL`) and the coral of
Lisavu (`XLC`). The convention limits the names: ISO 4217 already uses
`XUA` and `XBA` to `XBD`, so Urvania's currency cannot start with an A and
Bayvarra's not with A to D. Each code is checked against the current
ISO 4217 list, so that none is a real code.

The three currencies also differ in their minor unit, because currencies
do: the ferra has none (amounts are whole ferra, as with the Japanese yen),
the lume has two decimals, and the coral three (as with the Bahraini or
Kuwaiti dinar). An example that only ever shows two decimals hides a case
that software must handle. Neither the countries nor
the currencies are in the UBL default code lists. UBL lets trading partners
use their own code lists in the second phase of validation, so the world
has its own: copies of the UBL 2.5 default lists, unchanged, with the
world's codes added and their own identification.

The land border between Urvania and Bayvarra has two parts. From the border
crossing, where the largest river of the plateau joins the main river, it
follows the main river down to the sea, and then the middle line of the
estuary: all land south of the river is Urvania. North of the crossing it
follows the watershed, so that Urvania keeps the whole valley of that
plateau river. The boundary convention of about 1857 drew it so (see
"History"). The sawmill stands in Marrowdale, in Upland State, and buys its
logs from the Upland State Forest, a managed forest on the slope where the
upland falls towards the town, about 50 km north of the river.

Each country also has an address format (`address` in `world/countries.json`),
which fixes the lines of an address: first the optional lines (attention,
department, in-house mail, post box, building, floor and room), then the
street and number (street first in Urvania, number first in Bayvarra and on
the island), additional street, block and plot, quarter, and last the town
line (postal code before the town in Urvania; the town, state and postal code
in Bayvarra), with the province in Urvania and the district and a
description of the way on the island. The province is a subdivision of the
country, like a Bayvarran state, so it is written in `CountrySubentity`;
UBL's `Region` names an informal area or a group of countries, which no
address of the world has. Where a delivery goes to a gate or a dock, that is
a delivery location with its own identifier, not part of the postal address. A field the address does not have is
left out with its line. A name in two languages is written on its line in
both, the national language first, then ` / `, then English, and the number
once: `<Urvanian street> / <English street> 12` in Urvania, `35 <Lisavan
street> / <English street>` on the island. Every address that has a street, a
building number or a post box carries the code of its country's format in
`AddressFormatCode`, and where a party writes its address in
`AddressLine` elements, one function makes the lines from the structured
fields, so they cannot disagree. The build checks all three. A farm on the
island has no house number: its track is described instead ("at kilometre 4").

Urvania's energy market is unbundled, as the EU's is: a gas-fired power
station produces electricity, a grid operator runs the electricity and gas
networks and reads the meters, and a retail company buys the energy and
bills the customers. The gas comes from an offshore field off Bayvarra's
north coast and crosses the border by pipeline. The Trade Accord's energy
protocol of 2007 asks for less than that: a network is run with its own
accounts and its own management and is open to others on equal terms;
whether it becomes a company of its own is each country's choice, and an
isolated system is exempt. Urvania chose the full split in 2007. Bayvarra
keeps one energy company with a separately run network division, and the
island, connected to no one, has one company that does everything, so the
three countries show three arrangements.

The supply of electricity, gas, water and telephone to end customers is a
national matter under the Accord: each country keeps its own utilities,
public or under national licence, and no utility of one country supplies end
customers in another. Ferrano Energy serves Urvania, the Coastal State Water
Company Bayvarra's Coastal State, and Selanu Telecom the island. What crosses
the border is wholesale energy: the energy protocol opened the trade in gas
and electricity between producers, networks and suppliers, and since 2011
Kelpstone Gas of Bayvarra sells gas by pipeline to Urvania's power station
and to Ferrano Energy. Because the customers of a protected supplier cannot
go elsewhere, the three countries agreed minimum rules for utility bills;
one of them is the period to pay (see "Money and payment").

## History

Before the Europeans came, the Urvanians farmed the wet valley of the main
river and the hills to the west of it. Their town, Ruldraz, grew where the
valleys meet and where the river stops being navigable, below the rapids.
It is the town the Italians later called Ferrano, and its old town still
carries the Urvanian name.

The first Europeans to reach it came from Tuscany. In reality, Grand Duke
Ferdinando I of Tuscany sent the Thornton expedition from Livorno to Guiana
and the Amazon in 1608–09, the only official attempt of an Italian state
before unification at a colony overseas; a second voyage, with settlers from
Livorno and Lucca, was cancelled when the Grand Duke died in 1609. In the
world that second voyage sailed, in 1609–10, and reached Ruldraz. This is
invented. A small Tuscan trading post lasted some decades and faded in the
18th century. It left Ferrano's quarter Borgo Toscano and the chapel of San
Ranieri del Guado, by an old ford of the upper river.

In the 1820s British settlers landed at Larkmouth, at the mouth of the
largest river of the east coast: a sheltered harbour, with fresh water and
dry grassland behind it. They spread over the dry east and the plateau as
graziers and wheat farmers. Larkmouth was their first town and first
capital, and Bayvarra keeps the landing as Settlers' Day. The settlers held
the coast through their own company, without the Crown: Britain's Colonial
Office avoided new colonies in those years for what they cost. In the late
1830s the company kept a small trading station at the narrows of the
estuary, on the shore of the bay, where a brook gave fresh water; the
narrows command the entry to the river.

About 1840 the Sardinian corvette *Euridice* came from Sardinia's naval
station on the Río de la Plata. Because the station was the company's and the
Crown had no sovereignty over the river, the warship of a friendly kingdom
could sail past the station up the river to Ruldraz. The Urvanian rulers signed a
treaty of protection with Sardinia, which revived the old Tuscan claim, and
Forte Euridice was built about 1842 in the angle of the main river and the
largest river of the plateau. The station on the Plata and the corvette are
real: Sardinia kept a naval station and a consulate general there from 1837,
with some ten thousand subjects, most of them Ligurians, and the *Euridice*
was stationed there in 1836–38 before it sailed up the Amazon. Its voyage to
the world is invented; Italy's first real possession was Assab on the Red
Sea, bought by the Rubattino shipping company in 1869 and taken over by the
state in 1882. Ligurian fishermen from the Plata settled under the
protectorate at Marina Ligure on the south coast.

The treaty made Britain act. It annexed the coast and the dry east, as
cheaply as it could, fortified the station at the narrows and laid out the
town of Lumeport there, about 1841, as the colony's seat; as the river trade
grew it became the capital in Larkmouth's place. Britain did not take the valley: Sardinia protected it, it was
densely peopled and would have been costly to conquer, and the settlers
wanted the grazing land, not the valley. A real parallel is New Zealand, which Britain annexed in
1840 only under pressure, among it the fear of a French settlement at
Akaroa, and where it then let the French settlers keep their settlement.
Sardinia fought beside Britain and France in the Crimean War (1855) and sat
at the Congress of Paris (1856). A boundary convention of about 1857 then set
the border along the main river below the confluence and along the watershed
north of it, with free navigation of the river to the sea, the principle the
Final Act of the Congress of Vienna laid down for international rivers in
1815 and the Berlin Act extended in 1885. The crossing has been known by the
fort ever since. In 1861 the Kingdom of Italy inherited the protectorate,
and Urvania stayed an Italian territory until 1941.

In the late 19th century Bayvarra built its railway, and villages grew at its
stations. On Lisavu, English settlers laid out cotton estates in the 19th
century on the dry north-eastern plain, at Lintwell and Bollworth, and named
the island's capital Port Wrenfield. In 1941, in the Second World War,
British forces took Urvania and put it under British administration, which
stayed after Italy renounced its colonies in the peace treaty of 1947. (In
the real treaty, article 23 renounces Italy's possessions in Africa; in the
world the renunciation also covers Urvania.) The British kept the Italian
place and street names, and Urvania kept a continental cast in its
institutions, among them its value added tax and its Italian-style bank
codes. It became independent in 1962, bilingual in Urvanian and English, and
built a protected economy around state mining, state energy and its own
manufacturers: Ferrano Energy dates from 1949, Serravona Mining from 1958,
and Valdara Industries, the bench maker, was founded in the year of
independence. Bayvarra's settler economy is older than Urvania's state; the
Bank of Lumeport was founded in 1903. The exact dates of the first landing,
the treaty and the boundary convention are not yet settled, and neither is
when the island was first settled or how Bayvarra and the island became
independent.

In 1974 Bayvarra and Lisavu signed the **Lumeport Agreement**. The island's
cotton entered Bayvarra free of duty, a regular shipping service linked the
two, and the island's coral was tied to the lume. The island kept its duties
on imports. Tidewell Ocean Lines was founded that year to run the service,
and the agreement called other companies into being: the Port of Selanu was
formed as a company ahead of it, a customs broker on the island followed in
1975, and in 1976 a Bayvarran forwarder and the Lumeport Textile Mill,
built to spin the island's duty-free cotton.

Urvania opened its economy in the early 1990s, as several real countries did
in those years. In 1994 it joined the two others in the **Lumeport Trade
Accord**, signed in Lumeport, which turned the agreement of 1974 into a free
trade area of all three countries; the Accord takes its name from it. The
Accord entered into force on 1 January 1996. The ferra joined the lume and
the coral at a fixed parity. The island stopped charging duty on its
partners' goods and kept its import consumption tax, which falls on every
import whatever its origin: it is the island's substitute for a sales tax,
and the reason it could afford to join. Lumeway Distribution became Valdara's
distributor for Bayvarra and the island in that year, under a distribution
agreement, which is why Valdara's benches reach the island through Lumeport.
Hauliers, forwarders, customs brokers, a factoring company, a border terminal
and Urvania's numbering agency were set up around that time to serve the new
cross-border trade.

Later protocols of the Accord followed. The energy protocol of 2007 opened
the wholesale trade in gas and electricity and asked for networks to be run
apart from supply, while the supply to end customers stayed national;
Urvania's Ferrano Grid was split off that year. In 2011 Kelpstone Gas began
producing from its offshore field and the pipeline brought gas to Urvania;
Ferrano Energy and Ferrano Grid, electricity companies until then, took up
gas as a second business. Further protocols gave the three countries common
procurement rules, the payment link and card schemes, and electronic
business documents, which is why they share these and the code lists
although each keeps its own taxes; their dates are not yet settled. The
Accord also keeps public services national: it leaves the supply of
electricity, gas, water and telephone to end customers to each country and
sets a common minimum for the customers of those utilities.

The companies' founding years follow this history: the old trades before
1962 (the river barges, marine insurance, the island's cotton ginnery, the
water company); the companies the agreement of 1974 called for; and the
Accord's wave from 1996 to 1999 (the haulier, the factoring company, the
border terminal, Valdara's logistics arm, the numbering agency, island
warehousing). Each party has its own founding date, headcount and turnover,
from which its size class follows. The table of founding years and figures
in `analysis/worklist-decisions.md` is a current base, open to correction;
each party's day and month of founding are in `world/parties.json`.

## Geography

The mainland is a land of about 550 by 411 km and about 159,000 km² in the
middle of the South Atlantic, astride the Mid-Atlantic Ridge, far from every
continent. Urvania holds the west and all the land south of the main river,
about 90,500 km², about the size of Portugal; Bayvarra most of the plateau,
the dry east and the north coast, about 70,100 km². Lumeport stands on the east
coast, on a bay at the mouth of the estuary. Lisavu is an isolated volcanic
island about 1,080 km east of Lumeport, about 116 by 85 km and
7,100 km², smaller than Cyprus, standing on a seamount of the Walvis Ridge.

The position is a current base: the mainland centred on 30.0° South, 15.0°
West, from about 28.2° to 31.8° South and from 17.9° to 12.0° West (Ferrano at
about 30.7° South, 15.5° West; Lumeport at about 31.0° South, 13.3° West), and
the island around 33.0° South, 2.65° West, with Selanu at about 2.2° West
(`geography` in `world/countries.json`). Both lie
on the high seas, outside every country's waters and claims; the nearest real
land is Tristan da Cunha, about 600 km south of the mainland's south coast. It
is still to be confirmed against a nautical chart that both areas lie outside
the 200-nautical-mile zones of the nearest islands and that no extended-shelf
claim or sea-bed licence reaches them. The mainland lies at the latitude of
southern Brazil and South Africa, and the island, at 33° South, is warm
enough for cotton.

The land is made from its geology (`tools/terrain.py` makes
`world/terrain.json` from `world/terrain-inputs.json`): a volcanic massif in
Urvania's north-west, which reaches about 1,920 m, and a rift valley 15 to
18 km wide, where the Mid-Atlantic Ridge runs under the land. The main river
rises on the massif at about 1,510 m and runs 470 km through the rift valley
to the sea. It is the trunk of one large basin of about 53,000 km², a third
of the mainland, and the larger branch at every confluence; its tributaries
come from the massif, the plateau and the southern hills. Just above Ferrano
it falls through rapids, from about 124 to 91 m in about 12 km, which end
navigation: the barges work below them. From the border crossing the river
forms the border, and some 45 km above Lumeport it becomes a drowned estuary,
which narrows at Lumeport before it opens into the bay. Urvania's western
hills and the land south of the river are green and hilly, wet from the
westerly winds; east of them the plateau of Upland State falls to the dry
east of Coastal State, grazing and wheat land, and the north coast is low.

From the mainland the first sight of the island is its west coast: cliffs of
about 115 to 435 m, with two bays where the land has slid into the sea,
stacks and islets, and flats of landslide debris at their foot. That side
faces the prevailing westerly wind and the ocean swell and has no port. The
island is an eroded volcano, which rises to about 1,810 m some 25 km inland
from the west coast and falls to the east. Ships round a cape to the lee
side, where the port and the town of Selanu lie on a sheltered bay of the
east coast, the airport on the plain about 10 km to the north, and the cotton
on a plain of about 690 km² in the dry north-east, in the island's rain
shadow: the high ground on the windward side catches the rain, and the lee
side is drier and sunnier. An island cut off like this has to work for its
ties, which is the story of the Lumeport Agreement and of the shipping line
founded to serve it.

The countries have about 2.1 million people: Urvania about 1.2 million,
Bayvarra about 800,000 and Lisavu about 60,000. Each capital holds about half
its country's people. The towns:

| Town | Country | What it is | People | Built-up area |
|---|---|---|---|---|
| Ferrano (*Ruldraz*) | Urvania | the capital; works, rail hub, river port below the rapids | about 600,000 | about 15 km across |
| Lumeport | Bayvarra, Coastal State | the capital and the port city, at the estuary's narrows | about 400,000 | about 12 km |
| Larkmouth | Bayvarra, Coastal State | the first landing and first capital; a wool and meat port at the mouth of the east river | about 80,000 | about 6 km |
| Marrowdale | Bayvarra, Upland State | inland town: distributor, sawmill, furniture maker, works | about 40,000 | about 5 km |
| Selanu (Port Wrenfield) | Lisavu | the island's capital and only town | about 30,000 | about 4 km |
| Serravona, Gullhaven | Urvania, Bayvarra | villages: the mining village, the fishing village by the gas plant | 1,000 to 3,000 | about 1 km |

Urvania also has seven country towns of 14,000 to 28,000 people, among them
Portaggio at the head of the rapids, Fierabruna, the old cattle fair where
two plateau rivers meet, Lanternino on a bay of the south coast, and Forte
Euridice by the border. Bayvarra has ten railway and coast towns of 5,000 to
12,000, such as Tallowford, a ford market on a plateau river, and
Brackenmere and Saltmere, which gave their names to Marrowdale firms. Lisavu's villages have at most 2,500 people each. Besides them there
are about 430 villages and hamlets in Urvania, 160 in Bayvarra and 17 on the
island, and scattered farms. Each lies where it has a reason to be (a ford
or bridge, a confluence, a spring, a harbour, a crossroads, a mine), and its
farmland follows the soil, the slope and the rain, not a ring round the
village. Each town has quarters by period: in Ferrano the Urvanian old town,
Borgo Toscano, the Italian quarters, the British-era suburb and the growth
since independence; in Lumeport the settlers' Old Town, Government Hill and
the docks of the colonial years and the suburbs after them.

Roads, railways and pipelines are laid over the land as a builder would lay
them: main roads climb at most 7 %, minor roads 10 % and railways 2 %, and
they follow the contours and cross few rivers. The largest bridges are
Ferrano's road bridge, about 106 m above the river, the ore line's river
bridge, 78 m high, and a viaduct over a side valley; no tunnel was worth its
cost. The railways are the ore line from the mine down to Valdara's works at
Ferrano, the line from Ferrano across the border to Lumeway's siding at
Marrowdale, a line to the Port of Lumeport, and the wool line from Marrowdale
down to Larkmouth's harbour. No main road runs south of the main river: the farmland there is served by
minor roads, which reach the rest of the country over Ferrano's bridge.

Urvania separated its rail infrastructure from its train operators, as it
separated its electricity grid from supply. A public body, the Rail
Infrastructure Agency of Urvania, owns and maintains the tracks, allocates
the train paths and runs the traffic control that dispatches every train,
up to the border station; Ferrano Rail Cargo runs its trains on the paths
it is given, and the intermodal hub at Ferrano only loads and unloads them.
The European Union went part of that way: Directive 91/440/EEC required
separate accounts and left the organisational separation optional, and an
infrastructure manager must be a legally distinct body only since Directive
2012/34/EU as amended by Directive (EU) 2016/2370; full separation, as in
Urvania, is one model a state may choose. Carriage by rail between the
Accord's members follows the Accord's uniform rules for international
carriage by rail, modelled on the CIM (COTIF Appendix B). Like the CIM they
also cover a carriage by road within one member state that supplements the
rail carriage under the same contract, so the rail carrier's haulage of a
container to the hub is a stage of the rail contract.

Some places of the examples:

- **The mine.** Serravona Mining works an underground mine on the massif's
  lower flank: an adit in the hillside at about 720 m, 29 km from Serravona,
  with its address in the village of Fucinalta, a small crushing and
  screening plant and a spoil heap; the hillside around it stays green. The ore line is laid
  up to the portal, where the wagons are loaded and weighed at Fucinalta mine
  siding.
- **The forest.** The Upland State Forest, about 345 km² of compartments
  planted and felled by age, lies on the slope north of Marrowdale, between
  about 300 and 550 m, and supplies the sawmill in Marrowdale.
- **Lumeport's brook** rises in the low hills west of the centre and runs
  through the town to the bay; it gave the town its first fresh water.
- **The river quay.** Rinova Recovery stands on the river at Ferrano with a
  quay of its own, where the barge loads. The barge sails below the rapids,
  about 250 km down the river and the estuary to Lumeport, without locks.
- **The crossing.** The road crosses the border at Valico Euridice
  (*Menbaz*) on the Urvanian side and Euridice Crossing on the Bayvarran
  side, with their customs posts facing each other, named after Forte
  Euridice, 8 km down the road.
- **The gas.** The offshore platform stands about 80 km out from the gas
  plant at Gullhaven.

One square of the map is 3.5 km. The map is leading: a distance is the
length of the route laid on the map, and every distance and time a document
states comes from it, as listed in the place list (`analysis/place-list.md`,
made by `tools/place_list.py`). By road Ferrano to Marrowdale is about
192 km and Marrowdale to Lumeport about 81 km; the ore line runs about
166 km; the gas pipeline runs about 207 km from the gas plant to the power
station, its branch to the grid's city gate about 97 km, and the subsea line
from the platform about 83 km. A document states the kilometres driven on its
own leg, from party to party. Lumeport to Selanu is about 1,080 km in a
straight line. By sea, out through the estuary and the bay and round the
island's south-eastern cape, it is about 1,200 km, which the ship sails in
about 48 hours at 13.5 knots. The island airline's freighter flies about
1,080 km between the airports, about 2½ hours from gate to gate in still air;
its timetable allows 2 h 45 eastbound and 3 h 00 westbound, a margin for
delays.

The printed map is an A3 landscape sheet at 1 : 2,500,000, with clear sea
around the mainland. Lisavu stands beside it in a panel of its own, at the
same scale: two panels in one frame, with a gutter between them and each
with its own header and border, and a note that the island lies about
1,100 km east of Lumeport. The island is drawn nearer than it lies; the
coordinates in the documents are its true position.

## Languages

The countries speak differently. Bayvarra speaks English, the working
language between the three countries. Urvania was an Italian territory and
then under British rule; the British kept the Italian place and street
names, while the people kept their own Urvanian names for the same places.
Independent since 1962, Urvania is bilingual, Urvanian and English, and the
inherited Italian names count as English: Ferrano is also *Ruldraz*, the
older name of the Urvanians' town, and an address gives both, as in
Brussels. The country towns have Italian and Urvanian names alike:
Portaggio is *Trenzir*, Fierabruna *Hihek* and Forte Euridice *Girkul*. At
the border crossing the Urvanian side is Valico Euridice, in Urvanian
*Menbaz*, and the Bayvarran side Euridice Crossing. Bayvarra's places carry
the English names its settlers gave them (Larkmouth, Marrowdale,
Tallowford). The island is officially bilingual, as
many Pacific islands are, in Lisavan and English, Lisavan having a
Polynesian sound like the island's names. Both languages are invented, and
their codes come from the range ISO 639 reserves for local use, `qaa` to
`qtz`: `qau` for Urvanian and `qal` for Lisavan. A document between the
countries, whose sender and receiver are in different countries, is in
English, the working language of the Trade Accord. A sender from Urvania or
the island gives the notes of its domestic documents in its own language and
in English, each with its `languageID`, and those across a border in English
only. A seller there names and describes its items in both
(its name, description, warranty and what comes with it); a seller in
Bayvarra does so in English only. Both countries
name their streets and towns in both official languages, as Brussels and Canada do: UBL 2.5
lets an address repeat its street, city and state names, one per
language. The island's capital keeps its Lisavan name as the primary one,
and has the English name its English-speaking settlers gave it: Selanu is
also *Port Wrenfield*, a name checked not to be a real place. Most of the
island's villages have Lisavan names only (Felulaka, Natahoma, Setahu); the
villages of the 19th-century cotton estates have English names with Lisavan
ones beside them: Lintwell (*Kefalasa*) and Bollworth (*Pakesa*).
The texts in the invented languages are made word by word from a fixed
vocabulary, the English text being the reference. Real Polynesian languages
are deliberately not used, and the invented words are checked against
common words of real languages.

English is not one language across the three countries. Each country's
English was shaped by its history and by the language spoken there before,
and has drifted from standard English. **Urvanian English** carries the
Italian place and street names the British kept, and stands beside
Urvanian; **Bayvarran English** is the settlers' English and the working
language between the three countries; **Lisavan English** stands beside
Lisavan on the island and uses the Lisavan names for places. The three
varieties are written `en-XU`, `en-XB` and `en-XL`. A party states the
language of the exchange. In English it says which English it writes, in
`LocaleCode`, from the world's list of locales, while `Language/ID` stays
the plain language `en`. Only English has a locale, because it is the one
language used in all three countries; Urvanian and Lisavan are each used in
one country, and their plain codes say all. So an Urvanian company states
`qau` at home and `en` with `en-XU` in a document to Bayvarra or the
island.

A text keeps the English it was written in when it travels. A party's
address, legal form and other master data are written by that party or its
country's register and carry that party's variety in every document: a
Bayvarran clerk copies an Urvanian address as it stands in Urvania's address
register and does not translate it, so one address reads the same in every
document of the world. Free text written for a document, such as a note or a
description, carries the issuer's variety. One document can therefore hold
two Englishes side by side: the buyer's note in Bayvarran English and the
seller's address in Urvanian English. Whether and by whom an item's name and
description are localised for the market it is sold in is not yet settled.

Port Wrenfield is still the official English name of the island's capital
and stands in every address, the Lisavan name first, but it is fading from
use: in speech and in writing, also in English, the town is Selanu, whoever
writes. Proper names such as the port's and the bank's keep "Selanu", and
the name lives on in the port quarter, Port Wrenfield. Using
the Lisavan names for places is a trait of Lisavan English, as the Italian
names are of Urvanian English. Urvania works the other way round: English
text uses the inherited Italian name (Ferrano, Serravona) and Urvanian text
the Urvanian one (Ruldraz, Drinzul).

## Code lists

Every code in the examples comes from a code list, and every code element
names its list in `listID`. The lists are made from one source,
`world/codelists/lists.json`, as genericode files, together with the world's
context/value associations, which say which list each element uses. Where a
standard has a list for a concept, the world uses it; otherwise the Lumeport
Trade Accord, the treaty between the three countries, has a regional list.
A few lists are national, because the countries differ: legal forms, tax
exemption reasons, Bayvarra's states and Urvania's customs tariff.

- **Lists of standards** are used where UBL uses them (its default lists),
  where practice uses them (EN 16931 uses UN/EDIFACT 1001, 5189 and 7161),
  or where a standard is the authority for its domain: the IMO for
  emergency schedules and security levels, the WCO for the Harmonized
  System, the UN for product classification (CPC) and dangerous goods,
  ISO 20022 for payments, EPSG for coordinates, PRONOM for file formats,
  UN/ECE Recommendation 28 for means of transport and, as it refers air
  transport there, IATA's aircraft type codes.
  UBL is not "EDIFACT in XML", so a UN/EDIFACT list is not used just because
  it exists. Each is a world copy of the codes the world uses, with others of
  the same list, made from the copy of the source kept in
  `world/codelists/sources`; its `listID` is in UBL's text style, such as
  `UN/EDIFACT EDED 1001` or `WCO HS 2022`. No code of such a list is invented.
- **Regional and national lists** have short upper-case codes and a name in
  English, Urvanian and Lisavan; their `listID` is a URN such as
  `urn:ubl-examples:world:codelist:AddressTypeCode` or
  `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`.
- **One list per concept.** Elements that only qualify one concept share its
  list, as `PreviousMeterReadingMethodCode` and `LatestMeterReadingMethodCode`
  do. An element used for several things, such as `TypeCode`, gets one list
  per meaning, chosen by its parent element.
- **No filler.** A code says something the receiver needs. Where "none"
  matters, it is a defined code, such as UN/EDIFACT 8339 code 4 "Not
  assigned" for goods without a packing group.

Some choices differ from common practice, on purpose:

- **Allowances and charges.** An allowance takes its reason from
  UN/EDIFACT 5189 and a charge from 7161, as in EN 16931. Where 7161 has no
  code, the world uses 5189 for a charge too, with that list's `listID`
  (96 insurance, 48 interest on arrears), which EN 16931 does not allow.
  UBL's own default list for this element is labelled 5189 but holds the
  codes of UN/EDIFACT 4465, so the world replaces it.
- **Languages.** Language codes are written in lower case, as ISO 639 and
  BCP 47 recommend; UBL's copy of the list is in upper case and merges the
  two alpha-3 codes of a language into one value. The world's list follows
  the ISO 639-2 registration authority and adds `qau` and `qal`. An English
  text is tagged with the English it was written in, `en-XU`, `en-XB` or
  `en-XL`, which BCP 47 allows for private use: a party's master data with
  that party's country, free text with the issuer's (see "Languages").
- **Invoice periods.** `InvoicePeriod/DescriptionCode` describes the
  period (a month), as UBL defines it, not the tax point date code that
  EN 16931 puts there.
- **Document distribution.** `DocumentDistribution/DocumentTypeCode`
  gives the type of the distributed document (a bill of lading), and
  `DistributionTypeCode` how the party receives it, original or copy: an
  original by courier, a scanned copy, the electronic document itself.
  UBL 2.5 deprecated the elements that said this before (`CopyIndicator`,
  `MaximumCopiesNumeric`, `MaximumOriginalsNumeric`, `PrintQualifier`),
  and an original is not a type of document.
- **Self-billing.** Where the customer bills itself, as the cotton gin
  does for the farms' seed cotton, the world uses UBL's own
  `SelfBilledInvoice` and `SelfBilledCreditNote`, never an `Invoice` with
  type code 389 as EN 16931 and Peppol BIS do (their syntax binding has
  only Invoice and CreditNote). UBL 2.5 defines Invoice as "A document used
  to request payment" and SelfBilledInvoice as "An Invoice document created
  by the Customer (rather than the Supplier) in a Self Billing
  relationship"; its semantic definitions (§4.7) are what a document must
  conform to (§7.2). The type codes are UN/EDIFACT 1001 389 and 261: they
  repeat the root element, but their definitions are exact ("An invoice the
  invoicee is producing instead of the seller"), while 380 is a document
  "claiming payment". The gin's advance to a farm before the harvest is a
  self-billed prepayment invoice, type 386, which the final self-billed
  invoice deducts as its prepaid amount.
- **Procurement.** The Accord's procurement rules are modelled on the EU's,
  without being EU law: its lists give the matching eForms or ESPD code.
- **Customs.** The Accord is a free trade area, not a customs union: it has
  one customs data model with common procedures and statuses, while tariffs
  and the valuation of imports stay national. A procedure code is the
  requested procedure followed by the previous one, numbered differently
  from the EU's, so release for free circulation is `1000`.

## Identifiers

An identifier that comes from a scheme names it in `schemeID`; one that only
its sender assigns, such as a document number or a line number, does not.
The world's own schemes have lowercase URNs, as its first ones had
(`urn:ubl-examples:world:XB:register`, `urn:ubl-examples:world:endpoint`),
and a country's scheme carries its code (`urn:ubl-examples:world:XU:tax`,
`urn:ubl-examples:world:XB:vehicle-register`). Real schemes keep the name
their standard gives them, in the text style of UBL's `listID`s: `ISO 11649`
for the creditor references, `ISO 6166` for the securities, `ISO6346` for the
containers. Each scheme has its format in `world/countries.json`, with its
check digit where it has one, and the build checks every identifier against
it, as it checks the telephone numbers. A `schemeID` has no fixed format; the
examples show two.

Every register issues its own numbers. A company's business register number,
its tax number, its Codana number or GS1 company prefix and its other
numbers are each issued by a different body, in that body's own series, and
none is derived from another. Each scheme has a shape of its own, so that a
value shows which scheme it belongs to, and no value of one scheme repeats
the digits of a value of another. There are two stated exceptions. An
electronic address is always an identifier the party already has, under a
scheme code, never a new number: the network addresses a company by its
business register number, as Peppol addresses a company by a number it
already has. And customs registers a trader under its business register
number, as the EU's EORI number is built from a national number. The build
checks that no identifier of a party repeats the digits of another, apart
from these two. An identifier is opaque: what a thing is and who issued its
number is said by the elements around it, not read from the number.

Companies are entered in their country's register of businesses, and a
document shows that entry: the register, its type, the company's status and
its size class. Public bodies are not: customs services, chambers of
commerce, the Trade Accord Council, the review board, the public works
department, Codana and the other agencies are set up by law, so they carry no
commercial register entry, no liquidation status and no size class. The
ports and the island's telecom operator are companies owned by the state and
are in the register like any company. A farmer on the island is entered in
Lisavu's farm register, which renews a grower's registration each season.

Instead, each country keeps a register of its public bodies, on the model of
Italy's IPA code, and the register gives each body a number of its own
shape, derived from no other register:

| Register | Kept by | A number | Scheme |
|---|---|---|---|
| Index of Public Administrations of Urvania | the Agency for Digital Administration | `xu_` and four lower-case letters or digits (`xu_k4r7`, the customs administration) | `XU:public-body-register` |
| Federal list of public bodies of Bayvarra | the Bayvarra Information Service | ten digits, the first not 0 (`3071845926`, the customs and border service) | `XB:public-body-register` |
| Government list of public bodies of Lisavu | the Government Secretariat | `GOV-` and three digits (`GOV-118`, the customs service) | `XL:public-body-register` |
| Farm register of Lisavu | the Department of Agriculture of Lisavu (`GOV-206`), whose Plant Protection Service also issues the island's phytosanitary certificates | `LFR-` and four digits (`LFR-0412`, the cotton farm) | `XL:farm-register` |

The Trade Accord Council, an international body seated in Lumeport, is in
Bayvarra's federal list under its seat agreement with Bayvarra, so that it can
deal with Bayvarran bodies, banks and the exchange network.

A public body's party identifier and the `CompanyID` of its legal entity
carry that number under its register's scheme (`urn:ubl-examples:world:` and
the scheme), and its electronic address is built from it, as a company's is
from its business register number; the farm's likewise from its number in the
farm register. Bayvarra's customs build a trader number from the last six
digits of the trader's number in its register: a company's business register
number, a public body's number in the federal list (`XB-TR-397184` for the
Lumeport Public Works Department). No real code of Italy's index starts with `xu_`. The
build checks that each public body carries a number of its country's
register in that register's shape, that no company carries a number in a
public body's shape and no public body one in a company register's, and that
the number repeats the digits of none of the party's other identifiers.

A code held in an identifier element, such as the tax category in
`TaxCategory/ID`, the language in `Language/ID`, the hazard class or the
Incoterms rule in `DeliveryTerms/ID`, names its code list in `schemeID`, with
the list's `listID` (`UN/EDIFACT EDED 5305`, `ISO 639`), and the world's code
list validation checks it like any code. What a dimension or a temperature is
(`AttributeID`) is a code too, from three lists of the Trade Accord: one for
dimensions (`LENGTH`, `SEATHEIGHT` …), each mapped to the UN/EDIFACT 6313
measured attribute in its description, one for temperatures (`STORAGE`,
`PRODUCT`, `AMBIENT` …) and one for the rest (`COLOUR`, `PALLETPLACES`,
`TEU` …).

Vehicles are registered nationally: plates, aircraft and railway wagons each
have a national scheme. A wagon number follows the UIC's twelve digits with
its check digit. Driving licences and identity numbers carry no `schemeID`:
the element already says what they are, and the person's country says whose.
Values that would look like real ones are made visibly fictional in the right
format: the call signs and aircraft nationality marks use the series `QU`,
`QB` and `QL`, which the ITU has not allocated, the ships' MMSIs the
unallocated maritime identification digits 297, 298 and 299, and the wagons
the UIC country codes 46, 47 and 48, which no railway uses. A container
owner code is one the container register of the Bureau International des
Containers does not hold, looked up on its public site.

Certificates and licences name their issuer in one of two ways. A number
from a national register, such as Urvania's haulage licences and waste
permits, Bayvarra's forestry register or its customs' register of bonded
warehouses, names the register in `schemeID`, and with it the authority that
keeps it, so no issuer party is needed. A certificate whose number is unique
only with its issuer, such as an environmental, medical or sanitation
certificate or the X.509 certificate of an access point, has no `schemeID`
and names its issuer in `IssuerParty`. Rinova's granulate, for example, is
certified for its recycled content by Certovira Certification, an accredited
certification body in Ferrano that audits the plant every year under a
recycled-content scheme following EN 15343:2007, as industry schemes such as
RecyClass do; the certificate travels in the product information Rinova sends
its buyer, not in the order, the invoice or the customs declaration.

Payment cards follow ISO/IEC 7812 in a range real cards cannot use: the
major industry identifier 9, which is for national use, followed by the
numeric code of the issuer's country (901, 902 and 903 are user-assigned in
ISO 3166), the issuer's digits and a Luhn check digit. A chip application
starts with its card scheme's application provider identifier from the
national category `D` of ISO/IEC 7816-5 with the same country code. The
Accord has three card schemes: Lumecard, the Bayvarran banks' domestic debit
card, Coralcard on the island, and Tressa, an international credit card of
the banks of all three countries; the names were checked against the real
card networks. A till receipt shows the card number as the merchant's till
prints it, never more than the first six and the last four digits, and never
the card's security code or its dates. The department store's tills print only the last four digits;
the trading company's shop on the island prints the first six and the last
four. A webshop order is different: the card is not at hand, so the order
carries the full number, the card's dates and its security code, and the store
has the payment authorised before it reserves the goods. PCI DSS allows a
merchant to hold the security code until the authorisation, never after.

## Two identification systems

Each party identifies what it makes, ships and runs in one convention, as
real companies do, chosen by whom it trades with.

**GS1** is the system of Bayvarra's retail and distribution chain: the
distributor Lumeway Distribution, the department store Brightmarket Stores,
the furniture maker Brackenmere Furniture and the textile mill, which makes
the shirts the store sells. They use a GTIN for their
items, a GLN for themselves and their places (the distribution centre's rail
siding, the store's goods-in), an SSCC for every pallet or skid they make
up, and a GRAI for the distributor's own returnable pallets, which go back
to it after each delivery to the store. Their company prefixes start with
952, which GS1 reserves for demonstrations and examples. The prefixes are
licensed by GS1 Bayvarra, a not-for-profit association owned by its member
companies. It began around 1981 as an article numbering association, when
Brightmarket and other retailers wanted bar codes at the till, and took its
present name in 2005, when the worldwide organisation became GS1. It gives
a company a seven-digit company prefix, from which the company builds its
own GTINs, GLNs, SSCCs and GRAIs. It also serves Lisavu, which has no such
organisation of its own. It belongs to the story, not to the documents: no
document names it until one has a reason to.

**Codana**, the Codana Identification Agency, is Urvania's public numbering
body, founded in 1999 when the country opened its trade. It is an issuing
agency under ISO/IEC 15459 with the issuing agency code `KXU` (`K` is the
range for national public administrations, and XU is a user-assigned
country code, so no real agency can hold it), and it keeps the organisation
register behind the ISO/IEC 6523 code designator `0990`, which no real
scheme has. The bench maker, its warehouse, the mine, the recycler, the
packaging maker, the gas producer, the power station and the grid operator
work this way. Codana registers any company that asks, foreign ones too:
Rivermouth Packaging and Kelpstone Gas are Bayvarran, but their customers
are Valdara and the power station, so they use their customers' system.
Codana gives each company a five-digit number, in order of registration
since 1999, unrelated to the company's business register number; a large
early member has a low one:

| Company | Registered | Company number |
|---|---|---|
| Valdara Industries | November 1999 | `10014` |
| Montebrio Power | December 1999 | `10087` |
| Serravona Mining | January 2000 | `10252` |
| Castrano Logistics | March 2000 | `10519` |
| Rinova Recovery | September 2003 | `13362` |
| Rivermouth Packaging | February 2006 | `15128` |
| Ferrano Grid | January 2007 | `16043` |
| Kelpstone Gas | October 2012 | `19676` |

| | Codana | GS1 Bayvarra |
|---|---|---|
| Country | Urvania | Bayvarra (also serves Lisavu) |
| What it is | a public body, set up by the state | an association of companies |
| Founded | 1999, when Urvania opened its trade | around 1981, by retailers and distributors |
| Standard | ISO/IEC 15459 and ISO/IEC 6523 | GS1 |
| Gives a company | a five-digit company number | a seven-digit company prefix |

A company registers once with Codana, and its one number serves as its
party identifier (`0990:` and the number) and as the root of everything it
labels (`KXU` and the number). This is how the real systems work: a D&B
DUNS number is ISO/IEC 6523 code 0060 and issuing agency code `UN`, an Odette
number 0177 and `OD`, and GS1 itself is 0088 (the GLN) and the agency codes
`0` to `9`. Codana's rule book is short:

- the company prefix is `KXU` followed by the five-digit company number,
  eight characters;
- after the prefix comes the company's own reference, in upper-case letters
  and digits only, without hyphens or spaces;
- no identifier is longer than 20 characters, which ISO/IEC 15459 recommends
  for a one-line bar code;
- Codana adds no check character, as ISO/IEC 15459 itself adds none; the
  build checks instead that the prefix of every identifier is the company
  number of the party that issued it. A company may end its own reference
  with a check character if that makes its processes more robust, as
  Castrano does on its licence plates; it chooses the method (ISO/IEC 7064
  gives systems for digits and for letters and digits, such as MOD 97-10 and
  MOD 37,2), and the character stays inside its own part of the number;
- Codana does not hand out item numbers. It gives a company its number, and
  the company numbers its own items, lots, pallets and places.

What each thing looks like, for Valdara Industries, company number `10014`:

| Thing | The company's own number | Globally unique form (Codana) | GS1 side |
|---|---|---|---|
| Item (the bench) | `VI-B180` | `KXU10014B180` | GTIN |
| One serialised item (a casting) | `VI-SF-01230` | `KXU10014SF01230` | serialised GTIN |
| Production lot | `VI-LOT-260510` | `KXU10014LOT260510` | GTIN and lot |
| Transport unit (a pallet) | none | prefix and serial | SSCC |
| Returnable transport item | none | prefix, type and serial | GRAI |
| Site | none | prefix and site code | GLN |
| Company | register number | `0990:10014` | GLN |

The company's own reference in the globally unique form is its item number
without its initials and hyphens: the mine's `SM-ORE-L` is `KXU10252OREL`,
the packaging maker's `RP-SF-23` is `KXU15128SF23`. In a document the
company prefix `KXU10014` is the scope within which the company gives its
numbers.

The data identifier that a bar code puts in front of such a value (`25P`
for an item, `J` for a transport unit) is not part of the value in a UBL
document, where the element says what the value is. In a document the
company's own number stays where it is (the seller's item identification,
the serial, the lot); the globally unique form is the standard
identification, given where a document crosses company borders and the
receiver needs it. Which documents carry serials, lots, sites and returnable
items in this form is not yet settled; none is numbered without a case.

The two systems meet in the park bench. Valdara ships it under its Codana
form; Lumeway, as an importer may, gives it a GTIN from its own GS1 prefix
for the shops, as its own number, and carries the maker's number alongside;
where a document names the GTIN's issuer, it is Lumeway, not Codana. A
reseller gives no GTIN of its own to an item that already has one: the
store sells the mill's shirts under the mill's GTIN.
A pallet needs no relabelling on the way: GS1 is itself an ISO/IEC 15459
issuing agency, so Lumeway's warehouse reads Castrano's licence plates and
its own SSCCs alike. The engineering company, the sawmill, the island's
cotton farm and ginnery and the utilities use only their own numbers. A
reseller shows its own item number and the maker's. Inner packages have
local numbers without a scheme. A logistic unit has the same identifier in
every document of its flow, which the build checks.

## Parties

The parties are the organisations of the world, chosen so that every party
role in every UBL document type can be filled (see the party cover
analysis). Each party has:

- a **role**, such as manufacturer, road carrier or contracting authority;
- a **place** on the map, in a town or a locality;
- an **identity**: a name, the identifiers of its country's schemes, a
  postal address in its country's format, an electronic address, a main
  contact and the desks it works through (sales, purchasing, accounts
  receivable and payable, goods-in, dispatch, transport planning, customs,
  bids; a customs service has its export, import and transit offices, a
  chamber its certificates and carnet offices), and, where it is paid, an
  account at one of the world's banks. The role a party plays in a document
  picks the desk that speaks for it: the buyer's purchasing in an order, its
  accounts payable in an invoice, its goods-in in a receipt. The desks share
  the party's switchboard number; a small party such as the cotton farm has
  one office for everything;
- for a company, its **founding date, headcount and turnover**, from which
  its size class follows by the Trade Accord's limits, modelled on the EU
  definition of small and medium-sized enterprises and given in all three
  currencies.

Names are invented and checked against real organisations. E-mail
addresses use the reserved domain `.example` (RFC 2606), so that none can
reach a real organisation. Telephone numbers use +999, which the ITU reserves for
a future global service (ITU-T E.164), followed by the country's digit. Each
country has its own numbering plan: Urvania kept the open plan of Italian
times, with area codes of different lengths (9 or 10 digits); Bayvarra has a
British-style plan of always 10 digits; the island has short 7-digit numbers.
A telephone number has no relation to any identifier of its party. Account numbers follow the structure of ISO 13616
with its check digits, using the world's country codes, but they are not
called IBANs, because the world's countries are not registered IBAN
countries. Each country writes the bank and the branch into the account
number in its own way: Bayvarra the bank code and a British-style six-digit
sort code, Urvania the Italian-style ABI and CAB codes, the island the bank
code and a three-digit branch number. A bank is identified across the
countries by a code in the structure of ISO 9362, the BIC, with the world's
country codes (`BLUMXBLX`), which the Trade Accord's payment link gives out,
and its branch by the national code; the build checks that every account
number holds the codes of its bank and branch.

An address has a number in its country's address register where it is a
party's postal address or a delivery address: in Urvania one national
register, like the Dutch one, sixteen digits starting with the code of the
municipality; in Bayvarra a register per state, except in Lumeport, which
keeps the city's own register (`LUM-ADR-000417`); on the island the post
office's numbers of its delivery points, as the island has no postal codes.
The build checks that the register is the one of the address's state or
city.

Lisavu's farm register renews a grower's registration each season, so a
farm's register entry carries an expiry date.

### What a document says about a party

Master data is not copied from one record into every document. Each party
is the authority on its own data, and every document stands on its own: no
party relies on the other having kept an older document.

- **The sender** describes itself in full for the kind of document. In a
  trade, payment or transport document, that means its identifiers, name,
  language, address, contact and electronic address. An invoice adds the
  sender's tax registration and legal entity. A customs or cross-border
  transport document adds the customs trader number. A tender, a catalogue
  or a business presentation adds what presents the company: its legal
  details, website and industry class.
- **The receiver** is described with what the sender knows and needs. This
  may be less than the receiver says about itself, and never contradicts
  it. A buyer's order names the seller by number, name, address and
  electronic address. The seller's language comes in its order response, and
  its legal entity in its invoice. The answer completes the picture.
- **A third party** (a carrier in a despatch advice, a bank, a party
  collected for) gets what the receiver needs to recognise or reach it.

The table per kind of document is `analysis/party-profile.md`, and the
build checks it.

**Company documents.** Urvania's company law asks every company to state
its register, its number in it, its legal form and its registered office on
its invoices and business letters. An SUA also states its share capital as
paid up, as the last balance sheet shows it, as Italian law asks of
companies limited by shares (art. 2250 codice civile). Bayvarra and Lisavu
follow the EU company-law directive (2017/1132, Art. 26), under which
stating the capital is optional, and their companies leave it out. So only
an Urvanian SUA's own invoices carry its share capital.

## Items

Every party that sells has items. Goods carry what the documents along
their way need: a seller's item identifier, a standard item
identification where the party's identification system gives one (see "Two
identification systems"), its classification in the UN Central Product
Classification (CPC), its Harmonized System subheading and, in Urvania, the
national tariff code below it, the country of origin, dimensions, net and gross weight, and the packaging. Services
have a unit and a price. Units of measure and packaging types are UN/ECE
Recommendation 20 and 21 codes from the UBL default code lists. Prices are
in the seller's currency. A unit price may be finer than the currency, as
an electricity tariff of 27.3 ferra per kilowatt hour is, but every amount
to pay is rounded to the currency's minor unit.

Items connect the chains. The park bench is made with slats from the
sawmill and film from the packaging maker; the distributor resells the
bench, and its own item points to the manufacturer's, so the maker's
identifiers travel along. A component or a resold item is only possible
if the maker or reseller orders it from that seller somewhere in the flows.

An item's facts come in three layers, each known at a different moment.
The item type and its variants are known when the product is designed:
dimensions, materials, the standard colours, the warranty, the carbon
footprint, the commodity code. The lot or the single piece is known when it
is made, graded or tested: a production lot and its manufacture date, a
casting's serial and melt number, the classing grade and moisture of a
cotton lot. The transaction is known when the goods are ordered, shipped,
measured or cleared: the variant chosen, anything made to order, the
quantity and the price, the actual gross weight of a shipment, a seal
number, a meter reading, the customs value. Two rules follow:

1. A fact is stated first in the document of the moment it becomes known:
   the type in the catalogue or the product information, the lot or piece in
   the document that accompanies the goods (a despatch advice, a
   certificate, a weight statement), the transaction in its own document
   (the order, the despatch advice, the invoice, the declaration).
2. A later document repeats a fact only if its own transaction uses it.
   Otherwise it identifies the item, the lot or the earlier document, and
   the reader finds the fact there.

The rules work in both directions: a catalogue with a lot number is as wrong
as an invoice with the search keywords. Companies keep their item data in
step through catalogues, and every later document points to the item by its
identifier. A reader who follows one bench through its documents sees it
gain facts: a type in the catalogue, a variant in the order, a lot and
serial numbers when it leaves the factory, a weight and a seal on the truck,
a value at the border. A catalogue line adds the seller's terms (lead time,
minimum and maximum quantity, the price list and its validity); a despatch
advice names the production lot, or the serial number of every casting,
which stays the same when a cancelled despatch advice is replaced; and a
till receipt during a promotion shows the discount on the shelf price. What
each kind of document carries is fixed in the item table
(`analysis/item-profile.md`): a catalogue or an offer everything about the
type; an order the identification and the variant chosen; a despatch advice
the lots, serials and dangerous goods; an invoice the identification and
what tax needs; a customs declaration the description, commodity code and
origin; a shopper's receipt the name, the brand and the warranty.

The colours an item comes in are facts of its type, listed in the catalogue
as variants; an order names the variant it wants by its identifier and
states nothing new about the item. Only a colour the catalogue does not
offer is specified in the order, as something made to order. Where the
shopper sees and chooses the variant, as the wood of the Marrow bench and
chair, each variant is a trade item of its own with a GTIN of its own, as
GS1 asks: the maker keeps one item number for the model and adds the
variant to it, and the store gives each variant a number of its own. A product's
carbon footprint is stated per lifecycle stage, the supply of raw materials
and the making of the product, as two figures that add up to the total.

Items are combined in four ways, each shown by a case the world already has:

- **A single item**, ordered and sold alone, with its own number: the
  Elderwick Marrow bench in oak, or the chair in ash.
- **A pack of the same item**, n times the same packed as one unit: the
  sawmill's bundle of 50 hardwood bench slats. The item and the pack are two
  levels, each with its own number.
- **A kit of different items**, wrapped in one package and sold as one: the
  Elderwick care kit for the Marrow dining furniture (a 250 ml tin of
  hard-wax oil and a lint-free cloth), or the ground anchor set of the park
  bench. A kit is one item with its own number and a stated content; on the
  GS1 side it has a GTIN of its own, because it is physically combined.
- **An offer**, items bought together for less but never one package: the
  Marrow set of a bench and two chairs in one wood, 899 lume in the shop
  instead of 947.
  It has no number of its own; each piece keeps its own, and a document
  that shows the sale carries a line per piece and a "Marrow set"
  allowance. GS1 calls this a virtual bundle and treats it as a selling
  arrangement, not a trade item.

The content of the slat bundle and the anchor set is settled with their
flows; the care kit's is given above. A cotton bale is not a pack: its
nominal weight of about 227 kg belongs to the item's description,
the number of bales to the shipment, and each bale's real weight to the
weight statement.

**Brands.** Elderwick is Brightmarket Stores' own label for home and garden,
built to stand as a brand of its own, as most retailers' private labels are.
The Elderwick Marrow bench (1400 mm) and the Elderwick Marrow chair are
dining furniture for indoors, in solid kiln-dried oak or ash with a hard-wax
oil finish, a closed seat, glued joints, felt pads under the legs and a seat
height of about 45 cm. Each comes in oak and in ash, and the shopper
chooses; the store plans three oak pieces for every two in ash. Brackenmere
Furniture makes them to the store's specification and sells them to the
store at 380 and 115 lume, the same in both woods; the store sells them in
its home and garden department at 549 and 199, from the day the department
reopens after its renovation, Monday 11 May, and gives a care kit free with
each bench. The stock comes in March and waits for the reopening; the line is
taken on sale-or-return terms for its first four weeks of sales. Many shoppers buy the chairs alone, because the 1400 mm
bench is too long for many apartment kitchens. The shopper sees the store's
label, and the maker's name is on no label: Elderwick is the world's case of
an item whose brand owner and manufacturer are different parties. The shirts
the store sells are the other way round: they carry the textile mill's own
brand, Lumeport, so the mill numbers them from its own GS1 prefix. Under
GS1's rules the brand owner numbers the item, so the bench and the chair in
each wood and the care kit each have a GTIN from Brightmarket's prefix,
whoever sells them: five GTINs; the set, being an offer, has none. Brackenmere sells its own office and outdoor
furniture under its own name: the office desk, the park bench PB-2 it
tenders with, and the furnishing of public offices with installation.

## The park bench

The park bench Serra 180 is the item the world follows furthest. It is made
of two side frames of ductile cast iron (EN-GJS-400-15), galvanised and
powder-coated, of 11.1 kg each; five slats of thermally modified ash of
1,800 × 95 × 45 mm at 4.24 kg each, which the sawmill in Marrowdale modifies
in a kiln of its own and which are left untreated to turn silver-grey; and a
set of 20 stainless A4 bolts with nuts and washers: 44.1 kg in all. It is
1,800 mm long over the slats and 1,660 mm over the armrests. It is bolted to
the ground with four anchors, which are a separate item. A spare side frame
is classified as a part of a seat (HS 9401.99), because it is made for the
bench; the anchors and bolts are parts of general use and stay in the metal
chapters. The bench's figures come from a parametric model of it, with
drawings, in `world/bench/`.

The bench ships knocked down, in three parcels that a person can carry: two
frame cartons of 790 × 680 × 100 mm, of 12.2 kg and 13.0 kg (the second with
the bolts), and a strapped bundle of five slats of 21.8 kg, 1.81 m long,
which two people carry because of its length: 47.0 kg gross. A spare side
frame is simply one frame carton. Four benches make a pallet of
1,850 × 700 × 745 mm and about 216 kg, with the pallet's own 28.2 kg, moved
by fork-lift and stacked two high; 24 such pallets and a pallet of frame
cartons take 13 floor positions of a 13.6 m trailer or a 40-foot container.
An installation crew of two assembles and anchors the benches in a park; a
shopper who buys one has the three parcels delivered.

The three countries apply the limit of ISO 11228-1 for manual handling:
25 kg for one person in good conditions, and about two thirds of the
combined capacity for two people lifting together. Goods are packed so that
a parcel a person lifts stays within it. Anything heavier is moved by
machine, as a pallet is by fork-lift and a cotton bale of about 227 kg is,
and the documents say so.

The bench's goods chain runs through the documents of several flows.
Valdara makes to order, in lots: a lot has a date, a quantity and a coating
batch, every side frame has a serial number that rises with the day it was
cast, and every casting day has its own melt number. Lumeway holds stock in
Marrowdale. It receives 96 benches and 12 spare frames by road on 25 March
and 192 benches by rail on 15 April, and sells from that stock in the order
the goods arrived: 24 benches to Brightmarket on 29 April, and 104 benches
and the 12 frames to Velumi on the island on 13 May. The store refuses one
of its 24 benches at goods-in, damaged; it goes back to Marrowdale on the
truck the same day and is held apart as damaged stock, not for sale. At the
end of May Lumeway holds 161 benches, 160 for sale and the damaged one. Velumi buys by the pallet: of its 104 benches, on
26 pallets of four, 96 are for the Port of Selanu's harbour parks and two
pallets are for its own stock, from which its shop sells two benches to a
cotton farm in June; six remain. An urgent order does not come from stock: when
Velumi asks for eight more frames on 11 May, Lumeway has none, so Valdara
casts them and they pass through Lumeway's dispatch area to the aircraft, a
cross-dock. They are spares for the port's harbour benches and travel under
the Accord's common transit from Ferrano to Selanu airport. Booked on the
afternoon flight of 13 May, they reach the cargo terminal after the cut-off,
because the truck from Ferrano is late, and fly the next morning; Lumeway
cancels its despatch advice, which named the missed flight, and replaces it. Valdara also sells direct: 40 benches to the public works
department on 30 March, from a lot of their own, and two benches travel to a
fair under a carnet.

## Billing

An invoice requests payment. A supplier may invoice on despatch, as Valdara
Industries does, or after the customer's receipt advice. A credit note is
the supplier's document for what the customer does not owe after all. A
debit note is its counterpart: the supplier's addition to an invoice it
issued, when more is due than was charged; it refers to that invoice and
gives the reason. It is not a buyer's claim against its supplier. When a
buyer has a claim on its supplier (a service the buyer performed, a cost it
had to bear, a contract penalty), the world uses an invoice from the buyer,
a credit note from the supplier, or a deduction shown in the remittance
advice, as the flow's story requires.

The world's debit notes come from the rail delivery to Lumeway. Its
framework contract gives a container five free days at the consignee's
siding, counted from the day after it is placed, and then charges 7,500
ferra per container day. The second container waits two days beyond that,
because Lumeway's fork-lift is in repair: the freight invoice was right when
it was issued, and more became due afterwards by a rule of the contract. So
Ferrano Rail Cargo adds the demurrage to its freight invoice with a debit
note to Valdara, the transport user, and Valdara, whose buyer bears a delay
in unloading under DAP, adds it to its goods invoice with a debit note to
Lumeway. A bonus that is known before the invoice, such as the ore train's
for arriving on the first day of its window, is a charge on the invoice.

## Tax and customs

A seller states its own country's tax. An Urvanian seller's invoice shows
Urvanian value added tax or the reason none is due; a Bayvarran seller's
shows the state sales tax or an exemption; a Lisavan seller's has no tax
section at all: no tax total, no tax category on the line and no tax
scheme. Nothing is implied by that absence, because the totals state it: the
amount without tax, the amount with tax and the amount to pay are equal.
Taxes the island does have keep their section. Urvania does not tax a
service supplied outside Urvania, to a customer established abroad or on
land abroad; it exempts the carriage of goods directly linked to their
export, as most VAT systems do, so the barge operator's freight for the
granulate going down the river to Bayvarra carries no Urvanian tax and says
why; and Urvania also levies an energy tax per kilowatt hour, in two
tiers, on which value added tax is then charged.

Bayvarra taxes what foreign businesses earn from its public purse, at
source. A public body in Bayvarra withholds 10 % of the price of a service
from a business not established there and pays it to the state; such a
supplier names a tax representative in Bayvarra, registered with the tax
office. It is a tax on income, not a sales tax, and it applies to public
bodies only: a company withholds nothing from a foreign carrier. On the
island, a buyer of farm produce withholds a presumptive tax, 1 % of a
delivery's value up to 2,000 coral and 2 % above, and the farm collects a
levy of 1 % for the cotton fund of the chamber of commerce; seed cotton is
priced from the trade accord's lint reference price, published in lume.
Lumeport's water company also collects the city's sewage levy, as a line
collected on behalf of the city, and runs the city's district heating.

Goods of Accord origin cross the borders free of duty, on proof of origin:
every import declaration claims the preference, names the criterion
(wholly obtained, sufficiently processed, or regional value content) and
refers to its proof of origin. The proof is a certificate of origin from a
chamber of commerce where the exporter asks for one, or else the exporter's
statement on origin on its commercial invoice, worded as the origin
declarations of the EU's preferential arrangements. Goods from outside the Accord pay each
country's own tariff. What is still due at the border differs. In Urvania,
value added tax of 20 % on the value with freight to the border, which a
business deducts again. In Bayvarra nothing, because its sales tax is
charged once, at the final retail sale. In Lisavu the import consumption
tax of 10 % on the landed value, whatever the goods' origin, so imported
goods cost more on the island than on the mainland: freight, and 10 % on
top.

Goods may also cross a land border under the Accord's common transit
procedure, modelled on the convention on a common transit procedure of
20 May 1987, which the EEC and the EFTA countries concluded and which today
joins the European Union and eleven other common transit countries. The
holder of the procedure lodges one transit declaration at the office of
departure; the goods travel under seal past the offices of exit and of
transit, and the procedure ends at the office of destination, where the
importer declares them for import, citing the transit declaration as the
previous one. The declaration's jurisdiction is the Accord, not the country
of departure alone. Valdara's containers by rail travel so, from the
customs office at the Ferrano hub to Bayvarra customs' inland office at
Marrowdale.

Valuation is national too, within the WTO's rules on customs valuation. In
all three countries the value starts from the price actually paid, and
charges that are part of that price (a special finish, export packing)
belong to it. Urvania includes freight and insurance to its border, in the
continental way. Bayvarra values goods as they left the exporting country,
without freight and insurance, in the settlers' tradition, as the United
States, Canada and Australia do. Lisavu, an island that lives on import
taxes, values everything landed, with freight and insurance to the island.
Every declaration follows the rule of the country it is lodged in, and a
customs value declared on a transport document agrees with it; so the same
bench has one customs value entering Bayvarra and another entering Lisavu.

## Money and payment

The three currencies trade at fixed parities: 1 lume = 100 ferra = 0.4
coral. The coral has been tied to the lume since the Lumeport Agreement of
1974, as an island that sells its cotton in lume has every reason to do; the
ferra joined at a fixed parity when the Trade Accord came into force in
1996. The parities are fixed by the Accord's monetary protocol and reviewed
every five years, against how the three economies have developed: an
adjustable peg, as the Bretton Woods system was. The last review, on
1 January 2022, left them unchanged; the next is on 1 January 2027. Through
2026 every exchange rate in the examples is the parity. There is still a
daily official rate, the noon fixing of the Lumeport Exchange, which does not
change between reviews, and the Accord's size classes give their turnover
limits in all three currencies at the parities. Currency risk is real across
a review: anything agreed now and paid after 1 January 2027 may be paid at
another rate, and a forward exchange contract protects a long commitment
across the review date.

Payment terms come in three layers. First, what the parties agreed in a
contract or a framework agreement. Where they agreed nothing, the seller's
standard terms, which follow its country's practice: Urvania gives 2 %
discount for payment within ten days of 30 days net; Bayvarra charges a
surcharge per month late on 30 days net; the island gives 45 days. Where
neither says anything about late payment, the statutory interest of the
seller's country applies (in Urvania 8 % a year). Across a border the
seller's country's rule applies, unless the contract chooses another. So
Valdara's framework agreement with its rail carrier sets 30 days net from
the consignment note, and the carrier's invoices fall due from the
consignment note with no discount; the public works contract sets 30 days
after each accepted release, so Valdara's invoice falls due from the
acceptance, not from its own date. A standard terms code means one text and
one period wherever it is used.

Utility bills are due 21 days after they are issued, in all three
countries, by a rule of the Accord, part of the common minimum it sets for
the customers of the national utilities. They carry terms of their own, an
Accord code, `TA-UTIL`, not a country's standard terms; a bill collected by direct
debit says so and is collected on the due date.

Bayvarra rounds cash payments to 5 cents, its smallest coin. A transfer
quotes a creditor reference in the structure of ISO 11649, made from the
invoice number, so the payee can match it, and runs over the domestic
clearing or, between the countries, the trade accord's payment link. Coral
net, the island's clearing, settles tokenised deposits on the Bank of
Selanu's ledger.

## Prices

Prices along the bench's chain follow its steps, and the figures are a
current base. Valdara has a list price, the price of its list VI-PL-2026,
which a direct customer pays, and gives Lumeway, its distributor for Bayvarra
and the island under a distribution agreement of 1996, a lower distributor
price: it sells the bench to Lumeway at 399.00 lume, and to the public works
department, delivered, at its list price of 499.00, which the tender
catalogue calls the contract price. Lumeway sells it to the department store and to
the island's importer at a trade price of 520.00, a margin of about 22 %
after the truck from Ferrano. The store sells it to a shopper at a shop
price of 749.00, or 674.10 during the spring promotion, 10 % off. The
island's shop price is not yet settled. The spare side frame goes from
Valdara to Lumeway at 47.50; Lumeway's trade price for it is 64.00, and
58.00 on its revised list of 20 May. To the island Lumeway sells it at 67.00, CIF Selanu: a price
with the frame's share of the sea freight, export clearance and insurance in
it, which leaves Lumeway about 16 %. The cargo insurance that CIF obliges
Lumeway to take out costs a premium of 0.22 % of the insured value, the CIF
value plus 10 %, so it follows the value of each shipment. The eight urgent frames that fly to the
island go at the trade price, carriage paid to Selanu airport, and Lumeway
recharges the air freight at cost, a surcharge the island's buyer accepted
when it asked for them. In the
public tender Valdara bids 499 a bench plus 18 for installation: above what
its distributor pays and below what its distributor charges, a direct
project price.

A shop price in Bayvarra excludes the sales tax, which is added at the till
(674.10, tax 43.82 at 6.5 %, 717.92 to pay): the tax is levied once, at the
final sale, by the state. On the island there is no sales tax, so the price
is the price. With its value added tax, a consumer price in Urvania would
include the tax. Every kind of price in the world's price type list (trade,
distributor, catalogue, contract, recommended retail, promotional price) is
a price before tax, and the list says so for each.

Three rules of thumb keep the figures plausible, and the build checks them:
nobody resells below what they paid plus the freight the documents state
(shared over a transport's load by gross weight) and the import tax they
bear; a
reseller's gross margin falls in a band for its kind (a distributor 15 to
30 %, a retailer 30 to 45 %, and 40 to 60 % on clothing, lower during a
promotion), freight recharged at cost counting neither as cost nor as price;
and a company's
turnover per person falls in a band for its kind.

## Document numbers

Every issuer numbers its own documents, per kind of document, and its
numbers rise with the time of issue across all flows. The numbers reflect
the size of the business: the examples show a sample of each company's
sequence, with gaps where its other business lies. A distributor that issues
some 2,800 invoices a year is near number 920 at the end of April; a farm is
in its low two digits.

The style of a number fits the issuer's country, size and trade. Large
companies use plain numeric ranges from their business systems, one range
per kind of document, running on from year to year (`4500021873`).
Mid-sized companies use a code of their own, the kind of document, the year
and a number, restarting each year (`LMW-INV-26-0920`); each company chooses
its code, which is unique in the world and not made from its initials. Small
companies write the year and a number. Public bodies use file references
(`PWD/2026/0187`). In Urvania invoices and credit notes are numbered within
the year by its rules for value added tax (`2026/0920`), whatever the
seller's own style; Bayvarra and Lisavu have no such rule. Transport
documents follow their trade: an air waybill has the airline's three-digit
prefix, a serial and a check digit, a bill of lading the shipping line's code
and a number, a utility bill the customer's account and the period. Whoever
runs the system gives the number: a shopper's web order carries the shop's
number. Which issuer uses which style is a current base.

A number says nothing by itself: what a document is, and who issued it, is
said by its elements. A creditor reference on an invoice is built from the
invoice number and changes with it.

A transaction has an identifier of its own. `ProfileExecutionID` identifies
one collaboration: one run of a process between the same parties, such as an
order with its despatch advice and its invoice, or a tender procedure. The
party that starts the collaboration gives it, in its own numbering style (for
an order-to-invoice cycle the buyer, for a tender the contracting body, whose
procurement file is such an identifier), and every later document of that
transaction repeats it, so that a reader can collect the documents of one
transaction by this element alone. A document that belongs to no
collaboration with others carries none.

## The calendar

Offices and factories work Monday to Friday; shops Monday to Saturday;
ports, carriers, terminals, border customs and the operations of utilities
every day, and their contacts say so. The week is the same in all three
countries. A document is dated on a day its issuer works, unless it says why
not, and the build checks it.

The three states are secular: there is no state church and the law names no
religion. The public holidays fall on dates a reader recognises and carry
civil names, as Uruguay's did when it renamed its holidays in 1919. The
seasons are those of the south: December is midsummer and August midwinter,
and the island's cotton is picked from March to May. All three countries
keep 1 January as New Year's Day and Accord Day, the day the Trade Accord
came into force in 1996. The holidays below, with their dates in 2026, are a
current base.

Urvania has 11 days, on fixed dates, in the Italian manner; a holiday that
falls on a weekend is not made up for.

| Date in 2026 | Holiday | Why |
|---|---|---|
| Thursday 1 January | New Year and Accord Day | shared by the three countries |
| Tuesday 6 January | Children's Day | the Italian gift-giving day, under a civil name |
| Monday 9 March | Independence Day | independence in 1962 |
| Friday 1 May | Labour Day | |
| Wednesday 17 June | Language Day | the day Urvanian became an official language beside English |
| Saturday 15 August | Ferragosto | kept from the Italians (the Roman emperor Augustus's rest after the harvest), though it falls in midwinter here; people still call it the summer rest |
| Wednesday 14 October | Constitution Day | the constitution adopted after independence |
| Monday 2 November | Remembrance Day | the Italian custom of visiting the family graves, as a civil day |
| Friday 25 and Saturday 26 December | Family Day and the Day of Rest | the year-end holiday, in midsummer |
| one local day | Founders' Day of one's town | Ferrano: Friday 4 September; Serravona: Friday 4 December, Miners' Day |

Bayvarra has 8 days, mostly Mondays, in the British manner of bank holidays;
a holiday that falls on a weekend is given on the next working day.

| Date in 2026 | Holiday | Why |
|---|---|---|
| Thursday 1 January | New Year and Accord Day | shared by the three countries |
| Monday 16 February | Settlers' Day (third Monday in February) | the first landing, at Larkmouth in the 1820s |
| Monday 4 May | Labour Day (first Monday in May) | |
| Monday 3 August | Winter Bank Holiday (first Monday in August) | the British August holiday, moved into winter by geography |
| Monday 19 October | Federation Day (third Monday in October) | the states formed the federation |
| Friday 25 December | Family Day | |
| Monday 28 December | Boxing Day, observed | 26 December is a Saturday |
| one state day | Upland State Day: Monday 13 April; Coastal State Day: Monday 30 November | Bayvarra is federal; Marrowdale is in Upland State and Lumeport in Coastal State |

Lisavu has 9 days, around the sea and the cotton.

| Date in 2026 | Holiday | Why |
|---|---|---|
| Thursday 1 January | New Year and Accord Day | shared by the three countries |
| Friday 6 February | Seafarers' Day (first Friday in February) | an island that lives by ships |
| Wednesday 18 March | Agreement Day | the Lumeport Agreement of 1974, which ended the island's isolation |
| Friday 1 May | Labour Day | |
| Friday 15 May | Harvest Festival (third Friday in May) | when the cotton is in |
| Tuesday 7 July | Island Day | self-government |
| Monday 21 September | Elders' Day | the Lisavan tradition of honouring the old, at the start of spring |
| Friday 25 and Saturday 26 December | Family Day and the Day of Rest | |

The countries are not kept in step. On 1 May Urvania and the island are
closed and Bayvarra works; on Monday 4 May it is the other way round. On
Upland State Day Marrowdale is closed and Lumeport is open. An order sent on
the receiver's holiday is read a day later; a due date on a holiday moves to
the next working day; a payment between two countries settles on a day both
banking systems are open; a deadline in working days counts the working days
of the party that set it. Ports, ships, aircraft and border customs work
through all of it, and those who plan a ship's arrival plan around such days.

The world has two time zones and no summer time. The mainland is one hour
behind UTC (UTC−01:00) and the island on UTC (UTC+00:00), all year. Each
country names its own legal time: Urvanian Time and Bayvarran Time, both
UTC−01:00, and Lisavu Time, UTC+00:00. Documents use no abbreviations, which
are not standardised and collide, and not "GMT", the name of the United
Kingdom's civil time. A time is written with its offset from UTC, as
ISO 8601 writes it (`07:00:00-01:00`), at least wherever a document crosses
the zone boundary, and an address states its zone as an offset. A flight
that leaves Lumeport at 07:00 is timetabled into Selanu at 10:45 island
time: a block time of 2 h 45, of which about 2 h 10 to 2 h 15 are needed
eastbound with the westerly winds, so it usually lands early.

The week starts on Monday in all three countries, and weeks are numbered as
ISO 8601 numbers them: week 1 is the week with the year's first Thursday. In
2026 week 1 runs from Monday 29 December 2025 to Sunday 4 January 2026, and
the year has 53 weeks. UBL has no element for a week number, so a document
states a week as a period from Monday to Sunday, described by the code
`WEEK` of the world's period list; a week number appears only in free text
("delivery in week 21"), and then as the ISO number.

## Flows of documents

The parties do business in flows. Each country has its own raw material
and industry: Urvania mines ore and makes park benches, recovering its
production waste as recycled plastic; Bayvarra saws timber, makes furniture,
packaging and clothing, and distributes and retails; the island Lisavu grows
and gins cotton, its export. Goods cross the land border by road, rail and
river barge and go overseas by sea and air in both directions; there is a
public tender and a design contest, a temporary export with an ATA carnet, a
utility in each country, and gas by pipeline from Bayvarra's offshore field to Urvania's
power station and grid. Each flow starts from the business: who buys
from whom, on which delivery terms, and therefore who arranges and pays the
transport. A distributor that buys free carrier (FCA) books the truck
itself and names the carrier in its order; a retailer that buys delivered
duty paid (DDP) leaves the transport to its supplier, who then needs an
outgoing waybill.

A document that is revised keeps its number and says which version it
supersedes, with `VersionID` 2 and `PreviousVersionID` 1, and its reasons say
what changed. The design contest shows this: the city of Lumeport relaunches a
contest for its harbour promenade bench, cancelled the year before because no
design met the brief (the new notice gives the reason), offers three prizes and
asks a group of designers to form a limited company before the follow-up
contract. The council raises the prize fund, a corrigendum corrects the site
plan and widens a selection criterion, the design team updates its
declarations, the registry reissues its extract when new accounts are filed,
and the results notice corrects a prize amount.

Every document in a flow records:

- the document type, its sender and its receiver;
- why it is sent, in business terms;
- every party it mentions, at its place in the UBL structure, for example
  the road carrier at `Order/Delivery/Despatch/CarrierParty`.

A flow also lists its transport legs: the mode, from which party to which,
and the carrier. The goods only move where the world allows it. A road leg
needs a road from party to party, so a truck cannot drive to the island; a
rail leg needs a rail line between them, a barge needs the river at both
ends, gas a pipeline from party to party, a ship a sea route from port to
port and an aircraft an air route from airport to airport. The carrier must
have a vehicle, train, vessel, aircraft or pipeline of that mode in its
fleet, and every carrier a document of the
flow names must carry one of its legs. Domestic jobs go to a carrier of
that country: a truck of one country driving within another would be
cabotage, which only happens where a document says so.

A truck is weighed against the Trade Accord's road protocol: a tractor unit
with its semi-trailer, or a truck with its trailer, may weigh at most 40
tonnes with its load. The carrier's fleet gives each vehicle's empty weight,
so its payload is what is left: Trasvia's tractor of about 7.8 t and its
curtain-side trailer of about 7.5 t can carry about 24.7 t. A weighed load
stays within both, and the build checks it.

Waste that stays in Urvania moves under Urvania's own waste law, not under
the Basel Convention's procedure for transboundary movements, on the model
of a national reporting point for waste. Urvania's environment agency is the
competent authority: it issues the permits of waste treatment plants,
registers waste carriers, and receives two reports. The producer notifies
its waste stream for a year before the first load (the waste by its code in
Urvania's waste list, which takes over the numbers and the rules of the
European List of Waste, the planned total, the number of loads, the period,
the loading place and the facility), and the agency acknowledges it with a
waste-stream number; a domestic stream of non-hazardous waste for recovery
needs no consent. The facility then reports each load it receives, with its
net weight from its weighbridge and the stream's number. UBL's waste
notification requires a `CustomsParty`, "the competent authority granting a
permit to export or import the waste"; for a domestic stream it names the
environment agency, the only competent authority there is.

Goods that go abroad for a while and come back, such as samples for a fair,
travel under an ATA carnet, which the Accord's countries take over from the
real convention on temporary admission. The exporter's chamber of commerce
issues it and guarantees it, the chamber of the country visited guarantees
it there, and customs stamp its counterfoils as the goods move: exportation
and re-importation at home, importation and re-exportation abroad, and a
transit counterfoil with its two vouchers for each crossing of a third
country, on entry and on exit. As issued, a carnet carries its counterfoils
unstamped. Valdara shows two Serra benches at the Selanu Chamber of
Commerce's trade fair in early June: the carnet is issued on 25 May, the
samples cross Bayvarra on their transit vouchers both ways, and the island's
customs give them until 30 June to leave. Its re-exportation voucher goes
astray, so in July, after the limit, the island's chamber asks for proof, a
month later it reminds, and Urvania's chamber answers with the stamped
counterfoils and Urvania's record of the re-import. What was at stake is
only the island's import consumption tax of 10 % on the declared value and
the carnet's surcharge of 10 % of it, about 44 coral: benches of Accord
origin owe no duty.

A leg takes the time its distance needs at the mode's usual speed. Where a
document's timeline is longer than that, the extra time has a reason that is
part of the world, before any date moves:

- Lumeway's customs desk, which clears its imports, works on weekdays from
  08:00 to 17:00, and its goods-in takes deliveries in the morning only, in
  slots booked a week ahead. A truck that reaches the border after the desk has closed
  waits there for the night, which is also the driver's rest, clears in the
  morning and is unloaded in its slot.
- A train stops at the border station for a crew change, a brake test and a
  seal check, and leaves on its timetabled path; a shunting trip then places
  the wagons on the receiver's siding.
- Selanu's pilots bring ships in by daylight only. A ship that arrives in the
  dark does not anchor; it waits under way and berths at first light.
- The barge on the river sails by daylight only and is unloaded by the
  receiver's morning shift.

An air leg also says how the goods are loaded, and the build checks that the
load fits the island airline's ATR 72-600F, as ATR's fact sheet gives it: at
most 9,200 kg, 75 m³ and seven LD3 containers, each within its own maximum
weight, and loose pieces that pass the 2.94 × 1.80 m cargo door into the aft
bulk compartment. The sample benches, at 1.8 m, fly loose. Dangerous goods are
stowed as the IATA Dangerous Goods Regulations ask. The mast flow's twelve
lithium-ion battery modules, 27 kg each in their crates on a pallet, and its
box of five 1-litre tins of coating stripper may fly on cargo aircraft only,
the stripper because five litres in one package are more than a passenger
aircraft may take of it; both go in LD3 containers with net doors at the front
of the main deck, where the crew can reach them, with an empty position between
them, because the stripper's flammable subsidiary label must not be stowed next
to the batteries. The smoke detectors, an excepted package of class 7, need
neither crew access nor segregation and fly in a closed container further aft.
No container is cooled: batteries on a flight of under three hours in the
island's winter need no temperature control. A subsidiary hazard has no
emergency schedule of its own in the IMDG Code, which gives one per UN entry;
the road rules give the crew's actions per hazard label, so the subsidiary
hazard names the Accord's emergency card of its class.

A ship reports to the port before it arrives, with its security and health
certificates. The ocean carrier's second feeder came under Bayvarra's flag in
January: it sails with an interim security certificate and says why, and it
carries a sanitation control exemption certificate, which the port health
office issues when an inspection finds no control measures needed; the first
feeder carries a sanitation control certificate, as its inspection found pests
in the galley stores. The security report lists the ship-to-ship activities of
the last ten port calls, here a bunkering from the port's barge, with the
measure the ship took.

The vehicles on the map are these legs: one truck, train, barge, ship or
aircraft per leg, travelling the way the build found for it, from the
from-party to the to-party, and a leg flown the same way by the same carrier
in several flows is one aircraft. Each makes a round trip: it waits at the
from-party, travels out, waits at the to-party and travels back, and a leg and
its return leg by the same carrier are one vehicle. An aircraft takes off and
lands along the runway: it rolls along it, climbs out straight ahead over the
approach zone, and joins the final approach in line with the runway of the
airport it goes to. A pipeline has no vehicle: the gas is shown
flowing from the field to the consumers. Pipelines follow the rules of real
ones. They are buried, so they cross roads, rail lines and the river
underneath, at right angles and in a straight line, never along them; they
keep out of towns, and nothing is built or planted on their right of way.
They start at the producer, at its offshore platform or as a branch of
another pipeline, end at a customer, and carry exactly the pipeline legs of
the flows, in the direction the gas flows. Where the pipeline crosses the
land border, a border metering station measures the gas, as at the
interconnection points between real gas networks.

## Specifications

Every document says which specification it follows. `CustomizationID` names
a *transaction*: one kind of business message between two roles, with a
purpose, a content and rules, as in CEN BII and Peppol. One or more
document types carry a transaction (billing is the invoice, the credit note
and the debit note), and one document type can carry several (an
application response that answers an invoice is not one that answers a
message). The specification has up to three levels, chained with
`#compliant#` as EN 16931, Peppol and XRechnung chain theirs: the Trade
Accord's transaction (`urn:ubl-examples:world:trns:billing:1.0`), a national
specification built on it, such as Urvania's invoice rules for its value
added tax or Bayvarra's rules for bills to its public bodies, and the
specification of a community that exchanges among itself: the retail
community of the distributor and the store, the port community of
Lumeport, Urvania's energy market and public procurement. `ProfileID` names
one of the Accord's generic process profiles (ordering, billing, transport,
customs …), versioned, and no longer the flow; `ProfileExecutionID`
identifies one collaboration under such a profile, given by the party that
starts it (see "Document numbers"). Each specification has a short public page,
and the build checks that every identifier a document uses has one. The
world claims no compliance with real specifications such as EN 16931.

`UBLVersionID` gives the earliest UBL 2 version that defines every element
the document uses, as its definition asks. The build computes it from the
published models of UBL 2.0 to 2.5. For now every example needs 2.5: nearly
all use elements that UBL 2.5 added, such as the electronic address and the
further party identification.

## Signatures

Signatures are to be redone as a stage of their own, after the stories of
the flows are settled. The target is real electronic signatures, made and
verified by the build. Which documents are signed, and how, is decided in
that stage; until then the signatures in the examples stay as they are.

## Who sends and who receives

Who sends and who receives a document type comes from the UBL 2.5 semantic
model first: the elements `SenderParty` and `ReceiverParty`, or a definition
of the document or of one of its party elements, such as "The Party who
submits this Tender". Where the model does not say it, the party role table
of the UBL specification is used. Where neither says it, the choice is
marked as inferred, with the definitions it rests on. Every quote is checked
word for word against its source.
