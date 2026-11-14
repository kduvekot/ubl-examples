# LLM review: 10-UnsubscribeFromProcedureRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/10-UnsubscribeFromProcedureRequest.xml`, Git blob `77ba312be318d0b7309984f6f48be21161975fc5` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/10#F1 · High · The sawmill is a small enterprise here, but states 85 employees in its expression of interest
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: The world's list defines `SMALL` as "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL, …" (checked in `world/codelists/gc/EntitySizeCode.gc`): both conditions must hold. In the expression of interest that this request withdraws, the same party states 85 employees, which can at most be `MEDIUM` ("Fewer than 250 persons and …"). Unlike Valdara's `LARGE` with 180 employees (13), where the list's "250 persons or more, or a turnover above …" leaves room through the turnover, `SMALL` with 85 persons is a strict contradiction between two examples of the flow (section 6 High). Needs decision yes (parties; broad said no): which of the two figures is the sawmill's real size is a fact of the story.
- Condition: The size class of Marrowdale Sawmill agrees with the number of employees it states in 04 (in 04, 05, 10 and 11 alike).
- Options: (a) fewer than 50 employees in 04, if the sawmill is meant to be small (preferred: it is described as `SMALL` in four examples); (b) `MEDIUM` in 04, 05, 10 and 11.
- Needs decision: yes
- From: broad (F1), parties (F1)

### tender/10#F2 · Medium · Language code in LocaleCode
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F1), parties (F2)

### tender/10#F3 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F4), parties (F7)

### tender/10#F4 · Low · Issued by the sawmill on a Sunday, outside the hours its contact states
- XPath: `/UnsubscribeFromProcedureRequest/cbc:IssueDate` = `2026-02-22`
- XPath: `/UnsubscribeFromProcedureRequest/cbc:IssueTime` = `14:30:00`
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: Added by the merge from broad's refuted candidate, to treat it as 09 F4: 2026-02-22 is a Sunday in the real calendar (2026-01-01 is a Thursday; 52 days later), and the sawmill's contact states weekdays 08:00–17:00. Against it (broad): the examples nowhere say that the world's week follows the real calendar; and a contact's hours say when it can be reached, not when a document may be sent. The merge cannot settle it; Low with both arguments.
- Condition: The request is issued on a working day, or the world records that its parties send documents at weekends.
- Options: (a) Monday 2026-02-23 morning, before the department's confirmation 11 at 14:48 the same day (preferred); (b) keep it and state the convention.
- Needs decision: yes
- From: merge (broad's refuted candidate)

### tender/10#F5 · Low · Signature ID with a prefix that is not the sawmill's
- XPath: `/UnsubscribeFromProcedureRequest/cac:Signature/cbc:ID` = `HS-SIG-UNS`
- XPath: `/UnsubscribeFromProcedureRequest/cbc:ID` = `MS-DOC-26-0196`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- Why: `Signature/ID` is "An identifier for this signature". Every other signature ID of the flow begins with the abbreviation its signatory uses (`PWD-`/`LPWD-`, `BF-`, `VI-`, `BLUM-`, `BIS-`, `CL-`; recounted over the flow's XML). Marrowdale Sawmill numbers its documents `MS-…`, but its two signatures (here and in 04) begin with `HS`, which matches no party of the flow (`grep -rl --include='*.xml' HS-SIG world/examples` finds only 04 and 10).
- Condition: The sawmill's signature IDs use its own abbreviation, consistent with its document numbers.
- Options: (a) `MS-SIG-UNS` (and `MS-SIG-EOI` in 04) (preferred); (b) leave as is if `HS` has a meaning in the world that the XML does not show.
- Needs decision: no
- From: broad (F3), context (F2), logistics (F2), parties (F3)

### tender/10#F6 · Low · Customs trader numbers of both parties in an unsubscribe request
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): customs trader numbers identify the parties towards customs; nothing here is declared to customs, and the sawmill ships nothing in this flow.
- Condition: Each party carries only the identifiers the document uses or the receiver needs to identify it.
- Options: (a) leave the customs trader numbers to the customs and transport documents (preferred); (b) keep them if the world's rule is that every document carries all identifiers of a party, and state that rule.
- Needs decision: no
- From: context (F3), parties (F4)

### tender/10#F7 · Low · Registration date 1 January 1996, shared by 25 unrelated companies, against 22 operating years
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:OperatingYearsQuantity` = `22`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Marrowdale Sawmill shares the New Year's Day with 24 other parties, 271 times in 181 of the 250 examples (recounted: `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files): a default, not a fact of each company. The merge adds that in 04 the sawmill states 22 operating years, which would mean about 2004, not 1996.
- Condition: Each company has its own registration date, consistent with what it says about its age (or none where the world has none).
- Options: (a) a date per company from its history (preferred); (b) drop the date where unused; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F5); the operating years added by the merge

### tender/10#F8 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F5), parties (F6)

## Checked and consistent
- The sawmill registered with the expression of interest 04 (2026-02-14, `LOT-1`, "Park benches", SUPPLIES), was confirmed by 05 (2026-02-15) and unsubscribes here on 2026-02-22, before the tender deadline of 2026-02-26 and the end of the validity of its expression of interest (2026-02-26 in 04); 11 confirms on 2026-02-23 and refers to this request by its ID `MS-DOC-26-0196`. The note ("No bench maker joined the sawmill; it will not tender.") continues the note of 04.
- `ContractFolderID` `PWD-2026-PARKS`, the project block and `LOT-1` equal those of 04 and 05. `MS-DOC-26-0196` follows the sawmill's `MS-DOC-26-0190` (04) in number and date.
- Parties: Marrowdale Sawmill as EconomicOperatorParty and SignatoryParty, Lumeport Public Works Department as ContractingParty, described as in the other examples of the flow (parties compared by script). ISIC 1610 and 8411 fit; +999 telephone numbers and `.example` addresses; `check_ids.py` finds no identifier with a check digit.

## Considered and refuted
- `/UnsubscribeFromProcedureRequest/cac:ProcurementProjectLotReference`: the request names neither the expression of interest (04) nor its confirmation (05) — refuted, the document type has no dedicated reference for it, and the folder, the operator and the lot identify the subscription unambiguously (from broad, context, logistics).
- `/UnsubscribeFromProcedureRequest/cbc:IssueDate`: 2026-02-22 is a Sunday — refuted by broad (the world's week is not stated to follow the real calendar); the merge disagrees in part and made it F4, Low/yes, with this argument, as in 09.
- `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).
- `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact ("Sales office") for a procurement procedure — refuted, for a small manufacturer the sales office answers tenders; name, job title and department agree (from parties).

## Changed in the merge
- broad/F1 (Needs decision no), parties/F1 (yes) → F1 High, yes: which figure is the sawmill's size is a story fact.
- broad/F4, parties/F7 (Low) → F3 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- F4 added by the merge from broad's refuted candidate (Sunday issue), to treat it as 09 F4 (Low/yes, both arguments).
- parties/F5 (Needs decision no) → F7 yes: aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01); the 22 operating years of 04 added to "Why".

## Outside this review
- In 04 itself the sawmill is described as `SMALL` next to its 85 employees, and with 22 operating years next to a 1996 registration; those contradictions lie in 04.
