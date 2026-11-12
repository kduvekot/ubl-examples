# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/04-Waybill.xml`, Git blob `df051bb647e8d343d035d6fb70ee57e379ee8b0f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/04#F1 · High · ShippingOrderID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0322`
- Why: Waybill/ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own ID. The forwarding instructions of this shipment are `LD-FI-26-0322` and give the shipping order as `LD-SH-26-0323`; neither is `LD-CS-26-0324`. An identifier of one kind (a consignment) is used as another (a shipping order), and it contradicts the document that defines the shipping order. The same value is in `05-TransportationStatus.xml` and `09-TransportationStatus.xml`. Merge check: refutation attempted (a consignor numbering its shipping order like its consignment); refuted, because 03 itself names a different shipping order number.
- Condition: ShippingOrderID holds the identifier of the forwarding instructions or of the shipping order they name, the same value that 03, 05 and 09 use.
- Options: (a) preferred: `LD-FI-26-0322`, the forwarding instructions that exist in the flow (the definition names them explicitly), with 03's own ShippingOrderID dropped (air/03#F10); (b) `LD-SH-26-0323` everywhere, as 03 states it.
- Needs decision: no
- From: broad, logistics, context

### air/04#F2 · High · "Not consolidated", yet the consignment has a consolidation and a house waybill
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChildConsignmentQuantity` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsolidatedShipment/cbc:ID` = `BF-CONS-26-0207`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: ConsolidatedIndicator is "An indicator of whether this waybill is consolidated from other waybills (true) or not (false)". The consignment says the opposite: it belongs to a consolidated shipment (ConsolidatedShipment, "a shipment created by an act of consolidation") and has a child consignment (ChildConsignment, "one of the child consignments of which a consolidated consignment is composed") numbered as the forwarder's house air waybill. A master air waybill over a forwarder's consolidation names the forwarder as consignor and its agent as consignee (own knowledge of air cargo practice); this one names the shipper Lumeway and the buyer Velumi, as a direct waybill does, and calls itself `AWB`. The consignment `LD-CS-26-0324` is the consignor's own (03), so it cannot also be the parent of a house consignment of the same goods. Neither `BF-CONS-26-0207` nor `BF-HAWB-26-0918` occurs in any other example (`grep -rn --include='*.xml'`), and the forwarder's invoice 10 refers to this carrier's waybill, not to a house waybill. Merge check: the definitions of indicator, ConsolidatedShipment and ChildConsignment re-read; no reading lets a waybill with a child consignment be "not consolidated".
- Condition: indicator and structure agree: either a direct air waybill (indicator false, no ConsolidatedShipment, ChildConsignment or ChildConsignmentQuantity), or a master waybill (indicator true, forwarder as consignor, the house consignment as child, and the house waybill the document the shipper and the invoice refer to).
- Options: (a) preferred: direct air waybill, dropping the consolidation elements: one small urgent consignment on a named priority flight, and every other document of the flow treats it that way; (b) a forwarder consolidation story, which changes several documents.
- Needs decision: yes (whether the forwarder consolidates)
- From: broad, logistics, context

### air/04#F3 · High · AdValoremIndicator true here, false in the forwarding instructions for the same shipment
- XPath: `/Waybill/cbc:AdValoremIndicator` = `true`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- XPath: `10-Invoice.xml:/Invoice/cbc:LineCountNumeric` = `1`
- Why: The indicator is defined by "ad valorem duties, which are levied on commodities at certain rates per centum on their value". Goods, shipment `LD-SH-26-0323` and declared value (512.00 XBL) are the same in both documents, so whether duties are ad valorem cannot change between them. Read in transport practice as the carrier's valuation charge on the declared value (the context part's reading, by which `true` fits the declared value here), it is used against its definition, and `true` would then call for a valuation charge that the waybill does not state and the forwarder's invoice does not bill (one line, air freight only). Merge check: as in air/03#F3; under both readings the two documents disagree about one consignment.
- Condition: waybill and forwarding instructions carry the same AdValoremIndicator, chosen according to the UBL definition (duties), or neither carries it.
- Options: (a) preferred: leave it out of both, as neither document deals with duties; (b) the same value in both, set by whether Lisavu's duty on HS 7325.99 is ad valorem.
- Needs decision: no
- From: broad, money; context found the value consistent with the declared value (see Considered and refuted)

