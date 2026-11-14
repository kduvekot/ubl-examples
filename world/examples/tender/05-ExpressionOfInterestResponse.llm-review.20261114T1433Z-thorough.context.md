# LLM review: 05-ExpressionOfInterestResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/05#F1 · Medium · A language code in `LocaleCode`
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/05#F2 · Low · Issued by the department on a Sunday morning, outside the hours its contact states
- XPath: `/ExpressionOfInterestResponse/cbc:IssueDate` = `2026-02-15`
- XPath: `/ExpressionOfInterestResponse/cbc:IssueTime` = `08:35:00`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/ExpressionOfInterestResponse/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: 2026-02-15 is a Sunday (1 January 2026 is a Thursday; my own calculation, assuming the world uses the common calendar as its dates suggest). The procurement office that signs this confirmation states in the same document that it is reachable on weekdays from 08:00 to 17:00. A signed reply of a public office at 08:35 on a Sunday needs an explanation (an automatic confirmation of the platform would not be "signed" by the office).
- Condition: The issue date and time of a document signed by the procurement office fall within its working days, or the document says that it is generated automatically.
- Options: (a) Preferred: issue it on Monday 2026-02-16. (b) Say in the note that the platform registers and confirms automatically.
- Needs decision: no

### tender/05#F3 · Low · Customs trader numbers of the parties in a confirmation of interest
- XPath: `/ExpressionOfInterestResponse/cac:EconomicOperatorParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412329`
- XPath: `/ExpressionOfInterestResponse/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `ExpressionOfInterestDocumentReference` `MS-DOC-26-0190` is 04, issued the day before; operator, contracting party, contract name, project name and lot agree with it.
- The note ("Registered: the sawmill receives every change to the documents.") is what the document type is for ("to inform the Economic Operator he has been registered as an interested party").

## Considered and refuted
- `/ExpressionOfInterestResponse/cbc:TenderLanguageLocaleCode` = `en`: suspected language code in a locale element, as `LocaleCode` — refuted, the definition of this element is "a code signifying the language required for the tender"; a language code fits it despite the element name.
