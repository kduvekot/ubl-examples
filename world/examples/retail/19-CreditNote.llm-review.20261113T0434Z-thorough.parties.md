# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/19#F1 · Medium · Language/LocaleCode holds the language code, not a locale
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". Every party language here has `LocaleCode` = `en` with `listID="ISO 639"`: the ISO 639 code of the language itself, which repeats `Language/cbc:ID` and names no locale (no country or region in which English is used). ISO 639 is a list of languages, not of locales. The world does have locales: Urvanian addresses carry renderings tagged `languageID="en-XB"` (English as used in Bayvarra). The checklist of the review names "a language code in LocaleCode" as a Medium case. The same value occurs 364 times in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `-rl … | wc -l` for the files).
- Condition: No `Language/cbc:LocaleCode` of a party holds a bare language code; where a `LocaleCode` is present it identifies a locale and its `listID` names a list of locales.
- Options: Drop `LocaleCode` from the parties' languages (preferred: nothing in this document depends on a locale, so it has no business reason, and `Language/cbc:ID` already says English); or give a real locale (e.g. English as used in Bayvarra) with a `listID` for a locale list such as BCP 47. The fix belongs in the party master data, so it applies to every example at once.
- Needs decision: no

### retail/19#F2 · Medium · A site gate in AdditionalStreetName of Lumeway's address
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is not a street name but an entrance of the distribution centre at Distribution Drive 43; it only matters to vehicles that load or unload there, and the postal address of the party holds nothing for vehicles (checklist of the review: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles"). The same value occurs 79 times in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: No `AdditionalStreetName` holds "Gate 3"; Lumeway's postal address holds only postal parts, and where a transport document needs the gate it is given in the pickup or delivery location, not in a street element.
- Options: Remove the gate from Lumeway's postal address (preferred), and where a transport document needs it, say it in that location's `Description` (or as a location identifier of the gate, e.g. a GLN of the dock). Fix it in the party master data.
- Needs decision: no

### retail/19#F3 · Medium · PayeeParty in a credit note that nobody pays to the factor
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: UBL defines `PayeeParty` as "The Party who receives the Payment". Under this credit note the money, if any, flows to Brightmarket (a refund), or the credit is offset; the note says it is "Settled against the next payment to the seller", so no payment is received by Harbourline under this document. The note also speaks of a payment "to the seller", while the factored invoice it corrects directs payment to Harbourline (`18-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`, invoice type `393`, factored).
- Condition: The credit note names a payee only if a party receives a payment under it, and its note on settlement agrees with the factoring of the invoice (who the debtor pays).
- Options: Remove the payee and say in the note that the credit is offset against the next payment to Harbourline (preferred: it keeps the factoring story consistent); or, if the factor must be told, use a note and keep the payee out.
- Needs decision: yes

### retail/19#F4 · Low · Valdara's GTINs are in Lumeway's GS1 company prefix
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: Lumeway's GLN `9520610900008` and the GTIN of Valdara's bench share the GS1 company prefix 9520610. Across the world that prefix is Lumeway's: its rail-siding GLN 9520610900015 and every SSCC in the examples, all despatched by Lumeway (`12-DespatchAdvice.xml`, `air/03-ForwardingInstructions.xml`, `sea/14-BillOfLading.xml`), start with it, and the other companies follow the same pattern (Brackenmere's GLN 9523710900008 and GTIN 9523710000012). The item, however, is Valdara's: brand Valdara, manufacturer Valdara Industries (Urvania), made in Urvania, and its GTIN is said to be issued by Codana. Under the GS1 GTIN allocation rules (own knowledge) the brand owner allocates the GTIN from its own prefix; a distributor allocates one only when the brand owner has none, and then it is no longer the manufacturer's identification. Either the GTINs or Lumeway's keys are under the wrong company prefix.
- Condition: The GTINs of Valdara's items and Lumeway's GLNs, SSCCs and GRAIs are under different GS1 company prefixes, or the story states that Lumeway allocated the GTINs and the item identification says so.
- Options: Give Valdara its own company prefix for its GTINs (preferred: Valdara is the brand owner, and Codana as issuer points to Urvania), or state that the distributor allocated the GTINs. The check digits of all keys are correct either way.
- Needs decision: yes

### retail/19#F5 · Low · Lumeway's customs trader number in a document without customs
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: Lumeway (`AccountingSupplierParty`) carries its customs trader identifier `XB-TR-410274`. Nothing in this flow is declared to customs: every movement in it is inside Bayvarra (Marrowdale to Lumeport), and no example of the flow is a customs document. The identifier looks copied from Lumeway's master data (section 4.8 of the review).
- Condition: Lumeway's party in this document carries no customs identifier, unless the document is used for customs.
- Options: Leave the customs trader identifier out of the documents of this domestic flow (preferred) and keep it for the import and export flows where customs use it.
- Needs decision: no

### retail/19#F6 · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: UBL defines `PartyLegalEntity/CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount. The value here is a sum of money (`currencyID="XBL"`), i.e. the share capital, which is not what the definition says; for Lumeway, a private limited company, the definition's "corporation" fits only loosely. This is a conflict between the UBL definition and its data type rather than a choice the example can resolve alone, so it is a candidate for the findings recorded for the OASIS UBL TC.
- Condition: Either the share capital is no longer carried in `CorporateStockAmount`, or the use is recorded as a finding against the UBL definition (semantic conformance, UBL 2.5 §4.7/§7.2) and kept on purpose.
- Options: Record it as a finding against the UBL definition and keep the value where a document needs the share capital (invoices); keep it here, since an invoice may legally have to show it. The decision is the same for every example.
- Needs decision: yes

