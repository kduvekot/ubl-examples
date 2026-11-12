# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/11-Invoice.xml`, Git blob `d14230a475262f9f8b47c7b7e1cbf9ab963fc61a` (committed)
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

### wood/11#F1 · Medium · A language code in `Language/LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). `en` from ISO 639 is the language itself and repeats `Language/ID`; it says nothing about the locale, so the element carries a meaning other than its definition (the severity guide names "a language code in `LocaleCode`" as Medium). The same pair occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`). The documents themselves already use locale-like tags such as `en-XU` and `en-XB` in `languageID`.
- Condition: Wherever `cbc:LocaleCode` is present it holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: Preferred: drop `LocaleCode` where no locale matters (the document gains nothing from it). Alternative: carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`.
- Needs decision: no

### wood/11#F2 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role the party has in this document. Here the accounting supplier's contact answers questions about the invoice (accounts receivable); the accounting customer's contact receives and pays the invoice (accounts payable), but here it is "Trade sales" in Sales. A customer-service officer in the Sales department answers customers; it is not the function this role needs. The same Sales contact is used for every role of these parties in every example of the flow.
- Condition: Each contact in this document belongs to the function the party's role here needs (purchasing, goods receipt, shipping, customs, accounts receivable or payable), or the contact is left out.
- Options: Preferred: give each party role-specific contacts in the world data and pick the one that fits the role of the document. Alternative: leave the contact out where the document does not need one.
- Needs decision: no

### wood/11#F3 · Low · Customs classification and origin in a domestic sale
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- Why: UBL defines `CommodityCode` as "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". This sale is between two companies in the same town and state of Bayvarra (both in Upland State, the buyer collecting ex works); no border is crossed and no customs or foreign-trade statistics apply, and the country of origin is likewise without use. The HS code is in the definition's condition only for cross-border trade.
- Condition: The domestic order and invoice carry only the classification their purpose uses (the CPC trade classification may stay), or the example states a domestic regulatory use of the HS code.
- Options: Preferred: drop the HS code and the origin country from the domestic documents. Alternative: keep them if a Bayvarran rule requires them, and say so in the world story.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `BF-PO-26-0637` is `10-Order.xml`; quantity, price and tax treatment agree with it.
- Penalty 1.5 % of 6 480.00 = 97.20; due date 2026-04-08 is 30 days after 2026-03-09.
- Payment channel MPNS (mass payment net system) with the domestic rail LUMEPAY fits a domestic payment, while the cross-border invoice `08-Invoice.xml` uses the real-time Trade Accord rail.
