# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/17-TransportationStatus.xml`, Git blob `ca6268e2b075e6b8011b2c7aa08d386ab1c51391` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/17#F1 · High · Shipping order ID is the consignment ID; the referenced bill of lading names another shipping order
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- Why: `ShippingOrderID` is "A reference number for a shipping order." The value is the consignment identifier of the same document (`Consignment/ID`), an identifier of another kind. The bill of lading this status refers to (`TOL-BL-26-0139`) gives the shipping order as `BF-FI-26-0137`, the forwarder's instructions to the carrier (`12-ForwardingInstructions.xml`), so the two examples contradict each other. Across the flow the element carries three values for the same shipment (merge, grep of `<cbc:ShippingOrderID>` over `sea/*.xml`): `LD-SH-26-0132` in 09 and 12 (the shipment ID), `LD-CS-26-0133` in 13 and 17 (the consignment ID), `BF-FI-26-0137` in 14.
- Condition: `ShippingOrderID`, if present, is the identifier of the shipping order and the same as in `14-BillOfLading.xml`.
- Options: (a) preferred: `BF-FI-26-0137`, as on the bill of lading (the forwarding instruction that booked the carriage exists in the flow; same preference as the air flow's merges); (b) drop it: the consignment and the bill of lading reference already identify the shipment (context's preference).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, Medium)

### sea/17#F2 · Medium · Detention of the transport means used for a pallet-marking check on the container
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:OccurrenceTime` = `12:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:OccurrenceTime` = `11:20:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: `DetentionTransportEvent` under a shipment stage is "The detention of a transport means during loading and unloading operations", i.e. the ship being held. At 12:00 the container had already been discharged (11:20); what was held for the heat-treatment check (ISPM 15 mark, own knowledge) is the container and its pallets, which the document records separately as the container's quarantine (completed 15:00). What happened, according to `28-DebitNote.xml:/DebitNote/cac:DiscrepancyResponse/cbc:Description` = `Heat-treatment mark illegible on pallet 095206101230000070.`, is an illegible mark on one pallet; the description instead states a general rule, not an event.
- Condition: No detention of the transport means is reported unless the ship was held; the hold of the container is recorded on the container, with a description of what happened.
- Options: (a) preferred: drop the stage-level detention and describe the hold on the container's quarantine event (start 12:00 as an event or in the description, completion 15:00); (b) if the story wants the ship held, a reason concerning the ship and a time before discharge ended.
- Needs decision: no
- From: broad (F2), context (F2), logistics (F2)

### sea/17#F3 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; both values are the ISO 639 language code already in `Language/cbc:ID` (`listID="ISO 639"`), so they name no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F1)

### sea/17#F4 · Low · Container events without type, description, reason or place
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-18`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEvent/cbc:OccurrenceTime` = `11:40:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The equipment's `TransportEvent` is "An additional transport event not specified elsewhere in this Transport Equipment"; it carries only a date and a time, no type code, description or location, so the receiver cannot tell what happened at 11:40 (between discharge 11:20 and the hold 12:00); without that it has no business content (IND5). The quarantine event gives no reason or place; it can be linked to the pallet problem only through `28-DebitNote.xml`.
- Condition: Every event says what it is (type or description) and, where it matters, where; the quarantine says why.
- Options: (a) preferred: give the 11:40 event a type and description (e.g. container moved to the inspection area) and the quarantine a description and location; (b) drop the 11:40 event.
- Needs decision: no
- From: broad (F3), context (F3), logistics (F3)

### sea/17#F5 · Low · The discharge is reported twice, once as an "additional" event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 discharged and available for customs clearance.`
- XPath: `/TransportationStatus/cbc:Description` = `Container TWLU4120872 discharged and available for customs clearance.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DischargeTransportEvent/cbc:OccurrenceTime` = `11:20:00`
- Why: The document-level `TransportEvent` is for "Any additional events associated with this Transportation Status report that are not defined elsewhere in this document". The discharge is already in the dedicated `DischargeTransportEvent`; the extra event repeats the document `Description` word for word, with a date but no time. Only "available for customs clearance" is new, and that is a status that comes after the quarantine (15:00).
- Condition: The discharge is reported once, in its dedicated element; an additional event adds something not expressed elsewhere.
- Options: (a) preferred: keep the additional event only for the release for customs clearance, with its time (after 15:00); (b) drop it.
- Needs decision: no
- From: context (F4)

