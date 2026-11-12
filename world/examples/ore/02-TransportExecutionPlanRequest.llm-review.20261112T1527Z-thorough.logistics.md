# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### ore/02#F1 · High · Container train requested for ore carried loose in wagons
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `RAILCONT`
- XPath: `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:Name` = `Container train`
- Why: `RAILCONT` means "Containers on a scheduled container train" (world list
  TransportServiceCode). The goods are "loose in rail wagons"
  (`01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Non-agglomerated iron ore, lump size 10–30 mm, 62 % Fe, loose in rail wagons.`),
  the request asks for wagons to be sheeted
  (`/TransportExecutionPlanRequest/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Wagons sheeted against dust.`),
  the despatch line counts 30 wagons
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`),
  and the carrier invoices "Rail freight, ore in bulk wagons"
  (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Rail freight, ore in bulk wagons`).
  No container appears anywhere in the flow. The same list has `RAILWAGON` ("A whole wagon for one
  consignment"), which is closer to a block train of wagons for one consignment.
- Condition: the main transportation service code and name describe carriage of bulk ore in wagons,
  and agree with 03-TransportExecutionPlan.xml and 06-Invoice.xml.
- Options: (a, preferred) `RAILWAGON` with a matching name; (b) add a code for a whole (block) train
  to the world list if "wagon load" is felt too narrow for a 30-wagon train.
- Needs decision: no

### ore/02#F2 · Medium · Province given in Region in the transport locations
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries in which
  this address is located"; a province is a country subdivision, for which UBL has
  `CountrySubentity`. The same use of `Region` for a province occurs 219 times in 104 examples
  (count of `cbc:Region` values containing "Province" over `*/*.xml` with lxml), so it is likely a
  general convention; it stays a finding here.
- Condition: the province is in `CountrySubentity` (or `Region` holds a real region or group of
  countries).
- Options: (a, preferred) move it to `CountrySubentity` everywhere, since the problem is general;
  (b) record a decision if `Region` was chosen on purpose.
- Needs decision: no

### ore/02#F3 · Low · What is to be carried is only in the notes
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`
- XPath: `/TransportExecutionPlanRequest/cbc:Note[2]` = `The ore train from the mine siding to the factory.`
- Why: a transport execution plan request is "sent by a transport user to request a transport
  service"; the carrier needs to know what it is to carry and in what equipment. The consignment
  carries only its gross weight: no goods item, description, commodity code or number and type of
  wagons. That the goods are ore comes only from the free-text note and the status reason. Not
  Medium, because the notes do say "ore" and the weight is given.
- Condition: the consignment says what the goods are (e.g. a goods item with description and HS
  code, or a consignment description) and, if the request concerns the wagons, how many are needed.
- Options: (a, preferred) a `GoodsItem` with the ore description and `260111`; optionally the
  number of wagons as `TransportHandlingUnit`/equipment requirement; (b) at least
  `Consignment/cbc:Information` describing the goods.
- Needs decision: no

### ore/02#F4 · Low · Weekly quantity in the request, monthly call-off in the order
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusReasonDescription` = `This week's quantity of ore differs from the standing plan.`
- XPath: `01-Order.xml:/Order/cbc:Note[2]` = `Monthly call-off, one train.`
- Why: the order presents the train as a monthly call-off, the request as this week's quantity.
  Both can be true only if the standing plan is weekly and the call-off monthly, which neither
  document says.
- Condition: both documents describe the same rhythm (weekly or monthly) of the ore train.
- Options: (a, preferred) align the request's reason text with the order ("this month's"); (b) make
  the order's note say how the monthly call-off relates to the weekly standing plan.
- Needs decision: no

### ore/02#F5 · Low · References with only an ID to documents that are not among the examples
- XPath: `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
- XPath: `/TransportExecutionPlanRequest/cac:TransportServiceDescriptionDocumentReference/cbc:ID` = `FRC-TSD-26`
- XPath: `/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID` = `SM-ASSAY-26-11`
- Why: none of the three resolves to an example of the flow (`flow_index.py ore`: `-> ?`). The
  first two are named by their element (original/standing plan, service description); the
  additional reference is not: it carries no `DocumentTypeCode` or `DocumentType`, and the reader
  has to guess from the prefix that it is the mine's assay certificate, and why a transport request
  needs it. ID-only references are common in the examples (555 of 595 `*DocumentReference`
  aggregates in 177 examples have only `cbc:ID`, counted with lxml over `*/*.xml`).
- Condition: the additional reference says what kind of document it is (type code or text), and
  each referenced document either exists in the world as intended or the decision that it needs no
  example is recorded.
- Options: (a, preferred) add `DocumentTypeCode`/`DocumentType` to the additional reference;
  (b) drop the assay reference if the transport request does nothing with it.
- Needs decision: yes (whether the standing plan and the service description should exist as
  examples)

### ore/02#F6 · Low · Location names are party names
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Serravona Mining`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: a location's name should name the place. The loading place is the mine siding
  (`/TransportExecutionPlanRequest/cac:AtLocation/cbc:Name` = `Serravona mine siding`) and the place
  of delivery the factory siding (06-Invoice.xml line description "to the factory siding"); the
  from/to locations instead carry the company names and their business addresses
  (`AddressTypeCode` `BUSINESS`). The same pattern (a `*Location/cbc:Name` equal to a party name in
  the same document) occurs at 46 places in 25 examples (lxml over `*/*.xml`).
- Condition: from and to locations name the sidings (and, where available, carry their location
  identifier such as `XUSRV`).
- Options: (a, preferred) "Serravona mine siding" / "Valdara factory siding", with `cbc:ID` UN/LOCODE
  where known; (b) keep the company names but add the siding as `SubsidiaryLocation`.
- Needs decision: no

## Checked and consistent
- Physics: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000` kg
  equals the ordered 1800 t (01-Order.xml) and 30 wagons × 60 t (04-DespatchAdvice.xml). For loose
  ore there is no packaging, so the consignment gross weight (which excludes the carrier's
  equipment) equals the net weight; correct as a planned figure (actual: 1788.4 t in
  04-DespatchAdvice.xml).
- Consignment ID `VI-CS-26-0306` is the same in 03, 04 and 05; consignor, consignee and carrier agree
  with 03 and 05.
- Dates: issued 2026-03-03 09:24; response deadline 2026-03-04, met by 03-TransportExecutionPlan.xml
  (issued 2026-03-04 12:50); service 2026-03-10 to 2026-03-13 inside the order's requested period
  2026-03-09 to 2026-03-13.
- `AtLocation` `Serravona mine siding` fits the additional weighing service (`WEIGH`), which needs no
  movement.
- `TimezoneOffset` `-1` at both addresses fits the mine's longitude 15°30.6′ W.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0001`
  in a request: suspected a reference to a plan that does not exist yet — refuted because the
  status reason `UPDATE` ("Update of a standing plan") explains that the request updates an existing
  standing plan.

## Outside this review
- Whether 30 loaded ore wagons can be assembled at the mine siding and run within the window
  (capacity and timeline across documents) is for the consistency review.
