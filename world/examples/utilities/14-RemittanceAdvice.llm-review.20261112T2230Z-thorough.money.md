# LLM review: 14-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/14-RemittanceAdvice.xml`, Git blob `13ca288b96ca5f33f56aefe8db004930ea15062a` (committed)
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

### utilities/14#F1 · Medium · Remittance number and payment-order references copied from Valdara's remittance for another invoice
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `VT-0313`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0313`
- Why: Velumi Trading sends this advice under Valdara Industries' remittance number from 04 (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`), and 07 uses the same number. Its payment-order references end in 0313, the number of Ferrano's invoice paid in 04, not the number of ST-INV-26-0323 paid here. `PaymentOrderReference` is "an internal reference to the order for payment from the payer to the payer's bank", so these values point to another payer's payment.
- Condition: The remittance ID is unique in the flow and belongs to the payer, and the payment-order references are Velumi's own.
- Options: (a, preferred) Velumi's own numbering (for example VT-RM-…, VT-PAY-…).
- Needs decision: no

### utilities/14#F2 · Medium · Credit transfer to a current account that carries a blockchain identifier
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:BlockchainID` = `CORAL-NET-L1`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: `BlockchainID` is "An identifier of the Blockchain on which the crypto or stablecoin is being held". The payee account is a CACC current account in XLC, paid by credit transfer. This repeats invoice 13's account (13#F3), and the payer's own account, also XLC at the same bank, has no such identifier.
- Condition: The same as 13#F3. The remittance describes the account the same way as the corrected invoice.
- Options: (a, preferred) remove BlockchainID, together with 13.
- Needs decision: yes

### utilities/14#F3 · Low · Purpose "supplier payment" for a telephone bill whose lines say "telephone"
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:PaymentPurposeCode` = `SUPP`
- Why: Invoice 13 gives both lines the ISO 20022 purpose PHON, TelephoneBill (`13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:PaymentPurposeCode` = `PHON`). The remittance uses the generic SUPP. The same is in 04 and 07.
- Condition: The remittance line's purpose is that of the invoice it pays.
- Options: (a, preferred) PHON.
- Needs decision: no

## Checked and consistent
- The debit of 135.566 equals invoice 13's PayableAmount. Credit 0.000, payment 135.566, balance 0.000.
- The advice is issued 2026-04-19, before the stated due date of 2026-04-23 (and before 2026-05-17 under the 45-day note), so no interest is due.
- PaymentID and InvoicingPartyReference RF26STINV260323 equal the invoice's reference (the ISO 11649 check passes).
- The payee account XL18BSEL0010004293889 equals the invoice's. The payer account XL40BSEL0010003665515 passes the IBAN-like check. Both are in XLC with three decimals.
