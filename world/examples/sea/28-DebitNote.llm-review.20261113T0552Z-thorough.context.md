# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCost` = `Stock for municipal projects`
- Why: A debit note is "A document used to specify debits due to the Creditor from the Debtor". The document is issued and signed by Velumi Trading (ID `VT-DOC-26-0153`), asks for payment into Velumi's account, and passes on to Lumeway costs Velumi incurred (customs inspection and storage caused by the illegible pallet mark, which the note calls "the packer's responsibility"). So Velumi is the creditor and Lumeway the debtor. The accounting parties say the opposite: Lumeway as accounting supplier (the creditor's role) and Velumi as accounting customer (the debtor's role), while Velumi is also the payee. The seller and buyer are given the other way round (Velumi seller, Lumeway buyer), so within one document the roles contradict each other. The line's accounting cost "Stock for municipal projects" is Velumi's own cost centre from the order (`05-Order.xml:/Order/cbc:AccountingCost` = `Stock for municipal projects`), which in a debit note is "The buyer's accounting cost centre" — here that would be Lumeway's.
- Condition: The accounting supplier is the creditor that issues the debit note and receives payment (Velumi), the accounting customer is the debtor (Lumeway); payee appears only if different from the accounting supplier; the buyer's accounting code, if any, is the debtor's.
- Options: (a) preferred: Velumi as accounting supplier (and seller of the recharge, if seller/buyer are kept), Lumeway as accounting customer, no separate payee, no accounting cost or one of Lumeway's; (b) if the intent is a correction of Lumeway's invoice issued by Lumeway, the issuer, ID and payee must change instead, which changes the story.
- Needs decision: no

### sea/28#F2 · High · Reference to a statement issued three weeks after this debit note
- XPath: `/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-05-22`
- Why: `StatementDocumentReference` is "A reference to a Statement associated with this document". The statement `HF-ST-26-0151` exists, but it is issued on 2026-06-13 (`25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`), after this debit note of 2026-05-22. A document cannot refer to a document that does not yet exist. That statement is also the factor's statement of Lumeway's receivable from Velumi; it does not contain this debit note.
- Condition: Every document the debit note refers to exists on its issue date and is related to the debit.
- Options: (a) preferred: remove the reference; (b) issue the debit note after 2026-06-13 if it is meant to be set off against the factored balance, which changes the timeline.
- Needs decision: no

### sea/28#F3 · High · The storage charge appears three times and the line amount excludes its own charge
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:AllowanceCharge/cbc:Amount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:ItemPriceExtension/cbc:Amount` = `51.250`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `51.250`
- Why: The storage at the port (12.750 XLC) is stated as a charge on line 1, as sub-line 1.2 of line 1, and as a separate collection line "collected for the port". Line 1's `LineExtensionAmount` is "The total amount for this debit note line, including allowance charges but net of taxes", yet it is 38.500, i.e. without its own 12.750 charge, while its price extension is 51.250 (38.5 + 12.75). The document total 51.250 equals 38.500 + 12.750 once, so either the line charge or the collection line is not counted, and the reader cannot tell which. Calculation: 38.500 + 12.750 = 51.250; with the line charge included in line 1 and the collection line added, the total would be 64.000.
- Condition: The storage charge is stated once; each line amount includes its own allowances and charges; the sum of the line amounts equals the document's line extension total.
- Options: (a) preferred: line 1 = customs inspection 38.500 only (no charge, no sub-lines), collection line 2 = storage 12.750 for the Port of Selanu; total 51.250; (b) keep storage inside line 1 (as charge or sub-line, not both), line amount 51.250, and drop the collection line.
- Needs decision: no

### sea/28#F4 · Medium · Exchange rates between a currency and itself, and an alternative amount in a currency that is not the alternative one
- XPath: `/DebitNote/cac:TaxExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:PricingExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAlternativeAmount` = `128.13`
- Why: The document currency is Coral (XLC). The tax currency, pricing currency and payment alternative currency are also Coral, and each comes with an exchange rate from Coral to Coral at 1 (`TaxExchangeRate` "between the document currency and the tax currency", `PricingExchangeRate`, `PaymentAlternativeExchangeRate`). These say nothing that their absence would not say (rule: no fillers). The payable alternative amount, "expressed in an alternative currency", is 128.13 in Lume (XBL), which is the payment currency (`PaymentCurrencyCode` XBL, rate 2.5), not the declared alternative currency (XLC). The payee account Velumi names is a Coral account, so asking for payment in Lume into it is also odd.
- Condition: Tax, pricing and alternative payment currencies and their rates are present only where they differ from the document currency; the payable alternative amount is in the payment alternative currency.
- Options: (a) preferred: Coral throughout (document, payment), no tax/pricing/alternative rates; if Lumeway may pay in Lume, declare XBL as the payment alternative currency with the rate 2.5 and the amount 128.13; (b) keep payment in Lume, drop the alternative currency and amount.
- Needs decision: no

### sea/28#F5 · Medium · A bill of lading given as the delivery note
- XPath: `/DebitNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: `DeliveryNoteDocumentReference` is "A reference to a Delivery Note associated with this document". `TOL-BL-26-0139` is the carrier's bill of lading (`14-BillOfLading.xml`), a transport document and document of title, not a delivery note. A reference of one kind is used as another.
- Condition: The delivery note reference names a delivery note, or is absent; the bill of lading, if needed, is referenced as an additional document.
- Options: (a) preferred: move the bill of lading to a general document reference (with a type), or drop it; the despatch advice and receipt advice already cover the delivery.
- Needs decision: no

