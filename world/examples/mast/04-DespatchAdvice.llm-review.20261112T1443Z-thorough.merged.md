# LLM review: 04-DespatchAdvice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/04-DespatchAdvice.xml`, Git blob `96e68e1c850420976f9df7c6ba1c6da30707cd43` (committed)
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

### mast/04#F1 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639)
  repeats Language/ID and names no locale. Section 6 names this case as Medium. 213 examples
  (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent, or holds a locale (e.g. `en-XB`) from a locale list, with a
  matching listID.
- Options: (a) `en-XB` (preferred by broad and parties); (b) remove it (preferred by context).
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### mast/04#F2 · Medium · Shipment gross weight is goods plus packaging only
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment". 376 kg is the sum of the goods' gross weights in the transport documents (348 + 3 + 25),
  without the two ULDs they travel in (mast/02#F4, mast/03#F4). The despatch advice does not describe
  the equipment, but the value it states for this shipment is not what the element means.
- Condition: the 376 kg is given in an element that excludes the transport equipment
  (Consignment/GrossWeightMeasure), or the shipment weight includes it.
- Options: (a, preferred) move the value to the consignment's gross weight; (b) leave the shipment
  weight out.
- Needs decision: no
- From: logistics (F3, Low)

### mast/04#F3 · Medium · Placard notation 7 for an excepted package that carries no label and no placard
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: PlacardNotation is the "Text of the placard notation corresponding to the hazard class of this
  hazardous item" (or the orange plate's upper number). UN 2911 excepted packages carry no class 7
  label and are not placarded; only the UN number is marked (own knowledge: SSR-6, ADR
  1.7.1.5/5.1.5.4). The item's own text says so. Same as mast/01#F1 (4 examples of this flow).
- Condition: no placard notation for the UN 2911 item, and the HazardousItem agrees with its own
  AdditionalInformation.
- Options: (a, preferred) remove it; the class is in HazardClassID; (b) a real placard would change
  UN number and story.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, as High)

### mast/04#F4 · Medium · Fissile-contents aggregate used for a non-fissile americium source
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:Name` = `Americium-241`
- Why: ApplicableRadioactiveIsotope is "The maximum activity of the radioactive contents capable of
  sustaining a nuclear fission chain reaction during carriage"; Am-241 is not fissile (IAEA SSR-6,
  own knowledge). The definition looks defective (the aggregate is UBL's only place for a nuclide and
  its activity), which does not lower the severity but makes this a candidate for the TC findings.
  Same as mast/01#F3.
- Condition: either ApplicableRadioactiveIsotope is used only for fissile contents, or the use is
  recorded in `analysis/codelist-decisions.md` as a finding about a defective UBL definition.
- Options: (a) remove it and state nuclide and activity in the RadioactiveMaterial name or
  description (preferred by context); (b) keep it and record the defect (preferred by logistics).
- Needs decision: yes
- From: logistics (F7, Low), context (F3)

### mast/04#F5 · Low · "No status" codes that say nothing
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cbc:LineStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Despatch Advice with respect to its
  original state", LineStatusCode the same for the line. "No status on document" and "Line has no
  status" state what the absence of the codes would mean; they carry no business information
  (no-filler rule, nothing implied by absence). `NoStatus` occurs in 29 examples
  (`grep -rl --include='*.xml' 'NoStatus' world/examples | wc -l`).
- Condition: DocumentStatusCode and LineStatusCode are present only with a status that means
  something for this despatch (e.g. a replacement, a cancelled line).
- Options: (a, preferred) remove them; (b) keep them only where the story gives a status.
- Needs decision: no
- From: context (F5)

### mast/04#F6 · Low · "Consignment note" for goods sent on an air waybill
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- XPath: `03-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `AWB`
- Why: The goods travel by air with Kelaro Air Cargo under an air waybill (03). A consignment note is
  the road (CMR) or rail (CIM) document; under the Montreal Convention damage is notified to the
  carrier in writing within time limits (own knowledge). The note points the consignee to a document
  that does not exist in this flow.
- Condition: the note names the transport document actually used (the air waybill) or the carrier to
  whom damage is notified.
- Options: (a, preferred) "report any damage to the carrier, on the air waybill or in writing";
  (b) drop the sentence.
- Needs decision: no
- From: broad (F3), logistics (F2), context (F4)

### mast/04#F7 · Low · Despatch advice without despatch date, expected delivery or transport reference
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-06-04`
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SE-SH-26-0715`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: A despatch advice tells the buyer what was sent and when to expect it. This one names carrier,
  shipment and consignment but has no despatch date or time (only the issue date), no estimated
  delivery, no delivery place, no packages, no flight (KXL209) and no reference to the air waybill
  (KXL-WB-26-0717, issued four hours later). The buyer cannot plan the receipt at the mast site from
  it.
- Condition: the advice states at least when the goods were despatched and when (or where) delivery
  is expected, or references the transport document that does.
- Options: (a, preferred) Shipment/Delivery with the despatch date, an estimated delivery period and
  the delivery location, plus the flight; (b) at least the despatch date.
- Needs decision: no
- From: broad (F4), logistics (F4)

### mast/04#F8 · Low · Despatch and delivery contacts do not fit the roles
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The despatch party's contact answers for the despatch, and the delivery customer's contact
  receives the goods (the note asks the recipient to "check the goods on arrival"). Here they are
  Saltmere's procurement office and Selanu Telecom's sales desk. Same as mast/01#F9.
- Condition: the despatch party's contact handles despatch and the delivery customer's contact
  receives goods.
- Options: (a, preferred) role-specific contacts.
- Needs decision: no
- From: broad (F8), parties (F2)

### mast/04#F9 · Low · Registration date 1 January 1996 shared by many companies
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date for about 25 companies in 181 examples
  (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`) reads as a
  default (no fillers). Same as mast/01#F12.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes
- From: parties (F4)

### mast/04#F10 · Low · A mast operator classified as wired telecommunications
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120). See mast/01#F10.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes
- From: broad (F10)

### mast/04#F11 · Low · Selanu Telecom and Kelaro described differently than in the order and the waybill
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `03-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road`
- XPath: `03-Waybill.xml:/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: In 01 and 03 the legal forms of Selanu Telecom and Kelaro Air Cargo are given in Lisavan and
  English with languageIDs and their English address renderings are tagged `en-XL`; here each legal
  form has one rendering without languageID and the English renderings are tagged `en-XB` (the
  issuer's country). The tags follow the issuer throughout the flow, which may be a convention; the
  merge could not settle that (see mast/02#F14).
- Condition: each party's legal form and address renderings carry the same languageIDs in every
  example of the flow, or the issuer convention is recorded.
- Options: (a, preferred) both legal-form renderings with their tags, English address renderings
  tagged by the address's country, everywhere; (b) record the convention.
- Needs decision: yes
- From: broad (F9), parties (F3)

### mast/04#F12 · Low · Kelaro's contact: a sales name with an operations job
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: The carrier's contact is called "Cargo sales" while its job title and department are
  operations; name and department disagree. Same as mast/03#F11.
- Condition: name, job title and department of the contact agree.
- Options: (a, preferred) "Cargo operations"; (b) a sales title and department.
- Needs decision: no
- From: broad (part of F8), parties (part of F2)

### mast/04#F13 · Low · Mode-specific transport data and an empty note in the despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `D/E`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The buyer receiving the goods needs to know that they are dangerous, what they are and how to
  handle them. ADR tunnel codes (road) and IMDG EmS schedules (sea fire and spillage schedules) serve
  carriers of other modes than this air shipment, and "Packed as the rules require" says nothing
  (IND5). Context refuted the EmS value: the advice accompanies dangerous goods to the consignee, who
  handles them on arrival. The merge agrees for hazard identification and the ERG guide, not for sea
  schedules and road tunnel codes, which the consignee does nothing with. The merge added the tunnel
  code of line 3.
- Condition: the advice's dangerous-goods data serves the receiver, or each element has a stated
  reason.
- Options: (a, preferred) keep UN number, class, proper shipping name, ERG guide and the handling
  notes, drop tunnel codes, EmS and the empty note; (b) keep them with a reason.
- Needs decision: no
- From: broad (F6); refuted in part by context (see Considered and refuted)

### mast/04#F14 · Low · Placard endorsement "9A" is the lithium-battery label model
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- Why: PlacardEndorsement is the "Text of the placard endorsement that is to be shown on the shipping
  papers" or the orange plate's lower number. "9A" is the lithium-battery label model for packages;
  it is not used for placarding and the papers show class 9 (own knowledge). Same as mast/01#F5.
- Condition: absent, or what the papers or the orange plate show for UN 3480.
- Options: (a, preferred) drop it; (b) `3480` for the orange-plate reading.
- Needs decision: no
- From: broad (part of F5), logistics (F5)

### mast/04#F15 · Low · Activity of one detector given for the set of ten
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: "The measure of the radioactive contents during carriage"; the line is one set of ten detectors
  ("One set of ten for the equipment room"), 37 kBq is one detector's usual activity (own knowledge),
  the set holds 370 kBq. Far below the excepted-package limits. Same as mast/01#F4.
- Condition: the activity is that of the set, or the text says per detector.
- Options: (a, preferred) 370 kBq; (b) "per detector".
- Needs decision: no
- From: broad (F7), logistics (F6), context (part of F3)

### mast/04#F16 · Low · Placard endorsements that only repeat the class (UN 2920)
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cac:SecondaryHazard/cbc:PlacardEndorsement` = `3`
- Why: Broad: "8" repeats the class given in PlacardNotation. In 01 logistics refuted the same value
  as the class shown on the papers; the merge could not settle it (mast/01#F6) and added the secondary
  hazard's "3".
- Condition: absent, or an endorsement text or the orange plate's lower number, or the owner confirms
  the class-on-papers reading.
- Options: (a, preferred) drop both; (b) keep them if the reading is accepted.
- Needs decision: yes
- From: broad (part of F5)

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `ST-PO-26-0713` resolves to mast/01 (an Order); order
  line references 1–3 exist there; delivered quantities 6 EA, 1 SET, 20 LTR equal the ordered ones.
- Line notes against the data: "Six packs" = 6 EA; "One set of ten" = 1 SET; "Four cans of five
  litres" = 20 LTR.
- Back-up time (figures from the document, load from own knowledge): 6 × 4.8 kWh = 28.8 kWh; over four
  hours 7.2 kW at full discharge, about 5.8 kW at 80 % usable: plausible for a mast site (2–8 kW).
- Shipment SE-SH-26-0715 and consignment SE-CS-26-0716 as in 02 and 03; the carrier is the waybill's.
- Roles: Saltmere despatch supplier and seller, Selanu Telecom delivery customer and buyer, matching
  01; identifiers, names, address IDs, tax ID, contacts and endpoints agree with 01–03 (apart from F11).
- Dates: issued 2026-06-04 13:20, after the order (2026-06-01) and the forwarding instructions
  (2026-06-03), before the waybill (17:15) and the invoice (17:34).

## Considered and refuted
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: "DELIVERY" for an advice sent at despatch — refuted
  because the code types the despatch as a delivery to the customer; nothing presents it as a
  confirmation of receipt (from broad, logistics and context).
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:WebsiteURI`: the carrier's full
  master data copied into a despatch advice — refuted because the advice tells the recipient who
  carries the goods, and an identifiable carrier with its contact is useful to the recipient (from
  parties).
- `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode`: transport data the despatch advice
  does nothing with — refuted by context because the advice accompanies dangerous goods to the
  consignee, who handles them on arrival; the merge disagrees for the sea EmS schedule and the road
  tunnel codes and kept them in F13.

## Changed in the merge
- logistics/F3 (Low) → F2: Medium, because the value does not carry the element's meaning, as
  mast/02#F4 and mast/03#F4.
- context/F1 (High) → F3: Medium, as mast/01#F1.
- logistics/F7 (Low, decision yes) and context/F3 (Medium, decision no) → F4: Medium, decision yes, as
  mast/01#F3; the per-detector part went to F15.
- broad/F5 split into F14 (9A, with logistics/F5) and F16 (the "8", Low with decision yes, as
  mast/01#F6; secondary hazard added).
- broad/F6 → F13: Needs decision yes → no (removing fillers does not change the story); tunnel code of
  line 3 added; context's refutation recorded.
- broad/F8 and parties/F2 split into F8 (despatch and delivery contacts) and F12 (Kelaro's contact,
  name against department), as in mast/03.
- broad/F9 (decision yes) and parties/F3 (decision no) → F11: decision yes, as mast/02#F14.
- broad/F2, parties/F1, context/F2 → F1; broad/F3, logistics/F2, context/F4 → F6; broad/F4,
  logistics/F4 → F7: combined, all XPaths kept.
