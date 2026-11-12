"""Layer 0: XSD-minimal UBL 2.5 documents.

Only the elements (minOccurs >= 1) and attributes (use="required") the
schemas demand, with one fixed value per unqualified data type.
Fetches the UBL 2.5 package from OASIS into minimal/.ubl/ (not committed)
and writes xml/<DocType>.xml (endorsed) and xml/deprecated/<DocType>.xml.
Self-contained: uses nothing else from this repository.

After writing, every document is checked against the UBL 2.5 rules of
chapter 4, "Additional Document Constraints" (IND1-IND9, see check()).
The script exits with status 1 and lists every violation if one fails.

Usage: python3 minimal/gen_minimal.py               generate and check
       python3 minimal/gen_minimal.py --check FILE...  only check FILEs
"""
import os, re, sys, glob, io, subprocess, tempfile, urllib.request, zipfile
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
ATTRS = {"mimeCode": "X"}

# Currency: one per document (every currency code and currencyID in it),
# varied across the set by turns in alphabetical document order.
CURRENCIES = ["USD", "EUR", "JPY", "INR", "BRL", "ZAR"]
CUR = "@CURRENCY@"  # placeholder, replaced per document

# Unit per Measure element, chosen from the element's UBL definition. No
# default: a Measure not listed here stops the build until a unit is chosen.
UNITS = {
    # ExceptionNotificationLine: the compared value and the source value it
    # is compared with count the line's SupplyItem, so the same unit: piece.
    "ComparedValueMeasure": "H87",
    "SourceValueMeasure": "H87",
}

# Optional children added to an aggregate type on purpose (UBL 2.5 chapter 4).
# PeriodType: both StartDate and EndDate. A period with only a start would be
# "open-ended" by absence of its end, which IND6 forbids.
# TransportMeansType ("a particular vehicle or vessel"): only the mode-specific
# aggregates identify the vehicle; road is the simplest (its required
# LicensePlateID follows from the schema).
FILL = {"PeriodType": {"cbc:StartDate", "cbc:EndDate"},
        "TransportMeansType": {"cac:RoadTransport"},
        # TenderedProjectType: the project is identified by the Tender's
        # ContractFolderID; the content is the bid, "the total amount for
        # this tendered project" (its PayableAmount follows from the schema).
        "TenderedProjectType": {"cac:LegalMonetaryTotal"}}

schemas = {}  # targetNamespace -> list of schema roots
for f in glob.glob(os.path.join(xsd_dir, "common", "*.xsd")) + glob.glob(os.path.join(xsd_dir, "maindoc", "*.xsd")):
    r = etree.parse(f).getroot()
    schemas.setdefault(r.get("targetNamespace"), []).append(r)

QDT = "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDataTypes-2"

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
            out[a.get("name")] = ATTRS.get(a.get("name"))
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
            if (cur_ns, cur) == (QDT, "CurrencyCodeType"):
                e.text = CUR
            ct = find("complexType", cur_ns, cur)
            attrs.update(required_attrs(ct))
            der = ct.find(".//" + X + "extension")
            if der is None: der = ct.find(".//" + X + "restriction")
            b_ns, b = qname(der, der.get("base"))
            if b_ns == XS: break
            cur_ns, cur = b_ns, b
        if "currencyID" in attrs:
            attrs["currencyID"] = CUR
        if "unitCode" in attrs:
            if el_decl.get("name") not in UNITS:
                raise KeyError("no unit chosen for " + el_decl.get("name"))
            attrs["unitCode"] = UNITS[el_decl.get("name")]
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
                if p.tag == X + "element" and (p.get("minOccurs", "1") != "0"
                                               or p.get("ref") in FILL.get(t.get("name"), ())):
                    ns, name = qname(p, p.get("ref"))
                    build(e, find("element", ns, name))
                elif p.tag in (X + "sequence", X + "choice", X + "any") and p.get("minOccurs", "1") != "0":
                    raise NotImplementedError(p.tag)

def generate():
    os.makedirs(os.path.join(out, "deprecated"), exist_ok=True)
    n_cur = 0
    written = []
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
        uses = [e for e in doc.iter() if e.text == CUR or e.get("currencyID") == CUR]
        if uses:
            currency = CURRENCIES[n_cur % len(CURRENCIES)]
            n_cur += 1
            for e in uses:
                if e.text == CUR: e.text = currency
                if e.get("currencyID") == CUR: e.set("currencyID", currency)
        path = os.path.join(out, "" if os.path.basename(f) in endorsed else "deprecated", name + ".xml")
        with open(path, "wb") as fh:  # declaration exactly as the IND2/IND3 example
            fh.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            fh.write(etree.tostring(doc, encoding="UTF-8", pretty_print=True))
        written.append((path, f))
    return written

