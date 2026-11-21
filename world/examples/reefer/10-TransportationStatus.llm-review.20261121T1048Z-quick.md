# LLM review: 10-TransportationStatus.xml

Flow: reefer (BYF-TX-26-2160) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/10-TransportationStatus.xml`, Git blob `c306e95134de9741da174af306622b9e5af5a836` (committed)
- Last commit changing the example: 99d799b3 2026-11-20 O97 and O78: the call states the withholding, tenders carry the tax subtotal, every time carries its place's UTC offset
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### reefer/10#F1 · Medium · The discharge is reported twice, the second time as an "additional" event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:TransportEventTypeCode` = `DISCHARGE`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Reefer TWLU5316047 discharged and on the port's power; released by customs.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:OccurrenceTime` = `08:10:00+00:00`
- Why: TransportationStatus/TransportEvent is defined as "any additional events associated with this Transportation Status report that are not defined elsewhere in this document". The discharge is defined elsewhere: the main-carriage stage carries it as DischargeTransportEvent with time and completion, and the storage on the port's power is the equipment's own event at 08:25. The document-level event repeats the discharge without a time and adds, only in text, the one fact not stated elsewhere: the release by customs, which has no event, time or code of its own.
- Condition: each event is reported once, in its dedicated element; a document-level TransportEvent, if present, reports an event not covered elsewhere (such as the customs release) with its own type and time.
- Options: (a) turn the document-level event into the customs-release event (its own type code, time and location) and drop the repeated discharge text (preferred: the release is what the consignee needs before collecting); (b) remove the document-level event and state the release in a note.
- Needs decision: no

### reefer/10#F2 · Low · The voyage's temperature log hangs on the storage event at the port
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:TransportEventTypeCode` = `STORAGE`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cac:CurrentStatus/cbc:Description` = `The reefer's own log, read by the carrier's monitoring at sea, over the voyage from loading at Lumeport to discharge.`
- Why: CurrentStatus is "the current status of this transport event". The event is the placing of the reefer on rack power point 7 at 08:25 on 26 April; its status is a summary of the whole voyage before it, and the condition code `COMPLETED` refers to the storage event, not to the log. The voyage summary belongs to the main carriage (e.g. the discharge event's status, which closes the voyage) rather than to the storage that follows it.
- Condition: the temperature summary of the voyage is attached to an event of the voyage (or to the equipment generally), and the storage event's status describes the storage.
- Options: (a) move the status with its condition to the main-carriage DischargeTransportEvent (preferred); (b) keep it under the equipment in an event whose type is a monitoring report for the voyage.
- Needs decision: no

## Checked and consistent
- Times: arrival 06:40 UTC, discharge 08:10 UTC, storage 08:25 UTC, all before the issue at 07:45 −01:00 (08:45 UTC); departure was 23 April 19:00 UTC (`05-ExportCustomsDeclaration.xml`), 2½ days for the crossing.
- Temperature: supply air 0.2–0.9 °C, mean 0.5 °C = set point, inside the 0–1 °C range of `07-BillOfLading.xml`; the same range is quoted in `11-ReceiptAdvice.xml`.
- Container `TWLU5316047` and consignment `HRW-CS-26-0730` are those of the bill of lading; sender is the carrier, receiver the consignee.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:StorageLocation/cbc:ID` = `XLSEL-RR-07`: an ID without schemeID — refuted: a port's own position number (party-internal), with the port's UN/LOCODE as prefix.
