#!/bin/sh
# Build the documentation site into a folder (default: _site).
#
#   _site/index.html                  home: the world
#   _site/world.html, map-sheet.html  the map, and the printed map sheet (A3, 1 : 2,500,000)
#   _site/examples.html, example-*    Trade: the flows and their documents, with the reason for every value
#   _site/parties.html, world-<id>.html  Parties: the index and a page per party
#   _site/world-specifications.html, world-spec-*, world-codelists.html  Rules: specifications and code lists
#   _site/about.html                  About: the project
#   _site/note/                       the method note (DocBook -> HTML, OASIS stylesheets)
#   _site/coverage.html               element coverage of the world's documents (computed at every build)
#   _site/coverage-details.html       every missing element
#   _site/releases.html, history.html the OASIS sample documents: releases, and how their history was built
#   _site/examples/<flow>/*.xml       the example documents themselves
#
# Usage: tools/build_site.sh [out-dir]
# Requires: xsltproc, xmllint, pandoc; fetches the OASIS stylesheets into .oasis
set -eu
export LC_ALL=C.UTF-8   # pandoc reads the header and footer from its arguments, in the locale's encoding
cd "$(dirname "$0")/.."
OUT=${1:-_site}
ROOT=$(pwd)

tools/fetch_oasis_stylesheets.sh .oasis
tools/md2docbook.sh --check
# The tile model of the world, made once by the world check, for the map sheet below (outside $OUT, which is made anew)
MODEL=$(mktemp)
trap 'rm -f "$MODEL"' EXIT
python3 tools/check_world.py --model "$MODEL"   # includes tools/terrain.py --check: the committed terrain is made from its current inputs
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
BUILT_SHA=$(git rev-parse HEAD 2>/dev/null || echo "")
BUILT_DATE=$(TZ=UTC git log -1 --format=%cd --date=format-local:'%Y-%m-%d %H:%M UTC' 2>/dev/null || echo "")

# Header, the same on every page; $2 is the page it is shown on
NAV_ITEMS="world.html|World examples.html|Trade parties.html|Parties world-specifications.html|Rules about.html|About"
CODE_ICON='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>'
nav() { # root-prefix, current-page
  section=$2
  case "$section" in
    map-sheet.html) section=world.html ;;                               # the map sheet belongs to World
    example-*.html) section=examples.html ;;                            # the documents belong to Trade
    world-spec*.html|world-codelists.html) section=world-specifications.html ;;  # specifications and code lists: Rules
    world-*.html) section=parties.html ;;                               # a party's page belongs to Parties
    coverage*.html|releases.html|history.html) section=about.html ;;    # the project's pages belong to About
  esac
  printf '<header class="site-header"><div class="bar">'
  printf '<a class="brand" href="%sindex.html" title="The UBL World: home">UBL <span>World</span></a>' "$1"
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
  printf '<p>A fictional world, made to show UBL 2.5 in use. Work in progress, not an OASIS publication. UBL is an OASIS Standard and ISO/IEC 19845. <a href="%sabout.html">About this project</a></p>' "${1:-}"
  if [ -n "$BUILT_SHA" ]; then
    printf '<p><a href="https://github.com/kduvekot/ubl-examples">Source on GitHub</a> · built from commit <a href="https://github.com/kduvekot/ubl-examples/commit/%s"><code>%s</code></a> of %s</p>' "$BUILT_SHA" "$BUILT" "$BUILT_DATE"
  else
    printf '<p><a href="https://github.com/kduvekot/ubl-examples">Source on GitHub</a> · built from <code>%s</code></p>' "$BUILT"
  fi
  printf '</div></footer>'
}

