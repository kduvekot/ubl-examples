# LLM review: 02-Quotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/02-Quotation.xml`, Git blob `b8dd536e88f83270060fe92537f76080cae01be9` (committed)
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

### wood/02#F1 · High · 'Quoted per thousand slats' contradicts a price per single slat
- XPath: `/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `7.2`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`
- Why: The transaction conditions say the price is quoted per thousand slats, but the price is 7.2 XBL per base quantity of 1 EA, and the line amount (4800 × 7.2 = 34560.00) is computed per slat. Price/BaseQuantity is "The quantity at which this price applies"; a price per thousand would be 7200 XBL per 1000 EA. The text and the structured price disagree.
- Condition: The text and Price agree: either the price is given per 1000 EA (PriceAmount 7200, BaseQuantity 1000) or the text no longer says "per thousand".
- Options: (a, preferred) Express the price as quoted, 7200 per 1000 EA, carried through to the order and invoice (amounts unchanged), because the text states the trade's practice; (b) drop "per thousand" from the text.
- Needs decision: no

### wood/02#F2 · Medium · Urvanian province carried in Region
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is defined as "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division, which UBL puts in CountrySubentity ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses in the same flow do use CountrySubentity and CountrySubentityCode for their states, so the two countries are encoded differently. The same value occurs 219 times in 104 XML files (`grep -r --include='*.xml' -c '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address carries an administrative division in Region; the province, where given, is in CountrySubentity (with CountrySubentityCode if the world has a list for it).
- Options: (a, preferred) Move the province to CountrySubentity, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world a non-administrative region, keep Region but name it as such, without "Province of".
- Needs decision: no

### wood/02#F3 · Medium · Language code in LocaleCode
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/02#F4 · Low · OrderableUnitFactorRate 50 while the quantity is ordered in single slats
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`
- XPath: `/Quotation/cac:QuotationLine/cbc:Quantity` = `4800`
- Why: OrderableUnitFactorRate is "The factor by which the base price unit can be converted to the orderable unit". A factor of 50 says the orderable unit is 50 base units (a bundle of 50), but the quotation quantity, and the order, are in EA (4800 slats), so the orderable unit is the slat itself and the factor would be 1. The bundle is already expressed by Item/PackSizeNumeric 50.
- Condition: The orderable unit implied by the factor is the unit of the quoted and ordered quantities.
- Options: (a, preferred) Drop the factor (or set it so that it matches EA); (b) quote and order in bundles (96 packs) with factor 50.
- Needs decision: no

### wood/02#F5 · Low · Zero tax total without a tax category
- XPath: `/Quotation/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Quotation/cac:QuotationLine/cbc:TotalTaxAmount` = `0.00`
- Why: The quotation states a tax total of 0.00 but no TaxSubtotal or tax category, so the reader cannot tell whether no tax applies (export) or tax was simply not computed. The order (`03-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`) and the invoice give the export category and reason. A zero without its reason is a value implied by absence (IND6).
- Condition: The quotation either states the tax category and exemption reason behind the 0.00, or carries no tax amounts.
- Options: (a, preferred) Add the TaxSubtotal with category G and reason EXP, as in the order; (b) remove TaxTotal and the line tax amounts.
- Needs decision: no

### wood/02#F6 · Low · Alternative and substitute items without price, and the alternative is covered by the main line
- XPath: `/Quotation/cac:QuotationLine/cbc:Note` = `As drawn; ash or oak.`
- XPath: `/Quotation/cac:QuotationLine/cac:AlternativeLineItem/cac:Item/cbc:Name` = `Oak bench slat 1800`
- XPath: `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Hardwood bench slat 1800 × 95 × 35`
- Why: AlternativeLineItem is "An item proposed by the seller as an alternative to the item that is the subject of this quotation line". The main line already offers "ash or oak", so an oak slat is not an alternative to it. Neither the alternative nor the 35 mm substitute has a price, a line amount or a description, so the buyer cannot accept them on the basis of this quotation.
- Condition: Each alternative or substitute item differs from the main offer and carries what the buyer needs to accept it (at least a price).
- Options: (a, preferred) Make the main line one species (e.g. ash) and the oak slat the priced alternative; give the 35 mm substitute its price; (b) remove the alternative.
- Needs decision: no

### wood/02#F7 · Low · Same Urvanian address tagged en-XB here and en-XU elsewhere
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The same English rendering of the same Urvanian address is tagged `en-XB` in this example and `en-XU` in `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` and in 03-Order.xml; in addition, the legal form appears here in one rendering without languageID, while 01 and 03 give the Urvanian and the English rendering, and the certificate type (`/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:Certificate/cbc:CertificateType` = `Sustainable forestry`) has lost its Urvanian rendering. The languageID describes the language of the text, which does not change with the sender's country, so the same text should carry the same tag. 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|…) '`).
- Condition: The same rendering of the same address carries the same languageID in every example of the flow.
- Options: (a, preferred) Tag the rendering by the language variant of the text (the Urvanian English, en-XU) everywhere; (b) document that the tag follows the sender's locale.
- Needs decision: no

