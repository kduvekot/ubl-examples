# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/07-Invoice.xml`, Git blob `c9439fcedf37997f7173ad361e9246f5cc5439d9` (committed)
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

### energy/07#F1 · Medium · Pricing exchange rate on a price that the note says was set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`
- Why: as in 06-Invoice: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole", i.e. a price converted from another currency. The note says the price was set in ferra, all currencies of the invoice are XUF and there is no document-level rate. If the rate is there for the seller's books in lume (its tax scheme currency is XBL), the elements for that are `TaxCurrencyCode` and `TaxExchangeRate`.
- Condition: the exchange rate is a price-level rate only if the price was converted (and the note then says so), or it is the document-level rate to the seller's tax currency, or it is absent.
- Options: (a) preferred: TaxCurrencyCode XBL with TaxExchangeRate, PricingExchangeRate dropped; (b) price set in lume: keep the rate, correct the note; (c) drop the rate. Resolve together with 06-Invoice so that both invoices of the same supply contract tell the same story.
- Needs decision: yes (which story: price set in ferra or in lume)

### energy/07#F2 · Low · The exported gas of this sale has no import into Urvania in the flow, and the export names another consignee
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `8640000`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: the invoice exempts the sale as an export outside Bayvarra. The only export declaration of the flow (energy/04) covers 39200 MWh = 36800 (energy/06) + 2400 (this invoice), with a value of 1411200.00 XBL that is exactly both invoices at 36 XBL/MWh, but names only Montebrio Power as consignee. The only import declaration (energy/05) is Montebrio Power's and covers its own 36800 MWh and 132480000 XUF. So the 2400 MWh (8640000 XUF) that Ferrano Energy buys here are exported to Montebrio Power and imported by nobody: the customs value and the import VAT of this purchase are not accounted for anywhere in the flow. A consignee may differ from the buyer, and the import might be outside the flow, so this is not necessarily a contradiction; but as it stands the money of this sale cannot be followed through customs.
- Condition: the 2400 MWh of this invoice can be followed from the export to an import with the buyer (or a stated consignee on its behalf) as importer, with a customs value of 8640000 XUF; or the flow states why no import declaration of its own is needed.
- Options: (a) preferred: let the export declaration name both consignees (or two goods items), and add Ferrano Energy's import, or make the import declaration cover both purchases with the importer per goods item if the world's customs allow it; (b) state in the flow (e.g. a note in the import declaration) that Montebrio Power imports the whole border flow and passes 2400 MWh on, which would then also change who sells to Ferrano Energy.
- Needs decision: yes (adds or changes a document of the flow)

## Checked and consistent
- Line and totals: 2400 × 3600 = 8640000 = LineExtensionAmount, TaxExclusiveAmount, TaxInclusiveAmount and PayableAmount; tax 0 under category G, exemption EXP, Bayvarra's STT; supply type GOODS for gas.
- Penalty: 1.5 % of 8640000 = 129600 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `129600`; penalty period from the day after the due date, one month, as in 06-Invoice.
- Payment: RF14KGINV260158 passes its check digits; the payee account is Kelpstone's same lume account as in 06-Invoice, 08-Reminder and 09-RemittanceAdvice (XB45BLUM38522004817534, check passes).
- No reminder or remittance advice in the flow refers to this invoice; nothing in the flow says it was paid late, so its absence from the follow-up documents is consistent.

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF` against `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XBL`: payment in ferra into a lume account — refuted: a cross-currency credit transfer is normal, with ChargeBearerCode SHAR settling the charges.
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`: export exemption for a buyer who is not the consignee on the export declaration — refuted as a separate finding: the goods do leave Bayvarra under energy/04, which is what the exemption reason states; the remaining question is F2.
