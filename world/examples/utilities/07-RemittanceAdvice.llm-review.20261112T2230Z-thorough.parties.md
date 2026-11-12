# LLM review: 07-RemittanceAdvice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/07-RemittanceAdvice.xml`, Git blob `ff1d21cc9e8ef3dfbfbdbfde835f54314d67116b` (committed)
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

### utilities/07#F1 · Medium · Brightmarket's remittance advice numbered in Valdara's series, and its payer references carry Ferrano's invoice number
- XPath: `/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`
- XPath: `/RemittanceAdvice/cbc:PaymentOrderReference` = `BS-PAY-26-0313`
- XPath: `/RemittanceAdvice/cbc:PayerReference` = `BS-0313`
- Why: the document `ID` is "An identifier for this document, assigned by the sender". The sender is Brightmarket Stores (accounting customer and signatory, whose own references start `BS-`), but the ID has the `VI-` prefix of Valdara Industries and is exactly the ID of Valdara's remittance advice `04-RemittanceAdvice.xml` (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:ID` = `VI-RM-26-0316`); `14-RemittanceAdvice.xml` has it a third time. Three documents of one collaboration (`UTILITIES-2026-01`) from three different senders share one ID, and two of them carry another company's prefix. The payment order and payer references end in `0313`, the number of Ferrano Energy's invoice FE-INV-26-0313 that 04 pays (`04-RemittanceAdvice.xml:/RemittanceAdvice/cbc:PaymentOrderReference` = `VI-PAY-26-0313`), while this advice pays CSWC-INV-26-0317. The identifiers look copied from 04 with the prefix partly changed.
- Condition: the remittance advice's ID belongs to Brightmarket's own numbering and differs from the IDs of 04 and 14; the payer references are Brightmarket's own and do not echo another party's invoice number.
- Options: (a) a `BS-RM-…` document ID and payment references numbered for this payment (preferred); (b) any other numbering of Brightmarket's, as long as it is not Valdara's series.
- Needs decision: no

### utilities/07#F2 · Medium · A language code in LocaleCode
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/07#F3 · Low · Payer's marketing data the remittance advice does nothing with
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: logo, online shop and social media profile play no part in telling the water company which invoice a payment settles; they are part of the block repeated in all 41 examples with Brightmarket's full data.
- Condition: they appear in this remittance advice only with a use in it.
- Options: (a) drop them here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/07#F4 · Low · Payer's contact: buying office with a sales job title and department
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: name and job title/department contradict each other, and the payer's contact on a remittance advice is the one who answers for the payment (accounts payable, treasury), not the sales side. The contact is the same in all 41 examples with Brightmarket's full data.
- Condition: name, job title and department agree, and the function deals with payments.
- Options: (a) an accounts payable contact for Brightmarket in the payment documents (preferred); (b) drop the job title and department.
- Needs decision: no

### utilities/07#F5 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/RemittanceAdvice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

## Checked and consistent
- Payer Brightmarket Stores and payee Coastal State Water Company are the accounting customer and supplier of the invoice paid, `06-Invoice.xml`, with the same register numbers, and are described as in 05 and 06.
- `SignatoryParty` is Brightmarket, the issuer; the line's accounting parties repeat the header parties.
- Payer account `XB48BLUM38010001570935` is named "Brightmarket Stores Corp" (its registration name) and is Brightmarket's account in the furniture flow as well; payee account `XB21BLUM38010004189160` is the one invoice 06 gives. Both are at the Bank of Lumeport, branch `380100`, as the account digits say.

## Considered and refuted
- `/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`: a real GLN was suspected. Refuted: GS1 prefix 952 is reserved for demonstrations and examples (own knowledge), check digit valid.
