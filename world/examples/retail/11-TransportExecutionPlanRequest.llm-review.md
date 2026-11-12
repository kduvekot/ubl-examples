# LLM review: 11-TransportExecutionPlanRequest.xml

Reviewed file: [11-TransportExecutionPlanRequest.xml](11-TransportExecutionPlanRequest.xml) · Flow: `retail` (`RETAIL-2026-01`) · Review date: 2026-11-12

**Basis.** The semantic model of UBL 2.5 (`UBL-Entities-2.5.gc` from
<https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/>, SHA-256
`c7df070e…fe988d1`), the meaning of codes in `world/codelists`, and the other
XML documents of the flow where this document refers to them. The fictional
world (countries, currencies, languages, identifier schemes) is accepted as
given; only clashes with real standards are flagged.

**Severity.**
**High**: the value contradicts another value in this document or in a referenced document, or a reference is broken.
**Medium**: the element carries a meaning other than its UBL definition.
**Low**: plausibility, consistency or completeness remark.
**Recurring**: the same pattern occurs in many other examples.

## Summary

| # | Severity | Element(s) | Issue |
|---|---|---|---|
| 1 | Medium | `/TransportExecutionPlanRequest/cac:Consignment` | The request does not say what is to be transported |
| 2 | High | `/TransportExecutionPlanRequest/cbc:TransportUserRemarks`, `/TransportExecutionPlanRequest/cac:TransportServiceProviderResponseDeadlinePeriod` | Confirmation requested by a deadline, but the flow never answers; instead the sender itself reports its request as accepted |
| 3 | Low · Recurring | `…/cac:PostalAddress/cbc:AdditionalStreetName`, `…/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` | A loading gate in the element for a street name |
| 4 | Low | `…/cac:ConsigneeParty/cac:Contact` | Contact name, job title and department contradict each other and do not fit the consignee role |
| 5 | Low | `…/cac:ReceiverParty/cac:Contact/cbc:Name`, `…/cac:SenderParty/cac:Contact` | An export desk for a domestic job; customer service as the transport user's contact |
| 6 | Low | `…/cac:FromLocation/cbc:Name`, `…/cac:ToLocation/cbc:Name` | Party names used as location names |
| 7 | Low | `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` | Framework contract that the forwarder's later documents never reference |
| 8 | Medium · Recurring | `…/cac:Language/cbc:LocaleCode` | A language code where a locale is defined |

## Findings

### 1. The consignment is not described (Medium)

- **XPath:** `/TransportExecutionPlanRequest/cac:Consignment`
- **Values:** Only `cbc:ID` = `LD-CS-26-0228`, `cbc:GrossWeightMeasure` = `996` KGM, consignee and consignor.
- **UBL definitions:**
  - *Transport Execution Plan Request*: "A document sent by a transport user to request a transport service from a transport service provider."
  - *Transport Execution Plan Request. Consignment*: "A description of an identifiable collection of goods items to be transported …".
- **Why it does not fit:**
  - The purpose of the document is to let the provider plan a transport. The
    consignment is the description of what is to be carried. Here it has only a
    weight: no summary description, no number of handling units and no
    goods item.
  - From [12-DespatchAdvice](12-DespatchAdvice.xml) the consignment is six pallets
    (`PX`, SSCC-identified) with 24 park benches, and that document links its first handling
    unit back to this request (`TransportHandlingUnit[1]/cac:ShipmentDocumentReference`
    `LD-TR-26-0227`).
    The request itself does not say any of this. A forwarder cannot judge from this
    request whether one truck and a 13.6 m loading length are needed, and the request
    asks for a full truck load (`TransportServiceCode` `FTL`).
  - The rail flow's [request](../rail/02-TransportExecutionPlanRequest.xml) shows the
    expected level ("192 park benches in two 40-foot containers").
- **Suggestion:** Add at least `cbc:SummaryDescription` ("24 park benches on 6 pallets"),
  `cbc:TotalTransportHandlingUnitQuantity` 6 and, if wanted, the handling units or goods
  items.

### 2. A confirmation that never comes (High, cross-document)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.`
  - `/TransportExecutionPlanRequest/cac:TransportServiceProviderResponseDeadlinePeriod/cbc:EndDate` = `2026-04-26`
- **UBL definitions:**
  - *Transport Service Provider Response Deadline_ Period*: "A deadline for a response from the Transport Service Provider to this Transport Execution Plan Request."
  - *Transport User Remarks*: "Remarks from the transport user regarding the transport operations …".
- **Why it does not fit:**
  - The request asks the forwarder (Bayforth Forwarding) to confirm by 26 April. The
    retail flow has no `TransportExecutionPlan` (the UBL response to this request) or
    any other answer from Bayforth.
  - Instead, [10-DocumentStatus](10-DocumentStatus.xml), sent by Lumeway Distribution
    (the sender of this request) to Brightmarket, lists `LD-TR-26-0227` in an
    `AdditionalDocumentResponse` with `ResponseCode` `AP` (accepted). The transport user
    thus reports its own request as accepted, to a third party, without a document from
    the provider. The next document from the forwarder is the
    [Waybill](13-Waybill.xml) of 29 April. And
    [14-TransportationStatusRequest](14-TransportationStatusRequest.xml) refers to a
    Transport Execution Plan `BF-TEP-26-0227`
    (`/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID`) that
    exists nowhere: a broken reference that assumes the answer this request never got.
- **Suggestion:** Either add a `TransportExecutionPlan` from Bayforth that answers this
  request before 26 April, or drop the confirmation request and the deadline. In 10, the
  acceptance should refer to that Transport Execution Plan, not to Lumeway's own request.

