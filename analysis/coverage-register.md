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

### Stage 1 step 1a: party master data (C02, C03, C05, C07)

Coverage 5153 → 5151 (commit c15bf42c), 2 elements.

> O140: **`Address/Region` lost its only example (stage 1 step 1a, 2026-11-17):** it held the Urvanian province, which is a country subdivision and went to `CountrySubentity` (C03). UBL defines `Region` as "the recognized geographic or economic region or group of countries in which this address is located". A real case: a price or a territory that covers the Trade Accord area as a whole (for example `ApplicableTerritoryAddress` of a catalogue price valid in all three countries), to look for with C25 in step 1e; otherwise it stays uncovered

> O141: **`Address/AdditionalStreetName` lost its only example (stage 1 step 1a, 2026-11-17):** it held Lumeway's "Gate 3", which is a delivery location and went to the road order's `DeliveryLocation` (C05). A real case: an address whose street needs a second name to be found, such as a building that stands on a corner and is entered from the side street, or a farm track off a named road; to be found with the place list (O91) or the encyclopaedia; otherwise it stays uncovered

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Address/AdditionalStreetName` | 0..n | air/01-OrderChange, air/02-OrderResponse, air/03-ForwardingInstructions … | | | open |
| `Address/Region` | 0..1 | carnet/01-GoodsItemPassport, carnet/02-ProofOfReexportationRequest, carnet/03-ProofOfReexportationReminder … | | | open |

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
| `Delivery/ReleaseID` | 0..1 | tender/26-Order | | | open |
| `DeliveryNote/DocumentStatusCode` | 0..1 | cotton/03-DeliveryNote | | | open |
| `Despatch/ReleaseID` | 0..1 | road/04-DespatchAdvice | | | open |
| `DespatchAdvice/DocumentStatusCode` | 0..1 | air/06-DespatchAdvice, air/08-DespatchAdvice, mast/04-DespatchAdvice … | | | open |
| `DespatchLine/LineStatusCode` | 0..1 | air/06-DespatchAdvice, air/08-DespatchAdvice, mast/04-DespatchAdvice … | | | open |
| `ForwardingInstructions/DocumentStatusCode` | 0..1 | air/03-ForwardingInstructions, cotton/09-ForwardingInstructions, sea/09-ForwardingInstructions … | | | open |
| `FulfilmentCancellation/Contract` | 0..n | air/07-FulfilmentCancellation | | | open |
| `InvoiceLine/BillingReference` | 0..n | furniture/17-Invoice | | | open |
| `LineReference/LineStatusCode` | 0..1 | cotton/04-SelfBilledInvoice, road/02-OrderResponse | | | open |
| `Order/SalesOrderID` | 0..1 | tender/26-Order | | | open |
| `OrderChange/SalesOrderID` | 0..1 | air/01-OrderChange | | | open |
| `OrderReference/CustomerReference` | 0..1 | air/07-FulfilmentCancellation | | | open |
| `OrderResponse/Contract` | 0..n | sea/06-OrderResponse | | | open |
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
| `TransportExecutionPlan/AtLocation` | 0..1 | ore/03-TransportExecutionPlan, plastics/04-TransportExecutionPlan, rail/03-TransportExecutionPlan | | | open |
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
| `RemittanceAdviceLine/DocumentReference` | 0..n | cotton/18-RemittanceAdvice, ore/08-RemittanceAdvice, plastics/11-RemittanceAdvice … | | | open |

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
| `Consignment/OfficeOfEntryLocation` | 0..1 | rail/06-TransitCustomsDeclaration | | | open |
| `ImportCustomsDeclaration/CustomsExitOfficeLocation` | 0..1 | cotton/15-ImportCustomsDeclaration, plastics/09-ImportCustomsDeclaration, road/10-ImportCustomsDeclaration … | | | open |
| `ImportCustomsDeclaration/PreviousCustomsDeclaration` | 0..1 | cotton/15-ImportCustomsDeclaration, plastics/09-ImportCustomsDeclaration, road/10-ImportCustomsDeclaration … | | | open |
| `ImportCustomsDeclaration/ValidityPeriod` | 0..1 | cotton/15-ImportCustomsDeclaration, plastics/09-ImportCustomsDeclaration, road/10-ImportCustomsDeclaration … | | | open |
| `Shipment/DeclaredCustomsValueAmount` | 0..1 | sea/11-ExportCustomsDeclaration | | | open |
| `Shipment/DeclaredStatisticsValueAmount` | 0..1 | sea/11-ExportCustomsDeclaration | | | open |
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
| `FulfilmentCancellation/BeneficiaryParty` | 0..n | air/07-FulfilmentCancellation | | | open |
| `FulfilmentCancellation/OriginatorCustomerParty` | 0..1 | air/07-FulfilmentCancellation | | | open |
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
| `Temperature/MeasureCode` | 0..1 | mast/02-ForwardingInstructions, plastics/09-ImportCustomsDeclaration | | | open |
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
| `RemittanceAdviceLine/Note` | 0..n | utilities/04-RemittanceAdvice | Lumeway pays Valdara's road invoice within the ten days of `XU-STD` and takes the 2 % discount, 77,748 ferra on 3,887,400, explained on the line (road/17; the payment moves from 22 April to 3 April at the latest; proposed by G5, O181, not yet in the decided story) | road | candidate |

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
| `Item/LifecycleStageCode` | 0..1 | waste/03-Invoice | | | open |
| `Item/LifecycleStageDescription` | 0..n | waste/03-Invoice | | | open |

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
| `LineItem/SubLineItem` | 0..n | furniture/08-Order, furniture/10-Order | | | open |

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
| `EmissionCalculationMethod/FullnessIndicationCode` | 0..1 | retail/02-Catalogue, retail/04-CatalogueItemSpecificationUpdate, sea/02-Catalogue … | | | open |
| `EnvironmentalEmission/ValueBaseMeasure` | 0..1 | retail/02-Catalogue, retail/04-CatalogueItemSpecificationUpdate, sea/02-Catalogue … | | | open |
| `EnvironmentalEmission/ValueFactorNumeric` | 0..1 | retail/02-Catalogue, retail/04-CatalogueItemSpecificationUpdate, sea/02-Catalogue … | | | open |

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
| `GoodsCertificate/FreightForwarderParty` | 0..1 | cotton/10-GoodsCertificate | | | open |
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
| `ItemInstance/BestBeforeDate` | 0..1 | plastics/08-DespatchAdvice | fresh food with a best-before date, such as the reefer's apples (O137, still to design) | reefer | open |
| `LotIdentification/ExpiryDate` | 0..1 | plastics/08-DespatchAdvice | a lot of vaccines or medicines with its expiry date in the medicines flow's despatch advice (D47) | medicines | candidate |

> C89, D43: the sawmill sells the bundle of 50 slats as its item, so quotation, order and invoice are in bundles and no price converts a piece price into a pack (02#F13, 03#F10, 08#F14); the quotation's main line is oak with ash as the priced alternative, and the 35 mm substitute goes (02#F16).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Price/OrderableUnitFactorRate` | 0..1 | wood/02-Quotation, wood/03-Order, wood/08-Invoice | | | open |
| `QuotationLine/SellerProposedSubstituteLineItem` | 0..1 | wood/02-Quotation | | | open |

