# LLM review: 04-ProofOfReexportation.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: context

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

### carnet/04#F1 · Medium · The proof does not identify the carnet or the claim in structured form
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- Why: A counterfoil ID such as `REIMP-1` is only unique within one carnet; GoodsItemPassportCounterfoil has a GoodsItemPassportID element for the carnet number ("The identifier of the Goods Item Passport or ATA Carnet of this counterfoil"), and it is empty here, so the carnet `FCC-DOC-26-0724` of 01 is named only in free text inside the attachment. Nor does the proof refer to the request it answers (`02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:ID` = `SCC-DOC-26-0726`) or the reminder (`03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cbc:ID` = `SCC-DOC-26-0727`); its only document reference is a customs record that no example has. The Selanu chamber and the island customs, who must close the claim against the guarantee, cannot link the proof to the carnet and the claim from the structured data, and the proof's purpose depends on that link.
- Condition: The proof identifies the carnet in a structured element (the counterfoil's GoodsItemPassportID) and refers to the request (and reminder) it answers.
- Options: (a, preferred) add GoodsItemPassportID `FCC-DOC-26-0724` to the counterfoil and AdditionalDocumentReferences to 02 and 03 with their document type; (b) at least the GoodsItemPassportID.
- Needs decision: no

### carnet/04#F2 · Medium · No date of re-exportation, though the note relies on it
- XPath: `/ProofOfReexportation/cbc:Note[2]` = `The samples came home on the date stamped.`
- Why: Proof of re-exportation has to show that the goods left the country of temporary admission, and within the time limit (01 sets `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`). The note refers to "the date stamped", but no date appears anywhere in the document: not on the counterfoil, the evidence or the attachment. The structured data cannot show the re-exportation was in time, which is what the importing guarantor needs to release the guarantee.
- Condition: The proof states the date of re-exportation (or of re-importation, as evidence for it) in a structured element or at least in the evidence description, and the note refers to a date that is in the document.
- Options: (a, preferred) put the date in the ReexportationEvidence (e.g. its description, or an evidence document reference with IssueDate) and keep the note; (b) put the date in the note itself.
- Needs decision: no

### carnet/04#F3 · Low · Attachment text describes the attachment instead of containing it
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: EmbeddedDocument is "A clear text object containing an attached document". The value is a sentence about the scanned counterfoil, which itself is referenced as a PDF (`/ProofOfReexportation/cac:GoodsItemPassportAttachment/cac:ExternalReference/cbc:URI` = `https://www.ferrano-chamber.example/ata/carnet-scan.pdf`); it does not contain the document. A description of an attachment belongs in a description element.
- Condition: EmbeddedDocument, if present, contains the attached document (its clear text); a description of the attachment is in a description element or the Note.
- Options: (a, preferred) remove EmbeddedDocument and describe the scan in the ExternalReference's Description; (b) keep only the external reference.
- Needs decision: no

### carnet/04#F4 · Low · Counterfoil named is not the one claimed, and the attached one is not named
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `REIMP-1`
- XPath: `02-ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:GoodsItemPassportCounterfoilID` = `IMP-1`
- XPath: `/ProofOfReexportation/cac:GoodsItemPassportAttachment/cbc:EmbeddedDocument` = `Re-exportation counterfoil of carnet FCC-DOC-26-0724, stamped by the Island Customs Service: all items re-exported.`
- Why: The request and the reminder concern the importation counterfoil `IMP-1`; the proof's GoodsItemPassportCounterfoil ("counterfoils associated with this proof") names only the re-importation counterfoil `REIMP-1`, while its attachment is the re-exportation counterfoil `REEXP-1`, which is not named. Both counterfoils are valid evidence under the ATA rules (own knowledge), but the document links neither to the claimed `IMP-1` nor lists the counterfoil it attaches.
- Condition: The counterfoils the proof lists include the claimed counterfoil and every counterfoil it brings as evidence (or attaches).
- Options: (a, preferred) list `IMP-1` (the claim) and `REEXP-1` and `REIMP-1` (the evidence); (b) keep one evidence counterfoil and attach that one, so text and structure agree.
- Needs decision: yes

### carnet/04#F5 · Low · Additional document reference without saying what it is
- XPath: `/ProofOfReexportation/cac:AdditionalDocumentReference/cbc:ID` = `XU-CUS-REIMP-26-0044`
- Why: Only an ID; nothing says what the document is (from the ID, the Urvanian customs' re-importation record). No example of the flow has it.
- Condition: The reference says what kind of document it is, or is removed.
- Options: (a, preferred) add DocumentType and issuer; (b) remove it.
- Needs decision: no

## Checked and consistent
- ReexportationEvidence: a re-importation counterfoil stamped by the customs of the exporting country is accepted proof of re-exportation in the ATA system (Istanbul Convention, Annex A; own knowledge); the evidence description says so.
- Sender and signatory are the Ferrano chamber (exporting guarantor), the party that collects the proof from its holder and sends it to the claiming chamber; ExportingCustomsParty is the Urvanian customs that stamped the re-importation; all as in 01.
- Issue date 2026-08-28 is five days after the reminder (2026-08-23) and within its 30-day period.

## Considered and refuted
- `/ProofOfReexportation/cac:ExportingCustomsParty/cac:PartyName/cbc:Name`: suspected a party the proof does nothing with — refuted because this customs administration stamped the re-importation counterfoil that serves as evidence.
