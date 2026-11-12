# LLM review: 02-ProofOfReexportationRequest.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: context

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

### carnet/02#F1 · Low · "No re-export stamp" against a carnet that shows the re-exportation counterfoil stamped
- XPath: `/ProofOfReexportationRequest/cbc:Note[2]` = `The island's customs found no re-export stamp.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[3]/cbc:Note` = `Stamped by customs.`
- XPath: `04-ProofOfReexportation.xml:/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: The request's reason is that the island's customs "found no re-export stamp", while the carnet lists the re-exportation counterfoil `REEXP-1` at Selanu airport as stamped, and the proof later attaches exactly that counterfoil stamped by the Island Customs Service. Under the ATA procedure (own knowledge) the two can be reconciled: the customs stamp the counterfoil that stays in the carnet and detach the voucher for their own file; when the voucher does not reach the importation office's records, that office claims and the holder proves re-exportation with the stamped counterfoil. The note, however, says the stamp was not found, not that the voucher is missing, and the request is the document whose reason the reader relies on. Whether this is a contradiction or a loose wording could not be settled.
- Condition: The request's stated reason agrees with what the carnet and the proof say about the re-exportation counterfoil and voucher (e.g. "no re-exportation voucher on file" if the counterfoil was stamped).
- Options: (a, preferred) reword the note to the missing voucher/discharge record, which keeps the story; (b) if the stamp was really missing, the carnet (01, see carnet/01#F1) and the attachment in 04 must not show it stamped.
- Needs decision: yes

### carnet/02#F2 · Low · Additional document reference without saying what it is
- XPath: `/ProofOfReexportationRequest/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: The reference carries only an ID; nothing says what the document is (from the ID, presumably the island customs' claim or non-discharge notice that triggers the request). It is the one document the request rests on, and no example of the flow has it as document ID.
- Condition: The reference says what kind of document it is (DocumentTypeCode or DocumentType) and, where useful, who issued it.
- Options: (a, preferred) add DocumentType (and the issuing customs office as IssuerParty); (b) remove it.
- Needs decision: no

## Checked and consistent
- `GoodsItemPassportID` `FCC-DOC-26-0724` is the document ID of 01; `GoodsItemPassportCounterfoilID` `IMP-1` is the importation counterfoil of 01 (Counterfoil[2]), which is the counterfoil the importing country needs discharged: the right one to name.
- Parties: the Selanu chamber as ImportingGuarantorParty sends the request to the Ferrano chamber as ExportingGuarantorParty ("fiscally responsible for the counterfoils"), on behalf of the Island Customs Service as ImportingCustomsParty ("who originally requests the Proof"); the same parties as in 01.
- Issue date 2026-07-24 is after the importation at the fair and before the final re-exportation date of 01 (2026-11-21).

## Considered and refuted
- `/ProofOfReexportationRequest/cbc:VersionID`: suspected filler — refuted because the definition "the current version of this request for proof" fits this document exactly, and the reminder in 03 refers back to this version.
- `/ProofOfReexportationRequest/cac:Signature/cbc:ID`: suspected a signature without a reason — refuted because a guarantor's claim is a formal act that is signed in the ATA chain.
