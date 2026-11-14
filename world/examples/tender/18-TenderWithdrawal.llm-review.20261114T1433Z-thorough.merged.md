# LLM review: 18-TenderWithdrawal.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/18-TenderWithdrawal.xml`, Git blob `d02ecd959438556075917a15e5b54cd6caa90c26` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/18#F1 · High · "A corrected tender follows", but the corrected tender was issued almost six hours before the withdrawal
- XPath: `/TenderWithdrawal/cbc:Note` = `The price per bench was entered wrongly; a corrected tender follows.`
- XPath: `/TenderWithdrawal/cbc:IssueDate` = `2026-02-24`
- XPath: `/TenderWithdrawal/cbc:IssueTime` = `17:56:00`
- XPath: `/TenderWithdrawal/cbc:ID` = `BF-DOC-26-0204`
- XPath: `19-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0205`
- XPath: `19-Tender.xml:/Tender/cbc:IssueDate` = `2026-02-24`
- XPath: `19-Tender.xml:/Tender/cbc:IssueTime` = `12:10:00`
- XPath: `19-Tender.xml:/Tender/cbc:Note` = `Tender for both lots, with a bench of the furniture maker's own make. It corrects the price per bench of the withdrawn tender.`
- XPath: `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:MultipleTendersCode` = `NOTALLOWED`
- Why: The withdrawal, issued 2026-02-24 17:56, announces a corrected tender for later; the corrected tender 19 was issued the same day at 12:10 (5 h 46 min earlier) and already calls 17 "the withdrawn tender". Each document places the other in its future. The document numbers show the intended order (0204 withdrawal, 0205 tender), so the sender's lower number is issued after the higher one. Between 12:10 and 17:56 Brackenmere also had two tenders in, which the terms exclude. Re-checked in the merge; a tenderer may in practice submit before withdrawing, but then neither note could be true.
- Condition: The withdrawal is issued after 17 and before 19, so that notes, document numbers and issue times agree.
- Options: (a) issue the withdrawal on 2026-02-24 before 12:10 (preferred: the IDs and both notes then agree); (b) issue 19 after 17:56.
- Needs decision: no
- From: broad, logistics, context (parties and money listed it under "Outside this review" as a timeline question; it is a contradiction between this example and 19, so a finding)

### tender/18#F2 · High · Reference to a tender receipt that does not exist in the flow, in a numbering the department does not use
- XPath: `/TenderWithdrawal/cac:TenderNotificationDocumentReference/cbc:ID` = `PWD-RCPT-BF-1`
- XPath: `/TenderWithdrawal/cac:TenderDocumentReference/cbc:ID` = `BF-DOC-26-0203`
- XPath: `16-TenderReceipt.xml:/TenderReceipt/cbc:ID` = `LPWD-DOC-26-0202`
- XPath: `16-TenderReceipt.xml:/TenderReceipt/cac:TenderDocumentReference/cbc:ID` = `VI-DOC-26-0201`
- Why: `TenderNotificationDocumentReference` is "A reference to the Tender Receipt Notification", the department's receipt for the tender being withdrawn. The only tender receipt of the flow is 16, for Valdara's tender (issued the day after this withdrawal); none exists for `BF-DOC-26-0203`, and `PWD-RCPT-BF-1` occurs only here (`grep -rl --include='*.xml' PWD-RCPT`). It does not follow the department's numbering (`LPWD-DOC-26-nnnn`, as 16 and every other document it issues), so it cannot be read as an unshown receipt of that series either. A reference to a document of the flow's own types that does not exist is section 6's High example (as furniture/09's unresolved delivery note); broad (Low) and context (Medium) rated it lower.
- Condition: The reference resolves to a tender receipt for tender 17 in the department's numbering, existing in the flow, or is absent.
- Options: (a) add a tender receipt for 17 (between 2026-02-23 16:37 and the withdrawal) and cite its ID (preferred by all three parts); (b) an ID of the department's series for an unshown receipt; (c) remove the reference.
- Needs decision: yes
- From: broad (Low), logistics (High), context (Medium)

### tender/18#F3 · Medium · Language code in LocaleCode
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TenderWithdrawal/cac:TendererParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, logistics, context

