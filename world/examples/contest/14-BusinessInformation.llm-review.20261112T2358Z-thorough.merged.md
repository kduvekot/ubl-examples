# LLM review: 14-BusinessInformation.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/14-BusinessInformation.xml`, Git blob `ea59d9c8ec70285678a63c9762adc18d4f21b15e` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
- Checkout: branch `claude/keen-feynman-45qjti`, commit 374ad95 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
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

### contest/14#F1 · Medium · Language code in LocaleCode
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code and repeats `Language/cbc:ID` (section 6: Medium). 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`, recounted).
- Condition: every `Language/LocaleCode` is absent or holds a locale from a locale list named in its `listID`.
- Options: (preferred) leave `LocaleCode` out; or a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### contest/14#F2 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: Bayvarra Information Service (ISIC 8411, the keeper of the register) and the Public Works Department (a city department) are entered as `COMMERCIAL` ("A register of businesses") and have a liquidation status; public bodies are not businesses and are not liquidated, and a city department is not a legal person of its own (section 5; parties). In a register extract the point is sharper: the register keeper describes itself as a business in its own register. The world list has no register type for public bodies.
- Condition: no public body carries a `CompanyLiquidationStatusCode` or a registration scheme of the type "Commercial register".
- Options: (preferred) drop the liquidation status and the registration type for public bodies; or a public-sector register type; or the City of Lumeport as legal entity of the department (a change of who the entity is).
- Needs decision: no
- From: broad (F2), parties (F1), context (F4)

### contest/14#F3 · Low · The production capability is an amount without a measure, and implausible against Brackenmere's turnover
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: `Capability/ValueAmount` is "A monetary amount as a measure of this capability". With type `PRODUCTION` and the description "Furniture of wood and steel, designed and made in its own workshop", the reader cannot tell whether the amount is yearly output, capacity or plant value, nor for which period; there is no quantity, evidence or validity period. Compare Valdara's extract in the same register, with quantity, evidence and validity (`tender/12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`). The same company (register 20412466) declared a 2025 turnover of 410,000 lume in the parks tender (`tender/07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`, verified); a production value of 6,830,000 is about 16.7 times that; version 1 had 6,410,000, whose digits after the leading 6 repeat the turnover, which suggests a slip (money). Parties refuted the size code against the amount: a capability is not a turnover, and a small workshop can have a capability in the low millions. The merge keeps the finding: the amount is not a hard contradiction (a capability need not equal output), but an extract the jury relies on should say what it measures, and against the declared turnover the figure is not plausible.
- Condition: the capability says what the amount measures and for which period (or quantity and evidence), and the figure is plausible against what Brackenmere declares about its turnover elsewhere.
- Options: (a, preferred) restate it as a yearly production value in line with the 410,000 lume turnover, with the period, quantity or evidence that gives it meaning; (b) if a capacity is meant, say so in the description and give the quantity it rests on; (c) drop the amount, since the extract is about registration and exclusion grounds (context's alternative).
- Needs decision: yes
- From: money (F1, Low, yes), broad (F5, Low, no), context (F2, Low, yes)

### contest/14#F4 · Low · Version 2 changes the capability amount without saying why, and keeps the subtype "Register extract"
- XPath: `/BusinessInformation/cbc:VersionID` = `2`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- XPath: `13-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6410000.00`
- XPath: `/BusinessInformation/cac:NoticeSubType/cbc:SubTypeCode` = `EXTRACT`
- Why: version 2 of the extract `BIS-DOC-26-0639`, four days after version 1, changes only the capability amount (verified with a diff of the two `*.xml`: apart from UUID, issue date and time and the version elements, the amount is the only difference). Nothing (`Note`, `BriefDescription`) says whether it corrects an error or reflects accounts filed in between, which matters to the department that uses the figure for the selection; a receiver sees two extracts with the same ID and different figures. The world's `NoticeSubTypeCode` list has `CORRECTION` ("A correction of an earlier notice."), but the document keeps `EXTRACT`. Whether the new version is a correction or an updated extract is not stated, so the code is preferred only if it is a correction.
- Condition: the extract says why the figure changed (correction, or a new period), and, if it is a correction, its subtype or text says so.
- Options: (preferred) a `Note` naming what changed and why, with `SubTypeCode` `CORRECTION` if it corrects version 1, or a validity period on the capability if it is a new period.
- Needs decision: no
- From: broad (F8), logistics (F1), context (F2, part), money (F1, part)

### contest/14#F5 · Low · Only the lead member's register extract; the group member is not checked
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Brackenmere Furniture: registered, no exclusion grounds recorded.`
- Why: the participant is a group, "Brackenmere and Saltmere design team" (`06-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cbc:EconomicOperatorGroupName` = `Brackenmere and Saltmere design team`), with Saltmere Engineering as member (`07-TendererQualification.xml`, `12-TendererQualification.xml`). The extract states "no exclusion grounds recorded" for Brackenmere only; no extract for Saltmere exists in the flow (verified: the only BusinessInformation documents are 13 and 14, both about 20412466), although exclusion grounds are normally checked for every member of a group (own knowledge of procurement practice, broad).
- Condition: the flow shows that every member of the group was checked, or says why the member is not.
- Options: (preferred) an extract for Saltmere Engineering (a new example), or a `BusinessPartyGroup` if the register issues one extract for a group; or state in the story why the member need not be checked.
- Needs decision: yes
- From: broad (F6)

