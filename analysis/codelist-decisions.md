# Code-list decisions

The decisions taken in the review of `codelist-classification.md`, in order.

## General rules

- **Party-internal codes** (Q1): a code a party defines internally gets no code list and no listID, unless it could be confused between parties. AccountingCostCode, BuyerReferenceCode, FundingProgramCode and TradeServiceCode get no list; their values may keep their hyphens.
- **No filler, nothing implied by absence** (Q7, UBL IND5/IND6, 7.2 semantic conformance): a "none" that the receiver needs is stated with a defined code. A filler is removed. An element that only a filler covered comes back through a real business situation.
- **Semantic conformance** (7.2): every element is used according to its UBL 2.5 definition.

- **Not everything UN/EDIFACT** (Q20): UBL is not "EDIFACT in XML". A UN/EDIFACT (UNCL) list is used only where UBL itself already uses it (its default lists), where established practice uses it (EN 16931: 1001, 5189, 7161), or where it is clearly the best authority for the domain. Otherwise a list from the domain's own authority (IMO, ISO, PRONOM, EPSG, ERG …) or a regional Trade Accord list.

## Decisions

| Q | Decision |
|---|---|
| EA | unitCode EA replaces H87 and C62. SET stays for real sets. Exceptions (identifier report): tonnage and the half pallet place stay C62, rate of turn E96, TEU capacity 20, persons IE, shares E21. Ballast water TNE becomes MTQ. |
| Q1 | Party-internal codes have no list (see above). |
| Q2 | (a) World copies, each with a listID, of the nine UBL lists that have none and of PackagingType (whose listID has a line break). The world CVA points to the copies. |
| Q3 | (b) Real UNCL 5189 for allowances and UNCL 7161 for charges, bound on ChargeIndicator. Every allowance and charge gets a code. UBL's AllowanceChargeReason list carries 4465 content under a 5189 label: say so in the note, and possibly report it to the OASIS UBL TC. |
| Q4 | (a) External lists in UBL text style (`UN/EDIFACT EDED nnnn`, `ISO 20022 <name>`, `WCO HS 2022`, `ISIC Rev.4`). The world's lists use URNs: `urn:ubl-examples:world:codelist:<Name>Code`, and national ones `urn:ubl-examples:world:<CC>:codelist:<Name>Code`. schemeID follows the same rule. |
| Q5 | No version attribute, because listVersionID is deprecated in UBL 2.5. The edition goes in the listID only where it is part of the standard's name (`WCO HS 2022`, `ISIC Rev.4`). Otherwise the version is in the genericode file only. |
| Q6 | (a) One list per concept, with plausible extra codes where the concept has room for them. Qualified variants of one concept share its list: Previous/Latest MeterReadingMethod, (Previous)CancellationReason, (Current)ChargeType, (Current)OperatingSecurityLevel, (Required)ResponseMessageLevel, (Required)Curricula, (Applicable)Category. The listID is the concept's name. |
| Q7 | PackagingDangerLevel "no packing group", InhalationToxicityZone "not toxic by inhalation" and SecurityClearance "not required" get defined codes. EmergencyProceduresCode `None` belongs to UN 2911 (radioactive, excepted package) and gets its real EmS (F-I, S-S; verify). The F-E on SecondaryHazard is removed, because an EmS belongs to the UN entry. The mast flow already has UN 2920 in packing group II, so PackagingDangerLevelCode `2` can cover that element without a new scenario. CompanyLegalFormCode `Any` is removed and said in the tender text instead. PreviousCancellationReasonCode and Prize are removed and come back through real scenarios: a relaunched tender and a design contest. |
| Q8 | (a) TimeBasisCode uses UN/ECE Rec 20 (ANN). CalculationMethodCode gets a regional list. |
| Q9 | (a), for now: UNCL 1001 for DespatchAdviceTypeCode (351) and WaybillTypeCode (730/740/720/711). The convention (CMR, CIM, CMNI) is no longer a code. |
| Q11 | (a) Each element keeps its own source. UNPackingGroupCode uses a world list based on the UN Model Regulations (I/II/III, plus NA for "no packing group assigned"). PackagingDangerLevelCode uses UNCL 8339 (1/2/3), or is left out when there is no packing group. The build checks that the two agree (I↔1, II↔2, III↔3). |
| Q12 | (b) EmS pairs are written `F-A,S-I`: the IMDG form without the space. They come from a world list of the pairs used plus extras, with listID `IMO IMDG EmS`. Hyphens in external codes are allowed where the standard writes them. |
| Q13 | (a) MedicalFirstAidGuideCode keeps the ERG guide numbers (147, 161, 132), with listID `ERG 2024`. The `.md` explanations say that the guide used is the ERG. To verify: that the IMDG Code no longer gives MFAG table numbers per UN number. |
| Q14 | (a) CoordinateSystemCode `4326`, listID `EPSG` (WGS 84 geographic), replacing `WGS84`. The platform's grid reference is part of the identifier questions. |
| Q15 | (a) AddressFormatCode: a regional list with one code per country format (XU/XB/XL). The full layout of each format is its description. The address fix itself runs separately (see the work items). |
| Q16 | (a) Both regional. EntitySizeCode gets a Trade Accord definition with thresholds in the style of the EU SME definition (headcount plus turnover, the limits given in all three currencies and their minor units). Parties get headcount and turnover, and the size class follows from them. MeterReadingMethod gets one regional list, with extra codes such as SMART and PROFILE. |
| Q17 | (b) MarketCode becomes a 4-character code shaped like ISO 10383 (e.g. `XFER` for the Ferrano Stock Exchange). It is checked against the published MIC list, as the currencies are against ISO 4217, with a stored copy for `--check`. listID: world URN. Fix the ISIN check digit in the same pass. |
| Q18 | **Open until further research.** PaymentChannelCode `IBAN` is wrong: an account format, not a channel. The candidate is UNCL 4435 (payment channel) for the kind of channel, with PaymentRailID naming the system. Research: what 4435 really contains; how ISO 20022, EN 16931 and Peppol use the payment channel; whether it duplicates PaymentRailID (new in UBL 2.5). |
| Q19 | (b) FormatCode uses PRONOM PUIDs (listID `PRONOM`). The registry's slash is allowed. The build checks that FormatCode agrees with MimeCode. To verify: the PUIDs for PDF/A-3. |
| Q20 | (b) PriceTypeCode uses a regional Trade Accord list (TRD trade price, RRP recommended retail price, CAT catalogue price, CON contract price, …). The buyer must understand it, so it is not the seller's own code (Q1). The tender catalogue uses CON. |
| Q21 | (b) LifecycleStageCode uses a regional list with the UBL definition's stages (SOURCING, MANUFACTURING, DISTRIBUTION, USAGE, ENDOFLIFE, maybe RECOVERY). Each description names the matching EN 15804 modules. FullnessIndicationCode gets a consistent separate list (CRADLETOGATE …). The footprint's standard names the real one (e.g. ISO 14067). |
| Q22 | (c) SealIssuerTypeCode uses a regional list (SHIPPER, CARRIER, CUSTOMS, PHYTOSANITARY, VETERINARY …). Each description maps to DCSA seal source and UNCL 9303. OwnerTypeCode, ProviderTypeCode and SealIssuerTypeCode get separate lists. SealStatusCode gets a regional list, treated the same way. To verify: the DCSA codes. |
| Q23 | (a) TransportEmergencyCardCode uses a regional list of the Accord's emergency cards, one per hazard class (TEC1 … TEC9, plus a general card), following ADR's class-based instructions in writing. `TEC-90-3480` becomes `TEC9`. The build checks that the card matches HazardClassID. HazardousCategoryCode `UN` becomes the class. |
| Q24 | (a) One Trade Accord customs data model, with shared regional lists for procedures, statuses, declaration types and subtypes, export reasons and types, nature of transaction (mapped to the UN/EU statistics list), transit direction and location types. The Accord is a free trade area, not a customs union, so tariffs, rates and exemptions stay national. CustomsStatus means "not in free circulation in the declaring territory". CustomsProcedureCode gets **new Accord codes**, not the EU's: the Accord's own structure, with the requested procedure followed by the previous one. Proposed: a 2-digit requested procedure plus a 2-digit previous procedure, numbered differently from the EU (10 release for free circulation, 20 temporary admission, 30 export, 35 re-export, 40 transit, 50 customs warehousing; 00 = no previous procedure). So `4000` becomes `1000`. The full list follows in the list review. |
| Q25 | (b) Procurement uses regional Trade Accord lists modelled on eForms/ESPD-EDM, with the eForms/ESPD code mapped in the descriptions (procedure types incl. RESTRICTED, NEGOTIATED, DESIGNCONTEST; response data types; property group types; cancellation reasons …). The note: the Accord's procurement rules are modelled on the EU's, without being EU law. |
| Q26 | Settled by Q6: one list per element (RetailTactic …). |
| Q27 | (b) CountrySubentityCode in ISO 3166-2 style: `XB-CO`, `XB-UL`, `XB-NT`. A national list `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`, structured like ISO but not ISO 3166-2 itself. Third subdivision: the Northern Territory (north coast, Gullhaven, the gas plant), a federal territory with its own sales tax rate. Done along with it: the river made a real river, the south-western border following the river, and the sawmill moved to the north bank (sub-agent). |
| Q28 | (a) Tax exemption reasons use national lists without the country prefix. XB: EXP, RESALE, PUBLIC, SVCB2B, WATER, LEVY. XU: EXP, SVCABROAD. Plus extras, with a national listID. ExemptionReasonCode on PartyTaxScheme uses the same XB list. The Northern Territory uses the XB list. The build checks that the list matches the seller's country. The reason text is bilingual for XU. |
| Q29 | (b) DocumentTypeCode uses UNCL 1001 where it fits, plus a regional supplementary list (TARIFF, TERMS, RETURNNOTICE, plus extras), each value with its own listID. The CVA accepts either list, chosen by listID. Check 1001 for exact matches first. |
| Q30 | (a) InvoicePeriod/DescriptionCode uses a regional PeriodDescription list (MONTH, QUARTER, HALFYEAR, YEAR, WEEK …), following the UBL definition. EN 16931's use of this element for the VAT point date code (BT-8, UNCL 2005) is considered semantically incorrect. A tax point date belongs in TaxPointDate. |
| Q10 | (a) Follow the UBL definitions: HS 6-digit and the national tariff go in CommodityCode, as two CommodityClassification entries, each with its listID. ItemClassificationCode gets UN CPC Ver.2.1, for goods and services. PARKS-FURN becomes a CPC code. Consignment/TariffCode is the carrier's freight tariff item, with no list (Q1). |

