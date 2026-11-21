# LLM review: 08-ImportCustomsDeclaration.xml

Flow: medicines (QLM-TX-26-4067) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/08-ImportCustomsDeclaration.xml`, Git blob `0a99677a14d7e5e5457a53df26ae0cba866db750` (committed)
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

### medicines/08#F1 · High · The stated maximum activity during the flight from the Netherlands is lower than the activity on arrival
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cbc:Name` = `Mo-99 (with its daughter Tc-99m), maximum activity during transport 97 GBq (9.7 × 10^10 Bq)`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cbc:TransportIndexNumeric` = `1.5`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Category III-YELLOW; maximum dose rate at the surface 0.30 mSv/h`
- Why: the generator has 20 GBq at its reference time 2026-06-21 12:00 UTC (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ItemInstance/cac:AdditionalItemProperty[2]/cbc:Value` = `2026-06-21T12:00:00+00:00`). With the half-life of Mo-99 of 65.94 h (own knowledge), its activity is 20 × 2^(157.3/65.94) ≈ 105 GBq when this declaration is issued (2026-06-14 21:40 −01:00, i.e. 22:40 UTC), and about 150 GBq on 13 June at 12:00 UTC, the day of despatch from Alkmaar (`07-Invoice.xml:/Invoice/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate` = `2026-06-13`). The "maximum activity during transport" for this transport must therefore be at least about 150 GBq, not 97 GBq; 97 GBq is the value for the onward flight on 15 June (`11-Waybill.xml`). The transport index and the surface dose rate, which scale with the activity, are likewise those of the later flight (about 1.5 × 150/97 ≈ 2.3 and 0.46 mSv/h on this flight; still Category III-YELLOW and within the Type A limit, A2 = 0.6 TBq).
- Condition: the radioactive data of this declaration are those of the package on the flight from the Netherlands, consistent with the reference activity, the reference time and the despatch date.
- Options: (a, preferred) the maximum activity at the start of the inbound transport (about 150 GBq) with its transport index and dose rate; (b) leave out the radioactive transport data in the customs declaration, which customs does not need beyond the UN number.
- Needs decision: no

### medicines/08#F2 · Low · The declaration does not say where and on which transport document the generator arrived
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cbc:TransportModeCode` = `4`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `HVI-INV-26-1344`
- Why: as in `03-ImportCustomsDeclaration.xml` (medicines/03#F2): only mode and invoice; no air waybill of the flight from the Netherlands, no airport or office of entry, while `13-ImportCustomsDeclaration.xml` references its waybill.
- Condition: the declaration identifies the transport document of the arrival, or the place of entry.
- Options: as medicines/03#F2.
- Needs decision: no

## Checked and consistent
- Customs value 1,187.00 XBL for 1,000 EUR (1.187 XBL per EUR), against 1.178 a month earlier in `03-ImportCustomsDeclaration.xml`.
- Classification: HS 2844.43 and CPC 33690 for a radioisotope generator; origin Netherlands as the supplier; `AdditionalDocumentReference` resolves to `07-Invoice.xml` with the same item and quantity.
- UN 2915, class 7, ERG 163, no packing group, Type A non-special form (own knowledge).
- Gross weight 18 kg as in the onward documents of the flow.
