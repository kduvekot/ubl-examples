# LLM review: 05-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### packaging/05#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already in Language/ID, not a locale. The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/05#F2 · Low · The contacts do not fit the roles: a purchasing contact for the seller, a sales job for the buying office
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Party/Contact is "The primary contact for this party". Lumeport Textile Mill is the seller here, but its contact is its purchasing mailbox, the one it used as buyer in `03-Order.xml` (`03-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`); orders for shirts go to its sales side. Brightmarket's buying office fits the buyer, but its job title and department (customer service in sales) contradict the name and e-mail `buying@brightmarket.example`. Across the examples, `Buying office`/`Customer service officer`/`Sales` occurs 41 times and `Purchasing`/`Customer service officer`/`Sales` 52 times (lxml count over `*.xml`): each party has one contact, used in every role.
- Condition: the seller's contact is a sales or order contact of Lumeport Textile Mill; the buyer's contact has a name, job title and department that agree and belong to buying.
- Options: (a) preferred: give each party a contact per role it plays (sales and purchasing), with matching job titles and departments; (b) drop JobTitle and Department where only a functional mailbox is meant.
- Needs decision: no

### packaging/05#F3 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". 25 companies in three countries' registers share exactly this date (271 occurrences in 181 examples, lxml count over `*.xml`), while Brightmarket in the same order has its own (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1979-02-14`). It looks like a default (IND5).
- Condition: Lumeport Textile Mill's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: an individual date; (b) remove; (c) confirm as a story fact.
- Needs decision: yes

### packaging/05#F4 · Low · Marketing and customs data the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- Why: LogoReferenceID ("An identifier for this party's logo"), AdditionalWebSite ("An additional web site associated with this party") and SocialMediaProfile ("A social media profile associated with this party") describe how Brightmarket presents itself to consumers; a purchase order to a supplier does nothing with them. The customs trader ID of the seller has no use in a DDP delivery within Lumeport. All look copied from master data (the logo reference is in 41 examples, Grep for `BM-LOGO-2024` over `*.xml`).
- Condition: every party detail in the order has a role in this order.
- Options: (a) preferred: keep the logo, web shop and social media profile for documents Brightmarket issues to consumers (the purchase receipts of this flow) and leave them out here, together with the customs ID; (b) state in the example why the order carries them.
- Needs decision: no

### packaging/05#F5 · Low · The goods-in point is not identified although it has a GLN elsewhere
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- Why: Location identifiers should be used where the same place is identified elsewhere. Brightmarket identifies its goods-in with GLN `9522610900019` in other flows (`furniture/01-RequestForQuotation.xml:/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`, named `Brightmarket Stores, goods-in`; also `retail/08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`). This order, which the buyer issues and which names the same place in words, gives neither that GLN nor an address for it; the delivery is identified only through the delivery party.
- Condition: the delivery place (in Delivery or DeliveryTerms) carries the goods-in GLN, or the example says why it is not used.
- Options: (a) preferred: add a Delivery/DeliveryLocation with the goods-in GLN, as in `retail/08-Order.xml`; (b) leave as is if the textile mill is not meant to know Brightmarket's GLNs (Lumeport Textile Mill uses its own numbers rather than GS1).
- Needs decision: no

## Checked and consistent
- Brightmarket Stores and Lumeport Textile Mill carry the same register IDs, tax IDs (`CO-1231233`, `CO-1237809`), legal entities, addresses and endpoints as in `06-DespatchAdvice.xml` and `07-Invoice.xml` (compared line by line) and, for the mill, `03-Order.xml`/`04-Invoice.xml`.
- The delivery party is the buyer (`20410411`), consistent with DDP to Brightmarket's goods-in.
- check_ids.py: GLN `9522610900002` has a valid check digit; its prefix 952 is the GS1 range for demonstrations and examples (own knowledge), so it cannot be mistaken for a real GLN.
- Brightmarket as a large public corporation with share capital, active, in the Federal business register; its industry class (other retail in non-specialised stores) fits a department store with clothing and garden departments.
- The buyer's item number `BM-778120` is the same number Brightmarket uses as seller in `08-PurchaseReceipt.xml` and `09-PurchaseReceipt.xml`.

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cbc:IndustryClassificationCode` = `1312`: a weaving mill selling shirts (ISIC 1410 would be apparel) — refuted because ISIC records the main activity and the mill weaves the cotton it makes the shirts from; the shirts are a downstream product of the same company.
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:TradePartyName/cbc:Name` = `Brightmarket`: trading name in an order — refuted because it is the name the store trades under and the brand the supplier delivers to.
