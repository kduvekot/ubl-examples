# LLM review: 04-ExpressionOfInterestRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/04-ExpressionOfInterestRequest.xml`, Git blob `1ca94275bd6d396987ad7aa46080a104842bb2c3` (committed)
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

### tender/04#F1 · High · A small enterprise with 85 employees
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: The world's list defines `SMALL` as "Fewer than 50 persons and a turnover of at most 10,000,000.00 XBL …" and `MEDIUM` as "Fewer than 250 persons and …"; `EmployeeQuantity` is "The number of people employed by this qualifying party" (unit `IE`, person). 85 is not fewer than 50, and the definition of `SMALL` requires both conditions, so the two values of the same party in the same document contradict each other (unlike Valdara's `LARGE` with 180 persons, whose definition reads "or"). The sawmill is `SMALL` also in 05, 10 and 11.
- Condition: the number of employees and the size class of Marrowdale Sawmill agree with the list's thresholds, here and in every example that describes the sawmill.
- Options: (a) preferred by both parts: fewer than 50 employees here (one value changes); (b) `MEDIUM` everywhere the sawmill is described. Which figure is the sawmill's real size is a story question.
- Needs decision: yes
- From: broad (F1, Needs decision no), parties (F1)

### tender/04#F2 · Medium · A language code in `LocaleCode` and in `PreferredLanguageLocaleCode`
- XPath: `/ExpressionOfInterestRequest/cbc:PreferredLanguageLocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `PreferredLanguageLocaleCode` is "A code signifying the locale in which the language in the required documents is preferred", `LocaleCode` "A code signifying the locale in which this language is used." `en` with listID `ISO 639` is a language, not a locale; in the parties it only repeats `cbc:ID`. (The response 05 uses `TenderLanguageLocaleCode`, whose definition does ask for a language.) 362 `LocaleCode` elements with this value in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: a locale element carries a locale from a list of locales, or is absent.
- Options: (a) preferred: remove `LocaleCode` from the parties; give `PreferredLanguageLocaleCode` a locale (e.g. `en-XB`) from a locale list, or remove it and state the preferred language in the note; (b) locales everywhere.
- Needs decision: no
- From: broad (F2), context (F1), logistics (F2, F3), parties (F2)

### tender/04#F3 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`
- Why: The department, a local authority (ISIC 8411), is described with a liquidation status and a register of type `COMMERCIAL` ("A register of businesses"); a public body is not a business in a commercial register and cannot be in liquidation. The world's list has no register type for public bodies.
- Condition: a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop `CompanyLiquidationStatusCode` and type the scheme differently (a new code), or keep only the identifier; (b) a stated world rule, without the liquidation status.
- Needs decision: no
- From: broad (F7, Low), parties (F9, Low)

### tender/04#F4 · Low · The interest is expressed after the period for requests to participate has ended
- XPath: `/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- XPath: `/ExpressionOfInterestRequest/cac:DocumentReference/cbc:ID` = `LPWD-DOC-26-0188`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cbc:ProcedureCode` = `OPEN`
- Why: The contract notice this document answers ends "the period during which requests for participation must be completed and delivered" on 2026-02-11 (also in 03); the sawmill writes on 2026-02-14, and is still registered in 05. Logistics rated it High: if the expression of interest is the request to participate, the two documents contradict each other on whether it is in time. Broad rated it Low: in an open procedure no request is needed to tender, the expression of interest only serves to "follow the procedure" (its note), and the stale periods are a finding of 02 and 03 (context put it under Outside this review on the same ground). The merge cannot settle whether an expression of interest is a request for participation in the world's open procedure; the fix belongs to 02/F13 and 03/F14 in either reading.
- Condition: the expression of interest lies within the period the notice gives for it, or the notice gives no such period.
- Options: (a) preferred: correct the periods of 02 and 03 (remove them, or a registration period that ends after 04); (b) date the expression of interest within the period.
- Needs decision: yes
- From: logistics (F1, High), broad (F3); context (Outside this review)

