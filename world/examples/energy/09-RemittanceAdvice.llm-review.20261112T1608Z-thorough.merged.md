# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/09#F1 · Medium · Province held in Region
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division and belongs in `CountrySubentity`, as in the payee's bank address in this document (`/RemittanceAdvice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). It is a world convention: 219 occurrences in 104 of the 250 XML examples (counted by the parts over `*.xml`).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense, and record why.
- Needs decision: no
- From: broad (F2), parties (F2)

### energy/09#F2 · Medium · Language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language code that repeats `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 of the 250 XML examples (counted by the parts over `*.xml`).
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB`, with a locale list ID; (b) leave it out.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### energy/09#F3 · Low · Customs numbers and the plant location on a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: the remittance advice reports a payment. The customs trader numbers and the location of the payee's gas plant have no role in it; they look copied from master data. The `InformationURI` is also the company's home page rather than a document about the location. Context counted customs trader identifiers in 11 of 12 RemittanceAdvice examples (`grep -l customs-trader` over `world/examples/*/*-RemittanceAdvice.xml`).
- Condition: the parties carry only data the remittance advice uses, and any `InformationURI` is about the location itself.
- Options: (a) preferred: leave them out; (b) keep them only with a stated reason.
- Needs decision: no
- From: parties (F4), context (F2)

### energy/09#F4 · Low · The contacts of a remittance advice are the trading and sales desks
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Energy trading`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Energy trader`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Gas sales`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- Why: the remittance advice tells the payee which invoice and surcharge a payment settles. It is sent by the payer's accounts payable or treasury to the payee's accounts receivable. Montebrio's energy trader and Kelpstone's gas sales manager are the commercial contacts of the deal, copied from `06-Invoice.xml`.
- Condition: the payer's contact handles payments and the payee's contact handles receivables.
- Options: (a) preferred: accounts contacts on both sides (as for the reminder 08); (b) leave the contacts out.
- Needs decision: no
- From: broad (F3), parties (F3)

## Checked and consistent
- Totals: 132480000 + 1987200 = 134467200 = `/RemittanceAdvice/cbc:TotalDebitAmount` = `134467200` = `/RemittanceAdvice/cbc:TotalPaymentAmount` = `134467200`; credits 0; `LineCountNumeric` 2 = the number of lines (all parts; recalculated in the merge).
- Line 1: `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `132480000` = `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`, both in XUF, so no rate (money, context, broad).
- Line 2: `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:DebitLineAmount` = `1987200` = 19872.00 XBL × 100 (`/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:ExchangeRate/cbc:CalculationRate` = `100`), the surcharge of `08-Reminder.xml:/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`. The rate runs XBL → XUF, from the reminder's currency to this document's, as the element's definition asks. Together the two lines equal the reminder's payable 1344672.00 XBL × 100 (money, context, broad).
- References: KG-INV-26-0157 is `06-Invoice.xml` and KG-DOC-26-0159 is `08-Reminder.xml`, each of the kind its element names. `PaymentID` RF41KGINV260157 = `06-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157` (logistics, context, broad).
- Dates: issued 2026-06-06 16:36, after the reminder (2026-06-03) and before its new due date 2026-06-10, so one month's surcharge is the right amount (logistics, money).
- Accounts: the payer account XU720351041700000005021992 is held by Montebrio Power SUA and is the account Montebrio gives as payee in 03. The payee account is Kelpstone's account of 06 and 08. `check_ids.py` passes RF41KGINV260157 and both accounts (parties, money, logistics).
- Parties: the payer and payee are the parties of 06 and 08, with the same identifiers, legal entities and tax schemes. Montebrio's address here is tagged `en-XU`, as in 03 and 05 (parties, broad).
- Notes: the two-language note agrees with the two references. "March" in the Urvanian text is the month name (a loan word the lexicon may lack), not a different statement (context, logistics).

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:ExchangeRate/cbc:Date` = `2026-06-06`: suspected because the rate is dated 2026-06-06, while the reminder converted on 2026-06-03. Refuted because both use 100 XUF per XBL, so the amounts agree; the date is when the payer established the rate (from broad).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:DebitLineAmount` = `1987200`: suspected that the line should carry the reminder's full total (1344672 XBL). Refuted because line 1 pays the invoice and the reminder line only adds the surcharge, so no amount is counted twice (from broad).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BillingReference/cac:ReminderDocumentReference/cbc:ID` = `KG-DOC-26-0159`: suspected because the line pays 1987200 XUF against a reminder whose payable amount is the whole debt. Refuted because the two lines together settle the reminder exactly; a `BillingReferenceLine` pointing at reminder line 2 would make it explicit, but nothing is ambiguous (from money).
- `/RemittanceAdvice/cbc:DocumentCurrencyCode` = `XUF` against the reminder in lume: refuted for this example, because paying in ferra is what the invoice and the reminder's note ask; the currency mismatch lies in the reminder (08/F1) (from money).
- `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157`: suspected that one payment covering the invoice and the surcharge should not carry the invoice's creditor reference alone. Refuted because the reference identifies the creditor's claim the surcharge belongs to, and the reminder asks to pay the surcharge with the invoice (from context, money).
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `KG-INV-26-0157`: suspected that the reference needs the invoice's issue date to be unambiguous. Refuted because the identifier is unique in the flow and the payment reference repeats it (from logistics).

## Changed in the merge
- broad/F2, parties/F2 → F1: Needs decision is no (broad said yes), because this is an encoding change; the same choice is made across the flow. The two places stay one finding.
- broad/F1, parties/F1, context/F1 → F2: combined, no change. It is numbered after F1 because the customer's address comes before the supplier party in this document.
- parties/F4, context/F2 → F3: combined into one finding of copied master data.
- broad/F3, parties/F3 → F4: combined; the job titles come from parties.
