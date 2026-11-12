# LLM review: 09-TransportationStatus.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/09-TransportationStatus.xml`, Git blob `e1a610d76310b4d013c2aaf846292a8900b63b3e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/09#F1 · High · Import declaration reported as accepted before it was lodged
- XPath: `/TransportationStatus/cbc:IssueTime` = `09:10:00`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:StatusReason` = `Customs released the goods at the border.`
- XPath: `/TransportationStatus/cbc:Description` = `Border crossing passed; customs cleared on both sides.`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- Why: the report (2026-03-24 09:10) says that at the border crossing completed at 08:55 the import declaration was accepted and the goods released. The only import declaration of the flow, LD-IM-26-0161, is issued the same day at 09:54, an hour after the crossing and 44 minutes after this report. Merge check: no other import declaration exists in the flow (`flow_index.py`), so a pre-lodged declaration under another ID cannot explain it.
- Condition: no document of the flow reports the import declaration as accepted, or the goods as released on import, before the declaration's issue time.
- Options: (a, preferred) issue the import declaration before the truck reaches the border (e.g. as a pre-lodged declaration on 2026-03-23 or early on 2026-03-24), which fits "the import by the distributor at the border"; (b) report only the export exit and the seal check here and the import release in a later status after 09:54.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1); parties noted it under "Outside this review"

### road/09#F2 · Medium · Consignment ID given as shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0152`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0152`
- XPath: `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`
- Why: `ShippingOrderID` is "A reference number for a shipping order". The value is the consignment's ID; the order the carrier works under is the transport request LD-TR-26-0151. Same as `08-Waybill.xml`. Medium, as in rail: no example states a different shipping-order ID.
- Condition: `ShippingOrderID` holds the transport request's number, or is absent; the same in 08 and 09.
- Options: (a, preferred) LD-TR-26-0151; (b) drop it.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### road/09#F3 · Medium · Language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 occurrences in 213 files (over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad (F3), context (F4), parties (F1, yes)

### road/09#F4 · Medium · Gate number in AdditionalStreetName of the consignee's postal address
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance of the business park, not a street, and a status report has no use for it.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop it from the address; where a delivery needs it, in the delivery location or instruction.
- Needs decision: no
- From: broad (F4), parties (F2)

### road/09#F5 · Medium · Province in Region instead of CountrySubentity
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address of the same document uses (`/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`).
- Condition: the province is in `CountrySubentity`.
- Options: (a, preferred) move it; (b) define Urvanian provinces as economic regions in the world's rules.
- Needs decision: no
- From: broad (F5), context (F3), parties (F3)

### road/09#F6 · Low · Status location named after the carrier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Trasvia Haulage`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`
- Why: `StatusLocation` holds "Locations associated with this Transportation Status report"; `Trasvia Haulage` is the carrier (already sender and responsible party), not a place. The event has its own location. Low, aligned with rail and air for locations named after companies (logistics and parties had Medium): the place the report is about is given in the event, so nothing is lost.
- Condition: `StatusLocation` names or identifies a place the status refers to, or is absent.
- Options: (a, preferred) drop it; (b) the border crossing or the truck's position (Marrowdale, `XBMRW`).
- Needs decision: no
- From: broad (F10, Low), logistics (F3, Medium), context (F7, Low), parties (F4, Medium)

### road/09#F7 · Low · Consignee contact is the customer service desk
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: the consignee's contact plans the delivery slot ("Reply only if the delivery slot must change") and receives the goods; Lumeway gives its customer service in Sales.
- Condition: the consignee's contact is a goods-in or logistics contact.
- Options: (a, preferred) a goods-in contact; (b) drop job title and department.
- Needs decision: no
- From: broad (F6), context (F8, contact part), parties (F5)

### road/09#F8 · Low · Carrier's operating permit in a progress report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the permit plays no part in reporting progress (section 4.8, IND5); in the waybill it has a reason (international haulage).
- Condition: the status report carries no carrier permit.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (F8, master-data part)

### road/09#F9 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID"; 1 January is a public holiday, and the date occurs 271 times across the examples for at least 25 companies (parties' count over `*.xml`), while Lumeway and Valdara have their own dates (IND5).
- Condition: each party's registration date is its own plausible date, or absent.
- Options: (a, preferred) a date from the company's history; (b) leave it out.
- Needs decision: yes (aligned with rail and air)
- From: parties (F6, no)

### road/09#F10 · Low · Status values without a stated meaning
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:IndicationIndicator` = `true`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Percent` = `70`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:ReliabilityPercent` = `90`
- Why: `IndicationIndicator` "Specifies an indicator relevant to a specific status" and `Percent` is "A percentage meaningful in the context of this status"; nothing says what `true` indicates or what 70 % measures (distance, time, pallets), so they carry no information (IND5). `ReliabilityPercent` qualifies the on-time estimate and is plausible (context).
- Condition: each status value states what it measures, or is absent.
- Options: (a, preferred) drop `IndicationIndicator`, give `Percent` a stated meaning (e.g. "70 % of the distance covered") or drop it; keep `ReliabilityPercent`.
- Needs decision: no
- From: broad (F7), context (F5)

### road/09#F11 · Low · Temperature range for goods that need no protection
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Measure` = `14`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MinimumMeasure` = `4`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MaximumMeasure` = `18`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Description` = `No protection needed for steel benches.`
- Why: the condition gives 14 °C within 4–18 °C, as if the goods had to be kept in that range, while its own description says they need no protection; no document of the flow states a temperature requirement. The seal condition next to it has a use.
- Condition: a temperature condition (or range) is reported only if the goods or the contract require one.
- Options: (a, preferred) drop `Condition[2]`; (b) keep only a measured value with a reason in the story (timber slats).
- Needs decision: no
- From: broad (F8), logistics (F4), context (F6)

