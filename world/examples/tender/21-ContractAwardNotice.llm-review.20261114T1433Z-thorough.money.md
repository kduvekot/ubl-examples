# LLM review: 21-ContractAwardNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/21-ContractAwardNotice.xml`, Git blob `59a77855a9c7e78ea4690806b5a919a52b58df71` (committed)
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

### tender/21#F1 · Medium · The two framework values are composed differently and neither includes both the option and the renewal
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount` = `148896.00`
- XPath: `/ContractAwardNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:MaximumValueAmount` = `186120.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` = `62040.00`
- Why: `EstimatedMaximumValueAmount` is "the estimated value which will be spent within a framework agreement over its whole duration, including options and renewals" and `MaximumValueAmount` "the maximum value which can be spent within a framework agreement over its whole duration, including options and renewals". The notice has an option on quantity (240 benches, at most 288: 288 × 499 + 288 × 18 = 148896.00, the budget's `MaximumAmount`) and a renewal (`OptionsDescription` "One extension of a year with 120 more benches", 120 × 499 + 120 × 18 = 62040.00). The estimated value 148896.00 contains the quantity option but not the renewal; the maximum value 186120.00 = 124080.00 + 62040.00 contains the renewal but not the quantity option. What can be spent at most under the stated terms is 148896.00 + 62040.00 = 210936.00, which is above the stated maximum, and an estimate "including renewals" cannot leave the renewal out. The same two values are in 02-ContractNotice.xml and 03-CallForTenders.xml.
- Condition: `MaximumValueAmount` is not lower than the sum of the highest amount the base period allows and the amounts of all renewals stated in the notice, and `EstimatedMaximumValueAmount` is an estimate over the same scope (base, options and renewals) that does not exceed it; both can be recomputed from the quantities, unit estimates and the renewal amount in the notice.
- Options: (a, preferred) set the maximum to 210936.00 and the estimate to the expected spend with renewal (e.g. 186120.00), because that keeps every other figure of the notice; (b) state in `OptionsDescription` that the 288 benches are a ceiling that already contains the renewal's benches, and adjust the renewal amount and the two values to that reading.
- Needs decision: no

### tender/21#F2 · Medium · The paper-copy fee is carried in the reimbursement fee for concession projects, three times, in a notice issued after the award
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- Why: `RequiredFeeAmount` is "the amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "text describing the reimbursement fee for concession procurement projects". The project is a purchase of supplies under a framework agreement (`/ContractAwardNotice/cac:ProcurementProject/cbc:ProcurementSubTypeCode` = `PURCHASE`), not a concession, and the 50 lume is the price of a paper copy of the procurement documents, for which UBL has `TenderingTerms/DocumentationFeeAmount` (used with the same 50.00 in 01–03). Repeating it in the project and in each lot also reads as a fee per lot (150 lume for a tenderer for both lots), which the description contradicts. Finally, a contract award notice reports the result: the documents can no longer be bought, so the fee has no function in this document. Counted with `grep -c RequiredFeeAmount *.xml` over the flow: 01 (1), 02, 03 and 21 (3 each).
- Condition: no `RequiredFeeAmount`/`FeeDescription` in a project that is not a concession; a document fee, where a document needs it, is stated once in the element defined for it.
- Options: (a, preferred) remove the fee and its description from the award notice, project and lots; (b) if the fee must stay visible, move it to `TenderingTerms/DocumentationFeeAmount` once.
- Needs decision: no

### tender/21#F3 · Low · The line's minimum and maximum amount are unit prices, its estimated amount is a total
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: the three elements are "the minimum amount allowed for this deliverable", "the maximum amount allowed for this deliverable" and "the estimated total amount of the deliverable"; the deliverable of the line is 240 benches (`Quantity` 240 EA). 350.00 and 600.00 are prices of one bench, 119760.00 is the price of 240 (499 each), so within one line the estimate is 200 times the maximum allowed. Read as the definitions stand, the awarded lot (119760.00) would be far above the allowed maximum. Nothing in the line says that two of the three amounts are per unit. Two readings: the minimum and maximum are meant per unit (then the line needs to say so), or they must be totals like the estimate (then 84000.00 and 144000.00).
- Condition: the three amounts of a request-for-tender line are on the same basis, or the basis of each is stated in the line, so that minimum ≤ estimate ≤ maximum holds.
- Options: (a, preferred) give minimum and maximum as totals of the line (240 × 350 = 84000.00, 240 × 600 = 144000.00) and leave the unit-price range to the awarding criterion, which is where the call evaluates unit prices; (b) keep the unit values and say so in the line's `Note`.
- Needs decision: no

### tender/21#F4 · Low · The "precise percentage" subcontracted is rounded and does not give the amount
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted" and `Amount` "the monetary amount assigned to the subcontracted task". 4320.00 / 124080.00 = 3.4816 %; 3.5 % of 124080.00 is 4342.80, not 4320.00. The amount is right (240 × 18 lume, as the description says, and equal to line 2 of 15-Tender.xml); the rate is a rounding of it.
- Condition: `Rate` × awarded amount / 100 equals `Amount` to the cent, or the rate is absent.
- Options: (a, preferred) drop `Rate`, since amount and awarded total are both in the result; (b) give it with enough decimals (3.4816 still gives 4319.97, so (a) is cleaner).
- Needs decision: no

### tender/21#F5 · Low · The winning tender equals the authority's estimate to the cent, in both lots
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cbc:HigherTenderAmount` = `124080.00`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- Why: the estimate was published before any tender existed (the same 124080.00, 119760.00 for lot 1 and 4320.00 for lot 2, is in 01-PriorInformationNotice.xml of 12 January). The winning tender offers exactly these amounts per lot (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`), i.e. 499 and 18 lume a piece. An authority's estimate and an independent tender agreeing to the cent on two separate prices is not plausible, and it makes the notice's estimate indistinguishable from the result.
- Condition: either the estimate differs from the awarded amounts, or the notice explains why they coincide (e.g. the estimate being a published ceiling price that the tenderer chose to meet).
- Options: (a, preferred) give the estimate round figures of its own (e.g. 500 and 20 lume a piece) in the notices of the flow; (b) keep the figures and say in the notices that the estimate is the price of the previous framework, which the tenderer matched.
- Needs decision: yes

## Checked and consistent
- Budget of the whole project: 119760.00 + 4320.00 = 124080.00; minimum 59880.00 + 2160.00 = 62040.00 (120 benches: 120 × 499 = 59880.00, 120 × 18 = 2160.00); maximum 143712.00 + 5184.00 = 148896.00 (288 × 499 = 143712.00, 288 × 18 = 5184.00). The lot figures agree with the line quantities 120/240/288.
- Average subsequent contract: 124080.00 / 6 = 20680.00; lots 119760.00 / 6 = 19960.00 and 4320.00 / 6 = 720.00. The first release that is ordered and invoiced (32-Invoice.xml: 40 benches, 19960.00 + 720.00 = 20680.00) is exactly this average.
- Renewal amounts: 59880.00 + 2160.00 = 62040.00, i.e. 120 benches with installation, as the options description says.
- Tender result: lowest tender 119040.00 = 19-Tender.xml; highest 124080.00 = 15-Tender.xml; awarded payable amount 124080.00 = 15-Tender.xml and 22-AwardedNotification.xml. Subcontract amount 4320.00 = 240 × 18 = line 2 of 15-Tender.xml.
- Advertisement 320.00 is below the 500.00 the notices allow (`MaximumAdvertisementAmount` in 01–03).
- Tax category of the budget: E, 0 %, reason PUBLIC, scheme STT, with `TaxIncludedIndicator` false: consistent with each other, with the contracting party's own status, and with 01–03.
- All amounts in XBL.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:TotalAmount`: defined as the total budget "including … taxes" while `TaxIncludedIndicator` is false — refuted because the applicable category is exempt at 0 %, so the amount with and without tax is the same.
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: the exemption PUBLIC of the Bayvarran sales tax is stated although the winner is an Urvanian exporter that invoices under Urvanian VAT (32-Invoice.xml) — refuted because the element describes "the categories of taxes that apply to the budget amount", i.e. the authority's side, and a Bayvarran tenderer (19-Tender.xml) would have sold under exactly this category.
- `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MinimumAmount`: equal to the renewal amount (62040.00) — refuted as a coincidence of both being 120 benches with installation.
- `/ContractAwardNotice/cac:TenderResult/cbc:AdvertisementAmount`: no counterpart in another example — refuted because it is the authority's own cost of publication and lies within the stated maximum.