### tender/18#F4 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The Lumeport Public Works Department (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411) carries a liquidation status `ACTIVE` and a registration scheme of type `COMMERCIAL` ("A register of businesses"). A city department is not a business and cannot be in liquidation. Same in all 36 examples of the flow.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) a register type for public bodies; (c) a world rule that public bodies are in the federal business register.
- Needs decision: no
- From: broad, parties

### tender/18#F5 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/TenderWithdrawal/cac:TendererParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1996-01-01 is given for 25 unrelated parties, 271 times in 181 examples (`grep -r --include='*.xml' 'RegistrationDate>1996-01-01'`): a default, not a fact of each company.
- Condition: Each party's registration date is its own, or absent.
- Options: (a) a date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties (needs decision no)

### tender/18#F6 · Low · Customs trader number of the department in a tender withdrawal
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8: the customs trader number identifies the department towards customs (used in 30, 31); a withdrawal declares nothing to customs.
- Condition: Each party carries only the identifiers the document uses.
- Options: (a) leave customs trader numbers to the customs and transport documents (preferred); (b) a stated world rule that every document carries all identifiers.
- Needs decision: no
- From: parties, context

### tender/18#F7 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" describes a transaction; the code `PUBLIC` fits (list description: a public body "buys free of sales tax"); broad would prefer a party-status code. A withdrawal has no tax content at all, so the whole tax scheme is also copied master data.
- Condition: The party's exemption reason states its status.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code; (c) leave the tax scheme out of this document.
- Needs decision: no
- From: broad, parties

## Checked and consistent
- check_ids.py: GLN `9523710900008` has a correct check digit.
- `TenderDocumentReference` `BF-DOC-26-0203` is 17, Brackenmere's tender (2026-02-23 16:37); the withdrawal is before the deadline 2026-02-26 12:00; `WithdrawOfferIndicator` true agrees with the note and the document type; folder, contract name and parties are those of 17; the signatory is the tenderer.
- The reason given agrees with the tenders, recalculated: 112 800.00 / 240 = 470.00 in 17, 115 200.00 / 240 = 480.00 in 19; installation 3 840.00 in both; total 116 640.00 → 119 040.00 (+2 400.00).
- The example contains no amounts, prices, payment data or guarantees (money).

## Considered and refuted
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator`: `true` in a document whose only purpose is withdrawal — refuted, the definition provides for both values, so `true` carries the statement (from broad, logistics, context).
- `/TenderWithdrawal/cbc:WithdrawOfferIndicator`: the withdrawal says nothing about the tender guarantee — refuted, before the deadline a tender may be replaced and the guarantee secures the tender after it (from money).
- `/TenderWithdrawal/cac:TenderDocumentReference/cbc:ID`: "a reference to a received Tender" while the sender is the tenderer — refuted, the tender was received by the party the withdrawal is addressed to (from logistics).
- `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` invalid — refuted, no format prescribed (from parties).
- `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PostalAddress/cbc:InhouseMail`: belongs in `Room` — refuted (from parties).
- `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:Contact/cbc:Name`: functional name, two department wordings — refuted (from parties).
- `/TenderWithdrawal/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: `STATE` vs local authority — refuted, the level of the tax (from parties).
- `/TenderWithdrawal/cac:TendererParty/cac:Contact`: `Trade sales` — refuted, for a small maker the sales office answers tenders (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: kept High; the parties' and money's "Outside this review" entries folded in, because the contradiction is between this example and 19.
- broad/F3 (Low), logistics/F2 (High), context/F2 (Medium) → F2: High/yes, as a reference to a non-existent document of the flow's own types (section 6; furniture b decision for an unresolved delivery note).
- broad/F4, parties/F4 → F4: raised to Medium, as analysis/review-merge-decisions.md and the other tender merges.
- parties/F5 → F5: needs decision yes, as every earlier flow.

## Outside this review
- The department does not confirm the withdrawal in any document, and whether 21 and 23 count Brackenmere's tenders correctly (one withdrawn, one valid) belongs to their reviews (from logistics).
- Whether the fees in 17 and 19 were incurred once or twice; raised with 17 (from money).
