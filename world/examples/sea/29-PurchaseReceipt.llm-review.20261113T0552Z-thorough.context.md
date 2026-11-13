# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/29#F1 · Medium · "Services outside scope of tax" used for a sale of goods
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: UNCL 5305 code O is "Services outside scope of tax" (the listing gives this meaning; own knowledge: "Code specifying that taxes are not applicable to the services"). The receipt sells two park benches, and the same tax category states `SupplyTypeCode` GOODS. Lisavu has no general sales tax (`TaxScheme/Name` "No general sales tax"), so the sale is indeed outside the scope of tax, but the code chosen names services. EN 16931 uses O for any supply "not subject to VAT", goods included; under the agreed rule of semantic conformance that practice does not make the code fit. The same combination (O with GOODS in a classified tax category) occurs 5 times in 5 examples (counted with a script over `world/examples/*/*.xml` matching `ClassifiedTaxCategory` blocks with both values).
- Condition: The tax category code of a goods supply outside the scope of tax names goods or supplies in general, not services; or the project records the use of O for goods as a deliberate finding against UNCL 5305.
- Options: (a) preferred: decide at project level, since the issue is the same wherever Lisavu's "no general sales tax" applies to goods, and record it in the code list decisions (a world code for "outside the scope of tax" or a documented exception); (b) keep O and add the case to the findings on EN 16931 practice.
- Needs decision: yes

### sea/29#F2 · Low · The farm's full master data and the seller's search keywords on a till receipt
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine[2]/cbc:Line` = `Farm track off Plantation Road at kilometre 4, past the cotton fields.`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: A purchase receipt is "A receipt for a purchase made with cash or cash equivalents" at a point of sale. The farm collected the benches itself (note "Collected by the farm with its own trailer"), so nothing is delivered to its address; still the receipt carries the farm's address twice (structured and as four address lines repeating the same parts), its coordinates, the physical location of its cotton fields, a contact and legal-entity data. The item carries the seller's search keywords ("A keyword (search string) for this item, assigned by the seller party"), which mean nothing on a receipt. These are master data copied into a document that does not use them; naming the business customer (for its accounts) needs its name and identifier, perhaps its address once.
- Condition: The receipt carries the customer data a business customer needs on a receipt (identification, name, at most one rendering of the address) and no catalogue search data.
- Options: (a) preferred: keep the farm's identifier, name and structured address; drop the address lines, coordinates, physical location and keywords.
- Needs decision: no

### sea/29#F3 · Low · The point-of-sale location named by the company and its address
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Velumi Trading, Reef Street, Selanu`
- Why: `PointOfSaleLocation` is "The location of the point of sale where this purchase took place", and a location's name names the place, not the company. The value combines the seller's name with its street and town, i.e. it repeats the seller's postal address (Reef Street 16, Selanu) as a name. The till `T1` identifies the register, but the shop itself has no name or identifier of its own.
- Condition: The point-of-sale location is named as a place (e.g. the shop or counter) or identified, and does not repeat the seller's name and address as its name.
- Options: (a) preferred: name the shop or sales counter (e.g. "Trade counter") and, if needed, give its address in the location's address; (b) remove it, since the seller's address already says where the sale took place.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 × 289 = 578.000 XLC = line, totals and paid amount; tax 0.000.
- Card payment: debit card (UNCL 4461 code 55) agrees with the card type DEBIT; the masked PAN, issuer (Bank of Selanu), approval status and terminal fit a card sale; payment time equals the transaction time.
- The item is the bench of the sea flow (GTIN `9520610000012`, manufacturer's ID `VI-B180`, origin Urvania); the description "imported from Bayvarra" agrees with the import declaration `19-ImportCustomsDeclaration.xml`.
- Price plausibility: Velumi bought at 49920.00 / 96 = 520.00 XBL per bench, i.e. 208.000 XLC at 0.4 (`22-Invoice.xml`); selling at 289 XLC leaves a plausible margin.

## Considered and refuted
- `/PurchaseReceipt/cbc:ProfileExecutionID`: the retail sale carrying the same execution ID `SEA-2026-01` as the sea shipment, under another profile, suspected to join unrelated transactions — refuted because every document of this flow, under transport, customs, billing and despatch profiles alike, shares the flow's execution ID, and the receipt sells goods from this shipment.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:WarrantyInformation[2]`: warranty text on a receipt suspected as copied catalogue data — refuted because the receipt is the buyer's proof of purchase for a warranty claim, so the warranty has a reason here.
- `/PurchaseReceipt/cac:PaymentMeans/cac:CardAccount/cbc:HolderName`: a company as cardholder suspected implausible — refuted because business debit cards are issued in a company's name.

## Outside this review
- The order's accounting cost "Stock for municipal projects" and its beneficiary (the Port of Selanu) suggest that all 96 benches were bought for the port; whether two of them can be sold from stock to the farm on 2026-06-13 is a stock question across documents.
