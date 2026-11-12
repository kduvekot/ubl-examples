# LLM review: 02-Quotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/02-Quotation.xml`, Git blob `b8dd536e88f83270060fe92537f76080cae01be9` (committed)
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

### wood/02#F1 · High · "Quoted per thousand slats" contradicts a price per single slat
- XPath: `/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `7.2`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`
- Why: `Price/BaseQuantity` is "The quantity at which this price applies"; here it is 1 EA, so the price is 7.20 XBL per slat, and 4800 × 7.20 = 34 560.00 = `/Quotation/cac:QuotationLine/cbc:LineExtensionAmount` = `34560.00` confirms the per-slat reading (recalculated in the merge). The transaction conditions ("purchasing, sales, or payment conditions applying to Orders related to this Quotation") say the slats are quoted per thousand; a price per thousand would be 7 200.00 per 1000 EA. The text and the structured price contradict each other. The order and the invoice follow the structured value (`03-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`, `08-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1`).
- Condition: The transaction conditions and `Price` (PriceAmount, BaseQuantity) state the same price basis, and PriceAmount × Quantity / BaseQuantity still gives the line amount.
- Options: (a, preferred) correct the text (e.g. "Prices per slat; minimum one truck."), since order and invoice already use the per-slat price and only one document changes; (b) quote per thousand (PriceAmount 7200, BaseQuantity 1000 EA) here and in the order and invoice, amounts unchanged.
- Needs decision: no
- From: broad, money, context

### wood/02#F2 · Medium · Language code `en` in `Language/LocaleCode`
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language as used in a region or country (the examples' own `languageID` values `en-XU`, `en-XB` show such variants). `en` with `listID="ISO 639"` is a language code only and repeats `Language/ID`, so the element carries a meaning other than its definition; the Urvanian parties carry no `LocaleCode`, so the parties are described unevenly. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; files with `grep -rl`).
- Condition: Every `cbc:LocaleCode` in this example either holds a locale (e.g. `en-XB`) with a `listID` naming a list of locales, or is absent.
- Options: (a, preferred) leave `LocaleCode` out where no locale matters, as here; (b) a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags), named in `listID`.
- Needs decision: no
- From: broad, context, parties

### wood/02#F3 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `Address/CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province belongs in `CountrySubentity`, as the Bayvarran address of the same example has it (`/Quotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`; files with `grep -rl`).
- Condition: No Urvanian address in this example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` where the world has a list), and `cbc:Region`, if present, holds a region in the UBL sense.
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, as for Bayvarra; (b) if Ferrano is an economic region in the world, rename it without "Province" and record that in the story.
- Needs decision: no
- From: broad, context, parties

### wood/02#F4 · Low · Two sets of terms, neither saying what it is or which governs
- XPath: `/Quotation/cac:AdditionalDocumentReference/cbc:ID` = `MS-GTC-2026`
- XPath: `/Quotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026`
- Why: The quotation names the buyer's purchase terms as its contract and also refers, by ID only and without `DocumentTypeCode` or `DocumentDescription`, to a document whose ID suggests the seller's own general terms. Where both apply, the quotation does not say which governs. Counter-argument (broad part): a seller can quote under the buyer's purchase terms and attach its own conditions, and nothing says the two conflict. That the seller's document does not say what it is holds either way; whether a governing-terms statement is needed is a judgment on the story the merge could not settle.
- Condition: Each reference says what kind of document it is, and the quotation makes clear which terms govern (or that the seller's apply only where the buyer's are silent).
- Options: (a, preferred) keep the buyer's contract and describe `MS-GTC-2026` (type and description) as subsidiary, or drop it; (b) quote under the seller's terms only.
- Needs decision: yes
- From: context (broad refuted it; see "Considered and refuted"), logistics (the ID-only reference)

### wood/02#F5 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". The date occurs 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`; files with `grep -rl`), for about 25 companies of every kind in all three countries' registers (parties part, lxml count), while other dates are specific (`/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`). It reads as a filler unless the world has an event that explains it.
- Condition: Each company's registration date is its own date in the world, or the world documents why these companies share 1996-01-01; otherwise it is absent.
- Options: (a, preferred) each company its own date; (b) record a 1996 re-registration in the story if that is intended; (c) leave the date out.
- Needs decision: yes
- From: broad, parties

