# LLM review: 02-Invoice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/02-Invoice.xml`, Git blob `ca1ffa8a13476757483bcb761f1e9079132080e5` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
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

### energy/02#F1 · Medium · Network-use lines do not say which connections they bill; two lines are indistinguishable
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `FG-NET-E`
- XPath: `/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `412800`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- Why: the invoice bills the retailer for network use "per kilowatt hour taken at the connection", but no line names the connection (consumption point, delivery location or a note), and no line or document reference points to the utility statement 01-UtilityStatement.xml that supplements it. Lines 1 and 2 carry the same item, description and price and differ only in quantity, so the buyer cannot tell what each line is for or check it against its customers' metering. Line 3 matches the consumption point of 01-UtilityStatement.xml (61 200 kWh), but only by its quantity. For a grid-use invoice to a retailer, which connection is billed is what the document's purpose depends on.
- Condition: each line identifies the connection (or group of connections) it bills, and lines 1 and 2 can be told apart; the link to the utility statement can be followed from the invoice.
- Options: (a, preferred) add the connection per line (e.g. `InvoiceLine/cac:Delivery/cac:DeliveryLocation` with the consumption point ID, or a line `Note`), and an `AdditionalDocumentReference` to FG-DOC-26-0149; (b) merge lines 1 and 2 if they are not separate connections.
- Needs decision: no

### energy/02#F2 · Medium · Province given in Region
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (`CountrySubentity`). The XU address format code puts Region on the last line, so this is a world convention. The value occurs 219 times in 104 of the 250 XML examples (`grep -rh --include='*.xml' -o '<cbc:Region>[^<]*'`).
- Condition: the province of an Urvanian address is in `CountrySubentity`, or the world states why it is an economic region.
- Options: (a, preferred) move to `CountrySubentity` and update the XU address format; (b) document the convention.
- Needs decision: yes

### energy/02#F3 · Low · Contacts do not fit the roles on an invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Metering office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the accounting supplier's contact answers questions about the bill and the accounting customer's contact deals with payables. The grid operator's metering office and the retailer's customer service in Sales are the contacts of the metering statement (01-UtilityStatement.xml), copied here.
- Condition: the contacts of the accounting parties are billing / accounts-payable functions (or the metering office is explained as the billing contact for grid use).
- Options: (a, preferred) role-specific contacts; (b) keep the metering office for the supplier if grid-use queries go there, and change the customer's.
- Needs decision: no

### energy/02#F4 · Low · Supplier's industry code covers electricity only, but it bills gas network use
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is electricity; distribution of gaseous fuels through mains is 3520 (own knowledge of ISIC). Line 3 bills gas network use.
- Condition: the classification covers the party's gas network activity.
- Options: (a, preferred) add 3520 as a second code; (b) leave as is.
- Needs decision: no

## Checked and consistent
- Lines: 412 800 × 6.2 = 2 559 360; 18 600 × 6.2 = 115 320; 61 200 × 1.9 = 116 280; sum 2 790 960 = LineExtensionAmount = TaxExclusiveAmount = TaxableAmount.
- VAT 20 % of 2 790 960 = 558 192; TaxInclusiveAmount 3 349 152 = PayableAmount.
- Settlement discount 2 % of 3 349 152 = 66 983.04 → 66 983; settlement period 2026-04-03 to 2026-04-13 (10 days); due date 2026-05-03 (30 days), equal in DueDate, PaymentMeans and PaymentTerms.
- RF13FGINV260150 and the payee account check digits OK (`check_ids.py`); account holder and branch agree with the supplier.
- Line 3 quantity equals the energy of the consumption point in 01-UtilityStatement.xml; InvoicePeriod March 2026 equals the statement's period.

## Considered and refuted
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: suspected the discount should be on the net amount — refuted: UBL does not fix the base, and 2 % of the payable amount is a common reading; the Note says "2 % discount", consistent.
- `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode`: suspected network use as goods — refuted: use of a network is a service.

## Outside this review
- The retailer buys 18 400 MWh of electricity in March (03-Invoice.xml) but is billed network use for only 431.4 MWh of electricity here; whether this invoice covers only some of its customers' connections is a question of volumes across documents.
