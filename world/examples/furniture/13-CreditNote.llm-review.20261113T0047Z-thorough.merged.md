# LLM review: 13-CreditNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/13-CreditNote.xml`, Git blob `62fa2031ce86b8f92b5eb82929f1d00df2904665` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/13#F2 · Low · Restocking deduction on a return the maker asked for
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Restocking deduction`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- XPath: `12-InstructionForReturns.xml:/InstructionForReturns/cbc:Note` = `The maker takes back six sets to free the store's shelf.`
- XPath: `14-DebitNote.xml:/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`
- Why: A restocking deduction compensates a seller for taking back goods the buyer chose to return. Here the return is the maker's initiative (an Instruction for Returns is "The producer … requesting the return of products that are not selling well"), as 12 and 14 both say. The maker asks for the goods back, then deducts 5 % for restocking them, while the store charges the maker for the transport. The reason code 64 "Special agreement" could mean the deduction was agreed, but no document of the flow (quotation 02, return instruction 12) states such an agreement. Whether such a term exists is a question for the story.
- Condition: The flow states the agreement under which the store bears a restocking deduction for a return the maker requested, or the credit note credits the returned sets without it (3660.00).
- Options: (a) remove the deduction and credit 3660.00 (broad's preference), which also changes the billing reference amount in 14; (b) state the agreed return terms where the return is arranged (12, or the quotation) so the deduction rests on them (money's preference); (c) change the story so the store asks to return the sets. The merge prefers (a) as the smallest change consistent with 12 and 14.
- Needs decision: yes
- From: broad, money

