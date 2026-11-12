# LLM review: 07-TransportationStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/07-TransportationStatus.xml`, Git blob `104dc14ba8f489635d6473fbc6d93903f6bf457e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/07#F1 · Medium · Province in Region of carrier and terminal operator
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/07#F2 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/07#F3 · Low · Status and event locations are the company name, without identifier
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, and identifiers are given where the same place is identified elsewhere. Both locations are named with the terminal operator's name only (the operator is in `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`), while the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`) and the waybill identifies the loading place with a UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`) and the storage place as "Ferrano Intermodal Hub, stack C".
- Condition: the locations identify the terminal the same way the other examples of the flow do.
- Options: (a) a location identifier for the terminal used in every example (preferred); (b) at least the plan's address or a place name distinct from the company.
- Needs decision: no

## Checked and consistent
- Sender and signatory are the hub (`XU-R-105096`), the same party as the terminal operator of the main carriage; receiver and carrier are Ferrano Rail Cargo (`XU-R-104685`), the transport service provider of the plan referenced (`03-TransportExecutionPlan.xml`).
- The full descriptions of the carrier and the terminal operator are identical to those in `04-TransportProgressStatusRequest.xml` and `05-TransportProgressStatus.xml`.
