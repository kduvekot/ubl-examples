# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: context

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### waste/01#F1 · Medium · A notification of a transboundary movement, with a permit authority for export or import, for a movement that stays inside one town
- XPath: `/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: UBL defines `CustomsParty` as "The competent authority granting a permit to export or import the waste", and the WasteNotification as the notice to "the competent authorities of planned movements of waste" — in the Basel Convention sense (own knowledge) a prior informed consent procedure for transboundary movements. Here the waste producer/notifier (Valdara Industries, Ferrano, XU) and the recovery facility (Rinova Recovery, Ferrano, XU) are in the same town of the same country; no other country, border crossing, transit or route is stated anywhere in the document, and nothing is exported or imported. The customs authority is addressed through its "Border office", and the carrier's authorization is quoted for "International road haulage", although the movement is local. The same situation is in `02-WasteMovement.xml:/WasteMovement/cac:RecoveryFacilityParty` and its receiver. Either the story is a domestic movement (then a customs authority "granting a permit to export or import" has nothing to grant, and the document type and roles do not fit), or it is a transboundary movement (then the facility's country, or the route and border, is missing, and the purpose of the document depends on it).
- Condition: Either the recovery facility (or the stated route) lies in a country other than the producer's, so that an export or import exists for `CustomsParty` to permit; or the document states a domestic procedure in which the receiving authority is the one that approves the movement, and no element claims an export/import or international carriage.
- Options: (a) preferred: move the recovery facility (or add a destination across a border) so the movement is transboundary, as the WasteNotification's purpose presumes; this keeps the document type meaningful. (b) Keep the domestic story but name a competent environmental authority instead of the customs border office, and drop "International" from the carrier's authorization purpose; the CustomsParty element then still reads as "permit to export or import", which remains a strain.
- Needs decision: yes

### waste/01#F2 · Medium · A province in `Region`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province, an administrative subdivision of the country, belongs in `CountrySubentity` ("The territorial division of a country, such as a county or state"). The same value is in `Region` in 104 examples (219 occurrences; `grep -r --include='*.xml' -o '<cbc:Region>Province of'` over `world/examples`).
- Condition: No `Address/Region` holds a province; the province, where needed, is in `CountrySubentity`.
- Options: (a) preferred: move the value to `CountrySubentity` (with `CountrySubentityCode` if the world has one). (b) Drop it, since the postal zone and city already locate the address.
- Needs decision: no

### waste/01#F3 · Low · Party master data the notification does nothing with
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- Why: The sender is the notifier and waste producer. Its warehousing and despatch provider (Castrano Logistics) takes no part in this waste movement (the carrier is Trasvia Haulage), and its stock listing, share capital and paid-up shares have no bearing on a notification to the authorities. The contact is the sales order desk ("Customer service officer", Sales), not the person responsible for the notified waste — a waste notification needs a contact the authority can reach about the waste and the movement. These values look copied from the party's master data: the same `VI-SP-2026-01` service provider and the same security listing appear in 75 examples each, the "Order desk" contact in 87 (counted with `grep -rl --include='*.xml' -F` over `world/examples`).
- Condition: Every element under `SenderParty` has a reason in a waste notification; the contact is one responsible for the notified waste or its shipment.
- Options: (a) preferred: drop `ServiceProviderParty`, `SecurityListing`, `CorporateStockAmount` and `FullyPaidSharesIndicator` here, and give the sender an environmental/waste or logistics contact. (b) Keep the service provider only if the story makes Castrano Logistics take part in the waste shipment (then it belongs in the shipment, not as master data).
- Needs decision: no

### waste/01#F4 · Low · A public authority described as a VAT-registered company in the commercial register
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The receiver is the Customs Administration, a public body (ISIC 8411). A public administration is not registered in the "Commercial register of Urvania" and has no liquidation status; its VAT registration plays no role in a waste notification. Nothing in this document uses these values.
- Condition: The customs administration carries no commercial-register scheme or liquidation status, and no tax scheme unless the document uses it.
- Options: (a) preferred: drop `PartyTaxScheme` and the commercial-register parts of `PartyLegalEntity` (keep the name and, if it exists in the world, a public-body register). (b) Use a public-sector registration scheme instead of the commercial register.
- Needs decision: no

### waste/01#F5 · Low · The notification's shipment carries the identifiers of the first actual shipment, although it covers twelve
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- XPath: `/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- Why: `ConsignmentQuantity` is the "Estimated total number of shipments for this Notification Document" (12), while `Shipment` is "The relevant shipment information describing the planned transport and the waste material". The shipment and consignment IDs are those of the first movement (`02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`, `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`, `02-WasteMovement.xml:/WasteMovement/cbc:SequenceNumberID` = `1`). So it is unclear whether the notification's `Shipment` describes the whole notified quantity (then 40 000 kg for 12 shipments, about 3.3 t each, does not fit the 38 200 kg of the first one) or only the first shipment (then it is not the planned transport of the notification, and the other 11 shipments get IDs that this document does not know).
- Condition: The notification's `Shipment` either describes the whole notified movement (its own ID, and a weight for all shipments together or clearly per shipment), or the document states that it describes the first of the shipments; the weights in 01 and 02 can be read together without contradiction.
- Options: (a) preferred: give the notification's shipment its own ID (the notified movement as a whole) and a total weight for the 12 shipments; the movement document keeps the ID of the actual shipment. (b) Keep the IDs and state in the goods description or a note that the figures are per shipment.
- Needs decision: yes

