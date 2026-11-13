# LLM review: 16-CommonTransportationReport.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/16-CommonTransportationReport.xml`, Git blob `fcbb7ae1a07ebdd8f8e779b15a6991056933bf53` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/16#F1 · Low · Reporter's sales-tax registration and share capital in a ship's pre-arrival report
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: The document is a pre-arrival report (`/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL`) from the carrier to the Maritime Administration of Lisavu: crew, passengers, stores, waste, ballast, ISPS and health. Nothing in it is invoiced, taxed or paid, and the Bayvarran state sales-tax registration (Coastal State) of the carrier, and its share capital, play no part in what the Lisavan maritime authority does with the report. It looks like the carrier's master data copied in (section 4.8). The same `PartyTaxScheme` of Tidewell Ocean Lines appears in 10 examples of the flow (07, 08, 12, 13, 14, 15, 16, 17, 18, 20; counted over `world/examples/sea/*.xml` by parsing every `cac:PartyTaxScheme` and grouping by party name), most of them non-billing documents.
- Condition: The reporter party carries a tax scheme and share-capital data only if the report has a stated use for them; otherwise neither is present.
- Options: (a) preferred: leave `PartyTaxScheme` and the capital data out of the reporter in this report, keeping identification, name, address and contact; (b) keep them and give the report a reason to carry them (e.g. port dues invoiced against this report), which changes the story.
- Needs decision: no

## Checked and consistent
- No monetary amount, price, allowance, charge, tax total or payment element occurs in the report; the only `currencyID` is on `CorporateStockAmount` (XBL, the currency of Bayvarra where the reporter is registered), and `TaxScheme/cbc:CurrencyCode` = XBL matches the Bayvarran jurisdiction.
- Tidewell's tax scheme (`CO-1235754`, STT, Coastal State, XBL) is described identically in every example of the flow that carries it.
- Fuel and emissions (not money, checked for completeness): 38 t marine gas oil × about 3.206 t CO2/t (IMO factor for MGO, own knowledge) = 121.8 t, matching `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:FuelConsumption/cac:EnvironmentalEmission/cbc:ValueMeasure` = `122`.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ShipStoreArticle[1]/cbc:Quantity` = `24`: suspected that bonded stores (spirits, cigarettes) need a value for duty — refuted because a ship's stores declaration reports quantities under seal; duty arises only if stores are landed, and the report does not say they are.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:FuelConsumption/cac:FuelProviderParty/cac:PartyName/cbc:Name` = `Port of Lumeport`: suspected a bunker purchase that should be priced or billed in the flow — refuted because the report only states who supplied the fuel; the bunker purchase is the carrier's own business outside this flow.
