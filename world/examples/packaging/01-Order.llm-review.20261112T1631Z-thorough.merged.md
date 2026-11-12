# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
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

### packaging/01#F1 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in
  which this address is located"; CountrySubentity is "The political or administrative division of a
  country in which this address is located, such as the name of its county, province, or state". A
  province is that administrative division. The Bayvarran addresses of the same order use
  CountrySubentity for their state
  (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`).
  The pattern is systematic: `<cbc:Region>Province of …` occurs 219 times in 104 example files
  (grep -c over `*.xml`, re-counted in the merge), and every Urvanian address uses Region and none
  CountrySubentity (215 Urvanian addresses, lxml count by the parties part).
- Condition: no address in the example carries a province in Region; the province of Ferrano, where
  needed, is in CountrySubentity (with CountrySubentityCode and its listID if Urvania has such a list),
  in both addresses.
- Options: (a) preferred: move the value to CountrySubentity, as Bayvarra does for its states, so all
  three countries use the same element for the same level; (b) drop it if the Urvanian address format
  does not need the province; (c) keep Region only for a real economic region (e.g. the Trade Accord
  area), if the story has one.
- Needs decision: no
- From: broad, parties, context

### packaging/01#F2 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". A locale
  is a language in a region (as in the `en-XU`/`en-XB` languageID values the examples use); `en` with
  listID `ISO 639` is the bare language code that
  `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:ID` = `en` already carries. The same value
  occurs 362 times in 213 example files, always `en` (grep over `*.xml` for
  `<cbc:LocaleCode listID="ISO 639">`, re-counted in the merge); the Urvanian parties of this order
  carry no LocaleCode.
- Condition: LocaleCode is absent, or holds a locale (language and region) from a list that defines
  locales, named in its listID.
- Options: (a) preferred: remove it, because Language/ID already says English and nothing in the order
  depends on a locale; (b) a locale such as `en-XB` with a locale list (e.g. BCP 47) as listID.
- Needs decision: no
- From: broad, parties, context

### packaging/01#F3 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: SecurityListing ("One or more securities issued by this Party Legal Entity that are listed on
  regulated markets") is nothing a purchase order for 480 kg of stretch film relies on.
  ServiceProviderParty is "A party providing a service to this party": Valdara's warehousing and
  despatch provider Castrano Logistics plays no part in this order, since the film is collected FCA at
  Rivermouth's dispatch by Valdara's carrier
  (`/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`) and
  no delivery to, storage by or despatch by Castrano is stated. Party/FinancialAccount is "The
  financial account associated with this party": the order is issued by the buyer, has no
  PaymentMeans or PaymentTerms, and nothing in it is paid to or from the seller's account; the
  payment instruction is where it belongs, in
  `02-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
  All of this reads as party master data copied into the document (section 4.8, IND5). Counts
  (re-done in the merge over `*.xml`): the Castrano block (`VI-SP-2026-01`, and the name
  `Castrano Logistics`) is in 75 files; among the 18 Orders of the world only this one and
  `03-Order.xml` carry a seller FinancialAccount.
- Condition: each of these aggregates is either absent from the order or has a stated purpose in it
  (e.g. prepayment terms that use the account; Castrano as the receiving warehouse).
- Options: (a) preferred: remove SecurityListing, ServiceProviderParty and the seller's
  FinancialAccount from the order; (b) if Castrano is where the film is to be taken, say so in its
  role through Delivery (DeliveryParty/DeliveryLocation) instead of ServiceProviderParty, which would
  also answer where the goods go; (c) keep the account only with payment terms in the order that need
  it.
- Needs decision: no
- From: broad, money, parties, logistics, context

### packaging/01#F4 · Low · The buyer's contact is a sales customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party"; in BuyerCustomerParty of an Order it is
  whom the seller turns to about the purchase. Valdara buys stretch film here, but its contact is an
  order desk staffed by a customer service officer in its Sales department, i.e. the contact for
  Valdara's own customers. The seller's contact is described identically
  (`/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`), which fits the
  seller. Over all examples the triple (`Order desk`, `Customer service officer`, `Sales`) occurs in
  89 contacts, for buyers and sellers alike; job titles and departments look derived from the kind of
  party rather than the role (lxml count over `*.xml`, re-done in the merge).
- Condition: the buyer's contact in the order names a buying or procurement function, and its name,
  job title and department agree with it.
- Options: (a) preferred: give Valdara a purchasing contact for documents where it buys (as other
  buyers in the world have, e.g. `Procurement office` / `Procurement officer` / `Procurement`);
  (b) neutral job title and department; (c) no Contact for the buyer where the order does not need one.
- Needs decision: no
- From: broad, parties, context

### packaging/01#F5 · Low · Same registration date 1996-01-01 for unrelated companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". Rivermouth
  Packaging (Federal business register of Bayvarra) and Trasvia Haulage (Commercial register of
  Urvania) are in different registers of different countries but were both registered on New Year's
  Day 1996; 25 different companies in all three countries carry exactly this date (271 occurrences in
  181 files, 25 distinct CompanyIDs; counted over `*.xml`, re-done in the merge), while the other
  companies have individual dates
  (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`).
  It reads as a default (IND5); if it is a story fact (e.g. a common re-registration date), that is
  not visible in the documents.
- Condition: each company's RegistrationDate is the date of its own registration in the story, or the
  element is absent where the story has none.
- Options: (a) preferred: give each company its own date from its history; (b) omit RegistrationDate
  where the history has none; (c) if 1996-01-01 is a story fact, confirm it so later reviews can
  accept it.
- Needs decision: yes (company histories)
- From: broad, parties

### packaging/01#F6 · Low · No requested pick-up or delivery time
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FCA`
- Why: Under FCA the buyer's carrier collects the goods at the seller's premises, so the seller must
  have the 480 kg ready when Trasvia arrives. The order names the despatch party, the carrier and the
  FCA place, but carries no Delivery/RequestedDeliveryPeriod, Despatch/RequestedDespatchPeriod,
  LatestDeliveryDate or similar, and nothing else in the flow gives the date (no order response, no
  despatch advice for this order); by IND6 nothing can be implied from absence. Completeness remark:
  an order can rely on agreed lead times. 15 of the world's 18 Orders carry none of
  RequestedDeliveryPeriod, PromisedDeliveryPeriod, EstimatedDeliveryPeriod, LatestDeliveryDate,
  RequestedDespatchPeriod (lxml over `*/*-Order.xml`, re-done in the merge), including all three
  orders of this flow.
- Condition: the order states when the goods are to be ready for collection (or delivered), or the
  flow's story records that a standing lead time applies.
- Options: (a) preferred: a requested despatch (collection) period under Delivery/Despatch, since
  under FCA the handover to the carrier is the delivery; (b) Delivery/RequestedDeliveryPeriod; (c) a
  note that the standard lead time applies.
- Needs decision: no
- From: broad, logistics

### packaging/01#F7 · Low · The carrier's haulage licence in the order
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: The broad part counted Trasvia's operating permit among the master data the order does nothing
  with (IND5). The parties part refuted the same element: Trasvia crosses the Bayvarra–Urvania border
  and the seller hands the goods to it under FCA, so the buyer may reasonably tell the seller that its
  nominated carrier holds an international road haulage permit (valid to 2030-06-30). The merge
  cannot settle which reading the story intends: the order states no use for the permit, but a seller
  handing goods to a foreign haulier has a plausible interest in it.
- Condition: either the order no longer carries the carrier's PartyAuthorization, or the story
  records why the seller needs the permit at handover (and the review of later documents can accept
  it).
- Options: (a) remove the PartyAuthorization from the carrier in the order (preferred by the broad
  part: nothing in the order uses it); (b) keep it and record the reason (preferred by the parties
  part).
- Needs decision: yes (the two parts disagree; whether the permit belongs in the order is a story
  question)
- From: broad (as part of its master-data finding); refuted by parties

### packaging/01#F8 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a
  standard system", here the world's own scheme `urn:ubl-examples:world:item`. The value is twelve
  digits with a valid GS1 mod-10 check digit, i.e. a well-formed GTIN-12 (UPC-A); read as GTIN-13
  (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own
  knowledge), and such numbers are assigned to real companies. Whether this one is assigned was not
  checked (no GEPIR access). The world's real GS1 keys use prefix 952 (GS1's range for examples). All
  8 distinct values of the scheme have valid GTIN-12 check digits (82 occurrences in 64 files, grep
  over `*.xml`; check digits recomputed in the merge). The rule "fictional values must not be
  mistaken for real ones" applies.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates
  to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: give the world's item numbers a form that cannot be read as a GTIN
  (letters, another length, or a failing mod-10 digit), which removes the confusion at the source;
  (b) GTINs with prefix 952 and schemeID `GS1 GTIN`, if the items are meant to be GS1-identified;
  (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes (whether the numbers are assigned could not be settled; the change touches the
  world's item scheme)
- From: broad, logistics

## Checked and consistent
- Arithmetic (merge re-did it): 480 KGM × 3.1 XBL per 1 KGM = 1488.00 = line LineExtensionAmount =
  AnticipatedMonetaryTotal LineExtensionAmount = PayableAmount; tax 0 % of 1488.00 = 0.00, taxable
  amount equals the line total.
- Tax: seller in Coastal State, Bayvarra (state sales tax `STT`, state level), buyer in Urvania;
  category `G` at 0 % with reason `EXP` "Export outside Bayvarra" fits a sale collected FCA for
  carriage to Urvania; the scheme matches the seller's PartyTaxScheme; order and invoice agree
  (`02-Invoice.xml`). Currency XBL throughout; the buyer's own VAT reporting currency XUF does not
  conflict.
- Item, quantity, price, codes and item IDs agree with `02-Invoice.xml`.
- Physics: 480 kg on 16 kg rolls = 30 rolls; a 16 kg roll of 23 µm PE (about 920 kg/m³, own
  knowledge) at an assumed 0.5 m width holds about 1 510 m, a normal machine stretch-film roll; 30
  such rolls fit one 1.2 × 0.8 m pallet in two layers (logistics part; width and pallet are
  assumptions). Thickness 23 µm agrees with the seller's item ID `RP-SF-23`.
- Codes: HS 392010 and CPC 36330 fit polyethylene film; unit KGM for quantity and base quantity;
  origin XB fits a Bayvarran producer.
- Delivery terms FCA at the seller's dispatch; the carrier named under Delivery/Despatch (Trasvia,
  ISIC 4923, Urvanian) is the buyer's, as FCA implies; the despatch party is the seller (`20412740`).
- Party identifiers: Valdara `XU-R-104274`, Rivermouth `20412740` and Trasvia `XU-R-104822` are the
  same in PartyIdentification, PartyLegalEntity/CompanyID and the endpoint; Valdara and Rivermouth are
  described with the same IDs, tax IDs and legal forms in `02-Invoice.xml`.
- Legal entities and tax schemes fit the kinds of party (Valdara a listed SUA, large; Rivermouth and
  Trasvia small private companies; all active); legal form texts agree with the codes.
- Contacts of the seller (order desk, sales) and of the carrier (planning desk, operations) fit their
  roles.
- check_ids.py: ISIN `XU0001042501` and account `XB96BLUM38020504712805` pass. Fictional codes against
  real registers: MIC `XFER` not in ISO 10383, bank owner code `BLUM` not in the BIC owner-code list,
  `+999` reserved by ITU, `.example` domains reserved (parties part).

## Considered and refuted
- `/Order/cbc:AccountingCostCode` = `3100` and `/Order/cbc:AccountingCost` = `Raw materials and parts`:
  same digits as Valdara's ISIC code 3100, and a cost centre that may not fit stretch film — refuted
  because the cost code is the buyer's own chart of accounts (the other buyers of the flow use 2200
  and 6120, unrelated to their ISIC codes), and pallet-wrapping film is a production consumable a
  furniture maker can book under raw materials and parts; unlike `03-Order.xml` the cost centre does
  not name a different kind of goods (from broad, money, context).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`:
  Italian-looking text tagged `en-XU` — refuted because the world renders Urvanian names in an
  Italianate exonym form in English (as `Ferrano`); the tag says which variety of English uses the
  name, and in this order it is the issuer's and the party's own variety (from broad, parties,
  context).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`:
  UBL defines it as "The number of shares in the capital stock of a corporation", but the element is
  an Amount with currencyID — refuted for this example: the value is the share capital in XUF, the
  only reading the data type allows; the inconsistency lies in UBL's definition (a possible point for
  the TC write-up). Legal-entity data identify the contracting party, which an order is (from broad,
  money, parties, context).
