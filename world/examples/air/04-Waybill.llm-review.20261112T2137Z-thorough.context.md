# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/04-Waybill.xml`, Git blob `df051bb647e8d343d035d6fb70ee57e379ee8b0f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### air/04#F1 · High · ConsolidatedIndicator false on a waybill that describes a consolidation
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsolidatedShipment/cbc:ID` = `BF-CONS-26-0207`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChildConsignmentQuantity` = `1`
- Why: ConsolidatedIndicator is "An indicator of whether this waybill is consolidated from other waybills (true) or not (false)". The same waybill describes its consignment as a consolidated shipment (ConsolidatedShipment, "a shipment created by an act of consolidation") with a child consignment whose ID is a house air waybill number of the forwarder. Either the waybill is a master waybill over the forwarder's house waybill (then the indicator is true), or it is a direct waybill (then the consolidation and child consignment do not belong here). The indicator contradicts the structure next to it.
- Condition: the indicator and the presence of ConsolidatedShipment/ChildConsignment agree.
- Options: (preferred) keep it a direct air waybill (one shipper, one consignee, one consignment, no house waybill) and drop the consolidation data, since nothing else in the flow refers to a consolidation or to BF-HAWB-26-0918; or make it a master waybill (indicator true) and let the forwarder's documents (10-Invoice.xml) refer to its house waybill.
- Needs decision: yes (whether the forwarder consolidates)

### air/04#F2 · High · Shipping order ID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: In a Waybill, ShippingOrderID is "An identifier … of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment ID. The forwarding instructions for this shipment are LD-FI-26-0322 and give LD-SH-26-0323 as their shipping order ID; the waybill quotes neither. An identifier of one kind (a consignment) is used as another (a shipping order).
- Condition: ShippingOrderID is the ID of the forwarding instructions or of the shipping order those instructions name, and equals what 03-ForwardingInstructions.xml says.
- Options: (preferred) `LD-FI-26-0322`, the forwarding instructions that exist in the flow; or the shipping order ID of 03 once that is settled.
- Needs decision: no

### air/04#F3 · High · Exchange rate established a week after the waybill was issued
- XPath: `/Waybill/cac:ExchangeRate/cbc:Date` = `2026-05-20`
- XPath: `/Waybill/cbc:IssueDate` = `2026-05-13`
- Why: ExchangeRate/Date is "The date on which the exchange rate was established". A waybill issued on 13 May cannot quote a rate established on 20 May. Besides, the waybill has no amount in Coral and no charges collect at destination: its only amounts are the declared values in XBL, so the exchange rate has no use in this document.
- Condition: the exchange rate, if present, is dated on or before the issue date and serves an amount or charge of the waybill; otherwise it is absent.
- Options: (preferred) drop the ExchangeRate, as the waybill states no charges; or keep it with a date not after 13 May and add the collect charges in XLC that need it.
- Needs decision: no

### air/04#F4 · Medium · The waybill does not say what is carried
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `/Waybill/cbc:Description` = `The flight to the island.`
- Why: A Waybill is "A transport document describing a shipment … It states the instructions … and the conditions of carriage". This one has no GoodsItem, no TransportHandlingUnit or Package, no number of pieces and no description of the nature of the goods; only weights and the volume. An air waybill under the Montreal Convention states the number of pieces and the nature of the goods (own knowledge of the convention and of IATA practice); the forwarding instructions do describe them (1 skid, a box of 8 bags of bench side frame castings).
- Condition: the waybill describes the goods carried: at least number of pieces and nature of the goods, consistent with 03-ForwardingInstructions.xml.
- Options: (preferred) a GoodsItem with description and the handling unit/package count as in the forwarding instructions; or at least TotalPackagesQuantity and a goods description on the consignment.
- Needs decision: no

### air/04#F5 · Medium · A warehousing company as substitute carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cbc:IndustryClassificationCode` = `5210`
- Why: SubstituteCarrierParty is "The Party who subtitutes the carrier of this Consignment". Nalevi Warehousing (ISIC 5210, warehousing and storage) is the delivery party of the buyer (01-OrderChange.xml, 06-DespatchAdvice.xml); it receives the goods, it does not take over the carriage from Kelaro Air Cargo. The waybill has no on-carriage stage that Nalevi could perform. A valid party in the wrong role.
- Condition: SubstituteCarrierParty, if present, is a carrier that performs (part of) the carriage instead of the contracting carrier; the warehouse appears, if at all, as the delivery or notify party.
- Options: (preferred) drop SubstituteCarrierParty and, if useful, name Nalevi as DeliveryParty or NotifyParty of the consignment; or, if Nalevi trucks the goods from Selanu airport, an on-carriage stage with Nalevi as its carrier.
- Needs decision: yes (who brings the goods from the airport to the warehouse)

### air/04#F6 · Medium · The consignor's consignment ID is the forwarding instructions' document number
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ConsignorAssignedID` = `LD-FI-26-0322`
- Why: ConsignorAssignedID is "An identifier for this consignment, assigned by the consignor". The consignor's ID for the consignment is LD-CS-26-0324 (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`); LD-FI-26-0322 is the ID of the forwarding instructions document. A document number is used as a consignment identifier.
- Condition: ConsignorAssignedID is the consignor's consignment ID, or is absent (see F1 about whether the child consignment belongs here at all).
- Options: (preferred) resolve together with F1; if the child consignment stays, `LD-CS-26-0324`.
- Needs decision: no

