# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/01#F1 · High · The consumption average amount is this month's amount, not the average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `11269440`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 405433 kWh.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `11269440`
- Why: AverageAmount is "The average monetary amount of the consumption". The description gives the three-month average as 405433 kWh ((398400 + 405100 + 412800) / 3 = 405433.3, from the two `ConsumptionHistory` entries and this month), which at the unit price of 27.3 XUF is about 11068330 XUF (the history amounts 10876320 and 11059230 plus 11269440, divided by 3, give the same). The value 11269440 is exactly March's line amount (412800 × 27.3), so the average amount contradicts both its own description and the history it averages.
- Condition: AverageAmount equals the average of the amounts of the months the description averages (or the description and the amount describe the same thing).
- Options: (a, preferred) set AverageAmount to the three-month average amount, consistent with the description; (b) drop AverageAmount and keep only the description.
- Needs decision: no

### utilities/01#F2 · High · Excise reported for the factory is the whole invoice's excise, and is left out of the statement's payable amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- Why: The EnergyTaxReport sits in the consumption of this consumption point (the factory meter FE-M-881204, 412800 kWh). The parent invoice's excise of 288840 XUF covers both electricity lines: 50000 kWh × 1.2 + (412800 + 18600 − 50000) kWh × 0.6 = 60000 + 228840 (the subtotals of `02-Invoice.xml:/Invoice/cac:TaxTotal[1]`). It therefore includes the excise on the 18600 kWh of the Castrano warehouse, which `03-UtilityStatement.xml` reports as a separate consumption point; the factory's share is at most 277680 XUF. In addition, the statement's `LegalMonetaryTotal` ("The total amount payable on this consumption, including any allowances, charges, or taxes") is 11269440 + 20 % VAT = 13523328 and contains neither the excise it reports nor the VAT the invoice charges on that excise (the invoice's VAT base `02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140` includes it).
- Condition: The excise reported for this consumption point is the excise on this consumption point's quantity, and the statement's totals either include the taxes the statement reports for it or the statement says why not.
- Options: (a, preferred) report the factory's share of the excise and include it (and the VAT on it) in the consumption totals; (b) move the excise to a level that covers the whole invoice and state it there; (c) drop the EnergyTaxReport.
- Needs decision: no

### utilities/01#F3 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cbc:Description` = `The supply under the customer's contract.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Ferrano Energy`
- Why: UBL defines SubscriberConsumption/Consumption as "The consumption in case the consumption is from one and only one supplier" and SupplierConsumption as "The consumption in case the consumption is from more than one supplier". This consumption point has one supplier (Ferrano Energy, the sender), and the statement carries both aggregates, with the same period and totals in both. The condition of SupplierConsumption is not met; the two aggregates also present the same consumption twice.
- Condition: SupplierConsumption appears only where the consumption of the point comes from more than one supplier; a single-supplier consumption is described in Consumption alone.
- Options: (a, preferred) remove SupplierConsumption here and keep the line-level data (ConsumptionLine, Contract) only where UBL places it for one supplier, accepting the loss of coverage; (b) give the world a real second supplier at this point (e.g. a separate network operator billing the network charges) and describe each supplier's share — this changes the story.
- Needs decision: yes

### utilities/01#F4 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: UtilityStatement/CustomerParty is "The buyer, if different from the receiver of the document." Here the buyer is the receiver (same identifier XU-R-104274), so the condition of the element is not met (contrast `03-UtilityStatement.xml`, where the receiver is Castrano Logistics and the customer Valdara).
- Condition: CustomerParty is present only when the buyer differs from ReceiverParty.
- Options: (a, preferred) leave CustomerParty out in this statement.
- Needs decision: no

### utilities/01#F5 · Medium · One-time charge type on an item that is charged monthly
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeType` = `Connection to the 10 kV grid, paid once in 2024`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeTypeCode` = `CONN`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:CurrentChargeTypeCode` = `M`
- Why: OneTimeChargeType is "Information about the one-time payment type in case everything is paid One time". The utility item is electricity per kWh, charged monthly (CurrentChargeTypeCode M); nothing of it is paid one time. The text describes a different charge (the 2024 grid connection), which this statement and its invoice do not bill; it is history of the contract, not a property of the consumed item.
- Condition: OneTimeChargeType/Code appear only on a utility item that is paid one time, and describe that item's payment.
- Options: (a, preferred) remove both elements from the kWh item; (b) if the world needs the connection charge, bill it as its own item in a statement whose invoice charges it.
- Needs decision: no

### utilities/01#F6 · Medium · The subscriber identifier is the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`
- Why: SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point" (and, on the item, "An identifier for the subscriber to the utility"). The value is the contract identifier (Contract/ID, and `02-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:Description` = `Supply contract`). An identifier of a contract is used as the identifier of a party.
- Condition: SubscriberID holds an identifier of the subscriber (e.g. a customer number assigned by Ferrano Energy), distinct from the contract number, or is absent.
- Options: (a, preferred) give the subscriber its own customer number and use it in both places; (b) remove SubscriberID where only the contract is known.
- Needs decision: no

