# Coverage register

The UBL 2.5 elements that no example covers, one row each, with where each was lost and where it is to get a real case. Kept by hand; the build checks it against the examples (`tools/coverage_register.py`, run by `tools/check_world.py`). Decided by the owner on 2026-11-19 (O145): no loss may disappear silently.

**Rules**

- Every element that `sh tools/coverage_world.sh` reports as missing has a row under "Missing", and every row under "Missing" is missing: the build stops otherwise. An element that a change removes from its last example gets its row in the same commit, with the cause; an element that comes back moves to "Won back" with the example that covers it.
- No filler: an element gets back only through a real business case in the world (UBL IND5/IND6, the rules of `analysis/codelist-decisions.md`). "Left out on purpose" holds the elements the world has no case for, with the reason.
- **Status:** `open` (no candidate case yet), `candidate` (a case proposed, not yet agreed), `agreed` (the owner agreed the case and its place), `left out` (no case, on purpose).
- **Lost from:** the examples that had the element just before the change that removed it (found from the history; a parent matched by name, so a hint, not a proof).
- **Place:** the flow or stage-6 building group where the case is to be built (`analysis/worklist.md`).

The history of losses before this register is in O145 of `analysis/worklist-decisions.md`, whose text per step is quoted below.

## Missing

### G8: cotton, sea (2026-11-19)

Stage 6, building group G8 (C106 to C108, C114 to C118).

