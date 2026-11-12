# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/03-Order.xml`, Git blob `4c3acea07de9e59031f62d8970fa32ff7a492ca6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### packaging/03#F1 · Low · The order says nothing about when the goods are wanted
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: Under `DeliveryTerms` DAP the seller delivers to the mill's goods-in, and `Delivery` names the delivery party, but no requested delivery period or latest delivery date is given, so the order does not say when Rivermouth Packaging is to deliver. The garment bags are needed before the mill packs the store's shirts (`05-Order.xml`, despatched in `06-DespatchAdvice.xml` on 2026-05-12), so the timing has a business reason in the flow. Completeness remark. The same gap occurs in 15 of the world's 18 orders (`*/*-Order.xml` without any of `RequestedDeliveryPeriod`, `PromisedDeliveryPeriod`, `EstimatedDeliveryPeriod`, `LatestDeliveryDate`, `RequestedDespatchPeriod`).
- Condition: the order states when the bags are to be delivered, or the flow records that a standing lead time applies.
- Options: (a, preferred) add `Delivery/cac:RequestedDeliveryPeriod`, which is the element for a DAP delivery date; (b) `Delivery/cbc:LatestDeliveryDate`; (c) a note on the standard lead time.
- Needs decision: no

### packaging/03#F2 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- Delivery: `/Order/cac:DeliveryTerms/cbc:ID` = `DAP` with the place `Lumeport Textile Mill, goods-in`; the delivery party is the buyer itself (`20412603`), whose address is in the buyer party. No carrier is named, which is right: under DAP the seller arranges carriage.
- Physics, count against packing: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20000` bags in boxes of 500 (description) is exactly 40 boxes. A 60 cm wide garment cover of about 1 m length and 15 µm film, two layers, weighs about 0.6 × 1.0 × 2 × 15·10⁻⁶ × 920 kg/m³ ≈ 17 g (dimensions other than the 60 cm and the film thickness are my own assumption, not stated), so a box of 500 is about 8 kg and the order about 330 kg: a normal parcel or small-van delivery inside Lumeport.
- Codes: HS `392321` (sacks and bags of polymers of ethylene) and CPC `36410` fit a PE garment bag; unit `EA` for quantity and base quantity.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garment bag of recycled polyethylene, 60 cm, boxes of 500.`: suspected that "60 cm" does not say which dimension, so its fit with the shirts of `05-Order.xml` cannot be checked — refuted because 60 cm is the usual width designation of garment covers, wider than a shirt on a hanger (about 42–46 cm, own knowledge); the description is enough for the order.
