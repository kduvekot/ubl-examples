# The position of the world on the real ocean

The record of decision D19 in `analysis/worklist-decisions.md` (2026-11-16): where the fictional
countries lie in the South Atlantic, and why.

| File | What it is |
|---|---|
| `world-position.png` | The current base: the mainland astride the Mid-Atlantic Ridge (28.1° to 31.9° South, 17.7° to 12.3° West), the island Lisavu on a seamount of the Walvis Ridge (33.0° South, 2.65° West). Dashed rings: 200 nautical miles around the real islands. Hatched: the Rio Grande Rise. |
| `plot_world_position.py` | Draws it. |
| `world-position-rio-grande-rise-withdrawn.png` | The first proposal, on the Rio Grande Rise. Withdrawn: Brazil has claimed that plateau as continental shelf since 7 December 2018. Kept so that the reason stays visible. |
| `plot_world_position_rio_grande_rise.py` | Draws it. |

## How to redraw

    pip install numpy matplotlib
    python3 analysis/world-position/plot_world_position.py

The script fetches the depth grid once into `.review/geo/etopo.csv`, which is not committed.

## Sources and limits

- **Sea floor and coasts:** NOAA ETOPO1, one value every 10 arc-minutes, from NOAA's ERDDAP server
  (the address is in the script), fetched 2026-11-16. At that spacing (about 18 km) small islands do
  not show.
- **Real islands** (Tristan da Cunha, Gough, Saint Helena, Trindade, the Falkland Islands): positions
  entered by hand from memory, not from a chart.
- **The 200-nautical-mile rings** are circles around those positions, not official limits.
- **Brazil's claim** is drawn as a rough box around the Rio Grande Rise, not as the claimed limit.
- **Still to check** (open point O55 in `analysis/worklist-decisions.md`): a nautical chart for both
  areas; that no extended-shelf claim and no sea-bed licence reaches either; winds and climate from a
  source.

The map squares are 14 km. The position is a current base, open to correction.
