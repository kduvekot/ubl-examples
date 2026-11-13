# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

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

### sea/18#F1 · Medium · Pre-carriage by Bayforth on the bill of lading is not invoiced
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Name` = `Sea freight, 40-foot container`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:FreightAllowanceCharge/cbc:Amount` = `310.00`
- Why: The bill of lading this invoice refers to shows Bayforth Forwarding as carrier of the pre-carriage by road, with a freight charge of 310.00 XBL. Under the agreed CIF Selanu terms (`05-Order.xml`), the seller Lumeway bears carriage to Selanu, so Bayforth's road haulage would be billed to Lumeway. This invoice bills sea freight (2 700 + 250 = 2 950), export clearance and insurance, but not the pre-carriage, and nothing says it is billed elsewhere.
- Condition: Either the invoice carries the pre-carriage charge of 310.00, or the flow shows where the pre-carriage is billed (or that it is included in another line).
- Options: (a) add a line "Pre-carriage by road" 310.00 (payable 3 485.00); (b) state in a note that the haulage is billed separately; (c) change the bill of lading's charge. Preferred (a): Bayforth is the carrier and the shipper's forwarder.
- Needs decision: yes

### sea/18#F2 · Medium · Gate number in AdditionalStreetName of the buyer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is not a street name; it is a vehicle entrance to the business park, which a postal address does not need. The same value occurs in 76 examples (`grep -l` for `<cbc:AdditionalStreetName>Gate 3</cbc:AdditionalStreetName>` over `world/examples/*/*.xml`).
- Condition: The postal address holds no gate in `AdditionalStreetName`; the gate, if needed, is in a delivery location.
- Options: drop it from the postal address and keep it where goods are delivered (delivery location / `Location` description), preferred; or move it to `MarkAttention`-like text only where a delivery needs it.
- Needs decision: no

### sea/18#F3 · Low · Accounting cost "Stock purchases" on a forwarding invoice
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: The buyer's accounting code books the invoice as stock purchases, but the invoice bills freight, export clearance and insurance, which are distribution/selling costs for Lumeway (it sells CIF). (`4410` / "Stock purchases" occurs in no other example; `grep` over `world/examples/sea/*.xml`.)
- Condition: The accounting code fits what the buyer books this invoice to (outbound freight and services), or is absent.
- Options: an outbound-freight cost code of Lumeway; or omit it.
- Needs decision: no

### sea/18#F4 · Low · Contacts do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact is the forwarder's export desk (operations planner), and the accounting customer's contact is Lumeway's customer service in Sales. For an invoice, the supplier's contact answers billing questions and the customer's contact receives and approves invoices (accounts payable).
- Condition: Both accounting parties carry a contact that handles invoices, or no contact.
- Options: accounts receivable at Bayforth and accounts payable at Lumeway (preferred); or omit the contacts.
- Needs decision: no

### sea/18#F5 · Low · Reference to the bill of lading without type; no reference to the forwarding order
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: The additional reference gives only the bill of lading number, without `DocumentTypeCode` or `DocumentType`, so the reader cannot tell what `TOL-BL-26-0139` is. The service was ordered by Lumeway's forwarding instructions `LD-FI-26-0131` (`09-ForwardingInstructions.xml`), which the invoice does not mention although it is the basis of the charges.
- Condition: The reference says it is a bill of lading; the forwarding instructions are referenced (e.g. as order or additional document).
- Options: add a document type to the B/L reference and an `OrderReference` or additional reference to `LD-FI-26-0131`.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 950 + 85 + 140 = 3 175.00 = line extension = tax exclusive = tax inclusive = payable; tax 0 at 0 % on 3 175; penalty 1.5 % × 3 175 = 47.625 → 47.63.
- Sea freight 2 950 = ocean freight 2 700 + bunker surcharge 250 on `14-BillOfLading.xml`; insurance 140 = the B/L's insurance premium 140.00 XBL; export clearance matches the export declaration `BF-EX-26-0135` lodged by Bayforth (`11-ExportCustomsDeclaration.xml`).
- Due date 2026-06-18 = issue 2026-05-19 + 30 days, as the terms "30 days net" say; penalty period starts the day after.
- RF reference `RF98BFINV260143`, GLN `9520610900008` and the IBAN-like account `XB40BLUM38020502618225` pass `check_ids.py`; the account's bank code and branch `380205` agree with the branch ID.
- Consignment `LD-CS-26-0133` and carrier Tidewell Ocean Lines agree with the B/L.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`: buyer and seller repeat the accounting parties — refuted: allowed and consistent, no contradiction.
- `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: insurance would normally be exempt as insurance, not as a business service — refuted as a finding: the forwarder rebills the premium as part of its service; the world's state sales tax exempts B2B services.
- `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PaymentTerms/cbc:Note` = `Ocean freight payable before release of the bill of lading.`: freight payable before release, invoice due a month later — refuted: the B/L term is between Tidewell and Bayforth; this invoice is from Bayforth to Lumeway.
