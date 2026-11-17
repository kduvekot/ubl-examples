# Review of the values in minimal/layer1, round 3

## Reviewed version

- Run: `20261116T1715Z-round3`, topic: values. Finding IDs VA3#F1 ...
- Source: branch `claude/elegant-franklin-kk2dky`, commit `6f3c96249f32ccee9c469666e3a3e4db6ccca635` (`minimal: UtilityStatement shows its consumption (DM#F116)`). Focus: `git diff 01f8672..6f3c962 -- minimal/` (52 commits).
- Files: `minimal/gen_minimal.py` (1158 lines), `minimal/layer1/*.xml` (93) and `minimal/layer1/deprecated/*.xml` (8); layer0 checked where a value is shared.
- Model: UBL 2.5 OASIS Standard, local package `minimal/.ubl/os-UBL-2.5/`. Definitions are quoted from `xsd/common/UBL-CommonAggregateComponents-2.5.xsd` and `xsd/maindoc/*.xsd` (`ccts:Definition`).
- Reproducibility: a copy of the generator, run in a scratch directory against the same package, produces output byte-identical to the committed `layer0/` and `layer1/` (`diff -r`: no differences; "202 documents, 0 with violations").
- Paths are relative to `minimal/`. Line numbers refer to `gen_minimal.py` at 6f3c962. Every XPath was evaluated with lxml (`cac`/`cbc` as usual, `/*` = the root document element) and selects exactly the value shown.
- Out of scope, not repeated: `ubl-findings.md`, and the round-2 findings, which are processed. Overlap: VA3#F1 and VA3#F3 were also found independently by `meaning-p-z.llm-review.20261116T1711Z-round3.md` (the criterion reference and the Enquiry text). They are listed here because they are value faults. DM3#F107 (the stale KWH comment) is not repeated.

## Findings

### VA3#F1 · High · Regression: the criterion answer refers to a property ID that is not in the document

- **Where:** `layer1/QualificationApplicationResponse.xml` (and `layer0/`, the same):
  - `/*/cac:TenderingCriterion/cac:TenderingCriterionPropertyGroup/cac:TenderingCriterionProperty/cbc:ID` = `TenderingCriterionProperty-631`
  - `/*/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID` = `TenderingCriterionProperty-1`
  - `count(//cbc:ID[. = /*/cac:TenderingCriterionResponse/cbc:ValidatedCriterionPropertyID])` = 0.