> C106, D33: the farm's documents belong to the farm and the ginnery alone. The mill is not originator or beneficiary of the seed-cotton purchase and its season agreement not the originator document (cotton/03#F10, 04#F4, 05#F14, D33); the chamber's "cotton quality project", the ginnery's season account of the farm, the annotation that repeated the note and the customs broker as tax representative of a purchase between two Lisavan businesses go (03#F3, 04#F5, F12, F13, F14, 05#F6, F13, F15, F16); the gin's outturn report did not exist when the invoice was issued and the price does not rest on it (04#F10); the haulage charge keeps only its per-kilogram amount (04#F20); the credit note names no payee (nothing is paid under it, 05#F5), no delivery terms (05#F20) and cites the chamber's classing report as its work report instead of the export lot's certificate (05#F2).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `AllowanceCharge/PaymentMeans` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `AllowanceCharge/PrepaidIndicator` | 0..1 | cotton/04-SelfBilledInvoice |  |  | open |
| `AllowanceCharge/SequenceNumeric` | 0..1 | cotton/04-SelfBilledInvoice |  |  | open |
| `DeliveryNote/BeneficiaryParty` | 0..n | cotton/03-DeliveryNote |  |  | open |
| `DeliveryNote/OriginatorCustomerParty` | 0..1 | cotton/03-DeliveryNote |  |  | open |
| `DeliveryNote/ProjectReference` | 0..n | cotton/03-DeliveryNote |  |  | open |
| `SelfBilledCreditNote/AdditionalDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/Annotation` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/DeliveryTerms` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/OriginatorDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/PayeeParty` | 0..1 | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/ProjectReference` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/StatementDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledCreditNote/TaxRepresentativeParty` | 0..1 | cotton/05-SelfBilledCreditNote |  |  | open |
| `SelfBilledInvoice/Annotation` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/BeneficiaryParty` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/OriginatorCustomerParty` | 0..1 | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/OriginatorDocumentReference` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/ProjectReference` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/StatementDocumentReference` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/TaxRepresentativeParty` | 0..1 | cotton/04-SelfBilledInvoice |  |  | open |
| `SelfBilledInvoice/WorkReportDocumentReference` | 0..n | cotton/04-SelfBilledInvoice |  |  | open |

> C107, D33: the classing certificate is no earlier version of the phytosanitary certificate (cotton/10#F3); the criterion type code only repeated "processing" (10#F17); the feeder's interim security certificate is a valid one, so the report gives no reason for an absence (14#F3).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CriterionItem/TypeCode` | 0..1 | cotton/10-GoodsCertificate |  |  | open |
| `GoodsCertificate/OriginalDocumentReference` | 0..1 | cotton/10-GoodsCertificate |  |  | open |
| `ISPSRequirements/ISSCAbsenceReason` | 0..n | cotton/14-CommonTransportationReport |  |  | open |

> C108, D33: open account, no documentary collection: the Bank of Selanu holds no mortgage on the bales (cotton/13#F3); the ginnery signs its own verified gross mass, so no one signs it on its behalf (12#F2).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Consignment/MortgageHolderParty` | 0..1 | cotton/13-BillOfLading |  |  | open |
| `WeightStatement/ResponsibleParty` | 0..1 | cotton/12-WeightStatement |  |  | open |

> C118, D30 point 1: 520 and 68 lume are CIF Selanu prices, the sea freight and the insurance in them. The factor's statement repeats no freight or insurance of the invoice (sea/25#F1); Bayvarra's export declaration states the value on board without the freight and the insured value after export (11#F13); Lisavu values the CIF price as it is, so the import declaration gives no freight share or policy per goods item (19#F20); the pre-carriage is the forwarder's merchant haulage, billed in its invoice (18), not a charge of the carrier's bill (14#F14); the policy has one retention, its deductible (14#F13); the seller's instructions arrange no on-carriage at Selanu, which is the buyer's (09#F7); the credit note claims nothing from the insurer, the loss being below the deductible (26#F3).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Consignment/FinalDeliveryTransportationService` | 0..1 | sea/09-ForwardingInstructions |  |  | open |
| `CreditNote/Annotation` | 0..n | sea/26-CreditNote |  |  | open |
| `GoodsItem/FreightAllowanceCharge` | 0..n | sea/19-ImportCustomsDeclaration |  |  | open |
| `GoodsItem/InsurancePolicy` | 0..n | sea/19-ImportCustomsDeclaration |  |  | open |
| `InsurancePolicy/ExcessAmount` | 0..1 | sea/14-BillOfLading |  |  | open |
| `Shipment/FreightAllowanceCharge` | 0..n | sea/11-ExportCustomsDeclaration |  |  | open |
| `ShipmentStage/FreightAllowanceCharge` | 0..n | sea/14-BillOfLading |  |  | open |
| `Statement/AllowanceCharge` | 0..n | sea/25-Statement | a charge of the factor's own in its statement, such as a factoring fee, if the factoring agreement gives one | sea | open |
| `StatementLine/AllowanceCharge` | 0..n | sea/25-Statement |  |  | open |

> C116, D30 point 3 (O6, D9, O104): the buyer's debit note sea/28 is removed; the customs inspection and the day of storage it passed on are the second line of Lumeway's credit note sea/26. Its number 28 is not used again (D28). The world's debit notes are now the rail flow's two of the demurrage (rail/12, 13, D37) and tender/34 until the tender flow removes it (D28); the elements below were in sea/28 alone. The factor's collection account is the invoice's payee account, not a financing account (sea/22#F7); the deposit's payment dates are no invoice period of the statement (25#F3).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `DebitNote/AccountingCost` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/AccountingCostCode` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/Annotation` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/BuyerAssignedReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/BuyerCustomerParty` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/CollectionDebitNoteLine` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/Delivery` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/DeliveryNoteDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/DeliveryTerms` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/DespatchDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/OriginatorDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/PayeeParty` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/PaymentCurrencyCode` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/PaymentExchangeRate` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/ProjectReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/PurchaseReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/ReceiptDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/SellerSupplierParty` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNote/Signature` | 0..n | sea/28-DebitNote | the rail flow's debit notes of the demurrage (rail/12, 13), signed when the signatures stage gives every signing party its key pair (D6) | stage 8 | candidate |
| `DebitNote/StatementDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNote/WorkReportDocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/AccountingCost` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/AccountingCostCode` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/AllowanceCharge` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/BeneficiaryParty` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/CollectedForParty` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/DeliveryTerms` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/DespatchLineReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/DocumentReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/FreeOfChargeIndicator` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/ItemPriceExtension` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/OrderLineReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/OriginatorParty` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/PaymentPurposeCode` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/PaymentTerms` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/PricingReference` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/ReceiptLineReference` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/SubDebitNoteLine` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/TaxInclusiveLineExtensionAmount` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/TaxPointDate` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/TaxTotal` | 0..n | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/UUID` | 0..1 | sea/28-DebitNote |  |  | open |
| `DebitNoteLine/WorkReportLineReference` | 0..n | sea/28-DebitNote |  |  | open |
| `ProjectReference/IssueDate` | 0..1 | sea/28-DebitNote |  |  | open |
| `ProjectReference/UUID` | 0..1 | sea/28-DebitNote |  |  | open |
| `ProjectReference/WorkPhaseReference` | 0..n | sea/28-DebitNote |  |  | open |
| `StatementLine/InvoicePeriod` | 0..n | sea/25-Statement |  |  | open |
| `TradeFinancing/FinancingFinancialAccount` | 0..1 | sea/22-Invoice |  |  | open |

> C114, D30 point 8: the bill of lading's container carries no road chassis on board, no goods-item container count of pallets and no second package beside the frames' pallet (sea/14#F1, F7, F8); the cargo manifest names no crew and no passenger, which are in the ship's report (15#F7); the ship's report gives no reason for an absence of control actions it took, no WHO affected area and no INF class for a feeder without INF cargo (16#F6, F7, F21); the hold at Selanu was the container's quarantine check, not a detention of the ship, and the discharge status reports no terminal charge (17#F2, F9). The consignor's consignment ID held the buyer's order (sea/14#F6); the consignment's own `ID` is Lumeway's, and road/08's went with G5's C100 (road/08#F11), so with both groups merged the element has no example left. Won back: `ShipmentStage/PassengerQuantity` (O128).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BallastWaterSummary/NoControlActionsReason` | 0..n | sea/16-CommonTransportationReport |  |  | open |
| `GoodsItemContainer/Quantity` | 0..1 | sea/14-BillOfLading |  |  | open |
| `Manifest/CrewPerson` | 0..n | sea/15-Manifest |  |  | open |
| `Manifest/PassengerPerson` | 0..n | sea/15-Manifest |  |  | open |
| `MaritimeHealthDeclaration/WHOAffectedAreaVisit` | 0..n | sea/16-CommonTransportationReport |  |  | open |
| `MaritimeTransport/INFShipClassCode` | 0..1 | sea/16-CommonTransportationReport |  |  | open |
| `Package/ContainingTransportEquipment` | 0..1 | sea/14-BillOfLading |  |  | open |
| `ShipmentStage/DetentionTransportEvent` | 0..n | sea/17-TransportationStatus |  |  | open |
| `TransportEquipment/AttachedTransportEquipment` | 0..n | sea/14-BillOfLading |  |  | open |
| `TransportEquipment/Package` | 0..n | sea/14-BillOfLading |  |  | open |
| `WHOAffectedAreaVisit/VisitDate` | 1 | sea/16-CommonTransportationReport |  |  | open |
| `WHOAffectedAreaVisit/WHOAffectedAreaPortLocation` | 1 | sea/16-CommonTransportationReport |  |  | open |

> C117, D30 point 7: the digital agreement is the Trade Accord's multilateral agreement; the certification it requires is the council's for access points, published as a PDF with its hash, no embedded text with a file name of its own, no character set for a PDF and no XPath into a document that is not XML (sea/03#F6, F13, F14).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `DocumentReference/XPath` | 0..n | sea/03-DigitalAgreement |  |  | open |
| `ExternalReference/CharacterSetCode` | 0..1 | sea/03-DigitalAgreement |  |  | open |

> C115, D30 points 6 and 9: the carrier's service description classifies its service with no goods code for seats (sea/08#F7).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TransportationService/CommodityClassification` | 0..n | sea/08-TransportServiceDescription |  |  | open |

### Stage 1 step 1a: party master data (C02, C03, C05, C07)

Coverage 5153 → 5151 (commit c15bf42c), 2 elements.

> O140: **`Address/Region` lost its only example (stage 1 step 1a, 2026-11-17):** it held the Urvanian province, which is a country subdivision and went to `CountrySubentity` (C03). UBL defines `Region` as "the recognized geographic or economic region or group of countries in which this address is located". A real case: a price or a territory that covers the Trade Accord area as a whole (for example `ApplicableTerritoryAddress` of a catalogue price valid in all three countries), to look for with C25 in step 1e; otherwise it stays uncovered

> O141: **`Address/AdditionalStreetName` lost its only example (stage 1 step 1a, 2026-11-17):** it held Lumeway's "Gate 3", which is a delivery location and went to the road order's `DeliveryLocation` (C05). A real case: an address whose street needs a second name to be found, such as a building that stands on a corner and is entered from the side street, or a farm track off a named road; to be found with the place list (O91) or the encyclopaedia; otherwise it stays uncovered

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Address/AdditionalStreetName` | 0..n | air/01-OrderChange, air/02-OrderResponse, air/03-ForwardingInstructions … | | | open |

### Stage 1 step 1b: public bodies and state companies (C04, D46)

Coverage 5151 → 5150 (commit 3bdb6f31), 1 element.

> O143: **`PartyLegalEntity/HeadOfficeParty` lost its only example (stage 1 step 1b, 2026-11-17):** D46 drops the port as head office of Selanu Airport Cargo, a company of its own (air/09#F3). A real case: a branch that is not a legal entity of its own and states its head office, such as a branch of the Bank of Lumeport or one of Brightmarket's stores, where a document's job needs the legal entity; otherwise it stays uncovered

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `PartyLegalEntity/HeadOfficeParty` | 0..1 | air/09-TransportationStatus | | | open |

### Stage 1 step 1c: references and statuses (C06, C16, C26, C37, C39)

Coverage 5150 → 5129 (commit d2506729), 21 elements.

> O145, Step 1c (5150 → 5129): `DocumentStatusCode` in DeliveryNote, TransportExecutionPlanRequest, ForwardingInstructions, CommonTransportationReport and DespatchAdvice, `LineStatusCode` in LineReference and DespatchLine (the `NoStatus` values, C16); `DespatchDocumentReference` and `ReceiptDocumentReference` in SelfBilledInvoice and SelfBilledCreditNote (C26); `Contract` in OrderResponse and FulfilmentCancellation and `ContractDocumentReference` in CreditNote (the digital agreement as a sale's contract, C26, D30); `BillingReference` in WorkReport and InvoiceLine (C26); `SalesOrderID` in Order and OrderChange, `ReleaseID` in Delivery and Despatch, `CustomerReference` in OrderReference (C37). Candidate real cases noted so far: air/08 replaces a cancelled despatch advice (D39), a `Revised` status; road/13 is a corrected receipt advice (D35); the tender's order response (28) answers under the framework contract; the export release once a document can quote the declaration's number (stage 5).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CommonTransportationReport/DocumentStatusCode` | 0..1 | sea/16-CommonTransportationReport | | | open |
| `CreditNote/ContractDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote, sea/26-CreditNote | | | open |
| `Delivery/ReleaseID` | 0..1 | tender/26-Order |  |  | open |
| `DeliveryNote/DocumentStatusCode` | 0..1 | cotton/03-DeliveryNote | | | open |
| `DespatchAdvice/DocumentStatusCode` | 0..1 | air/06-DespatchAdvice, air/08-DespatchAdvice, mast/04-DespatchAdvice … | | | open |
| `DespatchLine/LineStatusCode` | 0..1 | air/06-DespatchAdvice, air/08-DespatchAdvice, mast/04-DespatchAdvice … | | | open |
| `ForwardingInstructions/DocumentStatusCode` | 0..1 | air/03-ForwardingInstructions, cotton/09-ForwardingInstructions, sea/09-ForwardingInstructions … | | | open |
| `FulfilmentCancellation/Contract` | 0..n | air/07-FulfilmentCancellation | | | open |
| `InvoiceLine/BillingReference` | 0..n | furniture/17-Invoice | | | open |
| `LineReference/LineStatusCode` | 0..1 | cotton/04-SelfBilledInvoice, road/02-OrderResponse | | | open |
| `OrderReference/CustomerReference` | 0..1 | air/07-FulfilmentCancellation | the fulfilment cancellation's reference to the order change quotes the buyer's own reference of it, "Harbour parks Selanu": the frames are spares for the port's harbour benches (O199 a') | air | candidate |
| `OrderResponse/Contract` | 0..n | sea/06-OrderResponse |  |  | open |
| `SelfBilledCreditNote/DespatchDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/ReceiptDocumentReference` | 0..n | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledInvoice/DespatchDocumentReference` | 0..n | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/ReceiptDocumentReference` | 0..n | cotton/04-SelfBilledInvoice | | | open |
| `TransportExecutionPlanRequest/DocumentStatusCode` | 0..1 | ore/02-TransportExecutionPlanRequest, plastics/03-TransportExecutionPlanRequest, rail/02-TransportExecutionPlanRequest … | | | open |
| `WorkReport/BillingReference` | 0..n | furniture/16-WorkReport | | | open |

### Stage 1 step 1d, part 1: shipping order, originals, ad valorem, journey (C20, C33, C36, C41)

Coverage 5129 → 5121 (commit ca324ac5), 8 elements.

> O145, Step 1d, part 1 (5129 → 5121): `AdValoremIndicator` in Waybill, ForwardingInstructions, BillOfLading and Manifest (it names ad valorem duties, which no shipment has under D18; C36); `DeclaredCarriageValueAmount` in ForwardingInstructions and BillOfLading (the cotton value declared for the Bank of Selanu, whose role goes with D33, and for which nothing was charged; C36); `ShippingOrderID` in ForwardingInstructions (its own number, not a shipping order) and TransportationStatusRequest (the retail flow has no forwarding instructions; C20). Candidate real cases: a valuation charge billed for a declared value (the air frames, D39, and the uninsured granulate, D41, keep their declared value and get the charge in stage 6); `ShippingOrderID` in a status request of a flow with forwarding instructions (sea, air, mast).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BillOfLading/AdValoremIndicator` | 0..1 | cotton/13-BillOfLading, sea/14-BillOfLading | | | open |
| `BillOfLading/DeclaredCarriageValueAmount` | 0..1 | cotton/13-BillOfLading | | | open |
| `ForwardingInstructions/AdValoremIndicator` | 0..1 | air/03-ForwardingInstructions, cotton/09-ForwardingInstructions, sea/09-ForwardingInstructions … | | | open |
| `ForwardingInstructions/DeclaredCarriageValueAmount` | 0..1 | cotton/09-ForwardingInstructions | | | open |
| `ForwardingInstructions/ShippingOrderID` | 0..1 | air/03-ForwardingInstructions, cotton/09-ForwardingInstructions, sea/09-ForwardingInstructions … | | | open |
| `Manifest/AdValoremIndicator` | 0..1 | sea/15-Manifest | | | open |
| `TransportationStatusRequest/ShippingOrderID` | 0..1 | retail/14-TransportationStatusRequest | | | open |
| `Waybill/AdValoremIndicator` | 0..1 | air/04-Waybill, mast/03-Waybill, ore/05-Waybill … | | | open |

### Stage 1 step 1d, part 2: service codes, waybill types, despatch dates (C35, C30, C27)

Coverage 5121 → 5120 (commit 6e7125c2), 1 element.

> O145, Step 1d, part 2 (5121 → 5120): `Delivery/DeliveryNoteDocumentReference` (it held the road waybill in the receipt advices road/11 and 13, now a typed additional reference; C30). Candidate real case: a delivery note cited from a delivery, such as the farm's delivery note on the island (cotton).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Delivery/DeliveryNoteDocumentReference` | 0..n | road/11-ReceiptAdvice, road/13-ReceiptAdvice | | | open |

### Stage 1 step 1d, part 4: framework transport terms and periods (C19)

Coverage 5120 → 5117 (commit 5e00c80d), 3 elements.

> O145, Step 1d, part 4 (5120 → 5117): `NotificationRequirement/PostEventNotificationDurationMeasure` (an hour after delivery on a pre-arrival notice), `TransportExecutionPlan/AtLocation` (where the carrier's planning sits), `TransportExecutionTerms/CommissionPaymentTerms` (a broker who does not appear; C19). Candidate real cases: an arrival or delivery confirmation that is due after the event; the weighing of the ore wagons at the mine siding as a service without movement in the ore plan; a broker who really finds a barge or a ship for a carrier.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `NotificationRequirement/PostEventNotificationDurationMeasure` | 0..1 | ore/03-TransportExecutionPlan, plastics/04-TransportExecutionPlan, rail/03-TransportExecutionPlan | | | open |
| `TransportExecutionTerms/CommissionPaymentTerms` | 0..1 | plastics/04-TransportExecutionPlan | | | open |

### Stage 1 step 1e, part 3: remittance advices (C17)

Coverage 5117 → 5111 (commit 9f3f108b), 6 elements.

> O145, Step 1e, part 3 (5117 → 5111): `RemittanceAdviceLine/AccountingSupplierParty`, `AccountingCustomerParty` and `DocumentReference` (the line repeated the header's parties and referred to the paid invoice twice), `RemittanceAdvice/PayerReference` (a second value for the payment order), `CreditNoteLine/PaymentPurposeCode` (a purpose on a credit settled by set-off), `LineItem/LineReference` (the quotation line referenced twice; C17). Candidate real cases: a remittance advice that pays invoices of several suppliers in one payment run, such as Valdara paying the mine's and the rail carrier's invoices together (line parties and a line document reference of another kind); a payer's own payment-run reference beside the payment order; a credit note refunded by credit transfer; an order line that takes up a line of a document other than its quotation.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CreditNoteLine/PaymentPurposeCode` | 0..1 | retail/19-CreditNote | | | open |
| `LineItem/LineReference` | 0..n | furniture/08-Order | | | open |
| `RemittanceAdvice/PayerReference` | 0..1 | cotton/18-RemittanceAdvice, ore/08-RemittanceAdvice, plastics/11-RemittanceAdvice … | | | open |
| `RemittanceAdviceLine/AccountingCustomerParty` | 0..1 | cotton/18-RemittanceAdvice, ore/08-RemittanceAdvice, plastics/11-RemittanceAdvice … | | | open |
| `RemittanceAdviceLine/AccountingSupplierParty` | 0..1 | cotton/18-RemittanceAdvice, ore/08-RemittanceAdvice, plastics/11-RemittanceAdvice … | | | open |

### Stage 1 step 1e, part 4: tax arithmetic and empty zero totals (C24)

Coverage 5111 → 5110 (commit c3a2692e), 1 element.

> O145, Step 1e, part 4 (5111 → 5110): `Statement/TaxTotal` (a zero tax total in a factor's statement of account, C24). Candidate real case: a statement of account whose lines carry tax that is reported per period, such as a utility's yearly statement of the household's account (D31).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Statement/TaxTotal` | 0..n | sea/25-Statement | | | open |

### Stage 1 step 1e, part 5: catalogue terms (C25)

Coverage 5110 → 5106 (commit 6fe6444b), 4 elements.

> O145, Step 1e, part 5 (5110 → 5106): `ItemLocationQuantity/DependentPriceReference` with its `Percent`, `LocationAddress` and `DependentLineReference` (the spare frame priced as a share of the bench, which D34 contradicts: Lumeway lowers the frame's price and keeps the bench's; C25). Candidate real case: a price that follows another by a stated rule, such as the sawmill's single slat priced from the bundle of 50 (D43) or a special colour priced as a share of the standard variant.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `DependentPriceReference/DependentLineReference` | 0..1 | retail/02-Catalogue, sea/02-Catalogue | no longer the single slat priced from the bundle (D43 sells only the bundle, G1); other candidate from O145: a price that follows another by a stated rule | | open |
| `DependentPriceReference/LocationAddress` | 0..1 | retail/02-Catalogue | no longer the single slat priced from the bundle (D43 sells only the bundle, G1); other candidate from O145: a price that follows another by a stated rule | | open |
| `DependentPriceReference/Percent` | 0..1 | retail/02-Catalogue, sea/02-Catalogue | no longer the single slat priced from the bundle (D43 sells only the bundle, G1); other candidate from O145: a price that follows another by a stated rule | | open |
| `ItemLocationQuantity/DependentPriceReference` | 0..1 | retail/02-Catalogue, sea/02-Catalogue | no longer the single slat priced from the bundle (D43 sells only the bundle, G1); other candidate from O145: a price that follows another by a stated rule | | open |

### Stage 1 step 1e, part 6: currencies with something to convert (C11)

Coverage 5106 → 5064 (commit 6ec37a8f), 42 elements.

> O145, Step 1e, part 6 (5106 → 5064, C11): 42 currency elements that converted nothing: `PricingCurrencyCode`, `TaxCurrencyCode`, `PaymentCurrencyCode` and `PaymentAlternativeCurrencyCode` with their exchange rates in SelfBilledInvoice and SelfBilledCreditNote (cotton/04, 05: all equal to the coral document currency, or a lume pricing currency for coral prices), in Order (retail/08), Invoice and CreditNote (tender/32, 33), Reminder (tender/35) and DebitNote (sea/28, removed with D30 anyway); `RequestedInvoiceCurrencyCode` in Order and OrderChange; the free-standing `ExchangeRate` of Waybill, ForwardingInstructions, BillOfLading, StatementLine, the purchase receipt's `Payment`, and the telecom statement's service and supply lines; `PurchaseReceipt/PricingExchangeRate`; the tender order's `ExchangeMarketID` and `ForeignExchangeContract` (D28: no forward contract in a tender document; O96). Candidate real cases: the Lumeport Textile Mill pays the island ginnery's coral invoice from its lume account (cotton/16, 18): the invoice asks for payment in lume with its rate (`PaymentCurrencyCode`, `PaymentExchangeRate`); a Lisavan buyer shown the coral equivalent of a lume amount it pays (`PaymentAlternativeCurrencyCode` with `PayableAlternativeAmount`); freight charges collect at Selanu stated in coral on a bill of lading or air waybill (`ExchangeRate`); a contract priced in one currency and invoiced in another, for `PricingCurrencyCode`, which D28 removes from the tender (the trade outside the Accord, O51).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BillOfLading/ExchangeRate` | 0..n | cotton/13-BillOfLading, sea/14-BillOfLading | | | open |
| `CreditNote/PaymentAlternativeCurrencyCode` | 0..1 | cotton/05-SelfBilledCreditNote, sea/26-CreditNote | | | open |
| `CreditNote/PaymentAlternativeExchangeRate` | 0..1 | cotton/05-SelfBilledCreditNote, sea/26-CreditNote | | | open |
| `DebitNote/PaymentAlternativeCurrencyCode` | 0..1 | sea/28-DebitNote | | | open |
| `DebitNote/PaymentAlternativeExchangeRate` | 0..1 | sea/28-DebitNote | | | open |
| `DebitNote/PricingCurrencyCode` | 0..1 | sea/28-DebitNote | | | open |
| `DebitNote/PricingExchangeRate` | 0..1 | sea/28-DebitNote | | | open |
| `DebitNote/TaxCurrencyCode` | 0..1 | sea/28-DebitNote | | | open |
| `DebitNote/TaxExchangeRate` | 0..1 | sea/28-DebitNote | | | open |
| `ExchangeRate/ExchangeMarketID` | 0..1 | tender/26-Order, tender/27-OrderChange, tender/28-OrderResponse … | | | open |
| `ExchangeRate/ForeignExchangeContract` | 0..1 | tender/26-Order, tender/27-OrderChange, tender/28-OrderResponse … | | | open |
| `ForwardingInstructions/ExchangeRate` | 0..n | air/03-ForwardingInstructions, cotton/09-ForwardingInstructions, sea/09-ForwardingInstructions … | | | open |
| `Invoice/PricingCurrencyCode` | 0..1 | cotton/04-SelfBilledInvoice, tender/32-Invoice | | | open |
| `Invoice/PricingExchangeRate` | 0..1 | cotton/04-SelfBilledInvoice, tender/32-Invoice | | | open |
| `Order/PricingCurrencyCode` | 0..1 | tender/26-Order | | | open |
| `Order/PricingExchangeRate` | 0..1 | tender/26-Order | | | open |
| `Order/RequestedInvoiceCurrencyCode` | 0..1 | cotton/08-Order | | | open |
| `OrderChange/RequestedInvoiceCurrencyCode` | 0..1 | tender/27-OrderChange | | | open |
| `Payment/ExchangeRate` | 0..1 | sea/24-InvoiceStatusResponse | | | open |
| `PurchaseReceipt/PricingExchangeRate` | 0..1 | packaging/09-PurchaseReceipt | | | open |
| `Reminder/PaymentAlternativeCurrencyCode` | 0..1 | tender/35-Reminder | | | open |
| `Reminder/PaymentAlternativeExchangeRate` | 0..1 | tender/35-Reminder | | | open |
| `SelfBilledCreditNote/PaymentAlternativeCurrencyCode` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/PaymentAlternativeExchangeRate` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/PaymentCurrencyCode` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/PaymentExchangeRate` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/PricingCurrencyCode` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/PricingExchangeRate` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/TaxCurrencyCode` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/TaxExchangeRate` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledInvoice/PaymentAlternativeCurrencyCode` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/PaymentAlternativeExchangeRate` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/PaymentCurrencyCode` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/PaymentExchangeRate` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/PricingCurrencyCode` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/PricingExchangeRate` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/TaxCurrencyCode` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/TaxExchangeRate` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `StatementLine/ExchangeRate` | 0..1 | sea/25-Statement | | | open |
| `TelecommunicationsService/ExchangeRate` | 0..n | utilities/12-UtilityStatement | | | open |
| `TelecommunicationsSupplyLine/ExchangeRate` | 0..n | utilities/12-UtilityStatement | | | open |
| `Waybill/ExchangeRate` | 0..n | air/04-Waybill | | | open |

### Stage 1 step 1e, part 7: cost centres by what is bought (C14)

Coverage 5064 → 5058 (commit cdebe62f), 6 elements.

> O145, Step 1e, part 7 (5064 → 5058, C14): `AccountingCostCode` and `AccountingCost` of DeliveryNote (the gin's code on the farm's delivery note), of Reminder and of ReminderLine (the water company's own ledger accounts given as the household's). Candidate real cases: a reminder to a business buyer that quotes the buyer's cost centre from the unpaid invoice, so that its accounts payable can match it (Valdara's reminder to the public works department, tender/35, or the gas producer's, energy/08); a delivery note on which the buyer asked the supplier to quote its cost centre.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `DeliveryNote/AccountingCost` | 0..1 | cotton/03-DeliveryNote | | | open |
| `DeliveryNote/AccountingCostCode` | 0..1 | cotton/03-DeliveryNote | | | open |
| `Reminder/AccountingCost` | 0..1 | utilities/10-Reminder | | | open |
| `Reminder/AccountingCostCode` | 0..1 | utilities/10-Reminder | | | open |
| `ReminderLine/AccountingCost` | 0..1 | utilities/10-Reminder | | | open |
| `ReminderLine/AccountingCostCode` | 0..1 | utilities/10-Reminder | | | open |

### Stage 1 step 1f: customs builders (C29, C12)

Coverage 5058 → 5049 (commit 0edd7d78), 9 elements.

> O145, Step 1f (5058 → 5049, C12): `ImportCustomsDeclaration/PreviousCustomsDeclaration` (another country's export declaration; now a typed additional reference), `/ValidityPeriod` (a validity on a release) and `/CustomsExitOfficeLocation` (the exporting country's office); `TransitCustomsDeclaration/PreviousCustomsDeclaration`, `/ImportCustomsExitOfficeLocation` and `/TransitCustomsExitOfficeLocation`, `Consignment/OfficeOfEntryLocation` (offices that did not fit their definitions); `Shipment/DeclaredCustomsValueAmount` and `/DeclaredStatisticsValueAmount` (a sum over two tariff headings). Candidate real cases: an import from temporary storage or a bonded store in the same country (plastics/09, option a of its finding), for the previous declaration; a pre-lodged import declaration, for the validity period; the Accord's common transit of the air frames across Bayvarra (D39) or the samples' transit (D40), for the transit offices and the office of entry; a shipment of one tariff heading, for the shipment-level declared values.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ImportCustomsDeclaration/CustomsExitOfficeLocation` | 0..1 | cotton/15-ImportCustomsDeclaration, plastics/09-ImportCustomsDeclaration, road/10-ImportCustomsDeclaration … | | | open |
| `TransitCustomsDeclaration/ImportCustomsExitOfficeLocation` | 0..1 | rail/06-TransitCustomsDeclaration | | | open |
| `TransitCustomsDeclaration/PreviousCustomsDeclaration` | 0..n | rail/06-TransitCustomsDeclaration | | | open |
| `TransitCustomsDeclaration/TransitCustomsExitOfficeLocation` | 0..1 | rail/06-TransitCustomsDeclaration | | | open |

### Stage 1 step 1g: redundant party roles, independent unit serials, slat data, codes

Coverage 5049 → 4996 (commit 1bf967d6), 53 elements.

> O145, Step 1g (5049 → 4996): C08, 47: `OriginatorCustomerParty` and `BeneficiaryParty` of RequestForQuotation, Quotation, OrderCancellation, FulfilmentCancellation, PriorInformationNotice, ContractNotice, CallForTenders, Tender, ContractAwardNotice and Statement, `OriginatorParty` and `BeneficiaryParty` of LineItem and `OriginatorParty` of CreditNoteLine, the originator, beneficiary and seller of StatementLine and the originator and beneficiary of RemittanceAdviceLine (all repeated the buyer, the contracting party or the header); the six tendering roles of the prior information notice and `DocumentProviderParty` and `TenderRecipientParty` of ProcurementStatus (the contracting party again); `ContractorCustomerParty` and `SellerSupplierParty` of the catalogue lines (the header's); `InstructionForReturnsLine/ManufacturerParty`; `TransportProgressStatus/SourceIssuerParty` (the sender); `TransitCustomsDeclaration/FreightForwarderParty` (the carrier); `Consignment/PerformingCarrierParty` and `PerformingCarrierAssignedID` of TransportExecutionPlanRequest (the contracted carrier). C22, 2: `ItemProperty/UsabilityPeriod` and `ItemIdentification/MeasurementDimension` (the slat). C42, 1: `RequestForQuotationLine/SecurityClassificationCode`. C43, 1: `Temperature/MeasureCode`. C44, 2: `ReplacementRelatedItem` of CatalogueLine and TenderLine. Candidate real cases: a buyer that orders on behalf of another body, such as the parks service as a body of its own that uses the benches the public works department buys (originator and beneficiary in the tender documents, D28), or a store ordering for a franchisee; a catalogue line from another supplier than the header's (the distributor's catalogue with a line that Brackenmere supplies direct); a statement or remittance that covers invoices of several suppliers (also listed under step 1e); a contracting authority with a tender box or helpdesk of its own (`TenderRecipientParty`, `AdditionalInformationParty` with their own contact); a return instruction for lines of two makers; a status relayed from the network manager by the hub (`SourceIssuerParty`, rail/05#F9 option b); a forwarder that lodges the transit declaration for the shipper; a subcontracted carrier beyond the border (`PerformingCarrierParty`); a slat oil with a shelf life (`UsabilityPeriod`); an item numbered per length (`MeasurementDimension` in the seller's identification, if a real seller does that); a confidential tender line (`SecurityClassificationCode`); a reefer set to a temperature class rather than a value (`MeasureCode`, O137); a newer frame casting that replaces the 2026 one (`ReplacementRelatedItem`). The running list is complete for stage 1: 164 elements uncovered, of which 7 on purpose.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CallForTenders/BeneficiaryParty` | 0..n | tender/03-CallForTenders | | | open |
| `CallForTenders/OriginatorCustomerParty` | 0..n | tender/03-CallForTenders | | | open |
| `CatalogueItemSpecificationUpdateLine/ContractorCustomerParty` | 0..1 | retail/04-CatalogueItemSpecificationUpdate | | | open |
| `CatalogueItemSpecificationUpdateLine/SellerSupplierParty` | 0..1 | retail/04-CatalogueItemSpecificationUpdate | | | open |
| `CatalogueLine/ContractorCustomerParty` | 0..1 | retail/02-Catalogue | | | open |
| `CatalogueLine/ReplacementRelatedItem` | 0..n | retail/02-Catalogue | | | open |
| `CatalogueLine/SellerSupplierParty` | 0..1 | retail/02-Catalogue | | | open |
| `CataloguePricingUpdateLine/ContractorCustomerParty` | 0..1 | retail/03-CataloguePricingUpdate | | | open |
| `CataloguePricingUpdateLine/SellerSupplierParty` | 0..1 | retail/03-CataloguePricingUpdate | | | open |
| `Consignment/PerformingCarrierAssignedID` | 0..1 | rail/08-Waybill | | | open |
| `Consignment/PerformingCarrierParty` | 0..1 | rail/08-Waybill | | | open |
| `ContractAwardNotice/BeneficiaryParty` | 0..n | tender/21-ContractAwardNotice | | | open |
| `ContractAwardNotice/OriginatorCustomerParty` | 0..1 | tender/21-ContractAwardNotice | | | open |
| `ContractNotice/BeneficiaryParty` | 0..n | tender/02-ContractNotice | | | open |
| `ContractNotice/OriginatorCustomerParty` | 0..n | tender/02-ContractNotice | | | open |
| `CreditNoteLine/OriginatorParty` | 0..1 | tender/33-CreditNote | | | open |
| `FulfilmentCancellation/BeneficiaryParty` | 0..n | air/07-FulfilmentCancellation | the Port of Selanu, for whose harbour benches the frames of the cancelled despatch are, as the order change names it (O199 a'; with O198's open point on who bears what) | air | candidate |
| `FulfilmentCancellation/OriginatorCustomerParty` | 0..1 | air/07-FulfilmentCancellation | the Port of Selanu, whose need started the order of the frames, as in the order change (O199 a'; with O198) | air | candidate |
| `InstructionForReturnsLine/ManufacturerParty` | 0..1 | furniture/12-InstructionForReturns | the wholesaler\'s instruction for returns of the spent Mo-99/Tc-99m generator to its maker (a fictional maker abroad, named in the document, not a world party), with the return shipment; owner, 2026-11-19 (O202 choice 7) | medicines | candidate |
| `ItemIdentification/MeasurementDimension` | 0..n | wood/01-RequestForQuotation, wood/02-Quotation, wood/03-Order … | | | open |
| `ItemProperty/UsabilityPeriod` | 0..1 | wood/01-RequestForQuotation, wood/02-Quotation, wood/03-Order … | | | open |
| `OrderCancellation/BeneficiaryParty` | 0..n | furniture/11-OrderCancellation | | | open |
| `OrderCancellation/OriginatorCustomerParty` | 0..1 | furniture/11-OrderCancellation | | | open |
| `PriorInformationNotice/BeneficiaryParty` | 0..n | tender/01-PriorInformationNotice | | | open |
| `PriorInformationNotice/OriginatorCustomerParty` | 0..n | tender/01-PriorInformationNotice | | | open |
| `ProcurementStatus/DocumentProviderParty` | 0..1 | tender/09-ProcurementStatus | | | open |
| `ProcurementStatus/TenderRecipientParty` | 0..1 | tender/09-ProcurementStatus | | | open |
| `Quotation/BeneficiaryParty` | 0..n | furniture/01-RequestForQuotation, furniture/02-Quotation | | | open |
| `Quotation/OriginatorCustomerParty` | 0..1 | furniture/01-RequestForQuotation, furniture/02-Quotation | | | open |
| `RemittanceAdviceLine/BeneficiaryParty` | 0..n | sea/27-RemittanceAdvice | | | open |
| `RemittanceAdviceLine/OriginatorCustomerParty` | 0..1 | sea/27-RemittanceAdvice | | | open |
| `RequestForQuotation/BeneficiaryParty` | 0..n | furniture/01-RequestForQuotation | | | open |
| `RequestForQuotation/OriginatorCustomerParty` | 0..1 | furniture/01-RequestForQuotation | | | open |
| `RequestForQuotationLine/SecurityClassificationCode` | 0..1 | furniture/01-RequestForQuotation, wood/01-RequestForQuotation | | | open |
| `Statement/BeneficiaryParty` | 0..n | sea/25-Statement | | | open |
| `Statement/OriginatorCustomerParty` | 0..1 | sea/25-Statement | | | open |
| `StatementLine/BeneficiaryParty` | 0..n | sea/25-Statement | | | open |
| `StatementLine/OriginatorCustomerParty` | 0..1 | sea/25-Statement | | | open |
| `StatementLine/SellerSupplierParty` | 0..1 | sea/25-Statement | | | open |
| `Tender/BeneficiaryParty` | 0..n | tender/15-Tender, tender/17-Tender, tender/19-Tender | | | open |
| `Tender/OriginatorCustomerParty` | 0..1 | tender/15-Tender, tender/17-Tender, tender/19-Tender | | | open |
| `TenderLine/ReplacementRelatedItem` | 0..n | tender/15-Tender, tender/17-Tender, tender/19-Tender | | | open |
| `TenderingTerms/AdditionalInformationParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/ContractResponsibleParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/DocumentProviderParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/QualificationRequestRecipientParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/TenderEvaluationParty` | 0..n | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/TenderRecipientParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TransitCustomsDeclaration/FreightForwarderParty` | 0..1 | rail/06-TransitCustomsDeclaration | | | open |
| `TransportProgressStatus/SourceIssuerParty` | 0..1 | rail/05-TransportProgressStatus | | | open |

### C01: apply the approved party table; O147: share capital in Urvania only

Coverage 4996 → 4993 (commit df5d1101), 3 elements.

> O145, Party table (C01, 4996 → 4993): `PartyLegalEntity/ShareholderParty` with its `ParticipationPercent` and `Party` (only Castrano Logistics has a shareholder, Valdara with 100 %, and no document presents Castrano). Candidate real cases: a qualification in which Valdara relies on its subsidiary Castrano for delivery and installation (D28), or a business card from Castrano.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `PartyLegalEntity/ShareholderParty` | 0..n | road/01-Order, road/04-DespatchAdvice, road/11-ReceiptAdvice … | | | open |
| `ShareholderParty/ParticipationPercent` | 0..1 | road/01-Order, road/04-DespatchAdvice, road/11-ReceiptAdvice … | | | open |
| `ShareholderParty/Party` | 0..1 | road/01-Order, road/04-DespatchAdvice, road/11-ReceiptAdvice … | | | open |

### Stage 2: C51, C55 payment terms in three layers (D22, D23, O70, O73)

Coverage 4993 → 4992 (commit 0cbe740c), 1 element.

> O145, Stage 2, C55 (4993 → 4992): `RemittanceAdviceLine/Note` (the electricity bill's 2 % discount taken, which the Accord's utility term no longer gives). Candidate real cases: a buyer that pays an Urvanian seller within ten days and takes the 2 % of `XU-STD` (Lumeway paying Valdara's road invoice, road/17), or a short payment explained on the line.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|

### Stage 2: C50 (no tax section in Lisavan sales), C54 (withholding, D17)

Coverage 4992 → 4982 (commit 87db8c59), 10 elements.

> O145, Stage 2, C50 and C54 (4992 → 4982): `TaxTotal` and `TaxPointDate` of SelfBilledInvoice and SelfBilledCreditNote, `AllowanceCharge/TaxTotal` (the only self-billed documents are Lisavan, and a Lisavan sale has no tax section, D15); `Duty/TaxCategory`, `TelecommunicationsService/TaxTotal` and `TelecommunicationsSupplyLine/TaxTotal` (the only telecom statement is Lisavan); `Reminder/PrepaidPayment` and `Reminder/TaxRepresentativeParty` (the withholding receipt read as a payment on account, and a representative with no tax on the reminder, tender/35#F4, #F10). Candidate real cases: self-billing in Urvania or Bayvarra with tax, such as an Urvanian buyer that self-bills its supplier under VAT (the scrap or ore deliveries) or the energy flow's monthly settlement; an Urvanian or Bayvarran telecom statement with VAT per service; a reminder of an invoice paid in part (a payment on account received); a reminder from a non-resident seller that charges a tax its representative accounts for.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `AllowanceCharge/TaxTotal` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `Duty/TaxCategory` | 0..1 | utilities/12-UtilityStatement | | | open |
| `Reminder/PrepaidPayment` | 0..n | tender/35-Reminder | | | open |
| `Reminder/TaxRepresentativeParty` | 0..1 | tender/35-Reminder | | | open |
| `SelfBilledCreditNote/TaxPointDate` | 0..1 | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledCreditNote/TaxTotal` | 0..n | cotton/05-SelfBilledCreditNote | | | open |
| `SelfBilledInvoice/TaxPointDate` | 0..1 | cotton/04-SelfBilledInvoice | | | open |
| `SelfBilledInvoice/TaxTotal` | 0..n | cotton/01-SelfBilledInvoice, cotton/04-SelfBilledInvoice | | | open |
| `TelecommunicationsService/TaxTotal` | 0..n | utilities/12-UtilityStatement | | | open |
| `TelecommunicationsSupplyLine/TaxTotal` | 0..n | utilities/12-UtilityStatement | | | open |

### C48: apply the approved item table (D11, O20)

Coverage 4982 → 4971 (commit 11566a00), 11 elements.

> O145, Stage 2, C48, the item table (4982 → 4971): `Item/EnvironmentalCertificate` (the recycled granulate), `CircularityProfile` with `CircularityTypeCode`, `RecycledContentPercent`, `RecyclabilityPercent` and `EndOfLifeTreatment` with its `ImpactCode`, `ProcessingTypeCode`, `TreatmentLocation` and `TreatmentPathwayCode`, and `Item/LifecycleStageCode` and `LifecycleStageDescription` (the pallet film): both items appear only in orders, invoices and customs documents. Candidate real cases: the recycled-content certificate of D41 (plastics); a catalogue or product information of Rivermouth for its film; a rule that makes a buyer prove the recycled content of plastic packaging, as the United Kingdom's plastic packaging tax does.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CircularityProfile/EndOfLifeTreatment` | 0..1 | packaging/01-Order, packaging/02-Invoice | the stretch film's product information from Rivermouth (a catalogue of the film to Valdara, packaging flow): recyclable in full, back to Rinova for recycling (the film's data in world/items.json) | packaging | candidate |
| `CircularityProfile/RecyclabilityPercent` | 0..1 | packaging/01-Order, packaging/02-Invoice | the stretch film's product information from Rivermouth (a catalogue of the film to Valdara, packaging flow): recyclable in full, back to Rinova for recycling (the film's data in world/items.json) | packaging | candidate |
| `EndOfLifeTreatment/ImpactCode` | 0..1 | packaging/01-Order, packaging/02-Invoice | with `CircularityProfile/EndOfLifeTreatment`: the film's end of life in Rivermouth's product information (packaging, G1's candidate), or the spent Mo-99/Tc-99m generator's (decay storage, recovery of the shielding) if the medicines flow carries its product data (O202 choice 7) | packaging or medicines | candidate |
| `EndOfLifeTreatment/ProcessingTypeCode` | 0..1 | packaging/01-Order, packaging/02-Invoice | with `CircularityProfile/EndOfLifeTreatment`: the film's end of life in Rivermouth's product information (packaging, G1's candidate), or the spent Mo-99/Tc-99m generator's (decay storage, recovery of the shielding) if the medicines flow carries its product data (O202 choice 7) | packaging or medicines | candidate |
| `EndOfLifeTreatment/TreatmentLocation` | 0..1 | packaging/01-Order, packaging/02-Invoice | with `CircularityProfile/EndOfLifeTreatment`: the film's end of life in Rivermouth's product information (packaging, G1's candidate), or the spent Mo-99/Tc-99m generator's (decay storage, recovery of the shielding) if the medicines flow carries its product data (O202 choice 7) | packaging or medicines | candidate |
| `EndOfLifeTreatment/TreatmentPathwayCode` | 0..1 | packaging/01-Order, packaging/02-Invoice | with `CircularityProfile/EndOfLifeTreatment`: the film's end of life in Rivermouth's product information (packaging, G1's candidate), or the spent Mo-99/Tc-99m generator's (decay storage, recovery of the shielding) if the medicines flow carries its product data (O202 choice 7) | packaging or medicines | candidate |

### C62: the Elderwick Marrow bench, chair and care kit as items of their own under Brightmarket's GTINs; the set a shop offer; indoor dining furniture (D32)

Coverage 4971 → 4961 (commit 7c976a98), 10 elements.

> O145, C62/D32 (2026-11-19), 10 elements lost (4971 → 4961): ItemManagementProfile/FrozenPeriodDaysNumeric; ActivityDataLine/ActivityFinalLocation, /BuyerCustomerParty, /SellerSupplierParty; LineItem/SubLineItem, InvoiceLine/SubInvoiceLine (the set's sub-lines); CreditNoteLine/AllowanceCharge, /ItemPriceExtension, BillingReferenceLine/AllowanceCharge (the restocking deduction); CatalogueLine/ComplementaryRelatedItem (retail/02).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ActivityDataLine/ActivityFinalLocation` | 0..1 | furniture/06-ProductActivity | | | open |
| `ActivityDataLine/BuyerCustomerParty` | 0..1 | furniture/06-ProductActivity | | | open |
| `ActivityDataLine/SellerSupplierParty` | 0..1 | furniture/06-ProductActivity | | | open |
| `BillingReferenceLine/AllowanceCharge` | 0..n | furniture/14-DebitNote | | | open |
| `CatalogueLine/ComplementaryRelatedItem` | 0..n | retail/02-Catalogue | the care kit as the complement of the Marrow bench in Brightmarket's or Brackenmere's catalogue, or seat pads for the Marrow chair once the seat-pad line is settled (D32); the owner asked for a new home | furniture or retail | candidate |
| `CreditNoteLine/AllowanceCharge` | 0..n | furniture/13-CreditNote | | | open |
| `CreditNoteLine/ItemPriceExtension` | 0..1 | furniture/13-CreditNote | | | open |
| `InvoiceLine/SubInvoiceLine` | 0..n | furniture/09-Invoice | | | open |
| `ItemManagementProfile/FrozenPeriodDaysNumeric` | 0..1 | furniture/04-TradeItemLocationProfile | | | open |

### O155: the Marrow line's first sale on the reopening day, 11 May; the sales side of the furniture flow from then on (owner)

Coverage 4961 → 4958 (commit b53fd04a), 3 elements.

> O145, O155 (2026-11-19), 3 elements lost (4961 → 4958): SalesItem/TaxExclusivePrice, SalesItem/TaxInclusivePrice and ProductActivity/DocumentCurrencyCode (the activity report no longer carries the shop's prices).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ProductActivity/DocumentCurrencyCode` | 0..1 | furniture/06-ProductActivity | | | open |
| `SalesItem/TaxExclusivePrice` | 0..n | furniture/06-ProductActivity | | | open |
| `SalesItem/TaxInclusivePrice` | 0..n | furniture/06-ProductActivity | | | open |

### C63: the cotton farm's address lines go (they repeated its structured address); the yearly registration stays

Coverage 4958 → 4956 (commit 14f7152b), 2 elements.

> O145, C63 (2026-11-19), 2 elements lost (4958 → 4956): `PostalAddress/AddressLine` and `AddressLine/Line` (the farm's lines repeated its structured address); candidate real case: an address the structured fields cannot carry, such as directions to a site without a street, or an address from a country whose format the receiver does not know.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Address/AddressLine` | 0..n | cotton/01-SelfBilledInvoice, cotton/03-DeliveryNote, cotton/04-SelfBilledInvoice … | | | open |
| `AddressLine/Line` | 1..n | cotton/01-SelfBilledInvoice, cotton/03-DeliveryNote, cotton/04-SelfBilledInvoice … | | | open |

### Merge C83, C84, C94, C109: energy, packaging, utilities and cotton slips

Coverage 4956 → 4954 (commit 3dfd90d6), 2 elements.

> O145, C83 (2026-11-19), 2 elements lost (4956 → 4954): `ReminderLine/ExchangeRate` (utilities/10) and `RemittanceAdviceLine/ExchangeRate` (sea/27), since the energy reminder and its payment are now in ferra; candidate real case: a reminder or remittance between parties that keep their accounts in different currencies (the island's coral against the ferra).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ReminderLine/ExchangeRate` | 0..1 | energy/08-Reminder | | | open |
| `RemittanceAdviceLine/ExchangeRate` | 0..1 | energy/09-RemittanceAdvice | | | open |

### C47 with C09: the bench's footprint by life cycle stage, without factor and boundary

Coverage 4954 → 4951 (commit baad0535), 3 elements.

> O145, Stage 4 (2026-11-19), 4 elements lost (4954 → 4950): `EnvironmentalEmission/ValueFactorNumeric` and `/ValueBaseMeasure` (the bench's footprint is now two stage figures; candidate real case: rail/08's 410 kg CO2e as 1,220 kWh of traction energy × Urvania's grid factor, about 0.336 kg/kWh, for the owner to set); `EmissionCalculationMethod/FullnessIndicationCode` (candidate: an empty return run, such as D48's LPG tanker, with a full/partial/empty list); `ItemInstance/RegistrationID` (dropped from the castings, D46; candidate: a registered item, such as a calibrated data logger in the medicines flow).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|

### C70: one melt per casting day, one coating batch per lot, from the production record

Coverage 4951 → 4950 (commit 7cc3085e), 1 element.

> O145, Stage 4 (2026-11-19), 4 elements lost (4954 → 4950): `EnvironmentalEmission/ValueFactorNumeric` and `/ValueBaseMeasure` (the bench's footprint is now two stage figures; candidate real case: rail/08's 410 kg CO2e as 1,220 kWh of traction energy × Urvania's grid factor, about 0.336 kg/kWh, for the owner to set); `EmissionCalculationMethod/FullnessIndicationCode` (candidate: an empty return run, such as D48's LPG tanker, with a full/partial/empty list); `ItemInstance/RegistrationID` (dropped from the castings, D46; candidate: a registered item, such as a calibrated data logger in the medicines flow).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ItemInstance/RegistrationID` | 0..1 | air/06-DespatchAdvice, air/08-DespatchAdvice, road/04-DespatchAdvice … | | | open |

### O170, C107: Lisavu's Department of Agriculture issues the phytosanitary certificate

Coverage 4950 → 4947 (commit 964ca3d7), 3 elements.

> O145, O170 (2026-11-19), 3 elements lost (4950 → 4947): `GoodsCertificate/FreightForwarderParty` (candidate: a certificate the forwarder applies for and collects for the exporter, as in the medicines flow, D47); `GoodsCertificate/LegalAuthorityParty` (candidate: an inspection company authorised by the Plant Protection Service, ISPM 7, or a GDP certificate under the medicines agency); `GoodsCertificate/PreviousDocumentReference` (candidate: a replacement phytosanitary certificate, ISPM 12, when the bales are rebooked on a later ship).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `GoodsCertificate/LegalAuthorityParty` | 0..1 | cotton/10-GoodsCertificate | | | open |
| `GoodsCertificate/PreviousDocumentReference` | 0..1 | cotton/10-GoodsCertificate | | | open |

### Stage 5, C72 and C73 (2026-11-19)

Coverage 4947 → 4937 (commits 80c237bd to ea814dd4), 10 elements. The job's report named eight; `GoodsItem/ReceiptLineReference` (road/14) and `ShipmentStage/ActualWaypointTransportEvent` (rail/08) were lost in its first commits without being reported, found when this register was made.

> O145, Stage 5: `Invoice/StatementDocumentReference` (candidate: a utility bill citing the account statement that shows an unpaid balance); `InvoiceStatusResponse/Payment`, `Payment/BillingReference`, `Payment/RemittanceDocumentReference` (candidate: a second status response in the sea flow, issued after the payment of 25 June); `TenderingTerms/ReplacedNoticeDocumentReference` (candidate: the contest's version-2 notices, contest/02 or 08, with D29); `CatalogueRequest/RequestedCatalogueReference` (candidate: the store asking for an update of the catalogue retail/02); `OrderResponse/OrderDocumentReference` (candidate: a response to a replacement or repeat order naming the earlier order); `RetailEvent/OriginalDocumentReference` (candidate: a revised retail event citing the forecast it was based on).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CatalogueRequest/RequestedCatalogueReference` | 0..1 | retail/01-CatalogueRequest | | | open |
| `GoodsItem/ReceiptLineReference` | 0..1 | road/14-Invoice | | | open |
| `Invoice/StatementDocumentReference` | 0..n | air/10-Invoice, cotton/04-SelfBilledInvoice | | | open |
| `InvoiceStatusResponse/Payment` | 0..n | sea/24-InvoiceStatusResponse | | | open |
| `OrderResponse/OrderDocumentReference` | 0..n | tender/28-OrderResponse | | | open |
| `Payment/BillingReference` | 0..n | sea/24-InvoiceStatusResponse | | | open |
| `Payment/RemittanceDocumentReference` | 0..1 | sea/24-InvoiceStatusResponse | | | open |
| `RetailEvent/OriginalDocumentReference` | 0..n | retail/06-RetailEvent | | | open |
| `ShipmentStage/ActualWaypointTransportEvent` | 0..1 | rail/08-Waybill | | | open |
| `TenderingTerms/ReplacedNoticeDocumentReference` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |

### O172: the sea order split into the port's line and the buyer's stock lines (2026-11-19)

Coverage 4937 → 4930, 9 elements lost and 2 won back (`LineItem/OriginatorParty` and `LineItem/BeneficiaryParty`, see Won back).

> O172 (owner, a): the sea order has a line of 96 benches for the Port of Selanu, which names the port as originator and beneficiary, and a line of 8 benches and the frames line for Velumi's own stock, which do not. The order, its response, the despatch advice and the invoice cover the stock lines too, so the port is no longer the originator and beneficiary of the whole document: the document-level parties go (the invoice's port line names both). The credit note credits a spare frame of Velumi's stock, so it no longer cites the harbour parks project.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CreditNote/ProjectReference` | 0..n | sea/26-CreditNote | a credit for goods bought for the harbour parks project, such as one of the port's benches found damaged | sea | candidate |
| `DespatchAdvice/BeneficiaryParty` | 0..n | sea/20-DespatchAdvice | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `DespatchAdvice/OriginatorCustomerParty` | 0..1 | sea/20-DespatchAdvice | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `Invoice/BeneficiaryParty` | 0..n | sea/22-Invoice | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `Invoice/OriginatorCustomerParty` | 0..1 | sea/22-Invoice | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `Order/BeneficiaryParty` | 0..n | sea/05-Order | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `Order/OriginatorCustomerParty` | 0..1 | sea/05-Order | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `OrderResponse/BeneficiaryParty` | 0..n | sea/06-OrderResponse | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |
| `OrderResponse/OriginatorCustomerParty` | 0..1 | sea/06-OrderResponse | a document wholly for one beneficiary: a later order of Velumi Trading only for the Port of Selanu (replacement benches for the harbour parks), with its response, despatch advice and invoice | sea | candidate |

### G1: waste, plastics, wood (2026-11-19)

Stage 6, building group G1 (C77, C87, C88, C89).

> C77, D42, O190: the waste movement is domestic, under Urvania's environment agency. Rinova recovers the film and disposes of nothing, so it is no longer named a disposal facility (waste/01#F2, 02#F5). The customs administration no longer receives the notification and the movement, and with its border office's contact the world's only fax number went. `CustomsParty` stays: the schema requires it in a waste notification (1..n), and it names the environment agency, the competent authority (see the question in the G1 report).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Contact/Telefax` | 0..1 | waste/01-WasteNotification, waste/02-WasteMovement | | | open |
| `WasteMovement/DisposalFacilityParty` | 0..1 | waste/02-WasteMovement | a waste whose operation is disposal (a D code of Basel Annex IV), such as Rinova's sorting residue (labels, contaminated film) sent to an incinerator under its own notification and movement reports (O190) | waste | candidate |
| `WasteNotification/DisposalFacilityParty` | 0..1 | waste/01-WasteNotification | the same: the residue's own notification, with the incinerator as disposal facility (O190) | waste | candidate |

> C87, D41: the barge's consignment note no longer gives a value for duties (06#F11), nor the bags as a returnable quantity of the goods (06#F9; the bag stays returnable on its package), and the bag's height moves to the bag (06#F13). The granulate's despatch advice gives no best-before or expiry date: polymer granulate has none (08#F6).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `GoodsItem/MeasurementDimension` | 0..n | plastics/06-Waybill | | | open |
| `GoodsItem/ReturnableQuantity` | 0..1 | plastics/06-Waybill | | | open |
| `GoodsItem/ValueAmount` | 0..1 | plastics/06-Waybill | the amount the island's import consumption tax of 10 % is assessed on, the landed value of a goods item in an import declaration into Lisavu (D18; "the amount on which a duty, tax, or fee will be assessed") | sea | candidate |
| `ItemInstance/BestBeforeDate` | 0..1 | plastics/08-DespatchAdvice |  |  | open |

> C89, D43: the sawmill sells the bundle of 50 slats as its item, so quotation, order and invoice are in bundles and no price converts a piece price into a pack (02#F13, 03#F10, 08#F14); the quotation's main line is oak with ash as the priced alternative, and the 35 mm substitute goes (02#F16).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Price/OrderableUnitFactorRate` | 0..1 | wood/02-Quotation, wood/03-Order, wood/08-Invoice | | | open |
| `QuotationLine/SellerProposedSubstituteLineItem` | 0..1 | wood/02-Quotation | | | open |

### G2: carnet, mast, air (2026-11-19)

Stage 6, building group G2 (C78 with C57's carnet/03#F1, F2; C79, C80; C85, C86).

> C78, D40: the carnet as issued is stamped nowhere; the chambers quote the stamped counterfoils afterwards. The carnet names no office of subsequent entry: the samples enter the island at Selanu airport, which the importation counterfoil names (carnet/01#F17). The representative is named by first and family name, title and passport only: the middle name, the "other name" (UBL: a second family name) and the suffix had no reason (01#F5, F14). The proof's attachment is a scan, described, not a sentence in place of the document (04#F10).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Consignment/OfficeOfSubSequentiallyEntryLocation` | 0..1 | carnet/01-GoodsItemPassport | the containers of the rail flow enter Bayvarra at the rail border station and are cleared at Bayvarra customs' inland office at Marrowdale, a facility where goods are processed after their initial entry point (D37, rail/14) | rail | candidate |
| `Person/MiddleName` | 0..1 | carnet/01-GoodsItemPassport | | | open |
| `Person/NameSuffix` | 0..1 | carnet/01-GoodsItemPassport | | | open |
| `Person/OtherName` | 0..1 | carnet/01-GoodsItemPassport | | | open |

> C79, D36, O182: the mast flow, the world's only dangerous-goods flow so far, keeps only the data its carriage uses. It goes by road and air, not by sea, so no emergency schedules for ships (EmS) and no marine pollutant code; not by road alone, so no tunnel code; packages by air carry no orange plates, and a truck with packages shows blank ones (mast/02#F6, 03#F7); no placard endorsement that repeats the class or the label model (02#F21, F23); no emergency temperature (D36 point 5); americium-241 is not fissile, so the pack's nuclide and activity are in the radioactive material's name, not in `ApplicableRadioactiveIsotope` (02#F9, O127); no pricing reference in the invoice that only repeats the dangerous-goods indicator (05#F3).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `DeliveryUnit/HazardousRiskIndicator` | 0..1 | mast/05-Invoice | | | open |
| `HazardousItem/EmergencyProceduresCode` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | the Trade Accord's emergency card for the propane's class (TEC2), the instructions in writing the road tanker carries, as the secondary hazard already uses it (D48) | lpg | candidate |
| `HazardousItem/EmergencyTemperature` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill | a self-reactive substance or organic peroxide whose control and emergency temperatures the rules set; the world has none (O126) | | open |
| `HazardousItem/MaritimePollutantCode` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | | | open |
| `HazardousItem/PlacardEndorsement` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | an endorsement a rule asks for on the papers; none in the world so far (O126) | | open |
| `ItemLocationQuantity/HazardousRiskIndicator` | 0..1 | mast/05-Invoice | | | open |
| `RadioactiveIsotope/ActivityLevelMeasure` | 1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | only under `ApplicableRadioactiveIsotope`, for fissile contents, which the world does not have (O126, O127) | | open |
| `RadioactiveIsotope/Name` | 1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | as above (O127) | | open |
| `RadioactiveMaterial/ApplicableRadioactiveIsotope` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | fissile contents only; the world has none (O126, O127) | | open |
| `SecondaryHazard/PlacardEndorsement` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill, mast/04-DespatchAdvice | as for the hazardous item (O126) | | open |

> C80, D36 point 3, O210: no active container on the mast flight: lithium batteries on a flight of under three hours in the island's winter need no temperature control, so the reefer settings, the food approvals and the temperatures go from the forwarding instructions and the waybill (mast/02#F17, 03#F18), and with them the road emergency card and the "not toxic" zone on the air consignment's transit data; the dangerous goods' transit data is stated once, on each loaded item (02#F17). The cold chain comes back with the medicines flow (D47, O124), the reefer settings with the fresh produce by sea (O137, O205).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `HazardousGoodsTransit/InhalationToxicityZoneCode` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill | a gas or liquid toxic by inhalation; the world has none | | open |
| `HazardousGoodsTransit/MaximumTemperature` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill | | | open |
| `HazardousGoodsTransit/MinimumTemperature` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill | | | open |
| `HazardousItem/AdditionalTemperature` | 0..n | mast/02-ForwardingInstructions, mast/03-Waybill | | | open |
| `TransportEquipment/AnimalFoodApprovedIndicator` | 0..1 | mast/02-ForwardingInstructions, mast/03-Waybill | | | open |
| `TransportEquipment/HazardousGoodsTransit` | 0..n | mast/02-ForwardingInstructions, mast/03-Waybill | | | open |

> C85, C86, D39: the urgent frames fly on a direct air waybill, one small consignment on a named flight, so the consolidation, the house consignment and its sequence number go (air/04#F2, F7); the forwarder trucks the skid to the terminal itself and Nalevi collects it at Selanu, so no substitute carrier (04#F6); CPT is stated once, on the order change's air line, so neither the order change nor its delivery carries delivery terms (01#F5); the acceptance is unconditional, so it has no validity period (02#F4).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Consignment/ChildConsignment` | 0..n | air/04-Waybill | a forwarder's consolidation under a master air waybill or a groupage bill of lading, with the house consignments as children; none decided | | open |
| `Consignment/ChildConsignmentQuantity` | 0..1 | air/04-Waybill | as above | | open |
| `Consignment/ConsolidatedShipment` | 0..n | air/04-Waybill | as above | | open |
| `Consignment/SequenceID` | 0..1 | air/04-Waybill | as above | | open |
| `Consignment/SubstituteCarrierParty` | 0..1 | air/04-Waybill | a carrier that performs the carriage in place of the contracting carrier, such as an airline's road feeder service; none decided | | open |
| `Delivery/DeliveryTerms` | 0..1 | air/01-OrderChange | | | open |
### G3: ore, rail (2026-11-19)

Stage 6, building group G3 (C81, C90).

> C81, D45: the ore train's transport request has no status, so it gives no status reason; how it updates the standing plan is said next to its reference to the plan (ore/02#F4, F5).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TransportExecutionPlanRequest/DocumentStatusReasonCode` | 0..1 | ore/02-TransportExecutionPlanRequest | | | open |
| `TransportExecutionPlanRequest/DocumentStatusReasonDescription` | 0..1 | ore/02-TransportExecutionPlanRequest | | | open |

> C90, D37: a freight train carries no passengers, so the stages state no passenger quantity (03#F20, 08#F22). The waybill describes both containers alike and drops what did not fit: the wagon given as equipment "contained in" the container (08#F8; UBL's name and definition disagree, recorded for the TC), the hub's stack as the storage location of a box that is on the train (08#F10; the stack is now the place of the box's handling event), the terminal as operator of the carrier's own box (08#F15), the reference from the box to the waybill it stands in (08#F21) and the Container Convention indicator, which nothing in the story settles (08#F25).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TransportEquipment/ContainedInTransportEquipment` | 0..n | rail/08-Waybill | | | open |
| `TransportEquipment/LegalStatusIndicator` | 0..1 | rail/08-Waybill | | | open |
| `TransportEquipment/OperatingParty` | 0..1 | rail/08-Waybill | | | open |
| `TransportEquipment/ShipmentDocumentReference` | 0..n | rail/08-Waybill | | | open |

### G7: furniture, retail, packaging (2026-11-19)

Stage 6, building group G7 (C103 to C105, C110 to C113, the packaging leftovers).

> C103, D32, D38: the store's buyer-issued debit note furniture/14 goes (O6, D9): the store invoices the return transport (furniture/18), so its debit-note elements go with it; the invoice of the opening stock cites the maker's despatch advice furniture/19 instead of a delivery note that exists nowhere (09#F1); the order takes the quoted price without an 'original' price (08#F8); the cancellation refers to the maker's exception notification as an additional document, not as an originator document (11#F4); the request for quotation refers to the store's range plan as an additional document, not as a catalogue (01#F2).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BillingReferenceLine/Amount` | 0..1 | furniture/14-DebitNote |  |  | open |
| `DebitNote/DefaultLanguageCode` | 0..1 | furniture/14-DebitNote |  |  | open |
| `DebitNoteLine/Delivery` | 0..n | furniture/14-DebitNote |  |  | open |
| `DebitNoteLine/DiscrepancyResponse` | 0..n | furniture/14-DebitNote |  |  | open |
| `Invoice/DeliveryNoteDocumentReference` | 0..n | furniture/09-Invoice |  |  | open |
| `LineItem/PricingReference` | 0..1 | furniture/08-Order |  |  | open |
| `OrderCancellation/OriginatorDocumentReference` | 0..1 | furniture/11-OrderCancellation |  |  | open |
| `RequestForQuotation/CatalogueDocumentReference` | 0..1 | furniture/01-RequestForQuotation |  |  | open |

> C104, D32 (Encoding): each collaboration document carries one kind of criterion per line: the maker asks for sales only (03#F1), the criteria and the notification are sales criteria without a performance metric (05#F2, 07#F1), and the notification reports no forecast exception, because the flow has no forecast it could compare (07#F1, F3 to F5); the criteria give no exception status, which UBL defines for shipments (05#F8).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ExceptionCriteriaLine/ExceptionStatusCode` | 0..1 | furniture/05-ExceptionCriteria |  |  | open |
| `ExceptionCriteriaLine/PerformanceMetricTypeCode` | 0..1 | furniture/05-ExceptionCriteria |  |  | open |
| `ExceptionNotificationLine/ForecastException` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ExceptionNotificationLine/PerformanceMetricTypeCode` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/ComparisonDataCode` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/ComparisonForecastIssueDate` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/ComparisonForecastIssueTime` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/DataSourceCode` | 1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/ForecastPurposeCode` | 1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/ForecastTypeCode` | 1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/IssueDate` | 1 | furniture/07-ExceptionNotification |  |  | open |
| `ForecastException/IssueTime` | 0..1 | furniture/07-ExceptionNotification |  |  | open |
| `ItemInformationRequestLine/ForecastTypeCode` | 0..1 | furniture/03-ItemInformationRequest |  |  | open |
| `ItemInformationRequestLine/PerformanceMetricTypeCode` | 0..1 | furniture/03-ItemInformationRequest |  |  | open |

> C110, D34: Lumeway's catalogue for the store is new, version 1.0 with no version before it (02#F2); its bench line carries no comparison that repeats the unit price (02#F13); the request names the real Harmonized System without an invented UUID or a midnight revision time (01#F7); the updates repeat no trading terms they do not change (03#F9, 04#F12); the deletion states only when it takes effect (20#F4).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Catalogue/PreviousVersionID` | 0..1 | retail/02-Catalogue |  |  | open |
| `CatalogueDeletion/ValidityPeriod` | 0..n | retail/20-CatalogueDeletion |  |  | open |
| `CatalogueItemSpecificationUpdate/TradingTerms` | 0..n | retail/04-CatalogueItemSpecificationUpdate |  |  | open |
| `CatalogueLine/ItemComparison` | 0..n | retail/02-Catalogue |  |  | open |
| `CataloguePricingUpdate/TradingTerms` | 0..n | retail/03-CataloguePricingUpdate |  |  | open |
| `ClassificationScheme/LastRevisionTime` | 0..1 | retail/01-CatalogueRequest |  |  | open |
| `ClassificationScheme/UUID` | 0..1 | retail/01-CatalogueRequest |  |  | open |
| `ItemComparison/PriceAmount` | 0..1 | retail/02-Catalogue |  |  | open |
| `ItemComparison/Quantity` | 0..1 | retail/02-Catalogue |  |  | open |

### G5: road (2026-11-19)

Stage 6, building group G5 (C100, C101, C102; D35).

> C100, D35 point 4: the order states no maximum delivery unit, which no delivery of the flow uses (01#F11); the carrier's status no longer reports a temperature the goods do not need (09#F11), nor an indicator that said nothing (09#F10); the application response no longer names the issuer and recipient of the invoice it answers (16#F11).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Delivery/MaximumDeliveryUnit` | 0..1 | road/01-Order | | | open |
| `DocumentResponse/IssuerParty` | 0..1 | road/16-ApplicationResponse | | | open |
| `DocumentResponse/RecipientParty` | 0..1 | road/16-ApplicationResponse | | | open |

> C101, D35 point 2: the chamber certifies and is the only endorser; the embassy endorsement by the Trade Accord Council goes, since a certificate between Accord members needs no legalisation (07#F10), and so does the insurer's endorsement (06#F3, 07#F9); the application is a first one and names no previous job (06#F17, 07#F18).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CertificateOfOrigin/EmbassyEndorsement` | 0..1 | road/07-CertificateOfOrigin | | | open |
| `CertificateOfOrigin/InsuranceEndorsement` | 0..1 | road/06-CertificateOfOrigin, road/07-CertificateOfOrigin | | | open |
| `CertificateOfOriginApplication/PreviousJobID` | 0..1 | road/06-CertificateOfOrigin, road/07-CertificateOfOrigin | | | open |

> C102, D35 point 3: the order response substitutes the 2026 casting and proposes no other substitute; the old casting it proposed from stock was the item ordered (02#F6).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `OrderLine/SellerProposedSubstituteLineItem` | 0..n | road/02-OrderResponse | | | open |

### G6: contest, tender (2026-11-19)

Stage 6, building group G6 (C96 to C99, C119 to C128; D28, D29).

> C96, D29 points 6 and 11: the tender's self-declaration asks what the notices announce (exclusion grounds, register, years, turnover, staff, three similar supplies, certified timber, a group's shares), each limit once in the element of its data type and as a question; the request states no fulfilment, and no expected values that are only thresholds (tender/06#F4 to F8, F13 to F16). Brackenmere's response answers each question in its own criterion response, each value in the element of the property's kind (tender/07#F1, F4, F5). The debt ratio, which no notice announced, goes, and with it the only upper limits; a validity date of the timber certificate was not asked as a date, because a response date in the future reads as a fact reported after the issue (C72).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ResponseValue/ResponseBinaryObject` | 0..1 | tender/07-QualificationApplicationResponse | | | open |
| `ResponseValue/ResponseDate` | 0..1 | tender/07-QualificationApplicationResponse | | | open |
| `ResponseValue/ResponseMeasure` | 0..1 | tender/07-QualificationApplicationResponse | | | open |
| `ResponseValue/ResponseNumeric` | 0..1 | tender/07-QualificationApplicationResponse | | | open |
| `ResponseValue/ResponseTime` | 0..1 | tender/07-QualificationApplicationResponse | | | open |
| `TenderingCriterion/FulfilmentIndicatorTypeCode` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterion/FulfilmentIndicator` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterion/SubTenderingCriterion` | 0..n | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/ExpectedAmount` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/ExpectedCode` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/ExpectedID` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/ExpectedURI` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/ExpectedValueNumeric` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/MaximumQuantity` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/MaximumValueNumeric` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionProperty/MinimumValueNumeric` | 0..1 | tender/06-QualificationApplicationRequest | | | open |
| `TenderingCriterionPropertyGroup/FulfilmentIndicator` | 0..1 | tender/06-QualificationApplicationRequest | | | open |

> C97, D29 points 1, 9 and 11, O101: `PublishAwardIndicator` goes from the contest's results notices and from the tender's award notice and contract: its definition names service categories for which publication is optional, and the world has none. Urvanian is declared only where a notice gives Urvanian text (the tender's prior information notice and contract notice now do); the registry's extract and the award notice give none and no longer declare it. The tender's process no longer states the defaults (normal urgency, not terminated, no reduction of candidates); the contest states the reduction of candidates in its results, after the selection.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BusinessInformation/AdditionalNoticeLanguage` | 0..n | tender/12-BusinessInformation | | | open |
| `ContractAwardNotice/AdditionalNoticeLanguage` | 0..n | tender/21-ContractAwardNotice | | | open |
| `ContractAwardNotice/PublishAwardIndicator` | 0..1 | contest/15-ContractAwardNotice, contest/16-ContractAwardNotice, tender/21-ContractAwardNotice | | | open |
| `TenderContract/PublishAwardIndicator` | 0..1 | tender/24-TenderContract | | | open |
| `TenderingProcess/TerminatedIndicator` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice … | | | open |
| `TenderingProcess/UrgencyCode` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice … | | | open |

> C125, D28 point 1: an open procedure has no invitation period and no period for requests to participate, so the notices, the call, the award notice and the procurement status no longer state them (tender/02#F1, 03#F1, 21#F2); the contest's request period stays.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ProcurementStatus/InvitationSubmissionPeriod` | 0..1 | tender/09-ProcurementStatus | | | open |
| `ProcurementStatus/ParticipationRequestReceptionPeriod` | 0..1 | tender/09-ProcurementStatus | | | open |
| `TenderingProcess/InvitationSubmissionPeriod` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice | | | open |
| `TenderingProcess/ParticipationInvitationPeriod` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice | | | open |

> C119, D28 points 2, 3, 5, 6: the tendering terms state each term once and as it is meant: no security clearance where none is required (tender/01#F1), no variant indicator next to a maximum, no concession fee for the paper copies (their price in the terms' note), no reference to an "original" framework, no negotiation indicator in an open procedure, a tender preparation for both lots, no lot terms or process that only say "as for the procedure" (the installers' curricula become lot 2's own term), and no rounded "precise" subcontract rate.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `AwardingTerms/NoFurtherNegotiationIndicator` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `ProcurementProject/FeeDescription` | 0..n | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `ProcurementProject/RequiredFeeAmount` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `ProcurementProjectLot/TenderingProcess` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice | | | open |
| `SecurityClearanceTerm/Code` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `SecurityClearanceTerm/Description` | 0..n | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `SubcontractTerms/Rate` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderPreparation/ProcurementProjectLot` | 0..n | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingProcess/OriginalContractingSystemID` | 0..1 | tender/02-ContractNotice, tender/03-CallForTenders, tender/21-ContractAwardNotice | | | open |
| `TenderingTerms/LatestSecurityClearanceDate` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/SecurityClearanceTerm` | 0..n | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |
| `TenderingTerms/VariantConstraintIndicator` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |

> C121, D28 point 2: `QualityControlCode` is for works; the inspection of the benches on delivery is an acceptance term of a supply and goes to the project's note (tender/01#F28, 02#F34, 03#F35).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ProcurementProject/QualityControlCode` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders … | | | open |

> C124, D28 point 4: the registry's extract of Valdara carries what the register holds: no group of the two competing tenderers (they are not a group, 12#F4), no operation type holding the line of business (12#F5), no publication date on an extract sent to one authority (12#F6), no brochure (12#F14), and no service provider of the business (Castrano, 12#F13; Valdara was the only party with one in its presentation); Valdara's qualification gives no party capacity that repeats the task's amount (13#F12); the procurement status cites only the act's rule on deadlines it rests on (09#F5).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `BusinessInformation/BrochureDocumentReference` | 0..n | tender/12-BusinessInformation | | | open |
| `CompletedTask/PartyCapacityAmount` | 0..1 | tender/13-TendererQualification | | | open |
| `BusinessInformation/BusinessPartyGroup` | 0..n | tender/12-BusinessInformation | | | open |
| `BusinessInformation/OperationType` | 0..1 | tender/12-BusinessInformation | | | open |
| `BusinessInformation/RequestedPublicationDate` | 0..1 | tender/12-BusinessInformation | | | open |
| `OperationType/Code` | 0..1 | tender/12-BusinessInformation | | | open |
| `OperationType/Description` | 0..n | tender/12-BusinessInformation | | | open |
| `PartyGroup/GroupType` | 0..n | tender/12-BusinessInformation | | | open |
| `PartyGroup/GroupTypeCode` | 0..1 | tender/12-BusinessInformation | | | open |
| `PartyGroup/Party` | 1..n | tender/12-BusinessInformation | | | open |
| `ProcurementStatus/EmploymentLegislationDocumentReference` | 0..n | tender/09-ProcurementStatus | | | open |
| `ProcurementStatus/EnvironmentalLegislationDocumentReference` | 0..n | tender/09-ProcurementStatus | | | open |
| `ProcurementStatus/FiscalLegislationDocumentReference` | 0..n | tender/09-ProcurementStatus | | | open |
| `ServiceProviderParty/ID` | 0..1 | tender/12-BusinessInformation | | | open |

> C126: the article of the procurement act a guarantee follows is referred to by its legal reference, not as an ontology (tender/14#F8).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Regulation/OntologyURI` | 0..1 | tender/14-GuaranteeCertificate | | | open |

> C120, C123, C128, D28 points 8 to 10, O6, O12, O50, O69: the call-off executes the contract as signed. The contract, the catalogue and every document of the release are in lume, the contract's currency, so no pricing currency, pricing exchange rate or base rates of 1 (C11's tender part: 26#F1, 27#F8, 28#F7, 32#F6, F9, F14, 33#F3, 35#F8); the order change and the response carry no tax or pricing currency of their own (27#F8, 28#F7), the reminder no pricing or tax currency (35#F8), the credit note no payment currency, being deducted (33#F13); the order documents cite the contract by its number, not the procedure as originator (26#F14, 27#F11, 32#F19); the order change names no forwarder, payment means, payment terms or conditions it does not change (27#F9, F10), and the special colour is quoted in the catalogue, not a quotation of its own (D28 point 8); the despatch advice shows no 200 benches outstanding (29#F3, D28's goods balance) and no back-ordered anchor sets or spare bolts (40 sets, no loose bolts, O10); the invoice of the benches bills no installation and carries no annotation of the 200 still open; the credit note credits the bench and its colour charge only, once settled (deducted), with no period, no sub-line, no ferra alternative price, no withholding or tax representative (no installation credited), no work report the world has not got (33#F1, F7, F12, F15 to F17); the debit note tender/34 is removed (D9, O6: the penalty is a deduction in the remittance advice), and with it the reminder's and the remittance's references to it. Kept: Valdara's VAT in ferra (the tax currency, its rate and the tax total in ferra) on both invoices and the credit note, and payment in ferra on both invoices and the reminder (33#F13, 35#F8 option a); the seller's signature on the invoices (until the signatures stage, D6).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Annotation/Subject` | 0..n | tender/32-Invoice | | | open |
| `Annotation/SubjectCode` | 0..1 | tender/32-Invoice | | | open |
| `BillingReference/AdditionalDocumentReference` | 0..1 | tender/36-RemittanceAdvice | | | open |
| `BillingReference/DebitNoteDocumentReference` | 0..1 | tender/35-Reminder, tender/36-RemittanceAdvice | | | open |
| `CreditNote/DeliveryNoteDocumentReference` | 0..n | tender/33-CreditNote | | | open |
| `CreditNote/PaymentCurrencyCode` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/PaymentExchangeRate` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/PricingCurrencyCode` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/PricingExchangeRate` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/PurchaseReference` | 0..n | tender/33-CreditNote | | | open |
| `CreditNote/TaxPointDate` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/TaxRepresentativeParty` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNote/WithholdingTaxTotal` | 0..n | tender/33-CreditNote | | | open |
| `CreditNote/WorkReportDocumentReference` | 0..n | tender/33-CreditNote | | | open |
| `CreditNoteLine/FreeOfChargeIndicator` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNoteLine/InvoicePeriod` | 0..n | tender/33-CreditNote | | | open |
| `CreditNoteLine/PaymentTerms` | 0..n | tender/33-CreditNote | | | open |
| `CreditNoteLine/PricingReference` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNoteLine/SubCreditNoteLine` | 0..n | tender/33-CreditNote | | | open |
| `CreditNoteLine/TaxPointDate` | 0..1 | tender/33-CreditNote | | | open |
| `CreditNoteLine/WithholdingTaxTotal` | 0..n | tender/33-CreditNote | | | open |
| `CreditNoteLine/WorkReportLineReference` | 0..n | tender/33-CreditNote | | | open |
| `DebitNote/AllowanceCharge` | 0..n | tender/34-DebitNote | | | open |
| `DebitNote/TaxRepresentativeParty` | 0..1 | tender/34-DebitNote | | | open |
| `DebitNote/WithholdingTaxTotal` | 0..n | tender/34-DebitNote | | | open |
| `DebitNoteLine/WithholdingTaxTotal` | 0..n | tender/34-DebitNote | | | open |
| `DespatchLine/BackorderQuantity` | 0..1 | tender/29-DespatchAdvice | | | open |
| `DespatchLine/BackorderReason` | 0..n | tender/29-DespatchAdvice | | | open |
| `DespatchLine/OutstandingQuantity` | 0..1 | tender/29-DespatchAdvice | | | open |
| `DespatchLine/OutstandingReason` | 0..n | tender/29-DespatchAdvice | | | open |
| `DespatchLine/OversupplyQuantity` | 0..1 | tender/29-DespatchAdvice | | | open |
| `ExchangeRate/SourceCurrencyBaseRate` | 0..1 | tender/26-Order, tender/32-Invoice | | | open |
| `ExchangeRate/TargetCurrencyBaseRate` | 0..1 | tender/26-Order, tender/32-Invoice | | | open |
| `Invoice/Annotation` | 0..n | tender/32-Invoice | | | open |
| `Invoice/OriginatorDocumentReference` | 0..n | tender/32-Invoice | | | open |
| `OrderChange/FreightForwarderParty` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/OriginatorDocumentReference` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/PaymentExchangeRate` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/PaymentMeans` | 0..n | tender/27-OrderChange | | | open |
| `OrderChange/PaymentTerms` | 0..n | tender/27-OrderChange | | | open |
| `OrderChange/PricingCurrencyCode` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/PricingExchangeRate` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/QuotationDocumentReference` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/TaxCurrencyCode` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/TaxExchangeRate` | 0..1 | tender/27-OrderChange | | | open |
| `OrderChange/TransactionConditions` | 0..1 | tender/27-OrderChange | | | open |
| `OrderResponse/PaymentExchangeRate` | 0..1 | tender/28-OrderResponse | | | open |
| `OrderResponse/PricingCurrencyCode` | 0..1 | tender/28-OrderResponse | | | open |
| `OrderResponse/PricingExchangeRate` | 0..1 | tender/28-OrderResponse | | | open |
| `OrderResponse/TaxCurrencyCode` | 0..1 | tender/28-OrderResponse | | | open |
| `OrderResponse/TaxExchangeRate` | 0..1 | tender/28-OrderResponse | | | open |
| `Price/PricingExchangeRate` | 0..1 | tender/26-Order, tender/32-Invoice | | | open |
| `Reminder/PricingCurrencyCode` | 0..1 | tender/35-Reminder | | | open |
| `Reminder/PricingExchangeRate` | 0..1 | tender/35-Reminder | | | open |
| `Reminder/TaxCurrencyCode` | 0..1 | tender/35-Reminder | | | open |
| `Reminder/TaxExchangeRate` | 0..1 | tender/35-Reminder | | | open |

> C127, D28 point 7: the Procurement Review Board is only the party appeals go to, given with its address and contact in every document that states appeal terms (a rule of `party_profile()`); there is no mediation step, and the board is not also the party for information on appeals (tender/20#F6, 23#F4; the admission notice tender/20 already carries no appeal terms, 20#F8).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `AppealTerms/AppealInformationParty` | 0..1 | tender/01-PriorInformationNotice, tender/02-ContractNotice, tender/03-CallForTenders, tender/23-UnawardedNotification | | | open |
| `AppealTerms/MediationParty` | 0..1 | tender/02-ContractNotice, tender/23-UnawardedNotification | | | open |

> C122, D28: the tenders carry no fee of their own costs: the paper copy of the documents is what the tenderer paid the department, not a fee of the tendered project (tender/15#F11, 17#F11, 19#F11); Brackenmere's courier of the original certificate stays as an additional fee (D28 point 5).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TenderedProject/FeeAmount` | 0..1 | tender/15-Tender, tender/17-Tender, tender/19-Tender | | | open |
| `TenderedProject/FeeDescription` | 0..n | tender/15-Tender, tender/17-Tender, tender/19-Tender | | | open |

> Merge of G6 with G8 (2026-11-19): two elements whose last examples went in both groups: the invoice annotation (tender/32's note of the 200 benches still open, D28; G8's cotton and sea examples no longer carry one) and the alternative condition price (tender/33's price in ferra, C11; sea/28 removed by D30).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Annotation/AnnotationContent` | 0..1 | tender/32-Invoice; cotton/04-SelfBilledInvoice, cotton/05-SelfBilledCreditNote, sea/26-CreditNote (G8) | | | open |
| `PricingReference/AlternativeConditionPrice` | 0..n | tender/33-CreditNote; sea/28-DebitNote (G8) | | | open |

### G4: energy, utilities (2026-11-19)

Stage 6, building group G4 (C82, C91, C92, C93, C95, C50's levy findings).

> C91, D31 points 2 and 5: a statement shows a second supplier only where one really bills part of the consumption (Ferrano Grid's network charges on Ferrano Energy's bill, the city's sewage levy on the water bill); the island's telephone statement has one supplier, so `Consumption` only, and with the supplier branch its consumption lines go (utilities/12#F9; UBL reaches consumption lines only under `SupplierConsumption`, a point for the TC, O107): the bundle discount on the subscription line, the subscription's price "per month" and the data pack of 5 GB (which D31 point 6 drops anyway). The consumption lines' delivery location only pointed back to the statement's consumption point (utilities/01#F14, 03#F15, 05#F13, 08#F16, 12#F21).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ConsumptionLine/AllowanceCharge` | 0..n | utilities/12-UtilityStatement | | | open |
| `ConsumptionLine/Delivery` | 0..n | utilities/01-UtilityStatement, utilities/03-UtilityStatement, utilities/05-UtilityStatement, utilities/08-UtilityStatement | | | open |
| `ConsumptionLine/UnstructuredPrice` | 0..1 | utilities/12-UtilityStatement | | | open |
| `UnstructuredPrice/PriceAmount` | 0..1 | utilities/12-UtilityStatement | | | open |
| `UnstructuredPrice/TaxInclusivePriceAmount` | 0..1 | utilities/12-UtilityStatement | | | open |
| `UnstructuredPrice/TimeAmount` | 0..1 | utilities/12-UtilityStatement | | | open |
| `UtilityItem/PackQuantity` | 0..1 | utilities/12-UtilityStatement | | | open |
| `UtilityItem/PackSizeNumeric` | 0..1 | utilities/12-UtilityStatement | | | open |

> C92, D31 point 6: the bundle discount of the telephone statement is given once, on the whole supply, as on the invoice (utilities/12#F6); the six business lines no longer repeat their share of it.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TelecommunicationsSupplyLine/AllowanceCharge` | 0..n | utilities/12-UtilityStatement | | | open |

> C93, D31 points 1 and 7: the household's annual account. The meter reader reads the meters once a year, so the reading website and its password go (D31 point 7); the open-ended recurring mandate has no limit of instructions (09#F3) and names no payer besides the debtor (09#F4); the household's account appears only in the mandate that collects from it, not again in its party block, nor in the credit note, which is set off (09#F7, 11#F5; the element stays covered by the purchase receipts); the reminder's fee line states its amount once (10#F10).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ConsumptionPoint/WebSiteAccess` | 0..1 | utilities/08-UtilityStatement | | | open |
| `PaymentMandate/MaximumPaymentInstructionsNumeric` | 0..1 | utilities/09-Invoice | | | open |
| `PaymentMandate/PayerParty` | 0..1 | utilities/09-Invoice | | | open |
| `ReminderLine/Amount` | 0..1 | utilities/10-Reminder | | | open |

> C95, D31 points 4 and 7: Valdara, which owns the warehouse, holds its subscription, so the warehouse statement's consumption names no subscriber of its own (03#F6); a monthly tariff carries no one-time charge (01#F6); a remittance advice of one bill carries no tax total (04#F2); a reminder without tax no tax point date (10#F3).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Reminder/TaxPointDate` | 0..1 | utilities/10-Reminder | | | open |
| `RemittanceAdvice/TaxTotal` | 0..n | utilities/04-RemittanceAdvice | | | open |
| `SubscriberConsumption/SubscriberParty` | 0..1 | utilities/03-UtilityStatement | | | open |
| `UtilityItem/OneTimeChargeType` | 0..n | utilities/01-UtilityStatement | | | open |
| `UtilityItem/OneTimeChargeTypeCode` | 0..1 | utilities/01-UtilityStatement | | | open |

> C111, D34: the retail event of the reopening is confirmed and agreed, so it gives no acceptance deadline (06#F7); stock on the shelf has no availability date (07#F10); the shop sale's line has no period of its own, the warranty being the maker's card (21#F12).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `PromotionalEvent/LatestProposalAcceptanceDate` | 0..1 | retail/06-RetailEvent |  |  | open |
| `PurchaseReceiptLine/PurchaseLinePeriod` | 0..1 | retail/21-PurchaseReceipt |  |  | open |

> C112, D34: the store's order offers no substitute the catalogue does not have (08#F8), gives no third-party account under its own number (08#F12) and no e-document channel as card data capability (08#F5); the document status answers for the store's order only, not for Lumeway's own transport booking (10#F4); the invoice line has no pricing reference and no payment terms of its own (18#F2, F13); the credit note on the factored invoice names no payee: the store deducts it from what it pays the factor (19#F2).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CreditNote/PayeeParty` | 0..1 | retail/19-CreditNote |  |  | open |
| `CustomerParty/AdditionalAccountID` | 0..n | retail/08-Order |  |  | open |
| `DocumentStatus/AdditionalDocumentResponse` | 0..n | retail/10-DocumentStatus |  |  | open |
| `InvoiceLine/PaymentTerms` | 0..n | retail/18-Invoice |  |  | open |
| `InvoiceLine/PricingReference` | 0..1 | retail/18-Invoice |  |  | open |
| `OrderLine/BuyerProposedSubstituteLineItem` | 0..n | retail/08-Order |  |  | open |
| `PricingReference/OriginalItemLocationQuantity` | 0..1 | retail/18-Invoice |  |  | open |
| `SupplierParty/DataSendingCapability` | 0..1 | retail/08-Order |  |  | open |

> C113, D34: the despatch advice gives the truck once, for the shipment, and no empty goods item on a pallet (12#F10); Lumeway's status request to the carrier does not name the store's order (14#F6).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `TransportHandlingUnit/GoodsItem` | 0..n | retail/12-DespatchAdvice |  |  | open |
| `TransportHandlingUnit/TransportMeans` | 0..n | retail/12-DespatchAdvice |  |  | open |
| `TransportationStatusRequest/DocumentReference` | 0..n | retail/14-TransportationStatusRequest |  |  | open |

### O226: the tender paid in lume into Valdara's lume account (2026-11-20)

> O226 (owner, 2026-11-20, option 2): Valdara holds a lume account at Bank of Lumeport (`XB13BLUM38010005341179`, main branch 380100); the tender's invoices (32, 39) and the reminder (35) ask for payment in lume into it, a domestic transfer over Lumepay; the department's remittance advice (36) is in lume throughout, with no ferra amount credited and no rate (a conversion is the banks' business). The payment currency equal to the document's goes with its rate (C11), and the order (26) gives no payment rate; Valdara's value added tax stays in ferra, its tax currency, with its tax rate.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Order/PaymentExchangeRate` | 0..1 | tender/26-Order | a trade outside the Accord at a floating rate (O51, where O96 places `ForeignExchangeContract`): a document in the contract's currency whose payment is asked in another currency at the day's rate, which the parities of the Accord never make necessary | O51 | candidate |
| `Reminder/PaymentCurrencyCode` | 0..1 | tender/35-Reminder | a trade outside the Accord at a floating rate (O51, where O96 places `ForeignExchangeContract`): a document in the contract's currency whose payment is asked in another currency at the day's rate, which the parities of the Accord never make necessary | O51 | candidate |
| `Reminder/PaymentExchangeRate` | 0..1 | tender/35-Reminder | a trade outside the Accord at a floating rate (O51, where O96 places `ForeignExchangeContract`): a document in the contract's currency whose payment is asked in another currency at the day's rate, which the parities of the Accord never make necessary | O51 | candidate |

### Stage 5, C74, C75, C76: numbering and collaborations (2026-11-20)

Coverage 4623 → 4613, 10 elements; all 10 won back the same day (4613 → 4623), when every document got the collaboration it is exchanged in (O260): see "Won back".

> D26, O77: `ProfileExecutionID` identifies one collaboration (one run of a process between the same parties, whose documents refer to each other), given by the party that starts it; a document that belongs to no collaboration with others carries none. The collaborations of each flow are listed in `world/documents.json` (`flows[].collaborations`); the build checks them (`check_numbering()` in `tools/build_examples.py`). Every customs declaration, goods certificate, ship's manifest and port report of the examples stands alone (the authority's answer is not an example), as do the shop's till receipts and the sea flow's business card, digital agreement and capability statement, which refer to no other document: their `ProfileExecutionID` goes.

### O262: the tax currency and rate only on documents that charge VAT (2026-11-20, owner)

> The tender flow's call-off order (tender/26) charges no tax (category G) but stated the manufacturer's tax currency and the lume-to-ferra tax exchange rate; the owner decided that these belong only on documents on which VAT is actually charged (invoices, credit notes, self-billed invoices and credit notes, debit notes, a receipt that charges the tax), not on quotations and orders.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Order/TaxCurrencyCode` | 0..1 | tender/26-Order | none under O262: an order charges no tax | — | open |
| `Order/TaxExchangeRate` | 0..1 | tender/26-Order | none under O262: an order charges no tax | — | open |

### O262/Q5: zero tax is not charged (2026-11-21, owner)

> Stage 7, Q5 (owner, 2026-11-21, option A): a document whose tax is 0 (the 0 % export of tender/32 and 33, the service outside the scope of tender/39) charges no tax, so it carries no tax currency, no tax exchange rate and no second tax total in ferra; `check_tax_currency()` in `tools/build_examples.py` allows them only on a bill or purchase receipt with a tax amount above 0. The invoices keep `Invoice/TaxCurrencyCode` and `Invoice/TaxExchangeRate` through wood/08.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `CreditNote/TaxCurrencyCode` | 0..1 | tender/33-CreditNote | O262/Q5: zero tax is not charged; a credit note of a taxed sale whose seller accounts for its tax in another currency, as the sawmill's taxed slat sale (wood/08) would be credited | O262 | open |
| `CreditNote/TaxExchangeRate` | 0..1 | tender/33-CreditNote | O262/Q5: zero tax is not charged; a credit note of a taxed sale whose seller accounts for its tax in another currency, as the sawmill's taxed slat sale (wood/08) would be credited | O262 | open |

### Read-throughs of 2026-11-20: the air frames in common transit (D39, owner)

> The air frames cross Bayvarra in the Accord's common transit (D39 point 2): they are neither imported into Bayvarra nor exported from it, and goods in transit are not recorded in trade statistics (owner, 2026-11-20). The forwarding instructions air/03 no longer give an export statistics value. `Shipment/DeclaredStatisticsValueAmount` stays covered by modification/05.

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Consignment/DeclaredStatisticsValueAmount` | 0..1 | air/03-ForwardingInstructions | a consignment that is exported or imported for good, whose forwarding instructions or declaration give the value trade statistics record (a real export, not goods in transit) | missing-elements work | candidate |

## Left out on purpose

Never covered; added only through a real business situation in the world (`CLAUDE.md`, open work 4).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ContractExtension/MinimumNumberNumeric` | 0..1 | never covered |  |  | left out |
| `Manifest/DeclaredCarriageValueAmount` | 0..1 | never covered |  |  | left out |
| `RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` | 0..1 | never covered |  |  | left out |
| `ShipmentStage/TransshipPortLocation` | 0..1 | never covered |  |  | left out |
| `SubcontractTerms/MinimumPercent` | 0..1 | never covered |  |  | left out |

## Won back

Elements that were in this register and are covered again, with the example that covers them.

| Element | Covered by | Case | Date |
|---|---|---|---|
| `GoodsItem/GoodsItemContainer` | rail/08-Waybill | the rail delivery's consignment note splits the 192 benches into two goods items, one production lot in each container (VI-LOT-260409 in FRXU1044175, VI-LOT-260410 in FRXU1044180): how the goods items are split across the transport equipment (O271, D37, O128) | 2026-11-20 |
| `GoodsItemContainer/ID` | rail/08-Waybill | the goods item's one container entry (O271) | 2026-11-20 |
| `GoodsItemContainer/TransportEquipment` | rail/08-Waybill | the container each lot was packed in (O271) | 2026-11-20 |
| `HazardousItem/UpperOrangeHazardPlacardID` | lpg/03-Waybill | the propane road tanker's orange plates, 23 over 1965: the upper half, the hazard identification number 23 (gas, flammable), on the tank's loaded hazardous item in the haulier's consignment note (D48, O126) | 2026-11-20 |
| `HazardousItem/LowerOrangeHazardPlacardID` | lpg/03-Waybill | the lower half of the tanker's orange plates, the UN number 1965 (D48, O126) | 2026-11-20 |
| `HazardousItem/TunnelRestrictionCode` | lpg/03-Waybill | the propane's tunnel restriction code B/D (ADR 2025), a carriage by road alone, which the consignment note must give for the tank (D48) | 2026-11-20 |
| `HazardousGoodsTransit/TransportEmergencyCardCode` | lpg/03-Waybill | the Trade Accord's emergency card for class 2 (TEC2), the instructions in writing the tanker's crew carries, on the road transit of the loaded propane; HazardousItem/EmergencyProceduresCode stays open (owner, 2026-11-20) | 2026-11-20 |
| `EmissionCalculationMethod/FullnessIndicationCode` | lpg/03-Waybill | the tanker's CO2e for the water company's greenhouse-gas report: the loaded run Gullhaven to Lumeport, UN/EDIFACT 8169 code 5 full, and the empty run back, code 4 empty (owner, 2026-11-20; list UNCL8169) | 2026-11-20 |
| `EnvironmentalEmission/ValueFactorNumeric` | lpg/03-Waybill | each run's CO2e is its diesel times the tank-to-wheel factor 0.268 kg CO2e per kWh (D41's factor): the factor | 2026-11-20 |
| `EnvironmentalEmission/ValueBaseMeasure` | lpg/03-Waybill | and the base: the kWh of diesel each run used, from the haulier's fuel records (1,700 kWh loaded, 1,240 kWh empty) | 2026-11-20 |
| `Attachment/EmbeddedDocument` | medicines/12-TransportationStatus | the active container's logger readings, a comma-separated text of 25 readings from its closing at the wholesaler to its opening at Selanu's cargo terminal, attached to the arrival status so the hospital pharmacy keeps them with its stock records (D47) | 2026-11-20 |
| `Attachment/FileName` | medicines/12-TransportationStatus | the name of the logger's file attached to the arrival status (D47) | 2026-11-20 |
| `Condition/MaximumMeasure` | medicines/12-TransportationStatus, reefer/10-TransportationStatus | the highest temperature the active container logged on the way to the island, inside 2 to 8 °C (D47); and the highest, while the reefer was off power between the quay and the ship (O137) | 2026-11-20 |
| `Condition/Measure` | medicines/10-TransportationStatus, medicines/12-TransportationStatus, reefer/10-TransportationStatus | the container's temperature read at acceptance at Lumeport's cargo terminal, and when it was opened at Selanu (D47); and the average supply-air temperature of the reefer over the voyage, from the carrier's reefer monitoring, in its status on discharge (O137) | 2026-11-20 |
| `Condition/MinimumMeasure` | medicines/12-TransportationStatus, reefer/10-TransportationStatus | the lowest temperature the active container logged on the way (D47); and the lowest supply-air reading of the voyage (O137) | 2026-11-20 |
| `GoodsItem/MaximumTemperature` | medicines/06-ForwardingInstructions, medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the highest temperature each cold-chain goods item may reach: 8 °C for the vaccine and the insulin, -15 °C for the frozen vaccine (D47, O124); and the warmest, 1 °C (O137) | 2026-11-20 |
| `GoodsItem/MinimumTemperature` | medicines/06-ForwardingInstructions, medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the lowest: 2 °C, and -50 °C for the frozen vaccine (D47, O124); and the coldest the fruit may be carried at, 0 °C (O137) | 2026-11-20 |
| `GoodsItem/Temperature` | medicines/06-ForwardingInstructions, medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading, reefer/11-ReceiptAdvice | the vaccine's and the insulin's carriage temperature, the set point of 5 °C (D47, O124); and the set point 0.5 °C the fruit is carried at, and the pulp temperature the wholesaler measures at unloading (O137) | 2026-11-20 |
| `Invoice/PaymentCurrencyCode` | medicines/02-Invoice | the Indian maker invoices in rupees and asks payment in euro, the currency the wholesaler pays its suppliers abroad in (O229; a trade outside the Accord, O51) | 2026-11-20 |
| `Invoice/PaymentExchangeRate` | medicines/02-Invoice | the ECB's euro reference rate of the invoice date, 110.938 rupees per euro, by which the rupee amount is paid in euro (O229, O51) | 2026-11-20 |
| `LotIdentification/ExpiryDate` | medicines/09-DespatchAdvice | the expiry dates of the makers' lots of the influenza and varicella vaccines and of the insulin, which the hospital pharmacy checks on receipt (D47) | 2026-11-20 |
| `RadioactiveMaterial/TransportIndexNumeric` | medicines/06-ForwardingInstructions, medicines/11-Waybill | the technetium generator's Type A package, transport index 1.5, Category III-YELLOW (D47, O202) | 2026-11-20 |
| `Status/IndicationIndicator` | medicines/12-TransportationStatus | whether the temperature stayed within 2 to 8 °C for the whole carriage, which the hospital needs to accept the goods (D47) | 2026-11-20 |
| `Temperature/MeasureCode` | medicines/06-ForwardingInstructions, medicines/11-Waybill | the set point of the cold-chain goods as the target of their range (TARGET, D47) | 2026-11-20 |
| `TransportEquipment/MaximumTemperature` | medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the airline's active RKN container's upper limit, 8 °C (D47, O124); and the highest, 1 °C: warmer, the fruit ripens on the way (O137) | 2026-11-20 |
| `TransportEquipment/MinimumTemperature` | medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading | its lower limit, 2 °C (D47, O124); and the lowest air temperature the reefer may reach, 0 °C: colder, the fruit begins to freeze (O137) | 2026-11-20 |
| `TransportEquipment/RefrigerationOnIndicator` | medicines/11-Waybill, reefer/03-ForwardingInstructions, reefer/07-BillOfLading, reefer/10-TransportationStatus | the active container switched on, holding its set point on its batteries (D47, O124); and the reefer's refrigeration running from pre-cooling to the cold store, and again on the port's power at Selanu (O137) | 2026-11-20 |
| `TransportHandlingUnit/MaximumTemperature` | medicines/06-ForwardingInstructions, medicines/11-Waybill | the cold-chain handling unit at 8 °C at most, the frozen vaccine's box at -15 °C (D47, O124) | 2026-11-20 |
| `TransportHandlingUnit/MinimumTemperature` | medicines/06-ForwardingInstructions, medicines/11-Waybill | at 2 °C at least, the frozen vaccine's box at -50 °C (D47, O124) | 2026-11-20 |
| `Order/OriginatorDocumentReference` | sea/05-Order | the Port of Selanu's request to the trader, which the order's port line follows (G8, O172) | 2026-11-19 |
| `RemittanceAdviceLine/DocumentReference` | tender/36-RemittanceAdvice | the department's deduction of the penalty for late completion under clause PEN-1 of the framework contract, which the remittance line cites as the document it is based on (D28 point 9, D9: the penalty is not a debit note) | 2026-11-19 |
| `QualificationResolution/ExclusionReason` | contest/18-TendererQualificationResponse | Fernhollow Studio, a small design studio of Lumeport, asks to take part in the design contest and is excluded at the selection for social security contributions of 3,860 lume due and unpaid, above the minor amounts; the department tells it why and how to appeal (O102, D29 point 6) | 2026-11-19 |
| `ShipmentStage/PassengerQuantity` | sea/16-CommonTransportationReport | the feeder's one passenger, a supercargo travelling with the cargo, in the ship's report before arrival at Selanu, which lists the crew and passengers instead of the cargo manifest (D37 point 7, O128, D30 point 8) | 2026-11-19 |
| `RemittanceAdviceLine/Note` | road/17-RemittanceAdvice | Lumeway pays Valdara's road invoice on Thursday 2 April, within the ten days of `XU-STD`, and takes the 2 % discount, 77,748 ferra on 3,887,400; the line states the short payment (O218) | 2026-11-19 |
| `TransportExecutionPlan/AtLocation` | ore/03-TransportExecutionPlan | the weighing of the ore wagons at Fucinalta mine siding, a service without movement that the plan confirms as requested (D45, ore/03#F3) | 2026-11-19 |
| `Address/Region` | rail/06-TransitCustomsDeclaration | the jurisdiction of the transit declaration: the Lumeport Trade Accord, a group of countries, because the Accord's common transit runs from Urvania's office of departure to Bayvarra's office of destination (D37 point 2, rail/06#F18; O140's candidate, a territory that covers the Accord area) | 2026-11-19 |
| `ImportCustomsDeclaration/PreviousCustomsDeclaration` | rail/14-ImportCustomsDeclaration | Lumeway's import at Marrowdale ends the Accord's common transit that Valdara lodged at Ferrano: the transit declaration, a declaration of the same procedure chain valid in Bayvarra, is its previous declaration (D37 point 2) | 2026-11-19 |
| `LineItem/BeneficiaryParty` | sea/05-Order, sea/06-OrderResponse | the port's line of the sea order, 96 benches for the harbour parks; the buyer's stock lines name no originator or beneficiary (O172) | 2026-11-19 |
| `LineItem/OriginatorParty` | sea/05-Order, sea/06-OrderResponse | the port's line of the sea order, 96 benches for the harbour parks; the buyer's stock lines name no originator or beneficiary (O172) | 2026-11-19 |
| `CircularityProfile/CircularityTypeCode` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
| `CircularityProfile/RecycledContentPercent` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
| `Item/EnvironmentalCertificate` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
| `TransportEquipment/ServiceAllowanceCharge` | reefer/07-BillOfLading | the carrier's charge for reefer power and monitoring at Selanu after discharge, a day, collect from the consignee (O137) | 2026-11-20 |
| `ImportCustomsDeclaration/ValidityPeriod` | reefer/09-ImportCustomsDeclaration | the wholesaler's import declaration lodged before the reefer arrives, so that the fruit is released on discharge; it lapses if the goods are not presented within 30 days (O137; also O150's candidate) | 2026-11-20 |
| `TransportEquipment/AirFlowPercent` | reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the reefer's fresh-air vent, open 15 %: apples and pears breathe, and fresh air carries off their carbon dioxide and ethylene (O137, O205) | 2026-11-20 |
| `TransportEquipment/HumanFoodApprovedIndicator` | reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the reefer approved for food, for unpacked fruit in open trays (O137) | 2026-11-20 |
| `TransportEquipment/HumidityPercent` | reefer/03-ForwardingInstructions, reefer/07-BillOfLading | the reefer set to hold about 90 % relative humidity, so that the fruit does not shrivel (O137) | 2026-11-20 |
| `TransportEquipment/StorageLocation` | reefer/10-TransportationStatus | the power point in the Port of Selanu's reefer rack where the reefer stands from discharge until it is collected (O137) | 2026-11-20 |
| `OrderResponse/ValidityPeriod` | reefer/02-OrderResponse | the cooperative's conditional acceptance of the wholesaler's order, three pallets of pears instead of four and a fifth of Granny Smith, open until Friday 17 April at noon, its cut-off for booking the reefer on the Thursday's ship (O236) | 2026-11-20 |
| `Shipment/InsuranceValueAmount` | reefer/03-ForwardingInstructions | the cooperative instructs its forwarder to insure the reefer's fruit for 110 % of its CIP value, the least cover Incoterms 2020 CIP asks of the seller (O239) | 2026-11-20 |
| `GoodsCertificate/FreightForwarderParty` | reefer/04-GoodsCertificate | Bayforth, the cooperative's forwarder, applies for the phytosanitary certificate on the cooperative's behalf and collects it with the export papers (O239) | 2026-11-20 |
| `Order/SalesOrderID` | modification/01-Order | the modification plant's job number of the kiln slot the sawmill's processing order fills, allotted by the plant with the season agreement's slots before any order (O150 row 1) | 2026-11-20 |
| `OrderChange/SalesOrderID` | modification/07-OrderChange | the plant's job number of the processing order the sawmill's call-off changes (O150 row 2) | 2026-11-20 |
| `LineItem/SubLineItem` | modification/01-Order | the 4,800 ash blanks the sawmill supplies free of charge, the material of the processing order's line of 96 bundles of modified slats (O150 row 3) | 2026-11-20 |
| `Despatch/ReleaseID` | modification/07-OrderChange, wood/06-DespatchAdvice | the sawmill's pick-up release for its finished job in the plant's store: the call-off issues it, the plant hands the bundles only to the driver who quotes it, and its despatch advice records it (O150 row 4) | 2026-11-20 |
| `Consignment/ConsignorAssignedID` | wood/06-DespatchAdvice | the plant's own loading number for the consignment it despatches for the sawmill, beside the sawmill's consignment number from the transport booking (O150 row 5; the study placed it in wood/04, moved to wood/06 because the plant gives its number when it loads) | 2026-11-20 |
| `InventoryReportLine/AvailabilityDate` | modification/06-InventoryReport | the plant's stock report to the sawmill: the second kiln charge's 48 bundles available from Wednesday 4 February, when planing and sealing are finished (O150 row 6) | 2026-11-20 |
| `Shipment/DeclaredCustomsValueAmount` | wood/07-ImportCustomsDeclaration | the release from inward processing covers the goods of two entries, one per load of blanks: two goods items of the same subheading, procedure and origin, whose customs values the shipment totals (O150 row 7) | 2026-11-20 |
| `Shipment/DeclaredStatisticsValueAmount` | modification/05-ImportCustomsDeclaration | the value trade statistics record the blanks at as they enter inward processing, what they would be invoiced at with the carriage to the border; the release is not recorded again (O150 row 8, O251 after the coordinator's source check of 2026-11-20: statistics on entry, not on release) | 2026-11-20 |
| `Item/LifecycleStageCode` | modification/08-Invoice | the plant's thermal modification service, the slat's manufacturing stage, which the sawmill needs for its slat's footprint (O150 row 10) | 2026-11-20 |
| `Item/LifecycleStageDescription` | modification/08-Invoice | the environmental impact of the plant's kiln in words: heat from a boiler fired with its offcuts, grid electricity, fumes burned, no chemicals; no figures until O252 (O150 row 11) | 2026-11-20 |
| `Consignment/OfficeOfEntryLocation` | modification/05-ImportCustomsDeclaration | the offices the plant's inward-processing authorisation names as empowered to accept its entries: the border post, with the inland office at Ferrano as a subsidiary location (O150 row 12) | 2026-11-20 |
| `Party/ServiceProviderParty` | wood/02-Quotation | the sawmill names the plant that modifies this delivery: Valdara's approval of the supplier of a type-tested part covers the special process (O150 row 13) | 2026-11-20 |
| `ServiceProviderParty/Party` | wood/02-Quotation | Tostara Wood Modification (O150 row 14) | 2026-11-20 |
| `ServiceProviderParty/ServiceTypeCode` | wood/02-Quotation | PROCESSING, contract processing, in the regional service type list (O150 row 15) | 2026-11-20 |
| `ServiceProviderParty/ServiceType` | wood/02-Quotation | the plant's work in words: modification, planing, end-grain sealing, storage and despatch (O150 row 16) | 2026-11-20 |
| `ServiceProviderParty/SellerContact` | wood/02-Quotation | the plant's despatch desk, which Valdara's goods-in deals with on the delivery day (O150 row 17) | 2026-11-20 |
| `OrderChange/DeliveryTerms` | modification/07-OrderChange | the call-off changes the processing order's ex works to free carrier at the plant's dock, loaded onto Trasvia's trailer, at the sawmill's risk from loading (O150 row 18) | 2026-11-20 |
| `BusinessCard/ProfileExecutionID` | sea/01-BusinessCard | Lumeway's onboarding of Velumi as a new island customer, a collaboration of the business card, the digital agreement and the capability statement, started by Lumeway (O260) | 2026-11-20 |
| `CommonTransportationReport/ProfileExecutionID` | cotton/14-CommonTransportationReport, sea/16-CommonTransportationReport | each port call's report is a collaboration of the carrier with the port or the maritime administration, started by the carrier, whose other step is the authority's clearance to enter (a cited document, O260) | 2026-11-20 |
| `DigitalAgreement/ProfileExecutionID` | sea/03-DigitalAgreement | the onboarding collaboration of sea/01 (O260) | 2026-11-20 |
| `DigitalCapability/ProfileExecutionID` | sea/04-DigitalCapability | the onboarding collaboration of sea/01; the agreement's governor answers in it (O260) | 2026-11-20 |
| `ExportCustomsDeclaration/ProfileExecutionID` | cotton/11, energy/04, modification/04, plastics/05, reefer/05, road/05, sea/11, tender/30 (ExportCustomsDeclaration) | each declaration is a collaboration of the declarant with customs, started by the declarant in its own numbering, whose other step is customs' release (a cited document); it does not carry the trade's identifier (O260) | 2026-11-20 |
| `GoodsCertificate/ProfileExecutionID` | cotton/10-GoodsCertificate, reefer/04-GoodsCertificate | the application for the certificate and its issue, started by the applicant (the ginnery; the cooperative, whose forwarder lodges the application); the application is a cited document (O260) | 2026-11-20 |
| `ImportCustomsDeclaration/ProfileExecutionID` | cotton/15, energy/05, energy/10, medicines/03, medicines/08, medicines/13, modification/05, plastics/09, rail/14, reefer/09, road/10, sea/19, tender/31, wood/07 (ImportCustomsDeclaration) | as for the export declarations: the declarant's collaboration with customs, to the release (O260) | 2026-11-20 |
| `Manifest/ProfileExecutionID` | sea/15-Manifest | the carrier's collaboration with the island's customs, to the customs' acceptance of the manifest (a cited document, O260) | 2026-11-20 |
| `PurchaseReceipt/ProfileExecutionID` | packaging/08, packaging/09, retail/21, sea/29 (PurchaseReceipt) | each sale at the till is a collaboration of its own, started by the shop: the receipt is the whole exchange, with the home delivery order booked with the sale in retail/21 (O260) | 2026-11-20 |
| `TransitCustomsDeclaration/ProfileExecutionID` | rail/06-TransitCustomsDeclaration | the holder's collaboration with the office of departure, to the release for transit (a cited document, O260) | 2026-11-20 |
