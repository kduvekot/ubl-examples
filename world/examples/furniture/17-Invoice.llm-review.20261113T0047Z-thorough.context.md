# LLM review: 17-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/17#F1 · Medium · The work report referenced as a billing document
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `BF-DOC-26-0582`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:WorkReportLineReference/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0582`
- Why: `InvoiceLine/BillingReference` is "A reference to a billing document associated with this invoice line". `BF-DOC-26-0582` is the work report `16-WorkReport.xml`, not a billing document; the same line already refers to it by the dedicated `WorkReportLineReference` ("A reference to a work report line associated with this invoice line"), and the header by `WorkReportDocumentReference`. The billing reference uses an element for a kind of document it is not meant for and repeats a reference that is already there.
- Condition: the line's `BillingReference` refers to a billing document, or is absent; the work report is referenced by the work-report references only.
- Options: (a) remove the line's `BillingReference` (preferred); (b) none other seen.
- Needs decision: no

### furniture/17#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/17#F3 · Low · Office project invoiced to the parks renewal programme
- XPath: `/Invoice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Invoice/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `PWD-PARKS-26-AP`
- XPath: `/Invoice/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole", and the buyer's routing reference also points to the parks programme. The invoice itself places the supply in the office project, for office desks and their installation in the department's offices. A parks renewal programme paying for a new office does not fit the situation unless the story says so. Same cost centre in `15-Order.xml` and `16-WorkReport.xml`.
- Condition: cost centre and buyer reference fit the office project, consistently in 15, 16 and 17, or the story says why the parks programme pays.
- Options: (a) an office or facilities cost centre and routing code (preferred); (b) state that the office belongs to the parks programme.
- Needs decision: yes

### furniture/17#F4 · Low · Customs trader number of the customer in a domestic invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`) has no purpose in a domestic invoice for desks and installation (section 4.8). Also in 15 and 16.
- Condition: present only in documents with a customs purpose.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `OrderReference` resolves to `15-Order.xml`; `WorkReportDocumentReference` and `WorkReportLineReference` (line 1) to `16-WorkReport.xml`; invoiced quantities and prices equal the order and the work report.
- `InvoiceLine[2]/InvoicePeriod` 2026-04-08 to 2026-04-09 equals the reported period of the work.
- `SupplyTypeCode` `GOODS` for the desks and `SERVICES` for the installation fit the lines.
- `PaymentTerms` with `PaymentMeansID` = `1` refers to the one payment means.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[2]/cbc:Note` = `Two installers, seven hours.`: suspected to repeat the work report — refuted because it explains the 14 hours to a reader of the invoice who does not open the report.
- `/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`: a routing reference of the buyer — fits the element ("used for internal routing of the document"); only its code's link to the parks programme is part of F3.