### air/04#F4 · High · The exchange rate is dated a week after the waybill was issued
- XPath: `/Waybill/cac:ExchangeRate/cbc:Date` = `2026-05-20`
- XPath: `/Waybill/cbc:IssueDate` = `2026-05-13`
- XPath: `/Waybill/cbc:VersionID` = `1`
- Why: ExchangeRate/Date is "The date on which the exchange rate was established". A waybill issued on 2026-05-13 (version 1, the only one) cannot quote a rate established on 2026-05-20; the date is also after the flight (14 May) and after the forwarder's invoice (`10-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-05-15`). Merge check: a forward rate agreed for a later date would still be established before the document; the definition names the date of establishment, not of application.
- Condition: the exchange rate's Date is on or before the issue date, or the exchange rate is absent (F12).
- Options: (a) preferred: remove the exchange rate (F12); (b) date it on or before 2026-05-13.
- Needs decision: no
- From: broad, money, logistics, context

### air/04#F5 · Medium · The waybill does not say what is carried or in how many pieces
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- XPath: `/Waybill/cbc:Description` = `The flight to the island.`
- Why: A Waybill is "a transport document describing a shipment"; an air waybill states the number of pieces, the weight and the nature and quantity of the goods (Montreal Convention art. 5 and the IATA air waybill, own knowledge). This one has weight, volume and chargeable weight, but no GoodsItem, no description of the goods, no number of packages or handling units and not the SSCC `095206103190000015` of the skid in 03. The carrier could not check what it accepted. Merge check: no GoodsItem, TransportHandlingUnit, Package or Total…Quantity in the waybill.
- Condition: the consignment states the nature of the goods (bench side frame castings) and the number of pieces, consistent with `03-ForwardingInstructions.xml`, in the structured elements (GoodsItem with description and quantity, TotalTransportHandlingUnitQuantity or TotalPackagesQuantity, TransportHandlingUnit with the SSCC).
- Options: (a) preferred: a GoodsItem and the handling unit with its SSCC, taken from 03 (as resolved by air/03#F2); (b) at least the totals and a goods description.
- Needs decision: no
- From: logistics, context

### air/04#F6 · Medium · A warehouse as substitute carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cbc:IndustryClassificationCode` = `5210`
- XPath: `01-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: SubstituteCarrierParty is "The Party who subtitutes the carrier of this Consignment", i.e. one that performs the carriage in the carrier's place. Nalevi Warehousing is a warehouse (ISIC 5210, warehousing and storage), the delivery party of the order change and the delivery customer of the despatch advices; its contact is `Goods inwards`. Nothing in the flow has it carry the goods, let alone take Kelaro's place on the only stage of this waybill (main carriage by air, flight KXL207), and the waybill has no on-carriage stage it could perform. The party seems to stand for the receiving warehouse at destination, a role the waybill names nowhere else.
- Condition: SubstituteCarrierParty is absent, or holds a party that actually takes over carriage from Kelaro Air Cargo; Nalevi, if the waybill needs it, is in a role that fits a receiving warehouse (the consignment's Delivery/DeliveryParty or NotifyParty).
- Options: (a) preferred: move Nalevi to the consignment's delivery or notify party, matching the order; (b) drop it, if the consignee is enough; (c) if Nalevi trucks the goods from Selanu airport, an on-carriage stage with Nalevi as its carrier (then it is an on-carrier, not a substitute for the airline).
- Needs decision: yes (which role Nalevi plays, and who brings the goods from the airport)
- From: broad, parties, logistics, context

### air/04#F7 · Medium · The consignor-assigned ID of the child consignment is the forwarding instructions' document number
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ConsignorAssignedID` = `LD-FI-26-0322`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: ConsignorAssignedID is "An identifier for this consignment, assigned by the consignor". Lumeway numbered its consignment `LD-CS-26-0324` (03); `LD-FI-26-0322` is the ID of the forwarding instructions document. A document number is used as a consignment identifier.
- Condition: no consignment identifier holds a document number; where a consignor-assigned consignment ID is given, it is `LD-CS-26-0324`, or the child consignment is removed (F2 option a).
- Options: resolve together with F2 (preferred); if the child stays, `LD-CS-26-0324`.
- Needs decision: no
- From: broad, logistics, context

### air/04#F8 · Medium · LocaleCode holds a language code
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en` (Bayforth Forwarding)
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language, not a locale, and repeats Language/ID. Counted over `*.xml`: 362 such elements in 213 files.
- Condition: every LocaleCode holds a locale from a locale list, or is absent.
- Options: (a) preferred: drop it; (b) a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### air/04#F9 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street, and the air waybill involves no vehicle at the consignor's premises. Counted over `*.xml`: 79 occurrences in 76 files.
- Condition: no gate in a street-name element of the postal address.
- Options: (a) preferred: drop it; (b) a pickup or despatch location in documents that arrange a pickup.
- Needs decision: no
- From: parties, context

### air/04#F10 · Low · The waybill's flight and the missed-flight story of the flow are not tied together
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL207`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: The logistics part read the waybill (version 1, issued 13 May 10:43) as booking flight KXL207 on 14 May 07:00, and the cancellation 07 (issued 14 May 17:53) as saying the cargo missed that flight and goes on the next day's, i.e. 15 May, while 09 reports arrival at Selanu on 14 May; it rated this High. The merge tried to refute it and found a reading under which the waybill is consistent: the flight missed was an earlier one on 13 May (07 cites `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`, an offload on 13 May, and 05 reports cargo "built up for the flight" on 13 May), and KXL207 on 14 May is the "next day's flight", on which it arrived (09). Under that reading the contradictions lie in 07 (issued after the arrival, announcing a despatch advice that 08 already issued at 10:48), which are findings of 07's review. What remains for this example is that nothing in the waybill shows which flight was booked first and which is the replacement, so the reader cannot tell from it whether the cargo flew as booked. The parallel merge of 06–10 prefers the same reading.
- Condition: the waybill's flight, the missed flight of 07 and the arrival in 09 tell one story that a reader can follow from the documents (e.g. the waybill, or a version of it, shows the flight on which the cargo actually flew, and 07 names the flight missed).
- Options: (a) preferred: the missed flight is the 13 May flight (offload `KXL-OFFLOAD-26-0513`), this waybill names the replacement KXL207 of 14 May, and 07's wording and timing are aligned (the fewest changes); (b) the cargo missed KXL207 on 14 May: a new waybill version with the 15 May flight, and 09 reports arrival on the 15th.
- Needs decision: yes (the flow's story)
- From: logistics (High; lowered in the merge)

### air/04#F11 · Low · The carrier's flight schedule is given as "requested" events
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceTime` = `10:00:00`
- Why: RequestedDepartureTransportEvent is "The departure requested by the party requesting a transportation service". The waybill is the carrier's document for scheduled flight KXL207; its times are the carrier's plan, for which ShipmentStage has PlannedDepartureTransportEvent and PlannedArrivalTransportEvent. The forwarding instructions requested no flight times (only despatch on 13 May and delivery on 14 May).
- Condition: the booked flight's times are in the planned (or estimated) events; requested events only where a requesting party's wish is stated.
- Options: (a) preferred: PlannedDeparture/PlannedArrival with the same times; (b) keep a requested arrival only if it reflects 03's requested delivery.
- Needs decision: no
- From: broad, logistics, context

### air/04#F12 · Low · An exchange rate with nothing in the waybill to convert
- XPath: `/Waybill/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Waybill/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The waybill states no charges (no freight, no charges collect at destination); its only amounts are the declared values in XBL. Converting charges collect into the destination currency is what a waybill carries a rate for; here nothing is converted. Freight is prepaid by the consignor under CPT and billed in XBL (`10-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`). The rate itself (0.4, Multiply) agrees with the world's other XBL→XLC rates.
- Condition: the exchange rate is used by something in the waybill (charges collect in XLC) or is absent.
- Options: (a) preferred: remove it; (b) keep it, dated (F4), with the charges it converts.
- Needs decision: no
- From: broad, money, context

### air/04#F13 · Low · Chargeable weight rests on a volume the forwarding instructions' package does not support
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[1]/cbc:Measure` = `800`
- Why: ChargeableWeightMeasure is "the weight upon which a charge is to be based". 96 kg is the volumetric weight of 0.576 m³ at the IATA ratio of 6000 cm³/kg (own knowledge): 576 000 / 6000 = 96. 0.576 m³ is 8 × 0.072 m³, eight boxes of 800 × 300 × 300 mm, but the forwarding instructions describe one such box holding all 8 items (0.072 m³, volumetric weight 12 kg, below the gross 81.6 kg; on that description the chargeable weight would be the gross weight, about 82 kg). The waybill's own figures agree with each other and with 03's net volume (0.576 ≥ 0.42); what contradicts them is 03's package, which is itself wrong (air/03#F2). Which description is right decides what the freight costs.
- Condition: the chargeable weight follows from the packages as described in the flow, and gross volume and package dimensions agree.
- Options: (a) preferred: describe eight boxes (or a crate of 0.576 m³) in 03 and keep 96 kg here, since 0.42 m³ of frames needs more than one such box; (b) if there is one box, chargeable weight 82 kg and gross volume 0.072 m³ (then the net volume in 03 is wrong too).
- Needs decision: no
- From: money (needs decision yes there)

### air/04#F14 · Low · Special security required for cast-iron frames, with no reason
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:SpecialSecurityIndicator` = `true`
- Why: SpecialSecurityIndicator is "An indication that the transported goods in this consignment require special security (true) or not (false)". Eight bench side frame castings worth 512.00 XBL are not valuable, dangerous or sensitive goods, and nothing in the waybill (SpecialServiceInstructions speak of priority handling only) explains the indicator. Against (logistics, own knowledge): all air cargo must be secured (screened or from a known consignor) before loading. That is the ordinary security every consignment gets; the definition says "special", so the merge keeps the finding.
- Condition: the indicator is false or absent, or the document states why the goods need special security.
- Options: (a) preferred: `false` or drop it; (b) a reason in SpecialServiceInstructions.
- Needs decision: no
- From: broad, context; logistics refuted it

### air/04#F15 · Low · Issue location named after the terminal company, without the identifier used for the place
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMA`
- XPath: `05-TransportationStatus.xml:/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: IssueLocation is "The location where this waybill was issued"; its Name is "The name of this location". The value is the trading name of a party (the terminal operator, sender of 05), not of a place, and the issuer is Kelaro, not the terminal company, so a reader may take the location for a party. The same place is `XBLMA` "Lumeport airport" in this waybill and "Lumeport airport, cargo terminal" in `05-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal`.
- Condition: the issue location names the place and, where available, carries UN/LOCODE `XBLMA`.
- Options: (a) preferred: name `Lumeport airport, cargo terminal` with ID `XBLMA`; (b) keep the facility name and add the identifier; (c) drop IssueLocation.
- Needs decision: no
- From: broad, parties, logistics, context

### air/04#F16 · Low · "Three originals", but the distribution lists one original and one copy
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note states the Montreal Convention's three originals (art. 7, own knowledge: for the carrier, for the consignee with the goods, for the consignor). The distribution lists the consignee's original going with the goods to the destination handling agent and an electronic copy to the forwarder; the consignor's original is distributed to no one. Against (broad; context listed the distribution as consistent): the distribution need not list the originals kept by the carrier and handed to the consignor at issue. The merge cannot settle whether DocumentDistribution is meant to be complete.
- Condition: the distribution lists the consignor's original (to Lumeway, or to Bayforth as its agent), or the note does not claim three originals, or the story states that the list is not complete.
- Options: (a) preferred: make distribution 2 the consignor's original to the forwarder acting for the consignor; (b) add a third distribution.
- Needs decision: yes (cannot be settled)
- From: logistics; broad refuted it

### air/04#F17 · Low · Two air waybill numbers for one air waybill
- XPath: `/Waybill/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`
- Why: In air freight the air waybill number identifies both the document and the shipment (own knowledge of IATA practice). Here the document ID and the carrier's shipment number differ, both assigned by Kelaro, and the other examples quote only `KXL-WB-26-0325` (05, 09, 10), so the "AWB" number is never used. Against (broad): CarrierAssignedID identifies "a specific shipment" for the carrier, and a separate shipment number is a legitimate reading. The merge cannot settle whether the two numbers have different purposes in the story.
- Condition: the waybill has one AWB number that the other documents quote, or the two identifiers have visibly different purposes.
- Options: (a) preferred: the AWB number as the document ID and no CarrierAssignedID; (b) keep CarrierAssignedID as a booking number distinct from the waybill, and say so.
- Needs decision: yes (cannot be settled)
- From: context; broad refuted it

### air/04#F18 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Kelaro Air Cargo)
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Bayforth Forwarding)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Nalevi Warehousing)
- Why: RegistrationDate is "The registration date of the CompanyID." `1996-01-01` is the date of 25 different companies in three countries and registers (lxml over `*.xml`), in 181 example files, while other companies have individual dates (Lumeway Distribution `1988-10-03`). It reads as a default value ("no fillers").
- Condition: each company's RegistrationDate is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) preferred: a date per company from its history; (b) drop it where unknown; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes (company histories)
- From: parties

