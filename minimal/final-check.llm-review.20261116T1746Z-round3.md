# Final check of the round-3 fixes

## Reviewed version

- Commit `3d3863a9edffc0dafc6453d3d5529e5fbce6b8a4` (HEAD of the local checkout).
- Scope: `git diff 6f3c962 3d3863a -- minimal/gen_minimal.py minimal/layer0 minimal/layer1`. That is 15 commits, 47 files, +204/−62.
- Checked against the five round-3 reviews (`minimal/*-round3.md`) and the decisions in the brief and the task.

## Result in short

Every round-3 finding is fixed in the documents as the commits describe. There is no validation error, broken reference, locale mix, duplicate value, misordered date or wrong unit. What remains is three Low findings, all about generator comments or dead configuration. None of them changes a document.

## Validation

- `python3 minimal/gen_minimal.py --check` on all 202 files gives `202 documents, 0 with violations`. That covers XSD, phase 2 (default code lists, Saxon) and the generator's IND checks.
- xmllint, run independently, validates 202/202:
  - the 93 endorsed documents against `endorsed/xsd/maindoc`;
  - the 8 + 8 deprecated documents against the full `xsd/maindoc`;
  - none of the deprecated types has an endorsed schema.
- Reproducibility: I copied the generator to the scratchpad and ran it there, linked to the same `.ubl`. The output is byte-identical to `layer0/` and `layer1/` (`diff -r`), so the committed XML is what the generator produces.
- The old `6f3c962:minimal/layer0/QualificationApplicationResponse.xml` is now flagged with `REF …/cbc:ValidatedCriterionPropertyID refers to no TenderingCriterionProperty`, so the new reference check works.

## Findings

### FC#F1 · Low · Three items of ST3#F5 are only partly fixed, and new comment drift

