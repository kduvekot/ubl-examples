# LLM review: 01-Order.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/01-Order.xml`, Git blob `a15e986388f03b87c705a9a004911992c536b517` (committed)
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

### mast/01#F1 · Medium · Placard notation 7 for an excepted package that carries no label and no placard
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "Text of the placard notation corresponding to the hazard class of
  this hazardous item. Can also be the hazard identification number of the orange placard (upper
  part) required on the means of transport." UN 2911 (radioactive material, excepted package –
  instruments or articles) carries no class 7 label, and vehicles, containers or ULDs carrying only
  excepted packages are not placarded; only the UN number is marked (own knowledge: IAEA SSR-6, ADR
  1.7.1.5/5.1.5.4, IATA DGR 10.5). The item's own AdditionalInformation says there is no label and
  only the UN number, so a placard notation states something the text next to it, rightly, denies.
  The same value is in 02, 04 and 05 of this flow (`grep -l --include='*.xml' '<cbc:PlacardNotation>7<'`
  over `world/examples/mast`: 4 files).
- Condition: no placard notation is given for the UN 2911 item, and the HazardousItem agrees with its
  own AdditionalInformation.
- Options: (a, preferred) remove PlacardNotation for this item; the class is already in
  HazardClassID and HazardousCategoryCode; (b) if a placard were really meant, the item would not be
  an excepted package, which changes UN number and story.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, as High)

