# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/03-UtilityStatement.xml`, Git blob `a8d48fa5c4e614ea05c1521143210974ea8bf6f9` (committed)
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


### utilities/03#F1 · High · The estimate correction double-counts February's over-estimate and is applied nowhere
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity` = `117250`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterReadingMethodCode` = `ESTIMATE`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:LatestMeterQuantity` = `135850`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:BasicConsumedQuantity` = `18600`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Quantity` = `17200`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `507780`
- Why: March is billed as the actual reading of 31 March minus February's estimated reading: 135850 − 117250 = 18600 kWh. Redone by the merge: if February's estimate was 750 kWh too high, the true reading on 28 February was 116500, February's real use 16450 and March's 19350 kWh; February billed 17200 (+750) and March billed 18600 (−750), so billing from the estimated reading already settles the error over the two months. A further −750 kWh / −20475 XUF would credit it a second time. The only actual reading is the one of 31 March, which cannot on its own show "as the actual reading shows" how the 35800 kWh since the last actual reading split between the months. And the correction is applied nowhere: the payable amount 609336 = 18600 × 27.3 × 1.2 contains no −20475, and invoice 02 bills line 2 at the full 507780 without allowance or credit. At the same time the history, the referenced February report and the three-month average still use February's 17200 kWh ("Normal", not marked as estimated), and BasicConsumedQuantity ("The basic quantity consumed, excluding additional consumption") shows 18600 where the correction implies 19350. Refutation attempted: the correction could be purely informative (explaining why March looks low); but then it would not carry a CorrectionAmount, and March does not look low (18600 against 17900 and 17200). The broad part rated this Medium because the credit may be implicit; the other three parts High; the merge keeps High (the statement announces a credit that no amount of this statement or of invoice 02 contains).
- Condition: Readings, consumption, correction and amounts tell one story: either March is measured from the estimated reading and no separate credit is stated (the correction element, if kept, says only that this reading settles February's estimate), or the February reading is replaced by a corrected value, March is measured from it (19350 kWh), and the −750 kWh credit appears in the totals here and in invoice 02; history and average agree with the chosen reading.
- Options: (a, preferred) drop the correction (or keep only type, meter and a description that the March reading settles February's estimate, without amount) and say so in MeterReadingComments; mark February's history entry as estimated; (b) base March on a corrected February reading (19350 kWh) and credit −750 kWh in this statement and in invoice 02 (then utilities/02#F7's billing reference gets its purpose), with all arithmetic adjusted.
- Needs decision: yes
- From: money (F2), logistics (F1), context (F1), broad (F6, Medium)

### utilities/03#F2 · High · Correction unit amount × quantity ≠ correction amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Price/cbc:PriceAmount` = `27.3`
- Why: Redone by the merge: 27 × (−750) = −20250, not −20475. The stated amount is −750 × 27.3 (the price per kWh of the statement); the unit amount is that price rounded to whole Ferra and contradicts both the price and the amount.
- Condition: CorrectionUnitAmount × ConsumptionEnergyQuantity = CorrectionAmount, if the correction and the unit amount stay (see F1 and F7).
- Options: (a, preferred) drop CorrectionUnitAmount together with F7 (its definition does not fit) or with F1(a); (b) 27.3 if the element is kept.
- Needs decision: no
- From: broad (F1), money (F1, first half), logistics (F2), context (F2)

### utilities/03#F3 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `507780`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 17900 kWh.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `507780`
- Why: AverageAmount is "The average monetary amount of the consumption". Redone by the merge: (17900 + 17200 + 18600) / 3 = 17900 kWh, right; the amounts (488670 + 469560 + 507780) / 3 = 1466010 / 3 = 488670 XUF. The value 507780 is March's line amount. Same pattern as 01 and 05.
- Condition: AverageAmount is the average of the amounts of the months the description averages (488670 with the current history; different if F1 corrects February).
- Options: (a, preferred) 488670 (or the value after F1); (b) drop AverageAmount and keep only the description.
- Needs decision: no
- From: broad (F2), money (F5), context (F3); logistics (outside its lens)

### utilities/03#F4 · High · The statement's cost centre contradicts the invoice line it explains
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:ParentDocumentLineReferenceID` = `2`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCost` = `Warehouse, Castrano Logistics`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". This statement explains only invoice line 2, the warehouse electricity, which the invoice books to Valdara's cost centre 7100 "Warehouse, Castrano Logistics". The statement gives the invoice header's 3100 "Raw materials and parts" instead, so the two documents give different cost accounts for the same consumption. The statement's receiver, Castrano, has no use for Valdara's cost codes anyway (money).
- Condition: The statement's accounting cost is the one the invoice applies to line 2, or is absent.
- Options: (a) 7100 "Warehouse, Castrano Logistics" (broad, context); (b) leave it out, since the receiver is not the buyer whose accounts these are (money). The merge prefers (b): a statement addressed to Castrano carries no Valdara cost centre.
- Needs decision: no
- From: broad (F3), money (F4), context (F4)

