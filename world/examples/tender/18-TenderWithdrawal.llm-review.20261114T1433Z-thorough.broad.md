# LLM review: 18-TenderWithdrawal.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/18-TenderWithdrawal.xml`, Git blob `d02ecd959438556075917a15e5b54cd6caa90c26` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit e0e5001 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/18#F1 · High · "A corrected tender follows", but the corrected tender was issued before the withdrawal
- XPath: `/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`
- XPath: `/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`
- XPath: `/TenderWithdrawal/cbc:IssueTime` = `17:56:00`
- XPath: `19-Tender.xml:/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `19-Tender.xml:/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `19-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0205`
- Why: The withdrawal is issued on 2026-02-24 at 17:56 and announces a corrected tender. The corrected tender, 19 (`BF-DOC-26-0205`, whose note calls 17 "the withdrawn tender"), is issued the same day at 12:10, almost six hours earlier. Between 12:10 and 17:56 Brackenmere had two tenders in the procedure, which the tendering terms forbid (`02-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`), and the document numbers run the other way too (withdrawal 0204, tender 0205).
- Condition: The withdrawal precedes the corrected tender (or the note says the corrected tender has been submitted).
- Options: (a) issue the withdrawal before 19, e.g. in the morning of 2026-02-24 (preferred: IDs and both notes then agree); (b) issue 19 after 17:56.
- Needs decision: no

### tender/18#F2 · Medium · Language code in LocaleCode
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderWithdrawal/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/18#F3 · Low · Reference to a tender receipt that no document carries, in another numbering than the department's
- XPath: `/TenderWithdrawal/cac:TenderNotificationDocumentReference/cbc:ID` = `PWD-RCPT-BF-1`
- XPath: `16-TenderReceipt.xml:/TenderReceipt/cbc:ID` = `LPWD-DOC-26-0202`
- Why: TenderNotificationDocumentReference is "A reference to the Tender Receipt Notification." The flow contains no receipt for Brackenmere's tender 17, and the only receipt of the department (16, for Valdara) is numbered `LPWD-DOC-26-0202`, as all documents of the department are; `PWD-RCPT-BF-1` does not follow that numbering.
- Condition: The reference carries the ID of a receipt as the department numbers them; ideally that receipt exists in the flow.
- Options: (a) add the receipt for 17 to the flow and use its ID (preferred); (b) at least an ID in the department's numbering.
- Needs decision: yes

### tender/18#F4 · Low · A public body described as a company in a commercial register
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/18#F5 · Low · The department's tax exemption reason describes a sale
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit.
- TenderDocumentReference `BF-DOC-26-0203` is the ID of 17-Tender.xml (2026-02-23 16:37), by the same tenderer; the withdrawal is before the tender deadline 2026-02-26 12:00; WithdrawOfferIndicator `true` agrees with the note.
- The reason given ("The price per bench was entered wrongly") agrees with the tenders: 470.00 a bench in 17 (112 800.00 / 240), 480.00 in 19 (115 200.00 / 240), everything else unchanged.
- Folder, contract name and parties are those of 17; signatory is the tenderer.

## Considered and refuted
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator`: an indicator `true` in a document whose only purpose is withdrawal — refuted because the definition provides for both values and `true` is the statement the document makes.
