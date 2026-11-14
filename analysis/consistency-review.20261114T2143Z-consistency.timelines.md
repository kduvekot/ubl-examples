# Consistency review: timelines

Run: `20261114T2143Z-consistency` · Review date: 2026-11-14 · Topic: timelines
Examples: 250 in 18 flows, at commit c41ed3c (claude/stoic-noether-5pboei); tables rebuilt from the same commit (README of `.review/tables`: "examples changed against the commit: no").
Inputs: the XML examples, the extraction tables, the merged per-example reviews, `analysis/review-merge-decisions.md`, the finished conditions review of this run (for its notes to this topic and its F7), the output of `check_consistency.py`, and own knowledge of transport practice where stated. No world data, generators or companion documentation were read.

## What is expected

Every finding below, and every entry under "Considered and refuted", "Leads" and "Cannot be told", is looked into and ends either resolved (its condition holds in the XML) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by the owner first, because the fix changes the story of the world (dates of a flow, where places lie, which goods travel when), not only an encoding. This review describes what is inconsistent in time across documents and flows; it does not say where or how the examples are produced.

## The world as the documents state it

### How to read the tables

One table per flow, in issue order (date, time, weekday). "Dated events and periods" lists the transport events, despatch/delivery/pickup dates, manufacture dates, receipt and payment dates, and the business periods (delivery, invoice, procurement, appeal, service, status, reminder periods) the document carries; measurement periods of emission data, registration dates, due dates, exchange-rate dates and validity periods are left out (they are in `dates.csv`/`periods.csv`). "Refers to" lists the examples whose document ID the document cites (same flow by number, other flows by `flow/NN`). Built mechanically from `documents.csv`, `dates.csv`, `periods.csv` and `references.csv`; every value used in a finding was checked in the XML.

### Links between flows (in time order)

| When | Flow → flow | What the documents say |
|---|---|---|
| 2026-02-16 → 02-27 | wood → (Valdara, Ferrano) | Marrowdale Sawmill sells hardwood slats (kiln lot `MS-L26-0223`, made 2026-02-23) to Valdara; despatched 2026-02-26, import-cleared in Urvania 2026-02-27 11:05 (wood/06, wood/07). |
| 2026-03-02 → 03-10 | ore → (Valdara, Ferrano) | Serravona Mining's ore train (30 wagons, 1788.4 t) for Valdara; waybill and despatch 2026-03-10; no arrival recorded (ore/04, ore/05). |
| 2026-03-20 | (Valdara) → road | Bench lot `VI-LOT-260320` and side-frame castings `VI-SF-01490`…`01501` (melt `M-26-0412`) made 2026-03-20 (road/04). |
| 2026-03-23 → 03-25 | road | 96 benches + 12 castings, Ferrano → Marrowdale by Trasvia truck `UR 4160 KT`; delivered 2026-03-25 09:40 to Lumeway. |
| 2026-03-27 → 03-31 | tender | Lot `VI-LOT-260327` (40 benches, moss green) made 2026-03-27, despatched from Castrano (Ferrano) 2026-03-30, import-cleared in Lumeport 2026-03-31. |
| 2026-04-13 → 04-15 | rail | 192 benches in two containers, Ferrano hub → Lumeway's siding at Marrowdale; departure 2026-04-14 06:52, delivery 2026-04-15 11:00. No lot or manufacture date stated. |
| 2026-04-26 → 04-30 | retail | Lot `VI-LOT-260426` "from the distributor's stock", made 2026-04-26 (a Sunday), despatched by Lumeway in Marrowdale 2026-04-29, received at Brightmarket 2026-04-30. |
| 2026-05-10 → 05-21 | sea | Lot `VI-LOT-260510` (96 benches) and castings `VI-SF-01230`…`01241` (melt `M-26-0412`) made 2026-05-10, "from the distributor's stock"; despatched 2026-05-13 from Lumeway, shipped Lumeport → Selanu 2026-05-14/18, received 2026-05-21. |
| 2026-05-10/11 → 05-14 | air | Castings `VI-SF-03190`…`03197` (melt `M-26-0412`) made 2026-05-10 (air/06) or 2026-05-11 (air/08), ready at Lumeway's dispatch area in Marrowdale 2026-05-12, flown Lumeport → Selanu 2026-05-14. The air order change cites the sea order `VT-PO-26-0127`. |
| 2026-03 (month) | energy → utilities | Gas meter `FG-G-20417` read by Ferrano Grid for 2026-02-28 → 03-31 (energy/01, issued 2026-04-02 17:42) and billed onward by Ferrano Energy to Valdara in utilities/02 (issued 2026-04-02 13:20). |
| 2026-03 (month) | energy | Kelpstone's pipeline gas for March: export declaration 39200 MWh, import declaration 36800 MWh, invoices 36800 + 2400 MWh (all issued 2026-04-02/03). |
| 2026-03-01 → 03-06 | cotton | Container `TWLU4123110` with 27 bales Selanu → Lumeport on `Tidewell Reef`; bill of lading 2026-03-02, pre-arrival report 2026-03-03, import declaration 2026-03-06; no loading, departure or arrival time anywhere. |


### Timeline per flow

#### air

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-05-11 07:50 Mon | 01-OrderChange `VT-OC-26-0320` |  | sea/05 |
| 2026-05-12 10:46 Tue | 02-OrderResponse `LD-OR-26-0321` |  | 01, sea/05 |
| 2026-05-12 13:44 Tue | 03-ForwardingInstructions `LD-FI-26-0322` | Event 2026-05-13 19:00; Pickup.EarliestPickup 2026-05-12; Despatch.RequestedDespatch 2026-05-13; RequestedDeliveryPeriod 2026-05-14–2026-05-14 |  |
| 2026-05-13 10:05 Wed | 05-TransportationStatus `LACT-TS-26-0326` | Event 2026-05-13 | 04 |
| 2026-05-13 10:07 Wed | 06-DespatchAdvice `LD-DA-26-0327` | ItemInstance.Manufacture 2026-05-10 06:40 |  |
| 2026-05-13 10:43 Wed | 04-Waybill `KXL-WB-26-0325` | RequestedDeparture 2026-05-14 07:00; RequestedArrival 2026-05-14 10:00 |  |
| 2026-05-14 10:48 Thu | 08-DespatchAdvice `LD-DA-26-0329` | ItemInstance.Manufacture 2026-05-11 06:40 |  |
| 2026-05-14 17:53 Thu | 07-FulfilmentCancellation `LD-DOC-26-0328` |  | 01, 06, sea/05 |
| 2026-05-14 17:58 Thu | 09-TransportationStatus `SAC-TS-26-0330` | Event 2026-05-14 | 04 |
| 2026-05-15 17:03 Fri | 10-Invoice `BF-INV-26-0331` |  | 04 |

#### carnet

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-05-25 15:04 Mon | 01-GoodsItemPassport `FCC-DOC-26-0724` |  |  |
| 2026-07-24 08:50 Fri | 02-ProofOfReexportationRequest `SCC-DOC-26-0726` |  |  |
| 2026-08-23 12:04 Sun | 03-ProofOfReexportationReminder `SCC-DOC-26-0727` |  | 02 |
| 2026-08-28 13:19 Fri | 04-ProofOfReexportation `FCC-DOC-26-0728` |  |  |

#### contest

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-02-02 10:07 Mon | 01-PriorInformationNotice `LPWD-DOC-26-0633` |  |  |
| 2026-02-23 11:17 Mon | 02-PriorInformationNotice `LPWD-DOC-26-0633` |  |  |
| 2026-03-19 08:51 Thu | 03-ContractNotice `LPWD-DOC-26-0634` | TenderSubmissionDeadlinePeriod –2026-06-12 12:00; ParticipationRequestReceptionPeriod –2026-04-18 | 01, 02 |
| 2026-03-20 15:02 Fri | 05-QualificationApplicationRequest `LPWD-DOC-26-0636` |  |  |
| 2026-03-20 16:56 Fri | 04-CallForTenders `LPWD-DOC-26-0635` | TenderSubmissionDeadlinePeriod –2026-06-12 12:00; ParticipationRequestReceptionPeriod –2026-04-18 | 01, 02 |
| 2026-04-01 08:04 Wed | 06-QualificationApplicationResponse `BF-DOC-26-0637` |  |  |
| 2026-04-01 16:10 Wed | 07-TendererQualification `BF-DOC-26-0638` |  |  |
| 2026-04-05 08:19 Sun | 08-ContractNotice `LPWD-DOC-26-0634` | TenderSubmissionDeadlinePeriod –2026-06-12 12:00; ParticipationRequestReceptionPeriod –2026-05-02 | 01, 02 |
| 2026-04-05 09:40 Sun | 10-QualificationApplicationRequest `LPWD-DOC-26-0636` |  |  |
| 2026-04-05 16:45 Sun | 09-CallForTenders `LPWD-DOC-26-0635` | TenderSubmissionDeadlinePeriod –2026-06-12 12:00; ParticipationRequestReceptionPeriod –2026-05-02 | 01, 02 |
| 2026-04-13 09:52 Mon | 12-TendererQualification `BF-DOC-26-0638` |  |  |
| 2026-04-13 14:18 Mon | 11-QualificationApplicationResponse `BF-DOC-26-0637` |  |  |
| 2026-05-05 08:38 Tue | 13-BusinessInformation `BIS-DOC-26-0639` |  |  |
| 2026-05-09 09:33 Sat | 14-BusinessInformation `BIS-DOC-26-0639` |  |  |
| 2026-07-02 11:31 Thu | 15-ContractAwardNotice `LPWD-DOC-26-0640` | TenderResult.Award 2026-06-28 | 03, 08 |
| 2026-07-05 12:33 Sun | 16-ContractAwardNotice `LPWD-DOC-26-0640` | TenderResult.Award 2026-06-28 | 03, 08 |

