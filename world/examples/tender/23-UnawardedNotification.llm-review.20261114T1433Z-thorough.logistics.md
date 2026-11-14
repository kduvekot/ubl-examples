# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

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

### tender/23#F1 · Low · Additional document reference with only an ID
- XPath: `/UnawardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-SCORES-BF`
- Why: "A reference to an additional document associated with this document." The element does not say what the document is, and the reference has no type or description; the document is not in the flow (grep for `>PWD-EVAL-SCORES-BF<` over `world/examples/**/*.xml`: this example only). From the identifier it is presumably the score sheet of Brackenmere's tender, which is what an unsuccessful tenderer needs to decide about an appeal.
- Condition: The reference states what it refers to (`cbc:DocumentType` or `cbc:DocumentDescription`).
- Options: add `cbc:DocumentType` "Evaluation scores of the tender" (preferred).
- Needs decision: no

### tender/23#F2 · Low · The contract may be formalised on the last day of the appeal period
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: The period "during which an appeal can be presented" includes 19 March; the period "during which a contract associated with the awarded project is to be formalized" starts on the same day, and the contract was in fact signed then (`24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`, 17:24). `22-AwardedNotification.xml` says "The contract follows after the standstill period". On 19 March both are true at once: Brackenmere may still appeal and the contract may already be signed.
- Condition: The formalisation period starts after the last day on which an appeal can be presented, or the appeal period ends before it.
- Options: (a) preferred: formalisation from 2026-03-20 (and the contract dated accordingly); (b) appeal period 9–18 March, if "within ten days" counts the day of the award.
- Needs decision: yes

## Checked and consistent
- GLN 9523710900008: check digit correct (`check_ids.py`).
- Award 9 March 09:30, this notification 9 March 10:15, the notification to the winner 13:37: in order. Appeal period 9–19 March is ten days from the award, as the call for tenders and the text say.
- The receiver is the tenderer of `19-Tender.xml`. "Lower in price" holds: 119040.00 (19) against 124080.00 (15). "The warranty offered scored lower": 6 years (19) against 10 years (15).
- `cac:TenderResult` is identical to that of `22-AwardedNotification.xml` (award ID, date, contract, lots, amounts, winner). Contract validity from 2026-03-23 for 24 MON agrees with the planned period 2026-03-23 to 2028-03-22.
- `cac:MinutesDocumentReference` PWD-MIN-AWARD-26 is the same in 21, 22 and 23.
- Codes TenderResultCode AWARDED, ContractTypeCode FRAMEWORK: in their lists.

## Considered and refuted
- `/UnawardedNotification/cac:TenderResult/cbc:TenderResultCode`: `AWARDED` in a notification to the loser — refuted: the tender result describes the outcome of the procedure (awarded, to the named winning party), not the receiver's outcome.
- `/UnawardedNotification/cac:TenderResult/cac:Contract/cbc:ID`: `PWD-2026-PARKS` equals the contract folder ID — refuted: the department numbers the contract like its file; order and invoice of the flow use the same number for the contract.
- `/UnawardedNotification/cbc:ID`: number …0209 issued before …0208 (`22-AwardedNotification.xml`, 13:37) — see 22; here the number is the later one issued earlier, kept as a finding there.
