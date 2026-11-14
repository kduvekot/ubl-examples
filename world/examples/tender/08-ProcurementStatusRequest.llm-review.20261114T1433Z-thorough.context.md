# LLM review: 08-ProcurementStatusRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/08#F1 · Medium · A language code in `LocaleCode`
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/08#F2 · Low · The project is named "… for the city parks" here and "… for the parks renewal programme" everywhere else
- XPath: `/ProcurementStatusRequest/cac:ProcurementProject/cbc:Name` = `Park benches for the city parks`
- XPath: `/ProcurementStatusRequest/cbc:ContractName` = `Park benches for the parks renewal programme`
- XPath: `02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cbc:Name` = `Park benches for the parks renewal programme`
- Why: `ProcurementProject/Name` is "a name of this procurement project". The notices name the project "Park benches for the parks renewal programme", and this document uses that name itself as `ContractName`. Its `ProcurementProject` has another name, which occurs only in 08, 09 and 24 (`grep -c "Park benches for the city parks" world/examples/tender/*.xml`). A reader matching the status exchange to a procedure by name finds two names for one project in one document.
- Condition: The project has the same name in `ProcurementProject/Name` as in the notices (or the name of the lot, where the document is about one lot).
- Options: (a) Preferred: use the name of the notices. (b) None other seen.
- Needs decision: no

### tender/08#F3 · Low · Customs trader numbers of the parties in a status request
- XPath: `/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in a question about a deadline is declared to customs. They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `TenderingProcess/ID` `PWD-2026-PARKS-P` is the process ID of 02 and 03; folder, contract name and both lots agree with the notices.
- The question ("Does the deadline stand after the answers to the questions?") fits the date: 2026-02-20, the day after the period for requesting additional information ended (02: 2026-02-19), and it is answered by 09, which refers back to this document.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/ProcurementStatusRequest/cac:ProcurementProjectLot[2]`: the operator only tenders for lot 1 (06, 07, 17), so naming lot 2 was suspected to be superfluous — refuted, the deadline it asks about is that of the whole procedure.
