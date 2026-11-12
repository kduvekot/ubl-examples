# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
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

### utilities/12#F1 · High · Numbers declared masked, but a called number is shown in full
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cbc:PrivacyCode` = `MASKED`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `+999 2 7121 474 274`
- Why: PrivacyCode is "A code signifying the level of confidentiality of this information for this telephone line"; MASKED means "Numbers masked". The international call lists the complete number called, so the code contradicts the value it governs.
- Condition: With PrivacyCode MASKED, every called number is masked (e.g. last digits replaced); otherwise the code says the numbers are shown.
- Options: (a, preferred) mask the number (e.g. `+999 2 7121 474 ***`); (b) a privacy code for unmasked numbers.
- Needs decision: no

### utilities/12#F2 · High · The month's 35 GB appear twice: as roaming on a fixed line on 18 March and as the data pool
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:CallDate` = `2026-03-18`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cbc:Description` = `Business line with calls on the island included.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `35`
- Why: Line 1 is a business telephone line (+999 3 721 1850); under it a service records 35 GB of mobile data roaming in Bayvarra on 18 March at 08:00. Line 7, the mobile data pool, records 35 GB for the month and bills them (14.840), and the statement's total metered quantity is 35 GB. Either all of the month's data was used abroad in a single session on a fixed line, which is not possible, or the same 35 GB are listed twice. The roaming service carries no amount, so what it bills is not visible either.
- Condition: Each gigabyte appears once, under the line (the data pool or a mobile subscription) on which it was used, and roaming data is a part of the total with its own amount if roaming is charged.
- Options: (a, preferred) move the roaming record to the data pool line with a plausible part of the 35 GB and its amount (or 0 with the Trade Accord reason); (b) remove the roaming record.
- Needs decision: no

### utilities/12#F3 · High · An allowance of 2.400 on a call priced at 0
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:Price/cbc:PriceAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallBaseAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:BaseAmount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:Amount` = `2.400`
- Why: The allowance ("Calls to the trade accord countries are included in the subscription") is taken from a base of 2.400, but the call's price, base amount, duties and extension amount are all 0. A discount of 2.400 from a call worth 0 contradicts the price; and it is in no total (the line amount 21.180 is the bare subscription).
- Condition: Either the call is priced (e.g. 12 min at 0.20 = 2.400) and the allowance brings it to 0, or the price is 0 and there is no allowance.
- Options: (a, preferred) price the call at its list rate and keep the allowance, so the inclusion is visible; (b) drop the allowance and keep the note in the reason of the zero price.
- Needs decision: no

### utilities/12#F4 · Medium · ConsumptionLine amounts said to include the discount are before the discount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:LineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: ConsumptionLine/LineExtensionAmount is "The monetary amount, including discount, to be charged for this consumption line", and TaxInclusiveLineExtensionAmount "The total amount for this consumption line, including all allowances, charges and taxes". The line carries a discount of 6.354, so both should be 127.080 − 6.354 = 120.726; 127.080 is 6 × 21.18 before the discount.
- Condition: Both amounts of the consumption line include its allowance.
- Options: (a, preferred) 120.726 in both (the totals then follow the line, without a second deduction).
- Needs decision: no

### utilities/12#F5 · Medium · Quantity "the number of calls" holds minutes, gigabytes and views
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:Quantity` = `140`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:Quantity` = `12`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- Why: TelecommunicationsService/Quantity is defined as "The number of calls." The values are durations in minutes (unitCode MIN), data volumes in gigabytes (E34) and a view (EA); one call of 12 minutes is recorded as 12. The same holds for the island-call and data services of all seven lines.
- Condition: Quantity holds the number of calls (or the definition's narrowness is recorded as a UBL finding and the use is decided).
- Options: (a) Quantity = number of calls, duration where UBL has it (e.g. via TimeDuty or a note); (b) record that UBL lacks a duration/volume element here and keep the use as a documented deviation. Preferred: (b) with a finding, as no other element carries duration.
- Needs decision: yes

### utilities/12#F6 · Medium · Words where telephone numbers are defined, and month totals posing as calls
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:ServiceNumberCalled` = `data`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `video`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cbc:PhoneNumber` = `data pool`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallDate` = `2026-03-31`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- Why: ServiceNumberCalled is "The telephone number called" and PhoneNumber the line's telephone number; "island", "data", "video" and "data pool" are not numbers. The island-call services of lines 1–6 (and the data service of line 7) are monthly totals given a call date and time of 31 March 23:59, which no call had (CallDate: "The date of the call"). The same pattern is in every supply line.
- Condition: ServiceNumberCalled and PhoneNumber hold numbers or are absent; a TelecommunicationsService is one service use with its real date and time, and monthly totals are expressed as totals (supply line amounts, category text).
- Options: (a, preferred) leave ServiceNumberCalled out where no number exists, keep the category text, and drop CallDate/CallTime from monthly totals; for the data pool, leave PhoneNumber out or use the pool's SIM/line number.
- Needs decision: no

