# LLM review: 16-TenderReceipt.xml

## Reviewed version
- Run: `20261112T0851Z-manual` (a manual review, made before the skill existed; layout differs from the skill's)
- Example: `world/examples/tender/16-TenderReceipt.xml`, Git blob `947d3f76ed323067f1f47b34b36a7e5cfb559573` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 9f79ecd 2026-11-12 Publish workflow: publish only while the commit is still the head of main
- Skill: none · Register: none
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)
- Corrections: occurrence counts corrected in 12fd4c1, and findings corrected after an independent
  verification in c4e112d (before the rule that reviews are never changed)

Reviewed file: [16-TenderReceipt.xml](16-TenderReceipt.xml) · Flow: `tender` (`TENDER-2026-01`) · Review date: 2026-11-12

**Basis.** The semantic model of UBL 2.5 (`UBL-Entities-2.5.gc` from
<https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/>, SHA-256
`c7df070e…fe988d1`), the meaning of codes in `world/codelists`, and the other
XML documents of the flow where this document refers to them. The fictional
world (countries, currencies, languages, identifier schemes) is accepted as
given; only clashes with real standards are flagged.

**Severity.**
**High**: the value contradicts another value in this document or in a referenced document, or a reference is broken.
**Medium**: the element carries a meaning other than its UBL definition.
**Low**: plausibility, consistency or completeness remark.
**Recurring**: the same pattern occurs in many other examples.

## Summary

| # | Severity | Element(s) | Issue |
|---|---|---|---|
| 1 | Medium · Recurring | `…/cac:Language/cbc:LocaleCode` | A language code where a locale is defined |
| 2 | Medium · Recurring | `…/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`, `cbc:CityName[2]` | Italian text tagged as English, and tagged differently from the Tender it acknowledges |
| 3 | Medium · Recurring | `…/cac:ReceiverParty/cac:PostalAddress/cbc:Region` | A province in the element for a supra-national or economic region |
| 4 | Low | `…/cac:SenderParty/cac:PartyLegalEntity`, `…/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReason*` | A municipal department described as a commercially registered company with a transaction-type tax exemption |
| 5 | Low | `…/cac:ReceiverParty/cac:Contact`, `…/cac:ReceiverParty/cac:ServiceProviderParty` | Order-desk contact and a logistics provider on a tender receipt |
| 6 | Low · Recurring | `…/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` | Only the Italian-English legal form, without language, while the Tender has two language versions |

## Findings

### 1. `LocaleCode` holds a language, not a locale (Medium, recurring)

- **XPath:** `/TenderReceipt/cac:SenderParty/cac:Language/cbc:LocaleCode`
- **Value:** `en` with `@listID="ISO 639"`
- **UBL definition:** *Language. Locale Code*: "A code signifying the locale in which this language is used."
- **Why it does not fit:** The parent `cac:Language` already says *which* language
  (`cbc:ID` = `en`). `LocaleCode` should add *where/how* the language is used: a
  language plus a region, as in a BCP 47 or POSIX locale (`en-XB`, `en_XB`). The value repeats
  `Language/cbc:ID` and so adds nothing. `listID="ISO 639"` names a list of
  languages, not of locales. The document itself shows that the
  world has locale-level tags: the receiver's address uses `languageID="en-XB"`.
- **Suggestion:** `LocaleCode` = `en-XB` with a listID for BCP 47 / IETF language
  tags. Otherwise, omit the element.
- **Recurring:** `LocaleCode listID="ISO 639">en` occurs 362 times in 213 examples.

### 2. Address renderings tagged as English are Italian, and differ from the Tender (Medium, recurring)

- **XPaths:**
  - `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine` (`@languageID="en-XB"`)
  - `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano` (`@languageID="en-XB"`)
- **UBL definition:** *Address. Street Name*: "… (may be repeated only to provide the same content in multiple natural languages)." The same applies to *City Name*.
- **Why it does not fit:**
  - The repetition exists to give the *same* name in another natural language, and the
    `languageID` says which language. "Via delle Officine" is Italian, not English. A
    consumer that picks the `en` variant gets an Italian street name.
  - The tag also disagrees with the document this receipt acknowledges. In
    [`15-Tender.xml`](15-Tender.xml) the tenderer gives the same address of the
    same party with `languageID="en-XU"`. Here the contracting authority re-tags it
    `en-XB`. The second rendering is the party's own data and should not change
    between documents.
- **Suggestion:** Tag the second rendering with the language it is actually in.
  Alternatively, provide a genuine English rendering ("Workshops Street"). Keep the
  same tag as in the Tender.
- **Recurring:** `languageID="en-XB">Via delle Officine` occurs 31 times and `en-XU` 49 times
  in `world/examples`. Similar cases include `Viale della Stazione` and `Via del Terminal`.

### 3. `Region` holds a province (Medium, recurring)

- **XPath:** `/TenderReceipt/cac:ReceiverParty/cac:PostalAddress/cbc:Region`
- **Value:** `Province of Ferrano`
- **UBL definition:** *Address. Region*: "The recognized geographic or economic region or group of countries in which this address is located."
- **Why it does not fit:** A province is a political or administrative division of
  *one* country. UBL has a dedicated element for that, *Address. Country Subentity*:
  "The political or administrative division of a country … such as the name of its
  county, **province**, or state". `Region` is meant for supra-national or economic
  regions (e.g. a customs union or a free-trade area). The sender's own address in the
  same document uses `CountrySubentity` correctly (`Coastal State`), so the two party
  addresses are encoded inconsistently.
