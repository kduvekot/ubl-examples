# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit c959f36 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/17#F1 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2: an ISO 639 language code in an element for a locale, repeating `Language/ID`.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/17#F2 · Low · Forwarder bills the sea freight that the bill of lading leaves to be collected
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- XPath: `13-BillOfLading.xml:/BillOfLading/cbc:Note` = `Freight collect.`
- Why: "Freight collect" on the carrier's bill of lading means the carrier collects the freight at destination, normally from the consignee (the mill). The forwarder here invoices the mill for the same port-to-port sea freight. Either the forwarder pays the carrier (then the carrier's bill is prepaid or collect from the forwarder) or the mill pays the carrier; as written, the mill could be asked twice.
- Condition: the bill of lading's freight terms and this invoice describe one payer of the carrier's freight.
- Options: (preferred) make clear that the forwarder pays the carrier (bill of lading freight payable by Bayforth at Lumeport, or prepaid by the forwarder) and bills the mill; or let the mill pay the carrier and make this invoice the forwarder's fee only.
- Needs decision: yes

### cotton/17#F3 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the accounting supplier's contact is its operations export desk, the accounting customer's a "Purchasing" contact placed in sales; questions about an invoice go to the parties' accounts functions, and the customer's name and department contradict each other (as cotton/02#F3).
- Condition: the accounting parties' contacts handle billing, with names and departments that agree.
- Options: (preferred) accounts receivable / payable contacts; or no contacts.
- Needs decision: no

### cotton/17#F4 · Low · The carrier's tax registration in a delivery block
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- Why: the carrier is named to identify the carriage billed; it is not a party to this invoice's tax, and its tax registration (and full legal data) looks copied from master data.
- Condition: the carrier is identified without data the invoice does not use.
- Options: (preferred) identification and name only.
- Needs decision: no

## Checked and consistent
- 1 × 2950 XBL = 2950.00 line, totals and taxable amount; tax 0 under exemption "Service to a business".
- Due 2026-03-04 + 30 days = 2026-04-03, as "30 days net"; penalty 1.5 % × 2950.00 = 44.25 XBL; penalty period starts the day after the due date and lasts one month.
- "One 40-foot container" agrees with the 3750 kg tare in the VGM 12; the bill of lading 13 and consignment LTM-CS-26-0201 resolve; FOB in 08 makes the mill the party that pays the main carriage.
- Payee account `XB40BLUM38020502618225` passes its check digits; `RF08BFINV260211` passes.

## Considered and refuted
- `/Invoice/cbc:AccountingCost`: "Raw cotton" for sea freight — refuted: freight inward is commonly booked to the cost of the raw material (landed cost).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason`: an exemption for a transaction rather than a party status — refuted: here it is the transaction's exemption under the state sales tax, which is what the tax category describes.

## Outside this review
- No remittance advice for this invoice exists in the flow; whether it is paid is not shown (not required).
