# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/25-Statement.xml`, Git blob `a032666792c16cd3abc0420251a04e56790287b6` (committed)
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

### sea/25#F1 · Medium · The invoice's freight and insurance repeated as charges of the statement, outside its totals
- XPath: `/Statement/cac:AllowanceCharge/cbc:Amount` = `3090.00`
- XPath: `/Statement/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Freight and insurance of the CIF invoice`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`
- XPath: `/Statement/cac:StatementLine[1]/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`
- XPath: `/Statement/cbc:TotalDebitAmount` = `53778.00`
- Why: A statement is "a statement of account, not a summary invoice". Its document-level `AllowanceCharge` is "A discount or charge that applies to a price component", on a line "A charge or discount price component associated with this statement line". The freight (2950.00) and insurance (140.00) are already part of the invoice amount debited on line 1 (53778.00 = 50688.00 goods + 3090.00 charges, `22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`). Stated again on the line and once more on the document (2950.00 + 140.00 = 3090.00), they read as charges levied by the statement itself, yet the totals do not include them (total debit 53778.00 = line 1's debit; 53778.00 − 10000.00 = 43778.00 balance). The reader cannot tell whether 3090.00 is owed in addition.
- Condition: The statement reports the invoice amount once; every charge it carries is a separate item of the account and reflected in its totals, or is clearly informative.
- Options: (a) preferred: drop the document-level charge and the line-level charges; the invoice reference carries the breakdown; (b) keep only the line-level breakdown, unchanged totals; (c) if the factor adds charges of its own (e.g. a factoring fee), state those and include them in the totals.
- Needs decision: no
- From: broad (F1), context (F1), money (F1)

### sea/25#F2 · Medium · Exchange rate on a statement line whose invoice is in the statement currency
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/Statement/cbc:DocumentCurrencyCode` = `XBL`
- Why: The line's `ExchangeRate` is "The rate of exchange between the currency of the Statement and the currency of the document described in the BillingReference". The statement is in Lume (XBL) and the referenced invoice is in Lume too (`22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`), so there is no rate between them; the XBL→XLC rate is the invoice's payment-alternative rate, which is not what this element means.
- Condition: A statement line carries an exchange rate only when its billing document is in another currency than the statement, and then between those two currencies.
- Options: (a) preferred: drop the rate; (b) if the payer's XLC equivalent is wanted, give it as information elsewhere (a note), not in this element.
- Needs decision: no
- From: broad (F2), context (F2), money (F2)

### sea/25#F3 · Medium · The deposit's payment dates given as an invoice period
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:StartDate` = `2026-05-08`
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:EndDate` = `2026-05-09`
- XPath: `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`
- Why: `InvoicePeriod` on a statement line is "An invoice period to which this statement line applies". Line 2 is the deposit payment `VT-DEP-26-0412`, paid on 2026-05-08 and received on 2026-05-09 (`22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-05-08`); the two dates are the payment's transit, not a period invoiced, and the invoice itself (a one-off sale) has no invoice period. The element carries a meaning other than its definition.
- Condition: The deposit line carries no invoice period, or one that is an actual invoicing period.
- Options: (a) preferred: drop it; the collected payment already carries the received date (and could carry the paid date).
- Needs decision: no
- From: broad (F4), context (F3), money (F4)

### sea/25#F4 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in the supplier's postal address in a statement of account. 79 occurrences in 76 files (`grep -rho --include='*.xml'` over `world/examples`), always Lumeway's address.
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it; (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F3), parties (F1)

### sea/25#F5 · Medium · A language code in LocaleCode
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Statement/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F2)

### sea/25#F6 · Low · A deposit received before the statement period, listed as an ordinary movement
- XPath: `/Statement/cac:StatementPeriod/cbc:StartDate` = `2026-05-14`
- XPath: `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`
- XPath: `/Statement/cac:StatementLine[1]/cbc:BalanceBroughtForwardIndicator` = `false`
- Why: The statement covers 2026-05-14 to 2026-06-13; line 2 credits the deposit received on 2026-05-09, five days before the period starts, without a brought-forward indicator, while line 1 is explicitly marked as not brought forward. Either the deposit belongs to an earlier period or the period should start earlier. The broad part refuted this: the deposit was applied on the invoice inside the period and explains the balance, and the line note says so ("Paid to the distributor before the invoice was assigned"). The merge keeps it as Low: the note explains why the deposit is there, but not why its date lies outside the stated period.
- Condition: Every movement listed falls inside the statement period, or the line carrying an earlier movement is marked as brought forward.
- Options: (a) preferred: start the statement period with the account's first movement (the deposit, 2026-05-08/09) or the order; (b) mark line 2 as balance brought forward; (c) present the deposit as part of the invoice's balance, as the invoice does with its `PrepaidAmount`.
- Needs decision: no
- From: context (F4), logistics (F1); broad considered and refuted it

