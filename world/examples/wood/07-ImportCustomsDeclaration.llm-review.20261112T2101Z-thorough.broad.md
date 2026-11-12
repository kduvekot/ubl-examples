# LLM review: 07-ImportCustomsDeclaration.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/07-ImportCustomsDeclaration.xml`, Git blob `45419bf3fd0c23bb1b64bfa1ca0140c26025be7e` (committed)
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

### wood/07#F1 · Medium · Customs value excludes the packing charge and states no conversion
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000`
- XPath: `05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `34560.00`
- XPath: `08-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `34800.00`
- Why: DeclaredCustomsValueAmount is "The total declared value for customs purposes of the goods item". The value 3 456 000 XUF is the slats' price 34 560.00 XBL at 100 XUF per XBL; it leaves out the 240.00 XBL billed for the heat-treated pallets, although the cost of packing belongs to the customs value of imported goods under the WTO Customs Valuation Agreement, Art. 8.1(a)(iii) (own knowledge). Nor does any document of the flow state the exchange rate used.
- Condition: The customs value includes the packing charge (34 800.00 XBL converted), and the rate used for the conversion is stated or derivable from the examples.
- Options: (a, preferred) Declare 3 480 000 XUF (if the rate is 100) and state the rate (e.g. in a note or via the invoice's exchange rate); (b) if the world's valuation rules exclude packing, state that.
- Needs decision: yes

### wood/07#F2 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Customs Administration of Urvania`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105507`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The customs authority is a public body (its industry code is 8411, general public administration), but its PartyLegalEntity places it in the commercial register (CorporateRegistrationTypeCode `COMMERCIAL`) and gives it a liquidation status. CompanyLiquidationStatusCode is "A code signifying the party's liquidation status", which a state authority does not have, and a commercial-register entry asserts something about the authority that is not true of a public body.
- Condition: The authority carries no liquidation status and no commercial-register scheme; if it has an identifier in a public-sector register, that register is named as such.
- Options: (a, preferred) Drop CompanyLiquidationStatusCode and CorporateRegistrationScheme (or use a public-body registration type, if the world's list has one); (b) leave PartyLegalEntity out for the authority.
- Needs decision: no

### wood/07#F3 · Medium · Urvanian province carried in Region
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address/Region is defined as "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division, which UBL puts in CountrySubentity ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses in the same flow do use CountrySubentity and CountrySubentityCode for their states, so the two countries are encoded differently. The same value occurs 219 times in 104 XML files (`grep -r --include='*.xml' -c '<cbc:Region>Province of Ferrano'`).
- Condition: No Urvanian address carries an administrative division in Region; the province, where given, is in CountrySubentity (with CountrySubentityCode if the world has a list for it).
- Options: (a, preferred) Move the province to CountrySubentity, as for Bayvarra, because that is the element UBL defines for it; (b) if Ferrano is in the world a non-administrative region, keep Region but name it as such, without "Province of".
- Needs decision: no

### wood/07#F4 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". The value `en` with listID ISO 639 is a language code and only repeats Language/ID (`en`); it names no locale (the examples' own languageID attributes, e.g. `en-XB`, show what a locale looks like). The same element and value occur 362 times over the examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<'`).
- Condition: Every LocaleCode present holds a locale (language and region, e.g. the party's country variant) with a listID naming a list of locales, or LocaleCode is absent.
- Options: (a, preferred) Use the locale that matches the party (e.g. en-XB) from a list that defines locales, which also matches the languageID convention of the examples; (b) leave LocaleCode out where nothing needs a locale.
- Needs decision: no

### wood/07#F5 · Low · Signature ID contains the example flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-IM-wood`
- Why: The signature identifier ends in "wood", the name of the example flow, not a number the importer would assign (the RFQ's signature is `VI-SIG-26-RFQ`). The pattern occurs in 14 XML files (`grep -rlE --include='*.xml' 'SIG-[A-Z]+-[a-z]+<'`).
- Condition: The signature ID is an identifier the signatory would assign, without the flow name.
- Options: (a, preferred) Use the importer's numbering (e.g. VI-SIG-26-0634).
- Needs decision: no

### wood/07#F6 · Low · Notifier is the importer and consignee again
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`
- Why: NotifierParty is "The Party who is responsible for contact on master level". It is Valdara, already importer, consignee and signatory; a separate role that repeats the same party adds nothing the declaration uses, unless the story gives a reason.
- Condition: NotifierParty is absent, or a different party the declaration needs.
- Options: (a, preferred) Leave NotifierParty out; (b) use a customs broker or forwarder if one acts for Valdara (which would change the story).
- Needs decision: no

### wood/07#F7 · Low · Import declaration does not reference the invoice its value rests on
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `MS-CD-26-0631`
- XPath: `08-Invoice.xml:/Invoice/cbc:ID` = `MS-INV-26-0635`
- Why: The declaration references the export declaration but no commercial document; the customs value is the transaction value of invoice MS-INV-26-0635, which exists at the time (issued 2026-02-26) and would let customs verify the value.
- Condition: The import declaration references the commercial invoice (AdditionalDocumentReference).
- Options: (a, preferred) Add an AdditionalDocumentReference to MS-INV-26-0635 with its type.
- Needs decision: no

### wood/07#F8 · Low · Contacts do not fit the parties' roles in this document
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The importer's contact for its customs declaration is its order desk in Sales, not someone handling import formalities; the customs border office is reachable only on weekdays 08:00–17:00, although goods arrive at the border.
- Condition: The importer's contact is the one handling the import, and the border office's hours cover the time goods pass.
- Options: (a, preferred) Give each party the contact that handles this document for it (purchasing, goods-in, accounts, despatch); (b) if the parties have only one contact, give it a neutral name and function.
- Needs decision: no

### wood/07#F9 · Low · Valdara's master data the document does nothing with
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Valdara's SecurityListing (listed shares) and its ServiceProviderParty (Castrano Logistics, "Warehousing and despatch") are carried in full in this import declaration, which does nothing with either: no security is traded, and Castrano plays no role (the goods go to Valdara's own goods-in in Ferrano). This is party master data copied into a document that does not use it (section 4.8).
- Condition: The party carries in this document only data the document uses, or the example gives the reason for the security listing and the service provider.
- Options: (a, preferred) Leave SecurityListing and ServiceProviderParty out of this document; (b) give Castrano a role the document uses (e.g. as the receiving warehouse), which would change the story.
- Needs decision: no

### wood/07#F10 · Low · Usability period of 12 months on the 'Surface' property
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cbc:Value` = `Planed on four sides`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:AdditionalItemProperty[3]/cac:UsabilityPeriod/cbc:DurationMeasure` = `12`
- Why: ItemProperty/UsabilityPeriod is "The period during which this item property is valid". A planed surface does not cease to be planed after 12 months; nothing in the example says what the period stands for (a storage or warranty period would be a property of its own).
- Condition: The UsabilityPeriod is absent, or it sits on a property whose validity really expires, and the example makes clear what it means.
- Options: (a, preferred) Remove the UsabilityPeriod from 'Surface'; (b) move it to a property that expires (e.g. a moisture guarantee while stored as agreed).
- Needs decision: no

### wood/07#F11 · Low · Length repeated in SellersItemIdentification/MeasurementDimension
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:SellersItemIdentification/cac:MeasurementDimension/cbc:Measure` = `1800`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- Why: The length 1800 mm is given both as a measurable dimension of the seller's item identification and as Item/Dimension[1]. The identification carries no other variant dimension (width and thickness are only in Item/Dimension), so the repetition has no business reason of its own (IND5/IND6).
- Condition: The length appears once, or the MeasurementDimension under the identification is needed to distinguish item variants and the example says so.
- Options: (a, preferred) Keep the length in Item/Dimension only; (b) keep it in the identification if the seller's item number is length-specific and that is stated.
- Needs decision: no

### wood/07#F12 · Low · English (en-X?) renderings of Urvanian names are Italian
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: The second rendering of the Urvanian street name (and, where present, of the legal form) is tagged as English (`en-XU`/`en-XB`) but is Italian ("Via …", "Piazza …", "Società urvaniana per azioni"). The world's languages are English, Urvanian and Lisavan, so a reader cannot tell which language this text is meant to be, and the languageID does not describe it. 217 English-tagged street names in 102 XML files start with Via/Viale/Piazza/Corso/Strada/Valico/Banchina (`grep -rhoE --include='*.xml'`).
- Condition: Every text tagged with an English languageID is English, or the world states that these Italian forms are the official English-language names in Urvania.
- Options: (a) Give the English rendering in English (e.g. "Workshops Street"); (b) if the Italian forms are the world's exonyms, record that in the world's story so the tag is explained. Preference: (b) if it is intended, as the pattern is consistent; otherwise (a).
- Needs decision: yes

### wood/07#F13 · Low · RegistrationDate 1996-01-01 looks like a default
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: PartyLegalEntity/RegistrationDate is "The registration date of the CompanyID". `1996-01-01` occurs 271 times in 181 XML files (`grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'`), for companies of different sizes and in different countries' registers (Bayvarra's federal register and Urvania's commercial register), while the other dates are specific (e.g. 1962-04-12 for Valdara). A New Year's Day date shared by unrelated companies in two registers reads as a filler unless the world has a reason (e.g. a re-registration on that day).
- Condition: Each RegistrationDate is the party's own date from the world, or the world states why the date is shared.
- Options: (a) Give each party its own registration date; (b) state in the world's story that the registers were re-founded on 1996-01-01. Preference: (a), unless (b) is already the story.
- Needs decision: yes

## Checked and consistent
- Shipment `MS-SH-26-0632`, gross weight 21600 kg, 4800 EA and HS 440799 agree with 05-ExportCustomsDeclaration.xml; PreviousCustomsDeclaration resolves to the export declaration's CustomsDeclaration ID.
- Roles: importer and consignee Valdara, consignor Marrowdale; NatureOfTransactionCode PURCHASE and SubTypeCode FREECIRC fit a purchase for use in Ferrano.
- Dates: declared 2026-02-27 11:05, the day after the transport started (2026-02-26); validity 30 days.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` (the Bayvarran exit office) in an import declaration — refuted: the UBL 2.5 ImportCustomsDeclaration has only this office element, defined as the "Customs exit office of the goods being declared", which is the Bayvarran post.
- `/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.` with no duty amounts — refuted as a finding: the UBL 2.5 ImportCustomsDeclaration has no element for duty or tax amounts, so the note is the only place.
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` pointing to another country's export declaration — refuted: under the Trade Accord the export declaration is a plausible preceding declaration, and the ID resolves.
