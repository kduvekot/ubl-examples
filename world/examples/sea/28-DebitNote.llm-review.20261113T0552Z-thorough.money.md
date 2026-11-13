# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/28#F1 · High · Line arithmetic does not close; the storage charge appears three times
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:TaxInclusiveLineExtensionAmount` = `38.500`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:AllowanceCharge/cbc:Amount` = `12.750`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:Price/cbc:PriceAmount` = `38.5`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:ItemPriceExtension/cbc:Amount` = `51.250`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:LineExtensionAmount` = `12.750`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `51.250`
- Why: Line 1's `LineExtensionAmount` is "the total amount for this debit note line, including allowance charges but net of taxes"; with the line's own charge of 12.750 it would be 38.500 + 12.750 = 51.250, not 38.500. Its `ItemPriceExtension` is "calculated by multiplying the price per unit by the quantity": 38.5 × 1 = 38.500, not 51.250. The port storage of 12.750 is stated as a charge on line 1, as sub-line 1.2 of line 1, and once more as a separate collection line 2 "collected for the port". The document total 51.250 = 38.500 + 12.750 counts it once, but only by adding line 1's extension without its charge to the collection line, so whether storage is in line 1 or in line 2 cannot be read from the document.
- Condition: Storage appears once; every line's extension amount equals price × quantity plus its own charges; the price extension equals price × quantity; the sub-lines add up to their parent line; the line extension total is the sum of the line extensions.
- Options: (a) preferred: line 1 is the customs inspection only (38.500, no charge, no storage sub-line, price extension 38.500), and storage is the collection line 2 (12.750); total 51.250; (b) line 1 carries both (51.250 with the storage charge and the two sub-lines, price extension 38.500), and the collection line is dropped.
- Needs decision: no

### sea/28#F2 · High · Payable alternative amount in XBL although the alternative currency is XLC; payment currency XBL to an XLC account
- XPath: `/DebitNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAlternativeAmount` = `128.13`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/DebitNote/cbc:PaymentCurrencyCode` = `XBL`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: `PayableAlternativeAmount` is "the amount of the monetary total to be paid, expressed in an alternative currency"; the document names XLC as the alternative currency, with an XLC→XLC rate of 1, which would give 51.250 XLC, while the amount is 128.13 in XBL (51.250 × 2.5 = 128.125, i.e. the payment currency via `PaymentExchangeRate`). The payment currency is XBL, but the payee's account to be credited is held in XLC, and the document currency is XLC too: the debtor would convert XLC into XBL only for the bank to convert it back.
- Condition: The payable alternative amount is in the alternative currency the document names, at its stated rate; payment currency, alternative currency and the payee account's currency agree with a stated reason for any conversion.
- Options: (a) preferred: payment in XLC (the document and account currency), XBL as the alternative currency for the Bayvarran debtor with rate 2.5 and alternative amount 128.13 XBL; drop the XLC→XLC rates; (b) keep payment in XBL and give an XBL account of Velumi.
- Needs decision: no

### sea/28#F3 · High · Debit note of 2026-05-22 refers to a statement issued on 2026-06-13
- XPath: `/DebitNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- XPath: `/DebitNote/cbc:IssueDate` = `2026-05-22`
- Why: The statement HF-ST-26-0151 was issued by Harbourline Factoring on 2026-06-13 (`25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`), three weeks after this debit note. It is the factor's statement of Lumeway's receivable on Velumi and does not list this debit note, which is a claim of Velumi on Lumeway. The reference cannot exist when the debit note is issued, and the statement has no relation to the claim.
- Condition: Every document the debit note refers to exists on its issue date and concerns the debited amount.
- Options: (a) preferred: drop the statement reference; (b) none better.
- Needs decision: no

### sea/28#F4 · High · Debtor and creditor reversed between the party roles
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cbc:AccountingCost` = `Stock for municipal projects`
- Why: A debit note specifies "debits due to the Creditor from the Debtor". Velumi issues it (`/DebitNote/cbc:ID` = `VT-DOC-26-0153`), is paid under it (payee, payee account) and is named seller; Lumeway pays and is named buyer. In the same document, Lumeway is the accounting supplier and Velumi the accounting customer, so the accounting customer is also the payee who receives the money, and the accounting supplier is the buyer. The buyer's accounting code (`AccountingCost`, "the Buyer's accounting code") is Velumi's own code from its order (`05-Order.xml:/Order/cbc:AccountingCost` = `Stock for municipal projects`), although the buyer here is Lumeway. Under one consistent reading (Velumi charges Lumeway), Velumi is accounting supplier, seller and payee, and Lumeway accounting customer and buyer.
- Condition: The accounting supplier and the seller are the same creditor (who is also payee, or the payee differs from it with a reason); the accounting customer and the buyer are the same debtor; the buyer's accounting code belongs to that buyer.
- Options: (a) preferred: Velumi as accounting supplier (and seller, payee), Lumeway as accounting customer and buyer, with Lumeway's accounting code or none; (b) if the debit note is meant in the original sale's roles (Lumeway supplier, Velumi customer), then Velumi debits itself, which contradicts the payee; so (a) is the only consistent reading.
- Needs decision: yes

