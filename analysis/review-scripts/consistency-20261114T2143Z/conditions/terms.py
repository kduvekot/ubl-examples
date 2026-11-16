import sys; sys.path.insert(0,sys.argv[1])
from lib import *
import datetime as dt
D=lambda s: dt.date.fromisoformat(s) if s else None
for f,t,root in docs():
    for pt in root.xpath('cac:PaymentTerms',namespaces=NS):
        tid=txt(pt,'cbc:ID')
        if not tid: continue
        iss=D(txt(root,'cbc:IssueDate'))
        due=[txt(root,'cbc:DueDate'),txt(root,'cbc:PaymentDueDate'),txt(pt,'cbc:PaymentDueDate'),txt(root,'cac:PaymentMeans/cbc:PaymentDueDate')]
        ti=txt(root,'cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount') ; pay=txt(root,'cac:LegalMonetaryTotal/cbc:PayableAmount')
        da=txt(pt,'cbc:SettlementDiscountAmount'); pa=txt(pt,'cbc:PenaltyAmount')
        dd=[ (D(x)-iss).days if x else '' for x in due]
        sp=(txt(pt,'cac:SettlementPeriod/cbc:StartDate'),txt(pt,'cac:SettlementPeriod/cbc:EndDate'))
        pp=txt(pt,'cac:PenaltyPeriod/cbc:StartDate')
        chk=''
        try:
            if da: chk+=' disc/TI=%.4f disc/pay=%.4f'%(float(da)/float(ti),float(da)/float(pay))
            if pa: chk+=' pen/pay=%.4f pen/TI=%.4f'%(float(pa)/float(pay),float(pa)/float(ti))
        except Exception as e: chk+=' ERR'
        print(f,tid,'iss',iss,'due',due,'days',dd,'TI',ti,'pay',pay,'disc',da,'pen',pa,chk,'SP',sp,'PP',pp, 'ev',txt(pt,'cbc:PaymentTermsReferenceEventCode') if False else '')
