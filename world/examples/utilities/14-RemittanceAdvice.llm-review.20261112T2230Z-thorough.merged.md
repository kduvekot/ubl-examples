# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/14-RemittanceAdvice.xml`, Git blob `13ca288b96ca5f33f56aefe8db004930ea15062a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/14#F1 · High · Document ID of Valdara Industries' remittance advice, shared by three remittance advices of the flow
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/RemittanceAdvice/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: The document ID is "An identifier for this document, assigned by the sender." The sender is Velumi Trading, whose own references here carry the prefix VT (VT-PAY-26-0313, VT-BANK-26-04, VT-SIG-RA). VI-RM-26-0316 is Valdara Industries' prefix and the ID of Valdara's advice `04-RemittanceAdvice.xml` (sequence 0316 of the Ferrano documents), and Brightmarket's `07-RemittanceAdvice.xml` uses it too: verified in the merge, the ID occurs in exactly these three files (`grep -rl --include='*.xml' 'VI-RM-26-0316'`), all in profile execution UTILITIES-2026-01. A reference to the ID is therefore ambiguous, and the prefix names another party. Refutation tried: nothing makes the ID a shared collection or batch number (each advice pays one invoice of a different payer to a different payee).
- Condition: The document ID is one Velumi Trading assigns, and unique within the flow.
- Options: (a, preferred) a Velumi number with prefix VT and its own sequence (e.g. VT-RM-26-…); the same kind of fix in 07.
- Needs decision: no
- From: broad (F1, High), context (F1, High), logistics (F1, High), money (F1, Medium, part), parties (F1, Medium, part)

### utilities/14#F2 · Medium · Credit transfer to a current account that carries a blockchain identifier
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:AccountFormatCode` = `ISO13616`
- Why: BlockchainID is "An identifier of the Blockchain on which the crypto or stablecoin is being held". The payee account is an ISO 13616 current account in XLC, paid by credit transfer, copied from `13-Invoice.xml` (13#F2); the payer's own account in this same advice, also XLC at the same bank, has no such identifier, so the transfer is bank to bank.
- Condition: As 13#F2: BlockchainID only for an account holding crypto or stablecoins on that chain; the remittance describes the account the same way as the corrected invoice.
- Options: (a, preferred) remove BlockchainID, together with 13; (b) as in 13, if Coral is a ledger currency in the world.
- Needs decision: yes
- From: money (F2), context (F3); logistics (noted under "Checked")

### utilities/14#F3 · Low · Payment-order references numbered after another party's invoice, and two references for one order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0313`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PayerReference` = `VI-0313`
- Why: PaymentOrderReference is "An internal reference to the order for payment from the payer to the payer's bank" and PayerReference "An internal reference to the payer's order for payment"; they denote the same thing with two values. Both end in 0313, the number of Ferrano Energy's invoice FE-INV-26-0313 that 04 pays with VI-PAY-26-0313 / VI-0313, not of Selanu Telecom's invoice ST-INV-26-0323 paid here; the values look copied from 04 with the prefix changed (same pattern in 07).
- Condition: Velumi's own payment-order reference, not borrowing an unrelated invoice's number, given once (or two distinct, explained references).
- Options: (a, preferred) one Velumi payment-order number (e.g. VT-PAY-26-0323 or a Velumi sequence) as PaymentOrderReference and InstructionID, and drop PayerReference.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2), money (F1, part), parties (F1, part)

### utilities/14#F4 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VT-BANK-26-04`
- Why: No type, description or issuer says what VT-BANK-26-04 is or why the payee needs it, and no example carries it; same pattern in 04 and 07.
- Condition: The reference says what kind of document it is, or is absent.
- Options: (a, preferred) add a DocumentTypeCode or DocumentDescription; (b) remove it.
- Needs decision: no
- From: broad (F4), context (F5, part), logistics (F3)

### utilities/14#F5 · Low · Signature without method or reason
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `VT-SIG-RA`
- Why: Only an ID and the signatory; nothing says how or why the remittance advice is signed (no fillers). A convention across the world: 137 of the 147 Signature aggregates in `world/examples/*/*.xml` hold only ID and SignatoryParty (counted with lxml in the merge).
- Condition: A signature with a reason and the data that make it one, or none.
- Options: (a, preferred) remove it; (b) add the signature method and reason.
- Needs decision: yes
- From: broad (F3)

