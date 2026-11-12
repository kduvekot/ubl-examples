# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/03-TransportExecutionPlanRequest.xml`, Git blob `fe5bfa14052d31ed395823661598b379931d78e9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/03#F1 · Medium · LocaleCode holds a language code
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID` and names no locale, while the document uses `en-XB` in `languageID`. All 362 `LocaleCode` elements (213 files) are `en` with ISO 639 (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) drop it (preferred: `Language/ID` says English; broad, parties, rail and air merges); (b) `en-XB` with a locale list (context's preference).
- Needs decision: no
- From: broad (F1), parties (F1), context (F2)

### road/03#F2 · Medium · Gate number in AdditionalStreetName
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance of the business park. In the sender's postal address it has no place at all; at the to-location it is useful information for the haulier, but not a street name. 79 occurrences in 76 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance; where the gate matters for the delivery it is given in an element meant for it (e.g. the to-location's `Description`, or the delivery event's location).
- Options: (a) drop the gate from the sender's address and move it, at the to-location, into a location description (preferred); (b) drop it from both if the waybill's delivery instruction is enough.
- Needs decision: no
- From: broad (F2), parties (F2)

### road/03#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the same document use (`/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity`.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions in the world's address rules.
- Needs decision: no
- From: broad (F3), parties (F3), context (F1)

### road/03#F4 · Low · DocumentStatusCode NoStatus carries nothing
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Transport Execution Plan Request"; the code means "No status on document". This is a first request with nothing updated, cancelled or confirmed; `NoStatus` states only that there is no status, which absence would say equally (IND6: nothing implied by absence, no fillers). The code occurs as `DocumentStatusCode` in 26 files (`grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus<'`). Added by the merge (no part raised it), aligned with the rail, air, wood and plastics merges.
- Condition: `DocumentStatusCode` is absent, or carries a status the request actually has.
- Options: drop it (preferred).
- Needs decision: no
- From: merge

### road/03#F5 · Low · Document note narrates the example instead of informing the carrier
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The truck the distributor booked, from the 3PL's warehouse across the border.`
- Why: `Note` is "Free-form text pertinent to this document, conveying information that is not contained explicitly in other structures". The text speaks about the sender in the third person ("the distributor booked") and repeats what the structures say (from Castrano's warehouse, cross-border); it reads as a caption of the example, not as a message from Lumeway to Trasvia.
- Condition: the note is absent, or says something to the carrier that the structures do not.
- Options: (a) drop it (preferred); (b) replace it with information the carrier can use (e.g. that the export declaration is ready at pickup).
- Needs decision: no
- From: context (F6)

### road/03#F6 · Low · Contacts that do not fit a transport booking
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender books a truck, so its contact is the one the carrier answers ("Please confirm by return"); Lumeway's customer service in Sales serves its own customers. The consignor's contact is the one the haulier needs at pickup, which happens at Castrano's warehouse, whose `Warehouse office` is the loading contact in the order (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:Contact/cbc:Name` = `Warehouse office`); Valdara's order desk in Sales is not at the pickup place. Each party carries one fixed contact in every role of the flow.
- Condition: the sender's contact handles transport; the consignor's contact, or a contact for the pickup, can be reached about the loading.
- Options: (a) a transport contact for Lumeway and Castrano's warehouse office as pickup contact (e.g. at the from-location or the pickup event) (preferred); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F4, F6 in part), parties (F4), context (F3)

### road/03#F7 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". Trasvia Haulage SRU carries 1 January 1996, a public holiday, the date that occurs 271 times in 181 files for at least 25 companies (`grep -rho`/`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway and Valdara have dates of their own. It reads as a filler (IND5).
- Condition: each party's `RegistrationDate` is its own plausible date, or absent.
- Options: (a) the company's own date from its history (preferred); (b) leave it out.
- Needs decision: yes (company history is story; aligned with the rail and air merges)
- From: parties (F5)

### road/03#F8 · Low · From and to locations named after companies, without identifiers
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Lumeway Distribution`
- Why: `Location/Name` is "The name of this location"; both carry the operating company's name instead of the place (Castrano's warehouse in Ferrano, Lumeway's distribution centre in Marrowdale Business Park), and carry no identifier, although the same places are identified in the same document (`/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cac:Location/cbc:ID` = `XUFER`, `/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cac:Location/cbc:ID` = `XBMRW`) and by address register IDs elsewhere (parties).
- Condition: each location's name names the place, and the location carries the identifiers used for the same place in the flow.
- Options: (a) name the sites (e.g. "Castrano warehouse, Ferrano", as the order's FCA place already does) and add their identifiers (preferred); (b) drop the names and rely on address and identifiers.
- Needs decision: no
- From: broad (F5), parties (F6), logistics (F2), context (F4)

### road/03#F9 · Low · Number and size of the handling units only in free text
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `Park benches and spare side frames on 25 pallets.`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `4106.4`
- Why: the 25 pallets appear only in text, and nothing says that 24 of them are 1850 × 650 mm bench pallets (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:MeasurementDimension[1]/cbc:Measure` = `1850`). The merge recalculated whether the request is plannable without them: on a 13.6 m × 2.45 m trailer, three 650 mm pallets fit side by side and 7 rows of 1850 mm fit in the length, i.e. 21 pallet places single-stacked, fewer than 24; the waybill's loading length of 9.3 m (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:LoadingLengthMeasure` = `9.3`) needs stacking two high. A carrier accepting an FTL booking can check none of this from the request. Broad and context refuted a missing structured count (the request says what is carried, weight and pallets in text, which its purpose needs); the merge agrees that the purpose is met and keeps logistics' point as a completeness remark (Low), not as missing information.
- Condition: the request carries the number of handling units as a structured value (e.g. `TotalTransportHandlingUnitQuantity` 25) and, for non-standard units, their dimensions or the loading length.
- Options: (a) add `TotalTransportHandlingUnitQuantity` and `LoadingLengthMeasure` as in the waybill (preferred); (b) add transport handling units with type and dimensions.
- Needs decision: no
- From: logistics (F1)

