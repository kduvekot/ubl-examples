# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit e7f2d60 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/14#F1 · High · One SSCC for the last pallet and for a box inside it, with different package counts
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:ID` = `095206101230000254`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:Quantity` = `12`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:Package/cbc:PackagingTypeCode` = `BX`
- Why: An SSCC identifies one logistic unit. Pallet 25 carries it and is said to hold 12 packages
  ("the total number of packages in this transport handling unit"); the container's Package, "a
  package contained in this piece of transport equipment", carries the same SSCC and is one box
  holding 12 items ("the quantity of items contained in this package"). Either the pallet holds 12
  packages or one box of 12; and pallet and box cannot share an SSCC.
- Condition: every SSCC identifies one unit; the side frames are described once, either as 12
  packages on pallet 25 or as one box (with its own identifier) on pallet 25, with counts that agree.
- Options: (a) preferred: drop the container-level Package and keep pallet 25 with its 12 side
  frames (the castings travel unboxed on the pallet, as the packing list and 09 suggest: "load the
  castings last"); (b) keep the box with its own SSCC and set pallet 25's TotalPackageQuantity to 1.
- Needs decision: no

### sea/14#F2 · High · Shipping order and the consignment IDs assigned by consignor and forwarder are other parties' numbers
- XPath: `/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ConsignorAssignedID` = `VT-PO-26-0127`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`
- XPath: `12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- Why: ConsignorAssignedID is "an identifier for this consignment, assigned by the consignor" and
  FreightForwarderAssignedID "… assigned by the freight forwarder". VT-PO-26-0127 is Velumi's
  purchase order (05-Order), assigned by the buyer, not by the consignor Lumeway; LD-FI-26-0131 is
  Lumeway's forwarding instructions (09), a document number assigned by the consignor, not a
  consignment number of the forwarder Bayforth. The ShippingOrderID BF-FI-26-0137 is the forwarder's
  instructions to the carrier, while those instructions give LD-SH-26-0132 as their shipping order,
  and the port's status message LD-CS-26-0133 (13-TransportationStatus): three numbers for one
  shipping order.
- Condition: each assigned ID is a consignment identifier of the party the element names (or is
  absent), and the shipping order has the same number in 09, 12, 13 and 14.
- Options: (a) preferred: ConsignorAssignedID = Lumeway's consignment number LD-CS-26-0133 (or
  drop it, since it is already the consignment ID), drop FreightForwarderAssignedID or give Bayforth's
  own file number, and settle the shipping order number on BF-FI-26-0137 in the other documents;
  (b) reference the order and the instructions as document references with types instead.
- Needs decision: no

### sea/14#F3 · Medium · Goods-item count in the container given as the number of pallets
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:GoodsItem/cac:GoodsItemContainer/cbc:Quantity` = `25`
- XPath: `/BillOfLading/cac:Shipment/cbc:TotalGoodsItemQuantity` = `2`
- Why: GoodsItemContainer Quantity is "the number of goods items loaded into or onto one piece of
  transport equipment". The bill of lading has one goods item with two contained goods items, and
  the shipment counts two goods items; 25 is the number of pallets (PackagedTransportHandlingUnits).
- Condition: the GoodsItemContainer quantity equals the number of goods items in the container
  (1 or 2, consistent with TotalGoodsItemQuantity), or is absent.
- Options: (a) preferred: drop GoodsItemContainer (the goods item is already inside the container's
  TransportEquipment) or set its quantity to the goods-item count.
- Needs decision: no

### sea/14#F4 · Medium · The road trailer still attached to the container on a shipped-on-board bill
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:ID` = `BV CH 0412`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:AttachedTransportEquipment/cbc:TransportEquipmentTypeCode` = `TE`
- XPath: `/BillOfLading/cbc:Description` = `Shipped on board.`
- Why: AttachedTransportEquipment is "a piece of transport equipment attached to this piece of
  transport equipment". The trailer BV CH 0412 is the pre-carriage chassis
  (`/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:TrailerLicensePlateID`
  = `BV CH 0412`), which dropped the container at the terminal on 13 May. A container shipped on
  board a feeder ship has no road trailer attached; the trailer belongs to the pre-carriage stage,
  where it is already given.
- Condition: the container carries no attached equipment that is not with it during the carriage the
  bill covers.
- Options: (a) preferred: drop AttachedTransportEquipment.
- Needs decision: no

### sea/14#F5 · Medium · Gross weight of the shipment without its transport equipment
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: In Shipment, GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment". The same bill gives the container 7,856.4 kg gross (VGM likewise); the shipment cannot
  weigh less than its container.
- Condition: the shipment's gross weight includes the container, or is absent.
- Options: (a) preferred: 7,856.4 kg, or drop it and give the goods' gross weight on the goods item.
- Needs decision: no

### sea/14#F6 · Medium · A language code in LocaleCode (four places)
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; each is the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/14#F7 · Low · The buyer named as holder of a bill whose originals go to the forwarder
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:BillOfLadingHolderParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: BillOfLadingHolderParty is "the Party who holds the Bill of Lading". The three originals are
  sent by courier to Bayforth, as the instructions asked
  (`12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`);
  the bill is to order. At issue the holder is the shipper's side; Velumi becomes holder only when the
  originals are endorsed and handed over, which no document of the flow shows.
- Condition: the holder named is the party that holds the originals at the time of the document, or
  the element is absent.
- Options: (a) preferred: drop BillOfLadingHolderParty; (b) name Bayforth (or Lumeway).
- Needs decision: no