- **Where and why:** commit 84529f0 says the comments match the current generator, but some do not.
  1. **Docstring, l. 15–16:** "A value type with no rule and no default stops the build, so a later layer must choose it." This is ST3#F5.8 and is unchanged. Code, Identifier, Text and Name are written as `@UNCHOSEN@` and rejected by `check()` (l. 51, 58–59, 1159).
  2. **ROLE_NAMES comment, l. 705:** "Translations: checked against two independent human translations". This is the second half of ST3#F5.6, still unchanged, while the TEXTS comment (l. 764) now says "round 2 against three".
  3. **New WorkReport role names, l. 730–732:** these have no review note. Only the pt-BR names are used, because WorkReport is BR in both layers. The en, de and ja values ("Dienstleister", "Ekimu Teikyōsha", …) are unreviewed fallbacks, as with RetailEvent, whose comment says so.
  4. **"Document level (IND6)" comment, l. 349–351:** "These are listed as UBL findings (ubl-findings.md, 'essential but optional')". `ubl-findings.md` did not change in this range (`git diff --stat` is empty). The new document-level additions have no E-entry:
     - CommonTransportationReport `cac:Shipment`;
     - ProcurementStatus and TenderStatus `cac:TenderSubmissionDeadlinePeriod`;
     - TransportationStatus `cbc:IssueDate` and `cbc:IssueTime`;
     - TransportSchedule `cac:ActualArrivalTransportEvent`;
     - DebitNoteLine `cac:Item`;
     - the line quantities;
     - Waybill and TransitCustomsDeclaration `cac:GoodsItem`.

     The statement was already inexact (ST3#F5.7) and now covers less.
  5. **`scheme_for` docstring, l. 576–581:** it still lists only D-U-N-S, the contracting-authority, sender and participant LEIs, and the carnet holder's tax number. The code now also converts the LEIs of CarrierParty, FreightForwarderParty and TransportServiceProviderParty, and the tax numbers of ImporterParty, ExporterParty and TransitExporterParty (ID3#F1).
  6. **FILL comment, l. 444:** "(DM3#F105, ST3#F3)" stands on the TransportSchedule arrival. DM3#F105 is the TransportationStatus finding, which is fixed by `cbc:IssueDate` and `cbc:IssueTime` at l. 380–383. The arrival fixes ST3#F3 only.
  7. **Uncommented FILL entries, l. 436–437:** `TransitCustomsDeclaration:ShipmentType` and `Waybill:ShipmentType` (GoodsItem) have no reason comment. The block comment above them still lists only "a packing list describes goods".
- **Condition:** every comment states the current reason (the generator's comments are the decision record).
- **Options:** rewrite items 1–7. For item 4, either say "most are also UBL findings", or add the E-entries.
- **Needs decision:** no.

### FC#F2 · Low · Dead GLN rule for the CommonTransportationReport receiver

- **Where:**
  - `gen_minimal.py` l. 553–558 gives GLN to `CommonTransportationReport/SenderParty` and `…/ReceiverParty`.
  - Since d725bad, `generate()` (l. 1085–1090) replaces ReceiverParty with a copy of AuthorityParty, which has no scheme.
  - Result in `layer1/CommonTransportationReport.xml`:
    - `/*/cac:ReceiverParty` = `PartyName/Name` "Beispielbehörde 132", with no PartyIdentification;
    - the former GLN `9520000001346` (receiver 134) is gone.
- **Why:** the document is right: AuthorityParty and ReceiverParty are both "the Party who receives" the report, and are the same party by decision. But the SCHEMES table still states a GLN decision for that receiver that is overwritten afterwards.
- **Condition:** the scheme table states only decisions that take effect.
- **Options:**
  1. Remove the `ReceiverParty` half for CommonTransportationReport, keeping the GLN rule for SenderParty.
  2. Add a comment there saying that the receiver is the authority.
- **Needs decision:** no.

### FC#F3 · Low · The PriorInformationNotice project is "numbered as its procedure", but it has no procedure identifier

- **Where:**
  - `layer0/PriorInformationNotice.xml` and `layer1/PriorInformationNotice.xml`: `/*/cac:ProcurementProject/cbc:Name` = `Office supplies 2027 (541)`.
  - `count(/*/cbc:ContractFolderID)` = 0.
  - The `name_for` comment (l. 824–825) and commit 3d3863a say the name is "numbered as the document's procedure identifier (ContractFolderID-k)".
- **Why:** this holds for CallForTenders (`ContractFolderID-61`, "(61)") and ContractNotice (`ContractFolderID-151`, "(151)"). In the PIN, ContractFolderID is optional and not used, so 541 matches only the contracting authority ("Example Contracting Authority 541"). The value is unique and harmless. Only the stated reason is wrong for this document.
- **Condition:** the comment describes all three documents.
- **Options:** reword the comment as "document position × 10 + 1, the same number as the procedure identifier where the document has one". No document changes.
- **Needs decision:** no.

## Checked and consistent

| Round-3 finding | Fix | Verified |
|---|---|---|
| DM3#F101, ST3#F1, VA3#F1 | `ValidatedCriterionPropertyID` follows the property ID | `TenderingCriterionProperty-631` in both layers; `check()` now verifies the reference |
| VA3#F2 | bill lines state their quantity | Invoice, SelfBilledInvoice, CreditNote, SelfBilledCreditNote and PurchaseReceipt all state `10` H87. FreightInvoice states `1` E54, which is "trip" in UBL's UnitOfMeasureCode-2.4 ("A unit of count defining the number of trips"). Its line still describes "Frete rodoviário" |
| DM3#F3, ST3#F2 | DebitNote line has a quantity and an item | `DebitedQuantity 10 H87` and `Item/Description` "Ballpoint pen, blue" (en, ZA locale); 270.00 ZAR, i.e. 27 per pen |
| DM3#F4 | catalogue price has a base quantity | CataloguePricingUpdate states `BaseQuantity 1 H87` next to `PriceAmount 7.50 BRL`. No other document has a Price, so the global `PriceType` fill affects nothing else |
| DM3#F1 | the report names its shipment | CommonTransportationReport has `Shipment/ID` = `Shipment-131` |
| DM3#F2 | authority and receiver are one party | ReceiverParty = AuthorityParty in both layers |
| DM3#F102 | the status documents state the tender period | ProcurementStatus and TenderStatus: `TenderSubmissionDeadlinePeriod` from 2026-08-12 (= IssueDate) to 2026-09-08 (a Tuesday, D+27) |
| DM3#F103, DM3#F104 | the shipments carry goods | TransitCustomsDeclaration (en) and Waybill (ja-Latn-hepburn) have `GoodsItem/Item/Description` in the locale's language |
| DM3#F105 | the status is dated | TransportationStatus has IssueDate 2026-08-12 and IssueTime `09:30:00-04:00`, the US offset as elsewhere |
| ST3#F3 | the arrival is stated | TransportProgressStatus: `TransportSchedule/ActualArrivalTransportEvent` ("The actual arrival at a location") on 2026-08-11 `09:30:00+09:00`, which is before IssueDate and IssueTime 2026-08-12 `09:30:00+09:00` |
| ST3#F4 | the vehicle's country code states its scheme | `RegistrationNationalityID/@schemeID` = `urn:iso:std:iso:3166`, which is the CanonicalUri of `CountryIdentificationCode-2.4.gc` (TransportProgressStatus JP, TransportProgressStatusRequest IN) |
| DM3#F106, VA3#F3 | the enquiry names its item | Enquiry (en) and EnquiryResponse (de) name the blue ballpoint pen. The German is grammatical ("der blaue Kugelschreiber ist ab Lager lieferbar"). The TEXTS comment marks the new wording as not yet reviewed |
| DM3#F107, ST3#F5.1–5 | comments | UtilityStatementTypeCode, CODE_VALUES, BillingReference, Response and Location comments are updated |
| VA3#F4 | the Brazilian WorkReport names its parties as services | "Prestador de Serviços Exemplo 1001" and "Tomador de Serviços Exemplo 1002" |
| VA3#F5 | consumption comment | the comment now reads "a small business's month". The layer1 receiver has D-U-N-S `362242799`, and `ParentDocumentReference` is present |
| VA3#F6 | project name | "Office supplies 2027 (61 / 151 / 541)" in both layers; but see FC#F3 for the PIN |
| ID3#F1 | Japanese transport parties have the Corporate Number | layer1 Waybill CarrierParty `0188` `9999900000982`, whose check digit 9 is correct. No `0199` remains in any of the 17 JP documents per layer |
| ID3#F2, ID3#F3 | identifier comments and D-U-N-S order | the docstring names its exceptions, and the ROLE_NAMES k-note excludes D-U-N-S. `next_duns()` documents its order dependence and raises a clear error when the 123 test numbers run out |

**Checks across the set, within each layer:**
- no duplicate identifier `(schemeID, value)` across documents;
- no duplicate numbered names across documents;
- one language, one currency and one time-zone offset per document, in all 202 files;
- the JP Corporate Number check digit is correct for every `0188` value.

## Considered and refuted

- **The same party twice in CommonTransportationReport breaks "values unique across the set".** No: the duplication is inside one document, and it is the agreed decision. The value is not repeated across documents.
- **The tender period starts on the status document's own issue date.** This is the agreed decision (D..D+27), so it is not reopened.
- **TransportationStatus IssueDate is defined as the document's issue date, not as the status moment.** This is the agreed decision. The status is read as of issue, and TransportEvent is correctly avoided.
- **"Four weeks" for D+27.** From 2026-08-12 to 2026-09-08 inclusive is 28 days, so "four weeks" is right.
- **The global FILL entries (`TransportEventType`, `PriceType`, `InvoiceLineType`) could spill into other documents.** They do not: the regenerated set differs from 6f3c962 only in the 47 files of the diff.

## Not verified

- Whether "Ekimu Teikyōsha / Ekimu Juryōsha" and the ja/pt-BR enquiry wordings are what human translators would choose. They are unreviewed by design and noted in FC#F1.
