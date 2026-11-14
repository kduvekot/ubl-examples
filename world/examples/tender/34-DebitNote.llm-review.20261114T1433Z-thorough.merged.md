# LLM review: 34-DebitNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/34-DebitNote.xml`, Git blob `b6bf3671341fe2437750245b0f5de26efdc18dc0` (committed)
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

### tender/34#F1 · High · The department's penalty claim is encoded with the supplier as creditor and the department as debtor
- XPath: `/DebitNote/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6.48`
- Why: A debit note is "A document used to specify debits due to the Creditor from the Debtor"; its structure follows the invoice: the accounting supplier is the creditor, the accounting customer the debtor, and `PayableAmount` is "The amount of the monetary total to be paid". The ID ("An identifier for this document, assigned by the sender") is in the department's series (LPWD-DOC-26-…, its notices and the contract), and the claim is the department's penalty against Valdara. With Valdara as accounting supplier and the department as customer, the document says the opposite: that the department owes Valdara a further 6.48. The later documents read it as meant, not as encoded: `35-Reminder.xml:/Reminder/cac:ReminderLine[3]/cbc:Note` = `The department's penalty, set off.` with `35-Reminder.xml:/Reminder/cac:ReminderLine[3]/cbc:CreditLineAmount` = `6.48`, and `36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount` = `6.48`; both reduce what the department pays. So the roles of this document contradict 35 and 36 and its own number (High). The same pattern was found in furniture/14 and sea/28 (analysis/review-merge-decisions.md: High, needs decision). A buyer-raised debit note is known commercial practice (money), but UBL's document has no such reading.
- Condition: The party to whom the penalty is owed is the creditor of the document, the party owing it the debtor, the ID is assigned by the issuing party, and 35 and 36 treat the amount accordingly.
- Options: (a) keep the debit note as the department's claim and swap the accounting parties: the department as `AccountingSupplierParty`, Valdara as `AccountingCustomerParty` (preferred by money and parties, and as furniture b and sea d decided for the same pattern; 35 and 36 keep their credit lines); (b) a `SelfBilledCreditNote` issued by the department, referenced downstream as a credit note (preferred by context); (c) a credit note from Valdara for the penalty under a VI number (logistics' alternative); (d) keep the roles, say so in a note, and record that UBL has no buyer-issued debit note (broad's acceptable option).
- Needs decision: yes
- From: money (F1), broad (F3), parties (F1), logistics (F2), context (F1)

### tender/34#F2 · High · A penalty for late installation of a service the invoice billed as supplied on 31 March
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `3`
- XPath: `/DebitNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-04-06`
- Why: The debit note of 6 April charges three days of delay of the release's installation. The invoice it refers to billed the installation of all 40 benches with `32-Invoice.xml:/Invoice/cbc:TaxPointDate` = `2026-03-31` (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`), i.e. as supplied by then. Both cannot be true: either the installation was done by 31 March and was not late (the procedure's requested delivery date is 2 April, `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate` = `2026-04-02`), or it was late in April and billed before it was done. The same contradiction is 32/F2, seen from the invoice.
- Condition: The installation is billed after it is done, and the penalty for its delay is consistent with the invoice's dates.
- Options: (a) bill the installation later (32/F1, F2), which makes this penalty consistent (preferred); (b) drop the penalty.
- Needs decision: yes
- From: broad (F1)

