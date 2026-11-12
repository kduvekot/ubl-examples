# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8991d4f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/12#F1 · High · Allowance of 2.40 on a call whose base amount and price are 0
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallBaseAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:Price/cbc:PriceAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:Amount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:BaseAmount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- Why: The 12-minute call to Bayvarra has a base amount ("The amount to be payed as the base for one call") of 0 and a price of 0, yet carries an allowance of 2.40 whose base amount is 2.40, and the amount to be paid ("The amount to be payed for the call") is 0. Either the call's base was 2.40 and the allowance brings it to 0 (then CallBaseAmount and price are wrong), or the base is 0 and the allowance reduces nothing (then the allowance is wrong); 0 − 2.40 ≠ 0. The allowance also has no multiplier, so BaseAmount ("to which the multiplier factor is applied") has nothing to be applied to.
- Condition: CallBaseAmount (or price × quantity) − allowance = CallExtensionAmount for the call.
- Options: (a, preferred) price 0.20 per minute, CallBaseAmount 2.400, allowance 2.400 (base amount only with a multiplier), extension 0.000, which shows the waived charge; (b) drop the allowance and keep the call at 0 with the reason in a note.
- Needs decision: no

### utilities/12#F2 · High · Tax-inclusive line amounts ignore the lines' own discount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:LineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: TaxInclusiveLineExtensionAmount is, for the supply line, "The total amount for this telecommunications supply line, including all allowances, charges and taxes", and for the consumption line "The total amount for this consumption line, including all allowances, charges and taxes". Each business line has a 5 % discount of 1.059 (21.18 × 0.05), so its total after allowances (tax 0) is 20.121, not 21.180; the six lines together (consumption line 1) come to 127.08 − 6.354 = 120.726, not 127.080. ConsumptionLine/LineExtensionAmount is "The monetary amount, including discount, to be charged for this consumption line", which also points to 120.726. The same applies to supply lines 2 to 6.
- Condition: Every line amount whose definition includes allowances equals the line amount minus the line's allowance (plus tax, here 0).
- Options: (a, preferred) TaxInclusiveLineExtensionAmount 20.121 per business line and 120.726 for consumption line 1, and consumption line 1's LineExtensionAmount 120.726 with the totals' LineExtensionAmount adjusted accordingly; (b) move the discount to the consumption level only (as invoice 13 has it at document level) and drop it from the lines.
- Needs decision: no

### utilities/12#F3 · Medium · The data pool's 35 GB also listed as a roaming session on a fixed business line
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:TelecommunicationsServiceCategory` = `Roaming: mobile data in Bayvarra`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `35`
- Why: The data pool (supply line 7) bills 35 GB for March, which is also the statement's total metered quantity. Under business line 1, a roaming service of 35 GB of mobile data in Bayvarra on 2026-03-18 at 08:00 is listed, with no amount. Either all of March's 35 GB were used abroad in one session on a fixed business line (implausible, and then the roaming would be billed on line 7 at the domestic rate), or the same 35 GB are listed twice. The roaming entry also carries an exchange rate Lume→Coral although no amount in Lume is given.
- Condition: The roaming quantity is part of the data pool's usage and is stated where it is billed, with a quantity that fits one roaming use; quantities are not counted twice.
- Options: (a, preferred) move the roaming entry to the data pool (line 7) with a plausible part of the 35 GB, and the roaming partner's charge in Lume with the exchange rate if any is charged; (b) drop the roaming entry.
- Needs decision: yes

### utilities/12#F4 · Medium · Telephone-number and call elements used for aggregates
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:ServiceNumberCalled` = `data`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `video`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cbc:PhoneNumber` = `data pool`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `data`
- Why: ServiceNumberCalled is "In the case of a telephone call, the phone number called", CallDate/CallTime "In the case of a telephone call, the date of the call", and PhoneNumber "The phone number used for this telecommunication supply line". "island", "data", "video" and "data pool" are not phone numbers, and the monthly totals of island calls (S-03-1 to S-03-6) and data (D-03) carry a fictitious call time of 2026-03-31 23:59. The elements are mandatory, which is why values were needed; the values do not have the elements' meaning. The same pattern occurs on supply lines 2 to 6.
- Condition: Phone-number elements hold phone numbers (or the data SIM's number), and aggregated usage is not presented as a call at a time that did not occur.
- Options: (a) give the data pool the mobile number of its SIM and model monthly aggregates as the supply line's own amounts instead of pseudo-calls; (b) keep the aggregates and record as a finding on the UBL model that TelecommunicationsService requires call data even for non-call services. Preference: (a) where possible, (b) for video and data sessions.
- Needs decision: yes

### utilities/12#F5 · Medium · CustomerParty is the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: UtilityStatement/CustomerParty is "The buyer, if different from the receiver of the document." Both are Velumi Trading.
- Condition: CustomerParty only when the buyer differs from the receiver.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/12#F6 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`
- Why: Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "... from more than one supplier". One supplier, Selanu Telecom (the Bayvarran roaming partner is not a supplier to Velumi), both alternatives with identical totals.
- Condition: Only the alternative matching the number of suppliers is used.
- Options: (a) Consumption only; (b) SupplierConsumption only with a second supplier; (c) record the UBL model limitation.
- Needs decision: yes

