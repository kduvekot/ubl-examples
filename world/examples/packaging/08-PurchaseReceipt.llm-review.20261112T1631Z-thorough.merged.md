# LLM review: 08-PurchaseReceipt.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/08-PurchaseReceipt.xml`, Git blob `9ece1e4003ae05ddafa0eb8d78c7dfd4d1e85d0d` (committed)
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

### packaging/08#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language already in `Language/ID` and names no locale. The same
  value occurs 362 times in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`,
  re-counted in the merge).
- Condition: `LocaleCode` is absent or holds a locale (language and region) from a locale list named
  in `listID`.
- Options: (a) remove it (preferred by broad and context, and here: it needs no new code list);
  (b) a real locale such as `en-XB` from a locale list (preferred by parties).
- Needs decision: no
- From: broad F1, context F1, parties F1

### packaging/08#F2 · Low · The retailer's contacts on a till receipt are its buying office
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- XPath: `/PurchaseReceipt/cac:PointOfSaleContact/cbc:Telephone` = `+999 2 38 2511 0411`
- Why: `Party/Contact` is "The primary contact for this party"; on a receipt handed to a consumer it
  is whom the customer contacts about the purchase (returns, complaints). Brightmarket gives its
  buying office, the contact it uses towards its suppliers
  (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`);
  job title and department (customer service, sales) would fit a receipt, but contradict the name
  and e-mail. `PointOfSaleContact` is "The contact person at the point of sale where this purchase
  took place", yet its telephone is the buying office's
  (`/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 2511 0411`),
  not a number of the store or the clothing floor.
- Condition: the supplier's contact and the point-of-sale contact are customer-facing contacts of
  the store, differ from the buying office, and have agreeing name, title, department and numbers.
- Options: (a) preferred: a customer service contact for the store in `Party/Contact` and the
  store's or floor's own number in `PointOfSaleContact`; (b) leave out `Party/Contact` and keep only
  the point-of-sale contact, or drop `PointOfSaleContact` if the store has no number of its own.
- Needs decision: no
- From: broad F3, context F4, parties F2

