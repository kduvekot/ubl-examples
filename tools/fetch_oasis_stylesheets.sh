#!/bin/sh
# Fetch the OASIS DocBook publishing stylesheets (spec-0.9) used by the
# OASIS UBL TC, from https://github.com/oasis-tcs/ubl at a fixed commit.
#
# They are fetched at build time instead of being copied into this
# repository: they are OASIS TC content, governed by the OASIS IPR Policy.
#
# Usage: tools/fetch_oasis_stylesheets.sh [target-dir]   (default: .oasis)
# Result: <target-dir>/db/spec-0.9/...
set -eu

# oasis-tcs/ubl branch ubl-2.5-os (spec-0.9 last changed 2026-01-10)
COMMIT=345386aa0504488aebdbec1c7d629ce9b7d08826
DIR=${1:-.oasis}

if [ -f "$DIR/.commit" ] && [ "$(cat "$DIR/.commit")" = "$COMMIT" ]; then
  echo "OASIS stylesheets already present in $DIR"
  exit 0
fi
rm -rf "$DIR"
git init -q "$DIR"
cd "$DIR"
git remote add origin https://github.com/oasis-tcs/ubl.git
git sparse-checkout set --no-cone /db/spec-0.9/
git fetch -q --depth 1 --filter=blob:none origin "$COMMIT"
git checkout -q FETCH_HEAD
rm -rf .git
echo "$COMMIT" > .commit
echo "OASIS stylesheets from oasis-tcs/ubl@$COMMIT in $DIR"
