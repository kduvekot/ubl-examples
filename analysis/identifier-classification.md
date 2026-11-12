# Identifier schemes and code-valued attributes — UBL example world

> Working analysis from the code-list and identifier review of November 2026. The decisions taken on it are in `analysis/codelist-decisions.md`, which wins where the two differ; the Q-numbers there refer to this table.


*Analysis only; nothing in the repository was changed. Own sweep of the 230 `world/examples/*/*.xml`: every `cbc:*ID` and `cbc:*URI` (all 143 elements of UBL 2.5 type IdentifierType that the examples use), with parent paths, plus every attribute. Formats were checked with scripts against `world/countries.json`, `parties.json`, `items.json` and the check-digit rules in `tools/world_parties.py`, `tools/world_items.py`, `tools/examples_kit.py`. Consistent with `codelist-classification.md` (its `R:` = `urn:ubl-examples:world:codelist:<Name>Code`).*

## Summary

**Counts.** 143 identifier element types, 12,628 occurrences (11,947 `…ID`, 681 `…URI`), 2,663 with schemeID, on 3 element names only (ID 2,076, ElectronicAddressID 582, VesselID 5). 14 schemeIDs today. Grouped by (element, parent) there are 599 groups; about 85 % of all occurrences are local identifiers that need no scheme.

**Missing schemeID where a scheme exists** (must-fix, ≈ 2,720 occurrences):
- tax and register numbers in `PartyLegalEntity/CompanyID` (582) and `PartyTaxScheme/CompanyID` (467);
- RF creditor references in `PaymentID` (50); bank codes in `FinancialInstitution/ID` (89);
- ISINs in `SecurityListing/ID` and `SecurityID` (74); agency property numbers in `StandardPropertyIdentification/ID` (45);
- endpoint in `DigitalDeliveryChannel/ParticipantID` (4), register number in `BusinessIdentityEvidenceID` (1);
- codes carried in ID elements: TaxCategory ×3 (170), TaxScheme (622), Language ×4 (596), HazardClassID and SecondaryHazard/ID (18);
- three slips: 2 DeliveryTerms/ID and 1 container (two elements) without the scheme their siblings carry.

**Optional schemeIDs**, where the element name already says what it is: plates, aircraft, wagon, call sign, MMSI, national ID, driving licence, payment rail. About 110 occurrences, plus AttributeID (413) if it becomes a code list.

**Proposed convention** (mirrors the listID convention):
- **Real external schemes**: the scheme's official short name, as UBL writes listIDs: `UN/LOCODE`, `ISO 6346`, `ISO 11649`, `ISO 6166`, `Incoterms 2020`.
- **An ID that carries a code from a list**: schemeID = that list's listID, exactly as in the code list (`UN/EDIFACT EDED 5305`, `UN/EDIFACT EDED 5153`, `ISO 639`, `ISO 3166`).
- **Regional (Trade Accord) schemes**: `urn:ubl-examples:world:scheme:<Name>`, shown as `S:<Name>`.
- **National schemes**: `urn:ubl-examples:world:<CC>:scheme:<Name>`, shown as `XB:S:<Name>`.
- **Same name in every country**: CompanyRegister, TaxNumber, CustomsTrader, ShipRegister …
- **The register's own `CorporateRegistrationScheme/ID`** carries the same URN as the schemeID (today `XB:FBR`).
- **Effect on today's values**: all 2,627 non-LOCODE schemeID values change name (Q1 offers "keep the current names").

**Most important findings**
1. **ISIN check digit wrong.** `XU0001042505` fails ISO 6166 (Luhn), and the correct form is `XU0001042501`. It occurs 74 times in 73 files: SecurityListing/ID in all Valdara Industries party blocks (e.g. ore/01-Order.xml), plus SecurityID in tender/14-GuaranteeCertificate.xml.
2. **Wrong UUID reference.** retail/03-CataloguePricingUpdate, retail/04-CatalogueItemSpecificationUpdate and retail/20-CatalogueDeletion reference catalogue LD-CAT-26-0218 with UUID `8fbee548-a66b-588f-b69b-2e8546501907`. The catalogue itself (retail/02-Catalogue.xml) has UUID `f5163e36-0159-5b9f-b172-a86137e369e6`.
3. **All other check digits and formats pass.** This covers 133 world item numbers, 89 account numbers (ISO 13616 mod 97), 50 RF references, 4 distinct ISO 6346 container numbers, all XU VAT numbers (mod 11), and all XB permits, whose state matches the party's state.
   It also covers the registers (XU-R-nnnnnn / 8 digits / ICnnnnn), the customs trader numbers, the 582 endpoints, the 36 LOCODEs (all 7 known places) and the 272 UUIDs (all valid RFC 4122 v5).
4. **Codes in ID elements.**
   - **No fix needed**: Incoterms in DeliveryTerms/ID, because UBL 2.5 has no Incoterms code element. Likewise UNCL 5305 in TaxCategory/ID and UNCL 5153 in TaxScheme/ID; these are the normal UBL places.
   - **Wrong element**: ISO 6346 size-type codes `22G1`/`42G1`/`45R1` in (Un)SupportedTransportEquipment/ID and in TransportEquipment/ID (sea/08) belong in `SizeTypeCode`. Words in AttributeID (`Length`, `Pallet places`) and TypeID (`Sulphur`) are labels, not identifiers.
