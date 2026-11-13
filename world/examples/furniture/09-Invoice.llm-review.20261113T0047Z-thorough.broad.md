# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/09#F1 · High · Delivery note reference does not resolve
- XPath: `/Invoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `BF-DN-26-0320`
- Why: `DeliveryNoteDocumentReference` is "A reference to a Delivery Note associated with this document". No example in the flow (or anywhere: `grep -rl --include='*.xml' 'BF-DN-' world/examples` finds only this file) is a delivery note or despatch advice with this ID, and the number does not follow the flow's numbering (0567–0583). The invoice therefore points to a document that does not exist in the world's records.
- Condition: The delivery note reference resolves to an example of the flow (e.g. a Despatch Advice), or is absent.
- Options: (a) remove the reference (preferred if the flow is not meant to show the delivery); (b) add a Despatch Advice of 20 sets and 20 care kits to the flow and reference its ID.
- Needs decision: yes

### furniture/09#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/09#F3 · Low · Free care kits exempted as a sale for resale
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:Note` = `Wood oil and a cloth, for the store to hand to its customers.`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- Why: Line 2 invoices 20 care kits free of charge, which the store is to hand to its customers. They are not sold, and not resold, so "Sale for resale or manufacture" does not describe them; a free gift is either outside the scope of the sales tax or, in some jurisdictions, a taxable deemed supply. The kits are also not in the order `08-Order.xml`. The tax treatment of free goods is a judgment for the world.
- Condition: The tax category and exemption reason of the free line describe the treatment of goods given free of charge in Bayvarra's state sales tax.
- Options: (a, preferred) a world code for supplies without consideration (out of scope), since nothing is sold; (b) keep RESALE if the world decides free promotional goods for resale customers follow the main supply.
- Needs decision: yes

### furniture/09#F4 · Low · Own-line item carries the maker's brand
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/09#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `183.00`: 1.5 % × 12 200 = 183; the penalty period starts 2026-04-22, the day after the due date 2026-04-21 (30 days after 2026-03-22).
- Totals: lines 12 200 + 0 = 12 200 = tax exclusive = tax inclusive = payable; tax 0.00 (exempt).
- Sub-invoice lines 7 600 + 4 600 = 12 200, as in the order.
- RF creditor reference `RF74BFINV260575` and the IBAN-like account `XB42BLUM38712004503347` pass their check digits; the branch ID 387120 matches the account's bank and branch digits.
- `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0574` resolves to `08-Order.xml`; `13-CreditNote.xml` references this invoice with the same issue date.
- Invoice date 2026-03-22 against the order date 2026-03-16 and the lead time of 5 days in `04-TradeItemLocationProfile.xml`.
