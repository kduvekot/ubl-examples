# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1b44438 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### utilities/12#F1 · High · 35 GB of data stated twice, against a metered total of 35 GB
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:TelecommunicationsServiceCategory` = `Roaming: mobile data in Bayvarra`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cbc:InvoicedQuantity` = `35`
- Why: the services of the statement carry 35 GB twice: once as a roaming session in Bayvarra on 18 March under business line 1, and once as the data pool's monthly use under line 7. Together that is 70 GB, while the total metered quantity, the consumption line and the invoice (`13-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `35`) give 35 GB. Either the roaming session is the pool's whole month of data (then it is counted twice, and all of March's pool data was used in one roaming session at 08:00 on one day, priced at the domestic per-GB rate of line 7), or it is additional data that is neither totalled nor billed. The roaming record also sits under a fixed business line ("Business line with calls on the island included"), not under the mobile data pool it belongs to.
- Condition: the data quantities of the services add up to the metered and invoiced total, each gigabyte appears once, and roaming data sits under the line (pool or subscription) that carries it.
- Options: (a, preferred) split the 35 GB: e.g. a roaming session of a few GB under line 7 plus the remaining domestic use, totalling 35; (b) remove the roaming record from line 1 and keep only the pool line; (c) keep 35 GB roaming and add it to the totals and the invoice (changes amounts in 12, 13 and 14).
- Needs decision: yes (how much data was used abroad changes the story and possibly the amounts)

### utilities/12#F2 · Medium · Words instead of numbers in the phone-number elements
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
- Why: ServiceNumberCalled is "In the case of a telephone call, the phone number called", and PhoneNumber is "The phone number used for this telecommunication supply line". The values are category words (island, data, video, data pool), not numbers; the categories are already given in TelecommunicationsServiceCategory and the line Description. Only the international call (Service[2] of line 1) carries a real number. Both elements are mandatory, so the aggregates force a value; for services that are not calls (data, video on demand, monthly summaries) the element has no meaningful value.
- Condition: every ServiceNumberCalled holds a called number, and every PhoneNumber holds the number of the line (for the data pool, e.g. the number or SIM of the pool's access line); services that are not calls to a number are not represented as such calls.
- Options: (a, preferred) give the data pool a line number of its own and represent island calls as individual calls (or one call per real number) only where they are reported; (b) leave out the summary and data records whose number would be invented, keeping the information in the line Description and the consumption line.
- Needs decision: no

### utilities/12#F3 · Low · Contract number used as subscriber identifier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cac:Contract/cbc:ID` = `ST-C-1077`
- Why: SubscriberID ("An identifier for the subscriber responsible for the consumption at this consumption point") holds the contract's ID, also used as SubscriberID of both utility items. Same pattern in all five statements of the flow (see utilities/01#F3).
- Condition: SubscriberID identifies the subscriber (customer number), or is absent.
- Options: a customer number (preferred), or drop SubscriberID.
- Needs decision: no

### utilities/12#F4 · Low · Monthly summaries dated as calls at 23:59 on 31 March
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[1]/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[3]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[4]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[5]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[6]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:CallTime` = `23:59:00`
- Why: CallDate is "In the case of a telephone call, the date of the call". The island-call records (140 to 265 minutes) and the data pool record (35 GB) are month totals; the date 2026-03-31 and time 23:59 are not when any call took place but stand in for "the month". A reader cannot tell them from a real call at that moment. (Physics: 265 minutes in one call starting at 23:59 is possible, but six such calls on six lines at the same minute are not what the statement means.)
- Condition: a CallDate/CallTime is the start of an actual call or session; month totals are not given a call time.
- Options: see F2 option (b): carry month totals outside TelecommunicationsService (line Description, consumption line); or list real calls.
- Needs decision: no

### utilities/12#F5 · Low · Six line-months invoiced as "6 months"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:Period/cbc:EndDate` = `2026-03-31`
- Why: unitCode MON is "month"; 6 MON reads as six months of subscription, while the period is one month (2026-03-01 to 2026-03-31) and the quantity is six lines for one month each. The same quantity is in the invoice (`13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`).
- Condition: quantity and unit say six line subscriptions for one month (e.g. 6 of a unit "each"/"piece" with the price per line and month, or six lines of 1 MON).
- Options: (a, preferred) quantity 6 with unit EA (or C62) and price 21.18 per line and month, stated in the description; (b) one consumption line per business line, 1 MON each.
- Needs decision: no

### utilities/12#F6 · Low · Delivery location that only points back to the statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- Why: no identifier or address, only a pointer to consumption point ST-CP-1077 already identified (no fillers). For mobile data the "delivery location" is moreover not the office (the data was partly used in Bayvarra, see F1). See utilities/01#F5.
- Condition: Delivery is absent or identifies the location.
- Options: remove it (preferred).
- Needs decision: no

### utilities/12#F7 · Low · Pack quantity and pack size on a data item billed per gigabyte
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackQuantity` = `5`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:PackSizeNumeric` = `7`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:Price/cbc:BaseQuantity` = `1`
- Why: PackQuantity is "The unit packaging quantity" and PackSizeNumeric "The number of items in a pack". 5 GB × 7 = 35 GB is this month's use, i.e. a quantity of the consumption, not a property of the item; and the item is described and priced "per gigabyte" (base quantity 1 GB, 35 × 0.424 = 14.84), so no pack applies. Read literally, a pack of 7 items of 5 GB each would be a 35 GB pack, which the price per GB does not reflect either.
- Condition: pack elements appear only if the data is sold in packs, and then price and quantity are per pack.
- Options: (a, preferred) remove both elements; (b) sell data in 5 GB packs: 7 packs, price per pack 2.12, with the description saying so.
- Needs decision: no

## Checked and consistent
- Six lines × 21.18 = 127.08; data 35 × 0.424 = 14.84; TotalAmount 141.92 = LineExtensionAmount; 5 % of 127.08 = 6.354 (6 × 1.059); payable 135.566 — all equal to 13-Invoice.xml.
- ParentDocumentReference ST-INV-26-0323 resolves to 13-Invoice.xml (issued 11:19, before this statement at 17:37); ParentDocumentLineReferenceID 1 and 2 match its lines (6 MON business lines, 35 GB data).
- Service dates (11, 18, 20 and 31 March) lie within the period 2026-03-01 to 2026-03-31 and before the issue date.
- International call of 12 minutes: allowance 2.400 = 12 × 0.20 (implied per-minute price); country XB matches the called number's country prefix in the world's numbering (+999 2 …) and the category text.
- Units: MIN for minutes, E34 for gigabytes, EA for the video, MON for months (see F5).

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity`: the "total quantity consumed, as calculated from meter readings" omits the minutes — refuted because only the data is metered against a charge; the minutes are included in the subscription.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[1]/cbc:Quantity`: the island-call minutes rise by exactly 25 from line to line (140 … 265) — refuted as a finding: unusual but not impossible, and no value contradicts another.

## Outside this review
- Outside the logistics lens (money/context): the roaming record carries an exchange rate XBL → XLC but no amount in either currency; the pay-per-view video is priced 0 although PayPerView is true; both for the money and context parts.
