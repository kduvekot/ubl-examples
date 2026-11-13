# LLM review: 09-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/09-ForwardingInstructions.xml`, Git blob `ba67389d2ddd1ff0fe54f4614822678c58b812b2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/09#F1 · Low · Exchange rate that no amount in the instructions uses, and without a date
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ExchangeRate` is "information about the rate of exchange (conversion) between two currencies". The only amount in the forwarding instructions is the insured value in lume (`/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`); nothing is stated or to be converted in coral, and the instructions ask the forwarder for nothing that would be paid or valued in coral. A rate without a `Date` also does not say when it applied. The element has no business reason in this document (no fillers).
- Condition: the forwarding instructions carry an exchange rate only if an amount in them is in, or must be converted to, the target currency, and then with the date the rate applies to.
- Options: (a) preferred: remove the exchange rate; (b) keep it only together with an amount that needs it (e.g. a value the forwarder must declare in coral at import) and give it a date.
- Needs decision: no

## Checked and consistent
- Insured value: 110 % of the CIF value of the sale, 53,778.00 × 1.10 = 59,155.80 (`/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`); the CIF value is the invoice total (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`), and the same insured value is stated in the bill of lading and both customs declarations. The insurer (Wavesure Cargo Insurance) is the same party as the insurer in `14-BillOfLading.xml`.

## Considered and refuted
- `/ForwardingInstructions/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`: suspected that on 2026-05-09 the shipper could not yet know the CIF value, which contains the freight (2,950.00) and premium (140.00) only fixed in the bill of lading of 2026-05-14 — refuted because the ocean freight is a published box rate under the carrier's tariff (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:TariffCode` = `TWL-T-0940`) and the premium a known rate, so the CIF value is calculable when the instructions are written; any remaining doubt is a timeline question across documents.
