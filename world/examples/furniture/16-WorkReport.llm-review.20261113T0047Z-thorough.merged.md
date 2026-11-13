# LLM review: 16-WorkReport.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/16-WorkReport.xml`, Git blob `ff4f75f1f6e61357a2aa095fc65cac1d3e911e09` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/16#F1 · Medium · Budget commitment cited as a billing document
- XPath: `/WorkReport/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COMMIT-26-0381`
- Why: `BillingReference` is "A reference to a related billing document". `PWD-COMMIT-26-0381` carries the department's prefix and is, by its name, the department's budget commitment (an encumbrance), the buyer's internal financial record, not a billing document (invoice, credit note, self-billing). The element thus carries a meaning other than its definition. The supplier issuing the report would also know the commitment number only if the order gave it, and `15-Order.xml` does not; `17-Invoice.xml`, where a public buyer would need it most, does not quote it. That the reference resolves to no example is not the problem (logistics refuted that: an internal record need not exist as an example).
- Condition: `BillingReference` refers to a billing document, or is absent; the commitment number, if needed, is carried as an additional document reference with a document type, given in the order and quoted on the invoice.
- Options: (a, preferred) move it to `AdditionalDocumentReference` with a document type "budget commitment", give it in `15-Order.xml` and quote it in `17-Invoice.xml`; (b) remove it.
- Needs decision: no
- From: broad (Medium, yes), context (Low, no); logistics refuted the unresolved-reference aspect

### furniture/16#F2 · Medium · Public works department described as a company in the commercial register, with a liquidation status
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The department is part of the city administration (ISIC 8411; exempt as a public body). Its legal entity names the commercial register (world list: COMMERCIAL = "A register of businesses.") and carries a liquidation status ("A code signifying the party's liquidation status"); a public department is not a business in a commercial register and cannot be in liquidation. Same description in 15, 16 and 17.
- Condition: The department's legal entity describes a public body: no liquidation status, and no commercial-register type (a register of public bodies, or none).
- Options: (a, preferred) drop `CompanyLiquidationStatusCode` and the COMMERCIAL registration scheme, keeping registration name and identifier, or use a world register of public bodies; (b) the legal entity of the City of Lumeport, which would change who the party is.
- Needs decision: no
- From: broad (Medium, no), parties (Medium, yes)

