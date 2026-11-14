# LLM review: 18-TenderWithdrawal.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/18-TenderWithdrawal.xml`, Git blob `d02ecd959438556075917a15e5b54cd6caa90c26` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/18#F1 · High · "A corrected tender follows", but the corrected tender was issued almost six hours before this withdrawal
- XPath: `/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`
- XPath: `/TenderWithdrawal/cbc:IssueTime` = `17:56:00`
- XPath: `/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`
- XPath: `/TenderWithdrawal/cbc:ID` = `BF-DOC-26-0204`
- Why: the withdrawal announces a corrected tender for later. The corrected tender is `19-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0205`, issued on `19-Tender.xml:/Tender/cbc:IssueDate` = `2026-02-24` at `19-Tender.xml:/Tender/cbc:IssueTime` = `12:10:00`, i.e. 5 hours 46 minutes before this withdrawal, and its own note already speaks of "the withdrawn tender". The two documents contradict each other on the order of events. The document numbers show the intended order (0204 withdrawal, then 0205 tender), so a lower number of the same sender is issued after a higher one. For six hours Brackenmere also had two live tenders, which the tendering terms exclude (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`).
- Condition: the withdrawal is issued before the corrected tender (and after the withdrawn one), so that note, document numbers and issue times agree.
- Options: (a) issue the withdrawal before 2026-02-24 12:10, e.g. in the morning (preferred, 17 is of 2026-02-23 16:37); (b) issue 19 after 17:56.
- Needs decision: no

### tender/18#F2 · High · Reference to a tender receipt that does not exist in the flow
- XPath: `/TenderWithdrawal/cac:TenderNotificationDocumentReference/cbc:ID` = `PWD-RCPT-BF-1`
- Why: the element is "a reference to the Tender Receipt Notification", the department's receipt for the tender being withdrawn (`/TenderWithdrawal/cac:TenderDocumentReference/cbc:ID` = `BF-DOC-26-0203`). The flow has one tender receipt, 16, for Valdara's tender, with the ID `16-TenderReceipt.xml:/TenderReceipt/cbc:ID` = `LPWD-DOC-26-0202` (issued the day after this withdrawal). No receipt for Brackenmere's tender exists, and `PWD-RCPT-BF-1` occurs only here (`grep -l` over `world/examples/*/*.xml`); it also does not follow the pattern of the department's document numbers (`LPWD-DOC-26-nnnn`), under which such a receipt would be issued.
- Condition: the reference resolves to a tender receipt for tender 17 that exists in the flow, or is absent.
- Options: (a) add a tender receipt for 17 to the flow (between 2026-02-23 16:37 and this withdrawal) and refer to its ID (preferred if the flow is to show the receipt for every tender); (b) remove the reference.
- Needs decision: yes

### tender/18#F3 · Medium · Language code in LocaleCode
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderWithdrawal/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: GLN `9523710900008` has a correct check digit.
- `TenderDocumentReference` `BF-DOC-26-0203` resolves to 17, a tender of the same tenderer (Brackenmere), issued 2026-02-23 16:37, before this withdrawal; the withdrawal is before the deadline 2026-02-26 12:00, when tenders can still be withdrawn.
- `WithdrawOfferIndicator` true agrees with the note and with the document type; `ContractFolderID` and `ContractName` equal those of the tender.
- The reason given (price per bench entered wrongly) agrees with the tenders: 112800.00 / 240 = 470.00 in 17 against 115200.00 / 240 = 480.00 in 19.

## Considered and refuted
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator`: redundant in a document whose only purpose is withdrawal — refuted, the definition foresees the value false as well, so stating true carries information.
- `/TenderWithdrawal/cac:TenderDocumentReference/cbc:ID`: element defined as "a reference to a received Tender" although the withdrawing party is the sender of that tender — refuted, the tender was received by the contracting party the withdrawal is addressed to.

## Outside this review
- The department does not confirm the withdrawal in any document of the flow, and the unawarded notification (23) and the award notice (21) lie in the other part; whether they count Brackenmere's tenders correctly (one withdrawn, one valid) belongs to their reviews.
