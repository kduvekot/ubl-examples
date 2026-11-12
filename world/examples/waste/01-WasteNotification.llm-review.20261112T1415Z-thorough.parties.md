# LLM review: 01-WasteNotification.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### waste/01#F1 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located"; an administrative subdivision of a country (a province) belongs in `CountrySubentity` ("The territorial division of a country, such as a county or state, expressed as text"). The world itself does this for Bayvarra (`CountrySubentity` = Coastal State / Upland State, 799 occurrences over `*.xml`), so Urvanian provinces are encoded differently from Bayvarran states. The same value occurs 219 times in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of Ferrano'`, summed; `grep -rl` for the file count).
- Condition: no address in this example carries a province in `Region`; where the province is given it is in `CountrySubentity` (optionally with `CountrySubentityCode`), consistently for all four addresses.
- Options: (preferred) move the province to `CountrySubentity` for every Urvanian address, as for Bayvarra, so all three countries are encoded alike; or drop the province where the postal zone already identifies it.
- Needs decision: no

### waste/01#F2 · Medium · Customs administration as the competent authority for a movement that stays inside Urvania
- XPath: `/WasteNotification/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- XPath: `/WasteNotification/cac:SenderParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`
- Why: `WasteNotification/CustomsParty` is defined as "The competent authority granting a permit to export or import the waste", and the document as "used to notify the competent authorities of planned movements of waste". The waste producer and notifier (Valdara, Via delle Officine 17, Ferrano) and the recovery facility (Rinova, Via del Riciclo 31, Ferrano) are both in Urvania, in the same town; nothing in the example (no route, location, transit country or note) says that the waste leaves the country. A movement without export or import has no export/import permit, and no customs authority to grant one. Under the Basel Convention (own knowledge) the competent authorities of the countries of export, transit and import are the environmental authorities; customs only controls at the border. The receiver's contact (`Border office`, see F5) adds to the impression that the authority was chosen for a border crossing that does not happen.
- Condition: either the movement is transboundary and the example says so (a disposal/recovery facility or route outside Urvania), with `CustomsParty` the authority that grants the export/import permit; or the movement is domestic and the authority receiving the notification is a party whose role is to permit domestic waste movements, not the customs administration.
- Options: (a) introduce a competent waste/environment authority of Urvania as `ReceiverParty`/`CustomsParty` (preferred if the story is domestic recovery; the element name is the only place for the competent authority in this document); (b) make the movement transboundary (e.g. recovery in Bayvarra), which changes the flow's story; (c) keep customs only if the world's story makes the Urvanian customs administration the competent authority for waste movements, and then say so somewhere in the world.
- Needs decision: yes

### waste/01#F3 · Medium · Rinova is named as disposal facility in a recovery notification
- XPath: `/WasteNotification/cac:DisposalFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyName/cbc:Name` = `Rinova Recovery`
- XPath: `/WasteNotification/cbc:WasteNotificationTypeCode` = `RECOVERY`
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- Why: `DisposalFacilityParty` is "The Party disposing of the waste material"; `RecoveryFacilityParty` is "The Party recovering the waste material". The notification is of type Recovery and Rinova's only authorization is for R3 (recycling/reclamation of organic substances, Basel Annex IV), a recovery operation; nothing says that any part of the waste is disposed of (a D operation). Naming the same party in both roles says that Rinova both disposes of and recovers this waste, which the type code and the permit contradict. In the Basel notification form (own knowledge) the facility is either a disposal or a recovery facility, according to the operation notified.
- Condition: `DisposalFacilityParty` is present only if a disposal operation is part of the notified movement (and then with an authorization for it); otherwise only `RecoveryFacilityParty` identifies Rinova.
- Options: (preferred) remove `DisposalFacilityParty`; or, if residues are to be disposed of, name the party that does that with its own D-operation authorization.
- Needs decision: no

### waste/01#F4 · Low · Notifier's capital-market and service-provider data copied into the notification
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/WasteNotification/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/WasteNotification/cac:SenderParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: A waste notification tells the authority who produces, notifies, carries and recovers the waste. Valdara's share capital, its listed shares on the Ferrano Stock Exchange and its warehousing-and-despatch provider Castrano Logistics play no part in it: Castrano is not the carrier (that is Trasvia Haulage) and appears nowhere else in the document, so naming a "despatch" service provider in a waste notification even blurs who moves the waste. The customs administration's VAT registration is likewise not used by the notification. The same Valdara block (`Ordinary shares of Valdara`, `VI-SP-2026-01`) occurs in 75 examples (`grep -rl --include='*.xml' -F`), which points to master data copied into every document (section 4.8).
- Condition: every party detail present has a use in a waste notification; in particular no share capital, security listing or unrelated service provider of the notifier, and no tax registration of the authority, unless the example gives the reason.
- Options: (preferred) leave these elements out of the notification's parties; or, if a service provider is meant to act for the notifier in the movement, name it in a role the notification uses and make it consistent with the carrier.
- Needs decision: no

### waste/01#F5 · Low · Contacts that do not fit the notifier and the competent authority
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:Contact/cbc:Name` = `Border office`
- Why: The sender is the notifier, "responsible for providing the Waste Notification information"; the authority will contact the notifier about the waste, its classification and the permit. A sales order desk (`Customer service officer`, `order@valdara.example`) is the contact for customers placing orders, not for a waste producer's environmental obligations (one would expect e.g. environmental/HSE or plant management). The authority's contact is a border office, while a notification is handled by the office that grants waste-movement consents. Valdara carries this same order-desk contact in every one of its 75 examples, whatever its role (buyer, seller, notifier, tenderer), which shows it is one master contact rather than one chosen for the role.
- Condition: the notifier's contact is one that answers for the waste and the notification; the authority's contact is the office that handles waste notifications.
- Options: (preferred) give Valdara a role-specific contact for waste/environment matters and the authority a waste-permits office; or omit the contacts.
- Needs decision: no

