# LLM review: 03-TransportExecutionPlan.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/03-TransportExecutionPlan.xml`, Git blob `b9cd241a833ef55a0d6d59ac19ae0579457b6de6` (committed)
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

### ore/03#F1 · Medium · Province in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlan/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located" and Address/CountrySubentity as "The territorial
  division of a country, such as a county or state, expressed as text". "Province of Ferrano" names a
  territorial division of Urvania, which is what CountrySubentity is for. Bayvarran addresses in
  the world put their states in CountrySubentity (`Coastal State`, `Upland State` and others in 214
  examples), so the first-level divisions of the two countries are encoded in different elements.
  The value occurs 219 times in 104 examples, always in Region (`grep -c
  '<cbc:Region>Province of'` over `world/examples/*/*.xml`, files with a count above 0).
- Condition: the province of every Urvanian address in this example is in `cbc:CountrySubentity`
  (optionally with `cbc:CountrySubentityCode`) and not in `cbc:Region`, or the world states that
  Urvanian provinces are not territorial divisions and Region is used on purpose.
- Options: (a) preferred: move the province to CountrySubentity for all Urvanian addresses, as for
  Bayvarra, because it fits the definition and makes the two countries consistent; (b) keep Region
  and record in the world why an Urvanian province is a region and not a subdivision.
- Needs decision: yes (it changes the Urvanian address format in every flow and may be deliberate)

### ore/03#F2 · Low · Contact does not fit the party's role in this document
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- Why: Contact is "The primary contact for this party", and the checklist asks whether it fits the
  role the party plays in this document. Valdara Industries receives the plan as transport user and must accept it by `TransportUserResponseRequiredPeriod`; the contact for that is its transport planning, not its sales order desk. Serravona Mining is the consignor whose siding the train collects from; its sales office is not the contact for loading. Every party carries one and the same contact in all
  roles: Valdara Industries' 'Order desk' / 'Customer service officer' / 'Sales' is in 75 examples
  (`grep -rl 'order@valdara.example'` over `*.xml`), Serravona Mining's 'Sales office' in 7 and
  Ferrano Rail Cargo's 'Freight desk' in 15.
- Condition: the receiver's Contact belongs to the function that books and accepts transport, and the consignor's Contact to the function that loads the train (or each is left out).
- Options: (a) preferred: give the party a contact per function (purchasing, logistics, goods-in,
  accounts payable or receivable) and use the one that fits the role here; (b) leave the Contact
  out where the party has no contact for this role, so that no wrong department is implied.
- Needs decision: no

### ore/03#F3 · Low · Party master data the document does nothing with
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlan/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: Valdara Industries is described with a `cac:ServiceProviderParty` (Castrano Logistics, 'Warehousing and despatch') and a `cac:SecurityListing` (its shares on the Ferrano Stock Exchange). Castrano Logistics plays no role in this flow: in all eight ore examples it appears only inside Valdara's party, and the listing of Valdara's shares is not used by a transport execution plan. Both occur in 75 examples (`grep -rl 'Castrano Logistics'` and `grep -rl 'XU0001042501'` over `*.xml`). Serravona Mining's `PhysicalLocation/cbc:Conditions` describes road access ('Unpaved access road; heavy vehicles only.'), but the ore leaves the mine by train from its own siding, so road access matters to no party of this document (7 examples, all in this flow). Section 4.8 of the review rules and IND5 (no fillers): data copied from a party's
  master data into a document that does not use it.
- Condition: these elements are present only where a transport execution plan uses them, or the document says why it
  carries them.
- Options: (a) preferred: leave them out of this document and keep them for documents that need
  them (a qualification, a contract, a road delivery); (b) give them a role in the story (for
  instance Castrano Logistics handling goods-in at Valdara) and show it in the flow.
- Needs decision: no

