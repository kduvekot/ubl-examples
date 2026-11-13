# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/03#F1 · Low · The textile mill as originator and beneficiary of a seed cotton purchase from the farm
- XPath: `/DeliveryNote/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- Why: `cac:OriginatorCustomerParty` is defined here as "A customer party as originator." and `cac:BeneficiaryParty` as "A Party for whom the associated transaction is ultimately intended or who derives benefit from it." The transaction is the ginnery's purchase of seed cotton from the farm, called off under the ginnery's own season agreement (an order reference assigned by the buyer, the ginnery). The mill buys lint from the ginnery later and separately (08-Order.xml, `08-Order.xml:/Order/cbc:ID` = `LTM-PO-26-0198`); it neither originated this call-off nor is the seed cotton intended for it, since the ginnery gins and sells the lint on its own account. The other documents of the same purchase, 01-SelfBilledInvoice.xml and 05-SelfBilledCreditNote.xml, name no originator or beneficiary, so the flow is not consistent either. A reading in which the mill's season agreement drives the ginnery's purchases is possible, but the documents do not show it.
- Condition: The mill appears as originator or beneficiary of the farm-to-ginnery documents only if the story makes it the party that requested, or the party for whom, the seed cotton is bought, and then in every document of that purchase.
- Options: (a, preferred) drop both roles from the farm-to-ginnery documents; (b) if the mill finances or pre-buys the farm's crop, say so in the story and name it the same way in 01, 03, 04 and 05.
- Needs decision: yes

### cotton/03#F2 · Low · The ginnery's sales contact in a role that is not selling
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The checklist asks whether a party's contact fits its role. The ginnery is described with its cotton sales desk, the contact for customers buying lint. Here the ginnery is the delivery customer: the party to whom three trailer loads of seed cotton are delivered and weighed at the gin. Its contact for this is the gin yard or weighbridge that receives the loads.
- Condition: The ginnery's contact in this role is receiving seed cotton at the gin (gin yard or weighbridge), or the contact is left out.
- Options: (a, preferred) use a contact for receiving seed cotton at the gin (gin yard or weighbridge); (b) drop the contact, since the document gives the ginnery's electronic address.
- Needs decision: no

### cotton/03#F3 · Low · A customer service officer in the sales department of a one-person farm
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/DeliveryNote/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: The farm is a sole proprietorship and a micro enterprise, owned and run by one person. A job title `Customer service officer` in a department `Sales` describes a company with a sales organisation; it does not fit the farm, whose contact is called `Farm office`.
- Condition: The farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) drop JobTitle and Department; (b) a job title such as Farmer or Owner.
- Needs decision: no

### cotton/03#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

### cotton/03#F5 · Low · Party master data the document does not use
- XPath: `/DeliveryNote/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- Why: Section 4.8 (presence): the ginnery's customs trader number is present. A domestic delivery of seed cotton from a Lisavan farm to a Lisavan gin involves no customs, and the delivery note does nothing with them, so they read as copied from the parties' master data (no fillers, IND5).
- Condition: Every identifier, location and registration in the parties of this document is one the document has a use for.
- Options: (a, preferred) leave them out of this document; (b) keep them only where the document's purpose gives them a role, and say which.
- Needs decision: no

## Checked and consistent
- Despatch supplier and seller (the farm), delivery customer and buyer (the ginnery) are identified as in 01, 04 and 05; the signatory is the farm, which issues the delivery note (`LCF-` number).
- The farm's physical location (the fields, with coordinates) has a reason here: it is where the despatched loads come from.
- The farm's and the ginnery's full descriptions are identical to those in 01, 04, 05 and 06 (compared block by block).

## Considered and refuted
- `/DeliveryNote/cac:DespatchSupplierParty`: suspected because a farm rarely "executed the delivery" itself — refuted because the note says the loads came by trailer and no carrier is named; a farm hauling its own crop to the gin is normal, and 04 pays the farm a haulage allowance.
