# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/14-RemittanceAdvice.xml`, Git blob `13ca288b96ca5f33f56aefe8db004930ea15062a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit f9f7596 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/14#F1 · High · Document ID belongs to another sender and is used by two other remittance advices
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `07-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- Why: The document ID is "An identifier for this document, assigned by the sender." The sender is Velumi Trading, whose own references carry the prefix VT (`/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`, `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VT-BANK-26-04`, `/RemittanceAdvice/cac:Signature/cbc:ID` = `VT-SIG-RA`). VI is Valdara Industries' prefix, and the same ID is used by Valdara's 04-RemittanceAdvice.xml and Brightmarket's 07-RemittanceAdvice.xml in the same profile execution.
- Condition: The document ID is Velumi's own and unique within the flow.
- Options: (a, preferred) a Velumi number with prefix VT and its own sequence number.
- Needs decision: no

### utilities/14#F2 · Low · Payment order references numbered after another party's invoice, and two references for one order
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0313`
- Why: PaymentOrderReference ("An internal reference to the order for payment from the payer to the payer's bank") and PayerReference ("An internal reference to the payer's order for payment") denote the same thing with two values. Both end in 0313, the number of Ferrano's invoice FE-INV-26-0313 paid in 04-RemittanceAdvice.xml (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`), not of the invoice paid here (ST-INV-26-0323); the values look derived from the other example.
- Condition: Velumi's own payment-order reference, given once (or two distinct, explained references).
- Options: (a, preferred) one Velumi payment-order number; drop PayerReference.
- Needs decision: no

### utilities/14#F3 · Low · Signature without method or reason
- XPath: `/RemittanceAdvice/cac:Signature/cbc:ID` = `VT-SIG-RA`
- Why: Only an ID and signatory; nothing says how or why the remittance advice is signed (rule "no fillers").
- Condition: A signature with a reason and the data that make it one, or none.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/14#F4 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VT-BANK-26-04`
- Why: The reference does not say what VT-BANK-26-04 is, and it is not an example of the flow.
- Condition: The reference states its document type, or is absent.
- Options: (a, preferred) add DocumentTypeCode or DocumentDescription.
- Needs decision: no

### utilities/14#F5 · Low · Payment purpose differs from the purpose the invoice gave
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `PHON`
- Why: The invoice asks for TelephoneBill on both lines; the remittance advice reports SupplierPayment without explanation.
- Condition: The purpose agrees with the invoice, or the difference is explained.
- Options: (a, preferred) PHON.
- Needs decision: no

### utilities/14#F6 · Low · The invoice is referenced twice in the line, and payer data the advice does not use
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `ST-INV-26-0323`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- Why: The line's BillingReference already identifies the invoice; the DocumentReference repeats it. The customs trader number has nothing to do with a payment, and the payer's contact for a remittance advice is accounts payable, not purchasing.
- Condition: Each reference and party detail serves the remittance advice; the payer's contact handles payments.
- Options: (a, preferred) drop the DocumentReference and the customs trader ID; give an accounts-payable contact.
- Needs decision: no

## Checked and consistent
- Amounts: invoice payable 135.566 (`13-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`) = debit = payment; no credit; balance 0.000.
- Timing: issued 2026-04-19, before the due date 2026-04-23 of invoice 13.
- References: ST-INV-26-0323 of 2026-04-02 is 13-Invoice.xml; RF26STINV260323 is the invoice's creditor reference; payee account XL18BSEL0010004293889 is the invoice's.
- check_ids.py: RF references and both IBAN-like accounts correct.
