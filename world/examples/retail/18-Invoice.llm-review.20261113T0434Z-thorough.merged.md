# LLM review: 18-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/18-Invoice.xml`, Git blob `4c83015ab6e72109b8aa59490284886f5aa405ef` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/18#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", `ValueBaseMeasure` "The base quantity to which the value factor applies". Recomputed: 0.82 × 1 EA = 0.82 ≠ 96 kg; 96 / 0.82 = 117.1, no quantity of the bench. The same triple is in 39 XML files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a, preferred) drop factor and base (as road, rail, retail a/b); (b) state the activity so that factor × activity = 96 kg; (c) drop the emission from the invoice (context; see F16).
- Needs decision: no
- From: broad (F1), logistics (F2), context (F2)

### retail/18#F2 · High · The "original" lead time of 5 days contradicts the catalogue's 3, and is the only content of the pricing reference
- XPath: `/Invoice/cac:InvoiceLine/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:LeadTimeMeasure` = `3`
- Why: `PricingReference` is "A reference to pricing and item location information associated with this invoice line" and `OriginalItemLocationQuantity` "An original set of location-specific properties (e.g., price and quantity) associated with this item". The original terms of this sale are those of catalogue line 1 of `LD-CAT-26-0218` (the bench), which the order 08 cites: lead time 3 days. Verified in the merge: no document of the flow changes the bench's lead time (03 and 04 change only the side frame's price and the slat wood, and both are issued after this invoice; `LeadTimeMeasure` occurs in the flow only in 02 and here), and the actual time from order (2026-04-24) to receipt (2026-04-30) is 6 days, so 5 is neither the agreed nor the actual figure. Attempted refutation: "original" could mean another location's terms; no document gives one. Besides, the aggregate carries no price, quantity band or allowance, so as a pricing reference it says nothing about the price billed (money, context: Medium for that reason). The contradiction makes it High.
- Condition: the invoice line's pricing reference is absent, or repeats the catalogue line's original values (lead time 3 days, price 520 per bench) and is used by the invoice.
- Options: (a, preferred) drop `PricingReference`: the billed price equals the catalogue and order price and needs no reference; (b) fill it from the catalogue line (price, minimum/maximum quantity, lead time 3 days).
- Needs decision: no
- From: broad (F3), logistics (F1), money (F1), context (F3)

### retail/18#F3 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 364 occurrences in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F4), parties (F1), context (F4, the LocaleCode half)

### retail/18#F4 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is a vehicle entrance, not a street name. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address; (b) record it in Bayvarra's address format (finding then dismissed).
- Needs decision: no
- From: broad (F5), parties (F2)

### retail/18#F5 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle system boundary from another list (39 XML files, `grep -rl --include='*.xml' 'CRADLETOGATE' world/examples | wc -l`). UBL has no element for the boundary: TC write-up candidate.
- Condition: no system-boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it and record the missing element for the TC write-up.
- Needs decision: no
- From: context (F4, the FullnessIndicationCode half)

### retail/18#F6 · Medium · Lifecycle stage "Manufacturing" for an emission from ore to factory gate
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; the description covers raw material supply, transport and manufacturing (EN 15804 A1–A3, own knowledge), the code only manufacturing. Added by the merge (no part raised it here), aligned with retail a/b and road/rail/air.
- Condition: the code covers the stages the description names, or is absent.
- Options: (a, preferred) omit the code; (b) one emission per stage.
- Needs decision: no
- From: added by the merge

### retail/18#F7 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: on an invoice the supplier's contact answers billing questions and the customer's handles incoming invoices. The order names both accounts contacts (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`, `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:AccountingContact/cbc:Name` = `Accounts payable`); the invoice uses Lumeway's sales customer service and Brightmarket's buying office, whose job title and department contradict its name. The factor's contact is its "Client accounts" (in factoring the client is the seller, Lumeway), while the reader of the payee here is the debtor Brightmarket, whose contact at a factor would be collections (own knowledge of factoring).
- Condition: the accounting parties' contacts are their accounts departments, with consistent name, job title and department; the payee's contact is the one the debtor uses for payment questions.
- Options: (a, preferred) accounts receivable and accounts payable as in the order, and a debtor-facing contact (collections) for Harbourline.
- Needs decision: no
- From: broad (F8), parties (F6, F7, F10)

### retail/18#F8 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Lumeway's customs trader number on a domestic invoice of a flow without customs, the customer's share capital (company law asks for the issuer's, not the customer's), and Brightmarket's consumer web shop and social-media profile play no part in requesting payment (section 4.8). `CorporateStockAmount` is defined as "The number of shares in the capital stock of a corporation" while its data type is an amount: a conflict for the TC write-up (the parties part's "Needs decision: yes" set to no, as retail a/b). Lumeway's own share capital and the logo are not part of this finding (see Refuted in the merge and Considered and refuted).
- Condition: the parties carry only data the invoice uses.
- Options: (a, preferred) leave these out of the invoice.
- Needs decision: no
- From: parties (F4, F5, F8), context (F7, part)

