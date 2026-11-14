# LLM review: 12-BusinessInformation.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/12-BusinessInformation.xml`, Git blob `0bf87195abba0708389105425a425c36428e3dc5` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/12#F1 · Low · The capability's amount and quantity say neither what they measure nor agree with the tenderer's own qualification
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:Description` = `Steel frame benches, cast, galvanised and coated in its own plant.`
- Why: `ValueAmount` is "A monetary amount as a measure of this capability", `ValueQuantity` "A quantity as a measure of this capability". For a production capability with the evidence "Annual accounts", 4800000.00 lume may be the yearly production value, the turnover in benches or the value of the plant; 6000 "each" may be a yearly output or something else; no period is given, only a validity until the end of 2026. Two days earlier the same company describes itself to the same buyer with other figures: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.` (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`) and `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`. If both quantities are the yearly output of benches, 6000 and 4000 contradict each other; if they are not, the extract does not say what its figures are. I could not settle which, hence Low. (For scale: 6000 benches at the tendered 499 lume would be 2994000.00, 4000 benches 1996000.00; neither gives 4800000.00.)
- Condition: the extract says what the amount and the quantity measure and for which period, and figures for the same measure are the same in this extract and in the tenderer's qualification (example 13), or the difference is explained (register figure of an earlier year, all products against benches only).
- Options: (a, preferred) describe the figures ("production in 2025: 6,000 pieces of street furniture, of which 4,000 benches, sales value 4.8 million lume") and keep example 13 consistent with it; (b) align the quantity with example 13 and drop the amount.
- Needs decision: yes

## Checked and consistent
- The amount is in lume, the currency of the receiving authority, for a company whose capital is stated in ferra (`CorporateStockAmount` 250000000 XUF); at the rate the flow's invoice uses (2088000 XUF for 20880.00 XBL, 100 to 1) the capital is 2.5 million lume, in proportion with the figures here and in example 13.
- The example contains no prices, taxes on a transaction, payment data or guarantees.