### utilities/03#F5 · High · The warehouse's share of the energy tax is missing; tax and payable amounts differ from the invoice
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `101556`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:TaxInclusiveLineExtensionAmount` = `609336`
- XPath: `02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`
- XPath: `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- Why: The Consumption's TaxTotal is "The total of taxes for each tax type covering the consumption" and its LegalMonetaryTotal "The total amount payable on this consumption, including any allowances, charges, or taxes". Both contain only VAT (507780 × 20 % = 101556; 609336). Invoice 02's excise works out only with this meter's 18600 kWh included (50000 × 1.2 + (412800 + 18600 − 50000) × 0.6 = 288840, recalculated by the merge) and the invoice levies VAT on it. With these 18600 kWh in the upper tier the warehouse's excise is 11160 and the amount payable (507780 + 11160) × 1.2 = 622728 (pro rata 288840 × 18600 / 431400 ≈ 12454). The statement has no EnergyTaxReport, while statement 01 reports the excise of both meters. The broad part rated this Medium because the invoice does not apportion the excise per line; the merge follows money (High): whatever the apportionment, some excise falls on these kWh, and the statement's payable amount contains none, which contradicts the invoice it explains.
- Condition: The statement reports this point's energy tax, and its tax and payable amounts include it and the VAT on it, consistent with invoice 02 and statement 01; or the statement says that the excise is charged at invoice level only and its totals say what they leave out.
- Options: (a, preferred) an EnergyTaxReport with the warehouse's share (11160 under the tier reading) and corrected totals, together with utilities/01#F1–F2; (b) a note in both statements that the energy tax is assessed per customer on the invoice as a whole (broad's preference, since tiers on the month's total cannot be split without an allocation rule), still carrying the VAT on it where the payable amounts claim to include taxes.
- Needs decision: no
- From: money (F3), broad (F5, Medium); logistics and context (noted outside their findings)

### utilities/03#F6 · High · Castrano Logistics named as subscriber of a subscription that is Valdara's
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cbc:Description` = `The supply under the customer's contract.`
- XPath: `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: SubscriberParty is "The Party that is the subscriber of the utility" (in SubscriberConsumption "The Party who is subscribed to the utility"), and SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point". The ID is Valdara's supply contract FE-C-0047120, the supply is "under the customer's contract" with Valdara as UtilityCustomerParty, and invoice 02 bills this consumption to Valdara. In `01-UtilityStatement.xml` the same subscriber ID belongs to Valdara as subscriber. One subscriber ID thus names two different subscribers in the flow, and within this statement the subscriber party contradicts the subscriber ID and the utility customer. Castrano is the occupant of the warehouse, not the party subscribed. Severity: parties High, the other three parts Medium; the merge takes High, since the statement contradicts statement 01 on who the subscriber with this ID is (section 6).
- Condition: The subscriber of the warehouse point is the same party in the subscriber elements, the subscriber ID, the utility customer and statement 01; Castrano appears only in roles that fit it (receiver, occupant of the point).
- Options: (a, preferred) Valdara as SubscriberParty (both places), Castrano as receiver, with the consumption point's description naming Castrano's warehouse; (b) Castrano with its own subscription (own subscriber ID or sub-contract), which changes invoice 02's line 2 and the utility customer.
- Needs decision: yes
- From: parties (F1), broad (F4, Medium), logistics (F3, Medium), context (F6, Medium)

### utilities/03#F7 · Medium · District-heating correction elements used for an electricity estimate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: The aggregate is general, but these children are defined for district heating (checked in the model by the merge): CorrectionUnitAmount "Correction per MWH per degree C.", ConsumptionEnergyQuantity "Your consumpt for district heating energy.", CorrectionAmount "Your correction for heating correction." Here they carry a price per kWh, an electricity quantity and an electricity credit for an estimate, with no temperature involved.
- Condition: The correction elements, if kept, are used with the meaning their definitions give; an electricity estimate correction is expressed with elements that fit (CorrectionType/Code, MeterNumber, Description, MeterReadingComments, an allowance on the consumption line) or left out (F1).
- Options: (a, preferred) remove the three elements (or the aggregate) together with F1(a); (b) move quantity and amount to an allowance of the consumption line; (c) record the narrowness of the UBL definitions for the TC.
- Needs decision: no
- From: logistics (F4), context (F5), money (F1, second half)

### utilities/03#F8 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- Why: SubscriberConsumption/Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "The consumption in case the consumption is from more than one supplier". Both are present with identical totals for one supplier, Ferrano Energy. Same as utilities/01#F5.
- Condition: Only the alternative that matches the number of suppliers is used.
- Options: (a) Consumption only (coverage loss); (b) SupplierConsumption only with a real second supplier (story); (c) record for the TC that consumption lines are only reachable under SupplierConsumption. Preference: (c) with (a) or (b).
- Needs decision: yes
- From: broad (F7), context (F7)

### utilities/03#F9 · Medium · Province in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity). The Bayvarran addresses use CountrySubentity. 219 occurrences in 104 files (recount over `*.xml`).
- Condition: Urvanian provinces are in CountrySubentity (with a code where the world has a list).
- Options: (a, preferred) CountrySubentity; (b) Region only if the story makes the province an economic or geographic region.
- Needs decision: no
- From: broad (F8), parties (F2)

### utilities/03#F10 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`
- Why: Apart from whose ID it is (F6), SubscriberID identifies a subscriber but holds the supply contract's number. Whether the world's subscription number is the contract number cannot be settled (the broad part refuted the same question in 01: a contract number can serve as subscription number). Same as utilities/01#F12.
- Condition: SubscriberID holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a, preferred) a customer number of the subscriber at Ferrano Energy; (b) drop SubscriberID; (c) record the convention.
- Needs decision: yes
- From: parties (F6), context (F6, last sentence)

