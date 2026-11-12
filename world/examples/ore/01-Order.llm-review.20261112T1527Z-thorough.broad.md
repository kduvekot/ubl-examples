# LLM review: 01-Order.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/01-Order.xml`, Git blob `af435c2882d01f0ca686e44a410c2da3f745d496` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### ore/01#F1 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located". A province is an administrative subdivision of the
  country, which UBL gives its own element, `CountrySubentity` ("The territorial division of a
  country, such as a county or state, expressed as text"). The same value is in Region in all 8
  examples of the flow; over all examples, 104 `*.xml` files carry a `<cbc:Region>Province of …`
  (219 occurrences, `grep -rh --include='*.xml' '<cbc:Region>Province of'`), while 213 files use
  `CountrySubentity`.
- Condition: no address of the example holds a province in `cbc:Region`; where the province is
  given, it is in `cbc:CountrySubentity` (optionally with `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, the element made for it, as the
  other examples do; (b) drop it, since postal zone and city identify the address.
- Needs decision: no

### ore/01#F2 · Low · "Monthly call-off" but typed as a plain order, with no blanket order referenced
- XPath: `/Order/cbc:OrderTypeCode` = `220`
- XPath: `/Order/cbc:Note[2]` = `Monthly call-off, one train.`
- Why: UN/EDIFACT 1001 has its own code for this, 226 "Call off order" (to provide split
  quantities and delivery dates of a blanket order); 220 is a stand-alone order. The note says the
  document is a call-off, but neither the type code nor a reference (`cac:Contract`,
  `cac:OriginatorDocumentReference` or `cac:AdditionalDocumentReference` to the frame agreement)
  says from which agreement it calls off (own knowledge of UNTDID 1001). The transport side has its
  frame agreement (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportContract/cbc:ID`
  = `VI-FRC-FW-2026`); the purchase side has none.
- Condition: the type code and the note agree: either the order is a call-off (type 226, or the note
  explains another reading) and refers to its blanket order or supply contract, or the note no
  longer calls it a call-off.
- Options: (a, preferred) keep the story of a monthly call-off, use 226 and add a reference to the
  supply agreement; (b) reword the note to a regular monthly order.
- Needs decision: yes (whether a supply agreement exists in the story)

### ore/01#F3 · Low · A furniture manufacturer buys a trainload of iron ore every month
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name[2]` = `Iron ore, lump`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `1800`
- Why: ISIC 3100 is "Manufacture of furniture". Iron ore (HS 260111, 62 % Fe lump) is raw material
  for a blast furnace or direct-reduction plant, not for a furniture factory, which buys steel tube,
  sheet or wire. 1 800 t of ore a month is a steelworks' input. The transport execution plan speaks of the
  factory starting "the blend" (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:BonusPaymentTerms/cbc:Note`
  = `2 % of the freight when the train is delivered on the first day of the window, so that the factory can start the blend a day early.`),
  which also points to a smelter. Valdara is classified 3100 in 112 `*.xml` files
  (`grep -rl --include='*.xml' 'ISIC Rev.4">3100<'`), so the party is a furniture maker throughout the world.
- Condition: the buyer of the ore is a party whose activity uses iron ore (or the story explains
  why Valdara does, e.g. its own foundry, and its classification shows it).
- Options: (a) give the ore flow a steel-making buyer; (b) give Valdara a second activity (a
  foundry or steel works) and the matching additional ISIC code; (c) change the goods to something a
  furniture maker buys by the train. Preference: (a) or (b), decided with the story of the flow.
- Needs decision: yes

### ore/01#F4 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact of the BuyerCustomerParty is the person or desk who buys; the buyer's order desk
  belongs to purchasing, not to sales, and a "customer service officer" serves the party's own
  customers. Name (`Order desk`), job title and department do not agree with each other or with the
  role. The same contact is used for Valdara in every role of the flow (75 `*.xml` files carry
  `order@valdara.example`).
- Condition: the buyer's contact is a purchasing contact (job title and department of purchasing).
- Options: (a, preferred) a purchasing desk for Valdara in the buyer role; (b) drop job title and
  department and keep the functional name.
- Needs decision: no

