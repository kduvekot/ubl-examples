# LLM review: 07-TransportationStatus.xml

## Reviewed version
- Run: `20261112T0851Z-manual` (a manual review, made before the skill existed; layout differs from the skill's)
- Example: `world/examples/rail/07-TransportationStatus.xml`, Git blob `8099ef7d1b83489b28527fb6bac80705248e606a` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 9f79ecd 2026-11-12 Publish workflow: publish only while the commit is still the head of main
- Skill: none · Register: none
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)
- Corrections: occurrence counts corrected in 12fd4c1, and findings corrected after an independent
  verification in c4e112d (before the rule that reviews are never changed)

Reviewed file: [07-TransportationStatus.xml](07-TransportationStatus.xml) · Flow: `rail` (`RAIL-2026-01`) · Review date: 2026-11-12

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
| 1 | Medium | `…/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent` | An "optional takeover" on 14 April 17:00 that no other document knows and that conflicts with the journey |
| 2 | Medium | `…/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent` | The pickup at the shipper (13 April) placed in the rail main-carriage stage, which starts on 14 April |
| 3 | Medium | `/TransportationStatus/cbc:Description`, `/TransportationStatus/cac:TransportEvent`, `…/cac:MainCarriageShipmentStage/cac:TransportEvent` | Status at 13:11 reports only the 05:40 loading, as an untyped event split in two; the 06:52 departure from the reporting terminal is missing |
| 4 | Medium | `/TransportationStatus/cbc:ShippingOrderID` | A consignment identifier used as a shipping order number |
| 5 | Medium | `/TransportationStatus/cac:DocumentReference/cbc:ID` | A consignment identifier used as a document identifier; no such document exists |
| 6 | Medium · Recurring | `…/cac:PostalAddress/cbc:Region`, `…/cbc:StreetName[2]`, `…/cbc:CityName[2]`, `…/cbc:CompanyLegalForm[2]` | Province in `Region`; Italian text tagged as English |
| 7 | Low | `/TransportationStatus/cbc:OtherInstruction` | Asks the carrier about a delivery slot that the terminal does not manage |
| 8 | Low | `/TransportationStatus/cac:Consignment`, `/TransportationStatus/cac:StatusLocation` | No status type, no containers, no stage mode or means, location by name only |
| 9 | Low · Recurring | `…/cac:PartyLegalEntity/cbc:RegistrationDate` | The same placeholder date `1996-01-01` for both companies |

## Findings

### 1. An optional takeover that conflicts with the journey (Medium)

- **XPath:** `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent`
- **Values:** `OccurrenceDate` = `2026-04-14`, `OccurrenceTime` = `17:00:00`, `CompletionIndicator` = `false`
- **UBL definitions:**
  - *Shipment Stage. Optional Takeover_ Transport Event*: "The optional takeover of the goods in this shipment stage."
  - Compare *Shipment Stage. Takeover_ Transport Event*: "The receiver's takeover of the goods in this shipment stage."
- **Why it does not fit:**
  - A takeover is the moment the receiving party takes over the goods. The train `FRC 4417`
    left the hub at 06:52 on 14 April ([05](05-TransportProgressStatus.xml) and the
    [Waybill](08-Waybill.xml)); the [TEP](03-TransportExecutionPlan.xml) plans the arrival at
    10:30 and the delivery at 11:00 on 15 April.
  - A takeover at 17:00 on 14 April, mid-journey, fits none of these. No other document
    in the flow has an event at that time, and nothing says who would take over the
    goods or where.
  - Because the event carries no `Location`, `TransportEventTypeCode` or `Description`,
    the receiver cannot interpret it.
- **Suggestion:** Remove it. If an intermediate event was intended (e.g. the waypoint at
  13:00/13:20 in the Waybill, or arrival at a border), use the matching element, such as
  `EstimatedArrivalTransportEvent` or a typed `TransportEvent` with a `Location`.

### 2. The pickup at the shipper is placed in the rail main-carriage stage (Medium)

- **XPath:** `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent`
- **Values:** `2026-04-13` `15:00:00`
- **UBL definitions:**
  - *Consignment. Main Carriage_ Shipment Stage*: "A shipment stage during main carriage."
  - *Shipment Stage. Actual Pickup_ Transport Event*: "The pickup of goods in this shipment stage."
