# LLM review: 04-Order.xml

Flow: medicines (SGH/2026/1099) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/04-Order.xml`, Git blob `a59e0658b93455f17d5019bf5c5a26421a817953` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

## Checked and consistent
- Arithmetic: 300 × 72 = 21,600.00; 240 × 21.5 = 5,160.00; 40 × 48 = 1,920.00; 1 × 1450 = 1,450.00; sum 30,130.00 XBL = line extension and payable amount; tax 0.00 with exemption "Export outside Bayvarra" for a delivery to Lisavu.
- 2026-06-15 is a Monday, as the note says; the requested delivery date, CPT Selanu airport (`XLSLA`) and the flight fit `06-ForwardingInstructions.xml` and `11-Waybill.xml`.
- Items: Quillmoor's own identifiers (`QLM-VAC-1102`, `QLM-INS-0310`, `QLM-VAC-2410`, `QLM-RAD-0020`) as seller's identifiers and the makers' identifiers as manufacturer's identifiers agree with `01-Order.xml`, `05-Order.xml`, `09-DespatchAdvice.xml` and `14-Invoice.xml`.
- Prices against purchase costs: influenza 54.37 XBL bought (`03-ImportCustomsDeclaration.xml`), sold at 72; insulin 17.24 → 21.5; varicella 37.79 → 48; generator 1,187 XBL customs value (`08-ImportCustomsDeclaration.xml`) → 1,450; all plausible margins.
- The hospital's contact (hospital pharmacy, pharmacist, weekdays) fits the buyer of medicines.

## Considered and refuted
- `/Order/cbc:ProfileExecutionID` = `SGH/2026/1099` against `/Order/cbc:ID` = `SGH/2026/1100`: suspected as a mistyped document number — refuted, it identifies the collaboration, and the despatch advice and invoice carry the same value.
- `/Order/cac:OrderLine[4]/cac:LineItem/cac:Item/cbc:Description`: "reference time, six days after delivery" — refuted for this order: delivery on 15 June and the reference of 21 June (`09-DespatchAdvice.xml`) are six days apart.
