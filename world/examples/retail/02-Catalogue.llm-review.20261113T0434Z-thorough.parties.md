# LLM review: 02-Catalogue.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/02-Catalogue.xml`, Git blob `1c92d827b4d756ddbac6f7506b2c222c22480912` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/02#F1 · Medium · Language/LocaleCode holds the language code, not a locale
- XPath: `/Catalogue/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". Every party language here has `LocaleCode` = `en` with `listID="ISO 639"`: the ISO 639 code of the language itself, which repeats `Language/cbc:ID` and names no locale (no country or region in which English is used). ISO 639 is a list of languages, not of locales. The world does have locales: Urvanian addresses carry renderings tagged `languageID="en-XB"` (English as used in Bayvarra). The checklist of the review names "a language code in LocaleCode" as a Medium case. The same value occurs 364 times in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `-rl … | wc -l` for the files).
- Condition: No `Language/cbc:LocaleCode` of a party holds a bare language code; where a `LocaleCode` is present it identifies a locale and its `listID` names a list of locales.
- Options: Drop `LocaleCode` from the parties' languages (preferred: nothing in this document depends on a locale, so it has no business reason, and `Language/cbc:ID` already says English); or give a real locale (e.g. English as used in Bayvarra) with a `listID` for a locale list such as BCP 47. The fix belongs in the party master data, so it applies to every example at once.
- Needs decision: no

### retail/02#F2 · Medium · A site gate in AdditionalStreetName of Lumeway's address
- XPath: `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is not a street name but an entrance of the distribution centre at Distribution Drive 43; it only matters to vehicles that load or unload there, and the postal address of the party holds nothing for vehicles (checklist of the review: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles"). The same value occurs 79 times in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: No `AdditionalStreetName` holds "Gate 3"; Lumeway's postal address holds only postal parts, and where a transport document needs the gate it is given in the pickup or delivery location, not in a street element.
- Options: Remove the gate from Lumeway's postal address (preferred), and where a transport document needs it, say it in that location's `Description` (or as a location identifier of the gate, e.g. a GLN of the dock). Fix it in the party master data.
- Needs decision: no

### retail/02#F3 · Medium · Codana's province in Region
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located". The Province of Ferrano is an administrative subdivision of Urvania, i.e. a country subentity (`CountrySubentity`, "the subdivision of a country"); the review checklist names "a province in Region" as a Medium case. The address has no `CountrySubentity`. The same value is in `Region` 219 times (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: The province of Codana's address is in `CountrySubentity` (with its code where the world has one), and `Region` is absent or holds a region in the UBL sense.
- Options: Move the province to `CountrySubentity`/`CountrySubentityCode` (preferred); fix it in the address data so all 219 places change together.
- Needs decision: no

### retail/02#F4 · Low · Valdara's GTINs are in Lumeway's GS1 company prefix
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: Lumeway's GLN `9520610900008` and the GTIN of Valdara's bench share the GS1 company prefix 9520610. Across the world that prefix is Lumeway's: its rail-siding GLN 9520610900015 and every SSCC in the examples, all despatched by Lumeway (`12-DespatchAdvice.xml`, `air/03-ForwardingInstructions.xml`, `sea/14-BillOfLading.xml`), start with it, and the other companies follow the same pattern (Brackenmere's GLN 9523710900008 and GTIN 9523710000012). The item, however, is Valdara's: brand Valdara, manufacturer Valdara Industries (Urvania), made in Urvania, and its GTIN is said to be issued by Codana. Under the GS1 GTIN allocation rules (own knowledge) the brand owner allocates the GTIN from its own prefix; a distributor allocates one only when the brand owner has none, and then it is no longer the manufacturer's identification. Either the GTINs or Lumeway's keys are under the wrong company prefix.
- Condition: The GTINs of Valdara's items and Lumeway's GLNs, SSCCs and GRAIs are under different GS1 company prefixes, or the story states that Lumeway allocated the GTINs and the item identification says so.
- Options: Give Valdara its own company prefix for its GTINs (preferred: Valdara is the brand owner, and Codana as issuer points to Urvania), or state that the distributor allocated the GTINs. The check digits of all keys are correct either way.
- Needs decision: yes

