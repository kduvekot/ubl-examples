# LLM review: 16-WorkReport.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/16#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/WorkReport/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/16#F2 · Low · Work for the office project charged to the parks renewal programme
- XPath: `/WorkReport/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/WorkReport/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- XPath: `/WorkReport/cac:WorkReportLine/cac:WorkPhaseReference/cbc:WorkPhase` = `Furnishing: the new office is furnished`
- Why: `AccountingCost` is "An accounting cost centre or account to which this Work Report is charged". In the same document the work belongs to the office project and its furnishing phase; a parks renewal programme as the account for furnishing a new office does not fit, unless the office is part of that programme, which nothing says. The same cost centre is in `15-Order.xml` and `17-Invoice.xml`.
- Condition: the cost centre fits the office project, consistently in 15, 16 and 17, or the story says why the parks programme pays for the office.
- Options: (a) an office or facilities cost centre (preferred); (b) state that the office belongs to the parks programme.
- Needs decision: yes

### furniture/16#F3 · Low · A budget commitment given as a billing reference
- XPath: `/WorkReport/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COMMIT-26-0381`
- Why: `WorkReport/BillingReference` is "A reference to a related billing document". `PWD-COMMIT-26-0381` is, by its numbering, a commitment of the public works department (a budget commitment or encumbrance), the buyer's internal financial document, not a billing document (invoice, credit note, self-billing). If the commitment number has to be quoted (as public buyers often require), it is an additional document reference of the work report or an `OrderReference`-like reference, not a billing reference. The invoice `17-Invoice.xml` does not quote the commitment at all.
- Condition: `BillingReference` refers to a billing document, or is absent; a commitment number, if needed, is carried as an additional document reference with a document type, and also on the invoice if the buyer requires it there.
- Options: (a) move it to `AdditionalDocumentReference` with a document type "budget commitment" and add it to the invoice (preferred: a public buyer needs it on the invoice more than on the report); (b) remove it.
- Needs decision: no

### furniture/16#F4 · Low · Customs trader number of the buyer in a domestic work report
- XPath: `/WorkReport/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`) has no purpose in a report of installation hours on the department's own premises (section 4.8). Also in 15 and 17.
- Condition: present only in documents with a customs purpose.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- 14 hours in total = two sub lines of 7 hours = `WorkQuantityTotal`; 14 × 48 = 672; plus the 24.00 disposal charge = 696 payable.
- `OrderReference` and `WorkOrderDocumentReference` resolve to `15-Order.xml`; the ordered 14 hours of installation are reported.
- `ReportedPeriod`, line period and work phase dates (2026-04-08 to 2026-04-09) agree, and the issue date 2026-04-09 is the last day of work; `CompletionPercent` and `ProgressPercent` 100 fit a finished phase.
- `ApproverParty` = the department and its signature, with the note "Approved by the department's facilities officer.": the buyer approving the report fits the element.

## Considered and refuted
- `/WorkReport/cac:WorkReportLine/cac:SubWorkReportLine[1]/cac:PerformingParty`: the performing party of each installer's line is the company, not the installer — refuted because `PerformingParty` is a party (organisation) and the installers are distinguished in `WorkItemDescription`.
- `/WorkReport/cac:WorkReportLine/cac:ActivityOriginLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`: the location where the work was performed, as defined.
