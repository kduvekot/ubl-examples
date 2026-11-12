# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### wood/11#F1 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/11#F2 · Low · Invoice without delivery (collection) date
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-09`
- XPath: `10-Order.xml:/Order/cbc:IssueDate` = `2026-03-08`
- Why: The invoice, issued the morning after the order, does not say when the timber was collected at the yard (no Delivery/ActualDeliveryDate or InvoicePeriod), so the reader cannot tell whether it bills goods already collected or in advance, which also determines the tax point for the sales tax (own knowledge).
- Condition: The invoice states the date the goods were collected or delivered.
- Options: (a, preferred) Add Delivery/ActualDeliveryDate.
- Needs decision: no

### wood/11#F3 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact is Brackenmere's trade sales desk, which sells furniture; an invoice goes to accounts payable. The supplier's contact is the sawmill's sales office, not accounts receivable.
- Condition: The accounting parties' contacts are the ones that handle this invoice.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/11#F4 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day).
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 12 × 540 = 6480.00; tax 0.00 under category E/RESALE as in the order; totals 6480.00 throughout.
- Payment terms: issued 2026-03-09, due 2026-04-08 (30 days net); penalty 1.5 % × 6480.00 = 97.20; penalty period from 2026-04-09.
- RF02MSINV260638 passes ISO 11649 and IBAN-like XB78BLUM38712004398618 passes its check (check_ids.py); the payee account is the same as in 08-Invoice.xml.
- Order reference BF-PO-26-0637 resolves to 10-Order.xml; quantity, price and item agree.
- Domestic payment channel (MPNS, LUMEPAY) for a payment inside Bayvarra, against RTNS on the Trade Accord rail for the cross-border invoice 08: consistent.

## Considered and refuted
- `/Invoice/cac:PaymentMeans` without ChargeBearerCode, unlike 08 — refuted: a domestic transfer has no shared foreign charges to allocate.
