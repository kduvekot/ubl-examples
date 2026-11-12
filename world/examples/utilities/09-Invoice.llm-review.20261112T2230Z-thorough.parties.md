# LLM review: 09-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/09-Invoice.xml`, Git blob `f578132e365ef70fff8b3b325066166662819a4a` (committed)
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

### utilities/09#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/09#F2 · Medium · PayerParty of the mandate is the debtor
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UBL defines `PaymentMandate/PayerParty` as "The Party, if different from the debtor, that makes the Payment." The debtor of this invoice is its accounting customer Robin Ashdale, and the mandate's payer is the same person (and the payer account is the debtor's own account). The condition of the definition is not met.
- Condition: `PayerParty` is present in the mandate only when someone other than the debtor pays.
- Options: (a) remove `PayerParty` from the mandate (preferred: the definition makes its absence mean that the debtor pays; the payer account stays); (b) keep it only if the story has someone else pay Robin's water bill.
- Needs decision: no

### utilities/09#F3 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

### utilities/09#F4 · Low · The customer's bank account given twice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerFinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: the account to be debited is stated where the invoice uses it, in the direct debit mandate ("The payer's financial account"). The same account, with its full bank and branch description, is repeated under the customer's `Person` ("The financial account associated with this person"), where the invoice does nothing with it; the block is the person's master data, repeated in every example that carries Robin Ashdale.
- Condition: the debtor's account appears in this invoice only where the payment uses it.
- Options: (a) drop the account from `Person` here (preferred); (b) keep it only with a reason the mandate does not cover.
- Needs decision: no

## Checked and consistent
- Supplier Coastal State Water Company and customer Robin Ashdale match statement `08-UtilityStatement.xml` (sender, receiver, subscriber) and are described as in 08, 10 and 11.
- The mandate account is named after the account holder Robin Ashdale; the payee account `XB21BLUM38010004189160` is named "Coastal State Water Company Ltd" and is the supplier's account in 06, 07 and 10.
- The collection line names Lumeport Public Works Department (`20410548`) as the party collected for and as beneficiary, as in invoice 06.
- No `BuyerCustomerParty` or `SellerSupplierParty`: for a household water bill the accounting parties are the parties of the sale; nothing else is implied.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`: a private person as accounting customer without tax or register identifiers was questioned. Refuted: a household has none to give.
