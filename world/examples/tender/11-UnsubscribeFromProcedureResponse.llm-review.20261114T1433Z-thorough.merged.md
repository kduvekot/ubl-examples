# LLM review: 11-UnsubscribeFromProcedureResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/11-UnsubscribeFromProcedureResponse.xml`, Git blob `fb12fe4c0c9c9356bb49cf3774522f5fcb156bfb` (committed)
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

### tender/11#F1 · High · The sawmill is a small enterprise here, but states 85 employees in its expression of interest
- XPath: `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: The world's list defines `SMALL` as "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL, …" (`world/codelists/gc/EntitySizeCode.gc`): both conditions must hold. In 04, whose registration this response ends, the same party states 85 employees, at most `MEDIUM`. Unlike Valdara's `LARGE` with 180 employees (13), where "250 persons or more, or a turnover above …" leaves room, `SMALL` with 85 persons is a strict contradiction between two examples of the flow (section 6 High). Which figure is the sawmill's real size is a story fact, hence Needs decision yes (parties; broad said no). Same finding as 10 F1.
- Condition: The size class of Marrowdale Sawmill agrees with the number of employees it states in 04 (in 04, 05, 10 and 11 alike).
- Options: (a) fewer than 50 employees in 04 (preferred: `SMALL` in four examples); (b) `MEDIUM` in 04, 05, 10 and 11.
- Needs decision: yes
- From: broad (F1), parties (F1)

### tender/11#F2 · Medium · Language code in LocaleCode
- XPath: `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F1), parties (F2)

### tender/11#F3 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F3), parties (F6)

### tender/11#F4 · Low · Customs trader numbers of both parties in an unsubscribe confirmation
- XPath: `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): customs trader numbers identify the parties towards customs; nothing here is declared to customs.
- Condition: Each party carries only the identifiers the document uses or the receiver needs to identify it.
- Options: (a) leave the customs trader numbers to the customs and transport documents (preferred); (b) keep them if the world's rule is that every document carries all identifiers of a party, and state that rule.
- Needs decision: no
- From: context (F2), parties (F3)

### tender/11#F5 · Low · Registration date 1 January 1996, shared by 25 unrelated companies, against 22 operating years
- XPath: `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:OperatingYearsQuantity` = `22`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Marrowdale Sawmill shares the New Year's Day with 24 other parties, 271 times in 181 of the 250 examples (recounted: `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files): a default, not a fact of each company. In 04 the sawmill states 22 operating years (about 2004).
- Condition: Each company has its own registration date, consistent with what it says about its age (or none where the world has none).
- Options: (a) a date per company from its history (preferred); (b) drop the date where unused; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F4); the operating years added by the merge

### tender/11#F6 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F4), parties (F5)

## Checked and consistent
- `UnsubscribeToProcedureDocumentReference` `MS-DOC-26-0196` resolves to 10, the unsubscribe request of the same operator (2026-02-22 14:30); this confirmation follows on 2026-02-23 14:48, a Monday. Parties, `ContractFolderID`, the project block and `LOT-1` equal those of 10 and of 04/05, the registration that ends here.
- The note ("The sawmill no longer receives the procedure's messages.") states what the document is for ("confirming that the latter has been unsubscribed") and mirrors 05 ("the sawmill receives every change to the documents").
- `LPWD-DOC-26-0197` is issued after the department's `-0195` (2026-02-21), in order. Signature `PWD-SIG-UNSR` uses the department's prefix.
- Parties described as in the other examples of the flow (parties compared by script); +999 telephone numbers and `.example` addresses; `check_ids.py` finds no identifier with a check digit.

## Considered and refuted
- `/UnsubscribeFromProcedureResponse/cac:ProcurementProject/cbc:Name`: "Park benches" is the lot's name, not the project's — refuted, 04, 05, 10 and 11 consistently concern lot 1 only and name it as the notice names lot 1 (`02-ContractNotice.xml:/ContractNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:Name` = `Park benches`, checked in the merge) (from broad).
- `/UnsubscribeFromProcedureResponse/cbc:IssueDate`: a confirmation a full day after the request — refuted, no rule of the flow sets a shorter time and 05 also answered the next day (from logistics).
- `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).
- `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact ("Sales office") — refuted, for a small manufacturer the sales office answers tenders (from parties).

## Changed in the merge
- broad/F1 (Needs decision no), parties/F1 (yes) → F1 High, yes, as in 10.
- broad/F3, parties/F6 (Low) → F3 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- parties/F4 (Needs decision no) → F5 yes: aligned with analysis/review-merge-decisions.md; the 22 operating years of 04 added to "Why".
