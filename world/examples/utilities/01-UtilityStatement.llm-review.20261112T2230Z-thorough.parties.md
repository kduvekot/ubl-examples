# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/01-UtilityStatement.xml`, Git blob `5afddf1d0c8c1838c6abd6e06e483af49cb2664f` (committed)
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

### utilities/01#F1 · Medium · Province of Ferrano held in Region instead of CountrySubentity
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Region` as "The recognized geographic or economic region or group of countries in which this address is located", and `CountrySubentity` as "the political or administrative division of a country in which this address is located, such as the name of its county, province, or state". "Province of Ferrano" names an administrative province, so it belongs in `CountrySubentity` (with `CountrySubentityCode` where the world has a list). The Bayvarran addresses of the world do exactly that (`CountrySubentity` = `Coastal State` with `XB-CO`), so the Urvanian ones are the odd ones out. The same value occurs 219 times in `Region` over `world/examples/*/*.xml` (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano'`), in every Urvanian address.
- Condition: no Urvanian address carries a province in `Region`; the province is in `CountrySubentity` (and its code in `CountrySubentityCode` if the world defines one), or, if the world's Urvanian provinces are not administrative divisions, the value says what kind of region it is.
- Options: (a) move the value to `CountrySubentity` in every Urvanian address (preferred: it is what the definition names, and it matches the Bayvarran addresses); (b) keep `Region` only if the story makes "Province of Ferrano" an economic or geographic region rather than an administrative one.
- Needs decision: no

### utilities/01#F2 · Medium · CustomerParty repeats the receiver although it is defined for a buyer different from the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Here the customer is the receiver (same party, same register number `XU-R-104274`), so the condition of the definition is not met. In `03-UtilityStatement.xml` the element is used as defined: the receiver is Castrano Logistics and `03-UtilityStatement.xml:/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`. The same pattern (customer = receiver) occurs in 05, 08 and 12 of this flow.
- Condition: `CustomerParty` is present only when the buyer differs from `ReceiverParty`.
- Options: (a) remove `CustomerParty` from this statement (preferred: the receiver already is the buyer, and the definition makes absence mean exactly that); (b) keep it only if the story gives the statement a receiver other than Valdara.
- Needs decision: no

### utilities/01#F3 · Low · Receiver's master data the statement does nothing with
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: a utility statement explains the consumption behind an electricity bill. Valdara's customs trader number, its share listing on the Ferrano Stock Exchange and its warehousing service provider (Castrano Logistics, with its `SellerContact` = "Key account desk") play no part in it: nothing in the statement is customs-related, traded or warehoused. The block is identical in all 75 examples that carry Valdara's full party data, which suggests it is copied master data. The service provider could explain why Castrano gets statement 03 on Valdara's contract, but this statement is about Valdara's own factory connection.
- Condition: every identifier, listing and service provider in the receiver party has a use in this statement, or is absent.
- Options: (a) drop the customs trader ID, the security listing and the service provider from this statement (preferred); (b) keep the service provider only if the statement is meant to show the warehouse arrangement, and then say so (e.g. in a note).
- Needs decision: no

### utilities/01#F4 · Low · Receiver's contact is the order desk in Sales, not someone who handles an electricity statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver of a utility statement is the customer of the energy supply; the useful contact is the person or desk that checks energy bills (accounts payable, facility or energy management). Valdara's contact is its own sales order desk with a customer service officer, i.e. the contact Valdara gives its own customers. It is the same contact in all 75 examples with Valdara's full data, whatever role Valdara has there.
- Condition: the receiver's contact is a function that deals with the energy supply or its bills, and name, job title and department agree with each other.
- Options: (a) give Valdara a contact for purchasing or accounts payable of utilities in this flow (preferred); (b) drop the contact if the electronic address is meant to be the only channel.
- Needs decision: no

### utilities/01#F5 · Low · SubscriberID holds the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047120`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `FE-C-0047120`
- Why: `SubscriberID` is "An identifier for the subscriber responsible for the consumption at this consumption point" (and, in `UtilityItem`, "An identifier for the subscriber to the utility"): it identifies a party. The value is the supply contract's number, the same as `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Contract/cbc:ID` = `FE-C-0047120`. A contract number identifies the contract, not the subscriber; whether the world treats the subscription number and the contract number as one is a story question.
- Condition: `SubscriberID` holds an identifier of the subscriber (e.g. Ferrano Energy's customer number for Valdara), or the world states that the contract number is the subscriber number.
- Options: (a) give the subscriber a customer number of its own (preferred: it keeps the two identifiers apart); (b) record that the contract number serves as the subscriber number in this world.
- Needs decision: yes

## Checked and consistent
- Ferrano Energy and Valdara Industries are described identically (identifiers, names, addresses, tax schemes, legal entities, contacts, electronic addresses) in 01–04 of this flow, and in every other example of the world that carries their full data (Valdara: 75 examples; Ferrano Energy: 8).
- `SenderParty` Ferrano Energy is the supplier of `02-Invoice.xml` (the parent document, `02-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`), and the receiver is its accounting customer.
- `UtilitySupplierParty` and `UtilityCustomerParty` carry the same register numbers as the sender and the receiver; `SubscriberParty` is Valdara, the holder of the contract, as `SupplierConsumption/Description` says.
- The consumption point address equals Valdara's postal address (Via delle Officine 17, postal zone 4120), fitting a factory at the company's seat; the Urvanian and en-XU renderings carry their language tags.
- Industry codes against the ISIC Rev.4 source in `world/codelists/sources/isic`: 3510 (electric power generation, transmission and distribution) for Ferrano Energy, 3100 (manufacture of furniture) for Valdara, which sells park benches in the retail and wood flows.
- ISIN `XU0001042501` has a valid check digit (`check_ids.py`); the market code `XFER` is not a MIC in `world/codelists/sources/iso10383/ISO10383_MIC.csv`.
- Legal forms: SUA (public limited company) with corporate stock and fully paid shares, size LARGE, both plausible for an energy supplier founded 1949 and a listed manufacturer.

## Considered and refuted
- `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: an Italian name under `languageID` `en-XU` was suspected as a wrong language tag. Refuted: street and city names are proper names, and the world uses these Italianate forms as the English names of Urvanian places consistently in every example; only the Urvanian rendering is translated.
- `/UtilityStatement/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`: the same suspicion. Refuted: it is the legal form's proper name with an English gloss in brackets.
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberTypeCode` = `ELEC`: a code from the utility type list in a subscriber type was suspected. Refuted: UBL defines this element in `UtilityItem` as "The code identifying for the service type", which electricity is; the subscriber's own type is given correctly at the consumption point (`IND`, Industrial).
- `/UtilityStatement/cac:ReceiverParty/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: a real ISO 6523 ICD was suspected. Refuted from my own knowledge of the ICD register: ICDs are allocated in sequence and have not reached 0990; the world uses it for its own identification agency.
- `/UtilityStatement/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`: the sender's contact fits the role (customer service of the supplier answers questions about the statement).
