#!/usr/bin/env python3
"""Check the UBL world: builds the tile model (tools/world_model.py) and
reports every broken structural rule, then checks the documents of
the world against the UBL 2.5 model (tools/world_docs.py). Exit status 1 if there are problems.

Usage: python3 tools/check_world.py
"""
import os
import runpy
import sys

sys.argv = [sys.argv[0]]
failed = False
for script in ("world_model.py", "world_docs.py"):
    try:
        runpy.run_path(os.path.join(os.path.dirname(__file__), script), run_name="__main__")
    except SystemExit as e:
        failed = failed or bool(e.code)
sys.exit(1 if failed else 0)
