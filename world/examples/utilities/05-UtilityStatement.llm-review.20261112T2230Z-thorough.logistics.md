# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/05-UtilityStatement.xml`, Git blob `f5bb8506980bfe0a7e311a1ed3ba8b85f0c771d7` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
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

### utilities/05#F1 · Low · Contract number used as subscriber identifier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-260118`
- Why: SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point" (and, under UtilityItem, "An identifier for the subscriber to the utility"); the value is the supply contract's ID. An identifier of one kind is used as another. Same pattern in all five statements of the flow (see utilities/01#F3).
- Condition: SubscriberID identifies the subscriber (customer number), or is absent.
- Options: a customer number of the water company (preferred), or drop SubscriberID.
- Needs decision: no

### utilities/05#F2 · Low · "Maximum flow" of 2.5 m³/h is the meter's nominal (permanent) flow rate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:Name` = `Maximum flow`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `2.5`
- Why: (own knowledge) 2.5 m³/h is a standard size of a small water meter: the permanent flow rate Q3 of ISO 4064 / OIML R49 (formerly the nominal flow Qn). The maximum (overload) flow of such a meter is Q4 = 1.25 × Q3 = 3.125 m³/h (old scheme: Qmax = 2 × Qn = 5 m³/h). Calling the 2.5 m³/h value the maximum flow mislabels the property. The size itself fits the use: 86 m³ in March is 0.12 m³/h on average, about 5 % of Q3.
- Condition: the property name and value agree with the meter rating they state (Q3 2.5 m³/h, or a maximum flow of 3.125 m³/h).
- Options: (a, preferred) rename the property to the permanent flow rate (Q3); (b) keep "Maximum flow" with 3.125 m³/h. The same property occurs in 08-UtilityStatement.xml.
- Needs decision: no

### utilities/05#F3 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: the Location carries no identifier or address, only a pointer to the consumption point CSW-CP-38510-411 that the statement already identifies; no information (no fillers). See utilities/01#F5.
- Condition: Delivery is absent or identifies the location.
- Options: remove it (preferred), or give the consumption point's ID.
- Needs decision: no

## Checked and consistent
- Meter reading: 4,298 − 4,212 = 86 m³ × constant 1 = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity; invoice 06 line 1 bills 86 m³ for meter CSW-W-55102 and the sewage levy line also uses 86 m³.
- History: 81 × 2.35 = 190.35; 79 × 2.35 = 185.65; 86 × 2.35 = 202.10; average (81 + 79 + 86) / 3 = 82 m³ as described; ConsumptionReportReference CSW-CP-38510-411-2602 (79 m³) agrees with the February entry.
- Reading dates 2026-02-28 and 2026-03-31 enclose the period; issued 2026-04-02 11:55, after the parent invoice 06-Invoice.xml (09:13); ParentDocumentLineReferenceID 1 is that invoice's InvoiceLine 1.
- Units: MTQ (cubic metre) for quantities, MQH (cubic metre per hour) for the flow property.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID`: the point ID contains 38510 while the postal zone is 38515 — refuted because a consumption point ID need not encode the postal zone.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: the statement explains 202.10 while the parent invoice is 238.22 — refuted because the difference is the sewage levy collected for the city (86 m³ × 0.42 = 36.12), which is not a consumption of the water supply this statement explains.

## Outside this review
- Outside the logistics lens (money): `ConsumptionAverage/AverageAmount` = 202.10 is March's amount, not the three-month average amount ((190.35 + 185.65 + 202.10) / 3 = 192.70).
