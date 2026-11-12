# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/01#F1 · High · The added line reuses line ID 1, which is the bench line of the order being changed
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10443`
- XPath: `/OrderChange/cbc:Note[2]` = `Add eight side frames by air; the rest of the order is unchanged.`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cbc:ID` = `2`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10443`
- Why: OrderLine in an Order Change is "an association to one or more (changed) Order Lines", and LineItem/ID is "an identifier for this line item, assigned by the buyer", i.e. the line of the order being changed (`OrderReference/ID` `VT-PO-26-0127`, `sea/05-Order.xml`). In that order, line 1 is 96 Serra 180 park benches and line 2 is 12 side frames LD-10443. This change carries one line, ID 1, with 8 side frames LD-10443 and no LineStatusCode. Read by its ID it replaces the bench line with 8 side frames, which contradicts the note ("add …; the rest of the order is unchanged"), the item of order line 1 and the anticipated total (F2), which still includes the benches. It does not fit a change of line 2 either, which would show 20 frames. The same line ID 1 is carried on in `02-OrderResponse.xml:/OrderResponse/cac:OrderLine/cac:LineItem/cbc:ID` = `1` and in the order line references of both despatch advices (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`, `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`). Merge check: refutation attempted on the reading that an Order Change may number its own lines afresh; refuted, because the definition ties the lines to the changed order and the line carries no other link (no LineReference, no status) to the order's lines.
- Condition: the added side frames have a line ID that is not used by a different line of `VT-PO-26-0127` (e.g. 3), or the change is recognisably a change of line 2; the note, the totals (F2) and every later document of the flow that refers to this line (02, 06, 08) use the same line identification.
- Options: (a) preferred: a new line ID 3 with LineStatusCode `Added` (UBL LineStatusCode list), carried into 02, 06 and 08, because the note says the frames are added and the sea part of line 2 stays as ordered; (b) a revised line 2 (20 frames, `Revised`) with a split delivery, which changes the story more.
- Needs decision: no
- From: broad, money, logistics, context

### air/01#F2 · High · The anticipated total and the tax base are the whole new order total, while the only line is 512.00
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `51200.00`
- XPath: `/OrderChange/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `51200.00`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`
- XPath: `/OrderChange/cbc:LineCountNumeric` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`
- Why: In an Order Change, AnticipatedMonetaryTotal is "the amount of change to the total cost of the order anticipated by the buyer". The document has one line, 8 × 64 = 512.00 XBL; 51200.00 = 50688.00 (the original order) + 512.00, so the value is the new order total, not the amount of change. Under either reading the arithmetic of the document does not hold: as the amount of change it should be 512.00; as a restated total it covers lines (96 benches, 12 sea frames) that this document does not carry, so neither the line extension total nor the taxable amount can be recalculated from the document's lines. Merge check: redone (8 × 64 = 512.00; 49920.00 + 768.00 = 50688.00; + 512.00 = 51200.00). Raised to High: arithmetic in the example that does not hold is High by section 6; broad and context had Medium (element meaning), money High.
- Condition: AnticipatedMonetaryTotal/LineExtensionAmount, PayableAmount and TaxSubtotal/TaxableAmount equal the sum of the lines the Order Change carries, and agree with the definition (the amount of change).
- Options: (a) preferred: 512.00 in all three, the amount of change as the definition says, with the added line under its own ID (F1 option a); (b) carry every line of the changed order (bench line 1, sea frames line 2, new air line 3) so that 51200.00 is the sum of the lines (money part's preference; it keeps the restated total but contradicts the definition "amount of change", which would then be a finding on UBL to record).
- Needs decision: no
- From: broad, money, context

### air/01#F3 · Medium · LocaleCode holds a language code
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". A locale is a language as used in a region (English as used in Bayvarra), not the language itself. `en` with listID `ISO 639` is the bare language code and repeats Language/ID. The skill names "a language code in `LocaleCode`" as a Medium case. Counted over `*.xml`: 362 LocaleCode elements in 213 example files, all `en` with listID ISO 639 (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples | wc -l`; `grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: every LocaleCode holds a locale (language and region) from a list of locales with a matching listID, or is absent.
- Options: (a) preferred: drop LocaleCode where only the language is known, since Language/ID already says it; (b) a real locale such as `en-XB` with a locale list, if the world has a reason to state it.
- Needs decision: no
- From: broad, parties, context

### air/01#F4 · Medium · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". `Gate 3` is the entrance of the business park where vehicles or visitors come in, not a street name; it directs vehicles, not post, and sits in the seller's postal address in an order change that sends nothing to that gate (street, building number, block and plot are already given). Skill checklist: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles." Counted over `*.xml`: 79 occurrences in 76 example files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: Lumeway Distribution's PostalAddress has no AdditionalStreetName holding a gate; where the gate matters (a pickup or despatch place), it is carried by an element meant for it (e.g. the pickup or despatch Location).
- Options: (a) preferred: remove it from the postal address; (b) move it to the pickup or despatch location in the documents that arrange a pickup (03, the despatch advices).
- Needs decision: no
- From: parties, context

### air/01#F5 · Low · Document-level CPT next to "the rest of the order stays CIF", stated twice
- XPath: `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:SpecialTerms` = `The rest of the order stays CIF by sea.`
- XPath: `sea/05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: The same CPT term appears twice: at document level with the place, and on the Delivery with the remark. Document-level DeliveryTerms is "A set of delivery terms associated with this document". With totals covering the whole order (F2), CPT at document level reads as replacing the order's CIF terms, which the special terms then contradict; the Incoterm decides who bears freight and insurance for those amounts. CPT only concerns the added air frames, which the delivery-level terms already say.
- Condition: CPT and its place are stated once, where they apply only to the air delivery (or line), with the remark about CIF for the rest next to it, and nothing at document level says the whole order is CPT.
- Options: (a) preferred: one DeliveryTerms on the Delivery (or on the added line, as `02-OrderResponse.xml` does) with place and remark; (b) keep document-level CPT only if the document covers only the air line (F2 option a), without the duplicate.
- Needs decision: no
- From: broad, money, logistics (Medium there); context refuted it (see Changed in the merge)

