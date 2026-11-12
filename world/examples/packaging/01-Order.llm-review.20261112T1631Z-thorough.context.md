# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/01#F1 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located", and `CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is the administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the same example do with `Coastal State` (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). The same `Region` value occurs in 104 examples (`grep -rl --include='*.xml' '<cbc:Region>Province' world/examples | wc -l`).
- Condition: no address of the example carries a province in `Region`; the province of Ferrano is in `CountrySubentity` (with `CountrySubentityCode` if Urvania has such a list).
- Options: (a) preferred: move the value to `CountrySubentity`, because that is the element whose definition names a province; (b) if the world means an economic region rather than the province, rename the value so it is a region and add the province separately.
- Needs decision: no

### packaging/01#F2 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used." A locale is a language in a region (the examples themselves use locales such as `en-XB` in `languageID`); `en` with `listID="ISO 639"` is only the language, which `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en` already says. The element therefore repeats the language and gives no locale. The same `LocaleCode` occurs in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`); the Urvanian parties of this example carry no `LocaleCode`.
- Condition: `LocaleCode` is absent, or holds a locale (language and region) from a list named in its `listID`.
- Options: (a) preferred: remove it where the party has no locale-specific need; (b) give the locale (e.g. English as used in Bayvarra) with a locale list as `listID`.
- Needs decision: no

### packaging/01#F3 · Low · Seller's bank account in an order that pays nothing
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: The Order carries no payment means or payment terms; nothing in it is paid to or from this account, so the seller's account, with branch and bank address, looks copied from master data (section 4.8). Among all Orders of the world only this one and `03-Order.xml` carry a `FinancialAccount` on the seller party (counted with an XPath over `world/examples/*/*.xml`). The account is used where it belongs, in `02-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
- Condition: the Order carries no seller `FinancialAccount`, or carries a reason to (e.g. prepayment terms that use it).
- Options: (a) preferred: remove it; (b) keep it only together with payment terms that need it.
- Needs decision: no

### packaging/01#F4 · Low · Buyer master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: The buyer's logistics provider for "Warehousing and despatch" plays no part in this order: the goods are collected FCA at the seller by the buyer's carrier (`/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`) and no delivery to a Castrano warehouse is stated. The buyer's listed shares are equally irrelevant to buying 480 kg of stretch film. Both are master data of Valdara Industries; they appear in every example that carries Valdara in full (84 examples contain `Castrano Logistics`, counted with `grep -rl --include='*.xml'`).
- Condition: every optional aggregate of the buyer party is one the order uses, or the order states the reason (e.g. Castrano as the receiving warehouse of this delivery).
- Options: (a) preferred: leave ServiceProviderParty and SecurityListing out of the order; (b) give Castrano a real role here (e.g. the delivery or receiving party) if that is the story.
- Needs decision: no

### packaging/01#F5 · Low · Buyer's ordering contact described as a seller's sales desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact in an order is the person who buys (purchasing). Here it is a customer service officer of the Sales department, the same description the seller's contact carries (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`). Job title and department fit a seller, not a buyer. 229 examples carry `Customer service officer`, and 89 examples have a contact named `Purchasing` or `Buying office` in the Sales department (XPath count over `world/examples/*/*.xml`), so every party seems to have one contact description whatever its role.
- Condition: the buyer's contact in the order has a job title and department of a buying function.
- Options: (a) preferred: a purchasing contact (e.g. buyer, Purchasing department) for the buyer; (b) give each party role-specific contacts in the world data.
- Needs decision: no

## Checked and consistent
- Arithmetic: 480 KGM × 3.1 XBL per 1 KGM = 1488.00 = line, LineExtensionAmount and PayableAmount; tax 0 % of 1488.00 = 0.00.
- `check_ids.py`: ISIN `XU0001042501` and the IBAN-like account pass.
- Delivery terms FCA at the seller's despatch with a carrier named by the buyer in `Delivery/Despatch/CarrierParty`: under FCA the buyer contracts the carriage, so the carrier belongs in the order.
- The carrier's authorisation "International road haulage" fits a Bayvarra → Urvania collection.
- Tax category G with exemption reason "Export outside Bayvarra" fits a Bayvarran seller and an Urvanian buyer, in the seller's state sales tax scheme.
- HS 392010 and CPC 36330 both describe polyethylene film; thickness 23 µm fits stretch film.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian-looking text tagged `en-XU` — refuted because the English rendering of Urvanian places uses established exonyms (`Ferrano`), and the tag follows the sender's country in every example (`en-XB` for the same street in `02-Invoice.xml`); the text is the English name, not Italian.
- `/Order/cbc:AccountingCost`: `Raw materials and parts` for stretch film — refuted because packaging consumables are commonly booked as materials; unlike `03-Order.xml` the cost centre does not name a different kind of goods.
- `/Order/cbc:AccountingCostCode`: `3100` equals the buyer's ISIC code 3100 — refuted because the cost code is the buyer's own number and nothing shows it was meant as an industry code.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`: circularity data in an order — refuted because the recycled content is a property the buyer orders ("recycled polyethylene"), and the end-of-life treatment in the buyer's country fits where the film ends up.
- `/Order/cac:TaxTotal`: tax totals in an order — refuted because the anticipated tax treatment (export, 0 %) is information the buyer can rely on.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount`: legal-entity detail in an order — refuted as a separate finding; party legal data identify the contracting party, which an order is.
