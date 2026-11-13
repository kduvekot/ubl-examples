# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/15#F1 · Medium · Shipment gross weight without the container
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment"; the goods item's is "including packing and packaging but excluding the carrier's equipment". The same 6190.29 kg in both, for a shipment that arrived in container TWLU4123110 with a verified gross mass of 9940.29 kg (12: 6190.29 + 3750 tare). Customs practice declares the gross mass without the container; under the agreed rule of semantic conformance the UBL definition applies. Medium, as in 11 and 13 (logistics had Low): not High, because this declaration names no equipment.
- Condition: the shipment gross weight includes the container, or only the goods-item gross weight is given.
- Options: (a, preferred) drop the shipment gross weight; (b) 9940.29 kg with the container declared.
- Needs decision: no
- From: broad (F1), logistics (F3)

### cotton/15#F2 · Medium · The customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Customs and Border Service of Bayvarra is a public authority (ISIC `8411`). `CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `CompanyLiquidationStatusCode` the party's liquidation status: a government agency is not registered in a commercial companies register and cannot be in liquidation. The values contradict the party's own classification. All 7 example files that give this authority's `RegistrationName` carry a liquidation status (parties' count over *.xml).
- Condition: the authority's legal entity carries no commercial registration scheme and no liquidation status; an identifier, if any, is from a register of public bodies.
- Options: (a, preferred) keep only `RegistrationName` (and a public-body register identifier, if the world has one); (b) drop the authority's `PartyLegalEntity`.
- Needs decision: no
- From: parties (F1)

### cotton/15#F3 · Medium · Language code in `LocaleCode`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F2), parties (F2)

### cotton/15#F4 · Low · Customs value is the FOB value; the sea freight to Lumeport is not in it
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`
- XPath: `16-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `2950.00`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". Recalculated: 6055.452 XLC / 0.4 XLC per XBL = 15138.63 XBL, exactly the FOB invoice value (16) at the port of Selanu. The goods were bought FOB (08), and the mill pays 2950.00 XBL for the port-to-port sea freight (17). Under the WTO Valuation Agreement (Art. 8.2, own knowledge) each member decides whether the cost of transport to the place of importation is included; most value CIF, some FOB. With a CIF rule the value would be 15138.63 + 2950.00 = 18088.63 XBL (plus insurance, if any; none appears in the flow). The declaration does not state its basis, and the flow does not show Bayvarra's rule (context refuted it for its lens on that ground).
- Condition: the customs value follows Bayvarra's valuation basis, recorded in the world: the FOB value if Bayvarra values FOB, or FOB plus freight (and insurance) to Lumeport if it values CIF.
- Options: (a) keep 15138.63 XBL and record that Bayvarra values imports FOB; (b) declare 18088.63 XBL under a CIF rule. No preference without the rule (money); broad leans to deciding the rule first.
- Needs decision: yes
- From: broad (F3), money (F1); context (considered, refuted for its lens)

### cotton/15#F5 · Low · `PackQuantity` 1 / `PackSizeNumeric` 227: the nominal bale weight as a pack size
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count; 227 is the nominal bale weight in kilograms. Logistics and context read it as a weight in a count element (Medium). Counter-argument (merge): the item is declared per kilogram (`Quantity` 6129 KGM), so "227 one-kilogram units per pack" is a possible reading of the definition, though the bales are only "about" 227 kg. Cannot be settled from the definition alone. Same in 02, 07, 08, 10, 11 and 16.
- Condition: the pack elements, where present, state a count whose unit is clear; otherwise the bale weight is carried where a weight belongs, and the bale count as in F6.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric`, with the nominal bale weight as an item property if needed; (b) keep them and record the reading as a convention.
- Needs decision: yes
- From: logistics (F1), context (F1), broad (F8)

### cotton/15#F6 · Low · The number of bales is not declared
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- Why: an import declaration normally states the number and kind of packages (own knowledge of customs data models); only the net kilograms are given, not the 27 bales (6129 / 227 = 27).
- Condition: the declaration states the number of bales as a package count.
- Options: (a, preferred) a package of the goods item with `Quantity` 27 and a bale packaging type.
- Needs decision: no
- From: broad (F5), logistics (inside F1)

### cotton/15#F7 · Low · The phytosanitary certificate made out for Bayvarra is not presented with the import
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cbc:ID` = `SCC-GC-26-0202`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cbc:Description` = `The ginned cotton is free of the pests named by Bayvarra's plant health rules.`
- Why: the certificate 10 exists because Bayvarra's plant-health rules require it for this lint; it is valid in XB until 2026-03-14, covers this shipment and names the mill as importer. The import declaration for release into free circulation, made on 2026-03-06 within that validity, refers only to the bill of lading; the certificate the release depends on is not referenced, so nothing in the flow uses it at import.
- Condition: the import declaration refers to SCC-GC-26-0202 with its document type, or the flow shows another way it is presented to the Bayvarran authorities.
- Options: (a, preferred) an `AdditionalDocumentReference` to SCC-GC-26-0202 with its type.
- Needs decision: no
- From: broad (F5), logistics (F2), context (F3)