- `/Order/cac:TaxTotal/cbc:TaxAmount` = `0.00`: a tax total in an order — refuted because the
  anticipated tax treatment (export, 0 %) is legitimate in an Order and agrees with the invoice (from
  broad, context).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XUF`
  against the document currency XBL — refuted because it is the buyer's own VAT reporting currency in
  Urvania; the order's tax (Bayvarran STT) is in XBL (from money).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`:
  customs trader IDs in an order — refuted because the sale is cross-border (Bayvarra to Urvania,
  category G), so both parties' customs identities are relevant (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`:
  ISO 6523 ICD 0990 as a clash with a real register — refuted because ICD 0990 is not assigned (own
  knowledge of the parties part; assigned ICDs end in the 0200s) (from parties).
- `/Order/cac:Delivery/cac:Despatch`: a despatch block in an order — refuted because under FCA the
  buyer tells the seller which carrier collects, which is what Despatch/CarrierParty ("The Party who
  provides the transport of goods between named points") says (from logistics).
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rivermouth Packaging, dispatch, Lumeport`:
  a delivery location without address or ID — refuted because the place is the seller's own
  premises, whose address is in the seller party; the description names the point within it, enough
  for an FCA named place (from parties, logistics).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:EndOfLifeTreatment/cac:TreatmentLocation/cbc:Name` = `Rinova Recovery's plant, Ferrano`:
  a company name in a location name, and a possible town/country mismatch — refuted because it names
  the plant (the place) of that company, and Ferrano is in Urvania as the address says (from parties,
  logistics).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`: circularity data in an order —
  refuted because the recycled content is a property the buyer orders ("recycled polyethylene") and
  the end-of-life treatment in the buyer's country fits where the film ends up (from context).

## Changed in the merge
- broad/F4 → F3 and F7: the broad part's master-data finding is grouped with parties/F5, money/F1,
  logistics/F2, context/F3 and context/F4 into F3 (seller account, Castrano, security listing); the
  carrier's haulage permit, which the broad part included and the parties part refuted under
  "Considered and refuted", is split off as F7, Low with Needs decision: yes, because the merge could
  not settle the disagreement.
- context/F4 → F3: the count "84 examples contain `Castrano Logistics`" is corrected to 75 (grep -rl
  over `*.xml` in the merge gives 75 for both `Castrano Logistics` and `VI-SP-2026-01`).
- parties/F2 → F2: the parties part preferred a locale such as `en-XB`; the merge prefers removal (as
  broad and context), because nothing in the order uses a locale; `en-XB` stays as option (b). The
  same choice is applied in the other half of the flow's merge (decisions file of this run).
- broad/F3, parties/F3, context/F5 → F4; broad/F7, parties/F4 → F5; broad/F5, logistics/F1 → F6;
  broad/F6, logistics/F3 → F8: combined, wording and options merged; severities unchanged.
- broad/F1, parties/F1, context/F1 → F1; broad/F2, parties/F2, context/F2 → F2: combined; severities
  unchanged.

## Outside this review
- Whether Trasvia Haulage's road leg from Lumeport (XB) to Ferrano (XU) runs on a route of the map and
  fits the dates is a cross-flow question of location and timeline (from broad, logistics).