### sea/17#F6 · Low · "Automatic report" while a named duty officer reports, and an instruction about a delivery slot the report does not contain
- XPath: `/TransportationStatus/cbc:Note[2]` = `Automatic report from the sender's tracking system.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ReportingPerson/cbc:JobTitle` = `Duty officer`
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: The note says the report is generated automatically, but the main-carriage stage names the port's duty officer as `ReportingPerson` ("a person being responsible for providing the required administrative reporting relating to a transport"); the `OtherInstruction` refers to a "delivery slot", but the document contains no delivery or slot (it reports arrival, discharge, quarantine and availability for clearance). The parties part refuted the duty officer as reporting person (a legitimate reading of the definition for the sender's report) and read the slot as the forwarder's on-carriage; the merge accepts the reporting person as such but keeps the mismatch with the "automatic" note and the slot that the report does not state.
- Condition: The notes and instructions describe what this report is and refer only to things the report contains or the receiver can identify.
- Options: (a) preferred: drop the "automatic" note (or the reporting person) and let the instruction refer to something in the report (e.g. collection after clearance); (b) add the delivery slot, if the port books one.
- Needs decision: no
- From: context (F5); parties' refutation of the reporting person carried as counter-argument

### sea/17#F7 · Low · The contacts do not fit the roles in a discharge notice
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- Why: The consignee is "the party who receives the goods", but its contact is named Purchasing with the job title customer service officer in Sales: name, title and department disagree, and none is goods receipt or import. The same consignee contact occurs in 24 examples of the flow (parties, grep over sea `*.xml`), i.e. master data. The terminal's "Port control" (a vessel-traffic function) is an operations planner with office hours. The receiver's "Export desk" for an import-side status is the weakest part: broad refuted it (Bayforth booked the export and follows the shipment to delivery; its export desk is its single shipment contact), and the merge keeps it only as part of this grouped remark.
- Condition: Each contact's name, job title and department agree, and the consignee's and terminal's contacts are the functions that handle the arrival and release of the container.
- Options: (a) preferred: role-specific contacts (consignee: goods receipt or import desk; terminal: container desk; forwarder: arrivals desk if it has one); (b) leave out contacts that do not serve the report.
- Needs decision: no
- From: broad (F4), parties (F2)

### sea/17#F8 · Low · Tax registrations and share capital in a status report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: A transportation status circulates events; it bills nothing and does nothing with the carrier's and the forwarder's Bayvarran sales-tax registrations or the carrier's share capital: master data copied into a document that does not use them (section 4.8).
- Condition: Carrier and receiver carry only the party data a status report uses.
- Options: (a) preferred: drop `PartyTaxScheme` from both and `CorporateStockAmount`/`FullyPaidSharesIndicator` from the carrier; (b) keep them with a stated reason.
- Needs decision: no
- From: parties (F3), money (F2)