### mast/01#F2 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". A locale is a
  language as used in a region (the examples themselves use `en-XB`, `en-XL` as `languageID`); `en`
  with listID ISO 639 is the language code of Language/ID again and names no locale. Section 6 of the
  review rules names this case as Medium. The same value occurs in 213 examples
  (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent, or holds a locale (language plus territory, e.g. `en-XB`) from a
  locale list, with a matching listID.
- Options: (a) a locale such as `en-XB` with a listID naming BCP 47 or the world's locale list
  (preferred by broad and parties: Saltmere uses Bayvarran English, consistent with the `en-XB`
  languageIDs); (b) remove LocaleCode, since Language/ID already says English and nothing in the
  document depends on a locale (preferred by context). The merge prefers (a) where the world has a
  reason to state the locale, else (b).
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### mast/01#F3 · Medium · Fissile-contents aggregate used for a non-fissile americium source
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: UBL 2.5 defines RadioactiveMaterial/ApplicableRadioactiveIsotope as "The maximum activity of
  the radioactive contents capable of sustaining a nuclear fission chain reaction during carriage".
  Americium-241 in smoke detectors is not fissile material (the fissile nuclides of the transport
  regulations are U-233, U-235, Pu-239 and Pu-241; IAEA SSR-6, own knowledge), so the definition's
  condition is not met. The aggregate is at the same time the only place in UBL to give a nuclide
  and its activity, and its type (Radioactive Isotope) suggests a general use, so the definition
  looks defective; under the semantic-conformance rule this does not lower the severity, but it makes
  the case a candidate for the findings to the UBL TC.
- Condition: either ApplicableRadioactiveIsotope is used only for fissile contents (and the
  americium activity, if stated, is in an element whose definition covers it), or the use is
  recorded in `analysis/codelist-decisions.md` as a finding about a defective UBL definition.
- Options: (a) remove ApplicableRadioactiveIsotope and state nuclide and activity in the
  RadioactiveMaterial name or description (e.g. "10 × 37 kBq Am-241") (preferred by context: it
  conforms to the definition as written); (b) keep the element and record the definition defect for
  the TC write-up (preferred by logistics). The merge leaves the choice to the owner, because it
  decides between the semantic-conformance rule and a model finding.
- Needs decision: yes
- From: logistics (F4, Low), context (F3), broad (part of F5)

### mast/01#F4 · Low · Activity of one detector given for the set of ten
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cbc:Description` = `Ten ionisation smoke detectors for the mast's equipment room, each with a small americium-241 source.`
- Why: ActivityLevelMeasure is "The measure of the radioactive contents during carriage". The item
  is one set of ten detectors, each with a source; 37 kBq (1 µCi) is the usual activity of one
  ionisation detector (own knowledge), so the set holds 10 × 37 = 370 kBq. The value under-states the
  item's contents by a factor of ten or leaves the reader to guess that it is per detector. Both
  figures are far below the excepted-package limits (Am-241 A2 = 1 × 10⁻³ TBq; instrument limit
  10⁻² A2 = 10 MBq; package limit A2 = 1 GBq; own knowledge), so the classification is not affected.
- Condition: the activity stated is that of the item as ordered and carried (370 kBq for the set),
  or the text says that it is per detector.
- Options: (a, preferred) 370 kBq for the set; (b) keep 37 and say "per detector" in the material's
  name or description.
- Needs decision: no
- From: broad (F5), logistics (F3), context (part of F3)

### mast/01#F5 · Low · Placard endorsement "9A" is the lithium-battery label model
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "Text of the placard endorsement that is to be shown on the shipping
  papers for this hazardous item. Can also be used for the number of the orange placard (lower part)
  required on the means of transport." "9A" is the model number of the lithium-battery hazard label
  on packages; under ADR and IMDG the 9A model is not used for placarding (the placard is model 9),
  and the shipping papers show class 9 (own knowledge). The orange-plate lower number would be 3480.
  The same value is in 4 examples of this flow (grep `'<cbc:PlacardEndorsement>9A<'` over `*.xml`).
- Condition: PlacardEndorsement is absent, or holds what the shipping papers or the orange plate show
  for UN 3480; a 9A label, if it is to be stated, is stated as a package label.
- Options: (a, preferred) drop PlacardEndorsement (the class is in PlacardNotation and HazardClassID);
  (b) `3480` if the orange-plate reading is intended.
- Needs decision: no
- From: broad (F3), logistics (F2), context (part of F4)

### mast/01#F6 · Low · Placard endorsements that only repeat the class (UN 2920)
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cac:SecondaryHazard/cbc:PlacardEndorsement` = `3`
- Why: Broad held that "8" only repeats the class already in PlacardNotation and that, read as the
  orange plate's lower number, it would be 2920. Logistics refuted this: the class shown on the
  shipping papers is a legitimate reading of "the placard endorsement that is to be shown on the
  shipping papers". The merge could not settle it: the definition does not say what an endorsement
  is beyond its two readings, and under neither reading is it the class number (the orange plate's
  lower part is the UN number; an endorsement on papers is, in the merge's understanding, an
  additional text such as a subsidiary-risk or "inhalation hazard" wording, own knowledge). The
  merge added the secondary hazard, which repeats its class 3 in the same way.
- Condition: either PlacardEndorsement is absent or holds an endorsement text or the orange plate's
  lower number, or the owner confirms that the class on the papers is the intended reading.
- Options: (a, preferred) drop both PlacardEndorsement values, since the classes are already in
  PlacardNotation; (b) keep them if the class-on-papers reading is accepted.
- Needs decision: yes
- From: broad (part of F3); refuted by logistics (Considered and refuted); SecondaryHazard added in the merge

### mast/01#F7 · Low · Mode-specific transport data in the buyer's order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:MedicalFirstAidGuideCode` = `147`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `State of charge below 30 %, as the air rules require.`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `D/E`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:MaritimePollutantCode` = `N`
- XPath: `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The order is the buyer's request to buy. Under `/Order/cac:DeliveryTerms/cbc:ID` = `CPT` the
  seller arranges and pays the carriage, and the order names no mode; IMDG EmS schedules, ERG guide
  numbers, ADR tunnel codes, the marine-pollutant status and the state of charge "as the air rules
  require" are data of the consignor and the carrier of a given mode (the goods later go by air and
  sea, not by road). "Packed as the rules require" says nothing. The data looks copied from the
  item's dangerous-goods master data into a document that does nothing with it (IND5). The UN
  number, class, proper shipping name and the hazardous indicator, which tell the seller what kind
  of goods is ordered, have a reason. The placard data of lines 1–3 is the subject of F1, F5 and F6.
- Condition: the order's HazardousItem carries only what the buyer needs to identify what is ordered
  (e.g. UN number, class, proper shipping name), or each element has a reason visible in the order.
