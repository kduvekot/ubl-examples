# LLM review: 09-DespatchAdvice.xml

Flow: medicines (SGH/2026/1099) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/09-DespatchAdvice.xml`, Git blob `a448a829e016639c4d98e62ff67627dd3c840f2b` (committed)
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### medicines/09#F1 · Low · The generator's hazardous item has another identifier than in the forwarding instructions and the waybill
- XPath: `/DespatchAdvice/cac:DespatchLine[4]/cac:Item/cac:HazardousItem/cbc:ID` = `HVI-TCG-20-DG`
- Why: `HazardousItem/ID` identifies the hazardous item. The same generator in the same consignment `QLM-CS-26-3980` is `QLM-RAD-0020-DG` in `06-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cbc:ID` and `11-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cbc:ID`, both issued by or for Quillmoor, the despatch party here. `HVI-TCG-20-DG` is the maker's identifier used on the inbound leg (`08-ImportCustomsDeclaration.xml`). The despatch advice and the transport documents of one consignment cannot be linked by this identifier.
- Condition: the hazardous item of the generator has the same identifier in every document of consignment `QLM-CS-26-3980`.
- Options: (a, preferred) Quillmoor's `QLM-RAD-0020-DG` in this despatch advice (and in `13-ImportCustomsDeclaration.xml`); (b) the maker's identifier everywhere.
- Needs decision: no

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` resolves to `04-Order.xml`; the four lines reference order lines 1 to 4 with the ordered quantities; 300 packs × 10 = 3,000 doses, as line 1's note says.
- Shipment `QLM-SH-26-3980`, consignment `QLM-CS-26-3980`, gross weight 101.1 kg and the carrier Kelaro Air Cargo agree with `06-ForwardingInstructions.xml` and `11-Waybill.xml`.
- Times: issued 05:10 −01:00 on 15 June, before the van reaches the terminal at 05:30 (`06-ForwardingInstructions.xml`) and before acceptance (`10-TransportationStatus.xml`).
- Lots: expiry dates in the future; 2028-02-29 is a valid date (2028 is a leap year).
- Generator: serial `HVI-TCG20-26-0137`, 20 GBq and reference 2026-06-21T12:00 UTC as in `07-Invoice.xml`; six days after delivery on 15 June; 97 GBq at the time of transport (20 × 2^(150/65.94) ≈ 97, own knowledge of the half-life).
- The delivery customer's contact (pharmacy goods-in) fits receiving the goods.
