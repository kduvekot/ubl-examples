# LLM review: 06-DespatchAdvice.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/06-DespatchAdvice.xml`, Git blob `e24fe891b1bc7348a4d9bc77947476a40bc1b949` (committed)
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

### wood/06#F1 · Medium · A language code in `Language/LocaleCode`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply (e.g. English as used in Bayvarra). The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples themselves already use locale-like tags (`en-XB`, `en-XU`) in `languageID`. The Urvanian parties of the flow carry no `LocaleCode`, so the parties are also described unevenly. The same element and value occur 362 times in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `grep -rl` for the files).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters, since this document gains nothing from it; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47 tags) and name that list in `listID`, consistent with the `languageID` values the world uses.
- Needs decision: no
- From: broad/F3, parties/F2, context/F2

### wood/06#F2 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`, with `CountrySubentityCode`). Affected here: the addresses of Valdara Industries and Trasvia Haulage. The same element and value occur 219 times in 104 examples (merge recount: `grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`, `grep -rl` for the files).
- Condition: No Urvanian address carries an administrative division in `cbc:Region`; the province, where given, is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if the world has a list for it).
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, at the source of the Urvanian address format, as for Bayvarra; (b) if in the world the Urvanian "provinces" are economic regions, not administrative divisions, rename them so the name does not say "Province", record that in the story, and still give any administrative division in `CountrySubentity`.
- Needs decision: no (the name itself says "province"; option (b) only would change the world)
- From: broad/F2, parties/F1, context/F1

### wood/06#F3 · Medium · Despatch advice states neither despatch nor expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `MS-SH-26-0632`
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-02-26`
- XPath: `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and services"; the receiver uses it to plan receipt. The shipment carries no `Delivery` (no `EstimatedDeliveryDate`, `PromisedDeliveryPeriod`, `ActualDeliveryDate`) and no `Despatch/ActualDespatchDate`, so the document does not say when the goods leave Marrowdale or when Valdara can expect them; the reader has to assume despatch on the issue date, which would be implied by absence (excluded by the repository's rules). The note asks for a check "on arrival" without saying when that is. This matters more because the transport window differs from the delivery window agreed in `02-Quotation.xml:/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02` (a finding of `04-TransportExecutionPlanRequest.xml`, this run). Medium: information the document's purpose depends on is missing.
- Condition: The despatch advice states the despatch date (and time) and the expected delivery date or period at the consignee.
- Options: (a, preferred) add `Shipment/Delivery` with `Despatch/ActualDespatchDate` (and time) and `EstimatedDeliveryDate` (or an estimated delivery period), consistent with the transport window of `04-TransportExecutionPlanRequest.xml`; (b) at least the despatch date.
- Needs decision: no
- From: broad/F1 (dates part), logistics/F1, context/F3

### wood/06#F4 · Low · Status codes that say "no status"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Despatch Advice with respect to its original state. This code may be used if the document precedes the event and is subsequently found to be incorrect and in need of cancellation or revision." Nothing here is cancelled or revised, so the definition's condition is not met; `NoStatus` ("No status on document", "Line has no status.") states only that there is nothing to state, which its absence would say as well (no fillers, IND5/IND6). The broad part refuted this as "an original despatch advice with no status change is what the code says"; the merge disagrees because the definition ties the element to a revision situation, which this original is not. `DocumentStatusCode` `NoStatus` occurs in 26 examples (`grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus' world/examples | wc -l`).
- Condition: A document or line status code is present only where the document has a status to convey (a replacement, cancellation or copy).
- Options: (a, preferred) drop both elements; (b) use them in an example where a status really applies.
- Needs decision: no
- From: context/F4 (refuted by broad, see "Considered and refuted")