### utilities/12#F7 · Low · Exchange rates with nothing converted
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: No amount in Lume (XBL) appears anywhere in the statement or in invoice 13; all amounts are in Coral. An exchange rate for a conversion that does not happen is a filler.
- Condition: An exchange rate is present only where an amount is converted, and the converted amount is shown.
- Options: (a, preferred) drop both; (b) show the roaming partner's charge in XBL and its conversion.
- Needs decision: no

### utilities/12#F8 · Low · Pay-per-view with nothing paid, and indicators without content
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:PayPerView` = `true`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:PayPerView` = `false`
- Why: The training video is marked pay-per-view, but nothing is paid for it and nothing says it is included in the subscription. PayPerView false on the data pool says nothing (a data volume is never pay-per-view).
- Condition: A pay-per-view item has a charge or a stated reason why it is free; PayPerView appears only where it informs.
- Options: (a, preferred) give the video its price and an allowance "included in the business bundle", or a note; drop PayPerView on line 7.
- Needs decision: no

### utilities/12#F9 · Low · Telecom costs booked as "Stock for municipal projects", and a purchasing contact as receiver
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `500`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Stock for municipal projects`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". The office's telephone lines and data are communication costs, not stock for municipal projects; the same text is used for Velumi's purchases of goods (10 occurrences in `*.xml`, counted with `grep -rh --include='*.xml' -o 'Stock for municipal projects'`). The receiver's contact "Purchasing" has the job title "Customer service officer" in "Sales": name, title and department disagree, and none of them handles telecom bills.
- Condition: The accounting cost is Velumi's communication cost account (or absent); the contact handles utility bills, with agreeing name, title and department.
- Options: (a, preferred) a communication cost account; an accounts-payable or office-management contact.
- Needs decision: no

### utilities/12#F10 · Low · Pack quantity and size for data billed per gigabyte
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackSizeNumeric` = `7`
- Why: The data is priced and billed per gigabyte (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Price/cbc:PriceAmount` = `0.424`, 35 GB). Seven packs of 5 GB give the same 35 GB but play no role in the price or quantity, and nothing in the statement or invoice 13 mentions packs.
- Condition: Pack data appear only if the data is sold in packs, and then price and quantity refer to the packs.
- Options: (a, preferred) drop PackQuantity and PackSizeNumeric; (b) price per 5 GB pack (2.12) with 7 packs.
- Needs decision: no

### utilities/12#F11 · Low · Subscriber type of the utility items is "Telephone", the consumption point's is "Business"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberType` = `Telephone`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:SubscriberType` = `Telephone`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `BUS`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text", its code "The code identifying for the service type". As in the other statements of the flow.
- Condition: Consistent with the consumption point, or the service-type reading is recorded as deliberate.
- Options: (a) record the UBL definition inconsistency; (b) leave both out.
- Needs decision: yes

### utilities/12#F12 · Low · Filler delivery location
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: Says nothing that the consumption point does not say (rule "no fillers"); consumption line 1 has none.
- Condition: Absent, or carrying real information.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/12#F13 · Low · "Numbers masked" while the called number is shown in full
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cbc:PrivacyCode` = `MASKED`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `+999 2 7121 474 274`
- Why: PrivacyCode says the numbers called are masked, but the only external number called is given complete. Masking usually hides the last digits (own knowledge of itemised telephone bills).
- Condition: The called numbers are masked as the privacy code says, or the privacy code says they are not.
- Options: (a, preferred) mask the last digits (e.g. +999 2 7121 474 ***).
- Needs decision: no

## Checked and consistent
- Amounts: 6 × 21.18 = 127.08; 35 GB × 0.424 = 14.84; 127.08 + 14.84 = 141.92 = TotalAmount = LineExtensionAmount; discount 5 % of 127.08 = 6.354 = 6 × 1.059; payable 141.92 − 6.354 = 135.566; tax 0 (outside scope).
- Agreement with 13-Invoice.xml: line 1 (6 months of ST-BL at 21.18), line 2 (35 GB of ST-GB at 0.424), discount 6.354 on 127.08, payable 135.566; ParentDocumentLineReferenceIDs 1 and 2.
- Supply: "Six business lines and a mobile data pool" = supply lines 1 to 6 (+999 3 721 1850 to 1855) and line 7.
- Statement issued 17:37 after the invoice at 11:19 on the same day.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:CallDuty/cac:TaxCategory/cbc:ID`: O for a set-up duty — refuted, the world's Lisavu has no general sales tax and all lines use O consistently.
