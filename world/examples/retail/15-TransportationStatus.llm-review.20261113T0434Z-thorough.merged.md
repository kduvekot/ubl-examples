# LLM review: 15-TransportationStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/15-TransportationStatus.xml`, Git blob `5b9a4c32822b9c4f60e917122105de36cde607f1` (committed)
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

### retail/15#F1 · High · The carrier's shipment reference differs in each transport document
- XPath: `/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- Why: `CarrierAssignedID` is "A reference number assigned by a carrier or its agent to identify a specific shipment". Bayforth is the carrier and reports here on consignment `LD-CS-26-0228`, the consignment of its own waybill 13, with the reference `BF-ROAD-26-0231`; its waybill gives `BF-CMR-26-0217`, and the request 14 that this status answers gives `BF-WB-26-0231` (which is the waybill's document ID, `13-Waybill.xml:/Waybill/cbc:ID` = `BF-WB-26-0231`). One shipment, three carrier references. Verified in the merge in the three XML files; no reading makes three different carrier references for one shipment by one carrier consistent.
- Condition: the carrier-assigned ID is the same in the waybill, the status request and the status.
- Options: (a, preferred) the waybill's `BF-CMR-26-0217` in all three, because the waybill is where the carrier assigns it; (b) another single value.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### retail/15#F2 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatus/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself, repeats `Language/cbc:ID` and names no locale (no country or region). ISO 639 is a list of languages, not of locales. The same value occurs 362 times in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `grep -rl` for the files; recounted in the merge; the parties part's 364 also counted `PreferredLanguageLocaleCode` and `TenderLanguageLocaleCode`).
- Condition: no `Language/cbc:LocaleCode` holds a bare language code; where present it identifies a locale and its `listID` names a list of locales.
- Options: (a, preferred) drop `LocaleCode`: nothing in this document depends on a locale; (b) a real locale such as English as used in Bayvarra (`en-XB`) from a list that defines locales (context preferred this). Fixed in the party master data, so it applies everywhere.
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### retail/15#F3 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is an entrance of the distribution centre at Distribution Drive 43, a vehicle access detail and not a street name; a postal address holds nothing that only matters for vehicles. The value occurs 79 times in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`; where a transport document needs the gate it is given in the pickup or delivery location.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (location description, or a GLN of the dock); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition, and the finding is dismissed. Fixed in the party master data.
- Needs decision: no
- From: broad (F3), parties (F2)

### retail/15#F4 · Medium · "On its way" and expected on 29 April at 14:00, but received on 30 April at 10:40
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `15:34:00`
- Why: at 11:49 on 2026-04-29 the carrier reports, as a fact, that the truck is on its way from the distribution centre (on the Marrowdale ring road) and expects it at the store at 14:00 the same day. The trip is billed as 38 km (`16-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`). The receipt advice for the same consignment records the arrival on the next morning at 10:40 ("40 minutes into the slot"), and the despatch advice is only issued at 15:34 on the 29th, after the announced arrival. An estimate may be wrong, which is why this is not High; but a truck already on the road for 38 km that arrives 23 hours later, with no further status and no mention of the delay in the receipt's timing complaint, is a contradiction the flow does not explain. The broad and context parts recorded this under "Outside this review" as a timeline question; the merge keeps it as a finding because the documents describe the same delivery of the same consignment (section 4: contradictions with another example describing the same object are findings). Which day the benches were delivered is a story decision; 16 (freight invoice 10:31 on 30 April) depends on it.
- Condition: the status, the despatch advice and the receipt advice describe one consistent delivery: either the truck is on its way on the day it delivers, or a later status explains the delay.
- Options: (a, preferred) move this status (and the "on its way" event) to the morning of 2026-04-30 with an expected arrival around 10:00, which fits the "slot" in 17; (b) keep 2026-04-29 and move the receipt in 17 to that afternoon.
- Needs decision: yes
- From: logistics (F2); broad and context (Outside this review)

### retail/15#F5 · Low · The position event has no time and no type, and repeats the delivery update
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Marrowdale ring road`
- Why: `TransportEvent` is "Any additional events associated with this Transportation Status report that are not defined elsewhere in this document". The report places the truck on the Marrowdale ring road on 2026-04-29 but not at what time, so the position cannot be related to the expected arrival at 14:00 (the issue time 11:49 is the only clue). The event has no type code, so "on its way" is only in free text, and its description repeats the expected arrival that the `UpdatedDeliveryTransportEvent` already gives.
- Condition: the position event carries the time it was observed (and, where the world's list has one, an event type), and its description does not restate the delivery update.
- Options: (a, preferred) an occurrence time before the issue time (e.g. 11:40), an event type for en-route/position, and a description without the arrival time; (b) keep it if the issue time is meant as the time of the position, and say so.
- Needs decision: no
- From: broad (F4), logistics (F3), context (F4)

### retail/15#F6 · Low · Contacts that do not fit the parties' roles in this transport
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatus/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the transport is domestic, from Lumeway's distribution centre in Marrowdale (Upland State) to Brightmarket in Lumeport (Coastal State), both in Bayvarra (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CityName` = `Marrowdale`, `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CityName` = `Lumeport`), yet Bayforth's status comes from its "Export desk". Lumeway, which asked about the delivery as transport user, is represented by its sales customer service, while the flow has a dispatch office for it (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`). Both parties are copied with one master contact into every role.
- Condition: the contacts fit the parties' roles in this transport.
- Options: (a, preferred) a road or domestic operations contact for Bayforth in this flow (keeping the export desk for export flows) and Lumeway's dispatch office; (b) leave the contacts out where the document does not need them.
- Needs decision: no
- From: broad (F5), parties (F4, F7)

