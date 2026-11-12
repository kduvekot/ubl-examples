# LLM review: 08-Reminder.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/08-Reminder.xml`, Git blob `e24bac5879420244e021d7b208594e7ca88f789d` (committed)
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

## Checked and consistent
- Reference: `ReminderLine[1]` refers to KG-INV-26-0157 of 2026-04-03, which is `06-Invoice.xml` (an Invoice of Kelpstone Gas to Montebrio Power, issued 2026-04-03, due 2026-05-03, for March's gas, as the note says).
- Dates: the reminder period 2026-05-04 → 2026-06-03 starts the day after the invoice's due date and equals the invoice's penalty period (start 2026-05-04, one month); issued 2026-06-03 09:46 at its end; the new due date 2026-06-10 is after the issue date and before the remittance in `09-RemittanceAdvice.xml` (2026-06-06).
- Text against structure: "a month overdue" agrees with the period of one month; line 1 note "due 2026-05-03" agrees with `06-Invoice.xml`.
- `check_ids.py`: the payee account check digits OK.

## Considered and refuted
- `/Reminder/cac:ReminderLine[2]`: suspected that the surcharge line should refer to the invoice it is charged on — refuted because the reminder concerns one invoice only, and the line's note and percentage tie it to line 1; `09-RemittanceAdvice.xml` refers to this reminder for the surcharge.