### utilities/12#F7 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Selanu Telecom`
- Why: SupplierConsumption is "The consumption in case the consumption is from more than one supplier"; Selanu Telecom is the only supplier, and Consumption already describes the supply (with the roaming partner only as a name in a service record).
- Condition: SupplierConsumption only where there is more than one supplier.
- Options: (a, preferred) remove it here.
- Needs decision: yes

### utilities/12#F8 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: CustomerParty is "The buyer, if different from the receiver of the document."
- Condition: CustomerParty only when the buyer differs from the receiver.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/12#F9 · Medium · The subscriber identifier is the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- Why: SubscriberID identifies the subscriber; ST-C-1077 is the contract (`13-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:ID` = `ST-C-1077`, "Supply contract").
- Condition: SubscriberID holds a subscriber identifier, or is absent.
- Options: (a, preferred) a customer number; (b) remove.
- Needs decision: no

### utilities/12#F10 · Low · Pay-per-view with nothing to pay; pay-per-view flag on data
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:PayPerView` = `true`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:PayPerView` = `false`
- Why: A pay-per-view title is paid per viewing, but the view costs 0.000 and no reason is given (e.g. included in the bundle). On the data service, PayPerView false says only that data is not a video (nothing implied by absence, IND6).
- Condition: A pay-per-view view has its price or a stated reason why it is free; PayPerView appears only on video services.
- Options: (a, preferred) a price for the view, or PayPerView false with a note that the training video is included; remove the flag from the data service.
- Needs decision: no

### utilities/12#F11 · Low · Exchange rates with nothing converted
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: ExchangeRate is "Exchanges rates used to calculate the amount for this line" (and for the service, "used in the pricing e.g. when phone calls has crossed border lines"). No amount of line 1 or of the roaming service is in Lume or results from a conversion: the line is the subscription in Coral, the call costs 0 and the roaming record has no amount.
- Condition: An exchange rate is given only where an amount was converted with it, and the converted amount is visible.
- Options: (a, preferred) remove both, or keep the one on the roaming service once it carries the partner's Lume charge and its Coral amount (see F2).
- Needs decision: no

### utilities/12#F12 · Low · The bundle discount is stated at three levels
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:AllowanceCharge/cbc:Amount` = `6.354`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: The same 5 % discount appears on the consumption (6.354), on each of the six supply lines (6 × 1.059 = 6.354) and on the consumption line (6.354). The totals deduct it once (141.920 − 6.354 = 135.566), but a reader summing the allowances finds it three times, and the supply-line TaxInclusiveLineExtensionAmount (21.180) ignores its own 1.059.
- Condition: The discount is stated once per level that actually computes it, and amounts at that level include it.
- Options: (a, preferred) keep it on the consumption line (matching the invoice's allowance) and remove the others.
- Needs decision: no

### utilities/12#F13 · Low · Buyer's cost centre "Stock for municipal projects" for telephone bills
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `500`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Stock for municipal projects`
- Why: Velumi Trading's telephone and data costs are office overheads, not stock for municipal projects; the text occurs in 10 examples (grep over `*.xml`), Velumi's purchasing default.
- Condition: The cost centre fits telecommunication costs, or is absent.
- Options: (a, preferred) an office or telecommunication cost centre.
- Needs decision: no

### utilities/12#F14 · Low · SubscriberType names the utility; filler location
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberType` = `Telephone`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: The item's SubscriberType ("Identification of the subscriber type") gives the utility, while the subscriber type at the point is "Business"; the delivery location says nothing the statement does not (IND5).
- Condition: As in `01-UtilityStatement.xml`.
- Options: drop the text SubscriberType and the filler Delivery.
- Needs decision: no

## Checked and consistent
- ParentDocumentReference ST-INV-26-0323 → `13-Invoice.xml`: line 1 6 × 21.18 = 127.08, line 2 35 GB × 0.424 = 14.84; totals 141.920, allowance 6.354 (5 % of 127.08), payable 135.566, equal to the invoice.
- Supply line amounts: 6 × 21.180 + 14.840 = 141.920 = TelecommunicationsSupply/TotalAmount.
- UtilityItem ST-GB: 7 packs × 5 GB = 35 GB.
- Exchange rate 1 XBL = 0.4 XLC agrees with the rate used in other flows (e.g. `energy/06-Invoice.xml`).
- Statement issued after its invoice (17:37 vs 11:19).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UnstructuredPrice/cbc:PriceAmount` = `21.18`: repeats the structured price — refuted because UBL offers the unstructured price with the time basis ("per month") as a reading aid, and the two agree.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:MovieTitle`: a training video on a business line — refuted because a warehouse safety training watched at the office is a plausible business use.