### furniture/16#F3 · Medium · Language code in LocaleCode
- XPath: `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/16#F4 · Low · Packaging-disposal charge that the order does not contain
- XPath: `/WorkReport/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Packaging disposal`
- XPath: `/WorkReport/cac:AllowanceCharge/cbc:Amount` = `24.00`
- XPath: `/WorkReport/cac:StatementMonetaryTotal/cbc:ChargeTotalAmount` = `24.00`
- Why: The work report adds a document-level charge of 24.00 for packaging disposal (code `AEO` "Collection and recycling") to the 14 installation hours. The order it reports against, `15-Order.xml`, contains only the desks and the hours (`15-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00`), and no document of the flow agrees the charge. A public buyer's order normally fixes what may be billed (own knowledge of procurement practice). `17-Invoice.xml` bills the same 24.00. Whether the charge was agreed is a question of the story.
- Condition: The packaging-disposal charge can be traced to the order or another agreement in the flow (or an approval stated in the report), or it is neither reported nor billed.
- Options: (a, preferred) add the charge to `15-Order.xml` (anticipated total 5976.00); (b) state in the report that the department's officer approved it on site (the report is signed by the department); (c) drop it from 16 and 17.
- Needs decision: yes
- From: broad (yes), money (no)

### furniture/16#F5 · Low · Office work charged to the parks renewal programme
- XPath: `/WorkReport/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/WorkReport/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- XPath: `/WorkReport/cac:WorkReportLine/cac:WorkPhaseReference/cbc:WorkPhase` = `Furnishing: the new office is furnished`
- Why: `AccountingCost` is "An accounting cost centre or account to which this Work Report is charged". In the same document the work belongs to the office project and its furnishing phase; the parks renewal programme, which in the tender flow carries the park benches (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`), does not fit unless the office belongs to it, which nothing says. Same cost centre in `15-Order.xml` and `17-Invoice.xml`.
- Condition: The cost centre fits the office project, consistently in 15, 16 and 17, or the flow states why the parks programme pays for the office.
- Options: (a, preferred) a cost centre for the office project (e.g. matching `PWD-PLAN-OFFICE-26`); (b) a note that the new office belongs to the parks programme.
- Needs decision: no
- From: broad, money, context (all three: yes)

### furniture/16#F6 · Low · Zero tax total without category, and a charge without tax category
- XPath: `/WorkReport/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/WorkReport/cac:WorkReportLine/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/WorkReport/cac:AllowanceCharge/cbc:ChargeIndicator` = `true`
- Why: `TaxTotal` is "A total amount of taxes of a particular kind applicable to this Work Report". The report states 0.00 at document and line level without a `TaxSubtotal` or tax category, so it does not say why no tax applies (exempt, not subject, or not yet calculated), and the charge has no `TaxCategory`. `17-Invoice.xml`, which bills the same amounts, states the exempt STT category with reason `PUBLIC` for the lines and the charge; here the exemption is only implied (IND6).
- Condition: The report's tax figures state the category and reason they rest on, as in 17, or the report carries no tax figures.
- Options: (a, preferred) remove the tax totals, since the work report is not the billing document (the smaller change); (b) a `TaxSubtotal` with exempt STT and reason `PUBLIC` (taxable amount 696.00) and the same category on the charge (money's preference).
- Needs decision: no
- From: money

### furniture/16#F7 · Low · The approving facilities officer is not in the structured data
- XPath: `/WorkReport/cbc:Note` = `Approved by the department's facilities officer.`
- XPath: `/WorkReport/cac:ApproverParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- Why: The note says the facilities officer approved the report. `ApproverParty` ("The party approving this work report") carries only the department's identifier and name, and the department's only contact in the document is its procurement office. Who approved, which the note stresses, is not in the structured data, and the contact shown is not the approver.
- Condition: The approver is identifiable as the facilities officer (a contact under `ApproverParty`), or the note no longer names a role the data does not show.
- Options: (a, preferred) a `Contact` (job title "Facilities officer", department) under `ApproverParty`; (b) drop the role from the note.
- Needs decision: no
- From: parties

### furniture/16#F8 · Low · Place of work named only, although its address is registered
- XPath: `/WorkReport/cac:WorkReportLine/cac:ActivityOriginLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`
- Why: `ActivityOriginLocation` is "The Location from which the work in this Work Report Line originated or was performed". It carries a name only; the building is registered (`LUM-ADR-000417`) in the department's postal address in the same document, and the new office (floor or room) is not identified. Logistics and context refuted the narrower suspicion that the name is a company rather than a place (it designates the department's building on Civic Square); the missing identification remains.
- Condition: The place of work is identified by its address (register ID), consistent with the department's address, preferably with the office's floor or room.
- Options: (a, preferred) an `Address` with `LUM-ADR-000417` under the location, the name reduced to the place (e.g. the new office); (b) keep the name and add the address ID.
- Needs decision: no
- From: parties (logistics and context refuted the company-name aspect)

### furniture/16#F9 · Low · PerformingParty in the sub-lines repeats the line's party
- XPath: `/WorkReport/cac:WorkReportLine/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[2]/cac:PerformingParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cbc:WorkItemDescription` = `Installer 1: seven hours.`
- Why: The sub-lines split the 14 hours between two installers, but their `PerformingParty` ("The Party performing the work") is the company already given on the line; what distinguishes them (the installer) is only in the description. Context refuted the suspicion that the performing party should be the installer (a party is an organisation; the installers are distinguished in the description), which supports option (a): the sub-line parties add nothing.
- Condition: Each sub-line's performing party says something the line does not, or the sub-lines carry no performing party.
- Options: (a, preferred) remove `PerformingParty` from the sub-lines; (b) name the installer (`Person`) in each sub-line's performing party.
- Needs decision: no
- From: parties (context refuted a related reading)

### furniture/16#F10 · Low · The department's own exemption is described as a sale
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme/ExemptionReason` is "The reason for party's exemption from tax, expressed as text", i.e. the party's own status; the text opens with the transaction reason "Sale to a public body", the second half states the status. Money also questioned the code; the world list describes PUBLIC as a buyer status ("A body of the federation, a state or a city buys free of sales tax"), so the code fits, as the contest merges decided. All 55 party-level `ExemptionReasonCode` elements are `PUBLIC` (merge recount).
- Condition: The party's exemption reason text states the party's status without describing a sale.
- Options: (a, preferred) a text such as "Public body: exempt from the state sales tax"; (b) only the code; (c) a separate status code, if the world wants the list to distinguish party and transaction.
- Needs decision: no
- From: money, parties

### furniture/16#F11 · Low · Customs trader number of the department in a domestic work report
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department's customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`) has no use in a report of domestic installation work (section 4.8, IND5). 55 files carry it (merge recount: 36 tender, 16 contest, 3 furniture).
- Condition: The customs trader number is present only in documents with a customs purpose.
- Options: (a, preferred) remove it from this document.
- Needs decision: no
- From: broad, context, parties

### furniture/16#F12 · Low · Hourly price without base quantity
- XPath: `/WorkReport/cac:WorkReportLine/cac:Price/cbc:PriceAmount` = `48`
- Why: `BaseQuantity` is "The quantity at which this price applies". The rate 48 is per hour per installer (14 h × 48 = 672.00), which order and invoice state with `BaseQuantity` 1 HUR (`17-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:BaseQuantity` = `1`); here it is implied by absence (IND6). 12 of 117 `Price` elements with a `PriceAmount` lack it (merge recount, lxml over `world/examples/*/*.xml`).
- Condition: The price states the quantity it applies to (1 HUR).
- Options: (a, preferred) add `BaseQuantity` 1 HUR.
- Needs decision: no
- From: money

### furniture/16#F13 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Hours (merge recalculation): sub-lines 7 h + 7 h = 14 h = `/WorkReport/cac:WorkReportLine/cbc:Quantity` = `14` = `/WorkReport/cac:WorkQuantityTotal/cbc:Quantity` = `14` = the ordered hours in `15-Order.xml`.
- Amounts: 14 × 48 = 672.00 = `/WorkReport/cac:WorkReportLine/cbc:LineExtensionAmount` = `672.00` = `/WorkReport/cac:StatementMonetaryTotal/cbc:LineExtensionAmount` = `672.00`; 672.00 + 24.00 = 696.00 = `/WorkReport/cac:StatementMonetaryTotal/cbc:PayableAmount` = `696.00`; `17-Invoice.xml` bills these figures and refers to this report and its line 1.
- "Six desks assembled and placed" = the six desks of `15-Order.xml`; completion and phase progress 100 %; reported period, line period and phase dates all 2026-04-08 to 2026-04-09; issue date the last day of the work.
- `/WorkReport/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581` and the phase's work order reference resolve to `15-Order.xml`.
- Approver and signatory are the department, consistent with the approval note; codes INSTALL, FURNISH, HUR and AEO (UNCL 7161, collection and recycling) resolve and fit.

## Considered and refuted
- `/WorkReport/cac:AdditionalDocumentReference/cbc:ID` = `BF-PHOTO-26-0408` and `/WorkReport/cac:WorkReportLine/cac:DocumentReference/cbc:ID` = `BF-CHECK-26-0408`: references that resolve to no example — refuted, they are supporting attachments (photos, a checklist), not UBL documents, numbered in the maker's series with the date of the work (from broad, logistics).
- `/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`: unresolved — refuted, a project is not a document (from broad, logistics).
- `/WorkReport/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COMMIT-26-0381`: unresolvable reference — refuted as unresolvable, an internal record of the department (from logistics); its use as a billing reference is F1.
- `/WorkReport/cbc:IssueDate`: no issue time, and a report on the last day of the work — refuted, `IssueTime` is optional and the report may have been issued after the work ended (from broad, logistics); see "Outside this review" for the invoice time.
- `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cac:PerformingParty`: the performing party is the company, not the installer — refuted because `PerformingParty` is a party (organisation) and the installers are distinguished in `WorkItemDescription` (from context); the repetition is F9.
- `/WorkReport/cac:WorkReportLine/cac:ActivityOriginLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`: a company name instead of a place — refuted, it designates the department's building, as in `15-Order.xml` (from logistics, context); the missing address is F8.
- `/WorkReport/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name`: a report issued by Brackenmere signed by the customer — refuted because the signature records the department's approval, consistent with `ApproverParty` (from parties).
- `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: a city department registered at state level — refuted because the level is that of the tax (from parties).
- `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention`: head of procurement and procurement officer — refuted, two functions of the same office (from parties).
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F13 by the merge.
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because name, title and department agree and the desk plausibly handles the relationship (from parties).
- `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F13: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- broad/F1 (Medium, yes), context/F3 (Low, no) → F1: Medium (the element carries a meaning other than its definition) with "Needs decision: no" (moving a reference does not change the story); context's option (a) preferred.
- broad/F2, parties/F1 → F2: "Needs decision" no (parties: yes), as for public bodies in all earlier flows.
- broad/F3, parties/F2, context/F1 → F3: removal preferred.
- broad/F4 (yes), money/F2 (no) → F4: combined, "Needs decision: yes" because whether the charge was agreed is story (as 10#F4 for the discount).
- broad/F5, money/F1, context/F2 → F5: "Needs decision" set to no (all three: yes), as the earlier flows' cost-centre findings.
- money/F3 → F6: preferred option changed to removing the tax totals (the smaller change; money preferred adding the category), both kept.
- money/F4, parties/F6 → F10: combined; the code kept as fitting (contest merges), money's option kept as (c).
- broad/F6, context/F4, parties/F7 → F11: combined; count recounted.

## Outside this review
- `17-Invoice.xml` is issued on 2026-04-09 at 10:10, the last day of the work this report covers; whether the work was finished by then is a timeline question across documents (from logistics).
