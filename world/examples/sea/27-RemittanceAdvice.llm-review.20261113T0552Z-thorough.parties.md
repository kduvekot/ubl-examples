# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/27-RemittanceAdvice.xml`, Git blob `a83f4a9e20f100a4540611eef91ece79f8f5dfa3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/27#F1 · High · The factor as accounting supplier of the invoice line, against the header and the invoice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The line's `AccountingSupplierParty` is "the Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line", i.e. the accounting supplier of the invoice the line pays. That invoice names Lumeway Distribution (`22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`), as do this document's header and the line's own seller. The factor bought the receivable and is the payee (it is already named as the line's `PayeeParty`); it did not become the invoice's accounting supplier. The line contradicts the header and the invoice it references.
- Condition: The line's accounting supplier is the invoice's accounting supplier (Lumeway Distribution, `20410274`), and the factor appears only as payee.
- Options: (a) Lumeway as the line's `AccountingSupplierParty` (preferred: matches the invoice and the header); (b) drop the line-level accounting supplier, since it equals the header's.
- Needs decision: no

### sea/27#F2 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of the supplier in a remittance advice paid to the factor. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/27#F3 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/27#F4 · Low · The contacts do not fit a payment to the factor
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: Velumi, the payer, gives as its contact Purchasing, a customer service officer in Sales: name, title and department disagree, and none of them is accounts payable, which made the payment. The factor's contact is its client relationship manager for client accounts, but in this payment Velumi is the factor's debtor, not its client; the factor's cash allocation or debtor collections is the function that matches the payment. Both are master-data contacts used in every role.
- Condition: Each contact's name, job title and department agree, and the payer's and payee's contacts are the functions that deal with the payment.
- Options: (a) accounts payable at Velumi and cash allocation or debtor collections at Harbourline (preferred); (b) drop the contacts.
- Needs decision: no

### sea/27#F5 · Low · Tax registrations, share capital and customs numbers in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: A remittance advice tells the payee which documents a payment settles; the parties' sales-tax registrations, the supplier's share capital and the customs trader numbers play no part in it. They are copied from master data (section 4.8 of the review rules).
- Condition: The parties carry only the data a remittance advice uses.
- Options: (a) drop the `PartyTaxScheme` aggregates, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Header accounting customer (Velumi Trading, `IC41859`) and supplier (Lumeway Distribution, `20410274`) match the invoice `22-Invoice.xml` and the credit note `26-CreditNote.xml`; the payee (Harbourline Factoring, `20411233`) is the invoice's payee, and the payee account `XB51BLUM38020502304038` is the invoice's, in the factor's name.
- The payer account is in Velumi's name (`Velumi Trading Ltd`) at a Lisavu bank, with the holder's country `XL`, which fits the payer.
- Velumi's address and legal form carry `en-XL` and Lisavan renderings, as in its other documents; Harbourline's and Lumeway's descriptions are identical to the invoice (compared with a script).
- Line 1's buyer, seller, originator and beneficiary match the invoice; GLN, IBAN-like accounts and RF references pass their checks (check_ids.py).

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount`: the credit line names no accounting supplier or payee — refuted as a parties finding because the header names both and the line inherits them; whether the factor accepts the deduction is noted in the credit note's review.
