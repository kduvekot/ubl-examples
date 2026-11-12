"""Layer 0: XSD-minimal UBL 2.5 documents.

Only the elements (minOccurs >= 1) and attributes (use="required") the
schemas demand, with one fixed value per unqualified data type.
Fetches the UBL 2.5 package from OASIS into minimal/.ubl/ (not committed)
and writes xml/<DocType>.xml (endorsed) and xml/deprecated/<DocType>.xml.
Self-contained: uses nothing else from this repository.

Usage: python3 minimal/gen_minimal.py
"""
import os, glob, io, urllib.request, zipfile
from lxml import etree

XS = "http://www.w3.org/2001/XMLSchema"
X = "{%s}" % XS
HERE = os.path.dirname(os.path.abspath(__file__))
ZIP_URL = "https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.zip"
UBL = os.path.join(HERE, ".ubl", "os-UBL-2.5")
if not os.path.isdir(UBL):
    with urllib.request.urlopen(ZIP_URL) as r:
        zipfile.ZipFile(io.BytesIO(r.read())).extractall(os.path.join(HERE, ".ubl"))
xsd_dir = os.path.join(UBL, "xsd")
endorsed = {os.path.basename(f) for f in glob.glob(os.path.join(UBL, "endorsed", "xsd", "maindoc", "*.xsd"))}
out = os.path.join(HERE, "xml")

# One value per UDT data type (UBL's unqualified data types).
VALUES = {
    "AmountType": "0", "BinaryObjectType": "AA==", "GraphicType": "AA==",
    "PictureType": "AA==", "SoundType": "AA==", "VideoType": "AA==",
    "CodeType": "X", "DateTimeType": "2000-01-01T00:00:00", "DateType": "2000-01-01",
    "TimeType": "00:00:00", "IdentifierType": "X", "IndicatorType": "true",
    "MeasureType": "0", "NumericType": "0", "ValueType": "0", "PercentType": "0",
    "RateType": "0", "QuantityType": "0", "TextType": "X", "NameType": "X",
}
ATTRS = {"currencyID": "XXX", "unitCode": "X", "mimeCode": "X"}

schemas = {}  # targetNamespace -> list of schema roots
for f in glob.glob(os.path.join(xsd_dir, "common", "*.xsd")) + glob.glob(os.path.join(xsd_dir, "maindoc", "*.xsd")):
    r = etree.parse(f).getroot()
    schemas.setdefault(r.get("targetNamespace"), []).append(r)

def qname(node, ref):
    p, _, local = ref.rpartition(":")
    return node.nsmap.get(p or None), local

def find(kind, ns, name):
    for r in schemas.get(ns, []):
        for d in r.findall(X + kind):
            if d.get("name") == name:
                return d
    raise KeyError((kind, ns, name))

def udt_name(ctype_ns, ctype):
    """Follow derivation until a UDT type is reached."""
    udt = "urn:oasis:names:specification:bdndr:schema:xsd:UnqualifiedDataTypes-1"
    while ctype_ns != udt:
        t = find("complexType", ctype_ns, ctype)
        base = t.find(".//" + X + "restriction") if t.find(".//" + X + "extension") is None else t.find(".//" + X + "extension")
        ctype_ns, ctype = qname(base, base.get("base"))
    return ctype

def required_attrs(t):
    out = {}
    for a in t.iter(X + "attribute"):
        if a.get("use") == "required":
            out[a.get("name")] = ATTRS[a.get("name")]
    return out

def build(parent, el_decl):
    """el_decl: a global xsd:element. Append an instance to parent."""
    ns = el_decl.getparent().get("targetNamespace")
    e = etree.SubElement(parent, "{%s}%s" % (ns, el_decl.get("name")))
    tns, tname = qname(el_decl, el_decl.get("type"))
    t = find("complexType", tns, tname)
    if t.find(X + "simpleContent") is not None:
        u = udt_name(tns, tname)
        e.text = VALUES[u]
        attrs = {}
        cur_ns, cur = tns, tname
        while True:  # collect required attributes along the derivation chain
            ct = find("complexType", cur_ns, cur)
            attrs.update(required_attrs(ct))
            der = ct.find(".//" + X + "extension")
            if der is None: der = ct.find(".//" + X + "restriction")
            b_ns, b = qname(der, der.get("base"))
            if b_ns == XS: break
            cur_ns, cur = b_ns, b
        for k, v in attrs.items(): e.set(k, v)
    else:
        content(e, t)
    return e

def content(e, t):
    for child in t:
        if child.tag in (X + "sequence", X + "choice"):
            if child.get("minOccurs") == "0": continue
            if child.tag == X + "choice":
                raise NotImplementedError("required choice in %s" % t.get("name"))
            for p in child:
                if p.tag == X + "element" and p.get("minOccurs", "1") != "0":
                    ns, name = qname(p, p.get("ref"))
                    build(e, find("element", ns, name))
                elif p.tag in (X + "sequence", X + "choice", X + "any") and p.get("minOccurs", "1") != "0":
                    raise NotImplementedError(p.tag)

os.makedirs(os.path.join(out, "deprecated"), exist_ok=True)
for f in sorted(glob.glob(os.path.join(xsd_dir, "maindoc", "UBL-*-2.5.xsd"))):
    r = etree.parse(f).getroot()
    ns = r.get("targetNamespace")
    root_decl = r.find(X + "element")
    name = root_decl.get("name")
    nsmap = {None: ns,
             "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
             "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"}
    doc = etree.Element("{%s}%s" % (ns, name), nsmap=nsmap)
    t = find("complexType", *qname(root_decl, root_decl.get("type")))
    content(doc, t)
    etree.cleanup_namespaces(doc)  # drop cac/cbc where unused
    etree.ElementTree(doc).write(os.path.join(out, "" if os.path.basename(f) in endorsed else "deprecated", name + ".xml"), xml_declaration=True,
                                 encoding="UTF-8", pretty_print=True)
