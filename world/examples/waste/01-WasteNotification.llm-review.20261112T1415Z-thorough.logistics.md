# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/01-WasteNotification.xml`, Git blob `59bbf75435c6cd8c4e16f9d3d8ff87cea9ce93be` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

### waste/01#F1 · Medium · The notification does not identify the waste, its intended total quantity or the shipment period
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- Why: A Waste Notification is "a document used to notify the competent authorities of planned movements of waste", and its Shipment is "the relevant shipment information describing the planned transport and the waste material". What the authority decides on is which waste (a waste classification, e.g. a Basel Annex VIII/IX entry or a national waste-list code), how much in total, and over which period. The goods item carries only a free-text description; there is no `cac:Item/cac:CommodityClassification` (or similar code) for the waste, no net quantity, no total intended quantity for the twelve shipments and no period (e.g. `cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod`). The only quantity, `GrossWeightMeasure` = 40 000 kg, is defined as "goods plus packaging plus transport equipment" and does not say whether it is one shipment or all twelve (see F3). Basel notification practice (own knowledge: notification form, intended quantity in tonnes and m3, intended period, waste code) needs all of these.
- Condition: The notification identifies the waste with a code in a structured element, states the intended total quantity (net, in tonnes) of the notified movements and the period in which they are planned.
- Options: (preferred) add a commodity/waste classification on the goods item's Item, a net weight on the goods item or shipment that is clearly the total for the notification, and a planned period on the shipment's Delivery; alternatively state the per-shipment quantity and keep `ConsignmentQuantity` as the multiplier, saying so in `cac:Shipment/cbc:Information`.
- Needs decision: no

### waste/01#F2 · Low · 40 000 kg gross for one road shipment of polyethylene waste in big bags is not physically plausible
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `4923`
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: The carrier is a road haulier (ISIC 4923, "Freight transport by road"), so one shipment is one lorry load. Figures used (own knowledge, not in the document): a road combination is limited to 40 t (in some countries 44 t) gross combination weight, with tractor about 7.5 t and curtain-side semi-trailer about 7 t, leaving about 25 t payload; a semi-trailer has 13.6 m x 2.45 m x 2.7 m = 90 m3 inner volume; a big bag (FIBC) of about 0.9 x 0.9 x 1.1 m = 0.89 m3; bulk density of sorted mixed PE production waste 0.05-0.2 t/m3 for film and offcuts, 0.25-0.45 t/m3 for regrind or lumps. Calculation: a floor of 13.6 m x 2.45 m takes 15 x 2 = 30 bags per layer, two layers = 60 bags = 53 m3; at the highest density, 0.45 t/m3, that is 53 x 0.45 = 24 t of waste; even filling the whole 90 m3 at 0.45 t/m3 gives 40.5 t, which bagged goods cannot reach. 40 t "goods plus packaging plus transport equipment" means about 33 t of bagged waste if the trailer counts as transport equipment, which is over the payload (about 25 t) and needs 33 / 0.45 = 73 m3 at the highest density (about 82 bags, more than the 60 that fit). If the 40 t is instead the total of all twelve shipments (F3), it is 3.3 t per load, implausibly little for a lorry. Either reading fails.
- Condition: The weight stated for one shipment can be carried by one road vehicle and fits its loading space at the bulk density of the described waste (for bagged PE waste roughly 10-24 t), or the document states that the figure is the total of the notified shipments and that total is consistent with twelve loads.
- Options: (preferred) state a per-shipment weight of about 20 t and give the total separately (F1); alternatively keep 40 t and describe it as the total for the notification.
- Needs decision: no

