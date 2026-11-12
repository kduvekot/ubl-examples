# Review of the placeholder values in minimal/

## Reviewed version

- Run: `20261112T1724Z-minimal`
- Source: branch `claude/elegant-franklin-kk2dky`, commit `779ede3` (`minimal: real identifier values, tax scheme names, JP Corporate Number`)
- Files: `minimal/gen_minimal.py` (536 lines), `minimal/layer1/*.xml` (93) and `minimal/layer1/deprecated/*.xml` (8), 101 documents in all. Counts are over `*.xml` only.
- Model: UBL 2.5, `UBL-Entities-2.5.gc` (definitions as printed by `annotate.py --full` and loaded with `ubl_model.py`). UBL default code lists: the 11 genericode files cached by `ubl_model.py` (see Not verified).
- Scope: every value that comes from `VALUES` (l. 36–43), `ATTRS` (l. 47), the locale (`LOCALES` l. 54–55: currencyID, currency codes, country codes) and `UNITS` (l. 61–66). The layer-1 party identifiers and tax schemes are reviewed in `minimal/layer1.llm-review.20261112T1659Z-minimal.md` (L1#F1–F16) and are not repeated here.
- Survey: a script walked all 101 files, joined each leaf with the model row of its parent object class, and grouped the 504 placeholder values by (data type, parent, element). Paths below are relative to `minimal/`; line numbers refer to `gen_minimal.py` at 779ede3. Every cited XPath was checked with lxml and selects exactly the value shown. Unprefixed steps are in the root document's namespace; `cac`/`cbc` are the usual UBL prefixes.

| Data type | Values | Files |
|---|---|---|
| Identifier `X` | 166 | 94 |
| Name `X` | 158 | 85 |
| Date `2000-01-01` | 108 | 82 |
| Text `X` | 27 | 26 |
| Code `X` | 13 | 11 |
| Amount `0` | 11 | 11 |
| Quantity `0` | 7 | 7 |
| Time `00:00:00` | 7 | 7 |
| Numeric `0` | 3 | 2 |
| Measure `0` | 2 | 1 |
| BinaryObject `AA==` | 1 | 1 |
| Indicator `true` | 1 | 1 |
| Locale values (currency, country) | 3 element values + 11 currencyID | 14 |

The `VALUES` entries for DateTime, Percent, Rate, Value, Graphic, Picture, Sound and Video occur in no layer-1 document (PH#F19).

## What is expected

1. Decide each finding marked **Needs decision: yes**. Options are listed; pick one or write your own.
2. Make every change at the source, in `gen_minimal.py`. Change a type-level value in `VALUES`/`ATTRS`/`UNITS`, or add a per-element value table: e.g. `ELEMENT_VALUES = {"Parent/Element": value or rule}`, consulted in `build()` before `VALUES[u]` (l. 332). If a placeholder should stay in layer 0, add the replacement as a new `LAYERS` entry. Never hand-edit the XML.
3. Regenerate with `python3 minimal/gen_minimal.py`. The XSD, IND and phase-2 checks must still pass. Then re-check the dependencies in "Value dependencies for the next layer".
4. Where a value carries a decision (a date, an indicator, a code), add a comment in the generator with the reason, as for `FILL`.

## Findings

### PH#F1 · High · Amount `0` negates the purpose of the document

- **Where:** `VALUES["AmountType"] = "0"` (l. 37). 11 values in **11 files**:
  - PayableAmount (9): CreditNote, Invoice, PurchaseReceipt, Quotation (`QuotedMonetaryTotal`), Reminder, SelfBilledCreditNote, SelfBilledInvoice, Tender (`TenderedProject/LegalMonetaryTotal`), deprecated/FreightInvoice
  - DebitNoteLine/LineExtensionAmount (1): DebitNote
  - LiabilityAmount (1): GuaranteeCertificate

  Examples:
  - `layer1/Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
  - `layer1/Reminder.xml:/Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
  - `layer1/Tender.xml:/Tender/cac:TenderedProject/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
  - `layer1/DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `0`
  - `layer1/GuaranteeCertificate.xml:/GuaranteeCertificate/cbc:LiabilityAmount` = `0`
- **Why:**
  - Invoice is "A document used to request payment". Its PayableAmount is "The amount of the monetary total to be paid". An invoice with a line that requests 0 contradicts its own purpose.
  - The same holds for a reminder of 0 owed, a credit note crediting 0, a debit note line of 0 ("The total amount for this debit note line"), a tender bid of 0 ("the total amount for this tendered project", FILL comment l. 76–78) and a guarantee whose "liability amount" is 0.
  - `0` here is not empty, but it is the null-like value IND5 is meant to exclude: it says "nothing". A zero invoice exists in practice (e.g. fully prepaid), but then other elements (PrepaidAmount) would have to say why. The minimal document does not, so the zero is unexplained.
- **Condition:** Each amount is positive and plausible for its element. Amounts that depend on each other add up (see Value dependencies).
- **Options:**
  1. A type-level value `"100"` for AmountType. It is an integer, so it is valid for every locale currency: JPY has no minor unit in ISO 4217, the others have 2 decimals. All 11 elements stand alone in layer 1 (no line amount sits beside a total), so no sum breaks. Cheapest.
  2. A per-currency format: `"100.00"`, but `"100"` for JPY. This is more realistic for the decimal currencies and needs a small lookup next to `LOCALES`.
  3. Keep `0` in layer 0 and replace it in a "monetary" layer that also adds line amounts and quantities, so that totals are sums (see PH#F2).
- **Needs decision:** yes (type value versus per-currency format)

### PH#F2 · High · Quantity `0` on lines that exist to report a quantity

- **Where:** `VALUES["QuantityType"] = "0"` (l. 42). 7 values in **7 files**:
  - InstructionForReturnsLine/Quantity
  - InventoryReportLine/Quantity
  - WorkReportLine/Quantity
  - SalesItem/Quantity (ItemInformationRequest, ProductActivity)
  - StockAvailabilityReportLine/Quantity (deprecated)
  - ExceptionCriteriaLine/ThresholdQuantity

  Examples:
  - `layer1/InstructionForReturns.xml:/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Quantity` = `0`
  - `layer1/WorkReport.xml:/WorkReport/cac:WorkReportLine/cbc:Quantity` = `0`
  - `layer1/ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:SalesItem/cbc:Quantity` = `0`
  - `layer1/InventoryReport.xml:/InventoryReport/cac:InventoryReportLine/cbc:Quantity` = `0`
  - `layer1/ExceptionCriteria.xml:/ExceptionCriteria/cac:ExceptionCriteriaLine/cbc:ThresholdQuantity` = `0`
- **Why:**
  - "The quantity of goods being returned" = 0 means nothing is returned, yet the line instructs a return. "The quantity of work reported in this line" = 0 means no work. "The quantity the given information are related to" = 0 makes the sales information refer to nothing. These contradict the line's own reason to exist.
  - InventoryReportLine and StockAvailabilityReportLine ("currently in stock") = 0 is not a contradiction: it is a real statement, "out of stock". But the reader cannot tell that statement from a placeholder.
  - ThresholdQuantity ("A quantity beyond which an exception will be triggered") = 0 makes any activity an exception, which is degenerate.
- **Condition:** Every quantity is positive. A stock of 0 appears only if a later layer means "out of stock".
- **Options:**
  1. A type-level value `"10"` (with a unit, PH#F7).
  2. Per element: Returns `"2"`, Inventory/Stock `"40"`, Work `"8"` (hours), SalesItem `"10"`, ThresholdQuantity `"5"`. This makes PH#F3 consistent.
  3. Keep `0` in layer 0 and replace it in a quantity layer together with PH#F7.
- **Needs decision:** yes (type value versus per element)

### PH#F3 · High · Exception notification: compared value equals source value, so there is no exception

- **Where:** `VALUES["MeasureType"] = "0"` (l. 41) with `UNITS` H87 (l. 64–65). 2 values in **1 file**:
  - `layer1/ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionNotificationLine/cbc:ComparedValueMeasure` = `0`
  - `layer1/ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionNotificationLine/cbc:SourceValueMeasure` = `0`
- **Why:** ComparedValueMeasure is "The value that was compared with the source value that resulted in the exception", and SourceValueMeasure is "The value used as the basis of comparison". When both are equal (0 = 0), the comparison shows no deviation, so the notification asserts an exception that its own values deny. Also, both being 0 is null-like.
- **Condition:** ComparedValueMeasure ≠ SourceValueMeasure, in the same unit. The difference lies beyond a threshold of the kind ExceptionCriteria states (ThresholdQuantity with ThresholdValueComparisonCode, PH#F6).
- **Options:**
  1. Per element: `SourceValueMeasure` = `100`, `ComparedValueMeasure` = `80`, unit H87 (a forecast of 100 pieces against 80 sold, a 20-piece shortfall). With ExceptionCriteria ThresholdQuantity `5` and `FALLS_BELOW_EXCEPTION_VALUE`, the pair is consistent if read as one exchange.
  2. Keep the measures at layer 0 and set them in the same layer as PH#F2, which decides the threshold.
- **Needs decision:** yes (the values, and whether ExceptionCriteria and ExceptionNotification are meant to match)

### PH#F4 · High · `2000-01-01` predates the identifier schemes used in the same document, and UBL itself

- **Where:** `VALUES["DateType"] = "2000-01-01"` (l. 39). This applies to all 108 dates in **82 files**. The contradiction is concrete in **30 files** that combine a date with an identifier scheme that did not exist in 2000:
  - LEI (ICD 0199) in 22 files: AwardedNotification, CallForTenders, ContractAwardNotice, DigitalAgreement, ExpressionOfInterestRequest, ExpressionOfInterestResponse, GoodsItemItinerary, GuaranteeCertificate, PriorInformationNotice, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationRequest, QualificationApplicationResponse, TenderContract, TenderReceipt, TenderWithdrawal, TendererQualificationResponse, UnawardedNotification, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse, deprecated/TenderStatus, deprecated/TenderStatusRequest
  - JP Corporate Number (0188) in 7 files: AwardedNotification, OrderChange, ProcurementStatusRequest, RequestForQuotation, Tender, TendererQualification, UnawardedNotification
  - JP qualified-invoice T-number in 1 file: InvoiceStatusRequest
  - alphanumeric CNPJ in 3 files: CreditNote, SelfBilledCreditNote, deprecated/FreightInvoice

  (Some files have two schemes.) Examples:
  - `layer1/InvoiceStatusRequest.xml:/InvoiceStatusRequest/cbc:RequestDate` = `2000-01-01`, next to `layer1/InvoiceStatusRequest.xml:/InvoiceStatusRequest/cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` = `T8999999990001`
  - `layer1/CreditNote.xml:/CreditNote/cbc:IssueDate` = `2000-01-01`, next to `layer1/CreditNote.xml:/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `12ABC345000188`
  - `layer1/Tender.xml:/Tender/cbc:IssueDate` = `2000-01-01`, next to `layer1/Tender.xml:/Tender/cac:TendererParty/cac:PartyIdentification/cbc:ID` = `8999999990001`
- **Why:**
  - IssueDate is "The date, assigned by the sender, on which this document was issued". A document issued on 2000-01-01 cannot carry:
    - an LEI (ISO 17442, first issued 2012);
    - a Japanese Corporate Number (assigned from October 2015);
    - a qualified-invoice registration number (system from 1 October 2023);
    - an alphanumeric CNPJ (issued from July 2026, L1 review).
  - UBL 1.0 dates from 2004, and many of these document types are UBL 2.1–2.5 additions. So the dates make every document anachronistic.
  - 2000-01-01 is also the classic sentinel or "epoch" date, so it reads as a null value (IND5). It is a Saturday and New Year's Day, a public holiday in all six locales. Few business documents are issued then.
- **Condition:** Every date is on or after the introduction of every identifier scheme and code list in its document (at the latest: alphanumeric CNPJ, July 2026). It is a business day in the locale and not in the future at publication time.
- **Options:**
  1. A type-level base date `"2026-10-05"` (Monday). It is not a public holiday in US, DE, JP, IN, BR or ZA (it falls after Germany's 3 October and India's 2 October, and before Columbus Day/Sports Day/Brazil's 12 October), and it is after July 2026. Other dates are offsets from it (PH#F5).
  2. A base date per locale. This is unnecessary unless a locale needs it.
  3. Keep `2000-01-01` in layer 0, document it as "clearly a placeholder", and replace it in the next layer. Layer 1 already adds the post-2012 schemes, so the contradiction would then already show in layer 1. Choose this only if the date layer comes right after layer 1.
- **Needs decision:** yes (base date)

### PH#F5 · Medium · One date for every date element: one-day periods at the issue date, no order between dates

- **Where:** `VALUES["DateType"]` (l. 39) together with `FILL["PeriodType"]` (l. 74), which deliberately sets both StartDate and EndDate. 10 periods (20 dates) in **8 files**, plus 8 other non-issue dates in **8 files**:
  - `layer1/Forecast.xml:/Forecast/cbc:IssueDate` = `2000-01-01` and `layer1/Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:StartDate` = `2000-01-01`, `layer1/Forecast.xml:/Forecast/cac:ForecastPeriod/cbc:EndDate` = `2000-01-01`
  - `layer1/ExceptionNotification.xml:/ExceptionNotification/cac:ExceptionObservationPeriod/cbc:EndDate` = `2000-01-01`
  - `layer1/ItemInformationRequest.xml:/ItemInformationRequest/cac:ItemInformationRequestLine/cac:Period/cbc:StartDate` = `2000-01-01`
  - `layer1/TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cac:EffectivePeriod/cbc:EndDate` = `2000-01-01`
  - `layer1/ForecastRevision.xml:/ForecastRevision/cac:ForecastRevisionLine/cbc:SourceForecastIssueDate` = `2000-01-01` (the same as the revision's own IssueDate)
  - `layer1/AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cbc:AwardDate` = `2000-01-01`
  - `layer1/TenderReceipt.xml:/TenderReceipt/cbc:RegisteredDate` = `2000-01-01`
  - The other non-issue dates are AwardDate in ContractAwardNotice, TenderContract and UnawardedNotification, `QualificationResolution/ResolutionDate` (TendererQualificationResponse) and `InvoiceStatusRequest/RequestDate`.
- **Why:**
  - Each period has its own definition, and the definitions imply a position relative to the issue date:
    - ForecastPeriod: "The period to which the Forecast applies", normally after the issue date (a forecast);
    - ExceptionObservationPeriod: "The period of time during which the exceptions are observed", and ActivityPeriod: "The period covered by this Product Activity report", both before or up to the issue date (observed or reported);
    - ValidityPeriod: "The period of time during which the Exception Criteria is valid", and EffectivePeriod: "during which this profile is effective", both starting at or after the issue date and lasting some time.
  - With one date everywhere, none of these relations can be seen. A forecast that covers only its own issue day, and a revision of a forecast issued the same day (SourceForecastIssueDate "The date on which the forecast modified by this revision was generated"), are possible but not typical.
  - StartDate = EndDate is a valid one-day period, so it is not a contradiction. But a one-day period makes the FILL decision's purpose (a period is bounded, IND6) invisible.
- **Condition:** For each document: start ≤ end; observed or reported periods end ≤ IssueDate; forecast, validity and effective periods start ≥ IssueDate; AwardDate, ResolutionDate and the source forecast's IssueDate ≤ IssueDate; a line period lies within the header period (ItemInformationRequest).
- **Options:**
  1. A per-element offset table from the base date D (PH#F4):
     - IssueDate, RequestDate, RegisteredDate: D;
     - AwardDate, ResolutionDate: D − 3;
     - SourceForecastIssueDate: D − 7;
     - Forecast periods: D + 7 to D + 34;
     - Validity, effective and the TradeItemLocationProfile periods: D to D + 364;
     - Observation and activity periods: D − 28 to D − 1;
     - ItemInformationRequest periods: header D − 28 to D − 1, line the same or within it;
     - RetailEvent period: D + 14 to D + 20.
  2. Only make periods longer (StartDate D, EndDate D + 27) and keep everything else at D. This is simpler, but forecasts and observations still sit on the wrong side of the issue date.
- **Needs decision:** yes (offset table)

### PH#F6 · High · Codes that contradict their own definitions: ThresholdValueComparisonCode and AdmissionCode

- **Where:** `VALUES["CodeType"] = "X"` (l. 39). 2 values in **2 files**:
  - `layer1/ExceptionCriteria.xml:/ExceptionCriteria/cac:ExceptionCriteriaLine/cbc:ThresholdValueComparisonCode` = `X`
  - `layer1/TendererQualificationResponse.xml:/TendererQualificationResponse/cac:QualificationResolution/cbc:AdmissionCode` = `X`
- **Why:**
  - ThresholdValueComparisonCode: the definition itself enumerates the values: "Type of comparison to be carried out in reference to the set threshold. Allowed values are: EXCEEDS_EXCEPTION_VALUE FALLS_BELOW_EXCEPTION_VALUE". `X` is outside the allowed values UBL itself states.
  - AdmissionCode is a Code, but its definition reads like an Indicator: "An indicator that the economic operator has been accepted into the tendering process (true) or rejected from the tendering process (false)". `X` is neither, and the response's central statement (admitted or not) is left without meaning.
- **Condition:** The value is one the definition admits.
- **Options:**
  - ThresholdValueComparisonCode: `EXCEEDS_EXCEPTION_VALUE` or `FALLS_BELOW_EXCEPTION_VALUE`. Pick the one that fits PH#F3 (option 1 there: `FALLS_BELOW_EXCEPTION_VALUE`). UBL gives no list identifier, so no listID; the values come from the definition (they originate in GS1/VICS CPFR, not verified).
  - AdmissionCode:
    1. `true` (admitted), taking the definition literally. An admission needs no further reason, whereas `false` would leave a rejection without the reason elements. This states a real answer, as the generator avoids for TenderingCriterionResponse (FILL l. 132–136). But AdmissionCode is required (cardinality 1), so some answer must be given.
    2. A code from a real list, if one is found (eForms has no direct equivalent known to me).
    3. Record the Code-vs-Indicator mismatch as a finding for the OASIS UBL TC either way.
- **Needs decision:** yes

### PH#F7 · Medium · Quantities without unitCode: the unit is implied by absence (IND6)

- **Where:** `build()` l. 349–352 applies `UNITS` only where `unitCode` is a *required* attribute (Measure). QuantityType's unitCode is optional, so the 7 quantities of PH#F2 have none. Examples:
  - `layer1/WorkReport.xml:/WorkReport/cac:WorkReportLine/cbc:Quantity` = `0` (no unitCode, and the line has no Item that could suggest a unit)
  - `layer1/deprecated/StockAvailabilityReport.xml:/StockAvailabilityReport/cac:StockAvailabilityReportLine/cbc:Quantity` = `0`
- **Why:** Quantity.Type is "A counted number of non-monetary units". Without unitCode, the reader must assume the unit. For a work report the assumption could be hours, days or tasks; for an item, pieces, cases or pallets. IND6 forbids meaning that comes from absence. It is the same reasoning the generator applies to Measure ("No default: a Measure not listed here stops the build", l. 59–60).
- **Condition:** Every Quantity carries a unitCode from UN/ECE Recommendation 20 (the UBL default UnitOfMeasureCode list), chosen per element.
- **Options:**
  1. Extend `UNITS` to optional unitCode on QuantityType and keep the "no default, stop the build" rule:
     - `H87` (piece) for InstructionForReturnsLine, InventoryReportLine, StockAvailabilityReportLine, SalesItem and ThresholdQuantity. This is the same unit as the ExceptionNotification measures.
     - `HUR` (hour) for WorkReportLine.

     `UNITS` is keyed by element name, and `Quantity` occurs under several parents, so the key would need to be `Parent/Element` (e.g. `"WorkReportLine/Quantity": "HUR"`).
  2. `C62` (one) everywhere, which is neutral but says little.
- **Needs decision:** yes (small: H87/HUR per element versus C62)

### PH#F8 · Medium · Time `00:00:00` without offset: midnight boundary, time zone implied by absence

- **Where:** `VALUES["TimeType"] = "00:00:00"` (l. 40). 7 values in **7 files**: IssueTime in GoodsItemItinerary, RequestForQuotation, TransportProgressStatus, TransportProgressStatusRequest and TransportServiceDescriptionRequest; TenderReceipt/RegisteredTime; ForecastRevisionLine/SourceForecastIssueTime. Examples:
  - `layer1/TenderReceipt.xml:/TenderReceipt/cbc:RegisteredTime` = `00:00:00`
  - `layer1/TransportProgressStatus.xml:/TransportProgressStatus/cbc:IssueTime` = `00:00:00`
- **Why:**
  - IssueTime is "The time, assigned by the sender, at which this document was issued". Midnight is the day boundary (is 00:00:00 on D the end of D − 1?), and it is the usual default for "time unknown", so it is null-like (IND5).
  - xsd:time without an offset leaves the time zone to the reader. The six locales span UTC−5 to UTC+9, which is meaning implied by absence (IND6).
  - The time matters most for TenderReceipt: the registration time proves a tender arrived before the deadline.
- **Condition:** A time within business hours, with an explicit offset. For ForecastRevision, the source forecast's date+time is before the revision's own issue.
- **Options:**
  1. `"09:30:00"` plus the locale's offset on the base date, kept in a table beside `LOCALES`:
     - US `-04:00` (America/New_York, EDT on 2026-10-05);
     - DE `+02:00` (CEST);
     - JP `+09:00`;
     - IN `+05:30`;
     - BR `-03:00`;
     - ZA `+02:00`.
  2. `"09:30:00Z"` (UTC) everywhere. This is simpler and unambiguous, but less natural locally.
  3. Keep `00:00:00` in layer 0 and set times in the date layer.
- **Needs decision:** yes

### PH#F9 · Medium · Identifier `X` everywhere: references equal the document's own ID, and distinct things share one ID

- **Where:** `VALUES["IdentifierType"] = "X"` (l. 40). 166 values in **94 files**:
  - 79 document IDs;
  - 13 ContractFolderIDs;
  - 28 line IDs (PH#F16);
  - 16 references to other documents, in **16 files**, all `X`.
  - 57 files contain two or more different identifiers with the value `X`.

  References whose value equals the document's own ID:
  - `layer1/deprecated/AttachedDocument.xml:/AttachedDocument/cbc:ParentDocumentID` = `X`, and `layer1/deprecated/AttachedDocument.xml:/AttachedDocument/cbc:ID` = `X`
  - `layer1/UtilityStatement.xml:/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `X`, and `layer1/UtilityStatement.xml:/UtilityStatement/cbc:ID` = `X`
  - `layer1/OrderResponse.xml:/OrderResponse/cac:OrderReference/cbc:ID` = `X`, and `layer1/OrderResponse.xml:/OrderResponse/cbc:ID` = `X`
  - `layer1/GoodsItemItinerary.xml:/GoodsItemItinerary/cbc:TransportExecutionPlanReferenceID` = `X`, and `layer1/GoodsItemItinerary.xml:/GoodsItemItinerary/cbc:ID` = `X`
  - `layer1/ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:GoodsItemPassportID` = `X`, and `layer1/ProofOfReexportationRequest.xml:/ProofOfReexportationRequest/cbc:ID` = `X`
  - `layer1/ForecastRevision.xml:/ForecastRevision/cac:ForecastRevisionLine/cbc:RevisedForecastLineID` = `X`, and `layer1/ForecastRevision.xml:/ForecastRevision/cac:ForecastRevisionLine/cbc:ID` = `X`
  - The others: CatalogueDeletion, CatalogueItemSpecificationUpdate, CataloguePricingUpdate, InvoiceStatusRequest, InvoiceStatusResponse, OrderCancellation, OrderChange, ProofOfReexportation, ProofOfReexportationReminder, deprecated/EnquiryResponse, deprecated/OrderResponseSimple.

  Many distinct identifiers in one document (CertificateOfOrigin, five):
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cbc:ID` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cbc:DocumentID` = `X`
- **Why:**
  - ParentDocumentID is "The Identifier of the parent document". UtilityStatement/ParentDocumentReference is "A reference to the parent Invoice or Credit Note". With the same value as the document's own ID, both read as "this document is its own parent". It is not a formal contradiction (IDs are only unique per sender and type), but it is exactly the ambiguity an example should avoid.
  - An identifier is meant to distinguish. Five different things all identified `X` in one certificate cannot be told apart.
  - Across the set the uniform `X` makes references *match by accident*. For example, `layer1/DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `X` equals Order's line ID `X`. A reader cannot tell whether the set is meant to relate.
- **Condition:**
  - Within a document, distinct identified things have distinct values.
  - No reference equals the referencing document's own ID unless it really is a self-reference.
  - If the set is meant to relate, each reference equals the ID of the document in the set that it refers to. If not, it equals none.
- **Options:**
  1. A per-element rule: document ID = an abbreviation of the type plus a number, e.g. `INV-0001`, `ORD-0001`, `OR-0001`. Reference elements take the referenced type's ID: OrderReference/ID = `ORD-0001`, ParentDocumentReference in UtilityStatement = `INV-0001`, InvoiceDocumentReference = `INV-0001`, TransportExecutionPlanReferenceID = the TransportExecutionPlan's ID. This makes the 101 documents one coherent set. It needs a table of reference element → referenced document type, about 16 entries.
  2. Distinct values without cross-document intent: own ID `<DocType>-1`, every other identifier `<Element>-1` (e.g. `OriginalJobID-1`). Unambiguous within a document, no claim across documents. Mechanical: the element name is known in `build()`.
  3. Keep `X` in layer 0 and introduce identifiers in a "references" layer. ContractFolderID stays one shared value for all procurement documents, if they are meant to be one procedure (currently they are, by accident).
- **Needs decision:** yes (related set or not)

### PH#F10 · Medium · Sequence and version identifiers `X` cannot be sequenced

- **Where:** `VALUES["IdentifierType"]` (l. 40). 5 values in **5 files**:
  - `layer1/OrderChange.xml:/OrderChange/cbc:SequenceNumberID` = `X`
  - `layer1/ForecastRevision.xml:/ForecastRevision/cbc:SequenceNumberID` = `X`
  - `layer1/DigitalAgreement.xml:/DigitalAgreement/cbc:VersionID` = `X`
  - `layer1/GoodsItemItinerary.xml:/GoodsItemItinerary/cbc:VersionID` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `X`
- **Why:** OrderChange/SequenceNumberID is "The Order Change Sequence Number assigned by the Buyer to ensure the proper sequencing of changes". ForecastRevision/SequenceNumberID is "A sequence number, to ensure the proper sequencing of revisions". VersionID "Identifies a version … in order to distinguish updates". A sequence number must be orderable, and `X` is not.
- **Condition:** Sequence numbers are positive integers; a first change or revision is `1`. Versions follow a version convention.
- **Options:** SequenceNumberID `1` (the first change or revision), VersionID `1` (or `1.0`), OriginalJobID per PH#F9. As per-element values in the new table.
- **Needs decision:** no

### PH#F11 · Medium · SequenceNumeric `0`: not an ordinal, and two endorsements share one position

- **Where:** `VALUES["NumericType"] = "0"` (l. 41). 3 values in **2 files**:
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cbc:SequenceNumeric` = `0`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `0`
  - `layer1/GoodsItemItinerary.xml:/GoodsItemItinerary/cac:TransportationSegment/cbc:SequenceNumeric` = `0`
- **Why:**
  - EndorserParty/SequenceNumeric is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". Two endorsers at the same position make the order undefined. TransportationSegment/SequenceNumeric is "the order of this segment in the sequence of transportation segments".
  - Position 0 is unusual for an order "in the sequence"; ordinals in UBL documents conventionally start at 1.
- **Condition:** Sequence numbers start at 1 and are distinct among the things they order. If the application's endorser and the issuer endorsement's endorser are the same party, they have the same number on purpose, and their names and identifiers say so.
- **Options:**
  1. A per-element rule: SequenceNumeric = position among siblings of the same kind in the document, starting at 1. That gives CoO `1` and `2`, and the segment `1`.
  2. If the issuer is meant to be the application's (only) endorser, use `1` for both and make the parties visibly the same (PH#F15).
- **Needs decision:** yes (CoO: one endorser or two)

### PH#F12 · Medium · Code `X` without listID in 11 more elements; one has a real list

- **Where:** `VALUES["CodeType"] = "X"` (l. 39). FILL comment l. 121–124 ("Its code list is left to the code-list layer"). 11 values in **9 files** (besides PH#F6):
  - SupplyChainActivityTypeCode (ProductActivity)
  - EndorserParty/RoleCode ×2 (CertificateOfOrigin)
  - ForecastPurposeCode, ForecastLine/ForecastTypeCode (Forecast)
  - ProofOfReexportationReminder/ProcedureCode
  - Response/ResponseCode (InvoiceStatusResponse)
  - RetailEventStatusCode
  - TransportServiceCode ×2 (GoodsItemItinerary, TransportServiceDescriptionRequest)
  - UtilityStatementTypeCode

  Examples:
  - `layer1/InvoiceStatusResponse.xml:/InvoiceStatusResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode` = `X`
  - `layer1/Forecast.xml:/Forecast/cac:ForecastLine/cbc:ForecastTypeCode` = `X`
  - `layer1/TransportServiceDescriptionRequest.xml:/TransportServiceDescriptionRequest/cac:TransportationService/cbc:TransportServiceCode` = `X`
- **Why:**
  - None of these 13 code elements has a UBL default code list, so phase 2 passes on `X`. Each is a CodeType with no listID, and `X` means nothing in any list: a reader cannot decode it.
  - ResponseCode in an invoice status response is "A code signifying the type of response". A response type of `X` leaves the reply's content undefined: the document answers nothing.
  - ForecastTypeCode's definition gives its own examples ("BASE PROMOTIONAL SEASONAL TOTAL"), so a meaningful value costs nothing.
- **Condition:** Each code comes from a named list (listID, plus listAgencyID where useful) whose meaning fits the element, or from the definition's own examples where UBL gives them.
- **Options:**
  1. A code-list layer (a new `LAYERS` entry) with a per-element table `{element: (code, listID)}`:
     - ResponseCode: `AB` (message acknowledgement) or `IP` (in process), listID `UNCL4343` (UN/EDIFACT 4343 Response type code, as used for invoice responses in practice);
     - ForecastTypeCode: `TOTAL` (definition example, no listID);
     - TransportServiceCode: a UN/EDIFACT code for door-to-door or port-to-port service, if one is confirmed (see Not verified);
     - EndorserParty/RoleCode: from the definition's examples ("issuer, embassy, insurance") a role code for the issuer, list to be chosen (UN/EDIFACT 3035 Party function code qualifier is a candidate, not verified);
     - ForecastPurposeCode, SupplyChainActivityTypeCode, RetailEventStatusCode, ProcedureCode, UtilityStatementTypeCode: there is no known real list, so they stay `X` until one is chosen.
  2. Keep `X` in layer 0 (it does say "a code, not yet chosen") and do all of this in the code-list layer, as FILL already intends. Only ResponseCode is urgent, because it is the document's answer.
- **Needs decision:** yes (lists per element)

### PH#F13 · Medium · AttachedDocument embeds one zero byte as `application/octet-stream`

- **Where:** `VALUES["BinaryObjectType"] = "AA=="` (l. 37), `ATTRS["mimeCode"]` (l. 47), with the generator's own open point (l. 44–46). 1 value in **1 file**:
  - `layer1/deprecated/AttachedDocument.xml:/AttachedDocument/cac:Attachment/cbc:EmbeddedDocumentBinaryObject` = `AA==`
  - `layer1/deprecated/AttachedDocument.xml:/AttachedDocument/cac:Attachment/cbc:EmbeddedDocumentBinaryObject/@mimeCode` = `application/octet-stream`
- **Why:**
  - EmbeddedDocumentBinaryObject is "A binary large object containing an attached document", and AttachedDocument is "a document of any kind to be packaged with" another. One zero byte is not a document; it is the binary form of a null value (IND5), as the generator comment admits.
  - `application/octet-stream` says "unknown type". It is valid (it is in the UBL default BinaryObjectMimeCode list), but a reader cannot open the attachment as anything.
- **Condition:** The bytes are a real, small, valid document whose media type the mimeCode states exactly.
- **Options:**
  1. A 1×1 grey PNG, `image/png`, 67 bytes (checked: valid PNG signature, IHDR/IDAT/IEND with correct CRCs). Base64: `iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACklEQVR4nGP4DwABAQEAsTj2FAAAAABJRU5ErkJggg==`. It is the smallest real content, and the same value can serve Graphic/Picture (PH#F19). An image is a plausible attachment, e.g. a scanned signature.
  2. A minimal one-page PDF, `application/pdf`, about 300–400 bytes as a fixed byte string in the generator. This is the most typical attachment for AttachedDocument (a PDF rendering of the parent document), but longer.
  3. `text/plain`, `WA==` (the letter X). Consistent with the Text placeholder and tiny, but still a filler.

  In each case, ParentDocumentID should then name a real parent (PH#F9). Optionally add `@filename` (e.g. `X.png`) so the attachment can be saved; it is optional in UBL.
- **Needs decision:** yes

### PH#F14 · Medium · Text `X`: descriptions, reasons and statuses that say nothing

- **Where:** `VALUES["TextType"] = "X"` (l. 42). 27 values in **26 files**:
  - Item/Description: 20 values in 20 files (FILL l. 90–94)
  - CancellationNote: OrderCancellation, FulfilmentCancellation
  - CertificateOfOriginApplication/CertificateType
  - Endorsement/ApprovalStatus
  - DigitalProcess/Description: DigitalAgreement, DigitalCapability
  - ResponseValue/Response (QualificationApplicationResponse)

  Examples:
  - `layer1/Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `X`
  - `layer1/OrderCancellation.xml:/OrderCancellation/cbc:CancellationNote` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:CertificateType` = `X`
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cbc:ApprovalStatus` = `X`
  - `layer1/QualificationApplicationResponse.xml:/QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:Response` = `X`
- **Why:**
  - FILL adds Item/Description because "an item of trade … includes a generic description". `X` describes no item, so the FILL decision is defeated by its own placeholder.
  - CancellationNote is "The (general) reason for cancellation"; `X` is no reason.
  - CertificateType's definition lists the values: "The type of CoO being applied for (Ordinary, Re-export, Commonwealth Preferential, etc.)".
  - ApprovalStatus is "The status of this endorsement".
  - A one-letter text is not null in the IND5 check, but it is a filler in the sense of the brief.
  - Language: TextType has an optional `languageID`. A real English text in a JP or BR document leaves the language to be guessed (IND6); `X` avoids that only by saying nothing.
- **Condition:** Each text says what its definition asks, in a language the document states.
- **Options:**
  1. Per-element English texts with `languageID="en"` (`en` is in the UBL default LanguageCode list):
     - Item/Description: `Ballpoint pen, blue` (one item for all 20 documents, so the set describes one item);
     - CancellationNote: `Ordered in error`;
     - CertificateType: `Ordinary` (from the definition);
     - ApprovalStatus: `Approved`;
     - DigitalProcess/Description: `Ordering`;
     - ResponseValue/Response: an answer that matches the criterion property it responds to. Its ValidatedCriterionPropertyID is `X` too, and the QualificationApplicationRequest in the set defines no criteria, so this needs a decision on what is answered.
  2. Locale-language texts (e.g. `ja` for JP documents). More faithful to the locale, but needs translations and is harder to read.
  3. Keep `X` in layer 0 (language-neutral, honest as "not chosen"), and add texts in a "content" layer.
- **Needs decision:** yes

### PH#F15 · Medium · PartyName `X`: different parties in one document share one name

- **Where:** `VALUES["NameType"] = "X"` (l. 42) with `FILL["PartyType"]` (l. 86–89). 153 PartyName values in **85 files**. In **60 files**, two or more distinct parties have the same name `X`, while layer 1 gives them different identifiers. Examples:
  - `layer1/Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `X` (ID `999990001`)
  - `layer1/Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `X` (ID `999990002`)
- **Why:** PartyName/Name is "The name of the party", and FILL chose it because "A name stands on its own" as the party's identity. One name with two identifiers is contradictory: by name it is the same party, by ID two parties. In the 11 name-only parties in 6 files (authorities, issuers, L1#F15), the name is the *only* identity, so `X` identifies no one.
- **Condition:** Distinct parties in one document have distinct names. The names are visibly fictitious (no real company), and stable per role across documents if L1#F9's role numbering is adopted.
- **Options:**
  1. A name from the role and the party number `n` already used for identifiers (`generate()` l. 410): e.g. `Buyer Customer 1`, `Seller Supplier 2`, `Contracting Authority 3`, the role split into words, without a legal form (a legal form would claim a registration). Mechanical and readable.
  2. Fictitious company names per locale (e.g. `Beispiel Handel` for DE). More realistic, but needs a reviewed name table and a check against real registers.
- **Needs decision:** yes

### PH#F16 · Low · Line identifiers `X`

- **Where:** `VALUES["IdentifierType"]` (l. 40). 28 line IDs in **28 files** (InvoiceLine, CreditNoteLine, DespatchLine, LineItem, ForecastLine …). Example:
  - `layer1/Invoice.xml:/Invoice/cac:InvoiceLine/cbc:ID` = `X`
- **Why:** "An identifier for this invoice line". Line numbering `1`, `2` … is the universal convention and makes OrderLineReference/LineID matches readable (PH#F9). `X` works, but it reads as a placeholder rather than a first line.
- **Condition:** Line IDs are unique within their document.
- **Options:** Line ID = position of the line, starting at `1`. LineItem/ID (Order, OrderChange, Quotation, RequestForQuotation: "assigned by the buyer") uses the same rule, so DespatchAdvice/DeliveryNote `OrderLineReference/LineID` = `1` matches the Order's line.
- **Needs decision:** no

### PH#F17 · Low · AcceptedIndicator `true`: right choice, but undocumented

- **Where:** `VALUES["IndicatorType"] = "true"` (l. 40). 1 value in **1 file**:
  - `layer1/deprecated/OrderResponseSimple.xml:/OrderResponseSimple/cbc:AcceptedIndicator` = `true`
- **Why:** "Indicates whether the Order is accepted (true) or rejected (false)". It is required, so any value states a real answer, unlike the optional Indicator the generator avoided for TenderingCriterionResponse. `true` is the better choice: `false` would call for RejectionNote ("The reason for rejection if the order was not accepted", 0..n), and its absence would imply "no reason" (IND6). The value is not harmful, but it is a decision taken implicitly by a type-level default.
- **Condition:** Every Indicator value is chosen per element, with its reason in the generator.
- **Options:**
  1. Keep `true` and move it into the per-element table with the comment "accepted: a rejection would need RejectionNote". The type-level default would then raise an error for any new required Indicator, like `UNITS`.
  2. Keep it as is.
- **Needs decision:** yes (small)

### PH#F18 · Low · Other names and identifiers `X`: signatory, location, project, licence plate

- **Where:** `VALUES["NameType"]`/`["IdentifierType"]` (l. 40–42). 7 values in **6 files**:
  - `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `X` (and the application's signatory)
  - `layer1/ProductActivity.xml:/ProductActivity/cac:SupplyChainActivityDataLine/cac:ActivityOriginLocation/cbc:Name` = `X`
  - `layer1/CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:Name` = `X` (and ContractNotice)
  - `layer1/TransportProgressStatus.xml:/TransportProgressStatus/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `X` (and TransportProgressStatusRequest)
- **Why:**
  - FILL chose a signatory's personal name because "A signature needs the person's name" (l. 108–111); `X` is no person.
  - ProcurementProject/Name is "A name of this procurement project".
  - A licence plate `X` is safe (it cannot be a real vehicle), but it is unreadable as a plate.
- **Condition:** Names are readable and visibly fictitious. A plate cannot be a real registration.
- **Options:**
  - Signatory: `Alex Example`.
  - Location: `Store 1`.
  - Project: `Office supplies 2026`.
  - LicensePlateID: keep `X`, or use a pattern no locale issues. Real formats risk real plates, so keeping `X` is defensible.

  All are per-element values.
- **Needs decision:** yes (small)

### PH#F19 · Low · VALUES entries no document exercises

- **Where:** `VALUES` (l. 36–43): DateTimeType `2000-01-01T00:00:00`, PercentType `0`, RateType `0`, ValueType `0`, GraphicType, PictureType, SoundType and VideoType `AA==` occur in **0 files** in layer 0 and layer 1.
- **Why:** These defaults were never tested in context. As soon as a later layer adds an optional element of these types, the build will silently write values with the same problems as above: a DateTime at the sentinel date and midnight (PH#F4/PH#F8); Percent/Rate `0`, which states "no tax" or "no interest", a real and often false statement; and a zero-byte "picture" (PH#F13).
- **Condition:** No type-level default writes a value that PH#F1–F13 rejects.
- **Options:**
  1. Remove the unused entries, so `VALUES[u]` raises `KeyError` and the layer that first needs one must choose per element (the `UNITS` principle).
  2. Set them now by the rules of this review: DateTime = base date + `T09:30:00` + offset; Percent `19`/Rate `1` only per element (no type default); Graphic/Picture = the PNG of PH#F13; Sound/Video with no default.
- **Needs decision:** yes (small)

## Suggested value table

### Amount

| Element | Current | Suggested | Reason |
|---|---|---|---|
| default | `0` | `100` (integer, valid for JPY too), or per currency `100.00` (JPY `100`) | a payment, credit, bid or liability of 0 contradicts the document (PH#F1) |
| PayableAmount | `0` | = sum of line amounts + tax, once lines carry amounts; until then `100` | "The amount of the monetary total to be paid" |
| LiabilityAmount | `0` | e.g. `1000` | a guarantee for nothing is no guarantee |

### Quantity / Measure

| Element | Current | Suggested | Reason |
|---|---|---|---|
| InstructionForReturnsLine/Quantity | `0`, no unit | `2` `H87` | goods being returned (PH#F2, F7) |
| InventoryReportLine/Quantity, StockAvailabilityReportLine/Quantity | `0`, no unit | `40` `H87` | in stock; 0 would mean "out of stock" |
| WorkReportLine/Quantity | `0`, no unit | `8` `HUR` | quantity of work; the unit is otherwise unknowable |
| SalesItem/Quantity | `0`, no unit | `10` `H87` | the quantity the information relates to |
| ExceptionCriteriaLine/ThresholdQuantity | `0`, no unit | `5` `H87` | a threshold beyond which an exception triggers |
| ExceptionNotificationLine/SourceValueMeasure | `0` H87 | `100` H87 | basis of comparison (PH#F3) |
| ExceptionNotificationLine/ComparedValueMeasure | `0` H87 | `80` H87 | must differ from the source value |

### Numeric

| Element | Current | Suggested | Reason |
|---|---|---|---|
| SequenceNumeric (default) | `0` | position among its kind, from `1` | an order in a sequence (PH#F11) |
| CoO EndorserParty ×2 | `0`, `0` | `1`, `2` (or `1`, `1` if the same party) | two endorsements cannot share position 0 |

### Date / Time

| Element | Current | Suggested | Reason |
|---|---|---|---|
| default (IssueDate, RequestDate, RegisteredDate) | `2000-01-01` | base date D = `2026-10-05` | predates LEI, JP CN/T-number, alphanumeric CNPJ, UBL (PH#F4) |
| AwardDate, ResolutionDate | D | D − 3 | formalised before the notice |
| SourceForecastIssueDate | D | D − 7 | the revised forecast came first |
| ForecastPeriod | D…D | D + 7 … D + 34 | a forecast is about the future (PH#F5) |
| ExceptionObservationPeriod, ActivityPeriod, ItemInformationRequest periods | D…D | D − 28 … D − 1 | observed or reported |
| ValidityPeriod, EffectivePeriod, TradeItemLocationProfile/Period | D…D | D … D + 364 | valid or effective from issue |
| RetailEvent/Period | D…D | D + 14 … D + 20 | an announced event |
| default Time | `00:00:00` | `09:30:00` + locale offset (US −04:00, DE +02:00, JP +09:00, IN +05:30, BR −03:00, ZA +02:00) or `09:30:00Z` | midnight is null-like; offset otherwise implied (PH#F8) |
| SourceForecastIssueTime | `00:00:00` | `09:30:00` + offset (on D − 7) | before the revision |
| DateTime (unused) | `2000-01-01T00:00:00` | D + `T09:30:00` + offset, or no default | PH#F19 |

### Identifier

| Element | Current | Suggested | Reason |
|---|---|---|---|
| document cbc:ID | `X` | `<TYPE>-0001` (e.g. `INV-0001`) | distinct from references (PH#F9) |
| references (OrderReference/ID, ParentDocumentID, ParentDocumentReference/ID, InvoiceDocumentReference/ID, TransportExecutionPlanReferenceID, GoodsItemPassportID, catalogue references …) | `X` | the referenced document's ID in the set, or a distinct `<Element>-1` | no self-reference by accident |
| ContractFolderID | `X` | one shared value, e.g. `PROC-2026-001`, if the procurement documents are one procedure | the "process file" they belong to |
| line IDs, LineItem/ID, OrderLineReference/LineID | `X` | `1`, `2` … | PH#F16 |
| SequenceNumberID | `X` | `1` | must be orderable (PH#F10) |
| VersionID | `X` | `1` | distinguishes updates |
| Shipment/ID, Consignment/ID, Endorsement/DocumentID, ReferenceID, OriginalJobID, GoodsItemPassportCounterfoil/ID | `X` | distinct per element (`SHP-1`, `CON-1` …) | distinct things in one document |
| LicensePlateID | `X` | keep `X`, or a format no locale issues | real formats risk real plates |

### Code / Indicator

| Element | Current | Suggested | Reason |
|---|---|---|---|
| default Code | `X` | keep in layer 0; code-list layer per element | no UBL default list for these 13 elements |
| ThresholdValueComparisonCode | `X` | `FALLS_BELOW_EXCEPTION_VALUE` (or `EXCEEDS_…`) | the definition enumerates the allowed values (PH#F6) |
| AdmissionCode | `X` | `true` (definition), or a real list | the definition asks true/false |
| ResponseCode (InvoiceStatusResponse) | `X` | `AB` or `IP`, `listID="UNCL4343"` | the document's answer (PH#F12) |
| ForecastTypeCode | `X` | `TOTAL` | the definition's example |
| AcceptedIndicator | `true` | keep `true`, per element with reason | `false` would need RejectionNote (PH#F17) |

### Text / Name / Binary

| Element | Current | Suggested | Reason |
|---|---|---|---|
| Item/Description | `X` | `Ballpoint pen, blue`, `languageID="en"` | the FILL reason is a description (PH#F14) |
| CancellationNote | `X` | `Ordered in error` | "The reason for cancellation" |
| CertificateType | `X` | `Ordinary` | the definition's example |
| Endorsement/ApprovalStatus | `X` | `Approved` | "The status of this endorsement" |
| DigitalProcess/Description | `X` | `Ordering` | a kind of process |
| ResponseValue/Response | `X` | an answer to a criterion defined in the request | depends on ValidatedCriterionPropertyID |
| PartyName/Name | `X` | role words + n, e.g. `Seller Supplier 2` | distinct parties, distinct names (PH#F15) |
| Contact/Name (signatory) | `X` | `Alex Example` | a person signs |
| Location/Name, ProcurementProject/Name | `X` | `Store 1`, `Office supplies 2026` | readable |
| EmbeddedDocumentBinaryObject | `AA==` `application/octet-stream` | 1×1 PNG `image/png` (67 bytes), or a minimal PDF `application/pdf` | one zero byte is no document (PH#F13) |

## Value dependencies for the next layer

1. **Amounts:**
   - Once lines get amounts: LineExtensionAmount = quantity × price (when both are present), LegalMonetaryTotal/LineExtensionAmount = Σ line amounts, and PayableAmount = Σ lines − allowances + charges + tax − PrepaidAmount.
   - Tax: TaxAmount = TaxableAmount × Percent / 100, rounded to the currency's minor unit (JPY 0 decimals, the other locales 2).
   - All amounts in one document carry the same currencyID (the locale, already true).
   - DebitNote: if a RequestedMonetaryTotal is added, its PayableAmount = the line amount.
2. **Quantities:** a returned, despatched or received quantity ≤ the ordered quantity, if those documents are meant to relate; the unitCode is the same on related lines.
3. **Exceptions:** ExceptionNotification Compared ≠ Source. The deviation lies on the side ThresholdValueComparisonCode names, and is beyond ThresholdQuantity, in the same unit.
4. **Dates, within a document:**
   - Period StartDate ≤ EndDate.
   - Observed or reported periods end ≤ IssueDate; forecast, validity and effective periods start ≥ IssueDate.
   - AwardDate, ResolutionDate and SourceForecastIssueDate+Time are before IssueDate(+IssueTime).
   - A line period lies within its header period (ItemInformationRequest).
   - A due date, if added, is ≥ IssueDate.
   - Every date is ≥ the introduction of every scheme in the document (PH#F4).
5. **Dates, across documents (only if the set relates):** documents follow process order:
   - Order < OrderResponse/OrderChange/OrderCancellation;
   - Order < DespatchAdvice < ReceiptAdvice;
   - Invoice < InvoiceStatusRequest < InvoiceStatusResponse;
   - Invoice < Reminder;
   - Invoice ≤ UtilityStatement;
   - CallForTenders < Tender < TenderReceipt < AwardedNotification;
   - Forecast < ForecastRevision (SourceForecastIssueDate = Forecast's IssueDate);
   - GoodsItemPassport < ProofOfReexportationRequest < ProofOfReexportationReminder.
6. **Identifiers:**
   - Within a document, all identified things are distinct, and no reference equals the document's own ID.
   - If the set relates, each reference equals the referenced document's ID:
     - OrderReference/ID = Order/ID;
     - OrderLineReference/LineID = Order's LineItem/ID;
     - UtilityStatement ParentDocumentReference = Invoice/ID;
     - InvoiceDocumentReference = Invoice/ID;
     - TransportExecutionPlanReferenceID = TransportExecutionPlan/ID;
     - catalogue references = Catalogue/ID;
     - RevisedForecastLineID = Forecast's ForecastLine/ID;
     - ProofOfReexportationRequestDocumentReference = ProofOfReexportationRequest/ID;
     - GoodsItemPassportID and the counterfoil IDs = GoodsItemPassport/ID or its counterfoil;
     - every procurement ContractFolderID is the same value.
   - SequenceNumberID and SequenceNumeric are ordinals from 1.
7. **Parties:** distinct names for distinct identifiers. The same party (same ID) has the same name across documents (combine with L1#F9).
8. **Criteria:** TenderingCriterionResponse/ValidatedCriterionPropertyID must equal a criterion property ID that the QualificationApplicationRequest defines. Today the request defines none, so a criteria layer has to add both sides together.
9. **Attachment:** mimeCode matches the actual bytes. ParentDocumentID (and ParentDocumentTypeCode if added) names the document the attachment belongs to.

## Considered and refuted

- **Locale-driven currency and country values:**
  - `layer1/Statement.xml:/Statement/cbc:DocumentCurrencyCode` = `USD`, `layer1/UtilityStatement.xml:/UtilityStatement/cbc:DocumentCurrencyCode` = `ZAR`, `layer1/CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:IssuingCountry/cbc:IdentificationCode` = `US` and the 11 currencyID attributes are real ISO 4217 / ISO 3166-1 codes in the UBL default lists, consistent per document (also checked in the L1 review).
  - Statement has a DocumentCurrencyCode but no amounts. The element is required, so this is not a filler.
  - The missing tax jurisdiction is L1#F6, not repeated here.
- **Measure unitCode `H87` (piece):** it is in the UBL default UnitOfMeasureCode list ("piece"), and the UNITS comment gives the reason (the compared values count the SupplyItem). A count expressed as a Measure is unusual, but the elements are Measures by definition. Not raised; only the values are (PH#F3).
- **`mimeCode` `application/octet-stream` as a code:** it is in the UBL default BinaryObjectMimeCode list, so it is not invalid. Only its pairing with one zero byte is raised (PH#F13).
- **StartDate = EndDate as a contradiction:** a one-day period is valid; raised only as Medium for the lost ordering (PH#F5).
- **AcceptedIndicator `true` as harmful:** the element is required, and `true` is the choice that needs no further elements (PH#F17, Low).
- **ContractFolderID `X` shared by 13 procurement documents:** this is coherent if they are one procedure. It is raised only as a decision in PH#F9, not as an error.
- **TenderReceipt RegisteredDate = IssueDate:** "the date … on which the Tender Receipt was created" is naturally the issue date; equal values are right.
- **IND5 failures:** none. Every placeholder is non-empty, so the generator's IND5 check passes. The findings concern null-like meaning, not empty content.

## Not verified

- **Introduction dates:** they are from domain knowledge, not fetched: LEI 2012, JP Corporate Number October 2015, qualified-invoice system 1 October 2023, UBL 1.0 2004. The alphanumeric CNPJ date (July 2026) is from the L1 review. The base-date holiday check (2026-10-05 in six locales) is from general calendars, not an official source per country. The US/DE offsets on 2026-10-05 assume DST rules unchanged.
- **UN/EDIFACT 4343:** the codes `AB`/`IP` and their exact names in the current directory. The UNECE site blocks automated access.
- **TransportServiceCode:** no real list was confirmed (UN/EDIFACT 7273 or 8335 are candidates).
- **EndorserParty/RoleCode:** UN/EDIFACT 3035 as a list was not checked.
- **ThresholdValueComparisonCode:** the GS1/VICS CPFR origin of its values.
- **Default code lists:** checked against the 2.4-version genericode files cached by `ubl_model.py` (`~/.cache/ubl-example-review/cl/*-2.4.gc`), not the UBL 2.5 package (not fetched in this session). `en`, `H87`, `HUR`, `C62`, `image/png`, `application/pdf`, `application/octet-stream`, `USD`, `ZAR`, `US` are in those lists. That none of the 13 code elements has a UBL 2.5 default list is inferred from the 11 default lists and from phase 2 passing on `X`.
- **The PNG:** checked structurally in Python (signature, chunk CRCs, zlib stream), not opened in an image viewer. The minimal PDF option was not built.
- **Regeneration:** no suggested value was regenerated or validated against the XSDs, phase 2 or the IND checks. Type-level changes such as `100` and `2026-10-05` are lexically valid for their xsd types.
