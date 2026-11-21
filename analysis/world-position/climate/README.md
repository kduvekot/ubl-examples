# The climate of the world, from real data at its position

The UBL World's climate is taken from real measurements at the place on the ocean where the world lies
(`world/countries.json` "geography": the mainland around 30° S, 15° W, Lisavu around 33° S, 2.65° W), so that it
is factual and can be checked again if the world is ever moved or changed (owner, 2026-11-21, OW023, WK004).

## Source

- **NASA POWER** (Prediction Of Worldwide Energy Resources), Climatology API v2.10.2, community RE:
  <https://power.larc.nasa.gov/api/temporal/climatology/point>. Monthly and annual means for January 2001 to
  December 2025: temperature, rain, wind and humidity from NASA's MERRA-2 reanalysis, sunshine and cloud from
  CERES SYN1deg. Fetched 2026-11-21.
- `fetch_climate.py` fetches it for six points (the mainland's centre, north and east, Lisavu's centre, and Tristan
  da Cunha and St Helena to compare) and writes the raw answers to `data/` and the monthly tables to
  `climate-table.md`. The points follow the world's geography, so after a move the script is run again and the
  rules below are checked against the new table.
- The values are over the open sea at sea level. The world's land does not exist there: height (about 6.5 °C colder
  per 1,000 m) and the mountains' effect on rain (wet windward slopes, dry rain shadows, from the terrain's rain
  raster) come on top.
- **Considered and set aside:** Lord Howe Island (31.5° S, Tasman Sea; Bureau of Meteorology), first proposed as a
  model because it lies at the same latitude in the same subtropical belt; the owner preferred data from the
  world's own position, and that data differs (the mainland's summer wind is north-easterly, not east to
  south-easterly, and Lisavu is westerly nearly all year).

## What the data says (2001-2025 means)

| | Mainland (30° S, 15° W) | Lisavu (33° S, 2.65° W) | Tristan da Cunha (37° S) | St Helena (16° S) |
|---|---|---|---|---|
| Mean temperature, year | 20.0 °C | 17.5 °C | 14.9 °C | 21.8 °C |
| Warmest / coolest month | 23.4 °C (Feb) / 16.9 °C (Sep) | 20.5 °C (Feb) / 15.0 °C (Sep) | 18.1 / 12.2 °C | 24.5 / 19.7 °C |
| Rain over the sea, year | 791 mm | 541 mm | 1,316 mm | 58 mm |
| Wettest / driest months | Mar-Jun (110 mm in May) / Jan-Feb (35-38 mm) | May (91 mm) / Jan (18 mm) | all year | almost none |
| Summer wind (Nov-Mar) | north-east, about 5 m/s | south-west to west, about 5-6 m/s | west-north-west | east-south-east (trade wind) |
| Winter wind (May-Sep) | west-north-west, about 7 m/s | west to west-north-west, about 7.8 m/s | west, about 8.9 m/s | east-south-east |
| Sunshine, year | 5.1 kWh/m² a day (7.7 in Jan, 2.8 in Jun) | 4.8 (7.4 in Jan, 2.3 in Jun) | 4.0 | 5.4 |
| Cloud, year | 64 % (48 % in summer) | 72 % | 81 % | 69 % |

The world lies in the belt of the South Atlantic high, between the south-east trade winds (St Helena) and the
westerlies (Tristan da Cunha). The high moves north in winter and south in summer, so the mainland has two wind
seasons, and Lisavu, further south and east, lies on the westerlies' edge.

## The rules the world takes from it

1. **Seasons:** summer from November to March, dry, sunny and light-winded; winter from May to September,
   cloudier, with the strongest winds and the fronts. The rainiest months are the autumn, March to June.
2. **Winds:** the mainland's summer wind is north-easterly, its winter wind west-north-westerly ("the winter
   westerlies"); Lisavu's wind is westerly nearly all year, south-west in summer. The terrain's wet west and dry
   east (made with a prevailing west wind) follow the winter rain, which brings most of the year's total.
3. **Temperatures on the coasts:** about 23 °C in the warmest months and 17 °C in the coolest on the mainland, 20
   and 15 °C on Lisavu; day highs to about 27 °C in summer, night lows to about 12-13 °C in winter (10 °C on Lisavu).
4. **Height:** about 6.5 °C colder per 1,000 m: the massif's summit (1,920 m) and Lisavu's (1,810 m) are about
   12 °C colder than the coast, with winter nights just below freezing, so snow in some winters, not most.
5. **Rain on land:** 791 mm (mainland) and 541 mm (Lisavu) over the sea, raised on the windward slopes and lowered
   in the rain shadows by the terrain: Urvania's median about 900 mm, Bayvarra's dry north-east about 500 mm,
   Lisavu's windward high ground up to 4,800 mm, its lee plain 640-760 mm.
6. **Sun and wind for energy** (OW022): the mainland's sunshine, 5.1 kWh/m² a day over the year, is about that of
   southern Spain, best in summer; the wind is strongest in winter (about 8 m/s at 50 m over the sea, more on high
   ground), so sun and wind complement each other through the year.

## If the world moves or changes

Run `fetch_climate.py` again (it reads the new geography), compare `climate-table.md` with the rules above, and
bring the rules, the encyclopedia's climate texts (the countries' Geography and Climate sections) and, where the
winds change, the terrain inputs into line. A change of the wind regime would change the wet and dry sides of the
land, which is a terrain change (`tools/terrain.py`, O152).