### ore/03#F4 · Low · Location named after a company, not the place
- XPath: `/TransportExecutionPlan/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlan/cac:ToLocation/cbc:Name` = `Valdara Industries`
- XPath: `/TransportExecutionPlan/cac:TransportExecutionTerms/cac:NotificationRequirement/cac:NotificationLocation/cbc:Name` = `Valdara Industries`
- Why: Location/Name is "The name of this location", and the checklist asks that the name be the
  place, not the company. Origin, destination and notification location are named after companies. The origin carries Serravona's postal business address although the train is loaded at the siding identified as `/TransportExecutionPlan/cac:Consignment/cac:ConsignorParty/cac:PhysicalLocation/cbc:ID` = `XUSRV`.
- Condition: FromLocation, ToLocation and NotificationLocation name places, and the origin carries the identifier the flow uses for the siding.
- Options: (a) preferred: name the place ('Serravona mine siding', 'Valdara works, Ferrano') and add
  the UN/LOCODE `XUSRV` where the place is the mine siding; (b) leave the name out where the address
  or identifier already says where it is.
- Needs decision: no

### ore/03#F5 · Low · AtLocation is the carrier, not a place, and differs from the request
- XPath: `/TransportExecutionPlan/cac:AtLocation/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`
- Why: AtLocation is "The location of a transport service (e.g., terminal handling service) that does
  not require transport movement". The plan gives the carrier's company name, which is not a place,
  while the request it answers named the mine siding. The plan is `Confirmed` with reason
  `ASREQUESTED`, so a changed place is not explained either.
- Condition: AtLocation names the place where the stationary service of this plan is performed and
  agrees with the request unless the plan says why it differs, or it is absent if the plan has no such
  service.
- Options: (a) preferred: 'Serravona mine siding' as in the request, because the plan confirms the
  request as asked; (b) leave AtLocation out if the plan's additional service needs no place.
- Needs decision: no

## Checked and consistent
- Every party is described identically in all eight ore examples: compared by PartyIdentification/ID, Valdara Industries (XU-R-104274) has one full form (13 child elements) and one short form (identification and name), and so do Serravona Mining (XU-R-104137), Ferrano Rail Cargo (XU-R-104685) and Castrano Logistics (XU-R-104411); no address, tax, legal or contact detail differs between examples.
- For each full party `PartyIdentification/cbc:ID` = `PartyLegalEntity/cbc:CompanyID`, the `ElectronicAddressID` is 'XU:' plus that ID, and `PartyTaxScheme/cbc:RegistrationName` = `PartyLegalEntity/cbc:RegistrationName`; legal form, size and liquidation status fit companies (SUA with share capital and listing, SRU without).
- Roles: Ferrano Rail Cargo is sender, transport service provider and signatory; Valdara Industries receiver, transport user, bill-to party, notify party and consignee; Serravona Mining consignor. They match `02-TransportExecutionPlanRequest.xml` (sender and receiver swapped, as for an answer).
- `NotifyParty` Valdara Industries is the consignee, the right party for a pre-arrival notice.
- `check_ids.py`: the ISIN `XU0001042501` of Valdara's SecurityListing has a correct check digit.

## Considered and refuted
- the English renderings in Italian form (`StreetName` 'Via delle Officine', 'Strada della Miniera', `CompanyLegalForm` 'Società urvaniana per azioni (public limited company)', all with `languageID` `en-XU`): suspected to be in another language than the tag says — refuted because these are proper names, which English text keeps in their local form (as with 'Via del Corso'); the legal form adds an English gloss in brackets.
- telephone numbers starting with `+999`: suspected to be real numbers — refuted because ITU-T E.164 keeps country code 999 reserved and unassigned, so they cannot reach a real subscriber (own knowledge).
- Valdara's `AdditionalPartyIdentification` `0990:10427` with schemeID `ISO 6523`: suspected to use a real ICD — refuted on my knowledge of the ISO 6523 ICD register, where 0990 is not assigned; not checked against the register itself.
- Ferrano Rail Cargo's `EntitySizeCode` `SMALL`: suspected too small for a rail freight operator running 30-wagon ore trains — refuted because nothing in the flow states staff or turnover, and small rail operators with hired traction exist.
