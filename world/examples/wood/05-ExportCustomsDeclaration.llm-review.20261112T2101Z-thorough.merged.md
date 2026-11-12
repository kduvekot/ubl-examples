# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
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

### wood/05#F1 · Medium · Language code `en` in `Language/LocaleCode`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". `en` with `listID="ISO 639"` is a language code only and repeats `Language/ID`; a locale is a language as used in a country (cf. the examples' `languageID` values `en-XU`, `en-XB`). The Urvanian parties carry no `LocaleCode`. 362 occurrences in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; files with `grep -rl`).
- Condition: Every `cbc:LocaleCode` in this example holds a locale with a `listID` naming a list of locales, or is absent.
- Options: (a, preferred) leave `LocaleCode` out where no locale matters, as here; (b) a real locale such as `en-XB` from a list of locales, named in `listID`.
- Needs decision: no
- From: broad, context, parties

### wood/05#F2 · Medium · Urvanian province in `Region` instead of `CountrySubentity`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country …", which UBL puts in `CountrySubentity`, as the Bayvarran addresses of the same document do (`/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Affected: Trasvia Haulage and Valdara Industries. 219 occurrences in 104 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`; files with `grep -rl`).
- Condition: No Urvanian address in this example carries the province in `cbc:Region`; it is in `cbc:CountrySubentity` (with a code where the world has one), and `cbc:Region`, if present, holds a region in the UBL sense.
- Options: (a, preferred) move the province to `CountrySubentity` in every Urvanian address; (b) if Ferrano is an economic region in the world, rename it without "Province" and record that in the story.
- Needs decision: no
- From: broad, context, parties

### wood/05#F3 · Medium · Declared value leaves out the pallet charge the buyer pays, and its basis is not stated
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`
- XPath: `08-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `34560.00`
- XPath: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `34800.00`
- Why: `GoodsItem/DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". 34 560.00 XBL is the price of the slats alone; the invoice bills 240.00 XBL more for the heat-treated export pallets they travel on, so the goods as sold with their packing are worth 34 800.00. Under customs valuation practice packing costs borne by the buyer are part of the value (WTO Customs Valuation Agreement Art. 8.1(a)(iii)), and statistical export values are commonly the invoiced value including packing at the border (own knowledge). At the same time the price is DAP Ferrano and so includes transport beyond the Bayvarran border, while an export value is usually stated on a border basis. The declaration states neither its delivery terms nor how the value was derived, so it cannot be reconciled with the invoice. The import declaration repeats the same base (`07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000` XUF, 34 560.00 × 100).
- Condition: The declared value either includes the packing charge, or the example states why it does not; and the basis of the value (delivery terms or border-value adjustment) can be read from the declaration.
- Options: (a, preferred) declare 34 800.00 XBL (goods with packing) and state the delivery terms (DAP) on the shipment, so the basis is visible; (b) declare a border value (34 800.00 less the transport share beyond the border) and say so; (c) keep 34 560.00 and explain in the story why packing is excluded. Which value Bayvarran customs rules require is a story decision.
- Needs decision: yes
- From: money, broad

### wood/05#F4 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `20410137`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The Customs and Border Service of Bayvarra is a public administration (its own ISIC code 8411, "General public administration activities"). Its `PartyLegalEntity` places it in the Federal business register with `CorporateRegistrationTypeCode` `COMMERCIAL` ("Commercial register") and gives it `CompanyLiquidationStatusCode` `ACTIVE`; `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status". A customs administration is established by law, is not entered in a commercial register and cannot be in liquidation, so these values contradict the party's own industry code and describe a kind of party it is not; nothing in the declaration uses them.
- Condition: The authority carries no liquidation status and no commercial-register scheme; its `PartyLegalEntity` is either absent or describes it as a public body.
- Options: (a, preferred) leave `PartyLegalEntity` out for the authority (the declaration does not need it); (b) a registration type for public bodies, if the world's list has one, and no liquidation status.
- Needs decision: no
- From: broad, context, parties

