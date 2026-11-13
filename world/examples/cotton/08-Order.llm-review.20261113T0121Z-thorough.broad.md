# LLM review: 08-Order.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/08-Order.xml`, Git blob `71ce9b04ed217222f38cfab91ff0f8de0f9cd595` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/08#F1 · Medium · Tax category "Services outside scope of tax" for an order of goods
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name[2]` = `Cotton lint, compressed bale`
- Why: as cotton/01#F2: `O` in UN/EDIFACT 5305 is "Services outside scope of tax"; the order is for cotton lint, goods. 17 examples use `O`.
- Condition: the subtotal carries a code whose meaning covers goods outside the scope of tax, or the deviation is recorded.
- Options: (preferred) one world-wide decision.
- Needs decision: yes

### cotton/08#F2 · Medium · Language code in `LocaleCode`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2: an ISO 639 language code in an element for a locale, repeating `Language/ID`.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/08#F3 · Low · "No general sales tax" typed as a tax on consumption
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:TaxTypeCode` = `CONSUMPTION`
- Why: the scheme is the absence of a sales tax, without an `ID`, yet it is classified as a consumption tax. A tax total of zero for a tax that does not exist tells the seller nothing (see cotton/01#F3); in the invoice 16 the same scheme has no type code.
- Condition: the order's tax total names a real scheme with a type that fits it, or the order carries no tax total.
- Options: (preferred) drop the tax total from the order (an anticipated total without tax suffices); or name the real scheme.
- Needs decision: yes

### cotton/08#F4 · Low · Order without a requested delivery date
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: the order states what, how much, at what price and on which terms, but not when the lint is to be shipped FOB Selanu. The seller has to deduce the date; the shipment followed on 2 March (13). An order's delivery period is information its purpose relies on.
- Condition: the order states a requested delivery (shipment) date or period.
- Options: (preferred) a requested delivery period in `Delivery`, e.g. loading in the first week of March.
- Needs decision: no

### cotton/08#F5 · Low · Requested invoice currency equal to the document currency
- XPath: `/Order/cbc:RequestedInvoiceCurrencyCode` = `XLC`
- XPath: `/Order/cbc:DocumentCurrencyCode` = `XLC`
- Why: requesting invoices in coral adds nothing when the order is in coral and nothing suggests another currency; it is a filler (IND5).
- Condition: the requested invoice currency is absent or differs from the document currency for a stated reason.
- Options: (preferred) drop it; or keep it if the mill, which pays from a Lume account (18), wants to make clear that it accepts invoices in coral, and say so.
- Needs decision: no

### cotton/08#F6 · Low · Purchasing contact described as a sales customer-service officer
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: as cotton/02#F3: the buyer's contact is named Purchasing but sits in Sales as a customer-service officer.
- Condition: name, title and department agree and fit a buyer.
- Options: (preferred) department Purchasing with a buyer's title.
- Needs decision: no

### cotton/08#F7 · Low · Item texts tagged as Bayvarran English
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: as cotton/02#F4: the seller's item text carries `en-XL` in the seller's documents (10, 11, 16) and `en-XB` here; the ginnery's address renderings likewise.
- Condition: the same text carries the same tag in every example.
- Options: (preferred) `en-XL` everywhere for the ginnery's texts.
- Needs decision: no

### cotton/08#F8 · Low · Classing results in the applicant's remarks
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: as cotton/02#F5: "Remarks by the applicant", but the text is the classer's result.
- Condition: the result is not carried as an applicant's remark.
- Options: (preferred) drop the remark.
- Needs decision: no

### cotton/08#F9 · Low · Origin area in `Region`, in `District` in the farm's address
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- Why: as cotton/02#F6.
- Condition: the north coast in the same element everywhere.
- Options: (preferred) `District`.
- Needs decision: no

### cotton/08#F10 · Low · Pack size given as a number of items for a bale of 227 kg
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: as cotton/02#F7; the order quantity 6129 kg is exactly 27 bales of 227 kg, but the number of bales is nowhere stated as a count.
- Condition: the bale weight is not carried as a count; if the bale count matters, it is stated as one.
- Options: (preferred) drop the pack elements and, if wanted, give 27 bales as a package quantity elsewhere.
- Needs decision: no

## Checked and consistent
- 6129 kg × 0.988 XLC/kg = 6055.452 = line, anticipated total and taxable amount; 6129 = 27 × 227.
- FOB Port of Selanu with the buyer's forwarder named fits a buyer who arranges main carriage; 09 (instructions to that forwarder), 13 ("Freight collect") and 17 (forwarder's freight invoice to the mill) follow it.
- 16 invoices exactly this line (`16-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0198`), quantity and price.
- The certificate quoted is signed 2026-02-20, before the order (2026-02-24).
- The 6129 kg of lint fit the 18000 kg of seed cotton delivered in 03 at a typical lint turnout of about 34 % (own knowledge).

## Considered and refuted
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`: place without an identifier — refuted: no example of the flow identifies the port of Selanu by code, so there is nothing to be consistent with.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate`: a lot certificate in an order — refuted: here the mill orders the classed lot itself (27 bales certified in 10), so the certificate identifies what is ordered.
