# Consistency review: conditions

Run: `20261114T2143Z-consistency` · Review date: 2026-11-14 · Topic: conditions
Examples: 250 in 18 flows, at commit e8ff272 (claude/stoic-noether-5pboei); tables built from commit a7f6100 on the same branch (README of .review/tables); `git diff a7f6100 e8ff272 -- world/examples` is empty, so the tables describe the examples as reviewed.
Inputs: the XML examples, the extraction tables, the merged per-example reviews, `analysis/review-merge-decisions.md`, the output of `check_consistency.py`, and `world/codelists/gc/*.gc` only to read what a code means. No world data, generators or companion documentation were read.

## What is expected

Every finding below, and every entry under "Considered and refuted", "Leads" and "Cannot be told", is looked into and ends either resolved (its condition holds in the XML) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by the owner first, because the fix changes a rule of the world, not only an encoding. This review describes which conditions of the world are stated or applied inconsistently across documents and flows; it does not say where or how the examples are produced.

## The world's conditions as the documents state them

Counts are over `world/examples/*/*.xml` (250 files), made with scripts over the extraction tables and checked in the XML with lxml.

### Exchange rates

| Rule as it appears | Evidence | Open points |
|---|---|---|
| Two fixed parities for the whole of 2026: 1 XBL = 100 XUF, 1 XBL = 0.4 XLC (1 XLC = 2.5 XBL). No XUF↔XLC rate is ever quoted. | All 56 `*ExchangeRate` aggregates in 28 files: XBL→XLC 0.4 (18), XBL→XUF 100 (15), XUF→XBL 0.01 (11), XLC→XBL 2.5 (4), identity rates (8). Dates 2026-01-02 to 2026-06-06. The world list `EntitySizeCode` states the same parities in its thresholds (2,000,000.00 XBL = 200,000,000 XUF = 800,000.000 XLC). | Whether the currencies are pegged is never said (see "Cannot be told"). A "forward purchase of ferra" (`BL-FX-26-0091`, 2026-01-02) at exactly the later spot rate only makes sense under a peg. |
| Direction: Tax/Payment/PaymentAlternative rates run from the document currency to the other currency; Pricing rates run from the pricing currency to the document currency; line rates in reminders, statements and remittances run from the referenced document's currency to this document's. | tender/26–35, cotton/04–05, packaging/09, road/15, sea/22, sea/28; energy/06–09; sea/25, sea/27. | Consistent; no finding. |
| Rate date = issue date of the document; a pricing rate carries the date its contract fixed it. | 44 of 56 rates are dated. Every Tax, Payment, PaymentAlternative and line rate is dated on the issue date except air/04 (a week later) and sea/22 (one rate four days later), both already High in their reviews; the pricing rates of tender (12) and energy/06–07 are dated 2026-01-02; the telecom rates of utilities/12 carry the statement period's end. | With fixed parities the date changes no amount. |
| Amounts in two currencies follow the parities. | packaging/09 (35.940 XLC ↔ 89.85 XBL), sea/02 (520 ↔ 208), sea/19 freight share, sea/22 (43778.00 ↔ 17511.200), sea/28 (51.250 ↔ 128.13), tender/32 (20880.00 ↔ 2088000), tender/33 (499 ↔ 49900), energy/08–09 (132480000 XUF ↔ 1324800.00 XBL; surcharge 19872.00 XBL ↔ 1987200 XUF), carnet threshold. | All hold. |
| Tax amounts are also given in the seller's national currency when a document is in another currency. | tender/32, 33, 35 (XBL document, XUF tax currency); packaging/09 (XLC receipt, tax subtotals in XBL). | Missing in energy/06 and energy/07 (Kelpstone, a Bayvarran seller, invoicing in XUF): already option (a) of energy/06#F1 and energy/07#F2. |

### Taxes per country

| Country / scheme | Rule as it appears | Evidence | Open points |
|---|---|---|---|
| Urvania, `VAT` | Standard 20 % (S) on every domestic supply, goods and services, B2B (no resale exemption: it is a VAT). Exports of goods G 0 % `EXP` "Export of goods outside Urvania". Services to a customer established abroad O `SVCABROAD` "Service to a business established outside Urvania". International carriage bought by an Urvanian customer is taxed at 20 % (plastics/07 river freight, rail/10 container rail freight to Marrowdale); bought by a foreign customer it is `SVCABROAD` (road/14). So place of supply follows the customer. | 48 VAT rows of `taxes.csv` in energy, ore, plastics, rail, road, tender, utilities, waste. | `SVCABROAD` also used for a foreign public body (F8). Excise (`EXC`) only in utilities/02. |
| Bayvarra, `STT` (sales tax) | Standard 6.5 % (S) only on retail sales to consumers (packaging/08–09, retail/21–22). Every B2B supply is exempt E: `RESALE` "Sale for resale or manufacture" (goods to a reseller or manufacturer), `SVCB2B` "Service to a business" (freight by air, sea and road, customs clearance, insurance, return transport), `PUBLIC` "Sale to a public body" (goods and installation work, furniture/15, 17), `WATER` "Drinking water". Exports G 0 % `EXP` "Export outside Bayvarra" (to Urvania and Lisavu, also in XUF invoices). Levy collected for the city O `LEVY`. | 103 STT rows of `taxes.csv` in air, cotton, energy, furniture, mast, packaging, retail, sea, tender, utilities, wood. | A Bayvarran withholding tax of 10 % on services of non-residents and a tax representative appear only in the tender flow (F4). |
| Lisavu, no ID | "No general sales tax": category O 0 % on goods and services, scheme with a name and no ID. A presumptive tax on farm produce (OTH, tiered 1 % up to 2,000 coral, 2 % above) is withheld by the ginnery at delivery, not on the advance; a cotton fund levy is collected for the Selanu Chamber of Commerce. | 20 rows in cotton/01, 04, 05, 08, 16; sea/28, 29; utilities/12, 13. | Category O for goods is the recurring Medium/yes of the merge decisions. An "import consumption tax" is mentioned once (carnet/03, F5). |
| Who charges which tax | The seller applies its own country's scheme; exports are exempt there; nothing about the importing country's tax on import is stated anywhere (all import declarations: "Duties paid by the importer's account at customs."). | 6 import declarations. | F5. |

### Payment