### wood/05#F5 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". The Bayvarran sawmill and the Urvanian haulier share it; it occurs 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`; files with `grep -rl`), for about 25 companies of every kind in all three registers (parties part), while other dates are specific (Valdara 1962-04-12). It reads as a filler unless the world has an event that explains it.
- Condition: Each company's registration date is its own date in the world, or the world documents why these companies share 1996-01-01; otherwise it is absent.
- Options: (a, preferred) each company its own date; (b) record a 1996 re-registration in the story if intended; (c) leave the date out.
- Needs decision: yes
- From: broad, parties

### wood/05#F6 · Low · Exporter's and consignee's contacts are sales customer-service desks
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: `Party/Contact` is "The primary contact for this party", read in its role. Customs asks the exporter about the export, so its contact should be shipping or customs, not the sales office; the consignee's contact is the one who receives the goods (goods-in), not an order desk in Sales. `Customer service officer` occurs 395 times in 229 examples (`grep -rho --include='*.xml' 'Customer service officer' world/examples | wc -l`; files with `grep -rl`).
- Condition: The exporter's contact handles the export declaration and the consignee's receives the goods, with name, job title and department agreeing.
- Options: (a, preferred) role-specific contacts per party in the world, chosen by the role in each document; (b) drop `JobTitle` and `Department` where only a functional mailbox is known.
- Needs decision: no
- From: broad, context, parties

### wood/05#F7 · Low · `Shipment/GrossWeightMeasure` equals the goods' gross weight
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", while the goods item's gross weight includes packing but excludes the carrier's equipment. Both carry 21 600 kg, so (context part) the shipment value is the goods weight and does not meet the shipment definition if the truck's trailer counts as transport equipment. Counter-argument (broad and logistics parts): the shipment declares no transport equipment (no container, swap body or trailer as equipment); the truck is the means of transport, whose weight is in neither figure, so the two are equal. Whether a trailer of an articulated truck is "transport equipment" here depends on how the world models road transport; the merge could not settle it.
- Condition: `Shipment/GrossWeightMeasure` either includes the declared transport equipment, or equals the goods' gross weight because none is declared and the example models it that way; or it is absent.
- Options: (a, preferred) drop the shipment gross weight and keep it on the goods item (and the consignment), where its definition clearly fits; (b) declare the trailer as transport equipment and add its tare; (c) keep it, if the world models trucks without equipment.
- Needs decision: yes
- From: context (broad and logistics refuted it; see "Considered and refuted")

### wood/05#F8 · Low · Text tagged as English is Italian
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The English renderings (tagged `en-XB`) of the Urvanian street names are Italian, and so are the legal forms (untagged here, see F10). 219 English-tagged street names in 104 examples start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml' 'StreetName languageID="en-X[A-Z]">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): street names are proper names, commonly left untranslated, and the world uses Italianate names consistently. That does not cover the legal forms. The merge could not settle whether the Italian forms are the world's English exonyms.
- Condition: Every text tagged (or meant) as English is English, or the world's story states that these Italian forms are the English-language names used for Urvania.
- Options: (a, preferred if intended) record the convention in the story and give the legal forms in English; (b) English renderings throughout.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/05#F9 · Low · Same Urvanian text tagged `en-XB` here and `en-XU` in the Urvanian-issued examples
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: Valdara's address (and Trasvia's town) carry `en-XB` in this Bayvarran declaration and `en-XU` in 01, 03, 07 and 09. If `languageID` describes the language of the text, the same text should carry the same tag; 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) ' world/examples | wc -l`). Counter-argument (parties part): the tag names the variant of the issuer's English, consistently within each document. Both readings are possible; the examples do not say which rule they follow.
- Condition: The same text carries the same `languageID` in every example of the flow, or the rule that the tag follows the issuer is documented.
- Options: (a, preferred) one rule, documented in the world; (b) document that the tag follows the issuer's locale.
- Needs decision: yes
- From: broad (parties refuted it; see "Considered and refuted")

