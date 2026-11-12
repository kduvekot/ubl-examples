# LLM review: 09-ImportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/09-ImportCustomsDeclaration.xml`, Git blob `f2d4fcae7f399f23e32926db94e2eab6ad1dd2dc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/09#F1 · Medium · An exit office in an import declaration
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`
- Why: CustomsExitOfficeLocation is the "Customs exit office of the goods being declared." Goods imported into Bayvarra do not leave its customs territory; the value is the Urvanian exit office of the export (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`), which plays no part in the Bayvarran import.
- Condition: The import declaration names no exit office, or one through which the goods leave Bayvarra.
- Options: Remove it (preferred); the place where the goods are presented is already the bonded store.
- Needs decision: no

### plastics/09#F2 · Medium · Temperature code given together with a measure
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:Measure` = `5`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:MeasureCode` = `MIN`
- Why: Temperature/MeasureCode is "A code describing the temperature, when not expressed as a measure." The temperature is expressed as a measure (5 °C), so the condition of the definition is not met.
- Condition: MeasureCode appears only where the temperature has no Measure.
- Options: Remove the MeasureCode (preferred); the element MinimumTemperature already says it is a minimum.
- Needs decision: no

### plastics/09#F3 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: PartyLegalEntity/CompanyLiquidationStatusCode is "A code signifying the party's liquidation status" and CorporateRegistrationScheme the "corporate registration scheme used to register the party". The customs authority is a public body (ISIC 8411); it is established by law, not registered in a commercial register, and cannot be in liquidation. The values describe it as a company.
- Condition: The customs authority's legal entity carries no commercial registration and no liquidation status, or names the public-body register the world has.
- Options: Drop the corporate registration and liquidation status for public bodies (preferred); or use a registration type for public bodies if the world's list has one.
- Needs decision: no

### plastics/09#F4 · Medium · A province is held in Region
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/09#F5 · Medium · A language code is held in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/09#F6 · Low · Technical data of the bonded store in the declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:AirFlowPercent` = `0`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:HumidityPercent` = `60`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:PowerIndicator` = `true`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:RefrigeratedIndicator` = `false`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MaximumTemperature/cbc:Measure` = `35`
- Why: BondedWarehouseLocation is "The location of the bonded warehouse where this goods item is temporarily stored"; customs needs to know where the goods are. Air flow, humidity, power supply, food approvals and temperature range describe the store's equipment and do nothing in an import declaration for granulate. The temperatures are moreover defined as "The minimum (maximum) allowable operating temperature for this refriguated storage", while the storage is not refrigerated.
- Condition: The bonded-store location carries what identifies it (name, licence, hall, gate), not its technical equipment.
- Options: Remove the technical storage data (preferred).
- Needs decision: no

### plastics/09#F7 · Low · The export declaration as previous declaration of the import
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `RR-CD-26-0888`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode` = `1000`
- Why: PreviousCustomsDeclaration is "A reference to a previously sent customs declaration." The ID is the Urvanian export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `RR-CD-26-0888`), sent to another customs administration, while the procedure code says the goods come from no previous procedure. A previous declaration of an import is normally one lodged in the same territory (temporary storage, transit) (own knowledge).
- Condition: The previous declaration is a declaration that the Bayvarran customs know as preceding this one, or the element is absent.
- Options: Remove it (preferred); or, if the Trade Accord links export and import declarations, reference the export declaration in a way that says so (e.g. as an additional document).
- Needs decision: yes

### plastics/09#F8 · Low · Notifier repeats the importer
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- Why: NotifierParty is "The Party who is responsible for contact on master level". It is the importer and consignee again, given only by ID and name, and adds nothing to the declaration.
- Condition: NotifierParty is absent, or is a party other than the importer with its own role.
- Options: Remove it (preferred).
- Needs decision: no

### plastics/09#F9 · Low · Signature ID contains the example flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `RP-SIG-IM-plastics`
- Why: Signature/ID is "An identifier for this signature". The value ends in `plastics`, the name of the example flow in the repository, not a value the signing party would assign; the other signatures of the flow use the party's numbering (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Signature/cbc:ID` = `FB-SIG-882`).
- Condition: The signature ID is an identifier that the signatory could assign, without reference to the example flow.
- Options: Number it like the party's other documents (preferred); or derive it from the document ID.
- Needs decision: no

### plastics/09#F10 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in an import declaration of a product depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/09#F11 · Low · Contacts do not fit the role the party has in this document
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The importer's contact answers the customs about this import (customs or shipping), not an "Order desk" in Sales.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/09#F12 · Low · Every party registered on 1 January 1996
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

### plastics/09#F13 · Low · Recycled-content certificate issued by a chamber of commerce
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- Why: EnvironmentalCertificate/IssuerParty is "The authorised Organisation who issues this Certificate". A chamber of commerce issues certificates of origin; a certificate of recycled content is normally issued by a certification body that audits the recycler (own knowledge, e.g. certification against EN 15343 or ISO 14021 claims). The issuer does not fit the kind of certificate.
- Condition: The issuer of the recycled-content certificate is an organisation that the world authorises to certify recycled content, or the world states why the chamber does so.
- Options: Name a certification body of the world as issuer (preferred); or give the chamber that role in the world story.
- Needs decision: yes

## Checked and consistent
- Values: 9984000 XUF (01, 10) = 99840.00 XBL at 100 XUF per XBL; FOB 98046.00 XBL = 99840.00 − 1794.00, the freight of 179400 XUF (06, 07).
- Quantities and weights (120 t, 120480 kg gross, 120000 kg tariff quantity) agree with 06.
- Subtype FREECIRC, procedure 1000 and status FOREIGN agree with each other.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890` resolves to 06-Waybill.xml.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount`: the importer's bank account in a declaration — refuted because the note says the duties are paid by the importer's account, which gives the account a use in this document (whether it is the bank account or a deferment account at customs is a question for the money lens).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation` with procedure 1000 "no previous procedure" — refuted because temporary storage before release is not a customs procedure.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description[2]` tagged `en-XB` here and `en-XU` in 05 — refuted because the tag follows the declarant's variety of English.
