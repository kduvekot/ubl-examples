# LLM review: 07-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/07-CertificateOfOrigin.xml`, Git blob `9dd12c4b7afb7cb32c342c0e094823576afb0a28` (committed)
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

### road/07#F1 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL 2.5 defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". `Province of Ferrano` names a province, i.e. an administrative division, so it belongs in `CountrySubentity`. In the same document the Bayvarran addresses put their state in `CountrySubentity` (e.g. `/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`), so the two countries' first-level divisions are encoded differently. The same value occurs 219 times in the examples (counted with `grep -rho --include='*.xml' '<cbc:Region>[^<]*</cbc:Region>' world/examples`).
- Condition: No Urvanian address in this example holds the province in `Region`; the province is in `CountrySubentity` (with `CountrySubentityCode` where the Urvanian list has one).
- Options: (a, preferred) Move the province to `CountrySubentity` (plus code), as Bayvarra does; this matches the definition directly. (b) If the world's Urvanian provinces are not administrative divisions, use `Region` only for a real geographic/economic region and drop the province.
- Needs decision: no

### road/07#F2 · Medium · Language code in LocaleCode
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used". A locale is a language in a region (e.g. English as used in Bayvarra), but the value is the bare ISO 639 language code `en`, with `listID` `ISO 639`, which only repeats `Language/ID` = `en` next to it. The element therefore carries no locale. The value looks deliberate (plain `en` occurs 362 times as `LocaleCode` in the examples, counted with `grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>' world/examples | wc -l`), which is why a decision is needed.
- Condition: Every `LocaleCode` present names a locale (language plus region, from a list of locales), or the element is absent.
- Options: (a, preferred) Drop `LocaleCode` where it would only repeat the language: the party's language is fully given by `Language/ID`. (b) Use a locale value (e.g. a BCP 47 tag such as `en-XB`, which the examples already use as `languageID`) with a listID naming that scheme.
- Needs decision: yes

### road/07#F3 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". `Gate 3` is not a street name but an entrance of the business park, information that only matters to vehicles arriving there; in Lumeway's postal and registered business address it says nothing about where mail goes. The value is part of every rendering of Lumeway's address (79 occurrences of `Gate 3` in `AdditionalStreetName` over the examples, counted with `grep -rho --include='*.xml'`).
- Condition: No `AdditionalStreetName` of Lumeway's address holds a gate; where a gate or dock matters for a delivery it is given in an element meant for it (e.g. a delivery location's description or `Delivery/DeliveryLocation`).
- Options: (a, preferred) Drop the gate from the address; carry it, where a delivery needs it, in the delivery's location. (b) Keep it only in delivery addresses, in `MarkAttention`/`MarkCare` or a location description, not as a street name.
- Needs decision: no

