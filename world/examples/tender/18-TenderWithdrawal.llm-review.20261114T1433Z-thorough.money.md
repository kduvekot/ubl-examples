# LLM review: 18-TenderWithdrawal.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/18-TenderWithdrawal.xml`, Git blob `d02ecd959438556075917a15e5b54cd6caa90c26` (committed)
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

## Checked and consistent
- The reason given, `/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`, agrees with the amounts of the two tenders: the withdrawn one has `17-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `112800.00` (470 lume a bench for 240 benches), the corrected one `19-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `115200.00` (480 lume); the installation line is unchanged (3840.00 in both), so only the price per bench changed, by 2400.00 in total (116640.00 to 119040.00).
- The example itself contains no amounts, prices, taxes on a transaction, payment data or guarantees.

## Considered and refuted
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator`: suspected that withdrawing a tender should have a consequence for the tender guarantee that the terms require (2400.00 lume), which the withdrawal does not mention — refuted because the withdrawal is made on 2026-02-24, before the tender deadline of 2026-02-26; a tender guarantee secures the tender during its validity after the deadline, and a tender may be replaced before it.

## Outside this review
- The corrected tender that this withdrawal says "follows" (example 19) is issued at 12:10 on the same day, before this withdrawal (17:56); the order of the two is a timeline question.
- The withdrawn and the corrected tender both state the fees of 50.00 and 12.00 lume; whether they were incurred once or twice is raised in the review of example 17.
