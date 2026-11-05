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

# Markdown pages
page() { # source, target, title
  pandoc -f gfm -t html5 -s --metadata title="$3" -c site.css "$1" |
    sed -E 's#href="(history/)?README\.md"#href="history.html"#g; s#href="element-coverage-details\.md"#href="coverage-details.html"#g' \
    > "$OUT/$2"
}
page history/README.md history.html "History of the OASIS UBL sample documents"
page README.md releases.html "Releases"
page analysis/element-coverage.md coverage.html "UBL 2.5 element coverage"
page analysis/element-coverage-details.md coverage-details.html "UBL 2.5 element coverage: details"

cp site/site.css "$OUT/site.css"
cp site/index.html "$OUT/index.html"
touch "$OUT/.nojekyll"
echo "site built in $OUT"
