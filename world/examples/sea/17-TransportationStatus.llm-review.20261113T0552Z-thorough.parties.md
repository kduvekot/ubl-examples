# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/17-TransportationStatus.xml`, Git blob `ca6268e2b075e6b8011b2c7aa08d386ab1c51391` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/17#F1 · Medium · A language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used". Both values are the ISO 639 language code already given in `Language/cbc:ID`, with `listID="ISO 639"`, so they name no locale. Tidewell and Bayforth are Bayvarran companies; their locale would be English in Bayvarra. The same `LocaleCode` = `en` occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country), not a bare language code.
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) give a locale such as `en-XB` with a list identifier that defines locales.
- Needs decision: no

### sea/17#F2 · Low · The contacts do not fit the roles in a discharge notice
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- Why: The report says the container has been discharged at Selanu and is available for customs clearance. The consignee's contact is "the party who receives the goods", but its contact is called Purchasing while its job title is a customer service officer in the Sales department: name, title and department disagree with each other, and none of them is goods receipt or import. The receiver, Bayforth, is addressed through its export desk although the report is about the arrival and import side. The terminal's contact is named Port control (a vessel traffic function) but is an operations planner with office hours, not the terminal's container or customer desk. The same consignee contact is in 24 examples of the flow (grep for `<cbc:Name>Purchasing</cbc:Name>` over sea *.xml), so it comes from the party's master data.
- Condition: Each contact's name, job title and department agree with each other, and the consignee's, receiver's and terminal's contacts are the functions that handle the arrival and release of the container.
- Options: (a) role-specific contacts (consignee: goods receipt or import; forwarder: import or arrivals desk; terminal: container desk) (preferred); (b) leave contacts out where the party's master-data contact does not serve the report.
- Needs decision: no

### sea/17#F3 · Low · Tax registrations and share capital in a status report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: A transportation status report circulates events; it bills nothing (the terminal handling charge it mentions is not invoiced here) and does nothing with the carrier's or the forwarder's state sales-tax registration or with the carrier's capital stock. They are copied from master data (section 4.8 of the review rules).
- Condition: The carrier and the receiver carry only the party data a status report uses.
- Options: (a) drop `PartyTaxScheme` from both and `CorporateStockAmount`/`FullyPaidSharesIndicator` from the carrier (preferred); (b) keep them with a reason in the document.
- Needs decision: no

## Checked and consistent
- Sender and signatory are the Port of Selanu (`IC41037`), which is also the terminal operator of the discharge, so the status comes from the party that saw the events.
- The consignee (Velumi Trading, `IC41859`) and the carrier (Tidewell, `20411918`) match the bill of lading `14-BillOfLading.xml` by identifier and name; their full descriptions are identical to the other examples that use the same language tags (compared element by element with a script).
- The Port of Selanu, Velumi Trading and their legal forms carry `en-XL` and the Lisavan rendering here, which is the convention of the other examples issued on the island (17, 19, 21, 24, 27, 28, 29); the differing examples are reviewed there.
- The consignee's customs trader identifier (`XL-TR-041859`) fits a report that the goods are available for customs clearance.
- Industry classifications fit: 5012 carrier, 5222 port, 5229 forwarder, 4649 wholesaler.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ReportingPerson/cbc:JobTitle`: a port duty officer as reporting person of the main carriage, while `16-CommonTransportationReport.xml` names the master — refuted because the two documents report different things (the ship's arrival formalities against the discharge status), and the sender's duty officer providing this report is a legitimate reading of "responsible for providing the required administrative reporting".
- `/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name`: the export forwarder as receiver of an import status — refuted because Bayforth is the freight forwarder of the whole consignment (also named in `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`) and the instruction about the delivery slot fits a forwarder arranging on-carriage.
- `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cbc:IndustryClassificationCode`: ISIC 4649 (wholesale of household goods) for a trader of park benches — refuted because 4649 includes the wholesale of furniture.
