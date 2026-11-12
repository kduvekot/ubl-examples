"""Shared helpers: locate the repository, fetch and verify the UBL 2.5 model and code lists, read code lists.

The UBL files are downloaded once into a cache directory outside the repository
($UBL_REVIEW_CACHE, else $XDG_CACHE_HOME/ubl-example-review, else ~/.cache/ubl-example-review).
"""
import glob
import hashlib
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
WORLD_CODELISTS = REPO / 'world' / 'codelists'
EXAMPLES = REPO / 'world' / 'examples'

MODEL_URL = 'https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/UBL-Entities-2.5.gc'
MODEL_SHA256 = 'c7df070e1a2927792a8a85103665924973d2559552ea87aa495ea7248fe988d1'
CODELIST_BASE = 'https://docs.oasis-open.org/ubl/os-UBL-2.5/cl/gc/default/'
CODELIST_FILES = [
    'AllowanceChargeReasonCode-2.4.gc', 'BinaryObjectMimeCode-2.4.gc', 'ChannelCode-2.4.gc',
    'CountryIdentificationCode-2.4.gc', 'CurrencyCode-2.4.gc', 'LanguageCode-2.4.gc',
    'PackagingTypeCode-2.4.gc', 'PaymentMeansCode-2.4.gc', 'TransportEquipmentTypeCode-2.4.gc',
    'TransportModeCode-2.4.gc', 'UnitOfMeasureCode-2.4.gc',
]


def cache_dir():
    d = os.environ.get('UBL_REVIEW_CACHE') or os.path.join(
        os.environ.get('XDG_CACHE_HOME') or os.path.expanduser('~/.cache'), 'ubl-example-review')
    Path(d, 'cl').mkdir(parents=True, exist_ok=True)
    return Path(d)


def _fetch(url, dest):
    """Download once; write to a temporary name first so a parallel run never reads a partial file."""
    if not dest.exists():
        print(f'downloading {url}', file=sys.stderr)
        tmp = dest.with_name(f'{dest.name}.{os.getpid()}.part')
        urllib.request.urlretrieve(url, tmp)
        os.replace(tmp, dest)


def model_path():
    p = cache_dir() / 'UBL-Entities-2.5.gc'
    _fetch(MODEL_URL, p)
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    if sha != MODEL_SHA256:
        p.unlink()
        sys.exit(f'UBL-Entities-2.5.gc has SHA-256 {sha}, expected {MODEL_SHA256}; file removed')
    return p


def codelist_paths():
    out = []
    for f in CODELIST_FILES:
        p = cache_dir() / 'cl' / f
        _fetch(CODELIST_BASE + f, p)
        out.append(p)
    # world lists come last so that they override the UBL defaults
    out += sorted(WORLD_CODELISTS.glob('*.gc')) + sorted((WORLD_CODELISTS / 'gc').glob('*.gc'))
    return out


def load_model():
    """Return (children, documents): children[(ObjectClass, ComponentName)] = row, documents[DocName] = ABIE row."""
    children, documents = {}, {}
    for row in ET.parse(model_path()).getroot().iter('Row'):
        r = {v.get('ColumnRef'): (v.findtext('SimpleValue') or '') for v in row.findall('Value')}
        if r['ComponentType'] == 'ABIE':
            if not r['ModelName'].startswith('UBL-CommonLibrary'):
                documents[r['ComponentName']] = r
        else:
            children[(r['ObjectClass'], r['ComponentName'])] = r
    return children, documents


def load_codelists():
    """Return (by_stem, by_list_id): each maps to {code: name}."""
    by_stem, by_id = {}, {}
    for f in codelist_paths():
        root = ET.parse(f).getroot()
        ident = root.find('Identification')
        stem = ident.findtext('ShortName')
        codes = {}
        for row in root.iter('Row'):
            v = {x.get('ColumnRef'): (x.findtext('SimpleValue') or '') for x in row.findall('Value')}
            codes[v.get('code', '')] = v.get('name') or v.get('description', '')
        by_stem[stem] = codes
        for ln in ident.findall('LongName'):
            if ln.get('Identifier') == 'listID':
                by_id[ln.text] = codes
    return by_stem, by_id