### wood/02#F6 · Low · Text tagged as English is Italian
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The street name is tagged `en-XB` but is Italian; the legal form is Italian too (untagged here, `en-XU` in 01 and 03, see F8). The world's languages are English, Urvanian and Lisavan. 219 English-tagged street names in 104 examples start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml' 'StreetName languageID="en-X[A-Z]">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): proper names of streets are commonly kept untranslated, and the world uses Italianate names consistently. That covers the street, not the legal form, which is a descriptive term. The merge could not settle whether the Italian forms are the world's English exonyms.
- Condition: Every text tagged (or meant) as English is English, or the world's story states that these Italian forms are the English-language names used for Urvania.
- Options: (a, preferred if intended) record the convention in the story and give the legal form in English; (b) English renderings throughout.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/02#F7 · Low · Same Urvanian text tagged `en-XB` here and `en-XU` in 01 and 03
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same rendering of Valdara's address carries `en-XB` in this Bayvarran-issued quotation and `en-XU` in the Urvanian-issued request and order. If `languageID` describes the language of the text, the same text should carry the same tag; 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): the tag names the language variant of the issuer's English, consistently within each document. Both readings are possible; the examples do not say which rule they follow.
- Condition: The same text carries the same `languageID` in every example of the flow, or the rule that the tag follows the issuer is documented.
- Options: (a, preferred) one rule, documented in the world (tag by the variant of the text, `en-XU`, everywhere); (b) document that the tag follows the issuer's locale.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/02#F8 · Low · Urvanian legal form and certificate type in one untagged rendering
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:Certificate/cbc:CertificateType` = `Sustainable forestry`
- Why: Valdara's address is given in two tagged renderings (`qau` and English), but its legal form only once, without `languageID`; in the Urvanian-issued examples the legal form has both renderings, each tagged (`01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). The certificate type likewise has lost its Urvanian rendering and its tag (`01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Certificate/cbc:CertificateType[1]` = `Zhazdran zakrek`). Within this example the address and the legal form follow different language rules, and Valdara is described differently from example to example.
- Condition: Within this example each multilingual text follows one rule: both renderings, each with its `languageID`, or one rendering with its `languageID`.
- Options: (a, preferred) render legal form (and certificate type) like the address, as the Urvanian-issued examples do; (b) if a Bayvarran issuer writes only English, tag the single rendering and say why the address keeps its Urvanian rendering (it is needed for delivery).
- Needs decision: no
- From: parties, broad (the untagged legal form and the certificate type)

### wood/02#F9 · Low · Valdara's master data the document does nothing with
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A quotation offers goods to a buyer; it needs the buyer's identity and contact. Valdara's share capital, stock-exchange listing and logistics service provider (Castrano Logistics, "Warehousing and despatch") are master data the quotation does nothing with (section 4.8). Castrano appears in 9 of the 11 wood examples (`grep -l Castrano world/examples/wood/*.xml | wc -l`), never in a role of its own.
- Condition: Valdara's description here carries share capital, listing and service provider only if the document uses them.
- Options: (a, preferred) leave them out of this document; (b) give Castrano a role the document uses, which changes the story.
- Needs decision: no
- From: broad, context, parties

### wood/02#F10 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party", read in its role here: the buyer the quotation is addressed to should be reached in purchasing, not at an order desk in its own Sales department. The same contact is used for Valdara in every role of the flow; `Customer service officer` occurs 395 times in 229 examples (`grep -rho --include='*.xml' 'Customer service officer' world/examples | wc -l`; files with `grep -rl`).
- Condition: The buyer's contact belongs to purchasing (or the function that handles quotations), with name, job title and department agreeing.
- Options: (a, preferred) role-specific contacts per party in the world, chosen by the party's role in each document; (b) drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no
- From: broad, context, parties

