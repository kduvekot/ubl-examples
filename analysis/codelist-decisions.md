# Code-list decisions

The decisions taken in the review of `codelist-classification.md`, in order.

## General rules

- **Party-internal codes** (Q1): a code a party defines internally gets no code list and no listID, unless it could be confused between parties. AccountingCostCode, BuyerReferenceCode, FundingProgramCode and TradeServiceCode get no list; their values may keep their hyphens.
- **No filler, nothing implied by absence** (Q7, UBL IND5/IND6, 7.2 semantic conformance): a "none" that the receiver needs is stated with a defined code. A filler is removed. An element that only a filler covered comes back through a real business situation.
- **Semantic conformance** (7.2): every element is used according to its UBL 2.5 definition.

- **Not everything UN/EDIFACT** (Q20, sharpened after the UNCL 1001 review): UBL is not "EDIFACT in XML". A UN/EDIFACT (UNCL) list is used only where UBL itself already uses it (its default lists), where established practice uses it (EN 16931: 1001, 5189, 7161), or where it is clearly the best authority for the domain. Otherwise a list from the domain's own authority (IMO, ISO, PRONOM, EPSG, ERG …) or a regional Trade Accord list.

## Decisions

| Q | Decision |
|---|---|
| EA | unitCode EA replaces H87 and C62. SET stays for real sets. Exceptions (identifier report): tonnage and the half pallet place stay C62, rate of turn E96, TEU capacity 20, persons IE, shares E21. Ballast water TNE becomes MTQ. |
| Q1 | Party-internal codes have no list (see above). |
| Q2 | (a) World copies, each with a listID, of the nine UBL lists that have none and of PackagingType (whose listID has a line break). The world CVA points to the copies. |
| Q3 | (b) Real UNCL 5189 for allowances and UNCL 7161 for charges, bound on ChargeIndicator. Every allowance and charge gets a code. UBL's AllowanceChargeReason list carries 4465 content under a 5189 label: say so in the note, and possibly report it to the OASIS UBL TC. |
| Q3b | Charge codes from UNCL 7161 (FC freight, CAB haulage, ACH heat treatment, DL delivery, AEO disposal, CAT special colour, WH storage, HD terminal handling). Where 7161 has no code, UNCL 5189 is used with its own listID: 96 Insurance (cargo insurance), 48 Interest on arrears (statutory interest on a reminder). The CVA accepts 7161 or 5189 for charges, chosen by listID. The note says how this differs from EN 16931. Allowances: 95 Discount (bundle, repeat order, spring promotion, full container, two-for), 64 Special agreement (moisture, restocking, one day waived, classing fee, included calls), 100 Special rebate (promotion support, goodwill). |
| Q-TM | **Transport means types: UN/ECE Recommendation 28** (code list Revision 4.2, 2018; text Revision 3, 2010; sources in world/codelists/sources/rec28), replacing the regional list. listID `UNECE Recommendation 28`. Container ship 1511; truck carrying containers 37, other trucks with trailer 395; freight barge 815; container train 2302; pipeline 71. **Air:** Rec 28 refers air transport to the IATA SSIM aircraft type codes (Appendix A, not public). Kelaro Air Cargo flies the **ATR 72-600F**, IATA type code **ATF** (ICAO AT72), listID `IATA SSIM Aircraft Types`. ATF is confirmed by OpenTravelData, ACNL's slot allocation lists, avcodes.co.uk and SeatLink. It must be the new-built 600F: it carries 7 LD3 (incl. the RKN active container), 9,200 kg payload, 75 m³, door 2.94 × 1.80 m (ATR fact sheet; earlier written 2.95). A freighter is needed anyway for the CAO lithium batteries. The fleet description in parties.json says so. Stage 5: a build check that each air leg stays within the aircraft's payload, volume and ULD positions, and the DG segregation in the mixed ULD (classes 9, 7 excepted, 8) checked against secondary sources. |
| P2 | UNDGCode: listID `UN Model Regulations Dangerous Goods List` (the UN Recommendations on the Transport of Dangerous Goods, where the UN numbers are assigned), not `UN/EDIFACT EDED 7124`, which only names the data element. Secondary sources (BAM DGG-Info) are used, since the UNECE publication is blocked. A build check makes UN number, proper shipping name and class agree per item. |
| P3 | DocumentDistribution: DocumentTypeCode = the type of the distributed document (UBL document type list); DistributionTypeCode = how the party receives it, from a regional list following UBL's examples ("Collect", "Sent by courier", "Sent scanned copy"): ORIGINALCOURIER, SCANNEDCOPY, ELECTRONIC, COLLECT …. The DocumentCopyType list goes. Reason: UBL 2.5 deprecated CopyIndicator, MaximumCopiesNumeric, MaximumOriginalsNumeric and PrintQualifier ("No consensus of real use cases for this."), and original/copy is not a type of document (7.2). |
| P-SB | **Self-billing** uses only SelfBilledInvoice and SelfBilledCreditNote, never an Invoice with 389.
- **Why:** UBL 2.5 defines Invoice as "A document used to request payment" and SelfBilledInvoice as "An Invoice document created by the Customer (rather than the Supplier) in a Self Billing relationship"; §4.7 and §7.2 on semantic conformance.
- **Type code (option c):** 386 prepayment where there is a real self-billed advance (cotton: a self-billed advance to the farm before the final settlement, added in stage 5). Otherwise 389 (SelfBilledInvoice) and 261 (SelfBilledCreditNote). They repeat the root, but their UNCL 1001 definitions are exact ("An invoice the invoicee is producing instead of the seller"; "… claiming credit in a self billing environment"). 380 would be wrong ("claiming payment").
- **The note** explains both points. Coverage is unaffected. |
| P5 | The CPC codes were checked against UNSD's official HS 2017 → CPC 2.1 correspondence (world/codelists/sources/cpc/CPC21-HS2017.csv). Confirmed: 7325.99 → **42999** "Metal goods n.e.c." (bench casting); 3814.00 → **35110** "Paints and varnishes and related products" (coating stripper: UNSD maps paint removers to this class); 9401.79 → 38111; 9401.69 → 38112. Build check (implemented in the correction pass, d9001cd): each item's CPC must be the CPC the correspondence gives for its HS subheading. The correspondence is HS 2017 and the world uses HS 2022, so changed subheadings must be checked by hand. |
| P6 | (b) The text partner of a code (RejectReason next to RejectReasonCode, and so on) gives the code's meaning from the list, **plus the specific detail of the case where there is any**, e.g. "Damaged in transit: one bench arrived in a damaged carton and was refused." or "Estimated: no access to the meter". The plain list name only where nothing specific applies, bilingual where the sender's country is (IND7/IND8). Restore the details lost in stage 3 (from the examples before commit 84155d7). |
| P7 | Accepted.
- PaymentPurposeCode: TRPT (ISO 20022 "road pricing") → SCVE for the return transport; GOVT → SCVE for the public body's payment to its supplier. The purpose is what the payment is for. Checked against ISO 20022 External Code Sets 2Q2026.
- ActionCode `Trade` is removed from the item TransactionConditions, because it named whom the conditions apply to, not an action.
- Open suggestion: GOVT where a payment really goes to the government, e.g. Bayvarra's 10 % withholding paid to the state. |
| Q4 | (a) External lists in UBL text style (`UN/EDIFACT EDED nnnn`, `ISO 20022 <name>`, `WCO HS 2022`, `ISIC Rev.4`). The world's lists use URNs: `urn:ubl-examples:world:codelist:<Name>Code`, and national ones `urn:ubl-examples:world:<CC>:codelist:<Name>Code`. schemeID follows the same rule. |
| Q5 | No version attribute, because listVersionID is deprecated in UBL 2.5. The edition goes in the listID only where it is part of the standard's name (`WCO HS 2022`, `ISIC Rev.4`). Otherwise the version is in the genericode file only. |
| Q6 | (a) One list per concept, with plausible extra codes where the concept has room for them. Qualified variants of one concept share its list: Previous/Latest MeterReadingMethod, (Previous)CancellationReason, (Current)ChargeType, (Current)OperatingSecurityLevel, (Required)ResponseMessageLevel, (Required)Curricula, (Applicable)Category. The listID is the concept's name. |
| Q7 | PackagingDangerLevel "no packing group", InhalationToxicityZone "not toxic by inhalation" and SecurityClearance "not required" get defined codes. EmergencyProceduresCode `None` belongs to UN 2911 (radioactive, excepted package) and gets its real EmS (F-I, S-S; verify). The F-E on SecondaryHazard is removed, because an EmS belongs to the UN entry. The mast flow already has UN 2920 in packing group II, so PackagingDangerLevelCode `2` can cover that element without a new scenario. CompanyLegalFormCode `Any` is removed and said in the tender text instead. PreviousCancellationReasonCode and Prize are removed and come back through real scenarios: a relaunched tender and a design contest. |
| Q8 | (a) TimeBasisCode uses UN/ECE Rec 20 (ANN). CalculationMethodCode gets a regional list. |
| Q9 | **Revised** (the earlier "for now" choice of UNCL 1001 for all document types). A TypeCode should give a real subtype, not repeat the root element.
- **UNCL 1001 stays** where established practice uses it: InvoiceTypeCode (380, 389, plus real subtypes in the examples such as 386 prepayment and 384 corrected), CreditNoteTypeCode (381, 261), DebitNoteTypeCode (383), OrderTypeCode (220, 230, 227 …).
- **WaybillTypeCode:** a regional list of waybill types by legal regime (road/CMR, rail/CIM, air, inland waterway/CMNI), with 1001 codes (730, 720, 740, 700) mapped in the descriptions.
- **DespatchAdviceTypeCode:** a regional list of real subtypes (delivery, return, cross-dock, partial, complete …) instead of 351. |
| Q11 | (a) Each element keeps its own source. UNPackingGroupCode uses a world list based on the UN Model Regulations (I/II/III, plus NA for "no packing group assigned"). PackagingDangerLevelCode uses UNCL 8339 (1/2/3, and **4 "Not assigned"** for goods without a packing group, e.g. the lithium batteries; verified 2026-11-11). The build checks that the two agree: I↔1, II↔2, III↔3, NA↔4. |
| Q12 | (b) EmS pairs are written `F-A,S-I`: the IMDG form without the space. They come from a world list of the pairs used plus extras, with listID `IMO IMDG EmS`. Hyphens in external codes are allowed where the standard writes them. |
| Q13 | (a) MedicalFirstAidGuideCode keeps the ERG guide numbers (147, 161, 132), with listID `ERG 2024`. The `.md` explanations say that the guide used is the ERG. To verify: that the IMDG Code no longer gives MFAG table numbers per UN number. |
| Q14 | (a) CoordinateSystemCode `4326`, listID `EPSG` (WGS 84 geographic), replacing `WGS84`. The platform's grid reference is part of the identifier questions. |
| Q15 | (a) AddressFormatCode: a regional list with one code per country format (XU/XB/XL). The full layout of each format is its description. The address fix itself runs separately (see the work items). |
| Q16 | (a) Both regional. EntitySizeCode gets a Trade Accord definition with thresholds in the style of the EU SME definition (headcount plus turnover, the limits given in all three currencies and their minor units). Parties get headcount and turnover, and the size class follows from them. MeterReadingMethod gets one regional list, with extra codes such as SMART and PROFILE. |
| Q17 | (b) MarketCode becomes a 4-character code shaped like ISO 10383 (e.g. `XFER` for the Ferrano Stock Exchange). It is checked against the published MIC list, as the currencies are against ISO 4217, with a stored copy for `--check`. listID: world URN. Fix the ISIN check digit in the same pass. |
| Q18 | (2) PaymentChannelCode uses ISO 20022 **ClearingChannel2Code** (RTGS, RTNS, MPNS, BOOK), listID `ISO 20022 ClearingChannel2Code`. It is paired with the rail in PaymentRailID: FERRA-RTGS → RTGS; LUMEPAY → MPNS (batch) or RTNS (instant); TRADE-ACCORD-PAY → RTNS; CORAL-NET → RTGS. ServiceLevelCode must agree, and the build checks the pairing. The 38 `IBAN` values go, because the account format is already in AccountFormatCode. PaymentRailID gets a world list of rails, modelled on ISO 20022 ExternalCashClearingSystem1Code. Reasons: UBL aims to stay compatible with ISO 20022; EN 16931 excludes the element (UBL-CR-413); UNCL 4435 doesn't fit (no RTGS code, mostly ways of sending). Research: scratchpad q18-payment-channel.md (2026-11-11). |
| Q19 | (b) FormatCode uses PRONOM PUIDs (listID `PRONOM`). The registry's slash is allowed. The build checks that FormatCode agrees with MimeCode. To verify: the PUIDs for PDF/A-3. |
| Q20 | (b) PriceTypeCode uses a regional Trade Accord list (TRD trade price, RRP recommended retail price, CAT catalogue price, CON contract price, …). The buyer must understand it, so it is not the seller's own code (Q1). The tender catalogue uses CON. |
| Q21 | (b) LifecycleStageCode uses a regional list with the UBL definition's stages (SOURCING, MANUFACTURING, DISTRIBUTION, USAGE, ENDOFLIFE, maybe RECOVERY). Each description names the matching EN 15804 modules. FullnessIndicationCode gets a consistent separate list (CRADLETOGATE …). The footprint's standard names the real one (e.g. ISO 14067). |
| Q22 | (c) SealIssuerTypeCode uses a regional list: SHIPPER, CARRIER, CUSTOMS, VETERINARY (mapped to DCSA SHI, CAR, CUS, VET, eBL 3.0.3) and PHYTOSANITARY (no DCSA equivalent in eBL 3.0). Each description also maps to UNCL 9303. OwnerTypeCode, ProviderTypeCode and SealIssuerTypeCode get separate lists. SealStatusCode gets a regional list, treated the same way. |
| Q23 | (a) TransportEmergencyCardCode uses a regional list of the Accord's emergency cards, one per hazard class (TEC1 … TEC9, plus a general card), following ADR's class-based instructions in writing. `TEC-90-3480` becomes `TEC9`. The build checks that the card matches HazardClassID. HazardousCategoryCode `UN` becomes the class. |
| Q24 | (a) One Trade Accord customs data model, with shared regional lists for procedures, statuses, declaration types and subtypes, export reasons and types, nature of transaction (mapped to the UN/EU statistics list), transit direction and location types. The Accord is a free trade area, not a customs union, so tariffs, rates and exemptions stay national. CustomsStatus means "not in free circulation in the declaring territory". CustomsProcedureCode gets **new Accord codes**, not the EU's: the Accord's own structure, with the requested procedure followed by the previous one. Proposed: a 2-digit requested procedure plus a 2-digit previous procedure, numbered differently from the EU (10 release for free circulation, 20 temporary admission, 30 export, 35 re-export, 40 transit, 50 customs warehousing; 00 = no previous procedure). So `4000` becomes `1000`. The full list follows in the list review. |
| Q25 | (b) Procurement uses regional Trade Accord lists modelled on eForms/ESPD-EDM, with the eForms/ESPD code mapped in the descriptions (procedure types incl. RESTRICTED, NEGOTIATED, DESIGNCONTEST; response data types; property group types; cancellation reasons …). The note: the Accord's procurement rules are modelled on the EU's, without being EU law. |
| Q26 | Settled by Q6: one list per element (RetailTactic …). |
| Q27 | (b) CountrySubentityCode in ISO 3166-2 style: `XB-CO`, `XB-UL`, `XB-NT`. A national list `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`, structured like ISO but not ISO 3166-2 itself. Third subdivision: the Northern Territory (north coast, Gullhaven, the gas plant), a federal territory with its own sales tax rate. Done along with it: the river made a real river, the south-western border following the river, and the sawmill moved to the north bank (sub-agent). |
| Q28 | (a) Tax exemption reasons use national lists without the country prefix. XB: EXP, RESALE, PUBLIC, SVCB2B, WATER, LEVY. XU: EXP, SVCABROAD. Plus extras, with a national listID. ExemptionReasonCode on PartyTaxScheme uses the same XB list. The Northern Territory uses the XB list. The build checks that the list matches the seller's country. The reason text is bilingual for XU. |
| Q29 | DocumentTypeCode, depending on what is referred to:
- **external, non-UBL documents:** UNCL 1001 where an exact code exists (774 general terms and conditions, certificates …);
- **generic references to UBL documents:** a list of the UBL document type names (Order, Invoice …);
- **the rest:** a regional list (TARIFF, RETURNNOTICE; 1001 239 "Rejected direct debit(s)" is close but means a reject, not a return).

