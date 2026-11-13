# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/25-Statement.xml`, Git blob `a032666792c16cd3abc0420251a04e56790287b6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/25#F1 · Low · A deposit received before the statement period is listed as a movement of the period
- XPath: `/Statement/cac:StatementPeriod/cbc:StartDate` = `2026-05-14`
- XPath: `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`
- Why: the statement covers 2026-05-14 to 2026-06-13; line 2 credits the deposit received on
  2026-05-09, five days before the period starts, as an ordinary line. Line 1 is marked as not
  brought forward (BalanceBroughtForwardIndicator false), and line 2 carries no such indicator,
  so the reader cannot tell that this credit belongs to an earlier date. (The deposit itself is
  consistent with `22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:ReceivedDate` = `2026-05-09`.)
- Condition: every line dated outside the statement period is either marked as brought forward or
  the period covers its date.
- Options: (a, preferred) start the period at the date of the deposit or of the order; (b) present
  the deposit as part of the invoice's balance (as the invoice does with its PrepaidAmount).
- Needs decision: no

### sea/25#F2 · Low · Factoring agreement and assignment referenced by number only
- XPath: `/Statement/cac:AdditionalDocumentReference/cbc:ID` = `HF-FA-2026-007`
- XPath: `/Statement/cac:StatementLine[1]/cac:DocumentReference/cbc:ID` = `HF-ASSIGN-26-0091`
- Why: neither reference says what the document is. In 22-Invoice.xml the same numbers are the
  factoring contract (TradeFinancing/ContractDocumentReference) and a further trade-financing
  document (TradeFinancing/DocumentReference, by its number the assignment); here,
  as a bare AdditionalDocumentReference and line DocumentReference, the debtor reading the
  statement cannot tell. The note "whose receivables Harbourline Factoring holds" depends on them.
- Condition: both references state their document type.
- Options: add DocumentType (or DocumentTypeCode) "Factoring agreement" and "Notice of
  assignment".
- Needs decision: no

## Checked and consistent
- `/Statement/cac:StatementLine[1]/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `LD-INV-26-0147`
  with issue date 2026-05-14 matches 22-Invoice.xml; its charges 2950.00 + 140.00 = 3090.00 equal
  the invoice's; the due date 2026-06-28 and the factor's account equal the invoice's.
- Issue 2026-06-13 08:43 is the period's end date; the statement precedes the credit note
  26-CreditNote.xml (2026-06-15) that refers to it.
