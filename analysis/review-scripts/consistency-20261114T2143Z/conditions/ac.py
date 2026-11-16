import sys; sys.path.insert(0,sys.argv[1])
from lib import *
import collections
c=collections.defaultdict(list)
for f,t,root in docs():
    for ac in root.xpath('.//cac:AllowanceCharge|.//cac:FreightAllowanceCharge',namespaces=NS):
        code=ac.find('cbc:AllowanceChargeReasonCode',NS)
        k=(txt(ac,'cbc:ChargeIndicator'),code.text if code is not None else '',code.get('listID') if code is not None else '',txt(ac,'cbc:AllowanceChargeReason')[:50],txt(ac,'cbc:MultiplierFactorNumeric'))
        c[k].append(f.replace('.xml','')+':'+ln(ac.getparent()))
for k,v in sorted(c.items()): print(k,len(v),v[:8])
