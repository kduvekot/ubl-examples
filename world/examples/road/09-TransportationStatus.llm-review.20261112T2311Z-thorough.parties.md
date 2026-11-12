# LLM review: 09-TransportationStatus.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/09-TransportationStatus.xml`, Git blob `e1a610d76310b4d013c2aaf846292a8900b63b3e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### road/09#F1 · Medium · Language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (e.g. English as used in Bayvarra), but the value is the bare ISO 639 language code `en`, with `listID` `ISO 639`, which only repeats `Language/ID` = `en` next to it. The element therefore carries no locale. The value looks deliberate (plain `en` occurs 362 times as `LocaleCode` in the examples, counted with `grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>' world/examples | wc -l`), which is why a decision is needed.
- Condition: Every `LocaleCode` present names a locale (language plus region, from a list of locales), or the element is absent.
- Options: (a, preferred) Drop `LocaleCode` where it would only repeat the language: the party's language is fully given by `Language/ID`. (b) Use a locale value (e.g. a BCP 47 tag such as `en-XB`, which the examples already use as `languageID`) with a listID naming that scheme.
- Needs decision: yes

### road/09#F2 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". `Gate 3` is not a street name but an entrance of the business park, information that only matters to vehicles arriving there; in Lumeway's postal and registered business address it says nothing about where mail goes. The value is part of every rendering of Lumeway's address (79 occurrences of `Gate 3` in `AdditionalStreetName` over the examples, counted with `grep -rho --include='*.xml'`).
- Condition: No `AdditionalStreetName` of Lumeway's address holds a gate; where a gate or dock matters for a delivery it is given in an element meant for it (e.g. a delivery location's description or `Delivery/DeliveryLocation`).
- Options: (a, preferred) Drop the gate from the address; carry it, where a delivery needs it, in the delivery's location. (b) Keep it only in delivery addresses, in `MarkAttention`/`MarkCare` or a location description, not as a street name.
- Needs decision: no

### road/09#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL 2.5 defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". `Province of Ferrano` names a province, i.e. an administrative division, so it belongs in `CountrySubentity`. In the same document the Bayvarran addresses put their state in `CountrySubentity` (e.g. `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`), so the two countries' first-level divisions are encoded differently. The same value occurs 219 times in the examples (counted with `grep -rho --include='*.xml' '<cbc:Region>[^<]*</cbc:Region>' world/examples`).
- Condition: No Urvanian address in this example holds the province in `Region`; the province is in `CountrySubentity` (with `CountrySubentityCode` where the Urvanian list has one).
- Options: (a, preferred) Move the province to `CountrySubentity` (plus code), as Bayvarra does; this matches the definition directly. (b) If the world's Urvanian provinces are not administrative divisions, use `Region` only for a real geographic/economic region and drop the province.
- Needs decision: no

### road/09#F4 · Medium · Status location is the carrier's name, not a place
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Trasvia Haulage`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Land border crossing Urvania–Bayvarra`
- Why: `StatusLocation` holds "Locations associated with this Transportation Status report". Its name `Trasvia Haulage` is the carrier, not a location; the report is about the border crossing (the event's location) and the truck now in transit in Bayvarra.
- Condition: `StatusLocation`, if present, names or identifies a place the status refers to.
- Options: (a, preferred) Drop `StatusLocation`; the event carries the location. (b) Use the truck's position (e.g. Marrowdale, `XBMRW`, where the driver rests) or the border crossing.
- Needs decision: no

### road/09#F5 · Low · Contacts do not fit the roles the parties have in this document
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist for a party in a role asks whether its `Contact` ("The primary contact for this party") fits the role and whether name, job title ("The job title or function of this contact") and department agree. Each party carries one fixed contact in every role of the flow, so here: Lumeway as delivery recipient/consignee gives its customer-service desk in Sales; a consignee's contact receives the goods (goods-in at the distribution centre).
- Condition: Each contact listed above fits the role its party has in this document, and its name, job title and department agree with each other.
- Options: (a, preferred) Give the parties role-specific contacts (purchasing, goods receipt, despatch, customs, accounts payable/receivable, as the role needs) and pick the one matching the role. (b) Where a party has only one contact desk, at least make job title and department consistent with the desk's name.
- Needs decision: no

### road/09#F6 · Low · Registration date 1996-01-01 looks like a default, not a party's real date
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". `Trasvia Haulage SRU` carry the same date, 1 January 1996, a public holiday on which no register records an incorporation. Over the examples, `1996-01-01` occurs 271 times as `RegistrationDate`, for at least 25 different companies in both countries (counted over `*.xml` with `grep -rho --include='*.xml' '<cbc:RegistrationDate>[^<]*'` and a per-RegistrationName count), while the other parties have individual dates (Lumeway 1988-10-03, Valdara 1962-04-12). It reads as a filler (IND5), not as each company's own history.
- Condition: Each party's `RegistrationDate` is its own plausible registration date (a working day consistent with its story), or the element is absent for that party.
- Options: (a, preferred) Give each company its own date from its history. (b) Leave `RegistrationDate` out where the world has no date for the company.
- Needs decision: no

## Checked and consistent
- Party identity: Lumeway, Valdara, Castrano and Trasvia are described identically in every example of the flow that carries their full data (identifiers, tax scheme, legal entity, addresses, contact, electronic address), compared field by field over all 17 XML files of the flow; the only difference is the region subtag of the English renderings, which follows the sender.
- Identifier check digits (`check_ids.py`): GS1 GLN `9520610900008` and ISIN `XU0001042501` are correct.
- Roles: sender, carrier, event responsible party and signatory Trasvia; receiver and consignee Lumeway; the event signature by the Customs and Border Service of Bayvarra fits a border entry.
- `TransportEvent/Contact` (`Planning desk`, `+999 1 041 354 4822`) is Trasvia's contact, the event's responsible party.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]`: an Italian-language street name tagged as English (`languageID` `en-XU`) — refuted because English text normally keeps foreign street names unchanged (as with "Via del Corso" or "Piazza San Marco"); the rendering is the English exonym the sender uses, and the region subtag follows the sender. The same Urvanian address is rendered identically by every sender of the flow, only the subtag changes with the sender's country.
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be a real one — refuted because prefix 952 is the GS1 prefix reserved for demonstrations and examples (own knowledge of the GS1 General Specifications), and the check digit is correct (`check_ids.py`).
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because country code +999 is reserved by ITU-T E.164 and assigned to no country (own knowledge).

## Outside this review
- Timeline: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` reports the import declaration accepted at the border by 08:55, but `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`; a question for the logistics part and the cross-document review.
