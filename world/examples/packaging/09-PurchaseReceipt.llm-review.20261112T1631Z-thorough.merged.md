# LLM review: 09-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/09-PurchaseReceipt.xml`, Git blob `8c680565e9cab9b2d106e8f8d8cf3831c5abddd0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 1d81251 2026-11-12 Reviews of the packaging flow, run 20261112T1631Z-thorough: parts written so far
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

### packaging/09#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language already in `Language/ID` and names no locale. The same
  value occurs 362 times in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`,
  re-counted in the merge); the Lisavan customer of this receipt has none.
- Condition: `LocaleCode` is absent or holds a locale (language and region) from a locale list named
  in `listID`.
- Options: (a) remove it (preferred by broad and context, and here: it needs no new code list);
  (b) a real locale such as `en-XB` from a locale list (preferred by parties).
- Needs decision: no
- From: broad F1, context F1, parties F1

### packaging/09#F2 · Low · The contacts do not fit a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- Why: `Party/Contact` is "The primary contact for this party". On a receipt Brightmarket's contact
  should be customer-facing, but it is its buying office (`buying@brightmarket.example`), and the
  point-of-sale contact ("The contact person at the point of sale where this purchase took place")
  has the buying office's number, not the store's or the clothing floor's. Velumi Trading's contact
  is named `Purchasing`, which fits a business that buys, but has a sales job title and department,
  so name and department contradict each other; a till purchase needs no customer contact at all.
  The ('Purchasing', 'Customer service officer', 'Sales') combination occurs in 52 contacts (parties,
  lxml count over `*.xml`). Same store contacts as in `08-PurchaseReceipt.xml` (F2 there).
- Condition: Brightmarket's contacts on the receipt are customer-facing contacts of the store, with
  the store's or floor's own number at the point of sale; Velumi's contact, if present, has a name,
  job title and department that agree.
- Options: (a) preferred: a store customer service contact and the floor's own number, as in the fix
  of `08-PurchaseReceipt.xml`; a purchasing title and department for Velumi, or no customer contact;
  (b) omit the `Party/Contact` elements on the receipt.
- Needs decision: no
- From: broad F2, context F4, parties F2

### packaging/09#F3 · Low · A customs trader ID on a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: The customs trader identifier identifies Velumi to customs; the receipt is an over-the-counter
  sale in Lumeport with Coastal State sales tax charged, not a tax-free export sale, so customs has no
  role in it. It looks copied from master data (section 4.8).
- Condition: the receipt carries the customs ID only if the sale involves customs (e.g. a tax-free
  export sale).
- Options: (a) preferred: leave it out; (b) if the shirts are meant to be exported by Velumi, show it
  in the tax treatment.
- Needs decision: no
- From: parties F6

### packaging/09#F4 · Low · Velumi's address is tagged en-XB here, en-XL in its own documents
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: The English renderings of Velumi Trading's Lisavan address carry `languageID="en-XB"` here, but
  `en-XL` where Velumi issues the document
  (`sea/05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`,
  languageID `en-XL`). Velumi's English street name is tagged en-XB in 11 examples and en-XL in 8
  (lxml count over `*.xml` of the `PostalAddress/StreetName` of parties named Velumi Trading,
  re-counted in the merge). The tag follows the issuer's country, so the same text of the same
  address is attributed to two varieties of English. Broad and context refuted the candidate: the
  English rendering carries the issuer's locale, as elsewhere in the world. That reading is a
  possible convention, but none is stated, and one object is described two ways. The merge cannot
  settle which reading the world intends, so the finding stays Low with a decision.
- Condition: the same text of Velumi's address carries the same `languageID` in every example, or the
  convention (issuer's variety) is stated.
- Options: (a) preferred by parties: tag a party's English names with the variety of the party's
  country (`en-XL`), as in Velumi's own documents; (b) adopt the issuer's variety as an explicit,
  recorded convention.
- Needs decision: yes (a world-wide language-tagging convention)
- From: parties F3 (refuted by broad and context, see "Considered and refuted")

### packaging/09#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Velumi Trading (Island
  companies register) shares this date with 24 companies in the registers of Bayvarra and Urvania
  (271 occurrences in 181 examples, grep over `*.xml`, re-counted in the merge), which reads as a
  default (IND5).
- Condition: Velumi's RegistrationDate is its own date in the story, or absent.
- Options: (a) preferred: an individual date from the company history; (b) remove; (c) confirm as a
  story fact.
- Needs decision: yes (dates are part of the companies' histories)
- From: broad F5, parties F4

### packaging/09#F6 · Low · Three shirts without the "5.00 off the pair" given the day before
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:Quantity` = `3`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cbc:LineExtensionAmount` = `35.940`
- XPath: `08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Two shirts: 5.00 off the pair`
- Why: On 2026-05-22 the same store, till `C1` and cashier gave 5.00 off a pair of the same shirt
  (`BM-778120`, `08-PurchaseReceipt.xml`). On 2026-05-23 Velumi Trading buys three of them, which
  contain a pair, at the full price (3 × 11.98 XLC = 35.94 XLC = 3 × 29.95 XBL at 0.4, recomputed in
  the merge); no allowance is applied. Either the promotion ended on 22 May, which neither receipt
  says, or one discount of 5.00 XBL (2.00 XLC) is missing here.
- Condition: the two receipts agree on the promotion: either this line carries the pair discount
  (converted to coral), with line, tax and totals recalculated, or one of the receipts states when
  the offer applies.
- Options: (a) preferred: state the offer's validity in the allowance reason of 08 (e.g. a one-day or
  weekend offer, 22 May), which keeps this receipt's arithmetic; (b) apply 2.00 XLC off the pair here
  and recalculate.
- Needs decision: yes (whether the promotion applies is part of the story)
- From: context F2, money F1

### packaging/09#F7 · Low · The item description carries a tax statement
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description` = `Men's cotton shirt; the state sales tax is added at the till.`
- Why: `Item/Description` is "Text describing this item"; the second half describes the taxation of
  the sale, which the structured `TaxTotal` already gives. Same text in 3 examples
  (`grep -rl --include='*.xml' 'sales tax is added at the till'`, re-counted in the merge).
