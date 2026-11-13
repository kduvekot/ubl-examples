# LLM review: 21-PurchaseReceipt.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/21-PurchaseReceipt.xml`, Git blob `7f75d1791cf92b3eb6f0f963657d0181e309ff88` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/21#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", `ValueBaseMeasure` "The base quantity to which the value factor applies". Recomputed: 0.82 × 1 EA = 0.82 ≠ 96 kg; 96 / 0.82 = 117.1. Same triple in 39 XML files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a, preferred) drop factor and base; the footprint itself may interest a consumer (context); (b) a factor and activity that give 96 kg.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F2)

### retail/21#F2 · High · Home delivery "booked for Saturday", requested for a Sunday
- XPath: `/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.`
- XPath: `/PurchaseReceipt/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-05-17`
- XPath: `/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`
- Why: the purchase is on Friday 2026-05-15; the Saturday after it is 2026-05-16. The requested delivery period ("The period requested for delivery") starts on 2026-05-17, a Sunday, 09:00–12:00 (weekdays recomputed in the merge). Attempted refutation: "Saturday" could be a later Saturday (2026-05-23), but the period has no end date other than the same day's 12:00, so it names 17 May only. The note and the structured delivery date contradict each other.
- Condition: the requested delivery date and the note name the same day.
- Options: (a, preferred) start date 2026-05-16, keeping 09:00–12:00 and the note; (b) the note says Sunday, if the store delivers on Sundays.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### retail/21#F3 · High · The promotion price is valid for another period than the promotion
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-05-12`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2026-05-18`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceChangeReason` = `Spring garden promotion`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:EndDate` = `2026-05-24`
- XPath: `06-RetailEvent.xml:/RetailEvent/cbc:Description` = `Ten per cent off garden furniture for two weeks.`
- Why: `Price/ValidityPeriod` is the period during which this price is valid. The price is reduced for the "Spring garden promotion" (price change reason and allowance reason), which 06-RetailEvent runs from 2026-05-11 to 2026-05-24, "for two weeks". The promotional price here is valid from 2026-05-12 to 2026-05-18: one week, starting a day late. Attempted refutation: the money and logistics parts checked that the purchase date lies within the promotion (it does, and within both periods), and a store may run a shorter price than the event; but the receipt names the same promotion, with the same 10 % (74.90 off 749.00 = 06's promotional amount 74.90), so the two documents describe one object with two periods. Verified against the XML.
- Condition: the validity of the promotional price equals the promotion period of 06-RetailEvent, or the retail event states the shorter price period.
- Options: (a, preferred) 2026-05-11 to 2026-05-24; (b) if the price really runs for a shorter period in this store, say so in the retail event.
- Needs decision: no
- From: broad (F3)

### retail/21#F4 · Medium · A language code in LocaleCode
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 364 occurrences in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F4), parties (F1), context (F3, the LocaleCode half)

### retail/21#F5 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle system boundary from another list (39 XML files, `grep -rl --include='*.xml' 'CRADLETOGATE' world/examples | wc -l`). TC write-up candidate.
- Condition: no system-boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it and record the missing element for the TC write-up.
- Needs decision: no
- From: context (F3, the FullnessIndicationCode half)

### retail/21#F6 · Medium · Lifecycle stage "Manufacturing" for an emission from ore to factory gate
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; the description covers EN 15804 stages A1–A3 (own knowledge), the code only manufacturing. Added by the merge, aligned with retail a/b and road/rail/air.
- Condition: the code covers the stages the description names, or is absent.
- Options: (a, preferred) omit the code; (b) one emission per stage.
- Needs decision: no
- From: added by the merge

