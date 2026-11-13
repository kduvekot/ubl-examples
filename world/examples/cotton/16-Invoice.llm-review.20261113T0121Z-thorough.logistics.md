# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/16#F1 · High · "45 days net", but due after 30 days
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-02`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-01`
- Why: Calculated: 2026-03-02 + 45 days = 2026-04-16; 2026-04-01 is 30 days after the issue date. The terms and all three due dates contradict each other. (The same terms ID `XL-STD` and note in 04 give the right 45-day date there.)
- Condition: the terms note and every due date of the invoice agree.
- Options: (preferred) set the due dates to 2026-04-16; or change the note to 30 days if the gin grants the mill shorter terms (then also a terms ID other than `XL-STD`, which in 04 means 45 days).
- Needs decision: no

### cotton/16#F2 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal bale weight in kilograms. Same as in 02, 07, 08, 10, 11 and 15.
- Condition: `PackSizeNumeric`, where present, is a count; the nominal bale weight is stated where a weight belongs.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an item property, and if wanted the 27 bales in the description.
- Needs decision: no

### cotton/16#F3 · Low · Export invoice says nothing about the delivery
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: The invoice is for goods shipped from Lisavu to Bayvarra on 2026-03-02 (13), issued the same day after the bill of lading. It carries no delivery date, no delivery terms (FOB Port of Selanu in the order 08) and no reference to the shipment or the bill of lading `TOL-BL-26-0206`. The buyer's customs declaration (15) and the transfer of risk under FOB both rest on these; an export commercial invoice normally states them. This is a completeness remark.
- Condition: the invoice states the actual delivery (date shipped on board, place) and the Incoterms rule agreed in 08, and refers to the transport document.
- Options: (preferred) add `Delivery` (actual delivery date 2026-03-02, Port of Selanu), `DeliveryTerms` FOB and a document reference to `TOL-BL-26-0206`.
- Needs decision: no

## Checked and consistent
- `OrderReference` `LTM-PO-26-0198` and `OrderLineReference` line 1 resolve to the order 08; 6129 KGM × 0.988 = 6055.452 XLC as ordered.
- `18-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` refers to this invoice with its issue date 2026-03-02 and pays the full 6055.452 XLC on 2026-03-29.
- The classing certificate of the item (signature 2026-02-20) predates the invoice; item `SCG-LINT`, HS 520100 and quantity agree with 08, 10, 11 and 15.
- `check_ids.py`: RF reference `RF46SCGINV260210` and the gin's account `XL31BSEL0020004922263` have valid check digits; the account is the one the gin pays from in 06.
