# LLM review: 03-DigitalAgreement.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/03-DigitalAgreement.xml`, Git blob `2af11a686be2a4eb3d82b639256ce234b6e7bcf7` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### sea/03#F1 · High · Signature validated before the agreement and its terms were issued
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationDate` = `2026-05-05`
- XPath: `/DigitalAgreement/cac:Signature/cbc:ValidationTime` = `09:05:00`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:IssueTime` = `12:00:00`
- XPath: `/DigitalAgreement/cbc:IssueTime` = `12:59:00`
- Why: `ValidationDate`/`ValidationTime` are "The date upon which this signature was verified" and the time of it. The signature is the agreement's own approval signature (`ReasonCode` `APPROVAL`), yet it was verified at 09:05, three hours before the terms it approves were issued (12:00, verified 12:05 by the same validator `LTAC-VALIDATOR`) and four hours before the agreement itself (12:59). A signature on version 1.0 of the agreement cannot be verified before the terms version 1.0 exist.
- Condition: the signature's validation time lies after the issue of the terms document and is consistent with the agreement's issue time.
- Options: move the validation after 12:05 (e.g. just before or at the issue at 12:59) (preferred: keeps the order terms → verification of terms → signature → issue); or, if the signature belongs to an earlier draft, say so through the signed document reference (see F2) and date the terms accordingly.
- Needs decision: no

### sea/03#F2 · Low · Signed document reference does not identify the agreement
- XPath: `/DigitalAgreement/cac:Signature/cac:OriginalDocumentReference/cbc:ID` = `LD-DOC-26-DA-1`
- Why: `OriginalDocumentReference` is "A reference to the document that the signature applies to". The ID matches neither this agreement (`LD-DAG-26-0125`) nor any example of the flow (`flow_index.py sea` resolves it to `?`), and the reference has no type, version or description, so it is not clear what was signed (the agreement image, a draft 0.9, the terms?).
- Condition: the reference identifies the signed document so that it can be matched (this agreement and its version, or a described image of it).
- Options: use the agreement's ID with `VersionID` 1.0 (preferred: the signature then demonstrably covers this document); or keep a separate image ID and describe it (`DocumentDescription`, attachment).
- Needs decision: no

### sea/03#F3 · Low · XPath of the terms reference does not resolve as written
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cbc:XPath` = "/DigitalAgreement/DigitalAgreementTerms" (quoted without backticks, as the value is itself a path)
- Why: `XPath` is "An unambiguous location within the bounding document or the document referenced by the parent DocumentReference, expressed as an XPath". The referenced document is a PDF/text attachment, in which an XPath has no meaning; in the bounding document the element is `cac:DigitalAgreementTerms` in the UBL namespace, so the path without prefixes selects nothing. The reference also carries `ReferencedDocumentInternalAddress` `section-2`, a second, different pointer.
- Condition: the XPath, if kept, selects the intended element in the document it applies to, and does not compete with the internal address.
- Options: drop the XPath and keep `section-2` as the location inside the terms (preferred: the terms are not XML); or give a namespace-qualified path into this agreement.
- Needs decision: no

### sea/03#F4 · Low · Link to the terms expires a day before the terms do
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cac:ExternalReference/cbc:ExpiryDate` = `2027-05-04`
- XPath: `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`
- Why: the external reference expires on 2027-05-04 at 23:59 while the terms, and the agreement terms (`/DigitalAgreement/cac:DigitalAgreementTerms/cac:ValidityPeriod/cbc:EndDate` = `2027-05-05`), remain valid until 2027-05-05. On the last day of the agreement the full terms would no longer be reachable.
- Condition: the external reference stays available at least until the end of the terms' validity.
- Options: expiry on 2027-05-05 (or later) (preferred); or end the validity periods on 2027-05-04.
- Needs decision: no

## Checked and consistent
- The agreement's digital processes match the documents of the flow: ordering with profile `urn:ubl-examples:world:profile:ordering:1.0` and customization `urn:ubl-examples:world:trns:order:1.0`, as in `05-Order.xml`; billing with `urn:ubl-examples:world:profile:billing:1.0` and `urn:ubl-examples:world:trns:billing:1.0`, as in `22-Invoice.xml`. The endpoint IDs `XL:IC41859` and `XB:20410274` agree with the parties' electronic addresses in `01-BusinessCard.xml`.
- The agreement is referenced as the contract by `06-OrderResponse.xml:/OrderResponse/cac:Contract/cbc:ID` = `LD-DAG-26-0125`; the order (2026-05-07) and order response (2026-05-08) fall inside the adoption period (2026-05-05 to 2026-05-19).
- Version 1.0 with previous version 0.9; validity of one year from the issue date; terms verified at 12:05 after their issue at 12:00.

## Considered and refuted
- `/DigitalAgreement/cac:RequiredCertificationDocumentReference/cac:Attachment/cbc:EmbeddedDocumentBinaryObject` (text/plain) next to an external PDF in the same attachment: suspected two different documents in one attachment — refuted as outside this lens's concern for references: both carry the same terms (the embedded text names "version 1.0"), and the external reference has its own hash.
