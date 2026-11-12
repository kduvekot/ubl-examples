# LLM review: 04-TransportExecutionPlanRequest.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/04-TransportExecutionPlanRequest.xml`, Git blob `291e2fcd1c4b728be274ce60b1b1117f4ce1b87d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 83ce5da 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### wood/04#F1 · High · Transport window ends before the delivery window the seller promised
- XPath: `/TransportExecutionPlanRequest/cac:ServiceStartTimePeriod/cbc:StartDate` = `2026-02-26`
- XPath: `/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-03-01`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-02-27`
- Why: `ServiceEndTimePeriod` is "The period during which the services referred to in the Transport Execution Plan Request must be completed". The seller asks the haulier to complete the DAP transport to Valdara by 1 March, but the buyer requested and the seller promised delivery from 2 to 16 March; the goods are cleared for import on 27 February, so in the flow as written they arrive at least three days before the agreed window opens. Early delivery is possible in practice, but no document of the flow records that the buyer agreed to it (the order states no period, see F8 of the merged review of `03-Order.xml`). The transport request and the quotation state dates for the same delivery that contradict each other.
- Condition: The transport service window lies within the delivery window that the request for quotation and the quotation establish, or an example of the flow states that the buyer agreed to an earlier delivery.
- Options: (a) move the delivery window of the request for quotation and the quotation to the transport's dates (e.g. 26 February – 6 March), which keeps the documents from despatch onwards unchanged and changes the fewest documents; (b) if the story wants the March window, move the transport window and the dates of despatch, export, import and invoice into it; (c) keep both and add the buyer's agreement to early delivery (e.g. an order with that period). Preference: (a), because it changes two documents instead of five; the person deciding may prefer (b) for the story.
- Needs decision: yes
- From: logistics, broad, context

### wood/04#F2 · Medium · Language code `en` in `Language/LocaleCode`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with `listID="ISO 639"` is a language code only and repeats `Language/ID`; a locale is a language as used in a country. The Urvanian parties carry no `LocaleCode`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; files with `grep -rl`).
- Condition: Every `cbc:LocaleCode` in this example holds a locale with a `listID` naming a list of locales, or is absent.
- Options: (a, preferred) leave `LocaleCode` out where no locale matters, as here; (b) a real locale such as `en-XB` from a list of locales, named in `listID`.
- Needs decision: no
- From: broad, context, parties

### wood/04#F3 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country …", which UBL puts in `CountrySubentity`, as the Bayvarran addresses of the same document do (`/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CountrySubentity` = `Upland State`). Affected: Trasvia Haulage, the destination, Valdara Industries. 219 occurrences in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`; files with `grep -rl`).
- Condition: No Urvanian address in this example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with a code where the world has one), and `cbc:Region`, if present, holds a region in the UBL sense.
- Options: (a, preferred) move the province to `CountrySubentity` in every Urvanian address; (b) if Ferrano is an economic region in the world, rename it without "Province" and record that in the story.
- Needs decision: no
- From: broad, logistics, context, parties

### wood/04#F4 · Medium · The transport request does not say in structured form what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `MS-CS-26-0629`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The slats across the border to the bench factory.`
- Why: A Transport Execution Plan Request is sent "to request a transport service"; the provider needs to know what it carries and how it is packed. The consignment gives only its ID, gross weight and parties: no goods description, no number or kind of packages or handling units (96 bundles of 50 on heat-treated pallets, per `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.` and `03-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`), no volume. "Slats" appears only in the free-text note. For a full truck load the weight lets the haulier check the payload (logistics and context parts, which rated this Low), but not plan the loading; the skill names "a transport request that does not say what is to be carried" as a Medium case, and the note is not structured data.
- Condition: The consignment states in structured form what is carried: at least a goods description and the number and kind of packages or handling units (and, if relevant, volume).
- Options: (a, preferred) add a `GoodsItem` (description, quantity, gross weight) and a `TransportHandlingUnit` or package count for the 96 bundles; (b) at least `Consignment/TotalTransportHandlingUnitQuantity` (or a package count) and a goods description.
- Needs decision: no
- From: broad, logistics, context

