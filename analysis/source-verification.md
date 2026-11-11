# Source verification (Q31 and "For future research")

All sources were accessed on **2026-11-11**. The machine-readable lists the world's code lists are built from are copied, with their SHA-256, in `world/codelists/sources/` (see its PROVENANCE.md). Other evidence (standards texts, PDFs, web pages) is cited here by URL and quoted text but not copied, because it is copyrighted or large.

Verdicts: **confirmed** · **differs** (the source says something other than the decision or classification assumed) · **not verifiable** (no reachable authoritative text).

Sources referred to below:

| Short name | What | URL / location | Version |
|---|---|---|---|
| CEFACT | UN/CEFACT vocabulary JSON code lists | github.com/uncefact/vocabulary-outputs `_data/*codelist.json`, main @ 51768f9 (2024-07-29); `_config.yml` says `dataSet: '22A'`. Copies: `sources/uncefact-vocabulary-outputs/` | D.22A-based, names only (no descriptions) |
| PEPPOL-BIL | Peppol BIS Billing 3.0 code lists | git clone github.com/OpenPEPPOL/peppol-bis-invoice-3 @ 38d693d (2026-11-04), `structure/codelist/` → `sources/peppol-bis-invoice-3/` | UNCL lists D.16B (7161 with later additions) |
| PEPPOL-UP3 | Peppol BIS 3 (post-award) code lists | git clone github.com/OpenPEPPOL/poacc-upgrade-3 @ c3bd29f (2025-11-20) → `sources/poacc-upgrade-3/` | UNCL1001 full D.17A, 8273 D.23A, 6313/4343 subsets D.17A |

unece.org, service.unece.org, iso.org (Cloudflare), the iso20022.org external code sets, phmsa.dot.gov, the gs1.org web pages and github.com web pages (not git) returned 403.

---

## 1. UNCL 1001 (document name code)

Quotations are from CEFACT `documentcodelist.json` ("[Reference United Nations Code List (UNCL) 1001]"). Descriptions are from PEPPOL-UP3 `UNCL1001.xml` (D.17A full list).

| Code | Quoted text | Verdict |
|---|---|---|
| 351 | "Despatch advice" — "Document/message by means of which the seller or consignor informs the consignee about the despatch of goods." | confirmed |
| 380 | "Commercial invoice" — "Document/message claiming payment for goods or services supplied under conditions agreed between seller and buyer." | confirmed |
| 381 | "Credit note" — "Document/message for providing credit information to the relevant party." | confirmed |
| 383 | "Debit note" | confirmed |
| 389 | "Self-billed invoice" — "An invoice the invoicee is producing instead of the seller." | confirmed |
| 261 | "Self billed credit note" — "A document which indicates that the customer is claiming credit in a self billing environment." | confirmed. It is not in the Peppol/EN 16931 credit-note subset (`UNCL1001-cn.xml`), which is irrelevant here. |
| 220 | "Order" | confirmed |
| 230 | "Purchase order change request" — "Change to an purchase order already sent." | confirmed |
| 481 | "Remittance advice" — "Document/message advising of the remittance of payment." | confirmed |
| 711 | "Inland waterway bill of lading" — "Negotiable transport document made out to a named person, to order or to bearer, signed by the carrier and handed to the sender after receipt of the goods." | confirmed as a code, **but doubtful for CMNI**. 711 is a *negotiable* bill of lading. 1001 has no inland-waterway consignment note or waybill: the only matches for inland/waterway/barge/river are 109, 111, 126 (equipment reports) and 711. If the world's barge document is a non-negotiable consignment note, there is no exact 1001 code. Keep 711 only if the document is meant as a (negotiable) B/L; otherwise 760 "Multimodal/combined transport document (generic)" is no better. Recommend 711 with a note, or a regional code. |
| 720 | "Rail consignment note (generic term)" — "Transport document constituting a contract for the carriage of goods between the sender and the carrier (the railway). For international rail traffic, this document must conform to the model prescribed by the international conventions concerning carriage of goods by rail, e.g. CIM Convention, S[MGS] …" | confirmed |
| 730 | "Road consignment note" — "Transport document/message which evidences a contract between a carrier and a sender for the carriage of goods by road (generic term). Remark: For international road traffic, this document must contain at least the particulars prescribed by the convention on the contract for the international carriage of good[s by road (CMR)]" | confirmed |
| 740 | "Air waybill" — "Document/message made out by or on behalf of the shipper which evidences the contract between the shipper and carrier(s) for carriage of goods over routes of the carrier(s) and which is identified by the airline prefix issuing the document plus a serial (IATA)." | confirmed |

