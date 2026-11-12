# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/01-UtilityStatement.xml`, Git blob `5afddf1d0c8c1838c6abd6e06e483af49cb2664f` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### utilities/01#F1 · High · Energy tax of the whole invoice reported for this one consumption point
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `412800`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- Why: the EnergyTaxReport sits in the Consumption of the consumption point FE-CP-4120-01 ("A utility statement for a particular consumption point"), which consumed 412,800 kWh. 288,840 XUF is the energy tax of the whole parent invoice 02-Invoice.xml, which covers the factory (412,800 kWh) and the Castrano warehouse (18,600 kWh, statement 03-UtilityStatement.xml): with the invoice's two tiers the figures only work out for 431,400 kWh, i.e. 50,000 kWh × 1.2 = 60,000 and (431,400 − 50,000) = 381,400 kWh × 0.6 = 228,840 (`02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`). For this point alone the same tiers give 50,000 × 1.2 + 362,800 × 0.6 = 277,680. The warehouse statement 03 carries no EnergyTaxReport, so the warehouse's share (18,600 × 0.6 = 11,160) is reported here. (The rates 1.2 and 0.6 are derived; the invoice states 1 per kWh for both tiers, see utilities/02.)
- Condition: the energy tax reported in this statement is the tax on this consumption point's 412,800 kWh, and the energy tax reported over statements 01 and 03 adds up to the invoice's energy tax.
- Options: (a, preferred) report this point's share here and the warehouse's share in 03, with the tier split stated; (b) state explicitly (e.g. in a description of the report) that the amount is the invoice total for both points, which still leaves a report attached to the wrong consumption point.
- Needs decision: no

### utilities/01#F2 · Low · Statement numbers out of order with their issue times
- XPath: `/UtilityStatement/cbc:ID` = `FE-DOC-26-0314`
- XPath: `/UtilityStatement/cbc:IssueTime` = `17:54:00`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cbc:ID` = `FE-DOC-26-0315`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cbc:IssueTime` = `17:10:00`
- Why: both statements were issued by Ferrano Energy on 2026-04-02 for the same invoice; the lower document number 0314 was issued 44 minutes after the higher number 0315. A sender's sequential numbering would normally follow issue order.
- Condition: within one sender and day, the document number order matches the issue time order.
- Options: swap the issue times (or the numbers) of 01 and 03.
- Needs decision: no

### utilities/01#F3 · Low · Contract number used as subscriber identifier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`
- Why: SubscriberID under UtilityConsumptionPoint is "An identifier for the subscriber responsible for the consumption at this consumption point", and under UtilityItem "An identifier for the subscriber to the utility". The value is the contract's ID, which the same statement gives as `Contract/ID`. An identifier of one kind (a contract) is used as another (a subscriber). The same pattern (SubscriberID equal to the contract ID) occurs in all five utility statements of the flow (01, 03, 05, 08, 12; counted by comparing SubscriberID with Contract/ID in `world/examples/utilities/*.xml`).
- Condition: SubscriberID holds an identifier of the subscriber (a customer or subscriber number), or the element is absent where only the contract identifies the subscription.
- Options: (a, preferred) give the customer a subscriber/customer number of Ferrano Energy (e.g. the account number used on the bill) and keep the contract in `Contract/ID`; (b) drop SubscriberID, since the contract reference already identifies the supply.
- Needs decision: no