#### cotton

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-01-13 09:45 Tue | 01-SelfBilledInvoice `SCG-SBI-26-0191` |  |  |
| 2026-02-02 09:00 Mon | 02-Forecast `LTM-FC-26-0192` | ForecastPeriod 2026-02-16–2026-06-02 |  |
| 2026-02-05 14:29 Thu | 03-DeliveryNote `LCF-DN-26-0193` | Delivery.ActualDelivery 2026-02-05 |  |
| 2026-02-07 15:50 Sat | 04-SelfBilledInvoice `SCG-SBI-26-0194` | Delivery.ActualDelivery 2026-02-05; PrepaidPayment.Paid 2026-01-13; InvoicePeriod 2026-02-03–2026-02-05 | 01, 03 |
| 2026-02-14 13:28 Sat | 05-SelfBilledCreditNote `SCG-SBC-26-0195` | Delivery.ActualDelivery 2026-02-05; InvoicePeriod 2026-02-03–2026-02-05 | 03, 04 |
| 2026-02-16 13:06 Mon | 06-RemittanceAdvice `SCG-RM-26-0196` |  | 04, 05 |
| 2026-02-22 11:08 Sun | 07-ForecastRevision `LTM-FR-26-0197` | ForecastPeriod 2026-02-16–2026-06-02; ForecastPeriod 2026-04-03–2026-06-02 | 02 |
| 2026-02-24 10:37 Tue | 08-Order `LTM-PO-26-0198` |  |  |
| 2026-02-25 11:39 Wed | 09-ForwardingInstructions `LTM-FI-26-0199` |  | 08 |
| 2026-02-28 14:43 Sat | 10-GoodsCertificate `SCC-GC-26-0202` |  | 08 |
| 2026-03-01 13:33 Sun | 11-ExportCustomsDeclaration `SCG-EX-26-0203` |  | 08 |
| 2026-03-01 15:19 Sun | 12-WeightStatement `SCG-WS-26-0205` |  |  |
| 2026-03-02 09:37 Mon | 13-BillOfLading `TOL-BL-26-0206` |  | 09 |
| 2026-03-02 12:38 Mon | 16-Invoice `SCG-INV-26-0210` |  | 08 |
| 2026-03-03 11:22 Tue | 14-CommonTransportationReport `TOL-CTR-26-0207` |  |  |
| 2026-03-04 10:40 Wed | 17-Invoice `BF-INV-26-0211` |  | 13 |
| 2026-03-06 15:32 Fri | 15-ImportCustomsDeclaration `LTM-IM-26-0209` |  | 13 |
| 2026-03-29 15:45 Sun | 18-RemittanceAdvice `LTM-RM-26-0212` |  | 16 |

#### energy

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-02 16:41 Thu | 04-ExportCustomsDeclaration `KG-EX-26-0152` |  |  |
| 2026-04-02 16:55 Thu | 05-ImportCustomsDeclaration `MP-IM-26-0156` |  |  |
| 2026-04-02 17:42 Thu | 01-UtilityStatement `FG-DOC-26-0149` | MeterReading.PreviousMeterReading 2026-02-28; MeterReading.LatestMeterReading 2026-03-31 | 02 |
| 2026-04-03 08:20 Fri | 02-Invoice `FG-INV-26-0150` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-03 11:25 Fri | 06-Invoice `KG-INV-26-0157` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-03 15:31 Fri | 07-Invoice `KG-INV-26-0158` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-03 16:42 Fri | 03-Invoice `MP-INV-26-0151` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-06-03 09:46 Wed | 08-Reminder `KG-DOC-26-0159` | ReminderPeriod 2026-05-04–2026-06-03; ReminderPeriod 2026-05-04– | 06 |
| 2026-06-06 16:36 Sat | 09-RemittanceAdvice `MP-RM-26-0160` |  | 06, 08 |

#### furniture

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-03-02 10:00 Mon | 01-RequestForQuotation `BS-DOC-26-0567` |  |  |
| 2026-03-06 08:58 Fri | 02-Quotation `BF-DOC-26-0568` |  | 01 |
| 2026-03-12 12:44 Thu | 03-ItemInformationRequest `BF-DOC-26-0569` |  | 02 |
| 2026-03-14 08:23 Sat | 04-TradeItemLocationProfile `BS-DOC-26-0570` |  | 02 |
| 2026-03-14 09:21 Sat | 05-ExceptionCriteria `BS-DOC-26-0571` |  | 04 |
| 2026-03-16 11:16 Mon | 08-Order `BS-PO-26-0574` |  | 02 |
| 2026-03-22 12:42 Sun | 09-Invoice `BF-INV-26-0575` |  | 08 |
| 2026-04-01 08:46 Wed | 15-Order `LPWD-PO-26-0581` |  |  |
| 2026-04-09 Thu | 16-WorkReport `BF-DOC-26-0582` | ReportedPeriod 2026-04-08–2026-04-09 | 15 |
| 2026-04-09 10:10 Thu | 17-Invoice `BF-INV-26-0583` | InvoicePeriod 2026-04-08–2026-04-09 | 15, 16 |
| 2026-04-16 12:09 Thu | 10-Order `BS-PO-26-0576` |  | 08 |
| 2026-04-20 16:35 Mon | 06-ProductActivity `BS-DOC-26-0572` | ActivityPeriod 2026-03-23–2026-04-20 | 03 |
| 2026-04-21 17:49 Tue | 07-ExceptionNotification `BF-DOC-26-0573` | ExceptionObservationPeriod 2026-03-23–2026-04-20 | 05, 06 |
| 2026-04-22 11:51 Wed | 11-OrderCancellation `BS-DOC-26-0577` |  | 06, 07, 10 |
| 2026-04-27 14:21 Mon | 12-InstructionForReturns `BF-DOC-26-0578` | RequestedDeliveryPeriod 2026-04-29–2026-05-02 | 07 |
| 2026-05-03 11:55 Sun | 13-CreditNote `BF-CN-26-0579` |  | 08, 09, 12 |
| 2026-05-04 11:12 Mon | 14-DebitNote `BS-DOC-26-0580` | Delivery.ActualDelivery 2026-05-02 | 02, 08, 12, 13 |

#### mast

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-06-01 08:15 Mon | 01-Order `ST-PO-26-0713` |  |  |
| 2026-06-03 11:57 Wed | 02-ForwardingInstructions `SE-FI-26-0714` |  |  |
| 2026-06-04 13:20 Thu | 04-DespatchAdvice `SE-DA-26-0718` |  | 01 |
| 2026-06-04 17:15 Thu | 03-Waybill `KXL-WB-26-0717` |  |  |
| 2026-06-04 17:34 Thu | 05-Invoice `SE-INV-26-0719` |  | 01, 04 |

#### ore

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-03-02 11:10 Mon | 01-Order `VI-PO-26-0304` | RequestedDeliveryPeriod 2026-03-09–2026-03-13 |  |
| 2026-03-03 09:24 Tue | 02-TransportExecutionPlanRequest `VI-TR-26-0305` | ServiceStartTimePeriod 2026-03-10–; ServiceEndTimePeriod –2026-03-13 |  |
| 2026-03-04 12:50 Wed | 03-TransportExecutionPlan `FRC-TEP-26-0307` | ServiceStartTimePeriod 2026-03-10–; ServiceEndTimePeriod –2026-03-13; NotificationPeriod 2026-03-04–2026-03-08 | 02 |
| 2026-03-10 11:35 Tue | 05-Waybill `FRC-WB-26-0310` |  | 03 |
| 2026-03-10 15:37 Tue | 04-DespatchAdvice `SM-DA-26-0308` |  | 01 |
| 2026-03-11 14:59 Wed | 07-Invoice `SM-INV-26-0312` |  | 01, 04 |
| 2026-03-12 14:45 Thu | 06-Invoice `FRC-INV-26-0311` |  | 03, 05 |
| 2026-04-09 12:10 Thu | 08-RemittanceAdvice `VI-RM-26-0313` |  | 07 |

#### packaging

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-27 08:44 Mon | 01-Order `VI-PO-26-0521` |  |  |
| 2026-04-29 08:56 Wed | 03-Order `LTM-PO-26-0523` |  |  |
| 2026-05-02 14:06 Sat | 02-Invoice `RP-INV-26-0522` |  | 01 |
| 2026-05-03 08:11 Sun | 04-Invoice `RP-INV-26-0524` |  | 03 |
| 2026-05-07 09:33 Thu | 05-Order `BS-PO-26-0525` |  |  |
| 2026-05-12 11:35 Tue | 06-DespatchAdvice `LTM-DA-26-0526` |  | 05 |
| 2026-05-12 14:49 Tue | 07-Invoice `LTM-INV-26-0529` |  | 05 |
| 2026-05-22 16:05 Fri | 08-PurchaseReceipt `BS-PR-26-0530` | PurchaseReceipt.Issue 2026-05-22 16:05; PurchaseReceipt.Transaction 2026-05-22 16:05; PurchaseReceipt.Purchase 2026-05-22 16:05; Payment.Paid 2026-05-22 16:05 |  |
| 2026-05-23 12:20 Sat | 09-PurchaseReceipt `BS-PR-26-0531` | PurchaseReceipt.Issue 2026-05-23 12:20; PurchaseReceipt.Transaction 2026-05-23 12:20; PurchaseReceipt.Purchase 2026-05-23 12:20; Payment.Paid 2026-05-23 |  |

#### plastics

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-13 16:17 Mon | 01-Order `RP-PO-26-0882` |  |  |
| 2026-04-14 09:57 Tue | 03-TransportExecutionPlanRequest `RR-TR-26-0884` | ServiceStartTimePeriod 2026-04-19–; ServiceEndTimePeriod –2026-04-22 |  |
| 2026-04-14 15:39 Tue | 02-OrderResponse `RR-OR-26-0883` |  | 01 |
| 2026-04-15 13:10 Wed | 04-TransportExecutionPlan `FB-TEP-26-0886` | Loading 2026-04-19 13:30; Exportation 2026-04-20 16:00; Discharge 2026-04-22 08:00; Takeover 2026-04-19 09:00; ServiceStartTimePeriod 2026-04-19–; ServiceEndTimePeriod –2026-04-22 | 03 |
| 2026-04-19 09:38 Sun | 06-Waybill `FB-WB-26-0890` | Loading 2026-04-19 13:30; Exportation 2026-04-20 16:00; Discharge 2026-04-22 08:00; Takeover 2026-04-19 09:00; Delivery.LatestDelivery 2026-04-23; Pickup.EarliestPickup 2026-04-19 08:00; Pickup.LatestPickup 2026-04-19 16:00; Despatch.ActualDespatch 2026-04-19 15:10 | 01, 04 |
| 2026-04-19 16:08 Sun | 05-ExportCustomsDeclaration `RR-EX-26-0887` |  | 01 |
| 2026-04-19 17:57 Sun | 08-DespatchAdvice `RR-DA-26-0892` | ItemInstance.Manufacture 2026-04-16; ItemInstance.BestBefore 2027-04-16 | 01 |
| 2026-04-20 11:20 Mon | 10-Invoice `RR-INV-26-0894` |  | 01, 08 |
| 2026-04-22 10:35 Wed | 09-ImportCustomsDeclaration `RP-IM-26-0893` |  | 06 |
| 2026-04-22 14:20 Wed | 07-Invoice `FB-INV-26-0891` |  | 06 |
| 2026-05-19 09:34 Tue | 11-RemittanceAdvice `RP-RM-26-0895` |  | 10 |

