import sys; sys.path.insert(0,sys.argv[1])
from lib import *
import collections
rows=[]
for f,t,root in docs():
    s=pcountry(root,['AccountingSupplierParty','SellerSupplierParty'])
    for pr in root.xpath('.//cac:Price',namespaces=NS):
        line=pr.getparent()
        item=line.find('cac:Item',NS)
        if item is None:
            item=line.getparent().find('cac:Item',NS) if line.getparent() is not None else None
        nm=''
        if item is not None:
            ns=[n for n in item.findall('cbc:Name',NS) if n.get('languageID') not in('qau','qal')]
            nm=ns[0].text if ns else ''
        pa=pr.find('cbc:PriceAmount',NS)
        bq=pr.find('cbc:BaseQuantity',NS)
        rows.append((nm[:34],f.replace('.xml',''),s[1][:20],pa.text if pa is not None else '',pa.get('currencyID') if pa is not None else '',(bq.text+' '+bq.get('unitCode','')) if bq is not None else '',txt(pr,'cbc:PriceTypeCode'),txt(pr,'cbc:PriceType')[:25],txt(pr,'cac:PriceList/cbc:ID'),txt(pr,'cbc:OrderableUnitFactorRate')))
for r in sorted(rows): print(' | '.join(r))
