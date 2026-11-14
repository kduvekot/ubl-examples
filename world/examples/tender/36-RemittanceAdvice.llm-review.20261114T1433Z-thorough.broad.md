# LLM review: 36-RemittanceAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/36-RemittanceAdvice.xml`, Git blob `0d67d6237dbe199fe762a5dccb67b4360d07c700` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 5660045 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/36#F1 · Medium · An advice of an actual payment without the payment date
- XPath: `/RemittanceAdvice/cbc:IssueDate` = `2026-05-08`
- XPath: `/RemittanceAdvice/cbc:TotalPaymentAmount` = `20308.55`
- XPath: `/RemittanceAdvice/cbc:Note` = `Payment of the first release, with the interest.`
- Why: a remittance advice is "A document that specifies details of an actual payment". The document has an issue date but no payment date (no PaymentDate on the lines, no PaymentDueDate or value date in PaymentMeans). The date matters here: the reminder (35) charges interest up to 2026-05-05 and asks for payment by 2026-05-12; whether further interest runs, and which day's rate converts the payment, depends on the day the money moved, which the payee cannot read from the advice.
- Condition: the advice states the date on which the payment was or will be executed.
- Options: (a) PaymentMeans/PaymentDueDate or line-level payment date = execution date (preferred).
- Needs decision: no

### tender/36#F2 · Medium · The payment is advised in lume only, though it is owed and received in ferra
- XPath: `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`
- Why: the invoice and the reminder name the payment currency ferra (`32-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `XUF`) and the payee's account is a ferra account. The advice gives every amount in lume, paid from a lume account, with no payment currency, no exchange rate and no amount in ferra (20308.55 XBL would be 2030855 XUF at the rate of 100 used throughout). The order, invoice and reminder all quote a forward purchase of ferra (BL-FX-26-0091) as the department's hedge for exactly this payment; the one document where it would fix the amount received does not mention it. The payee cannot reconcile the ferra credit on its account with this advice.
- Condition: the advice states the amount in the currency credited to the payee and the rate (and contract) used, consistent with the invoice's payment currency.
- Options: (a) add the payment currency, PaymentExchangeRate (with the forward contract if it is kept) and the ferra amount (preferred); (b) make lume the payment currency in 32 and 35 and pay to a lume account.
- Needs decision: no

### tender/36#F3 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/36#F4 · Low · The department pays interest that, by its own contract, was not due
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cbc:DebitLineAmount` = `22.23`
- XPath: `/RemittanceAdvice/cac:RemittanceAdviceLine[4]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-PAY-AUTH-26-0412`
- Why: the interest of the reminder rests on a due date of 2026-04-30 from the seller's standard terms. The department's contract says payment falls due 30 days after the accepted release (24), and the department itself claimed a penalty for late installation on 2026-04-06 (34), so by its own terms the invoice was not overdue on 1 May (see 35 F2). A public body nevertheless authorises and pays the interest, described as "Urvania's statutory interest", without remark.
- Condition: the payment of interest is consistent with the payment terms that the world decides apply to the contract.
- Options: (a) follow the decision on 32 F5 / 35 F2: if the contract's terms stand, the reminder and this line fall away and the payment is 20286.32 (preferred); (b) keep, if the invoice's terms become the contract's.
- Needs decision: yes (payment terms of the contract)

### tender/36#F5 · Low · The payer describes the payee with its logistics provider and order desk; department as a company; procurement office as payment contact
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: a payment advice needs payer, payee, accounts and the documents paid. The payee is given with its warehouse provider, stock listing and the sales order desk as contact; the payer's contact is the procurement office, although the invoice was routed to accounts payable (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`). The department carries a company liquidation status and a commercial-register type.
- Condition: parties carry what the advice uses; contacts are those who pay and who reconcile receipts; no liquidation status on the department.
- Options: (a) reduce the parties and use finance contacts (preferred).
- Needs decision: no

## Checked and consistent
- Arithmetic: debits 20808.00 + 22.23 = 20830.23; credits 515.20 + 6.48 = 521.68; 20830.23 − 521.68 = 20308.55 = TotalPaymentAmount = the reminder's payable amount (35). Four lines, LineCountNumeric 4.
- Each line's amount is the payable amount of the referenced document: invoice VI-INV-26-0221 (20808.00, net of withholding), credit note VI-CN-26-0222 (515.20), debit note LPWD-DOC-26-0223 (6.48, the department's claim, credited), reminder VI-DOC-26-0224 (22.23 interest), whose issue date 2026-05-05 is quoted correctly.
- Payment reference RF48VIINV260221 is the invoice's; payee account and bank as on the invoice; payer account at the Bank of Lumeport, whose address (Exchange Street 48, Lumeport) agrees with the guarantor of 14; branch number 380100 is contained in the account number.
- Issue 2026-05-08 is within the reminder's seven days (to 2026-05-12).
- check_ids.py: ISIN, RF reference and both IBAN-like accounts correct.

## Considered and refuted
- `/RemittanceAdvice/cac:AdditionalDocumentReference/cbc:ID`: the payment authorisation is given at header and again on line 4 only — refuted, the interest is the item that needed a separate authorisation, and the header reference covers the payment.
- `/RemittanceAdvice/cac:RemittanceAdviceLine[3]/cbc:CreditLineAmount`: a debit note as a credit — refuted, it is the payer's own claim (see 34 F3 on its roles).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount`: the withholding tax (69.48 net) is not shown — refuted, the lines carry payable amounts net of it, and the tax goes to the treasury, not to the payee.
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BLUMXBLX as a possible real BIC — refuted, country part XB is not an assigned ISO 3166 code.
- `/RemittanceAdvice/cbc:TotalPaymentAmount`: the 2 % settlement discount of the invoice — not applicable, payment is after the discount period.
