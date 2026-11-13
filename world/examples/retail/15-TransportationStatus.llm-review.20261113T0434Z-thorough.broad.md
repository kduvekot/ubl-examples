# LLM review: 15-TransportationStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/15-TransportationStatus.xml`, Git blob `5b9a4c32822b9c4f60e917122105de36cde607f1` (committed)
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

### retail/15#F1 · High · The carrier's shipment reference differs in each transport document
- XPath: `/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- Why: `CarrierAssignedID` is "A reference number assigned by a carrier or its agent to identify a specific shipment". Bayforth is the carrier and reports here on consignment `LD-CS-26-0228` with reference `BF-ROAD-26-0231`; its own waybill for the same consignment gives `BF-CMR-26-0217`, and the request it answers gives `BF-WB-26-0231`. One shipment, three carrier references.
- Condition: the carrier-assigned ID is the same in the waybill, the status request and the status.
- Options: (a, preferred) the waybill's carrier reference in all three.
- Needs decision: no

### retail/15#F2 · Medium · Language codes in LocaleCode
- XPath: `/TransportationStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/15#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/15#F4 · Low · Current position without a time
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Marrowdale ring road`
- Why: a current status report places the truck on the Marrowdale ring road on 2026-04-29, but not at what time; without it the position cannot be related to the expected arrival at 14:00. The event also has no type code, so "on its way" is only in the free text; the expected arrival is repeated in the description and in the updated delivery event.
- Condition: the position event carries the time it was observed (and, where the world's list has one, an event type).
- Options: (a, preferred) an occurrence time before the issue time (11:49), and a description without the repeated arrival time; (b) keep it as is if the issue time is meant as the time of the position, and say so.
- Needs decision: no

### retail/15#F5 · Low · Contacts that do not fit the transport roles
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:Department` = `Operations`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Bayforth's status report on a domestic haul comes from its "Export desk", and Lumeway, which asked about the delivery, is represented by its customer service in sales. The flow has a dispatch office for Lumeway (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`).
- Condition: the contacts fit the parties' roles in this transport.
- Options: (a, preferred) Bayforth's road or domestic operations and Lumeway's dispatch office.
- Needs decision: no

## Checked and consistent
- The status answers 14-TransportationStatusRequest (`LD-DOC-26-0232`), issued 50 minutes earlier, with the expected delivery time it asked for (2026-04-29 14:00), within the requested status period.
- Consignment `LD-CS-26-0228` is the consignment of 11 to 14; sender is the carrier, receiver the transport user.
- The position "Marrowdale ring road" lies on the way from the distribution centre in Marrowdale.

## Considered and refuted
- `/TransportationStatus/cbc:TransportationStatusTypeCode` = `CURRENT`: suspected to contradict the request's type `DELIVERY` — refuted: the report gives the current status and an updated delivery event, which answers a request about the delivery.

## Outside this review
- Timeline: the expected arrival on 2026-04-29 at 14:00 is not met; 17-ReceiptAdvice records receipt on 2026-04-30, and 12-DespatchAdvice is only issued at 15:34 on 2026-04-29.