### retail/02#F5 · Low · Lumeway's customs trader number in a document without customs
- XPath: `/Catalogue/cac:ProviderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: Lumeway (`ProviderParty`) carries its customs trader identifier `XB-TR-410274`. Nothing in this flow is declared to customs: every movement in it is inside Bayvarra (Marrowdale to Lumeport), and no example of the flow is a customs document. The identifier looks copied from Lumeway's master data (section 4.8 of the review).
- Condition: Lumeway's party in this document carries no customs identifier, unless the document is used for customs.
- Options: Leave the customs trader identifier out of the documents of this domestic flow (preferred) and keep it for the import and export flows where customs use it.
- Needs decision: no

### retail/02#F6 · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/Catalogue/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Catalogue/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: UBL defines `PartyLegalEntity/CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount. The value here is a sum of money (`currencyID="XBL"`), i.e. the share capital, which is not what the definition says; for Lumeway, a private limited company, the definition's "corporation" fits only loosely. Besides, nothing in this document uses the share capital (it is not an invoice or another business letter on which company law could require it). This is a conflict between the UBL definition and its data type rather than a choice the example can resolve alone, so it is a candidate for the findings recorded for the OASIS UBL TC.
- Condition: Either the share capital is no longer carried in `CorporateStockAmount`, or the use is recorded as a finding against the UBL definition (semantic conformance, UBL 2.5 §4.7/§7.2) and kept on purpose.
- Options: Record it as a finding against the UBL definition and keep the value where a document needs the share capital (invoices); leave it out here, where the document does not use it (preferred). The decision is the same for every example.
- Needs decision: yes

### retail/02#F7 · Low · Brightmarket's consumer-facing master data copied into a trade document
- XPath: `/Catalogue/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Catalogue/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Catalogue/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Brightmarket (`ReceiverParty`) carries its logo reference, its online shop and its photo social-media profile. This document is exchanged between trading partners (Catalogue) and does nothing with a logo, a consumer online shop or a social-media profile; the values look copied from Brightmarket's master data, which is the same in every example of the flow (section 4.8 of the review: data copied into a document that does not use it).
- Condition: Brightmarket's party in this document carries only data this document uses.
- Options: Leave the logo, online shop and social-media profile out of the trade documents and keep them for the consumer documents (the purchase receipt and the consumer order), where they have a reason.
- Needs decision: no

### retail/02#F8 · Low · Brightmarket's contact: name, job title and department disagree
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Catalogue/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: The primary contact of Brightmarket (`ReceiverParty`) is named "Buying office" with the e-mail buying@brightmarket.example, but its job title is "Customer service officer" and its department "Sales": a buying office is part of purchasing, not of sales. In this document it receives the document as the buyer, so "Buying office" fits, but the job title and department are those of a seller's customer service. The same contact is used in every role Brightmarket has in the flow (41 XML files contain `<cbc:Name>Buying office</cbc:Name>`, all with this job title; `grep -rl --include='*.xml'`).
- Condition: The name, job title and department of Brightmarket's contact in this document agree with each other and with Brightmarket's role here.
- Options: Make the master contact consistent (e.g. Buying office / Buyer / Purchasing), and give Brightmarket role-specific contacts where its role is not purchasing (goods-in for delivery and consignee roles, accounts payable for invoices, customer service for sales to consumers). Preferred: role-specific contacts, since the flow already has them in the order.
- Needs decision: no

### retail/02#F9 · Low · Codana: a private limited company with a public-service contact
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cbc:IndustryClassificationCode` = `8299`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyLegalFormCode` = `SRU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Name` = `Member services`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:Department` = `Public services`
- Why: Codana, the identification agency that issues GTINs and property identifiers, is described as a small private limited company (SRU) classified 8299 "Other business support service activities n.e.c.", yet its contact is "Member services", a "Public service officer" in "Public services". A members' service points to a membership organisation (as GS1 member organisations are; ISIC 9411, own knowledge), a public-service officer to a public body; neither fits a private company, and the name and the department of the contact disagree with each other.
- Condition: Codana's legal form, industry classification and contact describe the same kind of organisation.
- Options: Decide what Codana is (membership association, public agency or company) and align legal form, classification and contact with it; preferred: a not-for-profit membership association with a member-services contact, as identification agencies usually are.
- Needs decision: yes

