# Code list classification — UBL example world

> Working analysis from the code-list and identifier review of November 2026. The decisions taken on it are in `analysis/codelist-decisions.md`, which wins where the two differ; the Q-numbers there refer to this table.


*Analysis only; nothing in the repository was changed. Sweep: 302 distinct `cbc:*Code` elements in the 230 examples under `world/examples/*/*.xml`, the reasons from the `.md` files, and the UBL 2.5 CVA data in `world/codelists/ubl-default-codes.json`. Re-swept independently; the counts match `codes.txt`.*

## Summary

**Elements per source** (302 in all)

- UBL default list, bound by the UBL 2.5 CVA: **31**
- UBL default list exists, but the UBL CVA does not bind the element (world CVA must): **6**
- External standard: **32**
- External standard, doubtful (fallback: regional): **10**
- Several lists by context (one element, different meanings): **18**
- National (XU / XB / XL): **4**
- Regional (Trade Accord): **197**
- Party-specific list (not world-wide; Q1): **4**

**Invented lists needed**: about **203 regional** (`R:` lists, incl. those for split elements) plus 6 fallback/follow-up lists if doubtful external choices are rejected or misused values are split off (CargoType, PackingInstruction, PaymentTermsEvent, RequirementType, StrategicProcurement, TransportAuthorization); **7 national** lists (XB:CompanyLegalForm, XB:CountrySubentity, XB:TaxExemptionReason, XL:CompanyLegalForm, XU:CompanyLegalForm, XU:CustomsTariff, XU:TaxExemptionReason); **4 party-specific** kinds (<buyer>:CostCentre, <buyer>:FundingProgramme, <buyer>:InvoiceRouting, <carrier>:TradeService) if you accept that category (Q1). 
Many regional lists are tiny (1–3 codes today) — see Q6 on merging.

**External lists to build or reference** (beyond the UBL defaults): UNCL 1001, 1225, 1229, 4343, 4465 (= UBL AllowanceChargeReason content), 7075, 7124, 8051, 8273, 8339; ISO 20022 ExternalPurpose1Code, ChargeBearerType1Code, ExternalServiceLevel1Code, ExternalCashAccountType1Code, SequenceType3Code; ISO 6346, ISO 5218; ISIC Rev.4; WCO HS 2022 (+ sections); UN Model Regulations (classes, packing groups); ADR tunnel codes; IMDG EmS; IMO ISPS levels, IMO INF classes; ITU-R M.1371; EPSG; IANA character sets; UNECE Rec 28; Basel Convention Annex IV. Doubtful ones are marked `EXT?`.

### Proposed listID conventions

- **UBL default lists**: exactly the listID of the UBL genericode — phase 2 (`tools/validate_examples.py`) compares it literally (`UN/EDIFACT EDED 4461`, `UNECE Recommendation 19 - Codes for Modes of Transport`, `ISO 4217 Alpha`, `ISO 3166`, `ISO 639`, `IANA Media Types`, `IMO SOLAS`). Nine UBL lists have **no listID** (Chip, DocumentStatus, LineStatus, Latitude/LongitudeDirection, Operator, SubstitutionStatus, WeekDay, ReceiptAdviceType): there a listID can only be given via a world copy that adds one (Q2).
- **Other external lists**: the same human-readable style UBL uses — `UN/EDIFACT EDED nnnn` for every UNCL list (replaces `UNCL4343`, `UNCL8273`), `UNECE Recommendation nn - <title>`, `ISO nnnn` / `ISO 20022 <CodeSetName>`, `WCO HS 2022` (replaces bare `HS`), `ISIC Rev.4` (kept), `IMO <instrument>`, `IANA <registry>`. The world genericode copy carries that string as `LongName Identifier="listID"`, like the existing Currency and Country copies.
- **Invented regional lists**: `urn:ubl-examples:world:codelist:<Name>Code` — the form the world already uses as CanonicalUri of `CurrencyCode-2.4-world.gc`. In the tables `R:AddressType` = `urn:ubl-examples:world:codelist:AddressTypeCode`.
- **Invented national lists**: `urn:ubl-examples:world:<CC>:codelist:<Name>Code` (pattern of the existing scheme `urn:ubl-examples:world:XB:register`). In the tables `XB:CountrySubentity` = `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`.
- **Party-specific lists** (if kept): `urn:ubl-examples:world:party:<party-id>:codelist:<Name>Code`, party id from parties.json (e.g. `13-xb`). Shown as `P:<buyer>:CostCentre`.

### Top problems

- **Wrong or misleading listIDs**: `UNCL8273` on all 14 UNDGCode (8273 is the dangerous-goods *regulations* list; UN numbers are 7124); `UN/EDIFACT EDED 5189` on AllowanceChargeReasonCode is UBL's own label, but its codes are UNCL 4465 — the .md reasons follow real 5189 (95 = discount, 64 = special agreement) while the validated list says 95 = small order processing charge, 64 = expecting new terms; 72/75/78 are not 5189 codes at all.
- **listID inconsistency**: outside PaymentMeans/TransportMode/TransportEquipmentType/ISIC/HS it is mostly absent; mixed within one element (AllowanceChargeReasonCode 8/18, ChannelCode 1/74, ResponseCode 1/14); three spellings for UN/EDIFACT lists (`UN/EDIFACT EDED 4461`, `UNCL4343`, `UNCL8273`). The PackagingType listID of UBL contains a line break, so it cannot be matched by an instance.
- **Sentences and spaces in codes** (9 elements): ImpactCode, ShipConfigurationCode, ScoringSystemCode, FullnessIndicationCode (`Cradle to gate`), TreatmentPathwayCode, SocialMediaTypeCode, MeterConstantCode, ActivityTypeCode, EmergencyProceduresCode (`F-A, S-I`), and slashes/hyphens in invented codes (FormatCode `PDF/A-3`, LifecycleStageCode `End-of-life`, TEC-90-3480, PI965-IA, XB-… exemption codes).
- **One element, several meanings** (18 split elements): ResponseCode (4 concepts), TypeCode (7), DocumentTypeCode (3), RoleCode (4), StatusCode, ConditionCode, SubscriberTypeCode, FunctionCode, PurposeCode, ProcedureCode, SubTypeCode, ContractTypeCode, CalculationMethodCode, DescriptionCode, FullnessIndicationCode, WasteTypeCode, Code, CommodityCode — the world CVA must bind lists by parent path, not by element name.
- **Semantic misuse**: HazardousCategoryCode `UN` (a regulation, not a hazard class); ItemClassificationCode `9988.00` (not HS); IndustryClassificationCode `3513` (NACE, not ISIC Rev.4); PaymentChannelCode `IBAN` (an account format); TransportMeansTypeCode `TE` (an equipment code); ActionCode `Trade`; MedicalFirstAidGuideCode holds ERG guide numbers; PaymentPurposeCode ELEC on a gas line, TRPT (road pricing) for return transport; EnvironmentalEmissionTypeCode `CO2` explained as CO2 equivalent; SubscriberTypeCode ELEC/WATE/TELE (utility types).
- **`None` used as a code** where the element should be omitted: PackagingDangerLevelCode, InhalationToxicityZoneCode, EmergencyProceduresCode, PreviousCancellationReasonCode, RankCode, Code (security clearance); CompanyLegalFormCode `Any`. (WeightingTypeCode/TranslationTypeCode `None` are meaningful and kept as NONE.)
- **Mixed styles**: ResponseCode (AP/CN with Grade/Met), DocumentTypeCode (380 with Order, Tariff, Original), TransportServiceCode (RAIL/ROAD with RailContainer/OceanContainer), TransportMeansTypeCode (AIR with Pipeline), NoticeTypeCode (PIN with ContractNotice), CertificateTypeCode (Cottonclassing with BondedStore), DefaultLanguageCode `en` vs `EN` everywhere else.
- **UBL lists not bound by UBL's CVA**: ReceiptAdviceTypeCode has a UBL default list that phase 2 never checks; DefaultLanguageCode, NationalityCode, MimeCode, TransportHandlingUnitTypeCode can reuse UBL lists once the world CVA binds them.

**Legend**: ✓ = current value is a valid code of the proposed list; ✗ = wrong for the element or not a code; "(was `x`)" = current value replaced. Values: `value`×count. Context: parent elements (files using the element).

## UBL default list, bound by the UBL 2.5 CVA — 31 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **AllowanceChargeReasonCode** | AllowanceCharge (11 files) | `95`×11, `72`×3, `78`×2, `64`, `75` · listID now: none 10, `UN/EDIFACT EDED 5189` 8 | UBL default | AllowanceChargeReason-2.4 · `UN/EDIFACT EDED 5189` | 72 = Temporary special promotion ✓; 75 = Promotion discount ✓; 78 = Volume discount ✓; 95 = Small order processing service charge ✗ → 91 = Agreed discount (bundle), 78 (repeat order), 2 = Below specification goods (moisture); 64 = Expecting new terms ✗ → 35 = Goods returned (restocking) | listID on 8 of 18. The .md files cite real UNCL 5189 meanings (95 discount, 64 special agreement), but UBL's list carries UNCL 4465 content under a 5189 label (UBL 2.0 called it "UN/ECE 4465"); in that list 95 and 64 mean something else. 72, 75 and 78 are not 5189 codes at all. Values pass phase 2 but are wrong in meaning (Q3). |
| **ChannelCode** | OtherCommunication, Communication (74 files) | `AL`×73, `EM` · listID now: none 73, `UN/EDIFACT EDED 3155` 1 | UBL default | Channel-2.4 · `UN/EDIFACT EDED 3155` | AL = Cellular phone ✓; EM = Electronic mail ✓ | listID on 1 of 74. |
| **CardChipCode** | CardAccount (1 file) | `Chip` | UBL default | Chip-2.0 · (no listID) | Chip = Chip ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **IdentificationCode** | Country, OriginCountry (230 files) | `XB`×1540, `XU`×881, `XL`×351 | UBL default | CountryIdentificationCode-2.4-world · `ISO 3166` | XU = Urvania ✓; XB = Bayvarra ✓; XL = Lisavu ✓ | 2,772 uses, none with listID. |
| **CurrencyCode** | TaxScheme, PayeeFinancialAccount, PayerFinancialAccount … (227 files) | `XBL`×348, `XUF`×198, `XLC`×10 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **DocumentCurrencyCode** | Invoice, Order, RemittanceAdvice … (91 files) | `XBL`×54, `XUF`×26, `XLC`×11 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **PaymentAlternativeCurrencyCode** | SelfBilledInvoice, SelfBilledCreditNote, Invoice … (6 files) | `XBL`×3, `XLC`×3 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **PaymentCurrencyCode** | Invoice, SelfBilledInvoice, SelfBilledCreditNote … (17 files) | `XUF`×9, `XBL`×5, `XLC`×3 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **PricingCurrencyCode** | RequestForQuotation, Quotation, SelfBilledInvoice … (13 files) | `XBL`×6, `XUF`×6, `XLC` | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **RequestedInvoiceCurrencyCode** | Order, OrderChange (2 files) | `XLC`, `XBL` | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **SourceCurrencyCode** | PricingExchangeRate, ExchangeRate, PaymentExchangeRate (28 files) | `XBL`×34, `XLC`×11, `XUF`×11 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **TargetCurrencyCode** | PricingExchangeRate, ExchangeRate, PaymentExchangeRate (28 files) | `XLC`×25, `XBL`×16, `XUF`×15 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **TaxCurrencyCode** | SelfBilledInvoice, SelfBilledCreditNote, DebitNote … (9 files) | `XUF`×6, `XLC`×3 | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **ValueCurrencyCode** | TenderingCriterionProperty (1 file) | `XBL` | UBL default | CurrencyCode-2.4-world · `ISO 4217 Alpha` | XUF = Ferra ✓; XBL = Lume ✓; XLC = Coral ✓ | No listID used anywhere. |
| **DocumentStatusCode** | DespatchAdvice, TransportExecutionPlanRequest, ForwardingInstructions … (33 files) | `NoStatus`×26, `Confirmed`×6, `Revised` | UBL default | DocumentStatus-2.1 · (no listID) | NoStatus ✓; Confirmed ✓; Revised ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **LocaleCode** | Language (195 files) | `EN`×317 | UBL default | Language-2.4 · `ISO 639` | EN = English ✓ (UBL list is upper case); add QAU = Urvanian, QAL = Lisavan in a world copy if they are ever used | UBL's list does not contain the local-use codes qau/qal: a LanguageCode-world copy is needed if they are used. 317 uses, no listID. |
| **NoticeLanguageCode** | PriorInformationNotice, ContractNotice, BusinessInformation … (4 files) | `EN`×4 | UBL default | Language-2.4 · `ISO 639` | EN = English ✓ (UBL list is upper case); add QAU = Urvanian, QAL = Lisavan in a world copy if they are ever used | UBL's list does not contain the local-use codes qau/qal: a LanguageCode-world copy is needed if they are used. |
| **PreferredLanguageLocaleCode** | ExpressionOfInterestRequest (1 file) | `EN` | UBL default | Language-2.4 · `ISO 639` | EN = English ✓ (UBL list is upper case); add QAU = Urvanian, QAL = Lisavan in a world copy if they are ever used | UBL's list does not contain the local-use codes qau/qal: a LanguageCode-world copy is needed if they are used. |
| **TenderLanguageLocaleCode** | ExpressionOfInterestResponse (1 file) | `EN` | UBL default | Language-2.4 · `ISO 639` | EN = English ✓ (UBL list is upper case); add QAU = Urvanian, QAL = Lisavan in a world copy if they are ever used | UBL's list does not contain the local-use codes qau/qal: a LanguageCode-world copy is needed if they are used. |
| **LatitudeDirectionCode** | LocationCoordinate (22 files) | `South`×29 | UBL default | LatitudeDirection-2.0 · (no listID) | South ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **LineStatusCode** | DespatchLine, LineItem, OrderLineReference … (15 files) | `NoStatus`×20, `Revised`×3 | UBL default | LineStatus-2.0 · (no listID) | NoStatus ✓; Revised ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **LongitudeDirectionCode** | LocationCoordinate (22 files) | `West`×29 | UBL default | LongitudeDirection-2.0 · (no listID) | West ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **MathematicOperatorCode** | PricingExchangeRate, PaymentExchangeRate, ExchangeRate … (18 files) | `Multiply`×44 | UBL default | Operator-2.0 · (no listID) | Multiply ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **PackagingTypeCode** | Package, ActualPackage, ContainedPackage … (9 files) | `PX`×28, `SW`×24, `BX`×3, `CR`×2, `BG`, `JB` | UBL default | PackagingType-2.4 · `UNECE Recommendation 21 - Codes for Passengers, Types of Cargo, Packages and Packaging Materials (with Complementary Codes for Package Names)` | PX = Pallet ✓; SW = Shrinkwrapped ✓; BX = Box ✓; JB = Bag, jumbo ✓; BG = Bag ✓; CR = Crate ✓ | No listID used. The UBL genericode listID contains a line break and 6 spaces ("Cargo,⏎      Packages"); validate_examples.py compares it literally, so no instance listID can match it (Q2). |
| **PaymentMeansCode** | PaymentMeans (61 files) | `30`×58, `97`, `10`, `54`, `55`, `49` · listID now: `UN/EDIFACT EDED 4461` 63 | UBL default | PaymentMeans-2.4 · `UN/EDIFACT EDED 4461` | 30 Credit transfer; 54 Credit card; 10 In cash; 49 Direct debit; 97 Clearing between partners; 55 Debit card — all ✓ | The only element with listID on every use (63/63). |
| **SubstitutionStatusCode** | OrderLine (1 file) | `Substitution` | UBL default | SubstitutionStatus-2.0 · (no listID) | Substitution ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **TransportEquipmentTypeCode** | TransportEquipment, ContainedInTransportEquipment, AttachedTransportEquipment (6 files) | `CN`×6, `AM`×2, `RR`, `TE` · listID now: `UN/EDIFACT EDED 8053` 10 | UBL default | TransportEquipmentType-2.4 · `UN/EDIFACT EDED 8053` | CN Container; RR Rail car; TE Trailer; AM Refrigerated container — all ✓ | listID on every use. |
| **TransportModeCode** | MainCarriageShipmentStage, ShipmentStage, PreCarriageShipmentStage … (13 files) | `2`×3, `3`×3, `1`×3, `4`×2, `7`×2, `8`×2 · listID now: `UNECE Recommendation 19 - Codes for Modes of Transport` 15 | UBL default | TransportMode-2.4 · `UNECE Recommendation 19 - Codes for Modes of Transport` | 1 Maritime; 2 Rail; 3 Road; 4 Air; 7 Fixed transport installations; 8 Inland water — all ✓ | listID on every use. |
| **ValueUnitCode** | TenderingCriterionProperty (1 file) | `ANN` | UBL default | UnitOfMeasure-2.4 · `UNECE Recommendation N°. 20 - Codes for Units of Measure Used in International Trade` | ANN = year ✓ | listID contains the non-ASCII "N°."; must be copied exactly. |
| **WeekDayCode** | ScheduledServiceFrequency (1 file) | `5` | UBL default | WeekDay-2.1 · (no listID) | 5 = Friday ✓ | UBL list has no listID: a listID can only be added with a world copy of the list that carries one (see Q2). |
| **WeighingMethodCode** | VerifiedGrossMass (1 file) | `SM2` · listID now: `IMO SOLAS` 1 | UBL default | WeighingMethod-2.2 · `IMO SOLAS` | SM2 = SOLAS verification method 2 ✓ | listID on its one use. |

