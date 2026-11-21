# LLM review: 07-Invoice.xml

Flow: medicines (QLM-TX-26-3960) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/07-Invoice.xml`, Git blob `207b81fe2588a8f34d9d54e94cdc6f2ec35c31f7` (committed)
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

### medicines/07#F1 · Low · "Six days after delivery" against a delivery on 14 June and a reference on 21 June
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration)…`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ItemInstance/cac:AdditionalItemProperty[2]/cbc:Value` = `2026-06-21T12:00:00+00:00`
- Why: Haarvliet delivers to Quillmoor at Lumeport on 14 June (`05-Order.xml:/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-14`); the reference time on this invoice is seven days later. The "six days" describe the hospital's delivery of 15 June, not this sale.
- Condition: the item's description agrees with this delivery and the reference time on the same line.
- Options: as medicines/05#F2.
- Needs decision: no

### medicines/07#F2 · Low · An export invoice from the Netherlands without the supplier's VAT identification
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside the European Union`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Haarvliet Isotopes B.V.`
- Why: an invoice that applies the EU export exemption carries the supplier's VAT identification number (EU VAT Directive, art. 226; own knowledge); the supplier here has no `PartyTaxScheme`.
- Condition: the supplier carries its VAT registration, with a value that cannot be mistaken for a real Dutch VAT number, or the invoice states no VAT treatment.
- Options: (a, preferred) a `PartyTaxScheme` with a clearly fictional VAT identifier; (b) leave out the tax total if the world does not model EU VAT.
- Needs decision: no

### medicines/07#F3 · Low · No payment means on the invoice
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `14 days net.`
- Why: the invoice asks for 1,000 euro within 14 days but says nothing about how or to which account; the same gap is in `02-Invoice.xml`, while `14-Invoice.xml` carries its means.
- Condition: the invoice gives the means and the payee account, or the terms name the standing arrangement that replaces them.
- Options: (a, preferred) a `PaymentMeans` with the supplier's euro account; (b) payment terms that refer to the supply agreement's payment arrangement.
- Needs decision: no

### medicines/07#F4 · Low · Accounts payable "every day, around the clock" on the company's one number
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Note` = `Every day, around the clock`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 6047 1582`
- Why: as medicines/01#F1.
- Condition: the accounts-payable contact has office hours and its own line or the switchboard, or no note.
- Options: as medicines/01#F1.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` resolves to `05-Order.xml`; price, quantity, item and delivery terms agree with it.
- Dates: issued Saturday 2026-06-13; +14 days = Saturday 2026-06-27, due Monday 2026-06-29; despatch on 13 June fits the arrival on 14 June and the import declaration of 14 June (`08-ImportCustomsDeclaration.xml`).
- The serial number and the nominal activity agree with `09-DespatchAdvice.xml`.
