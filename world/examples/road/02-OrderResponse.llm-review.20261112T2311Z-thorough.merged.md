# LLM review: 02-OrderResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/02-OrderResponse.xml`, Git blob `4fa9a01f7c53c819946f93ff994818f91259d67f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/02#F1 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address of the same document uses `CountrySubentity` (`/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: the province is in `CountrySubentity` (with a code where the world has a list); `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) define Urvanian provinces as non-administrative regions in the world's address rules.
- Needs decision: no
- From: broad (F1), parties (F1), context (F4)

### road/02#F2 · Medium · LocaleCode holds a language code
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID` and names no locale, while the document uses locales such as `en-XU` in `languageID`. All 362 `LocaleCode` elements (213 files) are `en` with ISO 639 (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) drop it (preferred: `Language/ID` says English; broad, parties, rail and air merges); (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad (F2), parties (F2), context (F5)

### road/02#F3 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance of the business park, information for vehicles, not part of the buyer's postal address. 79 occurrences in 76 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance; where a gate matters for a delivery it is in a delivery location.
- Options: (a) drop the gate from the address (preferred); (b) keep it only in delivery addresses in an element meant for it.
- Needs decision: no
- From: broad (F3), parties (F3)

### road/02#F4 · Medium · Promised delivery ends before the guaranteed despatch
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchDate` = `2026-03-24`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchTime` = `12:00:00`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:EstimatedDespatchPeriod/cbc:EndDate` = `2026-03-24`
- Why: `PromisedDeliveryPeriod` is "The period promised for delivery" and `GuaranteedDespatchDate` "The date guaranteed for the despatch (pickup)". Under the order's FCA term (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) delivery is the hand-over to the carrier at the warehouse, i.e. the despatch; the seller promises it for 23 March only but guarantees and estimates the despatch up to 24 March (12:00). Read as arrival at Marrowdale, 23 March is impossible as well, since the waybill expects delivery on `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:EstimatedDeliveryDate` = `2026-03-25` (context). Refutation attempt in the merge: a promise can be a target and a guarantee an outer limit (broad, logistics), so the two values do not strictly exclude each other; but a promise that ends before the guaranteed limit gives the guarantee no meaning. Kept as Medium, between logistics' Low and context's High.
- Condition: the promised delivery period, the estimated despatch period and the guaranteed despatch agree (under FCA the guaranteed despatch lies within the promised delivery period).
- Options: (a) end the promised delivery period on 2026-03-24, matching the estimated despatch period (preferred by all three parts); (b) guarantee despatch by the end of 23 March; (c) drop the guarantee if only the estimate matters.
- Needs decision: no
- From: broad (F4), logistics (F2), context (F2)

