# LLM review: 22-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/22-Order.xml`, Git blob `99761f3da8d912c9ddd379e499bc58fce3343fa8` (committed)
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

### retail/22#F1 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 362 occurrences in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files; recounted in the merge).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### retail/22#F2 · Low · "Ready from Tuesday", but collection requested from Monday
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- XPath: `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-01`
- XPath: `/Order/cbc:IssueDate` = `2026-05-30`
- Why: the order is placed on Saturday 2026-05-30; the next Tuesday is 2026-06-02, while the requested collection period ("The period requested for delivery") starts on Monday 2026-06-01 (weekdays recomputed in the merge). The buyer requests collection on a day the goods are said not to be ready. The note also reads as the store's message, while the order is the buyer's document (broad, context).
- Condition: the requested period does not start before the day the goods are ready, and the note is a statement the buyer can make (or the shop's, if the story says the shop writes the order).
- Options: (a, preferred) start the period on 2026-06-02; (b) note "from Monday"; (c) a note in the buyer's voice ("I will collect from Tuesday").
- Needs decision: no
- From: broad (F3), logistics (F1), context (F4)

### retail/22#F3 · Low · The retailer's buying office as its contact in a consumer order
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: as the seller to a consumer Brightmarket's contact would be its customer service; the contact is named "Buying office" with the purchasing address buying@brightmarket.example, while job title and department say sales customer service. Name, job title and department contradict each other.
- Condition: the seller's contact fits selling to consumers, with consistent name, job title and department.
- Options: (a, preferred) Brightmarket's customer service as contact.
- Needs decision: no
- From: broad (F4, part), parties (F4)

### retail/22#F4 · Low · The seller's share capital in the consumer's order
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: the order is the buyer's document; nothing in it uses the seller's share capital, and no rule asks the buyer to state it (section 4.8). Unlike Brightmarket's own till receipt (21, where this was refuted), this is not the issuer's business letter. `CorporateStockAmount` is moreover defined as "The number of shares in the capital stock of a corporation" while its data type is an amount: a TC write-up note; the parties part's "Needs decision: yes" set to no, as retail a/b.
- Condition: the seller party in the consumer order carries no share capital.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: parties (F3)

### retail/22#F5 · Low · The buyer's bank account on an order paid by credit card
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:CardTypeCode` = `CREDIT`
- Why: the order is to be paid by credit card; nothing is paid from or to the buyer's current account under it, and a shop does not need a consumer's account number for click and collect. The account (with branch and bank) is copied from the person's master data; it appears the same way on 21-PurchaseReceipt, paid by debit card (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`).
- Condition: the order carries the buyer's financial account only if a payment or refund under the order uses it.
- Options: (a, preferred) drop the person's financial account.
- Needs decision: no
- From: broad (F4, part), money (F2), parties (F2), context (F3)

### retail/22#F6 · Low · The EXW named place as text only, although it has a GLN
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Garden department of the Lumeport store`
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900026`
- Why: for EXW the named place is where the goods are made available; it is the same garden department as the delivery location, which has GLN `9522610900026`, but here it is described only in text.
- Condition: the EXW named place identifies the same location as the delivery location.
- Options: (a, preferred) `DeliveryTerms/DeliveryLocation/ID` `9522610900026`; (b) drop the terms' location (the delivery location already says it).
- Needs decision: no
- From: logistics (F2)

