# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/24#F1 · High · A payment "made" 26 days after the response, with a remittance advice that does not exist yet
- XPath: `/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- Why: PaidDate is "the date on which this payment was made"; on 2026-05-30 a payment of
  2026-06-25 cannot have been made. The referenced remittance advice is
  `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:IssueDate` = `2026-06-25`, issued 26 days after
  this response, so the reference points to a document that does not yet exist when this one is
  issued. The English note itself speaks of the future ("the balance will be paid to the factor").
  Between the two dates the credit note 26-CreditNote.xml (2026-06-15) changes what is paid.
- Condition: the response reports no payment as made after its issue time and refers to no
  document issued after it; a planned payment, if stated, is not presented as made.
- Options: (a, preferred) drop the Payment (approval is the answer to the request) or keep only the
  intended due date in the note; (b) issue the response after 2026-06-25, which changes the story
  (approval only after payment).
- Needs decision: no

### sea/24#F2 · High · The payment's ID and amount differ from the remittance advice it refers to
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:ID` = `VT-PAY-26-0199`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- Why: the remittance advice named as this payment's remittance gives the payment instruction as
  `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
  (also its PaymentOrderReference) and the amount paid as
  `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00` (43778.00 less
  the 64.00 credit note). The same payment cannot have two instruction IDs and two amounts.
- Condition: if the response describes the payment at all, its ID, instruction ID and amount are
  those of the payment the remittance advice reports.
- Options: (a, preferred) resolved together with F1 by removing the Payment; (b) align ID and
  amount with 27-RemittanceAdvice.xml.
- Needs decision: no

## Checked and consistent
- `/InvoiceStatusResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147` is 22-Invoice.xml; the
  response (2026-05-30) follows the request 23-InvoiceStatusRequest.xml (2026-05-29 10:00), and
  sender and receiver are the request's parties reversed.
