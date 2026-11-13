# LLM review: 01-RequestForQuotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/01-RequestForQuotation.xml`, Git blob `25a98f65310576bccebca7415f6252636f7b9a02` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/01#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language as used in a region (English as used in Bayvarra), not the language itself. The value `en` with `listID="ISO 639"` is an ISO 639 language code and only repeats the `Language/ID` next to it, so it carries the meaning of another element. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` for the files), in every example of this flow.
- Condition: every `cac:Language/cbc:LocaleCode` is absent, or holds a locale (language plus region) from a list that defines locales, named in its `listID`, and different from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`: nothing in the flow depends on a regional variant of English (preference of context and parties, and of the merges of every earlier flow); (b) a locale such as `en-XB` from a BCP 47-style list (broad's preference).
- Needs decision: no
- From: broad, context, parties

### furniture/01#F2 · Low · CatalogueDocumentReference points to the store's own range document, not a Catalogue
- XPath: `/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`
- XPath: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: The element is "The Catalogue on which this Request for Quotation is based"; a UBL Catalogue is the document in which a provider describes the items it offers. `BM-RANGE-26` carries the buyer's own prefix (as in `/RequestForQuotation/cac:Signature/cbc:ID` = `BM-SIG-26-RFQ`), no example has it as its document ID, and the only other example that carries it uses it as a plain document reference in a catalogue request to another supplier, i.e. as the store's own range plan (verified with Grep over `world/examples/*/*.xml`: these two places only). The requested item is the maker's model with the maker's item number and GTIN, and no Catalogue of Brackenmere appears in the flow. With only an ID, the reader cannot tell what the document is. Whether the store's range plan counts as a catalogue cannot be settled from the examples.
- Condition: `CatalogueDocumentReference` refers to a Catalogue (of the seller, or one the store publishes), or is absent; the range plan, if referenced, uses an element that does not claim it is a catalogue, with a document type or description that says what it is.
- Options: (a, preferred) an `AdditionalDocumentReference` with a description or document type "range plan", as the retail flow uses the ID (preference of broad and logistics); (b) remove the reference and leave the range in the note (context's preference: nothing else in the flow uses it); (c) keep it if the story makes BM-RANGE-26 a catalogue, then also in the retail flow, and describe it.
- Needs decision: yes
- From: broad, context, logistics

### furniture/01#F3 · Low · Originator and beneficiary repeat the buyer
- XPath: `/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/RequestForQuotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") carry information when they are someone other than the buyer (a requisitioning department, an end customer). Here both are the buyer itself, with the same register number `20410411`, so they add nothing and suggest a distinction the story does not have. The broad part considered this and refuted it: with nothing implied by absence (IND6), stating that the store is also originator and beneficiary is a legitimate explicit statement. The merge keeps the finding because the definitions carry no condition that makes the statement necessary, and IND5 asks for a business reason, which no document of the flow gives (none uses the two roles).
- Condition: originator and beneficiary are absent, or each names a party other than `BuyerCustomerParty` with its own role in the story.
- Options: (a, preferred) remove both; (b) name a real originator (e.g. the store's garden department) if the story wants one, which is a story change.
- Needs decision: no
- From: context, parties (broad refuted it, see Why)

### furniture/01#F4 · Low · Brackenmere's registration date 1 January 1996
- XPath: `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge does not settle it either way and keeps it as a finding, for alignment with the merges of every earlier flow, which kept the same value as Low with a decision: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), including Brackenmere in every example of this flow, while Brightmarket has its own date (`/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`). A date shared by so many unrelated companies reads as a default rather than part of their histories.
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact (e.g. a register opened on that day).
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event and record it; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

### furniture/01#F5 · Low · Brightmarket's contact: buying office with a sales job title and department
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores is the buyer here. Its contact is named "Buying office", but its job title is "Customer service officer" in the "Sales" department, which serves the store's own customers: name, title and department do not agree with each other, and a sales customer-service desk is not the contact of a buyer. The same contact is used wherever Brightmarket is described in full in this flow.
- Condition: name, job title and department of Brightmarket's contact agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buying contact (job title e.g. "Buyer", department "Purchasing"; in billing documents an accounts-payable contact); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/01#F6 · Low · Store master data copied into the request
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo reference, online-shop website ("An additional web site associated with this party"), photo-sharing profile ("A social media profile associated with this party") and share capital are party master data; a request for quotation for an own-line garden set does nothing with any of them (section 4.8). The same four elements are carried on Brightmarket Stores in examples 01 to 14 of the flow (`BM-LOGO-2024` in 14 files, Grep over `world/examples/furniture/*.xml`). The parties part refuted the logo: the line is the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`), so the logo could have a reason in the sourcing documents. The merge keeps the logo as the weakest part of the finding: nothing in this request says the logo is to be used for the label, and the same logo is carried in documents (sales reports, notifications) that have no label at all.
- Condition: each of these elements is present only in a document that has a reason to carry it; a logo kept for the own label is tied to it in the document (e.g. a line note or an attached artwork).
- Options: (a, preferred) remove them here; (b) keep the logo only if the request uses it for the own-label artwork, and say so.
- Needs decision: no
- From: context, parties (parties refuted the logo part)

### furniture/01#F7 · Low · DAP delivery terms without their named place
- XPath: `/RequestForQuotation/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: An Incoterms rule is complete only with its named place ("DAP <named place of destination>", own knowledge of Incoterms 2020). UBL gives `DeliveryTerms` its own `DeliveryLocation` ("The location for the contracted delivery"), and the order of this flow uses it (`08-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`). Here the terms carry only the rule; the place is in the separate `Delivery` aggregate, so a quotation based on the request has to infer that the two belong together.
- Condition: the DAP terms name their place, in `DeliveryTerms/DeliveryLocation` (preferably with the goods-in GLN) or by an unambiguous link to the delivery location.
- Options: (a, preferred) add `DeliveryTerms/DeliveryLocation` with the goods-in GLN `9522610900019`, the same location as in `retail/08-Order.xml`; (b) keep the `Delivery` aggregate as the only place and accept the implied link.
- Needs decision: no
- From: logistics

### furniture/01#F8 · Low · DestinationCountry "for customs purposes" in a domestic request
- XPath: `/RequestForQuotation/cac:DestinationCountry/cbc:IdentificationCode` = `XB`
- Why: `DestinationCountry` is "The country of destination of potential orders (for customs purposes)". Buyer (Lumeport, Coastal State), seller (Marrowdale, Upland State), the item's origin (`/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`) and the delivery place are all in Bayvarra. The goods cross no customs border, so there is no customs purpose for the element to serve (IND5).
- Condition: `DestinationCountry` is absent, or the request describes a cross-border supply in which customs applies.
- Options: (a, preferred) remove it; the delivery location already says where the goods go; (b) if the store wants to rule out an imported supply, say so in a note.
- Needs decision: no
- From: broad, context, logistics

### furniture/01#F9 · Low · Optional cushions requested only in a note next to a non-optional line
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:Note` = `Optional: seat cushions to match.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:OptionalLineItemIndicator` = `false`
- Why: The line note asks for optional matching seat cushions, while UBL has a dedicated mechanism for optional requested items: a line with `OptionalLineItemIndicator` ("An indication whether this line is optional (true) or not (false) for purposes of this request for quotation") set to true. The line that carries the note is the bench set and is not optional, so the note sits next to an indicator that says the opposite. The quotation `02-Quotation.xml` neither quotes nor declines the cushions (one line, no note on cushions), so the request leads nowhere in the flow.
- Condition: either the cushions are a request line of their own with `OptionalLineItemIndicator` = `true` (and the quotation answers it), or the note no longer asks for them.
- Options: (a, preferred) remove the note, since nothing in the flow follows from it; (b) add an optional cushion line and let 02 quote or decline it.
- Needs decision: yes
- From: broad, context

### furniture/01#F10 · Low · Line confidentiality and security classification give two levels
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` = `CONFIDENTIAL`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode` = `INTERNAL`
- Why: `PrivacyCode` is "the level of confidentiality of this request for quotation line" and `SecurityClassificationCode` "the security classification of this request for quotation line". The same line gets "Confidential" in one and "Internal" in the other, leaving two different handling levels for one line. An own-brand development has a business reason for marking the line (which is why the broad part refuted the suspicion that both are fillers), but not obviously for two different levels.
- Condition: the two codes express one consistent handling level, or only one of them is present.
- Options: (a, preferred) keep `PrivacyCode` and drop the security classification: the confidentiality of an own-brand range is a commercial, not a security matter; (b) align both to the same level.
- Needs decision: no
- From: context

### furniture/01#F11 · Low · Maker's brand on an item for the store's own line
- XPath: `/RequestForQuotation/cbc:Note` = `For the store's own garden line.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: `BrandName` is "A brand name of this item". The note, the description, the contract `BM-OWN-BRAND-2026` and the quotation's note (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`) all describe a private-label product of Brightmarket, which is normally sold under the retailer's brand, not the maker's. The brand `Brackenmere` points the other way unless the story means a co-branded or maker-branded exclusive line, which is why this needs a decision. The garden set carries this brand in all 12 furniture examples that carry the item (`BF-GS-01`; Grep over `world/examples/furniture/*.xml`).
- Condition: the item's brand and the texts about the line agree, consistently in every example that carries the item: either the brand is the store's own-line brand, or the texts no longer say it is the store's own line or label.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) keep `Brackenmere` and reword the texts to an exclusive maker-branded line made for the store.
- Needs decision: yes
- From: broad, context

## Checked and consistent
- GS1 check digits of the GLNs `9523710900008`, `9522610900002`, `9522610900019` and the GTIN `9523710000012` (`check_ids.py`, re-run by the merge). Prefix 952 is the GS1 range for demonstrations and examples (own knowledge), so the keys cannot be mistaken for real ones. `XBL` is not an assigned ISO 4217 code (own knowledge).
- Dates: `/RequestForQuotation/cbc:SubmissionDueDate` = `2026-03-07` follows the issue date 2026-03-02; the quotation `02-Quotation.xml` was issued on 2026-03-06, in time, and its validity end 2026-05-05 is the requested 60 days (`/RequestForQuotation/cac:RequestedValidityPeriod/cbc:DurationMeasure` = `60`) after its issue date.
- The goods-in GLN `9522610900019` is the store's goods-in in `retail/08-Order.xml` as well.
- Item: 20 sets; HS 940169 and CPC 38112 fit a wooden-framed seat set; the bench length 1400 mm agrees with the sub-item name "Garden bench Marrow, 1400 mm" in `08-Order.xml` and fits a three-seat garden bench (about 1.2 to 1.6 m, own knowledge).
- `cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`: an own-brand agreement as the contract of an own-line request fits the element.
- Party data of Brackenmere and Brightmarket (identifiers, address, tax scheme, legal entity, contact, electronic address) are identical in every example of the flow where they are given in full (broad and parties compared them element by element); register number, legal-entity `CompanyID` and electronic-address suffix agree per party (20412466, 20410411), and the tax identifiers carry the prefix of the party's state (UL-, CO-).

## Considered and refuted
- `/RequestForQuotation/cac:RequestForQuotationLine/cbc:PrivacyCode` and `/RequestForQuotation/cac:RequestForQuotationLine/cbc:SecurityClassificationCode`: suspected fillers — refuted because a store's own-line development is commercially confidential, a business reason to mark the line (from broad; the two different levels are F10).
- `/RequestForQuotation/cac:Signature/cbc:ID`: a signature without method or attachment — refuted because the element only identifies the signature applied, and the signatory is the issuing buyer, which fits a binding request (from broad, context).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode`: HS code in a domestic request suspected to be without purpose — refuted because the definition includes regulatory and trade-statistics purposes and the code describes the item, not a customs movement (from context).
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:OriginCountry`: origin of a domestic product suspected to be a filler — refuted because origin marking is a legitimate requirement for a store's own line (from context).
- `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name`: suspected a company name instead of a place — refuted because it names the store's goods-in, a place at the company, identified by its GLN, and `retail/08-Order.xml` names the same GLN in the same way (from logistics, parties).
- `/RequestForQuotation/cac:Contract/cbc:ID`: suspected an unresolvable reference — refuted because a framework contract is not a UBL document of the world and need not exist as an example; its contradiction with the contract IDs used later in the flow belongs to the reviews of `11-OrderCancellation.xml` and `14-DebitNote.xml` (from logistics).
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge); the same holds for every 952… key here (from parties).
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: the +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the web and mail domains are under the reserved `.example` domain (from parties).
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact in roles other than selling — refuted because Brackenmere is a small enterprise whose trade-sales desk plausibly handles the whole customer relationship; name, title and department agree with each other (from parties).
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: Brackenmere's address in a state-level register while the Lumeport parties use a city register — refuted because address registers are kept by country level, and Bayvarra keeps them per state or city, as the schemeIDs show (from parties).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: `Name` and `ID` hold the account handle and number rather than the platform — refuted because the aggregate is the profile, and naming and identifying the profile is a legitimate reading; the presence of the profile is part of F6 (from parties).
- `/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID`: the logo as master data without use — refuted by parties (own label); the merge disagrees in part and keeps it in F6 with this argument.
- `/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; the merge made it F4 (see there).
- `/RequestForQuotation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` and `/RequestForQuotation/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: redundant copies of the buyer — refuted by broad (IND6); the merge kept it as F3 (see there).

## Changed in the merge
- broad/F1, context/F1, parties/F1 → F1: combined; preferred option set to removal (context, parties and the earlier flows' merges), broad's `en-XB` kept as option (b); count re-verified with the exact pattern.
- broad/F2, context/F2, logistics/F3 → F2: combined; the three preferences listed as options (a) to (c).
- context/F4, parties/F4 → F3: combined; broad's refutation carried into Why with the merge's counter-argument.
- parties' refuted RegistrationDate → F4: made a finding (Low, needs decision) for alignment with the merges of all earlier flows, which kept the same shared date as Low/yes.
- broad/F5, parties/F2 → F5: combined.
- context/F7, parties/F3 → F6: grouped into one finding with one XPath line per element (website and social profile from both parts, logo and share capital from context); the parties' refutation of the logo carried with the merge's counter-argument.
- broad/F6, context/F3, logistics/F1 → F8: combined; same severity in all parts.
- broad/F4, context/F5 → F9: combined.
- broad/F3, context/F8 → F11: combined; the count of examples verified (12 examples carry the item `BF-GS-01`; `BrandName` `Brackenmere` occurs in 14, two of them for the public works order).