### wood/05#F10 · Low · Urvanian legal forms in one untagged rendering, unlike the addresses
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Ban Kumek`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`
- Why: Trasvia's and Valdara's addresses have two tagged renderings (`qau` and English), their legal forms only one, without `languageID`; in the Urvanian-issued examples Valdara's legal form has both, each tagged (`01-RequestForQuotation.xml:/RequestForQuotation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`). Within this example address and legal form follow different language rules.
- Condition: Within this example each Urvanian party's legal form follows the same language rule as its address.
- Options: (a, preferred) both renderings, each tagged; (b) one tagged rendering, with the reason why the address keeps its Urvanian rendering.
- Needs decision: no
- From: parties

### wood/05#F11 · Low · Packages and transport mode at the border not declared
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- Why: The goods item gives 4800 slats and the gross weight, but not the number and kind of packages (96 bundles, per `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Slats for 960 benches: five per bench, 96 bundles of 50.`), and the shipment states neither the mode of transport at the border nor the identity of the truck that will present the goods (own knowledge: packages, mode at the border and means of transport are standard data of an export declaration, e.g. boxes 31, 21 and 25 of the Single Administrative Document). The declaration can be understood without them, so this is a completeness remark. (The part of the parts' findings about the exit office's identifier is refuted in the merge; see "Refuted in the merge".)
- Condition: The declaration states the packages of the goods item and the transport mode and means of transport at the border, or the story explains why the world's export procedure does not need them.
- Options: (a, preferred) add a package count (`TransportHandlingUnit` or package) to the goods item and a `ShipmentStage` with road transport mode and the truck's registration; (b) only the package count and transport mode.
- Needs decision: no
- From: broad, logistics

### wood/05#F12 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length is given as a measurable dimension of the seller's item identification and again as `Item/Dimension[1]`; the identification carries no other dimension, so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the dimension under the identification distinguishes item variants and the example says so.
- Options: (a, preferred) keep it in `Item/Dimension` only; (b) keep it in the identification if the item number is length-specific and that is stated.
- Needs decision: no
- From: broad

### wood/05#F13 · Low · The commercial specification of the slats in a customs declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:TestMethod` = `Oven-dry method on samples from each kiln charge`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[2]/cbc:Name` = `Thickness tolerance`
- Why: An export declaration needs the goods' classification, value, origin and quantity. The commercial specification of the slats (the test method of the moisture content, its standard property identification, the thickness tolerance) is the requirement the buyer measures delivery against and does nothing for customs (section 4.8). The forestry certificate is a different case (see "Considered and refuted").
- Condition: The item in the declaration carries only properties customs uses (or the example states why customs needs them).
- Options: (a, preferred) keep description, classification, origin and certificate, and leave the commercial properties out; (b) keep them with a stated reason.
- Needs decision: no
- From: context (split off from its master-data finding)

### wood/05#F14 · Low · A 12-month validity on the property "Planed on four sides"
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what ends the property after 12 months. The moisture content, which does change, carries no period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear, or it is absent.
- Options: (a, preferred) remove it from the surface property (or, with F13, the property altogether); (b) move it to a property that changes and say what it means.
- Needs decision: no
- From: broad, context

### wood/05#F15 · Low · Valdara's master data the declaration does nothing with
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: An export declaration needs the consignee's identity and address. Valdara's share capital, stock-exchange listing and logistics service provider are master data the declaration does nothing with (section 4.8). Castrano appears in 9 of the 11 wood examples (`grep -l Castrano world/examples/wood/*.xml | wc -l`), never in a role of its own.
- Condition: The consignee's description carries share capital, listing and service provider only if the declaration uses them.
- Options: (a, preferred) leave them out of this document; (b) give Castrano a role the declaration uses, which changes the story.
- Needs decision: no
- From: broad, context, parties

### wood/05#F16 · Low · The supporting document is the order, given by ID only; the invoice is not referred to
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `/ExportCustomsDeclaration/cbc:IssueTime` = `09:25:00`
- XPath: `08-Invoice.xml:/Invoice/cbc:ID` = `MS-INV-26-0635`
- XPath: `08-Invoice.xml:/Invoice/cbc:IssueTime` = `08:56:00`
- Why: The only supporting document is the buyer's order (`03-Order.xml`), referenced without `DocumentTypeCode` or `DocumentType`, so the declaration does not say what `VI-PO-26-0627` is. The commercial invoice, which normally evidences the export sale and its value, already exists when the declaration is made (both on 2026-02-26, the invoice half an hour earlier) and is not referenced.
- Condition: Every document reference of the declaration says what kind of document it is, and the declaration references the commercial invoice of the sale (or the story says why not).
- Options: (a, preferred) type the order reference and add a reference to `MS-INV-26-0635` typed as commercial invoice; (b) replace the order reference by the invoice.
- Needs decision: no
- From: broad, logistics, context

