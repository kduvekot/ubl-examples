# LLM review: 11-OrderCancellation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/11-OrderCancellation.xml`, Git blob `f390fff919e1ccd9ec4fabfe839b81fd2f19846c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### furniture/11#F1 · Medium · Contract identified by the quotation's document number, not by the contract of the flow
- XPath: `/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`
- Why: UBL: `Contract` is "A contract associated with the original Order(s)", and its `ID` "An identifier for this contract". BF-DOC-26-0568 is the document ID of the seller's Quotation (`02-Quotation.xml:/Quotation/cbc:ID` = `BF-DOC-26-0568`), i.e. a document number used as a contract identifier. The flow already names the contract the orders fall under: the store's own-brand contract (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`). The cancelled order (`10-Order.xml`) names no contract. Two different contract identifiers for the same supply relation contradict each other. The debit note does the same (`14-DebitNote.xml:/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`).
- Condition: the contract named in the cancellation is the contract of the flow (BM-OWN-BRAND-2026), or the cancellation names no contract; the quotation, if referenced, is referenced as a document.
- Options: (preferred) set `Contract/ID` to BM-OWN-BRAND-2026, the contract the request for quotation was made under; or remove `Contract`, since the cancellation needs only the order reference.
- Needs decision: no

### furniture/11#F2 · Low · Originator document is the seller's exception notification
- XPath: `/OrderCancellation/cac:OriginatorDocumentReference/cbc:ID` = `BF-DOC-26-0573`
- Why: UBL: "A reference to an originator document associated with this document"; in the ordering documents the originator is the `OriginatorCustomerParty` ("The originator"), here Brightmarket Stores, and its document is the requisition behind the order. BF-DOC-26-0573 is the seller's Exception Notification (`07-ExceptionNotification.xml`), issued by Brackenmere. It is the trigger of the cancellation, but not a document of the originator. Read loosely ("the document that gave rise to this cancellation") the use is defensible, so the finding needs a decision.
- Condition: the originator document reference points to a document of the originator customer party, or the exception notification is referenced as an additional document.
- Options: (preferred) move BF-DOC-26-0573 to an `AdditionalDocumentReference`, next to the Product Activity report already there; or keep it, if the world reads "originator document" as the cause of the cancellation, and record that reading.
- Needs decision: yes

### furniture/11#F3 · Low · "Cancelled before production" after the agreed lead time has passed
- XPath: `/OrderCancellation/cbc:Note` = `No cost: cancelled before production.`
- XPath: `/OrderCancellation/cbc:IssueDate` = `2026-04-22`
- Why: The cancelled order was issued on 2026-04-16 (`10-Order.xml:/Order/cbc:IssueDate` = `2026-04-16`) without a requested delivery date, so the agreed lead time applies (`04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:LeadTimeMeasure` = `5`, days). The delivery was then due on 2026-04-21 (calculated: 2026-04-16 + 5 days), one day before this cancellation. A cancellation six days after the order, after the due delivery date, can hardly come "before production". The contradiction rests on the missing delivery date of `10-Order.xml` (its finding F2).
- Condition: the cancellation date lies before the production or delivery date the flow implies for the cancelled order.
- Options: (preferred) give `10-Order.xml` a requested delivery period well after 2026-04-22 (e.g. the summer peak), which makes "before production" true; or move the cancellation before 2026-04-21, which conflicts with the exception notification of 2026-04-21 17:49 that triggered it.
- Needs decision: yes

## Checked and consistent
- References: `/OrderCancellation/cac:OrderReference/cbc:ID` = `BS-PO-26-0576` resolves to `10-Order.xml`, an order of the same buyer and seller, issued before the cancellation; BS-DOC-26-0572 resolves to `06-ProductActivity.xml`; BF-DOC-26-0573 resolves to `07-ExceptionNotification.xml`.
- Order of events: product activity 2026-04-20 16:35 → exception notification 2026-04-21 17:49 → cancellation 2026-04-22 11:51.
- The cancellation note ("the second delivery") agrees with `10-Order.xml` being the repeat order after `08-Order.xml`.
