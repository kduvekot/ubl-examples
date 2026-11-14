# LLM review: 36-RemittanceAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/36-RemittanceAdvice.xml`, Git blob `0d67d6237dbe199fe762a5dccb67b4360d07c700` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/36#F1 · High · The debit note is deducted as a credit, while the debit note makes the payer the debtor
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount` = `6.48`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cac:BillingReference/cac:DebitNoteDocumentReference/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `521.68`
- Why: The line deducts 6.48 from the payment and gives a debit note as the reason. In that debit note the supplier is the creditor and the department the debtor (`34-DebitNote.xml:/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`, payable 6.48), so by it the department would add 6.48, not deduct it; the payment would be 12.96 higher. The advice follows what the debit note means (the department's penalty), not what it encodes. Counter-argument (broad, logistics, context): the amount reduces what the department pays, which is what the penalty means; the mismatch lies in 34. As in 35 (F3), the merge keeps it because the two examples contradict each other, with the fix in 34: under 34/F1 option (a) this line and the totals stand.
- Condition: The line's side (debit or credit) agrees with who is creditor and debtor in the referenced document, and `TotalCreditAmount` and `TotalPaymentAmount` follow.
- Options: (a) correct the roles of the debit note (34/F1 (a)); this line then stands (preferred); (b) if the penalty becomes a credit note, reference it here as a credit note.
- Needs decision: yes (decided with 34/F1)
- From: money (F1); refuted by broad, logistics and context (carried as counter-argument)

### tender/36#F2 · Medium · The advice of an actual payment gives neither its date nor the amount in the currency that is paid
- XPath: `/RemittanceAdvice/cbc:IssueDate` = `2026-05-08`
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `20308.55`
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`
- Why: A remittance advice is "A document that specifies details of an actual payment". The invoice and the reminder ask for payment in ferra (`32-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XUF`, `35-Reminder.xml:/Reminder/cbc:PaymentCurrencyCode` = `XUF`) into a ferra account; the payer pays from a lume account. The advice gives every amount in lume, no amount in ferra (2030855 at the rate of 100 used throughout), no rate, and no date of payment (only the issue date). The date matters: the reminder's interest runs to 5 May and payment is asked by 12 May; and the forward purchase of ferra the flow cites as the department's hedge (BL-FX-26-0091, 32/F14) would fix the amount received here, the one document where it applies. The payee cannot reconcile the ferra credit on its account with the advice. Model note (checked in the gc): `RemittanceAdvice` has no payment currency or payment exchange rate; the line's `ExchangeRate` is "The rate of exchange between the currency of the Remittance Advice and the currency of the document described in the BillingReference"; the closest date is `PaymentMeans/PaymentDueDate` ("The date on which payment is due for this means of payment"). Broad rated both parts Medium (the purpose depends on them), money, logistics and context Low; the merge takes Medium.
- Condition: The advice states the date of the payment and the amount credited in the payee's currency, or the rate from which it follows.
- Options: (a) `PaymentMeans/PaymentDueDate` 2026-05-08 and the advice in ferra (`DocumentCurrencyCode` XUF, line amounts in ferra with each line's `ExchangeRate` to the lume of the documents paid) (preferred: it uses the elements the model has for it); (b) the date and "2030855 ferra transferred at 100" in the note; (c) pay and advise in lume, using the reminder's alternative payment currency, and say so.
- Needs decision: no
- From: broad (F1, F2), money (F3), logistics (F2), context (F3)

### tender/36#F3 · Medium · A province in `Region`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity`. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`.
- Options: move it to `CountrySubentity` (preferred); or record a postal-region convention.
- Needs decision: no
- From: broad (F3), parties (F2), context (F1)

### tender/36#F4 · Medium · A language code as locale
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code. 362 occurrences in 213 files.
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale from a locale list (broad).
- Needs decision: no
- From: broad (F3), parties (F1), context (F2)

### tender/36#F5 · Medium · The department described as a company in a commercial register, with a liquidation status
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: A municipal department (ISIC 8411) has no liquidation status and is not in a commercial register as a company; the register number itself is not questioned.
- Condition: The department carries no liquidation status, and its register is not typed as commercial.
- Options: (a) drop the status and type the register neutrally (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F5), context (F6), broad (F5)

### tender/36#F6 · Low · The department pays interest that its own contract does not make due
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount` = `22.23`
- XPath: `/RemittanceAdvice/cbc:Note` = `Payment of the first release, with the interest.`
- Why: The department pays the reminder's interest in full, with a payment authorisation. Its contract says `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` and contains no interest clause; the department itself penalised the installation as late on 6 April (34), so the invoice was not overdue on 1 May by its own terms, and the interest is "Urvania's statutory interest" (35). The advice reports the payment correctly; what it reports follows 32/F5 and 35/F1. Money rated it Medium (a contradiction in the flow's payment story), broad and context Low; the merge takes Low, because the cause and its fix lie in 32 and 35.
- Condition: The interest paid is due under the payment terms the world decides for the contract.
- Options: (a) decide with 32/F5 and 35/F1; if the contract's term stands, the interest line falls away (payment 20286.32) or is recalculated (preferred); (b) change the contract's term and add an interest clause, which makes this advice right.
- Needs decision: yes
- From: broad (F4), money (F2), context (F4)

### tender/36#F7 · Low · The payment authorisation is referenced by ID only, and again inside the interest line's billing reference
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- Why: "A reference to an additional document associated with this document", without type, description or date; the document is not in the flow (`grep -l '>PWD-PAY-AUTH-26-0412<'` over `world/examples/*/*.xml`: this example only). It reads as the department's internal payment authorisation, which means nothing to the supplier unless named. Inside line 4 it sits in a `BillingReference` ("A reference to a billing document associated with this remittance advice line"); an internal authorisation is not a billing document of the interest (the reminder is, and is referenced). Counter-argument (broad): the interest is the item that needed a separate authorisation, and the header reference covers the payment. The merge keeps it: if so, the advice should say so.
- Condition: The reference states what the document is; it appears on a line only if it concerns that line, outside the billing reference or with the reason stated.
- Options: (a) `DocumentType` "Payment authorisation" at header level and no copy on line 4 (preferred); (b) keep the line copy and say that the interest needed its own authorisation.
- Needs decision: no
- From: logistics (F1), context (F5); refuted by broad (carried as counter-argument)

### tender/36#F8 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName[2]` = `Piazza della Banca`
- Why: Here (issued by the department) Valdara's renderings are tagged `en-XB` and the legal form appears once, untagged; in the Urvanian-issued examples `en-XU` and `qau` + `en-XU` (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). The tag follows the issuer; could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated.
- Options: (a) `en-XU` everywhere (preferred); (b) the issuer's tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F6)

### tender/36#F9 · Low · Payment advised by the procurement office to the sales order desk
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: A payment advice is exchanged between those who pay and those who reconcile receipts; the invoice was routed to the department's accounts payable (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`).
- Condition: Finance contacts, or none.
- Options: (a) accounts contacts (preferred); (b) drop `Contact`, `Department` and `MarkAttention`.
- Needs decision: no
- From: parties (F3), broad (F5)

### tender/36#F10 · Low · The payer describes the payee with master data the advice does not use
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: A remittance advice tells the payee what was paid for which documents; the payee's share capital, listing and warehouse provider (whose contact has no means of contact) are not used, and here it is the payer who copies them (section 4.8). Counter-argument (parties): the listing describes a listed company's legal entity.
- Condition: These appear only in documents whose purpose uses them.
- Options: (a) remove them (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: parties (F7), context (F7), broad (F5)

### tender/36#F11 · Low · Party tax exemption reason worded as a transaction
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` "A reason for the party's exemption from tax"; the text begins with a kind of sale. Only its second half is the party's status.
- Condition: The party-level reason states the party's status.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F4)

## Checked and consistent
- Totals (re-done): debits 20808.00 + 22.23 = 20830.23 = `TotalDebitAmount`; credits 515.20 + 6.48 = 521.68 = `TotalCreditAmount`; 20830.23 − 521.68 = 20308.55 = `TotalPaymentAmount` = `35-Reminder.xml:/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20308.55`; four lines = `LineCountNumeric`.
- Each line equals the payable amount of its document: invoice VI-INV-26-0221 20808.00 (net of withholding), credit note VI-CN-26-0222 515.20, debit note LPWD-DOC-26-0223 6.48, reminder VI-DOC-26-0224 22.23 (interest), whose issue date 2026-05-05 is quoted correctly. All four references exist and are of the kind their elements name.
- Issue 8 May is after the reminder and before its new due date (12 May); the settlement discount (until 10 April) is rightly not taken; no tax representative is carried here.
- Payment reference RF48VIINV260221 is the invoice's; payment means 30 as requested; payee account, holder, branch and bank as on the invoice and the reminder; payer account at the Bank of Lumeport (branch 380100 in the account number). `check_ids.py` (re-run): RF reference, both IBAN-like accounts and ISIN correct; BLUMXBLX and CREVXUFR carry the user-assigned codes XB and XU.
- Parties: the department (sender, LPWD prefix) pays; Valdara is the payee, as in the documents the lines refer to. The credit note is set off as its document-level terms say (33/F1).

## Considered and refuted
- `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID`: the authorisation given twice — refuted by broad (the interest needed a separate authorisation); logistics and context raised it: F7, with broad's argument.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount`: a debit note as a credit — refuted by broad, logistics and context (the mismatch is in 34); money raised it: F1, with their argument.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount`: the withholding tax (69.48 net) not shown — refuted, the lines carry payable amounts net of it and the tax goes to the treasury (from broad, money).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BLUMXBLX a real BIC — refuted, country part XB is user-assigned (from broad, parties).
- `/RemittanceAdvice/cbc:TotalPaymentAmount`: the 2 % settlement discount — not applicable, payment after the discount period (from broad).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount`: pays only 22.23 of the reminder's 20308.55 — refuted, lines 1 to 3 pay the rest against their own documents (from money).
- `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID`: one reference for four documents — refuted, it identifies the payment; the lines give the breakdown (from money).
- `/RemittanceAdvice/cbc:ID`: `LPWD-RM-26-0225` continues the flow-wide running number — refuted, an identifier of the payer's own prefix (from logistics).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount`: the payer's full bank details — refuted, the paying account identifies the transfer for the payee (from context).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:ReminderDocumentReference/cbc:IssueDate`: an issue date only on this reference — refuted, correct and harmless (from context).
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` (`-1`), `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 2648 0548`, `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: malformed offset, real country code, real ICD — each refuted (from parties).
- `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties; kept in F10; check digit and fictional prefix confirmed.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:StreetName`: the bank's address shorter than its description as a party elsewhere — refuted, a shorter form of the same address (from parties).

## Changed in the merge
- money/F1 → F1: kept High, yes, although three parts refuted it, as 35/F3; tied to 34/F1.
- broad/F1 + broad/F2 (Medium) + money/F3 + logistics/F2 + context/F3 (Low) → F2: combined into one Medium finding (date and currency of the payment), because the document's purpose depends on both; options adjusted to the model (no payment currency or rate in a remittance advice; checked in the gc).
- broad/F4 (Low) + money/F2 (Medium) + context/F4 (Low) → F6: Low, yes; the cause lies in 32 and 35.
- logistics/F1 + context/F5 → F7: combined; broad's refutation added.
- broad/F5 split into F9 (contacts), F10 (master data) and F5 (department, raised to Medium as analysis, with parties/F5 and context/F6).
- parties/F4 → F11: preferred option changed to keeping the code and rewording the text, aligned with the other tender merges.

## Outside this review
- Whether 20308.55 lume arrive as 2030855 ferra at 100, and who bears the charges (SHAR in the invoice), cannot be read from the advice (context); see F2.