### utilities/14#F6 · Low · Payer's customs trader number in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: Velumi's customs trader number has nothing to do with paying a domestic telephone bill; it is Velumi's party data repeated in every example that carries it.
- Condition: The customs trader number appears here only with a use in this document.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (F6, part), parties (F2), context (F6, part)

### utilities/14#F7 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 companies of the world are registered on 1 January 1996 (parties' count), Selanu Telecom and Velumi Trading among them; recounted in the merge: 271 occurrences in 181 files. A shared default (no fillers). For Selanu Telecom, `SMALL` is also questionable for the island's operator; on a small island it may still be intended.
- Condition: Both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits its story, the same in every example.
- Options: (a, preferred) a registration date of its own for each company, and review the operator's size; (b) drop the elements where the documents do not need them.
- Needs decision: yes
- From: parties (F3)

### utilities/14#F8 · Low · Payer's contact: "Purchasing" with a sales job title and department
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name and job title/department contradict each other, and on a remittance advice the payer's contact is the one who answers for the payment (accounts payable), not purchasing or sales. The contact is the same in every example with Velumi's full data.
- Condition: Name, job title and department agree, and the function deals with payments.
- Options: (a, preferred) an accounts-payable contact for Velumi in the payment documents; (b) drop the job title and department.
- Needs decision: no
- From: broad (F6, part), parties (F4), context (F6, part)

### utilities/14#F9 · Low · Purpose "supplier payment" for a telephone bill whose lines say "telephone"
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `PHON`
- Why: Invoice 13 gives both lines the ISO 20022 purpose PHON (TelephoneBill); the remittance reports the generic SUPP (SupplierPayment) without explanation. The same is in 04 and 07.
- Condition: The remittance line's purpose is that of the invoice it pays, or the difference is explained.
- Options: (a, preferred) PHON.
- Needs decision: no
- From: broad (F5), money (F3), context (F4)

### utilities/14#F10 · Low · The invoice referenced twice in the line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `ST-INV-26-0323`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `ST-INV-26-0323`
- Why: The line's BillingReference already identifies the invoice; the DocumentReference repeats it without saying anything more.
- Condition: Each document is referenced once per line.
- Options: (a, preferred) keep the BillingReference only.
- Needs decision: no
- From: broad (F6, part), context (F5, part)

## Checked and consistent
- Amounts (redone in the merge): invoice payable 135.566 (`13-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`) = TotalDebitAmount = DebitLineAmount = TotalPaymentAmount; credit 0.000; balance 0.000.
- Timing: issued 2026-04-19, before the stated due date 2026-04-23 of invoice 13 and before 2026-05-17, the date "45 days net" gives (13#F1); no interest due.
- References: ST-INV-26-0323 of 2026-04-02 is `13-Invoice.xml`; PaymentID and InvoicingPartyReference RF26STINV260323 are the invoice's creditor reference; payee account XL18BSEL0010004293889 is the invoice's; payer account XL40BSEL0010003665515 is named "Velumi Trading Ltd" and is Velumi's account in the sea flow as well; both at Bank of Selanu, branch 001, in XLC with three decimals.
- Payer Velumi Trading and payee Selanu Telecom are the accounting customer and supplier of `13-Invoice.xml`, with the same register numbers and descriptions; SignatoryParty is Velumi, the issuer.
- check_ids.py: RF references and both IBAN-like accounts correct.

## Considered and refuted
- `/RemittanceAdvice/cbc:TotalCreditAmount`: 0.000 stated — refuted, a zero credit total is an actual statement of a debit-only advice (from context).

## Changed in the merge
- broad/F1, context/F1, logistics/F1 (High) with the ID part of money/F1 and parties/F1 (Medium) → F1: High (a broken, ambiguous document identity shared by three documents; section 6). The payment-order part of money/F1 and parties/F1 went to F3 (Low, with broad, context and logistics): different elements and severity.
- broad/F3 → F5: Needs decision no → yes, aligned with the air, rail and utilities 01–07 merges (signature convention).
- broad/F6 and context/F5, F6 split by element into F4, F6, F8 and F10.
- parties/F3 → F7: count recalculated (271 in 181 files).
