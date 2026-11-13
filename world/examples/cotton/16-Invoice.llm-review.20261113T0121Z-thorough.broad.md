# LLM review: 16-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/16-Invoice.xml`, Git blob `50bd624d3511a103ce29142147e25386c48bed58` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/16#F1 · High · "45 days net" with a due date 30 days after the invoice
- XPath: `/Invoice/cbc:IssueDate` = `2026-03-02`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-01`
- XPath: `/Invoice/cbc:DueDate` = `2026-04-01`
- Why: 45 days after 2 March 2026 is 16 April 2026; 1 April is 30 days. The terms text and the three due dates (invoice, payment means, payment terms) contradict each other. The same terms ID and text in 04 give the correct 45-day date (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-03-24`, 45 days after 7 February).
- Condition: the terms text and the due dates agree.
- Options: (preferred) due date 2026-04-16 in all three places, if the ginnery's standard 45 days apply; or "30 days net" if the mill has 30-day terms (the remittance on 29 March fits either).
- Needs decision: no

### cotton/16#F2 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: as cotton/01#F2: `O` of UN/EDIFACT 5305 means "Services outside scope of tax"; the line is an export of cotton lint. 17 examples use `O`.
- Condition: a code whose meaning covers goods outside the scope of tax, or the deviation recorded.
- Options: (preferred) one world-wide decision.
- Needs decision: yes

### cotton/16#F3 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/16#F4 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: as cotton/01#F3.
- Condition: the zero tax total names a real scheme, or is absent.
- Options: (preferred) one decision for the nine examples with this name.
- Needs decision: yes

### cotton/16#F5 · Low · Export invoice without delivery terms or shipment
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`
- XPath: `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: the commercial invoice of an export sale is the document customs and the buyer use to see what was delivered on which terms (own knowledge of export practice). It gives neither the Incoterm of the order (FOB Selanu) nor the date of shipment or the bill of lading (13, issued the same morning), although the import value in 15 is derived from it.
- Condition: the invoice states the delivery terms and the delivery (shipment) it bills.
- Options: (preferred) `DeliveryTerms` FOB port of Selanu and a delivery with the shipment date or a reference to the bill of lading TOL-BL-26-0206.
- Needs decision: no

### cotton/16#F6 · Low · Payment currency equal to the document currency
- XPath: `/Invoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/Invoice/cbc:DocumentCurrencyCode` = `XLC`
- Why: a payment currency equal to the document currency adds nothing (filler); the mill pays from a Lume account (18), but in coral, the invoice currency.
- Condition: the payment currency is absent or differs from the document currency.
- Options: (preferred) drop it; or keep it with a note that the mill must pay in coral although its account is in Lume.
- Needs decision: no

### cotton/16#F7 · Low · The buyer's contact is its purchasing desk in sales
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: as cotton/02#F3; for the accounting customer, accounts payable would be expected.
- Condition: name, title and department agree and fit the accounting customer.
- Options: (preferred) an accounts-payable contact.
- Needs decision: no

### cotton/16#F8 · Low · Classing results in the applicant's remarks
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as cotton/02#F5.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark.
- Needs decision: no

### cotton/16#F9 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: as cotton/02#F6.
- Condition: the north coast in the same element everywhere.
- Options: (preferred) `District`.
- Needs decision: no

### cotton/16#F10 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: as cotton/02#F7.
- Condition: the bale weight is not carried as a count.
- Options: (preferred) drop the pack elements.
- Needs decision: no

## Checked and consistent
- 6129 kg × 0.988 XLC/kg = 6055.452 = line, tax-exclusive, tax-inclusive and payable amount; tax 0.
- Order 08 resolves: same line, quantity and price; order line 1.
- The remittance advice 18 pays exactly 6055.452 XLC on 29 March, quoting `RF46SCGINV260210` (check digits pass) into the payee account `XL31BSEL0020004922263` (check digits pass), the ginnery's account also in 06.
- Shared charges (`SHAR`) fit a cross-border transfer.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode`: the buyer's cost code on the seller's invoice — refuted: the definition is "The buyer's accounting code", which the seller may quote from the order (08 gives the same code).
