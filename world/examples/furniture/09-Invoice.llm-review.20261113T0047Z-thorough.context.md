# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/09-Invoice.xml`, Git blob `ee49a007b8043177d29c63f3b1b0c8223f117844` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/09#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/09#F2 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/09#F3 · Low · Customer's master data copied into the invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo, online-shop website, social-media profile and share capital have no use in an invoice to it (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `OrderReference` resolves to `08-Order.xml` (`BS-PO-26-0574`); line 1 with its two sub lines repeats the order's breakdown (20 benches, 40 chairs) and amounts.
- `InvoiceLine[2]`: a free care kit with `FreeOfChargeIndicator` true and amount 0, the note giving the reason; an invoice may carry a free line not ordered.
- `AccountingCost` and `AccountingCostCode` are the buyer's cost centre from the order, as the definition ("The buyer's accounting code") requires.
- `PaymentTerms` with `PaymentMeansID` = `1` refers to the one `PaymentMeans` of the invoice.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF74BFINV260575`: repeats `PaymentID` — refuted as a filler because the instruction to quote the reference is a real payment instruction to the payer, which the identifier alone does not give.
- `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[1]`: priced sub lines in an invoice were suspected to double the amounts — refuted because only the parent lines enter `LegalMonetaryTotal/LineExtensionAmount` (12200 + 0).
