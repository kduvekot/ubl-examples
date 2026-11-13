# LLM review: 07-InventoryReport.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/07-InventoryReport.xml`, Git blob `e1019ee6a13e2a7196d8ba163e99b452ac02b47f` (committed)
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

### retail/07#F1 · High · Emission factor times base does not give the emission
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F5: the report need not carry it).
- Options: drop the emission here (preferred), or correct the factor.
- Needs decision: no

### retail/07#F2 · Medium · Stock "currently in stock" counted four days before the report, for a period that ends on the issue day
- XPath: `/InventoryReport/cbc:Note` = `Counted on Sunday evening.`
- XPath: `/InventoryReport/cac:InventoryPeriod/cbc:EndDate` = `2026-04-23`
- XPath: `/InventoryReport/cbc:IssueDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:Quantity` = `3`
- Why: Quantity is "The quantity of the item reported that is currently in stock", and the
  InventoryPeriod is "The period covered by this report", ending on Thursday 2026-04-23, the issue
  day. The note says the stock was counted on Sunday evening, i.e. 2026-04-19, four shopping days
  earlier; the count does not give the current stock, nor the stock at the end of the period. Either
  the date of the count or the period/"current" is wrong.
- Condition: the count date and the period (and the meaning "currently in stock") agree.
- Options: (a) preferred: issue the report on Monday 2026-04-20 with a period ending on Sunday 19th;
  (b) keep the dates and say the count was made on the evening of the 23rd.
- Needs decision: no

### retail/07#F3 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples, `grep -l` over
  `*.xml`). LocaleCode is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) is a language code (213 examples).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/07#F4 · Low · Availability date for goods that are in stock
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityDate` = `2026-04-23`
- XPath: `/InventoryReport/cac:InventoryReportLine/cbc:AvailabilityStatusCode` = `AVAILABLE`
- Why: AvailabilityDate is "The date from which the goods will be available. If not present, the
  goods are available now." The three benches are in stock and available; a date equal to the issue
  date says nothing that the absence of the element would not say.
- Condition: AvailabilityDate only for goods that become available later.
- Options: drop it.
- Needs decision: no

### retail/07#F5 · Low · The report carries the item's full catalogue description and the parties' master data
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/InventoryReport/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/InventoryReport/cac:RetailerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: an inventory report tells the supplier how much is in stock. The item repeats the whole
  catalogue entry (seller's sales conditions, footprint, circularity, load test, dimensions, customs
  codes) and the parties carry share capital, tax schemes, a customs trader number and social media;
  the report does nothing with them (IND5/IND6).
- Condition: item and parties carry what the report uses (identifiers, name, quantity, location).
- Options: reduce the item to identifiers and name; drop the master data.
- Needs decision: no

### retail/07#F6 · Low · Stock location without the store
- XPath: `/InventoryReport/cac:InventoryReportLine/cac:InventoryLocation/cbc:Name` = `Garden department, ground floor`
- Why: InventoryLocation is "The location of the reported quantity of goods". It names a department
  and a floor, but not the store; Brightmarket is a chain ("Brightmarket Stores"), and the store
  receiving the benches has its own delivery location in the flow. The supplier cannot tell which
  store's stock this is.
- Condition: the location identifies the store (name, address or GLN), with the department as detail.
- Options: add the store's identification or address (preferred).
- Needs decision: no

### retail/07#F7 · Low · Signature without anything that signs
- XPath: `/InventoryReport/cac:Signature/cbc:ID` = `BM-SIG-26-0423`
- Why: only an ID and a signatory; no method, no attachment, no reason in the story.
- Condition: a signature with reason and data, or none.
- Options: drop it.
- Needs decision: no

## Checked and consistent
- RetailerCustomerParty ("The retailer, who sends this message") and InventoryReportingParty are
  Brightmarket; SellerSupplierParty is Lumeway, as the document definition expects (buyer to seller).
- InventoryValueAmount 1560.00 = 3 × 520 XBL, the trade price of 02-Catalogue.xml.
- The note on the line ("Below the minimum of 6 before the promotion") fits the promotion of
  06-RetailEvent.xml and the order 08-Order.xml that follows the next morning.
- The DocumentReference `BS-FC-26-0221` resolves to 05-Forecast.xml, issued the day before.

## Considered and refuted
- `/InventoryReport/cac:DocumentReference/cbc:ID`: a reference with only an ID — refuted because it
  resolves to the flow's forecast, an obvious companion of a stock report.
