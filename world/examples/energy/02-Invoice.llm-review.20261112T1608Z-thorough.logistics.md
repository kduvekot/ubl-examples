# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### energy/02#F1 · Medium · The network-use lines cannot be linked to the connections and metering documents they bill
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `412800`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- Why: the grid operator bills the retailer for network use per kilowatt hour "taken at the connection" (item description), but no line says which connection, meter or metering document it is for. Lines 1 and 2 are identical in item, description, price and tax and differ only in quantity, so a reader cannot tell what each is for. The quantities match connections described elsewhere: 412800 kWh is `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `412800` (Valdara Industries, main connection), 18600 kWh is `utilities/03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `18600` (warehouse of Castrano Logistics), and 61200 kWh is `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:TotalDeliveredQuantity` = `61200` (gas, coating line). Only the gas line has a supplementing Utility Statement of the grid operator (`01-UtilityStatement.xml`, which names this invoice as its parent), and this invoice does not refer to it either; the electricity lines have no metering document of the grid operator at all, although the operator "owns and reads the meter" (`01-UtilityStatement.xml:/UtilityStatement/cbc:Note[2]`). The links exist only by coincidence of numbers.
- Condition: every invoice line identifies the connection or meter it bills (in an element whose definition fits, e.g. a line `DocumentReference` to the metering document, a line `Note`, or `Delivery/DeliveryLocation`), and the invoice refers to the Utility Statement that supplements it.
- Options: (a) preferred: give each line a reference to the consumption point or metering document it bills (`InvoiceLine/cac:DocumentReference`) and the invoice an `AdditionalDocumentReference` to FG-DOC-26-0149, because it ties the invoice to the documents that carry the readings; (b) add a delivery location per line (the connection's address and consumption point ID); (c) if the electricity lines should also be supported by the grid operator's readings, add Utility Statements of Ferrano Grid for the two electricity connections (changes the flow).
- Needs decision: no

## Checked and consistent
- Quantity × price, calculated: 412800 × 6.2 = 2 559 360; 18600 × 6.2 = 115 320; 61200 × 1.9 = 116 280; per `BaseQuantity` 1 KWH; the line amounts agree.
- Line 3 quantity 61200 kWh agrees with the converted gas energy of `01-UtilityStatement.xml` (1350 m³ × 4.9477 × 9.163 kWh/m³ ≈ 61 200 kWh).
- `LineCountNumeric` 3 = number of lines.
- Dates: `InvoicePeriod` March 2026 (2026-03-01 → 2026-03-31) agrees with the reading period of `01-UtilityStatement.xml`; issue 2026-04-03 is after the period; due date 2026-05-03 and settlement period 2026-04-03 → 2026-04-13 start at the issue date.
- Units: KWH for all lines, consistent with the per-kWh item descriptions; `check_ids.py`: RF13FGINV260150 and the payee account check digits OK.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-G`: suspected the gas line is billed by an electricity grid operator — refuted because the item, `01-UtilityStatement.xml` (Ferrano Grid reads the gas meter) and the flow consistently make Ferrano Grid the operator of both networks.
