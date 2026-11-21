# LLM review: 04-WeightStatement.xml

Flow: waste (9900043338) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/waste/04-WeightStatement.xml`, Git blob `9c968df28300fde5767f30a29fbe35be53b49d2e` (committed)
- Last commit changing the example: 0cee647c 2026-11-20 Stage 5, C74, C75, C76: issuers' own numbering, one code per company, collaborations
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### waste/04#F1 · Low · Driver identifier without a scheme
- XPath: `/WeightStatement/cac:Shipment/cac:ShipmentStage/cac:DriverPerson/cbc:ID` = `XU-DL-0417722`
- Why: `Person/ID` is "An identifier for this person". The value looks like an Urvanian driving-licence number (prefix XU-DL), but it carries no `schemeID`, while every other identifier in the document names its register. The agreed rule is that identifiers name their scheme; without one the reader cannot tell a licence number from an employee or haulier number. The same ID without scheme occurs in all 3 `DriverPerson` elements of the examples (grep over `*.xml`: waste/02, waste/04, road/08).
- Condition: The driver's ID carries a `schemeID` naming the register it comes from (e.g. the Urvanian driving-licence register), consistent in waste/02, waste/04 and road/08.
- Options: (a) preferred: a world scheme for driving licences (e.g. `urn:ubl-examples:world:XU:driving-licence`), since a weighbridge ticket records the licence; (b) leave the ID out, if the driver's name is enough for the statement.
- Needs decision: no

## Checked and consistent
- Arithmetic: gross 38 200 kg (loaded, 10:07) − tare 15 300 kg (empty, 10:46) = 22 900 kg net, as in `/WeightStatement/cac:Shipment/cbc:NetWeightMeasure`; the same net weight is in `02-WasteMovement.xml` (22 900 kg) and invoiced in `03-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `22.9` (TNE).
- Times: delivery at the recovery facility at 10:05 (`02-WasteMovement.xml`), loaded weighing at 10:07, empty weighing at 10:46, statement issued at 10:50; 02 (issued 11:45) refers to this statement.
- Physics: 54 bales of 22 900 kg = 424 kg per bale, plausible for baled PE film; 22.9 t payload with a tare of 15.3 t for tractor and trailer gives 38.2 t, within the usual 40 t for an articulated vehicle.
- Shipment 7400043504, consignment 7300043504, 54 bales (BL), waste code 150102, vehicle UR 4160 KT / UR 4160 TR, owner Trasvia Haulage and driver agree with `02-WasteMovement.xml`; ProfileExecutionID 9900043338 as in 01–03; the description and code agree with `01-WasteNotification.xml`.

## Considered and refuted
- `/WeightStatement/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Logistics planner`: a planner rather than the weighbridge operator as the contact of a weight statement — refuted: the sender's contact is who answers questions on the statement, and the logistics desk that plans the loads is a fair choice.
- No weighing date or device in structured form — refuted: the UBL 2.5 WeightStatement has no element for them; the times are given with each measurement.
