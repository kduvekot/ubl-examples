# LLM review: 01-Order.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/01-Order.xml`, Git blob `888e6ba193f9e99d9a10149a112547e954b6d115` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/01#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With 0.82 per 1 EA (one bench) the calculated value is 0.82 kg CO2e, not the stated 96 kg. No activity quantity of the item explains the figure: 96 / 0.82 = 117.1, which is neither a count of the order (96, 12) nor the materials consumed per bench (34 kg steel + 22.5 kg hardwood = 56.5 kg; 0.82 × 56.5 = 46.3) nor the bench's weight in the transport documents (about 38–41.5 kg). Verified in the merge by recalculation. The same triple occurs in 39 examples, 9 of them in this flow (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'` over `world/examples`, and over `road/*.xml`).
- Condition: `ValueFactorNumeric` × (activity quantity / `ValueBaseMeasure`) equals `ValueMeasure`, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) drop `ValueFactorNumeric` and `ValueBaseMeasure` and keep the per-bench total (preferred: the value is a per-item LCA figure and nothing in the order uses a factor; same preference as the rail merge); (b) give a factor and base whose product is 96 kg (e.g. per kg of material, base in KGM).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F3)

### road/01#F2 · Medium · LocaleCode holds a language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (the document itself uses `en-XB` in `languageID`); `en` with listID `ISO 639` only repeats `Language/ID` = `en` and names no locale. All 362 `LocaleCode` elements of the examples (in 213 files) are `en` with ISO 639 (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>'` and `grep -rl` over `world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and region) from a list of locales named in its listID.
- Options: (a) drop `LocaleCode` (preferred: `Language/ID` already says English and nothing in the order needs the region; preferred by broad and parties and by the rail and air merges); (b) a locale such as `en-XB` with a locale list as listID (context's preference).
- Needs decision: no
- From: broad (F2), parties (F1), context (F6)

### road/01#F3 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/Order/cac:Delivery/cac:DeliveryAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance of the business park, not a street name; in the postal address of the buyer it says nothing about where mail goes, and in the delivery address it is a delivery instruction in the wrong element. 79 occurrences in 76 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`). How the gates relate to the alternative delivery location is F10.
- Condition: No `AdditionalStreetName` holds a gate, dock or entrance; where a gate matters for the delivery it is in an element meant for it (a delivery location or its description).
- Options: (a) drop the gate from the party address and, for the delivery, carry it in `Delivery/DeliveryLocation` (preferred: the definition, and same as the rail and air merges); (b) keep it only in the delivery address, in `MarkAttention` or a location description.
- Needs decision: no
- From: broad (F3), parties (F2)

### road/01#F4 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address of the same document puts its state in `CountrySubentity` (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: No Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with `CountrySubentityCode` where the world has a list).
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules.
- Needs decision: no
- From: broad (F4), parties (F3), context (F5)

### road/01#F5 · Medium · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text". In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)", while raw material supply and its transport (A1, A2) is `SOURCING`. The text and the description cover A1 to A3 (cradle to gate), so the code names a narrower stage than the figure and its text.
- Condition: the lifecycle stage code and text name the same stage(s), and the figure covers exactly what they name.
- Options: (a) omit the code and keep the cradle-to-gate text, or use a code covering A1–A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure and texts to A3.
- Needs decision: no
- From: context (F1)

### road/01#F6 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life a figure covers), which says nothing about the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl --include='*.xml' 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'`); other uses of the element take `LoadTypeCode`.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated in text.
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` (preferred: an item's cradle-to-gate figure has no transport equipment), and record the missing boundary element for the UBL TC write-up; (b) none that keeps the code here.
- Needs decision: no
- From: context (F2)

### road/01#F7 · Low · Contacts that do not fit the party's role in the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact in an order is the one who buys (purchasing); Lumeway gives the customer-service desk in Sales that serves its own customers. Castrano's contact is named `Warehouse office`, which fits a despatch party, but its job title and department are those of a sales customer-service officer, so name, job title and department disagree. Each party carries one fixed contact in every role of the flow.
- Condition: the buyer's contact is a purchasing function; the despatch party's contact has a name, job title and department that agree and fit warehouse work.
- Options: (a) role-specific contacts (purchasing for Lumeway, a warehouse job title and department for Castrano) (preferred); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F5), parties (F4), context (F7)

### road/01#F8 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: section 4.8: data copied from a party's master data into a document that does not use it. The seller's stock-exchange listing ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") and the despatch party's shareholder play no part in ordering, despatching or delivering. The carrier's international haulage permit is the weakest part: parties refuted it (the buyer names the carrier it booked for an international leg, and the permit qualifies it); context kept it because the order does not make the permit a condition of carriage. Both arguments are kept here; the merge keeps it in the finding because nothing in the order refers to the permit.
- Condition: every party detail in the order has a use in ordering, despatching or delivering the goods, or the order's purpose explains it.
- Options: (a) drop the listing and the shareholder; drop the permit unless the order makes it a condition of carriage (preferred); (b) state in the order why the permit is given.
- Needs decision: no
- From: parties (F5), context (F8)

### road/01#F9 · Low · Registration date 1996-01-01 looks like a default, not each company's own date
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Castrano Logistics SRU and Trasvia Haulage SRU share 1 January 1996, a public holiday; the date occurs 271 times in 181 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), for at least 25 companies, while Lumeway (1988-10-03) and Valdara (1962-04-12) have dates of their own. It reads as a filler (IND5).
- Condition: each party's `RegistrationDate` is its own plausible date, or the element is absent for that party.
- Options: (a) give each company its own date from its history (preferred); (b) leave the date out where the world has none.
- Needs decision: yes (the companies' histories are story; aligned with the rail and air merges)
- From: parties (F6)

### road/01#F10 · Low · Gates and docks of the delivery are named inconsistently
- XPath: `/Order/cac:Delivery/cac:AlternativeDeliveryLocation/cbc:Description` = `Gate B of the business park, if dock 4 is blocked.`
- XPath: `/Order/cac:Delivery/cac:DeliveryAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: the delivery address names `Gate 3`, the alternative location "Gate B ... if dock 4 is blocked", and the waybill says `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:DeliveryInstructions` = `Unload at dock 4; report to the gatehouse first.` Gate 3, Gate B, dock 4 and the gatehouse are never related to each other; the alternative is a gate, while what it replaces is a dock. Context checked the dock 4 match with the waybill as consistent, which holds for the dock alone.
- Condition: the delivery address or location, the alternative delivery location and the waybill's instruction describe the same entrances and docks consistently, and the alternative is of the same kind as what it replaces.
- Options: (a) name the normal entrance and dock once in the delivery location and make the alternative another dock or gate of the same kind (preferred); (b) drop the alternative location if the story has no use for it.
- Needs decision: no
- From: broad (F6)

### road/01#F11 · Low · Maximum delivery unit of 100 has no role in a single delivery of 108 items
- XPath: `/Order/cac:Delivery/cac:MaximumDeliveryUnit/cbc:BatchQuantity` = `100`
- XPath: `/Order/cac:Delivery/cac:MinimumDeliveryUnit/cbc:BatchQuantity` = `4`
- XPath: `/Order/cac:Delivery/cbc:Quantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MinimumQuantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MaximumQuantity` = `108`
- Why: `MaximumDeliveryUnit` is "The maximum delivery unit for this delivery" and `BatchQuantity` "The quantity of ordered Items that constitutes a batch for delivery purposes". The minimum of 4 matches the 4 benches per pallet (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `24 pallets of 4 benches: one full truck.`); 100 matches nothing in the flow, which delivers 108 items in one truck of 25 handling units (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalTransportHandlingUnitQuantity` = `25`), and no document refers to it (IND5). Context read it as a limit the delivery cannot meet (Medium); a delivery can consist of several batches, so 100 does not strictly forbid 108, and the merge keeps it as Low.
- Condition: every delivery-unit value of the order corresponds to a real constraint the delivery respects, or is absent.
- Options: (a) remove `MaximumDeliveryUnit` (preferred: no real case); (b) a batch size the story uses (e.g. a full pallet load).
- Needs decision: no
- From: broad (F7), logistics (F2), context (F4)

### road/01#F12 · Low · Item number reads as a real GTIN-12
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- XPath: `/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- Why: the numbers of the world item scheme are 12 digits with a valid GS1 mod-10 check digit (recomputed in the merge: 7 and 4), so a GS1 check reads them as GTIN-12s in the range administered by GS1 US; `771` is also a GS1 prefix range (GS1 Colombia, 770–771; own knowledge of the GS1 prefix allocation). The rule that fictional values must not be mistakable for real register entries applies. Only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`.
- Condition: the item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the scheme are described the same way.
- Options: (a) a non-GS1 structure or a GS1 prefix reserved for examples (952) if the scheme is meant to mimic GTIN (preferred); (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role.
- Needs decision: yes (the world's item scheme; aligned with the rail and plastics merges)
- From: broad (F8)

### road/01#F13 · Low · Catalogue and product-passport data in the order
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CircularityProfile`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- Why: the buyer's order says what is ordered; search keywords, the seller's warranty, the circularity profile (materials, maintenance, waste, repairability) and the product's LCA emission are catalogue or product-passport data of the seller that nothing in ordering, despatch or delivery uses (section 4.8, IND5). The same item block recurs in the despatch advice, customs and origin documents of the flow, where the parts made it a finding. Added by the merge: no part of 01 raised it; aligned with the rail merge (rail 01) and with this flow's 04, 05 and 06.
- Condition: the ordered item carries what identifies and specifies it for the order, and no catalogue or passport data without a use in the order.
- Options: (a) drop keyword, warranty, circularity profile and environmental emission from the order line (preferred); (b) keep any of them only if the order makes it a requirement (e.g. a maximum emission the buyer asks for), and say so.
- Needs decision: no
- From: merge

### road/01#F14 · Low · Italian street names and legal forms tagged as English
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- Why: these renderings carry an English `languageID` but are Italian. In this Bayvarra-issued order they are tagged `en-XB`, while the same addresses are tagged `en-XU` in the Urvanian documents (broad refuted the subtag difference: each document tags English in the issuer's locale; the rail merge kept it as a Low/yes question, folded in here). Parties (and broad in 01) refuted this: English text keeps foreign street names as proper names, and the subtag follows the sender. Counter-argument: where a `qau` rendering already gives the local name, a second rendering tagged English has a reason only if it is English, and a legal-form text such as "Società urvaniana per azioni" is not a proper name. The merge cannot settle which rule the world follows; added from the parts' refutation, aligned with the rail merge and the merger of road 13–17 (217 renderings in 102 files tagged `en-XU`/`en-XB` start with Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina, the rail merge's count).
- Condition: every rendering tagged as English is English, or the world's rule that place names and legal forms keep their source form under an English tag (and which region subtag an Urvanian address gets in a Bayvarran document) is documented.
- Options: (a) document the rule for street names and render legal forms in English (preferred: street names as proper names are common practice, legal forms are not); (b) tag the Italian renderings with a tag of their own language, if the world has one.
- Needs decision: yes
- From: merge (from the refutation of parties, broad)

### road/01#F15 · Low · Urvanian legal forms in one untagged rendering
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: in the documents Urvanian parties issue, the legal forms of Valdara, Castrano and Trasvia are given twice, tagged `qau` and `en-XU` (e.g. `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`); this Bayvarra-issued document gives one rendering without `languageID`, while its addresses of the same parties are rendered in two tagged languages. The same party is described differently in the examples of the flow (checklist: party described the same way). Added by the merge (parties noted the subtag difference only), aligned with the rail and air merges and the merger of road 13–17.
- Condition: each Urvanian legal form is rendered like the party's address in the same document (tagged renderings), or the single rendering carries a `languageID`.
- Options: (a) both renderings, tagged, as in the Urvanian documents (preferred); (b) one rendering with a `languageID`.
- Needs decision: no
- From: merge

## Checked and consistent
- Line arithmetic: 96 × 49 900 = 4 790 400 and 12 × 5 980 = 71 760; sum 4 862 160 = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `4862160` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `4862160` = taxable amount; tax 0 at 0 %; `LineCountNumeric` 2 (broad, money; redone in the merge).
- Prices reappear unchanged in `15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `49900` and in the substituted line of `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Price/cbc:PriceAmount` = `5980`; `AccountingCostCode` 4410 is repeated in `15-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410` (money).
- XUF and XBL are not ISO 4217 codes (money, own knowledge).
- `Delivery/Quantity` 108 = 96 + 12; both lines multiples of the minimum unit 4 (broad, logistics, context).
- Requested despatch 2026-03-23 14:00 lies in the requested despatch period 13:00–17:00 and equals the requested pickup in `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `14:00:00` (broad, logistics, context).
- FCA at Castrano's warehouse fits the despatch address and party, the buyer-appointed carrier and the instruction to have the export declaration ready; `05-ExportCustomsDeclaration.xml` is issued 2026-03-23 13:25, before the pickup (logistics, context).
- Tax category G with exemption reason EXP fits the export from Urvania (broad, money, context).
- Check digits: GLN 9520610900008 (GS1 prefix 952 for examples) and ISIN XU0001042501 pass (`check_ids.py`; broad, parties, logistics).
- Parties: Lumeway, Valdara, Castrano and Trasvia are described identically across the flow apart from the region subtag of the English renderings; Castrano's shareholder (Valdara 100 %) agrees with Valdara's service provider (Castrano); `DeliveryAddress` has the same register ID `UL-ADR-693911` as Lumeway's postal address (parties).
- Item dimensions and resource consumption agree with the despatch advice and the customs documents; HS codes 940179 and 732599 fit bench and cast side frame (logistics, context).
- Material story (Serravona ore, Upland State slats) agrees with `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:Remarks` = `Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.` (broad).
- Physics: five 1800 mm slats with 22.5 kg wood consumed per bench (about 4.5 kg per slat at roughly 700 kg/m³) and 34 kg steel consumed against two cast side frames of about 10 kg plus rails and fittings; consumption including casting and sawing losses fits a finished bench of 36–38 kg (broad, logistics).

## Considered and refuted
- `/Order/cac:Delivery/cbc:MinimumQuantity` = `108` (and `MaximumQuantity` 108): suspected filler — refuted because equal minimum and maximum state that neither short nor over-delivery is accepted, a real ordering condition (from broad, context).
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty`: carrier named a day before the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:IssueDate` = `2026-03-17`) — refuted because under FCA the buyer appoints the carrier and books it under the framework contract `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-TH-FW-2026` (from broad, logistics, context).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian-looking rendering tagged `en-XB` — refuted because English text keeps foreign street names as proper names, and the subtag follows the sender (from broad, parties). Not followed in full by the merge, see F14.
- Valdara's address tagged `en-XB` here but `en-XU` in `02-OrderResponse.xml` — refuted because each document tags English in the issuer's locale (from broad).
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649` for a distributor of park benches — refuted because ISIC 4649 includes the wholesale of furniture (from broad).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`: SellerContact under a service provider — refuted because the definition is "The contact for the Service Provider" (from broad).
- Consumption 56.5 kg per bench above the 41.5 kg gross per bench of the customs declaration — refuted because `ConsumptionMeasure` includes production losses (from broad).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP` under FCA at the seller's 3PL — refuted because the seller itself declares the export (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`), which is what zero-rating requires (from money).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN that could be real — refuted because prefix 952 is reserved for examples and the check digit is correct (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: numbers that could be real — refuted because +999 is reserved by ITU-T E.164 (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number rather than an identifier — refuted because the definition does not say who assigns it (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`: master data — refuted because Castrano despatches under this order (from context).
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID`: carrier licence as copied master data — refuted by parties (it qualifies the booked carrier); the merge does not follow fully and keeps it, with this argument, as the weakest part of F8.
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Castrano Logistics warehouse, Ferrano`: company as location, and FCA place without identifier — refuted because the text names the place (the warehouse in Ferrano) and the full despatch address is in the same Delivery (from parties, logistics).
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ImportanceCode` = `OPTIONAL` for the frame colour — refuted because the colour is also fixed by `SellersItemIdentification/ExtendedID` (from context).

## Changed in the merge
- broad/F1, logistics/F1, context/F3 → F1: combined; context's Medium raised to High (arithmetic that does not hold, section 6); preferred option set to dropping factor and base (context's and the rail merge's preference) instead of broad/logistics' "give the real factor".
- broad/F2, parties/F1, context/F6 → F2: combined; parties' "Needs decision: yes" set to no (an encoding fix; aligned with the rail and air merges); preferred option drop (broad, parties) with context's en-XB as option (b).
- broad/F3, parties/F2 → F3: combined; the alternative delivery location XPath of parties/F2 moved to F10.
- broad/F4, parties/F3, context/F5 → F4: combined; counts redone (219 in 104 files).
- context/F1 → F5: High lowered to Medium, aligned with the rail merge: the code is from the right list but names a narrower stage; the text next to it says what the figure covers, so the reader is not misled about the figure, and the misuse of the code is what remains.
- context/F2 → F6: TC write-up moved from option (b) into option (a).
- broad/F5, parties/F4, context/F7 → F7: combined.
- parties/F5, context/F8 → F8: combined; parties' refutation of the carrier licence carried into the Why.
- parties/F6 → F9: "Needs decision" set to yes, aligned with the rail and air merges (companies' histories).
- broad/F7, logistics/F2, context/F4 → F11: combined; context's Medium lowered to Low (a delivery may hold several batches, so no hard conflict; IND5 remark).
- broad/F8 → F12: the side frame's number added as a second place.
- F13: added by the merge, aligned with the rail merge and with this flow's 04–06.
- F14: added by the merge from broad's and parties' refutations (Italian text and en-XB subtag), aligned with the rail merge and the merger of road 13–17.
- F15: added by the merge, aligned with the rail and air merges and the merger of road 13–17.

## Outside this review
- The same emission, lifecycle, fullness, item-number and catalogue data recur in 04, 05, 06, 07, 10, 11, 13 and 15 of this flow (`grep -l CircularityProfile road/*.xml`); each example's review carries its own finding.