**Q29: exact 1001 matches for the regional words**

- **Terms** (sea/03 DigitalAgreement → `/DigitalAgreement/DigitalAgreementTerms`): CEFACT has **774 "General terms and conditions"** (also 776 "Contract clauses" and 777 "Specific contract conditions"). These are newer than D.17A (not in PEPPOL-UP3), so no description is available. **Exact match: 774.** The regional TERMS code is not needed.
- **Tariff** (utilities: "Prices per unit and the terms of supply"): **no exact code.** Nothing in 1001 contains "tariff". The nearest is 9 "Price/sales catalogue": "A document/message to enable the transmission of information regarding pricing and catalogue details for goods and services offered by a seller to a buyer." (728 "…containing commercial information" means "only commercial terms or conditions data".) Recommend keeping the regional TARIFF, or using 9 if a near fit is acceptable.
- **ReturnNotice** (utilities/10: "Direct debit returned: insufficient funds", issued by the bank): **no exact code.** The goods-return codes 729/732/733 do not fit. Nearest: 239 "Rejected direct debit(s)" — "The message contains rejected direct debit(s)"; 457 "Reversal of debit" — "Reversal of debit accounting entry by bank." Recommend the regional RETURNNOTICE, or 239.
- Also in Q31: CMNI → see 711 above.

## 2. UNCL 5189 and UNCL 7161; proposed codes

**Which list is which**

- CEFACT `allowancechargeidcodelist.json` ("AllowanceChargeIdCodeList") is the **full UNCL 5189** (106 codes: 1 Handling commission … 41 Bonus for works ahead of schedule … 48 Interest on arrears … 79 Freight charges … 85 Warehousing charge … 95 Discount, 96 Insurance … 100 Special rebate … 104 Standard, 105 Yearly turnover, 106 Withheld taxes and social security contributions). It holds charge codes as well as allowance codes.
- `allowancechargereasoncodelist.json` ("AllowanceChargeReasonCodeList", 1 Agreed settlement … 95 Small order processing service charge …) is **UNCL 4465**.
- The **EN 16931 allowance subset** of 5189 (PEPPOL-BIL `UNCL5189.xml`, "Allowance reason codes (UNCL5189 subset)", D.16B) has 19 codes: 41, 42, 60, 62, 63, 64, 65, 66, 67, 68, 70, 71, 88, 95, 100, 102, 103, 104, 105. It gives names only.
- **UNCL 7161 is not in CEFACT.** It is taken from PEPPOL-BIL `UNCL7161.xml` ("Charge reason code (UNCL7161)", D.16B plus the later codes CAX–CAZ, DAC, DAF–DAQ and PRV; 178 codes, with descriptions). The full dump is in the evidence.
- **Verdict: confirmed**, and consistent with the Q3 note.

**Finding.** 7161 has **no code for insurance and none for interest.** The only matches are CAP "Insurance brokerage service" and AEN "Guarantee". Exact codes exist only in full 5189: 96 "Insurance" and 48 "Interest on arrears". Under Q3's strict binding (7161 for every charge), those two charges get a 7161 fallback. Decide either to allow the full 5189 for charges where 7161 has no code, or to use the fallback.

**Allowances (ChargeIndicator false → 5189, EN 16931 subset)**

| Example (file) | Context | Proposal | Quoted name | Fit |
|---|---|---|---|---|
| Business bundle discount (utilities/12, 13) | 5 % bundle discount | **95** | "Discount" | generic. 5189 has no bundle code. |
| Repeat order (furniture/10) | "The quotation gives 3 % on a repeat order" | **95** (alt. 64) | "Discount" / "Special agreement" | generic |
| Moisture deduction (ore/07) | contract deducts 1.5 % for moisture above 6 % | **64** | "Special agreement" | nearest. 4465's "2 Below specification goods" is not 5189. |
| Restocking deduction (furniture/13 CreditNote, 14 DebitNote) | "The instruction for returns lets the furniture maker keep 5 %" | **64** | "Special agreement" | nearest. 7161 RAF "Restocking — The service of restocking." is exact, but it is a charge code. |
| Promotion support (retail/08, 18, 19) | supplier funds the store's promotion | **100** (alt. 60) | "Special rebate" / "Manufacturer's consumer discount" | nearest. 7161's DAH "Allowance transferable to the consumer" and DAK "Multi-buy promotion" are 7161 codes. |
| Spring garden promotion (retail/21 receipt, price discount) | till promotion 10 % | **95** | "Discount" | generic |
| Full container / volume (retail/02, sea/02) | discount for a full container | **95** (alt. 104 "Standard") | "Discount" | generic. 5189 has no volume code. |
| Goodwill (tender/33, amount 0.00) | for the inconvenience | **100** | "Special rebate" | nearest |
| One day waived (tender/34) | one day of a penalty waived "as both agree" | **64** | "Special agreement" | good |
| Two-for discount (packaging/08: "Two shirts: 5.00 off the pair") | multi-buy | **95** | "Discount" | generic (7161 DAK is the exact concept but is a 7161 code) |
| *Also found:* Classing fee (cotton/04, ChargeIndicator false) | farm bears the fee "as the agreement says" | **64** | "Special agreement" | nearest |
| *Also found:* Calls included in subscription (utilities/12) | 100 % allowance | **64** | "Special agreement" | nearest |

