# LLM review: 09-CallForTenders.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/09-CallForTenders.xml`, Git blob `9f861a12870496547d09c98a4f266718a7a6d679` (committed)
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

### contest/09#F1 · Low · The call for tenders refers to the prior information notice but not to the contract notice it belongs to
- XPath: `/CallForTenders/cac:TenderingProcess/cac:NoticeDocumentReference/cbc:ID` = `LPWD-DOC-26-0633`
- Why: NoticeDocumentReference is "a reference to a notice pertaining to this tendering process". The
  only notice referred to is the prior information notice (01/02), an advance notice that announced
  the contest; the contract notice that actually calls for competition and sets the deadlines and
  qualification requirements this call repeats, `LPWD-DOC-26-0634` (03-ContractNotice.xml and, as version 2, 08-ContractNotice.xml, issued 2026-03-19 and 2026-04-05), is
  not referred to, although it exists before this document. The link from the procurement documents
  to the notice is only implicit, through ContractFolderID.
- Condition: the call for tenders refers to the contract notice LPWD-DOC-26-0634 (with or without the
  prior information notice).
- Options: (a) preferred: add a second NoticeDocumentReference with ID LPWD-DOC-26-0634 (and keep the
  PIN reference, which is also a notice of the process); (b) replace the PIN reference by the
  contract-notice reference.
- Needs decision: no

### contest/09#F2 · Low · The brief and the site plan are referred to by a bare ID only
- XPath: `/CallForTenders/cac:TechnicalDocumentReference/cbc:ID` = `PWD-PROM-BRIEF`
- XPath: `/CallForTenders/cac:ProvidedDocumentReference/cbc:ID` = `PWD-PROM-SITE-PLAN-B`
- Why: the call for tenders is "a document used by a Contracting Party to define a procurement
  project"; its Note (`/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`)
  and the contract notice ("The brief now states both limits") make the brief and the site plan
  the substance of what is defined. The two references carry only an identifier: no DocumentType or
  DocumentTypeCode, no version or issue date, no Attachment or external URI. Neither resolves to
  an example (`flow_index.py` shows `-> ?`), so a participant cannot tell from the document what
  the referenced documents are or where to obtain them. Version 2 replaces SITE-PLAN-A by SITE-PLAN-B without saying what changed (the brief keeps the same ID although it is not said to be unchanged).
- Condition: each of the two references says what the referenced document is (type or description)
  and how it is obtained (attachment or external reference), so that it can be linked to the
  documents it stands for.
- Options: (a) preferred: add DocumentType (e.g. "Design brief", "Site plan") and an
  Attachment/ExternalReference/URI on the buyer profile; (b) at least DocumentType and IssueDate or
  VersionID, so that the change between the versions is traceable.
- Needs decision: no

### contest/09#F3 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/CallForTenders/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this CallForTenders is a procurement document of a design
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
- Deadlines and process data agree with the contract notice of the same date range: submission deadline 2026-06-12 12:00, participation deadline 2026-05-02 (CN v2, 08), short list 3/5/5, prizes 8,000 / 4,000 / 2,000 lume, design-lead requirement architect or industrial designer (08).
- Receiver identifiers: Brackenmere Furniture, register 20412466 (= PartyLegalEntity CompanyID and endpoint XB:20412466), GLN 9523710900008 (check digit correct, `check_ids.py`; GS1 prefix 952 is reserved for demonstrations and examples, so it cannot be mistaken for a real GLN), address UL-ADR-821551; the same in every example of the flow that carries the party.
- Codes: ProcedureCode DESIGNCONTEST, SubmissionMethodCode ELECTRONIC, EvaluationCriterionTypeCode REFERENCES, PrizeRankCode values, CPC 83912, ISIC 3100 for a furniture maker.
- Version chain: `/CallForTenders/cbc:VersionID` = `2`, `/CallForTenders/cbc:PreviousVersionID` = `1`, same ID LPWD-DOC-26-0635 as 04, issued after the contract notice v2 (08, 08:19 the same day).
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/CallForTenders/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: suspected that a restricted contest should send the call only to selected participants, after the requests to participate — refuted: the procurement documents are available from the notice onwards, and the receiver is the operator that obtained them; the selection of participants concerns who may submit designs, not who may read the brief.
- `/CallForTenders/cbc:Note` = `The brief, the site plan and the rules of the contest.`: suspected that "the rules of the contest" lack a reference — refuted: the rules (awarding terms, prizes, jury, appeal, deadlines) are in this document itself.
