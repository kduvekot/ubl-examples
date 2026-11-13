# LLM review: 15-ContractAwardNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/15-ContractAwardNotice.xml`, Git blob `df753bf00bfa8a999e3e4cf1826906a62184db6d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 219a684 2026-11-12 Reviews of the road flow, run 20261112T2311Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### contest/15#F1 · High · First prize of 6,000 lume contradicts the contest notice it refers to
- XPath: `/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`
- XPath: `/ContractAwardNotice/cac:PreviousDocumentReference/cbc:ID` = `LPWD-DOC-26-0634`
- Why: `Prize/ValueAmount` is "The monetary value amount of a prize". The award notice refers to contract notice LPWD-DOC-26-0634, which in both of its versions promises 8,000 lume for the first prize (`03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`, `08-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), as do the corrected prior information notice and both calls for tenders (`02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`, `09-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`). 6,000 is the amount of the superseded first version of the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`). The second prize (4,000) matches. Version 2 of this award notice changes exactly this amount to 8,000 (`16-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), so the story may mean this as an error that is then corrected; but neither notice says so (the note of both is `Results of the design contest for the harbour promenade bench.`), and as it stands the published result awards less than the contest notice promised.
- Condition: The first-prize amount in the award notice equals the 8,000 lume of the contract notice it refers to; or, if version 1 is meant to carry an error that version 2 corrects, the corrected version states that it corrects the first-prize amount.
- Options: (a) set the first prize to 8,000 here and keep version 2 for another real change; (b, preferred if the correction is part of the story) keep 6,000 as the error and let version 2 say in a note that it corrects the first-prize amount from 6,000 to 8,000 lume, so the correction is visible to readers of the notice.
- Needs decision: yes

### contest/15#F2 · Low · What the estimated contract amount of 54,000 lume covers is not stated, and it does not follow the prize change
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/ContractAwardNotice/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `RequestedTenderTotal` holds "Budget monetary amounts for the project as whole" and `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". The project procured here is a design contest for services (`ProcurementTypeCode` `SERVICES`, UN CPC 83912, industrial design services): prizes, payments of 1,000 lume to each of at most five participants, and a follow-up service contract for the detailed design and the supervision of production. Nothing says what the 54,000 lume consist of. The figure equals exactly 60 × the 900 lume production limit per bench in the description, which suggests it is the production cost of the benches: a supply or works contract that this procurement does not award. Read instead as prizes, payments and the follow-up service contract (the usual way of valuing a design contest, e.g. Directive 2014/24/EU Art. 78, from my own knowledge), it should have changed when the prizes changed. The first prize rose from 6,000 in `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00` to 8,000 from version 2 of the prior information notice onwards, yet the estimate is 54,000 in every notice of the flow (8 of the 16 contest `*.xml` carry `EstimatedOverallContractAmount`, all with `54000.00`; counted with `grep -c EstimatedOverallContractAmount world/examples/contest/*.xml`).
- Condition: The estimated overall contract amount is the estimated value of what this procurement buys (the prizes and payments and/or the follow-up service contract), it agrees with the prize amounts of the same version, and what it covers can be read from the notice.
- Options: (a, preferred) keep an estimate of prizes, payments and follow-up service contract, state what it covers (e.g. in the project description), and adjust it in the version where the first prize rose, because that is what the element means for a design contest; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal`, since production is not procured here, and keep the per-bench limit in the description.
- Needs decision: yes

### contest/15#F3 · Low · Tax schemes carried in a document that does nothing with tax
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[1]/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/ContractAwardNotice/cac:TenderResult/cac:WinningParty[2]/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". This ContractAwardNotice carries the economic operators' tax registrations, but nothing in it is taxed, priced, invoiced or paid, and no element refers to a tax registration: the values look copied from the parties' master data. Under the agreed rule "no fillers" (UBL IND5/IND6) a value needs a business reason in the document.
- Condition: Every `PartyTaxScheme` left in this document serves something the document does (a priced or paid amount, a tax-dependent criterion), or it is absent.
- Options: (a, preferred) remove the tax schemes listed, because the document has no tax content; (b) keep one only where the story gives this document a tax reason, and say so where the reason is not obvious.
- Needs decision: no

## Checked and consistent
- Only the first and second prize are listed, in line with `TenderResult/Description` ("The jury withheld the third prize: no other design reached prize standard.") and the conditional third prize of the contest notice.
- Second prize 4,000 lume equals the contest notice (`03-ContractNotice.xml:/ContractNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[2]/cbc:ValueAmount` = `4000.00`).
- Four designs received (`ReceivedTenderQuantity` 4) is within the five participants the contest provided for, so the participation payments stay within the announced 1,000 lume each (at most 4,000 lume, calculated).
- Prizes are stated in `XBL` also for the Urvanian second-prize winner, whose own tax currency is `XUF`; the prize is the buyer's commitment in its own currency, which is consistent.

## Considered and refuted
- `/ContractAwardNotice/cac:TenderingProcess/cbc:NegotiationDescription`: considered whether the award notice should state the value of the follow-up service contract — refuted because that contract is still to be negotiated ("on fees, timetable and the number of prototypes"); the notice reports the contest result, whose amounts are the prizes.
- `/ContractAwardNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as master data copied into the notice — refuted because the buyer's exemption from the state sales tax bears on the follow-up service contract the notice announces (its fees are net of that tax).
