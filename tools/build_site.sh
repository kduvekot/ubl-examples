#!/bin/sh
# Build the documentation site into a folder (default: _site).
#
#   _site/index.html                  landing page
#   _site/note/                       the note (DocBook -> HTML, OASIS stylesheets)
#   _site/history.html                how the examples history was built
#   _site/releases.html               README.md: releases and their changes
#   _site/coverage.html               element coverage analysis
#   _site/coverage-details.html       every missing element
#
# Usage: tools/build_site.sh [out-dir]
# Requires: xsltproc, xmllint, pandoc; fetches the OASIS stylesheets into .oasis
set -eu
cd "$(dirname "$0")/.."
OUT=${1:-_site}
ROOT=$(pwd)

tools/fetch_oasis_stylesheets.sh .oasis
tools/md2docbook.sh --check

rm -rf "$OUT"
mkdir -p "$OUT/note"

# The note: validate, then transform
xmllint --noout --valid --noent note/ubl-examples-method.xml
xsltproc --nonet \
  --stringparam css.path "$ROOT/.oasis/db/spec-0.9/css/" \
  -o "$OUT/note/ubl-examples-method.html" \
  note/xsl/draft-note-html.xsl note/ubl-examples-method.xml
xmllint --noent --dropdtd note/ubl-examples-method.xml > "$OUT/note/ubl-examples-method.xml"

# Top bar, the same on every page; $2 is the page it is shown on
NAV_ITEMS="note/ubl-examples-method.html|Method releases.html|Releases history.html|History coverage.html|Coverage"
nav() { # root-prefix, current-page
  printf '<header class="topbar"><nav aria-label="Site">'
  home=""
  [ "$2" = index.html ] && home=' aria-current="page"'
  printf '<a class="brand" href="%sindex.html"%s>UBL Example Documents</a><ul>' "$1" "$home"
  section=$2
  [ "$section" = coverage-details.html ] && section=coverage.html  # sub-page of Coverage
  for item in $NAV_ITEMS; do
    href=${item%%|*}; label=${item#*|}
    cur=""
    [ "$href" = "$section" ] && cur=' aria-current="page"'
    printf '<li><a href="%s%s"%s>%s</a></li>' "$1" "$href" "$cur" "$label"
  done
  printf '</ul><a class="source" href="https://github.com/kduvekot/ubl-examples">Source</a></nav></header>'
}

# Markdown pages, with an "On this page" list when toc-depth is given
page() { # source, target, title, [toc-depth]
  toc=""
  [ -n "${4:-}" ] && toc="--toc --toc-depth=$4"
  pandoc -f gfm -t html5 -s --template=site/page.html $toc \
      -M pagetitle="$3" -V root="" -V nav="$(nav "" "$2")" "$1" |
    sed -E 's#href="(history/)?README\.md"#href="history.html"#g; s#href="element-coverage-details\.md"#href="coverage-details.html"#g' \
    > "$OUT/$2"
}
page history/README.md history.html "How the history was built" 2
page README.md releases.html "Releases" 3
page analysis/element-coverage.md coverage.html "Element coverage" 2
page analysis/element-coverage-details.md coverage-details.html "Element coverage: details" 3

cp site/site.css "$OUT/site.css"
nav "" index.html > "$OUT/.nav"
sed -e "/<!--NAV-->/r $OUT/.nav" -e "/<!--NAV-->/d" site/index.html > "$OUT/index.html"
rm "$OUT/.nav"
touch "$OUT/.nojekyll"
echo "site built in $OUT"