5. **Text or placeholders in IDs**: `none`, `to follow`, `Harbour parks Selanu`, `World reference rate`, `Codana street furniture properties`, ranges `SE-CR-1..6`, `JB-001..120`, `LD-AIR-0001..0008`. Internal party ids leak into values (`5-xu-SP-8-xu`, `6-XB-PL-2026`, `ACCORD-CERT-1-xl`).
6. **Realistic look-alikes that may collide with real registries.** World item numbers are structurally valid GTIN-12s, and `0771…` reads as a GS1 US prefix. ISO 6346 owner codes TWL/FRC are BIC-registered codes in real life. Call signs `XB…`/`XU…` are in ITU blocks of Mexico and Cambodia. Air ULD `RKN-41207-KC` uses KC, a real IATA airline code. MMSIs `99…` read as aids to navigation. AID `A000009999…` is a real-format RID.
7. **unitCode change to EA**: H87 (476 uses, 95 files) and C62 (79 uses, 28 files) → EA. EA is right for counted articles, packages and units. It is wrong for:
   - dimensionless numbers: Gross/NetTonnageMeasure, PalletSpace 0.5;
   - RateOfTurnMeasure (use `E96`);
   - persons (`IE` is better);
   - TEU capacity (use `20`);
   - shares (`E21`).
   One more real unit error: ballast `VolumeMeasure` in TNE (should be MTQ).
8. **languageID is not validated.** The UBL Language list is upper case and holds `QAA-QTZ` as one literal entry, so `QAU`/`QAL` can never match. A world Language copy adding QAU and QAL is needed, plus a world CVA context for `@languageID` with a case decision (Q6).

---

## Part A — identifier schemes

Kind: **L** local to the sender or issuer · **W** issued by a world authority · **X** real external scheme · **U** UUID · **C** a code, not an identifier. Need: **Yes** / **Opt** (element name already says it) / **No**.

### A1 Party identifiers

| Element | Context | Examples | Now | Kind | Need | Proposed | Issuer | Format | Problems |
|---|---|---|---|---|---|---|---|---|---|
| ID | PartyIdentification (1,462) | XU-R-104274, 20410274, IC41859 | `…:XU/XB/XL:register` | W | Yes | `XU/XB/XL:S:CompanyRegister` | national register (countries.json `registry`) | XU `^XU-R-\d{6}$`, XB `^\d{8}$`, XL `^IC\d{5}$`; no check digit | ✓ all match the scheme's country and parties.json |
| CompanyID | PartyLegalEntity (582) | same values | – | W | **Yes** | same as PartyIdentification | same | same | No schemeID at all; same number as PartyIdentification |
| CompanyID | PartyTaxScheme (467: XU 174, XB 293) | XU007299291, UL-1230822 | – | W | **Yes** | `XU:S:TaxNumber`, `XB:S:TaxNumber`; XL parties use `XL:S:CompanyRegister` (no tax number) | XU tax office; XB state | XU `^XU\d{9}$`, mod 11, weights 9..2 over 8 digits, remainder 10 never issued; XB `^(UL\|CO)-\d{7}$`, no check digit, state = party's state | ✓ all valid |
| ID | AdditionalPartyIdentification (309) | XB-TR-410274, XL-TR-041859 | `…:<CC>:customs-trader` | W | Yes | `<CC>:S:CustomsTrader` | customs 19-xu/19-xb/19-xl | `^XU-TR-\d{6}$` etc.; no check digit | ✓ all = parties.json customs_id |
| ElectronicAddressID | ElectronicAddress (582) | XB:20410274, XU:XU-R-104274 | `…:endpoint` | W | Yes | `S:Endpoint` | Trade Accord network (32-xb) | `^X[UBL]:<register no.>$` | ✓; `XU:XU-R-…` repeats XU (cosmetic) |
| ParticipantID | DigitalDeliveryChannel (4) | XL:IC41859 | – | W | **Yes** | `S:Endpoint` | 32-xb | as above | Missing schemeID |
| BusinessIdentityEvidenceID | MainQualifyingParty (1) | XU-R-104274 | – | W | **Yes** | `XU:S:CompanyRegister` | register | as above | Missing schemeID |
| ID | CorporateRegistrationScheme (582) | XB:FBR, XU:CR, XL:ICR | – | name of scheme | No | value → the scheme URN | – | – | Third name for the same register (vs `…:XB:register` and the endpoint prefix) |
| ID | SecurityListing (73), SecurityID (1) | XU0001042505 | – | X | **Yes** | `ISO 6166` | world numbering agency (XU code = world copy of ISO 3166) | `^[A-Z]{2}[A-Z0-9]{9}\d$`, Luhn | **✗ check digit: should be XU0001042501** |
| ID | ServiceProviderParty (73) | 5-xu-SP-8-xu | – | L | No | – | – | – | Built from internal party ids; use a contract number (e.g. VI-SP-2026-01) |
| ID | PostalAddress (39) | LUM-ADR-000417 | – | W (city register) | Opt | `XB:S:LumeportAddress` | City of Lumeport | `^LUM-ADR-\d{6}$` | Only one value; Q8 |
| ID | SocialMediaProfile (40) | 10442197 | – | L (the medium) | No | – | – | – | – |
| AdditionalAccountID, CustomerAssignedAccountID, SupplierAssignedAccountID | Customer/SupplierParty (6) | BM-6120, LD-C-0418 | – | L | No | – | – | – | – |
| LogoReferenceID | parties (40) | BM-LOGO-2024 | – | L | No | – | – | – | – |

### A2 Financial and payment