### wood/04#F5 · Low · A status code that says "no status"
- XPath: `/TransportExecutionPlanRequest/cbc:DocumentStatusCode` = `NoStatus`
- Why: `NoStatus` means "No status on document". Present, it states only that there is nothing to state, a filler under "no fillers, and nothing implied by absence": its absence would say the same. The value occurs as `DocumentStatusCode` in 26 examples (`grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: A document status code is present only where the document has a status to convey (e.g. a replacement or a copy).
- Options: (a, preferred) drop the element; (b) use it in an example where the status matters.
- Needs decision: no
- From: context

### wood/04#F6 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Here the Bayvarran sawmill and the Urvanian haulier share it; the date occurs 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`; files with `grep -rl`), for about 25 companies of every kind in all three registers (parties part), while other dates are specific (Valdara 1962-04-12). It reads as a filler unless the world has an event that explains it.
- Condition: Each company's registration date is its own date in the world, or the world documents why these companies share 1996-01-01; otherwise it is absent.
- Options: (a, preferred) each company its own date; (b) record a 1996 re-registration in the story if intended; (c) leave the date out.
- Needs decision: yes
- From: broad, parties

### wood/04#F7 · Low · Sender's and consignee's contacts are sales customer-service desks
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party", read in its role. The sender booking a truck should be reached in despatch or logistics, not its sales office; the consignee's contact is the one the haulier turns to on arrival (goods-in), not an order desk in Sales. `Customer service officer` occurs 395 times in 229 examples (`grep -rho --include='*.xml' 'Customer service officer' world/examples | wc -l`; files with `grep -rl`). The haulier's own contact (a planning desk in Operations) fits.
- Condition: The sender's contact is the one who arranges this transport and the consignee's the one who receives the goods, with name, job title and department agreeing.
- Options: (a, preferred) role-specific contacts per party in the world, chosen by the role in each document; (b) drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no
- From: broad, context, parties

### wood/04#F8 · Low · Text tagged as English is Italian
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: The English renderings (tagged `en-XB`) of the Urvanian street names are Italian, and so are the legal forms (untagged here, see F10). 219 English-tagged street names in 104 examples start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml' 'StreetName languageID="en-X[A-Z]">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): street names are proper names, commonly left untranslated, and the world uses Italianate names consistently. That does not cover the legal forms, descriptive terms. The merge could not settle whether the Italian forms are the world's English exonyms.
- Condition: Every text tagged (or meant) as English is English, or the world's story states that these Italian forms are the English-language names used for Urvania.
- Options: (a, preferred if intended) record the convention in the story and give the legal forms in English; (b) English renderings throughout.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/04#F9 · Low · Same Urvanian text tagged `en-XB` here and `en-XU` in the Urvanian-issued examples
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: Valdara's address (and the town Ferrano) carries `en-XB` in this Bayvarran-issued request and `en-XU` in 01, 03, 07 and 09. If `languageID` describes the language of the text, the same text should carry the same tag; 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties and context parts): the tag names the variant of the issuer's English, consistently within each document. Both readings are possible; the examples do not say which rule they follow.
- Condition: The same text carries the same `languageID` in every example of the flow, or the rule that the tag follows the issuer is documented.
- Options: (a, preferred) one rule, documented in the world; (b) document that the tag follows the issuer's locale.
- Needs decision: yes
- From: broad (parties and context refuted it; see "Considered and refuted")

### wood/04#F10 · Low · Urvanian legal forms in one untagged rendering, unlike the addresses
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Ban Kumek`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- Why: Trasvia's and Valdara's addresses have two tagged renderings (`qau` and English), their legal forms only one, without `languageID`; in the Urvanian-issued examples Valdara's legal form has both, each tagged (`01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). Within this example the address and the legal form follow different language rules, and the parties are described differently from example to example.
- Condition: Within this example each Urvanian party's legal form follows the same language rule as its address.
- Options: (a, preferred) both renderings, each tagged, as in the Urvanian-issued examples; (b) one tagged rendering, with the reason why the address keeps its Urvanian rendering (delivery).
- Needs decision: no
- From: parties

