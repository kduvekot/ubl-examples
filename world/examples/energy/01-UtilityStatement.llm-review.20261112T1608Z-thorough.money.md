# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/01-UtilityStatement.xml`, Git blob `ddb038e38819569df4aa78c5bfc77925766f9bb9` (committed)
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

### energy/01#F1 · High · Payable amount of the consumption is 0, but the parent invoice bills it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `61200`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`
- Why: `Consumption/LegalMonetaryTotal` is "The total amount payable on this consumption, including any allowances, charges, or taxes". The statement is the supplement of its parent invoice FG-INV-26-0150 (energy/02), and that invoice bills exactly this consumption: line 3, gas network use, 61200 kWh × 1.9 XUF = 116280 XUF net, 139536 XUF with 20 % VAT. A payable amount of 0 says that nothing is payable on this consumption, which the parent invoice contradicts. The value looks like a filler for the mandatory element (IND5/IND6: nothing implied by absence, no fillers). The note ("Metered consumption for the retail company's billing") explains why the statement exists, but not why nothing would be payable under the parent invoice it supplements.
- Condition: the payable amount of the consumption equals what the parent invoice charges for it (139536 XUF including VAT, or a stated net/gross split), or the statement no longer presents itself as the supplement of an invoice that bills this consumption.
- Options: (a) preferred: PayableAmount 139536 XUF, optionally with LineExtensionAmount 116280, TaxExclusiveAmount 116280 and TaxInclusiveAmount 139536 in the same LegalMonetaryTotal, so the statement reconciles with line 3 of the invoice; (b) if the statement is meant as pure metering data for the retailer's billing, attach it to the invoice that bills the consumption to the subscriber (utilities flow) instead, with that invoice's amount.
- Needs decision: no

## Checked and consistent
- Currency: `/UtilityStatement/cbc:DocumentCurrencyCode` = `XUF`, the same as the parent invoice and the payable amount's currencyID.
- Quantity against the parent invoice: the consumption in energy, 61200 kWh, equals `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`, the line priced per kWh at `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cac:Price/cbc:PriceAmount` = `1.9`; 61200 × 1.9 = 116280.
- The conversion behind the billed kWh: 29760 − 28410 = 1350 m³; 1350 × 4.9477 = 6679.4 m³; 6679 × 9.163 = 61199.6 ≈ 61200 kWh (figures from the description in the document).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: whether the statement should instead carry the retail price the subscriber pays (Ferrano Energy's own billing to Valdara Industries) — refuted as an alternative finding, because the parent of this statement is the grid operator's invoice to the retailer, so the amount to reconcile with is the network charge of that invoice (see F1).
- The electricity lines 1 and 2 of the parent invoice have no utility statement in this flow — refuted for this example: a statement may cover one consumption point; the question is noted in the review of 02-Invoice.
