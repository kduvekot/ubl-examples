# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/01-BusinessCard.xml`, Git blob `3b6f96c9fc61de8c4dad42aecf09e84a3a8c83dc` (committed)
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

### sea/01#F1 · Medium · Evidence issued by Lumeway, but described as the auditor's year-end count
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:EvidenceIssuingParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Description` = `Year-end count by the auditor.`
- Why: `EvidenceIssuingParty` is "The Party who issues the evidentiary Document". The evidence is typed as an audit report (`AUDIT`) and described as the count "by the auditor", so its issuer is the auditor, not the company whose stock was audited. As it stands the business card says Lumeway issued its own audit report, which contradicts the type code and the description.
- Condition: the issuing party of the evidence is the party that issued the evidence document as described by its type and description (an auditor for an audit report), or the type and description say that Lumeway's own stock count is the evidence.
- Options: (a) preferred: name the auditing firm as `EvidenceIssuingParty` (needs a party in the world); (b) keep Lumeway and change type and description to Lumeway's own stock count (weaker as evidence).
- Needs decision: yes (who the auditor is)

### sea/01#F2 · Medium · Tendering-only elements of Evidence used in a business card
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:CandidateStatement` = `The stock is counted every year.`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:Language/cbc:ID` = `en`
- Why: `CandidateStatement` is "Information about a candidate statement that the contracting authority accepts as a sufficient response", and `Evidence/Language` is "Information about a required translation to be part of the response, i.e. the language". Both belong to a tender: there is no contracting authority, candidate or response in a business card sent from a distributor to a customer. The sentence is a plain statement about the stock count (it would fit `Description`), and no translation is required of anyone.
- Condition: the evidence carries no `CandidateStatement` and no `Language`, or the document context has a contracting authority and a required translation.
- Options: (a) preferred: drop both and, if wanted, move the sentence into `Evidence/Description`; (b) none better seen.
- Needs decision: no

### sea/01#F3 · Medium · Language code in LocaleCode
- XPath: `/BusinessCard/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`), not the language itself, which `Language/ID` already gives as `en`. The value repeats `ID` and carries listID `ISO 639`, a language list. The same locale for Bayvarran English is written `en-XB` in the `languageID` attributes of the same document (`/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`). `LocaleCode` with listID `ISO 639` occurs in 213 of 250 examples (`grep -c LocaleCode world/examples/*/*.xml`, files with a count above 0).
- Condition: `LocaleCode` is either absent or a locale (language plus region) from a locale list.
- Options: (a) preferred: `en-XB` with a locale list (BCP 47), since Lumeway is in Bayvarra; (b) drop `LocaleCode`.
- Needs decision: no

### sea/01#F4 · Medium · A gate in AdditionalStreetName
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is not a street name but an entrance of the business park, which only matters for vehicles; it does not belong in Lumeway's postal address. The same value occurs in 25 of the 29 sea examples (`grep -c "Gate 3" world/examples/sea/*.xml`).
- Condition: no street-name element of the postal address holds a gate, dock or entrance.
- Options: (a) preferred: drop it from the postal address and give the gate, where a document needs it, in a delivery or pickup location (e.g. `Location/Description` or `Address/MarkAttention`); (b) none better seen.
- Needs decision: no

### sea/01#F5 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the functional name says purchasing and the e-mail is `purchasing@velumi.example`, but job title and department are those of a seller's customer service. For the receiver of a supplier's business card the purchasing function is the right one; job title and department contradict it. The same three values occur in every sea example that carries the Velumi contact (counted with `grep -A5 "<cbc:Name>Purchasing</cbc:Name>"` over `world/examples/sea/*.xml`).
- Condition: name, job title and department of Velumi's contact describe the same function.
- Options: (a) preferred: job title and department of purchasing (e.g. "Purchasing officer", "Purchasing"); (b) none better seen.
- Needs decision: no

### sea/01#F6 · Low · Additional document reference with only an ID
- XPath: `/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB`
- Why: the reference carries nothing but an identifier; the receiver cannot tell what the document is (an extract of the company register is a guess from the ID) or where to get it. It is not referred to by any other example (`grep -rn LD-REG-XB --include=*.xml world/examples`).
- Condition: the reference says what the document is (type code or description) and, if the receiver should read it, how to get it; or it is removed.
- Options: (a) preferred: add `DocumentTypeCode`/`DocumentDescription` (and an attachment if relevant); (b) drop it if the card has no use for it.
- Needs decision: no

### sea/01#F7 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the English renderings of Velumi Trading's address in Lisavu are tagged `en-XB` (English as used in Bayvarra), while the same address of the same party is tagged `en-XL` in the documents Velumi sends itself (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`). Across the sea flow the tag follows the sender's country rather than the address: `en-XB` in 16 examples, `en-XL` in 8 (`grep -c 'languageID="en-XB">Reef Street'` and `'languageID="en-XL">Reef Street'` over `world/examples/sea/*.xml`). The same rendering of the same address should carry the same language tag; for a Lisavu address `en-XL` is the natural one.
- Condition: Velumi's address renderings carry the same `languageID` in every example of the flow.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere; (b) a world-wide rule that the tag is the sender's locale, stated where the world documents its conventions.
- Needs decision: no

## Checked and consistent
- GLN `9520610900008` check digit correct (`check_ids.py`); prefix 952 is the GS1 prefix reserved for demonstrations and examples (own knowledge).
- Capability amount against the catalogue price: 2,000 × 520 XBL (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520`) = 1,040,000 XBL = `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount`.
- Sender and business party are the same party (Lumeway, `20410274`), as the definition of `SenderParty` allows; signatory is the owner of the card.
- Lumeway and Velumi party data (identifiers, register, address, endpoint) are the same as in `02-Catalogue.xml` and `05-Order.xml`.
- Currency codes XBL and XLC are not assigned in ISO 4217 (own knowledge).

## Considered and refuted
- `/BusinessCard/cac:BusinessCapability/cac:WebSite/cac:WebSiteAccess/cbc:Password`: a password in a business card looked out of place — refuted because `WebSiteAccess` is defined for "Access information for the website (e.g. guest credentials)" and the login `velumi` is issued to the receiver of the card.
- `/BusinessCard/cac:BusinessCapability/cac:ValidityPeriod/cbc:EndDate` = `2026-12-30`: the end date one day before year end looked arbitrary — refuted because the capability is backed by a year-end count, and validity until the eve of the next count is a legitimate reading.
- `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount`: the stock valued at the trade price rather than at cost — refuted because the element is just "a monetary amount as a measure of this capability", and the selling value is a fair measure for a customer.
- `/BusinessCard/cac:SenderParty/cbc:IndustryClassificationCode` = `4649`: street furniture under "Wholesale of other household goods" — refuted because ISIC 4649 includes wholesale of furniture (own knowledge).
