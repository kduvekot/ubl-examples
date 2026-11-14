# LLM review: 31-ImportCustomsDeclaration.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/31-ImportCustomsDeclaration.xml`, Git blob `f995e80c478f86074b7bfa4eca588151c5ee7767` (committed)
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

### tender/31#F1 · High · The declared goods are the grey variant; the shipment is moss green
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The importer itself changed the release to moss green (`27-OrderChange.xml:/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`), the seller accepted (`28-OrderResponse.xml:/OrderResponse/cbc:Note[2]` = `Accepted: moss green, at the quoted charge.`), and shipment CL-SH-26-0216 was despatched so (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`). The importer's own declaration describes grey benches: extended identifier, colour attribute and colour property. Same problem in 30 (F1).
- Condition: The item's variant and colour data describe the goods of the shipment (moss green), or the declaration carries no colour data.
- Options: (a) the green variant's identification and colour, in every document from the despatch on (preferred by broad and context, and by the merge, as in 30); (b) reduce the item to what customs needs (preferred by logistics).
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### tender/31#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × 1 EA = 0.82, not 96 kg; 96 / 0.82 = 117.07 of an unstated activity. 39 files carry factor 0.82 (`grep -l 'ValueFactorNumeric>0.82<' world/examples/*/*.xml`).
- Condition: factor × base = value, or factor and base are absent.
- Options: (a) drop factor and base (preferred); (b) a real factor and its activity.
- Needs decision: no
- From: broad (F4), logistics (F2)

### tender/31#F3 · Medium · A language code as locale
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used". The value (listID `ISO 639`) repeats the language code of the sibling `cbc:ID`. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale (`en-XB`) from a locale list (broad).
- Needs decision: no
- From: broad (F5), parties (F1), context (F4)

### tender/31#F4 · Medium · Public bodies described as companies in a commercial register, with a liquidation status
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The importing department and the Customs and Border Service of Bayvarra are public bodies (`IndustryClassificationCode` 8411). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status"; a public body is not wound up like a company, and a register typed "Commercial register" does not fit a body that is not a company. The register number itself is not questioned.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) drop the status and type the register neutrally, or omit the type (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F4), context (F7), broad (F9)

### tender/31#F5 · Medium · A province in `Region`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity` ("… such as the name of its county, province, or state"), where the Bayvarran addresses of the same document put their state. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`; `Region` is absent or holds a region in the sense of the definition.
- Options: move it to `CountrySubentity` (preferred); or record that Urvania's format has a postal region only (parties' alternative).
- Needs decision: no
- From: broad (F5), parties (F2), context (F3)

### tender/31#F6 · Medium · The customs value leaves out the colour charge that is part of the price of the imported goods
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- Why: "The total declared value for customs purposes of the goods item." 19960.00 XBL = 40 × 499.00, the price of the standard bench. The importer itself agreed the special-colour charge (`27-OrderChange.xml:/OrderChange/cac:AllowanceCharge/cbc:Amount` = `200.00`; `27-OrderChange.xml:/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`), and the invoice issued at 09:28 that day, before this declaration at 11:14, bills it as part of the goods (`32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `20160.00`). By the usual transaction-value rule (own knowledge: WTO Valuation Agreement) a charge for the goods' colour belongs to their value; the declaration on which any duty is assessed is 200.00 XBL short. The valuation basis (whether carriage to the border is included, as under CIF, or the DAP price to Lumeport) is not stated either, which broad noted; that question is the analysis file's open "customs value basis" decision and is not settled here. Same value in 30 (F4).
- Condition: The declared customs value equals the invoice's price for the goods (20160.00 XBL), or a stated valuation rule explains the difference.
- Options: (a) declare 20160.00 (preferred by money, logistics, context); (b) bill the colour separately from the goods in the invoice and keep 19960.00; (c) state the valuation basis.
- Needs decision: no
- From: money (F1), logistics (F4), context (F5), broad (F6)

### tender/31#F7 · Medium · Goods imported into Bayvarra are classified with the Urvanian tariff
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: The national subdivision carries the list `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, the tariff of the exporting country. The declaration is for release for free circulation in Bayvarra, lodged with the Bayvarran customs service, which classifies by its own tariff (or a common Trade Accord tariff, if one exists). National subdivisions beyond the six HS digits (940179, also given) differ by country (own knowledge). All 39 occurrences of the code use the XU list; no XB tariff list occurs in the examples (grep for `CustomsTariffCode">94017910` over `*.xml`).
- Condition: A national tariff code in the import declaration comes from the tariff of the importing territory (or a common Accord tariff named as such), or only the HS code is given.
- Options: (a) a Bayvarran tariff code with its own list (preferred by broad); (b) drop the national code and keep HS 940179; (c) if the Accord has a common tariff, name the list so in both declarations.
- Needs decision: yes (whether the Trade Accord countries share a tariff)
- From: broad (F3), logistics (F3)

### tender/31#F8 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty. …" The value is a footprint system boundary for a bench.
- Condition: The element holds a fullness of transport equipment or is absent.
- Options: (a) remove it, keep the boundary in the lifecycle stage description (preferred); (b) in addition, record the missing boundary element for the TC write-up.
- Needs decision: no
- From: context (F2)

### tender/31#F9 · Low · Party tax exemption reason worded as a transaction
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` these are "A reason for the party's exemption from tax". Code and text ("Sale to a public body", from the transaction exemption list) describe a sale; only the second half of the text is the party's status.
- Condition: The party-level exemption reason states the party's status, in code and text.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F3); money considered and left it to the party review

### tender/31#F10 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- Why: Here (issued in Bayvarra) Valdara's English renderings are tagged `en-XB` and the legal form appears once, untagged and without the Urvanian text. In the Urvanian-issued examples the same texts are tagged `en-XU` and the legal form is in `qau` and `en-XU`: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`, `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`. The tag follows the issuer, not the text; `en-XB` occurs in 13 tender examples, `en-XU` in 9. Whether this is an intended convention could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated; the legal form is rendered in the same languages wherever the party is described in full.
- Options: (a) `en-XU` for the English rendering of Urvanian names everywhere (preferred); (b) the issuer-dependent tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F5)

### tender/31#F11 · Low · Consignor's master data, service provider and sales contact in an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- Why: The import declaration needs the consignor's identity and address. Share capital, listing, the warehouse provider ("A party providing a service to this party", with a `SellerContact` that has a name and no means of contact) and the sales order desk are not customs data of the importing country; the block is in all 22 full descriptions of Valdara in the flow (parties, by script). Counter-argument (parties): the listing describes the legal entity of a listed company. The merge keeps it: the document uses none of it (section 4.8).
- Condition: The consignor carries only what the declaration uses; a service provider, where it appears, has a usable contact.
- Options: (a) leave these out here (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: context (F8), parties (F6), broad (F9)

### tender/31#F12 · Low · Importer repeated as notifier, without a contact
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `NotifierParty` is "The Party who is responsible for contact on master level". It is the department again, already importer (with contact) and consignee, here with an ID and a name only; a role defined by being the contact adds nothing without a contact (no fillers). Counter-argument (broad): the definition fits the declarant. The merge keeps the finding: nothing is said that the importer does not already say.
- Condition: A notifier is named only if another party or contact is responsible for contact about the declaration, or it carries that contact.
- Options: (a) remove `NotifierParty` (preferred); (b) give it the unit customs should contact.
- Needs decision: no
- From: parties (F7), context (F6); refuted by broad (carried as counter-argument)

### tender/31#F13 · Low · "Duties paid" without a duty, rate or amount
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- Why: The note states a payment, but the declaration gives no duty, rate or tariff treatment, no other example of the flow shows a duty on this import, the importer is exempt from the state sales tax (F9) and the goods originate in a Trade Accord partner. The same sentence is in six import declarations of different flows (`grep -l "Duties paid by the importer"` over `world/examples/*/*.xml`), so it is not specific to this import. Counter-argument (context): the declaration has no place for assessed duties and the note only says how duties are settled; broad and context found it consistent with DAP. Whether any duty is due under the Trade Accord is a world rule the merge cannot settle.
- Condition: A statement about duties agrees with what is due on this import: the duty is stated, or the note says none is due and why, or it describes the settlement without asserting a payment.
- Options: (a) reword to what applies (e.g. no duty under the Trade Accord) (preferred by money); (b) "Any duties are settled through the importer's deferment account at customs."
- Needs decision: yes
- From: money (F2); refuted by context (carried as counter-argument)

### tender/31#F14 · Low · No office of entry, no commercial invoice, no packages
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Customs and Border Service of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0219`
- XPath: `/ImportCustomsDeclaration/cbc:NatureOfTransactionCode` = `PURCHASE`
- Why: The declaration is for a purchase, but its only reference is the export declaration: the commercial invoice VI-INV-26-0221 (issued 09:28, before this declaration at 11:14), on which value and origin rest, is not referenced, nor the order. The Bayvarran office where the goods enter is not given (the customs party is the service as a whole), nor the vehicle presenting the goods, packages or net weight. Missing details the document could carry.
- Condition: The declaration references the commercial invoice and identifies the office of entry; packages are stated.
- Options: an `AdditionalDocumentReference` to the invoice, the entry office as a location or note, and packages (preferred).
- Needs decision: no
- From: broad (F6), logistics (F5)

### tender/31#F15 · Low · Exit office named by a description, not as a place
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: "Customs exit office of the goods being declared." The name describes a kind of office without code or place name. As in 30 (F14), the parties part there refuted it as a world convention (the same text in six examples), and if Urvania has a single land-border post the name does identify it; the merge could not settle that. That the office is Urvanian is right (the element is the exit office; parties, logistics and context refuted the "wrong office" suspicion).
- Condition: The exit office is identified by the name of the crossing (and an ID where the world has one), or the single-crossing convention is recorded; the same as in 30.
- Options: (a) name and ID of the border post, as in 30 (preferred); (b) record the convention.
- Needs decision: yes
- From: broad (F7), logistics (F5)

### tender/31#F16 · Low · The whole catalogue description of the item in a customs declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[4]`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: Customs needs description, classification, origin, quantity, weight and value; the goods item repeats the full catalogue entry of `25-Catalogue.xml` (keywords, brand, load test, seat-height range, manufacturing emissions, circularity profile). Item master data copied into the document; F2 and F8 come along with it.
- Condition: The item carries the identification and the properties this document uses.
- Options: (a) reduce the item (preferred); (b) keep the full copy everywhere and record that decision (context's alternative).
- Needs decision: no
- From: context (F9), broad (F9)

### tender/31#F17 · Low · Signature identifier carries the flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LPWD-SIG-IM-tender`
- Why: "An identifier for this signature." "tender" is the name of the example flow, and the prefix LPWD differs from the department's other signature IDs, which all start PWD-SIG- (PWD-SIG-CAN, PWD-SIG-OC, PWD-SIG-CONTRACT and eleven more in the flow, 14 in all).
- Condition: The signature ID is in the department's style, without the flow name.
- Options: e.g. PWD-SIG-IM (preferred).
- Needs decision: no
- From: broad (F8), logistics (F6)

## Checked and consistent
- `PreviousCustomsDeclaration` VI-CD-26-0219 is the customs declaration inside 30; shipment CL-SH-26-0216, 40 EA and 1660 kg (shipment = goods item; no transport equipment declared) agree with 29 and 30.
- 19960.00 XBL = 1996000 XUF of 30 at 100 XUF per XBL; value in lume, the importing country's currency; the installation is rightly not part of it (money).
- Issue 31 March 11:14 follows the export declaration (30 March 13:40), the despatch (17:37) and the invoice (31 March 09:28); validity 30 days.
- Importer = consignee: the department, which buys DAP and clears the import; customs trader number XB-TR-410548. Consignor Valdara. TypeCode IMPORT, SubTypeCode FREECIRC, NatureOfTransactionCode PURCHASE fit a purchase released for free circulation; jurisdiction XB; HS 940179 in section XX; origin XU.
- Customs party: the Bayvarran service at Border Crossing Road 36, Marrowdale, Upland State, contact "Border office".
- Party identifiers and the identity checks of 30 hold for this document too (parties, by script). `check_ids.py`: ISIN XU0001042501 correct (re-run in the merge).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID`: an export declaration of another party to another authority as "previously sent" — refuted, it is the preceding declaration of the same movement and the ID resolves (from broad, logistics).
- `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name`: the importer as its own notifier — refuted by broad (the definition fits the declarant). The merge disagrees, with parties and context: F12.
- `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure`: 30 days here, 90 in 30 — refuted, two authorities with their own rules (from broad, context).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Procurement office`: unsuitable as the importer's customs contact — refuted, the procurement office bought the goods, holds the papers and lodges the declaration; the receiving place is not this document's concern (from broad, parties).
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: the wrong (Urvanian) office in a Bayvarran import declaration — refuted, the element is "Customs exit office of the goods being declared" (from parties, logistics, context). Its content is F15.
- `/ImportCustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name`: consignee redundant with importer — refuted, distinct roles, no condition (from parties).
- `/ImportCustomsDeclaration/cbc:Note`: duties without an amount — refuted by context (the note says how duties are settled). The merge could not settle it, with money: F13.
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode`: worded as a sale — left by money to the party review; it is F9 (from money).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:TimezoneOffset` (`-1`): malformed — refuted, text offset used throughout (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Telephone` = `+999 2 38 2648 0548`: real country code — refuted, +999 is not assigned (from parties).
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties as part of the legal entity; the merge keeps it in F11; check digit and fictional prefix confirmed.
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: real ICD — refuted, 0990 not allocated to the parties' knowledge (from parties).

## Refuted in the merge
### broad/F1 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `1660`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `40`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- The part's finding: one bench contains 34 kg steel and 22.5 kg hardwood; 40 benches are 2260 kg net, but the gross weight is 1660 kg (41.5 a bench), in 29, 30 and 31. Condition: gross ≥ 40 × bench weight plus packaging and pallets, consistent with the material figures. Options: about 2600 kg, or lower material figures. Needs decision: no.
- Refuted because: as in 30, `ResourceConsumption` is "A record of a resource consumed", what manufacturing a bench consumes (offcuts included), not its content. The world's bench weighs 41.5 kg gross and 39.19 kg net (`sea/10-PackingList.xml:/PackingList/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `3984` for 96 benches), and 40 × 41.5 = 1660 exactly; a material yield of 69 % is plausible (own knowledge).

## Changed in the merge
- broad/F2 + logistics/F1 + context/F1 → F1: combined; `DescriptionCode` added; (a) the green variant preferred, as in 30.
- broad/F4 (Medium) + logistics/F2 (High) → F2: High, as in 30 and analysis/review-merge-decisions.md.
- broad/F5 split into F3 (LocaleCode) and F5 (Region), combined with parties and context.
- parties/F4 (Low) + context/F7 (Low) + broad/F9 (public-body part) → F4: raised to Medium, aligned with analysis/review-merge-decisions.md.
- money/F1 (Medium, no) + logistics/F4 (Medium, no) + context/F5 (Low, yes) + broad/F6 (value part; Low, yes) → F6: Medium, no, as 30/F4; broad's note on the DAP valuation basis kept in Why.
- broad/F6's missing invoice reference and logistics/F5's missing entry office and packages → F14; logistics/F5's exit-office part with broad/F7 → F15 (Low, needs decision yes, as 30/F14; broad and logistics had no).
- context/F2 (Medium, yes) → F8: Needs decision no, as analysis.
- context/F8 + parties/F6 + broad/F9 (service provider and order desk) → F11.
- context/F9 (Low, yes) + broad/F9 (catalogue part) → F16: Needs decision no, as analysis.
- broad/F8 + logistics/F6 → F17: the count of PWD-SIG- IDs added (re-counted in the merge: 14 in the flow).
- money/F2 → F13: context's refutation added as counter-argument.
- parties/F3 → F9: preferred option changed to keeping the code and rewording the text, because the code's list definition names a buyer that is a public body; aligned with the other tender merges.

## Outside this review
- Bayforth Forwarding, freight forwarder in 27 and tax representative from 32 on, has no role in this declaration; a matter for the reviews of 27 and 32 (parties).
- Whether duties are due at all between Urvania and Bayvarra under the Trade Accord is a world rule (context).
- Pallet tare (about 9 kg per pallet if the bench weighs 39.19 kg net): cross-flow plausibility, as in 30.
