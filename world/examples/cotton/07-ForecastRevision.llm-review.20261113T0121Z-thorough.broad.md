# LLM review: 07-ForecastRevision.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

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

### cotton/07#F1 · High · "Twenty per cent more" does not match the revised quantity and period
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cbc:Note` = `Twenty per cent more.`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cbc:Quantity` = `30000`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:StartDate` = `2026-04-03`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastLine/cac:SalesItem/cbc:Quantity` = `24000`
- XPath: `02-Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:StartDate` = `2026-02-16`
- Why: the revised line 1 of forecast 02 was 24000 kg for 16 February to 2 June. Twenty per cent more would be 28800 kg. The revision gives 30000 kg (25 % more), and for a shorter period, 3 April to 2 June, so per day it is about twice the original rate (30000 kg / 61 days against 24000 kg / 107 days). Note, quantity and period cannot all be right; and it is not stated what happens to 16 February – 2 April.
- Condition: the note, the revised quantity and the revised period describe the same change, and the part of the original period not covered by the revision line is accounted for.
- Options: (preferred) keep the whole period (16 Feb – 2 Jun) and give 28800 kg, as the note says; or keep 30000 kg for 3 April – 2 June and rewrite the note (and the description "more bales from the second half of the season") to state the new rate and what remains for the first half.
- Needs decision: no

### cotton/07#F2 · Medium · Language code in `LocaleCode`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` "signif[ies] the locale in which this language is used"; `en` from ISO 639 is a language code and repeats `Language/ID`. Same value in 213 of 250 examples.
- Condition: `LocaleCode` is absent or a locale code different from the language identifier.
- Options: (preferred) drop it; or a locale such as `en-XB` from a list of locales.
- Needs decision: no

### cotton/07#F3 · Low · Lot certificate attached to a forecast of future supplies
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:ForecastPeriod/cbc:EndDate` = `2026-06-02`
- Why: the revision forecasts lint "from the second half of the season" (3 April – 2 June), but the item carries the classing certificate of one lot already classed (signed 2026-02-20; the same certificate goes with the 27 bales ordered in 08 and certified in 10). Lint ginned in April and May cannot be covered by a February lot certificate; the forecast can only state the quality it expects.
- Condition: the forecast item states the expected quality (grade, staple) without a certificate of a specific lot, or the certificate covers the forecast quantity.
- Options: (preferred) drop the certificate and keep the grade and staple properties.
- Needs decision: no

### cotton/07#F4 · Low · Purchasing contact described as a sales customer-service officer
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ForecastRevision/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: as cotton/02#F3: name, department and job title of the buyer's contact contradict each other.
- Condition: the buyer's contact has a name, title and department that agree and fit a buyer.
- Options: (preferred) department "Purchasing" with a buyer's title.
- Needs decision: no

### cotton/07#F5 · Low · The ginnery's English address and the item texts tagged as Bayvarran English
- XPath: `/ForecastRevision/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:Name[2]` = `Cotton lint, compressed bale`
- Why: as cotton/02#F4: the same renderings carry `en-XL` in the ginnery's own documents and `en-XB` here.
- Condition: the same rendering carries the same language tag in every example.
- Options: (preferred) `en-XL` for the ginnery's address and items everywhere.
- Needs decision: no

### cotton/07#F6 · Low · Classing results in the applicant's remarks
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: `Remarks` is "Remarks by the applicant for this certificate"; the text is the classer's result.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark; grade and staple are item properties already.
- Needs decision: no

### cotton/07#F7 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: as cotton/02#F6: the same part of Lisavu in two different address elements.
- Condition: the north coast is carried in the same element everywhere.
- Options: (preferred) `District` in both.
- Needs decision: no

### cotton/07#F8 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/ForecastRevision/cac:ForecastRevisionLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: as cotton/02#F7: `PackSizeNumeric` is "The number of items in a pack"; 227 is the bale weight in kg.
- Condition: the bale weight is not carried as a count.
- Options: (preferred) drop `PackQuantity` and `PackSizeNumeric`.
- Needs decision: no

### cotton/07#F9 · Low · Tax registration of the sender in a forecast revision
- XPath: `/ForecastRevision/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: a forecast revision has no amounts or taxes; the tax registration looks copied from master data.
- Condition: no tax registration of the parties without a use in the document.
- Options: (preferred) drop `PartyTaxScheme`.
- Needs decision: no

## Checked and consistent
- The revision refers to forecast 02 (`OriginalDocumentReference` LTM-FC-26-0192), revises its line 1, and gives the source issue date and time of 02 (2026-02-02, 09:00:00); sequence number 1 is the first revision.
- Purpose code ORDER as in 02; header forecast period unchanged (16 Feb – 2 Jun).
- The classing certificate quoted is signed on 2026-02-20, before this revision (2026-02-22).

## Considered and refuted
- `/ForecastRevision/cbc:RevisionStatusCode`: `REVISED` in a document that is by definition a revision — refuted: the code distinguishes a revision from a cancellation; it carries meaning.
