# What a document says about a party: the party table (O88)

Prepared 2026-11-17 for the owner's approval, before cause C01 (245 findings) is fixed. It applies the story line "What a document says about a party" (O86, `analysis/worklist-decisions.md`), which says:

- each party is the authority on its own data;
- every document stands on its own;
- the answer completes the picture.

The table is built into `tools/build_examples.py` (`DOC_CLASS`, `PROFILE`, `THIRD`, `party_profile()`, `apply_profile()`). It is switched off (`APPLY_PARTY_PROFILE = False`) until the owner approves it, so the published examples are unchanged. All figures below come from a build with the switch on.

## The rule in one paragraph

Every party in a document plays one of three parts:

- **The sender** describes itself in full for that kind of document ("about yourself").
- **The receiver** is described with what the sender knows and needs ("about the other"). This is never more than the receiver says about itself, and never contradicts it.
- **A third party** gets what the receiver needs to recognise or reach it.

What "full" means depends on the kind of document. For example:

- an order carries an address, a contact and an electronic address, but no share capital;
- an invoice carries the issuer's tax registration and legal entity;
- a customs declaration carries customs trader numbers;
- a tender presents the tenderer as a company.

## Blocks

A party description is made of blocks. Each element of `cac:Party` belongs to exactly one block.

| Block | Elements |
|---|---|
| id | `PartyIdentification`, `PartyName`, `TradePartyName`, `Person` (a consumer's name), `AdditionalPartyIdentification` with the GLN or the Codana number |
| customs | `AdditionalPartyIdentification` with the customs trader number |
| lang | `Language` (with its `LocaleCode`, D1) |
| addr | `PostalAddress` |
| site | `PhysicalLocation` |
| eaddr | `ElectronicAddress` |
| contact | `Contact` (the desk for the role, C02) |
| tax | `PartyTaxScheme` |
| legal-name | `PartyLegalEntity/RegistrationName`, `CompanyID` |
| legal | adds `CompanyLegalFormCode`, `CompanyLegalForm`, `RegistrationAddress`, `CorporateRegistrationScheme`, `SoleProprietorshipIndicator`, `RegistrationExpirationDate` |
| legal-full | adds `RegistrationDate`, `EntitySizeCode`, `CompanyLiquidationStatusCode`, `ShareholderParty`, `HeadOfficeParty`, `SecurityListing` |
| capital | `CorporateStockAmount`, `FullyPaidSharesIndicator` (see the open question O147) |
| present | `WebsiteURI`, `LogoReferenceID`, `IndustryClassificationCode`, `AdditionalWebSite`, `SocialMediaProfile` |
| permit | `PartyAuthorization` |
| account | `FinancialAccount`, `Person/FinancialAccount` |
| service | `ServiceProviderParty` |

## Kinds of document

All 93 document types of the world fall into 12 kinds. The figure is the number of examples.

| Kind | Examples | Document types |
|---|---|---|
| trade | 60 | Order (18), OrderResponse (5), OrderChange (2), OrderCancellation, RequestForQuotation (2), Quotation (2), DespatchAdvice (11), ReceiptAdvice (4), DeliveryNote, InstructionForReturns, FulfilmentCancellation (2), Forecast (2), ForecastRevision, InventoryReport, ProductActivity, RetailEvent, TradeItemLocationProfile, ItemInformationRequest, ExceptionCriteria, ExceptionNotification, WorkReport |
| catalogue | 7 | Catalogue (3), CataloguePricingUpdate, CatalogueItemSpecificationUpdate, CatalogueDeletion, CatalogueRequest |
| invoice | 51 | Invoice (33), CreditNote (5), DebitNote (3), SelfBilledInvoice (2), SelfBilledCreditNote, Reminder (3), PurchaseReceipt (4) |
| payment | 19 | RemittanceAdvice (12), Statement, UtilityStatement (6) |
| transport | 41 | Waybill (7), BillOfLading (2), ForwardingInstructions (5), TransportExecutionPlan (3), TransportExecutionPlanRequest (6), TransportationStatus (7), TransportationStatusRequest, TransportProgressStatus, TransportProgressStatusRequest, PackingList, Manifest, CommonTransportationReport (2), WeightStatement, GoodsItemItinerary, TransportServiceDescription, TransportServiceDescriptionRequest |
| customs | 22 | ImportCustomsDeclaration (7), ExportCustomsDeclaration (7), TransitCustomsDeclaration, CertificateOfOrigin (2), GoodsItemPassport, GoodsCertificate, ProofOfReexportation, ProofOfReexportationRequest, ProofOfReexportationReminder |
| waste | 2 | WasteMovement, WasteNotification |
| notice | 27 | PriorInformationNotice (3), ContractNotice (3), CallForTenders (3), ContractAwardNotice (3), AwardedNotification, UnawardedNotification, ProcurementStatus, ProcurementStatusRequest, ExpressionOfInterestRequest, ExpressionOfInterestResponse, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse, TenderReceipt, TenderWithdrawal, TendererQualificationResponse, GuaranteeCertificate, QualificationApplicationRequest (3) |
| qualification | 9 | Tender (3), TendererQualification (3), QualificationApplicationResponse (3) |
| contract | 2 | TenderContract, DigitalAgreement |
| presentation | 5 | BusinessCard, BusinessInformation (3), DigitalCapability |
| message | 5 | ApplicationResponse, DocumentStatus, DocumentStatusRequest, InvoiceStatusRequest, InvoiceStatusResponse |

## The table

| Kind | About yourself (the sender) | About the other (the receiver) | A third party |
|---|---|---|---|
| trade | id, lang, addr, site, eaddr, contact | id, addr, site, eaddr, contact | id, addr, contact |
| catalogue | id, lang, addr, site, eaddr, contact, legal, present | id, addr, site, eaddr, contact | id |
| invoice | id, lang, addr, site, eaddr, contact, tax, legal, capital, account | id, addr, eaddr, contact, legal-name | id |
| payment | id, lang, addr, eaddr, contact | id, addr, eaddr, contact | id |
| transport | id, lang, addr, site, eaddr, contact, customs | id, addr, site, eaddr, contact, customs | id, addr, contact, customs |
| customs | id, lang, addr, site, eaddr, contact, customs, legal-name | id, addr, eaddr, contact, customs, legal-name | id, addr, customs |
| waste | id, lang, addr, site, eaddr, contact, permit | id, addr, site, eaddr, contact, permit | id, addr, contact, permit |
| notice | id, lang, addr, eaddr, contact, legal-name | id, addr, eaddr, contact | id |
| qualification | id, lang, addr, eaddr, contact, legal-full, present, tax | id, addr, eaddr, contact, legal-name | id |
| contract | id, lang, addr, eaddr, contact, legal | id, addr, eaddr, contact, legal | id |
| presentation | id, lang, addr, site, eaddr, contact, legal-full, present, service | id, addr | id |
| message | id, lang, eaddr, contact | id, eaddr | id |

A block only appears if the party has the data. For example, `site` appears only for the six parties with a site of their own, and `permit` only for Rinova and Trasvia.

### Special rules on top of the table

1. **The answer completes the picture.** In a response, the receiver's language is given as well, because the sender knows it from the document it answers. The response types are:
   - OrderResponse, Quotation, TransportExecutionPlan, Waybill and BillOfLading, Tender, QualificationApplicationResponse, Catalogue, ReceiptAdvice;
   - the status answers and receipts: ApplicationResponse, DocumentStatus, InvoiceStatusResponse, ExpressionOfInterestResponse, UnsubscribeFromProcedureResponse, TenderReceipt, TendererQualificationResponse, ProcurementStatus, TransportationStatus, TransportProgressStatus, TransportServiceDescription.
2. **Customs numbers only across a border.** A transport document carries customs trader numbers only when its consignor and consignee (or exporter and importer, or else sender and receiver) are in different countries.
3. **The customer's tax registration only where the tax rests on it.** It appears in an invoice when the document's exemption rests on who the customer is: in Bayvarra a sale for resale (`RESALE`), to a public body (`PUBLIC`) or a service to a business (`SVCB2B`); in Urvania a service to a business abroad (`SVCABROAD`). It also appears for the importer in an import declaration, because the import tax is accounted for under the importer's registration.
4. **Self-billing.** In a SelfBilledInvoice or SelfBilledCreditNote, the buyer issues the seller's invoice, so the seller (`AccountingSupplierParty`) gets the invoice's "about yourself" profile. This brings back the farm's own legal entity: sole proprietor, and registration until the end of the year.
5. **The party a document presents.** These parties get the sender's profile of the kind (without the tax block for parties in a tender), even when they are not the sender:
   - the business in a BusinessInformation (`BusinessParty`);
   - in a tender or qualification, the parties the tenderer relies on (`AdditionalQualifyingParty`, `SubcontractorParty`).
6. **A consumer's account.** In an invoice to a consumer, the consumer's own account is given (`Person/FinancialAccount`), because the bills are collected from it.
7. **Share capital** on the issuer's own invoices, credit and debit notes, reminders and purchase receipts. Whether this stays depends on O147 (below).

### Example: the road order (road/01)

- **Before:** the buyer Lumeway (the sender) and the seller Valdara are both written in full: website, industry class, both further identifiers, language, address, tax registration, the full legal entity with share capital (and Valdara's stock listing), contact, Valdara's service provider, and electronic address.
- **After:**
  - Lumeway, about itself: identifier, GLN, name, language, address, contact, electronic address.
  - Valdara, as Lumeway knows it: identifier, Codana number, name, address, contact, electronic address.
  - Valdara gives its language itself in its order response (road/02).
  - Valdara's tax registration, legal entity and share capital are in its own invoice (road/15).
  - Valdara's stock listing is where it presents itself: in its tender, its qualification and the business information about it.

## Pairs where the answer completes the picture

| Flow | Request → response |
|---|---|
| ore | 02 TransportExecutionPlanRequest → 03 TransportExecutionPlan (Valdara → Ferrano Rail Cargo) |
| road | 01 Order → 02 OrderResponse (Lumeway → Valdara); 04 DespatchAdvice → 11 and 13 ReceiptAdvice (Castrano → Lumeway) |
| rail | 02 TransportExecutionPlanRequest → 03 TransportExecutionPlan (Valdara → Ferrano Rail Cargo) |
| retail | 01 CatalogueRequest → 02 Catalogue (Brightmarket → Lumeway); 12 DespatchAdvice → 17 ReceiptAdvice (Lumeway → Brightmarket) |
| sea | 05 Order → 06 OrderResponse (Velumi → Lumeway); 12 ForwardingInstructions → 14 BillOfLading (Bayforth → Tidewell); 20 DespatchAdvice → 21 ReceiptAdvice (Lumeway → Nalevi) |
| tender | 03 CallForTenders → 15, 17, 19 Tender; 06 QualificationApplicationRequest → 07 QualificationApplicationResponse; 26 Order → 28 OrderResponse |
| plastics | 01 Order → 02 OrderResponse (Rivermouth → Rinova); 03 TransportExecutionPlanRequest → 04 TransportExecutionPlan (Rinova → Fiumella) |
| wood | 01 RequestForQuotation → 02 Quotation (Valdara → Marrowdale) |
| furniture | 01 RequestForQuotation → 02 Quotation (Brightmarket → Brackenmere) |
| contest | 05 QualificationApplicationRequest → 06 QualificationApplicationResponse; 10 → 11 |

The flows air, carnet, waste, utilities, cotton, packaging, mast and energy have no such pair. In those flows each party describes itself only in the documents it sends. The flow decisions of stage 6 (D28 to D48) add documents. Where a new document is the answer to one already there, it joins this list.

## What it does

### Size

The 250 examples go from 79,130 to 58,106 elements (−27 %).

| Kind | Examples | Elements before | after |
|---|---|---|---|
| trade | 60 | 18,357 | 12,584 |
| transport | 41 | 14,476 | 9,933 |
| invoice | 51 | 16,845 | 14,548 |
| payment | 19 | 5,665 | 3,907 |
| customs | 22 | 8,174 | 5,767 |
| notice | 27 | 7,536 | 5,367 |
| qualification | 9 | 2,055 | 1,744 |
| catalogue | 7 | 2,534 | 2,028 |
| presentation | 5 | 1,029 | 766 |
| contract | 2 | 872 | 747 |
| message | 5 | 883 | 319 |
| waste | 2 | 704 | 396 |

### Party elements, counted over all examples

| Element | Before | After |
|---|---|---|
| `PartyIdentification` / `PartyName` | 1,420 / 1,432 | 1,339 / 1,351 (the 81 less are the parties nested in removed service provider and shareholder blocks) |
| `AdditionalPartyIdentification` | 589 | 333 |
| `PostalAddress` | 640 | 603 |
| `Contact` | 633 | 564 |
| `ElectronicAddress` | 633 | 496 |
| `Language` | 633 | 309 |
| `PartyLegalEntity` | 633 | 210 |
| `PartyTaxScheme` | 501 | 79 |
| `IndustryClassificationCode` | 633 | 29 |
| `WebsiteURI` | 511 | 21 |
| `CorporateStockAmount` | 236 | 20 |
| `EntitySizeCode` / `RegistrationDate` | 511 | 14 |
| `ServiceProviderParty` | 75 | 1 |
| `SecurityListing` | 75 | 3 |
| `PartyAuthorization` | 29 | 4 |
| `LogoReferenceID`, `AdditionalWebSite`, `SocialMediaProfile` | 41 each | 1 each |

These follow from the table, with no extra check:

- every customs trader number is in a customs document or a cross-border transport document;
- every share capital is on its issuer's own invoice;
- every website, logo and industry class is in a document that presents the party.

### Coverage before and after

Coverage goes from **4996 to 4993** of 5160. Three pairs are lost:

| Lost | Why | Candidate real case to win it back |
|---|---|---|
| `PartyLegalEntity . ShareholderParty`, `ShareholderParty . ParticipationPercent`, `ShareholderParty . Party` | Only Castrano Logistics has a shareholder (Valdara, 100 %). Castrano never sends a document that presents it, and as a receiver it is described with what the sender knows. | Castrano presents itself as a company: a qualification in which Valdara relies on its own subsidiary for the delivery and installation of the benches (D28), or a business card from Castrano. |

Everything else stays covered. Sometimes this needs one of the special rules:

- the farm's legal entity: rule 4;
- Valdara's service provider: rule 5, in the business information about Valdara;
- the consumer's account: rule 6.

If O147 is answered a), share capital leaves, and coverage falls by two more pairs to 4991.

The same build also fixes a fault in the currency clean-up of step 1e: a remittance line that pays a document in another currency into the document's own currency now keeps its exchange rate. This is energy/09: a reminder in lume, paid in ferra. Until now the rate stayed only because the parties' share capital happened to be in lume.

## Open question for the owner

**O147 · Share capital on documents.** No country of the world has a rule on it yet.

- **The real models:**
  - The EU company-law directive (Directive (EU) 2017/1132, Art. 26) requires the register, the company's number in it, the legal form and the registered office on a company's letters and order forms. Capital is optional; if it is stated, it must be the capital subscribed and paid up.
  - Italy goes further (art. 2250 codice civile): companies limited by shares state their paid-up capital, as shown in the last balance sheet, in their documents and correspondence, and say whether they have a single shareholder.
- **The options:**
  - a) No country requires it: share capital disappears from every document. This costs 2 coverage pairs.
  - b) Urvania requires it, Italian-style, of every SUA on its invoices and business letters; Bayvarra and Lisavu follow the EU model, where capital is optional. Share capital then stays on the own invoices of the Urvanian SUAs (Valdara, the mine, the energy companies). Urvania's VAT is already EU-style, and this gives the element a reason in the world's law.
  - c) Every company states it voluntarily on its invoices, as now. This keeps 20 occurrences, but without a reason in law.
- **Recommendation:** b).

## After approval

1. Switch the profile on, and add the build checks of C01 and O90:
   - no customs trader number outside customs and cross-border documents;
   - no share capital outside its issuer's own invoices;
   - what A says about B is a part of what B says about itself;
   - every party element the rule keeps appears in at least one document.
2. Record the outcome in the decisions file, and the three lost pairs in O145.
