# LLM review: 05-QualificationApplicationRequest.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/05-QualificationApplicationRequest.xml`, Git blob `28d9b7bf1f028e6d60a3a976a753b0913f3d8eed` (committed)
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

### contest/05#F1 · Low · The request does not identify the contest notice whose criteria it implements
- XPath: `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:Description` = `The two completed designs of furniture or fittings for public spaces in the last five years that the contest notice asks for.`
- Why: a Qualification Application Request defines "how the Exclusion Grounds and the Selection
  Criteria should be addressed … for a specific procurement". Its criteria repeat the requirements of
  the contract notice (03-ContractNotice.xml) and the text points to "the contest notice", but the document
  carries no AdditionalDocumentReference to that notice (`LPWD-DOC-26-0634`); the procurement is
  identified only by ContractFolderID and ContractName. Since the notice exists in two versions with
  different requirements for the design lead, the reference is the way to tie the request to the
  notice it implements.
- Condition: the request refers to the contract notice LPWD-DOC-26-0634 it implements.
- Options: (a) preferred: an AdditionalDocumentReference with ID LPWD-DOC-26-0634 and a
  DocumentTypeCode or DocumentType saying it is the contract notice (as ESPD requests refer to the
  notice); (b) leave it implicit through ContractFolderID and drop the textual pointer.
- Needs decision: no

### contest/05#F2 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/QualificationApplicationRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this QualificationApplicationRequest is a procurement document of a design
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
- Criterion structure: three criteria with unique IDs (`/QualificationApplicationRequest/cac:TenderingCriterion[1]/cbc:ID` = `CR-PROF`, `/QualificationApplicationRequest/cac:TenderingCriterion[2]/cbc:ID` = `CR-REF-PUBLIC`, `/QualificationApplicationRequest/cac:TenderingCriterion[3]/cbc:ID` = `CR-REF-COAST`), each with one property group and property with unique IDs; the response (06) refers to CR-PROF and P-PROF-1, which resolve here.
- Weights: WeightNumeric 60 and 40 add up to 100 and match WeightScoringMethodologyNote (pass/fail for the lead, references weighted 60 and 40).
- CR-REF-PUBLIC agrees with the contract notice's TechnicalEvaluationCriterion (two designs, five years); CR-PROF agrees with the design-lead requirement of the notice version in force (architect, CN v1).
- Codes: ProcedureCode DESIGNCONTEST, QualificationApplicationTypeCode REGULATED, WeightingTypeCode WEIGHTED, CriterionTypeCode SUITABILITY / TECHNICAL, EvaluationMethodTypeCode PASSFAIL / WEIGHTED, PropertyGroupTypeCode ON, TypeCode QUESTION, ValueDataTypeCode DESCRIPTION — each from the list its listID names, and the meaning fits the element.
- `/QualificationApplicationRequest/cbc:IssueDate` = `2026-03-20` follows the contract notice (2026-03-19).
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/QualificationApplicationRequest/cbc:CustomizationID` = `urn:ubl-examples:world:trns:qualification-application:1.0#compliant#urn:ubl-examples:world:community:procurement:1.0`: suspected that request and response should not share one customization ID — refuted: the world uses one customization per document pair throughout (billing, order-status, tender …, counted over `*.xml`), which CustomizationID allows.
