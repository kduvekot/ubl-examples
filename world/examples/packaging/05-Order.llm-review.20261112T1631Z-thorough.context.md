# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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

### packaging/05#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) repeats the language of `Language/ID` and names no locale. Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/05#F2 · Low · Buyer's cost centre "Garden department" for men's shirts
- XPath: `/Order/cbc:AccountingCostCode` = `6120`
- XPath: `/Order/cbc:AccountingCost` = `Garden department`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Cotton shirt`
- Why: `AccountingCost` is "The buyer's accounting cost centre, applied to the Order as a whole". The store buys 600 men's shirts, which its receipts sell in "Clothing, first floor" (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`), but books them to the garden department. The pair 6120 / Garden department is Brightmarket's constant: it fits its garden benches (`furniture/08-Order.xml`, `retail/08-Order.xml`) and is repeated on every purchase, also on water bills (`utilities/06-Invoice.xml`); 12 examples carry it (`grep -rl --include='*.xml' '<cbc:AccountingCost>Garden department<'`).
- Condition: the order's cost centre is the store's clothing (or a general merchandise) cost centre, or absent.
- Options: (a) preferred: a clothing department cost centre, because the receipts already place the shirts there; (b) leave it out.
- Needs decision: no

### packaging/05#F3 · Low · Contacts do not fit the roles
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- Why: The buyer's contact is a buying office placed in Sales as customer service officer (name and department contradict each other). The seller's contact is the mill's purchasing contact, the one it uses as a buyer in `03-Order.xml`; in this order the mill sells, so its contact should be its sales or order desk. Every party carries one contact whatever its role: 89 examples have a `Purchasing` or `Buying office` contact in Sales (XPath count).
- Condition: the buyer's contact describes a buying function, the seller's a selling one, each with agreeing name, title and department.
- Options: (a) preferred: role-specific contacts per party (purchasing for the buyer role, sales/order desk for the seller role).
- Needs decision: no

### packaging/05#F4 · Low · Buyer's marketing data in an order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: The buyer's logo reference, online shop and photo-sharing profile have no use in a purchase order to its supplier; they are Brightmarket's master data (they belong on its receipts, `08-PurchaseReceipt.xml`, where the customer sees them). SocialMediaProfile appears in 41 examples of many document types (XPath count over `world/examples/*/*.xml`).
- Condition: the order carries none of these, or a reason to (e.g. the supplier is to print the logo on labels).
- Options: (a) preferred: leave them out of the order.
- Needs decision: no

## Checked and consistent
- Arithmetic: 600 × 14.5 = 8700.00 = line and totals; tax 0.
- Item: "in a garment bag" links the shirts to the garment bags of `03-Order.xml`; HS 620520 and CPC 28232 describe men's cotton shirts, not knitted.
- Exemption "Sale for resale or manufacture" fits a retailer buying stock.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode`: origin XB while the cotton is "grown on Lisavu" — refuted because origin is where the shirt is made (woven and sewn by the Lumeport mill); the property says where the fibre comes from.
- `/Order/cac:DeliveryTerms/cbc:ID`: DDP for a delivery within Lumeport — refuted because Incoterms may be used domestically; DDP says the seller delivers to the store at its cost.
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName`: brand `Lumeport` equal to the city — refuted because a mill naming its brand after its town is plausible.
