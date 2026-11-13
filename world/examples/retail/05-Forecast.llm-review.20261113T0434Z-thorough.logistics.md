# LLM review: 05-Forecast.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/05-Forecast.xml`, Git blob `e5ca058f329dbb9d83da42c0dcf6bbefbfd16c1c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/05#F1 · High · Reference to the retail event uses an identifier that no document has
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:ID` = `BS-RE-26-0222`
- XPath: `/Forecast/cbc:Note` = `Includes the spring garden promotion.`
- Why: The note says the forecast includes the spring garden promotion, and the only document of the flow that describes it is the retail event 06, issued the same morning (2026-04-22 08:17, before this forecast at 11:55), with ID `BS-RE-26-0222`. `BM-RE-26` occurs in no example (`grep -rn --include='*.xml' 'BM-RE-26<' world/examples`), and it matches neither 06's ID nor its buyer event ID (`06-RetailEvent.xml:/RetailEvent/cbc:BuyerEventID` = `BM-SPRING-GARDEN-26`). The order 08 cites the event correctly as `BS-RE-26-0222`.
- Condition: the forecast's reference to the promotion resolves to 06-RetailEvent (its document ID), and says what it refers to.
- Options: (a, preferred) ID `BS-RE-26-0222` with a DocumentType (or type code) for a retail event; (b) if a separate promotion plan is meant, give it a type, but the forecast then still has no link to 06.
- Needs decision: no

### retail/05#F2 · High · Emission value is not factor × base
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

## Checked and consistent
- Forecast period 2026-05-04 to 2026-06-15 contains the promotion period of 06 (`06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11` to 2026-05-24), and the line period equals the header period.
- Quantities: 40 benches over six weeks, against a stock of 3 (07), an order of 24 (08) and promotion shelf space for 12 (06). 3 + 24 = 27 covers the display of 12 and the first weeks; the rest of the 40 can come from later orders. No contradiction.
- Item identifiers (LD-10442, GTIN `9520610000012`, VI-B180) agree with 02 line 1; GTIN check digit OK.
- Issue time 11:55 is after 06 (08:17), so the forecast can include the confirmed promotion.

## Considered and refuted
- `/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `40`: suspected not a multiple of the pallet of four — refuted because 40 is ten pallets, and a sales forecast counts consumer units anyway.
