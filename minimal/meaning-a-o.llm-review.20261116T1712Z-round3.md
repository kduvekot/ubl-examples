# Review of document meaning in minimal/layer1, A to O (round 3)

## Reviewed version

- Repository kduvekot/ubl-examples, branch `claude/elegant-franklin-kk2dky`, commit `6f3c96249f32ccee9c469666e3a3e4db6ccca635` ("minimal: UtilityStatement shows its consumption (DM#F116)").
- Scope: the 48 files directly in `minimal/layer1/` from `ApplicationResponse.xml` to `OrderResponse.xml`. P to Z and `deprecated/` are covered by another reviewer.
- Baseline: the round-2 review `meaning-a-o.llm-review.20261116T1419Z-minimal.md` (commit `01f8672`). The changes since then are `git diff 01f8672..6f3c962 -- minimal/`.
- Standard: UBL 2.5 OASIS Standard in `minimal/.ubl/os-UBL-2.5/`. Root and element definitions come from the `ccts:Definition` in `endorsed/xsd/`. Submitter and receiver roles come from section 3.2.x of `UBL-2.5.html`.
- Method:
  - I read every document as a whole, using an indented dump of all 48 files.
  - I compared each with its root definition, its roles and the definitions of its elements.
  - Each XPath below was run with lxml against the file named. The namespaces were `cac`, `cbc` and the document namespace as `d`.
  - Scratch scripts are in `/tmp/claude-0/-home-user-ubl-examples/cf0e0c4e-4ca5-5fb4-92ba-ea1bf0fe6f57/scratchpad/round3/meaning-a-o/`.
  - `python3 minimal/gen_minimal.py --check` on the 48 files reports "48 documents, 0 with violations".
- Test (the same as in round 2): a document gets a finding only when something essential to its defined purpose is absent, or when its parts contradict each other or the purpose. Something that would merely be nice to have is not a finding.

## Round-2 findings: status

