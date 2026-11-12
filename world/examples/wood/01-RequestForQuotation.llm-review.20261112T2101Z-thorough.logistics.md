# LLM review: 01-RequestForQuotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/01-RequestForQuotation.xml`, Git blob `c0a83fe4f0fa1f96f25fae6aedf8f2a7b3fb0857` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

## Checked and consistent
- Dates: `/RequestForQuotation/cbc:IssueDate` = `2026-02-16`, `/RequestForQuotation/cbc:SubmissionDueDate` = `2026-02-21`; the quotation answers on `02-Quotation.xml:/Quotation/cbc:IssueDate` = `2026-02-19`, before the due date. The requested validity `/RequestForQuotation/cac:RequestedValidityPeriod/cbc:DurationMeasure` = `30` matches the quotation's `02-Quotation.xml:/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21` (19 February + 30 days in a 28-day February = 21 March).
- Requested delivery window `/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02` to `/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-03-16` is the window the quotation promises (`02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`). Whether the transport later keeps to it is a finding of `04-TransportExecutionPlanRequest.xml` (its review, this run).
- Incoterm `/RequestForQuotation/cac:DeliveryTerms/cbc:ID` = `DAP` with destination `/RequestForQuotation/cac:DestinationCountry/cbc:IdentificationCode` = `XU` and origin `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`: a cross-border delivery, consistent with the export and import declarations of the flow.
- Codes: every code resolved in its list (annotate.py shows no `NOT IN LIST`); HS `440799` and CPC `31102` both describe non-coniferous sawn wood over 6 mm, which fits the 38 mm hardwood slat.
- Item properties: average moisture `12` % and core moisture `13` % lie inside the range `10`–`14`; nominal thickness `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Dimension[3]/cbc:Measure` = `38` lies inside the tolerance `37.5`–`38.5` mm of `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[2]/cac:RangeDimension/cbc:Measure` = `38`.
- Physics (calculated): one slat 1800 × 95 × 38 mm = 0.006498 m³; `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cbc:Quantity` = `4800` slats = 31.19 m³; at 650–750 kg/m³ for kiln-dried hardwood at 12 % moisture (own knowledge: ash, oak, beech) that is 20.3–23.4 t, which matches the 21 600 kg gross that the later transport documents give. 4800 / `50` per pack = 96 packs, as `06-DespatchAdvice.xml` later states.
- Certificate: `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:Certificate/cbc:ID` = `XB-FOR-2025-0118`, valid to `2027-12-31`, is the same certificate (ID, reference ID, audit document `XB-FOR-AUD-2025-0118`) in every example of the flow that carries the item.

## Considered and refuted
- `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:PackQuantity` = `1` next to `/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `50`: suspected contradiction (pack of one against pack of fifty) — refuted because PackQuantity counts the subunits making up the item (a slat is one piece) and PackSizeNumeric the items in a pack (a bundle of 50); the two answer different questions and agree with the 96 bundles of 50 in `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`
- `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`: suspected a location named after the company and without address or identifier — refuted for this document because the name does name the place (the goods-in of the buyer's works in Ferrano), the buyer's address is in the same document, and a request for quotation only needs the place to price DAP.
- `/RequestForQuotation/cac:AdditionalDocumentReference/cbc:ID` = `VI-DS-SL1800` and `/RequestForQuotation/cac:RequestForQuotationLine/cac:DocumentReference/cbc:ID` = `VI-DS-SL1800`: suspected an ID-only reference that does not say what it refers to — refuted because `/RequestForQuotation/cbc:Note[2]` = `Slats to our drawing VI-DS-SL1800.` says it is the buyer's drawing, and the header and line references are both legitimate with a single line.
