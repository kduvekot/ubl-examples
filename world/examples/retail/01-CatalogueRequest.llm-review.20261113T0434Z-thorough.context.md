# LLM review: 01-CatalogueRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### retail/01#F1 · Medium · Update reference and update indicators in a request for a new catalogue
- XPath: `/CatalogueRequest/cac:RequestedCatalogueReference/cbc:ID` = `LD-CAT-SPRING-26`
- XPath: `/CatalogueRequest/cbc:PricingUpdateRequestIndicator` = `true`
- XPath: `/CatalogueRequest/cbc:ItemUpdateRequestIndicator` = `true`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:ActionCode` = `NEW`
- Why: UBL defines RequestedCatalogueReference as "A reference to a specific Catalogue; used if the
  Catalogue Request is for an update", and the two indicators as requests for a pricing update and
  for an update of the item specifications. The catalogue that answers this request,
  02-Catalogue.xml (ID `LD-CAT-26-0218`, same ProfileExecutionID, issued the same day), is sent as a
  new catalogue (ActionCode `NEW`, all lines `ADD`). No example of the flow has the ID
  `LD-CAT-SPRING-26`, so the request asks for an update of a catalogue that, as far as the flow
  shows, does not exist, and the answer treats it as a request for a new one. (02-Catalogue.xml
  itself carries a PreviousVersionID `0.9`, which points the other way; see its own review.)
- Condition: either the request is for a new catalogue (no RequestedCatalogueReference, no update
  indicators, or indicators false), or it is for an update of a catalogue that the answer
  identifies as such (the answer is an update/replacement of the referenced catalogue).
- Options: (a) preferred: make it a request for a new spring catalogue and drop the reference and
  the indicators, since 02 is a new catalogue and 03/04 are the later updates; (b) keep the update
  request and make 02 a replacement of `LD-CAT-SPRING-26`, which changes 02's story.
- Needs decision: yes

### retail/01#F2 · Medium · A language code in LocaleCode
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CatalogueRequest/cac:RequestedLanguage/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used", i.e. a locale
  (language plus region, such as English as used in Bayvarra). The value is the bare ISO 639 language
  code, with listID `ISO 639`, which only repeats Language/ID. The same pattern
  (`LocaleCode listID="ISO 639"`) occurs in 213 examples (counted with `grep -l` over `*.xml` in
  `world/examples`).
- Condition: every LocaleCode holds a locale code from a locale list (or is absent where no locale is
  meant).
- Options: (a) preferred: a locale code (e.g. a BCP 47 tag with the country, `en-XB`) with a matching
  listID, because the parties and the requested catalogue are Bayvarran; (b) drop LocaleCode where
  only the language matters.
- Needs decision: no

### retail/01#F3 · Medium · A code that is not an HS code in the HS classification scheme
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cac:ClassificationCategory/cac:CategorizesClassificationCategory/cbc:CodeValue` = `FUR-OUT-SP`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:ID` = `HS`
- Why: CategorizesClassificationCategory is "A recursive description of a subcategory of this
  category" within the classification scheme, here the WCO Harmonized System 2022. `FUR-OUT-SP` is
  not an HS code (HS codes are numeric headings and subheadings; parts of seats of heading 9401 are
  subheading 9401.99, from own knowledge of HS 2022). It looks like a party-internal category placed
  in the WCO scheme.
- Condition: every CodeValue under the HS scheme is an HS heading or subheading, or the internal
  category is described under a scheme of its own.
- Options: (a) preferred: the HS subheading for parts of seats (`940199`), which fits the note
  "Six-digit subheadings."; (b) a second RequestedClassificationScheme for the buyer's or seller's own
  category scheme.
- Needs decision: no

### retail/01#F4 · Low · Buyer's buying office described as a sales customer-service contact
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:Contact/cbc:Department` = `Sales`
- Why: the provider of the request is the buyer, Brightmarket. Its contact is named "Buying office",
  but job title and department are those of the supplier's contact (compare
  `/CatalogueRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`,
  `/CatalogueRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`). A buying office is not
  in the sales department.