### retail/19#F7 · Low · Lumeway's sales customer-service contact does not fit its role here
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway's primary contact (`AccountingSupplierParty`) is "Customer service", a customer service officer in Sales, the contact a buyer uses. In this document Lumeway is the accounting supplier; the order names its accounting contact, `08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`. The party is copied with its sales contact into every role it has in the flow.
- Condition: The contact of Lumeway in this document is the one that handles what this document is about.
- Options: Give Lumeway a role-specific contact in this document (preferred, the order shows the flow already knows them), or leave the contact out where the document does not need one.
- Needs decision: no

### retail/19#F8 · Low · Brightmarket's contact: name, job title and department disagree, and do not fit the role
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: The primary contact of Brightmarket (`AccountingCustomerParty`) is named "Buying office" with the e-mail buying@brightmarket.example, but its job title is "Customer service officer" and its department "Sales": a buying office is part of purchasing, not of sales. In this document it is the accounting customer, whose contact deals with the invoice; the order `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:AccountingContact/cbc:Name` = `Accounts payable` names that contact, and neither the buying office nor a sales customer-service officer is it. The same contact is used in every role Brightmarket has in the flow (41 XML files contain `<cbc:Name>Buying office</cbc:Name>`, all with this job title; `grep -rl --include='*.xml'`).
- Condition: The name, job title and department of Brightmarket's contact in this document agree with each other and with Brightmarket's role here.
- Options: Make the master contact consistent (e.g. Buying office / Buyer / Purchasing), and give Brightmarket role-specific contacts where its role is not purchasing (goods-in for delivery and consignee roles, accounts payable for invoices, customer service for sales to consumers). Preferred: role-specific contacts, since the flow already has them in the order.
- Needs decision: no

### retail/19#F9 · Low · Brightmarket's consumer-facing master data copied into a trade document
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Brightmarket (`AccountingCustomerParty`) carries  its online shop and its photo social-media profile. This document is exchanged between trading partners (CreditNote) and does nothing with a consumer online shop or a social-media profile; the values look copied from Brightmarket's master data, which is the same in every example of the flow (section 4.8 of the review: data copied into a document that does not use it).
- Condition: Brightmarket's party in this document carries only data this document uses.
- Options: Leave the logo, online shop and social-media profile out of the trade documents and keep them for the consumer documents (the purchase receipt and the consumer order), where they have a reason.
- Needs decision: no

### retail/19#F10 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The registration date `1996-01-01` is shared by 25 different parties of the world (counted over `world/examples/*/*.xml` with lxml: distinct `PartyLegalEntity/RegistrationName` per `RegistrationDate`), among them Bayforth Forwarding, Harbourline Factoring, Codana Identification Agency, Brackenmere Furniture and Castrano Logistics, while every other party has a date of its own (e.g. Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January for unrelated companies in three countries is a filler, not a fact of the world (rule "no fillers").
- Condition: The registration date of each party here is a date with a reason in the world's history, or it is absent.
- Options: Give each party its real registration date from its history (preferred), or leave the date out where the history has none.
- Needs decision: yes

### retail/19#F11 · Low · The factor's contact is its client service, not the debtor's
- XPath: `/CreditNote/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/CreditNote/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: Harbourline is the payee as the factor that bought Lumeway's receivable. In factoring the "client" is the seller (Lumeway); Harbourline's contact here is "Client accounts", a client relationship manager in Client services, i.e. Lumeway's contact at the factor. The party that reads the payee in this document is the debtor, Brightmarket, whose contact at a factor would be its debtor or collections department (own knowledge of factoring practice).
- Condition: The payee's contact is the one the debtor uses for payment questions.
- Options: Give Harbourline a debtor-facing contact (e.g. collections) in the invoices it is payee of (preferred).
- Needs decision: no

## Checked and consistent
- Roles: supplier, customer, buyer and seller are those of the invoice `LD-INV-26-0236` it corrects (`18-Invoice.xml`).
- Every party is described the same way in every example of the flow: each of the full descriptions of Brightmarket Stores, Lumeway Distribution, Bayforth Forwarding and Harbourline Factoring is identical in all examples that carry it (compared leaf by leaf over all 22 XML files), and the short references (register identifier and name) match them.
- Party identifiers: the register identifiers (Brightmarket 20410411, Lumeway 20410274, Bayforth 20411644, Harbourline 20411233) agree with `PartyLegalEntity/CompanyID` and with the endpoint identifiers `XB:<register number>`; `check_ids.py` finds the check digits of all GS1 keys and IBAN-like accounts in this example correct. The GLN prefix 952 is GS1's prefix for demonstrations and examples (own knowledge), so the GLNs cannot be mistaken for real ones.
- Tax schemes: each Bayvarran party is registered for the state sales tax (STT) of the state its address is in (Lumeway Upland State, the others Coastal State), with matching jurisdiction.

## Considered and refuted
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`: suspected as copied master data — refuted for this document, because an invoice or credit note may be rendered with the logos of its parties.
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected of misusing BlockName for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits a business park, and `PlotIdentification` "Plot 14" is the land parcel as defined.
