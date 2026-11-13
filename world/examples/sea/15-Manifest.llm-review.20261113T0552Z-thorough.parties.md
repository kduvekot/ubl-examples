# LLM review: 15-Manifest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/15-Manifest.xml`, Git blob `4caf72d7f9decfbb65355d2cdfb4c4e93fc08906` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/15#F1 · Medium · A language code in LocaleCode
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Manifest/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/15#F2 · Medium · The Island Customs Service described as a company in a commercial register, with a liquidation status
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- Why: The Island Customs Service is the customs authority of Lisavu (ISIC `8411`, general public administration). Its legal entity places it in a register of companies with `CorporateRegistrationTypeCode` = commercial register and gives it `CompanyLiquidationStatusCode` (UBL: "A code signifying the party’s legal status", here "Active, not in liquidation"). A public body is not entered in the commercial register and cannot go into liquidation; the checklist names exactly this case. The same kind of description is used for the Customs and Border Service of Bayvarra in 11-ExportCustomsDeclaration.xml.
- Condition: The legal entity of The Island Customs Service describes it as the public body it is: no commercial-register scheme, no liquidation status (an official register of public bodies, or only the registration name, if anything).
- Options: Preferred: keep `RegistrationName` and drop `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme`; if the world has a register of public bodies, use it with a registration type that says so. Alternative: drop `PartyLegalEntity` altogether for public bodies.
- Needs decision: no

### sea/15#F3 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/Manifest/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but an access point of the business park for vehicles, and a postal address (where the post reaches Lumeway Distribution) has no use for it. The same value occurs 79 times in 76 examples of the world (25 times in this flow, counted with `grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: The postal address of Lumeway Distribution holds no gate in `AdditionalStreetName` (or in any other street element); a gate, where a document needs it for vehicles, is given in a location or delivery element of that document.
- Options: Preferred: drop `Gate 3` from the postal address; documents where a truck must find the gate (pickup, despatch) can carry it in their delivery or despatch location (e.g. a `SubsidiaryLocation` or `Location/Description`).
- Needs decision: no

### sea/15#F4 · Low · Velumi Trading and the Island Customs Service described differently from the examples issued in Lisavu (English renderings tagged en-XB, legal form only in English)
- XPath: `/Manifest/cac:AuthorityParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/Manifest/cac:AuthorityParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: In this example (issued by Tidewell Ocean Lines) the English renderings of the Island Customs Service’s and Velumi Trading’s street and town in Selanu carry `languageID="en-XB"` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi Trading issued itself Velumi Trading has `languageID="en-XL"` on the English renderings and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: the examples issued by Bayvarran parties (01–04, 06, 09–12, 14, 15, 20, 22, 23, 25, 26) use the first form, those issued by Lisavan parties (05, 17, 19, 21, 24, 27–29) the second. The street and town names and the legal form belong to the party and its place in Lisavu; which variety of English the issuer writes does not change them, and the Lisavan legal form is part of the party’s description wherever it is given. The checklist asks that the same address of the same party be described the same way in every example. The Island Customs Service has the en-XL form in the import declaration: `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`.
- Condition: Velumi Trading and the Island Customs Service carry the same address renderings, `languageID` values and legal-form renderings in every example of the flow.
- Options: Preferred: describe it everywhere as in 05-Order.xml (Lisavan and en-XL renderings, legal form in both languages), because those are the names used in Lisavu. Alternative: if the world’s rule is that a rendering is tagged with the issuer’s variety of English, record that rule and still give the Lisavan legal form in every example.
- Needs decision: yes

### sea/15#F5 · Low · The authority’s contact is reachable on weekdays only, the ship arrives on a Sunday night
- XPath: `/Manifest/cac:AuthorityParty/cac:Contact/cbc:Name` = `Import office`
- XPath: `/Manifest/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-05-17`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`
- Why: The manifest is lodged with the Island Customs Service for the arrival at Selanu, estimated for 2026-05-17 at 22:00, which is a Sunday. The authority’s only contact is its import office with the note "Weekdays 08:00–17:00" (UBL: `Contact/Note` describes "the circumstances under which this contact can be used"). The checklist asks that an authority’s contact be reachable when ships or goods arrive; nobody can be reached for this arrival.
- Condition: The contact given for the receiving authority is one that can be used at the estimated arrival time, or the note no longer restricts it to weekday office hours.
- Options: Preferred: give the customs service’s port or duty office at Selanu with round-the-clock or arrival-time availability. Alternative: keep the import office but drop the restricting note, if it is reachable outside office hours.
- Needs decision: no

