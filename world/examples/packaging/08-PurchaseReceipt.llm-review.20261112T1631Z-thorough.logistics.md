# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/08-PurchaseReceipt.xml`, Git blob `9ece1e4003ae05ddafa0eb8d78c7dfd4d1e85d0d` (committed)
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

### packaging/08#F1 · Low · The shirt's GTIN is on the retailer's prefix, not the brand owner's
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: A GTIN is allocated by the brand owner of the trade item (GS1 General Specifications, own knowledge). The shirt is branded `Lumeport` and made by Lumeport Textile Mill (the item's manufacturer party), but its GTIN has the company prefix of Brightmarket Stores, the retailer: the store's own GLN is `9522610900002`, and `9522610000016` is built on the same prefix 9522610. A retailer allocates GTINs from its own prefix only to its own-label goods; for a manufacturer's brand without a GTIN it would use a restricted-circulation number (prefixes 02, 20–29) in its own stores. The B2B documents of the flow (`05-Order.xml`, `06-DespatchAdvice.xml`, `07-Invoice.xml`) carry no GTIN, which fits a store-assigned number but not the GS1 rule. The world mixes conventions here: Brackenmere-brand items carry Brackenmere's prefix 9523710, but Valdara-brand items in `retail/02-Catalogue.xml` carry the distributor's prefix 9520610 (`grep -rh --include='*.xml' -o 'schemeID="GS1 GTIN">[0-9]*'`, prefixes matched against the parties' GLNs). The prefix 952 itself is GS1's demonstration range, so the value is not mistaken for a real one.
- Condition: the shirt's GTIN is allocated by the party the world treats as its brand owner, or the shirt is identified in the store by a restricted-circulation number, or the world's identification convention records that retailers assign GTINs to items whose makers use no GS1 numbers.
- Options: (a) record the convention (the store assigns GTINs because the mill has no GS1 membership), which keeps the receipts; (b, preferred) give the shirt a GTIN from a GS1 prefix of the mill (if the mill is to be a GS1 user) and carry it through order, despatch advice and invoice too, because that is how GS1 intends the number to travel along the chain; (c) make `Lumeport` Brightmarket's own label in the story.
- Needs decision: yes

### packaging/08#F2 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `772030000090`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `check_ids.py`: GTIN `9522610000016`, the store's GLN `9522610900002` and the customer's account pass.
- Item against the flow: the same shirt as `05-Order.xml` to `07-Invoice.xml` (world item number, HS `620520`, CPC `28232`, properties); the store's `BM-778120` is now the seller's ID and the mill's `LT-SH-01` the manufacturer's ID, which is right for the changed roles.
- Quantity and timing: 2 shirts sold on 2026-05-22, after the 600 were despatched to the store (`06-DespatchAdvice.xml`, issued 2026-05-12); the purchase, transaction and issue times are the same moment (16:05) at a till.
- Place: the point of sale `Brightmarket Stores, Lumeport`, `Clothing, first floor`, is a location in the store, not a party name in disguise; nothing needs an identifier there.