**Charges (ChargeIndicator true → 7161)**

| Example (file) | Proposal | Quoted (PEPPOL-BIL UNCL7161) | Fit |
|---|---|---|---|
| Cargo insurance (sea/22, 25) | **no 7161 code** → ABK, or 5189 **96** | ABK "Miscellaneous — Miscellaneous services."; 5189 96 "Insurance" | 7161 does not cover it |
| Freight and insurance of the CIF invoice (sea/25) | **FC** | "Freight service — The service of moving goods, by whatever means, from one place to another." | partial (freight part) |
| Sea freight (sea/22, 25) | **FC** | as above | exact |
| Haulage (cotton/03 "Haulage allowance", ChargeIndicator **true**: the gin pays the farm for bringing the cotton) | **CAB** | "Cartage — Movement of goods by heavy duty cart or vehicle." | good. Its name says "allowance" while it is a charge on the self-billed invoice: check the wording. |
| Heat-treated export pallets (wood/02, 03, 08; ISPM 15) | **ACH** (alt. PL) | "Heat treatment — The service of treating with heat."; PL "Palletizing — The service of palletizing." | good |
| Home delivery (retail/21) | **DL** | "Delivery — The service of providing delivery." | exact |
| Packaging disposal (furniture/16, 17) | **AEO** (alt. AEV) | "Collection and recycling — The service of collection and recycling products."; AEV "Environmental protection service" | good |
| Special colour (tender/27, 28, 32) | **CAT** | "Special colour service — Providing a colour which is different from the default colour." | exact |
| Statutory interest (tender/35 Reminder) | **no 7161 code** → ZZZ/ABK, or 5189 **48** | 5189 48 "Interest on arrears"; ZZZ "Mutually defined" | 7161 does not cover it |
| Storage while held (sea/28) | **WH** | "Warehousing — The service of storing and handling of goods in a warehouse." | good |
| Terminal handling (sea/14, under DeliveryTerms) | **HD** (alt. SAA) | "Handling — Handling service."; SAA "Shipping and handling" | good |

## 3. Other UNCL lists

