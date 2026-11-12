# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/04-ProofOfReexportation.xml`, Git blob `8c48bdf6e2b8e4826241a1f283bf58fe44ebe304` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
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
- The proof is issued on `/ProofOfReexportation/cbc:IssueDate` = `2026-08-28`, before the due date of the claim in `03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-09-22`, so the duties of the reminder do not become payable and the flow rightly has no invoice or payment after it.

## Considered and refuted
- `/ProofOfReexportation`: suspected that the proof should say that the claim of 1,300 coral (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`) is withdrawn — refuted because the reminder makes the claim conditional on no proof arriving in time; a proof within the period ends it by itself, and the UBL document has no element for a withdrawn amount.
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`: suspected a tax registration the proof does nothing with — not a money question here (no tax is charged or reported by this document); left to the parties lens.
