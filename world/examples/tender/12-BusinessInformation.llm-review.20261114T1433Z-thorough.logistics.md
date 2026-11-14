# LLM review: 12-BusinessInformation.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/12-BusinessInformation.xml`, Git blob `0bf87195abba0708389105425a425c36428e3dc5` (committed)
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

### tender/12#F1 · Medium · OperationType holds the company's line of business, not the operation the document performs
- XPath: `/BusinessInformation/cac:OperationType/cbc:Code` = `MANUFACTURE`
- XPath: `/BusinessInformation/cac:OperationType/cbc:Description` = `Manufacture of furniture for public spaces.`
- Why: `OperationType` is "the type of operation for which this document is created", and its `Code` is "a code to specify the type of operation (e.g. deletion)": the operation on the registration information that the document carries out (registration, update, deletion, extract). The value describes what Valdara does as a business. That activity is already stated by the party's industry classification (ISIC 3100) and by `BusinessCapability`; what this document is created for is stated in `NoticeSubType` (register extract).
- Condition: `OperationType` states an operation on the business registration information, from a list of such operations, or is absent.
- Options: (a) remove `OperationType`, since `NoticeSubType` `EXTRACT` already says what the document is (preferred); (b) use a code meaning "extract" or "consultation" from a list of register operations.
- Needs decision: no

### tender/12#F2 · Medium · Language code in LocaleCode
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/12#F3 · Low · Capability figures that cannot be reconciled with the operator's own qualification
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- Why: the register extract measures Valdara's production capability as 6000 EA and 4,800,000.00 XBL, without saying per what period or what the amount is. Valdara's own qualification document, issued two days earlier, states `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000` ("4,000 benches a year") and a financial capability of `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`. If both quantities are yearly bench output they contradict each other (6000 against 4000); if they measure different things, the extract does not say which. The department receives this extract "for the evaluation" and has to compare the two.
- Condition: the capability's description says what the quantity and the amount measure (unit of time, kind of amount), and the figures agree with 13 where they measure the same thing.
- Options: (a) state the measure in `Description` (e.g. "installed capacity 6,000 benches a year; production value 2025") and align with 13 (preferred); (b) drop the figures from the register extract.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit.
- Issued 2026-02-27 16:26, the day after the tender opening (2026-02-26 14:00), which fits "for the evaluation"; `RequestedPublicationDate` 2026-02-27 is the issue date, not before it. The capability's `ValidityPeriod` ends 2026-12-31, after the issue date.
- Sender (register 20410959) is the Bayvarra Information Service that receives the notices 01, 02 and 21; receiver is the department; the business party's identifiers (`XU-R-104274`, `0990:10427`, `XU-TR-104274`) equal those of Valdara in 03, 13 and 15.
- `BusinessPartyGroup`: the two members (`XU-R-104274` Valdara, `20412466` Brackenmere) are the two operators that tender in the flow (15; 17/19), and both carry ISIC 3100, as the group type says.
- Codes: `NoticeTypeCode` BUSREG, `NoticeSubType` EXTRACT, `CapabilityTypeCode` PRODUCTION, `WebSiteTypeCode` COMPANY, `ServiceTypeCode` LOGISTICS resolve in the world lists; language codes en, qau; unit code EA.

## Considered and refuted
- `/BusinessInformation/cac:BrochureDocumentReference/cbc:ID`: reference with only an ID — refuted because the element itself says what the document is (a company brochure).
- `/BusinessInformation/cac:AdditionalDocumentReference/cbc:ID`: `VI-ISO9001-CERT` with only an ID — refuted because the ID names the document (an ISO 9001 certificate) well enough for a reader; no example needs to resolve it.
- `/BusinessInformation/cbc:ID`: `BIS-DOC-26-0198` is lower than numbers of documents issued earlier (0199 to 0205, 2026-02-23 to 2026-02-25) — refuted because those are other senders' series; the information service has no other document in the flow.
- `/BusinessInformation/cbc:IssueDate`: the extract has no reference to the procedure (no `ContractFolderID`) — refuted because the document type has no such element and the business party group names the procedure in text.
