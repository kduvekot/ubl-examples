# LLM review: 11-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/11-Invoice.xml`, Git blob `ee9c00c2aed8b2e82ac3390db74cfce890bdf1a1` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/11#F1 · High · Emission factor × base quantity does not give the stated emission
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: As in the order (rail/01#F1) and the transit declaration (rail/06#F2): ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies"; 0.82 × 1 EA gives 0.82 kg CO2e per bench, not the stated 96 kg. The same triple occurs in 39 examples (`grep -rc --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, with the adjacent ValueMeasure/ValueBaseMeasure).
- Condition: ValueFactorNumeric × ValueBaseMeasure equals ValueMeasure, or the factor and base are absent.
- Options: as in rail/01 (preferred: remove factor and base).
- Needs decision: no

## Checked and consistent
- OrderReference LD-PO-26-0325 resolves to the order rail/01; order line 1 exists there; quantity 192 EA, price 49 900 XUF per 1 EA and the item (VI-B180, GRY, 771020000027) are the same as in the order and the transit declaration (rail/06).
- 192 benches invoiced = 192 in the consignment summaries (rail/02, rail/03, rail/08) and the goods item of rail/06.
- The note "Delivered at place: the price includes the carriage to the siding" agrees with the order's DAP terms at the Lumeway siding and with the freight being billed to Valdara, not Lumeway (rail/10).
- Issue 2026-04-17 lies after the planned delivery on 2026-04-15 (rail/03, rail/07).

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item`: an export invoice without Delivery (actual delivery date and place) or a reference to the transport document — refuted within this lens: the invoice's purpose does not depend on it, and the delivery is documented in the waybill; whether the export exemption needs the transport document as evidence is for the money review.
- `/Invoice/cac:InvoiceLine/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`: does not resolve to an example — refuted as a broken reference: the seller's data sheet is a document the flow does not model; likewise VI-LCA-2025 and VI-RM-B180.
