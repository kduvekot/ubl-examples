# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

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

### utilities/01#F1 · High · Energy tax report carries the excise of the whole invoice, not of this consumption point
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- Why: The statement covers one consumption point, the factory main connection (`/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID` = `FE-CP-4120-01`), 412800 kWh, which is invoice line 1 (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:ParentDocumentLineReferenceID` = `1`). Its Energy Tax Report ("A tax on the consumption of energy or water", under the consumption of this subscriber) states 288840 XUF, which is exactly the excise of the whole invoice 02, levied there on all three lines: this factory electricity, the warehouse electricity of Castrano Logistics (line 2, 18600 kWh, reported in 03-UtilityStatement.xml) and the gas of the coating line (line 3, 61200 kWh). The statement thus attributes to this consumption point excise that belongs to other consumption.
- Condition: The energy tax reported in this statement is the share of the excise of invoice 02 that falls on this consumption (412800 kWh of electricity), consistent with the tiers of 02-Invoice.xml, or the report says explicitly that it is the invoice total.
- Options: (a, preferred) report only the excise on this consumption point's 412800 kWh, so that the statements of the same invoice add up to the invoice; (b) leave out the EnergyTaxReport here if the excise cannot be apportioned per consumption point.
- Needs decision: no

### utilities/01#F2 · High · Statement totals ignore the energy tax the statement says is owed
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `2253888`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:TaxInclusiveLineExtensionAmount` = `13523328`
- Why: The Consumption's TaxTotal is "The total of taxes for each tax type covering the consumption", and its LegalMonetaryTotal is "The total amount payable on this consumption, including any allowances, charges, or taxes". Both contain only VAT: 11269440 × 20 % = 2253888, 11269440 + 2253888 = 13523328. The same Consumption says in its EnergyTaxReport that 288840 XUF of excise is owed (balance, nothing paid on account). In invoice 02 the excise is charged on top of the lines and VAT is levied on it too (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140` = 12291300 + 288840). The statement's totals therefore contradict its own energy tax report and the way the invoice charges the excise.
- Condition: The Consumption's TaxTotal covers every tax type reported for the consumption (VAT and excise, each as its own TaxTotal), and its LegalMonetaryTotal and the consumption line's tax-inclusive amount include the excise share and the VAT on it, as invoice 02 charges them.
- Options: (a, preferred) add the excise share (see F1) as its own TaxTotal, compute VAT on line amount plus excise, and adjust the payable amounts; (b) remove the EnergyTaxReport, if the statement is meant to show only the energy price (then the statement no longer explains the excise on the invoice).
- Needs decision: no

### utilities/01#F3 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `11269440`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 405433 kWh.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Amount` = `10876320`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Amount` = `11059230`
- Why: AverageAmount is "The average monetary amount of the consumption". The description gives the three-month average quantity (398400 + 405100 + 412800 = 1216300 kWh / 3 = 405433 kWh, correct). The matching average amount is (10876320 + 11059230 + 11269440) / 3 = 11068330 XUF (equivalently 405433.3 kWh × 27.3). The value given, 11269440, is March's line amount (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `11269440`), not an average.
- Condition: AverageAmount equals the average of the amounts of the same months whose quantities the description averages (11068330 XUF for January to March), or the description and the amount state the same basis.
- Options: (a, preferred) set the average amount to 11068330; (b) if a different basis is meant, state it in the description.
- Needs decision: no

### utilities/01#F4 · Medium · CustomerParty is the receiver, though its definition is "the buyer, if different from the receiver"
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: UBL defines UtilityStatement/CustomerParty as "The buyer, if different from the receiver of the document." Here buyer and receiver are the same party, Valdara Industries, so the condition is not met and the element repeats the receiver. (In 03-UtilityStatement.xml the receiver is Castrano Logistics and the customer Valdara, where the element has its purpose.)
- Condition: CustomerParty is present only when the buyer differs from ReceiverParty.
- Options: (a, preferred) leave CustomerParty out in this statement; (b) none other seen.
- Needs decision: no

### utilities/01#F5 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cbc:Description` = `The supply under the customer's contract.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- Why: UBL defines SubscriberConsumption/Consumption as "The consumption in case the consumption is from one and only one supplier" and SubscriberConsumption/SupplierConsumption as "The consumption in case the consumption is from more than one supplier." This consumption point has one supplier, Ferrano Energy (the only UtilitySupplierParty, and the price includes network charges, so no separate network operator). Both alternatives are present, with the same period and the same totals, so the definitions' conditions are contradicted: SupplierConsumption says there is more than one supplier, Consumption says there is one. The consumption lines (which are only available under SupplierConsumption) are the likely reason for the duplication.
- Condition: The statement uses either Consumption (one supplier) or SupplierConsumption (more than one supplier) according to the number of suppliers of this consumption point, and the two do not repeat the same totals.
- Options: (a) keep SupplierConsumption only if a second supplier (e.g. the grid operator) really bills part of this consumption; (b) keep Consumption only and drop the consumption-line detail; (c) record as a finding on the UBL model that consumption lines are only reachable under the multi-supplier branch. Preference: (c) together with (a) or (b), since the model forces the choice.
- Needs decision: yes

### utilities/01#F6 · Medium · One-time charge type describes a connection charge, though the item is charged monthly
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeType` = `Connection to the 10 kV grid, paid once in 2024`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeTypeCode` = `CONN`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:CurrentChargeTypeCode` = `M`
- Why: OneTimeChargeType is "Information about the one-time payment type in case everything is paid One time". The utility item of this line is the electricity per kWh (`FE-KWH`), charged monthly. Nothing about it is paid one time; the text is about another, past charge (the 2024 grid connection) that neither this statement nor invoice 02 bills. The element's condition is not met, and the value describes something other than the item.
- Condition: OneTimeChargeType and its code are absent, or describe a one-time payment of this utility item.
- Options: (a, preferred) leave both out; (b) if the connection charge matters, mention it in a note of the consumption point.
- Needs decision: no

### utilities/01#F7 · Medium · Province in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative subdivision of the country, which UBL puts in CountrySubentity ("The territorial division of a country, such as a county or state"). The Bayvarran examples of this flow use CountrySubentity for their states. The same value is in Region in 104 examples (`grep -l --include='*.xml' -r '<cbc:Region>Province of'`).
- Condition: Urvanian provinces are given in CountrySubentity (with a CountrySubentityCode where a list exists), not in Region.
- Options: (a, preferred) move the province to CountrySubentity, as for Bayvarran states; (b) keep Region only for a real economic or geographic region.
- Needs decision: no

### utilities/01#F8 · Low · Electricity booked as "Raw materials and parts"
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". Electricity for a factory is an energy or overhead cost, not raw materials and parts; the same code and text appear in Valdara's orders and invoices for goods (e.g. packaging/01-Order.xml, ore/01-Order.xml, counted with `grep -l --include='*.xml' -r 'Raw materials and parts'`: 12 examples). The code 3100 also equals Valdara's ISIC code (`/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3100`), which suggests a copy rather than a cost account. Invoice 02 books its warehouse line to a separate cost centre (`02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`), so the buyer does distinguish cost accounts.
- Condition: The accounting cost of this statement is the buyer's account for energy (or is absent).
- Options: (a, preferred) use Valdara's energy cost account in statement and invoice; (b) leave it out of the statement, which only explains consumption.
- Needs decision: no

### utilities/01#F9 · Low · Meter constant and rated current do not fit a 10 kV connection consuming 412800 kWh a month
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstant` = `40`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:LatestMeterQuantity` = `63280`
- Why: Arithmetic holds: (63280 − 52960) × 40 = 412800 kWh. Physically (own knowledge of metering practice): 412800 kWh in 31 days is an average load of 555 kW. A meter rated 5 A behind a current-transformer ratio of 40 measures a primary of 200 A at most. On a 400 V secondary side that is at most about 140 kW; at 10 kV a meter needs a voltage transformer as well (10 kV/100 V, ratio 100), which would make the meter constant 4000, and the register would then advance about 103 per month, not 10320. A 5 A meter cannot register 10320 kWh a month on its secondary side (about 0.87 kW × 744 h ≈ 640 kWh at most at 100 V). The constant 40 with "Transformer ratio" is therefore implausible for this connection.
- Condition: Meter constant, its type code, the readings and the rated current are physically consistent with the stated 10 kV connection and the monthly consumption.
- Options: (a, preferred) a combined CT/VT constant (e.g. 200/5 × 10000/100 = 4000) with readings that advance accordingly; (b) a low-voltage meter description with a CT ratio sized for about 1 MW peak (e.g. 1500/5 = 300).
- Needs decision: no

### utilities/01#F10 · Low · Receiver data the statement does nothing with, and an order desk as the receiver's contact
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: This statement only explains the factory's electricity consumption. The receiver's logistics service provider (Castrano's warehouse is not this consumption point), the customs trader number and the stock-exchange listing play no part in it and look copied from Valdara's master data. The receiver's contact is the "Order desk" in Sales with the job title "Customer service officer": the party that receives a utility statement deals with energy costs (accounts payable or facility management), not with sales orders.
- Condition: The receiver carries only data this statement uses, and its contact is the one who handles utility bills.
- Options: (a, preferred) drop the service provider, customs trader ID and security listing from this document, and give a contact for utility bills; (b) keep the service provider only if the statement explains the link to 03-UtilityStatement.xml (then say so in a note).
- Needs decision: no

### utilities/01#F11 · Low · Subscriber type of the utility item is a utility type, while the consumption point says "Industrial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `ELEC`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `IND`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text" and SubscriberTypeCode "The code identifying for the service type". The text says subscriber type, the code says service type; the example follows the code's reading and puts the utility type ("Electricity", a code of the UtilityTypeCode list) in both. Under the consumption point the same subscriber is "Industrial" (code IND of the SubscriberTypeCode list). Read by the element names, the same subscriber has two different types in one statement.
- Condition: The subscriber type of the utility item either agrees with the consumption point's subscriber type, or the use of these elements for the service type is recorded as a deliberate reading of UBL's inconsistent definitions.
- Options: (a) record the inconsistency of UBL's definitions (name and text say subscriber type, code definition says service type) as a finding and keep the service-type reading; (b) leave the two elements out of the utility item, since UtilityStatementTypeCode already says electricity. Preference: (a), because the code definition supports the current value.
- Needs decision: yes

### utilities/01#F12 · Low · Filler descriptions
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: A delivery location described as "the consumption point of the statement" says nothing that the consumption point (with ID and address) does not say, and the delivery aggregate adds nothing else. "Earlier month." repeats what the period of each history entry says. These values have no business content (rule "no fillers").
- Condition: Every description carries information not already given by the structured data next to it, or is absent.
- Options: (a, preferred) leave out the delivery location and the history descriptions; (b) give the delivery location the consumption point's ID or address if a delivery is wanted.
- Needs decision: no

## Checked and consistent
- Meter arithmetic: (63280 − 52960) × 40 = 412800 kWh = DeliveredQuantity = TotalDeliveredQuantity (meter and point) = TotalMeteredQuantity = TotalConsumedQuantity = BasicConsumedQuantity = InvoicedQuantity.
- Price and amounts: 412800 × 27.3 = 11269440; VAT 20 % = 2253888; 11269440 + 2253888 = 13523328. History amounts: 398400 × 27.3 = 10876320, 405100 × 27.3 = 11059230. Three-month average quantity 405433 kWh is correct.
- Reference to the parent invoice: FE-INV-26-0313 is 02-Invoice.xml (same supplier, customer, period March 2026, issued the same day before the statement); consumption line 1 matches invoice line 1 (412800 kWh, 11269440 XUF, price 27.3, meter FE-M-881204, VAT S 20 %).
- ConsumptionReportReference for February (405100 kWh, 2026-02-01 to 2026-02-28) agrees with ConsumptionHistory[2]; reading dates 2026-02-28 to 2026-03-31 agree with the period of March.
- Contract FE-C-0047120 is the same in the consumption point, the utility item, SupplierConsumption/Contract and the invoice's PurchaseReference.
- check_ids.py: ISIN XU0001042501 check digit correct.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID`: contract number used as subscriber ID — refuted because the supply contract number is the identifier under which the supplier knows the subscriber at this point (UBL PurchaseReference itself names a "subscription number"), and it is used consistently in all statements of the flow.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[1]/cbc:ValueQualifier`: "Calibrated 2024" as a qualifier of the accuracy class — refuted because ValueQualifier is "An additional value to qualify the value of the meter property", and the calibration year qualifies the stated accuracy class.
- `/UtilityStatement/cbc:IssueTime`: statement issued at 17:54, after the invoice at 13:20 — refuted, a supplement may be issued after its parent on the same day.
- `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD 0990 possibly assigned in the real register — refuted as far as known: ICDs in the 0990 range are not assigned to real schemes as of my knowledge; not verified against the current ISO 6523 RA list.

## Outside this review
- 02-Invoice.xml: the excise tiers look inconsistent in themselves (first tier "The first 50,000 kWh" with TaxableAmount 60000 at 1 XUF/kWh; both tiers at the same per-unit amount 1, so the "industrial rate" is not different; TaxableAmount and TaxAmount equal). Belongs to that example's review.