Leave the element out where the reference element already says the type (OrderReference, DespatchDocumentReference …). Each value carries its own listID. |
| Q30 | (a) InvoicePeriod/DescriptionCode uses a regional PeriodDescription list (MONTH, QUARTER, HALFYEAR, YEAR, WEEK …), following the UBL definition. EN 16931's use of this element for the VAT point date code (BT-8, UNCL 2005) is considered semantically incorrect. A tax point date belongs in TaxPointDate. |
| Q10 | (a) Follow the UBL definitions: HS 6-digit and the national tariff go in CommodityCode, as two CommodityClassification entries, each with its listID. ItemClassificationCode gets UN CPC Ver.2.1, for goods and services. PARKS-FURN becomes a CPC code. Consignment/TariffCode is the carrier's freight tariff item, with no list (Q1). |

## Stage 5 (real scenarios for the last elements)

- **Design contest** (flow `contest`): DESIGNCONTEST, prizes (FIRST/SECOND/THIRD), a relaunch after a cancelled contest (PreviousCancellationReasonCode UNSUITABLE), a legal form for groups before the follow-up contract (CompanyLegalFormCode LTD). Eight document types revised: version 2 with PreviousVersionID 1, same number, new UUID.
- **ExchangeMarketID**: XLMX, the Lumeport Exchange's noon fixing, which the tender's contract names; bound to the Market list in schemeID.
- **Cards**: a webshop order with full PAN, dates and CV2 (Tressa credit card of the consumer); Velumi Trading's island shop masks first 6 + last 4 (Coralcard of the cotton farm).
- **Self-billed prepayment**: cotton SelfBilledInvoice 386, deducted in the final self-billed invoice.
- **Air**: capacity and DG stowage check (sources/atr, sources/iata-dgr). SecondaryHazard/EmergencyProceduresCode: the IMDG Code has no EmS per subsidiary hazard, so the Accord's class card of the subsidiary hazard (TEC3), following ADR's instructions in writing per label.
- **Fillers removed**: masked passwords (WebSiteAccess stays only with a real one-time password or reading code), ISSCAbsenceReason, AdditionalMattersDescription and the "no activity" ship-to-ship record in sea/16 (replaced by a real bunkering). The absence reason and additional matters come back in the second feeder's report (interim ISSC; a stowaway search). The sanitation exemption certificate is that ship's.
- **GRAI**: Lumeway's returnable pallets in the retail despatch advice.
- **GOVT**: not used. No document of the world pays Bayvarra's withholding to the state, and the state has no party to receive one.

