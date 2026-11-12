# LLM review: 08-Waybill.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/08-Waybill.xml`, Git blob `72164dc3855513c969135349f0d20e5d5cef08c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/08#F1 · High · The waybill, issued in the morning, reports events of the afternoon and the next day
- XPath: `/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceDate` = `2026-03-24`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:Remarks` = `Received in apparent good order; seals XU-CL-77310 on the trailer doors.`
- Why: a CMR consignment note is made out when the carrier takes over the goods; its remarks ("Received in apparent good order", seals applied) record the takeover. This waybill is issued on 2026-03-23 at 08:16 but states an actual pickup at 15:05, an actual departure at 16:20 and a seal check on the next morning, and the takeover remarks; none of these can be known at 08:16. The waybill is also issued at Castrano's warehouse (`/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`) seven hours before the truck is there.
- Condition: every actual event and takeover remark in the waybill lies before its issue time; events after issue are absent or stated as estimates.
- Options: (a) issue the waybill at takeover (after loading, before the 16:20 departure) and drop the next-day examination, which belongs in the status report (preferred: a CMR is made out at takeover); (b) keep the morning issue time and replace the actual events by planned ones.
- Needs decision: no

### road/08#F2 · High · Customs instruction says the 3PL declares the export; the export declaration is Valdara's
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`
- Why: the export declaration of this consignment is made and signed by Valdara as exporter (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyName/cbc:Name` = `Valdara Industries`, `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`), and the waybill's own customs declaration reference is in Valdara's numbering (`VI-CD-…`). The instruction that "the 3PL" (Castrano) declares the export contradicts both.
- Condition: the customs instruction names the party that actually declares the export in the flow.
- Options: (a) "The export is declared by the seller in Ferrano; …" (preferred: matches 05 and FCA, under which export clearance is the seller's); (b) make Castrano the declarant (as agent) in the export declaration.
- Needs decision: no

### road/08#F3 · Medium · Consignment ID given as shipping order number
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0152`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- Why: `ShippingOrderID` is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". The value is the consignment's ID; the shipping order of this transport is Lumeway's transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`). An identifier of one kind is used as another.
- Condition: `ShippingOrderID` holds the number of the shipping order or forwarding instruction (the transport request), or is absent.
- Options: (a) `LD-TR-26-0151` (preferred: the document by which Lumeway ordered the transport); (b) drop it.
- Needs decision: no

### road/08#F4 · Medium · Despatch advice number given as the consignor's consignment ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `CL-DA-26-0153`
- Why: `ConsignorAssignedID` is "An identifier for this consignment, assigned by the consignor". The consignor is Valdara (`/Waybill/cac:ConsignorParty`), but the value is Castrano's despatch advice number (`04-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `CL-DA-26-0153`): a document number, assigned by another party, used as a consignment identifier.
- Condition: `ConsignorAssignedID` is an identifier of the consignment in the consignor's (or its agent's, if the story says so) numbering, or is absent; the despatch advice, if needed, is referred to as a document.
- Options: (a) drop it (preferred: the consignment ID and the carrier's and consignee's IDs suffice); (b) use a Valdara or Castrano shipment reference such as the shipment ID `CL-SH-26-0154`, if Castrano acts for the consignor.
- Needs decision: no

