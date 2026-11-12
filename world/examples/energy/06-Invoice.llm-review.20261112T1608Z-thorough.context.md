# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/06#F1 · Medium · Pricing exchange rate from lume on a price the invoice says is set in ferra
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- Why: PricingExchangeRate is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole." The price is in ferra, the document currency, and the note says the contract prices in ferra; there is no lume price to convert and no document-level exchange rate it could differ from. The rate therefore has no function in this price, and it suggests the opposite of the note (a lume price converted to ferra). If the rate is wanted for Kelpstone's reporting in lume, Invoice/TaxExchangeRate (or a Note) is the element for that.
- Condition: Either the price carries no exchange rate, or the note and the price agree that the price was set in lume and converted at the stated rate.
- Options: (a) preferred: drop PricingExchangeRate (consistent with the note); if the seller needs the lume equivalent for reporting, use TaxCurrencyCode/TaxExchangeRate at document level; (b) change the story to a lume contract price (36 XBL/MWh) converted at 100, and change the note.
- Needs decision: no

### energy/06#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` (ISO 639) repeats the language, not a locale. The same value occurs 362 times in 213 of 250 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: LocaleCode is absent or holds a locale (e.g. en-XB).
- Options: (a) preferred: `en-XB`; (b) leave it out.
- Needs decision: no

### energy/06#F3 · Low · The plant's coordinates on an invoice that does nothing with them
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- Why: The seller's physical location (plant description, coordinates) has no role in requesting payment for gas measured at the border station; the item already carries its origin (OriginCountry, OriginAddress). It looks copied from the party's master data.
- Condition: The seller party carries only data the invoice uses, or the invoice's purpose explains the physical location.
- Options: (a) preferred: leave PhysicalLocation out of the invoice; (b) keep it only if it serves a stated purpose (e.g. place of supply, which would then belong in a delivery element).
- Needs decision: no

## Checked and consistent
- Arithmetic: 36800 MWh × 3600 XUF = 132480000; tax 0 under category G; payable 132480000; penalty amount 1.5 % = 1987200.
- Against 05: the customs value `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000` equals this invoice.
- Against 08 and 09: the reminder and the remittance advice refer to KG-INV-26-0157 with this amount and this due date.
- SupplyTypeCode GOODS fits natural gas; exemption reason EXP fits a supply leaving Bayvarra.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412877`: suspected copied master data — refuted because on an export invoice the exporter's customs number is commonly given and links the invoice to the export declaration.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cbc:ID` = `33/03`: suspected unused data — refuted because origin information on an export invoice supports the customs declarations.
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected redundancy with DocumentCurrencyCode — refuted because the payee account is held in lume, so stating that payment is in ferra is information the payer needs.
