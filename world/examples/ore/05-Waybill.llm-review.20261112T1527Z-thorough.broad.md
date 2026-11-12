# LLM review: 05-Waybill.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/05-Waybill.xml`, Git blob `e7a36055c2d576e9c4683563c6c0c9a29856e375` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
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
- Why: ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping Order or
  Forwarding Instruction associated with this shipment". `VI-CS-26-0306` is the consignment's
  identifier ("An identifier assigned to a collection of goods"), the same value as the
  consignment ID in this waybill and in `02-TransportExecutionPlanRequest.xml`. The transport order
  of this shipment is the request `VI-TR-26-0305`
  (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID`), confirmed by the
  plan `FRC-TEP-26-0307`. An identifier of one kind is used as another (section 4.5).
- Condition: ShippingOrderID holds the identifier of a shipping order or transport instruction, or
  is absent.
- Options: (a, preferred) `VI-TR-26-0305`, the transport user's order for this train; (b) leave it
  out, since the plan is referenced already.
- Needs decision: no

### ore/05#F2 · Medium · The consignment note does not describe the goods, the wagons or the places
- XPath: `/Waybill/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/Waybill/cbc:Description` = `The ore train from the mine siding to the factory.`
- Why: a waybill is "A transport document describing a shipment"; a rail consignment note states
  what is carried, in which wagons, from where to where (CIM Art. 7 lists the description of the
  goods, the number of packages or wagons, the place and date of taking over and the place of
  delivery; own knowledge). The shipment here has only an ID, a weight and the consignee: no goods
  item or description, no wagons, no place of taking over or delivery, no date of taking over. The
  content is in free text only (`Description`), and it does not name the goods either. The plan it
  refers to does not describe the goods (`03-TransportExecutionPlan.xml`), so the information is
  nowhere in the transport documents.
- Condition: the waybill's shipment states the goods (description or commodity code, quantity), the
  wagons, and the places (and date) of taking over and delivery.
- Options: (a, preferred) a goods item with the ore's description and HS 260111, the 30 wagons as
  transport equipment, and origin/delivery with the sidings (UN/LOCODE `XUSRV` for the origin);
  (b) at least a goods description and the two places.
- Needs decision: no

### ore/05#F3 · Medium · Shipment gross weight is the net weight of the ore, without the wagons
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment". 1 788 400 kg equals the despatched ore exactly
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`); with
  30 wagons of roughly 20–25 t tare (own knowledge) the gross weight as defined would be about
  2 390–2 540 t. For the carrier the difference matters (train weight, brake calculation).
- Condition: the shipment gross weight includes the wagons, or the ore's weight is carried in an
  element defined as the goods' weight.
- Options: (a, preferred) the ore's weight as net weight or in the consignment, and the gross with
  the wagons' tare; (b) leave the gross weight out.
- Needs decision: no

### ore/05#F4 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/Waybill/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/05#F5 · Low · CIM consignment note for carriage within one country
- XPath: `/Waybill/cbc:WaybillTypeCode` = `CIM`
- XPath: `/Waybill/cbc:Name` = `Rail consignment note under the CIM uniform rules`
- Why: the CIM uniform rules (COTIF Appendix B) apply to contracts of carriage by rail where the
  place of taking over and the place of delivery are in two different member states (own knowledge).
  This carriage runs from Serravona to Ferrano, both in Urvania (`/Waybill/cac:ConsignorParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode`
  = `XU`, consignee Valdara in Ferrano, XU). Unless Urvanian law applies CIM to domestic carriage,
  the consignment note is a national one.
- Condition: the waybill type and name fit the legal regime of a domestic rail carriage, or the
  world's story says Urvania applies the CIM rules nationally.
- Options: (a) a national rail consignment note type; (b) keep CIM and record in the world's story
  that Urvanian law extends CIM to domestic carriage. Preference: (a), unless the story already
  says (b).
- Needs decision: yes

### ore/05#F6 · Low · Three originals announced, distribution lists one
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionType[2]` = `Original, with the goods: the consignee's original`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionType[2]` = `Electronic copy`
- Why: DocumentDistribution is "A list of interested parties to whom this document is distributed".
  The note names three originals (consignor, consignee, carrier), but the list has the consignee's
  original and an electronic copy for the same consignee; the consignor's original (the duplicate
  that proves handing over, the one the consignor needs) is not distributed.
- Condition: the distribution list and the note agree on who receives which original or copy.
- Options: (a, preferred) a distribution entry for the consignor's original (Serravona), and drop or
  justify the second entry for Valdara; (b) reword the note.
- Needs decision: no

### ore/05#F7 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining`
- Why: IssueLocation is "The location where this waybill was issued"; its name should be the place
  (the mine siding, UN/LOCODE `XUSRV` in the consignor's physical location), not the consignor.
- Condition: the issue location designates a place.
- Options: (a, preferred) name "Serravona mine siding" and ID `XUSRV`; (b) only the ID.
- Needs decision: no

### ore/05#F8 · Low · Contacts do not fit the roles
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver of the consignment note is the consignee, whose contact receives the train; the
  consignor's contact handles loading and the handing over. Both are sales desks.
- Condition: the receiver's contact handles goods receipt; the consignor's contact handles despatch.
- Options: (a, preferred) role-specific contacts; (b) drop job title and department.
- Needs decision: no

### ore/05#F9 · Low · Buyer's logistics service provider copied into the waybill
- XPath: `/Waybill/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics has no part in this carriage. Master data without use; 75 `*.xml` files.
- Condition: no service provider without a role in the waybill.
- Options: (a, preferred) leave it out; (b) give it a role.
- Needs decision: no

### ore/05#F10 · Low · Reference to the transport plan without its kind
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FRC-TEP-26-0307`
- Why: the reference resolves to `03-TransportExecutionPlan.xml`, but it has no `DocumentTypeCode`,
  so the receiver sees only an ID; the waybill's other references (distribution) do carry type codes.
- Condition: the reference says it is a transport execution plan.
- Options: (a, preferred) `DocumentTypeCode` `TransportExecutionPlan` from the world's document type
  list; (b) a document description.
- Needs decision: no

## Checked and consistent
- Shipment `SM-SH-26-0309`, consignment `VI-CS-26-0306`, consignor, consignee and carrier agree with
  `04-DespatchAdvice.xml` and `03-TransportExecutionPlan.xml`; the plan reference resolves.
- Issued 10 March 11:35, the first day of the service period (10–13 March); the despatch advice
  follows the same afternoon; the freight invoice (`06-Invoice.xml`) refers to this waybill.
- Signature by the carrier, the issuer of the consignment note.
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: suspected filler — refuted because the indicator
  states that no value is declared for the carriage, which a consignment note states.
- `/Waybill/cbc:CarrierAssignedID` = `FRC-CIM-26-0304`: suspected a number from another sequence —
  refuted because the carrier's shipment reference has its own numbering.
- `/Waybill/cbc:OtherInstruction` = `Deliver against signature of the consignee.`: suspected
  contradiction with "the consignee unloads" in the plan — refuted because signing for the train
  and unloading it are compatible.
