# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/28#F1 · High · Creditor and debtor reversed: Velumi claims, but Lumeway is the accounting supplier and Velumi the accounting customer and payee
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `LD-AP-CLAIMS`
- XPath: `/DebitNote/cbc:AccountingCost` = `Stock for municipal projects`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCost` = `Stock for municipal projects`
- Why: A debit note is "A document used to specify debits due to the Creditor from the Debtor". Velumi issues and signs it (`VT-DOC-26-0153`), is named seller and payee and gives its own account; Lumeway is named buyer and routes the note to its accounts payable claims unit. Velumi is thus the creditor, Lumeway the debtor. Yet the accounting supplier (the creditor's accounting role) is Lumeway and the accounting customer (the debtor's) Velumi, which makes the accounting customer also the payee of its own debt. The buyer's accounting code (`AccountingCost`, the buyer's code) is Velumi's own cost centre from its order (`05-Order.xml:/Order/cbc:AccountingCost` = `Stock for municipal projects`), although the buyer named here is Lumeway. The same pattern (accounting roles of the original sale kept, seller/buyer/payee reversed) occurs in `furniture/14-DebitNote.xml`; UBL defines no convention for a buyer-issued debit note, so the choice should be settled once for both.
- Condition: Accounting supplier, seller, payee (if kept) and signatory are the same creditor, and accounting customer and buyer the same debtor (Velumi creditor, Lumeway debtor); the buyer's accounting code, if any, is the debtor's.
- Options: (a) preferred: Velumi as accounting supplier, Lumeway as accounting customer, the payee dropped (it would equal the supplier), no accounting cost or one of Lumeway's; (b) keep the original sale's accounting roles and make seller, buyer and payee follow them, which conflicts with UBL's creditor/debtor definition (Velumi would debit itself).
- Needs decision: yes
- From: broad (F1), context (F1), money (F4), parties (F1)

### sea/28#F2 · High · The storage charge appears three times and line 1 does not add up
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:TaxInclusiveLineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:Price/cbc:PriceAmount` = `38.5`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:AllowanceCharge/cbc:Amount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:ItemPriceExtension/cbc:Amount` = `51.250`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[1]/cbc:LineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount` = `51.25`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `51.250`
- Why: The one-day storage at Selanu (12.750 XLC) is stated as a charge "Storage while held" on line 1, as sub-line 1.2 of line 1, and as the separate collection line 2 "collected for the port"; line 1's alternative condition price 51.25 includes it a fourth time. Recomputed: line 1's `LineExtensionAmount` ("including allowance charges but net of taxes") should be 38.500 × 1 + 12.750 = 51.250 with its own charge, not 38.500; its `ItemPriceExtension` ("price per unit × quantity") should be 38.5 × 1 = 38.500, not 51.250; its sub-lines add up to 38.500 + 12.750 = 51.250, not to the parent's 38.500. The document total 51.250 = 38.500 (line 1) + 12.750 (line 2) counts storage once only by ignoring line 1's own charge and sub-line; with line 1 complete and line 2 added it would be 64.000. Whether storage belongs to line 1 or line 2 cannot be read from the document.
- Condition: Storage appears once; each line's extension equals price × quantity plus its own charges; the price extension equals price × quantity; sub-lines add up to their parent line; the line extension total is the sum of the line extensions.
- Options: (a) preferred: line 1 = customs inspection only (38.500; no charge, no storage sub-line, price extension 38.500, no alternative price or one without storage), line 2 = storage 12.750 collected for the port; total 51.250; (b) storage inside line 1 (as charge or sub-line, not both; line extension 51.250, price extension 38.500) and no collection line.
- Needs decision: no
- From: broad (F2), context (F3), money (F1); parties (F3, part). The alternative condition price was added by the merge as a further place.

### sea/28#F3 · High · Reference to a statement issued three weeks after this debit note
- XPath: `/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-05-22`
- XPath: `25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`
- Why: `StatementDocumentReference` is "A reference to a Statement associated with this document". The statement `HF-ST-26-0151` is issued by Harbourline Factoring on 2026-06-13, 22 days after this debit note, so the reference points to a document that does not exist when the debit note is issued. The statement is also the factor's statement of Lumeway's receivable on Velumi; its two lines are the invoice and the deposit, and it does not contain this claim of Velumi on Lumeway.
- Condition: Every document the debit note refers to exists on its issue date and concerns the debited amount.
- Options: (a) preferred: drop the statement reference; (b) issue the debit note after 2026-06-13 if it is meant to answer a statement, which changes the order of the flow.
- Needs decision: no
- From: broad (F3), context (F2), logistics (F1), money (F3)

