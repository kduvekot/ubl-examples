# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/05-Order.xml`, Git blob `5869f45d431110e527ca796d40b56bf3f3390192` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### packaging/05#F1 · Low · Men's shirts charged to the buyer's "Garden department"
- XPath: `/Order/cbc:AccountingCost` = `Garden department`
- XPath: `/Order/cbc:AccountingCostCode` = `6120`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Cotton shirt`
- Why: UBL defines `Order/AccountingCost` as "The buyer's accounting cost centre, applied to the Order as a whole, expressed as text". Brightmarket Stores buys 600 men's shirts for resale; they are sold in its clothing department (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`), not in the garden department. "Garden department" is Brightmarket's cost centre in the furniture and retail flows as well (12 XML files, counted with `grep -rl --include='*.xml' '>Garden department<' world/examples`), so it looks like one cost centre copied into every purchase of the party.
- Condition: the cost centre of this order fits clothing (e.g. the clothing department), and the invoice `07-Invoice.xml` carries the same one.
- Options: (a, preferred) a clothing-department cost centre for Brightmarket, with its own code, in this order and its invoice; (b) drop `AccountingCost`/`AccountingCostCode` here.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `600` × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `14.5` = 8700.00 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `8700.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `8700.00`.
- Tax: `E`, 0 %, `RESALE` fits a retailer buying shirts for resale; both parties registered for STT in Coastal State; the invoice `07-Invoice.xml` uses the same treatment, and the retail sales (`08-PurchaseReceipt.xml`, `09-PurchaseReceipt.xml`) then charge STT at 6.5 %, which is what the resale exemption presupposes.
- Purchase against resale price: bought at 14.50, sold at 29.95 net of tax in the receipts; a plausible retail margin.
