# LLM review: 05-ExpressionOfInterestResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/05-ExpressionOfInterestResponse.xml`, Git blob `3fc9021a423cb516bf42fbd92205840f2d256f11` (committed)
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

### tender/05#F1 · High · Registration confirmed for a request that came after the period the contract notice sets
- XPath: `/ExpressionOfInterestResponse/cac:ExpressionOfInterestDocumentReference/cbc:ID` = `MS-DOC-26-0190`
- XPath: `/ExpressionOfInterestResponse/cbc:Note` = `Registered: the sawmill receives every change to the documents.`
- Why: the response confirms the expression of interest `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:IssueDate` = `2026-02-14`. The department's own contract notice ends the period for requests to participate on `02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:ParticipationRequestReceptionPeriod/cbc:EndDate` = `2026-02-11` (same in 03). The department thus accepts without comment a request that its notice says is three days late; one of the two statements is wrong. (The notice's periods are reported with 02 and 03.)
- Condition: the request this response confirms lies inside the period the notice sets for it, or the notice sets no such period.
- Options: (a) resolve in 02/03 by dropping or moving the reception period (preferred); (b) move 04 and this response before 2026-02-11.
- Needs decision: yes

### tender/05#F2 · Medium · Language code in LocaleCode
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- `ExpressionOfInterestDocumentReference` `MS-DOC-26-0190` resolves to 04, an expression of interest request, issued 2026-02-14 14:05; this response is issued 2026-02-15 08:35, after it. Parties, `ContractFolderID`, `ContractName`, project block and `LOT-1` equal those of 04.
- `TenderLanguageLocaleCode` `en`: the definition here is "a code signifying the language required for the tender", so a language code fits (unlike `LocaleCode`); it agrees with the notice language `en` of 02.
- Codes: ISIC 1610, 8411; world-list codes resolve.

## Considered and refuted
- `/ExpressionOfInterestResponse/cbc:TenderLanguageLocaleCode`: language code in an element named "locale" — refuted because the UBL definition of this element asks for the language required for the tender.
- `/ExpressionOfInterestResponse/cbc:ID`: `LPWD-DOC-26-0191` is issued two days after the department's `LPWD-DOC-26-0192` (06, 2026-02-13) — kept out of this example; reported as a finding of 06, the document whose number is ahead of its date.
