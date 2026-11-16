import glob
from lxml import etree
NS={'cac':'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2','cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'}
def docs():
    for f in sorted(glob.glob('/home/user/ubl-examples/world/examples/*/*.xml')):
        t=etree.parse(f)
        yield f.split('world/examples/')[1], t, t.getroot()
def ln(e): return etree.QName(e).localname
def txt(e,p):
    r=e.xpath(p,namespaces=NS)
    return ' | '.join((x.text or '').strip() if hasattr(x,'text') else str(x) for x in r)
def path(t,e):
    p=t.getpath(e)
    return p
def cpath(t,e):
    # path with prefixes
    parts=[]
    while e is not None and e.getparent() is not None:
        par=e.getparent()
        q=etree.QName(e)
        pre={'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2':'cac','urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2':'cbc'}.get(q.namespace,'')
        name=(pre+':' if pre else '')+q.localname
        sib=[s for s in par if s.tag==e.tag]
        if len(sib)>1: name+='[%d]'%(sib.index(e)+1)
        parts.append(name); e=par
    parts.append(etree.QName(e).localname)
    return '/'+'/'.join(reversed(parts))
def pcountry(root,role):
    for r in role:
        v=root.xpath('cac:%s//cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode/text()'%r if 'Party' not in r.split('/')[-1] or r.endswith('SupplierParty') or r.endswith('CustomerParty') else 'cac:%s/cac:PostalAddress/cac:Country/cbc:IdentificationCode/text()'%r,namespaces=NS)
        n=root.xpath('cac:%s//cac:PartyName/cbc:Name/text()'%r,namespaces=NS)
        if v: return v[0],(n[0] if n else '')
    return '',''