# --- Checks: UBL 2.5 chapter 4, Additional Document Constraints -------------
# IND6 (absence carries no meaning) cannot be tested by machine; it is
# handled where values are chosen (see FILL).
CBC = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
CAC = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
TEXT_ELEMENTS = {  # cbc elements of "Text. Type" (TextType and NameType)
    d.get("name") for d in schemas[CBC][0].findall(X + "element")
    if udt_name(*qname(d, d.get("type"))) in ("TextType", "NameType")}

def check(path, xsd):
    errors = []
    raw = open(path, "rb").read()
    decl = re.match(rb'<\?xml[^>]*\?>', raw)
    enc = decl and re.search(rb'encoding=["\']([^"\']+)', decl.group(0))
    if not enc:  # IND2
        errors.append("IND2 no character encoding in the XML declaration")
    elif enc.group(1).upper() != b"UTF-8":  # IND3
        errors.append("IND3 encoding is %s, not UTF-8" % enc.group(1).decode())
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError as ex:
        errors.append("IND3 not valid UTF-8: %s" % ex)
    try:
        doc = etree.parse(path)
    except etree.XMLSyntaxError as ex:
        return errors + ["IND1 not well-formed: %s" % ex]
    schema = etree.XMLSchema(etree.parse(xsd))
    if not schema.validate(doc):  # IND1
        errors += ["IND1 %s" % e for e in schema.error_log]
    def path_of(e):
        steps = []
        while e is not None:
            q = etree.QName(e)
            pre = {CBC: "cbc:", CAC: "cac:"}.get(q.namespace, "")
            sib = [s for s in (e.getparent() if e.getparent() is not None else []) if s.tag == e.tag]
            steps.append(pre + q.localname + ("[%d]" % (sib.index(e) + 1) if len(sib) > 1 else ""))
            e = e.getparent()
        return "/" + "/".join(reversed(steps))
    for e in doc.iter(etree.Element):
        where = path_of(e)
        if len(e) == 0 and not (e.text or "").strip():  # IND5
            errors.append("IND5 empty element %s" % where)
        for k, v in e.attrib.items():  # IND9
            if not v.strip():
                errors.append("IND9 empty attribute %s/@%s" % (where, k))
        seen = {}  # IND7, IND8: repeated Text siblings of the same name
        for c in e:
            q = etree.QName(c)
            if q.namespace == CBC and q.localname in TEXT_ELEMENTS:
                seen.setdefault(q.localname, []).append(c.get("languageID"))
        for n, langs in seen.items():
            if len(langs) > 1:
                if langs.count(None) > 1:
                    errors.append("IND8 %s/cbc:%s: more than one without languageID" % (where, n))
                dup = {l for l in langs if l is not None and langs.count(l) > 1}
                if dup:
                    errors.append("IND7 %s/cbc:%s: languageID repeated: %s" % (where, n, ", ".join(sorted(dup))))
    return errors

def phase2(paths):
    """IND1 section's recommended second phase: UBL default code lists,
    with the package's own XSLT and Saxon, as in val/validate.sh."""
    val = os.path.join(UBL, "val")
    errors = {}
    with tempfile.TemporaryDirectory() as tmp:
        src, res = os.path.join(tmp, "in"), os.path.join(tmp, "out")
        os.makedirs(src); os.makedirs(res)
        for i, p in enumerate(paths):  # one Saxon run for all files
            os.symlink(os.path.abspath(p), os.path.join(src, "%04d.xml" % i))
        r = subprocess.run(["java", "-jar", os.path.join(val, "saxon9he.jar"), "-s:" + src,
                            "-o:" + res, "-xsl:" + os.path.join(val, "UBL-DefaultDTQ-2.5.xsl")],
                           capture_output=True, text=True)
        for i, p in enumerate(paths):
            o = os.path.join(res, "%04d.xml" % i)
            if not os.path.exists(o):
                errors[p] = ["code list: not checked: " + (r.stderr.strip().splitlines() or ["?"])[-1]]
                continue
            msgs = re.findall(r"<svrl:text>(.*?)</svrl:text>", open(o, encoding="utf-8").read(), re.S)
            if msgs:
                errors[p] = ["code list: " + " ".join(m.split()) for m in msgs]
    return errors

def xsd_for(path):
    try:
        name = etree.QName(etree.parse(path).getroot()).localname
    except etree.XMLSyntaxError:
        name = "Invoice"  # not parseable; check() reports it
    return os.path.join(xsd_dir, "maindoc", "UBL-%s-2.5.xsd" % name)

if sys.argv[1:2] == ["--check"]:
    written = [(p, xsd_for(p)) for p in sys.argv[2:]]
else:
    written = generate()
failed = {}
for path, xsd in written:
    errs = check(path, xsd)
    if errs:
        failed[path] = errs
for p, errs in phase2([p for p, _ in written]).items():
    failed.setdefault(p, []).extend(errs)
for p in sorted(failed):
    print(os.path.relpath(p))
    for e in failed[p]:
        print("  " + e)
print("%d documents, %d with violations" % (len(written), len(failed)))
sys.exit(1 if failed else 0)
