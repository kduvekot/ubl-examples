# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/01-UtilityStatement.xml`, Git blob `5afddf1d0c8c1838c6abd6e06e483af49cb2664f` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/01#F1 · High · Energy tax report carries the excise of the whole invoice, not of this consumption point
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `412800`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- Why: The EnergyTaxReport ("A tax on the consumption of energy or water") sits in the Consumption of the one consumption point of this statement, the factory main connection FE-CP-4120-01 with 412800 kWh, which is invoice line 1. It states 288840 XUF, which is exactly the excise of the whole invoice 02. Recalculated by the merge from the invoice's tiers: the amounts only work out for the invoice's electricity of both meters, 412800 + 18600 = 431400 kWh: 50000 kWh × 1.2 = 60000 and (431400 − 50000) = 381400 kWh × 0.6 = 228840, total 288840. It therefore includes the excise on the 18600 kWh of the Castrano warehouse meter, which `03-UtilityStatement.xml` reports as a separate consumption point (and which carries no EnergyTaxReport). For the factory's 412800 kWh alone the same tiers give at most 50000 × 1.2 + 362800 × 0.6 = 277680 (if the first tier is assigned to the factory; pro rata it would be 288840 × 412800 / 431400 ≈ 276387). Any reading gives less than 288840 for this point. The rates 1.2 and 0.6 are derived; the invoice itself states 1 XUF/kWh for both tiers (utilities/02#F1). Refutation attempted: if the world's excise is assessed per customer, a per-point report cannot hold the full customer amount either, since it sits under this point's consumption. The finding stands.
- Condition: The energy tax reported in this statement is the share of the excise of invoice 02 that falls on this consumption point's 412800 kWh, consistent with the tiers of `02-Invoice.xml`, and the energy tax reported in statements 01 and 03 adds up to the invoice's excise; or the report says explicitly that it is the invoice total.
- Options: (a, preferred) report this point's share (e.g. 277680, with the tier split stated) here and the warehouse's share in 03, so that the statements of the same invoice add up to the invoice; (b) state explicitly that the amount is the customer's total for both points (a report then still sits under the wrong consumption point); (c) leave out the EnergyTaxReport if the excise cannot be apportioned per consumption point.
- Needs decision: no
- From: broad (F1), money (F1, first half), logistics (F1), context (F2, first half)

### utilities/01#F2 · High · Statement totals leave out the energy tax the statement says is owed, and the VAT on it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `2253888`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:TaxInclusiveLineExtensionAmount` = `13523328`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140`
- Why: The Consumption's TaxTotal is "The total of taxes for each tax type covering the consumption", and its LegalMonetaryTotal is "The total amount payable on this consumption, including any allowances, charges, or taxes". Both contain only VAT on the energy price: 11269440 × 20 % = 2253888, 11269440 + 2253888 = 13523328. The same Consumption says in its EnergyTaxReport that 288840 XUF of excise is owed (nothing on account). Invoice 02 charges the excise on top of the lines and levies VAT on it (VAT base 12580140 = 12291300 + 288840). Checked by the merge: the electricity part of the invoice is (11269440 + 507780 + 288840) × 1.2 = 14479272 (= 15096168 − 514080 × 1.2 for the gas); statements 01 and 03 together show 13523328 + 609336 = 14132664; the difference 346608 is exactly 1.2 × 288840. The totals contradict the statement's own energy tax report and the way the invoice it explains charges the excise.
- Condition: The Consumption's TaxTotal covers every tax type of the consumption (VAT and excise, each as its own TaxTotal), and the PayableAmounts and the line's TaxInclusiveLineExtensionAmount include this point's excise share and the VAT on it, so that statements 01 and 03 together add up to the electricity part of invoice 02.
- Options: (a, preferred) add the excise share (F1) as its own TaxTotal, compute VAT on line amount plus excise, and adjust the payable amounts; (b) remove the EnergyTaxReport and say the statement shows only the energy price (it then no longer explains the excise of the bill its note says it explains).
- Needs decision: no
- From: broad (F2), money (F1, second half), context (F2, second half); logistics (outside its lens)

