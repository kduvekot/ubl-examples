# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/02-TransportExecutionPlanRequest.xml`, Git blob `bb392b17a2189c68bda879780827c73623d85abb` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
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
  transportation service". In the world's list `RAILCONT` means "Containers on a scheduled container
  train"; the same list has `RAILWAGON` "Rail wagon load – A whole wagon for one consignment".
  Nothing in the flow is in containers: this request asks for sheeted wagons
  (`/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`),
  the goods are
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`),
  the despatch is
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`)
  and the carrier bills
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`).
  The request contradicts its own special terms and four other examples.
- Condition: the main transportation service code and name describe carriage of bulk ore in rail
  wagons, consistent with the special terms, with 01, 04 and 06, and with
  `03-TransportExecutionPlan.xml`.
- Options: (a, preferred) `RAILWAGON` "Rail wagon load" with a matching name; (b) a new world code
  for a whole (block) train, if "wagon load" is felt too narrow for a 30-wagon train.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### ore/02#F2 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- XPath: `/TransportExecutionPlanRequest/cbc:Note[2]` = `The ore train from the mine siding to the factory.`
- Why: a Transport Execution Plan Request is "sent by a transport user to request a transport
  service"; the carrier needs the commodity (tariff class, dust sheeting, wagon type) to plan the
  train. The consignment carries only an ID, a gross weight and the two parties: no goods item,
  description, commodity code, or number and type of wagons. That the goods are ore comes only from
  the free-text note, the status reason and an assay reference. Section 4.3 / section 6 name "a
  transport request that does not say what is to be carried" as Medium.
- Condition: the consignment states in structured form what is carried (at least a goods item or
  consignment description with the ore's description and/or commodity classification, and the
  quantity), and, if the request concerns the wagons, how many are needed.
- Options: (a, preferred) a `GoodsItem` with the ore description, HS `260111` and the weight (the
  values of 01), optionally the number of wagons as a handling-unit or equipment requirement;
  (b) at least a consignment-level description (`cbc:SummaryDescription` or `cbc:Information`), as
  other transport requests of the world do (e.g. `rail/02-TransportExecutionPlanRequest.xml`).
- Needs decision: no
- From: broad (F2), context (F2), logistics (F3, as Low)

### ore/02#F3 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this
  address is located"; a province is a territorial division of the country, for which UBL has
  `CountrySubentity`, and the world uses CountrySubentity for Bayvarra's states. 219 occurrences in
  104 `*.xml` files (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`; where given, it is in
  `cbc:CountrySubentity`, or the world states why an Urvanian province is a region.
- Options: (a, preferred) move to `CountrySubentity` in all Urvanian addresses; (b) record a decision
  if Region is deliberate; (c) drop.
- Needs decision: no
- From: broad (F3), parties (F1), logistics (F2, the two location addresses), context (F3)

### ore/02#F4 · Low · Weekly quantity in the request, monthly call-off in the order
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
- XPath: `01-Order.xml:/Order/cbc:Note[2]` = `Monthly call-off, one train.`
- Why: the order calls off one train a month; the request explains its deviation from the standing
  plan by "this week's quantity", which implies a weekly rhythm. Both can be true only if the
  standing plan is weekly and the call-off monthly, which neither document says. Also, the 1 800 t
  requested is exactly the ordered quantity of the monthly call-off, so it is not clear in what the
  quantity "differs". The context part refuted this (the carrier's standing plan may be weekly, and
  the train does run this week); that reading is possible, but then a weekly standing plan for a
  monthly train is itself unexplained, so the merge cannot settle it.
- Condition: the request's explanation and the order describe the same rhythm and quantity, or one
  of them says how the monthly call-off relates to the weekly standing plan.
- Options: (a, preferred) "This month's quantity …", or name the standing plan's quantity; (b) say
  in the order's note how the call-off relates to the weekly standing plan.
- Needs decision: yes (the rhythm of the ore trains is part of the story; not settled in the merge)
- From: broad (F5), logistics (F4); refuted by context (see "Considered and refuted")

