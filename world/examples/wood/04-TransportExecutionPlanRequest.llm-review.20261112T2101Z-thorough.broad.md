# LLM review: 04-TransportExecutionPlanRequest.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/04-TransportExecutionPlanRequest.xml`, Git blob `291e2fcd1c4b728be274ce60b1b1117f4ce1b87d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### wood/04#F1 · Medium · Transport request does not say what is to be carried
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `MS-CS-26-0629`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The slats across the border to the bench factory.`
- Why: A Transport Execution Plan Request is "sent by a transport user to request a transport service"; the haulier needs to know what it carries. The consignment gives only its ID and gross weight: no goods description, no number or kind of packages (96 bundles on pallets, per `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`), no volume or loading metres. Only the free-text note says "slats".
- Condition: The consignment states what is carried: at least a goods description and the number and kind of packages or handling units (and, if relevant, volume).
- Options: (a, preferred) Add a GoodsItem or TransportHandlingUnit with description, 96 pallets/bundles and their weight; (b) at least ConsignmentQuantity / package count and a goods description on the consignment.
- Needs decision: no

### wood/04#F2 · Medium · Urvanian province carried in Region
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is defined as "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division, which UBL puts in CountrySubentity ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses in the same flow do use CountrySubentity and CountrySubentityCode for their states, so the two countries are encoded differently. The same value occurs 219 times in 104 XML files (`grep -r --include='*.xml' -c '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address carries an administrative division in Region; the province, where given, is in CountrySubentity (with CountrySubentityCode if the world has a list for it).
- Options: (a, preferred) Move the province to CountrySubentity, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world a non-administrative region, keep Region but name it as such, without "Province of".
- Needs decision: no

### wood/04#F3 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/04#F4 · Low · Transport to be completed before the promised delivery window opens
- XPath: `/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-03-01`
- XPath: `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-03-02`
- XPath: `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueDate` = `2026-02-27`
- Why: The buyer asked for delivery from 2026-03-02 to 2026-03-16 and the seller promised that window; the seller then asks the haulier to finish by 2026-03-01, and the goods are declared for import on 2026-02-27. Delivering early is possible in practice, but no document says the buyer agreed to it, so the plan contradicts the promise unless the story explains it.
- Condition: The transport's completion date lies within the delivery window the order and the quotation agree on, or an example records that the buyer accepted an earlier delivery.
- Options: (a, preferred) Move the transport (start, end, and the dependent despatch, export and import dates) into the window; (b) bring the promised/requested window forward to match the transport.
- Needs decision: yes

### wood/04#F5 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The transport user's contact is the sawmill's sales office (customer service officer), not someone who arranges transport or despatch; the consignee's contact is Valdara's order desk in its Sales department, but a consignee's contact receives the goods (goods-in), which is where the haulier will turn on arrival.
- Condition: The sender's contact is the one who arranges this transport, and the consignee's contact is the one who receives the goods.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/04#F6 · Low · Valdara's master data the document does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's SecurityListing (listed shares) and its ServiceProviderParty (Castrano Logistics, "Warehousing and despatch") are carried in full in this transport request (for the consignee), which does nothing with either: no security is traded, and Castrano plays no role (the goods go to Valdara's own goods-in in Ferrano). This is party master data copied into a document that does not use it (section 4.8).
- Condition: The party carries in this document only data the document uses, or the example gives the reason for the security listing and the service provider.
- Options: (a, preferred) Leave SecurityListing and ServiceProviderParty out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which would change the story.
- Needs decision: no

### wood/04#F7 · Low · From/To location names are company names
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Marrowdale Sawmill`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Valdara Industries`
- Why: Location/Name is "The name of this location". The names given are the companies, not the places (e.g. the sawmill's loading yard, Valdara's goods-in), although the order already names the delivery place as "Valdara Industries, goods-in, Ferrano" (`03-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`).
- Condition: From and To locations are named as places, consistent with the delivery location of the order.
- Options: (a, preferred) Name the places ("Marrowdale Sawmill, loading yard", "Valdara Industries, goods-in, Ferrano"); (b) leave Name out and rely on the address.
- Needs decision: no

### wood/04#F8 · Low · Same Urvanian address tagged en-XB here and en-XU elsewhere
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same English rendering of the same Urvanian address is tagged `en-XB` in this example and `en-XU` in `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` (and 03, 07, 09) for Valdara's address. The languageID describes the language of the text, which does not change with the sender's country, so the same text should carry the same tag. 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|…) '`).
- Condition: The same rendering of the same address carries the same languageID in every example of the flow.
- Options: (a, preferred) Tag the rendering by the language variant of the text (the Urvanian English, en-XU) everywhere; (b) document that the tag follows the sender's locale.
- Needs decision: no

### wood/04#F9 · Low · English (en-X?) renderings of Urvanian names are Italian
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The second rendering of the Urvanian street name (and, where present, of the legal form) is tagged as English (`en-XU`/`en-XB`) but is Italian ("Via …", "Piazza …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be, and the languageID does not describe it. 217 English-tagged street names in 102 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml'`).
- Condition: Every text tagged with an English languageID is English, or the world states that these Italian forms are the official English-language names in Urvania.
- Options: (a) Give the English rendering in English (e.g. "Workshops Street"); (b) if the Italian forms are the world's exonyms, record that in the world's story so the tag is explained. Preference: (b) if it is intended, as the pattern is consistent; otherwise (a).
- Needs decision: yes

### wood/04#F10 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day). Here the sawmill (Bayvarra) and the haulier (Urvania) share it.
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Consignment `MS-CS-26-0629` recurs with the same gross weight 21600 kg in 05-ExportCustomsDeclaration.xml and 06-DespatchAdvice.xml; the carrier Trasvia Haulage (XU-R-104822) is the same party there.
- Roles: transport user, sender and bill-to are the seller, as DAP requires the seller to contract and pay for the carriage; the consignee is the buyer.
- Dates: issued 2026-02-23 16:19, response deadline 2026-02-24, service start 2026-02-26, consistent with the despatch and invoice on 2026-02-26.
- Physics: one slat is 1.800 × 0.095 × 0.038 m = 0.006498 m³, 4800 slats = 31.19 m³; kiln-dried ash or oak at 12 % moisture weighs about 650–750 kg/m³ (own knowledge), i.e. 20.3–23.4 t of wood, plus 96 heat-treated pallets; the stated 21 600 kg gross is plausible and within an ordinary full-truck payload (about 24 t).
- The haulier's authorization (international road haulage, valid to 2030-06-30) fits a cross-border road transport and is valid at the time.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization`: copied master data — refuted: a transport user has a reason to know that the haulier is licensed for international haulage.
- `/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `MS-TH-FW-2026` not an example — refuted: a framework contract is an external document; the definition ("a potential contract") is met.
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty` with ID and name only — refuted: the consignor is the sender, fully described in SenderParty.

## Outside this review
- Whether Trasvia has a vehicle available and able to carry 21.6 t on 2026-02-26 is a capacity question for the cross-flow review.
