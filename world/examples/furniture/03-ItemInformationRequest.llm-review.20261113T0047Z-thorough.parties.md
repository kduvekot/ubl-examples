# LLM review: 03-ItemInformationRequest.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/03-ItemInformationRequest.xml`, Git blob `831fa39b706e496e223832845d95a8ebe56ea67b` (committed)
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

### furniture/03#F1 · Medium · Language/LocaleCode holds a language code, not a locale
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with `listID="ISO 639"` is the language itself, repeating `Language/ID` (`en`, ISO 639) and saying nothing about a locale. The same value occurs 362 times in 213 examples (counted with `grep -rc --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'` over world/examples).
- Condition: `LocaleCode` is absent, or holds a locale code from a declared locale list (language plus region), different from `Language/ID`.
- Options: (a, preferred) Remove `LocaleCode`: nothing in the flow depends on a regional variant of English. (b) A locale such as English as used in Bayvarra from a declared list (e.g. a BCP 47 tag), if the world wants to show the element.
- Needs decision: no

### furniture/03#F2 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket's contact is named "Buying office" (functional name) but has the job title "Customer service officer" in the "Sales" department, i.e. the department that serves the store's own customers. Name, job title and department do not agree with each other, and a buyer's contact buys: a sales customer service officer is not the contact for purchasing, planning or returns with a supplier. The same contact is used in every example of the flow where Brightmarket is described in full.
- Condition: Name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) A buying contact: job title e.g. 'Buyer', department 'Purchasing' (and, in accounting roles, an accounts contact). (b) Rename the contact to fit the sales title, if the sales customer-service desk is really meant.
- Needs decision: no

### furniture/03#F3 · Low · Brightmarket's online shop and social media profile are carried without a use in this document
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: `AdditionalWebSite` ("An additional web site associated with this party (e.g. a satellite web site)") and `SocialMediaProfile` ("A social media profile associated with this party") come from the store's master data. Nothing in this document concerns the store's online shop or its photo-sharing profile; the products are an own-label line bought from a supplier. Data copied from master data into a document that does not use it is a filler under the repository's rule. (SocialMediaProfile occurs in 41 examples, counted with `grep -rc --include='*.xml' 'SocialMediaProfile>'` over world/examples.)
- Condition: The two aggregates are present only in documents of the flow where they have a business reason (e.g. a document about online sales or consumer communication), or nowhere in this flow.
- Options: (a, preferred) Remove both from this document. (b) Give the flow a reason for them (e.g. the product activity reporting online-shop sales separately) and keep them only there.
- Needs decision: no

### furniture/03#F4 · Low · Tax registration and share capital of both parties in a document without tax or payment content
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/ItemInformationRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- XPath: `/ItemInformationRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: This document carries no taxable amounts, no tax treatment and no payment, yet both parties come with their full state-sales-tax registration (`PartyTaxScheme`) and Brightmarket with its corporate stock amount and fully-paid-shares indicator. These are master data that the documents of the flow that do bill or exempt (the orders and invoices) need, not this one; here they serve no business purpose.
- Condition: The document carries the parties' tax registration and share capital only where it has a reason to.
- Options: (a, preferred) Remove `PartyTaxScheme` and `CorporateStockAmount`/`FullyPaidSharesIndicator` from both parties in this document; keep identification, name, address and contact. (b) Keep them and state the reason in the example (none is apparent).
- Needs decision: no

## Checked and consistent
- Every party aggregate of the flow was compared across all 17 examples (a hash over every leaf value and attribute): Brackenmere Furniture, Brightmarket Stores and Lumeport Public Works Department are each described identically wherever they appear in full, and every short reference (signatory, delivery, warranty, manufacturer, payee, performing, approver party) uses the same register identifier and name as the full party.
- Party identifier, legal-entity `CompanyID` and the suffix of `ElectronicAddressID` agree for each party (20412466, 20410411, 20410548); tax identifiers carry the prefix of the party's state (UL- Upland State, CO- Coastal State), matching `CountrySubentityCode` and the tax scheme's jurisdiction.
- `check_ids.py`: all GS1 keys (party and location GLNs, GTINs) have valid check digits.

## Considered and refuted
- `/ItemInformationRequest/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge of the GS1 prefix list); the same holds for every 952… key in the example.
- `/ItemInformationRequest/cac:SenderParty/cac:Contact/cbc:Telephone`: the +999 telephone numbers could be real — refuted because country code 999 is not assigned in ITU-T E.164 (spare), and the web and mail domains are under the reserved .example domain.
- `/ItemInformationRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate`: a registration on 1 January (1996-01-01) looks like a placeholder date — refuted because nothing in the world says the Bayvarran register is closed that day, and no other value depends on it.
- `/ItemInformationRequest/cac:SenderParty/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact in roles other than selling (sender of planning documents, accounting supplier) — refuted because Brackenmere is a small enterprise whose trade-sales desk plausibly handles the whole customer relationship, invoices included; name, title and department agree with each other.
- `/ItemInformationRequest/cac:SenderParty/cac:PostalAddress/cbc:ID`: Brackenmere's address is in a state-level register (XB:UL) while the Lumeport parties use a city register — refuted because the rule for the examples is "address registers by country level": Bayvarra keeps them per state or city, which is what the schemeIDs show.
- `/ItemInformationRequest/cac:ReceiverParty/cac:SocialMediaProfile/cbc:Name`: `Name` ("The common name of the social media") and `ID` ("An identifier for a specific social media") hold the account handle and account number rather than the platform — refuted because the aggregate is the profile, and naming and identifying the profile is a legitimate reading of these definitions; the presence of the profile is a finding of its own.
- `/ItemInformationRequest/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: buyer and seller repeat the sender and receiver — refuted because sender and receiver are the message parties while buyer and seller state the trade relationship the planning data belongs to; both are UBL's design for these documents, and they are given only by identifier and name.
