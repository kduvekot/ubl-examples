# LLM review: 11-Invoice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/11-Invoice.xml`, Git blob `d14230a475262f9f8b47c7b7e1cbf9ab963fc61a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### wood/11#F1 · Medium · Language code 'en' in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "a code signifying the locale in which this language is used". A locale is a language as used in a region or country; the example itself distinguishes locales of English in its `languageID` attributes (`en-XB`, `en-XU`). The value `en` with `listID="ISO 639"` is a language code only and repeats `Language/cbc:ID`, so the element carries a meaning other than its definition. The Urvanian parties in the flow carry no `LocaleCode` at all, so the parties are also described unevenly. The same value occurs 362 times in 213 examples (`grep '<cbc:LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: Every `cbc:LocaleCode` in this example either holds a locale (language and country, e.g. `en-XB`) with a list identifier for locales, or is absent.
- Options: (Preferred) a locale value such as `en-XB` with a locale list (e.g. BCP 47), consistent with the `languageID` values the world already uses; or remove `LocaleCode` where the locale adds nothing to `Language/cbc:ID`.
- Needs decision: no

### wood/11#F2 · Low · Contact does not fit the party's role in this invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist question for a party in a role is whether its `Contact` fits the role. In this invoice: Marrowdale Sawmill as accounting supplier (Sales office / Customer service officer / Sales), whose contact should be the one who handles receivables: accounts receivable or credit control; Brackenmere Furniture as accounting customer (Trade sales / Customer service officer / Sales), whose contact should be the one who handles payables: accounts payable. A sales department and a customer service officer are the functions of a seller towards its customers; they do not fit a party acting as accounting customer or accounting supplier. The parties carry the same contact in every example of the flow, whatever role they have there (Valdara Industries' `Order desk` in Sales also as consignee, importer and accounting customer). Across all examples the job title `Customer service officer` occurs 395 times in 229 examples (`grep -o` over `*.xml`), with departments always `Sales`, including contacts named `Purchasing`, `Buying office` and `Goods inwards`, so the job title and department look like a default rather than a description of the contact.
- Condition: Each contact listed above has a name, job title and department that fit the role the party has in this invoice, and name, job title and department agree with each other.
- Options: (Preferred) give each party role-specific contacts in the world (purchasing, goods-in, despatch, customs, accounts) and pick the one for the role the party has in each document; alternatively drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no

### wood/11#F3 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "the registration date of the CompanyID". Here Brackenmere Furniture Ltd and Marrowdale Sawmill Ltd are each registered on 1996-01-01. Across all examples this date is given 271 times in 181 examples (`grep` over `*.xml`) for 25 different companies in all three countries' registers (Bayvarra's federal business register, the Urvanian commercial register and Lisavu's register), from a sawmill and a haulier to ports, an airport cargo terminal, a telecom company and an insurer (counted with lxml over every `PartyLegalEntity` in `*.xml`). A first of January shared by companies of every kind in three registers is not plausible as their actual registration dates and looks like a filler, which the rules exclude, unless the world has an event (e.g. a re-registration of all companies under the Trade Accord) that explains it.
- Condition: The registration date of each company in this example is either its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (Preferred) give each company its own registration date from its history in the world; or, if a 1996 re-registration is part of the story, record it there so the date has a reason; or leave the date out where the world has none.
- Needs decision: yes

## Checked and consistent
- Every full description of the same party in the flow was compared field by field (script over `*.xml`): Valdara Industries is described identically in its nine full descriptions (01–09) apart from the language renderings noted above; Marrowdale Sawmill identically in all eleven examples; Trasvia Haulage identically in 04, 05 and 06; Brackenmere Furniture identically in 10 and 11.
- Every short party reference (identifier and name only, e.g. signatories, `SellerSupplierParty`/`BuyerCustomerParty` next to the accounting parties, consignor, transport user, bill-to) carries the same register identifier as the full description of that party.
- Identifiers per party are consistent: register number in `PartyIdentification` = `PartyLegalEntity/CompanyID`; customs trader number, tax number and endpoint (`XB:20412329`, `XU:XU-R-104274` …) follow the party's country; tax schemes fit the country (Bayvarra: state sales tax STT, level STATE, Upland State; Urvania: VAT, level NATIONAL).
- `check_ids.py`: all check digits in this example pass.
- The payee account's name is the supplier's registered name (`Marrowdale Sawmill Ltd`), held at Bank of Lumeport in Bayvarra, the supplier's country.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9523710900008`: GLN — refuted as in `10-Order.xml` (GS1 prefix 952 is for examples; check digit correct).
