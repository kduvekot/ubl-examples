# LLM review: 08-ProcurementStatusRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/08-ProcurementStatusRequest.xml`, Git blob `8b0ed73feb4728e9ed11f9a24ad476449b06b7f2` (committed)
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

### tender/08#F1 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1), parties (F1)

### tender/08#F2 · Medium · The contracting authority, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F3), parties (F4)

### tender/08#F3 · Low · The department's customs trader number in a status request
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Copied master data (section 4.8): a customs trader number identifies the department towards customs; nothing in a question about a deadline is declared to customs (such numbers are used in the customs declarations 30 and 31).
- Condition: Each party carries only the identifiers the document uses or the receiver needs to identify it.
- Options: (a) leave the customs trader number to the customs and transport documents (preferred); (b) keep it if the world's rule is that every document carries all identifiers of a party, and state that rule.
- Needs decision: no
- From: context (F3), parties (F2)

### tender/08#F4 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F4), parties (F3)

### tender/08#F5 · Low · Registration date 1 January 1996, shared by 25 unrelated companies
- XPath: `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Brackenmere Furniture shares the New Year's Day with 24 other parties, 271 times in 181 of the 250 examples (recounted: `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`, `-l` for files): a default, not a fact of each company. In 07 Brackenmere states 26 years (07 F11).
- Condition: Each company has its own registration date (or none where the world has none).
- Options: (a) a date per company from its history (preferred); (b) drop the date where unused; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F5)

### tender/08#F6 · Low · The project is named "… for the city parks" here and "… for the parks renewal programme" in the notices and in this document's own contract name
- XPath: `/ProcurementStatusRequest/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatusRequest/cbc:ContractName` = `Park benches for the parks renewal programme`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "A name of this procurement project". The notices and the call for tenders name the project "Park benches for the parks renewal programme", and this document uses that name as `ContractName`; its `ProcurementProject` has a name found only in 08, 09 and 24 (recounted: `grep -rc --include='*.xml' 'Park benches for the city parks' world/examples`). The process is identified unambiguously by `TenderingProcess/ID` and `ContractFolderID`, so this is only an inconsistency of the name (Low).
- Condition: The project has the same name as in the contract notice.
- Options: (a) use the notice's name (preferred); (b) drop the name and rely on the IDs.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2)

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit (prefix 952, GS1 range for examples).
- `TenderingProcess/ID` `PWD-2026-PARKS-P` is the process ID of 02, 03, 21 and 24; `ContractFolderID` `PWD-2026-PARKS`; `LOT-1` and `LOT-2` are the two lots of the notice.
- Issued 2026-02-20 15:50, the day after the period for additional information ended (`AdditionalInformationRequestPeriod/EndDate` 2026-02-19 in 02, re-checked) and six days before the tender deadline (2026-02-26 12:00); answered by 09 on 2026-02-21, which refers to this request by its ID `BF-DOC-26-0194`. The question ("Does the deadline stand after the answers to the questions?") states what is asked; nothing the request's purpose needs is missing.
- Parties: Lumeport Public Works Department as ContractingParty, Brackenmere Furniture as EconomicOperatorParty and SignatoryParty (register number 20412466), described as in the other examples of the flow (parties compared by script). ISIC 3100 and 8411 fit; +999 telephone numbers and `.example` addresses. `ProcurementTypeCode` SUPPLIES resolves.

## Considered and refuted
- `/ProcurementStatusRequest/cac:ProcurementProjectLot[2]/cbc:ID`: Brackenmere asks about lot 2 although its qualification (06, 07) and tenders (17, 19) concern lot 1 — refuted, the deadline it asks about is that of the whole procedure (from broad, context).
- `/ProcurementStatusRequest/cac:ProcurementProject/cbc:ProcurementTypeCode`: SUPPLIES although lot 2 is a service — refuted, the project as a whole is classified as supplies in the notices (from broad).
- `/ProcurementStatusRequest/cbc:IssueDate`: a question after the period for additional information ended on 2026-02-19 — refuted, a status request asks for the state of the procedure, not for additional information (from logistics).
- `/ProcurementStatusRequest/cbc:ID`: `BF-DOC-26-0194` directly after Brackenmere's `BF-DOC-26-0193` (07, the day before) — refuted, the numbers are in date order (from logistics).
- `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office` — refuted, a functional contact name; "Procurement office" and "Procurement" name the same unit (from parties).
- `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` = `STATE` — refuted, the level of the tax, not of the party (from parties).
- `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact ("Trade sales") for a procurement procedure — refuted, for a small manufacturer the sales office handles tenders; name, job title and department agree (from parties). Kept refuted in the merge; the contest merge (a) had kept the same contact as Low.

## Changed in the merge
- broad/F3, parties/F4 (Low) → F2 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- parties/F5 (Needs decision no) → F5 yes: aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01).
