# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/01-Order.xml`, Git blob `a15e986388f03b87c705a9a004911992c536b517` (committed)
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

### mast/01#F1 · Medium · Placard notation 7 on an excepted package that carries no label
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "text of the placard notation corresponding to the hazard class of
  this hazardous item". UN 2911 (radioactive material, excepted package – instruments or articles)
  carries no class 7 label and no placard (own knowledge: SSR-6, ADR 5.1.5.4, IATA DGR 10.5); the
  item's own additional information says so. Stating a placard notation for it contradicts that
  text. The same pair occurs in 02, 04 and 05 of this flow.
- Condition: no placard notation is given for the UN 2911 item, or the text explains what the
  notation is for.
- Options: (a, preferred) drop PlacardNotation for UN 2911; (b) keep the class only in HazardClassID,
  which already says 7.
- Needs decision: no

### mast/01#F2 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; a locale
  combines language and region (e.g. en-XB). The value is the ISO 639 language code again, with
  listID ISO 639, so it adds nothing to the Language ID and is not a locale. 213 examples carry
  `<cbc:LocaleCode listID="ISO 639">en<` (grep -rl --include='*.xml').
- Condition: LocaleCode, if present, is a locale (language plus region) from a locale list, or it
  is absent.
- Options: (a, preferred) `en-XB` with a locale list (e.g. BCP 47); (b) drop it.
- Needs decision: no

### mast/01#F3 · Low · Placard endorsement repeats the class or gives the label model
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- Why: PlacardEndorsement is the "text of the placard endorsement that is to be shown on the
  shipping papers", or the lower number of the orange plate. "9A" is the model number of the
  lithium-battery hazard label, not an endorsement and not shown on papers; for UN 2920 the value
  "8" just repeats the class already in PlacardNotation (the orange plate's lower number would be
  2920).
- Condition: PlacardEndorsement is absent or holds an endorsement text (or, for road, the UN
  number on the orange plate).
- Options: (a, preferred) drop it in the order; (b) if a lithium-battery label must be stated, use
  the label element or text that means a label.
- Needs decision: no

### mast/01#F4 · Low · Carriage data for road and sea in a purchase order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:MedicalFirstAidGuideCode` = `147`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `D/E`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The buyer orders the goods; it needs to know that they are dangerous (HazardousRiskIndicator,
  UN number). IMDG EmS schedules, ERG guide numbers and ADR tunnel codes serve the carrier of a
  particular mode, and the goods go by air (state of charge for "the air rules"). "Packed as the
  rules require" says nothing. They look copied from the item's dangerous-goods master data
  (IND5).
- Condition: the order's hazardous-item data is limited to what the buyer uses, or each element
  has a reason in the order.
- Options: (a, preferred) keep UN number, class and proper shipping name, drop the mode-specific
  codes and the empty note; (b) keep them and say in the order why the buyer needs them.
- Needs decision: yes (affects coverage)

### mast/01#F5 · Low · Activity of the americium sources: per detector or for the set?
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: The line is one set of ten detectors, "each with a small americium-241 source". 37 kBq
  (1 µCi) is the typical activity of one detector (own knowledge); the set would hold 370 kBq. The
  element is "the measure of the radioactive contents during carriage", i.e. of the whole item. Its
  parent ApplicableRadioactiveIsotope is defined by UBL as "the maximum activity of the radioactive
  contents capable of sustaining a nuclear fission chain reaction", which Am-241 in detectors is
  not; that definition is a model defect worth recording.
- Condition: the activity stated is that of the item as ordered (the set), or the text says it is
  per detector.
- Options: (a, preferred) 370 kBq for the set; (b) a note "per detector".
- Needs decision: no

### mast/01#F6 · Low · Contacts that do not fit buyer and seller
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: The buyer's contact is Selanu Telecom's sales desk for business customers, the seller's is
  Saltmere's procurement (its buying side). In an order the buyer's contact buys and the seller's
  contact sells. The same contacts are used for Saltmere in 9 and for Selanu Telecom in 8 examples
  (grep -rl '<cbc:Name>Bids office' / 'Business accounts' --include='*.xml'), whatever the role.
- Condition: the buyer's contact is a purchasing function and the seller's a sales or order
  function.
- Options: (a, preferred) role-specific contacts per party; (b) drop the contacts.
- Needs decision: no

### mast/01#F7 · Low · A mast operator classified as a wired telecom
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Selanu Telecom buys back-up batteries for a telecom mast; masts serve wireless networks
  (ISIC 6120, wireless telecommunications activities). 6110 is wired telecommunications. A mixed
  operator may have 6110 as main activity, which the world would have to say.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep 6110 if the world makes it a wired operator with radio masts.
- Needs decision: yes

### mast/01#F8 · Low · CPT without a named place
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu Telecom, mast site`
- Why: CPT is "carriage paid to (named place of destination)"; the place is described only as "mast
  site", without address or identifier, while the air waybill ends at the airport.
- Condition: the delivery location names a place that can be found (address or identifier).
- Options: (a, preferred) the mast site's address or the destination airport, as the parties
  agree; (b) the buyer's address.
- Needs decision: no

## Checked and consistent
- Arithmetic: 6 × 2400 = 14400; 1 × 180 = 180; 20 × 9.5 = 190; sum 14770.00 = taxable amount =
  payable; tax 0 at category G 0 %.
- 48 V × 100 Ah = 4.8 kWh, as the description says.
- Dangerous goods (own knowledge): UN 3480 class 9, EmS F-A/S-I, ERG 147, tunnel E; UN 2911 class 7,
  EmS F-I/S-S, ERG 161; UN 2920 class 8 (3) PG II, flash point 28 °C < 60 °C fits the class 3
  subsidiary, technical name given for an n.o.s. entry, EmS F-E/S-C, ERG 132, tunnel D/E. 37 kBq is
  the typical Am-241 activity of one ionisation detector.
- HS 850760, 853110, 381400 match the items; CPC 46420 and 46921 match.
- 04 and 05 refer to this order by ID ST-PO-26-0713 and its line IDs 1–3; quantities and prices agree.

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: export exemption in an order — refuted:
  the anticipated tax is part of what the buyer expects to pay; the treatment matches the invoice.
- `/Order/cac:SellerSupplierParty/cac:Party/cbc:IndustryClassificationCode`: a civil-engineering
  firm selling batteries and detectors — refuted: Saltmere builds masts and supplies their
  equipment; plausible.
