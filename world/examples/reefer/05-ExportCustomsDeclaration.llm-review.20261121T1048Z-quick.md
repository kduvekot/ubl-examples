# LLM review: 05-ExportCustomsDeclaration.xml

Flow: reefer (BYF-TX-26-2122) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/05-ExportCustomsDeclaration.xml`, Git blob `0f81babef71a61c3fb50b3b7eb0b4cc99670df3c` (committed)
- Last commit changing the example: 99d799b3 2026-11-20 O97 and O78: the call states the withholding, tenders carry the tax subtotal, every time carries its place's UTC offset
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

### reefer/05#F1 · Low · The declarant appears only as the customs agent of the sea stage
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: Bayforth lodges and signs the declaration on the exporter's behalf (`03-ForwardingInstructions.xml` asks it to "declare the export"). ShipmentStage/CustomsAgentParty is "the Customs Agent who is associated with this Shipment Stage", i.e. an agent tied to one leg of the transport; the declaration itself has `IssuerParty` and `FreightForwarderParty` under CustomsDeclaration for the party who makes it. As it is, the declaration names no declarant at its own level; the only trace of who lodged it is a party attached to the main-carriage stage and the signature.
- Condition: the party lodging the declaration is named at the level of the customs declaration, in an element whose definition fits that role.
- Options: (a) move Bayforth to `cac:CustomsDeclaration/cac:IssuerParty` (preferred: the declarant issues the declaration) and drop it from the stage; (b) keep it in the stage and add it as issuer as well, if the stage agent has its own meaning in the world.
- Needs decision: no

### reefer/05#F2 · Low · The customs office is named three times, never identified
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExportLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- Why: office of export and office of exit may be the same office, but CustomsDeclaration/CustomsExitOfficeLocation ("the exit office from where the goods will leave") and Consignment/OfficeOfExitLocation say the same thing twice. None of the three carries an identifier, although customs offices are identified by a code in a customs declaration (own knowledge: customs office reference numbers), and the port itself is identified as `XBLMP` in the same document.
- Condition: each office is stated once per meaning and is identified by an ID of a world customs-office scheme (or the reason for name-only is visible).
- Options: (a) keep office of export and exit in the consignment with an office ID, drop the duplicate CustomsExitOfficeLocation (preferred); (b) keep CustomsExitOfficeLocation and drop OfficeOfExitLocation.
- Needs decision: no

## Checked and consistent
- Customs values: 14,524.58 / 17,472.00 = 5,702.76 / 6,860.00 = 3,770.80 / 4,536.00 = 0.83131; total 23,998.14 = the CIP contract value 28,868.00 less 4,869.86, which is the ocean freight and bunker of `07-BillOfLading.xml` (4,400.00 + 400.00) plus 69.86 (0.22 % of the insured 31,754.80, a plausible premium) — an export value at the frontier, apportioned by value.
- Weights 13,036.8 + 5,432 + 3,259.2 = 21,728 kg = consignment gross; 1,120 packages on 20 handling units, as in `06-DespatchAdvice.xml`.
- Vessel, journey `TH-26-17E`, estimated departure 2026-04-23 18:00 agree with `07-BillOfLading.xml`; MMSI 298… and call sign Q… are not allocated by the ITU (known refutation).
- Shipment and consignment IDs agree with `03-ForwardingInstructions.xml`; the declaration ID `BYF-EX-26-0425` is cited by `09-ImportCustomsDeclaration.xml`.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `26-0215`: the order's quantities differ from the declared ones — refuted: on 21 April the invoice does not exist yet (issued 23 April), and the order is the contract the export is made under.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CityName` = `Euridice Crossing`: the declaration is made at the port of Lumeport — refuted: the same head-office address is used for this authority in every example that names it (11 places in 10 examples, counted with grep over `*.xml`).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryCertificateDocumentReference/cbc:ID` = `REG-XB-S-20117`: resolves to no example — refuted: a ship's registry certificate is an external document, not a UBL example.
