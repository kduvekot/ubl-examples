# LLM review: 18-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/18-Invoice.xml`, Git blob `4c83015ab6e72109b8aa59490284886f5aa405ef` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 44b84c0 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/18#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/18#F2 · High · Invoices 24 benches while referring to the receipt that accepted 23
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `24`
- XPath: `/Invoice/cac:InvoiceLine/cac:ReceiptLineReference/cac:DocumentReference/cbc:ID` = `BS-RA-26-0235`
- XPath: `/Invoice/cbc:IssueTime` = `15:52:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`
- Why: the invoice line refers to receipt line 1 of 17-ReceiptAdvice, issued half an hour earlier (15:21), which records 23 benches received and 1 refused, with a credit requested. The invoice nevertheless bills 24 benches (12480.00 before the promotion allowance). Referring to a receipt and invoicing more than it accepted contradicts it; the credit note 19 then corrects the invoice two days later, which would not be needed if the invoice followed the receipt it cites.
- Condition: the invoiced quantity agrees with the receipt the invoice refers to, or the invoice does not refer to that receipt (and the credit note then corrects the invoice for the refused bench).
- Options: (a) invoice the 23 accepted benches, and drop or rethink 19-CreditNote; (b, preferred, keeps the flow) remove the receipt references from the invoice (the invoice is based on the despatch advice, and the receipt arrives with the credit request), so that 19 credits the refused bench against it.
- Needs decision: yes

### retail/18#F3 · High · Lead time in the pricing reference contradicts the catalogue
- XPath: `/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `3`
- Why: `PricingReference/OriginalItemLocationQuantity` refers to the original terms (location, quantity, price) under which the item was priced, i.e. those of the catalogue the order refers to. The catalogue line for the bench gives a lead time of 3 days; the invoice says 5. A lead time also does not bear on the invoiced price; the element carries nothing the invoice uses except this contradiction.
- Condition: the pricing reference agrees with the catalogue line it reflects, or is absent.
- Options: (a, preferred) drop the pricing reference; (b) give the catalogue's price terms (price 520 per each, lead time 3 days).
- Needs decision: no

### retail/18#F4 · Medium · Language codes in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/18#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/18#F6 · Low · Tax point date after delivery and invoice, without a reason
- XPath: `/Invoice/cac:InvoiceLine/cbc:TaxPointDate` = `2026-05-08`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: `TaxPointDate` is the date on which the tax becomes due for this line. The goods were delivered and invoiced on 2026-04-30; nothing in the flow happens on 2026-05-08 (the promotion starts on 2026-05-11, payment is due on 2026-05-30). A tax point eight days after both delivery and invoice needs a rule of Bayvarra's state sales tax that the document does not show; with an exempt supply it has no effect on the amounts.
- Condition: the tax point date follows from an event the flow shows (delivery, invoice, payment) under the world's tax rules, or is absent.
- Options: (a, preferred) drop it (the supply is exempt) or set it to the delivery date; (b) keep 2026-05-08 if Bayvarra's rules make it so, and record the rule in the story.
- Needs decision: yes

### retail/18#F7 · Low · Line-level payment terms that repeat the header, and an unexplained line reference
- XPath: `/Invoice/cac:InvoiceLine/cac:PaymentTerms/cbc:Note` = `The promotion stock is paid with the invoice, 30 days net.`
- XPath: `/Invoice/cac:InvoiceLine/cac:DocumentReference/cbc:ID` = `LD-DS-B180`
- Why: the line's payment terms say what the header's terms already say (30 days net, due 2026-05-30); on a one-line invoice they add nothing. The line also refers to `LD-DS-B180`, a document no example carries, without saying what it is (the manufacturer's data sheet is `VI-DS-B180`, referenced elsewhere in the flow).
- Condition: line-level terms only where they differ from the header; every reference says what it refers to where it is not obvious.
- Options: (a, preferred) drop both; (b) give the reference a document type (e.g. Lumeway's own data sheet) if it is a real document of the story.
- Needs decision: no

### retail/18#F8 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: on an invoice the supplier's contact answers billing questions and the customer's contact handles incoming invoices. The order names both: `08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable` and `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:AccountingContact/cbc:Name` = `Accounts payable`. The invoice uses customer service and the buying office instead, the latter with a job title and department that contradict its name.
- Condition: the accounting parties' contacts are their accounts departments, with name, job title and department that agree.
- Options: (a, preferred) Lumeway's accounts receivable and Brightmarket's accounts payable, as in the order.
- Needs decision: no

### retail/18#F9 · Low · Whole item master data copied into the invoice line
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: an invoice identifies what is billed; emissions, circularity data, load test, dimensions and Urvania's customs tariff code (a domestic Bayvarran sale) are catalogue data the invoice does not use.
- Condition: the invoiced item carries its identifiers, its tax category and what the invoice depends on.
- Options: (a, preferred) drop the catalogue data from the item.
- Needs decision: no

## Checked and consistent
- Arithmetic: 24 × 520.00 = 12480.00; allowance 5 % × 12480.00 = 624.00 (the order's promotion support); tax exclusive = taxable = payable = 11856.00; tax 0.00 at 0 %; penalty 1.5 % × 11856.00 = 177.84; due date 2026-05-30 = issue + 30 days, as agreed in 02-Catalogue and 08-Order.
- Factoring: type code 393 (factored invoice) with Harbourline Factoring as payee and the payee account in Harbourline's name; account `XB51BLUM38020502304038` and RF reference `RF42LDINV260236` pass their check digits.
- References to 08-Order, 12-DespatchAdvice (despatch line 1, 24 benches) and 17-ReceiptAdvice resolve; tax category `E` "sale for resale" agrees with the catalogue and the order; delivery terms DDP agree with the order.
- Harbourline is described identically in 18 and 19.
