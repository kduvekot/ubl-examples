# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/03-Order.xml`, Git blob `4c3acea07de9e59031f62d8970fa32ff7a492ca6` (committed)
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

### packaging/03#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en`
  (listID `ISO 639`) is the language that Language/ID already gives, not a locale (a language in a
  region). The same value occurs 362 times in 213 example files, always `en` (grep over `*.xml`,
  re-counted in the merge).
- Condition: LocaleCode, for both parties, is absent or holds a locale (language and region) from a
  list named in its listID.
- Options: (a) preferred: remove it, because Language/ID already says English and nothing in the
  order uses a locale; (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, context

### packaging/03#F2 · Low · Garment bags booked to the buyer's cost centre "Raw cotton"
- XPath: `/Order/cbc:AccountingCostCode` = `2200`
- XPath: `/Order/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Garment bag`
- Why: Order/AccountingCost is "The buyer's accounting cost centre, applied to the Order as a whole,
  expressed as text". The only line orders 20 000 polyethylene garment bags, packaging for the mill's
  shirts, yet the whole order is booked to the raw-cotton cost centre. The pair 2200 / Raw cotton is
  the mill's account for its cotton purchases
  (`cotton/08-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`) and occurs on every purchase of
  the mill: 5 files (`cotton/08-Order.xml`, `cotton/16-Invoice.xml`, `cotton/17-Invoice.xml`, this
  order and `04-Invoice.xml`; grep -rl over `*.xml`, re-done in the merge). It looks copied from the
  party, not chosen for this purchase.
- Condition: the order's cost centre is one under which the mill plausibly books packaging material,
  and `04-Invoice.xml` carries the same one; or the order carries none.
- Options: (a) preferred: a packaging-materials or consumables cost centre with its own code, in the
  order and its invoice; (b) omit AccountingCost and AccountingCostCode here.
- Needs decision: no
- From: broad, money, context

### packaging/03#F3 · Low · Party data a domestic order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-412740`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: The customs trader identifiers (schemeID `urn:ubl-examples:world:XB:customs-trader`) identify
  the parties to customs; both parties are in Lumeport and the bags are delivered DAP to the buyer's
  goods-in in Lumeport, so no customs formality is involved (in `01-Order.xml`, a cross-border sale,
  the same IDs were accepted for that reason). Party/FinancialAccount is "The financial account
  associated with this party"; the order is issued by the buyer, has no PaymentMeans or PaymentTerms,
  and nothing in it uses the seller's account, which is given where it is used in
  `04-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
  Among the 18 Orders of the world only this one and `01-Order.xml` carry a seller FinancialAccount
  (lxml over `*/*-Order.xml`, re-done in the merge). These look copied from master data (section 4.8,
  IND5).
- Condition: every party detail in the order has a role in this domestic order; in particular no
  customs trader IDs and no seller FinancialAccount unless the order states a use (e.g. prepayment
  terms).
- Options: (a) preferred: leave out the seller's FinancialAccount and both customs trader IDs here;
  (b) keep the customs IDs only where the order involves customs, the account only with payment terms
  that need it.
- Needs decision: no
- From: broad (account), money (account), parties, context (account)

### packaging/03#F4 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Both companies of this order
  carry it, as do 25 different companies in the registers of all three countries (271 occurrences in
  181 files, 25 distinct CompanyIDs; counted over `*.xml`, re-done in the merge). It reads as a
  default (IND5).
- Condition: each company's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: individual dates from the companies' histories; (b) omit; (c) confirm
  1996-01-01 as a story fact.
- Needs decision: yes (company histories)
- From: broad, parties

### packaging/03#F5 · Low · The buyer's contact contradicts itself: "Purchasing" in the Sales department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact/JobTitle is "The job title or function of this contact" and Department "The
  department where this contact works". Name and e-mail
  (`/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`)
  say purchasing, which fits the buyer, but job title and department say customer service in sales.
  The triple (`Purchasing`, `Customer service officer`, `Sales`) occurs in 52 contacts, and 89 files
  have a `Purchasing` or `Buying office` contact in Sales (lxml count over `*.xml`, re-done in the
  merge): job title and department look derived from the kind of party, not the contact.
- Condition: name, job title and department of the buyer's contact agree with each other and with
  buying.
- Options: (a) preferred: a purchasing job title and department (e.g. Buyer, Purchasing); (b) drop
  JobTitle and Department where only a functional mailbox is meant.
- Needs decision: no
- From: broad, parties, context

### packaging/03#F6 · Low · No requested delivery date
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Textile Mill, goods-in`
- Why: Under DAP the seller delivers to the mill's goods-in, and the order names the delivery party
  and place but not when the 20 000 bags are wanted (no RequestedDeliveryPeriod or
  LatestDeliveryDate). The timing has a business reason in the flow: the bags are needed before the
  mill packs the store's shirts (`05-Order.xml`, ordered 2026-05-07, despatched in
  `06-DespatchAdvice.xml`). By IND6 nothing may be implied from absence; completeness remark. 15 of
  the world's 18 Orders carry no requested, promised or estimated delivery period, latest delivery
  date or requested despatch period (lxml over `*/*-Order.xml`, re-done in the merge).
- Condition: the order states when the bags are to be delivered, or the flow records that a standing
  lead time applies.
- Options: (a) preferred: Delivery/RequestedDeliveryPeriod, the element for a DAP delivery date;
  (b) Delivery/LatestDeliveryDate; (c) a note on the standard lead time.
- Needs decision: no
- From: broad, logistics

### packaging/03#F7 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000110`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a
  standard system", here the world's own scheme `urn:ubl-examples:world:item`. The value is twelve
  digits with a valid GS1 mod-10 check digit (0), i.e. a well-formed GTIN-12 (UPC-A) whose GTIN-13
  prefix 077 lies in the range GS1 US allocates to real companies (060–139, own knowledge); whether
  it is assigned could not be checked. All 8 distinct values of the scheme have valid check digits (82
  occurrences in 64 files, grep over `*.xml`; check digits recomputed in the merge). The rule
  "fictional values must not be mistaken for real ones" applies.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates
  to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN (letters, another length, or a failing
  mod-10 digit); (b) GTINs with GS1's example prefix 952; (c) keep them and record why they are not
  mistaken for real UPCs.
- Needs decision: yes (whether the numbers are assigned could not be settled; the change touches the
  world's item scheme)
- From: broad, logistics

## Checked and consistent
- Arithmetic (re-done): 20 000 EA × 0.08 = 1600.00 = line = AnticipatedMonetaryTotal
  LineExtensionAmount = PayableAmount; tax 0.
- Tax: category E at 0 % with reason RESALE "Sale for resale or manufacture" fits garment bags a
  garment maker passes on with its shirts (`05-Order.xml`: "in a garment bag"); both parties are
  registered for Coastal State sales tax, a domestic sale; order and invoice agree. Currency XBL.
- Item, quantity, price, item IDs, HS 392321 and CPC 36410 agree with `04-Invoice.xml`; both codes fit
  polyethylene sacks and bags; unit EA.
- Delivery: DAP to "Lumeport Textile Mill, goods-in", delivery party the buyer itself (`20412603`),
  no carrier named, which is right under DAP.
- Physics: 20 000 bags in boxes of 500 = 40 boxes; at about 17 g per bag (60 cm × about 1 m × two
  layers of 15 µm PE at 920 kg/m³; length and thickness assumed by the logistics part) a box is about
  8 kg and the order about 330 kg, a small-van delivery inside Lumeport.
- Parties: register IDs, tax IDs (`CO-1237809`, `CO-1238220`), legal entities, addresses and endpoints
  are the same as in `04-Invoice.xml` and, for Rivermouth, `01-Order.xml`/`02-Invoice.xml`; both small
  private limited companies, active, legal form texts agree with the codes; the seller's contact
  (order desk, sales) fits the seller. check_ids.py: the account passes.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `1312`: a weaving mill
  buying garment bags and selling finished shirts (`05-Order.xml`) — refuted because the code states
  the party's main activity, and a mill that also makes up garments from its cloth is plausible (from
  broad, parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`: delivery
  party equal to the buyer — refuted because it names who receives the goods at the DAP place; not a
  filler (from broad, context).
- `/Order/cac:DeliveryTerms/cbc:ID` = `DAP`: a delivery cost the order should price — refuted because
  under DAP the seller bears transport to the buyer's goods-in and includes it in the price (from
  money).
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Textile Mill, goods-in`:
  a location without address or ID — refuted because the delivery party and the buyer's full address
  are in the order (from parties).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garment bag of recycled polyethylene, 60 cm, boxes of 500.`:
  "60 cm" does not say which dimension — refuted because 60 cm is the usual width designation of
  garment covers, wider than a shirt on a hanger (about 42–46 cm, own knowledge) (from logistics).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item`: a garment bag "of recycled polyethylene" without a
  CircularityProfile, unlike the film of `01-Order.xml` — refuted because absence is not a finding;
  the description states the material (from context).

## Changed in the merge
- broad/F4, money/F2, context/F3 (seller account) and parties/F4 (account and customs IDs) → F3:
  grouped as one master-data finding; severity unchanged.
- broad/F2, money/F1, context/F2 → F2; broad/F7, parties/F3 → F4; broad/F3, parties/F2, context/F4 →
  F5; broad/F5, logistics/F1 → F6; broad/F6, logistics/F2 → F7; broad/F1, parties/F1, context/F1 → F1:
  combined, evidence and options merged; severities unchanged. For LocaleCode the merge prefers
  removal (broad, context) over `en-XB` (parties), which stays option (b).