- **Why it does not fit:**
  - 13 April 15:00 is the pickup of the consignment at the shipper. It is the
    `Consignment/cac:PlannedPickupTransportEvent` of the [TEP](03-TransportExecutionPlan.xml)
    and the equipment `PickupTransportEvent` of the [Waybill](08-Waybill.xml).
  - The main carriage is the rail leg. Per
    [05-TransportProgressStatus](05-TransportProgressStatus.xml) the train only arrived at
    the hub at 05:30 on 14 April, and per the Waybill it was loaded at 05:40, so the
    goods cannot have been picked up *in this stage* the day before.
  - The value describes pre-carriage. Under main carriage it gives the rail leg a
    start a day too early.
- **Suggestion:** Put the pickup in `cac:PreCarriageShipmentStage`, or at consignment level.
  For the main-carriage stage, report the loading (`LoadingTransportEvent` 05:40) and the
  departure (`ActualDepartureTransportEvent` 06:52) instead.

### 3. The loading is reported late, untyped and split in two; the departure is missing (Medium)

- **XPaths:**
  - `/TransportationStatus/cbc:Description` = `Two containers loaded on the container train.`
  - `/TransportationStatus/cac:TransportEvent` (`OccurrenceDate` `2026-04-14`, no time, `Description` as above, `Location/cbc:Name` `Ferrano Intermodal Hub`)
  - `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent` (`2026-04-14` `05:40:00`, `CompletionIndicator` `true`, nothing else)
  - `/TransportationStatus/cac:StatusPeriod` (`2026-04-14` – `2026-04-14`)
- **UBL definitions:**
  - *Transportation Status. Transport Event*: "Any additional events … that are not defined elsewhere in this document."
  - *Shipment Stage. Transport Event*: "A additional significant occurrence … that is not defined elsewhere in this Shipment Stage."
  - *Shipment Stage. Loading_ Transport Event*: "The loading of goods in this shipment stage."
