# LLM review: 19-Tender.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/19-Tender.xml`, Git blob `21feca31f7c744f8e198c18ed5445abb1d1142ee` (committed)
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

### tender/19#F1 · Medium · The tender total is given as the amount tendered for the quality criterion; the price criterion gets no response
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:AwardingCriterionID` = `AC-2`
- XPath: `/Tender/cac:TenderedProject/cac:AwardingCriterionResponse/cbc:Amount` = `119040.00`
- Why: `Amount` is "the monetary amount tendered for this awarding criterion". The response answers criterion AC-2, which the call for tenders defines as the quality criterion (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[2]/cbc:AwardingCriterionTypeCode` = `QUALITY`, measured in years, 5 to 10), and the response itself is about warranty and coating. No money is tendered for a warranty criterion; 119040.00 is the total of the tender (`/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `119040.00`). The criterion that is about money is AC-1 (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:AwardingCriterion[1]/cbc:AwardingCriterionTypeCode` = `PRICE`, "The lowest total of unit prices", with a range of 350.00 to 600.00 lume, i.e. a unit price), and the tender carries no response to it. The same construction is in 15-Tender.xml and 17-Tender.xml.
- Condition: an `AwardingCriterionResponse/Amount` is present only under a response whose `AwardingCriterionID` is a criterion evaluated in money, and its value is the figure that criterion evaluates (for AC-1, a value comparable with the 350.00–600.00 range of the criterion, or the total if the criterion is redefined as a total); the response to AC-2 carries no amount.
- Options: (a, preferred) add a response to AC-1 with the amount the criterion evaluates and remove the amount from the AC-2 response, because that is what the two criteria of the call ask for; (b) remove the amount from the AC-2 response only and leave the price to the tender lines and totals.
- Needs decision: no

### tender/19#F2 · Low · Fees the tenderer paid are stated as fees of the tendered project
- XPath: `/Tender/cac:TenderedProject/cbc:FeeAmount` = `50.00`
- XPath: `/Tender/cac:TenderedProject/cbc:FeeDescription` = `Paper copy of the documents.`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeAmount` = `12.00`
- XPath: `/Tender/cac:TenderedProject/cac:AdditionalFee/cbc:FeeDescription` = `Courier of the guarantee's original.`
- Why: `FeeAmount` is "the fee amount for tendered projects" and `AdditionalFee` "an additional fee for this tendered project". The 50.00 lume is the contracting authority's charge for a paper copy of the procurement documents (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:FeeDescription` = `Electronic documents are free; paper copies cost 50 lume.`); the 12.00 lume is what the tenderer paid a courier to deliver its guarantee. Neither is part of the offer: they are not in the tender's totals, the authority already knows its own document fee, and the courier cost is the tenderer's own expense towards a third party, which the authority neither charges nor reimburses. The document does nothing with either amount, and the document does not say who owes them to whom. The identical two fees are in 15-Tender.xml and 17-Tender.xml, so this tenderer states them twice (withdrawn tender and this one) and both tenderers state the same courier cost. No guarantee of this tenderer occurs in the flow (14-GuaranteeCertificate.xml is the other tenderer's), so the courier fee cannot be tied to anything.
- Condition: every fee in the tender is an amount the tender's purpose uses (e.g. a fee the tenderer must show it has paid in order to be admitted, stated as such), or the fees are absent.
- Options: (a, preferred) remove both fees from the tender, because no rule of the call makes a tender's validity depend on them; (b) keep only the documentation fee, with a description that says it is the proof of payment of the fee required by the call, if the world has such a rule.
- Needs decision: no

### tender/19#F3 · Low · Zero tax without a tax category or exemption reason
- XPath: `/Tender/cac:TenderedProject/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:TotalTaxAmount` = `0.00`
- Why: `TaxTotal` is "a total amount of taxes of a particular kind", and `TaxAmount` "the total tax amount for a particular taxation scheme … the sum of the tax subtotals for each tax category within the taxation scheme". The tender states zero tax twice but names neither the scheme nor the category, so the reader cannot tell whether no tax applies, which tax was considered, or why it is zero. The call gives the basis (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`, state sales tax, category E), and the tenderer is a Bayvarran seller under that tax.
- Condition: the zero tax of the tender is tied to a tax scheme and category with its exemption reason (a `TaxSubtotal` with `TaxCategory`), or the tender makes no tax statement.
- Options: (a, preferred) add a `TaxSubtotal` with taxable amount 119040.00, category E, reason PUBLIC and scheme STT, matching the call; (b) drop `TaxTotal`, `TotalTaxAmount` and `TaxInclusiveLineExtensionAmount` and rely on the call's tax category.
- Needs decision: no

## Checked and consistent
- Totals: 115200.00 (line 1) + 3840.00 (line 2) = 119040.00 = `LegalMonetaryTotal/LineExtensionAmount` = `PayableAmount` (tax 0.00). Line 1: `TaxInclusiveLineExtensionAmount` 115200.00 = 115200.00 + 0.00.
- Unit prices implied: 115200.00 / 240 = 480.00 lume a bench, inside the call's range 350.00–600.00 (`RequestForTenderLine/MinimumAmount`, `MaximumAmount`); 3840.00 / 240 = 16.00 lume an installation.
- The note "It corrects the price per bench of the withdrawn tender" holds: 17-Tender.xml has 112800.00 / 240 = 470.00 a bench and the same 3840.00 for lot 2; nothing else in the money differs between the two tenders (compared with `diff`).
- Against the outcome: 119040.00 is below the winning 124080.00 (22-AwardedNotification.xml), which agrees with 23-UnawardedNotification.xml ("lower in price").
- Order quantities: minimum 20 and maximum 96 are multiples of the increment 4 and of the pallet content 4; the average release of the call (119760.00 / 19960.00 = 6 releases, 40 benches each) lies between them.
- All amounts are in XBL, the currency of the call.
- GLN 9523710900008: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Tender/cac:TenderedProject/cac:TenderLine[2]/cbc:LineExtensionAmount`: line 2 has no `TaxInclusiveLineExtensionAmount` and `TotalTaxAmount` although line 1 has them — refuted as a finding of its own because both are optional and the totals are consistent with zero tax on both lines; the missing tax basis is F3.
- `/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount`: the call evaluates unit prices (`PriceEvaluationCode` UNITPRICE) but the tender states only line totals — refuted because quantity and line amount are both present and give the unit price exactly (480.00); the missing response to the price criterion is F1.
- `/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount`: the fees (50.00, 12.00) are not in the payable amount — refuted because they are not part of the price offered; whether they belong in the tender at all is F2.
