# LLM review: 34-DebitNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/34-DebitNote.xml`, Git blob `b6bf3671341fe2437750245b0f5de26efdc18dc0` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 5660045 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/34#F1 · High · A penalty for late installation of a service that the invoice billed as supplied on 31 March
- XPath: `/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `3`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-04-06`
- XPath: `/DebitNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`
- Why: the debit note of 6 April charges three days of delay in installing the release's benches. The invoice it refers to billed the installation of all 40 benches with the tax point `32-Invoice.xml:/Invoice/cbc:TaxPointDate` = `2026-03-31` (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`), i.e. as a supply made by then. Both cannot be true: either the installation was done by 31 March and was not late, or it was late in April and was billed before it was done.
- Condition: the installation is billed after it is done, and a penalty for its delay is consistent with the dates of the invoice.
- Options: (a) bill the installation later (see 32 F1), which makes this penalty consistent (preferred); (b) drop the penalty.
- Needs decision: yes (when release 1 was installed)

### tender/34#F2 · Medium · The penalty counts days late, but no document says when the installation was due
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: clause PEN-1 is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.` "Late" needs a due date. The order cited here contains no installation line and no delivery or completion date (26), the order response promises none (28), and the debit note itself gives neither the due date nor the date of completion: it has no period, only "3 days". The debtor cannot verify the count.
- Condition: the debit note states the due date and the completion date (or the period of delay), and the due date can be found in the order or contract.
- Options: (a) add the period of delay on the line (InvoicePeriod or in the Note: due date, completed date) and a completion date for the installation in the order (preferred).
- Needs decision: no

### tender/34#F3 · Medium · The department's claim is drawn up with the department as customer and the supplier as creditor
- XPath: `/DebitNote/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: a debit note is "A document used to specify debits due to the Creditor from the Debtor", and in UBL the accounting supplier is the party that claims and the accounting customer the party that owes. Here the penalty is owed by Valdara to the department: the document is numbered in the department's series (LPWD-DOC…), and the remittance advice deducts it from the payment (`36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount` = `6.48`). Read by its roles, however, it says that Valdara debits the department with a penalty for Valdara's own late installation. The creditor of the debit is in the debtor's role.
- Condition: the party to whom the penalty is due is recognisable as the creditor of the document, and the party owing it as the debtor.
- Options: (a) keep the trade roles but say so explicitly (a note that the document is issued by the customer and the amount is due to it), if the world's convention is to keep supplier/customer fixed (acceptable); (b) issue the penalty with the department as AccountingSupplierParty (creditor) and Valdara as customer (preferred by the definition); (c) let Valdara issue a credit note for the penalty.
- Needs decision: yes (which document and roles the world uses for a customer's penalty claim)

### tender/34#F4 · Medium · Language code in LocaleCode; province in Region
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/34#F5 · Low · Withholding tax on the line and in the total differ; the base ignores the credit note
- XPath: `/DebitNote/cac:DebitNoteLine/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.08`
- XPath: `/DebitNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `0.72`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `10.80`
- Why: the only line carries 1.08 of withholding tax (10 % of 10.80), the document 0.72 (10 % of 7.20 after the waived day). A document total that is not the sum of its lines' amounts needs the allowance to carry its own share (−0.36), which it does not. The penalty base is "the installation price of the release", taken as 720.00 (40 × 18.00); two days earlier the credit note (33) had taken one installation back, so the release's installation price is 702.00 and a day is 3.51, not 3.60.
- Condition: line and document withholding amounts reconcile; the penalty base is the installation price after the credit note, or the note says it is the price as invoiced.
- Options: (a) give the withholding only at document level, and compute on 702.00 (preferred); (b) charge two days on the line instead of three days less an allowance.
- Needs decision: no

### tender/34#F6 · Low · Tax representative, seller master data and company attributes of the department in a penalty note
- XPath: `/DebitNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: the note claims a contractual penalty. A tax representative of the seller (without tax registration, see 32), the seller's logistics provider and stock listing have no function in it, least of all in a document the department draws up. The department carries a company liquidation status. The contract is cited by the number that is also the procurement file (see 24).
- Condition: the parties carry what the penalty claim uses; the contract reference uses the contract's identifier.
- Options: (a) remove them (preferred).
- Needs decision: no

## Checked and consistent
- Arithmetic: 0.5 % × 720.00 = 3.60 per day; 3 days = 10.80; one day waived −3.60 = 7.20 (tax exclusive); withholding 10 % × 7.20 = 0.72; payable 7.20 − 0.72 = 6.48, the amount the remittance advice (36) and the reminder (35) use. 7.20 is 1 % of 720.00, well under the clause's ceiling of 10 %.
- Clause PEN-1 exists in the contract (24) with the rate used; allowance reason 64 is "Special agreement" in UNTDID 5189 and fits a waived day.
- The reduction of the withholding tax is coherent: the penalty lowers the price of the withheld service, so the tax withheld on it falls by 10 % of the penalty.
- Invoice reference VI-INV-26-0221 (32) and order reference (26) resolve; issue 2026-04-06 follows both.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/DebitNote/cac:TaxTotal/cbc:TaxAmount`: a tax total of 0.00 without category — refuted, a penalty is outside the scope of the taxes of the invoice and the total merely says no tax.
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity`: days as a debited quantity without a price — refuted, the note gives the rate per day and the base.
- `/DebitNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: list 5189 (allowance or charge identification) for a reason — refuted, 5189 is the list UBL practice uses for allowance reasons and 64 fits.

## Outside this review
- Whether four missing anchor sets (29) caused the delay, and on which days the installers worked, are timeline questions.
