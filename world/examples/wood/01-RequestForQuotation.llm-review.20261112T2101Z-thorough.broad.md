# LLM review: 01-RequestForQuotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/01-RequestForQuotation.xml`, Git blob `c0a83fe4f0fa1f96f25fae6aedf8f2a7b3fb0857` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### wood/01#F1 · Medium · Urvanian province carried in Region
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is defined as "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division, which UBL puts in CountrySubentity ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses in the same flow do use CountrySubentity and CountrySubentityCode for their states, so the two countries are encoded differently. The same value occurs 219 times in 104 XML files (`grep -r --include='*.xml' -c '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address carries an administrative division in Region; the province, where given, is in CountrySubentity (with CountrySubentityCode if the world has a list for it).
- Options: (a, preferred) Move the province to CountrySubentity, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world a non-administrative region, keep Region but name it as such, without "Province of".
- Needs decision: no

### wood/01#F2 · Medium · Language code in LocaleCode
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/01#F3 · Low · Line marked both Confidential and Internal
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode` = `INTERNAL`
- Why: PrivacyCode is "A code signifying the level of confidentiality of this request for quotation line" and SecurityClassificationCode "the security classification of this request for quotation line". The two give different levels for the same line (Confidential against Internal, which in usual classification schemes is the lower level), and nothing in the example says why this one standard slat line needs either marking while the rest of the request carries none.
- Condition: The line carries at most one confidentiality level, or both codes agree and the example gives the business reason (e.g. the drawing VI-DS-SL1800 being confidential).
- Options: (a, preferred) Keep one marking with its reason (the buyer's drawing); (b) remove both if the line has nothing confidential.
- Needs decision: no

### wood/01#F4 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact for a request for quotation is the one who buys (purchasing); Valdara's contact is an order desk staffed by a customer service officer in the Sales department, i.e. the function that serves Valdara's own customers. The seller's contact (Sales office) fits the seller role.
- Condition: The buyer's contact in this request is a purchasing contact (name, job title and department agreeing with each other).
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/01#F5 · Low · Valdara's master data the document does nothing with
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's SecurityListing (listed shares) and its ServiceProviderParty (Castrano Logistics, "Warehousing and despatch") are carried in full in this request for quotation, which does nothing with either: no security is traded, and Castrano plays no role (the goods go to Valdara's own goods-in in Ferrano). This is party master data copied into a document that does not use it (section 4.8).
- Condition: The party carries in this document only data the document uses, or the example gives the reason for the security listing and the service provider.
- Options: (a, preferred) Leave SecurityListing and ServiceProviderParty out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which would change the story.
- Needs decision: no

### wood/01#F6 · Low · Usability period of 12 months on the 'Surface' property
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: ItemProperty/UsabilityPeriod is "The period during which this item property is valid". A planed surface does not cease to be planed after 12 months; nothing in the example says what the period stands for (a storage or warranty period would be a property of its own).
- Condition: The UsabilityPeriod is absent, or it sits on a property whose validity really expires, and the example makes clear what it means.
- Options: (a, preferred) Remove the UsabilityPeriod from 'Surface'; (b) move it to a property that expires (e.g. a moisture guarantee while stored as agreed).
- Needs decision: no

### wood/01#F7 · Low · Length repeated in SellersItemIdentification/MeasurementDimension
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both as a measurable dimension of the seller's item identification and as Item/Dimension[1]. The identification carries no other variant dimension (width and thickness are only in Item/Dimension), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the MeasurementDimension under the identification is needed to distinguish item variants and the example says so.
- Options: (a, preferred) Keep the length in Item/Dimension only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no

### wood/01#F8 · Low · English (en-X?) renderings of Urvanian names are Italian
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The second rendering of the Urvanian street name (and, where present, of the legal form) is tagged as English (`en-XU`/`en-XB`) but is Italian ("Via …", "Piazza …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be, and the languageID does not describe it. 217 English-tagged street names in 102 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml'`).
- Condition: Every text tagged with an English languageID is English, or the world states that these Italian forms are the official English-language names in Urvania.
- Options: (a) Give the English rendering in English (e.g. "Workshops Street"); (b) if the Italian forms are the world's exonyms, record that in the world's story so the tag is explained. Preference: (b) if it is intended, as the pattern is consistent; otherwise (a).
- Needs decision: yes

### wood/01#F9 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day).
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- References: the quotation 02-Quotation.xml answers this request (`02-Quotation.xml:/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `VI-DOC-26-0625`), after its issue date and before the submission due date (`/RequestForQuotation/cbc:SubmissionDueDate` = `2026-02-21`; quotation issued 2026-02-19). The drawing, purchase terms and audit report (VI-DS-SL1800, VI-PUR-TERMS-2026, XB-FOR-AUD-2025-0118) are external documents, not examples of the flow.
- Item data agree with every later example of the flow (description, 1800 × 95 × 38 mm, HS 440799, CPC 31102, moisture 12 % in the range 10–14 %, thickness 38 mm in 37.5–38.5 mm, certificate XB-FOR-2025-0118 valid to 2027-12-31).
- HS 440799 ("other" non-coniferous sawn wood) fits a hardwood slat whose species is not fixed; HS 4407 covers sawn wood whether or not planed, and CPC 31102 is the non-coniferous counterpart (own knowledge of HS 2022 and CPC 2.1).
- Check digits: ISIN XU0001042501 passes (check_ids.py).
- Delivery window 2026-03-02 to 2026-03-16 lies after the issue date; validity 30 days.
- Bayvarran addresses: Upland State in CountrySubentity with code XB-UL, consistent in every example.

## Considered and refuted
- `/RequestForQuotation/cac:AdditionalDocumentReference/cbc:ID` and `/RequestForQuotation/cac:RequestForQuotationLine/cac:DocumentReference/cbc:ID`: a reference with only an ID — refuted because the header note says it is the buyer's drawing, and the line reference ties the drawing to the only line.
- `/RequestForQuotation/cac:DeliveryTerms/cbc:ID` (DAP) without a named place in DeliveryTerms — refuted because Delivery/DeliveryLocation names Valdara's goods-in in Ferrano, which is the place DAP refers to.
- `/RequestForQuotation/cac:Signature/cbc:ID`: a signature on a request for quotation — refuted: the buyer may sign its request; party and ID are consistent.
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50` with PackQuantity 1 EA — refuted: one slat is the item, 50 slats a pack, consistent with the 96 bundles of 50 in 06-DespatchAdvice.xml.
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: possible clash with a real ISO 10383 MIC — not settled here: I could not check the MIC register; noted only so that it is checked against the recorded sources.