## Identifier decisions

| ID-Q | Decision |
|---|---|
| 11 | The exceptions to EA are accepted: tonnage and the half pallet place stay C62, persons IE, shares E21, TEU capacity 20, rate of turn E96. Ballast water VolumeMeasure TNE becomes MTQ. All of these are in UBL's UnitOfMeasure-2.4. |
| 10b | **Payment cards.**
- **Masking (PCI DSS):** at most the BIN plus the last 4, varying per merchant within that maximum. Brightmarket shows the last 4; the island shop the first 6 + last 4; first 8 + last 4 is allowed for 8-digit BINs (verify).
- **What goes where:** receipts carry no CV2 and no expiry date. CV2ID, ExpiryDate and ValidityStartDate move to a new pre-authorisation scenario (e.g. a webshop order paid by card), with a full world test PAN.
- **Fictional numbers:** card numbers use ISO/IEC 7812 MII 9 + the ISO 3166 user-assigned numeric code (9 901 XU, 9 902 XB, 9 903 XL) plus issuer digits and a Luhn check digit. The chip AID uses the ISO/IEC 7816-5 national category `D` + 9xx. Verify both rules.
- **Card schemes:** LUMECARD (Bayvarran banks' domestic debit, like Interac or Girocard), CORALCARD (the island's, on the coral ledger) and a new Accord-wide international credit scheme (fictional name; no real network names). Cards may be co-badged.
- NetworkID gets a regional list. IssuerID becomes the BIC-like bank code (ID-Q9). The note gets a paragraph on cards. |
| 10 | A mix of two ways to identify the issuer of a certificate or licence:
- **schemeID**, which names the issuer implicitly: for numbers from a national register of licences or registrations, such as the XU haulage licence, the XB forestry registration and the bonded warehouse permit (e.g. `…:XU:haulage-licence`). The scheme stands for the authority's register, so no IssuerParty is needed.
- **IssuerParty, without a schemeID:** for certificates whose number is only unique within the issuer, such as environmental, test, medical and sanitation certificates, the ship security certificate and digital (X.509) certificates (the issuer is the CA).

