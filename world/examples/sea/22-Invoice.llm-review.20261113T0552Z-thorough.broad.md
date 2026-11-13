# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/22#F1 · High · Due date does not follow "30 days net" from the shipment date
- XPath: `/Invoice/cbc:DueDate` = `2026-06-28`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:InstallmentDueDate` = `2026-06-28`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:IssueDate` = `2026-05-14`
- Why: The balance terms run from event 81, "Date of shipment as evidenced by the transport document(s)". The bill of lading is dated 2026-05-14 and the ship sailed that day (`13-TransportationStatus.xml`), so 30 days net gives 2026-06-13. The stated due date 2026-06-28 is 45 days after shipment (and 45 days after the invoice date); no event of the flow lies 30 days before it (that would be 2026-05-29). Terms text, reference event and due date contradict each other. The same due date is carried into `25-Statement.xml`.
- Condition: Due date and instalment due date equal the reference event's date plus the stated net period.
- Options: (a) change the note to "45 days net" (or the event to one 30 days before 06-28); (b) set the due date to 2026-06-13 and follow it through the statement, reminders and remittance. Preferred (a) if the later documents' timing is to stay.
- Needs decision: no

### sea/22#F2 · High · Exchange rate of the payment terms dated after the invoice
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:Date` = `2026-05-18`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-14`
- XPath: `/Invoice/cac:PaymentAlternativeExchangeRate/cbc:Date` = `2026-05-14`
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ValidityPeriod/cbc:StartDate` = `2026-05-18`
- Why: ExchangeRate/Date is "The date on which the exchange rate was established." An invoice issued on 2026-05-14 cannot carry a rate established on 2026-05-18; the document's own payment-alternative rate (same 0.4) is dated 2026-05-14. The terms' validity also only starts on 05-18, four days after the invoice that states them.
- Condition: No date in the invoice that records something already established lies after the issue date; the two exchange rates agree in date, or the later one is explicitly a future fixing (which UBL's element does not express).
- Options: date the terms' exchange rate 2026-05-14 (preferred: it is the same rate) or remove it, since `PaymentAlternativeExchangeRate` already gives it; start the validity on the issue date or drop it.
- Needs decision: no

### sea/22#F3 · Medium · Gate number in AdditionalStreetName of the supplier's postal address
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name, and has no place in a postal (invoicing) address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`.
- Options: drop it from the postal address (preferred).
- Needs decision: no

### sea/22#F4 · Low · Real-time settlement channel with a non-urgent service level
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTNS`
- XPath: `/Invoice/cac:PaymentMeans/cbc:ServiceLevelCode` = `NURG`
- Why: The channel is ISO 20022 `RTNS` (RealTimeNetSettlementSystem), the service level `NURG` (non-urgent payment). A non-urgent payment due 45 days later is normally cleared through a mass/batch system (as `18-Invoice.xml` does with `MPNS`); asking for a real-time channel and a non-urgent service level at once is contradictory.
- Condition: Channel and service level fit each other.
- Options: `MPNS` with `NURG` (preferred); or `RTNS` without the non-urgent level.
- Needs decision: no

### sea/22#F5 · Low · Contacts do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier's contact is customer service in Sales and the accounting customer's is "Purchasing" in Sales; the warehouse's goods-inwards contact also sits in Sales. An invoice's accounting parties need contacts for receivables and payables; names and departments contradict each other.
- Condition: The accounting parties' contacts handle invoices, and each contact's name and department agree.
- Options: accounts receivable at Lumeway, accounts payable at Velumi; fix the departments.
- Needs decision: no

### sea/22#F6 · Low · Product master data copied into the invoice
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: Search keywords, sales conditions, load tests, maintenance and repairability data and the item's emissions are catalogue data; the invoice bills 96 benches and 12 castings and does nothing with them. The same item blocks appear in all goods documents of the flow.
- Condition: The invoiced item carries identification, classification, origin and tax category, plus other data only with a billing reason.
- Options: reduce the item (preferred).
- Needs decision: no

## Checked and consistent
- Lines: 96 × 520 = 49 920.00; 12 × 64 = 768.00; sum 50 688.00; charges 2 950 + 140 = 3 090.00; tax exclusive = inclusive = 53 778.00 (0 % export); prepaid 10 000.00; payable 43 778.00; alternative 43 778 × 0.4 = 17 511.200 XLC.
- Terms: 10 000 / 53 778 = 18.595 % → 18.59 %; 81.41 % → 43 778.00; penalty 1.5 % × 43 778 = 656.67; deposit due 2026-05-09 after the order response of 05-08 (event 8); prepaid payment paid 05-08, received 05-09.
- Freight 2 950 = 2 700 + 250 and insurance 140 agree with `14-BillOfLading.xml`; insured value there is 53 778 × 1.1; CIF Selanu agrees with the order.
- Order `VT-PO-26-0127` lines 1 and 2 resolve; quantities agree with despatch, receipt and import declaration.
- Factoring: type 393, assignment note, payee and payee account `XB51BLUM38020502304038` (Harbourline Factoring Ltd), financing party and financing account agree; RF `RF20LDINV260147` and IBAN-like account pass `check_ids.py`.
- Tax: category G with exemption "Export outside Bayvarra" fits a CIF export to Lisavu for goods and the related freight/insurance.

## Considered and refuted
- `/Invoice/cac:AllowanceCharge[2]/cbc:AllowanceChargeReasonCode` = `96`: an insurance charge coded from UNTDID 5189 while the freight charge uses 7161 — refuted: 5189 is the "allowance or charge identification" list and 7161 (as in `world/codelists/sources/peppol/UNCL7161.xml`) has no code for cargo insurance itself, only for insurance brokerage.
- `/Invoice/cac:PaymentMeans/cac:CreditAccount/cbc:AccountID` = `HF-CL-VT-001`: a credit account in an invoice's payment means — refuted: it is the factor's ledger account for this debtor, which helps matching the payment at Harbourline.
- `/Invoice/cac:PaymentMeans/cac:RemittanceDocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`: remittance advices to the factor rather than the seller — refuted: under the assignment the factor receives the payment and needs the remittance.
- `/Invoice/cbc:IssueDate` = `2026-05-14`: invoice before arrival — refuted: under CIF the seller invoices on shipment.
