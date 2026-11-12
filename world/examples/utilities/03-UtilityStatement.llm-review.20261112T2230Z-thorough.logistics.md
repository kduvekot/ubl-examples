# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/03#F1 · High · Estimate correction contradicts the meter readings and is not reflected anywhere
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity` = `117250`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterReadingMethodCode` = `ESTIMATE`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:LatestMeterQuantity` = `135850`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:DeliveredQuantity` = `18600`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Quantity` = `17200`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `507780`
- Why: March's consumption is computed from the estimated February reading: 135,850 − 117,250 = 18,600 kWh. Measuring from an estimated reading already settles February's error over the two months (February billed + March billed = actual advance since the last actual reading), so a further −750 kWh correction would credit the same error a second time. If February really was 750 kWh lower (16,450 kWh), the true reading on 28 February was 116,500 and March's actual consumption is 135,850 − 116,500 = 19,350 kWh, not 18,600. The description also says "as the actual reading shows", but the only actual reading is the one of 31 March, which cannot show February's share on its own. Finally, the correction is reflected nowhere: the March line is 18,600 × 27.3 = 507,780 with no correction, the history and the referenced February report still give 17,200 kWh, the average (17,900 kWh) uses 17,200, and the invoice line 2 bills 18,600 kWh at full price (`02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `507780`).
- Condition: readings, consumption and correction tell one story: either the March quantity is measured from the estimated reading and no separate correction is stated, or the February reading is replaced by a corrected value, the March quantity is measured from it, and the correction of February's billed quantity appears in the amounts of this statement and of the invoice 02.
- Options: (a, preferred) drop the correction (the reading from an estimate settles it) and say in MeterReadingComments that this reading settles February's estimate; (b) keep a correction, but then base March on a corrected February reading (116,500 → 19,350 kWh) and carry the −750 kWh credit into the totals here and in 02 (see utilities/02#F2), with all arithmetic adjusted.
- Needs decision: yes (whether the estimate is corrected separately changes what the customer is billed)

### utilities/03#F2 · High · Correction unit amount does not give the correction amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Price/cbc:PriceAmount` = `27.3`
- Why: −750 kWh × 27 = −20,250, not −20,475. The stated amount is −750 × 27.3 (the price per kWh of the statement), so the unit amount is rounded and does not match the amount it is meant to explain.
- Condition: CorrectionUnitAmount × quantity = CorrectionAmount (if the correction stays, see F1).
- Options: unit amount 27.3; or remove the correction under F1 option (a).
- Needs decision: no

### utilities/03#F3 · Medium · Subscriber identifier of the warehouse point is Valdara's contract, while the subscriber is Castrano Logistics
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`
- Why: SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point". The statement names Castrano Logistics as "The Party who is subscribed to the utility" for this point, but the identifier given is the number of Valdara Industries' supply contract (the same as in 01-UtilityStatement.xml, Valdara's own factory point). An identifier of one kind (contract) is used as another (subscriber), and it identifies a different party than the subscriber the statement names.
- Condition: the subscriber identifier at the warehouse point identifies the same party as the SubscriberParty of this point, or the statement makes Valdara the subscriber consistently.
- Options: (a, preferred) give Castrano Logistics' own subscriber number at this point (or drop SubscriberID) and keep the contract in Contract/ID; (b) if Valdara is the subscriber of the warehouse supply and Castrano only the occupant, name Valdara as SubscriberParty and describe Castrano differently.
- Needs decision: yes (who subscribes to the warehouse supply)

### utilities/03#F4 · Medium · District-heating correction elements used for an electricity estimate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: in UBL 2.5 these elements are defined for the district-heating cooling correction: CorrectionUnitAmount "Correction per MWH per degree C", ConsumptionEnergyQuantity "Your consumpt for district heating energy", CorrectionAmount "Your correction for heating correction". Here they carry a price per kWh (not per MWh per °C), an electricity quantity and an electricity credit for an estimate correction. The unit also does not fit: 27 XUF per MWh per °C would be a different quantity altogether.
- Condition: if an estimate correction for electricity is stated, it uses only elements whose definition fits (e.g. CorrectionType/Code, MeterNumber, Description), and amounts or quantities of the correction appear where UBL defines them for electricity (e.g. as an allowance on the consumption line).
- Options: (a, preferred, together with F1 a) remove the correction aggregate; (b) keep type, meter and description in the correction aggregate and move quantity and amount to an allowance of the consumption line.
- Needs decision: no

### utilities/03#F5 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: the Location has no identifier or address, only a sentence pointing to the consumption point FE-CP-4160-07 that the statement already identifies; the aggregate carries no information (no fillers). Same sentence in five statements of the flow (see utilities/01#F5).
- Condition: Delivery is absent or identifies the location (e.g. with FE-CP-4160-07).
- Options: remove it (preferred), or give the consumption point's ID.
- Needs decision: no

## Checked and consistent
- Meter reading: 135,850 − 117,250 = 18,600 kWh × constant 1 (DIRECT) = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity = invoice 02 line 2 (meter FE-M-881377 in its PurchaseReference).
- History: 17,900 × 27.3 = 488,670; 17,200 × 27.3 = 469,560; average (17,900 + 17,200 + 18,600) / 3 = 17,900 kWh as described. ConsumptionReportReference FE-CP-4160-07-2602 (17,200 kWh) agrees with the February history entry.
- Reading methods: previous estimated ("no access to the meter"), latest read by the meter reader, with the comment saying so; dates 2026-02-28 and 2026-03-31 before the issue date 2026-04-02.
- Physics: 18,600 kWh in 744 h is 25 kW average, about 36 A per phase at 400 V; a direct-connected meter with basic current 5 A (maximum typically 60–100 A) carries that (own knowledge).
- VAT 20 % × 507,780 = 101,556; tax-inclusive 609,336.
- ParentDocumentReference FE-INV-26-0313 resolves to 02-Invoice.xml (issued 13:20, before this statement at 17:10); ParentDocumentLineReferenceID 2 is that invoice's line 2.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity`: rated current 5 A looked copied from the CT meter of 01 and too small for a direct meter — refuted because 5 A is a normal basic current of a direct-connected meter (e.g. 5(60) A or 5(100) A), and the average current (about 36 A) is within such a meter's range.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID`: the point ID FE-CP-4160-07 contains 4160 while the postal zone is 4130 — refuted because nothing requires a consumption point ID to encode the postal zone (it may be a network area).

## Outside this review
- Outside the logistics lens (money): `ConsumptionAverage/AverageAmount` = 507,780 is March's amount, not the three-month average amount (488,670).
- Outside the logistics lens (money): this statement carries no energy tax for the warehouse's 18,600 kWh; the whole invoice's energy tax is reported in 01-UtilityStatement.xml (finding utilities/01#F1).
