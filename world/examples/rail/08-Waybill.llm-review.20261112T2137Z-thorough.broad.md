# LLM review: 08-Waybill.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

{{HEADER}}

{{EXPECTED}}

## Findings

### rail/08#F1 · High · Road consignment note (CMR) for a cross-border rail carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- XPath: `/Waybill/cbc:Description` = `Carrier haulage: the rail carrier's tractor brings the packed boxes to the hub.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `2`
- Why: WaybillTypeCode is "The type of waybill (Bill of Laden, Airwaybill, CMR, House waybill, etc.)". The document is typed and named as a road consignment note under the CMR convention, and its description covers only the tractor leg to the hub. Yet the carriage it documents is the rail main carriage (mode 2, train FRC 4417) from the Ferrano hub to the Lumeway siding in Marrowdale, Bayvarra, with the consignee there, the containers' unloading in Marrowdale and the rail freight charge. An international rail carriage is documented by a rail consignment note (in reality CIM, my knowledge), not by a CMR; and a CMR for the tractor leg alone would end at the hub, not at the consignee in Bayvarra.
- Condition: The waybill's type, name and description agree with the carriage it documents (rail from the hub to Marrowdale, with the haulage as pre-carriage), or it documents only the road leg and then carries no rail stage and no delivery in Bayvarra.
- Options: (a) preferred: a rail consignment note type (a world code for the Trade Accord's rail convention, or CIM if the world uses it), name and description covering haulage plus rail; (b) two documents: a CMR for the haulage and a rail note for the main carriage.
- Needs decision: yes (which convention governs the carriage is part of the story)

### rail/08#F2 · High · Shipment gross weight leaves out the containers it is defined to include
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport equipment". The two containers weigh 7884 kg each gross (15 768 kg together; 3984 kg goods plus about 3900 kg tare each), so 7968 kg is the goods' weight without the equipment. The transit declaration has the same value (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`).
- Condition: The shipment gross weight includes the transport equipment (15 768 kg), or is absent.
- Options: (a) preferred: 15 768 kg at shipment level; (b) drop it and give the goods' 7968 kg at consignment level (as in 02/03).
- Needs decision: no

### rail/08#F3 · High · Actual waypoint after the waybill was issued
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`
- XPath: `/Waybill/cbc:IssueTime` = `13:10:00`
- Why: ActualWaypointTransportEvent is "The location of an actual waypoint during a transportation service"; the waybill, issued on 14 April at 13:10, records the train actually passing its waypoint at 13:20 the same day, ten minutes in the future.
- Condition: Every actual event lies at or before the issue time.
- Options: (a) preferred: drop the actual waypoint (a consignment note is not a progress report) and keep the planned one; (b) issue the waybill later, if the world's waybill is updated en route.
- Needs decision: no

### rail/08#F4 · High · Distribution contradicts the three originals and the consignee
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: The note says there are three originals, for consignor, consignee and carrier. The distribution list gives "the consignee's original" to Ferrano Intermodal Hub, which is the terminal at the start of the rail stage, not the consignee (Lumeway Distribution, Marrowdale); the consignor Valdara receives only an electronic copy, not an original; and the carrier's original is not listed.
- Condition: The distribution names the consignor, the consignee (or the party carrying the consignee's original with the goods) and the carrier as in the note, each with the kind of copy the note says.
- Options: (a) preferred: three distributions (original to Valdara, original with the goods for Lumeway, original kept by Ferrano Rail Cargo); (b) change the note if the world's convention differs.
- Needs decision: no

### rail/08#F5 · High · Customs declaration referenced before it exists, and with the wrong issuer
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: CustomsDeclaration/IssuerParty is "The Party who issues this Customs Declaration". VI-TD-26-0331 is Valdara's transit declaration: Valdara makes it as TransitExporterParty and signs it (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`), and its number has Valdara's prefix; customs processes it but does not issue it. The declaration is also issued at 17:29 on 14 April (`06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cbc:IssueTime` = `17:29:00`), four hours after this waybill (13:10) already quotes its number.
- Condition: The issuer of the referenced declaration is the party that issued it (Valdara), and the waybill does not refer to a declaration issued after the waybill.
- Options: (a) preferred: IssuerParty Valdara; resolve the order of the two documents (declaration before the waybill, or waybill updated later); (b) if the reference is to a customs-assigned number (MRN), use that number and keep customs as issuer.
- Needs decision: no