- Options: (a, preferred) reduce the HazardousItem to identification (UNDGCode, HazardClassID,
  ProperShippingName) and keep the transport data in the forwarding instructions and waybill;
  (b) keep it with a stated reason (e.g. the buyer prescribes air carriage, which the order would
  then say).
- Needs decision: no
- From: broad (F4), context (F4)

### mast/01#F8 · Low · CPT named place described only as "mast site"
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu Telecom, mast site`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Selanu Telecom`
- Why: CPT is "carriage paid to (named place of destination)": the place decides how far the seller
  must arrange carriage (here: beyond the destination airport to the mast). The place is described
  only by the buyer's name and "mast site", without address or identifier, and Selanu Telecom
  presumably has more than one mast; neither the location nor the DeliveryParty carries an address.
  The consignee's address appears only in the transport documents
  (`02-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`),
  and nothing says whether the mast site is that address. A location's description should be the
  place, not the company.
- Condition: the delivery location of the CPT term identifies the place (address or location ID), so
  that the transport documents can be checked against it.
- Options: (a, preferred) give DeliveryLocation the mast site's name and address; (b) if the mast
  site is the buyer's business address on Mast Hill Road, say so.
- Needs decision: no
- From: broad (F8), parties (F4), logistics (F5); context refuted it (see Considered and refuted)

### mast/01#F9 · Low · Buyer's and seller's contacts fit the opposite roles
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- Why: In an order the buyer's contact buys and the seller's contact sells. The buyer, Selanu
  Telecom, is represented by its sales desk for business customers, and the seller, Saltmere
  Engineering, by a procurement officer of its procurement department (its buying side). Each
  contact fits the opposite role. The same contacts are used for Saltmere in 9 and for Selanu
  Telecom in 8 examples, whatever the role (`grep -rl --include='*.xml' '<cbc:Name>Bids office'` and
  `'<cbc:Name>Business accounts'` over `world/examples`).
- Condition: the buyer's contact is a purchasing person or desk of Selanu Telecom, and the seller's
  a sales or order-handling person or desk of Saltmere Engineering.
- Options: (a, preferred) role-specific contacts per party; (b) if the "Bids office" is Saltmere's
  tendering (sales) office, make job title and department say so; (c) drop the contacts.
- Needs decision: no
- From: broad (F6), parties (F2)

### mast/01#F10 · Low · A mast operator classified as wired telecommunications
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Selanu Telecom buys back-up batteries for a telecom mast; masts serve wireless networks
  (ISIC Rev.4 6120, wireless telecommunications activities; own knowledge). 6110 is wired
  telecommunications. A mixed operator may have 6110 as its main activity, which the world would
  have to say.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep 6110 if the world makes it a wired operator that also runs masts.
- Needs decision: yes
- From: broad (F7)

### mast/01#F11 · Low · The island's telecom operator described as a small entity
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: Selanu Telecom runs a mast network on the island and orders back-up power for it; a network
  operator is usually at least medium-sized. In a small island economy it could still be small, so
  this needs a decision.
- Condition: the size code matches the company's description in the world.
- Options: (a) `MEDIUM` or `LARGE` if the world describes it as the island's operator; (b) keep
  `SMALL` if the world says so.
- Needs decision: yes
- From: parties (F5)

