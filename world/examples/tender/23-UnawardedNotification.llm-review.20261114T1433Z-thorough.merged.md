# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/23-UnawardedNotification.xml`, Git blob `39a6b648377d44e8a82177e1c91a57309cca5cc5` (committed)
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

### tender/23#F1 · Medium · Language code in LocaleCode
- XPath: `/UnawardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (`listID="ISO 639"`) repeats the language of `cbc:ID` and names no locale. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `cbc:LocaleCode` holds a bare language code.
- Options: (a) remove `cbc:LocaleCode` (preferred by parties and context); (b) a locale such as `en-XB` from a locale list (preferred by broad).
- Needs decision: no
- From: broad, parties, context

### tender/23#F2 · Medium · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The sender is a city department (ISIC 8411). A liquidation status has no meaning for it and a scheme of type `COMMERCIAL` ("A register of businesses") does not fit; the register number itself is not questioned.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the liquidation status and the `COMMERCIAL` type (preferred); (b) reduce the legal entity to registration name and identifier.
- Needs decision: no
- From: broad, parties, context

### tender/23#F3 · Low · The contract may be formalised on the last day on which an appeal can still be presented
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cbc:Note` = `Your tender has won both lots. The contract follows after the standstill period.`
- XPath: `24-TenderContract.xml:/TenderContract/cbc:IssueDate` = `2026-03-19`
- Why: The period "during which an appeal can be presented" includes 2026-03-19; the formalisation period starts the same day in the same document, and the contract is in fact signed then (24, 17:24), while 22 promises the contract "after the standstill period". On that day Brackenmere may still appeal and the contract may already be signed. Same as 22#F5.
- Condition: The formalisation period starts after the last day of the appeal period, or the appeal period ends before it.
- Options: (a) formalisation from 2026-03-20, the contract dated accordingly (preferred: keeps "ten days"); (b) appeal period to 2026-03-18, if "within ten days" counts the day of the award.
- Needs decision: yes
- From: broad, logistics (needs decision yes); context listed it under "Outside this review"

### tender/23#F4 · Low · The review board as information party, receiver and mediator of the appeal
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: `MediationParty` is "The Party who mediates any appeal", `AppealReceiverParty` "The Party who receives the appeal". Mediation is done by someone other than the deciding body; the description names one step ("goes to the review board"), and nothing in the flow says the board mediates. The same as in 02 and 20.
- Condition: `MediationParty` is present only if the procedure has mediation, with the body that mediates; `AppealInformationParty` only where it adds something to the receiver.
- Options: (a) keep `AppealReceiverParty` only (preferred); (b) name a separate mediation body and describe the step.
- Needs decision: yes
- From: broad, parties, context

### tender/23#F5 · Low · The party to appeal to cannot be reached from this document
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cbc:Description` = `An appeal against the decision goes to the review board within ten days.`
- XPath: `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:ElectronicMail` = `registry@review-xb.example`
- Why: For the one tenderer who has reason to appeal, the notification gives the board by register number and name only, while the notices carry its address and contact (21). Low because the board can be looked up by its number.
- Condition: The appeal receiver carries at least a postal or electronic address, as in the notices.
- Options: (a) describe the receiver as in 21 (preferred); (b) at least its electronic address and contact.
- Needs decision: no
- From: parties, broad (in its mediator finding)

### tender/23#F6 · Low · The winner's subcontractor and subcontract price are told to the losing competitor
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- Why: An unawarded notification is "A document communicating to a tenderer that the contract has been awarded to different tenderer"; the receiver needs the result, the winner, the reasons and its remedies, which are there. The tender result is a full copy of the winner's (22), including whom the winner subcontracts to and at what unit price, which by common procurement practice (own knowledge: confidentiality of tenders) would not be told individually (context). Counter-arguments (broad, money, parties, refuted): the same terms are published in the award notice (21), so nothing confidential is added, and naming the winner is the document's purpose. Whether the world's law makes subcontract terms public decides it.
- Condition: The tender result sent to an unsuccessful tenderer carries the winner and what explains the decision, and terms between the winner and its subcontractor only if the law makes them public.
- Options: (a) leave `SubcontractTerms` out of this notification (preferred by context); (b) keep them and record that the world's law makes them public (as 21 does).
- Needs decision: yes
- From: context (broad, money and parties refuted it)

### tender/23#F7 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted". Recalculated: 4 320.00 / 124 080.00 = 3.4816 %; 3.5 % of 124 080.00 is 4 342.80. Same as 21#F15 and 22#F7 (broad and context refuted it in 21 as rounding and a legitimate reading in a result).
- Condition: `Rate` × awarded amount / 100 equals `Amount`, or the rate is absent.
- Options: (a) drop `Rate` (preferred); (b) more decimals.
- Needs decision: no
- From: money

### tender/23#F8 · Low · Registration date 1 January 1996 shared by 25 parties
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 1996-01-01 is given for 25 unrelated companies, 271 times in 181 examples (`grep -r --include='*.xml' 'RegistrationDate>1996-01-01'`): a default, not a fact of Brackenmere.
- Condition: Each company's registration date is its own, or absent.
- Options: (a) a date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties (needs decision no)

### tender/23#F9 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/cbc:ExemptionReason` is "A reason for the party's exemption from tax": the party's status; the text begins with a transaction. Counter-argument (broad, refuted): the text states the status. Kept as in 15–22; the code fits (list description: a public body "buys free of sales tax"). A notification without tax content also does not need the tax scheme.
- Condition: The party's exemption reason states its status only.
- Options: (a) reword the text, keeping the code (preferred); (b) a party-status code; (c) leave the tax scheme out here.
- Needs decision: no
- From: parties (broad refuted it; context listed it under "Outside this review")

