# LLM review: 06-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/06-Invoice.xml`, Git blob `a42ab090a50a199d6ef007b111b5c77252c9f943` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/06#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/06#F2 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

### utilities/06#F3 · Low · Customer's marketing data the invoice does nothing with
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Brightmarket's logo, online shop and social media profile have no use in a water invoice it receives; they are part of the block repeated in all 41 examples with Brightmarket's full data.
- Condition: logo, additional web site and social media profile appear in this invoice only with a use in it.
- Options: (a) drop them here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/06#F4 · Low · Customer's contact: buying office with a sales job title and department
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: name (buying office) and job title and department (customer service, Sales) contradict each other, and the accounting customer's contact should be the one who receives and settles the invoice (accounts payable), not Brightmarket's sales side. The contact is the same in all 41 examples with Brightmarket's full data.
- Condition: name, job title and department of the accounting customer's contact agree, and the function deals with incoming invoices or utilities purchasing.
- Options: (a) an accounts payable contact, or a purchasing job title and department for the buying office (preferred); (b) drop the job title and department.
- Needs decision: no

## Checked and consistent
- Supplier, seller, accounting customer and buyer are the parties of statement `05-UtilityStatement.xml` with the same register numbers, and are described as in 05 and 07.
- `BuyerCustomerParty` and `SellerSupplierParty` repeat the accounting parties; their definitions ("The buyer.", "The seller.") carry no condition, so stating them follows the rule that nothing is implied by absence.
- The payee account `XB21BLUM38010004189160` is named "Coastal State Water Company Ltd", the supplier's registration name; it is the same payee account in 07, 09 and 10; branch `380100` matches the account digits (BLUM 3801 00…).
- The collection line names the party it collects for: Lumeport Public Works Department, register number `20410548`, the same party and number as in 09, 11 and in the contest flow.

## Considered and refuted
- `/Invoice/cac:CollectionInvoiceLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`: the beneficiary repeating the `CollectedForParty` was suspected as a filler. Refuted: the definitions state two different facts ("for whom the associated transaction is ultimately intended or who derives benefit from it"; "on whose behalf this item or amount is collected"), and both are true of the city's works department here.
- `/Invoice/cac:CollectionInvoiceLine/cbc:Note` = `Collected for the city of Lumeport and paid on to it.`: the note names the city, the party its works department. Refuted: the department is the city's body that charges the sewage levy; naming the department as the party and the city in the text is consistent.
- `/Invoice/cac:CollectionInvoiceLine/cac:CollectedForParty/cac:PartyIdentification/cbc:ID` = `20410548`: a public department in a business register scheme was suspected. Refuted for this review: the department is identified with this scheme in every example of the world (127 occurrences of the name), so whether public bodies belong in that register lies with the world's identifier rules, not with this invoice.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`: a real GLN was suspected. Refuted: GS1 prefix 952 is reserved for demonstrations and examples (own knowledge), check digit valid.