### utilities/03#F11 · Low · SubscriberType on the utility item names the utility, the consumption point says "Commercial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Electricity`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `ELEC`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Commercial`
- Why: Under UtilityItem the text is "Identification of the subscriber type, expressed as text" and the code "The code identifying for the service type"; UBL's two definitions disagree. "Electricity" fits only the code's; the same subscriber is "Commercial" at the consumption point. Same as utilities/01#F13.
- Condition: Text and code describe the same thing and fit their definitions, or the reading is recorded as a TC finding.
- Options: (a) record the UBL inconsistency and keep the service-type reading; (b) drop the text and keep the code; (c) the subscriber type in both.
- Needs decision: yes
- From: broad (F10), context (F8)

### utilities/03#F12 · Low · Customer master data the statement does nothing with
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Valdara's customs trader number and share listing play no part in a statement of warehouse electricity; they are part of the block repeated in all 75 examples with Valdara's full data (in 01 the CustomerParty has only ID and name). The context part also listed Castrano's ShareholderParty and Valdara's ServiceProviderParty; the parties part showed that both explain why the warehouse runs on Valdara's contract and why the statement goes to Castrano, so the merge leaves them out of this finding.
- Condition: The customer carries only data this statement uses (e.g. identification and name, as in 01).
- Options: (a, preferred) reduce CustomerParty to identification and name; (b) keep the data only with a stated reason.
- Needs decision: no
- From: broad (F9, part), parties (F5), context (F9, part)

### utilities/03#F13 · Low · Contacts of the receiver and the customer do not fit their roles
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Castrano's contact is the "Warehouse office" with the job title of a customer service officer in Sales: name, title and department disagree, and Sales is not the receiver of a statement of the warehouse's electricity. Valdara, the buyer of the supply, is reachable only through its sales order desk. Both contacts are identical in every example with the parties' full data (Castrano 7, Valdara 75; parties part).
- Condition: Each contact's name, job title and department agree, and the function fits the party's role here.
- Options: (a, preferred) a fitting title and department for Castrano's warehouse office (e.g. warehouse manager, Operations) and a utilities purchasing or accounts payable contact for Valdara; (b) drop job title and department where only the functional name is meant.
- Needs decision: no
- From: broad (F9, part), parties (F4), context (F9, part)

### utilities/03#F14 · Low · Castrano's registration date is the date shared by 25 companies of the world
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". 25 companies of the world are registered on 1 January 1996, while every other date is used by one company only (parties part); recounted by the merge: 271 occurrences in 181 files (`grep -rh`/`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01'`). It looks like a default value. Same decision as in the earlier flows' merges.
- Condition: Castrano's registration date is a date from its own history, consistent in every example, or a 1996 (re-)registration is recorded in the story.
- Options: (a, preferred) a date of its own; (b) record the 1996 event in the story; (c) drop the date where unused.
- Needs decision: yes
- From: parties (F3)

### utilities/03#F15 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: The delivery location only points back to the consumption point FE-CP-4160-07 that the statement already identifies; "Earlier month." repeats the Period. No fillers (IND5). February's description could carry real information here: that it was an estimate (broad).
- Condition: Each description carries information of its own, or is absent (the Delivery aggregate goes if it has nothing else).
- Options: (a, preferred) drop the delivery location and January's description; describe February's entry as estimated; (b) give the location the consumption point's ID.
- Needs decision: no
- From: broad (F11), logistics (F5), context (F10)

