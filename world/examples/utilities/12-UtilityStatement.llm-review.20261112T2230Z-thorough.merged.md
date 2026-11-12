# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
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

### utilities/12#F1 · High · The month's 35 GB stated twice: as one roaming session on a fixed business line and as the data pool
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cbc:Description` = `Business line with calls on the island included.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:TelecommunicationsServiceCategory` = `Roaming: mobile data in Bayvarra`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:CallDate` = `2026-03-18`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:CallExtensionAmount` = `14.840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cbc:InvoicedQuantity` = `35`
- Why: The services of the statement carry 35 GB twice: once as a roaming session in Bayvarra on 18 March at 08:00 under business line 1 (a fixed line, "Business line with calls on the island included"), with no amount, and once as the data pool's month under line 7, billed at 35 × 0.424 = 14.840 (recalculated in the merge). Together that is 70 GB, while the total metered quantity, the consumption line and the invoice (`13-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `35`) give 35 GB. Either the roaming session is the pool's whole month (counted twice, and all of March's data used in one session abroad on a fixed line, billed at the domestic per-GB rate), or it is extra data that is neither totalled nor billed. Refutation tried: no element links the roaming record to the pool (no reference, no "included in" note), so no reading makes the quantities add up.
- Condition: The data quantities of the services add up to the metered and invoiced total, each gigabyte appears once, under the line (pool or mobile subscription) on which it was used, and roaming data carries its own amount if roaming is charged.
- Options: (a, preferred) move the roaming record to the data pool line with a plausible part of the 35 GB (the rest domestic use, totalling 35), with its amount (or 0 with the Trade Accord reason); (b) remove the roaming record; (c) keep 35 GB of roaming in addition and add it to the totals and the invoice (changes amounts in 12, 13 and 14).
- Needs decision: yes (how much data was used abroad changes the story and possibly the amounts)
- From: broad (F3, Medium/yes), money (F6, Low/yes), context (F2, High/no), logistics (F1, High/yes)

### utilities/12#F2 · High · Numbers declared masked, but the called number is shown in full
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cbc:PrivacyCode` = `MASKED`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `+999 2 7121 474 274`
- Why: PrivacyCode is "A code signifying the level of confidentiality of this information for this telecommunication supply". The world's PrivacyCode list defines MASKED as "Numbers masked": "Telephone numbers are shown with their last digits replaced." (`world/codelists/gc/PrivacyCode.gc`, read in the merge). The only external number called is given complete, so the code contradicts the value it governs. The merge tried the reading "caller-ID of the line withheld"; the list's own description excludes it.
- Condition: With PrivacyCode MASKED, every called number has its last digits replaced; otherwise the code says the numbers are shown (PUBLIC or CONFIDENTIAL, as the list defines them).
- Options: (a, preferred) mask the number (e.g. `+999 2 7121 474 ***`); (b) another privacy code.
- Needs decision: no
- From: broad (F13, Low), context (F1, High)

### utilities/12#F3 · High · Line totals "including all allowances" ignore the allowance on the same line
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[3]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[4]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[5]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[6]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:LineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: UBL defines TaxInclusiveLineExtensionAmount for the supply line as "The total amount for this telecommunications supply line, including all allowances, charges and taxes", and for the consumption line as "The total amount for this consumption line, including all allowances, charges and taxes"; ConsumptionLine/LineExtensionAmount is "The monetary amount, including discount, to be charged for this consumption line". Each business line carries a 5 % discount of 1.059 (21.180 × 0.05) and no tax, so its total is 21.180 − 1.059 = 20.121, not 21.180; consumption line 1 carries the discount of 6.354, so both its amounts should be 127.080 − 6.354 = 120.726 (recalculated in the merge). (The supply line's LineExtensionAmount, "An amount specifying the cost of this telecommunication line", has no such condition and may stay 21.180.)
- Condition: On every line that carries an allowance, the tax-inclusive total (and, on the consumption line, the line extension amount) equals the amount after that allowance (plus tax, here 0).
- Options: (a, preferred) 20.121 on supply lines 1–6 and 120.726 on consumption line 1 (both amounts), with the totals following the lines without a second deduction; (b) move the discount off the lines to the consumption level only (as invoice 13 has it at document level), so that 21.180 and 127.080 hold. See F6 for which level carries the discount.
- Needs decision: no
- From: broad (F2), money (F1), context (F4, Medium, consumption line only; F12, part)

### utilities/12#F4 · High · Allowance of 2.400 on an international call whose price and base amount are 0, missing from every total
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallBaseAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:Price/cbc:PriceAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:Amount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:BaseAmount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` = `6.354`
- Why: The 12-minute call to Bayvarra has a base amount ("The amount to be payed as the base for one call") of 0, a price of 0, duties of 0 and an amount to be paid ("The amount to be payed for the call") of 0, yet carries an allowance ("Calls to the trade accord countries are included in the subscription") of 2.400 from a base of 2.400, an amount the call never had: 0 − 2.400 ≠ 0. The allowance has no multiplier, so its BaseAmount has nothing to be applied to. The consumption's allowance total, "the total monetary amount of all allowances", is 6.354 = 6 × 1.059, the bundle discount alone, so the 2.400 is in no total. Logistics read 2.400 as 12 × 0.20, an implied per-minute rate; that rate is stated nowhere, and the price says 0.
- Condition: The call's price × quantity (or base amount) − allowance = extension amount, and every allowance is in AllowanceTotalAmount (or the call is priced 0 without an allowance).
- Options: (a, preferred) price 0.20 per minute, CallBaseAmount 2.400, the allowance of 2.400 (BaseAmount only with a multiplier), extension 0.000, and AllowanceTotalAmount 8.754 with the totals adjusted, which keeps the "included in the subscription" reason visible; (b) drop the allowance and keep the call at 0 with the reason in a note.
- Needs decision: no
- From: broad (F1), money (F2), context (F3)