| List | Source and quoted content | Verdict |
|---|---|---|
| **8339** packaging danger level | CEFACT DangerousGoodsPackagingLevelCodeList: "1 Great danger · 2 Medium danger · 3 Minor danger · **4 Not assigned**" | confirmed 1/2/3. **New:** code 4 "Not assigned" exists. That is a defined "no packing group" code for PackagingDangerLevelCode, so Q11's "left out when there is no packing group" (and Q7's no-filler rule) can use 4 instead. The build mapping becomes I↔1, II↔2, III↔3, NA↔4. |
| **4435** payment channel | CEFACT PaymentMeansChannelCodeList: 1 Ordinary post, 2 Air mail, 3 Telegraph, 4 Telex, 5 S.W.I.F.T., 6 Other transmission networks, 7 Networks not defined, 8 Fedwire, 9 Personal (face-to-face), 10 Registered air mail, 11 Registered mail, 12 Courier, 13 Messenger, 14 National ACH, 15 Other ACH, ZZZ Mutually defined | confirmed (16 codes). For Q18: it names the channel *kind* (ACH, SWIFT, Fedwire), not the system or the account format, so `IBAN` is wrong. National ACH (14) plus PaymentRailID naming the system do not duplicate each other. |
| **5305** tax category | CEFACT TaxCategoryCodeList: S "Standard rate", E "Exempt from tax", G "Free export item, tax not charged", O "Services outside scope of tax", Z "Zero rated goods", AE "VAT Reverse Charge", K "VAT exempt for EEA intra-community supply of goods and services", L "Canary Islands general indirect tax", M "Tax for production, services and importation in Ceuta and Melilla". PEPPOL-BIL subset descriptions, e.g. E "Code specifying that taxes are not applicable.", G "…the item is free export and taxes are not charged." | confirmed. K, L and M are EU/Spain-specific: do not use them in the world unless the scenario needs that meaning. |
| **5153** duty/tax/fee type | CEFACT TaxTypeCodeList: VAT "Value added tax", STT "State/provincial sales tax", CUD "Customs duty", IMP "Import tax", EXC "Excise duty", OTH "Other taxes" (also GST, LOC, ENV, FRE …) | confirmed |
| **7124** UN number | Not a coded list in CEFACT. Its property `uNDGIdentificationCode` has range `xsd:string`: "The code specifying the unique United Nations Dangerous Goods (UNDG) number assigned to these transported dangerous goods." | not verifiable as "7124" (the UNTDID page is blocked). The concept is confirmed: the UN number is a free 4-digit value, not a code list. Keep listID `UN/EDIFACT EDED 7124` or switch to "UN Model Regulations"; either way `UNCL8273` on UNDGCode is wrong. |
| **8273** DG regulations | CEFACT: "ICA IATA ICAO". PEPPOL-UP3 (D.23A): ICA — "Regulations covering the international transportation of dangerous goods issued by the International Air Transport Association and the International Civil Aviation Organization." Also IMD "IMO IMDG code", ADR, RID | **confirmed: ICA = IATA/ICAO** |
| **4343** response type | CEFACT ResponseTypeCodeList (27 codes): AP "Accepted", CA "Conditionally accepted", RE "Rejected", AB "Message acknowledgement" … PEPPOL-UP3 D.17A invoice-response subset also has IP "In process", UQ "Under query", PD "Paid", which are **missing** from CEFACT 22A (the CEFACT copy looks incomplete). | AP and CA confirmed. **CN is not a 4343 code** (absent from both sources). That matches the classification (ResponseCode CN → discrepancy list, not 4343). |
| **6313** measured attribute | CEFACT MeasuredAttributeCodeList: LN "Length", WD "Width dimension", HT "Height dimension", DP "Depth", TH "Thickness", DI "Diameter", ID/OD inside/outside diameter, LM/WM/HM maxima, AEA "Loading height", AEB "Stacking height". 6313 has **no seat-height, bench-length or slot code**. | confirmed. The dimension list maps LENGTH→LN, WIDTH→WD, HEIGHT→HT, DEPTH→DP, THICKNESS→TH, LOADINGLENGTH→(none; nearest LN), SEATHEIGHT→(none; HT), BENCHLENGTH→(none; LN), SLOT→(none). |
| **9303** sealing party | CEFACT SealingPartyRoleCodeList: AA Consolidator, AB Unknown, AC Quarantine agency, CA Carrier, CU Customs, SH Shipper, TO Terminal operator | confirmed. There is no veterinary or phytosanitary code (only AC quarantine agency). |
| **4461** payment means | PEPPOL-BIL UNCL4461 (D.16B): 10 "In cash", 30 "Credit transfer", 49 "Direct debit", 54 "Credit card", 55 "Debit card", 97 "Clearing between partners" (with descriptions; e.g. 97 "Amounts which two partners owe to each other to be compensated in order to avoid useless payments."). The same names are in CEFACT PaymentMeansCodeList. | confirmed |
| 2475 event time reference (Q31) | CEFACT TimeReferenceCodeList = 2475: 1 "Date of order", 2 "Date of confirmation", 8 "Date of confirmation of order received", 25 "Date goods handed over for shipment by seller or agent", 81 "Date of shipment as evidenced by the transport document(s)" | confirmed list. Proposal: OrderAccepted → **8** (or 2); Shipment → **81** (or 25). |
| 7085 cargo type (Q31) | CEFACT CargoTypeClassificationCodeList: "12 General cargo", "10 Breakbulk", "13 Liquid cargo" … **no bulk code** | GEN → **12** confirmed. **BULK: no 7085 code.** CEFACT CargoCategoryCodeList has "0 Liquid Bulk", "1 Solid Bulk", but its UN number cannot be identified from the source. Keep the regional BULK or use that list with a verified ID. |
| Rec 28 means type (Q31) | CEFACT TransportMeansTypeCodeList (134 codes, incomplete): 4000 "Aircraft, type unknown"; 1511 "Full container ship/cellular vessel"; 2302 "Train, container"; 3130 "Truck, with crane for moving goods, with trailer" … no generic truck+trailer, no pipeline, no dry-cargo barge except 8163 "Tank barge, dry cargo". | partly verifiable: 4000, 1511 and 2302 confirmed. Truck-with-trailer, barge and pipeline codes are not verifiable: the full Rec 28 is on unece.org (blocked). |
| ISO 20022 TRPT/GOVT (Q31) | iso20022.org external code sets: 403 | not verifiable |