### road/07#F4 · Medium · Embassy endorsement given by the Trade Accord Council
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cbc:RoleCode` = `LEGALISATION`
- Why: `EmbassyEndorsement` holds "Embassy Endorsement details": the legalisation of the certificate by the importing country's embassy or consulate. The endorser is the Lumeport Trade Accord Council, an organ of the trade accord, not an embassy, with role code `LEGALISATION`. Within a free trade area with preferential origin (the note) legalisation by the importing country is normally unnecessary; if the accord's council confirms the chamber's signature, that is a different endorsement from an embassy's. The Council is also identified in Bayvarra's federal business register (`20411096`), unusual for an intergovernmental body.
- Condition: The embassy endorsement, if present, is given by an embassy or consulate (of Bayvarra in Urvania); a confirmation by the accord's council, if the story needs one, is carried in an element that does not call it an embassy.
- Options: (a, preferred) Drop the embassy endorsement: preferential origin within the accord needs no legalisation. (b) Have Bayvarra's embassy or consulate in Urvania legalise it. (c) If the council's confirmation is part of the story, use a general `EndorserParty` with a council role.
- Needs decision: yes

### road/07#F5 · Low · Party master data copied into a document that does not use it
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: Section 4.8: data that looks copied from a party's master data into a document that does not use it is a finding. Valdara's `SecurityListing` ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") tells the reader where Valdara's shares are traded; nothing in this document depends on that. A certificate of origin is about the goods' origin and the exporter's identity, not its listing.
- Condition: Every optional party aggregate present in this document has a reason in this document's purpose.
- Options: (a, preferred) Leave the listed aggregates out of this document (they stay in the documents where they matter). (b) If the story gives this document a reason to carry them, state it in the document.
- Needs decision: no

### road/07#F6 · Low · Contacts do not fit the roles the parties have in this document
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist for a party in a role asks whether its `Contact` ("The primary contact for this party") fits the role and whether name, job title ("The job title or function of this contact") and department agree. Each party carries one fixed contact in every role of the flow, so here: Valdara as exporter gives its order desk in Sales; an exporter's contact answers customs and origin questions (export/customs desk). Lumeway as importer gives its customer-service desk in Sales; the importer's contact answers customs and origin questions (import/customs desk).
- Condition: Each contact listed above fits the role its party has in this document, and its name, job title and department agree with each other.
- Options: (a, preferred) Give the parties role-specific contacts (purchasing, goods receipt, despatch, customs, accounts payable/receivable, as the role needs) and pick the one matching the role. (b) Where a party has only one contact desk, at least make job title and department consistent with the desk's name.
- Needs decision: no

### road/07#F7 · Low · Chamber of commerce described as a company in the commercial register
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Ferrano Chamber of Commerce (ISIC `9411`, membership organisation) is registered in the commercial register and has a liquidation status. Depending on the country's system a chamber is a public-law body (then the checklist applies: not a company in a commercial register, no liquidation status) or a private association/company. The world's Urvanian chamber issues certificates of origin on public authority (`camera-ferrano`, issuer role), which suggests a public-law body; this cannot be settled from the examples.
- Condition: The chamber's legal entity matches what the chamber is in the world: either a public-law body without commercial registration and liquidation status, or a private entity registered as such.
- Options: (a, preferred) Decide the chamber's legal nature; if public-law, drop the commercial registration and the liquidation status. (b) If private, keep it and give it a legal form.
- Needs decision: yes

### road/07#F8 · Low · Endorsement signatories are desks, not individuals
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Legalisation desk`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Cargo claims desk`
- Why: `EndorserParty/SignatoryContact` is defined as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party" (the definition is carried over from the application; in an endorser it can only mean the individual who signs for the endorser). The values are functional desk names (`Certificates office`, `Cargo claims desk`, `Legalisation desk`), not individuals who can sign. `Contact/Name` recommends functional names for ordinary contacts, but a signatory is a person.
- Condition: Each `SignatoryContact` identifies the individual (or at least the signing function, e.g. job title) who signs the endorsement.
- Options: (a, preferred) Give the signatory contacts a signing function (`JobTitle`, e.g. certificates officer, underwriter) and keep the name functional if personal names are avoided in the world. (b) Use named fictional persons.
- Needs decision: no

### road/07#F9 · Low · Two endorsements with the same sequence number
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- Why: `EndorserParty/SequenceNumeric` is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". The legalisation and the insurance endorsement both have number 2. The legalisation confirms the chamber's signature and must follow it; the insurance endorsement was given before the chamber's (06-CertificateOfOrigin shows it endorsed while the chamber's was pending). Equal numbers could mean parallel steps, so this is only a remark.
- Condition: The sequence numbers state the order in which the endorsements were applied, without two endorsements sharing a number unless they are really parallel.
- Options: (a, preferred) Insurer 1, chamber 2, legalisation 3 (if kept). (b) Keep equal numbers and say nothing more, if parallel endorsement is meant.
- Needs decision: no

## Checked and consistent
- Party identity: Lumeway, Valdara, Castrano and Trasvia are described identically in every example of the flow that carries their full data (identifiers, tax scheme, legal entity, addresses, contact, electronic address), compared field by field over all 17 XML files of the flow; the only difference is the region subtag of the English renderings, which follows the sender.
- Identifier check digits (`check_ids.py`): GS1 GLN `9520610900008` and ISIN `XU0001042501` are correct.
- Roles: exporter and preparation party Valdara, importer Lumeway, issuer and first endorser the Ferrano Chamber of Commerce agree between the certificate, its application and 05-ExportCustomsDeclaration.
- Signatures: the certificate's own signature and the issuer endorsement's signature are the chamber's, the application's is Valdara's, as the roles require.

## Considered and refuted
- `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]`: an Italian-language street name tagged as English (`languageID` `en-XU`) — refuted because English text normally keeps foreign street names unchanged (as with "Via del Corso" or "Piazza San Marco"); the rendering is the English exonym the sender uses, and the region subtag follows the sender. The same Urvanian address is rendered identically by every sender of the flow, only the subtag changes with the sender's country.
- `/CertificateOfOrigin/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be a real one — refuted because prefix 952 is the GS1 prefix reserved for demonstrations and examples (own knowledge of the GS1 General Specifications), and the check digit is correct (`check_ids.py`).
- `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because country code +999 is reserved by ITU-T E.164 and assigned to no country (own knowledge).
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number rather than an identifier of the service provider — refuted because `ServiceProviderParty/ID` is "An identifier for this Service Provider" without saying who assigns it; a number Valdara assigns to its logistics provider (the VI prefix) is a legitimate reading.
