# LLM review: 01-Order.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/01-Order.xml`, Git blob `b65397fa0c7cc5caf77d2e114d9eb2db2610109c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/01#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a base of 1 bench (unitCode EA) the factor gives 0.82 × 1 = 0.82 kg CO2e, not the 96 kg stated. No other quantity of the item makes 0.82 a meaningful factor: 96 / 0.82 = 117, which matches nothing in the item (steel 34 kg + hardwood 22.5 kg consumed = 56.5 kg; 192 benches × 0.82 = 157.4; 56.5 × 0.82 = 46.3; consignment gross 7968 kg / 192 = 41.5 kg per bench). Merge check: recomputed, confirmed. The same triple 96 / 0.82 / 1 EA occurs in 39 files (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`), in this flow also in 06 and 11.
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure (in consistent units), or factor and base are absent.
- Options: (a) preferred: drop factor and base, since 96 kg is a per-product footprint, not an activity-based calculation (context, logistics); (b) state the factor that produced 96 kg with its real base (e.g. kg CO2e per kg of material, base in KGM); (c) set the factor to 96 per 1 EA (broad's first variant; adds nothing over ValueMeasure). If 0.82 is meant as something else (an allocation share), it does not belong in ValueFactorNumeric.
- Needs decision: no
- From: broad (F1), context (F1), logistics (F1)

### rail/01#F2 · Medium · Language code in LocaleCode of the buyer
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode/@listID` = `ISO 639`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` from ISO 639 is a language code and only repeats `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`; it names no locale (the examples themselves use locale tags such as `en-XB` as languageID). The seller's Language carries no LocaleCode. The same value occurs 364 times (`grep -rh --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, recounted in the merge; the parts counted 362).
- Condition: LocaleCode is absent or holds a locale (language plus region) from a list of locales with a matching listID.
- Options: (a) preferred: drop LocaleCode (Language/ID already says English and nothing in the order depends on the locale; parties); (b) `en-XB` with a locale list (e.g. BCP 47) as listID (broad, context).
- Needs decision: no
- From: broad (F5), context (F4), parties (F1)

### rail/01#F3 · Medium · Gate in AdditionalStreetName of the buyer's postal address
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the business park for vehicles, not a street name, and it sits in the party's business address (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AddressTypeCode` = `BUSINESS`), used for every purpose of the party. The goods are delivered by rail to the siding, not through a road gate. AdditionalStreetName starting with "Gate" occurs in 76 files (`grep -rl --include='*.xml' 'AdditionalStreetName>Gate' world/examples | wc -l`).
- Condition: Lumeway's postal address has no gate in AdditionalStreetName (or anywhere else in the postal address); a gate, where it matters, is given at a delivery location.
- Options: (a) preferred: remove it from the postal address and, where a delivery needs it, state it at the delivery location (here probably not needed at all); (b) if "Gate 3" is part of the official Bayvarran address, record that in the world's address rules and use the element the format defines for it.
- Needs decision: no
- From: broad (F6), parties (F2)

### rail/01#F4 · Medium · Province in Region of the seller's address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "the political or administrative division of a country … such as the name of its county, province, or state". The buyer's Bayvarran address in the same document puts its state in CountrySubentity (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). "Province of Ferrano" in Region occurs 219 times in 104 files (`grep -rh --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`, and `-l` for files).
- Condition: an Urvanian province is in CountrySubentity (with CountrySubentityCode where a list exists); Region is not used for it.
- Options: (a) preferred: move it to CountrySubentity, as for the Bayvarran states; (b) drop it where postal zone and city already locate the address; (c) if the world defines Urvanian provinces as non-administrative regions, keep Region and record that in the address rules.
- Needs decision: no
- From: broad (F4), context (F5), parties (F3)

### rail/01#F5 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: In the world's LifecycleStageCode list (`world/codelists/lists.json`, checked in the merge) MANUFACTURING is "Making the product (EN 15804 module A3)"; SOURCING is "Raw material supply and its transport (EN 15804 modules A1 and A2)". The description, the Description and the cradle-to-gate value of 96 kg cover A1 to A3. The code and its text equivalent describe different stages.
- Condition: the stage code(s) cover exactly what LifecycleStageDescription and Description say the value covers.
- Options: (a) preferred: omit LifecycleStageCode and keep the description, since the list has no single code for A1–A3 (broad); (b) split into two emissions, SOURCING and MANUFACTURING, if the figures exist (context's preference); (c) narrow description and value to A3 only; (d) a list code for A1–A3 together.
- Needs decision: no
- From: broad (F3), context (F3)

### rail/01#F6 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value comes from the world's EmissionBoundaryCode list, the life-cycle boundary of a product footprint, not the load state of transport equipment. A bench's manufacturing footprint involves no transport equipment whose fullness could be a parameter. The code is valid in its list but not the kind of value the element names. 39 files use this list in FullnessIndicationCode (`grep -rl --include='*.xml' 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"' world/examples | wc -l`).
- Condition: FullnessIndicationCode, where present, says how full a piece of transport equipment is; the product footprint's boundary is not carried in it.
- Options: (a) preferred: drop the element; the boundary is already expressed by LifecycleStageDescription (see F5) and can be named in EmissionStandardReference; (b) record the missing boundary element of EmissionCalculationMethod as a finding for the TC write-up.
- Needs decision: no
- From: broad (F2), context (F2)

### rail/01#F7 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Section 4.8: data copied from a party's master data into a document that does not use it. The order is the buyer's request for 192 benches DAP to its own siding; nothing in it depends on the seller's share listing on the Ferrano Stock Exchange, on either party's share capital, or on Valdara's warehousing provider Castrano Logistics (the order names no despatch party or place).
- Condition: every element of the parties' legal entity and service providers present in the order has a purpose in the order.
- Options: (a) preferred: drop SecurityListing, CorporateStockAmount and ServiceProviderParty from the order; (b) keep the service provider only if the order gets a role for it (e.g. a despatch party or place), and say so.
- Needs decision: no
- From: broad (F8), context (F6), parties (F7)

### rail/01#F8 · Low · Buyer's contact is its sales customer service
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party". In an order the buyer's contact is the one the seller asks about the order: purchasing. Lumeway's sales customer service serves Lumeway's own customers. The same contact is used for Lumeway in every role in the flow (consignee, accounting customer).
- Condition: the buyer's contact in the order is a purchasing (or order-handling) function of Lumeway, with matching name, job title and department.
- Options: (a) preferred: a purchasing contact for the buyer role; (b) role-specific contacts in Lumeway's master data so each document picks the fitting one.
- Needs decision: no
- From: broad (F7), parties (F6)

### rail/01#F9 · Low · Valdara's address tagged en-XB here, en-XU in the other examples
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: In every other example of the flow the English renderings of Valdara's address are tagged `en-XU` (e.g. `02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XU`). The order is written by the Bayvarran buyer, which may explain the tag (broad refuted it on that ground: both tags denote English, and `en-XB` is the issuer's English). The merge cannot settle whether the tag should follow the party or the issuer; the same party is in any case described in two ways within one flow.
- Condition: Valdara's address renderings carry the same languageIDs in every example of the flow, or the difference follows a stated rule (e.g. the issuer's locale) applied to every party of every document.
- Options: (a) preferred: describe Valdara as in the other examples (`en-XU`; the party's own master data); (b) keep the issuer's locale, but then apply it consistently and record the rule.
- Needs decision: yes
- From: parties (F4, first part); broad listed it under "Considered and refuted"

### rail/01#F10 · Low · "English" renderings of the seller's street name and legal form are Italian
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: Section 5 asks for each repeated rendering to be in the language its languageID names. The street name tagged as English (`en-XB`) is Italian ("street of the workshops"), and the legal form is Italian with an English gloss (own knowledge of Italian). The Urvanian rendering (`/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`) is a different name, so the Italian text is neither the local name nor English. Broad refuted the street name because the world consistently uses Italian-styled names (Ferrano, Serravona) as the English names of Urvanian places; that holds for proper names of places, but not obviously for a street name with a meaning, and not for a legal form, which is a description. The merge cannot settle whether this is the world's convention. 217 renderings in 102 files are tagged `en-XU` or `en-XB` and start with Via, Viale, Piazza, Valico, Corso, Largo, Strada or Banchina (`grep -rh --include='*.xml' -E 'languageID="en-X[UB]">(Via|Viale|Piazza|Valico|Corso|Largo|Strada|Banchina) ' world/examples | wc -l`, and `-l` for files).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms and the renderings are those names.
- Options: (a) preferred: record the Italianate English usage in the world's story and keep the values, if that is the intent (the legal form is the stronger case for an English rendering); (b) translate into English (e.g. "Workshops Street"); (c) tag the text with the language it is in, if Italian exists in the world.
- Needs decision: yes
- From: parties (F5); broad listed the street name under "Considered and refuted"

### rail/01#F11 · Low · Valdara's legal form in one untagged rendering
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: In the other examples of the flow Valdara's legal form is given in Urvanian and English (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`); here it has a single rendering without languageID, while the address next to it is rendered in both languages.
- Condition: Valdara's legal form is rendered like its address (both languages, each tagged), as in the other examples.
- Options: (a) preferred: both renderings with languageID, as in 02; (b) one tagged rendering, if the issuer's language rule (F9) says so.
- Needs decision: no
- From: parties (F4, second part)

### rail/01#F12 · Low · No requested delivery date in the order
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The order's Delivery names only the receiving party. The seller's transport request asks for delivery on a specific day (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-16`), which the buyer has not asked for anywhere in the flow.
- Condition: the order states when the buyer wants the goods (RequestedDeliveryPeriod or a promised date), or the story explains that the buyer leaves timing to the seller.
- Options: (a) preferred: add a RequestedDeliveryPeriod ending 2026-04-16 in `cac:Delivery`; (b) leave it out if the world's buyer leaves timing to the seller.
- Needs decision: no
- From: broad (F9), logistics (F2, second part)

### rail/01#F13 · Low · Delivery location described only in text, identified elsewhere by GLN
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Rail siding of Lumeway Distribution, Marrowdale`
- Why: Section 5: a location carries its identifier where the same place is identified elsewhere. The waybill identifies the same siding with a GLN (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9520610900015`, check digit correct, GS1 prefix 952 is GS1's range for examples) and Marrowdale by UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:UnloadingLocation/cbc:ID` = `XBMRW`). The order, which sets the delivery place under DAP, has only a description.
- Condition: the order's delivery location carries the siding's GLN (and a Name) used in the waybill.
- Options: (a) preferred: add `cbc:ID` with schemeID GS1 GLN and a Name to the DeliveryLocation (the buyer owns the GLN); (b) move the location into `cac:Delivery/cac:DeliveryLocation` and keep DeliveryTerms for the Incoterms rule only; (c) leave it if the GLN is assigned only later, and say so in the world.
- Needs decision: no
- From: logistics (F2, first part), parties (F8)

### rail/01#F14 · Low · Product passport data of the seller copied into the buyer's order
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: An order says what the buyer wants. Repairability score, maintenance frequency, resource consumption, packaging waste per bench, warranty text and the cradle-to-gate footprint are statements of the seller about its product; the buyer does not set them and the order does nothing with them. Item identification, description and the properties the buyer selects (frame colour) are enough to order.
- Condition: every item element in the order is something the buyer specifies or needs to identify the item.
- Options: (a) preferred: leave the product passport data to the documents that carry it (catalogue, product documentation VI-RM-B180); (b) keep it only if the story says the buyer orders against these declared values (e.g. a tender requirement), and say so.
- Needs decision: no
- From: context (F7)

### rail/01#F15 · Low · Item number in the world's scheme is a valid GTIN-12 with a US/Canada prefix
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- Why: The value passes the GS1 check digit (computed in the merge: 7 = 7), and as a GTIN-12 its leading digits fall in the UPC range used for the US and Canada (own knowledge), so it could be mistaken for a real GTIN, which the repository rule "fictional values must not be mistaken for real ones" forbids unless verified against GS1. Broad refuted this: the schemeID is the world's item scheme and the symbology is Code 128, so the value does not claim to be a GTIN. The merge does not follow the refutation, in line with the plastics merge (item number 771030000048): a scanner or reader sees a 12-digit number with a valid GS1 check digit regardless of the schemeID. Values 7710… with 12 digits occur in 51 files (`grep -rl --include='*.xml' '>7710[0-9]\{8\}<' world/examples | wc -l`).
- Condition: the world's item numbers cannot be read as assigned GTINs (other length or a failing GS1 check), or their verification against GS1 is recorded in the sources.
- Options: (a) preferred: change the world's item-number format; (b) record the GS1 verification.
- Needs decision: yes
- From: merge (broad listed it under "Considered and refuted")

## Checked and consistent
- Line arithmetic: 192 × 49 900 XUF = 9 580 800 XUF = line LineExtensionAmount = AnticipatedMonetaryTotal LineExtensionAmount = PayableAmount = TaxableAmount; tax 0 at 0 % (broad, money, context; redone in the merge).
- Tax category G with exemption EXP "Export of goods outside Urvania" fits a sale from Urvania to Bayvarra under DAP; the invoice applies the same treatment (broad, money).
- Price, quantity, totals and tax category agree with the sales invoice (`11-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9580800`); its OrderReference resolves to this order (money, logistics, broad).
- 192 EA here = `11-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `192` = `06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `192`, and "192 park benches" in the consignment summaries of 02, 03, 08 (logistics).
- DAP with delivery location at the Lumeway siding agrees with the transport documents (03, 08) and with Valdara paying the freight (02, 10); the invoice note says the price includes the carriage (broad, money, logistics).
- AccountingCostCode 4410 "Stock purchases" fits a wholesaler (ISIC 4649) buying for resale and is repeated in the invoice (money, context).
- Lumeway is described identically in 01, 02, 03, 06, 08 and 11; Valdara identically apart from F9/F11 (parties, broad).
- Roles: buyer Lumeway, seller Valdara, delivery party Lumeway with the same register ID; the invoice 11 has the same buyer and seller (parties).
- Tax schemes: buyer state sales tax (Upland State, XBL), seller national VAT (XUF), consistent within each party (parties).
- Codana Identification Agency as issuer of the property identifier: same ID and name as in 06 and 11 (parties).
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass (check_ids.py); GS1 prefix 952 is GS1's range for demonstrations; XU is a user-assigned ISO 3166 code. ISO 6523 ICD `0990` is not an assigned ICD (parties, own knowledge).
- Physics: 34 kg steel + 22.5 kg hardwood consumed per bench against 41.5 kg gross per bench with packaging (7968 / 192): consumption about 15 kg above product mass, plausible for casting and sawing losses; five slats of 1.8 m at about 700 kg/m³ (own knowledge) about 2.5 kg each; load capacity 450 kg over three seats plausible; dimensions 1800 × 620 × 780 mm and seat height 450 within 440–460 mm consistent (broad, logistics).
- Not verified: whether `XFER` is assigned in the real ISO 10383 MIC register (no register at hand; broad).

## Considered and refuted
- Bench weight against the gross weights of the transport documents (41.5 kg each including packaging) against 56.5 kg of materials consumed — refuted because consumption includes casting and sawing losses (broad).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode`: the buyer states the seller's Urvanian export exemption in its order — refuted because the Order's TaxTotal is the anticipated tax, the buyer knows the goods are exported, and the invoice applies the same treatment (money).
- `/Order/cbc:DocumentCurrencyCode`: a Bayvarran buyer ordering in XUF — refuted because ordering in the seller's currency is legitimate and the invoice follows it (money).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`: packaging waste not waste of the profiled item — refuted because WasteGenerated is "the waste generated by the profiled entity" and the packaging of each bench is plausibly counted for it (context; the presence question is F14).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`: suspected filler — refuted because a symbology is a legitimate attribute of the identification (context).
- `/Order/cbc:AccountingCost` = `Stock purchases`: checked as the buyer's cost text — fits (context).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`: does not resolve to an example — refuted as a broken reference because it is the seller's data sheet, a document the flow does not model, named unambiguously; the same for `VI-LCA-2025` and `VI-RM-B180` (logistics).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteMeasure` = `0.4`: palletised benches might contradict the container fill in the waybill — refuted here, the order says nothing about transport packaging; the container-fill question belongs to the waybill (logistics).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: a sales order desk as the seller's contact — refuted because that is the seller's order handling (parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: delivery party equal to the buyer — refuted because Delivery Party is "The Party who receives the goods" and under DAP to its own siding the buyer does (parties).
- Not followed by the merge (made findings): broad's refutations of `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027` as a GTIN (F15), of `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` as Italian text (F10), and of `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano` tagged `en-XB` instead of `en-XU` (F9); each finding gives broad's argument and why the merge does not follow it.

## Changed in the merge
- broad/F1, context/F1, logistics/F1 → F1: combined; options from all three, with "drop factor and base" preferred (two parts against broad's "factor 96").
- broad/F5, context/F4, parties/F1 → F2: combined; preferred option "drop" (parties) rather than `en-XB` (broad, context), aligned with the wood, plastics, air and rail 06–11 merges; count recounted (364).
- broad/F4, context/F5, parties/F3 → F4: Needs decision changed from yes (broad, context) to no (parties): the value itself says "Province", so moving it is an encoding change; aligned with the earlier merges.
- context/F2 → F6: Needs decision changed from yes to no (broad: no): dropping the element changes no story; the TC write-up is an option, not a condition.
- broad/F8, context/F6, parties/F7 → F7: combined into one finding with one line per place.
- logistics/F2 → F12 and F13: split, because the missing delivery date and the missing location identifier are different problems with different fixes; F12 combined with broad/F9, F13 with parties/F8.
- parties/F4 → F9 and F11: split into the languageID question (Needs decision yes, as in the wood and plastics merges: the tag may follow the issuer) and the single untagged legal form (Needs decision no); parties had said no for both.
- broad's refutation of the item number → F15: made a finding (Low, yes), aligned with the plastics merge.
