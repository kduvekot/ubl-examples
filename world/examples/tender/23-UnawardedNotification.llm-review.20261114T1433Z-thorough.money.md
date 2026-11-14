# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/23-UnawardedNotification.xml`, Git blob `39a6b648377d44e8a82177e1c91a57309cca5cc5` (committed)
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

### tender/23#F1 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `Amount` "the monetary amount assigned to the subcontracted task". 4320.00 / 124080.00 = 3.4816 %; 3.5 % of 124080.00 is 4342.80. The amount is the right one (240 × 18 lume, line 2 of 15-Tender.xml); the rate is a rounding of it. The same pair is in 21, 22 and 24.
- Condition: `Rate` × awarded amount / 100 equals `Amount` to the cent, or the rate is absent.
- Options: (a, preferred) drop `Rate`; (b) state it with the decimals needed.
- Needs decision: no

## Checked and consistent
- The note's statement that the receiver's tender "was lower in price" holds: its tender is 119040.00 (`19-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`), the awarded one 124080.00.
- Awarded amount 124080.00 = 15-Tender.xml, 21, 22 and 24. Subcontract amount 4320.00 = 240 × 18 lume.
- With the call's price formula (60 × lowest / tendered) the receiver scores 60 and the winner 60 × 119040 / 124080 = 57.56 on price, so the winner needs at least 2.44 points more on quality (40 points); "ranked second … scored lower on quality" is arithmetically possible.
- The notification carries no `FinalFinancialGuarantee`, correctly: the receiver is not the winner.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount`: the winner's subcontract amount and price per bench are told to the losing tenderer — refuted as a money finding because the same terms are published in the contract award notice (21-ContractAwardNotice.xml), so nothing confidential is added here.
- `/UnawardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: the winner's total in a notification to the loser — refuted for the same reason (published in 21), and the unsuccessful tenderer needs the winning price to judge an appeal.
