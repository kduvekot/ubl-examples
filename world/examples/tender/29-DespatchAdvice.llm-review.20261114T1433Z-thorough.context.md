# LLM review: 29-DespatchAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/29-DespatchAdvice.xml`, Git blob `79edc7989dc6f0f5e4d8a3b040fb4fdfaa8e1ecc` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit e0e5001 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/29#F1 · High · The benches are described as grey although the release was changed to moss green
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). This document concerns those same 40 benches, yet it identifies them as the grey variant: extended identifier `GRY` (the variant suffix of the seller's item number), colour attribute of the frame `GRY` "Frame in Ferro grey", and the property "Frame colour" = "Ferro grey". The despatch advice contradicts itself as well: its own line note says `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`
- Condition: Every document about the benches of this release states the colour that was ordered after the change (moss green, RAL 6005) in the extended identifier, the colour attribute and the colour property, or states none.
- Options: (a) preferred: a variant for moss green (extended identifier, colour code and text; the colour list needs a code for it) in all documents from the despatch on; (b) remove the colour data where the document does not need it.
- Needs decision: no
### tender/29#F2 · Medium · The despatch advice does not say when the goods left, when they arrive or where they go
- XPath: `/DespatchAdvice/cac:Shipment`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `CL-CS-26-0217`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and services"; its purpose is to let the recipient prepare for the arrival. The shipment gives an identifier, a gross weight, a consignment number and the carrier. There is no delivery or despatch element anywhere in the document (no `Delivery`, despatch date, estimated delivery date, delivery address; searched the annotated listing): the recipient learns neither when the lorry left Castrano's warehouse, nor when it will be at the depot, nor that the depot is the destination (the order names "Public works depot, Lumeport" only as the place of the delivery terms). The type code is `DELIVERY`, and the note asks the recipient to check the goods on arrival.
- Condition: The despatch advice states the despatch date, the estimated (or actual) delivery date and the delivery location.
- Options: (a) preferred: a `Delivery` in the shipment with despatch (date, Castrano's warehouse) and estimated delivery period at the depot's address; (b) at least the estimated delivery date.
- Needs decision: no

### tender/29#F3 · Medium · Benches that were never ordered given as "outstanding"
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingQuantity` = `200`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingReason` = `Later releases under the framework contract.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `40`
- Why: `OutstandingQuantity` is "The quantity outstanding (which will follow in a later despatch)", measured against the order line the despatch line references (`/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` of order `LPWD-PO-26-0212`). That line orders 40 benches (`26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `40`), and 40 are delivered: nothing is outstanding. The 200 are the rest of the framework's estimated 240, which nobody has ordered and which the buyer need not order (the contract's minimum is 120, its maximum 288). A logistics provider's despatch advice cannot announce them as following.
- Condition: The outstanding quantity of a despatch line is the part of the referenced order line not yet despatched (here none), or is absent.
- Options: (a) preferred: remove `OutstandingQuantity` and `OutstandingReason`; (b) none seen.
- Needs decision: no

### tender/29#F4 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/29#F5 · Medium · A province in `Region`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/29#F6 · Medium · A language code as locale
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/29#F7 · Low · "No status" stated for the document and the line
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Despatch Advice with respect to its original state", the line's code the status of the line (added, revised, cancelled). This is the first and only despatch advice of the release; "no status" is what the absence of the element already says. Under the rule that nothing is stated that is implied by absence (IND5/IND6, no fillers) the two values have no business reason.
- Condition: Status codes are present only when the document or line has a status to report (revised, cancelled, …).
- Options: (a) preferred: remove both; (b) none seen.
- Needs decision: no

### tender/29#F8 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/29#F9 · Low · Master data of a party that the document does not use
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The despatch advice is issued by Castrano Logistics, the service provider itself, as despatch party; restating under the seller that Castrano is its service provider, and the seller's share capital and listing, adds nothing to a description of a despatch. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/29#F10 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:Dimension[4]`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). A despatch advice says what was put on the lorry: item, variant, lot, quantity. The recipient checks the goods against the order, not against emission factors, test methods or a repairability score. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- `OrderReference` `LPWD-PO-26-0212` and order line 1; 40 benches delivered = 40 ordered; the despatch (2026-03-30) follows the accepted order change (2026-03-25) and the manufacture date of the lot (2026-03-27).
- Sub-lines against the item's text "Supplied with four ground anchors and the bolts to fix them": 36 anchor sets delivered + 4 on back order = 40, one per bench, with a reason and a date ("within a week"); 170 bolts delivered with an oversupply of 10 = 160 due = 4 per bench.
- Despatch party Castrano Logistics is the seller's logistics provider ("Warehousing and despatch") in all documents of the flow; it signs the advice; seller, buyer and delivery customer are in their roles; the carrier is a road haulier with an operating permit for international haulage, which a cross-border road transport needs.
- The line's shipment `CL-SH-26-0216` is the document's shipment.
- Lot `VI-LOT-260327` matches the manufacture date 2026-03-27.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: a haulage licence in a despatch advice looked like unused master data — refuted because the transport crosses the border between Urvania and Bayvarra and the licence is what entitles this carrier to do it.
- `/DespatchAdvice/cac:DespatchLine/cbc:AccountingCostCode`: the buyer's accounting code in a document of the seller's logistics provider — refuted because it is copied from the order (`PWD-PARKS-26`) so that the buyer can book the receipt.
- `/DespatchAdvice/cac:DespatchLine/cac:DocumentReference/cbc:ID`: the contract as a line's document reference — refuted, the definition allows any associated document; its kind is for the logistics part.
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: `DELIVERY` — refuted, fits a despatch on delivery to the customer.
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[2]/cbc:OversupplyQuantity`: oversupply of bolts — refuted, spare bolts are plausible and the arithmetic holds.

## Outside this review
- Gross weight 1660 kg for 40 benches is 41.5 kg a bench, while the item's own resource consumption gives 34 kg of steel and 22.5 kg of hardwood (56.5 kg a bench, 2260 kg for 40, before pallets); physics is the logistics part's lens.
- The emission factor arithmetic of the item (0.82 × 1 against 96 kg): logistics part.
