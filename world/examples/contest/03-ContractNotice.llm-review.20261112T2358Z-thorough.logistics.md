# LLM review: 03-ContractNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/03-ContractNotice.xml`, Git blob `7954b4a6494a5104f6b223a28caf36da90fc85ff` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 219a684 2026-11-12 Reviews of the road flow, run 20261112T2311Z-thorough: merge complete
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

### contest/03#F1 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/ContractNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this ContractNotice is a procurement document of a design
  contest for a service: nothing is imported, declared or transported, and no receiver of the
  document uses a customs number. It looks copied from the party's master data (the same value occurs
  in 55 examples, counted with `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`,
  all 16 of this flow among them).
- Condition: every identifier carried for a party in this document is one the document or its
  receiver uses (no customs trader number in a procurement document of a services contest), or the document states why it is needed.
- Options: (a) preferred: leave the customs trader identification out of the procurement documents
  (keep it in the customs documents of the tender flow); (b) keep it only if the world gives the
  contest a customs reason (none is visible).
- Needs decision: no

## Checked and consistent
- Reference: `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633` resolves to the prior information notice (01, 02), a notice of the same process (same ContractFolderID), which is what NoticeDocumentReference means.
- Dates against the issue time: `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-04-18` and `/ContractNotice/cac:TenderingProcess/cac:TenderSubmissionDeadlinePeriod/cbc:EndDate` = `2026-06-12` lie after the issue date and in that order; the requests to participate (06, 11: 2026-04-01 and 2026-04-13) arrive before the participation deadline, the award (`15-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-06-28`) after the submission deadline.
- Quantities: `/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2` with DurationMeasure 5 ANN matches its Description (two designs in the last five years); short list Minimum 3 / Expected 5 / Maximum 5 matches "three to five selected participants" in TenderingProcess/Description.
- Codes: NoticeTypeCode CN, ProcedureCode DESIGNCONTEST, SubmissionMethodCode ELECTRONIC, PreviousCancellationReasonCode UNSUITABLE (fits the cancelled 2025 contest with unacceptable designs), EvaluationCriterionTypeCode REFERENCES, EconomicOperatorRoleCode LEAD, CompanyLegalFormCode LTD, ISIC 8423 for the review board.
- Appeal receiver: the Procurement Review Board (register 20410822, address LUM-ADR-075593) is described identically in 03, 04, 08 and 09.
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/ContractNotice/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`: suspected that a reference by ID alone is ambiguous because two versions of the referenced document exist (01 and 02) — refuted because the versions share one document ID by design (VersionID/PreviousVersionID), a reference by document ID addresses the document, and the issue dates make the intended version unambiguous (the notice refers to the PIN published before it; version 2 of 2026-02-23 is the current one).
- `/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-04-18`: suspected that a deadline without EndTime is incomplete — refuted: a date-only deadline is a legitimate reading (end of that day); the submission deadline, where the hour matters for the anonymous judging, does carry `12:00:00`.
- `/ContractNotice/cbc:ID` = `LPWD-DOC-26-0634`: suspected that document numbers running consecutively across three senders (LPWD-DOC-26-0633 … BF-DOC-26-0637, BF-DOC-26-0638, BIS-DOC-26-0639, LPWD-DOC-26-0640) imply one shared counter — refuted: each number carries its sender's prefix, is unique over `*.xml` (`grep -rl --include='*.xml'` finds each only in this flow) and nothing in UBL requires gaps; the same numbering style runs through the whole world (e.g. `tender/*.xml`).
