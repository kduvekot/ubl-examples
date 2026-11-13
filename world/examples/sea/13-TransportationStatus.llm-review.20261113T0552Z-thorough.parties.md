# LLM review: 13-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/13-TransportationStatus.xml`, Git blob `96261f3aedd684757ce22785ce1d8da29955cd70` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/13#F1 · High · The port facility security officer given as the ship’s security officer; the ship’s report names another person
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:FirstName` = `Tamsin`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:FamilyName` = `Orrel`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:JobTitle` = `Port facility security officer`
- Why: UBL defines `ShipmentStage/SecurityOfficerPerson` as "The person on board the vessel, accountable to the master, designated by the company as responsible for the security of the ship" (the ship security officer of the ISPS Code). The person given here is a port facility security officer, by her own job title: under the ISPS Code (own knowledge) that is the port’s officer for the port facility, not a person on board accountable to the master. The ship’s own report for this voyage names the chief officer as ship security officer: `16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:FamilyName` = `Marrin` with `16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`; and the crew of the vessel in the manifest does not include Tamsin Orrel (`15-Manifest.xml:/Manifest/cac:CrewPerson[2]/cbc:FamilyName` = `Marrin`). The example contradicts the definition and the other two examples.
- Condition: `SecurityOfficerPerson` of the main-carriage stage is the ship security officer of the vessel, the same person as in 16-CommonTransportationReport.xml, or the element is absent.
- Options: Preferred: drop `SecurityOfficerPerson` from this terminal’s status report (the port reports loading; the ship’s security officer is reported by the ship in 16). Alternative: give the ship security officer as in 16 (Elsbeth Marrin, SSO); the port facility security officer, if the report needs one, belongs in the terminal operator’s contact.
- Needs decision: no

### sea/13#F2 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used", i.e. the regional variant of the language. The value `en` with listID `ISO 639` is the language code itself and repeats `Language/ID` = `en` of the same party; it names no locale. The same value occurs 362 times in 213 examples of the world (54 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: No `Language/LocaleCode` in this example holds a bare ISO 639 language code; where a LocaleCode is present it names a locale (language with region, e.g. the variant of English used in the party's country) from a list that defines locales.
- Options: Preferred: remove `LocaleCode` where nothing in the document depends on the locale (the language is already in `Language/ID`). Alternative: give a real locale (e.g. `en-XB` style, from a list of language tags with region) with a listID that defines such codes.
- Needs decision: no

### sea/13#F3 · Low · The Port of Lumeport described as a small enterprise
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:SubsidiaryLocation/cbc:Name` = `Container quay`
- Why: The Port of Lumeport, the port the Trade Accord is named after, runs the container quay where Tidewell Ocean Lines’ feeder loads, issues ships’ sanitation and medical certificates and supplies fuel (16-CommonTransportationReport.xml). Its legal entity calls it a small enterprise, the same size as a forwarder or a 3PL warehouse in this flow. The checklist asks that size fit what the party is; a container port operator is not small.
- Condition: The size class of the Port of Lumeport fits a container port operator in the world (or is absent).
- Options: Preferred: `LARGE` (or the class the world’s story gives the port). Alternative: drop `EntitySizeCode` where the document makes no use of it.
- Needs decision: yes

### sea/13#F4 · Low · The same registration date 1996-01-01 for unrelated companies in three registers
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/RegistrationDate` as "The registration date of the CompanyID". In this example `1996-01-01` is the registration date of the Port of Lumeport (terminal operator) and Bayforth Forwarding (receiver). The same date is given to companies in the island companies register, the federal business register of Bayvarra and the commercial register of Urvania: it occurs 271 times in 181 examples of the world (48 times in this flow; counted with `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while the parties with a known history have their own dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`). A New Year's Day registration shared by unrelated companies in three countries reads as a default value, not a fact of the world (rule "No fillers").
- Condition: Every `RegistrationDate` in this example is the registration date of that party in the world, or the element is absent where the world has no such date.
- Options: Preferred: give each company its own registration date from its history in the world. Alternative: leave `RegistrationDate` out for parties whose registration date the world does not know.
- Needs decision: yes

## Checked and consistent
- Sender and signatory are the Port of Lumeport (`20411781`), the terminal operator of the loading port, whose tracking system reports the loading; the receiver is the forwarder Bayforth Forwarding, which booked the sailing (12-ForwardingInstructions.xml); the carrier is Tidewell Ocean Lines, as in 14-BillOfLading.xml.
- The terminal operator’s physical location `XBLMP` is the loading port of 14-BillOfLading.xml (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMP`).

## Outside this review
- The coordinates of the Port of Lumeport here (40°1.20′ S, 15°12.60′ W) and of the Port of Selanu in 16/17 (40°1.20′ S, 15°8.40′ W) are 4.2′ of longitude apart, about 6 km at that latitude (4.2 nmi × cos 40° ≈ 3.2 nmi), while 08-TransportServiceDescription.xml announces two days at sea between them. This is a question of the map’s scale across examples.
