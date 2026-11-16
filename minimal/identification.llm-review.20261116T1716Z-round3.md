# Review of minimal/layer1, round 3: party identification

## Reviewed version

- Run: `20261116T1716Z-round3`. Topic: layer 1, party identification.
- Source: branch `claude/elegant-franklin-kk2dky`, commit `6f3c962` (`minimal: UtilityStatement shows its consumption (DM#F116)`). The checkout HEAD is `73cae4f`, but the only commits after `6f3c962` add two other round-3 review files: `gen_minimal.py`, `layer0/` and `layer1/` are identical to `6f3c962`. Nothing was modified, regenerated or committed. The only file created in the repository is this one.
- Scope: `git diff 01f8672..6f3c962 -- minimal/gen_minimal.py`, which covers `PARTY_SCHEMES`, `scheme_for`, `DUNS_TEST`/`next_duns`, `ID_VALUES`, `TAX_VALUES`, `TAX_NAMES` and `ROLE_NAMES`. Also all 168 parties in `layer1/*.xml` and `layer1/deprecated/*.xml` (101 files). A party is any element with a `cac:PartyName`.
- Standard: UBL 2.5 OS. The definitions were read from the `ccts:Definition` annotations in `minimal/.ubl/os-UBL-2.5/xsd/`.
- Method:
  - Parties were extracted and every XPath below was evaluated with lxml (cac/cbc prefixes, root `/*`). Each XPath selects exactly the value shown.
  - Check digits were tested with python-stdnum 2.2, which was installed in the scratch directory only.
  - Registers were queried on 2026-11-16 with 1.5–2 s pauses, each with a positive control.
  - `python3 minimal/gen_minimal.py --check` on the 101 layer-1 files reported `0 with violations`.
- Round-2 findings ID#F1–F5 (`identification.llm-review.20261116T1423Z-minimal.md`):
  - ID#F1 (D-U-N-S): fixed with D&B test numbers.
  - ID#F2 (GLN wording): fixed.
  - ID#F3: fixed for ParticipantParty. Its latent part is now instantiated; see ID3#F1.
  - ID#F4 (`ja-Latn-hepburn`): fixed.
  - ID#F5: fixed except for one point; see ID3#F2.

## Findings

### ID3#F1 · Low · A Japanese carrier keeps an LEI, while every other Japanese business, including the consignor in the same Waybill, has a Corporate Number

