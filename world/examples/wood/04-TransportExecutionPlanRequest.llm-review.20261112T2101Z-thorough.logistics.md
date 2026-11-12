# LLM review: 04-TransportExecutionPlanRequest.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/04-TransportExecutionPlanRequest.xml`, Git blob `291e2fcd1c4b728be274ce60b1b1117f4ce1b87d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### wood/04#F1 · High · Transport window ends before the delivery window the seller promised
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-02-26`
- XPath: `/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-03-01`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-02-27`
- Why: ServiceEndTimePeriod is "The period during which the services referred to in the Transport Execution Plan Request must be completed". The seller asks the haulier to complete the DAP transport to `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries` by 1 March, but the buyer requested, and the seller promised, delivery between 2 and 16 March. The goods are then cleared for import on 27 February, so in the flow as written they arrive at least three days before the window opens. No document of the flow records that the buyer agreed to an earlier delivery (the order states no period; see the review of `03-Order.xml`, this run). Either the transport request or the agreed window is wrong.
- Condition: the transport service window lies within (or is explicitly agreed to replace) the delivery window that the request for quotation, the quotation and the order establish.
- Options: (a) move the delivery window of the request for quotation and the quotation to the dates of the transport (e.g. 26 February – 6 March), which keeps the documents from despatch onwards unchanged; (b) preferred if the story wants the March window: move the transport window and the dates of despatch, export, import and invoice into it; (c) keep both and add an order with a requested period that explains the earlier delivery. (a) changes fewest documents.
- Needs decision: yes

### wood/04#F2 · Medium · Destination province in `Region`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country", which UBL puts in `CountrySubentity` (and its code in `CountrySubentityCode`), as the Bayvarran addresses of the same document do (`/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CountrySubentity` = `Upland State`). The same value appears in the party addresses of this example (parties lens) and 219 times in 104 examples (counted with `grep -rh --include='*.xml' -o '<cbc:Region>[^<]*' world/examples | sort | uniq -c`), so it is a systematic choice for Urvanian addresses.
- Condition: no Urvanian province is carried in `cbc:Region` of this location's address; it is in `cbc:CountrySubentity` (with a code where the world has one).
- Options: (a) preferred: move the province to `CountrySubentity` (and `CountrySubentityCode`) in the Urvanian address format, everywhere; (b) if "Province of Ferrano" is in fact a non-administrative region in the world's story, say so and keep it, but then the address has no subdivision at all.
- Needs decision: no

### wood/04#F3 · Low · Goods to be carried only in a free-text note
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The slats across the border to the bench factory.`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- Why: the consignment carries only its ID, gross weight and the parties. What is carried (4800 planed hardwood slats, 1.8 m long, in 96 bundles of 50 on heat-treated pallets, per `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.` and `03-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`) appears only as "the slats" in the note. For a full truck load the weight is the decisive figure and it is given, so the request can be served; but the number of handling units, their length and the goods description are what the haulier plans loading with, and the request is the document that should carry them.
- Condition: the consignment says, in structured form, what is carried: at least a goods description and the number and kind of handling units or packages.
- Options: (a) preferred: add a `GoodsItem` (description, quantity, gross weight) and a `TransportHandlingUnit` or `ChildConsignment`/`Package` count for the 96 bundles; (b) at least `Consignment/cbc:TotalTransportHandlingUnitQuantity` and a goods description.
- Needs decision: no

### wood/04#F4 · Low · From and to locations are named after the companies
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: Location/Name is "The name of this location". The names are the parties' names; the place where the goods are to be delivered is called `Valdara Industries, goods-in, Ferrano` in the request for quotation and the order (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`). The same DAP place is thus named differently in the transport request than in the commercial documents.
- Condition: the locations are named as places (e.g. the yard of the sawmill, the goods-in of the works), and the destination is named as in the commercial documents of the flow.
- Options: (a) preferred: use the place names already used in the flow (`Valdara Industries, goods-in, Ferrano`) and a matching one for the sawmill yard; (b) add identifiers to the locations.
- Needs decision: no

## Checked and consistent
- Dates: `/TransportExecutionPlanRequest/cbc:IssueDate` = `2026-02-23` at `16:19:00`; response deadline `/TransportExecutionPlanRequest/cac:TransportServiceProviderResponseDeadlinePeriod/cbc:EndDate` = `2026-02-24` is after issue; the service starts on 2026-02-26, the day of the despatch advice, the export declaration and the invoice.
- Parties against Incoterm: DAP (`03-Order.xml`) puts carriage on the seller; here the seller is transport user and bill-to party, and the haulier `Trasvia Haulage` is the carrier named in `05-ExportCustomsDeclaration.xml` and `06-DespatchAdvice.xml` (same register ID `XU-R-104822`, same haulage licence `XU-HAUL-2020-0877`, valid to 2030-06-30).
- Consignment `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `MS-CS-26-0629` is the consignment of `05-ExportCustomsDeclaration.xml` and `06-DespatchAdvice.xml`, with the same gross weight 21 600 kg in all three.
- Physics (calculated): 4800 slats × (1.800 × 0.095 × 0.038 m = 0.006498 m³) = 31.19 m³; 21 600 kg / 31.19 m³ = 692 kg/m³ including packaging, inside 650–750 kg/m³ for kiln-dried hardwood at 12 % moisture (own knowledge). If the bundles stand on 30–50 pallets of about 25 kg, the net timber is about 20.4–20.9 t, about 655–670 kg/m³, still plausible (ash, birch, maple). 21.6 t and 31 m³ fit one truck (own knowledge: about 24 t payload, about 90 m³), consistent with `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL` and with the quotation's "minimum one truck".
- Codes: `FTL`, `NoStatus`, `BUSINESS`, `XB`/`XU` formats all resolved in their lists.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address`: suspected a postal address copied into a location (no address register ID, unlike the party's) — refuted because the location address is the same street address as the party's, which is where the goods are loaded, and an identifier is optional.

## Outside this review
- Timeline across documents: despatch on 2026-02-26 in Marrowdale (Upland State, Bayvarra) and import clearance on 2026-02-27 11:05 in Urvania — whether the road distance and the border crossing fit this is for the consistency review.
