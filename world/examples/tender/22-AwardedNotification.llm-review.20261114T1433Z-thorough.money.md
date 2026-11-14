# LLM review: 22-AwardedNotification.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

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

### tender/22#F1 · Low · A performance guarantee is required of the winner that no earlier document of the procedure announced and no later document takes up
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:GuaranteeTypeCode` = `PERFORMANCE`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cbc:AmountRate` = `5`
- XPath: `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`
- Why: `FinalFinancialGuarantee` is "a bond guarantee by the submitter of a tender or bid, required of the tender winner". The terms the tenderers priced against name one guarantee only, the tender guarantee (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`, 2400.00 lume); a performance guarantee of 5 % is a cost to the contractor that appears here for the first time, after the tenders are binding. It also has no follow-up: the contract signed on the day the guarantee is due (24-TenderContract.xml, 19 March) repeats the tender guarantee and does not mention a performance guarantee, and the flow has no guarantee certificate for it (14-GuaranteeCertificate.xml is the tender guarantee). Searched with `grep -l '>6204\.00<\|PERFORMANCE' *.xml` over the flow: only this example.
- Condition: a guarantee required of the winner is one the tendering terms of the call announced (type and rate), and the contract of the flow either records it or does not contradict it.
- Options: (a, preferred) announce the performance guarantee (5 %) in the tendering terms of the notices and the call next to the tender guarantee, and let the contract carry it instead of the tender guarantee; (b) remove it from the award notification.
- Needs decision: yes

### tender/22#F2 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `Amount` "the monetary amount assigned to the subcontracted task". 4320.00 / 124080.00 = 3.4816 %; 3.5 % of 124080.00 is 4342.80. The amount is the right one (240 × 18 lume, line 2 of 15-Tender.xml); the rate is a rounding of it. The same pair is in 21, 23 and 24.
- Condition: `Rate` × awarded amount / 100 equals `Amount` to the cent, or the rate is absent.
- Options: (a, preferred) drop `Rate`; (b) state it with the decimals needed.
- Needs decision: no

## Checked and consistent
- Awarded amount 124080.00 = total of the winning tender (`15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`), and the same in 21, 23 and 24.
- Performance guarantee: 5 % of 124080.00 = 6204.00, exact.
- Subcontract: 4320.00 = 240 × 18 lume = line 2 of the winning tender; the description names the same price.
- Currency XBL throughout.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: a framework agreement guarantees no fixed total (the call allows 120 to 288 benches), so "the amount … to be paid" could be called misleading — refuted because the element here is the total of the awarded tender, which is what the winner offered for the stated 240 benches, and the contract type FRAMEWORK is stated next to it.
- `/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate`: the guarantee is due on the first day of the formalisation period (19 March), ten days after the award — refuted as a timing problem: the period is short but possible, and the due date does not fall after the contract's start (23 March).
