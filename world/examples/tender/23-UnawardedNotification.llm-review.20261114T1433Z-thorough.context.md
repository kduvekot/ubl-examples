# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/23-UnawardedNotification.xml`, Git blob `39a6b648377d44e8a82177e1c91a57309cca5cc5` (committed)
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

### tender/23#F1 · Medium · A language code as locale
- XPath: `/UnawardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/23#F2 · Low · The winner's subcontractor and subcontract price are disclosed to the losing competitor
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- Why: An unawarded notification is "A document communicating to a tenderer that the contract has been awarded to different tenderer". What the unsuccessful tenderer needs is the result, the winner, the reasons and its remedies; those are there (winning party, total, note, appeal terms). The tender result is, however, a full copy of the one sent to the winner (`22-AwardedNotification.xml`), including who the winner subcontracts to and at what unit price, a commercial detail of a competitor's tender that the receiver has no use for and, by common procurement practice (my knowledge: confidentiality of tenders), would not be told individually.
- Condition: The tender result sent to an unsuccessful tenderer carries the winner and the characteristics that explain the decision, and no terms between the winner and its subcontractor.
- Options: (a) preferred: leave `SubcontractTerms` out of this notification; (b) keep them if the law of the world makes them public (the award notice `21-ContractAwardNotice.xml` publishes the same terms), and record that rule.
- Needs decision: yes

### tender/23#F3 · Low · The review board is also the mediator and the source of appeal information
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: `MediationParty` is "The Party who mediates any appeal", `AppealReceiverParty` "The Party who receives the appeal". Mediation is an attempt to settle a dispute before or instead of a decision, by someone other than the body that decides; the description names one step only ("goes to the review board"). The same board in all three roles tells the reader nothing beyond the receiver and makes the deciding body its own mediator.
- Condition: `MediationParty` is present only if the world has a mediation step, with the body that mediates; `AppealInformationParty` only if it adds something to the receiver.
- Options: (a) preferred: keep `AppealReceiverParty` only; (b) name a real mediation body and describe the step.
- Needs decision: yes (whether the world has mediation in procurement appeals)

### tender/23#F4 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
## Checked and consistent
- `check_ids.py`: GLN 9523710900008 has a correct check digit.
- The note against the tenders: Brackenmere's tender is lower in price (`19-Tender.xml`, 119040.00, against 124080.00) and offers 6 years against Valdara's 10 years on criterion AC-2; with two tenders, "ranked second" follows.
- Tender result identical to the one in `22-AwardedNotification.xml` and `21-ContractAwardNotice.xml` (award of 2026-03-09 09:30, both lots to Valdara Industries, 124080.00); the notification is issued at 10:15 the same day, after the award.
- Appeal terms: "within ten days", period 2026-03-09 to 2026-03-19, starting on the day of the decision and of this notification; they belong in a notification to the tenderer who lost.
- Receiver is the tenderer of `19-Tender.xml`; sender and signatory are the contracting party.

## Considered and refuted
- `/UnawardedNotification/cac:TenderResult/cbc:TenderResultCode`: `AWARDED` in a notification of not being awarded — refuted because the tender result describes the procedure's result (awarded, to the winning party named), which is what the document communicates.
- `/UnawardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod`: the winner's formalization period in the loser's notification — refuted because it tells the receiver until when the contract is not yet concluded, which matters for an appeal.
- `/UnawardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: the winner's price disclosed — refuted because the price of the selected tender is among the characteristics a loser is normally told, and the award notice publishes it.
- `/UnawardedNotification/cac:AdditionalDocumentReference/cbc:ID`: `PWD-EVAL-SCORES-BF`, no example — refuted for this lens: a non-UBL annex with the receiver's own scores, as the element's definition allows.

## Outside this review
- The formalization period starts on the last day of the appeal period (2026-03-19) and the contract is issued that day; raised in the review of `22-AwardedNotification.xml`, whose note promises the contract after the standstill.
- The receiver's contact (trade sales) against the role of a tenderer, and the sender's tax exemption reason worded as a transaction: parties part.
