# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/05-Order.xml`, Git blob `5869f45d431110e527ca796d40b56bf3f3390192` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### packaging/05#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) repeats the language of Language/ID and names no locale (a language in a
  region). The same value occurs 362 times in 213 example files, always `en` (grep over `*.xml`,
  re-counted in the merge).
- Condition: LocaleCode is absent, or holds a locale (language and region) from a list named in its
  listID, for both parties.
- Options: (a) preferred: remove it, because Language/ID already says English and nothing in the
  order uses a locale; (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, context

### packaging/05#F2 · Low · Men's shirts booked to the buyer's "Garden department"
- XPath: `/Order/cbc:AccountingCostCode` = `6120`
- XPath: `/Order/cbc:AccountingCost` = `Garden department`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Cotton shirt`
- Why: Order/AccountingCost is "The buyer's accounting cost centre, applied to the Order as a whole,
  expressed as text". Brightmarket buys 600 men's shirts for resale; its receipts sell them in the
  clothing department
  (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`),
  but the order books them to the garden department. The pair 6120 / Garden department is
  Brightmarket's constant: it fits its garden benches
  (`furniture/08-Order.xml:/Order/cbc:AccountingCost` = `Garden department`) and recurs on its other
  purchases, also water bills (`utilities/06-Invoice.xml`); 12 files carry it (grep -rl over
  `*.xml`, re-done in the merge). It looks copied from the party.
- Condition: the order's cost centre fits clothing (e.g. the clothing department, or general
  merchandise), and `07-Invoice.xml` carries the same one; or both carry none.
- Options: (a) preferred: a clothing-department cost centre with its own code in this order and its
  invoice, because the receipts already place the shirts there; (b) drop AccountingCost and
  AccountingCostCode here.
- Needs decision: no
- From: broad, money, context

### packaging/05#F3 · Low · Marketing and customs data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: LogoReferenceID ("An identifier for this party's logo"), AdditionalWebSite ("An additional
  web site associated with this party") and SocialMediaProfile ("A social media profile associated
  with this party") describe how Brightmarket presents itself to consumers; a purchase order to its
  supplier does nothing with them (IND5). On the receipts to shoppers (`08-PurchaseReceipt.xml`,
  `09-PurchaseReceipt.xml`) they have a reason. The seller's customs trader ID has no use in a DDP
  delivery within Lumeport. All look copied from master data (the logo reference is in 41 files,
  grep -rl over `*.xml` for `BM-LOGO-2024`, re-done in the merge).
- Condition: every party detail in the order has a role in this order, or the order states it (e.g.
  the supplier is to print the logo on labels).
- Options: (a) preferred: keep logo, web shop and social media profile for documents Brightmarket
  issues to consumers and leave them out here, together with the customs ID; (b) state in the
  example why the order carries them.
- Needs decision: no
- From: broad, parties, context

### packaging/05#F4 · Low · Contacts do not fit the roles: a sales job for the buying office, a purchasing contact for the seller
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- Why: Party/Contact is "The primary contact for this party". Brightmarket's buying office fits the
  buyer, but its job title and department (customer service in sales) contradict the name and e-mail
  `buying@brightmarket.example`. Lumeport Textile Mill is the seller here, yet its contact is the
  purchasing mailbox it uses as buyer in `03-Order.xml`
  (`03-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`);
  orders for shirts go to its sales side (it also carries a sales job title and department). Each
  party carries one contact whatever its role: world-wide (`Buying office`, `Customer service officer`,
  `Sales`) occurs in 41 contacts and (`Purchasing`, …) in 52, in 89 files with a Purchasing or
  Buying office contact in Sales (lxml count over `*.xml`, re-done in the merge).
- Condition: the buyer's contact describes a buying function and the seller's a selling one, each
  with agreeing name, job title and department.
- Options: (a) preferred: role-specific contacts per party (purchasing for the buyer role, sales or
  order desk for the seller role), with matching job titles and departments; (b) drop JobTitle and
  Department where only a functional mailbox is meant.
- Needs decision: no
- From: broad, parties, context

