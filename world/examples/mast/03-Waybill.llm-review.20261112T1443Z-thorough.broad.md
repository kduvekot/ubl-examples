# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### mast/03#F1 · Medium · Shipping order ID holds the consignment ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `SE-CS-26-0716`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- Why: ShippingOrderID is the "reference number to identify a Shipping Order", i.e. the shipper's
  or forwarder's booking instruction to the carrier. The value is the consignment's identifier; the
  instruction in this flow is the forwarding instructions SE-FI-26-0714 (02), and the forwarder's
  booking with Kelaro is not in the flow. 14 of the 19 examples with a ShippingOrderID set it to a
  consignment ID of the same document (script over *.xml: ShippingOrderID value equal to a
  Consignment/cbc:ID in the file).
- Condition: ShippingOrderID is the identifier of a shipping order (booking) that exists in the
  story, or is absent.
- Options: (a, preferred) drop it, or use the forwarder's booking number if the world has one;
  (b) refer to 02 with a document reference if that is what is meant.
- Needs decision: no

### mast/03#F2 · Medium · An air waybill without airports of departure and destination or flight date
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL209`
- XPath: `/Waybill/cbc:Description` = `A cargo-aircraft-only flight to the island.`
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: An air waybill states the airport of departure, the airport of destination and the
  requested flight and date (own knowledge: Montreal Convention art. 5, IATA AWB). The main-carriage
  stage has a flight number, aircraft type and registration but no loading or unloading location,
  no departure or arrival time; the only place is the issue location, given by name only; the
  destination is "the island". The waybill's purpose depends on them.
- Condition: the main-carriage stage states the airport of departure and of destination (with
  their identifiers) and the flight's planned departure date.
- Options: (a, preferred) LoadingPortLocation and UnloadingPortLocation (or the stage's
  departure/arrival locations) with IATA location codes or UN/LOCODEs of the world, and
  EstimatedDepartureDate; (b) at least the two airports.
- Needs decision: no

### mast/03#F3 · Medium · Language codes in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639)
  is a language, not a locale. 213 examples carry it.
- Condition: LocaleCode is a locale (e.g. en-XB) or absent.
- Options: (a, preferred) `en-XB`; (b) drop it.
- Needs decision: no

### mast/03#F4 · Low · "Three originals" but only one original distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note announces three originals for consignor, consignee and carrier; the distribution
  lists the consignee's original (with the goods, to Selanu Airport Cargo) and an electronic copy to
  the forwarder, but no original for the consignor (or the forwarder acting for it) and none kept
  by the carrier.
- Condition: the distribution matches the note: each original listed, or the note says what is
  distributed.
- Options: (a, preferred) add the consignor's original (to Bayforth as agent) and the carrier's;
  (b) change the note.
- Needs decision: no

### mast/03#F5 · Low · Each lithium-battery crate exceeds the cargo-aircraft limit of PI 965 IA
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- Why: 348 kg in six crates = 58 kg per package; PI 965 Section IA allows 35 kg gross per package on
  cargo aircraft (own knowledge), more only with a State-of-Origin approval under special provision
  A99, which the waybill does not mention. A carrier accepting the waybill would have to see it.
- Condition: packages within the limit, or the approval referenced.
- Options: (a, preferred) reference the A99 approval; (b) change packing or weights.
- Needs decision: yes

### mast/03#F6 · Low · Road data and negatives without a reason on an air waybill
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:TransportEmergencyCardCode` = `TEC9`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:InhalationToxicityZoneCode` = `NOTTOXIC`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumanFoodApprovedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure` = `60`
- Why: Orange plates and road emergency cards belong to road/rail vehicles, not to an air
  waybill; an inhalation-toxicity zone of "not toxic", food approvals of a battery container, and an
  emergency temperature (a concept for temperature-controlled self-reactive substances and organic
  peroxides) have no business reason for lithium batteries on an aircraft (IND5). The
  HazardousGoodsTransit block appears three times with the same content.
- Condition: every dangerous-goods element present applies to air carriage of these goods, stated
  once where it applies.
- Options: (a, preferred) drop them; (b) keep road data only in a road stage, if there is one.
- Needs decision: yes (affects coverage)

### mast/03#F7 · Low · Two ULDs of the same kind coded differently
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `AM`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- Why: Both RKN41207K0 (temperature-controlled LD3-size container) and AKE20514K0 (LD3) are ULDs;
  only one is coded as ULD.
- Condition: both are coded as ULDs, the RKN's temperature control in the refrigeration elements.
- Options: (a, preferred) UL for both.
- Needs decision: no

### mast/03#F8 · Low · Contacts that do not fit the roles
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Business accounts`
- Why: The carrier's contact is named "Cargo sales" but its job title is operations planner. The
  consignor's contact is its procurement office and the consignee's a sales desk, while the AWB's
  consignee contact must be reachable for arrival notification of dangerous goods.
- Condition: name, title and department of each contact agree, and each fits the role.
- Options: (a, preferred) role-specific contacts (carrier operations, consignor shipping,
  consignee goods receipt).
- Needs decision: no

### mast/03#F9 · Low · Two different numbers for the waybill from the same party
- XPath: `/Waybill/cbc:ID` = `KXL-WB-26-0717`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0713`
- Why: ID is "assigned by the sender" and CarrierAssignedID by the carrier; here sender and
  carrier are the same party (Kelaro Air Cargo), yet the two numbers differ. A reader cannot tell
  which is the air waybill number to quote. The serial 0713 is also the serial of the order
  ST-PO-26-0713, which looks accidental.
- Condition: either one number, or the two numbers have a stated difference in meaning.
- Options: (a, preferred) drop CarrierAssignedID, or make it the AWB number and ID the document's
  message number with a reason; (b) explain.
- Needs decision: no

### mast/03#F10 · Low · A mast operator classified as a wired telecom
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120); see the review of 01.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes

## Checked and consistent
- Shipment SE-SH-26-0715, consignment SE-CS-26-0716, ULDs, packages, weights (376 kg) and DG data
  agree with 02 and 04.
- Parties: Kelaro Air Cargo as sender, carrier and signatory; Bayforth Forwarding as receiver and
  forwarder; consignor Saltmere; consignee Selanu Telecom — consistent with 02 and 04.
- Issued 2026-06-04 17:15, after the despatch advice (13:20) and the forwarding instructions
  (2026-06-03).
- KXL is recorded as a fictional ICAO-style designator not assigned in the real lists
  (world/codelists/sources/icao/airline-designators.txt); ATF is the real IATA code for the ATR 72
  freighter (world/codelists/sources/optd).
- A cargo-aircraft-only flight matches both the UN 3480 batteries and the 5-L cans of UN 2920 PG II.

## Considered and refuted
- `/Waybill/cbc:CarrierAssignedID`: not in IATA AWB form (3-digit prefix + 8 digits) — refuted:
  deliberately fictional so as not to collide with a real airline prefix (source note in
  world/codelists/sources/icao); the remaining issue is F9.
- `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name`: the consignee's original
  sent to Selanu Airport Cargo — refuted: the ground handler at destination holds it for the
  consignee.

## Outside this review
- Whether an RKN and an AKE fit an ATR 72 freighter at main-deck positions MD-2 and MD-6, and
  whether flight KXL209 runs on that day, are capacity and timeline questions.
