# LLM review: 14-DebitNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/14-DebitNote.xml`, Git blob `46010db5dff2abd14661e7fabad9e7fd90e953c2` (committed)
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

### furniture/14#F1 · High · Accounting supplier and customer are the reverse of seller, buyer, payee and issuer
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Brightmarket Stores Corp`
- XPath: `/DebitNote/cbc:ID` = `BS-DOC-26-0580`
- XPath: `/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`
- Why: A Debit Note is "A document used to specify debits due to the Creditor from the Debtor". The store charges the maker 85.00 for the return transport it performed with its own van: the store is the creditor, issuer (`BS-` number), seller of the service (`SellerSupplierParty`; the item ID `BM-SVC-RT` is the store's) and payee with its own account; the maker is the debtor and buyer. The accounting parties say the opposite: the maker is the accounting supplier (the party that claims the amount) and the store the accounting customer (the party that settles it), so the store would be both the debtor and the payee (`PayeeParty`, "The Party who receives the Payment") of its own claim. Under no single reading are both role pairs right: if the document keeps the roles of the original sale, seller and buyer must not be swapped either. The same pattern (PayeeParty = AccountingCustomerParty, seller/buyer reversed against the accounting parties) occurs in `sea/28-DebitNote.xml` (money's script check over the three `*DebitNote*.xml`), which suggests a convention of the generator; UBL defines none, hence the decision.
- Condition: Accounting supplier, seller, payee and issuer are one party (the creditor), accounting customer and buyer the other (the debtor); `PayeeParty` is present only if the payee differs from the accounting supplier.
- Options: (a, preferred) Brightmarket as accounting supplier and Brackenmere as accounting customer, matching seller, buyer, payee and the note; `PayeeParty` removed (it would equal the accounting supplier); all four parts prefer this. (b) If the world means a debit note issued by the customer within the original sale, keep the original roles throughout (Brackenmere seller and accounting supplier) and say so in the note, and record the reading as a finding for the UBL TC write-up. (c) Model the charge as a reduction of the maker's next invoice, which changes the flow.
- Needs decision: yes
- From: broad (High), context (High), parties (High), money (Medium)

### furniture/14#F2 · Medium · The store's cost centre given as the buyer's accounting code
- XPath: `/DebitNote/cbc:AccountingCostCode` = `6120`
- XPath: `/DebitNote/cbc:AccountingCost` = `Garden department`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCostCode` = `6120`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:AccountingCost` = `Garden department`
- Why: UBL defines the header `AccountingCostCode` as "The Buyer's accounting code" and the line element as "The buyer's accounting cost centre for this debit note line". The buyer in this debit note is Brackenmere Furniture; `6120` "Garden department" is the store's own cost centre (the buyer's code in `08-Order.xml:/Order/cbc:AccountingCostCode` = `6120`, when the store was the buyer). Here it is the seller's cost centre in an element for the buyer's. The finding depends on F1 only under its option (b) (store as buyer again); under the preferred option (a) it stands.
- Condition: `AccountingCostCode`/`AccountingCost` carry the cost centre of the buyer of this debit note, or are absent.
- Options: (a, preferred) remove them: the store issuing the document does not know the maker's cost centre, and the story gives none; (b) the maker's cost centre, if the story gives one.
- Needs decision: no
- From: context (Medium), broad (in its F1)

### furniture/14#F3 · Medium · The quotation referred to as a contract
- XPath: `/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`
- Why: `ContractDocumentReference` is "A reference to a contract associated with this document". `BF-DOC-26-0568` is the quotation `02-Quotation.xml`, an offer, and nothing in it covers return transport. The flow names a different contract for the supply relation, the store's own-brand contract (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`); the cancellation uses the quotation number the same way (`11-OrderCancellation.xml:/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`). Logistics rated it Low because an accepted quotation can be the contractual document of a sale; the merge keeps Medium because the reference points to a document of another kind, and the charge arises from the return instruction, not from the quotation.
- Condition: `ContractDocumentReference` refers to a contract of the story under which the transport charge arises, or is absent; the quotation, if referenced, is referenced as an additional document.
- Options: (a, preferred) remove it, since the return instruction (already referenced) is the basis of the charge (broad), or move the quotation to an `AdditionalDocumentReference` (logistics); (b) `BM-OWN-BRAND-2026`, if that agreement provides for return transport charges (context, logistics).
- Needs decision: no
- From: broad (Medium), context (Medium), logistics (Low)

