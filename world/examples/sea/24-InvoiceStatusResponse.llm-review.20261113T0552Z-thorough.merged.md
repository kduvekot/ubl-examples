# LLM review: 24-InvoiceStatusResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/24-InvoiceStatusResponse.xml`, Git blob `e531150d68b1f203250613d0bd1bd36bd1ae7591` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/24#F1 · High · A response of 2026-05-30 reports a payment made on 2026-06-25 and a remittance advice issued that day
- XPath: `/InvoiceStatusResponse/cbc:IssueDate` = `2026-05-30`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- XPath: `/InvoiceStatusResponse/cbc:Note[2]` = `Approved; the balance will be paid to the factor.`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:IssueDate` = `2026-06-25`
- Why: `Payment` is "A Payment associated with one or more Invoices referenced in this Invoice Status Response", and `PaidDate` is "The date on which this payment was made". On 2026-05-30 no payment of 2026-06-25 can have been made, and the remittance advice the payment refers to is issued 26 days after this response, so the reference points to a document that does not exist when this one is issued. The response's own note says the balance "will be paid", so note and payment contradict each other. Between the two dates the credit note `26-CreditNote.xml` (2026-06-15) changes what is paid (see F2).
- Condition: The response reports only what is known on its issue date: no paid date and no remittance reference after 2026-05-30; a planned payment, if stated, is recognisable as planned.
- Options: (a) preferred: drop the `Payment` and keep the response as an approval (response code AP and the note already say that payment will follow); (b) issue a second response (version 2) after 2026-06-25 that reports the payment as `27-RemittanceAdvice.xml` does; (c) move this response after 2026-06-25, which changes its role (it would no longer answer `23-InvoiceStatusRequest.xml` of 05-29).
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1), money (F1)

### sea/24#F2 · High · Paid amount and payment identifiers differ from the remittance advice they refer to
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:ID` = `VT-PAY-26-0199`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0123`
- Why: The remittance advice named as this payment's remittance pays 43714.00, i.e. the invoice balance 43778.00 less the credit note `LD-CN-26-0152` of 64.00 (recomputed: 43778.00 − 64.00 = 43714.00), under payment order and instruction `VT-PAY-26-0123`. This response gives the same payment of the same invoice to the same payee as 43778.00 under `VT-PAY-26-0199`. The two documents refer to each other and describe different payments.
- Condition: If the response reports the payment at all, its amount, date and identifiers are those of `27-RemittanceAdvice.xml`.
- Options: (a) preferred: resolved together with F1 by dropping the `Payment`; (b) if a payment is kept (F1 option b), amount 43714.00 and instruction `VT-PAY-26-0123`.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F2), money (F2)

### sea/24#F3 · Medium · Exchange rate on a payment made in the invoice currency
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/InvoiceStatusResponse/cac:Payment/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- Why: The payment's `ExchangeRate` is "The exchange rate applicable to this payment, if the payment currency differs from the document currency". The paid amount is in Lume (XBL), the invoice's document and payment currency (`22-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XBL`), and the remittance advice pays in XBL too; the condition of the definition is not met, and no XLC amount is stated. The rate repeats the invoice's alternative-currency rate. The money part rated this Low and noted that the payer's account is held in XLC (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`), which could explain a rate; but that conversion is the bank's, between the payer's account and the XBL payment, not a difference between payment and document currency.
- Condition: The payment carries an exchange rate only if it is made in a currency other than the document currency, together with the amount it converts.
- Options: (a) preferred: drop the rate (moot if F1 removes the payment); (b) state the payment in XLC with the paid amount in XLC, if the story wants Velumi to pay in its home currency.
- Needs decision: no
- From: broad (F3), context (F2), money (F3)

### sea/24#F4 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in the postal address of the receiver of an invoice status response. 79 occurrences in 76 files (`grep -rho --include='*.xml'` over `world/examples`), always Lumeway's address.
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it; (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F4), parties (F1)

### sea/24#F5 · Medium · A language code in LocaleCode
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F2)

### sea/24#F6 · Low · Sales contacts for the approval of an invoice
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi approves the invoice and announces the payment; its contact is named Purchasing but is a customer service officer in Sales, so name, title and department disagree, and none of them is accounts payable. The receiver's contact is Lumeway's sales customer service rather than accounts receivable. Both are the parties' master-data contacts.
- Condition: Each contact's name, job title and department agree; the sender's contact is the function that approved the invoice, the receiver's the one following up the receivable.
- Options: (a) preferred: accounts payable at Velumi and accounts receivable at Lumeway; (b) drop the contacts.
- Needs decision: no
- From: broad (F5), parties (F3)

### sea/24#F7 · Low · Tax registration, share capital, legal-entity data and customs numbers in a status response
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41859`
- XPath: `/InvoiceStatusResponse/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/InvoiceStatusResponse/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: An invoice status response tells the invoice's issuer how far the invoice has been processed. The receiver's sales-tax registration and share capital, both parties' legal-entity descriptions and both customs trader numbers play no part in it; they are master data copied into a document that does not use them (section 4.8).
- Condition: Sender and receiver carry only the party data the response uses (identification, name, contact, electronic address).
- Options: (a) preferred: drop `PartyTaxScheme`, `PartyLegalEntity` (or at least `CorporateStockAmount`/`FullyPaidSharesIndicator`) and the customs trader identifiers; (b) keep them with a stated reason.
- Needs decision: no
- From: context (F3), money (F4), parties (F4)

## Checked and consistent
- `/InvoiceStatusResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147` resolves to `22-Invoice.xml`; the response (2026-05-30 13:49) answers `23-InvoiceStatusRequest.xml` (2026-05-29 10:00, "Has the invoice been approved?") the next day; sender and receiver are the request's parties reversed.
- Response code `AP` (UNTDID 4343, accepted) agrees with "Approved" in the note; the Lisavan and English notes carry `qal` and `en-XL`.
- The note that the balance goes to the factor agrees with the factored invoice (type 393, payee Harbourline Factoring) and with the payee of `27-RemittanceAdvice.xml`.
- 43778.00 is the invoice's payable amount after the 10000.00 deposit (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`); 0.4 is the flow's XBL→XLC rate.
- Velumi's address and legal form carry `en-XL` and Lisavan renderings, as in its other documents (parties).

## Considered and refuted
- `/InvoiceStatusResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147`: the response does not reference the status request `LD-DOC-26-0148` — refuted because the document response refers to the invoice whose status is given; linking the request is optional and the profile execution ID ties them (from broad).
- `/InvoiceStatusResponse/cbc:VersionID` = `1`: version 1 of a response suspected as a filler — refuted because the version distinguishes updates of the response, and a later response reporting the payment (F1 option b) would be version 2 (from context).
- `/InvoiceStatusResponse/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: the response going to the supplier rather than the factor — refuted because it answers the supplier's request; the factor is informed through the remittance advice (from parties).

## Changed in the merge
- money/F1 → F1: Needs decision yes → no, because dropping the payment changes only the encoding (the note and the response code already say the invoice is approved and will be paid); aligned with broad, context and logistics.
- context/F1 → F1 and F2: context's single finding split into the date problem (F1) and the amount/identifier contradiction (F2), as the other three parts did; the two have different conditions.
- money/F3 → F3: Low → Medium, because the element's own condition ("if the payment currency differs from the document currency") is not met, which is a meaning other than the definition (broad and context: Medium); money's argument about the XLC payer account is kept in Why.
- context/F3, money/F4, parties/F4 → F7: grouped (one problem, one fix).
