# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/02-Invoice.xml`, Git blob `ca1ffa8a13476757483bcb761f1e9079132080e5` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/02#F1 · Medium · The network-use lines do not say which connections they bill; lines 1 and 2 cannot be told apart
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `412800`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- Why: the grid operator bills the retailer for network use "per kilowatt hour taken at the connection" (item description), but no line names the connection, consumption point, meter or metering document. Lines 1 and 2 carry the same item (FG-NET-E), description, price (6.2 XUF/kWh), tax category and period and differ only in quantity; the split is implied only by the existence of two lines, which IND5/IND6 exclude, and the retailer, who passes these charges on, cannot check 2559360 and 115320 XUF against its customers' metering. For a grid-use invoice, which connection is billed is what its purpose depends on. The quantities do match connections described elsewhere, but only by coincidence of numbers: 412800 kWh is `utilities/01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `412800` (Valdara, main connection), 18600 kWh is `utilities/03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `18600` (Castrano Logistics' warehouse), both statements of the retailer to its customers; 61200 kWh is the gas consumption point of 01-UtilityStatement.xml. For the electricity lines the flow has no metering document of the grid operator, although it "owns and reads the meter" (`01-UtilityStatement.xml:/UtilityStatement/cbc:Note[2]`).
- Condition: each line identifies the connection, consumption point or meter it bills (in an element whose definition fits), and lines 1 and 2 can be told apart, or they are one line if the split has no meaning.
- Options: (a) preferred: give each line the identifier of its consumption point, e.g. `InvoiceLine/cac:DocumentReference` to the metering document, `cac:Delivery/cac:DeliveryLocation` with the consumption point ID, or a line `Note`, so lines can be checked against meter data; (b) merge lines 1 and 2 into one line of 431400 kWh if the retailer needs no split; (c) add Utility Statements of Ferrano Grid for the two electricity connections (changes the flow, would then need a decision).
- Needs decision: no
- From: broad F1, money F1 (Low), logistics F1, context F1

