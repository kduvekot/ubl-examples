# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/08-UtilityStatement.xml`, Git blob `2ad70d0c87bdcb2a69e49f63c3882af20185d03e` (committed)
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

### utilities/08#F1 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". `en` is an ISO 639 language code (the `listID` says so), the same value as `Language/ID`; it names no locale. A locale is a language in a region (the world's own language tags show what one looks like: `en-XB` in the `languageID` attributes of other examples). The value occurs 362 times over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en'`), in every Bayvarran party with full data.
- Condition: `LocaleCode` either holds a locale (language and region, from a list that defines locales) with a matching `listID`, or is absent.
- Options: (a) drop `LocaleCode` where the party has no locale to state beyond its language (preferred: `Language/ID` already says English); (b) use a locale value such as `en-XB` with a list that defines it.
- Needs decision: no

### utilities/08#F2 · Medium · CustomerParty repeats the receiver although it is defined for a buyer different from the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Here the customer is the receiver (same register number), so the condition of the definition is not met. `03-UtilityStatement.xml` uses the element as defined (receiver Castrano Logistics, customer Valdara Industries). The same pattern occurs in 01, 05, 08 and 12 of this flow.
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a) remove `CustomerParty` from this statement (preferred: the definition makes its absence mean that the receiver is the buyer); (b) keep it only if the story gives the statement a different receiver.
- Needs decision: no

### utilities/08#F3 · Low · The state's water company described as a small enterprise registered on the world's default date
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Coastal State Water Company supplies drinking water in the Coastal State (shops and households of Lumeport in this flow, with its own meter network). A water utility serving a state's capital is a large organisation; `SMALL` ("Small enterprise") is implausible for it. 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), while every other registration date is used by one company only, so both values look like a default description, not the company's story (no-fillers rule). The description is the same in all 7 examples of this flow that carry it.
- Condition: size and registration date of the water company are values of its own story (or absent), the same in every example.
- Options: (a) give the company a size that fits a state water utility (medium or large) and a registration date of its own (preferred); (b) drop the two elements where the documents do not need them.
- Needs decision: yes

### utilities/08#F4 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-311790`
- Why: `SubscriberID` identifies the subscriber ("An identifier for the subscriber responsible for the consumption at this consumption point"), but holds the supply contract's number, the same as `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `CSW-C-311790`. Whether the world treats the subscription number and the contract number as one is a story question.
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a) a customer number of Robin Ashdale at the water company (preferred); (b) record that the contract number serves as the subscriber number.
- Needs decision: yes

## Checked and consistent
- Robin Ashdale (receiver, customer, subscriber, utility customer) is described identically in 08–11 and in the retail and packaging examples that carry the person (name, residential address Gull Lane 57, Old town, 38516 Lumeport, `LUM-ADR-934215`, account `XB64BLUM38010007251840`).
- A private person is described without legal entity, tax scheme or register identifier, and with `Person` first and family name: fitting a household customer.
- The consumption point address equals Robin's postal address and is typed `RESIDENTIAL`, with subscriber type Household (`HH`) and a flat's water meter.
- Sender, signatory and `UtilitySupplierParty` are Coastal State Water Company with register number `20412192`, the supplier of the parent invoice `09-Invoice.xml`.

## Considered and refuted
- `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`: a private bank account in a consumption statement was suspected as copied master data. Refuted: the statement says the on-account payments and the bill are collected by direct debit (`/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`), and the account shows the household which account is debited; it is the mandate's account in invoice 09.
- `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Robin Ashdale`: a party without identifier was questioned. Refuted: a household subscriber has no register number; the name, the subscriber ID and the address identify it.
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `WATER`: refuted as in 05: UBL defines it in `UtilityItem` as "The code identifying for the service type".
