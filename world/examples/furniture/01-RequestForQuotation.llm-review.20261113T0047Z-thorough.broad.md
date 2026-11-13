# LLM review: 01-RequestForQuotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/01#F1 · Medium · Language code in LocaleCode
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/01#F2 · Low · Catalogue reference points to the store's own range document
- XPath: `/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`
- XPath: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: `CatalogueDocumentReference` is "The Catalogue on which this Request for Quotation is based"; a UBL Catalogue describes a seller's items and prices. `BM-RANGE-26` carries Brightmarket's own prefix, and in the retail flow the same identifier is cited by Brightmarket as a plain `DocumentReference` in a catalogue request to another supplier, i.e. as the store's own range document, not as a catalogue. No example has `BM-RANGE-26` as a Catalogue ID (searched over `*.xml`). Whether the store's range plan counts as a catalogue cannot be settled from the examples.
- Condition: The reference in `CatalogueDocumentReference` identifies a catalogue (a seller's catalogue, or a catalogue the store publishes), or the range document is referenced with an element that does not claim it is a catalogue.
- Options: (a, preferred) reference `BM-RANGE-26` as an `AdditionalDocumentReference` with a document type that says it is the store's range plan, as the retail flow does; (b) keep it if the world decides the range is a Brightmarket catalogue (then it should be a catalogue in the retail flow too).
- Needs decision: yes

### furniture/01#F3 · Low · Own-line item carries the maker's brand
- XPath: `/RequestForQuotation/cbc:Note` = `For the store's own garden line.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/01#F4 · Low · Optional cushions mentioned in a note, not as an optional line
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:OptionalLineItemIndicator` = `false`
- Why: The request asks, in the line note, for optional seat cushions, while the line's `OptionalLineItemIndicator` ("whether this line is optional … for purposes of this request for quotation") is false and there is no line for cushions. UBL has a structure for exactly this (a second line with the indicator true). The quotation `02-Quotation.xml` neither quotes nor declines cushions, so the optional request leads nowhere in the flow.
- Condition: Either the optional cushions are requested as their own RFQ line with `OptionalLineItemIndicator` true (and the quotation responds to it), or the note no longer asks for them.
- Options: (a) drop the note, since nothing in the flow follows from it (preferred, smaller change); (b) add a cushion line with the indicator true and quote or decline it in 02.
- Needs decision: yes

### furniture/01#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

### furniture/01#F6 · Low · Destination country for customs purposes in a domestic request
- XPath: `/RequestForQuotation/cac:DestinationCountry/cbc:IdentificationCode` = `XB`
- Why: `DestinationCountry` is "The country of destination of potential orders (for customs purposes)". Buyer, seller, origin (`OriginCountry` = XB) and delivery are all in Bayvarra; there is no customs purpose, so the element has no business reason here (IND5).
- Condition: `DestinationCountry` is absent, or the request involves a cross-border delivery that needs it.
- Options: (a, preferred) remove it; (b) keep it only if the world makes this a cross-border sourcing.
- Needs decision: no

## Checked and consistent
- GS1 check digits of the GLNs `9523710900008`, `9522610900002`, `9522610900019` and the GTIN `9523710000012` (check_ids.py). The 952 prefix is the GS1 range reserved for demonstrations and examples (own knowledge), so the keys cannot be mistaken for real ones.
- `/RequestForQuotation/cbc:SubmissionDueDate` = `2026-03-07`: the quotation `02-Quotation.xml` is issued on 2026-03-06, in time; its validity (end 2026-05-05) matches the requested 60 days from 2026-03-06.
- `XBL` is not an assigned ISO 4217 code (own knowledge: the assigned X-codes near it are XBA–XBD).
- HS 940169 and CPC 38112 fit a wooden-framed seat set; the bench length 1400 mm agrees with the sub-item name "Garden bench Marrow, 1400 mm" in `08-Order.xml`.
- Party data of Brackenmere and Brightmarket (address, tax scheme, legal entity, contact, electronic address) are identical in all examples of the flow (compared element by element over the XML).

## Considered and refuted
- `/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` and `/RequestForQuotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: suspected redundant copies of the buyer — refuted because, with nothing implied by absence (IND6), stating that the store is also originator and beneficiary of its own-line request is a legitimate explicit statement.
- `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` and `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode`: suspected fillers — refuted because a store's own-line development is commercially confidential, which is a business reason to mark the line.
- `/RequestForQuotation/cac:Signature/cbc:ID`: a signature without method or attachment — refuted because the element only identifies the signature applied; how it is applied is not required.
