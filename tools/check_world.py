#!/usr/bin/env python3
"""Check the UBL world: checks that the terrain (world/terrain.json) was made from its current inputs
(tools/terrain.py --check) and that the place list (analysis/place-list.md) is current
(tools/place_list.py --check), that the Lumeport Exchange's fixings (world/fx-fixings.json) are current
(tools/fx_fixing.py --check), that every element no example covers has its row in the coverage register
(tools/coverage_register.py, analysis/coverage-register.md), builds the tile model (tools/world_model.py) and
reports every broken structural rule, then checks the documents of
the world against the UBL 2.5 model (tools/world_docs.py), the identities of the parties
(tools/world_parties.py), the items (tools/world_items.py), the goods against the built examples: lots and serials, the goods chains, item
physics and vehicle loads (tools/world_goods.py), the times of the transports against the map at the world's
speeds and the tax treatment against the goods' movement (tools/world_movement.py), and that the world code lists
are up to date (tools/build_codelists.py --check). Exit status 1 if there are problems.

The checks only read the repository, so they run side by side, each in a process of its own; their output is
printed in the order of the list, and the exit status is 1 when any of them fails. One thing passes between them:
tools/build_codelists.py --check reports the words missing from the vocabularies of the world's languages that the
checks before it met (world_data.MISSING_WORDS, which they shared when they ran one after another in one process).
Each check hands its missing words back; when the checks before build_codelists.py met any, it runs again with
them, so it reports exactly what it reported in one process.

Usage: python3 tools/check_world.py [--model model.json]
  --model: also write the tile model there (tools/world_model.py model.json), for the map sheet of the site build
"""
import concurrent.futures
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = [("terrain.py", ["--check"]), ("place_list.py", ["--check"]), ("fx_fixing.py", ["--check"]),
           ("world_model.py", []), ("world_docs.py", []), ("world_parties.py", []), ("world_items.py", []),
           ("world_goods.py", []), ("world_movement.py", []), ("build_codelists.py", ["--check"]), ("coverage_register.py", [])]
SHARES_WORDS = "build_codelists.py"     # reads world_data.MISSING_WORDS, as the checks before it left it

# Run one script as runpy did in one process (tools/ first on the path, argv[0] the script's name); afterwards write
# the words missing from the vocabularies to the file argv[3], and seed them from argv[4] if given.
RUNNER = r"""
import json, os, runpy, sys
here, script, words_out, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
args = json.loads(sys.argv[5])
sys.path[0] = here
if seed:
    import world_data
    world_data.MISSING_WORDS.update(json.load(open(seed)))
sys.argv = [script] + args
def words():
    wd = sys.modules.get("world_data")
    json.dump(sorted(wd.MISSING_WORDS) if wd else [], open(words_out, "w"))
try:
    runpy.run_path(os.path.join(here, script), run_name="__main__")
except SystemExit:
    words()
    raise
words()
"""


def run(script, args, tmp, seed=None):
    words = os.path.join(tmp, script + (".seeded" if seed else "") + ".words.json")
    seed_file = ""
    if seed:
        seed_file = os.path.join(tmp, script + ".seed.json")
        json.dump(sorted(seed), open(seed_file, "w"))
    p = subprocess.run([sys.executable, "-c", RUNNER, HERE, script, words, seed_file, json.dumps(args)],
                       capture_output=True)
    missing = set(json.load(open(words))) if os.path.exists(words) else set()
    return p.returncode, p.stdout, p.stderr, missing


def main():
    argv = sys.argv[1:]
    scripts = [(s, list(a)) for s, a in SCRIPTS]
    if argv[:1] == ["--model"] and len(argv) == 2:
        scripts[[s for s, _ in scripts].index("world_model.py")][1].append(os.path.abspath(argv[1]))
    elif argv:
        sys.exit(__doc__.split("\n\n")[-1])
    with tempfile.TemporaryDirectory() as tmp:
        with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count() or 1) as pool:
            results = list(pool.map(lambda sa: run(sa[0], sa[1], tmp), scripts))
        names = [s for s, _ in scripts]
        i = names.index(SHARES_WORDS)
        before = set().union(*(r[3] for r in results[:i]))
        if before:
            results[i] = run(SHARES_WORDS, scripts[i][1], tmp, seed=before)
    failed = False
    for code, out, err, _ in results:
        sys.stdout.buffer.write(out)
        sys.stdout.flush()
        sys.stderr.buffer.write(err)
        sys.stderr.flush()
        failed = failed or code != 0
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
