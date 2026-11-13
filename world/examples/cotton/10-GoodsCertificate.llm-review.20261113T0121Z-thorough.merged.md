# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/10-GoodsCertificate.xml`, Git blob `a573492644f6156f64f31e963d3578b9c5d69634` (committed)
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

### cotton/10#F1 · High · "10 bales sampled out of 80" for a shipment of 27 bales
- XPath: `/GoodsCertificate/cac:Attestation/cbc:Note` = `10 bales sampled out of 80.`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- XPath: `/GoodsCertificate/cac:Attestation/cac:AttestationLine/cac:CriterionItem/cbc:CriterionDescription` = `No live insects in a sample of 10 bales.`
- Why: the certificate covers shipment SCG-SH-26-0200, one goods item of 6129 kg of lint in bales of about 227 kg. Recalculated: 6129 / 227 = 27.0, so 27 bales (27 × 227 = 6129), the quantity of the order (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `6129`). The attestation says 10 of 80 bales were sampled; 80 bales would be 80 × 227 = 18160 kg, three times the certified quantity. It is also more lint than the flow's seed cotton can give: 18000 kg of seed cotton were delivered to the gin (`03-DeliveryNote.xml:/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000`), and at a lint turnout of about 35 % (own knowledge) that gives about 6300 kg, i.e. the 27 bales. Refutation tried: the gin may have held 80 bales of several farms' lint and sampled the whole lot; but then the certificate does not say so, does not identify the lot, and certifies 27 bales on a sample statement about another quantity.
- Condition: the number of bales the attestation sampled from is the number of bales of the certified shipment (27), or the attestation says that the shipment was drawn from a larger inspected lot and identifies it.
- Options: (a, preferred) "10 bales sampled out of 27" (or the sample size the rule XB-PH-07 sets for 27 bales, with the criterion text adapted); (b) keep 80 and describe the inspected lot that includes the 27 bales.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### cotton/10#F2 · High · Version 1 with a "previous version" from last season
- XPath: `/GoodsCertificate/cbc:VersionID` = `1`
- XPath: `/GoodsCertificate/cac:PreviousDocumentReference/cbc:ID` = `SCC-PH-25-0198`
- Why: `PreviousDocumentReference` is "A reference to the previous version of the goods certificate"; `VersionID` "Identifies the current version of this goods certificate". Version 1 has no previous version. The referenced ID, a 2025 number in the chamber's phytosanitary series (SCC-PH-25-…), reads as last season's certificate for another shipment, not an earlier version of this one. No example of the flow carries that ID (`grep -rn --include='*.xml' 'SCC-PH-25'` finds only this file).
- Condition: `PreviousDocumentReference` is present only for a later version of the certificate, and then points to the earlier version of this same certificate; `VersionID` agrees.
- Options: (a, preferred) drop the reference; if last season's certificate matters, cite it as an `AdditionalDocumentReference` with a type or description that says what it is; (b) make this version 2 of a certificate whose version 1 was SCC-PH-25-0198 (unlikely across seasons).
- Needs decision: no
- From: broad (F1), logistics (F2), context (F2)

### cotton/10#F3 · High · The classing certificate given as the "original version" of the phytosanitary certificate
- XPath: `/GoodsCertificate/cac:OriginalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:CertificateTypeCode` = `COTTONCLASS`
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- Why: `OriginalDocumentReference` is "A reference to the original version of the goods certificate". The same document says, in the item's `Certificate`, that XL-CLS-2026-0042 is a cotton classing certificate (`COTTONCLASS`), a different certificate of another kind, and that this phytosanitary certificate is itself at version 1, i.e. its own original. The reference contradicts two other values of the example.
- Condition: `OriginalDocumentReference`, if present, refers to the first version of this phytosanitary certificate and the certificate is at a later version; the classing certificate is cited only where certificates of the item belong.
- Options: (a, preferred) drop `OriginalDocumentReference`; the classing certificate is already in the item (whether it belongs there at all: F12).
- Needs decision: no
- From: broad (F1, grouped there with the previous version), logistics (F3), context (F3)

