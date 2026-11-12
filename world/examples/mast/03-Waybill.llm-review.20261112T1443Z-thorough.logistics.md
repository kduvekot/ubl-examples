# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/03-Waybill.xml`, Git blob `bd3a3f9d377d18d732a5834ff59fed7e413de940` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/03#F1 · High · ShippingOrderID holds the consignment ID, not the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `SE-CS-26-0716`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- XPath: `02-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `SE-FI-26-0714`
- Why: Waybill/ShippingOrderID is "an identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own ID; the forwarding instructions of this flow are SE-FI-26-0714. The waybill therefore does not reference the instruction it executes, and it uses an identifier of one kind (consignment) as another (shipping order). The same pattern is common: 14 of the 19 ShippingOrderID values over `world/examples/*/*.xml` equal a consignment ID of the same document (lxml script over `*.xml` only).
- Condition: `ShippingOrderID` = `SE-FI-26-0714` (or another real shipping order of the flow), and no longer the consignment ID.
- Options: (a) preferred: set it to SE-FI-26-0714, which links the waybill to 02; (b) drop it and reference the forwarding instructions through a DocumentReference.
- Needs decision: no

### mast/03#F2 · High · Hazardous-item package holds six batteries, the handling unit six crates of one
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:Quantity` = `6`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:PackagingTypeCode` = `CR`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[1]/cbc:Quantity` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[6]/cbc:Quantity` = `1`
- Why: Package/Quantity is "the quantity of items contained in this package". Under the loaded hazardous item it says one crate containing six batteries; the handling unit lists six crates SE-CR-1 to SE-CR-6 with one battery each (Package[1] to Package[6], each `1`). Both cannot be true. The physics favour one battery per crate: six batteries of 52 kg net (312 kg / 6) make a 348 kg package in one crate, which would also be far above the per-package limit (F5).
- Condition: the package description under the hazardous item agrees with the handling unit's packages (one battery per crate, six crates), e.g. `Package/cbc:Quantity` = `1` with six such packages, or the hazardous item refers to the six crates.
- Options: (a) preferred: describe the hazardous item's package as one battery per crate (Quantity 1) and state the six crates in the hazardous item quantity; (b) drop the package from the hazardous item, since the handling unit already lists the crates.
- Needs decision: no

### mast/03#F3 · Medium · Shipment gross weight leaves out the transport equipment
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:GrossWeightMeasure` = `3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:GrossWeightMeasure` = `25`
- Why: Shipment/GrossWeightMeasure is defined as "the weight of the goods plus packaging plus transport equipment". 348 + 3 + 25 = 376 kg, i.e. goods and packaging only. The shipment travels in two pieces of transport equipment listed in the same document, an RKN temperature-controlled container (RKN41207K0) and an AKE container (AKE20514K0), whose tare (own knowledge: an active RKN roughly 1 t, an AKE about 80 kg) is not included. The same 376 kg is used in the forwarding instructions, the waybill and the despatch advice.
- Condition: the shipment gross weight includes the tare of the listed transport equipment, or the 376 kg is given in an element whose definition excludes the equipment (e.g. the consignment's gross weight, which excludes the carrier's equipment).
- Options: (a) preferred: put 376 kg on `Consignment/cbc:GrossWeightMeasure` (goods plus packaging, "excluding the carrier's equipment"), and give the shipment weight with tare or leave it out; (b) add the ULD tares to the shipment weight.
- Needs decision: no

### mast/03#F4 · Medium · Air waybill without airports of departure and destination and without flight date
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL209`
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: An air waybill must indicate the places of departure and destination (Montreal Convention Art. 5(a), own knowledge), and the main carriage stage is meaningless for the consignee without them and without a flight date. The stage gives mode, flight and aircraft only; departure can only be guessed from the issue location, and the destination from the consignee's address. The air flow's waybill on the same aircraft has them (`air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMA`, `air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`, with a requested departure event).
- Condition: the main carriage stage has a loading and an unloading port location (Lumeport airport and Selanu airport, with UN/LOCODE) and a departure date (requested or planned).
- Options: (a) preferred: add LoadingPortLocation XBLMA, UnloadingPortLocation XLSLA and a RequestedDepartureTransportEvent, as in air/04; (b) at least the two airports.
- Needs decision: no

