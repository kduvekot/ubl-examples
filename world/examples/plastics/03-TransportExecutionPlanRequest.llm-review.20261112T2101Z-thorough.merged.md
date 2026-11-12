# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/03-TransportExecutionPlanRequest.xml`, Git blob `ce4cb0e21e72b3398e1856fda182f568fe87940d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:PostalZone` = `4170`
- XPath: `/TransportExecutionPlanRequest/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:PostalZone` = `4140`
- XPath: `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- XPath: `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`
- Why: `FromLocation` is "The location of origin of the transport service referenced in the Transport Execution Plan Request". The request names the carrier and gives Fiumella's own business address (the same as `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:PostalZone` = `4170`, building 52), while its own note says the barge leaves from the quay next to the recovery plant (Rinova, Via del Riciclo 31, postal zone 4140), and the plan answering this request and the waybill for the same consignment load at Rinova's quay. A location's name is the place, not the company. Parties part rated it Medium, because the document alone cannot exclude that Fiumella's address is next to the plant; the merge keeps High (as broad): the postal zones differ, and the plan and waybill, which describe the same consignment `RR-CS-26-0885`, name a different place of origin, which is a contradiction with other examples of the flow (section 6).
- Condition: the origin of the requested service is the place where the goods are taken over and loaded (Rinova's quay in Ferrano), named and located as a place, and agrees with the note and with the loading place in `04-TransportExecutionPlan.xml` and `06-Waybill.xml`.
- Options: (a) `FromLocation` = Rinova's quay, with a name and its address or location identifier, the same values in 03, 04 and 06 (preferred); (b) if the barge really starts at Fiumella's base, say so in the note and keep the loading quay as the place of takeover elsewhere in the request (and in 04 and 06).
- Needs decision: no
- From: broad, logistics, parties, context

### plastics/03#F2 · Medium · Province of Urvanian addresses in Region
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country … such as the name of its county, province, or state", i.e. `CountrySubentity`, as the Bayvarran address of the same document does (`/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Coastal State`, with `CountrySubentityCode`). No `languageID`, unlike the other parts of these addresses. 219 occurrences in 104 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; where given, it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) drop it where the postal code identifies the place; (c) keep only if Ferrano is an economic region, recorded in the world data.
- Needs decision: no
- From: broad, parties, context

### plastics/03#F3 · Medium · The request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: a Transport Execution Plan Request is "sent by a transport user to request a transport service from a transport service provider"; the carrier needs to know what it is asked to carry. The consignment states an ID, a gross weight and five indicators set to false, but no goods item, description, number or type of packages, and no volume. The cargo is 120 jumbo bags of PE granulate of about 204 m³ (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:Quantity` = `120`, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cbc:GrossVolumeMeasure` = `204`), which decides the space in a barge hold. The indicators only say what the cargo is not. This is the skill's own example of missing information the purpose depends on.
- Condition: the request describes the goods to be carried: at least a description (or goods item) and the number and type of packages (120 × JB), ideally the volume, consistent with 06.
- Options: (a) add a `cac:GoodsItem` (description, quantity, gross weight, packages) or, at consignment level, `TotalPackagesQuantity`, `GrossVolumeMeasure` and a goods description (preferred: mirrors the waybill); (b) a `TransportHandlingUnit` with the 120 bags.
- Needs decision: no
- From: broad, logistics, context

### plastics/03#F4 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language, already in `Language/ID`. All 362 `LocaleCode` elements, in 213 of the 250 XML examples, carry this value.
- Condition: a locale (e.g. `en-XB`) from a locale list named in `listID`, or no `LocaleCode`.
- Options: (a) drop it (preferred); (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### plastics/03#F5 · Low · Document status "no status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: the element is optional, and the code (UBL default list: "No status on document") states that there is nothing to state; it adds nothing the absence of the element would not say (IND5/IND6). The document-level value occurs 26 times in the XML examples (`grep -rho --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: `DocumentStatusCode` is absent, or carries a status with a reason in the situation (e.g. a revision).
- Options: (a) omit it (preferred); (b) a status with a business meaning.
- Needs decision: no
- From: broad, context

### plastics/03#F6 · Low · Italian text tagged as English
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- Why: each repeated rendering should be in the language its `languageID` names; these `en-XU` renderings are Italian ("Via del Riciclo", "Recycling street"; "Banchina del Fiume", "River quay") and the legal form is Italian with an English gloss, while Bayvarran streets are English. 101 of the 250 XML examples show the pattern (parties part). Counter-argument (the broad and context parts refuted the same candidate in `01-Order.xml`): Italianate exonyms are the world's convention for Urvanian names in English. The merge cannot settle it for street names; the legal form is a description, not a name, and is the stronger case.
- Condition: every rendering tagged `en-…` is English or a proper name used as such in English, and the convention is recorded in the world story if meant.
- Options: (a) record the convention and render the legal form in English (preferred); (b) translate all renderings; (c) drop the second rendering where the local form suffices.
- Needs decision: yes
- From: parties

### plastics/03#F7 · Low · All three companies registered on 1 January 1996
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Three companies (`XU-R-104548`, `XU-R-104959`, `20412740`) in two registers share New Year's Day 1996; the date occurs 271 times in 181 of the 250 XML examples (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`). A default value (IND5) unless the story explains it.
- Condition: each company's registration date is its own, or the shared date is explained in the world's history, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a general (re-)registration in the story; (c) drop where no history is known.
- Needs decision: yes
- From: broad, parties, context

