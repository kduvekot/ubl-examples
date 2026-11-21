# LLM review: 03-ImportCustomsDeclaration.xml

Flow: medicines (QLM-TX-26-3215) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/03-ImportCustomsDeclaration.xml`, Git blob `c553adcc72727ddf720fe64ca51a87999ada6fb7` (committed)
- Last commit changing the example: a9214989 2026-11-21 Stage 7 Q2: documents are issued within the hours of the desk that issues them
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

### medicines/03#F1 · Low · The consignment's gross weight is the bare product weight of a cold-chain air shipment
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:Consignment/cbc:GrossWeightMeasure` = `172.8`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` = `120`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cbc:GrossWeightMeasure` = `48`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[3]/cbc:GrossWeightMeasure` = `4.8`
- Why: 120 + 48 + 4.8 = 172.8 kg, so the consignment's gross weight leaves nothing for the outer cartons, the insulated packaging of goods shipped at 2 to 8 °C, or the dry-ice box of 120 frozen varicella doses that the order asks for ("the varicella vaccine frozen", `01-Order.xml:/Order/cbc:Note`). The outbound consignment of the same products in this flow weighs 9.5 kg more than its goods items (`06-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:GrossWeightMeasure` = `101.1` against 91.6 kg of goods items).
- Condition: the consignment's gross weight includes its packaging and refrigerant, and exceeds the sum of the goods items' gross weights by a plausible amount.
- Options: (a, preferred) a consignment gross weight with cartons, insulated shippers and dry ice; (b) leave out the consignment's gross weight in the declaration.
- Needs decision: no

### medicines/03#F2 · Low · The declaration does not say where and on which transport document the goods arrived
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cbc:TransportModeCode` = `4`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `NLB-INV-26-1732`
- Why: the declaration names the mode (air) and the invoice but no air waybill and no airport or customs office of entry; the customs party's address is the service's office at a land crossing (Euridice Crossing, Upland State), not Lumeport airport. The Lisavu import of this flow references its air waybill (`13-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference[1]/cbc:DocumentTypeCode` = `Waybill`). For an import declaration the transport document and the place of entry are what customs matches the goods against.
- Condition: the declaration identifies the transport document of the arrival, or the place of entry, as the world's other import declarations do.
- Options: (a, preferred) an `AdditionalDocumentReference` to the air waybill of the flight from India and the airport `XBLMA` as place of entry; (b) at least the airport of arrival.
- Needs decision: no

### medicines/03#F3 · Low · The note speaks of radioactive isotopes, which this declaration does not carry
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `No duty: goods made in India, outside the Accord, but medicines and radioactive isotopes for medicine are free of duty in Bayvarra's tariff…`
- Why: the declaration covers vaccines and insulin only; the reference to isotopes belongs to the generator's import (`08-ImportCustomsDeclaration.xml`), and here reads as copied text.
- Condition: the note gives the duty reason for the goods declared.
- Options: (a, preferred) "medicines and vaccines are free of duty"; (b) keep the general tariff rule, if the note quotes the tariff line.
- Needs decision: no

## Checked and consistent
- Customs values: 32,620.20 + 16,548.78 + 4,535.00 = 53,703.98 XBL for 4,050,000 INR, a uniform rate of 75.41 INR per XBL (line 1: 2,460,000 ÷ 32,620.20; line 2: 1,248,000 ÷ 16,548.78; line 3: 342,000 ÷ 4,535.00, all 75.41); the implied 1.178 XBL per EUR is close to the 1.187 of `08-ImportCustomsDeclaration.xml` a month later.
- Quantities, names and origin India agree with `02-Invoice.xml`; `AdditionalDocumentReference` resolves to it.
- Classification: HS 3002.41 for both vaccines and 3004.31 for insulin in vials; CPC 35270 and 35260 are the CPC 2.1 correspondences of HS 3002 and 3004 (`world/codelists/sources/cpc/CPC21-HS2017.csv`).
- Weights per unit: 0.2 kg per pack of ten syringes, 50 g per 10 ml vial, 40 g per vial with diluent; plausible (own knowledge) and the same as in `06-ForwardingInstructions.xml`.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note`: no tax at import because sales tax is charged at the final retail sale — refuted as a contradiction; consistent with the importer's state sales tax registration in Coastal State.
