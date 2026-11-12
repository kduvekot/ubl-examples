# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/07-Invoice.xml`, Git blob `0345a2bca9a5957f58f15a04460ca368ab893cee` (committed)
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

### packaging/07#F1 · Low · The invoice is not linked to the despatch advice of the goods it bills
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525`
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `600`
- Why: The shirts billed here were sent the same day under `06-DespatchAdvice.xml` (`06-DespatchAdvice.xml:/DespatchAdvice/cbc:ID` = `LTM-DA-26-0526`, issued 11:35, this invoice 14:49), but the invoice refers only to the order: it has no `DespatchDocumentReference` and no `Delivery` with a delivery date or place. The store has to match the invoice to its goods receipt through the order alone, and the flow records no delivery date anywhere (see the despatch advice's review). Completeness remark.
- Condition: the invoice refers to despatch advice `LTM-DA-26-0526`, or states the delivery (date, place) it bills.
- Options: (a, preferred) add `cac:DespatchDocumentReference` with `LTM-DA-26-0526`, since the document exists in the flow and is what goods-in matches against; (b) add `cac:Delivery` with the actual delivery date.
- Needs decision: no

### packaging/07#F2 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml` (same buyer and seller); the invoice is issued after the order and after the despatch advice.
- Quantity: 600 EA invoiced = 600 ordered (`05-Order.xml`) = 600 delivered (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`); item, seller's ID `LT-SH-01`, HS `620520`, CPC `28232` and properties agree.
- `check_ids.py`: the store's GLN, the account and the RF reference `RF18LTMINV260529` pass.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LT-SH-01`: suspected an inconsistency because the order and the despatch advice also carry the buyer's item ID `BM-778120` and the invoice does not — refuted because leaving out an optional identifier contradicts nothing; the item is still identified by the seller's ID and the world item number.
