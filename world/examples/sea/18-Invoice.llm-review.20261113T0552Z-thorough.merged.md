# LLM review: 18-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/18-Invoice.xml`, Git blob `8959fff2666b14c481d466f04457f91ebe10f1e4` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/18#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used". The values repeat the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and name no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F2)

### sea/18#F2 · Medium · Gate number in AdditionalStreetName of the customer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance to the business park, not a street, and the postal address to which an invoice is sent does not need it. The same value occurs 79 times in 76 files, always in Lumeway Distribution's address (parties, grep over `*.xml`; broad counted the 76 files).
- Condition: The postal address holds no gate in `AdditionalStreetName`; where the gate matters (deliveries), it is in a delivery location or instruction.
- Options: (a) preferred: drop it from the postal address and give it where goods are delivered; (b) the business park's internal road name, if it has one.
- Needs decision: no
- From: broad (F2), parties (F1)

### sea/18#F3 · Medium · Bayforth's own pre-carriage on the bill of lading is not invoiced
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Name` = `Sea freight, 40-foot container`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:FreightAllowanceCharge/cbc:Amount` = `310.00`
- Why: The bill of lading this invoice refers to shows Bayforth Forwarding as road carrier of the pre-carriage, with a freight charge of 310.00 XBL. Under CIF Selanu (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:ID` = `CIF`) the seller Lumeway bears carriage to Selanu, so this haulage would be billed by Bayforth to Lumeway. The invoice bills sea freight (2 700 + 250 = 2 950), export clearance and insurance, but not the pre-carriage, and no other example of the flow bills the 310.00 (merge: `grep -l '310.00'` over `sea/*.xml` finds only `14-BillOfLading.xml`). Refutation attempt: the haulage may be billed on another invoice outside the flow; nothing says so, so it stays Medium with a decision.
- Condition: Either the invoice carries the pre-carriage charge of 310.00, or the flow shows where it is billed (or that it is included in another line).
- Options: (a) preferred: a line "Pre-carriage by road" 310.00 (payable 3 485.00), since Bayforth is the carrier and the shipper's forwarder; (b) a note that the haulage is billed separately; (c) change the bill of lading's charge.
- Needs decision: yes
- From: broad (F1)

### sea/18#F4 · Low · Outbound freight, export clearance and insurance booked as "stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCost` is "The buyer's accounting code, applied to the Invoice as a whole". The buyer Lumeway ships goods it sells under CIF Selanu; sea freight, its own export declaration and cargo insurance are, for it, distribution/selling costs of that sale, not purchases of stock ("stock purchases" fits an inbound freight bill capitalised into stock). The code occurs in no other example of the flow (broad, grep over `sea/*.xml`) and reads as copied from a purchase of goods.
- Condition: The accounting code and text name a cost the buyer books these services to (outbound freight, distribution), or are absent.
- Options: (a) preferred: an outbound freight / distribution cost account of Lumeway; (b) drop both if Lumeway gave no cost code.
- Needs decision: no
- From: broad (F3), context (F1), money (F1)

### sea/18#F5 · Low · The bill of lading is referenced with ID only
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: `AdditionalDocumentReference` is "a reference to an additional document associated with this document"; with only an ID the receiver has to guess that it is the carrier's bill of lading (`14-BillOfLading.xml`). No `DocumentTypeCode` or `DocumentType`.
- Condition: The reference states that the document is a bill of lading.
- Options: add `DocumentTypeCode` (e.g. `BillOfLading` from the world's UBLDocumentTypeCode list, which `14-BillOfLading.xml` uses in its DocumentDistribution) or `DocumentType`.
- Needs decision: no
- From: broad (F5, part), logistics (F1)

### sea/18#F6 · Low · The contacts on the invoice are operations and sales, not billing
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier claims payment and the accounting customer pays; their contacts are where questions about the invoice go. Bayforth's contact is its export desk (an operations planner) and Lumeway's is the customer service of its sales department, which serves Lumeway's own customers. Neither handles invoices; the same contacts are used for all roles of these parties in the flow (master data).
- Condition: The accounting parties' contacts handle this invoice (accounts receivable / payable), or there are none.
- Options: (a) preferred: billing contacts; (b) leave the contacts out.
- Needs decision: no
- From: broad (F4), parties (F3)

### sea/18#F7 · Low · Party master data the invoice does nothing with (carrier's tax, capital and contact; customer's share capital)
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: The carrier Tidewell Ocean Lines is neither supplier nor customer of this invoice; naming it identifies the booking, but its sales-tax registration, share capital, legal form, size, contact and electronic address play no part in Bayforth's invoice. The customer's share capital is not needed either (where a law asks for share capital on invoices, it asks for the issuer's). Master data copied in (section 4.8). The money part refuted the customer's capital as outside its lens (a parties question); the parties part raised it, and earlier flows kept the customer's share capital as a finding.
- Condition: The carrier is identified (identifier, name) without tax, capital and contact data; the customer carries no share capital.
- Options: (a) preferred: reduce the carrier to `PartyIdentification` and `PartyName` and drop the customer's `CorporateStockAmount`/`FullyPaidSharesIndicator`; (b) drop the carrier and rely on the consignment ID and the bill of lading reference.
- Needs decision: no
- From: context (F2), parties (F4), money (F2)

### sea/18#F8 · Low · The documents the charges rest on are not referenced (export declaration, forwarding instructions)
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cbc:Description` = `Preparing and lodging one export declaration as customs agent.`
- XPath: `11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cbc:ID` = `BF-EX-26-0135`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ID` = `LD-FI-26-0131`
- Why: The forwarder bills "one export declaration"; the declaration exists in the flow (`BF-EX-26-0135`, lodged by Bayforth), but neither the line nor the invoice refers to it, so the customer cannot link the service to it. The services were ordered by Lumeway's forwarding instructions `LD-FI-26-0131`, which the invoice does not mention either.
- Condition: The invoice (or line 2) refers to `BF-EX-26-0135`, and the order basis (`LD-FI-26-0131`) is referenced.
- Options: (a) preferred: a `DocumentReference` on line 2 to `BF-EX-26-0135` and an `OrderReference` (or additional reference) to `LD-FI-26-0131`; (b) additional references on the invoice.
- Needs decision: no
- From: logistics (F2), broad (F5, part)

## Checked and consistent
- Arithmetic (merge recalculated): 2950.00 + 85.00 + 140.00 = 3175.00 = line extension = tax exclusive = tax inclusive = payable; tax 0.00; each line 1 × price per base quantity 1; penalty 1.5 % × 3175.00 = 47.625 → 47.63 (broad, money, context).
- Sea freight 2950.00 = ocean freight 2700.00 + bunker surcharge 250.00 on `14-BillOfLading.xml`, prepaid by the shipper; insurance 140.00 = the B/L's premium; insured value 59155.80 = 110 % × 53778.00 (CIF) = 110 % × (FOB 50688.00 + 2950.00 + 140.00) (money; merge recalculated: 50688 + 2950 + 140 = 53778; × 1.1 = 59155.80).
- Due date (merge recalculated): 2026-05-19 + 30 days = 2026-06-18 (12 days to 31 May + 18) = `DueDate`, the payment means' and the terms' due date, matching "30 days net"; penalty period from 2026-06-19 (broad, money, context).
- Tax: category E with reason SVCB2B (service to a business in Bayvarra) on all lines and the subtotal; EXP would require a buyer outside Bayvarra (money).
- `RF98BFINV260143`, GLN `9520610900008` and the account `XB40BLUM38020502618225` pass `check_ids.py`; the account's bank code and branch `380205` agree with the branch ID; account name Bayforth Forwarding Ltd (broad, logistics, money, parties).
- Consignment `LD-CS-26-0133` and carrier Tidewell Ocean Lines agree with the B/L; one 42G1 container; issue 2026-05-19 after the arrival 2026-05-18 (`17-TransportationStatus.xml`) (logistics).
- Bayforth and Lumeway carry the same identifiers and full descriptions as in the forwarding instructions and the export declaration (parties, by script); ISIC 5229 / 4649 / 5012 fit.

## Considered and refuted
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`: buyer and seller repeat the accounting parties — refuted: UBL does not condition `BuyerCustomerParty` on being different; consistent and harmless (from broad, context, parties).
- `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: insurance would be exempt as insurance — refuted: the forwarder rebills the premium as part of its service; the world's state sales tax exempts B2B services (from broad).
- `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PaymentTerms/cbc:Note` = `Ocean freight payable before release of the bill of lading.`: freight payable before release vs a due date a month later — refuted: the B/L term is between Tidewell and Bayforth (from broad).
- `/Invoice/cbc:InvoiceTypeCode` = `380`: "commercial invoice" for services — refuted: UNCL 1001 code 380 covers any claim for goods or services (from context).
- `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0133`: shipment without its ID — refuted: the consignment ID identifies the goods in every document of the flow (from logistics).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: a business park as block name — refuted: an area containing several buildings (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`: the customer's customs trader number — refuted: the invoice bills an export declaration lodged for that trader (from parties).
- `/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `2950.00`: freight resold without margin — refuted: pass-through at cost with the fee in separate lines is common practice (from money).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: international transport as export (EXP) — refuted: EXP requires a buyer outside Bayvarra (from money).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`: refuted by money as outside its lens — not followed: raised by parties, kept in F7 (from money).

## Changed in the merge
- broad/F2, parties/F1 → F2: combined.
- broad/F3, context/F1, money/F1 → F4: combined.
- broad/F5 split: the ID-only bill of lading reference joins logistics/F1 in F5; the missing forwarding-instructions reference joins logistics/F2 in F8 (two conditions).
- broad/F4, parties/F3 → F6: combined.
- context/F2, parties/F4, money/F2 → F7: combined (one copied-master-data finding per example, as earlier flows).
