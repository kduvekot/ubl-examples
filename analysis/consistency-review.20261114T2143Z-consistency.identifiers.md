# Consistency review: identifiers

Run: `20261114T2143Z-consistency` · Review date: 2026-11-15 · Topic: identifiers
Examples: 250 in 18 flows, at commit 9bdf89a (claude/stoic-noether-5pboei); tables current for that commit (extract_tables.py --check: "current (250 examples and the script unchanged)").
Inputs: the XML examples, the extraction tables, the merged per-example reviews. No world data, generators or companion documentation were read. Also read: `analysis/review-merge-decisions.md`, the conditions, timelines and equipment files of this run (their "For other topics" notes), the output of `check_consistency.py` and of `check_ids.py` over all 250 examples, and the code lists in `world/codelists/gc` for the meaning of codes. Statements about real registers rest on own knowledge where said.

## What is expected

Every finding below, and every entry under "Considered and refuted", "Leads" and "Cannot be told", is looked into and ends either resolved (its condition holds in the XML) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by the owner first, because the fix changes the world's identifier rules or master data (who numbers what, and how), not only an encoding. This review describes what is inconsistent in the identifiers as the documents state them; it does not say where or how the examples are produced.

## The world as the documents state it

### Scheme register

Every `schemeID` in use (identifiers.csv, 13526 identifier leaves; the 7928 leaves without a schemeID are document numbers, line IDs, party-internal codes and the like). "Identifies" lists the parent/element pairs with their number of uses.

