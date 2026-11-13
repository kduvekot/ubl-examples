# LLM review: 18-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/18-Invoice.xml`, Git blob `4c83015ab6e72109b8aa59490284886f5aa405ef` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/18#F1 · High · The invoice cites the receipt advice that refused one bench, and bills all 24
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `24`
- XPath: `/Invoice/cac:ReceiptDocumentReference/cbc:ID` = `BS-RA-26-0235`
- XPath: `/Invoice/cac:InvoiceLine/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`
- Why: ReceiptDocumentReference is "A reference to a Receipt Advice associated with this document",
  and the line refers to receipt line 1. That line says 23 benches were accepted and one refused with
  a request for credit. The invoice, issued 31 minutes after the receipt advice, bills 24 benches on
  the strength of it. 19-CreditNote.xml then credits the refused bench, so the story works only if the
  invoice was made before the receipt was known, which its references contradict.
- Condition: the quantity invoiced on the line agrees with the receipt line the invoice refers to, or
  the invoice does not rest on that receipt (no receipt reference, issued before it).
- Options: (a) invoice 23 benches against the receipt and drop the credit note's role for the bench,
  keeping the credit note for something else or removing it; (b) preferred, as it keeps the flow's
  credit note: issue the invoice on despatch (before the receipt) without the receipt references, so
  the credit note corrects it afterwards.
- Needs decision: yes

### retail/18#F2 · High · Emission factor times base does not give the emission
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 "per unit of activity" with a base of one bench gives 0.82 kg CO2e, not 96 kg (values
  copied from 02-Catalogue.xml).
- Condition: factor × activity = value, or no factor (see F7).
- Options: drop the emission from the invoice (preferred), or correct the factor.
- Needs decision: no

### retail/18#F3 · Medium · An "original" lead time that is not the catalogue's, as the only pricing reference
- XPath: `/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `3`
- Why: PricingReference is "A reference to pricing and item location information associated with this
  invoice line", OriginalItemLocationQuantity "An original set of location-specific properties (e.g.,
  price and quantity)". The only property given is a lead time of 5 days; the catalogue the order was
  based on gives 3 days for the bench. The invoice neither prices nor delivers by the lead time, so the
  aggregate has no use here, and its value contradicts the original it claims to repeat.
- Condition: no pricing reference, or one that repeats the catalogue's original values and that the
  invoice uses (e.g. the original price).
- Options: drop it (preferred).
- Needs decision: no

### retail/18#F4 · Medium · A system-boundary code in the fullness indication, and a language code in LocaleCode
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full,
  partially full, or empty"; "Cradle to gate" is a life-cycle boundary (39 examples). LocaleCode is "A
  code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is a language
  code (213 examples; both counted with `grep -l` over `*.xml`).
- Condition: no boundary code in FullnessIndicationCode; LocaleCode a locale or absent.
- Options: drop FullnessIndicationCode; `en-XB` or no LocaleCode.
- Needs decision: no

### retail/18#F5 · Low · Tax point eight days after the invoice and the delivery
- XPath: `/Invoice/cac:InvoiceLine/cbc:TaxPointDate` = `2026-05-08`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: TaxPointDate is "The date of this invoice line, used to indicate the point at which tax becomes
  applicable". The goods were delivered and invoiced on 2026-04-30; nothing in the invoice explains why
  the tax point falls on 2026-05-08, a date that matches no event of the flow (the sale is moreover
  exempt). Unless Bayvarra's sales-tax rules set the tax point by another event, the date has no
  reason.
- Condition: the tax point date is the date of the event that the tax rules make the tax point, or
  absent.
- Options: (a) the delivery/invoice date 2026-04-30, or drop it (the line is exempt); (b) if the
  world's tax rules place the tax point later, state the rule in the story.
- Needs decision: yes

### retail/18#F6 · Low · Line-level payment terms and a document reference that add nothing
- XPath: `/Invoice/cac:InvoiceLine/cac:PaymentTerms/cbc:Note` = `The promotion stock is paid with the invoice, 30 days net.`
- XPath: `/Invoice/cac:InvoiceLine/cac:DocumentReference/cbc:ID` = `LD-DS-B180`
- Why: the line's payment terms repeat the header's 30 days net for the invoice's only line. The
  line's document reference `LD-DS-B180` has no type and matches no example; the item's specification
  is referenced as `VI-DS-B180` everywhere else, so the reader cannot tell what `LD-DS-B180` is.
- Condition: line-level terms and references only where they add something, and typed.
- Options: drop both (preferred).
- Needs decision: no

### retail/18#F7 · Low · The invoice carries the item's full catalogue description and the parties' master data
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the footprint, circularity profile, load test, dimensions and customs codes of the bench, a
  customs trader number on a domestic invoice and the customer's social-media profile play no part in
  requesting payment (IND5/IND6). (Share capital may be a legal mention on invoices and is not part of
  this finding.)
- Condition: item and parties carry what the invoice uses.
- Options: reduce them.
- Needs decision: no

## Checked and consistent
- OrderReference `BS-PO-26-0224`, DespatchDocumentReference `LD-DA-26-0229` and
  ReceiptDocumentReference `BS-RA-26-0235` resolve; despatch line 1 and receipt line 1 exist.
- Price 520 XBL and the 5 % promotion support of 624.00 XBL match 08-Order.xml; 12480.00 − 624.00 =
  11856.00 = TaxExclusiveAmount = PayableAmount.
- InvoiceTypeCode 393 "Factored invoice" with the factor Harbourline as PayeeParty and its account as
  the payee's account; AccountingCost "Garden department" / `6120` are the buyer's codes from the order.
- PenaltyAmount 177.84 = 1.5 % of 11856.00; the penalty period starts the day after the due date.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:DeliveryTerms/cbc:ID`: DDP at line level repeats the order's terms —
  refuted because the invoice has no header-level delivery terms, so nothing is repeated, and stating
  the terms of the delivery invoiced on its line is a legitimate use.
