# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/05-UtilityStatement.xml`, Git blob `f5bb8506980bfe0a7e311a1ed3ba8b85f0c771d7` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
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

### utilities/05#F1 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/05#F2 · Medium · CustomerParty repeats the receiver although it is defined for a buyer different from the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Here the customer is the receiver (same register number), so the condition of the definition is not met. `03-UtilityStatement.xml` uses the element as defined (receiver Castrano Logistics, customer Valdara Industries). The same pattern occurs in 01, 05, 08 and 12 of this flow.
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a) remove `CustomerParty` from this statement (preferred: the definition makes its absence mean that the receiver is the buyer); (b) keep it only if the story gives the statement a different receiver.
- Needs decision: no

### utilities/05#F3 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own reservoir address and a meter network). Water utilities serving a state's capital are large organisations; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

### utilities/05#F4 · Low · Receiver's marketing data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: the receiver's logo, online shop and social media profile matter where Brightmarket presents itself to its own customers (retail documents), not in a water statement it receives. They are part of the block repeated in all 41 examples with Brightmarket's full data.
- Condition: logo, additional web site and social media profile appear in this statement only with a use in it.
- Options: (a) drop them here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/05#F5 · Low · Receiver's contact: buying office with a sales job title and department
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name says buying office, its job title and department say customer service in Sales; they contradict each other. For a statement on the shop's water supply, the buying office (or facilities, accounts payable) is a fitting addressee, the sales department is not. The contact is the same in all 41 examples with Brightmarket's full data.
- Condition: name, job title and department of the receiver's contact agree, and the function fits the receiver of a utility statement.
- Options: (a) a purchasing job title and department for the buying office, or a facilities or accounts payable contact (preferred); (b) drop the job title and department.
- Needs decision: no

### utilities/05#F6 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-260118`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-260118`
- Why: `SubscriberID` identifies the subscriber ("An identifier for the subscriber responsible for the consumption at this consumption point"), but holds the supply contract's number, the same as `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-260118`. Whether the world treats the subscription number and the contract number as one is a story question.
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a) a customer number of Brightmarket at the water company (preferred); (b) record that the contract number serves as the subscriber number.
- Needs decision: yes

## Checked and consistent
- Coastal State Water Company and Brightmarket Stores are described identically in 05–07 (and Coastal in 08–11), and Brightmarket as in the 41 other examples with its full data.
- Sender, `UtilitySupplierParty`, receiver, subscriber and `UtilityCustomerParty` match the parties of the parent invoice `06-Invoice.xml` (`06-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`), with the same register numbers.
- The consumption point address (Market Street 50, Old town, 38515 Lumeport, Coastal State, `XB-CO`) equals Brightmarket's postal address, matching "Shop, Lumeport"; province and state are in `CountrySubentity` with their code.
- ISIC codes against `world/codelists/sources/isic`: 3600 (water collection, treatment and supply) for the water company, 4719 (other retail sale in non-specialized stores) for Brightmarket.
- The tax scheme of both parties is the Coastal State's sales tax (`STT`, `TaxLevelCode` `STATE`, jurisdiction Coastal State), matching their seats.

## Considered and refuted
- `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `9522610900002`: a real GLN was suspected. Refuted: the GS1 prefix 952 is reserved by GS1 for demonstrations and examples (own knowledge of the GS1 prefix list), and the check digit is valid (`check_ids.py`); the GLN is Brightmarket's identification convention (GS1) in the world.
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Limited company (private)`: a privately formed company for a state's water supply was questioned. Refuted: a utility can be a private limited company (possibly owned by the state); nothing in the flow says otherwise.
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `WATER`: a utility type code in a subscriber type was suspected. Refuted: UBL defines this element in `UtilityItem` as "The code identifying for the service type".