### mast/03#F5 · Medium · Battery crates exceed the cargo-aircraft limit of PI 965 Section IA
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:NetWeightMeasure` = `312`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- Why: Calculated from the document: 348 kg gross / 6 crates = 58 kg per crate; one battery alone weighs 312 / 6 = 52 kg. IATA PI 965 Section IA (own knowledge) allows at most 35 kg gross per package on cargo aircraft; heavier batteries need the approval of the State of Origin under special provision A99, and that approval travels with the shipment. The document states CAO and PI 965 IA but no approval, so the declared packing does not permit what is packed.
- Condition: either each package is within 35 kg gross, or the document carries the A99 approval (reference and description) that permits the heavier packages.
- Options: (a) preferred: add a reference to the A99 approval of Bayvarra's aviation authority (e.g. in the hazardous goods transit description and a document reference), because the battery size is part of the story; (b) use smaller battery modules within 35 kg.
- Needs decision: yes

### mast/03#F6 · Low · "Three originals" but only one original is distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note says the waybill is made out in three originals for consignor, consignee and carrier (as the Montreal Convention provides), but the distribution lists only the consignee's original (handed to the handling agent at Selanu) and an electronic copy for the forwarder. The consignor's and the carrier's originals are not distributed, and the consignor's original would go to the forwarder acting for Saltmere.
- Condition: the distribution and the note describe the same set of originals and copies.
- Options: (a) preferred: add the consignor's original (to the forwarder or Saltmere) and note the carrier's original kept by Kelaro; (b) shorten the note to what is distributed.
- Needs decision: no

### mast/03#F7 · Low · Orange-plate numbers on an air ULD
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: The orange plate is an ADR/RID marking for road and rail vehicles and tank/bulk containers (own knowledge); the numbers 90/3480 are correct for UN 3480 but have no use in a ULD carried on a cargo aircraft, which is the only stage in the flow. The document gives no road leg in which the equipment would need them.
- Condition: orange-plate numbers appear only where a road or rail leg of the equipment needs them.
- Options: (a) preferred: remove them; (b) keep them only if a road leg with this equipment is added.
- Needs decision: no

### mast/03#F8 · Low · Packaging danger level "4" under the UN/EDIFACT 8339 list ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:PackagingDangerLevelCode` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:PackagingDangerLevelCode` = `4`
- Why: To my knowledge UN/EDIFACT 8339 (Packaging danger level) has only the codes 1, 2 and 3 (great, medium, minor danger). The world's copy of the list (`UNCL8339Code.gc`, "UBL example world") adds "4 Not assigned". If 8339 D22A has no code 4, a world-made code is published under a real list ID. I could not check the official directory (UNECE blocks automated access).
- Condition: every code given with `listID="UN/EDIFACT EDED 8339"` is in the official 8339 list; for entries without packing group the element is omitted or uses a world list.
- Options: (a) preferred: omit the element for UN 3480 and UN 2911 (no packing group); (b) keep "4" only if the official directory has it.
- Needs decision: yes

### mast/03#F9 · Low · Cargo-aircraft-only liquid in a closed AKE without CAO data
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:Quantity` = `20`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: UN 2920 PG II in 5-litre cans exceeds the passenger-aircraft limit (PI 851: 1 L) and can only fly on cargo aircraft (PI 855: 30 L) (own knowledge). Cargo-aircraft-only packages of class 8 must be loaded so that the crew can reach them in flight; a closed AKE container is not accessible. The battery equipment carries CAO, packing instruction and "Main deck, accessible", but the AKE with the corrosive liquid carries no transit data, no packing instruction and no accessibility statement.
- Condition: the UN 2920 cans carry their CAO status and packing instruction, and their stowage allows crew access (or the document states how the requirement is met).
- Options: (a) preferred: give the AKE's hazardous item its own HazardousGoodsTransit (PI 855, CAO) and stow the cans accessibly (e.g. loose on an accessible position or in an open ULD); (b) pack the liquid in inner packagings of at most 1 L so that it may also fly on passenger aircraft.
- Needs decision: yes

## Checked and consistent
- Equipment, weights, quantities and stowage are identical to the forwarding instructions (`02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cbc:ID` = `AKE20514K0`): physics as calculated there (52 kg and 40 L per battery, 92 Wh/kg, 1,300 kg/m³; 36 kg packaging for six crates; stripper 20 L ≈ 18–20 kg plus cans against 25 kg; total 376 kg = 348 + 3 + 25).
- Aircraft: ATR 72 freighter (main deck only, takes LD3-size containers, payload of several tonnes, own knowledge); positions "MD-2" and "MD-6" are main-deck positions, and 376 kg plus two ULDs is well within its payload. The same aircraft QL-KXA flies KXL207 in the air flow.
- Mode 4 (air) for the main carriage of a waybill typed AWB by an air carrier; CAO in the transit data matches a freighter.
- Dates: waybill 2026-06-04 17:15, after the forwarding instructions (2026-06-03 11:57) and the despatch advice (2026-06-04 13:20), before the invoice (17:34).
- Consignment and shipment IDs are the same as in 02 and 04.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:ProperShippingName`: the waybill carries no goods items, so the nature of the goods might be missing — refuted: each of the three goods is described by its proper shipping name, UN number and weights in the loaded hazardous items, which is what an air waybill needs.
- `/Waybill/cbc:CarrierAssignedID`: "KXL-AWB-26-0713" is not in the 11-digit AWB format (3-digit prefix + 8 digits) — refuted as a finding: an obviously fictional number avoids being mistaken for a real AWB.

## Outside this review
- On-carriage from Selanu airport to the mast site under CPT (01-Order) is not shown in any transport document of the flow; whether and by whom it was carried belongs to the cross-document review (also raised as missing information in 02, mast/02#F2).
- Whether flight KXL209 has room for both ULDs with the other loads of that day (capacity across documents).
