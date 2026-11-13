# LLM review: 12-InstructionForReturns.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/12-InstructionForReturns.xml`, Git blob `5e0dc8288b904ffb502e97310af81193916c603c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### furniture/12#F1 · Medium · The return instruction does not say where the goods are to go
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-29`
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-02`
- XPath: `/InstructionForReturns/cbc:Note` = `The maker takes back six sets to free the store's shelf.`
- Why: An Instruction for Returns is "A document used to initiate a return of goods". The shipment's delivery has a requested period but no `DeliveryLocation`, `DeliveryAddress` or `DeliveryParty`, and no despatch (pick-up) place is given either, so the store is not told where to bring the six sets (or where the maker collects them). The place appears only afterwards, in the store's debit note for the transport (`14-DebitNote.xml:/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9523710900015`, `14-DebitNote.xml:/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Brackenmere Furniture, Marrowdale`), a GLN that occurs in no other example (merge: `grep -rn --include='*.xml' 9523710900015 world/examples/furniture` finds only 14); it is not Brackenmere's postal address in this document, and nothing may be implied by absence. The document's purpose depends on the destination (section 6, Medium).
- Condition: The instruction states the delivery location of the return (Brackenmere, Marrowdale, GLN 9523710900015, as in `14-DebitNote.xml`), or, if the maker collects, the pick-up place at the store.
- Options: (a, preferred) `Shipment/Delivery/DeliveryLocation` with GLN 9523710900015 and the name "Brackenmere Furniture, Marrowdale", matching the debit note; (b) a `DeliveryAddress` with Brackenmere's Marrowdale address.
- Needs decision: no
- From: logistics (Medium), parties (Medium), broad (Low), context (Low, with F8)

### furniture/12#F2 · Medium · Language code in LocaleCode
- XPath: `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/12#F3 · Low · Who carries the return, and at whose cost, is not instructed
- XPath: `/InstructionForReturns/cbc:Note` = `The maker takes back six sets to free the store's shelf.`
- XPath: `14-DebitNote.xml:/DebitNote/cac:DebitNoteLine/cbc:Note` = `Collected with the store's van.`
- XPath: `14-DebitNote.xml:/DebitNote/cbc:Note` = `The furniture maker asked for the sets back; the store charges the transport.`
- Why: The note "The maker takes back six sets" can be read as the maker collecting them; the debit note `14-DebitNote.xml` later charges the maker 85.00 for the store's own transport to Marrowdale. The arrangement the debit note relies on (the store transports at the maker's cost) appears nowhere in the instruction that initiated the return, and the instruction names no carrier.
- Condition: The instruction states who carries the goods and, if the story keeps the debit note, that the store transports them at the maker's cost.
- Options: (a, preferred) a note (or a carrier party) saying the store delivers with its own van at the maker's cost, so the debit note follows from this document; (b) let the maker collect and drop the transport debit note, which changes the flow.
- Needs decision: yes
- From: context (part of its F2), logistics (remark in its F1)

### furniture/12#F4 · Low · Manufacturer stated twice, identical to the seller
- XPath: `/InstructionForReturns/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: The header `ManufacturerParty` ("The Party that manufactures the goods to which this Instruction for Return applies") and the line `ManufacturerParty` ("The Party who manufactures the Goods being returned") name the same party for the same goods, and it is also the seller. With one line and one maker the line repetition adds nothing (IND5).
- Condition: The manufacturer is stated once (header), or at line level only where lines have different manufacturers.
- Options: (a, preferred) keep the header party, remove the line one (the document definition speaks of the producer requesting the return); (b) keep the line one only.
- Needs decision: no
- From: broad, parties, context

### furniture/12#F5 · Low · Own-line item carries the maker's brand
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description says the set is the store's own line, and the quotation adds the store's own label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` ("A brand name of this item") names the maker. Text and brand disagree unless the story means a co-branded or exclusive maker-branded line.
- Condition: The item's brand and its description of the line agree.
- Options: (a, preferred) a Brightmarket own-line brand in `BrandName`; (b) reword as an exclusive Brackenmere line made for the store.
- Needs decision: yes
- From: broad, context

