"""Shared by check_xpaths.py and check_values.py: find the XPaths a review cites and resolve them.

A review cites an element in one of two ways, always between backticks:
  `/Root/cac:…/cbc:…`                      an absolute path: in the reviewed example, or, if it does not
                                           resolve there, in the other examples of the same flow with
                                           that root element
  `<flow>/NN-DocumentType.xml:/Root/…`     a path in a named example, also in another flow
  `NN-DocumentType.xml:/Root/…`            a path in a named example of the same flow
Paths containing '…' are shorthand and are skipped.
"""
import re
from pathlib import Path

from lxml import etree

NS = {'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
      'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
      'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'}
CITATION = re.compile(r'`((?:[\w.-]+/)?[\w.-]+\.xml:)?(/[A-Za-z][^`\s]*)`')
_cache = {}


def review_xml(md):
    """The example a review file belongs to (final review or a run's part file)."""
    return Path(re.sub(r'\.llm-review(\.[^/]+)?\.md$', '.xml', str(md)))


def parse(xml_file):
    key = str(Path(xml_file).resolve())
    if key not in _cache:
        _cache[key] = etree.parse(key)
    return _cache[key]


def select(path, xml_file):
    """The elements (or attribute values) the path selects in the file."""
    doc = parse(xml_file)
    ns = dict(NS, d=doc.getroot().nsmap[None])
    q = re.sub(r'(^|/)([A-Z][A-Za-z]*)(?=/|\[|$)', lambda m: m.group(1) + 'd:' + m.group(2), path)
    return doc.xpath(q, namespaces=ns)


def root_name(xml_file):
    return etree.QName(parse(xml_file).getroot()).localname


def candidates(md, file_prefix, path):
    """The example files a citation may refer to, in order of preference."""
    xml = review_xml(md)
    flow = xml.parent
    if file_prefix:
        name = file_prefix[:-1]
        target = flow.parent / name if '/' in name else flow / name
        return [target]
    root = path.split('/')[1].split('[')[0]
    own = [xml] if root_name(xml) == root else []
    others = [f for f in sorted(flow.glob('*.xml')) if f.resolve() != xml.resolve() and root_name(f) == root]
    return own + others


def resolve(md, file_prefix, path):
    """(matches, files): for each candidate file where the path selects something, its selection."""
    hits = []
    for f in candidates(md, file_prefix, path):
        if f.exists():
            sel = select(path, f)
            if sel:
                hits.append((f, sel))
                if not file_prefix and f.resolve() == review_xml(md).resolve():
                    break  # the reviewed example itself wins
    return hits


def citations(md):
    """Every (file_prefix, path) cited in the review, without shorthand paths."""
    text = Path(md).read_text(encoding='utf-8')
    return sorted({(m.group(1) or '', m.group(2)) for m in CITATION.finditer(text) if '…' not in m.group(2)})


def value_citations(md):
    """Every `citation` = `value` pair in the review (the value as quoted, between backticks)."""
    text = Path(md).read_text(encoding='utf-8')
    pat = re.compile(r'`((?:[\w.-]+/)?[\w.-]+\.xml:)?(/[A-Za-z][^`\s]*)`\s*=\s*`([^`]*)`')
    return [(m.group(1) or '', m.group(2), m.group(3)) for m in pat.finditer(text) if '…' not in m.group(2)]


def text_of(node):
    if isinstance(node, str):
        return node.strip()
    return (node.text or '').strip()
