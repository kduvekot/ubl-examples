# LLM review: 21-PurchaseReceipt.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/21-PurchaseReceipt.xml`, Git blob `7f75d1791cf92b3eb6f0f963657d0181e309ff88` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit bb7d002 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/21#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/21#F2 · High · Home delivery "for Saturday" requested on a Sunday
- XPath: `/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.`
- XPath: `/PurchaseReceipt/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-05-17`
- XPath: `/PurchaseReceipt/cac:SalesDocumentReference/cbc:ID` = `BM-DEL-26-0518-07`
- Why: the purchase is made on Friday 2026-05-15; the Saturday after is 2026-05-16. The requested delivery period starts on 2026-05-17, a Sunday. The sales document's number, which looks like Brightmarket's delivery number, carries yet another date (`0518`, 18 May). Note and structured delivery date contradict each other.
- Condition: the requested delivery date and the note name the same day.
- Options: (a, preferred) requested delivery on 2026-05-16 (the Saturday); (b) change the note to Sunday. In either case, a delivery number that encodes a date should encode that day.
- Needs decision: no

### retail/21#F3 · High · Promotion price valid for another period than the promotion
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-05-12`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2026-05-18`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:EndDate` = `2026-05-24`
- Why: the price is reduced for the "Spring garden promotion" (price change reason and discount reason), which 06-RetailEvent runs from 2026-05-11 to 2026-05-24, "for two weeks". The promotional price here is valid from 2026-05-12 to 2026-05-18, one week that starts a day late. The receipt and the retail event describe the same promotion with different periods.
- Condition: the validity of the promotional price equals the promotion period of 06-RetailEvent.
- Options: (a, preferred) 2026-05-11 to 2026-05-24; (b) if the price reduction in this store really runs for a shorter period, say so in the retail event.
- Needs decision: no

### retail/21#F4 · Medium · Language codes in LocaleCode
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/21#F5 · Low · A purchase line period of five years for a bench
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:StartDate` = `2026-05-15`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:EndDate` = `2031-05-15`
- Why: `PurchaseLinePeriod` is "A period to which this purchase line applies", e.g. a subscription or a season ticket. The purchase of a bench applies to no period; the five years match the frame warranty ("Five years on the frame against corrosion"), which is a different thing and already referenced (`VI-WARRANTY-B180`).
- Condition: the purchase line period is absent, or describes a period the purchase itself covers.
- Options: (a, preferred) drop it and leave the warranty to the warranty reference and the item's warranty information.
- Needs decision: no

### retail/21#F6 · Low · Payment and transaction numbers that encode another day
- XPath: `/PurchaseReceipt/cac:Payment/cbc:ID` = `BM-G2-26-0518-0047`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:TransactionID` = `TX-26-0518-773104`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:PaidDate` = `2026-05-15`
- Why: the payment at till G2 is made on 2026-05-15, but its identifiers carry `26-0518`, which reads as 18 May 2026, like the delivery number in F2. Identifiers built from a date should carry the date of the event they identify.
- Condition: date-coded identifiers of the payment carry the payment date (or are not date-coded).
- Options: (a, preferred) `…-26-0515-…`.
- Needs decision: no

### retail/21#F7 · Low · Customer's bank account and the retailer's buying office on a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the customer pays by debit card (card account given); the receipt does nothing with his current account, and a consumer's bank account on a till receipt is data copied from somewhere else. The seller's party contact is the buying office (with a job title and department that contradict its name), although the receipt already names the cashier and the point of sale's contact; for a consumer the store's customer service would be the contact.
- Condition: the receipt carries the customer's data it uses (name, delivery address, card) and a seller contact that fits a sale to a consumer.
- Options: (a, preferred) drop the person's financial account and use Brightmarket's customer service as the party contact (or drop it in favour of the point-of-sale contact).
- Needs decision: no

### retail/21#F8 · Low · Point of sale named after the company
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- Why: a location's name is the place; the store is identified elsewhere by its address and GLN `9522610900002`. The description (garden department, ground floor) is a place.
- Condition: the point of sale names the store (and may carry its GLN or address).
- Options: (a, preferred) "Lumeport store, Market Street" or similar, with the GLN.
- Needs decision: no

### retail/21#F9 · Low · Catalogue data on a consumer's receipt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CircularityProfile`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a till receipt identifies what was bought; the manufacturer's emissions, circularity data, load test and Urvania's customs tariff code are not used by it. The emission and repairability data may interest a consumer, but then as information the receipt deliberately gives, not as a copy of the catalogue item with its tariff codes.
- Condition: the item carries what the receipt needs, and anything more is there for a stated reason.
- Options: (a, preferred) identifiers, name, warranty and tax category; (b) keep the consumer-facing data (emissions, repairability) and drop the tariff and property data.
- Needs decision: no

## Checked and consistent
- Arithmetic: 749.00 − 10 % (74.90) = 674.10; tax 6.5 % × 674.10 = 43.82 (43.8165); tax-inclusive line 717.92; delivery charge 25.00; taxable 699.10 × 6.5 % = 45.44 (45.4415); total 699.10 + 45.44 = 744.54 = payable = paid amount.
- The regular price 749.00 and the discount 74.90 agree with 06-RetailEvent's promotional amount (74.90 off per bench).
- Standard rate `S` 6.5 % for a sale to a consumer, against the exempt resale in 18-Invoice: consistent tax story.
- Seller's item ID `BM-551210` is the buyer's item ID of 08, 12 and 17; GTIN `9520610000012` and account `XB64BLUM38010007251840` pass their check digits.
- Robin Ashdale and his residential address are described identically here and in 22-Order; the delivery address equals his postal address; the carrier is Brightmarket itself.

## Considered and refuted
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseReference/cbc:ID` = `VI-SF-02170`: suspected a serial number misused as a purchase reference — refuted: UBL defines it as "A reference to an object … to which this purchase line relates", and the bench's frame is that object.
- `/PurchaseReceipt/cac:PurchaseReference/cbc:ID` = `BM-LOYAL-0088127`: likewise a person's loyalty card, which the definition ("person") covers.