### energy/02#F2 · Low · The invoice does not refer to the utility statement that supplements it
- XPath: `/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `01-UtilityStatement.xml:/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- Why: the utility statement FG-DOC-26-0149 (01-UtilityStatement.xml) names this invoice as its parent and gives the readings and conversion for exactly the 61200 kWh of line 3. The invoice mentions neither the statement nor the consumption point FG-CP-4120-G1, so the link exists in one direction only and a reader of the invoice cannot find the supporting data. The statement is also issued before this invoice (energy/01#F5), which a reference from the invoice would resolve.
- Condition: line 3 (or the invoice) can be linked to FG-DOC-26-0149 or to the consumption point FG-CP-4120-G1 from the invoice itself.
- Options: (a) preferred: a line-level `cac:DocumentReference` to FG-DOC-26-0149, since the statement is line-specific; (b) a document-level `cac:AdditionalDocumentReference`; (c) leave it, if the world's billing profile says the statement always refers to the invoice and not the other way round (then say so in the profile).
- Needs decision: no
- From: context F2; the statement-link parts of broad F1 and logistics F1

### energy/02#F3 · Medium · Province held in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as the Bayvarran addresses of the flow do (e.g. `06-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:CountrySubentity` = `Coastal State`). The XU address format puts Region on the last line, so this is a world convention. `Province of Ferrano` occurs 219 times in 104 of the 250 `*.xml` examples, always in `cbc:Region`.
- Condition: no Urvanian address carries its province in `cbc:Region`, or the world states why it is an economic region.
- Options: (a) preferred: move the province to `CountrySubentity` (with a subentity code) and update the XU address format; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no
- From: broad F2, parties F1

### energy/02#F4 · Low · Contacts that do not fit an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Metering office`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Metering`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the accounting supplier's contact answers questions about the bill (billing, accounts receivable) and the accounting customer's contact deals with payables or purchasing. Ferrano Grid's metering office fits the utility statement (01-UtilityStatement.xml), from which both contacts are copied unchanged; Ferrano Energy's customer service in Sales serves its own customers, not its grid supplier.
- Condition: each accounting party's contact deals with invoicing or payment of the network charges, or the metering office is explained as the billing contact for grid use.
- Options: (a) preferred: billing / accounts contacts for this document; (b) keep the metering office for the supplier if grid-use queries go there, and change the customer's; (c) leave the contacts out.
- Needs decision: no
- From: broad F3, parties F2

### energy/02#F5 · Low · Industry classification leaves out the gas business
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is "Electric power generation, transmission and distribution"; distribution of gaseous fuels through mains and their sale is 3520 (own knowledge). Line 3 bills gas network use (`/Invoice/cac:InvoiceLine[3]/cac:Item/cbc:Name[2]` = `Gas network use`), and Ferrano Energy retails gas (01-UtilityStatement.xml) and buys gas (07-Invoice.xml). The context part refuted this because electricity is the main activity (lines 1 and 2 are 96 % of the net amount); the finding is therefore about completeness, not a wrong code.
- Condition: the classification of both parties covers their gas activity, the same way in every example of the flow, or the world states that parties carry their main activity only.
- Options: (a) preferred: add `IndustryClassificationCode` 3520 next to 3510; (b) keep the main activity only and record that rule.
- Needs decision: no
- From: broad F4 (supplier), parties F3 (supplier and customer); context listed the supplier as refuted

## Checked and consistent
- Lines, recalculated: 412800 × 6.2 = 2559360; 18600 × 6.2 = 115320; 61200 × 1.9 = 116280 (`/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`); per BaseQuantity 1 KWH; sum 2790960 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `2790960` = TaxExclusiveAmount = TaxableAmount.
- VAT 20 % of 2790960 = 558192 = `/Invoice/cac:TaxTotal/cbc:TaxAmount` = `558192`; 2790960 + 558192 = 3349152 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3349152`.
- Settlement discount 2 % of 3349152 = 66983.04 → `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `66983`; settlement period 2026-04-03 → 2026-04-13 (10 days); due date 2026-05-03 (30 days) in DueDate, PaymentMeans and PaymentTerms.
- `LineCountNumeric` 3 = number of lines; unit KWH on all lines, consistent with the per-kWh descriptions.
- Tax: standard 20 % VAT, `SupplyTypeCode` SERVICES for network use (a service, also in real VAT practice, own knowledge).
- Payment: RF13FGINV260150 and the payee account pass their check digits (`check_ids.py`); account holder `Ferrano Grid SUA` = the supplier's registration name; account in XUF.
- Line 3 quantity = the energy of the consumption point in 01-UtilityStatement.xml (1350 m³ × 4.9477 × 9.163 kWh/m³ ≈ 61200 kWh); InvoicePeriod March 2026 = the statement's period; issue 2026-04-03 after the period.
- Parties: Ferrano Grid and Ferrano Energy described exactly as in 01-UtilityStatement.xml, and Ferrano Energy as in 03-Invoice.xml; BuyerCustomerParty/SellerSupplierParty repeat the accounting parties, which their definitions ("The buyer.", "The seller.") allow; the grid operator invoicing the retailer fits the supplier model of 01.

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `66983`: discount on the wrong base — refuted: 2 % of the payable amount including VAT is a legitimate reading of the element and matches the note "2 % discount"; the net base (55819) would be the other reading, but nothing asks for it (from broad, money)
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: network use as goods — refuted: use of a network is a service (from broad)
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: implausible channel for a domestic invoice — refuted: a 3.3 million XUF payment between two large utilities is a typical RTGS payment, consistent with 03 (from money, context)
- `/Invoice/cac:PaymentTerms/cac:PenaltyInterestRate/cbc:InterestRatePercent` = `8`: penalty interest not in the terms note — refuted: the note summarises net days and discount; the structured penalty does not contradict it (from money)
- `/Invoice/cac:AccountingCustomerParty`: the grid should invoice the end customer Valdara — refuted: 01 shows the supplier model with the retailer as buyer of the grid service (from parties)
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: a possible real BIC — refuted: `XU` is not an ISO 3166 country code assigned to a country, so no real BIC has it (from parties)
- `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-G`: gas billed by an electricity grid operator — refuted: the flow consistently makes Ferrano Grid the operator of both networks (from logistics)
- `/Invoice/cbc:TaxPointDate` = `2026-04-03`: redundant with IssueDate — refuted: the definition is met; for a monthly continuous supply the tax point is the invoice date in many VAT systems (from context)
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`: repetition of the accounting customer — refuted: "The buyer." has no "if different" condition (from context)
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `3510`: the context part refuted it (main activity); the merge keeps it as Low F5 with that argument

## Changed in the merge
- broad F1, money F1, logistics F1, context F1 → F1: combined at Medium (money had Low), because the document's purpose (billing network use per connection) depends on identifying the connection; the logistics evidence (utilities/01 and utilities/03 quantities) added; the statement link split off into F2.
- context F2 + statement-link parts of broad F1 and logistics F1 → F2: kept as a separate Low finding, because a one-way link is a different problem (and condition) from the unidentified lines.
- broad F2, parties F1 → F3: Needs decision set to no (broad had yes); same decision across the flow (section 6 names it a Medium encoding problem).
- broad F4, parties F3 → F5: grouped supplier and customer; context refutation quoted in Why, condition widened.

## Outside this review
- The retailer buys 18400 MWh of electricity in March (03-Invoice.xml) but is billed network use for only 431.4 MWh here; whether this invoice covers only some of its customers' connections is a volume question across documents (from broad).
- The same gas consumption (61200 kWh, meter FG-G-20417) is billed onward in utilities/02-Invoice.xml at 8.4 XUF/kWh "network charges included"; whether that covers the 1.9 XUF/kWh billed here is a question across flows (from money).
