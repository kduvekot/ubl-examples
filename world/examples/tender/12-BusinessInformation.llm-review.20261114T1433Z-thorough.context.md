# LLM review: 12-BusinessInformation.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/12-BusinessInformation.xml`, Git blob `0bf87195abba0708389105425a425c36428e3dc5` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/12#F1 · Medium · The business "operation type" in the element for the operation on the registration
- XPath: `/BusinessInformation/cac:OperationType/cbc:Code` = `MANUFACTURE`
- XPath: `/BusinessInformation/cac:OperationType/cbc:Description` = `Manufacture of furniture for public spaces.`
- XPath: `/BusinessInformation/cac:BusinessParty/cbc:IndustryClassificationCode` = `3100`
- Why: `OperationType` is "the type of operation for which this document is created", its code "a code to specify the type of operation (e.g. deletion)": what the document does to the business registration information (create, update, delete, extract). `MANUFACTURE` / "Manufacture of furniture for public spaces." is the activity of the business, which the party already carries as its industry classification (ISIC 3100).
- Condition: `OperationType` says for which operation on the registration information the document was created; the activity of the business is stated in the party's classification and capabilities.
- Options: (a) Preferred: remove it (the notice sub-type already says "register extract"). (b) Use an operation code such as "extract"/"consultation" from a list of register operations.
- Needs decision: no

### tender/12#F2 · Medium · A requested publication date on an extract sent to one authority
- XPath: `/BusinessInformation/cbc:RequestedPublicationDate` = `2026-02-27`
- XPath: `/BusinessInformation/cbc:Note` = `Extract from the register of economic operators for the evaluation.`
- XPath: `/BusinessInformation/cac:NoticeSubType/cbc:SubTypeDescription` = `Extract asked for by a contracting authority.`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `RequestedPublicationDate` is "the requested publication date for this Business Registration Information Notice". This document is not a notice to be published: it is an extract "asked for by a contracting authority", sent to that authority "for the evaluation" of tenders, with a statement on exclusion grounds. Nobody is asked to publish it, and publishing an extract made for one evaluation would make no sense. The date equals the issue date.
- Condition: The document asks for publication only if it is a notice that is to be published.
- Options: (a) Preferred: remove the date. (b) None other seen.
- Needs decision: no

