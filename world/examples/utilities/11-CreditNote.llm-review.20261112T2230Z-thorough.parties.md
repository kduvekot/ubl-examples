# LLM review: 11-CreditNote.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/11-CreditNote.xml`, Git blob `831c5f12acb5889efdae887718f56b4fd27594fc` (committed)
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

### utilities/11#F1 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/11#F2 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

### utilities/11#F3 · Low · The collection credit line names the beneficiary but not the party the levy was collected for
- XPath: `/CreditNote/cac:CollectionCreditNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: the credit note corrects the collection line of `09-Invoice.xml`, which states both the beneficiary and the party on whose behalf the levy is collected (`09-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`). The credit line keeps only `BeneficiaryParty`, although its note says the levy is "credited for the city" and `CreditNoteLine` also has `CollectedForParty` ("The Party on whose behalf this item or amount is collected"). Under the rule that nothing is implied by absence, the credit line no longer says on whose behalf the credited amount had been collected, and it describes the third party differently from the line it corrects.
- Condition: the collection credit line names the third party in the same roles as the invoice line it corrects.
- Options: (a) add `CollectedForParty` (Lumeport Public Works Department, `20410548`) to the credit line (preferred: it mirrors invoice 09); (b) if only one role is wanted, use the same one in invoice and credit note.
- Needs decision: no

## Checked and consistent
- Supplier and customer are those of the invoice credited, `09-Invoice.xml`, described the same way; the beneficiary carries the same register number `20410548` as in 06 and 09.

## Considered and refuted
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`: the customer's account in a credit note without payment means was suspected as copied master data. Refuted: the credit note offers a refund as an alternative (`/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`), and the account is where a refund would go.
