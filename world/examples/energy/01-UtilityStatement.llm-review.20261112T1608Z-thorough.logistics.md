# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/01-UtilityStatement.xml`, Git blob `ddb038e38819569df4aa78c5bfc77925766f9bb9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/01#F1 · Low · The parent invoice is issued after the statement that supplements it
- XPath: `/UtilityStatement/cbc:IssueDate` = `2026-04-02`
- XPath: `/UtilityStatement/cbc:IssueTime` = `17:42:00`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-03`
- XPath: `02-Invoice.xml:/Invoice/cbc:IssueTime` = `08:20:00`
- Why: UBL defines the Utility Statement as "a supplement to an Invoice or Credit Note" and `ParentDocumentReference` as "a reference to the parent Invoice or Credit Note". At the statement's issue time (2026-04-02 17:42) the parent invoice did not yet exist; it is issued the next morning (2026-04-03 08:20). A reserved invoice number is possible, but the statement then points to a document nobody can retrieve yet, and the parent invoice itself does not refer back to the statement (see `energy/02#F1`). Counted over `world/examples/*/*UtilityStatement.xml` (each statement's `ParentDocumentReference/cbc:ID` resolved to the example with that document ID, then issue date and time compared): 2 of 6 statements are issued before their parent invoice, this one and `utilities/08-UtilityStatement.xml`.
- Condition: the statement's issue date and time are not earlier than those of the invoice it names as parent, or the story says why the invoice number is known in advance.
- Options: (a) preferred: issue the statement after the invoice on 2026-04-03, or the invoice before the statement, so that the parent exists when it is referenced; (b) keep the order and let the invoice carry the reference to the statement (an `AdditionalDocumentReference`), so the link exists in both directions once both are issued.
- Needs decision: no

## Checked and consistent
- Meter arithmetic: `PreviousMeterQuantity` 28410 m³ + `DeliveredQuantity` 1350 m³ = `LatestMeterQuantity` 29760 m³; the same 1350 m³ in `UtilityMeter/cbc:TotalDeliveredQuantity` and `SubscriberConsumption/cbc:TotalMeteredQuantity`; `MeterConstant` 1 with `DIRECT` ("connected directly: the constant is 1").
- Volume conversion, calculated: (4 bar + 1.01325 bar) / 1.01325 bar = 4.9477, so the 4 bar in `GasPressureQuantity` is gauge pressure and the factor converts to an absolute reference pressure of 1.01325 bar; 1350 × 4.9477 = 6679.4 m³ (text: 6679 m³); 6679.4 × 9.163 kWh/m³ = 61 204 kWh, 6679 × 9.163 = 61 200 kWh. The 61200 kWh agree in `UtilityConsumptionPoint/cbc:TotalDeliveredQuantity`, `ConsumptionReport/cbc:TotalConsumedQuantity` and `EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity`, and with `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`.
- Plausibility of the load: 61 200 kWh over March (744 h) is an average of 82 kW, a plausible gas load for the coating ovens of one factory line.
- Dates: reading period 2026-02-28 → 2026-03-31 and `MainPeriod`/`ConsumptionReport/cac:Period` 2026-03-01 → 2026-03-31 agree; all readings are before the issue date.
- Reference: `ParentDocumentReference` FG-INV-26-0150 resolves to `02-Invoice.xml`, an Invoice of Ferrano Grid to Ferrano Energy for March 2026 that has a gas network line for the same 61200 kWh.
- Identifiers: consumption point FG-CP-4120-G1, meter FG-G-20417 and reading FG-G-20417-2603 are consistent with each other; the meter number in `EnergyWaterConsumptionCorrection/cbc:MeterNumber` is the meter of the consumption point. `check_ids.py`: ISIN XU0001042501 OK.
- Codes: `UtilityStatementTypeCode` GAS (top level and in `Consumption`), `CorrectionTypeCode` CONV ("Gas volume converted to energy"), `LatestMeterReadingMethodCode` REMOTE agree with their text equivalents; units MTQ, KWH and BAR fit their quantities.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `1350 m³ at line pressure × 4.9477 (pressure) = 6679 m³ at standard conditions, × 9.163 kWh/m³ (calorific value of March) = 61200 kWh.`: suspected a missing temperature correction, since a gas volume conversion normally corrects for pressure and temperature — refuted because a factor of 1 for temperature is legitimate when the gas is metered at the reference temperature, and the text names the corrections it applies; the figures hold.
- Same element: suspected that 9.163 kWh/m³ is too low for natural gas — refuted because it is within the range of low-calorific natural gas (about 8.4 to 13.1 kWh/m³ for the second gas family, own knowledge of DVGW G 260). Comparing it with the Kelpstone gas of `04-ExportCustomsDeclaration.xml` (75 kg per MWh) would give a density of 9.163 kWh/m³ × 0.075 kg/kWh = 0.687 kg/m³, which is lighter than gas of that calorific value should be; but nothing in the flow says the gas at this connection is the Kelpstone gas, so no contradiction can be shown.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:GasPressureQuantity` = `4`: suspected that the value is not a "correction of the gas pressure" (the definition) but the line pressure — refuted because the element is a quantity in bar, the pressure on which the correction is based, and the text next to it shows how it is applied.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ID` = `FG-CP-4120-G1-2603`: the same value as `/UtilityStatement/cac:SubscriberConsumption/cbc:ConsumptionID`; suspected one identifier used for two objects — refuted because the statement has one specification with one consumption report for the same consumption point and month, so one identifier for both is a legitimate choice.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047121`: suspected a mismatch with the electricity contract FE-C-0047120 of the same customer in `utilities/02-Invoice.xml` — refuted because a separate gas contract with its own subscriber number is plausible, and no example calls FE-C-0047121 anything else.

## Outside this review
- `utilities/02-Invoice.xml` (issued 2026-04-02 13:20) bills the 61200 kWh of this connection "converted ... by the grid operator's metering report", four and a half hours before this statement (2026-04-02 17:42) is issued: a timeline question across flows.
