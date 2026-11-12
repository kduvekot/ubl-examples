# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/07-RemittanceAdvice.xml`, Git blob `ff1d21cc9e8ef3dfbfbdbfde835f54314d67116b` (committed)
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

### utilities/07#F1 · Medium · Remittance number and payment-order references copied from Valdara's remittance for another invoice
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `BS-PAY-26-0313`
- Why: The advice is sent by Brightmarket Stores, but its number has Valdara Industries' prefix and is the number of Valdara's remittance in 04 (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`); 14 has it too. The payer's payment-order references end in 0313, the number of Ferrano Energy's invoice FE-INV-26-0313 paid in 04 (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`), not of the invoice paid here (CSWC-INV-26-0317). `PaymentOrderReference` is "an internal reference to the order for payment from the payer to the payer's bank"; a reference that looks like it belongs to another payer's payment of another invoice makes reconciliation with the bank statement (BS-BANK-26-04) unreliable.
- Condition: The remittance ID is unique in the flow and the payer's own; the payment-order references are Brightmarket's and do not echo another invoice's number.
- Options: (a, preferred) Brightmarket's own numbering (e.g. BS-RM-…, BS-PAY-…) with a sequence not derived from 04.
- Needs decision: no

### utilities/07#F2 · Low · Purpose "supplier payment" for a water bill whose lines say "water"
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- Why: Invoice 06 gives both its lines the ISO 20022 purpose WTER, WaterBill (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:PaymentPurposeCode` = `WTER`); the remittance uses the generic SUPP (SupplierPayment). Same in 04 and 14.
- Condition: The remittance line's purpose is that of the invoice it pays.
- Options: (a, preferred) WTER.
- Needs decision: no

## Checked and consistent
- Debit 238.22 = invoice 06 PayableAmount; credit 0.00; payment 238.22; balance 0.00.
- Issued 2026-04-19, before the due date 2026-04-23 of invoice 06: no penalty due, none taken.
- PaymentID and InvoicingPartyReference RF03CSWCINV260317 equal invoice 06's PaymentID (ISO 11649 check passes).
- Payee account XB21BLUM38010004189160 equals invoice 06's; payer account XB48BLUM38010001570935 passes the IBAN-like check; both in XBL.
- The sewage levy collected for the city (36.12) is included in the amount paid, as the invoice asks.