### contest/14#F6 · Low · The receiving authority's customs-trader number and tax scheme in a register extract about another party
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- Why: section 4.8. The extract reports what the register holds about Brackenmere; the receiving department's customs number (55 files carry it, `grep -rl --include='*.xml' XB-TR-410548 world/examples | wc -l`) and its sales-tax registration and exemption play no part in it, and nothing in the document is taxed or declared. Brackenmere's own tax registration is not part of this finding: the extract reports the registrations the register holds about the party it describes (money; context agrees).
- Condition: the receiver carries only identifiers and registrations the extract uses.
- Options: (preferred) leave the receiver's customs number and tax scheme out of the extract.
- Needs decision: no
- From: broad (F3), money (F2), parties (F4), logistics (F2), context (F3)

### contest/14#F7 · Low · The receiver's tax exemption reason is worded as a sale
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the code's list definition ("A body of the federation, a state or a city buys free of sales tax") is the buyer's status and fits; the text begins "Sale to a public body", a transaction. Applies only if F6 keeps the tax scheme.
- Condition: where stated, the text describes the party's status, not a sale.
- Options: (preferred) "Public body: exempt from the state sales tax"; or a status code.
- Needs decision: no
- From: broad (F3, part), parties (F3), context (F3, part)

### contest/14#F8 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". In a register extract the date is part of what the register certifies, yet 1 January is a holiday and a typical placeholder, and the same date is given for 25 companies (271 occurrences in 181 files, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, recounted).
- Condition: Brackenmere's registration date is a date with a reason in the world, or absent.
- Options: (preferred) its own date from the story; or leave it out if only the year is known; or record 1996-01-01 as an event in the story.
- Needs decision: yes
- From: broad (F7, Low, no), parties (F6, Low, yes)

## Checked and consistent
- `NoticeTypeCode` `BUSREG` and `NoticeSubType` `EXTRACT` fit the note "Extract from the register of economic operators." and the `BriefDescription` (broad, logistics, context).
- Sender (the register keeper, Bayvarra Information Service 20410959), receiver (the contracting authority that asked) and business party (Brackenmere, 20412466, the same register number as in its application) fit a register extract (broad, parties, logistics, context).
- Issued 2026-05-09, after the participation deadline (2026-05-02) and before the submission deadline: the department checks a candidate at selection (broad, logistics).
- Brackenmere's legal entity (SMALL, LTD, active) and tax registration `UL-1237398` are the same as in the other examples; currency `XBL` is Bayvarra's (broad, money).
- BusinessInformation has no `ContractFolderID`; `ProfileExecutionID` `CONTEST-2026-01` ties it to the contest (logistics).
- Parties identical across the flow; GLN check digit valid; +999 and `.example` not real (broad, parties).
- Version chain: `VersionID` 2, `PreviousVersionID` 1, same ID as `13-BusinessInformation.xml`, issued four days later (logistics).
- Physics: nothing to calculate (logistics).