Fix along the way: `XB-FOR-2025-118` against its reference `XB-FOR-REG-0118` (align them, or explain them as two numbers), and `ACCORD-CERT-1-xl`, which has an internal party ID in the value. |
| 9 | (c) Both layers, as in reality. FinancialInstitution/ID gets a BIC-like Accord-wide code (ISO 9362 structure with the world's country codes, e.g. `BLUMXBLX`, scheme `urn:ubl-examples:world:bank-identifier`, issued under the Trade Accord's payment link). FinancialInstitutionBranch/ID gets the national branch code in each country's style: XB a British-style sort code (6 digits), XU Italian-style ABI/CAB (5 + 5 digits), XL a 3-digit branch number, each with a national scheme. The account numbers (ISO 13616 structure) must contain the matching bank or branch code, which the build checks; regenerate them if needed. Each bank gets a few branches. |
| 8 | Address registers at the level that fits each country:
- **XU:** one national register (BAG-like, about 16 digits: municipality code + serial), `…:XU:address-register`.
- **XB:** state registers (`…:XB:CO:address-register`, UL, NT), plus the Lumeport city register `…:XB:lumeport:address-register` for addresses inside the city (`LUM-ADR-000417`).
- **XL:** the post office's delivery point numbers (no postcodes; PostNL/UDPRN-like), `…:XL:delivery-point`.

