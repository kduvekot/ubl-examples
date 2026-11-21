# LLM review: 11-ReceiptAdvice.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/11-ReceiptAdvice.xml`, Git blob `42ed0a6772d841a5c80d6dd1423a04d92244057d` (committed)
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

## Findings

### reefer/11#F1 · Low · One goods item number, three different goods and temperatures
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Shipment/cac:GoodsItem/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Shipment/cac:GoodsItem/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[3]/cac:Shipment/cac:GoodsItem/cbc:ID` = `1`
- Why: each receipt line refers to shipment `HRW-SH-26-0730` and to its goods item `1`, with a different product temperature each time (0.8, 0.7 and 0.6 °C), so the same goods item of the same shipment has three temperatures. In the other examples of this shipment goods item `1` is either the whole load (`07-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:GoodsItem/cbc:ID` = `1`, with the varieties as 1.1 and 1.2) or the Gala alone (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:Description` = `Apples Gala, carton 18 kg, count 100`); in neither is it the Granny Smith of line 2 or the pears of line 3.
- Condition: the goods item each receipt line points to is the goods item of that line's goods, with the same numbering as another document of the shipment, so that each measured temperature belongs to one identifiable goods item.
- Options: (a) number the goods items 1, 2, 3 as in the customs documents and the certificate (preferred: one goods item per variety, as measured); (b) use the bill of lading's numbering (1.1 apples for lines 1–2, 1.2 pears for line 3) if the measurement is per fruit type.
- Needs decision: no

## Checked and consistent
- Received quantities 672, 280 and 168 equal the despatched quantities of `06-DespatchAdvice.xml`, line by line, with order and despatch line references resolving; acceptance code "all accepted" agrees with "received as despatched".
- The note's range 0.2–0.9 °C is the log reported in `10-TransportationStatus.xml`; product temperatures 0.6–0.8 °C lie inside the 0–1 °C range.
- Received on Monday 27 April at 09:27, within the cold store's hours (`Monday to Saturday 05:00–14:00`), the date the despatch advice estimated.