- Condition: the item description describes only the item.
- Options: (a) preferred: drop the tax sentence; (b) move it to `/PurchaseReceipt/cbc:Note`.
- Needs decision: no
- From: context F3

### packaging/09#F8 · Low · The shirt's GTIN is under the retailer's GS1 prefix, not the brand owner's
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: Under the GS1 General Specifications a GTIN is allocated by the brand owner from its own
  company prefix (own knowledge). The `Lumeport`-brand shirt made by Lumeport Textile Mill has a GTIN
  that starts with the seven digits `9522610` of Brightmarket's GLN, so it reads as allocated by the
  retailer; a retailer does that only for its own label, otherwise it uses restricted-circulation
  numbers (02, 20–29). The B2B documents of the flow (05–07) carry no GTIN. Whether it is a problem
  depends on who owns the brand and on the length of Brightmarket's company prefix, which the
  documents do not say. The 952 prefix is GS1's demonstration range. Same as in
  `08-PurchaseReceipt.xml` (F5 there, with the world's mixed conventions).
- Condition: the GTIN is allocated by the party the world treats as the shirt's brand owner, and the
  documents make that owner recognisable; or the shirt is identified by a restricted-circulation
  number; or the world's identification convention records that retailers assign GTINs to items
  whose makers use no GS1 numbers.
- Options: as in `08-PurchaseReceipt.xml` F5: (a) decide who owns the brand and allocate, carry or
  drop the GTIN accordingly (preferred); (b) record the convention; (c) keep the store's number only
  as `SellersItemIdentification`.
- Needs decision: yes (brand ownership is part of the story)
- From: broad F3, logistics F1, parties F5

### packaging/09#F9 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `772030000090`
- Why: The world's item scheme (`urn:ubl-examples:world:item`) holds a well-formed GTIN-12 (UPC-A;
  check digit 0, recomputed in the merge) whose GTIN-13 prefix 077 lies in the range GS1 US
  allocates (060–139, own knowledge), so it can be taken for a real UPC; the agreed rule is that
  fictional values must not be mistaken for real ones. 8 distinct values of the scheme, all valid,
  in 64 examples (logistics, grep over `*.xml`).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1
  allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN; (b) GTINs in GS1's demonstration
  prefix 952; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes (world-wide identifier convention)
- From: broad F4, logistics F2

## Checked and consistent
- Pricing in coral (dynamic currency conversion, `/PurchaseReceipt/cbc:Note` = `Paid in coral: the card's currency was chosen at the till.`):
  `/PurchaseReceipt/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4` from XBL to XLC; 29.95 × 0.4
  = 11.98 = `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:PriceAmount` = `11.98`; 3 × 11.98
  = 35.94 = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `35.940` (XLC has 3
  decimals in `world/codelists/CurrencyCode-2.4-world.gc`).
