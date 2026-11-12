# LLM review: 03-ProofOfReexportationReminder.xml

Flow: carnet (CARNET-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/carnet/03-ProofOfReexportationReminder.xml`, Git blob `a4b75fb8a0fa66ce587c269390e36886f30cf151` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### carnet/03#F1 · High · Duties of 1,300 coral are more than three times the value of the goods
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Amount` = `1300.000`
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Note` = `Duties and import consumption tax of 1,300 coral fall due if no proof arrives within 30 days.`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99800`
- Why: PaymentTerms/Amount is "The monetary amount covered by these payment terms", here the import duties and import consumption tax that the island would claim on the carnet goods. Those taxes are a percentage of the customs value of the goods, which the carnet declares as 99,800 ferra for the two benches. At the rates the examples use, 1 XUF = 0.01 XBL (`tender/32-Invoice.xml:/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`, and `road/05-ExportCustomsDeclaration.xml` declares 4,790,400 XUF that `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00` lume) and 1 XBL = 0.4 XLC (`packaging/09-PurchaseReceipt.xml:/PurchaseReceipt/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`). The goods are therefore worth 99,800 × 0.01 × 0.4 = 399.20 coral, and 1,300 coral is 326 % of that. No combination of a duty rate and a consumption tax that the world uses elsewhere (the highest tax rate in the examples is 20 %) gets near it; the amount looks as if it was computed in another currency or on another base. Nothing in the document explains it (no tax rate, no penalty).
- Condition: the amount in `PaymentTerms/Amount` and in the note can be derived from the customs value of the carnet goods, converted to coral, at the duty and tax rates of Lisavu (or the note says what else it includes, e.g. a penalty).
- Options: (a) preferred: recompute the claim from 399.20 XLC with the island's duty and consumption tax rates and use the same figure in Amount and Note; (b) if the claim is meant to be higher (e.g. includes a penalty under the carnet rules), say so in the note.
- Needs decision: no

### carnet/03#F2 · Medium · Duties fall due before the carnet's re-export deadline
- XPath: `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-09-22`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:GoodsItemPassportCounterfoil[1]/cbc:FinalReexportationDate` = `2026-11-21`
- XPath: `01-GoodsItemPassport.xml:/GoodsItemPassport/cac:ValidityPeriod/cbc:EndDate` = `2027-05-25`
- Why: the payment terms say the duties "fall due if no proof arrives within 30 days" and set the due date to 2026-09-22. Under temporary admission with an ATA carnet, duties become payable only when the goods have not been re-exported by the date set for re-exportation; the carnet sets that date to 2026-11-21 (and its own note says "to come back within six months"). On 2026-09-22 the goods could still lawfully be on the island, so no duty can be due then. In addition, the claim procedure of the ATA and Istanbul Conventions (own knowledge, article not checked) gives the guaranteeing association six months from the claim to provide proof of re-exportation, not 30 days. The amount and date of the claim therefore contradict the carnet the reminder is about.
- Condition: `PaymentTerms/PaymentDueDate` is not earlier than the re-export deadline of the carnet plus the period the guarantor has to furnish proof, or the document states why the duties fall due earlier.
- Options: (a) preferred: move the claim and the reminder after the re-export deadline (this changes the timeline of the flow); (b) keep the dates and explain in the note why the island claims earlier (e.g. a shorter deadline set by the island's customs on the importation counterfoil, which the carnet would then have to carry).
- Needs decision: yes

## Checked and consistent
- `/ProofOfReexportationReminder/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-09-22` is 30 days after `/ProofOfReexportationReminder/cbc:IssueDate` = `2026-08-23`, as the note says.
- The amount in the note (1,300 coral) and in `cbc:Amount` agree, and the currency (XLC, coral) is the importing country's, which is the right currency for duties claimed by the island's customs. XLC amounts carry three decimals as in 189 of 202 XLC amounts in the examples (counted over `*.xml` with `grep -o 'currencyID="XLC">[0-9.]*<'`).
- The PaymentTerms are used as the UBL definition intends: "used for generating a subsequent invoice in case no proof of re-exportation can be provided"; the proof arrives on 2026-08-28 (`04-ProofOfReexportation.xml:/ProofOfReexportation/cbc:IssueDate` = `2026-08-28`), before the due date, so no follow-up invoice is needed in the flow.
- The reminder refers to the request (`/ProofOfReexportationReminder/cac:ProofOfReexportationRequestDocumentReference/cbc:ID` = `SCC-DOC-26-0726`), which exists as `02-ProofOfReexportationRequest.xml`.
