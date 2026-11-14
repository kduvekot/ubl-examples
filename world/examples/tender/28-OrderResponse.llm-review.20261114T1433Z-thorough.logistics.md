# LLM review: 28-OrderResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/28-OrderResponse.xml`, Git blob `3ed78b3450611e60a961e71c98db29842ff2963f` (committed)
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

### tender/28#F1 · High · Reference to "another order" that does not exist
- XPath: `/OrderResponse/cac:OrderDocumentReference/cbc:ID` = `PWD-PO-26-0212`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: OrderDocumentReference is "a reference to an Order other than the one being responded to". No order `PWD-PO-26-0212` exists (grep for `>PWD-PO-26-0212<` over `world/examples/**/*.xml`: this example only); the value is the number of the order being responded to without its first letter. The flow has a single order, so there is no other order to refer to.
- Condition: The element is absent, or refers to an existing order that is not `LPWD-PO-26-0212`.
- Options: remove it (preferred).
- Needs decision: no

### tender/28#F2 · Low · The seller's response gives neither its own order number nor a delivery date
- XPath: `/OrderResponse/cac:OrderReference`
- Why: The buyer's order carries a seller's order number (`26-Order.xml:/Order/cbc:SalesOrderID` = `VI-SO-26-0058`), which only the seller can assign; the seller's own response, the natural first place for it (`cbc:SalesOrderID`, "an identifier for the Order, assigned by the seller", also available in `cac:OrderReference`), does not have it. Nor does the response promise a delivery date, although the order requests none and the accepted change (a special colour) affects the lead time; the penalty clause of the contract counts days late.
- Condition: The seller's order number appears in the seller's response if it exists at all; the release has a delivery date either requested (order) or promised (response).
- Options: (a) preferred: `cbc:SalesOrderID` VI-SO-26-0058 here (and not in the order), plus a `cac:Delivery/cac:PromisedDeliveryPeriod`; (b) leave the response minimal and fix the date in the order.
- Needs decision: no

## Checked and consistent
- No identifiers with check digits (`check_ids.py` reports no failures).
- `cac:OrderReference/cbc:ID` LPWD-PO-26-0212 and `cac:OrderChangeDocumentReference/cbc:ID` LPWD-OC-26-0213 exist and are of the right kind; the response (25 March 16:15) follows both and lies within the change's validity (until 27 March).
- OrderResponseCode AP = "Accepted" (UNCL 4343) agrees with the note "Accepted: moss green, at the quoted charge."
- Amounts are those of the order change: 19960.00 + 200.00 = 20160.00; charge reason CAT, "Special colour".
- A response without order lines is allowed for an unconditional acceptance.

## Considered and refuted
- `/OrderResponse/cac:PricingExchangeRate/cbc:Date`: `2026-01-02` in a document of 25 March — refuted here: it is the date of the forward contract the rate comes from, the same in 26 and 27 (question raised in the review of 26).
- `/OrderResponse/cbc:OrderResponseCode`: `AP` although the order was changed — refuted: the change is accepted too (it is referenced), so the order as amended is accepted without amendment by the seller.