### air/01#F6 · Low · The buyer names the air carrier in a CPT order change
- XPath: `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: Under CPT the seller contracts the carriage (Incoterms 2020 CPT A4, own knowledge). In this flow the seller books a forwarder (`02-OrderResponse.xml` names Bayforth Forwarding and its quote, `03-ForwardingInstructions.xml` asks for the booking on 12 May), and the airline appears in the waybill (`04-Waybill.xml`). A buyer's order change of 11 May that names the airline needs a reason in the story (a buyer's routing wish), or it does not belong here. Against: the parties and context parts read it as naming the expected carrier, which the waybill confirms, without contracting it; Kelaro is the island's air cargo carrier. The merge cannot settle which reading the story means.
- Condition: the CarrierParty in the order change has a stated reason (the buyer's routing request) or is absent.
- Options: (a) preferred: remove it (the seller chooses the carrier under CPT); (b) keep it and state the buyer's request in SpecialTerms or a note.
- Needs decision: yes
- From: broad, logistics; parties and context refuted it

### air/01#F7 · Low · SalesOrderID is the seller's number of the original order, not of the Order Change
- XPath: `/OrderChange/cbc:SalesOrderID` = `LD-SO-26-0123`
- XPath: `sea/06-OrderResponse.xml:/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: OrderChange/SalesOrderID is "An identifier for the Order Change, assigned by the seller". The buyer issues this document; the value is the seller's sales order number of the original order (`sea/06-OrderResponse.xml`), not an identifier of the change. Quoting the seller's order number is a legitimate need, but UBL has the place for it: OrderReference/SalesOrderID. Against (logistics): a seller commonly keeps one sales order for the order and its changes, and `07-FulfilmentCancellation.xml` cites the same pair; that explains the value, not its element.
- Condition: SalesOrderID holds a seller-assigned identifier of this Order Change, or the seller's order number is carried in OrderReference/SalesOrderID.
- Options: (a) preferred: move the value to `OrderReference/SalesOrderID`; (b) keep it and accept the reading "seller's number of the order being changed".
- Needs decision: no
- From: broad; logistics refuted it as a logistics finding

### air/01#F8 · Low · The delivery airport is given only by a description, without its UN/LOCODE
- XPath: `/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`
- Why: The named place of a CPT term is where the risk passes. The same airport is identified as UN/LOCODE XLSLA in the waybill; the checklist asks for the identifier where the same place is identified elsewhere.
- Condition: the delivery location carries `cbc:ID` XLSLA (schemeID UN/LOCODE) and its name.
- Options: add ID and Name (preferred), keeping the description as additional text.
- Needs decision: no
- From: logistics

