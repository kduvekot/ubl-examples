# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
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

### packaging/01#F1 · Low · The order says nothing about when the goods are wanted
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`
- Why: The order names the despatch party, the buyer's carrier and the FCA place, so the seller knows who collects and where, but neither `Delivery` nor `Delivery/Despatch` carries a requested delivery or despatch period (`RequestedDeliveryPeriod`, `Despatch/RequestedDespatchPeriod`, `LatestDeliveryDate`). Under FCA the seller must have the goods ready when the buyer's carrier arrives; without a date the order does not say when that is, and nothing else in the flow does (no order response, no despatch advice). This is a completeness remark, not a contradiction: an order can rely on agreed lead times. The same gap occurs in 15 of the world's 18 orders (`*/*-Order.xml` without any of `RequestedDeliveryPeriod`, `PromisedDeliveryPeriod`, `EstimatedDeliveryPeriod`, `LatestDeliveryDate`, `RequestedDespatchPeriod`), including all three orders of this flow.
- Condition: the order states when the goods are to be ready for collection (a requested despatch period under `Delivery/Despatch`, or a requested delivery period), or the flow's story records that a standing lead time applies.
- Options: (a, preferred) add `Delivery/Despatch/cac:RequestedDespatchPeriod` with the collection window, since under FCA the despatch (collection) is the delivery; (b) `Delivery/cac:RequestedDeliveryPeriod`; (c) leave it and say in a note that the standard lead time applies.
- Needs decision: no

### packaging/01#F2 · Low · The buyer's logistics service provider plays no part in this order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: `ServiceProviderParty` is "A party providing a service to this party". Castrano Logistics is given as Valdara's warehousing and despatch provider, but this order has the goods collected under FCA by Trasvia Haulage at the seller's premises and nothing in the order is delivered to, stored by or despatched by Castrano. It reads as master data copied into a document that does not use it. The same block (`VI-SP-2026-01`) occurs in 75 examples (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: the order carries Castrano Logistics only if it has a role in this delivery (e.g. as the delivery party or receiving warehouse), otherwise not.
- Options: (a, preferred) drop the service provider from the buyer party in documents where it has no role; (b) give it a role here, e.g. make Castrano's warehouse the delivery location the carrier takes the film to, which would also answer where the goods go.
- Needs decision: no

### packaging/01#F3 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` and the account `XB96BLUM38020504712805` pass.
- Physics, roll weight against film: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `480` kg at 16 kg per roll (item description) is exactly 30 rolls. A 16 kg roll of 23 µm film (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty/cbc:ValueQuantity` = `23`, unit 4H = micrometre) of polyethylene at about 920 kg/m³ (own knowledge), at the usual machine-roll width of 0.5 m (assumed; the width is not stated), holds 16 / (0.5 × 23·10⁻⁶ × 920) ≈ 1 510 m of film, which is a normal machine stretch-film roll (1 500–2 000 m). Its diameter on a 76 mm core is about 0.22 m (film cross-section 1 510 m × 23 µm = 0.035 m²), so the 30 rolls stand on one 1.2 × 0.8 m pallet in two layers of 15 (5 × 3), about 1 m high; no pallet is stated, so this is only a plausibility check.
- Delivery terms: `/Order/cac:DeliveryTerms/cbc:ID` = `FCA` at the seller's dispatch; the carrier named under `Delivery/Despatch` (Trasvia Haulage, ISIC 4923 road freight, Urvanian, with an international road haulage permit valid to 2030-06-30) is the buyer's, as FCA requires, and the despatch party is the seller (`20412740`, same as the seller party).
- Codes: HS `392010` (film of polymers of ethylene) and CPC `36330` fit stretch film; unit `KGM` for quantity and base quantity; origin XB fits a Bayvarran producer.

## Considered and refuted
- `/Order/cac:Delivery/cac:Despatch`: suspected that a despatch block does not belong in an order — refuted because under FCA the buyer tells the seller which carrier collects, which is what `Despatch/CarrierParty` ("The Party who provides the transport of goods between named points") says.
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rivermouth Packaging, dispatch, Lumeport`: suspected a location without address or identifier — refuted because the place is the seller's own premises, whose address is in the seller party; the description names it sufficiently for FCA.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:EndOfLifeTreatment/cac:TreatmentLocation/cbc:Name` = `Rinova Recovery's plant, Ferrano`: suspected a mismatch between the named town and the country — refuted because Ferrano is in Urvania (the buyer's town) and the address gives XU.

## Outside this review
- Whether Trasvia Haulage's road leg from Lumeport (XB) to Ferrano (XU) runs on a route of the map is a question of location across the world, not of this example.
