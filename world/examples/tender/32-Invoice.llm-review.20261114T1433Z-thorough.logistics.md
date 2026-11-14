# LLM review: 32-Invoice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/32-Invoice.xml`, Git blob `670ec0ba9b4bae748393682c8030e3f46b70c018` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/32#F1 · High · Forty installations are invoiced that the order does not contain and that cannot have taken place
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `40`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`
- XPath: `/Invoice/cbc:TaxPointDate` = `2026-03-31`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: The invoice refers to order `LPWD-PO-26-0212`. That order has one line, 40 benches (`26-Order.xml:/Order/cbc:LineCountNumeric` = `1`); order change and order response agree a total of `28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00` (benches plus colour charge). Invoice line 2, "Installation of a park bench" × 40, has no order line reference and nothing in the flow orders it; the invoice total before withholding (20880.00) is 720.00 above the accepted order. Moreover the invoice is issued on 31 March at 09:28 with that day as tax point: the benches left Urvania the evening before (`29-DespatchAdvice.xml`, 30 March 17:37), the import declaration is lodged at 11:14 the same morning, and four anchor sets are on back order "before the installers need them" (29). The installation therefore had not been performed when it was invoiced; the debit note `34-DebitNote.xml` later charges a penalty for "late installation".
- Condition: Every invoice line is covered by the order (or another ordering document of the flow), and a service is invoiced with a tax point not before its performance.
- Options: (a) preferred: order the installation in the order (a second line, quantity 40) and invoice it separately after completion; (b) add the installation line to the order and date the invoice after the installation; (c) drop line 2 from this invoice. All change the story (the credit note and the debit note build on the invoiced installation).
- Needs decision: yes

### tender/32#F2 · High · A special-colour charge is invoiced for benches identified as the standard grey
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Special colour`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: The charge is for the moss-green coating of this release (27, 28; `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`). The invoiced item is identified as variant GRY with the colour attribute and the property "Frame colour: Ferro grey", the standard colour for which no surcharge is due. The invoice contradicts itself and the despatch note.
- Condition: The invoiced item's variant and colour are those delivered (moss green), consistent with the charge.
- Options: identify the green variant as in the corrected despatch advice (preferred).
- Needs decision: no

### tender/32#F3 · High · Emission factor × base does not give the emission value
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg CO2e; see `25-Catalogue.xml` (F4 of its review). 39 examples across flows carry these values (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: as in 25.
- Needs decision: no

### tender/32#F4 · Low · The invoice names neither the despatch nor a delivery date
- XPath: `/Invoice/cac:OrderReference`
- Why: The invoice refers to order, contract and project, but not to the despatch advice `CL-DA-26-0215` under which the invoiced benches travel, and it has no `cac:Delivery` with an actual delivery date. The contract's payment term counts from "each accepted release" (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.`), and the credit note of 4 April does cite the despatch advice. On the invoice the buyer has no reference to match the goods received. Missing details the document could carry.
- Condition: The invoice references the despatch advice and states the delivery date (or period) of the goods.
- Options: `cac:DespatchDocumentReference` CL-DA-26-0215 and `cac:Delivery/cbc:ActualDeliveryDate` (preferred).
- Needs decision: no

### tender/32#F5 · Low · The contract is cited twice, once as an unexplained "originator document"
- XPath: `/Invoice/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Invoice/cac:ContractDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: As in `26-Order.xml` (F6): the originator document reference has only an ID, identical to the contract number cited next to it, and does not say which document of an originator is meant.
- Condition: The originator reference names a document other than the contract and says what it is, or is absent.
- Options: remove it (preferred).
- Needs decision: no

### tender/32#F6 · Low · Programme code differs from the procurement documents
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: As in `26-Order.xml` (F7): the programme is coded `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in the procurement documents; here one string serves as project identifier and as the buyer's accounting code.
- Condition: One code for the programme throughout the flow.
- Options: as in 26.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: creditor reference RF48VIINV260221 (ISO 11649) and the account number pass their checks; no failures.
- `cac:OrderReference` and `InvoiceLine[1]/cac:OrderLineReference/cbc:LineID` 1 resolve to the order and its bench line; quantity 40 EA at 499 = 19960.00, as ordered; the charge of 200.00 is the one accepted in 28.
- Contract `PWD-2026-PARKS` is the contract of 21–24; annotation "First release: 40 benches; 200 remain" = 240 − 40.
- Dates: issue 31 March 09:28; due date and payment due date 2026-04-30 = issue + 30 days; settlement period 31 March–10 April = 10 days, as the terms say; exchange-rate dates of the issue day.
- `cbc:LineCountNumeric` 2 = two invoice lines. InvoiceTypeCode 380 = commercial invoice (UNCL 1001); PaymentMeansCode 30; allowance reason CAT = special colour service: each fits its element.
- Arithmetic in passing: 19960.00 + 720.00 = 20680.00; + 200.00 = 20880.00; − 72.00 = 20808.00; 2 % of 20880.00 = 417.60.

## Considered and refuted
- `/Invoice/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: forward contract of 2 January, before the procedure — raised once, in the review of `26-Order.xml` (F8).
- `/Invoice/cbc:IssueTime`: the invoice is issued before the goods are imported (11:14) — refuted for the goods: invoicing at despatch is usual, and the tax point of an export is the despatch; the objection holds only for the installation (F1).
- `/Invoice/cac:PaymentTerms/cbc:Note`: "30 days net" from the invoice date although the contract counts from the accepted release — left to the money lens; noted so it is not lost.
