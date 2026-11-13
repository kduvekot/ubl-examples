# LLM review: 02-Quotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/02-Quotation.xml`, Git blob `6e768c2e81f270872df5b742e223f22c2e4950bf` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/02#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region, not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it, so it carries the meaning of another element. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`: nothing in the flow depends on a regional variant of English (context, parties, and the merges of every earlier flow); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/02#F2 · Low · Maker's brand on an item sold under the store's own label
- XPath: `/Quotation/cbc:Note` = `Including the store's own label.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The quotation's own note says the price includes the store's own label, and the description says the set is made for the store's own line: a private-label product, normally sold under the retailer's brand. The brand `Brackenmere` points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`; Grep over `world/examples/furniture/*.xml`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName` (the GTIN may then also be the store's); (b) keep `Brackenmere` and reword note and description to an exclusive maker-branded line.
- Needs decision: yes
- From: broad, context

### furniture/02#F3 · Low · The optional cushions of the request are not answered
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`
- XPath: `/Quotation/cbc:LineCountNumeric` = `1`
- XPath: `/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cbc:Name` = `Garden bench set Marrow`
- Why: The request asks, in its line note, for optional matching seat cushions. The quotation has one line, the bench set, and its only note is about the label: it neither quotes the cushions nor says they are not offered. A quotation answers the request; a part of the request left without any answer is either not needed in the request or missing here.
- Condition: either the quotation answers the cushions (a line, or a note that they are not offered), or the request no longer asks for them.
- Options: (a, preferred) resolve it in the request (remove its note, see the review of 01), since nothing later in the flow involves cushions; (b) add a quotation line for cushions, or a note declining them.
- Needs decision: yes
- From: broad, context

### furniture/02#F4 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/Quotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`). A date shared by so many unrelated companies reads as a default rather than part of their histories.
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/02#F5 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores is the buyer here. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact of a buyer. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying contact (job title e.g. "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/02#F6 · Low · Store master data copied into the quotation
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo reference, online-shop website, photo-sharing profile and share capital are master data that a quotation does nothing with (section 4.8). The same four elements are carried on Brightmarket Stores in examples 01 to 14 of the flow. The parties part refuted the logo because the quotation includes the store's own label (`/Quotation/cbc:Note` = `Including the store's own label.`); the merge keeps the logo as the weakest part of the finding, because the quotation does not tie the logo to the label (no line, attachment or note uses it) and the same logo is carried in documents without any label.
- Condition: these elements are present only where the document has a reason for them; a logo kept for the own label is tied to it in the document.
- Options: (a, preferred) remove them; (b) keep the logo only if the quotation uses it for the own-label artwork, and say so.
- Needs decision: no
- From: context, parties (parties refuted the logo part)

### furniture/02#F7 · Low · Originator and beneficiary repeat the buyer
- XPath: `/Quotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Quotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") say something only when they differ from the buyer. Both are the buyer, register number `20410411`; they are copied from the request and add nothing. The broad part refuted this as in 01 (an explicit statement under IND6); the merge keeps it because no document of the flow uses the two roles, so they lack the business reason IND5 asks for.
- Condition: both are absent, or each names a party other than the buyer with its own role in the story.
- Options: (a, preferred) remove both; (b) name a real originator if the story has one (a story change).
- Needs decision: no
- From: context, parties (broad refuted it, see Why)

### furniture/02#F8 · Low · Quoted payable amount says nothing about tax
- XPath: `/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount` = `12200.00`
- XPath: `/Quotation/cac:QuotedMonetaryTotal/cbc:LineExtensionAmount` = `12200.00`
- Why: `PayableAmount` is "The amount of the monetary total to be paid". The quotation has no `TaxTotal` and no tax category on its line, so the amount to be paid equals the net line amount without saying whether the supply is taxed, exempt or quoted net of tax. The order that accepts the quotation states the treatment explicitly (`08-Order.xml:/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`, state sales tax exempt). Under "nothing implied by absence" (IND6) the zero tax in the quoted total is only implied. The broad part refuted this: the supply is exempt (sale for resale), so the quoted amount is also the payable amount, and a quotation need not carry a tax breakdown. The merge keeps the finding at Low: the exemption is known only from the later order, not from the quotation.
- Condition: the quotation states the tax treatment of the quoted amount (a `TaxTotal` with the exempt STT category and reason, as in the order, or a note that prices exclude state sales tax for resale).
- Options: (a, preferred) a `TaxTotal` with a `TaxSubtotal` E / `RESALE` under STT, mirroring 08, so quotation, order and invoice agree; (b) a note that the prices are net of state sales tax.
- Needs decision: no
- From: money (broad refuted it, see Why)

