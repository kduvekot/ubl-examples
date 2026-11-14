# LLM review: 30-ExportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/30-ExportCustomsDeclaration.xml`, Git blob `badd401509d1f287a27ff308ccae49e844329ef6` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/30#F1 · High · The declared goods are the grey variant; the shipment is moss green
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The buyer changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), the seller accepted on 25 March (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`), and the shipment this declaration covers (CL-SH-26-0216) was despatched in that colour (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`). The declaration identifies the same 40 benches as the grey variant: extended identifier `GRY`, colour attribute "Frame in Ferro grey" and property "Frame colour" = "Ferro grey". A declaration that describes goods differently from those on the lorry is a discrepancy at the customs check. The same grey data is in 29 (structured part), 31, 32 and 33 (`grep ExtendedID tender/*.xml`).
- Condition: The item's variant and colour data describe the goods of the shipment (moss green, RAL 6005), or the declaration carries no colour data.
- Options: (a) the green variant's identification and colour (extended identifier, attribute code and text, property; the world's colour list needs a code for it), in every document from the despatch on (preferred by broad and context: the declaration then says what is presented); (b) reduce the item to what customs needs, without variant and colour (preferred by logistics; fits F11 as well). Merge: (a), because the colour is part of the goods' identity and the same item data recur in 31-33.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### tender/30#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", ValueBaseMeasure "The base quantity to which the value factor applies". 0.82 × 1 EA = 0.82, not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Arithmetic within one aggregate that does not hold (section 6 High). The same triple is in 39 examples (`grep -l 'ValueFactorNumeric>0.82<' world/examples/*/*.xml`), from `25-Catalogue.xml` on.
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: (a) drop ValueFactorNumeric and ValueBaseMeasure (preferred, as in every earlier merge: the value stands on its own); (b) state a real factor and the activity it applies to.
- Needs decision: no
- From: broad (F3), logistics (F2)

### tender/30#F3 · Medium · A province in `Region`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country …, such as the name of its county, province, or state", i.e. `CountrySubentity`. The Bayvarran addresses of the same document put their state in `CountrySubentity` (`Coastal State`). 219 occurrences in 104 files (`grep -rho --include='*.xml' '<cbc:Region>Province of'`).
- Condition: The province of an Urvanian address is in `CountrySubentity` (with a code where a list exists); `Region` is absent or holds a region in the sense of the definition.
- Options: move the value to `CountrySubentity` (preferred, all parts); or record that Urvania's format has a postal region only (parties' alternative).
- Needs decision: no
- From: broad (F4), parties (F1), context (F3)

### tender/30#F4 · Medium · The customs value leaves out the colour charge that the invoice exempts as part of the exported goods
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1996000`
- Why: "The total declared value for customs purposes of the goods item." 1996000 XUF = 40 × 49900, the catalogue price of the standard bench (19960.00 XBL at 100 XUF to the XBL). The benches exported are those of the order change, for which the seller accepted a special-colour charge of 200.00 XBL on 25 March (`28-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`). The exporter's own invoice treats the charge as part of the exported goods: `32-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `200.00` under the export category, and `32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00` with reason `EXP` ("Export of goods outside Urvania"). The declaration evidences 19960.00 only, so 200.00 XBL (20000 XUF) of the exemption claimed on the invoice have no export evidence. By the usual transaction-value rule (own knowledge: WTO Valuation Agreement, price actually paid or payable) a charge for the colour of the goods is part of their value; the world's valuation rule is not stated, but whatever it is, it cannot differ between the exporter's two documents for the same goods. The import declaration declares the same 19960.00 (`31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`).
- Condition: The declared customs value equals the value the invoice of the same goods treats as exported (2016000 XUF at the stated rate), or a stated valuation rule explains the difference.
- Options: (a) declare 2016000 XUF (preferred by all four parts); (b) keep 1996000 and bill the colour as a service outside the goods' value in the invoice, with its own tax category; (c) state the valuation basis.
- Needs decision: no
- From: broad (F5), money (F1), logistics (F3), context (F5)

