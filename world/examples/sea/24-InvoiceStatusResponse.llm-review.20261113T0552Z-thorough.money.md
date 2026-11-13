# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
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

### sea/24#F1 · High · A status response of 2026-05-30 reports a payment made on 2026-06-25 and a remittance advice issued that day
- XPath: `/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- Why: `Payment` is "a Payment associated with one or more Invoices referenced in this Invoice Status Response", and `PaidDate` is "the date on which this payment was made". On 2026-05-30 the payment had not been made: it is dated 2026-06-25, and the remittance advice it refers to was issued on 2026-06-25 (`27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:IssueDate` = `2026-06-25`). The response's own note says the balance "will be paid" (`/InvoiceStatusResponse/cbc:Note[2]` = `Approved; the balance will be paid to the factor.`), so the note and the payment aggregate contradict each other.
- Condition: The response reports only what is known on its issue date: no paid date or remittance reference after 2026-05-30; a planned payment, if stated, is recognisable as planned.
- Options: (a) preferred: leave the `Payment` out (the approval and the note say what is planned); (b) issue the response after 2026-06-25 if it is meant to confirm the payment, which changes the order of the flow.
- Needs decision: yes

### sea/24#F2 · High · Paid amount and payment instruction differ from the remittance advice
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:ID` = `VT-PAY-26-0199`
- Why: The referenced remittance advice pays 43714.00, the balance of 43778.00 less the credit note of 64.00 (`27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`), under payment instruction `VT-PAY-26-0123` (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`). The response reports 43778.00 under instruction `VT-PAY-26-0199`, so the two documents describe different payments while referring to each other.
- Condition: If the response reports the payment, amount and instruction ID are those of the remittance advice it references.
- Options: (a) preferred: resolve together with F1 by leaving the payment out; (b) if kept, align amount (43714.00) and instruction (`VT-PAY-26-0123`) with the remittance advice.
- Needs decision: no

### sea/24#F3 · Low · Exchange rate on a payment made in the document currency
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The payment's exchange rate is "applicable to this payment, if the payment currency differs from the document currency". The paid amount is in XBL, the invoice's currency, so the condition is not met as stated. The payer's account is in XLC (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`), which could justify the rate, but the response does not show an XLC amount.
- Condition: The exchange rate is present only together with an amount in the other currency it converts, or absent.
- Options: (a) preferred: drop the rate (moot if F1 removes the payment); (b) state the XLC debit amount the rate converts.
- Needs decision: no

### sea/24#F4 · Low · Receiver's sales-tax registration and share capital in a status response
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The response approves an invoice; Lumeway's sales-tax registration and share capital have no use in it (section 4.8).
- Condition: The receiver carries tax scheme and capital data only if the response uses them.
- Options: (a) preferred: leave them out; (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- The response answers the request of 2026-05-29 (`23-InvoiceStatusRequest.xml:/InvoiceStatusRequest/cbc:RequestDate` = `2026-05-29`) about invoice `LD-INV-26-0147` with AP (Accepted); the note that the balance goes to the factor agrees with the invoice's assignment.
- The balance 43778.00 is the invoice's payable amount (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`); the rate 0.4 is the flow's XBL→XLC rate.
