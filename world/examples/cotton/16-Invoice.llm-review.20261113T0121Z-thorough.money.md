# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/16#F1 · High · Due date is 30 days after issue, the terms say 45 days net
- XPath: `/Invoice/cbc:DueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:ID` = `XL-STD`
- Why: the invoice is issued on 2026-03-02; 45 days net gives 2026-04-16, while all three due
  dates are 2026-04-01, which is 30 days after issue. The same terms `XL-STD` with the note
  "45 days net." in the self-billed invoice 04 do give 45 days
  (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:DueDate` = `2026-03-24` for an issue on
  2026-02-07). The terms text and the structured due dates contradict each other.
- Condition: the payment terms text and every due date of the invoice give the same period from
  the issue date, and terms with the same ID mean the same period in 04 and 16.
- Options: (a, preferred) make all due dates 2026-04-16, as the ginnery's standard terms say;
  (b) if the mill was granted 30 days, give these terms their own ID and note ("30 days net.").
- Needs decision: no

## Checked and consistent
- Line: 6 129 kg × 0.988 per 1 kg = 6 055.452 = line extension = tax-exclusive = tax-inclusive = payable (no allowances, charges or prepayment); tax 0.000 on the O subtotal of 6 055.452, which equals the tax-exclusive amount.
- Order: price, quantity, amount, order line 1 and the buyer's accounting cost `2200` match 08; the invoice is in the requested invoice currency XLC.
- Tax: category O "outside scope of tax" with the scheme "No general sales tax" for a sale from Lisavu, the same treatment as in the order 08; the buyer's Bayvarra sales-tax registration on an export invoice is the customer's identification for its import.
- Payment: `check_ids.py` passes the RF reference `RF46SCGINV260210` and the ginnery's account `XL31BSEL0020004922263`, which is the ginnery's account also in 06 and 18; 18 pays the full 6 055.452 quoting this RF reference.
- Penalty interest 6 % per year, simple, the same as under `XL-STD` in 04.

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XLC`: a payment currency equal to the document currency was suspected of being a filler (as the identity rates in 04) — refuted because the buyer is in Bayvarra and pays from a Lume account (18); stating that the invoice is to be paid in coral is information the buyer needs, and no exchange rate is added.
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: shared charges on a cross-border transfer, suspected of making the ginnery receive less than invoiced — refuted because 18 reports the full amount remitted and a zero balance; the sharing of bank charges is the usual cross-border arrangement.
