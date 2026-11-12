# LLM review: 09-TransportationStatus.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/09-TransportationStatus.xml`, Git blob `e1a610d76310b4d013c2aaf846292a8900b63b3e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 60500a8 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/09#F1 · High · Import declaration reported as accepted before it was lodged
- XPath: `/TransportationStatus/cbc:IssueTime` = `09:10:00`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:StatusReason` = `Customs released the goods at the border.`
- XPath: `/TransportationStatus/cbc:Description` = `Border crossing passed; customs cleared on both sides.`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- Why: The status, issued on 2026-03-24 at 09:10 for a border crossing completed at 08:55, says that the import declaration was "accepted by Bayvarra's customs" and that customs "released the goods at the border" ("customs cleared on both sides"). The only import declaration of the flow, Lumeway's LD-IM-26-0161, is issued on 2026-03-24 at 09:54, 45 minutes after this report and an hour after the crossing. The goods cannot have been released on a declaration that did not yet exist.
- Condition: The status reports the import release only after the import declaration's issue time, or the import declaration is issued before the crossing (e.g. as a pre-arrival declaration).
- Options: (a, preferred) issue the import declaration before the truck reaches the border (e.g. 2026-03-24 early morning or the evening before), so that release at 08:55 is possible; (b) let this status report only the export side and the arrival at the Bayvarran post, with release in a later status.
- Needs decision: no

### road/09#F2 · Medium · Consignment ID used as shipping order ID
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0152`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`
- Why: `ShippingOrderID` is "A reference number for a shipping order". The value is the consignment's own ID; the order to the carrier in this flow is the transport execution plan request LD-TR-26-0151.
- Condition: `ShippingOrderID` holds the shipping order or transport request number, or is absent.
- Options: (a, preferred) set it to LD-TR-26-0151; (b) remove it.
- Needs decision: no

### road/09#F3 · Medium · Language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/09#F4 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/09#F5 · Medium · Province in Region instead of CountrySubentity
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/09#F6 · Low · Consignee contact is the customer service desk
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The consignee's contact receives the goods and the delivery slot (the status asks to reply "only if the delivery slot must change"); Lumeway's contact is its `Customer service` desk in `Sales`.
- Condition: The consignee's contact is a goods-in or logistics contact.
- Options: (a, preferred) give Lumeway a goods-in contact; (b) omit JobTitle/Department.
- Needs decision: no

### road/09#F7 · Low · Status values whose meaning the document does not state
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:IndicationIndicator` = `true`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Percent` = `70`
- Why: `IndicationIndicator` "Specifies an indicator relevant to a specific status" and `Percent` is "A percentage meaningful in the context of this status": both need the context to say what they indicate. Nothing in the status says what `true` indicates or what 70 % measures (share of the distance, of the time, of the goods?). Without that, the values are fillers (IND5).
- Condition: Each of these values has a meaning stated in the document (e.g. a description or a code that names it), or is absent.
- Options: (a, preferred) remove both; (b) keep `Percent` as the share of the distance covered and say so in the status text.
- Needs decision: no

### road/09#F8 · Low · Temperature range for goods that need no protection
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Measure` = `14`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MinimumMeasure` = `4`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MaximumMeasure` = `18`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Description` = `No protection needed for steel benches.`
- Why: The condition reports a transport temperature of 14 °C with a range of 4–18 °C, and says in the same breath "No protection needed for steel benches". A temperature range that the goods do not need is not a condition anyone monitors; the range also has no source in the transport request or the waybill.
- Condition: A temperature condition is reported only if the goods have a temperature requirement stated in the transport documents.
- Options: (a, preferred) remove the temperature condition; (b) give the hardwood slats a stated range in the transport request and keep it.
- Needs decision: no

### road/09#F9 · Low · Signature ID made from the example number or flow name
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `TH-SIG-TS-09`
- Why: `Signature/ID` is "An identifier for this signature". The value `TH-SIG-TS-09` is built from the example's place in the collection (the example number or the flow name), not from a numbering the signing party would use; the other signature IDs of the flow follow the party's own document numbering (e.g. `FCC-SIG-26-0309`, `LTAC-SIG-26-0311`, `XB-CUS-SIG-0884`). An identifier that reveals the example structure is out of the world's story.
- Condition: The signature ID follows the signing party's own numbering and contains no example number or flow name.
- Options: (a, preferred) number the signature like the party's other signatures (prefix, year, running number); (b) derive it from the document ID.
- Needs decision: no

### road/09#F10 · Low · Status location named after the carrier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Trasvia Haulage`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`
- Why: `StatusLocation` holds "Locations associated with this Transportation Status report"; the name `Trasvia Haulage` is the carrier, not a location. The event already has its location (the border crossing).
- Condition: The status location names a place (or is absent).
- Options: (a, preferred) remove it, or give the border crossing; (b) name the carrier's tracking centre as a place, if that is meant.
- Needs decision: no

## Checked and consistent
- `DocumentReference` TH-WB-26-0159 resolves to `08-Waybill.xml`; consignment LD-CS-26-0152, carrier ID TH-26-04471, shipment CL-SH-26-0154 and 25 pallets agree with the waybill.
- Border dwell 07:30–08:55 includes the waybill's seal check at 07:45; updated pickup 2026-03-23 15:05 = actual pickup in the waybill; updated delivery 2026-03-25 09:30 before the required 10:00 and close to the actual delivery 09:40 in `11-ReceiptAdvice.xml`.
- The customs signature on the event fits the definition "A signature that can be used to sign for an entry or an exit at a transport location"; the signing party (XB register 20410137) is the same customs authority as in `10-ImportCustomsDeclaration.xml`.
- Driver resting in Marrowdale overnight before a 09:30 delivery is consistent with an 08:55 border crossing and the delivery the next morning.

## Considered and refuted
- `/TransportationStatus/cbc:Note[2]` = `Automatic report from the sender's tracking system.` while the event carries a customs signature — refuted: the tracking system can transmit the customs exit/entry signature captured at the border.
