# LLM review: 10-UnsubscribeFromProcedureRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/10-UnsubscribeFromProcedureRequest.xml`, Git blob `77ba312be318d0b7309984f6f48be21161975fc5` (committed)
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

### tender/10#F1 · Medium · Language code in LocaleCode
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/10#F2 · Low · Signature ID with a prefix that fits no party of the document
- XPath: `/UnsubscribeFromProcedureRequest/cac:Signature/cbc:ID` = `HS-SIG-UNS`
- Why: `Signature/ID` is "an identifier for this signature". Every other signature ID of the flow begins with the abbreviation its signatory also uses in its document numbers (`PWD-SIG-…`, `BF-SIG-…`, `VI-SIG-…`, `BLUM-SIG-…`, `BIS-SIG-…`). The sawmill numbers its documents `MS-…` (`/UnsubscribeFromProcedureRequest/cbc:ID` = `MS-DOC-26-0196`), but its two signatures (here and in 04, `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`) begin with `HS`, which matches no party name in the flow.
- Condition: the signature ID is recognisably the sawmill's, consistent with its document numbers.
- Options: (a) `MS-SIG-UNS` (preferred); (b) leave as is if `HS` has a meaning in the world that the XML does not show.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no identifiers with check digits in this example.
- Issued 2026-02-22 14:30, a week after the registration was confirmed (05, 2026-02-15) and before the tender deadline (2026-02-26) and the end of the validity of the expression of interest (2026-02-26 in 04); confirmed by 11 on 2026-02-23, which refers to this request by its ID.
- Parties, `ContractFolderID` `PWD-2026-PARKS`, the project block ("Park benches", SUPPLIES) and `LOT-1` equal those of 04 and 05, so the request unsubscribes from exactly what was registered. The note ("No bench maker joined the sawmill") continues the note of 04.
- `MS-DOC-26-0196` follows the sawmill's `MS-DOC-26-0190` (04) in number and date.

## Considered and refuted
- `/UnsubscribeFromProcedureRequest/cbc:ContractFolderID`: the request names neither the expression of interest (04) nor the confirmation (05) it undoes — refuted because the folder ID, the operator and the lot identify the subscription unambiguously, and the document type offers no dedicated reference for it.
