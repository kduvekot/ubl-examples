# LLM review: 14-DebitNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/14-DebitNote.xml`, Git blob `46010db5dff2abd14661e7fabad9e7fd90e953c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### furniture/14#F1 · Low · Contract document reference names the quotation, not the contract of the flow
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`
- Why: UBL: "A reference to a contract associated with this document." BF-DOC-26-0568 is the seller's Quotation (`02-Quotation.xml`). The flow names a different contract for the same supply relation, the store's own-brand contract (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`). An accepted quotation can be the contractual document of a sale, so the reference is not wrong in kind, but two contracts for the same relation are left side by side, and the charge here (return transport at the maker's request) arises from neither of them explicitly. The cancellation does the same (`11-OrderCancellation.xml:/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`).
- Condition: the contract referenced is the one under which the transport charge arises, and the flow names one contract for the supply relation, or says how the quotation and the own-brand contract relate.
- Options: (preferred) reference BM-OWN-BRAND-2026 if the own-brand contract provides for return transport at the maker's request; or keep the quotation and move it to an `AdditionalDocumentReference`, since the debit note's reason is the return instruction, which is already referenced.
- Needs decision: no

## Checked and consistent
- References: BF-CN-26-0579 resolves to `13-CreditNote.xml` (credit note line 1, 3477.00, with the restocking deduction 183.00, both as quoted in the billing reference line); BF-DOC-26-0578 resolves to `12-InstructionForReturns.xml`; BS-PO-26-0574 resolves to `08-Order.xml`, the order under which the returned sets were bought.
- Delivery: `/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02` lies within the period requested in `12-InstructionForReturns.xml` (2026-04-29 to 2026-05-02); the location GLN 9523710900015 passes the check digit and shares its first eleven digits (95237109000) with the maker's party GLN 9523710900008, i.e. the maker's own numbering.
- Transport: 282 kg in six sets (`12-InstructionForReturns.xml`) fits a delivery van; one service unit at 85 = 85.00.
- Codes: 383, 35 (goods returned), E48 resolve and fit the charge.

## Considered and refuted
- `/DebitNote/cac:DebitNoteLine/cbc:Note` = `Collected with the store's van.`: suspected a contradiction with `12-InstructionForReturns.xml` ("The maker takes back six sets") about who transports — refuted because "takes back" means the maker accepts the return, and the store charging for its own van is consistent with that; the instruction's silence on the carrier is a finding of `12-InstructionForReturns.xml`.
- `/DebitNote/cac:OrderReference/cbc:ID` = `BS-PO-26-0574`: suspected an order reference for a service that was never ordered — refuted because UBL defines it as "an Order with which this Debit Note is associated", and the returned goods come from that order.
