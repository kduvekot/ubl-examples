# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

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

### utilities/03#F1 · High · Correction unit amount does not produce the correction amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: −750 kWh × 27 XUF = −20250 XUF, not −20475. The correction amount corresponds to the actual price of 27.3 XUF/kWh (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Price/cbc:PriceAmount` = `27.3`; 750 × 27.3 = 20475). The unit amount is rounded and contradicts both the price and the correction amount.
- Condition: CorrectionUnitAmount × ConsumptionEnergyQuantity = CorrectionAmount, with the unit amount equal to the price at which February was billed.
- Options: (a, preferred) CorrectionUnitAmount 27.3.
- Needs decision: no

### utilities/03#F2 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `507780`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 17900 kWh.`
- Why: AverageAmount is "The average monetary amount of the consumption". The average quantity is right ((17900 + 17200 + 18600) / 3 = 17900 kWh), and its amount is 17900 × 27.3 = 488670 XUF (= (488670 + 469560 + 507780) / 3). The value given, 507780, is March's line amount (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `507780`). The same pattern is in 01-UtilityStatement.xml.
- Condition: AverageAmount is the average of the amounts of the months whose quantities the description averages (488670 XUF).
- Options: (a, preferred) set it to 488670.
- Needs decision: no

### utilities/03#F3 · High · Statement books the warehouse consumption to the account the invoice does not use for it
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCost` = `Warehouse, Castrano Logistics`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". This statement covers only invoice line 2 (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:ParentDocumentLineReferenceID` = `2`), which the parent invoice books to the buyer's cost centre 7100 "Warehouse, Castrano Logistics". The statement applies the invoice header's 3100 "Raw materials and parts" instead, so the two documents give different cost accounts for the same consumption.
- Condition: The accounting cost of this statement is the one the invoice gives for line 2 (7100), or is absent.
- Options: (a, preferred) 7100 "Warehouse, Castrano Logistics"; (b) leave it out, since the receiver (Castrano) is not the buyer whose accounts these are.
- Needs decision: no

### utilities/03#F4 · Medium · Castrano is the subscriber, but the subscription and the subscriber ID are Valdara's
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: SubscriberParty is "The Party that is the subscriber of the utility", and the consumption point's SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point". The ID given is Valdara's supply contract FE-C-0047120, the same as in 01-UtilityStatement.xml where Valdara is the subscriber, and invoice 02 bills this consumption to Valdara under that contract. Castrano consumes at the warehouse but does not hold the subscription. One identifier thus stands for two different subscribers in the two statements.
- Condition: The subscriber parties and the subscriber ID of this statement name the same party, and agree with who holds contract FE-C-0047120.
- Options: (a) Valdara as subscriber, with Castrano in another role (e.g. ReceiverParty only, plus a note that it is the user of the warehouse connection); (b) Castrano as subscriber with its own subscriber ID or contract, if Castrano holds a sub-contract under Valdara's supply. Preference: (a), since the invoice bills Valdara under its own contract.
- Needs decision: yes

### utilities/03#F5 · Medium · Statement totals leave out the excise the invoice charges on this consumption
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `101556`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- Why: The Consumption's LegalMonetaryTotal is "The total amount payable on this consumption, including any allowances, charges, or taxes", and its TaxTotal "The total of taxes for each tax type covering the consumption". Here both contain only VAT (507780 × 20 % = 101556; 507780 + 101556 = 609336). Invoice 02 levies an excise on its electricity (288840 = 50000 × 1.2 + 381400 × 0.6 over the 431400 kWh of lines 1 and 2) and VAT on top of it, so part of the excise and its VAT falls on these 18600 kWh. The invoice does not apportion the excise per line explicitly, which is why this is Medium rather than High.
- Condition: The statement's tax total and payable amount include the share of excise (and VAT on it) that invoice 02 charges on this consumption, or the statement says that the excise is charged at invoice level only.
- Options: (a) add the excise share as its own TaxTotal and include it in the totals; (b) a note that the energy tax is charged on the invoice as a whole. Preference: (b), since the tiers apply to the month's total kWh and cannot be split per meter without an allocation rule.
- Needs decision: no

