# LLM review: 13-ImportCustomsDeclaration.xml

Flow: medicines (26-1361) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/13-ImportCustomsDeclaration.xml`, Git blob `7833f514c9e17653f9633bdeec80ad3ca9179a0b` (committed)
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

## Findings

### medicines/13#F1 · Low · The generator's hazardous item has another identifier than in the air waybill this declaration references
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cbc:ID` = `HVI-TCG-20-DG`
- Why: the declaration references the air waybill `KXL-00698121` (`/ImportCustomsDeclaration/cac:AdditionalDocumentReference[1]/cbc:ID`), in which the same hazardous item is `QLM-RAD-0020-DG` (`11-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cbc:ID`). The same split occurs in `09-DespatchAdvice.xml` (medicines/09#F1).
- Condition: the generator's hazardous item has the same identifier in the declaration and in the transport documents of consignment `QLM-CS-26-3980`.
- Options: as medicines/09#F1.
- Needs decision: no

## Checked and consistent
- Customs values in Coral: 8,640.000 / 2,064.000 / 768.000 / 580.000 XLC against 21,600 / 5,160 / 1,920 / 1,450 XBL on `14-Invoice.xml`, a uniform rate of 0.4 XLC per XBL; three decimals as the Coral is used elsewhere in the world (135 of 148 XLC amounts in `world/examples/*/*.xml` have three decimals, counted with `grep -rho --include='*.xml' 'currencyID="XLC">[0-9.]*'`).
- References: `AdditionalDocumentReference[1]` resolves to `11-Waybill.xml`, `[2]` to `14-Invoice.xml` (issued 10:27 −01:00 = 11:27 UTC, before this declaration at 11:40 +00:00); goods arrived at 10:45 UTC (`12-TransportationStatus.xml`).
- Origins: India for the three products of Nilavar Biologics, Netherlands for the generator, as in the note and in `03-ImportCustomsDeclaration.xml` and `08-ImportCustomsDeclaration.xml`.
- Tax: import consumption tax exempt with reason `MEDHOSP` for a public hospital; the English and Lisavan renderings carry their `languageID`.
- Representation: the broker lodges as direct representative under a power of attorney dated 2026-01-06, and is the waybill's notify party; quantities and weights per goods item equal those of the waybill.
