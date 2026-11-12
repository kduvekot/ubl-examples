# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/08-UtilityStatement.xml`, Git blob `2ad70d0c87bdcb2a69e49f63c3882af20185d03e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/08#F1 · Medium · District-heating correction for a heat meter that this water statement does not otherwise know
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionTypeCode` = `COOL`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:MeterNumber` = `CSW-H-71844`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `0.80`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionWaterQuantity` = `6.2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `19.84`
- XPath: `/UtilityStatement/cbc:UtilityStatementTypeCode` = `WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ContractType` = `Water supply`
- Why: the statement is a drinking-water statement (type WATER, contract "Water supply", one water meter CSW-W-71844). The correction concerns district heating ("District heating cooling correction", "Your consumpt for district heating water") and names a meter CSW-H-71844 that appears nowhere else in the flow (MeterNumber counted over `world/examples/*/*.xml`: once) and is not among the consumption point's meters. Neither this statement nor its invoice 09-Invoice.xml has a heat supply, a heat contract or a district-heating line. The residence's heating type (district heating) explains why the flat has such a meter, not why the water company corrects its cooling here. The unit is also not the one the definition names: CorrectionUnitAmount is "Correction per MWH per degree C", but the amount works out per m³ per °C: 0.80 × 6.2 m³ × 4 °C = 19.84. (Physics, own knowledge: 6.2 m³ cooled by 31 K carries 6.2 × 1.163 × 31 ≈ 224 kWh of heat; a plausible quantity, but only part of a flat's heating in March.)
- Condition: a district-heating correction appears only in a statement that covers the district-heating supply and its heat meter (meter described at the consumption point, contract or supplier for heat present), with the correction unit per MWh per °C as UBL defines it; otherwise the water statement carries no such correction.
- Options: (a, preferred) remove the correction from the water statement (it belongs to the heat supplier's annual account, "charged on the annual account"); (b) if Coastal State Water Company also supplies district heat to this flat, add that supply (heat meter, contract, a separate SupplierConsumption or statement) and express the correction per MWh per °C.
- Needs decision: yes (whether the water company also supplies district heat changes the story)

### utilities/08#F2 · Low · Statement issued before the invoice it supplements
- XPath: `/UtilityStatement/cbc:IssueTime` = `15:10:00`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `CSWC-INV-26-0319`
- XPath: `09-Invoice.xml:/Invoice/cbc:IssueTime` = `15:44:00`
- Why: a Utility Statement is "A supplement to an Invoice or Credit Note", and ParentDocumentReference is "A reference to the parent Invoice or Credit Note". Both are dated 2026-04-02, but the statement is issued at 15:10, 34 minutes before its parent invoice exists (15:44). In the other four statement/invoice pairs of the flow the statement follows the invoice (01 after 02, 03 after 02, 05 after 06, 12 after 13). The document numbers (statement 0320 after invoice 0319) also put the invoice first.
- Condition: the statement's issue date and time are not earlier than those of its parent invoice.
- Options: an issue time after 15:44 for the statement (preferred, matches the numbering), or an earlier invoice time.
- Needs decision: no

### utilities/08#F3 · Low · Contract number used as subscriber identifier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-311790`
- Why: SubscriberID ("An identifier for the subscriber responsible for the consumption at this consumption point") holds the supply contract's ID. Same pattern in all five statements of the flow (see utilities/01#F3).
- Condition: SubscriberID identifies the subscriber (customer number), or is absent.
- Options: a customer number (preferred), or drop SubscriberID.
- Needs decision: no

### utilities/08#F4 · Low · "Maximum flow" of 2.5 m³/h is the meter's nominal (permanent) flow rate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:Name` = `Maximum flow`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `2.5`
- Why: (own knowledge) 2.5 m³/h is the permanent flow rate Q3 of a standard domestic meter (ISO 4064 / OIML R49); its maximum (overload) flow is Q4 = 1.25 × Q3 = 3.125 m³/h. See utilities/05#F2, same property.
- Condition: property name and value agree (Q3 2.5 m³/h, or maximum 3.125 m³/h).
- Options: rename to permanent flow rate (preferred), or give 3.125 m³/h.
- Needs decision: no

### utilities/08#F5 · Low · "Low consumer" for a consumption well above the usual per-person use
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevelCode` = `LOW`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidentOccupantsNumeric` = `2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `14`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidenceTypeCode` = `APT`
- Why: the level is "compared to the average for this residence type and the number of people living in the residence". 14 m³ in 31 days for 2 people is 14,000 l / 31 / 2 = 226 l per person and day. Typical household use in Europe is about 120–150 l per person and day (own knowledge). A household at 226 l/person/day is a high, not a low, consumer, unless the world's average is stated to be higher.
- Condition: the consumer level agrees with the consumption per occupant against the average the statement compares with.
- Options: (a) a lower consumption for two people (e.g. about 7–8 m³ a month) with readings, history and invoice to match, keeping LOW; (b) keep 14 m³ and make the level normal or high; (c, preferred, least change) three or four occupants, which gives 113–151 l per person and day.
- Needs decision: no

### utilities/08#F6 · Low · Document references with only an ID whose kind does not match the element
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:GuidanceDocumentReference/cbc:ID` = `CSW-SAVE-WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:DocumentReference/cbc:ID` = `CSW-QUALITY-2026-Q1`
- Why: GuidanceDocumentReference is "A reference to a document providing an explanation of this kind of report"; the ID suggests a water-saving guide, which explains how to save water, not how to read the consumption report. DocumentReference is "A reference to some other document (for example, this report in another format)"; CSW-QUALITY-2026-Q1 suggests a quarterly water-quality report, unrelated to the consumption report. Neither reference has a type, description or URI saying what it is.
- Condition: each reference says what it refers to, and the guidance reference refers to a document that explains the report.
- Options: (a, preferred) give each a DocumentTypeCode/DocumentDescription, and point the guidance reference to an explanation of the statement (or move the water-saving guide to an additional document reference at the header); (b) remove the references that the report does nothing with.
- Needs decision: no

### utilities/08#F7 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: the Location has no identifier or address, only a pointer to consumption point CSW-CP-38516-57 already identified in the statement (no fillers). See utilities/01#F5.
- Condition: Delivery is absent or identifies the location.
- Options: remove it (preferred), or give the consumption point's ID.
- Needs decision: no

## Checked and consistent
- Meter reading: 1,844 − 1,830 = 14 m³ × constant 1 = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity; invoice 09 line 1 bills 14 m³ for meter CSW-W-71844 (PurchaseReference), and the sewage levy line 14 m³.
- History: 15 × 2.35 = 35.25; 13 × 2.35 = 30.55; 14 × 2.35 = 32.90; average (15 + 13 + 14) / 3 = 14 m³ and (35.25 + 30.55 + 32.90) / 3 = 32.90; ConsumptionReportReference CSW-CP-38516-57-2602 (13 m³) agrees with February.
- Correction temperatures: 31 − 35 = −4 °C as DifferenceTemperatureReductionQuantity; 0.80 × 6.2 × 4 = 19.84.
- Reading dates 2026-02-28 and 2026-03-31; issued 2026-04-02 15:10.
- Login of the web access equals the consumption point ID CSW-CP-38516-57.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ActualTemperatureReductionQuantity`: a temperature difference in degrees Celsius (CEL) rather than kelvin — refuted because a difference of 1 °C equals 1 K and CEL is commonly used for such cooling values in district-heating billing.
- `/UtilityStatement/cac:Signature/cbc:ID`: CSW-SIG-26-0401 looks dated 1 April while the statement is of 2 April — refuted because the number need not be a date (it may be a signature sequence or the signing key's ID).

## Outside this review
- Outside the logistics lens (money): the statement says the household pays on account each month for the estimated use and that "the next bill settles it against the reading" (`/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note`), while the invoice 09 bills the full metered 14 m³ (32.90 + 5.88) with no on-account payment deducted.
