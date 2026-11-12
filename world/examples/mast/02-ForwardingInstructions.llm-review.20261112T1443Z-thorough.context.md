# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/02-ForwardingInstructions.xml`, Git blob `2697645dcfc391cd36edbe8e8ed4c28f35be7a85` (committed)
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

### mast/02#F1 · High · Placard notation for an excepted package that needs no placard
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is "Text of the placard notation corresponding to the hazard class of this hazardous item. Can also be the hazard identification number of the orange placard (upper part) required on the means of transport." UN 2911 (radioactive material, excepted package – instruments or articles) is carried as an excepted package: it needs no class 7 label and no placard (IAEA SSR-6 and ADR 1.7.1.5/5.1.5.4; own knowledge), only the UN number marking. The same HazardousItem says so in its own text, so the placard notation contradicts the explanation next to it. The same value is in 01, 04 and 05 of this flow.
- Condition: No placard notation is given for the excepted package of UN 2911, and the HazardousItem agrees with its own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; (b) if a placard were meant, the item would not be an excepted package, which changes UN number and story.
- Needs decision: no

### mast/02#F2 · Medium · Forwarding instructions that do not say where to, when or how
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SE-SH-26-0715`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:HazardousGoodsTransit/cbc:TransportAuthorizationCode` = `CAO`
- Why: ForwardingInstructions is "A document issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein". The document describes the goods in detail but gives no instruction: no shipment stage, no place or time of collection, no destination location or airport, no requested delivery date, no transport mode or service (air carriage is only implied by the cargo-aircraft-only code), no delivery terms. The consignee's address is the only hint where the goods go. The document's purpose depends on these instructions (section 4.3).
- Condition: The forwarding instructions say at least where and when the goods are to be collected, where they are to be delivered, and the transport mode or service requested.
- Options: (a, preferred) add a Delivery (or MainCarriageShipmentStage) with the collection place/time and the destination, and the requested mode; (b) at minimum the requested delivery and the destination location.
- Needs decision: no

### mast/02#F3 · Medium · Numbered orange placard for packaged goods carried by air
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: UpperOrangeHazardPlacardID and LowerOrangeHazardPlacardID are "The number for the upper/lower part of the orange hazard placard required on the means of transport". Orange plates are an ADR/RID requirement for road vehicles and rail wagons; for goods in packages ADR 5.3.2.1.1 requires plain orange plates without numbers, and numbered plates only for tanks and bulk (own knowledge). These items travel packed in a ULD (`RKN41207K0`) on a cargo aircraft (`CAO`), where no orange plate exists. No means of transport in this flow requires the numbers 90/3480, so the condition in the definition is not met. The same values are in 03.
- Condition: Orange placard numbers are given only for goods whose means of transport requires numbered orange plates (tank or bulk carriage by road or rail).
- Options: (a, preferred) remove both elements; (b) if a road pre-carriage to the airport is meant, still no numbers apply to packages — mention the plain plates in text if needed.
- Needs decision: no

### mast/02#F4 · Medium · Temperature code given next to a measured value
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[1]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[3]/cac:Temperature/cbc:MeasureCode` = `TARGET`
- Why: MeasureCode is "A code describing the temperature, when not expressed as a measure". Each Temperature also has a Measure of 20 °C, so the condition of the definition is not met; the code is used as a qualifier ("this measure is a target") rather than as a description of a temperature that has no measure (such as "ambient" or "frozen").
- Condition: MeasureCode is present only in a Temperature that has no Measure.
- Options: (a, preferred) remove MeasureCode and say "target transport temperature" through AttributeID or the Description; (b) use MeasureCode alone (without Measure) if a coded temperature is meant.
- Needs decision: no

### mast/02#F5 · Medium · Language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". The value repeats the language code from Language/ID (`en`, list ISO 639); it does not name a locale (a language in a country or region, e.g. English as used in Bayvarra). A language code in LocaleCode is the case section 6 names as Medium. The same value occurs 362 times in 213 examples (`grep -rh --include='*.xml' -o '<cbc:LocaleCode[^<]*' world/examples | sort | uniq -c`; every occurrence is `en` with list ISO 639).
- Condition: LocaleCode, where present, holds a locale identifier (language plus territory, e.g. `en-XB`) from a list of locales, or it is absent.
- Options: (a, preferred) remove LocaleCode, since Language/ID already says English and nothing in the document depends on a locale; (b) use a locale code such as `en-XB` with a locale list as listID, consistent with the `en-XB`/`en-XL` languageIDs used elsewhere.
- Needs decision: no

### mast/02#F6 · Medium · Fissile-isotope element used for a non-fissile americium source
- XPath: `/ForwardingInstructions/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: ApplicableRadioactiveIsotope is defined as "The maximum activity of the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage". Americium-241 in smoke detectors is not fissile material (the fissile nuclides in the transport regulations are U-233, U-235, Pu-239 and Pu-241; IAEA SSR-6, own knowledge), so the definition's condition is not met. In addition 37 kBq is the typical activity of one ionisation detector, while the item is a set of ten, and the definition speaks of the radioactive contents.
- Condition: ApplicableRadioactiveIsotope is used only for fissile contents; the activity of the americium sources, if stated, is in an element whose definition covers it and refers to the contents it states (one detector or the set).
- Options: (a, preferred) remove ApplicableRadioactiveIsotope and state the activity in the RadioactiveMaterial description (e.g. "10 × 37 kBq Am-241"); (b) record that UBL lacks a non-fissile activity element as a finding for the UBL TC.
- Needs decision: no