### retail/02#F10 · Low · Full description of Codana as issuer of a GTIN
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:ID` = `4160200261972596`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007395206`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105644`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:Contact/cbc:ElectronicMail` = `member@codana.example`
- Why: The issuer of the GTIN in catalogue line 1 carries Codana's full description: address, tax registration, legal entity, contact and electronic address. The issuer of a standard item identification only needs to be identified (as in line 2, `/Catalogue/cac:CatalogueLine[2]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyName/cbc:Name` = `Codana Identification Agency`, with identifier and name only). Lumeway and Brightmarket do nothing with Codana's tax registration or contact; the data looks copied from master data (section 4.8 of the review).
- Condition: The issuer party of the GTIN carries what identifies it, as in line 2, and nothing the catalogue does not use.
- Options: Reduce the issuer to its identifier and name in both lines (preferred).
- Needs decision: no

### retail/02#F11 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The registration date `1996-01-01` is shared by 25 different parties of the world (counted over `world/examples/*/*.xml` with lxml: distinct `PartyLegalEntity/RegistrationName` per `RegistrationDate`), among them Bayforth Forwarding, Harbourline Factoring, Codana Identification Agency, Brackenmere Furniture and Castrano Logistics, while every other party has a date of its own (e.g. Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January for unrelated companies in three countries is a filler, not a fact of the world (rule "no fillers").
- Condition: The registration date of each party here is a date with a reason in the world's history, or it is absent.
- Options: Give each party its real registration date from its history (preferred), or leave the date out where the history has none.
- Needs decision: yes

## Checked and consistent
- Roles: Lumeway provides the catalogue to Brightmarket; the line parties (contractor customer, seller, warranty party, manufacturer, information content provider) are the parties the lines describe.
- Every party is described the same way in every example of the flow: each of the full descriptions of Brightmarket Stores, Lumeway Distribution, Bayforth Forwarding and Harbourline Factoring is identical in all examples that carry it (compared leaf by leaf over all 22 XML files), and the short references (register identifier and name) match them.
- Party identifiers: the register identifiers (Brightmarket 20410411, Lumeway 20410274, Bayforth 20411644, Harbourline 20411233) agree with `PartyLegalEntity/CompanyID` and with the endpoint identifiers `XB:<register number>`; `check_ids.py` finds the check digits of all GS1 keys and IBAN-like accounts in this example correct. The GLN prefix 952 is GS1's prefix for demonstrations and examples (own knowledge), so the GLNs cannot be mistaken for real ones.
- Tax schemes: each Bayvarran party is registered for the state sales tax (STT) of the state its address is in (Lumeway Upland State, the others Coastal State), with matching jurisdiction.

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:StandardItemIdentification/cac:IssuerParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Codici`: suspected of not being English although tagged `languageID="en-XB"` — refuted because the world consistently renders Urvanian street names in Bayvarran English with their Romance exonyms (e.g. "Via delle Officine" 31 times, "Via del Magazzino" 6 times under `languageID="en-XB"`, counted with `grep -rhoE --include='*.xml'`), the way English keeps foreign street names; the rendering is the name as Bayvarrans write it, not a translation.
- `/Catalogue/cac:CatalogueLine[1]/cac:WarrantyParty/cac:PartyName/cbc:Name` = `Valdara Industries`: checked whether the warranty party fits — it does: the line says the warranty is "from the maker", and Valdara is the manufacturer in `ManufacturerParty`.
- `/Catalogue/cac:ProviderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected of misusing BlockName for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits a business park, and `PlotIdentification` "Plot 14" is the land parcel as defined.
