# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/03-Waybill.xml`, Git blob `bd3a3f9d377d18d732a5834ff59fed7e413de940` (committed)
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

### mast/03#F1 · High · ShippingOrderID holds the consignment ID, not the forwarding instructions
- XPath: `/Waybill/cbc:ShippingOrderID` = `SE-CS-26-0716`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `SE-CS-26-0716`
- XPath: `02-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `SE-FI-26-0714`
- Why: Waybill/ShippingOrderID is "An identifier (in the form of a reference number) of the Shipping
  Order or Forwarding Instruction associated with this shipment". The value is the consignment's own
  ID, which the waybill already carries; the forwarding instructions of this flow are SE-FI-26-0714.
  An identifier of one kind is used as another, and the reference does not resolve to the
  instruction the waybill executes. The pattern is common: 14 of the 19 examples with a
  ShippingOrderID set it to a consignment ID of the same document (script over `*.xml`, from broad
  and logistics).
- Condition: ShippingOrderID is the ID of the forwarding instructions or shipping order the waybill
  was issued for (here `SE-FI-26-0714`, or the forwarder's booking if the world has one), or absent.
- Options: (a, preferred) set it to SE-FI-26-0714, which links the waybill to 02; (b) remove it and
  reference the forwarding instructions through a DocumentReference, or not at all if the carrier
  never received them (they were issued to the forwarder, the waybill's receiver).
- Needs decision: no
- From: broad (F1, Medium), logistics (F1), context (F1)

### mast/03#F2 · High · The hazardous item's package holds six batteries, the handling unit six crates of one
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:Quantity` = `6`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:Package/cbc:PackagingTypeCode` = `CR`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[1]/cbc:Quantity` = `1`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:Package[6]/cbc:Quantity` = `1`
- Why: Package/Quantity is "The quantity of items contained in this package", and the hazardous item
  has at most one Package. It says one crate containing six batteries; the handling unit lists six
  crates SE-CR-1 to SE-CR-6 with one battery each. Both cannot be true; the physics (52 kg net per
  battery, 348 kg gross in all) favour one battery per crate. Same as mast/02#F1.
- Condition: the package description under the hazardous item agrees with the handling unit's
  packages (six crates of one battery each).
- Options: (a, preferred) Quantity 1 under the hazardous item's package, the six crates in
  LoadedHazardousItem/Quantity and the handling unit; (b) drop the hazardous item's package.
- Needs decision: no
- From: logistics (F2)

### mast/03#F3 · Medium · Language codes in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639)
  repeats the language and names no locale. Section 6 names this case as Medium. 213 examples
  (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent or holds a locale (e.g. `en-XB`) from a locale list, with a
  matching listID.
- Options: (a) `en-XB` from a locale list (preferred by broad and parties); (b) remove it
  (preferred by context).
- Needs decision: no
- From: broad (F3), parties (F3), context (F4)

### mast/03#F4 · Medium · Shipment gross weight leaves out the transport equipment
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `376`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:GrossWeightMeasure` = `3`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:GrossWeightMeasure` = `25`
- Why: Shipment/GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment". 348 + 3 + 25 = 376 kg: goods and packaging only. The two ULDs listed in the waybill
  (an active RKN and an AKE) are not included (tares, own knowledge: AKE about 70–80 kg, active RKN
  several hundred kilograms). For an air waybill the chargeable weight depends on this. Same as
  mast/02#F4.
- Condition: the shipment gross weight includes the tare of the listed transport equipment, or the
  376 kg is given in an element whose definition excludes the equipment.
- Options: (a, preferred) 376 kg on Consignment/GrossWeightMeasure and the shipment weight with
  tare, or left out; (b) add the ULD tares.
- Needs decision: no
- From: logistics (F3)

### mast/03#F5 · Medium · Air waybill without airports of departure and destination or flight date
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/Waybill/cbc:Description` = `A cargo-aircraft-only flight to the island.`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL209`
- Why: An air waybill must indicate the places of departure and destination (Montreal Convention
  art. 5(a); IATA AWB practice; own knowledge), and the main-carriage stage means little without them
  and a flight date. The stage gives mode, flight and aircraft only; the issue location is where the
  waybill was issued, not by definition the departure airport, and the destination is only "the
  island", the consignee's address and the distribution to Selanu Airport Cargo. The air flow's
  waybill on the same aircraft has the airports
  (`air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMA`,
  `air/04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`).
  The document's purpose depends on these places.
- Condition: the main-carriage stage has a loading and an unloading port location (Lumeport and
  Selanu airports, with their identifiers) and a requested or planned departure date.
- Options: (a, preferred) LoadingPortLocation XBLMA, UnloadingPortLocation XLSLA and a requested
  departure event, as in air/04; (b) at least the two airports.
- Needs decision: no
- From: broad (F2), logistics (F4), context (F2)

### mast/03#F6 · Medium · Battery crates exceed the cargo-aircraft limit of PI 965 Section IA
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:HazardousGoodsTransit/cbc:PackingCriteriaCode` = `PI965IA`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:GrossWeightMeasure` = `348`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:NetWeightMeasure` = `312`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:Quantity` = `6`
- Why: 348 kg / 6 crates = 58 kg per package; one battery is 312 / 6 = 52 kg. PI 965 Section IA
  allows 35 kg gross per package on cargo aircraft, more only with a State-of-Origin approval under
  special provision A99, which travels with the shipment (own knowledge). The waybill states CAO and
  PI 965 IA but no approval; a carrier accepting the waybill would have to see it. Same as
  mast/02#F5.
- Condition: each package within 35 kg gross, or the A99 approval referenced.
- Options: (a, preferred) reference the A99 approval; (b) smaller modules; (c) record differing
  world air rules.
- Needs decision: yes
- From: broad (F5, Low), logistics (F5)

### mast/03#F7 · Medium · Numbered orange plates for packaged goods carried by air
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:UpperOrangeHazardPlacardID` = `90`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:LowerOrangeHazardPlacardID` = `3480`
- Why: The elements are "The number for the upper/lower part of the orange hazard placard required on
  the means of transport". Orange plates are an ADR/RID requirement for road and rail; packages need
  plain plates, numbered ones only tanks and bulk (ADR 5.3.2.1.1, own knowledge). The waybill is the
  air carrier's document for a cargo-aircraft flight, on which no orange plate exists, so the
  definition's condition is not met. Same as mast/02#F6.
- Condition: orange-plate numbers only where the means of transport requires numbered plates.
- Options: (a, preferred) remove both; (b) none apply to packages even on a road leg.
- Needs decision: no
- From: context (F3), logistics (F7, Low), broad (part of F6)

### mast/03#F8 · Low · "Three originals", but only the consignee's original is distributed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: The note announces three originals for consignor, consignee and carrier (as the Montreal
  Convention provides). The distribution lists only the consignee's original, handed with the goods
  to Selanu Airport Cargo, and an electronic copy for the forwarder, although the forwarder is the
  waybill's receiver and acts for the consignor; the consignor's and the carrier's originals are not
  distributed. Selanu Airport Cargo appears in no other role of the flow and is not described beyond
  its name, so its role (handler at destination) is not stated. Free text and structure disagree.
- Condition: the distribution and the note agree on which originals exist and who receives them,
  and every distribution party's role is identifiable.
- Options: (a, preferred) add the consignor's original (to Bayforth as agent, or Saltmere) and note
  the carrier's kept by Kelaro; identify Selanu Airport Cargo's role; (b) reword the note.
- Needs decision: no
- From: broad (F4), parties (F4), logistics (F6), context (F5)

### mast/03#F9 · Low · Two numbers for the waybill from the same party
- XPath: `/Waybill/cbc:ID` = `KXL-WB-26-0717`
- XPath: `/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0713`
- Why: ID is "An identifier for this document, assigned by the sender", CarrierAssignedID "An
  identifier ... assigned by a carrier or its agent to identify a specific shipment". Sender and
  carrier are the same party (Kelaro Air Cargo). Broad: a reader cannot tell which is the air
  waybill number to quote, and the value "KXL-AWB-…" presents itself as the AWB number, i.e. the
  document's number; its serial 0713 is also the order's serial, which looks accidental. Against
  that, the definitions allow a document number and a separate shipment reference from the same
  party. The merge could not settle whether the two numbers are meant to differ in meaning.
- Condition: either one number, or the two numbers have a recognisable difference in meaning
  (document number against shipment reference).
- Options: (a, preferred) make CarrierAssignedID a shipment reference that does not read as the AWB
  number, or drop it; (b) explain the difference.
- Needs decision: yes
- From: broad (F9)

### mast/03#F10 · Low · Issue location named after a company, without an identifier
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: IssueLocation is "The location where this waybill was issued". "Lumeport Airport Cargo
  Terminal" is also a company elsewhere (`air/05-TransportationStatus.xml` gives the RegistrationName
  "Lumeport Airport Cargo Terminal Ltd"), and the location has no identifier, although the world
  identifies Lumeport's airport (XBLMA in air/04). Context refuted the company-name point: the name
  also names the terminal, a place. The merge accepts that the name can stand, but the missing
  identifier remains. All 7 examples with an IssueLocation name it after a company (`grep -rh
  --include='*.xml' -A3 '<cac:IssueLocation>' world/examples`, from parties).
- Condition: the issue location names the place and, where the world identifies it elsewhere,
  carries its identifier.
- Options: (a, preferred) keep or adjust the name ("Lumeport Airport, cargo terminal") and add the
  location ID; (b) keep the name alone if no identifier is wanted.
- Needs decision: no
- From: parties (F7); context refuted its company-name part (see Considered and refuted)

### mast/03#F11 · Low · Kelaro's contact: a sales name with an operations job
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Department` = `Operations`
- Why: The contact is named "Cargo sales" but its job title is operations planner in the operations
  department; name and department disagree. For the carrier issuing the waybill, operations is the
  fitting one.
