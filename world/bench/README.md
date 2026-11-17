# Serra 180 park bench: parametric model

The geometry behind the world's most-followed item, the park bench Serra 180 (Valdara Industries, VI-B180),
made for open point O149. The results and the check of every figure the world uses are in `report.md`.
Nothing in the world's data is changed by this directory.

## Files

- `parameters.json`: the single source of truth (dimensions, materials, the two slat woods under `woods` with
  `main_wood` = thermally modified ash and `comparison_wood` = oak, stainless fixings, loads, casting, packaging,
  vehicles, and the world's current figures for comparison). The analysis runs for both woods; drawings and the
  main figures use the main wood.
- `build_bench.py`: builds everything from the parameters: the solids (build123d / OpenCascade), the analysis
  (masses, centre of gravity, slat and frame stresses, casting yield, parcels, pallet, vehicles), STEP and GLB files,
  the SVG drawings, `results.json`, then calls `render.js` and `report.py`.
- `report.py`: writes `report.md` from `results.json`.
- `render.js`: PNG renders with three.js in headless Chromium (Playwright).
- Generated: `step/`, `glb/`, `drawings/`, `renders/`, `results.json`, `report.md`.

## Running

The repository's own build does not use this directory. Install the CAD kernel in a virtual environment outside
the repository, and three.js with npm in a scratch directory:

```sh
python3 -m venv /path/to/venv
/path/to/venv/bin/pip install build123d          # tested with build123d 0.13.0, Python 3.13
(cd /path/to/scratch && npm install three@0.160.0)
THREE_DIR=/path/to/scratch/node_modules/three /path/to/venv/bin/python world/bench/build_bench.py
```

Options: `--no-render` (skip the PNG renders), `--no-drawings`. A full run takes well under a minute.
Playwright and its Chromium must already be installed (`require('playwright')` must work in Node).

To change the design, edit `parameters.json` and run the generator again; every drawing, file and figure in the
report follows. The report's prose has the numbers filled in by `report.py`; its judgements (the list of
inconsistencies) are written for the current parameters and should be read again after a change.
