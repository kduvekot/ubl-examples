# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
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

### packaging/02#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". A locale
  is a language in a region; `en` (listID `ISO 639`) is the language that
  `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:ID` = `en` already gives. The same
  value occurs 362 times in 213 example files, always `en`, only on English-speaking parties (grep
  over `*.xml`, re-counted in the merge).
- Condition: LocaleCode is absent, or holds a locale (language and region) from a list named in its
  listID.
- Options: (a) preferred: remove it, because Language/ID already says English and nothing in the
  invoice uses a locale; (b) a locale such as `en-XB` from a locale list.
- Needs decision: no
- From: broad, parties, context

### packaging/02#F2 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is "The recognized geographic or economic region or group of countries in
  which this address is located"; a province is "The political or administrative division of a
  country in which this address is located, such as the name of its county, province, or state",
  i.e. CountrySubentity, which the Bayvarran address of the same invoice uses
  (`/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`).
  219 occurrences in 104 example files (grep -c over `*.xml` for `<cbc:Region>Province of`,
  re-counted in the merge); all 215 Urvanian addresses use Region and none CountrySubentity (lxml
  count by the parties part).
- Condition: the province of Ferrano is not in Region; where needed it is in CountrySubentity; Region
  is absent or holds an actual region.
- Options: (a) preferred: move it to CountrySubentity, as for Bayvarra; (b) drop it if the Urvanian
  format does not need it; (c) keep Region only for a real economic region.
- Needs decision: no
- From: broad, parties, context

### packaging/02#F3 · Low · Default-looking registration date 1996-01-01
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Rivermouth shares exactly this
  date with 24 other companies in the registers of all three countries (271 occurrences in 181 files,
  25 distinct CompanyIDs; counted over `*.xml`, re-done in the merge), while the customer in this
  invoice has its own (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1962-04-12`).
  It reads as a default, not as Rivermouth's registration date (IND5).
- Condition: Rivermouth's RegistrationDate is the date of its own registration in the story, or
  absent.
- Options: (a) preferred: a date from the company history; (b) omit it; (c) confirm 1996-01-01 as a
  story fact.
- Needs decision: yes (company histories)
- From: broad, parties

### packaging/02#F4 · Low · The contacts of the accounting parties are order desks, not accounting contacts
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party"; under AccountingCustomerParty it is
  whom the supplier contacts about the invoice and its payment (accounts payable), under
  AccountingSupplierParty whom the customer asks about the invoice (accounts receivable or billing).
  Valdara, the invoiced buyer, gives its order desk in its Sales department with the title
  `Customer service officer`, a seller-side function that is neither its accounts payable nor its
  purchasing; Rivermouth's order desk is plausible but not an accounting contact. The same contacts
  are used in the order (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`):
  each party has one contact for every role. World-wide, 89 contacts carry
  (`Order desk`, `Customer service officer`, `Sales`) and 229 files carry `Customer service officer`
  (lxml count over `*.xml`, re-done in the merge).
- Condition: the contacts of the accounting parties belong to invoicing or payment, with name, job
  title and department that agree (or are absent).
- Options: (a) preferred: an accounts contact for each accounting party (accounts payable for
  Valdara, accounts receivable or billing for Rivermouth); (b) at least an accounts payable or
  purchasing contact for Valdara, keeping the order desk for Rivermouth; (c) omit the Contact where
  the invoice does not need one.
- Needs decision: no
- From: broad, parties, context

### packaging/02#F5 · Low · Valdara's English address tagged `en-XB` here but `en-XU` in the order; legal form rendered differently
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The English renderings of Valdara's address carry `languageID="en-XB"` here but `en-XU` in the
  order this invoice answers, for the same text
  (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`,
  languageID `en-XU`); the legal form is given once, without languageID, here, but in Urvanian and
  `en-XU` in the order
  (`01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`).
  Over all examples Valdara's English street name is tagged `en-XU` in 24 places and `en-XB` in 18
  (lxml count over `*.xml`, re-done in the merge): the tag follows the issuer's country. The parties
  part reads this as the same party's address described as two varieties of English (the skill asks
  whether the same party is described the same way in every example). The broad and context parts
  refuted it: the English rendering carries the issuer's variety (Rivermouth writes English as used in
  Bayvarra), the content is identical and both tags are valid; and one legal-form rendering in the
  document's default language (`/Invoice/cbc:DefaultLanguageCode` = `en`) is sufficient. Both
  readings are defensible; the merge cannot settle which convention the world intends.
- Condition: the same text of Valdara's address carries the same languageID in every example and its
  legal form is rendered the same way wherever given, or the issuer's-variety convention is stated as
  the world's rule (then this finding is dismissed).
- Options: (a) preferred by the parties part: tag a party's English names with the variety of the
  party's own country (`en-XU` for Valdara), which is what the party registers and what the order
  uses; (b) adopt the issuer's variety as an explicit convention, and apply it to the legal form as
  well.
- Needs decision: yes (a convention for the whole world; two parts refuted it)
- From: parties; refuted by broad and context (their entries are taken up here)

### packaging/02#F6 · Low · Customer master data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: ServiceProviderParty is "A party providing a service to this party"; Valdara's warehousing and
  despatch provider has no part in an invoice for stretch film collected FCA at the seller by
  Valdara's haulier (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`).
  The customer's stock listing is not used for invoicing, payment or tax. Both are copied from
  Valdara's master data (IND5); the Castrano block is in 75 files (grep -rl over `*.xml` for
  `VI-SP-2026-01` and for `Castrano Logistics`, re-done in the merge).
