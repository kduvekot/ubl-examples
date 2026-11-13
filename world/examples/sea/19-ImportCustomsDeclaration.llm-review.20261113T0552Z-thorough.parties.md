# LLM review: 19-ImportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/19-ImportCustomsDeclaration.xml`, Git blob `64061347e935665afd0ab08807b3400cadbb512f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/19#F1 · Medium · The customs authority is described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41448`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: `CustomsParty` is "the Authority who is legally responsible for processing the Declaration"; the Island Customs Service is a state administration (ISIC 8411, public administration). Its legal entity gives it a `CompanyID` ("as registered within a company registration scheme") in the "Island companies register" of type "Commercial register" and a liquidation status. A customs administration is not a registered company and cannot be liquidated. The world's CorporateRegistrationTypeCode list has no code for public bodies; 26 `PartyLegalEntity` aggregates of public bodies over `world/examples/*/*.xml` carry `COMMERCIAL` and `ACTIVE` (counted with lxml over *.xml by `RegistrationName` of customs administrations, the maritime administration and the Trade Accord Council).
- Condition: The customs authority's legal entity claims no registration in a commercial companies register and carries no liquidation status.
- Options: (a) keep `RegistrationName` only (and the party identification), dropping `CompanyID`, `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` (preferred); (b) a register of public bodies with its own registration type code.
- Needs decision: no

### sea/19#F2 · Medium · A gate in the consignor's AdditionalStreetName
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and a postal address holds nothing that only matters for vehicles. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The consignor's postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it where vehicles need it (a delivery or pickup location) (preferred); (b) use the name of the park's internal road if it has one.
- Needs decision: no

### sea/19#F3 · Medium · A language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and name no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/19#F4 · Low · A chamber of commerce as notary and a warehouse company as witness of the power of attorney
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:NotaryParty/cac:PartyName/cbc:Name` = `Selanu Chamber of Commerce`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PowerOfAttorney/cac:WitnessParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- Why: `NotaryParty` is "the Party who notarises this Power of Attorney", `WitnessParty` "a Witness to this Power of Attorney". Notarisation is the act of a notary (own knowledge); a chamber of commerce certifies signatures and origin, but is not a notary, and it is identified only by a number in the companies register. A witness attests that the principal signed; that is done by a natural person, not by a warehouse company, and Nalevi, which stores the goods for Velumi (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`), has an interest of its own in the customs clearance. Nothing in the flow says why these two parties take these roles.
- Condition: The notary is a notary (or the element is absent if the power of attorney was not notarised), and the witness is a person or party with no interest in the clearance, or absent.
- Options: (a) drop `NotaryParty` and `WitnessParty`, since a customs power of attorney is usually a signed form with neither (preferred: no new parties needed); (b) give a notary's office in Selanu and a natural person as witness.
- Needs decision: yes (changes who takes a role)

### sea/19#F5 · Low · Contacts that do not fit an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:Contact/cbc:Name` = `Export desk`
- Why: The importer's contact is named Purchasing but is a customer service officer in Sales; name, title and department disagree, and none is the import function customs would ask about the declaration (the broker's contact `Declarations` fits its role). The forwarder appears in an import declaration with its export desk. Both are the parties' master-data contacts, used in every role in the flow.
- Condition: The importer's contact agrees in name, title and department and is the function responsible for imports; the forwarder's contact is the one handling the import side, or absent.
- Options: (a) role-specific contacts (preferred); (b) drop the contacts where the broker is the contact for customs.
- Needs decision: no

### sea/19#F6 · Low · Tax registrations and share capital of Bayvarran parties in the island's import declaration
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: The Island Customs Service needs the consignor's and forwarder's name, address and identification; their state sales-tax registrations in Bayvarra and the consignor's share capital play no part in levying Lisavu duties and taxes on the importer. They are copied from master data (section 4.8 of the review rules).
- Condition: Consignor and forwarder carry only the party data the import declaration uses.
- Options: (a) drop their `PartyTaxScheme` and the consignor's `CorporateStockAmount`/`FullyPaidSharesIndicator` (preferred); (b) keep them with a reason the declaration needs them.
- Needs decision: no

## Checked and consistent
- The agent of the importer, the holder of the power of attorney, the notifier, the customs agent of the stage and the signatory are the same party (Tevaro Customs Brokers, `IC41585`), and the document number prefix `TCB` is Tevaro's, so the broker lodges the declaration on Velumi's behalf as the power of attorney describes ("lodging import declarations and paying duties and taxes on behalf of Velumi Trading").
- The importer and consignee (Velumi Trading, `IC41859`, customs trader `XL-TR-041859`) and the consignor (Lumeway Distribution, `20410274`) match the bill of lading `14-BillOfLading.xml` and the manifest `15-Manifest.xml` by identifier.
- The customs authority is the Island Customs Service, `IC41448`, as in the manifest `15-Manifest.xml`; its contact (import office) fits the role.
- Velumi's, Tevaro's and the customs service's Lisavu addresses and legal forms carry `en-XL` and Lisavan renderings, as in the other examples issued on the island.
- The manufacturer (Valdara Industries, `XU-R-104274`) is the same in both goods items and in the other examples of the flow; the origin country Urvania fits a manufacturer in the Urvanian register.
- Industry classifications fit: 8411 for a customs administration, 5229 for a customs broker and a forwarder, 4649 for the wholesalers.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AgentParty/cac:PartyName/cbc:Name`: the agent given twice (as `AgentParty` and in the power of attorney) — refuted because the two elements say different things (who acts for the importer, and who holds this power of attorney), and they agree.
- `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name`: the broker as "responsible for contact on master level" — refuted because the broker is the party customs deals with for this declaration.
- `/ImportCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode`: ISIC 8411 rather than a customs-specific class — refuted because ISIC Rev.4 8411 covers the operation of taxation schemes and duty collection on goods.
