# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
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

### packaging/01#F1 · Medium · Province held in Region
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in
  which this address is located". A province is "the political or administrative division of a
  country", which is what Address/CountrySubentity (and CountrySubentityCode) is defined for; the
  Bayvarran addresses of the same document use CountrySubentity for their state
  (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`).
  The same pattern (`<cbc:Region>Province of …`) occurs 219 times in 104 example files (grep -c over
  `*.xml`).
- Condition: no address in the example carries a province in Region; the province, where needed,
  is in CountrySubentity (optionally with CountrySubentityCode and its listID).
- Options: (a) move the value to CountrySubentity, with a code from an Urvanian subdivision list if
  one exists (preferred: the definition names exactly this case); (b) drop it if the Urvanian address
  format does not need the province.
- Needs decision: no

### packaging/01#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". `en`
  with listID `ISO 639` is a language code, identical to Language/ID next to it, and names no locale
  (a locale is language plus region, as in the `en-XU`/`en-XB` languageID values used in this world).
  The same value occurs 362 times in 213 example files (grep -c over `*.xml` for
  `<cbc:LocaleCode listID="ISO 639">`, always `en`).
- Condition: LocaleCode is absent, or holds a locale identifier from a list that defines locales,
  with that list as listID.
- Options: (a) remove it (preferred: Language/ID already says English and nothing in the order
  depends on a locale); (b) use a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### packaging/01#F3 · Low · Buyer's contact is a sales customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact on an order is the person or desk that buys and answers questions about
  the order. Valdara's contact is a customer service officer in its Sales department, i.e. the
  contact a seller would give; the seller Rivermouth uses the identical triple
  (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`). Over all examples
  the triple ('Order desk', 'Customer service officer', 'Sales') occurs in 89 contacts (counted with
  lxml over `*.xml`), for buyers and sellers alike.
- Condition: the buyer's contact names a buying or procurement function whose job title and
  department fit it.
- Options: (a) give Valdara a purchasing contact (e.g. procurement desk, procurement officer,
  Procurement), as other buyers in the world have (preferred); (b) keep one contact but change job
  title and department to a neutral function.
- Needs decision: no

### packaging/01#F4 · Low · Master data the order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: An order requests goods; it neither pays nor receives payment, so the seller's bank account
  has no use in it (payment instructions come with the invoice, `02-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`).
  Valdara's warehousing provider Castrano Logistics plays no role in this FCA order (the goods are
  collected by Trasvia at Rivermouth's dispatch, and no delivery to Castrano is stated); Valdara's
  stock-exchange listing and Trasvia's haulage licence are not used by the order either. They read
  as party master data copied into the document (rule "no fillers", IND5).
- Condition: every one of these aggregates is either absent or has a stated purpose in this order.
- Options: (a) remove them (preferred); (b) if Castrano is where the film is to be delivered, say so
  through Delivery (DeliveryParty/DeliveryLocation) instead of ServiceProviderParty.
- Needs decision: no

### packaging/01#F5 · Low · No requested pick-up or delivery time
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FCA`
- Why: Under FCA the buyer's carrier collects the goods at the seller's premises, so the seller needs
  to know when to have the 480 kg ready. The order names the carrier but has no
  Delivery/RequestedDeliveryPeriod, Despatch/RequestedDespatchPeriod or similar date; by IND6 nothing
  can be implied from its absence.
- Condition: the order states when the goods are to be ready for collection (or delivered), or the
  story states why no date is needed.
- Options: (a) add a requested despatch (pick-up) period under Delivery/Despatch (preferred, it fits
  FCA); (b) a requested delivery period.
- Needs decision: no

### packaging/01#F6 · Low · Item number in the world scheme is a valid UPC-A in the GS1 US range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: The value has 12 digits with a correct GS1 mod-10 check digit, so any GS1 system reads it as
  the UPC-A / GTIN-12 00772040000103, whose prefix 077 belongs to GS1 US; such numbers are assigned to
  real companies (own knowledge, not verified against GEPIR). All eight values of scheme
  `urn:ubl-examples:world:item` in the examples have valid GTIN-12 check digits (82 occurrences in
  64 files, grep over `*.xml`; check digits computed in this review), while the world's real GS1
  numbers use prefix 952 (reserved by GS1 for examples). The rule "fictional values must not be
  mistaken for real ones" applies.
- Condition: the world item numbers cannot be read as GTINs that may be assigned to real
  companies (e.g. a non-GTIN length or check digit, or a GS1 prefix reserved for examples).
- Options: (a) change the world item number format so it is not a valid GTIN-12 (preferred: keeps
  the scheme visibly fictional); (b) use GTINs with prefix 952 and schemeID `GS1 GTIN` if the items
  are meant to be GS1-identified.
- Needs decision: yes (could not settle whether the specific numbers are assigned; the change touches
  the world's item scheme)

### packaging/01#F7 · Low · Same registration date for unrelated companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Rivermouth Packaging (Bayvarra)
  and Trasvia Haulage (Urvania) were both registered on New Year's Day 1996, in two different
  national registers; over all examples 25 different companies in all three countries carry
  `1996-01-01` (271 occurrences in 181 files, counted over `*.xml`), while the other dates in use
  (e.g. Valdara's `1962-04-12`) look individual. A default date is a filler (IND5).
- Condition: each company's registration date is its own date from the world's company history, or
  the element is absent where no date is known.
- Options: (a) give each company a date from its history (preferred); (b) omit RegistrationDate where
  the history has none.
- Needs decision: yes (company histories)

## Checked and consistent
- Arithmetic: 480 KGM × 3.1 XBL per 1 KGM = 1488.00 = line, LineExtensionAmount and PayableAmount;
  tax 0 % on 1488.00 = 0.00.
- 480 kg of film on 16 kg rolls = 30 rolls; thickness 23 µm agrees with the seller's item ID
  `RP-SF-23`.
- Tax: seller in Coastal State, Bayvarra (state sales tax STT), buyer in Urvania; category G with
  exemption reason EXP "Export outside Bayvarra" fits a sale collected FCA for carriage to Urvania.
- Item, price and tax agree with `02-Invoice.xml` (same quantity, price, codes, item IDs).
- check_ids.py: ISIN `XU0001042501` and account `XB96BLUM38020504712805` pass.
- HS 392010 and CPC 36330 fit stretch film of polyethylene.

## Considered and refuted
- `/Order/cbc:AccountingCostCode` = `3100`: same digits as Valdara's ISIC code 3100 — refuted:
  coincidence of an internal account number; "Raw materials and parts" plausibly covers packaging
  material for a furniture maker, and the same code and text recur in orders and invoices of other flows (ore, wood, rail, utilities, waste).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`:
  Italian-looking text tagged `en-XU` — refuted: the world renders Urvanian names in an Italianate
  exonym form for English; it is the name used in English, not a translation.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`:
  definition says "number of shares" but the value is an amount — refuted: the element is an Amount
  type in UBL; the definition text is UBL's own inconsistency.
- `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.00`: tax total in an order — refuted: an anticipated tax
  is legitimate in an Order and agrees with the invoice.

## Outside this review
- Whether Trasvia's road leg from Lumeport to Ferrano exists on the map and fits the dates (cross-flow
  logistics).