- Condition: name, job title and department of the contact agree.
- Options: (a, preferred) a name such as "Cargo operations"; (b) a sales title and department.
- Needs decision: no
- From: broad (part of F8), parties (F5)

### mast/03#F12 · Low · Consignor's and consignee's contacts do not fit the transport roles
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: On a waybill the consignor's contact despatched the goods and the consignee's contact receives
  them ("Deliver against signature of the consignee") and, for dangerous goods, is notified on
  arrival. Here they are Saltmere's procurement office and Selanu Telecom's sales desk. Same as
  mast/02#F10.
- Condition: the consignor's contact handles despatch and the consignee's contact receives goods.
- Options: (a, preferred) role-specific contacts.
- Needs decision: no
- From: broad (part of F8), parties (F6)

### mast/03#F13 · Low · Registration date 1 January 1996 shared by many companies
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date for about 25 companies in 181 examples
  (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`) reads as a
  default (no fillers). Same as mast/01#F12.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes
- From: parties (F8)

### mast/03#F14 · Low · Kelaro Air Cargo described differently than in the despatch advice
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- XPath: `04-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Here Kelaro's legal form is given in Lisavan and English with languageIDs and its English
  address renderings are tagged `en-XL`; in 04 the legal form has one rendering without languageID
  and the address renderings are tagged `en-XB`. Selanu Telecom shows the same difference between
  this example and 02, 04, 05. The tags follow the issuer's country throughout the flow, which may be
  a convention (see mast/02#F14).
- Condition: each party's legal form and address renderings carry the same languageIDs in every
  example of the flow, or the issuer convention is recorded.
- Options: (a, preferred) both renderings with their tags, English address renderings tagged by the
  address's country, everywhere; (b) record the convention.
- Needs decision: yes
- From: parties (F9)

### mast/03#F15 · Low · A mast operator classified as wired telecommunications
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode` = `6110`
- Why: Masts serve wireless networks (ISIC 6120). See mast/01#F10.
- Condition: the ISIC code matches what the world says Selanu Telecom does.
- Options: (a) 6120; (b) keep if the world says so.
- Needs decision: yes
- From: broad (F10)

### mast/03#F16 · Low · The consignor named as the party to be notified of its own dangerous goods
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/Waybill/cac:ConsignorParty/cac:PartyIdentification/cbc:ID` = `20410685`
- Why: HazardousItemNotificationParty is "The Party who is notified of a Hazardous Item in this
  Consignment". It names the consignor, which declared the goods and needs no notification; a party
  to be notified would be the consignee or the destination handler (Selanu Airport Cargo, who receives
  the consignee's original). The consignor's emergency role is already the ContactParty. In 02 broad
  refuted the same finding on the reading "party notified in case of an incident", for which the
  shipper is usual; the merge could not settle which reading the definition intends. Same as
  mast/02#F15.
- Condition: the party is one that has to be told about the goods and is not their consignor, or the
  element is absent, or the incident reading is confirmed.
- Options: (a, preferred) the consignee or the destination handler; (b) remove it.
- Needs decision: yes
- From: parties (F1, Medium), context (F7)

### mast/03#F17 · Low · Freight forwarder role defined by UBL as a consolidator, but the waybill is not consolidated
- XPath: `/Waybill/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/Waybill/cbc:ConsolidatedIndicator` = `false`
- Why: UBL defines FreightForwarderParty as "The Party who combines individual smaller consignments
  into a single larger shipment (a so-called consolidated consignment or shipment) …". Bayforth does
  not consolidate here (one consignor, one consignment, not consolidated). It is the forwarder in
  the ordinary sense, which the definition does not cover. Whether this is a misuse or a too-narrow
  definition could not be settled. Same as mast/02#F11.
- Condition: either the party consolidates, or the use for a non-consolidating forwarder is recorded
  as a deliberate reading (finding on the UBL definition).
- Options: (a, preferred) keep the role and record the narrow definition for the TC write-up;
  (b) make the shipment a consolidation, which changes the story.
- Needs decision: yes
- From: context (F6)

### mast/03#F18 · Low · Reefer settings, food approvals, road data and negatives without a reason
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AirFlowPercent` = `40`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumidityPercent` = `50`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:AnimalFoodApprovedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:HumanFoodApprovedIndicator` = `false`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:TransportEmergencyCardCode` = `TEC9`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:HazardousGoodsTransit/cbc:InhalationToxicityZoneCode` = `NOTTOXIC`
- Why: The 5–35 °C range has a reason for the batteries, but air flow, humidity and "not approved for
  food" have none, and the false indicators say only what absence would say. A road emergency card
  has no use on an air waybill; an inhalation-toxicity zone of "not toxic" for a battery states
  nothing. The HazardousGoodsTransit block appears three times with the same content (equipment,
  loaded item, handling unit). No business reason (IND5/IND6). Same as mast/02#F17.
- Condition: every reefer setting, approval indicator and dangerous-goods element present applies to
  air carriage of these goods, stated once where it applies.
- Options: (a, preferred) remove them; (b) keep one with a stated reason.
- Needs decision: no
- From: broad (F6, without the orange plates, now F7, and the emergency temperature, refuted in the
  merge), context (F8)

### mast/03#F19 · Low · Packaging danger level "4" under the UN/EDIFACT 8339 list ID
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:PackagingDangerLevelCode` = `4`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[1]/cbc:PackagingDangerLevelCode` = `4`
- Why: UN/EDIFACT 8339 has, to the reviewers' knowledge, only 1, 2 and 3; the world's copy
  (`UNCL8339Code.gc`) adds "4 Not assigned". Not verifiable against the official directory (UNECE
  blocks automated access). Same as mast/02#F18.
- Condition: every code with `listID="UN/EDIFACT EDED 8339"` is in the official list; entries without
  packing group omit the element or use a world list.
- Options: (a, preferred) omit it for UN 3480 and UN 2911; (b) keep "4" if the directory has it.
- Needs decision: yes
- From: logistics (F8)

### mast/03#F20 · Low · The emergency contact party has no means of contact
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:ContactParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: ContactParty is "The individual, group, or body who is contacted in case of a hazardous
  incident associated with this item". It has only an ID and a name; the only Saltmere contact in the
  waybill is its "Bids office", weekdays 08:00–17:00. Crew and handlers need a contact reachable
  during the flight (a 24-hour number is required by several states' rules, own knowledge). The
  other two loaded items have no ContactParty. Same as mast/02#F19.
- Condition: a contact party, where given, has a means of contact reachable while the goods are in
  transit, for every hazardous item it covers.
- Options: (a, preferred) a Contact with a 24-hour emergency number, for all three items; (b) drop
  ContactParty.
- Needs decision: no
- From: parties (F2, Medium)

### mast/03#F21 · Low · Cargo-aircraft-only liquid in a closed AKE without CAO data
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cbc:Quantity` = `20`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cac:LoadedHazardousItem[2]/cac:PositionOnBoardStowage/cbc:LocationID` = `MD-6`
- Why: UN 2920 PG II in 5-L cans may fly only on cargo aircraft (PI 855: 30 L; passenger PI 851: 1 L),
  and cargo-aircraft-only class 8 packages must be accessible to the crew in flight; a closed AKE is
  not (own knowledge). The AKE's hazardous item carries no CAO status, packing instruction or
  accessibility statement, unlike the batteries. Same as mast/02#F20.
- Condition: the UN 2920 cans carry their CAO status and packing instruction, and their stowage
  allows crew access (or the document says how it is met).
- Options: (a, preferred) its own HazardousGoodsTransit (PI 855, CAO) and accessible stowage;
  (b) inner packagings of at most 1 L.
- Needs decision: yes
- From: logistics (F9)

## Checked and consistent
- Equipment, weights, quantities and stowage are identical to 02; physics as there (52 kg and 40 L per
  battery, 92 Wh/kg, 1300 kg/m³; 36 kg packaging for six crates; stripper 22–24 kg against 25 kg;
  376 kg = 348 + 3 + 25).
- Aircraft: ATR 72 freighter (ATF, the real IATA code; main deck, LD3-size containers, payload of
  several tonnes, own knowledge); MD-2 and MD-6 are main-deck positions; 376 kg plus two ULDs is well
  within the payload. The same aircraft QL-KXA flies KXL207 in the air flow. KXL is recorded as a
  fictional designator not assigned in the real lists (world/codelists/sources/icao).
- Mode 4 for the main carriage of a waybill typed AWB by an air carrier; CAO matches a freighter and
  both the UN 3480 batteries and the 5-L cans of UN 2920 PG II.
- Dates: waybill 2026-06-04 17:15, after the forwarding instructions (2026-06-03 11:57) and the
  despatch advice (2026-06-04 13:20), before the invoice (17:34).
- Roles: Kelaro Air Cargo `IC41311` sender, carrier and signatory; Bayforth Forwarding `20411644`
  receiver and forwarder (it received the instructions of 02 and booked the carriage); Saltmere
  consignor and Selanu Telecom consignee as in 02. Identifiers, names, address IDs, tax IDs, contacts
  and endpoints agree with 01, 02 and 04 (apart from F14). The aircraft's registration nationality XL
  matches the carrier's country. Shipment and consignment IDs as in 02 and 04.
- PositionOnBoardStowage belongs in the carrier's document.

## Considered and refuted
- `/Waybill/cbc:CarrierAssignedID`: not in the IATA AWB form (3-digit prefix + 8 digits) — refuted
  because the number is deliberately fictional so as not to collide with a real airline prefix (from
  broad and logistics); the remaining question is F9.
- `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name`: the consignee's original
  sent to Selanu Airport Cargo rather than the consignee — refuted because the consignee's original
  travels with the goods and is held at destination by the ground handler (from broad and parties,
  the latter at `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyIdentification/cbc:ID`);
  the remaining question is in F8.
- `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: an airline operating cargo
  aircraft described as SMALL — refuted because an island cargo airline with few aircraft can be
  small (from parties).
- `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cbc:ProperShippingName`: the waybill carries
  no goods items, so the nature of the goods might be missing — refuted because each of the three
  goods is described by proper shipping name, UN number and weights in the loaded hazardous items
  (from logistics).
- `/Waybill/cbc:AdValoremIndicator`: suspected filler — refuted because on an air waybill the
  ad valorem (declared value) indicator is a standard field on which the carrier's charges depend
  (from context). The merge notes that UBL's definition speaks of ad valorem duties; `false` fits
  that reading as well, so the refutation stands.
- `/Waybill/cac:IssueLocation/cbc:Name`: the cargo terminal is a company, not a place — refuted by
  context because it names the terminal, a place; the merge agrees on the name and kept the missing
  identifier as F10.

## Refuted in the merge
### broad/F6 (partly) · Low · Emergency temperature on an air waybill for lithium batteries
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:EmergencyTemperature/cbc:Measure` = `60`
- Broad, as one place of its F6 ("Road data and negatives without a reason on an air waybill"): an
  emergency temperature is a concept for temperature-controlled self-reactive substances and organic
  peroxides and has no business reason for lithium batteries (IND5). Condition: every dangerous-goods
  element applies to air carriage of these goods.
- Refuted because: the definition, "The threshold temperature at which emergency procedures apply in
  the handling of temperature-controlled goods", is general; the batteries travel in an active
  temperature-controlled ULD with a 35 °C maximum, and 60 °C is a plausible thermal-runaway threshold.
  Logistics and context refuted the same value in 02 on this ground. The other places of broad/F6 are
  in F7 and F18.

### broad/F7 · Low · Two ULDs of the same kind coded differently
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `AM`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:TransportEquipmentTypeCode` = `UL`
- Broad: both RKN41207K0 (temperature-controlled LD3-size) and AKE20514K0 (LD3) are ULDs; only one is
  coded as ULD. Condition: both coded as ULDs, the RKN's temperature control in the refrigeration
  elements. Option: UL for both.
- Refuted because: "Refrigerated container" describes the active RKN correctly and agrees with its
  refrigeration and power indicators; the more specific code for one ULD and the generic one for the
  other contradict nothing. Logistics and context refuted the same pair in 02.

## Changed in the merge
- broad/F1 (Medium), logistics/F1, context/F1 → F1: High, because the reference does not resolve to
  the forwarding instructions and uses one kind of identifier as another.
- broad/F5 (Low), logistics/F5 (Medium) → F6: Medium, as mast/02#F5.
- context/F3 (Medium), logistics/F7 (Low), orange-plate places of broad/F6 → F7: Medium, as mast/02#F6.
- broad/F6 → split: orange plates to F7, emergency temperature to "Refuted in the merge", the rest
  merged with context/F8 into F18; Needs decision yes → no (removing fillers does not change the story).
- broad/F8 → split: the Kelaro contact (name against department) merged with parties/F5 into F11,
  the consignor and consignee contacts merged with parties/F6 into F12.
- broad/F9 → F9: Needs decision no → yes, because the definitions allow two numbers and the merge
  could not settle whether a difference in meaning is intended.
- parties/F1 (Medium), context/F7 (Low) → F16: Low, Needs decision yes, as mast/02#F15.
- parties/F2 → F20: Medium → Low, as mast/02#F19.
- parties/F7 → F10: the company-name point weakened after context's refutation; the missing
  identifier carries the finding.
- parties/F9 → F14: Needs decision no → yes, because the tags follow the issuer's country throughout
  the flow.
- broad/F2, logistics/F4, context/F2 → F5; broad/F4, parties/F4, logistics/F6, context/F5 → F8;
  broad/F3, parties/F3, context/F4 → F3: combined, all XPaths kept.

## Outside this review
- Whether an ATR 72 freighter can take the RKN and the AKE (contour, door size) at MD-2 and MD-6
  together with the other loads of flight KXL209, and whether KXL209 runs on that day (capacity and
  timeline across documents; from broad, logistics and context).
- On-carriage from Selanu airport to the mast site under CPT (01-Order) is not shown in any transport
  document of the flow; whether and by whom it was carried belongs to the cross-document review (from
  logistics; the missing instruction is mast/02#F3).
