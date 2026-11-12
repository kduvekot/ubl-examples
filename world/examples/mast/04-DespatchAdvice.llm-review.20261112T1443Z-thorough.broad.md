# LLM review: 04-DespatchAdvice.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/04-DespatchAdvice.xml`, Git blob `96e68e1c850420976f9df7c6ba1c6da30707cd43` (committed)
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

### mast/04#F1 · Medium · Placard notation 7 on an excepted package that carries no label
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:PlacardNotation` = `7`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Excepted package: no radioactive label, the UN number on the package.`
- Why: UN 2911 excepted packages carry no class 7 label or placard (own knowledge); the item's own
  text says so, the placard notation says otherwise.
- Condition: no placard notation for the UN 2911 item.
- Options: (a, preferred) drop it.
- Needs decision: no

### mast/04#F2 · Medium · A language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639)
  is a language. 213 examples carry it.
- Condition: a locale (e.g. en-XB) or absent.
- Options: (a, preferred) `en-XB`; (b) drop it.
- Needs decision: no

### mast/04#F3 · Low · "Consignment note" for goods sent by air
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods travel under air waybill KXL-WB-26-0717 (03); a consignment note is the road (CMR)
  or rail (CIM) document. The note points the consignee to a document that does not exist in this
  shipment.
- Condition: the note names the transport document of this shipment (the air waybill), or no
  document.
- Options: (a, preferred) "on the air waybill"; (b) drop the document name.
- Needs decision: no

### mast/04#F4 · Low · No despatch date and no link to the transport
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SE-SH-26-0715`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: The advice tells the buyer what was despatched and how; it names the carrier but gives
  neither the despatch date (Shipment/Delivery or Despatch) nor an expected arrival nor the flight.
  The issue date is the only date. The buyer cannot plan receipt at the mast site.
- Condition: the advice gives the despatch date (or the expected delivery), and the flight or the
  transport document if known.
- Options: (a, preferred) Delivery/Despatch with actual despatch date and an estimated delivery
  period, plus the flight KXL209; (b) at least the despatch date.
- Needs decision: no

### mast/04#F5 · Low · Placard endorsement repeats the class or gives the label model
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `9A`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cbc:PlacardEndorsement` = `8`
- Why: "9A" is the model number of the lithium-battery label, not a placard endorsement shown on
  papers; "8" repeats the class given in PlacardNotation.
- Condition: PlacardEndorsement absent or an endorsement text.
- Options: (a, preferred) drop it.
- Needs decision: no

### mast/04#F6 · Low · Carriage data for road and sea in a despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:TunnelRestrictionCode` = `E`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:HazardousItem/cbc:EmergencyProceduresCode` = `F-A,S-I`
- XPath: `/DespatchAdvice/cac:DespatchLine[3]/cac:Item/cac:HazardousItem/cbc:AdditionalInformation` = `Packed as the rules require.`
- Why: The buyer receiving the goods needs to know they are dangerous and what they are; ADR tunnel
  codes and IMDG EmS for an air shipment, and an empty "packed as the rules require", have no use
  here (IND5).
- Condition: the advice's dangerous-goods data serves the receiver, or each element has a stated
  reason.
- Options: (a, preferred) keep UN number, class, proper shipping name and the handling notes;
  (b) keep and justify.
- Needs decision: yes (affects coverage)

### mast/04#F7 · Low · Activity of the americium sources: per detector or for the set?
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:HazardousItem/cac:RadioactiveMaterial/cac:ApplicableRadioactiveIsotope/cbc:ActivityLevelMeasure` = `37`
- Why: 37 kBq is one detector's typical activity; the line is one set of ten (370 kBq).
- Condition: the activity is that of the set, or the text says per detector.
- Options: (a, preferred) 370 kBq; (b) a note.
- Needs decision: no

### mast/04#F8 · Low · Contacts that do not fit the roles
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- Why: The despatching party's contact is its procurement office, the delivery customer's a sales
  desk, and the carrier's contact is called "Cargo sales" with the job title "Operations planner".
  A despatch supplier's contact ships, a delivery customer's contact receives goods.
- Condition: each contact fits its role and its name, title and department agree.
- Options: (a, preferred) role-specific contacts.
- Needs decision: no

### mast/04#F9 · Low · Lisavan address renderings tagged en-XB
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road`
- XPath: `03-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road`
- Why: The addresses of Selanu Telecom and Kelaro Air Cargo (Lisavu) are tagged `en-XB` here and
  `en-XL` in 01 and 03.
- Condition: the same address carries the same language tags in every example.
- Options: (a, preferred) tag by the address's own country.
- Needs decision: yes (the world's language convention)

### mast/04#F10 · Low · A mast operator classified as a wired telecom
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120); see the review of 01.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes

## Checked and consistent
- OrderReference ST-PO-26-0713 resolves to 01; order line references 1–3 and despatched quantities
  (6 EA, 1 SET, 20 LTR) equal the ordered ones.
- Line notes: six packs × 4.8 kWh = 28.8 kWh, four hours at about 7.2 kW, a plausible load for a
  mast site with several operators (own knowledge, typical 2–8 kW); four 5-L cans = 20 L.
- Shipment and consignment IDs and gross weight 376 kg agree with 02 and 03; the carrier is the one
  in 03.
- Issued 13:20 on 2026-06-04, before the waybill (17:15) and the invoice (17:34) of the same day.

## Considered and refuted
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode`: "Delivery" for a despatch — refuted: the world's
  code for a despatch advice announcing a delivery; it fits.
