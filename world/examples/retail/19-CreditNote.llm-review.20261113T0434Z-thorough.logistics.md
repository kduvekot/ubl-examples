# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/19#F1 · High · Emission value is not factor × base
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/19#F2 · Medium · "Carton torn", while the despatch advice describes no cartons
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:Note` = `Bench refused: armrest bent, carton torn.`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- Why: The despatch advice 12 (which this credit note references) describes the packaging of each pallet as a single pallet package, with no cartons; the credit note, like the receipt advice 17, gives a torn carton as part of the damage. The packaging of the credited bench is described differently in the documents of the flow. See 12/F2 and 17/F4.
- Condition: the packaging named in the credit note is the packaging declared in the despatch advice.
- Options: (a, preferred) declare the cartons in 12; (b) drop the carton here and in 17.
- Needs decision: no

## Checked and consistent
- CreditedQuantity 1 = RejectedQuantity of 17's receipt line; 1 × 520 = 520.00 line amount; the promotion support of 5 % on 520 = 26.00, so 494.00, matching the 5 % allowance of the invoice 18.
- References: InvoiceDocumentReference `LD-INV-26-0236` with IssueDate 2026-04-30 matches 18; despatch line 1 of 12, receipt line 1 of 17, order line 1 of 08 and billing line 1 of 18 exist.
- ActualDeliveryDate 2026-04-30 on the line equals the receipt date in 17.
- DiscrepancyResponse code `17` (UNTDID 4465 "Transport damage") agrees with 17's reject reason "Damaged in transit." and the line note.
- Issued 2026-05-02, after 17 (credit requested) and 18.