### ore/01#F5 · Low · Buyer's logistics service provider copied into the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics provides "Warehousing and despatch" to Valdara, but it has no part in this
  order: the ore is delivered FCA to the mine siding, carried by Ferrano Rail Cargo to the factory
  siding and unloaded by the consignee
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms`
  = `Delivery within the agreed slot; the consignee unloads.`). Data copied from master data into a
  document that does not use it (section 4.8). It is in all 8 examples of the flow and in 75
  `*.xml` files overall (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: the order carries a service provider only if that provider does something for this
  order.
- Options: (a, preferred) leave it out of the ore flow; (b) give Castrano a role in the story (e.g.
  stock-keeping of the ore at the factory) and say so.
- Needs decision: no

### ore/01#F6 · Low · Delivery location given only as text although it has an identifier
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Mine siding, Serravona`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cbc:ID` = `XUSRV`
- Why: the FCA place is the point where risk passes; the same place is identified as UN/LOCODE
  `XUSRV` ("The mine and its rail siding") in the seller's physical location. A free-text
  description alone leaves the named place of the Incoterm less precise than the data in the same
  document.
- Condition: the delivery location of the FCA term is identified the way the same place is
  identified elsewhere in the document (ID, or a name that is a place name).
- Options: (a, preferred) add `cbc:ID` `XUSRV` with schemeID `UN/LOCODE` to the delivery location;
  (b) leave it as is if text is deliberate.
- Needs decision: no

### ore/01#F7 · Low · World item number has the form of a valid GTIN-12 in the GS1 US range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: the value is 12 digits with a correct GS1 mod-10 check digit (computed over the first 11
  digits: check digit 3). As GTIN-13 it reads `0771010000013`, prefix 077, which lies in the
  GS1 US range (060–139; own knowledge). The schemeID `urn:ubl-examples:world:item` marks it as the
  world's own scheme, but a reader or a tool that sees 12 digits with a valid check digit can take
  it for a real UPC/GTIN-12, which the rule "fictional values must not be mistaken for real ones"
  excludes. The scheme is used in 64 `*.xml` files (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`).
  I could not check whether this GTIN is actually assigned.
- Condition: the item number cannot be mistaken for a real GTIN, or it is shown that the GS1
  register does not assign it and the scheme is documented as GTIN-shaped on purpose.
- Options: (a) a format that cannot be a GTIN (letters, or a length GS1 does not use); (b) keep it
  and record the check against GS1 in the sources. Preference: (a), it needs no register check.
- Needs decision: yes (the scheme is world-wide)

## Checked and consistent
- Arithmetic: 1 800 t × 8 060 XUF = 14 508 000 XUF (line and LineExtensionAmount); 20 % VAT on
  14 508 000 = 2 901 600; 14 508 000 + 2 901 600 = 17 409 600 = PayableAmount.
- `62 % Fe` in the description agrees with the property `Iron content` = 62 P1; HS 260111 and CPC
  14100 both mean non-agglomerated iron ore; lump size and "loose in rail wagons" agree with the
  later documents (`04-DespatchAdvice.xml`, `07-Invoice.xml`).
- FCA with the buyer naming the carrier (Ferrano Rail Cargo) agrees with the buyer requesting the
  transport (`02-TransportExecutionPlanRequest.xml`, sender Valdara) and paying the freight
  (`06-Invoice.xml`).
- Requested delivery period 9–13 March agrees with the requested service period
  (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate`
  = `2026-03-10`) and the despatch on 10 March (`04-DespatchAdvice.xml`).
- The three parties (Valdara, Serravona, Ferrano Rail Cargo) are described with identical content
  (identifiers, addresses, tax schemes, legal entities, contacts) in every example of the flow
  (compared element by element).
- `check_ids.py`: ISIN `XU0001042501` OK.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `FCA`: suspected missing Incoterms version in schemeID — refuted
  because the schemeID style is a repository-wide convention ("schemeIDs keep their current style")
  and nothing in the flow is ambiguous between versions.
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`:
  suspected the seller should not name the carrier under FCA — refuted because the order is the
  buyer's document and under FCA the buyer nominates the carrier, which it does.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` =
  `XU0001042501`: suspected master data copied into the order — refuted because it describes the
  party as a legal entity (listed company) rather than adding a party that does nothing; it is
  party description, not transaction data.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeDirectionCode`
  = `South`: suspected implausible coordinates — refuted because the world is fictional and the
  values are consistent across the flow.
- `/Order/cbc:AccountingCostCode` = `3100`: suspected the ISIC code copied into the buyer's
  accounting code — refuted because it is the buyer's own cost code with a matching text
  (`Raw materials and parts`), and it is used consistently in the invoices of the flow.
