# Review of minimal/layer1

## Reviewed version

- Run: `20261112T1659Z-minimal`
- Source: branch `claude/elegant-franklin-kk2dky`, commit `779ede3` (`minimal: real identifier values, tax scheme names, JP Corporate Number`)
- Files: `minimal/gen_minimal.py` (536 lines), `minimal/layer1/*.xml` (93) and `minimal/layer1/deprecated/*.xml` (8); `layer0/` compared with `diff -r`
- Model: UBL 2.5, `UBL-Entities-2.5.gc` (definitions as printed by `annotate.py --full` and `ubl_model.py`)
- Paths below are relative to `minimal/`. Line numbers refer to `gen_minimal.py` at 779ede3. All XPaths were checked with lxml: each selects exactly the value shown. The default namespace is the root document's namespace, `cac`/`cbc` are the usual UBL prefixes.

## What is expected

1. Decide each finding marked **Needs decision: yes** (the options are listed; pick one or write your own).
2. Make every change at the source: the tables `PARTY_SCHEMES`, `ID_VALUES`, `TAX_VALUES`, `TAX_NAMES`, `LAYER1` and the functions `scheme_for` and `generate` in `gen_minimal.py`. Never hand-edit the XML.
3. Regenerate with `python3 minimal/gen_minimal.py`. The XSD, IND and phase-2 checks must still pass. Then re-run the check-digit recomputation (`python-stdnum` validates GLN/EAN, LEI, DE VAT, CNPJ incl. alphanumeric, JP CN, GSTIN Luhn-mod-36).
4. Update the generator comments wherever a decision or a claimed source changes (e.g. "D&B publishes no check", "SARS's example").

## Findings

### L1#F1 · High · BR: two distinct parties get the same CNPJ root, i.e. the same legal entity

- **Where:** `TAX_VALUES["BR"]` (l. 262): `_cnpj("12ABC345%04d" % n)`. The party number `n` goes into the *establishment order* (positions 9–12), so the root `12ABC345` stays the same for every party. 4 files use BR tax numbers; 2 of them have two parties and are affected:
  - `layer1/SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000188`
  - `layer1/SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000269`
  - `layer1/deprecated/FreightInvoice.xml:/FreightInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000188`
  - `layer1/deprecated/FreightInvoice.xml:/FreightInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000269`
  - Single-party, not affected: `layer1/CreditNote.xml`, `layer1/ExportCustomsDeclaration.xml`.
