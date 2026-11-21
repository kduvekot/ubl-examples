# LLM review: 06-DespatchAdvice.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/06-DespatchAdvice.xml`, Git blob `b0d0f1cda033bec2fafe834b8343c0725ec2c454` (committed)
- Last commit changing the example: d34fe695 2026-11-21 O277 (3): UBL's spelling "despatch" for UBL concepts, and a published-text rule for it
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Checked and consistent
- Lots against lines: Gala 224 + 224 + 224 = 672; Granny Smith 168 + 112 = 280; pears 168; the delivered quantities equal those of `02-OrderResponse.xml` and `08-Invoice.xml`.
- 20 pallets (SSCC check digits pass, serials …0001 to …0020, marks `001 of 020` to `020 of 020`) × 56 cartons = 1,120 cartons = 672 + 280 + 168; 12 + 5 + 3 pallets as the line notes say.
- Container `TWLU5316047` (ISO 6346 check digit passes) and seal `TWL-S-0884517` are those of `07-BillOfLading.xml`; actual despatch 22 April agrees with the bill of lading's drop-off at Lumeport at 17:40 that day.
- Estimated delivery 27 April agrees with the on-carriage receipt date in `07-BillOfLading.xml` and the received date in `11-ReceiptAdvice.xml`.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-04-20`: fruit picked in February and March has no manufacture date in April — refuted: for fresh produce the packing date is the usual reading of a production date, and the fruit was packed out of the cold store before despatch.
- `/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU5316047`: its schemeID `ISO6346` is spelt without the space used in listID `ISO 6346` for size-type codes elsewhere — refuted: the spelling is the same in all 19 container IDs of the examples (grep over `*.xml`), and the agreed rule is that schemeIDs keep their current style.
