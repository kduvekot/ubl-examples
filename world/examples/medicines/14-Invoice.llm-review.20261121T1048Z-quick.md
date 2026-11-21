# LLM review: 14-Invoice.xml

Flow: medicines (SGH/2026/1099) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/14-Invoice.xml`, Git blob `93e2b539ada8f0c4a5083b887354aac7de05401e` (committed)
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

### medicines/14#F1 · Low · An actual delivery to the hospital pharmacy stated before the goods have arrived or been cleared
- XPath: `/Invoice/cac:Delivery/cbc:ActualDeliveryDate` = `2026-06-15`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Selanu General Hospital, pharmacy`
- XPath: `/Invoice/cbc:IssueTime` = `10:27:00-01:00`
- Why: `ActualDeliveryDate` is "the actual date of delivery". The invoice is issued at 11:27 UTC; the flight landed at 10:45 UTC (`12-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `10:45:00+00:00`) and the goods are declared for import only at 11:40 UTC (`13-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `11:40:00+00:00`), so they have not reached the hospital pharmacy when the invoice states that they were delivered there. The date is right only if the delivery happens later that day, which the invoice cannot know.
- Condition: the invoice states an actual delivery only once it has happened, or states the date as planned.
- Options: (a, preferred) leave out the actual delivery date (the despatch advice is referenced) or give the date of despatch; (b) issue the invoice after the delivery, which conflicts with customs needing it at 11:40.
- Needs decision: no

### medicines/14#F2 · Low · Accounts receivable "every day, around the clock"; the hospital's finance office on the pharmacy's number
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Note` = `Every day, around the clock`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 3 726 8840`
- Why: a credit controller is not reachable around the clock (as medicines/01#F1, the shared Quillmoor number and note); the hospital's finance office has the telephone number of the pharmacy and of pharmacy goods-in (`04-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone`, `09-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Telephone`), which looks copied.
- Condition: each contact's note and number fit its function.
- Options: (a, preferred) office hours for the credit controller; a finance number (or the hospital's switchboard) for the finance office; (b) leave out notes and numbers that are not known.
- Needs decision: no

## Checked and consistent
- Arithmetic: lines and total 30,130.00 XBL as in `04-Order.xml`; penalty 1.5 % of 30,130.00 = 451.95; tax 0 with "Export outside Bayvarra" for a delivery to Lisavu.
- Dates: issued Monday 2026-06-15; +30 days = Wednesday 2026-07-15 = due date; penalty from 2026-07-16.
- References: `/Invoice/cac:OrderReference/cbc:ID` resolves to `04-Order.xml`, `/Invoice/cac:DespatchDocumentReference/cbc:ID` to `09-DespatchAdvice.xml`; quantities and order lines agree.
- Check digits: `RF48QLMINV264080` (ISO 11649) and `XB31BLUM38020504913407` (mod 97) are correct (`check_ids.py`); the payee account is the supplier's own, in Lume, at a Lumeport branch.