## 4. IMDG and ERG

**EmS.** Source: BAM DGG-Info (Bundesanstalt für Materialforschung, German federal database), "Detailinfo IMDG-Code, Amdt. 42-24". The free public IMDG text is not available (the IMDG Code is a paid IMO publication).

- **UN 3480**: https://www.dgg.bam.de/dgginfo/detailinfo/imdg/qiiwcmqpnmffsyq — "Unfallmerkblätter (EmS) F-A , … S-I", "Feuer-Unfallmerkblatt A (Alfa): Allgemeines Feuer Unfallmerkblatt", "Leckage-Unfallmerkblatt I (India) für: Entzündbare feste Stoffe". **Confirmed `F-A,S-I`.**
- **UN 2920** (generic n.o.s. entry, PG II): https://www.dgg.bam.de/dgginfo/detailinfo/imdg/cgxnlqz9 — "Emergency Schedules (EmS) F-E , … Fire Schedule E (Echo) for: Non-water-reactive flammable liquids … S-C Spillage Schedule C (Charlie) for: Flammable, corrosive liquids". **Confirmed `F-E,S-C`.**
- **UN 2911** (instruments, solid): BAM radioactive module https://www.dgg.bam.de/dggradio/en/show/fopisxi353gvokc46mpq23ia4i — "IMDG-Code, Amdt. 42-24 … EmS F-I, S-S MFAG 20 ERG-Code 7L". **Confirmed `F-I,S-S`** (Q7's "verify" is resolved).

**MFAG column.** BAM's IMDG detail pages have an "MFAG No." field that is **empty** for UN 3480 and UN 2920. The IMDG detail page also quotes the requirement that "the emergency response information in accordance with 5.4.3.2 of the IMDG Code shall include … (EmS) and the Medical First Aid Guide … (MFAG)", so MFAG survives as a separate IMO publication. BAM's radioactive module still gives "MFAG 20" for UN 2911, so a table number exists outside the DGL. **Not verifiable from primary text** (the IMDG Code is paywalled); the evidence suggests the DGL has no MFAG column. Q13's use of the ERG stands.

**ERG 2024.** PHMSA returned 403. NOAA CAMEO Chemicals (US government) states "Emergency Response Guidebook (ERG, 2024)", with guide PDFs saved in `sources/noaa-cameo-erg/`:

- UN 3480 → "Response Guide 147". Guide_147.pdf title: "**Lithium Ion and Sodium Ion Batteries**".
- UN 2911 → "Response Guide 161". Guide_161.pdf: "**Radioactive Materials (Low Level Radiation)**".
- UN 2920 → "Response Guide 132". Guide_132.pdf: "**Flammable Liquids - Corrosive**".

**Verdict: all confirmed.** Note that 147's ERG 2024 title includes sodium ion batteries.

## 5. EPSG, PRONOM, CPC, DCSA, MIC, ISO 4217

