# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/02#F1 · Low · A penalty period of one month against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-06-02`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: UBL defines `PaymentTerms/PenaltyPeriod` as "The period during which penalties may apply". A period starting 2026-06-02 with a duration of one month says penalties may apply only until early July; the note says the surcharge accrues for every month of delay, without an end. `PenaltyAmount` = 22.32 is one month's surcharge (1.5 % × 1488.00), so the period seems meant as "the period one PenaltyAmount covers", which is not what the element means. The same pattern (a one-month `PenaltyPeriod` next to a "per month" surcharge) is in `04-Invoice.xml` and `07-Invoice.xml`, and in 18 XML files across the world (counted with `grep -rl --include='*.xml' '<cac:PenaltyPeriod>' world/examples`, all with `DurationMeasure unitCode="MON"` = 1).
- Condition: the penalty period either has no end (start date only) or ends when the terms say penalties stop; the per-month rate and the one-month PenaltyAmount are stated without suggesting that penalties stop after one month.
- Options: (a, preferred) keep `StartDate` and drop `DurationMeasure`, so the period is open-ended as the note says; keep `PenaltyAmount` as the surcharge per month, stated in the note ("22.32 per month"); (b) if the terms really cap penalties, state the cap in the note and keep the duration.
- Needs decision: no

### packaging/02#F2 · Low · Export exemption without any delivery information in the invoice
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `G`
- Why: the invoice applies category `G` ("Free export item, tax not charged") because the goods leave Bayvarra, but carries no `Delivery` (no delivery date, place or country) and no `DeliveryTerms`; the only foreign element is the customer's address. The order agreed `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA` at the seller's dispatch in Lumeport, i.e. the goods are handed over in Bayvarra; whether and when they were exported, which is what the exemption rests on, is not visible in the tax document. Own knowledge: sales-tax and VAT export exemptions are normally tied to evidence that the goods were dispatched abroad, which invoices commonly state through the delivery place and date.
- Condition: the invoice states when and to which country the goods were delivered or dispatched (e.g. `Delivery/ActualDeliveryDate` and `Delivery/DeliveryLocation` with the country of destination, or the despatch reference), so the export exemption has its basis in the document.
- Options: (a, preferred) add a `cac:Delivery` with the actual delivery (handover to Trasvia Haulage) date and the destination in Urvania, and the `DeliveryTerms` FCA from the order; (b) leave it as it is if the world's export evidence lives only in the customs documents, and say so in the exemption reason text.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `480` × `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3.1` / `/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1` = 1488.00 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `1488.00`; totals `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `1488.00`, tax 0.00, `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `1488.00` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1488.00`.
- Against the order: quantity, price, item and tax treatment equal `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `1488.00`; `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521` resolves to `01-Order.xml`.
- Tax: category `G`, 0 %, reason `EXP`, scheme `STT` identical in `TaxTotal` and `ClassifiedTaxCategory`; the seller is registered for STT in Coastal State, the buyer in Urvania.
- Payment terms: due date 2026-05-02 + 30 days = 2026-06-01 = `/Invoice/cbc:DueDate` = `2026-06-01` = `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-06-01` = `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-06-01`; `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `22.32` = 1.5 % × 1488.00; penalty start the day after the due date.
- Payment means: credit transfer to Rivermouth Packaging's own account, which is the same in `PayeeFinancialAccount` and in the supplier party; cross-border payment from Urvania over the Trade Accord rail (`RTNS`) with shared charges (`SHAR`) fits a payment between two countries; the RF creditor reference `RF29RPINV260522` has a valid check (check_ids.py) and is quoted in the instruction note.
- Currency: document and payment currency XBL; the payee account is held in XBL.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`: suspected a duplicate of the payee account — refuted because it is the account of the party that receives the payment under this invoice, and it agrees with `PayeeFinancialAccount`.
- `/Invoice/cbc:PaymentCurrencyCode` = `XBL`: suspected redundant, equal to the document currency — refuted because the payer is in Urvania (currency XUF) and the element states that payment is expected in lume, which is a real piece of information for a foreign payer.
- `/Invoice/cbc:AccountingCost` = `Raw materials and parts`: suspected not to fit stretch film — refuted as in the order (packaging consumable booked by a manufacturer under materials).
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF29RPINV260522`: suspected to duplicate `PaymentID` — refuted because the note is the instruction to the payer, the ID is the structured reference; they agree.
