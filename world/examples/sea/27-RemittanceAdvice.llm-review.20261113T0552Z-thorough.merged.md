# LLM review: 27-RemittanceAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/27-RemittanceAdvice.xml`, Git blob `a83f4a9e20f100a4540611eef91ece79f8f5dfa3` (committed)
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

### sea/27#F1 · High · The factor named as accounting supplier of the invoice line, against the header and the invoice
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The line's `AccountingSupplierParty` is "The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line", i.e. the accounting supplier of the invoice the line pays. That invoice names Lumeway Distribution, as do this document's header and the line's own seller. The factor bought the receivable and is the payee, which the line already says in `PayeeParty`; it did not become the invoice's accounting supplier. The line contradicts the header and the referenced invoice.
- Condition: The line's accounting supplier is the invoice's accounting supplier (Lumeway Distribution, `20410274`) or is absent; the factor appears only as payee.
- Options: (a) preferred: Lumeway as the line's accounting supplier, Harbourline as payee; (b) drop the line-level accounting supplier, since the header gives it.
- Needs decision: no
- From: broad (F1), context (F1), money (F1), parties (F1)

### sea/27#F2 · High · This payment does not match the payment the invoice status response reports with this remittance advice
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `43714.00`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `VT-PAY-26-0123`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:InstructionID` = `VT-PAY-26-0123`
- XPath: `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cac:RemittanceDocumentReference/cbc:ID` = `VT-RM-26-0150`
- XPath: `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:PaidAmount` = `43778.00`
- XPath: `24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:InstructionID` = `VT-PAY-26-0199`
- Why: `24-InvoiceStatusResponse.xml` cites this remittance advice for a payment of 43778.00 on 2026-06-25 under instruction `VT-PAY-26-0199`. This remittance advice, of the same date, reports 43714.00 (recomputed: 43778.00 − 64.00 credit note = 43714.00) under payment order and instruction `VT-PAY-26-0123`. The two examples describe the same payment of the same invoice to the same payee differently in amount and identifier. The status response is the likelier one to change: it predates the payment (see its review, F1 and F2).
- Condition: The payment of `LD-INV-26-0147` has one amount, date and instruction identifier in every example of the flow that reports it.
- Options: (a) preferred: keep this remittance advice as it is (it accounts for the credit note) and drop or align the payment in `24-InvoiceStatusResponse.xml`; (b) if the status response's figures are the intended ones, change this document, which would drop the credit-note set-off.
- Needs decision: no
- From: broad (F2), context (F2)

### sea/27#F3 · Medium · Exchange rate on a line whose invoice is in the remittance currency
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: The line's `ExchangeRate` is "The rate of exchange between the currency of the Remittance Advice and the currency of the document described in the BillingReference". Both are Lume (XBL): the remittance advice's document currency and the invoice's (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`); the condition of the definition is not met. The rate probably reflects that Velumi pays from its Coral account (43714.00 × 0.4 = 17485.600 XLC debited), but that conversion is the bank's, between the payer's account and the payment, and not what this element means.
- Condition: A remittance line carries an exchange rate only when its billing document's currency differs from the remittance advice's currency.
- Options: (a) preferred: drop the rate; (b) if the debit of Velumi's Coral account matters, state it as information (a note with the XLC amount), not as the line's exchange rate.
- Needs decision: no
- From: broad (F3), context (F3), money (F2)

### sea/27#F4 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in the supplier's postal address in a remittance advice paid to the factor. 79 occurrences in 76 files (`grep -rho --include='*.xml'` over `world/examples`), always Lumeway's address.
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it; (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F4), parties (F2)

### sea/27#F5 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F3)

