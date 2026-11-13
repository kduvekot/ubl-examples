# LLM review: 01-BusinessCard.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/01-BusinessCard.xml`, Git blob `3b6f96c9fc61de8c4dad42aecf09e84a3a8c83dc` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/01#F1 · Medium · A language code in LocaleCode
- XPath: `/BusinessCard/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. The value `en` with listID `ISO 639` is the language code itself and repeats `/BusinessCard/cac:SenderParty/cac:Language/cbc:ID` = `en`; it names no locale. The same element and value occur 362 times in 213 examples of the world (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`, and `grep -rlc` for the files), nowhere with another value.
- Condition: no `Language/LocaleCode` holds a bare ISO 639 language code; where present it names a locale (language with region) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode` (the language is in `Language/ID`; nothing in the card depends on a locale), as in all earlier flows; (b) a locale such as `en-XB` (the tag the examples already use in `languageID`) with a list of language tags. Broad and context preferred (b).
- Needs decision: no
- From: broad (F3), parties (F1), context (F2)

### sea/01#F2 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is not a street name but a vehicle entrance of the business park; a postal address has no use for it, and `BlockName`, `BuildingNumber` and `PlotIdentification` already locate the premises. The value occurs 79 times in 76 examples of the world, 25 of them in this flow (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`; `grep -c 'Gate 3' world/examples/sea/*.xml`).
- Condition: no street-name element of Lumeway Distribution's postal address holds a gate, dock or entrance; where a truck must find the gate, the document gives it in a delivery, pickup or despatch location.
- Options: (a) preferred: drop it from the postal address and give it, where needed, in a location of the transport documents (`Location/Description`, a `SubsidiaryLocation`); (b) none better seen.
- Needs decision: no
- From: broad (F4), parties (F2), context (F7, Low)

### sea/01#F3 · Medium · Audit evidence issued by the audited company itself
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:EvidenceTypeCode` = `AUDIT`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Description` = `Year-end count by the auditor.`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:EvidenceIssuingParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: `EvidenceIssuingParty` is "The Party who issues the evidentiary Document". The evidence is typed as an audit report and described as the year-end count "by the auditor", so the document is issued by the auditor; with Lumeway Distribution (`20410274`, the party whose stock is counted) as issuer it reads as a self-declaration, which does not fit the type code and the description and weakens what makes it evidence for `CAP-STOCK`. It only partly survives refutation: Lumeway could issue its own record of the auditor's count, but then the type is not an audit report.
- Condition: issuer, type and description of the evidence agree: either the auditor is the `EvidenceIssuingParty` of an audit report, or Lumeway issues evidence typed and described as its own stock record.
- Options: (a) preferred: name Lumeway's audit firm as `EvidenceIssuingParty` (needs a party in the world), since text and code both say audit; (b) change type and description to Lumeway's own stock count.
- Needs decision: yes (who the auditor is)
- From: broad (F1), parties (F3), context (F4)

