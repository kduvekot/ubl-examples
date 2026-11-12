# LLM review: 05-Invoice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/05-Invoice.xml`, Git blob `a846f2c92225b4f657cb71040b2ccfd1f8ecfc9d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/05#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language code again, and the invoice already gives `en` as `DefaultLanguageCode`. 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale with a matching listID.
- Options: (a, preferred) `en-XB` from a locale list (BCP 47); (b) drop it.
- Needs decision: no

### mast/05#F2 · Low · Contacts that do not fit invoicing
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers questions about the invoice (accounts receivable), and the accounting customer's contact handles the invoice on the buyer's side (accounts payable). Here they are Saltmere's procurement "Bids office" and Selanu Telecom's sales desk "Business accounts" (customer service officer).
- Condition: the accounting supplier's contact is a billing or accounts-receivable contact, and the accounting customer's contact an accounts-payable contact.
- Options: (a, preferred) billing contacts for both parties.
- Needs decision: no

### mast/05#F3 · Low · Selanu Telecom described differently than in the order and the waybill
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: In 01 and 03 Selanu Telecom's legal form is given in Lisavan and English with `languageID`s, and its English address renderings are tagged `en-XL`; here the legal form has one rendering without `languageID`, and the English address renderings are tagged `en-XB` (the issuer's country). The same party should be described the same way in every example.
- Condition: Selanu Telecom's legal form and address renderings are the same, with the same `languageID`s, in every example of the flow.
- Options: (a, preferred) both legal-form renderings with their tags, and English address renderings tagged by the address's country, everywhere.
- Needs decision: no

### mast/05#F4 · Low · Registration date 1 January 1996
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is the registration date of 25 different companies in 181 examples (lxml count and `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`); it reads as a default, not as Selanu Telecom's history.
- Condition: the company's registration date is its own, or absent.
- Options: (a, preferred) the date from the company history; (b) drop it.
- Needs decision: yes (company histories)

## Checked and consistent
- Roles: Saltmere Engineering is AccountingSupplierParty and SellerSupplierParty, Selanu Telecom AccountingCustomerParty and BuyerCustomerParty, as in the order (01) and the despatch advice (04); identifiers, names, address IDs, tax ID, contacts and endpoints agree.
- Payee account `XB69BLUM38712001885122` is in the name of Saltmere Engineering, the accounting supplier; its check digits are valid (check_ids.py), and the branch "Marrowdale branch" is in Saltmere's town. The bank identifier `BLUMXBLX` uses the country part `XB`, which is not an ISO 3166 country assigned to a real country, so it cannot be a real BIC.
- No PayeeParty or PayerParty: payee and payer are the accounting parties, which is correct.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID`: the seller's state sales-tax number on an invoice taxed at 0 % for export — refuted because the seller's tax registration belongs on its invoice whatever the tax treatment of the supply.
