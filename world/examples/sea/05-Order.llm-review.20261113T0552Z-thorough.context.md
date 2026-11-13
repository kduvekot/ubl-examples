# LLM review: 05-Order.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/05-Order.xml`, Git blob `f1e12ba8710e50edcc4d14d6820937dec2dde266` (committed)
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

### sea/05#F1 · High · Ordered package of 24 benches, against "per pallet of four benches"
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:OrderedShipment/cac:Package/cbc:Quantity` = `24`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- Why: Package Quantity is "the quantity of items contained in this package": the order asks for
  pallets (PX) of 24 benches each. The same line's transaction conditions sell the bench per pallet
  of four, the catalogue it orders from packs four per pallet
  (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Package/cbc:Quantity`
  = `4`), and the bill of lading carries pallets of four
  (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[1]/cbc:TotalPackageQuantity`
  = `4`). 24 is the number of pallets for 96 benches, put in the element for the contents of one.
- Condition: the ordered package states four benches per pallet (and, if wanted, the number of
  pallets is given where a count of packages belongs), consistent with the conditions and the
  catalogue.
- Options: (a) preferred: Package Quantity 4 and, if the pallet count matters, a package count
  elsewhere (e.g. the shipment's handling units); (b) drop the ordered package, since the
  conditions already fix the packing.
- Needs decision: no

### sea/05#F2 · High · Emission value does not follow from its factor and base
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement", applied to
  ValueBaseMeasure; 0.82 × 1 each = 0.82, not 96 kg CO2e. (Copied from the catalogue, where the
  same contradiction stands.)
- Condition: factor × base = value in the stated units, or factor and base absent.
- Options: (a) preferred: drop factor and base (and see F4: the order need not carry the footprint
  at all).
- Needs decision: no

### sea/05#F3 · Medium · An emission boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The element is "a code signifying whether a piece of transport equipment is full, partially
  full, or empty"; cradle-to-gate is a footprint boundary and an ordered bench has no transport
  equipment fullness.
- Condition: no FullnessIndicationCode on the item's emission.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/05#F4 · Low · The order repeats the seller's catalogue description of the item
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:EmissionStandardReference` = `Greenhouse Gas Protocol Product Standard`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: An Order is "used to order goods and services"; the item is identified by buyer's, seller's,
  manufacturer's and standard identifiers and by a reference to the catalogue it comes from. Keywords
  ("assigned by the seller party"), warranty text, test method, emission calculation and the
  circularity profile are the seller's catalogue content; the buyer orders nothing by them and the
  seller learns nothing from them. Line 2, ordering from the same catalogue, carries none of this.
- Condition: the ordered item carries what identifies and specifies the order (identifiers,
  catalogue reference, the chosen colour), not a copy of the catalogue description, or the order
  states why the buyer restates it (e.g. a required minimum property).
- Options: (a) preferred: reduce line 1's Item to the form of line 2 plus the chosen colour;
  (b) keep only properties the buyer requires (e.g. load capacity as a requirement).
- Needs decision: no

### sea/05#F5 · Low · Contacts of the buyer and the delivery party carry a seller's title and department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact (purchasing) and the warehouse's goods-inwards contact both have the job
  title and department of a seller's customer service. A goods-inwards contact receives goods; a
  purchasing contact buys.
- Condition: each contact's title and department fit its name and role (purchasing; goods
  receiving), or are absent.
- Options: (a) preferred: titles and departments matching the function.
- Needs decision: no

### sea/05#F6 · Low · Delivery location named as a warehouse no other document knows
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Lanoro warehouse, Selanu`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: The goods are to be delivered to Nalevi Warehousing, whose address is Lagoon Road 9, Selanu.
  The delivery location is only a description naming a "Lanoro warehouse", which occurs in no other
  example (grep over `world/examples/*/*.xml`); the despatch advice and receipt advice for this
  order deliver to Nalevi without that name. The reader cannot tell whether Lanoro is Nalevi's
  site or another place.
- Condition: the delivery location is identified (name, address or identifier) so that it is
  recognisably the place where the follow-up documents deliver.
- Options: (a) preferred: name the location as Nalevi's warehouse with its address or identifier;
  (b) drop the location and rely on the DeliveryParty's address.
- Needs decision: no

### sea/05#F7 · Medium · A language code in LocaleCode
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; the value is the
  ISO 639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a Bayvarran English locale; (b) drop it.
- Needs decision: no

### sea/05#F8 · Low · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: A gate is not a street; it matters for pickup, which the order does not arrange.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- GTINs and GLN pass their check digits (`check_ids.py`).
- 96 × 520 = 49,920.00 and 12 × 64 = 768.00; sum 50,688.00 = LineExtensionAmount, TaxableAmount and
  PayableAmount; tax 0 under the export category. (The catalogue's 3 % full-container discount is not
  applied; that is for the money lens.)
- The catalogue reference `LD-CAT-26-0124` resolves to 02-Catalogue; seller and catalogue item IDs,
  GTINs and prices agree with it.
- CIF Port of Selanu fits a sea carriage to the buyer's island; the BL repeats it.
- OriginatorCustomerParty and BeneficiaryParty (Port of Selanu, for whose harbour parks the benches
  are bought, per CustomerReference) fit their definitions; AccountingCustomerParty is the buyer.

## Considered and refuted
- `/Order/cbc:AccountingCost`: "Stock for municipal projects" while the beneficiary is the port —
  refuted: the port's parks can be a municipal project; nothing contradicts it.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason`: the buyer stating
  the seller's export exemption — refuted: the anticipated tax of an order may follow the
  catalogue's tax category.
