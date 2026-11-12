# LLM review: 02-ForwardingInstructions.xml

Flow: mast (MAST-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1443Z-thorough`
- Example: `world/examples/mast/02-ForwardingInstructions.xml`, Git blob `2697645dcfc391cd36edbe8e8ed4c28f35be7a85` (committed)
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

### mast/02#F1 · Medium · The consignor as the party "notified" of its own dangerous goods
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- Why: UBL defines HazardousItemNotificationParty as "the Party who is notified of a Hazardous Item in this Consignment". Saltmere Engineering is the consignor that declares the dangerous goods in these instructions; it is the party that gives the notification, not the one that receives it. A party to be notified would be one that does not already know: the consignee (Selanu Telecom, who receives batteries, a radioactive excepted package and a corrosive liquid), the destination handler, or an authority. The same occurs in 03 (`03-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:HazardousItemNotificationParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`); these are the only two examples with this element (`grep -rl --include='*.xml' HazardousItemNotificationParty world/examples`).
- Condition: the HazardousItemNotificationParty is a party that has to be told about the dangerous goods and is not their consignor, or the element is absent.
- Options: (a, preferred) the consignee Selanu Telecom (or the destination ground handler, if the world has one), which must prepare for receiving them; (b) drop the element; the consignor's emergency role is already carried by `LoadedHazardousItem/ContactParty`.
- Needs decision: no

### mast/02#F2 · Medium · The emergency contact has no means of contact
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadedHazardousItem/cac:ContactParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: ContactParty is "the individual, group, or body who is contacted in case of a hazardous incident associated with this item". It carries only Saltmere's register number and name, no contact; the only Saltmere contact in the document is the consignor's "Bids office", reachable on weekdays 08:00–17:00. Air transport of lithium batteries needs an emergency contact reachable for the whole journey (own knowledge of IATA DGR practice). The purpose of the element depends on a telephone number that is answered at any time. The other two loaded hazardous items (UN 2911, UN 2920) have no ContactParty at all.
- Condition: every loaded hazardous item that has a contact party gives a means of contact reachable around the clock (e.g. a 24-hour emergency telephone), and the items without one are covered by the same contact or say why not.
- Options: (a, preferred) give the ContactParty a Contact with a 24-hour emergency number (Saltmere's or an emergency response provider's) and use it for all three items; (b) drop ContactParty if the world does not model emergency response.
- Needs decision: no

### mast/02#F3 · Medium · A language code in LocaleCode
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language code again, not a locale. 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale with a matching listID.
- Options: (a, preferred) `en-XB` from a locale list (BCP 47); (b) drop it.
- Needs decision: no

### mast/02#F4 · Low · Consignor's and consignee's contacts do not fit the transport roles
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Name` = `Bids office`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:Contact/cbc:Department` = `Procurement`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Business accounts`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The consignor's contact in forwarding instructions is the one who arranges the despatch (shipping or logistics), and the consignee's contact is the one who receives the goods. Here they are Saltmere's procurement "Bids office" and Selanu Telecom's sales desk for business customers.
- Condition: the consignor's contact handles despatch, and the consignee's contact receives goods (stores, site or goods-in).
- Options: (a, preferred) a despatch contact for Saltmere and a goods-receiving contact for Selanu Telecom.
- Needs decision: no

### mast/02#F5 · Low · Selanu Telecom described differently than in the order and the waybill
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Mast Hill Road`
- XPath: `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: In 01 and 03 Selanu Telecom's legal form is given in Lisavan and English, each with its `languageID`, and the English address renderings are tagged `en-XL`; here the legal form has one rendering without `languageID` and the English address renderings are tagged `en-XB` (the issuer's country). The same applies in 04 and 05. The same party should be described the same way in every example.
- Condition: Selanu Telecom's legal form and address renderings are the same, with the same `languageID`s, in every example of the flow.
- Options: (a, preferred) both legal-form renderings with their tags, and the English address renderings tagged by the address's country, everywhere.
- Needs decision: no

### mast/02#F6 · Low · Registration date 1 January 1996
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same date is the registration date of 25 different companies in 181 examples (counted with lxml over `world/examples/*/*.xml` and `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`); it reads as a default, not as each company's history.
- Condition: each company's registration date is its own, or absent.
- Options: (a, preferred) dates from the company histories; (b) drop them.
- Needs decision: yes (company histories)

## Checked and consistent
- Parties against 01, 03 and 04: Saltmere Engineering `20410685`, Bayforth Forwarding `20411644`, Selanu Telecom `IC42407`; identifiers, names, address IDs, tax IDs, contacts and endpoints agree (apart from F5).
- Bayforth Forwarding is the forwarder receiving the instructions; in 03 it is the waybill's ReceiverParty and FreightForwarderParty, consistent with it having booked the air carriage.
- Bayforth's tax registration (STT, Coastal State) matches its Lumeport address in Coastal State.

## Considered and refuted
- `/ForwardingInstructions/cac:FreightForwarderParty`: UBL defines the FreightForwarderParty as a consolidator, while Bayforth forwards one unconsolidated consignment — refuted because forwarding instructions are by definition "issued to a forwarder" and this is the only element for that party; consolidation is not required by the role.
- `/ForwardingInstructions/cac:FreightForwarderParty/cbc:IndustryClassificationCode`: ISIC 5229 (other transportation support activities) — refuted, the class covers freight forwarding.
- `/ForwardingInstructions/cac:FreightForwarderParty/cac:Contact/cbc:Name`: "Export desk", operations planner — refuted, it fits a forwarder handling an export.