### retail/22#F7 · Low · Full card number and card verification value in the order
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `9902382000715526`
- XPath: `/Order/cac:PaymentMeans/cac:CardAccount/cbc:CV2ID` = `731`
- XPath: `/Order/cbc:Note` = `Click and collect: ready in the garden department from Tuesday; bring the card used for the order.`
- Why: `CardAccount` is the card "that constitutes this means of payment", `CV2ID` "An identifier for the Card Verification Value". The order carries the complete card number and the verification value. Card industry rules forbid storing or forwarding the verification value after authorisation and mask the number in documents (PCI DSS, own knowledge); the purchase receipt of the same customer masks it (`21-PurchaseReceipt.xml:/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:PrimaryAccountNumberID` = `************4417`), and the note asks the customer to bring the card at collection, so the order does not need the code. The number passes the Luhn check (recomputed) and starts with 9 (national assignment under ISO/IEC 7812, own knowledge), so it cannot be mistaken for a real scheme's card. The money part rated this Medium; the merge sets Low because the elements are used according to their definitions and the problem is implausible practice (section 6, Low), as broad and context rated it. "Needs decision: yes" (context): `CV2ID` occurs in this example only (`grep -rl --include='*.xml' CV2ID world/examples`), so dropping it removes the element from the world's coverage, which `CLAUDE.md` tracks (5153/5160, the uncovered ones listed on purpose); the rule "no fillers, even if coverage drops" decides it, but the owner confirms the coverage change.
- Condition: the order carries no card verification value, and the card number only masked (or tokenised), unless the story gives the order a role in the card authorisation.
- Options: (a, preferred) mask the PAN and drop `CV2ID`; (b) no card account, only the payment means code, since payment happens at collection; (c) cover `CV2ID` in a document whose purpose is the authorisation itself, if the world has one.
- Needs decision: yes
- From: broad (F2), money (F1), context (F2)

## Checked and consistent
- Arithmetic (redone): 1 SET × 899.00 = 899.00; tax 6.5 % × 899.00 = 58.435 → 58.44 (S, STT); payable 957.44.
- Standard rate 6.5 % for a consumer sale, as in 21; the bench set is not a promoted item, and the order (2026-05-30) is after the promotion (to 2026-05-24).
- Card: payment means 54 "Credit card" matches card type CREDIT; validity 2025-03-01 to 2029-02-28 covers the order date.
- Item `BM-551004` "Garden bench set Marrow", GTIN `9523710000012` (Brackenmere's own prefix), manufacturer ID `BF-GS-01`: the complementary item offered in 02 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:ComplementaryRelatedItem/cbc:ID` = `BM-551004`) and the store's article of the furniture flow; HS 940169 and CPC 38112 fit a wooden frame.
- Delivery location GLN `9522610900026` is the garden department of the Lumeport store (as in furniture/06), distinct from the goods-in GLN of 08; EXW at the store fits click and collect (own knowledge of Incoterms 2020).
- Robin Ashdale, his address (LUM-ADR-934215) and the delivery party agree with 21; GS1 keys, account and card number pass their check digits (`check_ids.py` rerun; Luhn recomputed).

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `EXW`: an Incoterm in a consumer sale — refuted, EXW at the store states that the buyer collects, and Incoterms may be used for domestic sales (from broad and context).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:SocialMediaProfile`, `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalWebSite`, `/Order/cac:SellerSupplierParty/cac:Party/cbc:LogoReferenceID`: copied master data — refuted, a shop's order confirmation carries its logo, online shop and social media for the customer (from parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Robin Ashdale`: too thin a delivery party — refuted, the buyer collects himself and is described in full as buyer (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`: against "The store's own garden bench set." — refuted, the Marrow set is Brackenmere's brand in all examples that carry it, and "the store's own" reads as the store's own range (from parties).
- `/Order/cbc:ID`: an order number `RA-PO-…` assigned by a consumer — refuted, a web shop numbers the orders it sends on the buyer's behalf, and the prefix is the buyer's initials (from context).

## Changed in the merge
- broad/F4 → F3 and F5: split (seller contact / buyer bank account), grouped with parties/F4 and with money/F2, parties/F2, context/F3.
- parties/F3 → F4: "Needs decision: yes" set to no (definition conflict as TC note, aligned with retail a/b); kept as a finding because the order is not the seller's own document (contrast 21, where the same value was refuted).
- money/F1 (Medium), broad/F2 (Low/no), context/F2 (Low/yes) → F7: Low with "Needs decision: yes" (coverage of `CV2ID`).
- context/F1 option order: drop preferred.
