#!/bin/sh
# Convert the Markdown sections of the note (note/src/*.md) into DocBook 4.5
# fragments (note/sections/*.xml) that the hub document includes.
#
# DocBook is the authoritative source of the note; Markdown is the
# convenient way to write it. Run this after editing a Markdown file and
# commit both. The site workflow fails if the two are out of step.
#
# Usage: tools/md2docbook.sh [--check]
# Requires: pandoc
set -eu
cd "$(dirname "$0")/../note"
check=${1:-}
status=0
for md in src/*.md; do
  base=$(basename "$md" .md)
  out=sections/$base.xml
  tmp=$(mktemp)
  {
    echo "<!-- Generated from note/$md by tools/md2docbook.sh; edit the Markdown, not this file. -->"
    # sect1..sect5 -> section, so fragments nest inside the hub's article;
    # ids are prefixed with the section file name to keep them unique.
    pandoc -f gfm -t docbook4 --top-level-division=section --id-prefix="S-$base-" "$md" |
      sed -E 's#<(/?)sect[1-5]([ >])#<\1section\2#g'
  } > "$tmp"
  if [ "$check" = "--check" ]; then
    if ! cmp -s "$tmp" "$out"; then
      echo "out of date: $out (run tools/md2docbook.sh)"
      status=1
    fi
    rm -f "$tmp"
  else
    mv "$tmp" "$out"
    echo "wrote $out"
  fi
done
exit $status
