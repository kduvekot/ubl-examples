# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### plastics/05#F1 · Medium · Province of Ferrano in `Region` instead of `CountrySubentity`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is an administrative division of Urvania, so it belongs in `CountrySubentity` (with `CountrySubentityCode` if Urvania has a list), not in `Region`. The Bayvarran addresses of the same flow do it that way (`CountrySubentity` = `Coastal State`). The same `Region` value occurs in 104 of the 250 examples (`grep -rl --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address in this example carries the province in `Region`; where the province is given, it is in `CountrySubentity`.
- Options: (a) move the value to `CountrySubentity` (preferred: it is what the element is for, and it matches the Bayvarran addresses); (b) drop it where the postal code already identifies the place.
- Needs decision: no

### plastics/05#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; the language itself is `Language/ID`. The value `en` with `listID` `ISO 639` repeats the language code from `Language/ID` instead of naming a locale (a language plus a region, such as the Bayvarran variant the example itself writes as `en-XB`). The same value occurs in 213 of the 250 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<'`).
- Condition: Every `LocaleCode` holds a locale identifier from a locale list (e.g. a BCP 47 tag such as `en-XB`) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` (preferred unless the locale matters to the receiver: the language is already in `Language/ID`); (b) set it to the locale (`en-XB`) with a locale list as `listID`.
- Needs decision: no

### plastics/05#F3 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyIdentification/cbc:ID` = `XU-R-105507`
- Why: `CustomsParty` is "The Authority who processes this Customs Declaration": the Customs Administration of Urvania, a public body. Its legal entity says it is registered in the "Commercial register of Urvania" (type `COMMERCIAL`) and gives a company liquidation status ("A code signifying the party's liquidation status", `ACTIVE`, "Active, not in liquidation"). A state administration is created by law, is not entered in a commercial register and cannot be liquidated like a company (checklist: a public body is not a company in a commercial register and has no liquidation status). Its identifier uses the commercial-register scheme for the same reason.
- Condition: The customs authority's legal entity carries no company liquidation status and no commercial-register registration; if it is identified, the identifier comes from a scheme for public bodies.
- Options: (a) reduce the legal entity to the registration name (or drop it) and identify the authority by a public-body scheme (preferred); (b) if Urvania does register public bodies in a register, use a scheme of type other than `COMMERCIAL` and drop the liquidation status.
- Needs decision: no

### plastics/05#F4 · Low · Contacts do not fit the role the party has in this document
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's `Contact` fits its role. The parties carry one generic contact in every document of the flow: Rinova's "Customer service" in Sales, Rivermouth's "Order desk" with job title "Customer service officer" in Sales (a buyer's order desk is not a sales department), and Fiumella's "Chartering desk" in Operations. In this document `/ExportCustomsDeclaration/cac:ExporterParty` is the exporter that customs contacts about the declaration (export or customs); `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty` is the consignee that receives the goods (goods receiving). The contacts shown are the ones for a different task.
- Condition: Each contact listed above is one that handles the task the party has in this document (or is absent where the document needs no contact for that party).
- Options: (a) give each party role-specific contacts and use the one for the role (preferred: it is what `Contact` is for); (b) drop the contact where the document does not need one.
- Needs decision: no

### plastics/05#F5 · Low · Rivermouth's bank account copied into a document that does not use it
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". Section 4.8 of the review rules: a bank account of a party that pays or receives nothing under this document is data copied from master data. The Urvanian export declaration does not involve a payment by the consignee.
- Condition: Rivermouth's party in this document carries no `FinancialAccount`, unless the document gets a purpose for it.
- Options: (a) drop the account from the party (preferred); (b) keep it only where a payment by Rivermouth is part of this document.
- Needs decision: no

### plastics/05#F6 · Low · Rinova's waste-recovery permit carried in a document about a non-waste product
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: `Party/PartyAuthorization` is "An authorization issued to this party". The permit (Basel Annex IV R3, "Recovery of non-hazardous plastic waste") authorises Rinova to operate its recovery plant. The goods of the flow are recycled PE granulate classified as a product (HS `390110`, polyethylene in primary forms, not HS 3915 waste), so no step of this flow carries waste. Nothing in this document refers to the permit, so it looks copied from Rinova's master data. It could be argued that the permit supports the recycled-content claim, but that claim has its own `EnvironmentalCertificate` on the item where the document has an item.
- Condition: Rinova's party carries the permit only in documents whose purpose needs it, or the document states why it is there.
- Options: (a) drop it here (preferred if the granulate is a product, as the HS code says); (b) keep it and make its purpose explicit if the story wants the buyer or the authorities to see that the granulate comes from a licensed recovery plant.
- Needs decision: yes

### plastics/05#F7 · Low · Registration date 1996-01-01 looks like a default value
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Every company in this example (`20412740`, `XU-R-104548`, `XU-R-104959`) is registered on 1 January 1996, a public holiday on which registers do not normally register companies. The same date occurs in 181 of the 250 examples, for at least 24 unrelated companies (counted with `grep -rl --include='*.xml' 'RegistrationDate>1996-01-01'` and the `RegistrationName` before it), while some other parties have specific dates (e.g. `1962-04-12`, `1988-10-03`). Under the no-filler rule a value needs a reason in the world.
- Condition: Each company's `RegistrationDate` is a date that belongs to that company's history, or the element is absent.
- Options: (a) give each company its own registration date from its history (preferred); (b) drop `RegistrationDate` where no history is known.
- Needs decision: no

