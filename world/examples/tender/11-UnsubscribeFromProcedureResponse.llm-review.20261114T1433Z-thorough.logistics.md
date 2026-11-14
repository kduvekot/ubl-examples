# LLM review: 11-UnsubscribeFromProcedureResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/11-UnsubscribeFromProcedureResponse.xml`, Git blob `fb12fe4c0c9c9356bb49cf3774522f5fcb156bfb` (committed)
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

### tender/11#F1 · Medium · Language code in LocaleCode
- XPath: `/UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnsubscribeFromProcedureResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- `UnsubscribeToProcedureDocumentReference` `MS-DOC-26-0196` resolves to 10, an unsubscribe request of the same operator, issued 2026-02-22 14:30; this confirmation is issued 2026-02-23 14:48, after it.
- Parties, `ContractFolderID`, the project block and `LOT-1` equal those of 10 (and of 04/05, the registration that ends here); the note states the effect.
- `LPWD-DOC-26-0197` is issued after the department's `-0195` (2026-02-21), in order.

## Considered and refuted
- `/UnsubscribeFromProcedureResponse/cbc:IssueDate`: a confirmation a full day after the request — refuted, no rule of the flow sets a shorter time and 05 also answered the next day.
