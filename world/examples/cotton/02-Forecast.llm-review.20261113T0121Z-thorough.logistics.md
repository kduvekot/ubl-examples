# LLM review: 02-Forecast.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/02-Forecast.xml`, Git blob `564d177fc853a93d7bb7f285f6471573cea2ed35` (committed)
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

### cotton/02#F1 · High · Forecast carries a classing certificate of a lot that did not yet exist
- XPath: `/Forecast/cbc:IssueDate` = `2026-02-02`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`
- XPath: `10-GoodsCertificate.xml:/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:StartDate` = `2026-02-07`
- Why: The forecast, issued on 2026-02-02, describes the forecast item with the classing certificate `XL-CLS-2026-0042`, whose signature is dated 2026-02-20, eighteen days after the forecast. The same certificate is attached to the lint actually shipped (10, 11, 15, 16); that lint was ginned from seed cotton delivered to the gin on 2026-02-05 (03) and ginned from 2026-02-07 to 2026-02-22 (10). On 2026-02-02 the lint, and so its classing, did not exist yet. A forecast of a season's purchases (`ForecastPeriod` 2026-02-16 to 2026-06-02) also has no reason to name the certificate of one lot.
- Condition: no date or document cited in the forecast lies after its issue time; the forecast item carries no certificate of a lot produced later.
- Options: (preferred) remove the lot certificate from the forecast item and describe the quality only by the agreed grade and staple (`AdditionalItemProperty`), which a forecast can name in advance; or cite a certificate that existed on 2026-02-02 (e.g. a previous season's).
- Needs decision: no

### cotton/02#F2 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count. Here it carries the weight of a bale in kilograms (the description says "compressed bales of about 227 kg"); a bale does not contain 227 items. The forecast quantity is in kilograms, so the item is the kilogram of lint, and a pack of it is a bale; the count of kilograms in a bale is not a number of items in the sense of the definition, and the value "about 227" is not exact either. The same value is in 07, 08, 10, 11, 15 and 16 (counted with `grep -c '<cbc:PackSizeNumeric>227<'` over `world/examples/*/*.xml`: 7 files, all in this flow).
- Condition: `PackSizeNumeric`, where present, is a count of items in a pack; the nominal bale weight is stated where a weight belongs (description, or an item property with a weight unit).
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an `AdditionalItemProperty` with `ValueQuantity` in KGM; or keep the description only.
- Needs decision: no

## Checked and consistent
- Staple length 28.6 MMT agrees with "staple 1-1/8 inch" in the certificate remarks (1.125 × 25.4 mm = 28.575 mm).
- 24000 KGM over 2026-02-16 to 2026-06-02 is about 106 bales of 227 kg (24000 / 227 = 105.7), plausible for a forecast "of about"; the first order (08) is 6129 kg = 27 × 227 kg.
- Item identification `SCG-LINT`, HS 520100 and CPC 01921 are the same as in 07, 08, 10, 11, 15, 16.
- `AdditionalDocumentReference` `SCG-SEASON-2026` is the season agreement cited throughout the flow.

## Considered and refuted
- `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`: a district in `Region` was suspected — refuted for this lens because "North coast" is offered as a recognised growing region of origin, which `Region` covers ("recognized geographic or economic region"); whether it should match the farm's `District` is a parties question.
