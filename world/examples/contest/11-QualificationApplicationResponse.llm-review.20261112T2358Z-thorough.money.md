# LLM review: 11-QualificationApplicationResponse.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/11-QualificationApplicationResponse.xml`, Git blob `786906485480cbed630ad927abbdceded6391e3d` (committed)
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

### contest/11#F1 · Low · Tax schemes carried in a document that does nothing with tax
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/QualificationApplicationResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". This QualificationApplicationResponse carries tax registrations (including the contracting authority's sales tax exemption), but nothing in it is taxed, priced, invoiced or paid, and no element refers to a tax registration: the values look copied from the parties' master data. Under the agreed rule "no fillers" (UBL IND5/IND6) a value needs a business reason in the document. The contracting authority's exemption from the state sales tax (`PUBLIC`, "A body of the federation, a state or a city buys free of sales tax") matters for what it buys and pays; this document neither prices nor pays anything, so it has no use for it either.
- Condition: Every `PartyTaxScheme` left in this document serves something the document does (a priced or paid amount, a tax-dependent criterion), or it is absent.
- Options: (a, preferred) remove the tax schemes listed, because the document has no tax content; (b) keep one only where the story gives this document a tax reason, and say so where the reason is not obvious.
- Needs decision: no

## Checked and consistent
- The document has no amounts, prices, payment means or financial criteria (searched for `Amount`, `currencyID`, `Price`, `Payment`, `Percent` in the `*.xml`); its criteria are professional qualification and references only, so there is no money arithmetic to check.
- Brackenmere's tax registration `UL-1237398` is the same as in every other contest example that carries it (04, 05, 06, 07, 09–16) and in its register extract (13, 14).

## Considered and refuted
- `/QualificationApplicationResponse/cac:ContractingParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`: suspected that the reason describes a transaction rather than the party's status — refuted because the list defines it as the buyer's status ("A body of the federation, a state or a city buys free of sales tax"); its presence is part of finding F1.
- Missing financial standing criterion (turnover): considered whether a qualification request without one lacks something the document needs — refuted because a design contest selects participants on their references and professional qualification; nothing in the flow asks for financial standing.