### cotton/15#F8 · Low · The Lisavan exit office instead of Bayvarra's office of entry
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Selanu`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: the declaration applies in Bayvarra and is processed by the Customs and Border Service of Bayvarra. `CustomsExitOfficeLocation` ("Customs exit office of the goods being declared") names the Lisavan office at the port of Selanu, an office of another administration that plays no part in Bayvarra's release; the office where the goods enter and are declared, at Lumeport, is not given.
- Condition: the offices named in the import declaration are those of Bayvarra's procedure (entry and declaration at Lumeport); the Lisavan exit office only if Bayvarra's procedure needs it.
- Options: (a, preferred) leave the exit office out and give the Lumeport customs office (as a location of the shipment, or the customs party's address, see F9).
- Needs decision: no
- From: broad (F4), context (F2, office part)

### cotton/15#F9 · Low · An inland border office's address and contact for a sea import at Lumeport
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName` = `Border Crossing Road`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CityName` = `Marrowdale`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- Why: the customs party is "The Authority who is legally responsible for processing the Declaration." The bales arrive by sea at Lumeport in the Coastal State (13, 14); the authority is given the address and contact of a border office in Marrowdale, Upland State. As a contact for this declaration the border office does not fit. The same address is used in every example that gives this authority an address (7 of the 8 files naming it, parties' count over *.xml), so it may be meant as the service's head office, which is story.
- Condition: the customs party's address and contact are those of the office handling imports at the port of Lumeport, or explicitly the head office with a contact that handles this declaration.
- Options: (a, preferred) the customs office at the port of Lumeport with an import contact; (b) keep the head-office address, rename the contact to an import or clearance office, and record the head office in the story.
- Needs decision: yes
- From: parties (F3)

### cotton/15#F10 · Low · The Lisavan export declaration cited as the previous customs declaration of this import
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`
- XPath: `11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`
- Why: context: `PreviousCustomsDeclaration` ("A reference to a previously sent customs declaration") here cites the export declaration of another declarant to another administration, not a previous declaration of this import procedure (such as a summary or temporary-storage declaration); it would be a supporting document. Logistics (and broad, listing it as consistent) refuted it: the definition does not restrict it to the importing country, and the export declaration is the previous customs declaration of these goods. The definition allows both readings.
- Condition: the reference is the previous declaration of the procedure the world intends; if it is the export declaration, that reading is recorded.
- Options: (a, context's preference) move SCG-CD-26-0204 to an `AdditionalDocumentReference` typed as the export declaration; (b) keep it as previous declaration (logistics).
- Needs decision: yes
- From: context (F2, previous-declaration part); refuted by logistics (argument carried)

### cotton/15#F11 · Low · Classing results carried as the applicant's remarks
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for this certificate"; the text is the classer's result, and grade and staple are already item properties of the same item.
- Condition: the classing result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark.
- Needs decision: no
- From: broad (F6)

### cotton/15#F12 · Low · Origin area in `Region` here, in `District` in the farm's address
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: the same area is a `District` in the farm's address and a `Region` here; a consistency remark.
- Condition: the north coast is in the same address element wherever it occurs in the flow.
- Options: (a, preferred) `District` in the origin address.
- Needs decision: no
- From: broad (F7), context (F4)

### cotton/15#F13 · Low · The importer's contact: Purchasing, Customer service officer, Sales
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: the mill makes its own import declaration; customs questions go to its import or customs desk, and name (buying) and job title and department (selling) contradict each other. The combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: name, job title and department agree and fit the importer role.
- Options: (a, preferred) an import / customs desk contact; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F9), parties (F4)

### cotton/15#F14 · Low · The ginnery's Lisavan address parts tagged as Bayvarran English
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: tagged `en-XB` here, `en-XL` in the documents Lisavan parties issue; counted over *.xml, en-XB in the seven Bayvarran-issued examples 02, 07, 08, 09, 13, 15, 18, en-XL in the other nine. Parties: `languageID` describes the text, so these are Lisavan English names whoever sends the document. The pattern is consistent with "the tag follows the issuer's English", a convention earlier flows could not settle either.
- Condition: one rule for the tags of the same party's renderings, applied in every example and documented.
- Options: (a, preferred) the ginnery's own tags (en-XL) everywhere; (b) if tags follow the issuer, record the rule.
- Needs decision: yes
- From: parties (F5, address part)