### retail/21#F7 · Low · Identifiers of the sale and the payment encode 18 May; the purchase is on 15 May
- XPath: `/PurchaseReceipt/cac:SalesDocumentReference/cbc:ID` = `BM-DEL-26-0518-07`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:ID` = `BM-G2-26-0518-0047`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:TransactionID` = `TX-26-0518-773104`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:PaidDate` = `2026-05-15`
- Why: three identifiers built from a date (`26-0518`) point to Monday 2026-05-18, while purchase, payment and receipt are dated 2026-05-15 11:42 and the delivery is requested for the 17th (F2); in this flow such numbers follow the date (e.g. `BM-SIG-26-0424` on the order of 2026-04-24). A till payment ID and card transaction ID dated three days after the payment make a reader doubt which day the sale took place. `SalesDocumentReference` is moreover "A reference to the sales document to which this purchase receipt is related"; `BM-DEL-…` reads as a delivery note or booking rather than a sales document, and the reference does not say which (context). Identifiers are opaque in UBL; the issue is only that they look like dates that do not fit.
- Condition: identifiers that encode a date encode the date of their event, or no date; the sales document reference says what it refers to.
- Options: (a, preferred) `…-26-0515-…` in the three identifiers, and a typed reference to the delivery booking (or none); (b) numbers without a date part.
- Needs decision: no
- From: broad (F6, and F2 for the delivery number), money (F1), logistics (F3), context (F6)

### retail/21#F8 · Low · A till signature without signature content
- XPath: `/PurchaseReceipt/cac:Signature/cbc:ID` = `BM-SIG-POS-G2`
- Why: the signature (presumably the till's fiscal signature) has only an ID and a signatory, no value or method, so it signs nothing. The earlier flows and retail a/b treat this convention (137 of 147 Signature aggregates, air merge count, lxml) as one decision.
- Condition: the signature carries what makes it one, or is absent.
- Options: (a, preferred) complete it if the world's tills sign receipts (a fiscal signature has a business reason on a till receipt); (b) drop it.
- Needs decision: yes
- From: context (F7, part)

### retail/21#F9 · Low · The retailer's buying office as its contact on a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: Brightmarket sells to a consumer here; a sales customer-service officer could fit, but the contact is named "Buying office" with the address buying@brightmarket.example, which serves Brightmarket's own purchasing; name, job title and department contradict each other. The receipt already names the cashier and the point of sale's contact.
- Condition: the seller's contact fits a sale to a consumer, with consistent name, job title and department.
- Options: (a, preferred) Brightmarket's customer service as contact; (b) drop it in favour of the point-of-sale contact.
- Needs decision: no
- From: broad (F7, part), parties (F3)

### retail/21#F10 · Low · The consumer's bank account on a receipt paid by debit card
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `55`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`
- Why: the payment is a debit card payment at the till, identified by the masked card number and issuer. The customer's full current account, with branch and bank address, is used for nothing on the receipt (no refund, no direct debit), and a till does not learn the account behind a card (own knowledge of card payments). It looks copied from the person's master data; the same account is in 22-Order, also paid by card, and in four utilities examples (`grep -rl --include='*.xml' 'XB64BLUM38010007251840' world/examples`: 7 files), where the utilities merges kept it as copied data except where a refund used it.
- Condition: the receipt carries the consumer's financial account only if the purchase is paid from or refunded to it by transfer.
- Options: (a, preferred) drop the person's financial account; (b) keep it with a reason, e.g. a refund by transfer promised on the receipt.
- Needs decision: no
- From: broad (F7, part), money (F2), parties (F4), context (F4)