- **Where:**
  - `layer1/Waybill.xml:/*/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `999900MINIMAL0098255`, `@schemeID` = `0199`, name `Sanpuru Unsōnin 982` (`ja-Latn-hepburn`).
  - In the same document: `layer1/Waybill.xml:/*/cac:ConsignorParty/cac:PartyIdentification/cbc:ID` = `1999900000981`, `@schemeID` = `0188`.
  - Waybill is document 98, and 98 mod 6 = 2, which is the JP locale.
  - Over the 17 JP documents, Waybill is the only one with an LEI. Each of the others uses 0188, or 0088 in GS1 domains, or the T-number.
  - Source: `scheme_for` (gen_minimal.py l. 545–557), which maps LEI to 0188 only for `ContractingParty`, `SenderParty` and `ParticipantParty`. `CarrierParty: LEI` is new since 01f8672 (l. 496, commit a0f77b2).
- **Why:**
  - UBL: Waybill/CarrierParty is "The Party who provides the transport of goods between named points". It is a business and the counterparty of the carriage contract.
  - Commit 2970d66 (ID#F3) moved JP agreement participants to 0188 "as other Japanese businesses do". The `scheme_for` docstring gives the reason: "Japanese buyers, authorities and customs identify businesses and public bodies by it". The inline comment says "JP authorities and customs traders also have Corporate Numbers".
  - That reason covers a Japanese carrier just as it covers the Japanese consignor beside it. Yet the carrier stays on LEI, and no comment says why carriers are an exception. Round-2 ID#F3 option 2 had proposed such a note ("LEI kept for agreement participants, carriers and guarantors as international legal-entity roles"). The decision went the other way for participants, and nothing was recorded for carriers.
  - Latent cases with the same gap, not instantiated in this set:
    - In JP, `TransportServiceProviderParty`, `FreightForwarderParty` and `GuarantorParty` would keep LEI.
    - The customs roles `ExporterParty`, `ImporterParty` and `TransitExporterParty` would get the consumption-tax T-number under `Shōhizei`. Two of these roles are new since 01f8672. A customs trader identified by a consumption-tax number is exactly what L1#F7 fixed for the carnet `HolderParty`.
    - Round 2 also asked for an assertion or comment for these cases. None was added.
- **Condition:** Every JP business role, customs traders included, gets 0188, or the comment states which JP roles keep another scheme and why.
- **Options:**
  1. In `scheme_for`, map every LEI role in JP to 0188, and every customs or waste TAX role in JP to 0188 as well. Keep the T-number only for invoice-related roles. Waybill/CarrierParty would then become 0188.
  2. Keep LEI for transport-contract providers, forwarders and guarantors. Say so in the docstring, for example: "international legal-entity roles in transport and finance keep the LEI, which Japanese carriers and banks hold". Add an `assert` that stops the build for a JP customs or waste TAX role until a scheme is chosen.
- **Needs decision:** yes

### ID3#F2 · Low · Two comments still describe the identifier values as they were before the D-U-N-S change

- **Where and why:**
  1. ROLE_NAMES comment, l. 662–664: the party name is "'example' + the role … + the party's number k **as in its identifier**". This held for every scheme while D-U-N-S was `99%07d % k`. Since 0066ba9 (ID#F1), the 38 D-U-N-S parties take the next unused D&B test number, and that number has no relation to k. Examples:
     - `layer1/Order.xml:/*/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Example Buyer 481`, but `…/cac:PartyIdentification/cbc:ID` = `302150375`.
     - For comparison, a GLN party: `layer1/Catalogue.xml:/*/cac:ProviderParty/cac:PartyIdentification/cbc:ID` = `9520000000714` (k = 71).
  2. Module docstring, l. 12–13: "identifier values follow each scheme's format and check digit (ID_VALUES, TAX_VALUES)".
     - Round-2 ID#F5.1 asked for the exceptions to be named. Commit 17dd527 named them at l. 559–562 (ZA fails Luhn, US prefix 00, D-U-N-S unpublished), but left the docstring unqualified.
     - The ZA and US values still depart from their check digit and prefix on purpose: `layer1/DebitNote.xml:/*/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4000001712` fails Luhn, and `layer1/Reminder.xml:/*/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `000000661` is an InvalidComponent for stdnum.
- **Condition:** Each comment describes the current values.
- **Options:**
  1. Change l. 663–664 to "+ the party's number k (as in its identifier, except for D-U-N-S, which takes D&B test numbers)".
  2. Change l. 13 to "… format and check digit, with the exceptions named at ID_VALUES".
- **Needs decision:** no

### ID3#F3 · Low · D-U-N-S values depend on the order in which they are used, so a later layer would renumber parties that already exist

- **Where:** `next_duns()` (l. 625–628) and `ID_VALUES[DUNS] = lambda k: next_duns()` (l. 638). In `generate()`, the line `_duns_used.clear()  # the same assignment in every layer` runs once per layer.
- **Why:**
  - Every other scheme derives its value from k = document position × 10 + party number, so a party has the same identifier in every layer. The module docstring says each layer is "a table of decisions on top of the layers below it", and that "a document keeps its locale in every layer".
  - D-U-N-S values are taken in global document order. Suppose a later layer gives a D-U-N-S to a party that had none, or adds a D-U-N-S role in an early document. Then every later D-U-N-S value in the set shifts. The same party, for example `layer1/WorkReport.xml:/*/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `362248622`, would carry a different number in layer 2 than in layer 1. The comment "the same assignment in every layer" holds only while the set of D-U-N-S parties stays the same.
  - The list also has a hard limit: 38 of the 123 numbers are used, and the 124th would raise an `IndexError` with no message. Other limits in the generator use an `assert` with a message (l. 158, l. 980).
  - This is latent: there is no layer 2 yet, and layer 0 has no identifiers.
- **Condition:** A party's identifier is the same in every layer, as for the other schemes.
- **Options:**
  1. Key the assignment by party, not by order. For example, keep a frozen map `{k: DUNS_TEST[i]}` built from the layer-1 D-U-N-S parties, and let new parties take numbers from the end of the list.
  2. Keep the current approach, and add an assertion in `check()` or `generate()` that the party identifiers of layer n equal those of layer n−1, plus an `assert len(_duns_used) < len(DUNS_TEST)` with a message.
- **Needs decision:** no

## Checked and consistent

