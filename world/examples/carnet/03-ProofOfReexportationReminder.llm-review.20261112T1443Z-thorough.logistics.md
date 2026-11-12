# LLM review: 03-ProofOfReexportationReminder.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/03-ProofOfReexportationReminder.xml`, Git blob `a4b75fb8a0fa66ce587c269390e36886f30cf151` (committed)
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

## Findings

### carnet/03#F1 · Medium · Duties claimed before the re-exportation time limit has expired
- XPath: `/ProofOfReexportationReminder/cbc:IssueDate` = `2026-08-23`
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-09-22`
- XPath: `/ProofOfReexportationReminder/cbc:Note[2]` = `Without proof, the import duties will be claimed from the guarantee.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- Why: The reminder threatens to claim the duties from the guarantee by 2026-09-22, but the carnet it refers to (`GoodsItemPassportID` FCC-DOC-26-0724) still allows re-exportation until 2026-11-21. Under the ATA Convention (own knowledge) duties become claimable only after the re-exportation time limit has passed without discharge; on 2026-09-22 the goods would still be within their lawful admission period. Same root as carnet/02#F1.
- Condition: the claim date (and the reminder) lie after the carnet's final re-exportation date for the importation counterfoil.
- Options: (a) preferred: shorten the carnet's final re-exportation date so it has passed before 2026-07-24 (see carnet/02#F1); (b) move the reminder and its due date after 2026-11-21.
- Needs decision: yes

### carnet/03#F2 · Low · Customs reference with only an ID
- XPath: `/ProofOfReexportationReminder/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: As in the request (02), the reference has no DocumentType and appears in no other example except 02, so it is not clear what it is.
- Condition: the reference says what kind of document it is.
- Options: add a DocumentType; or drop it if the request reference already covers it.
- Needs decision: no

## Checked and consistent
- `/ProofOfReexportationReminder/cac:ProofOfReexportationRequestDocumentReference/cbc:ID` = `SCC-DOC-26-0726` resolves to carnet/02, a ProofOfReexportationRequest; same carnet ID and same counterfoil `IMP-1` (`/ProofOfReexportationReminder/cac:GoodsItemPassportCounterfoil/cbc:ID` = `IMP-1`).
- Dates: reminder 2026-08-23, 30 days after the request of 2026-07-24; due date 2026-09-22 = 2026-08-23 + 30 days, matching "within 30 days" in the payment terms note.
- The counterfoil carries no own GoodsItemPassportID; the document-level `GoodsItemPassportID` covers it ("used when all counterfoils refer to the same").

## Considered and refuted
- `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:DocumentID`: suspected wrong ID (the request's ID, not the reminder's) — refuted because the definition in this document is "An Issuers endorsment of this Request for Proof of Reexportation", so the request ID is a legitimate reading.
- `/ProofOfReexportationReminder/cbc:ProcedureCode`: 2000 "Temporary admission, no previous procedure" fits the procedure of the goods on the island.
