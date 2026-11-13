# LLM review: 06-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/06-RemittanceAdvice.xml`, Git blob `e26eebc8bac0997744bbae65cf8d2aa86a65b428` (committed)
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

### cotton/06#F1 · Low · The payment reference the invoice asked for is not quoted
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentID` = `RF77SCGSBI260194`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF77SCGSBI260194`
- Why: A Remittance Advice is "A document that specifies details of an actual payment". The
  self-billed invoice it settles instructs the payer to quote the creditor reference
  RF77SCGSBI260194 with the transfer. The remittance advice carries neither a PaymentID nor an
  InvoicingPartyReference, so the transfer it announces cannot be matched by that reference; the
  other remittance advice of the flow does quote it
  (`18-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF46SCGINV260210`).
  The billing references still link the lines to 04 and 05, so the advice is usable without it.
- Condition: the remittance advice quotes the payment reference requested in 04, or the story says
  why it is not used (e.g. the net amount after set-off has its own reference).
- Options: (a, preferred) add PaymentID RF77SCGSBI260194 to the payment means (or as
  InvoicingPartyReference on line 1).
- Needs decision: no

### cotton/06#F2 · Low · The farm's physical location in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: Party/PhysicalLocation is "The physical location of this party". A remittance advice
  announcing a bank transfer does nothing with where the farm's fields are; the aggregate (with
  coordinates and the website as InformationURI) reads as copied master data (UBL IND5). Same in 01,
  04 and 05.
- Condition: the supplier party of the remittance advice carries no PhysicalLocation.
- Options: (a, preferred) leave it out.
- Needs decision: no

## Checked and consistent
- 3,210.320 (payable of 04) − 69.250 (payable of 05) = 3,141.070 = TotalPaymentAmount; the line
  amounts are the payable amounts of the referenced documents, and both references resolve.
- Payer account (ginnery, XL31BSEL0020004922263) and payee account (farm, XL67BSEL0020004817534,
  as in 04) pass `check_ids.py`; the payee account is the one 04 asks to be paid into.
- Issue date 2026-02-16 is the due date of 05 and before the due date of 04 (2026-03-24), which
  fits the set-off the credit note announces.
- Roles: the ginnery as accounting customer (payer) and the farm as accounting supplier fit a
  self-billing settlement.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Selanu Cotton Ginnery Ltd`:
  payer account in a remittance advice suspected as unneeded — refuted because it tells the payee
  which account the transfer comes from, which is part of the details of an actual payment.
