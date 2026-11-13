# LLM review: 07-InventoryReport.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/07-InventoryReport.xml`, Git blob `e1019ee6a13e2a7196d8ba163e99b452ac02b47f` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/07#F1 · High · Emission value is not factor × base
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/07#F2 · Medium · "Counted on Sunday evening", but the report period ends and the report is issued on a Thursday
- XPath: `/InventoryReport/cbc:Note` = `Counted on Sunday evening.`
- XPath: `/InventoryReport/cac:InventoryPeriod/cbc:EndDate` = `2026-04-23`
- XPath: `/InventoryReport/cbc:IssueDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:Quantity` = `3`
- Why: 2026-04-23 is a Thursday (calculated); the last Sunday before it is 2026-04-19. InventoryReportLine/Quantity is "The quantity of the item reported that is currently in stock". If the count was made on Sunday 19 April, the quantity is four days old and the period 2026-04-16 to 2026-04-23 is not what was counted; if the stock is that of Thursday 23 April, the note is wrong. The order 08 of the next morning is based on this stock.
- Condition: the day of the count in the note agrees with the inventory period and the issue date (the count lies at the end of the period the report covers).
- Options: (a, preferred) change the note to the day of the count that fits the period, e.g. "Counted on Thursday afternoon" (the report is issued at 17:43); (b) end the period on 2026-04-19 and issue the report on Monday 2026-04-20.
- Needs decision: no

### retail/07#F3 · Low · Inventory location without the store it is in
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:InventoryLocation/cbc:Name` = `Garden department, ground floor`
- Why: InventoryLocation is "The location of the reported quantity of goods". The name gives a department and floor but no store, address or GLN; the retailer's other documents identify its goods-in by GLN (`08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`). The supplier who replenishes on this report cannot tell which store's stock it is.
- Condition: the inventory location identifies the store (name of the store, and its GLN or address) as well as the department.
- Options: (a, preferred) add the store's GLN as Location/ID and its name ("Brightmarket Lumeport, garden department, ground floor"); (b) an Address of the store.
- Needs decision: no

## Checked and consistent
- InventoryValueAmount 1560.00 XBL = 3 × 520 XBL, the trade price of catalogue line 1 in 02.
- AvailabilityDate 2026-04-23 = issue date, status `AVAILABLE`, which fits stock on the shelf.
- "Below the minimum of 6 before the promotion": 3 < 6, and the order 08 of 2026-04-24 replenishes with 24.
- DocumentReference `BS-FC-26-0221` resolves to the forecast 05, issued the day before.
- Inventory period 2026-04-16 to 2026-04-23 is one week and ends on the issue date.
- Item identifiers agree with 02 line 1.