| schemeID | Identifies (element: uses) | Value format | Values | Uses | Files | Flows | Example |
|---|---|---|---:|---:|---:|---|---|
| `urn:ubl-examples:world:XB:register` | PartyIdentification/ID: 768; PartyLegalEntity/CompanyID: 356; MainQualifyingParty/BusinessIdentityEvidenceID: 2 | `99999999` | 22 | 1126 | 216 | air,carnet,contest,cotton,energy,furniture,mast,packaging,plastics,rail,retail,road,sea,tender,utilities,wood | `20410137` |
| `urn:ubl-examples:world:XU:register` | PartyIdentification/ID: 527; PartyLegalEntity/CompanyID: 176; MainQualifyingParty/BusinessIdentityEvidenceID: 1 | `AA-A-999999` | 14 | 704 | 127 | air,carnet,contest,energy,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `XU-R-104137` |
| `UN/EDIFACT EDED 5153` | TaxScheme/ID: 658 | `AAA` | 4 | 658 | 242 | all 18 | `EXC` |
| `ISO 639` | Language/ID: 644; AdditionalNoticeLanguage/ID: 4; DefaultLanguage/ID: 2; RequestedLanguage/ID: 1 | `AA`, `AAA` | 3 | 651 | 250 | all 18 | `en` |
| `urn:ubl-examples:world:endpoint` | ElectronicAddress/ElectronicAddressID: 633; DigitalDeliveryChannel/ParticipantID: 4 | `AA:99999999`, `AA:AA-A-999999`, `AA:AA99999` | 47 | 637 | 250 | all 18 | `XB:20410137` |
| `urn:ubl-examples:world:XL:register` | PartyIdentification/ID: 243; PartyLegalEntity/CompanyID: 101 | `AA99999` | 13 | 344 | 64 | air,carnet,cotton,mast,packaging,sea,utilities | `IC41037` |
| `urn:ubl-examples:world:XB:tax` | PartyTaxScheme/CompanyID: 325 | `AA-9999999` | 15 | 325 | 213 | air,contest,cotton,energy,furniture,mast,packaging,plastics,rail,retail,road,sea,tender,utilities,wood | `CO-0900002` |
| `urn:ubl-examples:world:codelist:DimensionAttributeCode` | Dimension/AttributeID: 196; MeasurementDimension/AttributeID: 90; RangeDimension/AttributeID: 7 | `AAAAAA`, `AAAAA`, `AAAAAAAAAA` | 9 | 293 | 66 | air,carnet,furniture,plastics,rail,retail,road,sea,tender,wood | `BENCHLENGTH` |
| `urn:ubl-examples:world:XB:lumeport:address-register` | PostalAddress/ID: 211; DeliveryAddress/ID: 1 | `AAA-AAA-999999` | 16 | 212 | 156 | air,contest,cotton,furniture,mast,packaging,plastics,retail,sea,tender,utilities | `LUM-ADR-000417` |
| `urn:ubl-examples:world:XB:customs-trader` | AdditionalPartyIdentification/ID: 182 | `AA-AA-999999` | 6 | 182 | 176 | air,contest,cotton,energy,furniture,packaging,plastics,rail,retail,road,sea,tender,wood | `XB-TR-410274` |
| `UN/EDIFACT EDED 5305` | TaxCategory/ID: 97; ClassifiedTaxCategory/ID: 63; ApplicableTaxCategory/ID: 16 | `A` | 4 | 176 | 80 | air,cotton,energy,furniture,mast,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `E` |
| `urn:ubl-examples:world:XU:address-register` | PostalAddress/ID: 176 | `9999999999999999` | 14 | 176 | 104 | carnet,contest,energy,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `4160200139820702` |
| `urn:ubl-examples:world:XU:tax` | PartyTaxScheme/CompanyID: 176 | `AA999999999` | 14 | 176 | 104 | carnet,contest,energy,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `XU007289704` |
| `GS1 GLN` | AdditionalPartyIdentification/ID: 156; DeliveryLocation/ID: 5; ActivityOriginLocation/ID: 1 | `9999999999999` | 7 | 162 | 125 | air,contest,furniture,packaging,rail,retail,road,sea,tender,utilities,wood | `9520610900008` |
| `urn:ubl-examples:world:XB:UL:address-register` | PostalAddress/ID: 146; DeliveryAddress/ID: 1 | `AA-AAA-999999` | 5 | 147 | 139 | air,contest,cotton,energy,furniture,mast,plastics,rail,retail,road,sea,tender,wood | `UL-ADR-296778` |
| `ISO 6523` | AdditionalPartyIdentification/ID: 104 | `9999:99999` | 5 | 104 | 94 | carnet,contest,energy,ore,packaging,plastics,rail,road,tender,utilities,waste,wood | `0990:10427` |
| `urn:ubl-examples:world:XL:delivery-point` | PostalAddress/ID: 101 | `99999999` | 12 | 101 | 64 | air,carnet,cotton,mast,packaging,sea,utilities | `23618907` |
| `urn:ubl-examples:world:bank-identifier` | FinancialInstitution/ID: 91; CardAccount/IssuerID: 4 | `AAAAAAAA` | 3 | 95 | 73 | air,cotton,energy,furniture,mast,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `BLUMXBLX` |
| `urn:ubl-examples:world:XU:customs-trader` | AdditionalPartyIdentification/ID: 95 | `AA-AA-999999` | 3 | 95 | 92 | carnet,contest,energy,ore,packaging,plastics,rail,road,tender,utilities,waste,wood | `XU-TR-104274` |
| `urn:ubl-examples:world:account` | PayeeFinancialAccount/ID: 56; FinancialAccount/ID: 21; PayerFinancialAccount/ID: 13; FinancingFinancialAccount/ID: 1 | `AA99AAAA99999999999999`, `AA999999999999999999999999`, `AA99AAAA9999999999999` | 26 | 91 | 71 | air,cotton,energy,furniture,mast,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `XB19BLUM38712001466206` |
| `urn:ubl-examples:world:codelist:OtherAttributeCode` | PhysicalAttribute/AttributeID: 39; FloorSpaceMeasurementDimension/AttributeID: 25; PalletSpaceMeasurementDimension/AttributeID: 25; Condition/AttributeID: 1 … | `AAAAAA`, `AAAAAAAAAA`, `AAAAAAAAAAAA` | 5 | 91 | 42 | carnet,rail,retail,road,sea,tender | `COLOUR` |
| `urn:ubl-examples:world:item` | StandardItemIdentification/ID: 48; AdditionalItemIdentification/ID: 34 | `999999999999` | 8 | 82 | 64 | air,carnet,energy,ore,packaging,plastics,rail,retail,road,sea,tender | `771010000013` |
| `ISO 6166` | SecurityListing/ID: 75; ImmobilizedSecurity/SecurityID: 1 | `AA9999999999` | 1 | 76 | 75 | carnet,contest,energy,ore,packaging,rail,road,tender,utilities,waste,wood | `XU0001042501` |
| `urn:ubl-examples:world:XB:bank-branch` | FinancialInstitutionBranch/ID: 56 | `999999` | 4 | 56 | 48 | air,cotton,energy,furniture,mast,packaging,plastics,retail,road,sea,tender,utilities,wood | `380100` |
| `urn:ubl-examples:world:XL:customs-trader` | AdditionalPartyIdentification/ID: 52 | `AA-AA-999999` | 2 | 52 | 52 | air,cotton,packaging,sea,utilities | `XL-TR-041859` |
| `ISO 11649` | PaymentMeans/PaymentID: 51 | `AA99AAAAA999999`, `AA99AAAAAA999999`, `AA99AAAAAAA999999` | 39 | 51 | 51 | air,cotton,energy,furniture,mast,ore,packaging,plastics,rail,retail,road,sea,tender,utilities,waste,wood | `RF02MSINV260638` |
| `ISO 15459` | TransportHandlingUnit/ID: 25; ActualPackage/ID: 25; ReferencedPackage/ID: 1 | `AAA999999999999999` | 26 | 51 | 2 | rail,road | `KXU104411490000015` |
| `GS1 GTIN` | StandardItemIdentification/ID: 49 | `9999999999999` | 5 | 49 | 40 | air,furniture,packaging,retail,sea | `9520610000012` |
| `urn:ubl-examples:world:XU:property` | StandardPropertyIdentification/ID: 46 | `AA-AA-9999` | 2 | 46 | 46 | carnet,rail,retail,road,sea,tender,wood | `UR-SF-0450` |
| `UN/LOCODE` | PhysicalLocation/ID: 13; Location/ID: 5; LoadingPortLocation/ID: 3; UnloadingPortLocation/ID: 3 … | `AAAAA` | 7 | 37 | 21 | air,cotton,ore,rail,road,sea | `XBLMA` |
| `INCOTERMS` | DeliveryTerms/ID: 36 | `AAA` | 7 | 36 | 34 | air,cotton,furniture,mast,ore,packaging,plastics,rail,retail,road,sea,tender,wood | `CIF` |
| `urn:ubl-examples:world:codelist:TemperatureAttributeCode` | MinimumTemperature/AttributeID: 11; MaximumTemperature/AttributeID: 11; FlashpointTemperature/AttributeID: 4; Temperature/AttributeID: 3 … | `AAAAAAA`, `AAAAAAAAA`, `AAAAAAAAAA` | 7 | 35 | 8 | mast,plastics,road,sea | `AMBIENT` |
| `GS1 SSCC` | PackagedTransportHandlingUnit/ID: 25; TransportHandlingUnit/ID: 8; Package/ID: 1 | `999999999999999999` | 32 | 34 | 4 | air,retail,sea | `095206101230000018` |
| `urn:ubl-examples:world:XU:bank-branch` | FinancialInstitutionBranch/ID: 24 | `99999-99999` | 3 | 24 | 22 | energy,ore,plastics,rail,road,tender,utilities,waste,wood | `03510-41600` |
| `UN Model Regulations hazard class` | HazardousItem/HazardClassID: 12; LoadedHazardousItem/HazardClassID: 6; SecondaryHazard/ID: 4 | `9` | 4 | 22 | 5 | mast | `3` |
| `urn:ubl-examples:world:XU:haulage-licence` | Certificate/ID: 15 | `AA-AAAA-9999-9999` | 1 | 15 | 15 | packaging,road,tender,waste,wood | `XU-HAUL-2020-0877` |
| `urn:ubl-examples:world:XU:waste-permit` | Certificate/ID: 14 | `AA-AAA-9999-9999` | 1 | 14 | 14 | plastics,waste | `XU-ENV-2024-0311` |
| `urn:ubl-examples:world:XB:forestry-register` | Certificate/ID: 7; Certificate/CertificateReferenceID: 7 | `AA-AAA-9999-9999`, `AA-AAA-AAA-9999` | 2 | 14 | 7 | wood | `XB-FOR-2025-0118` |
| `ISO 3166` | TransportMeans/RegistrationNationalityID: 13 | `AA` | 3 | 13 | 12 | air,cotton,mast,plastics,rail,retail,road,sea | `XB` |
| `ISO6346` | TransportEquipment/ID: 10; ReferencedTransportEquipment/ID: 1; ContainingTransportEquipment/ID: 1; GoodsItemContainer/ID: 1 | `AAAA9999999` | 4 | 13 | 8 | cotton,rail,sea | `FRXU1044175` |
| `urn:ubl-examples:world:XL:bank-branch` | FinancialInstitutionBranch/ID: 11 | `999` | 2 | 11 | 9 | cotton,sea,utilities | `001` |
| `urn:ubl-examples:world:vessel` | MaritimeTransport/VesselID: 6 | `AA-A-99999`, `AA-AA-99999` | 3 | 6 | 6 | cotton,plastics,sea | `XB-S-20117` |
| `urn:ubl-examples:world:XB:NT:address-register` | PostalAddress/ID: 6 | `AA-AAA-999999` | 1 | 6 | 6 | energy | `NT-ADR-587853` |
| `GS1 GRAI` | ActualPackage/ID: 6 | `999999999999999999` | 6 | 6 | 1 | retail | `095206100000122217` |
| `urn:ubl-examples:world:codelist:MarketCode` | PricingExchangeRate/ExchangeMarketID: 6 | `AAAA` | 1 | 6 | 6 | tender | `XLMX` |
| `urn:ubl-examples:world:XB:vehicle-register` | RoadTransport/LicensePlateID: 2; RoadTransport/TrailerLicensePlateID: 2; AttachedTransportEquipment/ID: 1 | `AA AA 9999` | 4 | 5 | 2 | retail,sea | `BV CH 0412` |
| `urn:ubl-examples:world:codelist:CardSchemeCode` | CardAccount/NetworkID: 4 | `AAAAAAAAA`, `AAAAAAAA`, `AAAAAAAAAA` | 3 | 4 | 4 | packaging,retail,sea | `CORALCARD` |
| `urn:ubl-examples:world:grid` | OriginAddress/ID: 3 | `99/99` | 1 | 3 | 3 | energy | `33/03` |
| `urn:ubl-examples:world:XL:aircraft-register` | AirTransport/AircraftID: 2 | `AA-AAA` | 1 | 2 | 2 | air,mast | `QL-KXA` |
| `urn:ubl-examples:world:XU:rail-vehicle-register` | RailTransport/RailCarID: 1; ContainedInTransportEquipment/ID: 1 | `99 99 9999 999-9` | 1 | 2 | 1 | rail | `31 46 4521 042-3` |
| `urn:ubl-examples:world:XU:vehicle-register` | RoadTransport/LicensePlateID: 1; RoadTransport/TrailerLicensePlateID: 1 | `AA 9999 AA` | 2 | 2 | 1 | road | `UR 4160 KT` |
| `urn:ubl-examples:world:XB:bonded-warehouse` | Certificate/ID: 1 | `AA-AAAA-AAA-9999` | 1 | 1 | 1 | plastics | `XB-BOND-LIC-0388` |