## Identifier decisions

| ID-Q | Decision |
|---|---|
| 7 | **An identification convention per party**, covering everything it identifies:
- **GS1:** GTIN for items, GLN for party and locations, SSCC for logistic units, GRAI for returnable assets. Parties: Lumeway Distribution 6-xb, Brightmarket Stores 26-xb, the furniture maker 37-xb.
- **ISO via Codana (31-xu):** the Codana item number (ISO 15459 style), an ISO 6523 organisation identifier with a fictional ICD, ISO 15459 licence plates. Parties: Valdara 5-xu, the 3PL 8-xu, the packaging maker, the power station, the grid operator.
- **Own:** seller's item IDs only, register numbers, company-local or local unit IDs. Parties: Saltmere 27-xb, the sawmill 36-xb, the island's cotton farms and gin, the utilities.

All prefixes are fictional: GS1 from an unallocated prefix range, Codana's IAC and ICD checked against the AIM and ISO 6523 registers. A reseller shows its own number and the maker's (ManufacturersItemIdentification). Inner packages get local IDs without a scheme. Ranges in IDs become one Package with Quantity, except the mast crates, which get six individual Saltmere IDs. The build checks that unit IDs agree across the documents of a flow. |
| 6 | Lowercase for every language code: the `languageID` attribute (BCP 47 / RFC 5646, `xsd:language`) and the coded elements and Language/ID (ISO 639). A world Language list follows the ISO 639-2 Registration Authority (Library of Congress), not UBL's copy: lowercase codes, B and T codes as separate entries, no duplicates, `qau`/`qal` added as local-use codes, listID `ISO 639`. The world CVA uses it instead of UBL's list. `build_codelists.py` fetches the LoC list and records the date. LocaleCode and the tender language codes become `en`. |
| 6b | (a) Every sender tags its English texts with its own region: `languageID` `en-XU`, `en-XB` or `en-XL`. These are valid BCP 47 tags, because RFC 5646 §2.2.4 reserves the region subtags XA–XZ for private use. The national languages stay `qau`/`qal`. Coded elements (LocaleCode, Language/ID, DefaultLanguageCode) stay plain `en`, because ISO 639 has no region. |
| 5 | (b) AttributeID uses regional lists, one per meaning: a dimension list (LENGTH, WIDTH, HEIGHT, DEPTH, THICKNESS, SEATHEIGHT, BENCHLENGTH, LOADINGLENGTH, SLOT …, each mapped to UNCL 6313 in its description), shared by Dimension, MeasurementDimension and RangeDimension; a temperature list (STORAGE, TRANSPORT, FLASHPOINT, EMERGENCY, PRODUCT, AMBIENT …); and a list for the other attributes (COLOUR, PALLETPLACES, FLOORSPACE, TEU, SEAL …). schemeID = the list's URN (ID-Q2). |
| 4 | (b) Make values that look real visibly fictional, in the right format: item numbers with a non-company GS1 prefix (world scheme, check digit kept); container owner codes checked as free; call signs, MMSI, aircraft prefixes and the ULD owner from unallocated or world blocks (one rule for all ITU-based ones); the ULD owner a world airline. |
| 3 | National schemes in today's style for licence plates, aircraft registrations and rail wagon numbers (e.g. `…:XB:vehicle-register`), with formats in countries.json checked like the phone numbers. Aircraft prefixes are chosen with ID-Q4; wagon numbers follow the UIC 12-digit structure with check digit. Driving licences and national ID numbers get no schemeID. |
| 2 | (a) Codes held in ID elements carry schemeID = their code list's identifier (about 1,440 additions): TaxCategory/ID `UN/EDIFACT EDED 5305`, TaxScheme/ID `UN/EDIFACT EDED 5153`, Language/ID `ISO 639`, HazardClassID (UN Model Regulations class), DeliveryTerms/ID. The two DeliveryTerms without a scheme get one. Assumed, not yet confirmed by the user: the existing `INCOTERMS` stays as it is, and new external schemeIDs use the listID text. |
| 1 | Keep today's schemeID names (`urn:ubl-examples:world:XB:register`, `…:item`, `…:endpoint` …). New world schemes follow the same lowercase style (e.g. `…:XB:tax`, `…:payment-system`). The examples show that a schemeID has no fixed format, unlike the listIDs, which mirror UBL. |

