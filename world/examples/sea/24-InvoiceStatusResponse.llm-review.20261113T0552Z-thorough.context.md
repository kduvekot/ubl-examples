# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 0919fae 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/24#F1 · High · A payment made on 2026-06-25 reported in a response issued on 2026-05-30, and it does not match the remittance advice it cites
- XPath: `/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- XPath: `/InvoiceStatusResponse/cbc:Note[2]` = `Approved; the balance will be paid to the factor.`
- Why: `PaidDate` is "The date on which this payment was made". On 2026-05-30 the buyer cannot report a payment made on 2026-06-25, and its own note says the balance "will be paid". The response also cites the remittance advice `VT-RM-26-0150`, which is issued only on 2026-06-25 (`27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:IssueDate` = `2026-06-25`). That remittance advice describes a different payment: total `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00` (the invoice balance less the credit note `LD-CN-26-0152` of 64.00, issued 2026-06-15) under payment order `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0123`, whereas this response gives 43778.00 under instruction `VT-PAY-26-0199`.
- Condition: The response reports only what is known on its issue date: either a planned payment expressed as such (no paid date in the future, no reference to a remittance advice not yet issued), or the response is issued after the payment and then agrees with the remittance advice in amount and payment reference.
- Options: (a) preferred: keep the response on 2026-05-30 as an approval only (status "accepted", with the planned payment in the note or as the due date) and drop the `Payment`; (b) issue a second response after 2026-06-25 that reports the payment as in `27-RemittanceAdvice.xml`.
- Needs decision: no

### sea/24#F2 · Medium · Exchange rate on a payment made in the document currency
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The payment's `ExchangeRate` is "The exchange rate applicable to this payment, if the payment currency differs from the document currency". The paid amount is in Lume (XBL), the invoice's document and payment currency (`22-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XBL`); the condition of the definition is not met. The rate to Coral repeats the invoice's alternative currency rate without a payment in Coral.
- Condition: The payment carries an exchange rate only if it is made in a currency other than the document currency.
- Options: (a) preferred: remove the exchange rate; (b) state the payment in Coral, if the story wants Velumi to pay in its home currency, with the paid amount in XLC.
- Needs decision: no

### sea/24#F3 · Low · Tax registration and legal-entity data in a status response
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41859`
- Why: An invoice status response tells the invoice's issuer how far the invoice has been processed. Sender and receiver are identified by their identifiers and names; the receiver's tax registration and both parties' legal-entity descriptions have no part in it. They are master data copied into a document that does not use them.
- Condition: Sender and receiver carry identification, name and the contact or address the exchange needs, and no tax or legal-entity data without a reason in this document.
- Options: (a) preferred: reduce both parties to identifier, name, electronic address and contact.
- Needs decision: no

## Checked and consistent
- The response answers `23-InvoiceStatusRequest.xml` (2026-05-29, "Has the invoice been approved?") the next day; the response code AP "Accepted" agrees with "Approved" in the note.
- The referenced invoice `LD-INV-26-0147` exists (`22-Invoice.xml`); the amount 43778.00 is its payable amount after the deposit.

## Considered and refuted
- `/InvoiceStatusResponse/cbc:VersionID`: version 1 of a response suspected as a filler — refuted because the definition provides a version of the response to distinguish updates, and a later response reporting the payment (see F1, option b) would be its version 2.