### wood/02#F11 · Low · Zero tax without a category that says why
- XPath: `/Quotation/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Quotation/cac:QuotationLine/cbc:TotalTaxAmount` = `0.00`
- Why: The quotation states a tax amount of 0.00 but no `TaxSubtotal` or `TaxCategory`, so the reason (Bayvarran state sales tax not charged on an export to Urvania) is only implied by the zero (IND6). The order of the same deal carries it explicitly (`03-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`, with exemption reason EXP), as does the invoice.
- Condition: The quotation's tax total carries the category (G, STT, exemption reason) behind the zero, or the quotation carries no tax amounts.
- Options: (a, preferred) add a `TaxSubtotal` as in the invoice (taxable 34 800.00 including the pallet charge, G, EXP), so the quotation says what the buyer will pay and why; (b) drop `TaxTotal` and the line tax amounts.
- Needs decision: no
- From: broad, money

### wood/02#F12 · Low · Line refers to an unnamed seller document, not to the buyer's drawing it is quoted "as drawn"
- XPath: `/Quotation/cac:QuotationLine/cac:DocumentReference/cbc:ID` = `MS-SPEC-SL1800`
- XPath: `/Quotation/cac:QuotationLine/cbc:Note` = `As drawn; ash or oak.`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cac:DocumentReference/cbc:ID` = `VI-DS-SL1800`
- Why: `QuotationLine/DocumentReference` is "A reference to a document associated with this quotation line". Its only document is given by ID alone, without a type, and is not the drawing the request asked to be quoted against, while the note says the slats are quoted "as drawn". A reader cannot tell whether `MS-SPEC-SL1800` is the seller's own specification replacing the drawing or a restatement of it; the buyer's drawing is not referenced. It is an external document, so this is about saying what it is, not a broken reference.
- Condition: The line's document reference says what kind of document it is, and the line makes clear which drawing or specification the quoted slat follows.
- Options: (a, preferred) type the reference and add a line reference to `VI-DS-SL1800`, keeping `MS-SPEC-SL1800` as the seller's specification derived from it; (b) replace `MS-SPEC-SL1800` by `VI-DS-SL1800` if the seller has no specification of its own.
- Needs decision: no
- From: logistics

### wood/02#F13 · Low · `OrderableUnitFactorRate` 50 while quantities are in single slats
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50`
- XPath: `/Quotation/cac:QuotationLine/cbc:Quantity` = `4800`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50`
- Why: `Price/OrderableUnitFactorRate` is "The factor by which the base price unit can be converted to the orderable unit". A factor of 50 says the orderable unit is 50 slats, but the quoted (and later ordered) quantity is in EA, which suggests the orderable unit is the slat (factor 1, or no factor). Counter-argument (money part): the item is sold in packs of 50 (`PackSizeNumeric`), so the orderable unit is the pack, and 4800 is a whole number of packs (96); the quantity can still be counted in slats. UBL gives no separate orderable-unit element in a quotation line, so the merge could not settle which reading is meant.
- Condition: The orderable unit implied by the factor is evident: either the quantities are in that unit, or the pack of 50 is stated to be the orderable unit.
- Options: (a, preferred) drop the factor, since `PackSizeNumeric` already states the bundle and quantities are in EA; (b) keep it and quote/order 96 packs, or state that slats are ordered in whole packs.
- Needs decision: yes
- From: broad (money refuted it; see "Considered and refuted")

### wood/02#F14 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length is given as a measurable dimension of the seller's item identification and again as `Item/Dimension[1]`; the identification carries no other dimension, so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the dimension under the identification distinguishes item variants and the example says so.
- Options: (a, preferred) keep the length in `Item/Dimension` only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no
- From: broad

### wood/02#F15 · Low · A 12-month validity on the property "Planed on four sides"
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what ends the property after 12 months. The moisture content, which does change, carries no period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear, or it is absent.
- Options: (a, preferred) remove it from the surface property; (b) move it to a property that changes (e.g. moisture content during storage) and say what it means.
- Needs decision: no
- From: broad, context

### wood/02#F16 · Low · Substitute and alternative offered without price, the alternative overlapping the main line
- XPath: `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Hardwood bench slat 1800 × 95 × 35`
- XPath: `/Quotation/cac:QuotationLine/cac:AlternativeLineItem/cac:Item/cbc:Name` = `Oak bench slat 1800`
- XPath: `/Quotation/cac:QuotationLine/cbc:Note` = `As drawn; ash or oak.`
- Why: `SellerProposedSubstituteLineItem` is "An item proposed by the seller as a substitute for the item that is the subject of this quotation line" and `AlternativeLineItem` one proposed "as an alternative". Both carry only a name and the quantity 4800: no price, line amount or reason, so the buyer cannot accept or compare them (ash and oak are normally priced differently). The main line already offers "ash or oak", so an oak slat is not an alternative to it. Why the 35 mm substitute is proposed is not said (its being outside the main item's tolerance is not itself a contradiction, see "Considered and refuted"). The order (`03-Order.xml`) uses neither.
- Condition: Each substitute or alternative differs clearly from the main offer and states its price (or the quotation states it is offered at the same price); or the options are absent.
- Options: (a, preferred) make the main line one species (e.g. ash) and the oak slat the priced alternative, and give the 35 mm substitute a price and a reason (e.g. available sooner); (b) state that the options are at the same price; (c) drop the options the story does not use.
- Needs decision: yes
- From: broad, money, context

## Checked and consistent
- Arithmetic, recalculated in the merge: 4800 × 7.20 = 34 560.00 (line, line item and `QuotedMonetaryTotal/LineExtensionAmount`); 34 560.00 + 240.00 = 34 800.00 = `/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount` = `34800.00`; `ChargeTotalAmount` 240.00 equals the single charge (broad, money, context).
- Validity: issued 2026-02-19, `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21` is 30 days later, as `/Quotation/cbc:Note` = `Valid for 30 days.` says and the request asked; the order (2026-02-22) falls within it (broad, money, logistics, context).
- References: `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `VI-DOC-26-0625` resolves to `01-RequestForQuotation.xml`; `RequestForQuotationLineID` and `RequestLineReference/LineID` point to its only line; quoted before the submission due date (broad, logistics, context).
- Promised window equals the requested one (2026-03-02 to 2026-03-16); quantity 4800 EA equals the request; the substitute and alternative keep that quantity (broad, logistics, context).
- The pallet charge (ACH, 240.00) recurs unchanged in the order and the invoice; PricingCurrencyCode XBL matches the request and every currencyID; PaymentMeansCode 30 matches the invoice; DAP puts carriage on the seller, consistent with Marrowdale as bill-to party in `04-TransportExecutionPlanRequest.xml` (money).
- Price plausibility: 7.20 XBL / 0.006498 m³ ≈ 1 108 XBL/m³, about twice the 540 XBL/m³ for boards in `10-Order.xml`, plausible for planed, cut-to-size hardwood (money; recalculated).
- "Minimum one truck": 4800 slats = 31.19 m³ and about 21.6 t, one articulated truck (own knowledge: about 24 t payload, about 90 m³), consistent with the FTL service of `04-TransportExecutionPlanRequest.xml` (logistics).
- Parties identical to their other full descriptions in the flow apart from the language renderings in F6–F8; `check_ids.py` passes (parties).