- **Cause:** `id_for()` l. 154–155 still hard-codes `"TenderingCriterionProperty-1"`. Commit `5664959` (VA#F1, unique identifiers) renumbered every other identifier to `label-(DOCNO×10+n)` (l. 156–161), so the property became `-631`. At 01f8672 both values were `TenderingCriterionProperty-1` (`git show 01f8672:minimal/layer1/QualificationApplicationResponse.xml`), and round 2 recorded them as consistent.
- **Why:** ValidatedCriterionPropertyID is "An identifier for this item of criterion support"; the generator's own comment says it is "the question in this document" (l. 154, and FILL l. 328–332: "the yes/no property repeated in the same document"). TenderingCriterionProperty/ID is "An identifier to refer to the criterion property". The answer `true` now answers a question that the document does not contain. The check in `check()` cannot see this, because both values are well-formed.
- **Condition:** ValidatedCriterionPropertyID equals the TenderingCriterionProperty/ID of the same document.
- **Options:**
  1. Return the property's own value: for example, look up the ID already assigned to `TenderingCriterionProperty` in the document, or compute `"TenderingCriterionProperty-%d" % (DOCNO * 10 + 1)`. This works only if the property is built first, which it is in schema order.
  2. Post-process in `generate()` (as done for the IssuerEndorsement name): copy the property's ID into ValidatedCriterionPropertyID.
  3. Add a check that every ValidatedCriterionPropertyID equals a TenderingCriterionProperty/ID in its document, so that a renumbering cannot break it again.
- **Needs decision:** no.

### VA3#F2 · Medium · Bills name the pen and a total but no quantity, so the "10 pens" amount reads as the price of one pen

- **Where:** five documents whose line has an Item and whose total comes from AMOUNTS (l. 68–79, "mostly 10 ballpoint pens at a plausible unit price"), but where no quantity is stated:

  | File | Line item (Description) | `/*/cac:LegalMonetaryTotal/cbc:PayableAmount` |
  |---|---|---|
  | `layer1/Invoice.xml` | `/*/cac:InvoiceLine/cac:Item/cbc:Description` = `Kugelschreiber, blau` | `15.00` EUR |
  | `layer1/PurchaseReceipt.xml` | `/*/cac:PurchaseReceiptLine/cac:Item/cbc:Description` = `Kugelschreiber, blau` | `15.00` EUR |
  | `layer1/CreditNote.xml` | `/*/cac:CreditNoteLine/cac:Item/cbc:Description` = `Caneta esferográfica, azul` | `75.00` BRL |
  | `layer1/SelfBilledCreditNote.xml` | `/*/cac:CreditNoteLine/cac:Item/cbc:Description` = `Caneta esferográfica, azul` | `75.00` BRL |
  | `layer1/SelfBilledInvoice.xml` | `/*/cac:InvoiceLine/cac:Item/cbc:Description` = `Ballpoint pen, blue` | `270.00` ZAR |

  `count(//cbc:InvoicedQuantity | //cbc:CreditedQuantity | //cac:PurchaseReceiptLine/cbc:Quantity)` = 0 in all five.
- **Why:** The amounts were made plausible as "10 × unit price" (VA#F6). But the 10 appears only in the generator comment. A reader of the document sees one line, one blue ballpoint pen and a total, and because no quantity is stated, reads it as one pen: EUR 15, BRL 75 or ZAR 270 for a single ballpoint pen. That is the implausibility VA#F6 set out to remove, now implied by absence (IND6). UBL has the elements for this: InvoicedQuantity "The quantity (of items) on this invoice line", CreditedQuantity "The quantity of items credited in this credit note line", PurchaseReceiptLine/Quantity "The quantity (of items) on this purchase receipt line". The generator already gives quantities to the lines that despatch, deliver, order or quote (FILL l. 437–445; Quotation states `10` H87 next to BRL 75.00, which is consistent). Documents without an Item (DebitNote, Reminder, Statement, RemittanceAdvice) are not affected.
- **Condition:** Where a line names the item and the total is "10 × unit price", the document states the quantity 10 H87, or the amount is the price of one unit.
- **Options:**
  1. FILL `InvoiceLineType: {cbc:InvoicedQuantity}`, `CreditNoteLineType: {cbc:CreditedQuantity}` (next to `cac:Item`), `PurchaseReceiptLineType: {cbc:Quantity}`, with QUANTITY_UNITS H87. FreightInvoice uses InvoiceLineType too, so it needs its own unit and value there (one road transport: e.g. `1` with unit C62, or a distance or weight).
  2. Make the amount the price of one pen in these five (EUR 1.50, BRL 7.50, ZAR 27.00), and record that the bills are for one pen.
  3. Keep the current values and record why the quantity is not needed for "minimal".
- **Needs decision:** yes.

### VA3#F3 · Medium · Enquiry and EnquiryResponse speak of "the item", but the document has no item

- **Where:**
  - `layer1/deprecated/Enquiry.xml`: `/*/cbc:Description` = `Is the item available from stock?` (US, en). `count(//cac:Item)` = 0, and no other element names a product.
  - `layer1/deprecated/EnquiryResponse.xml`: `/*/cbc:Description` = `Ja, der Artikel ist ab Lager lieferbar.` (DE).
  - Source: TEXTS l. 735–739, added in `775897a` (DM#F126).
- **Why:** Enquiry is "A document sent by a requestor to a responder requesting information about a particular business process"; its Description is the "Free-form text-only description ... conveying information that is not contained explicitly in other structures". The definite "the item" / "der Artikel" refers back to something, but neither document (nor its references, which point outside the set) names an item. So the question cannot be answered from the document alone, and the answer cannot be checked against it. The rest of the set uses one item, the blue ballpoint pen, so it can be named in the text without adding elements.
- **Condition:** The enquiry text says which item it asks about, and the response repeats it.
- **Options:**
  1. Name the item in the text: "Is the blue ballpoint pen available from stock?" / "Ja, der blaue Kugelschreiber ist ab Lager lieferbar." (pt-BR "A caneta esferográfica azul está disponível em estoque?", ja "Ao no bōrupen wa zaiko ga arimasu ka?"). These are new terms and go to the translators.
  2. Keep "the item" and add a reference to it (AdditionalDocumentReference to a catalogue line). That is heavier and less minimal.
- **Needs decision:** yes (the wording).

### VA3#F4 · Low · Brazilian WorkReport names the provider of work "Vendedor" and its client "Comprador"

- **Where:** `layer1/WorkReport.xml` (BR): `/*/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Vendedor Exemplo 1001`, `/*/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Comprador Exemplo 1002`; the line is `Manutenção de equipamentos de escritório`, 10 HUR. Source: ROLE_NAMES l. 675–676 (generic per role).
- **Why:** In this document the roles are defined as "The party providing the work" and "The party receiving the work". The translation brief asks for "the term a business ... professional in that country would use for that role, not a literal translation". For a maintenance service in Brazil, the usual terms are *prestador (de serviços)* and *tomador (de serviços)* or *contratante*; *vendedor*/*comprador* belong to the sale of goods. The generator already overrides a generic role per document where the meaning differs (`StockAvailabilityReport/InventoryReportingParty` → Branch, DM#F118). German "Verkäufer/Käufer" and English "Seller/Buyer" have the same issue in principle, but they are not used in this document. (Not verified against a native speaker. This is a terminology judgement.)
- **Condition:** Role names in WorkReport fit "providing / receiving the work" in the locale's language.
- **Options:**
  1. Add `WorkReport/SellerSupplierParty` and `WorkReport/BuyerCustomerParty` to ROLE_NAMES (en "Service Provider"/"Client", de "Dienstleister"/"Auftraggeber", pt-BR "Prestador de Serviços"/"Tomador de Serviços", ja "Ukeoinin"/"Itakusha" or similar), and send them to the translators.
  2. Keep the generic names and record that role names follow the UBL element name, not the document's definition.
- **Needs decision:** yes.

### VA3#F5 · Low · UtilityStatement: 350 kWh "a month, household", but the period is not stated and the receiver is a D-U-N-S business

- **Where:** `layer1/UtilityStatement.xml` (ZA):
  - `/*/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `350` (`unitCode="KWH"`)
  - `/*/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `362242799` (`schemeID="0060"`)
  - `count(//cac:MainPeriod | //cac:Period)` = 0.
  - Sources: QUANTITY_VALUES l. 260–261 ("# a month, household"), PARTY_SCHEMES l. 540 ("a utility customer is often not tax-registered" → D-U-N-S).
- **Why:**
  - TotalMeteredQuantity is "The total quantity consumed, as calculated from meter readings". A consumption total only means something over a period. The month is the generator's reason, but nothing in the document states it. The only period UBL offers here is Consumption/MainPeriod, which brings a required LegalMonetaryTotal. Read charitably, the period is that of the parent invoice (ParentDocumentReference, "A reference to the parent Invoice or Credit Note"), which lies outside the set.
  - The stated household also conflicts with the receiver's identification: D-U-N-S numbers identify businesses (here one of D&B's fictitious test companies), not households.
  - The value itself is plausible for either case.
- **Condition:** The reason for the value agrees with the document: the consumer type matches the receiver's identification, and the period is stated or explicitly taken from the parent invoice.
- **Options:**
  1. Change the comment to "a month of a small business; the period is the parent invoice's". This changes no value.
  2. Add `cac:Consumption` with `cac:MainPeriod` (and its required LegalMonetaryTotal, which needs an amount in AMOUNTS).
- **Needs decision:** yes (option 1 or 2).

### VA3#F6 · Low · ProcurementProject/Name: suffix numbered differently from every other value, and "2026" for a notice of future buying

- **Where:**
  - `layer1/CallForTenders.xml`: `/*/cac:ProcurementProject/cbc:Name` = `Office supplies 2026 (6)`, next to `/*/cbc:ContractFolderID` = `ContractFolderID-61`.
  - `layer1/ContractNotice.xml`: `Office supplies 2026 (15)` (ContractFolderID-151).
  - `layer1/PriorInformationNotice.xml`: `Office supplies 2026 (54)`, `/*/cbc:IssueDate` = `2026-08-12`.
  - Source: `name_for()` l. 776–777, `"%s (%d)" % (..., DOCNO)`.
- **Why:**
  - Every other value that is unique across the set uses `DOCNO×10+n` (party names, identifiers). The project name alone uses `DOCNO`, so in one document the numbers disagree (6 vs 61). In parentheses the number also reads like a lot or a version of the project, not like the "Example ... k" convention. NAMES says these names are "visibly fictitious", but "Office supplies 2026 (6)" is the only name with no Example/Beispiel/Exemplo/Sanpuru marker.
  - A Prior Information Notice is "A document used by a contracting party to declare the intention to buy goods, services, or works during a specified period". Issued on 12 August 2026 for "2026" (the PIN is US; the US federal fiscal year 2026 ends on 30 September 2026), it announces purchases for a period that is mostly over. "2027" would fit an advance notice.
- **Condition:** The project name follows the set's numbering and marker convention, and its year fits the issue date.
- **Options:**
  1. `"Example Office Supplies 2027 %d" % (DOCNO*10 + 1)` (and the same pattern in de/pt-BR/ja). The translators are needed only for the word order.
  2. Keep "2026" for CallForTenders and ContractNotice (current-year buying) and use "2027" only in the PIN.
  3. Keep the values and record why.
- **Needs decision:** yes.

## Checked and consistent

Round-2 values findings, status at 6f3c962:
- VA#F1 (unique identifiers): fixed, except the regression VA3#F1.
- VA#F2 and VA#F3: fixed. The IssuerEndorsement EndorserParty name equals the IssuerParty name (`Example Issuer 123`), and the signatories differ (`Alex Example` / `Sam Example`).
- VA#F4: fixed (ON_HAND, SALES).
- VA#F5: fixed (awards on Monday 2026-08-10).
- VA#F6: fixed (amounts per document; but see VA3#F2).
- VA#F7: fixed (Fornecedor).
- VA#F8: fixed (`pt-BR`, `ja-Latn-hepburn`).
- VA#F9: fixed (LineID and RevisedForecastLineID `1`).
- VA#F10: fixed.

- **Locale consistency (all 101 files, scripted):** every `currencyID`, DocumentCurrencyCode, Country/IdentificationCode and RegistrationNationalityID matches the document's locale. Every `languageID` is the locale's language, except the BR-only register name "Cadastro Nacional da Pessoa Jurídica". No `@UNCHOSEN@`, `X`, `@CURRENCY@` or `@COUNTRY@` remains in layer0 or layer1.
- **Amounts:** minor units are right: JPY 0 decimals (`Tender` `500000`), INR/BRL/ZAR/EUR/USD two. Within a document, line = total: DebitNote LineExtensionAmount = PayableAmount = 270.00 ZAR; Reminder DebitLineAmount = PayableAmount = 16.00 USD; Statement BalanceAmount = TotalBalanceAmount = 16.00 USD; RemittanceAdvice DebitLineAmount = TotalPaymentAmount = 15.00 EUR. Quotation 10 H87 for BRL 75.00 is consistent. Unit prices are plausible and mutually consistent at August-2026 orders of magnitude: EUR 1.50 ≈ USD 1.60 ≈ ZAR 27 ≈ BRL 7.50 per pen. The other amounts are plausible too: CataloguePricingUpdate one pen BRL 7.50, FreightInvoice road freight BRL 1,200.00, GuaranteeCertificate bid bond INR 50,000.00, Tender JPY 500,000 for office supplies.
- **Dates:** all IssueDates are 2026-08-12 (Wednesday). Observed and reported periods run 2026-07-15 to 2026-08-11, forecasts 2026-08-19 to 2026-09-15, and the SourceForecastIssueDate 2026-08-05 comes before the revision. Validity and effective periods run 2026-08-12 to 2027-08-11. The RetailEvent runs from 2026-08-26 to 2026-09-01: two weeks ahead and inside India's monsoon season, and the status `PLANNED` agrees. AwardDate and ResolutionDate 2026-08-10 (Monday) fall in JP and IN documents only, so not on South Africa's observed Women's Day. Japan's Mountain Day (11 August) is not used.
- **Times:** 09:30 with the locale's August offset in every Time and DateTime (DE +02:00, JP +09:00, IN +05:30, BR −03:00).
- **Quantities, units, measures:** H87 for pens, HUR for WorkReportLine ("The quantity of work reported in this line"), ANN for OperatingYearsQuantity 12, KWH for the electricity statement (matches `ELECTRICITY`), KGM 12000 for Shipment/GrossWeightMeasure ("goods plus packaging plus transport equipment"; plausible for a loaded container). ExceptionNotification compared 8 < source 10 with ON_HAND agrees with ExceptionCriteria FALLS_BELOW 10 ON_HAND. Phase-2 code-list validation passes.
- **Codes:**
  - New since round 2: `Revised` (UBL default LineStatusCode list), `IN_TRANSIT` ("the overall status of transport service execution"), `PORT_TO_PORT` for a segment and `DOOR_TO_DOOR` for a whole service (both from the definition's examples), `ON_HAND`/`SALES`.
  - Earlier codes are unchanged and still fit.
  - ProcedureCode `TEMPORARY_ADMISSION` is in a ZA document (an ATA country).
- **Identifiers:** non-party identifiers are `label-(DOCNO×10+n)` and unique across the set, apart from the local `1`s (line, sequence, version). LicensePlateID `LicensePlateID-861`/`-871` is visibly fictitious.
- **Names and texts (new since round 2):**
  - German: `Voranmeldung der Ankunft`, `Beispielfrachtführer`, `Beispielwarenempfänger`, `Beispielfiliale`, `Beispielbehörde`, `Beispielzollbehörde`, `Beispielabfallerzeuger`, `Gebrauchte Blei-Säure-Batterien`, `Ja, der Artikel ist ab Lager lieferbar.` These are understandable and in idiomatic register.
  - Portuguese: `Frete rodoviário`, `Manutenção de equipamentos de escritório`, `Transportadora`, `Importador`, `Exportador`, `Fornecedor` (procurement), `Órgão Contratante`. These are natural.
  - Japanese: `Jigyōsha wa shōgyō tōki sarete imasu ka?`, `Sanpuru Tāminaru 1`, `Hatchū Kikan`, `Rakusatsusha`, `Meiginin`, `Niokurinin`, `Unsōnin`, `Daihyō Nyūsatsusha`, `Hatchū` (DigitalProcess). The Hepburn and macron use is consistent, and family-name-first in `Sanpuru Tarō` / `Sanpuru Samu` is consistent.
- **Embedded PDF:** unchanged since 01f8672. It decodes to a valid PDF (`pdfinfo` no errors, `pdftotext` → "PDF"), with mimeCode `application/pdf`.
- **Criterion question:** a yes/no question in the Description, answered with ResponseIndicator `true`. Only the ID link is broken (VA3#F1).

## Considered and refuted

- **FulfilmentCancellation "Ordered in error":** refuted in round 2 (spec 2.3.5.1.4); not reopened.
- **ItemInformationRequest carries SalesItem/Quantity 10 in a request:** SalesItem/Quantity is required by the schema, and it is defined as "The quantity the given information are related to", so it is a reference quantity, not the answer.
- **RetailEvent fallbacks ("Promoção de monções", "Monsūn sēru") unreviewed:** they are never emitted. The locale follows from the position in the fixed UBL 2.5 set, which puts RetailEvent in IN. The generator comment says so.
- **"Kourigyōsha", Shiiresaki/Tokuisaki, German nominalized participles, "Beispiel Öffentlicher Auftraggeber":** refuted in round 2; unchanged.
- **The CataloguePricingUpdate price has no item:** CataloguePricingUpdateLine/ID is "An identifier for the catalogue line to be updated", so the item is that of the referenced catalogue line (VA#F9 rule). Without BaseQuantity the price is per the item's unit, which is the usual reading. Not raised.

## Not verified

- Native-speaker naturalness of `Voranmeldung der Ankunft` (versus e.g. "Ankunftsvoranmeldung" or "Vorabanmeldung") and of the WorkReport alternatives in VA3#F4. These come from knowledge, and the round-2 majority of translators decided the current terms.
- Exchange rates and price levels behind "plausible" (approximate, from knowledge), and the average South African household or small-business consumption behind 350 kWh.
- Public holidays (ZA Women's Day observed on 10 August 2026; JP Mountain Day 11 August 2026) and the US federal fiscal year boundary: from knowledge, not checked against official calendars.
- Party identifier values (check digits, registers, D-U-N-S): left to the identification topic. Not re-verified in this round.
- The IANA registration of the `hepburn` variant (prefix `ja-Latn`): from knowledge.