### plastics/05#F8 · Low · Italian text tagged as English
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Banchina del Fiume`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- Why: The checklist asks that each repeated rendering is in the language its `languageID` names. The second renderings of Urvanian street names are Italian ("Via del Riciclo" is "Recycling street", "Banchina del Fiume" "River quay", "Piazza della Banca" "Bank square", "Valico di Confine" "Border crossing"), and the English legal form is Italian with an English gloss, while they are tagged `en-XU` or `en-XB` (or, for `CompanyLegalForm` without a tag, sit in a document whose other texts are English). Bayvarran streets in the same flow are English (`Estuary Road`, `Exchange Street`). If the world gives Urvanian places Italianate names as their English exonyms (as `Ferrano` for `Ruldraz`), that convention is not visible in the documents; the same pattern occurs in 101 of the 250 examples (`grep -rlE --include='*.xml' 'languageID="en-X[UB]">(Via|Banchina|Piazza|Valico|Società)'`).
- Condition: Every rendering tagged `en-…` is English (or a proper name used as such in English), and Italian text, if the world has it, carries an Italian tag or none.
- Options: (a) translate the renderings into English ("Recycling Street", "River Quay") (preferred if English is meant); (b) if the Italianate forms are the world's official exonyms, record that in the world's story and keep them; (c) drop the second rendering where the local form suffices.
- Needs decision: yes

### plastics/05#F9 · Low · Chamber of commerce as issuer of a recycled-content certificate
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: `EnvironmentalCertificate/IssuerParty` is "The authorised Organisation who issues this Certificate". In the world the Ferrano Chamber of Commerce issues certificates of origin and ATA carnets (`road/06-CertificateOfOrigin.xml`, `carnet/01-GoodsItemPassport.xml`). Verifying recycled content (the share of recovered material in a product) is normally done by an accredited certification body or the environment authority that supervises the recovery plant, not by a chamber of commerce (own knowledge of recycled-content schemes). The remark "Made entirely from sorted production waste recovered in Urvania" reads like an origin statement, which would fit the chamber, but the certificate type is `RECYCLED`.
- Condition: The issuer of the recycled-content certificate is an organisation the world authorises to certify recycled content, or the certificate is a kind the chamber issues.
- Options: (a) name a certification body or the Urvanian environment authority as issuer (preferred); (b) keep the chamber and record in the world why it certifies recycled content.
- Needs decision: yes

### plastics/05#F10 · Low · Customs authority's VAT registration copied into the declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The declaration is processed by customs; the authority's own VAT registration plays no part in it (it neither supplies nor buys anything here). Data that looks copied from a party's master data into a document that does not use it is a finding (section 4.8).
- Condition: The customs party carries no `PartyTaxScheme` in this declaration, unless the declaration uses it.
- Options: (a) drop it (preferred); (b) keep it only with a reason in the document.
- Needs decision: no

## Checked and consistent
- Exporter, consignor and signatory Rinova (with its Urvanian customs-trader ID `XU-TR-104548`), consignee Rivermouth (with its Bayvarran customs-trader ID), carrier Fiumella and the Customs Administration of Urvania (ISIC `8411`, which covers the collection of duties) fit an export declaration lodged by the exporter.
- Every party that appears in several documents of the flow was compared field by field (script over all `*.xml` of the flow): Rinova Recovery (`XU-R-104548`), Rivermouth Packaging (`20412740`), Fiumella Barges (`XU-R-104959`) and the Ferrano Chamber of Commerce (`XU-R-105370`) carry the same identifiers, names, tax registrations, legal entities, addresses, contacts and electronic addresses everywhere, apart from the language renderings noted in the findings.
- `check_ids.py`: every IBAN-like account and RF reference in the example passes its check digits (where present).
- Industry classifications fit the parties: Rinova `3830` (materials recovery), Rivermouth `2220` (manufacture of plastics products), Fiumella `5022` (inland freight water transport), customs `8411`.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: an ISO 6523 identifier with ICD `0990` could clash with a real ICD — refuted because the ICDs assigned in the real ISO 6523 register are four-digit codes far below 0990 (own knowledge: the register runs to the 02xx range), so `0990` is free and stands for the world's identification agency.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped bank identifier (`BLUMXBLX`) could be a real BIC — refuted because positions 5–6 carry the user-assigned ISO 3166 code of a fictional country (`XB`/`XU`), which no real BIC uses.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox`: a postal address (`AddressTypeCode` `POSTAL`) with both a post box and a street and building number — refuted because a post-box address may name the delivery office's street; nothing contradicts it.
- `/ExportCustomsDeclaration/cac:ExporterParty`: no separate declarant — refuted because the exporter lodges and signs the declaration itself (`/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Rinova Recovery`).