## Considered and refuted
- `/Quotation/cac:PaymentMeans/cbc:PaymentMeansCode` = `30` without an account — refuted: a quotation states the expected means; the account follows on the invoice (from broad, context).
- `/Quotation/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `ACH` for pallets — refuted: UN/EDIFACT 7161 ACH is "Heat treatment", which is what the export pallets get ("Heat-treated export pallets") (from broad, context, money).
- `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Hardwood bench slat 1800 × 95 × 35` outside the main item's thickness tolerance 37.5–38.5 mm — refuted: a substitute is by definition a different item and need not meet the main item's tolerance (from logistics; context used it as part of its finding, which F16 keeps only as "no reason given").
- Item specification (moisture with test method and range, thickness tolerance, forestry certificate): copied — refuted: in a sourcing document these are the requirements price and delivery are measured against (from context).
- `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `NameCode` — refuted: the ID identifies the occurrence, `NameCode` classifies it (from context).
- `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50` — refuted: together they state the pack structure (from context).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a possibly real ICD — refuted: not in the repository's ICD list (from parties).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: a possibly real MIC — refuted: not in the repository's MIC list (from parties; re-checked in the merge).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted by `check_ids.py` (from parties).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: definition says "number of shares" — refuted: the element is an Amount; a quirk of UBL's wording. Whether it belongs here is F9 (from parties).
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: a default contact — refuted: a sales office is the right contact for the seller of a quotation (from parties).
- `/Quotation/cac:Signature/cac:SignatoryParty/cac:PartyIdentification/cbc:ID` = `20412329` — refuted: it is the seller, identified as in `SellerSupplierParty`; the signature ID `MS-SIG-26-QT` is document-style, not the flow name (from parties; the last point added in the merge).
- `/Quotation/cac:AdditionalDocumentReference/cbc:ID` = `MS-GTC-2026` together with `/Quotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026` — refuted by the broad part (the seller may quote under the buyer's terms and attach its own; nothing says they conflict). Not followed in full: kept as F4 with this counter-argument, Needs decision: yes.
- `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:OrderableUnitFactorRate` = `50` — refuted by the money part (the pack of 50 is the orderable unit). Not followed: kept as F13, Needs decision: yes, with both arguments.
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text tagged English — refuted by the parties part as a world convention. Not followed: kept as F6, Needs decision: yes.
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano` tagged `en-XB` here and `en-XU` in 01 — refuted by the parties part (the tag follows the issuer's English). Not followed: kept as F7, Needs decision: yes.

## Changed in the merge
- broad/F1, money/F1, context/F1 → F1: combined. Preferred option is now "correct the text" (money's and context's preference; broad preferred quoting per thousand, kept as option b), because order and invoice already use the per-slat price.
- broad/F3, context/F3, parties/F2 → F2 and broad/F2, context/F2, parties/F1 → F3: combined; context's "Needs decision: yes" on Region set to no (encoding, not story); LocaleCode's preferred option set to "leave out" (context's), aligned with the merge of wood 06–11.
- context/F5 and the ID-only part of logistics/F1 → F4: kept as Low, Needs decision: yes, with the broad part's refutation as counter-argument; the reference to `MS-GTC-2026` moved here from logistics/F1, whose line reference stays F12.
- broad/F13, parties/F6 → F5: combined.
- broad/F12 → F6: count corrected (219 in 104 files instead of 217 in 102); parties' counter-argument added.
- broad/F7 split: the `en-XB`/`en-XU` question → F7, now Needs decision: yes (the parties part refuted it; the merge could not settle it); the untagged legal form and the certificate type → F8, combined with parties/F5.
- broad/F9, context/F7, parties/F4 → F9; broad/F8, context/F6, parties/F3 → F10; broad/F5, money/F2 → F11: combined, wording only.
- logistics/F1 → F12: the `MS-GTC-2026` reference moved to F4.
- broad/F4 → F13: Needs decision changed from no to yes, with money's refutation as counter-argument (cannot settle).
- broad/F11 → F14; broad/F10, context/F8 → F15: wording only.
- broad/F6, money/F3, context/F4 → F16: combined; Needs decision: yes (context's; broad and money had no) because pricing or dropping the options changes the offer in the story; the tolerance argument reduced to "no reason given", following logistics' refutation.

## Outside this review
- Whether 21.6 t fits Trasvia's vehicle is a capacity question for the cross-flow review (from broad).
