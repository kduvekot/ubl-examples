# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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

### utilities/05#F1 · High · The consumption average amount is this month's amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 82 m³.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `202.10`
- Why: AverageAmount is "The average monetary amount of the consumption". The three-month average (81 + 79 + 86) / 3 = 82 m³ is worth 82 × 2.35 = 192.70 XBL (the average of the amounts 190.35, 185.65 and 202.10 is 192.70 as well). 202.10 is March's amount (86 × 2.35).
- Condition: AverageAmount is the average amount of the months the description averages.
- Options: (a, preferred) 192.70; (b) drop AverageAmount.
- Needs decision: no

### utilities/05#F2 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`
- Why: SupplierConsumption is "The consumption in case the consumption is from more than one supplier"; Consumption covers "one and only one supplier". The shop has one water supplier and the statement carries both aggregates with identical totals.
- Condition: SupplierConsumption only where there is more than one supplier.
- Options: (a, preferred) remove it here; (b) a real second supplier in the story.
- Needs decision: yes

### utilities/05#F3 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: CustomerParty is "The buyer, if different from the receiver of the document." The receiver is Brightmarket Stores (same register ID 20410411).
- Condition: CustomerParty only when the buyer differs from the receiver.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/05#F4 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." "en" with listID ISO 639 is a language code and repeats Language/ID; a locale names language and region (e.g. en-XB, the form the world uses in languageID attributes elsewhere). The same value occurs 362 times in 213 examples (`grep -rc --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`, summed; files counted with `grep -rl`), so it is a world-wide pattern; it remains a finding here.
- Condition: LocaleCode holds a locale (language and region) from a locale list, or is absent.
- Options: (a, preferred) remove LocaleCode where only the language is known; (b) a locale such as en-XB with a list that defines it.
- Needs decision: no

### utilities/05#F5 · Medium · The subscriber identifier is the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-260118`
- Why: SubscriberID is "An identifier for the subscriber responsible for the consumption at this consumption point"; the value is the water supply contract's ID (`06-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:Description` = `Supply contract`).
- Condition: SubscriberID holds a subscriber (customer) identifier, distinct from the contract ID, or is absent.
- Options: (a, preferred) a customer number of the water company; (b) remove.
- Needs decision: no

### utilities/05#F6 · Low · SubscriberType on the utility item names the utility
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberType` = `Commercial`
- Why: The text is "Identification of the subscriber type"; the code twin is defined as "the service type". "Water" fits only the code's definition and differs from the subscriber type "Commercial" at the consumption point.
- Condition: Text and code describe one thing according to their definitions, or the UBL inconsistency is recorded.
- Options: (a) drop the text; (b) align and record the definition conflict.
- Needs decision: yes

### utilities/05#F7 · Low · Buyer's cost centre "Garden department" for the shop's water
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `6120`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Garden department`
- Why: AccountingCost is the buyer's cost code for the statement. The consumption point is "Shop, Lumeport", the whole shop's drinking water; booking it to the garden department is implausible unless the story says the garden department uses it. "Garden department" occurs as AccountingCost in 16 examples (`grep -rh --include='*.xml' -o '<cbc:AccountingCost>[^<]*' world/examples | sort | uniq -c`), Brightmarket's purchasing default.
- Condition: The cost centre fits the shop's utility costs, or is absent.
- Options: (a, preferred) a facilities/utilities cost centre of the shop.
- Needs decision: no

### utilities/05#F8 · Low · Receiver master data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:SocialMediaProfile/cbc:ID` = `10442197`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- Why: A water statement to Brightmarket uses none of its logo, online shop, social media profile, and its buying office (which buys goods for resale) is not the contact for utility bills.
- Condition: The receiver carries what the statement uses, with a contact for utility bills.
- Options: (a, preferred) remove them; use accounts payable or facility management.
- Needs decision: no

### utilities/05#F9 · Low · Descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- Why: Both repeat what the consumption point and the history Period already say (IND5).
- Condition: Removed or replaced by informative text.
- Options: (a, preferred) remove.
- Needs decision: no

## Checked and consistent
- ParentDocumentReference CSWC-INV-26-0317 → `06-Invoice.xml`, line 1: 86 m³ × 2.35 = 202.10, meter CSW-W-55102; statement issued after the invoice (11:55 vs 09:13).
- Meter: 4298 − 4212 = 86 m³, constant 1; 86 m³/month ≈ 2.8 m³/day, well under the meter's maximum flow of 2.5 m³/h.
- History: 81 × 2.35 = 190.35; 79 × 2.35 = 185.65; ConsumptionReportReference February 79 m³ agrees.
- Tax: exempt (drinking water), tax 0.00; consistent with the invoice's category E and reason WATER.

## Considered and refuted
- `06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `36.12`: the statement does not explain the sewage levy — refuted because the levy is collected for the city, not a consumption supplied by the sender, and a statement may explain only the supplier's own supply.