### mast/01#F12 · Low · Registration date 1 January 1996 shared by many companies
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `1996-01-01` is the registration date of about 25 different companies (Selanu Telecom,
  Bayforth Forwarding, Kelaro Air Cargo and others) in 181 examples
  (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`). A shared
  New Year's Day for so many companies reads as a default value, not as each company's own history
  (IND5/IND6: no fillers).
- Condition: each company's registration date is its own (from its history in the world), or absent.
- Options: (a, preferred) give each company the date of its history; (b) drop the date where the
  world has none.
- Needs decision: yes
- From: parties (F3)

## Checked and consistent
- Arithmetic (redone in the merge): 6 × 2400 = 14400.00; 1 × 180 = 180.00; 20 × 9.5 = 190.00; sum
  14770.00 = LineExtensionAmount = TaxableAmount = PayableAmount; tax 0.00 at category G, 0 %.
- Battery energy: 48 V × 100 Ah = 4800 Wh = 4.8 kWh, as the description says.
- Coating stripper: 20 LTR in 5-litre cans = 4 cans (the despatch advice says four cans of five litres).
- Dangerous goods (own knowledge): UN 3480 class 9, EmS F-A,S-I, ERG 147, tunnel E; UN 2911 class 7,
  EmS F-I,S-S, ERG 161, no packing group; UN 2920 class 8 (3) PG II, flash point 28 °C (class 3 range
  23–60 °C) fits the subsidiary risk and the precedence table, technical name given for an n.o.s.
  entry, EmS F-E,S-C, ERG 132, tunnel D/E. State of charge below 30 % matches IATA PI 965 for UN 3480.
- HS 850760, 853110, 381400 and CPC 46420, 46921 fit the items.
- Parties: Selanu Telecom `IC42407` (XL register) as buyer and delivery party, Saltmere Engineering
  `20410685` (XB register) as seller; the same identifiers, names, addresses, tax ID, contacts and
  endpoints in 02–05. Saltmere's tax registration (state sales tax STT of Upland State, TaxLevelCode
  STATE) matches its address in Upland State (`XB-UL`).
- 04 and 05 refer to this order by ID ST-PO-26-0713 and its line IDs 1–3; quantities and prices agree.

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: export exemption in an order —
  refuted because the anticipated tax is part of what the buyer expects to pay, and the treatment
  matches the invoice (from broad).
- `/Order/cac:SellerSupplierParty/cac:Party/cbc:IndustryClassificationCode`: ISIC 4290 (other civil
  engineering) for a supplier of batteries and detectors — refuted because an engineering firm that
  builds and equips telecom masts supplies their equipment (from broad and parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName`: no legal form
  for Saltmere Engineering, unlike the other companies — refuted because a firm without a company
  suffix (partnership or sole trader) is a legitimate reading, and its name is the same in every
  example (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress`: no PostalZone — refuted because no
  Lisavan address in the examples has one (from parties).
- `/Order/cac:OrderLine[3]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement`: "8" for
  UN 2920 — refuted by logistics as the primary class shown on the papers; the merge could not settle
  it and kept it as F6 (Needs decision: yes).
- `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:HazardousItem/cbc:UNDGCode`: smoke detectors
  could be exempt consumer products rather than UN 2911 — refuted because the consumer-product
  exemption applies only after sale to the end user, and 370 kBq exceeds the Am-241 consignment
  exemption limit of 10 kBq (own knowledge) (from logistics).
- `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cbc:HazardousRiskIndicator`: excepted packages are
  not "subject to an international regulation" — refuted because excepted packages remain subject to
  the transport regulations (marking, documentation limits), only with reduced requirements (from
  context).
- `/Order/cac:DeliveryTerms/cbc:ID`: CPT needs a named place — refuted by context because the
  DeliveryLocation names the mast site; the merge disagrees (the description does not identify which
  site) and kept it as F8, made by broad, parties and logistics.

## Changed in the merge
- context/F1 → F1: severity High → Medium, because the AdditionalInformation speaks of the label, not
  of the placard, so the contradiction rests on the regulations (own knowledge) rather than on a value
  of the example; the element carries a meaning that does not apply (Medium).
- logistics/F4 (Low, decision yes) and context/F3 (Medium, decision no) → F3: combined; severity
  Medium, because the element is used against its UBL definition (semantic-conformance rule: a defect
  in the definition does not lower the severity); Needs decision yes, because the choice between
  removal and a TC finding is the owner's. The per-detector activity part of context/F3 and broad/F5
  went to F4.
- broad/F3 split into F5 (9A) and F6 (the "8"); F6 is Low with Needs decision yes because logistics
  refuted it and the merge could not settle it; the SecondaryHazard PlacardEndorsement was added to F6.
- context/F4's PlacardEndorsement place moved to F5; its other places merged with broad/F4 into F7.
- broad/F4 → F7: Needs decision yes → no, because reducing the data does not change the story; the
  no-filler rule applies even if coverage drops.
- broad/F8, parties/F4, logistics/F5 → F8: combined, with the DeliveryParty place from parties.
- broad/F6, parties/F2 → F9: combined, all six contact elements cited.
- broad/F2, parties/F1, context/F2 → F2: combined; the parts' different preferred options are both kept.
