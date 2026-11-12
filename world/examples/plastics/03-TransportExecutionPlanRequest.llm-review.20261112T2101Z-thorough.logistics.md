# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/03-TransportExecutionPlanRequest.xml`, Git blob `ce4cb0e21e72b3398e1856fda182f568fe87940d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/03#F1 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: A Transport Execution Plan Request is "a document sent by a transport user to request a transport service". The only consignment carries an ID, a gross weight and five false indicators, but no goods item, no description, no number or type of packages and no volume. The carrier is asked to plan a barge without being told that the cargo is 120 jumbo bags of PE granulate (about 204 m³, see `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`). The indicators only say what the cargo is not. A transport request that does not say what is to be carried is the skill's own example of missing information the purpose depends on.
- Condition: The consignment of the request describes the goods to be carried: at least a description (or goods item) and the number and type of packages (120 × JB), ideally also the volume, matching 06.
- Options: (a) preferred: add a `cac:GoodsItem` (description, quantity, gross weight, `ContainingPackage` or package count) or, at consignment level, `TotalPackagesQuantity`, `GrossVolumeMeasure` and a goods description, because the carrier needs those to accept the load; (b) add `cac:Consignment/cac:TransportHandlingUnit` with the 120 bags.
- Needs decision: no

### plastics/03#F2 · Medium · From and to locations are the parties' office addresses, not the quays
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- XPath: `/TransportExecutionPlanRequest/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`
- Why: `FromLocation` is "the location of origin of the transport service". Here it is named after the carrier and carries the carrier's own postal address (the same street, number and postal zone as `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone` = `4170`), while the note says the barge starts at "the quay next to the recovery plant" (Rinova, postal zone 4140). The plan that answers this request loads at `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`. Likewise `ToLocation` is the consignee's business address (AddressTypeCode BUSINESS), while unloading is at `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`, the CPT place of the order. A location's name is the place, not the company.
- Condition: `FromLocation` is the place where the service starts (Rinova's quay in Ferrano) and `ToLocation` the place where it ends (the river quay in Lumeport), named as places and consistent with the loading and unloading locations of 04 and 06 and with the note.
- Options: (a) preferred: name and locate the two quays (with an address or location identifier for each) and use the same values in 03, 04 and 06; (b) if the barge really starts at the carrier's base, say so in the note and keep the loading quay as a separate stage location.
- Needs decision: no

## Checked and consistent
- Gross weight: 120 bags × 1000 kg net + 120 × 4 kg bag tare = 120480 kg, matching 04, 05, 06, 08 and 09 (tare per bag derived from 06: 120480 − 120000 = 480 kg; a woven-PP 1 t jumbo bag weighs about 2.5–5 kg, own knowledge).
- `BulkCargoIndicator` = false fits goods in jumbo bags.
- Service window 2026-04-19 to 2026-04-22 and response deadline 2026-04-15 agree with the plan (04 issued 2026-04-15 13:10, same window).
- Consignment `RR-CS-26-0885` is the same consignment ID in 04, 05, 06 and 08.
- `TransportUserParty` and `BillToParty` = Rinova fit CPT (seller pays carriage).

## Outside this review
- Timeline across documents: this request is issued 2026-04-14 09:57, before the seller accepts the order (`02-OrderResponse.xml:/OrderResponse/cbc:IssueTime` = `15:39:00` on the same day). A seller may book transport before formally confirming, but whoever checks the flow's timeline may want to look at it.