### wood/04#F11 · Low · The haulier's own operating permit in the request sent to the haulier
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: The request is sent by the sawmill to Trasvia Haulage; describing the receiver with its own permit tells the receiver nothing, and the request does nothing with it (it does not, e.g., require the permit for the service). It looks copied from the haulier's master data (section 4.8). Counter-argument (broad part): a transport user has a reason to know the haulier is licensed for international haulage. That reason concerns the sawmill's own records; the request does not state it as a requirement. In the export declaration (05) the same permit concerns a third party, customs, and is not a finding there.
- Condition: The receiver carries only what the request needs to address it, or the authorization is used for a stated purpose (e.g. as a requirement of the service).
- Options: (a, preferred) drop the authorization here and keep it where a third party relies on it; (b) state it as a requirement of the requested service.
- Needs decision: no
- From: context (broad refuted it; see "Considered and refuted")

### wood/04#F12 · Low · From and to locations are named after the companies, not the places
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: `Location/Name` is "The name of this location"; the names are the parties' names. The commercial documents name the DAP place more precisely (`03-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Valdara Industries, goods-in, Ferrano`; `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Valdara Industries, goods-in, Ferrano`), and the sawmill's own later order names its yard (`10-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Marrowdale Sawmill, timber yard`). The same place is thus named differently here.
- Condition: The locations name the places where the goods are loaded and unloaded, and the destination is named as in the commercial documents of the flow.
- Options: (a, preferred) "Marrowdale Sawmill, timber yard" and "Valdara Industries, goods-in, Ferrano", keeping the addresses; (b) leave `Name` out and rely on the address, or add identifiers if the world has them.
- Needs decision: no
- From: broad, logistics, parties

### wood/04#F13 · Low · Valdara's master data the request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: A transport request needs the consignee's identity and the delivery address. Valdara's share capital, stock-exchange listing and logistics service provider are master data the request does nothing with (section 4.8). In this document the copy also raises a question of the story (parties part): if Castrano Logistics runs Valdara's warehousing, the goods might be received by Castrano rather than by Valdara's goods-in; the request does not say, and delivers to Valdara's business address. Castrano appears in 9 of the 11 wood examples (`grep -l Castrano world/examples/wood/*.xml | wc -l`), never in a role of its own.
- Condition: The consignee's description carries share capital, listing and service provider only if the request uses them; if Castrano has a part in this delivery, the request says so.
- Options: (a, preferred) leave them out of this document, if Castrano has no part in the delivery; (b) make Castrano's part explicit (e.g. as the party receiving the goods, or the destination).
- Needs decision: yes (whether Castrano receives this delivery is a question of the story)
- From: broad, context, parties

