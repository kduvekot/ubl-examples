# LLM review: 05-ExportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/05-ExportCustomsDeclaration.xml`, Git blob `485e09ca0ec698fc71593b783ad60898b71c45fd` (committed)
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

### wood/05#F1 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Customs and Border Service of Bayvarra`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `20410137`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The customs authority is a public body (its industry code is 8411, general public administration), but its PartyLegalEntity places it in the commercial register (CorporateRegistrationTypeCode `COMMERCIAL`) and gives it a liquidation status. CompanyLiquidationStatusCode is "A code signifying the party's liquidation status", which a state authority does not have, and a commercial-register entry asserts something about the authority that is not true of a public body.
- Condition: The authority carries no liquidation status and no commercial-register scheme; if it has an identifier in a public-sector register, that register is named as such.
- Options: (a, preferred) Drop CompanyLiquidationStatusCode and CorporateRegistrationScheme (or use a public-body registration type, if the world's list has one); (b) leave PartyLegalEntity out for the authority.
- Needs decision: no

### wood/05#F2 · Medium · Urvanian province carried in Region
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is defined as "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division, which UBL puts in CountrySubentity ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses in the same flow do use CountrySubentity and CountrySubentityCode for their states, so the two countries are encoded differently. The same value occurs 219 times in 104 XML files (`grep -r --include='*.xml' -c '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address carries an administrative division in Region; the province, where given, is in CountrySubentity (with CountrySubentityCode if the world has a list for it).
- Options: (a, preferred) Move the province to CountrySubentity, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world a non-administrative region, keep Region but name it as such, without "Province of".
- Needs decision: no

### wood/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/05#F4 · Low · Declared value leaves out the pallet charge billed with the goods
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`
- XPath: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `34800.00`
- Why: The goods are declared at 34560.00 XBL, the price of the slats alone. The invoice bills 240.00 XBL more for the heat-treated export pallets the slats travel on, so the value of what crosses the border as sold is 34800.00. Whether the export value includes packing depends on the declaration's valuation basis, which the example does not state (own knowledge: export statistical values are commonly the invoiced value including packing).
- Condition: The declared value either includes the packing charge, or the example states the valuation basis that excludes it.
- Options: (a, preferred) Declare 34800.00 (goods with their packing), consistent with the import valuation; (b) state the basis (e.g. a statistical value without packing).
- Needs decision: yes

### wood/05#F5 · Low · Signature ID contains the example flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `MS-SIG-EX-wood`
- Why: The signature identifier ends in "wood", the name of the example flow, not a number the exporter would assign; the other signatures of the flow use document-style IDs (e.g. `MS-SIG-26-QT`). The same pattern (SIG-<code>-<flow name>) occurs in 14 XML files (`grep -rlE --include='*.xml' 'SIG-[A-Z]+-[a-z]+<'`). A construction label in business data is a filler-like value.
- Condition: The signature ID is an identifier the signatory would assign, without the flow name.
- Options: (a, preferred) Use the exporter's numbering (e.g. MS-SIG-26-0630); (b) drop the ID's suffix.
- Needs decision: no

### wood/05#F6 · Low · Declaration refers only to the order, not to the invoice issued before it
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `VI-PO-26-0627`
- XPath: `08-Invoice.xml:/Invoice/cbc:IssueTime` = `08:56:00`
- XPath: `/ExportCustomsDeclaration/cbc:IssueTime` = `09:25:00`
- Why: The export declaration references the purchase order with an ID only (no type code or description saying it is the buyer's order), but not the commercial invoice MS-INV-26-0635, issued the same morning before the declaration, which is the document that supports the declared value.
- Condition: The declaration's references say what they are, and it references the invoice its value rests on.
- Options: (a, preferred) Add a DocumentTypeCode to the order reference and a reference to MS-INV-26-0635; (b) replace the order reference by the invoice.
- Needs decision: no

### wood/05#F7 · Low · Packages and the exit office are given only loosely
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side`
- Why: The goods item gives 4800 slats but not the 96 bundles they are packed in (only 06-DespatchAdvice.xml says so, in a note), although a customs declaration normally declares number and kind of packages; the exit office is named in prose without an identifier or address, while the customs authority has a postal address (Border Crossing Road 36, Marrowdale).
- Condition: The declaration states the number and kind of packages, and the exit office is identified (ID or address) as the authority's other places are.
- Options: (a, preferred) Add GoodsItem/ContainingPackage (or Shipment/TransportHandlingUnit) with 96 bundles, and an ID or address for the exit office; (b) at least the package count.
- Needs decision: no

### wood/05#F8 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The exporter's contact for a customs declaration is its sales office, not someone responsible for export formalities; the consignee's contact is Valdara's order desk (Sales) rather than its goods-in; the customs border office is reachable only on weekdays 08:00–17:00, although it is the office where the goods leave the country.
- Condition: Each contact fits the party's role in the declaration, and the border office's hours cover the time goods pass.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/05#F9 · Low · Valdara's master data the document does nothing with
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's SecurityListing (listed shares) and its ServiceProviderParty (Castrano Logistics, "Warehousing and despatch") are carried in full in this export declaration (for the consignee), which does nothing with either: no security is traded, and Castrano plays no role (the goods go to Valdara's own goods-in in Ferrano). This is party master data copied into a document that does not use it (section 4.8).
- Condition: The party carries in this document only data the document uses, or the example gives the reason for the security listing and the service provider.
- Options: (a, preferred) Leave SecurityListing and ServiceProviderParty out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which would change the story.
- Needs decision: no

