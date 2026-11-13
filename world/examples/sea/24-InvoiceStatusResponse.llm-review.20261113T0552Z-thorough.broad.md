# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/24#F1 · High · Status response of 05-30 reports a payment made on 06-25 and a remittance advice not yet issued
- XPath: `/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- XPath: `/InvoiceStatusResponse/cbc:Note[2]` = `Approved; the balance will be paid to the factor.`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:IssueDate` = `2026-06-25`
- Why: `Payment` is "A Payment associated with one or more Invoices referenced in this Invoice Status Response", with `PaidDate` "The date on which this payment was made". On 2026-05-30 no payment made on 2026-06-25 can be reported, and the remittance advice `VT-RM-26-0150` it references is only issued on 2026-06-25 (`27-RemittanceAdvice.xml`). The document's own note says the balance "will be paid", i.e. not yet paid.
- Condition: The response reports no payment that has not been made by its issue date and references no document issued after it.
- Options: (a) preferred: drop the `Payment` (the note already says payment will follow); (b) move the response to after 2026-06-25, which changes its role in the flow (it would no longer answer `23-InvoiceStatusRequest.xml` of 05-29).
- Needs decision: no

### sea/24#F2 · High · Payment amount and instruction contradict the remittance advice
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
- Why: The referenced remittance advice pays 43 714.00 (43 778.00 less the credit note `LD-CN-26-0152` of 64.00) under instruction `VT-PAY-26-0123`; this response gives the same payment as 43 778.00 under instruction `VT-PAY-26-0199`. Both cannot describe the same payment.
- Condition: If a payment is reported, its amount, date and instruction ID agree with `27-RemittanceAdvice.xml`.
- Options: removing the payment (F1, preferred) resolves this too; otherwise align amount and IDs with the remittance advice.
- Needs decision: no

### sea/24#F3 · Medium · Exchange rate on a payment in the invoice currency
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- Why: Payment/ExchangeRate is "The exchange rate applicable to this payment, if the payment currency differs from the document currency." The paid amount is in XBL, the invoice's document currency (`22-Invoice.xml`), and the remittance advice pays in XBL too; the condition of the definition is not met, and no XLC amount is stated.
- Condition: No exchange rate on a payment made in the document currency.
- Options: drop it (preferred).
- Needs decision: no

### sea/24#F4 · Medium · Gate number in AdditionalStreetName of the receiver's postal address
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/24#F5 · Low · Contacts do not fit an invoice approval answer
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- Why: The approval of an invoice is answered by the buyer's accounts payable and received by the seller's accounts receivable; here the contacts are "Purchasing" (a customer service officer in Sales) and Lumeway's customer service. Name and department of the sender's contact also contradict each other.
- Condition: The contacts handle invoice status, and each contact's name and department agree.
- Options: accounts payable at Velumi, accounts receivable at Lumeway.
- Needs decision: no

## Checked and consistent
- `LD-INV-26-0147` resolves to `22-Invoice.xml`; sender Velumi (its customer), receiver Lumeway (its supplier); response `AP` (UNTDID 4343 accepted) answers the question of `23-InvoiceStatusRequest.xml` ("Has the invoice been approved?") one day later.
- The note "the balance will be paid to the factor" agrees with the factored invoice (type 393, payee Harbourline Factoring); 43 778.00 is the invoice's payable balance after the deposit.
- Notes in Lisavan and English carry `qal` and `en-XL`; GLN passes `check_ids.py`.

## Considered and refuted
- `/InvoiceStatusResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147`: the response does not reference the status request `LD-DOC-26-0148` — refuted: the model's document response refers to the invoice whose status is given; linking the request is optional and the profile execution ID ties them.