### sea/25#F7 · Low · A tax total of 0.00 in a statement of account
- XPath: `/Statement/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- Why: A statement of account reports debits, credits and the balance of billing documents; the tax was settled in the invoice (export, category G, `22-Invoice.xml`). A tax total of 0.00 without subtotal says nothing a statement needs and can be read as "no tax applied on the statement", which it does not levy anyway.
- Condition: The statement carries a tax total only if it reports tax of the listed documents with its basis.
- Options: (a) preferred: drop the tax total; (b) give the subtotal with category G and the invoice's taxable amount, if the factor reports tax.
- Needs decision: no
- From: money (F3), broad (F1, part), context (F5, part)

### sea/25#F8 · Low · The order's originator and beneficiary in the factor's statement
- XPath: `/Statement/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Statement/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Statement/cac:StatementLine[1]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/Statement/cac:StatementLine[2]/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The factor's statement tells Velumi what it owes on the assigned account. The Port of Selanu, which originated the order and benefits from the goods, has no role in the account between Velumi and the factor, yet it is repeated at document level and on both lines (including the deposit line). These are values copied from the sale into a document that does not use them (section 4.8).
- Condition: The statement carries only the parties of the account (creditor/supplier, customer, payee).
- Options: (a) preferred: drop the originator and beneficiary at all levels.
- Needs decision: no
- From: context (F5, part)

### sea/25#F9 · Low · Contacts that do not fit a statement issued by the factor
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Statement/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/Statement/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: The statement is issued and signed by the factor "on behalf of Lumeway Distribution, whose receivables Harbourline Factoring holds", and tells Velumi what it owes. Velumi's contact is named Purchasing but is a customer service officer in Sales (name, title and department disagree; none is accounts payable, which reconciles a statement). The factor's contact is its client relationship manager, but the factor's client is Lumeway, while the statement addresses the debtor (debtor collections would fit). The supplier's contact is its sales customer service, although questions about the balance now go to the factor.
- Condition: Each contact's name, job title and department agree, and the customer's and payee's contacts are the functions that deal with the account balance.
- Options: (a) preferred: accounts payable at Velumi, debtor collections at Harbourline, Lumeway's contact dropped or its accounts receivable; (b) drop the contacts that do not serve the statement.
- Needs decision: no
- From: broad (F5), parties (F3)