| Element | Context | Examples | Now | Kind | Need | Proposed | Issuer | Format | Problems |
|---|---|---|---|---|---|---|---|---|---|
| ID | Payee/Payer/Financing/FinancialAccount (89) | XB66BLUM0004712805 | `…:account` | W | Yes | `S:AccountNumber` | the bank; structure set by the Trade Accord | `^X[UBL]\d{2}[A-Z]{4}\d{10}$`; ISO 13616 mod 97-10 | ✓ all; correctly *not* called IBAN or `ISO 13616` |
| ID | FinancialInstitution (89) | BLUM, CREV, BSEL | – | W | **Yes** | `S:BankCode` | Trade Accord / central banks (Q9) | `^[A-Z]{4}$` = account chars 5–8 | Not a BIC (ISO 9362 is 8/11 chars); do not claim it |
| ID | FinancialInstitutionBranch (89) | BLUM-001 | – | L (bank) | No | – | – | – | – |
| PaymentID | PaymentMeans (50) | RF20LDINV260147 | – | X | **Yes** | `ISO 11649` | creditor (structure: ISO) | `^RF\d{2}[A-Z0-9]{1,21}$`, mod 97-10 | ✓ all 50 |
| PaymentRailID | PaymentMeans (38) | LUMEPAY, FERRA-RTGS, CORAL-NET, TRADE-ACCORD-PAY | – | W (system id) | Opt | `S:PaymentSystem` | central banks / Trade Accord | countries.json `payment.system.id` | Same values proposed for PaymentChannelCode (prior Q18) |
| BlockchainID | PayeeFinancialAccount (2) | CORAL-NET-L1 | – | W | Opt | `S:PaymentSystem` | Bank of Selanu | countries.json ledger id | – |
| NetworkID, IssuerID, MerchantID | CardAccount, Payment (5) | LUMECARD, BLUM, LUMECARD-M-0026118 | – | L (card network) | No | – | – | – | – |
| PrimaryAccountNumberID, CV2ID | CardAccount (3) | ************2286, *** | – | X (masked PAN) | No | – | – | – | Masked: fine |
| ChipApplicationID | CardAccount (1) | A0000099990001 | – | X-shaped (ISO/IEC 7816-5 AID) | No | – | – | RID 10 hex + PIX | RID `A000009999` is a real-format registered RID (doubtful) |
| ID / InstructionID / TransactionID / AuthorizationID / PaymentTerminalID / PaymentPlatformID / PrepaidPaymentReferenceID / SignatureID | Payment, PaymentMeans, PrepaidPayment, PaymentMandate | VT-PAY-26-0199, TX-26-0518-773104, CSW-DD-2024-08812 | – | L | No | – | – | – | – |
| ID | PaymentMeans (39) `1`, PaymentTerms (36) XB-STD/DEPOSIT, PaymentMeansID (34) | 1, XB-STD | – | L | No | – | – | – | – |
| ExchangeMarketID | PricingExchangeRate (5) | World reference rate | – | W | Opt | – | central banks | – | A sentence; use a short id (e.g. `WRR`) |
| ImmobilizationCertificateID | ImmobilizedSecurity (1) | BLUM-IMM-26-0044 | – | L | No | – | – | – | – |

### A3 Items, properties, classification

| Element | Context | Examples | Now | Kind | Need | Proposed | Issuer | Format | Problems |
|---|---|---|---|---|---|---|---|---|---|
| ID | StandardItemIdentification (126), AdditionalItemIdentification (7) | 771020000027, 772010000065 | `…:item` | W | Yes | `S:ItemNumber` | Codana Identification Agency (31-xu) | `^77[123]\d{9}$` (771 XU, 772 XB, 773 XL makers); mod 10, weights 3/1 from the right | ✓ all 133; structurally a valid GTIN-12 (doubtful: may be read as a real GTIN, prefix 0771 = GS1 US) |
| IssuerScopeID | StandardItemIdentification (38) | 771 | – | W | No | – | 31-xu | first 3 digits | Only given where a barcode is given; never for 772/773 |
| BarcodeSymbologyID | StandardItemIdentification (38) | Code128 | – | C | Opt | – | – | – | Code-like; no list |
| ID | StandardPropertyIdentification (45) | UR-SF-0450, UR-WD-0012 | – | W | **Yes** | `S:ItemProperty` | 31-xu | `^UR-[A-Z]{2}-\d{4}$` | Missing schemeID |
| IssuerScopeID | StandardPropertyIdentification (45) | Codana street furniture properties | – | W | No | – | 31-xu | – | A sentence; use a code (`SF`, `WD` – already in the ID) or drop |
| ID | Sellers/Buyers/Manufacturers/CatalogueItemIdentification (239), ExtendedID (41), *RelatedItem (10) | LD-10442, VI-B180, GRY | – | L | No | – | – | – | – |
| ProductTraceID, RegistrationID, SerialID | ItemInstance (120) | VI-TR-03190, VI-QR-03190, VI-SF-03190 | – | L | No | – | – | – | – |
| LotNumberID | LotIdentification (6) | VI-LOT-260426 | – | L | No | – | – | – | – |
| ID | AdditionalItemProperty (83) COL/LOAD/MC, ItemPropertyGroup (83) APP/SAF/QUA | COL | – | L | No | – | – | – | – |
| TypeID | AdditionalFuelProperty, FuelMetering (2) | Sulphur, FlowMeter | – | C | No | – | – | – | Words, not ids |
| ID | BusinessClassificationScheme (1), RequiredBusinessClassificationScheme (4) | ISIC4 | – | name of list | No | value → `ISIC Rev.4` (= listID) | – | – | Differs from the listID used |
| ID | RequestedClassificationScheme (1) | HS | – | name of list | No | value → `WCO HS 2022` | – | – | – |
| ID | RequiredClassificationScheme (4) | LUM-BUDGET | – | L | No | – | – | – | – |
| AgencyID | RequestedClassificationScheme (1) | WCO | – | C | No | – | – | – | Fine as text-like id |
| BusinessClassificationEvidenceID | MainQualifyingParty (1) | ISIC-3100 | – | L | No | – | – | – | Holds a class, not evidence; use an evidence document id |
| RequiredCustomsID | GoodsItem (1) | 3901.10.00 | – | C | No | – | – | – | A tariff number; belongs in CommodityClassification/ItemClassificationCode (national tariff list) |

### A4 Transport means, equipment, locations

