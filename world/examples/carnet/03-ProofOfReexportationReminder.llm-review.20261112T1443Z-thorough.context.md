# LLM review: 03-ProofOfReexportationReminder.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: context

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

### carnet/03#F1 · Low · Endorsement status "Open" describes the request, not an endorsement
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Open`
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cbc:DocumentID` = `SCC-DOC-26-0726`
- Why: The IssuerEndorsement is "An Issuers endorsment of this Request for Proof of Reexportation", and ApprovalStatus is "The status of this endorsement". "Open" is the status of the pending request (the proof has not arrived), not of an endorsement, which is given or not. The endorsement also carries the request's ID (from 02), not the reminder's, while the endorser is the guaranteeing association that issues the reminder.
- Condition: ApprovalStatus states the status of the endorsement itself (e.g. endorsed, approved), and the open state of the request is said elsewhere (note or not at all, since the reminder's existence already says it).
- Options: (a, preferred) set an endorsement status and leave the request's state to the note; (b) remove the IssuerEndorsement, since the signature already authenticates the reminder.
- Needs decision: no

### carnet/03#F2 · Low · Signatory contact defined for a certificate-of-origin application
- XPath: `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Carnet desk`
- Why: UBL 2.5 defines EndorserParty/SignatoryContact as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party". Here it is the guaranteeing chamber's desk signing a reminder. The value is what the element name suggests, but the definition is copied from the certificate-of-origin context (a model defect, as in carnet/01#F8).
- Condition: The use is either justified and recorded as a finding on the UBL 2.5 definition, or the element is not used.
- Options: (a, preferred) keep it and record the definition for the OASIS UBL TC write-up; (b) drop it.
- Needs decision: yes

### carnet/03#F3 · Low · Additional document reference without saying what it is
- XPath: `/ProofOfReexportationReminder/cac:AdditionalDocumentReference/cbc:ID` = `XL-CUS-ATA-26-0071`
- Why: As in 02, the reference carries only an ID, and nothing says what the referenced document is; no example of the flow has this ID as document ID.
- Condition: The reference says what kind of document it is, or is removed.
- Options: (a, preferred) add DocumentType; (b) remove it, since the reminder refers to the request, which carries it.
- Needs decision: no

## Checked and consistent
- `ProofOfReexportationRequestDocumentReference` `SCC-DOC-26-0726` resolves to 02; GoodsItemPassportID and counterfoil `IMP-1` agree with 02 and 01.
- Issue date 2026-08-23 is 30 days after the request (2026-07-24), a plausible reminder interval.
- PaymentTerms is present for the reason its definition gives ("used for generating a subsequent invoice in case no proof of re-exportation can be provided"), and the note explains it; the due date 2026-09-22 is 30 days after issue, as the note says.
- ProcedureCode `2000` "Temporary admission, no previous procedure" fits the carnet's procedure.

## Considered and refuted
- `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount`: suspected payment data in a non-commercial document — refuted because the element's definition foresees exactly this use (the duties claimed from the guarantee).
- `/ProofOfReexportationReminder/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode`: suspected wrong role (the reminder's issuer is not the carnet's issuer) — refuted because `GUARANTOR` "Guaranteeing association" is the Selanu chamber's role, and the code is not `ISSUER`.