### tender/12#F3 · Medium · The two competing tenderers presented as a "group of business parties"
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupTypeCode` = `SAMEACTIVITY`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupType` = `Tenderers in this procedure registered for ISIC 3100`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[1]/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[2]/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Valdara Industries: registered, no exclusion grounds recorded.`
- Why: `BusinessPartyGroup` is "a group of Business Parties", with a type code whose example is the EEIG (a legal grouping of enterprises). The document is the information of one business, Valdara Industries ("the Party who owns this Business Registration Information"). The group here is "tenderers in this procedure registered for ISIC 3100": Valdara and its competitor Brackenmere. That is not a grouping the business belongs to; it is a list of who tendered, which a register of economic operators does not know and which discloses a competitor in Valdara's extract. Brackenmere's own data are not given, so the group serves no evaluation either.
- Condition: `BusinessPartyGroup` is present only for a grouping the business party is a member of (corporate group, EEIG, consortium).
- Options: (a) Preferred: remove the group. (b) If the service is to report on all tenderers, send one extract per tenderer.
- Needs decision: yes

### tender/12#F4 · Medium · Capability figures without a meaning, and different from the ones Valdara declares
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:CapabilityTypeCode` = `PRODUCTION`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount` = `4800000.00`
- XPath: `/BusinessInformation/cac:BusinessCapability/cbc:ValueQuantity` = `6000`
- XPath: `/BusinessInformation/cac:BusinessCapability/cac:SuppliedEvidence/cbc:Name` = `Annual accounts`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:ValueQuantity` = `4000`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:TechnicalCapability/cbc:Description` = `4,000 benches a year.`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: `ValueAmount` is "a monetary amount as a measure of this capability" and `ValueQuantity` "a quantity as a measure of this capability". The production capability carries 4800000.00 lume and 6000 pieces without saying what they measure (a year's output? turnover from benches?) or for which period; the evidence, "Annual accounts", suggests turnover. In its own qualification (13), dated two days earlier, Valdara declares a technical capability of "4,000 benches a year" and a financial capability of 9200000.00 lume. If the figures measure the same things, the two documents contradict each other (6000 against 4000 benches; 4.8 against 9.2 million); if they do not, neither document lets the reader see that. The evaluator who receives both cannot reconcile them.
- Condition: The measures of a capability say what they measure and for which period, and agree with the figures the same party declares elsewhere in the flow for the same thing.
- Options: (a) Preferred: one production capacity (benches a year) and one turnover figure for Valdara in 12 and 13, each named in its description. (b) Keep different figures and name the difference (e.g. capacity against output, group against company).
- Needs decision: yes

### tender/12#F5 · Medium · A language code in `LocaleCode`
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/12#F6 · Low · Urvanian is declared as a language of the notice, but only an address is given in it
- XPath: `/BusinessInformation/cbc:NoticeLanguageCode` = `en`
- XPath: `/BusinessInformation/cac:AdditionalNoticeLanguage/cbc:ID` = `qau`
- XPath: `/BusinessInformation/cbc:BriefDescription` = `Valdara Industries: registered, no exclusion grounds recorded.`
- XPath: `/BusinessInformation/cbc:Note` = `Extract from the register of economic operators for the evaluation.`
- Why: `AdditionalNoticeLanguage` is "an additional official language used in this document". The texts of the document (note, brief description, capability, group type, operation and sub-type descriptions) are in English only; the only Urvanian in the file is the street and city of Valdara's address (the 6 `languageID` attributes, 3 of them `qau`). The document is therefore not written in Urvanian.
- Condition: Every language declared for the document is used for its texts, or is not declared.
- Options: (a) Preferred: remove the additional language (the receiver is a Bayvarran authority). (b) Add Urvanian renderings of the descriptions.
- Needs decision: no

### tender/12#F7 · Low · A brochure and an ISO 9001 certificate in an official register extract
- XPath: `/BusinessInformation/cac:BrochureDocumentReference/cbc:ID` = `VI-BROCHURE-26`
- XPath: `/BusinessInformation/cac:AdditionalDocumentReference/cbc:ID` = `VI-ISO9001-CERT`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyName/cbc:Name` = `Bayvarra Information Service`
- XPath: `/BusinessInformation/cbc:Note` = `Extract from the register of economic operators for the evaluation.`
- Why: The sender is the public information service, and the document is an "extract from the register of economic operators for the evaluation". A company brochure ("a reference to a company brochure document") is marketing material of the business; it and the certificate are what the business itself would attach when it sends its own profile. In an extract issued by a register they suggest that the register vouches for them. Both references have only an ID.
- Condition: An extract issued by the register refers to what the register holds; material of the business is referenced in documents the business sends, and each reference says what it is.
- Options: (a) Preferred: remove the brochure; keep the certificate only if the register records certifications, with a document type. (b) Let Valdara be the sender of a business profile of its own, with these references.
- Needs decision: no

### tender/12#F8 · Low · The logistics provider of Valdara Industries, with contract number and key account desk, in a register extract
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ServiceProviderParty` is "a party providing a service to this party": Castrano Logistics, which warehouses and despatches for Valdara Industries, with the number of their arrangement and its key account desk. A register extract on registration and exclusion grounds has no use for the company's warehouse contractor. It looks copied from the party's master data into a document that does not use it.
- Condition: The party carries a service provider only in documents in which that provider acts or must be known (despatch, transport, customs).
- Options: (a) Preferred: remove the service provider here. (b) If the provider matters to the buyer, declare it where the document has a place for it (as a subcontractor or in the delivery terms).
- Needs decision: no

### tender/12#F9 · Low · Customs trader numbers of the parties in a register extract
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/BusinessInformation/cac:BusinessParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- Notice type `BUSREG`, sub-type `EXTRACT` and the note agree with each other; the extract is dated the day after the opening of tenders (02: 2026-02-26), which fits "for the evaluation".
- Valdara Industries is identified as in 03, 13 and 15 (register number `XU-R-104274`, ISIC 3100); Brackenmere Furniture as in 06–09 (`20412466`).
- `BusinessCapability/ValidityPeriod` ends 2026-12-31, after the evaluation.

## Considered and refuted
- A Bayvarran information service issuing an extract on a company registered in Urvania (`XU-R-104274`): suspected wrong source — refuted, the notices name a register of economic operators of Bayvarra (`EconomicOperatorRegistryURI`) in which foreign tenderers can be entered, and the brief description says "registered".
- `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:StreetName[2]` is tagged `en-XB` here and `en-XU` in 13 and 15 for the same text: suspected inconsistency — not judged in this lens (language tags of addresses are the parties part); the tag follows the sender's country in every example looked at (03, 12, 14, 16 against 13, 15).
- `/BusinessInformation/cac:BusinessCapability/cac:WebSite`: suspected duplicate of the party's `WebsiteURI` — refuted as a problem, the definition is "a web site where the capability is detailed" and a company site can be that.
