# LLM review: 02-PriorInformationNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/02-PriorInformationNotice.xml`, Git blob `a3f76e84106ee3bfd01686b7e8ab9a1352366cec` (committed)
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

### contest/02#F1 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this PriorInformationNotice is a procurement document of a design
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
- Version chain: `/PriorInformationNotice/cbc:VersionID` = `2`, `/PriorInformationNotice/cbc:PreviousVersionID` = `1`, same ID `LPWD-DOC-26-0633` as 01, issued later (2026-02-23 against 2026-02-02).
- `/PriorInformationNotice/cbc:PlannedDate` = `2026-03-19` lies after the issue date and equals the issue date of the contract notice (`03-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-03-19`).
- The changed first prize (`/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`) agrees with its PrizeDescription (8,000 lume) and with the contract notice and calls for tenders (`03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`).
- Codes and party identifiers as in 01 (NoticeTypeCode PIN, DESIGNCONTEST, SERVICES, CPC 83912; register numbers 20410548 and 20410959 consistent across the flow).
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/PriorInformationNotice/cac:ProcurementProject/cac:RealizedLocation/cbc:Name` = `Harbour promenade, Lumeport`: suspected a missing location identifier — refuted: the promenade is part of the town and has no identifier anywhere in the world; the town's LOCODE would not identify it.
