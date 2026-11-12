# LLM review: 07-ImportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/07-ImportCustomsDeclaration.xml`, Git blob `45419bf3fd0c23bb1b64bfa1ca0140c26025be7e` (committed)
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

### wood/07#F1 · Medium · A province of Urvania in `Region` instead of `CountrySubentity`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names a province, an administrative division, so it belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `01-RequestForQuotation.xml:/RequestForQuotation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`, with `CountrySubentityCode`). Affected here: the addresses of Valdara Industries and the Customs Administration of Urvania. The same element and value occur 219 times in 104 examples (merge recount: `grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano</cbc:Region>' world/examples | wc -l`, `grep -rl` for the files).
- Condition: No Urvanian address carries an administrative division in `cbc:Region`; the province, where given, is in `cbc:CountrySubentity` (with `cbc:CountrySubentityCode` if the world has a list for it).
- Options: (a, preferred) move the province of every Urvanian address to `CountrySubentity`, at the source of the Urvanian address format, as for Bayvarra; (b) if in the world the Urvanian "provinces" are economic regions, rename them so the name does not say "Province", record that in the story, and still give any administrative division in `CountrySubentity`.
- Needs decision: no (the name itself says "province"; option (b) only would change the world)
- From: broad/F3, parties/F1, context/F1

### wood/07#F2 · Medium · A language code in `Language/LocaleCode`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:ID` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". A locale is a language together with the region or country whose conventions apply. The value `en` with `listID="ISO 639"` is the language itself and only repeats `Language/ID`, so the element carries a meaning other than its definition (section 6 names "a language code in `LocaleCode`" as Medium). The examples already use locale-like tags (`en-XB`, `en-XU`) in `languageID`; the Urvanian parties carry no `LocaleCode`, so the parties are also described unevenly. The same element and value occur 362 times in 213 examples (merge recount, `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cbc:LocaleCode` present holds a locale (language plus country or region) from a list that defines locales, with a matching `listID`; otherwise it is absent.
- Options: (a, preferred) drop `LocaleCode` where no locale matters, as in a customs declaration; (b) carry a real locale such as `en-XB` from a list of locales (e.g. BCP 47) and name that list in `listID`.
- Needs decision: no
- From: broad/F4, parties/F2, context/F2

### wood/07#F3 · Medium · The customs authority is described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Customs Administration of Urvania`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105507`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: The customs administration is a public body (its own industry code is ISIC 8411, general public administration). Its legal entity nevertheless places it in the commercial register (`COMMERCIAL`, "Commercial register") and gives it `CompanyLiquidationStatusCode` `ACTIVE` ("Active, not in liquidation"), "A code signifying the party's liquidation status", which a state authority established by law does not have (checklist: "a public body or a department is not a company in a commercial register and has no liquidation status"). It also carries a VAT registration that the declaration does not use: the authority supplies nothing taxable here. Medium because the codes carry meanings that do not apply to this kind of party and contradict its own classification in the same party.
- Condition: The authority's legal entity, if present, describes it as a public body: no commercial-register scheme, no liquidation status, and no tax registration unless the declaration uses it.
- Options: (a, preferred) leave `PartyLegalEntity` (and `PartyTaxScheme`) out for the authority, which the declaration does not need; (b) describe its legal basis with a registration type for public bodies, if the world's list has one, and drop the liquidation status.
- Needs decision: no
- From: broad/F2 (Medium), parties/F6 (Low), context/F5 (Low)