- **D-U-N-S test list.** `https://docs.dnb.com/direct/2.0/en-US/duns-testing` was fetched today (HTTP 200). The page lists exactly 123 (number, country) pairs. They are identical, in the same order, to `DUNS_TEST`.
  - The page says: "Transactions using these D-U-N-S numbers will return data … for a fictitious company that is not intended for data field validation purposes and/or for use in live/production applications".
  - All 38 D-U-N-S values in the set are on the list, and each is used once.
  - No JP document has a D-U-N-S.
- **Scheme per role, new roles since 01f8672** (the UBL definitions were read from the XSDs):
  - **CarrierParty, LEI**, BillOfLading and Waybill: "The Party who provides the transport of goods between named points". This is the same reasoning as for TransportServiceProviderParty. For the JP exception, see ID3#F1.
  - **ConsignorParty, D-U-N-S (0188 in JP)**: "The Party who is reponsible for sending the goods". This is a responsible business, not a location, so not using GLN is consistent. DespatchSupplierParty (ship-from) stays GLN.
  - **FreightForwarderParty, LEI**: "The Party who combines individual smaller consignments into a single larger shipment …". It is a contract counterparty, like the carrier.
  - **AuthorityParty, name only**: "normally an Authority or regulator". This matches the comment's rule "authorities … by name only".
  - **ImporterParty, TAX**: "makes the import declaration … owner of the goods". In the BR locale this becomes the CNPJ in PartyLegalEntity (`layer1/ImportCustomsDeclaration.xml:/*/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyID` = `ZZ000401000109`, register name `Cadastro Nacional da Pessoa Jurídica`, jurisdiction BR). This is consistent with ExporterParty.
  - **TransitExporterParty, TAX**: `layer1/TransitCustomsDeclaration.xml:/*/cac:TransitExporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `4000008311`, TaxScheme `Value-Added Tax`, jurisdiction ZA. This follows the decided customs rule "the legally responsible trader, by tax registration".
  - **WinningParty, D-U-N-S (0188 in JP)**: "A party that is identified as the awarded by a tender result". This is the same scheme as TendererParty: `layer1/ContractAwardNotice.xml://cac:WinningParty/cac:Party/cac:PartyIdentification/cbc:ID` = `7999900000142` (0188).
  - **Branch** (StockAvailabilityReport/InventoryReportingParty): the name was changed, and the scheme stays GLN (`9520000007324`).
- **Counts over 168 parties:**

  | Scheme | Parties |
  |---|---|
  | GLN 0088 | 44 |
  | D-U-N-S 0060 | 38 |
  | LEI 0199 | 23 |
  | JP Corporate Number 0188 | 18 |
  | PartyTaxScheme | 25 |
  | CNPJ in PartyLegalEntity | 8 |
  | name only | 12 |

  The 12 name-only parties include the CoO issuer in its own endorsement, the same party as IssuerParty; see Considered and refuted. No scheme dominates.
- **ICD codes.** They were checked against the Peppol Participant identifier schemes v9.7, a secondary copy of the ICD entries (docs.peppol.eu, fetched today):
  - 0060 "Data Universal Numbering System (D-U-N-S Number)", Dun and Bradstreet;
  - 0088 "Global Location Number", 13 digits;
  - 0188 "Corporate Number of The Social Security and Tax Number System", National Tax Agency Japan, with the check-digit formula given there;
  - 0199 "Legal Entity Identifier (LEI)", characters 1–4 the LOU prefix, 5–6 "00", 19–20 MOD 97-10.

  The values match these structures.
- **Check digits** (stdnum 2.2 or the published formula), all correct:
  - 44 GLNs (GS1 mod 10);
  - 23 LEIs (ISO 17442);
  - 18 Corporate Numbers and the 2 T-number bases. `_jpcn` was checked against the 0188 entry's formula: Qn = 1 for odd n, counted from the bottom digit.
  - 9 DE VAT numbers (MOD 11,10);
  - 8 alphanumeric CNPJs.

  The deliberately invalid values are invalid as intended: 6 ZA numbers fail Luhn, and 10 EINs with prefix 00 give InvalidComponent.
- **Registers, today:**
  - **GLEIF:** all 23 LEIs return 404. The control `5493001KJTIIGC8Y1R12` returns 200. The new LEIs are `999900MINIMAL0003292` (BillOfLading carrier), `…0033265` (forwarder) and `…0098255` (Waybill carrier).
  - **VIES (DE):** all 9 numbers give `isValid: false`, `INVALID`: DE990004313, …4321, …6116, …6719, …6727, …9712, …9729, …9737, …9753. The control `DE129274202` is `VALID`.
  - **NTA houjin-bangou:** all 20 13-digit numbers answer "存在しません". These are the 18 values under 0188, plus the bases of `T5999900000441` and `T4999900000442`. The control `7000012050002` is found.
  - **BrasilAPI** (a secondary mirror): all 8 CNPJs answer "não encontrado" (404). The control `00000000000191` is found.
