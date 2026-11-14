# LLM review: 24-TenderContract.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/24-TenderContract.xml`, Git blob `f51644d96669fd1bea4cfc230ed7d7bb275322e5` (committed)
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

### tender/24#F1 · Medium · The allowed subcontracting is "precisely" 30 % and, in the same aggregate, 4320.00 lume, which is 3.5 %
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/TenderContract/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5`
- XPath: `/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`
- Why: `Rate` is "the precise percentage allowed to be subcontracted", `MaximumPercent` "the maximum percentage allowed to be subcontracted", `Amount` "the monetary amount assigned to the subcontracted task". In the allowed terms the precise rate repeats the maximum (30), while the amount next to it (4320.00) is 3.48 % of the contract (`/TenderContract/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`; 30 % would be 37224.00). The same contract then states, for the same 4320.00, a rate of 3.5 in the tender result. So one document gives the subcontracted share of one amount as 30 % and as 3.5 %. The rate in the result is itself rounded (3.5 % of 124080.00 = 4342.80). The allowed terms with these values are also in 01–03.
- Condition: within `AllowedSubcontractTerms`, `Rate` (if present) and `Amount` describe the same share of the same total, and a ceiling is carried only in `MaximumPercent`; within `TenderResult/SubcontractTerms`, `Rate` × awarded amount / 100 = `Amount` to the cent, or the rate is absent.
- Options: (a, preferred) in the allowed terms keep `MaximumPercent` 30 and the description, and remove `Rate` and `Amount` (the terms set a ceiling, not a task); in the result keep `Amount` and the description and remove `Rate`; (b) keep the amount in the allowed terms as the estimate of the installation lot and say so in the description.
- Needs decision: no

### tender/24#F2 · Medium · The tender guarantee's amount cannot be calculated with its rate from any amount of the procedure
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "the rate used to calculate the amount of liability in this financial guarantee". 2 % of the estimated and awarded contract value (`/TenderContract/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`) is 2481.60; 2 % of lot 1 (119760.00) is 2395.20; 2400.00 is 2 % of 120000.00, an amount that occurs nowhere in the flow. By contrast the performance guarantee of 22-AwardedNotification.xml is exactly 5 % of 124080.00 (6204.00). The guarantee certificate (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`) follows the amount. The pair 2400.00 / 2 is also in 01–03. It is rated Medium, not High, because the base of the rate is not stated, so the arithmetic fails against every candidate base but not against a stated one.
- Condition: `LiabilityAmount` = `AmountRate` % of an amount that the same document states (and names in the guarantee's description), or the rate is absent and the amount is a fixed sum.
- Options: (a, preferred) drop `AmountRate` and describe the guarantee as a fixed 2400.00 lume, which leaves the guarantee certificate untouched; (b) set the amount to 2481.60 (2 % of the estimate) here, in 01–03 and in the certificate.
- Needs decision: no

### tender/24#F3 · Low · The signed contract repeats the money terms of the tendering stage and leaves out the guarantee the award demanded
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:GuaranteeTypeCode` = `TENDER`
- XPath: `/TenderContract/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:MaximumAdvertisementAmount` = `500.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- Why: the document is the contract "signed by both parties" (`/TenderContract/cbc:Note`), issued on 19 March. It carries a `RequiredFinancialGuarantee`, "a financial guarantee of a tenderer or bid submitter's actual entry into a contract in the event that it is the successful bidder", that was due three weeks earlier and whose purpose ends with this very signature (14-GuaranteeCertificate.xml: "Released at the award."); the fee "to be paid to obtain the contract documents"; the ceiling for the cost of advertising the procedure; and the turnover threshold for admission. None of these is a term between the two signatories any more. What the award did require of the winner by the day of signature, the performance guarantee (`22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cbc:LiabilityAmount` = `6204.00`), is not in the contract. A reader of the contract therefore finds a guarantee of 2400.00 that no longer exists and not the one of 6204.00 that secures performance.
- Condition: every amount under the contract's `TenderingTerms` is a term that binds the parties from signature (payment terms, penalty, price revision, subcontracting ceiling, budget line), and a guarantee stated in the contract is the one in force during performance.
- Options: (a, preferred) remove the tender guarantee, documentation fee, advertisement ceiling and qualification threshold from the contract, and state the performance guarantee instead (decided together with 22#F1 of this part); (b) keep them, with a note that the tendering terms are reproduced as the annex the contract incorporates.
- Needs decision: yes

### tender/24#F4 · Low · The penalty clause names no base for its percentages
- XPath: `/TenderContract/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: the clause is the contract's only statement of the penalty, and it says neither of what amount the 0.5 % and the 10 % are taken (the contract, the release, the late part) nor what "late" refers to (delivery, installation). The flow's later document has to choose: `34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`, i.e. 0.5 % of 720.00 lume a day; on the contract value the same three days would be 1861.20 lume. A clause that allows readings 170 times apart cannot be checked against what is charged under it.
- Condition: the clause states the base of both percentages and the event that is late, and the amount in 34-DebitNote.xml follows from it.
- Options: (a, preferred) word the clause as the flow applies it, e.g. "0.5 % of the price of the late part of a release per day of delay, at most 10 % of that price"; (b) choose another base and recalculate the debit note.
- Needs decision: no

### tender/24#F5 · Low · The turnover threshold is not "twice the estimate", and "at least" is coded as "greater than"
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/TenderContract/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: twice the estimate of the same document (124080.00) is 248160.00, not 250000.00; and the description says "at least" (≥) while code and expression say "greater than" (>). A tenderer with a turnover of 249000.00 passes by the text and the expression and fails by the amount; one with exactly the threshold passes by the description and fails by the code. The same criterion is in 01–03.
- Condition: threshold amount, description, code and expression state one rule: the amount equals what the expression yields from figures in the document (or the text says it is a fixed, rounded sum), and the comparison is the same in text and code.
- Options: (a, preferred) describe it as "Yearly turnover of at least 250000 lume (about twice the estimate)" with a greater-or-equal code; (b) set the threshold to 248160.00 and align the comparison.
- Needs decision: no

### tender/24#F6 · Low · The framework contract does not state the prices its releases are ordered at
- XPath: `/TenderContract/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`
- XPath: `/TenderContract/cac:TenderingTerms/cbc:PriceEvaluationCode` = `UNITPRICE`
- Why: the contract is a framework agreement with quantities that may vary (the call allows 120 to 288 benches) and releases "at the framework prices" (21-ContractAwardNotice.xml). Its only price information is the total of the awarded tender for 240 benches; the unit prices (499 lume a bench, 18 lume an installation, derivable only from the lines of 15-Tender.xml) and the price of the special colour later charged (27-OrderChange.xml, 32-Invoice.xml) are not in it. `AwardedTenderedProject` can carry the awarded `TenderLine`s. The orders and invoices of the flow refer to this contract for their prices, so the document's purpose depends on them more than on the total. Rated Low because the tender is referenced through the award and the catalogue that follows (25-Catalogue.xml) lists the prices.
- Condition: the unit prices that govern releases can be read from the contract, or the contract references the document that states them (the awarded tender by its ID).
- Options: (a, preferred) add the two awarded tender lines with quantity and line amount to `AwardedTenderedProject`; (b) add a reference to the tender VI-DOC-26-0201 as the price basis.
- Needs decision: no

## Checked and consistent
- Tender result: lowest tender 119040.00 = 19-Tender.xml, highest and awarded 124080.00 = 15-Tender.xml; the same figures as in 21, 22 and 23. Subcontract amount 4320.00 = 240 × 18 lume.
- Budget line total 124080.00 = estimate of the notices = awarded amount.
- Advertisement 320.00 ≤ ceiling 500.00.
- Payment: `PaymentFrequencyCode` PERRELEASE ("After each release") agrees with the payment terms note "30 days after each accepted release."
- Awarding criterion AC-1 ("The lowest total of unit prices", 350.00 to 600.00): the winner's unit prices 499 + 18 = 517 and the other tenderer's 480 + 16 = 496 are both inside the range.
- All amounts in XBL; ISIN XU0001042501 check digit correct (`check_ids.py`).

## Considered and refuted
- `/TenderContract/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric`: the whole 124080.00 of a framework running from March 2026 to March 2028 sits on the budget account of 2026 — refuted because a commitment for the whole contract can be entered in the year of signature, and the funding programme is the "Parks renewal programme 2026"; whether later releases are paid from later budgets is not stated anywhere and is not contradicted.
- `/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note`: the contract's payment terms differ from those the invoice applies (30 days from the invoice date, a 2 % settlement discount, 8 % interest) — refuted as a finding of the contract: the contract's term is clear in itself; the difference is a finding of 32-Invoice.xml.
- `/TenderContract/cac:TenderingTerms/cbc:PriceRevisionFormulaDescription`: "Steel index each January." gives no formula — refuted because the element is a description, the first revision would fall in January 2027, and no document of the flow applies a revision.
- `/TenderContract/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount`: award criteria in a signed contract — refuted for the money lens: the range is consistent with the awarded prices (see above); whether award criteria belong in a contract is a question of context, not of money.
- `/TenderContract/cac:TenderResult/cbc:AdvertisementAmount`: the authority's advertising cost in a contract with the supplier — refuted as harmless repetition of the published result (21-ContractAwardNotice.xml), with no effect on the parties' obligations; noted in F3's sense only for the ceiling under the tendering terms.
