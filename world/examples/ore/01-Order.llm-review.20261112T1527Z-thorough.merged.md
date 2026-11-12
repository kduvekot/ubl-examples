# LLM review: 01-Order.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/01-Order.xml`, Git blob `af435c2882d01f0ca686e44a410c2da3f745d496` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### ore/01#F1 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located". A province is an administrative subdivision of the
  country, for which UBL has `CountrySubentity` ("The territorial division of a country, such as a
  county or state, expressed as text"). The world encodes Bayvarra's first-level divisions
  (`Coastal State`, `Upland State`) in CountrySubentity, but Urvania's provinces in Region, so the
  two countries differ in encoding for the same kind of division. The parts counted the pattern
  over `*.xml`: `<cbc:Region>Province of` occurs 219 times in 104 files
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`); the value is in Region in all 8 examples
  of the flow.
- Condition: no address of the example holds a province in `cbc:Region`; where the province is
  given, it is in `cbc:CountrySubentity` (optionally with `cbc:CountrySubentityCode`), or the world
  states why an Urvanian province is a region and not a subdivision.
- Options: (a, preferred) move the value to `CountrySubentity` for all Urvanian addresses, as for
  Bayvarra, because it fits the definition and makes the two countries consistent; (b) keep Region
  and record in the world why it is a region; (c) drop it, since postal zone and city identify the
  address.
- Needs decision: no (an encoding change; the parties part asked for a decision because it may be
  deliberate, see "Changed in the merge")
- From: broad (F1), parties (F1), context (F1)

### ore/01#F2 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party"; the contact of the BuyerCustomerParty in an
  order is the person or desk that buys and answers the seller's questions about the purchase
  (purchasing). Valdara's contact is the order intake desk of its own Sales department, the one its
  customers use when they buy benches; the seller's contact has the same job title and department
  (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`). Every party
  carries one and the same contact in all roles: Valdara's `order@valdara.example` is in 75 `*.xml`
  files (`grep -rl --include='*.xml' 'order@valdara.example'`).
- Condition: the buyer's contact in this Order is a purchasing function of Valdara (name, job title
  and department agreeing with each other and with the buyer role), or there is none.
- Options: (a, preferred) give the party a contact per function (purchasing, logistics, goods-in,
  accounts payable) and use the purchasing one here; (b) drop the contact, or job title and
  department, where the world has no purchasing contact.
- Needs decision: no
- From: broad (F4), parties (F2), context (F2)

### ore/01#F3 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: section 4.8 and IND5 (no fillers): data copied from a party's master data into a document
  that does not use it. Castrano Logistics provides "Warehousing and despatch" to Valdara, but has
  no part in this order: the ore is delivered FCA at the mine siding, carried by Ferrano Rail Cargo
  and unloaded by the consignee
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms`
  = `Delivery within the agreed slot; the consignee unloads.`); in all eight ore examples it occurs
  only inside Valdara's party. The listing of Valdara's shares on the Ferrano Stock Exchange has
  no use in an order for ore. Serravona's road-access condition concerns road vehicles, but the ore
  leaves by train from the mine's own siding. Service provider `VI-SP-2026-01` and ISIN
  `XU0001042501` each occur in 75 `*.xml` files (`grep -rl --include='*.xml'`); the road condition
  in 7, all of this flow.
- Condition: every aggregate of the parties has a use in this Order; the service provider, the
  security listing and the road-access condition are present only where a document of the flow
  does something with them, or the document says why it carries them.
- Options: (a, preferred) leave them out of the order and keep them for documents that need them (a
  qualification, a contract, a road delivery); (b) give Castrano a role in the story (e.g.
  goods-in or stock-keeping of the ore at Valdara) and show it in the flow.
- Needs decision: no
- From: broad (F5: service provider), parties (F3: all three), context (F3: service provider and
  security listing)

### ore/01#F4 · Low · "Monthly call-off" typed as a plain order, without the agreement it calls off
- XPath: `/Order/cbc:OrderTypeCode` = `220`
- XPath: `/Order/cbc:Note[2]` = `Monthly call-off, one train.`
- Why: UNTDID 1001 (the list the code's listID names) has its own code 226 "Call off order" (to
  provide split quantities and delivery dates of a blanket order); 220 is a plain order (own
  knowledge of UNTDID 1001). The note calls the document a call-off, but neither the type code nor a
  reference (`cac:Contract`, `cac:OriginatorDocumentReference`, `cac:AdditionalDocumentReference`)
  says from which agreement it calls off. The transport side has its frame agreement
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportContract/cbc:ID` =
  `VI-FRC-FW-2026`); the purchase side has none. The code and the free text next to it disagree.
