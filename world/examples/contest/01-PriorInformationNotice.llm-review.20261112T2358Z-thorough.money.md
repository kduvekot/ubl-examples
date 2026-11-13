# LLM review: 01-PriorInformationNotice.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/01-PriorInformationNotice.xml`, Git blob `eabac2882841f25d8b6985b6d92b45b2d3caf81b` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### contest/01#F1 · Low · What the estimated contract amount of 54,000 lume covers is not stated, and it does not follow the prize change
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`
- XPath: `/PriorInformationNotice/cac:ProcurementProject/cbc:Description` = `A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in salt air, accessible, and buildable for at most 900 lume a bench.`
- Why: `RequestedTenderTotal` holds "Budget monetary amounts for the project as whole" and `EstimatedOverallContractAmount` is "The estimated overall monetary amount of a contract". The project procured here is a design contest for services (`ProcurementTypeCode` `SERVICES`, UN CPC 83912, industrial design services): prizes, payments of 1,000 lume to each of at most five participants, and a follow-up service contract for the detailed design and the supervision of production. Nothing says what the 54,000 lume consist of. The figure equals exactly 60 × the 900 lume production limit per bench in the description, which suggests it is the production cost of the benches: a supply or works contract that this procurement does not award. Read instead as prizes, payments and the follow-up service contract (the usual way of valuing a design contest, e.g. Directive 2014/24/EU Art. 78, from my own knowledge), it should have changed when the prizes changed. In this first version the first prize is 6,000 lume; in the next version the first prize rises to 8,000 (`02-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `8000.00`), but the estimate stays the same (`02-PriorInformationNotice.xml:/PriorInformationNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:EstimatedOverallContractAmount` = `54000.00`).
- Condition: The estimated overall contract amount is the estimated value of what this procurement buys (the prizes and payments and/or the follow-up service contract), it agrees with the prize amounts of the same version, and what it covers can be read from the notice.
- Options: (a, preferred) keep an estimate of prizes, payments and follow-up service contract, state what it covers (e.g. in the project description), and adjust it in the version where the first prize rose, because that is what the element means for a design contest; (b) if 54,000 is the production budget, remove it from `RequestedTenderTotal`, since production is not procured here, and keep the per-bench limit in the description.
- Needs decision: yes

## Checked and consistent
- Prizes: `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[1]/cbc:ValueAmount` = `6000.00`, second 4,000, third 2,000 lume; `PrizeDescription` ("Three prizes; the first is 6,000 lume.") agrees with the three `Prize` aggregates and their ranks.
- Currency: every amount is in `XBL` (Lume), the currency of the contracting authority's tax scheme (`TaxScheme/CurrencyCode` `XBL`).
- Payments to participants: 1,000 lume to each selected participant that submits a conforming design; with at most five participants (`EconomicOperatorShortList/MaximumQuantity` 5) the outlay is at most 5,000 lume, and prizes plus payments total at most 17,000 lume (calculated).
- The change of the first prize to 8,000 lume in version 2 (02) is a legitimate change of a notice in a new version (`VersionID` 2, `PreviousVersionID` 1); the later notices follow it.

## Considered and refuted
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction ("Sale to a public body") rather than the party's own status — refuted because the list defines the code as "A body of the federation, a state or a city buys free of sales tax", a status of the buyer, and `ExemptionReason` says so ("public bodies are exempt from the state sales tax").
- `/PriorInformationNotice/cac:ContractingParty/cac:Party/cac:PartyTaxScheme`: suspected as master data copied into a notice without tax content — refuted because the notice sets a production limit of 900 lume a bench and announces a follow-up service contract; the buyer's exemption tells candidates that these amounts are net of the state sales tax.
- `/PriorInformationNotice/cac:TenderingTerms/cac:AwardingTerms/cac:Prize[3]/cbc:Description`: suspected that a third prize awarded only "if the jury finds it of prize standard" contradicts "Three prizes" and `PrizeIndicator` true — refuted because a conditional third prize is an ordinary contest term and the first two prizes are unconditional.
- `XBL` as currency: checked that it is not a code assigned in ISO 4217 (own knowledge: the assigned X-codes near it are XBA–XBD, bond-market units); it is the world's fictional Lume.