## Separate work items found along the way

- IND5: `retail/10-DocumentStatus.xml` has an empty `cbc:ID` in AdditionalDocumentResponse/DocumentReference. The build's IND5 check covers only aggregates, so it should also check basic elements. Add IND7/IND8/IND9 checks as well.
- ISIN `XU0001042505` fails ISO 6166; it should be `XU0001042501` (74 uses in 73 files).
- retail/03, 04 and 20 refer to the catalogue with the wrong UUID (`8fbee548-…` instead of `f5163e36-0159-5b9f-b172-a86137e369e6`).

- Addresses (being done by a sub-agent):
  - the full format layout per country, including the optional fields and the bilingual rule (national language / English on one line);
  - a format code on every structured address;
  - AddressLine generated from the format;
  - fix the cotton farm address ("kilometre 4" against BuildingNumber 35);
  - build checks.

## For future research

- **EN 16931 and ItemClassificationCode.** EN 16931 (BT-158, item classification identifier) and Peppol BIS put HS and other customs codes in `CommodityClassification/ItemClassificationCode`, with a listID from UNCL 7143. UBL 2.5 defines ItemClassificationCode as "A code signifying the trade classification of the commodity" and CommodityCode as "The harmonized international commodity code for cross border and regulatory (customs and trade statistics) purposes". Why does the EN mapping use the element whose definition doesn't fit? Was it a deliberate choice in the CEN TC 434 syntax binding (for example, one element for every classification scheme), a historical one from UBL 2.1, or an oversight? Sources to check:
  - the EN 16931-3-2 UBL syntax binding;
  - CEN/TC 434 working documents;
  - the Peppol BIS Billing 3.0 rules;
  - the UBL TC's minutes on CommodityClassification.
