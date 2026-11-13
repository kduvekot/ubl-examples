# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/18-Invoice.xml`, Git blob `8959fff2666b14c481d466f04457f91ebe10f1e4` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/18#F1 · Low · Buyer's accounting cost "Stock purchases" for outbound freight, clearance and insurance under CIF
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCost` is "the buyer's accounting code, applied to the Invoice as a whole". The buyer here is Lumeway Distribution, which ships goods it sells to Velumi Trading under CIF Selanu (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:ID` = `CIF`). The invoice bills sea freight, export clearance and cargo insurance for that outbound sale: under CIF these are the seller's costs of delivering what it sold (selling/distribution costs), not purchases of stock. "Stock purchases" fits an inbound freight bill (freight capitalised into stock), not this one.
- Condition: The buyer's accounting cost names an account that fits outbound freight, clearance and insurance paid by the seller under CIF, or is absent.
- Options: (a) preferred: an outbound freight / distribution cost account of Lumeway (e.g. "Outbound freight and insurance"), since the reason is the CIF sale; (b) leave the element out if Lumeway gave the forwarder no cost code.
- Needs decision: no

### sea/18#F2 · Low · Carrier's tax registration and share capital in the forwarder's invoice
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- Why: The ocean carrier Tidewell Ocean Lines is neither supplier nor customer of this invoice; Bayforth bills the freight in its own name. The carrier's sales-tax registration and share capital play no role in the tax treatment or payment of the invoice (section 4.8: master data copied into a document that does not use it). Naming the carrier, if wanted, needs only its identification and name.
- Condition: The carrier party in the delivery carries no tax scheme or capital data unless the invoice uses them.
- Options: (a) preferred: reduce the carrier to identification and name; (b) leave the carrier out entirely, since the bill of lading reference already ties the invoice to the carriage.
- Needs decision: no

## Checked and consistent
- Lines: 2950.00 + 85.00 + 140.00 = 3175.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`; tax exclusive, tax inclusive and payable 3175.00 with tax 0.00; each line quantity 1 × price 2950 / 85 / 140 per base quantity 1.
- Sea freight 2950.00 = ocean freight 2700.00 + bunker surcharge 250.00 on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `2700.00`, `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:Amount` = `250.00`), prepaid by the shipper (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Ocean freight and bunker surcharge prepaid by the shipper.`).
- Insurance 140.00 = premium on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsurancePremiumAmount` = `140.00`); insured value 59155.80 = 110 % of CIF 53778.00 = FOB 50688.00 + freight 2950.00 + insurance 140.00.
- Tax: category E with reason SVCB2B ("A service supplied to a business is not a retail sale", Bayvarra list) fits services to Lumeway, a business in Bayvarra; EXP would not apply because the buyer is in Bayvarra. The same category on all three lines and in the subtotal.
- Payment terms: 30 days net from 2026-05-19 = 2026-06-18 = `/Invoice/cbc:DueDate`, the payment means' and the terms' due date; penalty 1.5 % × 3175.00 = 47.625 → 47.63 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount`, for one month from 2026-06-19.
- Payee account `XB40BLUM38020502618225` is Bayforth's own account (name Bayforth Forwarding Ltd, XBL), used for Bayforth in other flows too; RF reference `RF98BFINV260143` has a valid check digit.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `2950.00`: suspected the forwarder resells the freight without margin — refuted because pass-through of carrier freight at cost, with the forwarder's fee in separate lines, is common practice and consistent with the bill of lading.
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: suspected international transport should be treated as export (EXP) — refuted because the EXP reason requires a buyer outside Bayvarra; the buyer Lumeway is in Bayvarra and buys a service as a business.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`: suspected copied master data — refuted as a finding of this lens because the customer of an invoice is identified with its legal entity in the flow's billing documents; whether its capital belongs there is a parties question.
