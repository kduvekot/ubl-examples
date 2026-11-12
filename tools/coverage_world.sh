#!/bin/sh
# Coverage of the world's examples against the endorsed (non-deprecated) elements of UBL 2.5: how many of the
# document types, aggregates and basic elements the model allows appear in at least one example.
# Fetches the UBL 2.5 entity model into .ubl/ (not committed) the first time.
# Usage: sh tools/coverage_world.sh [report.md]
#   prints the summary line ("| All | covered | total | missing | % |") and the missing elements;
#   the full report (per document type) goes to report.md when given.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
MODEL=.ubl/mod/UBL-Entities-2.5.gc
[ -s "$MODEL" ] || { mkdir -p .ubl/mod; curl -sSf -o "$MODEL" https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/UBL-Entities-2.5.gc; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
mkdir "$TMP/xml"
for f in world/examples/*/*.xml; do cp "$f" "$TMP/xml/$(basename "$(dirname "$f")")-$(basename "$f")"; done
python3 tools/coverage.py --model "$MODEL" --examples "$TMP/xml" --endorsed world/ubl-model.json > "$TMP/report.md"
[ -n "$1" ] && cp "$TMP/report.md" "$1"
grep "^| All" "$TMP/report.md"
awk '/<summary>/{match($0,/<b>[^<]*<\/b>/); t=substr($0,RSTART+3,RLENGTH-7)} /^\| [A-Z]/ && !/Parent \|/{split($0,f,"|"); if (t!="") print "missing: "t" :: "f[2]"."f[3]}' "$TMP/report.md" | sed 's/  */ /g' | grep "\.xml" || true
