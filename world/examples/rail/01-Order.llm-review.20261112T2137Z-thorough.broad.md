# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### rail/01#F1 · High · Emission value does not equal factor × base
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". With a base of 1 bench (unitCode EA) the factor gives 0.82 × 1 = 0.82 kg CO2e, not the 96 kg stated. No other quantity of the item explains the 96 either (192 benches × 0.82 = 157.4; the resources consumed, 34 + 22.5 = 56.5 kg, × 0.82 = 46.3). The same triple 96 / 0.82 / 1 EA occurs in 39 examples (counted with `grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82' world/examples`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure (in consistent units), or the factor and base are absent.
- Options: (a) preferred: keep the 96 kg per bench and set the factor to 96 per 1 EA, or drop factor and base, since the value is a per-product footprint, not an activity-based calculation; (b) state the activity the factor really applies to (e.g. kg CO2e per kg of material) with that base and a value that results from it.
- Needs decision: no

### rail/01#F2 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value comes from the world's EmissionBoundaryCode list (cradle to gate, EN 15804 A1–A3), which describes the life-cycle boundary of a product footprint, not the load state of transport equipment. A bench's manufacturing footprint involves no transport equipment whose fullness could be a parameter. The same use occurs in 39 examples (`grep -rl --include='*.xml' 'EmissionBoundaryCode">CRADLETOGATE'`).
- Condition: FullnessIndicationCode is absent here, or carries a load-state code of transport equipment that the calculation really used.
- Options: (a) preferred: drop the element; the boundary is already expressed by LifecycleStageCode/LifecycleStageDescription (see F3); (b) record the boundary as a finding about a missing UBL element (no boundary element in EmissionCalculationMethod) for the TC write-up.
- Needs decision: no

### rail/01#F3 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: In the world's LifecycleStageCode list MANUFACTURING is "Making the product (EN 15804 module A3)"; raw material supply and its transport are SOURCING (A1, A2). The description and the 96 kg cover A1 to A3 (mining, steel making, sawing and the transport between them). The code and its text equivalent disagree.
- Condition: The stage code(s) cover exactly what LifecycleStageDescription and Description say the value covers.
- Options: (a) split into two emissions (SOURCING and MANUFACTURING) if the figures exist; (b) preferred: omit LifecycleStageCode and keep the description, since the list has no single code for A1–A3; (c) narrow the description and value to A3 only.
- Needs decision: no

