# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/03-TransportExecutionPlanRequest.xml`, Git blob `ce4cb0e21e72b3398e1856fda182f568fe87940d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### plastics/03#F1 · High · Origin of the transport is the carrier's office, not the loading quay
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlanRequest/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`
- Why: FromLocation is "The location of origin of the transport service referenced in the Transport Execution Plan Request". The request names the carrier and gives the carrier's own business address (the same as `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`, building 52, postal zone 4170), while its own note says the barge leaves from the quay next to the recovery plant, and the plan and the waybill load at Rinova's quay (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`; `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`). Rinova's plant is at another address (Via del Riciclo 31, postal zone 4140). The location name is also a company name, not a place.
- Condition: the origin of the requested service is the place where the goods are taken over and loaded (Rinova's quay), named as a place, and agrees with the note and with the loading place in `04-TransportExecutionPlan.xml` and `06-Waybill.xml`.
- Options: (a) FromLocation = Rinova's quay in Ferrano, with a name and, where it exists, an address or identifier of the quay (preferred); (b) if the barge really starts at Fiumella's base, say so and keep the quay as the place of takeover elsewhere in the request.
- Needs decision: no

### plastics/03#F2 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: A Transport Execution Plan Request is "sent by a transport user to request a transport service"; the carrier needs to know what it is asked to carry. The consignment states only a gross weight and negative indicators; there is no goods item, description, package type or count (120 jumbo bags of PE granulate, see `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`) and no volume. The note only says "the barge … to the packaging maker". This is the skill's own example of missing information the purpose depends on.
- Condition: the request describes the goods to be carried: at least description, number and type of packages, gross weight (and volume, which matters for a barge hold).
- Options: (a) add a goods item (description, packages, weight, volume) or a handling-unit/package description to the consignment (preferred); (b) state the goods in the consignment's description fields if a structured goods item is not wanted.
- Needs decision: no

### plastics/03#F3 · Medium · Province of Urvanian addresses in Region
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity` ("such as the name of its county, province, or state"), as the Bayvarran address in the same document does (`/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Coastal State`). No `languageID`, unlike the other parts of these addresses. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if Ferrano is an economic region, documented.
- Needs decision: no

### plastics/03#F4 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` from ISO 639 is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale (e.g. `en-XB`) from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` with a locale list (preferred); (b) drop it.
- Needs decision: no

### plastics/03#F5 · Low · Destination named after the consignee, with its business address
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- Why: ToLocation is "The destination location for the transport service". It is named after the company and carries its business address (`AddressTypeCode` `BUSINESS`, Old town), while the agreed place of delivery is the river quay (`01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`) and the plan unloads at `River quay, Lumeport`. Whether Estuary Road 28 is at that quay is not stated.
- Condition: the destination is the place where the barge is unloaded, named as a place, and agrees with the delivery place of the order and the unloading place of the plan.
- Options: (a) ToLocation = the river quay in Lumeport (preferred); (b) if the quay is part of Rivermouth's premises at Estuary Road 28, name the quay and keep the address.
- Needs decision: no

### plastics/03#F6 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- Why: The sender books a barge as transport user; its contact is a sales customer-service officer, not shipping or logistics. The consignee's contact, who receives the goods and the pre-arrival notice, is a sales order desk (job title customer service officer), not goods receipt.
- Condition: the transport user's contact handles transport bookings, and the consignee's contact handles goods receipt.
- Options: (a) role-specific contacts for transport documents (preferred); (b) neutral general contacts.
- Needs decision: no

### plastics/03#F7 · Low · Consignee's bank account in a transport request
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: The consignee pays nothing under this request (the bill-to party is Rinova, `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`). The account is master data the document does nothing with.
- Condition: no consignee account in the request.
- Options: remove it (preferred); no other reason to keep it is visible.
- Needs decision: no

### plastics/03#F8 · Low · Waste-recovery authorisation in a transport request for a product
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The goods are a product (HS 390110 granulate, see `01-Order.xml`), not waste, so the carrier needs no waste permit for this voyage. Carrying the recovery permit (Basel Annex IV code `R3`) in a transport document can even suggest a waste shipment.
- Condition: the waste-recovery authorisation appears only in documents that use it.
- Options: remove it from the transport request (preferred).
- Needs decision: no

### plastics/03#F9 · Low · Document status "no status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: The element is optional and the code says there is no status; it adds nothing to the request (IND5/IND6: no fillers). 26 occurrences at document level in the world (`grep -rh --include='*.xml' '<cbc:DocumentStatusCode' world/examples | sort | uniq -c`).
- Condition: `DocumentStatusCode` is present only with a status that means something here (e.g. original, revised).
- Options: (a) omit it (preferred); (b) use a status with a business meaning.
- Needs decision: no

### plastics/03#F10 · Low · All three parties registered on 1 January 1996
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Three companies in two countries share one registration date, the most frequent one in the world (271 occurrences); a default value unless the story explains it.
- Condition: individual registration dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

## Checked and consistent
- Gross weight 120 480 kg = 120 t net + 120 jumbo bags × 4 kg (the waybill's net and package count); 4 kg is a usual tare for a woven-polypropylene 1 t FIBC (own knowledge). Matches `04-TransportExecutionPlan.xml`, `05-ExportCustomsDeclaration.xml` and `06-Waybill.xml`.
- `BulkCargoIndicator` `false` fits goods in jumbo bags.
- Service window 2026-04-19 to 2026-04-22 and response deadline 2026-04-15 agree with the plan (`04-TransportExecutionPlan.xml`, issued 2026-04-15).
- Consignment ID `RR-CS-26-0885` is used for the same consignment in 04, 05, 06 and 08.
- Bill-to party (Rinova) fits CPT: the seller pays the carriage.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:HumanFoodIndicator` and the other indicators set to `false`: suspected fillers — refuted: they tell the carrier what kind of goods it is not carrying (not food, not livestock, not bulk), which matters for a dry barge hold.

## Outside this review
- The request (2026-04-14 09:57) precedes the seller's acceptance of the order (`02-OrderResponse.xml`, 2026-04-14 15:39): timeline across documents.
