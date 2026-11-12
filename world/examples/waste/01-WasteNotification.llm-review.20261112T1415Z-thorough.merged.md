# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/01-WasteNotification.xml`, Git blob `59bbf75435c6cd8c4e16f9d3d8ff87cea9ce93be` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit e6f29b5 2026-11-12 Reviews of the waste flow, run 20261112T1415Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

This merged file combines the parts broad, money, parties, logistics and context of run
`20261112T1415Z-thorough`; all five parts reviewed the same Git blob as this file.

## Findings

### waste/01#F1 · Medium · Notification of a transboundary movement, addressed to the customs administration, for a movement inside one town of Urvania
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- Why: `CustomsParty` is defined as "The competent authority granting a permit to export or import the waste", and the world list bound to `WasteNotificationTypeCode` (`world/codelists/lists.json`, list `WasteNotificationType`) is described as "Whether a notification of a transboundary movement of waste is for recovery or for disposal (Basel Convention, Annex V A)". The waste producer and notifier (Valdara Industries, Via delle Officine 17, Ferrano, postal zone 4120) and the recovery facility (Rinova Recovery, Via del Riciclo 31, Ferrano, 4140) are in the same town of Urvania; no other country, route, border crossing or transit is stated. Nothing is exported or imported, so there is no export/import permit for a customs party to grant, and the Basel notification procedure does not apply. Under the Basel Convention (own knowledge; also EU Regulation 2024/1157) the competent authorities are environmental authorities; customs controls at the border. The authority is addressed through its "Border office", although no border is crossed. The carrier's licence for "International road haulage" (`/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`) adds to the transboundary impression, but it is not itself wrong (see F12 and "Considered and refuted"). The same receiver is in `02-WasteMovement.xml:/WasteMovement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`.
- Condition: either the recovery facility (or a stated route) lies in another country than the producer, so that an export or import exists for `CustomsParty` to permit; or the movement is domestic, and the notification, its type code and its receiving authority are those of a domestic procedure, with a receiving/competent authority whose task is waste movements, and no element claims an export or import.
- Options: (a) preferred by broad and context: move the recovery facility to Bayvarra or Lisavu (a real transboundary movement), with the competent authorities of dispatch and destination as `CustomsParty` (1..n) and, if the story wants it, a consent step in the flow; this keeps the document type meaningful. (b) preferred by parties for a domestic story: keep the movement domestic and name a competent Urvanian waste/environment authority as `ReceiverParty`/`CustomsParty` (the element is mandatory [1..n] and the only place for the competent authority in this document, so its definition remains a strain). (c) keep customs only if the world's story makes the Urvanian customs administration the competent authority for waste, and say so in the world. Merge preference: (a), because it is the only option under which every element keeps its UBL meaning.
- Needs decision: yes
- From: broad (F1, High), parties (F2), context (F1)