### utilities/12#F5 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Both are Velumi Trading (same register number IC41859). `03-UtilityStatement.xml` uses the element as defined.
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: broad (F5), parties (F1), context (F8)

### utilities/12#F6 · Medium · The same bundle discount appears at three levels
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:AllowanceCharge/cbc:Amount` = `6.354`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: The Consumption carries the 5 % bundle discount of 6.354 as "An allowance or charges that may apply with this consumption"; each of its six supply lines carries its share of 1.059 again (6 × 1.059 = 6.354), and the supplier view's consumption line 1 carries 6.354 once more. Within the same Consumption the allowances add up to 12.708 while the total says 6.354; the totals deduct the discount once (141.920 − 6.354 = 135.566), so a reader cannot tell which of these is the allowance and which are repetitions. The invoice gives the discount once, at document level (`13-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `6.354`).
- Condition: Within one Consumption, the discount is given once, at the level where it is calculated, and the allowances present add up to AllowanceTotalAmount.
- Options: (a, preferred, money) keep the discount on the six supply lines and on consumption line 1 (each view once) and remove it from the Consumption level; (b, context) keep it only on the consumption line, matching the invoice, and remove the others; (c) keep it only at the Consumption level. Whichever is chosen, F3's line totals follow.
- Needs decision: no
- From: money (F3, Medium), context (F12, Low)