- **EPSG 4326**: https://apps.epsg.org/api/v1/CoordRefSystem/4326/ — "Name": "WGS 84", "Kind": "geographic 2D", CoordSys 6422 "Ellipsoidal 2D CS. Axes: latitude, longitude. Orientations: north, east. UoM: degree". GeodeticCoordRefSystem: Datum 6326 "World Geodetic System 1984 ensemble". RevisionDate 2022-11-29. **Confirmed.** Note the axis order is latitude, longitude.
- **PRONOM** (https://www.nationalarchives.gov.uk/PRONOM/fmt/479.xml etc.): fmt/479 "Acrobat PDF/A - Portable Document Format", version "3a"; **fmt/480** "3b"; **fmt/481** "3u". All have MIME `application/pdf`; fmt/479 was last updated 11 Feb 2022. Also fmt/95 1a, fmt/354 1b, fmt/476/477/478 2a/2b/2u. **Confirmed.** The FormatCode↔MimeCode check is `application/pdf` for all of them.
- **UN CPC Ver.2.1**: https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/CPC_Ver_2_1_english_structure.txt and the explanatory notes `CPC_Ver_2.1_Exp_Notes_Updated_3Apr2025.xlsx`.
  - CPC has no specific park or outdoor furniture code; classification follows the HS.
  - **38111** "Seats, primarily with metal frames": "defined through … HS 2012: 9401.10, .20, .30, .71, .79". This fits the Serra park bench (cast/galvanised steel frame, HS 9401.79). **Proposal: 38111.**
  - **38112** "Seats, primarily with wooden frames" (HS 9401.40–.69). This fits the hardwood garden bench set (HS 9401.69). **Proposal: 38112.**
  - 38140 "Other furniture n.e.c." (9403.20, .50–.89). 38122 "Other wooden furniture, of a kind used in offices" (HS 9403.30).
  - Installation: **87390** "Installation services of other goods n.e.c." — "installation of other household goods … installation services of goods not elsewhere classified". **Proposal: 87390** for "Installation of furniture on site". The alternative 87310 (fabricated metal products) fits less well.
  - **New:** **CPC Ver.3.0** was published (structure dated 30 Jun 2025). Q10 names Ver.2.1, which remains valid, but consider the edition. The listID `UN CPC Ver.2.1` keeps the edition in the name, as Q5 requires.
- **DCSA seal source**: SwaggerHub `dcsaorg/DCSA_EBL` 3.0.0 and **3.0.3** (latest published) — "The source of the seal, namely who has affixed the seal. - `CAR` (Carrier) - `SHI` (Shipper) - `VET` (Veterinary) - `CUS` (Customs)", `"enum": ["CAR","SHI","VET","CUS"]`. **Confirmed. There is no PHY (phytosanitary) in the current version.** Map the regional PHYTOSANITARY code to UNCL 9303 AC (quarantine agency) only; it has no DCSA equivalent.
- **ISO 10383 MIC**: https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.csv (2,893 rows: 2,304 ACTIVE, 580 EXPIRED, 9 UPDATED).
  - Not present (in any status): XFER, XLUM, XSEL, XBAY, XURV, XCOD, XLMP, XSAL, XGUL, XACC.
  - Present: **XCOR (ICMA, GB) and XBRM (Romanian Commodities Exchange)**.
  - **Caution:** 649 real MICs start with X (XLON, XPAR …), so X is no fictional marker: a world MIC is free only because the list check says so. No MIC uses country XU, XB or XL.
  - **Verdict: XFER is free** (confirmed). Store this CSV for `--check`.
- **ISO 4217**: SIX list-one.xml (`Pblshd="2026-09-17"`) and list-three.xml (historic, `Pblshd="2026-01-01"`). XUF, XBL and XLC are in neither. The X codes in use are XAD, XAF, XAG, XAU, XBA, XBB, XBC, XBD, XCD, XCG, XDR, XOF, XPD, XPF, XPT, XSU, XTS, XUA, XXX. **Confirmed free.** Note **XUA** is real (ADB Unit of Account) and XAD and XCG are recent additions, so never use XUA, XCG or XAD.

## 6. Cards

- **ISO/IEC 7812 MII 9**: ISO text (iso.org) is blocked. Secondary source: Wikipedia "ISO/IEC 7812" (raw wikitext saved) — "9 || For assignment by national standards bodies"; "9 CCC || National standards bodies. The US National Numbering system (9840...) is managed by the American National Standards Institute"; "Card numbers starting with "80" or "9" are followed by the three-digit numeric-3 country code from ISO 3166-1". **Consistent, but not verifiable from primary text.**
- **ISO 3166-1 numeric 900–999**: iso.org blocked. Two independent confirmations:
  - RFC 5646 §2.2.4 (primary, below) confirms that ISO 3166 reserves AA, QM–QZ, XA–XZ and ZZ for private use (alpha-2 only).
  - Wikipedia "ISO 3166-1 numeric", citing the ISO glossary: "The numeric codes 900 to 999 can be user-assigned."
  - **Numeric: not verifiable from primary text; secondary sources confirm it.** 9901/9902/9903 card prefixes are consistent with it.
- **ISO/IEC 7816-5 category 'D' + country code**: not verifiable (paywalled; nothing on Wikipedia). Indirect evidence: the OpenPGP card spec v3.4.1 (gnupg.org) uses the nationally registered RID "D2 76 00 01 24", where D + 276 is the numeric code for Germany: "The RID in the AID is registered by FSF Europe e. V." `D9xx` follows that pattern. **Consistent, not verified.**
- **PCI DSS** (FAQ pages reachable; the standard PDF is 403):
  - FAQ **1492** (Apr 2024): "PCI DSS Requirement **3.4.1** requires that no more than the BIN and last four digits of the PAN are displayed on computer screens, reports, etc. unless there is a documented business justification". For 8-digit BINs that means **first 8 + last 4 for display: confirmed**. FAQ 1492 is the FAQ number to cite.
  - FAQ **1091** (Jun 2022) is about *truncation for storage* (Req 3.5.1): "16-digit PAN (with either 6- or 8-digit BIN) … Maximum digits which may be retained: 'First 8, any other 4'".
  - FAQ **1146**: "Masking is addressed in PCI DSS Requirement 3.4.1, whereas truncation is one of several options specified to meet PCI DSS Requirement 3.5.1."
  - SAD: FAQ **1533** — "sensitive authentication data must not be stored after authorization even if encrypted"; FAQ **1280** — "It is not permitted to retain card verification codes once the specific purchase or transaction for which it was collected has been authorized."
  - **Confirmed in substance. The requirement numbers 3.3.1 / 3.3.1.2 (SAD, card verification code) are not verifiable**: the v4.0.1 PDF is behind the document-library gate, and the FAQs say only "PCI DSS Requirement 3".

## 7. Identifier blocks (proposed fictional values)

- **GS1 prefix**: GS1 General Specifications, Release 26.0 (Jan 2026), PDF from https://ref.gs1.org/standards/genspecs/, Table 1-4: "**952** Used for demonstrations and examples of the GS1 system"; "984 – 989 Reserved for future use"; "951 … discontinued"; "02 / 20 – 29 … Restricted Circulation Numbers within a geographic region (MO defined)". GS1-8 Table 1-5 also has 952 for demonstrations. **Proposal: use GS1 Prefix 952** for every world GCP (GTIN, GLN, SSCC, GRAI). It is GS1's own example prefix, visibly fictional, and keeps the check digits valid. Do not use 984–989 (reserved, could be allocated) or 02/20–29 (RCNs, not GTINs).
- **ISO/IEC 15459 IAC (Codana)**:
  - AIM's current online register (item-id.org) is a Wasm app with no readable list, so it is **not verifiable**.
  - Rules: AIM RA procedures (Nov 2025 PDF) and the ISO/IEC 15459-2:2015 sample.
    - IACs are allocated from A–Z and 0–9: "IACs A – J … single character"; "IACs with first character **K** shall be reserved for national public administration and shall be completed with the relevant alpha-2 country code as established by ISO 3166-1"; "L-U … two character"; "V-Z … three character"; "GS1 is allocated a block of IACs ranging from 0 to 9".
  - Last readable register: NEN 2011-10-17 (pips.com copy). Codes used there: D, IBM, J, KDK, KKR, KNL, KUS, LA, LB, LD, LE, LF, LI, LM, LN, ND, NL, OD, PP, QC, RG, SI, ST, UN, VBS, VEC, VEG, VGL, VGT, VIB, VNA.
  - **Proposal: `KXU`.** By the rules only a public administration of country "XU" can hold it, and XU is ISO 3166 user-assigned, so no real agency can ever have it. This means presenting Codana as the XU public numbering administration; in parties.json it is now a "company" in category "government". If it must stay private, use a three-character V–Z code not in the 2011 register, such as `XCD`, and record that the current register could not be checked.
- **ISO 6523 ICD**: there is no public copy from the RA. Peppol's ICD list (PEPPOL-BIL `icd.xml`, Nov 2026) has 0002–**0248** (latest: 0248 "Oman Value Added Tax Identification Number (VATIN)"). The gaps 0092, 0103, 0181 and 0182 are probably withdrawn, so avoid them. The Peppol EAS list uses 9910–9959. **Proposal: ICD `0990`.** It is not in the ICD list, far above the current maximum, and outside the EAS 99xx range. ISO 6523 has no reserved private range, so this can only be checked, not guaranteed; the build should check it against `icd.xml`.
- **ASC MH10 DI "J"**: MHI page https://www.mhi.org/standards/mh10/dataidentifiers ("ANSI MH10.8.2-2021 | Updated September 9, 2025") and the e-d-c.info PDF of the same update. Category 10: "J LIC PLATE Unique license plate number"; "1J … assigned to a transport unit which is the lowest level of packaging, the unbreakable unit"; "5J … mixed transport unit"; "6J … master transport unit". **Confirmed.** For the 15459 licence plate use `J` + IAC + CIN + serial (an1+an1…35). Note ISO/IEC 15459-1 permits J and 1J–6J.
- **UIC wagon numbers**: OTIF UTP Marking, in force 01.01.2026 (PDF saved), §9 "RULES FOR THE DETERMINATION OF THE CHECK-DIGIT (DIGIT 12)":
  - "the digits in the even positions of the basic number (counting from the right) are taken at their own decimal value; the digits in the odd positions … are multiplied by 2; … the units digit of this sum is retained; the complement required to bring the units digit to 10 forms the check-digit".
  - This is the Luhn method over 11 digits; with the check digit the number has 12. **Confirmed.**
  - Digits 3–4 are the country code (§10). Numbers **not** in the §10 table: 11–19, 34–39, 45–48, 69, 77, 89 (49 is reserved for Bosnia-Herzegovina). **Proposal: XU 46, XB 47, XL 48.** UIC IRS 920-14 is not public, so this is checked against OTIF only.
- **ITU call sign series**: ITU table https://www.itu.int/gladapp/Allocation/CallSigns (saved).
  - **XB = Mexico (XAA–XIZ), XL = Canada (XJA–XOZ), XU = Cambodia (XUA–XUZ)**, so today's XBTH7 and XUBF4 call signs and the XL-KAC aircraft mark are **real-country prefixes**.
  - **No series starting with Q is allocated** (QA–QZ absent; Q is the Q-code series). Some lone former blocks are also absent, e.g. 4N and YZ (former Yugoslavia), but avoid those.
  - **Proposal: the Q series for all ITU-based world prefixes.** Ships' call signs `QU…`, `QB…`, `QL…` (e.g. QUBF4, QBTH7). Aircraft nationality marks `QU-`, `QB-`, `QL-` (e.g. QL-KAC).
- **MMSI MIDs**: ITU table https://www.itu.int/gladapp/Allocation/MIDs (292 MIDs allocated).
  - Unallocated in the European 2xx block: 200, 217, 221, 222, 223, 260, **280–299**. Many are free in the other regions too (e.g. 380–399, 480–499, 580–599, 680–699, 780–799).
  - ITU has no reserved fictional MID, so these can only be checked against the table.
  - The current values 999801042 and 999702117 start with 99, which is the AtoN format (99 MID xxxx), not a ship MMSI.
  - **Proposal: MIDs 297 (XU), 298 (XB), 299 (XL)**, ship MMSI `MID` + 6 digits, e.g. 297801042.

## 8. BCP 47 and ISO 639-2

- **RFC 5646 §2.2.4** (https://www.rfc-editor.org/rfc/rfc5646.txt): "The region subtags 'AA', 'QM'-'QZ', 'XA'-'XZ', and 'ZZ' are reserved for private use in language tags. These subtags correspond to codes reserved by ISO 3166 for private use. These codes MAY be used for private use region subtags". **Confirmed.**
  - IANA registry (File-Date 2026-09-17): "Subtag: XA..XZ Description: Private use".
  - §4.6: they "SHOULD NOT be used in content or protocols intended for general use" but are "RECOMMENDED over the 'x' singleton". `en-XU` etc. are fine for the closed world.
- **ISO 639-2 RA** (https://www.loc.gov/standards/iso639-2/ISO-639-2_utf-8.txt, Last-Modified 29 Sep 2025, 486 lines, saved for `build_codelists.py`): "qaa-qtz|||Reserved for local use|réservée à l'usage local". B/T pairs are on one line, e.g. "ger|deu|de|German|allemand", "dut|nld|nl|Dutch; Flemish|…", "fre|fra|fr|French|français", so the world list must split B and T into separate entries (ID-Q6). **Confirmed** (qaa–qtz local use; `qau`/`qal` lie inside it). RFC 5646 §2.2.1: "'qaa' through 'qtz' are reserved for private use"; IANA "Subtag: qaa..qtz … Scope: private-use".

## Not verifiable here (summary)

- UNECE UNTDID text for any UNCL (blocked). Code meanings come from UN/CEFACT's own vocabulary JSON plus Peppol's copies (D.16B/D.17A/D.23A).
- The full UNECE Rec 28.
- ISO 20022 ExternalPurpose1Code (TRPT, GOVT).
- The IMDG Code text itself (paywalled).
- ISO/IEC 7812-1, 7816-5, ISO 3166-1 and ISO 6523 primary texts (iso.org blocked or paywalled).
- PCI DSS v4.0.1 requirement numbers for SAD.
- The current AIM IAC register.
- UIC IRS 920-14.
