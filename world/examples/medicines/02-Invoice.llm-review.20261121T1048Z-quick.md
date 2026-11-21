# LLM review: 02-Invoice.xml

Flow: medicines (QLM-TX-26-2699) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/02-Invoice.xml`, Git blob `8bf30c810d20016a01a0f07d68f2db0f50701143` (committed)
- Last commit changing the example: a9214989 2026-11-21 Stage 7 Q2: documents are issued within the hours of the desk that issues them
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

### medicines/02#F1 · Low · An invoice payable in euro with no payment means
- XPath: `/Invoice/cbc:PaymentCurrencyCode` = `EUR`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; payment in euro at the ECB's euro reference rate of the invoice date.`
- Why: the invoice asks for 45,577.57 euro by 2026-06-08 but carries no `PaymentMeans` (means code, payee account). The buyer, a Bayvarran company paying an Indian exporter in a third currency, cannot pay from this document; the other invoices of the flow (`14-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode`) carry their means.
- Condition: the invoice says how and to which account the euro amount is paid, or it is clear from the world why it need not (for example payment against a documentary collection named in the terms).
- Options: (a, preferred) a `PaymentMeans` with credit transfer and the seller's euro account; (b) payment terms that name the arrangement that replaces it.
- Needs decision: no

### medicines/02#F2 · Low · The seller has no tax registration although it applies the GST export zero rate
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID` = `GST`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Nilavar Biologics Private Limited`
- Why: a zero-rated export under the Indian GST is invoiced by a registered supplier under its GSTIN (own knowledge of Indian GST invoicing rules); the supplier here has no `PartyTaxScheme`, so the zero rate is claimed by a party that shows no registration under the scheme it cites.
- Condition: the supplier carries its tax registration under the GST scheme, or the invoice does not state a GST treatment.
- Options: (a, preferred) a `PartyTaxScheme` with the supplier's GST registration (a value that cannot be mistaken for a real GSTIN); (b) leave out the tax total if the world does not model Indian taxes.
- Needs decision: no

### medicines/02#F3 · Low · Accounts payable "every day, around the clock" on the company's one number
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Note` = `Every day, around the clock`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 6047 1582`
- Why: as in `01-Order.xml` (medicines/01#F1): an accounts-payable clerk is not reachable around the clock; the number and note are those of every Quillmoor contact in the flow.
- Condition: the accounts-payable contact has office hours and its own line or the switchboard, or no note.
- Options: as medicines/01#F1.
- Needs decision: no

## Checked and consistent
- Arithmetic: lines as in `01-Order.xml`, total 4,050,000.00 INR; 4,050,000 ÷ 88.8595 = 45,577.569 → 45,577.57 EUR as in the note; operator `Divide` with source INR and target EUR is the right direction.
- Dates: issued Thursday 2026-05-07; +30 days = Saturday 2026-06-06, due Monday 2026-06-08; despatch on the invoice date fits arrival by 11 May (`01-Order.xml`) and the import declaration of 11 May (`03-ImportCustomsDeclaration.xml`).
- `/Invoice/cac:OrderReference/cbc:ID` resolves to `01-Order.xml`; invoice lines reference the order lines 1 to 3 with the same quantities and prices.

## Considered and refuted
- `/Invoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Lumeport airport`: under CPT the seller delivers when it hands the goods to the first carrier in India — refuted as a finding, the delivery location of the invoice may name where the goods are delivered to; the delivery terms name the same place.
