# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/03-Invoice.xml`, Git blob `802363ed10113ef3a82c854031713a677b74609e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

### waste/03#F1 · High · The tonnes billed "per tonne collected" are the shipment's gross weight, including packaging and transport equipment
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38.2`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Collection at the factory and recovery of sorted production waste, per tonne collected.`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: The line bills the waste collected, per tonne. The referenced waste movement (`/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`) states 38 200 kg only as `GrossWeightMeasure`, defined as "the weight of the goods plus packaging plus transport equipment". Billing 38.2 t therefore bills the big bags and the transport equipment as waste, or the movement's 38 200 kg is in fact a net figure in the wrong element. Either way the two documents contradict each other on the quantity of waste. (The magnitude itself, 38.2 t for one road load of bagged PE, is also implausible; see the physics finding in `02-WasteMovement.xml`'s review.)
- Condition: The invoiced quantity equals the net weight of waste stated in the referenced movement (or in a referenced weight statement), and that net weight is below the shipment's gross weight.
- Options: (preferred) state a net weight in `02-WasteMovement.xml` (from the weight statement) and invoice that quantity, recalculating the line and totals; alternatively, if the price is agreed per gross tonne, say so in the item description and the movement keeps 38 200 kg as gross.
- Needs decision: no

### waste/03#F2 · Low · The invoice does not say when the collection took place
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-04`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-04-04`
- Why: The invoice bills a collection and recovery service but carries no `cac:Delivery` (actual delivery date and place) and no `cac:InvoicePeriod`. The referenced movement does not state a transport date either (only its issue date 2026-04-02, see its review), so no document of the flow says on which day the waste was collected. A per-shipment service invoice normally states the date of performance.
- Condition: The invoice (or the referenced movement) states the date of collection/delivery, no later than the invoice issue date 2026-04-04, and consistent with the movement.
- Options: (preferred) add `cac:Delivery/cbc:ActualDeliveryDate` with the facility as `DeliveryLocation`, matching the date added to `02-WasteMovement.xml`; alternatively an `InvoicePeriod`.
- Needs decision: no

### waste/03#F3 · Low · The reference to the waste movement gives only its ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207`
- Why: The reference resolves to `02-WasteMovement.xml` (a Waste Movement, ID `RR-DOC-26-0207`), but the invoice does not say what kind of document it is: no `DocumentTypeCode`/`DocumentType` and no issue date. The ID's prefix `RR-DOC` does not tell the buyer that it is the movement document of the collected load. The same pattern (a `*DocumentReference` whose only child is `cbc:ID`) occurs 555 times in 177 of 250 examples (counted over `world/examples/*/*.xml` with lxml).
- Condition: The reference states that it is the waste movement document (code or text), and preferably its issue date 2026-04-02.
- Options: (preferred) add `cbc:DocumentTypeCode` (world UBL document type list, `WasteMovement`) or `cbc:DocumentType`, plus `cbc:IssueDate`.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `RR-DOC-26-0207` resolves to `02-WasteMovement.xml`, issued 2026-04-02 12:34, before this invoice (2026-04-04 12:44).
- Quantity x unit: 38 200 kg in the movement = 38.2 t (`TNE`) here; price base quantity 1 TNE; 38.2 x 12 350 = 471 770 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount`.
- The supplier's R3 authorisation and permit `XU-ENV-2024-0311` (valid to 2029-12-31) are the same as in `01-WasteNotification.xml` and `02-WasteMovement.xml`, and cover the service date.
- `ProfileExecutionID` `WASTE-2026-01` is the same as in the other two examples.
- `check_ids.py`: ISIN, RF reference `RF84RRINV260208` and account `XU700351041620000000418916` check digits OK.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]`: suspected a contradiction because the invoice bills "collection at the factory" while the carrier in the movement is Trasvia Haulage, not Rinova — refuted because the recovery facility can sell collection as part of its service and subcontract the haulage; nothing in the flow says Valdara contracted Trasvia itself.
- `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity`: suspected a unit conversion error between KGM in the movement and TNE here — refuted: 38 200 kg = 38.2 t exactly.
- Missing reference to the notification `VI-DOC-26-0204`: suspected that the invoice should cite it — refuted because the movement it cites already refers to the notification, and the invoice bills one movement.

