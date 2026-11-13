# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: parties

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

### furniture/09#F1 · Medium · Language/LocaleCode holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with `listID="ISO 639"` is the language itself, repeating `Language/ID` (`en`, ISO 639) and saying nothing about a locale. The same value occurs 362 times in 213 examples (counted with `grep -rc --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'` over world/examples).
- Condition: `LocaleCode` is absent, or holds a locale code from a declared locale list (language plus region), different from `Language/ID`.
- Options: (a, preferred) Remove `LocaleCode`: nothing in the flow depends on a regional variant of English. (b) A locale such as English as used in Bayvarra from a declared list (e.g. a BCP 47 tag), if the world wants to show the element.
- Needs decision: no

### furniture/09#F2 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket's contact is named "Buying office" (functional name) but has the job title "Customer service officer" in the "Sales" department, i.e. the department that serves the store's own customers. Name, job title and department do not agree with each other, and a buyer's contact buys: a sales customer service officer is not the contact for purchasing, planning or returns with a supplier. Here the party is in an accounting role, where the contact would be the accounts function, not purchasing or sales. The same contact is used in every example of the flow where Brightmarket is described in full.
- Condition: Name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) A buying contact: job title e.g. 'Buyer', department 'Purchasing' (and, in accounting roles, an accounts contact). (b) Rename the contact to fit the sales title, if the sales customer-service desk is really meant.
- Needs decision: no

### furniture/09#F3 · Low · Brightmarket's online shop and social media profile are carried without a use in this document
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: `AdditionalWebSite` ("An additional web site associated with this party (e.g. a satellite web site)") and `SocialMediaProfile` ("A social media profile associated with this party") come from the store's master data. Nothing in this document concerns the store's online shop or its photo-sharing profile; the products are an own-label line bought from a supplier. Data copied from master data into a document that does not use it is a filler under the repository's rule. (SocialMediaProfile occurs in 41 examples, counted with `grep -rc --include='*.xml' 'SocialMediaProfile>'` over world/examples.)
- Condition: The two aggregates are present only in documents of the flow where they have a business reason (e.g. a document about online sales or consumer communication), or nowhere in this flow.
- Options: (a, preferred) Remove both from this document. (b) Give the flow a reason for them (e.g. the product activity reporting online-shop sales separately) and keep them only there.
- Needs decision: no

## Checked and consistent
- Every party aggregate of the flow was compared across all 17 examples (a hash over every leaf value and attribute): Brackenmere Furniture, Brightmarket Stores and Lumeport Public Works Department are each described identically wherever they appear in full, and every short reference (signatory, delivery, warranty, manufacturer, payee, performing, approver party) uses the same register identifier and name as the full party.
- Party identifier, legal-entity `CompanyID` and the suffix of `ElectronicAddressID` agree for each party (20412466, 20410411, 20410548); tax identifiers carry the prefix of the party's state (UL- Upland State, CO- Coastal State), matching `CountrySubentityCode` and the tax scheme's jurisdiction.
- `check_ids.py`: all GS1 keys (party and location GLNs, GTINs) have valid check digits.

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge of the GS1 prefix list); the same holds for every 952… key in the example.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: the +999 telephone numbers could be real — refuted because country code 999 is not assigned in ITU-T E.164 (spare), and the web and mail domains are under the reserved .example domain.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: a registration on 1 January (1996-01-01) looks like a placeholder date — refuted because nothing in the world says the Bayvarran register is closed that day, and no other value depends on it.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact in roles other than selling (sender of planning documents, accounting supplier) — refuted because Brackenmere is a small enterprise whose trade-sales desk plausibly handles the whole customer relationship, invoices included; name, title and department agree with each other.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: Brackenmere's address is in a state-level register (XB:UL) while the Lumeport parties use a city register — refuted because the rule for the examples is "address registers by country level": Bayvarra keeps them per state or city, which is what the schemeIDs show.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: `Name` ("The common name of the social media") and `ID` ("An identifier for a specific social media") hold the account handle and account number rather than the platform — refuted because the aggregate is the profile, and naming and identifying the profile is a legitimate reading of these definitions; the presence of the profile is a finding of its own.
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID`: the Marrowdale branch of the Bank of Lumeport could contradict the account — refuted because the account number contains the branch number 387120 and the account name is Brackenmere's registration name.
