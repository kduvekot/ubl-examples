# LLM review: 11-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/11-ReceiptAdvice.xml`, Git blob `6223208a8a0ee6befbffd7cfc33c817e4bdf5f7e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/11#F1 · High · Emission value is not factor × base
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 per 1 EA gives 0.82 kg, not 96; 96 / 0.82 = 117.1 matches nothing in the flow, nor does 0.82 × 56.5 kg of material = 46.3 kg (recalculated in the merge). 39 examples carry the triple (over `*.xml`).
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` equals `ValueMeasure`, or factor and base are absent.
- Options: (a, preferred, as rail and air) drop factor and base; (b) a factor and base the 96 kg are calculated from.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F3, Medium)

### road/11#F2 · Medium · The carrier's CMR waybill referenced as a delivery note
- XPath: `/ReceiptAdvice/cac:Shipment/cac:Delivery/cac:DeliveryNoteDocumentReference/cbc:ID` = `TH-WB-26-0159`
- XPath: `08-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `CMR`
- XPath: `/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`
- Why: `DeliveryNoteDocumentReference` is "a reference to a Delivery Note associated with this Delivery". TH-WB-26-0159 is the carrier's CMR consignment note, a transport contract document, not the supplier's delivery note; the document that accompanies the goods from the supplier's side is the despatch advice, already referenced. A reference element for one document kind is used for another. Broad listed the reference as resolving correctly, which is true of the target but not of its kind.
- Condition: `DeliveryNoteDocumentReference`, if present, refers to a delivery note; the waybill, if referenced, is referenced as a transport document.
- Options: (a, preferred) an `AdditionalDocumentReference` with document type Waybill (the signed CMR is the consignee's proof of receipt); (b) drop it.
- Needs decision: no
- From: logistics (F2)

### road/11#F3 · Medium · Lifecycle stage code MANUFACTURING for a cradle-to-gate figure
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `MANUFACTURING` is module A3 in the world list; the texts cover A1–A3. Code and text name different stages.
- Condition: code and text name the same stage(s), and the figure covers exactly them.
- Options: (a, preferred) omit the code (or two entries); (b) reduce figure and texts to A3.
- Needs decision: no
- From: context (F1, High)

### road/11#F4 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty …"; the value is from the world's `EmissionBoundaryCode` list (semantic conformance).
- Condition: absent from this item emission, or says how full transport equipment is.
- Options: (a, preferred) drop it, boundary in text, missing element for the UBL TC write-up.
- Needs decision: no
- From: context (F2)

### road/11#F5 · Medium · Language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 occurrences in 213 files.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F2), context (F5), parties (F1, yes)

### road/11#F6 · Medium · Gate number in AdditionalStreetName of the delivery customer's postal address
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is an entrance, not a street. If the receipt needs the place of unloading, it belongs in the delivery location.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop it from the address.
- Needs decision: no
- From: broad (F3), parties (F2)

### road/11#F7 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address uses (`/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`).
- Condition: the province is in `CountrySubentity`.
- Options: (a, preferred) move it; (b) define Urvanian provinces as economic regions.
- Needs decision: no
- From: broad (F4), context (F4), parties (F3)

### road/11#F8 · Low · Contacts that do not fit a receipt advice
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the receipt advice comes from goods-in, but Lumeway's contact is its customer service in Sales; Castrano's contact is named `Warehouse office` but has a sales customer-service title and department, so name, title and department disagree.
- Condition: the delivery customer's contact is goods-in; the despatch supplier's contact has a name, title and department that agree and fit the warehouse.
- Options: (a, preferred) goods-in for Lumeway, a warehouse title and department for Castrano; (b) drop titles and departments that do not fit.
- Needs decision: no
- From: broad (F5), context (F6), parties (F4)

### road/11#F9 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID"; 1 January is a public holiday and the date occurs 271 times across the examples for at least 25 companies (parties' count over `*.xml`), while Lumeway and Valdara have their own dates (IND5).
- Condition: each party's registration date is its own plausible date, or absent.
- Options: (a, preferred) a date from Castrano's history; (b) leave it out.
- Needs decision: yes (aligned with rail and air)
- From: parties (F5, no)

### road/11#F10 · Low · Seller's stock-exchange listing in a receipt advice
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: a receipt advice reports what arrived; the seller's listing plays no part (section 4.8, IND5).
- Condition: every optional party aggregate present has a reason in the receipt's purpose.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: parties (F6), context (F7, listing part)

### road/11#F11 · Low · Product passport and catalogue data copied into the receipt advice
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission`
- Why: the receipt needs item identification and description; keywords, warranty, circularity and the emission figure play no part (section 4.8).
- Condition: the item carries what reporting the receipt needs.
- Options: (a, preferred) reduce the item to identification and description.
- Needs decision: no
- From: context (F7, item part)

### road/11#F12 · Low · Received side frames not identified as the substituted 2026 casting
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- Why: the order response substituted the 2026 casting (and also proposed the 2025 casting from stock); the receipt records only VI-C180, so it does not show which casting arrived, and the application response's match "to the substituted 2026 casting" (`16-ApplicationResponse.xml`) has nothing in the goods documents to match against. The same gap is in `04-DespatchAdvice.xml`.
- Condition: the receipt line identifies the casting version as the order response identifies the substitute.
- Options: (a, preferred) `ExtendedID` 2026; (b) drop the version distinction everywhere.
- Needs decision: no
- From: logistics (F3)

### road/11#F13 · Low · Item number reads as a real GTIN-12
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: 12 digits with a valid GS1 mod-10 check digit (recomputed: 7; 4 for the side frame), so they read as GTIN-12s of a real GS1 prefix range (own knowledge). Only the bench carries symbology and issuer scope.
- Condition: the item numbers cannot be read as check-digit-valid GTINs of a real GS1 prefix.
- Options: (a, preferred) a non-GS1 structure or the example prefix 952; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where unused.
- Needs decision: yes
- From: broad (F6)

### road/11#F14 · Low · Italian street names tagged as English
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: the second rendering of the Urvanian street names is Italian text with `languageID` `en-XB`. Parties refuted it: English keeps foreign street names unchanged and the region subtag follows the sender. Against that: the tag says the text is English, which the words are not, and the other rendering is in Urvanian (`qau`), so the Italian form is a third language without a tag of its own. The merge cannot settle which reading the world intends; aligned with rail and the other road merges (Low, decision). Counted by rail over `*.xml`: 217 such renderings in 102 files.
- Condition: one rule for Italian-form names in English renderings, recorded in the world's language rules, and the tags follow it.
- Options: (a, preferred) record that English renderings keep the Italian exonym (then no change); (b) tag the Italian form with an Italian language tag.
- Needs decision: yes
- From: merge (parties considered and refuted it)

### road/11#F15 · Low · Urvanian legal forms in one untagged rendering
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: in Urvania-issued documents the same legal forms come in two tagged renderings (`qau` and `en-XU`); in this Bayvarra-issued document they are one untagged text, so the same party is described differently across the flow and the language of the text is not stated. Added by the merge, aligned with rail, air and the other road merges.
- Condition: the legal form is rendered as in the other documents of the flow (both renderings, tagged), or in one rendering with its language tag.
- Options: (a, preferred) render it as the address is rendered in this document.
- Needs decision: no
- From: merge

## Checked and consistent
- References: order LD-PO-26-0149 (`01`), despatch advice CL-DA-26-0153 lines 1 and 2 (`04`), waybill TH-WB-26-0159 (`08`, see F2 for the element), shipment CL-SH-26-0154 (broad, logistics, context).
- Quantities (redone in the merge): line 1 received 95 + short 1 = 96 despatched; line 2 received 13 − oversupply 1 = 12; 95 + 13 = 108 = the waybill's `TotalPackagesQuantity`; the note and line notes (one pallet held three benches and a box) agree; one box holds one casting (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[25]/cac:Package/cbc:Quantity` = `12` boxes for 12 frames), so "one box over" is one casting.
- Actual delivery 2026-03-25 09:40 within the waybill's estimated window 09:00–11:00, before the required 10:00, after the status update to 09:30; issued afterwards at 15:40; `ReceiptAdviceTypeCode` Actual fits (broad, logistics, context).
- Castrano's `ShareholderParty` (Valdara, 100 %) agrees with Valdara's `ServiceProviderParty` (parties).
- Party identity, GLN and ISIN check digits (parties).

