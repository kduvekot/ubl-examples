# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/27-RemittanceAdvice.xml`, Git blob `a83f4a9e20f100a4540611eef91ece79f8f5dfa3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit e7f2d60 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/27#F1 · High · Factor named as accounting supplier of the invoice line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The line's AccountingSupplierParty is "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line". The line pays invoice `LD-INV-26-0147`, whose accounting supplier is Lumeway Distribution, as the remittance advice's own header says. Harbourline Factoring is the payee (it is already the line's `PayeeParty`), not the supplier; the line contradicts both the header and the invoice.
- Condition: The line's accounting supplier is Lumeway Distribution (or absent), and the factor appears only as payee.
- Options: set it to Lumeway (preferred: the line then repeats the invoice's parties consistently); or drop it, since the header gives the supplier.
- Needs decision: no

### sea/27#F2 · High · Payment amount and instruction differ from the status response that announces this remittance
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
- XPath: `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- Why: `24-InvoiceStatusResponse.xml` references this remittance advice (`VT-RM-26-0150`) for a payment of 43 778.00 under instruction `VT-PAY-26-0199` on 2026-06-25. This remittance advice, of the same date, pays 43 714.00 (after the credit note's 64.00) under instruction `VT-PAY-26-0123`. The two examples describe the same payment differently. (The status response is the likelier one to change: it predates the payment, see its review.)
- Condition: Every example that describes this payment gives the same amount, date and instruction ID as this remittance advice.
- Options: align or remove the payment in `24-InvoiceStatusResponse.xml` (preferred); keep this remittance advice as is.
- Needs decision: no

### sea/27#F3 · Medium · Exchange rate on a line whose invoice is in the remittance currency
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: RemittanceAdviceLine/ExchangeRate is "The rate of exchange between the currency of the Remittance Advice and the currency of the document described in the BillingReference." The remittance advice and invoice `LD-INV-26-0147` are both in XBL, so the condition of the definition is not met. The rate seems meant for the payer's conversion from its XLC account (43 714 × 0.4 = 17 485.60 XLC debited), which the line element does not express.
- Condition: No exchange rate on a line whose referenced document is in the remittance advice's currency; a conversion of the payer's account, if wanted, is stated where it applies.
- Options: drop the line's exchange rate (preferred); state the XLC debit in a note or the payer's payment instruction if the story needs it.
- Needs decision: no

### sea/27#F4 · Medium · Gate number in AdditionalStreetName of the supplier's postal address
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/27#F5 · Low · Contacts do not fit a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- Why: Questions about a remittance go to the payer's accounts payable and the payee's cash application; here the payer's contact is "Purchasing" (a customer service officer in Sales) and the supplier's is customer service. Name and department of the payer's contact contradict each other.
- Condition: The contacts handle payments, and each contact's name and department agree.
- Options: Velumi accounts payable; Lumeway receivables (the factor's contact is already on the payee).
- Needs decision: no

## Checked and consistent
- Totals: debit 43 778.00 (invoice balance after the 10 000.00 deposit, `22-Invoice.xml`) − credit 64.00 (`26-CreditNote.xml`, issued 06-15) = 43 714.00 paid; line 1 balance 0.00.
- Payee Harbourline Factoring and payee account `XB51BLUM38020502304038` agree with the factored invoice; RF `RF20LDINV260147` is the invoice's payment reference; payment on 2026-06-25 is before the due date 2026-06-28.
- Payer account `XL40BSEL0010003665515` (Bank of Selanu) and the other identifiers pass `check_ids.py`.
- Invoice and credit-note issue dates (05-14, 06-15) agree with the referenced documents.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147`: the invoice is referenced twice on the line (billing reference and document reference) — refuted: the document reference adds the document type; redundant but not contradictory.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`: paying an XBL amount from an XLC account — refuted: the invoice offers XLC as payment-alternative currency; the bank converts.
