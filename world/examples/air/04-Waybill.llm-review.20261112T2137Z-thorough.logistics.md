# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### air/04#F1 · High · ShippingOrderID holds the consignment ID, not the shipping order or the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0322`
- Why: Waybill/ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping
  Order or Forwarding Instruction associated with this shipment". The forwarding instructions air/03
  are LD-FI-26-0322 and name the shipping order LD-SH-26-0323; the value here is the consignment ID
  LD-CS-26-0324, an identifier of another kind. The same value is in air/05 and air/09.
- Condition: ShippingOrderID is LD-SH-26-0323 or LD-FI-26-0322, as the forwarding instructions state.
- Options: LD-SH-26-0323, the shipping order number the instructions give (preferred); or the
  instructions' own ID.
- Needs decision: no

### air/04#F2 · High · Consolidation data contradicts ConsolidatedIndicator and the direct consignor
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsolidatedShipment/cbc:ID` = `BF-CONS-26-0207`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChildConsignmentQuantity` = `1`
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: ConsolidatedIndicator is "An indicator of whether this waybill is consolidated from other
  waybills". The consignment says the opposite: it belongs to a consolidated shipment
  (BF-CONS-26-0207, "a shipment created by an act of consolidation") and has a child consignment
  with a house air waybill number of the forwarder (BF-HAWB-26-0918, ChildConsignmentQuantity 1).
  A master air waybill over a forwarder's consolidation names the forwarder as consignor and its
  agent as consignee (own knowledge of air cargo practice); this one names the shipper Lumeway and the
  buyer Velumi directly, as a direct (unconsolidated) air waybill does. The consignment
  LD-CS-26-0324 is the consignor's own consignment (air/03), so it cannot also be the parent of a
  house consignment for the same goods. Neither BF-CONS-26-0207 nor BF-HAWB-26-0918 occurs in any
  other example (`grep -rn --include='*.xml'`), and the forwarder's invoice air/10 refers to this
  carrier's waybill, not to a house waybill.
- Condition: either the waybill is a direct air waybill (ConsolidatedIndicator false and no
  ConsolidatedShipment, ChildConsignment or ChildConsignmentQuantity), or it is a master waybill
  (indicator true, forwarder as consignor, the house consignment as child) and the house waybill is
  the document the shipper and the forwarder's invoice refer to.
- Options: (a) preferred: direct air waybill, dropping the consolidation elements, because 8 urgent
  frames booked for a named flight and every other document of the flow treat it that way;
  (b) a consolidation story, which changes several documents.
- Needs decision: yes

### air/04#F3 · High · The exchange rate is dated a week after the waybill was issued
- XPath: `/Waybill/cac:ExchangeRate/cbc:Date` = `2026-05-20`
- XPath: `/Waybill/cbc:IssueDate` = `2026-05-13`
- Why: ExchangeRate/Date is "The date on which the exchange rate was established". A rate cannot be
  established on 2026-05-20 and used in a document issued on 2026-05-13.
- Condition: the exchange rate date is on or before 2026-05-13.
- Options: the issue date or the rate's publication date before it (preferred); or drop the date.
- Needs decision: no

### air/04#F4 · High · The waybill's flight contradicts "the cargo missed its flight" in air/07
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL207`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: The waybill (version 1, the only one) books the consignment on flight KXL207 departing
  2026-05-14 07:00, arriving 10:00. The cancellation air/07 says the cargo missed its flight and goes
  on the next day's flight, which would be 2026-05-15; the status air/09 reports it arrived at Selanu
  on 2026-05-14. Either the cargo flew as booked (then nothing was missed) or it missed this flight
  (then it cannot have arrived on the 14th, and the waybill or a new version names the new flight).
- Condition: the flight in the waybill, the arrival in air/09 and the reason in air/07 tell one story.
- Options: (a) the missed flight is an earlier one (e.g. 2026-05-13 evening, cf. the 19:00 event in
  air/03) and this waybill books the replacement flight; then air/07's wording and dates change;
  (b) the cargo missed KXL207 on the 14th: a new waybill version (or event) with the flight of the
  15th, and air/09 reports arrival on the 15th. Preference (a), it changes the fewest documents.
- Needs decision: yes

### air/04#F5 · Medium · The waybill does not say what is carried or in how many pieces
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: A Waybill is "A transport document describing a shipment"; an air waybill states the number
  of pieces, the weight and the nature and quantity of the goods (Montreal Convention art. 5 and the
  IATA air waybill, own knowledge). This one has weight, volume and chargeable weight, but no
  GoodsItem, no description of the goods, no number of packages or handling units and not the SSCC
  095206103190000015 of the skid given in air/03. The carrier could not check what it accepted.
- Condition: the consignment states the nature of the goods (bench side frame castings, 8 pieces or
  one skid as declared) and the number of pieces, in the structured elements (e.g. GoodsItem with
  description and quantity, TotalTransportHandlingUnitQuantity or TotalPackagesQuantity,
  TransportHandlingUnit with the SSCC).
- Options: add a GoodsItem and the handling unit with its SSCC, taken from air/03 (preferred); or at
  least the totals and a goods description.
- Needs decision: no

### air/04#F6 · Medium · A warehouse company as substitute carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cbc:IndustryClassificationCode` = `5210`
- Why: SubstituteCarrierParty is "The Party who subtitutes the carrier of this Consignment". Nalevi
  Warehousing (ISIC 5210, Warehousing and storage) is the delivery party of the despatch advices
  (air/06, air/08) and the buyer's warehouse; it carries nothing in this flow. Kelaro Air Cargo
  carries airport to airport, and no document makes Nalevi perform any part of the carriage.