### mast/02#F7 · Low · Stowage position on board stated by the consignor
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-2`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: PositionOnBoardStowage is "A stowage indicating where to find this hazardous item" on board. The consignor issues these instructions a day before the waybill and before any flight is booked; the position on the aircraft's main deck is fixed by the carrier's load plan, not by the consignor. The positions are the same as in the carrier's waybill (03), where they belong. If the consignor means a requirement ("accessible", as cargo-aircraft-only items require), that is an instruction, not a position.
- Condition: The forwarding instructions state stowage requirements only as requirements (e.g. in text or handling instructions), not as positions on board, which only the carrier's documents state.
- Options: (a, preferred) remove PositionOnBoardStowage here and, if needed, say "to be stowed accessible" in HandlingInstructions or the TransitDescription; (b) keep the positions only in 03.
- Needs decision: no

### mast/02#F8 · Low · Hazardous-item notification party is the consignor itself
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: HazardousItemNotificationParty is "The Party who is notified of a Hazardous Item in this Consignment". It names Saltmere Engineering, the consignor, which declared the dangerous goods itself and needs no notification of them. A party that has to be notified would be someone else (consignee, airport, authority), and the consignor as emergency contact is already the ContactParty of the hazardous item.
- Condition: HazardousItemNotificationParty, where present, names a party other than the one that declares the goods, which has to be notified of them.
- Options: (a, preferred) remove it, since the consignor is already the emergency contact; (b) name the party that has to be notified in the story (e.g. the consignee or the destination airport cargo terminal).
- Needs decision: no

### mast/02#F9 · Low · Freight forwarder role defined as a consolidator, but nothing is consolidated
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: The FreightForwarderParty is defined in UBL as "The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart who mirrors the consolidator's activity". In this flow Bayforth does not consolidate: the air waybill is not consolidated (`03-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`) and there is one consignment of one consignor. The party is the forwarder in the ordinary sense (it arranges the carriage), which the UBL definition does not cover. Whether to keep the role and record the narrow definition, or treat it as a misuse, could not be settled here.
- Condition: Either FreightForwarderParty is used for a party that consolidates, or the use for a non-consolidating forwarder is recorded as a deliberate reading (finding on the UBL definition).
- Options: (a, preferred) keep the role (ForwardingInstructions are by definition "issued to a forwarder") and record the narrow definition for the UBL TC write-up; (b) make the shipment a consolidation, which changes the story.
- Needs decision: yes

### mast/02#F10 · Low · Reefer settings and food approvals that do not serve this shipment
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumidityPercent` = `50`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AnimalFoodApprovedIndicator` = `false`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumanFoodApprovedIndicator` = `false`
- Why: The temperature range 5–35 °C has a reason for lithium-ion batteries, but air-flow and humidity settings (relevant to perishables) and the statement that the unit is not approved for animal or human food have none: no food is carried, and "not approved" says only what absence would say (no-filler rule).
- Condition: Every reefer setting and approval indicator of the unit serves the goods carried (or the story says why).
- Options: (a, preferred) remove the two food indicators and the air-flow/humidity settings; (b) keep one with a stated reason (e.g. humidity limit for the batteries).
- Needs decision: no

## Checked and consistent
- Shipment `SE-SH-26-0715` and consignment `SE-CS-26-0716` are the same as in 03 and 04; goods items, UN numbers and quantities agree with the order lines of 01 (6 batteries, 1 set of detectors, 20 L stripper).
- The consignor is the seller and the consignee the buyer of 01; under CPT the seller instructs the forwarder, which fits.
- DG transit data: packing instruction 965 section IA and cargo-aircraft-only for UN 3480 batteries shipped alone fit the IATA rules (own knowledge); the state of charge below 30 % in the text agrees.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure`: suspected that an emergency temperature applies only to self-reactive substances and organic peroxides — refuted because the definition speaks of "temperature-controlled goods" generally, and these batteries are carried in a temperature-controlled unit, with a plausible threshold for thermal runaway risk.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode`: suspected that a refrigerated container code does not fit a ULD — refuted because `RKN` is a temperature-controlled ULD and "Refrigerated container" describes it; the second ULD uses the generic `UL`.