### sea/01#F4 · Medium · Tendering-only elements of Evidence in a business card
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cbc:CandidateStatement` = `The stock is counted every year.`
- XPath: `/BusinessCard/cac:BusinessCapability/cac:SuppliedEvidence/cac:Language/cbc:ID` = `en`
- Why: under `Evidence`, `CandidateStatement` is "Information about a candidate statement that the contracting authority accepts as a sufficient response", and `Language` is "Information about a required translation to be part of the response, i.e. the language". Both presuppose a procurement procedure with a contracting authority and a response; a business card from a distributor to a trading customer has neither. The sentence describes how the evidence is produced (it would fit `Description`), and no translation is required of anyone.
- Condition: the evidence carries no `CandidateStatement` and no `Language`, or the document is set in a procedure where a contracting authority defines accepted statements and translations.
- Options: (a) preferred: drop both and, if wanted, add "counted every year" to `SuppliedEvidence/Description`; (b) keep them only in a tendering flow.
- Needs decision: no
- From: broad (F2), context (F3)

### sea/01#F5 · Low · The card's subject is described under SenderParty, not under BusinessParty
- XPath: `/BusinessCard/cac:BusinessParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Lumeway Distribution Ltd`
- XPath: `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:StreetName` = `Distribution Drive`
- XPath: `/BusinessCard/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- Why: a BusinessCard is "a document used to provide information about a business party and its business capabilities"; `BusinessParty` is "The Party who owns this Business Card", `SenderParty` "The Party who sends this Business Card. This Party may be the owner of this Business Card or a third-Party …". The information the card exists to give (address, legal entity, tax registration, contact, industry classification, website) is on the sending role, while the party the card is about carries only identifier and name. Because both roles carry the same register ID `20410274`, a receiver can still find the data, and each value is true of the sender; so no element carries a wrong meaning, but the card's content is not on its subject.
- Condition: the description of Lumeway Distribution that the card is meant to give is carried in `cac:BusinessParty`; `cac:SenderParty` carries no more than identifies and reaches the sender.
- Options: (a) preferred: move the full party description to `BusinessParty` and reduce `SenderParty` to identification, name and electronic address; (b) drop `SenderParty`, since the sender is the owner (it is optional).
- Needs decision: no
- From: context (F1, Medium)