### ore/02#F5 · Low · Status reason given for a document without status
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonCode` = `UPDATE`
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
- Why: DocumentStatusReasonCode is "A code signifying a reason associated with the status of the
  Transport Execution Plan Request". The status is `NoStatus` ("No status on document"), so there is
  no status for the reason to explain; `UPDATE` ("Update of a standing plan") describes the
  request's relation to the standing plan (`TransportExecutionPlanDocumentReference`
  `FRC-TEP-26-0001`), not a status. Against this (context part): NoStatus is right for an original
  request, the world's list defines UPDATE for exactly this case, and no other element carries the
  reason. Both readings are defensible; the merge cannot settle whether the definition's "associated
  with the status" excludes a reason next to NoStatus.
- Condition: the status reason explains the status it accompanies, or there is no status reason and
  the relation to the standing plan is stated elsewhere (e.g. a note); or a recorded decision says
  why UPDATE with NoStatus fits the definition.
- Options: (a) drop the status reason and keep the explanation in a note next to the reference to
  the standing plan; (b) a status that the reason fits; (c) keep and record the decision. No
  preference in the merge.
- Needs decision: yes (not settled)
- From: broad (F4); refuted by context (see "Considered and refuted")

### ore/02#F6 · Low · From and to locations named after the companies, with their office addresses
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- Why: FromLocation/ToLocation are the location of origin and the destination of the transport
  service; Location/Name is "The name of this location", the place, not the company. The train is
  loaded at the mine siding, which the same example names
  (`/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`) and
  identifies (`/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:ID`
  = `XUSRV`), and delivered to the factory siding
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `Ore from the mine siding to the factory siding, per tonne.`).
  The addresses given are the parties' business addresses. The logistics part counted the pattern
  (a `*Location/cbc:Name` equal to a party name in the same document) at 46 places in 25 `*.xml`
  files (lxml).
- Condition: FromLocation and ToLocation name the places where the train is loaded and unloaded (the
  sidings), and the origin carries the identifier the flow uses for the siding.
- Options: (a, preferred) "Serravona mine siding" with ID `XUSRV` (UN/LOCODE), and "Valdara factory
  siding" with its identifier where it has one; (b) keep the company names and add the sidings as
  `SubsidiaryLocation` or identifiers.
- Needs decision: no
- From: broad (F6), parties (F4), logistics (F6), context (F4)

### ore/02#F7 · Low · The transport user's and consignor's contacts are sales desks
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party"; the sender of a transport request is the
  transport user, whose contact handles inbound transport (logistics), and the consignor's contact
  is where the carrier arranges loading at the siding. Both are customer-service desks in Sales,
  copied from master data (Valdara's `order@valdara.example` in 75 `*.xml` files); the carrier's
  contact, by contrast, is its freight desk in Operations.
- Condition: the sender's contact belongs to the function that books transport, and the consignor's
  to the function that loads the train (or each is left out).
- Options: (a, preferred) role-specific contacts (Valdara logistics, Serravona siding/loading);
  (b) leave out the contacts, or job title and department.
- Needs decision: no
- From: broad (F7), parties (F2), context (F6)

### ore/02#F8 · Low · Party master data the request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: section 4.8 and IND5. Castrano Logistics (warehousing and despatch for Valdara) has no part in
  this transport, which Ferrano Rail Cargo performs and Valdara unloads itself; it occurs only inside
  Valdara's party in all eight ore examples. Valdara's share listing has nothing to do with booking a
  train, and the road-access condition of the mine does not concern a rail collection at the
  siding. Service provider `VI-SP-2026-01` and ISIN `XU0001042501` each in 75 `*.xml` files.
- Condition: every aggregate of the parties has a use in this request.
- Options: (a, preferred) leave the service provider, the security listing and the road condition
  out; keep the PhysicalLocation's UN/LOCODE (it identifies the origin) or move it to FromLocation
  (F6); (b) give Castrano a role in the story.
- Needs decision: no
- From: broad (F8: service provider), parties (F3), context (F7)

### ore/02#F9 · Low · Assay certificate referenced by ID only, in a request that does nothing with it
- XPath: `/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`
- Why: the reference carries only an ID: no `DocumentTypeCode`, `DocumentType` or
  `DocumentDescription`, so the receiver has to guess from the prefix that it is the mine's assay
  certificate, and nothing says why the carrier gets it; a carrier plans and prices a train by weight
  and wagon type, not by assay. Where the assay would matter, the seller's invoice with its moisture
  deduction (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason`
  = `Moisture deduction`), it is not referenced. The logistics part counted ID-only references: 555
  of 595 `*DocumentReference` aggregates in 177 `*.xml` files carry only `cbc:ID` (lxml).
- Condition: the additional reference says what kind of document it is, and is present only if the
  request has a reason to carry it.
- Options: (a, preferred) drop it here (and consider referencing it from 07); (b) if the carrier needs
  it (e.g. for a moisture or dust class), add a type code or description and the reason.
- Needs decision: no
- From: broad (F9), logistics (F5), context (F5)

### ore/02#F10 · Low · Standing plan and service description referenced but not in the flow
- XPath: `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
- XPath: `/TransportExecutionPlanRequest/cac:TransportServiceDescriptionDocumentReference/cbc:ID` = `FRC-TSD-26`
- Why: neither resolves to an example of the flow (`flow_index.py ore`: `-> ?`). Against a finding
  (broad and context parts): both elements name their kind (original plan, service description),
  and an update of a standing plan has a reason to cite both, which may well exist outside the
  examples. Whether the world wants them as examples is a story question the merge cannot settle.
- Condition: each referenced document exists in the world as intended, or a decision records that it
  needs no example.
- Options: (a, preferred) record that the standing plan and service description are documents
  outside the examples; (b) add them as examples.
- Needs decision: yes
- From: logistics (F5, the part asking for a decision); broad (F9) and context accepted these two
  references

## Checked and consistent
- Consignment gross weight 1 800 000 kg = 1 800 t = ordered quantity
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800`) = 30 × 60 t (04); for loose
  ore without packaging the consignment gross weight ("excluding the carrier's equipment") equals the
  net weight; a planned figure (actual 1 788.4 t in 04).