# Markdown pages, with an "On this page" list when toc-depth is given
page() { # source, target, title, [toc-depth]
  toc=""
  [ -n "${4:-}" ] && toc="--toc --toc-depth=$4"
  pandoc -f gfm -t html5 -s --template=site/page.html $toc \
      -M pagetitle="$3" -V root="" -V cssv="$CSSV" -V nav="$(nav "" "$2")" -V footer="$(footer)" "$1" > "$OUT/$2.pandoc"
  sed -E 's#href="(history/)?README\.md"#href="history.html"#g; s#href="element-coverage-details\.md"#href="coverage-details.html"#g; s#href="manifest\.json"#href="https://github.com/kduvekot/ubl-examples/blob/main/history/manifest.json"#g' \
    "$OUT/$2.pandoc" > "$OUT/$2"
  rm "$OUT/$2.pandoc"
}
# The many pages of the loops are converted side by side, up to one per processor (BUILD_JOBS sets the number):
# bg starts a command in the background, waiting first for the oldest when that many run; bg_wait waits for all of
# them and stops the build when any of them failed
JOBS=${BUILD_JOBS:-$(nproc 2>/dev/null || getconf _NPROCESSORS_ONLN 2>/dev/null || echo 1)}
PIDS=""
BG_FAILED=0
bg() {
  "$@" &
  PIDS="$PIDS $!"
  set -- $PIDS
  if [ $# -ge "$JOBS" ]; then
    wait "$1" || BG_FAILED=1
    shift
    PIDS="$*"
  fi
}
bg_wait() {
  for pid in $PIDS; do wait "$pid" || BG_FAILED=1; done
  PIDS=""
  [ "$BG_FAILED" = 0 ] || { echo "a page conversion failed" >&2; exit 1; }
}
page history/README.md history.html "The OASIS sample documents: how the history was built" 2
page README.md releases.html "The OASIS sample documents: releases" 3
page site/about.md about.html "About this project"
# Element coverage of the world's documents, computed at every build (tools/coverage_world.sh)
sh tools/coverage_world.sh "$OUT/.coverage.md" > /dev/null
coverage=$(sed -n 's/^| All | [0-9]* | [0-9]* | [0-9]* | \([0-9.]*%\) |$/\1/p' "$OUT/.coverage.md")
doctypes=$(sed -n 's/^Document types with at least one example: \([0-9]* of [0-9]*\)\.$/\1/p' "$OUT/.coverage.md")
[ -n "$coverage" ] && [ -n "$doctypes" ] || { echo "coverage figures not found in the coverage report" >&2; exit 1; }
dt_used=${doctypes%% of *}; dt_all=${doctypes##* of }
if [ "$dt_used" = "$dt_all" ]; then doctypes="all $dt_all"; fi
python3 - "$OUT/.coverage.md" "$OUT/.coverage-summary.md" "$OUT/.coverage-details.md" <<'COV'
import re, sys
src, summary, details = sys.argv[1:]
text = open(src, encoding="utf-8").read()
text = re.sub(r"^# .*\n", "", text, count=1)
text = re.sub(r"^Model: .*\n", "", text, flags=re.M)
head, sep, rest = text.partition("\n## Missing elements per placement")
intro = ("The endorsed elements of UBL 2.5 that the documents of the world use: every document type, aggregate "
         "and basic element the UBL 2.5 model allows, without what it deprecates. An element is added only through "
         "a real business situation in the world, never as a filler, so some stay out on purpose. "
         "[Every missing element](coverage-details.html) is listed with where it fits.\n")
open(summary, "w", encoding="utf-8").write("# Element coverage\n\n" + intro + head)
open(details, "w", encoding="utf-8").write("# Element coverage: the missing elements\n\n"
                                           "[The summary](coverage.html)\n" + sep + rest)
COV
page "$OUT/.coverage-summary.md" coverage.html "Element coverage" 2
page "$OUT/.coverage-details.md" coverage-details.html "Element coverage: the missing elements" 3
rm -f "$OUT/.coverage.md" "$OUT/.coverage-summary.md" "$OUT/.coverage-details.md"
# The printed map sheet (O151): the A3 sheet at 1 : 2,500,000, drawn from the world data at every build
# (analysis/world-position/refine_map.py; needs numpy, Pillow and the DejaVu fonts), so it always matches the map
# (tools/map_sheet.py: drawn only when one of its inputs changed, else taken from the cache, $BUILD_CACHE or .cache)
python3 tools/map_sheet.py "$MODEL" "$OUT/map-sheet.png"
rm -f "$MODEL"
cat > "$OUT/.map-sheet.md" <<'SHEET'
# The map sheet

The printed map of the example world: an A3 landscape sheet at 1 : 2,500,000, drawn
from the same terrain, places and routes as the [interactive map](world.html). It
shows the landscape, the towns and villages, the roads, railways and pipelines, and
the border between Urvania and Bayvarra. Lisavu, about 1,100 km east of Lumeport,
stands in a panel of its own at the same scale.

[Open the sheet at full size](map-sheet.png) (4,961 × 3,508 pixels, 300 dpi, about 6 MB).

[![The A3 map sheet of the example world](map-sheet.png)](map-sheet.png)
SHEET
page "$OUT/.map-sheet.md" map-sheet.html "The map sheet"
rm -f "$OUT/.map-sheet.md"

cp site/site.css "$OUT/site.css"
mkdir -p "$OUT/codelists/gc" && cp world/codelists/*.gc "$OUT/codelists/"   # the world code lists, at their LocationUri
cp world/codelists/gc/*.gc "$OUT/codelists/gc/" && cp world/codelists/UBL-World-2.5.cva "$OUT/codelists/"
# The folder's own address leads to the index of the code lists
printf '<!doctype html><meta charset="utf-8"><title>Code lists</title><meta http-equiv="refresh" content="0; url=../world-codelists.html"><link rel="canonical" href="../world-codelists.html"><a href="../world-codelists.html">The code lists of the UBL World</a>\n' > "$OUT/codelists/index.html"
# The world: the map with its data, and a page per party
python3 tools/build_world.py "$OUT" "$OUT/.world-md"
# The home page's picture of the world: the 3D map as it opens (tools/map_still.py: a headless Chrome)
# Where no Chrome can take it, the printed sheet stands in, with a warning (in GitHub Actions too)
python3 tools/map_still.py "$OUT/world.html" "$OUT/world-preview.jpg" || {
  echo "::warning::no picture of the 3D map: the home page shows the map sheet instead" >&2
  python3 -c "import sys; from PIL import Image; im = Image.open(sys.argv[1]).convert('RGB'); im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS).save(sys.argv[2], quality=82, optimize=True, progressive=True)" "$OUT/map-sheet.png" "$OUT/world-preview.jpg"; }
for md in "$OUT"/.world-md/*.md; do
  name=$(basename "$md" .md)
  bg page "$md" "$name.html" "$(sed -n '1s/^# //p' "$md")"
done
bg_wait
rm -rf "$OUT/.world-md"
# The Encyclopedia (/wiki/): articles made from the world data (tools/build_wiki.py), in a look of its own
python3 tools/build_wiki.py "$OUT/.wiki-md"
mkdir -p "$OUT/wiki" && cp site/wiki.css "$OUT/wiki/wiki.css"
WCSSV=$(sha256sum site/wiki.css | cut -c1-10)
for md in "$OUT"/.wiki-md/*.md; do
  name=$(basename "$md" .md)
  bg pandoc -f gfm -t html5 -s --template=site/wiki.html -M pagetitle="$(sed -n '1s/^# //p' "$md")" -V cssv="$WCSSV" \
    "$md" -o "$OUT/wiki/$name.html"
done
bg_wait
rm -rf "$OUT/.wiki-md"
# The example documents: a page per document (values and reasons), and the XML files themselves
# (build_world.py adds to each page its place in the flow's story, its neighbours, parties and specification)
for md in "$OUT"/.example-md/*/*.md; do
  flow=$(basename "$(dirname "$md")"); name=$(basename "$md" .md)
  mkdir -p "$OUT/examples/$flow" && cp "world/examples/$flow/$name.xml" "$OUT/examples/$flow/"
  sed "s#](\($name\.xml\))#](examples/$flow/\1)#" "$md" > "$md.page"
  bg page "$md.page" "example-$flow-$name.html" "$(sed -n '1s/^# //p' "$md")"
done
bg_wait
rm -rf "$OUT/.example-md"
# Landing page: header, footer and key figures filled in
nav "" index.html > "$OUT/.nav"
footer > "$OUT/.footer"
# The world in figures, from the world's data and the coverage report; the build stops when one is missing
set -- $(python3 -c "
import sys; sys.path.insert(0, 'tools'); import world_data
w = world_data.load(); world_data.number_documents(w)
print(len(w['parties']), sum(1 for f in w['flows'] if any(d['flow'] == f['id'] for d in w['documents'])), len(w['documents']))")
n_parties=$1; n_flows=$2; n_documents=$3
preview_h=$(python3 -c "from PIL import Image; print(Image.open('$OUT/world-preview.jpg').height)")
for v in "$n_parties" "$n_flows" "$n_documents" "$preview_h"; do [ -n "$v" ] || { echo "a figure of the home page is missing" >&2; exit 1; }; done
sed -e "/<!--NAV-->/r $OUT/.nav" -e "/<!--NAV-->/d" \
    -e "/<!--FOOTER-->/r $OUT/.footer" -e "/<!--FOOTER-->/d" \
    -e "s/{{parties}}/$n_parties/; s/{{flows}}/$n_flows/; s/{{documents}}/$n_documents/; s/{{doctypes}}/$doctypes/" \
    -e "s/{{coverage}}/$coverage/; s/{{preview_h}}/$preview_h/; s/{{cssv}}/$CSSV/" \
    site/index.html > "$OUT/index.html"
grep -q '{{' "$OUT/index.html" && { echo "a placeholder of the home page is not filled in" >&2; exit 1; }
rm "$OUT/.nav" "$OUT/.footer"
# The published text states the world as fact: no internal references (the two-layer rule)
python3 tools/check_published.py "$OUT"
touch "$OUT/.nojekyll"
echo "site built in $OUT"
