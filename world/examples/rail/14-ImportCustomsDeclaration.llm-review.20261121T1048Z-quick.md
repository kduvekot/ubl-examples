# LLM review: 14-ImportCustomsDeclaration.xml

Flow: rail (LMW-TX-26-0801) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/rail/14-ImportCustomsDeclaration.xml`, Git blob `c08cd882d2b1d0c828ebb923710f6fc75ee4a7b6` (committed)
- Last commit changing the example: 771277df 2026-11-21 Rail lots per container, mast order DG identification, air timing and origin statement, sawmill buys its logs
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### rail/14#F1 · Low · Function code of the previous declaration taken from the declaration type list
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `TRANSIT`
- Why: `FunctionCode` under the previous declaration is "A code describing the function of this customs declaration"; the value comes from the world's `CustomsDeclarationTypeCode` list, the list this document uses for its own `TypeCode` (`IMPORT`). Saying that the previous declaration was a transit declaration is a sensible use of the element, and the reference 7800004369 does resolve to `06-TransitCustomsDeclaration.xml`; but a type list in a function code element is a code from a list meant for another element. The same pairing occurs in 3 examples (counted with grep over `*.xml` for `FunctionCode` under `PreviousCustomsDeclaration`: rail/14, sea/11, wood/07).
- Condition: Either the world's function-code list (or a documented decision) states that the declaration type list serves as the function code of a previous declaration, or the element carries a code from a list made for it.
- Options: (a) preferred: record the decision that `CustomsDeclarationTypeCode` is the list for this element (no change to the value), since the list's meaning is what is intended; (b) a separate function-code list with the same codes.
- Needs decision: no

## Checked and consistent
- Customs value 76 608.00 XBL = 7 660 800 XUF (`06-TransitCustomsDeclaration.xml` and `11-Invoice.xml`) at 100 XUF per XBL, the rate used in `wood/08-Invoice.xml:/Invoice/cac:TaxExchangeRate/cbc:CalculationRate` = `100`.
- Quantity 192 benches, gross weight 10 377.6 kg, origin XU, HS 940179, CPC 38111 and the package structure (pallets of 4 benches, three parcels per bench) agree with `06-TransitCustomsDeclaration.xml`; shipment ID 7400043688 as in 06 and 08.
- Physics: parcels 12.2 + 13 + 21.8 = 47 kg per bench, × 192 = 9 024 kg; 10 377.6 − 9 024 = 1 353.6 kg for 48 pallets = 28.2 kg per returnable pallet (plausible for a wooden pallet). 48 pallets × 4 = 192 benches, which is the 48 in `TotalTransportHandlingUnitQuantity` ("pallets, boxes, cases").
- HS section XX (miscellaneous manufactured articles) contains chapter 94; 9401.79 (seats with metal frames, other) fits a cast-iron-frame bench.
- Invoice 2026/1770 → `11-Invoice.xml`; previous declaration 7800004369 → `06-TransitCustomsDeclaration.xml`; importer and consignee Lumeway, consignor Valdara as in 06; the note on duty and sales tax agrees with preference criterion S and the absence of duty and tax lines; GLN passes `check_ids.py`.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `48`: the transit declaration and the waybill count 2 handling units (the containers) — refuted for this example: the definition names pallets, and 48 pallets is what the goods item describes; how 06 and 08 count is their own matter (see below).
- `/ImportCustomsDeclaration/cbc:ProfileExecutionID` = `LMW-TX-26-0801`: differs from the trade's LMW-TX-26-0734 — refuted: the import clearance is a collaboration of its own between the importer and customs.

## Outside this review
- `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalTransportHandlingUnitQuantity` = `2` counts the containers as handling units, while this declaration counts 48 pallets for the same shipment; whether 08's count fits the definition belongs to 08's review.
