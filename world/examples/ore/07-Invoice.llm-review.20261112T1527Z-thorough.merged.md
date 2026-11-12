# LLM review: 07-Invoice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/07-Invoice.xml`, Git blob `0e28c5a596e22d95a0c87b535ac9b772716f3863` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/07#F1 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located" and Address/CountrySubentity as "The territorial
  division of a country, such as a county or state, expressed as text". A province is a territorial
  division of Urvania; Bayvarran addresses put their states in CountrySubentity.
  `<cbc:Region>Province of` occurs 219 times in 104 XML examples (`grep -rl --include='*.xml'` and
  `grep -rh … | wc -l` over `world/examples`, recounted in the merge).
- Condition: the province of every Urvanian address in this example is in `cbc:CountrySubentity`
  and not in `cbc:Region`, or the world states why Region is used on purpose.
- Options: (a, preferred) move the province to CountrySubentity for all Urvanian addresses, as for
  Bayvarra; (b) keep Region and record in the world why.
- Needs decision: yes (it changes the Urvanian address format in every flow and may be deliberate)
- From: broad (F1), parties (F1), context (F1)

### ore/07#F2 · Low · Moisture deduction without a stated basis
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Moisture deduction`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`
- XPath: `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:MultiplierFactorNumeric` = `0.015`
- XPath: `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `8060`
- Why: the line deducts 1.5 % of the value (14 414 504 × 0.015 = 216 217.56 → 216 218) for moisture,
  under reason code 64 "Special agreement". No example of the flow states a moisture content, a
  moisture limit or the agreement: the item carries only
  `/Invoice/cac:InvoiceLine/cac:Item/cac:AdditionalItemProperty/cbc:Name` = `Iron content`; the order
  prices 8 060 XUF per tonne with no wet/dry basis and no moisture clause; and the flow's only assay
  reference (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:AdditionalDocumentReference/cbc:ID`
  = `SM-ASSAY-26-11`) sits in the transport request, is not referenced by the invoice and does not
  exist as an example. The buyer cannot verify the deduction, and "special agreement" points to an
  agreement nobody references. (Ore is commonly settled by converting wet to dry tonnes against a
  measured moisture, own knowledge; a value deduction is a legitimate simplification if its basis
  is stated.)
- Condition: the invoice states the basis of the deduction: the measured moisture (e.g. an
  AdditionalItemProperty or the reason text) and/or a reference to the assay or agreement that fixes
  the 1.5 %; and the order's price basis allows such a deduction.
- Options: (a, preferred) a "Moisture content" item property and an AdditionalDocumentReference (with
  its type) to the assay certificate, keeping the allowance; (b) a fuller reason text naming the
  measured and the contractual moisture and the contract clause, or the wet/dry basis in the order;
  (c) drop the deduction if the story has no moisture agreement.
- Needs decision: no
- From: broad (F5), money (F1), context (F2)

### ore/07#F3 · Low · World item number is a valid GTIN-12 in the real GS1 US range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: twelve digits with a correct GTIN-12 check digit (3, recomputed in the merge); read as GTIN-13
  `0771010000013` it has the prefix 077 of the GS1 US range (own knowledge of the prefix ranges, no
  register lookup). Under the world scheme `urn:ubl-examples:world:item` (64 XML examples, `grep -rl
  --include='*.xml'`, recounted) it can be mistaken for a real GTIN, which the rule on fictional
  values excludes. Whether it is assigned could not be checked. The same number is in `01-Order.xml`.
- Condition: the item number cannot be read as a valid GTIN in a real prefix range, or a recorded
  check against the GS1 register says why it is safe.
- Options: (a, preferred) a number form for the world item scheme that cannot be a GTIN; (b) record
  a GS1 check in the sources.
- Needs decision: yes (the scheme is used world-wide)
- From: broad (F6), logistics (F1)

### ore/07#F4 · Low · The accounting customer's contact is a sales desk
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party". Valdara Industries is the accounting
  customer, whose contact receives and approves the invoice (accounts payable); it gives its own
  sales order desk, the wrong side of the transaction altogether. The contact is copied from master
  data (in 75 XML examples, `grep -rl --include='*.xml' 'order@valdara.example'`, recounted).
- Condition: the accounting customer's contact belongs to accounts payable, or is left out.
- Options: (a, preferred) Valdara's accounts-payable contact; (b) leave the contact out.
- Needs decision: no
- From: broad (F3, customer part), parties (F2), context (F3, customer part); the supplier part is
  under "Refuted in the merge"

