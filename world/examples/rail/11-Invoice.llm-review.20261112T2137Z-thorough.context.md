# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/11#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: The factor is "used to calculate the value measurement (e.g., emissions per unit of activity)", the base is "the base quantity to which the value factor applies". 0.82 × 1 bench = 0.82, not 96 kg CO2e. Same values in 39 examples over `*.xml`.
- Condition: factor × base = value, or factor and base absent.
- Options: (a) preferred: drop factor and base; (b) the real factor and base.
- Needs decision: no

### rail/11#F2 · Medium · FullnessIndicationCode carries the emission boundary
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The element is "a code signifying whether a piece of transport equipment is full, partially full, or empty", a parameter of a transport emission; a product's cradle-to-gate boundary is not such a value. 39 occurrences over `*.xml`.
- Condition: FullnessIndicationCode, where present, says how full transport equipment is.
- Options: (a) preferred: drop it here; (b) keep it as a recorded gap for the UBL TC.
- Needs decision: yes

### rail/11#F3 · Medium · Lifecycle stage code covers less than its description
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is EN 15804 module A3 in the world's list; the description covers A1–A3 (SOURCING and MANUFACTURING).
- Condition: code(s) and description name the same stages.
- Options: (a) preferred: two entries; (b) narrow the description.
- Needs decision: no

### rail/11#F4 · Medium · LocaleCode holds a bare language code
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639) names no locale. 362 occurrences over `*.xml`.
- Condition: a locale (e.g. `en-XB`) or absent.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/11#F5 · Medium · Province in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/11#F6 · Low · Product passport data on the invoice line
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: An invoice requests payment for the benches delivered. Repairability, maintenance, resource consumption, packaging waste, the cradle-to-gate footprint, the load-capacity test and dimensions are product documentation (referenced as VI-RM-B180 and VI-DS-B180); the invoice does nothing with them.
- Condition: the invoice line carries what identifies, classifies and taxes the item.
- Options: (a) preferred: leave product documentation to the referenced documents; (b) keep only what a buyer's booking or a legal rule needs on an invoice.
- Needs decision: no

### rail/11#F7 · Low · Share listing and warehouse provider of the seller
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The invoice does nothing with the seller's share listing or its warehousing provider.
- Condition: no party data without a reason in the invoice.
- Options: (a) preferred: drop both here.
- Needs decision: no

## Checked and consistent
- The invoice references the order (`/Invoice/cac:OrderReference/cbc:ID` = `LD-PO-26-0325`, rail/01) and its line 1; quantity 192, price 49900 and line amount 9580800 agree with the order.
- Tax category G with exemption EXP fits an export to Bayvarra; the note on DAP agrees with the order's delivery terms.
- Settlement discount 2 % of 9580800 = 191616: holds.

## Considered and refuted
- `/Invoice/cbc:PaymentCurrencyCode` = `XUF`: suspected redundant with the document currency — refuted because the buyer is in Bayvarra (currency XBL), so stating that payment is in XUF has a reason.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: suspected master data copied into the invoice — refuted because share capital is information that company law in several jurisdictions requires on invoices of a public limited company (own knowledge), so it has a plausible reason here.