### packaging/05#F5 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". 25 companies in the registers of
  all three countries share exactly this date (271 occurrences in 181 files; counted over `*.xml`,
  re-done in the merge), while Brightmarket in the same order has its own
  (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`).
  It reads as a default (IND5).
- Condition: Lumeport Textile Mill's RegistrationDate is its own registration date in the story, or
  absent.
- Options: (a) preferred: a date from the company history; (b) omit; (c) confirm as a story fact.
- Needs decision: yes (company histories)
- From: broad, parties

### packaging/05#F6 · Low · No requested delivery date for the spring order
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: The order names the delivery party and DDP to the store's goods-in, but gives no requested
  delivery period or latest delivery date. The despatch advice calls this a seasonal order
  (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `The store's spring order of shirts.`),
  for which the wanted date matters. By IND6 nothing may be implied from absence; completeness
  remark. 15 of the world's 18 Orders carry no requested, promised or estimated delivery period,
  latest delivery date or requested despatch period (lxml over `*/*-Order.xml`, re-done in the
  merge).
- Condition: the order states when the shirts are to be delivered.
- Options: (a) preferred: Delivery/RequestedDeliveryPeriod; (b) Delivery/LatestDeliveryDate.
- Needs decision: no
- From: broad, logistics

### packaging/05#F7 · Low · The goods-in point is not identified although it has a GLN elsewhere
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: Location identifiers should be used where the same place is identified elsewhere (section 5).
  Brightmarket identifies its goods-in with a GLN in other flows
  (`furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`,
  named `Brightmarket Stores, goods-in`; also
  `retail/08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`). This
  order, which Brightmarket issues and which names the same place in words, gives neither that GLN
  nor an address for it; the place is identified only through the delivery party. Brightmarket uses
  GS1 keys in this very order (its party GLN
  `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`),
  so the convention "identification per party" does not explain the absence.
- Condition: the delivery place (in Delivery or DeliveryTerms) carries the goods-in GLN, or the
  example says why it is not used.
- Options: (a) preferred: add Delivery/DeliveryLocation with the goods-in GLN, as in
  `retail/08-Order.xml`; (b) leave it if the textile mill is not meant to know Brightmarket's GLNs
  (it uses its own numbers rather than GS1).
- Needs decision: no
- From: parties

### packaging/05#F8 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a
  standard system", here the world's own scheme `urn:ubl-examples:world:item`. The value is a
  well-formed GTIN-12 (valid mod-10 check digit) whose GTIN-13 prefix 077 lies in the range GS1 US
  allocates to real companies (060–139, own knowledge); whether it is assigned could not be checked.
  All 8 distinct values of the scheme share this (82 occurrences in 64 files, grep over `*.xml`; check
  digits recomputed in the merge), while the world's real GS1 keys use GS1's example prefix 952 (as
  Brightmarket's GLN in this order). The rule "fictional values must not be mistaken for real ones"
  applies.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates
  to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN (letters, another length, or a failing
  mod-10 digit); (b) GTINs with prefix 952; (c) keep them and record why they are not mistaken for
  real UPCs.
- Needs decision: yes (whether the numbers are assigned could not be settled; the change touches the
  world's item scheme)
- From: broad, logistics

## Checked and consistent
- Arithmetic (re-done): 600 EA × 14.5 = 8700.00 = line = AnticipatedMonetaryTotal
  LineExtensionAmount = PayableAmount; tax 0.
- Tax: E, 0 %, RESALE fits a retailer buying stock for resale; both parties registered for STT in
  Coastal State; `07-Invoice.xml` uses the same treatment, and the receipts (`08-PurchaseReceipt.xml`,
  `09-PurchaseReceipt.xml`) then charge STT at 6.5 %, which the resale exemption presupposes. Bought
  at 14.50, sold at 29.95 net of tax: a plausible retail margin.
- Item identification: the buyer's `BM-778120`, the seller's `LT-SH-01` and the world item number
  are the same in `06-DespatchAdvice.xml` and `07-Invoice.xml` (the invoice without the buyer's ID);
  in the receipts `BM-778120` is the seller's ID and `LT-SH-01` the manufacturer's, as the roles
  change.
- Codes: HS 620520 and CPC 28232 fit woven men's cotton shirts; "in a garment bag" links the shirts
  to the bags of `03-Order.xml`.
- Delivery: DDP to Brightmarket's goods-in, delivery party the buyer itself (`20410411`); the seller
  arranges carriage, and `06-DespatchAdvice.xml` names the seller's carrier, consistent with DDP.
- Parties: Brightmarket and Lumeport Textile Mill carry the same register IDs, tax IDs (`CO-1231233`,
  `CO-1237809`), legal entities, addresses and endpoints as in `06-DespatchAdvice.xml` and
  `07-Invoice.xml` and, for the mill, `03-Order.xml`/`04-Invoice.xml`. Brightmarket as a large public
  corporation, active, ISIC 4719 fits a department store. check_ids.py: GLN `9522610900002` passes;
  prefix 952 is GS1's range for examples (own knowledge).

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `DDP` for a delivery within Lumeport — refuted because Incoterms
  may be used for domestic contracts; DDP means the seller bears all costs to the buyer's door (from
  broad, logistics, context).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Lumeport` (also a town name) —
  refuted because a mill naming its brand after its town is plausible (from broad, context).
- `/Order/cac:SellerSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `1312`: a weaving mill
  selling shirts (ISIC 1410 would be apparel) — refuted because ISIC records the main activity and the
  mill weaves the cotton it makes the shirts from (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:TradePartyName/cbc:Name` = `Brightmarket`: a trading
  name in an order — refuted because it is the name the store trades under and the brand the supplier
  delivers to (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB` while
  the cotton is "grown on Lisavu" — refuted because origin is where the shirt is made (woven and sewn
  by the Lumeport mill); the description says where the fibre comes from (from logistics, context).

## Changed in the merge
- broad/F3, parties/F2, context/F3 → F4: combined; all XPath lines kept (the seller's e-mail from
  parties and context, the buyer's job title from broad and parties); severity unchanged.
- broad/F4, context/F4 (marketing data) and parties/F4 (marketing data and the seller's customs ID)
  → F3: combined; severity unchanged.
- parties/F5 → F7: kept; the merge adds Brightmarket's own GLN in this order as evidence that the
  party uses GS1 keys.
- broad/F1, parties/F1, context/F1 → F1; broad/F2, money/F1, context/F2 → F2; broad/F7, parties/F3 →
  F5; broad/F5, logistics/F1 → F6; broad/F6, logistics/F2 → F8: combined, evidence and options
  merged; severities unchanged. For LocaleCode the merge prefers removal (broad, context) over
  `en-XB` (parties), which stays option (b).
