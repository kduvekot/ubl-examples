# LLM review: 01-Order.xml

Flow: medicines (QLM-TX-26-2699) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/01-Order.xml`, Git blob `225019df9400add9a065c22e85ad17ff1504e38e` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### medicines/01#F1 · Low · The purchasing contact is "every day, around the clock" on the company's one number
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Note` = `Every day, around the clock`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 6047 1582`
- Why: `Contact/Note` gives "the circumstances under which this contact can be used". A purchasing department that buys vaccines from India is not staffed around the clock. Every contact of Quillmoor Pharma Distribution in the flow (purchasing, accounts payable, accounts receivable, customs desk, despatch office, hospital orders) has this telephone number and this note (e.g. `02-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone`, `06-ForwardingInstructions.xml:/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Telephone`), while the dangerous-goods emergency line has a number of its own (`06-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:GoodsItem[4]/cac:Item/cac:HazardousItem/cac:ContactParty/cac:Contact/cbc:Telephone` = `+999 2 38 6047 1590`). This looks like the warehouse's round-the-clock line copied into every role.
- Condition: the purchasing contact's note and number fit an office function (office hours, its own line or the switchboard), or the note is absent.
- Options: (a, preferred) office hours for purchasing and finance contacts, the round-the-clock note only for despatch and the cold rooms; (b) leave out the note.
- Needs decision: no

## Checked and consistent
- Arithmetic: 600 × 4100 = 2,460,000.00; 960 × 1300 = 1,248,000.00; 120 × 2850 = 342,000.00; sum 4,050,000.00 INR = line extension and payable amount; tax 0.00.
- 2026-05-11 is a Monday, as the note says; the requested delivery date and CPT Lumeport airport (`XBLMA`) agree with the note and with `02-Invoice.xml`.
- The three items (names, descriptions, seller's and buyer's identifiers, prices and quantities) are the same in `02-Invoice.xml`; the buyer's identifiers recur as Quillmoor's own seller's identifiers in `04-Order.xml`.
- GLN `9524910900003`: check digit correct (`check_ids.py`); prefix 952 is GS1's prefix for demonstrations and examples (own knowledge), so it is not a real company's key.

## Considered and refuted
- `/Order/cbc:Note` says "we pay in euro" while `/Order/cbc:DocumentCurrencyCode` = `INR` — refuted: the order is priced in rupees and paid in euro, which `02-Invoice.xml:/Invoice/cbc:PaymentCurrencyCode` = `EUR` and its exchange rate carry out.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Zero-rated export supply`: an Indian GST treatment stated by the Bayvarran buyer — refuted, an anticipated tax total may show the seller's expected treatment, and it matches the invoice.
