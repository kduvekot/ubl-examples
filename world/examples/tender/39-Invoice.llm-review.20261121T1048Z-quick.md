# LLM review: 39-Invoice.xml

Flow: tender (PWD/2026/0566) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/tender/39-Invoice.xml`, Git blob `6e901d5c3c50df697c295dabe94374a66afd544e` (committed)
- Last commit changing the example: 30a63f5b 2026-11-21 Stage 7 Q3, Q4, Q5: world reasons, the wood codes, tax currency only where tax is charged
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### tender/39#F1 · High · Withholding tax scheme coded as sales tax for the tax representative and as "other" in the withholding total
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- XPath: `/Invoice/cac:TaxRepresentativeParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Withholding tax on payments by public bodies to non-resident businesses`
- XPath: `/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID` = `OTH`
- Why: The same scheme, named identically and with the same `TaxTypeCode` INCOME in both places, is identified as `STT` (UN/EDIFACT 5153: state/provincial sales tax) under the tax representative and as `OTH` (other taxes) in the withholding total. `STT` is the code the buyer's own `PartyTaxScheme` uses for Bayvarra's state sales tax, of which the department is exempt; a withholding tax on income is not a sales tax. The two scheme IDs contradict each other within the invoice, and the representative's code says it is registered for a different tax than the one it represents the manufacturer for.
- Condition: The tax representative's scheme and the withholding scheme carry the same ID, and that ID is not the sales-tax code.
- Options: (a) preferred: `OTH` in both places, as in the withholding total (5153 has no withholding code; the name and the INCOME type code say what it is); (b) a scheme ID from a world list for Bayvarra's withholding tax, used in both places.
- Needs decision: no

## Checked and consistent
- Arithmetic: 39 × 18 = 702.00; withholding 10 % of 702.00 = 70.20 on line and header; payable 702.00 − 70.20 = 631.80; tax total 0.00 with category O.
- 39 installations agree with `38-ReceiptAdvice.xml` (line 2, 39 received) and refer to order line 2 of `26-Order.xml` (installation, 40 ordered at 720.00 = 18 each); receipt PWD/2026/0702 → 38; due date 2026-05-13 = 30 days after acceptance on 13 April, as the note says.
- The late-completion penalty of 7.02 is not on the invoice but deducted in `36-RemittanceAdvice.xml`, which agrees with 38's timing complaint (2 days × 0.5 % × 702.00); 36 lists this invoice.
- Payee account at Bank of Lumeport in XBL; RF reference and IBAN-like account pass `check_ids.py`; payment terms and penalty interest match `32-Invoice.xml`.
- The installer named in the item description, Saltmere Engineering, is the subcontractor of Valdara's tender (`15-Tender.xml`).

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days after the release is accepted, as the framework contract says; late payment carries Urvania's statutory interest of 8 % a year.`: Urvanian statutory interest in a Bayvarran public contract — refuted for this review: `32-Invoice.xml` and `35-Reminder.xml` apply the same rate; whether the contract's choice of law fits is a question for the flow's story, not a contradiction here.
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`: a service performed in Bayvarra with no Bayvarran tax — refuted: Urvanian VAT does not apply to a service supplied abroad, and the buyer's exemption from Bayvarra's sales tax as a public body is stated in its `PartyTaxScheme`.