Address/ID is 0..1, so each address gets the one register that applies. IDs go only where they make sense: party postal addresses and delivery addresses, not item origins or bank branches. Formats go in countries.json and are checked, including that the register matches the address's state or city. |
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

## Document identification (UBLVersionID, CustomizationID, ProfileID)

- **UBLVersionID:** the earliest UBL 2 version that defines every element in the document ("Identifies the earliest version of the UBL 2 schema for this document type that defines all of the elements that might be encountered in the current instance"). The build computes it from the version history; it is not always 2.5.
- **Transaction:** one kind of business message between two roles, with a defined purpose, information content and rules, as in CEN BII and Peppol. One or more document types carry a transaction (billing = Invoice + CreditNote (+ DebitNote); self-billing = SelfBilledInvoice + SelfBilledCreditNote; order-status = DocumentStatusRequest + DocumentStatus). One document type can carry several transactions (ApplicationResponse: invoice-response vs message-level response). Mostly it is one transaction per document type.
- **CustomizationID** names the transaction specification, versioned, at three levels chained with `#compliant#` (the EN 16931 / Peppol / XRechnung convention):
  1. **cross-country**, owned by the Trade Accord: `urn:ubl-examples:world:trns:<transaction>:1.0`;
  2. **national**, owned by a country's authority: e.g. `urn:ubl-examples:world:XU:invoice:1.0` (Urvania's EU-style VAT rules), Bayvarra's rules for public bodies (withholding);
  3. **community**, a group of parties exchanging among themselves: the retail community (Lumeway ↔ Brightmarket, GS1), the Lumeport port community (sea and customs), Urvania's energy market (power station, grid operator, retailer), public procurement (tender documents); e.g. `urn:ubl-examples:world:community:retail:1.0`.

  Example: `urn:ubl-examples:world:trns:invoice:1.0#compliant#urn:ubl-examples:world:XU:invoice:1.0#compliant#urn:ubl-examples:world:community:energy-xu:1.0`. The world does not claim EN 16931 compliance. Each specification gets a short public description page on the site. The world's code-list rules can be tied to the specification a document claims.
