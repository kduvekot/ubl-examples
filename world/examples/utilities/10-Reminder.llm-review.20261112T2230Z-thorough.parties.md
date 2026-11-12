# LLM review: 10-Reminder.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/10-Reminder.xml`, Git blob `11e7db92f151d2164c7a773e47dfe430253bad7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/10#F1 · Medium · A language code in LocaleCode
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/10#F2 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

## Checked and consistent
- Supplier and customer are those of the invoice reminded, `09-Invoice.xml`, described the same way.
- The return notice's `IssuerParty` is the Bank of Lumeport (`20411370`), the bank that holds Robin Ashdale's debited account (`BLUMXBLX`) and the only party that can return a direct debit "by your bank"; the bank has the same register number in the other examples that name it.
- `SignatoryParty` is the water company, the issuer of the reminder.

## Considered and refuted
- `/Reminder/cac:PayeeParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`: a payee equal to the supplier was suspected as redundant. Refuted: UBL defines `PayeeParty` here without a condition ("The Party who receives the Payment"), and the reminder changes the means of payment to a credit transfer, so stating the payee explicitly follows the rule that nothing is implied by absence.
- `/Reminder/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`: the customer's account in a reminder that asks for a credit transfer was suspected as copied master data. Refuted: it is the account from which the returned direct debit was collected, which the reminder is about (`/Reminder/cbc:Note` = `The direct debit was returned by your bank: insufficient funds.`), and from which the next direct debit will be taken.
- `/Reminder/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`: a receivables contact was expected. Refuted: customer service is a usual addressee for a household's questions about a returned payment.