| Element | Context | Examples | Now | Kind | Need | Proposed | Issuer | Format | Problems |
|---|---|---|---|---|---|---|---|---|---|
| ID | TransportEquipment (9), ContainingTransportEquipment, ReferencedTransportEquipment | TWLU4120872, FRCU1044171 | `ISO6346` | X | Yes | `ISO 6346` (with space) | owner (BIC registry) | `^[A-Z]{3}U\d{7}$`, mod 11 | ✓ check digits; TWL/FRC are invented owner codes in a registry with real holders (doubtful) |
| ID | TransportEquipment + GoodsItemContainer, sea/14-BillOfLading (2) | TWLU4120872 | – | X | **Yes** | `ISO 6346` | – | – | **Missing schemeID** (siblings have it) |
| ID | TransportEquipment, sea/08 (1); Supported/UnsupportedTransportEquipment (3) | 42G1, 22G1, 45R1 | – | C | – | → `SizeTypeCode` (listID ISO 6346) | – | – | **Code in an ID** |
| ID | TransportEquipment / TransportHandlingUnit (air ULD, 4) | RKN-41207-KC | – | X-shaped (IATA ULD) | Opt | `IATA ULD` (doubtful) | – | `^[A-Z]{3}\d{4,5}[A-Z0-9]{2}$` (no hyphens) | Hyphens are not IATA format; KC is a real IATA airline code |
| ID | AttachedTransportEquipment (1) | BV CH 0412 | – | W (plate) | Opt | `XB:S:VehicleRegistration` | XB vehicle register | – | – |
| ID | TransportEquipmentSeal (6) | XU-VI-30411, TWL-S-0884213 | – | L (sealing party) | No | – | – | – | – |
| TraceID | TransportEquipment (1) | TRK-FRCU1044171 | – | L | No | – | – | – | – |
| VesselID | MaritimeTransport (5) | XB-S-20117, XU-IW-08042 | `…:vessel` | W | Yes | `XB:S:ShipRegister`, `XU:S:ShipRegister` | national ship registers (XL: 30-xl) | `^XB-S-\d{5}$`, `^XU-IW-\d{5}$` | The .md says "its country's register": national, not regional; not IMO (right: no real IMO numbers) |
| MMSIRegistrationID | MaritimeTransport (5) | 999702117 | – | X-shaped | Opt | – | – | 9 digits | 99-prefix = aid-to-navigation format (doubtful; MID 999 unallocated is the intent) |
| RadioCallSignID | MaritimeTransport (5) | XBTH7, XUBF4 | – | X-shaped | Opt | – | – | – | XB/XU are ITU call-sign blocks of Mexico/Cambodia |
| RegistrationNationalityID | TransportMeans (12) | XU, XB, XL | – | C | Opt | `ISO 3166` (world copy) | – | – | Country code in an ID |
| LicensePlateID, TrailerLicensePlateID | RoadTransport (6) | BV LP 2203, UR TR 3381 | – | W | Opt | `<CC>:S:VehicleRegistration` | national vehicle register | UR/BV/LV + 2 letters + 4 digits | ✓ = parties.json fleet |
| AircraftID | AirTransport (2) | XL-KAC | – | W | Opt | `XL:S:AircraftRegister` | XL civil aviation | `^XL-[A-Z]{3}$` | – |
| RailCarID, StowagePositionID | RailTransport, TransportEquipment (2) | XU-FRC 4521 0042 | – | W | Opt | `XU:S:RailVehicleRegister` | XU rail register | – | Not the UIC 12-digit format (fine) |
| TrainID, JourneyID | Rail/TransportMeans (17) | FRC 4417, KAC207, TH-26-19E | – | L | No | – | – | – | – |
| ID | Location, PhysicalLocation, *PortLocation, Loading/Unloading/Delivery/FreightCharge/WHOAffectedArea (36) | XUFER, XBLMP | `UN/LOCODE` | X (world entries) | Yes | `UN/LOCODE` (keep) | UNECE; world copy | `^X[UBL][A-Z]{3}$` | ✓ 7 known places; needs a world LOCODE copy to validate |
| ID | OriginAddress (3) | 33/03 | `…:grid` | W | Yes | `S:MapGrid` | world map | `^\d{2}/\d{2}$` | – |
| LocationID, StowagePositionID | Stowage, TransportEquipment (2) | 140282 | – | X-shaped (bay/row/tier) | Opt | `ISO 9711` (doubtful) | – | BBRRTT | – |
| LocationID, GateID, PositionInPortID, ID | PositionOnBoardStowage, Storage, DestinationPortCall | MD-L2, Gate B, BERTH-2, XLSEL-26-0517 | – | L | No | – | – | – | – |
| HazardClassID | HazardousItem, LoadedHazardousItem (14) | 9, 8, 7 | – | C | **Yes** | `UN Model Regulations hazard class` | – | – | Same codes now proposed for HazardousCategoryCode (prior analysis): duplicate |
| ID | SecondaryHazard (4) | 3 | – | C | **Yes** | same | – | – | – |
| MarkingID | HazardousItem (12) | UN3480 | – | X | No | – | – | `UN` + UN number | Marking text; the number itself is in UNDGCode |
| Upper/LowerOrangeHazardPlacardID | LoadedHazardousItem (4) | 90, 3480 | – | X | Opt | ADR hazard id no. / `UN/EDIFACT EDED 7124` | – | – | – |
| ID | HazardousItem (12) | SE-BAT-48100-DG | – | L | No | – | – | – | – |
| ID / TraceID | Package (32), ActualPackage (25), Contained/ContainingPackage, TransportHandlingUnit (35), PackagedTHU (25) | LD-26-001, CL-26-001-1 | – | L | No (Q7) | – | – | – | **Ranges in one ID**: `SE-CR-1..6`, `JB-001..120`, `LD-AIR-0001..0008` |
| ID / *AssignedID / ShippingOrderID / TrackingID | Consignment, Shipment, ShipmentStage, ChildConsignment … | LD-CS-26-0324, KAC-AWB-26-0319 | – | L | No | – | – | – | AWB not in IATA 3+8 digit form (fine for local) |

### A5 Persons

