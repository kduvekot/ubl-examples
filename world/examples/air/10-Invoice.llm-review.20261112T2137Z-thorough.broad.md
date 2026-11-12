# LLM review: 10-Invoice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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

### air/10#F1 · High · Billed "per kilogram chargeable weight" on the gross weight instead of the chargeable weight
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `81.6`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: The item says the price applies per kilogram of chargeable weight, and the waybill gives the chargeable weight as 96 kg (volumetric weight of 0.576 m³). The invoice bills 81.6 kg, which is the gross weight. Either the quantity or the description is wrong: 96 × 6.8 = 652.80, against the 81.6 × 6.8 = 554.88 billed.
- Condition: the invoiced quantity is the weight the description names, and it agrees with the waybill. All amounts (line, tax subtotal, totals, penalty) follow from it.
- Options: (a) 96 kg chargeable weight, line 652.80 and the penalty recalculated (1.5 % = 9.79) (preferred: chargeable weight is how air freight is billed); (b) keep 81.6 kg and change the description to gross weight.
- Needs decision: no

### air/10#F2 · Medium · LocaleCode holds a language code
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/10#F3 · Low · The buyer's accounting text "Stock purchases" for an outbound freight cost
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: The buyer here is Lumeway. The freight it pays under CPT is the cost of delivering goods it *sold* to Velumi (`01-OrderChange.xml`), a selling or distribution cost, not a purchase of stock. "Stock purchases" fits Lumeway's purchases from its manufacturer, not this invoice.
- Condition: the buyer's accounting code and text fit a freight cost on a sale.
- Options: e.g. "Outbound freight" with a matching code.
- Needs decision: no

### air/10#F4 · Low · Statement reference to a statement that does not exist (yet)
- XPath: `/Invoice/cac:StatementDocumentReference/cbc:ID` = `BF-SOA-26-05`
- Why: StatementDocumentReference is "A reference to a Statement associated with this document". No example has this ID, and a May statement of account cannot exist on 15 May if it covers the month. If it is meant as "this invoice will be on the May statement", the reference anticipates a future document, and the invoice does nothing with it.
- Condition: the reference points to an existing statement, or is absent.
- Options: remove it (preferred), or add the statement to the flow.
- Needs decision: no

### air/10#F5 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact for questions about this invoice is the forwarder's export desk (an operations planner), and the accounting customer's contact is Lumeway's customer service in Sales. For the parties of an invoice, accounts receivable and accounts payable are the roles concerned.
- Condition: the accounting parties' contacts are the ones who handle invoices and payments.
- Options: e.g. "Accounts receivable" / "Accounts payable" contacts.
- Needs decision: no

## Checked and consistent
- Arithmetic: 81.6 × 6.8 = 554.88 = line = LineExtensionAmount = TaxExclusive = TaxInclusive = Payable. Tax 0.00 on 554.88 (category E, 0 %). Penalty 1.5 % × 554.88 = 8.3232 → 8.32. Due date 2026-06-14 = issue date + 30 days ("30 days net"), and the penalty period starts on 15 June.
- Payment: RF66BFINV260331 (RF check digits OK) is the same in PaymentID and InstructionNote. The IBAN-like account XB40BLUM38020502618225 passes its check, and its bank code BLUM and branch 380205 match the bank `BLUMXBLX` and the branch given. The account holder Bayforth Forwarding Ltd is the supplier.
- Parties: under CPT the seller Lumeway pays the main carriage, so Bayforth billing Lumeway is right. Consignment `LD-CS-26-0324` and carrier Kelaro match `04-Waybill.xml`, and `KXL-WB-26-0325` resolves to it.
- Tax: an exempt service to a business (SVCB2B, supply type SERVICES) in the issuer's state tax scheme is consistent in the line and the subtotal.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`: "road feeder" with no road leg in the waybill. Refuted because the forwarder's pickup at Lumeway (`03-ForwardingInstructions.xml`, pickup by Bayforth) is the road leg to the airport.
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`: reference by ID only. Refuted because it resolves, and the consignment and carrier in the same invoice make clear it is the air waybill.
- `/Invoice/cbc:InvoiceTypeCode` = `380`: a commercial invoice for a service. Refuted because 380 covers goods and services.