## Considered and refuted
- `/ReceiptAdvice/cbc:DeliveryAcceptanceCode` = `ACCEPTED` with a shortage and an oversupply — refuted because the buyer accepts what arrived and handles the shortage by `ShortageActionCode` (from broad, logistics and context).
- The receipt contradicts the despatch advice and the waybill (24 pallets of 4 benches) — refuted because revealing a mis-pick is the purpose of this receipt advice (from broad).
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:Note` contradicted by the recount in `13-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedQuantity` = `96` — refuted because this receipt advice is cancelled for exactly that reason (`12-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The recount found the bench reported short; the shortage did not exist.`) (from context).
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ShortageActionCode` = `REPLACE`, named "Deliver the rest" in the world list — refuted because delivering the missing quantity is what replacing it means here (from context).
- `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XB` — refuted by parties; the merge does not follow and made it F14.
- `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN could be real — refuted, prefix 952, check digit correct (from parties).
- `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: could be real — refuted, +999 reserved (from parties).
- `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01` as a contract number — refuted, the definition does not say who assigns it (from parties).

## Refuted in the merge
### context/F7 · Low · Master and product data the receipt advice does nothing with (shareholder part)
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- Why (context): the despatch supplier's shareholder plays no part in reporting the receipt (section 4.8, IND5).
- Condition (context): party and item data in the receipt advice have a use in reporting the receipt.
- Refuted because: the shareholding (Valdara owns Castrano) explains why Castrano, not the seller, is the despatch supplier of Valdara's goods, which the receipt advice answers; parties checked it as consistent, and merger C refuted the same part for `13-ReceiptAdvice.xml`. The rest of context/F7 is kept as F10 and F11.

## Changed in the merge
- broad/F1, logistics/F1, context/F3 → F1: High (context Medium); preferred option drop factor and base, as rail and air.
- context/F1 → F3: High lowered to Medium, aligned with rail and air.
- parties/F1 → F5: Needs decision no, aligned.
- parties/F5 → F9: Needs decision yes, aligned with rail and air.
- context/F7 split into F10 (listing, with parties/F6), F11 (item data) and the shareholder part refuted in the merge.
- New F14 (Italian tags) from parties' refuted candidate and new F15 (untagged legal forms), aligned with rail, air and merger C.
