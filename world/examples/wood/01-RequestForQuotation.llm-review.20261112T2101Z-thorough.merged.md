# LLM review: 01-RequestForQuotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/01-RequestForQuotation.xml`, Git blob `c0a83fe4f0fa1f96f25fae6aedf8f2a7b3fb0857` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 83ce5da 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### wood/01#F1 · Medium · Language code `en` in `Language/LocaleCode`
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language as used in a region or country (English as used in Bayvarra); the examples themselves distinguish such variants in their `languageID` attributes (`en-XU`, `en-XB`). The value `en` with `listID="ISO 639"` is a language code only and repeats `Language/ID`, so the element carries a meaning other than its definition. The Urvanian parties of the flow carry no `LocaleCode`, so the parties are also described unevenly. The same element and value occur 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; files with `grep -rl`).
- Condition: Every `cbc:LocaleCode` in this example either holds a locale (language and country, e.g. `en-XB`) with a `listID` naming a list of locales, or is absent.
- Options: (a, preferred) leave `LocaleCode` out where no locale matters, since nothing in this request uses it; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`, consistent with the `languageID` convention.
- Needs decision: no
- From: broad, context, parties

### wood/01#F2 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran address of the same example does (`/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`, with `CountrySubentityCode`). The same element and value occur 219 times in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`; files with `grep -rl`), so this is the pattern of every Urvanian address.
- Condition: No Urvanian address in this example carries the province in `cbc:Region`; the province is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` where the world has a list for Urvania), and `cbc:Region`, if present, holds a region in the UBL sense.
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world an economic rather than an administrative region, rename it without "Province" and record that in the world story.
- Needs decision: no
- From: broad, context, parties

### wood/01#F3 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd is registered on 1996-01-01; the same date is given 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`; files with `grep -rl`), for companies of every kind (sawmill, haulier, ports, an airport cargo terminal, a telecom company, an insurer) in the registers of all three countries (the parties part counted 25 companies with lxml over every `PartyLegalEntity`), while other dates are specific (`/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`). A New Year's Day shared by unrelated companies in three registers reads as a filler, unless the world has an event that explains it.
- Condition: Each company's registration date is its own date in the world, or the world documents why these companies share 1996-01-01; otherwise the date is absent.
- Options: (a, preferred) give each company its own registration date from its history; (b) if a 1996 re-registration (e.g. under the Trade Accord) is the story, record it there; (c) leave the date out where the world has none.
- Needs decision: yes
- From: broad, parties

### wood/01#F4 · Low · Text tagged as English is Italian
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The second renderings of Valdara's street name and legal form are tagged `en-XU` but are Italian ("Via …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so the `languageID` does not describe the text. 219 English-tagged street names in 104 examples start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml' 'StreetName languageID="en-X[A-Z]">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`; files with `grep -rlE`). Counter-argument (parties part): a street's proper name is commonly kept untranslated in English text, and the world uses Italianate names for Urvanian streets and towns consistently, so this may be a world convention. That argument covers the street name; it does not cover the legal form, which is a descriptive term followed by its English gloss, not a proper name. The merge could not settle whether the Italian forms are intended as the world's English exonyms.
- Condition: Every text tagged with an English `languageID` is English, or the world's story states that these Italian forms are the English-language names used for Urvania (and the legal form follows the same rule).
- Options: (a, preferred if the pattern is intended) record the convention in the world's story, and give the legal form in English (e.g. "Urvanian public limited company"); (b) give all English renderings in English (e.g. "Workshops Street").
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/01#F5 · Low · Valdara's master data the document does nothing with
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A request for quotation needs the buyer's identity and contact. Valdara is described with its share capital (`CorporateStockAmount`, with `FullyPaidSharesIndicator`), its stock-exchange listing (`SecurityListing`) and a logistics service provider (Castrano Logistics, "Warehousing and despatch"), none of which the document uses: no security is traded, and Castrano has no role (the goods go to `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`). This is party master data copied into a document that does not use it (section 4.8). Castrano appears in 9 of the 11 wood examples (`grep -l Castrano world/examples/wood/*.xml | wc -l`), never in a role of its own; the block is the same in every full description of Valdara in the flow (01–09).
- Condition: Valdara's description in this request carries share capital, security listing and service provider only if the document does something with them.
- Options: (a, preferred) leave them out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which changes the story.
- Needs decision: no
- From: broad, context, parties

