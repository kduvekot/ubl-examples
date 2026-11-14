# LLM review: 04-ExpressionOfInterestRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/04-ExpressionOfInterestRequest.xml`, Git blob `1ca94275bd6d396987ad7aa46080a104842bb2c3` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/04#F1 · Low · A share of 60 % for the party that only supplies the slats, in a consortium that does not exist yet
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:ParticipationPercent` = `60`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Supplies the slats; a bench maker would build the benches.`
- XPath: `/ExpressionOfInterestRequest/cbc:Note` = `The sawmill considers a tender for lot 1 with a bench maker and asks to follow the procedure.`
- Why: `ParticipationPercent` is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage." The sawmill has no partner yet (it only "considers" a tender, and later withdraws because "No bench maker joined", example 10), so a share cannot have been agreed; and the party that supplies five hardwood slats of a steel-framed bench estimated at 499 lume would hardly carry 60 % of it while the maker of the bench carries 40 %. The figure has no basis in the document.
- Condition: a participation percentage is given only where a consortium with agreed shares exists, and then fits what each member contributes.
- Options: (a, preferred) leave the percentage out of an expression of interest made before a partner is found; (b) keep a share that fits the slats' part of a bench and say that it is the share the sawmill intends.
- Needs decision: yes

## Checked and consistent
- The example contains no amounts, prices, taxes on a transaction, payment data or guarantees. The parties' tax scheme entries (state sales tax STT, currency XBL; the department with exemption PUBLIC) are the same as in the other examples of the flow.