### G5: road (2026-11-19)

Stage 6, building group G5 (C100, C101, C102; D35).

> C100, D35 point 4: the order states no maximum delivery unit, which no delivery of the flow uses (01#F11); the carrier's status no longer reports a temperature the goods do not need (09#F11), nor an indicator that said nothing (09#F10); the application response no longer names the issuer and recipient of the invoice it answers (16#F11).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `Condition/MaximumMeasure` | 0..1 | road/09-TransportationStatus | the highest temperature the temperature-controlled unit of the medicines flow logged during the flight, in the carrier's status on arrival (2–8 °C, D47) | medicines | candidate |
| `Condition/Measure` | 0..1 | road/09-TransportationStatus | the temperature in the medicines' temperature-controlled unit at arrival (D47) | medicines | candidate |
| `Condition/MinimumMeasure` | 0..1 | road/09-TransportationStatus | the lowest temperature the unit logged during the flight (D47) | medicines | candidate |
| `Delivery/MaximumDeliveryUnit` | 0..1 | road/01-Order | | | open |
| `DocumentResponse/IssuerParty` | 0..1 | road/16-ApplicationResponse | | | open |
| `DocumentResponse/RecipientParty` | 0..1 | road/16-ApplicationResponse | | | open |
| `Status/IndicationIndicator` | 0..1 | road/09-TransportationStatus | in the same status of the medicines flow, whether the temperature stayed within 2–8 °C for the whole carriage, stated as what the indicator means (D47) | medicines | candidate |

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

## Left out on purpose

Never covered; added only through a real business situation in the world (`CLAUDE.md`, open work 4).

| Element | Card. | Lost from | Candidate case | Place | Status |
|---|---|---|---|---|---|
| `ContractExtension/MinimumNumberNumeric` | 0..1 | never covered |  |  | left out |
| `Manifest/DeclaredCarriageValueAmount` | 0..1 | never covered |  |  | left out |
| `QualificationResolution/ExclusionReason` | 0..n | never covered | an excluded contest candidate (O102) | contest | agreed |
| `RadioactiveMaterial/FissileCriticalitySafetyIndexNumeric` | 0..1 | never covered |  |  | left out |
| `RadioactiveMaterial/TransportIndexNumeric` | 0..1 | never covered | the technetium generator of the medicines flow (D47) | medicines | agreed |
| `ShipmentStage/TransshipPortLocation` | 0..1 | never covered |  |  | left out |
| `SubcontractTerms/MinimumPercent` | 0..1 | never covered |  |  | left out |

## Won back

Elements that were in this register and are covered again, with the example that covers them.

| Element | Covered by | Case | Date |
|---|---|---|---|
| `LineItem/BeneficiaryParty` | sea/05-Order, sea/06-OrderResponse | the port's line of the sea order, 96 benches for the harbour parks; the buyer's stock lines name no originator or beneficiary (O172) | 2026-11-19 |
| `LineItem/OriginatorParty` | sea/05-Order, sea/06-OrderResponse | the port's line of the sea order, 96 benches for the harbour parks; the buyer's stock lines name no originator or beneficiary (O172) | 2026-11-19 |
| `CircularityProfile/CircularityTypeCode` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
| `CircularityProfile/RecycledContentPercent` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
| `Item/EnvironmentalCertificate` | plastics/12-Catalogue | Rinova's product information for its granulate to Rivermouth: the recycled-content certificate of the accredited certification body Certovira Certification, and the recycled content of 100 % (D41, O193) | 2026-11-19 |
