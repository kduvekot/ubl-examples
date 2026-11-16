import re,sys
from lxml import etree
NS={'cac':'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2','cbc':'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'}
txt=open(sys.argv[1]).read()
base='/home/user/ubl-examples/world/examples/'
cit=re.compile(r'`([a-z]+/\d\d-[A-Za-z]+\.xml):(/[^`]+)`(?:\s*=\s*`([^`]*)`)?')
n=bad=vals=vbad=0
cache={}
for m in cit.finditer(txt):
    f,xp,val=m.groups(); n+=1
    if f not in cache: cache[f]=etree.parse(base+f)
    t=cache[f]; root=t.getroot()
    # convert absolute path: replace root name with '/*[local-name()=..]'
    parts=xp.split('/')[1:]
    rootname=parts[0].split('[')[0]
    if etree.QName(root).localname!=rootname: print('ROOT MISMATCH',f,xp); bad+=1; continue
    rel='/'.join(parts[1:])
    try: res=root.xpath(rel,namespaces=NS) if rel else [root]
    except Exception as e: print('XPATH ERR',f,xp,e); bad+=1; continue
    if len(res)!=1: print('RESOLVES',len(res),f,xp); bad+=1; continue
    if val is not None:
        vals+=1
        actual=(res[0].text or '').strip()
        ok = actual==val or (val.endswith('…') and actual.startswith(val[:-1].rstrip()))
        if not ok: print('VALUE',f,xp,repr(val),'!=',repr(actual)); vbad+=1
print('citations',n,'unresolved',bad,'values',vals,'mismatch',vbad)