- **EN 16931 and InvoicePeriod/DescriptionCode.** BT-8 "Value added tax point date code" is bound to `cac:InvoicePeriod/cbc:DescriptionCode`, using a subset of UNCL 2005 (3 invoice date, 35 delivery date, 432 paid to date). Peppol BIS Billing 3.0 (docs.peppol.eu, checked 2026-11-11) defines it as "The code of the date when the VAT becomes accountable for the Seller and for the Buyer". Its rules are BR-CO-03 (mutually exclusive with BT-7 Value added tax point date, which is bound to `cbc:TaxPointDate`), BR-CL-06 and PEPPOL-EN16931-CL006 ("UNCL 2005 D.16B"). UBL defines Period/DescriptionCode as "A description of this period, expressed as a code". A tax point date is not a description of the invoice period. The versions to check are EN 16931-1:2017+A1:2019 (semantic model) and CEN/TS 16931-3-2 (the UBL syntax binding). Does the ongoing revision of EN 16931 change this?
- **Sources (Q31), checked 2026-11-11.**
  - UNECE (service.unece.org and unece.org) returns 403 behind Cloudflare, both from this environment and from a GitHub runner (workflow `check-sources.yml`, run 42971783848).
  - ISO 20022 external code sets also return 403.
  - Reachable: EPSG, PRONOM, UN CPC, the ISO 10383 MIC list, ISO 4217 (SIX), DCSA, IMO and Peppol docs.
  - **Authoritative alternative for the UNCL lists: UN/CEFACT's own GitHub repository `uncefact/vocabulary-outputs`** (the JSON code lists in `_data/*codelist.json`). It is reachable. It confirms UNCL 4435 (PaymentMeansChannelCodeList: 1 ordinary post … 5 S.W.I.F.T., 6 other transmission networks, 8 Fedwire, 14 national ACH, 15 other ACH, ZZZ).
  - It also explains Q3. UN/CEFACT itself calls the 4465 content "AllowanceChargeReasonCodeList" (95 = Small order processing service charge) and the 5189 content "AllowanceChargeIdCodeList" (95 = Discount, 100 = Special rebate). UBL's default list follows the UN/CEFACT naming; only its listID label `UN/EDIFACT EDED 5189` is wrong. Decision Q3 (b) stands: EN 16931 uses 5189 for the allowance reason code.