### air/04#F7 · Medium · LocaleCode holds a language code
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/04#F8 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street, and the air waybill involves no vehicle at the consignor's premises.
- Condition: no gate in a street-name element of the postal address.
- Options: (preferred) drop it.
- Needs decision: no

### air/04#F9 · Low · Requested times in a carrier's waybill for a booked flight
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceTime` = `10:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL207`
- Why: RequestedDepartureTransportEvent is "The departure requested by the party requesting a transportation service". The waybill is issued by the carrier for a scheduled flight KXL207; its times are the carrier's planned departure and arrival, for which ShipmentStage has PlannedDepartureTransportEvent and PlannedArrivalTransportEvent. Nothing in the flow shows that the shipper requested 07:00 and 10:00.
- Condition: the times of the booked flight are in the planned (or estimated) events; requested events only where a requesting party's wish is stated.
- Options: (preferred) PlannedDeparture/PlannedArrival with the same times; or keep the requested events if the forwarding instructions are changed to request them.
- Needs decision: no

### air/04#F10 · Low · Special security required for cast iron frames, with no reason
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:SpecialSecurityIndicator` = `true`
- Why: SpecialSecurityIndicator is "An indication that the transported goods in this consignment require special security". Bench side frame castings worth 512.00 XBL need no special security beyond the screening all air cargo gets; nothing in the waybill (no high-value or sensitive goods, no instruction) explains the indicator.
- Condition: the indicator is false or absent, or the document states why the goods need special security.
- Options: (preferred) `false` or drop it; or a reason in SpecialServiceInstructions.
- Needs decision: no

### air/04#F11 · Low · Two air waybill numbers for one air waybill
- XPath: `/Waybill/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`
- Why: In air freight the air waybill number identifies both the document and the shipment (own knowledge of IATA practice). Here the document ID and the carrier's shipment number differ, both assigned by Kelaro; the other examples quote only KXL-WB-26-0325 (05, 09, 10), so the carrier's AWB number is never used.
- Condition: the waybill has one AWB number that the other documents quote, or the two identifiers have visibly different purposes.
- Options: (preferred) use the AWB number as the document ID and drop CarrierAssignedID, or keep CarrierAssignedID only if it is a booking number distinct from the waybill, and say so.
- Needs decision: no

### air/04#F12 · Low · Issue location named after the company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: IssueLocation is "The location where this waybill was issued"; its name should be the place. The value is the name of the terminal operator (the TerminalOperatorParty of 05-TransportationStatus.xml); the same place is called `Lumeport airport` with UN/LOCODE XBLMA elsewhere in this waybill.
- Condition: the issue location is named and, where possible, identified as a place (as in LoadingPortLocation).
- Options: (preferred) name `Lumeport airport, cargo terminal` with ID XBLMA; or drop IssueLocation.
- Needs decision: no

### air/04#F13 · Low · Signature aggregate without a signature
- XPath: `/Waybill/cac:Signature/cbc:ID` = `KXL-SIG-KXL-WB-26-0325`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension. For an air waybill the carrier's signature matters (the Note speaks of three originals), so a signature that cannot be verified is a gap rather than a filler. 131 of 133 Signature aggregates over `world/examples/*/*.xml` are like this (lxml count).
- Condition: either the signature is present and verifiable (method, attachment) or the aggregate is absent.
- Options: (preferred) add SignatureMethod and DigitalSignatureAttachment for the carrier's signature on this waybill; or drop the aggregate.
- Needs decision: yes (a convention across many examples)

## Checked and consistent
- Shipment LD-SH-26-0323, consignment LD-CS-26-0324, gross weight 81.6 kg and the declared value 512.00 XBL agree with 03-ForwardingInstructions.xml.
- Chargeable weight 96 kg = gross volume 0.576 m³ × 166.67 kg/m³ (IATA volumetric factor 6000 cm³/kg, own knowledge), above the gross weight of 81.6 kg, so the chargeable weight is the volumetric weight.
- AdValoremIndicator true agrees with a declared value for carriage (the disagreement with 03 is a finding of that review).
- Consignee Velumi Trading is the buyer of 01-OrderChange.xml; Kelaro Air Cargo is the carrier named there; the flight on 14 May fits the despatch on 13 May.
- Distribution: the consignee's original with the goods to the destination handler Selanu Airport Cargo (sender of 09-TransportationStatus.xml), an electronic copy to the forwarder; fits the note about three originals.

## Considered and refuted
- `/Waybill/cbc:Name` = `Air waybill under the Montreal Convention`: suspected an unnecessary name — refuted: it names the regime of carriage, which the definition of a waybill (conditions of carriage) needs.
- `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`: suspected contradiction with delivery to Nalevi Warehousing — refuted: the instruction is about proof of delivery; delivery to the consignee's warehouse against a signature for the consignee is consistent.
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:TransportMeansTypeCode` = `ATF`: suspected a wrong IATA code — refuted: ATF is the IATA aircraft type code for the ATR 72 freighter (own knowledge), consistent with a short island route.
