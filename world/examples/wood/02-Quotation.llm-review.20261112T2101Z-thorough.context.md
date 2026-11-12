# LLM review: 02-Quotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/02#F1 · High · The free-text conditions say "per thousand slats", the price is per slat
- XPath: `/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `7.2`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1`
- Why: The transaction conditions state that the quotation is made per thousand slats, while the structured price is 7.20 XBL for a base quantity of one slat (EA), and the line amount (4800 × 7.20 = 34 560.00) is computed per slat. A reader following the text would read 7.20 per thousand. The text contradicts the structured value next to it.
- Condition: The free text and `Price/BaseQuantity` state the same price basis (either 7.20 per slat, or 7 200.00 per 1 000 EA with the line amount unchanged).
- Options: Preferred: correct the text (e.g. "Prices per slat; minimum one truck") so the price basis is stated once in the structured price. Alternative: quote per 1 000 EA with BaseQuantity 1000.
- Needs decision: no

### wood/02#F2 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/02#F3 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/02#F4 · Low · Substitute and alternative items are offered without price or explanation
- XPath: `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Hardwood bench slat 1800 × 95 × 35`
- XPath: `/Quotation/cac:QuotationLine/cac:AlternativeLineItem/cac:Item/cbc:Name` = `Oak bench slat 1800`
- XPath: `/Quotation/cac:QuotationLine/cbc:Note` = `As drawn; ash or oak.`
- Why: `SellerProposedSubstituteLineItem` is "An item proposed by the seller as a substitute for the item that is the subject of this quotation line" and `AlternativeLineItem` "an alternative". Both carry only a name and the quantity: no price, no line amount, no reason. A buyer cannot choose an option it is not quoted a price for. The alternative "Oak bench slat" also overlaps with the main line, whose note already offers "ash or oak", and the 35 mm substitute lies outside the mandatory thickness tolerance of the main line (37.5–38.5 mm) without saying why it is proposed. The order (`03-Order.xml`) does not refer to either option.
- Condition: Every substitute or alternative line item has a price (or the quotation states it is offered at the same price) and its difference from the main item is clear; or the options are absent.
- Options: Preferred: give each option a price and a note (thinner stock available sooner; oak-only at a surcharge), or drop the options the story does not use. Alternative: keep only one of the two.
- Needs decision: yes (adds or removes offers in the story)

### wood/02#F5 · Low · Two sets of terms without saying which governs
- XPath: `/Quotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026`
- XPath: `/Quotation/cac:AdditionalDocumentReference/cbc:ID` = `MS-GTC-2026`
- Why: The quotation names the buyer's purchase terms as its contract and also refers, without a document type or description, to what its ID suggests are the seller's own general terms. The two normally conflict; the quotation does not say whether its own terms apply, the buyer's, or the seller's only where the buyer's are silent. Neither reference says what kind of document it is.
- Condition: The quotation makes clear which terms govern, and each reference says what it refers to (`DocumentTypeCode` or `DocumentDescription`).
- Options: Preferred: keep the buyer's contract and describe the seller's document as subsidiary, or drop it. Alternative: quote under the seller's terms only.
- Needs decision: yes (which terms govern the sale is part of the story)

### wood/02#F6 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the buyer's contact is the purchaser the quotation is addressed to ("Order desk" in Sales). A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/02#F7 · Low · Party master data this document does nothing with
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. A quotation offers goods to a buyer; it needs the buyer's identity and contact. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

### wood/02#F8 · Low · A validity period on the property "Planed on four sides"
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A surface that has been planed on four sides stays planed; nothing in the document says what would stop the property being valid after 12 months, or from when the months are counted. The property that does change over time is the moisture content (`AdditionalItemProperty[1]`), which carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with a reason the document makes clear, or it is absent.
- Options: Preferred: drop it from the surface property. Alternative: if the world needs one, move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no

## Checked and consistent
- `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21` is 30 days after the issue date 2026-02-19, as the note says.
- `/Quotation/cbc:LineCountNumeric` = `1` matches the single quotation line; `RequestForQuotationLineID` and `RequestLineReference/LineID` both point to line 1 of `01-RequestForQuotation.xml`.
- The promised delivery period equals the requested one (2026-03-02 to 2026-03-16).
- Totals: 34 560.00 + 240.00 charge = 34 800.00 payable.

## Considered and refuted
- `/Quotation/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `ACH` for "Heat-treated export pallets": suspected that a heat-treatment code is used for pallets — refuted because the charge is for the heat treatment of the pallets (export pallets must be heat-treated), which is what the code means.
- `/Quotation/cac:PaymentMeans/cbc:PaymentMeansCode` = `30` without account: refuted as incomplete — a quotation states the expected means, the account follows on the invoice.
- Item specification (moisture content with test method and range, thickness tolerance, forestry certificate): suspected of being copied — refuted because in a sourcing or ordering document these are the requirements the price and the delivery are measured against.
- `AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `cbc:NameCode`: suspected duplicate — refuted because the ID identifies this occurrence of the property while `NameCode` classifies it; both have their own definition and the values agree.
- `Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50`: suspected filler or contradiction — refuted because together they state the pack structure (one slat per unit, 50 per bundle), which the despatch note ("96 bundles of 50") uses.