## UBL default list exists, but the UBL CVA does not bind the element (world CVA must) — 6 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **MimeCode** | ExternalReference (6 files) | `application/pdf`×4, `image/jpeg`×2 | UBL default (reuse) | BinaryObjectMime-2.4 · `IANA Media Types` | application/pdf ✓; image/jpeg ✓ | Same list UBL uses for @mimeCode; not bound for cbc:MimeCode. |
| **NationalityCode** | Person (1 file) | `XU` | UBL default (reuse) | CountryIdentificationCode-2.4-world · `ISO 3166` | XU = Urvania ✓ | Not bound by the UBL CVA. |
| **DefaultLanguageCode** | Invoice, CreditNote, SelfBilledInvoice … (41 files) | `en`×41 | UBL default (reuse) | Language-2.4 (+ world QAU/QAL) · `ISO 639` | EN = English (was `en`) | Written lower case `en` (41 uses) while every other language code is `EN`; UBL's ISO 639 list is upper case, so `en` would fail once bound. |
| **TransportHandlingUnitTypeCode** | TransportHandlingUnit, PackagedTransportHandlingUnit (4 files) | `PX`×56, `SI` | UBL default (reuse) | PackagingType-2.4 · (UNECE Rec 21 listID, see PackagingTypeCode) | PX = Pallet ✓; SI = Skid ✓ | .md cites Rec 21 correctly, but no listID and no CVA binding. |
| **ReceiptAdviceTypeCode** | ReceiptAdvice (4 files) | `Actual`×4 | UBL default (reuse) | ReceiptAdviceType-2.1 · (no listID) | Actual ✓ (list: Actual, Preliminary, Return) | UBL ships a default list for it, but the UBL 2.5 CVA has no context for it, so phase 2 never checks it; the sweep therefore counted it as free. |
| **TimeBasisCode** | PenaltyInterestRate (16 files) | `Year`×16 | UBL default (reuse) | UnitOfMeasure-2.4 · (UNECE Rec 20 listID) | ANN = year (was `Year`) | Free word `Year`; Rec 20 (already used for ValueUnitCode ANN) has the unit. Alternative: regional TimeBasis list (Q8). |