### rail/08#F6 · Medium · Container "being stored" at the hub while loaded on the train
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:StorageLocation/cbc:Name` = `Ferrano Intermodal Hub, stack C`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:DispositionCode` = `LOADED`
- Why: StorageLocation is "The location where this piece of transport equipment is being stored". At 13:10 the container is loaded on the train (DispositionCode LOADED, loading 05:40, departure 06:52) and travelling to Marrowdale; it is not being stored in stack C. The storage between the handling at 18:30 on 13 April and the loading is over.
- Condition: StorageLocation is absent, or states where the equipment is stored at the time of the document.
- Options: (a) preferred: drop it; (b) if the overnight storage matters, describe it as a past event (e.g. a WarehousingTransportEvent with that location).
- Needs decision: no

### rail/08#F7 · Medium · Consignment ID used as shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "An identifier ... of the Shipping Order or Forwarding Instruction associated with this shipment". VI-CS-26-0327 is the consignment's identifier (`/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0327`); the shipping order in this flow is the transport request VI-TR-26-0326 (02), and the waybill refers to the plan as well.
- Condition: ShippingOrderID holds the identifier of a shipping order or forwarding instruction, or is absent.
- Options: (a) preferred: VI-TR-26-0326 (Valdara's transport request); (b) drop it.
- Needs decision: no

### rail/08#F8 · Medium · EmissionCalculationLocation names an office, not a geographic context
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cac:EmissionCalculationLocation/cbc:Name` = `Ferrano Rail Cargo, energy office`
- Why: EmissionCalculationLocation is "The geographical context in which this environmental emission was calculated or for which the emission factor applies, such as the country of a national database or regulatory regime". The value is the carrier's department that did the calculation, not a geography.
- Condition: The location names the geographic context of the emission factor (e.g. Urvania and Bayvarra, or the Trade Accord grid), or is absent.
- Options: (a) preferred: the country or grid whose electricity factor was used; (b) drop it.
- Needs decision: no

### rail/08#F9 · Medium · Province given in Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity). 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/08#F10 · Medium · Language code in LocaleCode
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` is a language, not a locale.
- Condition: LocaleCode absent or a locale such as `en-XB`.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/08#F11 · Medium · A gate in AdditionalStreetName
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is not a street; the delivery is to the rail siding (GLN 9520610900015), not through a road gate.
- Condition: AdditionalStreetName holds a street name or is absent.
- Options: (a) preferred: drop it.
- Needs decision: no

### rail/08#F12 · Low · Waypoints without a place
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:PlannedWaypointTransportEvent/cbc:OccurrenceTime` = `13:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- Why: A waypoint is a place passed on the way; without a Location these events say only that the train was somewhere at 13:00/13:20. The request names the waypoint ("Rail border station Urvania–Bayvarra", 02).
- Condition: Each waypoint event carries its Location.
- Options: (a) preferred: Location = the rail border station, as in 02.
- Needs decision: no

### rail/08#F13 · Low · Second container described with much less than the first
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:SizeTypeCode` = `45G1`
- Why: The freight charge "Rail freight per container" (54 600 XUF), the pickup, loading, delivery, rail car, owner, provider and locations are given for FRXU1044175 only. FRXU1044180 travels the same way and is charged the same (the freight invoice bills 2 × 54 600, `10-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `109200`), but the waybill shows no charge and no rail car for it, so the consignment note states half of the freight.
- Condition: Both containers carry the data that differs between them or that the waybill needs for each (at least the freight charge and the rail car), or the shared data is stated once for the consignment.
- Options: (a) preferred: the freight charge for both containers (or once at consignment level, 109 200 XUF); the rail car of the second container; (b) state the shared events once at consignment level.
- Needs decision: no