### road/08#F5 · Medium · Customs authority named as issuer of the exporter's declaration
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: `CustomsDeclaration/IssuerParty` is "The Party who issues this Customs Declaration". The declaration `VI-CD-26-0156` is issued (lodged) by the exporter Valdara (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `VI-CD-26-0156`, in Valdara's numbering); the customs administration receives it.
- Condition: the issuer of the customs declaration is the declarant (Valdara), or the party is absent.
- Options: (a) Valdara as issuer (preferred); (b) drop `IssuerParty`.
- Needs decision: no

### road/08#F6 · Medium · Province given as Region
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:ReturnAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:Shipment/cac:OriginAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/08#F7 · Medium · LocaleCode holds a language code
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/08#F8 · Low · Document description narrates the example
- XPath: `/Waybill/cbc:Description` = `The truck the distributor booked, from the 3PL's warehouse across the border.`
- Why: `Description` is "Textual description of the document instance"; the text speaks about the parties in the third person ("the distributor", "the 3PL") and reads as a caption of the example, not as the carrier's description of its waybill. The same sentence is the note of the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:Note` = `The truck the distributor booked, from the 3PL's warehouse across the border.`).
- Condition: the description describes the waybill as the carrier would (or is absent; `Name` already says it is a CMR consignment note).
- Options: (a) drop it (preferred); (b) a carrier's description such as the route and consignment.
- Needs decision: no

### road/08#F9 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Castrano Logistics`
- Why: `IssueLocation` is "The location where this waybill was issued"; its name should be the place (e.g. Castrano's warehouse in Ferrano, which the CMR names as place of issue), not the company.
- Condition: the issue location's name is a place name, or the location is identified by its address or UN/LOCODE.
- Options: (a) "Ferrano" with the UN/LOCODE `XUFER` already used for the pickup (preferred: CMR box "established in"); (b) "Castrano Logistics warehouse, Ferrano".
- Needs decision: no

### road/08#F10 · Low · Contacts that do not fit a consignment note
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the consignee's contact on a waybill is the one who takes delivery and signs for it ("Deliver against signature of the consignee"), i.e. goods-in, not Lumeway's customer service in Sales; the consignor's contact is the one the carrier deals with at loading, which happens at Castrano's warehouse, not Valdara's order desk.
- Condition: the consignee's contact receives goods; the consignor's contact (or a contact for the loading place) handles the loading.
- Options: (a) goods-in for Lumeway and the warehouse office for the loading (preferred); (b) drop the job titles and departments that do not fit.
- Needs decision: no

### road/08#F11 · Low · Consignor's stock-exchange listing in a consignment note
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the listing of Valdara's shares plays no part in the contract of carriage; it looks copied from master data (section 4.8, IND5).
- Condition: the waybill carries no `SecurityListing`.
- Options: drop it (preferred).
- Needs decision: no

### road/08#F12 · Low · Fuel consumption of a trip that has not started at issue
- XPath: `/Waybill/cac:Shipment/cac:Delivery/cac:FuelConsumption/cbc:FuelConsumptionMeasure` = `61`
- Why: `FuelConsumption` records the fuel used for the delivery; at the waybill's issue (08:16, before pickup) the trip has not begun, and nothing in the waybill (no emission figure) uses the value. Fuel used is something the carrier reports after delivery (e.g. in the status report or the freight invoice).
- Condition: the fuel consumption appears in a document issued after the trip, or is stated as an estimate with a use in the waybill.
- Options: (a) move it to a document after delivery (preferred); (b) drop it.
- Needs decision: no

### road/08#F13 · Low · Distribution list does not match the three originals the note names
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: the note says there are three originals (consignor, consignee, carrier, as under the CMR), but the distribution lists only the consignee, once for the original with the goods and once for an electronic copy; the consignor's original is not distributed to anyone.
- Condition: the distribution list and the note agree on who receives which original.
- Options: (a) add the consignor's original to the distribution (preferred); (b) reduce the note to what the distribution says.
- Needs decision: no

## Checked and consistent
- Consignment `LD-CS-26-0152` and shipment `CL-SH-26-0154` are the ones of `03-TransportExecutionPlanRequest.xml` and `04-DespatchAdvice.xml`; gross weight 4 106.4 kg and the 25 pallets agree; 108 packages = 96 benches + 12 castings.
- `WaybillTypeCode` `CMR`, the name "Consignment note under the road convention, the CMR" and the three-originals note agree; `AdValoremIndicator` false fits a CMR without declared value.
- FCA delivery terms, the special terms (the buyer's carrier presents the truck, the seller loads) and the loss risk passing on loading at the warehouse agree with the order (`01-Order.xml`).
- The collect payment note (freight paid by the consignee under its contract with the carrier) and `ThirdPartyPayerIndicator` false agree with the transport request's bill-to party.
- Handling codes `STACK2` on bench pallets and `NOSTACK` on the box pallet agree with the handling instructions next to them.
- The carrier's operating permit fits a CMR for international road haulage (the vehicle must carry the licence), so its presence here is justified.

## Considered and refuted
- `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation`: suspected a port element for a road place — refuted because UBL defines it as "The location of loading for a shipment stage", without restriction to ports.
- `/Waybill/cac:Shipment/cac:Consignment/cbc:CarrierAssignedID` = `TH-26-04471`, equal to the journey and tracking IDs: suspected one identifier used for three things — refuted because in a full truck load the carrier's consignment, journey and tracking numbers can legitimately be the same job number.
- `/Waybill/cac:Shipment/cac:ReturnAddress`: suspected data without a use — refuted because the pallets are returnable (`ReturnableMaterialIndicator` true) and the address says where undeliverable goods and pallets go back to.
