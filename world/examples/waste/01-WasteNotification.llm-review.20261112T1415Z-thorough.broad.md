# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: broad

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

### waste/01#F1 · High · Transboundary notification to customs for a movement inside one city of Urvania
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- Why: `CustomsParty` is defined as "The competent authority granting a permit to export or import the waste", and the world list behind `WasteNotificationTypeCode` (`world/codelists/lists.json`, list `WasteNotificationType`) describes the code as "Whether a notification of a transboundary movement of waste is for recovery or for disposal (Basel Convention, Annex V A)". The waste producer/notifier (Valdara Industries, Via delle Officine 17, Ferrano) and the recovery facility (Rinova Recovery, Via del Riciclo 31, Ferrano) are both in Urvania, in the same city; nothing is exported or imported, so there is no export or import permit for a customs party to grant, and the Basel notification procedure does not apply. The document as a whole contradicts itself: a transboundary notification for a domestic movement. In addition, a customs administration is not normally the competent authority for waste shipments (that is an environmental authority; own knowledge of the Basel Convention and e.g. EU Regulation 2024/1157), and its contact is a "Border office" although no border is crossed. The flow also contains no consent of the authority before the movement in `02-WasteMovement.xml` takes place, which a transboundary procedure would require.
- Condition: either the facility (or the producer) is in another country than the other, so that an export/import exists and `CustomsParty` grants it, or the movement is domestic and the notification, its type code and its receiving authority are those of a domestic procedure; in both cases the receiving/competent authority is one whose task is waste shipments.
- Options: (a) preferred: move the recovery facility to Bayvarra or Lisavu (a real transboundary movement under the Lumeport Trade Accord), with the competent authorities of dispatch and destination as `CustomsParty` (1..n) and, if the story wants it, a consent step in the flow; this keeps the document type meaningful. (b) keep the movement domestic and replace the customs administration with the Urvanian environmental authority, using a type code from a list that covers domestic notifications (the list has `GENERAL`); `CustomsParty` stays mandatory [1..n], so this option needs a careful choice of which authority fills it.
- Needs decision: yes

### waste/01#F2 · Medium · Disposal facility given for a recovery operation
- XPath: `/WasteNotification/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material". The notification is for recovery (`RECOVERY`, R3 per the facility's authorisation `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`); the waste is recycled, not disposed of, and Rinova holds only a recovery permit. The same party in both roles says that it both disposes and recovers the same waste, which the rest of the document does not support. Basel Annex V A distinguishes disposal and recovery facilities by the operation (D or R codes).
- Condition: `DisposalFacilityParty` is present only if a disposal (D) operation is part of the notified movement, with a party authorised for it.
- Options: remove `DisposalFacilityParty` (preferred: nothing in the story is disposed of); or add a real disposal step (e.g. residues to a D-operation facility) with its own party and authorisation.
- Needs decision: no

### waste/01#F3 · Medium · Province in Region
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a country subdivision and belongs in `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state …"). The same value occurs in 219 `cbc:Region` elements in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of'` over `world/examples`).
- Condition: no address of this example carries a province in `Region`; the province, where wanted, is in `CountrySubentity` (and `CountrySubentityCode` if the world has codes).
- Options: move the value to `CountrySubentity` (preferred: it is the element made for it); or drop it.
- Needs decision: no

### waste/01#F4 · Medium · The notification does not identify the waste by code nor state the planned total quantity and period
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- Why: the document's purpose is "to notify the competent authorities of planned movements of waste". What the authority decides on (Basel Annex V A; own knowledge) is the waste identified by its classification (Basel Annex IX entry such as B3010 for non-hazardous plastic waste, national/EWC code), the estimated total quantity and the period of the planned shipments. Here the waste is described only in free text (no `CommodityClassification` or other code in the goods item), and the only quantity is a gross weight of 40000 kg that, by definition of `GrossWeightMeasure`, includes transport equipment; for a notification of 12 shipments it is not clear whether it is per shipment or total, and no net quantity of waste is given. No planned period is given anywhere (e.g. in `Shipment/Delivery`, "The delivery of this shipment").
- Condition: the notification identifies the waste by a code from a stated classification, states the estimated total quantity of waste (net) for the notified shipments, and the planned period of the shipments; any gross weight is clearly per shipment.
- Options: add a `CommodityClassification` with the Basel/national waste code to the goods item, a net weight or quantity for the whole notification, and a planned period under `Shipment/Delivery` (preferred: all within the existing `Shipment`); alternatively replace the gross weight by `NetWeightMeasure` for the total.
- Needs decision: no

