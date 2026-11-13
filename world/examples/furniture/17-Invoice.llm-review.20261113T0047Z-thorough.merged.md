# LLM review: 17-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/17-Invoice.xml`, Git blob `66ce2e15ac8d6433692b369df50c1ad798bd1603` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### furniture/17#F1 · Medium · The work report referenced as a billing document
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `BF-DOC-26-0582`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:WorkReportLineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0582`
- Why: `InvoiceLine/BillingReference` is "A reference to a billing document associated with this invoice line". `BF-DOC-26-0582` is the work report `16-WorkReport.xml`, not a billing document; the same line already refers to it through the dedicated `WorkReportLineReference` ("A reference to a work report line associated with this invoice line"), and the header through `WorkReportDocumentReference`. The element is used for a kind of document it is not meant for, repeating a reference that is already there.
- Condition: Invoice line 2's `BillingReference`, if any, refers to a billing document; the work report is referenced by the work-report references only.
- Options: (a, preferred) remove the line's `BillingReference`.
- Needs decision: no
- From: broad, context

### furniture/17#F2 · Medium · Public works department described as a company in the commercial register, with a liquidation status
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `8411`
- Why: The department is part of the city administration (ISIC 8411; exempt as a public body). Its legal entity names the commercial register (world list: COMMERCIAL = "A register of businesses.") and carries a liquidation status ("A code signifying the party's liquidation status"); a public department is not a business in a commercial register and cannot be in liquidation. Same description in 15, 16 and 17.
- Condition: The department's legal entity describes a public body: no liquidation status, and no commercial-register type (a register of public bodies, or none).
- Options: (a, preferred) drop `CompanyLiquidationStatusCode` and the COMMERCIAL registration scheme, keeping registration name and identifier, or use a world register of public bodies; (b) the legal entity of the City of Lumeport, which would change who the party is.
- Needs decision: no
- From: broad (Medium, no), parties (Medium, yes)

### furniture/17#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/17#F4 · Low · Packaging-disposal charge billed although the order does not contain it
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Packaging disposal`
- XPath: `/Invoice/cac:AllowanceCharge/cbc:Amount` = `24.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `24.00`
- Why: The invoice charges 24.00 for packaging disposal on top of the ordered goods and hours. The order it references (`/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581`) contains no such charge (`15-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00`, against `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `5976.00`); the charge appears otherwise only in the seller's work report `16-WorkReport.xml`, which the department signed. Nothing shows the department agreed it before it was billed, which a public buyer's invoice check would look for (own knowledge). Whether it was agreed is story.
- Condition: The charge can be traced to the order or another agreement in the flow, or it is not billed.
- Options: (a, preferred) add the charge to `15-Order.xml` so the invoice matches the order; (b) rely on the approved work report and say so; (c) drop the charge from 16 and 17.
- Needs decision: yes
- From: broad (yes), money (no)

### furniture/17#F5 · Low · Office project invoiced to the parks renewal programme
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `PWD-PARKS-26-AP`
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Invoice as a whole", and the buyer's routing code also points to the parks programme. The invoice itself places the supply in the office project (six office desks and their installation). The parks renewal programme carries the park benches in the tender flow (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`); paying for a new office from it is possible, but nothing in the flow says so. Same cost centre in `15-Order.xml` and `16-WorkReport.xml`.
- Condition: Cost centre and buyer routing code fit the office project, consistently in 15, 16 and 17, or the flow states why the parks programme pays.
- Options: (a, preferred) a cost centre, text and accounts-payable routing code for the office project; (b) a note that the new office belongs to the parks programme.
- Needs decision: no
- From: broad, money, context (all three: yes)

### furniture/17#F6 · Low · The accounting customer is addressed to procurement while the buyer reference names accounts payable
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Procurement officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`
- Why: The accounting customer is the party that receives and settles the invoice. Its contact and address attention are the procurement office and the head of procurement, copied from the ordering role (`15-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`), while the invoice routes itself to "Accounts payable, public works" through the buyer-assigned reference. The contact does not fit the role it is given and differs from the routing next to it.
- Condition: The contact (and the address attention, if kept) of the accounting customer is the accounts-payable function the buyer reference names.
- Options: (a, preferred) an accounts-payable contact for the department in the accounting customer role; (b) keep procurement and drop the attention line, if the world's public bodies route invoices through procurement, and say so in the buyer reference.
- Needs decision: no
- From: parties

### furniture/17#F7 · Low · The department's own exemption is described as a sale
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme/ExemptionReason` is "The reason for party's exemption from tax, expressed as text", i.e. the party's own status; the text opens with the transaction reason used on the lines, the charge and the subtotal of this invoice (`/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Sale to a public body`), the second half states the status. Money also questioned the code; the world list describes PUBLIC as a buyer status ("A body of the federation, a state or a city buys free of sales tax"), so the code fits both uses, as the contest merges decided. All 55 party-level `ExemptionReasonCode` elements are `PUBLIC` (merge recount).
- Condition: The party's exemption reason text states the party's status without describing a sale.
- Options: (a, preferred) a text such as "Public body: exempt from the state sales tax"; (b) only the code; (c) a separate status code, if the world wants the list to distinguish party and transaction.
- Needs decision: no
- From: money, parties

