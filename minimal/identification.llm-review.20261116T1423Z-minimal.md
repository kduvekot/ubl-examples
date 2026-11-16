# Review of minimal/layer1: party identification

## Reviewed version

- Run: `20261116T1423Z-minimal`
- Source: branch `claude/elegant-franklin-kk2dky`, commit `01f8672` (`minimal: findings on UBL 2.5 definitions, for the OASIS UBL TC`). The working tree was clean before and after the review.
- Files: `minimal/gen_minimal.py` (869 lines). In it: `PARTY_SCHEMES`, `scheme_for`, `ID_VALUES`, `TAX_VALUES`, `TAX_NAMES`, `LANG`/`EXAMPLE`/`ROLE_NAMES`, `LAYER1`, and the party loop in `generate()`. Also `minimal/layer1/*.xml` (93 files) and `minimal/layer1/deprecated/*.xml` (8 files).
- Standard: UBL 2.5 OASIS Standard. Definitions were read from the `ccts:Definition` annotations in `minimal/.ubl/os-UBL-2.5/xsd/`.
- Method:
  - All 153 parties (every element with a `cac:PartyName`) were extracted with lxml: role, name, languageID, schemeID/ID, tax CompanyID, legal-entity CompanyID, TaxScheme name and the countries in the document.
  - The locale rotation was recomputed: alphabetical over the 101 maindoc XSDs, index mod 6.
  - Check digits were validated with `python-stdnum` 2.2.
  - Public registers were queried on 2026-11-16, with pauses between requests.
  - `python3 minimal/gen_minimal.py --check` was run on all 101 layer-1 files: 0 violations.
