# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/03-UtilityStatement.xml`, Git blob `a8d48fa5c4e614ea05c1521143210974ea8bf6f9` (committed)
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

### utilities/03#F1 · High · Castrano Logistics named as subscriber of a subscription that is Valdara's
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: `SubscriberParty` is "The Party that is the subscriber of the utility" (in `SubscriberConsumption`: "The Party who is subscribed to the utility"), and the consumption point's `SubscriberID` is "An identifier for the subscriber responsible for the consumption at this consumption point". The subscriber ID here is `FE-C-0047120`, and the supply is "under the customer's contract" (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cbc:Description` = `The supply under the customer's contract.`) with Valdara as utility customer. In `01-UtilityStatement.xml` the same subscriber ID belongs to Valdara (`01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberParty/cac:PartyName/cbc:Name` = `Valdara Industries`). One subscription therefore has two different subscribers in the flow, and within this statement the subscriber party contradicts the subscriber ID and the utility customer. Castrano is the occupant of the warehouse that consumes the electricity, not the party subscribed to the supply.
- Condition: the subscriber of the warehouse consumption point is the same party in the subscriber elements, the subscriber ID, the utility customer and statement 01; Castrano Logistics appears only in a role that fits it (receiver of the statement, occupant or consumer of the point).
- Options: (a) make Valdara the `SubscriberParty` (both places) and keep Castrano as receiver, with the consumption point's description saying it is Castrano's warehouse (preferred: it matches the contract, invoice 02 and statement 01); (b) if the story wants Castrano to hold its own subscription, give it its own subscriber ID and contract, and then Valdara is no longer the utility customer of this point, which changes invoice 02's line 2.
- Needs decision: yes

### utilities/03#F2 · Medium · Province of Ferrano held in Region instead of CountrySubentity
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, which is `CountrySubentity` ("the political or administrative division of a country … such as the name of its county, province, or state"). The Bayvarran addresses of the world use `CountrySubentity`. The value occurs 219 times in `Region` over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano'`).
- Condition: no Urvanian address carries a province in `Region`; it is in `CountrySubentity`, or the story makes it a non-administrative region.
- Options: (a) move the value to `CountrySubentity` (preferred); (b) keep `Region` only if the province is an economic or geographic region in the story.
- Needs decision: no

### utilities/03#F3 · Low · Castrano's registration date is the date shared by 25 companies of the world
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". 25 different companies of the world are registered on 1 January 1996 (counted over the `PartyLegalEntity` elements of `world/examples/*/*.xml`: Castrano Logistics, Coastal State Water Company, Selanu Telecom, Velumi Trading, Port of Lumeport and 20 others), while every other date in the world is used by one company only. A New Year's Day registration shared by a quarter of the world's companies looks like a default value, not a fact of the story (no-fillers rule).
- Condition: Castrano Logistics' registration date is a date from its own history (or the element is absent).
- Options: (a) give the company a registration date of its own, consistent in every example (preferred); (b) drop the date where the documents do not need it.
- Needs decision: yes

### utilities/03#F4 · Low · Contacts of the receiver and the customer do not fit their roles
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Castrano's contact is called "Warehouse office" but has the job title of a customer service officer in Sales; name, job title and department disagree. A warehouse office is a fitting receiver of a statement about the warehouse's electricity, the sales department is not. Valdara, as the buyer of the supply, is reachable here only through its own sales order desk, which handles Valdara's customers, not its energy contract. Both contacts are identical in every example with the parties' full data (Castrano: 7, Valdara: 75).
- Condition: each contact's name, job title and department agree, and the function fits the party's role in this statement (receiver of a consumption statement; buyer of the supply).
- Options: (a) give Castrano's warehouse office a fitting job title and department, and Valdara a utilities purchasing or accounts payable contact (preferred); (b) drop the job title and department where only the functional name is meant.
- Needs decision: no

### utilities/03#F5 · Low · Customer's master data the statement does nothing with
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the customs trader number and the share listing of Valdara have no use in a statement of a warehouse's electricity consumption. They are part of the block repeated in all 75 examples with Valdara's full data.
- Condition: every identifier and listing in the customer party has a use in this statement, or is absent.
- Options: (a) drop them here (preferred); (b) keep them only with a stated reason.
- Needs decision: no

### utilities/03#F6 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- Why: `SubscriberID` identifies the subscriber ("An identifier for the subscriber …"), but holds the supply contract's number (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`). A contract number identifies the contract, not a party; whether the world treats them as one is a story question. (Who the subscriber is at all is F1.)
- Condition: `SubscriberID` holds an identifier of the subscriber, or the world states that the contract number is the subscriber number.
- Options: (a) a customer number of the subscriber at Ferrano Energy (preferred); (b) record that the contract number serves as the subscriber number.
- Needs decision: yes

## Checked and consistent
- `ReceiverParty` Castrano Logistics differs from `CustomerParty` Valdara, so `CustomerParty` meets its definition "The buyer, if different from the receiver of the document".
- Castrano Logistics is described identically in all 7 examples with its full data (SRU, size SMALL, 100 % owned by Valdara Industries, ISIC 5210 warehousing and storage, address Via del Magazzino 24, 4130 Ferrano).
- The consumption point address equals Castrano's postal address; the meter `FE-M-881377` is the one of `02-Invoice.xml` line 2, whose purchase reference says "Warehouse of Castrano Logistics".
- The customer's `ServiceProviderParty` (Castrano, warehousing and despatch) matches the receiver's register number `XU-R-104411` and explains why the warehouse's consumption runs on Valdara's contract.
- Ferrano Energy as sender and `UtilitySupplierParty` agrees with `02-Invoice.xml` and statement 01.

## Considered and refuted
- `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: suspected as a default size. Refuted: a single-site warehousing subsidiary is plausibly a small enterprise.
- `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:ShareholderParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`: suspected as unrelated master data. Refuted: the ownership explains why the subsidiary's warehouse is supplied under the parent's contract and why the statement goes to it.
- `/UtilityStatement/cac:CustomerParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`: suspected as copied master data. Refuted for this statement, together with its service provider (see "Checked and consistent").
