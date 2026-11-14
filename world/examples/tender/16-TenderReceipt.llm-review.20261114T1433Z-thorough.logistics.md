# LLM review: 16-TenderReceipt.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/16-TenderReceipt.xml`, Git blob `358439bdf09247da5f2bd664dc2d3fc8e35e72b0` (committed)
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

### tender/16#F1 · Medium · Language code in LocaleCode
- XPath: `/TenderReceipt/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` (receiver's data) has a correct check digit.
- `TenderDocumentReference` `VI-DOC-26-0201` resolves to 15, the tender of the receiver (Valdara), issued 2026-02-25 09:13. The receipt was registered at 11:42 the same day and issued at 17:47: tender < registration < issue, all before the deadline 2026-02-26 12:00, so "Received on time" holds; "unopened until the opening" agrees with the opening event `OPEN-1` on 2026-02-26 14:00 (02/03).
- `ContractFolderID` and `ContractName` equal those of the tender. `LPWD-DOC-26-0202` follows the department's `-0197` (2026-02-23) in number and date.

## Considered and refuted
- `/TenderReceipt/cbc:RegisteredTime`: by definition "the time … at which the Tender Receipt was created", six hours before the receipt's issue time — refuted because creation before issue is consistent, and the date and time are after the tender's issue time; whether a platform receipt would be sent sooner is not a contradiction.
- `/TenderReceipt/cac:TenderDocumentReference/cbc:ID`: Brackenmere's tenders (17, 19) have no receipt in the flow while 18 refers to one — not a finding of this example; reported with 18.
