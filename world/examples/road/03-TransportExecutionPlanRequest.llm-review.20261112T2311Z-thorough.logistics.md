# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/03-TransportExecutionPlanRequest.xml`, Git blob `fe5bfa14052d31ed395823661598b379931d78e9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### road/03#F1 · Low · Number and size of the handling units only in free text
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `Park benches and spare side frames on 25 pallets.`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `4106.4`
- Why: A transport request has to tell the carrier what to plan for. The weight is structured, but the 25 pallets appear only in the summary text, and nothing says that 24 of them are non-standard 1850 × 650 mm bench pallets 1650 mm high that must be stacked two high to fit (as the waybill later shows, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`). The loading length or the number of handling units is what a carrier uses to check that an FTL booking works; here it cannot be checked from the request.
- Condition: the request carries the number of handling units as a structured value (e.g. Consignment/TotalTransportHandlingUnitQuantity = 25) and, where the units are non-standard, their dimensions or the loading length.
- Options: (a) preferred: add TotalTransportHandlingUnitQuantity and LoadingLengthMeasure (the values the waybill gives); (b) add TransportHandlingUnit aggregates with type and dimensions.
- Needs decision: no

### road/03#F2 · Low · From and to locations named after companies, without identifiers
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Lumeway Distribution`
- Why: Location Name is the name of the place, not of the company at it. The same places carry identifiers elsewhere in this very document (`/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cac:Location/cbc:ID` = `XUFER`, `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cac:Location/cbc:ID` = `XBMRW`), and the consignee has a GLN (9520610900008) that could identify its delivery site.
- Condition: FromLocation and ToLocation are named as places (e.g. "Castrano warehouse, Ferrano") and carry the place identifiers used for the same places in the request.
- Options: (a) preferred: name the sites and add the UN/LOCODEs (and the GLN for the Marrowdale site if it identifies it); (b) keep the names but add the identifiers.
- Needs decision: no

## Checked and consistent
- Consignment ID LD-CS-26-0152 and gross weight 4106.4 kg are the same in `04-DespatchAdvice.xml`, `05-ExportCustomsDeclaration.xml` and `08-Waybill.xml`; 4106.4 = 3984 (benches) + 122.4 (side frames) as itemised in `05-ExportCustomsDeclaration.xml`.
- Requested pickup 2026-03-23 14:00 matches the order; the actual pickup (15:05) and delivery (2026-03-25 09:40, `11-ReceiptAdvice.xml`) fall within ServiceStartTimePeriod (from 2026-03-23) and ServiceEndTimePeriod (to 2026-03-26); requested delivery 2026-03-25 10:00 equals the waybill's required delivery.
- FTL and a curtain-side trailer loaded from the side by forklift fit 25 pallets of 4.1 t; the response deadline 2026-03-18 lies after the issue date.
- ContainerizedIndicator false / GeneralCargoIndicator true fit palletised benches on a trailer.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode`: FTL booked for a load that the waybill says needs 9.3 m of a 13.6 m trailer — refuted because a full truck load is a booking of the whole vehicle, which is legitimate for a 4.1 t cross-border load that must stay sealed; it does not claim the trailer is full.
