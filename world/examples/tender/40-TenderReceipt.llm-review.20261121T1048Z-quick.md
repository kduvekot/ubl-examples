# LLM review: 40-TenderReceipt.xml

Flow: tender (PWD/2026/PARKS) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/tender/40-TenderReceipt.xml`, Git blob `fb68499a3905b81385fc297f216a45fdc97f7c23` (committed)
- Last commit changing the example: 99d799b3 2026-11-20 O97 and O78: the call states the withholding, tenders carry the tax subtotal, every time carries its place's UTC offset
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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
- The receipt answers `17-Tender.xml` (ID 26-0008, Brackenmere Furniture, issued 2026-02-20 16:37): the registered date and time are those of the tender, and the receipt follows a minute later; ContractFolderID and ProfileExecutionID PWD/2026/PARKS as in the tender.
- "Received on time": the deadline in `03-CallForTenders.xml:/CallForTenders/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-02-25` (12:00) is five days later.
- The receipt is referred to as the tender notification by `18-TenderWithdrawal.xml` (PWD/2026/0348), and precedes that withdrawal (2026-02-23).
- Receiver Brackenmere Furniture is described as in its other examples (register ID 20412466, GLN 9523710900008, which passes `check_ids.py`); the sender is the department's procurement office.

## Considered and refuted
- `/TenderReceipt/cbc:CustomizationID` = `urn:ubl-examples:world:trns:tender:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0`: the customization of the tender in a tender receipt — refuted because the flow names a customization per exchange, used by all its documents (counted over the tender flow's `*.xml`: expression-of-interest, qualification-application, procurement-status, unsubscribe-from-procedure and tenderer-qualification each serve request and response), and `16-TenderReceipt.xml` and `18-TenderWithdrawal.xml` use the same one.
- No reference to the call for tenders — refuted: the contract folder ID identifies the procedure, and the tender referred to carries the call reference.
