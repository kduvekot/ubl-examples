# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/03-TransportExecutionPlanRequest.xml`, Git blob `ce4cb0e21e72b3398e1856fda182f568fe87940d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/03#F1 · Medium · The transport request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `RR-CS-26-0885`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `120480`
- Why: A Transport Execution Plan Request is "sent by a transport user to request a transport service from a transport service provider". The consignment gives an ID, a gross weight and five indicators set to false, but no description of the goods, no goods item and no packages: the barge operator cannot see that it is to carry 120 jumbo bags of PE granulate, which the waybill states (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:PackagingTypeCode` = `JB`, `06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:ContainingPackage/cbc:Quantity` = `120`).
- Condition: The request states what is to be carried: at least a description of the goods and the number and kind of packages.
- Options: Add a goods item (description, quantity, jumbo bags) or a handling-unit description to the consignment (preferred, mirrors the waybill); or describe the cargo in the consignment's own text.
- Needs decision: no

### plastics/03#F2 · Medium · FromLocation is the carrier's office, not the quay where the barge loads
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Fiumella Barges`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AddressTypeCode` = `BUSINESS`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Rivermouth Packaging`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName` = `Estuary Road`
- Why: FromLocation is "The location of origin of the transport service". It carries the carrier's name and business address, while the note of this request says the barge leaves "from the quay next to the recovery plant" (`/TransportExecutionPlanRequest/cbc:Note[2]` = `The barge from the quay next to the recovery plant down the river to the packaging maker.`) and the plan names it (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:Name` = `Quay of Rinova Recovery, Ferrano`). In the same way ToLocation is the consignee's business address, while the order delivers at the river quay (`01-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`). Both locations are named after companies, not places.
- Condition: FromLocation is the place where the transport begins (Rinova's quay) and ToLocation the place where it ends (the river quay at Lumeport), each named as a place.
- Options: Use the loading and unloading quays as From and To locations (preferred: it is what the request asks for and what the plan and waybill carry out); keep the business addresses in the parties.
- Needs decision: no

### plastics/03#F3 · Medium · A province is held in Region
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/03#F4 · Medium · A language code is held in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/03#F5 · Low · Rivermouth Packaging's bank account in a document that does not use it
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". A transport request is between the transport user and the barge operator; the consignee's bank account plays no part in it. The account (with its branch and bank address) reads as copied from the party's master data into a document that does nothing with it (section 4.8 of the review rules; IND5, no fillers).
- Condition: Rivermouth Packaging's FinancialAccount appears only in documents of the flow that pay or are paid through it (as `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` does).
- Options: Remove it here (preferred); or, if the document has a use for it, make that use visible.
- Needs decision: no

### plastics/03#F6 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in a request to carry granulate depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/03#F7 · Low · Contacts do not fit the role the party has in this document
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The sender books a barge, so its contact is the one who arranges the transport (shipping or logistics), not "Customer service" in Sales. The consignee's contact is the one who receives the goods and unloads them (the plan says "the consignee unloads"), not an "Order desk" in Sales.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/03#F8 · Low · Status code "NoStatus" carries no information
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: A status code signifies the status of the document or line; the code `NoStatus` ("No status on document") states that there is nothing to state. It adds nothing the absence of the element would not say, and is a filler under IND5/IND6 (the document-level code occurs 26 times in the examples: `grep -rho --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: The status codes are absent, or carry a status that has a reason in the situation (e.g. a replacement).
- Options: Remove (preferred); or use a code that says something about this document.
- Needs decision: no

### plastics/03#F9 · Low · Every party registered on 1 January 1996
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

## Checked and consistent
- Roles: Rinova is sender, transport user and bill-to party, as the seller who pays carriage under CPT; Fiumella Barges is receiver and transport service provider.
- TransportContract `RR-FB-FW-2026` is the same framework agreement the plan names.
- Service start 2026-04-19 and end 2026-04-22 agree with the plan and the waybill events.
- Consignment ID `RR-CS-26-0885` and gross weight 120480 kg are the same in 04, 05, 06 and 08.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:BulkCargoIndicator`: five indicators set to false as possible fillers — refuted because a carrier asks exactly these questions when it is offered a cargo, and false is a statement (jumbo bags are not bulk; granulate is no food).
- `/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.` — fits a request.

## Outside this review
- Timeline: the request is issued (2026-04-14 09:57) before the order is accepted (02-OrderResponse.xml, 2026-04-14 15:39).
