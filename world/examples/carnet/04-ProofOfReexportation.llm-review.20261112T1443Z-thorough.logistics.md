# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: logistics

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

## Findings

### carnet/04#F1 · Medium · The proof cannot be linked to the carnet or to the request it answers
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: A proof of re-exportation is useful only if the importing guarantor can match it to the carnet and the claim. The counterfoil ID "REIMP-1" is unique only within one carnet, and its `GoodsItemPassportID` ("The identifier of the Goods Item Passport or ATA Carnet of this counterfoil") is not given; the carnet number appears only in free text inside the attachment. The document also does not reference the request it answers (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:ID` = `SCC-DOC-26-0726`) or the reminder; its only reference (XU-CUS-REIMP-26-0044) occurs in no other example. ProofOfReexportation has no dedicated request reference, but AdditionalDocumentReference can carry it.
- Condition: `GoodsItemPassportCounterfoil/cbc:GoodsItemPassportID` = `FCC-DOC-26-0724`, and the document references the request SCC-DOC-26-0726 (and, optionally, the reminder).
- Options: (a) preferred: add the carnet ID on the counterfoil and an AdditionalDocumentReference to SCC-DOC-26-0726 with a DocumentType; (b) at least the carnet ID, if the request is to stay unreferenced.
- Needs decision: no

### carnet/04#F2 · Low · Counterfoil, evidence and attachment name different counterfoils
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:ReexportationEvidence/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: The document lists only the re-importation counterfoil (REIMP-1) as "associated with this proof", but the attachment is the re-exportation counterfoil (REEXP-1), which is not listed. The evidence ID re-uses the counterfoil ID, so the evidence and the counterfoil cannot be told apart, and the attachment is not described as evidence at all. Both are valid ATA evidence (own knowledge: re-importation into the home country and the stamped re-export counterfoil are both accepted), so the document should state both consistently.
- Condition: every counterfoil the proof relies on (REIMP-1 and REEXP-1) is listed as a counterfoil and as evidence, each with its own evidence identifier.
- Options: (a) preferred: add REEXP-1 as a second counterfoil and a second ReexportationEvidence, with evidence IDs of their own; (b) keep only the re-importation evidence and drop the attachment.
- Needs decision: no

### carnet/04#F3 · Low · Re-importation document identified differently from the carnet, and no date
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cac:ReimportationDocumentReference/cbc:ID` = `REIMP-1-STAMP`
- XPath: `/ProofOfReexportation/cbc:Note[2]` = `The samples came home on the date stamped.`
- Why: The re-importation by Urvania's customs is referenced here as XU-CUS-REIMP-26-0044 and in the carnet as REIMP-1-STAMP; neither reference has a DocumentType, so the two cannot be recognised as the same document. The note refers to "the date stamped" but no date of re-importation (or re-exportation) is given anywhere in the flow, although the date is what decides whether the proof meets the time limit. The counterfoil has no date element, but the evidence description or the document reference (IssueDate) can carry it.
- Condition: the same re-importation document has the same ID in 01 and 04 and says what it is; the date of re-importation is stated.
- Options: (a) preferred: give the reference an IssueDate and DocumentType and use the same ID in 01; (b) put the date in the evidence description.
- Needs decision: no

## Checked and consistent
- Dates: proof 2026-08-28 13:19, after the reminder (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cbc:IssueDate` = `2026-08-23`) and before its due date 2026-09-22, so it arrives in time.
- The re-importation counterfoil REIMP-1 exists in the carnet (`01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[4]/cbc:ID` = `REIMP-1`), stamped at the Urvanian land border, which fits "stamped by Urvania's customs" in the evidence.
- Attachment: `application/pdf` with an `.example` URI.

## Considered and refuted
- `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument`: suspected contradiction with the request's note that no re-export stamp was found — refuted as a finding of this example: the holder's stamped counterfoil is exactly the evidence that answers a missing customs record; the wording issue lies in 02 (carnet/02#F2).

## Outside this review
- Whether the re-importation date fits the transport legs of the samples (timeline across documents).