### tender/04#F5 · Low · A consortium lead with a 60 % share, in a consortium that has no other member
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:ParticipationPercent` = `60`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:TendererRoleCode` = `LEAD`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleCode` = `LEAD`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:EconomicOperatorRole/cbc:RoleDescription` = `Supplies the slats; a bench maker would build the benches.`
- XPath: `/ExpressionOfInterestRequest/cbc:Note` = `The sawmill considers a tender for lot 1 with a bench maker and asks to follow the procedure.`
- XPath: `10-UnsubscribeFromProcedureRequest.xml:/UnsubscribeFromProcedureRequest/cbc:Note` = `No bench maker joined the sawmill; it will not tender.`
- Why: `ParticipationPercent` is "The extent to which this party is expected to participate in the tendering process, expressed as a percentage"; `EconomicOperatorRole` is "The role of the party in a tender consortium", and `LEAD` "Consortium lead: Leads a group of economic operators". The sawmill only considers tendering with a bench maker that is not named and, as 10 shows, never joins. A lead role and a share presuppose a group with agreed members and shares; and 60 % for the party that supplies five slats of a steel-framed bench estimated at 499 lume, with the bench maker at 40 %, is not explained. Context adds that the qualifying party is the operator itself, so the aggregate only adds its years and staff, which an expression of interest does not need; broad refuted that part (the qualifying data are the operator's own), and the merge keeps them, since F1 and F6 use them.
- Condition: a consortium role and share are stated only for a consortium whose members are known, and the share fits what each contributes; otherwise the document says the operator is interested and what it considers.
- Options: (a) preferred: drop `ParticipationPercent` and both lead role codes, and say in the role description or note that a partner is sought; (b) name the bench maker as a second qualifying party with shares that fit.
- Needs decision: no
- From: broad (F5), parties (F5, Needs decision yes), context (F2), money (F1, Needs decision yes)

### tender/04#F6 · Low · 22 years in operation, registered 30 years ago
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:OperatingYearsQuantity` = `22`
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- Why: `OperatingYearsQuantity` is "The number of years that this qualifying party has been in operation". The company was registered ("The registration date of the CompanyID") on 1996-01-01, 30 years before this document (2026 − 1996). A company can be registered before it operates, but eight years in between are unexplained; the registration date is the shared default of F7.
- Condition: years in operation and registration date tell one history, or the difference is explained.
- Options: (a) preferred by parties: a registration date about 22 years before 2026, which also resolves F7 for the sawmill; (b) preferred by broad: 30 years in operation.
- Needs decision: no
- From: broad (F4), parties (F4)

### tender/04#F7 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The date 1996-01-01 is given for 25 different parties in three countries, 271 times in 181 files (`grep -rh --include='*.xml' 'RegistrationDate>1996-01-01' world/examples`, lines and files, recounted). One register entry date on New Year's Day for unrelated companies is a default, not a fact of each company (no fillers).
- Condition: each party's registration date is its own, or the date is absent where the world has none.
- Options: (a) preferred: a date of its own per party, from its history (here about 22 years ago, see F6); (b) leave `RegistrationDate` out for parties without a history; (c) a 1996 re-registration as a stated story fact.
- Needs decision: yes
- From: parties (F7, Needs decision no)

### tender/04#F8 · Low · Customs trader numbers of both parties in an expression of interest
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Nothing in an expression of interest is declared to customs, and the sawmill, which never tenders, ships nothing in this flow; the numbers are copied master data (section 4.8).
- Condition: a party carries the identifiers the document uses; no customs trader number in a tendering document.
- Options: (a) preferred: leave them to the customs and transport documents; (b) a stated world rule.
- Needs decision: no
- From: parties (F6), context (F4)

### tender/04#F9 · Low · The department's tax exemption reason is worded as a sale
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: In `PartyTaxScheme` the reason is "A reason for the party's exemption from tax"; the text starts with a transaction, while the code's definition ("A body of the federation, a state or a city buys free of sales tax") fits the party. (Money refuted the same text in 01–03 because its second half states the status.)
- Condition: the party's exemption reason states its status.
- Options: (a) preferred: "Public body: buys free of the state sales tax", code unchanged; (b) a separate status code.
- Needs decision: no
- From: broad (F8), parties (F8)

### tender/04#F10 · Low · Signature ID with a prefix that is not the sawmill's
- XPath: `/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- XPath: `/ExpressionOfInterestRequest/cbc:ID` = `MS-DOC-26-0190`
- XPath: `10-UnsubscribeFromProcedureRequest.xml:/UnsubscribeFromProcedureRequest/cac:Signature/cbc:ID` = `HS-SIG-UNS`
- Why: Every other signature of the flow starts with the abbreviation its party uses in its document numbers (`PWD-SIG-…`, `BF-SIG-…`, `VI-SIG-…`, `BLUM-SIG-…`, `BIS-SIG-…`). The sawmill numbers its documents `MS-…` but signs `HS-…` here and in 10; `HS` matches no party of the flow.
- Condition: the signature ID uses the sawmill's own abbreviation, or the prefix is explained.
- Options: (a) preferred: `MS-SIG-EOI` (and `MS-SIG-UNS` in 10); (b) keep it if `HS` has a meaning in the world (not visible in the XML).
- Needs decision: no
- From: broad (F6), parties (F3), context (F3), logistics (F4)

## Checked and consistent
- `DocumentReference` `LPWD-DOC-26-0188` resolves to 02, the contract notice, issued three days before; `ContractFolderID`, `ContractName`, lot `LOT-1` and the project block ("Park benches", SUPPLIES) agree with 02.
- `ValidityPeriod/EndDate` 2026-02-26 is the tender deadline of 02/03; 05 answers by this document's ID on 2026-02-15 08:35; 10 withdraws the registration on 2026-02-22, within the validity period.
- The sawmill is described identically in 04, 05, 10 and 11 (broad, parties, by script); signatory, qualifying party and operator carry the same register number 20412329.
- Codes: ISIC 1610 (sawmilling), 8411; unit codes ANN, IE; `TendererRoleCode` LEAD and `RoleCode` LEAD mean the same in their two lists; the world's EntitySizeCode thresholds as quoted in F1 (read in `world/codelists/gc/EntitySizeCode.gc`).
- The example contains no amounts, prices or payment data; the parties' tax scheme entries are those of the other examples (money).
- `check_ids.py`: no identifier with a check digit; +999 unassigned; addresses in `.example`.

## Considered and refuted
- `/ExpressionOfInterestRequest/cac:DocumentReference`: an ID only, without saying it is the contract notice — refuted because the ID resolves to the contract notice, the document an expression of interest answers (from broad, logistics).
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact/cbc:JobTitle`: a sales office with a customer service officer as contact in a procedure — refuted because for a small manufacturer the sales office answers public buyers; name, job title and department agree (from broad, parties; merger B refuted Brackenmere's sales contact likewise).
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cac:Party`: the operator names itself as qualifying party — refuted because the qualifying data are the operator's own (from broad; context's remark that an expression of interest does not need them is in F5).
- `/ExpressionOfInterestRequest/cac:ProcurementProject/cbc:Name`: "Park benches" against the contract name of the whole project — refuted, it is lot 1's name and the request is for lot 1 (from context).
- An expression of interest in an open procedure: suspected not to belong — refuted, the definition covers registering the interest of an operator, and the note gives that reason (from context).
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cbc:IndustryClassificationCode`: 1610 against the required 3100 — refuted, that is why the sawmill seeks a bench maker (from context).
- `/ExpressionOfInterestRequest/cbc:ID`: number 0190 continuing the department's 0187–0189 — refuted, each sender's number is its own (from logistics; the out-of-order numbers of one sender are findings of 06 and 18).
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`, `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`, `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`, `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode` — refuted as in 01 (from parties).
- `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Contact`: a sales contact for an operator in a procedure — refuted, the sales office answers tenders for a small manufacturer (from parties).

