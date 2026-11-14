# LLM review: 05-ExpressionOfInterestResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/05-ExpressionOfInterestResponse.xml`, Git blob `3fc9021a423cb516bf42fbd92205840f2d256f11` (committed)
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

### tender/05#F1 · High · The sawmill is a small enterprise here, but states 85 employees in its expression of interest
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: The world's list defines `SMALL` as "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL …". In 04, the expression of interest this response confirms, the same party states 85 employees. Both conditions of `SMALL` must hold, so the two descriptions of the same party cannot both be true.
- Condition: the size class of Marrowdale Sawmill agrees with the number of employees stated in 04.
- Options: settle the sawmill's size once (see 04/F1): (a) preferred: fewer than 50 employees in 04; (b) `MEDIUM` here and in 04, 10, 11.
- Needs decision: yes
- From: broad (F1, Needs decision no), parties (F1)

### tender/05#F2 · Medium · A language code in `LocaleCode`
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats `cbc:ID` and names no locale. 362 such elements in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, and `-rl` for files).
- Condition: `LocaleCode`, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) preferred: remove it; (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F2), parties (F2)

### tender/05#F3 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The department, a local authority (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`), is described with a liquidation status and a register of type `COMMERCIAL` ("A register of businesses"); a public body is neither. The world's list has no register type for public bodies.
- Condition: a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop `CompanyLiquidationStatusCode` and type the scheme differently, or keep only the identifier; (b) a stated world rule, without the liquidation status.
- Needs decision: no
- From: broad (F3, Low), parties (F6, Low)

### tender/05#F4 · Low · Registration confirmed for a request that came after the period the contract notice sets
- XPath: `/ExpressionOfInterestResponse/cac:ExpressionOfInterestDocumentReference/cbc:ID` = `MS-DOC-26-0190`
- XPath: `/ExpressionOfInterestResponse/cbc:Note` = `Registered: the sawmill receives every change to the documents.`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- Why: The department confirms, without comment, an expression of interest of 2026-02-14, while its own contract notice (and 03) ends the reception of requests to participate on 2026-02-11. Logistics rated it High (one of the two statements is wrong). In an open procedure an expression of interest need not be a request to participate (broad and context in 04: it only registers an interested operator, and the stale periods are findings of 02 and 03). The merge cannot settle which reading the world means, as in 04/F4.
- Condition: the request this response confirms lies inside the period the notice sets for it, or the notice sets no such period.
- Options: (a) preferred: resolve in 02/03 by removing or moving the reception period; (b) move 04 and this response before 2026-02-11.
- Needs decision: yes
- From: logistics (F1, High)

### tender/05#F5 · Low · Signed by the procurement office on a Sunday morning, against its stated weekday hours
- XPath: `/ExpressionOfInterestResponse/cbc:IssueDate` = `2026-02-15`
- XPath: `/ExpressionOfInterestResponse/cbc:IssueTime` = `08:35:00`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/ExpressionOfInterestResponse/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: 2026-02-15 is a Sunday in the common calendar (1 January 2026 is a Thursday; recalculated: 45 days later, 45 mod 7 = 3, Sunday). The office that signs states in the same document that it is reachable on weekdays, 08:00 to 17:00 (context). Broad refuted it: a registration confirmation can be issued by the platform automatically, and the world's calendar is not stated to follow real weekdays. Context answers that an automatic confirmation would not be signed by the office. The merge cannot settle it, as merger B for the documents of 09 and 10 (Low, Needs decision yes).
- Condition: a document signed by the office is issued on its working days, or says it is generated automatically, or the world states its calendar.
- Options: (a) preferred by context: issue it on Monday 2026-02-16; (b) say in the note that the platform registers and confirms automatically.
- Needs decision: yes
- From: context (F2, Needs decision no); broad refuted it (Considered and refuted)

