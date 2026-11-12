# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/02-TransportExecutionPlanRequest.xml`, Git blob `bb392b17a2189c68bda879780827c73623d85abb` (committed)
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

### ore/02#F1 · High · A container train is requested for ore loose in wagons
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: the world's TransportServiceCode list defines RAILCONT as "Containers on a scheduled container train". Nothing in the flow is in containers: this request asks for "Wagons sheeted against dust." (`/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`), the ordered item is "loose in rail wagons" (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`), the despatch is "30 wagons of about 60 tonnes" (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`) and the carrier bills "ore in bulk wagons" (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`). The same list has RAILWAGON ("A whole wagon for one consignment").
- Condition: the main transportation service code and name describe carriage of bulk ore in rail wagons, consistent with the special terms and with 01, 04 and 06.
- Options: (a) preferred: RAILWAGON "Rail wagon load" (or, if a whole train for one consignment should be distinguishable, a new code such as a block/unit train added to the world's list); (b) keep RAILCONT only if the story changes to ore in containers, which would contradict four other examples.
- Needs decision: no

### ore/02#F2 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- Why: a Transport Execution Plan Request is "sent by a transport user to request a transport service"; the consignment is the only place that says what the service is for, and here it carries only an ID, a weight and the two parties: no goods item, no description, no commodity code, no indication that it is bulk ore. Only the free-text note ("The ore train from the mine siding to the factory.") hints at it. The carrier needs the commodity (tariff class, dust sheeting, wagon type) to plan the train.
- Condition: the consignment states in structured form what is carried (at least a goods item with description and/or commodity classification of the iron ore, and the quantity).
- Options: (a) preferred: a `GoodsItem` with the ore description, HS 260111 and the weight (the values used in 01); (b) at minimum `Consignment/cbc:Information` or a goods item description.
- Needs decision: no

### ore/02#F3 · Medium · A province is given in `Region`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity` ("the political or administrative division of a country … such as the name of its county, province, or state"), as the world does for Bayvarra's states. "Province of Ferrano" is in `Region` in 104 XML examples (`grep -rl --include='*.xml' 'Province of Ferrano' world/examples | wc -l`).
- Condition: the province is in `CountrySubentity` in every address of this example.
- Options: (a) preferred: move it to `CountrySubentity` (with a code if an Urvanian list is wanted); (b) if it is meant as an economic region, give it a name that does not read as a province.
- Needs decision: no

### ore/02#F4 · Low · From- and to-location are company names with office addresses, not the sidings
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- Why: FromLocation/ToLocation are "the location of origin" and "the destination location" of the transport service. A location's name is the place, not the company; and the business addresses (Strada della Miniera 10, Via delle Officine 17) are the parties' postal addresses. The train runs "from the mine siding to the factory" (note) and is billed "from the mine siding to the factory siding" (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Ore from the mine siding to the factory siding, per tonne.`); the same document names the mine siding in `/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`, and the mine has the UN/LOCODE `XUSRV` in the consignor's PhysicalLocation.
- Condition: FromLocation and ToLocation name and identify the mine siding and the factory siding (name of the place, and an identifier or address that designates the siding, not the head office).
- Options: (a) preferred: FromLocation "Serravona mine siding" with ID `XUSRV`, ToLocation "Valdara factory siding" with its identifier; (b) keep the addresses but name the places and use an address type for a delivery/operational site if the world's list has one.
- Needs decision: no

### ore/02#F5 · Low · An assay certificate is referenced in a request to the carrier, without saying what it is
- XPath: `/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`
- Why: the reference carries only an ID; nothing says it is an assay (the type has to be guessed from the number) and nothing in the transport request uses it: the carrier plans and prices a train by weight and wagon type, not by the ore's assay. Where the assay would matter, the seller's invoice that deducts 1.5 % for moisture (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Moisture deduction`), it is not referenced.
- Condition: an assay reference appears only in a document that uses it, and every document reference whose kind is not obvious says what it refers to.
- Options: (a) preferred: drop it here (and consider referencing it from 07, see that review); (b) if the carrier needs it (e.g. for a declaration the story describes), add `DocumentTypeCode`/`DocumentType` and the reason.
- Needs decision: no

### ore/02#F6 · Low · The transport user's and consignor's contacts are sales desks
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- Why: the sender of a transport request is the transport user; its contact handles the transport (logistics/inbound planning), and the consignor's contact is the one who hands the goods over (loading at the siding). Both are sales/customer-service desks ("Customer service officer", Department "Sales") here, copied from the parties' master data; the carrier's contact, by contrast, is its freight desk in Operations.
- Condition: the sender's and consignor's contacts are functions that handle the transport and the loading.
- Options: (a) preferred: Valdara's logistics/inbound planning contact and Serravona's loading/siding contact; (b) omit the contacts where the world has none.
- Needs decision: no

### ore/02#F7 · Low · Party master data the request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: the sender's stock-exchange listing and its warehousing provider (Castrano Logistics, in no other role in the flow) have nothing to do with ordering a train; the road-access condition of the mine is irrelevant to a rail collection at the siding. They look copied from master data (SecurityListing `XU0001042501` in 75 XML examples, service provider `VI-SP-2026-01` in 75).
- Condition: every aggregate of the parties has a use in this request.
- Options: (a) preferred: leave the security listing and service provider out; keep the PhysicalLocation (its UN/LOCODE identifies the origin) but without the road condition, or move the siding data to FromLocation (F4).
- Needs decision: no

## Checked and consistent
- Dates: issued 2026-03-03 09:24; response deadline 2026-03-04 (the plan 03 was issued 2026-03-04 12:50, in time); service window 2026-03-10 to 2026-03-13 inside the order's requested delivery period 2026-03-09 to 2026-03-13 (01).
- Parties: transport user and bill-to Valdara (the buyer, who contracts the carriage under FCA in 01), service provider Ferrano Rail Cargo (the carrier named in 01), consignor Serravona (the seller), consignee Valdara.
- Consignment VI-CS-26-0306 weighs 1 800 000 kg = 1800 t, the ordered quantity in 01; "excluding the carrier's equipment" matches the ore without wagons.
- AdditionalTransportationService WEIGH at the AtLocation "Serravona mine siding": a service without movement at a named place, as AtLocation is defined.

## Considered and refuted
- `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonCode` = `UPDATE` with `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`: a reason "associated with the status" next to no status — refuted because the request is itself an original (NoStatus is right), and UPDATE ("The request or plan changes a plan already agreed") states why it exists relative to the referenced standing plan `FRC-TEP-26-0001`; no other element carries that reason.
- `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`: "this week" against the monthly call-off of 01 — refuted because the standing plan is the carrier's plan, which may be weekly, and the train does run this week.
- `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001` and `/TransportExecutionPlanRequest/cac:TransportServiceDescriptionDocumentReference/cbc:ID` = `FRC-TSD-26`: references to documents outside the flow — refuted for this lens because both elements name their kind (original plan, service description) and an update of a standing plan has a reason to cite both.
- `/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`: AtLocation in a request for a moving service — refuted because it is the place of the weighing service, which needs no movement.
- `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Valdara Industries`: bill-to equal to the transport user — refuted because the element is defined as the party that will receive the invoice, which is a statement in its own right, and 06 is addressed to Valdara.