### utilities/03#F6 · Medium · CorrectionAmount is not applied anywhere, and the history still shows the overestimated February
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Quantity` = `17200`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:BasicConsumedQuantity` = `18600`
- Why: The correction says February's estimate was 750 kWh too high. Because March is billed from the estimated previous reading (135850 − 117250 = 18600), the 750 kWh are already given back in March: the actual March consumption is 135850 − (117250 − 750) = 19350 kWh, of which 750 kWh are offset. Neither the statement's totals nor invoice line 2 (507780 = 18600 × 27.3) apply the −20475 separately, which is right if it is implicit, but the statement does not say so; read literally, a correction of −20475 XUF is reported and not credited. At the same time the history and the three-month average still use February's overestimated 17200 kWh, and BasicConsumedQuantity ("The basic quantity consumed, excluding additional consumption") shows 18600 where the real March consumption is 19350.
- Condition: It is clear from the statement whether the correction is contained in the March quantity or charged separately; the quantities and history are consistent with that reading (e.g. March 19350 kWh basic, −750 kWh correction, 18600 kWh total; February 16450 kWh).
- Options: (a, preferred) BasicConsumedQuantity 19350, TotalConsumedQuantity 18600, history and average with the corrected February, and a description saying the correction is settled through the March reading; (b) keep the quantities and state in the correction's description that it is included in the March quantity.
- Needs decision: no

### utilities/03#F7 · Medium · SupplierConsumption duplicates Consumption for a single supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- Why: SubscriberConsumption/Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption is "The consumption in case the consumption is from more than one supplier". Both are present with identical totals for one supplier, Ferrano Energy, so their conditions contradict each other. (CustomerParty is right here, since the buyer Valdara differs from the receiver Castrano.)
- Condition: Only the alternative that matches the number of suppliers is used.
- Options: (a) Consumption only; (b) SupplierConsumption only if a second supplier exists; (c) record that consumption lines are only reachable under SupplierConsumption as a finding on the UBL model.
- Needs decision: yes

### utilities/03#F8 · Medium · Province in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country (CountrySubentity). Same value in Region in 104 examples (`grep -l --include='*.xml' -r '<cbc:Region>Province of'`).
- Condition: Urvanian provinces are in CountrySubentity.
- Options: (a, preferred) CountrySubentity.
- Needs decision: no

### utilities/03#F9 · Low · Customer and receiver details that do not fit this statement
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The customer's customs trader number and stock-exchange listing and its order desk play no part in a statement of warehouse electricity; they look copied from Valdara's master data (CustomerParty here carries Valdara's full party, where 01 has only ID and name). The receiver's contact is the "Warehouse office", but with job title "Customer service officer" in department "Sales": name, title and department do not agree with each other.
- Condition: The customer carries only the data this statement uses; the receiver's contact has a name, title and department that agree.
- Options: (a, preferred) reduce CustomerParty to identification and name, as in 01; give the warehouse office a matching title and department (e.g. warehouse manager, Operations).
- Needs decision: no

### utilities/03#F10 · Low · Subscriber type of the utility item is "Electricity", the consumption point's is "Commercial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `COM`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text" while SubscriberTypeCode is "The code identifying for the service type". The example uses the utility type in both; by the element names the same subscriber has two types in one statement. Same as 01-UtilityStatement.xml.
- Condition: Either consistent with the consumption point, or the service-type reading is recorded as a deliberate reading of UBL's inconsistent definitions.
- Options: (a) record the UBL definition inconsistency and keep; (b) leave both out of the utility item.
- Needs decision: yes

### utilities/03#F11 · Low · Filler descriptions
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: These say nothing the structured data next to them does not say (rule "no fillers"). The history description of February could instead say that it was an estimate, which is real information here.
- Condition: Each description carries information of its own, or is absent.
- Options: (a, preferred) drop the delivery location; describe February's history entry as estimated and drop "Earlier month." for January.
- Needs decision: no

## Checked and consistent
- Meter: (135850 − 117250) × 1 = 18600 kWh with constant 1 "DIRECT" for a warehouse meter; consistent with all delivered and consumed quantities and with invoice line 2 (18600 kWh, 507780 XUF, meter FE-M-881377, delivery location the Castrano warehouse).
- Amounts: 18600 × 27.3 = 507780; VAT 20 % 101556; history 17900 × 27.3 = 488670 and 17200 × 27.3 = 469560; average quantity 17900 kWh correct.
- Reading methods: previous reading estimated (no access), latest manual, comment and correction description agree with each other.
- ConsumptionReportReference to February (17200 kWh) agrees with ConsumptionHistory[2].
- Parent reference FE-INV-26-0313 is 02-Invoice.xml; ParentDocumentLineReferenceID 2 is the warehouse line.
- Castrano Logistics as ReceiverParty, 100 % owned by Valdara (ShareholderParty), and CustomerParty Valdara different from the receiver: consistent with Castrano being Valdara's logistics provider (ServiceProviderParty of Valdara).
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/UtilityStatement/cbc:IssueTime`: statement FE-DOC-26-0315 issued at 17:10, before FE-DOC-26-0314 (01-UtilityStatement.xml) at 17:54 — refuted, document numbers may be allocated before issue; not material.
- `/UtilityStatement/cbc:Note[1]`: note in Urvanian to the receiver — refuted, Castrano's language is Urvanian.

## Outside this review
- 01-UtilityStatement.xml reports the whole invoice's excise as the energy tax of its consumption point (that example's review).