### wood/01#F6 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party", read in the party's role here. The buyer asking for a quotation should be reached in purchasing; Valdara's contact is an order desk staffed by a customer service officer in Sales, the function that serves Valdara's own customers. The parties carry the same contact in every example of the flow whatever their role (Valdara's `Order desk` also as consignee, importer and accounting customer). The job title `Customer service officer` occurs 395 times in 229 examples (`grep -rho --include='*.xml' 'Customer service officer' world/examples | wc -l`; files with `grep -rl`), with the department `Sales` even for contacts named `Purchasing` or `Goods inwards` (parties part), so it reads as a default. The seller's contact (Sales office) fits the seller's role.
- Condition: The buyer's contact in this request belongs to purchasing (or the function that handles the request), with name, job title and department agreeing with each other.
- Options: (a, preferred) give each party role-specific contacts in the world (purchasing, goods-in, despatch, customs, accounts) and use the one for the party's role in each document; (b) drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no
- From: broad, context, parties

### wood/01#F7 · Low · Line marked both "Confidential" and "Internal"
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode` = `INTERNAL`
- Why: `PrivacyCode` is "A code signifying the level of confidentiality of this request for quotation line" and `SecurityClassificationCode` "the security classification of this request for quotation line". The world's lists give PrivacyCode `CONFIDENTIAL` as "Not to be passed on" and SecurityClassificationCode `INTERNAL` as "Not for publication", and the security list also has its own `CONFIDENTIAL` level (`world/codelists/gc/SecurityClassificationCode.gc`), so the line has two different handling levels. Nothing says why this one standard slat line needs any marking while the rest of the request has none (the buyer's drawing VI-DS-SL1800 would be a reason).
- Condition: The line carries one consistent confidentiality level (or only one of the two codes), and the reason is evident (e.g. from the drawing reference).
- Options: (a, preferred) keep one marking, at a level that fits a line referring to the buyer's own drawing; (b) remove both if nothing on the line is confidential; (c) keep both if the world's lists define them as independent dimensions, and say so in the lists.
- Needs decision: no
- From: broad, context

### wood/01#F8 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: `ItemIdentification/MeasurementDimension` is "A measurable dimension (length, mass, weight, or volume) of the item". The length 1800 mm is given there and again as `Item/Dimension[1]`; the identification carries no other dimension (width and thickness are only in `Item/Dimension`), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the dimension under the identification is needed to tell item variants apart and the example says so.
- Options: (a, preferred) keep the length in `Item/Dimension` only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no
- From: broad

### wood/01#F9 · Low · A 12-month validity on the property "Planed on four sides"
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what would end the property after 12 months or from when the months count. The property that does change over time, the moisture content (`AdditionalItemProperty[1]`), carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear from the document, or it is absent.
- Options: (a, preferred) remove it from the surface property; (b) move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no
- From: broad, context

## Checked and consistent
- References: `02-Quotation.xml:/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `VI-DOC-26-0625` answers this request, on `02-Quotation.xml:/Quotation/cbc:IssueDate` = `2026-02-19`, before `/RequestForQuotation/cbc:SubmissionDueDate` = `2026-02-21`. The requested validity `/RequestForQuotation/cac:RequestedValidityPeriod/cbc:DurationMeasure` = `30` days is met (`02-Quotation.xml:/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21`, 30 days after 19 February). The drawing, purchase terms and audit report (VI-DS-SL1800, VI-PUR-TERMS-2026, XB-FOR-AUD-2025-0118) are external documents, not examples of the flow (broad, context, logistics; re-checked in the merge).
- Requested window `/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02` to `/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-03-16` is the window the quotation promises; whether the transport keeps to it is a finding of the merged review of `04-TransportExecutionPlanRequest.xml` (logistics).
- DAP, destination `XU`, origin `XB`: a cross-border delivery, consistent with the export and import declarations of the flow (logistics, context).
- Item data agree with every later example (1800 × 95 × 38 mm, HS 440799, CPC 31102, moisture 12 % and core 13 % within 10–14 %, thickness 38 mm within 37.5–38.5 mm, certificate XB-FOR-2025-0118 valid to 2027-12-31). HS 440799 and CPC 31102 fit non-coniferous sawn wood over 6 mm, whether or not planed (own knowledge of HS 2022 and CPC 2.1) (broad, context, logistics).
- Physics, recalculated in the merge: one slat 1.800 × 0.095 × 0.038 m = 0.006498 m³; 4800 slats = 31.19 m³; at 650–750 kg/m³ for kiln-dried hardwood (own knowledge) that is 20.3–23.4 t, matching the 21 600 kg gross of the transport documents; 4800 / 50 per pack = 96 packs, as `06-DespatchAdvice.xml` states (logistics).
- Parties: Valdara Industries is described identically in its nine full descriptions (01–09) apart from language renderings, Marrowdale Sawmill identically in all eleven examples; register number = `PartyLegalEntity/CompanyID`; tax schemes fit the countries (Bayvarra STT at state level, Urvania VAT at national level); Bayvarran addresses use `CountrySubentity` `Upland State` with code `XB-UL` throughout (parties, broad).
- Check digits: `check_ids.py` passes, including ISIN XU0001042501 (broad, parties).
- Market code `XFER` is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv`, and ICD `0990` is not in `world/codelists/sources/peppol/ICD.xml` (re-checked in the merge with grep: no match in either).

## Considered and refuted
- `/RequestForQuotation/cac:AdditionalDocumentReference/cbc:ID` = `VI-DS-SL1800` and `/RequestForQuotation/cac:RequestForQuotationLine/cac:DocumentReference/cbc:ID` = `VI-DS-SL1800`: a reference with only an ID — refuted because `/RequestForQuotation/cbc:Note[2]` = `Slats to our drawing VI-DS-SL1800.` says it is the buyer's drawing, and header and line references are both legitimate with one line (from broad, logistics).
- `/RequestForQuotation/cac:DeliveryTerms/cbc:ID` = `DAP` without a named place in DeliveryTerms — refuted because `Delivery/DeliveryLocation` names Valdara's goods-in in Ferrano, the place DAP refers to (from broad).
- `/RequestForQuotation/cac:Signature/cbc:ID` = `VI-SIG-26-RFQ`: a signature on a request for quotation — refuted: the buyer may sign its request; party and ID are consistent, and the ID is a document-style number, not the flow name (from broad; the last point added in the merge).
- `/RequestForQuotation/cac:Signature/cac:SignatoryParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`: signatory with ID and name only — refuted because it is the buyer, fully described in `BuyerCustomerParty` with the same identifier (from parties).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:PackQuantity` = `1` with `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50`: contradiction or filler — refuted because they state the pack structure (one slat per unit, 50 per bundle), which the despatch note uses: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.` (from broad, context, logistics).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: possibly a real ISO 10383 MIC — refuted because it is not in the MIC source of the repository (from context, parties; broad left it open, settled in the merge).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a possibly real ICD — refuted because `0990` is not in the ICD list of the repository (from parties).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted by `check_ids.py` (from parties).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: UBL's definition says "the number of shares" but the element is an Amount — refuted as a finding of the example: a quirk of the UBL definition; the value fits the data type. Whether it belongs here is F5 (from context, parties).
- `/RequestForQuotation/cbc:PricingCurrencyCode` = `XBL`: an Urvanian buyer asking for prices in the seller's Lume — refuted: a buyer may ask to be quoted in the exporter's currency; the definition ("the currency that the Seller will use to price the Quotation") is met (from context).
- `/RequestForQuotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026`: purchase terms in `Contract` — refuted: a standing purchase agreement under which the request is made is a contract associated with it (from context).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `MS-SL-1800` in a request — refuted: a buyer re-ordering from a known supplier knows the seller's number (from context).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Certificate/cbc:ID` = `XB-FOR-2025-0118`: filler — refuted: the buyer requires sustainably sourced timber and names the certificate it relies on (from context).
- Item specification (moisture with test method and range, thickness tolerance): copied — refuted: in a sourcing document these are the requirements price and delivery are measured against (from context).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `NameCode`: duplicate — refuted: the ID identifies this occurrence, `NameCode` classifies it (from context).
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: another default contact — refuted: a sales office is the right contact for the seller in a request for quotation (from parties).
- `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`: a location named after a company, without address or identifier — refuted: the name names the place, the buyer's address is in the document, and a request for quotation only needs the place to price DAP (from parties, logistics).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text tagged English — refuted by the parties part as a world convention for proper names. Not followed in the merge: kept as F4 (Needs decision: yes), because the merge could not settle it and the same rule does not cover the legal form.