What each scheme is, as the documents use it:
- Party identifiers, one register per country, used both as `PartyIdentification/ID` and `PartyLegalEntity/CompanyID` with the same value: Urvania `XU-R-1nnnnn` (14 parties), Bayvarra `2041nnnn` (22), Lisavu `IC4nnnn` (13). The endpoint `urn:ubl-examples:world:endpoint` is always `<country>:<register number>` (47 values, one per party with an endpoint). Customs trader IDs are derived from the register number in all three countries (`XU-TR-104274` ← `XU-R-104274`, `XB-TR-410274` ← `20410274`, `XL-TR-041859` ← `IC41859`). Tax IDs: Urvania `XU00nnnnnnn`, Bayvarra `<state>-nnnnnnn` with the state of the party's address (`CO`, `UL`, `NT`); Lisavu has none (no general sales tax).
- Additional party IDs: `GS1 GLN` for the three GS1 parties (Lumeway `9520610900008`, Brightmarket `9522610900002`, Brackenmere `9523710900008`) and their locations; `ISO 6523` with an ICD prefix in the value (`0990:` + five digits) for five parties (Valdara, Castrano, Montebrio, Ferrano Grid, and the Bayvarran Rivermouth).
- Addresses: one address register per country level: `XU:address-register` (16 digits), `XL:delivery-point` (8 digits), and in Bayvarra a city register for Lumeport (`LUM-ADR-nnnnnn`) next to state registers for Upland State (`UL-ADR-…`) and Northern Territory (`NT-ADR-…`). Every party has one address ID, the same in every document (checked: no address ID under two names, no party with two).
- Items: `GS1 GTIN` for Lumeway's, Lumeport Textile Mill's and Brackenmere's items, `urn:ubl-examples:world:item` (12 digits, `77…`) for the world item numbers; see items#F2 for how the two meet on one item.
- Money: `urn:ubl-examples:world:account` (IBAN-like, country `XB`/`XL`/`XU`, bank code and branch inside), bank identifiers in BIC form (`BLUMXBLX`, `BSELXLSL`, `CREVXUFR`), branch schemes per country, `ISO 11649` RF creditor references built from the invoice number (39 values), `ISO 6166` for Valdara's one listed share.
- Logistics: `ISO6346` containers, `GS1 SSCC`, `GS1 GRAI`, `ISO 15459` licence plates, UN/LOCODEs `XBLMA`, `XBLMP`, `XBMRW`, `XLSEL`, `XLSLA`, `XUFER`, `XUSRV`, vessel, vehicle, rail-vehicle and aircraft registers.

### Document numbering