### waste/01#F5 · Low · Customs administration described as a company in the commercial register
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: a public administration (`IndustryClassificationCode` `8411`, General public administration activities) is not registered in a commercial register and has no liquidation status (`CompanyLiquidationStatusCode`, "the party's liquidation status"). 12 examples contain the name `Customs Administration of Urvania` together with a `CompanyLiquidationStatusCode` (`grep -l` on both, over `*.xml`; not checked per party).
- Condition: the receiver's legal entity carries no commercial-register scheme and no liquidation status, or a scheme that fits a public body.
- Options: drop `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme` from the authority (preferred); or register it in a public-body register of the world if one exists.
- Needs decision: no

### waste/01#F6 · Low · Notifier's contact is the sales order desk
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender is the notifier of a waste movement; the authority needs a contact responsible for the waste and the notification (environment, waste or logistics officer), not Valdara's furniture sales order desk. The recovery facility's contact is its customer service in Sales; for the facility the authority would expect the plant/operations contact. "Order desk" occurs in 87 examples (`grep -rl --include='*.xml' '<cbc:Name>Order desk</cbc:Name>'`).
- Condition: the notifier's contact (and the facility's, if kept) is a function that answers for the waste movement.
- Options: use an environmental/waste management contact for Valdara and an operations contact for Rinova (preferred); or omit the contacts.
- Needs decision: no

### waste/01#F7 · Low · Master data the notification does nothing with
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: the listed shares, the share capital and Valdara's warehousing provider Castrano Logistics have no role in notifying a waste movement (the carrier is Trasvia Haulage). This looks copied from Valdara's master data; the same security listing occurs in 75 examples and the same service provider in 75 (`grep -rl --include='*.xml' 'XU0001042501'`, `'VI-SP-2026-01'`).
- Condition: the sender carries only data the notification uses, or the document gives a reason for each (e.g. Castrano loads the waste).
- Options: remove them (preferred); or give Castrano a role in the movement if it actually handles the waste.
- Needs decision: no

### waste/01#F8 · Low · Contract reference says nothing about what it is
- XPath: `/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`
- Why: a reference with only an ID; only the ID text suggests that it is the contract between notifier and facility (which Basel Annex V A asks the notifier to declare). No example of the flow carries this ID, and the reference has no `DocumentTypeCode`, `DocumentType` or issue date.
- Condition: the reference states what kind of document it is (and, ideally, its date).
- Options: add `DocumentTypeCode`/`DocumentType` ("contract for recovery") and `IssueDate` (preferred); a contract is not expected as a UBL example of the flow.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` check digit correct.
- `MarketCode` `XFER` is not in the ISO 10383 MIC file in `world/codelists/sources/iso10383/ISO10383_MIC.csv` (no clash with a real MIC); ICD `0990` is not in the Peppol ICD list (`sources/peppol/ICD.xml`).
- `ConsignmentQuantity` `12` is the same in `02-WasteMovement.xml:/WasteMovement/cbc:ConsignmentQuantity` = `12`.
- Parties: notifier, producer and sender are the same party (Valdara, `XU-R-104274`), as are recovery facility in 01 and sender of 02 (Rinova, `XU-R-104548`); identifiers agree across the three examples.
- R3 (Basel Annex IV, recycling/reclamation of organic substances not used as solvents) fits the recycling of polyethylene, an organic substance.
- Physics: a gross weight of 40000 kg per road shipment equals the usual 40 t maximum gross combination weight of a five-axle articulated vehicle (own knowledge); plausible as a per-shipment estimate (but see F4).
- `HazardousRiskIndicator` `false` fits sorted polyethylene production waste.

## Considered and refuted
- `/WasteNotification/cac:SenderParty/cbc:IndustryClassificationCode`: a furniture manufacturer (ISIC 3100) producing polyethylene production waste looked odd — refuted because plastic furniture or components are moulded from PE, and production scrap is a normal by-product.
- `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]`: Italian-style text (`Via delle Officine`) under `languageID` `en-XU` — refuted because the world uses these as the established English-usage names of Urvanian places (as with `Ferrano`); they are world convention, not a mislabelled language.
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose`: "International road haulage" for a domestic movement — refuted because a haulier's licence for international haulage also covers domestic carriage; it is the carrier's authorisation, not a statement about this movement.
- `/WasteNotification/cac:Signature`: signature with ID and signatory only, no method or date — refuted because the elements are optional and the signatory (the notifier) is the right party.

## Outside this review
- Whether a notification issued on 2026-03-23 could, under the world's procedure, be consented in time for the first movement reported on 2026-04-02 (`02-WasteMovement.xml`) is a timeline question across documents.