### air/01#F9 · Low · The change gives no requested delivery date, although urgency is its reason
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-14`
- Why: The frames go by air because they are needed before the sea shipment arrives. The Delivery carries a carrier, a delivery party and terms, but no RequestedDeliveryPeriod, so the seller cannot tell from the change by when the frames are needed. The forwarding instructions later request delivery on 2026-05-14, a date that appears in no ordering document.
- Condition: the change states by when the added frames are to be delivered (Delivery/RequestedDeliveryPeriod or the line's delivery).
- Options: a RequestedDeliveryPeriod ending on or before 2026-05-14 (preferred, matches 03); or a date on the line.
- Needs decision: no
- From: logistics

### air/01#F10 · Low · The Urvanian national tariff code in a Bayvarra–Lisavu order change
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The code is from `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, Urvania's national tariff. The trade is between a Bayvarran seller and a Lisavan buyer, shipped from Bayvarra to Lisavu (`/OrderChange/cac:DestinationCountry/cbc:IdentificationCode` = `XL`); Urvania is only the country of origin. No party of this document and no authority it reaches uses the Urvanian tariff; it looks copied from the item master (section 4.8). Against (broad): it is the only national tariff list in the examples (counted over `*.xml`: 61 occurrences in 43 files), it belongs to the country of origin, and the original order carries the same classification. That explains where the value comes from, not why this order change needs it, so the merge keeps it as a Low finding.
- Condition: the item carries the classifications this document's parties use (HS, and the export or import country's tariff where needed), or a stated reason for the Urvanian one.
- Options: (a) preferred: drop the XU tariff code from the order change, keeping HS 732599; (b) a Bayvarran export or Lisavan import tariff code, if the world has one and the order needs it.
- Needs decision: no
- From: context; broad refuted it

### air/01#F11 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Nalevi Warehousing)
- Why: RegistrationDate is "The registration date of the CompanyID." `1996-01-01` (a New Year's Day) is the date of 25 different companies in three countries and registers (XB:FBR, XL:ICR, XU:CR), while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`). Counted over `*.xml`: 181 example files (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), 25 distinct RegistrationNames (lxml, PartyLegalEntity with that date). Unless the world has an event that registered all of them on that day, it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's RegistrationDate is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) preferred: a date per company from its history (company histories are open work for the encyclopaedia); (b) drop RegistrationDate where no date is known; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes (company histories)
- From: parties

### air/01#F12 · Low · Contact names, job titles and departments do not fit each other or the role
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: JobTitle is "The job title or function of this contact" and Department "The department where this contact works". The buyer's `Purchasing` contact is a customer service officer in Sales; the receiving warehouse's `Goods inwards` contact is also a customer service officer in Sales. Name, title and department contradict each other, and neither title fits the role (buying; receiving goods). Counted over `*.xml`: `Purchasing` followed by `Customer service officer` 52 times (`grep -rh --include='*.xml' -A1 '<cbc:Name>Purchasing</cbc:Name>' | grep -c 'Customer service officer'`).
- Condition: each contact's name, job title and department describe the same function, and it fits the party's role in this document.
- Options: (a) preferred: titles and departments matching the functional name (Purchasing: buyer / Purchasing; Goods inwards: goods receiving clerk or warehouse supervisor / Warehouse); (b) drop JobTitle and Department where they add nothing.
- Needs decision: no
- From: broad, parties

## Checked and consistent
- References: `VT-PO-26-0127` is `sea/05-Order.xml`, an Order issued 2026-05-07 with the same buyer, seller, originator, beneficiary, CustomerReference, AccountingCostCode/AccountingCost and currency; `LD-DAG-26-0125` is `sea/03-DigitalAgreement.xml` between Lumeway and Velumi (flow_index.py, re-checked in the merge).
- Line: 8 × 64 = 512.00; price, item identifiers (GTIN 9520610000029, check digit OK), seller's and manufacturer's item IDs, HS and CPC codes and manufacturer are the same as order line 2 of `sea/05-Order.xml` (price `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Price/cbc:PriceAmount` = `64`).
- Tax: category G at 0 % with exemption reason EXP, scheme STT, fits an export from Bayvarra (Upland State) to Lisavu (DestinationCountry XL) and matches the original order; TaxAmount 0.00 in total and subtotal.
- Currency XBL throughout; AccountingCostCode `500` / "Stock for municipal projects" as in the order.
- Parties: Lumeway Distribution (register `20410274`, GLN `9520610900008` with correct check digit and GS1 demonstration prefix 952, customs trader `XB-TR-410274`, tax number `UL-1230822` in Upland State matching `XB-UL`, Ltd, MEDIUM, registered 1988-10-03), Velumi Trading (`IC41859`), Nalevi Warehousing (`IC41722`), Port of Selanu (`IC41037`) and Valdara Industries (`XU-R-104274`) carry the same identifiers, addresses and contacts as in `sea/05-Order.xml`; Kelaro Air Cargo `IC41311` is the carrier of `04-Waybill.xml`.
- ISIC Rev.4: Lumeway and Velumi `4649`, Nalevi `5210`; they fit what the parties do. Telephone numbers `+999 …` use an unassigned E.164 country code; domains use `.example`.
- DestinationCountry XL agrees with the delivery party's address and with the unloading airport XLSLA of `04-Waybill.xml`; quantity 8 EA agrees with 02, 03 (package quantity 8), 06 and 08 (DeliveredQuantity 8).