- Consignment ID `VI-CS-26-0306` is the same in 03, 04 and 05; consignor, consignee and carrier agree.
- Dates: issued 2026-03-03 09:24; response deadline 2026-03-04, met by 03 (issued 2026-03-04 12:50);
  service window 2026-03-10 to 2026-03-13 inside the order's requested period 2026-03-09 to
  2026-03-13.
- Roles: sender, transport user, bill-to, signatory and consignee Valdara (the buyer, who contracts
  the carriage under FCA); receiver and service provider Ferrano Rail Cargo; consignor Serravona;
  the freight invoice 06 is addressed to Valdara.
- `AtLocation` `Serravona mine siding` names a place and fits the weighing service (`WEIGH`), which
  needs no movement.
- Framework contract `VI-FRC-FW-2026` is the same in 03; `TimezoneOffset` -1 fits 15°30.6′ W.
- Party descriptions identical in all eight ore examples; ISIN `XU0001042501` check digit correct.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:AdditionalTransportationService/cbc:TransportServiceCode` =
  `WEIGH`: suspected a service without a place — refuted because the AtLocation gives the place.
  (from broad)
- `/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` =
  `Wagons sheeted against dust.`: suspected implausible for lump ore — refuted because dust from ore
  wagons is a real concern and covering is common practice (own knowledge). (from broad)
- `/TransportExecutionPlanRequest/cac:Signature/cbc:ID` = `VI-SIG-TEPR`: suspected a signature
  without content — refuted because UBL requires only the ID; the signatory is the sender. (from
  broad)
- `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` =
  `FRC-TEP-26-0001` in a request: suspected a reference to a plan that does not exist yet — refuted
  because the status reason `UPDATE` explains that the request updates an existing standing plan.
  (from logistics; whether that plan should be an example is F10)
- `/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`: AtLocation in a
  request for a moving service — refuted because it is the place of the weighing service. (from
  context)
- `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Valdara Industries`:
  bill-to equal to the transport user — refuted because the element states who receives the invoice,
  and 06 is addressed to Valdara. (from context)
- `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonCode` = `UPDATE` with `NoStatus` — the
  context part refuted it (NoStatus is right for an original; UPDATE states why the request exists
  relative to the standing plan). The merge cannot settle it and keeps it as F5 with both arguments.
- `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
  against the monthly call-off — the context part refuted it (the standing plan may be weekly). The
  merge keeps it as F4 with both arguments.
- `FRC-TEP-26-0001` and `FRC-TSD-26` outside the flow — refuted by the context part for its lens,
  because both elements name their kind; kept as F10 (needs decision) on the logistics part's
  question.
- English renderings in Italian form, `+999` telephone numbers, ISO 6523 ICD `0990`, Ferrano Rail
  Cargo `SMALL`: refuted as in 01 (proper names keep their local form; E.164 999 is unassigned; 0990
  not in the ICD register by own knowledge, not checked; nothing states the operator's size). (from
  parties)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; all evidence quoted with values.
- broad/F2, context/F2, logistics/F3 → F2: combined; severity Medium (not logistics' Low), because
  section 6 names a transport request that does not say what is to be carried as Medium; free-text
  notes do not replace the consignment's goods.
- broad/F3, parties/F1, logistics/F2, context/F3 → F3: combined, all five places; Needs decision no
  (parties: yes), as in ore/01#F1.
- broad/F5, logistics/F4 → F4: Needs decision set to yes, because the context part's refutation is
  a possible reading the merge cannot exclude.
- broad/F4 → F5: Needs decision set to yes and options left without preference, because the context
  part's counter-argument is a legitimate reading of the definition.
- broad/F6, parties/F4, logistics/F6, context/F4 → F6: combined.
- broad/F7, parties/F2, context/F6 → F7: combined.
- broad/F8, parties/F3, context/F7 → F8: combined; security listing and road condition added from
  parties and context.
- broad/F9, logistics/F5, context/F5 → F9 (assay reference) and F10 (standing plan and service
  description): split, because the two parts of logistics/F5 need different decisions; F10 keeps
  logistics' "Needs decision: yes".

## Outside this review
- Whether 30 loaded ore wagons can be assembled at the mine siding and run within the window
  (capacity and timeline across documents) is for the consistency review. (from logistics)