- Condition: every customer detail in the invoice has a role in invoicing, payment or tax, or the
  invoice states why it is there.
- Options: (a) preferred: leave ServiceProviderParty and SecurityListing out; (b) if Castrano received
  the goods, show it in that role through Delivery.
- Needs decision: no
- From: broad, parties, logistics, context

### packaging/02#F7 · Low · A one-month penalty period against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-06-02`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: PaymentTerms/PenaltyPeriod is "The period during which penalties may apply". A period starting
  2026-06-02 with a duration of one month says penalties may apply only until early July, while the
  note makes the surcharge accrue for every month of delay, without an end.
  `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `22.32` is one month's surcharge (1.5 % × 1488.00,
  re-computed), so the period seems meant as "the period one PenaltyAmount covers", which is not what
  the element means. All 18 example files with a PenaltyPeriod have
  `DurationMeasure unitCode="MON"` = 1 (grep over `*.xml`, re-counted in the merge), among them
  `04-Invoice.xml` and `07-Invoice.xml`.
- Condition: the penalty period either has no end (start date only) or ends when the terms say
  penalties stop; the per-month rate and the one-month PenaltyAmount are stated without suggesting
  that penalties stop after one month.
- Options: (a) preferred: keep StartDate and drop DurationMeasure, so the period is open-ended as the
  note says, and state in the note that 22.32 is the surcharge per month; (b) if the terms really cap
  penalties, state the cap in the note and keep the duration.
- Needs decision: no
- From: money

### packaging/02#F8 · Low · The export invoice says nothing about the delivery the exemption rests on
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `G`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521`
- Why: The invoice zero-rates the 480 kg of film as "Export outside Bayvarra" (category G, "Free
  export item, tax not charged"), but carries no Delivery (no actual delivery date, place, country
  or carrier), no DeliveryTerms and no reference to a despatch, transport or export document; the
  only foreign element is the customer's address. The order agreed
  `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA` at the seller's dispatch in Lumeport, with no
  date, so nowhere in the flow is it recorded when the goods were handed to the carrier, which is both
  the delivery under FCA and the event the export treatment rests on. Own knowledge: sales-tax and VAT
  export exemptions are normally tied to evidence that the goods were dispatched abroad, which
  invoices commonly state through the delivery place and date. By IND6 nothing may be implied from
  absence. Completeness remark; nothing contradicts.
- Condition: the invoice states when and where the goods were delivered or handed over and the
  country of destination (e.g. Delivery/ActualDeliveryDate and DeliveryLocation), or references the
  document that records it.
- Options: (a) preferred: add a Delivery with the actual handover date to Trasvia Haulage at the FCA
  place and the destination in Urvania, and the DeliveryTerms FCA from the order; (b) a document
  reference to a despatch advice, consignment note or export document, if the flow gets one; (c) leave
  it if the world's export evidence lives only in customs documents, and say so in the exemption
  reason text.
- Needs decision: no
- From: broad, money, logistics

### packaging/02#F9 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: StandardItemIdentification is "Identifying information for this item, assigned according to a
  standard system", here the world's own scheme `urn:ubl-examples:world:item`. The value is twelve
  digits with a valid GS1 mod-10 check digit, i.e. a well-formed GTIN-12 (UPC-A) whose GTIN-13 prefix
  077 lies in the range GS1 US allocates to real companies (060–139, own knowledge); whether it is
  assigned could not be checked. All 8 distinct values of the scheme have valid GTIN-12 check digits
  (82 occurrences in 64 files, grep over `*.xml`; check digits recomputed in the merge). The rule
  "fictional values must not be mistaken for real ones" applies. Same value as
  `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`.
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates
  to real companies, or the choice is recorded as checked against the real register.
