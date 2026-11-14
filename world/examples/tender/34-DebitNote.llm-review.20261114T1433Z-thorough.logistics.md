# LLM review: 34-DebitNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/34-DebitNote.xml`, Git blob `b6bf3671341fe2437750245b0f5de26efdc18dc0` (committed)
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

### tender/34#F1 · Medium · A penalty for three days' delay without any of the dates it rests on
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity` = `3`
- XPath: `/DebitNote/cac:DebitNoteLine/cbc:Note` = `3 days at 0.5 % of the installation price of the release.`
- XPath: `/DebitNote/cbc:Note` = `Penalty for late installation under the contract's clause PEN-1.`
- Why: The document claims a penalty per day late, so its purpose depends on a due date and a completion date. Neither is in the debit note (no period on document or line), and neither can be taken from the documents it refers to: the order `LPWD-PO-26-0212` states no delivery or installation date and does not order the installation at all, the order response promises none, and the invoice `VI-INV-26-0221` had already billed the installation with a tax point of `32-Invoice.xml:/Invoice/cbc:TaxPointDate` = `2026-03-31`, i.e. as performed. The only candidate due date in the flow is the procedure's requested delivery date (`03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate` = `2026-04-02`); three days from it end on 5 April, the day before this note, but that is a reconstruction. The receiver cannot verify which three days are charged (and which one is waived by the allowance "One day waived").
- Condition: The debit note states the period of delay (due date and date of completion), and these agree with a date fixed in the order or contract documents of the release.
- Options: (a) preferred: an `cac:InvoicePeriod` on the line (e.g. 2026-04-03 to 2026-04-05) with the due date in the note, after the order has been given a delivery date (see 26, F5); (b) dates in the note only.
- Needs decision: no

### tender/34#F2 · Medium · The document number is the buyer's, the issuing role is the seller's
- XPath: `/DebitNote/cbc:ID` = `LPWD-DOC-26-0223`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: The ID is "an identifier for this document, assigned by the sender". `LPWD-DOC-26-…` is the numbering series of the Lumeport Public Works Department (its notices, notifications and the contract, …0187 to …0210), and the content is the department's claim against the seller ("The department's penalty", as `35-Reminder.xml` calls it). In UBL a debit note is issued by the accounting supplier to the accounting customer, here Valdara to the department; Valdara's documents are numbered VI-…. Either the sender is the department, and then the parties are in the roles of the invoice rather than of this document, or the sender is Valdara, and then the number is not one it assigns. (Which party should be in which role is for the parties and money lenses; the identifier cannot be right for the roles as they stand.)
- Condition: The document number belongs to the series of the party in the issuing role.
- Options: (a) preferred: make the department the issuing party of its own claim (supplier role of this debit note, or another document type suited to a buyer's claim) and keep the number; (b) keep the roles and let Valdara issue a credit note for the penalty under a VI number. This changes who issues what.
- Needs decision: yes

## Checked and consistent
- No identifiers with check digits outside the parties (`check_ids.py` reports no failures).
- `cac:OrderReference` LPWD-PO-26-0212, `cac:BillingReference` VI-INV-26-0221 and `cac:ContractDocumentReference` PWD-2026-PARKS exist and are of the kinds named. Clause PEN-1 exists in the call for tenders and the contract (`24-TenderContract.xml`: "0.5 % per day late, at most 10 %").
- Arithmetic against the clause: installation of the release 720.00 (invoice line 2); 0.5 % = 3.60 per day; 3 days = 10.80; one day waived −3.60 = 7.20; less withholding 0.72 = 6.48, the amount set off in 35 and 36. 10.80 is below the cap of 10 % (72.00).
- Issue date 6 April follows the invoice (31 March) and the credit note (4 April).
- Unit DAY for the debited quantity fits a per-day penalty; AllowanceChargeReasonCode 64 is in UNCL 5189.

## Considered and refuted
- `/DebitNote/cac:DebitNoteLine/cbc:DebitedQuantity`: a quantity of days in an element for a quantity of items — refuted: the debited "item" is the penalty per day, so days are its quantity.
- `/DebitNote/cac:ContractDocumentReference/cbc:ID`: contract number equal to the file number — refuted: consistent with 21–24, 26 and 32.

## Outside this review
- Whether the installation was in fact finished on 5 April, and by whom (Saltmere Engineering as subcontractor), is shown by no document of the flow.
