# LLM review: 02-Forecast.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/02-Forecast.xml`, Git blob `564d177fc853a93d7bb7f285f6471573cea2ed35` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/02#F1 · High · A forecast of future lint carries a classing certificate verified 18 days after the forecast was issued
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `/Forecast/cbc:IssueDate` = `2026-02-02`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: Signature/ValidationDate is "The date upon which this signature was verified". A document
  issued on 2026-02-02 cannot report a verification that takes place on 2026-02-20. Beyond the date,
  Item/Certificate is "A certificate associated with this item": a classing certificate records the
  measured grade, staple and micronaire of one classed lot. The forecast is for 24,000 kg of lint to
  be supplied between 2026-02-16 and 2026-06-02; at its issue the seed cotton of the flow had not
  even been delivered to the gin (`03-DeliveryNote.xml:/DeliveryNote/cac:Shipment/cac:Delivery/cbc:ActualDeliveryDate` = `2026-02-05`),
  so no lot of it could have been classed. The same certificate, with the same validation date, is
  in the forecast revision 07 and the order 08, and referenced from 05 and 10.
- Condition: no element of the forecast states a fact (certificate, signature verification) dated
  after its issue date, and any quality requirement in the forecast describes what is wanted rather
  than the result of classing a particular lot.
- Options: (a, preferred) express the wanted quality only as item properties (grade, staple length,
  which are already there) and leave the classing certificate out of the forecast; (b) if a
  certificate of an earlier crop is meant, give it an ID and validation date before 2026-02-02 and
  make clear it describes a reference lot.
- Needs decision: no

### cotton/02#F2 · Medium · The mill's forecast refers to the ginnery's season agreement with the farm
- XPath: `/Forecast/cac:AdditionalDocumentReference/cbc:ID` = `SCG-SEASON-2026`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID` = `SCG-SEASON-2026`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- Why: The forecast is sent by Lumeport Textile Mill (buyer) to Selanu Cotton Ginnery (seller). In
  the flow, SCG-SEASON-2026 is the contract between the ginnery and the farm (the contract of the
  self-billed invoices 01 and 04, between ginnery and farm), while the mill's own season document is
  LTM-SEASON-2026 (04 cites it as the originator's document). A forecast between mill and ginnery has
  no reason to refer to the ginnery's purchase agreement with its farmer, a contract the mill is not
  a party to; the reference carries no DocumentTypeCode or description that would explain it.
- Condition: every document reference in the forecast points to a document that concerns the
  mill–ginnery relationship, and says what it is where the ID alone does not.
- Options: (a, preferred) refer to the mill–ginnery agreement (LTM-SEASON-2026, or whatever the
  story names it) with a DocumentTypeCode or DocumentDescription; (b) leave the reference out.
- Needs decision: yes (which agreement governs the mill–ginnery relationship is part of the story)

### cotton/02#F3 · Medium · PackSizeNumeric carries the bale weight in kilograms, not a number of items
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: Item/PackSizeNumeric is "The number of items in a pack of this item". 227 is the weight of a
  bale in kilograms (the description says "bales of about 227 kg"); a bale of lint holds no 227
  items. A numeric without a unit cannot carry a weight. The same value is in 07, 08, 10, 11, 15 and
  16 of the flow (`grep -n PackSizeNumeric` over `world/examples/cotton/*.xml`).
- Condition: no element meant for a count holds the bale weight; the bale weight, if stated in
  structured form, is in an element with a weight unit.
- Options: (a, preferred) leave PackSizeNumeric out (PackQuantity 1 EA already says one bale is the
  unit) and state the bale weight as an AdditionalItemProperty with ValueQuantity in KGM; (b) leave
  the weight to the description only.
- Needs decision: no

### cotton/02#F4 · Low · Region of origin "North coast" is the farm's District elsewhere
- XPath: `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cac:OriginAddress/cbc:Region` = `North coast`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:District` = `North coast`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in
  which this address is located"; Address/District is "The district or geographical division of a
  country or region". The flow describes North coast as a district of Lisavu in the farm's address;
  here the same area is given as a region. One of the two uses is not the element the area is.
- Condition: North coast is held in the same address element wherever it occurs in the flow.
- Options: (a, preferred) use District in OriginAddress, as in the farm's address; (b) if North
  coast is a recognised region, use Region in the farm's address too.
- Needs decision: no

## Checked and consistent
- Roles: sender and buyer are the mill, receiver and seller the ginnery, which fits a buyer's order
  forecast (ForecastPurposeCode ORDER, ForecastTypeCode TOTAL).
- ForecastPeriod 2026-02-16 to 2026-06-02 starts after the issue date.
- Staple length 28.6 mm agrees with the certificate remark 1-1/8 inch (28.575 mm).
- HS 5201.00 and CPC 01921 fit ginned lint not carded or combed.

## Considered and refuted
- `/Forecast/cbc:BasedOnConsensusIndicator` = `true`: a consensus forecast sent as version 1 by one
  side suspected as contradictory — refuted because a collaborative forecast can be agreed between
  the parties before it is sent; nothing in the example says otherwise.
- `/Forecast/cac:ForecastLine/cac:SalesItem/cac:Item/cbc:PackQuantity` = `1`: one subunit per item
  suspected as a filler — refuted because it states that the item is sold by the bale, which the
  description relies on.
- `/Forecast/cbc:Note` = `Depends on clothing orders from the store.`: suspected as unrelated —
  refuted because it explains why the forecast may change, which the revision 07 then does.