### waste/01#F6 · Low · The notification type covers several shipments, but the code says only "Recovery"
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- Why: The world list `WasteNotificationTypeCode` has three values: `RECOVERY` ("Waste for recovery operations"), `DISPOSAL` and `GENERAL` ("Several shipments of the same waste over up to a year"). This notification covers 12 shipments of the same waste, which is the case `GENERAL` names, and it is also for recovery. The list mixes two independent dimensions (recovery/disposal, and single/general — two separate boxes in the Basel notification form, own knowledge), so one code cannot say both; the code chosen leaves out that this is a general notification.
- Condition: The type of the notification (recovery, and general for several shipments) is fully expressed, or it is decided which of the two dimensions the code carries and the other is expressed elsewhere.
- Options: (a) Keep `RECOVERY` (the R3 authorization and recovery facility already say "recovery") and decide that the multi-shipment nature is carried by `ConsignmentQuantity`. (b) Use `GENERAL` and rely on `RecoveryFacilityParty` and the R-code for "recovery". (c) Split the world list into two dimensions. No strong preference; this is a code-list decision.
- Needs decision: yes

### waste/01#F7 · Low · `DisposalFacilityParty` in a notification for recovery
- XPath: `/WasteNotification/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material", `RecoveryFacilityParty` "The Party recovering the waste material". The notification is for recovery (`RECOVERY`, authorization R3 "Recovery of non-hazardous plastic waste"); no disposal (D-operation) takes place, so the same party in the disposal role says something the document otherwise denies. The same is in `02-WasteMovement.xml:/WasteMovement/cac:DisposalFacilityParty`. These two are the only examples carrying `DisposalFacilityParty` (`grep -rl --include='*.xml' -F '<cac:DisposalFacilityParty>'`).
- Condition: `DisposalFacilityParty` is absent, or a party that actually disposes of (part of) the waste is named, with that disposal stated.
- Options: (a) preferred: drop `DisposalFacilityParty`. (b) Keep it only if the story adds a disposal of residues, with its D-code.
- Needs decision: no

### waste/01#F8 · Low · The waste is identified by free text only
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: A waste notification exists so the authority can assess the notified waste; its identification by a waste code (Basel Annex VIII/IX code, e.g. B3011 for non-hazardous plastic waste, or a national/EWC waste code — own knowledge) is central to that, and the quantity notified is part of it. The goods item carries neither a classification nor a net quantity (`GoodsItem` offers `cac:Item/cac:CommodityClassification` and `NetWeightMeasure`). The R3 code is only stated as the facility's authorization scope, not as the operation of this notification.
- Condition: The notified waste carries a waste classification code and a notified quantity.
- Options: (a) preferred: add a commodity classification with a waste code from a world list (or the real Basel code list, if the world uses it) and the notified net weight. (b) Leave as is if the world deliberately keeps waste coding out; then say so in the description.
- Needs decision: no

### waste/01#F9 · Low · The contract reference does not say what it is
- XPath: `/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`
- Why: `DocumentReference` is "A reference to a relevant document associated with this Waste Movement"; only the ID hints that this is the contract between notifier and recovery facility (which a notification has to be backed by — own knowledge of the Basel procedure). Without `DocumentTypeCode` or `DocumentDescription` the reader cannot tell what the document is. It is not an example of the flow, which is acceptable for a contract.
- Condition: The reference states the kind of document (code or description).
- Options: (a) preferred: add a `DocumentTypeCode` or `DocumentDescription` ("Contract for recovery of production waste"), and its issue date.
- Needs decision: no

## Checked and consistent
- `WasteNotificationTypeCode` uses the world list that the CVA binds to this element (`WasteNotificationType`), and `RECOVERY` is in it.
- `PartyAuthorization/cbc:PurposeCode` = R3 ("Recycling/reclamation of organic substances which are not used as solvents"): plastic recycling is classed under R3 in Basel/EU practice (own knowledge); fits "Recovery of non-hazardous plastic waste" and the recovery facility's ISIC 3830.
- `HazardousRiskIndicator` = false agrees with "non-hazardous plastic waste" in the authorization purpose.
- `NotifierParty`, `WasteProducerParty`, `SenderParty` and `Signature/SignatoryParty` are the same party (XU-R-104274), consistent with the producer notifying its own waste; the receiver is the `CustomsParty` (XU-R-105507), consistent with the notification going to the authority.
- `ConsignmentQuantity` = 12 agrees with `02-WasteMovement.xml:/WasteMovement/cbc:ConsignmentQuantity`; the notification ID is the one 02 references.
- The authorization validity (end 2029-12-31) and the carrier licence (end 2030-06-30) are after the issue date 2026-03-23.

## Considered and refuted
- `/WasteNotification/cac:SenderParty/cbc:IndustryClassificationCode` = `3100`: a furniture manufacturer producing "polyethylene production waste" looked odd — refuted because plastic parts and packaging in furniture production plausibly yield PE production waste.
- `/WasteNotification/cbc:ConsignmentQuantity`: a number of shipments with `unitCode` "each" — refuted because a count of shipments in units of "each" fits the definition "Estimated total number of shipments".
- `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Telefax`: a fax number looked like filler — refuted because border and customs offices commonly still list fax as a channel for paper procedures; the contact itself is covered by F1.
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization`: an authorization in a party might be master data — refuted because a notification must show that the recovery facility is authorised for the operation; it is used here.
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: the carrier's haulage licence — refuted as filler, because the carrier's authorization is relevant to a waste movement; only the "International" in its purpose is part of F1.

## Outside this review
- Whether 40 000 kg (or 38 200 kg in 02) of sorted PE waste in big bags fits one road vehicle by volume and payload is a physics and capacity question for the logistics part, not of this lens.
