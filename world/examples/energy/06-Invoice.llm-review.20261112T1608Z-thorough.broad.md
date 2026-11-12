# LLM review: 06-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

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

### energy/06#F1 · Medium · Pricing exchange rate on a price that is set in ferra
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Invoice/cbc:Note` = `Priced in ferra as the supply contract says: the buyer's own currency.`
- Why: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole." It implies the price was converted from lume. The note says the contract sets the price in ferra, the document has only ferra amounts and no document-level exchange rate. Either the price is a converted lume price (and the note is wrong), or the rate has nothing to do with the price; the likely purpose, reporting the sale in Kelpstone's tax currency (its tax scheme's currency is XBL), is what `TaxCurrencyCode`/`TaxExchangeRate` are for.
- Condition: an exchange rate is present on the price only if the price is converted from another currency, and the note agrees; a rate needed for the seller's tax reporting sits in the element meant for it.
- Options: (a, preferred) remove the pricing exchange rate and, if the seller reports in lume, add `TaxCurrencyCode` XBL with `TaxExchangeRate`; (b) if the contract price is really 36 XBL/MWh, change the note and keep the rate.
- Needs decision: yes

### energy/06#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` is the language itself. 362 occurrences in 213 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'`).
- Condition: LocaleCode holds a locale (e.g. `en-XB`) or is absent.
- Options: (a, preferred) `en-XB`; (b) omit.
- Needs decision: no

### energy/06#F3 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries…"; a province is an administrative division (`CountrySubentity`). World convention; 219 occurrences in 104 of 250 XML examples.
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity`; (b) document the convention.
- Needs decision: yes

### energy/06#F4 · Low · Urvanian address renderings tagged en-XB, elsewhere en-XU
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- Why: Montebrio Power's address carries `en-XU` in 03-Invoice.xml, 05-ImportCustomsDeclaration.xml and 09-RemittanceAdvice.xml, `en-XB` here and in 04, 07 and 08 (documents sent from Bayvarra). The text is the Urvanian English form.
- Condition: the renderings of one address carry the same language tag in every example.
- Options: (a, preferred) `en-XU`; (b) document the rule.
- Needs decision: no

## Checked and consistent
- 36 800 × 3 600 = 132 480 000 = LineExtensionAmount = TaxableAmount = PayableAmount; tax 0 under category G (free export) with exemption reason EXP, scheme STT of the seller's territory.
- Penalty 1.5 % of 132 480 000 = 1 987 200; penalty period from 2026-05-04 (day after due date) for one month; matches 08-Reminder.xml (19 872 XBL × 100) and 09-RemittanceAdvice.xml line 2.
- Quantity and value equal 05-ImportCustomsDeclaration.xml; at 100 XUF/XBL the price equals the export declaration's 36 XBL/MWh (04).
- RF41KGINV260157 and the payee account check digits OK (`check_ids.py`); the same account and reference are used in 08 and 09.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode`: suspected a contradiction between the payee account in lume and `/Invoice/cbc:PaymentCurrencyCode` ferra — refuted: paying ferra into a lume account with conversion by the banks is normal for cross-border payments, and ChargeBearer SHAR covers the fees.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: suspected master data (customs-trader number) without use — refuted: the invoice of an export is evidence for the importer's customs declaration (05), where this number is relevant.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name`: suspected a trading contact on an invoice — refuted: for a wholesale gas contract the buyer's trading desk is the counterpart of the seller's gas sales contact.
