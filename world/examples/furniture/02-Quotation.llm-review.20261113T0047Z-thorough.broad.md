# LLM review: 02-Quotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/02-Quotation.xml`, Git blob `6e768c2e81f270872df5b742e223f22c2e4950bf` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### furniture/02#F1 · Medium · Language code in LocaleCode
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/02#F2 · Low · Own-line item carries the maker's brand
- XPath: `/Quotation/cbc:Note` = `Including the store's own label.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/02#F3 · Low · Optional cushions of the request are not answered
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`
- XPath: `/Quotation/cbc:LineCountNumeric` = `1`
- Why: The request asks for optional matching seat cushions; the quotation quotes only the set (one line) and says nothing about the cushions, neither a price nor a refusal. A quotation is "used to quote for the provision of goods and services" requested; leaving part of the request unanswered without a word is a gap.
- Condition: Either the quotation quotes or declines the cushions, or the request no longer asks for them.
- Options: (a, preferred) resolve it in the request (see the review of 01), since nothing later in the flow involves cushions; (b) add a quotation line for cushions, or a note declining them.
- Needs decision: yes

### furniture/02#F4 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/Quotation/cac:QuotationLine/cac:LineItem/cbc:LineExtensionAmount` = `12200.00`: 20 SET × 610 = 12 200; header line extension and payable amount agree.
- `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `BS-DOC-26-0567` resolves to `01-RequestForQuotation.xml`; quantity 20 SET, item identifiers and currency agree with the request.
- `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-05-05`: 60 days after the issue date 2026-03-06, as requested; the orders 08 (2026-03-16) and 10 (2026-04-16) fall within it.
- GS1 check digits (check_ids.py).

## Considered and refuted
- `/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount`: no tax total in the quotation — refuted because the order and invoice show the supply is exempt (sale for resale), so the quoted amount is also the payable amount; a quotation need not carry the tax breakdown.
- `/Quotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: repeats the buyer — refuted as in 01 (explicit statement, IND6).
