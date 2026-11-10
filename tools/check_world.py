#!/usr/bin/env python3
"""Check the UBL world: builds the tile model (tools/world_model.py) and
reports every broken structural rule. Exit status 1 if there are problems.

Usage: python3 tools/check_world.py
"""
import os
import runpy
import sys

sys.argv = [sys.argv[0]]
runpy.run_path(os.path.join(os.path.dirname(__file__), "world_model.py"), run_name="__main__")