### utilities/01#F4 · Low · Meter constant 40 does not fit metering at a 10 kV connection
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstant` = `40`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstantCode` = `CTRATIO`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:Description` = `Factory, main connection at 10 kV`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `5`
- Why: (own knowledge of metering practice) 412,800 kWh in March (744 h) is an average load of 555 kW. Metered on the 10 kV side, a meter needs both a current transformer and a voltage transformer (typically 10,000/100 V, ratio 100), so the multiplier would be CT × VT, e.g. 40 × 100 = 4,000, and the register would advance by about 103 kWh, not 10,320. Metered on the low-voltage side behind the factory's own transformer (400 V), the average current is 555,000 / (√3 × 400) ≈ 800 A, which a 200/5 A current transformer (ratio 40, secondary 5 A as in the rated-current property) cannot carry. The CT ratio 40 alone fits neither case; at 10 kV the primary current of about 32 A fits a 200/5 A CT, but then the VT ratio is missing.
- Condition: meter constant, its type code, the connection voltage and the register advance agree: register advance × constant = 412,800 kWh, with a constant that a meter at that voltage level would have.
- Options: (a, preferred) keep the 10 kV connection, give the combined transformer factor (e.g. 4,000, with a type code for CT × VT if the world's list has one) and readings that advance by 103.2 kWh; (b) meter on the LV side with a CT ratio that fits about 800 A average (e.g. 1500/5 = 300) and readings to match.
- Needs decision: no

### utilities/01#F5 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: the consumption line's Delivery/DeliveryLocation carries no identifier or address, only a sentence saying that it is the consumption point, which the statement already identifies (`/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID` = `FE-CP-4120-01`, with its address). The aggregate adds no information (no fillers, UBL IND5). The same sentence occurs in five examples (grep -c over `world/examples/*/*.xml`: 01, 03, 05, 08, 12 of utilities).
- Condition: the Delivery aggregate is either absent or identifies the delivery location (e.g. the consumption point's ID or address).
- Options: (a, preferred) remove the Delivery aggregate; (b) give the location the consumption point's ID.
- Needs decision: no

### utilities/01#F6 · Low · OneTimeChargeType on an item that is charged monthly
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeType` = `Connection to the 10 kV grid, paid once in 2024`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeTypeCode` = `CONN`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:CurrentChargeTypeCode` = `M`
- Why: OneTimeChargeType is "Information about the one-time payment type in case everything is paid One time". The item FE-KWH is kWh supply charged monthly (CurrentChargeTypeCode M), so the condition of the definition is not met; the text describes a different, past charge (the 2024 grid connection), which this line neither bills nor depends on.
- Condition: the utility item carries one-time charge information only if the item itself is paid once.
- Options: (a, preferred) remove both elements from this item; (b) if the connection charge matters to the statement, describe it where it belongs (e.g. a note or the contract), not as a property of the kWh item.
- Needs decision: no

## Checked and consistent
- Meter reading: (63,280 − 52,960) = 10,320 × constant 40 = 412,800 kWh = DeliveredQuantity = meter TotalDeliveredQuantity = consumption point TotalDeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity of 02-Invoice.xml line 1.
- Reading dates 2026-02-28 and 2026-03-31 enclose the period 2026-03-01 to 2026-03-31; both before the issue date 2026-04-02.
- Consumption history: 398,400 × 27.3 = 10,876,320; 405,100 × 27.3 = 11,059,230; 412,800 × 27.3 = 11,269,440. Three-month average (398,400 + 405,100 + 412,800) / 3 = 405,433.3 kWh, as the description says.
- ConsumptionReportReference FE-CP-4120-01-2602 (405,100 kWh, February) agrees with the February history entry.
- ParentDocumentReference FE-INV-26-0313 resolves to 02-Invoice.xml; ParentDocumentLineReferenceID 1 is that invoice's line 1 (412,800 kWh, 11,269,440 XUF, meter FE-M-881204 in its PurchaseReference). The invoice (13:20) is issued before this supplement (17:54).
- Average load 555 kW at 10 kV gives about 32 A primary current, within a 200/5 A CT with 5 A secondary (rated current property); see F4 for what does not fit.
- Check digits (check_ids.py): ISIN XU0001042501 OK.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode`: a utility type (ELEC) in a subscriber-type code — refuted because under UtilityItem the element is defined as "The code identifying for the service type", which ELEC fits; the consumption point uses its own SubscriberTypeCode (IND) correctly.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity`: register 52,960 × 40 = 2.12 GWh cumulative looks small for a supply of about 0.4 GWh a month since 2024 — refuted because a five-digit register rolls over at 99,999 and the meter may have been replaced at its 2024 calibration; the value cannot be shown to be wrong.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ID`: same value as the SubscriberConsumption's ConsumptionID — refuted because both identify this month's specification of the same point; no conflict of kinds.

## Outside this review
- Outside the logistics lens (money): `ConsumptionAverage/AverageAmount` = 11,269,440 is March's amount, not the three-month average amount ((10,876,320 + 11,059,230 + 11,269,440) / 3 = 11,068,330), while its description gives the three-month average quantity.
- Outside the logistics lens (money): the consumption's PayableAmount 13,523,328 = 11,269,440 + 20 % VAT on that amount, whereas the invoice charges VAT on the base including the energy tax (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140`).
