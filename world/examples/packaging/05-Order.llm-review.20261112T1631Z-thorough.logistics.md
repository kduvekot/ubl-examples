# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/05-Order.xml`, Git blob `5869f45d431110e527ca796d40b56bf3f3390192` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### packaging/05#F1 · Low · The order says nothing about when the shirts are wanted
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: The order names the delivery party and DDP to the store's goods-in, but gives no requested delivery period or latest delivery date. The despatch advice calls this "The store's spring order of shirts" (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `The store's spring order of shirts.`), a seasonal order for which the wanted date matters. Completeness remark. The same gap occurs in 15 of the world's 18 orders (`*/*-Order.xml` without any of `RequestedDeliveryPeriod`, `PromisedDeliveryPeriod`, `EstimatedDeliveryPeriod`, `LatestDeliveryDate`, `RequestedDespatchPeriod`).
- Condition: the order states when the shirts are to be delivered.
- Options: (a, preferred) add `Delivery/cac:RequestedDeliveryPeriod`; (b) `Delivery/cbc:LatestDeliveryDate`.
- Needs decision: no

### packaging/05#F2 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- Delivery: `/Order/cac:DeliveryTerms/cbc:ID` = `DDP` to `Brightmarket Stores, goods-in, Lumeport`, delivery party the buyer itself (`20410411`). Both parties are in Lumeport, Bayvarra, so no duties arise; DDP is still a valid term for a domestic sale (Incoterms 2020 apply to domestic contracts). The seller arranges carriage, and the despatch advice (`06-DespatchAdvice.xml`) names the seller's carrier, consistent with DDP.
- Item identification: the buyer's (`BM-778120`), seller's (`LT-SH-01`) and world item number are the same in `06-DespatchAdvice.xml` and `07-Invoice.xml` (the invoice without the buyer's ID); in the store's receipts `08-PurchaseReceipt.xml` and `09-PurchaseReceipt.xml` the store's `BM-778120` is the seller's ID and `LT-SH-01` the manufacturer's, as the roles change.
- Codes: HS `620520` (men's shirts of cotton) and CPC `28232` fit a woven men's cotton shirt; origin XB is right for a shirt made in Bayvarra from Lisavan cotton (origin is where the shirt is made, not where the cotton grew).
