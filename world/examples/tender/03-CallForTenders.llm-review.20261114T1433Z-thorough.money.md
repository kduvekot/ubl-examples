# LLM review: 03-CallForTenders.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/03-CallForTenders.xml`, Git blob `24f08018e3295692f3f3cc82e4d7e61355b48c44` (committed)
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

### tender/03#F1 · High · Subcontracting: "precise" rate of 30 % against an amount that is 3.5 % of the estimate
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Rate` = `30`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:Amount` = `4320.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AllowedSubcontractTerms/cbc:MaximumPercent` = `30`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- Why: `Rate` is "The precise percentage allowed to be subcontracted", `MaximumPercent` "The maximum percentage allowed to be subcontracted", `Amount` "The monetary amount assigned to the subcontracted task". The amount 4320.00 is the estimate of lot 2, the installation (`/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`), which is 3.48 % of the estimate of 124080.00; 30 % of the estimate would be 37224.00. So the rate and the amount describe two different shares. The later documents of the flow give the same amount with the matching rate: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Rate` = `3.5` next to `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Amount` = `4320.00`. In addition, a "precise" percentage and a "maximum" percentage with the same value say two things at once (exactly 30 %, and at most 30 %).
- Condition: the percentage(s) and the amount in `AllowedSubcontractTerms` describe the same share of the same base (amount = percentage × estimate), or only the limit the buyer really sets is given; a precise rate is present only if the buyer prescribes an exact share.
- Options: (a, preferred) keep `MaximumPercent` 30 as the limit and drop `Rate` and `Amount`: before any tender the buyer sets a limit, not the share or the price of the subcontract; (b) keep the amount as the estimate of the installation and give the rate that matches it (3.5), without a 30 % maximum that the text does not explain.
- Needs decision: no

### tender/03#F2 · High · Tender guarantee: 2400.00 is not 2 % of any amount in the document
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate` = `2`
- Why: `AmountRate` is "The rate used to calculate the amount of liability in this financial guarantee." 2 % of the estimated contract amount (124080.00) is 2481.60; 2 % of lot 1's estimate (`/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `119760.00`) is 2395.20; 2 % of lot 2's estimate (4320.00) is 86.40; 2400.00 would be 2 % of 120000.00, an amount the document does not contain. The certificate later issued follows the amount (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`), so the amount is the one the flow uses and the rate is what does not fit.
- Condition: liability amount = rate × a base amount that the document states (or that the guarantee's description names), or no rate is given.
- Options: (a, preferred) say in `Description` that the guarantee is a fixed 2400 lume and drop `AmountRate`; (b) set the amount to 2 % of the estimate (2481.60) here and in every document that repeats it, including the certificate.
- Needs decision: no

### tender/03#F3 · Medium · Framework agreement: the "estimated" value leaves out the renewal, the "maximum" value is below what the document allows
- XPath: `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:EstimatedMaximumValueAmount` = `148896.00`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:FrameworkAgreement/cbc:MaximumValueAmount` = `186120.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MaximumAmount` = `148896.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount` = `62040.00`
- Why: `EstimatedMaximumValueAmount` is "The estimated value which will be spent within a framework agreement over its whole duration, including options and renewals"; `MaximumValueAmount` "The maximum Value which can be spent within a framework agreement over its whole duration, including options and renewals." The document's own figures are: estimate 124080.00 (240 benches), maximum of the base contract 148896.00 (288 benches, the request line's maximum quantity), renewal 62040.00 (120 more benches). 148896.00 is the maximum of the base contract without the renewal, so it is neither an estimate (124080.00) nor "including options and renewals" (124080 + 62040 = 186120). 186120.00 is the estimate plus the renewal, not the maximum: the most that can be spent under the stated terms is 148896 + 62040 = 210936.00 (288 + 120 benches at the estimate's prices). Each element thus carries the figure that belongs to something else.
- Condition: `EstimatedMaximumValueAmount` is the expected spend including the renewal, `MaximumValueAmount` the highest spend the terms allow including the renewal, and both can be derived from the quantities, limits and renewal amount in the document.
- Options: (a, preferred) estimated 186120.00 and maximum 210936.00; (b) if the buyer means a ceiling of 186120.00 for everything, lower the maximum quantity or say that the renewal counts against the same ceiling, and give the estimate as 124080.00 or 186120.00 accordingly.
- Needs decision: yes

### tender/03#F4 · Medium · Turnover criterion: threshold 250000 against "twice the estimate" (248160), "at least" against "greater than"
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Description` = `Yearly turnover of at least twice the estimate.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ExpressionCode` = `GT`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:Expression` = `Turnover > 2 × estimate`
- Why: twice the estimate of 124080.00 is 248160.00, not 250000.00: a tenderer with a turnover of 249000 meets the expression and fails the threshold amount. The description says "at least" (≥), the code and the expression say "greater than" (>). Kept at Medium rather than High because the definition of `ThresholdAmount` calls it an "Estimated monetary amount of the threshold", which leaves room for a rounded figure; the two statements of the comparison still differ.
- Condition: threshold amount, description and expression give the same limit and the same comparison.
- Options: (a, preferred) threshold 248160.00 and one comparison throughout ("at least", with a code for greater-or-equal if the list has one); (b) keep 250000.00 and word description and expression as "a yearly turnover of at least 250,000 lume (about twice the estimate)".
- Needs decision: no

### tender/03#F5 · Medium · Fee for paper copies carried as the reimbursement fee of a concession, three times
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:RequiredFeeAmount` = `50.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`
- XPath: `/CallForTenders/cac:TenderingTerms/cbc:DocumentationFeeAmount` = `50.00`
- Why: `RequiredFeeAmount` is "The amount of the reimbursement fee for concession procurement projects" and `FeeDescription` "Text describing the reimbursement fee for concession procurement projects". Neither the project nor its lots are concessions (supplies; lot 2 is a service), and the 50 lume are the price of a paper copy of the documents, for which UBL has `DocumentationFeeAmount` ("The amount to be paid to obtain the contract documents and additional documentation"), already present with the same value. The fee is stated four times, three of them in an element that means something else; repeated in each lot it also reads as 50 lume per lot, while the tenders of the flow pay it once (`15-Tender.xml:/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`).
- Condition: no `RequiredFeeAmount`/`FeeDescription` in a project or lot that is not a concession; the fee for the documents is stated once, in `DocumentationFeeAmount`, and the explanation that only paper copies cost money is kept in a text element of the tendering terms.
- Options: (a, preferred) remove the elements from the project and both lots and move the sentence to a note of the tendering terms; (b) none seen that keeps the elements.
- Needs decision: no

### tender/03#F6 · Medium · Request line: minimum and maximum "amount" are unit prices, the estimated amount is a line total
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:MaximumAmount` = `600.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount` = `119760.00`
- Why: the three elements are defined for the same thing, the deliverable of the line: "The minimum amount allowed for this deliverable", "The maximum amount allowed for this deliverable", "The estimated total amount of the deliverable". Here the estimate is the total for 240 benches (240 × 499 = 119760), while minimum and maximum are prices of one bench. Read by their definitions, the line allows at most 600.00 for a deliverable estimated at 119760.00. Nothing in the line says that 350 and 600 are per unit.
- Condition: minimum, maximum and estimated amount of a line are on the same basis, or the unit-price limits are carried where a unit price is meant (they already are in the price criterion, `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`).
- Options: (a, preferred) line totals in the line (for 240 benches 84000.00 and 144000.00) and the unit-price limits only in the price criterion; (b) drop minimum and maximum from the line and state the unit-price limits in the line's note.
- Needs decision: no

### tender/03#F7 · Low · Money terms set for the whole procedure do not fit a tender for lot 2 alone
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumAmount` = `350.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MaximumAmount` = `600.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:MinimumImprovementBid` = `In the electronic auction, each new bid lowers the bench's unit price by at least 2 lume.`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:TendererQualificationRequest/cac:FinancialEvaluationCriterion/cbc:ThresholdAmount` = `250000.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:TenderingTerms/cbc:Note` = `As for the procedure.`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- Why: tenders may be made for one lot (`/CallForTenders/cac:TenderingProcess/cbc:PartPresentationCode` = `ONEORMORE`), and lot 2 takes its terms from the procedure. Lot 2 is the installation, estimated at 4320.00 for 240 benches, 18 lume each. For it, the price criterion's limits of 350 to 600 lume cannot be met by any unit price; the auction, which the auction terms say runs "on the unit prices of both lots", has a bid step only for "the bench's unit price", and a step of 2 lume would be 11 % of the installation price; the tender guarantee of 2400.00 is 56 % of the lot's estimate; and the turnover threshold of 250000.00 is 58 times the lot's estimate. The terms were written for lot 1 or for both lots together.
- Condition: every money term that applies to lot 2 (price limits, bid step, guarantee, turnover threshold) is one a tender for lot 2 alone can meet, or the document says that lot 2 can only be tendered together with lot 1.
- Options: (a, preferred) state the price limits, bid step, guarantee and turnover threshold per lot in each lot's tendering terms; (b) require tenders for both lots (the lots group G-1 already exists) and say so.
- Needs decision: yes

### tender/03#F8 · Low · The estimates equal the winning tender to the cent
- XPath: `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `124080.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[1]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `119760.00`
- XPath: `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `4320.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- Why: this document is issued on 2026-02-12; Valdara's tender of 2026-02-25 offers exactly these amounts: `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`, `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`. A buyer's estimate made before the tenders, with unit prices of 499 and 18 lume, that one of two tenderers then meets to the cent in both lots (the other offers 119040.00) is not plausible; it reads as the outcome copied back into the estimate. All derived figures (minimum, maximum, renewal, average release, budget line, framework values) inherit it.
- Condition: the buyer's estimate is a figure a buyer would plan with and differs from the tendered prices, or the story explains the equality (for instance a published ceiling price that the tenderer chose to offer).
- Options: (a, preferred) a rounded estimate (for example 500 and 20 lume per bench: 124800.00) with the derived amounts following it; (b) keep the figures and say in the tender that it offers the published estimate.
- Needs decision: yes

### tender/03#F9 · Low · An auction on the prices is announced, but the award is made at the prices of the tenders
- XPath: `/CallForTenders/cac:TenderingProcess/cac:AuctionTerms/cbc:AuctionConstraintIndicator` = `true`
- XPath: `/CallForTenders/cac:TenderingProcess/cac:AuctionTerms/cbc:Description` = `After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an electronic auction…`
- Why: `AuctionConstraintIndicator` "Indicates whether an electronic auction will be used before the awarding of a contract (true) or not (false)." The flow has two admissible tenders, and the award is made at exactly the amount of the winner's original tender: `22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00` = `15-Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`; the award notice reports the lowest tender at the other tenderer's original amount (`21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderResult/cbc:LowerTenderAmount` = `119040.00`). No document of the flow mentions that the auction took place or that nobody bid. Either the auction was held and changed nothing, or it was not held; in both cases the flow leaves the announced price step without any trace.
- Condition: the flow shows what became of the announced auction (held, with the final prices; held without bids; or not held, with the reason), or the procedure has no auction.
- Options: (a, preferred) say in the award documents that the auction of a given date brought no lower bids, so that the tender prices stand; (b) let the auction lower a price and carry the new prices through award, contract, catalogue, order and invoice; (c) remove the auction from the procedure.
- Needs decision: yes

### tender/03#F10 · Low · Penalty clause gives percentages without the amount they apply to
- XPath: `/CallForTenders/cac:TenderingTerms/cac:PenaltyClause/cbc:Content` = `0.5 % per day late, at most 10 %.`
- Why: the clause does not say of what the percentages are taken (the contract value, the value of the late release, the value of the late part). The flow later applies it to the installation price of one release: `34-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.` With the base missing, the clause as published cannot be applied, and the debit note's base is one choice among several.
- Condition: the clause names the base of the percentages, and it is the base the debit note uses.
- Options: (a, preferred) "0.5 % of the price of the late part of a release per day late, at most 10 % of that price"; (b) another base, with the debit note following it.
- Needs decision: no

### tender/03#F11 · Low · The whole two-year amount on one budget account of the year 2026
- XPath: `/CallForTenders/cac:TenderingTerms/cac:BudgetAccountLine/cbc:TotalAmount` = `124080.00`
- XPath: `/CallForTenders/cac:TenderingTerms/cac:BudgetAccountLine/cac:BudgetAccount/cbc:BudgetYearNumeric` = `2026`
- Why: the releases run from 2026-03-23 to 2028-03-22 (`/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:MonetaryScope` = `Two years of releases.`), paid 30 days after each release, so the spending falls in the budget years 2026, 2027 and 2028. The single budget line charges the full estimate to an account of "the year for this budget account" 2026. It may be meant as the commitment authorised in 2026; the document does not say so.
- Condition: the budget account line(s) show in which budget year(s) the amount is spent, or the line says that it is a multi-year commitment entered in 2026.
- Options: (a) one budget account per year with the amounts expected in it; (b, preferred, smallest) keep the line and state in the monetary scope or a note that it is a commitment of the 2026 budget for two years.
- Needs decision: yes

## Checked and consistent
- Estimate: 240 × 499 + 240 × 18 = 119760 + 4320 = 124080.00; the lots' estimates (119760.00, 4320.00) add up to the project's, and so do their minimums (59880 + 2160 = 62040), maximums (143712 + 5184 = 148896), renewals (59880 + 2160 = 62040) and average releases (19960 + 720 = 20680).
- Minimum and maximum follow the request line's quantity limits: 120 and 288 benches at 499 (lot 1), 18 (lot 2) and 517 lume (project). Average release: one sixth of the estimate, which is what the first release is invoiced at before the colour surcharge (`32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `20680.00`).
- Award weights: 60 + 40 = 100, matching `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cbc:Description` = `Price 60 %, quality 40 %.`; the formula "60 × lowest / tendered" fits the code INVERSE.
- Price limits of the criterion (350–600) contain the estimate's bench price (499) and the bench prices of tenders 15, 17 and 19 (499, 470, 480).
- Tax: category E, 0 %, reason PUBLIC under the state sales tax STT, in the project and both lots, agrees with the contracting party's own tax scheme entry (STT, state level, exemption PUBLIC, currency XBL).
- Payment: `PaymentFrequencyCode` PERRELEASE agrees with the payment terms note "30 days after each accepted release."
- Tender guarantee: the amount is that of the certificate in example 14; the constitution period ends on the tender deadline (2026-02-26). The quality criterion's range of 5 to 10 years starts at the required warranty of 5 years.
- Framework duration 24 months = planned period 2026-03-23 to 2028-03-22; expense code INVESTMENT fits a purchase of park furniture.
- `check_ids.py` reports nothing wrong. XBL and XUF are not assigned ISO 4217 codes.

## Considered and refuted
- `/CallForTenders/cac:TenderingTerms/cbc:MaximumAdvertisementAmount`: suspected that 500.00 does not fit "The maximum advertised monetary value of the tendering process" (which could be read as the highest contract value advertised) — refuted because the element pairs with `TenderResult/AdvertisementAmount`, "The monetary value of the advertisement for this tendering process", which the award notice of the flow fills with 320.00; read together, both are the cost of advertising the procedure, and 320 stays under the cap of 500.
- `/CallForTenders/cac:ProcurementProject/cac:RequestForTenderLine/cbc:EstimatedAmount`: suspected that the project's only request line (119760.00) does not add up to the project estimate (124080.00) — refuted because the difference of 4320.00 is the installation (lot 2), a service without a goods line; the sub-line for the anchor sets has no amount of its own and is part of the bench price.
- `/CallForTenders/cac:ProcurementProjectLot[2]/cac:ProcurementProject/cac:ContractExtension/cac:Renewal/cbc:Amount`: suspected that a renewal "with 120 more benches" has no meaning in the installation lot — refuted because 2160.00 is the installation of those 120 benches (120 × 18).
- `/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode`: suspected that an exemption under Bayvarra's sales tax says nothing about the taxes the invoice later shows (Urvanian VAT as export, and a 10 % withholding tax on the installation) — refuted because those depend on where the supplier is established, which is unknown when the document is issued; it states the buyer's own tax position.
- `/CallForTenders/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason`: suspected that "Sale to a public body…" describes a transaction rather than the party's status — refuted because the second half of the text ("public bodies are exempt from the state sales tax") states the party's status, which is what the element is for.
- `/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cac:SubordinateAwardingCriterion/cbc:WeightNumeric`: suspected that a single sub-criterion of 20 does not fill the parent's weight of 40 — refuted because the rest is the warranty period scored by the parent itself (5 to 10 years); not a money matter.
- `/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:AmountRate`: suspected that a rate should be 0.02 rather than 2 — refuted because the other percentages of the flow written as rates use the same convention (3.5, 5), and UBL does not fix it.
- `/CallForTenders/cac:TenderingProcess/cac:ProcessJustification/cbc:ProcessReason`: suspected that "Value above the threshold for open procedures." needs the threshold — refuted because the threshold is a matter of the procurement act the document references, and nothing in the document contradicts it.

## Outside this review
- The invoice of the first release applies the supplier's standard terms (2 % settlement discount, 8 % penalty interest) rather than the "30 days after each accepted release" of these terms; that lies in example 32.
