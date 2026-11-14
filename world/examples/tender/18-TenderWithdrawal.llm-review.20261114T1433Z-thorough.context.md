# LLM review: 18-TenderWithdrawal.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/18-TenderWithdrawal.xml`, Git blob `d02ecd959438556075917a15e5b54cd6caa90c26` (committed)
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

### tender/18#F1 · High · "A corrected tender follows", but the corrected tender is dated six hours before the withdrawal
- XPath: `/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`
- XPath: `/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`
- XPath: `/TenderWithdrawal/cbc:IssueTime` = `17:56:00`
- XPath: `19-Tender.xml:/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `19-Tender.xml:/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `19-Tender.xml:/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- XPath: `19-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0205`
- Why: The withdrawal is issued on 2026-02-24 at 17:56 and announces that a corrected tender will follow. The corrected tender (19, `BF-DOC-26-0205`) is issued the same day at 12:10 and speaks of "the withdrawn tender" as already withdrawn. Each document places the other in its future. The terms forbid multiple tenders (`MultipleTendersCode` `NOTALLOWED` in 03), so between 12:10 and 17:56 the operator would also have had two tenders in.
- Condition: The withdrawal is issued before the tender that replaces the withdrawn one (or the note says that the corrected tender has been submitted).
- Options: (a) Preferred: issue the withdrawal on 2026-02-24 before 12:10 (e.g. in the morning). (b) Issue 19 after 17:56.
- Needs decision: no

### tender/18#F2 · Medium · The withdrawal cites a tender receipt that the flow does not contain and that is not numbered like the department's documents
- XPath: `/TenderWithdrawal/cac:TenderNotificationDocumentReference/cbc:ID` = `PWD-RCPT-BF-1`
- XPath: `16-TenderReceipt.xml:/TenderReceipt/cbc:ID` = `LPWD-DOC-26-0202`
- XPath: `16-TenderReceipt.xml:/TenderReceipt/cac:TenderDocumentReference/cbc:ID` = `VI-DOC-26-0201`
- XPath: `/TenderWithdrawal/cac:TenderDocumentReference/cbc:ID` = `BF-DOC-26-0203`
- Why: `TenderNotificationDocumentReference` is "a reference to the Tender Receipt Notification", the department's receipt for the tender being withdrawn. The only tender receipt of the flow is 16, for Valdara's tender; none exists for `BF-DOC-26-0203`. The ID cited, `PWD-RCPT-BF-1`, does not follow the department's document numbering (`LPWD-DOC-26-…`, as the receipt 16 and every other document it issues), so even a reader who assumes an unshown receipt cannot take the ID as the department's.
- Condition: The reference carries the document ID of a tender receipt for the withdrawn tender, in the department's numbering, and that receipt exists in the flow or is plainly an unshown document of that series.
- Options: (a) Preferred: add a tender receipt for 17 to the flow and cite its ID. (b) Use an ID of the department's series for an unshown receipt. (c) Remove the reference.
- Needs decision: yes

### tender/18#F3 · Medium · A language code in `LocaleCode`
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderWithdrawal/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/18#F4 · Low · Customs trader numbers of the parties in a tender withdrawal
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. A withdrawal is not declared to customs. They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- `TenderDocumentReference` `BF-DOC-26-0203` is the tender 17 of the same operator, issued the day before; `WithdrawOfferIndicator` true agrees with the note.
- The reason given (price per bench entered wrongly) agrees with 17 and 19: line 1 is 112800.00 (470.00 per bench) in 17 and 115200.00 (480.00) in 19.
- The withdrawal is dated before the tender deadline (2026-02-26 12:00). GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator` = true in a document whose only purpose is to withdraw: suspected to state the obvious — refuted, the definition gives the element both values ("has to be withdrawn (true) or not (false)"), so the document needs it to say which.