#### rail

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-06 16:18 Mon | 01-Order `LD-PO-26-0325` |  |  |
| 2026-04-07 10:32 Tue | 02-TransportExecutionPlanRequest `VI-TR-26-0326` | RequestedPickup 2026-04-13 15:00; RequestedDelivery 2026-04-16; RequestedDeparture 2026-04-14 07:00; RequestedArrival 2026-04-15; RequestedWaypoint 2026-04-14; ServiceStartTimePeriod 2026-04-14–; ServiceEndTimePeriod –2026-04-17 |  |
| 2026-04-08 16:46 Wed | 03-TransportExecutionPlan `FRC-TEP-26-0328` | PlannedPickup 2026-04-13 15:00; PlannedDelivery 2026-04-15 11:00; PlannedDeparture 2026-04-14 06:45; PlannedArrival 2026-04-15 10:30; EstimatedDeparture 2026-04-14 06:50; EstimatedArrival 2026-04-15 10:40; NominationPeriod 2026-04-06–2026-04-12; ServiceStartTimePeriod 2026-04-14–; ServiceEndTimePeriod –2026-04-17 | 02 |
| 2026-04-14 06:30 Tue | 04-TransportProgressStatusRequest `FRC-DOC-26-0329` |  |  |
| 2026-04-14 06:45 Tue | 05-TransportProgressStatus `FIH-DOC-26-0330` | ActualArrival 2026-04-14 05:30; ActualDeparture 2026-04-14 06:52; EstimatedDeparture 2026-04-14 06:50; EstimatedArrival 2026-04-15 10:40; PlannedDeparture 2026-04-14 06:45; PlannedArrival 2026-04-15 10:30 | 04 |
| 2026-04-14 09:00 Tue | 09-GoodsItemItinerary `FRC-DOC-26-0335` |  |  |
| 2026-04-14 13:10 Tue | 08-Waybill `FRC-WB-26-0334` | PlannedDeparture 2026-04-14 06:45; PlannedArrival 2026-04-15 10:30; PlannedWaypoint 2026-04-14 13:00; ActualDeparture 2026-04-14 06:52; ActualWaypoint 2026-04-14 13:20; EstimatedDeparture 2026-04-14 06:50; EstimatedArrival 2026-04-15 10:40; Positioning 2026-04-12 08:00; Delivery 2026-04-15 11:00; Pickup 2026-04-13 15:00; Handling 2026-04-13 18:30; Loading 2026-04-14 05:40; Delivery.LatestDelivery 2026-04-16; Pickup.ActualPickup 2026-04-13 15:00; Despatch.ActualDespatch 2026-04-14 06:50 | 03 |
| 2026-04-14 13:11 Tue | 07-TransportationStatus `FIH-TS-26-0333` | OptionalTakeover 2026-04-14 17:00; ActualPickup 2026-04-13 15:00; Delivery 2026-04-15 11:00; Event 2026-04-14 05:40; Event 2026-04-14 | 03 |
| 2026-04-14 17:29 Tue | 06-TransitCustomsDeclaration `VI-TD-26-0331` |  | 03 |
| 2026-04-17 11:14 Fri | 11-Invoice `VI-INV-26-0337` |  | 01 |
| 2026-04-17 12:04 Fri | 10-Invoice `FRC-INV-26-0336` |  | 08 |

#### retail

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-20 08:42 Mon | 01-CatalogueRequest `BS-DOC-26-0217` |  |  |
| 2026-04-20 17:28 Mon | 02-Catalogue `LD-CAT-26-0218` |  |  |
| 2026-04-22 08:17 Wed | 06-RetailEvent `BS-RE-26-0222` |  |  |
| 2026-04-22 11:55 Wed | 05-Forecast `BS-FC-26-0221` | ForecastPeriod 2026-05-04–2026-06-15 |  |
| 2026-04-23 17:43 Thu | 07-InventoryReport `BS-IR-26-0223` | InventoryPeriod 2026-04-16–2026-04-23 | 05 |
| 2026-04-24 08:15 Fri | 08-Order `BS-PO-26-0224` |  | 02, 06 |
| 2026-04-25 10:28 Sat | 11-TransportExecutionPlanRequest `LD-TR-26-0227` | ServiceStartTimePeriod 2026-04-29–; ServiceEndTimePeriod –2026-05-02 |  |
| 2026-04-26 11:14 Sun | 10-DocumentStatus `LD-DOC-26-0226` |  | 08, 11 |
| 2026-04-26 11:52 Sun | 09-DocumentStatusRequest `BS-DOC-26-0225` |  | 08 |
| 2026-04-29 08:56 Wed | 13-Waybill `BF-WB-26-0231` |  |  |
| 2026-04-29 10:59 Wed | 14-TransportationStatusRequest `LD-DOC-26-0232` | RequestedStatusPeriod 2026-04-29–2026-04-30 | 08 |
| 2026-04-29 11:49 Wed | 15-TransportationStatus `BF-TS-26-0233` | Event 2026-04-29; UpdatedDelivery 2026-04-29 14:00 | 14 |
| 2026-04-29 15:34 Wed | 12-DespatchAdvice `LD-DA-26-0229` | ItemInstance.Manufacture 2026-04-26 | 08, 11 |
| 2026-04-30 10:31 Thu | 16-Invoice `BF-INV-26-0234` |  | 13 |
| 2026-04-30 15:21 Thu | 17-ReceiptAdvice `BS-RA-26-0235` | ReceiptLine.Received 2026-04-30 10:40 | 08, 12 |
| 2026-04-30 15:52 Thu | 18-Invoice `LD-INV-26-0236` |  | 08, 12, 17 |
| 2026-05-02 13:26 Sat | 19-CreditNote `LD-CN-26-0237` | Delivery.ActualDelivery 2026-04-30 | 08, 12, 17, 18 |
| 2026-05-15 11:42 Fri | 21-PurchaseReceipt `BS-PR-26-0239` | PurchaseReceipt.Issue 2026-05-15 11:42; PurchaseReceipt.Transaction 2026-05-15 11:42; PurchaseReceipt.Purchase 2026-05-15 11:42; Payment.Paid 2026-05-15 11:42; RequestedDeliveryPeriod 2026-05-17 09:00–12:00:00 |  |
| 2026-05-20 13:10 Wed | 03-CataloguePricingUpdate `LD-DOC-26-0219` |  | 02 |
| 2026-05-21 09:01 Thu | 04-CatalogueItemSpecificationUpdate `LD-DOC-26-0220` |  | 02 |
| 2026-05-30 11:25 Sat | 22-Order `RA-PO-26-0240` | RequestedDeliveryPeriod 2026-06-01–2026-06-08 |  |
| 2026-06-19 17:05 Fri | 20-CatalogueDeletion `LD-DOC-26-0238` |  | 02 |

#### road

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-03-16 14:36 Mon | 01-Order `LD-PO-26-0149` | Despatch.RequestedDespatch 2026-03-23 14:00 |  |
| 2026-03-17 14:16 Tue | 03-TransportExecutionPlanRequest `LD-TR-26-0151` | RequestedPickup 2026-03-23 14:00; RequestedDelivery 2026-03-25 10:00; ServiceStartTimePeriod 2026-03-23–; ServiceEndTimePeriod –2026-03-26 |  |
| 2026-03-17 17:42 Tue | 02-OrderResponse `VI-OR-26-0150` | Despatch.EstimatedDespatch 2026-03-23 14:00; Despatch.GuaranteedDespatch 2026-03-24 12:00; PromisedDeliveryPeriod 2026-03-23–2026-03-23; EstimatedDespatchPeriod 2026-03-23–2026-03-24 | 01 |
| 2026-03-20 12:39 Fri | 06-CertificateOfOrigin `FCC-CO-26-0157` |  | 01 |
| 2026-03-22 08:41 Sun | 07-CertificateOfOrigin `FCC-CO-26-0157` |  | 01 |
| 2026-03-23 08:16 Mon | 08-Waybill `TH-WB-26-0159` | ActualPickup 2026-03-23 15:05; MainCarriageShipmentStage.EstimatedDelivery 2026-03-25 09:00; MainCarriageShipmentStage.RequiredDelivery 2026-03-25 10:00; Examination 2026-03-24 07:45; ActualDeparture 2026-03-23 16:20; Delivery.LatestDelivery 2026-03-25 12:00; TransitPeriod 2026-03-23–2026-03-25; EstimatedDeliveryPeriod 2026-03-25 09:00–11:00:00 |  |
| 2026-03-23 13:25 Mon | 05-ExportCustomsDeclaration `VI-EX-26-0155` |  | 01 |
| 2026-03-23 15:15 Mon | 04-DespatchAdvice `CL-DA-26-0153` | Despatch.ActualDespatch 2026-03-23 16:20; ItemInstance.Manufacture 2026-03-20; ItemInstance.Manufacture 2026-03-20 06:40 | 01 |
| 2026-03-24 09:10 Tue | 09-TransportationStatus `TH-TS-26-0160` | Event 2026-03-24 08:55; UpdatedPickup 2026-03-23 15:05; UpdatedDelivery 2026-03-25 09:30 | 08 |
| 2026-03-24 09:54 Tue | 10-ImportCustomsDeclaration `LD-IM-26-0161` |  | 04, 06, 07 |
| 2026-03-24 11:41 Tue | 15-Invoice `VI-INV-26-0166` |  | 01, 04 |
| 2026-03-25 11:07 Wed | 14-Invoice `TH-INV-26-0165` | ActualDelivery 2026-03-25 09:40 | 08, 13 |
| 2026-03-25 12:55 Wed | 16-ApplicationResponse `LD-DOC-26-0167` |  | 15 |
| 2026-03-25 15:40 Wed | 11-ReceiptAdvice `LD-RA-26-0162` | Delivery.ActualDelivery 2026-03-25 09:40; ReceiptLine.Received 2026-03-25 | 01, 04, 08 |
| 2026-03-26 10:46 Thu | 12-FulfilmentCancellation `LD-DOC-26-0163` |  | 01, 04, 11 |
| 2026-03-26 10:48 Thu | 13-ReceiptAdvice `LD-RA-26-0164` | Delivery.ActualDelivery 2026-03-25 09:40; ReceiptLine.Received 2026-03-25 | 01, 04, 08 |
| 2026-04-22 15:05 Wed | 17-RemittanceAdvice `LD-RM-26-0168` |  | 15 |