### waste/01#F2 · Medium · Rinova named as disposal facility in a recovery notification
- XPath: `/WasteNotification/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material"; `RecoveryFacilityParty` is "The Party recovering the waste material". The notification is for recovery, and Rinova's only authorisation is R3 (Basel Annex IV, recycling/reclamation of organic substances not used as solvents), a recovery operation; nothing in the document says that any part of the waste is disposed of (a D operation). Naming the same party in both roles says that it both disposes of and recovers this waste. The Basel notification form (own knowledge) names the facility as either disposal or recovery facility, according to the operation. The same is in `02-WasteMovement.xml:/WasteMovement/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`; these are the only two examples carrying `DisposalFacilityParty` (`grep -rl --include='*.xml' -F '<cac:DisposalFacilityParty>'`).
- Condition: `DisposalFacilityParty` is present only if a disposal (D) operation is part of the notified movement, naming the party that performs it with an authorisation for it; otherwise only `RecoveryFacilityParty` identifies Rinova.
- Options: remove `DisposalFacilityParty` (preferred: nothing in the story is disposed of); or add a real disposal step (residues to a D-operation facility) with its own party and authorisation.
- Needs decision: no
- From: broad (F2), parties (F3), context (F7, Low)

### waste/01#F3 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division of the country and belongs in `CountrySubentity` ("The territorial division of a country, such as a county or state, expressed as text"). The world itself uses `CountrySubentity` for Bayvarra's states (Coastal State / Upland State, 799 occurrences over `*.xml`, counted by the parties part), so Urvanian provinces are encoded differently. `<cbc:Region>Province of` occurs 219 times in 104 examples (`grep -ro --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l` and `grep -rl … | wc -l`, re-counted in the merge).
- Condition: no address of this example carries a province in `Region`; where the province is given it is in `CountrySubentity` (optionally with `CountrySubentityCode`), consistently for all four addresses.
- Options: move the value to `CountrySubentity` for every Urvanian address, as for Bayvarra (preferred: the element made for it, and all countries encoded alike); or drop it where the postal zone already locates the address.
- Needs decision: no
- From: broad (F3), parties (F1), context (F2)

### waste/01#F4 · Medium · The notification does not identify the waste by code, nor state the planned total quantity and period
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- Why: the document is "used to notify the competent authorities of planned movements of waste", and its `Shipment` is "the relevant shipment information describing the planned transport and the waste material". What the authority decides on (Basel Annex V A and notification form; own knowledge) is the waste identified by its classification (Basel Annex IX entry, e.g. B3011 for non-hazardous plastic waste, or a national/EWC code), the intended total quantity (tonnes, m3) and the period of the planned shipments. Here the waste is described only in free text (no `cac:Item/cac:CommodityClassification` in the goods item), no net quantity is given, and the only quantity is a gross weight of 40 000 kg which by definition ("the weight of the goods plus packaging plus transport equipment") includes equipment and does not say whether it is per shipment or for all twelve (see F6). No planned period is given (e.g. `cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod`). R3 is stated only as the scope of the facility's authorisation, not as the operation of this notification.
- Condition: the notification identifies the waste by a code from a stated classification, states the estimated total quantity of waste (net) for the notified shipments and the planned period of the shipments; any gross weight is clearly per shipment.
- Options: (preferred) add a `CommodityClassification` with the waste code on the goods item's `Item`, a net weight that is clearly the total for the notification, and a planned period under `Shipment/Delivery`, all within the existing `Shipment`; alternatively state the per-shipment quantity and keep `ConsignmentQuantity` as the multiplier, saying so in `cac:Shipment/cbc:Information`; or, if the world deliberately keeps waste coding out, say so in the description.
- Needs decision: no
- From: broad (F4), logistics (F1), context (F8, Low)

### waste/01#F5 · Low · 40 000 kg gross for one road shipment of bagged polyethylene waste is hardly plausible
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `4923`
- XPath: `/WasteNotification/cac:Shipment/cac:GoodsItem/cbc:Description` = `Mixed polyethylene production waste, sorted, in big bags`
- Why: the carrier is a road haulier (ISIC 4923), so one shipment is one lorry load. Figures (own knowledge, not in the document): gross combination weight limit 40 t (44 t in some countries); tractor about 7.5 t, curtain-side semi-trailer about 7 t, payload about 25 t; trailer inner space 13.6 × 2.45 × 2.7 m = 90 m3; big bag about 0.9 × 0.9 × 1.1 m = 0.89 m3; bulk density of sorted PE production waste 0.05–0.2 t/m3 (film, offcuts) to 0.25–0.45 t/m3 (regrind, lumps). Calculation (logistics part, redone in the merge): 15 × 2 = 30 bags per layer, two layers = 60 bags = 53 m3; at 0.45 t/m3 that is 24 t of waste at most. If the trailer counts as "transport equipment" (UBL's `TransportEquipment` covers trailers; the tractor is a `TransportMeans`), 40 t gross leaves about 33 t of bagged waste, above the payload and needing 33 / 0.45 = 73 m3 (about 82 bags where 60 fit). If the 40 t is the total of twelve shipments, it is 3.3 t per load, implausibly little. Counter-argument (broad part): 40 t equals the usual maximum gross combination weight of a five-axle articulated vehicle, so as an estimate for a fully loaded vehicle including the tractor it is plausible (40 − 14.5 = 25.5 t of waste, at the limit of what 53–58 m3 of regrind in bags holds). Which reading applies cannot be settled from the document, hence a decision.
- Condition: the weight stated for one shipment can be carried by one road vehicle and fits its loading space at the bulk density of the described waste (for bagged PE waste roughly 10–24 t net), or the document states that the figure is the total of the notified shipments and that total is consistent with twelve loads.
- Options: (preferred) state a per-shipment weight of about 20 t and give the total separately (F4); alternatively keep 40 t and describe it as the total for the notification, or describe the waste as denser (baled, compacted).
- Needs decision: yes
- From: logistics (F2)

### waste/01#F6 · Low · The planned shipment carries the IDs of the first actual movement, although the notification covers twelve
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- XPath: `/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`
- XPath: `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`
- XPath: `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:GrossWeightMeasure` = `38200`
- Why: `ConsignmentQuantity` is the "Estimated total number of shipments for this Notification Document" (12), while `Shipment` is "The relevant shipment information describing the planned transport and the waste material". The movement that reports the first of the twelve (`02-WasteMovement.xml:/WasteMovement/cbc:SequenceNumberID` = `1`) uses the same shipment and consignment IDs (`02-WasteMovement.xml:/WasteMovement/cac:Shipment/cbc:ID` = `VI-SH-26-0205`, `02-WasteMovement.xml:/WasteMovement/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0206`) with 38 200 kg instead of 40 000 kg. One identifier thus names both the planned set (or a typical planned load) and one actual load; movements 2–12 would either reuse it or need IDs the notification does not know. A planned weight may differ from an actual one, so the weights alone are no contradiction; the identifiers do not say which object is meant.
- Condition: either the notification's `Shipment` describes the whole notified movement with its own identifier (and a weight for all shipments together or clearly per shipment) and each movement has its own shipment/consignment ID; or the documents state that the notification's shipment is shipment 1 and its weight is the planned value of that load.
- Options: (preferred) give the notification's shipment an identifier for the notified movement set, and each movement its own shipment ID, so twelve movements can be told apart; alternatively keep the shared IDs and state in `cac:Shipment/cbc:Information` that the figures are planned per-shipment values.
- Needs decision: yes
- From: logistics (F3), context (F5)

### waste/01#F7 · Low · The shipment names no place of loading or delivery
- XPath: `/WasteNotification/cac:Shipment/cbc:ID` = `VI-SH-26-0205`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- Why: the planned transport has no `ShipmentStage`, `Delivery`, `ExportCountry` or exit/arrival location; the only places are party addresses. A notification describes the planned route of the waste (own knowledge of the Basel notification form: places of export, transit, entry and exit, and the facility's actual site). If the movement is domestic (F1) the loading and delivery places still identify where the waste is taken over and where it is recovered; if it is transboundary, the countries of export and import and the border crossing are missing as well.
- Condition: the shipment states where the waste is loaded and where it is delivered (and, if transboundary, the countries of export and import or the border crossing), consistent with the role of `CustomsParty`.
- Options: (preferred) add `cac:Shipment/cac:Delivery/cac:DeliveryLocation` (the facility) and a loading place on a `ShipmentStage`, plus `ExportCountry` and `LastExitPortLocation`/`FirstArrivalPortLocation` if the story becomes transboundary; alternatively rely on the party addresses and make the story explicitly domestic.
- Needs decision: yes
- From: logistics (F4)

### waste/01#F8 · Low · Notifier's capital-market and service-provider master data copied into the notification
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: a waste notification tells the authority who produces, notifies, carries and recovers the waste. Valdara's listed shares, share capital and its warehousing-and-despatch provider Castrano Logistics play no part in it; Castrano is not the carrier (Trasvia Haulage) and appears nowhere else in the document, so a "despatch" service provider even blurs who moves the waste. This is Valdara's master data (section 4.8): `XU0001042501` and `VI-SP-2026-01` each occur in 75 examples (`grep -rl --include='*.xml' -F`, re-counted in the merge for the ISIN).
- Condition: the sender carries only data the notification uses, or the document gives a reason for each (e.g. Castrano loads the waste).
- Options: remove `SecurityListing`, `CorporateStockAmount`, `FullyPaidSharesIndicator` and `ServiceProviderParty` (preferred); or, if Castrano handles the waste, give it a role in the shipment consistent with the carrier.
- Needs decision: no
- From: broad (F7), parties (F4), context (F3)

### waste/01#F9 · Low · Contacts that do not fit the notifier, the authority and the facility
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender is the notifier, "responsible for providing the Waste Notification information"; the authority contacts it about the waste, its classification and the permit. Valdara's sales order desk (`Customer service officer`, `order@valdara.example`) takes customers' orders; one would expect an environmental/HSE, waste or plant contact. Valdara carries this same contact in all its 75 examples whatever its role (`grep -rl --include='*.xml' -F 'order@valdara.example'`; "Order desk" occurs in 87 examples), so it is one master contact, not one chosen for the role. The authority's contact is a border office, while a notification is handled by the office that grants waste-movement consents. For the recovery facility, broad expected a plant/operations contact rather than customer service in Sales; parties argued that Rinova's customer service is the desk that accepts waste from customers such as Valdara. The merge keeps that place as the weakest of the four (see "Considered and refuted").
- Condition: the notifier's contact answers for the waste and the notification; the authority's contact is the office that handles waste notifications; the facility's contact (if kept) is one the authority can reach about the recovery operation.
- Options: role-specific contacts: an environmental/waste contact for Valdara, a waste-permits office for the authority, and an operations contact for Rinova (preferred); or omit the contacts.
- Needs decision: no
- From: broad (F6), parties (F5), context (F3)

### waste/01#F10 · Low · Customs administration described as a company in the commercial register
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the receiver is a public administration (`IndustryClassificationCode` 8411, General public administration activities). A government authority is not registered in a commercial register and has no liquidation status (`CompanyLiquidationStatusCode`, "A code signifying the party's liquidation status"). The same description is given to all four public bodies of the world (Customs Administration of Urvania, Customs and Border Service of Bayvarra, Island Customs Service, Maritime Administration of Lisavu), in 23 examples (parties part, `grep -rlE --include='*.xml'` on their `RegistrationName`).
- Condition: the authority's legal entity, if present, carries no commercial-register scheme and no liquidation status, or a registration scheme that fits a public body.
- Options: keep only the registration name (and an identifier from a register of public bodies, if the world has one) (preferred); or drop `PartyLegalEntity` for the authority.
- Needs decision: no
- From: broad (F5), parties (F6), context (F4)

### waste/01#F11 · Low · VAT registrations of every party in a notification that does nothing with tax
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007337656`
- Why: the notification carries no amount, price or tax. `PartyTaxScheme` ("A tax scheme applying to this party") is given in full (VAT, `TaxLevelCode`, tax currency XUF, jurisdiction) for four parties, and nothing in the document uses it; the parties are already identified by register IDs and customs trader IDs. The receiving authority's own VAT registration is the least explicable. Counter-argument considered (money part): an authority might want the notifier's tax ID; but the notifier is identified three ways already. Of the 241 examples that carry `cac:PartyTaxScheme`, 154 are of non-financial document types (money part, classified by root element; the 241 re-counted in the merge).
- Condition: every `PartyTaxScheme` in the notification has a stated reason in this document, or is absent.
- Options: (a) preferred: remove `PartyTaxScheme` from all parties; (b) keep it only for the notifier if the world's notification rules require a tax ID, and remove it from the authority and the carrier.
- Needs decision: no
- From: money (F1), parties (F4, the authority's VAT number), context (F4, the authority's VAT number)