### road/03#F10 · Low · Party master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- Why: a carrier needs neither the consignor's stock-exchange listing and share capital nor its own operating permit sent back to it in a request for transport; copied master data (section 4.8, IND5). The consignor's `ServiceProviderParty` (Castrano, warehousing and despatch), which broad included, is not part of this finding: it explains why the pickup is at Castrano's warehouse (context's refutation, followed; same as the rail merge for 02/03).
- Condition: every party detail in the request has a use in booking or performing the transport.
- Options: drop them (preferred).
- Needs decision: no
- From: broad (F6 in part), parties (F7), context (F5)

### road/03#F11 · Low · Italian street names and legal forms tagged as English
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: these renderings carry an English `languageID` but are Italian. In this Bayvarra-issued request they are tagged `en-XB`, while the same addresses are tagged `en-XU` in the Urvanian documents (folded in here, as the rail merge's Low/yes question). Parties (and broad in 01) refuted this: English text keeps foreign street names as proper names, and the subtag follows the sender. Counter-argument: where a `qau` rendering already gives the local name, a second rendering tagged English has a reason only if it is English, and a legal-form text such as "Società urvaniana per azioni" is not a proper name. The merge cannot settle which rule the world follows; added from the parts' refutation, aligned with the rail merge and the merger of road 13–17 (217 renderings in 102 files tagged `en-XU`/`en-XB` start with Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina, the rail merge's count).
- Condition: every rendering tagged as English is English, or the world's rule that place names and legal forms keep their source form under an English tag (and which region subtag an Urvanian address gets in a Bayvarran document) is documented.
- Options: (a) document the rule for street names and render legal forms in English (preferred: street names as proper names are common practice, legal forms are not); (b) tag the Italian renderings with a tag of their own language, if the world has one.
- Needs decision: yes
- From: merge (from the refutation of parties)

### road/03#F12 · Low · Urvanian legal forms in one untagged rendering
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: in the documents Urvanian parties issue, the legal forms of Valdara, Castrano and Trasvia are given twice, tagged `qau` and `en-XU` (e.g. `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`); this Bayvarra-issued document gives one rendering without `languageID`, while its addresses of the same parties are rendered in two tagged languages. The same party is described differently in the examples of the flow (checklist: party described the same way). Added by the merge (parties noted the subtag difference only), aligned with the rail and air merges and the merger of road 13–17.
- Condition: each Urvanian legal form is rendered like the party's address in the same document (tagged renderings), or the single rendering carries a `languageID`.
- Options: (a) both renderings, tagged, as in the Urvanian documents (preferred); (b) one rendering with a `languageID`.
- Needs decision: no
- From: merge

## Checked and consistent
- Requested pickup 2026-03-23 14:00 at Ferrano equals the order's requested despatch; requested delivery 2026-03-25 10:00 at Marrowdale equals the waybill's required delivery (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:RequiredDeliveryTime` = `10:00:00`); both lie in the service periods (2026-03-23 to 2026-03-26) (broad, logistics, context).
- Consignment LD-CS-26-0152 and gross weight 4106.4 kg (= 3984 + 122.4) agree with 04, 05 and 08; 25 pallets = 24 bench pallets + one pallet of 12 boxed side frames (broad, logistics).
- Response deadline 2026-03-18 after the issue date 2026-03-17; `TransportUserRemarks` asks for confirmation (broad, logistics, context).
- Sender = transport user = bill-to Lumeway, receiver = provider Trasvia: fits FCA (buyer contracts and pays main carriage), the waybill's freight note and 14-Invoice (broad, parties, context).
- UN/LOCODEs XUFER and XBMRW as in the waybill; origin XU and destination XB fit the route (broad, context).
- `ContainerizedIndicator` false, `GeneralCargoIndicator` true, curtain-side trailer loaded from the side fit palletised benches; 4.1 t is far below a trailer's payload (logistics, context).
- Check digits: GLN 9520610900008, ISIN XU0001042501 pass (parties).

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription`: pallet count only as text, as missing information — refuted as missing information because the request says what is carried (from broad, context); kept by the merge only as logistics' completeness remark F9.
- `/TransportExecutionPlanRequest/cac:BillToParty`: bill-to equal to the transport user — refuted because stating the billed party is meaningful under a framework contract (from broad).
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: a load type where the definition asks for "the extent of this transportation service" — refuted because the world list defines FTL as "One truck for one consignment, from the place of loading to the place of delivery", which states the extent (from context); and FTL for a load needing 9.3 m of a 13.6 m trailer — refuted because FTL books the whole vehicle, legitimate for a sealed cross-border load (from logistics).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: master data — refuted because it explains why the pickup is at Castrano (from context; broad had it in its F6, see F10).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number rather than identifier — refuted: the definition does not say who assigns it (from parties).
- Consignment without structured goods items or package count — refuted because summary, gross weight, pallet count and FTL say what is carried (from context).
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: Italian-looking name tagged `en-XB` — refuted: proper names, subtag follows the sender (from parties). Not followed in full by the merge, see F11.
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: real GLN — refuted: prefix 952, check digit correct (from parties).
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Telephone`: real numbers — refuted: +999 reserved (from parties).
- `/TransportExecutionPlanRequest/cac:ReceiverParty`: full party data next to `TransportServiceProviderParty` with ID and name only — refuted: one full rendering of the addressee suffices (from parties).

## Changed in the merge
- broad/F1, parties/F1, context/F2 → F1: combined; parties' "Needs decision: yes" set to no (aligned with the rail and air merges).
- broad/F2, parties/F2 → F2: combined; options made specific for the to-location (delivery-relevant) and the postal address.
- broad/F3, parties/F3, context/F1 → F3: combined.
- F4: added by the merge (`NoStatus`), aligned with the rail and air merges.
- broad/F4, parties/F4, context/F3 and the contact part of broad/F6 → F6: combined.
- parties/F5 → F7: "Needs decision" set to yes (aligned with the rail and air merges).
- broad/F5, parties/F6, logistics/F2, context/F4 → F8: combined.
- logistics/F1 → F9: kept against broad's and context's refutations as a Low completeness remark; physics recalculated by the merge.
- the master-data part of broad/F6, parties/F7, context/F5 → F10: combined; the consignor's `ServiceProviderParty` removed from the finding (context's refutation, rail merge).
- F11: added by the merge from parties' refutation, aligned with the rail merge and the merger of road 13–17.
- F12: added by the merge, aligned with the rail and air merges and the merger of road 13–17.

## Outside this review
- The actual pickup (15:05 in `08-Waybill.xml` and `09-TransportationStatus.xml`) is an hour after the requested 14:00; a timeline question.
- This request (2026-03-17 14:16) precedes the order response `02-OrderResponse.xml` (17:42); plausible under the framework contract (noted by the 02 broad part).