### utilities/01#F7 · Low · SubscriberType on the utility item names the utility, not a type of subscriber
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Industrial`
- Why: UtilityItem/SubscriberType is "Identification of the subscriber type, expressed as text"; its code twin SubscriberTypeCode is defined as "The code identifying for the service type", and carries ELEC from the UtilityTypeCode list. The two definitions of the pair disagree in UBL itself. "Electricity" fits the code's definition but not the text's, and it differs from the subscriber type "Industrial" given for the same subscriber at the consumption point.
- Condition: Text and code on the utility item describe the same thing and fit their definitions, or the question is recorded as a UBL finding.
- Options: (a) drop the text SubscriberType and keep the code as service type (preferred: the code's definition is the more specific); (b) use the subscriber type (Industrial) in both, with a subscriber-type list; (c) record the contradiction between the two UBL definitions as a finding for the TC.
- Needs decision: yes

### utilities/01#F8 · Low · Buyer's accounting cost "Raw materials and parts" for the factory's electricity
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". Electricity for the factory is an energy or overhead cost, not raw materials and parts. The code 3100 is also Valdara's ISIC class (`/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3100`). The same text occurs in 12 examples (`grep -rl --include='*.xml' 'Raw materials and parts' world/examples | wc -l`), which suggests Valdara's default cost centre for material purchases copied into an energy statement.
- Condition: The accounting cost fits what is consumed (energy for the factory), or is absent.
- Options: (a, preferred) an energy or factory-overhead cost centre of Valdara; (b) leave it out of the statement.
- Needs decision: no

### utilities/01#F9 · Low · Receiver master data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- Why: A utility statement explains consumption to the receiver. Valdara's listed shares, its logistics service provider (warehousing and despatch by Castrano Logistics), its customs trader number and its order desk (a sales contact that takes Valdara's own customers' orders) play no part in it. They look copied from the party's master data.
- Condition: The receiver carries only what the statement uses: identification, name, address, electronic address and a contact that deals with energy bills.
- Options: (a, preferred) remove these from the statement and use a contact such as Valdara's accounts payable or facility management.
- Needs decision: no

### utilities/01#F10 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: The delivery location says only that it is the consumption point (which the statement already gives with address and ID), and the history descriptions say only what their Period already says. Under the rule "no fillers" (IND5) a value needs a reason; these carry none.
- Condition: Each description says something the structured data does not, or is absent (the Delivery aggregate goes if it has nothing else).
- Options: (a, preferred) remove them.
- Needs decision: no

### utilities/01#F11 · Low · Meter constant 40 and 5 A rated current do not fit a 10 kV main connection
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstant` = `40`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:Description` = `Factory, main connection at 10 kV`
- Why: (Own knowledge of metering practice.) A meter on a 10 kV connection is connected through voltage transformers (e.g. 10000/100 V, ratio 100) and current transformers, so its constant is the product of both, typically in the thousands. A constant of 40 corresponds to a 200/5 A current transformer alone, i.e. low-voltage metering. The consumption also does not fit low voltage: 412800 kWh in March is about 555 kW on average over 744 h, which at 400 V three-phase is about 800 A, four times a 200 A transformer. At 10 kV the same load is about 32 A primary.
- Condition: Meter constant, transformer type and the stated connection voltage agree with each other and with the consumption.
- Options: (a, preferred) a constant that combines VT and CT ratios for 10 kV (e.g. 100 × 10 = 1000, with readings scaled to match); (b) describe the connection as low-voltage with a CT ratio that fits the load.
- Needs decision: no

## Checked and consistent
- `ParentDocumentReference` FE-INV-26-0313 resolves to `02-Invoice.xml`; `ParentDocumentLineReferenceID` 1 is its line 1 (412800 kWh, 11269440 XUF, price 27.3 per kWh); the statement is issued after the invoice (17:54 vs 13:20).
- Meter reading: (63280 − 52960) × 40 = 412800 kWh, equal to DeliveredQuantity, TotalDeliveredQuantity, TotalMeteredQuantity, TotalConsumedQuantity and InvoicedQuantity.
- ConsumptionHistory amounts: 398400 × 27.3 = 10876320; 405100 × 27.3 = 11059230. ConsumptionReportReference (February, 405100 kWh) agrees with ConsumptionHistory[2].
- VAT: 20 % × 11269440 = 2253888; 11269440 + 2253888 = 13523328 (but see F2 for the excise).
- UtilityStatementTypeCode ELEC agrees with Consumption/UtilityStatementTypeCode and the item.
- Contract FE-C-0047120 agrees with `02-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:ID` = `FE-C-0047120`; meter FE-M-881204 with `02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:ID` = `FE-M-881204`.
- Check digit of the ISIN XU0001042501: OK (check_ids.py).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberParty`: the subscriber equals the receiver — refuted because SubscriberParty has no "if different" condition.
- `/UtilityStatement/cac:SubscriberConsumption/cbc:Note`: repeats the consumption point description — refuted because a note naming the consumption point as a heading of the specification is a legitimate use, not a contradiction.
- `/UtilityStatement/cac:SubscriberConsumption/cbc:SpecificationTypeCode`: DETAILED for a monthly statement — refuted because the definition gives on-account and yearly specifications as examples of types, and a detailed monthly specification is a type of that kind.
- `/UtilityStatement/cac:AdditionalDocumentReference`: tariff referenced only by ID — refuted because DocumentTypeCode TARIFF and the description say what it is.

## Outside this review
- The per-unit excise rates of `02-Invoice.xml` (PerUnitAmount 1 for both tiers, while the amounts imply 1.2 and 0.6 XUF/kWh) lie in that example.
