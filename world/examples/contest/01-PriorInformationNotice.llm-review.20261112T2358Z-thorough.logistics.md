# LLM review: 01-PriorInformationNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/01-PriorInformationNotice.xml`, Git blob `eabac2882841f25d8b6985b6d92b45b2d3caf81b` (committed)
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

### contest/01#F1 · Low · Customs and logistics master data the procurement document does nothing with
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
- `/PriorInformationNotice/cbc:PlannedDate` = `2026-03-04` (planned publication of the contract notice) lies after the issue date 2026-02-02; it is moved to 2026-03-19 by version 2 (`02-PriorInformationNotice.xml:/PriorInformationNotice/cbc:PlannedDate` = `2026-03-19`), on which the contract notice is indeed issued (`03-ContractNotice.xml:/ContractNotice/cbc:IssueDate` = `2026-03-19`).
- Document identity: `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0633` with `/PriorInformationNotice/cbc:VersionID` = `1`; version 2 (02) keeps the ID and carries PreviousVersionID 1; ContractFolderID `PWD-2026-PROM-DC` and ProfileExecutionID `CONTEST-2026-01` are the same in all 16 examples of the flow.
- Codes against their lists and elements: NoticeTypeCode PIN, ProcedureCode DESIGNCONTEST, ProcurementTypeCode SERVICES, PrizeRankCode FIRST/SECOND/THIRD, ISIC 8411 for public administration, UN CPC 83912 (industrial design services) for a bench design contest, EDED 5153 STT, ISO 4217-style XBL (fictional, not in ISO 4217).
- Party identifiers: register numbers 20410548 (Public Works Department) and 20410959 (Bayvarra Information Service) equal their PartyLegalEntity CompanyID and their endpoint IDs XB:20410548 / XB:20410959, and are the same in every example of the flow; address IDs LUM-ADR-000417 / LUM-ADR-634627 likewise.
- Short list: MinimumQuantity 3 and MaximumQuantity 5, consistent with the contract notice (three to five selected participants).
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/PriorInformationNotice/cac:ProcurementProject/cac:RealizedLocation/cbc:Name` = `Harbour promenade, Lumeport`: suspected a missing location identifier, since Lumeport has the UN/LOCODE XBLMP in other flows — refuted: the location is a promenade, a part of the town, which the city's LOCODE does not identify; no other example identifies the promenade itself.
- `/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0633`: suspected that document numbers running consecutively across three senders (LPWD-DOC-26-0633 … BF-DOC-26-0637, BF-DOC-26-0638, BIS-DOC-26-0639, LPWD-DOC-26-0640) imply one shared counter — refuted: each number carries its sender's prefix, is unique over `*.xml` (`grep -rl --include='*.xml'` finds each only in this flow) and nothing in UBL requires gaps; the same numbering style runs through the whole world (e.g. `tender/*.xml`).
- Telephone numbers with country code +999: suspected a real ITU code — refuted: +999 is not assigned to any country (ITU reserves it), so it cannot be mistaken for a real number.
