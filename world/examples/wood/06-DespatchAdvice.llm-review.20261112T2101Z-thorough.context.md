# LLM review: 06-DespatchAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/06-DespatchAdvice.xml`, Git blob `e24fe891b1bc7348a4d9bc77947476a40bc1b949` (committed)
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

### wood/06#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, i.e. an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same examples do (`Upland State`, `Coastal State`). The same value is in `Region` in 104 examples (`grep -rl --include='*.xml' 'Region>Province of Ferrano' world/examples | wc -l`).
- Condition: Every Urvanian address that names its province carries it in `cbc:CountrySubentity` (with a national code in `CountrySubentityCode` if the world has one), and `cbc:Region` is either absent or holds a region in the UBL sense.
- Options: Preferred: move the value to `CountrySubentity` everywhere (one change at the source of the Urvanian address format). Alternative: if in the world the Urvanian "provinces" are not administrative divisions but economic regions, rename them so that the name does not say "Province", and record that in the world story.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a decision about the world)

### wood/06#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/06#F3 · Low · No despatch date or expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `MS-SH-26-0632`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-02-26`
- Why: A despatch advice describes the despatch of goods so that the receiver can prepare for them. The shipment carries no `Delivery` (no despatch date, no estimated or requested delivery period); only the issue date hints at when the goods left. The note asks the receiver to check the goods "on arrival" without saying when that will be.
- Condition: The despatch advice states when the goods are despatched and when they are expected at the buyer.
- Options: Preferred: add the shipment's delivery with the actual despatch date and the estimated delivery period.
- Needs decision: no

### wood/06#F4 · Low · A status code that says "no status"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: The code `NoStatus` means "No status on document" (or "Line has no status"). Present, it states only that there is nothing to state, which is a filler under the rule "no fillers, and nothing implied by absence": its absence would say the same. The value occurs as `DocumentStatusCode` in 26 examples (`grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: A status code is present only where the document has a status to convey (e.g. a replacement or copy).
- Options: Preferred: drop the element. Alternative: use it in an example where the status matters.
- Needs decision: no

### wood/06#F5 · Low · `Shipment/GrossWeightMeasure` equals the goods' gross weight
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", while the goods item's gross weight is "including packing and packaging but excluding the carrier's equipment". Both carry the same 21600 kg, so the shipment value is the goods weight and does not meet the shipment definition (the truck's trailer is the transport equipment). The value of the goods (4800 slats of 1.8 × 0.095 × 0.038 m = 31.2 m³, i.e. about 690 kg/m³ including bundling and pallets, plausible for kiln-dried ash or oak) fits the goods item, not the shipment.
- Condition: `Shipment/GrossWeightMeasure` either includes the transport equipment (and so exceeds the goods' gross weight) or is absent.
- Options: Preferred: drop the shipment gross weight and keep it on the goods item (and the consignment) where its definition fits. Alternative: add the trailer's tare.
- Needs decision: no

### wood/06#F6 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the despatch supplier's contact is the one who despatched the goods (shipping); the delivery customer's contact receives and checks the goods. A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/06#F7 · Low · Party master data this document does nothing with
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: Under the rule "no fillers" every optional element needs a reason in this document. A despatch advice needs the delivery customer's identity and goods-in, and the carrier's identity; the carrier's operating permit is also carried and the document does nothing with it. Valdara's logistics service provider ("Warehousing and despatch" — a despatching service for a party that, in this flow, only receives goods) and its stock-exchange listing are master data of the party that look copied into the document; nothing in the document uses them. Castrano Logistics appears in 9 of the 11 wood examples, never in a role of its own (`grep -c Castrano world/examples/wood/*.xml`).
- Condition: Every party detail present in the document has a stated use in this document.
- Options: Preferred: carry the full description of a party only in the documents whose purpose needs it (e.g. the securities listing nowhere in this flow, the service provider only where it acts) and identify the party by ID and name elsewhere.
- Needs decision: no

### wood/06#F8 · Low · A validity period on the property "Planed on four sides"
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A surface that has been planed on four sides stays planed; nothing in the document says what would stop the property being valid after 12 months, or from when the months are counted. The property that does change over time is the moisture content (`AdditionalItemProperty[1]`), which carries no such period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with a reason the document makes clear, or it is absent.
- Options: Preferred: drop it from the surface property. Alternative: if the world needs one, move it to a property that changes (e.g. moisture content during storage) and say in the value qualifier what it means.
- Needs decision: no

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627` is `03-Order.xml`; the order line 1 is referenced and the delivered quantity 4800 EA equals the ordered quantity.
- The line note: 960 benches × 5 slats = 4800, 96 bundles × 50 = 4800.
- Manufacture date 2026-02-23 is after the order (2026-02-22) and before the despatch advice.

## Considered and refuted
- Lot `MS-L26-0223` with property "Kiln charge" = `K-07` in a despatch advice: refuted as a filler — it ties the delivered slats to the kiln charge whose moisture samples the test method refers to.
- `AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `cbc:NameCode`: suspected duplicate — refuted because the ID identifies this occurrence of the property while `NameCode` classifies it; both have their own definition and the values agree.
- `Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50`: suspected filler or contradiction — refuted because together they state the pack structure (one slat per unit, 50 per bundle), which the despatch note ("96 bundles of 50") uses.