## Changed in the merge
- broad/F2, context/F2, parties/F2 → F1: combined; numbered before the Region finding because the seller comes first in the document. Preferred option is now "leave LocaleCode out" (context's preference; broad and parties preferred a real locale, kept as option b), because nothing in this request uses a locale; aligned with the merge of wood 06–11.
- broad/F1, context/F1, parties/F1 → F2: combined. Context had "Needs decision: yes"; set to no because the value itself says "Province", so moving it to `CountrySubentity` is a matter of encoding; the economic-region reading stays as option (b).
- broad/F9, parties/F5 → F3: combined, with the parties' count of companies and registers.
- broad/F8 → F4: the count corrected from 217 street names in 102 files to 219 in 104 (the merge's grep, shown in the finding); the parties' counter-argument added to "Why"; the legal form named as the stronger case.
- broad/F5, context/F4, parties/F4 → F5: combined into one finding with all XPaths (share capital, listing, service type, service provider name).
- broad/F4, context/F3, parties/F3 → F6: combined; the counts from the parties part added.
- broad/F3, context/F5 → F7: combined; the meanings of the two codes from the world's lists added in the merge.
- broad/F7 → F8, broad/F6 and context/F6 → F9: wording only.
- broad's open candidate on `XFER` (MIC) settled as refuted, with context and parties.
