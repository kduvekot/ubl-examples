# LLM review: 17-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/17-Invoice.xml`, Git blob `66ce2e15ac8d6433692b369df50c1ad798bd1603` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### furniture/17#F1 · Medium · Work report cited as a billing document
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `BF-DOC-26-0582`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:WorkReportLineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0582`
- Why: `BillingReference` on an invoice line is "A reference to a billing document associated with this invoice line". `BF-DOC-26-0582` is the work report `16-WorkReport.xml`, not a billing document, and the line already references it through the dedicated `WorkReportLineReference` (and the invoice through `WorkReportDocumentReference`).
- Condition: Invoice line 2's billing reference, if any, references a billing document; the work report is referenced only through the work report references.
- Options: (a, preferred) remove the line's `BillingReference`.
- Needs decision: no

### furniture/17#F2 · Medium · Public works department described as a company in the commercial register
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Lumeport Public Works Department is a department of a public authority (ISIC 8411, exempt as a public body). Its legal entity says it is registered in the commercial register (`CorporateRegistrationTypeCode` COMMERCIAL, the federal business register) and gives it a liquidation status ("A code signifying the party's liquidation status"). A public department is not a company in a commercial register and cannot be in liquidation; the description does not fit the kind of party. The same description is used in all three examples where the department appears (15, 16, 17).
- Condition: The department's legal entity describes a public body: no liquidation status, and a registration scheme (if any) that registers public bodies, not the commercial register.
- Options: (a, preferred) the legal entity of the city of Lumeport (the legal person the department belongs to) with a public-body register or none, without `CompanyLiquidationStatusCode`; (b) drop `PartyLegalEntity` and keep the party identification.
- Needs decision: no

### furniture/17#F3 · Medium · Language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/17#F4 · Low · Packaging disposal charge billed without an order
- XPath: `/Invoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Packaging disposal`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `24.00`
- Why: The invoice bills a 24.00 packaging disposal charge that the order `15-Order.xml` (referenced by this invoice) does not contain; it comes only from the work report `16-WorkReport.xml`. For a public buyer, billing a charge outside the order is exactly what the order reference is meant to prevent.
- Condition: The charge is part of the order (or a stated contract), or it is not billed.
- Options: (a, preferred) add it to the order 15; (b) remove it from 16 and 17.
- Needs decision: yes

### furniture/17#F5 · Low · Office furniture charged to the parks renewal programme
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: The order is for office desks and their installation; the work report places the work in project `PWD-PLAN-OFFICE-26` and phase "Furnishing: the new office is furnished". The buyer's accounting cost is the "Parks renewal programme 2026" (`PWD-PARKS-26`), the same in order 15, work report 16 and invoice 17. Furnishing an office from a parks programme is at least unexplained.
- Condition: The buyer's accounting cost centre matches the purpose of the purchase (the new office), or the documents say why the parks programme pays for it.
- Options: (a, preferred) a cost code and text for the office project (e.g. matching `PWD-PLAN-OFFICE-26`); (b) a note that the new office belongs to the parks programme.
- Needs decision: yes

### furniture/17#F6 · Low · Customs trader number of the public works department in a domestic purchase
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department's `AdditionalPartyIdentification` is its customs trader number. Furniture made in Bayvarra is bought, delivered and installed in Bayvarra; no customs procedure is involved, so the identifier is master data the document does nothing with (IND5).
- Condition: The customs trader number appears only in documents that involve a customs procedure.
- Options: (a, preferred) remove it from this document.
- Needs decision: no

## Checked and consistent
- 5 280 + 672 = 5 952 = line extension; + charge 24 = 5 976 = tax exclusive = tax inclusive = payable; taxable 5 976 includes the charge, which carries the same exempt category.
- `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `89.64`: 1.5 % × 5 976 = 89.64; due 2026-05-09 = 30 days after 2026-04-09; penalty period starts the day after.
- Line 2: 14 h × 48 = 672, invoice period 2026-04-08 to 2026-04-09 = the reported period of 16; note "Two installers, seven hours" matches its sub-lines.
- RF `RF52BFINV260583` and the IBAN-like payee account pass their check digits; the payee account is the same as in `09-Invoice.xml`.
- References: order `LPWD-PO-26-0581` → `15-Order.xml`, work report `BF-DOC-26-0582` → `16-WorkReport.xml`.

## Outside this review
- Timeline: the invoice is issued on 2026-04-09 at 10:10, the last day of the installation period 2026-04-08 to 2026-04-09, and refers to a work report of 2026-04-09 (no time) that is already approved; whether 14 hours of work over two days were complete by then is a cross-document timeline question.
