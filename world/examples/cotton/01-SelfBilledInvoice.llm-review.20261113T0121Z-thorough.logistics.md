# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/01-SelfBilledInvoice.xml`, Git blob `aee01edf4f4e0c209dc01462389e7115dcceae7c` (committed)
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

### cotton/01#F1 · High · Payment due date contradicts "paid on issue"
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27`
- XPath: `/SelfBilledInvoice/cbc:DueDate` = `2026-01-13`
- XPath: `/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `Paid on issue by transfer. No presumptive tax is withheld…`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-01-13`
- Why: `PaymentDueDate` under `PaymentMeans` is "the date on which payment is due for this means of payment". The document's own `DueDate`, the payment terms ("Paid on issue by transfer") and the final self-billed invoice 04, which records the advance as paid on 2026-01-13, all put the payment on the issue date. A due date of 2026-02-27 for the same and only means of payment, six weeks later and after the delivery (2026-02-05) and the final invoice (2026-02-07), contradicts all three.
- Condition: every due date in the example (`DueDate`, `PaymentMeans/PaymentDueDate`) agrees with the payment terms and with the paid date recorded in 04.
- Options: (preferred) set the means-of-payment due date to the issue date, or drop it since `DueDate` already states it; or, if the advance really falls due later, change the terms note and the paid date in 04 accordingly.
- Needs decision: no

## Checked and consistent
- Quantity × price = line amount: 4500 KGM × 0.226 XLC/kg = 1017.000 XLC; the advance covers 4500 kg of the 18000 kg later delivered (`03-DeliveryNote.xml:/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity`), i.e. 25 %.
- `ContractDocumentReference` `SCG-SEASON-2026` is the season agreement also cited by 02, 03, 04 and 05; it is not a UBL document of the flow, and the element name says what it is.
- Item identification (`LCF-SC`), commodity code 520100 and CPC 01921 are the same as in 03, 04 and 05.
- Coordinates of the farm (39° 58.80′ S, 15° 7.80′ W) are the same in every example of the flow that carries them (01, 03, 04, 05, 06).
- `check_ids.py`: RF reference `RF61SCGSBI260191` and the account `XL67BSEL0020004817534` have valid check digits.

## Considered and refuted
- `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode`: HS 520100 for seed cotton (not ginned) was suspected — refuted because HS heading 5201 "cotton, not carded or combed" covers raw cotton whether or not ginned (own knowledge of the HS explanatory notes); cotton seed alone would be 1207.
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate`: same coordinates as the postal address was suspected as copied — refuted because the farm address is the farm track at the fields, so one point for both is a legitimate reading.