### air/04#F19 · Low · Contact names, job titles and departments do not fit each other or the role
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The carrier's `Cargo sales` contact is an operations planner in Operations; the consignee's `Purchasing` and the warehouse's `Goods inwards` contacts are customer service officers in Sales. In each, name and title disagree, and the consignee's contact does not receive goods. Counted over `*.xml`: `Cargo sales` in 8 files, `Purchasing` with this title 52 times.
- Condition: each contact's name, title and department agree with each other and with the party's role in the waybill.
- Options: (a) preferred: titles and departments matching the functional name (Cargo sales: cargo sales agent / Sales, or rename it to a cargo operations desk; Purchasing → an import or goods-receiving contact for the consignee; Goods inwards: warehouse supervisor / Warehouse); (b) drop JobTitle and Department.
- Needs decision: no
- From: broad, parties

### air/04#F20 · Low · Signature aggregate without a signature
- XPath: `/Waybill/cac:Signature/cbc:ID` = `KXL-SIG-KXL-WB-26-0325`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension. For an air waybill the carrier's signature matters (the note speaks of three originals), so a signature that cannot be verified is a gap rather than a filler. The ID also doubles the issuer prefix (`KXL-SIG-KXL-WB-…`), like the IDs the plastics merge flagged. Counted with lxml over `*.xml` in the merge: 137 of 147 Signature aggregates hold only ID and SignatoryParty.
- Condition: either the signature is present and verifiable (method, attachment), or the aggregate is absent; a Signature ID, where kept, is the signatory's own numbering.
- Options: (a) preferred here: add SignatureMethod and DigitalSignatureAttachment for the carrier's signature; (b) drop the aggregate.
- Needs decision: yes (a convention across many examples)
- From: context

