# LLM review: 03-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/03-Order.xml`, Git blob `f14d6ba97f84855490d38ffc0a4d1386846aa813` (committed)
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

### wood/03#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/03#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/03#F3 · Low · The order states no delivery period
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- Why: An order is the buyer's binding instruction. Its `Delivery` names only the delivery party; it carries no requested delivery period, although the request and the quotation agreed one (2026-03-02 to 2026-03-16). The order refers to the quotation, so the period can be inferred, but the transport arranged afterwards (`04-TransportExecutionPlanRequest.xml`) ends before that period begins, which an explicit period in the order would have exposed.
- Condition: The order's `Delivery` states the delivery period the buyer orders (or the order makes explicit that the quotation's promised period applies).
- Options: Preferred: add `RequestedDeliveryPeriod` 2026-03-02 to 2026-03-16 as in the quotation.
- Needs decision: no

### wood/03#F4 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the buyer's contact is the one placing the order ("Order desk" in Sales). A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/03#F5 · Low · Party master data this document does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. An order needs the buyer's identity, contact and delivery details. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

### wood/03#F6 · Low · A validity period on the property "Planed on four sides"
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A surface that has been planed on four sides stays planed; nothing in the document says what would stop the property being valid after 12 months, or from when the months are counted. The property that does change over time is the moisture content (`AdditionalItemProperty[1]`), which carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with a reason the document makes clear, or it is absent.
- Options: Preferred: drop it from the surface property. Alternative: if the world needs one, move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no

## Checked and consistent
- `/Order/cac:QuotationDocumentReference/cbc:ID` = `MS-DOC-26-0626` is `02-Quotation.xml`; the order is issued 2026-02-22, within the quotation's validity.
- Quantity, price, charge and total agree with the quotation (4800 EA × 7.20 + 240.00 = 34 800.00).
- The order is for the main quoted item (38 mm), not the substitute or the alternative.
- DAP with the delivery location at the buyer's goods-in agrees with the quotation.

## Considered and refuted
- `/Order/cbc:AccountingCostCode` = `3100`: equal to Valdara's ISIC code `3100`, suspected to be the industry code in the wrong place — refuted because `AccountingCost` = `Raw materials and parts` identifies it as a cost account of the buyer's chart of accounts; the coincidence is harmless.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:BuyersItemIdentification/cbc:ID` = `VI-R-SL1800`, a new number not in the request: refuted — the buyer assigns its item number when it orders.
- Item specification (moisture content with test method and range, thickness tolerance, forestry certificate): suspected of being copied — refuted because in a sourcing or ordering document these are the requirements the price and the delivery are measured against.
- `AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `cbc:NameCode`: suspected duplicate — refuted because the ID identifies this occurrence of the property while `NameCode` classifies it; both have their own definition and the values agree.
- `Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50`: suspected filler or contradiction — refuted because together they state the pack structure (one slat per unit, 50 per bundle), which the despatch note ("96 bundles of 50") uses.
