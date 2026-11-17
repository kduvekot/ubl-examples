# What a document says about an item: the item table (O20)

Prepared 2026-11-17 for the owner's approval, before cause C48 (41 findings) is fixed. It applies the story line "What a document says about an item" (D11, `analysis/worklist-decisions.md`):

- a fact is stated first in the document of the moment it becomes known;
- a later document repeats it only if its own transaction uses it; otherwise it identifies the item, the lot or the earlier document.

The table is built into `tools/build_examples.py` (`ITEM_BLOCK`, `ITEM_KIND`, `ITEM_PROFILE`, `item_profiles()`). It is switched off (`APPLY_ITEM_PROFILE = False`) until the owner approves it, so the published examples are unchanged. All figures below come from a build with the switch on.

## How it works

`item()` writes an item's master data from `world/items.json`: the facts of the item type. The table decides which of those facts each kind of document keeps.

What a scenario adds for its own transaction always stays, whatever the table says. That covers:

- the variant chosen (the grey bench `GRY` in the seller's item identification);
- a colour made to order;
- a lot or a serial number (`ItemInstance`);
- a buyer's own item number.

## Blocks

| Block | Elements of `cac:Item` |
|---|---|
| name | `Name` |
| desc | `Description` |
| id | `SellersItemIdentification` (with the variant), `BuyersItemIdentification`, `StandardItemIdentification`, `ManufacturersItemIdentification`, `AdditionalItemIdentification`, `CatalogueItemIdentification`, `CatalogueDocumentReference` |
| tax | `ClassifiedTaxCategory` |
| class | `CommodityClassification` (HS, CPC, national tariff) |
| origin | `OriginCountry`, `OriginAddress` |
| instance | `ItemInstance` (lot, serial) |
| lot | a certificate of the lot rather than the type: the cotton classing certificate (`"layer": "lot"` in `world/items.json`) |
| dg | `HazardousItem` |
| brand | `BrandName` |
| warranty | `WarrantyInformation` |
| pack | `PackQuantity`, `PackSizeNumeric` |
| type | the facts of the item type: `Keyword`, `ModelName`, `AdditionalInformation`, `Dimension`, `AdditionalItemProperty`, `ItemSpecificationDocumentReference`, `LifecycleStageCode` and `LifecycleStageDescription`, `Certificate`, `EnvironmentalCertificate`, `CircularityProfile`, `EnvironmentalEmission`, `ManufacturerParty`, `InformationContentProviderParty`, `TransactionConditions` |

## The table

| Kind | Document types | The item carries |
|---|---|---|
| catalogue | Catalogue, CatalogueItemSpecificationUpdate | name, desc, id, class, origin, brand, warranty, pack, type, dg, tax: everything about the type and its variants (not a lot) |
| offer | Tender, Quotation | the same as the catalogue, without tax: an offer presents the product |
| order | Order, OrderResponse, OrderChange, OrderCancellation, RequestForQuotation, Forecast, ForecastRevision, InventoryReport, ProductActivity, RetailEvent, TradeItemLocationProfile, ItemInformationRequest, CataloguePricingUpdate, CatalogueDeletion, CatalogueRequest, ExceptionCriteria, ExceptionNotification, InstructionForReturns, WorkReport, DigitalAgreement, TenderContract | name, desc, id (with the variant chosen), pack, tax |
| despatch | DespatchAdvice, ReceiptAdvice, DeliveryNote, PackingList, FulfilmentCancellation | name, desc, id, instance, lot, dg, pack |
| invoice | Invoice, CreditNote, DebitNote, SelfBilledInvoice, SelfBilledCreditNote, Reminder, Statement, UtilityStatement, RemittanceAdvice | name, desc, id, lot (the cotton is priced by its grade), tax |
| receipt | PurchaseReceipt (the shopper's) | name, desc, id, brand, warranty, tax: the shopper's proof |
| customs | Import, export and transit declarations, CertificateOfOrigin, GoodsCertificate | name, desc, class, origin, dg |
| carnet | GoodsItemPassport and the proofs of re-exportation | name, desc, id, class, origin, instance: the carnet lists the pieces by their marks |
| transport | Waybill, BillOfLading, ForwardingInstructions, the transport plans, status messages, Manifest, CommonTransportationReport, WeightStatement, GoodsItemItinerary, TransportServiceDescription and its request | name, desc, class, dg |
| waste | WasteMovement, WasteNotification | name, desc, class, dg |
| notice | the tender notices and messages, qualifications, the guarantee | name, desc, class |
| message | ApplicationResponse, the status messages, BusinessCard, BusinessInformation, DigitalCapability | name, desc, id |

Compared with D11's starting profile:

- **The offer:** the tender and the quotation get the type's facts, because they present the product.
- **Pack size:** orders keep it, because a bundle of 50 slats is how the sawmill sells (D12, D43).
- **The cotton grade:** it is lot data, so it is in the despatch and invoice documents and not in the catalogue.

## What it does

### Size

The elements inside `cac:Item`, counted over all examples:

| Kind | Examples | Before | After |
|---|---|---|---|
| order | 45 | 1,777 | 413 |
| despatch | 19 | 2,117 | 804 |
| invoice | 66 | 2,097 | 924 |
| customs | 18 | 1,736 | 308 |
| receipt | 4 | 344 | 77 |
| carnet | 4 | 137 | 26 |
| transport | 40 | 165 | 150 |
| catalogue | 4 | 668 | 668 |
| offer | 5 | 110 | 110 |
| notice | 33 | 28 | 28 |

In total 9,179 elements become 3,508; the examples shrink by about 22,800 lines.

### Item elements before and after

| Element | Before | After |
|---|---|---|
| `AdditionalItemProperty` | 255 | 23 |
| `Dimension` | 194 | 20 |
| `CommodityClassification` | 171 | 64 |
| `OriginCountry` | 127 | 33 |
| `BrandName` | 79 | 11 |
| `ModelName` | 72 | 7 |
| `WarrantyInformation`, `AdditionalInformation` | 60 each | 8, 5 |
| `CircularityProfile` | 41 | 4 |
| `EnvironmentalEmission`, `Keyword`, `ItemSpecificationDocumentReference` | 39 each | 4 each |
| `ManufacturerParty` | 35 | 5 |
| `Certificate` | 13 | 2 (the slat's forestry certificate in the quotation, the cotton classing certificate in the invoice) |
| `Name`, `Description`, `ItemInstance`, `ClassifiedTaxCategory`, `BuyersItemIdentification` | unchanged | |

### Coverage before and after

Coverage goes from **4982 to 4971** of 5160. The 11 lost pairs belong to two items that appear only in orders, invoices and customs documents and never in a catalogue:

| Lost | Item | Candidate real case to win it back |
|---|---|---|
| `Item/EnvironmentalCertificate` | the recycled granulate (plastics) | the certificate of the recycled content, which D41 settles with the plastics flow (who certifies it): it belongs in the document that certifies or presents it |
| `CircularityProfile` with `CircularityTypeCode`, `RecycledContentPercent`, `RecyclabilityPercent`, `EndOfLifeTreatment` and its four elements (`ImpactCode`, `ProcessingTypeCode`, `TreatmentLocation`, `TreatmentPathwayCode`) | the pallet film (packaging) | a catalogue or product information of the packaging maker, Rivermouth, for its film; or a rule of a country that makes a buyer prove the recycled content of plastic packaging (as the United Kingdom's plastic packaging tax does), which would make the transaction use the fact |
| `Item/LifecycleStageCode`, `LifecycleStageDescription` | the same film | the same catalogue or product information |

## After approval

1. Switch the profile on.
2. Rewrite the sentence of `note/src/03-world.md` that D11 replaces.
3. Record the outcome in the decisions file, and the lost pairs in O145.
