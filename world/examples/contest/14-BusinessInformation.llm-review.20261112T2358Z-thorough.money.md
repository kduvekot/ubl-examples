# LLM review: 14-BusinessInformation.xml

Flow: contest (CONTEST-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261112T2358Z-thorough`
- Example: `world/examples/contest/14-BusinessInformation.xml`, Git blob `ea59d9c8ec70285678a63c9762adc18d4f21b15e` (committed)
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

### contest/14#F1 · Low · Production capability amount without a measure, and implausible against Brackenmere's turnover
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6830000.00`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: `BusinessCapability/ValueAmount` is "A monetary amount as a measure of this capability". The extract gives Brackenmere Furniture a production capability of 6,830,000 lume with no period, quantity or evidence, so a reader cannot tell what is measured (yearly output, capacity, plant value). The same party declared a yearly turnover of 410,000 lume for 2025 in the parks tender a few months earlier (`tender/07-QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseAmount` = `410000.00`); a production capability some 15 times the company's turnover is not plausible for a small furniture maker, and the digits after the leading 6 (410,000) suggest a slip. Compare Valdara's extract in the same register, which states quantity and evidence with its amount (`tender/12-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`). Version 1 of the same extract, four days earlier, has 6,410,000 (`13-BusinessInformation.xml:/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `6410000.00`); this amount is the only change between the versions (diff of the two `*.xml`), and nothing says why it changed.
- Condition: The capability amount says what it measures (period, or quantity and evidence) and agrees with what Brackenmere states about its turnover elsewhere; any change between the extract's versions is explained.
- Options: (a, preferred) restate the capability as a yearly production value in line with the 410,000 lume turnover, with the period or quantity that gives it meaning, because the extract is evidence the jury relies on; (b) if a capacity much larger than turnover is meant, describe it as capacity in the description and give the quantity it rests on.
- Needs decision: yes

### contest/14#F2 · Low · The receiving authority's tax scheme carried in a register extract about another party
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-0900002`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme` is "A tax scheme applying to this party". This BusinessInformation carries tax registrations (including the contracting authority's sales tax exemption), but nothing in it is taxed, priced, invoiced or paid, and no element refers to a tax registration: the values look copied from the parties' master data. Under the agreed rule "no fillers" (UBL IND5/IND6) a value needs a business reason in the document. The contracting authority's exemption from the state sales tax (`PUBLIC`, "A body of the federation, a state or a city buys free of sales tax") matters for what it buys and pays; this document neither prices nor pays anything, so it has no use for it either.
- Condition: Every `PartyTaxScheme` left in this document serves something the document does (a priced or paid amount, a tax-dependent criterion), or it is absent.
- Options: (a, preferred) remove the tax schemes listed, because the document has no tax content; (b) keep one only where the story gives this document a tax reason, and say so where the reason is not obvious.
- Needs decision: no

## Checked and consistent
- Brackenmere's tax registration in the extract (`UL-1237398`, state sales tax of Upland State, currency `XBL`) is the same as in every other example of the flow that carries it.
- Currency `XBL` of the capability amount is the currency of the register's country (Bayvarra).

## Considered and refuted
- `/BusinessInformation/cac:BusinessParty/cac:PartyTaxScheme`: suspected as master data copied into the extract — refuted because a register extract reports the registrations the register holds about the party it describes.
