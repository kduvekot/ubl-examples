# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
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

### packaging/02#F1 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "the political or administrative division of a country ... such as ... province", i.e. `CountrySubentity`, which the Bayvarran addresses of the same invoice use for `Coastal State`. 104 examples carry a province in `Region` (`grep -rl --include='*.xml' '<cbc:Region>Province' world/examples | wc -l`).
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds an actual region.
- Options: (a) preferred: move the value to `CountrySubentity`; (b) keep `Region` only with a value that is a region.
- Needs decision: no

### packaging/02#F2 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language that `Language/ID` already gives, not a locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale (language and region) from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/02#F3 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: The customer's warehousing and despatch provider has no role in billing 480 kg of stretch film collected FCA by the buyer's carrier (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`), and the customer's listed shares have none either. Both are copied from Valdara's master data (84 examples contain `Castrano Logistics`, `grep -rl --include='*.xml'`).
- Condition: the invoice carries no customer aggregate it does not use, or states why it does.
- Options: (a) preferred: leave ServiceProviderParty and SecurityListing out; (b) give Castrano a role in this delivery if that is the story.
- Needs decision: no

### packaging/02#F4 · Low · Invoice contacts are order desks, not the accounting contacts
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: An invoice is addressed between the accounting parties; the customer's contact is the one who receives and pays invoices (accounts payable), the supplier's the one who answers invoice queries (accounts receivable). Here both are order desks, and the customer's sits in Sales with the title `Customer service officer`, a seller's description. The pattern is world-wide: 89 examples have a contact named `Purchasing` or `Buying office` in Sales, and 229 carry `Customer service officer` (XPath count and `grep -rl --include='*.xml'`).
- Condition: the accounting parties' contacts in the invoice have an accounting function (job title or department) fitting their role.
- Options: (a) preferred: accounts payable / receivable contacts for the accounting parties; (b) leave the contacts out of the invoice if the parties have only one general contact.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521` resolves to `01-Order.xml`; parties, item, quantity 480 KGM, price 3.1 XBL/KGM and the tax treatment agree with the order.
- Arithmetic: 480 × 3.1 = 1488.00 throughout; penalty 1.5 % × 1488.00 = 22.32 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount`; due date 2026-06-01 is 30 days after the issue date 2026-05-02, the penalty period starts the day after.
- `check_ids.py`: RF reference and IBAN-like account pass.
- The supplier's account appears both under the party and as `PayeeFinancialAccount`; both have the same ID, and an invoice does use it.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount`: seller account repeated at party level — refuted because the invoice requests payment to that account; the repetition is not unused data.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile`: circularity data on an invoice line — refuted because the recycled content is part of what is sold and billed.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Urvanian street tagged `en-XB` here but `en-XU` in `01-Order.xml` — refuted because the tag consistently follows the sender's country (the Bayvarran supplier writes English as used in Bayvarra); the text is the same.
- `/Invoice/cbc:AccountingCost`: `Raw materials and parts` — refuted as in the order: stretch film can be booked as material.