### rail/01#F4 · Medium · Province given in Region
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "the political or administrative division of a country", which UBL puts in CountrySubentity ("such as the name of its county, province, or state"). The Bayvarran addresses of the same examples use CountrySubentity for their states. "Province of Ferrano" in Region occurs 219 times over the examples (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`).
- Condition: An administrative province of Urvania is in CountrySubentity (and CountrySubentityCode if a code exists); Region is used only for a non-administrative region.
- Options: (a) preferred: move it to CountrySubentity, as for the Bayvarran states; (b) if the world defines Urvanian provinces as non-administrative regions, keep Region and rename the value so it does not read as an administrative unit.
- Needs decision: yes (whether Urvanian provinces are administrative divisions is a fact of the world)

### rail/01#F5 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` (listID ISO 639) is a language, the same value as Language/ID; it does not name a locale. The texts of the flow use the locale tags `en-XB` and `en-XU`. The same value occurs 362 times (`grep -rh --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: LocaleCode is absent or holds a locale (language plus country, e.g. `en-XB`) with a matching listID.
- Options: (a) preferred: `en-XB` for Lumeway (Bayvarra), with a locale listID; (b) drop LocaleCode.
- Needs decision: no

### rail/01#F6 · Medium · A gate in AdditionalStreetName
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". "Gate 3" is an access point of the business park for vehicles, not a street name, and it does not belong in the party's postal address used for mail and legal identity.
- Condition: AdditionalStreetName holds a street name or is absent; a gate, where it matters, is given in a delivery location or instructions.
- Options: (a) preferred: drop it from PostalAddress; put the gate in the delivery location where goods arrive (here the delivery goes to the rail siding, so it may not be needed at all); (b) use a dedicated address line if the world's address format requires it.
- Needs decision: no

### rail/01#F7 · Low · Buyer's contact is a sales desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: In an order the buyer's contact is the one who buys and answers questions about the order (purchasing); Lumeway's sales customer service serves Lumeway's own customers.
- Condition: The buyer's contact is a purchasing (or order) function of Lumeway.
- Options: (a) preferred: a purchasing contact for the buyer role; (b) keep the generic contact and accept it as master data (then the same remark applies to the other roles in the flow).
- Needs decision: no

### rail/01#F8 · Low · Seller's warehouse service provider copied into the order
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The order is issued by the buyer; nothing in it uses Valdara's warehousing provider (no despatch or collection details). It reads as master data of the seller copied into a document that does nothing with it.
- Condition: ServiceProviderParty appears in the order only if the order uses it (e.g. as despatch party).
- Options: (a) preferred: drop it from the order; (b) give it a role the order uses.
- Needs decision: no

### rail/01#F9 · Low · Delivery without a requested date
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The order's Delivery names only the receiving party. The requested delivery date (16 April, as in `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`) is not ordered by the buyer anywhere; the transport request takes it from nowhere in the flow.
- Condition: The order states when the buyer wants the goods (RequestedDeliveryPeriod or a promised date), or the absence is deliberate.
- Options: (a) preferred: add a RequestedDeliveryPeriod ending 2026-04-16; (b) leave it out if the world's buyer leaves timing to the seller.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 192 × 49 900 XUF = 9 580 800 XUF = LineExtensionAmount = AnticipatedMonetaryTotal/PayableAmount; tax 0 at 0 %.
- Tax category G with exemption EXP "Export of goods outside Urvania" fits a sale from Urvania to Bayvarra under DAP; the seller's VAT and the buyer's state sales tax are described consistently with the other examples.
- DAP with a delivery location "Rail siding of Lumeway Distribution, Marrowdale" agrees with the transport documents (03, 08: shunt to the Lumeway siding) and with Valdara paying the freight (02, 10).
- The order is referenced by `11-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LD-PO-26-0325`; quantity, price and item agree with the invoice.
- Lumeway and Valdara are described identically in all rail examples (address, legal entity, tax scheme, contact), apart from the `en-XB` language tags here (see refuted).
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass (check_ids.py). GS1 prefix 952 is GS1's range for demonstrations and examples.
- Physics: 34 kg steel and 22.5 kg hardwood consumed per bench; five slats of 1.8 m at about 700 kg/m³ (my knowledge) give about 3.6 l and 2.5 kg of wood each, so 22.5 kg consumed implies about 45 % sawing loss, plausible. Load capacity 450 kg over three seats is plausible for a park bench.
- Not verified: whether `XFER` is assigned in the real ISO 10383 MIC register (no register at hand).

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`: suspected a real GTIN-12 (it passes the GS1 check digit, and a GTIN-12 starting 07 is a US/Canada UPC prefix) — refuted because the schemeID is the world's own item scheme, not GS1, and the barcode symbology is Code 128, not UPC-A, so it does not claim to be a GTIN.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: suspected a rendering that is not in the language its `en-XB` tag names — refuted because the world consistently uses Italian-styled names (Ferrano, Serravona) as the established English names of Urvanian places, and this street follows that convention.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`: suspected inconsistency with the other examples, which tag Valdara's English renderings `en-XU` — refuted because the order is written by the Bayvarran buyer, for whom `en-XB` is its own English; both tags denote English.
- Bench weight against the gross weights of the transport documents (7968 kg for 192 benches = 41.5 kg each including packaging) against 56.5 kg of materials consumed — refuted because consumption includes casting and sawing losses (see Checked).
