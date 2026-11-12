# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

This part applies the context lens: whether each element belongs in this document and whether its value makes sense in this element, this parent and this situation.

## Findings

### plastics/05#F1 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: PartyLegalEntity/CompanyLiquidationStatusCode is "A code signifying the party's liquidation status" and CorporateRegistrationScheme the "corporate registration scheme used to register the party". The customs authority is a public body (ISIC 8411); it is established by law, not registered in a commercial register, and cannot be in liquidation. The values describe it as a company.
- Condition: The customs authority's legal entity carries no commercial registration and no liquidation status, or names the public-body register the world has.
- Options: Drop the corporate registration and liquidation status for public bodies (preferred); or use a registration type for public bodies if the world's list has one.
- Needs decision: no

### plastics/05#F2 · Medium · A province is held in Region
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of countries in which this address is located" and Address/CountrySubentity as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" is an administrative division of Urvania, so it is a CountrySubentity; the Bayvarran addresses of the flow put their state ("Coastal State") in CountrySubentity with a CountrySubentityCode. The same value occurs 219 times in 104 example files (`grep -rho --include='*.xml' 'Province of Ferrano' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: No Address in the example carries a province in `cbc:Region`; the province of each Urvanian address is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if Urvania has such a list).
- Options: Move the province to CountrySubentity (preferred: it is what the element is defined for and matches the Bayvarran addresses); or, if the world means an economic region, name a region and keep the province apart.
- Needs decision: no

### plastics/05#F3 · Medium · A language code is held in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID `ISO 639` is the language itself and repeats Language/ID; it says nothing about the locale (language and country or region, such as the `en-XB` the examples use in languageID). All 362 LocaleCode elements in the example files carry `en` with listID `ISO 639` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*' world/examples | sort | uniq -c`).
- Condition: Every LocaleCode names a locale from a list that its listID names, or is absent.
- Options: Use a locale code (for example `en-XB` from BCP 47, with that as listID; preferred, it matches the languageID tags of the examples); or remove LocaleCode where the party's locale has no use in the document.
- Needs decision: no

### plastics/05#F4 · Low · Rivermouth Packaging's bank account in a document that does not use it
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: Party/FinancialAccount is "The financial account associated with this party". An export declaration tells customs who exports what to whom; the consignee's bank account plays no part in it. The account (with its branch and bank address) reads as copied from the party's master data into a document that does nothing with it (section 4.8 of the review rules; IND5, no fillers).
- Condition: Rivermouth Packaging's FinancialAccount appears only in documents of the flow that pay or are paid through it (as `11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` does).
- Options: Remove it here (preferred); or, if the document has a use for it, make that use visible.
- Needs decision: no

### plastics/05#F5 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The PartyAuthorization of Rinova Recovery is its permit to recover plastic waste (Basel Annex IV R3, certificate of the scheme `waste-permit`). The goods of the flow are recycled PE granulate classified as a product (HS 390110, polyethylene in primary forms), not as waste, and nothing in an export declaration of granulate (HS 390110) depends on Rinova being allowed to take in and process waste. The same permit is in 14 example files, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples`), which reads as master data copied into every document (IND5).
- Condition: The permit appears only in documents that act on it (a waste shipment, or the evidence behind the recycled-content claim if the world wants to show it), or the document says why it is relevant.
- Options: Remove it from this document (preferred); or, if the recycled-content claim is to rest on it, connect it to the item's EnvironmentalCertificate instead of the party.
- Needs decision: no

### plastics/05#F6 · Low · The referenced order is not identified as an order
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `RP-PO-26-0882`
- Why: AdditionalDocumentReference is "A reference to additional documents relevant or related to this customs declaration". It gives only the number of the buyer's order (01-Order.xml), with no document type, so customs cannot tell what kind of document it is.
- Condition: The reference says what it refers to (a document type code).
- Options: Add DocumentTypeCode (preferred).
- Needs decision: no

### plastics/05#F7 · Low · Signature ID contains the example flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `RR-SIG-EX-plastics`
- Why: Signature/ID is "An identifier for this signature". The value ends in `plastics`, the name of the example flow in the repository, not a value the signing party would assign; the other signatures of the flow use the party's numbering (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Signature/cbc:ID` = `FB-SIG-882`).
- Condition: The signature ID is an identifier that the signatory could assign, without reference to the example flow.
- Options: Number it like the party's other documents (preferred); or derive it from the document ID.
- Needs decision: no

### plastics/05#F8 · Low · Contacts do not fit the role the party has in this document
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The exporter's contact answers customs about this export (shipping or customs), not "Customer service" in Sales; the consignee's "Order desk" in Sales has no role toward the Urvanian customs.
- Condition: The contact of each party is reachable for what the party does in this document (job title and department agree with that role).
- Options: Give each party a contact per role (preferred: buying, goods receipt, accounts payable or receivable, shipping, customs); or leave out contacts that have no use in the document.
- Needs decision: no

### plastics/05#F9 · Low · Every party registered on 1 January 1996
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Every company of the example is registered on the same day, New Year's Day 1996, a day on which registers are normally closed; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, and `grep -rl` for the files). It reads as a default value rather than a fact of each company's history (IND5).
- Condition: Each RegistrationDate is the date from that company's own history, or the element is absent.
- Options: Take the date from each company's history (preferred, if the world gives one); otherwise remove it.
- Needs decision: yes

### plastics/05#F10 · Low · Recycled-content certificate issued by a chamber of commerce
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- Why: EnvironmentalCertificate/IssuerParty is "The authorised Organisation who issues this Certificate". A chamber of commerce issues certificates of origin; a certificate of recycled content is normally issued by a certification body that audits the recycler (own knowledge, e.g. certification against EN 15343 or ISO 14021 claims). The issuer does not fit the kind of certificate.
- Condition: The issuer of the recycled-content certificate is an organisation that the world authorises to certify recycled content, or the world states why the chamber does so.
- Options: Name a certification body of the world as issuer (preferred); or give the chamber that role in the world story.
- Needs decision: yes

## Checked and consistent
- Consignment `RR-CS-26-0885`, shipment `RR-SH-26-0889`, carrier Fiumella Barges, goods (120 t, 120480 kg, HS 390110, origin XU) agree with 03, 04, 06 and 08.
- Export type PERMANENT with reason SALE fits the sale of 01-Order.xml.
- Exit office "Customs post at the river border" fits a barge leaving Urvania by the river.

## Considered and refuted
- `/ExportCustomsDeclaration/cbc:Note[2]` = `Declared electronically before the goods leave.` against the despatch at 15:10 (06) before the issue at 16:08 — refuted because "leave" means leave the customs territory, which happens at `06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`.
- `//cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `120480` equal to the goods gross weight although the shipment weight includes transport equipment — refuted because the jumbo bags travel loose in the barge hold, with no equipment.
- `//cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate`: a recycled-content certificate in a customs declaration — refuted because recycled content can matter for the Trade Accord or plastic levies, so it is not clearly without use.
