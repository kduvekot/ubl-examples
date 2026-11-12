# LLM review: 03-Waybill.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/03-Waybill.xml`, Git blob `bd3a3f9d377d18d732a5834ff59fed7e413de940` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow)
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### mast/03#F1 · Medium · The consignor as the party "notified" of its own dangerous goods
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: HazardousItemNotificationParty is "the Party who is notified of a Hazardous Item in this Consignment". Saltmere Engineering is the consignor (`/Waybill/cac:ConsignorParty/cac:PartyIdentification/cbc:ID` = `20410685`) that declared the dangerous goods; it gives the notification rather than receiving it. The same in 02.
- Condition: the HazardousItemNotificationParty is a party that has to be told about the dangerous goods and is not their consignor, or the element is absent.
- Options: (a, preferred) the consignee Selanu Telecom or the destination handler (Selanu Airport Cargo, who receives the consignee's original with the goods); (b) drop the element.
- Needs decision: no

### mast/03#F2 · Medium · The emergency contact has no means of contact
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:ContactParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: ContactParty is "the individual, group, or body who is contacted in case of a hazardous incident associated with this item". On an air waybill for a cargo-aircraft-only flight with lithium batteries, the crew and handlers need an emergency number reachable at any time (own knowledge of IATA DGR practice). The ContactParty has only an ID and name; the only Saltmere contact in the waybill is its "Bids office", weekdays 08:00–17:00. The other two loaded hazardous items have no ContactParty.
- Condition: the contact party for hazardous items gives a means of contact reachable around the clock, for every hazardous item it covers.
- Options: (a, preferred) a Contact with a 24-hour emergency number under ContactParty, for all three items; (b) drop ContactParty.
- Needs decision: no

### mast/03#F3 · Medium · A language code in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language code again. 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale with a matching listID.
- Options: (a, preferred) `en-XB` from a locale list (BCP 47); (b) drop it.
- Needs decision: no

### mast/03#F4 · Low · Distribution of the originals does not match the note
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: The note announces three originals for consignor, consignee and carrier. The distribution lists only the consignee's original (to Selanu Airport Cargo, which appears in no other party role of the flow and is not described beyond its name) and an electronic copy to the forwarder; the consignor's original (for Saltmere, or Bayforth on its behalf) and the carrier's are not distributed. Sending the consignee's original with the goods to the destination handler is a legitimate practice, but who Selanu Airport Cargo is for this consignment is not said.
- Condition: the distribution and the note agree on who receives which original, and every distribution party's role is identifiable (e.g. as the handler at destination).
- Options: (a, preferred) add the consignor's original (to Bayforth as the shipper's agent, or Saltmere) and, if wanted, the carrier's; identify Selanu Airport Cargo's role (e.g. by a description or as a party in the consignment); (b) reword the note to what is distributed.
- Needs decision: no

### mast/03#F5 · Low · Kelaro's contact: sales name, operations job
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Department` = `Operations`
- Why: The contact is named "Cargo sales" but its job title is operations planner in the operations department. Name and department contradict each other; for the carrier issuing the waybill, operations is the fitting one.
- Condition: name, job title and department of the contact agree.
- Options: (a, preferred) a name such as "Cargo operations"; (b) a sales job title and department, if the waybill is issued by sales.
- Needs decision: no

### mast/03#F6 · Low · Consignor's and consignee's contacts do not fit the transport roles
- XPath: `/Waybill/cac:ConsignorParty/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: On a waybill, the consignor's contact is the one who despatched the goods and the consignee's contact is the one who receives them ("Deliver against signature of the consignee"). Here they are Saltmere's procurement "Bids office" and Selanu Telecom's sales desk "Business accounts".
- Condition: the consignor's contact handles despatch and the consignee's contact receives goods.
- Options: (a, preferred) a despatch contact for Saltmere, a goods-receiving contact for Selanu Telecom.
- Needs decision: no

### mast/03#F7 · Low · Issue location named after a company, without an identifier
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: "Lumeport Airport Cargo Terminal" is a company elsewhere in the examples (RegistrationName "Lumeport Airport Cargo Terminal Ltd", XB register `20412055`); as an IssueLocation it should name and, where possible, identify the place (the airport or its cargo terminal, e.g. by the location identifier the world uses for Lumeport's airport). All 7 examples with an IssueLocation name it after a company (Castrano Logistics, Fiumella Barges, Lumeway Distribution, Serravona Mining, Lumeport Airport Cargo Terminal; `grep -rh --include='*.xml' -A3 '<cac:IssueLocation>' world/examples`).
- Condition: the issue location names the place and, where the world identifies it elsewhere, carries its identifier.
- Options: (a, preferred) a place name ("Lumeport Airport, cargo terminal") with a location ID; (b) keep the name and add the ID.
- Needs decision: no

### mast/03#F8 · Low · Registration date 1 January 1996
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is the registration date of 25 different companies in 181 examples (lxml count and `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`); it reads as a default, not as each company's history.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes (company histories)

### mast/03#F9 · Low · Kelaro Air Cargo described differently than in the despatch advice
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- XPath: `04-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Here Kelaro's legal form is given in Lisavan and English with `languageID`s and its English address renderings are tagged `en-XL`; in 04 the legal form has a single rendering without `languageID` and the address renderings are tagged `en-XB`. Selanu Telecom shows the same difference between this example and 02, 04 and 05.
- Condition: each party's legal form and address renderings are the same, with the same `languageID`s, in every example of the flow.
- Options: (a, preferred) both renderings with their tags, and English address renderings tagged by the address's country, everywhere.
- Needs decision: no

## Checked and consistent
- Roles: Kelaro Air Cargo `IC41311` is SenderParty and CarrierParty (the carrier issues the air waybill, signature `IC41311`); Bayforth Forwarding `20411644` is ReceiverParty and FreightForwarderParty (it received the forwarding instructions in 02 and booked the carriage); Saltmere Engineering consignor and Selanu Telecom consignee as in 02.
- The parties' identifiers, names, address IDs, tax IDs, contacts and endpoints agree with 01, 02 and 04 (apart from F9).
- The aircraft's registration nationality `XL` matches the carrier's country.

## Considered and refuted
- `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode`: an airline operating cargo aircraft described as SMALL — refuted because an island cargo airline with few aircraft can be small; nothing in the flow contradicts it.
- `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyIdentification/cbc:ID`: the consignee's original sent to a party other than the consignee — refuted as a role error because the consignee's original of an air waybill travels with the goods and is handed over at destination; the remaining question is in F4.
