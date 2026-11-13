# LLM review: 13-Waybill.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/13-Waybill.xml`, Git blob `0e28ae8a70150ecfdb1e12ab9527a6f9336f5e5e` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/13#F1 · High · Three originals in the note, one original and an electronic copy in the distribution
- XPath: `/Waybill/cbc:Note` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: the note says the consignment note is issued in three originals, for consignor, consignee and carrier (as a CMR note is). The document distribution lists the consignee's original and, for the consignor Lumeway, an electronic copy, not an original; the carrier's original is not listed. The structured distribution contradicts the note for the consignor.
- Condition: the distribution and the note describe the same set of originals and copies.
- Options: (a, preferred) give the consignor an original in the distribution (and add the carrier's if the distribution is meant to be complete); (b) change the note, if the world's electronic consignment note replaces the consignor's paper original.
- Needs decision: no

### retail/13#F2 · High · The carrier's shipment reference differs in each transport document
- XPath: `/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: `CarrierAssignedID` is "An identifier (in the form of a reference number) assigned by a carrier or its agent to identify a specific shipment". All three documents concern the same consignment `LD-CS-26-0228`, carried by Bayforth, yet the carrier's reference is `BF-CMR-26-0217` here, the waybill number in the status request and `BF-ROAD-26-0231` in Bayforth's own status report. A shipment has one carrier reference; the three cannot all be it.
- Condition: the carrier-assigned ID is the same in the waybill, the status request and the status, or each value is shown to be a different kind of reference in an element that fits it.
- Options: (a, preferred) one carrier reference (e.g. `BF-CMR-26-0217`, the CMR number) in all three; (b) drop it where the document ID already serves as the carrier's reference.
- Needs decision: no

### retail/13#F3 · Medium · Consignment note without goods, packages and places of taking over and delivery
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `996`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: a waybill is "A transport document describing a shipment"; a road consignment note records the goods taken over: their description, the number of packages and their marks, the gross weight, and the places and dates of taking over and of delivery (own knowledge of CMR Art. 6). This one gives only the gross weight, the consignment ID and the parties. The six pallets, their marks (`BRIGHTMARKET LUMEPORT / 001 of 006` …), the benches and the two addresses are only in 11 and 12. Damage, which the despatch advice asks to report "on the consignment note", cannot be recorded against goods the note does not describe.
- Condition: the waybill describes the goods (description, number and kind of handling units, marks) and the places of taking over and delivery.
- Options: (a, preferred) add a goods item or handling units with description, package count and marks, and the shipment's delivery with pick-up and delivery places and dates; (b) at least a consignment-level description and package count.
- Needs decision: no

### retail/13#F4 · Medium · Consignment ID used as shipping order ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: `ShippingOrderID` is "An identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". `LD-CS-26-0228` is the consignment's identifier; the forwarding instruction in this flow is 11-TransportExecutionPlanRequest (`LD-TR-26-0227`). An identifier of one kind is used as another.
- Condition: the shipping order ID is the ID of the forwarding instruction, or absent.
- Options: (a, preferred) `LD-TR-26-0227`; (b) drop it (the consignment ID is already given).
- Needs decision: no

### retail/13#F5 · Medium · Language codes in LocaleCode
- XPath: `/Waybill/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/13#F6 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/13#F7 · Low · A CMR consignment note for a domestic carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/Waybill/cbc:Name` = `Consignment note under the road convention, the CMR`
- Why: the CMR convention applies to the international carriage of goods by road (own knowledge, CMR Art. 1); this carriage runs from Marrowdale (Upland State) to Lumeport (Coastal State), both in Bayvarra. Unless the world's Bayvarran law adopts the CMR for domestic road haulage, a national consignment note is the document that applies.
- Condition: the waybill type is one that applies to a domestic Bayvarran road carriage, or the world states that Bayvarra applies the CMR domestically.
- Options: (a, preferred) a national road consignment note type (in the world's waybill type list); (b) record in the story that Bayvarra applies the CMR to domestic carriage.
- Needs decision: yes

### retail/13#F8 · Low · Issue location named after the company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeway Distribution`
- Why: `IssueLocation` is the place where the waybill was issued; the name given is the consignor's company. The place is Lumeway's distribution centre in Marrowdale, where the goods were taken over.
- Condition: the issue location names a place (and may carry its address or identifier).
- Options: (a, preferred) "Marrowdale" or "Lumeway distribution centre, Marrowdale".
- Needs decision: no

### retail/13#F9 · Low · Contacts that do not fit the transport roles
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Bayforth, the carrier, is represented by its "Export desk" for a domestic haul; Lumeway, the consignor, by its customer service in sales; Brightmarket, the consignee who receives the goods and signs for them ("Deliver against signature of the consignee"), by its buying office, whose job title and department also contradict its name. The flow names fitting contacts elsewhere (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`; `08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`).
- Condition: each party's contact fits its role in the carriage, and name, job title and department agree.
- Options: (a, preferred) Bayforth's domestic or road operations, Lumeway's dispatch office, Brightmarket's goods-in.
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0230`, consignment `LD-CS-26-0228` and gross weight 996 kg agree with 11-TransportExecutionPlanRequest and 12-DespatchAdvice.
- Parties: sender and carrier Bayforth, receiver and consignor Lumeway, consignee Brightmarket, as in 11; described as in every retail example.
- `AdValoremIndicator` `false` fits a carriage without declared value; `ConsolidatedIndicator` `false` fits a dedicated full truck load.
- The waybill is referenced by 16-Invoice (`16-Invoice.xml:/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `BF-WB-26-0231`).
