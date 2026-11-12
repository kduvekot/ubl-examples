# LLM review: 09-TransportationStatus.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/09-TransportationStatus.xml`, Git blob `e1a610d76310b4d013c2aaf846292a8900b63b3e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/09#F1 · High · Import declaration reported as accepted before it was lodged
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:StatusReason` = `Customs released the goods at the border.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `09:10:00`
- Why: the status report, issued on 2026-03-24 at 09:10 for a border crossing completed at 08:55, says the import declaration was accepted and the goods released. The import declaration of this consignment is issued later the same morning (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`, issue date 2026-03-24), so it cannot have been accepted at 08:55 or reported as accepted at 09:10.
- Condition: no document of the flow reports the import declaration as accepted, or the goods as released on import, before the declaration is issued.
- Options: (a) issue the import declaration before the border crossing (e.g. as a pre-lodged declaration on 2026-03-23 or early on 2026-03-24) (preferred: release at the border needs a declaration lodged beforehand); (b) report only the export exit and the seal check here and the import release in a later status.
- Needs decision: no

### road/09#F2 · Medium · Consignment ID given as shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0152`
- Why: `ShippingOrderID` is "A reference number for a shipping order". The value is the consignment's ID (`/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0152`); the shipping order of this transport is the transport request `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0151`.
- Condition: `ShippingOrderID` holds the number of the shipping order (the transport request), or is absent.
- Options: (a) `LD-TR-26-0151` (preferred); (b) drop it.
- Needs decision: no

### road/09#F3 · Medium · Province given as Region
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/09#F4 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/09#F5 · Low · Status values without a stated meaning
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Percent` = `70`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:IndicationIndicator` = `true`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:ReliabilityPercent` = `90`
- Why: `Percent` is "A percentage meaningful in the context of this status" and `IndicationIndicator` "Specifies an indicator relevant to a specific status"; neither the status nor its text says what the 70 % are (distance, time, pallets?) or what the indicator indicates being true, so they carry no information (IND5). `ReliabilityPercent` 90 % for an on-time arrival estimate is plausible but is not tied to anything either.
- Condition: every status value says, in the status or its text, what it measures; values without such a meaning are absent.
- Options: (a) drop `IndicationIndicator` and `Percent`, or give `Percent` a stated meaning (e.g. "70 % of the distance covered" in the status text) (preferred); (b) keep `ReliabilityPercent` with the arrival estimate it qualifies.
- Needs decision: no

### road/09#F6 · Low · Temperature condition reported for goods that need none
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Measure` = `14`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MinimumMeasure` = `4`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MaximumMeasure` = `18`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Description` = `No protection needed for steel benches.`
- Why: the condition's own text says the steel benches need no temperature protection, and nothing in the flow (order, waybill, handling codes) asks for a temperature; a measured transport temperature with a range is then data the report does nothing with (section 4.8). The seal condition next to it does have a use (the customs seal check).
- Condition: the status report carries a temperature condition only if the goods or the contract require one.
- Options: (a) drop the temperature condition (preferred); (b) keep it only with a reason in the story (e.g. timber slats that must not get wet or freeze).
- Needs decision: no

### road/09#F7 · Low · Status location named after the carrier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Trasvia Haulage`
- Why: `StatusLocation` holds "Locations associated with this Transportation Status report"; the name is the carrier's company name, which is not a place. The place of the event is already given (`/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`).
- Condition: the status location is a place (e.g. the border crossing or the truck's position), or is absent.
- Options: (a) drop it (preferred: the event has its location); (b) name the place.
- Needs decision: no

### road/09#F8 · Low · Contact and master data that do not fit a status report
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the status goes to the consignee's goods-in, which plans the delivery slot ("Reply only if the delivery slot must change"), not to Lumeway's customer service in Sales; and the carrier's operating permit plays no part in a progress report (section 4.8, IND5).
- Condition: the consignee's contact is the receiving function; the report carries no carrier permit.
- Options: (a) goods-in as contact and drop the permit (preferred); (b) drop the contact's job title and department.
- Needs decision: no

### road/09#F9 · Low · Signature ID built from the example number
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `TH-SIG-TS-09`
- Why: `09` is the number of this example file in the repository; the report is said to be an "Automatic report from the sender's tracking system", so a signature ID would follow Trasvia's numbering (as its waybill signature does, `08-Waybill.xml:/Waybill/cac:Signature/cbc:ID` = `TH-SIG-TH-WB-26-0159`).
- Condition: the signature ID follows the signer's own numbering, without repository file numbers.
- Options: (a) `TH-SIG-TH-TS-26-0160` after the document ID (preferred: same pattern as the waybill); (b) drop the document signature, since the report is automatic.
- Needs decision: no

## Checked and consistent
- Consignment `LD-CS-26-0152`, carrier ID `TH-26-04471` and shipment `CL-SH-26-0154` match `08-Waybill.xml`; the waybill reference `TH-WB-26-0159` resolves to `08-Waybill.xml`.
- Updated pickup 2026-03-23 15:05 equals the waybill's actual pickup; updated delivery 2026-03-25 09:30 lies within the waybill's estimated delivery period (09:00–11:00) and before the required time 10:00 that the current status refers to.
- `TransportationStatusTypeCode` `PROGRESS`, `TransportExecutionStatusCode` `INPROGRESS`, consignment status `INTRANSIT` ("All 25 pallets on board") and the event `BORDERCROSS` with `CompletionIndicator` true agree.
- The event's signature by Bayvarra's customs, validated 2026-03-24, fits "A signature that can be used to sign for an entry or an exit at a transport location"; the event period 07:30–08:55 ends at the event time; the waybill's seal check at 07:45 lies within it.
- Seal condition "Intact, as checked by customs" agrees with the waybill's seal remark and examination.

## Considered and refuted
- `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Text` = `Driver resting in Marrowdale tonight under the driving-time rules.`: suspected to contradict "In transit in Bayvarra, expected at the distribution centre on time" — refuted because a driver who reaches Marrowdale in the evening and rests there can deliver on the next morning (09:30) as stated.
- `/TransportationStatus/cac:DocumentReference/cbc:ID` = `TH-WB-26-0159` with ID only: suspected unclear reference — refuted because a status report naturally refers to the transport document of the consignment it reports on, and the ID is the carrier's own waybill number.

## Outside this review
- Whether the truck can take from the border crossing at 08:55 on 2026-03-24 until the evening to reach Marrowdale and then deliver on 2026-03-25 at 09:30 is a timeline question across the flow (map and driving times).
