import sys; sys.path.insert(0,'/tmp/claude-0/-home-user-ubl-examples/3a42b48a-1edc-5b37-938f-a9af42fda1cf/scratchpad/consistency-20261114T2143Z/conditions')
from lib import *
for f,t,root in docs():
    cats=root.xpath('.//cac:TaxSubtotal|.//cac:ClassifiedTaxCategory|.//cac:AllowanceCharge/cac:TaxCategory',namespaces=NS)
    if not cats: continue
    s=pcountry(root,['AccountingSupplierParty','SellerSupplierParty'])
    b=pcountry(root,['AccountingCustomerParty','BuyerCustomerParty'])
    print('##',f,'seller',s,'buyer',b,'cur',txt(root,'cbc:DocumentCurrencyCode'),'taxcur',txt(root,'cbc:TaxCurrencyCode'))
    for c in cats:
        cat=c if ln(c)!='TaxSubtotal' else c.find('cac:TaxCategory',NS)
        ctx=c.getparent()
        # find nearest line item name or allowance reason
        anc=c
        label=''
        while anc is not None:
            if ln(anc).endswith('Line') or ln(anc) in('AllowanceCharge',):
                label=ln(anc)+':'+txt(anc,'cac:Item/cbc:Name|cbc:AllowanceChargeReason|cbc:ID')[:50]; break
            anc=anc.getparent()
        print('  ',ln(c),label,'|',txt(cat,'cbc:ID'),txt(cat,'cbc:Percent'),txt(cat,'cbc:TaxExemptionReasonCode'),txt(cat,'cbc:TaxExemptionReason[1]')[:60],'|',txt(cat,'cac:TaxScheme/cbc:ID'),txt(cat,'cac:TaxScheme/cbc:Name'),'| base',txt(c,'cbc:TaxableAmount'),'tax',txt(c,'cbc:TaxAmount'),txt(c,'cbc:TransactionCurrencyTaxAmount'))