### utilities/12#F7 · Medium · Words where telephone numbers are defined
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:ServiceNumberCalled` = `data`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[1]/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:ServiceNumberCalled` = `video`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[3]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[4]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[5]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[6]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `island`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:ServiceNumberCalled` = `data`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cbc:PhoneNumber` = `data pool`
- Why: ServiceNumberCalled is "In the case of a telephone call, the phone number called", and PhoneNumber "The phone number used for this telecommunication supply line". "island", "data", "video" and "data pool" are category words, not numbers; the categories are already in TelecommunicationsServiceCategory and the line Description. Only the international call carries a real number. Both elements are mandatory ([1]), so month totals, data sessions and video views force a value the element cannot meaningfully hold; recording that as a UBL model finding is one of the options, which makes this a decision.
- Condition: Every ServiceNumberCalled holds a called number and every PhoneNumber the number of its line (for the data pool, e.g. the number or SIM of the pool's access line), and services that are not calls to a number are not represented as such calls; or the model limitation is recorded and the use decided.
- Options: (a, preferred where possible) give the data pool a line number of its own, list island calls only as real calls where they are reported, and carry month totals outside TelecommunicationsService (line Description, consumption line); (b) for video and data sessions, keep the records and record as a UBL finding that TelecommunicationsService requires call data even for non-call services.
- Needs decision: yes
- From: broad (F4, Medium/yes), context (F6, Medium/no), logistics (F2, Medium/no)

### utilities/12#F8 · Medium · Quantity "the number of calls" holds minutes, gigabytes and views
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:Quantity` = `140`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:Quantity` = `12`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- Why: TelecommunicationsService/Quantity is defined as "The number of calls." The values are durations in minutes (MIN), data volumes in gigabytes (E34) and a view (EA); one call of 12 minutes is recorded as 12. The same holds for the island-call, video and data services of all seven lines. UBL has no other element for a duration or volume here (TimeDuty is an amount), so the fix is either a model finding or a change of what the services record.
- Condition: Quantity holds the number of calls, or the definition's narrowness is recorded as a UBL finding and the use decided.
- Options: (a) Quantity = number of calls, with the duration elsewhere (note); (b, preferred by context) record that UBL lacks a duration/volume element here and keep the use as a documented deviation.
- Needs decision: yes
- From: context (F5)

### utilities/12#F9 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Selanu Telecom`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `135.566`
- Why: Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "The consumption in case the consumption is from more than one supplier". Selanu Telecom is the only supplier (the Bayvarran roaming partner appears only as a name in a service record and supplies nothing to Velumi), and both alternatives are present with identical totals. ConsumptionLine is only reachable under SupplierConsumption.
- Condition: Only the alternative matching the number of suppliers is used, or the model limitation is recorded.
- Options: (a) Consumption only; (b) SupplierConsumption only, with a real second supplier; (c) record the UBL model limitation (consumption lines only under SupplierConsumption).
- Needs decision: yes
- From: broad (F6), context (F7)

### utilities/12#F10 · Low · Telephone lines booked to "Stock for municipal projects"
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `500`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Stock for municipal projects`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". Velumi Trading's telephone and data costs are office overheads, not stock for municipal projects; the text is Velumi's purchasing default for goods (recounted in the merge: 10 occurrences in 9 files, `grep -rho --include='*.xml' 'Stock for municipal projects'` and `grep -rl`). Invoice 13 carries the same value.
- Condition: The accounting cost names a cost account that fits telecommunications (the same in 12 and 13), or is absent.
- Options: (a, preferred) a telecom or office cost code.
- Needs decision: no
- From: broad (F9, part), money (F8), context (F13)

### utilities/12#F11 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 companies of the world are registered on 1 January 1996 (parties' count), Selanu Telecom and Velumi Trading among them; recounted in the merge: 271 occurrences in 181 files over `world/examples/*/*.xml`. The shared New Year's Day looks like a default value (no fillers). For Selanu Telecom, `SMALL` is also questionable: it runs the island's business lines, a mobile data service and roaming agreements, which suggests a national operator; on a small island this may still be intended.
- Condition: Both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits what the story makes of it, the same in every example.
- Options: (a, preferred) a registration date of its own for each company, and review the operator's size; (b) drop the elements where the documents do not need them.
- Needs decision: yes
- From: parties (F2)

### utilities/12#F12 · Low · Receiver's customs trader number in a telecom statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: Velumi's customs trader number has no use in a domestic telecom document (island lines, data and roaming, no goods); it is part of Velumi's party data repeated in every example that carries it.
- Condition: The customs trader number appears here only with a use in this document.
- Options: (a, preferred) drop it here; (b) keep it only with a stated reason.
- Needs decision: no
- From: parties (F3)

### utilities/12#F13 · Low · Receiver's contact: "Purchasing" with a sales job title and department
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact's name says purchasing, its job title and department say customer service in Sales: they contradict each other, and the sales side does not handle the telecom bills Velumi receives. The contact is the same in every example with Velumi's full data.
- Condition: Name, job title and department agree, and the function fits receiving the telecom statement and bill (purchasing, accounts payable or office management).
- Options: (a, preferred) an accounts-payable or office-management contact; (b) drop the job title and department.
- Needs decision: no
- From: broad (F9, part), parties (F4)

### utilities/12#F14 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cac:Contract/cbc:ID` = `ST-C-1077`
- Why: `SubscriberID` is "An identifier for the subscriber responsible for the consumption at this consumption point", but holds the contract's number (`13-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:ID` = `ST-C-1077`, "Supply contract"). Whether the world treats the subscription number and the contract number as one cannot be settled from the examples (context Medium, parties and logistics Low). Same pattern in all five statements of the flow.
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number serves as the subscriber number.
- Options: (a, preferred) a customer number of Velumi at Selanu Telecom; (b) record that the contract number serves as the subscriber number; (c) remove SubscriberID.
- Needs decision: yes
- From: parties (F5, Low/yes), context (F9, Medium/no), logistics (F3, Low/no)

### utilities/12#F15 · Low · Monthly summaries dated as calls at 23:59 on 31 March
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallDate` = `2026-03-31`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[3]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[4]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[5]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[6]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- Why: CallDate is "In the case of a telephone call, the date of the call". The island-call records (140 to 265 minutes) and the data-pool record (35 GB) are month totals; the date 2026-03-31 and time 23:59 are not when any call took place but stand in for "the month", and a reader cannot tell them from a real call at that moment (seven calls on seven lines at the same minute). Both elements are mandatory, which is what F7 is about; this finding is about the invented time.
- Condition: A CallDate/CallTime is the start of an actual call or session; month totals are not given a call time.
- Options: see F7 option (a): carry month totals outside TelecommunicationsService, or list real calls.
- Needs decision: no
- From: logistics (F4); also part of broad (F4) and context (F6)

### utilities/12#F16 · Low · Exchange rates that convert nothing
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The line-level rate is "Exchanges rates used to calculate the amount for this line", the service-level rate "A exchanges rates used in the pricing e.g.. when phone calls has crossed border lines". No amount on line 1 or on the roaming service is in Lume (XBL) or results from a conversion: the line is the XLC subscription price of 21.180, and the roaming record has no amount at all. The rate itself (1 XBL = 0.4 XLC) agrees with the other examples that convert XBL to XLC (e.g. `energy/06-Invoice.xml`).
- Condition: An exchange rate is present only where an amount of the line or service was converted with it, and the converted amount is shown.
- Options: (a, preferred) remove both; (b) keep the one on the roaming service once it carries the partner's XBL charge and its XLC amount (see F1).
- Needs decision: no
- From: broad (F7), money (F5), context (F11); logistics (under "Outside this review")

### utilities/12#F17 · Low · A 0 % rate with category O under a "no sales tax" scheme
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:CallDuty/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cac:TaxCategory/cbc:Percent` = `0`
- Why: Category O (outside the scope of tax) has no rate, so 0 % suggests zero-rating (Z). The same is in invoice 13 (13#F5). The CallDuty place was added in the merge (same category, same value).
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no
- From: money (F9)

### utilities/12#F18 · Low · A pay-per-view title at no charge, and a pay-per-view flag on data
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:PayPerView` = `true`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:PayPerView` = `false`
- Why: Pay-per-view means the viewing is charged, but the training video costs 0.000 with no allowance or note explaining it (e.g. included in the business bundle). On the data pool, PayPerView false says only that data is not a video (no fillers, IND6).
- Condition: A pay-per-view view has its price or a stated reason why it is free; PayPerView appears only on video services.
- Options: (a, preferred) give the video its price and an allowance "included in the business bundle", or set PayPerView false with a note that it is included; remove the flag from the data service.
- Needs decision: no
- From: broad (F8), money (F7), context (F10); logistics (under "Outside this review")

### utilities/12#F19 · Low · Six lines for one month invoiced as "6 months"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:Price/cbc:BaseQuantity` = `1`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:Period/cbc:EndDate` = `2026-03-31`
- Why: unitCode MON is "month"; 6 MON reads as six months of subscription, while the period is one month (2026-03-01 to 2026-03-31) and the quantity counts six lines for that month. Read as six subscription-months (line-months) the arithmetic holds (6 × 21.18 per month = 127.08), which is why the merge rates it Low (logistics) rather than Medium (money): the unit is not wrong, only ambiguous against the period. The same quantity is in invoice 13 (`13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`).
- Condition: Quantity and unit say six line subscriptions for one month (e.g. 6 of a count unit at 21.18 per line and month, or six consumption lines of 1 MON), the same in invoice 13.
- Options: (a, preferred) quantity 6 with unit C62 (or EA) and the price per line and month stated in the description or UnstructuredPrice; (b) one consumption line per business line, 1 MON each.
- Needs decision: no
- From: money (F4, Medium), logistics (F5, Low)

### utilities/12#F20 · Low · Subscriber type of the utility items is "Telephone", the consumption point's is "Business"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberType` = `Telephone`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:SubscriberType` = `Telephone`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `BUS`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text", while SubscriberTypeCode is "The code identifying for the service type"; the text gives the utility where its definition asks for the subscriber type, and the consumption point says Business. UBL's two definitions disagree; the same occurs in 01, 03, 05 and 08.
- Condition: Text and code each match their definitions (text consistent with the consumption point), or the service-type reading is recorded as deliberate together with the UBL definition inconsistency.
- Options: (a) record the UBL definition inconsistency for the TC and keep the code; (b) drop the text SubscriberType (context's preference); (c) leave both out.
- Needs decision: yes
- From: broad (F11, Low/yes), context (F14, part, Low/no)

### utilities/12#F21 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: No identifier or address, only a pointer to consumption point ST-CP-1077 already identified (no fillers); consumption line 1 has none. For mobile data the "delivery location" is moreover not the office (part of the data was used in Bayvarra, F1).
- Condition: Delivery is absent or identifies the location.
- Options: (a, preferred) remove it.
- Needs decision: no
- From: broad (F12), context (F14, part), logistics (F6)

### utilities/12#F22 · Low · Pack quantity and pack size on a data item billed per gigabyte
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackSizeNumeric` = `7`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Price/cbc:PriceAmount` = `0.424`
- Why: PackQuantity is "The unit packaging quantity" and PackSizeNumeric "The number of items in a pack". 5 GB × 7 = 35 GB is this month's use, a quantity of the consumption, not a property of the item; and the item is described and priced "per gigabyte" (base quantity 1 GB, 35 × 0.424 = 14.840), so no pack applies. Read literally, a pack of 7 items of 5 GB would be a 35 GB pack, which the price per GB does not reflect either. Nothing in the statement or invoice 13 mentions packs.
- Condition: Pack elements appear only if the data is sold in packs, and then price and quantity are per pack.
- Options: (a, preferred) remove both elements; (b) sell data in 5 GB packs: 7 packs at 2.12 per pack, with the description saying so.
- Needs decision: no
- From: broad (F10), logistics (F7)

## Checked and consistent
- Amounts (redone in the merge): 6 × 21.180 = 127.080; 35 × 0.424 = 14.840; 127.080 + 14.840 = 141.920 = TotalAmount = LineExtensionAmount; 21.180 × 0.05 = 1.059 and 6 × 1.059 = 6.354 = 127.080 × 0.05; 141.920 − 6.354 = 135.566 = PayableAmount = invoice 13's PayableAmount; tax 0 (outside the scope, "No general sales tax").
- ParentDocumentReference ST-INV-26-0323 resolves to `13-Invoice.xml` (issued 11:19, before this statement at 17:37); ParentDocumentLineReferenceIDs 1 and 2 match its lines (6 MON business lines at 21.18; 35 GB at 0.424).
- "Six business lines and a mobile data pool" = supply lines 1–6 (+999 3 721 1850 to 1855) and line 7. Service dates (11, 18, 20 and 31 March) lie within the period and before the issue date.
- The international call's country XB matches the called number's prefix (+999 2 …); the number is the contact telephone of a Bayvarran party elsewhere in the world (parties).
- Selanu Telecom and Velumi Trading are described identically in 12–14, with the same register numbers as in `13-Invoice.xml`; neither carries a tax scheme, matching "No general sales tax"; the consumption point address equals Velumi's postal address with the Lisavan and en-XL renderings tagged; ISIC 6110 and 4649 against the world's ISIC source (parties).
- Units: MIN for minutes, E34 for gigabytes, EA for the video, MON for months (see F19).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:CallDuty/cac:TaxCategory/cbc:ID`: O for a set-up duty — refuted, Lisavu has no general sales tax and all lines use O consistently (from broad; the 0 % next to it is F17).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:RoamingPartnerName` = `Lumeport mobile network`: a roaming partner not described as a party — refuted, UBL defines only a name for it, and a network name is what a roaming record shows (from parties).
- `/UtilityStatement/cac:SenderParty/cac:PartyName/cbc:Name` = `Selanu Telecom`: the sender's contact "Business accounts" in customer service checked against the role — it fits the supplier of business lines (from parties).
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UnstructuredPrice/cbc:PriceAmount` = `21.18`: repeats the structured price — refuted, UBL offers the unstructured price with the time basis ("per month") as a reading aid, and the two agree (from context).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:MovieTitle`: a training video on a business line — refuted, a warehouse safety training watched at the office is a plausible business use (from context).
- `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity`: the "total quantity consumed, as calculated from meter readings" omits the minutes — refuted, only the data is metered against a charge; the minutes are included in the subscription (from logistics).
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:Quantity`: island-call minutes rising by exactly 25 from line to line (140 … 265) — refuted as a finding: unusual but not impossible, and no value contradicts another (from logistics).

## Changed in the merge
- broad/F3 (Medium/yes), money/F6 (Low/yes), context/F2 (High/no), logistics/F1 (High/yes) → F1: High/yes. Section 6: quantities that do not add up to the stated total are a contradiction; yes because the amount of roaming changes the story.
- broad/F13 (Low), context/F1 (High) → F2: High. The world's PrivacyCode list says the last digits are replaced; the full number contradicts it.
- context/F4 (Medium, consumption line) joined broad/F2 and money/F1 in F3 (High): same arithmetic problem.
- money/F3 (Medium), context/F12 (Low) → F6: Medium; both preferred options kept, labelled.
- broad/F4, context/F6, logistics/F2 and logistics/F4 → F7 (number words, Medium/yes) and F15 (invented call times, Low/no): split because the call-time part has another severity (logistics' split). F7 Needs decision yes (broad): one option is a UBL model finding.
- money/F4 (Medium), logistics/F5 (Low) → F19: Low; read as line-months the quantity and arithmetic hold, the unit is only ambiguous against the one-month period. Same in 13.
- money/F9 → F17: the CallDuty Percent added as a place.
- parties/F5, context/F9, logistics/F3 → F14: Low/yes, aligned with merger A.
- broad/F11, context/F14 (SubscriberType part) → F20: Low/yes, aligned with merger A. context/F14 (delivery part) joined broad/F12 and logistics/F6 in F21.
- broad/F9 split into F10 (cost centre) and F13 (contact).
- broad/F10, logistics/F7 → F22; money's base-price XPath added.
- Counts re-made: "Stock for municipal projects" 10 occurrences in 9 files (parts said 10 examples); RegistrationDate 271 in 181 files.
