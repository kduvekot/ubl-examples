#!/bin/sh
# Build the documentation site into a folder (default: _site).
#
#   _site/index.html                  landing page
#   _site/note/                       the note (DocBook -> HTML, OASIS stylesheets)
#   _site/history.html                how the examples history was built
#   _site/releases.html               README.md: releases and their changes
#   _site/coverage.html               element coverage analysis
#   _site/coverage-details.html       every missing element
#   _site/world.html, world-*.html    the example world: map and party pages
#   _site/examples.html, example-*    the example documents, with the reason for every value
#   _site/examples/<flow>/*.xml       the example documents themselves
#
# Usage: tools/build_site.sh [out-dir]
# Requires: xsltproc, xmllint, pandoc; fetches the OASIS stylesheets into .oasis
set -eu
cd "$(dirname "$0")/.."
OUT=${1:-_site}
ROOT=$(pwd)

tools/fetch_oasis_stylesheets.sh .oasis
tools/md2docbook.sh --check
python3 tools/check_world.py
# The example documents: up to date with the world, and valid (UBL schemas, code lists)
python3 tools/build_examples.py --check
sh tools/fetch_ubl_validation.sh $(ls world/examples/*/*.xml | sed 's#.*/[0-9]*-\(.*\)\.xml#\1#' | sort -u)
python3 tools/validate_examples.py world/examples/*/*.xml

rm -rf "$OUT"
mkdir -p "$OUT/note"

# The note: validate, then transform
xmllint --noout --valid --noent note/ubl-examples-method.xml
xsltproc --nonet \
  --stringparam css.path "$ROOT/.oasis/db/spec-0.9/css/" \
  -o "$OUT/note/ubl-examples-method.html" \
  note/xsl/draft-note-html.xsl note/ubl-examples-method.xml
xmllint --noent --dropdtd note/ubl-examples-method.xml > "$OUT/note/ubl-examples-method.xml"

# Version of the stylesheet, so browsers fetch a new one at once
# (GitHub Pages lets browsers cache files for 10 minutes)
CSSV=$(sha256sum site/site.css | cut -c1-10)
BUILT=$(git rev-parse --short HEAD 2>/dev/null || echo local)

# Header, the same on every page; $2 is the page it is shown on
NAV_ITEMS="note/ubl-examples-method.html|Method world.html|World examples.html|Examples releases.html|Releases history.html|History coverage.html|Coverage"
LOGO='<svg class="logo" viewBox="0 0 32 32" aria-hidden="true"><rect x="3" y="6" width="17" height="21" rx="3" class="l1"/><rect x="8" y="3" width="17" height="21" rx="3" class="l2"/><rect x="13" y="8" width="16" height="21" rx="3" class="l3"/><path d="M17 15h8M17 19h8M17 23h5" class="l4"/></svg>'
CODE_ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>'
nav() { # root-prefix, current-page
  section=$2
  [ "$section" = coverage-details.html ] && section=coverage.html  # sub-page of Coverage
  case "$section" in world-*.html) section=world.html ;; esac       # party pages belong to World
  case "$section" in example-*.html) section=examples.html ;; esac  # example pages belong to Examples
  printf '<header class="site-header"><div class="bar">'
  printf '<a class="brand" href="%sindex.html">%s<span>UBL Example Documents</span></a>' "$1" "$LOGO"
  printf '<input type="checkbox" id="nav-toggle" class="nav-toggle"><label for="nav-toggle" class="nav-burger" title="Menu"><span></span><span class="visually-hidden">Menu</span></label>'
  printf '<nav class="site-nav" aria-label="Site"><ul>'
  for item in $NAV_ITEMS; do
    href=${item%%|*}; label=${item#*|}
    cur=""
    [ "$href" = "$section" ] && cur=' aria-current="page"'
    printf '<li><a href="%s%s"%s>%s</a></li>' "$1" "$href" "$cur" "$label"
  done
  printf '</ul></nav><a class="source" href="https://github.com/kduvekot/ubl-examples">%s<span>Source</span></a></div></header>' "$CODE_ICON"
}
footer() {
  printf '<footer class="site-footer"><div>'
  printf '<p>Work in progress. Not an OASIS publication. UBL is an OASIS Standard and ISO/IEC 19845.</p>'
  printf '<p><a href="https://github.com/kduvekot/ubl-examples">Source on GitHub</a> · built from <code>%s</code></p>' "$BUILT"
  printf '</div></footer>'
}

# Markdown pages, with an "On this page" list when toc-depth is given
page() { # source, target, title, [toc-depth]
  toc=""
  [ -n "${4:-}" ] && toc="--toc --toc-depth=$4"
  pandoc -f gfm -t html5 -s --template=site/page.html $toc \
      -M pagetitle="$3" -V root="" -V cssv="$CSSV" -V nav="$(nav "" "$2")" -V footer="$(footer)" "$1" |
    sed -E 's#href="(history/)?README\.md"#href="history.html"#g; s#href="element-coverage-details\.md"#href="coverage-details.html"#g' \
    > "$OUT/$2"
}
page history/README.md history.html "How the history was built" 2
page README.md releases.html "Releases" 3
page analysis/element-coverage.md coverage.html "Element coverage" 2
page analysis/element-coverage-details.md coverage-details.html "Element coverage: details" 3

cp site/site.css "$OUT/site.css"
mkdir -p "$OUT/codelists/gc" && cp world/codelists/*.gc "$OUT/codelists/"   # the world code lists, at their LocationUri
cp world/codelists/gc/*.gc "$OUT/codelists/gc/" && cp world/codelists/UBL-World-2.5.cva "$OUT/codelists/"
# The world: the map with its data, and a page per party
python3 tools/build_world.py "$OUT" "$OUT/.world-md"
for md in "$OUT"/.world-md/*.md; do
  name=$(basename "$md" .md)
  page "$md" "$name.html" "$(sed -n '1s/^# //p' "$md")"
done
rm -rf "$OUT/.world-md"
# The example documents: a page per document (values and reasons), and the XML files themselves
for md in world/examples/*/*.md; do
  flow=$(basename "$(dirname "$md")"); name=$(basename "$md" .md)
  mkdir -p "$OUT/examples/$flow" && cp "world/examples/$flow/$name.xml" "$OUT/examples/$flow/"
  sed "s#](\($name\.xml\))#](examples/$flow/\1)#" "$md" > "$OUT/.example.md"
  page "$OUT/.example.md" "example-$flow-$name.html" "$(sed -n '1s/^# //p' "$md")"
done
rm -f "$OUT/.example.md"
# Landing page: header, footer and key figures filled in
nav "" index.html > "$OUT/.nav"
footer > "$OUT/.footer"
n_releases=$(grep -c '^### ' README.md)
n_examples=$(ls xml/*.xml | wc -l)
n_doctypes=$(sed -n 's/.*Document types with an example:\*\* \([0-9]*\) of.*/\1/p' analysis/element-coverage.md)
coverage=$(sed -n 's/^| \*\*All\*\* |.*| \*\*\([0-9]*%\)\*\* |$/\1/p' analysis/element-coverage.md)
sed -e "/<!--NAV-->/r $OUT/.nav" -e "/<!--NAV-->/d" \
    -e "/<!--FOOTER-->/r $OUT/.footer" -e "/<!--FOOTER-->/d" \
    -e "s/{{releases}}/$n_releases/; s/{{examples}}/$n_examples/; s/{{doctypes}}/$n_doctypes/; s/{{coverage}}/$coverage/; s/{{cssv}}/$CSSV/" \
    site/index.html > "$OUT/index.html"
rm "$OUT/.nav" "$OUT/.footer"
touch "$OUT/.nojekyll"
echo "site built in $OUT"