## Considered and refuted
- `/BusinessInformation/cbc:IssueDate` = `2026-05-09`: a new extract four days later is unnecessary — refuted: the changed amount gives the version a reason; its explanation is F4 (from broad).
- `/BusinessInformation/cbc:BriefDescription` = `Brackenmere Furniture: registered, no exclusion grounds recorded.`: no structured counterpart for the exclusion statement — refuted: BusinessInformation has no element for exclusion grounds (from broad).
- `/BusinessInformation/cac:BusinessParty/cac:PartyTaxScheme`: master data copied into the extract — refuted: a register extract reports the registrations held about its subject (from money).
- `/BusinessInformation/cac:ReceiverParty/cbc:IndustryClassificationCode`: ISIC 8411 too general — refuted (from parties).
- `/BusinessInformation/cac:ReceiverParty/cac:PostalAddress/cbc:Department`: address vs contact department — refuted: the same unit (from parties).
- `/BusinessInformation/cac:SenderParty/cac:PostalAddress/cbc:PostalZone`: two postal zones (38517, 38520) on one square — refuted: individual postal codes for large addressees are usual (from parties).
- `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: `SMALL` against 6,830,000 lume — refuted for the size code (a capability is not a turnover) (from parties); the amount's plausibility against the declared turnover is part of F3.
- `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`: a turnover in the wrong code — refuted for the code: an annual production value is a monetary measure of a production capability (from logistics); what the amount measures is F3.
- No reference from the extract to the request or the procedure — refuted: BusinessInformation has no `ContractFolderID`, and `ProfileExecutionID` links it (from logistics).
- `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:Name` = `Trade sales`: the sales desk as contact — refuted: the register publishes the contact it holds for the business, not a contest contact (from context; adopted by the merge, see Refuted in the merge).

## Refuted in the merge
### broad/F4 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why (broad): a contact is "The primary contact for this party" in its role in this document; Brackenmere takes part in a design contest through its trade-sales desk, while Saltmere uses a bids office; the contacts look taken from the trading master data.
- Condition (broad): each contact handles the party's role in the contest.
- Refuted because: in this document Brackenmere is not a contest participant but the `BusinessParty` an extract is about; the register reports the contact it holds on file for the business (context's argument), and a company's general contact is the plausible one to hold. The same finding stands in 09–12, where Brackenmere acts in the contest.

### parties/F5 · Low · Contacts that do not fit the party's role in the contest
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:Name` = `Trade sales`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why (parties): section 5, the contact must fit the role; a "Customer service officer" of "Trade sales" handles trade customers' orders, not a design contest or a tender.
- Condition (parties): each contact handles the party's part in the contest, with job title and department that agree.
- Refuted because: as for broad/F4: the business party of a register extract carries the contact the register holds.

## Changed in the merge
- broad/F2 (Low, yes), parties/F1 (Medium, yes), context/F4 (Low, no) → F2: Medium, needs decision no (aligned with the earlier flows).
- money/F1, broad/F5, context/F2 (Low, yes in 14) → F3: combined; Low with needs decision yes (money, context), because restating the figure changes the company's numbers in the story; parties' and logistics' refutations of the size code and capability type added as counter-arguments.
- broad/F3, money/F2, parties/F4, logistics/F2, context/F3 → F6 and F7 (wording of the exemption, parties/F3); limited to the receiver, following money's refutation for the business party.
- broad/F7 (Low, no), parties/F6 (Low, yes) → F8: needs decision yes, aligned with all earlier flows.
- broad/F8, logistics/F1, and the version-change parts of context/F2 and money/F1 → F4: combined; the subtype code made conditional on the change being a correction, since nothing says it is.
- broad/F4, parties/F5 → Refuted in the merge (context's refutation followed).

## Outside this review
- The same party descriptions recur in the other flows that carry these parties; they belong to those examples' reviews (from parties).