### rail/08#F14 · Low · Self-reference, filler and company names as places
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:ShipmentDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:PassengerQuantity` = `0`
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- Why: The container's shipping document reference points to this waybill itself, which adds nothing. Zero passengers on a freight train is a filler (IND5/IND6). The issue location is named after the warehouse company, while the same document names the place "Castrano Logistics warehouse, Ferrano".
- Condition: No self-reference; no PassengerQuantity; the issue location named as a place.
- Options: (a) preferred: drop the self-reference and PassengerQuantity; name the place as in PickupLocation.
- Needs decision: no

### rail/08#F15 · Low · Contacts do not fit the roles
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- Why: The consignor receives its consignment note at its sales order desk, and the consignee is reached at its sales customer service, while a waybill needs the consignor's shipping contact and the consignee's goods receiving.
- Condition: Role-specific contacts (shipping, goods receiving), or none.
- Options: (a) preferred: role-specific contacts; (b) drop Contact where it does not fit.
- Needs decision: no

## Checked and consistent
- References: `FRC-TEP-26-0328` resolves to 03; consignment, shipment, containers, seals, weights and the contract FRC-CON-2026-005 agree with 03 and 06; ContractedCarrierAssignedID `FRC-CON-2026-005/88` agrees with the plan's "Call-off 88 of the year". The waybill is referenced by the freight invoice (`10-Invoice.xml:/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`).
- Times of the rail stage: planned 06:45/10:30, estimated 06:50/10:40, actual departure 06:52 equal 03 and 05; equipment events in order: positioning 12 April 08:00, pickup 13 April 15:00, handling 18:30, loading 14 April 05:40, despatch 06:50, delivery planned 15 April 11:00 (= 03, 07), latest delivery 16 April (= 03).
- Check digits: ISO 6346 FRXU1044175 and FRXU1044180, GLN 9520610900015 and 9520610900008, ISIN pass (check_ids.py). The rail car number 31 46 4521 042-3 passes the UIC (Luhn) self-check digit (my calculation), under the world's rail vehicle register.
- Equipment: 45G1 = 40-foot high cube, length 12 192 mm, 76.3 m³; owner and provider Ferrano Rail Cargo agree with ProviderTypeCode/OwnerTypeCode CARRIER and with the return to the hub within five days (= the five days' free time in the demurrage instructions).
- Energy and emission: 2 × 610 kWh = 1220 kWh for 410 kg CO2e gives 0.34 kg CO2e/kWh, a plausible grid factor (my knowledge); hub to Marrowdale agrees with the rail stage.
- Parties described as in the other rail examples.

## Considered and refuted
- `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`: suspected copied master data — refuted because Castrano loads the containers (LoadingProofParty) and the boxes are picked up at its warehouse, so the waybill uses it.
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:OperatingParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`: suspected the wrong operator for a carrier-owned container — refuted because the hub operates the container on its terminal (stacking, loading), which fits "the Party who operates this piece of Transport Equipment" for the terminal part.
- `/Waybill/cbc:CarrierAssignedID` = `FRC-CMR-26-0325`: suspected a duplicate of the waybill number — refuted because a carrier may keep its own reference for the shipment next to the document number (it follows the CMR typing of F1, though).

## Outside this review
- Timeline: the waybill is issued at Castrano's warehouse on 14 April at 13:10, a day after the boxes were collected there (13 April 15:00) and six hours after the train left the hub (06:52); a consignment note is normally made out when the carrier takes over the goods.
- Capacity: whether 96 benches (1.80 × 0.62 × 0.78 m each, given in 06) fit one 76.3 m³ container is a question across documents (raised as a finding in the review of 06).