### utilities/01#F3 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `11269440`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 405433 kWh.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Amount` = `10876320`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Amount` = `11059230`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `11269440`
- Why: AverageAmount is "The average monetary amount of the consumption". The description gives the three-month average quantity, (398400 + 405100 + 412800) / 3 = 405433.3 kWh, which is right. Redone by the merge: the amount over the same three months is (10876320 + 11059230 + 11269440) / 3 = 33204990 / 3 = 11068330 XUF (= 405433.3 × 27.3). The value 11269440 is March's line amount alone. Refutation attempted: no other averaging window (e.g. a single month) is stated anywhere in the statement, so the amount contradicts both the description and the history. The same pattern occurs in 03 and 05.
- Condition: AverageAmount equals the average of the amounts of the months whose quantities the description averages (11068330 XUF, net of tax like the history amounts), or the description states another basis that the amount matches.
- Options: (a, preferred) set AverageAmount to 11068330; (b) state in the description what the amount averages; (c) drop AverageAmount and keep only the description.
- Needs decision: no
- From: broad (F3), money (F2), context (F1); logistics (outside its lens)

### utilities/01#F4 · Medium · CustomerParty repeats the receiver, though its definition is "the buyer, if different from the receiver"
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: UBL defines UtilityStatement/CustomerParty as "The buyer, if different from the receiver of the document." Buyer and receiver are the same party, Valdara Industries, so the condition is not met. In `03-UtilityStatement.xml` the receiver is Castrano Logistics and the customer Valdara, where the element has its purpose. The same pattern (customer = receiver) occurs in 05, 08 and 12 of this flow.
- Condition: CustomerParty is present only when the buyer differs from ReceiverParty.
- Options: (a, preferred) leave CustomerParty out of this statement; (b) keep it only if the story gives the statement a receiver other than Valdara.
- Needs decision: no
- From: broad (F4), parties (F2), context (F4)

### utilities/01#F5 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cbc:Description` = `The supply under the customer's contract.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- Why: UBL defines SubscriberConsumption/Consumption as "The consumption in case the consumption is from one and only one supplier" and SubscriberConsumption/SupplierConsumption as "The consumption in case the consumption is from more than one supplier." This point has one supplier, Ferrano Energy (the only UtilitySupplierParty; the price includes network charges, so no separate network operator bills). Both alternatives are present with the same period and totals, so one says one supplier and the other more than one. The consumption lines, which UBL only offers under SupplierConsumption, are the likely reason. The money part's reading (two alternative views, not double counting) is carried under "Considered and refuted"; it does not resolve the conflict of the two definitions' conditions.
- Condition: The statement uses Consumption (one supplier) or SupplierConsumption (more than one supplier) according to the number of suppliers of this consumption point, and the two do not repeat the same totals.
- Options: (a) keep SupplierConsumption only if a second supplier (e.g. a grid operator billing network charges) really bills part of this consumption (changes the story); (b, preferred by context) keep Consumption only and drop the line-level detail, accepting the loss of coverage; (c) record for the TC that consumption lines are only reachable under the multi-supplier branch. Preference: (c) together with (a) or (b), since the model forces the choice.
- Needs decision: yes
- From: broad (F5), context (F3)

### utilities/01#F6 · Medium · One-time charge type describes a past connection charge, though the item is charged monthly
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeType` = `Connection to the 10 kV grid, paid once in 2024`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeTypeCode` = `CONN`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:CurrentChargeTypeCode` = `M`
- Why: OneTimeChargeType is "Information about the one-time payment type in case everything is paid One time". The utility item of this line is electricity per kWh (`FE-KWH`), charged monthly (CurrentChargeType `Monthly`, code M). Nothing about it is paid one time; the text describes another, past charge (the 2024 grid connection) that neither this statement nor invoice 02 bills. The element's condition is not met.
- Condition: OneTimeChargeType and its code are absent, or describe a one-time payment of this utility item.
- Options: (a, preferred) leave both out; (b) if the connection charge matters, mention it in a note of the consumption point or the contract, or bill it as its own item where an invoice charges it.
- Needs decision: no
- From: broad (F6), money (F3), context (F5), logistics (F6, Low)

### utilities/01#F7 · Medium · Province in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division of the country, which UBL puts in CountrySubentity. The Bayvarran addresses of the world use CountrySubentity for their states (`Coastal State`, `XB-CO`). Recounted by the merge: 219 occurrences of `<cbc:Region>Province of` in 104 files (`grep -rho --include='*.xml'` and `grep -rl --include='*.xml'` over `world/examples`).
- Condition: Urvanian provinces are given in CountrySubentity (with a CountrySubentityCode where the world has a list), not in Region.
- Options: (a, preferred) move the province to CountrySubentity, as for Bayvarran states; (b) keep Region only if the story makes the province an economic or geographic region.
- Needs decision: no
- From: broad (F7), parties (F1)

### utilities/01#F8 · Low · Electricity booked as "Raw materials and parts"
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3100`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". Electricity for a factory is an energy or overhead cost, not raw materials and parts. The same text occurs in 12 files (`grep -rl --include='*.xml' 'Raw materials and parts' world/examples | wc -l`, recounted), mostly Valdara's orders and invoices for goods, where it fits. The code 3100 also equals Valdara's ISIC class, and invoice 02 books its warehouse line to a separate cost centre, so the buyer does distinguish cost accounts. It looks copied from master data.
- Condition: The accounting cost of this statement is the buyer's account for energy (the same as in invoice 02), or is absent.
- Options: (a, preferred) Valdara's energy or factory-overhead cost account in 01, 02 and 03 alike; (b) leave it out of the statement, which only explains consumption.
- Needs decision: no
- From: broad (F8), money (F4), context (F8)