#### sea

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-05-04 09:17 Mon | 02-Catalogue `LD-CAT-26-0124` |  |  |
| 2026-05-04 16:39 Mon | 01-BusinessCard `LD-DOC-26-0123` |  |  |
| 2026-05-05 09:44 Tue | 04-DigitalCapability `LTAC-DCP-26-0126` |  |  |
| 2026-05-05 12:59 Tue | 03-DigitalAgreement `LD-DAG-26-0125` | AdoptionPeriod 2026-05-05–2026-05-19 |  |
| 2026-05-07 11:10 Thu | 05-Order `VT-PO-26-0127` |  | 02 |
| 2026-05-08 09:30 Fri | 06-OrderResponse `LD-OR-26-0128` | PromisedDeliveryPeriod 2026-05-14–2026-05-18 | 05 |
| 2026-05-08 14:00 Fri | 07-TransportServiceDescriptionRequest `LD-DOC-26-0129` |  |  |
| 2026-05-09 12:03 Sat | 08-TransportServiceDescription `TOL-DOC-26-0130` | Event 2026-05-14 18:00 | 07 |
| 2026-05-09 16:45 Sat | 09-ForwardingInstructions `LD-FI-26-0131` |  | 05 |
| 2026-05-10 09:15 Sun | 12-ForwardingInstructions `BF-FI-26-0137` |  | 05 |
| 2026-05-12 14:25 Tue | 11-ExportCustomsDeclaration `BF-EX-26-0135` |  | 05 |
| 2026-05-12 15:59 Tue | 10-PackingList `LD-PL-26-0134` |  | 05 |
| 2026-05-13 08:52 Wed | 20-DespatchAdvice `LD-DA-26-0145` | ItemInstance.Manufacture 2026-05-10; ItemInstance.Manufacture 2026-05-10 06:40 | 05, 10 |
| 2026-05-14 10:54 Thu | 14-BillOfLading `TOL-BL-26-0139` | Availability 2026-05-18 14:00; Storage 2026-05-13 10:30; Acceptance 2026-05-13 10:15; Dropoff 2026-05-13 10:15; Warehousing 2026-05-19; Receipt 2026-05-19; VerifiedGrossMass.Weighing 2026-05-12 15:30 | 10, 12 |
| 2026-05-14 12:32 Thu | 22-Invoice `LD-INV-26-0147` | PrepaidPayment.Received 2026-05-09; PrepaidPayment.Paid 2026-05-08 | 05 |
| 2026-05-14 16:05 Thu | 13-TransportationStatus `PL-TS-26-0138` | ActualDeparture 2026-05-14 18:10; Event 2026-05-14 |  |
| 2026-05-15 16:08 Fri | 15-Manifest `TOL-MF-26-0140` | EstimatedDeparture 2026-05-15 06:00; EstimatedArrival 2026-05-17 22:00 | 14 |
| 2026-05-16 15:38 Sat | 16-CommonTransportationReport `TOL-CTR-26-0141` | RequestedArrivalEvent 2026-05-18 06:00 | 15 |
| 2026-05-18 16:36 Mon | 17-TransportationStatus `PS-TS-26-0142` | Discharge 2026-05-18 11:20; Detention 2026-05-18 12:00; ActualArrival 2026-05-18 06:30; Quarantine 2026-05-18 15:00; Event 2026-05-18 11:40; Event 2026-05-18 | 14 |
| 2026-05-19 09:07 Tue | 19-ImportCustomsDeclaration `TCB-IM-26-0144` |  | 14 |
| 2026-05-19 11:33 Tue | 18-Invoice `BF-INV-26-0143` |  | 14 |
| 2026-05-21 17:22 Thu | 21-ReceiptAdvice `NW-RA-26-0146` | ReceiptLine.Received 2026-05-21 | 05, 14, 20 |
| 2026-05-22 10:30 Fri | 28-DebitNote `VT-DOC-26-0153` | Delivery.ActualDelivery 2026-05-21; InvoicePeriod 2026-05-18–2026-05-19 | 03, 05, 14, 20, 21, 22, 25 |
| 2026-05-30 13:49 Sat | 24-InvoiceStatusResponse `VT-DOC-26-0149` | Payment.Paid 2026-06-25 | 22, 27 |
| 2026-06-13 08:43 Sat | 25-Statement `HF-ST-26-0151` | CollectedPayment.Received 2026-05-09; StatementPeriod 2026-05-14–2026-06-13; InvoicePeriod 2026-05-08–2026-05-09 | 22 |
| 2026-06-13 10:25 Sat | 29-PurchaseReceipt `VT-PR-26-0154` | PurchaseReceipt.Issue 2026-06-13 10:25; PurchaseReceipt.Transaction 2026-06-13 10:25; Payment.Paid 2026-06-13 10:25 |  |
| 2026-06-15 10:49 Mon | 26-CreditNote `LD-CN-26-0152` | Delivery.ActualDelivery 2026-05-21 | 03, 05, 21, 22, 25 |
| 2026-06-25 15:43 Thu | 27-RemittanceAdvice `VT-RM-26-0150` |  | 22, 26 |
| (none)  | 23-InvoiceStatusRequest `LD-DOC-26-0148` |  | 22 |

#### tender

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-01-12 14:18 Mon | 01-PriorInformationNotice `LPWD-DOC-26-0187` | DeliveryPeriod 2026-04-02–2028-03-22 |  |
| 2026-02-11 08:32 Wed | 02-ContractNotice `LPWD-DOC-26-0188` | DocumentAvailabilityPeriod 2026-01-26–2026-02-25; TenderSubmissionDeadlinePeriod –2026-02-26 12:00; InvitationSubmissionPeriod 2026-01-26–2026-02-01; ParticipationRequestReceptionPeriod –2026-02-11; DeliveryPeriod 2026-04-02–2028-03-22 | 01 |
| 2026-02-12 13:26 Thu | 03-CallForTenders `LPWD-DOC-26-0189` | DocumentAvailabilityPeriod 2026-01-26–2026-02-25; TenderSubmissionDeadlinePeriod –2026-02-26 12:00; InvitationSubmissionPeriod 2026-01-26–2026-02-01; ParticipationRequestReceptionPeriod –2026-02-11; DeliveryPeriod 2026-04-02–2028-03-22 | 01 |
| 2026-02-13 08:25 Fri | 06-QualificationApplicationRequest `LPWD-DOC-26-0192` | ApplicablePeriod 2023-01-01–2025-12-31; ApplicablePeriod 2025-01-01–2025-12-31 |  |
| 2026-02-14 14:05 Sat | 04-ExpressionOfInterestRequest `MS-DOC-26-0190` |  | 02 |
| 2026-02-15 08:35 Sun | 05-ExpressionOfInterestResponse `LPWD-DOC-26-0191` |  | 04 |
| 2026-02-19 10:47 Thu | 07-QualificationApplicationResponse `BF-DOC-26-0193` | ApplicablePeriod 2025-01-01–2025-12-31 |  |
| 2026-02-20 15:50 Fri | 08-ProcurementStatusRequest `BF-DOC-26-0194` |  |  |
| 2026-02-21 11:44 Sat | 09-ProcurementStatus `LPWD-DOC-26-0195` | TenderSubmissionDeadlinePeriod –2026-02-26 12:00; InvitationSubmissionPeriod 2026-01-26–2026-02-01; ParticipationRequestReceptionPeriod –2026-02-11 | 08 |
| 2026-02-22 14:30 Sun | 10-UnsubscribeFromProcedureRequest `MS-DOC-26-0196` |  |  |
| 2026-02-23 14:48 Mon | 11-UnsubscribeFromProcedureResponse `LPWD-DOC-26-0197` |  | 10 |
| 2026-02-23 16:37 Mon | 17-Tender `BF-DOC-26-0203` |  | 13 |
| 2026-02-24 08:23 Tue | 14-GuaranteeCertificate `BL-DOC-26-0200` | ApplicablePeriod 2026-02-21–2026-05-27 |  |
| 2026-02-24 12:10 Tue | 19-Tender `BF-DOC-26-0205` |  | 13 |
| 2026-02-24 17:56 Tue | 18-TenderWithdrawal `BF-DOC-26-0204` |  | 17 |
| 2026-02-25 08:52 Wed | 13-TendererQualification `VI-DOC-26-0199` |  |  |
| 2026-02-25 09:13 Wed | 15-Tender `VI-DOC-26-0201` |  | 13 |
| 2026-02-25 17:47 Wed | 16-TenderReceipt `LPWD-DOC-26-0202` | TenderReceipt.Issue 2026-02-25 17:47; TenderReceipt.Registered 2026-02-25 11:42 | 15 |
| 2026-02-27 16:26 Fri | 12-BusinessInformation `BIS-DOC-26-0198` |  |  |
| 2026-03-03 15:09 Tue | 20-TendererQualificationResponse `LPWD-DOC-26-0206` | QualificationResolution.Resolution 2026-03-03 10:00; PresentationPeriod 2026-03-09–2026-03-19 |  |
| 2026-03-09 10:15 Mon | 23-UnawardedNotification `LPWD-DOC-26-0209` | TenderResult.Award 2026-03-09 09:30; ContractFormalizationPeriod 2026-03-19–2026-03-22; PresentationPeriod 2026-03-09–2026-03-19 |  |
| 2026-03-09 13:37 Mon | 22-AwardedNotification `LPWD-DOC-26-0208` | TenderResult.Award 2026-03-09 09:30; ContractFormalizationPeriod 2026-03-19–2026-03-22 |  |
| 2026-03-13 13:55 Fri | 21-ContractAwardNotice `LPWD-DOC-26-0207` | TenderResult.Award 2026-03-09 09:30; TenderResult.Start 2026-03-23; DocumentAvailabilityPeriod 2026-01-26–2026-02-25; TenderSubmissionDeadlinePeriod –2026-02-26 12:00; InvitationSubmissionPeriod 2026-01-26–2026-02-01; ParticipationRequestReceptionPeriod –2026-02-11; DeliveryPeriod 2026-04-02–2028-03-22; ContractFormalizationPeriod 2026-03-19–2026-03-22 | 01, 02 |
| 2026-03-19 17:24 Thu | 24-TenderContract `LPWD-DOC-26-0210` | TenderResult.Award 2026-03-09 09:30; TenderResult.Start 2026-03-23; ContractFormalizationPeriod 2026-03-19–2026-03-22 | 22 |
| 2026-03-21 10:18 Sat | 25-Catalogue `VI-CAT-26-0211` |  | 03 |
| 2026-03-23 14:40 Mon | 26-Order `LPWD-PO-26-0212` |  | 25 |
| 2026-03-24 08:06 Tue | 27-OrderChange `LPWD-OC-26-0213` |  | 26 |
| 2026-03-25 16:15 Wed | 28-OrderResponse `VI-OR-26-0214` |  | 26, 27 |
| 2026-03-30 13:40 Mon | 30-ExportCustomsDeclaration `VI-EX-26-0218` |  | 26 |
| 2026-03-30 17:37 Mon | 29-DespatchAdvice `CL-DA-26-0215` | ItemInstance.Manufacture 2026-03-27 | 26 |
| 2026-03-31 09:28 Tue | 32-Invoice `VI-INV-26-0221` |  | 26 |
| 2026-03-31 11:14 Tue | 31-ImportCustomsDeclaration `LPWD-IM-26-0220` |  |  |
| 2026-04-04 09:10 Sat | 33-CreditNote `VI-CN-26-0222` | InvoicePeriod 2026-03-31–2026-04-04; InvoicePeriod 2026-04-02– | 29, 32 |
| 2026-04-06 15:41 Mon | 34-DebitNote `LPWD-DOC-26-0223` |  | 26, 32 |
| 2026-05-05 15:23 Tue | 35-Reminder `VI-DOC-26-0224` | PrepaidPayment.Paid 2026-05-02; ReminderPeriod 2026-05-01–2026-05-05 | 32, 33, 34 |
| 2026-05-08 12:49 Fri | 36-RemittanceAdvice `LPWD-RM-26-0225` |  | 32, 33, 34, 35 |