### wood/05#F17 · Low · The signature ID contains the name of the example flow
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `MS-SIG-EX-wood`
- Why: `Signature/ID` is "An identifier for this signature", assigned in the world by the signing party. Its last part `wood` is the name of the example flow in this repository, not a number a trader would assign; the other signatures of the flow use world-style IDs (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Signature/cbc:ID` = `VI-SIG-26-RFQ`, `02-Quotation.xml:/Quotation/cac:Signature/cbc:ID` = `MS-SIG-26-QT`). The pattern occurs in 14 examples (`grep -rlE --include='*.xml' 'SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: The signature ID follows the signing party's own numbering and contains nothing from the repository's structure.
- Options: (a, preferred) number it like the exporter's other documents (e.g. MS-SIG-26-0630); (b) drop the suffix.
- Needs decision: no
- From: broad, context

## Checked and consistent
- Shipment `MS-SH-26-0632` and consignment `MS-CS-26-0629` are those of `04-TransportExecutionPlanRequest.xml`, `06-DespatchAdvice.xml` and `07-ImportCustomsDeclaration.xml`; gross weight 21 600 kg is the same wherever stated; the carrier is the haulier of the transport request (same ID and licence) (broad, logistics, context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `MS-CD-26-0631` is the previous declaration the import cites (`07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631`) (broad, logistics).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VI-PO-26-0627` resolves to `03-Order.xml`, whose line amount is the declared 34 560.00 (money, logistics).
- Dates: issued 2026-02-26 09:25, validity from the same day for 90 days, covering the transport (to 2026-03-01); consistent with `/ExportCustomsDeclaration/cbc:Note` = `Declared electronically before the goods leave.` and the transport window starting 2026-02-26 (broad, logistics, context).
- Codes: HS 440799 with section IX, cargo type GEN, PERMANENT, SALE resolve and fit a sale of sawn timber; origin XB agrees with order and invoice (broad, logistics, context).
- Currency XBL is the exporter's and the invoice's currency; quantity 4800 EA and goods description agree with order and invoice (money).
- Physics, recalculated in the merge: 4800 × 0.006498 m³ = 31.19 m³; 21 600 kg gives 693 kg/m³ including packaging, plausible for kiln-dried hardwood (650–750 kg/m³, own knowledge); within a full-truck payload of about 24 t (broad, logistics).
- Parties identical to their other full descriptions in the flow apart from language renderings; identifiers and tax schemes consistent; `check_ids.py` passes; the customs authority is that of the country of the declaration, and the exporter is the seller of `03-Order.xml` (parties).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`: copied carrier data — refuted: the carrier and its international haulage permit are relevant to customs for an export by road (from broad, parties; context agrees).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800` in EA, where the supplementary unit of HS 4407 is m³ (own knowledge) — refuted: `GoodsItem/Quantity` is "The number of units making up this goods item", which 4800 slats are; a supplementary unit would be a separate statement (from logistics).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411` for a customs authority — refuted: ISIC Rev.4 class 8411 includes the administration of fiscal affairs and the collection of duties (own knowledge) (from parties).
- The forestry certificate on the item: copied — refuted: timber regulations commonly require proof of legal and sustainable harvest at the border (from context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `90`: filler — refuted: an export declaration is commonly valid for a limited period within which the goods must exit (from context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427` (real ICD?), `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER` (real MIC?), `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501` (check digit) — refuted: not in the repository's ICD and MIC lists; `check_ids.py` passes (from parties).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: definition says "number of shares" — refuted: the element is an Amount; whether it belongs here is F15 (from parties).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`: exit office without an identifier — refuted: no example of the world identifies a customs office by a code (the customs office locations of all examples carry names only; the name "Customs post at the land border" occurs in 7 examples, `grep -rl --include='*.xml' 'Customs post at the land border' world/examples | wc -l`), so there is no identifier to use, and the name names the place (from parties; count re-checked in the merge). This also refutes the exit-office part of broad/F7 and logistics/F2 (see "Refuted in the merge").
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: an authority contact should be reachable when the goods cross — refuted: the declaration is made and valid from Thursday 2026-02-26 within those hours (from parties). This also refutes that part of broad/F8 (see "Refuted in the merge").
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600` equal to the goods item's — refuted by the broad and logistics parts (no transport equipment declared). Not followed in full: kept as F7 (context), Needs decision: yes, with both arguments.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian text tagged English — refuted by the parties part as a world convention. Not followed: kept as F8, Needs decision: yes.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano` tagged `en-XB` here, `en-XU` elsewhere — refuted by the parties part (the tag follows the issuer's English). Not followed: kept as F9, Needs decision: yes.

## Refuted in the merge
### broad/F7 (part) and logistics/F2 (part) · Low · Exit office not identified
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`
- The parts' finding: the exit office is named in prose, without an identifier or address, while the customs authority has a postal address (Border Crossing Road 36, Marrowdale) (broad); it is identified only by a descriptive name, without a customs office identifier (logistics). Condition: the exit office is identified (ID or address) as the authority's other places are.
- Refuted because: no example of the world identifies a customs office by code (see "Considered and refuted", from parties), so there is no identifier to use, and the name names the place unambiguously (the same post appears on the Urvanian side in the import). The authority's postal address is its office address, not that of the border post, so it gives no address to copy. The remaining parts of both findings (packages, transport mode, means of transport) stay as F11.

### broad/F8 (part) · Low · Customs border office reachable only on weekdays
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- The part's finding: the customs border office is reachable only on weekdays 08:00–17:00, although it is the office where the goods leave the country. Condition: the border office's hours cover the time goods pass.
- Refuted because: the declaration is made at 09:25 on Thursday 2026-02-26 and the transport starts the same day, so the goods can pass within the stated hours; nothing in the flow has them cross outside them (with the parties part). The rest of broad/F8 (exporter's and consignee's contacts) stays as F6.

## Changed in the merge
- broad/F3, context/F2, parties/F2 → F1; broad/F2, context/F1, parties/F1 → F2: combined; context's "Needs decision: yes" on Region set to no; LocaleCode's preferred option set to "leave out" (context's), as in the other merged reviews.
- money/F1 (Medium), broad/F4 (Low) → F3: combined at Medium (money's), because the declared value is the price without the packing the buyer pays, against the invoice of the same sale, and its basis is not stated; aligned with the merge of wood 06–11 for the import declaration.
- broad/F1 (Medium), context/F4 (Low), parties/F7 (Low) → F4: combined at Medium (broad's), because the registration type and liquidation status contradict the party's own ISIC code; aligned with the merge of wood 06–11.
- broad/F14, parties/F6 → F5: combined.
- broad/F8, context/F7, parties/F3 → F6: combined; the customs office's hours moved to "Refuted in the merge".
- context/F6 → F7: Needs decision changed from no to yes, with the broad and logistics refutations as counter-argument (cannot settle); aligned with the merge of wood 06–11.
- broad/F13 → F8: count corrected (219 in 104 files instead of 217 in 102); the legal form added; parties' counter-argument added.
- broad/F12 → F9: Needs decision changed from no to yes, with the parties' refutation as counter-argument.
- parties/F5 → F10: wording only.
- broad/F7, logistics/F2 → F11: combined; the exit-office part moved to "Refuted in the merge".
- broad/F11 → F12; broad/F10, context/F9 → F14: wording only.
- context/F8 split: the commercial item properties → F13 (a finding of its own, because it concerns the item, not the party); the party master data → F15, combined with broad/F9 and parties/F4.
- broad/F6, logistics/F1, context/F3 → F16; broad/F5, context/F5 → F17: combined.

## Outside this review
- The note says the goods were declared "before the goods leave" at 09:25, while the despatch advice was issued at 08:31 the same day; whether the truck left before 09:25 is a timeline question for the cross-flow review (from broad).
