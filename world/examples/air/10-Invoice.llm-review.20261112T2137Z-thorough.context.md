# LLM review: 10-Invoice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/10-Invoice.xml`, Git blob `4f8e76fdb62682517ade76167e8a942e4bcac42e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/10#F1 · High · Freight "per kilogram chargeable weight" invoiced on the gross weight
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `81.6`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: The item description says the price applies per kilogram of chargeable weight. The air waybill the invoice refers to gives a chargeable weight of 96 kg (the volumetric weight of 0.576 m³); 81.6 kg is the gross weight. The invoiced quantity contradicts its own description and the referenced waybill: 81.6 × 6.8 = 554.88, while 96 × 6.8 = 652.80.
- Condition: the invoiced quantity is the quantity the description names, and agrees with the waybill.
- Options: (preferred) 96 kg chargeable weight and the amounts recalculated, as the description and the waybill agree on chargeable weight; or the description says gross weight, if the forwarder's tariff charges on gross weight.
- Needs decision: no

### air/10#F2 · Medium · LocaleCode holds a language code
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/10#F3 · Medium · A gate in AdditionalStreetName of the customer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street and has no place in the postal address an invoice is addressed to.
- Condition: no gate in a street-name element of the postal address.
- Options: (preferred) drop it.
- Needs decision: no

### air/10#F4 · Low · Reference to a statement of account that cannot exist yet
- XPath: `/Invoice/cac:StatementDocumentReference/cbc:ID` = `BF-SOA-26-05`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-15`
- Why: StatementDocumentReference is "A reference to a Statement associated with this document". BF-SOA-26-05 reads as the forwarder's statement of account for May 2026; on 15 May that statement has not been issued (a statement lists invoices after they are issued), and no example has this ID. An invoice cannot refer to a statement that will list it later.
- Condition: the invoice refers only to a statement that exists at its issue date, or carries no statement reference (the statement will refer to the invoice).
- Options: (preferred) drop the reference; or, if the world means a running account agreement, refer to that agreement as a contract instead.
- Needs decision: yes (whether the forwarder bills through a monthly statement)

### air/10#F5 · Low · "Airport-to-airport … road feeder included" does not match the carriage invoiced
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- Why: "Airport-to-airport" excludes carriage to or from the airports, while "road feeder included" says road legs are part of the service. The waybill shows only an air stage (Lumeport–Selanu, an ATR 72 freighter flight to an island), and a road feeder (a truck operated under a flight number) cannot serve an island destination. If the forwarder's pickup at Marrowdale is meant, it is a pickup, not an airport-to-airport service. Own knowledge of air-freight terms.
- Condition: the description matches the services invoiced and the carriage in the waybill.
- Options: (preferred) "Airport-to-airport air freight per kilogram chargeable weight", with the pickup as a separate line if it is charged; or describe the service as door-to-airport including pickup.
- Needs decision: no

### air/10#F6 · Low · Outbound freight booked as "Stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: AccountingCost is "The buyer's accounting code, applied to the Invoice as a whole". The buyer of this invoice, Lumeway Distribution, pays the air freight for goods it sells CPT to Velumi Trading (01-OrderChange.xml); this is outbound freight, a distribution cost, not a purchase of stock. The value fits the purchase invoices of the goods, not the freight.
- Condition: the accounting cost names what the buyer books this freight to, consistent with the delivery terms.
- Options: (preferred) an outbound freight or distribution cost code; or none, if the forwarder does not know the buyer's code.
- Needs decision: no

### air/10#F7 · Low · The forwarder invoices against the carrier's waybill, not its own house waybill
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- Why: According to the waybill, Bayforth consolidated the consignment under its own house waybill BF-HAWB-26-0918 within Kelaro's waybill. The forwarder's contract with Lumeway is then the house waybill; the master waybill is the forwarder's contract with the airline. The invoice refers to the master only, with no document type saying what the reference is. (If the consolidation in 04 is dropped, see the review of that example, the reference is right and only the document type is missing.)
- Condition: the invoice refers to the transport document between Bayforth and Lumeway, with its kind stated.
- Options: (preferred) settle the consolidation question in 04 first; then refer to the house waybill (if consolidated) or keep KXL-WB-26-0325 with a DocumentTypeCode.
- Needs decision: no

## Checked and consistent
- AdditionalDocumentReference KXL-WB-26-0325 resolves to 04-Waybill.xml; Delivery/Consignment LD-CS-26-0324 and carrier Kelaro Air Cargo agree with it.
- Supplier Bayforth Forwarding and customer Lumeway Distribution are the forwarder and the consignor that gave the forwarding instructions (03-ForwardingInstructions.xml); the invoice (15 May) follows the arrival (14 May, 09-TransportationStatus.xml).
- Price × quantity: 6.8 × 81.6 = 554.88; penalty 1.5 % of 554.88 = 8.32; due date 14 June = issue date + 30 days, as the payment terms note says.
- RF reference RF66BFINV260331 and the IBAN-like account pass their checks (check_ids.py).

## Considered and refuted
- `/Invoice/cbc:InvoiceTypeCode` = `380`: suspected a goods code for a service invoice — refuted: UN/EDIFACT 1001 code 380 "Commercial invoice" covers services as well as goods.
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`: suspected redundancy with AccountingCustomerParty — refuted: the buyer of the freight service and the accounting customer are the same company, and stating both is legitimate.
