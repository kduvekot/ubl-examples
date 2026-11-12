# LLM review: 01-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/01-Order.xml`, Git blob `ddc64baa43ff662f7332461675890f01136aaac2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/01#F1 · Low · The seller's bank account in a buyer's order that pays nothing
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: UBL defines `Party/FinancialAccount` as "The financial account associated with this party". The Order is issued by the buyer (Valdara Industries) and carries no `PaymentMeans` or `PaymentTerms`; nothing in the document is paid to or from this account. The seller's account, with its branch and the full address of the Bank of Lumeport, looks copied from Rivermouth Packaging's master data. Payment instructions belong in the invoice, and `02-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805` already carries them there. The same account is in the seller party of `03-Order.xml` (Rivermouth Packaging's other order).
- Condition: the Order carries a party financial account only if the order itself uses it (e.g. an agreed payment instruction or prepayment that the order states).
- Options: (a, preferred) remove `cac:FinancialAccount` from the seller party in the order: the invoice gives the payment account; (b) keep it only with a business reason the order states, e.g. payment terms that require prepayment to this account.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `480` kg × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `3.1` per `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:BaseQuantity` = `1` kg = 1488.00 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `1488.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `1488.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `1488.00` (no tax, no allowances).
- Tax: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `1488.00` equals the line total; category `G` (free export item) at 0 % with reason `EXP` "Export outside Bayvarra" fits a sale by a Bayvarran seller (Coastal State, state sales tax `STT`) to a buyer in Urvania; the tax scheme matches the seller's `PartyTaxScheme` (`STT`, state level). Order and invoice agree (`02-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`).
- Currency: `/Order/cbc:DocumentCurrencyCode` = `XBL` (seller's currency), all amounts in XBL; the order and the invoice use the same price and currency.
- Account check digits: `check_ids.py` reports the IBAN-like account and the ISIN as valid.

## Considered and refuted
- `/Order/cbc:AccountingCost` = `Raw materials and parts`: suspected a cost centre that does not fit stretch film, and `/Order/cbc:AccountingCostCode` = `3100` equal to the buyer's ISIC code `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100` — refuted because pallet-wrapping film is a production consumable a furniture maker can book under raw materials and parts, and the cost code is the buyer's own chart of accounts; the equality with the ISIC code is a coincidence with no contradiction (the other buyers in the flow use codes 2200 and 6120, unrelated to their ISIC codes).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`: the UBL definition reads "The number of shares in the capital stock of a corporation", but the element is an Amount with a currency — refuted because an Amount type cannot hold a count of shares; the value is the share capital in ferra (XUF, 0 decimals), the only reading the data type allows. The mismatch lies in UBL's own definition, not in the example.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:CurrencyCode` = `XUF` against the document currency XBL: refuted because it is the buyer's own VAT reporting currency in Urvania; the order's tax (Bayvarran STT) is in XBL.