### cotton/10#F4 · Medium · A phytosanitary certificate issued by a chamber of commerce and sanctioned by customs
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:IssuerParty/cbc:IndustryClassificationCode` = `9411`
- XPath: `/GoodsCertificate/cac:Attestation/cac:IssuerParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/GoodsCertificate/cac:LegalAuthorityParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: `PHYTO` means "Plants or plant products are free of the pests the importing country names" (world list). Under the International Plant Protection Convention (Art. IV and V; ISPM 12, own knowledge) phytosanitary certificates are issued only by the exporting country's national plant protection organisation, a public authority, or by officers it authorises. Here issuer, attestation issuer and signatory are the Selanu Chamber of Commerce, a business membership organisation (ISIC `9411`); and `LegalAuthorityParty`, "The legal Authority, when different from the issuer, who sanctions this Goods Certificate", is the island's customs service, which has no plant-health competence. A chamber issues certificates of origin, and its cotton classing (XL-CLS-2026-0042) is a commercial quality service. Neither party fits its role.
- Condition: the issuer of the phytosanitary certificate, or the legal authority sanctioning it, is Lisavu's plant protection authority (or a body the story makes responsible for plant health).
- Options: (a, preferred) a Lisavan plant protection service as issuer and signatory, without a separate legal authority (adding the party to the world); (b) the plant protection service as legal authority, with the chamber as issuer only if the story delegates inspection to it; (c) change the certificate type to one a chamber issues, which changes what the document attests.
- Needs decision: yes (who is responsible for plant health in Lisavu is part of the world)
- From: broad (F3), parties (F1), context (F4)

### cotton/10#F5 · Medium · Language code in `LocaleCode`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` used as `languageID` elsewhere). Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) a locale such as `en-XB` with a locale list (BCP 47).
- Needs decision: no
- From: broad (F5), parties (F2)

### cotton/10#F6 · Low · No number of bales on a certificate based on bale sampling
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Description` = `Cotton lint, compressed bale`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- Why: the certificate attests freedom from pests by sampling bales, but states nowhere as a count how many bales it covers (no package or handling-unit quantity); the importing authority cannot check the sample against the consignment. The 27 is only derivable from 6129 kg and "about 227 kg".
- Condition: the number of bales certified is stated as a count.
- Options: (a, preferred) a package of the goods item with `Quantity` 27 and a bale packaging type.
- Needs decision: no
- From: broad (F6); logistics (inside F4)

### cotton/10#F7 · Low · `PackQuantity` 1 / `PackSizeNumeric` 227: the nominal bale weight as a pack size
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackQuantity` = `1`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "The number of items in a pack of this item", a count; 227 is the nominal bale weight in kilograms ("bales of about 227 kg"). Logistics reads it as a weight in a count element (Medium). Counter-argument (merge): the item is traded per kilogram (`KGM` quantities and a base quantity of 1 KGM in 08 and 16), so "227 units of the item in one pack" is a possible reading of the definition, though bales vary in weight and the pack size is only "about". Neither reading can be settled from the definition alone.
- Condition: the pack elements, where present, state a count whose unit is clear; otherwise the bale weight is carried where a weight belongs (an item property), and the bale count as in F6.
- Options: (a, preferred) drop `PackQuantity`/`PackSizeNumeric` and count the bales (F6), with the nominal bale weight as an item property; (b) keep them and record the reading (pack of 227 one-kilogram units) as a convention.
- Needs decision: yes
- From: logistics (F4), broad (F9)

### cotton/10#F8 · Low · Classing certificate signed before the pressing of the lot ended
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- Why: the classing of the lint is signed (`ValidationDate`, "The date upon which this signature was verified", which cannot be earlier than the signing) on 2026-02-20; according to this certificate the ginning and pressing of the lint ran until 2026-02-22. A classing certificate cannot cover bales pressed after it was signed. It only partly survives: the 27 bales of this shipment may have been pressed before 20 February and the processing period may cover the whole season's ginning, which the certificate does not say; hence Low.
- Condition: the classing of the shipment's lint is dated on or after the end of the pressing of its bales, or the processing period ends before it.
- Options: (a, preferred) end the processing period on or before 2026-02-20 (18000 kg of seed cotton in two weeks is slow for a gin anyway); (b) date the classing after 2026-02-22.
- Needs decision: no
- From: logistics (F5)

### cotton/10#F9 · Low · Customs value, importer's tax registration and classing certificate in a phytosanitary certificate
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `6055.452`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods item". The certificate attests freedom from pests; it assesses nothing on value, bills nothing, assesses no tax and does nothing with the commercial grade. The customs value belongs in the declarations 11 and 15 (where it is declared), the mill's Coastal State sales-tax registration in documents that tax, the classing certificate in the order and the invoice where the grade is the quality basis. In the certificate they read as master and item data copied in (section 4.8, no fillers). The values themselves are correct (6055.452 XLC = the order and invoice value).
- Condition: the certificate carries only data its attestation or fee uses.
- Options: (a, preferred) drop the customs value, the importer's `PartyTaxScheme` and the item's classing `Certificate`.
- Needs decision: no
- From: money (F1, F2), context (F5, customs value and classing certificate)

