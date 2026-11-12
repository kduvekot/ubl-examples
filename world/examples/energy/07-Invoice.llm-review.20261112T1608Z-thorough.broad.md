# LLM review: 07-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

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

### energy/07#F1 · Medium · Export exemption for gas that no customs declaration of the flow sends to this buyer
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `XU-R-105918`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: the 2 400 MWh are invoiced free of tax as an export ("Export outside Bayvarra"). The export declaration 04 includes them in its 39 200 MWh but names only Montebrio Power as consignee, and the only import declaration (05) covers Montebrio's 36 800 MWh. In the flow, nothing shows these 2 400 MWh leaving Bayvarra for Ferrano Energy or being imported by it, which an export exemption rests on.
- Condition: the export of the gas sold to Ferrano Energy is documented with Ferrano Energy as consignee (and its import, if the flow shows imports).
- Options: (a, preferred) split the export declaration's consignments by buyer and add Ferrano Energy's import declaration; (b) state in the story that Ferrano Energy's gas is declared elsewhere and leave the flow as is.
- Needs decision: yes

### energy/07#F2 · Medium · Pricing exchange rate on a price that is set in ferra
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- Why: `PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole." It implies a price converted from lume, while the note says the contract prices in ferra and there is no other exchange rate in the document. A conversion for the seller's tax reporting in lume belongs in `TaxCurrencyCode`/`TaxExchangeRate`. Same in 06-Invoice.xml.
- Condition: an exchange rate on the price only if the price is converted, in agreement with the note.
- Options: (a, preferred) remove it, and add `TaxCurrencyCode`/`TaxExchangeRate` if the seller reports in lume; (b) change the note if the contract price is in lume.
- Needs decision: yes

### energy/07#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` is the language. 362 occurrences in 213 of the 250 XML examples.
- Condition: LocaleCode holds a locale (e.g. `en-XB`) or is absent.
- Options: (a, preferred) `en-XB`; (b) omit.
- Needs decision: no

### energy/07#F4 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`). World convention; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/07#F5 · Low · Urvanian address renderings tagged en-XB, elsewhere en-XU
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: Ferrano Energy's address carries `en-XU` in 01-UtilityStatement.xml, 02-Invoice.xml and 03-Invoice.xml and `en-XB` here; the text is the Urvanian English form.
- Condition: the renderings of one address carry the same language tag in every example.
- Options: (a, preferred) `en-XU`; (b) document the rule.
- Needs decision: no

### energy/07#F6 · Low · Buyer's contact is retail customer service for a wholesale gas purchase
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Ferrano Energy buys 2 400 MWh of gas wholesale; its customer service in Sales serves its own retail customers, not procurement or payables.
- Condition: the accounting customer's contact deals with energy procurement or payables.
- Options: (a, preferred) a procurement/accounts-payable contact; (b) omit.
- Needs decision: no

## Checked and consistent
- 2 400 × 3 600 = 8 640 000 = LineExtensionAmount = TaxableAmount = PayableAmount; penalty 1.5 % = 129 600.
- 2 400 + 36 800 (06) = 39 200 MWh = the export declaration's quantity (04).
- RF14KGINV260158 check digits OK; payee account as in 06.
- Supplier data identical to 06; customer data identical to 01–03 apart from the language tag (F5).

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode`: suspected contradiction with `/Invoice/cbc:PaymentCurrencyCode` — refuted: paying ferra into a lume account with bank conversion is normal cross-border practice.