### retail/18#F9 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Invoice/cac:PayeeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: shared by 25 unrelated parties of the world (parties part, lxml), among them Harbourline Factoring; a filler. Every earlier flow kept it as Low with a decision.
- Condition: Harbourline's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) its own date; (b) omit it; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F9)

### retail/18#F10 · Low · Bills 24 benches while referring to the receipt that accepted 23
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `24`
- XPath: `/Invoice/cac:ReceiptDocumentReference/cbc:ID` = `BS-RA-26-0235`
- XPath: `/Invoice/cac:InvoiceLine/cac:ReceiptLineReference/cbc:LineID` = `1`
- XPath: `/Invoice/cbc:IssueTime` = `15:52:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:21:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:RejectedQuantity` = `1`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`
- Why: the invoice, issued 31 minutes after the receipt advice, refers to it at document and line level ("A reference to a Receipt Advice associated with this document"), but bills all 24 despatched benches (24 × 520.00 = 12480.00, less 5 % = 11856.00), while the receipt line accepted 23 and refused one. The broad and context parts called this a contradiction (High): an invoice that rests on a receipt line bills the accepted quantity, and 19-CreditNote would not be needed; under factoring the seller also assigns a receivable of 494.00 it already knows is disputed (money). The merge tried to refute it and partly succeeded: the receipt itself asks for a credit note (`RejectActionCode` `CREDIT`, "credit requested"), so billing the despatched quantity and crediting the refused bench (19, one bench, 494.00) follows the buyer's own request, and `ReceiptLineReference` only says the receipt line is "associated" with the invoice line. Neither reading can be settled from the documents, so the finding stays, as Low with a decision (money and logistics rated it Low/yes as well).
- Condition: either the invoice bills the accepted quantity of the receipt it refers to (23, payable 11362.00) and the credit note is not needed for the bench, or the invoice visibly rests on the despatch (no receipt reference, or a note that the refused bench is credited separately) and the credit note corrects it.
- Options: (a, preferred, keeps the flow's credit note) keep 24, drop the receipt references (or add a note "the refused bench will be credited"); (b) bill 23 and drop or rethink 19-CreditNote.
- Needs decision: yes
- From: broad (F2), context (F1), money (F2), logistics (F3)

### retail/18#F11 · Low · Tax point date eight days after delivery and invoice, with no event behind it
- XPath: `/Invoice/cac:InvoiceLine/cbc:TaxPointDate` = `2026-05-08`
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- Why: `TaxPointDate` is "The date of this invoice line, used to indicate the point at which tax becomes applicable". The goods were delivered and invoiced on 2026-04-30 (also `19-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cac:Delivery/cbc:ActualDeliveryDate` = `2026-04-30`); nothing in the flow happens on 2026-05-08 (the promotion starts on 2026-05-11, payment is due on 2026-05-30). In sales-tax practice the tax point is the sale, delivery or invoice (own knowledge). The sale is exempt, so the date has no effect on the amounts, but it has no business reason as given, unless Bayvarra's rules set it, which the story does not show.
- Condition: the tax point date is the date of the event that fixes the tax point in this world, or is absent.
- Options: (a, preferred) 2026-04-30, or drop it (exempt sale, invoice date = delivery date); (b) keep 2026-05-08 and record the Bayvarran rule in the story.
- Needs decision: yes
- From: broad (F6), money (F3), context (F5)

### retail/18#F12 · Low · Line reference to a document that exists nowhere and does not say what it is
- XPath: `/Invoice/cac:InvoiceLine/cac:DocumentReference/cbc:ID` = `LD-DS-B180`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`
- Why: `LD-DS-B180` occurs only here (`grep -rn --include='*.xml' 'LD-DS-B180' world/examples`, rerun). It looks like a Lumeway data sheet of the bench, next to the manufacturer's data sheet `VI-DS-B180` that every other example uses; without a type the receiver cannot tell what it is or why the invoice line needs it.
- Condition: the reference says what it is and has a reason in the invoice, or is absent.
- Options: (a, preferred) drop it; (b) a document type, and the same reference in the catalogue, if Lumeway has its own data sheet.
- Needs decision: no
- From: broad (F7, part), logistics (F4), context (F6, part)

### retail/18#F13 · Low · Line payment terms repeat the document's terms
- XPath: `/Invoice/cac:InvoiceLine/cac:PaymentTerms/cbc:Note` = `The promotion stock is paid with the invoice, 30 days net.`
- Why: line-level `PaymentTerms` is needed where a line is paid differently from the rest. The invoice has one line, and the header's terms already say 30 days net with due date 2026-05-30 (`/Invoice/cbc:DueDate` = `2026-05-30`); "paid with the invoice" is what any invoice line is. No filler rule.
- Condition: no line payment terms, or terms that differ from the document's.
- Options: (a, preferred) drop them.
- Needs decision: no
- From: broad (F7, part), money (F4), context (F6, part)

