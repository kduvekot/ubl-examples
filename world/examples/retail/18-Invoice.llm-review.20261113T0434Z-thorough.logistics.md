# LLM review: 18-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/18#F1 · High · "Original" lead time of 5 days, where the catalogue gives 3
- XPath: `/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `3`
- Why: OriginalItemLocationQuantity is "An original set of location-specific properties (e.g., price and quantity) associated with this invoice line", i.e. the terms the sale was based on: the catalogue line 1 of LD-CAT-26-0218, which the order 08 cites, with a lead time of 3 days. The invoice states 5. Nothing in the flow changed the lead time (03 changes only the side frame's price, 04 only the slat wood, both after this invoice). The actual time from order (2026-04-24) to receipt (2026-04-30, 17) is 6 days, so 5 is neither the agreed nor the actual figure. The element carries only the lead time, without a price, so it has no other purpose in the invoice.
- Condition: the original item-location data quoted in the invoice are those of the catalogue line the order was based on (lead time 3 days), or the element is absent.
- Options: (a, preferred) drop PricingReference, which adds nothing to billing here; (b) LeadTimeMeasure 3 DAY, with the catalogue price 520 XBL if the reference is kept.
- Needs decision: no

### retail/18#F2 · High · Emission value is not factor × base
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/18#F3 · Low · Invoices 24 benches with reference to a receipt advice that accepted 23
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `24`
- XPath: `/Invoice/cac:InvoiceLine/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`
- XPath: `/Invoice/cbc:IssueTime` = `15:52:00`
- Why: The invoice is issued 31 minutes after the receipt advice 17 (15:21) and references its line 1, which accepted 23 and refused 1 bench with a request for credit. Billing 24 and crediting 1 two days later (19) is a possible practice, but the invoice then cites a receipt that contradicts its quantity without saying so; billing 23 would have made the credit note unnecessary. Under DDP the refused bench is still the seller's risk (own knowledge of Incoterms).
- Condition: either the invoiced quantity agrees with the accepted quantity of the receipt it references, or the invoice says why it bills the despatched quantity (e.g. "the refused bench will be credited").
- Options: (a) invoice 23 and drop 19; (b, preferred, keeps the flow's credit note) keep 24 and add a note that the refused bench is credited separately, or reference only the despatch advice.
- Needs decision: yes (whether the flow keeps the credit note)

### retail/18#F4 · Low · Line document reference to a document that exists nowhere and says nothing about itself
- XPath: `/Invoice/cac:InvoiceLine/cac:DocumentReference/cbc:ID` = `LD-DS-B180`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- Why: `LD-DS-B180` occurs only here (`grep -rn --include='*.xml' 'LD-DS-B180' world/examples`). It looks like a Lumeway data sheet of the bench, next to the manufacturer's data sheet `VI-DS-B180` that every other example uses; without a type the receiver cannot tell what it is, nor why the invoice line needs it.
- Condition: the reference says what it is and has a reason in the invoice, or is absent.
- Options: (a, preferred) drop it (the item already references the manufacturer's data sheet); (b) add DocumentType and use the same reference in the catalogue 02 if Lumeway has its own data sheet.
- Needs decision: no

## Checked and consistent
- References: OrderReference `BS-PO-26-0224` (08), DespatchDocumentReference `LD-DA-26-0229` (12), ReceiptDocumentReference `BS-RA-26-0235` (17) resolve, and all three precede this invoice; line references to despatch line 1 and receipt line 1 exist (but each ID exists twice in its document, see 12/F1 and 17/F1).
- InvoicedQuantity 24 × 520 XBL = 12480.00 = line amount; price and quantity agree with 08 and the catalogue 02.
- DeliveryTerms `DDP` on the line agrees with 08.
- Item identifiers and dimensions agree with 02 line 1.
