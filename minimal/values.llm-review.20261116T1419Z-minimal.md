# Review of the values in minimal/layer1

## Reviewed version

- Run: `20261116T1419Z-minimal`, topic: values
- Source: branch `claude/elegant-franklin-kk2dky`, commit `01f8672db560e38bf39ff4e0388672c1298a2f4f` (`minimal: findings on UBL 2.5 definitions, for the OASIS UBL TC`)
- Files: `minimal/gen_minimal.py` (869 lines), `minimal/layer1/*.xml` (93) and `minimal/layer1/deprecated/*.xml` (8).
- Model: UBL 2.5 OASIS Standard, the local package `minimal/.ubl/os-UBL-2.5/`. Definitions are quoted from `xsd/common/UBL-CommonAggregateComponents-2.5.xsd` and `xsd/maindoc/*.xsd` (`ccts:Definition`).
- Reproducibility: a copy of the generator, run in a scratch directory against the same package, produces output byte-identical to the committed `layer0/` and `layer1/` (`diff -r`: no differences; "202 documents, 0 with violations").
- Paths below are relative to `minimal/`; line numbers refer to `gen_minimal.py` at 01f8672. Every XPath was evaluated with lxml (prefix `d` = the root document's namespace, `cac`/`cbc` as usual) and selects exactly the value shown.
- Out of scope, not repeated: `ubl-findings.md` (F1–F10), and the findings of `layer1.llm-review.20261112T1659Z-minimal.md` and `placeholders.llm-review.20261112T1724Z-minimal.md` that have been processed. No value that those reviews fixed has regressed. One fix is only partly applied (VA#F1).

## Findings

### VA#F1 · High · Identifier values repeat across documents, against "values are unique across the set"

- **Where:** `id_for()` (l. 119–131) with `IDS = {}` reset per document in `generate()` (l. 694–695). Every non-party identifier is therefore `<label>-1` in every document that has one. Values that occur in more than one document:

  | Value | Files |
  |---|---|
  | `ContractFolderID-1` | 13: AwardedNotification, CallForTenders, ContractAwardNotice, ContractNotice, GuaranteeCertificate, QualificationApplicationRequest, QualificationApplicationResponse, Tender, TenderContract, TenderReceipt, TendererQualification, TendererQualificationResponse, UnawardedNotification |
  | `Shipment-1` | 11: CertificateOfOrigin, ForwardingInstructions, GoodsCertificate, GoodsItemPassport, ImportCustomsDeclaration, PackingList, WasteMovement, WasteNotification, Waybill, WeightStatement, deprecated/FreightInvoice |
  | `OrderReference-1` | 4: OrderCancellation, OrderChange, OrderResponse, deprecated/OrderResponseSimple |
  | `GoodsItemPassportCounterfoil-1` | 3: GoodsItemPassport, ProofOfReexportation, ProofOfReexportationReminder |
  | `Consignment-1` | TransportExecutionPlan, TransportExecutionPlanRequest |
  | `LicensePlateID-1` | TransportProgressStatus, TransportProgressStatusRequest |
  | `RelatedCatalogueReference-1` | CatalogueItemSpecificationUpdate, CataloguePricingUpdate |
  | `ParentDocumentReference-1` | UtilityStatement, deprecated/EnquiryResponse |
  | `DocumentReference-1` | InvoiceStatusResponse, ProofOfReexportation |
  | Name `Office supplies 2026` (NAMES, l. 517) | CallForTenders, ContractNotice |

  Examples:
  - `layer1/Tender.xml:/d:Tender/cbc:ContractFolderID` = `ContractFolderID-1`
  - `layer1/TenderReceipt.xml:/d:TenderReceipt/cbc:ContractFolderID` = `ContractFolderID-1`
  - `layer1/AwardedNotification.xml:/d:AwardedNotification/cbc:ContractFolderID` = `ContractFolderID-1`
  - `layer1/GoodsItemPassport.xml:/d:GoodsItemPassport/cac:GoodsItemPassportCounterfoil/cbc:ID` = `GoodsItemPassportCounterfoil-1`
  - `layer1/ProofOfReexportation.xml:/d:ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID` = `GoodsItemPassportCounterfoil-1`
  - `layer1/OrderChange.xml:/d:OrderChange/cac:OrderReference/cbc:ID` = `OrderReference-1`, and `layer1/OrderResponse.xml:/d:OrderResponse/cac:OrderReference/cbc:ID` = `OrderReference-1`
  - `layer1/TransportProgressStatus.xml:/d:TransportProgressStatus/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `LicensePlateID-1`, and the same in `layer1/TransportProgressStatusRequest.xml`
  - `layer1/CallForTenders.xml:/d:CallForTenders/cac:ProcurementProject/cbc:Name` = `Office supplies 2026`, and `layer1/ContractNotice.xml:/d:ContractNotice/cac:ProcurementProject/cbc:Name` = `Office supplies 2026`
- **Why:**
  - The docstring states the decision: "The documents are unrelated to each other: values are unique across the set, and references point outside it" (l. 15–16). The party values follow it (k = position × 10 + n, l. 417–418). The other identifiers do not.
  - ContractFolderID is defined as "An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs" (CallForTenders, Tender and the other procurement documents). With one value in 13 documents, the set says that a Japanese award notice, a US tender and an Indian guarantee belong to one procurement procedure. That is a cross-country procedure, which the one-locale decision excludes.
  - GoodsItemPassportCounterfoil is "One or more counterfoils associated with this Goods Item Passport" and, in ProofOfReexportation, "One or more goods item passport or ATA Carnet counterfoils associated with this proof of re-exportation", so the same counterfoil ID ties GoodsItemPassport (JP), ProofOfReexportation (BR) and ProofOfReexportationReminder (ZA) to one carnet. The same licence plate (`RoadTransport/LicensePlateID`, "The license plate identifier of this vehicle") makes one vehicle report in Japan and be asked about in India.
  - PH#F9 option 2 asked for "Distinct values without cross-document intent". The values are now distinct within each document, but equal values across documents are exactly the cross-document intent a reader infers.
- **Condition:** every identifier value (and every name of a particular thing, such as a project) occurs in at most one document of the set, unless both occurrences mean the same thing within that one document.
- **Options:**
  1. Do not reset `IDS` per document: a set-wide counter per label (`ContractFolderID-1` … `ContractFolderID-13`). Small change; the values remain labels.
  2. Number like the parties: label + the document's position (e.g. `ContractFolderID-76` in TenderReceipt), so a value says which document it belongs to and stays stable when other documents are added before it. Apply the same rule to `NAMES` with a per-document number (e.g. `Office supplies 2026-06`, or a different project per document).
  3. Keep the shared values but drop the claim "values are unique across the set" from the docstring. This contradicts the decision "documents are unrelated", so it is not recommended.
- **Needs decision:** no (the decision exists; only the pattern is to choose).

### VA#F2 · Medium · Certificate of Origin: the issuer's endorsement is made by a party other than the issuer

- **Where:** `layer1/CertificateOfOrigin.xml`, set by `generate()` (party names, l. 703–719) and `ENDORSERS` (l. 747–752):
  - `/d:CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:IssuerParty/cac:PartyName/cbc:Name` = `Example Issuer 123`
  - `/d:CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode` = `ISSUER`
  - `/d:CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Example Endorser 124`
- **Why:**
  - IssuerParty is "The authorised Organisation who issues the Certificate of Origin requested by this application".
  - EndorserParty/RoleCode is "A code specifying the role of the party providing the endorsement (e.g., issuer, embassy, insurance, etc.)". The value `ISSUER` says that the endorsing party *is* the issuer.
  - The two parties have different names and numbers (123 and 124), so the document states two different issuers. The generator numbers every party separately; it does not know that these two roles are the same organization. PH#F11 named this condition: "If the application's endorser and the issuer endorsement's endorser are the same party, … their names and identifiers say so."
- **Condition:** the EndorserParty whose RoleCode is `ISSUER` is visibly the same party as `IssuerParty`: the same name (and the same identifiers, once a layer adds them).
- **Options:**
  1. In `generate()`, give the issuer endorsement's party the IssuerParty's name and number (k = 123) instead of a new one. This is within one document, so the uniqueness rule is not affected.
  2. Change the RoleCode to something other than issuer. The definition of IssuerEndorsement ("Issuer Endorsement details") makes this unnatural, so it is not recommended.
- **Needs decision:** no

### VA#F3 · Low · Certificate of Origin: one signatory signs for the embassy and for the issuer

- **Where:** `NAMES["SignatoryContact/Name"]` (l. 515), used twice in `layer1/CertificateOfOrigin.xml`:
  - `/d:CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Alex Example` (endorser role `EMBASSY`, party `Example Endorser 121`)
  - `/d:CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Alex Example` (endorser role `ISSUER`, party `Example Endorser 124`)
- **Why:**
  - FILL (l. 253–256) adds the name because "A signature needs the person's name", that is, the signatory is a particular individual.
  - Read as ubl-findings F3 proposes ("The individual who signs this endorsement on behalf of the endorsing party"), one person signs for an embassy and for a chamber, which no real certificate shows.
  - Read literally ("The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party"), the same name is correct in both places, but then it is the exporter's representative. That does not fit an endorsement the issuer itself makes. The document does not say which reading the generator follows.
- **Condition:** each signatory name fits the reading the generator adopts, and that reading is stated in the comment at l. 253–256.
- **Options:**
  1. Follow ubl-findings F3: a distinct name per endorsing party (e.g. `Alex Example` and `Sam Example`; in ja-Latn `Sanpuru Tarō` and `Sanpuru Hanako`).
  2. Follow the literal definition: keep one name and say in the comment that it is the exporter's representative, and why the issuer's endorsement carries it.
- **Needs decision:** yes

### VA#F4 · Medium · Quantities and measures whose subject is not stated: exception criteria, exception notification, item information request

- **Where:**
  - `layer1/ExceptionCriteria.xml:/d:ExceptionCriteria/cac:ExceptionCriteriaLine/cbc:ThresholdQuantity` = `10` (unitCode `H87`), with `.../cbc:ThresholdValueComparisonCode` = `FALLS_BELOW_EXCEPTION_VALUE`
  - `layer1/ExceptionNotification.xml:/d:ExceptionNotification/cac:ExceptionNotificationLine/cbc:ComparedValueMeasure` = `8` and `.../cbc:SourceValueMeasure` = `10` (both `H87`)
  - `layer1/ItemInformationRequest.xml:/d:ItemInformationRequest/cac:ItemInformationRequestLine/cac:SalesItem/cbc:Quantity` = `10` (`H87`)
  - None of the three lines states the kind of activity. With lxml: `count(/d:ExceptionCriteria/cac:ExceptionCriteriaLine/*[self::cbc:SupplyChainActivityTypeCode or self::cbc:PerformanceMetricTypeCode or self::cac:ForecastExceptionCriterionLine])` = 0; `count(/d:ExceptionNotification/cac:ExceptionNotificationLine/*[self::cbc:SupplyChainActivityTypeCode or self::cbc:PerformanceMetricTypeCode or self::cac:ForecastException])` = 0; `count(/d:ItemInformationRequest/cac:ItemInformationRequestLine/*[self::cbc:SupplyChainActivityTypeCode or self::cbc:PerformanceMetricTypeCode or self::cbc:ForecastTypeCode])` = 0.
- **Why:**
  - ExceptionCriteriaLine is "a line … that specifies a threshold for forecast variance, product activity, or performance history". Its SupplyChainActivityTypeCode "Establishes the criterion for one of the three types of exceptions … This will be set if this Exception is about an Operational Exception … Possible values are: CANCELED_ORDERS EMERGENCY_ORDERS ON_HAND ORDERS RECEIPTS SALES SHIPMENTS". ExceptionNotificationLine has the same element ("This reports an exception notification about an operational exception").
  - The values 10 and 8 count pieces of the SupplyItem (UNITS comment, l. 156–157), but nothing says *what* is counted: stock on hand, sales, orders or receipts. A reader cannot tell whether "falls below 10" is a low-stock alert or a sales drop. The type of exception is implied by absence (IND6), and with it the meaning of every number in the line.
  - ItemInformationRequestLine/SalesItem/Quantity is "The quantity the given information are related to". Without the line's SupplyChainActivityTypeCode ("the type of supply chain activity about which information request is issued") the request does not say what information is requested about these 10 pieces.
- **Condition:** each of these lines states the kind of activity (or metric, or forecast) that its quantities measure. The kind is the same in ExceptionCriteria and ExceptionNotification if they are meant to illustrate one rule, and it fits the comparison direction (FALLS_BELOW).
- **Options:**
  1. Add `cbc:SupplyChainActivityTypeCode` to both exception lines with the value `ON_HAND` (a stock that falls below 10 pieces; UBL lists the value in both definitions), and `SALES` to ItemInformationRequestLine (consistent with its SalesItem). These are descriptive UBL-style values without listID, as decided.
  2. Use `SALES` in the exception documents too (sales below 10 pieces in the observation period). This matches ProductActivity's `SALES` and the four-week ExceptionObservationPeriod.
  3. Leave it to a later layer, and say in the comment at l. 156–157 that the type is still open.
- **Needs decision:** yes (which activity)

### VA#F5 · Low · Award and resolution dates fall on a Sunday

- **Where:** `DATE_OFFSETS["AwardDate"] = DATE_OFFSETS["ResolutionDate"] = -3` (l. 95), i.e. 2026-08-09, a Sunday:
  - `layer1/ContractAwardNotice.xml:/d:ContractAwardNotice/cac:TenderResult/cbc:AwardDate` = `2026-08-09` (JP)
  - `layer1/AwardedNotification.xml:/d:AwardedNotification/cac:TenderResult/cbc:AwardDate` = `2026-08-09` (JP)
  - `layer1/UnawardedNotification.xml:/d:UnawardedNotification/cac:TenderResult/cbc:AwardDate` = `2026-08-09` (JP)
  - `layer1/TenderContract.xml:/d:TenderContract/cac:TenderResult/cbc:AwardDate` = `2026-08-09` (IN)
  - `layer1/TendererQualificationResponse.xml:/d:TendererQualificationResponse/cac:QualificationResolution/cbc:ResolutionDate` = `2026-08-09` (IN)
- **Why:** AwardDate is "The date on which this result was formalized"; ResolutionDate is "The date on which this qualification resolution was formalized". A contracting authority formalizes decisions on a working day. Every other date in the set falls on a weekday (D is a Wednesday; offsets −28, −7, −1, +7, +14, +364 are Wednesdays and +20, +34 Tuesdays).
- **Condition:** dates on which an organization formalizes something fall on a working day in the document's locale.
- **Options:** −2 (Monday 2026-08-10). Not −1: 2026-08-11 is Mountain Day (Yama no Hi), a national holiday in Japan, and three of the five documents are Japanese. 2026-08-10 is the observed Women's Day holiday in South Africa, but no ZA document carries these dates (from knowledge, see Not verified).
- **Needs decision:** no

### VA#F6 · Low · The amount 100 is implausibly small in JPY and INR

- **Where:** `VALUES["AmountType"] = "100"` (l. 47–53):
  - `layer1/Tender.xml:/d:Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `100` (`JPY`)
  - `layer1/GuaranteeCertificate.xml:/d:GuaranteeCertificate/cbc:LiabilityAmount` = `100` (`INR`)
  - (The same value in USD, EUR, BRL and ZAR, e.g. Invoice, Reminder, Quotation, DebitNote, is plausible.)
- **Why:** TenderedProject/LegalMonetaryTotal is "The total amount for this tendered project". 100 yen (well under one US dollar) is not a bid for a procurement project. GuaranteeCertificate/LiabilityAmount is "The liability amount (a monetary value) in the Guarantee", and the guarantee is a bid bond ("the bid bond guarantee", InterestedParty). A bid bond of 100 rupees (about one US dollar) is not a real security. The generator's reason for 100, "a whole number, valid for every currency (JPY has no decimals)", is about format only. The principle at l. 7, "every value has a reason in its context", also covers magnitude.
- **Condition:** each amount is a whole number of a plausible order of magnitude in its document's currency.
- **Options:**
  1. One amount per currency, still a whole number, of about the same value: e.g. USD/EUR 100, BRL 500, ZAR 1800, INR 8000, JPY 15000. The exchange rates are orders of magnitude only and unverified; the build would still need no rounding rule.
  2. Keep 100 and record in the comment that magnitude is ignored on purpose.
- **Needs decision:** yes

### VA#F7 · Low · Brazilian Portuguese: "Operador Econômico" is the customs AEO term, not a procurement role

- **Where:** `ROLE_NAMES["EconomicOperatorParty"][2]` = `Operador Econômico` (l. 478):
  - `layer1/UnsubscribeFromProcedureResponse.xml:/d:UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name` = `Operador Econômico Exemplo 941` (`languageID="pt"`)
  - Related, also in a BR document: `layer1/CataloguePricingUpdate.xml:/d:CataloguePricingUpdate/cac:ProviderParty/cac:PartyName/cbc:Name` = `Provedor Exemplo 101`
- **Why:**
  - "Economic operator" is EU procurement vocabulary (Directive 2014/24/EU). In Brazil, "Operador Econômico" is used almost only in "Operador Econômico Autorizado" (OEA), the Receita Federal's customs AEO programme. Brazilian procurement law (Lei 14.133/2021) speaks of "licitante", "fornecedor", "interessado" and "contratado". In a Brazilian unsubscribe response the name reads as a customs status. The other BR role names follow Brazilian usage (Varejista, Estoque, Órgão Contratante, Licitante).
  - "Provedor" is mainly used in Brazil for service and internet providers. For the source of a catalogue, "Fornecedor" or a GS1 Brasil term would be more natural (unverified; minor).
- **Condition:** each role name is the term a Brazilian business would use for that role in that document type.
- **Options:**
  1. `Interessado` (the party taking part in, or leaving, a procedure); or `Fornecedor`, which AccountingSupplierParty already uses, so it would be ambiguous only if both roles met in one document (they do not).
  2. Keep it as a deliberate literal rendering of the UBL role, and say so in the comment.
  3. For ProviderParty: `Fornecedor do Catálogo`, or keep `Provedor`.
- **Needs decision:** yes

### VA#F8 · Low · languageID states the script for Japanese but not the variety for Brazilian Portuguese

- **Where:** `LANG` (l. 457): `"BR": "pt"`, `"JP": "ja-Latn"`. All Portuguese texts, e.g. `layer1/UnsubscribeFromProcedureResponse.xml:/d:UnsubscribeFromProcedureResponse/cac:EconomicOperatorParty/cac:Party/cac:PartyName/cbc:Name/@languageID` = `pt`.
- **Why:** the Portuguese values use Brazilian spelling and vocabulary (`Econômico` rather than European `Económico`, `Varejista` rather than `Retalhista`, `Estoque` rather than `Existências`). The decision is "texts in the locale's language … with languageID". For Japanese the generator states the script (`Latn`), as IND6 requires, because it is not implied. The Brazilian variety is equally specific to the locale, but it is left implied. The Japanese romanization is likewise implied: the IANA registry has a variant subtag `hepburn` with prefix `ja-Latn` (from knowledge, not checked against the registry in this session).
- **Condition:** languageID is equally precise for every locale whose text is variety-specific, or the comment says why not.
- **Options:**
  1. `pt-BR` (and optionally `ja-Latn-hepburn`). Both are valid BCP 47 tags for `xsd:language`.
  2. Keep `pt`, and say in the comment that the region subtag is left out on purpose because the document's country already says which variety it is.
- **Needs decision:** yes

### VA#F9 · Low · Two rules for references to a line of another document

- **Where:** `id_for()` (l. 123–124, 129–131):
  - `layer1/ForecastRevision.xml:/d:ForecastRevision/cac:ForecastRevisionLine/cbc:RevisedForecastLineID` = `RevisedForecastLineID-1` (label + number)
  - `layer1/DespatchAdvice.xml:/d:DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`, and the same in `layer1/DeliveryNote.xml` (line rule)
- **Why:** both are references to a line in another document. RevisedForecastLineID is "An identifier for the revised forecast line"; OrderLineReference/LineID is "An identifier for the referenced order line, assigned by the buyer". The comment says "line IDs are 1 (local by convention)". That convention fits a document's own lines, but it is applied to `LineID` wherever it appears, references included, while RevisedForecastLineID gets the reference rule. A referenced order line `1` also equals `layer1/Order.xml:/d:Order/cac:OrderLine/cac:LineItem/cbc:ID` = `1`, although the documents are unrelated. The match is weak, because no OrderReference says which order is meant.
- **Condition:** one rule for "an identifier of a line in another document".
- **Options:**
  1. Lines are numbered locally in every document, so a referenced line is `1` too: RevisedForecastLineID = `1`. This is simple, and it is how real documents number lines.
  2. References are labels, so OrderLineReference/LineID = `LineID-1`. Only `cac:*Line/cbc:ID` and `LineItem/ID` are then `1`.
- **Needs decision:** no (pick one)

### VA#F10 · Low · Generator comments contradict the values they document

- **Where and why:**
  - l. 278–281: "The answer is a neutral text placeholder, not an Indicator: 'true' would state a real answer; a later layer fills it." But l. 282 adds `cbc:ResponseIndicator`, and l. 64–65 set it to `true` ("yes to 'enrolled in a trade register?'"). The value is `layer1/QualificationApplicationResponse.xml:/d:QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`.
  - l. 498–499: "Not listed: stays X (e.g. the criterion answer, which waits for a real criterion). Not reviewed by native speakers." The first sentence is out of date (no `X` remains in layer1; the answer is set). The second contradicts l. 455–456: "Translations: checked against two independent human translations".
  - l. 178–180: ForecastPurposeCode `SALES_FORECAST` is "domain knowledge, not verified against GS1". UBL itself supports the value: ForecastExceptionType/ForecastPurposeCode reads "It is either Sales forecast or Order Forecast" (`xsd/common/UBL-CommonAggregateComponents-2.5.xsd:19902`). The comment can cite it.
  - l. 181–197: the comment for TransportServiceCode ("the extent of this transportation service …") is followed directly by the comment for SupplyChainActivityTypeCode. The two TransportServiceCode entries come only at the end of the table, after unrelated entries, so a reader takes one comment for the other.
- **Condition:** every comment describes the value the generator writes now, as the record of decisions (CLAUDE.md: "every decision and its reason is a comment").
- **Options:** rewrite the four places. For the second, say who checked the translations and that native-speaker review is still pending, if that is the case.
- **Needs decision:** no

## Checked and consistent

- **Dates (DATE_OFFSETS):** every period has StartDate ≤ EndDate. Observed and reported periods (ExceptionObservationPeriod, ActivityPeriod, ItemInformationRequest Period and line Period: 2026-07-15 to 2026-08-11) end the day before IssueDate. Forecast periods (2026-08-19 to 2026-09-15) and the retail event (2026-08-26 to 2026-09-01, seven days) lie in the future. Validity and effective periods start on IssueDate and end on 2027-08-11: 364 days later, so one year with both days inclusive. SourceForecastIssueDate (2026-08-05) is before the revision's IssueDate. TenderReceipt's RegisteredDate equals IssueDate, which fits "the date, assigned by the sender, on which the Tender Receipt was created".
- **Times (UTC_OFFSETS):** 09:30 local with the August offset of the locale: US −04:00 (EDT; the generator picks one US zone), DE +02:00 (CEST), JP +09:00, IN +05:30, BR −03:00 (Brasília; no DST since 2019, and Brazilian DST never covered August), ZA +02:00. Every Time and DateTime in a document uses its own locale's offset (GoodsItemItinerary DE, ForecastRevision JP, RequestForQuotation JP, TenderReceipt BR, TransportProgressStatus JP, TransportProgressStatusRequest IN, TransportServiceDescriptionRequest DE).
- **Currencies and countries:** every currencyID, DocumentCurrencyCode and Country/IdentificationCode matches the document's locale (checked across all 101 files). The amounts are one per document, so no totals need to add up.
- **Units:** H87 (piece) for pens and for the exception measures that count them, HUR for WorkReportLine/Quantity ("The quantity of work reported in this line"). Both come from UNECE Rec. 20, UBL's default unit list; phase-2 validation passes.
- **Measures and comparison:** ComparedValueMeasure 8 < SourceValueMeasure 10. This is consistent with the definitions ("The value used as the basis of comparison" / "The value that was compared … that resulted in the exception") and with the FALLS_BELOW direction used in ExceptionCriteria (the subject of the count: VA#F4).
- **Indicators:** AcceptedIndicator `true` (OrderResponseSimple, no rejection note needed). ResponseIndicator `true` answers a yes/no question, "An indicator used as a reply to the criterion requirement". AdmissionCode `true` is applied as decided (ubl-findings F7).
- **Codes (CODE_VALUES):** each value is in UBL's own style and fits its definition, without listID, as decided. `FALLS_BELOW_EXCEPTION_VALUE` comes from the definition's allowed values; `TOTAL` from the ForecastTypeCode examples; `SALES` from the values UBL lists for the same element; `PLANNED` fits an announced event; `ELECTRICITY` fits the utility statement; `TEMPORARY_ADMISSION` is the ATA procedure (all carnet documents are in ATA member countries: JP, BR, ZA, US); `PORT_TO_PORT` and `DOOR_TO_DOOR` come from the definition's examples; `ACCEPTED` is the type of response; EndorserParty RoleCode `ISSUER`/`EMBASSY` come from the definition's examples, with SequenceNumeric 1 and 2 in the order of endorsement.
- **Sequence and version identifiers:** SequenceNumberID, VersionID and TransportationSegment/SequenceNumeric `1` (first in sequence).
- **Party identifiers:** check digits were recomputed independently of the generator's functions, for all values. GLN 44 of 44 valid, all with GS1 prefix 952; LEI 20 of 20 (ISO 7064 MOD 97-10); Japanese Corporate Number 14 of 14, plus the 2 qualified-invoice numbers `T` + Corporate Number; DE USt-IdNr 8 of 8 (ISO 7064 MOD 11,10); CNPJ 6 of 6 (alphanumeric, a distinct root per party, establishment 0001); ZA VAT 4 of 4 *fail* Luhn, as intended; US EIN 8, nine digits with prefix 00. D-U-N-S 36, unverified as recorded in the generator. All party values are unique across the set.
- **Names and texts:** every Text and Name in a non-English document carries its locale's languageID, and no document mixes languages, except the fixed register name "Cadastro Nacional da Pessoa Jurídica", which is Portuguese and appears only in BR documents. Party names are unique and visibly fictitious (Example/Beispiel/Exemplo/Sanpuru + role + k). `Example Store 1` and `Alex Example` are visibly fictitious.
- **German terms used** (Lieferant, Kunde, Käufer, Verkäufer, Versender, Warenempfänger, Anbieter, Absender, Empfänger, Bieter, Wirtschaftsteilnehmer, Öffentlicher Auftraggeber, Frachtführer, Berichterstatter, Bestandsmelder, Abfallerzeuger, Notifizierender (the term of Regulation (EC) No 1013/2006 in German), Zollbehörde, Umsatzsteuer, "Kugelschreiber, blau", "Irrtümlich bestellt"): correct and understandable. The compounds follow the documented rule (one-word role → compound; multi-word → separate).
- **Japanese (Hepburn, macrons):** Sōshinsha, Jushinsha, Teikyōsha, Hatchū Kikan, Jigyōsha, Nyūsatsusha, Daihyō Nyūsatsusha, Sankasha, Meiginin (the carnet holder, 名義人), Urite/Kaite, "Bōrupen, ao", Hatchū, Shōhizei, Sanpuru Tarō (family name first). The spelling and long vowels are consistent.
- **Brazilian Portuguese used** (Fornecedor, Cliente, Vendedor, Comprador, Remetente, Destinatário, Empresa, Exportador, Órgão Contratante, "Caneta esferográfica, azul"): natural, except VA#F7.
- **Embedded PDF:** a valid PDF 1.4 (`pdfinfo`: 1 page, 240 × 160 pt, no errors). The xref offsets match the objects (9, 58, 115, 241, 324; startxref 394), `pdftotext` yields "PDF", and the mimeCode is `application/pdf`.
- **Criterion:** TenderingCriterionProperty/ID `TenderingCriterionProperty-1` equals ValidatedCriterionPropertyID, so the answer refers to the question in the same document. The question is a yes/no question in the Description ("A description of the criterion property"), and the answer is an indicator.
- **No placeholder `X` remains** in layer1.

## Considered and refuted

- **"Kourigyōsha" should be "Kōrigyōsha":** no. 小売 is ko-uri, where the u belongs to 売 (uri), so it is not a long ō.
- **Shiiresaki / Tokuisaki mix perspectives:** 仕入先/得意先 are the accounting terms for the counterparties of payables and receivables, which fits Accounting*Party. English "Supplier"/"Customer" are relational in the same way. They are not used in any layer1 document (no JP document has accounting parties).
- **German compounds with nominalized participles** (Beispielanfragender, Beispielantwortender, Beispielnotifizierender): a common German pattern (compare Geschäftsreisender), not wrong.
- **"Frachtführer" with PORT_TO_PORT** (GoodsItemItinerary, DE): HGB §407 Frachtführer covers road, rail, air and inland waterway; a port-to-port segment can be an inland waterway. Only a sea carrier would be "Verfrachter" (§481).
- **"Destinatário" for both DeliveryCustomerParty and ReceiverParty:** no BR document has both roles.
- **"Beispiel Öffentlicher Auftraggeber"** (two words): follows the documented rule for multi-word roles; not reopened.
- **Trade-register question in an Indian document:** the wording is generic ("a trade register") and fits Indian company registration as well.
- **One-locale exceptions:** none found. The CNPJ register name is Portuguese only in BR documents, and the US/IN/ZA documents are all in English.

## Not verified

- D-U-N-S values (36): no public check algorithm or test range, as the generator records. Whether `99xxxxxxx` numbers are real is unknown.
- Non-registration of the LEI, Japanese Corporate Number, CNPJ, USt-IdNr and EIN values: relied on the generator's claims ("checked … see the commit history"); not re-queried against GLEIF, NTA, Receita, VIES or the IRS in this session. The GS1 prefix 952 as the "demonstrations and examples" prefix is from knowledge of the GS1 General Specifications.
- Holidays (Japan's Mountain Day on 11 August; South Africa's Women's Day on 9 August, observed on Monday 10 August 2026) and the August UTC offsets: from knowledge, not checked against official calendars.
- Brazilian legal and customs usage of "Operador Econômico", "licitante" and "interessado" (Lei 14.133/2021, the Receita Federal OEA programme), and the naturalness of "Provedor": from knowledge, not checked against the law text or GS1 Brasil.
- The IANA variant subtag `hepburn`: from knowledge, not checked against the registry.
- The orders of magnitude in VA#F6: approximate exchange rates, not checked.
- No native-speaker review of the German, Portuguese or Japanese terms in this session.