- All XPaths below were run with lxml (default namespace = the document's root namespace). Each selects exactly the value shown. Paths are relative to `minimal/`.
- Earlier reviews: L1#F1, F5, F6, F7, F9, F10, F12 and F16 of `layer1.llm-review.20261112T1659Z-minimal.md` are fixed in this version. No regression was found (see "Checked and consistent").

## Findings

### ID#F1 · Medium · D-U-N-S values still cannot be shown to be unassigned; they are the only party numbers in the set with no proof

- **Where:** `ID_VALUES[DUNS] = "99%07d" % k` (gen_minimal.py l. 425–428). It covers 36 parties in 27 files: generic Sender/Receiver, Seller/Buyer, Business, Requestor/Responder, economic operators, tenderers, the guarantee depositor and the utility receiver. Examples:
  - `layer1/Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `990000481` (schemeID `0060`)
  - `layer1/Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `990000482`
  - `layer1/GuaranteeCertificate.xml:/GuaranteeCertificate/cac:InterestedParty/cac:PartyIdentification/cbc:ID` = `990000392`
  - `layer1/UtilityStatement.xml:/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `990000952`
- **Why:**
  - Project rule: fictional values "must not be mistaken for real ones". The generator states that values come "from official demonstration ranges where a scheme has one, and [are] checked not to be real registrations where a public register can be queried".
  - Every other scheme now has either a demonstration range or a register answer. Only D-U-N-S has neither:
    - GLN uses GS1 prefix 952.
    - LEI got 404 from GLEIF.
    - The JP Corporate Number and the T-number are "存在しません" at the NTA.
    - DE VAT is invalid in VIES.
    - The US EIN uses prefix 00, which is not in the IRS list.
    - The BR CNPJ is not found at BrasilAPI (secondary).
    - The ZA VAT number fails Luhn on purpose.
  - D&B publishes neither a test range nor a check algorithm, so `99xxxxxxx` may be a real number. The code itself marks this as "UNVERIFIED" (l. 425–427).
  - The ICD entry says the number has a check digit. If that digit were Luhn (unverified), 8 of the 36 values would pass and 28 would fail: `990000002`, `…051`, `…242`, `…291`, `…481`, `…762`, `…812`, `…952` pass. So the values are neither shown to be valid nor shown to be invalid.
  - This is the open part of L1#F2. It is restated here because the review question asks directly whether the values are provably not real. It has not regressed.
- **Condition:** Every party value in the set is either from an official example range or shown to be absent from the issuer's register.
- **Options:**
  1. Keep D-U-N-S and record it as "not provable" in the comment and in "Not verified" (status quo).
  2. Replace D-U-N-S for these roles by a scheme that has proof. GLN 952 is the only official example range. GS1 defines the GLN as identifying parties (legal entities, functions) as well as locations; see ID#F2, where this definition is not verified. LEI `9999…` can be checked in GLEIF. Either change makes all values provable, but it gives up the "D-U-N-S, long used in EDI" reasoning for ordering and procurement.
  3. Ask D&B (or the D-U-N-S ICD registrant) for a documentation range, and cite it.
- **Needs decision:** yes

### ID#F2 · Low · The GLN rationale says "Location" only; GS1 defines the GLN as a party and location key

- **Where:** gen_minimal.py l. 304–306: "GLN is a Global *Location* Number: only for location-bound roles and GS1's own domains … Generic roles (Sender, Receiver, Seller, Buyer) follow the document's domain." The rationale covers all 44 GLN parties, for example:
  - `layer1/InstructionForReturns.xml:/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `9520000004118` (schemeID `0088`), a seller, which is not location-bound
  - `layer1/Manifest.xml:/Manifest/cac:SendingLogisticsOperatorParty/cac:PartyIdentification/cbc:ID` = `9520000004712`, an organisation, which is not location-bound
- **Why:**
  - Since the 2018 GLN Allocation Rules, the GS1 General Specifications (from knowledge) describe the GLN as identifying "parties and locations": legal entities, functions, physical and digital locations. gs1.org answered 403 from this machine, so the wording was not re-read; see Not verified.
  - The code already gives GLNs to non-location roles (sellers, logistics operators, reporters, GS1-domain senders and receivers). So the domain reasoning is right, but the stated reason is not.
  - The scheme choices themselves remain justified by their document domain. Only the reason as written is wrong, and it matters for ID#F1 option 2.
- **Condition:** The comment states the GLN's scope as GS1 defines it.
- **Options:**
  1. Reword: "GLN (GS1's key for parties and locations): for location-bound roles and GS1's own domains …", and cite the GS1 General Specifications section.
  2. Keep the wording and add that only GS1-domain use is intended.
- **Needs decision:** no

### ID#F3 · Low · The JP Corporate Number rule is applied only in part: a JP agreement participant keeps an LEI, and other customs/waste traders would fall back to the T-number

- **Where:** `scheme_for` (l. 377–386). In JP it maps D-U-N-S to 0188, LEI to 0188 only for `ContractingParty`/`SenderParty`, and TAX to 0188 only for `HolderParty`.
  - Instantiated: `layer1/DigitalAgreement.xml:/DigitalAgreement/cac:ParticipantParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999900MINIMAL0020170` (`@schemeID` = `0199`). Its name is `Sanpuru Sankasha 201`, and DigitalAgreement is a JP-locale document (index 20).
  - Latent, not instantiated in this set: in JP, `TransportServiceProviderParty` and `GuarantorParty` would keep LEI. `ExporterParty`, `NotifierParty` and `WasteProducerParty` would get the consumption-tax T-number under "Shōhizei".
- **Why:**
  - The docstring's reason is that the Corporate Number "is how Japanese public and private buyers identify a business". The inline comment adds "JP authorities and customs traders also have Corporate Numbers".
  - DigitalAgreement/ParticipantParty is "The business parties agreeing on a set of digital processes, terms and conditions …". These are businesses, so the same reason applies. Meanwhile every other JP business in the set gets 0188 (OrderChange, Tender, TendererQualification, ProcurementStatusRequest, …).
  - The `ExporterParty` mapping would bring back exactly what L1#F7 fixed for HolderParty: a customs trader identified by a consumption-tax number. The comment ("customs traders") names a class, but the code lists one role.
  - The current output follows L1#F10 option 1 ("Keep LEI elsewhere"). So this is an inconsistency between the stated reason and the code, not a regression.
- **Condition:** In JP, every role the stated reason covers gets 0188. Or the reason is narrowed to the roles the code covers.
- **Options:**
  1. In JP, map every LEI and every customs/waste TAX role to 0188, and keep T-numbers for the invoice-related roles only. The Corporate Number register covers national and local government bodies and registered companies alike.
  2. Keep the code and narrow the comment, e.g. "JP: 0188 for buyers, suppliers, contracting authorities and the carnet holder; LEI kept for agreement participants, carriers and guarantors as international legal-entity roles". Also add a comment or assertion that a JP ExporterParty/Notifier/WasteProducer is not expected.
- **Needs decision:** yes

### ID#F4 · Low · `ja-Latn` says Latin script but not which romanization; the generator's decision is Hepburn

- **Where:** every Japanese text, which is 29 `languageID="ja-Latn"` attributes in 15 layer-1 files. Party examples:
  - `layer1/AwardedNotification.xml:/AwardedNotification/cac:SenderParty/cac:PartyName/cbc:Name` = `Sanpuru Sōshinsha 21`, `@languageID` = `ja-Latn`
  - `layer1/InvoiceStatusRequest.xml:/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name/@languageID` = `ja-Latn` (value `Shōhizei`)
- **Why:**
  - The project decision is "Japanese in Hepburn" (l. 451–453, 455–456). The romanization system is part of what the text means: "Shōhizei" reads differently under Kunrei-shiki ("Syôhizei") or Nihon-shiki. The document now leaves the system implied, which conflicts with the spirit of IND6 ("nothing implied by absence").
  - The IANA Language Subtag Registry (File-Date 2026-09-17, fetched) has `Type: variant / Subtag: hepburn / Description: Hepburn romanization / Prefix: ja-Latn`. So `ja-Latn-hepburn` states the system exactly.
  - The value is a valid `xsd:language`, which is the base of UBL's languageID.
  - The spelling `Sanpuru` (n before p) follows modified Hepburn. The subtag does not separate modified from traditional Hepburn, so it is enough here.
- **Condition:** The languageID states the romanization the texts use.
- **Options:**
  1. `LANG["JP"] = "ja-Latn-hepburn"`, and the same key in `EXAMPLE`/`LANG_INDEX`. The IND7/IND8 checks are unaffected.
  2. Keep `ja-Latn` and record in the generator that the romanization is a set-wide convention.
- **Needs decision:** yes

### ID#F5 · Low · Comments no longer match the values they describe

- **Where and why:**
  1. Module docstring l. 13: "identifier values follow each scheme's format and check digit (ID_VALUES, TAX_VALUES)". Three schemes depart from this on purpose or of necessity, and the docstring does not say so:
     - ZA fails Luhn on purpose: `layer1/DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4000001712`.
     - The US EIN uses the unassigned prefix 00: `layer1/Reminder.xml:/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `000000661`. python-stdnum reports `InvalidComponent`.
     - The D-U-N-S check digit is unknown (ID#F1).
  2. l. 445–446: "Official names: EU Directive 2006/112/EC 'value added tax'". No value uses this name any more. DE is now `Umsatzsteuer` (`layer1/Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Umsatzsteuer`), and its source (UStG) is given two lines later.
  3. The `scheme_for` docstring says the Corporate Number "takes D-U-N-S's place". The code also replaces LEI (ContractingParty, SenderParty) and TAX (HolderParty), for example `layer1/ProcurementStatusRequest.xml:/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `9999900000561`.
  4. `TAX_NAMES` capitalisation is mixed:
     - sentence case: `Federal income tax` (`layer1/Reminder.xml:/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name`);
     - title case: `Value-Added Tax` (`layer1/SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name`) and `Goods and Services Tax`.
     The IRS itself writes "federal income tax" in running text, so either form is sourced. The difference is not explained.
  5. l. 420–422: "checked not to be real registrations … (GLEIF, VIES, NTA; see the commit history)". Every value changed with the k-numbering, so the old checks no longer apply. They were redone on 2026-11-16, and all current values passed (see Checked and consistent).
- **Condition:** Every comment describes the current values and their sources.
- **Options:** Update the five comments. Point 1, for example: "follow each scheme's format and check digit, except where a deliberately invalid value is the only proof of non-assignment (ZA, US prefix) or the algorithm is unpublished (D-U-N-S)". Point 5: cite this review or a dated check log.
- **Needs decision:** no

## Checked and consistent

- **Scheme per role.** The same role gets the same scheme across documents, apart from the `Document/Role` overrides, and each override has a reason. Counts over 153 parties:

  | Scheme | Parties |
  |---|---|
  | GLN 0088 | 44 |
  | D-U-N-S 0060 | 36 |
  | LEI 0199 | 20 |
  | JP Corporate Number 0188 | 14 |
  | national tax number (PartyTaxScheme) | 22 |
  | CNPJ (PartyLegalEntity) | 6 |
  | name only | 11 |

  Definitions checked against the role choices:
  - ManifestType/SendingLogisticsOperatorParty: "The Party who issues this Manifest. This Party is normally the Logistics Operator."
  - InventoryReportType/RetailerCustomerParty: "The retailer, who sends this message."
  - GoodsItemPassportType/HolderParty: "… normally the temporary exporter of the Goods."
  - GuaranteeCertificateType/GuarantorParty: "The guarantee creditor organisation who has the authority to charge bid bond guarantee credit". This matches the comment's "guarantee creditor".
  - GuaranteeCertificateType/InterestedParty: "The Party who deposits the bid bond guarantee". This is the tenderer, so D-U-N-S is consistent with EconomicOperatorParty.
  - TransportExecutionPlanType/TransportServiceProviderParty: "The Party who offers the transport service …".
  - DigitalAgreementType/ParticipantParty: see ID#F3.
  - Name-only roles: CertificateOfOrigin's endorsers, preparer and issuer, the GoodsCertificate issuer, the customs authorities, and the ATA guaranteeing associations. These match the comment's list (authorities, chambers, certificate issuers, CoO preparer).
- **Fixes from the earlier review hold:**
  - L1#F1: each BR party has its own CNPJ root (`ZZ000161`, `ZZ000281`, `ZZ000341`, `ZZ000342`, `ZZ000701`, `ZZ000702`), always with order `0001`.
  - L1#F5: the CNPJ is in PartyLegalEntity/CompanyID ("An identifier for the party as registered within a company registration scheme"), under CorporateRegistrationScheme `Cadastro Nacional da Pessoa Jurídica`, languageID `pt`, jurisdiction `BR`.
  - L1#F6: every TaxScheme and CorporateRegistrationScheme carries `JurisdictionRegionAddress/Country/IdentificationCode` equal to the document's locale ("A geographic area in which this taxation scheme applies").
  - L1#F7: the JP carnet holder has 0188 `7999900000381`.
  - L1#F9: values are unique across the set. Of the 153 party names, none repeats, and of the 142 identifier values, none repeats. The digits of JP T-numbers no longer coincide with 0188 values.
  - L1#F10: JP contracting authorities and procurement senders use 0188.
  - L1#F12: each tax name is in the locale's language with languageID.
  - L1#F16: the utility receiver has D-U-N-S.
- **Check digits** (python-stdnum 2.2), all valid:
  - 44 GLNs (GS1 mod 10);
  - 20 LEIs (ISO 17442, MOD 97-10);
  - 14 Corporate Numbers and the 2 bases of the T-numbers (NTA formula; the generator's `_jpcn` matches NTA's definition: Qn = 1 for odd n, 2 for even n, counted from the least significant digit);
  - 8 DE VAT numbers (ISO 7064 MOD 11,10);
  - 6 alphanumeric CNPJs (mod 11 with ASCII−48).
  - The deliberately invalid values are invalid as intended: 4 ZA numbers fail Luhn, and 8 EINs give `InvalidComponent` (prefix 00 is absent from stdnum's `us/ein.dat`, taken from the IRS page "How EINs are assigned and valid EIN prefixes").
- **Formats:**
  - GLN 13 digits;
  - LEI 20 characters (LOU part `9999`, then `00`, then an entity part containing `MINIMAL`);
  - D-U-N-S 9 digits;
  - JP 13 digits, and T + 13 for the qualified-invoice issuer number of a corporation;
  - DE `DE` + 9 digits;
  - CNPJ 14 characters (8-character root, `0001`, 2 check digits);
  - EIN 9 digits;
  - ZA 10 digits starting with 4.
  - The k-numbering (position × 10 + n, at most 1009) fits every pattern.
- **Registers re-queried today (2026-11-16):**
  - GLEIF API, `lei-records/<LEI>`: all 20 LEIs return 404. The control `5493001KJTIIGC8Y1R12` returns 200.
  - VIES REST, DE: all 8 numbers (`DE990004313`, `…6116`, `…6719`, `…6727`, `…9712`, `…9729`, `…9737`, `…9753`) return `isValid: false`, `userError: INVALID`.
  - NTA Corporate Number site, `henkorireki-johoto.html`: all 16 13-digit numbers (14 values under 0188, plus the bases of `T5999900000441` and `T4999900000442`) answer "存在しません". The control `7000012050002` (NTA) is found.
  - NTA qualified-invoice issuer site, `invoice-kohyo.nta.go.jp/regno-search/detail?selRegNo=`: both T-numbers answer "存在しません". The control `1180301018771` (トヨタ自動車株式会社) is found.
  - BrasilAPI (a secondary mirror of Receita Federal's open CNPJ data): all 6 CNPJs answer "não encontrado". The control `00000000000191` is found.
- **ICD codes.** 0088 GLN, 0199 LEI, 0060 D-U-N-S and 0188 JP Corporate Number match the ICD names that the earlier review confirmed in the official list. The list could not be re-fetched today; see Not verified. No ICD is used for a national tax number, as decided.
- **Locale.** Every party name, tax-scheme name and register name carries the languageID of the document's locale. Every country code equals the locale. The 0188 scheme appears only in JP documents, and D-U-N-S never appears in JP documents. The IN documents (ContractNotice, GuaranteeCertificate, DigitalCapability, …) use only GLN, D-U-N-S or LEI.
- **Structure.**
  - Each party has at most one of PartyIdentification, PartyTaxScheme or PartyLegalEntity, and PartyIdentification occurs once.
  - Layer-0 and layer-1 party names are identical, so only identification was added.
  - `gen_minimal.py --check`: 101 documents, 0 violations (XSD, IND1–IND9, phase-2 code lists).
- **Hepburn spellings of the role names** match modified Hepburn throughout: Shiiresaki, Tokuisaki, Niokurinin, Niukenin, Kourigyōsha, Sōshinsha, Jushinsha, Hatchū Kikan, Nyūsatsusha, Kyōtakusha, Meiginin, Tsūkokusha, Yunyū Hoshō Dantai, Shōhizei, and the rest. "Kouri" (ko-uri) rightly has no macron.

## Considered and refuted

- **IN GSTIN rejected by python-stdnum.** `_gstin("97ZZZCZ0031Z1Z")` = `97ZZZCZ0031Z1ZN` passes the mod-36 check (`luhn.is_valid(…, alphabet)` = True). stdnum rejects it only because its state table stops at 37 and lacks 97 "Other Territory". The value is unused: no IN document has a TAX role. Not a finding (the dead code is L1#F13, already processed).
- **DE USt-IdNr in purely domestic documents.** §14(4) no. 2 UStG allows the Steuernummer or the USt-IdNr on invoices, and the BZSt assigns it "for tax purposes". This fits PartyTaxScheme/CompanyID, and it is not cross-country.
- **US "Federal income tax".** The IRS calls the EIN a "Federal Tax Identification Number". A business entity uses it for its federal income-tax filings, so a single named scheme is defensible. This was decided under L1#F4. Only the capitalisation is listed (ID#F5).
- **pt `Destinatário` for both ReceiverParty and DeliveryCustomerParty.** Both translations are correct, the numbers keep the names unique, and no pt document has a consignee.
- **The CNPJ in PartyLegalEntity hard-codes the name and `pt`** (l. 728–730). Only BR reaches PartyLegalEntity (`party_extra`), and a BR TAX_NAMES entry is absent on purpose, so another country would stop the build rather than get a wrong name.
- **Receivers and providers swapped in CatalogueRequest, and "Shiiresaki"/"Tokuisaki" mixing buyer and seller perspective.** The first was refuted earlier. The second is a translators' decision already taken.

## Not verified

- **D-U-N-S:** the check-digit algorithm, any test range, and the registration status of the 36 values. D&B offers no public lookup (ID#F1).
- **ZA VAT:** that SARS uses Luhn, which is the basis of the deliberate failure, and the status of the 4 values. The SARS vendor search was not reachable (404) and needs eFiling.
- **BR CNPJ:** Receita Federal's own query needs a captcha. Only the BrasilAPI mirror was checked, and it may lag behind new alphanumeric assignments, which started in July 2026. Whether Receita will ever assign roots starting `ZZ` is unverified.
- **US EIN:** no register exists. The proof rests on the IRS prefix list, seen as stdnum's copy, not re-fetched from irs.gov.
- **GS1:** the GLN definition ("parties and locations", ID#F2) and GS1 prefix 952 "for demonstrations and examples". gs1.org returned 403, so both are from knowledge and from the earlier review.
- **ISO/IEC 6523 ICD list** (iso6523.info): not reachable from this machine, so the ICD names rest on the earlier review's check.
- **JP:** that a T-number for an individual sole proprietor could not coincide with these numbers. Individual T-numbers are not Corporate Numbers, but the invoice registry answered "存在しません" for both, which covers this.
- **IN:** the GSTN meaning of state code 97 (unused).
