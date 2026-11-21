# LLM review: 04-Invoice.xml

Flow: lpg (9924528384) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/lpg/04-Invoice.xml`, Git blob `0ba020e6b06003ac0195266ab8c1416c49b9994f` (committed)
- Last commit changing the example: 3bcd24f4 2026-11-21 Company figures, legal forms, bridge heights and the languages' own names (O279)
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### lpg/04#F1 · Low · Which state's sales tax applies to propane delivered from the Northern Territory into Coastal State
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cac:JurisdictionRegionAddress/cbc:CountrySubentity` = `Northern Territory`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Coastal State Water Company, district heating plant, Reservoir Road, Lumeport`
- XPath: `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `6.5`
- Why: the tax is a state sales tax (`STT`, levied by a state or territory). The seller is registered for it in the Northern Territory; the goods are delivered in Coastal State (`XB-CO`). Under destination-based sales taxes the delivery state's tax would apply, under origin-based ones the seller's; the invoice does not say in which jurisdiction the 6.5 % is charged (the tax category carries no jurisdiction). I could not settle this from the XML alone (the same rate 6.5 % occurs in other flows).
- Condition: the invoice charges the sales tax of the state the world's rules assign to an interstate delivery, and it is clear which state that is.
- Options: (a, preferred) confirm the world's rule (origin or destination) and, if destination, show the seller's registration in Coastal State or the Coastal State tax; (b) if origin, nothing changes.
- Needs decision: yes

### lpg/04#F2 · Low · Accounts receivable reachable "every day, around the clock" on the plant's number
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Note` = `Every day, around the clock`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38522 68330`
- Why: `Contact/Note` describes "the circumstances under which this contact can be used". A credit controller in the finance department is not available around the clock; the telephone number is the same as that of the gas sales contact (`01-Order.xml:/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`) and the despatch office (`02-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Telephone`), with the same note, which looks copied from the plant's operations contact.
- Condition: the accounts-receivable contact's note and number fit a finance function (office hours, its own line), or the note is absent.
- Options: (a, preferred) office hours and a number of its own; (b) leave out the note.
- Needs decision: no

### lpg/04#F3 · Low · The customer's contact on the invoice is customer service, not accounts payable
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- Why: the Contact of `AccountingCustomerParty` is who handles the invoice and its payment for the buyer; the water company's customer service for its own customers is not that function. The same contact is used for the party in every role of the flow.
- Condition: the accounting customer's contact is an accounts-payable function, or there is none.
- Options: (a, preferred) an accounts-payable contact; (b) leave out the contact.
- Needs decision: no

### lpg/04#F4 · Low · Gullhaven telephone prefix "38522" overlaps Lumeport's "38"
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38522 68330`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 2 38 9310 7518`
- Why: as in `01-Order.xml` (lpg/01#F2); the Gullhaven bank branch code `385220` (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID`) follows the same pattern.
- Condition: one prefix-free numbering plan for Gullhaven and Lumeport.
- Options: as lpg/01#F2.
- Needs decision: yes

## Checked and consistent
- Arithmetic: 20.18 TNE × 560 XBL = 11300.80; 6.5 % = 734.552 → 734.55; 11300.80 + 734.55 = 12035.35 = payable amount; penalty 1.5 % of 12035.35 = 180.53.
- Dates: issued 2026-06-11 (Thursday); +30 days = 2026-07-11 (Saturday), due date moved to Monday 2026-07-13; penalty period from 2026-07-14. Actual delivery 2026-06-10 matches the waybill's planned arrival and the despatch advice.
- References: `/Invoice/cac:OrderReference/cbc:ID` resolves to `01-Order.xml`, `/Invoice/cac:DespatchDocumentReference/cbc:ID` to `02-DespatchAdvice.xml`; the weighbridge ticket `1700001734` is an external document, typed and dated on the day of loading, and explains the weighed 20.18 t.
- Check digits: `RF669000034662` (ISO 11649) and `XB45BLUM38522004817534` (mod 97) are correct (`check_ids.py`).
- Price and item agree with the order; the payee account is the supplier's own.