### sea/25#F10 · Low · Tax registrations, share capital and customs numbers in a statement of account
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Statement/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: A statement of account lists the documents and payments on the account and the balance; the parties' sales-tax registrations, the supplier's share capital and the customs trader numbers play no part in it (the tax was settled on the invoice). They are copied from master data (section 4.8).
- Condition: The parties carry only the data a statement uses (identification, name, address, contact, the payee's account).
- Options: (a) preferred: drop the `PartyTaxScheme` aggregates, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifiers; (b) keep them with a stated reason.
- Needs decision: no
- From: parties (F5)

### sea/25#F11 · Low · Velumi's Lisavu address tagged en-XB and its legal form in English only
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings carry `languageID="en-XB"` and its legal form is in English only, without `languageID`. In the documents Velumi issues itself it is described with `en-XL` and the legal form in Lisavan and English (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). Over `world/examples/*/*.xml` English renderings of Lisavu street and town names carry `en-XL` 188 times, `en-XB` 141 times, `en-XU` 9 times (parties, lxml). No rule says whether the tag follows the issuer or the place; both are defensible.
- Condition: One documented rule decides the tag of English renderings of Lisavu names, and Velumi's address and legal form follow it in every example.
- Options: (a) preferred: `en-XL` and the legal form in Lisavan and English everywhere; (b) keep the issuer's variety and state the convention once in the address rules.
- Needs decision: yes
- From: parties (F4)

### sea/25#F12 · Low · Factoring agreement and assignment referenced by number only
- XPath: `/Statement/cac:AdditionalDocumentReference/cbc:ID` = `HF-FA-2026-007`
- XPath: `/Statement/cac:StatementLine[1]/cac:DocumentReference/cbc:ID` = `HF-ASSIGN-26-0091`
- Why: Neither reference says what the document is. In `22-Invoice.xml` the same numbers are the factoring contract (`TradeFinancing/ContractDocumentReference`) and a further trade-financing document (by its number the notice of assignment); here, as a bare additional reference and line document reference, the debtor reading the statement cannot tell, although the note "whose receivables Harbourline Factoring holds" rests on them. Neither document exists as an example in the flow.
- Condition: Both references state their document type.
- Options: (a) preferred: add `DocumentTypeCode` or `DocumentType` ("Factoring agreement", "Notice of assignment").
- Needs decision: no
- From: broad (F6), logistics (F2)

## Checked and consistent
- Totals (recomputed): debit 53778.00 (invoice `LD-INV-26-0147`) − credit 10000.00 (deposit `VT-DEP-26-0412`) = balance 43778.00; line balances 53778.00 and 43778.00; agree with `22-Invoice.xml` (tax-exclusive 53778.00 = 96 × 520 + 12 × 64 + 2950.00 + 140.00; prepaid 10000.00; payable 43778.00; deposit received 2026-05-09).
- Due date 2026-06-28 at document, payment means and line level agrees with the invoice; payee account `XB51BLUM38020502304038` (Harbourline Factoring) and RF reference `RF20LDINV260147` are the invoice's and pass `check_ids.py`.
- Statement period 2026-05-14 to 2026-06-13 starts with the invoice date and ends on the issue date (2026-06-13 08:43).
- Payee and signatory Harbourline Factoring (`20411233`) are the invoice's payee and financing party; accounting supplier/seller Lumeway, customer/buyer Velumi as in the invoice; line 2 carries no payee, which fits a deposit paid before the assignment.
- The credit note (2026-06-15) and the remittance (2026-06-25) are after the statement and correctly absent; the buyer's debit note `28-DebitNote.xml` is a claim of Velumi on Lumeway, not part of the factored receivable, and correctly absent.

## Considered and refuted
- `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`: a payment received before the statement period — refuted by broad (applied on the invoice inside the period; the line note explains it). The merge does not follow this refutation fully: context and logistics made it a finding, kept as F6 (Low) with broad's argument.
- `/Statement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`: the factor signing a statement in which Lumeway is the accounting supplier — refuted because the note states that Harbourline issues it on behalf of Lumeway as holder of the receivable, and the factor is the payee (from broad, context).
- `/Statement/cac:StatementLine[1]/cbc:PaymentPurposeCode` = `GDDS`: wrong for a line that also contains freight and insurance, or in conflict with the remittance advice's `SUPP` (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:PaymentPurposeCode` = `SUPP`) — refuted because freight and insurance are part of a CIF sale of goods, and both codes are valid ISO 20022 purposes for the same payment, each party choosing its own view (from context, money).
- `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`: the distributor as accounting supplier of a statement the factor issues — refuted because the statement reports Lumeway's sale to Velumi; the factor appears as payee and signatory, which is how a Statement, having no sender role, can show its issuer (from parties).

## Changed in the merge
- broad/F4, money/F4 (Low) and context/F3 (Medium) → F3: Medium, because the element carries a meaning other than its definition (payment dates as an invoice period), which section 6 rates Medium.
- broad/F1 → F1 and F7: the statement-level tax total, which broad grouped with the charges, is its own finding F7 (with money/F3), since it has its own condition and fix.
- context/F5 → F7 and F8: split into the tax total (F7) and the copied originator/beneficiary (F8).
- logistics/F1, context/F4 → F6: grouped; broad's refutation carried into Why.

## Outside this review
- `28-DebitNote.xml` (issued 2026-05-22) refers to this statement, which is issued only on 2026-06-13; that is a finding of the debit note's review (from broad).
- The freight and insurance charged on top of the CIF price originate in the invoice (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`) and belong to its review; the statement follows the invoice (from money). The invoice's due date itself is questioned in the invoice's review (from broad, money).