- Tax in document currency: 6.5 % × 35.940 = 2.3361 → `/PurchaseReceipt/cac:TaxTotal[1]/cbc:TaxAmount` = `2.336`;
  35.940 + 2.336 = `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.276` =
  `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `38.276`.
- Tax in tax currency: `/PurchaseReceipt/cac:TaxExchangeRate/cbc:CalculationRate` = `2.5` from XLC to
  XBL, the reciprocal of 0.4; 35.940 × 2.5 = 89.85 = `/PurchaseReceipt/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `89.85`
  (= 3 × 29.95); 6.5 % × 89.85 = 5.84 = `/PurchaseReceipt/cac:TaxTotal[2]/cbc:TaxAmount` = `5.84`,
  also 2.336 × 2.5. XBL is the currency of Brightmarket's STT registration. (All redone in the merge.)
- Card: `PaymentMeansCode` 54, `CardTypeCode` CREDIT, Coralcard network, issuer `BSELXLSL` (world bank
  identifier; owner code `BSEL` not in `world/codelists/sources/bic/owner-codes.txt`, parties), holder
  `VELUMI TRADING` = the customer; PAN masked.
- Brightmarket's supplier block is identical to the one in `08-PurchaseReceipt.xml`; store, till C1,
  cashier and point of sale agree; item identifiers, manufacturer party, HS `620520`, CPC `28232` and
  properties agree with 05–08.
- Velumi Trading: register ID `IC41859` in PartyIdentification, CompanyID and endpoint `XL:IC41859`;
  Island limited company, small, active.
- Timing: 3 shirts sold 2026-05-23 12:20, after the despatch (`06-DespatchAdvice.xml`, 2026-05-12) and
  after `08-PurchaseReceipt.xml` (2026-05-22 16:05); together 5 of the 600 delivered.
- `check_ids.py` (rerun in the merge): GLN `9522610900002` and GTIN `9522610000016` pass.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
  and `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
  tagged `en-XB` for a Lisavan address — refuted because the English rendering carries the issuer's
  locale (Brightmarket, Bayvarra), as elsewhere in the world (from broad, context). The merge
  disagrees in part and keeps it as F4 (Low, needs decision): no such convention is stated, and the
  same address is tagged two ways.
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`, the web
  shop and `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`:
  master data — refuted because receipts carry the store's logo, web and social media details for the
  customer (from broad, context, parties).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649`: a
  household-goods wholesaler paying standard sales tax on three shirts at retail — refuted because a
  company may buy goods for its own use (staff clothing, samples) at a store with its company card,
  and no resale exemption is claimed (from broad, context, parties).
- `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `38.276` with three decimals — refuted because Coral
  has 3 fractional digits in the world's currency list (from broad).
- `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `54`: a credit card in "A receipt for a
  purchase made with cash or cash equivalents" — refuted because a card payment at a till counts as a
  cash equivalent for a point-of-sale receipt (from context).
- `/PurchaseReceipt/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL` while
  `/PurchaseReceipt/cac:TaxExchangeRate/cbc:SourceCurrencyCode` = `XLC`: suspected inconsistent
  directions — refuted because the two conversions really run in opposite directions (lume shelf
  price into coral; coral amounts into lume for the tax), each stated in its own direction, and the
  rates are reciprocal (from money).
- Two `TaxTotal` for the same scheme STT — refuted because the second is the same tax in the tax
  currency, linked by `TaxExchangeRate`; PurchaseReceipt has no `TaxCurrencyCode` in UBL 2.5, so the
  amounts' currencyID carries it (from money, broad).
- Sales tax charged to a company from Lisavu — refuted because it is an over-the-counter retail sale
  in Lumeport, taxable where the goods are handed over; there is no export (from money).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `40351721`: a
  delivery-point ID instead of a postal zone — refuted because it is Lisavu's own address register
  (`urn:ubl-examples:world:XL:delivery-point`), the national level the agreed rules prescribe (from
  parties).

## Changed in the merge
- parties F3 → F4: kept as Low with "Needs decision: yes" although broad and context refuted the
  candidate, because the merge can neither confirm nor refute which convention the world intends;
  the same treatment as merger A gives the Urvanian case in `02-Invoice.xml`
  (`packaging-merge-decisions-a.md`).
- context F2 / money F1 → F6: options combined; Needs decision yes (money's reason) adopted.
- broad F2 / context F4 / parties F2 → F2: grouped, store contacts and the customer's contact in one
  finding.
- F1 (LocaleCode): both options kept; preference stated as removal (broad, context) against
  parties' `en-XB`.
- Findings renumbered by severity and position.