### retail/15#F7 · Low · Party master data the status report does nothing with
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Lumeway carries its customs trader identifier, although every movement of the flow is inside Bayvarra and no example of the flow is a customs document, and its share capital, which a transport status does not use (section 4.8: data copied from master data). `CorporateStockAmount` is moreover defined as "The number of shares in the capital stock of a corporation" while its data type is an amount and the value is a sum in XBL: a conflict between UBL's definition and data type that belongs in the write-up for the UBL TC; it does not change the fix here. The parties part made the share capital a finding of its own with "Needs decision: yes"; the merge folds it in with "no", as retail mergers a and b and the furniture, road and rail merges do: dropping unused data changes no story.
- Condition: Lumeway's party in this document carries no customs identifier and no share capital.
- Options: (a, preferred) leave them out here and keep them for documents that use them (customs documents; the issuer's own invoices); (b) record the `CorporateStockAmount` definition conflict for the TC write-up in any case.
- Needs decision: no
- From: parties (F5, F6)

### retail/15#F8 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TransportationStatus/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the date `1996-01-01` is shared by 25 different parties of the world (counted by the parties part over `world/examples/*/*.xml` with lxml), among them Bayforth Forwarding, Harbourline Factoring and Castrano Logistics, while other parties have dates of their own (Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January for unrelated companies is a filler (rule "no fillers"). Every earlier flow's merge kept this as Low with a decision.
- Condition: the registration date of each party is a date with a reason in the world's history, or absent.
- Options: (a, preferred) Bayforth's own registration date from its history; (b) leave the date out; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F3)

## Checked and consistent
- The status answers 14-TransportationStatusRequest (`LD-DOC-26-0232`), issued at 10:59, 50 minutes earlier, with the expected delivery time it asked for, within its requested period (2026-04-29 to 2026-04-30); sender and receiver are the request's receiver and sender (broad, logistics, context, parties; verified).
- Consignment `LD-CS-26-0228` is the consignment of 11 to 14 and 16 (verified).
- The updated delivery event (14:00) lies after the issue time 11:49, as an expected time must (context).
- The Marrowdale ring road fits a truck that has just left the distribution centre in Marrowdale (11's FromLocation).
- Party descriptions are identical in every example of the flow; register identifiers agree with `PartyLegalEntity/CompanyID` and the endpoint IDs; the GLN `9520610900008` passes `check_ids.py` (rerun in the merge); the GS1 prefix 952 is reserved for demonstrations (parties).
- Each party is registered for the state sales tax of the state its address is in (parties).

## Considered and refuted
- `/TransportationStatus/cbc:TransportationStatusTypeCode` = `CURRENT`: suspected to contradict the request's type `DELIVERY` — refuted because the report gives the current status and an updated delivery event, which answers a request about the delivery (from broad; the merge also refutes context/F3 on this point, see below).
- `/TransportationStatus/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse of BlockName for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits a business park, and `PlotIdentification` "Plot 14" is the land parcel (from parties).

## Refuted in the merge
### context/F3 · Low · Status type "current" in answer to a request for delivery status
- XPath: `/TransportationStatus/cbc:TransportationStatusTypeCode` = `CURRENT`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:TransportationStatusTypeCode` = `DELIVERY`
- The part's finding: the request asks for the "Status of delivery" ("Answer with the expected delivery time"); the report's main content is the updated delivery event, but its type code says "Current status". Condition: the type code matches the status the report gives, i.e. the one requested. Options: `DELIVERY` (preferred), or keep `CURRENT` if the position report is the main content. Needs decision: no.
- Refuted because: the world's list defines `DELIVERY` as "Whether and when the goods were delivered." and `CURRENT` as "Where the goods are now." (`world/codelists/gc/TransportationStatusTypeCode.gc`). The goods are not delivered yet; the report says where the truck is and when it is expected, which is what `CURRENT` means. `DELIVERY` would claim a delivery status that does not exist. That the request asked for `DELIVERY` before delivery is a question of 14, not of this answer (see Outside this review). The broad part refuted the same suspicion.

## Changed in the merge
- logistics/F2 → F4: kept as Medium with "Needs decision: yes"; the broad and context parts' placement under "Outside this review" recorded in Why and From, because the contradiction is between documents describing the same delivery.
- broad/F4, logistics/F3, context/F4 → F5: grouped (same event); context's type-code and repetition points added to the condition.
- broad/F5, parties/F4, parties/F7 → F6: grouped into one contacts finding per example (as retail a/b and earlier flows).
- parties/F5, parties/F6 → F7: grouped into one copied-master-data finding; F6's "Needs decision: yes" set to no, the definition conflict kept in Why as a note for the TC write-up (aligned with retail a/b, furniture, road, rail).
- context/F2 option order: drop preferred instead of `en-XB`, aligned with all parts but context and with every earlier flow.

## Outside this review
- `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:TransportationStatusTypeCode` = `DELIVERY` asks for a delivery status before the delivery; that is a question for 14's review.
- Whether 38 km is the road distance from Marrowdale to the Lumeport store on the map (map/route checks).
