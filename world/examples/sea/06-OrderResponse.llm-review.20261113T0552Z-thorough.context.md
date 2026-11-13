# LLM review: 06-OrderResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/06-OrderResponse.xml`, Git blob `8c32d38abff802a363b6a976f771dad7ef600e7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/06#F1 · Medium · Net and gross weight measured without the parts their definitions include
- XPath: `/OrderResponse/cbc:NetWeightMeasure` = `3762`
- XPath: `/OrderResponse/cbc:GrossWeightMeasure` = `4106.4`
- Why: In an OrderResponse NetWeightMeasure is "the total net weight … (goods + packaging)" and
  GrossWeightMeasure "the total gross weight … (goods + packaging + transport equipment)". The
  values are the goods alone (3,762 kg) and goods plus pallets (4,106.4 kg): the packing list of the
  same consignment gives the container's tare as 3,750 kg and the loaded container as 7,856.4 kg
  (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure`
  = `7856.4`), i.e. 4,106.4 + 3,750. By UBL's definitions the net weight would be 4,106.4 kg and
  the gross weight 7,856.4 kg; the values follow the common trade usage (net = goods,
  gross = goods + packaging) instead.
- Condition: each weight contains what its definition in this document names, or the weights are
  absent from the order response.
- Options: (a) preferred: drop both from the order response (the seller arranges carriage under CIF;
  the buyer acts on neither, and the packing list carries them); (b) recompute them per the
  definitions; record the difference to trade usage as a finding for UBL if it is meant.
- Needs decision: no

### sea/06#F2 · Medium · Sales order number called an invoice in the payment note
- XPath: `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123`
- XPath: `/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: PaymentNote is "free-form text applying to the Payment for the owner of this account". The
  deposit is paid on acceptance, before any invoice; LD-SO-26-0123 is the seller's sales order ID of
  this response, not an invoice number (the invoice of the flow is `LD-INV-26-0147`, 22-Invoice).
  An identifier of one kind is presented as another.
- Condition: the payment note names the sales order (or the deposit), not an invoice.
- Options: (a) preferred: "Deposit, sales order LD-SO-26-0123"; (b) drop the note, since the RF
  reference already identifies the payment.
- Needs decision: no

### sea/06#F3 · Medium · A language code in LocaleCode
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; the value is the
  ISO 639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/06#F4 · Low · Packages counted as items
- XPath: `/OrderResponse/cbc:TotalPackagesQuantity` = `108`
- Why: TotalPackagesQuantity is "the total number of packages contained in the Order Response";
  108 is the number of items ordered (96 benches + 12 side frames). The goods travel on pallets of
  four (`05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:TransactionConditions/cbc:Description`
  = `Sold to trade customers only, per pallet of four benches.`), and the packing list counts 25
  handling units (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity`
  = `25`). Unless every bench and side frame is packed individually (nothing says so), 108 is not a
  number of packages.
- Condition: TotalPackagesQuantity is the number of packages, or the response states that each item
  is a package.
- Options: (a) preferred: drop it (see F1), or give the pallet count.
- Needs decision: no

### sea/06#F5 · Low · Originator document the order never mentioned
- XPath: `/OrderResponse/cac:OriginatorDocumentReference/cbc:ID` = `PS-REQ-26-0031`
- Why: OriginatorDocumentReference is "a reference to an originator document associated with this
  document". The port's request PS-REQ-26-0031 is neither in the order this responds to
  (05-Order carries no originator document reference) nor in any example of the flow; the seller
  responds with a reference it has received from nowhere.
- Condition: the originator document is known to the seller from the order (the order carries it),
  or the response does not carry it.
- Options: (a) preferred: carry it in 05-Order as OriginatorDocumentReference and keep it here;
  (b) drop it here.
- Needs decision: no

### sea/06#F6 · Low · The digital agreement given as the contract of the order
- XPath: `/OrderResponse/cac:Contract/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/OrderResponse/cac:Contract/cbc:ContractType` = `Digital trade agreement`
- Why: Contract is "a contract associated with the Order being responded to". 03-DigitalAgreement
  governs how the two parties exchange documents (processes, channels, SLA), not the sale of
  benches; the sale is governed by the transaction conditions `LD-TC-01` and the general terms
  `LD-GTC-2026`. Citing the exchange agreement as the order's contract mixes the two.
- Condition: the Contract is the commercial contract (or framework) of the sale, or is absent.
- Options: (a) preferred: drop Contract (the conditions are already referenced); (b) keep it if the
  story makes the digital agreement also the trading framework, and say so in the agreement.
- Needs decision: yes (whether the digital agreement is also the sales framework)

### sea/06#F7 · Low · Velumi's contact: purchasing name with a seller's title and department
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: the buyer's purchasing contact carries the sales department and customer-service title.
- Condition: purchasing title and department, or none.
- Options: (a) preferred: purchasing title and department.
- Needs decision: no

### sea/06#F8 · Low · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street and plays no role in the response.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- RF reference `RF41LDSO260123` and the account `XB19BLUM38712001466206` pass their check digits
  (`check_ids.py`).
- OrderReference `VT-PO-26-0127` resolves to 05-Order; lines, quantities, prices and amounts match
  it (49,920.00 + 768.00 = 50,688.00); OrderResponseCode AP with "Confirmed as ordered" and
  LineStatusCode NoStatus agree.
- The deposit: PaymentTerms Amount 10,000.00 due 2026-05-09 = PaymentMeans PaymentDueDate, and the
  note's "deposit of 10,000.00 lume" agrees.
- DeliveryTerms CIF Port of Selanu (XLSEL) and DestinationCountry XL fit the order.
- WarrantyParty (the manufacturer) and the five-year warranty period agree with the warranty text.

## Considered and refuted
- `/OrderResponse/cac:OrderLine[1]/cac:OrderLineReference/cbc:LineID`: a reference to the order line
  next to a LineItem with the same ID — refuted: in an order response the OrderLineReference is the
  usual way to tie the response line to the order line.
- `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate`:
  a promised delivery period under CIF, where delivery happens at loading — refuted: the dates
  (14–18 May) are a plausible promise of arrival to the buyer.