- **Why:** In a CNPJ, characters 1–8 are the root (*raiz*), which identifies the legal entity. Characters 9–12 are the establishment order (0001 = head office/*matriz*, 0002… = branches/*filiais*), and 13–14 are the check digits (Receita Federal, CNPJ Alfanumérico Q&A no. 14; SERPRO "Cálculo dos dígitos verificadores de CNPJ alfanumérico"). `…/0001` and `…/0002` with one root therefore state that supplier and customer are the head office and a branch of **one** company. That contradicts the generator's own rule "distinct per party in a document" (l. 222), and it makes a self-billed credit note and a freight invoice look like an internal transfer.
- **Condition:** Every distinct party has a distinct 8-character root. Each root is visibly fictitious, and the order is `0001` unless a branch is meant.
- **Options:**
  1. Vary the root and keep `0001`: e.g. `_cnpj("12ABC%03d0001" % n)`, giving roots `12ABC001`, `12ABC002`. This is close to Receita's example root, but the reused 12ABC prefix has the same unverified real-assignment risk (see Not verified).
  2. Use letters that make the roots obviously fictitious, e.g. `"ZZEX%04d0001"`. Alphanumeric CNPJs are only assigned from July 2026; a root starting `ZZ` is no less safe than `12ABC345`, and it is clearly an example.
- **Needs decision:** yes (choice of root pattern)

### L1#F2 · High · D-U-N-S values have no check digit and may be real registrations

- **Where:** `ID_VALUES[DUNS]` (l. 253): `"99999%04d" % n`, comment "UNVERIFIED: D&B publishes no check or test range". Used through `PARTY_SCHEMES` for SellerSupplierParty, BuyerCustomerParty, EconomicOperatorParty, TendererParty, MainQualifyingParty, InterestedParty, BusinessParty, RequestorParty, ResponderParty and generic SenderParty/ReceiverParty, plus the procurement `…/ReceiverParty` overrides (l. 162, 178–185, 191, 203–205). That is 35 values in **26 files**: ApplicationResponse, BusinessCard, BusinessInformation, DigitalCapability, ExpressionOfInterestRequest, ExpressionOfInterestResponse, GuaranteeCertificate, Order, OrderCancellation, OrderResponse, ProcurementStatus, QualificationApplicationResponse, Quotation, TenderContract, TenderReceipt, TenderWithdrawal, TendererQualificationResponse, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse, WorkReport, deprecated/AttachedDocument, deprecated/Enquiry, deprecated/EnquiryResponse, deprecated/OrderResponseSimple, deprecated/TenderStatus, deprecated/TenderStatusRequest. Examples:
  - `layer1/Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999990001`
  - `layer1/Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999990002`
- **Why:**
  - The official ICD registration for 0060 (iso6523.info ICD list, 2026-07-26) gives the D-U-N-S structure as "Eight identification digits and a check digit", display `IIIIIIIIC`. So the generator comment is wrong as stated: the scheme *has* a check digit, even if the ICD entry does not publish the algorithm.
  - Every other scheme in layer 1 computes its check digit (l. 221–223, "the scheme's own format and check digit"); D-U-N-S is the exception. If the check is Luhn mod 10 (often claimed, not verified), both values are invalid (`999990001` and `999990002` fail Luhn; the Luhn-valid one would be `999990005`).
  - There is no demonstration range, and the values cannot be looked up publicly. A 9-digit D-U-N-S of this shape may exist in D&B's register. This is the brief's High criterion ("may be a real registration").
- **Condition:** Either the values are provably not real registrations, or the scheme is replaced where a scheme with a safe demonstration range fits the role equally well.
- **Options:**
  1. Keep D-U-N-S, but make the values invalid on purpose and say so: e.g. a deliberately wrong check digit under Luhn (if confirmed), with a comment that it cannot be a real number. Clean but unverifiable.
  2. Replace D-U-N-S by LEI (0199, `999900MINIMALEX…` already proven not in GLEIF) for the legal-entity roles (TendererParty, EconomicOperatorParty, BusinessParty …). Keep GLN 952 for trade roles where GS1 is plausible. This loses D-U-N-S coverage, but every value is then verifiably fictitious.
  3. Ask D&B (or the owner) for a documented test D-U-N-S range. Until then, mark the values as "UNVERIFIED, may be real" in a visible place (README/commit), not only in a code comment.
- **Needs decision:** yes

### L1#F3 · Medium · ZA VAT numbers fail the modulus-10 (Luhn) check, and the "SARS example" is unsourced

- **Where:** `TAX_VALUES["ZA"]` (l. 263): `"412345678%d" % (10 - n)`, comment "SARS's example 4123456789; check UNVERIFIED". 5 values in **3 files**:
  - `layer1/DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4123456789`
  - `layer1/SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4123456789`
  - `layer1/SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4123456788`
  - `layer1/UtilityStatement.xml:/UtilityStatement/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `4123456789`
  - `layer1/UtilityStatement.xml:/UtilityStatement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `4123456788`
- **Why:**
  - The format is right: a ZA VAT number is 10 digits beginning with 4.
  - Secondary sources (LookupTax, Commenda, citing SARS's VAT vendor search documentation) say the 10th digit is a modulus-10 (Luhn) check digit, as for income-tax reference numbers. `python-stdnum`'s `za.tin` uses Luhn for 0/1/2/3/9-prefixed references. Under Luhn, both `4123456789` and `4123456788` are invalid.
  - "10 − n" is not a check-digit calculation at all. It is the only TAX_VALUES entry without one, and it breaks for n ≥ 11 (see F14).
  - I could not find the claimed SARS example "4123456789" in a SARS document.
- **Condition:** The ZA rule is either "valid check digit, verified not registered" or "deliberately invalid, documented as such", like US EIN prefix 00. The comment cites a real source.
- **Options:**
  1. Compute Luhn: `b = "4%08d" % (99999990 + n)`, then append the Luhn digit. Check each value with SARS VAT vendor search (needs eFiling access, so the owner has to do it).
  2. Keep invalid numbers on purpose (as for EIN). Replace "SARS's example" by "check digit deliberately wrong (Luhn), cannot be a registered vendor", and drop `10 - n` for a fixed invalid digit pattern that also works for n ≥ 10.
- **Needs decision:** yes

### L1#F4 · Medium · US: EIN in PartyTaxScheme under a "Federal taxes" scheme

- **Where:** `TAX_VALUES["US"]` (l. 258) and `TAX_NAMES["US"] = "Federal taxes"` (l. 265), reached through `PARTY_SCHEMES` TAX roles (Accounting*, Waste*, Sender/Receiver overrides). 8 values in **3 files**: Reminder, Statement, WasteMovement. Examples:
  - `layer1/Reminder.xml:/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `000000001`
  - `layer1/Reminder.xml:/Reminder/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Federal taxes`
  - `layer1/WasteMovement.xml:/WasteMovement/cac:WasteProducerParty/cac:PartyTaxScheme/cbc:CompanyID` = `000000004`
- **Why:**
  - PartyTaxScheme is "A tax scheme applying to this party", and TaxScheme/Name is "The name of this taxation scheme". "Federal taxes" is a group of schemes, not one taxation scheme.
  - On a Reminder or Statement the relevant tax would be the state sales tax, which has state-level permit numbers; the EIN is an employer/federal income-tax identifier.
  - PartyTaxScheme/CompanyID ("An identifier for the party assigned for tax purposes by the taxation authority") does accept an EIN: the IRS assigns it for federal tax purposes. So the element is defensible; the scheme name is the weak part.
  - The values themselves are sound: prefix 00 is not in the IRS list of valid EIN prefixes (python-stdnum `us/ein.dat`, from irs.gov "How EINs are assigned and valid EIN prefixes"), so they cannot be real.
- **Condition:** The TaxScheme names one taxation scheme that the EIN is actually registered for, or the US accounting parties are identified another way.
- **Options:**
  1. Keep the EIN and rename the scheme to the one it belongs to, e.g. `TAX_NAMES["US"] = "Federal income tax"` (the EIN is the taxpayer ID for it).
  2. In the US locale, identify Accounting* parties by PartyIdentification (D-U-N-S/LEI) and drop PartyTaxScheme. US invoices normally carry no tax registration, and IND5 (no fillers) favours omitting a tax scheme that has no bearing on the document. A locale-aware `scheme_for` would do this, like the JP rule.
  3. Put the EIN in PartyLegalEntity/CompanyID. Weaker: the EIN is not a company-registration number.
  - Note: the conventional display is `00-0000001`. The digits-only form is accepted (stdnum compacts it); keep digits-only for consistency with the other numbers.
- **Needs decision:** yes

### L1#F5 · Medium · BR: CNPJ in PartyTaxScheme under "Federal taxes"; the CNPJ is a legal-entity register number

- **Where:** `TAX_NAMES["BR"] = "Federal taxes"` (l. 266) with `TAX_VALUES["BR"]`. 6 values in **4 files**: CreditNote, ExportCustomsDeclaration, SelfBilledCreditNote, deprecated/FreightInvoice. Examples:
  - `layer1/CreditNote.xml:/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000188`
  - `layer1/ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Federal taxes`
- **Why:**
  - CNPJ = *Cadastro Nacional da Pessoa Jurídica*, the national register of legal entities and their establishments, kept by Receita Federal. It is used for all federal taxes and by customs (Siscomex), but it is not the registration for one tax scheme. That matches PartyLegalEntity/CompanyID: "An identifier for the party as registered within a company registration scheme".
  - The tax-scheme-specific registration on a Brazilian invoice is the state *Inscrição Estadual* (ICMS) or the municipal one (ISS); IPI/PIS/COFINS, and from the 2026 reform CBS/IBS, are keyed on the CNPJ itself.
  - "Federal taxes" again names a group, not "this taxation scheme".
- **Condition:** The CNPJ sits in the element whose definition matches it, and any TaxScheme names one scheme.
- **Options:**
  1. For BR, move the CNPJ to `cac:PartyLegalEntity/cbc:CompanyID` and drop PartyTaxScheme for BR. All PartyLegalEntity children are optional in the model (RegistrationName 0..1, CompanyID 0..1 …), so CompanyID alone is schema-valid. Needs a new mechanism: e.g. a scheme value `LEGAL` beside `TAX` in `party_extra`.
  2. Keep PartyTaxScheme and name one scheme, e.g. `"CBS"` (*Contribuição sobre Bens e Serviços*, federal, CNPJ-based from 2026) or `"IPI"`. Plausible for the invoices, not for ExportCustomsDeclaration.
  3. Keep as is and document "Federal taxes" as the scheme family. This is the weakest option.
- **Needs decision:** yes

### L1#F6 · Medium · Which country's tax scheme? Nothing in the document says so (IND6)

- **Where:** `LAYER1` (l. 268–273) adds only `cbc:CompanyID` and `cac:TaxScheme/cbc:Name`. The locale "is visible only where one is needed" (l. 49–52). All 30 TAX values in **16 files**: CreditNote, DebitNote, ExportCustomsDeclaration, GoodsItemPassport, Invoice, InvoiceStatusRequest, PurchaseReceipt, Reminder, RemittanceAdvice, SelfBilledCreditNote, SelfBilledInvoice, Statement, UtilityStatement, WasteMovement, WasteNotification, deprecated/FreightInvoice. The ones where the value does not show the country are the problem:
  - `layer1/Statement.xml:/Statement/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `000000001` (US; "Federal taxes" of which federation?)
  - `layer1/DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Value-added tax` (ZA; only the ZAR currency elsewhere hints at it)
  - `layer1/WasteMovement.xml:/WasteMovement/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `000000001` (US; the document has no currency or country at all)
  - `layer1/GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:PartyTaxScheme/cbc:CompanyID` = `T8999999990001` (JP; recognisable only by format)
- **Why:**
  - CompanyID is "assigned … by the taxation authority", but the document never says which authority. The reader can only infer it from the number's format (DE prefix, JP `T`, CNPJ mask) or not at all (US, ZA). That is meaning implied by context that is absent, which IND6 is meant to prevent.
  - TaxScheme has exactly the element for it: `cac:JurisdictionRegionAddress`, "A geographic area in which this taxation scheme applies". Its `cac:Country/cbc:IdentificationCode` would carry the locale, as CountryType already does in layer 0 (FILL "CountryType").
- **Condition:** For every PartyTaxScheme, the issuing jurisdiction is stated in the document, not implied by the number's format or by the generator's locale.
- **Options:**
  1. Add `"TaxSchemeType": {"cbc:Name", "cac:JurisdictionRegionAddress"}` and `"AddressType": {"cac:Country"}` for this context. FILL already gives CountryType its IdentificationCode = locale. This is exact and code-based.
  2. Add `cbc:ID` with an issuer-qualified scheme. There is no international code list for national tax schemes, so this is weaker.
  3. Accept format-based recognition and document it as a deliberate exception. This does not solve US/ZA.
- **Needs decision:** yes

### L1#F7 · Medium · JP: the customs holder of a Goods Item Passport is identified by a qualified-invoice (consumption tax) number

- **Where:** `PARTY_SCHEMES["HolderParty"] = TAX` (l. 187) with `TAX_VALUES["JP"]` (l. 260). `scheme_for` (l. 213–219) switches only DUNS to the Corporate Number, so TAX stays TAX in JP. **1 file:**
  - `layer1/GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:PartyTaxScheme/cbc:CompanyID` = `T8999999990001`
  - `layer1/GoodsItemPassport.xml:/GoodsItemPassport/cac:HolderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Consumption tax`
- **Why:**
  - HolderParty is "The Party who holds the Goods Item Passport. This Party is normally the temporary exporter of the Goods."
  - The `T` + 13-digit number is the registration number of a *qualified invoice issuer* (適格請求書発行事業者登録番号, NTA). It exists for consumption-tax invoices, and only registered issuers have one.
  - A temporary exporter under an ATA carnet is identified to customs by the Corporate Number (法人番号; Japanese customs/NACCS import/export codes are built on it). Consumption-tax registration has no bearing on a carnet.
  - InvoiceStatusRequest (JP) uses the T-number too. That fits better, because it is about an invoice, though see F9 for the receiver.
- **Condition:** In JP, the T-number appears only where the document is about consumption-tax invoices. Other legally responsible traders get the Corporate Number.
- **Options:**
  1. In `scheme_for`, map TAX to JPCN (`0188`, PartyIdentification) for JP when the role is not an Accounting* role or an invoice-domain Sender/Receiver. The result is `…/cac:HolderParty/cac:PartyIdentification/cbc:ID[@schemeID='0188']`.
  2. Generalise: give customs trader roles (ExporterParty, HolderParty) their own constant `CUSTOMS`, resolved per locale: DE EORI (`DE` + up to 15 chars), JP 0188, BR CNPJ, US EIN (the USPPI ID in AES/EEI), IN IEC, ZA customs client number. This is more realistic, but needs new value generators and checks.
- **Needs decision:** yes

### L1#F8 · Low · Waste parties identified by tax number, not by the waste registers

- **Where:** `PARTY_SCHEMES` "customs and waste" (l. 186–188: NotifierParty, WasteProducerParty) and the Sender/Receiver override for WasteMovement and WasteNotification (l. 207–208). 8 values in **2 files**:
  - `layer1/WasteMovement.xml:/WasteMovement/cac:NotifierParty/cac:PartyTaxScheme/cbc:CompanyID` = `000000003` (US)
  - `layer1/WasteNotification.xml:/WasteNotification/cac:WasteProducerParty/cac:PartyTaxScheme/cbc:CompanyID` = `DE999999954` (DE)
- **Why:**
  - NotifierParty is "The Party responsible for providing the Waste Notification information and acting in the role of notifier", and WasteProducerParty is "The Party producing the waste material".
  - These roles are identified by the waste authorities' own registers, not by a tax number: the US EPA Identification Number (RCRA, on the hazardous waste manifest) and the German *Erzeuger-/Beförderer-/Entsorgernummer* (eANV/ZKS-Abfall). A VAT number is legal but does not fit the domain.
  - The comment's reason ("the legally responsible trader") is right for customs, but weaker for waste.
- **Condition:** If kept, the comment states why the tax number is used rather than the waste register.
- **Options:**
  1. Keep TAX and document that national waste registers have no ICD and no demonstration range (no safe fictitious value).
  2. Use LEI for these roles (a verifiably fictitious legal-entity ID), until a later layer adds national waste-register numbers with schemeID/schemeAgencyID.
- **Needs decision:** yes

### L1#F9 · Medium · Values are numbered by position in the document, so one value means opposite roles in related documents

- **Where:** `generate()` l. 409–419: `n` counts parties in document order (also name-only ones), and `ID_VALUES`/`TAX_VALUES` are functions of `n` only. Pairs where a reader who opens both documents sees the same number for the other party:
  - `layer1/Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999990001`, but `layer1/OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999990001` (and `deprecated/OrderResponseSimple.xml` the same)
  - `layer1/DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `9520000000011`, but `layer1/ReceiptAdvice.xml:/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `9520000000011`
  - `layer1/Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `DE999999911`, but `layer1/RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `DE999999911` (same DE locale: the invoice's supplier appears as the remittance's payer)
  - `layer1/DebitNote.xml:/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4123456789`, but `layer1/SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `4123456789`
  - `layer1/Catalogue.xml:/Catalogue/cac:ProviderParty/cac:PartyIdentification/cbc:ID` = `9520000000011`, but `layer1/CatalogueDeletion.xml:/CatalogueDeletion/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `9520000000011`
  - The same LEI `999900MINIMALEX00117` stands for a contracting authority (CallForTenders), a carrier (`layer1/TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportServiceProviderParty/cac:PartyIdentification/cbc:ID` = `999900MINIMALEX00117`) and a guarantee creditor/bank (GuaranteeCertificate).
  - Affected: the numbering rule applies to all 80 files with a party identifier (PartyIdentification or PartyTaxScheme). The cross-document clash is visible at least in the pairs above.
- **Why:** Each document is valid alone, but the set is published together, and readers compare documents of one process. An identifier is "An identifier for the party". The same identifier for a buyer in one document and a seller in the next asserts that they are the same party, which is not intended. Within a document the values are distinct (checked), so the issue is only across documents.
- **Condition:** Within a locale, one value always denotes one kind of party in one role family (buyer side and seller side), across all documents.
- **Options:**
  1. Number by role, not by position: a table `ROLE_N = {"BuyerCustomerParty": 1, "AccountingCustomerParty": 1, "DeliveryCustomerParty": 1, "SellerSupplierParty": 2, "AccountingSupplierParty": 2, "DespatchSupplierParty": 2, "ContractingParty": 3, ...}`, with the position as fallback. Sender/Receiver are resolved per document (who sends a ReceiptAdvice is the delivery customer). Distinctness per document must still be checked.
  2. Accept the clash and state in the generator docstring that values are unique only within a document. This is the minimum.
- **Needs decision:** yes

### L1#F10 · Medium · Contracting authorities identified by LEI (also in JP documents)

- **Where:** `PARTY_SCHEMES["ContractingParty"] = LEI` (l. 177), the procurement `…/SenderParty: LEI` overrides (l. 200–202) and `ParticipantParty: LEI` (l. 183). `scheme_for` keeps LEI in JP. Contracting-authority LEIs are in **20 files**: CallForTenders, ContractAwardNotice, ContractNotice, ExpressionOfInterestRequest, ExpressionOfInterestResponse, PriorInformationNotice, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationRequest, QualificationApplicationResponse, TenderContract, TenderWithdrawal, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse, deprecated/TenderStatus, deprecated/TenderStatusRequest (ContractingParty), plus AwardedNotification, UnawardedNotification, TenderReceipt, TendererQualificationResponse (SenderParty). JP examples:
  - `layer1/ProcurementStatusRequest.xml:/ProcurementStatusRequest/cac:ContractingParty/cac:Party/cac:PartyIdentification/cbc:ID` = `999900MINIMALEX00117`, next to `layer1/ProcurementStatusRequest.xml:/ProcurementStatusRequest/cac:EconomicOperatorParty/cac:Party/cac:PartyIdentification/cbc:ID` = `7999999990002` (schemeID 0188)
  - `layer1/AwardedNotification.xml:/AwardedNotification/cac:SenderParty/cac:PartyIdentification/cbc:ID` = `999900MINIMALEX00117`
- **Why:**
  - ContractingParty/Party is "The Party who is reponsible for the Contract" (UBL typo). Public authorities rarely hold an LEI. Procurement systems identify buyers by national organisation numbers: in eForms the organisation identifier is national; Peppol uses e.g. 0204, 0007, 0190.
  - In Japan, national and local government bodies are themselves assigned Corporate Numbers (ICD 0188 "Orgs covered" includes them; NTA publishes them). The generator's own reason for 0188 ("how Japanese public and private buyers identify a business", l. 214–216) argues for using 0188 for the JP contracting authority too.
  - The rule is consistent across documents (checked), so this is a fit question, not an inconsistency.
- **Condition:** The contracting authority's scheme is one public buyers in that locale actually hold.
- **Options:**
  1. Extend `scheme_for`: in JP, LEI → 0188 for ContractingParty and for the procurement SenderParty (the authorities). Keep LEI elsewhere.
  2. Keep LEI everywhere and change the comment to "the buyer as a legal entity; LEI chosen because it is the only international legal-entity scheme with a verifiable non-assigned range". That reason is honest and does hold.
- **Needs decision:** yes

### L1#F11 · Low · Nothing in the document says that schemeID holds an ISO/IEC 6523 ICD

- **Where:** `generate()` l. 414: `pid.set("schemeID", s)`, with no other scheme attribute. The ICD values appear in 112 `PartyIdentification/cbc:ID` elements in **64 files** (by files: 0060 26, 0088 22, 0199 25, 0188 7; a file can hold several schemes). Example:
  - `layer1/Catalogue.xml:/Catalogue/cac:ProviderParty/cac:PartyIdentification/cbc:ID/@schemeID` = `0088`
- **Why:**
  - IdentifierType.schemeID is "The identification of the identification scheme". The value `0088` is meaningful only if the reader knows that the schemeID values are ICDs; that is a convention (EN 16931, Peppol), not stated in the document.
  - UBL offers `schemeAgencyID` ("The identification of the agency that maintains the identification scheme") and `schemeName`. Neither is required, and established practice omits them.
  - Weighed against IND6 this is minor: a 4-digit numeric schemeID is unambiguous to anyone who knows ISO/IEC 6523.
- **Condition:** A documented decision, either "ICD in schemeID, by convention" (state it in the generator docstring and later in the layer notes), or extra attributes.
- **Options:**
  1. Keep it as is and document the convention (recommended; matches EN 16931 and Peppol).
  2. Add `schemeName` (e.g. `GLN`, `LEI`, `D-U-N-S`, `Corporate Number`). It is redundant, but readable without the ICD list.
- **Needs decision:** yes (small)

### L1#F12 · Low · Tax scheme names: mixed spelling, and no code

- **Where:** `TAX_NAMES` (l. 265–266). DE `Value added tax` (8 values: Invoice, PurchaseReceipt, RemittanceAdvice, WasteNotification) and ZA `Value-added tax` (5 values: DebitNote, SelfBilledInvoice, UtilityStatement). Examples:
  - `layer1/Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Value added tax`
  - `layer1/SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` = `Value-added tax`
- **Why:**
  - Each spelling follows its jurisdiction: EU Directive 2006/112/EC writes "value added tax", and South Africa's statute is the "Value-Added Tax Act 89 of 1991". So both are right. But a reader of the set sees an unexplained inconsistency, and the comment does not say it is deliberate.
  - JP "Consumption tax" (消費税) and IN "Goods and services tax" match the official English names. Official capitalisation is "Goods and Services Tax".
  - TaxScheme/ID ("An identifier for this taxation scheme") is optional. Name alone is acceptable in UBL. EN 16931/Peppol require `TaxScheme/cbc:ID` = `VAT` (UN/EDIFACT 5153), but that is practice, not UBL.
- **Condition:** The spelling choice is documented, or uniform.
- **Options:**
  1. Keep the jurisdiction spellings and add a comment with the two sources.
  2. Add `cbc:ID` from UN/EDIFACT 5153 (`VAT`, `GST`, with listID `UN/ECE 5153`) where a code exists. Not for "Federal taxes" or "Consumption tax" (5153 has no consumption-tax code; `GST` would be a stretch for JP).
- **Needs decision:** yes (small)

### L1#F13 · Low · The IN tax path is never exercised; state code 97 is a special-purpose code

- **Where:** `TAX_VALUES["IN"]` (l. 261) and `TAX_NAMES["IN"]` (l. 265). No IN-locale document has a TAX role: the IN files are BillOfLading, CatalogueItemSpecificationUpdate, ContractNotice, DigitalCapability, ExceptionNotification, ForwardingInstructions, GuaranteeCertificate, InvoiceStatusResponse, OrderResponse, ProductActivity, QualificationApplicationResponse, RetailEvent, TenderContract, TendererQualificationResponse, TransportProgressStatusRequest, UnsubscribeFromProcedureRequest, WeightStatement. So no GSTIN appears in layer 1 (0 files).
- **Why:**
  - The code would generate `97ZZZCZ9991Z1ZK`, `97ZZZCZ9992Z1ZJ` …. The mod-36 check digit is correct (verified with stdnum `luhn` over the GSTIN alphabet), and the PAN part `ZZZCZ999nZ` is well-formed (4th char C = company).
  - However, state code 97 is "Other Territory" in the GST state-code table (third-party lists citing GSTN; not confirmed on gst.gov.in). It is a real, assignable code for supplies outside any state's jurisdiction, not an unused one. stdnum rejects it because its table stops at 37.
  - Untested generator code drifts.
- **Condition:** If kept, at least one IN document exercises it, or the comment says it is unused. The state code is a deliberate choice.
- **Options:**
  1. Keep 97 (a GSTIN with code 97 and PAN `ZZZCZ…` is very unlikely to be registered) and document the meaning of 97.
  2. Use an unassigned state code such as `00`. It is safely fictitious, but some validators reject it.
  3. Since the locale order is fixed alphabetically, accept that IN never gets a TAX party, and say so in the comment.
- **Needs decision:** yes (small)

### L1#F14 · Low · Value formats break at n ≥ 10 parties

- **Where:** `TAX_VALUES` l. 259 (`"9999999%01d"`: DE base becomes 9 digits for n ≥ 10), l. 261 (GSTIN `%01d`: 16 chars for n ≥ 10), l. 263 (ZA `10 - n`: `4123456780` at n = 10, then a negative digit at n = 11). Maximum n today is 5 (WasteNotification, `DE999999954`), so no current file is affected (0 files).
- **Why:** The generator promises "the scheme's own format" (l. 221). A future layer that adds more parties would silently write invalid lengths; for ZA the value is also not even numeric.
- **Condition:** Each generator either supports the needed n with the right length, or raises an error (as `UNITS` does, l. 59–60).
- **Options:** Add `assert` length checks after each value is generated, or widen the variable part (DE: `"999999%02d"`).
- **Needs decision:** no

### L1#F15 · Low · CertificateOfOrigin: the application's preparer (normally the exporter) is name-only, while other customs traders get IDs

- **Where:** `PARTY_SCHEMES` has no entry for `PreparationParty` (comment l. 155–156: "Roles not listed (authorities, chambers of commerce, certificate issuers)"). **1 file:**
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:PreparationParty/cac:PartyName/cbc:Name` = `X`
- **Why:**
  - PreparationParty is "The Party who prepares this Certificate of Origin Application. This Party is normally an individual, a group or a body", in practice the exporter or its agent, not an authority. ExporterParty (l. 187) and HolderParty get TAX for the same kind of party.
  - IssuerParty ("The authorised Organisation who issues the Certificate of Origin") and EndorserParty (endorsers) are authorities or chambers, so leaving them name-only is consistent with the comment.
- **Condition:** Either PreparationParty gets the customs-trader scheme (TAX, or CUSTOMS per F7 option 2), or the comment explains why it stays name-only. "Normally an individual" is a valid reason, since a person may have no tax number.
- **Options:** Add `"CertificateOfOriginApplication/PreparationParty"` (key must match `role()` → `PreparationParty`, so `"PreparationParty": TAX`). Or document the individual case.
- **Needs decision:** yes

### L1#F16 · Low · UtilityStatement: receiver (utility customer) gets a VAT number

- **Where:** `PARTY_SCHEMES` l. 207–208 (UtilityStatement Sender/Receiver → TAX). **1 file:**
  - `layer1/UtilityStatement.xml:/UtilityStatement/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `4123456788`
- **Why:** UtilityStatement has separate optional `CustomerParty` and `SubscriberParty` (model), so ReceiverParty ("The Party who receives this Utility Statement") is only the document's recipient: the consumer, or an agent or billing service. The consumer is often a household or a small business that is not VAT-registered (ZA registration is compulsory only above ZAR 1 million turnover). The sender (the utility) having a VAT number is right. For the receiver, the VAT number states a fact that is often untrue and that does not follow from the document's purpose.
- **Condition:** The receiver's identification fits a typical utility customer.
- **Options:** Receiver by D-U-N-S/LEI like other generic receivers (`"UtilityStatement/ReceiverParty": DUNS`), or name-only. A customer account reference belongs to a later layer.
- **Needs decision:** yes (small)

## Checked and consistent

- **Check digits recomputed** with independent code and with `python-stdnum` 2.2:
  - GLN `9520000000011`, `…028`, `…035`: GS1 mod 10, valid.
  - LEI `999900MINIMALEX00117`, `…00214`: ISO 17442 / ISO 7064 MOD 97-10, valid.
  - JP Corporate Number `8999999990001`, `7999999990002` (and in `T8999999990001`, `T7999999990002`): NTA formula, valid. The same formula validates NTA's own number `7000012050002`.
  - DE VAT `DE999999911`, `…920`, `…938`, `…954`: ISO 7064 MOD 11,10, valid.
  - CNPJ `12ABC345000188`, `12ABC345000269`: alphanumeric mod 11, valid. The algorithm reproduces Receita's example `12.ABC.345/01DE-35` (sums 459/424).
  - GSTIN (generated, unused): mod 36, valid.
- **Not real registrations:**
  - GLEIF API: `999900MINIMALEX00117` and `999900MINIMALEX00214` return Not Found, and no LEI starts with `9999`.
  - VIES REST API: `DE999999911`, `DE999999920`, `DE999999938`, `DE999999954` all `isValid: false`.
  - EIN prefix `00` is not in the IRS valid-prefix list.
  - GS1 prefix 952 is "Used for demonstrations and examples of the GS1 system" (GS1 Company Prefix page; GS1 Style Guide §2.18).
- **ICD codes and names** confirmed in the official ICD list (iso6523.info, "as of 2026-07-26"):
  - 0060 "Data Universal Numbering System (D-U-N-S Number)", 0088 "GLN, Global Location Number", 0199 "Legal Entity Identifier (LEI)", 0188 "Corporate Number of The Social Security and Tax Number System" (issuer National Tax Agency Japan; 12 digits + leading check digit), 0209 "GS1 identification keys".
  - The GS1 Application Standard for ICD 0209 says the GLN "shall be used with ICD 0088 if not used in combination", so 0088 for a plain GLN is right.
  - There is no ICD for EIN, CNPJ, GSTIN or ZA VAT, which supports the "TAX in PartyTaxScheme" design.
- **Locale consistency:**
  - The locale rotation was recomputed (alphabetical over all 101 XSDs, as `generate()` does).
  - Every currencyID and country code matches its document's locale: CreditNote/Quotation/SelfBilledCreditNote/FreightInvoice BRL, DebitNote/SelfBilledInvoice/UtilityStatement ZAR, Invoice/PurchaseReceipt EUR, Reminder/Statement USD, Tender JPY, GuaranteeCertificate INR, CertificateOfOrigin US.
  - Tax numbers and tax scheme names follow the locale in all 16 TAX files.
  - JP replaces D-U-N-S by 0188 in all 7 JP files that would have had D-U-N-S.
- **Distinctness:** within every document the party values are distinct, and no party appears twice with different identifiers.
- **Role consistency:** the same role gets the same scheme across documents, except for the documented `Document/Role` overrides (InstructionForReturns and StockAvailabilityReport SellerSupplierParty GLN; GS1-domain Sender/Receiver GLN; procurement Sender LEI / Receiver D-U-N-S; invoice/utility/waste Sender/Receiver TAX). Each override has a reason in the comment.
- **One identifier per party:** each party has either PartyIdentification or PartyTaxScheme, never both, and PartyIdentification is used once (endorsed cardinality 0..1).
- **JP qualified invoice issuer number:** format `T` + 13-digit Corporate Number is right for a corporation (NTA), and it uses the same digits as the 0188 values (consistent identity between OrderChange and InvoiceStatusRequest).
- **Definitions fit** (annotate.py, no "NOT IN MODEL"/"NOT IN LIST" flags in the added elements): PartyTaxScheme/CompanyID "An identifier for the party assigned for tax purposes by the taxation authority" fits DE VAT, JP T-number, ZA VAT and IN GSTIN. PartyIdentification/ID "An identifier for the party".

## Considered and refuted

- **GuaranteeCertificate GuarantorParty as LEI "a bank":** UBL defines it as "The guarantee creditor organisation who has the authority to charge bid bond guarantee credit". The wording can be read either as the bank or as the beneficiary. LEI fits both readings, so the identifier choice stands. Only the comment "(a bank)" (l. 180) may overstate it; worth softening, not a finding. InterestedParty ("deposits the bid bond guarantee", i.e. the tenderer) as D-U-N-S matches EconomicOperatorParty.
- **TransportServiceProviderParty LEI versus SendingLogisticsOperatorParty/ReporterParty GLN:** different roles in different domains (transport contract versus GS1 logistics reporting). The comment justifies both, so this is not an inconsistency.
- **CatalogueRequest ProviderParty and ReceiverParty swapped relative to Catalogue:** UBL itself defines CatalogueRequest/ProviderParty as "The Party who sends the Catalogue Request", so the numbering follows document order, not an error in the scheme (the cross-document value clash is covered by F9).
- **DE "Value added tax" versus ZA "Value-added tax" as an error:** both are the official spellings of their jurisdictions (only a documentation point, F12).
- **IND5 for numbers like `000000001`:** not empty, a real (deliberately unassigned) EIN form; the IND5 check passes.
- **Missing `schemeID` on PartyTaxScheme/CompanyID:** the element's definition already says whose number it is ("by the taxation authority"), and no ICD exists for these numbers. Acceptable (the jurisdiction gap is F6).
- **InvoiceStatusRequest (JP) T-numbers:** the document is about an invoice, so the consumption-tax registration is the relevant identity for the supplier side. Not raised (the receiver may not be a registered issuer, but F16's reasoning is weaker for business partners).
- **Layer 0 FILL decisions as seen in layer 1** (PartyName `X`, CountryType IdentificationCode = locale, ItemType Description, ShipmentType ID): no semantic conflict with the layer-1 additions found.

## Not verified

- **D-U-N-S:** the check-digit algorithm (the ICD entry states a check digit exists but not how), and whether `999990001`/`999990002` are registered. D&B has no public lookup.
- **ZA VAT:** the check-digit rule (only secondary sources say Luhn), the claimed SARS example `4123456789`, and whether `4123456789`/`4123456788` are registered. SARS VAT vendor search needs eFiling.
- **CNPJ:** whether Receita Federal will ever assign the root `12ABC345` (its own documentation example) now that alphanumeric CNPJs are issued (from July 2026). No public query was made.
- **JP:** NTA register lookup for `8999999990001`/`7999999990002` (the NTA Web-API needs an application ID; the claim "not in the NTA register" was not re-checked). Also not checked against an NTA/Customs source: that NACCS importer/exporter codes are based on the Corporate Number (stated from domain knowledge).
- **IN:** the official GSTN meaning of state code 97 (only third-party lists were seen); GSTIN registration status.
- **Domain rules cited from knowledge, not fetched:** US EPA ID / German waste-register numbers, the eForms buyer-identifier practice, and the ZA VAT registration threshold.
