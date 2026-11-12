# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/05#F1 · High · Consumption average amount is the current month's amount, not an average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 82 m³.`
- Why: AverageAmount is "The average monetary amount of the consumption". The average quantity is right ((81 + 79 + 86) / 3 = 82 m³); its amount is 82 × 2.35 = 192.70 XBL (= (190.35 + 185.65 + 202.10) / 3). The value 202.10 is March's amount (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:LineExtensionAmount` = `202.10`). The same pattern occurs in 01-UtilityStatement.xml and 03-UtilityStatement.xml.
- Condition: AverageAmount is the average of the amounts of the months whose quantities the description averages (192.70 XBL).
- Options: (a, preferred) 192.70.
- Needs decision: no

### utilities/05#F2 · Medium · CustomerParty is the receiver, though its definition is "the buyer, if different from the receiver"
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `20410411`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `20410411`
- Why: UtilityStatement/CustomerParty is "The buyer, if different from the receiver of the document." Both are Brightmarket Stores, so the condition is not met.
- Condition: CustomerParty is present only when the buyer differs from the receiver.
- Options: (a, preferred) leave CustomerParty out.
- Needs decision: no

### utilities/05#F3 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- Why: SubscriberConsumption/Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption is "The consumption in case the consumption is from more than one supplier". The only supplier is Coastal State Water Company; both alternatives are present with identical totals, so their conditions contradict each other. (The city's sewage levy in invoice 06 is collected for a third party, not supplied by a second utility supplier.)
- Condition: Only the alternative that matches the number of suppliers is used.
- Options: (a) Consumption only; (b) SupplierConsumption only if a second supplier exists; (c) record as a finding on the UBL model that consumption lines are only reachable under SupplierConsumption.
- Needs decision: yes

### utilities/05#F4 · Medium · Language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; a locale is a language together with a region (e.g. en-XB), while "en" with listID ISO 639 is the language itself, already given in Language/ID. The element therefore repeats the language instead of stating the locale. Counted with `grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`: 213 examples carry the same pattern.
- Condition: LocaleCode, where present, is a locale (language and region, e.g. from a locale list or BCP 47), not a bare ISO 639 language code; otherwise it is absent.
- Options: (a, preferred) leave LocaleCode out (Language/ID says enough); (b) give a real locale such as en-XB with a fitting list.
- Needs decision: no

### utilities/05#F5 · Low · Whole shop's water booked to the garden department
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `6120`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Garden department`
- Why: AccountingCost is "The buyer's accounting cost code, applied to the UtilityStatement". The consumption point is the whole shop (`/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:Description` = `Shop, Lumeport`, meter "Water meter, shop"), not a garden department. Booking all of it to one department only makes sense if the garden department is the main user (plant watering) and the story says so; nothing in the statement or invoice 06 does.
- Condition: The accounting cost fits the consumption point (e.g. building costs of the shop), or the story explains why the garden department carries it.
- Options: (a) a building or facilities cost centre; (b) keep it and give the reason in the story. Preference: (a).
- Needs decision: yes

### utilities/05#F6 · Low · Receiver master data the statement does nothing with, and a buying office as its contact
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: A water consumption statement uses neither the receiver's logo reference, its online shop nor its photo-sharing profile; these look copied from master data. The contact is the "Buying office" with job title "Customer service officer" in "Sales": a buyer's purchasing office in a sales department, and in any case not the one who handles utility bills (facilities or accounts payable).
- Condition: The receiver carries only data this statement uses, and its contact handles utility bills, with name, title and department agreeing.
- Options: (a, preferred) drop logo, additional web site and social media profile; give a facilities or accounts-payable contact.
- Needs decision: no

### utilities/05#F7 · Low · Subscriber type of the utility item is "Water", the consumption point's is "Commercial"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `COM`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text" and SubscriberTypeCode "The code identifying for the service type". The example uses the utility type; by the element names the same subscriber has two types in one statement. Same in 01 and 03.
- Condition: Either consistent with the consumption point, or the service-type reading is recorded as a deliberate reading of UBL's inconsistent definitions.
- Options: (a) record the UBL definition inconsistency and keep; (b) leave both out of the utility item.
- Needs decision: yes

### utilities/05#F8 · Low · Filler descriptions
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: These say nothing the structured data next to them does not say (rule "no fillers").
- Condition: Each description carries information of its own, or is absent.
- Options: (a, preferred) leave them out.
- Needs decision: no

## Checked and consistent
- Meter: 4298 − 4212 = 86 m³ × constant 1 = all delivered, metered and consumed quantities; maximum flow 2.5 m³/h against an average of 86 m³ / 744 h ≈ 0.12 m³/h is plausible for a shop meter (own knowledge: a Q3 2.5 meter is a common small size).
- Amounts: 86 × 2.35 = 202.10; history 81 × 2.35 = 190.35 and 79 × 2.35 = 185.65; average quantity 82 m³ correct; tax exempt (drinking water) with 0.00 tax, consistent with the invoice.
- Parent reference CSWC-INV-26-0317 is 06-Invoice.xml; consumption line 1 matches invoice line 1 (86 m³, 202.10, price 2.35, meter CSW-W-55102, contract CSW-C-260118, exemption WATER).
- ConsumptionReportReference to February (79 m³) agrees with ConsumptionHistory[2].
- Consumption point address equals the receiver's postal address (Market Street 50, 38515 Lumeport), consistent with "Shop, Lumeport".
- check_ids.py: GLN 9522610900002 check digit correct.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: statement total 202.10 lacks the sewage levy of invoice 06 (36.12) — refuted, the levy is collected for the city (CollectionInvoiceLine), not part of the water supplier's consumption; the statement explains the supply.
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: water company of a state as SMALL — refuted, a small private water company serving one city is plausible.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID`: ID contains 38510 while the postal code is 38515 — refuted, the consumption point ID is the supplier's own identifier and need not contain the postal code.
