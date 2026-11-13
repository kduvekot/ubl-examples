# LLM review: 02-Quotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/02#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used", a language in a region, not the language. `en` with `listID="ISO 639"` is a language code that repeats `cac:Language/cbc:ID`. The same value occurs 362 times in 213 examples (`grep -o '<cbc:LocaleCode listID="ISO 639">en'` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list named in its `listID`, or is absent.
- Options: (a) remove it (preferred: nothing in the flow depends on a locale); (b) a locale such as `en-XB` from a list that defines locales.
- Needs decision: no

### furniture/02#F2 · Low · Brand name of the maker on an item sold under the store's own label
- XPath: `/Quotation/cbc:Note` = `Including the store's own label.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: `BrandName` is "A brand name of this item". The quotation's own note says the price includes the store's own label, and the item description says it is made for the store's own line: a private-label product, sold under the retailer's brand. The brand `Brackenmere` contradicts that unless the story means a co-branded line. The same item carries the same brand in 12 furniture examples.
- Condition: the item's `BrandName` is the brand it is sold under in the story, consistently with the note and the description in every example that carries the item.
- Options: (a) the store's own label as `BrandName` (preferred); (b) keep `Brackenmere` and reword note and description to a maker-branded exclusive line.
- Needs decision: yes

### furniture/02#F3 · Low · Originator and beneficiary repeat the buyer
- XPath: `/Quotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Quotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") say something only when they differ from the buyer. Both are the buyer, register number `20410411`; they are copied from the request and add nothing.
- Condition: both are absent, or each names a party other than the buyer with its own role.
- Options: (a) remove both (preferred); (b) name a real originator if the story has one.
- Needs decision: no

### furniture/02#F4 · Low · The optional cushions of the request are not answered
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:Name` = `Garden bench set Marrow`
- XPath: `/Quotation/cbc:LineCountNumeric` = `1`
- Why: The request asked in its line note for optional matching seat cushions (`01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`). The quotation has one line, the bench set, and no note: it neither quotes the cushions nor says they are not offered. A quotation's purpose is to answer the request; a request element left without any answer is either not needed in the request or missing here.
- Condition: either the quotation answers the cushions (a line, or a note that they are not offered), or the request no longer asks for them.
- Options: (a) remove the request's note (preferred, see furniture/01: the cushions play no part in the flow); (b) add a quotation line or a note for the cushions.
- Needs decision: yes

### furniture/02#F5 · Low · Buyer's master data copied into the quotation
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo reference, online-shop website, social-media profile and share capital are master data that a quotation does nothing with (section 4.8). The same four elements are carried on Brightmarket Stores in examples 01 to 14 of the flow.
- Condition: these elements are present only where the document has a reason for them.
- Options: (a) remove them (preferred); (b) keep the logo only if the quotation uses it for the own-label artwork, and say so.
- Needs decision: no

## Checked and consistent
- `ValidityPeriod/EndDate` 2026-05-05 is 60 days after the issue date 2026-03-06, as the request asked (`RequestedValidityPeriod` 60 days).
- `RequestForQuotationDocumentReference` resolves to `01-RequestForQuotation.xml` (ID `BS-DOC-26-0567`), a request for quotation; quantity (20 sets) and item identifiers agree with it.
- Signature by the seller on its own quotation fits the element.

## Considered and refuted
- `/Quotation/cac:QuotationLine/cac:LineItem/cbc:ID`: a line item ID in a quotation is "assigned by the buyer" — refuted as a problem because `1` is the buyer's line number from the request.
- `/Quotation`: no `DeliveryTerms` although the request asked for DAP — refuted because the quotation's purpose (to quote) does not depend on repeating the terms; the order `08-Order.xml` states DAP.
