# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/22-AwardedNotification.xml`, Git blob `06273957bdbccc6b43bc0afefe91af957c32f85c` (committed)
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

### tender/22#F1 · Low · Additional document reference with only an ID
- XPath: `/AwardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-REPORT-26`
- Why: "A reference to an additional document associated with this document." Neither the element nor the reference says what the document is (no type, description or date), and it is not in the flow (grep for `>PWD-EVAL-REPORT-26<` over `world/examples/**/*.xml`: this example only). Presumably the evaluation report.
- Condition: The reference states what it refers to (`cbc:DocumentType` or `cbc:DocumentDescription`).
- Options: add `cbc:DocumentType` "Evaluation report" (preferred).
- Needs decision: no

### tender/22#F2 · Low · The contract may be formalised on the last day of the appeal period
- XPath: `/AwardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- XPath: `/AwardedNotification/cbc:Note` = `Your tender has won both lots. The contract follows after the standstill period.`
- Why: The appeal period notified to the unsuccessful tenderer runs until and including `23-UnawardedNotification.xml:/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`. The formalisation period starts on that same day, and the performance guarantee is due then too (`/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`), so the contract does not "follow after" the standstill but can coincide with its last day.
- Condition: The formalisation period starts after the last day of the appeal period.
- Options: (a) preferred: formalisation from 2026-03-20; (b) appeal period ending 2026-03-18.
- Needs decision: yes

### tender/22#F3 · Low · Document numbers of the department do not follow the issue times
- XPath: `/AwardedNotification/cbc:ID` = `LPWD-DOC-26-0208`
- XPath: `/AwardedNotification/cbc:IssueTime` = `13:37:00`
- Why: The department's documents carry one running number. This notification (…0208) is issued on 9 March at 13:37, after `23-UnawardedNotification.xml:/UnawardedNotification/cbc:ID` = `LPWD-DOC-26-0209` (9 March, `23-UnawardedNotification.xml:/UnawardedNotification/cbc:IssueTime` = `10:15:00`), and four days before `21-ContractAwardNotice.xml:/ContractAwardNotice/cbc:ID` = `LPWD-DOC-26-0207` (`21-ContractAwardNotice.xml:/ContractAwardNotice/cbc:IssueDate` = `2026-03-13`). A running number assigned at issue would rise with the issue time.
- Condition: Within one issuer's running series, a higher number is not issued before a lower one, or the numbers are not a running series.
- Options: (a) preferred: issue the notification to the winner before the one to the loser and the award notice after both, with numbers in that order; (b) leave, if the numbers are reserved per procedure step.
- Needs decision: no

## Checked and consistent
- No identifiers with check digits (`check_ids.py` reports none).
- Award 9 March 09:30 precedes the issue time 13:37; the qualification response (3 March) precedes the award; the tender (25 February, valid 90 days) is still valid.
- Contract validity from 2026-03-23, 24 MON: ends 2028-03-22, the planned period of the call for tenders; the first order (`26-Order.xml`, 23 March) falls on the first day.
- Awarded lots LOT-1 and LOT-2 and amount 124080.00 are those of `15-Tender.xml`; "ten years of warranty on the coating" is that tender's response to AC-2.
- Subcontract: 4320.00 / 240 = 18.00 per bench, as the text says; 4320.00 / 124080.00 = 3.48 %, stated as 3.5. Guarantee: 5 % of 124080.00 = 6204.00.
- `cac:MinutesDocumentReference` PWD-MIN-AWARD-26 is the same in 21, 22 and 23; AwardID is the same in 21–24.
- Codes TenderResultCode AWARDED, ContractTypeCode FRAMEWORK, GuaranteeTypeCode PERFORMANCE: in their lists and fitting.

## Considered and refuted
- `/AwardedNotification/cac:TenderResult/cac:Contract/cbc:ID`: `PWD-2026-PARKS` equals `cbc:ContractFolderID` and the procurement project ID — refuted: nothing forbids numbering the contract like the file, and order, invoice and debit note cite the contract under this number consistently. (The separate number `PWD-CONTRACT-2026-PARKS` in `24-TenderContract.xml` is a finding there.)
- `/AwardedNotification`: no reference to the tender that won (`VI-DOC-26-0201`) — refuted: the document type has no element for it; receiver, lots and amount identify it.
- `/AwardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:EndDate`: 22 March is a day before the contract starts — refuted: consistent (formalised before it takes effect).

## Outside this review
- The performance guarantee asked here (due 19 March) has no document in the flow; `14-GuaranteeCertificate.xml` is the tender guarantee.
- The call for tenders announces an electronic auction after the evaluation; no document of the flow shows it, and the awarded amount equals the tendered amount (see 21).
