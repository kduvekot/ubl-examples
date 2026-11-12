# LLM review: 05-Invoice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/05-Invoice.xml`, Git blob `a846f2c92225b4f657cb71040b2ccfd1f8ecfc9d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### mast/05#F1 · High · Due date 45 days after the invoice, terms say 30 days net
- XPath: `/Invoice/cbc:IssueDate` = `2026-06-04`
- XPath: `/Invoice/cbc:DueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-07-20`
- Why: 30 days after 2026-06-04 is 2026-07-04; 2026-07-19 is 45 days after issue. The due dates
  (document, payment means and payment terms) and the start of the penalty period follow the 45
  days; the note says 30. No other date (delivery, end of month) gives 30 days to 2026-07-19 within
  the documents (despatch 2026-06-04; end of June + 30 days would be 2026-07-30).
- Condition: the due dates and the penalty start agree with the terms stated in the note.
- Options: (a) due 2026-07-04 and penalty from 2026-07-05; (b) terms "45 days net" in the note; the
  choice depends on Saltmere's standard terms (XB-STD) in the world.
- Needs decision: yes (which terms are Saltmere's)

### mast/05#F2 · Medium · Placard notation 7 on an excepted package that carries no label
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: UN 2911 excepted packages carry no class 7 label or placard (own knowledge); the item's own
  text says so.
- Condition: no placard notation for the UN 2911 item.
- Options: (a, preferred) drop it (see also F5).
- Needs decision: no

### mast/05#F3 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639)
  is a language. 213 examples carry it.
- Condition: a locale (e.g. en-XB) or absent.
- Options: (a, preferred) `en-XB`; (b) drop it.
- Needs decision: no

### mast/05#F4 · Low · A pricing reference that carries no pricing information
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:BatchQuantity` = `1`
- Why: PricingReference is "a reference to pricing and item location information" for the line;
  here it holds only a hazardous-risk indicator and a delivery unit of one battery, no price, no
  location, no reference. Nothing in the invoice uses it (IND5); the price is in the line's Price.
- Condition: PricingReference is absent, or carries the pricing information it refers to.
- Options: (a, preferred) drop it.
- Needs decision: yes (affects coverage)

### mast/05#F5 · Low · Full dangerous-goods data in an invoice
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The invoice bills the goods; tunnel codes, EmS, ERG guides, placards, flash point and
  radioactive activity serve carriage, not billing (IND5). "9A" is the lithium-battery label model,
  not a placard endorsement, and "8" for the stripper repeats the class.
- Condition: the invoice's item data serve billing and identification; dangerous-goods details are
  absent or limited to what the invoice needs (e.g. a dangerous-goods surcharge, if any).
- Options: (a, preferred) drop HazardousItem from the invoice lines (keep the item identity and
  classification); (b) keep a minimal UN number with a reason.
- Needs decision: yes (affects coverage)

### mast/05#F6 · Low · Contacts that do not fit the accounting roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The supplier's contact for the invoice is its procurement office; the customer's is its sales
  desk. Accounting parties' contacts are accounts receivable and accounts payable.
- Condition: each accounting party's contact is its accounts function.
- Options: (a, preferred) role-specific contacts.
- Needs decision: no

### mast/05#F7 · Low · Lisavan address renderings tagged en-XB
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- Why: The same address is tagged `en-XB` here and `en-XL` in 01 and 03.
- Condition: the same address carries the same language tags in every example.
- Options: (a, preferred) tag by the address's own country.
- Needs decision: yes (the world's language convention)

### mast/05#F8 · Low · Activity of the americium sources: per detector or for the set?
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: 37 kBq is one detector's typical activity; the line is a set of ten (370 kBq). Falls away
  with F5 option (a).
- Condition: the activity is that of the set, or absent.
- Options: (a, preferred) drop with F5; (b) 370 kBq.
- Needs decision: no

### mast/05#F9 · Low · A mast operator classified as a wired telecom
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120); see the review of 01.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes

## Checked and consistent
- Arithmetic: lines 14400.00 + 180.00 + 190.00 = 14770.00 = line extension = tax exclusive = tax
  inclusive = payable; tax 0.00 at G 0 %; penalty 1.5 % × 14770.00 = 221.55.
- OrderReference ST-PO-26-0713 (01) and DespatchDocumentReference SE-DA-26-0718 (04) resolve; line
  references, quantities and prices agree with the order and the despatched quantities.
- Export exemption (G, "Export outside Bayvarra") fits goods despatched from Bayvarra to Lisavu,
  under the state sales tax of the seller's state (Upland State), as in the seller's tax scheme.
- RF78SEINV260719 check digits correct; account XB69BLUM38712001885122 passes the IBAN-style check
  (check_ids.py); the account belongs to the payee Saltmere Engineering.
- Issued 17:34 on the day of despatch, after the despatch advice.

## Considered and refuted
- `/Invoice/cbc:DefaultLanguageCode`: English for a Lisavan customer — refuted: the seller's language
  is English, and the invoice is in English.
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: real-time net settlement for a
  cross-border payment — refuted: the Trade Accord payment rail named in the payment means is the
  world's regional system.
