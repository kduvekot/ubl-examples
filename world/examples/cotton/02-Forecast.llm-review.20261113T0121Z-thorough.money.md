# LLM review: 02-Forecast.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/02-Forecast.xml`, Git blob `564d177fc853a93d7bb7f285f6471573cea2ed35` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/02#F1 · Low · Sender's tax registration in a forecast that does nothing with tax
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/Forecast/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: a Forecast is "a document used to forecast sales or orders"; this one carries a quantity
  (24 000 kg of lint) and no price, amount or tax. The mill's sales-tax registration in the Coastal
  State has no use in it: nothing in the forecast is taxed, and the ginnery (receiver) is not
  asked to do anything with it. It reads as the party's master data copied into a document that
  does not use it (section 4.8, rule "no fillers"). The same block appears in the non-billing
  documents 07, 09, 10, 12, 13 and 14 of the flow (counted with lxml over `cotton/*.xml`, every
  `PartyTaxScheme`).
- Condition: the forecast carries a party tax registration only if the forecast does something
  with it, otherwise none.
- Options: (a, preferred) drop the sender's `PartyTaxScheme` from the forecast; (b) keep it and
  give the forecast a tax-relevant purpose, which it does not have in this story.
- Needs decision: no

## Checked and consistent
- No price, amount, tax category or payment information is present; the forecast's only quantity is `/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `24000` kg, which carries no monetary value to check.
