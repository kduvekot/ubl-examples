# LLM review: 01-RequestForQuotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/01-RequestForQuotation.xml`, Git blob `25a98f65310576bccebca7415f6252636f7b9a02` (committed)
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

### furniture/01#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. a language in a region (English as used in Bayvarra), not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats `cac:Language/cbc:ID` = `en` next to it, so it carries the meaning of another element. The same value `<cbc:LocaleCode listID="ISO 639">en` occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`), in every furniture example.
- Condition: each `cbc:LocaleCode` either holds a locale code (language plus territory) from a locale code list named in its `listID`, or is absent.
- Options: (a) remove `LocaleCode` where nothing in the world depends on a locale (preferred: the documents use no locale-dependent formatting); (b) use a locale such as `en-XB` from a list that defines locales.
- Needs decision: no

### furniture/01#F2 · Low · CatalogueDocumentReference points to the buyer's own range, not a Catalogue
- XPath: `/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: The element is defined as "The Catalogue on which this Request for Quotation is based"; a UBL Catalogue is the document in which a provider describes the items it offers. The `BM-` prefix is the buyer's own numbering (as in `/RequestForQuotation/cac:Signature/cbc:ID` = `BM-SIG-26-RFQ`), and the note `/RequestForQuotation/cbc:Note` = `For the store's own garden line.` points to the store's own range plan. A buyer's range plan is not a Catalogue in the UBL sense, and no Catalogue of Brackenmere appears in the flow.
- Condition: `CatalogueDocumentReference` refers to a Catalogue of the seller (by the seller's numbering), or is absent; a reference to the buyer's range plan, if needed, is an `AdditionalDocumentReference` or contract reference with a type that says what it is.
- Options: (a) remove the reference and leave the range in the note (preferred: nothing else in the flow uses it); (b) keep it as an additional document reference with a document type "range plan"; (c) if the story has a seller catalogue, refer to it by Brackenmere's number.
- Needs decision: yes

### furniture/01#F3 · Low · DestinationCountry for a domestic request
- XPath: `/RequestForQuotation/cac:DestinationCountry/cbc:IdentificationCode` = `XB`
- Why: `DestinationCountry` is defined as "The country of destination of potential orders (for customs purposes)". Buyer (Lumeport, Coastal State) and seller (Marrowdale, Upland State) are both in Bayvarra, the item's origin is `XB` and delivery is to the store's goods-in in Lumeport: there is no border and no customs purpose. The value is valid but has no business reason in this request (IND5).
- Condition: `DestinationCountry` is absent, or the story gives the request a cross-border destination.
- Options: (a) remove it (preferred); (b) none other seen.
- Needs decision: no

### furniture/01#F4 · Low · Originator and beneficiary repeat the buyer
- XPath: `/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/RequestForQuotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") carry meaning when they differ from the buyer (a requisitioning department, an end customer). Here both are the buyer itself, with the same register number `20410411`, so they add nothing and imply a distinction that does not exist.
- Condition: both are absent, or each names a party other than `BuyerCustomerParty` with its own role in the story.
- Options: (a) remove both (preferred); (b) name a real originator (e.g. the garden department) if the story wants one.
- Needs decision: no

### furniture/01#F5 · Low · Optional cushions requested only in free text next to a non-optional line
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:OptionalLineItemIndicator` = `false`
- Why: The request asks for an optional item (cushions) in the line note, while UBL has a dedicated mechanism for optional requested items: a line with `OptionalLineItemIndicator` ("An indication whether this line is optional (true) or not (false) for purposes of this request for quotation") set to true. The line that carries the note is the bench set and is not optional, so the note sits next to an indicator that says the opposite of "optional". The quotation `02-Quotation.xml` neither quotes nor declines the cushions.
- Condition: either the cushions are a request line of their own with `OptionalLineItemIndicator` = true (and the quotation answers it), or the note is gone.
- Options: (a) remove the note (preferred if the cushions play no role in the flow); (b) add an optional line for the cushions and let the quotation answer it.
- Needs decision: yes

### furniture/01#F6 · Low · Line confidentiality and security classification disagree
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode` = `INTERNAL`
- Why: `PrivacyCode` is "the level of confidentiality of this request for quotation line" and `SecurityClassificationCode` "the security classification of this request for quotation line". Giving the same line the level "Confidential" in one and "Internal" in the other leaves a reader with two different handling levels for one line; an own-brand request has a reason for one of them, not obviously for two different ones.
- Condition: the two codes express one consistent handling level, or only one of them is present.
- Options: (a) keep `PrivacyCode` and drop the security classification (preferred: confidentiality of an own-brand range is a commercial, not a security matter); (b) align both to the same level.
- Needs decision: no

### furniture/01#F7 · Low · Buyer's master data copied into the request
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo reference, online-shop website, photo-sharing profile and share capital are party master data; a request for quotation does nothing with any of them (section 4.8). The same four elements are carried on Brightmarket Stores in examples 01 to 14 of the flow (Grep over `world/examples/furniture/*.xml`).
- Condition: each of these elements is present only in a document that has a reason to carry it.
- Options: (a) remove them here (preferred); (b) keep one only if the story gives it a use in this request (e.g. the logo for the own-label artwork, then say so).
- Needs decision: no

### furniture/01#F8 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: `BrandName` is "A brand name of this item". The description, the note `/RequestForQuotation/cbc:Note` = `For the store's own garden line.`, the contract `BM-OWN-BRAND-2026` and the quotation's note `02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.` all describe a store's own-brand (private-label) product, which is sold under the retailer's brand, not the maker's. The brand `Brackenmere` contradicts that unless the story means a co-branded exclusive line. The same `BrandName` occurs on this item in 12 furniture examples.
- Condition: the item's brand name is the brand it is sold under in the story (the store's own label, or explicitly both), consistently in every example that carries the item.
- Options: (a) the store's own label as `BrandName` (preferred: it is what "own line" and "own label" mean); (b) keep `Brackenmere` and change the texts to an exclusive maker-branded line.
- Needs decision: yes

## Checked and consistent
- `cac:RequestedValidityPeriod/cbc:DurationMeasure` (60 days) and `SubmissionDueDate` 2026-03-07: the quotation `02-Quotation.xml` is issued 2026-03-06 and valid to 2026-05-05, 60 days after its issue.
- `cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`: an own-brand agreement as the contract of an own-line request fits the element.
- `cac:Delivery/cac:DeliveryLocation` (store goods-in GLN) and `DeliveryTerms` DAP: fit a request for delivered prices; GS1 check digits pass (`check_ids.py`).

## Considered and refuted
- `/RequestForQuotation/cac:Signature`: a signature with only ID and signatory party was suspected to be a filler — refuted because the element only says a signature is applied; the signatory is the issuing buyer, which fits a binding request.
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode`: HS code in a domestic request was suspected to be without purpose — refuted because the definition includes regulatory and trade-statistics purposes, and the code belongs to the item's description, not to a customs movement (unlike `DestinationCountry`, which is defined only for customs purposes).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:OriginCountry`: origin of a domestic product was suspected to be filler — refuted because origin marking is a legitimate requirement for a store's own line.
