# LLM review: 11-RemittanceAdvice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/11-RemittanceAdvice.xml`, Git blob `d0c26e7bbd846569482f83cb92b801d665bd1d34` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/11#F1 · Medium · Province of Ferrano in Region instead of CountrySubentity
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the same document use CountrySubentity. The parts counted 219 occurrences in 104 example files.
- Condition: no Urvanian address carries the province in `cbc:Region`; it is in `cbc:CountrySubentity`.
- Options: (a) move it to CountrySubentity (preferred); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### plastics/11#F2 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. The parts counted 362 LocaleCode elements in 213 example files, all `en`.
- Condition: every LocaleCode holds a locale from a list its listID names, or is absent.
- Options: (a) drop it where the locale has no use (preferred, as parties and the wood merges); (b) `en-XB` with a locale list (broad, context).
- Needs decision: no
- From: broad (F2), parties (F2), context (F2)

### plastics/11#F3 · Low · Two different references for the payer's payment order
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `RP-0882`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `RP-PAY-26-0882`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `RP-PAY-26-0882`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank" and PayerReference "An internal reference to the payer's order for payment"; both name the payer's own payment order, here with two different values. `RP-PAY-26-0882` agrees with the instruction ID; `RP-0882` matches no other identifier in the flow (checked in the merge over the flow's `*.xml`) and reads like a shortened purchase order number (`01-Order.xml:/Order/cbc:ID` = `RP-PO-26-0882`), a different kind of reference.
- Condition: the payer's payment order has one reference, or PayerReference holds a reference of a distinct meaning that is not an order number.
- Options: (a) drop PayerReference (preferred: the payment order is identified twice already); (b) give it a value of its own kind (e.g. the payer's payment-run reference).
- Needs decision: no
- From: money (F1), context (F5)

### plastics/11#F4 · Low · The invoice is referenced twice on the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `RR-INV-26-0894`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `RR-INV-26-0894`
- Why: BillingReference/InvoiceDocumentReference is "A reference to an invoice"; the line's DocumentReference ("A reference to a document associated with this remittance advice line") repeats the same invoice with the same issue date and adds only a type code. Nothing uses the second reference (IND5).
- Condition: the paid invoice is referenced once in the line, in the billing reference; any DocumentReference refers to another document.
- Options: (a) drop the DocumentReference (preferred: the invoice reference already says what it refers to); (b) keep only the DocumentReference (less specific).
- Needs decision: no
- From: broad (F3), logistics (F1), context (F4)

### plastics/11#F5 · Low · Rinova's waste-recovery permit in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The payee's permit to recover plastic waste plays no part in a payment notice; master data copied into every document of the flow (IND5).
- Condition: no permit in the remittance advice.
- Options: remove it (preferred).
- Needs decision: no (parties said yes; aligned with broad, context and 06)
- From: broad (F5), parties (F4), context (F3)

### plastics/11#F6 · Low · Contacts do not fit the payment roles
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The payer that sends the remittance advice is reached in accounts payable, the payee that matches the payment in accounts receivable; an order desk and customer service in Sales are contacts for orders.
- Condition: the accounting parties' contacts handle payables and receivables, or are absent.
- Options: (a) role-specific contacts (preferred); (b) drop contacts the document does not need.
- Needs decision: no
- From: broad (F4), parties (F3), context (F6)

### plastics/11#F7 · Low · Both companies registered on 1 January 1996
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Two companies in two registers on New Year's Day 1996; the parts counted 271 occurrences in 181 example files. A default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (parties said no; aligned with broad, context and the wood merges)
- From: broad (F6), parties (F5), context (F7)

### plastics/11#F8 · Low · Italian text tagged as English, and Rinova rendered differently from the other documents
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:CertificateType` = `Operating permit`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- Why: (1) The street-name renderings tagged English are Italian ("Via del Riciclo", "Piazza della Banca"), and the legal form is Italian with an English gloss; a world convention of Italianate exonyms is not visible, and a legal form is not a proper name (parties F6). (2) In the documents Rinova issues (02–08, 10), its legal form and permit type carry an Urvanian and an English rendering, each tagged; in this Rivermouth-issued document (as in 01 and 09) they have one untagged rendering, while the address keeps both renderings and tags the English text `en-XB` instead of `en-XU` (parties F7). Broad refuted the tag difference for the bank address (each sender renders the address in its own English), a possible rule, but then not applied to all of Rinova's texts. Combined because the XPaths and the fix (one rendering rule for party master data) are shared; same as plastics/09#F20.
- Condition: every rendering tagged `en-…` is English or a proper name used as such, and Rinova's legal form, permit type and address carry the same renderings and tags in every document, or follow one recorded rule.
- Options: (a) record the naming convention, render the legal form in English, and describe Rinova identically everywhere as in its own documents (preferred: party master data does not change with the reader; aligned with the wood flow); (b) apply the issuer's-language rule to all texts.
- Needs decision: yes (the tagging rule is a world convention; parties said no for (2); aligned with the wood merges)
- From: parties (F6, F7)

## Checked and consistent
- Amounts (recalculated in the merge): debit 9 984 000 − credit 0 = payment 9 984 000 = line debit = `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000`; balance 0 (broad, money, logistics, context).
- Timing: issued and paid 2026-05-19, after the discount period (ended `10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-30`) and before the due date (`10-Invoice.xml:/Invoice/cbc:DueDate` = `2026-05-20`): no discount taken, no penalty due (broad, money, logistics, context).
- `RR-INV-26-0894` of 2026-04-20 resolves to 10 (flow index re-run in the merge); RF reference `RF89RRINV260894` as payment ID and invoicing-party reference equals the invoice's `PaymentID`; payee account equals the invoice's; payer account is Rivermouth's own; credit transfer `30` as requested; check digits pass `check_ids.py` (broad, money, logistics, parties).
- Purpose code `SUPP` fits payment of a supplier invoice; currency XUF as invoiced, paid from an XBL account (ordinary conversion) (money).
- `PaymentOrderReference` = `InstructionID` (`RP-PAY-26-0882`) (broad, money).
- Parties match 10 and are identical across the flow apart from the language renderings (parties).

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID`: Rivermouth's account copied from master data — refuted: here Rivermouth is the payer and the same account is the `PayerFinancialAccount` (`/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), so the document has a reason to carry it (redundant, not unused) (from broad, parties, context).
- `/RemittanceAdvice/cbc:InvoicingPartyReference`: an RF creditor reference in an element for an internal reference of the invoicing party — refuted: the definition continues "This may have been requested of the payer by the payee to accompany the payer's remittance", which is what the RF reference is (from broad, context).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` tagged `en-XB` here, `en-XU` in the invoice — broad refuted it (each sender renders the address in its own English); the merge keeps the inconsistency of the rule within F8 (from broad).
- `/RemittanceAdvice/cbc:PaymentOrderReference` = `RP-PAY-26-0882`: the payment order reuses the order number 0882 — refuted as a finding: the payer's own numbering may tie the payment to its purchase order (from logistics).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` could be real — refuted: real ICDs stay far below 0990 (from parties).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `BLUMXBLX` — refuted: fictional country code in positions 5–6 (from parties).

## Changed in the merge
- money/F1, context/F5 → F3: combined; added that `RP-0882` matches no other identifier of the flow (checked in the merge).
- broad/F5, parties/F4, context/F3 → F5: Needs decision changed from yes (parties) to no.
- broad/F6, parties/F5, context/F7 → F7: Needs decision yes (parties said no).
- parties/F6, parties/F7 → F8: combined, Needs decision yes (parties said no for F7), preferred option aligned with the wood flow.
- broad/F2, parties/F2, context/F2 → F2: preferred option set to dropping LocaleCode.
- Combined without change of severity: broad/F1, parties/F1, context/F1 → F1; broad/F3, logistics/F1, context/F4 → F4; broad/F4, parties/F3, context/F6 → F6.