### wood/06#F5 · Low · Contacts are the sales customer-service desk whatever the role
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The contact of a party is "The primary contact for this party", read in the role it has in this document. Marrowdale as despatch party should be reached at despatch or the timber yard; Valdara as delivery customer at goods-in, which the note asks to check the goods. A customer-service officer in a Sales department answers a seller's customers; it fits neither role, and for Valdara (a buyer) not even its own sales function. The parties carry the same contact in every example of the flow whatever their role. `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml' 'Customer service officer'`), with contacts named `Purchasing`, `Buying office` and `Goods inwards` among them (parties part), so job title and department look like a default.
- Condition: Each contact has a name, job title and department that fit the role the party has in this despatch advice, and agree with each other.
- Options: (a, preferred) give each party role-specific contacts in the world (purchasing, goods-in, despatch, customs, accounts) and pick the one for the role in each document; (b) drop `JobTitle` and `Department` (or the contact) where only a functional mailbox is known.
- Needs decision: no
- From: broad/F4, parties/F3, context/F6

### wood/06#F6 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd (Bayvarra) and Trasvia Haulage SRU (Urvania) both carry 1996-01-01. The date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), for about 25 companies of every kind in the registers of all three countries (parties part, counted with lxml), while other dates are specific (Valdara: 1962-04-12). A New Year's Day shared by unrelated companies in three registers reads as a filler, unless the world has an event for it. Counter-argument (context part of `10-Order.xml`): it may be the date a register began; the merge could not find that in the examples, and the review may not read the world story, so this is for a person to settle.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) give each company its own registration date from its history; (b) record a 1996 (re-)registration in the story; (c) leave the date out where the world has none.
- Needs decision: yes
- From: broad/F10, parties/F6

### wood/06#F7 · Low · Party master data this despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cbc:Purpose` = `International road haulage`
- Why: Every optional element needs a reason in this document (section 4.8, no fillers). Valdara's share capital and stock-exchange listing, its logistics service provider Castrano Logistics ("Warehousing and despatch") and the carrier's haulage permit are carried in full, and the despatch advice does nothing with them: no security is involved, Castrano has no role (it appears in 9 of the 11 wood examples, never in a role of its own: `grep -l Castrano world/examples/wood/*.xml | wc -l`), and the permit is not a subject of the despatch. Here it also raises a question of the story (parties part): if Castrano runs Valdara's warehousing, the goods might be received by Castrano rather than at Valdara's business address, which this document does not say. The permit is the weakest place: a carrier's operating authority can be of interest to the receiver, but nothing in the document refers to it.
- Condition: The parties carry in this document only data it uses: a service provider, share capital, security listing or permit is present only if the document does something with it (e.g. the service provider receives the goods).
- Options: (a, preferred) leave the security listing, share capital, service provider and permit out of this document and identify the parties by the data a despatch advice needs; fixing the party rendering per document type covers the whole flow; (b) if Castrano receives the goods for Valdara, make that explicit (delivery party or location), which changes the story.
- Needs decision: yes (whether Castrano has a part in this delivery)
- From: broad/F5, parties/F4, context/F7

### wood/06#F8 · Low · Legal form of the Urvanian parties in one untagged rendering, unlike their addresses
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Ban Kumek`
- Why: Valdara Industries and Trasvia Haulage give their address in two tagged renderings (Urvanian `qau` and English) but their legal form only once and without `languageID`. In the Urvanian-issued examples Valdara gives both renderings of its legal form, each tagged (`01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). So the same party is described differently between examples, and within this example address and legal form follow different language rules.
- Condition: Within this example each Urvanian party's legal form follows the same language rule as its address: both renderings, each tagged, or one rendering with its `languageID`.
- Options: (a, preferred) render the legal form like the address (Urvanian and English, each tagged), as the Urvanian-issued examples do; (b) if a Bayvarran issuer writes only English, tag the single rendering and keep the Urvanian address rendering for delivery.
- Needs decision: no
- From: parties/F5

### wood/06#F9 · Low · The same Urvanian address is tagged `en-XB` here and `en-XU` elsewhere
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- Why: The same English rendering of Valdara's address is tagged `en-XB` in this Bayvarran-issued example and `en-XU` in the Urvanian-issued ones (01, 03, 07, 09). Broad part: `languageID` names the language of the text, which does not change with the sender, so the same text should carry the same tag (55 Italianate Urvanian street names are tagged `en-XB` over the examples, merge recount with the same pattern for `en-XB`). Parties part (refuted): the tag names the language variant of the issuer's English, and the text is the same. Both readings are defensible; the merge cannot settle which rule the world wants.
- Condition: The same rendering of the same address follows one documented tagging rule in every example of the flow.
- Options: (a, preferred) tag the rendering by the variant of the text itself (en-XU for Urvanian addresses) everywhere; (b) keep the issuer's variant and record that rule.
- Needs decision: yes
- From: broad/F8; parties considered and refuted it (CityName), carried here with its argument

