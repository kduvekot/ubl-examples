# LLM review: 19-DespatchAdvice.xml

Flow: furniture (9900336121) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/furniture/19-DespatchAdvice.xml`, Git blob `ec5c1dc85db0ae217a97f2e502444eeaa09cc437` (committed)
- Last commit changing the example: 6c2fbc1f 2026-11-21 Merge stage 7 batch B1; the encyclopedia's texts kept, both lexicon additions
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

### furniture/19#F1 · Low · The despatch party's contact is the trade sales manager
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Trade sales manager`
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the pieces when the van unloads and report any damage the same day.`
- Why: the despatch supplier's contact in a despatch advice is the one the goods-in team calls about the delivery itself (a missing piece, damage at unloading, the van's arrival); the note asks for damage to be reported the same day. The contact given is the sales contact of the order (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Trade sales manager`), copied from the seller's master data, not a despatch or workshop contact.
- Condition: the despatch supplier's contact is one that handles despatch and delivery questions (or the sales contact is kept with a reason visible in the document).
- Options: (a) a despatch or workshop contact of Brackenmere (preferred); (b) keep the sales contact if the small workshop has no separate despatch desk, and say so in the contact's note.
- Needs decision: no

## Checked and consistent
- Quantities 12, 8, 24, 16 and 20 equal the order lines of `08-Order.xml` and the invoiced quantities of `09-Invoice.xml`, line by line; 20 care kits = one per bench (12 + 8), as the item description says.
- Weight: with the returned part of the same goods, 295.85 kg for 7 benches, 10 chairs and 7 kits in `12-InstructionForReturns.xml`, the two shipments give 24.75 kg per bench with its kit and 12.26 kg per chair, both packed (solving 20 b + 40 c = 985.4 and 7 b + 10 c = 295.85); plausible for solid oak and ash pieces in cartons (own knowledge).
- Dates: despatch and estimated delivery on Monday 23 March, the order's requested day; the invoice of 12:42 that day gives 23 March as the actual delivery and cites this despatch advice.
- Own-label GTINs carry Brightmarket's GS1 prefix (as its GLN `9522610900002`), fitting an own-brand range; all GTINs and GLNs pass their check digits; the wood codes match the species in the descriptions.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Brightmarket Stores, goods-in, Lumeport`: named differently in `09-Invoice.xml` (`Goods-in of the Lumeport store`) — refuted: the GLN `9522610900019` is the same, and the name is free text.
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `985.4`: shipment gross weight includes "transport equipment" — refuted: the goods travel loose in a van, with no transport equipment of their own to add.
