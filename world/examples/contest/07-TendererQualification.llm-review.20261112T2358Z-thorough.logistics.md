# LLM review: 07-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/07-TendererQualification.xml`, Git blob `b7c5c10127f35b254eea1a4905b11113ef334e8c` (committed)
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

### contest/07#F1 · Medium · One completed task where the contest asks for two references
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:CompletedTask/cbc:Description` = `Seating for the Lumeport central library's reading garden, 2024.`
- XPath: `03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:TechnicalEvaluationCriterion/cbc:ThresholdQuantity` = `2`
- Why: the tenderer qualification is "a document declaring the qualifications of a tenderer", and in
  a restricted contest whose jury "selects the participants on their references" these
  qualifications are the basis of the selection. The contract notice requires two completed designs
  of furniture or fittings for public spaces in the last five years (ThresholdQuantity 2, Duration 5
  years), and the request weights a second, coastal reference at 40. The team declares one completed
  task (Brackenmere, 2024) and none for the member Saltmere Engineering, so the threshold of 2 is not
  met by what the document declares, and the coastal reference is absent. The response (06-QualificationApplicationResponse.xml) does not
  answer the reference criteria either, so no document of the flow carries the second reference,
  although the team is selected and wins the first prize (15, 16).
- Condition: the team's qualifying parties together declare at least two completed tasks that meet
  the notice's criterion (public-space furniture or fittings, completed within five years), one of
  them on a coastal site, or the flow states why one suffices.
- Options: (a) preferred: add a second CompletedTask (to Brackenmere, or to Saltmere Engineering as
  AdditionalQualifyingParty), with period and description, one of the two near the sea; (b) keep one
  and record that the team was selected despite the threshold (a story change, unlikely).
- Needs decision: no

### contest/07#F2 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this TendererQualification is a procurement document of a design
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
- Participation: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `60` and `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40` add up to 100 %.
- Roles: TendererRoleCode LEAD for Brackenmere and MEMBER for Saltmere Engineering, consistent with the Note and with the contract notice's EconomicOperatorRole LEAD (the group names a lead member).
- Completed task period 2024-03-01 to 2024-09-30 lies within the five years before the issue date and agrees with the year in its description.
- Identifiers: Brackenmere register 20412466 and GLN 9523710900008 (check digit correct), Saltmere Engineering register 20410685 with its endpoint XB:20410685 and address UL-ADR-587295; the department 20410548.
- `/TendererQualification/cbc:IssueDate` = `2026-04-01`, before the participation deadline 2026-04-18.
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:BusinessIdentityEvidenceID` = `20412466`: suspected that the party's register number is not "an identifier for an item of evidence" — refuted: the evidence of business identity is the registration in the federal business register, and its number, with the register's schemeID, is how that evidence is identified and checked (as the extract 13/14 does).