### tender/30#F5 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the environmental emission." The value is a system boundary of a product footprint; the item is a bench, not transport equipment. The boundary is already stated in the sibling lifecycle stage description.
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent; the boundary is stated elsewhere.
- Options: (a) remove the element and keep the boundary in the lifecycle stage description (preferred); (b) in addition, record for the UBL TC write-up that the emission calculation method has no element for the system boundary.
- Needs decision: no
- From: context (F2)

### tender/30#F6 · Medium · A language code as locale
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used". The value (listID `ISO 639`) repeats the language code of the sibling `cbc:ID` and names no locale. The Urvanian parties (`qau`) carry no LocaleCode. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `LocaleCode` holds a bare language code; each one present names a locale from a list of locales.
- Options: (a) remove it (preferred by parties and context: it adds nothing); (b) a real locale (`en-XB`) from a list that defines locales (preferred by broad).
- Needs decision: no
- From: broad (F4), parties (F2), context (F4)

### tender/30#F7 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The consignee (Lumeport Public Works Department) and the Customs Administration of Urvania are public bodies (`IndustryClassificationCode` 8411, "General public administration activities"). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status"; a public body cannot be wound up like a company. A registration scheme typed "Commercial register" does not fit a body that is not a company. A general register may list public bodies, so the register number itself is not questioned.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop `CompanyLiquidationStatusCode` and type the register as what it is for public bodies, or omit the type (preferred); (b) reduce the legal entity to registration name and identifier.
- Needs decision: no
- From: parties (F7), context (F6), broad (F6, customs authority; F8, consignee's liquidation status)

### tender/30#F8 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: Here the second rendering of Valdara's names is tagged `en-XU` and the legal form is given in `qau` and `en-XU`. In the examples issued from Bayvarra the same texts are tagged `en-XB` and the legal form is given once without `languageID`: `03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` (`en-XB`), `03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)` (no tag). The text is identical, so the tag follows the issuer's country, not the text. `en-XB` occurs in 13 examples of the flow, `en-XU` in 9 (`grep -l` over `tender/*.xml`). Whether this is an intended convention could not be settled.
- Condition: The same rendering carries the same `languageID` in every example of the flow, or the rule by which it differs is stated; `CompanyLegalForm` is rendered in the same languages wherever the party is described in full.
- Options: (a) tag the English rendering of an Urvanian name `en-XU` everywhere (preferred: the tag then describes the text); (b) keep the issuer-dependent tag, apply it uniformly and document it.
- Needs decision: yes
- From: parties (F3)

### tender/30#F9 · Low · Exporter's master data that a customs declaration does not use
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty`
- Why: A customs declaration needs the exporter's identity, address and trader number. Share capital, whether shares are fully paid, the stock-exchange listing and the warehouse provider ("A party providing a service to this party") are not customs data; they read as master data copied into the document (section 4.8). (`CorporateStockAmount` is defined as "The number of shares in the capital stock", but holds an amount in XUF; a note for the TC write-up, as in earlier merges.) Counter-arguments of the parts: parties refuted the listing as part of the description of a listed public limited company, and parties and broad refuted the service provider because Castrano despatches the goods being exported. The merge keeps the finding: the declaration names Castrano in no role of its own (not as consignor, not as place of loading), so nothing in it uses the service provider.
- Condition: Share capital, listing and service provider appear only in documents whose purpose uses them.
- Options: (a) remove them here (preferred); (b) keep those for which a use in this document can be stated (e.g. Castrano as the place where the goods can be inspected, then as a location).
- Needs decision: no
- From: context (F7); refutations by parties and broad carried as counter-argument

### tender/30#F10 · Low · Exporter's and consignee's contacts and the consignee's address do not fit their roles
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Department` = `Procurement office`
- Why: The exporter ("The Party who exports the goods …") declares and signs; the contact customs would turn to is the sales order desk, the same contact Valdara carries in tender, catalogue and invoice. The consignee ("The Party who receives the goods") is given with the room and contact of the procurement office, not the depot that receives the benches (26). Section 6: a contact that does not fit the role is Low.
- Condition: The exporter's contact deals with export formalities (or is absent); the consignee's contact and address are those of the receiving place, or the consignee is given without them.
- Options: (a) an export or shipping contact for the exporter, and the depot as the consignee's address and contact (preferred); (b) leave the contacts out.
- Needs decision: no
- From: parties (F4), broad (F8)

### tender/30#F11 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID." The same date is given for 25 unrelated companies in three countries (271 occurrences in 181 files, `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`), among them Trasvia Haulage SRU here; it reads as a filler. (Valdara's date in this document, 1962-04-12, is its own.)
- Condition: Each company's `RegistrationDate` is its own, or the element is absent.
- Options: (a) a date per company from its history (preferred); (b) leave it out; (c) record a 1996 re-registration in the story.
- Needs decision: yes
- From: parties (F5)

### tender/30#F12 · Low · No packages, net weight or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem`
- Why: The goods item gives description, value, gross weight (1660 kg) and quantity (40 EA). Number and kind of packages (ten pallets of four), net weight and the means of transport crossing the border (Trasvia's lorry) are absent; from own knowledge of customs declarations these are standard particulars the exit office matches against what is presented. A missing detail the document could carry.
- Condition: The declaration states the packages and net weight of the goods item and identifies the means of transport at the border.
- Options: `cac:GoodsItem/cac:Package` and `cbc:NetWeightMeasure`, and a shipment stage with the lorry (preferred).
- Needs decision: no
- From: logistics (F5)

### tender/30#F13 · Low · The whole catalogue description of the item in a customs declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[4]`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: Customs needs description, classification, origin, quantity, weight and value. The goods item repeats the catalogue entry of `25-Catalogue.xml` in full: search keywords and brand, the load test method, the seat-height range, manufacturing emissions with method and period, and the circularity profile (resource consumption, packaging waste, repairability, repair manual). None of it is declared to customs; it reads as item master data copied into the document, and the remarks on it (F2, F5) come along with every copy.
- Condition: The item carries the identification and the properties this document uses; the catalogue description stays in the catalogue, which the item can reference.
- Options: (a) reduce the item to identification, name, description, classification and origin (preferred); (b) keep the full copy if the examples are meant to show the item completely everywhere, and record that decision (context's alternative).
- Needs decision: no
- From: context (F8), broad (F8)

### tender/30#F14 · Low · Exit office named by a description, not as a place
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: "The location of the exit office from where the goods will leave or have left the customs territory"; a location's name is "The name of this location". The value describes a kind of office, without identifier or address, although the customs party's border office has an address (Valico di Confine 22). Counter-argument (parties): the examples name customs offices this way throughout (the same text in six examples), the world shows no office code scheme, and if Urvania has a single land-border post the name does identify it. The merge could not settle whether the world has more than one crossing.
- Condition: The exit office is identified by the name of the crossing (and an office identifier where the world has one), or the world records that there is only one land-border post.
- Options: (a) the name of the border crossing on the Ferrano–Lumeport road, with an office ID (preferred); (b) record the single-crossing convention.
- Needs decision: yes
- From: broad (F6), logistics (F4); refuted by parties (carried as counter-argument)

### tender/30#F15 · Low · Party tax exemption reason worded as a transaction
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` the elements are "A reason for the party's exemption from tax". The code `PUBLIC` comes from the transaction exemption list (`…:XB:codelist:TaxExemptionReasonCode`, "Sale to a public body"), and the text begins "Sale to a public body": both describe a kind of sale. Only the second half of the text is the party's status.
- Condition: The party-level exemption reason states the party's status, in code and text.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F6)

### tender/30#F16 · Low · Supporting document with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LPWD-PO-26-0212`
- Why: "A reference to additional documents relevant or related to this customs declaration." The ID resolves to the buyer's order (`26-Order.xml`), but the reference does not say it is an order; customs cannot know the buyer's numbering.
- Condition: The reference states the kind of document.
- Options: add `cbc:DocumentTypeCode` or `cbc:DocumentType` for a purchase order (preferred).
- Needs decision: no
- From: logistics (F6)

### tender/30#F17 · Low · Signature identifier carries the flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-tender`
- Why: "An identifier for this signature." The suffix "tender" is the name of the example flow, not something the exporter's system would know; Valdara's other signature IDs are business-like (`32-Invoice.xml:/Invoice/cac:Signature/cbc:ID` = `VI-SIG-26-0078`).
- Condition: The signature ID is a business identifier in the exporter's style, without the flow name.
- Options: a numbered ID like the invoice's (preferred).
- Needs decision: no
- From: broad (F7), logistics (F7)

## Checked and consistent
- Value arithmetic: 40 × 49900 XUF = 1996000 XUF = 19960.00 XBL × 100 (rate of 26/32); value in ferra, the currency of the exporting country. The installation (a service in Bayvarra) is rightly not part of it (money).
- Shipment CL-SH-26-0216, consignment CL-CS-26-0217, carrier Trasvia Haulage with its haulage permit, quantity 40 EA and gross weight 1660 kg (shipment = goods item) agree with `29-DespatchAdvice.xml`. Shipment and goods-item gross weight are equal; no transport equipment is declared (road carriage), so the shipment figure has nothing to add.
- 1660 kg = 40 × 41.5 kg, the world's gross weight per bench elsewhere (sea/10-PackingList.xml: 3984 kg for 96 benches = 41.5; net 3762 kg = 39.19 per bench). See "Refuted in the merge".
- Issue 2026-03-30 13:40 precedes the despatch advice (17:37), as the note "Declared electronically before the goods leave." says; FunctionCode 9 (original), version 1; validity 90 days.
- `LPWD-PO-26-0212` is the order (26); the invoice (31 March) did not yet exist.
- Classification HS 940179 (chapter 94, section XX), national code 94017910 of the Urvanian tariff; origin XU; cargo type general cargo; ExportTypeCode PERMANENT and ExportReasonCode SALE fit a sale.
- Parties: exporter = consignor Valdara (signs; prefix VI), consignee the department, customs party the Customs Administration of Urvania, territory XU. Identifiers of Valdara, Castrano, Trasvia, Codana, the department and the customs administration are the same in every example of the flow that carries them; CompanyID = PartyIdentification; ElectronicAddressID = country prefix + number; RegistrationName agrees between tax scheme and legal entity; tax schemes fit the countries (parties, by script). Declaration ID VI-CD-26-0219 is the one the import declaration cites (logistics).
- `check_ids.py`: ISIN XU0001042501 correct; no other failures (re-run in the merge).
- Counts re-done in the merge over `*.xml`: LocaleCode 362/213, Region "Province of" 219/104, RegistrationDate 1996-01-01 271, factor 0.82 in 39 files, en-XB in 13 and en-XU in 9 tender examples.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 90 days for an export of the same day — refuted, a validity of the declaration for exit is a customs rule of the world, not a transport time (from broad, logistics, context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox`: post box and street in one address — refuted, the address type is POSTAL and both can be printed (from broad).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[1]/cbc:CargoTypeCode`: general cargo next to the HS code — refuted, palletised benches are general cargo (from broad).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted by broad and parties (the warehouse that despatches is relevant to an export). The merge disagrees and keeps it in F9 with this counter-argument.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`, with `CorporateStockAmount` and `FullyPaidSharesIndicator`: master data — refuted by parties (part of the description of a listed company; check digit correct; XU is no ISIN prefix). The merge disagrees on the master-data point and keeps it in F9; the check digit and the fictional prefix are confirmed.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: too vague — refuted by parties (world convention). The merge could not settle it: F14, Low, needs decision.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:TimezoneOffset` (all four `-1`): malformed offset — refuted, the element is text "as an offset from Universal Coordinated Time" and every address uses the same form (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: real country code — refuted, +999 is not assigned in ITU-T E.164 (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: real ISO 6523 ICD — refuted, 0990 is not an allocated ICD to the parties' knowledge (from parties).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`: VAT number of a customs authority — refuted, a public body can be registered for VAT (from parties).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: haulier's licence in a customs declaration — refuted, customs has an interest in the authorisation of the carrier that crosses the border (from context).
- `/ExportCustomsDeclaration/cac:Signature`: signed although "electronically" — refuted, an electronic declaration is signed electronically (from context).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID`: the order instead of the commercial invoice — refuted, the invoice is issued only on 31 March (from logistics).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: under DAP an export value at the border could be lower than the invoice price — refuted, no document of the flow separates a freight amount from the price (from money).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: amount without decimals — refuted, the ferra is used without decimals throughout the flow (from money).

## Refuted in the merge
### broad/F1 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `40`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- The part's finding: one bench takes 34 kg steel and 22.5 kg hardwood, 56.5 kg; 40 benches are 2260 kg net before anchors, packaging and about ten pallets, but the gross weight is 1660 kg (41.5 kg a bench), below the net weight, in 29, 30 and 31 alike. Condition: gross weight ≥ 40 × bench weight plus packaging and pallets, consistent in 29–31 and with the material figures. Options: about 2600 kg (preferred) or lower material figures. Needs decision: no.
- Refuted because: `ResourceConsumption` is "A record of a resource consumed, such as energy, water, or materials" under the circularity profile, i.e. what manufacturing a bench consumes, not what the bench contains; consumption includes offcuts and machining losses and is always at least the product's mass. The world gives the bench's weight elsewhere: `sea/10-PackingList.xml:/PackingList/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `3984` for 96 benches (41.5 kg each) and a net weight of 3762 kg (39.19 kg each). 40 × 41.5 = 1660 exactly, so the figure is consistent with the world; 56.5 kg consumed for a 39.2 kg bench is a material yield of 69 %, plausible for a welded steel frame with sawn hardwood slats (own knowledge). Whether 1660 − 40 × 39.19 = 92 kg is enough for ten pallets and their wrapping (about 9 kg a pallet) is a cross-flow plausibility question (see "Outside this review").

## Changed in the merge
- broad/F2 + logistics/F1 + context/F1 → F1: combined; the attribute code `DescriptionCode` (context) added as an XPath line; options of the parts kept, (a) preferred.
- broad/F3 (Medium) + logistics/F2 (High) → F2: High, because factor × base = value is arithmetic within the aggregate (section 6 High), as in every earlier merge (analysis/review-merge-decisions.md).
- broad/F4 split into F3 (Region) and F6 (LocaleCode), each combined with the parties and context findings.
- broad/F5 (Low, yes) + money/F1 (Medium, no) + logistics/F3 (Medium, no) + context/F5 (Low, yes) → F4: Medium, no. The contradiction with the exporter's own invoice (exemption on 20160.00) makes it more than a valuation question; the fix is the value, not the story. Differs from the wood merges' "packing charge: Medium, yes" because a charge for the goods' own colour is part of the price of the goods under any valuation basis.
- context/F2 (Medium, yes) → F5: Needs decision no, aligned with analysis/review-merge-decisions.md (CRADLETOGATE: Medium, no).
- parties/F7 (Low) + context/F6 (Low) + broad/F6 (customs part) + broad/F8 (consignee's liquidation status) → F7: raised to Medium, aligned with analysis/review-merge-decisions.md ("Public bodies … as companies: Medium, no"): the register type and status carry a meaning that does not fit the party.
- broad/F6 split: the exit-office part → F14 (with logistics/F4), the customs-authority part → F7.
- broad/F8 split: catalogue data → F13 (with context/F8); exporter's contact and consignee address → F10 (with parties/F4); consignee's liquidation status → F7.
- context/F8 (Low, yes) → F13: Needs decision no, aligned with analysis/review-merge-decisions.md (catalogue data copied: Low, no); context's option (b) kept.
- parties/F5 (Low, no) → F11: Needs decision yes, aligned with analysis/review-merge-decisions.md (RegistrationDate 1996-01-01: Low, yes).
- logistics/F4 (Low, no) → F14: Needs decision yes, because parties refuted it and the merge could not settle it; parties' argument added.
- context/F7 → F9: the parties' and broad's refutations of the listing and the service provider added as counter-arguments; CorporateStockAmount's definition noted.
- parties/F6 → F15: preferred option changed to keeping the code and rewording the text, because the code's list definition names a buyer that is a public body; aligned with the other tender merges.

## Outside this review
- Which border post lies on the road from Ferrano to Lumeport, and whether there is more than one, is a map question (broad).
- Pallet tare: 1660 kg gross against 40 × 39.19 kg net (bench weight from the sea flow) leaves about 9 kg per pallet including film and straps, light for a pallet carrying 1.8 m benches; a cross-flow plausibility question for 29 and the consistency review.
