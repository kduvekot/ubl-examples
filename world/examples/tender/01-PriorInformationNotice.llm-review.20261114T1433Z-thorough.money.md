# LLM review: 01-PriorInformationNotice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/01-PriorInformationNotice.xml`, Git blob `8ffc7805e1260abb517917498ec704d7f21b863c` (committed)
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

### tender/01#F1 · High · Subcontracting: "precise" rate of 30 % against an amount that is 3.5 % of the estimate
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". The amount 4320.00 is 3.48 % of the estimate of 124080.00 (4320 / 124080); 30 % of the estimate would be 37224.00. So the rate and the amount describe two different shares. The later documents of the flow give the same amount with the matching rate: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5` next to `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`. In addition, a "precise" percentage and a "maximum" percentage with the same value say two things at once (exactly 30 %, and at most 30 %).
- Condition: the percentage(s) and the amount in `AllowedSubcontractTerms` describe the same share of the same base (amount = percentage × estimate), or only the limit the buyer really sets is given; a precise rate is present only if the buyer prescribes an exact share.
- Options: (a, preferred) keep `MaximumPercent` 30 as the limit and drop `Rate` and `Amount`: before any tender the buyer sets a limit, not the share or the price of the subcontract; (b) keep the amount as the estimate of the installation and give the rate that matches it (3.5), without a 30 % maximum that the text does not explain.
- Needs decision: no

### tender/01#F2 · High · Tender guarantee: 2400.00 is not 2 % of any amount in the notice
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "The rate used to calculate the amount of liability in this financial guarantee." 2 % of the estimated contract amount (124080.00) is 2481.60; 2 % of the bench line's estimate (`/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`) is 2395.20; 2400.00 would be 2 % of 120000.00, an amount the notice does not contain. The certificate later issued follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`), so the amount is the one the flow uses and the rate is what does not fit.
- Condition: liability amount = rate × a base amount that the notice states (or that its description names), or no rate is given.
- Options: (a, preferred) say in `Description` that the guarantee is a fixed 2400 lume and drop `AmountRate`; (b) set the amount to 2 % of the estimate (2481.60) here and in every document that repeats it, including the certificate.
- Needs decision: no

### tender/01#F3 · Medium · Turnover criterion: threshold 250000 against "twice the estimate" (248160), "at least" against "greater than"
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: twice the estimate of 124080.00 is 248160.00, not 250000.00: a tenderer with a turnover of 249000 meets the expression and fails the threshold amount. The description says "at least" (≥), the code and the expression say "greater than" (>). Kept at Medium rather than High because the definition of `ThresholdAmount` calls it an "Estimated monetary amount of the threshold", which leaves room for a rounded figure; the two statements of the comparison still differ.
- Condition: threshold amount, description and expression give the same limit and the same comparison.
- Options: (a, preferred) threshold 248160.00 and one comparison throughout ("at least", with a code for greater-or-equal if the list has one); (b) keep 250000.00 and word description and expression as "a yearly turnover of at least 250,000 lume (about twice the estimate)".
- Needs decision: no

### tender/01#F4 · Medium · Fee for paper copies carried as the reimbursement fee of a concession
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "Text describing the reimbursement fee for concession procurement projects". The project is a purchase of supplies (`/PriorInformationNotice/cac:ProcurementProject/cbc:ProcurementTypeCode` = `SUPPLIES`), not a concession, and the 50 lume are the price of a paper copy of the documents, for which UBL has `DocumentationFeeAmount` ("The amount to be paid to obtain the contract documents and additional documentation"), already present with the same value. The same amount is thus stated twice, once in an element that means something else.
- Condition: no `RequiredFeeAmount`/`FeeDescription` in a project that is not a concession; the fee for the documents is stated once, in `DocumentationFeeAmount`, and the explanation that only paper copies cost money is kept in a text element of the tendering terms.
- Options: (a, preferred) remove both elements from `ProcurementProject` and move the sentence to a note of the tendering terms; (b) none seen that keeps the elements.
- Needs decision: no