### sea/15#F6 · Low · Crew list incomplete against the crew count and against the ship’s report
- XPath: `/Manifest/cac:CrewPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/Manifest/cac:CrewPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- XPath: `/Manifest/cbc:ManifestTypeCode` = `CARGO`
- Why: `CrewPerson` is "A person registred as crew in this manifest". The manifest lists two crew members (master and chief officer) and states 14 crew on board; the ship’s report for the same voyage lists a third, the chief engineer (`16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:FamilyName` = `Dunmore`), who is missing here. A crew list in a manifest is either the complete list or none; a cargo manifest (`CARGO`) normally carries none.
- Condition: The persons in the manifest are either the complete crew and passenger list of the voyage (consistent with `CrewQuantity` and with 16-CommonTransportationReport.xml) or absent from a cargo manifest.
- Options: Preferred: drop `CrewPerson` and `PassengerPerson` from the cargo manifest (the master stays as `MasterPerson`; crew and passengers are reported to the maritime administration in 16). Alternative: list the full crew and passengers and make the type a combined manifest.
- Needs decision: yes

### sea/15#F7 · Low · Lumeway Distribution’s sales customer-service contact used in a transport role
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: In this example Lumeway Distribution is the consignor of the manifested cargo. Its only contact is the sales department’s customer service, the same as in the catalogue and the order documents. For the questions this document raises (cargo, pickup, export formalities) the carrier, forwarder or authority needs Lumeway’s shipping or despatch contact; the checklist asks that a contact fit the party’s role in the document.
- Condition: The contact given for Lumeway Distribution in this example is one that handles the shipment (despatch, shipping or export), or there is none.
- Options: Preferred: give Lumeway Distribution a despatch or shipping contact for its transport roles. Alternative: leave the contact out of the transport documents where nobody needs to reach Lumeway about the shipment.
- Needs decision: no

### sea/15#F8 · Low · Velumi Trading’s contact: name, job title and department do not agree
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The contact is called `Purchasing`, but its job title is a customer service officer in the sales department, the same title and department as the seller Lumeway Distribution’s contact `Customer service`. Purchasing is a buyer function; a sales customer-service officer is not reachable as purchasing. Other examples of the world use `Procurement officer` for a purchasing contact. In this example Velumi Trading is the consignee, so its contact should be whoever receives the goods or handles their arrival, not purchasing. The same contact is used for Velumi Trading in every example of the flow.
- Condition: Name, job title and department of Velumi Trading’s contact agree with each other and with the role Velumi Trading has in this example.
- Options: Preferred: give Velumi Trading a purchasing contact with a purchasing job title and department (e.g. procurement officer, purchasing), and, in the transport documents, a contact for goods receipt or import. Alternative: keep one contact but make name, title and department consistent.
- Needs decision: no

### sea/15#F9 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of Velumi Trading (consignee). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

## Checked and consistent
- The manifest is issued and signed by Tidewell Ocean Lines as sending logistics operator, sent to the Island Customs Service (authority and distribution party), the customs authority of the port of first arrival `XLSEL`; consignor and consignee are those of 14-BillOfLading.xml, the bill the manifest refers to.
- Master Corin Halvard is given the same way as `MasterPerson`, as first `CrewPerson`, and in 16-CommonTransportationReport.xml; the passenger Ines Tavari is the same as in 16.
