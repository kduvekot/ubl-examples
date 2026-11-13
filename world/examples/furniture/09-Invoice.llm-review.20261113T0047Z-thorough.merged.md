# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/09-Invoice.xml`, Git blob `ee49a007b8043177d29c63f3b1b0c8223f117844` (committed)
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

### furniture/09#F1 · High · Delivery note reference to a document that exists nowhere in the world
- XPath: `/Invoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `BF-DN-26-0320`
- Why: `DeliveryNoteDocumentReference` is "A reference to a Delivery Note associated with this document". No example of any flow has this ID (merge: `grep -rl --include='*.xml' 'BF-DN-' world/examples` finds only this invoice), and the furniture flow has no Despatch Advice or Receipt Advice, the UBL documents that play the delivery note's part. The serial 0320 is also far below the seller's running numbers in this flow (BF-DOC/INV/CN 0568 to 0583, which share one counter); other BF series (BF-SIG, BF-CHECK, BF-PHOTO) have serials of their own, so the numbering alone is weak evidence, but the reference does not resolve. The invoice is the only trace of the delivery of the 20 sets: when they left Marrowdale, when they arrived at goods-in and that they arrived complete cannot be checked anywhere, although the flow later depends on that stock (sales in `06-ProductActivity.xml`, return of 6 sets in `12-InstructionForReturns.xml`).
- Condition: The delivery note reference resolves to a despatch document of the flow, or is described as a delivery note outside the exchange (with its type and date), or is absent.
- Options: (a, preferred) add a Despatch Advice for the 20 sets and 20 care kits to the flow and reference its ID (in the flow's numbering), because the later documents rely on the delivered stock; (b) describe the reference (`DocumentTypeCode`, `IssueDate`) as a paper delivery note; (c) remove the reference.
- Needs decision: yes
- From: broad (High), logistics (Medium)

### furniture/09#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. The value `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. The same value occurs 362 times in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, and `grep -rl` with the same pattern for the files).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`: nothing in the flow depends on a regional variant of English, and it needs no new list; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/09#F3 · Low · Free care kits exempted as a sale for resale
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:Note` = `Wood oil and a cloth, for the store to hand to its customers.`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Sale for resale or manufacture`
- Why: `TaxExemptionReasonCode` is "The reason for tax being exempted, expressed as a code". The world's list defines RESALE as "The buyer resells the goods or uses them in its products and charges the tax on its own retail sale". Line 2 invoices 20 care kits free of charge, which the store is to hand to its customers; they are not resold and no retail sale of them is taxed. In sales tax practice (own knowledge) a free gift is either outside the scope or a taxable deemed supply, and a resale exemption rarely covers promotional goods the retailer gives away; it could however be read as part of the store's retail sale of the bench set. The amount is 0.00 either way, so the totals are not affected. The kits are also not in `08-Order.xml` (see "Considered and refuted").
- Condition: The tax category and exemption reason of line 2 describe the treatment of goods given free of charge (or handed on with resold goods) under Bayvarra's state sales tax, consistently with the line note.
- Options: (a, preferred) decide in the world whether free goods handed on with resold goods count as resale; if yes, say so in the reason text (e.g. "supplied with goods for resale"); (b) if not, a world code for supplies without consideration (out of scope); (c) drop the note's statement if the kits are in fact resold.
- Needs decision: yes
- From: broad, money

### furniture/09#F4 · Low · Own-line item carries the maker's brand
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description says the set is made for the department store's own line, and the quotation adds the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`). `BrandName` ("A brand name of this item") names the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand point in different directions unless the story means a co-branded or exclusive maker-branded line, which is why this needs a decision. The same brand is on the item in 12 furniture examples (context's count).
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line or label.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes
- From: broad, context

### furniture/09#F5 · Low · Brightmarket's contact is a sales desk in an accounting-customer role
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact's name "Buying office", its job title "Customer service officer" and its department "Sales" (the department serving the store's own customers) do not agree with each other, and none of them fits the accounting customer of an invoice, whose contact would be accounts payable. The same contact is used in every example of the flow where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) an accounts-payable contact in billing documents (and a buyer in purchasing for the buying documents); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/09#F6 · Low · Store's master data copied into the invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: The store's logo, online-shop website ("An additional web site associated with this party"), photo-sharing profile ("A social media profile associated with this party") and share capital come from its master data; nothing in an invoice to the store about own-line garden furniture uses them (section 4.8, IND5). They are carried on Brightmarket in examples 01 to 14.
- Condition: These elements are present only in documents of the flow where they have a business reason, or nowhere in this flow.
- Options: (a, preferred) remove them from this document; (b) give the flow a reason (e.g. online-shop sales reported separately) and keep them only there.
- Needs decision: no
- From: parties (web site, social media), context (also logo and share capital)

