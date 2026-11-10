#!/bin/sh
# Fetch what validating the example documents needs from the UBL 2.5 OASIS
# Standard, into .ubl/ (not committed):
#   endorsed/xsdrt   the runtime schemas of the endorsed document types only
#                    (no deprecated ones), for phase 1 (XSD validation)
#   val/             UBL-DefaultDTQ-2.5.xsl and Saxon HE, for phase 2 with the
#                    UBL default code lists, exactly as UBL's own validate.sh
#   cva/             the context/value associations, for phase 2 with the
#                    world's code lists (tools/validate_examples.py)
# Usage: sh tools/fetch_ubl_validation.sh DocumentType...
set -e
BASE=https://docs.oasis-open.org/ubl/os-UBL-2.5
DIR="$(cd "$(dirname "$0")/.." && pwd)/.ubl"
get() { [ -s "$DIR/$1" ] || { mkdir -p "$(dirname "$DIR/$1")"; curl -sSf -o "$DIR/$1" "$BASE/$1"; }; }
for f in BDNDR-CCTS_CCT_SchemaModule-1.1 BDNDR-UnqualifiedDataTypes-1.1 UBL-CommonAggregateComponents-2.5 \
         UBL-CommonBasicComponents-2.5 UBL-CommonExtensionComponents-2.5 UBL-CommonSignatureComponents-2.5 \
         UBL-ExtensionContentDataType-2.5 UBL-QualifiedDataTypes-2.5 UBL-SignatureAggregateComponents-2.5 \
         UBL-SignatureBasicComponents-2.5 UBL-XAdES01903v132-201601-2.5 UBL-XAdES01903v141-201601-2.5 \
         UBL-xmldsig-core-schema-2.5 UBL-xmldsig1-schema-2.5 UBL-xmldsig11-schema-2.5; do
  get "endorsed/xsdrt/common/$f.xsd"
done
for d in "$@"; do get "endorsed/xsdrt/maindoc/UBL-$d-2.5.xsd"; done
get val/UBL-DefaultDTQ-2.5.xsl
get val/saxon9he.jar
get cva/UBL-DefaultDTQ-2.5.cva
echo "UBL 2.5 validation files in .ubl"