### wood/06#F10 · Low · English-tagged renderings of Urvanian names are Italian
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The second rendering of Urvanian street names is tagged English (`en-XB` here) but is Italian ("Via …"); the legal form is Italian with an English gloss. The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be. 219 English-tagged street names in 104 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (merge recount, `grep -rhoE --include='*.xml' '<cbc:StreetName languageID="en[^"]*">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) '`; the broad part counted 217 in 102). Parties part (refuted): a street's proper name is commonly kept untranslated in English text and the world uses Italianate names consistently (`Via delle Officine` 80 times over `*.xml`). The merge accepts that argument for street names but not for the legal form, which is a descriptive term, not a proper name; it cannot settle whether Italian is an intended exonym layer of the world.
- Condition: Every text tagged with an English `languageID` is English, or the world states that these Italian forms are the official English-language names and legal forms in Urvania.
- Options: (a, preferred if intended) record the convention in the world's story so the tag is explained; (b) give English renderings (e.g. "Workshops Street", "Urvanian public limited company").
- Needs decision: yes
- From: broad/F9; parties considered and refuted it (StreetName), carried here with its argument

### wood/06#F11 · Low · `Shipment/GrossWeightMeasure` equals the goods' gross weight
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure` = `21600`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". Context part: the value equals the goods' gross weight, so it does not include the trailer. Logistics part (refuted): the shipment has no transport equipment (no container or trailer is declared; the truck is a means of transport), so goods plus packaging is the whole shipment weight. The merge finds no `TransportEquipment` in 04–07 (`grep TransportEquipment`), which supports the logistics reading, but a road trailer can be transport equipment in UBL; neither reading is certain.
- Condition: `Shipment/GrossWeightMeasure` either includes the weight of declared transport equipment, or the shipment has none and the value is goods plus packaging, stated consistently across the flow.
- Options: (a, preferred) keep the value and declare no transport equipment (as now), if the trailer is part of the vehicle in the world; (b) declare the trailer as transport equipment and add its tare to the shipment weight; (c) drop the shipment weight and keep it on the consignment.
- Needs decision: yes
- From: context/F5; logistics considered and refuted it, carried here with its argument

### wood/06#F12 · Low · Packaging (bundles, pallets) only in a line note
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`
- XPath: `03-Order.xml:/Order/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`
- XPath: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Heat-treated export pallets`
- Why: The despatch advice is where the receiver learns how the goods arrive. The 96 bundles appear only in free text, and the heat-treated pallets the buyer pays a charge for appear nowhere in the logistics data of the flow: no `TransportHandlingUnit`, `Package`, package count, packaging type or marks. The goods-in check the note asks for has nothing structured to check the number of packages against.
- Condition: The shipment states its handling units or packages (number and kind: the bundles of 50 and the pallets they are on), consistent with 4800 slats and with the pallet charge.
- Options: (a, preferred) add `Shipment/TransportHandlingUnit` (pallets, packaging type and count) containing `Package` (bundles of 50), or at least a handling unit and package count; (b) if the bundles are not palletised, remove the pallet charge from quotation, order and invoice, which needs the story to say which.
- Needs decision: no
- From: broad/F1 (packaging part), logistics/F2

### wood/06#F13 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both as a measurable dimension of the seller's item identification and as `Item/Dimension[1]`. The identification carries no other dimension (width and thickness are only in `Item/Dimension`), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the identification's `MeasurementDimension` is needed to distinguish item variants and the example says so.
- Options: (a, preferred) keep the length in `Item/Dimension` only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no
- From: broad/F7

### wood/06#F14 · Low · A 12-month validity period on the property "Planed on four sides"
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what would end the property after 12 months or from when they count. The property that does change over time, the moisture content (`AdditionalItemProperty[1]`), has no such period. The same property with its period is in 7 examples (`grep -rl --include='*.xml' '<cbc:Value>Planed on four sides' world/examples | wc -l`).
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear from the document, or it is absent.
- Options: (a, preferred) drop it from the surface property; (b) move it to a property that changes (e.g. moisture content while stored as agreed) and say in the value qualifier what it means.
- Needs decision: no
- From: broad/F6, context/F8

## Checked and consistent
- Reference `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VI-PO-26-0627` resolves to `03-Order.xml`; `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1` matches its only line; `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `4800` equals the ordered quantity (broad, logistics, context; re-checked).
- Note arithmetic: 960 benches × 5 = 4800 = 96 bundles × 50; 50 is the item's `PackSizeNumeric` (broad, logistics, context; recalculated).
- Shipment `MS-SH-26-0632`, consignment `MS-CS-26-0629` and the gross weight 21 600 kg agree with `04-TransportExecutionPlanRequest.xml` and `05-ExportCustomsDeclaration.xml`; carrier Trasvia Haulage is the haulier of the transport request and is described identically in 04, 05 and 06 (broad, logistics, parties).
- Lot `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `MS-L26-0223` agrees with `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-02-23`, after the order (2026-02-22) and before despatch (broad, logistics, context).
- Physics (recalculated): one slat 1.800 × 0.095 × 0.038 m = 0.006498 m³; 4800 slats = 31.19 m³; at 650–750 kg/m³ for kiln-dried hardwood (own knowledge of the parts) 20.3–23.4 t; 21 600 kg / 96 bundles = 225 kg per bundle against 211–244 kg of wood per bundle; within an ordinary full-truck payload of about 24 t (broad, logistics).
- Parties: Marrowdale identical in all eleven examples, Valdara in its nine full descriptions apart from the language renderings above; identifiers, tax schemes and endpoints follow the party's country; check digits pass (`check_ids.py`, re-run by the merge); carrier ISIC 4923 with an international haulage permit fits its role (parties).

## Considered and refuted
- `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus` and `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`: suspected filler — refuted because an original despatch advice with no status change is what the code says (from broad). The merge disagrees and keeps it as F4.
- `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` used in a despatch advice — refuted because its definition in this context is "The quantity despatched (picked up)" (from broad).
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `21600`: shipment weight should include transport equipment — refuted because the shipment has no transport equipment; the truck is a means of transport (from logistics). The merge could not settle it and keeps it as F11 with both arguments.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-02-23`: too short after the order of 2026-02-22 for kiln drying 38 mm hardwood — refuted because the manufacture date can be the date the slats were cut and planed from timber kiln-dried earlier (from logistics).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text under an English tag — refuted as a world convention for proper names (from parties). The merge keeps it as F10 with both arguments, because the legal form is not a proper name.
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`: tagged `en-XB` here, `en-XU` in the Urvanian-issued examples — refuted because the tag follows the issuer's English (from parties). The merge keeps it as F9 with both arguments.
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ICD — refuted because `0990` is not in `world/codelists/sources/peppol/ICD.xml` (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: a real MIC — refuted because it is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv` (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted because `check_ids.py` reports it correct (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: UBL's definition says "number of shares" while the value is an amount — refuted because the element is of type Amount, so the amount of the capital stock is the only reading (a remark on UBL's wording); whether it belongs here is F7 (from parties).
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`: carrier contact — refuted because it fits the carrier role (from parties).
- Lot `MS-L26-0223` with the property "Kiln charge" `K-07` as filler — refuted because it ties the slats to the kiln charge whose samples the test method refers to (from context).
- `AdditionalItemProperty[1]/cbc:ID` = `MC` repeating `cbc:NameCode` — refuted because the ID identifies this occurrence while the name code classifies it (from context).
- `Item/cbc:PackQuantity` = `1` with `PackSizeNumeric` = `50` — refuted because together they state the pack structure that the note ("96 bundles of 50") uses (from context).

## Changed in the merge
- broad/F1 → F3 and F12: split, because the missing dates are Medium (the purpose depends on them) while the packaging in a note is a completeness remark (Low), as the logistics part graded them.
- context/F3 (Low) → F3 Medium: a despatch advice without despatch or expected delivery lacks information its purpose depends on (section 6).
- context/F1 "Needs decision: yes" → F2 "no": the value names itself a province; only the alternative option would change the world.
- context/F2, parties/F2 and broad/F3 options → F1: preferred option is dropping `LocaleCode` (context) rather than a locale value (broad, parties), because nothing in a despatch advice uses a locale; both kept.
- broad/F5, parties/F4, context/F7 → F7: grouped; the carrier permit (context only) added as a place; "Needs decision: yes" from parties kept because of the Castrano question.
- broad/F9: count corrected from 217 in 102 files to 219 in 104 (merge recount).
- parties: the refuted `en-XB`/`en-XU` and Italian-text candidates made findings F9 and F10 together with broad/F8 and broad/F9, Low with "Needs decision: yes", because the merge could not settle them.
- logistics' refuted shipment-weight candidate and context/F5 → F11, Low, "Needs decision: yes".
- broad's refuted status-code candidate and context/F4 → F4, with the definition's revision condition as the reason.

## Outside this review
- Issue time 08:31 against the export declaration at 09:25 "before the goods leave" (`05-ExportCustomsDeclaration.xml`): a timeline question (from broad).
- Whether the truck could leave Marrowdale on the morning of 2026-02-26 and the goods be cleared in Urvania by 11:05 on 2026-02-27 (from logistics).