## Checked and consistent
- Consignment `MS-CS-26-0629` recurs with the same gross weight 21 600 kg in `05-ExportCustomsDeclaration.xml` and `06-DespatchAdvice.xml`; the carrier Trasvia Haulage (XU-R-104822, haulage licence XU-HAUL-2020-0877 valid to 2030-06-30) is the same party there (broad, logistics, parties).
- Roles: sender, transport user and bill-to party are the seller, as DAP requires (`/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill`); the consignee is the buyer (broad, logistics, context, parties).
- Dates: issued 2026-02-23 16:19; response deadline `/TransportExecutionPlanRequest/cac:TransportServiceProviderResponseDeadlinePeriod/cbc:EndDate` = `2026-02-24` after issue and before the service start 2026-02-26, the day of the despatch advice, the export declaration and the invoice (broad, logistics, context).
- Physics, recalculated in the merge: 4800 × 0.006498 m³ = 31.19 m³; 21 600 kg / 31.19 m³ = 693 kg/m³ including packaging, within 650–750 kg/m³ for kiln-dried hardwood at 12 % moisture (own knowledge); 21.6 t and 31 m³ fit one truck (about 24 t payload, about 90 m³, own knowledge), consistent with `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL` and the quotation's "minimum one truck" (broad, logistics, context).
- From and to addresses match the seller's and the buyer's addresses; codes `FTL`, `NoStatus`, `BUSINESS`, `XB`/`XU` resolve in their lists (logistics, context).
- Parties identical to their other full descriptions in the flow apart from language renderings; identifiers and tax schemes consistent; `check_ids.py` passes; Trasvia (ISIC 4923) fits the carrier role (parties).

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `MS-TH-FW-2026` not an example — refuted: a framework contract is an external document; the definition ("a potential contract") is met (from broad).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty` with ID and name only — refuted: the consignor is the sender, fully described in `SenderParty` (from broad).
- `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address`: a postal address copied into a location, without address register ID — refuted: it is where the goods are loaded, and an identifier is optional (from logistics).
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: a load type where the definition speaks of "the extent of this transportation service (e.g., door-to-door, port-to-port)" — refuted: a full truck load defines the extent of the service (exclusive use of a truck, door to door), a legitimate reading (from context).
- `/TransportExecutionPlanRequest/cac:BillToParty/cac:PartyName/cbc:Name` = `Marrowdale Sawmill` — refuted: under DAP the seller pays the main carriage (from parties).
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Department` = `Operations` — refuted: a planning desk in operations is the right contact for a transport request (from parties).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427` (real ICD?), `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER` (real MIC?), `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501` (check digit) — refuted: not in the repository's ICD and MIC lists; `check_ids.py` passes (from parties).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: definition says "number of shares" — refuted: the element is an Amount; whether it belongs here is F13 (from parties).
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization`: copied master data — refuted by the broad part (the transport user has a reason to know the haulier is licensed). Not followed: kept as F11 (context).
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text tagged English — refuted by the parties part as a world convention. Not followed: kept as F8, Needs decision: yes.
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano` and `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via delle Officine` tagged `en-XB` here, `en-XU` elsewhere — refuted by the parties and context parts (the tag follows the issuer's English). Not followed: kept as F9, Needs decision: yes.

## Changed in the merge
- logistics/F1, broad/F4, context/F3 → F1: combined at High (logistics'); broad and context had Low. Section 6 makes "a statement in one example that another example of the flow contradicts" High: the quotation promises 2–16 March, this request has the delivery completed by 1 March, and no example records an agreement. Options from all three parts kept; preference stated for (a) (logistics').
- broad/F3, context/F2, parties/F2 → F2: combined; preferred option "leave out" (context's), as in the other merged reviews.
- broad/F2, logistics/F2, context/F1, parties/F1 → F3: combined (logistics had only the destination, the others all three addresses); context's "Needs decision: yes" set to no.
- broad/F1 (Medium), logistics/F3 (Low), context/F4 (Low) → F4: combined at Medium (broad's), because the skill names a transport request that does not say what is to be carried as Medium and the note is not structured data; the lower rating of logistics and context recorded in "Why".
- context/F6 → F5; broad/F10, parties/F6 → F6; broad/F5, context/F7, parties/F3 → F7: combined, wording only.
- broad/F9 → F8: count corrected (219 in 104 files instead of 217 in 102); the receiver's legal form added; parties' counter-argument added.
- broad/F8 → F9: Needs decision changed from no to yes, with the parties' and context's refutations as counter-argument (cannot settle).
- parties/F5 → F10; context/F5 → F11 (broad's refutation added as counter-argument); broad/F7, logistics/F4, parties/F7 → F12: combined.
- broad/F6, context/F8, parties/F4 → F13: combined; Needs decision: yes (parties'; broad and context had no), because whether Castrano receives this delivery is a question of the story; aligned with the merge of wood 06–11, which keeps the same question for 06-DespatchAdvice.

## Outside this review
- Whether Trasvia has a vehicle available and able to carry 21.6 t on 2026-02-26 is a capacity question for the cross-flow review (from broad).
- Despatch on 2026-02-26 in Marrowdale and import clearance on 2026-02-27 11:05 in Urvania: whether road distance and border crossing fit is for the consistency review (from logistics).