### furniture/13#F3 · Low · Payment terms describe a set-off the document note rules out
- XPath: `/CreditNote/cbc:Note` = `The store paid the invoice; the credit is refunded.`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: The document note and the payment means (credit transfer to the store's account by 2026-05-13) say the credit is refunded. The payment terms state set-off against the next payment as the rule and refund as the exception, keeping open a route the document has already excluded.
- Condition: Note, payment terms and payment means state the same way of settling the credit.
- Options: (a, preferred) payment terms that say the credit is refunded by credit transfer by 2026-05-13; (b) drop the terms note, since the payment means already say it; (c) a netting story without a refund payment means.
- Needs decision: no
- From: broad, money, context

### furniture/13#F4 · Low · Payment note calls the credit note an invoice
- XPath: `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-CN-26-0579`
- Why: `PaymentNote` is "Free-form text applying to the Payment for the owner of this account", i.e. the text the store sees on the refund. The document is a credit note (`/CreditNote/cbc:CreditNoteTypeCode` = `381`); the text calls it an invoice. The same wording occurs in `14-DebitNote.xml` ("Invoice BS-DOC-26-0580"); in `09-Invoice.xml` it is correct.
- Condition: The payment note names the document as a credit note (or refund), or carries only its number.
- Options: (a, preferred) "Credit note BF-CN-26-0579" or "Refund of credit note BF-CN-26-0579".
- Needs decision: no
- From: broad (part of its F4), money, context

### furniture/13#F5 · Low · Creditor reference built from the refunding party's own number
- XPath: `/CreditNote/cac:PaymentMeans/cbc:PaymentID` = `RF63BFCN260579`
- XPath: `/CreditNote/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF63BFCN260579`
- Why: An ISO 11649 reference is a structured creditor reference that the creditor creates to match the incoming payment (own knowledge). For this refund the creditor is the store (`/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Brightmarket Stores Corp`), but the reference is built from the maker's credit note number, and the instruction "Quote …" addresses the payer, which is the maker itself. In `09-Invoice.xml` and `14-DebitNote.xml` the RF reference is built by the party that receives the money.
- Condition: The payment identifier of the refund is one the payee can match (or a plain remittance identifier of the payer), and the instruction note addresses the party that makes the payment, or is absent.
- Options: (a, preferred) the credit note number as a plain `PaymentID` without the ISO 11649 scheme, and no "Quote" instruction; (b) a reference the store assigned; (c) remove payment ID and instruction note.
- Needs decision: no
- From: broad (part of its F4), money

### furniture/13#F6 · Low · Own-line item carries the maker's brand
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: The description says the set is the store's own line, and the quotation adds the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` ("A brand name of this item") names the maker. Text and brand disagree unless the story means a co-branded or exclusive maker-branded line.
- Condition: The item's brand and its description of the line agree.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) reword as an exclusive Brackenmere line made for the store.
- Needs decision: yes
- From: context

### furniture/13#F7 · Low · Brightmarket's contact is a sales desk in an accounting-customer role
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name ("Buying office"), job title ("Customer service officer") and department ("Sales") do not agree with each other, and none fits the accounting customer of a credit note, whose contact would be accounts (receivable for a refund, or payable). The same contact is used in every example where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) an accounts contact in billing documents; (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/13#F8 · Low · Store's master data copied into the credit note
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital come from the store's master data; a credit note for returned furniture uses none of them (section 4.8, IND5). Carried on Brightmarket in examples 01 to 14.
- Condition: Present only in documents of the flow where they have a business reason.
- Options: (a, preferred) remove them from this document.
- Needs decision: no
- From: parties (web site, social media), context (also logo and share capital)

### furniture/13#F9 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/*/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Arithmetic (merge recalculation): `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `6` sets × 610 = 3660.00 = `/CreditNote/cac:CreditNoteLine/cac:ItemPriceExtension/cbc:Amount` = `3660.00` = `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:BaseAmount` = `3660.00`; 0.05 × 3660.00 = 183.00; 3660.00 − 183.00 = 3477.00 = `/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `3477.00` = tax exclusive = tax inclusive = `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3477.00`; taxable 3477.00, tax 0.00 (exempt, as the invoice).
- Against the invoice: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `BF-INV-26-0575` resolves to `09-Invoice.xml`, issue date 2026-03-22 as stated; price 610 and STT/RESALE treatment are the invoice's; 6 of 20 invoiced sets credited, the quantity of `12-InstructionForReturns.xml:/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Quantity` = `6`.
- Against the debit note: `14-DebitNote.xml` refers to this credit note with line amount 3477.00 and the 183.00 deduction.
- Dates: the credit note (2026-05-03) follows the return delivery of 2026-05-02 recorded in `14-DebitNote.xml`; due date 2026-05-13 is ten days after issue.
- Refund account `XB48BLUM38010001570935` passes the IBAN-style check, contains branch 380100, is held by the store and is its account in 14 as well; `RF63BFCN260579` passes ISO 11649.
- Other references: `BS-PO-26-0574` resolves to `08-Order.xml`, `BF-DOC-26-0578` to `12-InstructionForReturns.xml`.

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:ChargeIndicator` = `false`: a restocking fee suspected to be wrongly encoded as an allowance — refuted because in a credit note the deduction reduces the credit, i.e. it is an allowance on the credited amount; a charge would increase the credit (from money).
- `/CreditNote/cac:CreditNoteLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: "Special agreement" suspected not to match "Restocking deduction" — refuted as a code/text mismatch: the code names the basis, the text the nature; whether the agreement exists is F2 (from money).
- `/CreditNote`: a credit for returned goods with no record that they arrived — refuted because the flow records the arrival (`14-DebitNote.xml:/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02`) (from logistics).
- `/CreditNote/cbc:DueDate` = `2026-05-13`: a due date on a credit note suspected out of place — refuted because the definition ("The date on which this Credit Note is due") applies to a refund that is to be paid (from context).
- `/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name`: the payee account is the customer's — refuted because the credit is refunded to the store (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F9 by the merge.
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact as accounting supplier — refuted because a small enterprise's trade-sales desk plausibly handles the whole relationship, and name, title and department agree (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name`/`ID` — refuted because the aggregate is the profile; its presence is F8 (from parties).

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F9: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- broad/F1, parties/F1, context/F1 → F1: removal preferred, as in earlier flows.
- broad/F2, money/F1 → F2: combined; both parts' preferred options kept, the merge prefers removal of the deduction.
- broad/F3, money/F2, context/F2 → F3: combined.
- broad/F4 split: its payment-note half joined money/F4 and context/F3 as F4; its RF-reference half joined money/F3 as F5 (two problems with different conditions).
- broad/F5, parties/F2 → F7: combined; wording fitted to the accounting-customer role.
- parties/F3, context/F5 → F8: grouped.