### wood/02#F8 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact (an order desk in Valdara's Sales department, a customer service officer) is the function that serves Valdara's own customers, not the one that buys slats.
- Condition: The buyer's contact in this quotation is a purchasing contact.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/02#F9 · Low · Valdara's master data the document does nothing with
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's SecurityListing (listed shares) and its ServiceProviderParty (Castrano Logistics, "Warehousing and despatch") are carried in full in this quotation, which does nothing with either: no security is traded, and Castrano plays no role (the goods go to Valdara's own goods-in in Ferrano). This is party master data copied into a document that does not use it (section 4.8).
- Condition: The party carries in this document only data the document uses, or the example gives the reason for the security listing and the service provider.
- Options: (a, preferred) Leave SecurityListing and ServiceProviderParty out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which would change the story.
- Needs decision: no

### wood/02#F10 · Low · Usability period of 12 months on the 'Surface' property
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: ItemProperty/UsabilityPeriod is "The period during which this item property is valid". A planed surface does not cease to be planed after 12 months; nothing in the example says what the period stands for (a storage or warranty period would be a property of its own).
- Condition: The UsabilityPeriod is absent, or it sits on a property whose validity really expires, and the example makes clear what it means.
- Options: (a, preferred) Remove the UsabilityPeriod from 'Surface'; (b) move it to a property that expires (e.g. a moisture guarantee while stored as agreed).
- Needs decision: no

### wood/02#F11 · Low · Length repeated in SellersItemIdentification/MeasurementDimension
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both as a measurable dimension of the seller's item identification and as Item/Dimension[1]. The identification carries no other variant dimension (width and thickness are only in Item/Dimension), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the MeasurementDimension under the identification is needed to distinguish item variants and the example says so.
- Options: (a, preferred) Keep the length in Item/Dimension only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no

### wood/02#F12 · Low · English (en-X?) renderings of Urvanian names are Italian
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The second rendering of the Urvanian street name (and, where present, of the legal form) is tagged as English (`en-XU`/`en-XB`) but is Italian ("Via …", "Piazza …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be, and the languageID does not describe it. 217 English-tagged street names in 102 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml'`).
- Condition: Every text tagged with an English languageID is English, or the world states that these Italian forms are the official English-language names in Urvania.
- Options: (a) Give the English rendering in English (e.g. "Workshops Street"); (b) if the Italian forms are the world's exonyms, record that in the world's story so the tag is explained. Preference: (b) if it is intended, as the pattern is consistent; otherwise (a).
- Needs decision: yes

### wood/02#F13 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day).
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 4800 × 7.2 = 34560.00 (line, line item, LineExtensionAmount); 34560.00 + 240.00 charge = 34800.00 PayableAmount.
- Validity: issued 2026-02-19, `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21` is 30 days later, as the note says.
- References: `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `VI-DOC-26-0625` resolves to 01-RequestForQuotation.xml; RequestForQuotationLineID and RequestLineReference point to its line 1; the quotation was issued before the submission due date 2026-02-21.
- Promised delivery period equals the period requested in 01; quantity 4800 EA equals the request.
- The pallet charge (ACH, heat treatment, 240.00) recurs unchanged in the order and the invoice.

## Considered and refuted
- `/Quotation/cac:AdditionalDocumentReference/cbc:ID` = `MS-GTC-2026` together with `/Quotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026`: two sets of terms — refuted: the seller can quote under the buyer's purchase terms and attach its own conditions; nothing says they conflict.
- `/Quotation/cac:PaymentMeans/cbc:PaymentMeansCode` = `30` without an account — refuted: in a quotation it is the expected means; the account follows on the invoice.
- `/Quotation/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `ACH` for pallets — refuted: UN/EDIFACT 7161 ACH is heat treatment, which is what the export pallets get (the text says heat-treated pallets).

## Outside this review
- The transaction condition "minimum one truck" against the transport actually ordered (04-TransportExecutionPlanRequest.xml, full truck load) is consistent; whether 21.6 t fits Trasvia's vehicle is a capacity question for the cross-flow review.