- Condition: the buyer's contact has a job title and department of a buying function.
- Options: e.g. a buyer job title in a purchasing department.
- Needs decision: no

### retail/01#F5 · Low · Signature without anything that signs
- XPath: `/CatalogueRequest/cac:Signature/cbc:ID` = `BM-SIG-26-0420`
- Why: Signature is "A signature applied to this document". Here it has only an ID and the signatory
  party: no signature method, no digital signature attachment, no original document reference, no
  validation date. It records nothing a receiver could check, and a catalogue request has no need for
  a signature in the story (no legal effect, no authority). Without such a reason it is a filler
  (UBL IND5/IND6).
- Condition: either the signature has a business reason and the data to make it a signature, or it
  is absent.
- Options: (a) preferred: drop it; (b) give it a method and attachment and a reason in the story.
- Needs decision: no

### retail/01#F6 · Low · Master data the request does nothing with
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/CatalogueRequest/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CatalogueRequest/cac:ProviderParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: a catalogue request asks for prices and items. Share capital, tax registrations, the
  supplier's customs trader number (both parties are in Bayvarra, nothing crosses a border) and the
  buyer's social media profile play no part in it; they look copied from the parties' master data.
- Condition: the parties carry what the request uses (identification, name, address, contact,
  electronic address), and anything else has a reason in this document.
- Options: drop legal-entity, tax and social-media detail from both parties here.
- Needs decision: no

### retail/01#F7 · Low · Invented UUID and midnight revision time for the real Harmonized System
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:UUID` = `1afc0bc8-8a3e-5d36-b5be-437211032bac`
- XPath: `/CatalogueRequest/cac:RequestedClassificationScheme/cbc:LastRevisionTime` = `00:00:00`
- Why: the scheme is the real WCO HS 2022. WCO assigns it no UUID, so the UUID is a value that only
  exists in this document; the revision "time" 00:00:00 is not a time anyone revised the scheme (HS
  2022 entered into force on 1 January 2022, from own knowledge). Both are fillers.
- Condition: the scheme carries only facts about HS (ID, name, agency, version, URIs).
- Options: drop both.
- Needs decision: no

### retail/01#F8 · Low · Document reference that does not say what it is
- XPath: `/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: the reference has only an ID. Nothing in the document says what `BM-RANGE-26` is (a range
  plan of the buyer?) or why the supplier needs it to answer, and no example of the flow carries it.
- Condition: the reference states what kind of document it is (DocumentTypeCode or DocumentType) or
  is absent.
- Options: add a document type (preferred), or drop it.
- Needs decision: no

## Checked and consistent
- ProviderParty is the sender of the request (Brightmarket) and ReceiverParty the catalogue provider
  (Lumeway), as the definitions require; SellerSupplierParty and ContractorCustomerParty agree with
  02-Catalogue.xml.
- ValidityPeriod 2026-04-20 to 2026-07-19 is the period of 02-Catalogue.xml; the referenced contract
  `LD-BM-SUPPLY-2026` is the one 02-Catalogue.xml carries.
- LineCountNumeric `2` matches the two request lines; the line items are those of the two catalogue
  lines of 02-Catalogue.xml.
- The HS heading `9401` and the version `2022` match the HS codes used in 02-Catalogue.xml.

## Considered and refuted
- `/CatalogueRequest/cac:TradingTerms/cbc:Information`: "Delivered duty paid" in a domestic trade
  (both parties in Bayvarra) — refuted because Incoterms 2020 may be used for domestic sales, and DDP
  then simply means delivered to the store with all costs paid.
- `/CatalogueRequest/cbc:Name`: the request is named after the catalogue it asks for — refuted
  because a request named for its subject identifies it well enough to business users.
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity`:
  24 benches while 02-Catalogue.xml sells pallets of four — refuted because the buyer asks for a price
  break at its own pallet volume; the catalogue answering with smaller pallets is no contradiction.
- `/CatalogueRequest/cac:CatalogueRequestLine[1]/cac:LineValidityPeriod/cbc:EndDate`: repeats the
  header's end date — refuted because a line validity may legitimately coincide with the header.
