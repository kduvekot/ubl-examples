# LLM review: 11-QualificationApplicationResponse.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/11-QualificationApplicationResponse.xml`, Git blob `786906485480cbed630ad927abbdceded6391e3d` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
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

### contest/11#F1 · Medium · The two weighted reference criteria of the request are not answered
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF`
- XPath: `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ID` = `CRR-PROF`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`
- XPath: `10-QualificationApplicationRequest.xml:/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`
- Why: a Qualification Application Response is "a self-declaration of an economic operator, stating
  that it does not fall under the Exclusion Grounds and that it meets the Selection Criteria"; its
  TenderingCriterion is "the criterion as described in the Qualification Application Request". The
  request (10-QualificationApplicationRequest.xml) asks three criteria; the response repeats and answers only CR-PROF (pass/fail).
  The two criteria that carry the whole weighted score (CR-REF-PUBLIC 60, CR-REF-COAST 40, property
  IDs P-REF-PUBLIC-1 and P-REF-COAST-1), and on which the jury selects the participants
  ("The jury selects the participants on their references" in the contract notice), are neither
  repeated nor answered. The tenderer qualification (12-TendererQualification.xml) does not fill the gap: it lists one
  completed task, not the two references asked for, and nothing about a coastal site.
- Condition: the response contains a TenderingCriterionResponse for every property of the request
  (P-PROF-1, P-REF-PUBLIC-1, P-REF-COAST-1), each validating the property ID it answers, or states
  why a criterion is not answered.
- Options: (a) preferred: add the two criteria and responses with the two references (project,
  client, year, what the team designed), one of them on a coastal site, consistent with the
  completed tasks of 12-TendererQualification.xml; (b) if the story wants an incomplete response, make that visible (a
  ResponseCode NOTMET or a note) and let a later document deal with it.
- Needs decision: no

### contest/11#F2 · Low · The response does not refer to the request it answers
- XPath: `/QualificationApplicationResponse/cbc:ID` = `BF-DOC-26-0637`
- Why: the response answers the request `LPWD-DOC-26-0636` (10-QualificationApplicationRequest.xml) and repeats its criterion and
  property IDs, but it carries no AdditionalDocumentReference to that request; the request exists in
  two versions with different design-lead requirements, so which one is answered can only be guessed
  from the issue dates. The link is only implicit, through ContractFolderID.
- Condition: the response identifies the request (ID LPWD-DOC-26-0636, and the version where it
  matters) that it answers.
- Options: (a) preferred: an AdditionalDocumentReference to LPWD-DOC-26-0636 with its VersionID;
  (b) leave it implicit through ContractFolderID.
- Needs decision: no

### contest/11#F3 · Low · The evidence is not linked to the response it supports
- XPath: `/QualificationApplicationResponse/cac:Evidence/cbc:ID` = `EV-REG-LEAD`
- Why: the document-level Evidence is "the evidence supporting this criterion requirement response",
  and the link from a response to its evidence is TenderingCriterionResponse/SuppliedEvidence (UBL
  2.5; the older EvidenceSupplied is deprecated). The response CRR-PROF carries no such link, so the
  identifier EV-REG-LEAD is referred to by nothing and the certificate is tied to the registration
  claim only by its name.
- Condition: the response that the certificate supports refers to the evidence EV-REG-LEAD.
- Options: (a) preferred: add SuppliedEvidence with ID EV-REG-LEAD to the TenderingCriterionResponse
  CRR-PROF; (b) drop the evidence ID if the evidence is meant to stand alone (weaker).
- Needs decision: no

### contest/11#F4 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this QualificationApplicationResponse is a procurement document of a design
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
- References that resolve: `/QualificationApplicationResponse/cac:TenderingCriterion/cbc:ID` = `CR-PROF` and `/QualificationApplicationResponse/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `P-PROF-1` exist in the request (10-QualificationApplicationRequest.xml).
- The answer fits the requirement in force: a registered industrial designer, allowed since CN v2 / QAR v2 (08, 10); ResponseCode MET fits; EvidenceTypeCode CERTIFICATE fits a certificate of registration.
- Dates: issued 2026-04-13, before the participation deadline (2026-05-02) and after the request.
- Version chain: VersionID 2, PreviousVersionID 1, same ID BF-DOC-26-0637 as 06.
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`: suspected that a group name without the second member as EconomicOperatorParty is an unresolved reference — refuted for this lens: the group's members are identified in the tenderer qualification (12-TendererQualification.xml: Brackenmere 20412466 and Saltmere Engineering 20410685); whether each member must also send its own response is a question of the parties lens.