## Considered and refuted
- `/OrderChange/cac:Delivery/cac:NotifyParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: notify party equal to the delivery party, suspected redundant — refuted because under CPT to the airport the warehouse has to be told when to collect the frames at the cargo terminal (from broad, parties, logistics, context).
- `/OrderChange/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: originator and beneficiary in an order change, suspected copied — refuted because the original order names them too and the frames serve the same project (`/OrderChange/cbc:CustomerReference` = `Harbour parks Selanu`) (from broad, parties, context).
- `/OrderChange/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `64`: price unchanged although the seller now bears air freight that exceeds the goods value (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `554.88`) — refuted because it is a commercial choice the documents state consistently (from money).
- `/OrderChange/cac:AccountingCustomerParty` and `/OrderChange/cac:AccountingSupplierParty`: suspected redundant copies of buyer and seller — refuted because their definitions carry no "if different" condition and the order does the same (from parties).
- `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`: English renderings of island addresses tagged `en-XL` here and `en-XB` in other examples — refuted here because `en-XL` fits island names; the inconsistency is recorded in the reviews of the examples that use `en-XB` (from parties).
- `/OrderChange/cac:BuyerCustomerParty/cac:Party`: no PartyTaxScheme for Velumi Trading — refuted as a gap: the order change does nothing with the buyer's tax registration (from parties).
- `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: fits the definition of a block (from parties).
- `/OrderChange/cbc:CustomerReference` = `Harbour parks Selanu`: suspected misuse (purchasing card) — refuted because at document level the definition is "A supplementary reference for the transaction"; a project reference fits (from context).
- `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo` (from parties and context): the merge does not follow this refutation; see F6, which carries the argument.
- `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`: duplication with Delivery/DeliveryTerms, refuted by context as the change's own terms agreeing with the delivery-level terms — the merge does not follow it; see F5.
- `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990` (from broad): the merge does not follow this refutation; see F10.
- `/OrderChange/cbc:SalesOrderID` = `LD-SO-26-0123` (from logistics, refuted as a logistics finding): the merge does not follow it; see F7.

## Changed in the merge
- broad/F1, money/F1 (line ID part), logistics/F1, context/F1 → F1: combined; context's LineStatusCode `Added` added to the preferred option.
- money/F1 → split into F1 (line ID) and F2 (totals), because the line ID is a different element with its own fix and recurs in 02, 06, 08.
- broad/F2, context/F2 (Medium), money/F1 (High) → F2: High, because the line amounts in the document do not add up to the totals (arithmetic, section 6 High); money's preferred option kept as option (b).
- broad/F3, parties/F1, context/F3 → F3: combined, counts re-made.
- parties/F2, context/F4 → F4: combined.
- broad/F5 (Low), money/F2 (Low), logistics/F2 (Medium) → F5: Low. The contradiction with "the rest stays CIF" exists only under the whole-order reading of the totals (F2); in a document that covers only the change, document-level CPT is the change's own term, as context argued. What remains certain is the duplication and the ambiguity, hence Low.
- broad/F6, logistics/F5 → F6: combined, with the refutations of parties and context carried into "Why".
- broad/F7 → F7: logistics' counter-argument added.
- context/F5 → F10: broad's refutation added as the counter-argument; the merge keeps it as a finding (section 4.8).
- broad/F4, parties/F4 → F12: combined; the "Cargo sales" option of parties dropped, as Kelaro has no contact here.

## Outside this review
- No example invoices the 8 air frames (512.00): the seller's invoice of the order bills only the 96 benches and 12 sea frames (`sea/22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`). Whether the frames are billed in a document outside the examples is a cross-flow question (from money).