- **Suggestion:** Move the value to `cbc:CountrySubentity`, and to `cbc:CountrySubentityCode` if
  Urvania's list has a code for the province. Leave `Region` out, or use it for a real
  supra-national region.
- **Recurring:** `Region>Province of Ferrano` occurs 195 times in 104 examples.

### 4. A municipal department described as a company (Low)

- **XPaths:**
  - `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Lumeport Public Works Department`
  - `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE` ("Active, not in liquidation")
  - `/TenderReceipt/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL` ("Commercial register")
  - `/TenderReceipt/cac:SenderParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC` ("Sale to a public body") and `…/cbc:ExemptionReason`
- **UBL definitions:**
  - *Party Legal Entity*: "A description of this party as a legal entity."
  - *Company Liquidation Status Code*: "the party's liquidation status".
  - *Party Tax Scheme. Exemption Reason Code*: "A reason for the party's exemption from tax".
- **Why it does not fit:**
  - The sender is identified throughout as a *department* of the city. A department is
    an organisational unit, not a legal entity in a commercial register, and it cannot
    go into liquidation. The legal entity behind it is the city (its contracting
    authority), registered in a public-body register if at all.
  - "Sale to a public body" describes a *transaction* from the seller's side. That
    belongs in a `TaxCategory` on a sales document, not in the description of the party
    itself.
  - On a tender receipt, none of these tax details serve the document's purpose.
- **Suggestion:** Name the legal entity (e.g. "City of Lumeport") in
  `PartyLegalEntity/cbc:RegistrationName`, with a public-body register. Drop
  `CompanyLiquidationStatusCode`. Word the exemption as the party's status (e.g.
  "Public body, exempt from state sales tax"), or omit `PartyTaxScheme` on this
  document.

### 5. Contact and service provider are not those of a tender procedure (Low)

- **XPaths:**
  - `/TenderReceipt/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`, `…/cbc:JobTitle` = `Customer service officer`, `…/cbc:Department` = `Sales`
  - `/TenderReceipt/cac:ReceiverParty/cac:ServiceProviderParty` (`ServiceTypeCode` = `LOGISTICS` ("Logistics service"), `ServiceType` = "Warehousing and despatch", Castrano Logistics)
- **UBL definitions:**
  - *Party. Contact*: "The primary contact for this party."
  - *Party. Service Provider Party*: "A party providing a service to this party."
- **Why it does not fit:** The receipt is addressed to the tenderer about its tender.
  The relevant contact is the person or desk responsible for the bid, not the order desk
  of the sales department. The logistics provider is valid party master data, but it
  has no role in acknowledging a tender. It suggests a supply relationship that does not
  exist yet at this stage of the procedure. The contact does match the
  `TendererParty/cac:Contact` in [`15-Tender.xml`](15-Tender.xml), so the fix belongs
  in both documents.
- **Suggestion:** Give the tenderer a bid or tender contact (e.g. "Tender desk",
  Department "Sales – public tenders"). Omit `ServiceProviderParty` from
  pre-award procurement documents.

### 6. Legal form without language, and only one of the Tender's two versions (Low, recurring)

- **XPath:** `/TenderReceipt/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm`
- **Value:** `Società urvaniana per azioni (public limited company)` (no `languageID`)
- **UBL definition:** *Party Legal Entity. Company Legal Form*: "The company legal status, expressed as a text."
- **Why it does not fit:** The value mixes an Italian legal form with an English gloss
  and has no `languageID`. The document has no `DefaultLanguageCode` to fall back on.
  The Tender gives the same party's legal form in Urvanian (`qau`) and in
  `en-XU`. The receipt keeps only the mixed-language version, so the same party data
  differs between the two documents.
- **Suggestion:** Use the same renderings and language tags as in the Tender.

## References checked and consistent

- `cac:TenderDocumentReference/cbc:ID` = `VI-DOC-26-0201` resolves to
  [`15-Tender.xml`](15-Tender.xml). That Tender was sent by Valdara Industries
  (`XU-R-104274`), the `ReceiverParty` here, so the receipt goes to the right party.
- `cbc:ContractFolderID` = `PWD-2026-PARKS` and `cbc:ContractName` match the Tender, the
  Contract Notice and the Call for Tenders.
- Timing: the Tender was issued 2026-02-25 09:13. The receipt was created 2026-02-25 11:42
  (`RegisteredDate/Time`: "the date … on which the Tender Receipt was created") and issued
  17:47 the same day. All of this is
  before the deadline `TenderSubmissionDeadlinePeriod/EndDate` 2026-02-26 12:00 (in
  `02-ContractNotice.xml` and `03-CallForTenders.xml`). It is consistent with the note
  "Received on time … unopened until the opening": the `OpenTenderEvent` is
  2026-02-26 14:00.
- `SecurityListing/cbc:ID` `XU0001042501` has a valid ISIN check digit. `MarketCode` `XFER`
  is not a real ISO 10383 MIC, so there is no clash.
- Currencies `XBL` and `XUF` and countries `XB` and `XU` are user-assigned or unassigned
  ranges, so there is no clash with real codes.
