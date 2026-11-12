# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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

### air/04#F1 · High · ShippingOrderID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0322`
- Why: Waybill/ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's own ID. The forwarding instruction of this shipment is `LD-FI-26-0322`, and it gives the shipping order as `LD-SH-26-0323`. Neither is `LD-CS-26-0324`.
- Condition: ShippingOrderID holds the identifier of the shipping order or forwarding instruction, the same one that `03-ForwardingInstructions.xml` gives.
- Options: (a) `LD-SH-26-0323` as in 03 (preferred, if 03 keeps it, see 03#F8); (b) `LD-FI-26-0322`.
- Needs decision: no

### air/04#F2 · High · "Not consolidated", yet the consignment has a consolidation and a house waybill
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChildConsignmentQuantity` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsolidatedShipment/cbc:ID` = `BF-CONS-26-0207`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- Why: ConsolidatedIndicator is "An indicator of whether this waybill is consolidated from other waybills". The consignment names a consolidated shipment of the forwarder and a child consignment numbered as a house air waybill. That is a consolidation, a master waybill over house waybills. At the same time the waybill says it is not consolidated, names Lumeway as consignor and calls itself an "AWB", as a direct waybill would. Neither the consolidation `BF-CONS-26-0207` nor the house waybill `BF-HAWB-26-0918` occurs in any other example.
- Condition: indicator and structure agree: either a direct air waybill (no ConsolidatedShipment, no ChildConsignment, indicator false), or a master waybill (indicator true, forwarder as shipper, the house waybill identifiable).
- Options: (a) direct waybill: drop the consolidation and the child (preferred: one small consignment, a priority flight, and Lumeway named as consignor); (b) consolidation: set the indicator to true and make the story a forwarder consolidation.
- Needs decision: yes

### air/04#F3 · High · AdValoremIndicator contradicts the forwarding instructions
- XPath: `/Waybill/cbc:AdValoremIndicator` = `true`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- Why: The same shipment is "ad valorem" in the waybill and not in the forwarding instructions. UBL defines the indicator by "ad valorem duties, which are levied on commodities at certain rates per centum on their value". Whether duties are ad valorem is a property of the goods' tariff treatment and cannot change between the two documents. If the indicator is meant as the carrier's valuation charge for the declared value, it is used against its definition.
- Condition: both documents state the same value, chosen according to the UBL definition (duties), or both leave the indicator out.
- Options: (a) leave it out in both (preferred: neither document deals with duties); (b) the same value in both, with the duty treatment as the reason.
- Needs decision: no

### air/04#F4 · High · Exchange rate established a week after the waybill was issued
- XPath: `/Waybill/cac:ExchangeRate/cbc:Date` = `2026-05-20`
- XPath: `/Waybill/cbc:IssueDate` = `2026-05-13`
- Why: ExchangeRate/Date is "The date on which the exchange rate was established". A waybill issued on 13 May cannot quote a rate established on 20 May.
- Condition: the exchange rate date is not later than the issue date, or the exchange rate is absent (see F9).
- Options: remove the exchange rate (preferred, F9), or date it on or before 13 May.
- Needs decision: no

### air/04#F5 · Medium · The consignor-assigned ID of the child consignment is the forwarding instruction's document number
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ConsignorAssignedID` = `LD-FI-26-0322`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: ConsignorAssignedID is "An identifier for this consignment, assigned by the consignor". Lumeway's own number for its consignment is `LD-CS-26-0324` (03). `LD-FI-26-0322` is the ID of a document, the forwarding instruction. One kind of identifier is used as another.
- Condition: ConsignorAssignedID holds the consignor's consignment identifier, or the child consignment is removed (F2, option a).
- Options: follows from F2; if the child stays, `LD-CS-26-0324`.
- Needs decision: no

### air/04#F6 · Medium · A warehouse as substitute carrier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cbc:IndustryClassificationCode` = `5210`
- Why: SubstituteCarrierParty is "The Party who subtitutes the carrier of this Consignment", i.e. one that performs the carriage in the carrier's place. Nalevi Warehousing is a warehouse (ISIC 5210), and in this flow it is the delivery recipient (`01-OrderChange.xml` DeliveryParty, `06-DespatchAdvice.xml` DeliveryCustomerParty). Nothing says it takes over any carriage from Kelaro.
- Condition: the role in which Nalevi appears is one it plays in the story (delivery party or notify party), or a real substitute carrier is named.
- Options: (a) Nalevi as notify party or delivery address (e.g. Consignment/NotifyParty or a delivery location) (preferred); (b) if Nalevi trucks the goods from the airport, say so with an on-carriage stage, but then it is an on-carrier, not a substitute for the airline.
- Needs decision: yes

### air/04#F7 · Medium · LocaleCode holds a language code
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files carry this pattern).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/04#F8 · Low · The carrier's own flight schedule is given as "requested" events
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedArrivalTransportEvent/cbc:OccurrenceTime` = `10:00:00`
- Why: A requested departure is "The departure requested by the party requesting a transportation service". The waybill is the carrier's document, and flight KXL207 at 07:00–10:00 is the carrier's schedule, i.e. planned or estimated times. The forwarding instructions requested no flight times (only despatch on 13 May and delivery on 14 May).
- Condition: the flight times are in the planned (or estimated) departure and arrival events, unless the story has the shipper requesting these times.
- Options: PlannedDepartureTransportEvent / PlannedArrivalTransportEvent (preferred).
- Needs decision: no

### air/04#F9 · Low · Exchange rate without any amount to convert
- XPath: `/Waybill/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Waybill/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The only amounts are the declared value in XBL. The waybill carries no charges collect in Coral, which is the usual reason for a rate on an air waybill, so nothing uses the rate.
- Condition: the exchange rate is absent, or the waybill carries the amounts it converts.
- Options: remove it (preferred).
- Needs decision: no

