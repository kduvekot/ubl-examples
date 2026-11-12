# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/02-ProofOfReexportationRequest.xml`, Git blob `a90efbc0c48ac2900e792ec8e07f70218ed57e7c` (committed)
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

### carnet/02#F1 · Medium · Proof of re-exportation requested before the re-exportation time limit
- XPath: `/ProofOfReexportationRequest/cbc:IssueDate` = `2026-07-24`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:ValidityPeriod/cbc:EndDate` = `2027-05-25`
- Why: The request is the start of a claim procedure: the importing guarantor asks for proof because the island's customs have no re-export record. Under the ATA Convention (own knowledge) such a claim can only arise once the time limit for re-exportation has expired without discharge. The referenced carnet (02 names it in `GoodsItemPassportID`) still allows re-exportation until 2026-11-21, almost four months after this request; until then the goods may lawfully remain on the island, so a missing re-export stamp is not yet an irregularity.
- Condition: the request is issued after the final re-exportation date that the carnet records for the importation counterfoil (or the carnet records an earlier final date that has passed by the issue date).
- Options: (a) preferred: give the carnet a final re-exportation date that has passed by 2026-07-24 (a short fair admission, e.g. one month), because the claim story then holds as it is; (b) move the request, reminder and proof after 2026-11-21.
- Needs decision: yes

### carnet/02#F2 · Low · The note says no re-export stamp, while the carnet shows one
- XPath: `/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cac:VoucherDocumentReference/cbc:ID` = `V-REEXP-1`
- Why: The carnet shows the re-exportation counterfoil stamped at "Customs office, Selanu airport" with its voucher V-REEXP-1, i.e. by the same Island Customs Service that, according to this note, found no re-export stamp. In ATA practice the claim concerns a voucher the importing customs did not receive or discharge, not a missing stamp. Read literally, the two documents contradict each other.
- Condition: the note states what the island's customs lack (no discharged re-exportation voucher in their records) in a way that does not contradict the carnet's counterfoil, or the carnet does not show the re-exportation as stamped (see carnet/01#F2).
- Options: (a) preferred: word the note as "no re-exportation voucher was received/discharged", which keeps the story; (b) leave the counterfoil unstamped in 01.
- Needs decision: no

### carnet/02#F3 · Low · Customs reference with only an ID
- XPath: `/ProofOfReexportationRequest/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: The reference has no DocumentType, and no other example carries this ID, so it is not clear what document of the island's customs it is (the claim file, the importation entry, a discharge list). It is also not the importation reference the carnet gives for the same counterfoil (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cac:ImportationDocumentReference/cbc:ID` = `IMP-1-STAMP`).
- Condition: the reference says what it refers to, and where it is the importation document it matches the carnet's reference.
- Options: (a) preferred: add a DocumentType (e.g. "Customs claim file") and use the same importation ID in 01; (b) drop it if it adds nothing.
- Needs decision: no

## Checked and consistent
- `/ProofOfReexportationRequest/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724` resolves to carnet/01; the counterfoil `IMP-1` exists there (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[2]/cbc:ID` = `IMP-1`) and is the right counterfoil for a claim (importation into Lisavu).
- Dates: issued 2026-07-24 08:50, after the carnet (2026-05-25) and within its validity; before the reminder (2026-08-23).
- Same ProfileExecutionID `CARNET-2026-01` as the rest of the flow.

## Considered and refuted
- `/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID`: suspected that the request should point at the re-exportation counterfoil REEXP-1 — refuted because the claim concerns the importation voucher that was not discharged; IMP-1 is correct.