### tender/23#F10 · Low · Customs trader number of the department in an unawarded notification
- XPath: `/UnawardedNotification/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: Section 4.8: the customs trader number identifies the department towards customs (used in 30, 31); this notification declares nothing to customs. Added by the merge, as parties and context raised it in 15–18.
- Condition: The party carries only the identifiers the document uses.
- Options: (a) leave customs trader numbers to the customs and transport documents (preferred).
- Needs decision: no
- From: merge

### tender/23#F11 · Low · Additional document reference with only an ID
- XPath: `/UnawardedNotification/cac:AdditionalDocumentReference/cbc:ID` = `PWD-EVAL-SCORES-BF`
- Why: "A reference to an additional document associated with this document." Nothing says what the document is, and it is not in the flow; from the ID it is presumably the score sheet of Brackenmere's tender, which the receiver needs to decide about an appeal. Counter-argument (context, refuted for its lens): a non-UBL annex, as the element allows; that answers whether it may be outside the flow, not whether the reference says what it is. Kept as the earlier flows' decision on ID-only references.
- Condition: The reference states what it refers to.
- Options: (a) add `cbc:DocumentType` "Evaluation scores of the tender" (preferred).
- Needs decision: no
- From: logistics (context refuted it)

## Checked and consistent
- The note against the tenders: Brackenmere's tender 19 is 119 040.00 against Valdara's 124 080.00 (lower in price) and offers 6 years against 10 on AC-2; with the call's formula (60 × lowest / tendered) Brackenmere scores 60.00 and Valdara 60 × 119 040 / 124 080 = 57.56 on price, so Valdara needs a quality lead above 2.44 of 40 points, which 10 against 6 years can give; with two tenders, "ranked second" follows.
- Tender result identical to 21 and 22 (award `PWD-2026-PARKS-AWARD-1`, 2026-03-09 09:30, both lots to Valdara, 124 080.00, contract from 2026-03-23 for 24 months); minutes `PWD-MIN-AWARD-26` as in 21 and 22; codes AWARDED and FRAMEWORK in their lists.
- Appeal period 2026-03-09 to 2026-03-19 is ten days from the award, as the text and the call say; issue 10:15 after the award 09:30.
- No `FinalFinancialGuarantee`, correctly: the receiver is not the winner (money).
- Receiver is the tenderer of 19 (register 20412466, GLN 9523710900008, check digit correct), described as there; winner Valdara as in 21 and 22; sender and signatory the department (parties).

## Considered and refuted
- `/UnawardedNotification/cac:TenderResult/cbc:TenderResultCode`: AWARDED in a notification of not being awarded — refuted, the result of the procedure (from broad, logistics, context).
- `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description`: the winner's subcontracting price disclosed to the loser — refuted, the same data is published in 21 (from broad; and money for `SubcontractTerms/cbc:Amount`; the merge keeps context's finding F6 with needs decision yes).
- `/UnawardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: the winner's total told to the loser — refuted, published in 21 and needed to judge an appeal (from money, context).
- `/UnawardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name`: a sales desk as receiver of the decision — refuted, the contact Brackenmere gave in its tender (from broad).
- `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like — refuted, the text states the status (from broad; the merge keeps F9).
- `/UnawardedNotification/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset`: `-1` malformed — refuted (from parties).
- `/UnawardedNotification/cac:SenderParty/cac:Contact/cbc:Telephone`: +999 real — refuted, unassigned (from parties).
- `/UnawardedNotification/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID`: a real GLN — refuted, prefix 952 is for examples (from parties).
- `/UnawardedNotification/cac:TenderResult/cac:WinningParty/cac:Party/cac:PartyName/cbc:Name`: naming the winner to the loser — refuted, the purpose of the document (from parties).
- `/UnawardedNotification/cac:TenderResult/cac:Contract/cbc:ID`: equals the folder ID — refuted, numbered like the file and used consistently (from logistics).
- `/UnawardedNotification/cbc:ID`: …0209 issued before …0208 — kept as a finding of 22 (22#F6) (from logistics).
- `/UnawardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod`: the winner's formalisation period in the loser's notification — refuted, it tells the receiver until when the contract is not concluded (from context).
- `/UnawardedNotification/cac:AdditionalDocumentReference/cbc:ID`: not an example — refuted, a non-UBL annex (from context; the merge keeps F11).

## Changed in the merge
- broad/F4, parties/F3, context/F4 → F2: raised to Medium, as analysis/review-merge-decisions.md and the other tender merges.
- logistics/F2 (needs decision yes), broad/F2 (no) → F3: yes, as 22#F5 and merger D (24): whether the end date is inclusive cannot be read from the XML.
- broad/F3 split: the mediator part with parties/F6 and context/F3 → F4; the reachability part with parties/F5 → F5.
- parties/F4 → F8: needs decision yes, as every earlier flow.
- F10 added by the merge (customs trader number), as raised by parties and context in 15–18.

## Outside this review
- The note says the warranty "scored lower"; Brackenmere's tender 19 itself states five years on the line and six in the criterion response (19#F3) (from broad).