### road/02#F5 · Medium · ResponsibleParty is the warehouse, not the party that picks up
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`
- Why: `Despatch/ResponsibleParty` is "The party who picks up the goods". Castrano Logistics is the seller's 3PL that hands the goods over (despatch party in `01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyName/cbc:Name` = `Castrano Logistics`, despatch supplier in `04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`); the goods are picked up by the buyer's carrier Trasvia, which records the pickup in `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`. Broad had checked the element as fitting ("hands the goods over"), which reads the definition the other way round.
- Condition: `ResponsibleParty`, if present, is the party that collects the goods (Trasvia Haulage); Castrano, if named, is the despatch party.
- Options: (a) name Trasvia as `ResponsibleParty` (preferred by parties and logistics: confirms who collects under FCA), and Castrano as `DespatchParty` if needed; (b) drop `ResponsibleParty` (the order already names both).
- Needs decision: no
- From: parties (F4), logistics (F1), context (F3)

### road/02#F6 · Medium · The proposed substitute is the old casting the response says is replaced
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Bench side frame casting, 2025, from stock`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2025`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- XPath: `/OrderResponse/cac:OrderLine[2]/cbc:Note` = `Same fit and price; the old casting is no longer made.`
- XPath: `/OrderResponse/cbc:Note[2]` = `Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the same price.`
- Why: `SellerProposedSubstituteLineItem` is "a line item proposed by the seller describing a product that might substitute for the product described in this order line", and `SellerSubstitutedLineItem` "a line item that has replaced the original order line item". The response carries both: the 2026 casting as the replacement, and the 2025 casting "from stock", which by the document note is the item ordered, as a proposed substitute for itself. The notes speak only of the replacement, and later documents treat the 2026 casting as delivered (`16-ApplicationResponse.xml:/ApplicationResponse/cac:DocumentResponse/cac:LineResponse/cac:Response/cbc:Description` = `Matched to the substituted 2026 casting.`). Refutation attempt in the merge: "no longer made" and "from stock" can both be true (old stock left), so the values do not strictly contradict each other (context's High lowered); but a proposed substitute that is the ordered product does not fit the definition, which makes it Medium rather than broad's Low.
- Condition: line 2 says one thing about what replaces the ordered casting: the 2026 casting as substituted item, and a proposed substitute only if the seller offers a different alternative, explained in a note.
- Options: (a) remove `SellerProposedSubstituteLineItem` and keep the substituted 2026 line (preferred: the substitution is decided, as `OrderResponseCode` CA, the notes and 16 say); (b) if the buyer may choose the remaining 2025 stock, say so in the line note.
- Needs decision: no
- From: broad (F7), context (F1)

### road/02#F7 · Low · Buyer's contact is its own customer service in Sales
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the order response goes to the buyer's purchasing, which must accept the substitution; Lumeway's customer service in Sales serves Lumeway's own customers. Each party carries one fixed contact in every role of the flow.
- Condition: the buyer's contact is a purchasing function, or absent.
- Options: (a) a purchasing contact (preferred); (b) drop job title and department.
- Needs decision: no
- From: broad (F5), parties (F6), context (F6)

### road/02#F8 · Low · Seller's stock-exchange listing in an order response
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the listing of Valdara's shares plays no part in accepting the order or substituting a line; copied master data (section 4.8, IND5).
- Condition: every optional party aggregate of the response has a reason in its purpose.
- Options: drop it (preferred).
- Needs decision: no
- From: parties (F5), context (F7)

### road/02#F9 · Low · Line document references by ID only
- XPath: `/OrderResponse/cac:OrderLine[1]/cac:DocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:DocumentReference/cbc:ID` = `VI-DS-C180-2026`
- Why: `OrderLine/DocumentReference` is "A reference to a document associated with this order line"; both carry only an ID. In the order the same `VI-DS-B180` is the item specification (`01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`); line 1 is accepted unchanged, so its reference does nothing here (context), and on line 2 the recipient has to guess that `VI-DS-C180-2026` is the data sheet of the new casting.
- Condition: every line document reference has a use in the response and says what it refers to (type code or type text), or the data sheet is in the item's `ItemSpecificationDocumentReference`.
- Options: (a) drop the reference on line 1 and type the one on line 2 (preferred: line 1 needs none); (b) move line 2's reference into the substituted item's `ItemSpecificationDocumentReference`.
- Needs decision: no
- From: broad (F6), context (F8)

### road/02#F10 · Low · Italian street names and legal forms tagged as English
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: these renderings carry an English `languageID` but are Italian. Parties refuted this: English text keeps foreign street names as proper names, and the subtag follows the sender. Counter-argument: where a `qau` rendering already gives the local name, a second rendering tagged English has a reason only if it is English, and a legal-form text such as "Società urvaniana per azioni" is not a proper name. The merge cannot settle which rule the world follows; added from the parts' refutation, aligned with the rail merge and the merger of road 13–17 (217 renderings in 102 files tagged `en-XU`/`en-XB` start with Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina, the rail merge's count).
- Condition: every rendering tagged as English is English, or the world's rule that place names and legal forms keep their source form under an English tag (and which region subtag an Urvanian address gets in a Bayvarran document) is documented.
- Options: (a) document the rule for street names and render legal forms in English (preferred: street names as proper names are common practice, legal forms are not); (b) tag the Italian renderings with a tag of their own language, if the world has one.
- Needs decision: yes
- From: merge (from the refutation of parties)

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `LD-PO-26-0149` resolves to `01-Order.xml`; buyer and seller agree; issued 2026-03-17 17:42, after the order (broad, logistics, context).
- Quantities 96 and 12 EA match the order lines; the substituted line keeps the ordered price 5980 XUF, as the notes say (broad, context).
- `OrderResponseCode` CA (conditionally accepted, UN/EDIFACT 4343) fits an acceptance with one substituted line; line 1 `NoStatus` next to line 2 `Revised` with `SubstitutionStatusCode` Substitution distinguishes the unchanged line from the changed one (broad, context; considered again in the merge, see below).
- Estimated despatch 2026-03-23 14:00 equals the order's requested despatch and the transport request's requested pickup; the actual despatch on 2026-03-23 lies within the estimated and guaranteed windows (broad, logistics, context).
- `NotifyParty` Lumeway is the buyer and consignee, the party told of the despatch (parties, logistics, context).
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass (`check_ids.py`; parties).
- Party identity agrees field by field with the other examples of the flow apart from the region subtag of English renderings (parties).

## Considered and refuted
- `/OrderResponse/cac:OrderLine[1]/cac:OrderLineReference/cbc:UUID` = `da67b26b-2501-5b9b-9b6f-d03d5ce50a97`: the order lines in 01 have no UUID — refuted because the UUID identifies the line reference, not the order line (from broad).
- `/OrderResponse/cac:OrderLine[2]/cac:OrderLineReference/cbc:SalesOrderLineID` = `2` only on line 2 — refuted because the seller's own line ID matters only for the revised line (from broad, context).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian-looking name tagged `en-XU` — refuted because foreign street names stay proper names in English and the subtag follows the sender (from parties). Not followed in full by the merge, see F10.
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN that could be real — refuted: prefix 952 is reserved for examples, check digit correct (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: real numbers — refuted: +999 is reserved by ITU-T E.164 (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number rather than identifier — refuted: the definition does not say who assigns it (from parties).
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: master data — refuted because Castrano despatches this order (from context).
- `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cbc:LineStatusCode` = `NoStatus`: considered by the merge for alignment with the rail and air merges, which made `NoStatus` a Low finding (no fillers) — refuted here because in an order response with a revised line 2, `NoStatus` on line 1 says that this line is accepted unchanged, which the response needs to say (from merge).

## Changed in the merge
- broad/F1, parties/F1, context/F4 → F1: combined.
- broad/F2, parties/F2, context/F5 → F2: combined; parties' "Needs decision: yes" set to no (encoding fix; aligned with the rail and air merges).
- broad/F3, parties/F3 → F3: combined.
- broad/F4, logistics/F2, context/F2 → F4: combined; severity Medium (broad) kept, logistics' Low raised and context's High lowered (target vs limit reading makes it no hard contradiction, but the promise as written empties the guarantee).
- parties/F4, logistics/F1, context/F3 → F5: combined; broad's "Checked and consistent" entry on `ResponsibleParty` not followed.
- broad/F7, context/F1 → F6: combined; severity set to Medium (broad Low, context High), "Needs decision" no (broad yes): dropping the proposed substitute changes no document of the flow and matches what the notes and 16 already say.
- broad/F5, parties/F6, context/F6 → F7: combined.
- parties/F5, context/F7 → F8: combined.
- broad/F6, context/F8 → F9: combined; context's preference (drop line 1's reference) taken as option (a).
- F10: added by the merge from parties' refutation, aligned with the rail merge and the merger of road 13–17.

## Outside this review
- `03-TransportExecutionPlanRequest.xml` is issued 2026-03-17 14:16, before this response (17:42): the buyer books the truck before the seller confirms; a timeline question, plausible under a framework contract (from broad).
- The documents after this response identify the side frame as `VI-C180` without the extended ID `2026` (`04-DespatchAdvice.xml`, `15-Invoice.xml`); a finding of 04 (from context; merged into road/04).