### tender/34#F3 · Medium · Three days late, but no date the delay is counted from or to
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `One day waived`
- XPath: `/DebitNote/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: Clause PEN-1 is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.` "Late" needs a due date and a completion date; the document's purpose (claiming a per-day penalty) depends on them. The debit note has no period on document or line, and the documents it cites give none: the order has no installation line and no delivery date (26), the order response promises none (28), the invoice billed the installation as done on 31 March (F2). The only candidate in the flow is the call's requested delivery date of 2 April; three days from it end on 5 April, the day before this note, but that is a reconstruction. The debtor cannot verify which three days are charged or which one is waived.
- Condition: The debit note states the due date and the completion date (or the period of delay), and the due date can be found in the order or contract.
- Options: (a) an `InvoicePeriod` on the line (e.g. 2026-04-03 to 2026-04-05) with the due date in the note, after the order has been given an installation date (preferred by broad and logistics); (b) the dates in the note only; (c) a reference to the acceptance record of the release (context).
- Needs decision: yes (the installation's due and completion dates are new facts of the story)
- From: broad (F2), logistics (F1), context (F4)

### tender/34#F4 · Medium · A province in `Region`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity`. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`.
- Options: move it to `CountrySubentity` (preferred); or record a postal-region convention.
- Needs decision: no
- From: broad (F4), parties (F2), context (F2)

### tender/34#F5 · Medium · A language code as locale
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code. 362 occurrences in 213 files.
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale from a locale list (broad).
- Needs decision: no
- From: broad (F4), parties (F3), context (F3)

### tender/34#F6 · Medium · The department described as a company in a commercial register, with a liquidation status
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: A municipal department (ISIC 8411) has no liquidation status and is not in a commercial register as a company; the register number itself is not questioned.
- Condition: The department carries no liquidation status, and its register is not typed as commercial.
- Options: (a) drop the status and type the register neutrally (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F8), context (F6), broad (F6)

### tender/34#F7 · Low · The line's withholding tax (1.08) is not the document's (0.72)
- XPath: `/DebitNote/cac:DebitNoteLine/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.08`
- XPath: `/DebitNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `0.72`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:WithholdingTaxTotalAmount` = `0.72`
- Why: The document has one line; its withholding is 1.08 (10 % of 10.80), the document's 0.72 (10 % of 7.20 after the document-level allowance "One day waived"). Money rated this High: the lines' withholding does not add up to the document's. Broad rated it Low and saw a way to reconcile it: the document-level allowance would have to carry its own share (−0.36). The merge could not settle it either way: a document-level allowance reduces the base after the lines, as it does for a tax total, so a line amount before the allowance is a possible reading; but UBL gives no rule that line withholding is stated before document allowances, and the allowance here carries no tax. The amount used further on is the document's (10.80 − 3.60 − 0.72 = 6.48; 72.00 − 1.80 − 0.72 = 69.48 in 35).
- Condition: The withholding of the line and of the document reconcile (by the line amount, by the allowance's own share, or by having the withholding at document level only).
- Options: (a) apply the waiver on the line (two days, or a line allowance), so the line is 7.20 with 0.72 (preferred by money); (b) give the withholding only at document level (broad); (c) give the allowance its tax share.
- Needs decision: yes
- From: money (F2), broad (F5)

### tender/34#F8 · Low · Zero tax total and withholding without category, rate or scheme; withholding "on services of non-residents" on a penalty
- XPath: `/DebitNote/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/DebitNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `0.72`
- Why: `TaxAmount` is "The total tax amount for a particular taxation scheme, e.g., VAT; the sum of the tax subtotals …"; neither total names its scheme, category, base or rate. For the 0.00 the reader cannot tell which tax was considered for a contractual penalty; for the 0.72 only the invoice shows that it is the 10 % withholding on non-residents' services, which is deducted from a payment for a service, while a penalty is not a service. The figure makes sense only if the penalty is read as a reduction of the invoiced installation price, whose withholding falls in proportion; the document does not say so. Counter-arguments: broad refuted the zero total (a penalty is outside the taxes of the invoice and the total merely says no tax); context refuted the withholding (the penalty reduces the installation price, so reducing the withholding is consistent, and 35 follows it). The merge keeps the finding for the missing subtotals and the unstated reading.
- Condition: Each tax amount has a subtotal with base, category, rate and scheme, or is absent; the document states that the penalty reduces the invoiced installation price if the withholding is to follow it.
- Options: (a) drop the zero tax total, give the withholding a subtotal (7.20, 10 %, the invoice's scheme) and add to the note that the penalty reduces the installation price (preferred); (b) charge the penalty without withholding (payable 7.20) and adjust 35 and 36.
- Needs decision: yes
- From: money (F3); refuted in part by broad and context (carried as counter-arguments)

### tender/34#F9 · Low · The penalty is calculated on the installation price before the credit note
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `10.80`
- Why: 10.80 = 3 × 0.5 % × 720.00, the invoice's installation line. Two days earlier the supplier credited one installation (`33-CreditNote.xml:/CreditNote/cac:CreditNoteLine[2]/cbc:LineExtensionAmount` = `18.00`), so the release's installation price stood at 702.00: 3 × 0.5 % × 702.00 = 10.53 (recomputed; a day 3.51). The clause names no base, so either can be defended, but the note's wording points to the price as it stands.
- Condition: The base is stated and equals an amount found in the billing documents at the date of the debit note.
- Options: (a) keep 720.00 and word the note "of the installation price invoiced (720.00)" (preferred by money); (b) recalculate on 702.00 (line 10.53, allowance 3.51, withholding 0.70, payable 6.32) and adjust 35 and 36 (broad).
- Needs decision: no
- From: money (F4), broad (F5)

### tender/34#F10 · Low · The supplier's tax representative on the department's penalty note
- XPath: `/DebitNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: As 32/F15: register number and name only, no tax registration. This document is the department's claim with a tax total of 0.00; Valdara's tax representative has no function in it, least of all in a document the customer draws up.
- Condition: As 32/F15.
- Options: (a) remove it (preferred); decided together with 32/F15.
- Needs decision: yes
- From: broad (F6), money (F5), parties (F9), context (F5)

### tender/34#F11 · Low · Contract cited by the procurement file number
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: PWD-2026-PARKS is the procurement file (`24-TenderContract.xml:/TenderContract/cbc:ContractFolderID` = `PWD-2026-PARKS`); the contract document is `24-TenderContract.xml:/TenderContract/cac:ContractDocumentReference/cbc:ID` = `PWD-CONTRACT-2026-PARKS`. Counter-argument (logistics): the number is used the same way in 21–24, 26 and 32. Consistency does not make it the contract's identifier; as 32/F19.
- Condition: The contract reference uses the contract's identifier.
- Options: as 32/F19.
- Needs decision: no
- From: broad (F6); refuted by logistics (carried as counter-argument)

### tender/34#F12 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Here (issued by the department) Valdara's renderings are tagged `en-XB` and the legal form appears once, untagged; in the Urvanian-issued examples `en-XU` and `qau` + `en-XU` (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). The tag follows the issuer; could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated.
- Options: (a) `en-XU` everywhere (preferred); (b) the issuer's tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F4)

### tender/34#F13 · Low · Accounting parties described with their procurement and sales contacts
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: For a billing document the contacts are those who book and pay (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`); here procurement and the sales order desk, as in the tender documents.
- Condition: Accounts contacts in billing documents, or none.
- Options: (a) accounts contacts (preferred); (b) drop `Contact`, `Department` and `MarkAttention`.
- Needs decision: no
- From: parties (F5)

### tender/34#F14 · Low · Supplier's master data that a penalty claim does not use
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: A penalty claim identifies the party it is addressed to; share capital, listing and warehouse provider (whose contact has no means of contact) have no part in it, least of all in a document the customer draws up (section 4.8). Counter-argument (parties): the listing describes a listed company's legal entity.
- Condition: These appear only in documents whose purpose uses them.
- Options: (a) remove them (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: parties (F6), context (F7), broad (F6)

### tender/34#F15 · Low · Party tax exemption reason worded as a transaction
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` "A reason for the party's exemption from tax"; the text begins with a kind of sale. Only its second half is the party's status.
- Condition: The party-level reason states the party's status.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F7)

## Checked and consistent
- Penalty arithmetic (re-done): 0.5 % × 720.00 = 3.60 a day; 3 days = 10.80 (line and `LineExtensionAmount`); allowance 3.60 = `AllowanceTotalAmount`; 10.80 − 3.60 = 7.20 = `TaxExclusiveAmount`; 10 % × 7.20 = 0.72; 7.20 − 0.72 = 6.48 = `PayableAmount`, the amount 35 and 36 use. 7.20 is 1 % of 720.00, below the clause's cap of 10 % (72.00).
- The withholding of the three billing documents nets to the buyer's payment to the tax office: 72.00 − 1.80 − 0.72 = 69.48 (35).
- Clause PEN-1 exists in the call and the contract with the rate used; allowance indicator false, reason code 64 ("Special agreement", UNTDID 5189) and the text "One day waived" agree.
- References: order LPWD-PO-26-0212 (26), invoice VI-INV-26-0221 (32) and contract file PWD-2026-PARKS exist; issue 6 April follows the invoice (31 March) and the credit note (4 April).
- Unit DAY for the debited quantity fits a per-day penalty.
- Parties: the two of the invoice and the order, described identically (parties, by script); `check_ids.py` (re-run): ISIN correct.

## Considered and refuted
- `/DebitNote/cac:TaxTotal/cbc:TaxAmount`: a tax total of 0.00 without category — refuted by broad (a penalty is outside the scope of the invoice's taxes); money raised the missing subtotals: F8, with broad's argument.
- `/DebitNote/cac:WithholdingTaxTotal`: a withholding tax on a penalty — refuted by context (the penalty reduces the installation price, so the withholding falls with it); kept in F8 for the unstated reading.
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity`: days as a quantity of items, without a price — refuted, the debited thing is days of delay, the unit says so and the note gives rate and base (from broad, logistics, context).
- `/DebitNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: list 5189 for a reason — refuted, 5189 is the list UBL practice uses for allowance reasons and 64 fits (from broad).
- `/DebitNote/cac:AllowanceCharge/cbc:Amount`: a waiver as a document allowance instead of charging two days — refuted, the result is the same and the reason is stated; its effect on the line's withholding is F7 (from money).
- `/DebitNote/cac:OrderReference/cbc:ID`: the order does not contain the installation — refuted as a finding of this document, the reference identifies the release; the missing order line is 32/F1 and 26's (from money, context).
- `/DebitNote/cbc:DocumentCurrencyCode`: no payment means or terms for the 6.48 — refuted, the amount is set off (35, 36) (from money).
- `/DebitNote/cac:ContractDocumentReference/cbc:ID`: contract number equal to the file number — refuted by logistics (consistent with 21–24, 26, 32); broad raised it: F11, with logistics' argument.
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` (`-1`): malformed — refuted (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: real country code — refuted, +999 not assigned (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties; kept in F14; check digit and fictional prefix confirmed.
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: real ICD — refuted (from parties).

## Changed in the merge
- money/F1 (High) + broad/F3, parties/F1, logistics/F2, context/F1 (Medium) → F1: High, yes, aligned with analysis/review-merge-decisions.md ("debit note with accounting supplier/customer reversed: High, yes"), because the roles contradict 35, 36 and the document's own number; all parts' options kept, swapping the parties preferred as in furniture b and sea d.
- broad/F2 + logistics/F1 (Medium, no) + context/F4 (Low, yes) → F3: Medium, Needs decision yes, because the fix adds due and completion dates to the story.
- money/F2 (High) + broad/F5 (Low, withholding part) → F7: Low, Needs decision yes; the merge could neither confirm nor refute that a line amount before a document allowance is wrong; both arguments in Why.
- money/F4 + broad/F5 (base part) → F9: combined; both options kept.
- broad/F6 split into F10 (tax representative), F14 (master data), F6 (department, raised to Medium as analysis) and F11 (contract reference).
- context/F5 (Low, no) → F10: Needs decision yes, as 32/F15 and the other parts.
- parties/F8 + context/F6 (Low) → F6: Medium, as analysis.
- parties/F7 → F15: preferred option changed to keeping the code and rewording the text, aligned with the other tender merges.

## Outside this review
- Whether the four missing anchor sets (29) caused the delay, on which days the installers (Saltmere Engineering) worked, and whether 39 or 40 installations were late, are timeline questions across the documents (broad, logistics, context, money).