### sea/01#F6 · Low · Signature with only an ID and a signatory
- XPath: `/BusinessCard/cac:Signature/cbc:ID` = `LD-SIG-26-BC`
- XPath: `/BusinessCard/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: `Signature` is a signature applied to the document; this one has no signature method, no attachment or validation date, only an ID and the signing party, so nothing is actually signed or verifiable. The context part considered this and refuted it (a signature identifying the signer is a legitimate minimal use of version 2 of a published card); every earlier flow's merge kept it as a Low/yes question, because the pattern is a world-wide convention: 137 of the 147 `Signature` aggregates of the world hold only `ID` and `SignatoryParty` (lxml count over `world/examples/*/*.xml`).
- Condition: either the signature carries what makes it a signature (method, attachment or reference to the signature), or the card has no `Signature`; the rule is the same across the world.
- Options: (a) preferred: drop the signature where no signature exists; (b) keep the convention and document it. Context's refutation is option (b).
- Needs decision: yes (world-wide convention)
- From: context (Considered and refuted), made a finding in the merge

### sea/01#F7 · Low · Receiver's full legal and register data copied into a card about the sender
- XPath: `/BusinessCard/cac:ReceiverParty/cbc:IndustryClassificationCode` = `4649`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Velumi Trading Ltd`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- Why: the card informs Velumi Trading about Lumeway; it does nothing with Velumi's legal form, size, registration, registration scheme, industry classification or postal address. To address the card, identification and the electronic address suffice. The block is the party's master data (section 4.8).
- Condition: `ReceiverParty` carries only what identifies and reaches the receiver, or the card has a stated use for the rest.
- Options: (a) preferred: reduce `ReceiverParty` to `PartyIdentification`, `PartyName` and `ElectronicAddress`; (b) keep, with a reason.
- Needs decision: no
- From: context (F6)

### sea/01#F8 · Low · Velumi Trading described differently from the documents it issues (en-XB tags, legal form only in English)
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: the English renderings of Velumi Trading's address in Lisavu are tagged `en-XB` (English as used in Bayvarra) and the legal form is given once, in English, without `languageID`. In the order Velumi issues itself the same party has `en-XL` and its legal form in Lisavan and English: `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`, `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`. The flow splits along the issuer: `en-XB">Reef Street` in 16 sea examples, `en-XL">Reef Street` in 8 (`grep -c` over `world/examples/sea/*.xml`). The checklist asks that the same address of the same party be described the same way in every example. The context part refuted the tag within its lens (the tag describes the variety of English the issuer writes): a possible world convention, so this needs a decision.
- Condition: Velumi Trading's postal address, registration address and legal form carry the same renderings and `languageID` values in every example of the flow, following one documented rule.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu names and the legal form in both languages everywhere, as in 05-Order.xml; (b) a world-wide rule that the tag is the issuer's variety, recorded where the world documents its conventions, with the Lisavan legal form still given.
- Needs decision: yes (as in air, wood, plastics and sea c)
- From: broad (F7, Low/no), parties (F4); context (Considered and refuted, carried as the counter-argument)

### sea/01#F9 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/BusinessCard/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The same New Year's Day date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: 271 times in 181 examples of the world (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while parties with a known history have their own dates (here `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1988-10-03`). It reads as a default value, not a fact of the world (no fillers).
- Condition: every `RegistrationDate` is that party's registration date in the world, or the element is absent where the world has none.
- Options: (a) preferred: an own registration date per company from its history; (b) drop `RegistrationDate` where the world does not know it.
- Needs decision: yes
- From: parties (F6)

### sea/01#F10 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BusinessCard/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the functional name and the e-mail (`purchasing@velumi.example`) say purchasing, the right function for the receiver of a supplier's card; job title and department are those of a seller's customer service and repeat the sender's own (`/BusinessCard/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`, `/BusinessCard/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`). The same combination is on Velumi's contact in 02-Catalogue, 03-DigitalAgreement, 04-DigitalCapability and 05-Order.
- Condition: name, job title and department of Velumi's contact describe the same function, fitting its role here.
- Options: (a) preferred: a purchasing job title and department (e.g. "Procurement officer", "Purchasing"); (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F5), parties (F5), context (F5)

### sea/01#F11 · Low · Additional document reference with only an ID
- XPath: `/BusinessCard/cac:AdditionalDocumentReference/cbc:ID` = `LD-REG-XB`
- Why: `AdditionalDocumentReference` is "A reference to an additional document (e.g. presentations)". It has no type, description or attachment, so the receiver cannot tell what `LD-REG-XB` is (a register extract is a guess from the ID) or where to get it; no example of any flow carries this ID (`grep -rn LD-REG-XB --include='*.xml' world/examples`), unlike the brochure next to it, which has its own element and an attachment URI.
- Condition: the reference says what the document is (type code or description) and, if the receiver should read it, how to get it; or it is removed.
- Options: (a) preferred: add `DocumentTypeCode`/`DocumentDescription` and an attachment or URI; (b) drop it.
- Needs decision: no
- From: broad (F6), logistics (F1), context (F8)

### sea/01#F12 · Low · Capability validity ends on 30 December, without a start
- XPath: `/BusinessCard/cac:BusinessCapability/cac:ValidityPeriod/cbc:EndDate` = `2026-12-30`
- Why: the capability is a stock level backed by the 2025 year-end count; the next count would be at year end (31 December), and 30 December has no reason in the card; the period has no start (the count). Broad and logistics refuted this (the definition gives no rule for the end date; a validity ending on the eve of the next count is a legitimate choice). Both readings hold, so it stays as Low/yes. `2026-12-30` occurs in no other example of the world (`grep -rl --include='*.xml' 2026-12-30`).
- Condition: the validity period matches what supports the claim (e.g. from the count to the next count), or the end date has a reason in the world.
- Options: (a) start at the count date and end at the next count (context's preference); (b) keep, as broad/logistics argue.
- Needs decision: yes
- From: context (F9, Low/no); broad and logistics (Considered and refuted, carried as counter-argument)

## Checked and consistent
- GLN `9520610900008` check digit correct (`check_ids.py`); prefix 952 is the GS1 prefix for demonstrations and examples (own knowledge).
- `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount` = `1040000.00` / `/BusinessCard/cac:BusinessCapability/cbc:ValueQuantity` = `2000` = 520.00 XBL per bench, the trade price in `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `520` (recalculated); XBL is Lumeway's tax currency (`/BusinessCard/cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XBL`).
- Sender, business party, signatory and evidence issuer all carry Lumeway's register ID `20410274`; Lumeway's description (identifiers, customs trader `XB-TR-410274`, tax scheme of Upland State, legal entity, contact, endpoint) is the same across the flow (parties: compared leaf by leaf); Velumi's identifiers (`IC41859`, `XL-TR-041859`, endpoint `XL:IC41859`) are the same in every example.
- `CorporateStockAmount` `2500000` XBL is the same as in `22-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`.
- Stock capability of 2,000 benches in Marrowdale fits the later pre-carriage from Marrowdale (`09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:OriginalDespatchTransportationService/cbc:Name` = `Truck from Marrowdale to the port of Lumeport`).
- Issued 2026-05-04 16:39, after the catalogue of the same day (09:17). XBL and XLC are not ISO 4217 codes (own knowledge).

## Considered and refuted
- `/BusinessCard/cac:BusinessCapability/cac:WebSite/cac:WebSiteAccess/cbc:Password`: a password in a business card — refuted because `WebSiteAccess` is "Access information for the website (e.g. guest credentials)" and login `velumi` is issued to the receiver (from broad; context agreed).
- `/BusinessCard/cac:BusinessCapability/cbc:ValueAmount`: stock valued at the trade price rather than at cost — refuted because the element is "a monetary amount as a measure of this capability", not a balance-sheet value (from broad, money).
- `/BusinessCard/cac:SenderParty/cbc:IndustryClassificationCode` = `4649`: street furniture under "Wholesale of other household goods" — refuted because ISIC 4649 includes wholesale of furniture (from broad, own knowledge).
- `/BusinessCard/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: definition says "the number of shares" while the value is an amount — refuted because the element is of type Amount; the definition text is UBL's own inconsistency (TC write-up note) (from money, context).
- `/BusinessCard/cac:BrochureDocumentReference/cbc:ID` = `LD-BROCHURE-2026`: resolves to no example — refuted because the element names the kind of document and the attachment URI points to it (from logistics).
- `/BusinessCard/cac:ReceiverParty`: no `PartyTaxScheme` for Velumi — refuted: the card has no tax purpose for the receiver; nothing is implied by absence (from parties).
- `/BusinessCard/cac:SenderParty/cac:PostalAddress/cbc:TimezoneOffset` = `-1` against Velumi's `-1` — refuted: both countries are in the same time zone throughout the world (from parties).
- `/BusinessCard/cbc:PreviousVersionID` = `1`: version 1 is not in the flow — refuted: an earlier card can exist outside the flow; nothing refers to it (from context).
- `/BusinessCard/cac:BusinessCapability/cac:ValidityPeriod/cbc:EndDate`: refuted by broad and logistics — not followed, see F12.
- `/BusinessCard/cac:Signature/cbc:ID`: refuted by context — not followed, see F6.
- `/BusinessCard/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: en-XB tag refuted by context — not followed, see F8.

## Changed in the merge
- context/F1 → F5: Medium lowered to Low, because each value under `SenderParty` is true of the sender, which is the same party as the owner (same register ID), so no element carries a meaning other than its definition; the problem is where the card's content sits.
- context/F7 → F2: Low raised to Medium, aligned with broad and parties and all earlier flows (a gate in a street-name element is a value with another meaning).
- broad/F3, parties/F1, context/F2 → F1: preferred option set to dropping `LocaleCode` (broad and context preferred `en-XB`), aligned with all earlier flows; `en-XB` kept as option (b).
- broad/F7 (Low/no) + parties/F4 (Low/yes) → F8: grouped (same party, same cause); needs decision yes, because context's refutation shows a possible convention, as in earlier flows.
- context's refutation of the signature → F6 (Low/yes), aligned with the earlier flows' merges.
- context/F9 → F12: needs decision set to yes, because broad and logistics refuted it and the question cannot be settled from the XML.
