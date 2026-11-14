# LLM review: 04-ExpressionOfInterestRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/04-ExpressionOfInterestRequest.xml`, Git blob `1ca94275bd6d396987ad7aa46080a104842bb2c3` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/04#F1 · High · Expression of interest issued after the period the contract notice sets for it
- XPath: `/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`
- XPath: `/ExpressionOfInterestRequest/cac:DocumentReference/cbc:ID` = `LPWD-DOC-26-0188`
- Why: the request refers to the contract notice (02). That notice sets `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11` as the end of "the period during which requests for participation must be completed and delivered" (the same date is in 03). An expression of interest is the request by which an operator asks to take part; this one is issued three days after that period ended, and is nevertheless registered in 05. The two documents contradict each other on whether the request is in time. (That the notice's periods are themselves questionable is reported with 02 and 03.)
- Condition: the request's issue date lies inside the period the notice sets for such requests, or the notice sets no such period.
- Options: (a) resolve together with the periods of 02/03: drop or move the reception period there (preferred, since the notice's dates are the outliers); (b) issue this request on or before 2026-02-11, which is the notice's own issue date and hardly leaves time.
- Needs decision: yes

### tender/04#F2 · Medium · Language code in PreferredLanguageLocaleCode
- XPath: `/ExpressionOfInterestRequest/cbc:PreferredLanguageLocaleCode` = `en`
- Why: the element is "a code signifying the locale in which the language in the required documents is preferred". The value is a language code from ISO 639 (`listID` "ISO 639"), not a locale; it says which language is preferred, not which regional variant. This is the same misuse as in `LocaleCode` (next finding). The response (05) uses `TenderLanguageLocaleCode`, whose definition does ask for a language.
- Condition: the element holds a locale, or the preferred language is stated in an element defined for a language.
- Options: (a) use a locale value such as a language-country pair from a locale list (preferred if the element is kept); (b) remove the element and state the preferred language in the note.
- Needs decision: no

### tender/04#F3 · Medium · Language code in LocaleCode
- XPath: `/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/04#F4 · Low · Signature ID with a prefix that fits no party of the document
- XPath: `/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- Why: `Signature/ID` is "an identifier for this signature". Every other signature ID of the flow begins with the abbreviation its signatory also uses in its document numbers (`PWD-SIG-…` for the department, `BF-SIG-…`, `VI-SIG-…`, `BLUM-SIG-…`, `BIS-SIG-…`). The sawmill numbers its documents `MS-…` (`/ExpressionOfInterestRequest/cbc:ID` = `MS-DOC-26-0190`), but its two signatures (here and in 10) begin with `HS`, which matches no party name in the flow. It looks like a leftover of another name.
- Condition: the signature ID is recognisably the sawmill's, consistent with its document numbers.
- Options: (a) `MS-SIG-EOI` (preferred); (b) leave as is if `HS` has a meaning in the world (it is not visible in the XML).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- `DocumentReference` `LPWD-DOC-26-0188` resolves to the contract notice (02), issued 2026-02-11, three days before this request; it is the notice an expression of interest answers.
- `ContractFolderID` `PWD-2026-PARKS` and `ContractName` equal the notice's folder ID and project name; `ProcurementProjectLotReference` `LOT-1` is the bench lot, and the project block ("Park benches", SUPPLIES) is lot 1 as described in 02.
- `ValidityPeriod/EndDate` 2026-02-26 is the tender deadline of 02/03, after the issue date.
- 05 answers this request by its ID `MS-DOC-26-0190` the next morning (2026-02-15 08:35); 10 withdraws the registration on 2026-02-22, within the validity period.
- Codes: ISIC 1610 (sawmilling), 8411; unit codes ANN, IE; `TendererRoleCode` LEAD and `RoleCode` LEAD have the same meaning in their two lists.

## Considered and refuted
- `/ExpressionOfInterestRequest/cac:DocumentReference/cbc:ID`: generic reference with only an ID — refuted because the ID resolves to the contract notice, the document an expression of interest naturally refers to.
- `/ExpressionOfInterestRequest/cbc:ID`: the number 0190 continues the department's numbers 0187 to 0189 although another party assigns it — refuted as a finding of this example: each sender's number is its own, and a sawmill's 190th document of the year in mid-February is not implausible. The numbering across the flow is noted under 06 and 18, where numbers of one sender are out of order.