### sea/28#F6 · Medium · Island Customs Service named as originator of the order
- XPath: `/DebitNote/cac:DebitNoteLine/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: The line's `OriginatorParty` is "The Party who originated the Order to which the Debit Note is related". The order `VT-PO-26-0127` was originated for the Port of Selanu (`05-Order.xml:/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`). Customs carried out the inspection that caused the cost, and is already named as `CollectedForParty`; it did not originate any order.
- Condition: The originator is the party that originated the order, or the element is absent.
- Options: (a) preferred: remove it; customs is identified as the party the fee is collected for.
- Needs decision: no

### sea/28#F7 · Low · Further values without a reason in this debit note
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:FreeOfChargeIndicator` = `false`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DeliveryTerms/cbc:ID` = `CIF`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice VT-DOC-26-0153`
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/DebitNote/cac:ProjectReference/cbc:ID` = `VT-PRJ-26-07`
- Why: `FreeOfChargeIndicator` false is the stated default ("The default is false") and says nothing. Delivery terms CIF on a line for a customs inspection fee do not apply to that service. The payment note calls the debit note an "Invoice". The contract referenced is the Digital Agreement on electronic exchange (`03-DigitalAgreement.xml`), though the note says the packer's responsibility arises "under the agreement" (the sale's terms would be that agreement). The project `VT-PRJ-26-07` occurs only here and in `26-CreditNote.xml` (counted with `grep -l VT-PRJ-26-07 world/examples/*/*.xml`), not in the order or invoice.
- Condition: Each of these is either removed or given a value that fits this debit note (the debit note's own number in the payment note; the sale's terms as the contract; a project only if the order carries it).
- Options: (a) preferred: remove the free-of-charge indicator, the line delivery terms and the project; reference the sale's terms (`LD-GTC-2026`) as the contract; correct the payment note.
- Needs decision: no

## Checked and consistent
- The pallet SSCC `095206101230000070` in the discrepancy description has a valid GS1 check digit and is the pallet in `14-BillOfLading.xml`; the cause (heat-treatment mark) agrees with the container's quarantine event and the detention text in `17-TransportationStatus.xml` (2026-05-18).
- Due date 2026-06-21 = issue date 2026-05-22 + 30 days, as the note "30 days net" says.
- Payable alternative 51.250 × 2.5 = 128.125, stated 128.13.
- References: order, despatch advice (line 1), receipt advice (line 1), invoice `LD-INV-26-0147` and the container `TWLU4120872` (ISO 6346 check digit OK) exist in the flow.

## Considered and refuted
- `/DebitNote/cac:WorkReportDocumentReference/cbc:ID`: the customs inspection record `XL-CUS-INSP-26-0517` as a "work report" suspected as a reference of the wrong kind — refuted because it reports the work (inspection) whose cost is passed on, which is what a work report reference is for; that the document is not in the flow is a matter for the logistics lens.
- `/DebitNote/cac:PurchaseReference/cbc:ID`: a container number as purchase reference suspected as misuse — refuted because the definition covers "an object, such as … a vehicle … to which this Debit Note relates", and the inspected container is that object.
- `/DebitNote/cac:DiscrepancyResponse/cbc:ResponseCode`: code 2 "Below specification goods" for an illegible pallet mark suspected unfit — refuted because the packaging failed a specification (ISPM 15 marking) the goods had to meet.