### retail/21#F11 · Low · Point of sale named after the company
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Garden department, ground floor`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: `PointOfSaleLocation` is "The location of the point of sale"; its name is the company plus a town, without the store's address or GLN, while the garden department of the Lumeport store has GLN `9522610900026` in 22 and in `furniture/06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:ID` = `9522610900026`. The parties part refuted this (a point of sale is usually called by the store's name, and the description gives the department); the merge keeps it as Low, as the earlier flows did for locations named after companies, with the weight on the missing identifier.
- Condition: the point-of-sale location identifies the store (name of the place, GLN or address).
- Options: (a, preferred) Location ID `9522610900026` and a place name such as "Lumeport store, garden department"; (b) keep the name and add the GLN.
- Needs decision: no
- From: broad (F8), logistics (F4), context (F7, part); parties (Considered and refuted)

### retail/21#F12 · Low · The warranty period as the purchase line's period
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:StartDate` = `2026-05-15`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseLinePeriod/cbc:EndDate` = `2031-05-15`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- Why: `PurchaseLinePeriod` is "A period to which this purchase line applies", e.g. a subscription or season ticket. The purchase of a bench applies to no period; the five years are the frame warranty, which the item's warranty information and the reference `VI-WARRANTY-B180` already give, and nothing on the receipt says the period is the warranty.
- Condition: the purchase line period is absent, or describes a period the purchase itself covers.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: broad (F5), context (F5)

### retail/21#F13 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: the GTIN of Valdara's bench is under the company prefix 9520610, which across the world is Lumeway's (its GLN `9520610900008` and its SSCCs, e.g. `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:ID` = `095206102170000038`); under GS1 rules the brand owner allocates the GTIN from its own prefix (own knowledge). The parties part raised it in 17, 18 and 19, not here; the merge adds it for the same item.
- Condition: Valdara's GTINs and Lumeway's keys are under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a prefix of Valdara's own; (b) state the distributor's allocation in the story.
- Needs decision: yes
- From: added by the merge

### retail/21#F14 · Low · The world item number has the form and check digit of a GTIN
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: twelve digits with a valid GS1 check digit (7, computed in the merge), so it reads as a GTIN-12 with prefix 07 (US/Canada, own knowledge). Added by the merge, as retail a, rail, road and plastics.
- Condition: the world item number cannot be mistaken for a real GTIN, or its form is recorded as deliberate.
- Options: (a, preferred) a format that is not a valid GTIN; (b) record the choice in the scheme.
- Needs decision: yes
- From: added by the merge

### retail/21#F15 · Low · Catalogue data on a consumer's receipt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a till receipt identifies what was bought; the load test, dimensions and Urvania's customs tariff code are not used by it. The context part refuted the footprint and repairability as legitimate consumer information handed over with the purchase; the merge accepts that for those two and keeps the finding for the rest (tariff and property data), so the preferred option changes accordingly.
- Condition: the item carries what the receipt needs, and anything more is there for a stated reason.
- Options: (a, preferred) keep the consumer-facing data (emission, repairability) and drop the tariff and property data; (b) identifiers, name, warranty and tax category only.
- Needs decision: no
- From: broad (F9); context (Considered and refuted)

## Checked and consistent
- Arithmetic (redone): 749.00 − 10 % (74.90) = 674.10 = line extension; line tax 6.5 % × 674.10 = 43.8165 → 43.82, tax-inclusive line 717.92 = tax-inclusive price; delivery charge 25.00 at 6.5 %; taxable 699.10 × 6.5 % = 45.4415 → 45.44; 699.10 + 45.44 = 744.54 = payable = paid.
- The discount 74.90 and 10 % agree with 06-RetailEvent's promotional amount; purchase date 2026-05-15 lies within 06's promotion (and within the price's own validity).
- Standard rate `S` 6.5 % for a consumer sale, against the exempt resale in 18; the same rate in 22.
- Seller's item ID `BM-551210` is the buyer's item ID of 08, 12 and 17; grey variant as delivered in 12; GTIN and account pass `check_ids.py` (rerun).
- Card: debit (55, DEBIT), issued by the customer's bank BLUMXBLX, PAN masked, holder `R ASHDALE`, status approved.
- Robin Ashdale and his residential address are described identically here and in 22; the delivery address is his postal address; the carrier is Brightmarket itself, charging home delivery.
- Stock: 3 (07) + 23 accepted (17) = 26 benches before the promotion (logistics).

## Considered and refuted
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:PurchaseReference/cbc:ID` = `VI-SF-02170`: a serial number as purchase reference — refuted, the definition names objects to which the purchase line relates, and the frame is one (from broad and context).
- `/PurchaseReceipt/cac:PurchaseReference/cbc:ID` = `BM-LOYAL-0088127`: a loyalty card — refuted, the definition covers a person's card (from broad).
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:SocialMediaProfile`, `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalWebSite`, `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID`: copied master data — refuted, a shop's receipt carries its logo, online shop and social media for the customer (from parties; as the packaging merge).
- `/PurchaseReceipt/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`: the store as its own carrier — consistent, home delivery is its own service, charged on the receipt (from parties).
- `/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:HolderName` = `R ASHDALE`: consistent with the customer (from parties).
- `/PurchaseReceipt/cac:CashierContact/cbc:Name`: a personal first name — refuted, a cashier is a person and receipts commonly show the first name (from context).
- `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`: refuted by the parties part (the store's usual name); the merge disagrees and keeps F11 (from parties).
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric`: full product data on a consumer receipt — refuted by the context part for footprint and repairability; accepted for those, the rest kept as F15 (from context).

## Refuted in the merge
### parties/F2 · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- The part's finding: UBL defines `CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount and the value is a sum in XBL; a conflict between definition and data type for the TC write-up. Condition: share capital no longer in `CorporateStockAmount`, or recorded as a finding against the definition and kept on purpose. Options: record it and keep it where a document needs it; keep it here. Needs decision: yes.
- Refuted because: this is the issuer's own receipt, a business document on which company law commonly requires the issuer's share capital (the part's own option keeps it), so the value is not copied data here; and an Amount-typed element can hold nothing but an amount, so the example uses the element the only way its type allows. The definition conflict belongs in the TC write-up, as noted in the copied-master-data findings of 15 to 20; it needs no change or decision in this example.

## Changed in the merge
- context/F3 → F4 and F5: split (LocaleCode / FullnessIndicationCode).
- F6 (MANUFACTURING), F13 (GTIN prefix) and F14 (world item number): added by the merge, aligned with retail a/b and 17–19.
- broad/F6, broad/F2 (delivery number), money/F1, logistics/F3, context/F6 → F7: grouped; context's "BM-DEL is not a sales document" folded in.
- context/F7 → F8 and F11: split (signature / point of sale); the signature set to "Needs decision: yes", aligned with retail a/b; preferred option "complete" because a fiscal till signature has a reason on a receipt.
- broad/F7 → F9 and F10: split (contact / bank account), grouped with parties/F3 and with money/F2, parties/F4, context/F4.
- broad/F9 → F15: preferred option changed to the broad part's option b, following the context part's refutation for footprint and repairability.

## Outside this review
- Whether Brightmarket's 26 benches are enough for the promotion (stock across documents) is a capacity question.