- Options: (a) preferred: a form that cannot be read as a GTIN (letters, another length, or a failing
  mod-10 digit); (b) GTINs with GS1's example prefix 952, like the world's other GS1 keys;
  (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes (whether the numbers are assigned could not be settled; the change touches the
  world's item scheme)
- From: broad, logistics

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521` resolves to `01-Order.xml` (an order, buyer
  Valdara, seller Rivermouth, as here); the invoice (2026-05-02) is issued after the order
  (2026-04-27). Parties, item, quantity 480 KGM, price 3.1 XBL per KGM, item IDs, HS/CPC codes,
  thickness and tax treatment agree with it.
- Arithmetic (re-done): 480 × 3.1 = 1488.00 = line = LineExtension = TaxExclusive = TaxInclusive =
  Payable; tax 0.00. Due date 2026-05-02 + 30 days = 2026-06-01 in DueDate, PaymentMeans and
  PaymentTerms; penalty 1.5 % × 1488.00 = 22.32; penalty period starts the day after the due date.
- Payment means: credit transfer to Rivermouth's own account (same in PayeeFinancialAccount and the
  supplier party, named after Rivermouth Packaging Ltd, Harbour branch of the Bank of Lumeport);
  cross-border payment from Urvania over the Trade Accord rail (`RTNS`) with shared charges (`SHAR`);
  RF creditor reference `RF29RPINV260522` and the account pass check_ids.py; the instruction note
  quotes the reference.
- Tax: category G, 0 %, reason EXP, scheme STT identical in TaxTotal and ClassifiedTaxCategory; the
  seller is registered for STT in Coastal State (`CO-1238220`), the buyer for Urvanian VAT
  (`XU007299291`), as in the order.
- BuyerCustomerParty and SellerSupplierParty repeat the accounting parties by ID and name only.
- Physics: 480 kg / 16 kg = 30 whole rolls (as in the order's review).

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`:
  the party's account repeated next to the payee account — refuted because in an invoice the
  supplier is paid to that account; the two agree (from broad, money, parties, context).
- `/Invoice/cbc:AccountingCost` = `Raw materials and parts`: a cost centre that may not fit stretch
  film — refuted because a manufacturer can book packaging consumables with raw materials and
  supplies (from broad, money, context).
- `/Invoice/cbc:PaymentCurrencyCode` = `XBL`: redundant with the document currency — refuted because
  the payer is in Urvania (currency XUF), and the element states that payment is expected in lume
  (from money).
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote` = `Quote RF29RPINV260522`: duplicates PaymentID —
  refuted because the note is the instruction to the payer and the ID the structured reference; they
  agree (from money).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:Address/cbc:CityName` = `Lumeport`:
  a branch address with only a city — refuted because the branch is identified by its ID and name; the
  town is enough for its location (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`:
  customs trader ID in an invoice — refuted because the supply is an export to Urvania and the invoice
  is a customs-relevant document (from parties).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`: checked against
  the export from Bayvarra — consistent, the film is made by Rivermouth in Lumeport (from logistics).
- `/Invoice/cac:InvoiceLine/cac:Item/cac:CircularityProfile`: circularity data on an invoice line —
  refuted because the recycled content is part of what is sold and billed (from context).

## Changed in the merge
- broad/F2, parties/F2, context/F2 → F1 and broad/F1, parties/F1, context/F1 → F2: combined and
  renumbered by position (the supplier's language comes before the customer's address); severities
  unchanged. For LocaleCode the merge prefers removal (broad, context) over `en-XB` (parties), which
  stays option (b).
- broad/F7, parties/F5 → F3; broad/F3, parties/F4, context/F4 → F4; broad/F5, parties/F6,
  logistics/F2, context/F3 → F6; broad/F4, money/F2, logistics/F1 → F8; broad/F6, logistics/F3 → F9:
  combined, evidence and options merged; severities unchanged.
- parties/F3 → F5: kept as Low with Needs decision: yes, and the refutations of broad (StreetName[2]
  tagged en-XB; CompanyLegalForm with one rendering) and context (StreetName[2] tagged en-XB) are
  taken into the finding as the counter-argument instead of being listed under "Considered and
  refuted", because the merge could neither confirm nor refute it: whether a party's English names
  follow the party's or the issuer's variety is a world-wide convention not stated in the examples.
- money/F1 → F7: unchanged except that the count (18 files, all one month) was re-verified.

