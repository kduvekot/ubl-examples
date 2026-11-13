# LLM review: 14-TransportationStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/14-TransportationStatusRequest.xml`, Git blob `e728f33a6fcfaa9b61feef53866fa38361baf8dd` (committed)
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

### retail/14#F1 · High · Reference to a transport execution plan that does not exist
- XPath: `/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `BF-TEP-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.`
- Why: `TransportExecutionPlanDocumentReference` is "A reference to the Transport Execution Plan associated with the transport service for which status is requested". No XML file has the ID `BF-TEP-26-0227` (`grep -rl --include='*.xml' 'BF-TEP' world/examples`: this file only, rechecked in the merge). The flow has Lumeway's request 11, which asks to be confirmed, but no Transport Execution Plan from Bayforth answering it; 10-DocumentStatus also reports the request as accepted without any such document.
- Condition: the reference resolves to a Transport Execution Plan in the flow, or is absent (and, if wanted, the request 11 is referenced through a typed document reference).
- Options: (a) add Bayforth's Transport Execution Plan `BF-TEP-26-0227` to the flow, between 11 and 13 (it would also give 10's "booked" a basis); (b, preferred if the flow is to stay as it is) drop the reference and rely on the consignment ID, or reference `LD-TR-26-0227` as a document reference of type "Transport execution plan request".
- Needs decision: yes (adding a document to the flow)
- From: broad, context, logistics

### retail/14#F2 · High · Carrier-assigned ID holds the waybill's document number, which differs from the carrier's own reference
- XPath: `/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: `CarrierAssignedID` is "A reference number assigned by a carrier or its agent to identify a specific shipment, such as a booking reference number". The value is the ID of the waybill document 13, not a shipment reference; the waybill gives Bayforth's shipment reference as `BF-CMR-26-0217`, and Bayforth's answer 15 uses a third value. One shipment, three carrier references, and a document ID used as a shipment reference.
- Condition: the carrier-assigned ID is the carrier's shipment reference, the same as in 13 and 15; a reference to the waybill, if wanted, is a document reference.
- Options: (a, preferred) `BF-CMR-26-0217`, as in 13 (and in 15); (b) in addition a document reference to `BF-WB-26-0231`.
- Needs decision: no
- From: broad, context, logistics (aligned with retail merge c for 15)

### retail/14#F3 · Medium · The consignment ID given as shipping order ID
- XPath: `/TransportationStatusRequest/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/TransportationStatusRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: `ShippingOrderID` is "A reference number for a shipping order". `LD-CS-26-0228` is the consignment's ID (also this document's `Consignment/ID`, and that of 11, 12 and 13); the shipping order or forwarding instruction is the transport request 11, `LD-TR-26-0227`. Medium, not High: no example states a different shipping-order ID (as rail b, road b). Same as 13.
- Condition: `ShippingOrderID`, if present, identifies the shipping order, not the consignment.
- Options: (a, preferred) `LD-TR-26-0227`; (b) drop it.
- Needs decision: no
- From: broad, context, logistics

### retail/14#F4 · Medium · Language codes in LocaleCode
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is a language code and names no locale. 362 such elements in 213 XML files (recounted in the merge).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop it (party master data); (b) a locale such as English as used in Bayvarra from a locale list.
- Needs decision: no
- From: broad, context, parties

### retail/14#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; "Gate 3" is a vehicle entrance of the distribution centre, not a street name. 79 occurrences in 76 XML files (recounted).
- Condition: no `AdditionalStreetName` of Lumeway holds the gate.
- Options: (a, preferred) drop it from the postal address (party master data); (b) if Bayvarra's address format makes the gate part of the postal address, record that and dismiss the finding.
- Needs decision: no
- From: broad, parties

### retail/14#F6 · Low · The buyer's order number in a request to the carrier
- XPath: `/TransportationStatusRequest/cac:DocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: the order is between Brightmarket and Lumeway; Bayforth has never received it, and it appears in none of the carrier's documents (11, 13). The reference has no type or description that would tell the carrier what it is, and the consignment ID already identifies the transport.
- Condition: references in the request are to documents the carrier knows, or are typed and have a reason.
- Options: (a, preferred) drop it; (b) a document type ("customer's order") if Lumeway wants the carrier to quote it.
- Needs decision: no
- From: broad, context