- Condition: the type code and the note agree: either the order is a call-off (type 226, or the
  note explains another reading) and refers to its blanket order or supply contract, or the note no
  longer calls it a call-off.
- Options: (a, preferred) keep the story of a monthly call-off, use 226 and add a reference to the
  supply agreement; (b) reword the note to a regular monthly order.
- Needs decision: yes (whether a supply agreement exists in the story)
- From: broad (F2); context listed the missing reference under "Considered and refuted" (see
  there, and "Changed in the merge")

### ore/01#F5 · Low · Delivery location of the Incoterm given only as text, though it has an identifier
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Mine siding, Serravona`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cbc:ID` = `XUSRV`
- Why: the FCA place is the point where delivery and risk pass; the same place is identified as
  UN/LOCODE `XUSRV` ("The mine and its rail siding") in the seller's physical location. A
  description alone leaves the named place of the Incoterm less precise than the data in the same
  document.
- Condition: the delivery location of the FCA term is identified the way the same place is
  identified elsewhere in the document (ID, or a name that is a place name).
- Options: (a, preferred) add `cbc:ID` `XUSRV` with schemeID `UN/LOCODE` to the delivery location;
  (b) leave it as is if the text is deliberate.
- Needs decision: no
- From: broad (F6)

### ore/01#F6 · Low · World item number is a valid GTIN-12 in the GS1 US prefix range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: StandardItemIdentification is "identifying information for this item, assigned according to
  a standard system"; the schemeID `urn:ubl-examples:world:item` marks the world's own scheme. The
  value has twelve digits and a correct GS1 mod-10 check digit (recomputed in the merge over
  `77101000001`: 3). As GTIN-13 it reads `0771010000013`, prefix 077, in the GS1 US range (own
  knowledge). A reader or a tool that sees the number without its schemeID can take it for a real
  UPC/GTIN-12, which the rule "fictional values must not be mistaken for real ones" excludes. The
  scheme is used in 64 `*.xml` files
  (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`). Whether this GTIN is
  actually assigned could not be checked (no register lookup).
- Condition: the item number cannot be read as a valid GTIN in a real GS1 prefix range, or a
  recorded decision states (with a check against GS1) why the GTIN-shaped form is safe.
- Options: (a, preferred) change the length or check-digit rule of the world's item scheme so the
  numbers are not valid GTINs; it needs no register check; (b) keep it and record the decision and
  the GS1 check in the sources.
- Needs decision: yes (the scheme is world-wide)
- From: broad (F7), logistics (F1)

## Checked and consistent
- Arithmetic (re-done in the merge): 1 800 TNE × 8 060 XUF per 1 TNE = 14 508 000 XUF (line
  LineExtensionAmount, AnticipatedMonetaryTotal/LineExtensionAmount, TaxableAmount); 20 % of
  14 508 000 = 2 901 600 = TaxAmount; 14 508 000 + 2 901 600 = 17 409 600 = PayableAmount.
- The price per tonne is the one the seller invoices
  (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `8060`); category S at 20 %
  is applied in both invoices of the flow.
- FCA at the mine siding: the buyer names the carrier (Ferrano Rail Cargo), requests the transport
  (02, sender Valdara) and pays the freight (06, bill-to Valdara in 02/03).
- Requested delivery period 2026-03-09 to 2026-03-13 contains the transport window of 02/03
  (2026-03-10 to 2026-03-13) and the despatch on 2026-03-10 (04).
- Physics (logistics): 1 800 t as "one train" = 30 wagons × 60 t (04). 60 t of lump ore at a bulk
  density of about 2.3–2.8 t/m³ (own knowledge) is 21–26 m³, inside an open ore wagon of about
  40–75 m³; with a tare of about 22–25 t, 82–85 t per four-axle wagon, 20.5–21.3 t per axle, under
  the usual 22.5 t limit.
- `62 % Fe` in the description agrees with the property `Iron content` = 62 P1; HS 260111 and CPC
  14100 both mean non-agglomerated iron ore; item identifiers, names, classification and iron
  content are identical in 04 and 07.
- The parties (Valdara Industries XU-R-104274, Serravona Mining XU-R-104137, Ferrano Rail Cargo
  XU-R-104685, Castrano Logistics XU-R-104411) are described identically in all eight ore examples;
  PartyIdentification = CompanyID, ElectronicAddressID = 'XU:' + ID, tax and legal registration names
  agree; legal forms, sizes and liquidation statuses fit companies.
- Codes: OrderTypeCode 220, ISIC 0710 (iron ore mining) for Serravona, 4912 (freight rail) for
  Ferrano Rail Cargo; `TimezoneOffset` -1 fits the solar offset at 15.5° W.
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `FCA`: suspected missing Incoterms version in schemeID —
  refuted because the schemeID style is a repository-wide convention ("schemeIDs keep their current
  style") and nothing in the flow is ambiguous between versions. (from broad)
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`:
  suspected the seller should not name the carrier under FCA — refuted because the order is the
  buyer's document and under FCA the buyer nominates the carrier. (from broad)
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty`: suspected the buyer names a carrier it has not
  yet booked (the request is issued a day later) — refuted because the delivery term is FCA and the
  framework contract `VI-FRC-FW-2026` exists, so Valdara knows its carrier when ordering. (from
  parties)
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeDirectionCode`
  = `South`: suspected implausible coordinates, or coordinates of a real place — refuted because the
  world is fictional, the values are consistent across the flow, and 39° 54.00′ S, 15° 30.60′ W lies
  in the open South Atlantic, so it cannot be taken for a real mine. (from broad, parties)
- `/Order/cbc:AccountingCostCode` = `3100`: suspected the ISIC code copied into the buyer's
  accounting code — refuted because the pair `3100` / `Raw materials and parts` is Valdara's own
  cost centre, used in all 12 `*.xml` files that carry it, all Valdara documents
  (`grep -rl --include='*.xml' '<cbc:AccountingCostCode>3100'`), and raw materials is the right cost
  centre for ore. (from broad, money, context)
- `/Order/cac:AnticipatedMonetaryTotal`: no TaxExclusiveAmount/TaxInclusiveAmount — refuted: both are
  optional and the given amounts state the anticipated total completely for a one-line order
  without allowances. (from money)
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` =
  `250000000`: suspected master data without use — refuted because stating the share capital on
  commercial documents is a legal requirement in several real jurisdictions (e.g. Italy, on which
  the Urvanian legal forms are modelled; own knowledge). (from context)
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` =
  `260111`: an HS code in a domestic order — refuted because the HS also serves statistics and
  national purposes. (from context)
- English renderings in Italian form (`StreetName` `Via delle Officine`, `Strada della Miniera`,
  `CompanyLegalForm` with an English gloss, all `en-XU`): suspected to be in another language than
  the tag says — refuted because these are proper names, which English text keeps in their local
  form. (from parties)
- Telephone numbers starting with `+999`: refuted because ITU-T E.164 keeps country code 999
  reserved and unassigned (own knowledge). (from parties)
- `AdditionalPartyIdentification` `0990:10427` with schemeID `ISO 6523`: suspected a real ICD —
  refuted on knowledge of the ICD register, where 0990 is not assigned; not checked against the
  register itself. (from parties)
- Ferrano Rail Cargo's `EntitySizeCode` `SMALL`: suspected too small for 30-wagon ore trains —
  refuted because nothing in the flow states staff or turnover, and small operators with hired
  traction exist. (from parties)
- `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-09`: suspected a clash
  with FCA and the transport starting on 2026-03-10 — refuted because the period is a window and the
  hand-over on 2026-03-10 lies inside it. (from logistics)
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries` without a
  delivery location: suspected missing place — refuted because under FCA the contracted place is in
  `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Mine siding, Serravona`. (from
  logistics)
- `/Order/cbc:Note[2]` = `Monthly call-off, one train.`: a call-off without a reference to the
  framework purchase agreement — the context part refuted this because a missing optional reference
  is not a finding. The merge disagrees for the combination of note and type code and keeps it as
  F4 (see "Changed in the merge"); the context part's argument stays recorded here.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` =
  `XU0001042501`: the broad part refuted "master data copied into the order" because it describes
  the party as a legal entity (a listed company). The merge disagrees, with parties and context, and
  keeps it in F3: nothing in an order for ore uses the share listing.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`:
  the context part refuted "road access in a rail delivery" because the PhysicalLocation is the FCA
  place the buyer's carrier has to reach. The merge disagrees, with parties, and keeps it in F3:
  the carrier is a railway collecting at the mine's own siding, so a road-access condition informs
  no party of this order.

## Refuted in the merge
### broad/F3 · Low · A furniture manufacturer buys a trainload of iron ore every month
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name[2]` = `Iron ore, lump`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800`
- Why (broad): ISIC 3100 is "Manufacture of furniture"; iron ore is raw material for a blast furnace
  or direct-reduction plant, and 1 800 t a month is a steelworks' input. The plan's bonus note speaks
  of the factory starting "the blend"
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note`
  = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`).
  Valdara is classified 3100 in 112 `*.xml` files.
- Condition (broad): the buyer of the ore is a party whose activity uses iron ore, or the story
  explains why Valdara does and its classification shows it.
- Options (broad): a steel-making buyer; a second ISIC code for Valdara; other goods. Needs decision: yes.
- Refuted because: the world gives Valdara its own steel making. Its bench orders state the
  emission scope `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description`
  = `Mining, steel making, casting, galvanising, sawing and the transport between them.` and the
  source `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:EmissionFactorSource`
  = `The steelworks' and sawmill's measured energy use of 2025` (the same in
  `road/01-Order.xml`). A furniture maker with its own steelworks and foundry buys ore; ISIC 3100
  names its main activity, as an IndustryClassificationCode should. A second code (2410) would make
  the steelworks visible but is not required. The parties and context parts refuted it on the same
  grounds.

## Changed in the merge
- broad/F1, parties/F1, context/F1 → F1: combined; Needs decision set to no (broad, context) rather
  than yes (parties), because moving the value to the element made for it changes the encoding, not
  the story; option (b) of parties (record why it is a region) is kept as an option.
- broad/F4, parties/F2, context/F2 → F2: combined, all three XPaths.
- broad/F5, parties/F3, context/F3 → F3: combined into one master-data finding. The security
  listing (refuted by broad) and the road-access condition (refuted by context) are kept in it,
  because the merge disagrees with those refutations (see "Considered and refuted").
- broad/F2 → F4: kept against the context part's refutation, because the finding is not only a
  missing optional reference but a type code that disagrees with the note next to it; wording
  sharpened accordingly.
- broad/F6 → F5: unchanged.
- broad/F7, logistics/F1 → F6: combined; check digit recomputed in the merge (3).
