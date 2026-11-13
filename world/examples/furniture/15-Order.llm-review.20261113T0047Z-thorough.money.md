# LLM review: 15-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/15-Order.xml`, Git blob `c87a13cb9349700b274d702bf91f928dddf95d64` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### furniture/15#F1 · Low · Office furniture booked to the parks renewal programme
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Order as a whole" and `AccountingCost` the cost centre as text. The goods and work are six office desks and their installation, which the work report and invoice attach to the office project `PWD-PLAN-OFFICE-26` ("Furnishing: the new office is furnished" in 16-WorkReport). The cost centre is the parks renewal programme, which in the tender flow carries the park benches (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`, with project `PWD-PARKS-26`). Booking office desks to the parks programme is possible (e.g. if the new office serves the programme), but nothing in the flow says so, and the project and the cost centre point to different budgets.
- Condition: The buyer's cost centre for the desks and installation is the budget of the office project, or the flow states why the parks programme pays for the office.
- Options: (preferred) give the office project its own cost centre code and text in 15, 16 and 17; or say (e.g. in the order note) that the new office belongs to the parks renewal programme.
- Needs decision: yes

### furniture/15#F2 · Low · The party's own exemption is given with a transaction reason
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `PartyTaxScheme/ExemptionReasonCode` is "A reason for the party's exemption from tax, expressed as a code", i.e. the party's own status. The code used is the transaction-level reason of the same list (`/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`), whose meaning "Sale to a public body" describes a sale, not the department. The text after the colon does state the status ("public bodies are exempt"), so the meaning is recoverable, but code and element do not match. The same code and text are used at party level in all 55 party-level `ExemptionReasonCode` elements of the examples (`grep -rh --include='*.xml' -A1 '<cbc:ExemptionReasonCode'` over `world/examples`, 55 matches, all `PUBLIC`).
- Condition: The party-level exemption reason code names the party's status (e.g. "public body"), and the transaction-level code keeps naming the transaction; or the shared list records that one code serves both, with a definition that fits both.
- Options: (preferred) give the party-level element a status code (a separate list or a separate code such as "public body") and a text that states only the status; or redefine the code's name in the list so it fits both uses.
- Needs decision: no

## Checked and consistent
- Lines: 6 × 880 = 5280.00 (`/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `5280.00`); 14 h × 48 = 672.00 (`/Order/cac:OrderLine[2]/cac:LineItem/cbc:LineExtensionAmount` = `672.00`); sum 5952.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00` = `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `5952.00`; tax 0.00.
- Tax: exempt STT with reason `PUBLIC` for a sale to the city's public works department, the treatment 17-Invoice applies to both lines.
- Prices and quantities are the ones 16-WorkReport (14 h at 48) and 17-Invoice (6 desks at 880, 14 h at 48) use.
- Prices state their base quantity (1 EA, 1 HUR).

## Outside this review
- 17-Invoice adds a packaging-disposal charge of 24.00 that this order does not contain; the finding is recorded in the reviews of 16-WorkReport and 17-Invoice, where the charge appears.