### plastics/03#F8 · Low · Contacts do not fit the transport roles
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender books a barge as transport user, so its contact is shipping or logistics, not a sales customer-service officer. The consignee's contact, who receives and unloads the goods, is a sales order desk, not goods receipt. The parties carry one generic contact in every document of the flow. (Fiumella's "Chartering desk" in Operations fits the receiver of a booking.)
- Condition: the transport user's contact handles transport bookings and the consignee's contact handles goods receipt, or the contacts are absent.
- Options: (a) role-specific contacts per party (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad, parties, context

### plastics/03#F9 · Low · Rinova's waste-recovery permit in a transport request for a product
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: the goods are a product (HS 390110 granulate, see `01-Order.xml`), not waste, so the carrier needs no waste permit for this voyage; carrying the recovery permit (Basel Annex IV `R3`) in a transport document can even suggest a waste shipment. It is in 14 XML examples, all 11 of this flow: master data copied into every document (IND5).
- Condition: the waste-recovery authorisation appears only in documents that use it.
- Options: (a) remove it from the request (preferred); (b) if the recycled-content claim is to rest on it, tie it to the item's certificate in documents that carry the item.
- Needs decision: no
- From: broad, parties, context

### plastics/03#F10 · Low · Destination named after the consignee, with its business address
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- XPath: `01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`
- XPath: `04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`
- Why: `ToLocation` is "The destination location for the transport service". It carries the consignee's company name and business address (`AddressTypeCode` `BUSINESS`, Estuary Road 28, Old town), while the CPT place of the order and the unloading port of the plan are the "River quay, Lumeport". Whether Estuary Road 28 is at that quay is not stated anywhere, so a contradiction cannot be shown; the name of a location is the place, not the company.
- Condition: the destination is the place where the barge is unloaded, named as a place, and agrees with the order's delivery place and the plan's unloading place.
- Options: (a) `ToLocation` = the river quay in Lumeport (preferred: the CPT place); (b) if Rivermouth has its own quay at Estuary Road 28, name it as such here and in 04.
- Needs decision: no
- From: broad, parties; logistics and context (grouped with F1 there)

### plastics/03#F11 · Low · Consignee's bank account in a transport request
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". The consignee neither pays nor receives anything under this request: the transport is billed to Rinova (`/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`), consistent with `CPT`. Master data the document does nothing with (section 4.8); the account is in 14 XML examples.
- Condition: the consignee party carries no financial account unless the request uses it (e.g. freight collect from the consignee).
- Options: (a) drop it (preferred); (b) keep it only if the story makes the consignee pay part of the transport.
- Needs decision: no
- From: broad, money, parties, context

## Checked and consistent
- Gross weight (redone in the merge): 120 bags × 1 000 kg net + 120 × 4 kg bag tare = 120 480 kg; tare derived from 06 (120 480 − 120 000 = 480 kg), and 2.5–5 kg is usual for a woven-PP 1 t FIBC (own knowledge). Same weight in 04, 05, 06, 08 and 09.
- `BulkCargoIndicator` `false` fits goods in jumbo bags.
- Service window 2026-04-19 to 2026-04-22 and response deadline 2026-04-15 agree with the plan (`04-TransportExecutionPlan.xml`, issued 2026-04-15 13:10, same window).
- Consignment ID `RR-CS-26-0885` is the same in 04, 05, 06 and 08; contract `RR-FB-FW-2026` is the framework agreement the plan names.
- Roles: Rinova as sender, transport user and bill-to party (seller paying carriage under CPT, invoiced in `07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`); Fiumella as receiver and transport service provider. Parties are described the same way across the flow apart from renderings (parties part). `check_ids.py`: the IBAN-like account passes.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:HumanFoodIndicator` and the other indicators set to `false`: suspected fillers — refuted: they answer what a carrier asks when offered a cargo (not food, not livestock, not bulk), which matters for a dry barge hold, and false is a statement. (from broad, context)
- `/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.` — fits a request. (from context)
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` could clash with a real ICD — refuted: not assigned in the real register (own knowledge). (from parties)
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped identifier (`BLUMXBLX`) could be a real BIC — refuted: positions 5–6 carry the user-assigned code `XB`. (from parties)
- `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name`: the seller as bill-to party while the goods go to the buyer — refuted: under CPT the seller contracts and pays the carriage, and `07-Invoice.xml` bills Rinova. (from parties)

## Changed in the merge
- broad/F1, logistics/F2, parties/F3, context/F2 → F1 (High) and F10 (Low): FromLocation and ToLocation split. FromLocation kept High (broad) against Medium (logistics, parties, context), because it contradicts the loading place of 04 and 06 for the same consignment and the note; ToLocation Low (broad, parties), because no contradiction can be shown for it.
- broad/F3, parties/F1, context/F3 → F2: combined.
- broad/F2, logistics/F1, context/F1 → F3: combined, evidence from all three.
- broad/F4, parties/F2, context/F4 → F4: combined; preferred option "drop" (parties) over "en-XB" (broad, context), for consistency with the other merges.
- broad/F9, context/F8 → F5: combined.
- parties/F8 → F6: counter-argument from the refutations in `01-Order.xml` added; preferred option changed to "record the convention, render the legal form in English".
- broad/F10, parties/F7, context/F9 → F7: combined; "Needs decision" yes (broad, context) rather than no (parties).
- broad/F6, parties/F4, context/F7 → F8: combined.
- broad/F8, parties/F6, context/F6 → F9: combined; "Needs decision" no (broad, context) instead of yes (parties).
- broad/F7, money/F1, parties/F5, context/F5 → F11: combined.

## Outside this review
- Timeline across documents: the request (2026-04-14 09:57) precedes the seller's acceptance of the order (`02-OrderResponse.xml`, 2026-04-14 15:39). A seller may book transport before confirming; a question for the consistency review. (from broad, logistics, context)
