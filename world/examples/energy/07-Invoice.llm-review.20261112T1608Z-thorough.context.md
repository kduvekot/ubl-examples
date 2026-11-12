# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/07#F1 · High · Exported gas sold to Ferrano Energy that no customs declaration of the flow consigns or imports to it
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: The invoice sells 2400 MWh of gas to Ferrano Energy tax-free as an export. The export declaration 04 consigns the whole 39200 MWh (36800 + 2400) to Montebrio Power, and the only import declaration (05) imports 36800 MWh for Montebrio. The 2400 MWh billed here are thus exported to a consignee other than the buyer and are never imported by Ferrano Energy; the exemption claimed here is not supported by the customs documents of the flow as they describe the goods.
- Condition: The 2400 MWh billed to Ferrano Energy appear in an export declaration with Ferrano Energy (or its agent) as consignee and are imported under a declaration naming the importer, or the invoice chain is changed so that the buyer of exported gas is the consignee of the export.
- Options: (a) preferred: split the export declaration into two consignments and add an import declaration by Ferrano Energy for 2400 MWh (a new document in the flow); (b) Montebrio imports everything and resells 2400 MWh to Ferrano Energy domestically, which replaces this invoice by a Montebrio invoice with Urvanian VAT.
- Needs decision: yes (adds or changes documents of the flow)

### energy/07#F2 · Medium · Pricing exchange rate from lume on a price the invoice says is set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- Why: PricingExchangeRate is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole." The price (3600 XUF/MWh) is in the document currency and the note says it is set in ferra; there is no lume price and no document-level rate. The rate has no function here and contradicts the note's story.
- Condition: Either no exchange rate on the price, or a note and price that agree the price was set in lume.
- Options: (a) preferred: drop PricingExchangeRate; use TaxCurrencyCode/TaxExchangeRate at document level if the seller needs the lume equivalent; (b) change the story to a lume contract price.
- Needs decision: no

### energy/07#F3 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` (ISO 639) repeats the language, not a locale. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (e.g. en-XB).
- Options: (a) preferred: `en-XB`; (b) leave it out.
- Needs decision: no

### energy/07#F4 · Low · The plant's coordinates on an invoice that does nothing with them
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- Why: The seller's plant description and coordinates have no role in this payment request; the item carries its origin already. Copied master data.
- Condition: The seller party carries only data the invoice uses.
- Options: (a) preferred: leave PhysicalLocation out; (b) keep it only for a stated purpose.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2400 MWh × 3600 XUF = 8640000; tax 0; penalty 1.5 % = 129600.
- 36800 (06) + 2400 (this invoice) = 39200 MWh, the quantity of the export declaration 04.
- Ferrano Energy as buyer of wholesale gas fits its role as retailer (it receives the gas network invoice for Valdara's gas connection in 02 and the statement 01).

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`: suspected copied master data — refuted because the exporter's customs number is relevant on an export invoice.
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected redundancy — refuted because the payee account is held in lume.