### waste/01#F12 · Low · Carrier's authorisation is a general international haulage licence, not a waste-carrier authorisation
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: in a waste notification the authority checks that the intended carrier may carry waste (the Basel notification form asks for the carrier's registration; own knowledge). The carrier shows only its general road haulage licence, copied into all 15 Trasvia examples (`grep -rl --include='*.xml' -F 'International road haulage'`, re-counted in the merge); it says nothing about waste. That the licence is "international" for a domestic movement is not itself wrong (an international licence covers domestic carriage; broad's refutation, kept below), so this finding is about the kind of authorisation, not its scope.
- Condition: the carrier's authorisation in this document permits it to carry this waste, or the authorisation is absent.
- Options: (preferred) give Trasvia a waste-carrier registration in the world and show that one here; or omit `PartyAuthorization` from the carrier in this document.
- Needs decision: yes
- From: parties (F8); context (F1, the word "International")

### waste/01#F13 · Low · Recovery facility and carrier both registered on 1 January 1996
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday on which registers do not register companies, and the same date is given to 25 different legal entities in Urvania and Bayvarra (parties part, script over `world/examples/*/*.xml`; the date occurs in 181 files, re-counted in the merge with `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01'`), while other parties have individual dates (Valdara `1962-04-12`). It looks like a default value (rule "no fillers").
- Condition: each party's `RegistrationDate` is the date its registration took effect in the world, or is absent.
- Options: (preferred) give each company its own plausible date; or remove the element. If the world's story has all registers re-founded on 1996-01-01, record that and dismiss this finding.
- Needs decision: yes
- From: parties (F7)

