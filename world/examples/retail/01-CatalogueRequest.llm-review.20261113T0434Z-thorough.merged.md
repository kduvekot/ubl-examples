# LLM review: 01-CatalogueRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/01-CatalogueRequest.xml`, Git blob `571e96113517945d8ea407ef7718908cdaf87ade` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/01#F1 · Medium · Request for an update of a catalogue that exists nowhere, answered by a new catalogue
- XPath: `/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- XPath: `/CatalogueRequest/cbc:PricingUpdateRequestIndicator` = `true`
- XPath: `/CatalogueRequest/cbc:ItemUpdateRequestIndicator` = `true`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ID` = `LD-CAT-26-0218`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ActionCode` = `NEW`
- Why: UBL defines `RequestedCatalogueReference` as "A reference to a specific Catalogue; used if the Catalogue Request is for an update", and the two indicators as "Indicates a request for a pricing update" and "Indicates a request for an update of the item specifications". The request thus asks for an update of a catalogue `LD-CAT-SPRING-26`. No example carries that ID (verified: `grep -rl --include='*.xml' LD-CAT-SPRING-26` finds only this file). The catalogue that answers the request, 02-Catalogue (same ProfileExecutionID, issued the same day), has another ID, is a new catalogue (`ActionCode` `NEW`, every line `ADD`) and does not refer to `LD-CAT-SPRING-26` (it carries a `PreviousVersionID` `0.9` that points the other way, see 02#F2). Either the request is for a new catalogue, and the reference has no reason, or it is for an update, and 02 is not a new catalogue. The indicators are the weaker part: broad refuted them as a request to be kept informed of later price and item changes, which 03 and 04 then deliver; that reading is possible, so the indicators alone would not be a finding, but together with the reference they make the request one for an update.
- Condition: either the request carries no `RequestedCatalogueReference` (and no update indicators, or the indicators are explained as a subscription to later updates), or the referenced ID is that of a catalogue which 02-Catalogue updates or replaces, consistent with 02's `ActionCode` and `PreviousVersionID`.
- Options: (a, preferred, all three parts) a request for a new spring catalogue: drop the reference (and the indicators unless they mean "keep me informed"), since 02 is `NEW` and 03/04 are the later updates; (b) keep an update story: make 02 an update or replacement of the referenced catalogue. Settle together with 02#F2.
- Needs decision: yes
- From: broad, logistics, context

### retail/01#F2 · Medium · A language code in LocaleCode
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:RequestedLanguage/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region (English as used in Bayvarra). The value `en` with `listID` `ISO 639` is the language code itself and repeats `Language/cbc:ID`; ISO 639 is a list of languages, not of locales. Section 6 names "a language code in LocaleCode" as a Medium case. The same element value occurs 362 times in 213 files (verified: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `-rl` for the files; the parts' 364 comes from a looser pattern).
- Condition: every `LocaleCode` holds a locale (language plus region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop `LocaleCode` where nothing depends on a locale (fix in the party master data, so it applies to every example); (b) a locale such as `en-XB` with a listID for a locale list (BCP 47 style), which context preferred because the parties and the catalogue are Bayvarran.
- Needs decision: no
- From: broad, parties, logistics, context

### retail/01#F3 · Medium · HS scheme with a non-HS subcategory, a note that does not match the codes, and a description wider than the heading
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cac:CategorizesClassificationCategory/cbc:CodeValue` = `FUR-OUT-SP`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:CodeValue` = `9401`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:Description` = `Outdoor furniture and its spare parts.`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:Note` = `Six-digit subheadings.`
- Why: the requested scheme is the WCO Harmonized System 2022 (`ID` `HS`, agency WCO). `CodeValue` is "The value of a code used to identify this category within the classification scheme", and `CategorizesClassificationCategory` "A recursive description of a subcategory of this category"; `FUR-OUT-SP` is not an HS code (it reads like a party-internal category). The note asks for six-digit subheadings, but the categories are a four-digit heading and a non-HS code. Heading 9401 is "Seats", not "outdoor furniture" (outdoor tables are 9403), and parts of seats are subheading 9401.99 (9401.91 of wood); own knowledge of HS 2022. 02-Catalogue then classifies the spare side frame outside heading 9401 (see 02#F24).
- Condition: every `CodeValue` inside the HS scheme is an HS 2022 code at the level the note states, the subcategory is a real subdivision of its parent, and the description matches the heading.
- Options: (a, preferred) category `9401` "Seats" with subcategory `940199` (parts of seats, other than of wood) and the note aligned; (b) if Brightmarket wants its own category tree, a second classification scheme of its own with its ID and agency.
- Needs decision: no
- From: broad, logistics, context

### retail/01#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is an entrance of the distribution centre at Distribution Drive 43, a detail for vehicles, not a street name; a postal address holds nothing that only matters for vehicles. The value occurs 79 times in 76 files (verified with `grep -rho` / `grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`; where a transport document needs the gate, it is in that document's pickup or delivery location.
- Options: (a, preferred) drop it from the postal address (party master data) and give the gate in a location `Description` or as a location identifier where vehicles need it; (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition, and the finding is dismissed.
- Needs decision: no
- From: broad, parties

### retail/01#F5 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: Brightmarket sends the request as a buyer; its contact's name and e-mail fit a buying office, but the job title and department are those of a seller's customer service (they are identical to Lumeway's own contact, `/CatalogueRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`). Name, job title and department contradict each other. The same contact is used for Brightmarket in every role (verified: 41 files contain `<cbc:Name>Buying office</cbc:Name>`, 19 of them in retail).
- Condition: name, job title and department of Brightmarket's contact agree with each other and with a buying role.
- Options: (a, preferred) a buyer's job title in a purchasing department, and role-specific contacts where Brightmarket's role is not buying (goods-in, accounts payable); (b) only make the master contact consistent.
- Needs decision: no
- From: broad, parties, context

### retail/01#F6 · Low · Party master data the request does nothing with
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueRequest/cac:ProviderParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- Why: a catalogue request asks for prices and items between two trading partners. Share capital, Lumeway's customs trader number (every movement of the flow is inside Bayvarra and no example of the flow is a customs document; the number is in 20 retail files), Brightmarket's logo, consumer online shop and social-media profile, and both tax registrations play no part in it; they are the parties' master data, identical in every example of the flow (section 4.8). In addition, UBL defines `CorporateStockAmount` as "The number of shares in the capital stock of a corporation", while the value is a sum of money (`currencyID` `XBL`), i.e. the share capital: a conflict between the UBL definition and its Amount data type that is a candidate for the write-up to the OASIS UBL TC (parties).
- Condition: the parties carry what the request uses (identification, name, address, contact, electronic address); anything else has a reason in this document.
- Options: (a, preferred) leave legal-entity capital, customs, tax, logo, web-shop and social-media detail out of this document (keep the consumer-facing data for the receipts and consumer orders, the customs number for customs flows); (b) where a document needs the share capital (company law on invoices), keep it and record the definition conflict as a finding for the TC.
- Needs decision: no
- From: parties (three findings), context

### retail/01#F7 · Low · Invented UUID and midnight revision time for the real Harmonized System
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:UUID` = `1afc0bc8-8a3e-5d36-b5be-437211032bac`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:LastRevisionTime` = `00:00:00`
- Why: the scheme is the real WCO HS 2022. WCO assigns it no UUID, so the UUID exists only in this document; HS 2022 entered into force on 1 January 2022 (`LastRevisionDate` `2022-01-01`, correct), and `00:00:00` is not a time anyone revised it (own knowledge). Both are fillers.
- Condition: the scheme description carries only facts about HS (ID, name, agency, version, date, URIs).
- Options: (a, preferred) drop both; (b) keep the UUID only if the world defines it as a shared identifier of the scheme in the Trade Accord, and say so.
- Needs decision: no
- From: broad, context

### retail/01#F8 · Low · Document reference with an ID only
- XPath: `/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: the reference has no `DocumentTypeCode` or `DocumentType`, so the receiver cannot tell what `BM-RANGE-26` is or why it needs it to answer. The only other occurrence is `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`, where it is Brightmarket's range catalogue (verified). Broad refuted it as an unresolved reference (a document outside the flow is legitimate); that is right for its existence, but not for what it is.
- Condition: the reference says what kind of document `BM-RANGE-26` is (type code or type text), or is absent.
- Options: (a, preferred) add a document type (e.g. "Brightmarket range plan 2026"); (b) drop it.
- Needs decision: no
- From: logistics, context