- **ProfileID:** generic Accord process profiles, versioned (`…:profile:ordering:1.0`, billing, despatch-receipt, transport, tendering, customs, catalogue, utility-billing …). It no longer names a flow.
- **ProfileExecutionID:** stays one per flow instance.

## Fictional values (verified as free, 2026-11-11)

| What | Value | Evidence |
|---|---|---|
| GS1 prefix (GTIN, GLN, SSCC of the GS1-convention parties) | 952 | GS1 General Specifications reserve it "for demonstrations and examples" |
| ITU call sign series and aircraft nationality marks | QU (XU), QB (XB), QL (XL) | no Q series is allocated (ITU table) |
| MMSI MIDs | 297 (XU), 298 (XB), 299 (XL) | unallocated in the ITU MID table |
| UIC wagon country codes | 46, 47, 48 | not in OTIF's table |
| ISO 6523 ICD (Codana organisation identifier) | 0990 | Peppol's ICD list ends at 0248 |
| ISO 15459 issuing agency code (Codana) | KXU | K is reserved for national public administrations + ISO 3166 alpha-2; XU is user-assigned, so no real agency can hold it. **Codana becomes Urvania's public numbering body.** |
| World MIC | 4-character code checked against the saved ISO 10383 list (649 real MICs start with X; XCOR and XBRM are real) | ISO10383_MIC.csv |
| Card numbers / chip RID | MII 9 + 901/902/903; RID D9xx | secondary sources (the ISO texts are paywalled) |
| Currencies | XUF, XBL, XLC free; avoid XUA, XCG, XAD (real) | SIX list-one.xml |

The evidence files are in the verification sources (to be committed with the code lists in stage 3).

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
- **EN 16931 and self-billing.** EN 16931 and Peppol BIS send a self-billed invoice as an `Invoice` with type 389, because their syntax binding has only Invoice and CreditNote. Under UBL 2.5 §4.7 and §7.2 this conflicts with the semantic definitions: Invoice is "A document used to request payment", while SelfBilledInvoice is "An Invoice document created by the Customer (rather than the Supplier)". UBL 1001 code 380 is also "claiming payment". This finding goes with the ItemClassificationCode and InvoicePeriod/DescriptionCode findings, to raise when EN 16931 moves to UBL 2.5 (OASIS UBL TC, CEN/TC 434).
- Q31: codes not yet checked against the published lists. UNCL 1001 351/711/720/730/740, 5189/7161 choices, UN CPC Ver.2.1 codes, plus the ones the classification marks "verify". unece.org blocked this environment on 2026-11-11.
