# LLM review: 01-CatalogueRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/01-CatalogueRequest.xml`, Git blob `571e96113517945d8ea407ef7718908cdaf87ade` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 89446f0 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### retail/01#F1 · Medium · Requested catalogue reference points to a catalogue that is not the one supplied
- XPath: `/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ID` = `LD-CAT-26-0218`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ActionCode` = `NEW`
- Why: UBL defines `RequestedCatalogueReference` as "A reference to a specific Catalogue; used if the Catalogue Request is for an update." The request therefore says it asks for an update of an existing catalogue `LD-CAT-SPRING-26`. No example carries a document with that ID (searched over `world/examples/*/*.xml`), and the catalogue that answers this request, 02-Catalogue, is a new catalogue (`ActionCode` `NEW`) with another ID. Either the request is for a new catalogue (then the reference has no reason to be there) or it updates an earlier catalogue (then 02 is not a new catalogue and should reference it).
- Condition: the request either carries no `RequestedCatalogueReference`, or its ID is the ID of the catalogue that 02-Catalogue updates, and 02-Catalogue's action code agrees.
- Options: (a, preferred) drop the reference: the story is a first spring catalogue for a new supply agreement, and 02 is `NEW`; (b) keep an update story, make 02 an update of the referenced catalogue (action code and `PreviousVersionID` consistent with it).
- Needs decision: yes

### retail/01#F2 · Medium · Language codes in LocaleCode
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:RequestedLanguage/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region (English as used in Bayvarra), not the language itself, which is already in `Language/cbc:ID`. The value `en` with `listID` `ISO 639` is the language code repeated. The same pattern (`<cbc:LocaleCode listID="ISO 639">en`) occurs 362 times in 213 examples (counted with `grep -rho --include='*.xml'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language plus region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop `LocaleCode` where the parties have no locale-specific need; (b) use a locale code such as `en-XB` with a list that defines it (BCP 47 style), if a regional variant of English matters in the world.
- Needs decision: no

### retail/01#F3 · Medium · Classification scheme: a non-HS code inside the HS scheme, and a note that does not match the codes
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cac:CategorizesClassificationCategory/cbc:CodeValue` = `FUR-OUT-SP`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cbc:CodeValue` = `9401`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:Note` = `Six-digit subheadings.`
- Why: the requested classification scheme is the WCO Harmonized System 2022 (`ID` `HS`, agency WCO). `CategorizesClassificationCategory` is "A recursive description of a subcategory of this category", so its code must be an HS code below heading 9401; `FUR-OUT-SP` is not an HS code (it reads like a party-internal category code). The note asks for six-digit subheadings, but the categories given are a four-digit heading and a non-HS code. The HS subheading for parts of seats is 9401.99 (own knowledge); in 02-Catalogue the spare side frame is in fact classified under `732599` (cast articles of iron or steel), outside heading 9401, so the category "Spare parts" under "Seats" also does not match how the supplier classifies the part.
- Condition: every `CodeValue` in the HS scheme is an HS code at the level the note states, and the subcategory is a real subdivision of its parent.
- Options: (a, preferred) give HS codes only (e.g. 9401 with subheadings 940179 and, for the spare part, the subheading the catalogue uses), and align the note; (b) if Brightmarket wants its own category tree, request it as a separate classification scheme with its own ID and agency.
- Needs decision: no

### retail/01#F4 · Medium · A vehicle gate as additional street name in a postal address
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is not a street name; it is a delivery or vehicle access detail, which does not belong in a postal address. The same value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: Lumeway's postal address holds no gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate in the delivery or loading location where a vehicle needs it (e.g. a `Location` description or `Delivery` instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/01#F5 · Low · Brightmarket's buying office described as customer service in sales
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact of the party requesting a catalogue as a buyer is its buying office, which fits the role; but the job title and department are those of a seller's customer service. Name, job title and department contradict each other. The identical contact is used for Brightmarket in all 19 retail examples where it appears with detail (compared with a script over `world/examples/retail/*.xml`).
- Condition: name, job title and department of Brightmarket's contact agree with each other and with a buying role.
- Options: (a, preferred) job title and department of a buyer (e.g. "Buyer", "Purchasing"); (b) a different contact per role where later documents need one (goods receiving, accounts payable).
- Needs decision: no

### retail/01#F6 · Low · Values without a business reason in the description of the HS scheme
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:UUID` = `1afc0bc8-8a3e-5d36-b5be-437211032bac`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:LastRevisionTime` = `00:00:00`
- Why: the HS has no UUID assigned by its maintaining agency, so a UUID here is invented for a real scheme; and the last revision of HS 2022 has no time of day (it entered into force on 1 January 2022, own knowledge); `00:00:00` is a placeholder. Both are fillers in the sense of the no-filler rule.
- Condition: the scheme description carries only values that the WCO scheme actually has.
- Options: (a, preferred) drop both; (b) keep the UUID only if the world defines one as a shared identifier of the scheme across the Trade Accord, and say so.
- Needs decision: no

### retail/01#F7 · Low · Document name is the catalogue's name, not the request's
- XPath: `/CatalogueRequest/cbc:Name` = `Spring catalogue 2026`
- Why: `Name` is "Text, assigned by the sender, that identifies this document to business users". This document is the request for the catalogue; its name reads as the name of the catalogue requested (which in 02-Catalogue is named differently, `Lumeway Distribution catalogue`).
- Condition: the request's name identifies the request (or is absent).
- Options: (a, preferred) a name such as "Request for the spring catalogue 2026"; (b) drop it.
- Needs decision: no

## Checked and consistent
- Parties: `ProviderParty` (Brightmarket) is the sender, as UBL defines it for the Catalogue Request, and `ReceiverParty` is Lumeway; seller and contractor customer agree with 02-Catalogue. Both parties are described identically in every retail example (compared by script).
- `LineCountNumeric` `2` matches the two request lines; validity period 2026-04-20 to 2026-07-19 equals the one in 02-Catalogue, and line 1's end date matches it.
- Contract `LD-BM-SUPPLY-2026` is the contract 02-Catalogue references; line items (Serra 180 bench, side frame casting) are the two lines of 02-Catalogue.
- Requested minimum of 24 each with "Pallet prices, please." fits 02-Catalogue's pallets of four (24 = 6 pallets).
- GLNs `9520610900008` and `9522610900002` pass the check digit (check_ids.py); prefix 952 is GS1's range for demonstrations, so they cannot be mistaken for real GLNs.
- ISIC codes 4649 (wholesale of household goods, including furniture) and 4719 fit Lumeway and Brightmarket.

## Considered and refuted
- `/CatalogueRequest/cbc:PricingUpdateRequestIndicator`, `/CatalogueRequest/cbc:ItemUpdateRequestIndicator`: suspected to contradict a request for a new catalogue — refuted because they can be read as asking to be kept informed of price and item changes, which 03-CataloguePricingUpdate and 04-CatalogueItemSpecificationUpdate then do.
- `/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`: suspected unresolved reference with only an ID — refuted because the same ID is Brightmarket's range document, cited as such in `furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID`; a document outside the flow is legitimate.
- `/CatalogueRequest/cac:TradingTerms/cbc:Information` = `Delivered duty paid to the store.`: suspected an Incoterm used for a domestic sale — refuted because DDP can be agreed domestically and the text only states who bears transport.