- Condition: SubstituteCarrierParty is absent, or a party that actually performs carriage in place
  of the carrier; the warehouse appears, if at all, in a role that fits (e.g. DeliveryParty or
  NotifyParty of the consignment's delivery).
- Options: move Nalevi to the consignment's Delivery/DeliveryParty or NotifyParty (preferred, it is
  where the goods go); or drop it.
- Needs decision: no

### air/04#F7 · Medium · The forwarding instructions' document number used as the consignor's consignment ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ConsignorAssignedID` = `LD-FI-26-0322`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: ConsignorAssignedID is "An identifier for this consignment, assigned by the consignor". The
  consignor numbered its consignment LD-CS-26-0324 (air/03); LD-FI-26-0322 is the ID of the
  forwarding instructions document. A document number is used as a consignment identifier. (If
  air/04#F2 is resolved by dropping the child consignment, this goes with it.)
- Condition: no consignment identifier holds a document number; where a consignor-assigned
  consignment ID is given, it is LD-CS-26-0324.
- Options: resolve together with air/04#F2 (preferred); otherwise LD-CS-26-0324.
- Needs decision: no

### air/04#F8 · Low · The carrier's waybill gives the flight as "requested" events
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceTime` = `10:00:00`
- Why: RequestedDepartureTransportEvent is "The departure requested by the party requesting a
  transportation service". The waybill is issued by the carrier and names a scheduled flight
  (KXL207); its departure and arrival are the carrier's plan, for which ShipmentStage has
  PlannedDepartureTransportEvent and PlannedArrivalTransportEvent. The shipper only requested
  delivery on 2026-05-14 (air/03).
- Condition: the flight's times are in the planned departure and arrival events (or a requested
  event that the shipper actually stated).
- Options: planned events (preferred); keep a requested arrival only if it reflects air/03's request.
- Needs decision: no

### air/04#F9 · Low · "Three originals" but the distribution lists one original and one copy
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: The note states the Montreal Convention's three originals (art. 7, own knowledge: one for the
  carrier, one for the consignee travelling with the goods, one for the consignor). The distribution
  lists the consignee's original going with the goods to the destination handling agent, and an
  electronic copy to the forwarder; the consignor's original is not distributed to anyone.
- Condition: the distribution lists the consignor's original (to Lumeway Distribution or to
  Bayforth Forwarding as its agent), or the note does not claim three originals.
- Options: make distribution 2 the consignor's original to the forwarder acting for the consignor
  (preferred); or add a third distribution.
- Needs decision: no

### air/04#F10 · Low · Issue location given by the terminal company's name, without an identifier
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMA`
- Why: The checklist asks for the place, not the company, and for the identifier where the place is
  identified elsewhere. The issue location is the name of the terminal operator (the sender of
  air/05); the airport is XBLMA in the same waybill.
- Condition: the issue location identifies the place (e.g. ID XBLMA and the name "Lumeport airport,
  cargo terminal").
- Options: add the UN/LOCODE and a place name (preferred).
- Needs decision: no

## Checked and consistent
- Physics: ChargeableWeightMeasure 96 kg = GrossVolumeMeasure 0.576 m³ at the IATA volumetric divisor
  6000 cm³/kg (own knowledge): 576 000 / 6000 = 96 kg, higher than the gross 81.6 kg, so the volume
  weight is correctly the chargeable one. Gross volume 0.576 m³ ≥ net volume 0.42 m³ of air/03.
  81.6 kg on an ATR 72 freighter (payload around 8–9 t, own knowledge) is no capacity issue.
- Gross weight 81.6 kg and declared value 512.00 XBL agree with air/03 (81.6 kg, 512.00 XBL).
- Shipment LD-SH-26-0323 and consignment LD-CS-26-0324 agree with air/03; consignor, consignee
  (Velumi Trading) and forwarder agree with air/03.
- Locations: XBLMA (Lumeport airport, XB) and XLSLA (Selanu airport, XL) agree with the countries
  of consignor and consignee and with air/05 (XBLMA) and air/09 (Selanu).
- TransportModeCode 4 (air), WaybillTypeCode AWB and TransportMeansTypeCode ATF (ATR 72 Freighter,
  in the world's IATA aircraft type list) fit an air waybill; RegistrationNationalityID XL fits a
  Lisavan carrier.
- Flight 07:00 to 10:00 with both airports at TimezoneOffset −1 (party addresses) is a 3-hour flight.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cbc:SpecialSecurityIndicator` = `true`: special security for cast-iron frames — refuted because
  air cargo must be secured (screened or from a known consignor) before loading, which is a real
  reason for the indicator on an air consignment (own knowledge of air cargo security rules).
- `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`: not in the real 3 + 8 digit air waybill
  number format — refuted because it is a fictional carrier's number in its own style, and the real
  format with its mod-7 check digit would risk looking like a real airline's AWB.
- `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Velumi Trading`: consignee differs from the
  despatch advices' delivery party Nalevi Warehousing — refuted because the buyer as consignee with
  delivery to its warehouse is normal; the role clash is only the substitute carrier (air/04#F6).

## Outside this review
- Whether a 3-hour ATR 72 flight fits the distance between Lumeport and Selanu airports on the map is
  a cross-flow geography and timeline question.