### cotton/10#F10 · Low · Classing results carried as the applicant's remarks
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Certificate/Remarks` is "Remarks by the applicant for the certificate". The text is the classer's result, not a remark of the applicant; grade and staple are also already in the item's `AdditionalItemProperty` (Grade `Middling`, staple 28.6 mm = 1-1/8 inch). Micronaire appears only here.
- Condition: the classing result is not carried as an applicant's remark.
- Options: (a, preferred) drop the remark (and add micronaire as an item property where it is needed); (b) a remark that really is the applicant's.
- Needs decision: no
- From: broad (F7)

### cotton/10#F11 · Low · Origin area in `Region` here, in `District` in the farm's address
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: the north coast of Lisavu is given as `Region` here, while the farm's address in the same flow has it as `District` (`03-DeliveryNote.xml:/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`). UBL's `District` is "The district or division of a country, region, or county in which this address is located"; `Region` can be read as a geographic region, so this is a consistency remark. 13 files carry "North coast" (`grep -rc --include='*.xml' 'North coast'`), 7 as Region.
- Condition: the north coast is in the same element everywhere.
- Options: (a, preferred) `District`, as in the farm's address.
- Needs decision: no
- From: broad (F8)

### cotton/10#F12 · Low · The importer's contact: Purchasing, Customer service officer, Sales
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: the name says buying, job title and department say selling: the three do not describe one contact, and for the importer named on a plant-health certificate the import or goods-receiving desk would fit the role. The same combination (a contact named Purchasing in department Sales) is in 52 example files (parties' count, `grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: name, job title and department agree with each other and with the importer role.
- Options: (a, preferred) an import / goods-in contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no
- From: broad (F10), parties (F5)

### cotton/10#F13 · Low · The issuer's contact is its carnet office
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:Contact/cbc:Name` = `Carnet office`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `carnet@chamber-selanu.example`
- Why: the contact of the party issuing a plant-health certificate is its desk for ATA carnets (temporary admission), which has nothing to do with this certificate or with the inspection at the ginnery's warehouse.
- Condition: the issuer's contact is the office responsible for the certificate (plant-health inspection or certification).
- Options: (a, preferred) the issuing body's inspection or certification office (follows F4); (b) drop the contact.
- Needs decision: no
- From: parties (F3); broad (evidence in F3)

### cotton/10#F14 · Low · The chamber of commerce described as a company in the commercial register
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/GoodsCertificate/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: a chamber of commerce is a membership body, in many countries one under public law; here it has no legal form or size but is registered in the island companies register as `COMMERCIAL` with a liquidation status. Whether the Selanu chamber is a public-law body or a registered association is a question of the world's story (as for the chamber in road).
- Condition: the chamber's legal entity describes the kind of body it is in the world, with a registration scheme of that kind and a liquidation status only if it can be liquidated as a company.
- Options: (a, preferred) decide the chamber's legal status in the story and describe it accordingly; (b) keep it if the world's chambers are companies, and give a legal form.
- Needs decision: yes
- From: parties (F4)

### cotton/10#F15 · Low · A freight forwarder named on a phytosanitary certificate
- XPath: `/GoodsCertificate/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: parties: the certificate attests the plant health of the bales for the importing country and does nothing with the forwarder that books the carriage (section 4.8). Broad and context refuted it: naming the forwarder that receives the original certificate and handles it for the shipment it books is common practice. The merge cannot settle whether the story gives the forwarder a role in the certificate; the definition of `FreightForwarderParty` gives none.
- Condition: the certificate names only parties it has a use for, or the forwarder's use is evident (e.g. as the party that receives the certificate).
- Options: (a, preferred) drop the forwarder; (b) keep it with a stated role (e.g. it receives and forwards the certificate).
- Needs decision: yes
- From: parties (F6); refuted by broad and context (their arguments carried here)

### cotton/10#F16 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/GoodsCertificate/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." The ginnery and the mill, in two different registers (`XL:ICR`, `XB:FBR`), are both registered on 1 January 1996; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other. That looks like a default rather than each company's history (no fillers). It may be deliberate (a register-wide date), which the examples cannot show.
- Condition: each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop it where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the story.
- Needs decision: yes
- From: parties (F7)

