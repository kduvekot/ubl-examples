# LLM review: 01-Order.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/01-Order.xml`, Git blob `af435c2882d01f0ca686e44a410c2da3f745d496` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/01#F1 · Low · Item number in the world's item scheme is a valid GTIN-12 in the real UPC range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: `StandardItemIdentification` is "identifying information for this item, assigned according to
  a standard system"; the schemeID is the world's own item scheme, not GS1. The number is twelve
  digits with a correct GTIN-12 (UPC-A) check digit (weights 3/1 from the right over
  `77101000001`: 37, check digit 3). As a GTIN-13 it reads `0771010000013`, prefix 077, which is in
  the GS1 US range (000–139). Read without the schemeID (as a scanner or a GTIN field would), it
  can be mistaken for a real GTIN, which the repository's rule on fictional values forbids. I could
  not check whether this exact key is assigned (own knowledge of the GS1 prefix ranges; no register
  lookup). The same scheme and number style is used for 8 distinct item numbers in 64 examples
  (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`).
- Condition: the item number cannot be read as a valid GTIN in a real GS1 prefix range, or a recorded
  decision states why this form is safe.
- Options: (a, preferred) change the check-digit rule or the length of the world's item scheme so
  the numbers are not valid GTINs; (b) keep it and record in the decisions why the world scheme is
  unambiguous through its schemeID.
- Needs decision: yes

## Checked and consistent
- Physics: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800` (TNE) as "one train"
  (`/Order/cbc:Note[2]` = `Monthly call-off, one train.`). 04-DespatchAdvice.xml states 30 wagons of
  about 60 t: 30 × 60 t = 1800 t. A 60 t payload of lump iron ore at a bulk density of about
  2.3–2.8 t/m³ (own knowledge) is 21–26 m³, well inside a four-axle open ore wagon (about
  40–75 m³); with a tare of about 22–25 t the wagon weighs 82–85 t, 20.5–21.3 t per axle, under the
  usual 22.5 t limit. Plausible.
- Delivery terms `FCA` at `Mine siding, Serravona` agree with the buyer naming the carrier
  (`/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`)
  and with the buyer booking the transport in 02-TransportExecutionPlanRequest.xml.
- Requested delivery period 2026-03-09 to 2026-03-13 contains the transport window of
  02-TransportExecutionPlanRequest.xml (start 2026-03-10, end 2026-03-13).
- HS `260111` and CPC `14100` fit the description "Non-agglomerated iron ore, lump size 10–30 mm,
  62 % Fe"; lump 10–30 mm is a usual lump fraction.
- The seller's location: UN/LOCODE-style `XUSRV` in the fictional country XU; coordinates 39°54.00′ S,
  15°30.60′ W, and the addresses' `TimezoneOffset` of -1 (in 02/03) match the solar offset at 15.5° W
  (15.51 / 15 = 1.03 h).
- Item identifiers, names, classification and iron content are identical in 04-DespatchAdvice.xml and
  07-Invoice.xml.

## Considered and refuted
- `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09`: suspected a clash
  with FCA (delivery at the seller's siding) and with the transport starting on 2026-03-10 —
  refuted because the period is a window, and the actual handover on 2026-03-10 lies inside it.
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries` without a
  delivery location: suspected missing place of delivery — refuted because under FCA the contracted
  place is given in `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Mine siding, Serravona`.