- **For the OASIS UBL TC** (findings to report):
  1. AllowanceChargeReasonCode default list: listID `UN/EDIFACT EDED 5189`, but its content is UNCL 4465. UN/CEFACT calls 4465 "AllowanceChargeReasonCodeList", so the content follows UN/CEFACT and only the label is wrong.
  2. The Language default list (`LanguageCode-2.4.gc`, version 2020-04-17, identical in the UBL 2.4 and 2.5 packages, LocationUri still 2.3). Its source is the ISO 639-2 RA table at the Library of Congress.
     - The codes are uppercased, while ISO 639 and BCP 47 recommend lowercase; the list's own cross-reference column keeps them lowercase.
     - Alpha-3 B/T pairs are merged into one code value (`GER (B) DEU (T)`, `DUT (B) NLD (T)`, `FRE (B) FRA (T)` …), each twice, so `DEU`, `NLD`, `FRA` etc. are not valid codes.
     - The local-use range is a single literal `QAA-QTZ`, which no real code can match.
  3. PackagingType default list: its listID contains a line break.
  4. Nine default lists have no listID (Chip, DocumentStatus, LineStatus, Latitude/LongitudeDirection, Operator, SubstitutionStatus, WeekDay, ReceiptAdviceType), and ReceiptAdviceTypeCode has a default list but no CVA context.
  5. The CVA has no context for `@languageID`.
- Q31: codes not yet checked against the published lists. UNCL 1001 351/711/720/730/740, 5189/7161 choices, UN CPC Ver.2.1 codes, plus the ones the classification marks "verify". unece.org blocked this environment on 2026-11-11.