All 31 round-2 findings (DM#F1 to DM#F31) are fixed in the documents as their conditions required:
- ApplicationResponse, DocumentStatus and DocumentStatusRequest now state their response or the document they concern.
- BillOfLading names its carrier, consignor and shipment. ForwardingInstructions names its consignor and forwarder.
- The CertificateOfOrigin issuer endorses its own certificate and the origin is stated. CommonTransportationReport has a report type and an authority.
- ContractAwardNotice has a winner.
- Customers are now on CreditNote, DebitNote and Invoice. Quantities and order references are now on despatch, delivery and order lines.
- DigitalAgreement has two participants.
- The exception and information-request lines carry an activity code, the forecast lines carry a SalesItem, and the cancellation references what it cancels.
- GoodsCertificate has a Description, ImportCustomsDeclaration has an importer and Manifest has its cargo.
- OrderChange is `Revised`, OrderResponse is `ACCEPTED`, and identifiers are unique across the set (`DOCNO * 10 + n`).

No regression was found. The three findings below come from the round-2 fixes or from rules that were applied unevenly.

## Findings

### CommonTransportationReport

#### DM3#F1 · Medium · A pre-arrival notification that does not say what arrives

- **Where:** `CommonTransportationReport.xml`:
  - `string(/d:CommonTransportationReport/cbc:ReportType)` = `Voranmeldung der Ankunft` (added since 01f8672 for DM#F6, `gen_minimal.py` l. 379 and the `TEXTS["ReportType"]` entry);
  - `count(/d:CommonTransportationReport/cac:Shipment | .../cac:TransportMeans | .../cac:ReportingLocation | .../cac:DocumentReference)` = 0.
- **Why:**
  - The root definition is "A common document used for reporting transport related issues to authorities or regulators". The spec's role table says "A Logistic operator sends a Common Transportation Report to a harbour".
  - The report type chosen in this round tells the authority that something will arrive. The document does not say what: no shipment ("A shipment to which this common transportation report applies"), no means of transport ("A means of transport used in relation to this common transportation report") and no location. A notification of an arrival that names nothing arriving cannot be acted on.
  - So the report's subject is left implied (IND6). The fix for DM#F6 met that finding's condition (type and authority), but the type it chose created this new gap.
  - The other transport documents in the set name their subject at least with a shipment reference: Manifest, ForwardingInstructions, BillOfLading, GoodsCertificate and ImportCustomsDeclaration.
- **Condition:** The report identifies the shipment or the means of transport that it announces.
- **Options:**
  1. `FILL["CommonTransportationReportType"]` adds `cac:Shipment`. `Shipment/ID` then follows from the existing `ShipmentType` fill (`Shipment-131`), the same pattern as Manifest.
  2. Add `cac:TransportMeans` instead. Its RoadTransport/LicensePlateID and RegistrationNationalityID follow from the existing `TransportMeansType` fill. That fits "arrival" better, but a road vehicle arriving at a harbour authority is a weaker story than a shipment.
  3. Choose a report type that needs no subject. I found none that fits "reporting transport related issues".
- **Needs decision:** no for option 1, which reuses the Shipment pattern. Yes if the means of transport is preferred.

#### DM3#F2 · Low · Two different parties both receive the report

- **Where:** `CommonTransportationReport.xml`:
  - `string(/d:CommonTransportationReport/cac:AuthorityParty/cac:PartyName/cbc:Name)` = `Beispielbehörde 132` (added since 01f8672);
  - `string(/d:CommonTransportationReport/cac:ReceiverParty/cac:PartyName/cbc:Name)` = `Beispielempfänger 134`;
  - also ReporterParty `Beispielberichterstatter 131` and SenderParty `Beispielabsender 133`.
- **Why:**
  - AuthorityParty is defined as "The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator." ReceiverParty is defined as "The Party who receives this Report." The spec's receiver role is "Authority party", described as "The party who is receiving a Common Transportation Report".
  - With AuthorityParty now present, the document names two different parties, each defined as the one that receives the report, and says nothing about how they relate. A reader cannot tell whether 134 forwards the report to 132 (for example a port community system) or whether the report has two addressees.
  - The same holds, more weakly, for ReporterParty ("provides") and SenderParty ("sends"). Different verbs make an agent sending on the reporter's behalf a reasonable reading, so that pair alone would not be a finding.
  - In round 2 the ReceiverParty-versus-authority question was refuted only on identification grounds, when no AuthorityParty was present. The addition creates the overlap.
- **Condition:** Either the two receiving roles are one party (same name; layer 1 may keep the GLN on ReceiverParty), or the generator records why the message receiver differs from the authority.
- **Options:**
  1. In `generate()`, give AuthorityParty the same name as ReceiverParty. This is the same identity-override mechanism used for the CertificateOfOrigin issuer (DM#F4, l. 1033-1038). The authority stays identified by name only.
  2. Keep the two parties, and add a generator comment that ReceiverParty is the transmitting intermediary (for example a port community system) and AuthorityParty the authority. Possibly add the double definition to `ubl-findings.md`, because UBL defines both elements with the same meaning.
- **Needs decision:** yes.

### DebitNote

#### DM3#F3 · Medium · 270 ZAR debited for nothing stated

- **Where:** `DebitNote.xml`:
  - `count(/d:DebitNote/cac:DebitNoteLine/*)` = 2 (`cbc:ID` = `1`, `cbc:LineExtensionAmount` = `270.00` ZAR);
  - `count(//cac:DebitNoteLine/cac:Item | //cac:DebitNoteLine/cbc:Note | //cac:DebitNoteLine/cac:DiscrepancyResponse | //cac:DebitNoteLine/cbc:DebitedQuantity | /d:DebitNote/cac:DiscrepancyResponse | /d:DebitNote/cbc:Note | /d:DebitNote/cac:BillingReference)` = 0.
- **Why:**
  - The root definition is "A document used to specify debits due to the Creditor from the Debtor". DebitNoteLine/Item [0..1] is "The item associated with this debit note line".
  - The line states an amount but says nothing about what is debited: no item, no reason (DiscrepancyResponse, "A reason for the debit") and no referenced bill.
  - The generator gives the pens and the amount only in a comment (`AMOUNTS`, l. 73: "ZAR 10 x 27.00").
  - This is the condition of round-2 DM#F112 ("SelfBilledCreditNote: 100 BRL credited for nothing"). Commit 14af369 ("commercial documents say what they concern") applied it to CreditNote and SelfBilledCreditNote through `FILL["CreditNoteLineType"] = {"cac:Item"}` (l. 404), but not to DebitNote. Every other bill in scope names its item (`count(//cac:InvoiceLine/cac:Item)` = 1, CreditNote `Caneta esferográfica, azul`), so DebitNote is the exception.
  - This is uneven application of a decision already taken, not new scope.
- **Condition:** The debit note line says what is debited.
- **Options:**
  1. `FILL["DebitNoteLineType"] = {"cac:Item"}`. `Item/Description` "Ballpoint pen, blue" follows from the ItemType fill, as for CreditNote.
  2. Also add `DebitedQuantity` = 10 H87, so that the 270.00 agrees visibly with 10 x 27.00. That would be nice, not essential, and CreditNote does not have it either.
  3. A DiscrepancyResponse as the reason. That needs a ResponseCode or Description decision, so it is not recommended for the minimal set.
- **Needs decision:** no (option 1 follows DM#F112). The other reviewer may want to check SelfBilledInvoice (P-Z) for the same pattern; I did not verify it.

### CataloguePricingUpdate

#### DM3#F4 · Low · A price whose unit is implied

- **Where:** `CataloguePricingUpdate.xml`:
  - `string(//cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount)` = `7.50` (BRL), added since 01f8672 for DM#F3;
  - `count(//cac:Price/cbc:BaseQuantity)` = 0;
  - `count(//cac:CataloguePricingUpdateLine/cac:Item)` = 0.
- **Why:**
  - Price/BaseQuantity [0..1] is "The quantity at which this price applies". Without it, the reader has to assume that 7.50 BRL is per one piece. The generator says so only in a comment (`AMOUNTS`, l. 72: "BRL one pen").
  - The generator's own rule for quantities is that a unit left to absence is IND6 (`QUANTITY_UNITS`, l. 245-246). A price per an unstated quantity is the same kind of gap.
  - The line refers to catalogue line 1 of `RelatedCatalogueReference-101` (outside the set), and catalogue practice prices per the line's orderable unit. So the reading "per catalogue unit" is defensible, and the severity is Low.
- **Condition:** The quantity the price applies to is stated, or the generator records that a catalogue price applies per the referenced line's orderable unit.
- **Options:**
  1. `FILL["PriceType@Price"]` (or `"CataloguePricingUpdate:PriceType"`) adds `cbc:BaseQuantity` with `QUANTITY_UNITS["Price/BaseQuantity"] = "H87"` and `QUANTITY_VALUES["Price/BaseQuantity"] = "1"`.
  2. Keep the document as is, and add the reason as a comment at `FILL["ItemLocationQuantityType"]` (l. 448).
- **Needs decision:** yes (small).

## Checked and consistent

Roles are checked against spec section 3.2.x. Every currency, country, language and UTC offset matches the document's place in the locale rotation.

- **ApplicationResponse:** the sender answers the receiver with `ACCEPTED` on `DocumentReference-1`, which is what "the application's response to a transaction" requires.
- **AwardedNotification:** the JP contracting authority informs the winner, who is the receiver by definition, of procedure `ContractFolderID-21`. The award was decided on Monday 2026-08-10.
- **BillOfLading:** the carrier (LEI) evidences carriage of `Shipment-31` for the consignor (D-U-N-S). This is the contract of carriage the definition describes.
- **BusinessCard / BusinessInformation:** the BusinessParty is the content.
- **CallForTenders / ContractNotice:** the contracting authority (LEI) announces a named project with its procedure ID.
- **Catalogue / CatalogueDeletion / CatalogueItemSpecificationUpdate / CatalogueRequest:** provider and receiver in GS1 (GLN) roles. Each document has the content its type names: an item, the deleted catalogue, the updated description, or the request itself.
- **CertificateOfOrigin:**
  - The origin `US` equals IssuingCountry `US`, consistent with the generator's reason "a CoO is issued in the country of origin".
  - The ISSUER endorsement (sequence 1) is given by the IssuerParty `Example Issuer 123` and signed by `Sam Example`. The EMBASSY endorser in the application is sequence 2, signed by `Alex Example`.
  - `Approved` fits a certificate that has been issued.
- **ContractAwardNotice:** authority, award date and now the winner (`Sanpuru Rakusatsusha 142`, JP Corporate Number).
- **CreditNote:** a credit of 75.00 BRL from supplier to customer (both by CNPJ) for blue pens.
- **DeliveryNote / DespatchAdvice:** shipper to consignee (GLN), with 10 pieces of blue pens on line 1 of `OrderReference-181` or `OrderReference-191`. That covers "delivered items, quantities".
- **DigitalAgreement:** two participants with distinct Corporate Numbers agree on the process "Hatchū" (ordering), version 1.
- **DigitalCapability:** a business and one supported process.
- **DocumentStatus / DocumentStatusRequest:** a status (`ACCEPTED`) for `DocumentReference-221`, and the document whose status is asked.
- **ExceptionCriteria / ExceptionNotification:** an `ON_HAND` falls-below threshold of 10 pieces, valid for a year. The notification observes 8 against 10 over the four weeks before issue. The two documents read alike.
- **ExportCustomsDeclaration / ImportCustomsDeclaration:** the declarant (CNPJ, BR jurisdiction) and what is declared (`CustomsDeclaration-281`, or `Shipment-401`). This mirrors the counterpart declaration.
- **ExpressionOfInterestRequest / ExpressionOfInterestResponse:** the economic operator and the contracting authority, for an identified procedure.
- **Forecast / ForecastRevision:**
  - A future sales forecast of 10 pieces of pens, type `TOTAL`.
  - The revision gives a new value for line 1 of the forecast issued 2026-08-05 09:30+09:00, for the same future period.
- **ForwardingInstructions:** the consignor (D-U-N-S) instructs the forwarder (LEI) about `Shipment-331`.
- **FulfilmentCancellation:** cancels `DespatchDocumentReference-351` with the reason "Ordered in error", a reason spec 2.3.5.1.4 allows.
- **GoodsCertificate:** a "Certificate of conformity" by the issuer for `Shipment-361`.
- **GoodsItemItinerary:** one port-to-port segment by a carrier (LEI) under the referenced TEP.
- **GoodsItemPassport:** holder, shipment and counterfoil.
- **GuaranteeCertificate:** a bank guarantor (LEI) and the depositor ("The Party who deposits the bid bond guarantee"), with 50000.00 INR liability for procedure `ContractFolderID-391`.
- **InstructionForReturns / InventoryReport:** seller to retailer (return 10 pens), and retailer with a reporting party (10 pens in stock).
- **Invoice:** a request for payment of 15.00 EUR from supplier to customer (DE VAT numbers) for blue pens.
- **InvoiceStatusRequest / InvoiceStatusResponse:** the typed invoice reference, and the answer `ACCEPTED` for a referenced document.
- **ItemInformationRequest:** asks for `SALES` data for blue pens over the four weeks before issue.
- **Manifest:** the logistics operator lists `Shipment-471` as cargo.
- **Order / OrderCancellation / OrderChange / OrderResponse:**
  - The buyer orders 10 pieces.
  - The cancellation references the order and gives a reason.
  - The change marks line 1 `Revised` with quantity 10.
  - The seller answers `ACCEPTED`.
  - Buyer and seller roles match spec 3.2.50 to 3.2.53.

Also checked:
- Every value of an `*ID` element or a `Name` in layer1 (including P-Z and deprecated) other than line number 1 occurs in one file only. The only repeats are the tax-scheme names (`Umsatzsteuer`, `Value-Added Tax`, `Federal Income Tax`, `Cadastro Nacional da Pessoa Jurídica`), which name the same scheme on purpose. DM#F31 is fixed.
- No `X` and no `@UNCHOSEN@` is left in A-O (the generator check passes).

## Considered and refuted

- **ItemInformationRequest: a request for sales data that already states a quantity (`SalesItem/Quantity` = 10):** SalesItem [1..unbounded] and its Quantity [1..1] are required by the schema. UBL defines the quantity as "The quantity the given information are related to", so the generator cannot avoid it. The tension is UBL's own and belongs in `ubl-findings.md` if anywhere. It was there before 01f8672, so it is not caused by the added `SALES` code.
- **CertificateOfOrigin without ExporterParty:** ExporterParty is [0..1] on both the certificate and the application. The goods are identified by the shipment and their origin, and the applicant is the PreparationParty. The certificate's claim (the origin of `Shipment-121`) can be understood without the exporter.
- **CertificateOfOrigin: the application names an EMBASSY endorser, but the certificate has no EmbassyEndorsement:** the application's EndorserParty [1..unbounded] is "A party providing an endorsement to the CoO", and legalization by an embassy follows issue (sequence 2). A certificate that is issued but not yet legalized is consistent.
- **BillOfLading, CertificateOfOrigin, GoodsCertificate, Manifest, ForwardingInstructions and ExportCustomsDeclaration without IssueDate:** the element is [0..1] in each. Round 2 refuted the same point for ContractNotice, and the rule is applied the same way here.
- **GoodsCertificate whose spec submitter is the "Exporter party" while the document has only IssuerParty:** IssuerParty [1..1] is required and is "The Party who issues this Goods Certificate". The gap between the spec's submitter and the schema is UBL's own.
- **ForecastRevision revises to 10, the same as Forecast's 10:** the documents are unrelated by decision. The revision's source is a forecast outside the set, so equal values carry no claim.
- **InvoiceStatusResponse references a plain `DocumentReference`, while the request uses a typed `InvoiceDocumentReference`:** DocumentResponse/DocumentReference is the schema's only place for this. Round 2 accepted it.

## Not verified

- Whether SelfBilledInvoice (P-Z) has the same gap as DM3#F3 (out of scope).
- Whether "pre-arrival notification" is a report type actually exchanged with UBL CommonTransportationReport in any implementation (DM3#F1). The finding rests only on the UBL definitions.
- The translations of the texts added after the translators' round (for example `Voranmeldung der Ankunft`). These belong to the translations topic.
