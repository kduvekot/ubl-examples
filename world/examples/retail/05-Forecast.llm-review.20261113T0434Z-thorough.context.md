# LLM review: 05-Forecast.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/05#F1 · High · The reference to the retail event does not lead to it
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `BM-RE-26`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:ID` = `BS-RE-26-0222`
- XPath: `/Forecast/cbc:Note` = `Includes the spring garden promotion.`
- Why: the forecast says it includes the spring garden promotion, which is the retail event
  06-RetailEvent.xml (`BS-RE-26-0222`, issued the same day at 08:17, before this forecast at 11:55).
  The only document reference, `BM-RE-26`, has no document type and matches no example, nor the
  event's own identifiers (BuyerEventID `BM-SPRING-GARDEN-26`, SellerEventID `LD-PROMO-26-03`). A
  receiver cannot link the forecast to the event it includes. 08-Order.xml does refer to the event by
  its document ID.
- Condition: the forecast's reference to the promotion resolves to 06-RetailEvent.xml (its ID) and
  says what it is.
- Options: reference `BS-RE-26-0222` with a document type "Retail event" (preferred); or drop the
  reference and rely on the note.
- Needs decision: no

### retail/05#F2 · High · Emission factor times base does not give the emission
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: the factor ("emissions per unit of activity") of 0.82 per one bench gives 0.82 kg, not 96 kg.
  Same values as in 02-Catalogue.xml.
- Condition: factor × activity = value, or no factor (see also F5: the forecast need not carry the
  footprint at all).
- Options: drop the emission from the forecast (preferred), or correct the factor.
- Needs decision: no

### retail/05#F3 · Medium · FrozenDocumentIndicator false means, by its UBL definition, that the forecast cannot be changed
- XPath: `/Forecast/cac:ForecastLine/cbc:FrozenDocumentIndicator` = `false`
- XPath: `/Forecast/cac:ForecastLine/cbc:Note` = `Week-by-week figures follow in the store's portal.`
- Why: UBL defines FrozenDocumentIndicator as "An indicator that the status of the forecast is
  modifiable (true) or not (false)". Read by that definition, `false` says the forecast line is not
  modifiable. The forecast is version 1, not based on consensus, and announces more detailed figures
  to follow, so it is evidently meant to be open to change; the value seems to follow the element's
  name ("frozen" = false) instead of its definition. Under the rule of semantic conformance the
  definition decides; the conflict between name and definition is worth recording as a finding for
  the TC.
- Condition: the indicator, read by its UBL definition, says what the story means (modifiable →
  `true`), or is absent.
- Options: (a) preferred: `true`, and record the name/definition conflict in the findings for the
  OASIS TC; (b) drop the indicator.
- Needs decision: yes

### retail/05#F4 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/Forecast/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Forecast/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples use this list in
  this element, `grep -l` over `*.xml`). LocaleCode is "A code signifying the locale in which this
  language is used"; `en` with listID `ISO 639` is a language code (213 examples, `grep -l` over
  `*.xml`). Both are codes of other lists in elements whose definitions name something else.
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; a locale such as `en-XB` or no LocaleCode.
- Needs decision: no

### retail/05#F5 · Low · The forecast carries the item's full catalogue description
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Dimension[4]/cbc:MinimumMeasure` = `440`
- XPath: `/Forecast/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: a Forecast is "A document used to forecast sales or orders": it needs the item's
  identification and the forecast quantity. The item here repeats the catalogue description in full
  (footprint, circularity profile, load test, dimensions with tolerances, customs codes, the seller's
  sales conditions), and the parties carry share capital, tax schemes and social-media profiles. The
  supplier already has all of it (it published the catalogue); the forecast does nothing with it.
- Condition: the forecast's item and parties carry what forecasting uses (identifiers, name,
  quantity, period).
- Options: reduce the item to its identifiers and name (preferred); drop the parties' legal, tax and
  social-media detail.
- Needs decision: no

### retail/05#F6 · Low · Signature without anything that signs
- XPath: `/Forecast/cac:Signature/cbc:ID` = `BM-SIG-26-0422`
- Why: only an ID and a signatory; no method, no attachment. Nothing in the story needs a signed
  forecast (IND5/IND6).
- Condition: a signature with a reason and data, or none.
- Options: drop it.
- Needs decision: no

## Checked and consistent
- SenderParty/BuyerCustomerParty Brightmarket and ReceiverParty/SellerSupplierParty Lumeway fit a
  buyer's sales forecast to its supplier.
- ForecastPeriod 2026-05-04 to 2026-06-15 contains the promotion period of 06-RetailEvent.xml
  (2026-05-11 to 2026-05-24), as "Includes the spring garden promotion" and ForecastTypeCode `TOTAL`
  say.
- The forecast quantity (40 benches in six weeks) is consistent with the 24 benches ordered in
  08-Order.xml and the 12-bench display of the event.
- Item identifiers match 02-Catalogue.xml.

## Considered and refuted
- `/Forecast/cac:ForecastLine/cac:ForecastPeriod/cbc:StartDate`: the line period repeats the header —
  refuted because the line period is the period the line's quantity is for; giving it is legitimate.
- `/Forecast/cbc:BasedOnConsensusIndicator`: `false` although the event was "agreed with the
  distributor's sales team" — refuted because the promotion was agreed, not the forecast figures.