### furniture/14#F4 · Medium · Language code in LocaleCode
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/14#F5 · Low · The credit note's line amount and restocking deduction repeated on the transport line
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cbc:Amount` = `3477.00`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Restocking deduction`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:BillingReference/cac:BillingReferenceLine/cac:AllowanceCharge/cbc:Amount` = `183.00`
- Why: The debit line charges a flat 85.00 per delivery for return transport. Its billing reference repeats the credit note line's amount and its restocking deduction (`BillingReferenceLine/AllowanceCharge`: "An allowance or charge applicable to the transaction line"). The values agree with `13-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cbc:LineExtensionAmount` = `3477.00`, but the debit neither disputes nor reverses the deduction, so the figures play no part here and look copied (section 4.8). The deduction itself is questioned in 13 (its F2).
- Condition: The billing reference line identifies the credit note line without amounts and allowances that do not bear on the debit, or the document says what the store does about the deduction.
- Options: (a, preferred) keep the reference to credit note line 1 (`BillingReferenceLine/ID`) and drop amount and allowance; (b) if the store disputes the deduction, say so (e.g. a discrepancy response) and charge it back.
- Needs decision: no
- From: broad, money, context

### furniture/14#F6 · Low · Payment note calls the debit note an invoice
- XPath: `/DebitNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BS-DOC-26-0580`
- Why: `PaymentNote` is "Free-form text applying to the Payment for the owner of this account". The document is a debit note (`/DebitNote/cbc:DebitNoteTypeCode` = `383`), not an invoice; the same wording occurs in `13-CreditNote.xml`.
- Condition: The payment note names the document as a debit note, or carries only its number.
- Options: (a, preferred) "Debit note BS-DOC-26-0580".
- Needs decision: no
- From: broad, money, context

### furniture/14#F7 · Low · Brightmarket's contact is a sales desk in a billing role
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name ("Buying office"), job title ("Customer service officer") and department ("Sales") do not agree with each other, and none fits Brightmarket's role in a debit note it issues for a transport charge (accounts receivable, or the goods-in that ran the van). The same contact is used in every example where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document (after F1).
- Options: (a, preferred) an accounts contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/14#F8 · Low · Store's master data copied into the debit note
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital come from the store's master data; a transport debit uses none of them (section 4.8, IND5). Carried on Brightmarket in examples 01 to 14.
- Condition: Present only in documents of the flow where they have a business reason.
- Options: (a, preferred) remove them from this document.
- Needs decision: no
- From: parties (web site, social media), context (also logo and share capital)

### furniture/14#F9 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/*/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Line (merge recalculation): 1 service unit (`/DebitNote/cac:DebitNoteLine/cac:Price/cbc:BaseQuantity` = `1`, E48) × 85 = `/DebitNote/cac:DebitNoteLine/cbc:LineExtensionAmount` = `85.00` = `/DebitNote/cac:DebitNoteLine/cbc:TaxInclusiveLineExtensionAmount` = `85.00` (tax 0.00) = `/DebitNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `85.00`; taxable amount 85.00.
- Tax: exempt STT with `SVCB2B` "Service to a business" (world list: "A service supplied to a business is not a retail sale") fits a transport service between two businesses.
- Due date: 2026-05-04 + 30 days = 2026-06-03 = `/DebitNote/cbc:DueDate` = `2026-06-03`, as "30 days net" says.
- Payment: `RF86BSDOC260580` passes ISO 11649 and is built from the store's own number (the store receives the money); account `XB48BLUM38010001570935` passes the IBAN-style check and is the store's account in `13-CreditNote.xml:/CreditNote/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB48BLUM38010001570935`; payment purpose `SCVE` fits a service.
- References: `BF-CN-26-0579` resolves to `13-CreditNote.xml` (line 1, 3477.00, deduction 183.00, as quoted); `BF-DOC-26-0578` to `12-InstructionForReturns.xml`; `BS-PO-26-0574` to `08-Order.xml`, the order under which the returned sets were bought.
- Delivery: `/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02` lies within the requested period of 12 (2026-04-29 to 2026-05-02) and before the credit note (2026-05-03); GLN 9523710900015 passes its check digit and shares the maker's GS1 company prefix with its party GLN 9523710900008.
- Transport: 282 kg in six sets (`12-InstructionForReturns.xml`) fits a delivery van.

## Considered and refuted
- `/DebitNote/cac:LegalMonetaryTotal`: incomplete totals (no tax-exclusive or tax-inclusive amount) — refuted because both are optional, no tax is due and the line carries its tax-inclusive amount (from money).
- `/DebitNote/cac:DebitNoteLine/cbc:PaymentPurposeCode` = `SCVE`: a payment element on a line — refuted because UBL 2.5 defines it on the debit note line (from money).
- `/DebitNote/cac:DebitNoteLine/cbc:Note` = `Collected with the store's van.`: contradiction with 12 ("The maker takes back six sets") about who transports — refuted because "takes back" means the maker accepts the return; the instruction's silence on the carrier is 12's finding (from logistics).
- `/DebitNote/cac:OrderReference/cbc:ID` = `BS-PO-26-0574`: an order reference for a service never ordered — refuted because it is "an Order with which this Debit Note is associated", and the returned goods come from it (from logistics).
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `1` with unit `E48`: odd for transport — refuted because one return delivery is one service unit, as "per delivery" says (from context).
- `/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:Name`: location name contains the company name — refuted because it names Brackenmere's Marrowdale site, identified by its own GLN (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F9 by the merge.
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because name, title and department agree and the desk plausibly handles the relationship (from parties).
- `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name`/`ID` — refuted because the aggregate is the profile; its presence is F8 (from parties).

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F9: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- broad/F1, context/F1, parties/F1, money/F1 → F1: combined; money's Medium raised to High (values in the document contradict each other); the cost-centre part of broad/F1 moved to F2.
- context/F2 → F2: kept Medium, joined by the cost-centre part of broad/F1; dependency on F1 stated.
- broad/F2, context/F3, logistics/F1 → F3: combined at Medium (logistics had Low, its argument stated); options of all three kept.
- broad/F3, parties/F2, context/F4 → F4: removal preferred, as in earlier flows.
- broad/F4, money/F3, context/F5 → F5: combined.
- broad/F5, money/F2, context/F6 → F6: combined.
- broad/F6, parties/F3 → F7: combined; wording fitted to Brightmarket's role in this document.
- parties/F4, context/F7 → F8: grouped.

## Outside this review
- `sea/28-DebitNote.xml` shows the same accounting-role pattern; it belongs to that example's review.