### cotton/10#F17 · Low · Criterion type code `PROCESSING` adds nothing to the criterion
- XPath: `/GoodsCertificate/cac:GoodsProcessing/cac:CriterionItem/cbc:TypeCode` = `PROCESSING`
- Why: `CriterionItem/TypeCode` is "A code describing the type of criteria". The code is from the goods-processing type list, which also holds the processing kinds GINNING and PRESSING used in this same aggregate. Broad read this as a code from another element's list (Medium). The merge checked the code's meaning in the world list: "Processing in general, as a criterion names it", i.e. the list provides it for criteria, so the code is not taken from a list meant only for another element. What remains (context): the code says only "processing", which the description "Seed removed; lint only." already says, and one list mixes kinds of processing with a criterion type.
- Condition: the criterion type code, if present, distinguishes this criterion from other types of criteria.
- Options: (a, preferred) drop the type code; (b) a criterion type list if criteria of several types are needed.
- Needs decision: no
- From: broad (F4, Medium), context (F5, code part)

## Checked and consistent
- 6129 / 227 = 27 bales; goods-item gross 6190.29 kg = 6129 kg + 61.29 kg packaging (2.27 kg per bale), the same as in 11 and 15; "excluding the carrier's equipment" fits the goods-item gross weight.
- Declared value 6055.452 XLC is the order and invoice value (08, 16), and at 0.4 XLC per XBL the 15138.63 XBL of 15 (6055.452 / 0.4 = 15138.63).
- Validity 2026-02-28 to 2026-03-14 covers the bill of lading (2026-03-02, 13) and the import declaration (2026-03-06, 15); the attestation ends on the same day.
- Ginning starts on 2026-02-07, after the seed-cotton delivery on 2026-02-05 (03); "Seed removed; lint only" fits HS 5201 (HS section XI).
- Applicable territory XB is the importing country of 08 and 15; the rule XB-PH-07 is a Bayvarran rule; attestation lines (boll weevil, pink bollworm) agree with the attestation's description.
- Shipment SCG-SH-26-0200 is the shipment of 09, 11, 12, 13 and 15; `AdditionalDocumentReference` LTM-PO-26-0198 resolves to the order 08.
- Exporter, consignor, applicant, warehouse and processing party are the ginnery (IC42681); importer and consignee the mill; their full descriptions are identical to 11 and 15 (parties, block by block). Issuer, attestation issuer and signatory are the same party (IC42133).

## Considered and refuted
- `/GoodsCertificate/cac:WarehouseParty`: the ginnery as warehouse, a duplicate of the exporter — refuted because the note says the bales were inspected at the ginnery's warehouse (from broad, parties).
- `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129` with unit KGM: a weight in "the number of units making up this goods item" — refuted because the element is a quantity with a unit code, and kilograms are a legitimate quantity of bulk goods (from logistics).
- `/GoodsCertificate/cac:AdditionalDocumentReference/cbc:ID` = `LTM-PO-26-0198`: the buyer's order unused in a plant-health certificate — refuted because such certificates are often tied to the commercial transaction for the importing authority, and the order resolves to 08 (from context).
- `/GoodsCertificate/cac:FreightForwarderParty`: refuted by broad and context (forwarder handles the certificate); parties made it a finding, so it is kept as F15 with both arguments.

## Changed in the merge
- broad/F1 → F2 and F3: split into the previous-version reference and the original-version reference, because the original reference also contradicts the item's own `Certificate` (classing); both High.
- logistics/F3, context/F3 → F3: Medium raised to High (broad's severity), because the reference contradicts `VersionID` 1 and the item's certificate type in the same document (section 6).
- logistics/F4 → F7: Medium lowered to Low with "Needs decision: yes", because the item is traded per kilogram, which makes "227 one-kilogram units per pack" a possible reading of the definition; the missing bale count is split off as F6 (broad's own finding).
- broad/F4 (Medium) + context/F5 code part → F17: lowered to Low, because the world list defines `PROCESSING` explicitly for criteria ("as a criterion names it"), so the code is not from another element's list; only the redundancy remains.
- money/F1, F2 + context/F5 (customs value, classing certificate) → F9: grouped as data the certificate does nothing with.
- parties/F6 → F15: "Needs decision" set to yes, because broad and context refuted it and the merge cannot settle it.
- broad/F7, F8, F9, F10 referred to findings in 02 ("as cotton/02#F…"); written out in full here (F10, F11, F7, F12).

## Outside this review
- The classing certificate XL-CLS-2026-0042, signed on 2026-02-20, is cited in 02-Forecast.xml, issued on 2026-02-02, before ginning even started on 2026-02-07 (a date question across documents; from parties).
