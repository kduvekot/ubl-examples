# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/22#F1 · Medium · Language/LocaleCode holds the language code, not a locale
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". Every party language here has `LocaleCode` = `en` with `listID="ISO 639"`: the ISO 639 code of the language itself, which repeats `Language/cbc:ID` and names no locale (no country or region in which English is used). ISO 639 is a list of languages, not of locales. The world does have locales: Urvanian addresses carry renderings tagged `languageID="en-XB"` (English as used in Bayvarra). The checklist of the review names "a language code in LocaleCode" as a Medium case. The same value occurs 364 times in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `-rl … | wc -l` for the files).
- Condition: No `Language/cbc:LocaleCode` of a party holds a bare language code; where a `LocaleCode` is present it identifies a locale and its `listID` names a list of locales.
- Options: Drop `LocaleCode` from the parties' languages (preferred: nothing in this document depends on a locale, so it has no business reason, and `Language/cbc:ID` already says English); or give a real locale (e.g. English as used in Bayvarra) with a `listID` for a locale list such as BCP 47. The fix belongs in the party master data, so it applies to every example at once.
- Needs decision: no

### retail/22#F2 · Low · The consumer's bank account in a document paid by card
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`
- Why: Robin Ashdale's party carries a person's financial account (a current account at the Bank of Lumeport). The order is paid by credit card, so the account is not used; a shop does not usually know a customer's bank account at all. It is the same account in both consumer documents of the flow (`21-PurchaseReceipt.xml` and `22-Order.xml`), copied with the person (section 4.8 of the review: a bank account of a party that pays nothing through it under this document).
- Condition: The consumer's party carries no bank account unless the document pays or refunds through it.
- Options: Remove the financial account from the person (preferred).
- Needs decision: no

### retail/22#F3 · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: UBL defines `PartyLegalEntity/CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount. The value here is a sum of money (`currencyID="XBL"`), i.e. the share capital, which is not what the definition says; for Lumeway, a private limited company, the definition's "corporation" fits only loosely. Besides, nothing in this document uses the share capital (it is not an invoice or another business letter on which company law could require it). This is a conflict between the UBL definition and its data type rather than a choice the example can resolve alone, so it is a candidate for the findings recorded for the OASIS UBL TC.
- Condition: Either the share capital is no longer carried in `CorporateStockAmount`, or the use is recorded as a finding against the UBL definition (semantic conformance, UBL 2.5 §4.7/§7.2) and kept on purpose.
- Options: Record it as a finding against the UBL definition and keep the value where a document needs the share capital (invoices); leave it out here, where the document does not use it (preferred). The decision is the same for every example.
- Needs decision: yes

### retail/22#F4 · Low · Brightmarket's contact: name, job title and department disagree, and do not fit the role
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: The primary contact of Brightmarket (`SellerSupplierParty`) is named "Buying office" with the e-mail buying@brightmarket.example, but its job title is "Customer service officer" and its department "Sales": a buying office is part of purchasing, not of sales. In this document here Brightmarket is the seller to a consumer: a sales customer-service officer could fit, but the contact is named "Buying office" with the address buying@brightmarket.example, which serves Brightmarket's own purchasing, not its customers. The same contact is used in every role Brightmarket has in the flow (41 XML files contain `<cbc:Name>Buying office</cbc:Name>`, all with this job title; `grep -rl --include='*.xml'`).
- Condition: The name, job title and department of Brightmarket's contact in this document agree with each other and with Brightmarket's role here.
- Options: Make the master contact consistent (e.g. Buying office / Buyer / Purchasing), and give Brightmarket role-specific contacts where its role is not purchasing (goods-in for delivery and consignee roles, accounts payable for invoices, customer service for sales to consumers). Preferred: role-specific contacts, since the flow already has them in the order.
- Needs decision: no

## Checked and consistent
- Roles: Robin Ashdale (the same person, address and register entry LUM-ADR-934215 as in `21-PurchaseReceipt.xml`) orders from Brightmarket; the collection point is the garden department, GLN 9522610900026.
- Every party is described the same way in every example of the flow: each of the full descriptions of Brightmarket Stores, Lumeway Distribution, Bayforth Forwarding and Harbourline Factoring is identical in all examples that carry it (compared leaf by leaf over all 22 XML files), and the short references (register identifier and name) match them.
- Party identifiers: the register identifiers (Brightmarket 20410411, Lumeway 20410274, Bayforth 20411644, Harbourline 20411233) agree with `PartyLegalEntity/CompanyID` and with the endpoint identifiers `XB:<register number>`; `check_ids.py` finds the check digits of all GS1 keys and IBAN-like accounts in this example correct. The GLN prefix 952 is GS1's prefix for demonstrations and examples (own knowledge), so the GLNs cannot be mistaken for real ones.
- Tax schemes: each Bayvarran party is registered for the state sales tax (STT) of the state its address is in (Lumeway Upland State, the others Coastal State), with matching jurisdiction.

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cac:SocialMediaProfile`, `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalWebSite`, `/Order/cac:SellerSupplierParty/cac:Party/cbc:LogoReferenceID`: suspected as master data copied into the document — refuted because here Brightmarket sells to a consumer, and a shop's receipt or order confirmation carries its logo, online shop and social media for that customer.
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Robin Ashdale`: suspected as too thin a delivery party — refuted because the buyer collects the goods himself and is described in full in `/Order/cac:BuyerCustomerParty`.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: suspected to contradict the description "The store's own garden bench set." — refuted because the Marrow set is Brackenmere's brand in all 13 examples that carry it (furniture flow), and "the store's own" reads as the store's own range, not its own label.