- **Why it does not fit:**
  - The loading has a dedicated element, `LoadingTransportEvent`. Both
    `TransportEvent`s are meant for events *not defined elsewhere*.
  - The stage-level event has no type, description or location, so on its own it says
    nothing. Only the time (05:40, matching the Waybill's `LoadingTransportEvent`)
    links it to the document-level event, which in turn has no time.
  - The report is issued at 13:11 by the hub, the party where the train departed at
    06:52. Yet it does not include that departure, which by then is the most relevant
    status for the carrier.
- **Suggestion:** Report one event per occurrence with the dedicated elements:
  `LoadingTransportEvent` 05:40 and `ActualDepartureTransportEvent` 06:52, both with
  `CompletionIndicator` `true` and `Location`. Keep `cac:TransportEvent` for events that
  have no element of their own, and give each one a `TransportEventTypeCode`.

### 4. `ShippingOrderID` holds the consignment ID (Medium)

- **XPath:** `/TransportationStatus/cbc:ShippingOrderID`
- **Value:** `VI-CS-26-0327`
- **UBL definition:** *Transportation Status. Shipping Order Identifier*: "A reference number for a shipping order."
- **Why it does not fit:** `VI-CS-26-0327` is the consignment identifier assigned in
  [02-TransportExecutionPlanRequest](02-TransportExecutionPlanRequest.xml)
  (`Consignment/cbc:ID`). The same document repeats it correctly in
  `/TransportationStatus/cac:Consignment/cbc:ID`. A shipping order is the order for the
  transport. In this flow that is the transport request `VI-TR-26-0326`, or
  a booking number from the carrier.
- **Suggestion:** Use the order number (`VI-TR-26-0326`) or omit the element. The same
  misuse is in [08-Waybill](08-Waybill.xml) (`/Waybill/cbc:ShippingOrderID`).

### 5. `DocumentReference` points to a consignment, not a document (Medium)

- **XPath:** `/TransportationStatus/cac:DocumentReference/cbc:ID`
- **Value:** `VI-CS-26-0327`
- **UBL definitions:**
  - *Transportation Status. Document Reference*: "A reference to another document associated with this document."
  - *Document Reference. Identifier*: "An identifier for the referenced document."
- **Why it does not fit:** No document in the flow has this ID: it is the consignment
  ID (see finding 4). A receiver that tries to resolve the reference finds nothing. The
  document that does belong with this status is the
  [Waybill](08-Waybill.xml) `FRC-WB-26-0334` for the same train, issued one minute
  earlier. The TEP is already referenced correctly in
  `TransportExecutionPlanDocumentReference`.
- **Suggestion:** Reference `FRC-WB-26-0334` with a `DocumentTypeCode` for a waybill.
  Otherwise, remove the reference.

### 6. Province in `Region`; Italian text tagged as English (Medium, recurring)

- **XPaths:**
  - `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
  - `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
  - `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione` (`en-XU`)
  - `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal` (`en-XU`)
  - `…/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)` (`en-XU`), in both parties
- **UBL definitions:**
  - *Address. Region*: "The recognized geographic or economic region or group of countries in which this address is located."
  - *Address. Country Subentity*: "… such as the name of its county, province, or state".
  - *Street Name*: "may be repeated only to provide the same content in multiple natural languages".
- **Why it does not fit:**
  - A province belongs in `CountrySubentity`, not in `Region`.
  - The repeated street name and legal form are meant to be the same content in another
    language, with `languageID` naming that language. These values are Italian, or
    Italian with an English gloss, yet tagged as English.
- **Suggestion:** Move the province to `CountrySubentity`. Tag the renderings with their
  real language, or provide real English renderings.
- **Recurring:** The `Region` pattern occurs 195 times in 104 examples. Italian-as-English addresses
  occur in all documents with Urvanian parties.

### 7. Instruction about a delivery slot sent to the carrier by the terminal (Low)

- **XPath:** `/TransportationStatus/cbc:OtherInstruction`
- **Value:** `Reply only if the delivery slot must change.`
- **UBL definition:** *Transportation Status. Other_ Instruction. Text*: "An instruction regarding this message."
- **Why it does not fit:** The sender is the terminal at the origin (Ferrano Intermodal
  Hub). The receiver is the rail carrier. The delivery slot (15 April 11:00 at Marrowdale)
  is agreed between the carrier and the consignee. The origin terminal has no slot to
  change, so the instruction does not fit the sender–receiver relationship of this
  message.
- **Suggestion:** Omit it, or replace it with an instruction that fits the terminal
  (e.g. "Reply only if the containers must be unloaded again").

### 8. Missing status type, containers and stage details (Low)

- **XPaths:**
  - `/TransportationStatus` (no `cbc:TransportationStatusTypeCode`)
  - `/TransportationStatus/cac:Consignment` (no `TransportHandlingUnit`/`TransportEquipment`)
  - `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage` (no `TransportModeCode`, no `TransportMeans`)
  - `/TransportationStatus/cac:StatusLocation/cbc:Name`
- **UBL definitions:**
  - *Transportation Status. Transportation Status Type Code*: "A code signifying the type of status provided in a Transportation Status document."
  - *Shipment Stage. Transport Mode Code*: "A code signifying the method of transport used for this shipment stage."
- **Why it does not fit:** The description speaks of "two containers" and "the
  container train". Yet the document identifies neither containers (the Waybill has e.g.
  `FRXU1044175`) nor the train (`FRC 4417`), and does not state the mode (`2`, rail).
  The status location is given only by name, while the flow uses UN/LOCODEs elsewhere.
  None of these values is wrong, but the report cannot be matched to equipment or train
  without the other documents.
- **Suggestion:** Add `TransportationStatusTypeCode`, the stage's `TransportModeCode` `2`
  and `TransportMeans/RailTransport/TrainID`, the two containers as
  `TransportHandlingUnit/TransportEquipment`, and a location identifier.

### 9. Placeholder registration date (Low, recurring)

- **XPaths:**
  - `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate`
  - `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate`
- **Value:** `1996-01-01` for both
- **UBL definition:** *Party Legal Entity. Registration Date*: "The registration date of the CompanyID."
- **Why it does not fit:** Two different companies registered on the same New Year's Day
  reads as a default value rather than a registration date. It is not wrong in itself.
- **Recurring:** `RegistrationDate>1996-01-01` occurs 271 times in 181 examples.

## References checked and consistent

- `cac:TransportExecutionPlanDocumentReference/cbc:ID` = `FRC-TEP-26-0328` resolves to
  [03-TransportExecutionPlan](03-TransportExecutionPlan.xml).
- `cac:Consignment/cbc:ID` = `VI-CS-26-0327` matches the consignment in documents 02, 03,
  06 and 08.
- `DeliveryTransportEvent` 2026-04-15 11:00 (not completed) matches the TEP's
  `PlannedDeliveryTransportEvent`.
- The 05:40 loading time matches the Waybill's `LoadingTransportEvent`.
- `TransportExecutionStatusCode` `INPROGRESS` ("The carriage is under way") is correct for
  14 April.
- `SenderParty` = terminal operator and `ReceiverParty` = carrier match the
  `TerminalOperatorParty` and `CarrierParty` in the body.
