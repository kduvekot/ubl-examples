# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: context

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

### mast/03#F1 · High · Shipping order reference holds the consignment ID, not the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `SE-CS-26-0716`
- XPath: `02-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `SE-FI-26-0714`
- XPath: `02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The forwarding instructions of this flow have the ID `SE-FI-26-0714`; `SE-CS-26-0716` is the consignment's ID, which the waybill already carries in its own consignment. An identifier of one kind is used as another, and the reference does not resolve to the forwarding instructions.
- Condition: ShippingOrderID is the ID of the forwarding instructions (or shipping order) the waybill was issued for.
- Options: (a, preferred) set it to `SE-FI-26-0714`; (b) remove it if the carrier did not receive the forwarding instructions (they were issued to the forwarder, the waybill's receiver).
- Needs decision: no

### mast/03#F2 · Medium · Air waybill without airport of departure and destination
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `4`
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- Why: The waybill is "A transport document describing a shipment"; an air waybill under the Montreal Convention must indicate the places of departure and destination (Montreal Convention art. 5; own knowledge). The main-carriage stage has mode, flight and aircraft but no loading or unloading location, no departure or arrival time, and the shipment has no delivery location; the destination is only implied by the consignee's address and the distribution to Selanu Airport Cargo. The issue location (Lumeport Airport Cargo Terminal) is where the waybill was issued, not the departure airport by definition. The document's purpose depends on these places.
- Condition: The main carriage states the airport of departure and the airport of destination (e.g. LoadingPortLocation and UnloadingPortLocation, or the stage's departure and arrival events), and where useful the flight date.
- Options: (a, preferred) add loading and unloading airport locations (with their identifiers as used elsewhere in the world) and the planned departure to the main-carriage stage; (b) at least the destination in a Delivery.
- Needs decision: no

### mast/03#F3 · Medium · Numbered orange placard for packaged goods carried by air
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: UpperOrangeHazardPlacardID and LowerOrangeHazardPlacardID are "The number for the upper/lower part of the orange hazard placard required on the means of transport". Orange plates are an ADR/RID requirement for road vehicles and rail wagons; for goods in packages ADR 5.3.2.1.1 requires plain orange plates without numbers, and numbered plates only for tanks and bulk (own knowledge). These items travel packed in a ULD (`RKN41207K0`) on a cargo aircraft (`CAO`), where no orange plate exists. No means of transport in this flow requires the numbers 90/3480, so the condition in the definition is not met. The waybill is the air carrier's document for exactly that flight. The same values are in 02.
- Condition: Orange placard numbers are given only for goods whose means of transport requires numbered orange plates (tank or bulk carriage by road or rail).
- Options: (a, preferred) remove both elements; (b) if a road pre-carriage to the airport is meant, still no numbers apply to packages — mention the plain plates in text if needed.
- Needs decision: no

### mast/03#F4 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value repeats the language code from Language/ID (`en`, list ISO 639); it does not name a locale (a language in a country or region, e.g. English as used in Bayvarra). A language code in LocaleCode is the case section 6 names as Medium. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' -o '<cbc:LocaleCode[^<]*' world/examples | sort | uniq -c`; every occurrence is `en` with list ISO 639).
- Condition: LocaleCode, where present, holds a locale identifier (language plus territory, e.g. `en-XB`) from a list of locales, or it is absent.
- Options: (a, preferred) remove LocaleCode, since Language/ID already says English and nothing in the document depends on a locale; (b) use a locale code such as `en-XB` with a locale list as listID, consistent with the `en-XB`/`en-XL` languageIDs used elsewhere.
- Needs decision: no

### mast/03#F5 · Low · Note on three originals does not match the distribution list
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionType[2]` = `Electronic copy`
- Why: The note says there are three originals, for consignor, consignee and carrier (as on a real air waybill). The distribution list names only the consignee's original (handed with the goods to Selanu Airport Cargo) and an electronic copy for the forwarder; the consignor's original, for Saltmere Engineering, is not distributed to anyone, and the forwarder receives only a copy although it is the waybill's receiver. Free text and structure disagree.
- Condition: The distribution list and the note agree on which originals exist and who receives them (in particular the consignor's original).
- Options: (a, preferred) add the consignor's original to the distribution (to Saltmere, or to Bayforth on its behalf); (b) reword the note to what is distributed.
- Needs decision: no

### mast/03#F6 · Low · Freight forwarder role defined as a consolidator, but the waybill is not consolidated
- XPath: `/Waybill/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- Why: The FreightForwarderParty is defined in UBL as "The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart who mirrors the consolidator's activity". In this flow Bayforth does not consolidate: the air waybill is not consolidated (`03-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`) and there is one consignment of one consignor. The party is the forwarder in the ordinary sense (it arranges the carriage), which the UBL definition does not cover. Whether to keep the role and record the narrow definition, or treat it as a misuse, could not be settled here.
- Condition: Either FreightForwarderParty is used for a party that consolidates, or the use for a non-consolidating forwarder is recorded as a deliberate reading (finding on the UBL definition).
- Options: (a, preferred) keep the role (ForwardingInstructions are by definition "issued to a forwarder") and record the narrow definition for the UBL TC write-up; (b) make the shipment a consolidation, which changes the story.
- Needs decision: yes

### mast/03#F7 · Low · Hazardous-item notification party is the consignor itself
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: HazardousItemNotificationParty is "The Party who is notified of a Hazardous Item in this Consignment". It names Saltmere Engineering, the consignor, which declared the dangerous goods itself and needs no notification of them. A party that has to be notified would be someone else (consignee, airport, authority), and the consignor as emergency contact is already the ContactParty of the hazardous item.
- Condition: HazardousItemNotificationParty, where present, names a party other than the one that declares the goods, which has to be notified of them.
- Options: (a, preferred) remove it, since the consignor is already the emergency contact; (b) name the party that has to be notified in the story (e.g. the consignee or the destination airport cargo terminal).
- Needs decision: no

### mast/03#F8 · Low · Reefer settings and food approvals that do not serve this shipment
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumidityPercent` = `50`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AnimalFoodApprovedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumanFoodApprovedIndicator` = `false`
- Why: As in 02: the temperature range has a reason for the batteries, but air flow, humidity and "not approved for food" have none in this shipment; the false indicators only say what their absence would say (no-filler rule).
- Condition: Every reefer setting and approval indicator of the unit serves the goods carried (or the story says why).
- Options: (a, preferred) remove them; (b) keep one with a stated reason.
- Needs decision: no

## Checked and consistent
- Shipment `SE-SH-26-0715`, consignment `SE-CS-26-0716`, ULDs `RKN41207K0` and `AKE20514K0` and their hazardous items agree with 02; the carrier Kelaro Air Cargo is the carrier named in 04.
- Sender (carrier) and receiver (the forwarder that booked) fit an air waybill issued to the forwarder; the consignor is the seller of 01.
- PositionOnBoardStowage belongs in the carrier's document; cargo-aircraft-only with an ATR 72 freighter (`ATF`) is consistent.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator`: suspected filler — refuted because on an air waybill the ad valorem (declared value) charge is a standard field, and `false` states that no value was declared for carriage, which the carrier's charges depend on.
- `/Waybill/cac:IssueLocation/cbc:Name`: suspected that the cargo terminal is a company, not a place — refuted because it names the terminal, a place.

## Outside this review
- Whether an ATR 72 freighter can take the RKN temperature-controlled container and the AKE container (contour and door size of the aircraft) is a capacity question across documents; for the cross-flow consistency review.
