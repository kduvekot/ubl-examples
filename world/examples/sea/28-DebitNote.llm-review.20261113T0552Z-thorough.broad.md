# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit c9983d2 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/28#F1 · High · Creditor and debtor roles contradict each other
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: A debit note specifies "debits due to the Creditor from the Debtor". Velumi issues and signs it, is the payee and the seller of the recharged services, and Lumeway is the buyer who must pay (its buyer reference `LD-AP-CLAIMS` routes it). Yet the accounting supplier (the creditor's accounting role) is Lumeway and the accounting customer (the debtor's) is Velumi, so the accounting customer is also the payee: Velumi would pay itself. The two pairs of roles in the same document point in opposite directions.
- Condition: Accounting supplier, seller and payee are the creditor (Velumi); accounting customer and buyer are the debtor (Lumeway); or, if the world keeps the original invoice's roles, seller/buyer/payee follow the same direction and the document says who pays whom.
- Options: (a) preferred: Velumi as accounting supplier, Lumeway as accounting customer (consistent with seller, buyer, payee and signature); (b) keep the original invoice's accounting roles and change seller, buyer and payee accordingly.
- Needs decision: no

### sea/28#F2 · High · Storage charge counted twice; line amounts do not add up
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:AllowanceCharge/cbc:Amount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:ItemPriceExtension/cbc:Amount` = `51.250`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `51.250`
- Why: The one-day storage at Selanu (12.750 XLC) appears three times: as a charge "Storage while held" on line 1, as sub-line 1.2 of line 1, and as the separate collection line 2 "collected for the port". Line 1's `LineExtensionAmount` ("including allowance charges") is 38.500, i.e. without its own charge, while its `ItemPriceExtension` ("price per unit × quantity") is 51.250 although the price is 38.5 × 1. The total 51.250 = 38.500 + 12.750 only works if line 1's charge and sub-line are ignored.
- Condition: The storage is charged once; line 1's line extension equals price × quantity plus its charges; item price extension equals price × quantity; the document total equals the sum of the lines.
- Options: (a) preferred: line 1 = inspection fee 38.500 only (no charge, no storage sub-line, item price extension 38.500), line 2 = storage 12.750 collected for the port, total 51.250; (b) storage as line 1's charge (line extension 51.250) and no collection line.
- Needs decision: no

### sea/28#F3 · High · Reference to a statement issued three weeks later
- XPath: `/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-05-22`
- XPath: `25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`
- Why: The referenced statement `HF-ST-26-0151` (`25-Statement.xml`) is issued on 2026-06-13 by Harbourline Factoring, 22 days after this debit note; it also does not contain this debit note (it is a statement of Lumeway's factored receivable from Velumi). A document cannot reference one that does not yet exist.
- Condition: The debit note references no document issued after it.
- Options: drop the statement reference (preferred); or move the debit note after 06-13 and include it in a statement it belongs to.
- Needs decision: no

### sea/28#F4 · Medium · Exchange rates between a currency and itself; alternative amount in the payment currency
- XPath: `/DebitNote/cac:TaxExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:PricingExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAlternativeAmount` = `128.13`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: The document, tax, pricing and payment-alternative currencies are all XLC, so the tax, pricing and payment-alternative exchange rates are XLC→XLC at 1: each definition ("between the document currency and the tax / pricing / payment alternative currency") has nothing to convert. `PayableAlternativeAmount` ("expressed in an alternative currency") is in XBL, the payment currency, not the alternative currency XLC (51.25 × 2.5 = 128.125). And the payment currency XBL is to be paid into Velumi's XLC account. Of the four rates only the payment rate (XLC→XBL 2.5) has a purpose.
- Condition: Only exchange rates between different currencies are given; the payable alternative amount is in the alternative currency; payment currency and payee account agree or the conversion is explained.
- Options: (a) preferred: drop tax, pricing and payment-alternative rates and the alternative currency; keep payment currency XBL with the payment rate, and state the XBL amount where it belongs; (b) make XLC the payment currency (the payee's account currency) and drop all rates.
- Needs decision: no

### sea/28#F5 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/28#F6 · Medium · Customs as originator of the order; bill of lading as delivery note
- XPath: `/DebitNote/cac:DebitNoteLine/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `/DebitNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: DebitNoteLine/OriginatorParty is "The Party who originated the Order to which the Debit Note is related"; the order `VT-PO-26-0127` was originated by the Port of Selanu (`05-Order.xml`), not by customs, which only levied the inspection fee. `DeliveryNoteDocumentReference` is "A reference to a Delivery Note"; `TOL-BL-26-0139` is the ocean bill of lading (`14-BillOfLading.xml`), a transport document, not a delivery note.
- Condition: The line's originator is the party that originated the order (or absent); the bill of lading is referenced as a transport/additional document.
- Options: drop `OriginatorParty` (customs is already `CollectedForParty`), preferred; reference the B/L as an additional document with its type.
- Needs decision: no

### sea/28#F7 · Low · Buyer's accounting cost of the other party; tax point and terms details unexplained
- XPath: `/DebitNote/cbc:AccountingCost` = `Stock for municipal projects`
- XPath: `/DebitNote/cbc:TaxPointDate` = `2026-05-20`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DeliveryTerms/cbc:ID` = `CIF`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice VT-DOC-26-0153`
- Why: `AccountingCost` is the buyer's accounting code; in this debit note the buyer is Lumeway, but `500` "Stock for municipal projects" is Velumi's cost centre from its order. The tax point 2026-05-20 matches neither the inspection (05-18/19) nor the issue date (05-22), and nothing explains it. The CIF delivery term on the inspection-fee line repeats the goods' term for a service. The payment note calls the debit note an invoice.
- Condition: The accounting cost is the buyer's (Lumeway's) or absent; the tax point is a date the document explains; the line carries no delivery term without a reason; the payment note names the document correctly.
- Options: Lumeway's claims cost centre or none; tax point = date of the inspection or of issue; drop the line's delivery terms; "Debit note VT-DOC-26-0153".
- Needs decision: no

### sea/28#F8 · Low · Contacts do not fit the claim
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A recharge of customs and storage costs is handled by claims / accounts payable at the debtor and accounts receivable at the creditor; the contacts are Lumeway's customer service and Velumi's "Purchasing" in Sales (name and department contradict each other).
- Condition: The contacts handle the claim, and each contact's name and department agree.
- Options: Lumeway's claims desk (it already routes `LD-AP-CLAIMS`), Velumi's receivables or claims desk.
- Needs decision: no

## Checked and consistent
- References resolve: order `VT-PO-26-0127`, despatch advice `LD-DA-26-0145` (line 1), receipt advice `NW-RA-26-0146` (line 1, issued 05-21, before this debit note), bill of lading `TOL-BL-26-0139`, invoice `LD-INV-26-0147`, digital agreement `LD-DAG-26-0125`; container `TWLU4120872` passes the ISO 6346 check.
- Story: the illegible heat-treatment mark and the container held for a day agree with the detention and quarantine events of 2026-05-18 in `17-TransportationStatus.xml`; one day of storage (`DAY`); invoice period 05-18 to 05-19 matches discharge and the import declaration of 05-19.
- Payment: due date 2026-06-21 = issue 2026-05-22 + 30 days ("30 days net"); payment rate 2.5 = 1 / 0.4 (the XBL→XLC rate of the flow); 51.25 × 2.5 = 128.125 → 128.13; payee account `XL40BSEL0010003665515` is Velumi's (as in `27-RemittanceAdvice.xml`) and passes `check_ids.py`; RF `RF75VTDOC260153` valid.
- Tax: 0 at category O, totals 0.000.

## Considered and refuted
- `/DebitNote/cac:PurchaseReference/cbc:ID` = `TWLU4120872`: a container number as purchase reference — refuted: the element is "a reference to an object ... to which this Debit Note relates", and the charges concern that container.
- `/DebitNote/cac:Annotation/cbc:AnnotationContent` = `The distributor may claim it from the packer.`: contradiction with Lumeway packing the goods — refuted: the note puts the responsibility on "the packer", a party other than the distributor (the manufacturer's pallets), which the annotation keeps consistent.
- `/DebitNote/cac:DiscrepancyResponse/cbc:ResponseCode` = `2`: "Below specification goods" for an illegible mark — refuted: an illegible ISPM 15 mark makes the packaging non-conforming, a plausible reading.