### tender/05#F6 · Low · Customs trader numbers of both parties in a confirmation of interest
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Nothing in this document is declared to customs; the numbers matter only when goods cross the border (30, 31). Copied master data (section 4.8).
- Condition: a party carries the identifiers the document uses; no customs trader number in a tendering document.
- Options: (a) preferred: leave them to the customs and transport documents; (b) a stated world rule.
- Needs decision: no
- From: parties (F3), context (F3)

### tender/05#F7 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default date for 25 unrelated parties, 271 times in 181 files (`grep -rh --include='*.xml' 'RegistrationDate>1996-01-01' world/examples`, lines and files, recounted); for the sawmill it also disagrees with the 22 operating years of 04 (04/F6).
- Condition: each party's registration date is its own, or absent.
- Options: (a) preferred: a date of its own per party (for the sawmill about 22 years ago); (b) leave it out; (c) a 1996 re-registration as a stated story fact.
- Needs decision: yes
- From: parties (F4, Needs decision no)

### tender/05#F8 · Low · The department's tax exemption reason is worded as a sale
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax" — the text starts with a transaction, while the code's definition ("A body of the federation, a state or a city buys free of sales tax") fits the party.
- Condition: the party's exemption reason states its status.
- Options: (a) preferred: "Public body: buys free of the state sales tax", code unchanged; (b) a separate status code.
- Needs decision: no
- From: broad (F4), parties (F5)

## Checked and consistent
- `ExpressionOfInterestDocumentReference` `MS-DOC-26-0190` resolves to 04, an expression of interest request issued 2026-02-14 14:05, before this response (2026-02-15 08:35); operator, contracting party, `ContractFolderID`, `ContractName`, project block and `LOT-1` equal those of 04.
- The note ("Registered: …") is what the document type is for ("to inform the Economic Operator he has been registered as an interested party").
- The sawmill is described identically in 04, 05, 10 and 11 (apart from the qualifying data, which only 04 carries), the department identically in all examples (broad, parties, by script).
- Codes: ISIC 1610, 8411; world-list codes resolve; `check_ids.py`: no check-digit identifiers; +999 unassigned.

## Considered and refuted
- `/ExpressionOfInterestResponse/cbc:TenderLanguageLocaleCode`: `en` from ISO 639 in an element named "locale code" — refuted because its definition is "A code signifying the language required for the tender"; a language code is what it asks for, and it agrees with the notice language of 02 (from broad, context, logistics).
- `/ExpressionOfInterestResponse/cbc:IssueDate`: a Sunday against "Weekdays 08:00–17:00" — refuted by broad (automatic platform confirmation; the world's calendar is not stated) — the merge cannot settle it and keeps context's F5, Low, Needs decision yes (from broad).
- `/ExpressionOfInterestResponse/cbc:ID`: `LPWD-DOC-26-0191` issued two days after the department's `LPWD-DOC-26-0192` (06, 2026-02-13) — kept out of this example; a finding of 06, whose number is ahead of its date (from logistics).
- `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`, `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`, `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`, `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` — refuted as in 01 (from parties).
- `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact for an operator in a procedure — refuted, the sales office answers tenders for a small manufacturer (from parties).

## Changed in the merge
- broad/F1 (no), parties/F1 (yes) → F1: Needs decision yes, as 04/F1 and merger B.
- broad/F3, parties/F6 → F3: Low raised to Medium (main table, mergers B, C, D, E).
- logistics/F1 (High) → F4: Low, Needs decision yes, as 04/F4 (cannot settle whether an expression of interest is a request to participate).
- context/F2 (no) → F5: Needs decision yes, with broad's refutation as counter-argument, aligned with merger B (issue on a Saturday/Sunday against weekday contacts: Low, yes).
- parties/F4 (no) → F7: Needs decision yes, as the main table and the other mergers.
- broad/F2, context/F1, logistics/F2, parties/F2 → F2; parties/F3, context/F3 → F6; broad/F4, parties/F5 → F8: combined, severity unchanged.

## Outside this review
- Whether an expression of interest and its confirmation belong in an open procedure is a question of the flow's story; see 02/F13 (from broad).