### waste/01#F3 · Low · The planned shipment carries the same shipment and consignment IDs as the first actual movement, with a different weight
- XPath: `/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: The notification covers twelve shipments (`ConsignmentQuantity` = 12) and its Shipment describes "the planned transport". The waste movement that reports the first of them (`02-WasteMovement.xml:/WasteMovement/cbc:SequenceNumberID` = `1`) uses the same shipment ID and consignment ID (`02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`) but a gross weight of 38 200 kg instead of 40 000 kg. One identifier thus names both the planned set (or a planned typical load) and one actual load; the remaining eleven movements would either reuse it or need new ones the notification does not know. A planned weight may differ from an actual one, so this is not a contradiction in itself, but the identifiers do not say which object is meant.
- Condition: Either the notification's Shipment is the notified set of movements with its own identifier, and each waste movement has its own shipment/consignment identifier; or the documents state that the notification's shipment is shipment 1 and the weights are planned and actual values of the same load.
- Options: (preferred) give the notification's Shipment an identifier for the whole notified movement set and the movement its own shipment ID, so that twelve movements can be told apart; alternatively keep the shared IDs and say in `cac:Shipment/cbc:Information` that the figure is a planned value.
- Needs decision: yes

### waste/01#F4 · Low · The shipment names no place of loading or destination, and all places are in Urvania
- XPath: `/WasteNotification/cac:Shipment`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: The planned transport has no `ShipmentStage`, `Delivery`, `ExportCountry` or exit/arrival location; the only places are party addresses, and producer and recovery facility are both in Ferrano, Urvania (postal zones 4120 and 4140). `CustomsParty` is "the competent authority granting a permit to export or import the waste", and the carrier's authorisation is for international haulage, which suggests a transboundary movement; the document does not show where the waste leaves or enters a country, or where it is loaded and delivered. If the movement is domestic, the export/import framing does not fit; if it is transboundary, the route is missing.
- Condition: The shipment states where the waste is loaded and where it is delivered (and, if transboundary, the countries of export and import or the border crossing), consistent with the role of `CustomsParty`.
- Options: (preferred) add `cac:Shipment/cac:Delivery/cac:DeliveryLocation` (the facility) and a loading place on a `ShipmentStage`, and, if the story is transboundary, `ExportCountry` and `LastExitPortLocation`/`FirstArrivalPortLocation`; alternatively make the story explicitly domestic.
- Needs decision: yes

### waste/01#F5 · Low · The contract reference says only an ID
- XPath: `/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`
- Why: The reference has no `DocumentTypeCode` or `DocumentType`, and the ID occurs in no example (searched over `*.xml`). A contract between notifier and recovery facility is what a notification has to refer to (own knowledge of Basel practice), so the reference has a reason to be here, but only the ID's wording says what it is. The same pattern, a `*DocumentReference` whose only child is `cbc:ID`, occurs 555 times in 177 of 250 examples (counted over `world/examples/*/*.xml` with lxml).
- Condition: The reference states what kind of document it is (code or text) and, if useful, its issue date.
- Options: (preferred) add `cbc:DocumentType` (e.g. the contract for recovery) and `cbc:IssueDate`; a `DocumentTypeCode` from the world's list where one fits.
- Needs decision: no

## Checked and consistent
- `/WasteNotification/cbc:ConsignmentQuantity` = `12` with unit EA ("estimated total number of shipments") agrees with `02-WasteMovement.xml:/WasteMovement/cbc:ConsignmentQuantity` = `12`.
- `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY` is in the world list bound to this element (`gc/WasteNotificationTypeCode.gc`) and agrees with the facility's authorisation `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3` (Basel Annex IV B, recycling of organic substances not used as solvents, which fits plastics recycling; own knowledge).
- `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:HazardousRiskIndicator` = `false` agrees with `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste` and with the goods description.
- Validity periods: recovery permit ends 2029-12-31 and haulage licence 2030-06-30, both after the issue date 2026-03-23 and the movement date 2026-04-02.
- Order of dates in the flow: notification 2026-03-23 09:28, movement 2026-04-02 12:34, invoice 2026-04-04 12:44.
- Shipment and consignment IDs and the goods description are the same in `02-WasteMovement.xml` (see F3 for the weight).
- `check_ids.py`: ISIN `XU0001042501` check digit OK.
- Physics: see F2 (figures and calculation there).

## Considered and refuted
- `/WasteNotification/cbc:ConsignmentQuantity`: suspected misuse (number of consignments, not shipments) — refuted because in Waste Notification the element is defined as "Estimated total number of shipments for this Notification Document", and 12 EA is such a count.
- `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure`: suspected that a gross weight is the wrong measure for the waste quantity — refuted as a separate finding: the definition (goods plus packaging plus transport equipment) is correctly used for a gross figure; the missing net/total quantity is F1, the magnitude is F2.
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode`: suspected an R code that does not fit plastics — refuted because R3 covers recycling/reclamation of organic substances, under which plastics recycling is normally reported.
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty`: suspected that a carrier is premature in a notification — refuted because the notification's shipment describes the planned transport, and naming the intended carrier is part of that.

## Outside this review
- Whether Trasvia Haulage (`XU-R-104822`, also carrier in the road flow) had a vehicle free for the waste movements on the dates of this flow is a cross-flow capacity and timeline question.