### sea/17#F9 · Low · Terminal handling charge of the Lisavan terminal in Bayvarran currency, reported to a party that does not pay it
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `185.00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:AllowanceChargeReason` = `Terminal handling at Selanu`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cac:AllowanceCharge/cbc:Amount` = `185.00`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `Terminal handling at Selanu collect from the consignee.`
- Why: `ServiceAllowanceCharge` is "a service allowance charge associated with this piece of transport equipment". The status comes from the Port of Selanu, which performs the handling, but the charge is in XBL (Bayvarra), while amounts arising in Lisavu elsewhere in the flow are in XLC (`19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`; `28-DebitNote.xml:/DebitNote/cbc:DocumentCurrencyCode` = `XLC`). On the bill of lading the same 185.00 is a carrier's tariff item collected from the consignee, so XBL is plausible there. Here it goes to the shipper's forwarder, while the consignee pays it, and the report does not say who pays. Counter-arguments: broad refuted the currency (the bill of lading fixes it in XBL, and Trade Accord parties trade in lume); context refuted the presence (telling the forwarder what the terminal will charge is a real reason). The merge cannot settle it.
- Condition: Either the charge is stated in the currency the terminal bills it in (or with a reason for XBL) and the report makes clear the consignee pays it, or it is left out because the bill of lading already carries it.
- Options: (a) preferred: leave it out of the status; (b) keep it, in XLC (185.00 XBL × 0.4 = 74.000 XLC at `14-BillOfLading.xml:/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`) or with a stated reason for XBL.
- Needs decision: yes
- From: money (F1); broad and context refuted parts of it (arguments above)

## Checked and consistent
- Reference `TOL-BL-26-0139` resolves to `14-BillOfLading.xml`: same consignment `LD-CS-26-0133`, container `TWLU4120872` (ISO 6346 check digit 2 correct), carrier Tidewell Ocean Lines and consignee Velumi Trading; stage ID 2 agrees with the main carriage stage of 14 and 15 (broad, logistics, context).
- Timeline within the document (merge re-checked): arrival 06:30, discharge 11:20 (completed), container event 11:40, detention 12:00, quarantine 15:00 (completed), issue 16:36; all before the issue time. Arrival agrees with the requested arrival 06:00 at the fairway buoy in `16-CommonTransportationReport.xml`.
- The charge 185.00 XBL with reason code HD (UN/EDIFACT 7161) equals the bill of lading's terminal handling charge (broad, money).
- Port of Selanu's address, coordinates and UN/LOCODE `XLSEL` agree with `16-CommonTransportationReport.xml`; the Port of Selanu and Velumi carry `en-XL` and Lisavan renderings, as in the other examples issued on the island (parties).
- Sender and signatory are the Port of Selanu, also the terminal operator; consignee and carrier match the bill of lading by identifier and name; the consignee's customs trader ID fits a report that goods are available for clearance; ISIC codes fit (parties).

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `185.00`: a Lisavu port charging in XBL — refuted by broad because the bill of lading fixes the charge in XBL and Trade Accord parties trade in lume; context refuted the presence (a real reason to tell the forwarder). Both carried into F9 as counter-arguments, since money raised it (from broad, context).
- `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`: the import-side status goes to the export desk — refuted by broad (Bayforth's single shipment contact); kept as the weakest part of F7 (from broad).
- `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Port of Selanu`: name without UN/LOCODE — refuted: the terminal operator's location in the same document carries `XLSEL` (from broad).
- `/TransportationStatus/cbc:Description` = `Container TWLU4120872 discharged and available for customs clearance.`: "available" despite the quarantine — refuted: the quarantine is completed (15:00) before the issue time (from broad).
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS`: contradicting the completed discharge — refuted: the transport to the consignee is not finished (from context).
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ReportingPerson/cbc:JobTitle` = `Duty officer`: the port's duty officer rather than the master as reporting person — refuted: the two documents report different things, and the sender's duty officer is a legitimate reading (from parties; see F6).
- `/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: the export forwarder as receiver of an import status — refuted: Bayforth is the forwarder of the whole consignment (`19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`) (from parties).
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode` = `4649`: wholesale of household goods for park benches — refuted: 4649 includes wholesale of furniture (from parties).
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`: detention costs that should appear as a charge — refuted: the hold was completed the same day (`/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:CompletionIndicator` = `true`); no charge implied (from money).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; context's Medium raised to High (contradiction with the referenced bill of lading, section 6); the flow-wide count of values added.
- broad/F2, context/F2, logistics/F2 → F2: combined.
- broad/F3, context/F3, logistics/F3 → F4: combined.
- context/F5 → F6: kept, with parties' refutation of the reporting person carried and the finding narrowed to the note/slot mismatch.
- broad/F4, parties/F2 → F7: all contacts grouped (as earlier flows); broad's refuted "Export desk" included as the weakest part.
- parties/F3, money/F2 → F8: combined.

## Outside this review
- `13-TransportationStatus.xml` also uses the consignment ID as `ShippingOrderID`, and 09/12 use the shipment ID; those belong to those examples' reviews (from broad, merge).
- `14-BillOfLading.xml` expects the container to be available on 2026-05-18 at 14:00; here it is released after the quarantine at 15:00 (timeline across documents) (from logistics).
