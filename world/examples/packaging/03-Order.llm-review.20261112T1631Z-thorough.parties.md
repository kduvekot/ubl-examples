# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/03-Order.xml`, Git blob `4c3acea07de9e59031f62d8970fa32ff7a492ca6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### packaging/03#F1 · Medium · LocaleCode holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) is the language, already given in Language/ID, not a locale (language in a region). The same value occurs 362 times in 213 examples (Grep over `*.xml`).
- Condition: LocaleCode names a locale (language and region) or is absent, for both parties.
- Options: (a) preferred: a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### packaging/03#F2 · Low · The buyer's contact contradicts itself: "Purchasing" in the sales department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact/JobTitle is "The job title or function of this contact" and Department "The department where this contact works". The name and e-mail address (`/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `purchasing@lumeporttextile.example`) say purchasing, which fits the buyer, but the job title and department say customer service in sales. The combination `Purchasing` / `Customer service officer` / `Sales` occurs in 52 contacts across the examples (lxml count over `*.xml`); job title and department look derived from the kind of party, not from the contact.
- Condition: name, job title and department of the buyer's contact agree with each other and with buying.
- Options: (a) preferred: a purchasing job title and department (e.g. buyer, Purchasing); (b) drop JobTitle and Department where only a functional mailbox is meant.
- Needs decision: no

### packaging/03#F3 · Low · Registration date 1996-01-01 shared by unrelated companies
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID". Both companies of this order, and 23 other companies in the registers of all three countries, carry exactly this date (271 occurrences in 181 examples, lxml count over `*.xml`), which looks like a default (IND5).
- Condition: each company's RegistrationDate is its own registration date in the story, or absent.
- Options: (a) preferred: individual dates from the companies' histories; (b) remove; (c) confirm 1996-01-01 as a story fact.
- Needs decision: yes

### packaging/03#F4 · Low · Party data a domestic order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-412603`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-412740`
- Why: Party/FinancialAccount is "The financial account associated with this party"; the order has no payment means or terms, so the seller's account is not used. The customs trader identifiers (schemeID `urn:ubl-examples:world:XB:customs-trader`) identify the parties to customs; both parties are in Lumeport and the garment bags are delivered DAP to the buyer's goods-in in Lumeport, so no customs formality is involved. These look copied from master data.
- Condition: every party detail in the order has a role in this domestic order.
- Options: (a) preferred: leave out the seller's FinancialAccount and the customs trader IDs here; (b) keep the customs IDs only where the order involves customs.
- Needs decision: no

## Checked and consistent
- Buyer Lumeport Textile Mill and seller Rivermouth Packaging carry the same register IDs, tax IDs (`CO-1237809`, `CO-1238220`), legal entities, addresses and endpoints as in `04-Invoice.xml` and (for Rivermouth) `01-Order.xml`/`02-Invoice.xml`; the seller block is identical to the one in `01-Order.xml`.
- The delivery party is the buyer (`20412603`), consistent with the DAP delivery to "Lumeport Textile Mill, goods-in".
- The seller's contact (order desk, sales) fits the seller.
- check_ids.py: the account `XB96BLUM38020504712805` has a valid check digit.
- Both are small private limited companies, active, in the Federal business register of Bayvarra; legal form text agrees with the code; both are registered for Coastal State sales tax, which fits their Lumeport addresses.

## Considered and refuted
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `1312`: a weaving mill buying garment bags — refuted because the mill also sells shirts in garment bags in this flow (`05-Order.xml`); ISIC gives the main activity only.
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Textile Mill, goods-in`: location without address or ID — refuted because the delivery party and the buyer's full address are in the order.