### road/09#F12 · Low · Signature ID built from the example number
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `TH-SIG-TS-09`
- XPath: `08-Waybill.xml:/Waybill/cac:Signature/cbc:ID` = `TH-SIG-TH-WB-26-0159`
- Why: `09` is the number of this example file; the same signer's waybill signature follows the document number (though with a doubled `TH-` prefix), and the other signers of the flow use their own numbering (`FCC-SIG-26-0309`).
- Condition: the signature ID follows the signer's own numbering, without example numbers.
- Options: (a, preferred) after the document ID, e.g. `TH-SIG-TS-26-0160`; (b) drop the document signature, since the report is automatic.
- Needs decision: no
- From: broad (F9), context (F9)

### road/09#F13 · Low · Waybill referred to by ID only
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `TH-WB-26-0159`
- Why: a generic `DocumentReference` with only an ID does not say what it refers to. Context refuted it because a status report naturally refers to the consignment's transport document and the ID carries the carrier's waybill prefix; the merge does not follow that refutation, aligned with rail (a reference with ID only for a waybill, Low): the prefix is a convention of the issuer, not a statement of the document type.
- Condition: the reference states the kind of document (type code or text).
- Options: (a, preferred) add `DocumentTypeCode` (waybill) or `DocumentType`.
- Needs decision: no
- From: merge (context considered and refuted it)

### road/09#F14 · Low · Italian street names tagged as English
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- Why: the second rendering of the Urvanian names is Italian text with `languageID` `en-XU`. Parties refuted it: English keeps foreign street names unchanged and the region subtag follows the sender. Against that, the tag states English for words that are not, next to an Urvanian (`qau`) rendering, so the Italian form is a third language without a tag of its own. The merge cannot settle which reading the world intends; aligned with rail and the other road merges (Low, decision). Rail counted 217 such renderings in 102 files (over `*.xml`).
- Condition: one rule for Italian-form names in English renderings, recorded in the world's language rules, and the tags follow it.
- Options: (a, preferred) record that English renderings keep the Italian exonym (then no change); (b) an Italian language tag for the Italian form.
- Needs decision: yes
- From: merge (parties considered and refuted it)

## Checked and consistent
- `DocumentReference` TH-WB-26-0159 resolves to `08-Waybill.xml`; consignment LD-CS-26-0152, carrier ID TH-26-04471, shipment CL-SH-26-0154 and 25 pallets agree with the waybill (all parts).
- Updated pickup 2026-03-23 15:05 = the waybill's actual pickup; updated delivery 2026-03-25 09:30 within the waybill's estimated period 09:00–11:00 and before the required 10:00; actual delivery 09:40 in `11-ReceiptAdvice.xml` (broad, logistics, context).
- Border event 07:30–08:55 contains the waybill's seal check at 07:45; seal condition "Intact, as checked by customs" agrees with the waybill (logistics, context).
- Type and status codes PROGRESS, INPROGRESS, INTRANSIT, BORDERCROSS with `CompletionIndicator` true agree; ONTIME against the 10:00 reference (context, logistics).
- The customs signature on the event fits "A signature that can be used to sign for an entry or an exit at a transport location"; the signing party (XB register 20410137) is the customs authority of `10-ImportCustomsDeclaration.xml` (broad, context, parties).
- Party identity, GLN and ISIN check digits (parties).

## Considered and refuted
- `/TransportationStatus/cbc:Note[2]` = `Automatic report from the sender's tracking system.` while the event carries a customs signature — refuted because the tracking system can transmit the signature captured at the border (from broad).
- `/TransportationStatus/cac:UpdatedPickupTransportEvent`: an "updated" pickup that already happened — refuted because reporting the actual pickup updates the planned 14:00 pickup (from logistics).
- `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Text` = `Driver resting in Marrowdale tonight under the driving-time rules.` against "expected … on time" — refuted because a driver resting in Marrowdale can deliver at 09:30 the next morning (from context); the driving-time question is under "Outside this review".
- `/TransportationStatus/cac:DocumentReference/cbc:ID` with ID only — refuted by context; the merge does not follow and made it F13.
- `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XU` — refuted by parties (English keeps foreign street names, the subtag follows the sender); the merge does not follow and made it F14.
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN could be real — refuted, prefix 952, check digit correct (from parties).
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Telephone`: could be real — refuted, +999 reserved (from parties).

## Changed in the merge
- New F14 (Italian tags) from parties' refuted candidate, aligned with rail and merger C.
- broad/F10, logistics/F3, context/F7, parties/F4 → F6: Low (logistics and parties Medium), aligned with rail and air.
- context/F8 split into F7 (contact, with broad/F6 and parties/F5) and F8 (permit).
- parties/F1 → F3: Needs decision no, aligned.
- parties/F6 → F9: Needs decision yes, aligned with rail and air.
- context/F5 and broad/F7 → F10: `ReliabilityPercent` kept as plausible within the finding.
- New F13 from context's refuted candidate, aligned with rail.

## Outside this review
- The trip is 186 km (`14-Invoice.xml`), about three hours' driving; departure 16:20 on 2026-03-23, border at 07:30 on 2026-03-24, and a rest in Marrowdale "under the driving-time rules" before a delivery on 2026-03-25: the overnight stops follow the delivery slot rather than driving time (logistics, context). For the cross-document timeline review.