### retail/01#F9 · Low · Signature without anything that signs
- XPath: `/CatalogueRequest/cac:Signature/cbc:ID` = `BM-SIG-26-0420`
- Why: Signature is "A signature applied to this document". It holds only an ID and the signatory party: no method, no attachment, no original document reference, no validation date, so nothing a receiver could check, and a catalogue request has no legal effect that needs a signature in the story (IND5/IND6). It is a world-wide convention: 137 of 147 `Signature` aggregates hold only ID and SignatoryParty (counted with lxml over `world/examples/*/*.xml`).
- Condition: either the signature has a business reason and the data that make it a signature, or it is absent.
- Options: (a, preferred) drop it; (b) give it a method and attachment and a reason in the story.
- Needs decision: yes (a convention across the world; aligned with the earlier flows' merges)
- From: context

### retail/01#F10 · Low · Document name is the catalogue's name, not the request's
- XPath: `/CatalogueRequest/cbc:Name` = `Spring catalogue 2026`
- Why: `Name` is "Text, assigned by the sender, that identifies this document to business users". This document is the request; its name reads as the name of the catalogue requested (which in 02 is named differently, `02-Catalogue.xml:/Catalogue/cbc:Name` = `Lumeway Distribution catalogue`). Context refuted it: a request named after its subject identifies it well enough. That is possible, but a request and the catalogue it asks for then carry names a business user can confuse, so it stays a remark.
- Condition: the request's name identifies the request (or is absent).
- Options: (a, preferred) a name such as "Request for the spring catalogue 2026"; (b) drop it.
- Needs decision: no
- From: broad (context refuted)

## Checked and consistent
- Roles: `ProviderParty` (Brightmarket) is "The Party who sends the Catalogue Request", `ReceiverParty` Lumeway; seller and contractor customer agree with 02-Catalogue.
- `LineCountNumeric` `2` matches the two request lines; validity period 2026-04-20 to 2026-07-19 starts on the issue date and equals 02's (`02-Catalogue.xml:/Catalogue/cac:ValidityPeriod/cbc:EndDate` = `2026-07-19`); line 1's end date matches it.
- Contract `LD-BM-SUPPLY-2026` is the one 02 references; the two request lines are the two lines of 02.
- Requested minimum of 24 each with "Pallet prices, please." fits 02's pallets of four (24 = 6 pallets) and its 4–192 band; 08-Order then buys 24 (`08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `24`).
- GLNs `9520610900008` and `9522610900002` pass the GS1 check digit (check_ids.py); prefix 952 is GS1's range for demonstrations.
- ISIC 4649 and 4719 fit Lumeway and Brightmarket; register identifiers agree with `PartyLegalEntity/CompanyID` and the endpoint IDs; each party is registered for the state sales tax of its own state.
- All parties are described identically in every example of the flow (parties, leaf by leaf).
- HS 2022 with LastRevisionDate 2022-01-01; heading 9401 and version 2022 match the HS codes of 02.
- DDP to the store matches 08 (`08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`).

## Considered and refuted
- `/CatalogueRequest/cbc:PricingUpdateRequestIndicator`, `/CatalogueRequest/cbc:ItemUpdateRequestIndicator`: suspected to contradict a request for a new catalogue — refuted on their own because they can be read as asking to be kept informed of later price and item changes, which 03 and 04 do (from broad; context made them part of its finding, so they are kept as the weaker part of F1).
- `/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`: suspected unresolved — refuted because it is Brightmarket's range document, cited as such in `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` (from broad; the missing document type is F8).
- `/CatalogueRequest/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store.`: suspected an Incoterm odd for a domestic sale — refuted because Incoterms may be used domestically, DDP to the store means delivered with all costs paid, and it also covers the import of the Urvanian-made benches the distributor bears (from broad, money, logistics, context).
- `/CatalogueRequest/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits it, and `PlotIdentification` is the land parcel (from parties).
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `24`: suspected to contradict 02's pallet of four — refuted because 24 benches are six pallets, the quantity from which a pallet price is asked (from logistics, context).
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:LineValidityPeriod/cbc:EndDate`: repeats the header's end date — refuted because a line validity may coincide with the header (from context).
- `/CatalogueRequest/cbc:Name`: request named after its subject — refuted by context; not followed by the merge, kept as F10.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; context's update indicators added as the weaker part, with broad's refutation of them in the Why.
- broad/F2, parties/F1, logistics/F3, context/F2 → F2: combined; logistics' "Needs decision: yes" set to no, aligned with every part here and every earlier flow (dropping the code is an encoding fix); count corrected to 362 in 213 files.
- broad/F3, logistics/F2, context/F3 → F3: combined (logistics' description/heading point added).
- broad/F4, parties/F2 → F4: combined.
- broad/F5, parties/F6, context/F4 → F5: combined.
- parties/F3 (customs trader ID), parties/F4 (CorporateStockAmount, Low/yes), parties/F5 (logo, web shop, social media), context/F6 → F6: grouped into one finding per example, as in the furniture and cotton merges; parties/F4's "Needs decision: yes" set to no because the fix (leave it out where unused) changes no story, its definition conflict kept as a TC write-up note and as option (b).
- broad/F6, context/F7 → F7: combined.
- logistics/F4, context/F8 → F8: combined.
- context/F5 → F9: "Needs decision" no → yes, aligned with the air and utilities merges (a convention across 137 of 147 signatures).
- broad/F7 → F10: unchanged, context's refutation added to the Why.