All 250 root document IDs are `<issuer prefix>-<type infix>-26-<four digits>` (the version pairs of contest share one number per pair, see "Mechanical hits"). The prefix names the party that really issued the document; where the mechanical `issuer` column of documents.csv shows another party, the document number, the language tag of English texts (parties#F-known row "en-XB/en-XU") and the document type agree on the real issuer (e.g. `LD-DOC-26-0328` for air/07, `TOL-BL-26-0206` for cotton/13). Per prefix:

| Prefix | Issuers (mechanical issuer column) | Type infixes | Numbers | Flows |
|---|---|---|---|---|
| `BF` | Brackenmere Furniture 11, Lumeport Public Works Department 7, Bayforth Forwarding 6, Lumeway Distribution 2 | CN, DOC, EX, FI, INV, PO, TS, WB | 0135–0638 (26 docs) | air,contest,cotton,furniture,retail,sea,tender,wood |
| `BIS` | Bayvarra Information Service 3 | DOC | 0198–0639 (3 docs) | contest,tender |
| `BL` | Bank of Lumeport 1 | DOC | 0200–0200 (1 docs) | tender |
| `BS` | Brightmarket Stores 17, Brackenmere Furniture 1, Lumeway Distribution 1 | DOC, FC, IR, PO, PR, RA, RE | 0217–0580 (19 docs) | furniture,packaging,retail |
| `CL` | Castrano Logistics 2 | DA | 0153–0215 (2 docs) | road,tender |
| `CSWC` | Coastal State Water Company 6 | CN, DOC, INV | 0317–0322 (6 docs) | utilities |
| `FB` | Fiumella Barges 3 | INV, TEP, WB | 0886–0891 (3 docs) | plastics |
| `FCC` | Valdara Industries 2, Ferrano Chamber of Commerce 1, Customs Administration of Urvania 1 | CO, DOC | 0157–0728 (4 docs) | carnet,road |
| `FE` | Ferrano Energy 3 | DOC, INV | 0313–0315 (3 docs) | utilities |
| `FG` | Ferrano Grid 2 | DOC, INV | 0149–0150 (2 docs) | energy |
| `FIH` | Ferrano Intermodal Hub 2 | DOC, TS | 0330–0333 (2 docs) | rail |
| `FRC` | Ferrano Rail Cargo 8 | DOC, INV, TEP, WB | 0307–0336 (8 docs) | ore,rail |
| `HF` | Lumeway Distribution 1 | ST | 0151–0151 (1 docs) | sea |
| `KG` | Kelpstone Gas 4 | DOC, EX, INV | 0152–0159 (4 docs) | energy |
| `KXL` | Kelaro Air Cargo 2 | WB | 0325–0717 (2 docs) | air,mast |
| `LACT` | Lumeport Airport Cargo Terminal 1 | TS | 0326–0326 (1 docs) | air |
| `LCF` | Lisavu Cotton Farm 1 | DN | 0193–0193 (1 docs) | cotton |
| `LD` | Lumeway Distribution 32, Velumi Trading 1, Brightmarket Stores 1, Lumeport Trade Accord Council 1 | CAT, CN, DA, DAG, DOC, FI, IM, INV, OR, PL, PO, RA, RM, TR | 0123–0329 (35 docs) | air,rail,retail,road,sea |
| `LPWD` | Lumeport Public Works Department 26, Marrowdale Sawmill 2, Valdara Industries 1 | DOC, IM, OC, PO, RM | 0187–0640 (29 docs) | contest,furniture,tender |
| `LTAC` | Lumeport Trade Accord Council 1 | DCP | 0126–0126 (1 docs) | sea |
| `LTM` | Lumeport Textile Mill 8, Selanu Cotton Ginnery 1 | DA, FC, FI, FR, IM, INV, PO, RM | 0192–0529 (9 docs) | cotton,packaging |
| `MP` | Montebrio Power 3 | IM, INV, RM | 0151–0160 (3 docs) | energy |
| `MS` | Marrowdale Sawmill 8 | DA, DOC, EX, INV, TR | 0190–0638 (8 docs) | tender,wood |
| `NW` | Nalevi Warehousing 1 | RA | 0146–0146 (1 docs) | sea |
| `PL` | Port of Lumeport 1 | TS | 0138–0138 (1 docs) | sea |
| `PS` | Port of Selanu 1 | TS | 0142–0142 (1 docs) | sea |
| `RA` | Robin Ashdale 1 | PO | 0240–0240 (1 docs) | retail |
| `RP` | Rivermouth Packaging 5 | IM, INV, PO, RM | 0522–0895 (5 docs) | packaging,plastics |
| `RR` | Rinova Recovery 7 | DA, DOC, EX, INV, OR, TR | 0207–0894 (7 docs) | plastics,waste |
| `SAC` | Selanu Airport Cargo 1 | TS | 0330–0330 (1 docs) | air |
| `SCC` | Selanu Chamber of Commerce 2, Selanu Cotton Ginnery 1 | DOC, GC | 0202–0727 (3 docs) | carnet,cotton |
| `SCG` | Selanu Cotton Ginnery 7 | EX, INV, RM, SBC, SBI, WS | 0191–0210 (7 docs) | cotton |
| `SE` | Saltmere Engineering 3 | DA, FI, INV | 0714–0719 (3 docs) | mast |
| `SM` | Serravona Mining 2 | DA, INV | 0308–0312 (2 docs) | ore |
| `ST` | Selanu Telecom 3 | DOC, INV, PO | 0323–0713 (3 docs) | mast,utilities |
| `TCB` | Velumi Trading 1 | IM | 0144–0144 (1 docs) | sea |
| `TH` | Trasvia Haulage 3 | INV, TS, WB | 0159–0165 (3 docs) | road |
| `TOL` | Tidewell Ocean Lines 4, Selanu Cotton Ginnery 1, Lumeway Distribution 1 | BL, CTR, DOC, MF | 0130–0207 (6 docs) | cotton,sea |
| `VI` | Valdara Industries 22, Lumeport Public Works Department 1, Brightmarket Stores 1, Velumi Trading 1, Marrowdale Sawmill 1 | CAT, CN, DOC, EX, IM, INV, OR, PO, RM, TD, TR | 0150–0636 (26 docs) | ore,packaging,rail,road,tender,utilities,waste,wood |
| `VT` | Velumi Trading 5, Lumeway Distribution 1 | DOC, OC, PO, PR, RM | 0127–0320 (6 docs) | air,sea |

| Flow | Number range of root IDs | Documents |
|---|---|---:|
| sea | 0123–0154 | 29 |
| energy | 0149–0160 | 9 |
| road | 0149–0168 | 17 |
| tender | 0187–0225 | 36 |
| cotton | 0191–0212 | 18 |
| waste | 0204–0208 | 3 |
| retail | 0217–0240 | 22 |
| ore | 0304–0313 | 8 |
| utilities | 0313–0324 | 14 |
| air | 0320–0331 | 10 |
| rail | 0325–0337 | 11 |
| packaging | 0521–0531 | 9 |
| furniture | 0567–0583 | 17 |
| wood | 0625–0638 | 11 |
| contest | 0633–0640 | 16 |
| mast | 0713–0719 | 5 |
| carnet | 0724–0728 | 4 |
| plastics | 0882–0895 | 11 |

The four-digit number is not the issuer's own counter: the second table shows one block of consecutive numbers per flow, used by every issuer in that flow in issue order (identifiers#F2).

## Findings

### identifiers#F1 · Medium · Two parties share the prefix `BF`, also for invoices, item numbers, signatures and creditor references
- XPath: `cotton/17-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0211`   (Bayforth Forwarding)
- XPath: `sea/18-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0143`   (Bayforth Forwarding)
- XPath: `furniture/09-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0575`   (Brackenmere Furniture)
- XPath: `furniture/17-Invoice.xml:/Invoice/cbc:ID` = `BF-INV-26-0583`   (Brackenmere Furniture)
- XPath: `sea/12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`   (Bayforth)
- XPath: `tender/17-Tender.xml:/Tender/cbc:ID` = `BF-DOC-26-0203`   (Brackenmere)
- XPath: `sea/18-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `BF-SEA40`   (Bayforth's service)
- XPath: `furniture/02-Quotation.xml:/Quotation/cac:QuotationLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `BF-GS-01`   (Brackenmere's product)
- XPath: `cotton/17-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF08BFINV260211`
- XPath: `furniture/17-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF52BFINV260583`
- XPath: `sea/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `BF-SIG-EX-sea`   (Bayforth)
- XPath: `furniture/03-ItemInformationRequest.xml:/ItemInformationRequest/cac:Signature/cbc:ID` = `BF-SIG-26-0312`   (Brackenmere)
- Why: everywhere else in the world a prefix names exactly one party (register above: 40 prefixes; the only other exception is the known duplicate `VI-RM-26-0316`, utilities/07#F1). `BF` is used by Bayforth Forwarding (6 documents in air, cotton, retail, sea, plus `BF-FI`, `BF-EX`, `BF-WB`, `BF-TS`, `BF-TEP`, `BF-SOA`, items `BF-AIR`, `BF-ROAD`, `BF-CLR`, `BF-INS`, `BF-SEA40`) and by Brackenmere Furniture (12 documents in furniture, tender, wood and contest, plus `BF-DN`, `BF-ESPD`, `BF-DS-PARK`, items `BF-GS-01`, `BF-DK-16`, `BF-INST`). Both issue `BF-INV-26-nnnn` invoices and RF references with the same infix `BFINV`, both sign `BF-SIG-…`; no value collides yet, but a reader who gets `BF-INV-26-0234` (retail/16) cannot tell from the number which company it belongs to, and the two number ranges overlap (Bayforth 0143–0331, Brackenmere 0203–0638). Each flow alone shows only one of the two, so the clash shows only across flows. Medium: one scheme of identification (the issuer prefix) identifies two different parties.
- Condition: every document-number, item-number and signature prefix belongs to one party in all 250 examples.
- Options: (a) preferred: give one of the two another prefix (e.g. Brackenmere `BFU`, the shorter change, 12 root IDs and their references, items and RF references); (b) keep `BF` for both and accept that the prefix is not an issuer key (then the world's numbering rule must say so).
- Needs decision: yes
- Seen in reviews: none

### identifiers#F2 · Medium · Document numbers are one counter per flow shared by all issuers, so no issuer numbers its own documents in order
- XPath: `retail/18-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0236`   (issued 2026-04-30)
- XPath: `sea/22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147`   (issued 2026-05-14)
- XPath: `wood/03-Order.xml:/Order/cbc:ID` = `VI-PO-26-0627`   (2026-02-22)
- XPath: `ore/01-Order.xml:/Order/cbc:ID` = `VI-PO-26-0304`   (2026-03-02)
- XPath: `packaging/01-Order.xml:/Order/cbc:ID` = `VI-PO-26-0521`   (2026-04-27)
- XPath: `cotton/14-CommonTransportationReport.xml:/CommonTransportationReport/cbc:ID` = `TOL-CTR-26-0207`   (2026-03-03)
- XPath: `sea/16-CommonTransportationReport.xml:/CommonTransportationReport/cbc:ID` = `TOL-CTR-26-0141`   (2026-05-16)
- XPath: `utilities/02-Invoice.xml:/Invoice/cbc:ID` = `FE-INV-26-0313`   (Ferrano Energy)
- XPath: `utilities/04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`   (Valdara)
- XPath: `utilities/06-Invoice.xml:/Invoice/cbc:ID` = `CSWC-INV-26-0317`   (Coastal State Water)
- XPath: `utilities/13-Invoice.xml:/Invoice/cbc:ID` = `ST-INV-26-0323`   (Selanu Telecom)
- XPath: `road/01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`   (road starts at 0149)
- XPath: `energy/01-UtilityStatement.xml:/UtilityStatement/cbc:ID` = `FG-DOC-26-0149`   (energy also starts at 0149)
- Why: counted over the 250 root IDs (documents.csv, last four digits; second table above): every flow uses one block of consecutive numbers (sea 0123–0154, road 0149–0168, utilities 0313–0324, …), and inside a flow the numbers rise in issue order across all issuers: in utilities Ferrano Energy has 0313–0315, Valdara 0316, Coastal State Water 0317–0322, Selanu Telecom 0323–0324. Blocks of different flows overlap (sea, energy and road; tender, cotton, waste and retail; ore, utilities, air and rail; wood and contest). Seen per issuer, numbers jump back and forth with the flow the document happens to belong to: Lumeway's invoice of 30 April is `0236`, its invoice of 14 May `0147`; Valdara's orders are `0627` (February), `0304` (March), `0521` (April); Tidewell's two reports `0207` (March) and `0141` (May). `check_consistency.py` group 5 lists 10 such inversions (Bayforth, Brightmarket, Ferrano Energy, Lumeway ×4, Tidewell, Valdara ×2). The per-example lead utilities/04 (entry 199) already suspected "one generator sequence rather than each sender's own numbering"; the cross-flow count shows it holds in all 18 flows. Invoice numbers in particular are normally one continuous sequence per issuer (own knowledge of VAT invoicing rules; the world's own rule is not stated in the documents). Medium: the number part of a document ID identifies the position in an example flow, not in the issuer's numbering.
- Condition: per issuer and document type, document numbers rise with the issue timestamp across all flows (no inversion in `check_consistency.py` group 5), and no number block is shared by unrelated issuers by construction.
- Options: (a) preferred: one counter per issuer (and type, if the world wants that), numbered in issue order across flows; every reference, RF reference, payment note and signature built from a number follows; (b) keep the flow blocks and state in the world's rules that document numbers are allocated per collaboration (unusual, and it does not explain the inversions within one issuer).
- Needs decision: yes
- Seen in reviews: lead utilities/04 (199); group 5 of `check_consistency.py`

### identifiers#F3 · Medium · `ProfileExecutionID` is the flow name in all 250 documents and joins unrelated collaborations
- XPath: `packaging/01-Order.xml:/Order/cbc:ProfileExecutionID` = `PACKAGING-2026-01`   (Valdara orders stretch film from Rivermouth)
- XPath: `packaging/01-Order.xml:/Order/cbc:ProfileID` = `urn:ubl-examples:world:profile:ordering:1.0`
- XPath: `packaging/02-Invoice.xml:/Invoice/cbc:ProfileExecutionID` = `PACKAGING-2026-01`
- XPath: `packaging/02-Invoice.xml:/Invoice/cbc:ProfileID` = `urn:ubl-examples:world:profile:billing:1.0`
- XPath: `energy/01-UtilityStatement.xml:/UtilityStatement/cbc:ProfileExecutionID` = `ENERGY-2026-01`   (Ferrano Grid's metering for Ferrano Energy)
- XPath: `energy/02-Invoice.xml:/Invoice/cbc:ProfileExecutionID` = `ENERGY-2026-01`
- Why: UBL defines `ProfileExecutionID` as "Identifies an instance of executing a profile, to associate all transactions in a collaboration". In every one of the 250 examples the value is `<FLOW>-2026-01` (identifiers.csv, 250 values, 18 distinct, one per flow, counted with the element filter `ProfileExecutionID`). A flow is a story, not one execution of one profile: within one flow the same execution ID is carried by documents of different profiles (packaging: ordering, billing, despatch-receipt and retail-sale profiles; energy: utility-billing, customs and billing) and of collaborations between different parties that have nothing to do with each other (packaging: Valdara–Rivermouth, Lumeport Textile Mill–Rivermouth, Brightmarket–Textile Mill, and two shop sales to consumers; energy: Ferrano Grid–Ferrano Energy, Kelpstone–Montebrio, Kelpstone's export declaration; contest: the information service's register extract and the department's notices). The sea/29 review refuted the remark for one example because "every document of the flow shares it"; seen over all flows that is exactly the problem: the ID names the example set. Medium: the element carries a meaning other than its definition, in every example.
- Condition: every `ProfileExecutionID` identifies one execution of the profile named in the same document's `ProfileID`, shared only by documents of that collaboration (same parties, same transaction), or the element is absent.
- Options: (a) preferred: one execution ID per collaboration and profile (e.g. per order-to-invoice cycle of two parties), so that documents of one transaction are linked and unrelated ones are not; (b) drop the element where no collaboration needs it.
- Needs decision: yes
- Seen in reviews: sea/29 (refuted there, "Considered and refuted"); contest/13, contest/14 (used as the link of the register extract, refuted there)

### identifiers#F4 · Low · Identifiers built from file numbers, flow names and other identifiers
- XPath: `road/05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road`
- XPath: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `SCG-SIG-EX-cotton`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Signature/cbc:ID` = `TWL-SIG-BL-sea`
- XPath: `air/05-TransportationStatus.xml:/TransportationStatus/cac:Signature/cbc:ID` = `LACT-SIG-TS-05`   (file 05)
- XPath: `sea/17-TransportationStatus.xml:/TransportationStatus/cac:Signature/cbc:ID` = `PS-SIG-TS-17`   (file 17)
- XPath: `tender/15-Tender.xml:/Tender/cac:Signature/cbc:ID` = `VI-SIG-TENDER-15`   (file 15)
- XPath: `road/08-Waybill.xml:/Waybill/cac:Signature/cbc:ID` = `TH-SIG-TH-WB-26-0159`
- XPath: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-CARNET-26`
- XPath: `retail/14-TransportationStatusRequest.xml:/TransportationStatusRequest/cac:TransportExecutionPlanDocumentReference/cbc:ID` = `BF-TEP-26-0227`   (the carrier's plan has the number of the shipper's request:)
- XPath: `retail/11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:ID` = `095206101230000018`   (and:)
- XPath: `sea/20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230`
- XPath: `road/08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cbc:ID` = `KXU104411490000015`   (and:)
- XPath: `road/04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01490`
- XPath: `retail/12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[1]/cbc:ID` = `095206102170000014`   (casting `VI-SF-02170`, retail/21)
- XPath: `air/03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cbc:ID` = `095206103190000015`   (castings `VI-SF-03190`…, air/06)
- XPath: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`   (Valdara's register number `XU-R-104274` without its last digit)
- XPath: `carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`   (ends in the register number)
- XPath: `energy/06-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB45BLUM38522004817534`
- XPath: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XL67BSEL0020004817534`
- Why: a real identifier does not encode the name of the example set or the position of a file in it. Counted over the 147 `Signature/ID` values (identifiers.csv): 14 contain the flow name (`…-EX-road`, `…-IM-wood`, `…-BL-cotton`, …), 15 end in the example's own file number (`…-TS-05` in air/05, `…-FI-09` in sea/09 and cotton/09, `…-TENDER-17` in tender/17, …), 7 repeat the document's own ID after a signature prefix, doubling the issuer prefix (`TH-SIG-TH-WB-26-0159`, `KXL-SIG-KXL-WB-26-0325`, `FRC-SIG-FRC-WB-26-0310`, `FB-SIG-FB-WB-26-0890`, …). Beyond signatures: the carnet consignment is `VI-CS-CARNET-26`; the carrier's transport plan carries the shipper's request number (`0227`); the serial reference of every pallet SSCC or licence plate starts with the serial number of the first casting of the same flow (road `…1044114900000…` / `VI-SF-01490`, sea `…01230000…` / `VI-SF-01230`, retail `…02170000…` / `VI-SF-02170`, air `…03190000…` / `VI-SF-03190`), although a pallet of 4 benches has nothing to do with a casting's serial number and the SSCC is Lumeway's while the serial is Valdara's; the five `ISO 6523` values are the national register numbers cut to five digits; every contact telephone number of a registered party ends in the last three or four digits of its register number (Valdara `…518 4274` / `104274`, Lumeway `…474 274` / `20410274`, Velumi `…729 1859` / `IC41859`; all 634 telephone values of contacts.csv that belong to a party with a register number); and the accounts of Kelpstone Gas (Bayvarra) and Lisavu Cotton Farm (Lisavu, another bank) end in the same nine digits `004817534` (conditions note). None of this is a contradiction; each is a value whose structure shows how it was made. The signature IDs are already Low in many per-example reviews under the merge decision "Signature with only an ID and a signatory"; the derivation is not.
- Condition: no identifier value contains a flow name or an example's file number; identifiers of different things (pallet and casting, plan and request, account and account) are not derived from each other unless the world's rule for that identifier says so.
- Options: (a) preferred: per scheme, an independent running number in the issuer's own series (signatures in the signer's series, pallets in the packer's SSCC series, plans in the carrier's series); (b) keep derived values where a real practice derives them (e.g. RF references from invoice numbers, customs trader IDs from register numbers, both kept) and replace the rest.
- Needs decision: no
- Seen in reviews: merge decision "Signature with only an ID and a signatory" (other aspect); conditions "For other topics" (the account tails); lead utilities/04 (199)

### identifiers#F5 · Low · One party, several prefixes; one prefix, several kinds of document
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cbc:ID` = `TOL-BL-26-0139`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Signature/cbc:ID` = `TWL-SIG-BL-sea`   (Tidewell: `TOL` and `TWL`)
- XPath: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cbc:ID` = `BS-DOC-26-0217`
- XPath: `retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:Signature/cbc:ID` = `BM-SIG-26-0420`   (Brightmarket: `BS` and `BM`)
- XPath: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:ID` = `LPWD-DOC-26-0187`
- XPath: `tender/01-PriorInformationNotice.xml:/PriorInformationNotice/cac:Signature/cbc:ID` = `PWD-SIG-PIN`   (the department: `LPWD` and `PWD`)
- XPath: `utilities/08-UtilityStatement.xml:/UtilityStatement/cbc:ID` = `CSWC-DOC-26-0320`
- XPath: `utilities/08-UtilityStatement.xml:/UtilityStatement/cac:Signature/cbc:ID` = `CSW-SIG-26-0401`   (Coastal State Water: `CSWC` and `CSW`)
- XPath: `tender/14-GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:ID` = `BL-DOC-26-0200`
- XPath: `tender/14-GuaranteeCertificate.xml:/GuaranteeCertificate/cac:Signature/cbc:ID` = `BLUM-SIG-GC`   (Bank of Lumeport: `BL` and `BLUM`)
- XPath: `cotton/02-Forecast.xml:/Forecast/cbc:ID` = `LTM-FC-26-0192`
- XPath: `cotton/02-Forecast.xml:/Forecast/cac:Signature/cbc:ID` = `LT-SIG-26-0202`   (Lumeport Textile Mill: `LTM` and `LT`)
- XPath: `tender/04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cbc:ID` = `MS-DOC-26-0190`
- XPath: `tender/04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:Signature/cbc:ID` = `HS-SIG-EOI`   (Marrowdale Sawmill: `MS` and `HS`)
- XPath: `wood/09-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0636`
- XPath: `rail/01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:ProductDocumentationDocumentReference/cbc:ID` = `VI-RM-B180`   (`VI-RM` for remittance advices and the repair manual)
- XPath: `ore/02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `VI-TR-26-0305`
- XPath: `air/06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ProductTraceID` = `VI-TR-03190`   (`VI-TR` for transport requests and product traces)
- XPath: `sea/10-PackingList.xml:/PackingList/cbc:ID` = `LD-PL-26-0134`
- XPath: `retail/03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026-2`   (`LD-PL` for packing lists and price lists)
- XPath: `tender/18-TenderWithdrawal.xml:/TenderWithdrawal/cac:TenderNotificationDocumentReference/cbc:ID` = `PWD-RCPT-BF-1`   (a receipt numbered unlike the department's receipt:)
- XPath: `tender/16-TenderReceipt.xml:/TenderReceipt/cbc:ID` = `LPWD-DOC-26-0202`
- Why: document numbers use one prefix per party (register above), but the same parties' signatures and other identifiers use a second prefix in seven cases, and two parties use one prefix-plus-infix for two kinds of document. The tender receipt that tender/18 cites (`PWD-RCPT-BF-1`, not in the flow, lead entries 160, 162, 167) is numbered in neither of the department's two series, which makes it harder to see that the department's real receipts are `LPWD-DOC-…`. Each case is small; together they show that the prefix does not reliably name the party or the kind of thing.
- Condition: each party uses one prefix for everything it numbers; within a prefix, one infix means one kind of document or object.
- Options: (a) preferred: align the signature and reference prefixes with the document prefix (`TOL`, `BS`, `LPWD`, `CSWC`, `BL`, `LTM`, `MS`) and give the repair manual, the trace IDs and the price lists infixes of their own; (b) state the second prefixes as the world's rule (e.g. a signing certificate series per party).
- Needs decision: no
- Seen in reviews: tender/18 (the missing receipt, per-example); none for the prefixes

## Mechanical hits

Groups of `check_consistency.py` that are this topic's, each hit and what became of it.

Group 1 (same identifier value + scheme, different names; 8 hits):
- `771020000027` (additional), `VI-B180` (manufacturer's), `LD-10442`, `VI-B180`, `VI-C180` (seller's), `GRY` (extended), `9520610000012` (GTIN): the variants are the same item in another language rendering (`Hiapi vusase Serra 180` in Velumi's Lisavan receipt sea/29, `[qau] Haz nanskir Serra 180` in Valdara's documents) or a substitute line (`… moss green`, `… 2025, from stock`, `… 2026` in road/02 and retail/08, whose extended IDs tell them apart): intended; the name renderings are items#Known. The `VI-C180` variants of road/02 are per-example (road/02, road/04: lead 92).
- `TWLU4120872` (ISO6346): the same container described with fewer details in sea/10 than in sea/14 and sea/15; no contradicting value: refuted (equipment checked the container).

Group 4 (same document ID from the same issuer; 9 hits):
- contest `LPWD-DOC-26-0633` … `0640`, `BF-DOC-26-0637`, `BF-DOC-26-0638`, `BIS-DOC-26-0639` (8 pairs): versions 1 and 2 of the same notice or response (`VersionID` 1 and 2, the second of the two contest rounds): intended. (The mechanical issuer for `BF-DOC-26-0637/0638` is the department; the prefix says Brackenmere, which is right: they are Brackenmere's responses.)
- `FCC-CO-26-0157` road/06 and road/07, both `VersionID` 1: the application (06) carries the number the chamber gives the certificate (07): known per-example (road/06, road/07#F1, leads 100, 101); not a version pair.

Group 5 (numbering against issue order; 10 hits): all ten are F2 (Bayforth `BF-INV`, Brightmarket `BS-PO`, Ferrano Energy `FE-DOC` 0314/0315 on the same day, Lumeway `LD-CAT`, `LD-CN`, `LD-DA`, `LD-INV`, Tidewell `TOL-CTR`, Valdara `VI-PO`, `VI-RM`). The Bayforth hit also mixes in nothing of Brackenmere's (the checker groups by the mechanical issuer); F1 shows the shared prefix.

Group 10 (citations of documents issued later; 12 hits): ten are timelines#F3 (air/05 → air/04, energy/01 → energy/02, road/14 → road/13, sea/24 → sea/27, sea/28 → sea/25, tender/17 and tender/19 → tender/13, utilities/08 → utilities/09, rail/08 → rail/06 twice). New relative to timelines#F3, not new as findings: road/06 → road/07 (`FCC-CO-26-0157` in the application, known per-example, see group 4) and road/08 → road/04 (`ConsignorAssignedID` `CL-DA-26-0153` in a waybill issued 08:16, the despatch advice at 15:15: one more case of the pattern of timelines#F3, noted under "For other topics").

`document_id_mentions.csv` (24 rows): every row was checked against the per-example reviews: the contracts given as `LD-DAG-26-0125` (air/01, air/07, sea/06; refuted in air/07, a finding in sea/06) and `BF-DOC-26-0568` (furniture/11, finding), the sea/14 consignor and forwarder IDs (`VT-PO-26-0127`, `LD-FI-26-0131`; finding of sea/14), `BF-FI-26-0137` as `ShippingOrderID` (merge decision), `LD-IM-26-0161` as previous declaration of sea/11 (finding of sea/11; its cross-flow consequence is items#F1), and the carnet, rail/09, retail/09, retail/14, road/06–08 and air/04 rows, which point to the right kind of document. Nothing further.

## Checked and consistent

- Check digits: `check_ids.py` over all 250 examples: 502 checks, all OK (251 GS1 keys: GLN, GTIN, SSCC, GRAI; 91 IBAN-like accounts; 76 ISIN; 70 RF references; 14 ISO 6346 container numbers).
- Party identifiers: no register, tax, customs-trader, GLN, ISO 6523 or endpoint value under two party names, and no party with two values of one scheme (party_ids.csv, 3998 rows, grouped by value and scheme). Register number, company ID, endpoint and customs trader ID of a party agree in every document.
- Address IDs: one per party, the same in all documents, never shared.
- Accounts: one account per party; no account under two parties; country and bank code inside each account agree with the bank identifier and branch scheme of the same aggregate (financial_accounts.csv, 91 rows, 26 accounts).
- Containers, vehicles, vessels and the aircraft: one ID per object across flows (equipment register of this run).
- References: no reference to another example's ID disagrees with that example's issue date, UUID or type code (group 6: 0 hits); the references of the wrong kind are per-example findings (see the mentions above and "Leads"). The unresolved references are documents the world does not model (data sheets, tariffs, ESPDs, certificates, framework contracts), plus the known per-example ones listed under "Leads".
- Real registers, from own knowledge: GS1 prefix 952 is reserved by GS1 for demonstrations and examples, so the GLNs, GTINs, SSCCs and GRAIs (`952…`, `0952…`) cannot collide with real company prefixes; `+999` is not an assigned E.164 country code; `XB`, `XL`, `XU` are in the ISO 3166 user-assigned range and are not IBAN or BIC country codes (SWIFT uses `XK` only), so the accounts and BICs cannot be real; the currencies `XBL`, `XUF`, `XLC` are not ISO 4217 codes (the assigned X-codes are metals, funds, units and test codes such as `XAU`, `XBA`–`XBD`, `XDR`, `XUA`, `XTS`); the UN/LOCODEs all start with an `X` country code; MMSI MID 297/298 and the `Q` call signs are not allocated (known refutation); the aircraft mark `QL-KXA` uses a `Q` prefix, which ICAO has not allocated as a nationality mark.

## Considered and refuted

- `PWD-PO-26-0212` (tender/28 `OrderDocumentReference`) next to `LPWD-PO-26-0212` (its `OrderReference`): one order under two numbers; within one example and already a per-example finding (tender/28), refuted as a cross-flow problem.
- `FRC-TEP-26-0001` cited by ore/02 and ore/03 although the plan of the flow is `FRC-TEP-26-0307`: per-example (ore/02, ore/03); no other flow uses the value.
- `VT-PO-26-0319` (air/03, air/06, air/08): per-example High (air/03#F1, air/06#F1); the air order is the change `VT-OC-26-0320` of the sea order `VT-PO-26-0127`. The cross-flow view adds only that `0319` is the change's number minus one (part of F4's pattern).
- `VI-RM-26-0316` used by Valdara (utilities/04), Brightmarket (utilities/07) and Velumi (utilities/14): one value on three documents of three issuers; per-example High (utilities/07#F1, lead 198), not repeated here.
- Prefix `FCC` for a customs document (carnet/04 `FCC-DOC-26-0728`, mechanical issuer the Urvanian customs): the proof is signed by the Ferrano Chamber of Commerce, its exporting guarantor (`SignatoryParty`), so the prefix names the real issuer; refuted.
- Debit notes whose number names the other party (`BS-DOC-26-0580` furniture/14, `VT-DOC-26-0153` sea/28, `LPWD-DOC-26-0223` tender/34): the number names the real issuer; the error is the reversed accounting roles (parties, Known table), not the number.
- Bayvarra's Lumeport city register next to state registers for Upland State and Northern Territory: possible as a rule (a capital with its own register); not refuted either: "Cannot be told".
- `ISO6346` written without a space while every other ISO scheme has one (`ISO 6523`, `ISO 639`, `ISO 3166`, `ISO 6166`): a spelling of the schemeID; CLAUDE.md keeps schemeIDs in their current style, so not a finding.

## Leads from the per-example reviews

All 221 "Outside this review" entries of the 250 merged files were extracted and numbered in file order (the numbering of the timelines file). Entries on this topic:

| Source (entry) | Entry in short | Outcome |
|---|---|---|
| cotton/12 (38) | owner code `TWLU` in the real BIC register | could not check against the register (logistics found it recorded as unassigned in the repository's source) |
| cotton/14 (41) | MMSI MID 298 | refuted (known refutation) |
| ore/07 (67) | item number `771010000013` recurs | items (merge decision on world item numbers as valid GTIN-12s) |
| road/05 (98) | border post without identifier | per-example (road/05#F14, the reviews of road/09 and road/10); nothing cross-flow added |
| road/06 (99, 100), road/07 (101) | sequence numbers of endorsements; `OriginalJobID`, `PreviousJobID`; the chamber's number in the application | per-example (road/06, road/07); group 4 hit |
| road/13 (106) | road/11 cites the waybill as delivery note | per-example (road/11) |
| sea/17 (129) | `ShippingOrderID` holding consignment or shipment IDs | merge decision; extent: 19 uses in 9 flows (air, cotton, mast, ore, plastics, rail, retail, road, sea), and within one shipment three values in sea (`LD-SH-26-0132`, `LD-CS-26-0133`, `BF-FI-26-0137`) and two in air (`LD-SH-26-0323`, `LD-CS-26-0324`) |
| tender/03 (144) | catalogue line refers to a call-for-tenders line 2 that does not exist | lies in tender/25 (its review mentions the reference); within one flow |
| tender/13 (155) | Brackenmere's tenders cite Valdara's qualification | timelines#F3 (time); the wrong party's document: per-example (tender/17, tender/19) |
| tender/16 (160), tender/17 (162), tender/19 (167) | receipt `PWD-RCPT-BF-1` not in the flow | per-example (tender/18); its numbering: F5 |
| tender/21 (172) | `PWD-2026-PARKS` as contract folder, project and contract | per-example (tender/21, 24, 26); extent counted: 23 × `ContractFolderID`, 6 × `ProcurementProject/ID`, 6 × `Contract/ID`, 7 × document references, all in tender |
| utilities/04 (198) | `VI-RM-26-0316` under three senders | per-example High (utilities/07#F1) |
| utilities/04 (199) | the numbers run across senders: one generator sequence | F2 |
| retail/18 (86) | despatch and handling-unit lines share ID 1 | per-example (retail/17#F13); within one flow |

Entries on parties and items are in those two files (parties: 18–28, 30–34, 55, 97, 128, 152, 154, 183, 186, 201, 207; items: 67, 79, 85, 87, 90, 92, 109, 175, 178, 200). The remaining entries that the timelines file left to other topics (1, 12, 16, 43, 46, 56, 65, 68, 70, 78, 80, 82, 108, 110, 112, 135, 137–139, 142, 145–148, 156–159, 161, 164–166, 168, 169, 171, 173, 174, 176, 177, 179, 181, 191, 194–197, 211, 220, 221) are money, customs rules, flow composition or the tender story, handled by the conditions file or left to the per-example reviews; none of them is about parties, items or identifiers.

## Cannot be told from the documents

1. Is `0990` meant to be an ISO 6523 ICD of the world (Codana)? From own knowledge the ICDs assigned by the ISO 6523 registration authority run from `0002` to about `0240`, so `0990` is very probably unassigned, but this could not be checked against the current register. Why does a Bayvarran party (Rivermouth, `0990:20274`) have an identifier in it?
2. Could not check against the register: the ISO 10383 MIC `XLMX` (`tender/26-Order.xml:/Order/cac:PricingExchangeRate/cbc:ExchangeMarketID` = `XLMX`; not a MIC known to me, but the list changes monthly); the ISIN prefix `XU` (`carnet/01-GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`; ISIN prefixes beginning with `X` are partly used for international securities, `XU` is not one I know); the ISO 6346 owner codes `TWLU` and `FRXU`; the ISO 15459 issuing agency code of `KXU104413250000013` and `KXU104411490000015` (equipment note); the airline-designator-like owner code `K0` of the ULDs `RKN41207K0` and `AKE20514K0` (equipment note; two-character designators with a digit are assigned by IATA, and whether `K0` is one could not be checked).
3. Is the Lumeport city address register a deliberate exception to "address registers by country level" (Coastal State has no state register in the documents)?
4. What is each party's numbering rule (one series per party, or per document type)? The documents cannot say, because the numbers come from the flow (F2).

## For other topics

- Timelines: road/08 (issued 08:16) carries the despatch advice number `CL-DA-26-0153` of road/04, issued 15:15, as `ConsignorAssignedID`: one more citation of a later document for timelines#F3's list.
- Parties: every debit note of the world (furniture/14, sea/28, tender/34) has the accounting roles reversed; its number and the language tag of its English texts name the real issuer (parties Known table).
