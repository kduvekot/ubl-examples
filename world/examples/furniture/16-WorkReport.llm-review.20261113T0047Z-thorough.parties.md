# LLM review: 16-WorkReport.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/16-WorkReport.xml`, Git blob `ff4f75f1f6e61357a2aa095fc65cac1d3e911e09` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/16#F1 · Medium · A public works department described as a company in the commercial register, with a liquidation status
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `8411`
- Why: Lumeport Public Works Department is a department of the city administration (ISIC 8411, "General public administration activities"; its tax scheme exempts it as a public body). Its legal entity nevertheless names the commercial register (world list CorporateRegistrationTypeCode: COMMERCIAL = "A register of businesses.") and carries `CompanyLiquidationStatusCode` ("the company's liquidation status"). A public body or a department is not a business in a commercial register and cannot be in liquidation; the register number used as its party and legal-entity identifier therefore claims a status the party does not have. (The legal form is, correctly, absent.)
- Condition: The legal entity of the department describes a public body: no commercial-register type and no liquidation status, or a registration scheme that is a register of public bodies.
- Options: (a, preferred) A world register of public bodies (or the city's own identifier) as the corporate registration scheme, without `CompanyLiquidationStatusCode`: it says what the party is. (b) Remove `CorporateRegistrationScheme` and `CompanyLiquidationStatusCode` and keep only the registration name and identifier. This decides how public bodies are identified in Bayvarra, so it is a story decision.
- Needs decision: yes

### furniture/16#F2 · Medium · Language/LocaleCode holds a language code, not a locale
- XPath: `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with `listID="ISO 639"` is the language itself, repeating `Language/ID` (`en`, ISO 639) and saying nothing about a locale. The same value occurs 362 times in 213 examples (counted with `grep -rc --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'` over world/examples).
- Condition: `LocaleCode` is absent, or holds a locale code from a declared locale list (language plus region), different from `Language/ID`.
- Options: (a, preferred) Remove `LocaleCode`: nothing in the flow depends on a regional variant of English. (b) A locale such as English as used in Bayvarra from a declared list (e.g. a BCP 47 tag), if the world wants to show the element.
- Needs decision: no

### furniture/16#F3 · Low · The approving facilities officer is not the contact of the approver party
- XPath: `/WorkReport/cbc:Note` = `Approved by the department's facilities officer.`
- XPath: `/WorkReport/cac:ApproverParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- Why: The note says the work report was approved by the department's facilities officer. `ApproverParty` ("The party approving this work report") carries only the department's identifier and name, and the only contact the department has in the document is its procurement office. Who approved, which the note stresses, is therefore not in the structured data, and the contact shown is not the approver.
- Condition: The approver is identifiable as the facilities officer (a contact or person under `ApproverParty`), or the note no longer names a role the data does not show.
- Options: (a, preferred) A `Contact` (functional name, job title 'Facilities officer', department) under `ApproverParty`. (b) Drop the role from the note.
- Needs decision: no

### furniture/16#F4 · Low · The place of work is a name only, although the address is registered
- XPath: `/WorkReport/cac:WorkReportLine/cac:ActivityOriginLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`
- Why: `ActivityOriginLocation` is "The Location from which the work in this Work Report Line originated or was performed". It carries the department's name and street only; the building is registered (`LUM-ADR-000417`) in the department's postal address in the same document. The location name also names the party rather than the place.
- Condition: The location of the work is identified by its address (register ID), consistent with the department's address.
- Options: (a, preferred) An `Address` with `LUM-ADR-000417` under the location, name reduced to the place (e.g. the new office). (b) Leave as is if the name is meant for display only, but add the address ID.
- Needs decision: no

### furniture/16#F5 · Low · PerformingParty in the sub-lines repeats the line's party and does not distinguish the installers
- XPath: `/WorkReport/cac:WorkReportLine/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[2]/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cbc:WorkItemDescription` = `Installer 1: seven hours.`
- Why: The sub-lines split the 14 hours between two installers, but their `PerformingParty` ("The Party performing the work") is the same company already given on the line. The party data in the sub-lines adds nothing, and what distinguishes them (the installer) is only in the description.
- Condition: Each sub-line's performing party says something the line does not (e.g. the installer as a person or contact), or the sub-lines carry no performing party.
- Options: (a, preferred) Remove `PerformingParty` from the sub-lines (the line already names the company). (b) Name the installer (`Person`) in each sub-line's performing party.
- Needs decision: no

### furniture/16#F6 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme/ExemptionReason` is "The reason for party's exemption from tax, expressed as text", i.e. the party's own status. The text opens with "Sale to a public body", which is the transaction-level reason (the same words as `TaxCategory/TaxExemptionReason` on the lines and totals of the order and invoice). The second half states the status correctly.
- Condition: The party's exemption reason states the party's status (a public body exempt from the state sales tax) without describing a sale.
- Options: (a, preferred) E.g. 'Public body: exempt from the state sales tax'. (b) Keep only the code and drop the text.
- Needs decision: no

### furniture/16#F7 · Low · A customs trader number for a public department in a domestic purchase
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department's additional identifier is a customs trader number (`schemeID` customs-trader). The flow is a domestic purchase of office furniture and its installation within Bayvarra, without any import, export or customs procedure, so the identifier has no use here (it occurs, with the same party master data, in 55 examples, counted with `grep -rl --include='*.xml' XB-TR-410548` over world/examples).
- Condition: The customs trader number is absent from documents without a customs purpose.
- Options: (a, preferred) Remove the additional identification from this flow. (b) Keep it only where a customs procedure takes place.
- Needs decision: no

## Checked and consistent
- Every party aggregate of the flow was compared across all 17 examples (a hash over every leaf value and attribute): Brackenmere Furniture, Brightmarket Stores and Lumeport Public Works Department are each described identically wherever they appear in full, and every short reference (signatory, delivery, warranty, manufacturer, payee, performing, approver party) uses the same register identifier and name as the full party.
- Party identifier, legal-entity `CompanyID` and the suffix of `ElectronicAddressID` agree for each party (20412466, 20410411, 20410548); tax identifiers carry the prefix of the party's state (UL- Upland State, CO- Coastal State), matching `CountrySubentityCode` and the tax scheme's jurisdiction.
- `check_ids.py`: all GS1 keys (party and location GLNs, GTINs) have valid check digits.

## Considered and refuted
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge of the GS1 prefix list); the same holds for every 952… key in the example.
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: the +999 telephone numbers could be real — refuted because country code 999 is not assigned in ITU-T E.164 (spare), and the web and mail domains are under the reserved .example domain.
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: a registration on 1 January (1996-01-01) looks like a placeholder date — refuted because nothing in the world says the Bayvarran register is closed that day, and no other value depends on it.
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's sales customer-service contact in roles other than selling (sender of planning documents, accounting supplier) — refuted because Brackenmere is a small enterprise whose trade-sales desk plausibly handles the whole customer relationship, invoices included; name, title and department agree with each other.
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: Brackenmere's address is in a state-level register (XB:UL) while the Lumeport parties use a city register — refuted because the rule for the examples is "address registers by country level": Bayvarra keeps them per state or city, which is what the schemeIDs show.
- `/WorkReport/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name`: a report issued by Brackenmere is signed by the customer — refuted because the signature records the department's approval, consistent with `ApproverParty`.
- `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: a city department registered at state level — refuted because the level is that of the tax (the state sales tax of Coastal State), not of the party.
- `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention`: the head of procurement in the address and a procurement officer as contact could contradict each other — refuted because they are two functions of the same office (attention line and day-to-day contact).
