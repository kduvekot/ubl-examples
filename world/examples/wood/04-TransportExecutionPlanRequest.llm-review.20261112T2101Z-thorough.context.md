# LLM review: 04-TransportExecutionPlanRequest.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

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

### wood/04#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/04#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/04#F3 · Low · The requested transport ends before the agreed delivery period begins
- XPath: `/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-03-01`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-02-27`
- Why: `ServiceEndTimePeriod` is "The period during which the services ... must be completed". The seller asks the haulier to complete delivery to the buyer by 2026-03-01, but the buyer requested and the seller promised delivery from 2026-03-02 to 2026-03-16; the goods are in fact declared for import on 2026-02-27. Nothing in the flow says the buyer accepted an early delivery.
- Condition: The transport service window lies within the agreed delivery period, or an example of the flow states that the buyer agreed to earlier delivery.
- Options: Preferred: move the service window into the delivery period (e.g. start 2026-03-02). Alternative: keep the dates and add the buyer's agreement to early delivery to the story.
- Needs decision: yes (changes when the delivery happens in the story)

### wood/04#F4 · Low · The goods to be carried are described only in a note
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The slats across the border to the bench factory.`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- Why: A transport execution plan request asks a provider to plan a transport; the provider needs to know what it carries and how it is packed. The consignment carries only an ID and the gross weight; the goods ("slats") appear only in the free-text note, and the 96 bundles of 50 that the despatch advice reports (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`) are not stated. For a full truck load the weight alone lets the haulier check the payload, but not the loading.
- Condition: The consignment states what is carried in structured form (goods description and the number and kind of packages or handling units).
- Options: Preferred: add the goods description and the 96 bundles (on pallets, if so) to the consignment.
- Needs decision: no

### wood/04#F5 · Low · The haulier's own licence in the request sent to the haulier
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: The request is sent by the sawmill to Trasvia Haulage. Describing the receiver with its own operating permit tells the receiver nothing and the request does nothing with it (it does not, for example, ask for a service that requires the permit). It looks copied from the haulier's master data.
- Condition: The receiver party carries only what the request needs to address it, or the authorization is used for a stated purpose.
- Options: Preferred: drop the authorization here and keep it in documents where a third party relies on it (e.g. a customs declaration naming the carrier).
- Needs decision: no

### wood/04#F6 · Low · A status code that says "no status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: The code `NoStatus` means "No status on document" (or "Line has no status"). Present, it states only that there is nothing to state, which is a filler under the rule "no fillers, and nothing implied by absence": its absence would say the same. The value occurs as `DocumentStatusCode` in 26 examples (`grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: A status code is present only where the document has a status to convey (e.g. a replacement or copy).
- Options: Preferred: drop the element. Alternative: use it in an example where the status matters.
- Needs decision: no

### wood/04#F7 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the sender's contact is the transport user booking a truck (shipping or logistics); the consignee's contact is the one who receives the truck at goods-in. A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/04#F8 · Low · Party master data this document does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. A transport request needs the consignee's identity and the delivery address. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

## Checked and consistent
- Sender, transport user and bill-to party are all the sawmill, which fits DAP (seller pays the main carriage); `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`.
- From and to locations match the seller's and the buyer's addresses.
- Gross weight 21 600 kg for 4800 slats of 1.8 × 0.095 × 0.038 m (31.2 m³): about 690 kg/m³ with packaging, plausible for kiln-dried ash or oak (own knowledge, 650–750 kg/m³), and within a full truck load.
- The response deadline (2026-02-24) is after the issue date (2026-02-23) and before the service start (2026-02-26).

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: the definition speaks of "the extent of this transportation service (e.g., door-to-door, port-to-port)", suspected that a load type is used — refuted because a full truck load defines the extent of the service (exclusive use of a whole truck, door to door), a legitimate reading.
- `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` tagged `en-XB` while the same street is tagged `en-XU` in Urvanian documents: suspected inconsistent tags — refuted because the tag follows the English of the issuing party, consistently within each document.
