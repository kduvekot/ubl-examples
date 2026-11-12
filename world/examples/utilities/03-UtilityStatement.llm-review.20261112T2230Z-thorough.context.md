# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/03-UtilityStatement.xml`, Git blob `a8d48fa5c4e614ea05c1521143210974ea8bf6f9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/03#F1 · High · The estimate correction double-counts February's over-estimate and is applied nowhere
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity` = `117250`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:LatestMeterQuantity` = `135850`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `507780`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:ConsumptionLevel` = `Normal`
- Why: March is billed as latest actual reading minus February's estimated reading: 135850 − 117250 = 18600 kWh. Billing from the estimated reading already corrects February's over-estimate (February 17200 + March 18600 = the real consumption of both months), so a further −750 kWh would correct it twice. Nor can a single actual reading on 31 March show how much of the 18600 + 17200 kWh fell in February: that would need an actual reading on 28 February, which the statement says did not exist ("Estimated: no access to the meter"). Finally the correction is applied nowhere: the consumption total 507780 = 18600 × 27.3, and `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `507780` contains no −20475. The history still lists February as 17200 kWh, "Normal", without marking it as an estimate.
- Condition: The statement describes a correction only if it is real and not already contained in the billed quantity, and then the statement's totals and the parent invoice apply it.
- Options: (a, preferred) remove the correction and explain in MeterReadingComments that billing from the estimated reading settles February's estimate; (b) keep a correction, but then base March on an actual February reading and carry the credit into the totals and invoice line 2.
- Needs decision: yes

### utilities/03#F2 · High · CorrectionUnitAmount × quantity ≠ CorrectionAmount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: −750 × 27 = −20250, not −20475. The amount was calculated with the price 27.3 XUF/kWh (−750 × 27.3 = −20475); the unit amount is that price rounded to whole Ferra.
- Condition: CorrectionUnitAmount × ConsumptionEnergyQuantity = CorrectionAmount (if the correction stays, see F1).
- Options: (a, preferred) CorrectionUnitAmount 27.3.
- Needs decision: no

### utilities/03#F3 · High · The consumption average amount is this month's amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `507780`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 17900 kWh.`
- Why: AverageAmount is "The average monetary amount of the consumption". The three-month average (17900 + 17200 + 18600) / 3 = 17900 kWh is worth 17900 × 27.3 = 488670 XUF (also the average of the history amounts 488670, 469560 and 507780). 507780 is March's amount.
- Condition: AverageAmount is the average amount of the months the description averages.
- Options: (a, preferred) 488670; (b) drop AverageAmount.
- Needs decision: no

### utilities/03#F4 · High · The statement's cost centre contradicts the invoice line it explains
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCost` = `Warehouse, Castrano Logistics`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". This statement explains only invoice line 2 (ParentDocumentLineReferenceID 2), the warehouse electricity, which the invoice books to Valdara's cost centre 7100 "Warehouse, Castrano Logistics". The statement gives the invoice header's cost centre for raw materials instead.
- Condition: The statement's cost centre is the one the invoice applies to the line it explains, or is absent.
- Options: (a, preferred) 7100 / "Warehouse, Castrano Logistics"; (b) leave it out.
- Needs decision: no

### utilities/03#F5 · Medium · District-heating correction elements used for an electricity estimate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: The aggregate is general ("Describes any corrections or adjustments to the supply of energy or water"), but these children are defined for district heating: CorrectionUnitAmount "Correction per MWH per degree C", ConsumptionEnergyQuantity "Your consumpt for district heating energy", CorrectionAmount "Your correction for heating correction". An electricity estimate correction is neither per MWh per °C nor district heating energy.
- Condition: The correction elements, if kept, are used with the meaning their definitions give; otherwise the estimate correction is expressed where UBL has a general place for it (e.g. MeterReadingComments, a correcting line) or left out (see F1).
- Options: (a, preferred) remove the aggregate together with F1(a); (b) record the narrowness of the UBL definitions as a finding.
- Needs decision: no

### utilities/03#F6 · Medium · Subscriber is Castrano, but the subscriber ID and contract are Valdara's
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: SubscriberParty is "The Party that is the subscriber of the utility"; SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point". The ID given is Valdara's supply contract FE-C-0047120 (the same as in `01-UtilityStatement.xml`), Valdara is the UtilityCustomerParty and pays the invoice. Either Valdara is the subscriber (one contract covering both points) and Castrano is only the occupant who receives the statement, or Castrano holds its own subscription, which would then need its own subscriber ID. The statement says both. The ID is also a contract number, not a subscriber identifier (see `01-UtilityStatement.xml`).
- Condition: Subscriber party, subscriber ID and contract describe one consistent arrangement.
- Options: (a, preferred) Valdara as subscriber, Castrano as receiver only (keeping the story of 02, where Valdara pays for the warehouse); (b) Castrano as subscriber with its own subscriber number under Valdara's contract.
- Needs decision: yes

### utilities/03#F7 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Ferrano Energy`
- Why: SupplierConsumption is "The consumption in case the consumption is from more than one supplier"; Consumption is for "one and only one supplier". The warehouse has one supplier, and both aggregates are present with the same totals.
- Condition: SupplierConsumption only where there is more than one supplier.
- Options: as in `01-UtilityStatement.xml` (remove, or give the world a real second supplier).
- Needs decision: yes

### utilities/03#F8 · Low · SubscriberType on the utility item names the utility
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Commercial`
- Why: The text is defined as "Identification of the subscriber type", its code twin as "the service type"; "Electricity" fits only the latter, and differs from the subscriber type "Commercial" at the consumption point.
- Condition: As in `01-UtilityStatement.xml`.
- Options: drop the text, or align both with one definition and record the UBL inconsistency.
- Needs decision: yes

### utilities/03#F9 · Low · Party master data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: Castrano's shareholder, and Valdara's listed shares, logistics provider, customs trader number and order desk, are not used by a statement of warehouse electricity. They look copied from master data. (The 100 % shareholding may explain why Valdara pays; if so the story should say it where it is used.)
- Condition: The parties carry only what the statement uses.
- Options: (a, preferred) remove them; keep CustomerParty to identification and name.
- Needs decision: no

### utilities/03#F10 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- Why: These repeat what the consumption point and the history Period already say (IND5, no fillers).
- Condition: Removed, or replaced by text that adds information.
- Options: (a, preferred) remove.
- Needs decision: no

## Checked and consistent
- `ParentDocumentReference` FE-INV-26-0313 → `02-Invoice.xml`, line 2: 18600 kWh, 507780 XUF, meter FE-M-881377 (`02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:PurchaseReference/cbc:ID` = `FE-M-881377`); issued after the invoice.
- Meter: 135850 − 117250 = 18600 kWh with constant 1 (direct connection, plausible for a warehouse of about 25 kW average).
- VAT 20 % × 507780 = 101556; 507780 + 101556 = 609336.
- History amounts 17900 × 27.3 = 488670, 17200 × 27.3 = 469560; ConsumptionReportReference February 17200 kWh agrees with ConsumptionHistory[2].
- CustomerParty Valdara differs from ReceiverParty Castrano, so its condition is met here.
- No excise is reported for the warehouse; the whole invoice excise appears in `01-UtilityStatement.xml` (finding there).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:MeterReadingComments`: duplicates the method code — refuted because it explains to the reader why the previous reading is an estimate, which the code alone does not.
- `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty`: subscriber given twice (document level and consumption level) — refuted because the two have different scopes in UBL.
