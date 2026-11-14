# LLM review: 08-ProcurementStatusRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/08-ProcurementStatusRequest.xml`, Git blob `8b0ed73feb4728e9ed11f9a24ad476449b06b7f2` (committed)
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

### tender/08#F1 · Medium · Language code in LocaleCode
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/08#F2 · Low · The project is named differently from the notices and from the document's own contract name
- XPath: `/ProcurementStatusRequest/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatusRequest/cbc:ContractName` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "a name of this procurement project". The project the request asks about is named `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme` in the notices and the call for tenders, and this document's own `ContractName` uses that name. "Park benches for the city parks" occurs only here and in the answer (09). The process is identified unambiguously by `TenderingProcess/ID` and `ContractFolderID`, so this is only an inconsistency of the name.
- Condition: the project name equals the name in the contract notice.
- Options: (a) use the notice's name (preferred); (b) drop the name and rely on the IDs.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit.
- `TenderingProcess/ID` `PWD-2026-PARKS-P` is the process ID of 02, 03, 21 and 24; `ContractFolderID` `PWD-2026-PARKS`; `LOT-1` and `LOT-2` are the two lots of the notice.
- Issued 2026-02-20 15:50: after the end of the period for additional information (2026-02-19 in 02/03), which fits the question ("after the answers to the questions"), and six days before the tender deadline; answered by 09 on 2026-02-21, which refers to this request by its ID `BF-DOC-26-0194`.
- The request states what it wants to know (the note) and identifies the process; nothing its purpose needs is missing.
- Codes: `ProcurementTypeCode` SUPPLIES (world list) resolves.

## Considered and refuted
- `/ProcurementStatusRequest/cbc:IssueDate`: a question about the procedure after the period for additional information requests ended on 2026-02-19 — refuted because a status request asks for the state of the procedure, not for additional information about the procurement.
- `/ProcurementStatusRequest/cbc:ID`: `BF-DOC-26-0194` directly follows Brackenmere's `BF-DOC-26-0193` (07, issued the day before) — refuted, the two numbers are in date order.
