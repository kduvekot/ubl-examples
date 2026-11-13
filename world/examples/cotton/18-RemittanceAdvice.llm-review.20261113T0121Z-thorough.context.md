# LLM review: 18-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/18-RemittanceAdvice.xml`, Git blob `47eb48a5adfeabc95404a79c9aab2a6843d04e46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/18#F1 · Low · The line repeats the header's parties and references the invoice twice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `SCG-INV-26-0210`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:DocumentReference/cbc:ID` = `SCG-INV-26-0210`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: The only line pays invoice SCG-INV-26-0210, and says so twice: once in BillingReference
  ("A reference to a billing document associated with this remittance advice line"), once as a
  generic DocumentReference with type Invoice. The line's accounting supplier and customer ("related
  to the remittance information reported on this Remittance Advice Line") are the header's parties;
  line-level parties serve a remittance that covers invoices of several parties, which this one does
  not. The repetitions add nothing (UBL IND5).
- Condition: the invoice is referenced once on the line, and line-level parties appear only where
  they differ from the header's.
- Options: (a, preferred) keep the BillingReference and leave the DocumentReference and the line
  parties out.
- Needs decision: no

## Checked and consistent
- TotalDebitAmount, line amount and TotalPaymentAmount 6,055.452 XLC = PayableAmount of 16;
  balance 0.000 after payment; billing reference and issue date resolve to 16.
- PaymentID and InvoicingPartyReference RF46SCGINV260210 are the reference 16 asks to be quoted; the
  payee account XL31BSEL0020004922263 is the ginnery's account of 16; the payer account is the mill's
  at the Bank of Lumeport (both pass `check_ids.py`).
- Issued 2026-03-29, before the due date of 16; PaymentPurposeCode SUPP (supplier payment) fits.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`: a Lume
  account paying a coral amount without an exchange rate — refuted because the advice tells the
  payee what it receives (coral); the conversion is the payer's bank's matter and is not required
  for remittance.
- `/RemittanceAdvice/cbc:TotalCreditAmount` = `0.000`: suspected as a filler — refuted because it
  states positively that no credits are set off, which IND6 (nothing implied by absence) favours.
