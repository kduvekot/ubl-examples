# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/04-ExportCustomsDeclaration.xml`, Git blob `d23054c9c05d2dbe62a877d4d23f4891f2983d71` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### energy/04#F1 · High · Montebrio Power named as consignee of gas that Ferrano Energy bought
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- Why: `ConsigneeParty` is "The Party who receives the goods." This declaration exports 39200 MWh of March gas on shipment `KG-SH-26-0154` with Montebrio Power as the only consignee. Montebrio, however, buys and imports only 36800 MWh (06, and 05 on the same shipment ID), and Kelpstone sells the remaining 2400 MWh of the same March gas from the same field, measured at the same border station, to Ferrano Energy (07; 36800 + 2400 = 39200, and the gross weights agree at 75 kg/MWh: 2 940 000 / 39 200 = 2 760 000 / 36 800 = 75). So for 2400 MWh this document names a receiver that the invoices of the flow contradict. No import declaration in the flow names Ferrano Energy as importer.
- Condition: the parties who receive the exported gas, as stated in the export declaration, agree with the buyers in 06 and 07 and with the import declaration(s) for the shipment.
- Options: (a) declare both consignees, e.g. one goods item per buyer with its own consignee (GoodsItem/Delivery or a consignment per buyer), and add an import declaration for Ferrano Energy's 2400 MWh; (b) preferred if the story allows: let the export cover only Montebrio's 36800 MWh and give Ferrano Energy's gas its own export and import declarations, so each declaration has one consignee; (c) if Montebrio really receives all the gas and passes 2400 MWh on, change 07 so that the story says so.
- Needs decision: yes

### energy/04#F2 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs and Border Service of Bayvarra is a public authority (ISIC 8411). `CorporateRegistrationTypeCode` `COMMERCIAL` says it is registered in a commercial register, and `CompanyLiquidationStatusCode` ("the party's liquidation status") presumes a company that can be wound up; neither applies to a government agency. Over all `*.xml`, 18 `CustomsParty`/`AuthorityParty` elements in 18 files carry a liquidation status, and 18 a `COMMERCIAL` registration type (lxml counts).
- Condition: the authority's legal entity contains no commercial-register type and no liquidation status; if it is listed in a register at all, the registration type names a register of public bodies.
- Options: (a) preferred: reduce the authority's `PartyLegalEntity` to its registration name and the identifier under which public bodies are listed (or leave it out); (b) add a registration type for public bodies to the world's list and use it.
- Needs decision: no

### energy/04#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; a locale names where (or in which regional variant) the language is used, e.g. `en-XB`, which is exactly the variant the flow uses elsewhere as `languageID`. The value `en` with listID `ISO 639` repeats `Language/ID` and names no locale. `LocaleCode` = `en` occurs 362 times in 213 `*.xml` examples (lxml count).
- Condition: `LocaleCode` holds a locale (language plus region, e.g. `en-XB`, from a stated locale list), or is absent.
- Options: (a) preferred: give Bayvarran parties the locale `en-XB` with a locale list ID; (b) leave `LocaleCode` out, since `Language/ID` already says English.
- Needs decision: no

### energy/04#F4 · Medium · Province held in Region
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as this very document does for the exporter (`/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). 219 occurrences in 104 `*.xml` examples (lxml count).
- Condition: no Urvanian address carries its province in `cbc:Region`.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no

### energy/04#F5 · Low · The consignee's Urvanian address and legal form are tagged as Bayvarran English
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: The English renderings of Montebrio Power's Urvanian street and town carry `languageID="en-XB"` (English as used in Bayvarra), while the same texts are tagged `en-XU` in `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale` and in 03 and 09. The legal form, given in `qau` and `en-XU` there, is a single untagged text here. The label follows the issuer's country rather than the language of the rendering, so the same address is described differently in the flow. Over all `*.xml`, 107 Urvanian addresses in 39 files carry an `en-XB` rendering, and 34 SUA legal entities in 34 files have an untagged `CompanyLegalForm` (lxml counts).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: always tag the English rendering of an Urvanian name `en-XU` and keep the `qau` rendering of the legal form; (b) if the world intends documents to tag renderings by the issuer's locale, record that rule and apply it to the legal form too.
- Needs decision: no

### energy/04#F6 · Low · Exporter's contact is its sales manager
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Commercial`
- Why: The exporter's contact in an export declaration is the one customs turns to with questions about the declaration (export or customs compliance, or gas logistics/dispatching). The gas sales manager of the commercial department is the party's general master-data contact and appears unchanged in every Kelpstone document of the flow (06, 07, 08, 09).
- Condition: the exporter's contact deals with the export formalities or the gas movement.
- Options: (a) preferred: give Kelpstone an export/customs or dispatching contact in its customs documents; (b) leave the contact out.
- Needs decision: no

### energy/04#F7 · Low · The plant's InformationURI is the company's home page
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cbc:WebsiteURI` = `https://www.kelpstone.example`
- Why: `Location/InformationURI` is "The Uniform Resource Identifier (URI) of a document providing information about this location." The value is the party's own web site, already given in `WebsiteURI`; it is not a document about the gas treatment plant.
- Condition: `InformationURI` points to information about the location itself, or is absent.
- Options: (a) preferred: leave it out; (b) point it to a page about the plant if the story has one.
- Needs decision: no

## Checked and consistent
- Kelpstone Gas (`20412877`) is described identically (59 leaf values) as exporter here and as consignor/supplier in 05, 06, 07, 08 and 09.
- Exporter: a natural gas producer (ISIC 0620) with the right of disposal over its gas fits "The Party who exports the goods"; its customs trader ID `XB-TR-412877` is the one used in 05.
- `CarrierParty` Kelpstone Gas: the consignment moves by fixed installation (mode 7, means type 71 pipeline) on journey `KG-P1-2603`, which carries Kelpstone's prefix; a producer operating its export pipeline is plausible.
- The customs party is the Bayvarran authority, which processes an export from Bayvarra; ISIC 8411 covers duty and tax collection on goods (own knowledge of ISIC Rev.4).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT` with `TaxLevelCode` `STATE`: an exporter registered only for a state sales tax — refuted because the world gives Bayvarra a state-level sales tax, and the territory (`Northern Territory`) agrees with the address.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`: a generic title for a customs contact — refuted because the contact name `Border office` makes clear which office it is, and job title and department agree.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Energy trading`: a trader as consignee contact — refuted because for pipeline gas the receiver's trading desk nominates and takes over the quantities.
