# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/04-Invoice.xml`, Git blob `b7615e989edc233d99c6d2b1a77b5e429b9d95e3` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/04#F1 · Low · The invoice says nothing about the delivery it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `20000`
- Why: The invoice bills 20 000 garment bags delivered DAP to the mill (`03-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`), but carries no `Delivery` (no actual delivery date or place) and no despatch reference; the flow has no despatch advice for this order either, and the order gives no date. So nowhere in the flow is it recorded when the bags arrived, which under DAP is when the seller's obligation was fulfilled and what the invoice bills. Completeness remark.
- Condition: the invoice states when the bags were delivered (an actual delivery date at the DAP place), or refers to a document that records it.
- Options: (a, preferred) add `cac:Delivery/cbc:ActualDeliveryDate` (with the place if useful); (b) leave it and record that the order reference suffices.
- Needs decision: no

### packaging/04#F2 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523` resolves to `03-Order.xml` (an order with the same buyer and seller); the invoice (2026-05-03) is issued after the order (2026-04-29).
- Quantity and item against the order: `20000` EA equals `03-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20000` (40 boxes of 500); the seller's item ID `RP-GB-60`, item number, HS `392321` and CPC `36410` are the same.
- `check_ids.py`: the account and the RF reference `RF72RPINV260524` pass.