### retail/18#F14 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: the GTIN of Valdara's bench is under Lumeway's company prefix 9520610 (Lumeway's GLNs and SSCCs across the world); under GS1 rules the brand owner allocates the GTIN from its own prefix (own knowledge). Check digits correct.
- Condition: Valdara's GTINs and Lumeway's keys are under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a prefix of Valdara's own; (b) state the distributor's allocation in the story.
- Needs decision: yes
- From: parties (F3)

### retail/18#F15 · Low · The world item number has the form and check digit of a GTIN
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: twelve digits with a valid GS1 check digit (7, computed in the merge): it reads as a GTIN-12 with prefix 07, a US/Canada range (own knowledge). Added by the merge, as retail a, rail, road and plastics.
- Condition: the world item number cannot be mistaken for a real GTIN, or its form is recorded as deliberate.
- Options: (a, preferred) a format that is not a valid GTIN; (b) record the choice in the scheme.
- Needs decision: yes
- From: added by the merge

### retail/18#F16 · Low · The item's catalogue data copied into the invoice line
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: an invoice identifies what is billed; emissions, circularity data, load test, dimensions and Urvania's customs tariff code (a domestic Bayvarran sale) are catalogue data the invoice does not use (IND5/IND6).
- Condition: the invoiced item carries its identifiers, its tax category and what the invoice depends on.
- Options: (a, preferred) drop the catalogue data from the item.
- Needs decision: no
- From: broad (F9), context (F7, part)

## Checked and consistent
- Arithmetic (redone): 24 × 520.00 = 12480.00; allowance 0.05 × 12480.00 = 624.00 (promotion support, reason 100); tax exclusive = taxable = tax inclusive = payable = 11856.00; tax 0.00 at 0 %; equal to the order's anticipated total (`08-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11856.00`).
- Penalty: 1.5 % × 11856.00 = 177.84, from 2026-05-31; due date 2026-05-30 = issue + 30 days, as in 02 and 08.
- Factoring: type `393` (UNTDID 1001 "Factored invoice") with Harbourline as payee and the payee account held by Harbourline Factoring Ltd; account `XB51BLUM38020502304038` and RF `RF42LDINV260236` pass `check_ids.py` (rerun).
- References to 08, 12 (despatch line 1, 24 benches) and 17 resolve and precede the invoice; tax `E` "sale for resale", supply type goods, as in 02 and 08; line delivery terms DDP as in 08; price 520 is the catalogue's.
- Harbourline is described identically in 18 and 19.

## Considered and refuted
- `/Invoice/cbc:AccountingCostCode` = `6120`: a copy of master data — refuted, it is the buyer's own code from its order (`08-Order.xml:/Order/cbc:AccountingCostCode` = `6120`) (from money; context checked the same).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`: copied master data — refuted, an invoice may be rendered with the logos of its parties (from parties).
- `/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`: checked against type and account — consistent (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted, the definition fits a business park (from parties).
- `/Invoice/cac:InvoiceLine/cac:DeliveryTerms/cbc:ID`: DDP at line level repeats the order — refuted, the invoice has no header delivery terms, so nothing is repeated (from context).

## Refuted in the merge
### parties/F5 (Lumeway's half) · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- The part's finding (both parties' share capital): UBL defines `CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount and the value is a sum in XBL; a conflict between definition and data type, a candidate for the TC write-up. Condition: share capital no longer in `CorporateStockAmount`, or the use recorded as a finding against the UBL definition and kept on purpose. Options: record it and keep it where a document needs it (invoices). Needs decision: yes.
- Refuted because (for the supplier's own share capital): this is the issuer's invoice, where company law commonly requires the share capital (the parties part's own option keeps it here; the road merge refuted the supplier's own share capital on its invoice for the same reason), and an amount is the only thing an Amount-typed element can hold. The definition conflict stays recorded as a TC write-up note in F8; the customer's share capital is kept as part of F8.

## Changed in the merge
- broad/F3, logistics/F1, money/F1, context/F3 → F2: grouped as High (contradiction with the catalogue); money/context's Medium point (no pricing content) included in Why.
- context/F4 → F3 and F5: split (LocaleCode / FullnessIndicationCode).
- F6 (MANUFACTURING) and F15 (world item number): added by the merge, aligned with retail a/b.
- broad/F8, parties/F6, F7, F10 → F7: one contacts finding per example.
- parties/F4, F5 (customer half), F8, context/F7 (party part) → F8: one copied-master-data finding; parties' "yes" set to no.
- broad/F2 (High), context/F1 (High), money/F2 (Low), logistics/F3 (Low) → F10: Low with "Needs decision: yes", because the receipt's own `RejectActionCode` `CREDIT` supports invoicing on despatch with a later credit; both readings carried.
- broad/F7 → F12 and F13: split (unexplained reference / repeated line terms), grouped with logistics/F4, money/F4 and context/F6.
- broad/F9, context/F7 (item part) → F16: item data separate from party data (as retail a/b).

## Outside this review
- In 12-DespatchAdvice the handling-unit line of pallet 1 and the despatch line share ID 1, and in 17-ReceiptAdvice the pallet-3 receipt line and the receipt line share ID 1 (see their reviews, 17/F13); the invoice's references to despatch line 1 and receipt line 1 are only as clear as those IDs.