## Checked and consistent
- Chargeable weight: 0.576 m³ = 576 000 cm³ / 6000 cm³ per kg (IATA volumetric divisor, own knowledge) = 96 kg, above the gross 81.6 kg, so 96 kg is right within the document; gross volume 0.576 m³ ≥ net volume 0.42 m³ of 03.
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross weight 81.6 kg and declared value 512.00 XBL (`/Waybill/cbc:DeclaredCarriageValueAmount` = `512.00`, `/Waybill/cac:Shipment/cbc:DeclaredForCarriageValueAmount` = `512.00`) agree with each other, with `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00` and with 8 × 64 XBL; consignor, consignee and forwarder agree with 03.
- Locations: `XBLMA` (Lumeport airport, Bayvarra) and `XLSLA` (Selanu airport, Lisavu) are fictional UN/LOCODEs in fictional countries and agree with 05 (XBLMA) and 09.
- TransportModeCode 4, WaybillTypeCode AWB, TransportMeansTypeCode ATF (IATA code for the ATR 72 freighter, own knowledge); RegistrationNationalityID XL fits a Lisavan carrier; the registration `QL-KXA` uses a nationality mark not allocated by ICAO (own knowledge). 81.6 kg is far below an ATR 72F's payload of several tonnes.
- Flight 07:00 to 10:00 on 14 May with both airports at TimezoneOffset −1 is a 3-hour flight after the issue time (13 May 10:43).
- Parties: Kelaro Air Cargo is SenderParty, CarrierParty and signatory (`IC41311`, ISIC 5120); Bayforth (receiver) booked the flight (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyIdentification/cbc:ID` = `20411644`) and receives the electronic copy; Selanu Airport Cargo `IC41174` is the destination terminal of `09-TransportationStatus.xml:/TransportationStatus/cac:SenderParty/cac:PartyIdentification/cbc:ID` = `IC41174`. Lumeway is described as in the other examples; GLN check digit OK; `+999` telephone numbers and `.example` domains cannot be mistaken for real ones.

## Considered and refuted
- `/Waybill/cbc:Name` = `Air waybill under the Montreal Convention`: a real convention in a fictional world, or an unnecessary name — refuted because a real treaty the fictional states can have joined is not a register value, and the name states the regime of carriage that a waybill's conditions of carriage need (from broad, context).
- `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`: suspected contradiction with delivery to Nalevi — refuted because the instruction is about proof of delivery, which a delivery to the consignee's warehouse against the consignee's signature satisfies (from context).
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:TransportMeansTypeCode` = `ATF`: suspected wrong IATA code — refuted: ATF is the IATA aircraft type code for the ATR 72 freighter (own knowledge) (from context).
- `/Waybill/cac:DocumentDistribution[1]/cac:Party`: the consignee's original goes to Selanu Airport Cargo, not to Velumi — refuted because the consignee's original travels with the goods and is handed over by the destination handling agent (from parties).
- `/Waybill/cac:ConsignorParty`: Lumeway as consignor although there is a house waybill — refuted for the party lens because the parties fit a direct waybill; the structure question is F2 (from parties).
- Kelaro Air Cargo as a `SMALL` enterprise operating freight aircraft — refuted: a small island airline is plausible (from parties).
- English renderings tagged `en-XL` here (`/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`) — refuted here, since `en-XL` fits island names; the inconsistency is recorded in the reviews of the examples that use `en-XB` (from parties).
- Missing freight charges and prepaid/collect indication — refuted because the Waybill definition says it "may contain" charges and the payer of the freight is clear from the flow (CPT, forwarder's invoice to the consignor) (from money).
- Declared value 512.00 below the Montreal Convention limit (26 SDR/kg × 81.6 kg, own knowledge) — refuted because XBL has no SDR conversion in the world (from money).
- `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Velumi Trading`: consignee differs from the despatch advices' delivery party Nalevi — refuted because the buyer as consignee with delivery to its warehouse is normal; the role clash is F6 (from logistics).
- `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`: not in the real 3 + 8 digit AWB format — refuted because a real-format number with its mod-7 check digit would risk looking like a real airline's AWB (from logistics); as a second number next to the waybill ID (from broad), the merge does not follow the refutation, see F17.
- `/Waybill/cbc:AdValoremIndicator` = `true` agreeing with a declared value for carriage (context, "Checked and consistent"): the merge does not follow it; see F3.
- `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.` against the distribution (from broad): the merge does not follow the refutation with certainty; see F16.
- `/Waybill/cac:Shipment/cac:Consignment/cbc:SpecialSecurityIndicator` = `true` (from logistics): the merge does not follow the refutation; see F14.

## Changed in the merge
- broad/F1, logistics/F1, context/F2 → F1: combined; preferred option set to `LD-FI-26-0322` (context's), because 03's own ShippingOrderID equals its Shipment ID (air/03#F10) and the definition names forwarding instructions; broad's and logistics' `LD-SH-26-0323` kept as option (b). Aligned with the parallel merge of 06–10 for 09.
- broad/F2, logistics/F2, context/F1 → F2: combined.
- broad/F3, money/F2 → F3: combined; context's contrary reading carried into "Why".
- broad/F4, money/F1, logistics/F3, context/F3 (date part) → F4: combined.
- context/F3 (unused part), broad/F9, money/F3 → F12: combined; context's F3 split between F4 and F12, as the date contradiction and the missing use are different problems with different severities.
- logistics/F5, context/F4 → F5; broad/F6, parties/F3, logistics/F6, context/F5 → F6 (needs decision yes, as three of four parts said); broad/F5, logistics/F7, context/F6 → F7; broad/F7, parties/F1, context/F7 → F8; parties/F2, context/F8 → F9: combined.
- logistics/F4 (High) → F10: Low, needs decision yes. The merge found a reading under which the waybill's flight, 05 and 09 agree (missed flight on 13 May, offload `KXL-OFFLOAD-26-0513`); the remaining contradictions lie in 07 (its timing against 08 and 09). Kept as a finding, because the waybill does not show which flight is the replacement and the story is not settled.
- broad/F8, logistics/F8, context/F9 → F11: combined.
- money/F4 → F13: needs decision no, because the preferred direction follows air/03#F2 (needs decision no there) and keeps this waybill as it is.
- broad/F10, context/F10 → F14: combined, logistics' refutation carried as counter-argument.
- broad/F11, parties/F4, logistics/F10, context/F12 → F15: combined.
- logistics/F9 → F16: needs decision yes, with broad's refutation as counter-argument.
- context/F11 → F17: needs decision yes, with broad's refutation as counter-argument.
- broad/F12, parties/F6 → F19: combined.
- context/F13 → F20: count re-made; the doubled-prefix remark added for consistency with plastics.

## Outside this review
- Timeline: `05-TransportationStatus.xml` reports the cargo accepted at the terminal (issued 10:05) before this waybill was issued (10:43); the reference problem is recorded in 05, the order of events is a timeline question (from broad).
- Whether a 3-hour ATR 72 flight fits the distance between Lumeport and Selanu airports on the map is a cross-flow geography and timeline question (from logistics).
- `07-FulfilmentCancellation.xml`, issued 2026-05-14 17:53 after the arrival reported in 09, announces that "a new despatch advice follows today", while `08-DespatchAdvice.xml` was already issued at 10:48: a problem of 07 and 08 (noted by the merge while checking F10).