### furniture/17#F8 · Low · Customs trader number of the customer in a domestic invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`) has no purpose in a domestic invoice for desks and their installation (section 4.8, IND5). 55 files carry it (merge recount: 36 tender, 16 contest, 3 furniture).
- Condition: Present only in documents with a customs purpose.
- Options: (a, preferred) remove it from this document.
- Needs decision: no
- From: broad, context, parties

### furniture/17#F9 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Arithmetic (merge recalculation): 6 × 880 = 5280.00 and 14 × 48 = 672.00; `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `5952.00`; + charge 24.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `5976.00` = `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `5976.00`; tax 0.00; tax inclusive and payable 5976.00.
- Penalty (merge recalculation): 1.5 % × 5976.00 = 89.64 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `89.64`, for one month from 2026-05-10, the day after the due date; due date 2026-04-09 + 30 days = 2026-05-09 = `/Invoice/cbc:DueDate` = `2026-05-09`.
- Tax: exempt STT with reason `PUBLIC` on both lines, the charge and the subtotal; supply types GOODS (desks) and SERVICES (installation) fit; prices state their base quantity (1 EA, 1 HUR).
- Against order and work report: prices and quantities equal `15-Order.xml`; line 2 and the charge equal `16-WorkReport.xml:/WorkReport/cac:StatementMonetaryTotal/cbc:PayableAmount` = `696.00` (672.00 + 24.00); line 2's invoice period 2026-04-08 to 2026-04-09 equals the reported period; "Two installers, seven hours" agrees with the sub-lines.
- References: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581` → `15-Order.xml`; `/Invoice/cac:WorkReportDocumentReference/cbc:ID` = `BF-DOC-26-0582` → `16-WorkReport.xml`, whose line 1 exists.
- Payment: `RF52BFINV260583` passes ISO 11649 and is built by the creditor from the invoice number; `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice BF-INV-26-0583` names the document correctly; the account is the seller's, as in `09-Invoice.xml`.
- Item dimensions (1600 × 800 × 740 mm) and identifiers agree with the order; GTIN and GLN check digits pass.

## Considered and refuted
- `/Invoice/cbc:IssueTime` = `10:10:00`: an invoice issued before the invoiced work ended (work to 2026-04-09, invoiced at 10:10 that day) — refuted because the 14 hours span two days, so the second day may have ended early, and the work report has no issue time the invoice would precede (from logistics); kept under "Outside this review" as a timeline question (broad, money).
- `/Invoice/cac:InvoiceLine[1]`: an invoice for desks without a delivery date — refuted because the desks were delivered and placed during the referenced work (from logistics).
- `/Invoice/cac:InvoiceLine[2]/cbc:Note` = `Two installers, seven hours.`: repeats the work report — refuted because it explains the 14 hours to a reader who does not open the report (from context).
- `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`: fits the element ("used for internal routing of the document"); only its code's link to the parks programme is part of F5 (from context).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F9 by the merge.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact as accounting supplier — refuted because name, title and department agree and the desk plausibly handles the relationship (from parties).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID`: the Marrowdale branch could contradict the account — refuted because the account number contains branch 387120 (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: a city department registered at state level — refuted because the level is that of the tax (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention`: head of procurement and procurement officer — refuted as a contradiction between the two (same office) (from parties); that both are the wrong function for an accounting customer is F6.

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F9: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- broad/F2, parties/F1 → F2: "Needs decision" no (parties: yes), as for public bodies in all earlier flows.
- broad/F3, parties/F2, context/F2 → F3: removal preferred.
- broad/F4 (yes), money/F3 (no) → F4: combined, "Needs decision: yes", as 16#F4.
- broad/F5, money/F1, context/F3 → F5: "Needs decision" set to no (all three: yes), as the earlier flows' cost-centre findings; the routing code added from money and context.
- money/F2, parties/F4 → F7: combined; the code kept as fitting (contest merges), money's option kept as (c).
- broad/F6, context/F4, parties/F5 → F8: combined; count recounted.

## Outside this review
- The invoice is issued 2026-04-09 at 10:10 for installation work that runs until 2026-04-09 (seven hours per installer over two days) and refers to a work report of the same day that is already approved; whether the work was complete by then is a timeline question across documents (from broad, money; logistics refuted it as a finding).