### waste/01#F14 · Low · Notification type: "Recovery" chosen where the list also has "General notification" for several shipments
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cbc:ConsignmentQuantity` = `12`
- Why: the world list `WasteNotificationType` has `RECOVERY` ("Waste for recovery operations (R codes)."), `DISPOSAL` and `GENERAL` ("Several shipments of the same waste over up to a year."). This notification covers 12 shipments of the same waste, which is the case `GENERAL` names, and it is also for recovery. The list mixes two independent dimensions (recovery/disposal and single/general are two separate boxes in the Basel notification form; own knowledge), so one code cannot say both; the chosen code leaves out that this is a general notification.
- Condition: the type of the notification (recovery, and general for several shipments) is fully expressed, or it is decided which dimension the code carries and the other is expressed elsewhere.
- Options: (a) keep `RECOVERY` and decide that the multi-shipment nature is carried by `ConsignmentQuantity`; (b) use `GENERAL` and rely on `RecoveryFacilityParty` and the R code for "recovery"; (c) split the world list into two dimensions. No strong preference; this is a code-list decision.
- Needs decision: yes
- From: context (F6)

### waste/01#F15 · Low · The contract reference does not say what it is
- XPath: `/WasteNotification/cac:DocumentReference/cbc:ID` = `VI-WASTE-CONTRACT-26`
- Why: `DocumentReference` is "A reference to a relevant document associated with this Waste Movement" (sic, in the WasteNotification model). Only the ID's wording suggests that it is the contract between notifier and recovery facility, which a notification has to be backed by (Basel Annex V A; own knowledge), so the reference has a reason to be here; but it has no `DocumentTypeCode`, `DocumentType` or `IssueDate`. No example carries this ID (re-checked over `*.xml`), which is acceptable for a contract. A `*DocumentReference` whose only child is `cbc:ID` occurs 555 times in 177 of 250 examples (logistics part, counted with lxml).
- Condition: the reference states what kind of document it is (code or text) and, ideally, its issue date.
- Options: add `cbc:DocumentType` (e.g. "Contract for recovery of production waste") or a `DocumentTypeCode` from the world's list, and `cbc:IssueDate` (preferred).
- Needs decision: no
- From: broad (F8), logistics (F5), context (F9)

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` check digit correct (all parts).
- `MarketCode` `XFER` is not in the ISO 10383 MIC file (`world/codelists/sources/iso10383/ISO10383_MIC.csv`); ICD `0990` is not in the Peppol ICD list (`world/codelists/sources/peppol/ICD.xml`, highest 0248); `+999` is not an ITU country code (broad, parties).
- `ConsignmentQuantity` `12` EA ("Estimated total number of shipments") equals `02-WasteMovement.xml:/WasteMovement/cbc:ConsignmentQuantity` = `12`; the notification ID `VI-DOC-26-0204` is the one 02 references.
- Notifier, waste producer, sender and signatory are the same party (Valdara, `XU-R-104274`); the receiver is the `CustomsParty` (`XU-R-105507`), consistent with the notification going to the authority (role question in F1).
- The same parties are described identically in 01, 02 and 03 (Valdara, Rinova, Customs Administration of Urvania, Trasvia): address, tax scheme, legal entity, contact, language, electronic address, authorisations (parties part, c14n comparison).
- Legal forms and sizes: `SUA` public limited company, LARGE, listed, 250 000 000 XUF capital for Valdara; `SRU` private limited company, SMALL for Rinova and Trasvia; plausible.
- `WasteNotificationTypeCode` `RECOVERY` is in the world list the CVA binds to the element; R3 (Basel Annex IV) fits recycling of polyethylene, and agrees with the facility's purpose "Recovery of non-hazardous plastic waste" and ISIC 3830.
- `HazardousRiskIndicator` `false` fits sorted, non-hazardous PE production waste.
- Validity periods: recovery permit until 2029-12-31, haulage licence until 2030-06-30, both after the issue date 2026-03-23 and the movement of 2026-04-02.
- Order of dates in the flow: notification 2026-03-23 09:28, movement 2026-04-02 12:34, invoice 2026-04-04 12:44.
- Bilingual renderings (`qau`, `en-XU`) carry the same content; `qau` lies in the ISO 639-2 local-use range.
- Money lens: no amounts, prices, taxes on transactions, payment means or terms in the notification; the VAT registrations agree with 02 and 03 (`03-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007318479`, `03-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `XU007299291`); tax currency XUF fits country XU.
- Merge re-checks: the XML was re-read; every count re-counted in the merge is marked as such above.

## Considered and refuted
- `/WasteNotification/cac:SenderParty/cbc:IndustryClassificationCode` = `3100`: a furniture manufacturer producing polyethylene production waste looked odd — refuted because plastic parts, foils, foams and packaging in furniture production yield PE waste (from broad, parties, context).
- `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian-style text under `languageID` `en-XU` — refuted because the world uses these as the established English-usage names of Urvanian places (as with `Ferrano`) (from broad).
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`: an international licence for a domestic movement — refuted because a licence for international haulage also covers domestic carriage (from broad). Context used the word as evidence for F1 and parties made the kind of authorisation F12; the merge keeps both there but not the scope as a problem of its own.
- `/WasteNotification/cac:Signature`: signature with ID and signatory only — refuted because the elements are optional and the signatory (the notifier) is the right party (from broad).
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`: an R code unfit for plastics — refuted because R3 covers recycling/reclamation of organic substances, under which plastics recycling is reported (from parties, logistics).
- `/WasteNotification/cac:SenderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ISO 6523 ICD — refuted because 0990 is not in the ICD list (from parties).
- `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: a real country code — refuted because ITU has not assigned +999 to a country (from parties).
- `/WasteNotification/cac:RecoveryFacilityParty/cac:Contact/cbc:Department` = `Sales`: a contact unfit for the facility — refuted by parties because the facility's customer service accepts waste from customers. The merge does not fully share the refutation (broad flagged it) and keeps the place in F9 as its weakest line, with both arguments.
- `/WasteNotification/cac:NotifierParty/cac:PartyName/cbc:Name` = `Valdara Industries`: the notifier lacks address and contact — refuted because the same party is fully described as `SenderParty` (from parties).
- `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Postbox` = `PB 18`: post box together with a street address — refuted because that is a legitimate postal address of an authority (from parties).
- `/WasteNotification/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`: a customs-trader ID with no use — refuted while the notification goes to the customs administration, which knows the trader ID; it falls with F1 (from parties).
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cac:ValidityPeriod/cbc:EndDate` = `2029-12-31`: checked against the issue date — the permit is valid for the notified movements (from parties).
- `/WasteNotification/cbc:ConsignmentQuantity` = `12`: a count of consignments rather than shipments, or "each" as unit — refuted because the element is defined as "Estimated total number of shipments for this Notification Document" and 12 EA is such a count (from logistics, context).
- `/WasteNotification/cac:Shipment/cbc:GrossWeightMeasure` = `40000`: a gross weight as the wrong measure — refuted as a separate finding; the missing net/total quantity is F4, the magnitude F5 (from logistics).
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty`: a carrier premature in a notification — refuted because the notification's shipment describes the planned transport, and the intended carrier is part of it (from logistics).
- `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Telefax` = `+999 1 041 326 0018`: a fax number as filler — refuted because customs offices commonly list fax for paper procedures; the contact itself is in F9 (from context).
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`: the facility's authorisation as master data — refuted because a notification must show that the facility is authorised for the operation (from context).
- `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`: the carrier's licence as filler — refuted because a carrier authorisation is relevant to a waste movement; its kind is F12 (from context).
- `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: an amount in a document without financial content — refuted for the money lens (not a transaction amount); it is part of F8 (from money).

## Changed in the merge
- broad/F1 (High) + parties/F2 (Medium) + context/F1 (Medium) → F1: combined at Medium, because the contradiction runs through the definitions of `CustomsParty` and of the type-code list (elements used for a meaning their definition does not cover, section 6 Medium), not between two values of the document; the "Border office" contact and the list description added as evidence; the carrier's "International" licence demoted from an XPath line to context in "Why" (its scope is not wrong, see "Considered and refuted"); all three option sets kept, with the merge's preference.
- context/F7 (Low) → F2: raised to Medium with broad/F2 and parties/F3, because `DisposalFacilityParty` names a party in a role its definition does not cover.
- context/F8 (Low) → F4: raised to Medium with broad/F4 and logistics/F1, because the notification's purpose depends on the waste's identification and quantity; Basel code written as B3011 (the current Annex IX entry for non-hazardous plastic waste since 2021, own knowledge) instead of broad's B3010.
- logistics/F2 → F5: broad's counter-argument (40 t is the usual maximum gross combination weight, so plausible as a full-vehicle estimate) added; "Needs decision" changed from no to yes, because the merge cannot settle which reading of the gross weight applies.
- logistics/F3 + context/F5 → F6: combined; wording from both.
- logistics/F4 → F7: the transboundary-framing part is covered by F1; this finding now stands on the missing loading and delivery places; the bare `/WasteNotification/cac:Shipment` XPath line replaced by its ID so the value can be checked.
- broad/F7 + parties/F4 + context/F3 → F8 (master data) and F9 (contacts): context/F3 combined both; split so each finding has one condition. The authority's VAT number from parties/F4 and context/F4 moved to F11.
- broad/F6 + parties/F5 + context/F3 (contact part) → F9: grouped; the facility's `Sales` line from broad kept despite parties' refutation, as the weakest place, with both arguments.
- broad/F5 + parties/F6 + context/F4 → F10: grouped; the authority's VAT registration from context/F4 moved to F11.
- money/F1 → F11: the authority's VAT number from parties/F4 and context/F4 joined.
- parties/F8 → F12: wording now separates the kind of licence (the finding) from its scope (refuted by broad).
- broad/F8 + logistics/F5 + context/F9 → F15: grouped.

## Outside this review
- Whether a notification issued on 2026-03-23 could, under the world's procedure, be consented in time for the first movement reported on 2026-04-02 (`02-WasteMovement.xml`) is a timeline question across documents (broad). The missing consent itself is a finding in 02's review.
- Whether Trasvia Haulage (`XU-R-104822`, also carrier in the road flow) had a vehicle free for the waste movements on the dates of this flow is a cross-flow capacity and timeline question (logistics).
- In other flows the same Urvanian parties are rendered with `languageID="en-XB"` on English texts and without the `qau` legal form (e.g. `plastics/01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` for Rinova; also Valdara in 30 files, Trasvia in 5, Castrano in 3); whether that is right lies in those examples (parties).
- Context noted the physics of 40 000 kg / 38 200 kg as a question for the logistics part; it is F5 here and a finding in 02's review.
