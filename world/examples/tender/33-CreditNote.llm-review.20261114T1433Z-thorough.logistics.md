# LLM review: 33-CreditNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/33-CreditNote.xml`, Git blob `fedb04ee2964c2e08e60565d54f4c570247bdfda` (committed)
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

### tender/33#F1 · High · The credited bench is identified as the standard grey; the release was moss green
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: The credit is for one bench of the delivery `CL-DA-26-0215` (`/CreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `CL-DA-26-0215`), whose line says `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` All 40 benches of that delivery are green; the credited one is described as grey.
- Condition: The credited item's variant and colour are those of the delivered bench.
- Options: identify the green variant, as in the corrected despatch advice and invoice (preferred).
- Needs decision: no

### tender/33#F2 · High · Emission factor × base does not give the emission value
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg CO2e; see `25-Catalogue.xml` (F4 of its review). 39 examples across flows carry these values (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: as in 25.
- Needs decision: no

### tender/33#F3 · Medium · Invoice periods on a credit note for one invoice, one of them a bare start date
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-03-31`
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:EndDate` = `2026-04-04`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:InvoicePeriod/cbc:StartDate` = `2026-04-02`
- Why: The header period "associates the Credit Note with Invoicing Periods rather than with a specific Invoice". This credit note is tied to a specific invoice (`/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`) for a one-off delivery; the period given is simply the span from the invoice's date to the credit note's date, not a billing period of anything. The line period ("an invoice period to which this credit note line applies") has only a start date, 2 April, with no end and no explanation: presumably the day the damage was found or the bench arrived, which is an event date, not a period, and is stated nowhere else in the flow.
- Condition: Periods are present only for supplies billed by period; the date of the damage or delivery, if wanted, is carried where a date of that meaning belongs (e.g. the issue date of the referenced damage report).
- Options: (a) preferred: remove both periods and give `cac:DocumentReference` PWD-DMG-26-0081 an `cbc:IssueDate`; (b) keep nothing but the billing reference.
- Needs decision: no

### tender/33#F4 · Low · References that do not say what they refer to, none resolvable in the flow
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:DocumentReference/cbc:ID` = `PWD-DMG-26-0081`
- XPath: `/CreditNote/cac:WorkReportDocumentReference/cbc:ID` = `VI-WR-26-0080`
- XPath: `/CreditNote/cac:PurchaseReference/cbc:ID` = `PARK-HB`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PurchaseReference/cbc:ID` = `PARK-HB-B17`
- Why: The line's document reference ("a document associated with this credit note line") has only an ID; from the prefix it is the department's damage report that the despatch note asked for, but nothing says so. The work report (a report of whose work, when? the bench was not installed, see line 2) has no date or description and `cac:WorkReportLineReference/cbc:LineID` 1 points into it. The purchase references ("a reference to an object, such as a subscription number, telephone number, meter, vehicle, person, etc.") carry bare IDs: presumably Harbour park and bench position 17 there, which the reader has to guess; no other example uses them (grep for `PARK-HB` over `world/examples/**/*.xml`: this example only), and the bench itself has no serial number through which it could be identified (see 29, F7).
- Condition: Each reference states the kind of thing it refers to (document type and date; a description of the object).
- Options: add `cbc:DocumentType` "Damage report" with issue date; a document type for the work report; `cbc:Description` on the purchase references (preferred).
- Needs decision: no

### tender/33#F5 · Low · Programme code differs from the procurement documents
- XPath: `/CreditNote/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: As in `26-Order.xml` (F7): the programme is PARKS-26 in the procurement documents (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`).
- Condition: One code for the programme throughout the flow.
- Options: as in 26.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no failures.
- `cac:BillingReference` VI-INV-26-0221 is the invoice of 31 March; `cac:DeliveryNoteDocumentReference` CL-DA-26-0215 is the despatch advice of the same goods, the document under which the note asked to "report any damage"; both exist and are of the kind the elements mean.
- Issue date 4 April follows invoice (31 March), import (31 March) and the line's date 2 April; it precedes the debit note (6 April) and the reminder (5 May), which sets off exactly this credit note's payable amount (515.20).
- Quantities: one bench at 499 (the invoiced price) and one installation at 18: the damaged bench and its installation; `cbc:LineCountNumeric` 2 = two lines. 499.00 + 18.00 = 517.00; − 1.80 = 515.20.
- CreditNoteTypeCode 381 = credit note (UNCL 1001).

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount`: `180.00` under a line of 499.00 — not followed up in this lens (amounts); a sub-line may detail a part ("Side frames of the bench") without summing to the line.
- `/CreditNote/cac:CreditNoteLine[2]/cbc:CreditedQuantity`: an installation credited that (per the review of 32, F1) should not have been invoiced yet — refuted as a finding here: given the invoice as issued, crediting the installation of the bench that was not installed is consistent.
- `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: see the review of `26-Order.xml` (F8).

## Outside this review
- No replacement bench is despatched or invoiced in the flow; the release therefore ends with 39 benches, while the reminder and remittance settle on that basis.