### sea/28#F4 · High · Payable alternative amount in XBL although the alternative currency is XLC
- XPath: `/DebitNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAlternativeAmount` = `128.13`
- XPath: `/DebitNote/cbc:PaymentCurrencyCode` = `XBL`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: `PayableAlternativeAmount` is "The amount of the monetary total to be paid, expressed in an alternative currency". The document names XLC as the payment alternative currency (with an XLC→XLC rate of 1, which would give 51.250 XLC), while the amount is 128.13 in XBL: 51.250 × 2.5 = 128.125, i.e. the payable amount converted into the payment currency at `PaymentExchangeRate`. Two values of the document contradict each other on what the alternative currency is. In addition, payment is requested in XBL into Velumi's XLC account, while the document currency is XLC: the Bayvarran debtor may pay in its own currency, but the document does not say so.
- Condition: The payable alternative amount is in the payment alternative currency the document names, at its stated rate; payment currency, alternative currency and the payee account's currency are consistent, or the conversion is explained.
- Options: (a) preferred: payment in XLC (document and account currency), XBL as the alternative currency for the Bayvarran debtor at 2.5 with the alternative amount 128.13 XBL, the XLC→XLC rates dropped (F10); (b) keep payment in XBL, drop the alternative currency, its rate and amount, and give an XBL account or explain the conversion.
- Needs decision: no
- From: money (F2); broad (F4, part) and context (F4, part)

