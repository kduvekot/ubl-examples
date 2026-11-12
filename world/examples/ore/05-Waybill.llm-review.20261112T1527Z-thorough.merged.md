# LLM review: 05-Waybill.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/05-Waybill.xml`, Git blob `e7a36055c2d576e9c4683563c6c0c9a29856e375` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
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

### ore/05#F1 · Medium · Consignment ID used as shipping order ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0306`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order
  or Forwarding Instruction associated with this shipment". `VI-CS-26-0306` is the consignment's
  identifier ("An identifier assigned to a collection of goods"): the same value is the consignment
  ID in this waybill and in `02-TransportExecutionPlanRequest.xml`, `03-TransportExecutionPlan.xml`
  and `04-DespatchAdvice.xml`. The instruction the transport user gave the carrier is the request
  `VI-TR-26-0305` (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID`),
  confirmed by the plan `FRC-TEP-26-0307`, which is already referenced. An identifier of one kind
  is used as another (section 4.5). Of the 19 XML examples with a ShippingOrderID, 14 carry a
  consignment number ("-CS-") in it (`grep -rl --include='*.xml' 'ShippingOrderID>[A-Z]*-CS-'
  world/examples | wc -l`, against `grep -rl --include='*.xml' ShippingOrderID`; recounted in the merge).
- Condition: ShippingOrderID holds the identifier of a shipping order or forwarding instruction that
  exists in the flow, or is absent.
- Options: (a, preferred) `VI-TR-26-0305`, the transport user's request that instructs the carrier;
  (b) leave ShippingOrderID out, since the plan is already referenced.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### ore/05#F2 · Medium · The consignment note does not describe the goods, the wagons or the places
- XPath: `/Waybill/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/Waybill/cbc:Description` = `The ore train from the mine siding to the factory.`
- Why: a Waybill is "A transport document describing a shipment"; as a rail consignment note
  (`/Waybill/cbc:Name` = `Rail consignment note under the CIM uniform rules`) it states what is
  carried, in which wagons, where and when it was taken over and where it is to be delivered (CIM
  Art. 7, own knowledge). The shipment holds only its ID, a gross weight and the consignee: no goods
  item or description, no commodity code, no place or date of taking over, no place of delivery, no
  transport stage, no wagons. The content is in free text only, and that text does not name the
  goods either. The plan the waybill refers to does not describe the goods
  (`03-TransportExecutionPlan.xml`), so the information is in no transport document. The consignee
  is asked to check the goods and report damage on this note (`04-DespatchAdvice.xml`), which it
  cannot do against anything structured.
- Condition: the waybill's shipment states in structured form the goods (description or commodity
  code, quantity or weight), the places of taking over and delivery, the date of taking over, and the
  wagons (number and identifiers).
- Options: (a, preferred) a goods item with the ore's description and HS `260111` (as in 01/04),
  `Delivery`/`Despatch` or a rail `ShipmentStage` with the two sidings (UN/LOCODE `XUSRV` for the
  origin) and the actual taking-over time, and the 30 wagons as transport equipment or handling units
  with their numbers and loaded weights; (b) at least goods description and the two places, with a
  reference to the wagon list.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### ore/05#F3 · Medium · Shipment gross weight is the ore alone, without the wagons
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment". 1 788 400 kg equals the despatched ore exactly
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4` t);
  with 30 wagons of about 20–25 t tare each (own knowledge) the weight as defined would be about
  2 390–2 540 t. For the carrier the difference matters (train weight, brake calculation). The
  request and the plan carry the planned ore weight as consignment gross weight
  (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `1800000`).
- Condition: the shipment gross weight includes the wagons, or the ore's weight is carried in an
  element whose definition excludes the transport equipment (Consignment/GrossWeightMeasure,
  Shipment/NetWeightMeasure).
- Options: (a, preferred) `Consignment/cbc:GrossWeightMeasure` = 1 788 400 kg, as in 02/03; (b) add
  the wagons' tare to the shipment weight (loaded-train weight).
