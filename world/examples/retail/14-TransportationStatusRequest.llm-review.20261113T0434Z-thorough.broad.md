# LLM review: 14-TransportationStatusRequest.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/14-TransportationStatusRequest.xml`, Git blob `e728f33a6fcfaa9b61feef53866fa38361baf8dd` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/14#F1 · High · Reference to a transport execution plan that does not exist in the flow
- XPath: `/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `BF-TEP-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- Why: `TransportExecutionPlanDocumentReference` is "A reference to the Transport Execution Plan associated with the transport service for which status is requested". The flow contains Lumeway's request for a plan (11, `LD-TR-26-0227`), but no Transport Execution Plan; no example carries `BF-TEP-26-0227` (searched over `world/examples/*/*.xml`). Either Bayforth's plan is missing from the flow, or the reference should point to what exists.
- Condition: the reference resolves to a Transport Execution Plan in the flow, or refers to the document that does exist with an element that fits it.
- Options: (a) add Bayforth's Transport Execution Plan `BF-TEP-26-0227` to the flow (it also explains the acceptance reported in 10-DocumentStatus); (b, preferred if the flow is to stay as it is) drop the reference and keep the consignment ID, which identifies the transport.
- Needs decision: yes

### retail/14#F2 · High · The carrier's shipment reference differs in each transport document
- XPath: `/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- Why: `CarrierAssignedID` is "A reference number assigned by a carrier or its agent to identify a specific shipment". Here it is the waybill's document number; the waybill itself gives `BF-CMR-26-0217` as the carrier's reference, and Bayforth's status report `BF-ROAD-26-0231`. One shipment, three carrier references.
- Condition: the carrier-assigned ID is the same in the waybill, the status request and the status.
- Options: (a, preferred) the waybill's carrier reference in all three; (b) if the waybill number is meant, reference the waybill with a document reference instead.
- Needs decision: no

### retail/14#F3 · Medium · Consignment ID used as shipping order ID
- XPath: `/TransportationStatusRequest/cbc:ShippingOrderID` = `LD-CS-26-0228`
- XPath: `/TransportationStatusRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0228`
- Why: `ShippingOrderID` is "A reference number for a shipping order". `LD-CS-26-0228` is the consignment's ID, which the document also gives in `Consignment/ID`; the shipping order (forwarding instruction) of the flow is 11-TransportExecutionPlanRequest, `LD-TR-26-0227`.
- Condition: the shipping order ID is the ID of the shipping order, or absent.
- Options: (a, preferred) `LD-TR-26-0227`; (b) drop it.
- Needs decision: no

### retail/14#F4 · Medium · Language codes in LocaleCode
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/14#F5 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/14#F6 · Low · Reference to the buyer's order in a request to the carrier
- XPath: `/TransportationStatusRequest/cac:DocumentReference/cbc:ID` = `BS-PO-26-0224`
- Why: the order is between Brightmarket and Lumeway; Bayforth has never received it, and the reference carries no type or description that would tell the carrier what it is. The consignment ID already identifies the transport for the carrier.
- Condition: references in the request are to documents the carrier knows, or say what they are.
- Options: (a, preferred) drop it; (b) add a document type ("customer's order") if Lumeway wants the carrier to quote it.
- Needs decision: no

### retail/14#F7 · Low · Contacts that do not fit the transport roles
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatusRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatusRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Operations`
- Why: Lumeway's question about a delivery is represented by its customer service in sales, and Bayforth by its "Export desk" for a domestic haul within Bayvarra. The flow has a dispatch office for Lumeway (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`).
- Condition: the contacts fit the parties' roles in this transport.
- Options: (a, preferred) Lumeway's dispatch office and Bayforth's road or domestic operations.
- Needs decision: no

## Checked and consistent
- Consignment `LD-CS-26-0228` is the consignment of 11, 12 and 13; sender and receiver are the transport user and the carrier.
- Requested status period 2026-04-29 to 2026-04-30 covers the delivery (expected 2026-04-29 in 15, received 2026-04-30 in 17); the request (10:59) precedes the answer 15-TransportationStatus (11:49), which refers to it.
- The status type "delivery" and the instruction to answer with the expected delivery time match the description "When will the benches arrive?" and the answer in 15.

## Considered and refuted
- `/TransportationStatusRequest/cac:RequestedStatusLocation/cbc:Name` = `Brightmarket Stores, goods-in`: suspected a company name as location — refuted: it names the place (the store's goods-in).
- `/TransportationStatusRequest/cbc:Note` = `The promotion starts soon.`: checked against the promotion start (2026-05-11 in 06-RetailEvent), twelve days later — consistent enough for "soon".