### furniture/09#F7 · Low · Invoice for goods without the delivery date or place
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `20`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `20`
- Why: The invoice bills delivered goods but has no `Delivery` (no `ActualDeliveryDate`, no delivery location) and no invoice period, so neither the date of supply nor the place of delivery is stated. The order `08-Order.xml` has no delivery date either, and the delivery note does not resolve (F1), so the flow nowhere says when the stock that `06-ProductActivity.xml` starts counting on 2026-03-23 arrived. Low, not Medium: an invoice can be issued without a delivery date where the tax point is the invoice date.
- Condition: The invoice states the actual delivery date of the goods, preferably with the goods-in location 9522610900019, or refers to a despatch document that does (F1).
- Options: (a, preferred) add `Delivery/ActualDeliveryDate` (between the order of 2026-03-16 and the invoice of 2026-03-22) and the delivery location; (b) rely on a Despatch Advice added under F1.
- Needs decision: no
- From: logistics

### furniture/09#F8 · Low · Supply type given for line 1 but not for line 2
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory`
- Why: Both lines are goods under the same exempt STT category, but only line 1 states the supply type; a reader of line 2 cannot tell whether the omission means something (IND6). In `17-Invoice.xml` every line carries `SupplyTypeCode`.
- Condition: Both lines state their supply type, or neither does, unless a reason for the difference is given.
- Options: (a, preferred) add `SupplyTypeCode` GOODS to line 2; (b) remove it from line 1.
- Needs decision: no
- From: money

### furniture/09#F9 · Low · Sub-line prices and the free line's price without base quantity
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[2]/cac:Price/cbc:PriceAmount` = `115`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `0`
- Why: `BaseQuantity` is "The quantity at which this price applies". Line 1 states it (`/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:BaseQuantity` = `1`, SET); the sub-line prices and the price of line 2 do not, so the unit they apply to is implied by absence (IND6). Merge recount (lxml over `world/examples/*/*.xml`): 12 of 117 `Price` elements with a `PriceAmount` lack `BaseQuantity`, 3 each in furniture 08, 09 and 10, 1 in furniture 16, utilities 12 and sea 28.
- Condition: Every `Price` in the invoice states the quantity it applies to, or the convention that a missing base quantity means one unit is recorded as a decision.
- Options: (a, preferred) add `BaseQuantity` 1 EA to the three prices; (b) record the convention.
- Needs decision: no
- From: money