#### utilities

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-04-02 09:13 Thu | 06-Invoice `CSWC-INV-26-0317` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-02 11:19 Thu | 13-Invoice `ST-INV-26-0323` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-02 11:55 Thu | 05-UtilityStatement `CSWC-DOC-26-0318` | MeterReading.PreviousMeterReading 2026-02-28; MeterReading.LatestMeterReading 2026-03-31 | 06 |
| 2026-04-02 13:20 Thu | 02-Invoice `FE-INV-26-0313` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-02 15:10 Thu | 08-UtilityStatement `CSWC-DOC-26-0320` | MeterReading.PreviousMeterReading 2026-02-28; MeterReading.LatestMeterReading 2026-03-31 | 09 |
| 2026-04-02 15:44 Thu | 09-Invoice `CSWC-INV-26-0319` | InvoicePeriod 2026-03-01–2026-03-31 |  |
| 2026-04-02 17:10 Thu | 03-UtilityStatement `FE-DOC-26-0315` | MeterReading.PreviousMeterReading 2026-02-28; MeterReading.LatestMeterReading 2026-03-31 | 02 |
| 2026-04-02 17:37 Thu | 12-UtilityStatement `ST-DOC-26-0324` |  | 13 |
| 2026-04-02 17:54 Thu | 01-UtilityStatement `FE-DOC-26-0314` | MeterReading.PreviousMeterReading 2026-02-28; MeterReading.LatestMeterReading 2026-03-31 | 02 |
| 2026-04-10 13:33 Fri | 04-RemittanceAdvice `VI-RM-26-0316` | InvoicePeriod 2026-03-01–2026-03-31 | 02 |
| 2026-04-19 11:40 Sun | 14-RemittanceAdvice `VI-RM-26-0316` | InvoicePeriod 2026-03-01–2026-03-31 | 13 |
| 2026-04-19 17:11 Sun | 07-RemittanceAdvice `VI-RM-26-0316` | InvoicePeriod 2026-03-01–2026-03-31 | 06 |
| 2026-05-01 14:29 Fri | 10-Reminder `CSWC-DOC-26-0321` | ReminderPeriod 2026-04-23–2026-05-01; ReminderPeriod 2026-04-23– | 09 |
| 2026-05-05 12:03 Tue | 11-CreditNote `CSWC-CN-26-0322` |  | 09 |

#### waste

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-03-23 09:28 Mon | 01-WasteNotification `VI-DOC-26-0204` |  |  |
| 2026-04-02 12:34 Thu | 02-WasteMovement `RR-DOC-26-0207` |  | 01 |
| 2026-04-04 12:44 Sat | 03-Invoice `RR-INV-26-0208` |  | 02 |

#### wood

| Issued | Document | Dated events and periods it carries | Refers to |
|---|---|---|---|
| 2026-02-16 10:00 Mon | 01-RequestForQuotation `VI-DOC-26-0625` | RequestedDeliveryPeriod 2026-03-02–2026-03-16 |  |
| 2026-02-19 11:34 Thu | 02-Quotation `MS-DOC-26-0626` | PromisedDeliveryPeriod 2026-03-02–2026-03-16 | 01 |
| 2026-02-22 14:40 Sun | 03-Order `VI-PO-26-0627` |  | 02 |
| 2026-02-23 16:19 Mon | 04-TransportExecutionPlanRequest `MS-TR-26-0628` | ServiceStartTimePeriod 2026-02-26–; ServiceEndTimePeriod –2026-03-01 |  |
| 2026-02-26 08:31 Thu | 06-DespatchAdvice `MS-DA-26-0633` | ItemInstance.Manufacture 2026-02-23 | 03 |
| 2026-02-26 08:56 Thu | 08-Invoice `MS-INV-26-0635` |  | 03 |
| 2026-02-26 09:25 Thu | 05-ExportCustomsDeclaration `MS-EX-26-0630` |  | 03 |
| 2026-02-27 11:05 Fri | 07-ImportCustomsDeclaration `VI-IM-26-0634` |  |  |
| 2026-03-08 16:20 Sun | 10-Order `BF-PO-26-0637` |  |  |
| 2026-03-09 09:54 Mon | 11-Invoice `MS-INV-26-0638` |  | 10 |
| 2026-03-26 14:22 Thu | 09-RemittanceAdvice `VI-RM-26-0636` |  | 08 |

## Findings