### sea/28#F5 · Medium · The inspection fee "collected for" customs although Velumi recovers its own outlay; storage attributed to two parties
- XPath: `/DebitNote/cac:DebitNoteLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DocumentReference/cbc:ID` = `XL-CUS-RCPT-26-0517`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cac:Item/cbc:Name` = `Storage at the port`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:Note` = `The port's storage charge for the day the container was held, collected for the port.`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: `CollectedForParty` is "The Party on whose behalf this item or amount is collected". Line 1 refers to a customs receipt, so the fee has been paid to customs already; Velumi recovers its own outlay (line 1's beneficiary is Velumi itself) and collects nothing on the customs service's behalf. Line 1 also carries the port storage (sub-line 1.2 and its charge), which line 2 says is "collected for the port"; so the storage is attributed to customs in line 1 and to the port in line 2. On line 2, the collection line, the port is given as `BeneficiaryParty` rather than in the dedicated `CollectedForParty`.
- Condition: Each amount is attributed to one party: the recovered inspection fee without `CollectedForParty` (or with Velumi only as beneficiary); the storage either a third-party collection for the port on line 2 with the port as `CollectedForParty`, or part of line 1, not both.
- Options: (a) preferred: line 1 the inspection fee without `CollectedForParty`, the receipt kept as evidence of the outlay; line 2 the storage with the port as `CollectedForParty`; (b) if Velumi has not yet paid customs, drop the receipt reference instead.
- Needs decision: no
- From: money (F5), parties (F3)

### sea/28#F6 · Medium · The customs service as originator of the order
- XPath: `/DebitNote/cac:DebitNoteLine/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `05-Order.xml:/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The line's `OriginatorParty` is "The Party who originated the Order to which the Debit Note is related". The order `VT-PO-26-0127` was originated by the Port of Selanu. The customs service inspected the container and charged a fee; it did not originate any order. The element is used for the party that caused the cost.
- Condition: The line's originator is the party that originated the order, or the element is absent.
- Options: (a) preferred: drop it; customs is identified by the work report reference (and, if kept, `CollectedForParty`, see F5); (b) the Port of Selanu as in the order.
- Needs decision: no
- From: broad (F6, part), context (F6), parties (F2)

### sea/28#F7 · Medium · The bill of lading referenced as a delivery note
- XPath: `/DebitNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: `DeliveryNoteDocumentReference` is "A reference to a Delivery Note associated with this document". `TOL-BL-26-0139` is the ocean carrier's bill of lading (`14-BillOfLading.xml`), a transport document and document of title; UBL has separate BillOfLading and delivery-note documents. No delivery note exists in the flow; the final delivery is documented by the despatch advice and the receipt advice, which the debit note already references.
- Condition: `DeliveryNoteDocumentReference` refers only to a delivery note; the bill of lading, if needed, is referenced in an element meant for any document, with its type.
- Options: (a) preferred: move it to `AdditionalDocumentReference` with `DocumentTypeCode` `BillOfLading`; (b) drop it.
- Needs decision: no
- From: broad (F6, part), context (F5), logistics (F2)

### sea/28#F8 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in Lumeway's postal address in a debit note. 79 occurrences in 76 files (`grep -rho --include='*.xml'` over `world/examples`), always Lumeway's address.
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it; (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F5), parties (F4)

### sea/28#F9 · Medium · A language code in LocaleCode
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F5)

### sea/28#F10 · Low · Identity exchange rates, tax and pricing currency equal to the document currency, and a tax point without tax
- XPath: `/DebitNote/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/DebitNote/cbc:PricingCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/DebitNote/cac:PricingExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/DebitNote/cbc:TaxPointDate` = `2026-05-20`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:TaxPointDate` = `2026-05-20`
- Why: The document, its prices and its (zero) tax are all in XLC; the tax, pricing and payment-alternative exchange rates convert XLC into XLC at 1 (each definition is a rate "between the document currency and" another currency), and the tax and pricing currency codes repeat the document currency. Lisavu has no general sales tax (category O, scheme "No general sales tax"), so a tax point date names the date of a tax that does not exist; 2026-05-20 also matches neither the inspection (2026-05-18/19) nor the issue (2026-05-22). None of these values says anything their absence would not (no fillers, IND5/IND6). The rate the payment needs (XLC→XBL 2.5) is not part of this finding.
- Condition: Currency codes and exchange rates appear only where a second currency is involved; a tax point date only where a tax applies.
- Options: (a) preferred: drop them, keeping only the XLC↔XBL rate the payment needs (see F4).
- Needs decision: no
- From: money (F6); broad (F4 part, F7 part), context (F4, part)

### sea/28#F11 · Low · The debit note called "Invoice" in the payment note
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice VT-DOC-26-0153`
- Why: The payment note names the document the payment settles; `VT-DOC-26-0153` is this debit note, not an invoice.
- Condition: The payment note names the document correctly.
- Options: (a) preferred: "Debit note VT-DOC-26-0153".
- Needs decision: no
- From: broad (F7, part), context (F7, part)

### sea/28#F12 · Low · Further values without a reason in this debit note
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DeliveryTerms/cbc:ID` = `CIF`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:FreeOfChargeIndicator` = `false`
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/DebitNote/cac:ProjectReference/cbc:ID` = `VT-PRJ-26-07`
- Why: Delivery terms CIF on a line for a customs inspection fee repeat the goods' term for a service they do not govern. `FreeOfChargeIndicator` false states the default and says nothing. The contract referenced is the Digital Agreement on electronic exchange (`03-DigitalAgreement.xml`), though the note's "the packer's responsibility under the agreement" points to the sale's terms (`LD-GTC-2026`). The project `VT-PRJ-26-07` occurs only here and in `26-CreditNote.xml` (2 files, `grep -rl --include='*.xml'`), not in the order or invoice.
- Condition: Each value is removed or replaced by one that fits this debit note (the sale's terms as the contract; a project only if the order carries it).
- Options: (a) preferred: drop the line delivery terms, the free-of-charge indicator and the project; reference the sale's terms as the contract.
- Needs decision: no
- From: context (F7), broad (F7, part)

### sea/28#F13 · Low · Contacts that do not fit a claim between the two companies
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway routes the note to its accounts payable claims unit (`LD-AP-CLAIMS`), but its contact is its sales customer service. Velumi, which raises the claim, gives a contact named Purchasing who is a customer service officer in Sales: name, title and department disagree, and none is the claims function that raised `VT-CLAIM-26-0021`.
- Condition: Each contact's name, job title and department agree and are the functions handling the claim on each side.
- Options: (a) preferred: claims or accounts contacts on both sides; (b) drop the contacts.
- Needs decision: no
- From: broad (F8), parties (F6)

### sea/28#F14 · Low · Lumeway's tax registration, share capital and customs number in a recharge outside the scope of tax
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: The debit note is outside the scope of tax under "No general sales tax"; Lumeway's Bayvarran sales-tax registration, its share capital and its customs trader number play no part in Velumi's recharge. They are copied from Lumeway's master data (section 4.8); Velumi, the issuer, carries no tax scheme.
- Condition: Lumeway carries only the party data the debit note uses.
- Options: (a) preferred: drop `PartyTaxScheme`, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifier; (b) keep them with a stated reason.
- Needs decision: no
- From: parties (F7)

### sea/28#F15 · Low · Tax category O with a percent of 0
- XPath: `/DebitNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- Why: Category O ("Services outside scope of tax") means no tax applies, so there is no rate; a percent of 0 states a rate for a tax that is not applicable (IND6: nothing implied, nothing filled). The category itself fits here (inspection and storage are services in Lisavu, which has no general sales tax).
- Condition: The tax category O carries no percent.
- Options: (a) preferred: drop `Percent`.
- Needs decision: no
- From: added by the merge (no part raised it), aligned with the earlier flows' merges (cotton, utilities, road)

## Checked and consistent
- Payment: due date 2026-06-21 = issue 2026-05-22 + 30 days, as "30 days net" says, and as the payment means' due date; payment rate 2.5 = 1 / 0.4 (the flow's XBL→XLC rate); 51.250 × 2.5 = 128.125 → 128.13 (recomputed).
- Payee account `XL40BSEL0010003665515` is in Velumi's name at the Bank of Selanu, the account Velumi pays from in `27-RemittanceAdvice.xml`; account, RF `RF75VTDOC260153`, GLN and container `TWLU4120872` pass `check_ids.py` (re-run).
- References that resolve: order `VT-PO-26-0127`, despatch advice `LD-DA-26-0145` (line 1), receipt advice `NW-RA-26-0146` (2026-05-21, line 1), bill of lading `TOL-BL-26-0139`, invoice `LD-INV-26-0147`, digital agreement `LD-DAG-26-0125`; all except the statement (F3) precede the debit note.
- The pallet `095206101230000070` in the discrepancy description is pallet 7 of 25 in the container, a pallet of four benches (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[7]/cbc:ID` = `095206101230000070`), so line 1 correctly points to order, despatch and receipt line 1 (benches); its GS1 check digit is valid.
- The hold for the heat-treatment mark agrees with the detention and quarantine events of 2026-05-18 in `17-TransportationStatus.xml`; one day of storage fits a hold until the import declaration of 2026-05-19 (`19-ImportCustomsDeclaration.xml`).
- Tax category O with 0.000 tax fits services in Lisavu; Velumi's address and legal form carry `en-XL` and Lisavan renderings; the Port of Selanu as beneficiary of the storage is the port where the container was held.

## Considered and refuted
- `/DebitNote/cac:PurchaseReference/cbc:ID` = `TWLU4120872`: a container number as purchase reference — refuted because the element is "a reference to an object, such as … a vehicle … to which this Debit Note relates", and the charges concern that container (from broad, context, logistics).
- `/DebitNote/cac:Annotation/cbc:AnnotationContent` = `The distributor may claim it from the packer.`: a contradiction with Lumeway packing the goods — refuted because the note puts the responsibility on "the packer", a party other than the distributor, which the annotation keeps consistent (from broad); the packer is not a party to this debit note (from parties, on `/DebitNote/cbc:Note[2]`).
- `/DebitNote/cac:DiscrepancyResponse/cbc:ResponseCode` = `2`: "Below specification goods" for an illegible mark — refuted because an illegible ISPM 15 mark makes the packaging fail a specification the goods had to meet (from broad, context).
- `/DebitNote/cac:DebitNoteLine/cac:ReceiptLineReference/cbc:LineID` = `1`: the receipt line ("Received as despatched.") does not support the claim — refuted because the defect was found at the port before goods-in, and the receipt line is cited for the goods concerned (from money).
- `/DebitNote/cac:InvoicePeriod/cbc:EndDate` = `2026-05-19`: two days of storage against one debited day, or the hold ending on 2026-05-18 — refuted because the container stayed under customs control until the import declaration on 2026-05-19, and a period 18–19 May can be the 24-hour hold (from money, logistics).
- The debit note is not settled by any later document of the flow — refuted because a claim between the parties may be settled outside the documents shown, and the remittance advice correctly does not net it against the factored invoice (from money).
- `/DebitNote/cac:WorkReportDocumentReference/cbc:ID` = `XL-CUS-INSP-26-0517`: an inspection record as a "work report", or "0517" read as 17 May, before the inspection — refuted because it reports the work whose cost is passed on, and the ID is an opaque number of the customs service (from context, logistics).
- `/DebitNote/cac:DebitNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading`: Velumi as beneficiary of its own line — refuted because it is the party that benefits from the recovered fee (from parties).

## Changed in the merge
- broad/F1, context/F1, parties/F1 (no) and money/F4 (yes) → F1: Needs decision yes, aligned with the furniture merge for `furniture/14-DebitNote.xml`, which has the same pattern: UBL defines no convention for buyer-issued debit notes, so the choice is settled once for both flows. The accounting cost lines (money, context, parties) are folded in; broad's F7 part on the accounting cost moved here.
- broad/F4 and context/F4 (Medium, grouped) → F4 (High) and F10 (Low): the alternative amount in a currency other than the declared alternative currency is a contradiction between two values of the document (High, as money/F2); the identity rates and repeated currency codes are fillers, rated Low as in money/F6 and in the earlier flows' merges (cotton: identity exchange rates Low).
- broad/F6 → F6 and F7: split into the originator and the delivery-note reference, as the other parts had them.
- broad/F7 → F1, F10, F11, F12: split by problem (accounting cost to F1, tax point to F10, payment note to F11, line delivery terms to F12); context/F7's payment note also moved to F11, as furniture's merge kept "Invoice" in a debit note's payment note as its own finding.
- F2: the alternative condition price 51.25 added as a further place by the merge.
- F15: added by the merge (no part raised it).