- Needs decision: no
- From: broad (F3), logistics (F3), context (F4)

### ore/05#F4 · Medium · CIM consignment note for a carriage within one country
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CIM`
- XPath: `/Waybill/cbc:Name` = `Rail consignment note under the CIM uniform rules`
- Why: the world's WaybillTypeCode list defines CIM as a consignment note under the Uniform Rules
  concerning the Contract of International Carriage of Goods by Rail; the real CIM rules (Appendix B
  to COTIF) apply where the places of taking over and delivery are in two different member states
  (own knowledge). This carriage runs from Serravona to Ferrano, both in Urvania
  (`/Waybill/cac:ConsignorParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XU`,
  consignee Valdara in Ferrano, XU). Unless Urvanian law applies the CIM rules to domestic carriage
  (which no document says), the code and the name state a legal regime that does not apply. This is
  the only XML example with WaybillTypeCode `CIM`, and the world list has no national rail type
  (CMR, CIM, AWB, CMNI, SEA).
- Condition: the waybill type and name name the regime that governs this domestic rail carriage, or
  the world states that Urvania applies the CIM rules nationally.
- Options: (a, preferred unless the story already says (b)) a type for a national rail consignment
  note (a new code in the world list) and a matching name; (b) keep CIM and record in the world's
  story that Urvanian law extends the CIM rules to domestic traffic (some real countries do similar).
- Needs decision: yes (which legal regime governs domestic rail carriage in Urvania is part of the
  world's story)
- From: broad (F5, Low), context (F3, Medium)

### ore/05#F5 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines Address/Region as "The recognized geographic or economic region or group of
  countries in which this address is located" and Address/CountrySubentity as "The territorial
  division of a country, such as a county or state, expressed as text". A province is a territorial
  division of Urvania. Bayvarran addresses in the world put their states in CountrySubentity, so the
  first-level divisions of the two countries are encoded in different elements. `<cbc:Region>Province
  of` occurs 219 times in 104 XML examples (`grep -rl --include='*.xml'` and `grep -rh … | wc -l`
  over `world/examples`, recounted in the merge).
- Condition: the province of every Urvanian address in this example is in `cbc:CountrySubentity`
  (optionally with a code) and not in `cbc:Region`, or the world states why an Urvanian province is
  a region and Region is used on purpose.
- Options: (a, preferred) move the province to CountrySubentity for all Urvanian addresses, as for
  Bayvarra, because it fits the definition and makes the countries consistent; (b) keep Region and
  record in the world why.
- Needs decision: yes (it changes the Urvanian address format in every flow and may be deliberate)
- From: broad (F4), parties (F1), context (F5)

### ore/05#F6 · Low · Three originals announced, the distribution lists one
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed".
  The note names three originals (consignor, consignee, carrier), but the list has the consignee's
  original with the goods and an electronic copy to the same consignee, which is already the
  waybill's ReceiverParty. The consignor's original (the duplicate that proves the handing over) is
  not listed; the carrier keeps its own and need not be listed.
- Condition: the distribution list and the note agree on who receives which original or copy, and
  every entry has a reason.
- Options: (a, preferred) add a distribution of an original to Serravona Mining (e.g.
  ORIGINALCOURIER or COLLECT, as the story has it), and drop or justify the second entry for
  Valdara; (b) change the note if the consignor gets no original in the story.
- Needs decision: no
- From: broad (F6), parties (F5), logistics (F4), context (F6)

### ore/05#F7 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining`
- Why: IssueLocation is "The location where this waybill was issued"; its name is the place, not
  the company. The waybill is issued by Ferrano Rail Cargo (sender, signatory) at the mine siding,
  which the consignor's physical location identifies
  (`/Waybill/cac:ConsignorParty/cac:PhysicalLocation/cbc:ID` = `XUSRV`, "The mine and its rail
  siding"). The location carries the consignor's name and no identifier.
- Condition: IssueLocation names (and preferably identifies) the place of issue.
- Options: (a, preferred) name "Serravona mine siding" with ID `XUSRV`; (b) only the ID, or the town.
- Needs decision: no
- From: broad (F7), parties (F2), logistics (F5, first half), context (F7)

### ore/05#F8 · Low · Receiver's and consignor's contacts are sales desks
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party", and it should fit the party's role here.
  Valdara Industries receives the waybill as consignee, and goods are delivered "against signature
  of the consignee"; its contact should receive the train. Serravona Mining is the consignor; its
  contact should hand the ore over at the siding. Both are sales desks copied from master data
  (Valdara's `order@valdara.example` contact is in 75 XML examples, per the parties part).
- Condition: the receiver's contact belongs to goods receiving and the consignor's to despatch or
  loading, or each is left out.
- Options: (a, preferred) role-specific contacts (Valdara goods-in, Serravona siding/loading);
  (b) leave the Contact (or job title and department) out.
- Needs decision: no
- From: broad (F8), parties (F3), context (F9)

### ore/05#F9 · Low · Party master data the waybill does nothing with
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/Waybill/cac:ConsignorParty/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: Valdara Industries is described with a share listing and a warehousing service provider
  (Castrano Logistics), which plays no role in this flow (in all eight ore examples it appears only
  inside Valdara's party); a rail consignment note uses neither. Serravona Mining's road-access
  condition does not concern a train collected at its own siding. Section 4.8 and IND5: data copied
  from master data into a document that does not use it. Castrano Logistics and the ISIN
  `XU0001042501` each occur in 75 XML examples (`grep -rl --include='*.xml'`, recounted in the merge).
- Condition: every aggregate of the parties has a use in this waybill, or the document says why it
  carries it.
- Options: (a, preferred) leave them out of this document and keep them for documents that need
  them (the siding as place of taking over belongs in the shipment, F2); (b) give them a role in the
  story (e.g. Castrano handling goods-in at Valdara) and show it in the flow.
- Needs decision: no
- From: broad (F9), parties (F4), context (F10)

### ore/05#F10 · Low · Reference to the transport plan without its kind
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FRC-TEP-26-0307`
- Why: DocumentReference is "A reference to another document associated with this document". The
  reference resolves to `03-TransportExecutionPlan.xml`, the contract basis of the carriage, but
  only by its number; it carries no `DocumentTypeCode`, while the waybill's distribution entries do.
- Condition: the reference states that it is a transport execution plan.
- Options: (a, preferred) `DocumentTypeCode` `TransportExecutionPlan` from the world's
  UBLDocumentTypeCode list (the code exists there); (b) a document description.
- Needs decision: no
- From: broad (F10), logistics (F5, second half), context (F8)

## Checked and consistent
- Shipment `SM-SH-26-0309`, consignment `VI-CS-26-0306`, consignor, consignee and carrier agree with
  `02-TransportExecutionPlanRequest.xml`, `03-TransportExecutionPlan.xml` and `04-DespatchAdvice.xml`;
  the reference `FRC-TEP-26-0307` resolves to the plan, valid 2026-03-04 to 2026-03-13.
- Issued 2026-03-10 11:35, the first day of the service window, before the despatch advice of the
  same day (15:37); the weight known at 11:35 is consistent with weighing at the siding before
  departure. The freight invoice `06-Invoice.xml` refers to this waybill.
- Physics: 1788.4 t over 30 wagons = 59.61 t per wagon (04), matching the planned 1800 t (02/03)
  within 0.64 %; 1 788 400 kg = 1788.4 t, the despatched (04) and invoiced (06, 07) quantity.
- Signature by Ferrano Rail Cargo, the carrier and issuer of the consignment note.
- Every party is described identically in all eight ore examples (identification, address, tax,
  legal and contact details); PartyIdentification = CompanyID, ElectronicAddressID 'XU:' + that ID,
  tax and legal registration names equal; legal forms, sizes and liquidation statuses fit companies.
- `check_ids.py`: the ISIN `XU0001042501` has a correct check digit.
- DistributionTypeCodes fit their texts in both languages; ELECTRONICCOPY fits a copy whose paper
  original travels with the goods.
- No freight charges on the note: the bill-to party is fixed in the plan
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` =
  `Valdara Industries`), and `06-Invoice.xml` bills Valdara accordingly.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: suspected filler — refuted because a domestic rail
  carriage bears no ad valorem duty and the freight is per tonne (`06-Invoice.xml`), and on a
  consignment note it states that no value is declared for the carriage; `false` is a real statement
  (from broad, money, logistics, context).
- `/Waybill/cbc:ConsolidatedIndicator` = `false`: refuted, a carrier's note for one consignment is
  not consolidated (from context).
- `/Waybill/cbc:CarrierAssignedID` = `FRC-CIM-26-0304`: suspected a second number from another
  sequence — refuted because it is defined as the carrier's reference for the shipment, which can
  differ from the document number (from broad, context).
- `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`: suspected
  contradiction with "the consignee unloads" in the plan, or an instruction that could be structured
  — refuted because signing for the train and unloading it are compatible, and UBL has no structured
  element for proof-of-delivery requirements on a waybill (from broad, context).
- The note states no freight charges or who pays them, although the Waybill definition mentions
  charges — refuted: the elements are optional, the bill-to party is fixed in the plan, and FCA terms
  (`01-Order.xml`) make the buyer pay (from money).
- `/Waybill/cbc:IssueDate` = `2026-03-10` as the start of the 30-day freight payment term of the plan,
  which the freight invoice does not follow — a finding of `06-Invoice.xml`, not here (from money).
- English renderings in Italian form (`StreetName` 'Via delle Officine', 'Strada della Miniera',
  `CompanyLegalForm` 'Società urvaniana per azioni (public limited company)', `languageID` `en-XU`):
  suspected another language than the tag says — refuted because they are proper names, kept in
  their local form, with an English gloss for the legal form (from parties).
- Telephone numbers starting with `+999`: suspected real — refuted because E.164 country code 999 is
  reserved and unassigned (own knowledge; from parties).
- Valdara's `AdditionalPartyIdentification` `0990:10427` with schemeID `ISO 6523`: suspected real
  ICD — refuted on knowledge of the ICD register, where 0990 is not assigned; not checked against the
  register itself (from parties).
- Ferrano Rail Cargo's `EntitySizeCode` `SMALL`: suspected too small for a 30-wagon ore operator —
  refuted because nothing in the flow states staff or turnover (from parties).
- `/Waybill/cac:ConsignorParty`: suspected that under CIM the consignor is the contracting party
  (Valdara, transport user under FCA) — refuted because UBL defines the consignor as "The Party who
  is reponsible for sending the goods", Serravona Mining; the contracting party is in the plan (from
  parties).

## Changed in the merge
- broad/F5 (Low) + context/F3 (Medium) → F4 Medium: a code whose list meaning (international
  carriage) does not fit the document's situation is a meaning other than the element's
  definition (section 6); kept Needs decision: yes.
- broad/F4, context/F5 (Needs decision: no) + parties/F1 (yes) → F5 Needs decision: yes, because
  the change touches the Urvanian address format in every flow and may be deliberate.
- logistics/F5 (issue location and reference in one finding) split into F7 and F10, because they are
  two different problems at different places.
- F1, F2, F3, F6–F10: wording and evidence combined from all parts; counts recounted (104 files, 219
  occurrences; 14 of 19; 75 and 75).

## Outside this review
- When the train arrived at the factory, and so whether the bonus or the penalty of
  `03-TransportExecutionPlan.xml` applies, is recorded in no document of the flow (timeline across
  documents; from logistics).
