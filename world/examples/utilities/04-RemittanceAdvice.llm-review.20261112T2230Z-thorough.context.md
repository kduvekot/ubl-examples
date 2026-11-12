# LLM review: 04-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/04-RemittanceAdvice.xml`, Git blob `ed53a13de1ca0b9a4d9a62d8bc6c094c15743208` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/04#F1 · Low · TaxTotal repeats the invoice's VAT only, before the discount taken
- XPath: `/RemittanceAdvice/cac:TaxTotal/cbc:TaxAmount` = `2516028`
- XPath: `/RemittanceAdvice/cbc:TotalCreditAmount` = `301923`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- Why: A remittance advice "specifies details of an actual payment". The TaxTotal gives the invoice's VAT (2516028) but not its excise (288840), and not the VAT on what was actually paid after the 2 % settlement discount (the discount of 301923 is taken on the tax-inclusive amount, so about 50321 of it is VAT). The figure is neither the tax in the payment nor the complete tax of the invoice, and nothing in the advice uses it.
- Condition: The remittance advice carries a tax total only if it states the tax contained in the payment (or the invoice's complete tax, said as such), or carries none.
- Options: (a, preferred) remove TaxTotal; (b) state the VAT contained in the payment after the discount.
- Needs decision: no

### utilities/04#F2 · Low · Payment purpose "supplier payment" where the invoice names an energy bill
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `ELEC`
- Why: PaymentPurposeCode is "A code signifying the business purpose for this payment" (ISO 20022 ExternalPurpose1Code). The invoice asks for ELEC (ElectricityBill) and GASB (GasBill); the payer reports the generic SUPP. ISO 20022 has the specific codes precisely for utility bills, and the invoice states them.
- Condition: The purpose code agrees with the purpose the invoice gives, or is absent.
- Options: (a, preferred) ELEC (the larger part of the payment), or one line per purpose; (b) leave the code out.
- Needs decision: no

### utilities/04#F3 · Low · Additional document reference with only an ID
- XPath: `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID` = `VI-BANK-26-04`
- Why: "A reference with only an ID says what it refers to where that is not obvious." VI-BANK-26-04 has no type code or description, and no example carries it; it may be a bank statement or a payment order batch.
- Condition: The reference says what document it is (DocumentTypeCode or DocumentDescription), or is removed.
- Options: (a, preferred) add a type and description; (b) remove it.
- Needs decision: no

### utilities/04#F4 · Low · The line references the same invoice twice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0313`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `FE-INV-26-0313`
- Why: The invoice is already referenced as the line's billing document; the generic DocumentReference ("A reference to a document associated with this remittance advice line") repeats it with type "Invoice" and adds nothing.
- Condition: Each referenced document appears once per line, in the most specific element.
- Options: (a, preferred) keep BillingReference only.
- Needs decision: no

### utilities/04#F5 · Low · Payer master data the remittance does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: Listed shares, logistics provider, customs trader number and a sales order desk play no part in a payment advice; the contact for a payment would be accounts payable.
- Condition: The payer carries what the advice uses.
- Options: (a, preferred) remove them; use an accounts payable contact.
- Needs decision: no

## Checked and consistent
- References FE-INV-26-0313 resolve to `02-Invoice.xml` (issue date 2026-04-02 agrees).
- 15096168 − 301923 = 14794245 = TotalPaymentAmount; balance 0. The discount is taken on 2026-04-10, inside the settlement period 2026-04-02 to 2026-04-12 of the invoice; the note says so.
- PaymentID / InvoicingPartyReference RF58FEINV260313 equal the invoice's PaymentID; payee account equals the invoice's PayeeFinancialAccount.
- InvoicePeriod March 2026 agrees with the invoice.

## Considered and refuted
- `/RemittanceAdvice/cac:Signature`: a signature with only an ID and party — refuted because a signature reference on a payment advice is a legitimate business element and nothing contradicts it.
- `/RemittanceAdvice/cbc:PaymentOrderReference`: equals PaymentMeans/InstructionID — refuted because the payment order and the instruction are the same object seen from the payer and from the payment means.

## Outside this review
- The ID of this advice, VI-RM-26-0316, is reused by `07-RemittanceAdvice.xml` and `14-RemittanceAdvice.xml` (findings there).
