# LLM review: 13-CreditNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/13-CreditNote.xml`, Git blob `62fa2031ce86b8f92b5eb82929f1d00df2904665` (committed)
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

### furniture/13#F1 · Medium · Language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/13#F2 · Low · Restocking deduction on a return the maker asked for
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Restocking deduction`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- XPath: `12-InstructionForReturns.xml:/InstructionForReturns/cbc:Note` = `The maker takes back six sets to free the store's shelf.`
- XPath: `14-DebitNote.xml:/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`
- Why: The return was initiated by the maker (Instruction For Returns: "The producer is requesting the return of products that are not selling well"), as 12 and 14 both say. A restocking deduction is what a seller charges when the buyer returns goods on its own initiative. Deducting 5 % from the store's credit for a return the maker itself requested, while the store charges the maker for the transport (14), is commercially contradictory. Whether such a term exists between the parties is a question for the story.
- Condition: The credit for the returned sets either has no restocking deduction, or the flow states the agreement under which the store bears it despite the maker's request.
- Options: (a, preferred) no deduction: credit 3 660.00, since the maker asked for the return; (b) keep it with a note naming the agreement.
- Needs decision: yes

### furniture/13#F3 · Low · Refund or set-off: notes disagree
- XPath: `/CreditNote/cbc:Note` = `The store paid the invoice; the credit is refunded.`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: The document note says the credit is refunded (and the payment means give the store's account and a due date); the payment terms say it is settled against the next payment to the seller unless refunded. One of the two ways of settling has to be the one that applies.
- Condition: The note and the payment terms state the same way of settling the credit.
- Options: (a, preferred) payment terms that say the credit is refunded by credit transfer by 2026-05-13, matching the note and the payment means.
- Needs decision: no

### furniture/13#F4 · Low · Refund payment references describe an invoice and are issued by the payer
- XPath: `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579`
- XPath: `/CreditNote/cac:PaymentMeans/cbc:PaymentID` = `RF63BFCN260579`
- XPath: `/CreditNote/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF63BFCN260579`
- Why: The payment note calls the credit note an invoice. The RF creditor reference (ISO 11649, a reference the creditor gives the debtor to quote) is built from Brackenmere's credit note number, although for the refund the payee is the store and Brackenmere is the payer; the instruction "Quote …" is addressed to the party that pays, here the issuer itself.
- Condition: The payment note names the credit note as such, and the payment references of the refund are ones the payer can use as its own remittance reference (or are absent).
- Options: (a, preferred) payment note "Credit note BF-CN-26-0579", and the credit note number as plain `PaymentID` without the RF form and without "Quote"; (b) remove the payment ID and instruction note.
- Needs decision: no

### furniture/13#F5 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- 6 SET × 610 = 3 660; 5 % = 183; 3 660 − 183 = 3 477 = line extension = all totals; tax 0.00 (exempt, as in the invoice).
- `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate` = `2026-03-22`, the issue date of `09-Invoice.xml`; credited quantity 6 = the 6 sets of `12-InstructionForReturns.xml`, delivered back on 2026-05-02 (14) before this credit note (2026-05-03).
- Payee account `XB48BLUM38010001570935` is the store's (same as in 14); IBAN-like and RF check digits pass.