### utilities/01#F9 · Low · Meter constant and rated current do not fit a 10 kV connection consuming 412800 kWh a month
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstant` = `40`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstantCode` = `CTRATIO`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:Description` = `Factory, main connection at 10 kV`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:LatestMeterQuantity` = `63280`
- Why: (Own knowledge of metering practice.) The arithmetic holds: (63280 − 52960) × 40 = 412800 kWh. Redone by the merge: 412800 kWh in March (744 h) is an average load of 555 kW. Metered at 10 kV, the primary current is 555000 / (√3 × 10000) ≈ 32 A, which fits a 200/5 A current transformer (ratio 40, 5 A secondary as in the rated-current property), but a 10 kV meter also needs a voltage transformer (typically 10000/100 V, ratio 100), so the constant would be the product, e.g. 4000, and the register would advance by about 103, not 10320. Metered at 400 V behind the factory's own transformer, the average current is about 800 A, four times what a 200/5 A transformer carries. A CT ratio of 40 alone fits neither case.
- Condition: Meter constant, its type code, the readings and the rated current are consistent with the stated 10 kV connection and the monthly consumption: register advance × constant = 412800 kWh with a constant a meter at that voltage level would have.
- Options: (a, preferred) a combined CT × VT constant (e.g. 200/5 × 10000/100 = 4000; the context part suggested 1000 for another CT ratio), with a type code for it if the world's list has one, and readings that advance accordingly; (b) a low-voltage meter with a CT ratio sized for the load (e.g. 1500/5 = 300) and the connection described accordingly.
- Needs decision: no
- From: broad (F9), logistics (F4), context (F11)

### utilities/01#F10 · Low · Receiver's master data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: This statement explains the factory's electricity consumption. Valdara's customs trader number, its share listing on the Ferrano Stock Exchange and its warehousing service provider (Castrano Logistics, "Warehousing and despatch") play no part in it; Castrano's warehouse is not this consumption point. The block is identical in all 75 examples with Valdara's full data (parties part), so it is copied master data (section 4.8).
- Condition: Every identifier, listing and service provider in the receiver party has a use in this statement, or is absent.
- Options: (a, preferred) drop the customs trader ID, the security listing and the service provider from this document; (b) keep the service provider only if the statement explains the link to `03-UtilityStatement.xml` (then say so in a note).
- Needs decision: no
- From: broad (F10, first half), parties (F3), context (F9, first half)

### utilities/01#F11 · Low · Receiver's contact is the order desk in Sales, not someone who handles an electricity statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The receiver of a utility statement deals with energy costs (accounts payable, facility or energy management). Valdara's contact is its own sales order desk with a customer service officer, the contact Valdara gives its own customers, the same whatever role Valdara has (section 6: a contact that does not fit the role, Low).
- Condition: The receiver's contact is a function that deals with the energy supply or its bills, and name, job title and department agree.
- Options: (a, preferred) a contact for utilities purchasing or accounts payable; (b) drop the contact if the electronic address is meant to be the only channel.
- Needs decision: no
- From: broad (F10, second half), parties (F4), context (F9, second half)