### sea/28#F5 · Medium · Inspection fee already paid to customs presented as collected on behalf of customs
- XPath: `/DebitNote/cac:DebitNoteLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DocumentReference/cbc:ID` = `XL-CUS-RCPT-26-0517`
- Why: `CollectedForParty` is "the Party on whose behalf this item or amount is collected". The line refers to a customs receipt, so the fee was already paid to the Island Customs Service; Velumi recovers its own outlay from Lumeway and does not collect for customs (it will pass nothing on). The storage line, by contrast, is a collection line "collected for the port", which the document does not show as already paid.
- Condition: `CollectedForParty` names a party only for amounts the issuer collects and passes on; a recharge of an outlay already paid is a normal debit line without it (or a disbursement, with the receipt as evidence).
- Options: (a) preferred: drop `CollectedForParty` from line 1, keeping the receipt reference as evidence of the outlay; (b) if Velumi has not yet paid customs, drop the receipt reference instead.
- Needs decision: no

### sea/28#F6 · Low · Tax point date, tax and pricing currency and identity exchange rates in a single-currency debit note without tax
- XPath: `/DebitNote/cbc:TaxPointDate` = `2026-05-20`
- XPath: `/DebitNote/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/DebitNote/cbc:PricingCurrencyCode` = `XLC`
- XPath: `/DebitNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/DebitNote/cac:PricingExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/DebitNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `1`
- Why: The document, its prices and its (zero) tax are all in XLC, and the island has no general sales tax (category O, "No general sales tax"). Tax and pricing currency equal to the document currency, three XLC→XLC rates of 1, and a tax point date for a tax that does not exist add no information (no fillers, IND5/IND6).
- Condition: Currency codes and exchange rates appear only where a second currency is involved; a tax point date only where a tax applies.
- Options: (a) preferred: drop them, keeping only the XLC↔XBL rate the payment needs (see F2); (b) none better.
- Needs decision: no

## Checked and consistent
- Due date 2026-06-21 = 2026-05-22 + 30 days, as the terms say ("30 days net"); the payment means' due date agrees.
- 51.250 XLC × 2.5 = 128.125 → 128.13 XBL; 2.5 is the inverse of the flow's 0.4.
- Payee account `XL40BSEL0010003665515` is Velumi's own (the payer account in the remittance advice); RF reference `RF75VTDOC260153` valid.
- Tax category O ("outside scope") with 0.000 tax fits services in Lisavu, which has no general sales tax.
- The customs inspection followed the hold at Selanu reported by the terminal (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`).

## Considered and refuted
- `/DebitNote/cac:DebitNoteLine/cac:ReceiptLineReference/cbc:LineID` = `1`: suspected that the referenced receipt line ("Received as despatched.") does not support the claim — refuted because the defect was found at the port before goods-in, and the receipt line is cited for the goods concerned, not as evidence of the defect.
- `/DebitNote/cac:InvoicePeriod/cbc:EndDate` = `2026-05-19`: suspected two days of storage against one debited day — refuted because a period from 2026-05-18 to 2026-05-19 can be the 24-hour period of the hold; the quantity of 1 DAY is consistent with it.
- The debit note is not settled by any later document of the flow: refuted as a finding because a claim between the parties may be settled outside the documents shown; the remittance advice correctly does not net it against the factored invoice.