### retail/14#F7 · Low · Requested status location named, not identified
- XPath: `/TransportationStatusRequest/cac:RequestedStatusLocation/cbc:Name` = `Brightmarket Stores, goods-in`
- XPath: `08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: `RequestedStatusLocation` is "A location for which status is requested". It is the store's goods-in, which the order identifies by GLN `9522610900019`; here it is given by a name only, which does not say which store and cannot be matched to the forwarder's delivery stop.
- Condition: the requested status location carries the goods-in GLN (or address) the flow uses.
- Options: (a, preferred) add `ID` `9522610900019`.
- Needs decision: no
- From: context, logistics, parties

### retail/14#F8 · Low · Contacts that do not fit the parties' roles in this transport
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- Why: Lumeway's question about a delivery comes from its sales customer service, and Bayforth is represented by its "Export desk" for a domestic haul within Bayvarra. The flow has a dispatch office for Lumeway (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`).
- Condition: the contacts fit the parties' roles in this transport.
- Options: (a, preferred) Lumeway's dispatch office and a Bayforth domestic or road desk.
- Needs decision: no
- From: broad, parties

### retail/14#F9 · Low · Party master data the status request does nothing with
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: a status question uses neither a customs trader number (no customs in this flow), nor share capital, nor tax registrations (IND5/IND6). `CorporateStockAmount`'s definition ("The number of shares in the capital stock of a corporation") against its amount type is a candidate for the TC write-up (parties part).
- Condition: the parties carry only what the request uses.
- Options: (a, preferred) drop them here; record the `CorporateStockAmount` definition conflict for the TC write-up.
- Needs decision: no
- From: context (with the signature, split in the merge), parties

### retail/14#F10 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is shared by 25 different companies in three countries (parties part; 271 occurrences in 181 files, earlier merges' count), among them Bayforth. It looks like a filler.
- Condition: Bayforth's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) a date from Bayforth's history; (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties

### retail/14#F11 · Low · Signature with an ID and a signatory only
- XPath: `/TransportationStatusRequest/cac:Signature/cbc:ID` = `LD-SIG-26-TSR`
- Why: no method, attachment or date: the aggregate records no signature, and a status question needs none. World-wide convention (137 of 147 `Signature` aggregates, lxml count of the air merge).
- Condition: a signature carries what makes it one, or is absent.
- Options: (a, preferred) drop it.
- Needs decision: yes
- From: context (Needs decision no there; set to yes, aligned with retail merges a and c, air and utilities)

## Checked and consistent
- Times, redone in the merge: issued 2026-04-29 10:59, after the waybill 13 (08:56) and before the answer 15 (11:49), which refers to this request (`15-TransportationStatus.xml:/TransportationStatus/cac:TransportationStatusRequestDocumentReference/cbc:ID` = `LD-DOC-26-0232`); the requested period 2026-04-29 to 2026-04-30 covers both the delivery expected in 15 (2026-04-29 14:00) and the receipt in 17 (2026-04-30).
- `TransportationStatusTypeCode` `DELIVERY`, the description "When will the benches arrive?" and the instruction "Answer with the expected delivery time." agree with each other and with 15's answer.
- Consignment `LD-CS-26-0228` is that of 11, 12 and 13; sender and receiver are the transport user and provider of 11, described identically in every retail example (parties part).
- "The promotion starts soon": the promotion starts 2026-05-11 (06-RetailEvent), twelve days later.

## Considered and refuted
- `/TransportationStatusRequest/cac:RequestedStatusLocation/cbc:Name` = `Brightmarket Stores, goods-in`: suspected a company name as location — refuted because it names the place, the store's goods-in (from broad; the missing identifier is F7).
- `/TransportationStatusRequest/cbc:Note` = `The promotion starts soon.`: checked against the promotion start twelve days later — consistent enough for "soon" (from broad).
- `/TransportationStatusRequest/cac:RequestedStatusPeriod/cbc:EndDate` = `2026-04-30`: a period ending the day after the request — refuted because the truck may arrive the next day; the period covers the expected delivery window (from context).
- `/TransportationStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted because the definition fits a business park (from parties).

## Changed in the merge
- broad/F1, context/F2, logistics/F1 → F1; broad/F2, context/F1, logistics/F2 → F2; broad/F3, context/F3, logistics/F3 → F3; broad/F4, context/F4, parties/F1 → F4; broad/F5, parties/F2 → F5; broad/F6, context/F5 → F6; context/F6, logistics/F4, parties/F8 → F7; broad/F7, parties/F5, F7 → F8: combined.
- context/F7 → split into F9 (master data) and F11 (signature); parties/F3, F4 folded into F9; parties/F4 (CorporateStockAmount) Needs decision yes → no with its TC note; tax-scheme XPaths added. F11: Needs decision no → yes.
