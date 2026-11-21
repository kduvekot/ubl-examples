# LLM review: 03-DespatchAdvice.xml

Flow: modification (MDS-TX-26-0047) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/modification/03-DespatchAdvice.xml`, Git blob `b9d58739e42874137c38283a7bfff67fa81e89e6` (committed)
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

### modification/03#F1 · Medium · The sawmill's blank code is given as the seller's item identification
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `MDS-BL-1830`
- Why: SellersItemIdentification is "assigned by the seller". The blanks are Marrowdale Sawmill's own goods, sent for processing; the sawmill is the despatch party here and the buyer in the order (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`), and nobody sells the blanks. Same problem as 01#F1.
- Condition: the code is in an item identification whose definition names the party that assigned it, the same as in 01.
- Options: (a) preferred: ManufacturersItemIdentification or BuyersItemIdentification, aligned with the fix of 01#F1; (b) StandardItemIdentification only if the code were a shared standard, which it is not.
- Needs decision: no

### modification/03#F2 · Low · The delivery customer's contact is Tostara's sales office
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Sales coordinator`
- Why: The delivery customer's contact receives the goods; the note asks the receiver to check the blanks on arrival and keep them apart. A goods-in or store contact fits; Tostara has a "Customs and stock clerk" in 05.
- Condition: Tostara's contact as delivery customer is a receiving or store contact.
- Options: (a) preferred: Tostara's goods-in / store contact; (b) keep the sales office if it is the plant's single point of contact, and say so.
- Needs decision: no

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `MDS-PO-26-0047` resolves to 01; `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1.1` is the sub-line of the blanks in 01.
- 2,400 blanks on 12 pallets agree with `/DespatchAdvice/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `12`, with 01's note (2,400 per load) and with 04 and 05 (same shipment, consignment, weight and quantity).
- Physics: one blank 1.830 × 0.101 × 0.051 m = 0.00943 m³; 2,400 blanks = 22.6 m³. Gross 14,448 kg less about 12 × 25 kg of pallets (own estimate) is about 14,150 kg, or about 625 kg/m³: plausible for kiln-dried ash (about 650–700 kg/m³ at 12 % moisture, own knowledge), and a load a lorry carries.
- Dates: manufacture 2026-01-09 and lot `MDS-BL26-0109` before the despatch of 2026-01-13.
