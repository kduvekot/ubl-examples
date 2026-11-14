# LLM review: 12-BusinessInformation.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/12-BusinessInformation.xml`, Git blob `0bf87195abba0708389105425a425c36428e3dc5` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/12#F1 · Medium · The business's activity in the element for the operation on the registration
- XPath: `/BusinessInformation/cac:OperationType/cbc:Code` = `MANUFACTURE`
- XPath: `/BusinessInformation/cac:OperationType/cbc:Description` = `Manufacture of furniture for public spaces.`
- Why: OperationType is "The type of operation for which this document is created", its Code "A code to specify the type of operation (e.g. deletion)": the operation performed on the business registration information (creation, update, deletion, here an extract). "Manufacture" is what the business does, which the party's IndustryClassificationCode 3100 and the capability already say.
- Condition: OperationType states what is done with the registration information, or is absent.
- Options: (a) remove it; the sub-type `EXTRACT` already says what the document is (preferred); (b) an operation code such as "extract" or "consultation".
- Needs decision: no

### tender/12#F2 · Medium · Two competing tenderers presented as a party group
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupTypeCode` = `SAMEACTIVITY`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cbc:GroupType` = `Tenderers in this procedure registered for ISIC 3100`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[1]/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/BusinessInformation/cac:BusinessPartyGroup/cac:Party[2]/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: BusinessPartyGroup is "A group of Business Parties", its type "A code to specify the type of grouping (e.g. EEIG)": a grouping the business belongs to (a consortium, an economic interest grouping, a corporate group). Valdara Industries and Brackenmere Furniture are competitors in this procedure, not a group; that two companies have the same activity class does not make them one. Moreover the document is an extract of Valdara's registration: who else tenders is not registration data of Valdara, and the register service would not know the tenderers of a procedure whose tenders are confidential.
- Condition: A party group is stated only for a grouping the business is a member of.
- Options: (a) remove the group (preferred); (b) if Valdara belongs to a real grouping (e.g. with its subcontractor Saltmere Engineering), state that one.
- Needs decision: yes

### tender/12#F3 · Medium · Language code in LocaleCode
- XPath: `/BusinessInformation/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/12#F4 · Medium · A province in Region
- XPath: `/BusinessInformation/cac:BusinessParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/12#F5 · Low · A requested publication date for an extract sent to one authority
- XPath: `/BusinessInformation/cbc:RequestedPublicationDate` = `2026-02-27`
- XPath: `/BusinessInformation/cac:NoticeSubType/cbc:SubTypeDescription` = `Extract asked for by a contracting authority.`
- XPath: `/BusinessInformation/cbc:Note` = `Extract from the register of economic operators for the evaluation.`
- Why: RequestedPublicationDate is "The requested publication date for this Business Registration Information Notice." The document is an extract sent to the contracting authority for its evaluation of tenders; nothing is to be published, so the date has no business reason.
- Condition: A publication date is present only when the information is to be published.
- Options: (a) remove it (preferred); (b) none other seen.
- Needs decision: no

### tender/12#F6 · Low · A public body described as a company in a commercial register
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:SenderParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Bayvarra Information Service, Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/12#F7 · Low · The department's tax exemption reason describes a sale
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/BusinessInformation/cac:ReceiverParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit.
- The extract (2026-02-27 16:26) is issued after the opening of tenders (2026-02-26 14:00 in 02), for the evaluation, as its note says; BriefDescription ("registered, no exclusion grounds recorded") is the information such an extract gives.
- Sender is the Bayvarra Information Service, the receiver of the notices 01, 02 and 21; receiver is the department; business party is Valdara Industries, described as in 03, 14, 16 (hash of leaf values). The service provider, share capital and listing of Valdara are business registration data and belong here.
- Capability: 4 800 000.00 lume for 6 000 benches is 800 lume per bench (own calculation); validity to 2026-12-31 lies after the issue date; the web site URI equals the party's WebsiteURI.
- Party group member IDs are the register numbers of the two parties as used elsewhere in the flow (XU-R-104274, 20412466).

## Considered and refuted
- `/BusinessInformation/cac:BusinessCapability/cbc:ValueAmount`: 800 lume per bench is above the 350 to 600 lume the procedure allows per bench — refuted because the capability describes Valdara's yearly production in general, not the price of this bench.
- `/BusinessInformation/cac:BusinessCapability/cac:SuppliedEvidence`: annual accounts as evidence for a production capability — refuted because the amount measure (production value) can be read from the accounts.
- `/BusinessInformation/cac:AdditionalNoticeLanguage`: Urvanian as additional language of a Bayvarran extract — refuted because the business is Urvanian and its registration data are bilingual.
- `/BusinessInformation/cac:BusinessParty/cac:PartyIdentification/cbc:ID`: an Urvanian company in the Bayvarran register of economic operators — refuted because the Trade Accord lets operators of the three countries register for procurement; the party keeps its Urvanian register number.

## Outside this review
- Whether the register service knows on 2026-02-27 who the tenderers are (see the party group finding) is also a question of the flow's story.
