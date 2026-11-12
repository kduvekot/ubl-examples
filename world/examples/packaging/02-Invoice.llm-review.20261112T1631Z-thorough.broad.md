# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/02#F1 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in
  which this address is located"; a province is the "political or administrative division of a
  country" that CountrySubentity is defined for, and the Bayvarran address of the seller uses
  CountrySubentity (`/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`).
  The pattern occurs 219 times in 104 example files (grep -c over `*.xml` for `<cbc:Region>Province of`).
- Condition: no address carries a province in Region; where needed it is in CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it if the Urvanian format does not
  need it.
- Needs decision: no

### packaging/02#F2 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID
  `ISO 639`) is a language code equal to Language/ID and names no locale. 362 occurrences in 213 files
  (grep -c over `*.xml`), always `en`.
- Condition: LocaleCode is absent or holds a locale identifier from a locale list named in listID.
- Options: (a) remove it (preferred); (b) a locale such as `en-XB` from a locale list.
- Needs decision: no

### packaging/02#F3 · Low · Contacts do not fit invoicing roles
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: The accounting customer's contact is the one who receives and pays the invoice (accounts
  payable); Valdara gives its order desk in its Sales department, a seller-side function. The
  accounting supplier's contact for a payment request would normally be accounts receivable, not
  the order desk. The same contact appears for Valdara as buyer in `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`.
- Condition: each accounting party's contact is a function that handles this invoice (accounts
  payable / receivable) with fitting job title and department.
- Options: (a) give both parties an accounts contact (preferred); (b) keep the order desk for the
  supplier but give Valdara an accounts payable or purchasing contact.
- Needs decision: no

### packaging/02#F4 · Low · Export exemption without any delivery information
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521`
- Why: The invoice zero-rates the sale as "Export outside Bayvarra" (category G) but says nothing
  about the delivery that makes it an export: no Delivery (date, place, country), no
  DespatchDocumentReference, no delivery terms. Whether and when the goods left Bayvarra is the fact
  the exemption depends on (own knowledge of export zero-rating practice); only the order says FCA at
  Lumeport for a buyer in Urvania. By IND6 nothing may be implied from absence.
- Condition: the invoice states the delivery the exemption rests on (at least the actual delivery or
  collection date, and the destination country or the place of collection), or references the
  document that does.
- Options: (a) add Delivery with ActualDeliveryDate and the delivery location/country (preferred);
  (b) add a DespatchDocumentReference to a despatch advice or consignment note, if the flow gets one.
- Needs decision: no

### packaging/02#F5 · Low · Buyer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Valdara's warehousing provider and its stock-exchange listing play no role in billing a film
  delivery; they read as master data copied from the party (IND5).
- Condition: both are absent or have a stated use in this invoice.
- Options: (a) remove them (preferred); (b) if Castrano received the goods, state that in Delivery.
- Needs decision: no

### packaging/02#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: 12 digits with a correct GS1 check digit: read by any GS1 system as GTIN-12 with prefix 077
  (GS1 US), a range assigned to real companies (own knowledge). All world item numbers have this
  property (82 occurrences in 64 files, grep over `*.xml`). See `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`.
- Condition: the world item numbers cannot be read as GTINs that may belong to real companies.
- Options: (a) change the format so it is not a valid GTIN (preferred); (b) GS1 GTINs with prefix 952.
- Needs decision: yes

### packaging/02#F7 · Low · Default-looking registration date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is carried by 25 different companies in all three countries (271 occurrences in
  181 files, counted over `*.xml`); it reads as a default, not as Rivermouth's registration date (IND5).
- Condition: the date is Rivermouth's own, or absent.
- Options: (a) a date from the company history (preferred); (b) omit it.
- Needs decision: yes

## Checked and consistent
- Order reference `VI-PO-26-0521` resolves to `01-Order.xml`; parties, item, quantity (480 KGM),
  price (3.1 per KGM) and the amount 1488.00 agree with it.
- Totals: line 1488.00 = LineExtension = TaxExclusive = TaxInclusive = Payable; tax 0.00.
- Dates: issue 2026-05-02 + 30 days = due 2026-06-01 (DueDate, PaymentMeans and PaymentTerms agree);
  penalty period starts 2026-06-02.
- Penalty: 1.5 % × 1488.00 = 22.32 = PenaltyAmount.
- RF reference `RF29RPINV260522` and the payee account pass check_ids.py; the payee account is the
  seller's own (same as Party/FinancialAccount). Credit transfer over the Trade Accord rail with
  shared charges fits a cross-border payment XU → XB.

## Considered and refuted
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
  is tagged `en-XB` here but `en-XU` in `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
  — refuted: in both examples the English rendering carries the issuer's locale (Valdara issues 01,
  Rivermouth 02); the content is the same and both tags are valid.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
  has no Urvanian rendering here, unlike the order — refuted: one rendering in the document's default
  language (`DefaultLanguageCode` en) is sufficient.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
  duplicated with the payee account — refuted: the supplier receives the payment, so its account has a
  use; same account in both places.
- `/Invoice/cbc:AccountingCost` = `Raw materials and parts` for stretch film — refuted: packaging
  consumables are commonly booked with raw materials and supplies.
