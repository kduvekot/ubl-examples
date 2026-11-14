# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/30-ExportCustomsDeclaration.xml`, Git blob `badd401509d1f287a27ff308ccae49e844329ef6` (committed)
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

### tender/30#F1 · High · The benches are described as grey although the release was changed to moss green
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), and the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`). This document concerns those same 40 benches, yet it identifies them as the grey variant: extended identifier `GRY` (the variant suffix of the seller's item number), colour attribute of the frame `GRY` "Frame in Ferro grey", and the property "Frame colour" = "Ferro grey". A customs declaration that describes the goods as grey while green benches are on the lorry misdescribes what is declared.
- Condition: Every document about the benches of this release states the colour that was ordered after the change (moss green, RAL 6005) in the extended identifier, the colour attribute and the colour property, or states none.
- Options: (a) preferred: a variant for moss green (extended identifier, colour code and text; the colour list needs a code for it) in all documents from the despatch on; (b) remove the colour data where the document does not need it.
- Needs decision: no
### tender/30#F2 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition of the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value, from a list of emission boundaries, says that the calculation covers cradle to gate; it says nothing about a transport equipment being full or empty, and the item is a bench, not a transport. The boundary is already stated in the sibling lifecycle stage description. (Semantic conformance asks for the UBL definition even where another use seems handy.) The same value comes with every copy of the item in the flow, from `25-Catalogue.xml` on.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the system boundary of the calculation is stated elsewhere.
- Options: (a) preferred: remove the element and keep the boundary in the lifecycle stage description; (b) record as a finding for the UBL TC that the emission calculation method has no element for the system boundary.
- Needs decision: yes (a recurring modelling decision)
### tender/30#F3 · Medium · A province in `Region`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/30#F4 · Medium · A language code as locale
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/30#F5 · Low · The declared value leaves out the charge for the special colour
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". 1996000 ferra is 40 × 49900, the list price of the grey benches (19960.00 lume at 100 ferra a lume). The goods exported are the 40 benches as changed and accepted, for which the buyer pays 200.00 lume more ("Special colour", `28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`, and the invoice bills the same charge). The charge is part of the price of these goods, so the value of the goods item for customs would be 2016000 ferra. (That the price paid for the goods is the basis of the customs value is my knowledge of customs valuation practice; the fictional world may rule otherwise.)
- Condition: The declared customs value equals the price payable for the declared goods including the colour charge, or the world's valuation rule that excludes such a charge is recorded.
- Options: (a) preferred: 2016000 ferra; (b) keep the value and state the rule.
- Needs decision: yes (a valuation rule of the world; the import declaration `31-ImportCustomsDeclaration.xml` declares the same 19960.00)

### tender/30#F6 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/30#F7 · Low · Master data of a party that the document does not use
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). A customs declaration needs the exporter's identity, address and trader number; its share capital, stock-exchange listing and the contact of its warehouse provider are not customs data. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
### tender/30#F8 · Low · The whole catalogue description of the item repeated in a document that does not use it
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[4]`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile`
- Why: The item is identified by the seller's and the standard item identification. Beyond that the line repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the test method of the load capacity, the range of the seat height, the greenhouse-gas emission of manufacturing with its calculation method and measurement period, and the circularity profile (maintenance frequency, resource consumption, packaging waste, repairability score, repair manual). Customs needs the description, tariff classification, origin, quantity, weight and value of the goods; a search keyword, a load test method, the seat-height range, manufacturing emissions and a repairability score are not declared to customs. It reads as item master data copied into the document; the remarks made on these values in the catalogue's review (lifecycle stage code against its description, no recycled steel shown, two keywords in one element) come along with every copy.
- Condition: The item of this document carries the identification and those properties the document's purpose uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) preferred: reduce the item to identification, name, description and the properties this document needs; (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision.
- Needs decision: yes (a design decision for all documents that carry the item)
## Checked and consistent
- `check_ids.py` reported nothing wrong for this example.
- Shipment `CL-SH-26-0216`, consignment `CL-CS-26-0217`, gross weight 1660 kg and carrier Trasvia Haulage are those of the despatch advice (`29-DespatchAdvice.xml`); 40 benches as despatched.
- Declared value 1996000 ferra = 40 × 49900 ferra (catalogue price) = 19960.00 lume at the order's rate of 100.
- The declaration is issued at 13:40 on 2026-03-30, before the despatch advice of 17:37 the same day; the note "Declared electronically before the goods leave." agrees.
- Exporter and consignor are Valdara Industries, consignee the department; the customs party is the Customs Administration of Urvania and the territory Urvania, the country of export; the exit office is on the Urvanian side of the land border, matching road carriage.
- `ExportTypeCode` permanent and `ExportReasonCode` sale fit a sale to a foreign buyer; function code 9 (original), version 1; validity 90 days from the issue date.
- `AdditionalDocumentReference` `LPWD-PO-26-0212` is the order (the invoice is issued a day later, so it cannot be referenced yet).
- Classification: HS 940179, tariff code 94017910, HS section XX (miscellaneous manufactured articles, which contains chapter 94), cargo type general cargo; origin Urvania.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: the haulier's licence in a customs declaration — refuted because customs has an interest in the authorisation of the carrier that takes the goods across the border.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod`: a validity for a declaration — refuted, the element is defined for it and a period in which the goods must exit is usual.
- `/ExportCustomsDeclaration/cac:Signature`: signed by the exporter although the note says "electronically" — refuted, an electronic declaration is signed electronically.

## Outside this review
- Gross weight 1660 kg for 40 benches against 56.5 kg of materials a bench, and the emission factor arithmetic of the item: logistics part.