### timelines#F1 · High · The coordinates put the three countries inside 35 km, against distances and travel times of hours and days in seven flows
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`   (Port of Selanu, 40°1.20′ S 15°8.40′ W)
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cac:ShipToShipActivityRecord/cac:Location/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`   (Lumeport anchorage, 40°1.20′ S 15°12.60′ W)
- XPath: `cotton/14-CommonTransportationReport.xml:/CommonTransportationReport/cac:AuthorityParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`   (Port of Lumeport, the same position)
- XPath: `cotton/12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`   (Port of Selanu, the same position)
- XPath: `air/05-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `59.40`   (Lumeport airport, 39°59.40′ S 15°16.20′ W)
- XPath: `ore/01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `30.60`   (Serravona mine, Urvania, 39°54.00′ S 15°30.60′ W)
- XPath: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `7.80`   (Lisavu Cotton Farm, 39°58.80′ S 15°7.80′ W)
- XPath: `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`   (days, Lumeport → Selanu)
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:BallastWaterSummary/cac:ExchangeBallastWaterTransaction/cac:Location/cbc:Name` = `At sea, 120 nautical miles west of Selanu`
- XPath: `air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceTime` = `07:00:00`   (arrival `10:00:00`, flight KXL207 Lumeport → Selanu)
- XPath: `road/14-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `186`   (km loaded, Ferrano → Marrowdale)
- XPath: `retail/16-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`   (km loaded, Marrowdale → Lumeport store)
- Why: these are all the coordinates the 250 documents state (`locations.csv`, `parties.csv`; 35 rows, seven distinct positions). Great-circle distances recalculated (WGS 84 per `CoordinateSystemCode` 4326, mean earth radius 6371 km): Lumeport port – Selanu port 6.0 km (3.2 nm); Lumeport port – Lumeport airport 6.1 km; Lumeport airport – Selanu port 11.6 km; Lumeport port – Serravona mine (in Urvania) 28.8 km; Selanu port – Serravona mine 34.2 km, the largest span; Kelpstone plant – field 6.1 km. Every stated position of the three countries lies inside a box of 21 km × 32 km. Against that, the documents of five flows state distances and durations of another scale: two days at sea and a ballast exchange 120 nm west of Selanu (sea), a three-hour freighter flight between Lumeport and Selanu (air; an ATR 72 cruises at about 500 km/h, own knowledge, so about 1500 km of flight for 12 km), 186 km by road from Ferrano to Marrowdale and 38 km from Marrowdale to Lumeport (road, retail), while the Urvanian mine is 29 km from Lumeport. The per-example reviews found the Lumeport–Selanu part inside single documents (sea/08#F3, sea/16#F2) and left the rest outside; the cross-flow count shows that every coordinate in the world is on the same small scale, and every stated distance or travel time on a scale ten to a hundred times larger. Directions agree with the coordinates (Lumeport lies west of Selanu: sea `EB`, cotton `WB`), so only the scale is wrong.
- Condition: the stated coordinates, the stated distances (`InvoicedQuantity` in KMT, nautical miles in location names, "four kilometres" in energy) and the stated durations (sea service duration, flight times, voyage events) agree within a plausible speed for each mode; checkable by recomputing the distances above.
- Options: (a) preferred: scale the coordinates up (the minutes of arc look like a map grid read as degrees; multiplying the offsets from a reference point by about ten to twenty would give Lumeport–Selanu 60–120 km, a one-night feeder crossing and a short flight), because the distances in road/retail/sea and the durations are spread over many documents and consistent with each other; (b) keep the coordinates and shrink the stated distances and durations to a world of 30 km (then the sea voyage, the flight and the 186 km road trip all change); (c) drop the coordinates where no document needs them (party physical locations) and keep only those of ports and airports, scaled as in (a).
- Needs decision: yes
- Seen in reviews: sea/08#F3, sea/16#F1, sea/16#F2, sea/16#F3, energy/04#F8 (and energy/05#F8, 06#F5, 07#F8: "four kilometres" vs 6.1 km); merge decision "Lumeport and Selanu 3.2 nm apart"; leads of air/04, cotton/14, sea/13, sea/15, sea/16, retail/15, retail/16, road/14

### timelines#F2 · High · One melt of steel is cast on 20 March, 10 May and 11 May, and the castings' serial numbers run against their manufacture dates
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cac:AdditionalItemProperty/cbc:Value` = `M-26-0412`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-03-20`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01490`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cac:AdditionalItemProperty/cbc:Value` = `M-26-0412`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230`
- XPath: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cac:AdditionalItemProperty/cbc:Value` = `M-26-0412`
- XPath: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `air/08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`
- XPath: `air/08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- Why: a melt number identifies one heat of steel poured at one time (own knowledge of foundry practice). All 40 melt numbers in the 250 examples are `M-26-0412` (counted with `grep -h -A1 'Melt number' */*.xml`): 12 castings made 2026-03-20 06:40 (road/04), 12 made 2026-05-10 06:40 (sea/20), 8 made 2026-05-10 06:40 (air/06) and the same 8 again made 2026-05-11 06:40 (air/08; the one-day difference is air/06#F3 and air/08#F4). Castings of one melt cannot be made seven weeks apart. The serial numbers do not follow time either: the castings made on 10 May carry `VI-SF-01230`…`01241` (sea) and `VI-SF-03190`…`03197` (air), the ones made on 20 March `VI-SF-01490`…`01501` (road), and the frame of a bench of the lot made 26 April `VI-SF-02170` (retail/21). The same pattern, one fixed manufacture time 06:40 for every casting, and one coating batch `ZN-26-114` for bench lots made on 20 March, 27 March, 26 April and 10 May (road/04, tender/29, retail/12, sea/20), point to a single set of production data reused for every lot; that shows only across flows.
- Condition: castings made on different days carry different melt numbers; within one manufacturer's serial series, a later manufacture date has a higher serial number, or the series is stated to be non-chronological; the coating batch of a bench lot is one that can exist on that lot's manufacture date.
- Options: (a) preferred: one melt (and one coating batch) per production day or lot, with serials ascending with the date, because the documents use melt and serial as traceability data, which only works if they identify one production event; (b) keep one melt and give all castings one manufacture date (then the lots of F4 below become one production run, which the sea and air stories do not allow).
- Needs decision: no
- Seen in reviews: air/06#F3, air/08#F4 (the one-day difference only); leads of air/06, air/08 (manufacture dates)

### timelines#F3 · High · Documents report as done what happens after their issue time, or cite documents not yet issued, in ten flows; the moment a transport document is issued differs by mode
- XPath: `road/08-Waybill.xml:/Waybill/cbc:IssueTime` = `08:16:00`
- XPath: `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`   (issued `15:15:00`)
- XPath: `plastics/06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`   (issued `09:38:00`)
- XPath: `rail/05-TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportSchedule/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `06:52:00`   (issued `06:45:00`)
- XPath: `rail/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`   (issued `13:10:00`)
- XPath: `rail/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`   (rail/06, issued `17:29:00`)
- XPath: `sea/13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`   (issued `16:05:00`)
- XPath: `air/05-TransportationStatus.xml:/TransportationStatus/cac:DocumentReference/cbc:ID` = `KXL-WB-26-0325`   (air/04, issued `10:43:00`; this report `10:05:00`)
- XPath: `sea/24-InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:Payment/cbc:PaidDate` = `2026-06-25`   (issued 2026-05-30)
- XPath: `sea/28-DebitNote.xml:/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`   (sea/25, issued 2026-06-13; this note 2026-05-22)
- Why: counted mechanically over all 250 examples (an actual pickup, loading, departure, waypoint, delivery, despatch, signature or payment dated after the document's own issue time; an estimate or plan dated before it; a reference to an example issued later), from `dates.csv` and `references.csv`, then checked in the XML, leaving out planned events in plans and bookings (plastics/04, sea/08, sea/14's expected on-carriage events, sea/16's planned ballast discharge) and events marked `CompletionIndicator` false (rail/07, rail/08's delivery, plastics/06's discharge): 10 events in 8 documents (road/04, road/08 three, plastics/06, rail/05, rail/08, sea/13, sea/24, cotton/02), 4 stale estimates or plans in 2 documents (rail/08, sea/15), and 9 citations of later documents (air/05 → air/04, energy/01 → energy/02, rail/08 → rail/06, road/14 → road/13, sea/24 → sea/27, sea/28 → sea/25, tender/17 and tender/19 → tender/13, utilities/08 → utilities/09; sea/23 has no issue date to compare), besides the revision times after the issue time in retail/03 and retail/04. Each was found by its own per-example review and rated High under the merge decision "Dates, events or references after the document's own issue time". The cross-flow view adds two things. First, a world-wide pattern: the same error in ten flows (air, cotton, energy, plastics, rail, retail, road, sea, tender, utilities), so one rule for "when is a document issued relative to what it reports" fixes them together. Second, the flows do not agree on when the transport document is made out: the road and barge waybills are issued before the carrier takes over the goods (road/08 at 08:16 for a 15:05 pickup; plastics/06 at 09:38 for a 09:00 takeover and 13:30 loading), the rail waybill six hours after departure (rail/08 13:10 for 06:52), the air waybill 38 minutes after the terminal accepted the cargo (air/04 10:43, air/05 10:05), and the shipped-on-board bill of lading before loading (sea/14 10:54, loading reported by sea/13 on the same day, departure 18:10); in cotton the bill is issued 2026-03-02 09:37 with no on-board date at all (cotton/13#F2). A consignment note or bill of lading is normally made out when the carrier takes over the goods, a shipped-on-board bill after loading (own knowledge of CMR, CIM, Montreal and Hague-Visby practice).
- Condition: no document reports as actual, or cites as existing, anything dated after its own issue time; in every flow the transport document is issued at the moment its type implies (takeover for waybills, loading on board for a shipped-on-board bill), or states that it is a booking or a planned schedule.
- Options: (a) preferred: move the issue times of the transport documents to just after takeover (road/08 after 15:05, plastics/06 after 13:30, rail/08 before the transit declaration is needed, sea/14 after loading) and the referencing documents after the referenced ones, because the events themselves are consistent across the documents of each flow; (b) keep the issue times and turn the future events into planned or estimated ones (where the document type allows).
- Needs decision: no
- Seen in reviews: cotton/02#F1, road/04#F1, road/08#F1, road/08#F3, road/14#F1, plastics/06#F1, rail/05#F1, rail/08#F3, rail/08#F5, air/05#F1, energy/01#F5, sea/13#F1, sea/24#F1, sea/28#F3, tender/17#F2, tender/19#F2, utilities/08#F8, retail/03#F1, retail/04#F1, retail/09#F1, retail/10#F1; merge decision row; leads of air/04, air/05, air/06, rail/06, rail/08, road/04, road/13, sea/13, sea/14, sea/25, utilities/09

### timelines#F4 · Medium · Goods "from the distributor's stock" in Bayvarra are made in Urvania two or three days before they leave, and no document moves them; the documented deliveries carry other lots
- XPath: `retail/12-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-04-26`
- XPath: `retail/12-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260510`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Status/cbc:Description` = `Waiting at the distributor's dispatch area.`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260320`
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:DeliveredQuantity` = `96`
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:DeliveredQuantity` = `96`
- XPath: `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `192`
- Why: three lots are sold by Lumeway from its Marrowdale stock (Bayvarra) days after Valdara made them in Urvania: retail lot `VI-LOT-260426` made Sunday 2026-04-26, despatched 2026-04-29 (three days); sea lot `VI-LOT-260510` and castings `VI-SF-01230`… made 2026-05-10, packed by 2026-05-12 (packing list) and despatched 2026-05-13; air castings made 2026-05-10 or 05-11, "waiting at the distributor's dispatch area" on 2026-05-12. The documents move Valdara goods to Lumeway only twice: the road flow (lot `VI-LOT-260320`, 96 benches + 12 castings, delivered 2026-03-25) and the rail flow (192 benches, delivered 2026-04-15, no lot stated). Both deliveries end before the three lots were made, so the lots reached Marrowdale in a transfer no document shows, and in two or three days including a border crossing; the road flow needed nearly two days for the same relation (pickup 2026-03-23 15:05 → delivery 2026-03-25 09:40). The sea shipment also repeats the road shipment figure for figure (96 benches + 12 castings, 4106.4 kg gross, 3762 kg net, 25 pallets: road/08, sea/10), which reads as the March delivery shipped on; its lot number and manufacture date say it is not. The per-example reviews flagged the short interval in single examples (sea/20#F16) and left the cross-flow part outside.
- Condition: every lot that Lumeway despatches from its stock was made before a documented delivery to Lumeway that could have carried it (lot or manufacture date matching that delivery), or the documents say how it reached Lumeway (another delivery, or "direct from the manufacturer").
- Options: (a) preferred: give the retail, sea and air goods lots and manufacture dates of the deliveries that exist (the sea shipment `VI-LOT-260320` and castings `VI-SF-01490`…, which the identical figures already suggest; the retail and air goods a lot of the rail delivery or the road delivery), because it keeps every flow's dates and only changes product data; (b) keep the lots and add a statement of direct supply from Valdara (then "from the distributor's stock" must go, and the transport to Marrowdale is still missing); (c) add a transfer flow.
- Needs decision: yes
- Seen in reviews: sea/20#F16; air/06#F3; leads of air/03, air/06, air/08, retail/12, sea/20

### timelines#F5 · Medium · The crossing Lumeport → Selanu takes two days, 64 hours or 84 hours, depending on the document
- XPath: `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`
- XPath: `sea/08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`   (2026-05-14)
- XPath: `sea/13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`   (2026-05-14)
- XPath: `sea/15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`   (06:00, issued 2026-05-15 16:08)
- XPath: `sea/15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`   (2026-05-17)
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:ReportingLocation/cbc:Name` = `At sea, 40 nautical miles off Selanu`   (issued 2026-05-16 15:38)
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cac:VesselDynamics/cbc:SpeedOverGroundMeasure` = `13.5`
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:DestinationPortCall/cac:RequestedArrivalEvent/cbc:OccurrenceTime` = `06:00:00`   (2026-05-18)
- XPath: `sea/17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime` = `06:30:00`   (2026-05-18)
- Why: the same voyage `TH-26-19E` of `Tidewell Harbour` is given four durations: two days announced for the service (sea/08); 64 hours estimated by the carrier's manifest a day after the port reported the actual departure (15 May 06:00 → 17 May 22:00; the stale estimate itself is sea/15#F1); 84 h 20 min actual (14 May 18:10 → 18 May 06:30, sea/13 and sea/17); and a position 40 nm off Selanu at 13.5 knots on 16 May 15:38, which would put the ship in port about three hours later, on 16 May, not on 18 May (sea/16#F1). No document gives a reason for the extra day and a half (weather, a call at another port, waiting for a berth). The return direction cannot be compared: the cotton voyage `TR-26-09W` Selanu → Lumeport by the same carrier states no loading, departure or arrival time (cotton/13#F2, cotton/14#F1); its bill of lading (2026-03-02 09:37) and pre-arrival report (2026-03-03 11:22) only bound it to about a day. Whatever scale F1 settles on, the documents of this one voyage must agree with each other.
- Condition: the service duration, the manifest's estimate, the report's position and speed, and the actual departure and arrival of voyage `TH-26-19E` describe one passage time, or a stated event explains the difference.
- Options: (a) preferred: settle the passage time with F1 (for example one night, as for a feeder) and derive the estimate, the reporting position and the arrival from it; (b) keep 84 hours and state the delay (a waypoint, weather) in the pre-arrival report and the status.
- Needs decision: yes
- Seen in reviews: sea/08#F3, sea/15#F1, sea/16#F1, sea/16#F17; leads of sea/08, sea/15, sea/16

### timelines#F6 · Low · Two flows lodge the export declaration after the goods have left, five lodge it before; both say "before the goods leave"
- XPath: `plastics/06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Despatch/cbc:ActualDespatchTime` = `15:10:00`   (2026-04-19)
- XPath: `plastics/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:IssueTime` = `16:08:00`   (2026-04-19)
- XPath: `plastics/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:Note[2]` = `Declared electronically before the goods leave.`
- XPath: `wood/06-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `08:31:00`   (2026-02-26)
- XPath: `wood/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:IssueTime` = `09:25:00`   (2026-02-26)
- XPath: `wood/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:Note` = `Declared electronically before the goods leave.`
- XPath: `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:IssueTime` = `13:25:00`   (2026-03-23, pickup 15:05)
- Why: in road (declared 13:25, pickup 15:05), tender (13:40, despatch advice 17:37), sea (2026-05-12, drop-off at the port 2026-05-13), cotton (2026-03-01, bill of lading 2026-03-02) and rail (transit declaration, see F3) the exporter declares before the goods leave its premises; in plastics the barge left the quay at 15:10 and the declaration follows at 16:08, in wood the despatch advice (08:31) precedes the declaration (09:25). "Before the goods leave" can be read as "before they leave the country" (the barge exits on 2026-04-20 16:00), which is why plastics/05 and the context part refuted it inside one example; across the flows it shows that the world has no single moment for export declarations. In practice the declaration is lodged and the goods released for export before they are moved from the place of loading (own knowledge, e.g. EU UCC art. 263/267).
- Condition: in every flow the export declaration is issued before the despatch or takeover the other documents record, or the flows that declare later state why (a simplified procedure, declaration at the border).
- Options: (a) preferred: move the issue times of plastics/05 and wood/05 before the despatch; (b) state a world rule that declarations may be lodged until the goods reach the exit office.
- Needs decision: no
- Seen in reviews: plastics/05 ("Considered and refuted"); leads of plastics/05, wood/05, wood/06

### timelines#F7 · Low · Sea flow: the goods are promised by 18 May, expected at the warehouse on 19 May, and received on 21 May, with nothing for 19–21 May
- XPath: `sea/06-OrderResponse.xml:/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-05-18`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:AvailabilityTransportEvent/cbc:OccurrenceTime` = `14:00:00`   (2026-05-18)
- XPath: `sea/17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:OccurrenceTime` = `15:00:00`   (2026-05-18)
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:ReceiptTransportEvent/cbc:OccurrenceDate` = `2026-05-19`
- XPath: `sea/21-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedDate` = `2026-05-21`
- XPath: `sea/28-DebitNote.xml:/DebitNote/cac:InvoicePeriod/cbc:EndDate` = `2026-05-19`
- Why: under CIF Selanu the seller's promise ends with the loading in Lumeport (2026-05-14), so the promised period of sea/06 is met by the loading; the later dates belong to the buyer's side. Across the sea documents the container is to be available on 18 May 14:00 (sea/14), is released after the pallet-mark check at 15:00 (sea/17), stays a day in port storage (sea/28's period 18–19 May), and the goods are to be received at Nalevi's warehouse on 19 May (sea/14) but are received on 21 May (sea/21, sea/26, sea/28 `ActualDeliveryDate`). Each date is plausible alone; together they leave two days in which no document places the container, and the import declaration is lodged on 19 May 09:07. Low because a short wait for on-carriage is ordinary; the owner may want the on-carriage leg dated.
- Condition: the on-carriage from the Port of Selanu to Nalevi's warehouse has a date in some document that fits both the release on 18 May and the receipt on 21 May, or the receipt is dated 19 May.
- Options: (a) preferred: give the bill of lading's on-carriage receipt event the date of the actual receipt or add an on-carriage date in the receipt advice; (b) move the receipt to 19 May (then the credit and debit notes follow).
- Needs decision: no
- Seen in reviews: none as findings; leads of sea/06, sea/17, sea/21

### timelines#F8 · Low · The retailer's gas bill cites the grid operator's metering report four hours before that report is issued
- XPath: `utilities/02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:Note` = `1,350 m³ at 4 bar, converted to 61,200 kWh by the grid operator's metering report.`
- XPath: `utilities/02-Invoice.xml:/Invoice/cbc:IssueTime` = `13:20:00`   (2026-04-02)
- XPath: `energy/01-UtilityStatement.xml:/UtilityStatement/cbc:IssueTime` = `17:42:00`   (2026-04-02)
- Why: energy/01 is Ferrano Grid's metering statement for meter `FG-G-20417` (March, 1350 m³ → 61200 kWh); utilities/02, Ferrano Energy's invoice to Valdara, bills exactly that conversion and says it comes from the grid operator's metering report, but is issued 4 h 22 min earlier. The figures agree (recalculated in energy/01's review); only the order does not. A meter reading can reach the retailer before the statement document, so this is a plausibility remark.
- Condition: utilities/02 is issued after energy/01, or its note refers to the reading (or a document that exists at 13:20) rather than to the report.
- Options: (a) preferred: issue energy/01 before utilities/02 (the grid operator's statement naturally comes first); (b) reword the note.
- Needs decision: no
- Seen in reviews: energy/01#F5 (the statement before its own parent invoice); lead of energy/01

## Checked and consistent

- Production before shipment across flows, where lots are stated: wood slats made 2026-02-23 and delivered to Valdara 2026-02-27, before the bench lot of 2026-03-20; ore despatched 2026-03-10 before the castings of 2026-03-20 (whether that ore is in them cannot be told); the road lot `VI-LOT-260320` made three days before its despatch from Castrano on 2026-03-23; the tender lot `VI-LOT-260327` made after the colour change of 2026-03-24 (tender/27) asked for moss green and three days before its despatch on 2026-03-30. The exceptions are F2 and F4.
- Contract before call-off: the tender contract (tender/24, 2026-03-19) and its validity from 2026-03-23 precede the first release order (tender/26, 2026-03-23 14:40); the catalogue under the contract (tender/25, 2026-03-21) precedes the order; the award (2026-03-09 09:30) precedes the notifications (10:15, 13:37) and the contract; tenders (2026-02-23 to 02-25) precede the deadline 2026-02-26 12:00 and the opening at 14:00; the register extract (tender/12, 2026-02-27) comes after the opening, so the register can know the tenderers. The guarantee certificate (tender/14, 2026-02-24, applicable from 2026-02-21) lies within the constitution period ending 2026-02-26.
- Order before order response before despatch, invoice before reminder before payment: checked in every flow with `documents.csv` and the references; the exceptions are the per-example findings listed in F3 and the remittance timing of the freight invoices (flow composition, other topic).
- Contest flow: every period (`ParticipationRequestReceptionPeriod` 2026-04-18 and 2026-05-02, `TenderSubmissionDeadlinePeriod` 2026-06-12 12:00) ends after the notice that announces it; the second notices and their follow-ups (contest/02, 08–12) are issued after the first ones.
- Meter readings: every meter appears in one statement only, for 2026-02-28 → 2026-03-31, and every delivered quantity is latest minus previous reading (× the meter constant 40 for `FE-M-881204`: (63280 − 52960) × 40 = 412800 kWh); the same quantities are billed in energy/02 and utilities/02 after the reading period ends.
- Energy month: the March pipeline declarations (energy/04, 05, issued 2026-04-02) and invoices (energy/06, 07, 03, issued 2026-04-03) follow the month they declare and bill.
- Directions of the two voyages agree with the coordinates (Lumeport west of Selanu): `EB` for Lumeport → Selanu (sea/14, 15, 16), `WB` for Selanu → Lumeport (cotton/14).
- Road leg Ferrano → Marrowdale (road): export declaration 13:25 before the pickup at 15:05; border passed 2026-03-24 07:30–08:55, seal check 07:45 inside that window; delivery 2026-03-25 09:40 inside the requested slot (10:00, road/03) and the estimated period 09:00–11:00 (road/08); the rest night in Marrowdale (road/09) follows from the slot, not from driving time.
- Rail leg (rail): pickup at Castrano 2026-04-13 15:00, handling at the hub 18:30, loading 2026-04-14 05:40, departure 06:52, border waypoint 13:20 (planned 13:00), delivery 2026-04-15 11:00 (planned arrival 10:30, estimated 10:40): one consistent sequence across rail/03, 05, 07, 08 apart from the issue times of F3.
- Barge leg (plastics): takeover 2026-04-19 09:00, loading 13:30, despatch 15:10, exit 2026-04-20 16:00, discharge 2026-04-22 08:00 against an estimated transit of 3 days (plastics/04, 06): consistent.
- Air leg: requested departure 2026-05-14 07:00, arrival 10:00 (air/04); the "morning flight" of air/02 fits it. The missed flight against the same-day arrival is air/07#F2 and air/09#F2.
- Sea flow interval checks: VGM weighed 2026-05-12 15:30 before the container's drop-off at Lumeport 2026-05-13 10:15 and acceptance 10:15; storage from 10:30; bunkering 2026-05-13 05:40–08:15 during the port call 05-13 to 05-14 (sea/16) before the departure 18:10.

## Considered and refuted

- Transport bookings before the seller confirms the order (plastics/03 09:57 before plastics/02 15:39; road/03 14:16 before road/02 17:42): refuted; booking capacity before or while the order is confirmed is normal practice and both flows run under framework contracts (plastics/04, road/03 cite them).
- Catalogue (sea/02 09:17) before the business card (sea/01 16:39) on the same day: refuted; no document makes one depend on the other.
- Forwarding instructions (sea/09, sea/12) before the packing list and the export declaration (2026-05-12), and the export declaration (14:25) before the packing list (15:59): refuted; instructions and a declaration rest on the order and the planned load, the packing list confirms the packed load; the numbering of their IDs is the identifiers topic.
- Contest: version 2 of the tenderer qualification (contest/12, 09:52) before version 2 of the response (contest/11, 14:18): refuted; neither cites the other's version 2.
- rail/07 issued at 13:11 reports the loading of 05:40: refuted; a status report may report an earlier event late. Its delivery and optional-takeover events after the issue time carry `CompletionIndicator` false, so they are planned, not actual.
- road/03 requested pickup 14:00, actual 15:05 (road/08, road/09): refuted; road/09 records the change as an updated pickup.
- road/10 import declaration (2026-03-24 09:54) before the commercial invoice road/15 (11:41): refuted as a timeline contradiction; road/10 cites the despatch advice and the certificates of origin, not the invoice, so it does not rest on a document that does not yet exist. The valuation basis is conditions#F5.
- Wood: despatch on 2026-02-26 in Marrowdale and import clearance in Urvania on 2026-02-27 11:05: refuted; about a day for a cross-border road leg that the road flow covers in 17 h to the border.
- Utilities: the credit note of 2026-05-05 (utilities/11) after the reminder of 2026-05-01 (utilities/10): refuted as a timeline problem; a credit after a reminder is possible; whether the reminded amount should change is money.
- Tender: a bench given a position (B17) in the park two days after delivery (tender/33): refuted as a timeline problem; delivery on 2026-03-31 and anchoring from 2026-04-02 (tender/33's line period) leave time for it.
- Cotton: classing certificate signed 2026-02-20 cited in the forecast of 2026-02-02: a single-example contradiction already established (cotton/02#F1, cotton/10#F8); the other cotton documents cite it after 2026-02-20, so nothing cross-flow is added.
- Pallet or vehicle movements of Trasvia Haulage at the same time in several flows (road 2026-03-23/25, wood 2026-02-26, tender 2026-03-30/31, waste around 2026-04-02): refuted at company level, the dates do not overlap; vehicles are named only in road (see the equipment review).

## Leads from the per-example reviews

All 221 "Outside this review" entries of the 250 merged files were extracted and read (numbered in file order). Entries on this topic:

| Source (entry) | Entry in short | Outcome |
|---|---|---|
| air/02 (2) | which "morning flight" | refuted: the flight of air/04 fits; the missed flight is air/07#F2, air/09#F2 |
| air/03 (3), air/06 (9), air/08 (11) | castings made in Urvania on 10/11 May, ready in Marrowdale on 12 May | F4; the melt and date part F2 |
| air/04 (4), air/05 (7), air/06 (8) | terminal accepts the cargo before the waybill and two minutes before the shipper's despatch advice | F3 |
| air/04 (5) | three-hour ATR 72 flight against the map | F1 |
| air/04 (6), air/08 (10), air/10 (13) | "new despatch advice follows today"; offloaded but arrived the same day | per-example (air/07#F1, F2; air/08#F1; air/09#F2); nothing cross-flow added |
| carnet/01 (15), carnet/04 (17) | re-export and re-import against the fair and the transport legs | cannot be told |
| contest/12 (29) | qualification v2 before response v2 | refuted |
| cotton/10 (35) | certificate signed after the forecast cites it | refuted as cross-flow (cotton/02#F1) |
| cotton/13 (39), cotton/14 (40, 42) | voyage dates, map, 6 km between the ports | F1; voyage time F5 (cannot be told for cotton); vessel position: equipment file |
| energy/01 (44) | retailer bills before the metering statement | F8 |
| energy/04 (48) | pipeline timeline against the declaration date | checked: monthly declaration after the month (consistent); volumes: equipment file |
| furniture/09 (53), furniture/10 (54) | when the 20 sets reached the store; what the store knew on 16 April | cannot be told |
| furniture/16 (57), furniture/17 (58) | invoice at 10:10 on the last day of the work | cannot be told |
| mast/03 (60, 61) | whether flight KXL209 runs that day; on-carriage under CPT | cannot be told (no flight date: mast/03#F5); capacity part: equipment file |
| ore/05 (64), ore/06 (66) | train arrival never recorded; bonus or penalty | cannot be told (ore/06's own finding) |
| packaging/01 (69) | Trasvia's road leg Lumeport → Ferrano fits the dates | cannot be told: no transport document in the flow |
| plastics/02 (71), plastics/03 (72) | barge requested before the order is accepted | refuted |
| plastics/05 (73), wood/05 (216), wood/06 (217) | declared "before the goods leave" after the despatch | F6 |
| rail/06 (75), rail/08 (77) | transit declared after departure; waybill after collection and departure | F3 |
| rail/07 (76) | report of loading issued after departure | refuted |
| retail/12 (81) | lot made on Sunday 26 April, despatched from stock on 29 April | F4 (weekend: conditions#F7) |
| retail/15 (83), retail/16 (84) | 38 km Marrowdale → store on the map | F1; the delivery day itself is retail/15, retail/17#F4 (merge decision, Medium/yes) |
| retail/20 (88) | catalogue revision times against issue times | per-example (retail/03#F1, F2; retail/04#F1); part of F3's pattern |
| road/02 (91), road/03 (94) | truck booked before the order response | refuted |
| road/03 (93) | pickup one hour late | refuted |
| road/04 (95) | waybill 08:16 reports the 15:05 pickup | F3 |
| road/04 (96) | pickup → departure, export release in between | checked and consistent |
| road/08 (102), road/09 (103), road/14 (107) | 186 km, border next morning, rest in Marrowdale, map | F1 (scale); the sequence: checked and consistent; driving-time rules: cannot be told |
| road/10 (104) | import declaration before the invoice | refuted |
| road/13 (105) | invoice cites a later receipt advice | F3 (road/14#F1) |
| sea/02 (111) | catalogue before business card | refuted |
| sea/06 (113), sea/17 (130), sea/21 (134) | promised by 18 May, available 14:00, received 21 May | F7 |
| sea/08 (114), sea/12 (119) | weekend issue against weekday SLA and hours; booking after the nomination deadline | conditions#F7 (weekend, not redone); deadline: sea/08#F1 |
| sea/08 (115), sea/16 (127) | manifest estimate after the actual departure | F5 (sea/15#F1) |
| sea/09 (116), sea/10 (117), sea/11 (118), sea/12 (120) | instructions and declaration before the packing list | refuted; numbering: other topic |
| sea/13 (121), sea/15 (125), sea/16 (126) | map scale: 3.2 nm against days at sea | F1 |
| sea/13 (122), sea/14 (123) | shipped-on-board bill before loading | F3 |
| sea/15 (124) | 3.5 days against "two days at sea" | F5 |
| sea/20 (132) | made 10 May, moved and packed by 12 May | F4 |
| sea/25 (136) | debit note cites a later statement | F3 (sea/28#F3) |
| tender/02 (140), tender/03 (143) | notice one day before the call, 14–15 days before the deadline | cannot be told: no document states a minimum period |
| tender/02 (141), tender/09 (151), tender/21 (170) | periods ending before the notices; requests after the reception period | per-example (tender/02#F1, 03#F1, 21#F2, 04#F4, 05#F4); nothing cross-flow added (the contest flow keeps its periods) |
| tender/06 (149) | request 13 Feb, answer 19 Feb, tender 23 Feb | checked and consistent |
| tender/07 (150) | tenders cite Valdara's later qualification | F3 (tender/17#F2, 19#F2) |
| tender/12 (153) | register knows the tenderers on 27 Feb | checked and consistent (after the opening) |
| tender/17 (163) | tender withdrawn after the corrected tender | per-example (tender/18#F1, 19#F1) |
| tender/32 (189), tender/33 (190), tender/34 (192), tender/35 (193) | invoice before installation; position B17; installers' days; acceptance | invoice: per-example (tender/32#F2, 34#F2); B17: refuted; installers' days and acceptance: cannot be told |
| utilities/09 (202) | statement before the invoice it supplements | F3 (utilities/08#F8) |
| utilities/10 (203), utilities/11 (204) | credit note after the reminder | refuted |
| waste/01 (205), waste/02 (209) | movement ten days after the notification | cannot be told |
| wood/04 (215), wood/06 (218), wood/07 (219) | despatch 26 Feb, cleared 27 Feb 11:05 | refuted |

Entries on the other topic of this run (equipment, capacity, places): 14, 36, 37, 39 (vessel), 42 (vessel position), 45, 47, 48 (volumes), 49–52, 59, 60 (capacity), 62, 63, 74, 89, 131, 133, 180, 182, 184, 185, 188, 206, 208, 210, 212, 213, 214; see the equipment review. All other entries (1, 12, 16, 18–28, 30–34, 38, 41, 43, 46, 55, 56, 65, 67, 68, 70, 78–80, 82, 85–87, 90, 92, 97–101, 106, 108–110, 112, 128, 129, 135, 137–139, 142, 144–148, 152, 154–162, 164–169, 171–179, 181, 183, 186, 187, 191, 194–201, 207, 211, 220, 221) are about parties, items, identifiers, money, customs rules or the composition of a flow, or are already a per-example finding of the named example; not this topic.

## Cannot be told from the documents

1. What is the real scale of the map: how far apart are Lumeport, Selanu, Marrowdale and Ferrano, and how long does each mode take between them? (F1, F5)
2. How did the lots `VI-LOT-260426`, `VI-LOT-260510` and the castings `VI-SF-03190`… reach Lumeway's stock in Marrowdale, and when? (F4)
3. When did the ore train arrive at Valdara (ore/05, ore/06), so that the bonus or penalty of ore/03 can be decided?
4. When did Saltmere's flight KXL209 (mast/03) leave and arrive, and who carried the goods from Selanu airport to the mast site?
5. When did the carnet samples leave Lisavu and come back to Urvania (carnet/04 refers only to "the date stamped"), and when was the Selanu fair?
6. When were the 20 sets of furniture/08 delivered to the store, and when did the installers of furniture/16 finish on 9 April (the invoice is issued at 10:10 that day)?
7. On which days did Saltmere install the benches of tender release 1, when was the release accepted, and from which date are the three days of tender/34's penalty counted?
8. How long does the authority take to consent to a waste movement (waste/01 2026-03-23 → waste/02 2026-04-02), and what are the "driving-time rules" of road/09?
9. Is there a minimum period between a contract notice and the tender deadline in Bayvarra (tender/02, 03: 15 and 14 days)?
10. When did the cotton container leave Selanu and arrive in Lumeport (no event in cotton/13, 14)?
11. When did Trasvia carry the packaging goods (packaging/01) and the waste (waste/02), and with which vehicles?

## For other topics

- Identifiers: the castings' serial numbers (`VI-SF-…`) are not in manufacture order across flows (F2); the journey IDs `TR-26-09W` (cotton, 2026-03-02, ISO week 10) and `TH-26-19E` (sea, 2026-05-14, ISO week 20) look like week numbers one off.
- Items: one coating batch `ZN-26-114` for bench lots of 20 March to 10 May (road/04, tender/29, retail/12, sea/20).
- Conditions: weekend issue dates (conditions#F7) include sea/08, sea/12, retail/12's manufacture day and the plastics waybill and declaration of Sunday 2026-04-19.
- Flow composition: no transfer of goods to Lumeway after 2026-04-15 (F4); no on-carriage document in mast and sea after the port.
