# LLM review: 03-Order.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/03-Order.xml`, Git blob `f14d6ba97f84855490d38ffc0a4d1386846aa813` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/03#F1 · Low · Order states no delivery date and gives the delivery place only as text
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Valdara Industries, goods-in, Ferrano`
- Why: the order's `Delivery` names only the receiving party; it carries no `RequestedDeliveryPeriod` (or `PromisedDeliveryPeriod`), so the binding document of the purchase does not say when the 4800 slats are to arrive. The window exists only in the quotation it refers to (`02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`), and the transport request then plans a different one (see the review of `04-TransportExecutionPlanRequest.xml`, this run). The DAP place is given only as free text, while the request for quotation gives the same text as the location's name (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`), and the transport request gives the place with a full address. The same place is thus described three ways, and the order, which fixes the named place of the Incoterm, has neither address nor identifier.
- Condition: the order states the delivery period it accepts (or explicitly the one of the quotation), and the DAP delivery location is identified the same way as in the other examples of the flow (name and address, or an identifier).
- Options: (a) preferred: add `Delivery/RequestedDeliveryPeriod` with the window the parties agreed, and give `DeliveryTerms/DeliveryLocation` a name and address matching `04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation`; (b) at least the period, leaving the place as text.
- Needs decision: no

## Checked and consistent
- Reference `/Order/cac:QuotationDocumentReference/cbc:ID` = `MS-DOC-26-0626` resolves to `02-Quotation.xml` (a quotation, issued 2026-02-19, valid to 2026-03-21); the order of `/Order/cbc:IssueDate` = `2026-02-22` is within its validity.
- Quantity `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `4800` and item (seller's ID `MS-SL-1800`, dimensions 1800 × 95 × 38 mm, HS `440799`) agree with the quotation and with the despatch advice and customs declarations that follow.
- Incoterm `/Order/cac:DeliveryTerms/cbc:ID` = `DAP`, as quoted; the seller then books and pays the haulage (`04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`), as DAP requires.
- The order is referenced as `VI-PO-26-0627` by `06-DespatchAdvice.xml`, `08-Invoice.xml` and `05-ExportCustomsDeclaration.xml`; all resolve.