## Changed in the merge
- broad/F1 (no), parties/F1 (yes) → F1: High, Needs decision yes, aligned with merger B (10, 11): which figure is the sawmill's size is story.
- broad/F2, context/F1, logistics/F2, logistics/F3, parties/F2 → F2: one finding for both locale elements; logistics' separate Medium for `PreferredLanguageLocaleCode` folded in.
- broad/F7, parties/F9 → F3: Low raised to Medium (main table, mergers B, C, D, E).
- logistics/F1 (High), broad/F3 (Low) → F4: Low, Needs decision yes, because whether an expression of interest is a request to participate cannot be settled; both arguments in Why.
- broad/F5, parties/F5 (yes), context/F2, money/F1 (yes) → F5: Needs decision no, because the preferred option (no share, no lead role) keeps the story (a sawmill considering a partner).
- parties/F7 (no) → F7: Needs decision yes, as the main table (`RegistrationDate` 1996-01-01: Low, yes) and mergers B, C, D, E.
- broad/F4, parties/F4 → F6; parties/F6, context/F4 → F8; broad/F8, parties/F8 → F9; broad/F6, parties/F3, context/F3, logistics/F4 → F10: combined, severity unchanged.

## Outside this review
- Whether an expression of interest belongs in an open procedure is a question of the flow's story; see 02/F13 (from broad, context).