### furniture/12#F6 · Low · Brightmarket's contact is a sales desk in the retailer role
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name ("Buying office"), job title ("Customer service officer") and department ("Sales", the department serving the store's own customers) do not agree with each other, and none is the contact a supplier needs for a return of stock (purchasing or goods-in). The same contact is used in every example where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer or goods-in contact (e.g. job title "Buyer", department "Purchasing"); (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/12#F7 · Low · Parties' master data copied into the instruction
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo, online-shop website, social-media profile and share capital, and both parties' state sales-tax registrations, come from master data. A return instruction carries no amounts, no tax treatment and no payment, so none of them is used here (section 4.8, IND5).
- Condition: The document carries these elements only where it has a reason to.
- Options: (a, preferred) remove them from this document, keeping identification, name, address and contact; (b) keep them with a stated reason (none is apparent).
- Needs decision: no
- From: parties (web site, social media; tax registrations and share capital), context (logo, web site, social media, share capital)

### furniture/12#F8 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files), while Brightmarket has its own date (`/*/cac:RetailerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Physics (merge recalculation): `/InstructionForReturns/cac:Shipment/cbc:GrossWeightMeasure` = `282` kg for 6 sets = 47 kg per set of one 1400 mm hardwood bench and two chairs in cartons. Own estimates (not in the flow; no other furniture example states a weight): bench 25 to 30 kg, chair 8 to 10 kg, cartons 1 to 2 kg per piece, i.e. 44 to 56 kg per set. Plausible. Gross weight ("goods plus packaging plus transport equipment") fits sets in original cartons without further equipment.
- Stock (merge recalculation): 20 delivered (`09-Invoice.xml`) − 3 sold to 2026-04-20 (`06-ProductActivity.xml`) = at most 17 on hand; returning 6 leaves at most 11, close to the target of 10 in `04-TradeItemLocationProfile.xml`, which fits "to free the store's shelf".
- Quantity 6 sets agrees with `13-CreditNote.xml` (6 sets credited) and `14-DebitNote.xml` ("six unsold garden sets"); the actual delivery there (2026-05-02) lies within the requested period 2026-04-29 to 2026-05-02; the issue date 2026-04-27 precedes the period.
- `/InstructionForReturns/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0573` resolves to `07-ExceptionNotification.xml`, the exception that led to the return; the purpose fits the UBL definition ("The producer is requesting the return of products that are not selling well … to free up rack or shelf space").
- Parties described identically across the flow; GLNs and GTIN pass their check digits.

## Considered and refuted
- `/InstructionForReturns/cac:DocumentReference/cbc:ID`: no reference to the order or invoice of the returned goods — refuted, the instruction needs item and quantity, and the credit note links the return to invoice 09 (from broad).
- `/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Note` = `In their original cartons.`: suspected filler — refuted because packing instructions are a real part of a return instruction (from context); missing package counts for the cartons — refuted because the gross weight is given and no other value depends on the count (from logistics).
- `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F8 by the merge.
- `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because it fits the seller and name, title and department agree (from parties).
- `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name`/`ID` — refuted because the aggregate is the profile; its presence is F7 (from parties).
- `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the store as retailer rather than buyer — refuted because the retailer role is mandatory and Brightmarket holds the unsold stock (from parties).

## Refuted in the merge
### broad/F3 · Low · Return shipment numbered with the store's prefix
- XPath: `/InstructionForReturns/cac:Shipment/cbc:ID` = `BM-RET-26-0427`
- XPath: `/InstructionForReturns/cbc:ID` = `BF-DOC-26-0578`
- Why (broad): The instruction is issued by Brackenmere (`BF-` numbers, signature `BF-SIG-26-0427`), but the shipment ID uses Brightmarket's prefix `BM-`; the issuer would not normally assign the store's shipment numbers before the store has arranged the transport.
- Condition (broad): The shipment ID is one the issuer can assign (a Brackenmere return number), or the document explains that the store gave it.
- Refuted because: the store carries the goods with its own van (`14-DebitNote.xml`, "Collected with the store's van."), so the shipment is the store's and a store number is the natural shipment identifier; the maker can quote it once the return was agreed after the exception notification of 2026-04-21 (logistics refuted it on the same ground). The serial 0427 being the instruction's date does not make it the maker's number. What the instruction lacks about the carrier is F3.

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F8: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- logistics/F1, parties/F1, broad/F2, context/F2 → F1 (Medium) and F3 (Low): the missing destination (all four parts) kept as Medium, because the document's purpose depends on it (broad and context had Low); the carrier and cost arrangement (context's F2, a remark in logistics/F1) split off as F3 with context's "Needs decision: yes", because its option (b) removes a document from the flow.
- broad/F1, parties/F2, context/F1 → F2: removal preferred, as in earlier flows.
- broad/F4, parties/F3, context/F3 → F4: combined.
- broad/F6, parties/F4 → F6: combined; wording fitted to the retailer role.
- parties/F5, parties/F6, context/F5 → F7: grouped into one finding of copied master data.
- broad/F3 → Refuted in the merge (see above).
