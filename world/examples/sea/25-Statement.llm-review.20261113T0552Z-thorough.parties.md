# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/25-Statement.xml`, Git blob `a032666792c16cd3abc0420251a04e56790287b6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/25#F1 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of the supplier in a statement of account. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/25#F2 · Medium · A language code in LocaleCode
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Statement/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/25#F3 · Low · The contacts do not fit a statement issued by the factor
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Statement/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/Statement/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: The statement is issued and signed by the factor "on behalf of Lumeway Distribution, whose receivables Harbourline Factoring holds", and tells Velumi what it owes. Velumi's contact is named Purchasing but is a customer service officer in Sales: name, title and department disagree, and none is accounts payable, which reconciles a statement. The factor's contact is its client relationship manager for client accounts; the factor's client is Lumeway, while the statement is addressed to the debtor, for whom debtor collections is the function. The supplier's contact is its sales customer service, although questions about the balance now go to the factor.
- Condition: Each contact's name, job title and department agree, and the customer's and payee's contacts are the functions that deal with the account balance.
- Options: (a) accounts payable at Velumi and debtor collections at Harbourline; Lumeway's contact dropped or its accounts receivable (preferred); (b) drop the contacts that do not serve the statement.
- Needs decision: no

### sea/25#F4 · Low · Velumi's Lisavu address and legal form are written differently than in its own documents
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings carry `languageID="en-XB"` (English as used in Bayvarra) and its legal form is in English only, without `languageID`. In the documents Velumi issues itself it is described with `en-XL` and the legal form in Lisavan and English (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). The tag follows the issuer's locale, not the language of the rendering; over `world/examples/*/*.xml`, English renderings of street and town names in Lisavu addresses carry `en-XL` 188 times, `en-XB` 141 times and `en-XU` 9 times (counted with lxml over *.xml).
- Condition: Velumi's address and legal form are described the same way as in the other examples of the flow.
- Options: (a) `en-XL` for English renderings of Lisavu names and the legal form in Lisavan and English everywhere (preferred: the rendering belongs to the place); (b) keep the issuer's locale and state the convention once in the address rules.
- Needs decision: no

### sea/25#F5 · Low · Tax registrations, share capital and customs numbers in a statement of account
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Statement/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: A statement of account lists the documents and payments on the account and the balance; the parties' sales-tax registrations, the supplier's share capital and the customs trader numbers play no part in it (the tax was settled on the invoice). They are copied from master data (section 4.8 of the review rules).
- Condition: The parties carry only the data a statement uses (identification, name, address, contact, the payee's account).
- Options: (a) drop the `PartyTaxScheme` aggregates, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Accounting supplier and seller (document and line 1) are Lumeway Distribution (`20410274`); accounting customer and buyer Velumi Trading (`IC41859`); originator and beneficiary the Port of Selanu (`IC41037`), all as in the invoice `22-Invoice.xml` the statement lists.
- Payee (document and line 1) and signatory are Harbourline Factoring (`20411233`), the payee and financing party of the invoice, and the payee account is in its name; the statement's prefix `HF` and the note make it the factor's statement for its client, which agrees with the assignment the invoice announces.
- Line 2 carries no payee, which fits a deposit "paid to the distributor before the invoice was assigned".
- Harbourline's description is identical to the invoice and the remittance advice (compared with a script); Lumeway's GLN passes its check digit.

## Considered and refuted
- `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name`: the distributor as accounting supplier of a statement the factor issues — refuted because the statement reports Lumeway's sale to Velumi; the factor appears as payee and signatory, which is how UBL's Statement, having no sender role, can show the issuer.