### ore/07#F5 · Low · Party master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: the mine's physical location with its road-access conditions and coordinates does nothing in
  an invoice for ore delivered FCA at the siding by rail; Valdara's share listing and its warehousing
  provider Castrano Logistics (which appears in the flow only inside Valdara's party) have no use in
  an ore invoice. Section 4.8 and IND5. The same physical location is in `08-RemittanceAdvice.xml`;
  SecurityListing and Castrano Logistics are in 75 XML examples each (`grep -rl --include='*.xml'`,
  recounted).
- Condition: every aggregate of the parties has a use in this invoice, or the document says why it
  carries it.
- Options: (a, preferred) leave them out (keep at most the location's identifier if the invoice
  needs the place of supply); (b) give them a role in the story and show it in the flow.
- Needs decision: no
- From: broad (F2, F4), parties (F3), context (F4)

## Checked and consistent
- Arithmetic (redone in the merge): 1 788.4 t × 8 060 = 14 414 504 (ItemPriceExtension, BaseAmount);
  × 0.015 = 216 217.56 → 216 218; 14 414 504 − 216 218 = 14 198 286 (line, LineExtension,
  TaxExclusive, Taxable); 20 % = 2 839 657.2 → 2 839 657; total 17 037 943 = TaxInclusive = Payable
  = TaxInclusiveLineExtension. Price-extension tax 20 % of 14 414 504 = 2 882 900.8 → 2 882 901;
  14 414 504 + 2 882 901 = 17 297 405. Settlement discount 2 % of 17 037 943 = 340 758.86 → 340 759.
- Due date 2026-04-10 = 30 days after 11 March, the same in DueDate, PaymentMeans and PaymentTerms;
  settlement period 11–21 March, 10 days as the note says.
- References: OrderReference `VI-PO-26-0304` → `01-Order.xml` (line 1 exists), price 8 060 per tonne
  as ordered; DespatchDocumentReference `SM-DA-26-0308` → `04-DespatchAdvice.xml`; quantity 1 788.4 t
  = despatched quantity = freight quantity in `06-Invoice.xml`.
- Item: descriptions, names, seller's and standard IDs, origin, HS `260111`, CPC `14100`, iron
  content 62 % agree with 01 and 04.
- Issued 2026-03-11 14:59, after the despatch (10 March 15:37); under FCA the goods were delivered at
  hand-over to the carrier, so invoicing before arrival is consistent.
- Payment: payee account `XU420351041700000000104729` (IBAN-style check passes, the seller's, branch
  `03510-41700`) and RF reference `RF73SMINV260312` are the ones `08-RemittanceAdvice.xml` quotes; the
  full payable amount is paid on 9 April, after the discount period and before the due date,
  consistent with no discount taken. Supply type GOODS, category S 20 %, domestic sale.
- Parties described identically in all eight ore examples; roles as in 01 and 04; `check_ids.py`
  passes (ISIN, RF, account).

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: suspected a
  code that does not fit a moisture deduction — refuted because UNTDID 5189 has no moisture or
  quality code, and 64 "Special agreement" covers a contractual price adjustment (own knowledge; the
  missing agreement is F2) (from broad, money, context).
- `/Invoice/cac:InvoiceLine/cac:ItemPriceExtension/cac:TaxTotal/cbc:TaxAmount` = `2882901`: suspected
  contradiction with the line tax 2 839 657 — refuted because the price extension is price ×
  quantity before the line allowance (from broad).
- `/Invoice/cbc:IssueDate` = `2026-03-11`: suspected an invoice before arrival — refuted, FCA delivery
  at the siding on 10 March (from broad).
- `/Invoice/cbc:TaxPointDate` = `2026-03-11` while the goods were handed over on 10 March — refuted as
  a finding: the element is defined as "The date of the Invoice, used to indicate the point at which
  tax becomes applicable"; the world's tax-point rule is outside what the review may consult (from
  money).
- `/Invoice/cbc:AccountingCostCode` = `3100`, equal to the buyer's ISIC code — refuted: Valdara's
  raw-materials cost centre in all 12 XML examples that carry it, right for ore (from money, context).
- English renderings in Italian form (street names, legal forms, `languageID` `en-XU`) — refuted:
  proper names kept in their local form (from parties).
- Telephone numbers `+999` — refuted: E.164 country code 999 is reserved and unassigned (from parties).
- `0990:10427` with schemeID `ISO 6523` — refuted on knowledge of the ICD register, not checked
  against it (from parties).
- Bank identifier `CREVXUFR` — refuted: country part `XU` is user-assigned, so no real BIC has it
  (from parties).
- Valdara Industries (ISIC `3100`, furniture) as buyer of iron ore — refuted because
  `road/01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description`
  = `Mining, steel making, casting, galvanising, sawing and the transport between them.` places steel
  making in Valdara's own production (from parties).
- Serravona Mining's 'Sales office' as accounting supplier contact — refuted: a seller's sales office
  answering questions about its own sales invoice is a legitimate contact (from parties; see also
  "Refuted in the merge").
- `/Invoice/cac:BuyerCustomerParty` and `/Invoice/cac:SellerSupplierParty` repeating the accounting
  parties — refuted: separate roles in UBL (from parties, context).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `260111` in a
  domestic invoice — refuted: also used for national statistics (from context).

## Refuted in the merge
### broad/F3 and context/F3 (supplier part) · Low · Accounting supplier's contact is a sales desk
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- The parts said the accounting supplier's contact should answer questions about the invoice
  (billing, accounts receivable), not a sales customer-service desk (context: "invoices are usually
  queried with billing"). Condition: the supplier's contact belongs to billing, if a contact is given.
- Refuted because: for a sales invoice of a single, large ore sale the seller's sales office, which
  took the order, is a function that can answer questions about the bill; Contact is only "The
  primary contact for this party", and nothing in the role demands accounts receivable. The parties
  part refuted the same candidate. The customer's sales desk (F4) is different: it is on the wrong
  side of the transaction.

## Changed in the merge
- broad/F1, context/F1 (Needs decision: no) + parties/F1 (yes) → F1 Needs decision: yes, because the
  change touches the Urvanian address format in every flow and may be deliberate.
- broad/F2 (physical location) and broad/F4 (service provider) → grouped into F5 with parties/F3 and
  context/F4, as the same problem (master data without use) at several places.
- broad/F3 and context/F3 → F4 narrowed to the accounting customer's contact; the supplier part moved
  to "Refuted in the merge".
- broad/F5, money/F1, context/F2 → F2: combined; options from all three kept.
- broad/F6, logistics/F1 → F3: combined; check digit recomputed.

## Outside this review
- The same item number `771010000013` in `01-Order.xml` and `04-DespatchAdvice.xml` belongs to their
  reviews; the scheme-wide question is F3.