### sea/14#F8 · Low · Final delivery party is the buyer, while the goods are delivered to its 3PL
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:FinalDeliveryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: FinalDeliveryParty is "the final delivery party for this consignment". The goods go to Nalevi
  Warehousing's warehouse (the packing list: "Deliver to the buyer's 3PL, Nalevi Warehousing,
  Selanu"; Nalevi is notify party, logistics operator and on-carrier here). The party the goods are
  finally delivered to is Nalevi; Velumi is the consignee.
- Condition: FinalDeliveryParty is the party at whose premises the goods are finally delivered, or
  absent.
- Options: (a) preferred: Nalevi Warehousing; (b) drop it (consignee and notify party already say
  enough).
- Needs decision: no

### sea/14#F9 · Low · The insurance certificate referenced as the policy document; two partial policies
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyDocumentReference/cbc:ID` = `WS-CERT-26-0884`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- Why: PolicyDocumentReference is "a reference to the policy document"; WS-CERT-… is by its number
  a certificate under the policy WS-CP-26-4471, which is what a CIF seller provides. The same
  policy is then described twice, at consignment level (number, cover, premium, holder, beneficiary,
  no insurer) and at shipment level (no number, insurer and broker), so neither instance is a
  complete description.
- Condition: the reference to a certificate is typed as such (or the policy document is referenced),
  and the policy is described once, at one level.
- Options: (a) preferred: one InsurancePolicy at consignment level with insurer and certificate
  reference typed as an insurance certificate; (b) keep both levels, each complete.
- Needs decision: no

### sea/14#F10 · Low · Vessel master data and port requirements in a bill of lading
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:SegregatedBallastMeasure` = `2480`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:NetTonnageMeasure` = `5120`
- Why: ShipsRequirements is "information about what services a vessel will require when it arrives
  at a port"; it is addressed to a port, not to the shipper and consignee who receive a bill of
  lading. Segregated ballast and tonnages are port-dues and port-call data. They look copied from the
  vessel's master data (they recur in 15-Manifest, where they belong).
- Condition: the bill's vessel data are what identifies the vessel (name, ID, call sign, voyage).
- Options: (a) preferred: drop requirements, ballast and tonnages here.
- Needs decision: no

### sea/14#F11 · Low · Exchange rate the bill does nothing with
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: all amounts are in lume; nothing is converted or payable in corals.
- Condition: no exchange rate without an amount that needs it.
- Options: (a) preferred: drop it; (b) keep it if the collect charges at Selanu are payable in XLC,
  and state them in XLC.
- Needs decision: no

### sea/14#F12 · Low · References with only an ID
- XPath: `/BillOfLading/cac:DocumentReference/cbc:ID` = `BF-FI-26-0137`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:DocumentReference/cbc:ID` = `LD-PL-26-0134`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:BrokerAssignedID` = `TCB-26-0331`
- Why: the forwarding instructions and the packing list are referenced without a type; the broker's
  number occurs in no other example (grep over `world/examples/*/*.xml`), not even in the import
  declaration of the broker's client (19-ImportCustomsDeclaration), so it ties to nothing.
- Condition: references carry a type; the broker's ID is the one the broker uses in the flow, or is
  absent.
- Options: (a) preferred: type codes on the references; drop BrokerAssignedID or use it in 19.
- Needs decision: no

### sea/14#F13 · Low · Contacts of consignor, consignee and notify party are sales customer service
- XPath: `/BillOfLading/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:NotifyParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The notify party's goods-inwards contact and the consignee's are the ones the carrier calls on
  arrival; all three carry a sales customer-service title.
- Condition: contacts with functions that fit (shipping, goods receiving), or none.
- Options: (a) preferred: titles matching the functions.
- Needs decision: no

### sea/14#F14 · Low · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- ISO 6346 check digit of TWLU4120872 and all 25 SSCCs pass (`check_ids.py`); SSCCs run 001–025 with
  shipping marks "VELUMI SELANU / nnn of 025".
- 24 pallets × 4 benches = 96 and pallet 25 with 12 side frames agree with the order.
- CIF value 53,778.00 = 50,688.00 goods + 2,700.00 freight + 250.00 bunker + 140.00 premium; insured
  value 59,155.80 = 110 % of it. Freight prepaid agrees with the TSD's payment condition.
- VGM 7,856.4 kg = 4,106.4 kg cargo + 3,750 kg tare; weighed by the shipper (SOLAS method 2) on
  12 May, before acceptance at the terminal on 13 May.
- Stowage LocationID equals StowagePositionID 140282 and "on deck" agrees with HandlingCode DECK.
- Ports XBLMP → XLSEL agree with LoadingPort/UnloadingPort, LastExitPort/FirstArrivalPort and the
  delivery terms; policy holder Lumeway and beneficiary Velumi fit CIF.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:HandlingCode`: on-deck stowage allowed next to "Keep dry" — refuted: a closed
  general-purpose container on deck keeps the goods dry.
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount`: 53,778.00 (CIF) where the export declaration declares
  50,688.00 — refuted for this lens: a CIF value is the import customs basis at Selanu; which value a
  bill should carry is for the money lens.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:VerifiedGrossMass/cac:DocumentReference/cbc:ID`: the VGM's ID equal to its documentary
  evidence — refuted: the VGM declaration document carries that number.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ExcessAmount`: deductible and excess both 250.00 — refuted for this
  lens (money).

## Outside this review
- The bill (issued 2026-05-14 10:54, "Shipped on board in apparent good order") and the port's report
  that the container was loaded (13-TransportationStatus, issued 16:05 the same day, loading without
  a time) and the manifest's estimated departure 15 May 06:00: whether the container was on board at
  10:54 is a timeline question across documents.
