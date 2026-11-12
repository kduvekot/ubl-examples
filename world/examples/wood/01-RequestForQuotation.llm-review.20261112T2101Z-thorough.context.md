# LLM review: 01-RequestForQuotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/01#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/01#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/01#F3 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the buyer's contact is the party asking for a quotation, i.e. purchasing ("Order desk" in Sales). A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/01#F4 · Low · Party master data this document does nothing with
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. A request for quotation asks a seller to quote; it needs the buyer's identity and contact. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

### wood/01#F5 · Low · Privacy code and security classification of the same line disagree
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode` = `INTERNAL`
- Why: `PrivacyCode` is "the level of confidentiality of this request for quotation line" and `SecurityClassificationCode` "the security classification of this request for quotation line". The same line is "Confidential" by one and only "Internal" by the other; in the usual graded schemes these are two different levels, so the line has two different handling levels and the document does not say why (e.g. the buyer's own drawing VI-DS-SL1800).
- Condition: The two codes give the line one consistent handling level, or only one of them is present, and the reason for the confidentiality is evident (e.g. from the drawing reference).
- Options: Preferred: keep one of the two with a level that fits a line referring to the buyer's own drawing. Alternative: keep both if the world's lists define them as independent dimensions, and state that in the lists.
- Needs decision: no

### wood/01#F6 · Low · A validity period on the property "Planed on four sides"
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A surface that has been planed on four sides stays planed; nothing in the document says what would stop the property being valid after 12 months, or from when the months are counted. The property that does change over time is the moisture content (`AdditionalItemProperty[1]`), which carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with a reason the document makes clear, or it is absent.
- Options: Preferred: drop it from the surface property. Alternative: if the world needs one, move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no

## Checked and consistent
- `/RequestForQuotation/cbc:SubmissionDueDate` = `2026-02-21` is after the issue date and before the quotation (`02-Quotation.xml:/Quotation/cbc:IssueDate` = `2026-02-19`).
- Requested validity of 30 days is met by the quotation (valid to 2026-03-21).
- HS 440799 and CPC 31102 both describe sawn non-coniferous wood thicker than 6 mm; the slat is 38 mm.
- DAP with the delivery location at the buyer's goods-in and destination country Urvania agree.
- Market code `XFER` is not in the ISO 10383 MIC source (`world/codelists/sources/iso10383`), so it cannot be mistaken for a real market.

## Considered and refuted
- `/RequestForQuotation/cbc:PricingCurrencyCode` = `XBL`: an Urvanian buyer asking for prices in the seller's Lume was suspected — refuted because a buyer may ask to be quoted in the exporter's currency; the definition ("the currency that the Seller will use to price the Quotation") is met.
- `/RequestForQuotation/cac:Contract/cbc:ID` = `VI-PUR-TERMS-2026`: purchasing terms in `Contract` suspected — refuted because a standing purchase agreement for 2026 under which the request is made is a contract associated with the request.
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `MS-SL-1800` in a request: suspected that the buyer cannot know the seller's number — refuted because a buyer re-ordering from a known supplier does.
- Item `Certificate` in the request: refuted as a filler because the buyer requires sustainably sourced timber and names the supplier's certificate it relies on.
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: UBL's definition says "the number of shares" but the element is an amount with a currency — refuted as a finding of the example; it is a quirk of the UBL definition, and the value fits the data type.
- Item specification (moisture content with test method and range, thickness tolerance, forestry certificate): suspected of being copied — refuted because in a sourcing or ordering document these are the requirements the price and the delivery are measured against.
- `AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `cbc:NameCode`: suspected duplicate — refuted because the ID identifies this occurrence of the property while `NameCode` classifies it; both have their own definition and the values agree.
- `Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50`: suspected filler or contradiction — refuted because together they state the pack structure (one slat per unit, 50 per bundle), which the despatch note ("96 bundles of 50") uses.