### utilities/01#F12 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`
- Why: SubscriberID under UtilityConsumptionPoint is "An identifier for the subscriber responsible for the consumption at this consumption point", and under UtilityItem "An identifier for the subscriber to the utility": it identifies a party. The value is the supply contract's ID, which the statement also gives as Contract/ID, so an identifier of one kind is used as another (logistics, context, parties). Against it (broad, which refuted it): the supply contract number is the identifier under which the supplier knows the subscriber at this point, and UBL's PurchaseReference itself names a "subscription number". Whether the world's subscription number is the contract number cannot be settled from the examples, so the merge keeps it Low with Needs decision: yes. The same pattern occurs in all five utility statements of the flow (01, 03, 05, 08, 12; logistics part).
- Condition: SubscriberID holds an identifier of the subscriber (e.g. Ferrano Energy's customer number for Valdara), or the world states that the contract number is the subscriber number.
- Options: (a, preferred) give the subscriber a customer number of its own and use it in both places, keeping the contract in Contract/ID; (b) drop SubscriberID where only the contract identifies the subscription; (c) record that the contract number serves as the subscriber number in this world.
- Needs decision: yes
- From: parties (F5), logistics (F3), context (F6, Medium); broad refuted it

### utilities/01#F13 · Low · Subscriber type of the utility item is a utility type, while the consumption point says "Industrial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `ELEC`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Industrial`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text", while SubscriberTypeCode is "The code identifying for the service type". The two definitions of the pair disagree in UBL itself. The example follows the code's reading and puts the utility type (code ELEC of the UtilityTypeCode list) in both; read by the element names, the same subscriber has two types in one statement ("Industrial" at the consumption point). The parties and logistics parts refuted it on the code's definition; the text element's definition is not met by "Electricity", so the question stays open.
- Condition: Text and code on the utility item describe the same thing and fit their definitions, or the use of these elements for the service type is recorded as a deliberate reading of UBL's inconsistent definitions (TC finding).
- Options: (a) record the inconsistency for the TC and keep the service-type reading (broad's preference); (b) drop the text SubscriberType and keep the code as service type (context's preference); (c) use the subscriber type (Industrial) in both, with a subscriber-type list.
- Needs decision: yes
- From: broad (F11), context (F7); parties and logistics refuted it

### utilities/01#F14 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: The delivery location carries no identifier or address, only a sentence saying that it is the consumption point, which the statement already identifies (FE-CP-4120-01, with address); the Delivery aggregate adds nothing else. "Earlier month." repeats what each history entry's Period says. No business content (no fillers, IND5). The delivery sentence occurs in five examples (01, 03, 05, 08, 12; logistics part).
- Condition: Every description carries information the structured data next to it does not, or is absent (the Delivery aggregate goes if it has nothing else).
- Options: (a, preferred) leave out the Delivery aggregate and the history descriptions; (b) give the delivery location the consumption point's ID if a delivery is wanted.
- Needs decision: no
- From: broad (F12), logistics (F5), context (F10)

### utilities/01#F15 · Low · Statement numbers out of order with their issue times
- XPath: `/UtilityStatement/cbc:ID` = `FE-DOC-26-0314`
- XPath: `/UtilityStatement/cbc:IssueTime` = `17:54:00`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cbc:ID` = `FE-DOC-26-0315`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cbc:IssueTime` = `17:10:00`
- Why: Both statements were issued by Ferrano Energy on 2026-04-02 for the same invoice; the lower number 0314 was issued 44 minutes after the higher 0315. A sender's sequential numbering normally follows issue order. Refutation attempted: numbers can be reserved at generation and issued later; the order is only implausible, hence Low.
- Condition: Within one sender and day, document number order matches issue time order.
- Options: swap the issue times (or the numbers) of 01 and 03.
- Needs decision: no
- From: logistics (F2)

### utilities/01#F16 · Low · Italian text tagged as English (street and legal form)
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Added by the merge from a candidate the parties part refuted, to align with the merges of the wood, plastics and rail flows. The renderings are tagged `en-XU` but are Italian. Parties' argument: street and city names are proper names, and the world uses these Italianate forms as the English names of Urvanian places in every example; the legal form is its proper name with an English gloss. Against it: a legal form like "Società urvaniana per azioni" is a description, not a proper name, and no convention is recorded. The merge cannot settle it. Recounted: 217 en-XU/en-XB renderings starting Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina in 102 files, 112 `Società…` legal forms tagged en-XU/en-XB (`grep -rhE --include='*.xml'` over `world/examples`).
- Condition: Either the convention (Italianate English names of Urvanian places and legal forms) is recorded in the world's story, or the en-XU renderings are English.
- Options: (a, preferred) record the convention for proper names, and give the legal form an English rendering; (b) English renderings throughout.
- Needs decision: yes
- From: merge (from parties' "Considered and refuted")

## Checked and consistent
- Meter arithmetic: (63280 − 52960) × 40 = 412800 kWh = DeliveredQuantity = TotalDeliveredQuantity (meter and point) = TotalMeteredQuantity = TotalConsumedQuantity = BasicConsumedQuantity = InvoicedQuantity of `02-Invoice.xml` line 1.
- Price and amounts: 412800 × 27.3 = 11269440; VAT 20 % = 2253888; sum 13523328 (internal arithmetic right; F2 is about what it leaves out). History: 398400 × 27.3 = 10876320, 405100 × 27.3 = 11059230. Three-month average quantity 405433 kWh is right.
- Parent invoice FE-INV-26-0313 is `02-Invoice.xml` (same supplier and customer, March 2026, issued 13:20 before this statement at 17:54); consumption line 1 matches invoice line 1 (412800 kWh, 11269440 XUF, price 27.3, meter FE-M-881204, VAT S 20 %).
- ConsumptionReportReference for February (405100 kWh) agrees with ConsumptionHistory[2]; reading dates 2026-02-28 and 2026-03-31 enclose March and precede the issue date.
- Contract FE-C-0047120 is the same in the consumption point, the utility item, SupplierConsumption/Contract and the invoice's PurchaseReference.
- EnergyTaxReport: 288840 − 0 on account = 288840 balance (internally consistent; F1 is about the amount).
- Ferrano Energy and Valdara Industries are described identically in 01–04 and in other examples with their full data; industry codes 3510 and 3100 from ISIC Rev.4; legal forms and sizes plausible.
- check_ids.py: ISIN XU0001042501 check digit correct; market code XFER not in the ISO 10383 MIC source.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID`: contract number used as subscriber ID — refuted by broad (subscription number, consistently used). The merge disagrees with the refutation as conclusive: kept as F12, Low, Needs decision: yes (from broad).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[1]/cbc:ValueQualifier`: "Calibrated 2024" as a qualifier of the accuracy class — refuted because ValueQualifier is "An additional value to qualify the value of the meter property", and the calibration year qualifies the stated class (from broad).
- `/UtilityStatement/cbc:IssueTime`: statement issued at 17:54, after the invoice at 13:20 — refuted, a supplement may be issued after its parent on the same day (from broad).
- `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD 0990 possibly assigned in the real register — refuted as far as known: ICDs have not reached the 0990 range; not verified against the current RA list (from broad, parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal`: tax total without subtotal or scheme — refuted as a separate finding: its amount is identifiable as VAT; the missing excise is F2 (from money).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: the same totals in Consumption and SupplierConsumption as double counting — refuted by money: UBL offers them as alternative views. The merge carries this argument; the conflict of the definitions' conditions remains F5 (from money).
- `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`, `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]`: Italian text under en-XU — refuted by parties as proper names. The merge disagrees for alignment with earlier flows: made F16, Low, Needs decision: yes (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode`: utility type in a subscriber-type code — refuted by parties and logistics on the code's definition ("service type"). The merge keeps F13 (broad, context), since the text element's definition is not met (from parties, logistics).
- `/UtilityStatement/cac:SenderParty/cac:Contact/cbc:Name`: the sender's contact "Customer service" fits the role of answering questions on the statement (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity`: 52960 × 40 = 2.12 GWh cumulative looks small since 2024 — refuted because a five-digit register rolls over and the meter may have been replaced at its 2024 calibration (from logistics).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ID`: same value as ConsumptionID — refuted, both identify this month's specification of the same point (from logistics).
- `/UtilityStatement/cac:SubscriberParty`: the subscriber equals the receiver — refuted, SubscriberParty has no "if different" condition (from context).
- `/UtilityStatement/cac:SubscriberConsumption/cbc:Note`: repeats the consumption point description — refuted, a legitimate heading of the specification (from context).
- `/UtilityStatement/cac:SubscriberConsumption/cbc:SpecificationTypeCode`: DETAILED for a monthly statement — refuted, a detailed monthly specification is a type of the kind the definition names (from context).
- `/UtilityStatement/cac:AdditionalDocumentReference`: tariff referenced only by ID — refuted, DocumentTypeCode TARIFF and the description say what it is (from context).

## Changed in the merge
- money/F1 and context/F2 → F1 and F2: split into the excise amount (F1) and the totals that omit it (F2), as broad had them, because the elements and conditions differ.
- broad/F10 and context/F9 → F10 and F11: master data and the contact split into two findings, as the parties part had them and as the earlier flows' merges do.
- logistics/F6 (Low) → F6 Medium: three parts gave Medium; the element's condition ("in case everything is paid One time") is not met, a meaning other than the definition (section 6 Medium).
- context/F6 (Medium, no), logistics/F3 (Low, no), parties/F5 (Low, yes) → F12 Low, Needs decision: yes: broad refuted it with a defensible reading (contract = subscription number); the merge cannot settle it.
- F1: wording extended with the pro-rata alternative and option (c) from context.
- F9: options combined from broad (4000), context (1000) and logistics.
- F16 added from parties' refuted candidates, aligned with the wood, plastics and rail merges.

## Outside this review
- `02-Invoice.xml`: excise per-unit amounts of 1 XUF/kWh against amounts implying 1.2 and 0.6 (broad, context): a finding of utilities/02 (F1 there).