### cotton/15#F15 · Low · Single untagged renderings of the ginnery's legal form and of the certificate type
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:CertificateType` = `Cotton classing`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: elsewhere the ginnery's legal form is given in Lisavan and English with language tags (01), and the classing certificate's type in Lisavan and English (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:CertificateType[1]` = `Tekapa vekona`); here each has one English rendering without `languageID`. The same party and certificate are described in two ways in the flow. (The certificate type was added by the merge.)
- Condition: the legal form and the certificate type carry the same renderings and tags in every example.
- Options: (a, preferred) both renderings with their tags, as in 01 and 11.
- Needs decision: no
- From: parties (F5, legal-form part); merge (certificate type)

### cotton/15#F16 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Mill and ginnery, in two registers, share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F6)

### cotton/15#F17 · Low · Signature ID built from the flow name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LTM-SIG-IM-cotton`
- Why: the mill's signature identifier ends in the name of the example flow ("cotton"), which exists in the repository, not in the world. No part raised it; added by the merge for alignment with earlier flows and with cotton/11#F14 and cotton/13#F14 (8 files with the pattern over all flows, `grep -rl --include='*.xml' 'SIG-[A-Z]*-\(cotton\|road\|rail\|sea\|air\)<'`).
- Condition: the signature ID is an identifier of the signer's own numbering, with no flow name in it.
- Options: (a, preferred) an ID in the mill's signature series (its forwarding instructions use LTM-SIG-FI-09, itself numbered after the example).
- Needs decision: no
- From: merge

## Checked and consistent
- 6055.452 XLC / 0.4 = 15138.63 XBL (XLC → XBL × 2.5), the rate of 04, 05, 09 and 13; the export value in 11 and the certificate value in 10 are the same 6055.452 XLC.
- `PreviousCustomsDeclaration` SCG-CD-26-0204 is the customs declaration of 11; the exit office name is the same as in 11; `AdditionalDocumentReference` TOL-BL-26-0206 resolves to 13.
- Issued 2026-03-06, after the bill of lading (2026-03-02) and the pre-arrival report (2026-03-03), within the validity of the phytosanitary certificate (to 2026-03-14); declaration valid 30 days.
- Shipment SCG-SH-26-0200, goods description, quantity 6129 kg and goods-item gross weight 6190.29 kg agree with 10, 11 and 13; type IMPORT, subtype FREECIRC and nature PURCHASE fit the sale of 08/16.
- Importer, consignee, notifier and signatory are the mill (20412603), which declares its own import; consignor the ginnery; both customs-trader numbers and the importer's sales-tax registration have a use in an import declaration (money, parties). The mill's description is identical to 10.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:NotifierParty`: the importer also as notifier — refuted: "The Party who is responsible for contact on master level" may be the importer itself, and it states who customs contacts (from broad, parties).
- `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`: a note on duties without duty amounts — refuted because the import declaration has no element for assessed duties; the declaration states how duties are paid, customs assesses them (from broad, money, context).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`: an FOB value as import value — refuted by context for its lens (WTO Art. 8.2 leaves the choice to each member); broad and money kept it, so it is F4 with "Needs decision: yes".
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `SCG-CD-26-0204`: an export declaration of another country as previous declaration — refuted by logistics (definition not restricted); context kept it, so it is F10 with both arguments.

## Changed in the merge
- logistics/F3 (Low) + broad/F1 (Medium) → F1: Medium, aligned with cotton/11#F1 and cotton/13#F4.
- logistics/F1, context/F1 (Medium) + broad/F8 (Low) → F5: Low with "Needs decision: yes" (item traded per kilogram; same as cotton/10#F7).
- broad/F5 split into F6 (bale count) and F7 (phytosanitary certificate, with logistics/F2 and context/F3).
- context/F2 split into F8 (exit office, with broad/F4) and F10 (previous declaration, Low/yes because logistics refuted it).
- parties/F5 split into F14 (tags, "Needs decision" changed from no to yes, as in cotton/13#F11) and F15 (untagged legal form, Low/no; the untagged certificate type added by the merge as a second place of the same problem).
- F17 added by the merge.
- broad's "as cotton/02#F…" findings written out in full (F3, F5, F11, F12, F13).