## External standard — 32 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **TunnelRestrictionCode** | HazardousItem (4 files) | `E`×4, `D/E`×4 | External | ADR tunnel restriction codes (ADR 1.1.3.6, 8.6) · `UNECE ADR tunnel restriction code` | E ✓; D/E ✓ (slash is ADR's own notation) | No listID. |
| **CoordinateSystemCode** | LocationCoordinate (22 files) | `WGS84`×29 | External | EPSG Geodetic Parameter Dataset · `EPSG` | 4326 = WGS 84 (was `WGS84`) | `WGS84` is a name, not an EPSG code (29 uses). Alternative: keep WGS84 in a small regional list (Q14). |
| **NatureCode** | CommodityClassification (16 files) | `XX`×7, `XI`×3, `XV`×3, `V`×2, `VII`×2, `IX`×2 | External | HS 2022 Sections · `WCO HS 2022 Sections` | V Mineral products; VII Plastics and rubber; IX Wood; XI Textiles; XV Base metals; XX Miscellaneous manufactured articles — all ✓ for their HS codes | No listID. |
| **CharacterSetCode** | ExternalReference (1 file) | `UTF-8` | External | IANA Character Sets · `IANA Character Sets` | UTF-8 ✓ (hyphen is the registry's) | No listID. |
| **EmergencyProceduresCode** | HazardousItem, SecondaryHazard (4 files) | `F-A, S-I`×4, `None`×4, `F-E, S-C`×4, `F-E`×4 | External | IMDG Code EmS Guide · `IMO IMDG EmS` | `F-A, S-I` ✓ (UN 3480); `F-E, S-C` ✓ (UN 2920); `None` ✗ → F-I, S-S for UN 2911 (verify); `F-E` on SecondaryHazard ✗ | Space and comma inside the code (EmS pairs, Q12). `None` is not a code. EmS belong to the UN entry, not to a subsidiary hazard: drop it on SecondaryHazard. |
| **INFShipClassCode** | MaritimeTransport (1 file) | `INF1` | External | IMO INF Code ship classes · `IMO INF Code` | INF1 = INF.1 ship ✓ (the Code writes INF.1; dot dropped) | No listID. |
| **IndustryClassificationCode** | Party, CarrierParty, ConsigneeParty (230 files) | `4649`×111, `3100`×100, `8411`×66, `4719`×40, `5229`×26, `5210`×17 … (+28 more) · listID now: `ISIC Rev.4` 582 | External | ISIC Rev.4 · `ISIC Rev.4` (keep) | 33 of 34 values are valid ISIC Rev.4 classes; 3513 ✗ → 3510 = Electric power generation, transmission and distribution | 3513 (Ferrano Grid, 2 uses) is NACE Rev.2 35.13, not ISIC: ISIC Rev.4 group 351 has only class 3510. listID used consistently (582/582). |
| **ChargeBearerCode** | PaymentMeans (15 files) | `SHAR`×15 | External | ISO 20022 ChargeBearerType1Code · `ISO 20022 ChargeBearerType1Code` | SHAR = Shared ✓ | No listID. |
| **AccountTypeCode** | PayeeFinancialAccount, PayerFinancialAccount, FinancialAccount (69 files) | `Current`×89 | External | ISO 20022 ExternalCashAccountType1Code · `ISO 20022 ExternalCashAccountType1Code` | CACC = Current account (was `Current`) | Free word, 89 uses. |
| **PaymentPurposeCode** | RemittanceAdviceLine, InvoiceLine, ReminderLine … (19 files) | `SUPP`×10, `WTER`×5, `ELEC`×3, `GDDS`×2, `PHON`×2, `TRPT`, `GOVT` | External | ISO 20022 ExternalPurpose1Code · `ISO 20022 ExternalPurpose1Code` | SUPP Supplier payment ✓; GDDS Purchase/sale of goods ✓; ELEC Electricity bill ✓; WTER Water bill ✓; PHON Telephone bill ✓; GOVT Government payment (doubtful); TRPT Transport road pricing (doubtful); energy/02 line 3 → GASB Gas bill | energy/02-Invoice line 3 is gas network use but carries ELEC. TRPT means road pricing/tolls in ISO 20022, used for a return-transport cost (furniture/14). GOVT used for a recharged customs inspection fee, which is not a payment to government. No listID. |
| **ServiceLevelCode** | PaymentMeans (1 file) | `NURG` | External | ISO 20022 ExternalServiceLevel1Code · `ISO 20022 ExternalServiceLevel1Code` | NURG = Non-urgent payment ✓ | No listID. |
| **SizeTypeCode** | TransportEquipment, SupportedTransportEquipment, UnsupportedTransportEquipment (5 files) | `45G1`×4, `42G1`×4, `22G1`, `45R1` | External | ISO 6346 · `ISO 6346` | 45G1, 42G1, 22G1, 45R1 ✓ (valid size-type codes) | No listID; .md of 22G1/45R1 does not say what they are. |
| **GenderCode** | CrewPerson, PassengerPerson (1 file) | `0`×3 | External | ISO/IEC 5218 · `ISO 5218` | 0 = Not known ✓ (list: 0, 1, 2, 9) | No listID. |
| **CurrentOperatingSecurityLevelCode** | ISPSRequirements (1 file) | `1` | External | ISPS Code security levels · `IMO ISPS security level` | 1 ✓ | Shares the list with SecurityLevelCode. |
| **SecurityLevelCode** | PortCallRecord (1 file) | `1` | External | ISPS Code security levels · `IMO ISPS security level` | 1 = Security level 1 (normal) ✓ | Shares the list with CurrentOperatingSecurityLevelCode. |
| **NavigationStatusCode** | VesselDynamics (1 file) | `0` | External | ITU-R M.1371 AIS navigational status · `ITU-R M.1371 Navigational status` | 0 = Under way using engine ✓ | No listID. |
| **HazardousCategoryCode** | HazardousItem (4 files) | `UN`×12 | External | UN Model Regulations classes · `UN Model Regulations hazard class` | 9 Miscellaneous; 8 Corrosive; 7 Radioactive (was `UN` for all three) | Misuse: `UN` names the regulation, not a hazard category; the class is already in PlacardNotation (9, 8, 7). |
| **UNPackingGroupCode** | HazardousItem (4 files) | `II`×4 | External | UN Model Regulations packing groups · `UN Model Regulations packing group` | II = Medium danger ✓ (I, II, III) | No listID. Same concept as PackagingDangerLevelCode (Q11). |
| **UNDGCode** | HazardousItem, LoadedHazardousItem (5 files) | `3480`×6, `2911`×4, `2920`×4 · listID now: `UNCL8273` 14 | External | UN numbers (UN Model Regulations) · `UN/EDIFACT EDED 7124` | 3480 Lithium ion batteries ✓; 2911 Radioactive material, excepted package – instruments or articles ✓; 2920 Corrosive liquid, flammable, n.o.s. ✓ | Wrong listID `UNCL8273` on all 14 uses: UNCL 8273 is the *dangerous goods regulations* code (ADR, RID, IMD, ICA …); the UN number is data element 7124. |
| **CreditNoteTypeCode** | CreditNote, SelfBilledCreditNote (6 files) | `381`×5, `261` | External | UNCL 1001 · `UN/EDIFACT EDED 1001` | 381 = Credit note ✓; 261 = Self billed credit note ✓ | No listID. |
| **DebitNoteTypeCode** | DebitNote (2 files) | `383`×2 | External | UNCL 1001 · `UN/EDIFACT EDED 1001` | 383 = Debit note ✓ | No listID. |
| **DespatchAdviceTypeCode** | DespatchAdvice (11 files) | `Delivery`×11 | External | UNCL 1001 · `UN/EDIFACT EDED 1001` | 351 = Despatch advice (was `Delivery`) | Free word; UNCL 1001 is what the other *TypeCode of documents use. Alternative: regional list if a finer distinction is wanted (Q9). |
| **InvoiceTypeCode** | Invoice, SelfBilledInvoice (34 files) | `380`×33, `389` | External | UNCL 1001 · `UN/EDIFACT EDED 1001` | 380 = Commercial invoice ✓; 389 = Self-billed invoice ✓ | No listID. |
| **OrderTypeCode** | Order, OrderReference (18 files) | `220`×17, `230` | External | UNCL 1001 · `UN/EDIFACT EDED 1001` | 220 = Order ✓; 230 = Purchase order change request ✓ (FulfilmentCancellation/OrderReference to an OrderChange) | No listID. |
| **ActionCode** | TransactionConditions, CatalogueLine, Catalogue (17 files) | `Trade`×17, `Add`×3, `Accepted` | External | UNCL 1229 · `UN/EDIFACT EDED 1229` | 1 = Added (was Add, Catalogue/CatalogueLine); 5 = Accepted without amendment (was Accepted, Order/TransactionConditions); Trade ✗ | Three meanings in one element. `Trade` (Item/TransactionConditions, 17×) says *to whom* the conditions apply — misuse: drop the code, the Description already says "Sold to trade customers only". |
| **OrderResponseCode** | OrderResponse (5 files) | `AP`×4, `CA` | External | UNCL 4343 · `UN/EDIFACT EDED 4343` | AP = Accepted ✓; CA = Conditionally accepted ✓ | No listID (ResponseCode uses `UNCL4343` once: inconsistent spelling). |
| **PackageLevelCode** | Package (1 file) | `1`×25 | External | UNCL 7075 · `UN/EDIFACT EDED 7075` | 1 = Inner ✓ (2 Intermediate, 3 Outer) | No listID. |
| **ShipmentStageTypeCode** | PreCarriageShipmentStage (1 file) | `PreCarriage` | External | UNCL 8051 · `UN/EDIFACT EDED 8051` | 10 = Pre-carriage transport (was `PreCarriage`) | Free word; UBL's own 8051 qualifier fits exactly (20 main, 30 on-carriage). |
| **PackagingDangerLevelCode** | LoadedHazardousItem (2 files) | `None`×2 | External | UNCL 8339 · `UN/EDIFACT EDED 8339` | 1 Great danger; 2 Medium danger; 3 Minor danger; `None` ✗ | `None` is not a code: lithium batteries have no packing group, so the element should be omitted. Same concept as UNPackingGroupCode with another notation (Q11). |
| **TransportMeansTypeCode** | TransportMeans, MainCarriageShipmentStage (13 files) | `TE`×4, `SEA`×3, `AIR`×2, `Pipeline`×2, `INLAND`×2, `RAIL`×2 | External | UNECE Rec 28 · `UNECE Recommendation 28 - Codes for Types of Means of Transport` | Rec 28 four-digit codes for: aircraft (was AIR), sea-going container ship (SEA), inland barge (INLAND), container train (RAIL), truck with trailer (TE), pipeline (Pipeline) — look up exact codes | Mixed styles (AIR/SEA upper, Pipeline mixed case); `TE` is a UNCL 8053 *equipment* code (trailer), not a means type; values duplicate TransportModeCode. Not checked against Rec 28 here. |
| **TariffCode** | Consignment (1 file) | `9401.79` | External | WCO Harmonized System 2022 · `WCO HS 2022` | 9401.79 ✓ (HS subheading) | The .md says "the tariff of the carrier", but the value is an HS subheading: reason and value disagree (Q10). |
| **ItemClassificationCode** | CommodityClassification, MainCommodityClassification (107 files) | `9401.79`×48, `7325.99`×22, `9401.69`×12, `5201.00`×10, `4407.99`×9, `6205.20`×5 … (+10 more) · listID now: `HS` 139 | External | WCO Harmonized System 2022 · `WCO HS 2022` (was `HS`) | 15 of 16 subheadings valid (7325.99, 9401.79, 5201.00, 2711.21, 9401.69, 9403.30, 8507.60, 8531.10, 3814.00, 2601.11, 3920.10, 3923.21, 6205.20, 3901.10, 4407.99); 9988.00 ✗ | 9988.00 (tender lot 2, installation service) is not an HS subheading — HS does not classify services. Use a separate procurement/service classification (R:ProcurementCategory or UN CPC Ver.2.1, Q10). listID "HS" does not name the edition. |

## External standard, doubtful (fallback: regional) — 10 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **TransportAuthorizationCode** | HazardousGoodsTransit (2 files) | `CAO`×6 | External (doubtful) | IATA DGR · or R:TransportAuthorization | CAO = Cargo aircraft only ✓ | IATA DGR is not published as a code list; fallback regional. |
| **PackingCriteriaCode** | HazardousGoodsTransit (2 files) | `PI965-IA`×6 | External (doubtful) | IATA DGR packing instructions · or R:PackingInstruction | PI965IA = IATA packing instruction 965, section IA (was `PI965-IA`) | Hyphen; IATA instructions are not a published code list; fallback regional. |
| **MedicalFirstAidGuideCode** | HazardousItem (4 files) | `147`×4, `161`×4, `132`×4 | External (doubtful) | IMO MFAG table numbers · `IMO MFAG` — or ERG · `ERG 2024` | 147, 161, 132 are Emergency Response Guidebook guide numbers (correct ERG guides for UN 3480, 2911, 2920) | Element means IMO's Medical First Aid Guide; values come from the North American ERG (the .md says "emergency response guide"). Choose the list (Q13). |
| **InhalationToxicityZoneCode** | HazardousGoodsTransit (2 files) | `None`×6 | External (doubtful) | Inhalation hazard zones A–D (US 49 CFR 173.116/173.133) · `49 CFR Hazard Zone` | A, B, C, D; `None` ✗ | `None` is not a code: no toxicity, so omit the element. Doubtful list for a non-US world; fallback regional with the same A–D. |
| **MandateTypeCode** | PaymentMandate (1 file) | `Recurrent` | External (doubtful) | ISO 20022 SequenceType3Code · `ISO 20022 SequenceType3Code` | RCUR = Recurring (was `Recurrent`) | Doubtful fit: ISO 20022 has no mandate-type list as such; SequenceType (OOFF/RCUR) carries the one-off/recurrent distinction. Fallback: regional MandateType. |
| **EncodingCode** | ExternalReference (1 file) | `Binary` | External (doubtful) | RFC 2045 Content-Transfer-Encoding · `RFC 2045 Content-Transfer-Encoding` | binary (was `Binary`) | Doubtful as an "external list" (a short RFC enumeration, lower case). Fallback: regional Encoding (BINARY, BASE64). |
| **WaybillTypeCode** | Waybill (7 files) | `CMR`×3, `AWB`×2, `CIM`, `CMNI` | External (doubtful) | UNCL 1001 · `UN/EDIFACT EDED 1001` | 740 = Air waybill (was AWB); 720 = Rail consignment note (was CIM); 730 = Road consignment note (was CMR); CMNI → 711 = Inland waterway bill of lading (verify; doubtful) | Current values name the transport convention (the .md says so), not the document type. If the convention is what matters, use a regional TransportConvention list instead (Q9). |
| **ReferenceEventCode** | PaymentTerms (1 file) | `OrderAccepted`, `Shipment` | External (doubtful) | UNCL 2475 Payment time reference · `UN/EDIFACT EDED 2475` | codes for "date of order acceptance" and "date of shipment" (look up) — was OrderAccepted, Shipment | 2475 is the PAT-segment list for this concept; codes not verified here. Fallback: R:PaymentTermsEvent ORDERACC, SHIPMENT. |
| **CargoTypeCode** | CommodityClassification, SupportedCommodityClassification, UnsupportedCommodityClassification (17 files) | `GEN`×18, `BULK`×3 | External (doubtful) | UNCL 7085 Cargo type classification · `UN/EDIFACT EDED 7085` | General cargo / Bulk codes of 7085 (look up numbers) — was GEN, BULK | Doubtful which UN list (7085 or Rec 21 part 1 "types of cargo"); codes must be looked up. Fallback: R:CargoType GEN = General cargo, BULK = Bulk. |
| **HazardousRegulationCode** | HazardousGoodsTransit (2 files) | `IATA`×6 | External (doubtful) | UNCL 8273 · `UN/EDIFACT EDED 8273` | ICA = IATA/ICAO (was `IATA`; verify code) | Free word. 8273 is exactly this element's list (and the one wrongly cited on UNDGCode). |

## Several lists by context (one element, different meanings) — 18 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **RoleCode** | EndorserParty, EconomicOperatorRole, CrewMemberPerson (13 files) | `Chamber`×6, `Lead`×6, `Master`×4, `ChiefOfficer`×4, `ChiefEngineer`×3, `Insurer`×2 … (+7 more) | Split | *EndorserParty → R:EndorserRole · CardAccount → R:CardAccountRole · Crew/Passenger/Master… persons → R:ShipPersonRole · EconomicOperatorRole → R:EconomicOperatorRole | ISSUER, GUARANTOR, CHAMBER, INSURER, LEGALISATION · HOLDER · MASTER, CHIEFOFFICER, CHIEFENG, SSO = Ship security officer, MEDICAL, PASSENGER · LEAD, SUBCONTRACTOR | Four role vocabularies in one element. R:EconomicOperatorRole is shared with TendererRoleCode. |
| **WasteTypeCode** | WasteGenerated, MaritimeWaste (39 files) | `Packaging`×38, `Oil`, `Garbage` | Split | CircularityProfile/WasteGenerated → R:WasteType · ShipmentStage/MaritimeWaste → R:ShipWasteType (MARPOL annexes) | PACKAGING · OIL = MARPOL Annex I; GARBAGE = MARPOL Annex V | Two vocabularies; for ship waste the IMO port-reception waste categories are the real model. |
| **TypeCode** | ImportCustomsDeclaration, OpenTenderEvent, TenderingCriterionProperty … (13 files) | `Import`×6, `Opening`×3, `Question`×3, `Phytosanitary`, `Pest`, `Ginning` … (+5 more) | Split | Customs declarations → R:CustomsDeclarationType · GoodsCertificate → R:GoodsCertificateType · AttestationLine → R:AttestationType · GoodsProcessing (+Sub, CriterionItem) → R:GoodsProcessingType · RequestedArrivalEvent → R:PortCallEventType · OpenTenderEvent → R:TenderEventType · TenderingCriterionProperty → R:CriterionPropertyType | IMPORT, TRANSIT, EXPORT · PHYTO = Phytosanitary certificate · PEST = Pest check · GINNING, PRESSING, PROCESSING · ARRIVAL · OPENING · QUESTION, REQUIREMENT | Generic element with seven unrelated meanings: the world CVA must bind by parent path. CriterionPropertyType mirrors ESPD-EDM criterion-element-type (Q25). |
| **FunctionCode** | CustomsDeclaration, PreviousCustomsDeclaration (7 files) | `Original`×6, `Export`, `Import` | Split | CustomsDeclaration → UNCL 1225 `UN/EDIFACT EDED 1225` · PreviousCustomsDeclaration → R:CustomsDeclarationType | 9 = Original (was Original) · EXPORT, IMPORT | On PreviousCustomsDeclaration the value is the *type* of the earlier declaration, not its function: misuse unless the list is defined as such. |
| **DocumentTypeCode** | DocumentDistribution, DocumentReference, AdditionalDocumentReference … (30 files) | `Copy`×11, `Original`×9, `380`×9, `Tariff`×5, `Order`×2, `Invoice`×2 … (+3 more) | Split | DocumentReference & DigitalDocumentMetadata → UNCL 1001 `UN/EDIFACT EDED 1001` · DocumentDistribution → R:DocumentCopyType | 1001: 380 ✓ (5 refs); 220 = Order (was Order); 380 = Invoice (was Invoice); 481 = Remittance advice (was RemittanceAdvice); Tariff, Terms, ReturnNotice → no clear 1001 code (Q29) · Copy type: ORIGINAL; COPY | Three styles in one element: UNCL 1001 numbers, UBL document names (Order, Invoice), words (Tariff, Terms, ReturnNotice), plus Original/Copy which is a copy status, not a document type. |
| **ResponseCode** | Response, DiscrepancyResponse (10 files) | `AP`×5, `ReturnCost`×2, `Damaged`×2, `Grade`, `CN`, `Offered`, `Packaging`, `Met` · listID now: none 13, `UNCL4343` 1 | Split | DocumentResponse/LineResponse → UNCL 4343 `UN/EDIFACT EDED 4343` · DiscrepancyResponse → UNCL 4465 (the UBL AllowanceChargeReason list content) or R:DiscrepancyReason · TenderingCriterionResponse/ResponseValue → R:CriterionResponse · TransportServiceDescription → R:ServiceOfferResponse | 4343: AP = Accepted ✓ · Discrepancy (4465): 17 = Transport damage (was CN, Damaged), 2 = Below specification goods (was Grade, Packaging), 35 = Goods returned (was ReturnCost) · MET = Criterion met · OFFERED = Service offered | Four concepts mixed (sweep: AP/CN next to Grade/Met). listID `UNCL4343` once (should be `UN/EDIFACT EDED 4343`). `CN` on CreditNote/DiscrepancyResponse is a reason ("damaged in transit"), not a response type, and is not a 4343 code as far as I can tell. |
| **FullnessIndicationCode** | EmissionCalculationMethod, TransportEquipment (40 files) | `Cradle to gate`×38, `FCL`×5 | Split | EmissionCalculationMethod → R:EmissionBoundary · TransportEquipment → R:LoadType (or UNCL 8169, not verified) | CRADLEGATE = Cradle to gate (was `Cradle to gate`) · FCL = Full container load ✓; LCL | Spaces; two unrelated concepts. |
| **CalculationMethodCode** | EmissionCalculationMethod, PenaltyInterestRate (52 files) | `Calculated`×39, `Simple`×16 | Split | EmissionCalculationMethod → R:EmissionCalculationMethod · PenaltyInterestRate → R:InterestCalculation | CALCULATED; MEASURED · SIMPLE = Simple interest; COMPOUND | Two concepts in one element. |
| **SubTypeCode** | ImportCustomsDeclaration, TransitCustomsDeclaration, NoticeSubType (8 files) | `FreeCirculation`×6, `External`, `Extract` | Split | Import/TransitCustomsDeclaration → R:CustomsDeclarationSubType · NoticeSubType → R:NoticeSubType | FREECIRC = Release for free circulation; EXTTRANSIT = External transit · EXTRACT = Register extract |  |
| **CommodityCode** | CommodityClassification, AdditionalCommodityClassification (46 files) | `9401.79.10`×38, `7325.99.90`×22, `PARKS-FURN`×10 | Split | Item/CommodityClassification → XU:CustomsTariff · ProcurementProject → R:ProcurementCategory | XU tariff: 73259990 / 9401.79.10 kept as 7325.99.90, 9401.79.10 (national 8-digit extension of HS) · PARKSFURN = Park furniture (was PARKS-FURN) | Two concepts: national tariff numbers and the buyer's own category ("the department's own category"). The latter belongs in a procurement classification, not a commodity code (Q10). |
| **PurposeCode** | PartyAuthorization, ForecastRevision (15 files) | `R3`×14, `Order` | Split | PartyAuthorization → Basel Convention Annex IV `Basel Convention Annex IV` · ForecastRevision → R:ForecastPurpose | R3 = Recycling/reclamation of organic substances not used as solvents ✓ · ORDER | Two concepts. R3 is a real recovery-operation code. |
| **DescriptionCode** | PhysicalAttribute, InvoicePeriod (46 files) | `GRY`×38, `Month`×15 | Split | PhysicalAttribute → R:Colour · InvoicePeriod → R:PeriodDescription (or UNCL 2005 as EN 16931 does) | GRY = Grey ✓ · MONTH = Calendar month (was Month) | Two concepts. EN 16931 uses InvoicePeriod/DescriptionCode for the VAT point date code (UNCL 2005: 3, 35, 432); "Month" is not that (Q30). |
| **Code** | SecurityClearanceTerm, OperationType (5 files) | `None`×4, `Manufacture` | Split | SecurityClearanceTerm → R:SecurityClearance · OperationType → R:OperationType | `None` ✗ (omit; or NONE = No clearance required) · MANUFACTURE | The bare cbc:Code takes its meaning from the parent only. |
| **ProcedureCode** | ProofOfReexportationReminder, TenderingProcess, QualificationApplicationRequest … (9 files) | `Open`×8, `TemporaryAdmission` | Split | TenderingProcess & qualification documents → R:ProcurementProcedure · ProofOfReexportationReminder → R:CustomsProcedure | OPEN = Open procedure · 5300 = Temporary admission (was TemporaryAdmission) | Procurement and customs procedures in one element. |
| **ContractTypeCode** | ForeignExchangeContract, Contract, TransportContract (11 files) | `Forward`×6, `Framework`×5 | Split | TenderResult/Contract, TransportContract → R:ContractType · ForeignExchangeContract → R:FXContractType | FRAMEWORK = Framework contract · FORWARD = Currency forward | Two concepts. |
| **ConditionCode** | CurrentStatus, Status, SubStatus (8 files) | `Scheduled`×3, `OnTime`×2, `Ready`, `Damaged`, `InTransit`, `Released`, `Matched` | Split | Transport/package/consignment Status & event CurrentStatus → R:StatusCondition · ApplicationResponse Response/Status → R:ResponseStatusCondition | READY, DAMAGED, INTRANSIT, ONTIME, RELEASED, SCHEDULED · MATCHED = Three-way match passed | CamelCase words. For the response status, OpenPEPPOL's status-action / clarification lists are the real-world model (not adopted). |
| **SubscriberTypeCode** | UtilityConsumptionPoint, UtilityItem (6 files) | `IND`×2, `ELEC`×2, `COM`×2, `WATE`×2, `TELE`×2, `HH`, `BUS` | Split | UtilityConsumptionPoint → R:SubscriberType · UtilityItem → R:UtilityType | IND = Industrial; COM = Commercial; HH = Household; BUS = Business · ELEC, WATER (was WATE), TEL (was TELE) | Misuse in UtilityItem: ELEC/WATE/TELE are utility types, not subscriber types (they belong with UtilityStatementTypeCode). WATE/TELE are truncated words. |
| **StatusCode** | Waybill, PriceList, GoodsItemPassport … (13 files) | `Issued`×7, `Active`×7, `Valid`, `Replaced`, `Approved` | Split | Waybill, GoodsItemPassport, PriceList → R:RecordStatus · PurchaseReceipt/Payment → R:PaymentStatus | ISSUED; VALID; ACTIVE; REPLACED · APPROVED = Payment approved | Document validity and payment status mixed in one element. |

## National (XU / XB / XL) — 4 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **CountrySubentityCode** | PostalAddress (195 files) | `CO`×192, `UL`×136 | National | XB:CountrySubentity | UL = Upland State ✓; CO = Coastal State ✓ | Only Bayvarra has subdivisions. Real model ISO 3166-2 writes XB-UL / XB-CO (Q27). |
| **ExemptionReasonCode** | PartyTaxScheme (39 files) | `XB-PUBLIC`×39 | National | XB:TaxExemptionReason | XBPUBLIC = Sale to a public body (was XB-PUBLIC) | Same list as TaxExemptionReasonCode (party-level exemption). |
| **CompanyLegalFormCode** | PartyLegalEntity (227 files) | `Ltd`×276, `SUA`×96, `SRU`×62, `Corp`×54, `SP`×4, `Any`×4 | National | XU:CompanyLegalForm · XB:CompanyLegalForm · XL:CompanyLegalForm | XU: SUA ✓, SRU ✓ · XB: CORP = Corporation (was Corp), LTD = Limited company (was Ltd) · XL: LTD = Island limited company (was Ltd), SP ✓ · `Any` ✗ | `Ltd` means different forms in XB and XL: only the listID tells them apart, so listID is required. `Any` (TendererQualificationRequest, 4×) is not a legal form: omit (CompanyLegalForm text already says it). Real-world model: ISO 20275 ELF codes. |
| **TaxExemptionReasonCode** | TaxCategory, ClassifiedTaxCategory, ApplicableTaxCategory (55 files) | `XB-EXP`×28, `XB-RESALE`×24, `XU-EXP`×18, `XB-PUBLIC`×15, `XB-SVC-B2B`×12, `XB-WATER`×8, `XU-SVC-ABROAD`×7, `XB-LEVY`×6 | National | XU:TaxExemptionReason · XB:TaxExemptionReason | XU: XUEXP (was XU-EXP), XUSVCABROAD (was XU-SVC-ABROAD) · XB: XBEXP, XBWATER, XBPUBLIC, XBSVCB2B, XBRESALE, XBLEVY (were with hyphens) | Hyphens; the country prefix becomes redundant once the listID names the country — or keep the prefixed codes in one regional list (Q28). Lisavu has no exemption list (no VAT/sales tax). |

## Regional (Trade Accord) — 197 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **AccountFormatCode** | PayeeFinancialAccount, PayerFinancialAccount, FinancialAccount (69 files) | `ISO13616`×89 | Regional | R:AccountFormat | IBAN = ISO 13616 IBAN structure (was `ISO13616`) | Names the standard rather than the format. Overlaps PaymentChannelCode=IBAN (see there). |
| **AddressFormatCode** | PostalAddress (230 files) | `XB`×327, `XU`×193, `XL`×98 | Regional | R:AddressFormat | XU = Urvanian format (StreetName BuildingNumber / PostalZone CityName); XB = Bayvarran format; XL = Lisavan format ✓ | Values are already short codes. Kept regional (one list, one row per country) rather than three national lists. Alternative: UNCL 3477 Address format (street-then-number etc.), doubtful (Q15). |
| **AddressTypeCode** | PostalAddress (230 files) | `Business`×600, `Postal`×10, `Residential`×8 | Regional | R:AddressType | BUSINESS = Business address; POSTAL = Postal address; RESIDENTIAL = Residential address | Words in mixed case (618 uses). |
| **AgreementTypeCode** | DigitalAgreement (1 file) | `Bilateral` | Regional | R:AgreementType | BILATERAL = Bilateral agreement |  |
| **MultipleTendersCode** | TenderingTerms (4 files) | `NotAllowed`×4 | Regional | R:AllowedIndicator | ALLOWED; NOTALLOWED | One list for MultipleTendersCode, VariantConstraintCode, SubcontractingConditionsCode. |
| **SubcontractingConditionsCode** | AllowedSubcontractTerms (4 files) | `Allowed`×4 | Regional | R:AllowedIndicator | ALLOWED | Shares R:AllowedIndicator. |
| **VariantConstraintCode** | TenderingTerms (4 files) | `Allowed`×4 | Regional | R:AllowedIndicator | ALLOWED | Shares R:AllowedIndicator. |
| **SubjectCode** | Annotation (1 file) | `Contract` | Regional | R:AnnotationSubject | CONTRACT = Contract |  |
| **ApplicationStatusCode** | CertificateOfOriginApplication (2 files) | `Submitted`, `Approved` | Regional | R:ApplicationStatus | SUBMITTED; APPROVED |  |
| **ActivityTypeCode** | ContractingActivity (3 files) | `Public works`×3 | Regional | R:AuthorityActivity | PUBWORKS = Public works (was `Public works`) | Space in code. |
| **AvailabilityStatusCode** | InventoryReportLine (1 file) | `Available` | Regional | R:AvailabilityStatus | AVAILABLE = Available |  |
| **AwardingCriterionTypeCode** | AwardingCriterion (4 files) | `Price`×4, `Quality`×4 | Regional | R:AwardCriterionType | PRICE = Price; QUALITY = Quality |  |
| **AwardingMethodTypeCode** | TenderingTerms (4 files) | `BestValue`×4 | Regional | R:AwardingMethod | BESTVALUE = Best price-quality ratio (was BestValue) |  |
| **ExchangeMethodCode** | ExchangeBallastWaterTransaction (1 file) | `Sequential` | Regional | R:BallastExchangeMethod | SEQ = Sequential (was Sequential); FLOW = Flow-through; DIL = Dilution | Methods of the BWM Convention guidelines (no code list). |
| **TankTypeCode** | UptakeBallastWaterTransaction (1 file) | `Wing` | Regional | R:BallastTankType | WING = Wing tank |  |
| **CapabilityTypeCode** | BusinessCapability (2 files) | `Warehousing`, `Production` | Regional | R:BusinessCapabilityType | PRODUCTION = Production; WAREHOUSING = Warehousing |  |
| **GroupTypeCode** | BusinessPartyGroup (1 file) | `SameActivity` | Regional | R:BusinessPartyGroupType | SAMEACTIVITY = Same registered activity (was SameActivity) |  |
| **CalculationExpressionCode** | AwardingCriterion (4 files) | `Inverse`×4 | Regional | R:CalculationExpression | INVERSE = Inverse proportion | .md: "As a code." |
| **PreviousCancellationReasonCode** | ProcessJustification (3 files) | `None`×3 | Regional | R:CancellationReason | `None` ✗ | Not a code: there was no cancelled procedure, so omit the element (3 uses). |
| **CardTypeCode** | CardAccount (1 file) | `Debit` | Regional | R:CardType | DEBIT = Debit card; CREDIT = Credit card | Possibly ISO 20022 card type codes (not verified). |
| **CertificateTypeCode** | Certificate, EnvironmentalCertificate (39 files) | `Permit`×29, `Cottonclassing`×7, `Sustainableforestry`×7, `Recycledcontent`×5, `BondedStore` | Regional | R:CertificateType | PERMIT = Operating permit; BONDEDSTORE = Bonded store licence; COTTONCLASS = Cotton classing; RECYCLED = Recycled content; SUSTFOREST = Sustainable forestry (was Permit, BondedStore, Cottonclassing, Recycledcontent, Sustainableforestry) | Odd casing (Cottonclassing, Recycledcontent) next to CamelCase BondedStore. |
| **ApplicableCategoryCode** | Certificate (7 files) | `HW`×7 | Regional | R:CertifiedProductCategory | HW = Hardwood ✓ |  |
| **CircularityTypeCode** | CircularityProfile (2 files) | `Recycled`×2 | Regional | R:CircularityType | RECYCLED = Recycled material |  |
| **CompanyLiquidationStatusCode** | PartyLegalEntity (230 files) | `Active`×582 | Regional | R:CompanyLiquidationStatus | ACTIVE = Active, not in liquidation (was Active) | 582 uses. |
| **ComparisonDataCode** | ForecastException (1 file) | `Actual` | Regional | R:ComparisonData | ACTUAL = Actual sales; FORECAST |  |
| **ExpressionCode** | FinancialEvaluationCriterion (4 files) | `GreaterThan`×4 | Regional | R:ComparisonOperator | GT = Greater than (was GreaterThan) | One list with ThresholdValueComparisonCode. |
| **ThresholdValueComparisonCode** | ExceptionCriteriaLine (1 file) | `LessThan`, `GreaterThan` | Regional | R:ComparisonOperator | LT = Less than; GT = Greater than | Shares R:ComparisonOperator. |
| **ConfidentialityLevelCode** | SuppliedEvidence, TenderingCriterionResponse, Evidence (2 files) | `Confidential`×2, `Public` | Regional | R:Confidentiality | PUBLIC; CONFIDENTIAL | Shares R:Confidentiality. |
| **PrivacyCode** | RequestForQuotationLine, TelecommunicationsSupply (3 files) | `Confidential`×2, `Masked` | Regional | R:Confidentiality | CONFIDENTIAL; MASKED = Numbers masked (telecom) | Shares R:Confidentiality with ConfidentialityLevelCode, SecurityClassificationCode; MASKED is telecom-specific (could be its own list). |
| **SecurityClassificationCode** | RequestForQuotationLine (2 files) | `Internal`×2 | Regional | R:Confidentiality | INTERNAL = Not for publication | Shares R:Confidentiality. |
| **CorrectionTypeCode** | EnergyWaterConsumptionCorrection (3 files) | `CONV`, `EST`, `COOL` | Regional | R:ConsumptionCorrectionType | CONV = Volume conversion ✓; EST = Estimate correction ✓; COOL = District heating cooling correction ✓ |  |
| **ConsumersEnergyLevelCode** | ConsumptionReport (1 file) | `Low` | Regional | R:ConsumptionLevel | LOW = Below average | Same list as ConsumptionLevelCode. |
| **ConsumptionLevelCode** | ConsumptionHistory (4 files) | `Normal`×8 | Regional | R:ConsumptionLevel | NORMAL = Within the usual range; LOW; HIGH | Same list as ConsumersEnergyLevelCode. |
| **ConsumptionTypeCode** | UtilityItem, ConsumptionReport, ConsumptionReportReference (5 files) | `MON`×8, `MET`×5, `SUB` | Regional | R:ConsumptionType | MON = Monthly consumption ✓; MET = Metered consumption; SUB = Subscription | Two meanings: report period (MON) vs charge basis (MET/SUB in UtilityItem); acceptable in one list, but check. |
| **PartyTypeCode** | ContractingPartyType (3 files) | `Local`×3 | Regional | R:ContractingPartyType | LOCAL = Local authority |  |
| **ContractingSystemCode** | TenderingProcess (3 files) | `Framework`×3 | Regional | R:ContractingSystem | FRAMEWORK = Framework agreement | Same list as ContractingSystemTypeCode. |
| **ContractingSystemTypeCode** | ContractingSystem (3 files) | `Framework`×3 | Regional | R:ContractingSystem | FRAMEWORK = Framework agreement | Same list as ContractingSystemCode. |
| **ModificationReasonCode** | TransportContract (1 file) | `Volume` | Regional | R:ContractModificationReason | VOLUME = Volume change |  |
| **CopyQualityTypeCode** | TenderingCriterionProperty (1 file) | `Copy` | Regional | R:CopyQuality | COPY = A copy is enough; ORIGINAL; CERTIFIED |  |
| **CorporateRegistrationTypeCode** | CorporateRegistrationScheme (230 files) | `Commercial`×582 | Regional | R:CorporateRegistrationType | COMMERCIAL = Commercial register (was Commercial) |  |
| **CriterionTypeCode** | TenderingCriterion (1 file) | `Economic` | Regional | R:CriterionType | ECONOMIC = Economic and financial standing |  |
| **CustomsProcedureCode** | GoodsItem (1 file) | `4000` | Regional | R:CustomsProcedure | 4000 = Release for free circulation, no previous procedure ✓; 5300 = Temporary admission | Modelled on the EU customs procedure codes (4000 is the EU CPC); in the world it is the Trade Accord's list (Q24). Shared with ProcedureCode=TemporaryAdmission. |
| **CustomsStatusCode** | GoodsItem (1 file) | `Foreign` | Regional | R:CustomsStatus | FOREIGN = Non-accord goods, not released; ACCORD = Released / accord goods | .md: "Bayvarra's customs status": national or accord-wide? (Q24). |
| **DeclarationTypeCode** | Declaration (1 file) | `Integrity` | Regional | R:DeclarationType | INTEGRITY = Integrity declaration |  |
| **DeliveryAcceptanceCode** | ReceiptAdvice (4 files) | `Partial`×2, `Accepted`×2 | Regional | R:DeliveryAcceptance | ACCEPTED = All accepted; PARTIAL = Partly refused; REFUSED |  |
| **DistributionTypeCode** | DocumentDistribution (20 files) | `Electronic`×17, `Paper`×10 | Regional | R:DistributionType | ELECTRONIC = Electronic; PAPER = Paper |  |
| **FormatCode** | ExternalReference (1 file) | `PDF/A-3` | Regional | R:DocumentFormat | PDFA3 = PDF/A-3 (ISO 19005-3) (was `PDF/A-3`) | Slash. No authoritative code list for file formats (PRONOM ids are an option, Q19). |
| **DocumentStatusReasonCode** | TransportExecutionPlan, TransportExecutionPlanRequest (4 files) | `AsRequested`×3, `Update` | Regional | R:DocumentStatusReason | UPDATE = Update of a standing plan; ASREQ = As requested (was AsRequested) |  |
| **TendererRoleCode** | QualifyingParty, MainQualifyingParty, AdditionalQualifyingParty (2 files) | `Lead`×2, `Subcontractor` | Regional | R:EconomicOperatorRole | LEAD = Consortium lead; SUBCONTRACTOR | Shares the list with RoleCode in EconomicOperatorRole. |
| **EnvironmentalEmissionTypeCode** | EnvironmentalEmission (43 files) | `CO2e`×40, `CO2`×3 | Regional | R:EmissionType | CO2E = Greenhouse gases as CO2 equivalent; CO2 = Carbon dioxide only | The 3 uses of `CO2` are explained as "greenhouse gases as CO2 equivalent": value/reason disagree, should be CO2E. |
| **ProcessingTypeCode** | EndOfLifeTreatment (2 files) | `Mechanical`×2 | Regional | R:EndOfLifeProcessing | MECHANICAL = Mechanical processing | Overlaps TreatmentPathwayCode. |
| **EnergySourceTypeCode** | EnergyConsumptionAllocation (2 files) | `Electricity`×2, `Diesel` | Regional | R:EnergySource | DIESEL = Diesel; ELECTRICITY = Electricity; MGO = Marine gas oil | One list with FuelTypeCode (Diesel occurs in both). |
| **FuelTypeCode** | FuelConsumption (2 files) | `Diesel`, `MGO` | Regional | R:EnergySource | DIESEL = Diesel; MGO = Marine gas oil ✓ | Shares R:EnergySource with EnergySourceTypeCode. MGO corresponds to ISO 8217 DMA, but ISO 8217 is a specification, not a code list. |
| **EntitySizeCode** | PartyLegalEntity (225 files) | `Small`×256, `Large`×154, `Medium`×78, `Micro`×4 | Regional | R:EntitySize | MICRO, SMALL, MEDIUM, LARGE (was Micro/Small/Medium/Large) | Size classes are the same in all three countries in parties.json; if thresholds differ per country, make it national (Q16). |
| **EnvelopeTypeCode** | DigitalMessageDelivery (1 file) | `SBDH`×4 | Regional | R:EnvelopeType | SBDH = UN/CEFACT Standard Business Document Header ✓ |  |
| **ImpactCode** | EndOfLifeTreatment (2 files) | `Low: the film becomes granulate again`×2 | Regional | R:EnvironmentalImpactLevel | LOW = Low impact (was `Low: the film becomes granulate again`) | A sentence in a code: keep LOW as the code and move "the film becomes granulate again" to a text element (e.g. EndOfLifeTreatment/Description). |
| **DispositionCode** | TransportEquipment (1 file) | `Loaded` | Regional | R:EquipmentDisposition | LOADED = Loaded; EMPTY = Empty |  |
| **OwnerTypeCode** | TransportEquipment (1 file) | `Carrier` | Regional | R:EquipmentPartyType | CARRIER = Carrier; SHIPPER = Shipper | Same list as ProviderTypeCode and SealIssuerTypeCode. |
| **ProviderTypeCode** | TransportEquipment (1 file) | `Carrier` | Regional | R:EquipmentPartyType | CARRIER = Carrier | Same list as OwnerTypeCode. |
| **SealIssuerTypeCode** | TransportEquipmentSeal (4 files) | `Shipper`×4, `Carrier`×2 | Regional | R:EquipmentPartyType | SHIPPER = Shipper; CARRIER = Carrier | Real equivalent: UNCL 9303 Sealing party (CA carrier, SH shipper, CU customs) — check whether to adopt it (Q22). |
| **EvaluationCriterionTypeCode** | TechnicalEvaluationCriterion, FinancialEvaluationCriterion (4 files) | `References`×4, `Turnover`×4 | Regional | R:EvaluationCriterionType | REFERENCES; TURNOVER |  |
| **EvaluationMethodTypeCode** | TenderingCriterion (1 file) | `PassFail` | Regional | R:EvaluationMethod | PASSFAIL = Pass/fail (was PassFail) |  |
| **EvidenceTypeCode** | SuppliedEvidence, Evidence (2 files) | `Audit`, `Accounts` | Regional | R:EvidenceType | AUDIT = Audit report; ACCOUNTS = Annual accounts |  |
| **ExceptionResolutionCode** | ExceptionCriteriaLine (1 file) | `Review` | Regional | R:ExceptionResolution | REVIEW = Joint review | One list with ResolutionCode. |
| **ResolutionCode** | ExceptionNotificationLine (1 file) | `Review` | Regional | R:ExceptionResolution | REVIEW | Shares R:ExceptionResolution. |
| **ExceptionStatusCode** | ExceptionCriteriaLine, ExceptionNotificationLine (2 files) | `Active`, `Open` | Regional | R:ExceptionStatus | ACTIVE = Criterion in force; OPEN = Not resolved | Two meanings (criteria line vs notification line). |
| **ExecutionRequirementCode** | ContractExecutionRequirement (4 files) | `Environmental`×4 | Regional | R:ExecutionRequirement | ENVIRONMENTAL | Same code as TendererRequirementTypeCode; could share R:RequirementType. |
| **TendererRequirementTypeCode** | SpecificTendererRequirement (4 files) | `Environmental`×4 | Regional | R:ExecutionRequirement | ENVIRONMENTAL | Shares the list with ExecutionRequirementCode. |
| **ExpectedCode** | TenderingCriterionProperty (1 file) | `Registered` | Regional | R:ExpectedResponse | REGISTERED = Registered |  |
| **ExpenseCode** | TenderingProcess (3 files) | `Investment`×3 | Regional | R:ExpenseType | INVESTMENT = Investment budget |  |
| **ExportReasonCode** | ExportCustomsDeclaration, GoodsItemPassport (7 files) | `Sale`×6, `Exhibition` | Regional | R:ExportReason | SALE = Sale; EXHIBITION = Exhibition or fair |  |
| **ExportTypeCode** | ExportCustomsDeclaration (6 files) | `Permanent`×6 | Regional | R:ExportType | PERMANENT = Permanent export; TEMPORARY = Temporary export |  |
| **FeeTypeCode** | AdditionalFee (3 files) | `Courier`×3 | Regional | R:FeeType | COURIER = Courier fee |  |
| **FinancingInstrumentCode** | TradeFinancing (1 file) | `Factoring` | Regional | R:FinancingInstrument | FACTORING = Factoring |  |
| **AdjustmentReasonCode** | ForecastRevisionLine (1 file) | `Demand` | Regional | R:ForecastAdjustmentReason | DEMAND = Demand change |  |
| **ForecastPurposeCode** | Forecast, ForecastExceptionCriterionLine, ForecastException … (5 files) | `Sales`×4, `Order` | Regional | R:ForecastPurpose | ORDER = Order forecast; SALES = Sales forecast | Shares the list with PurposeCode in ForecastRevision and RetailPlannedImpact. |
| **ForecastTypeCode** | ForecastLine, ItemInformationRequestLine, ForecastExceptionCriterionLine … (6 files) | `Total`×6 | Regional | R:ForecastType | TOTAL = Total; BASE; PROMOTIONAL |  |
| **FreightRateClassCode** | TransportationService (1 file) | `BOX` | Regional | R:FreightRateClass | BOX = Rate per container ✓ | Possibly UNCL 5243 rate/tariff class (not verified). |
| **TariffClassCode** | AdditionalTransportationService, TransportationService (2 files) | `B`, `FAK` | Regional | R:FreightRateClass | B = Basic class ✓; FAK = Freight all kinds ✓ | Same concept as FreightRateClassCode: one list. |
| **MaintenanceFrequencyCode** | CircularityProfile (38 files) | `Yearly`×38 | Regional | R:Frequency | YEARLY = Once a year | Shares R:Frequency with TimeFrequencyCode, PaymentFrequencyCode. |
| **PaymentFrequencyCode** | TenderingTerms (4 files) | `PerRelease`×4 | Regional | R:Frequency | PERRELEASE = After each release (was PerRelease) | Shares R:Frequency. |
| **TimeFrequencyCode** | ItemInformationRequestLine (1 file) | `Weekly` | Regional | R:Frequency | WEEKLY = Once a week | Shares R:Frequency. |
| **FulfilmentIndicatorTypeCode** | TenderingCriterion, TenderingCriterionPropertyGroup (1 file) | `All`×2 | Regional | R:FulfilmentIndicator | ALL = All properties |  |
| **ConstitutionCode** | GuaranteeCertificate (1 file) | `BankGuarantee` | Regional | R:GuaranteeConstitution | BANKGUAR = Bank guarantee (was BankGuarantee) |  |
| **GuaranteeTypeCode** | RequiredFinancialGuarantee, GuaranteeCertificate, FinalFinancialGuarantee (6 files) | `TenderGuarantee`×5, `PerformanceGuarantee` | Regional | R:GuaranteeType | TENDER = Tender guarantee; PERFORMANCE = Performance guarantee |  |
| **HandlingCode** | TransportHandlingUnit, Shipment, Consignment (2 files) | `Stack2`×24, `Upright`, `NoStack`, `Deck` | Regional | R:HandlingInstruction | STACK2 = Stack at most two high; NOSTACK = Do not stack; UPRIGHT = Keep upright; DECK = On-deck stowage allowed | DECK is a stowage permission, not handling; possibly UNCL 4079 handling codes (not verified). The .md of NoStack repeats the Stack2 reason. |
| **HazardousTypeCode** | LoadedHazardousItem (2 files) | `Article`×2 | Regional | R:HazardousGoodsType | ARTICLE = Article; SUBSTANCE = Substance |  |
| **HeatingTypeCode** | ConsumptionReport (1 file) | `DH` | Regional | R:HeatingType | DH = District heating ✓ |  |
| **InspectionMethodCode** | LineItem (2 files) | `Visual`×2 | Regional | R:InspectionMethod | VISUAL = Visual inspection |  |
| **InsuranceTypeCode** | InsurancePolicy (1 file) | `AllRisks` | Regional | R:InsuranceCover | ALLRISKS = All risks (was AllRisks) | Real model: Institute Cargo Clauses A/B/C (A = all risks). |
| **LifeCycleStatusCode** | CatalogueLine (1 file) | `Active`×2 | Regional | R:ItemLifeCycleStatus | ACTIVE = Active |  |
| **PositionCode** | PhysicalAttribute (38 files) | `FRM`×38 | Regional | R:ItemPartPosition | FRM = Frame ✓ |  |
| **NameCode** | AdditionalItemProperty, MeterProperty (49 files) | `LOAD`×38, `MC`×7, `ACC`×4 | Regional | R:ItemPropertyName | LOAD = Load capacity; MC = Moisture content; ACC = Accuracy class (meter) | One list for item and meter properties (MeterProperty uses the same element). .md: "as the property standard lists it" — no standard named. |
| **ItemTypeCode** | Item (1 file) | `Product`×2 | Regional | R:ItemType | PRODUCT = Product; SERVICE = Service |  |
| **LifecycleStageCode** | EnvironmentalEmission, Item (39 files) | `Manufacturing`×38, `End-of-life` | Regional | R:LifecycleStage | MANUFACTURING = Manufacturing; ENDOFLIFE = End of life (was `End-of-life`) | Hyphen. Possible external model: EN 15804 modules A1–A3 … C1–C4 (Q21). |
| **LocationTypeCode** | BondedWarehouseLocation (1 file) | `BondedStore` | Regional | R:LocationType | BONDEDSTORE = Customs bonded store |  |
| **PartPresentationCode** | TenderingProcess (3 files) | `OneOrMore`×3 | Regional | R:LotSubmission | ONEORMORE = One or more lots; ALL = All lots; ONE = One lot only |  |
| **ManifestTypeCode** | Manifest (1 file) | `Cargo` | Regional | R:ManifestType | CARGO = Cargo manifest |  |
| **MaritimePollutantCode** | HazardousItem (4 files) | `N`×4 | Regional | R:MarinePollutant | P = Marine pollutant; N = Not a marine pollutant ✓ | IMDG marks marine pollutants with "P"; no published code list. |
| **MarketCode** | SecurityListing (73 files) | `FSE`×73 | Regional | R:Market | FSE = (world stock exchange) ✓ | Real-world equivalent is ISO 10383 MIC (4 characters); a world exchange is not in it, so a regional list modelled on MIC (Q17). |
| **ResourceTypeCode** | ResourceConsumption (38 files) | `Steel`×38, `Hardwood`×38 | Regional | R:MaterialResource | STEEL = Steel; HARDWOOD = Hardwood |  |
| **MeterConstantCode** | UtilityMeter (5 files) | `Direct`×4, `Transformer ratio` | Regional | R:MeterConstantType | DIRECT = Direct connection; CTRATIO = Transformer ratio (was `Transformer ratio`) | Space in code. |
| **LatestMeterReadingMethodCode** | MeterReading (5 files) | `REMOTE`×3, `MANUAL`, `CUSTOMER` | Regional | R:MeterReadingMethod | REMOTE ✓; MANUAL ✓; CUSTOMER ✓; ESTIMATE ✓ | One list with PreviousMeterReadingMethodCode. Regional, unless the countries' metering rules differ (Q16). |
| **PreviousMeterReadingMethodCode** | MeterReading (4 files) | `REMOTE`×2, `ESTIMATE`, `CUSTOMER` | Regional | R:MeterReadingMethod | REMOTE ✓; ESTIMATE ✓; CUSTOMER ✓ | One list with LatestMeterReadingMethodCode. |
| **MeterReadingTypeCode** | MeterReading (4 files) | `M`×4 | Regional | R:MeterReadingType | M = Monthly reading ✓ |  |
| **NatureOfTransactionCode** | ImportCustomsDeclaration, TransitCustomsDeclaration (7 files) | `Purchase`×7 | Regional | R:NatureOfTransaction | PURCHASE = Outright purchase/sale | Real model: EU/UN statistics nature of transaction (1 = purchase), not adopted. |
| **NoticeTypeCode** | PriorInformationNotice, ContractNotice, BusinessInformation … (4 files) | `PIN`, `ContractNotice`, `BusinessRegistration`, `ContractAwardNotice` | Regional | R:NoticeType | PIN = Prior information notice ✓; CN = Contract notice (was ContractNotice); CAN = Contract award notice (was ContractAwardNotice); BUSREG = Business registration notice (was BusinessRegistration) | Mixed styles: one abbreviation, three long words. |
| **PackLevelCode** | TenderLine, CatalogueLine (4 files) | `Pallet`×4 | Regional | R:PackLevel | PALLET = Pallet | Possibly GS1 TradeItemUnitDescriptor (PALLET, CASE …) — not verified. |
| **PaymentChannelCode** | PaymentMeans (38 files) | `IBAN`×38 | Regional | R:PaymentChannel | IBAN ✗ → the world's payment systems (countries.json): FERRARTGS, LUMEPAY, CORALNET, TAPAY = Trade Accord payment link | Misuse: `IBAN` is an account format (already in AccountFormatCode); a channel is the payment system (Q18). |
| **PerformanceMetricTypeCode** | ItemInformationRequestLine, ExceptionCriteriaLine, ExceptionNotificationLine (3 files) | `SalesUnits`×3 | Regional | R:PerformanceMetric | SALESUNITS = Sales in units |  |
| **PurposeTypeCode** | PrimaryPortCallPurpose, AdditionalPortCallPurpose (1 file) | `Cargo`, `Water` | Regional | R:PortCallPurpose | CARGO = Cargo operations; WATER = Fresh water bunkering |  |
| **PreferenceCriterionCode** | GoodsItem (1 file) | `P` | Regional | R:PreferenceCriterion | P = Wholly obtained (Trade Accord rules of origin) ✓ | Explicitly a Trade Accord criterion. |
| **PriceEvaluationCode** | TenderingTerms (4 files) | `UnitPrice`×4 | Regional | R:PriceEvaluation | UNITPRICE = Unit prices |  |
| **PriceTypeCode** | Price (3 files) | `TRD`×6 | Regional | R:PriceType | TRD = Trade price ✓; RRP = Recommended retail price | .md calls it "the seller's code": decide whether regional or party list (Q20). |
| **CollaborationPriorityCode** | ExceptionCriteriaLine, ExceptionNotificationLine (2 files) | `High`×2 | Regional | R:Priority | HIGH; MEDIUM; LOW |  |
| **RankCode** | Prize (4 files) | `None`×4 | Regional | R:PrizeRank | `None` ✗ | No prizes: omit the element (Prize is optional). |
| **ProcessReasonCode** | ProcessJustification (3 files) | `Standard`×3 | Regional | R:ProcessJustification | STANDARD = Standard (open procedure) |  |
| **ProcurementSubTypeCode** | ProcurementProject (4 files) | `Purchase`×7, `Installation`×3 | Regional | R:ProcurementSubType | PURCHASE = Purchase; INSTALL = Installation |  |
| **ProcurementTypeCode** | ProcurementAdditionalType, ProcurementProject (11 files) | `Supplies`×15, `Green`×10, `Services`×3, `Works` | Regional | R:ProcurementType | SUPPLIES; SERVICES; WORKS; GREEN ✗ | `Green` (ProcurementAdditionalType) is a strategic-procurement aspect, not a contract nature: separate list R:StrategicProcurement GREEN. |
| **PropertyGroupTypeCode** | TenderingCriterionPropertyGroup (1 file) | `OnTrue` | Regional | R:PropertyGroupType | ONTRUE = Answered when criterion applies (was OnTrue) | ESPD-EDM has a real list for this (ON* codes) — Q25. |
| **ImportanceCode** | AdditionalItemProperty, ItemPropertyGroup (45 files) | `Mandatory`×90, `Optional`×76 | Regional | R:PropertyImportance | MANDATORY; OPTIONAL |  |
| **AdmissionCode** | QualificationResolution (1 file) | `Admitted`×2 | Regional | R:QualificationAdmission | ADMITTED; REJECTED |  |
| **QualificationApplicationTypeCode** | QualificationApplicationRequest, QualificationApplicationResponse (2 files) | `Regulated`×2 | Regional | R:QualificationApplicationType | REGULATED; SELFCONTAINED |  |
| **QualityControlCode** | ProcurementProject (4 files) | `Inspection`×10 | Regional | R:QualityControl | INSPECTION = Inspection on delivery |  |
| **RejectActionCode** | ReceiptAdvice, ReceiptLine (2 files) | `Credit`×4 | Regional | R:ReceiptAction | CREDIT = Credit requested; REPLACE = Replacement requested | One list with ShortageActionCode. |
| **ShortageActionCode** | ReceiptLine (1 file) | `Replace` | Regional | R:ReceiptAction | REPLACE | Shares R:ReceiptAction. |
| **QuantityDiscrepancyCode** | ReceiptLine (2 files) | `Damaged`×2 | Regional | R:ReceiptDiscrepancyReason | DAMAGED = Damaged | One list with RejectReasonCode (both "Damaged"). |
| **RejectReasonCode** | ReceiptAdvice, ReceiptLine (2 files) | `Damaged`×4 | Regional | R:ReceiptDiscrepancyReason | DAMAGED | Shares the list with QuantityDiscrepancyCode. |
| **ProfileStatusCode** | TradeItemLocationProfile (1 file) | `Active` | Regional | R:RecordStatus | ACTIVE | Shares R:RecordStatus with StatusCode (price list). |
| **ReminderTypeCode** | Reminder (3 files) | `Payment`×3 | Regional | R:ReminderType | PAYMENT = Payment reminder |  |
| **RepresentationTypeCode** | ContractingRepresentationType (3 files) | `Own`×3 | Regional | R:RepresentationType | OWN = On its own behalf |  |
| **RequiredCurriculaCode** | TenderingTerms (4 files) | `Installers`×4 | Regional | R:RequiredCurricula | INSTALLERS = Installers' qualifications |  |
| **ResidenceTypeCode** | ConsumptionReport (1 file) | `APT` | Regional | R:ResidenceType | APT = Apartment ✓ |  |
| **ValueDataTypeCode** | TenderingCriterionProperty (1 file) | `Amount`, `Quantity`, `Indicator`, `Percent` | Regional | R:ResponseDataType | AMOUNT; QUANTITY; INDICATOR; PERCENT | ESPD-EDM response-data-type list is the real model (Q25). |
| **RequiredResponseMessageLevelCode** | DigitalAgreement (1 file) | `Business` | Regional | R:ResponseMessageLevel | BUSINESS = Business response |  |
| **RetailEventStatusCode** | RetailEvent (1 file) | `Confirmed` | Regional | R:RetailEventStatus | CONFIRMED; PLANNED |  |
| **ConsumerIncentiveTacticTypeCode** | EventTacticEnumeration (1 file) | `TPR` | Regional | R:RetailTactic | TPR = Temporary price reduction ✓ | One retail-tactic list for the five *TacticTypeCode/EventTypeCode elements, or one each (Q26). |
| **DisplayTacticTypeCode** | EventTacticEnumeration (1 file) | `EndCap` | Regional | R:RetailTactic | ENDCAP = End-cap display (was EndCap) |  |
| **FeatureTacticTypeCode** | EventTacticEnumeration (1 file) | `Flyer` | Regional | R:RetailTactic | FLYER = Store flyer |  |
| **MiscellaneousEventTypeCode** | MiscellaneousEvent (1 file) | `StoreOpening` | Regional | R:RetailTactic | STOREOPEN = Store opening (was StoreOpening) |  |
| **PromotionalEventTypeCode** | PromotionalEvent (1 file) | `TPR` | Regional | R:RetailTactic | TPR ✓ |  |
| **TradeItemPackingLabelingTypeCode** | EventTacticEnumeration (1 file) | `Sticker` | Regional | R:RetailTactic | STICKER = Price sticker |  |
| **RevisionStatusCode** | ForecastRevision (1 file) | `Revised` | Regional | R:RevisionStatus | REVISED | Could reuse UBL DocumentStatus `Revised`. |
| **LossRiskResponsibilityCode** | DeliveryTerms (2 files) | `Buyer`×2 | Regional | R:RiskResponsibleParty | BUYER = Buyer; SELLER = Seller |  |
| **SanitaryMeasureTypeCode** | SanitaryMeasure (1 file) | `Disinfection` | Regional | R:SanitaryMeasure | DISINFECT = Disinfection |  |
| **ScoringSystemCode** | RepairabilityScore (38 files) | `Repairability index, 0–10`×38 | Regional | R:ScoringSystem | REPAIR10 = Repairability index, 0–10 (was `Repairability index, 0–10`) | Sentence with comma and en dash in a code (38 uses); the scale belongs in the list's description. |
| **SealStatusCode** | TransportEquipmentSeal (2 files) | `Applied`×4 | Regional | R:SealStatus | APPLIED = Applied | Possibly UNCL 4517 Seal condition (not verified). |
| **ServiceInformationPreferenceCode** | TransportServiceDescriptionRequest (1 file) | `Schedule` | Regional | R:ServiceInformationPreference | SCHEDULE = Schedule first |  |
| **ServiceTypeCode** | ServiceProviderParty (74 files) | `Logistics`×73, `Messaging` | Regional | R:ServiceProviderType | LOGISTICS = Logistics service; MESSAGING = Messaging service |  |
| **ShipConfigurationCode** | MaritimeTransport (5 files) | `Feeder container ship, 1,000 TEU`×3, `Dry cargo barge`×2 | Regional | R:ShipConfiguration | DRYBARGE = Dry cargo barge; FEEDER = Feeder container ship (was `Feeder container ship, 1,000 TEU`) | Sentences with spaces and commas. The capacity "1,000 TEU" is data, not a type: move it to text (or a measure). |
| **ShippingPriorityLevelCode** | Consignment, Shipment (4 files) | `Standard`×2, `Priority`, `Normal` | Regional | R:ShippingPriority | PRIORITY = Priority; STANDARD = Standard (was Standard and Normal) | `Normal` and `Standard` both mean "no priority": merge. |
| **ReasonCode** | Signature (1 file) | `Approval` | Regional | R:SignatureReason | APPROVAL = Approval | Real model: ETSI commitment types (proofOfApproval …), not a plain code list. |
| **SocialMediaTypeCode** | SocialMediaProfile (40 files) | `Photo sharing`×40 | Regional | R:SocialMediaType | PHOTO = Photo sharing (was `Photo sharing`) | Space in code (40 uses). |
| **StatementTypeCode** | Statement (1 file) | `Account` | Regional | R:StatementType | ACCOUNT = Statement of account |  |
| **StatusReasonCode** | CurrentStatus (1 file) | `Cleared` | Regional | R:StatusReason | CLEARED = Cleared (customs/border) |  |
| **SubmissionMethodCode** | TenderingProcess (3 files) | `Electronic`×3 | Regional | R:SubmissionMethod | ELECTRONIC; PAPER |  |
| **SupplyChainActivityTypeCode** | ItemInformationRequestLine, ExceptionCriteriaLine, SupplyChainActivityDataLine … (4 files) | `Sales`×4 | Regional | R:SupplyChainActivity | SALES = Sales |  |
| **SupplyTypeCode** | ClassifiedTaxCategory (42 files) | `Goods`×30, `Services`×29 | Regional | R:SupplyType | GOODS = Goods; SERVICES = Services |  |
| **TaxLevelCode** | PartyTaxScheme (223 files) | `State`×293, `National`×174 | Regional | R:TaxLevel | NATIONAL = Levied by the country; STATE = Levied by a state |  |
| **TaxTypeCode** | TaxScheme (1 file) | `Consumption` | Regional | R:TaxType | CONSUMPTION = Tax on consumption (was Consumption) |  |
| **TelecommunicationsServiceCallCode** | TelecommunicationsService (1 file) | `OUT` | Regional | R:TelecomCallType | OUT = Outgoing ✓ |  |
| **DutyCode** | CallDuty, TimeDuty (1 file) | `SETUP`, `MIN` | Regional | R:TelecomDuty | SETUP = Call set-up ✓; MIN = Per minute ✓ |  |
| **TelecommunicationsServiceCategoryCode** | TelecommunicationsService (1 file) | `INT`, `ROAM` | Regional | R:TelecomServiceCategory | INT = International ✓; ROAM = Roaming ✓ |  |
| **TelecommunicationsSupplyTypeCode** | TelecommunicationsSupply (1 file) | `BUS` | Regional | R:TelecomSupplyType | BUS = Business lines and data ✓ | `BUS` also appears in SubscriberTypeCode with another meaning. |
| **MeasureCode** | Temperature, MinimumTemperature (2 files) | `Target`×3, `Min` | Regional | R:TemperatureQualifier | TARGET = Target; MIN = Minimum |  |
| **TenderEnvelopeTypeCode** | TenderPreparation, TenderedProject (7 files) | `Combined`×7 | Regional | R:TenderEnvelope | COMBINED = Technical and financial together | One list with TenderTypeCode. |
| **TenderTypeCode** | Tender (3 files) | `Combined`×3 | Regional | R:TenderEnvelope | COMBINED | One list with TenderEnvelopeTypeCode. |
| **TenderResultCode** | TenderResult (4 files) | `Awarded`×4 | Regional | R:TenderResult | AWARDED; NOTAWARDED |  |
| **TimingComplaintCode** | ReceiptLine (1 file) | `Late` | Regional | R:TimingComplaint | LATE; EARLY |  |
| **TrackingDeviceCode** | TransportEquipment (1 file) | `GPS` | Regional | R:TrackingDevice | GPS = Satellite tracker ✓ |  |
| **ComparisonDataSourceCode** | ForecastExceptionCriterionLine (1 file) | `Buyer` | Regional | R:TradingPartnerRole | BUYER | Shares R:TradingPartnerRole. |
| **DataSourceCode** | ForecastExceptionCriterionLine, ForecastException (2 files) | `Seller`×2 | Regional | R:TradingPartnerRole | SELLER; BUYER | One list with ComparisonDataSourceCode. |
| **TransitDirectionCode** | MainCarriageShipmentStage (1 file) | `Export` | Regional | R:TransitDirection | EXPORT = Leaving the country; IMPORT; TRANSIT | Possibly UNCL 8101 (not verified). |
| **TranslationTypeCode** | TenderingCriterionProperty (1 file) | `None` | Regional | R:TranslationType | NONE = No translation; CERTIFIED; SIMPLE | `None` as a code; here meaningful. |
| **TransportationStatusTypeCode** | TransportationStatus, TransportationStatusRequest (3 files) | `Delivery`, `Current`, `Progress` | Regional | R:TransportationStatusType | DELIVERY = Status of delivery; CURRENT = Current status; PROGRESS = Progress report |  |
| **TransportEmergencyCardCode** | HazardousGoodsTransit (2 files) | `TEC-90-3480`×6 | Regional | R:TransportEmergencyCard | TEC903480 = Emergency card for UN 3480 (was `TEC-90-3480`) | Looks like an identifier of a card (CEFIC TREMCARD style), not a code; hyphens (Q23). |
| **TransportEventTypeCode** | TransportEvent (1 file) | `BorderCrossing` | Regional | R:TransportEventType | BORDERCROSS = Border crossing (was BorderCrossing) | Possibly UNCL 9353 / Rec-based event lists (not verified). |
| **TransportExecutionStatusCode** | TransportationStatus (6 files) | `InProgress`×6 | Regional | R:TransportExecutionStatus | INPROGRESS = In progress |  |
| **NotificationTypeCode** | NotificationRequirement (3 files) | `PreArrival`×3 | Regional | R:TransportNotificationType | PREARRIVAL = Pre-arrival notice (was PreArrival) | Same code as ReportTypeCode. |
| **ReportTypeCode** | CommonTransportationReport (1 file) | `PreArrival` | Regional | R:TransportNotificationType | PREARRIVAL = Pre-arrival report (was PreArrival) | Could share the list with NotificationTypeCode. |
| **TransportServiceCode** | MainTransportationService, AdditionalTransportationService, TransportationService (13 files) | `ROAD`×5, `NOTIFY`×3, `RAIL`×2, `RIVER`×2, `OceanContainer`×2, `MerchantHaulage`×2, `Weighing`, `RailContainer` | Regional | R:TransportService | RAILCONT = Container train (was RAIL and RailContainer); RIVERBARGE = River barge (was RIVER); FTL = Full truck load (was ROAD); OCEANCONT = Container liner service (was OceanContainer); MERCHHAUL = Merchant haulage (was MerchantHaulage); NOTIFY = Pre-arrival notice ✓; WEIGH = Weighing (was Weighing) | Mixed styles (RAIL/ROAD/RIVER upper case mode words, CamelCase service names). RAIL and RailContainer name the same container train; RAIL/ROAD/RIVER repeat TransportModeCode. |
| **DirectionCode** | TransportMeans (8 files) | `Westbound`×3, `Eastbound`×3, `Downstream`×2 | Regional | R:TravelDirection | EB = Eastbound; WB = Westbound; DS = Downstream; US = Upstream | .md: "as the carrier codes its services" — regional list instead of per carrier. |
| **TreatmentPathwayCode** | EndOfLifeTreatment (2 files) | `Mechanical recycling`×2 | Regional | R:TreatmentPathway | MECHRECYCLE = Mechanical recycling (was `Mechanical recycling`) | Space in code. |
| **UrgencyCode** | TenderingProcess (3 files) | `Normal`×3 | Regional | R:Urgency | NORMAL; ACCELERATED |  |
| **CurrentChargeTypeCode** | UtilityItem (5 files) | `M`×6 | Regional | R:UtilityChargeType | M = Monthly charge ✓ | Shares list with OneTimeChargeTypeCode? (M is a period, CONN a charge kind — keep apart if preferred). |
| **OneTimeChargeTypeCode** | UtilityItem (1 file) | `CONN` | Regional | R:UtilityChargeType | CONN = Connection charge ✓ |  |
| **SpecificationTypeCode** | SubscriberConsumption (6 files) | `Detailed`×6 | Regional | R:UtilitySpecificationType | DETAILED = Detailed |  |
| **UtilityStatementTypeCode** | UtilityStatement, Consumption (6 files) | `Electricity`×6, `Water`×6, `Gas`×2, `Telephone`×2 | Regional | R:UtilityType | ELEC = Electricity; GAS = Gas; WATER = Water; TEL = Telephone | Also the right list for SubscriberTypeCode in ConsumptionLine/UtilityItem (see there). |
| **ValidationResultCode** | ResultOfVerification (1 file) | `Valid` | Regional | R:ValidationResult | VALID = Valid; INVALID = Invalid |  |
| **WasteMovementTypeCode** | WasteMovement (1 file) | `Recovery` | Regional | R:WasteOperationCategory | RECOVERY = Recovery; DISPOSAL = Disposal | Shares list with WasteNotificationTypeCode (Basel Convention distinction). |
| **WasteNotificationTypeCode** | WasteNotification (1 file) | `Recovery` | Regional | R:WasteOperationCategory | RECOVERY = Recovery | Shares list with WasteMovementTypeCode. |
| **WebSiteTypeCode** | WebSite (2 files) | `Extranet`, `Company` | Regional | R:WebSiteType | COMPANY = Company site; EXTRANET = Extranet |  |
| **WeightingAlgorithmCode** | AwardingTerms (4 files) | `WeightedSum`×4 | Regional | R:WeightingAlgorithm | WSUM = Weighted sum (was WeightedSum) |  |
| **WeightingTypeCode** | QualificationApplicationRequest, QualificationApplicationResponse (2 files) | `None`×2 | Regional | R:WeightingType | NONE = No weighting | `None` as a code; here meaningful ("no weighting"). |
| **WeightStatementTypeCode** | WeightStatement (1 file) | `VGM` | Regional | R:WeightStatementType | VGM = Verified gross mass ✓ |  |
| **WorkPhaseCode** | WorkPhaseReference (2 files) | `Furnish`, `Supply` | Regional | R:WorkPhase | SUPPLY; FURNISH |  |
| **WorkTypeCode** | WorkQuantityTotal (1 file) | `Installation` | Regional | R:WorkType | INSTALL = Installation | Same code as ProcurementSubTypeCode Installation. |

## Party-specific list (not world-wide; Q1) — 4 elements

| Element | Context | Current values | Source | Proposed list (listID) | Proposed codes (CODE = name) | Problems |
|---|---|---|---|---|---|---|
| **AccountingCostCode** | Invoice, Order, CreditNote … (62 files) | `6120`×16, `3100`×12, `500`×10, `4410`×8, `PWD-PARKS-26`×8, `2200`×5 … (+8 more) | Party | P:<buyer>:CostCentre | cost centres as they are (500, 4410, 2200, PWD-PARKS-26 …) | Party-specific accounting codes; a shared world list makes no sense. PWD-PARKS-26 has hyphens. |
| **FundingProgramCode** | TenderingTerms (4 files) | `PARKS-26`×4 | Party | P:<buyer>:FundingProgramme | PARKS26 = Parks programme 2026 (was PARKS-26) | Programme of one buyer; hyphen. |
| **BuyerReferenceCode** | BuyerAssignedReference (6 files) | `SCG-AP-FARMS`×2, `PWD-PARKS-26-AP`×2, `VT-CLAIMS`, `LD-AP-CLAIMS` | Party | P:<buyer>:InvoiceRouting | SCGAPFARMS, PWDPARKS26AP, LDAPCLAIMS, VTCLAIMS (hyphens removed) or as they are | Buyer-specific routing codes. |
| **TradeServiceCode** | TransportMeans (1 file) | `TWL-ISL` | Party | P:<carrier>:TradeService (Tidewell Ocean Lines) | TWLISL = Tidewell island service (was `TWL-ISL`) | Carrier-specific service id; hyphen. |

## Lists shared by several elements

- **CountryIdentificationCode-2.4-world**: IdentificationCode, NationalityCode
- **ISPS Code security levels**: CurrentOperatingSecurityLevelCode, SecurityLevelCode
- **Language-2.4**: DefaultLanguageCode, LocaleCode, NoticeLanguageCode, PreferredLanguageLocaleCode, TenderLanguageLocaleCode
- **PackagingType-2.4**: PackagingTypeCode, TransportHandlingUnitTypeCode
- **R:AllowedIndicator**: MultipleTendersCode, SubcontractingConditionsCode, VariantConstraintCode
- **R:ComparisonOperator**: ExpressionCode, ThresholdValueComparisonCode
- **R:Confidentiality**: ConfidentialityLevelCode, PrivacyCode, SecurityClassificationCode
- **R:ConsumptionLevel**: ConsumersEnergyLevelCode, ConsumptionLevelCode
- **R:ContractingSystem**: ContractingSystemCode, ContractingSystemTypeCode
- **R:CustomsDeclarationType**: FunctionCode, TypeCode
- **R:CustomsProcedure**: CustomsProcedureCode, ProcedureCode
- **R:EconomicOperatorRole**: RoleCode, TendererRoleCode
- **R:EnergySource**: EnergySourceTypeCode, FuelTypeCode
- **R:EquipmentPartyType**: OwnerTypeCode, ProviderTypeCode, SealIssuerTypeCode
- **R:ExceptionResolution**: ExceptionResolutionCode, ResolutionCode
- **R:ExecutionRequirement**: ExecutionRequirementCode, TendererRequirementTypeCode
- **R:ForecastPurpose**: ForecastPurposeCode, PurposeCode
- **R:FreightRateClass**: FreightRateClassCode, TariffClassCode
- **R:Frequency**: MaintenanceFrequencyCode, PaymentFrequencyCode, TimeFrequencyCode
- **R:MeterReadingMethod**: LatestMeterReadingMethodCode, PreviousMeterReadingMethodCode
- **R:ReceiptAction**: RejectActionCode, ShortageActionCode
- **R:ReceiptDiscrepancyReason**: QuantityDiscrepancyCode, RejectReasonCode
- **R:RecordStatus**: ProfileStatusCode, StatusCode
- **R:RetailTactic**: ConsumerIncentiveTacticTypeCode, DisplayTacticTypeCode, FeatureTacticTypeCode, MiscellaneousEventTypeCode, PromotionalEventTypeCode, TradeItemPackingLabelingTypeCode
- **R:TenderEnvelope**: TenderEnvelopeTypeCode, TenderTypeCode
- **R:TradingPartnerRole**: ComparisonDataSourceCode, DataSourceCode
- **R:TransportNotificationType**: NotificationTypeCode, ReportTypeCode
- **R:UtilityChargeType**: CurrentChargeTypeCode, OneTimeChargeTypeCode
- **R:UtilityType**: SubscriberTypeCode, UtilityStatementTypeCode
- **R:WasteOperationCategory**: WasteMovementTypeCode, WasteNotificationTypeCode
- **UNCL 1001**: CreditNoteTypeCode, DebitNoteTypeCode, DespatchAdviceTypeCode, DocumentTypeCode, InvoiceTypeCode, OrderTypeCode, WaybillTypeCode
- **UNCL 4343**: OrderResponseCode, ResponseCode
- **UnitOfMeasure-2.4**: TimeBasisCode, ValueUnitCode
- **WCO Harmonized System 2022**: ItemClassificationCode, TariffCode
- **XB:TaxExemptionReason**: ExemptionReasonCode, TaxExemptionReasonCode
- **CurrencyCode-2.4-world**: the ten currency elements (already one list).
- **UNCL 4465 / UBL AllowanceChargeReason-2.4**: AllowanceChargeReasonCode, ResponseCode in DiscrepancyResponse (proposed).

## Open questions

- **Q1** Party-specific codes (AccountingCostCode, BuyerReferenceCode, FundingProgramCode, TradeServiceCode; maybe PriceTypeCode): build one small list per issuing party (`P:` lists), or exempt them from code-list validation as identifiers that only the issuing party defines? A shared world list would be artificial.
- **Q2** listID on *every* code: nine UBL lists have no listID and phase 2 rejects any listID on them; the UBL PackagingType listID contains a line break. Options: (a) world copies of those lists that carry a listID (e.g. UBL's CanonicalUri `urn:oasis:names:specification:ubl:codelist:gc:<Name>`) and the Rec 21 title on one line, with the CVA pointing to the copies; (b) accept "no listID" for those; (c) normalise whitespace in the validator.
- **Q3** AllowanceChargeReasonCode: keep UBL's default list (UNCL 4465 content, validated) and pick codes by its names (91 agreed discount, 78 volume discount …), or switch to the real UNCL 5189 (as EN 16931 does), which needs a world list and a world CVA context replacing UBL's?
- **Q4** External listID style: the UBL-style strings proposed here (`UN/EDIFACT EDED 1001`, `ISO 20022 ExternalPurpose1Code`) or URNs for everything (`urn:ubl-examples:world:codelist:…` also for copies of external lists)? UBL-covered elements must keep UBL's strings either way.
- **Q5** Versioning: add `listVersionID` (e.g. `2026`, `D.23A`, `HS 2022`) or keep the version only in the genericode CanonicalVersionUri?
- **Q6** Granularity: about 60 % of the proposed regional lists have one or two codes today. Keep one list per concept (cleaner, more lists), or merge small related ones (e.g. one R:RetailTactic, one R:AllowedIndicator, one R:TradingPartnerRole, as proposed)? Should each list get a few plausible codes beyond those used (e.g. DISPOSAL, NOTALLOWED)?
- **Q7** `None` and `Any`: omit the element (proposed where the element is optional), or define NONE codes so the documents keep showing the element?
- **Q8** TimeBasisCode `Year`: reuse UBL UnitOfMeasure (ANN) or a regional TimeBasis list?
- **Q9** Document *type* codes: use UNCL 1001 for DespatchAdviceTypeCode (351) and WaybillTypeCode (740/720/730/711), or keep finer regional lists (WaybillTypeCode currently names the transport convention: AWB, CIM, CMR, CMNI)?
- **Q10** Procurement and commodity classification: HS cannot classify services (9988.00) and PARKS-FURN is the buyer's own category. Invent a regional procurement vocabulary (CPV-like), use UN CPC Ver.2.1 for services, or both? And Consignment/TariffCode: is it the HS code (value) or the carrier's tariff (reason)?
- **Q11** Packing group: UNPackingGroupCode (I/II/III) and PackagingDangerLevelCode (UNCL 8339: 1/2/3) express the same concept — two notations or one?
- **Q12** EmS pairs: IMDG writes `F-A, S-I`. Allowed form for the code: `F-A,S-I`, `F-A S-I` (space), or two-part code without hyphens? Hyphen is the standard's own character; the comma/space are the problem.
- **Q13** MedicalFirstAidGuideCode: switch to IMO MFAG table numbers (meaning of the UBL element) or keep the ERG guide numbers and document the list as ERG?
- **Q14** CoordinateSystemCode: EPSG `4326` (authoritative code) or keep `WGS84` in a regional list?
- **Q15** AddressFormatCode: regional list XU/XB/XL (one format per country, as now) or UNCL 3477 (street-number order), which carries less information?
- **Q16** National vs regional for EntitySizeCode and the meter-reading method lists: are thresholds/methods the same in all three countries (regional, proposed) or national?
- **Q17** MarketCode FSE: keep 3 letters or adopt the 4-character ISO 10383 MIC shape (e.g. XFSE) in the regional list?
- **Q18** PaymentChannelCode: should it name the world's payment systems (FERRA-RTGS, LUMEPAY, CORAL-NET, TRADE-ACCORD-PAY from countries.json) as proposed, and with which code spelling (their ids contain hyphens)?
- **Q19** FormatCode `PDF/A-3`: invented PDFA3, or PRONOM PUIDs (an external registry) — doubtful fit?
- **Q20** PriceTypeCode TRD: regional price-type list or the seller's own list?
- **Q21** LifecycleStageCode: regional list or EN 15804 life-cycle modules (A1–A3 … C1–C4) as an external model?
- **Q22** SealIssuerTypeCode: adopt UNCL 9303 (sealing party) instead of the shared regional R:EquipmentPartyType?
- **Q23** TransportEmergencyCardCode `TEC-90-3480` is identifier-like: list of cards (regional) or treat as party/document identifier?
- **Q24** Customs: one Trade Accord customs data model (regional lists, proposed: procedures, statuses, declaration types) or national customs lists? The .md of CustomsStatusCode says "Bayvarra's customs status".
- **Q25** Procurement documents follow EU eForms/ESPD closely. Use the real eForms/ESPD-EDM code lists (contract-nature, procurement-procedure-type, criterion-element-type, response-data-type …) as external lists, or invented regional lists modelled on them (proposed, since the world is not in the EU)?
- **Q26** Retail/CPFR elements: one R:RetailTactic list for TPR/EndCap/Flyer/Sticker/StoreOpening (proposed) or one list per UBL element? GS1 lists could be a model but were not verified.
- **Q27** CountrySubentityCode: `UL`/`CO` as now, or ISO 3166-2 style `XB-UL`/`XB-CO`?
- **Q28** Tax exemption reasons: national lists without the country prefix (XB:TaxExemptionReason EXP, PUBLIC …) or one regional list keeping the prefixed codes (XBEXP …)? Codes must lose the hyphens either way, unless hyphens are allowed in invented codes.
- **Q29** DocumentTypeCode for Tariff, Terms and ReturnNotice: nearest UNCL 1001 codes, or a regional list for document references that 1001 does not cover?
- **Q30** InvoicePeriod/DescriptionCode `Month`: keep (regional PeriodDescription) or replace with UNCL 2005 as EN 16931 uses it (VAT point date code)?
- **Q31** Codes marked "verify" were not checked against the published list text (UNCL 7085, 2475, 8273 `ICA`, Rec 28 numbers, IMDG EmS for UN 2911, ISO 20022 TRPT/GOVT meanings, CMNI in 1001). Confirm against the sources before building.
