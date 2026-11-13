# LLM review: 11-ExportCustomsDeclaration.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/11-ExportCustomsDeclaration.xml`, Git blob `6df68444b58544480345d9e469661ab775d8d16a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### sea/11#F1 · High · Emission factor times base does not give the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` × `ValueBaseMeasure` is the value by definition ("A numeric factor used to calculate the value measurement", "The base quantity to which the value factor applies"); 0.82 × 1 EA = 0.82, not 96 kg CO2e. Same triple in 39 XML examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82</cbc:ValueFactorNumeric>' world/examples`).
- Condition: factor × base = value, or factor and base are absent.
- Options: drop factor and base (preferred); or a factor on a base whose product is 96.
- Needs decision: no

### sea/11#F2 · Medium · Function code of the previous declaration holds a declaration type
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `IMPORT`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:FunctionCode` = `9`
- Why: `CustomsDeclaration/FunctionCode` is "A code describing the function of this customs declaration". The declaration itself uses it as intended, with UN/EDIFACT 1225 `9` Original; the previous declaration uses a code from the world's `CustomsDeclarationTypeCode` list, "Import declaration", which is the kind of declaration, not its function. The same element thus carries two different meanings from two lists in one document. The referenced declaration exists: `road/10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:ID` = `LD-IM-26-0161`, Lumeway's import of the 96 benches and the frames from Urvania on 2026-03-24.
- Condition: `FunctionCode` of the previous declaration is a function code (from the list used for the declaration itself), and the fact that it was an import declaration is carried, if needed, where a type belongs.
- Options: drop the function code of the previous declaration (preferred: the reference's ID resolves to the import declaration, whose document type says it is one); or give its function (`9` Original) and say "import" in a description.
- Needs decision: no

### sea/11#F3 · Medium · Export declaration without packages, container or means of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:Quantity` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:CustomsAgentParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: an export declaration identifies the goods to customs so that the exit office can match them when they leave. Here the goods items have quantities and weights but no number or kind of packages and no marks, the shipment has no transport handling unit or container (`TWLU4120872` with seal `TWL-S-0884213` in the bill of lading), and the only shipment stage names the customs agent but neither mode of transport nor vessel or voyage (`Tidewell Harbour`, `TH-26-19E`). These are core data of an export declaration (own knowledge of the WCO data model: packages, container ID, mode and means of transport at the border). The declaration is made on 2026-05-12, when the container and its packing are already known (VGM weighed at 15:30 that day, packing list 15:59).
- Condition: the declaration states for each goods item the number and kind of packages, the container in which the goods leave, and the mode of transport at the border (with the vessel and voyage, if known at lodging).
- Options: add packages per goods item (24 pallets / 1 pallet), the container as transport handling unit, and mode `1` with the planned vessel on the shipment stage (preferred); or at least the packages and the container.
- Needs decision: no

### sea/11#F4 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus packaging (the goods items' 3,984 + 122.4 kg); with the container the shipment weighs 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`).
- Condition: the shipment's gross weight includes the transport equipment, or is left to the goods items.
- Options: drop it (the goods items carry 3,984 and 122.4 kg, which customs uses) (preferred); or 7,856.4 kg.
- Needs decision: no

### sea/11#F5 · Low · Customs offices named but not identified
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExportLocation/cbc:Name` = `Customs office, port of Lumeport`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs office, port of Lumeport`
- Why: the three offices are the same place, given only as a name; customs offices are identified by an office code, and the port itself has the LOCODE `XBLMP` used throughout the flow. A declaration routed to an office needs the office's identifier.
- Condition: the office locations carry an identifier (office code, or at least the port's LOCODE).
- Options: an office ID in Bayvarra's customs office scheme (preferred, if the world has one); or the LOCODE `XBLMP`.
- Needs decision: no

## Checked and consistent
- Values: declared customs value 50,688 XBL = sum of the goods items 49,920 + 768 = FOB value = the order's total; insurance value 59,155.80 = 110 % of the CIF value 53,778 on the bill of lading; the freight charge of 2,950 XBL = ocean freight 2,700 + bunker surcharge 250 on the bill of lading.
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` match the packing list and bill of lading; goods items, quantities, gross weights, HS codes `940179`/`732599` and origin Urvania match the packing list.
- Timing: lodged 2026-05-12 14:25, before the container is dropped at the port (2026-05-13 10:15) and before the sailing (2026-05-14): "declared electronically before the goods leave" holds. Validity 90 days from 2026-05-12.
- The previous declaration `LD-IM-26-0161` exists in another flow (`road/10-ImportCustomsDeclaration.xml`, 2026-03-24) and covers the same 96 benches, so the re-export of imported stock is traceable.