### tender/01#F5 · Medium · Request line: minimum and maximum "amount" are unit prices, the estimated amount is a line total
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:Quantity` = `240`
- Why: the three elements are defined for the same thing, the deliverable of the line: "The minimum amount allowed for this deliverable", "The maximum amount allowed for this deliverable", "The estimated total amount of the deliverable". Here the estimate is the total for 240 benches (240 × 499 = 119760), while minimum and maximum are prices of one bench. Read by their definitions, the line allows at most 600.00 for a deliverable estimated at 119760.00. Nothing in the line says that 350 and 600 are per unit.
- Condition: minimum, maximum and estimated amount of the line are on the same basis, or the unit-price limits are carried where a unit price is meant (they already are in the price criterion, `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`).
- Options: (a, preferred) line totals in the line (for 240 benches 84000.00 and 144000.00) and the unit-price limits only in the price criterion; (b) drop minimum and maximum from the line and state the unit-price limits in the line's note.
- Needs decision: no

### tender/01#F6 · Low · The estimates equal the winning tender to the cent
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- Why: the notice is issued on 2026-01-12; Valdara's tender of 2026-02-25 offers exactly these amounts: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`. A buyer's estimate made six weeks before the tenders, with unit prices of 499 and 18 lume, that one of two tenderers then meets to the cent (the other offers 119040.00) is not plausible; it reads as the outcome copied back into the estimate. All derived figures (minimum, maximum, renewal, average release, budget line) inherit it.
- Condition: the buyer's estimate is a figure a buyer would plan with and differs from the tendered prices, or the story explains the equality (for instance a published ceiling price that the tenderer chose to offer).
- Options: (a, preferred) a rounded estimate (for example 500 and 20 lume per bench: 124800.00) with the derived amounts following it; (b) keep the figures and say in the tender that it offers the published estimate.
- Needs decision: yes

### tender/01#F7 · Low · Price criterion describes an electronic auction that the notice does not announce
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- Why: `MinimumImprovementBid` "Describes the minimum improvement bid for this awarding criterion when used in an auction." This notice's tendering process (`/PriorInformationNotice/cac:TenderingProcess/cbc:Description` = `Planned as an open procedure in two lots.`) has no auction terms; the auction is only announced in the contract notice (`02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`). A reader of this notice learns of a bid step for an auction it is not told about.
- Condition: the notice either announces the auction or does not carry its bid step.
- Options: (a, preferred) leave the bid step to the contract notice and the call for tenders; (b) add the auction to this notice's description of the planned procedure.
- Needs decision: no

### tender/01#F8 · Low · Penalty clause gives percentages without the amount they apply to
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: the clause does not say of what the percentages are taken (the contract value, the value of the late release, the value of the late part). The flow later applies it to the installation price of one release: `34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.` With the base missing, the clause as published cannot be applied, and the debit note's base is one choice among several.
- Condition: the clause names the base of the percentages, and it is the base the debit note uses.
- Options: (a, preferred) "0.5 % of the price of the late part of a release per day late, at most 10 % of that price"; (b) another base, with the debit note following it.
- Needs decision: no

### tender/01#F9 · Low · The whole two-year amount on one budget account of the year 2026
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- XPath: `/PriorInformationNotice/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric` = `2026`
- Why: the releases run from 2026-03-23 to 2028-03-22 (`/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MonetaryScope` = `Two years of releases.`), paid 30 days after each release, so the spending falls in the budget years 2026, 2027 and 2028. The single budget line charges the full estimate to an account of "the year for this budget account" 2026. It may be meant as the commitment authorised in 2026; the document does not say so.
- Condition: the budget account line(s) show in which budget year(s) the amount is spent, or the line says that it is a multi-year commitment entered in 2026.
- Options: (a) one budget account per year with the amounts expected in it; (b, preferred, smallest) keep the line and state in the monetary scope or a note that it is a commitment of the 2026 budget for two years.
- Needs decision: yes

