# LLM review: 05-Invoice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/05-Invoice.xml`, Git blob `a846f2c92225b4f657cb71040b2ccfd1f8ecfc9d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8533627 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all five parts
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

### mast/05#F1 · High · Due date 45 days after the invoice, the terms say 30 days net
- XPath: `/Invoice/cbc:IssueDate` = `2026-06-04`
- XPath: `/Invoice/cbc:DueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-07-19`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-07-20`
- Why: 30 days after 2026-06-04 is 2026-07-04; 2026-07-19 is 45 days after issue (redone in the merge:
  26 days to 30 June plus 19). All three due dates and the start of the penalty period follow the 45
  days; the note says 30 and names no other start (delivery, receipt), and no document of the flow
  has a date from which 30 days end on 2026-07-19 (despatch advice and waybill are of 2026-06-04 too).
  Every other invoice with terms `XB-STD` and this note is due exactly 30 days after issue, except
  utilities/06-Invoice.xml (21 days) (merge's lxml count over `*/*.xml`: 15 of 16 others), e.g.
  `air/10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-06-14` for an invoice of
  2026-05-15.
- Condition: the due dates (DueDate, PaymentMeans/PaymentDueDate, PaymentTerms/PaymentDueDate) and the
  start of the penalty period agree with the terms the note states, counted from the date the note
  names (the invoice date when it names none).
- Options: (a, preferred) due date 2026-07-04 and penalty period from 2026-07-05, as the seller's
  standard terms say elsewhere; (b) keep 2026-07-19 and state the agreed term (e.g. "45 days net").
- Needs decision: no
- From: broad (F1), money (F1)

### mast/05#F2 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639)
  repeats Language/ID (and the invoice's DefaultLanguageCode) and names no locale. Section 6 names this
  case as Medium. 213 examples
  (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent, or holds a locale (e.g. `en-XB`) from a locale list, with a
  matching listID.
- Options: (a) `en-XB` (preferred by broad and parties); (b) remove it (preferred by context).
- Needs decision: no
- From: broad (F3), parties (F1), context (F3)

### mast/05#F3 · Medium · A pricing reference without any pricing, holding dangerous-goods indicators
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cbc:HazardousRiskIndicator` = `true`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:BatchQuantity` = `1`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:PricingReference/cac:OriginalItemLocationQuantity/cac:DeliveryUnit/cbc:HazardousRiskIndicator` = `true`
- Why: PricingReference is "A reference to pricing and item location information associated with
  this invoice line", OriginalItemLocationQuantity "An original set of location-specific properties
  (e.g., price and quantity) associated with this item". Here it holds no price, no location and no
  original quantity condition, only two hazardous indicators, which repeat
  `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:HazardousRiskIndicator` = `true`, and a delivery batch of one battery. The
  price is the plain `/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `2400` per battery, as in the order, which
  has no PricingReference, so nothing "original" is carried over. Lines 2 and 3, also dangerous
  goods, have no such block. The aggregate is used for a meaning other than its definition (IND5).
  (The batch of one does match one battery per crate in the transport documents, as logistics noted.)
  The same use without a price occurs in one other example, retail/18-Invoice.xml (from money).
- Condition: every PricingReference in the invoice carries information that bears on the price of its
  line, or the block is absent; hazard status is stated on the item only.
- Options: (a, preferred) remove the block; (b) if a batch of one battery per delivery unit is a price
  condition, say so with the price it conditions.
- Needs decision: no
- From: context (F2), broad (F4, Low), money (F2, Low)

### mast/05#F4 · Medium · Placard notation 7 for an excepted package that carries no label and no placard
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "Text of the placard notation corresponding to the hazard class of this
  hazardous item" (or the orange plate's upper number). UN 2911 excepted packages carry no class 7
  label and are not placarded; only the UN number is marked (own knowledge: SSR-6, ADR
  1.7.1.5/5.1.5.4). The item's own text says so. Same as mast/01#F1 (4 examples of this flow).
- Condition: no placard notation for the UN 2911 item, and the HazardousItem agrees with its own
  AdditionalInformation.
- Options: (a, preferred) remove it (or the whole HazardousItem, see F9); (b) a real placard would
  change UN number and story.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1, as High)

### mast/05#F5 · Medium · Fissile-contents aggregate used for a non-fissile americium source
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: ApplicableRadioactiveIsotope is "The maximum activity of the radioactive contents capable of
  sustaining a nuclear fission chain reaction during carriage"; Am-241 is not fissile (IAEA SSR-6, own
  knowledge). The definition looks defective, which does not lower the severity but makes this a
  candidate for the TC findings. Same as mast/01#F3. In the invoice, F9 option (a) would remove it.
- Condition: either ApplicableRadioactiveIsotope is used only for fissile contents, or the use is
  recorded in `analysis/codelist-decisions.md` as a finding about a defective UBL definition.
- Options: (a) remove it (with the HazardousItem, F9, or stating nuclide and activity in the
  RadioactiveMaterial description) (preferred by context); (b) keep it and record the defect
  (preferred by logistics).
- Needs decision: yes
- From: logistics (F4, Low), context (F4)

### mast/05#F6 · Low · Contacts that do not fit invoicing
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact answers questions about the invoice (accounts receivable),
  the accounting customer's contact handles it on the buyer's side (accounts payable). Here they are
  Saltmere's procurement office and Selanu Telecom's sales desk. Same as mast/01#F9.
- Condition: the accounting supplier's contact is a billing or accounts-receivable contact, the
  accounting customer's an accounts-payable contact.
- Options: (a, preferred) billing contacts for both parties.
- Needs decision: no
- From: broad (F6), parties (F2)

### mast/05#F7 · Low · Selanu Telecom described differently than in the order and the waybill
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: In 01 and 03 Selanu Telecom's legal form is given in Lisavan and English with languageIDs and
  its English address renderings are tagged `en-XL`; here the legal form has one rendering without
  languageID and the English renderings are tagged `en-XB` (the issuer's country). The tags follow
  the issuer throughout the flow, which may be a convention (see mast/02#F14).
- Condition: Selanu Telecom's legal form and address renderings carry the same languageIDs in every
  example of the flow, or the issuer convention is recorded.
- Options: (a, preferred) both legal-form renderings with their tags, English renderings tagged by the
  address's country (en-XL), everywhere; (b) record the convention.
- Needs decision: yes
- From: broad (F7), parties (F3)

### mast/05#F8 · Low · Registration date 1 January 1996 shared by many companies
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date for about 25 companies in 181 examples
  (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`) reads as a
  default (no fillers). Same as mast/01#F12.
- Condition: the company's registration date is its own, or absent.
- Options: (a, preferred) the date from the company history; (b) drop it.
- Needs decision: yes
- From: parties (F4)

### mast/05#F9 · Low · Transport data for dangerous goods in the invoice
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-E,S-C`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `D/E`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The invoice requests payment for goods already shipped under their own transport documents (02,
  03) and announced with the despatch advice (04). The buyer's accounts payable do nothing with sea
  emergency schedules, road tunnel codes, placards, flash point or radioactive activity; "Packed as
  the rules require" says nothing. The full HazardousItem blocks on all three lines look copied from
  the item master (IND5). The placard and activity values are the subject of F4, F5, F10, F11, F12.
- Condition: the invoice's items carry only data that billing, tax or customs valuation uses, or the
  reason for the dangerous-goods data is visible in the invoice.
- Options: (a, preferred) remove HazardousItem from the invoice lines (the HazardousRiskIndicator can
  stay if it serves a purpose); (b) keep only the UN number if the invoice serves as a commercial
  invoice for customs.
- Needs decision: no
- From: broad (F5), context (F5)

### mast/05#F10 · Low · Placard endorsement "9A" is the lithium-battery label model
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "Text of the placard endorsement that is to be shown on the shipping
  papers" or the orange plate's lower number. "9A" is the lithium-battery label model for packages;
  it is not used for placarding and the papers show class 9 (own knowledge). Same as mast/01#F5.
- Condition: absent, or what the papers or the orange plate show for UN 3480.
- Options: (a, preferred) drop it (or the whole HazardousItem, F9); (b) `3480`.
- Needs decision: no
- From: logistics (F2), broad (part of F5)

### mast/05#F11 · Low · Activity of one detector given for the set of ten
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: "The measure of the radioactive contents during carriage"; the line is one set of ten
  detectors, 37 kBq is one detector's usual activity (own knowledge), the set holds 370 kBq. Same as
  mast/01#F4.
- Condition: the activity is that of the set, or the text says per detector, or it is absent (F9).
- Options: (a, preferred) drop it with F9; (b) 370 kBq.
- Needs decision: no
- From: broad (F8), logistics (F3), context (part of F4)

### mast/05#F12 · Low · Placard endorsements that only repeat the class (UN 2920)
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:HazardousItem/cac:SecondaryHazard/cbc:PlacardEndorsement` = `3`
- Why: Broad: "8" for the stripper repeats the class. In 01 logistics refuted the same value as the
  class shown on the papers; the merge could not settle it (mast/01#F6) and added the secondary
  hazard's "3".
- Condition: absent (F9), or an endorsement text or the orange plate's lower number, or the owner
  confirms the class-on-papers reading.
- Options: (a, preferred) drop both (with F9); (b) keep them if the reading is accepted.
- Needs decision: yes
- From: broad (part of F5)

### mast/05#F13 · Low · A mast operator classified as wired telecommunications
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120). See mast/01#F10.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes
- From: broad (F9)

## Checked and consistent
- Arithmetic (redone in the merge): 6 × 2400 = 14400.00, 1 × 180 = 180.00, 20 × 9.5 = 190.00 (base
  quantity 1 in each line's unit); sum 14770.00 = LineExtensionAmount = TaxExclusiveAmount =
  TaxInclusiveAmount (tax 0.00) = PayableAmount; the same as
  `01-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `14770.00`. No allowances,
  charges or prepayments; no freight invoiced, which agrees with CPT (seller pays carriage).
- Penalty: `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `221.55` = 1.5 % × 14770.00, matching
  PenaltySurchargePercent and the note.
- Tax: category G with "Export outside Bayvarra" at document and line level, supply type goods, under
  the seller's Upland State sales tax; seller in Bayvarra, buyer on Lisavu; 0 % and 0.00 agree; the
  order states the same treatment.
- Payment means: credit transfer to the seller's own current account at Bank of Lumeport (Marrowdale
  branch, Saltmere's town), in lume; check_ids.py passes `XB69BLUM38712001885122` and
  `RF78SEINV260719` (also in InstructionNote); PaymentTerms/PaymentMeansID 1 points to the one
  PaymentMeans; no PayeeParty or PayerParty, correctly. BLUMXBLX cannot be a real BIC (country part
  XB is not an assigned ISO 3166 code).
- References: OrderReference `ST-PO-26-0713` resolves to 01 (Order) and DespatchDocumentReference
  `SE-DA-26-0718` to 04 (DespatchAdvice); line references 1–3 and quantities 6 EA, 1 SET, 20 LTR
  agree with both.
- Roles and party data agree with 01 and 04 (apart from F7). Dates: invoice 2026-06-04 17:34, after
  the despatch advice (13:20) and the waybill (17:15).

## Considered and refuted
- `/Invoice/cbc:DefaultLanguageCode`: English for a Lisavan customer — refuted because the seller's
  language is English and the invoice is in English (from broad); a language code where a locale is
  needed — refuted because the element is the default natural language and `en` is a language code
  (from context).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode`: real-time net settlement for a cross-border
  payment — refuted because the Trade Accord payment rail named in the payment means is the world's
  regional system (from broad).
- `/Invoice/cbc:PaymentCurrencyCode`: redundant with DocumentCurrencyCode — refuted because the buyer
  is on Lisavu (coral), so stating that payment is in lume has a reason (from money).
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode`: SHAR for a cross-border payment — refuted, shared
  charges is the usual choice and nothing in the flow says otherwise (from money).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID`: the seller's
  sales-tax number on an invoice taxed at 0 % for export — refuted because the seller's tax
  registration belongs on its invoice whatever the tax treatment (from parties).

## Changed in the merge
- broad/F1 (decision yes) and money/F1 (decision no) → F1: decision no, because 15 of the 16 other
  XB-STD invoices with this note are due after exactly 30 days, so Saltmere's standard terms are
  established.
- context/F2 (Medium), broad/F4 (Low, decision yes), money/F2 (Low) → F3: Medium, because the
  aggregate is used for a meaning other than its definition; decision no (removing a filler does not
  change the story).
- context/F1 (High) → F4: Medium, as mast/01#F1.
- logistics/F4 (Low, decision yes), context/F4 (Medium, decision no) → F5: Medium, decision yes, as
  mast/01#F3; the per-detector part went to F11.
- broad/F5 split: its 9A part merged with logistics/F2 into F10, its "8" part into F12 (Low, decision
  yes, as mast/01#F6, secondary hazard added), the rest merged with context/F5 into F9; decision yes →
  no; the empty note added from broad's XPath list.
- broad/F7 (decision yes), parties/F3 (decision no) → F7: decision yes, as mast/02#F14.
- broad/F3, parties/F1, context/F3 → F2; broad/F6, parties/F2 → F6; broad/F8, logistics/F3 → F11:
  combined.