### wood/05#F10 · Low · Usability period of 12 months on the 'Surface' property
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: ItemProperty/UsabilityPeriod is "The period during which this item property is valid". A planed surface does not cease to be planed after 12 months; nothing in the example says what the period stands for (a storage or warranty period would be a property of its own).
- Condition: The UsabilityPeriod is absent, or it sits on a property whose validity really expires, and the example makes clear what it means.
- Options: (a, preferred) Remove the UsabilityPeriod from 'Surface'; (b) move it to a property that expires (e.g. a moisture guarantee while stored as agreed).
- Needs decision: no

### wood/05#F11 · Low · Length repeated in SellersItemIdentification/MeasurementDimension
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both as a measurable dimension of the seller's item identification and as Item/Dimension[1]. The identification carries no other variant dimension (width and thickness are only in Item/Dimension), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the MeasurementDimension under the identification is needed to distinguish item variants and the example says so.
- Options: (a, preferred) Keep the length in Item/Dimension only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no

### wood/05#F12 · Low · Same Urvanian address tagged en-XB here and en-XU elsewhere
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same English rendering of the same Urvanian address is tagged `en-XB` in this example and `en-XU` in `07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` (and 01, 03, 09) for Valdara's address. The languageID describes the language of the text, which does not change with the sender's country, so the same text should carry the same tag. 55 Urvanian street names are tagged `en-XB` over the examples (`grep -rhoE --include='*.xml' 'StreetName languageID="en-XB">(Via|Viale|Piazza|…) '`).
- Condition: The same rendering of the same address carries the same languageID in every example of the flow.
- Options: (a, preferred) Tag the rendering by the language variant of the text (the Urvanian English, en-XU) everywhere; (b) document that the tag follows the sender's locale.
- Needs decision: no

### wood/05#F13 · Low · English (en-X?) renderings of Urvanian names are Italian
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The second rendering of the Urvanian street name (and, where present, of the legal form) is tagged as English (`en-XU`/`en-XB`) but is Italian ("Via …", "Piazza …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be, and the languageID does not describe it. 217 English-tagged street names in 102 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml'`).
- Condition: Every text tagged with an English languageID is English, or the world states that these Italian forms are the official English-language names in Urvania.
- Options: (a) Give the English rendering in English (e.g. "Workshops Street"); (b) if the Italian forms are the world's exonyms, record that in the world's story so the tag is explained. Preference: (b) if it is intended, as the pattern is consistent; otherwise (a).
- Needs decision: yes

### wood/05#F14 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day).
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Shipment `MS-SH-26-0632` and consignment `MS-CS-26-0629` match 04 and 06; gross weight 21600 kg is the same at shipment and goods-item level and in 04 and 06.
- Customs declaration `MS-CD-26-0631` is the previous declaration the import refers to (`07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631`).
- Item data, HS 440799, section IX nature code and origin XB agree with the order and invoice.
- Physics: one slat is 1.800 × 0.095 × 0.038 m = 0.006498 m³, 4800 slats = 31.19 m³; kiln-dried ash or oak at 12 % moisture weighs about 650–750 kg/m³ (own knowledge), i.e. 20.3–23.4 t of wood, plus 96 heat-treated pallets; the stated 21 600 kg gross is plausible and within an ordinary full-truck payload (about 24 t).
- Validity: start 2026-02-26 for 90 days covers the transport (to 2026-03-01).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`: Shipment gross weight is defined to include transport equipment, yet equals the goods-item weight — refuted: the load travels on a truck without container or other transport equipment declared, so there is no equipment weight to add.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: copied master data — refuted: the haulier's international haulage licence is relevant to the border crossing.

## Outside this review
- The note says the goods were declared "before the goods leave" at 09:25, while the despatch advice was issued at 08:31 the same day; whether the truck left before 09:25 is a timeline question for the cross-flow review.
