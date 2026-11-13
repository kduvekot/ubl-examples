# LLM review: 21-PurchaseReceipt.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/21-PurchaseReceipt.xml`, Git blob `7f75d1791cf92b3eb6f0f963657d0181e309ff88` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/21#F1 · High · Home delivery "booked for Saturday", requested for a Sunday
- XPath: `/PurchaseReceipt/cbc:Note` = `Home delivery booked for Saturday.`
- XPath: `/PurchaseReceipt/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-05-17`
- XPath: `/PurchaseReceipt/cbc:PurchaseDate` = `2026-05-15`
- Why: The purchase is on Friday 2026-05-15; the Saturday after it is 2026-05-16, but the requested delivery period starts on 2026-05-17, a Sunday (calculated). The note and the structured delivery date contradict each other.
- Condition: the delivery date and the note name the same day.
- Options: (a, preferred) StartDate `2026-05-16`, keeping 09:00–12:00 and the note; (b) note "booked for Sunday", if the store delivers on Sundays.
- Needs decision: no

### retail/21#F2 · High · Emission value is not factor × base
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/21#F3 · Low · Identifiers of the sale and the payment encode 18 May, the purchase is on 15 May
- XPath: `/PurchaseReceipt/cac:SalesDocumentReference/cbc:ID` = `BM-DEL-26-0518-07`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:ID` = `BM-G2-26-0518-0047`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:TransactionID` = `TX-26-0518-773104`
- XPath: `/PurchaseReceipt/cac:Payment/cbc:PaidDate` = `2026-05-15`
- Why: Three identifiers built from a date (`26-0518`) all point to 2026-05-18, while the purchase, the payment and the receipt are all dated 2026-05-15 11:42, and the requested delivery is on 2026-05-17. A till-generated payment ID and a card transaction ID dated three days after the payment would make a reader doubt which day the sale took place. (The identifiers are opaque in UBL; the issue is only that they look like dates that do not fit.)
- Condition: identifiers that contain a date contain the date of the event they identify, or contain no date.
- Options: (a, preferred) `…-26-0515-…` in the three identifiers; (b) numbers without a date part.
- Needs decision: no

### retail/21#F4 · Low · Point-of-sale location named after the company, without the GLN of the garden department
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Garden department, ground floor`
- XPath: `22-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: The location's name is the company plus a city, not the store; the garden department of the Lumeport store has GLN `9522610900026` in 22 and in `furniture/06-ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:ID` = `9522610900026`.
- Condition: the point-of-sale location names the store and carries its (department's) GLN.
- Options: Location/ID `9522610900026`, name "Lumeport store, garden department".
- Needs decision: no

## Checked and consistent
- Purchase on 2026-05-15 lies within the promotion 2026-05-11 to 2026-05-24 (06); "Promotion price" 674.10 = 749 − 74.90, the 10 % of 06.
- Purchase, transaction, payment and issue all at 2026-05-15 11:42.
- Requested delivery window 09:00–12:00 is after the purchase; delivery address Gull Lane 57 is the customer's address used again in 22; the carrier is the store itself (home delivery charge 25.00).
- Item `BM-551210` is the store's own number for the bench (as buyer's item ID in 17); GTIN and manufacturer data agree with 02.
- Stock: 3 (07) + 23 accepted (17) = 26 benches before the promotion; one sold here.
