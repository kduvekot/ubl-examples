# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/10#F1 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (e.g. English as used in Bayvarra), but the value is the bare ISO 639 language code `en`, with `listID` `ISO 639`, which only repeats `Language/ID` = `en` next to it. The element therefore carries no locale. The value looks deliberate (plain `en` occurs 362 times as `LocaleCode` in the examples, counted with `grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>' world/examples | wc -l`), which is why a decision is needed.
- Condition: Every `LocaleCode` present names a locale (language plus region, from a list of locales), or the element is absent.
- Options: (a, preferred) Drop `LocaleCode` where it would only repeat the language: the party's language is fully given by `Language/ID`. (b) Use a locale value (e.g. a BCP 47 tag such as `en-XB`, which the examples already use as `languageID`) with a listID naming that scheme.
- Needs decision: yes

### road/10#F2 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". `Gate 3` is not a street name but an entrance of the business park, information that only matters to vehicles arriving there; in Lumeway's postal and registered business address it says nothing about where mail goes. The value is part of every rendering of Lumeway's address (79 occurrences of `Gate 3` in `AdditionalStreetName` over the examples, counted with `grep -rho --include='*.xml'`).
- Condition: No `AdditionalStreetName` of Lumeway's address holds a gate; where a gate or dock matters for a delivery it is given in an element meant for it (e.g. a delivery location's description or `Delivery/DeliveryLocation`).
- Options: (a, preferred) Drop the gate from the address; carry it, where a delivery needs it, in the delivery's location. (b) Keep it only in delivery addresses, in `MarkAttention`/`MarkCare` or a location description, not as a street name.
- Needs decision: no

### road/10#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL 2.5 defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". `Province of Ferrano` names a province, i.e. an administrative division, so it belongs in `CountrySubentity`. In the same document the Bayvarran addresses put their state in `CountrySubentity` (e.g. `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`), so the two countries' first-level divisions are encoded differently. The same value occurs 219 times in the examples (counted with `grep -rho --include='*.xml' '<cbc:Region>[^<]*</cbc:Region>' world/examples`).
- Condition: No Urvanian address in this example holds the province in `Region`; the province is in `CountrySubentity` (with `CountrySubentityCode` where the Urvanian list has one).
- Options: (a, preferred) Move the province to `CountrySubentity` (plus code), as Bayvarra does; this matches the definition directly. (b) If the world's Urvanian provinces are not administrative divisions, use `Region` only for a real geographic/economic region and drop the province.
- Needs decision: no

### road/10#F4 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs and Border Service of Bayvarra is a public authority (ISIC `8411`, public administration). Its `PartyLegalEntity` states a registration in the commercial register (`CorporateRegistrationTypeCode` "A code signifying the type of this registration scheme" = Commercial register) and a `CompanyLiquidationStatusCode` ("the party's liquidation status"). A state authority is not registered as a company and cannot go into liquidation; the checklist names exactly this case. The identifier it carries in the register's scheme is reused as `PartyIdentification`.
- Condition: The customs authority's legal entity, if described at all, names the basis it exists on (statute/public body register) and carries no commercial-register type and no liquidation status.
- Options: (a, preferred) Keep only `RegistrationName` (and, if the world has one, an identifier from a public-bodies register with its own scheme and type); drop the commercial registration and the liquidation status. (b) Drop `PartyLegalEntity` for the authority altogether.
- Needs decision: no

### road/10#F5 · Low · Contacts do not fit the roles the parties have in this document
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist for a party in a role asks whether its `Contact` ("The primary contact for this party") fits the role and whether name, job title ("The job title or function of this contact") and department agree. Each party carries one fixed contact in every role of the flow, so here: Lumeway as importer gives its customer-service desk in Sales; the importer's contact answers customs and origin questions (import/customs desk). Valdara as consignor gives its order desk in Sales; a consignor's contact deals with despatch and transport documents (and the goods leave from Castrano's warehouse).
- Condition: Each contact listed above fits the role its party has in this document, and its name, job title and department agree with each other.
- Options: (a, preferred) Give the parties role-specific contacts (purchasing, goods receipt, despatch, customs, accounts payable/receivable, as the role needs) and pick the one matching the role. (b) Where a party has only one contact desk, at least make job title and department consistent with the desk's name.
- Needs decision: no

### road/10#F6 · Low · Party master data copied into a document that does not use it
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: Section 4.8: data that looks copied from a party's master data into a document that does not use it is a finding. Valdara's `SecurityListing` ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") tells the reader where Valdara's shares are traded; nothing in this document depends on that. Valdara's `ServiceProviderParty` (its 3PL Castrano) is equally irrelevant to Bayvarra's import clearance.
- Condition: Every optional party aggregate present in this document has a reason in this document's purpose.
- Options: (a, preferred) Leave the listed aggregates out of this document (they stay in the documents where they matter). (b) If the story gives this document a reason to carry them, state it in the document.
- Needs decision: no

### road/10#F7 · Low · Border customs contact hours exclude the time the goods crossed
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Period/cbc:StartTime` = `07:30:00`
- Why: The contact of the Customs and Border Service of Bayvarra is its border office, with `Contact/Note` ("a textual description of the circumstances under which this contact can be used") limiting it to weekdays 08:00–17:00. The checklist asks whether an authority's contact is reachable when goods arrive: in this flow the truck was at the land border from 07:30 on 2026-03-24 (09-TransportationStatus), before the office's hours. A road border customs post is normally staffed around the clock.
- Condition: The customs contact's stated hours cover the time the consignment was at the border (or the contact is one that is reachable then).
- Options: (a, preferred) Give the border office hours that fit a road border post (e.g. 24 hours), separate from an administrative office's hours. (b) Move the border passage into the stated hours.
- Needs decision: no

## Checked and consistent
- Party identity: Lumeway, Valdara, Castrano and Trasvia are described identically in every example of the flow that carries their full data (identifiers, tax scheme, legal entity, addresses, contact, electronic address), compared field by field over all 17 XML files of the flow; the only difference is the region subtag of the English renderings, which follows the sender.
- Identifier check digits (`check_ids.py`): GS1 GLN `9520610900008` and ISIN `XU0001042501` are correct.
- Roles: importer, consignee, notifier and signatory Lumeway; consignor Valdara; customs party Bayvarra's customs agree with 05-ExportCustomsDeclaration and 09-TransportationStatus.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]`: an Italian-language street name tagged as English (`languageID` `en-XB`) — refuted because English text normally keeps foreign street names unchanged (as with "Via del Corso" or "Piazza San Marco"); the rendering is the English exonym the sender uses, and the region subtag follows the sender. The same Urvanian address is rendered identically by every sender of the flow, only the subtag changes with the sender's country.
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be a real one — refuted because prefix 952 is the GS1 prefix reserved for demonstrations and examples (own knowledge of the GS1 General Specifications), and the check digit is correct (`check_ids.py`).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because country code +999 is reserved by ITU-T E.164 and assigned to no country (own knowledge).
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number rather than an identifier of the service provider — refuted because `ServiceProviderParty/ID` is "An identifier for this Service Provider" without saying who assigns it; a number Valdara assigns to its logistics provider (the VI prefix) is a legitimate reading.