### air/04#F10 · Low · Special security without a reason
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:SpecialSecurityIndicator` = `true`
- Why: The indicator says "the transported goods in this consignment require special security". Eight cast-iron bench side frames worth 512 XBL are not valuable, dangerous or sensitive goods, and no other value explains it. Ordinary air cargo screening is not "special security".
- Condition: the indicator is absent (or false), or the document gives the reason.
- Options: remove it (preferred).
- Needs decision: no

### air/04#F11 · Low · Issue location named after the company, without an identifier
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: A location's name is the place, not the company. Here it is the terminal operator's company name (cf. `05-TransportationStatus.xml`, where that company is the TerminalOperatorParty and the place is `XBLMA`, "Lumeport airport"). The waybill identifies the same airport as `XBLMA` in the loading port.
- Condition: the issue location names or identifies the place (e.g. "Lumeport airport, cargo terminal" with `XBLMA`).
- Options: name and UN/LOCODE of the airport.
- Needs decision: no

### air/04#F12 · Low · Contacts do not fit their roles
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The carrier's "Cargo sales" contact is an operations planner in Operations. The consignee's "Purchasing" and the warehouse's "Goods inwards" are customer service officers in Sales. In each, name and title disagree, and the consignee's contact does not receive goods. The same combinations occur in 8 ("Cargo sales") and 52 ("Purchasing") example files.
- Condition: each contact's name, title and department agree with each other and with the party's role.
- Options: align the names or the titles.
- Needs decision: no

## Checked and consistent
- Chargeable weight: gross volume 0.576 m³ = 576 000 cm³ / 6000 cm³ per kg (the IATA volumetric divisor, own knowledge) = 96 kg, higher than the 81.6 kg gross, so 96 kg is right.
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross weight 81.6 kg and declared value 512.00 XBL agree with `03-ForwardingInstructions.xml` and `06-DespatchAdvice.xml`. DeclaredCarriageValueAmount and Shipment/DeclaredForCarriageValueAmount agree with each other.
- Loading `XBLMA` (Bayvarra) and unloading `XLSLA` (Lisavu) are fictional UN/LOCODEs in fictional countries. The aircraft type code ATF is IATA's ATR 72 freighter. The registration `QL-KXA` uses a nationality mark not allocated by ICAO (own knowledge). The payload of 81.6 kg is far below an ATR 72F's capacity of several tonnes.
- The flight from 07:00 to 10:00 is in one time zone (both addresses at UTC−1) and lasts 3 hours, and it is after the issue time (13 May 10:43).
- Kelaro, Bayforth, Lumeway, Velumi and Nalevi carry the same identifiers as in the other examples. GLN check digit OK.

## Considered and refuted
- `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`: a second number next to the waybill ID. Refuted because CarrierAssignedID identifies "a specific shipment" for the carrier, and an AWB-style shipment number is a legitimate reading.
- `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`: only the consignee's original and an electronic copy are in DocumentDistribution. Refuted because the distribution need not list the originals kept by the carrier and handed to the consignor at issue.
- `/Waybill/cbc:Name` = `Air waybill under the Montreal Convention`: a real convention in a fictional world. Refuted because a real treaty that the fictional states can have joined is not a value from a register that could be mistaken for a real identifier.

## Outside this review
- Timeline: `05-TransportationStatus.xml` reports the cargo accepted at the terminal at 10:05, before this waybill was issued (10:43). The reference problem is recorded in 05; the order of events is a timeline question.
