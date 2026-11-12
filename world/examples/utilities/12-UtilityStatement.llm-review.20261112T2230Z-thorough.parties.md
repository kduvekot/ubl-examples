# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### utilities/12#F1 · Medium · CustomerParty repeats the receiver although it is defined for a buyer different from the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Here the customer is the receiver (same register number), so the condition of the definition is not met. `03-UtilityStatement.xml` uses the element as defined (receiver Castrano Logistics, customer Valdara Industries). The same pattern occurs in 01, 05, 08 and 12 of this flow.
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a) remove `CustomerParty` from this statement (preferred: the definition makes its absence mean that the receiver is the buyer); (b) keep it only if the story gives the statement a different receiver.
- Needs decision: no

### utilities/12#F2 · Low · Registration dates on the world's default date; the telecom operator described as a small enterprise
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`), Selanu Telecom and Velumi Trading among them, while every other registration date is used by one company only; the shared New Year's Day looks like a default value, not the companies' story (no-fillers rule). For Selanu Telecom, `SMALL` ("Small enterprise") is also questionable: it runs the island's business lines, a mobile data service and roaming agreements, which suggests a national operator rather than a small firm; on a small island this may still be intended.
- Condition: both companies' registration dates are dates of their own histories (or absent), and Selanu Telecom's size fits what the story makes of it, the same in every example.
- Options: (a) give each company a registration date of its own and review the operator's size (preferred); (b) drop the elements where the documents do not need them.
- Needs decision: yes

### utilities/12#F3 · Low · Receiver's customs trader number in a telecom statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`
- Why: Velumi's customs trader number has no use in a domestic telecom document (island lines, data and roaming, no goods). It is part of Velumi's party data repeated in every example that carries it.
- Condition: the customs trader number appears here only with a use in this document.
- Options: (a) drop it here (preferred); (b) keep it only with a stated reason.
- Needs decision: no

### utilities/12#F4 · Low · Receiver's contact: purchasing with a sales job title and department
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the contact's name says purchasing, its job title and department say customer service in Sales; they contradict each other. For telecom bills Velumi receives, purchasing (or accounts payable) fits, the sales side does not. The contact is the same in every example with Velumi's full data.
- Condition: name, job title and department of Velumi's contact agree, and the function fits the role of receiving the telecom statement and bill.
- Options: (a) a purchasing job title and department, or an accounts payable contact (preferred); (b) drop the job title and department.
- Needs decision: no

### utilities/12#F5 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cbc:SubscriberID` = `ST-C-1077`
- Why: `SubscriberID` identifies the subscriber ("An identifier for the subscriber responsible for the consumption at this consumption point"), but holds the contract's number, the same as `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cac:Contract/cbc:ID` = `ST-C-1077`. Whether the world treats the subscription number and the contract number as one is a story question.
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a) a customer number of Velumi at Selanu Telecom (preferred); (b) record that the contract number serves as the subscriber number.
- Needs decision: yes

## Checked and consistent
- Selanu Telecom and Velumi Trading are described identically in 12–14 (and in the other examples with their full data, apart from the en-XB renderings outside this flow); neither carries a tax scheme, matching "No general sales tax" in the tax categories.
- Sender, `UtilitySupplierParty`, receiver, subscriber and `UtilityCustomerParty` match the parties of the parent invoice `13-Invoice.xml` (`13-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`), with the same register numbers.
- The consumption point address equals Velumi's postal address (Reef Street 16, Port Wrenfield / Selanu), matching "Office of Velumi Trading"; the Lisavan and en-XL renderings carry their tags; Lisavu addresses have no postal zone, consistently, and use the delivery-point register.
- ISIC codes against `world/codelists/sources/isic`: 6110 (wired telecommunications activities) for Selanu Telecom, 4649 (wholesale of other household goods) for Velumi.
- The number called in Bayvarra, `+999 2 7121 474 274`, is the contact telephone of a Bayvarran party in 78 places of the world (`grep -rc --include='*.xml' '<cbc:Telephone>+999 2 7121 474 274'`), so the call goes to a party that exists.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:RoamingPartnerName` = `Lumeport mobile network`: a roaming partner not described as a party was questioned. Refuted: UBL defines only a name for it, and a network name, not a company name, is what a roaming record shows.
- `/UtilityStatement/cac:SenderParty/cac:PartyName/cbc:Name` = `Selanu Telecom`: the sender's contact "Business accounts" in customer service was checked against the role; it fits the supplier of business lines.
