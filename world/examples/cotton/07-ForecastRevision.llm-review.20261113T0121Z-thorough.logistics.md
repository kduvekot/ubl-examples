# LLM review: 07-ForecastRevision.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/07-ForecastRevision.xml`, Git blob `fc49267ef8416292c4c72e5eb19588b0cdccd24f` (committed)
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

### cotton/07#F1 · High · "Twenty per cent more" is twenty-five per cent
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Note` = `Twenty per cent more.`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cbc:Quantity` = `30000`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `24000`
- Why: The revised line raises the forecast for line 1 of 02 from 24000 kg to 30000 kg. Calculated: 30000 / 24000 = 1.25, i.e. 25 % more; 20 % more would be 28800 kg. The note and the quantity contradict each other.
- Condition: the note and the revised quantity agree with each other and with the original quantity of 02.
- Options: (preferred) state "Twenty-five per cent more" or drop the percentage from the note; or set the quantity to 28800 kg.
- Needs decision: no

### cotton/07#F2 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal weight of a bale in kilograms ("compressed bales of about 227 kg"). Same as in 02, 08, 10, 11, 15 and 16.
- Condition: `PackSizeNumeric`, where present, is a count of items in a pack; the nominal bale weight is stated where a weight belongs.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an `AdditionalItemProperty` with `ValueQuantity` in KGM.
- Needs decision: no

### cotton/07#F3 · Low · Revised line covers only part of the forecast period
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:StartDate` = `2026-04-03`
- XPath: `/ForecastRevision/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Description` = `More bales from the second half of the season.`
- Why: Line 1 of 02 forecasts 24000 kg for the whole period 2026-02-16 to 2026-06-02. The revision line that replaces it (`RevisedForecastLineID` 1) has its own period 2026-04-03 to 2026-06-02 and a quantity of 30000 kg. Read as written, the revised line forecasts 30000 kg for the second half only and leaves 2026-02-16 to 2026-04-02 without a forecast, although the order 08 (2026-02-24) falls in it; read as the season total, the line period is wrong. The description ("more bales from the second half") supports a total with a changed split, which the document cannot express with one line and one period.
- Condition: the revised line(s) together cover the forecast period and state unambiguously what quantity applies to which part of it.
- Options: (preferred) give the revision line the whole period with the new season total; or split it into two revision lines (first half unchanged, second half raised), so the periods and quantities add up.
- Needs decision: no

## Checked and consistent
- `OriginalDocumentReference` `LTM-FC-26-0192` resolves to 02; `SourceForecastIssueDate` 2026-02-02 and `SourceForecastIssueTime` 09:00:00 equal 02's issue date and time; `RevisedForecastLineID` 1 is 02's only line.
- The classing certificate cited in the item (signature 2026-02-20) predates this revision (2026-02-22); the date problem lies in 02.
- 30000 kg is about 132 bales of 227 kg (30000 / 227 = 132.2).
