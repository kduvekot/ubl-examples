# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/02-Invoice.xml`, Git blob `ca1ffa8a13476757483bcb761f1e9079132080e5` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/02#F1 · Medium · Two invoice lines that nothing tells apart
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `412800`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- Why: Lines 1 and 2 carry the same item (electricity network use, FG-NET-E), the same price (6.2 XUF/kWh) and the same tax category, and no element that says why they are separate: no consumption point, delivery location, note, period or order line reference. A network operator splits such lines per connection or per customer of the retailer; here the split is implied only by the existence of two lines, which the rules exclude ("nothing implied by absence", IND5/IND6). The buyer cannot check either quantity against anything.
- Condition: Each of lines 1 and 2 carries a value that identifies what it is for (e.g. the connection or consumption point, or a reference to the statement that supports it), or the two lines are one line.
- Options: (a) preferred: give each line the identification of the connection it bills (e.g. InvoiceLine/cbc:Note or cac:Delivery/cac:DeliveryLocation with the consumption point ID, or a cac:DocumentReference to a utility statement), which also lets lines be checked against meter data; (b) merge them into one line of 431400 kWh if the split has no reason in the world.
- Needs decision: no

### energy/02#F2 · Low · The gas line does not point to the utility statement that supplements it
- XPath: `/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `01-UtilityStatement.xml:/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- Why: The utility statement FG-DOC-26-0149 (01) declares this invoice its parent and gives the meter readings and conversion for exactly the 61200 kWh of line 3. The invoice itself does not mention the statement or the consumption point (FG-CP-4120-G1), so a reader of the invoice alone cannot find the supporting data; the link exists in one direction only.
- Condition: Line 3 (or the invoice) can be linked to the statement FG-DOC-26-0149 or to the consumption point FG-CP-4120-G1 from the invoice itself.
- Options: (a) preferred: a line-level cac:DocumentReference to FG-DOC-26-0149 (the statement is line-specific); (b) a document-level cac:AdditionalDocumentReference; (c) leave it, accepting the one-way link, if the world's billing profile says the statement always refers to the invoice and not the other way round.
- Needs decision: no

## Checked and consistent
- Line 3 against 01-UtilityStatement.xml: 61200 kWh = `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `61200`; invoice period 2026-03-01 to 2026-03-31 equals the statement's MainPeriod.
- Line arithmetic: 412800 × 6.2 = 2559360; 18600 × 6.2 = 115320; 61200 × 1.9 = 116280; sum 2790960 = LineExtensionAmount; 20 % VAT = 558192; total 3349152.
- SupplyTypeCode SERVICES fits network use (a service, not the supply of energy itself).
- LineCountNumeric 3 equals the number of InvoiceLine elements.

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-04-03`: suspected redundant with IssueDate — refuted because the definition ("used to indicate the point at which tax becomes applicable") is met: for a monthly continuous supply the tax point is the invoice date in many VAT systems, and stating it is not a filler.
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`: suspected repetition of the accounting customer — refuted because Invoice. Buyer_ Customer Party is defined as "The buyer." without an "if different" condition.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `3510`: suspected that a grid operator billing gas network use should be ISIC 3520 — refuted because electricity is its main activity (lines 1 and 2 are 96 % of the net amount).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: suspected an implausible channel for a domestic invoice — refuted because a 3.3 million XUF payment between two large companies is a typical RTGS payment.
