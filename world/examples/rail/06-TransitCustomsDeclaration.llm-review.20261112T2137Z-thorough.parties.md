# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/06-TransitCustomsDeclaration.xml`, Git blob `3619a51519aa158336a9817cd911b99963ad4351` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/06#F1 · Medium · Province in Region of three Urvanian addresses
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The consignee's address in the same document does so (`/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/06#F2 · Medium · Language code in LocaleCode of the consignee
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language. Locale Code is "A code signifying the locale in which this language is used." `en` (listID ISO 639) is a language code and repeats `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`. The value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the consignee's Language has no LocaleCode, or one that names a locale from a list of locales.
- Options: (a) drop it (preferred); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### rail/06#F3 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the site, not a street name; it has no meaning for the consignee's address in a customs declaration.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) remove it from the postal address (preferred); (b) state a gate, where a transport document needs it, at a delivery location.
- Needs decision: no

### rail/06#F4 · Medium · The rail carrier as freight forwarder (consolidator)
- XPath: `/TransitCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: Transit Customs Declaration. Freight Forwarder_ Party is "The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart who mirrors the consolidator's activity by dividing the consolidated consignment into its original components." Ferrano Rail Cargo is the carrier of this consignment (CarrierParty here, carrier and performing carrier in the waybill). It carries one consignment of one consignor to one consignee, and the waybill says it is not consolidated (`08-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`); no counterpart deconsolidates it.
- Condition: FreightForwarderParty is absent, or names a party that consolidates this consignment with others into one shipment that a counterpart splits again.
- Options: (a) drop FreightForwarderParty (preferred: the carrier is already in CarrierParty, and the transit declaration has no other role in UBL for the holder of the procedure); (b) if the story needs a forwarder, introduce one that consolidates, and change the waybill accordingly.
- Needs decision: yes

### rail/06#F5 · Medium · Customs administration described as a company in the commercial register
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105507`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: Section 5: a public body or a department is not a company in a commercial register and has no liquidation status. The Customs Administration of Urvania (ISIC 8411, general public administration) is described as registered in the commercial register with a company number and as "not in liquidation" (Party Legal Entity. Company Liquidation Status Code: "A code signifying the party's liquidation status"), which applies to companies. The same pattern — a party with ISIC 8411 and a commercial-register scheme — occurs 90 times in 75 example files (counted with lxml over `world/examples/*/*.xml`).
- Condition: the customs administration's legal entity, if present, describes a public authority (e.g. established by law, registered in a register of public bodies or none) and has no liquidation status.
- Options: (a) drop PartyLegalEntity for the authority, keeping name and identifier (preferred: the declaration needs neither); (b) a register of public bodies (with its own registration type) and no liquidation status.
- Needs decision: no

### rail/06#F6 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge; "Valico di Confine" means "border crossing"); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/06#F7 · Low · Declarant's contact is the sales order desk
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara makes the declaration (Transit Exporter_ Party: "The Party who makes the Transit Customs Declaration, or on whose behalf…") and signs it. Customs' questions about the declaration go to the person responsible for customs and export formalities, not to the order desk that takes customer orders. Valdara is also the notifier ("responsible for contact on master level") without a contact of its own there.
- Condition: the declarant's contact is Valdara's customs, export or shipping function.
- Options: (a) a customs/export contact for Valdara (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/06#F8 · Low · Consignee's contact is its sales customer service
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Section 5: a consignee's contact receives goods; under transit, the consignee also presents the goods at the office of destination. Lumeway's sales customer service serves Lumeway's own customers.
- Condition: the consignee's contact is Lumeway's goods-receiving or customs function.
- Options: (a) a goods-in or customs contact (preferred); (b) role-specific contacts in Lumeway's master data.
- Needs decision: no

### rail/06#F9 · Low · Master data the declaration does nothing with
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: a transit declaration does nothing with the declarant's stock-exchange listing, its warehousing provider (Castrano Logistics plays no role in the declaration) or the share capital of declarant and consignee.
- Condition: every legal-entity and service-provider element present has a purpose in the declaration.
- Options: (a) drop them here (preferred); (b) a reduced party description for customs documents.
- Needs decision: no

### rail/06#F10 · Low · VAT registration of the customs administration
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `VAT`
- Why: Section 4.8 and the legal-entity checklist: the authority processing a transit declaration acts as a public authority; its VAT registration (if a customs administration has one at all, for taxable side activities) has nothing to do with processing the declaration.
- Condition: the customs party carries no tax scheme, or one with a stated reason in this document.
- Options: (a) drop PartyTaxScheme for the authority (preferred); (b) keep it only if the world gives the authority taxable activities and the document uses it.
- Needs decision: no

### rail/06#F11 · Low · Customs contact is the border office, not the office that processes the declaration
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDepartureLocation/cbc:Name` = `Customs office Ferrano Intermodal Hub`
- Why: Customs Party is "The Authority who is legally responsible for processing the Declaration"; a transit declaration is lodged and accepted at the office of departure (Office Of Departure Location: "A Customs Office where the customs declaration placing goods under transit is accepted"), here the customs office at the hub. The authority's contact is the border office instead, which only sees the goods when they cross.
- Condition: the customs party's contact is the office that accepts and processes the declaration (the office of departure), or the contact's name and note explain why the border office is the contact.
- Options: (a) the office of departure at the hub as contact (preferred); (b) keep the border office and say in the contact's note what it is for.
- Needs decision: no

### rail/06#F12 · Low · Customs offices identified by description only
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDepartureLocation/cbc:Name` = `Customs office Ferrano Intermodal Hub`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDestinationLocation/cbc:Name` = `Customs office Marrowdale`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfTransitLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs post at the rail border station, Urvanian side`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfEntryLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- Why: Section 5: locations carry identifiers where they are places of a register. Customs offices are identified in transit by a customs office reference number (own knowledge: e.g. the COL reference numbers in NCTS); the declaration gives only descriptive names, partly phrased as descriptions ("Customs post at the rail border station, …") rather than office names, and the same offices are repeated under several elements without anything that ties them to an office register of the world.
- Condition: each customs office location carries an identifier of the world's customs office list (and its name), the same for the same office throughout the document.
- Options: (a) customs office identifiers from a world or Trade Accord list (preferred, if the world defines one); (b) at least names that are office names, used identically.
- Needs decision: no

## Checked and consistent
- Valdara (transit exporter, consignor, notifier, signatory), Lumeway (consignee) and Ferrano Rail Cargo (carrier) have the same identifiers and full descriptions as in the other examples of the flow.
- Codana Identification Agency (`XU-R-105644`) as issuer of the property identifier is the same as in `01-Order.xml` and `11-Invoice.xml`.
- The customs party's identifier `XU-R-105507` is the issuer named for this declaration in `08-Waybill.xml` (see the waybill's review for the contradiction this causes there).
- GLN `9520610900008`, ISIN `XU0001042501`, containers `FRXU1044175` and `FRXU1044180`: check digits correct.

## Considered and refuted
- `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`: an authority not reachable when the goods arrive — refuted: the train passes the border on a Tuesday between about 13:00 and 13:20 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`), within those hours.
- `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`: a generic job title for a customs contact — refuted: vague, but not contrary to the role.
- `/TransitCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Valdara Industries`: notifier equal to the declarant — refuted: Notifier_ Party is "The Party who is responsible for contact on master level", and the declarant can hold that role.