## Checked and consistent
- Line arithmetic: `/Quotation/cac:QuotationLine/cac:LineItem/cbc:Quantity` = `20` × `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `610` per `/Quotation/cac:QuotationLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1` set = 12200.00 = `/Quotation/cac:QuotationLine/cac:LineItem/cbc:LineExtensionAmount` = `12200.00` = line extension and payable amount of the total (recomputed by the merge). The price 610 is the one 08-Order, 09-Invoice and 13-CreditNote use.
- Reference: `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `BS-DOC-26-0567` resolves to `01-RequestForQuotation.xml`, a request for quotation; buyer, seller, item (BF-GS-01, GTIN 9523710000012), quantity (20 sets) and currency (`/Quotation/cbc:PricingCurrencyCode` = `XBL`) agree with it. `XBL` is not an assigned ISO 4217 code (own knowledge).
- Dates: issued 2026-03-06 08:58, before the request's submission due date 2026-03-07; `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-05-05` is 60 days after the issue date, as requested; the orders 08 (2026-03-16) and 10 (2026-04-16) fall within it.
- Codes: SET, HS 940169, CPC 38112 fit the item; GS1 check digits pass (`check_ids.py`, re-run by the merge).
- Signature by the seller on its own quotation fits the element.
- Party data of Brackenmere and Brightmarket are identical to the other examples of the flow (compared by the parties part over every leaf value).

## Considered and refuted
- `/Quotation/cac:QuotationLine/cac:LineItem/cbc:ID`: a line item ID is "assigned by the buyer" — refuted as a problem because `1` is the buyer's line number from the request (from context).
- `/Quotation`: no `DeliveryTerms` although the request asked for DAP to the store's goods-in — refuted because a quotation need not repeat the requested delivery terms, nothing in it departs from the request, and the order `08-Order.xml` carries DAP (from context, logistics).
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge); the same holds for every 952… key here (from parties).
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under `.example` (from parties).
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact in roles other than selling — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship; name, title and department agree (from parties).
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level address register for Brackenmere vs city register for Lumeport — refuted because Bayvarra keeps address registers per state or city, as the schemeIDs show (from parties).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number instead of the platform — refuted because the aggregate is the profile; its presence is part of F6 (from parties).
- `/Quotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID`: master data without use — refuted by parties (own label); kept by the merge as part of F6, with the argument there.
- `/Quotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F4 by the merge.
- `/Quotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: repeats the buyer — refuted by broad (IND6); kept by the merge as F7.
- `/Quotation/cac:QuotedMonetaryTotal/cbc:PayableAmount`: no tax total — refuted by broad (exempt supply; no breakdown needed); kept by the merge as F8.

## Changed in the merge
- broad/F1, context/F1, parties/F1 → F1: combined; preferred option set to removal (context, parties, earlier flows), broad's `en-XB` kept as option (b).
- broad/F2, context/F2 → F2: combined; example count verified (12 examples carry `BF-GS-01`).
- broad/F3, context/F4 → F3: combined.
- parties' refuted RegistrationDate → F4: made a finding (Low, needs decision) for alignment with the earlier flows.
- broad/F4, parties/F2 → F5: combined.
- context/F5, parties/F3 → F6: grouped into one finding, one XPath line per element; the parties' refutation of the logo carried with the merge's counter-argument.
- context/F3, parties/F4 → F7: combined; broad's refutation carried into Why.
- money/F1 → F8: severity and decision kept; broad's refutation added with the merge's counter-argument.
