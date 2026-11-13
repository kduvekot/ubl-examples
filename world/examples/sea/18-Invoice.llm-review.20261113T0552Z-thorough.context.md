# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/18#F1 · Low · Outbound freight, export clearance and cargo insurance booked as "stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole". The buyer is Lumeway Distribution, which here buys forwarding services for goods it sells: sea freight to Selanu, its own export declaration and cargo insurance. Under the sale's delivery terms CIF (`05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`, repeated in `14-BillOfLading.xml`) the seller pays freight and insurance to the port of destination as part of fulfilling the sale; for Lumeway these are distribution costs of a sale, not purchases of stock. The code reads as copied from Lumeway's purchase of goods.
- Condition: The accounting code and text name a cost the buyer would book these services to (outbound freight, distribution or selling costs), or are absent.
- Options: (a) preferred: an accounting code and text for outbound freight / distribution costs; (b) remove both if Lumeway gives no accounting code to its forwarder.
- Needs decision: no

### sea/18#F2 · Low · The carrier's full master data in a forwarder's invoice
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- Why: The consignment is given to identify which transport the invoiced services relate to; naming the carrier helps with that. But the carrier is described with its postal address, tax registration, share capital, legal form, size, registration scheme, contact and electronic address. None of this is used by the invoice: Tidewell Ocean Lines is neither supplier nor customer here, and the invoice settles nothing with it. This is master data copied into a document that does not use it.
- Condition: The carrier in the invoice's delivery is described only with what identifies it for the invoice's purpose (identifier and name).
- Options: (a) preferred: keep identification and name only; (b) remove the carrier and rely on the consignment ID and the bill of lading reference.
- Needs decision: no

## Checked and consistent
- The services agree with the flow: the forwarder lodged the export declaration (`11-ExportCustomsDeclaration.xml`, ID `BF-EX-26-0135`, a Bayforth number), booked the carriage on the bill of lading `TOL-BL-26-0139` (which exists, `14-BillOfLading.xml`), and the insurance agrees with the CIF terms.
- The consignment `LD-CS-26-0133` is the one in the forwarding instructions and the bill of lading.
- The invoice is issued after the sailing (bill of lading 2026-05-14) and before the due date; penalty period starts the day after the due date.
- The penalty amount 47.63 = 1.5 % × 3175.00 (47.625, rounded).

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeated with the same parties as the accounting parties, suspected as a filler — refuted because UBL defines `BuyerCustomerParty` as "The buyer" without a condition "if different", and naming the commercial parties of the service is a legitimate statement.
- `/Invoice/cbc:InvoiceTypeCode`: 380 "Commercial invoice" for a services invoice — refuted because UNCL 1001 code 380 covers any claim for payment for goods or services supplied.
