# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### air/01#F1 · High · The added line carries the ID of the order's bench line
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10443`
- XPath: `/OrderChange/cbc:Note[2]` = `Add eight side frames by air; the rest of the order is unchanged.`
- Why: An Order Change carries "(changed) Order Lines"; a LineItem ID is the buyer's identifier of the order line. In the order being changed (sea/05-Order.xml), line 1 is the 96 park benches; the side frames LD-10443 are line 2. A change line with ID `1` and 8 side frames therefore reads as replacing line 1 (96 benches) with 8 side frames, which contradicts the note that the rest of the order is unchanged. The line also has no LineStatusCode saying it is added (the UBL LineStatusCode list has `Added`; the code is used in other examples, e.g. road/02-OrderResponse.xml). The same line ID is echoed in 02-OrderResponse.xml and in the despatch lines of 06/08-DespatchAdvice.xml.
- Condition: the added air line has a line ID that does not occur in the original order (e.g. 3), or the change is expressed as a change of line 2 that the line ID and a line status make recognisable; the note and the lines agree.
- Options: (preferred) a new line ID `3` with LineStatusCode `Added`, because the note says eight frames are added by air and the sea delivery stays as ordered; or a revised line 2 (quantity 20, `Revised`) with a split delivery, which changes the story more.
- Needs decision: no

### air/01#F2 · Medium · AnticipatedMonetaryTotal holds the new order total, not the change
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `51200.00`
- XPath: `/OrderChange/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `51200.00`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`
- Why: In an Order Change, AnticipatedMonetaryTotal is "The amount of change to the total cost of the order anticipated by the buyer". The change is one line of 8 × 64 = 512.00 XBL; 51200.00 is the original order total 50688.00 (`sea/05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`) plus 512.00. The value is the new total, not the amount of change, and its LineExtensionAmount is not the sum of the line extension amounts of this document (LineCountNumeric `1`). The TaxableAmount repeats the same total for a document whose only line is 512.00.
- Condition: the monetary total and the taxable amount of the Order Change are consistent with the definition (the amount of change) and with the lines this document carries.
- Options: (preferred) 512.00 in LineExtensionAmount, PayableAmount and TaxableAmount, matching the definition and the single line; or, if the world reads the element as "anticipated new total", record that reading as a finding on the UBL definition and keep all three consistent.
- Needs decision: no

### air/01#F3 · Medium · LocaleCode holds a language code
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". A locale is a language in a region; `en` with listID `ISO 639` is the bare language code and only repeats Language/ID. Counted with grep over `world/examples/*/*.xml`: 362 LocaleCode elements, all `en` with listID ISO 639.
- Condition: LocaleCode holds a locale from a locale list, or is absent.
- Options: (preferred) drop LocaleCode where only the language is known, since Language/ID already says it; or a locale such as English as used in Bayvarra, with a listID for locales.
- Needs decision: no

### air/01#F4 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". `Gate 3` is a gate of the business park, not a street; it directs vehicles, not post, and sits in the seller's postal address in an order change that sends nothing to that gate.
- Condition: the postal address holds no gate in a street-name element; a gate, where a document needs it, is where vehicles are directed (a despatch or pickup location).
- Options: (preferred) drop it from the postal address; or move it to the location where goods are picked up, in documents that arrange a pickup.
- Needs decision: no

### air/01#F5 · Low · The Urvanian national tariff code in a Bayvarra–Lisavu order change
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The code is from `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, the national tariff of Urvania. The trade is between a Bayvarran seller and a Lisavan buyer, shipped from Bayvarra to Lisavu (DestinationCountry `XL`); Urvania is only the country of origin. Neither party, nor any authority this document reaches, uses the Urvanian tariff; it looks copied from the item master. Counted with grep over `*.xml`: 43 examples carry this list.
- Condition: the item carries the commodity classifications this document's parties use (HS, and the national tariff of the export or import country where needed), or a stated reason for the Urvanian one.
- Options: (preferred) drop the XU tariff code from the order change, keeping HS 732599; or replace it by the Bayvarran export or Lisavan import tariff code if the world has one and the order needs it.
- Needs decision: no

## Checked and consistent
- OrderReference `VT-PO-26-0127` resolves to sea/05-Order.xml (an Order of the same buyer and seller); Contract `LD-DAG-26-0125` resolves to sea/03-DigitalAgreement.xml.
- SalesOrderID `LD-SO-26-0123` is the seller's order number given in `sea/06-OrderResponse.xml:/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`.
- Price and item (64 XBL, LD-10443, GTIN check digit OK by check_ids.py) agree with line 2 of sea/05-Order.xml; 8 × 64 = 512.00.
- Delivery terms: CPT to the Selanu airport cargo terminal for the air part, with SpecialTerms stating the rest stays CIF by sea, agrees with the original CIF Port of Selanu.
- DestinationCountry `XL` and the export tax category G with reason EXP fit a Bayvarran seller shipping to Lisavu (tax treatment itself is for the money lens).

## Considered and refuted
- `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`: suspected that the buyer cannot name the carrier under CPT (the seller contracts carriage) — refuted because the buyer asks for air carriage to an island airport, Kelaro is a Lisavan air cargo carrier (XL register) and is the carrier actually used in 04-Waybill.xml; naming the expected carrier is legitimate in a delivery request.
- `/OrderChange/cac:Delivery/cac:NotifyParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: suspected redundancy with DeliveryParty — refuted because a notify party for arrival notice that is also the delivery party is normal in air cargo.
- `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`: suspected duplication with Delivery/DeliveryTerms — refuted: the document-level terms cover the change as a whole, the delivery-level terms carry the SpecialTerms about the sea part; they agree.
- `/OrderChange/cbc:CustomerReference` = `Harbour parks Selanu`: suspected misuse (purchasing card) — refuted because at document level the definition is "A supplementary reference for the transaction", with the card only as an example; a project reference fits.
- `/OrderChange/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: suspected copied data — refuted: the original order names the Port of Selanu as originator and beneficiary of the benches, and the spare frames serve the same project (AccountingCost `Stock for municipal projects`).
