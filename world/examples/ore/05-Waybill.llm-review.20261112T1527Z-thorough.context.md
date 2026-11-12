# LLM review: 05-Waybill.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/05-Waybill.xml`, Git blob `e7a36055c2d576e9c4683563c6c0c9a29856e375` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
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

### ore/05#F1 · Medium · The consignment ID is given as the shipping order
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0306`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- Why: ShippingOrderID is "an identifier (in the form of a reference number) of the Shipping Order or Forwarding Instruction associated with this shipment". VI-CS-26-0306 is the consignment's ID (the same value is Consignment/ID here and in 02, 03, 04), not an order or instruction to the carrier. The instruction to the carrier in this flow is the transport request `VI-TR-26-0305` (02), confirmed by the plan `FRC-TEP-26-0307` (03, already in DocumentReference). Of the 19 XML examples with a ShippingOrderID, 14 carry a consignment number ("-CS-") in it (`grep -rl --include='*.xml' 'ShippingOrderID>[A-Z]*-CS-' world/examples | wc -l`).
- Condition: ShippingOrderID holds the identifier of a shipping order or forwarding instruction that exists in the flow, or is absent.
- Options: (a) preferred: `VI-TR-26-0305`, the transport user's request that instructs the carrier; (b) leave ShippingOrderID out, as the plan is already referenced.
- Needs decision: no

### ore/05#F2 · Medium · The waybill does not describe the goods, the route or the taking-over
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/Waybill/cbc:Description` = `The ore train from the mine siding to the factory.`
- Why: a Waybill is "a transport document describing a shipment"; as a CIM consignment note (`/Waybill/cbc:WaybillTypeCode` = `CIM`) it must state, among others, the description of the goods, the place and date of taking over and the place designated for delivery (CIM Art. 7, own knowledge). The shipment here has only an ID, a weight and the consignee: no goods item or description, no commodity code, no origin or destination, no wagons, no taking-over date. Only the free-text description hints at ore and sidings.
- Condition: the waybill states in structured form what is carried (goods item with description/commodity code and weight), where it was taken over and where it is to be delivered, and when it was taken over.
- Options: (a) preferred: a goods item with the ore data of 01/04, Delivery with the siding locations and the actual pickup (taking-over) date/time, and the wagons as transport equipment if the wagon list is meant to be shown; (b) at least goods description, origin and destination.
- Needs decision: no

### ore/05#F3 · Medium · A CIM consignment note for a domestic carriage
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CIM`
- XPath: `/Waybill/cbc:Name` = `Rail consignment note under the CIM uniform rules`
- Why: the world's WaybillTypeCode list defines CIM as "A consignment note under the Uniform Rules concerning the Contract of International Carriage of Goods by Rail"; the real CIM rules (Appendix B to COTIF) apply to international carriage only (own knowledge). This carriage runs from Serravona to Ferrano, both in Urvania (consignor and consignee addresses with country `XU`). Unless Urvanian law applies the CIM rules to domestic carriage too (which no document says), the code and the name state a legal regime that does not apply. This is the only XML example with WaybillTypeCode CIM.
- Condition: the waybill type and name name the regime that governs this domestic rail carriage, or the world states that Urvania applies the CIM rules nationally.
- Options: (a) preferred: a type for a national rail consignment note (new code in the world list, e.g. under the Urvanian rail transport law) and a matching name; (b) keep CIM and record in the world's story that Urvanian law extends the CIM rules to domestic traffic (several real countries have done similar).
- Needs decision: yes (which legal regime governs domestic rail carriage in Urvania is part of the world's story)

### ore/05#F4 · Medium · The shipment's gross weight is the ore alone, without the wagons
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport equipment". 1 788 400 kg is the ore (the despatched and invoiced 1788.4 t, `04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`), without the 30 wagons (about 20–25 t tare each, own knowledge, i.e. about 600–750 t more). On a waybill the carrier knows the wagons; the figure is the weight of the goods, which the CIM note states as such.
- Condition: the ore weight is given in an element whose definition excludes transport equipment (e.g. Consignment/GrossWeightMeasure or Shipment/NetWeightMeasure), or the gross shipment weight includes the wagons.
- Options: (a) preferred: Consignment/GrossWeightMeasure = 1 788 400 kg (as in 02/03 for the planned 1 800 000 kg); (b) give the loaded-train weight in Shipment/GrossWeightMeasure if wanted.
- Needs decision: no

### ore/05#F5 · Medium · A province is given in `Region`
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" (`CountrySubentity`), as for Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it; (b) rename it if it is an economic region.
- Needs decision: no

### ore/05#F6 · Low · The note announces three originals, the distribution lists one
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: DocumentDistribution is "a list of interested parties to whom this document is distributed". It lists the consignee's original with the goods and an electronic copy, both to Valdara, but not the consignor's original (the duplicate the CIM note gives the consignor at taking-over). The carrier keeps its own and need not be listed; the consignor's is missing, so the note and the structured distribution do not agree.
- Condition: the distribution list and the note describe the same originals: either the consignor's original is listed (to Serravona Mining), or the note no longer names it.
- Options: (a) preferred: add a distribution of an original to the consignor (e.g. ORIGINALCOURIER or COLLECT, as the story has it); (b) adjust the note.
- Needs decision: no

### ore/05#F7 · Low · The issue location is a company name
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining`
- Why: IssueLocation is "the location where this waybill was issued"; a location's name is the place. The note was issued at the mine siding (UN/LOCODE `XUSRV` in the consignor's PhysicalLocation), not "at" the company.
- Condition: IssueLocation names (and preferably identifies) the place of issue.
- Options: (a) preferred: name "Serravona mine siding" with ID `XUSRV`; (b) the town Serravona.
- Needs decision: no

