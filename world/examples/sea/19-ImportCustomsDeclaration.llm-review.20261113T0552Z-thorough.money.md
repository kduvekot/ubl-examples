# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/19-ImportCustomsDeclaration.xml`, Git blob `64061347e935665afd0ab08807b3400cadbb512f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b532c38 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/19#F1 · Medium · Customs value of the goods is the FOB price, although freight is declared and the bill of lading gives a CIF customs value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `307.200`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:Amount` = `1162.121`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods item". The two values are exactly the FOB line values of the sale converted at 0.4 (49920.00 XBL × 0.4 = 19968.000; 768.00 XBL × 0.4 = 307.200; `11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`). The goods were bought CIF Selanu and invoiced with freight and insurance (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `53778.00`), and the bill of lading states the customs value as the CIF value (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`). On import, a customs value on a CIF basis (WTO valuation, Art. 8.2, as most countries apply it; own knowledge) would include freight and insurance to the place of import: 53778.00 XBL × 0.4 = 21511.200 XLC. The declaration lists a freight share for the benches, but does not include it in the value, and gives no reason why Lisavu values FOB. Either the island values FOB (then the bill of lading's CIF customs value contradicts it, and the freight line has no stated purpose), or the values are too low.
- Condition: The declared customs values follow one stated valuation basis of Lisavu, consistent with the freight and insurance figures in the same declaration and with the value the bill of lading gives for customs purposes.
- Options: (a) preferred: CIF basis, i.e. each goods item's value includes its share of freight and insurance (total 21511.200 XLC); (b) keep FOB valuation as Lisavu's rule, say so (e.g. in a note), and align the bill of lading's customs value; the choice is a question of Lisavu's customs law.
- Needs decision: yes

### sea/19#F2 · Low · Freight share declared for the benches only, and the whole insurance policy attached to the benches
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:FreightAllowanceCharge/cbc:AllowanceChargeReason` = `Ocean freight, share of the benches`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- Why: The freight 2950.00 XBL = 1180.000 XLC is apportioned by value: 1180.000 × 19968.000 / 20275.200 = 1162.121 XLC for the benches. The remaining share of 17.879 XLC for the side frames (goods item 2) is declared nowhere, so the declared freight does not add up to the freight paid. The insurance policy, whose insured value 59155.80 XBL is 110 % of the CIF value of both goods items, is attached to goods item 1 only and stated in XBL while all other values of the declaration are in XLC. Read per goods item, the benches appear insured for more than the whole consignment.
- Condition: Freight and insurance are given either per goods item for every goods item, adding up to the totals, or once for the shipment.
- Options: (a) preferred: give goods item 2 its freight share (17.879 XLC) and an insurance reference too, or move both to the shipment; (b) leave freight and insurance out if Lisavu's valuation does not use them (see F1).
- Needs decision: no

### sea/19#F3 · Low · Bayvarran sales-tax registrations of consignor and forwarder in a Lisavan import declaration
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: The registrations of Lumeway and Bayforth for Bayvarran state sales tax (Upland State, Coastal State) play no part in an import clearance by the Island Customs Service; the importer, who is the party liable for duties, carries no tax scheme. The data look copied from master data (section 4.8).
- Condition: Consignor and forwarder carry tax schemes only if the declaration uses them.
- Options: (a) preferred: leave both `PartyTaxScheme` out; (b) keep them with a stated customs purpose.
- Needs decision: no

## Checked and consistent
- Exchange rate: 0.4 XLC per XBL, as in the forwarding instructions, bill of lading and invoice; 49920.00 × 0.4 = 19968.000 and 768.00 × 0.4 = 307.200, in three decimals for XLC as elsewhere in the flow.
- Freight apportionment by value: 1180.000 × 19968.000 / 20275.200 = 1162.121 (rounded), matching goods item 1.
- Insured value 59155.80 XBL = 1.1 × 53778.00 XBL, the same policy amount as in the bill of lading and the export declaration.
- The power of attorney for the broker (paying duties on behalf of Velumi) and the note that duties are paid from the importer's account at customs agree: the broker initiates the payment, the importer's account is debited.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.`: suspected a contradiction with the bill of lading's disbursement terms (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DisbursementPaymentTerms/cbc:Note` = `Island customs fees advanced by the broker and recharged to the consignee.`) — refuted because duties and the broker's advanced fees are different amounts; one can be paid from the importer's customs account and the other advanced by the broker.
- Missing duty and tax amounts: suspected the declaration's purpose depends on them — refuted because the UBL 2.5 ImportCustomsDeclaration has no duty or tax aggregates; the assessment is made by customs.
