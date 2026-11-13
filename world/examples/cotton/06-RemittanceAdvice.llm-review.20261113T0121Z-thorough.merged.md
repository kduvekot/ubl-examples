# LLM review: 06-RemittanceAdvice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/06-RemittanceAdvice.xml`, Git blob `e26eebc8bac0997744bbae65cf8d2aa86a65b428` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/06#F1 · Low · The ginnery's customs-trader number and the farm's fields in a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- Why: section 4.8. A remittance advice announcing a domestic bank transfer uses neither a customs-trader number nor the location of the farm's fields (`Party/PhysicalLocation`, "The physical location of this party", with coordinates and the home page as `InformationURI`); both read as copied master data (IND5). Same in 01, 04 and 05.
- Condition: every identifier and location of the parties is one the document has a use for.
- Options: (a, preferred) leave both out.
- Needs decision: no
- From: parties (F4), context (F2)

### cotton/06#F2 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`); reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from the company's history; (b) drop it; (c) record a register-wide date.
- Needs decision: yes
- From: parties (F3)

### cotton/06#F3 · Low · Contacts do not fit the role or the party
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`
- Why: the ginnery pays the farm here; questions about the remittance go to its farm-payments / accounts-payable desk (04 routes these payments to "Farm payments"), not to lint sales. The farm is a one-person micro sole proprietorship with a "Customer service officer" in "Sales".
- Condition: the ginnery's contact handles payments (or is absent), and the farm's contact fits a one-person farm.
- Options: (a, preferred) a farm-payments contact for the ginnery; no job title/department (or "Owner") for the farm; (b) drop the contacts.
- Needs decision: no
- From: broad (F3), parties (F1, F2)

### cotton/06#F4 · Low · Address lines repeat the farm's structured address and mix languages
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the same four lines as in 01 and 03 repeat `StreetName`, `Description`, `District` and `CityName`, and lines 1 and 4 combine the Lisavan and English forms in one text without `languageID`, although `Line` "may be repeated only to provide the same content in multiple natural languages". No part raised it for 06; added by the merge so that the farm's address is treated the same way as in 01#F6 and 03#F5 (where parties' counter-argument, a Lisavan print format, is recorded).
- Condition: the farm's postal address states each part once, and language-specific renderings carry `languageID`.
- Options: (a, preferred) drop the address lines; (b) keep only lines with information not in the structured parts.
- Needs decision: no
- From: merge

### cotton/06#F5 · Low · The payment reference the invoice asked for is not quoted
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentID` = `RF77SCGSBI260194`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF77SCGSBI260194`
- XPath: `18-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF46SCGINV260210`
- Why: a Remittance Advice is "A document that specifies details of an actual payment". The self-billed invoice it settles asks for its creditor reference to be quoted; the advice carries neither a `PaymentID` nor an `InvoicingPartyReference`, so the transfer it announces cannot be matched on the farm's bank statement by that reference. The mill's remittance advice in the same flow quotes the reference it was asked for. The billing references still link the lines to 04 and 05, so the advice is usable without it; Low.
- Condition: the remittance advice identifies the transfer by the reference requested in 04, or says why another reference is used (e.g. the net amount after set-off has its own).
- Options: (a, preferred) `PaymentMeans/PaymentID` = RF77SCGSBI260194 (or `InvoicingPartyReference` on line 1); (b) leave it, if amount and date are considered enough for matching.
- Needs decision: no
- From: broad (F1), money (F1), context (F1)

### cotton/06#F6 · Low · No date of the payment
- XPath: `/RemittanceAdvice/cbc:IssueDate` = `2026-02-16`
- Why: a remittance advice "specifies details of an actual payment", but nothing says when the transfer is executed or value-dated; the issue date is only the date of the advice. The farm needs the date to reconcile the 3 141.070 and to see that the 45-day term (due 2026-03-24) was met. Refutation tried: other parts read the issue date as the payment date (it equals 05's due date, the set-off date), which is plausible but not stated.
- Condition: the payment's execution or value date is stated, or the document says that it equals the issue date.
- Options: (a, preferred) a payment date where the model offers one (e.g. `PaymentMeans/PaymentDueDate` as the requested execution date), or a note.
- Needs decision: no
- From: broad (F2)

### cotton/06#F7 · Low · Expiry date on the farm's commercial-register entry
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)"; the registration described is the farm's entry in the island companies register, which normally does not expire. Parties (in 01) read it as a seasonal farm registration (`XL-FARM-REG-0412` in 04); possible, but that is not the company registration described. No part raised it here; added by the merge (appended, without renumbering) for consistency with 01#F7 and 03#F6.
- Condition: the expiry date belongs to a registration that expires and is the one described.
- Options: (a, preferred) drop it; (b) make the world's register rules say that sole proprietorships register yearly.
- Needs decision: yes
- From: merge

## Checked and consistent
- Total (redone): `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `3210.320` (payable of 04) − `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `69.250` (payable of 05) = 3 141.070 = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `3141.070`.
- Line 1 refers to 04 (`SCG-SBI-26-0194`) and line 2 to 05 (`SCG-SBC-26-0195`); both exist; debit for the invoice, credit for the credit note, as in 18. 05's set-off note and payment means 97 agree with netting it here; 05's `DueDate` 2026-02-16 is this advice's issue date.
- Accounts: payer `XL31BSEL0020004922263`, named `Selanu Cotton Ginnery Ltd`, the ginnery's (the same account receives the mill's payment in 16 and 18); payee `XL67BSEL0020004817534`, the farm's account from 01 and 04; both pass `check_ids.py`, both coral accounts.
- The advance of 01 (1 017.000) is correctly not part of this payment: 04 deducts it as prepaid.
- Payment before 04's due date 2026-03-24, so no penalty interest arises.
- Accounting customer and supplier have the same full descriptions as in 04 and 05 (parties).

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount`: debit used for an amount the payer pays — refuted: from the payer's ledger the invoice is a debit to settle, the credit note a credit; consistent with 18. (from broad)
- `/RemittanceAdvice/cbc:TotalPaymentAmount`: early payment of a 45-day invoice — refuted: paying before the due date is allowed and explains the set-off date. (from broad)
- `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:Name` = `Selanu Cotton Ginnery Ltd`: payer account unneeded — refuted: it tells the payee which account the transfer comes from, part of the details of an actual payment. (from context)

## Changed in the merge
- broad/F1, money/F1, context/F1 → F5: combined.
- broad/F3 + parties/F1 + parties/F2 → F3: grouped (contacts).
- parties/F4 + context/F2 → F1: grouped (copied master data).
- F4: added by the merge (farm address lines), for consistency with 01 and 03.
- F7: added by the merge (farm registration expiry date), for consistency with 01 and 03.