| Element | Context | Examples | Now | Kind | Need | Proposed | Issuer | Format | Problems |
|---|---|---|---|---|---|---|---|---|---|
| NationalID | Person (1) | XU-NID-55102311 | – | W | Opt | `XU:S:NationalID` | XU civil register | `^XU-NID-\d{8}$` | – |
| ID | DriverPerson (1) | XU-DL-0417722 | – | W | Opt | `XU:S:DrivingLicence` | XU licensing authority | `^XU-DL-\d{7}$` | Licence number as person ID: fine |
| ID | IdentityDocumentReference (1) | XU-P-2210931 | – | W (document) | No | – | – | – | Document rule (A6) |
| ID | Person (1), Contact (40) | VI-E-0412, BM-CT-01 | – | L | No | – | – | – | – |

### A6 Documents, certificates, licences (local to the issuer: no scheme)

Rule: a document's ID is unique within its issuer. The issuer is the document's own party (IssuerParty, sender) or the referenced document's context, so no schemeID is given. This also holds for authority documents: certificates, licences, carnets, customs declarations, passports. Add IssuerParty where it is missing (Q10).

| Element | Context | Examples | Kind | Problems |
|---|---|---|---|---|
| ID | document root (230), all *DocumentReference (≈ 500), OrderReference, BillingReference … | VI-RM-26-0316, LD-INV-26-0147 | L | `RemittanceDocumentReference/ID` = `to follow` (sea/24); `ShipSanitationControlExemptionDocumentReference/ID` = `none` (sea/16): omit the element instead |
| ID | Certificate (44), EnvironmentalCertificate (5), ISPSRequirements, MedicalCertificate, ShipSanitationControlCertificate, RegistryCertificateDocumentReference | XU-HAUL-2020-0877, ISSC-XL-2026-0117 | W (authority's own numbering) | Only XL-CLS-2026-0042 has an IssuerParty |
| CertificateReferenceID | Certificate (7) | XB-FOR-REG-0118 | W | vs Certificate/ID XB-FOR-2025-118 |
| GoodsItemPassportID, GoodsItemPassportCounterfoil/ID | ATA carnet (13) | FCC-DOC-26-0724, IMP-1 | W (chamber) | – |
| ID | CustomsDeclaration (10), PreviousCustomsDeclaration (8) | VI-CD-26-0156 | L (declarant) | No customs-issued MRN anywhere (fine) |
| ID | Contract, TransportContract, InsurancePolicy, ForeignExchangeContract, TradeFinancing, Clause, PenaltyClause, PowerOfAttorney | FE-C-0047120, WS-CP-26-4471 | L | – |
| ID | ProjectReference (10) | Harbour parks Selanu | L | A name in an ID (sea/26, sea/28) |
| ID | PriceList (7), ServiceLevelAgreement, TransactionConditions | 6-XB-PL-2026 | L | Internal party id in the value |
| ID | DigitalCertificate (4) | ACCORD-CERT-1-xl | L | Internal party id in the value |
| ID / VersionID / PreviousVersionID / ContractFolderID / BuyerEventID / SellerEventID / OriginalJobID / PreviousJobID / ReferenceID / DocumentID / ValidatorID | various | PWD-2026-PARKS, 1.2 | L | – |

### A7 Lines, sequences, versions (local; no scheme)

All `…Line/ID`, `Sub…Line/ID`, `LineID` (83), SalesOrderLineID, ParentDocumentLineReferenceID, RequestForQuotationLineID, RevisedForecastLineID, ShipmentStage/ID, GoodsItem/ID, SequenceID, SequenceNumberID, SuccessiveSequenceID, LoadingSequenceID, ReleaseID, PaymentMeansID, VariantID, DocumentDistribution/ID: values `1`, `1.1`, `2`, `1-A`, `V0`. No problems. ReleaseID `XU-EX-REL-55120` (Despatch) is a customs release number (W, local to customs; no scheme).

### A8 Process, procurement, utilities, telecom (local; no scheme)

| Group | Examples | Problems |
|---|---|---|
| Procurement: ProcurementProject(Lot), AwardingCriterion(+Response), TenderingCriterion*, Evidence, LotsGroupID, OpenTenderID, TenderEnvelopeID, AwardID, IdentificationID … | LOT-1, AC-2.1, P-1, ENV-1 | – |
| Utilities: UtilityConsumptionPoint, SubscriberID, ConsumptionID, ConsumptionReportID, MeterReading, UtilityItem, PurchaseReference | FE-CP-4120-01, FE-C-0047120, FE-M-881204 | Supplier-local. Real markets use grid-operator metering-point ids; only a regional scheme would add that (not proposed) |
| Telecom: TelecommunicationsService/ID | S-03-1 | – |
| Digital agreement: DigitalProcess, DigitalCollaboration, Sending/ReceivingDigitalService | ordering-1, LD-Order-IN | – |
| ProtocolID AS4, FormatID UBL, EncryptionSymmetricAlgorithm/ID AES-256-GCM, OID | 2.16.840.1.101.3.4.1.46 | OID ✓ is the real NIST OID of AES-256-GCM |
| Cash register ID / SerialNumberID, WeighingDeviceID, TankID, WorkItemID, ShipStoreArticle … | C1, LD-SCALE-03, BT-3 | – |

### A9 UUID, URIs, header identifiers

| Element | Kind | Need | Notes |
|---|---|---|---|
| UUID (272: 230 documents, 42 lines/references) | U | No | All valid v5. **✗ retail/03, /04, /20**: reference UUID ≠ the catalogue's UUID (finding 2). The same line UUID under ProcurementProject and the lot in tender/02, /03, /21 is the same line: OK |
| UBLVersionID 2.5, CustomizationID `urn:ubl-examples:world`, ProfileID `urn:…:process:*`, ProfileExecutionID | L (world) | No | – |
| ExchangeNetworkID `urn:ubl-examples:world:network` | W | No | – |
| all `…URI` (681) | L | No | All under `.example` ✓; EndpointURI `ap.1-xl.example` uses an internal party id |

### A10 Codes carried in ID elements

| Element | Uses | Content | Correct UBL element | Proposal |
|---|---|---|---|---|
| DeliveryTerms/ID | 35 (33 `INCOTERMS`, **2 none**: road/08-Waybill FCA, sea/14-BillOfLading CIF) | Incoterms | No code element in UBL 2.5 (only ID, SpecialTerms, LossRiskResponsibilityCode) | Keep the ID; schemeID `Incoterms 2020` everywhere |
| TaxCategory / ClassifiedTaxCategory / ApplicableTaxCategory /ID | 93 + 61 + 16 | S, E, G, O (UNCL 5305) | ID is UBL's place for it | schemeID `UN/EDIFACT EDED 5305` |
| TaxScheme/ID | 622 | STT, VAT, EXC, OTH (UNCL 5153 ✓) | ID (TaxTypeCode is another concept) | schemeID `UN/EDIFACT EDED 5153` |
| Language, AdditionalNoticeLanguage, DefaultLanguage, RequestedLanguage /ID | 589 + 4 + 2 + 1 | en 321, qau 178, qal 97 | ID; LocaleCode holds the code | schemeID `ISO 639` (world copy); case Q6 |
| Supported/UnsupportedTransportEquipment/ID; TransportEquipment/ID sea/08 | 4 | 22G1, 42G1, 45R1 | SizeTypeCode | Move to the code; drop the ID or give a local one |
| HazardClassID, SecondaryHazard/ID | 18 | 9, 8, 7, 3 | ID is UBL's place | schemeID `UN Model Regulations hazard class` |
| RegistrationNationalityID | 12 | XU, XB, XL | ID | schemeID `ISO 3166` (optional) |
| Dimension…/AttributeID, Temperature/AttributeID | 413 | Length, Height, Colour, Pallet places, TEU, Battery, Hall | ID | Words today. Either UN/EDIFACT 6313 measured-attribute codes (LN/WD/HT …, doubtful fit for `Seat height`, `Pallet places`) or a regional list `R:MeasuredAttribute` with codes. Q5 |
| RequiredCustomsID | 1 | 3901.10.00 | ItemClassificationCode | Move |
| ExchangeMarketID, IssuerScopeID (properties), BusinessClassificationEvidenceID | 51 | sentences / class | – | Short ids |

### Scheme registry (proposed)

`S:` = `urn:ubl-examples:world:scheme:`; `XU:S:` = `urn:ubl-examples:world:XU:scheme:`.

| Scheme | Issuer | Format | Check | Elements | Replaces |
|---|---|---|---|---|---|
| `XU:S:CompanyRegister` | Commercial register of Urvania | `^XU-R-\d{6}$` | – | PartyIdentification/ID, PartyLegalEntity/CompanyID, BusinessIdentityEvidenceID; PartyTaxScheme/CompanyID (XL only) | `…:XU:register` |
| `XB:S:CompanyRegister` | Federal business register | `^\d{8}$` | – | same | `…:XB:register` |
| `XL:S:CompanyRegister` | Island companies register | `^IC\d{5}$` | – | same, also as the XL tax number | `…:XL:register` |
| `XU:S:TaxNumber` | Urvanian tax office | `^XU\d{9}$` | mod 11, weights 9..2 | PartyTaxScheme/CompanyID | – |
| `XB:S:TaxNumber` | state tax office (UL/CO) | `^(UL\|CO)-\d{7}$` | – (state = party's state) | PartyTaxScheme/CompanyID | – |
| `<CC>:S:CustomsTrader` | 19-xu / 19-xb / 19-xl | `^<CC>-TR-\d{6}$` | – | AdditionalPartyIdentification/ID | `…:<CC>:customs-trader` |
| `S:Endpoint` | Trade Accord Council 32-xb | `^(XU\|XB\|XL):<CompanyRegister>$` | – | ElectronicAddressID, ParticipantID | `…:endpoint` |
| `S:ItemNumber` | Codana Identification Agency 31-xu | `^77[123]\d{9}$` | mod 10, weights 3/1 from the right | Standard/AdditionalItemIdentification/ID | `…:item` |
| `S:ItemProperty` | 31-xu | `^UR-[A-Z]{2}-\d{4}$` | – | StandardPropertyIdentification/ID | – |
| `S:AccountNumber` | banks, Trade Accord structure | `^X[UBL]\d{2}[A-Z]{4}\d{10}$` | ISO 7064 mod 97-10 (ISO 13616 structure) | *FinancialAccount/ID | `…:account` |
| `S:BankCode` | Trade Accord (Q9) | `^[A-Z]{4}$` | – | FinancialInstitution/ID | – |
| `S:PaymentSystem` (opt.) | central banks / Trade Accord | FERRA-RTGS, LUMEPAY, CORAL-NET, TRADE-ACCORD-PAY, CORAL-NET-L1 | – | PaymentRailID, BlockchainID | – |
| `S:MapGrid` | world map | `^\d{2}/\d{2}$` | – | Address/ID (offshore) | `…:grid` |
| `XB:S:ShipRegister`, `XU:S:ShipRegister` | national ship registers | `^XB-S-\d{5}$`, `^XU-IW-\d{5}$` | – | VesselID | `…:vessel` |
| `<CC>:S:VehicleRegistration` (opt.) | national vehicle registers | `^(UR\|BV\|LV) [A-Z]{2,4} \d{1,4}$` | – | LicensePlateID, TrailerLicensePlateID, AttachedTransportEquipment/ID | – |
| `XL:S:AircraftRegister`, `XU:S:RailVehicleRegister`, `XU:S:NationalID`, `XU:S:DrivingLicence` (opt.) | national authorities | see A4/A5 | – | AircraftID, RailCarID, NationalID, DriverPerson/ID | – |
| `UN/LOCODE` | UNECE (world entries in a world copy) | `^X[UBL][A-Z]{3}$` | – | every Location-type ID | keep |
| `ISO 6346` | BIC (owner codes) | `^[A-Z]{3}[UJZ]\d{7}$` | mod 11 (values 2^i) | TransportEquipment-type ID | `ISO6346` |
| `ISO 11649` | ISO (creditor builds it) | `^RF\d{2}[A-Z0-9]{1,21}$` | mod 97-10 | PaymentID | – |
| `ISO 6166` | national numbering agency (world) | `^[A-Z]{2}[A-Z0-9]{9}\d$` | Luhn on letter-expanded digits | SecurityListing/ID, SecurityID | – |
| `Incoterms 2020` | ICC | EXW…DDP (11) | – | DeliveryTerms/ID | `INCOTERMS` |
| `UN/EDIFACT EDED 5305` / `5153` | UN/CEFACT | code lists | – | Tax category / scheme IDs | – |
| `ISO 639`, `ISO 3166`, `UN Model Regulations hazard class` | – | same lists as the code elements | – | Language IDs, RegistrationNationalityID, hazard class IDs | – |

Phase 2 (`tools/validate_examples.py`) checks no schemeID today. A world CVA context could bind allowed schemeIDs per element path, and a small phase-3 check could run the regexes and check digits above.

---

## Part B — code-valued attributes

### currencyID (1,547 uses on 83 amount elements)

| Value | Uses | Validated | List | Notes |
|---|---|---|---|---|
| XBL | 991 | ✓ UBL CVA `@currencyID` → CurrencyCode-2.4-world | `ISO 4217 Alpha` (world copy) | 2 decimals; only prices and CorporateStockAmount (0 decimals) differ, which is allowed |
| XUF | 376 | ✓ | same | 0 decimals; 9 PriceAmounts with 1 decimal (unit prices, allowed) |
| XLC | 180 | ✓ | same | 3 decimals; some PriceAmounts with 0–2 (allowed) |

No problems. No world copy beyond the existing one.

### mimeCode (3)

| Value | Elements | Validated | Notes |
|---|---|---|---|
| application/pkcs7-signature | EmbeddedDocumentBinaryObject (1) | ✓ BinaryObjectMime-2.4 (`IANA Media Types`) | – |
| text/plain | EmbeddedDocumentBinaryObject, ResponseBinaryObject (2) | ✓ | – |

### languageID (1,224 uses; not bound by any UBL CVA context)

| Value | Uses | Elements | Should bind to | Issues |
|---|---|---|---|---|
| en | 612 | StreetName 291, CityName 193, Note 64, Item/Name 64 | world Language copy | Lower case; Language-2.4 is upper case (`EN`) |
| qau | 483 | StreetName 193, CityName 193, Item/Name 52, Note 45 | world copy + **QAU = Urvanian** | Valid ISO 639-2 local-use code (qaa–qtz). The UBL list holds only the literal `QAA-QTZ`, so it can never match |
| qal | 129 | StreetName 98, Note 19, Item/Name 12 | world copy + **QAL = Lisavan** | Same |

Related codes:
- LocaleCode is `EN` (317); NoticeLanguageCode, PreferredLanguageLocaleCode and TenderLanguageLocaleCode are `EN` (6).
- DefaultLanguageCode is `en` (41).
- Language/ID is lower case (596).
- qau/qal Language blocks carry no LocaleCode, because the list lacks the codes.
- parties.json has `"language": "EN"`.

The XSD type of languageID is `xsd:language` (BCP 47, conventionally lower case). Phase 2 compares codes literally. **Option A**: a world Language copy with upper-case codes, used by the code elements; plus a second world list, or a case-insensitive check, for `@languageID` and Language/ID in lower case. **Option B**: everything upper case. → Q6.

### unitCode (1,902 uses, 33 values; every element covered by the UBL CVA unit contexts; all values in UnitOfMeasure-2.4)

✓ = right Rec 20 unit for the element's meaning. "→EA" = affected by the decision to replace H87/C62 with EA.

| Code (Rec 20 name) | Uses / files | Main elements (contexts) | Verdict |
|---|---|---|---|
| **H87** piece | 476 / 95 | Quantity (Package 31, GoodsItem 24, LineItem 21, ActualPackage 25 …), Price/BaseQuantity 44, EnvironmentalEmission/ValueBaseMeasure 38, THU TotalGoodsItemQuantity/TotalPackageQuantity 56+56, Invoiced/Delivered/Received/Credited, Min/Max/Order quantities, EstimatedOverallContractQuantity, Business/TechnicalCapability ValueQuantity | **→EA** everywhere: all are counted articles or packages ✓. Capability ValueQuantity 2000/4000 lacks a time base (pieces *per year*?), whatever the unit |
| **C62** one | 79 / 28 | PalletSpace…/Measure 25, Gross/NetTonnageMeasure 5+5, EmployeeQuantity 6, ThresholdQuantity 4, Crew/Passenger 5, tender counts 6, ballast tank counts 4, ill/dead persons 2, RateOfTurnMeasure 1, SharesNumberQuantity 1, TotalCapacityDimension 1 (TEU), consignment/THU/goods-item counts 7, InvoicedQuantity "care kit" 1, Package/Quantity 1, Telecom Quantity 1 | **→EA ok** for counts of things (consignments, THUs, tanks, tenders, kits, packages). **EA wrong**: tonnage (dimensionless: keep C62); PalletSpace 0.5 (a share of a place: keep C62); RateOfTurn (**E96** degree per second); TEU capacity (**20** twenty foot container); persons (crew, passengers, employees, ill/dead: **IE** person); shares (**E21** shares) |
| SET set | 49 / 24 | Garden bench set Marrow (furniture), Ionisation smoke detector set (mast), Ground anchor set (tender), their prices, inventory and exception lines | ✓ real sets; keep |
| KGM kilogram | 325 / 95 | weights, ConsumptionMeasure, WasteMeasure, Load capacity property, emissions | ✓ |
| MMT millimetre | 382 / 70 | Dimension/Measure, Min/Max, MeasurementDimension, RangeDimension, staple length | ✓ |
| MTR metre | 6 | LoadingLength, MeasurementDimension 13.6, Altitude, SeaHeight | ✓ |
| MTK square metre | 25 | FloorSpaceMeasurementDimension | ✓ |
| MTQ cubic metre | 66 | volumes, water meters, MaritimeWaste | ✓ |
| DD degree / D61 minute [unit of angle] | 58 + 58 / 22 | Latitude/LongitudeDegreesMeasure, …MinutesMeasure | ✓ correct (angle, not the time minute MIN) |
| P1 percent | 23 / 16 | Iron content 62, Moisture 12/13, Recycled content 100, exception threshold 30 | ✓; iron content is a mass fraction: `60` percent weight would be more exact (optional) |
| 23 g/cm³ | 5 | Density 0.92 (PE granulate) | ✓ |
| 4H micrometre | 2 | Thickness 23 (film) | ✓ |
| 2Q kilobecquerel | 4 | ActivityLevelMeasure 37 (Am-241 in smoke detectors) | ✓ |
| GL gram per litre | 1 | SalinityMeasure 30 | ✓ acceptable (PSU / g/kg is usual; no g/kg code in the UBL list) |
| TNE tonne | 31 / 16 | goods quantities, ballast totals/capacity, SegregatedBallast, fuel, emissions | ✓, except **Up/Ex/DischargeBallastWaterTransaction/VolumeMeasure (3): a volume in TNE → MTQ** |
| CEL degree Celsius | 46 / 9 | temperatures; Actual/Normal/DifferenceTemperatureReductionQuantity | ✓ (KEL is stricter for differences; optional) |
| KWH / MWH | 49 / 8 | energy | ✓ |
| LTR, MQH, AMP, BAR, KNT | 7, 2, 2, 1, 1 | fuel/litres, max flow, rated current, gas pressure, speed | ✓ |
| ANN, MON, WEE, DAY, HUR, MIN | 44, 47, 1, 53, 19, 7 | durations, lead times, operating years, telecom minutes | ✓ |
| E34 gigabyte, E48 service unit, KMT km | 8, 13, 4 | telecom data, services, transport km | ✓ |

### listID / schemeID as names of lists and schemes

| Attribute | Current values | Proposal |
|---|---|---|
| listID (834) | ISIC Rev.4 582, HS 139, UN/EDIFACT EDED 4461 63, UNECE Rec 19 15, UNCL8273 14, EDED 8053 10, EDED 5189 8, UNCL4343 1, EDED 3155 1, IMO SOLAS 1 | As in codelist-classification.md (`WCO HS 2022`, `UN/EDIFACT EDED 7124`/`4343` …) |
| schemeID (2,663) | 14 values (A-registry "Replaces") | Registry above; `ISO6346` → `ISO 6346`, `INCOTERMS` → `Incoterms 2020` |
| scheme names held as *values* | CorporateRegistrationScheme/ID `XB:FBR`; Business/RequiredBusinessClassificationScheme/ID `ISIC4`; RequestedClassificationScheme/ID `HS` | Make them equal to the schemeID/listID strings |

---

## Open questions

1. **schemeID naming**: rename the existing 2,627 URNs to `urn:ubl-examples:world[:<CC>]:scheme:<Name>` (symmetrical with `…:codelist:<Name>Code`)? Or keep today's names (`…:XB:register`, `…:item`) and add the new ones in the same lowercase style (`…:XB:tax`, `…:payment-system`)?
2. **Code-in-ID**: accept the rule "schemeID = the list's listID" for TaxCategory/TaxScheme/Language/HazardClass/DeliveryTerms IDs (≈ 1,440 additions)? Or leave codes in IDs without a scheme, as many UBL users do?
3. **Optional schemes**: give schemeIDs to plates, aircraft, wagons, national ID and driving licence (national registers)? Or rely on the element name plus RegistrationNationalityID?
4. **Realistic look-alikes**:
   - Keep the GTIN-shaped item numbers, real-format ISO 6346 owner codes, ITU-block call signs, the IATA-style ULD with KC, and the 99-prefixed MMSIs?
   - Or make them visibly fictional, e.g. an item prefix outside GS1 use, owner codes known to be free, call signs and ULD owner from a world block?
5. **AttributeID** (413 words): UN/EDIFACT 6313 codes (external, doubtful fit) or a regional measured-attribute code list (`LENGTH`, `WIDTH`, `SEATHEIGHT`, `PALLETPLACES` …)?
6. **Language case**: lower-case languageID and Language/ID (BCP 47 style) plus upper-case LocaleCode (UBL list), with two world lists or a case-insensitive check? Or upper case everywhere? Either way, add QAU/QAL to a world Language copy.
7. **Packages and handling units**: keep sender-local IDs (proposed), or invent a world SSCC-like scheme (an ISO 15459 look-alike under 31-xu)? And split the range IDs (`SE-CR-1..6` …) into one Package per number, or keep ranges as text?
8. **Lumeport address register** (`LUM-ADR-000417`, 39 uses): give it a national/municipal scheme, or keep as local?
9. **Bank code issuer**: who issues `BLUM`/`CREV`/`BSEL`: the Trade Accord (regional `S:BankCode`, proposed) or each central bank (national schemes)?
10. **Certificates and licences**: keep "issuer-local, no schemeID" (proposed) and add the missing IssuerParty (only 1 of 5 certificates has one)? Or create national licence schemes (haulage, environmental, forestry, bonded warehouse)?
11. **unitCode exceptions to EA**: keep C62 for tonnage and the 0.5 pallet place; use IE for persons, E21 for shares, 20 for TEU, E96 for rate of turn. Agree, or EA for all counts except the dimensionless tonnage?
