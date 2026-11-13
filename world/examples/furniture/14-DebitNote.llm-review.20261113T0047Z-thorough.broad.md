# LLM review: 14-DebitNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/14#F1 · High · Accounting roles contradict seller, buyer, payee and issuer
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cbc:AccountingCostCode` = `6120`
- XPath: `/DebitNote/cbc:ID` = `BS-DOC-26-0580`
- Why: A Debit Note specifies "debits due to the Creditor from the Debtor". Here the store charges the maker for the return transport (note; issued with the store's number `BS-DOC-26-0580`; the service item ID `BM-SVC-RT` is "assigned by the seller"; seller = Brightmarket, buyer = Brackenmere; payee and payee account are the store's). The accounting parties say the opposite: accounting supplier Brackenmere, accounting customer Brightmarket, so the party that is to pay is also the payee. `AccountingCostCode` 6120 "Garden department", defined as the buyer's accounting code, is the store's own cost centre (as in `08-Order.xml`), although the buyer of this transport is Brackenmere.
- Condition: Within the debit note, the creditor (accounting supplier, seller, payee, issuer) and the debtor (accounting customer, buyer) are one consistent pair, and the buyer's accounting code belongs to the buyer.
- Options: (a, preferred) accounting supplier Brightmarket and accounting customer Brackenmere, matching seller, buyer and payee, without a separate `PayeeParty` (it equals the creditor) and without the store's cost centre as buyer's code (or with Brackenmere's); (b) if the world means a debit note in the sense of a buyer's claim against the seller, swap seller and buyer instead and take the item ID as the buyer's — the choice changes who is creditor, hence the decision.
- Needs decision: yes

### furniture/14#F2 · Medium · Quotation number used as contract reference
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`
- Why: `ContractDocumentReference` is "A reference to a contract associated with this document". `BF-DOC-26-0568` is the quotation `02-Quotation.xml`, not a contract, and nothing in the quotation covers return transport.
- Condition: `ContractDocumentReference` references a contract, or is absent.
- Options: (a, preferred) remove it; the instruction for returns (already referenced) is the basis of the charge.
- Needs decision: no

### furniture/14#F3 · Medium · Language code in LocaleCode
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/14#F4 · Low · The credit note's restocking deduction is repeated without a purpose
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cbc:Amount` = `3477.00`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- Why: The debit line references line 1 of the credit note 13 with its amount and its restocking deduction. The debit note charges transport and does nothing with the credit amount or the deduction (it neither disputes nor reverses it), so the repeated figures have no function in this document.
- Condition: The billing reference line carries only what the debit relates to (e.g. the referenced line ID), or the debit note states what it does with the deduction.
- Options: (a, preferred) keep the reference to credit note line 1 and drop amount and allowance; (b) if the store disputes the deduction, say so and charge it back.
- Needs decision: no

### furniture/14#F5 · Low · Payment note calls the debit note an invoice
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BS-DOC-26-0580`
- Why: The document is a debit note (type 383), not an invoice; the note for the payee's account should name it correctly.
- Condition: The payment note names the debit note.
- Options: (a, preferred) "Debit note BS-DOC-26-0580".
- Needs decision: no

### furniture/14#F6 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- 1 service unit × 85 = 85.00 = line extension = tax-inclusive line amount = payable; tax exempt as a service to a business.
- `/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02` lies in the requested period 2026-04-29 to 2026-05-02 of `12-InstructionForReturns.xml`; GLN `9523710900015` check digit correct.
- Due date 2026-06-03 = 30 days after 2026-05-04, as the payment terms say; RF and IBAN-like check digits pass.
- `/DebitNote/cac:BillingReference/cac:CreditNoteDocumentReference/cbc:ID` = `BF-CN-26-0579` resolves to `13-CreditNote.xml`; the referenced line amounts 3 477.00 and 183.00 are those of 13.