### 3. A loading gate in `AdditionalStreetName` (Low, recurring)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
  - `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- **UBL definition:** *Address. Additional_ Street Name*: "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)."
- **Why it does not fit:**
  - "Gate 3" is not a street name. It is the access point for trucks at the
    distribution centre.
  - In the *postal* address it is irrelevant (mail is not delivered to a truck gate).
  - In the pickup location it is useful information, but UBL has a better place for
    it: a location within a location, *Location. Subsidiary_ Location* ("A location
    subsidiary to this location"), or `Location/cbc:Description`.
  - EN 16931 maps "address line 2" (BT-36) to this element, so it is widely used for
    address details that are not street names. That makes this a Low remark, not a breach.
- **Suggestion:** Remove it from `PostalAddress`. In `FromLocation`, use
  `cac:SubsidiaryLocation/cbc:Name` = `Gate 3` (or the Location's `cbc:Description`).
- **Recurring:** `AdditionalStreetName>Gate 3` occurs 79 times in 76 examples.

### 4. The consignee's contact contradicts itself (Low)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
  - `…/cac:Contact/cbc:JobTitle` = `Customer service officer`
  - `…/cac:Contact/cbc:Department` = `Sales`
- **UBL definitions:**
  - *Contact. Name*: "The name of this contact. It is recommended that this be used for a functional name".
  - *Contact. Department*: "The department where this contact works".
- **Why it does not fit:**
  - A buying office is part of purchasing, not of sales. A customer service officer in
    a retailer's sales department serves the retailer's own customers.
  - In this document the party is the *consignee* (*Consignment. Consignee_ Party*:
    "The Party who receives the goods"). For a carrier, the useful contact is the one
    who receives the truck at the store (goods-in, delivery window, unloading), not the
    buyer.
- **Suggestion:** For the consignee in transport documents, use a goods-receiving contact
  (e.g. Name "Goods receiving", JobTitle "Store receiving clerk", Department "Store
  operations"). Keep "Buying office" in Purchasing for ordering documents.

### 5. Contacts that do not fit a domestic transport booking (Low)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
  - `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service` (JobTitle `Customer service officer`, Department `Sales`)
- **Why it does not fit:**
  - The transport runs from Marrowdale to Lumeport, both in Bayvarra. An "export desk"
    is not the forwarder's desk for a domestic truck.
  - The sender is the transport user booking a truck. The relevant contact is its
    despatch or logistics desk, not customer service in sales.
- **Suggestion:** Receiver: e.g. "Road desk" or "Domestic transport". Sender: e.g.
  "Despatch office", Department "Logistics".

### 6. Party names used as location names (Low)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Lumeway Distribution`
  - `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Brightmarket Stores`
- **UBL definitions:**
  - *Location. Name*: "The name of this location."
  - *From_ Location*: "The location of origin of the transport service …".
- **Why it does not fit:** These are the names of the companies, not of the places. Each
  company may have several sites. Brightmarket Stores is a retail chain with an online
  shop, so "Brightmarket Stores" does not identify *which* store. The document's own
  `cbc:Note` calls the places "the distribution centre" and "the store".
- **Suggestion:** Use names of the sites (e.g. "Lumeway distribution centre Marrowdale",
  "Brightmarket store Old town, Lumeport"). Add a location `cbc:ID` (a GLN, as the
  parties have GS1 identifiers) where available.

### 7. A framework contract nobody else refers to (Low, cross-document)

- **XPath:** `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID`
- **Value:** `LD-BF-FW-2026`
- **UBL definition:** *Transport Execution Plan Request. Transport_ Contract*: "A potential contract related to the Transport Execution Plan Request."
- **Why it does not fit:** The ID suggests a 2026 framework agreement between Lumeway (LD)
  and Bayforth (BF). Neither the forwarder's [Waybill](13-Waybill.xml) nor its
  [Invoice](16-Invoice.xml) for this transport references any contract, so the
  transport appears to run outside the agreement the request names. This is not wrong in
  this document by itself, but the flow is not coherent.
- **Suggestion:** Reference `LD-BF-FW-2026` in the Waybill and Invoice as well (e.g.
  `ContractDocumentReference`), or drop it here.

### 8. `LocaleCode` holds a language, not a locale (Medium, recurring)

- **XPaths:**
  - `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode`
  - `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode`
  - `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode`
- **Value:** `en` with `@listID="ISO 639"`
- **UBL definition:** *Language. Locale Code*: "A code signifying the locale in which this language is used."
- **Why it does not fit:** The value repeats `Language/cbc:ID` and names a language, not a
  locale (language plus region, e.g. `en-XB`). ISO 639 is a list of languages.
- **Recurring:** 362 occurrences in 213 examples.

## References checked and consistent

- `LD-TR-26-0227` is referenced by [12-DespatchAdvice](12-DespatchAdvice.xml)
  (`TransportHandlingUnit/cac:ShipmentDocumentReference`). The consignment
  `LD-CS-26-0228` is used in 12, 13, 14, 15 and 16, and the gross weight 996 kg matches
  the Despatch Advice and Waybill.
- `TransportUserParty` and `BillToParty` = Lumeway (sender), and
  `TransportServiceProviderParty` = Bayforth (receiver), are consistent with the header
  parties.
- The service window (start from 2026-04-29, end by 2026-05-02) fits the despatch on
  29 April (documents 12–15).
- GS1 GLNs `9520610900008` and `9522610900002` have valid check digits and use GS1
  prefix 952, which GS1 reserves for examples.