### waste/01#F6 · Low · Customs administration described as a company in the commercial register
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/WasteNotification/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The receiver is a public administration (`IndustryClassificationCode` 8411, General public administration activities). A government authority is not registered in a commercial register and has no liquidation status (`CompanyLiquidationStatusCode`: "A code signifying the party's liquidation status"). The same description is given to all four public bodies of the world (Customs Administration of Urvania, Customs and Border Service of Bayvarra, Island Customs Service, Maritime Administration of Lisavu), in 23 examples (`grep -rlE --include='*.xml'` on their `RegistrationName`).
- Condition: the authority's legal entity, if present, describes a public body: no commercial-register scheme and no liquidation status, or a registration scheme that fits public bodies.
- Options: (preferred) keep only the registration name (and an identifier from a register of public bodies if the world has one); or drop `PartyLegalEntity` for the authority.
- Needs decision: no

### waste/01#F7 · Low · Recovery facility and carrier both registered on 1 January 1996
- XPath: `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 1 January is a public holiday on which no register registers companies, and the same date is given to 25 different legal entities in Urvania and Bayvarra (a script over `world/examples/*/*.xml` collecting `PartyLegalEntity/RegistrationDate` per `RegistrationName`; 181 files), while other parties have individual dates (Valdara `1962-04-12`). This looks like a default value rather than each company's registration date (rule "no fillers").
- Condition: each party's `RegistrationDate` is the date its registration took effect in the world, or is absent.
- Options: (preferred) give each company its own plausible date; or remove the element where the world has no date. If the world's story has all registers re-founded on 1996-01-01, record that and dismiss this finding.
- Needs decision: yes

### waste/01#F8 · Low · Carrier's authorization is a general international haulage licence, not a waste-carrier authorization
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- XPath: `/WasteNotification/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: In a waste notification the authority checks that the intended carrier may carry waste (the Basel notification form asks for the carrier's registration, own knowledge). The carrier shows only its general international road haulage licence, which is the authorization copied into all 15 Trasvia examples (`grep -rl --include='*.xml' -F 'International road haulage'`); it says nothing about waste, and the movement is domestic (F2), so an international licence is not what this document needs.
- Condition: the carrier's authorization in this document is one that permits it to carry this waste, or the authorization is absent.
- Options: (preferred) give Trasvia a waste-carrier registration in the world and show that one here; or omit `PartyAuthorization` from the carrier in this document.
- Needs decision: yes

## Checked and consistent
- The same parties (by `PartyIdentification/ID`) are described identically in 01, 02 and 03: Valdara (XU-R-104274), Rinova (XU-R-104548), Customs Administration of Urvania (XU-R-105507), Trasvia (XU-R-104822): postal address, address ID, tax scheme, legal entity, contact, language, electronic address and authorizations compared element by element (c14n comparison over all `*.xml` of the flow).
- Notifier, waste producer and signatory are the same party (Valdara), as for a producer that notifies its own waste; `SignatoryParty` = `SenderParty`.
- Registration names and legal forms agree with the legal form codes (`SUA` public limited company for Valdara, `SRU` private limited company for Rinova and Trasvia); `EntitySizeCode` LARGE for a listed company with 250 000 000 XUF capital, SMALL for Rinova and Trasvia: plausible.
- ISIN `XU0001042501` check digit OK (`check_ids.py`); `MarketCode` `XFER` is not in the ISO 10383 MIC list (`world/codelists/sources/iso10383/ISO10383_MIC.csv`), so not a real code.
- Party identifiers have the kinds their schemes name (register ID in `PartyIdentification` and `CompanyID`, tax number in `PartyTaxScheme/CompanyID`, customs trader ID as additional identification); the electronic address IDs derive from the register IDs.
- Bilingual renderings: street, city and legal-form texts carry `qau` and `en-XU` and are the same content in both (e.g. `Ruldraz`/`Ferrano`); `Language/ID` `qau` lies in the ISO 639-2 local-use range.

## Considered and refuted
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`: suspected wrong operation for plastic waste — refuted because Basel Annex IV R3 covers recycling/reclamation of organic substances not used as solvents, which includes plastics.
- `/WasteNotification/cac:SenderParty/cbc:IndustryClassificationCode` = `3100`: suspected mismatch between a furniture maker and polyethylene production waste — refuted because a furniture manufacturer produces PE waste from foils, foams and plastic parts.
- `/WasteNotification/cac:SenderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: suspected a real ISO 6523 ICD — refuted because 0990 is not in the ICD list (`world/codelists/sources/peppol/ICD.xml`, highest 0248).
- `/WasteNotification/cac:SenderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: suspected a real country code — refuted because ITU has not assigned +999 to a country.
- `/WasteNotification/cac:RecoveryFacilityParty/cac:Contact/cbc:Department` = `Sales`: suspected a contact unfit for the recovery facility — refuted because the facility's customer service is the desk that accepts waste from customers such as Valdara; it is a fitting contact for the facility in this role.
- `/WasteNotification/cac:NotifierParty/cac:PartyName/cbc:Name` = `Valdara Industries`: suspected the notifier lacks the address and contact the authority needs — refuted because the same party is fully described as `SenderParty` in the same document.
- `/WasteNotification/cac:ReceiverParty/cac:PostalAddress/cbc:Postbox` = `PB 18`: suspected a post box combined with a street address — refuted because a postal address with both a post box and the building address is a legitimate rendering for an authority.
- `/WasteNotification/cac:SenderParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`: suspected a customs-trader ID with no use — kept out of F4 because, as long as the notification goes to the customs administration (F2), the trader ID is the identifier that authority knows; it falls with F2.
- `/WasteNotification/cac:RecoveryFacilityParty/cac:PartyAuthorization/cac:ValidityPeriod/cbc:EndDate` = `2029-12-31`: checked against the notification date 2026-03-23 — the permit is valid for the notified movements.

## Outside this review
- In other flows the same Urvanian parties are rendered with `languageID="en-XB"` on English texts and without the `qau` legal form (e.g. `plastics/01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` for Rinova, also Valdara in 30 files, Trasvia in 5, Castrano in 3); whether that is right lies in those examples.