- **Uniqueness.** Across the set:
  - 156 identifier, tax and register values, with no repeat. No two values share the same digit core either: a JP T-number never reuses a 0188 value.
  - 168 party names, 167 of them distinct. The one repeat is the deliberate one in the CoO, where the issuer endorses as itself.
- **Locale, jurisdiction and language.** In every document:
  - each `JurisdictionRegionAddress/Country/IdentificationCode` equals the locale's country;
  - each PartyName, TaxScheme and CorporateRegistrationScheme name carries the locale's languageID (`en`, `de`, `pt-BR`, `ja-Latn-hepburn`);
  - 0188 occurs only in JP, and 0060 never occurs in JP.

  The tax names are `Federal Income Tax` (US, now title case), `Umsatzsteuer` (DE), `Shōhizei` (JP), `Value-Added Tax` (ZA), and the CNPJ register for BR.
- **The round-2 fixes hold:**
  - the GLN comment ("GS1 defines it for parties and locations");
  - the `scheme_for` docstring lists all the JP replacements;
  - the ID_VALUES note names the exceptions and the dated register checks;
  - the stale EU-directive note is gone;
  - JP agreement participants: `layer1/DigitalAgreement.xml` has 0188 `6999900000201` and `5999900000202`.
- **Structure.** Each party has at most one identification element. Layer 0 and layer 1 differ only in the identification elements and the tax and register names.

## Considered and refuted

- **Duplicate name `Example Issuer 123`:**
  - `layer1/CertificateOfOrigin.xml:/*/cac:CertificateOfOriginApplication/cac:IssuerParty/cac:PartyName/cbc:Name`
  - `layer1/CertificateOfOrigin.xml:/*/cac:IssuerEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name`

  This is the same party on purpose (DM#F4: "the issuer's endorsement is given by the issuer itself"). The uniqueness rule is about different parties.
- **Shared role words:**
  - pt `Fornecedor` for AccountingSupplierParty and EconomicOperatorParty (VA#F7);
  - de `Absender`, pt `Remetente` for SenderParty and ConsignorParty;
  - ja `Niokurinin` for DespatchSupplierParty and ConsignorParty;
  - `Transportadora`/`Transportador` and `Unsō Gyōsha`/`Unsōnin` for TransportServiceProviderParty and CarrierParty.

  These are majority translator decisions (d684198), which are not to be reopened. The numbers keep the names unique, and no document contains two roles with the same word.
- **ZA transit exporter identified by VAT and not by a SARS customs client number.** The customs rule ("by tax registration"; customs registers have no ICD and no safe test range) was decided in round 1 and is applied consistently. See Not verified.
- **D-U-N-S test companies in other countries** (e.g. `layer1/Order.xml` in the US locale uses `302150375`, an AT test company). This was decided on ID#F1.
- **D&B's note "not … for use in live/production applications".** Example documents are not a production application. The note confirms that the numbers belong to fictitious companies.

## Not verified

- **The official ISO/IEC 6523 ICD list** (iso6523.info: no connection from this machine). The ICD entries were checked only through Peppol's copy.
- **Whether LOU prefix `9999` is unallocated.** GLEIF's `lei-issuers` endpoint gave no JSON from here. Only the 23 records were confirmed absent.
- **The D-U-N-S check digit.** The ICD says "Eight identification digits and a check digit", but the D&B test numbers fit no published rule. This was decided; D&B publishes no algorithm.
- **ZA:**
  - that SARS uses Luhn for VAT numbers;
  - the status of the 6 ZA values;
  - whether SARS customs registration ties a customs client number to the VAT number (relevant to TransitExporterParty).
- **BR:** that Receita Federal will never assign alphanumeric roots starting with `ZZ`. Only the BrasilAPI mirror was queried; Receita's own query has a captcha.
- **US:** the IRS EIN prefix list. This was seen only through stdnum's copy, not on irs.gov.
- **GS1:** prefix 952 "for demonstrations and examples" and the GLN definition. gs1.org was not re-fetched; this rests on earlier reviews.
