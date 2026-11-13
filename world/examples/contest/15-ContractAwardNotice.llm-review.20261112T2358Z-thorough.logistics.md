# LLM review: 15-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/15-ContractAwardNotice.xml`, Git blob `df753bf00bfa8a999e3e4cf1826906a62184db6d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### contest/15#F1 · High · The first prize is 6,000 lume, against 8,000 in the contract notice it refers to
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`
- XPath: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634`
- XPath: `03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`
- XPath: `08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`
- Why: Prize/ValueAmount is "the monetary value amount of a prize". The award notice refers to the
  contract notice LPWD-DOC-26-0634 (both versions announce a first prize of 8,000 lume, also in
  their PrizeDescription "Three prizes; the first is 8,000 lume.", as do the calls for tenders 04 and
  09), but awards 6,000 lume, the value of the superseded prior information notice v1
  (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`).
  The second prize (4,000) agrees. Version 2 of this notice (16) carries 8,000 without saying it
  corrects anything, which suggests the value here is a mistake that 16 corrects; if that is the
  intended story, the version chain is the only trace of it.
- Condition: the first prize in this notice equals the first prize announced in the contract notice
  it refers to, or the flow makes explicit that version 1 of the award notice published a wrong
  amount that version 2 corrects.
- Options: (a) if 16 is meant as a correction: keep 6,000 here and make the correction explicit in 16
  (a Note saying what was corrected), so the contradiction is the story and not an accident; (b) if
  not: 8,000 here, and give 16 another reason to exist. Preferred: decide which story the two
  versions tell; (a) uses the version chain for what it is for.
- Needs decision: yes

### contest/15#F2 · Low · Customs and logistics master data the procurement document does nothing with
- XPath: `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- Why: `AdditionalPartyIdentification` is "one or more additional identifiers for this Party". The
  customs trader number (`urn:ubl-examples:world:XB:customs-trader`) identifies the Public Works
  Department towards customs; it is needed in its import declarations (e.g.
  `tender/31-ImportCustomsDeclaration.xml`), but this ContractAwardNotice is a procurement document of a design
  contest for a service: nothing is imported, declared or transported, and no receiver of the
  document uses a customs number. It looks copied from the party's master data (the same value occurs
  in 55 examples, counted with `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`,
  all 16 of this flow among them).
  The second-prize winner Valdara Industries carries the same kind of master data: its Urvanian
  customs trader number and a ServiceProviderParty (Castrano Logistics, "Warehousing and despatch",
  ID VI-SP-2026-01, which occurs in 73 examples of other flows, counted with
  `grep -rl --include='*.xml' VI-SP-2026-01 world/examples | grep -v contest | wc -l`). An award
  notice for a design prize despatches and stores nothing.
- Condition: every identifier carried for a party in this document is one the document or its
  receiver uses (no customs trader number, no logistics service provider in a procurement document of a services contest), or the document states why it is needed.
- Options: (a) preferred: leave the customs trader identification out of the procurement documents
  (keep it in the customs documents of the tender flow); (b) keep it only if the world gives the
  contest a customs reason (none is visible).
- Needs decision: no

## Checked and consistent
- Reference: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634` resolves to the contract notice (03, 08) of the same ContractFolderID.
- Dates: `/ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-06-28` lies after the submission deadline (2026-06-12 12:00) and before the issue date 2026-07-02.
- Counts: `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedTenderQuantity` = `4` lies within the short list of 3 to 5 participants; `/ContractAwardNotice/cac:TenderResult/cbc:ReceivedForeignTenderQuantity` = `1` is at most 4 and matches the one foreign winner, Valdara Industries of Urvania (country XU), against the Bayvarran contracting party.
- Ranks: WinningParty Rank 1 Brackenmere (20412466, the lead of the "Brackenmere and Saltmere design team" named in the Description and in 06/11) and Rank 2 Valdara; Prize[3] is absent, as the Description ("The jury withheld the third prize") and the contract notice ("if the jury finds it of prize standard") allow; PreSelectedParty Brackenmere matches the first-prize winner invited to negotiate.
- Identifiers of Valdara: ISIN XU0001042501 (check digit correct, `check_ids.py`; XU is not an ISO 3166 code, so it cannot be a real ISIN), register XU-R-104274 = CompanyID = endpoint XU:XU-R-104274.
- Codes: NoticeTypeCode CAN, TenderResultCode AWARDED (a winner was chosen), PrizeRankCode FIRST/SECOND, EDED 3155 AL (cellular phone) for a mobile number.
- Second prize 4,000 lume agrees with 03/08.
- Physics (section 5): the example describes a design-services contest and carries no goods, packages, handling units, equipment, vehicles, weights, volumes, energy or capacities, so there is nothing physical to calculate; the only figures with a physical meaning (a 420 m promenade, at most 900 lume a bench) are free text with no structured counterpart to check against.

## Considered and refuted
- `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634`: suspected that a reference by ID alone is ambiguous because two versions of the referenced document exist (03 and 08) — refuted because the versions share one document ID by design (VersionID/PreviousVersionID), a reference by document ID addresses the document, and the issue dates make the intended version unambiguous (the award follows version 2 of 2026-04-05, the current one).
- `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427` with schemeID ISO 6523: suspected an ICD assigned in the real ISO 6523 register — refuted as far as known: the assigned ICDs run in the low 0001–02xx range; 0990 is not assigned (own knowledge, not checked against the current register).
