# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/09#F1 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` (ISO 639) repeats the language, not a locale. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (e.g. en-XB).
- Options: (a) preferred: `en-XB`; (b) leave it out.
- Needs decision: no

### energy/09#F2 · Low · Customs numbers and plant location on a remittance advice
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-105918`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- Why: The remittance advice reports a payment. Customs trader numbers and the coordinates of the payee's gas plant have no role in it; they look copied from master data. Customs trader identifiers occur in 11 of 12 RemittanceAdvice examples (`grep -l customs-trader` over `world/examples/*/*-RemittanceAdvice.xml`).
- Condition: The parties carry only data the remittance advice uses.
- Options: (a) preferred: leave them out; (b) keep them only with a stated reason.
- Needs decision: no

## Checked and consistent
- References: InvoiceDocumentReference KG-INV-26-0157 resolves to 06-Invoice.xml; ReminderDocumentReference KG-DOC-26-0159 resolves to 08-Reminder.xml; both of the kinds the elements name.
- Amounts: line 1 132480000 XUF = `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`; line 2 1987200 XUF = 19872 XBL (`08-Reminder.xml:/Reminder/cac:ReminderLine[2]/cbc:DebitLineAmount` = `19872.00`) × 100; total 134467200 = TotalDebitAmount = TotalPaymentAmount; LineCountNumeric 2.
- ExchangeRate on line 2 only, where the referenced document (the reminder) is in another currency, as its definition requires; no rate on line 1 (same currency).
- Accounts: payer account is Montebrio's ferra account (the payee account of its own invoice 03), payee account is Kelpstone's account of invoices 06 and 08.
- Note in both languages says the same thing; "March" in the Urvanian text is the month name, a loan word the lexicon may lack, not a different statement.

## Considered and refuted
- `/RemittanceAdvice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157`: suspected that one payment covering invoice and surcharge should not carry the invoice's creditor reference alone — refuted because the reference identifies the creditor's claim the surcharge belongs to, and the lines say what is paid.
