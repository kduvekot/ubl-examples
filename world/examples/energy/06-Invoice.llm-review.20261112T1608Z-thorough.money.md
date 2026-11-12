# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/06-Invoice.xml`, Git blob `7c0dad8fdbb0040b1dab2a0e3035fb59f281af39` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/06#F1 · Medium · Pricing exchange rate on a price that the note says was set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`
- Why: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole": it says the price was converted from another currency. Here the price is a ferra price (the note: priced in ferra as the contract says), the document, payment and line currencies are all XUF, and the document has no exchange rate of its own that this one could differ from. So either the price was really set in lume (36 XBL/MWh converted at 100), which contradicts the note, or the rate serves another purpose. The likely purpose is the seller's own books and tax reporting: Kelpstone's tax scheme is kept in lume (TaxScheme CurrencyCode XBL); UBL has `TaxCurrencyCode` and `TaxExchangeRate` ("The exchange rate between the document currency and the tax currency") for that, and the export declaration energy/04 indeed states the value in lume (1411200.00 XBL for this and 07's gas at this rate). The same pattern occurs in 07-Invoice.
- Condition: the exchange rate in the invoice has the meaning of the element it is in: a price-level rate only if the price was converted from another currency (and then the note does not say it was set in ferra), or the rate to the seller's tax currency at document level (TaxCurrencyCode XBL with TaxExchangeRate), or no rate at all.
- Options: (a) preferred: TaxCurrencyCode XBL and TaxExchangeRate XUF→XBL (0.01, or XBL→XUF 100 with the operator that matches), with the tax amounts in XBL as `TaxTotal` in the tax currency if the world's rules ask for them; drop PricingExchangeRate; (b) if the contract really fixes the price in lume, keep PricingExchangeRate and change the note to say so; (c) drop the rate if it has no use in the invoice.
- Needs decision: yes (which story: price set in ferra or in lume)

## Checked and consistent
- Line and totals: 36800 × 3600 = 132480000 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `132480000` = LineExtensionAmount, TaxExclusiveAmount, TaxInclusiveAmount and `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`; tax 0.
- Tax: category G with exemption reason EXP ("Export outside Bayvarra") under Bayvarra's state sales tax (STT), in the subtotal and on the item; the goods are exported under energy/04 and imported by the buyer under energy/05; supply type GOODS for gas (own knowledge: gas is goods under VAT practice).
- Penalty: 1.5 % of 132480000 = 1987200 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `1987200`; penalty period starts on 2026-05-04, the day after the due date 2026-05-03, for one month, as the note ("1.5 % surcharge per month late") says.
- Follow-up documents: the reminder energy/08 charges exactly this penalty (19872.00 XBL = 1987200 XUF at the same rate) on this invoice of 132480000 XUF, after one month; the remittance advice energy/09 pays 132480000 + 1987200 = 134467200 XUF quoting this invoice's RF reference `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157` (check digits pass) to this payee account (XB45BLUM38522004817534, check passes).
- The rate 1 XBL = 100 XUF agrees with energy/04 (39200 MWh × 36 XBL = 1411200 XBL), energy/08 and energy/09 and with other flows.

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF` against `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XBL`: payment in ferra into a lume account — refuted: a cross-currency credit transfer is normal; the banks convert, and ChargeBearerCode SHAR settles who bears the charges.
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`: its definition speaks of "payment after the settlement period", and there is no settlement period in the terms — refuted: the due date and the penalty period (from 2026-05-04) make the point clear.
- `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`: the note says "per month", the structured period covers only the first month — refuted: the penalty amount is for that first month, and that is what the reminder charges.
- No TaxPointDate (02-Invoice and 03-Invoice carry one) — refuted: an export without tax charged needs no tax point in the invoice; the definition makes it optional.
