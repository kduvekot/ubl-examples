# LLM review: 25-Statement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/25-Statement.xml`, Git blob `a032666792c16cd3abc0420251a04e56790287b6` (committed)
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

### sea/25#F1 · Medium · Statement-level charge and tax total repeat the invoice's charges without entering the totals
- XPath: `/Statement/cac:AllowanceCharge/cbc:Amount` = `3090.00`
- XPath: `/Statement/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Freight and insurance of the CIF invoice`
- XPath: `/Statement/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Statement/cbc:TotalDebitAmount` = `53778.00`
- Why: A statement "is a statement of account, not a summary invoice". The freight and insurance of 3 090.00 are already inside the invoice's 53 778.00 debited on line 1 (and repeated again as the line's two charges). A charge on the statement as a whole reads as an additional charge levied by the statement, yet the totals do not include it (53 778 − 10 000 = 43 778). The tax total of 0.00 without any subtotal likewise only repeats the invoice's tax treatment.
- Condition: The statement carries no document-level charges or tax totals that it does not itself levy; every amount on the statement is reflected in its totals.
- Options: drop the statement-level `AllowanceCharge` and `TaxTotal` (preferred), keeping at most the line-level breakdown of the invoice; or, if the world wants the breakdown, keep it only on the line.
- Needs decision: no

### sea/25#F2 · Medium · Exchange rate on a statement line whose document is in the statement currency
- XPath: `/Statement/cac:StatementLine[1]/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/Statement/cbc:DocumentCurrencyCode` = `XBL`
- XPath: `22-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`
- Why: StatementLine/ExchangeRate is "The rate of exchange between the currency of the Statement and the currency of the document described in the BillingReference." Statement and invoice are both in XBL; a rate to XLC answers no question the definition asks.
- Condition: No exchange rate on a statement line whose referenced document is in the statement currency.
- Options: drop it (preferred).
- Needs decision: no

### sea/25#F3 · Medium · Gate number in AdditionalStreetName of the supplier's postal address
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/25#F4 · Low · Invoice period on the deposit line
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:StartDate` = `2026-05-08`
- XPath: `/Statement/cac:StatementLine[2]/cac:InvoicePeriod/cbc:EndDate` = `2026-05-09`
- XPath: `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`
- Why: Line 2 is the deposit payment, not an invoice; its "invoice period" 05-08 to 05-09 is the span from paying (05-08) to receiving (05-09) the deposit (`22-Invoice.xml` prepaid payment), which is not an invoice period. The dates are already in the collected payment.
- Condition: The deposit line carries no invoice period, or one that is a real invoicing period.
- Options: drop it (preferred).
- Needs decision: no

### sea/25#F5 · Low · Contacts: the statement comes from the factor, the contacts are sales staff
- XPath: `/Statement/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Statement/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The statement is issued and signed by Harbourline Factoring "on behalf of Lumeway Distribution"; questions about the balance go to the factor (whose contact is on the payee) or to receivables, not to Lumeway's customer service. Velumi's contact is "Purchasing" in Sales, which contradicts itself and is not accounts payable.
- Condition: The accounting parties' contacts handle the account, and each contact's name and department agree.
- Options: Lumeway's receivables (or none, since the payee carries the factor's contact); Velumi's accounts payable.
- Needs decision: no

### sea/25#F6 · Low · Factoring agreement referenced without type
- XPath: `/Statement/cac:AdditionalDocumentReference/cbc:ID` = `HF-FA-2026-007`
- Why: The additional reference gives only an ID; the reader cannot tell it is the factoring agreement under which Harbourline holds the receivable (the invoice cites it as `TradeFinancing/ContractDocumentReference`).
- Condition: The reference states its document type.
- Options: add a document type (factoring agreement).
- Needs decision: no

## Checked and consistent
- Totals: debit 53 778.00 (invoice `LD-INV-26-0147`), credit 10 000.00 (deposit `VT-DEP-26-0412`), balance 43 778.00; line balances 53 778.00 and 43 778.00; agree with `22-Invoice.xml` (payable 43 778.00, prepaid 10 000.00, deposit received 05-09).
- Line charges 2 950.00 and 140.00 agree with the invoice; due date 2026-06-28 and payee account `XB51BLUM38020502304038` agree with the invoice (the due date's own problem is in that example's review).
- Statement period 2026-05-14 to 2026-06-13 starts with the invoice date and ends on the issue date.
- Payee Harbourline Factoring and assignment `HF-ASSIGN-26-0091` agree with the invoice; RF reference and account pass `check_ids.py`.

## Considered and refuted
- `/Statement/cac:StatementLine[2]/cac:CollectedPayment/cbc:ReceivedDate` = `2026-05-09`: a payment received before the statement period — refuted: it was applied on the invoice inside the period and explains the balance; the line note says so.
- `/Statement/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`: issuer is not one of the accounting parties — refuted: the note states the statement is made on behalf of Lumeway by the factor holding the receivable, and the factor is the payee.

## Outside this review
- `28-DebitNote.xml` (issued 2026-05-22) references this statement `HF-ST-26-0151`, which is issued only on 2026-06-13; that lies in the debit note.
