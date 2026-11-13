# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/22#F1 · High · "30 days net" from shipment, but the balance falls due 45 days after shipment
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:InstallmentDueDate` = `2026-06-28`
- XPath: `/Invoice/cbc:DueDate` = `2026-06-28`
- Why: The balance terms count from the "Date of shipment as evidenced by the transport document(s)" (UNCL 2475 code 81). The transport document is the bill of lading of 2026-05-14 (`14-BillOfLading.xml:/BillOfLading/cbc:IssueDate` = `2026-05-14`), and the invoice itself is of that day. 30 days net from 2026-05-14 is 2026-06-13; the stated due date 2026-06-28 is 45 days after shipment. The free text and the structured due date contradict each other. (Bayforth's invoice in the same flow, `18-Invoice.xml`, uses the same note and its due date is exactly 30 days after issue.)
- Condition: The note, the reference event and the due dates give the same due date.
- Options: (a) preferred: due dates 2026-06-13 with the penalty period from 2026-06-14, if the terms are 30 days from shipment; (b) keep 2026-06-28 and change the note to "45 days net" or the reference event to one that falls on 2026-05-29.
- Needs decision: no

### sea/22#F2 · High · Exchange rate and validity of the payment terms dated after the invoice was issued
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:Date` = `2026-05-18`
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ValidityPeriod/cbc:StartDate` = `2026-05-18`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-14`
- XPath: `/Invoice/cac:PaymentAlternativeExchangeRate/cbc:Date` = `2026-05-14`
- Why: `ExchangeRate/Date` is "The date on which the exchange rate was established". An invoice issued on 2026-05-14 cannot state a rate established on 2026-05-18; the invoice's own payment alternative exchange rate (the same XBL→XLC rate 0.4) is dated 2026-05-14. The payment terms' validity also starts on 2026-05-18, four days after issue, so on the issue date the terms that set the balance due would not yet be valid. Nothing in the invoice explains why the terms should start later.
- Condition: No date in the invoice that records something established or valid at issue lies after the issue date; the two statements of the same rate carry consistent dates.
- Options: (a) preferred: date the payment terms' rate and validity on or before 2026-05-14; (b) drop the payment terms' exchange rate, since `PaymentAlternativeExchangeRate` already gives the rate for the alternative payable amount.
- Needs decision: no

### sea/22#F3 · Medium · The factor's collection account given as the financing (line of credit) account
- XPath: `/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:FinancingFinancialAccount/cbc:ID` = `XB51BLUM38020502304038`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB51BLUM38020502304038`
- Why: `FinancingFinancialAccount` is "An internal bank account used by the bank or its first agent to manage the line of credit granted to the financing requester". The value is Harbourline's current account (type CACC) at the Bank of Lumeport, the same account the buyer is told to pay into as payee account. A collection current account into which third parties pay is not the internal account on which the factor manages the funding it granted to Lumeway. The element carries a valid account, but not one with the meaning of the definition.
- Condition: The financing account is the account on which the financing granted to Lumeway is managed (e.g. Lumeway's factoring client account at Harbourline), or it is absent.
- Options: (a) preferred: remove it; the payee account and the contract reference already say where to pay and under which agreement; (b) give the factor's internal client account for Lumeway, if the story needs it, with an account type that fits.
- Needs decision: no

### sea/22#F4 · Low · Catalogue and product-passport data copied into the invoice line
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: The invoice line of the bench carries the whole catalogue item: search keywords ("assigned by the seller party" for searching), sales conditions, load test method, colour options with importance codes, emissions, circularity profile and product documentation. An invoice identifies what is billed and on what terms; the buyer's accounts payable does nothing with the search keywords, the load test or the maintenance frequency. This is master data copied from the catalogue (`02-Catalogue.xml`); the side-frame line does without it.
- Condition: The invoice item carries what identifies and classifies the billed item (and data with a billing or tax reason).
- Options: (a) preferred: reduce the bench's item to identification, name, description, classification and origin.
- Needs decision: no

## Checked and consistent
- Totals: lines 49920.00 + 768.00 = 50688.00; charges 2950.00 + 140.00 = 3090.00; tax-exclusive 53778.00; prepaid 10000.00; payable 43778.00; alternative payable 43778.00 × 0.4 = 17511.200 XLC.
- Payment percentages: 10000 / 53778 = 18.59 %, 43778 / 53778 = 81.41 %; penalty 1.5 % × 43778.00 = 656.67.
- The deposit (`VT-DEP-26-0412`, paid 2026-05-08, received 2026-05-09) matches its terms (due 2026-05-09, after the order response of 2026-05-08, `06-OrderResponse.xml`).
- Freight 2950.00 and insurance 140.00 equal the amounts Bayforth bills Lumeway for the same shipment (`18-Invoice.xml`), as CIF terms require the seller to pay them.
- The factoring note, payee party, payee account name, trade financing and clause agree: the receivable is assigned to Harbourline and only payment to its account discharges the buyer.

## Considered and refuted
- `/Invoice/cac:AllowanceCharge[2]/cbc:AllowanceChargeReasonCode`: a charge coded from UNCL 5189 while the freight charge uses UNCL 7161 suspected as a code from another element's list — refuted because UNCL 5189 is the "allowance or charge identification" list and code 96 "Insurance" ("The cost of insuring the goods") is in it, so the code is valid for a charge; the two lists side by side are a style question.
- `/Invoice/cac:PaymentMeans/cbc:ServiceLevelCode`: "non-urgent payment" suspected to contradict the real-time channel RTNS — refuted because the service level concerns the priority of execution requested from the bank, not the settlement mechanism.
