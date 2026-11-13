# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/17#F1 · Medium · Language code in `LocaleCode`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F1), parties (F1)

### cotton/17#F2 · Low · The forwarder bills the sea freight that the bill of lading leaves to be collected
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- XPath: `13-BillOfLading.xml:/BillOfLading/cbc:Note` = `Freight collect.`
- Why: the invoice charges the mill for the port-to-port sea freight and refers to the bill of lading 13, marked "Freight collect": the carrier collects the freight at destination from the consignee (the mill). Unless the forwarder collects as the carrier's agent, or has paid the carrier and recharges it, which the invoice does not say, the mill could be asked for the same freight twice (broad, logistics). Money and context found it consistent: under FOB (08) the buyer's side pays the main carriage, and the forwarder in Lumeport can pay the collect freight at destination for the mill and pass it on (money's refutation in 13). The documents do not say which way applies; the same question is cotton/13#F7.
- Condition: the invoice and the bill of lading describe one way in which the carrier's freight is paid.
- Options: (a, preferred) say in the invoice line that the forwarder paid the collect freight at Lumeport for the mill (or collects it as the carrier's agent); (b) mark 13 freight prepaid by the forwarder; (c) let the mill pay the carrier and make this invoice the forwarder's fee only.
- Needs decision: yes (who pays the carrier is part of the story)
- From: broad (F2), logistics (F1); money, context (checked as consistent; argument carried)

### cotton/17#F3 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: questions about an invoice go to the parties' billing functions. The accounting supplier's contact is Bayforth's export operations desk (the contact for the bookings in 09 and 13); the accounting customer's is a "Purchasing" contact with a sales job title and department, so name, title and department also contradict each other. The mill's combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: the accounting parties' contacts handle billing (accounts receivable / payable), with names, job titles and departments that agree.
- Options: (a, preferred) accounts-receivable and accounts-payable contacts; (b) drop the contacts or their job title and department.
- Needs decision: no
- From: broad (F3), parties (F2, F3)

### cotton/17#F4 · Low · Party master data the freight invoice does not use
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: the invoice is between Bayforth (supplier) and the mill (customer); their tax registrations are rightly present. The carrier Tidewell is named to identify the carriage billed ("booked with the ocean carrier"), but it is not a party to the supply, nothing is taxed for it, and its full party record (sales-tax registration, share capital, address, contact) has no use here; nor has the mill's customs-trader number in a domestic freight invoice (section 4.8, master data copied in).
- Condition: the carrier is described only by what identifies it; every identifier and registration in the parties is one the invoice has a use for.
- Options: (a, preferred) reduce the carrier to its identification and name, and drop the mill's customs-trader ID.
- Needs decision: no
- From: broad (F4), money (F1), parties (F4), context (F1)

### cotton/17#F5 · Low · The container invoiced is not identified
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4123110`
- Why: the invoice is priced per container ("one 40-foot container", 1 service unit) and describes the carriage through the consignment and the carrier, but identifies neither the container (TWLU4123110, 12) nor its size type, nor the shipment SCG-SH-26-0200. The bill of lading it refers to does not carry the container either (cotton/13#F2), so the container cannot be traced from the invoice. Completeness remark.
- Condition: the container the freight is charged for can be identified from the invoice or from the document it refers to.
- Options: (a, preferred) a transport handling unit with the container (ID and 40-foot size type) in the delivery's shipment; (b) rely on the bill of lading once it carries the container.
- Needs decision: no
- From: logistics (F2)

### cotton/17#F6 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Forwarder and mill share 1 January 1996 with the ginnery and both ports; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F5)

## Checked and consistent
- 1 service unit × 2950 XBL (base quantity 1 E48) = 2950.00 = line extension = tax-exclusive = tax-inclusive = payable; tax 0.00 on the E subtotal of 2950.00.
- Due date: 2026-03-04 + 30 days = 2026-04-03 (27 days to 31 March + 3), stated three times, as "30 days net"; penalty 1.5 % × 2950.00 = 44.25 XBL; the penalty period of one month starts 2026-04-04, the day after the due date, as "1.5 % surcharge per month late" says.
- Tax: exempt E with reason code SVCB2B and text "Service to a business" in the subtotal and the line, scheme STT, supply type SERVICES.
- `check_ids.py`: RF08BFINV260211 and Bayforth's account XB40BLUM38020502618225 (named Bayforth Forwarding Ltd, at the Bank of Lumeport) pass; a Lume account for a Lume invoice; domestic payment.
- `AdditionalDocumentReference` TOL-BL-26-0206 resolves to 13; consignment LTM-CS-26-0201 and carrier Tidewell agree with 09 and 13; Bayforth is the forwarder of 08, 09 and 13; the mill as FOB buyer pays the main carriage.
- "One 40-foot container" agrees with the 3750 kg tare in 12. Bayforth's, the mill's and Tidewell's descriptions are identical to 09/13, 08/16 and 12/13/14 (parties).

## Considered and refuted
- `/Invoice/cbc:AccountingCost` = `Raw cotton`: the raw-cotton cost centre on a freight invoice — refuted because freight inward is part of the landed cost of the cotton, booked to the same buyer's code as in 08 and 16 (from broad, money, context).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `SVCB2B`: an exemption reason for a transaction rather than a party status — refuted because the reason belongs to the tax category of the supply, where a transaction-based reason is correct; only a party tax scheme's exemption reason must be the party's status (from broad, money).
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `MPNS`: a mass-payment net system for a single business payment — refuted because domestic B2B credit transfers commonly run through such systems (from context).

## Changed in the merge
- broad/F4, money/F1, parties/F4, context/F1 → F4: grouped as copied party data (the mill's customs-trader ID from parties included).
- broad/F3 + parties/F2, F3 → F3: grouped, one finding for the contacts.
- broad/F2 + logistics/F1 → F2: money's and context's "consistent with FOB and freight collect" carried as counter-argument; yes kept.

## Outside this review
- No remittance advice for this invoice exists in the flow; whether it is paid is not shown (not required) (from broad).