### packaging/08#F3 · Low · The customer's bank account on a receipt paid in cash
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- XPath: `/PurchaseReceipt/cac:PaymentMeans/cbc:PaymentMeansCode` = `10`
- Why: `Person/FinancialAccount` is "The financial account associated with this person". The
  purchase is paid in cash (code 10, `PaidCashAmount` 70.00, change 11.55); nothing is paid from or
  to Robin Ashdale's current account, so its number, branch and bank address have no purpose on the
  receipt (section 4.8: "a bank account of a party that pays or receives nothing under this
  document"). The account is the person's master data, used where it belongs in the utilities flow
  (`utilities/09-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `49`, direct debit); it
  occurs in 7 XML files (grep over `*.xml`, re-counted in the merge).
- Condition: the receipt carries the customer's financial account only if the purchase uses it
  (card or account payment, or a refund to it).
- Options: (a) preferred: remove `cac:FinancialAccount` from the customer's `Person` here; the
  customer can still be named on the receipt; (b) change the story to a payment that uses the
  account.
- Needs decision: no
- From: broad F2, context F2, money F1, parties F3 (account part; the address part is under
  "Refuted in the merge")

### packaging/08#F4 · Low · The item description carries a tax statement
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description` = `Men's cotton shirt; the state sales tax is added at the till.`
- Why: `Item/Description` is "Text describing this item". The second half describes how the sale is
  taxed, not the shirt; that follows from the structured values already there
  (`Price/PriceAmount` 29.95 net, `TaxInclusivePriceAmount` 31.9, `TaxTotal`) or belongs in a
  document-level `Note`. The same text is in 3 examples (`grep -rl --include='*.xml' 'sales tax is added at the till'`:
  this one, `09-PurchaseReceipt.xml`, `retail/21-PurchaseReceipt.xml`; re-counted in the merge).
- Condition: the item description describes only the item; any explanation of the till tax is in a
  document-level note.
- Options: (a) preferred: drop the tax sentence (the structured tax data say it); (b) move it to
  `/PurchaseReceipt/cbc:Note`.
- Needs decision: no
- From: context F3

### packaging/08#F5 · Low · The shirt's GTIN is under the retailer's GS1 prefix, not the brand owner's
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:BrandName` = `Lumeport`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: Under the GS1 General Specifications a GTIN is allocated by the brand owner of the trade item
  from its own company prefix (own knowledge). The shirt is branded `Lumeport` and made by Lumeport
  Textile Mill, but its GTIN starts with the seven digits `9522610` of Brightmarket's own GLN, so it
  reads as allocated by the retailer. A retailer numbers goods from its own prefix only for its own
  label; for a manufacturer's brand without a GTIN it uses restricted-circulation numbers (prefixes
  02, 20–29). The B2B documents of the flow (`05-Order.xml`, `06-DespatchAdvice.xml`,
  `07-Invoice.xml`) carry no GTIN. Whether it is a problem depends on who owns the brand `Lumeport`
  and on the length of Brightmarket's company prefix (with an eight-digit `95226109` the GTIN would
  not be Brightmarket's), which the documents do not say. The world mixes conventions: Brackenmere-
  brand items carry Brackenmere's prefix 9523710, Valdara-brand items in `retail/02-Catalogue.xml`
  the distributor's prefix 9520610 (logistics). The 952 prefix is GS1's demonstration range, so the
  value itself is not mistaken for a real one. The context part refuted this candidate (GS1 lets a
  retailer number own-brand goods); the merge keeps it because nothing shows `Lumeport` to be
  Brightmarket's label, and the manufacturer party points the other way.
- Condition: the GTIN is allocated by the party the world treats as the shirt's brand owner, and the
  documents make that owner recognisable; or the shirt is identified in the store by a
  restricted-circulation number; or the world's identification convention records that retailers
  assign GTINs to items whose makers use no GS1 numbers.
- Options: (a) decide who owns the brand (preferred by broad and parties): if the mill, give it a
  GS1 prefix and carry the GTIN through order, despatch advice and invoice too (preferred by
  logistics, because that is how GS1 intends the number to travel), or use no GTIN; if Brightmarket
  (private label), keep the GTIN and make the brand ownership visible; (b) record the convention
  that the store assigns GTINs because the mill has no GS1 membership; (c) keep the store's number
  only as `SellersItemIdentification`.
- Needs decision: yes (brand ownership is part of the story)
- From: broad F4, logistics F1, parties F4 (refuted by context, see "Considered and refuted")

### packaging/08#F6 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `772030000090`
- Why: The world's item scheme (`urn:ubl-examples:world:item`) holds a well-formed GTIN-12 (UPC-A;
  check digit 0, recomputed in the merge) whose GTIN-13 prefix 077 lies in the range GS1 US
  allocates (060–139, own knowledge), so it can be taken for a real UPC; the agreed rule is that
  fictional values must not be mistaken for real ones. 8 distinct values of the scheme, all valid,
  in 64 examples (logistics, grep over `*.xml`). Here it sits next to a real-format GTIN, which makes
  the confusion likelier.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1
  allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN; (b) GTINs in GS1's demonstration
  prefix 952; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes (world-wide identifier convention)
- From: broad F5, logistics F2

## Checked and consistent
- Arithmetic (redone in the merge): 2 × 29.95 = 59.90 = `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:BaseAmount` = `59.90`;
  − 5.00 = 54.90 = line = LineExtension = TaxExclusive = TaxableAmount; 6.5 % × 54.90 = 3.5685 →
  `/PurchaseReceipt/cac:TaxTotal/cbc:TaxAmount` = `3.57`; 54.90 + 3.57 = 58.47; rounding
  `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount` = `-0.02` → 58.45 (0.05 step
  for cash); 70.00 − 11.55 = `/PurchaseReceipt/cac:Payment/cbc:PaidAmount` = `58.45` = payable.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Price/cbc:TaxInclusivePriceAmount` = `31.9` = 29.95 ×
  1.065 = 31.897 rounded.
- Tax category S, scheme STT matches Brightmarket's STT registration in Coastal State; the shirt was
  bought exempt for resale (`07-Invoice.xml`), so charging STT on the retail sale is consistent.
- Item: `BM-778120` (seller) and `LT-SH-01` (manufacturer) are the buyer's and seller's IDs of
  `05-Order.xml`, right for the changed roles; manufacturer party = the mill (`20412603`); HS, CPC
  and properties as in 05–07.
- Brightmarket's supplier block is identical in `09-PurchaseReceipt.xml` and matches the buyer block
  of `05-Order.xml`.
- Sold 2026-05-22 16:05, after the despatch to the store (`06-DespatchAdvice.xml`, 2026-05-12).
- `check_ids.py` (rerun in the merge): GLN `9522610900002`, GTIN `9522610000016` and the customer's
  account `XB64BLUM38010007251840` pass.

## Considered and refuted
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`, the
  online shop and the social media profile: marketing data — refuted because a receipt is the
  customer-facing document on which a store prints its logo, web shop and social media (from broad,
  context, parties).
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`:
  legal detail on a receipt — refuted because company details are commonly printed on receipts
  (from context).
- `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
  with residential address on a cash receipt — refuted because a named receipt (returns, warranty, a
  loyalty account) is plausible (from broad, context; see also "Refuted in the merge").
- `/PurchaseReceipt/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount` = `-0.02`: UBL's definition says
  it is "added to produce the line extension amount" — refuted because that wording is a known slip
  in UBL; the element rounds the payable amount, which the value does (from broad, money).
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `95`
  ("Discount") for "5.00 off the pair" — refuted: fits (from broad).
- `/PurchaseReceipt/cbc:TransactionDate`, `/PurchaseReceipt/cbc:PurchaseDate` and
  `/PurchaseReceipt/cbc:IssueDate`, all `2026-05-22` 16:05 — refuted because at a till the transaction
  is begun, completed and receipted in the same minute (from context).
- `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Brightmarket Stores, Lumeport`: company name
  as a place — refuted because it is the name of the store, and the description names the floor
  (from context, parties).
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9522610000016`:
  GTIN with the retailer's prefix — refuted by context because GS1 lets a retailer number goods made
  for it under its own brand and nothing shows `Lumeport` is the mill's brand (from context). The
  merge disagrees and keeps it as F5 (Low, needs decision), because nothing shows it is
  Brightmarket's brand either, and three parts found it.
- `/PurchaseReceipt/cac:CashierContact/cbc:Name` = `Joss`: only a first name — refuted because a till
  receipt identifies the cashier by first name (from parties).
- `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`:
  checked for the shared default date — refuted, Brightmarket has its own date (from parties).

## Refuted in the merge
### parties/F3 · Low · A cash customer's home address and bank account on the receipt (address part)
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` = `Gull Lane`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why (as in the part): Person/FinancialAccount is "The financial account associated with this
  person". Robin Ashdale pays 70.00 in cash and gets change, so no account is involved, and nothing
  in the receipt (no delivery, no account sale, no loyalty scheme) needs the customer's residential
  address. A till receipt for a cash sale normally names no customer at all; the data looks copied
  from master data.
- Condition (as in the part): every customer detail on the receipt has a role in this purchase, or
  the receipt states the reason. Options: (a) remove the bank account; keep name and address only
  with a stated reason, otherwise leave out the customer party; (b) a payment from that account.
  Needs decision: no.
- Refuted because: the account part is kept as F3. The address part does not hold as a finding:
  `AccountingCustomerParty` on a receipt is the customer of record, and a receipt made out to a
  named customer with address (asked for exchange, warranty or an expense claim) is ordinary retail
  practice; the address is the identifying detail of such a receipt. Broad and context refuted the
  same candidate. Whether the story wants a named receipt at all may be noted when F3 is fixed.

## Changed in the merge
- parties F3 split → F3 (account part, merged with broad F2, context F2, money F1) and "Refuted in the
  merge" (address part), because only the account has no possible use on this receipt.
- broad F4 / logistics F1 / parties F4 → F5: options of all three combined (decide brand owner;
  record the convention; seller's ID only); kept although context refuted it.
- F1 (LocaleCode): both options kept; preference stated as removal (broad, context) against
  parties' `en-XB`.
- Findings renumbered by severity and position.
