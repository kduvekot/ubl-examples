# LLM review: 07-ForecastRevision.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### cotton/07#F1 · High · "Twenty per cent more" does not match the revised quantity
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Note` = `Twenty per cent more.`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cbc:Quantity` = `30000`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:StartDate` = `2026-04-03`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `24000`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- Why: The revision line revises line 1 of the forecast 02, which forecast 24,000 kg for the whole
  period 2026-02-16 to 2026-06-02. Twenty per cent more is 28,800 kg; 30,000 kg is 25 % more. And
  the revised quantity applies only to the line's period from 2026-04-03 ("More bales from the
  second half of the season"): if 30,000 kg are for the second half alone, the increase over the
  original is far more than twenty per cent; if 30,000 kg is the new season total, the line period
  is wrong. The note and the structured values contradict each other whichever way the line is
  read.
- Condition: the revised quantity, the period it applies to and the stated increase agree with each
  other and with the forecast line they revise.
- Options: (a, preferred) make the quantity 28,800 kg (or the note "Twenty-five per cent more") and
  state whether it is the season total or the second-half quantity, with a line period to match;
  (b) state the second-half quantity and the unchanged first-half quantity in two revision lines.
- Needs decision: no

### cotton/07#F2 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item"; 227 is the weight of a
  bale in kilograms ("compressed bales of about 227 kg"). As in 02 and 08.
- Condition: no element meant for a count holds the bale weight.
- Options: (a, preferred) leave PackSizeNumeric out and, if needed, give the bale weight as an
  item property with a KGM quantity.
- Needs decision: no

### cotton/07#F3 · Low · A forecast of future lint carries the classing certificate of one classed lot
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: Item/Certificate is "A certificate associated with this item". The revision forecasts lint to
  be supplied between April and June; a classing certificate records the measured grade of a lot
  already ginned and classed. It cannot certify cotton that is still to be ginned; the wanted grade
  is already stated as item properties (Grade, Staple length). (Unlike in 02, the validation date
  2026-02-20 is before this document's issue date.)
- Condition: the forecast revision states the wanted quality without a certificate of a specific
  lot, or makes clear the certificate describes a reference lot.
- Options: (a, preferred) leave the certificate out and keep the item properties.
- Needs decision: no

### cotton/07#F4 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: The farm's address gives North coast as District ("The district or geographical division of
  a country or region"); here it is a Region ("recognized geographic or economic region or group of
  countries"). The same area should be in the same element.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress.
- Needs decision: no

## Checked and consistent
- OriginalDocumentReference LTM-FC-26-0192 resolves to 02; RevisedForecastLineID 1 and
  SourceForecastIssueDate/Time 2026-02-02 09:00:00 match 02's line ID and issue date and time.
- Parties (mill as sender and buyer, ginnery as receiver and seller) are those of 02.
- The line period lies within the forecast period, which is the period of 02.
- The note "Demand for clothing has risen" and AdjustmentReasonCode DEMAND agree, and follow on
  02's note that the forecast depends on clothing orders.

## Considered and refuted
- `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:Description[2]/@languageID` = `en-XB`:
  the seller's item description tagged as Bayvarran English while the ginnery's invoice 16 tags the
  same text en-XL — refuted because the text is identical English and the tag reflects the issuer
  (the mill), which is a legitimate reading of the language of that rendering.
- `/ForecastRevision/cbc:RevisionStatusCode` = `REVISED`: suspected as redundant in a forecast
  revision — refuted because it states the status of this revision as a positive value.
