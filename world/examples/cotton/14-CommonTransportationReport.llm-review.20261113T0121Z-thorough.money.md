# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/14-CommonTransportationReport.xml`, Git blob `081267759b51366ff3d8aad9d0f0d1d2385f1b91` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### cotton/14#F1 · Low · Reporter's tax registration and share capital in a pre-arrival report
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: the report is "a common document used for reporting transport related issues to
  authorities"; here a pre-arrival report to the Port of Lumeport. It announces no dues, fee or
  charge, so the carrier's Coastal State sales-tax registration has no use in it, and its share
  capital of 40 000 000 XBL, fully paid, even less (section 4.8, master data copied into a document
  that does not use it). The same blocks are in 12 and 13.
- Condition: the report carries the reporter's tax registration or capital only if the report
  does something with it (e.g. it is the basis on which port dues are billed, and says so).
- Options: (a, preferred) drop the reporter's `PartyTaxScheme`, `CorporateStockAmount` and
  `FullyPaidSharesIndicator`; (b) keep the tax registration if the port bills its dues from the
  pre-arrival report, and make that visible.
- Needs decision: no

## Checked and consistent
- The report contains no amount, price, tax or payment information, and its purpose (pre-arrival reporting) does not need any.
