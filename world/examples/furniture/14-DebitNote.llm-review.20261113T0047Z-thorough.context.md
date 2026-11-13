# LLM review: 14-DebitNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/14-DebitNote.xml`, Git blob `46010db5dff2abd14661e7fabad9e7fd90e953c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/14#F1 · High · Accounting supplier and customer contradict seller, buyer and payee
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: A Debit Note is "A document used to specify debits due to the Creditor from the Debtor". Here the store charges the maker for transport (`/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`): the store is the creditor, seller of the service and payee, the maker the debtor and buyer. Seller, buyer and payee say exactly that. The accounting parties say the opposite: the maker is the accounting supplier (the party that claims the amount) and the store the accounting customer (the party that owes it), so the store would be both the debtor and the payee of its own debt. The document number `BS-DOC-26-0580` and the seller's item number `BM-SVC-RT` are the store's, which confirms that the store issues and claims.
- Condition: the accounting supplier is the party that claims the debit (the store), the accounting customer the party that owes it (the maker), consistent with seller, buyer, payee, document numbering and payment account; `PayeeParty` is present only if different from the accounting supplier.
- Options: (a) swap the accounting parties and drop `PayeeParty` (it then equals the accounting supplier) (preferred: matches the note and every other role in the document); (b) model the charge as a reduction of the maker's next invoice instead, which would change the flow.
- Needs decision: yes

### furniture/14#F2 · Medium · The store's cost centre given as the buyer's accounting code
- XPath: `/DebitNote/cbc:AccountingCostCode` = `6120`
- XPath: `/DebitNote/cbc:AccountingCost` = `Garden department`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCostCode` = `6120`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCost` = `Garden department`
- Why: UBL defines the header `AccountingCostCode` as "The Buyer's accounting code" and the line element as "The buyer's accounting cost centre for this debit note line". The buyer in this debit note is Brackenmere Furniture; `6120` "Garden department" is the store's own cost centre (the buyer's code in `08-Order.xml:/Order/cbc:AccountingCostCode` = `6120`, when the store was the buyer). In this document it is the seller's cost centre, which the element does not carry.
- Condition: `AccountingCostCode`/`AccountingCost` carry the cost centre of the buyer of this debit note (the maker), or are absent.
- Options: (a) remove them (preferred: the store issuing the document does not know the maker's cost centre, and none is given in the story); (b) the maker's cost centre, if the story gives one.
- Needs decision: no

### furniture/14#F3 · Medium · The quotation referred to as a contract
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`
- Why: `ContractDocumentReference` is "A reference to a contract associated with this document". `BF-DOC-26-0568` is the quotation `02-Quotation.xml`, an offer, not a contract. The contract of the trade is `BM-OWN-BRAND-2026` (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`). A document of one kind is referenced as another.
- Condition: `ContractDocumentReference` refers to a contract of the story, or is absent.
- Options: (a) `BM-OWN-BRAND-2026`, if that agreement provides for return transport charges (preferred); (b) remove it.
- Needs decision: no

### furniture/14#F4 · Medium · LocaleCode holds a bare language code
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/14#F5 · Low · Credit-note line amount and restocking deduction carried in a transport debit
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cbc:Amount` = `3477.00`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- Why: The debit line charges 85 for return transport. Its billing reference repeats the amount of the credit note's line (3477.00) and that line's restocking deduction (183.00). `BillingReferenceLine` is "A reference to a transaction line in the billing document"; the line ID suffices for that. The amounts of the credited goods play no part in this debit (the transport is a flat 85 per delivery), so the debit note copies data it does nothing with.
- Condition: the billing reference line identifies the credit note line without amounts and allowances that do not bear on the debit, or the reference stays at document level.
- Options: (a) keep `BillingReferenceLine/ID` only (preferred); (b) drop the line-level billing reference, keeping the header one.
- Needs decision: no

### furniture/14#F6 · Low · Payment note calls the debit note an invoice
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BS-DOC-26-0580`
- Why: `PaymentNote` is the text for the owner of the account on the payment; `BS-DOC-26-0580` is this debit note, not an invoice.
- Condition: the payment note names the document by its kind (debit note) or carries only its number.
- Options: (a) "Debit note BS-DOC-26-0580" (preferred).
- Needs decision: no

### furniture/14#F7 · Low · Store's master data copied into the debit note
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in a transport debit (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `BillingReference/CreditNoteDocumentReference` resolves to `13-CreditNote.xml`; `AdditionalDocumentReference` and the line's `DocumentReference` to the return instruction `12-InstructionForReturns.xml`.
- `Delivery/ActualDeliveryDate` 2026-05-02 falls in the requested delivery period of `12-InstructionForReturns.xml` (2026-04-29 to 2026-05-02); delivery location Marrowdale is the maker's town.
- `PaymentPurposeCode` = `SCVE` (purchase/sale of services) fits a transport service; `DiscrepancyResponse` "Goods returned" gives the reason.

## Considered and refuted
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `1` with unit `E48` (service unit): suspected odd for transport — refuted because one return delivery is one service unit, as the item description ("per delivery") says.
