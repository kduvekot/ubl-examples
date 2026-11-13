# LLM review: 13-CreditNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/13-CreditNote.xml`, Git blob `62fa2031ce86b8f92b5eb82929f1d00df2904665` (committed)
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

### furniture/13#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/13#F2 · Low · Payment terms offer netting although the credit note says the credit is refunded
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cbc:Note` = `The store paid the invoice; the credit is refunded.`
- Why: The document note and the payment means (credit transfer to the store's account by 2026-05-13) say the credit is refunded. The payment terms instead describe settlement against the next payment as the rule and the refund as the exception. In this situation one of the two is already decided; terms that keep the other open contradict the note and the payment means next to them.
- Condition: payment terms, payment means and note describe the same way of settling the credit.
- Options: (a) payment terms that state the refund by 2026-05-13 (or no payment terms beyond the due date) (preferred: agrees with note and payment means); (b) a netting story without a refund payment means.
- Needs decision: no

### furniture/13#F3 · Low · Payment note calls the credit note an invoice
- XPath: `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579`
- Why: `PaymentNote` is "Free-form text applying to the Payment for the owner of this account", i.e. the text the store sees on the refund. `BF-CN-26-0579` is this credit note, not an invoice; the text misnames the document the refund settles.
- Condition: the payment note names the document by its kind (credit note) or carries only its number.
- Options: (a) "Credit note BF-CN-26-0579" (preferred).
- Needs decision: no

### furniture/13#F4 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/13#F5 · Low · Customer's master data copied into the credit note
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in a credit note (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `BillingReference/InvoiceDocumentReference` resolves to `09-Invoice.xml` (`BF-INV-26-0575`, issued 2026-03-22, as stated); `OrderReference` to `08-Order.xml`; `AdditionalDocumentReference` to the return instruction `12-InstructionForReturns.xml`.
- 6 sets credited = 6 sets returned; 6 × 610 = 3660, less 5 % restocking (183) = 3477.
- `PayeeFinancialAccount` is the store's account (the same ID is named "Brightmarket Stores Corp" in `14-DebitNote.xml`), which fits a refund to the customer.

## Considered and refuted
- `/CreditNote/cbc:DueDate` = `2026-05-13`: a due date on a credit note was suspected to be out of place — refuted because the definition ("The date on which this Credit Note is due") applies to a refund that is to be paid.
