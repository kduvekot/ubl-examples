# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

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

### ore/02#F1 · High · Container-train service requested for ore loose in wagons
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: TransportationService/TransportServiceCode is "A code signifying the extent of this
  transportation service". In the world's list `RAILCONT` means "Containers on a scheduled
  container train"; the same list has `RAILWAGON` "Rail wagon load – A whole wagon for one
  consignment". The goods are "loose in rail wagons"
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`),
  the despatch is "One train: 30 wagons of about 60 tonnes"
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note`) and the carrier bills "Rail
  freight, ore in bulk wagons" (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]`).
  No container occurs anywhere in the flow.
- Condition: the main transportation service names a wagon-load (bulk) rail service, consistent with
  the goods, the despatch advice and the freight invoice, in this example and in
  `03-TransportExecutionPlan.xml`.
- Options: (a, preferred) `RAILWAGON` "Rail wagon load" (30 wagons for one consignment fits "a whole
  wagon for one consignment" per wagon); (b) a new code for a block (whole) train if the world wants
  to distinguish it.
- Needs decision: no

### ore/02#F2 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- Why: a Transport Execution Plan Request is "sent by a transport user to request a transport
  service"; the carrier needs to know the goods to plan wagons and sheeting. The consignment carries
  only an ID, a gross weight and the two parties: no goods item, no description, no commodity code,
  no number or type of wagons. The goods appear only indirectly in the notes ("The ore train …") and
  in an assay reference. Section 4.3: a transport request that does not say what is to be carried.
- Condition: the consignment states the goods (at least description or commodity classification and
  the quantity/weight per goods item), so that the request alone says what is to be carried.
- Options: (a, preferred) a `cbc:SummaryDescription` of the consignment naming the goods (loose
  iron ore lump, 62 % Fe, HS 260111, 1 800 t in 30 open wagons), as other transport requests of the
  world do (e.g. `rail/02-TransportExecutionPlanRequest.xml`); (b) structured goods items in the
  consignment's consolidated shipment, as in `01-Order.xml`.
- Needs decision: no

### ore/02#F3 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this
  address is located"; a province is a territorial division of the country, for which UBL has
  `CountrySubentity`. 104 `*.xml` files carry a province in Region (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/02#F4 · Low · Status reason given for a document without status
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonCode` = `UPDATE`
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
- Why: DocumentStatusReasonCode is "A code signifying a reason associated with the status of the
  Transport Execution Plan Request". The status is `NoStatus` ("No status on document"), so there is
  no status for the reason to explain; the reason "Update of a standing plan" describes the
  request's relation to the standing plan (`TransportExecutionPlanDocumentReference`
  `FRC-TEP-26-0001`), not a status of this document.
- Condition: the status reason explains the status it accompanies, or there is no status reason.
- Options: (a, preferred) drop the status and status reason and keep the explanation in a note
  next to the reference to the standing plan; (b) use a status the reason fits.
- Needs decision: no

### ore/02#F5 · Low · "This week's quantity" against a monthly call-off of one train
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
- XPath: `01-Order.xml:/Order/cbc:Note[2]` = `Monthly call-off, one train.`
- Why: the order calls off one train a month; the request explains its deviation by "this week's
  quantity", which implies a weekly rhythm. Also the 1 800 t requested is exactly the ordered
  quantity of the monthly call-off, so it is not clear in what the quantity "differs".
- Condition: the request's explanation and the order describe the same rhythm and quantity.
- Options: (a, preferred) "This month's quantity …" or name the standing plan's quantity; (b) make
  the standing plan weekly in the order's note.
- Needs decision: no

### ore/02#F6 · Low · From and to locations named after the companies, not the places
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: the name of a location is the place, not the party. The places are the mine siding
  (`/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`, UN/LOCODE
  `XUSRV` in the consignor's physical location) and the factory siding (named so in
  `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Ore from the mine siding to the factory siding, per tonne.`).
  The addresses given are the companies' business addresses (`AddressTypeCode` `BUSINESS`).
- Condition: from and to location names (and identifiers where the place has one) designate the
  sidings, not the companies.
- Options: (a, preferred) names "Serravona mine siding" / "Valdara factory siding", with `XUSRV`
  as ID of the origin; (b) keep the names and add the place identifiers.
- Needs decision: no

### ore/02#F7 · Low · Contacts do not fit the roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender is the transport user that books the train; its contact should be the person who
  handles inbound transport (logistics/purchasing), not a sales customer-service officer. The
  consignor's contact is where the carrier arranges loading at the siding; Serravona's `Sales office`
  is the commercial desk. The same contacts are used in every role in the flow.
- Condition: the sender's contact handles transport for Valdara; the consignor's contact handles
  despatch/loading at the mine.
- Options: (a, preferred) role-specific contacts (Valdara logistics, Serravona siding/despatch);
  (b) leave out job title and department.
- Needs decision: no

### ore/02#F8 · Low · Buyer's logistics service provider copied into the request
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics (warehousing and despatch for Valdara) plays no part in this transport,
  which Ferrano Rail Cargo performs and Valdara unloads itself. Master data without use in the
  document (section 4.8); present in 75 `*.xml` files (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: no service provider without a role in the request.
- Options: (a, preferred) leave it out; (b) give it a role and state it.
- Needs decision: no

### ore/02#F9 · Low · References with only an ID, to documents that are not in the flow
- XPath: `/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`
- XPath: `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
- Why: none of the three referenced documents (`SM-ASSAY-26-11`, `FRC-TEP-26-0001`, `FRC-TSD-26`) is
  an example of the flow (`flow_index.py ore`: `-> ?`); that is acceptable for a standing plan and a
  service description issued earlier. The additional reference, however, has neither a
  `DocumentTypeCode` nor a `DocumentDescription`, so the receiver cannot tell from the document that
  it is an assay certificate, nor why the carrier gets it (a Serravona assay, number 11, sent by the
  buyer to the carrier).
- Condition: the additional reference says what kind of document it is and is there for a reason
  the carrier has (or it is left out).
- Options: (a, preferred) add a type code/description ("Assay certificate of the lot") if the
  carrier needs it (e.g. for the moisture or dust class); (b) leave it out of the transport request.
- Needs decision: no

## Checked and consistent
- Consignment gross weight 1 800 000 kg = 1 800 t = ordered quantity
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800`); consignment ID
  `VI-CS-26-0306` is the same in `03-TransportExecutionPlan.xml`, `04-DespatchAdvice.xml` and
  `05-Waybill.xml`.
- Service period 10–13 March lies within the order's requested delivery period 9–13 March.
- Response deadline 4 March; the plan is issued on 4 March 12:50
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cbc:IssueDate` = `2026-03-04`).
- Transport user, bill-to and sender are Valdara, which fits FCA (buyer pays main carriage) and the
  freight invoice to Valdara (`06-Invoice.xml`).
- The framework contract `VI-FRC-FW-2026` is the same in `03-TransportExecutionPlan.xml`.
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` =
  `WEIGH`: suspected a service without a place — refuted because the AtLocation (`Serravona mine
  siding`) gives the place where weighing without movement happens.
- `/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` =
  `Wagons sheeted against dust.`: suspected implausible for lump ore — refuted because dust from
  ore wagons is a real concern and covering wagons is common practice (own knowledge).
- `/TransportExecutionPlanRequest/cac:Signature/cbc:ID` = `VI-SIG-TEPR`: suspected a signature
  without content — refuted because UBL only requires the ID; the signatory is the sender.
