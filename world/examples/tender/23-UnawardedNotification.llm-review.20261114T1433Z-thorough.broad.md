# LLM review: 23-UnawardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

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

### tender/23#F1 · Medium · Language code in LocaleCode
- XPath: `/UnawardedNotification/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UnawardedNotification/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code and names no locale. Same pattern in 213 of the 250 examples (`grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`).
- Condition: LocaleCode, where present, identifies a locale and differs in kind from Language/ID.
- Options: (a) a locale (country or language-region tag; preferred); (b) leave it out.
- Needs decision: no

### tender/23#F2 · Low · The contract may be formalized on the last day an appeal can still be lodged
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:PresentationPeriod/cbc:EndDate` = `2026-03-19`
- XPath: `/UnawardedNotification/cac:TenderResult/cac:ContractFormalizationPeriod/cbc:StartDate` = `2026-03-19`
- Why: the notification gives the unsuccessful tenderer until 19 March (inclusive, as an end date) to appeal, and says in the same document that the contract with the winner is formalized from 19 March. The awarded notification promises the contract "after the standstill period" (22), and the contract is in fact issued on 2026-03-19 (24). On that day an appeal is still admissible, so the two periods should not overlap.
- Condition: the formalization period starts after the last day of the appeal period (or the appeal period ends the day before formalization starts).
- Options: (a) formalization from 2026-03-20 and the contract dated accordingly (preferred, keeps "ten days"); (b) appeal period ending 2026-03-18.
- Needs decision: no

### tender/23#F3 · Low · The same board informs about, receives and mediates the appeal, without an address
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealInformationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:AppealReceiverParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- XPath: `/UnawardedNotification/cac:AppealTerms/cac:MediationParty/cac:PartyName/cbc:Name` = `Procurement Review Board of Bayvarra`
- Why: MediationParty is "The Party who mediates any appeal"; the body that receives and decides the appeal is not a mediator between the parties. For the one tenderer who has reason to appeal, the notification gives the board's name and register number three times but no address, contact or electronic address, although the call for tenders and the award notice carry them (e.g. `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AppealTerms/cac:AppealReceiverParty/cac:Contact/cbc:ElectronicMail` = `registry@review-xb.example`).
- Condition: each appeal role present is held by a party that really has it, and the receiver of appeals can be reached from this document.
- Options: (a) AppealReceiverParty with address and contact, MediationParty only if the world has a mediation body (preferred); (b) a separate mediator.
- Needs decision: yes (whether Bayvarra has mediation in procurement appeals)

### tender/23#F4 · Low · The public works department described as a company in a commercial register
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/UnawardedNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the sender is a municipal department (ISIC 8411); it is not a company in a commercial register and has no liquidation status.
- Condition: the department's legal entity carries no liquidation status and no commercial-register type.
- Options: (a) drop the liquidation status and type the scheme as a register of public bodies (preferred); (b) drop CorporateRegistrationScheme for public bodies.
- Needs decision: no

## Checked and consistent
- The note agrees with the tenders: Brackenmere's corrected tender (19) is 119040.00 against Valdara's 124080.00 (15), so it was lower in price; it offered six years of warranty against Valdara's ten. With the call's formula (price 60 × lowest / tendered) Brackenmere scores 60.00 and Valdara 57.56 on price, so Valdara needs a quality lead of more than 2.44 of 40 points, which ten against six years (range 5–10) can give.
- Award data identical to 21 and 22: AwardID, award 2026-03-09 09:30, contract PWD-2026-PARKS from 2026-03-23 for 24 months, both lots, 124080.00, subcontracting 3.5 % / 4320.00.
- Appeal period 2026-03-09 to 2026-03-19 is ten days from the award, as the description and the call for tenders say.
- Issue time 10:15 follows the award time 09:30.
- Receiver is the tenderer of 19, described as there (register 20412466, GLN 9523710900008, Joiners Row 14, Marrowdale).
- check_ids.py: GLN 9523710900008 correct.

## Considered and refuted
- `/UnawardedNotification/cac:TenderResult/cbc:TenderResultCode`: AWARDED in a notification of not being awarded — refuted because TenderResult describes the result of the procedure (awarded to the winning party), not the receiver's own result.
- `/UnawardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description`: the winner's subcontracting price is disclosed to the losing competitor — refuted because the same data is published in the award notice (21).
- `/UnawardedNotification/cac:ReceiverParty/cac:Contact/cbc:Name`: sales desk as receiver of the decision — refuted, it is the contact Brackenmere gave in its tender.
- `/UnawardedNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: transaction-like reason on the party — refuted, the text states the party's status.

## Outside this review
- The note says the warranty "scored lower"; Brackenmere's tender (19) itself states five years on the line and six in the criterion response, see that example's review.