## Checked and consistent
- Estimate: 240 × 499 + 240 × 18 = 119760 + 4320 = 124080.00 = `EstimatedOverallContractAmount` = `EstimatedOverallFrameworkContractsAmount` = `TotalAmount` (tax is exempt, so with and without tax are equal; `TaxIncludedIndicator` false does not contradict).
- Minimum and maximum of the budget follow the line's quantity limits at the estimate's 517 lume per bench: 120 × 517 = 62040.00, 288 × 517 = 148896.00. Renewal: 120 × 517 = 62040.00 for the "120 more benches". Average release: 124080 / 6 = 20680.00, which is what the first release is invoiced at before the colour surcharge (`32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `20680.00`).
- Award weights: 60 + 40 = 100, matching `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cbc:Description` = `Price 60 %, quality 40 %.`; the formula "60 × lowest / tendered" fits the code INVERSE.
- Price limits of the criterion (350–600) contain the estimate's unit price (499) and both tenderers' bench prices (470–499, from tenders 15, 17 and 19).
- Tax: category E, 0 %, reason PUBLIC under the state sales tax STT agrees with the contracting party's own tax scheme entry (STT, state level, exemption PUBLIC, currency XBL).
- Payment: `PaymentFrequencyCode` PERRELEASE agrees with the payment terms note "30 days after each accepted release."
- Tender guarantee amount 2400.00 is the amount of the certificate in example 14; the quality criterion's range of 5 to 10 years starts at the required warranty of 5 years.
- `check_ids.py` reports nothing wrong (the example has no check-digit identifiers). XBL is not an assigned ISO 4217 code (the real X-codes near it are XBA, XBB, XBC, XBD).

## Considered and refuted
- `/PriorInformationNotice/cac:TenderingTerms/cbc:MaximumAdvertisementAmount`: suspected that 500.00 does not fit "The maximum advertised monetary value of the tendering process" (which could be read as the highest contract value advertised, 148896.00) — refuted because the element pairs with `TenderResult/AdvertisementAmount`, "The monetary value of the advertisement for this tendering process", which the award notice of the flow fills with 320.00; read together, both are the cost of advertising the procedure, and 320 stays under the cap of 500.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount`: suspected that the maximum of 148896.00 contradicts the renewal of 62040.00 (124080 + 62040 = 186120) — refuted because the maximum follows the maximum quantity of the base contract (288 benches), and the renewal is a separate option with its own amount; the contract notice gives the figure with the renewal separately.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallFrameworkContractsAmount`: suspected a framework amount in a notice that does not mention a framework — refuted because the monetary scope ("Two years of releases.") and the average subsequent contract amount describe call-offs, and the contract notice declares the framework agreement; the amount equals the estimate, which is what the releases add up to.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount`: suspected that the only request line (119760.00) does not add up to the project estimate (124080.00) — refuted because the difference of 4320.00 is the installation (lot 2), which is a service without a goods line; the sub-line for the anchor sets has no amount of its own and is part of the bench price.
- `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: suspected that an exemption under Bayvarra's sales tax says nothing about the taxes the invoice later shows (Urvanian VAT as export, and a 10 % withholding tax on the installation) — refuted because those depend on where the supplier is established, which is unknown when the notice is issued; the notice states the buyer's own tax position.
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason`: suspected that "Sale to a public body…" describes a transaction rather than the party's status — refuted because the second half of the text ("public bodies are exempt from the state sales tax") states the party's status, which is what the element is for; the code's name is that of the list.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric`: suspected that a single sub-criterion of 20 does not fill the parent's weight of 40 — refuted because the rest is the warranty period scored by the parent itself (5 to 10 years); not a money matter.
- `/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate`: suspected that a rate should be 0.02 rather than 2 — refuted because the other percentages of the flow written as rates use the same convention (3.5, 5), and UBL does not fix it.

## Outside this review
- Whether a prior information notice should already carry complete tendering terms (guarantee with a constitution date, budget line, payment terms) is a question for the context lens.
- The invoice of the first release applies the supplier's standard terms (2 % settlement discount, 8 % penalty interest) rather than the notice's "30 days after each accepted release"; that lies in example 32.
