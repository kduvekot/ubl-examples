# LLM review: 31-ImportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/31-ImportCustomsDeclaration.xml`, Git blob `f995e80c478f86074b7bfa4eca588151c5ee7767` (committed)
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

### tender/31#F1 · High · The benches are described as grey although the release was changed to moss green
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). This document concerns those same 40 benches, yet it identifies them as the grey variant: extended identifier `GRY` (the variant suffix of the seller's item number), colour attribute of the frame `GRY` "Frame in Ferro grey", and the property "Frame colour" = "Ferro grey". A customs declaration that describes the goods as grey while green benches arrive misdescribes what is declared.
- Condition: Every document about the benches of this release states the colour that was ordered after the change (moss green, RAL 6005) in the extended identifier, the colour attribute and the colour property, or states none.
- Options: (a) preferred: a variant for moss green (extended identifier, colour code and text; the colour list needs a code for it) in all documents from the despatch on; (b) remove the colour data where the document does not need it.
- Needs decision: no
### tender/31#F2 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/31#F3 · Medium · A province in `Region`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/31#F4 · Medium · A language code as locale
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/31#F5 · Low · The declared value leaves out the charge for the special colour
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". 19960.00 lume is 40 × 499.00, the price of the benches before the order change. The importer, who declares, itself asked for the special colour and accepted to pay 200.00 lume for it (`27-OrderChange.xml:/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`); the invoice issued two hours before this declaration bills the charge (`32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `200.00`). The charge is part of the price paid for these goods, so their value for customs would be 20160.00. (That the price paid is the basis of the customs value is my knowledge of customs valuation practice; the fictional world may rule otherwise.)
- Condition: The declared customs value equals the price payable for the declared goods including the colour charge, or the world's valuation rule that excludes such a charge is recorded.
- Options: (a) preferred: 20160.00; (b) keep the value and state the rule. The export declaration `30-ExportCustomsDeclaration.xml` has the same question.
- Needs decision: yes

### tender/31#F6 · Low · The importer repeated as notifier
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ImportCustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `NotifierParty` is "The Party who is responsible for contact on master level", a contact party distinct in function from the importer ("The Party who makes the import declaration …") and the consignee. Importer and consignee are needed and are rightly the department. The notifier is the same department again, without a contact of its own that would make it the party to turn to; it adds nothing (rule: no fillers).
- Condition: `NotifierParty` is present only when a party or contact other than the importer is responsible for contact about the declaration.
- Options: (a) preferred: remove it; (b) name the department's customs contact, or an agent, if the world has one.
- Needs decision: no

### tender/31#F7 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company. Here it concerns both the importing department and the customs service that processes the declaration.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/31#F8 · Low · Master data of a party that the document does not use
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). The import declaration needs the consignor's identity and address; its share capital, stock-exchange listing and warehouse provider are not customs data of the importing country. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/31#F9 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[4]`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). Customs needs the description, tariff classification, origin, quantity, weight and value of the goods; a search keyword, a load test method, the seat-height range, manufacturing emissions and a repairability score are not declared to customs. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- `PreviousCustomsDeclaration` `VI-CD-26-0219` is the customs declaration identifier of the export declaration (`30-ExportCustomsDeclaration.xml`); the exit office named is the one of that declaration.
- Shipment `CL-SH-26-0216`, 40 benches, 1660 kg: as in the despatch advice and the export declaration; the import declaration (2026-03-31 11:14) follows the despatch (2026-03-30 17:37).
- Type import, subtype release for free circulation, nature of transaction outright purchase: fit a purchase for use in Bayvarra; jurisdiction Bayvarra; customs party the Customs and Border Service of Bayvarra.
- The note "Duties paid by the importer's account at customs." agrees with delivery terms DAP of the order (import formalities and duties are the buyer's) and with the department being importer.
- Value 19960.00 lume = the export declaration's 1996000 ferra at the rate of 100.
- Signature by the importer.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: an exit office on the Urvanian side in an import declaration — refuted because the element is defined as "Customs exit office of the goods being declared", i.e. where they left the exporting territory; the model offers no entry office here.
- `/ImportCustomsDeclaration/cac:ValidityPeriod`: 30 days — refuted, defined for the declaration and plausible.
- `/ImportCustomsDeclaration/cbc:Note`: speaks of duties while no amount of duty is given — refuted because the declaration document has no place for assessed duties and the note only says how they are settled.

## Outside this review
- Gross weight 1660 kg for 40 benches against 56.5 kg of materials a bench, and the emission factor arithmetic of the item: logistics part.
- Whether duties are due at all between Urvania and Bayvarra under the Trade Accord: world rule, not checkable from the XML.
