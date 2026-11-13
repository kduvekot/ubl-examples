# LLM review: 07-TendererQualification.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/07-TendererQualification.xml`, Git blob `b7c5c10127f35b254eea1a4905b11113ef334e8c` (committed)
- Last commit changing the example: 50682e5 2026-11-11 Stage 5, tender part: a design contest with revised documents
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

### contest/07#F1 · Low · Tax schemes carried in a document that does nothing with tax
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1232055`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/TendererQualification/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". This TendererQualification carries tax registrations (including the contracting authority's sales tax exemption), but nothing in it is taxed, priced, invoiced or paid, and no element refers to a tax registration: the values look copied from the parties' master data. Under the agreed rule "no fillers" (UBL IND5/IND6) a value needs a business reason in the document. The contracting authority's exemption from the state sales tax (`PUBLIC`, "A body of the federation, a state or a city buys free of sales tax") matters for what it buys and pays; this document neither prices nor pays anything, so it has no use for it either.
- Condition: Every `PartyTaxScheme` left in this document serves something the document does (a priced or paid amount, a tax-dependent criterion), or it is absent.
- Options: (a, preferred) remove the tax schemes listed, because the document has no tax content; (b) keep one only where the story gives this document a tax reason, and say so where the reason is not obvious.
- Needs decision: no

## Checked and consistent
- Shares of the group: `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent` = `60` and `/TendererQualification/cac:TendererPartyQualification/cac:AdditionalQualifyingParty/cbc:ParticipationPercent` = `40` add up to 100 (calculated).
- The document has no amounts, prices or payment data (searched for `Amount`, `currencyID`, `Price`, `Payment` in the `*.xml`).
- The tax registrations of Brackenmere (`UL-1237398`) and Saltmere (`UL-1232055`) are the same in 07 and 12.

## Considered and refuted
- `/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:ParticipationPercent`: considered whether the shares should match a split of prize money or of the follow-up fee — refuted because no document of the flow states such a split; the percentage is the members' share in the group, as its definition says.