| Rule as it appears | Evidence | Open points |
|---|---|---|
| Domestic Urvania: credit transfer (30) over channel `RTGS`, rail `FERRA-RTGS`. Domestic Bayvarra: 30 over `MPNS`, rail `LUMEPAY`. Domestic Lisavu: 30 over `RTGS`, rail `CORAL-NET`. Cross-border: 30 over `RTNS`, rail `TRADE-ACCORD-PAY`, charge bearer `SHAR`. | All 66 PaymentMeans; no exception. | Service level only once (sea/22 `NURG`, sea/22#F14). |
| One bank per country: Crevalto Bank `CREVXUFR` (branch `03510-416nn`, 26-character `XU…` account), Bank of Lumeport `BLUMXBLX` (6-digit branch, 22-character `XB…`), Bank of Selanu `BSELXLSL` (3-digit branch, 21-character `XL…`); account in the country's currency, type `CACC`, format `ISO13616`; branch code embedded in the account number. | All 91 FinancialAccount rows. | Consistent. |
| Standard terms per seller country: `XU-STD` "30 days net; 2 % discount when paid within 10 days." (discount = 2 % of the tax-inclusive amount, settlement period issue date + 10 days, penalty interest 8 % a year, simple); `XB-STD` "30 days net; 1.5 % surcharge per month late." (penalty = 1.5 % of the payable amount, penalty period one month from the day after the due date); `XL-STD` "45 days net." (penalty interest 6 % a year). | 13 × XU-STD, 17 × XB-STD (plus sea/22's `BALANCE` with the XB-STD text), 3 × XL-STD; every discount, penalty amount and period recomputed: all hold. | The periods do not hold in 7 of these 34 places (F2). |
| Statutory late-payment rules: "Urvania's statutory interest" 8 % a year, computed per day (tender/35: 20286.32 × 0.08 × 5/365 = 22.23); "Bayvarra's surcharge of 1.5 % a month" (energy/08, applied after one full month; none after 8 days in utilities/10). In both cross-border cases the seller's country's rule is applied. | tender/35, energy/08, utilities/10. | Which law governs a cross-border contract (see "Cannot be told"). |
| Contract-specific terms (framework transport plans: "30 days net from the consignment note."; tender contract: "30 days after each accepted release.") | ore/03, plastics/04, rail/03; tender/01–03, 24. | Never applied by the invoices (F3). |
| Cards: 54 (credit) and 55 (debit) in shop receipts, cash 10 once, direct debit 49 with one mandate (utilities/09), clearing between partners 97 for a self-billed credit (cotton/05). | packaging/08–09, retail/21–22, sea/29, utilities/09, cotton/05. | Consistent. |

### Customs and trade rules

| Rule as it appears | Evidence | Open points |
|---|---|---|
| Declaration types: export `ExportTypeCode` PERMANENT + `ExportReasonCode` SALE; import `TypeCode` IMPORT + `SubTypeCode` FREECIRC + `NatureOfTransactionCode` PURCHASE; transit TRANSIT/EXTTRANSIT. `CustomsProcedureCode` only in plastics/09 (1000) and carnet/03 (2000, temporary admission). | 7 export, 7 import, 1 transit declarations. | Consistent apart from the procedure code being given in one import only (noted under F6). |
| Customs value = the value of the goods lines of the sales invoice, converted at the parity; the invoice's own document-level charges (special colour, export pallets, freight and insurance in sea/22) are never in it; separately invoiced freight is added only in plastics/09. | Every export and import value recomputed (F5). | Whether freight to the border belongs in the value differs by flow (F5). |
| Duty and preference under the Trade Accord: every import says "Duties paid by the importer's account at customs." without any duty; preference is claimed once (plastics/09 `P`); a certificate of preferential origin exists in road (06, 07) but the import (road/10) claims none. | 7 import declarations. | F6. |
| Incoterms against who pays carriage: FCA/FOB → buyer pays (ore/06, road/14, cotton/17); CPT/DAP/DDP → seller pays (plastics/07, rail/10, air/10, retail/16). | All 36 DeliveryTerms and the freight invoices. | Consistent except sea (CIF, freight and insurance charged on top: sea/22#F3) and cotton/04 (DAP with a haulage charge to the buyer: cotton/04#F18), both already findings. |
| Tariff classification: HS 2022 everywhere; an 8-digit national subheading only from the Urvanian tariff and only for the bench and its side frame. | 15 customs declarations. | F10. |

### Price and contract conditions

| Rule as it appears | Evidence | Open points |
|---|---|---|
| Lumeway's trade price list `LD-PL-2026`: bench 520 XBL, side frame 64 XBL per EA, "Full container" discount 3 %, territory Bayvarra; a revision `LD-PL-2026-2` (2026-05-20) sets the side frame to 58. | retail/02, sea/02, retail/03; used at 520/64 in retail/08, 18, 19, sea/05, 06, 22, 26, air/01. | Tax treatment under the same list differs (F1); revision below cost (F11). |
| Valdara's prices: bench 49900 XUF, side frame 5980 XUF, installation 1800 XUF; to the distributor (road, rail) and to the public works department (tender, list `VI-PL-2026`, "Contract price") alike. | road/01, 15; rail/01, 11; tender/25, 26, 32, 33. | F11. |
| Same item, same seller, same unit and price in every document of a flow (cotton lint 0.988 XLC/KGM, slats 7.2 XBL/EA, ore 8060 XUF/TNE, gas 3600 XUF/MWH, water 2.35 XBL/MTQ, sea freight 2950 XBL per 40-foot container in both directions). | Price table over all 283 lines. | Consistent. |
| Allowances coded from UNCL 5189, charges from UNCL 7161, except insurance (5189 `96`) and interest on arrears (5189 `48`), which the repository's 7161 list does not have; `64` "Special agreement" is the catch-all for deductions; `95` "Discount", `100` "Special rebate". | 47 AllowanceCharge and FreightAllowanceCharge aggregates. | Consistent; reasons used the same way across flows. |
| Framework transport agreements (Valdara–Ferrano Rail Cargo `VI-FRC-FW-2026` in ore and rail; Rinova–Fiumella `RR-FB-FW-2026` in plastics): identical clauses (payment 30 days from the consignment note, penalty 5 % a day up to 25 %, waiting time "40 per hour beyond two hours", changes free up to 24 hours). | ore/03, rail/03, plastics/04. | Not applied by the invoices (F3); the waiting-time rate has no currency (see "Cannot be told"). |

### Other rules the documents state

| Rule as it appears | Evidence | Open points |
|---|---|---|
| Legal references: Bayvarran acts cited by ID `XB-PPA-2019` (Public Procurement Act, art. 61 for guarantees), `XB-STT-ACT`, `XB-ENV-2021` (art. 12), `XB-LAB-2018`; `RegulatoryDomain` "Bayvarra public procurement". | tender/01–03, 06, 09, 14, 21, 24; same IDs and meaning everywhere. | The design-contest flow of the same authority cites none (not a contradiction). |
| Size classes (world list `EntitySizeCode`): micro < 10 persons, small < 50, medium < 250 and turnover ≤ 50,000,000.00 XBL, large above. | tender/04 (85 persons, SMALL), tender/13 (180 persons, LARGE). | F12; the sawmill case is already High in tender/04#F1. |
| Working week: of 779 contacts, 627 give "Weekdays 08:00–17:00" and 6 "Weekdays 07:00–19:00" (no other hours occur); the SLA of sea/03 excludes Saturday and Sunday; "two working days" (tender auction), "first working day of each month" (utilities/08). No holiday is stated anywhere. | contacts table; sea/03; tender/02, 03, 21; utilities/08. | 48 documents are dated on a Saturday or Sunday (F7). |

## Findings

### conditions#F1 · High · One price list for Bayvarra, two tax treatments; catalogue territory is always the seller's country
- XPath: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`
- XPath: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `retail/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`
- XPath: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XB`
- XPath: `sea/02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `sea/02-Catalogue.xml:/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XL`
- XPath: `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `tender/25-Catalogue.xml:/Catalogue/cac:ReceiverParty/cac:PostalAddress/cac:Country/cbc:IdentificationCode` = `XB`
- Why: `RequiredItemLocationQuantity` is the location-specific price; its `ApplicableTerritoryAddress` is where that price applies and its `ApplicableTaxCategory` the tax that applies there. The same price list `LD-PL-2026`, the same item, price (520 XBL), unit and territory (Bayvarra) carry two incompatible tax treatments in two flows: E `RESALE` in retail/02 (a domestic sale to a reseller) and G `EXP` "Export outside Bayvarra" in sea/02 (an export to Lisavu). An export exemption cannot apply to a price for the territory of Bayvarra. The same shape recurs in tender/25 (territory Urvania, export exemption, buyer in Bayvarra). All three catalogues put the seller's country into the territory, whatever the market; the contradiction appears wherever the market is abroad (2 of 3). sea/02#F1 and tender/25#F1 report each case alone; the cross-flow view adds that one Bayvarran price list is stated with both treatments, so the list itself does not say which tax applies.
- Condition: in every catalogue, the territory of a location-specific price is the market it is offered for, and its tax category is the one that applies to a sale into that territory; one price-list ID with one territory carries one tax treatment.
- Options: (a) preferred: territory = the buyer's market (XL in sea/02, XB in tender/25), keeping the export exemption; this matches the flows' invoices (sea/22, tender/32); (b) give the export catalogue its own price-list ID (an export list) so `LD-PL-2026` stays the domestic list; (c) both.
- Needs decision: no (the invoices already show the intended treatment)
- Seen in reviews: sea/02#F1, tender/25#F1

### conditions#F2 · High · The standard terms IDs do not mean the same number of days everywhere
- XPath: `mast/05-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XB-STD`
- XPath: `mast/05-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-06-04`
- XPath: `mast/05-Invoice.xml:/Invoice/cbc:DueDate` = `2026-07-19`
- XPath: `cotton/16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XL-STD`
- XPath: `cotton/16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- XPath: `cotton/16-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-01`
- XPath: `sea/22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `sea/22-Invoice.xml:/Invoice/cbc:DueDate` = `2026-06-28`
- XPath: `utilities/02-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `utilities/02-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `utilities/06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XB-STD`
- XPath: `utilities/06-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `utilities/09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XB-STD`
- XPath: `utilities/09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- XPath: `utilities/13-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XL-STD`
- XPath: `utilities/13-Invoice.xml:/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `air/10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`   (one of the 14 XB-STD places that do mean 30 days)
- Why: the terms IDs are the sellers' countries' standard terms, and their notes fix the period: `XU-STD` 30 days (13 invoices), `XB-STD` 30 days (17, plus sea/22's `BALANCE` with the same text), `XL-STD` 45 days (3). Recomputed due date − issue date for all 34: 27 agree. The 7 that do not fall into two patterns that each run across flows. (1) Utilities: all four utility invoices of 2026-04-02 are due 21 days later (2026-04-23), whatever their country and terms ID (XU-STD in utilities/02, XB-STD in 06 and 09, XL-STD in 13); utilities/09 even redefines `XB-STD` as "Collected by direct debit 21 days after the invoice date.", so the same ID carries two different texts. (2) Every cross-border invoice between Bayvarra and Lisavu uses the buyer's country's period under the seller's terms text: mast/05 (Bayvarran seller, Lisavan buyer) 45 days under "30 days net"; sea/22 (same direction) balance due 45 days after shipment under "30 days net"; cotton/16 (Lisavan seller, Bayvarran buyer) 30 days under "45 days net." (3 of 3; Urvania–Bayvarra invoices cannot show the pattern because both periods are 30 days). The per-example reviews rate each place High; the cross-flow view shows that the deviations are not random slips but two consistent rules the documents never state, while the reminders apply the seller's country's late-payment rule (tender/35, energy/08), not the buyer's.
- Condition: one terms ID has one text and one period in every document; every due date follows from the period of the terms the document cites; if utilities are due in 21 days or cross-border invoices follow the buyer's period, that rule is visible in the terms text (or in a terms ID of its own).
- Options: (a) if the world has no such rules: correct the 7 due dates (and the follow-up documents: sea/25, the penalty periods) to the cited terms; (b) if utility bills are due in 21 days: give the utilities their own terms ID and text (e.g. a regulated utility term), leaving `XB-STD` with one meaning; (c) if cross-border invoices follow the buyer's period: cite the buyer's terms ID and text. Preferred: (b) for utilities, because all four documents and the direct debit agree on 21 days, and (a) for the three Bayvarra–Lisavu invoices, because nothing else in the world supports a buyer's-period rule.
- Needs decision: yes (the merge decisions treat each place as "correct the due date, no decision"; the cross-flow patterns suggest the 21 days may be an intended rule of the utilities story)
- Seen in reviews: mast/05#F1, cotton/16#F1, sea/22#F1, utilities/02#F2, utilities/06#F1, utilities/13#F1; utilities/09 notes the 21 days as the only consistent case; merge decisions row "Due date that contradicts the payment-terms text"

### conditions#F3 · High · Contract-specific payment terms are never applied: every invoice under a contract uses the seller's standard terms
- XPath: `ore/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `ore/06-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `rail/03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `rail/10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `plastics/04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `plastics/07-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- XPath: `tender/24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.`
- XPath: `tender/27-OrderChange.xml:/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:ID` = `XU-STD`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`
- Why: four flows contain a contract with its own payment terms: the framework transport agreement `VI-FRC-FW-2026` (cited in ore and rail with the same clauses), `RR-FB-FW-2026` (plastics) and the public works contract (tender, terms identical in 01, 02, 03 and 24). In all four, the invoice under the contract applies `XU-STD` instead: due 30 days from the invoice date (not from the consignment note or the accepted release), a 2 % settlement discount the "net" terms exclude, and 8 % penalty interest the contracts do not state. In tender the order change even misquotes the contract ("after the invoice"), and the reminder (tender/35) charges interest from a due date the contract does not support. No invoice in the 250 examples follows a contract's own terms. The per-example reviews report each pair as High; the cross-flow view shows that it is one rule applied the same wrong way in every case, so it will recur in any new flow with a contract unless the rule is fixed.
- Condition: wherever an invoice belongs to a contract or plan that states payment terms, its payment terms, due date, discount and penalty follow that contract; the standard terms appear only where no contract terms exist; tender/27, 32, 35 and 36 agree with "30 days after each accepted release."
- Options: (a) preferred: the invoices cite the contract's terms (no discount, due date from the consignment note or the acceptance); the reminder and remittance follow; (b) if the carriers' and the manufacturer's standard terms are meant to apply, change the plans' and the contract's terms to say so (then it is a story change).
- Needs decision: no (option a keeps the contracts as written)
- Seen in reviews: ore/03#F4, ore/06#F1, rail/03#F4, rail/10#F1, plastics/07#F1, plastics/07#F4, tender/27#F1, tender/32#F5, tender/35#F1, tender/36#F6; leads of tender/01, 02, 03

### conditions#F4 · Medium · The tax treatment of the tender contract follows two countries' rules, and the Bayvarran rules for non-resident services are applied only there
- XPath: `tender/02-ContractNotice.xml:/ContractNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `Withholding tax on services of non-residents`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `10`
- XPath: `tender/32-Invoice.xml:/Invoice/cbc:Note[2]` = `Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.`
- XPath: `road/14-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- XPath: `road/14-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Name[2]` = `Road transport, full truck load`
- XPath: `road/14-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `44733`
- XPath: `furniture/17-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `PUBLIC`
- Why: the notices, the call and the award (tender/01, 02, 03, 21: 10 places) state the contract's tax as Bayvarran sales tax, exempt E `PUBLIC`, which is how a Bayvarran supplier treats the same buyer (furniture/15 and 17, including installation work). The winner's invoices (tender/32, 33) instead apply Urvanian VAT (G `EXP` for the benches, O `SVCABROAD` for the installation) plus a Bayvarran 10 % "Withholding tax on services of non-residents" on the installation, collected through a Bayvarran tax representative (also on 33, 34 and 35). Elsewhere in the world, a non-resident's service to a Bayvarran customer has neither: Trasvia Haulage (Urvania) invoices Lumeway (Bayvarra) for road transport that is partly performed in Bayvarra, `SVCABROAD`, no withholding, no representative; and no other non-resident seller into Bayvarra (Valdara in road and rail, Rinova in plastics, the Lisavan ginnery in cotton/16) has a tax representative. So the documents state no rule from which a reader can tell when Bayvarra withholds on non-residents' services and when a tax representative is required, and the tender documents announce a treatment the invoices do not use. tender/32#F15 and tender/33#F16 note the representative "with nothing to represent"; tender/34#F8 the withholding on a penalty; the cross-flow comparison with road/14 and the notices is new.
- Condition: one rule for Bayvarran taxes on supplies by non-residents is visible in the documents and applied the same way in tender and road (withholding, representative, which scheme the invoice states), and the notices' tax category describes the treatment the contract's invoices use.
- Options: (a) withholding only on services performed in Bayvarra for public bodies: say so in the scheme name or a note, and keep road/14 as it is; (b) withholding on all services of non-residents: add it to road/14 (Lumeway would then withhold on Trasvia's freight); (c) drop the withholding and the representative from tender/32–35 (the installation is outside Urvanian VAT and exempt in Bayvarra as a supply to a public body). Preferred: (c), because Bayvarra's STT exempts supplies to public bodies anyway and nothing else in the world uses either device; (a) if the story needs the withholding.
- Needs decision: yes
- Seen in reviews: tender/32#F15, tender/33#F16, tender/34#F8, tender/34#F10, tender/35#F4, tender/35#F10

### conditions#F5 · Medium · The customs value is built on a different basis in each flow, also within one country
- XPath: `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99840.00`
- XPath: `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:FreeOnBoardValueAmount` = `98046.00`
- XPath: `plastics/07-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `179400`
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`
- XPath: `road/01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`
- XPath: `cotton/15-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`
- XPath: `cotton/08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- XPath: `tender/31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `19960.00`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `200.00`
- XPath: `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`
- XPath: `wood/07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `3456000`
- XPath: `wood/08-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `240.00`
- XPath: `rail/06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9580800`
- Why: recomputed for all import and transit declarations (rates from the parities):

  | Declaration (country) | Sale | Customs value | What it is |
  |---|---|---|---|
  | plastics/09 (XB) | CPT river quay Lumeport | 99840.00 XBL | FOB 98046.00 + river freight 1794.00 (= 179400 XUF): freight to the destination, also after the border |
  | road/10 (XB) | FCA Ferrano | 47904.00 + 717.60 XBL | FCA price; the buyer's freight (road/14, 44733 XUF) not added |
  | cotton/15 (XB) | FOB Selanu | 15138.63 XBL | FOB price (6055.452 XLC); the sea freight (cotton/17, 2950.00 XBL) not added |
  | tender/31 (XB) | DAP Lumeport depot | 19960.00 XBL | DAP price of the benches; the special-colour charge (200.00) left out |
  | sea/19 (XL) | CIF Selanu | 19968.000 + 307.200 XLC | FOB value of a CIF sale; the bill of lading declares 53778.00 XBL (CIF) |
  | wood/07 (XU) | DAP Ferrano | 3456000 XUF | DAP price of the slats; the pallet charge (240.00 XBL) left out |
  | energy/05 (XU) | pipeline, no Incoterm | 132480000 XUF | invoice value |
  | rail/06 transit (XU → XB) | DAP Marrowdale | 9580800 XUF | DAP price, carriage inside Bayvarra included |

  Bayvarra alone values imports on four bases: freight to the destination added (plastics), FCA or FOB price without the freight to the border (road, cotton), and a delivered price (tender). Across all flows one pattern holds: the value is the sum of the goods lines; document-level charges (special colour, export pallets, freight, insurance) are never included, although packing and charges that are part of the price paid normally are (WTO Valuation Agreement, Art. 1 and 8: own knowledge). The merge decisions record "Customs value basis (FOB vs CIF) not stated or contradicting the bill of lading" as Medium/yes with "the world's valuation rule is undecided"; this table is the evidence for that decision across all flows.
- Condition: each country's customs values follow one stated basis (e.g. CIF to the border, or FOB/FCA at the exporting border), applied to every import declaration of that country, with charges that are part of the price paid (colour, packing) treated the same way everywhere; where a transport document declares a customs value, it agrees with the declaration.
- Options: (a) preferred: one Trade-Accord rule for all three countries, value at the importing border (CIF-type: goods + freight and insurance to the border), which makes plastics/09 the model and needs freight added in road/10, cotton/15 and sea/19, and colour/pallets added in tender/31 and wood/07; (b) FOB-type value at the exporting border for all (then plastics/09 drops the freight and tender/31, wood/07, rail/06 deduct carriage); (c) per country, stated in each declaration's note.
- Needs decision: yes
- Seen in reviews: plastics/09#F6, cotton/15#F4, sea/14#F3, sea/19#F6, tender/30#F4, tender/31#F6, wood/07#F4, rail/06#F17; merge decisions row "Customs value basis"; lead road/10

### conditions#F6 · Medium · Duties, import taxes and preference under the Trade Accord are stated nowhere, and claimed once
- XPath: `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P`
- XPath: `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode` = `1000`
- XPath: `plastics/09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- XPath: `road/07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:Note[2]` = `Preferential origin under the trade accord.`
- XPath: `tender/31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:Note[2]` = `Duties paid by the importer's account at customs.`
- XPath: `carnet/03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cac:PaymentTerms/cbc:Note` = `Duties and import consumption tax of 1,300 coral fall due if no proof arrives within 30 days.`
- XPath: `cotton/01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: all six release-for-free-circulation declarations (cotton/15, plastics/09, road/10, sea/19, tender/31, wood/07) carry the same note that duties were paid, and none states a duty, a rate, an import VAT or sales tax, or an amount; energy/05 says nothing. Every good imported is of Accord origin (Urvanian benches and granulate, Bayvarran timber and gas, Lisavan cotton), yet a preference is claimed only in plastics/09 (`P`, wholly obtained, with the only `CustomsProcedureCode`); road has a certificate of "Preferential origin under the trade accord." that its import declaration references but does not claim. Whether trade inside the Accord is duty-free, and whether Urvania levies import VAT, cannot be read from the documents. Lisavu is described everywhere as having "No general sales tax", while the carnet reminder (issued in Lisavu) names an "import consumption tax". The per-example reviews found the parts (road/10#F11 "duties paid on goods that claim preferential origin", tender/31#F13 "duties paid without a duty", plastics/09#F7, carnet/03#F1 on the amount); the cross-flow view shows that no declaration anywhere supplies the rule they all depend on, and that preference is handled three ways (claimed, certified but not claimed, ignored).
- Condition: the import declarations state, consistently for each country, whether duty and import tax are due on Accord-origin goods (amount, or a preference claim with its criterion and proof), and the Lisavan import tax is either named consistently or absent.
- Options: (a) preferred: Accord-origin goods are duty-free with a preference claim (criterion, reference to the proof of origin) in every import declaration, the note changed to say what is paid (import VAT in Urvania; nothing in Bayvarra for resale; the Lisavan import tax if it exists); (b) duties are due: state duty and import tax (with tax category and amount) in each declaration; (c) leave the declarations silent and drop "Duties paid" (then no reader can tell either way).
- Needs decision: yes
- Seen in reviews: road/10#F11, tender/31#F13, plastics/09#F7, carnet/03#F1, carnet/03#F2; lead tender/31

### conditions#F7 · Medium · The world's working week is stated and not kept: 48 documents dated on Saturday or Sunday
- XPath: `tender/09-ProcurementStatus.xml:/ProcurementStatus/cbc:IssueDate` = `2026-02-21`
- XPath: `tender/09-ProcurementStatus.xml:/ProcurementStatus/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `contest/09-CallForTenders.xml:/CallForTenders/cbc:IssueDate` = `2026-04-05`
- XPath: `contest/09-CallForTenders.xml:/CallForTenders/cac:ContractingParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `furniture/09-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-03-22`
- XPath: `furniture/09-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `road/07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:IssueDate` = `2026-03-22`
- XPath: `cotton/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:IssueDate` = `2026-03-01`
- XPath: `plastics/06-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-04-19`
- XPath: `sea/25-Statement.xml:/Statement/cbc:IssueDate` = `2026-06-13`
- XPath: `carnet/03-ProofOfReexportationReminder.xml:/ProofOfReexportationReminder/cbc:IssueDate` = `2026-08-23`
- XPath: `sea/03-DigitalAgreement.xml:/DigitalAgreement/cac:DigitalAgreementTerms/cac:ServiceLevelAgreement/cbc:SaturdayAvailabilityIndicator` = `false`
- XPath: `utilities/08-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- XPath: `tender/02-ContractNotice.xml:/ContractNotice/cac:TenderingProcess/cac:AuctionTerms/cbc:ProcessDescription` = `One round, opened by an invitation sent two working days ahead. …`
- Why: the documents state a Monday-to-Friday week: 633 of 779 contacts give weekday hours and none other, the digital agreement's SLA excludes the weekend, and "working days" are used as a unit. Counted over `documents.csv` (weekday of `issue_date`, 249 dated documents): Mon 44, Tue 42, Wed 35, Thu 50, Fri 30, Sat 23, Sun 25; 48 documents (19 %) fall on a weekend, fewer than a uniform spread over seven days would give (2/7 × 249 = 71) but with Saturday and Sunday as frequent as Friday, so issue dates do not follow the stated week. 47 of the 48 are issued by a party whose own contact in the same document says "Weekdays 08:00–17:00" (or 07:00–19:00), among them the public works department (contest/08, 09, 10, 16; tender/09), customs-relevant documents (cotton/11, plastics/05, road/07), invoices (furniture/09, packaging/02, 04, waste/03) and a chamber of commerce (carnet/03). The per-example reviews flagged seven of them, mostly as Low; the cross-flow count shows a world-wide pattern, not single slips.
- Condition: either issue dates of documents made by people or offices with weekday hours fall on weekdays (as far as the story has no reason for weekend work, which the document then states), or the world's week and office hours are described so that weekend documents are consistent with them.
- Options: (a) preferred: move the 47 weekend documents to working days where the timelines allow, and keep weekend dates only for automated or round-the-clock issuers (port, carrier systems), whose contacts then say so; (b) declare that electronic documents are issued by systems at any time and the contact hours concern people only (then no change in dates, but retail/21#F2-type contradictions in text remain); (c) give the world a different week (a story change).
- Needs decision: yes
- Seen in reviews: retail/07#F2, retail/21#F2, road/07#F11, sea/15#F9, tender/05#F5, tender/09#F4, tender/10#F4; leads of sea/08, sea/12, retail/12

### conditions#F8 · Low · Urvania's "service to a business established abroad" is used for a foreign public body
- XPath: `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- XPath: `road/14-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- Why: the Urvanian code `SVCABROAD` is used in road/14 for a business customer (Lumeway) and in tender/25, 32 and 33 for the installation billed to the Lumeport Public Works Department, which Bayvarra's own documents treat as a public body, not a business (E `PUBLIC` in furniture/15, 17 and the tender notices). Urvania has no other code for a foreign non-business customer in any document, so a reader cannot tell whether the world's place-of-supply rule treats public bodies as businesses (as EU VAT does for non-taxable legal persons identified for VAT: own knowledge) or whether the code is misapplied. tender/25#F18 reports the catalogue case; the same reasoning applies to the invoice and the credit note.
- Condition: the exemption reason used for the installation describes the PWD's status as the world's rules see it, the same in tender/25, 32 and 33.
- Options: (a) keep `SVCABROAD` and widen its wording to "service to a customer established outside Urvania"; (b) a separate reason for foreign public bodies; preferred (a), because the treatment (outside the scope of Urvanian VAT) is the same and road/14 still fits.
- Needs decision: yes
- Seen in reviews: tender/25#F18

### conditions#F9 · Low · The XB-STD surcharge is encoded as one month only in all 18 places; four were flagged
- XPath: `air/10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`
- XPath: `air/10-Invoice.xml:/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `energy/08-Reminder.xml:/Reminder/cbc:Note` = `The invoice for March's gas is a month overdue: Bayvarra's surcharge of 1.5 % a month applies.`
- Why: every one of the 18 terms with the XB-STD surcharge (17 × `XB-STD`: air/10; cotton/17; energy/06, 07; furniture/09, 17; mast/05; packaging/02, 04, 07; retail/16, 18; sea/18; utilities/06, 09; wood/08, 11; and sea/22 `BALANCE`) states "1.5 % surcharge per month late" with a `PenaltyPeriod` of one month from the day after the due date and a `PenaltyAmount` of exactly one month (1.5 % of the payable amount; all 18 recomputed). The reminder energy/08 reads it as a recurring monthly surcharge. The per-example reviews flagged the one-month period as Low in packaging/02, 04, 07 and utilities/06 only; whichever way it is resolved, it has to be resolved in all 18 places the same way.
- Condition: all 18 terms encode the surcharge the same way, and the encoding agrees with "per month late" (a period without an end, or a note that the amount is per month).
- Options: (a) preferred: keep the amount as the surcharge per month and drop the end of the period (no duration), so it reads as recurring; (b) keep one month and say "per month" in the note only. Decide once for all 18.
- Needs decision: no
- Seen in reviews: packaging/02#F7, packaging/04#F7, packaging/07#F7, utilities/06#F7

### conditions#F10 · Low · Only Urvania's national tariff appears, also in Bayvarran and Lisavan customs declarations
- XPath: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `tender/31-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `sea/19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- XPath: `sea/11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `rail/06-TransitCustomsDeclaration.xml:/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `wood/07-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `440799`
- Why: of the 15 customs declarations, eight carry only the HS 2022 subheading. The other seven, all about the bench and its side frame, add an 8-digit subheading from `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`, also where the declaring administration is Bayvarran (road/10, tender/31 imports; sea/11 export; rail/06 transit) or Lisavan (sea/19). An 8-digit national subheading belongs to the tariff of the country that applies it (own knowledge of customs practice); Urvania's own import (wood/07) uses HS only. So the world shows neither "each country its own tariff" nor "a common Accord tariff": the item's classification from the manufacturer's master data travels into foreign declarations.
- Condition: the national subheading in a customs declaration comes from the declaring country's tariff (or from an Accord tariff, if the world has one), and declarations of the same country treat it the same way.
- Options: (a) preferred: drop the Urvanian subheading from non-Urvanian declarations (keep it in road/05, tender/30 and commercial documents); (b) if the Accord has a common tariff, rename the list accordingly and use it in every declaration, wood/07 included.
- Needs decision: yes
- Seen in reviews: none (the related classification question of the side frame is a separate merge-decisions row)

### conditions#F11 · Low · Valdara's distributor price equals its public contract price, and Lumeway's revised frame price is below cost
- XPath: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `49900`
- XPath: `rail/11-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `49900`
- XPath: `tender/25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`
- XPath: `tender/32-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `road/15-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `5980`
- XPath: `retail/03-CataloguePricingUpdate.xml:/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- Why: Valdara sells the Serra 180 at 49900 XUF (499 XBL) to its distributor Lumeway (road/15 in March, rail/11 in April) and at the same price, as its "Contract price" list `VI-PL-2026`, directly to the public works department in Lumeport (tender/25, 32), undercutting the distributor's own trade price of 520 XBL in the same city; Lumeway's margin on the bench is 4.2 %. Lumeway's revised list `LD-PL-2026-2` (retail/03, 2026-05-20) sells the side frame at 58 XBL, below its purchase price of 5980 XUF = 59.80 XBL. Neither is impossible (a public tender can be won at cost; a clearance price can be below cost), but no document gives the reason, and the price conditions of the world (manufacturer, distributor, public buyer) do not read as one consistent pricing story.
- Condition: either the documents give the reason for the price relations (e.g. a tender price note, a clearance reason on the revised list), or the prices form a plausible chain (distributor price below the public contract price, resale prices above cost).
- Options: (a) a lower distributor price in road and rail (e.g. a distributor discount on `VI-PL-2026`); (b) a reason in tender/25 and retail/03; preferred (a), because it also explains the distributor's trade prices.
- Needs decision: yes
- Seen in reviews: none (lead tender/19 points at the estimate in 03, a related tender question)

### conditions#F12 · Low · Valdara's size class against its stated headcount and capability
- XPath: `tender/13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `tender/13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- XPath: `tender/13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `tender/04-ExpressionOfInterestRequest.xml:/ExpressionOfInterestRequest/cac:EconomicOperatorParty/cac:QualifyingParty/cbc:EmployeeQuantity` = `85`
- Why: by the world list `EntitySizeCode`, a large enterprise has 250 persons or more, or a turnover above 50,000,000.00 XBL; Valdara states 180 persons and a financial capability of 9,200,000.00 XBL, and is `LARGE` in all 75 of its PartyLegalEntity rows (parties table). Unless its turnover is more than five times the stated capability, it is `MEDIUM`. The same threshold question for the sawmill (85 persons, `SMALL`) is already High in tender/04#F1 and its follow-ups; with Valdara the two size classes are measured against the same definition, and both deviate in opposite directions.
- Condition: every size code the documents state is consistent with the headcounts and amounts they state, under the `EntitySizeCode` definitions.
- Options: (a) Valdara `MEDIUM` in all 75 places; (b) a turnover in tender/13 that justifies `LARGE`; preferred (b) if the story wants a large manufacturer (the ore and energy volumes suggest one), else (a).
- Needs decision: yes
- Seen in reviews: tender/04#F1, tender/05#F1, tender/10#F1, tender/11#F1 (the sawmill)

## Checked and consistent

- Exchange rates: all 56 rates use the two parities; direction conventions per rate kind hold in every document (picture above); every amount given in two currencies converts exactly (packaging/09, sea/02, sea/19, sea/22, sea/28, tender/32, tender/33, energy/08–09).
- Hit group 7 of `check_consistency.py` (XUF→XBL on 2026-01-02, "base -/-" against "base 1/1" in tender/26, 27, 28, 32, 33, 35): the same rate; only the line rates carry base rates of 1. Not a rate contradiction; the redundancy is tender/26#F6 and tender/32#F9.
- Payment means, channels, rails and charge bearers per country and for cross-border payments (66 PaymentMeans); account formats, branch IDs and bank identifiers per country (91 accounts).
- Discount, penalty amounts and periods of the three standard terms (34 places), recomputed.
- Withholding in Lisavu: the presumptive tax on farm produce is withheld at delivery (cotton/04: 2000.000 × 1 % + 2068.000 × 2 % = 61.360) and not on the advance, as cotton/01 says; the credit (cotton/05, 1.500 = 2 % of 75.000) follows the top tier.
- Incoterms against who pays and contracts the carriage, in all flows (exceptions already in sea/22#F3 and cotton/04#F18).
- Legal references (`XB-PPA-2019`, `XB-STT-ACT`, `XB-ENV-2021`, `XB-LAB-2018`): same ID and meaning in the eight tender documents that cite them.
- Prices, units and base quantities of the same item from the same seller agree in every document (283 lines); allowance and charge reason codes are used with the same meaning across flows.
- Urvanian VAT on international carriage: taxed when the customer is Urvanian (plastics/07, rail/10), outside the scope when it is foreign (road/14): one consistent customer-location rule. plastics/07#F5 compares this with EU practice (zero rate for carriage of exports); that remark stands, but the world does not contradict itself.

## Considered and refuted

- Gas price chain (lead energy/02): Ferrano Energy's 8.4 XUF/kWh "network charges included" (utilities/02) covers Kelpstone's 3600 XUF/MWh = 3.6 XUF/kWh (energy/07) plus Ferrano Grid's 1.9 XUF/kWh (energy/02); electricity likewise (9.8 + 6.2 < 27.3). No contradiction.
- Bayvarran surcharge not applied in utilities/10 (`PenaltySurchargePercent` 0, 8 days after the returned debit): refuted, because energy/08 applies the surcharge per full month late ("One month late at 1.5 %."); a fee for the returned debit is a different charge (its wording is utilities/10#F8).
- Lisavu "no general sales tax" against the presumptive tax and the cotton fund levy: refuted; neither is a general sales tax. The import consumption tax of carnet/03 is not refuted and is part of F6.
- Bayvarran 6.5 % sales tax charged to the Lisavan company Velumi in packaging/09: a retail sale in a Bayvarran shop, consistent with retail/21–22.
- Lisavan tax scheme (O "No general sales tax") on sea/28, whose accounting supplier is the Bayvarran Lumeway: follows from the reversed roles already reported (sea/28#F1, merge decisions); with the roles corrected the scheme fits.
- Charges coded from UNCL 5189 (insurance 96 in sea/22, sea/25; interest on arrears 48 in tender/35) while other charges use 7161: refuted as an inconsistency; the codes mean exactly that in 5189, and the repository's 7161 list has no insurance or interest code.
- Sea freight at 2950 XBL per 40-foot container in both directions (cotton/17 Selanu→Lumeport, sea/18 Lumeport→Selanu): one forwarder's tariff, consistent.
- Two-currency settlement in energy (reminder in XBL for an XUF invoice, remittance in XUF): amounts convert exactly; consistent.

## Leads from the per-example reviews

All 221 "Outside this review" entries of the 250 merged files were read. Entries on this topic:

| Source | Entry in short | Outcome |
|---|---|---|
| tender/01, 02, 03 | the first release's invoice applies the supplier's standard terms (2 %, 8 %) instead of "30 days after each accepted release" | F3 |
| sea/06 | sea/22's "30 days net" against a due date 45 days after shipment | F2 |
| sea/22 | sea/25 repeats the due date; follow-up documents depend on it | F2 (condition includes the follow-ups) |
| sea/25 | freight and insurance charged on top of the CIF price | confirmed as sea/22#F3; cross-flow check: the only flow where Incoterm and freight payer disagree (with cotton/04#F18) — "Checked and consistent" |
| tender/31 | whether duties are due at all between Urvania and Bayvarra under the Trade Accord | F6; "Cannot be told" |
| road/10 | the customs value rests on the order, the invoice is issued later | valuation part: F5; order of documents: other topic (timelines) |
| tender/36 | whether 20308.55 lume arrive as 2030855 ferra at 100, and who bears the charges (SHAR) | "Cannot be told" |
| energy/02 | gas billed onward at 8.4 XUF/kWh "network charges included" against 1.9 XUF/kWh network use | refuted |
| utilities/01, 02, 03 | excise per-unit amounts in utilities/02 | single-flow arithmetic (utilities/02#F1, 01#F1); excise appears nowhere else, so nothing cross-flow |
| tender/22, tender/24, tender/21 | guarantee of 2400.00 at 2 % matches no base; the copied terms repeat 01–03's problems; same fee and estimate in 02/03 | within the tender flow and already findings (tender/02#F9, 03#F10, 24#F9, 24#F12); no other flow has tendering terms |
| tender/19 | 03 estimates the contract at exactly Valdara's tender amounts | related to F11 (price conditions); the estimate itself belongs to tender/03 |
| sea/08, sea/12 | documents issued on a Saturday/Sunday against weekday SLA and contact hours | F7 |
| retail/12 | lot manufactured on Sunday 2026-04-26 | calendar part: F7; the timeline: other topic |
| mast/03 | on-carriage to the mast site under CPT shown in no transport document | Incoterm duty not contradicted, only not documented: "Cannot be told"; the missing instruction is mast/02#F3 |
| road/09 | the rest in Marrowdale "under the driving-time rules" | the rule is stated nowhere: "Cannot be told"; the timeline is another topic |
| tender/17, 18 | whether the tender fees of 17 and 19 are one payment or two | money within one flow; not a world rule — not taken up |
| furniture/15 | invoice and work report add a packaging-disposal charge the order lacks | within one flow (furniture/16, 17); not cross-flow |
| retail/02 | 03 changes the side frame's price without updating the dependent price | within retail (retail/03#F11); the price level is part of F11 |
| contest/01–16 | the same party descriptions (tax exemption wording of the authority, …) recur in other flows | the exemption-reason wording recurs in 55 places (parties table) and is already a Low in each review; nothing to add on the tax rule itself |
| tender/10 | the sawmill `SMALL` with 85 employees | F12 (threshold side); tender/04#F1 |
| air/09, energy/04–07 | no import declaration in the air flow; 2400 MWh never imported | flow composition, not a condition: "For other topics" |
| ore/06, ore/08, road/14, road/17, cotton/17 | freight invoices not remitted in the flow | flow composition: "For other topics" |

The remaining entries are timelines, map scale and routes, capacity, equipment, parties and identifiers (e.g. air/04, cotton/14, sea/13–16, rail/06–08, wood/04–07, waste/01–02, cotton/12 owner code, cotton/14 MMSI, utilities/04 document ID): not this topic.

## Cannot be told from the documents

1. Are the three currencies pegged (1 XBL = 100 XUF = 0.4 XLC for the whole year)? If not, the rates should move between January and June, and a forward contract at exactly the spot rate (tender, `BL-FX-26-0091`) needs a reason.
2. Which country's late-payment rule governs a cross-border contract? The documents apply the seller's (energy/08: Bayvarra's surcharge on a sale to Urvania; tender/35: Urvania's statutory interest), although the tender contract is under Bayvarran public procurement law.
3. Are imports between Accord members duty-free? Does Urvania levy import VAT, and does Lisavu have an import consumption tax (carnet/03) despite "No general sales tax"? (F6)
4. What is the customs valuation basis of each country? (F5)
5. Does Bayvarra withhold tax on all services of non-residents or only on some, and when must a non-resident appoint a tax representative? (F4)
6. Does Urvania treat a foreign public body as a business for its place-of-supply rule? (F8)
7. tender/36: does the department pay 20308.55 XBL into Valdara's XUF account, converted at 100 into 2030855 XUF, and who bears the bank charges under `SHAR`?
8. The framework agreements' "Waiting time 40 per hour beyond two hours." (ore/03, plastics/04, rail/03) has no currency: 40 XUF (0.40 XBL) an hour would be implausibly low; 40 XBL would be 4000 XUF. Which is meant?
9. Under CPT to the mast site (mast/01), who carries the goods from Selanu airport to the site, and under which document?
10. What are the "driving-time rules" road/09 refers to?
11. Is the world's week Monday to Friday, and are there public holidays? (F7)

## For other topics

- Identifiers: `XL67BSEL0020004817534` (Lisavu Cotton Farm, cotton/01) and `XB45BLUM38522004817534` (Kelpstone Gas, energy/06) end in the same nine digits `004817534`.
- Identifiers: whether `XLMX` (ExchangeMarketID "Lumeport Exchange", tender/26–35) is an assigned ISO 10383 MIC should be checked against the repository's MIC source.
- Identifiers/parties: rail/03 names two framework contracts for the same carrier and user (`VI-FRC-FW-2026` "Framework transport agreement", version 2, and `FRC-CON-2026-005` "Framework contract for container slots" with amendment `FRC-CON-2026-005-A1`); ore/03 cites only the first.
- Parties: `EntitySizeCode` of Valdara in 75 places (F12) and the size classes of other parties without headcounts.
- Flow composition: no import declaration in air (air/09 "ready for customs clearance") and mast (CPT into Lisavu); the 2400 MWh of energy/07 have no import declaration; freight invoices of ore, road and cotton are not remitted.
- Timelines: road/10 issued before the commercial invoice (road/15); tender/32 invoices the installation before it is done.
