# LLM review: 15-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/15-Tender.xml`, Git blob `a052a0ed15639e25ddae372a37b1960f7b6a9857` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/15#F1 · Medium · The tendered price sits in the response to the quality criterion; the price criterion has no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionDescription` = `Warranty and coating.`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `124080.00`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Quantity` = `10`
- Why: `Amount` "Specifies the monetary amount tendered for this awarding criterion", `Quantity` "Specifies the quantity tendered for this awarding criterion." The response refers to AC-2, which the call for tenders defines as the quality criterion, measured in years (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:AwardingCriterionTypeCode` = `QUALITY`, with a range of 5 to 10 years). The years answer it; the amount of 124080.00 lume does not: it is the tender's total price, which belongs to the price criterion (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:ID` = `AC-1`), and for that criterion the tender has no response at all. Besides, AC-1 is described as "The lowest total of unit prices" with unit-price limits of 350 to 600 lume, so even there the answer would be unit prices (499 and 18 lume for bench and installation), not the contract total.
- Condition: every awarding criterion response carries only what was tendered for the criterion it names; the price is given in a response to AC-1, in the terms that criterion is evaluated in.
- Options: (a, preferred) a response to AC-1 with the amount the criterion evaluates, and the response to AC-2 with the years only; (b) drop the amount and leave the price to the tender lines and the monetary total.
- Needs decision: no

### tender/15#F2 · Low · No unit price, although the procedure evaluates and auctions unit prices
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:Quantity` = `240`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount` = `4320.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cac:OfferedItemLocationQuantity/cbc:LeadTimeMeasure` = `7`
- Why: the terms evaluate unit prices (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:PriceEvaluationCode` = `UNITPRICE`), ask for a price schedule with "Unit prices per lot" (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:TenderPreparation/cac:DocumentTenderRequirement/cbc:Description` = `Unit prices per lot.`), announce an auction "on the unit prices of both lots", and the framework's releases are ordered "at the framework prices". The tender gives line totals only; the unit prices (499 and 18 lume) have to be worked out by dividing by 240. The line already has the aggregate that can hold a price (`OfferedItemLocationQuantity`), used for the lead time alone.
- Condition: each tender line states the unit price it offers, and quantity × unit price equals the line amount.
- Options: (a, preferred) a price in `OfferedItemLocationQuantity` of both lines (line 2 has none of it yet); (b) leave the totals and attach the price schedule as a referenced document.
- Needs decision: no

### tender/15#F3 · Low · A tax total of zero that names no tax
- XPath: `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TotalTaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `119760.00`
- Why: `TaxTotal/TaxAmount` is "The total tax amount for a particular taxation scheme, e.g., VAT; the sum of the tax subtotals for each tax category within the taxation scheme." The tax total has no subtotal, so neither the scheme nor the reason for zero is stated. The buyer's terms speak of an exemption from Bayvarra's sales tax for a sale to a public body; the invoice the tenderer later issues shows Urvanian VAT at zero as an export and a 10 % withholding tax on the installation (`32-Invoice.xml:/Invoice/cac:WithholdingTaxTotal/cbc:TaxAmount` = `72.00` for one release). Which of these the tender's zero stands for is not said. Line 1 repeats the zero and a tax-inclusive amount; line 2 has neither.
- Condition: the tax total says which tax it is and why the amount is zero (category, exemption reason, scheme), consistently with the terms, and both lines treat tax the same way; or the tender carries no tax total.
- Options: (a, preferred) one tax subtotal with the category and exemption reason that apply, for the taxable amount of 124080.00; (b) drop the zero amounts.
- Needs decision: no

### tender/15#F4 · Low · Fees in a tender: the same paper-copy and courier costs in all three tenders of the flow
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: the three tenders of the flow (examples 15, 17 and 19, counted with `grep -c "Courier of the guarantee" *.xml` over the flow's XML: one occurrence in each of the three) state the same two fees to the cent. The 50 lume are the buyer's price for a paper copy of documents that are free electronically (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`) in a procedure with electronic submission; that a tenderer in Urvania that submits electronically bought the paper copy needs a reason. The 12 lume are a courier cost of the tenderer itself; a tender is an offer to the buyer, and nothing says why the tenderer's own cost of delivering its guarantee is part of the offer, who owes it to whom, or whether it is included in the price (the payable amount is the sum of the lines, so it is not). (The guarantee was issued by a bank in Lumeport for a beneficiary in Lumeport, example 14, so the courier's route is not evident either.)
- Condition: a fee stated in the tender is one that plays a part between tenderer and buyer under this tender, with a reason in the story for this tenderer; costs the tenderer bears itself are not in the tender.
- Options: (a, preferred) no fees in the tenders; (b) keep the documentation fee only in the tender of a tenderer that the story says bought the paper copy, as a record that it was paid.
- Needs decision: yes

### tender/15#F5 · Low · The tender does not point to its tender guarantee
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: the terms require a tender guarantee of 2400.00 lume, constituted by the tender deadline (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-02-26`). The only trace of it in the tender is the courier fee. The certificate exists in the flow (`14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`, issued the day before), but the tender's document references name only the call for tenders, the data sheet, the qualification and a reference list. A buyer checking admissibility cannot link the tender to its guarantee.
- Condition: the tender references the guarantee (certificate or guarantee number) that covers it.
- Options: (a, preferred) a document reference to the guarantee certificate among the tender's references; (b) leave it to the certificate, which names the tenderer and the procedure, and say so.
- Needs decision: no

## Checked and consistent
- Lines: 119760.00 + 4320.00 = 124080.00 = `LineExtensionAmount` = `PayableAmount` (tax zero). Unit prices: 119760.00 / 240 = 499, 4320.00 / 240 = 18; the bench price lies within the criterion's limits of 350 to 600 lume.
- Order quantities: minimum 20, maximum 96, increment 4 (a pallet of 4): the average release of 40 benches (240 in six releases) fits all three.
- Validity 90 days as required by the terms; amounts in lume, the currency of the procedure.
- The same amounts appear in the award (`22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:AwardedTenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `124080.00`); line 2 is the amount of the subcontract there (4320.00, 18 lume a bench); the first release is invoiced at the same unit prices (40 × 499 + 40 × 18 = 20680.00).
- With the terms' formula the price score is 60 × 119040 / 124080 = 57.6 against 60 for the other tender, and ten years against six on the quality criterion; the award to this tender on the best price-quality ratio is consistent with that.

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: suspected that the payable amount should be reduced by the withholding tax that the invoice later deducts on the installation — refuted because the tender states the price; what the buyer withholds and pays to the tax office is a matter of settlement, shown on the invoice.
- `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount`: suspected that the subcontracted share exceeds what the terms allow — refuted: 4320 / 124080 = 3.5 %, under the maximum of 30 %.

## Outside this review
- The tender's amounts equal the buyer's published estimate to the cent in both lots; that is raised in the reviews of the notices (examples 01 to 03).
- The announced electronic auction leaves no trace in the flow; raised in the reviews of examples 02 and 03.
