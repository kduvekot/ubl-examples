# LLM review: 14-BusinessInformation.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/14-BusinessInformation.xml`, Git blob `ea59d9c8ec70285678a63c9762adc18d4f21b15e` (committed)
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

### contest/14#F1 · Low · A corrected version keeps the subtype "Register extract" although the list has "Correction"
- XPath: `/BusinessInformation/cac:NoticeSubType/cbc:SubTypeCode` = `EXTRACT`
- XPath: `/BusinessInformation/cbc:VersionID` = `2`
- Why: NoticeSubType/SubTypeCode is "a code to specify the Subtype of notice". This document is
  version 2 of the extract BIS-DOC-26-0639 (PreviousVersionID 1) and changes one value of version 1
  (`/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00` against
  `13-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6410000.00`).
  The NoticeSubTypeCode list the listID names has CORRECTION, "a correction of an earlier notice",
  for exactly this; the document keeps EXTRACT and says nowhere (Note, BriefDescription) that it
  corrects version 1, so a receiver sees two extracts with the same ID and different figures.
- Condition: the subtype code, or at least the text, says that this version corrects version 1.
- Options: (a) preferred: SubTypeCode CORRECTION (the version chain already ties it to the extract);
  (b) keep EXTRACT and add a Note naming what was corrected and why.
- Needs decision: no

### contest/14#F2 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this BusinessInformation is a procurement document of a design
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
- Parties: SenderParty Bayvarra Information Service (20410959, the register keeper) sends to the ReceiverParty, the Public Works Department (20410548), an extract about the BusinessParty Brackenmere Furniture (20412466) — the roles fit a register extract asked for by a contracting authority (NoticeSubTypeCode EXTRACT definition).
- `/BusinessInformation/cbc:IssueDate` = `2026-05-09` follows the participation deadline (2026-05-02, CN v2) and precedes the submission deadline: the department checks a candidate at selection.
- Codes: NoticeTypeCode BUSREG (information on an economic operator from a business register), CapabilityTypeCode PRODUCTION for a furniture workshop, ISIC 3100.
- Linking: the document has no ContractFolderID in the UBL 2.5 model; ProfileExecutionID `CONTEST-2026-01` ties it to the collaboration, as its definition intends.
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.
- Version chain: `/BusinessInformation/cbc:VersionID` = `2`, `/BusinessInformation/cbc:PreviousVersionID` = `1`, same ID as 13, issued four days later.

## Considered and refuted
- `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION` with a ValueAmount: suspected that a production capability measured in lume is a turnover in the wrong code — refuted for this lens: ValueAmount is "a monetary amount as a measure of this capability", which an annual production value is; the amount itself is for the money lens.
- No reference from the extract to the request for it or to the procedure: suspected a missing link — refuted: BusinessInformation has no ContractFolderID, and ProfileExecutionID links it to the contest.