### sea/27#F6 · Low · The order's originator and beneficiary on every remittance line
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: A remittance advice specifies the details of an actual payment so the payee can apply it. The Port of Selanu, which originated the order and benefits from the goods, plays no part in Velumi's payment to the factor; repeating it on both lines (the credit-note line included) is data copied from the sale into a document that does not use it (section 4.8).
- Condition: The remittance lines carry the billing references, amounts and the parties needed to apply the payment.
- Options: (a) preferred: drop the originator and beneficiary from both lines.
- Needs decision: no
- From: context (F4)

### sea/27#F7 · Low · The contacts do not fit a payment to the factor
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: Velumi, the payer, gives as its contact Purchasing, a customer service officer in Sales: name, title and department disagree, and none is accounts payable, which made the payment. The supplier's contact is its sales customer service. The factor's contact is its client relationship manager, but in this payment Velumi is the factor's debtor, not its client; cash allocation or debtor collections would fit. All are master-data contacts used in every role.
- Condition: Each contact's name, job title and department agree, and the payer's and payee's contacts are the functions that deal with the payment.
- Options: (a) preferred: accounts payable at Velumi, cash allocation or debtor collections at Harbourline, Lumeway's receivables or no Lumeway contact; (b) drop the contacts.
- Needs decision: no
- From: broad (F5), parties (F4)

### sea/27#F8 · Low · Tax registrations, share capital and customs numbers in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/RemittanceAdvice/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: A remittance advice tells the payee which documents a payment settles; the parties' sales-tax registrations, the supplier's share capital and the customs trader numbers play no part in it. They are copied from master data (section 4.8).
- Condition: The parties carry only the data a remittance advice uses.
- Options: (a) preferred: drop the `PartyTaxScheme` aggregates, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers; (b) keep them with a stated reason.
- Needs decision: no
- From: parties (F5)

## Checked and consistent
- Totals (recomputed): debit 43778.00 (the invoice's payable amount after the deposit, `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`) − credit 64.00 (`26-CreditNote.xml:/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `64.00`) = payment 43714.00; line 1 balance 0.00; line count 2.
- Invoice and credit-note references with issue dates 2026-05-14 and 2026-06-15 agree with `22-Invoice.xml` and `26-CreditNote.xml`; both precede this advice (2026-06-25 15:43).
- Payee Harbourline Factoring and payee account `XB51BLUM38020502304038` (in the factor's name, XBL) are the invoice's; RF `RF20LDINV260147` is the invoice's payment reference; the payment of 2026-06-25 is before the due date 2026-06-28; the remittance goes to the payee the invoice's remittance distribution names.
- Payer account `XL40BSEL0010003665515` is Velumi's own, at the Bank of Selanu (the payee account of `28-DebitNote.xml`); accounts, RF and GLN pass `check_ids.py` (re-run).
- Velumi's address and legal form carry `en-XL` and Lisavan renderings, as in its other documents; Harbourline's and Lumeway's descriptions are identical to the invoice (parties).

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:DocumentReference/cbc:ID` = `LD-INV-26-0147`: the invoice referenced twice on line 1 — refuted because the document reference adds the document type code, which the billing reference does not carry; redundant, not contradictory (from broad, context).
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XLC`: paying an XBL amount from an XLC account — refuted because the invoice offers XLC as payment-alternative currency and the bank converts (from broad).
- `/RemittanceAdvice/cbc:Note[2]` = `Payment of the invoice below.`: incomplete, since a credit note is set off too — refuted because the payment is for the invoice and the credit-note line is the deduction from it (from context).
- Debit note `VT-DOC-26-0153` (`28-DebitNote.xml:/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `51.250`) not deducted — refuted because the invoice's receivable belongs to the factor, and a buyer's counterclaim against the seller cannot simply be set off against a payment to the factor (from money).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `64.00`: the credit line names no accounting supplier or payee — refuted because the header names both and the line inherits them; whether the factor accepts the deduction is a finding of the credit note (`26-CreditNote.xml`, F4) (from parties).

## Changed in the merge
- No severity changes; findings of the same problem grouped (F1 from four parts, F3 from three).
