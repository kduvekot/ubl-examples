# LLM review: 07-ForecastRevision.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/07-ForecastRevision.xml`, Git blob `fc49267ef8416292c4c72e5eb19588b0cdccd24f` (committed)
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

### cotton/07#F1 · Low · Sender's tax registration in a forecast revision that does nothing with tax
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- Why: a Forecast Revision is "a document used to revise a Forecast"; this one revises a quantity
  and carries no price, amount or tax. The mill's Coastal State sales-tax registration has no use
  in it (rule "no fillers"; section 4.8, master data copied into a document that does not use it).
  The forecast it revises carries the same block (02).
- Condition: the forecast revision carries a party tax registration only if it does something
  with it, otherwise none.
- Options: (a, preferred) drop the sender's `PartyTaxScheme`, as for 02.
- Needs decision: no

## Checked and consistent
- No price, amount, tax category or payment information is present; the revised quantity `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cbc:Quantity` = `30000` kg carries no monetary value to check.