## Checked and consistent
- Lines (merge recalculation): 20 sets × 610 = 12200.00; sub-lines 20 × 380 = 7600.00 and 40 × 115 = 4600.00, sum 12200.00; line 2 free of charge, 20 × 0 = 0.00. Only the parent lines enter `LegalMonetaryTotal/LineExtensionAmount` (12200.00 + 0.00).
- Totals: `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `12200.00` = tax exclusive = tax inclusive (tax 0.00, exempt) = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `12200.00`; `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00` covers both lines.
- Against the order: price, quantity, sub-lines, item identifiers and tax treatment equal `08-Order.xml` (`08-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `12200.00`); `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0574` resolves to it.
- Due date: 2026-03-22 + 30 days = 2026-04-21 = `/Invoice/cbc:DueDate` = `2026-04-21` = `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-21`, as the note "30 days net" says.
- Penalty (merge recalculation): 1.5 % × 12200.00 = 183.00 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `183.00`, for one month (`/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`) starting the day after the due date (`/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-22`).
- Payment reference `RF74BFINV260575` passes ISO 11649, is built from the invoice number and repeated in the instruction note; account `XB42BLUM38712004503347` passes the IBAN-style check, contains branch 387120 and bank code BLUM of `BLUMXBLX`, is held in the seller's name and is the same account in `17-Invoice.xml` (`17-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB42BLUM38712004503347`).
- `AccountingCost`/`AccountingCostCode` (6120, Garden department) are the buyer's cost centre from the order and fit garden furniture.
- Parties: Brackenmere, Brightmarket and the short buyer/seller references are described identically across the flow (parties' hash comparison); identifiers, tax prefixes (UL-, CO-) and endpoints agree; GLNs and GTIN have valid check digits.
- `13-CreditNote.xml` references this invoice with the right issue date and credits 6 of the 20 sets at 610.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[2]/cbc:FreeOfChargeIndicator` = `true`: suspected that a line not in `08-Order.xml` is billed — refuted because it is free of charge (0.00), adds nothing to the amount payable, and a seller may add free goods to a delivery (from money, logistics).
- `/Invoice/cac:InvoiceLine[2]/cac:Item`: suspected an item without any identifier — refuted because a free give-away that is not stocked or resold by item number needs none for this invoice (from logistics).
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`: suspected a monthly rate in an element defined per payment — refuted because `PenaltyPeriod` (one month) and the terms note state the period, and the penalty amount matches (from money).
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF74BFINV260575`: suspected a filler repeating `PaymentID` — refuted because the instruction to quote the reference is a real payment instruction the identifier alone does not give (from context).
- `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[1]`: priced sub-lines suspected to double the amounts — refuted because only the parent lines enter the totals (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge); the same holds for every 952… key (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because country code 999 is spare in ITU-T E.164, and the domains are under the reserved .example (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: 1996-01-01 looks like a placeholder — refuted because nothing says the register is closed that day and no other value depends on it (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact as accounting supplier — refuted because a small enterprise's trade-sales desk plausibly handles the whole customer relationship, and name, title and department agree (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: a state-level address register for Brackenmere and a city register for the Lumeport parties — refuted because the rule is "address registers by country level", and Bayvarra keeps them per state or city (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name` and `ID` rather than the platform — refuted because the aggregate is the profile; its presence is F6 (from parties).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID`: the Marrowdale branch could contradict the account — refuted because the account number contains branch 387120 and the account name is Brackenmere's registration name (from parties).

## Changed in the merge
- logistics/F1 → F1: severity Medium → High, as broad/F1, because section 6 names a referenced document that does not exist as High; options of both parts combined; the numbering argument qualified (other BF series have their own serials).
- broad/F2, parties/F1, context/F1 → F2: options ordered with removal preferred (broad preferred en-XB), as parties, context and all earlier flows' merges; count recounted.
- broad/F3, money/F1 → F3: combined; the world list's definition of RESALE added; options of both kept.
- broad/F5, parties/F2 → F5: combined; title and preferred option fitted to the accounting-customer role of this document.
- parties/F3, context/F3 → F6: grouped into one finding (same problem: copied master data of the same party).
- logistics/F2 → F7: wording extended to the delivery place; reason for Low stated.
- money/F3 → F9: count verified and broken down per file.

## Outside this review
- When the 20 sets reached the store (needed for the stock and sales story of 06, 10, 11) is a timeline question across documents; see F1 and F7 for what this invoice lacks.
