# LLM review: 10-UnsubscribeFromProcedureRequest.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/10#F1 · Medium · A language code in `LocaleCode`
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/10#F2 · Low · Signature ID with the prefix "HS" in a document of the sender "MS"
- XPath: `/UnsubscribeFromProcedureRequest/cac:Signature/cbc:ID` = `HS-SIG-UNS`
- XPath: `/UnsubscribeFromProcedureRequest/cbc:ID` = `MS-DOC-26-0196`
- XPath: `04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`
- Why: Every other signature of the flow is numbered with the prefix its party uses for its documents (PWD, BF, VI, BIS, BLUM). Marrowdale Sawmill numbers its documents `MS-…` but its two signatures `HS-…`; the prefix matches no name in the document and looks left over from another party name.
- Condition: The signature ID uses the same party prefix as the sawmill's other identifiers, or the prefix is explained.
- Options: (a) Preferred: `MS-SIG-UNS` (and `MS-SIG-EOI` in 04). (b) None other seen.
- Needs decision: no

### tender/10#F3 · Low · Customs trader numbers of the parties in an unsubscribe request
- XPath: `/UnsubscribeFromProcedureRequest/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/UnsubscribeFromProcedureRequest/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing here is declared to customs, and the sawmill never ships anything in this flow. They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- The note ("No bench maker joined the sawmill; it will not tender.") follows from 04, where the sawmill considered a tender with a bench maker; project name, type and lot are those of 04 and 05.
- The request is dated after the registration (05, 2026-02-15) and before the tender deadline (2026-02-26); 11 confirms it and refers to it by its ID.

## Considered and refuted
- The request does not refer to the expression of interest (04) or its confirmation (05): suspected missing link — refuted, the document type has the procedure (folder, project, lot) as its subject and the operator is identified; the model defines no reference to the expression of interest here.