### utilities/03#F16 · Low · Italian text tagged as English (street and legal form)
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Corso della Repubblica`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Added by the merge for alignment with utilities/01#F16 and the wood, plastics and rail merges. The renderings are tagged en-XU but are Italian; proper names may keep their form (parties' argument in 01), but the legal form is a description and no convention is recorded. Cannot be settled.
- Condition: Either the convention is recorded in the world's story, or the en-XU renderings are English.
- Options: (a, preferred) record the convention for proper names and render legal forms in English; (b) English renderings throughout.
- Needs decision: yes
- From: merge

## Checked and consistent
- Meter: (135850 − 117250) × 1 (DIRECT) = 18600 kWh = DeliveredQuantity = TotalMeteredQuantity = TotalConsumedQuantity = InvoicedQuantity = invoice 02 line 2 (meter FE-M-881377 in its PurchaseReference).
- Physics: 18600 kWh in 744 h = 25 kW average, about 36 A per phase at 400 V; a direct-connected meter with basic current 5 A (maximum typically 60–100 A) carries it (own knowledge).
- Amounts: 18600 × 27.3 = 507780; VAT 101556; 609336 (internal arithmetic; F5 is about what is missing). History 17900 × 27.3 = 488670, 17200 × 27.3 = 469560; ConsumptionReportReference February 17200 kWh agrees with ConsumptionHistory[2].
- Reading methods: previous estimated ("no access to the meter"), latest manual, comment agrees; dates before the issue date.
- Parent FE-INV-26-0313 is `02-Invoice.xml` (13:20, before this statement at 17:10); ParentDocumentLineReferenceID 2 is the warehouse line.
- CustomerParty Valdara differs from ReceiverParty Castrano, so its condition is met here. Castrano is described identically in its 7 examples (SRU, SMALL, 100 % owned by Valdara, ISIC 5210, Via del Magazzino 24, 4130 Ferrano); the consumption point address equals it.
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/UtilityStatement/cbc:IssueTime`: FE-DOC-26-0315 issued at 17:10, before FE-DOC-26-0314 at 17:54 — refuted by broad (numbers may be allocated before issue). The merge keeps the logistics part's Low finding for the pair in utilities/01#F15 (from broad).
- `/UtilityStatement/cbc:Note[1]`: note in Urvanian to the receiver — refuted, Castrano's language is Urvanian (from broad).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty`: Valdara as utility customer while Castrano is subscriber, money effect — consistent with the invoice, which bills Valdara (from money; the role conflict is F6).
- `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: SMALL as a default — refuted, a single-site warehousing subsidiary is plausibly small (from parties).
- `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:ShareholderParty/cac:Party/cac:PartyName/cbc:Name`: unrelated master data — refuted, the ownership explains why the subsidiary's warehouse is supplied under the parent's contract (from parties; context's contrary view corrected in F12).
- `/UtilityStatement/cac:CustomerParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name`: copied master data — refuted with its service provider, which explains the arrangement (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterProperty[2]/cbc:ValueQuantity`: 5 A too small for a direct meter — refuted, a normal basic current (5(60) A) (from logistics).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID`: point ID with 4160 while the postal zone is 4130 — refuted, nothing requires the ID to encode the postal zone (from logistics).
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:MeterReadingComments`: duplicates the method code — refuted, it explains the estimate (from context).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty`: subscriber given twice — refuted, different scopes in UBL (from context).

## Changed in the merge
- broad/F6 (Medium) → F1 High: grouped with money/F2, logistics/F1, context/F1 (same condition); High as in three parts.
- money/F1 → F2 and F7: arithmetic (High) and the district-heating definitions (Medium) split, as logistics and context had them.
- broad/F5 (Medium) → F5 High: some excise falls on these kWh whatever the apportionment; options from both parts kept.
- broad/F4, logistics/F3, context/F6 (Medium) → F6 High: the statement contradicts 01 on the subscriber of the same ID (section 6); parties' High kept.
- context/F6 (last sentence) and parties/F6 → F10: the generic contract-number question split from the subscriber conflict, Low with Needs decision: yes as in 01.
- broad/F9 and context/F9 → F12 and F13: master data and contacts split; ShareholderParty and ServiceProviderParty XPaths of context/F9 dropped (refuted by parties).
- F4: preference set to option (b) (money) with the reason.
- F16 added for alignment.

## Outside this review
- `01-UtilityStatement.xml` reports the whole invoice's excise for its one consumption point (utilities/01#F1).