### ore/05#F8 · Low · The reference to the transport plan does not say what it is
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FRC-TEP-26-0307`
- Why: DocumentReference is "a reference to another document associated with this document"; with only an ID the reader must guess that it is the transport execution plan (03), which is the contract basis of the carriage.
- Condition: the reference states its kind.
- Options: (a) preferred: DocumentTypeCode `TransportExecutionPlan` from the world's document-type list.
- Needs decision: no

### ore/05#F9 · Low · Receiver's and consignor's contacts are sales desks
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- Why: the waybill's receiver (Valdara as transport user and consignee) needs a contact who receives the train; the consignor's contact is the one who handed over the goods and signs the note. Both are customer-service desks in Sales, copied from master data.
- Condition: the contacts are functions that handle receipt and loading.
- Options: (a) preferred: Valdara's goods-receipt contact, Serravona's siding/loading contact; (b) omit.
- Needs decision: no

### ore/05#F10 · Low · Party master data the waybill does nothing with
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the receiver's share listing and warehousing provider (in no role in the flow) have no use in a consignment note; the road-access condition does not concern a train collected at the siding. Same master data in 75 XML examples each.
- Condition: every aggregate of the parties has a use in this waybill.
- Options: (a) preferred: leave them out (the siding as place of taking over belongs in the shipment, F2).
- Needs decision: no

## Checked and consistent
- DocumentReference `FRC-TEP-26-0307` resolves to 03 (the plan under which the carriage runs); consignment `VI-CS-26-0306` and consignee Valdara as in 02/03/04; carrier, sender and signatory Ferrano Rail Cargo; consignor Serravona Mining.
- Issued 2026-03-10 11:35, on the first day of the service window of 03, before the despatch advice of the same day (15:37).
- Weight 1 788 400 kg = 1788.4 t, the despatched (04) and invoiced (06, 07) quantity.
- DocumentDistribution codes fit their texts in both languages; the electronic copy to the consignee whose paper original travels with the goods fits ELECTRONICCOPY ("the original is held or sent elsewhere").

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: an indicator about ad valorem duties in a domestic transport — refuted because on a consignment note the indicator expresses whether a value has been declared for the carriage (a declared value raises the carrier's liability); "false" is a real statement for this train, not a filler.
- `/Waybill/cbc:ConsolidatedIndicator` = `false`: refuted, a carrier's own note for one consignment is not consolidated, and the waybill type allows both.
- `/Waybill/cbc:CarrierAssignedID` = `FRC-CIM-26-0304`: a second carrier number next to the waybill ID — refuted because it is defined as the carrier's reference for the shipment, which can differ from the document number.
- `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`: instruction that could be structured — refuted, UBL has no structured element for proof-of-delivery requirements on a waybill.
