# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit c9983d2 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/29#F1 · Medium · Tax category "Services outside scope of tax" on a sale of goods
- XPath: `/PurchaseReceipt/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: UNTDID 5305 code `O` means "Services outside scope of tax" (as the listing shows). The receipt sells two benches, and the same tax category declares the supply type `GOODS`. The code's meaning and the supply type contradict each other; EN 16931 practice uses `O` for any supply not subject to VAT, but under the agreed semantic conformance the code's own meaning applies (practice is context only). 34 occurrences of category `O` exist over `world/examples/*/*.xml` (`grep -o`), so the choice affects other examples too.
- Condition: The tax category code used for the bench sale means a supply of goods not subject to tax (or the world records why `O` covers goods in Lisavu, which has no general sales tax).
- Options: (a) a code whose meaning covers goods outside the scope of tax, if the agreed lists offer one; (b) keep `O` and record the deviation as a finding of the code-list analysis. Preferred: (b) if 5305 offers nothing better, since Lisavu has no sales tax at all.
- Needs decision: yes

### sea/29#F2 · Low · Benches bought for the port's project sold from stock to a farm
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Description[2]` = `The Serra park bench from Velumi Trading's stock, imported from Bayvarra, for island customers.`
- XPath: `22-Invoice.xml:/Invoice/cbc:AccountingCost` = `Stock for municipal projects`
- XPath: `22-Invoice.xml:/Invoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The 96 benches of this flow were ordered, invoiced and booked for the Port of Selanu (originator and beneficiary on order, invoice and statement; cost centre "Stock for municipal projects"). The receipt sells two Serra benches "from Velumi Trading's stock, imported from Bayvarra" to Lisavu Cotton Farm three weeks later. Either the benches come from other stock, which nothing in the flow shows, or two of the port's benches went to a farm.
- Condition: The flow makes clear where the two benches come from (general stock beside the port's order, or part of the 96 with the port's consent).
- Options: say in the description or a note that they are from general stock (preferred); or adjust the order (e.g. 98 benches, 96 for the port).
- Needs decision: yes

### sea/29#F3 · Low · Point-of-sale location named by company and address
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Velumi Trading, Reef Street, Selanu`
- Why: A location's name is the place, not the company, and the street and town belong in an address. The seller's address (Reef Street 16, Selanu / Port Wrenfield) is already given in its postal address.
- Condition: The point of sale is named as a place (e.g. "Trade counter") with its address in `Address`, or it is identified by reference to the seller's address.
- Options: a place name plus `Address` (preferred).
- Needs decision: no

### sea/29#F4 · Low · Contacts do not fit a sales receipt
- XPath: `/PurchaseReceipt/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/PurchaseReceipt/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Velumi sells here; its contact is "Purchasing" (a customer service officer in Sales), the function that buys, not the counter that sold. The farm's office is placed in a Sales department as customer service officer, which does not fit a farm buying a bench.
- Condition: The seller's contact is the one handling sales/after-sales; each contact's name, title and department agree with the party.
- Options: Velumi sales counter / customer service; the farm office without a sales department.
- Needs decision: no

### sea/29#F5 · Low · Search keywords on a receipt
- XPath: `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- Why: `Keyword` is "A keyword (search string) for this item, assigned by the seller party"; a receipt for a completed sale has no use for search strings. (Warranty, anchors and maintenance data can serve the buyer and are not part of this finding.)
- Condition: The receipt's item carries no search keywords.
- Options: drop the keyword.
- Needs decision: no

## Checked and consistent
- 2 × 289.000 = 578.000 = line extension = tax exclusive = tax inclusive = payable = paid amount; tax 0.000.
- Payment: approved debit card payment of 578.000 XLC at 10:25, same as transaction and issue time; card issuer Bank of Selanu `BSELXLSL` (as Velumi's bank in `27-RemittanceAdvice.xml`); holder the farm; PAN masked.
- Price 289 XLC = 722.50 XBL at the flow's rate 0.4, above the purchase price of 520 XBL (`22-Invoice.xml`) plus freight and charges.
- Lisavu Cotton Farm `IC42544` and its field coordinates agree with `cotton/05-SelfBilledCreditNote.xml`; GTIN `9520610000012` passes `check_ids.py`.
- Lisavan and English renderings carry `qal` and `en-XL`.

## Considered and refuted
- `/PurchaseReceipt/cbc:Note[2]` = `Collected by the farm with its own trailer.`: two benches on a farm trailer — refuted: 2 × about 41 kg gross and 1.8 m length fit a farm trailer easily.
- `/PurchaseReceipt/cac:PurchaseReceiptLine/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`: master data copied into a receipt — refuted: warranty, fixing and maintenance information is useful to the end buyer of a retail sale.