### wood/07#F4 · Medium · Customs value leaves out the packing charge and states neither rate nor delivery basis
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`
- XPath: `08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `34800.00`
- XPath: `03-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". 3 456 000 XUF is the slats' price 34 560.00 XBL × 100; it leaves out the 240.00 XBL (24 000 XUF) billed to the importer for the heat-treated pallets, although under the transaction-value method packing costs borne by the buyer are added to the price (WTO Customs Valuation Agreement Art. 8.1(a)(iii); own knowledge of the broad and money parts). The rate 100 is not stated in any wood document; it is stated in other flows' `ExchangeRate` aggregates (merge check: `<cbc:CalculationRate>100</cbc:CalculationRate>` XBL→XUF in 9 examples, e.g. `energy/06-Invoice.xml`, `tender/26-Order.xml`). Nor does the declaration state the delivery terms (DAP Ferrano, in the order) that decide whether transport costs belong in the value.
- Condition: The declared customs value includes the packing charge (3 480 000 XUF at the rate 100), or the example states why not; the rate and the delivery terms the value rests on can be read from the declaration or the documents it references.
- Options: (a, preferred) declare 3 480 000 XUF, state the delivery terms (DAP) on the shipment, and make the rate derivable (a referenced invoice with an exchange rate, or a note); (b) keep the value and record the story's reason (e.g. a Trade Accord valuation rule) for leaving packing out. Which rule Urvanian customs applies is a story decision.
- Needs decision: yes
- From: broad/F1, money/F1

### wood/07#F5 · Low · Contacts are the sales customer-service desk whatever the role; the same hours for every party
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The contact of a party is "The primary contact for this party", read in its role here. The importer's contact should be the one who handles the import declaration and duties (customs or import clerk), not its order desk in Sales; a customer-service officer in Sales answers a seller's customers. `Customer service officer` occurs 395 times in 229 examples (merge recount, `grep -rho --include='*.xml'`). The broad part also notes that the border office is reachable only on weekdays 08:00–17:00 although goods arrive at the border; the merge finds the same note on all three full contacts of this example (importer, consignor, authority), which looks copied rather than a fact about the border post. The declaration itself is made within those hours (11:05 on a Friday), so the hours alone contradict nothing.
- Condition: The importer's contact is the one handling the import; each contact's hours, if given, are that contact's own.
- Options: (a, preferred) give each party role-specific contacts in the world and pick the one for the role in each document; (b) drop job title, department or the hours note where only a functional mailbox is known.
- Needs decision: no
- From: broad/F8, parties/F3, context/F8

### wood/07#F6 · Low · Valdara's master data the declaration does nothing with
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Every optional element needs a reason in this document (section 4.8). Valdara's share capital, stock-exchange listing and logistics service provider Castrano Logistics ("Warehousing and despatch") are carried in full; nothing in an import declaration uses them, and Castrano has no role (it appears in 9 of the 11 wood examples, never in a role of its own: `grep -l Castrano world/examples/wood/*.xml | wc -l`). The same block is in every full description of Valdara in the flow (01–09).
- Condition: Valdara's description in this declaration carries a service provider, share capital and security listing only if the declaration does something with them.
- Options: (a, preferred) leave them out of this document; fixing the party rendering per document type covers the flow; (b) if Castrano acts for Valdara at import (e.g. as declarant or receiving warehouse), give it that role, which changes the story.
- Needs decision: no
- From: broad/F9, parties/F4, context/F9 (party part)

### wood/07#F7 · Low · English-tagged renderings of Urvanian names are Italian
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The `en-XU` renderings of Urvanian street names and of Valdara's legal form are Italian. The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language the text is meant to be. 219 English-tagged street names in 104 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (merge recount, `grep -rhoE --include='*.xml' '<cbc:StreetName languageID="en[^"]*">(Via|Viale|Piazza|Corso|Strada|Valico|Banchina) '`; the broad part counted 217 in 102). Parties part (refuted): a street's proper name is commonly kept untranslated, and the world uses Italianate names consistently. The merge accepts that for street names but not for the legal form, a descriptive term; it cannot settle whether Italian is an intended exonym layer of the world.
- Condition: Every text tagged with an English `languageID` is English, or the world states that these Italian forms are the official English-language names and legal forms in Urvania.
- Options: (a, preferred if intended) record the convention in the world's story; (b) give English renderings.
- Needs decision: yes
- From: broad/F12; parties considered and refuted it, carried here with its argument

### wood/07#F8 · Low · Registration date 1 January 1996 looks like a default
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Marrowdale Sawmill Ltd carries 1996-01-01; the date occurs 271 times in 181 examples (merge recount, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`) for about 25 companies of every kind in the registers of all three countries (parties part), while other dates are specific (Valdara: 1962-04-12). Counter-argument (context part of `10-Order.xml`): it may be the date a register began; nothing in the examples says so.
- Condition: Each company's registration date is its own plausible date in the world, or the world documents an event that put these companies on the register on 1996-01-01; otherwise it is absent.
- Options: (a, preferred) its own date from the company's history; (b) record a 1996 (re-)registration in the story; (c) leave the date out.
- Needs decision: yes
- From: broad/F13, parties/F5

### wood/07#F9 · Low · The notifier is the importer itself
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: `NotifierParty` is "The Party who is responsible for contact on master level". It is Valdara Industries, already importer, consignee and signatory; naming it again adds nothing and implies a separate role nobody has here (no fillers).
- Condition: `NotifierParty` is absent, or names a party other than the importer with a reason in the story.
- Options: (a, preferred) leave it out; (b) name a broker, forwarder or Castrano Logistics if one handles the contact for Valdara, which changes the story.
- Needs decision: no
- From: broad/F6, parties/F7, context/F4

### wood/07#F10 · Low · `Shipment/GrossWeightMeasure` equals the goods' gross weight
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `21600`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `21600`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", the goods item's gross weight excludes the carrier's equipment; both are 21 600 kg (context part). Against it (logistics part's argument in `06-DespatchAdvice.xml`, this run): no transport equipment is declared anywhere in the flow (merge: no `TransportEquipment` in 04–07), so goods plus packaging may be the whole shipment weight. The merge cannot settle whether the road trailer counts as transport equipment in the world.
- Condition: The shipment weight either includes declared transport equipment, or no transport equipment exists and the equality is the stated reading across the flow.
- Options: (a, preferred) keep the value if the trailer is part of the vehicle; (b) declare the trailer and add its tare; (c) drop the shipment weight and keep the goods item's.
- Needs decision: yes
- From: context/F7

### wood/07#F11 · Low · The shipment carries no packages, consignment or transport
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `MS-SH-26-0632`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `4800`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cbc:ID` = `MS-CS-26-0629`
- Why: The import declaration declares the same shipment as the export declaration, but carries no packages or handling units, no consignment, no carrier and no transport mode, all of which the export declaration and the transport documents state. The number and kind of packages are standard data of an import declaration (Single Administrative Document box 31; own knowledge of the logistics part), and the consignment links the declaration to `04-TransportExecutionPlanRequest.xml` and the despatch advice. No value contradicts another example; the declaration is incomplete against them. (The logistics part also said the gross weight is missing; it is present, see F10.)
- Condition: The shipment states the packages of the goods item and identifies the consignment `MS-CS-26-0629` (and the transport mode or means), consistent with the export declaration.
- Options: (a, preferred) add a package or handling unit count and `Consignment/ID` with the carrier; (b) at least the consignment ID.
- Needs decision: no
- From: logistics/F1 (corrected)

### wood/07#F12 · Low · The customs value is not tied to the invoice it rests on
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000`
- XPath: `08-Invoice.xml:/Invoice/cbc:ID` = `MS-INV-26-0635`
- Why: The declaration references the export declaration but no commercial document. The customs value of an outright purchase rests on the transaction price in the commercial invoice MS-INV-26-0635, which exists at the time (issued 2026-02-26); without a reference the 3 456 000 XUF cannot be linked to the 34 560.00 XBL of the invoice line, nor the conversion checked.
- Condition: The declaration refers to the commercial invoice (with its document type) on which the customs value is based.
- Options: (a, preferred) add an `AdditionalDocumentReference` to MS-INV-26-0635 with its type.
- Needs decision: no
- From: broad/F7, context/F3

### wood/07#F13 · Low · Length repeated in `SellersItemIdentification/MeasurementDimension`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both under the seller's item identification and as `Item/Dimension[1]`; the identification carries no other dimension, so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the identification's `MeasurementDimension` is needed to distinguish variants and the example says so.
- Options: (a, preferred) keep the length in `Item/Dimension` only; (b) keep it in the identification if the item number is length-specific and that is stated.
- Needs decision: no
- From: broad/F11

### wood/07#F14 · Low · Commercial specification of the slats in a customs declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[2]/cbc:Name` = `Thickness tolerance`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[1]/cbc:TestMethod` = `Oven-dry method on samples from each kiln charge`
- Why: An import declaration needs the goods' classification, value, origin and quantity; the full commercial specification of the slats (thickness tolerance, test method, standard property identification) is carried as well and does nothing for customs (no fillers).
- Condition: The goods item carries only the item data the declaration uses (description, classification, origin, quantity, the forestry certificate), or the example states a customs use for the specification.
- Options: (a, preferred) leave the commercial properties out of the customs declaration; (b) keep a property customs checks (e.g. moisture for phytosanitary purposes) and say why.
- Needs decision: no
- From: context/F9 (item part)

### wood/07#F15 · Low · A 12-month validity period on the property "Planed on four sides"
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: `ItemProperty/UsabilityPeriod` is "The period during which this item property is valid". A planed surface stays planed; nothing says what would end the property after 12 months. The property that changes over time, moisture content, has no period.
- Condition: A `UsabilityPeriod` is present only on a property that can stop holding, with its meaning clear, or it is absent.
- Options: (a, preferred) drop it; (b) move it to a property that changes and say in the value qualifier what it means.
- Needs decision: no
- From: broad/F10, context/F10

### wood/07#F16 · Low · The signature ID contains the name of the example flow
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-IM-wood`
- XPath: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Signature/cbc:ID` = `VI-SIG-26-RFQ`
- Why: `Signature/ID` is "An identifier for this signature", assigned in the world by the signatory. Its last part `wood` is the name of the example flow in this repository, not a number a trader would assign; the importer's other signature in the flow has a world-style ID. The pattern occurs in 14 examples (merge recount, `grep -rlE --include='*.xml' 'SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: The signature ID follows the signatory's own numbering and contains nothing from the repository's structure.
- Options: (a, preferred) the importer's numbering, e.g. year and running number (VI-SIG-26-0634).
- Needs decision: no
- From: broad/F5, context/F6

## Checked and consistent
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631` is `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `MS-CD-26-0631`, the export declaration of the same shipment, issued the day before (broad, logistics, context).
- Shipment `MS-SH-26-0632`, 4800 EA, item `MS-SL-1800`, HS `440799`, origin `XB` and the forestry certificate `XB-FOR-2025-0118` agree with the export declaration and the despatch advice (broad, logistics).
- Roles: importer and consignee Valdara (the buyer of `03-Order.xml`), consignor Marrowdale; `IMPORT`/`FREECIRC`/`PURCHASE`, HS section `IX`, cargo type `GEN` fit the release of purchased timber (broad, logistics, context, parties).
- Dates: issued 2026-02-27 11:05, after the export declaration (2026-02-26 09:25) and within the transport window of `04-TransportExecutionPlanRequest.xml`; validity starts on the issue date (broad, logistics).
- Conversion: 34 560.00 XBL × 100 = 3 456 000 XUF, the rate stated in nine other examples (money; merge recount).
- The note "Duties paid by the importer's account at customs." fits DAP, under which the buyer bears import duties; the declaration's currency XUF is the importing country's (money).
- Parties: identifiers, tax schemes and endpoints follow the party's country; the customs authority is that of the declaring country; check digits pass (`check_ids.py`, re-run by the merge) (parties).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Bayvarran side` in an import declaration — refuted because the UBL 2.5 ImportCustomsDeclaration has only this office element, "Customs exit office of the goods being declared", and the value is the exit office of the export declaration it follows (from broad, logistics, context).
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.` without duty amounts or the account — refuted because the UBL 2.5 ImportCustomsDeclaration has no element for duty amounts, an assessment or a deferment account (from broad, money).
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` pointing to another country's export declaration — refuted because under the Trade Accord the export declaration is a plausible preceding declaration, and the ID resolves (from broad).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: Italian under an English tag — refuted as a world convention for proper names (from parties). The merge keeps it as F7 with both arguments.
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ICD — refuted because `0990` is not in `world/codelists/sources/peppol/ICD.xml` (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketCode` = `XFER`: a real MIC — refuted because it is not in `world/codelists/sources/iso10383/ISO10383_MIC.csv` (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: wrong ISIN check digit — refuted by `check_ids.py` (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: "number of shares" against an amount — refuted because the element is of type Amount; whether it belongs here is F6 (from parties).
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:AddressTypeCode` = `POSTAL` with a post box and a street — refuted because a postal address may carry both (from parties).
- `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411` — refuted because ISIC 8411 includes the collection of duties (from parties).
- `/ImportCustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Valdara Industries`, consignee equal to the importer — refuted because the importer receives the goods, consistent with 04 and 06 (from parties).
- `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `30` meaningless for a release — refuted because the definition ("a period, assigned by the issuer, during which the information in the declaration is valid") allows it (from context).
- The forestry certificate on the item as copied data — refuted because proof of sustainable origin is relevant to import controls on timber (from context).

## Changed in the merge
- parties/F6 and context/F5 (Low) → F3 Medium, with broad/F2: the codes describe a kind of party the authority is not and contradict its own ISIC 8411; aligned with the other merger's grading for 05. The VAT registration (parties only) added as a place.
- broad/F1 and money/F1 → F4: combined; the rate evidence (money) and the missing delivery basis (money) added to the broad wording; options merged.
- broad/F8 → F5: the customs office hours kept as part of the contact finding, with the merge's observation that the same note is on all three contacts and that the declaration time is within the hours (so not a contradiction).
- context/F9 → F6 and F14: split, because party master data and the item's commercial specification are different problems with different fixes.
- logistics/F1 → F11: corrected; the shipment and goods item do carry the gross weight (21 600 kg), so only packages, consignment, carrier and transport mode are missing; title changed.
- context/F1 "Needs decision: yes" → F1 "no", as in the other examples of this merge.
- broad/F12: count corrected from 217 in 102 files to 219 in 104 (merge recount); parties' refuted Italian-text candidate joined to it, "Needs decision: yes" kept.
- context/F7 → F10: "Needs decision: yes" added, because the logistics part's counter-argument (no transport equipment declared) could not be refuted.

## Outside this review
- Whether the goods can be cleared at 11:05 on 2026-02-27 after leaving Marrowdale on 2026-02-26 is a timeline question (from logistics).
- The contradiction between the transport window and the agreed delivery window is a finding of `04-TransportExecutionPlanRequest.xml` (from logistics).
