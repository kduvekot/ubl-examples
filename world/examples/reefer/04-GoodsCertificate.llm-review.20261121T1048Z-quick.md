# LLM review: 04-GoodsCertificate.xml

Flow: reefer (HRW-TX-26-0757) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/04-GoodsCertificate.xml`, Git blob `db060b320f947d55a9b0502be94f706cb1ea8b94` (committed)
- Last commit changing the example: 1b71959a 2026-11-20 O260: every document belongs to the collaboration it is exchanged in
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

### reefer/04#F1 · Low · Fire blight is a sub-line of the codling moth line
- XPath: `/GoodsCertificate/cac:Attestation/cac:AttestationLine/cbc:Description` = `Codling moth (Cydia pomonella): none found.`
- XPath: `/GoodsCertificate/cac:Attestation/cac:AttestationLine/cac:SubAttestationLine/cbc:Description` = `Fire blight (Erwinia amylovora): no symptoms in the orchards of origin this season.`
- Why: SubAttestationLine is "an attestation line subsidiary to this attestation line". Fire blight is a separate quarantine pest with a separate basis (a field inspection of the orchards this season, not the packhouse sample of 2 % of the cartons that the line's criterion `XL-PH-12` describes); it is not part of the codling moth statement. Nested this way, the fire blight statement inherits the codling moth line's criterion. The attestation's own description names both pests side by side (`Sampled at the packhouse and found free of codling moth and fire blight.`), and even that says "sampled at the packhouse", while the sub-line speaks of the orchards.
- Condition: each pest is attested in its own attestation line with its own basis (or the sub-line is a genuine part of its parent), and the attestation's description agrees with how each pest was checked.
- Options: (a) two attestation lines, codling moth (packhouse sample, criterion XL-PH-12) and fire blight (orchard inspection, its own criterion if the island names one) (preferred); (b) keep the nesting and make line 1 a general "pest freedom" line with both pests as sub-lines.
- Needs decision: no

### reefer/04#F2 · Low · The certificate refers to the original order and names the forwarder, neither used
- XPath: `/GoodsCertificate/cac:AdditionalDocumentReference/cbc:ID` = `26-0215`
- XPath: `/GoodsCertificate/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: a phytosanitary certificate attests the condition of the consignment; the plant health service has no use for the buyer's order, and the order it cites carries quantities the certificate does not certify (224 Granny Smith and 224 pears in `01-Order.xml:/Order/cac:OrderLine[3]/cac:LineItem/cbc:Quantity` = `224`, against 280 and 168 here, the quantities of `02-OrderResponse.xml`). The forwarder plays no part in the certificate (it neither applies nor receives it). Both look copied from the shipment's data rather than needed by the document (section 4.8 of the review rules).
- Condition: every reference and party in the certificate is one the certificate's purpose uses; a commercial reference, if kept, does not contradict the certified quantities.
- Options: (a) remove the order reference and the forwarder (preferred); (b) if the island requires a commercial reference on the certificate, cite the invoice or the order response, whose quantities match.
- Needs decision: no

## Checked and consistent
- Weights: 672 × 19.4 = 13,036.8 kg, 280 × 19.4 = 5,432 kg, 168 × 19.4 = 3,259.2 kg; sum 21,728 kg = the consignment gross weight in `03-ForwardingInstructions.xml` and `07-BillOfLading.xml`.
- Sample: 2 % of 1,120 cartons is 22.4, rounded up to the 23 of the attestation note; 672 + 280 + 168 = 1,120.
- Validity 21 April to 5 May covers the sailing (23 April) and the arrival at Selanu (26 April, `10-TransportationStatus.xml`); applicable territory is Lisavu, the destination.
- HS 080810/080830, CPC 01341/01342 and HS section II fit apples and pears. Harvest months (Gala February–March, Granny Smith April, Packham's March) are consistent across the descriptions.
- Shipment ID `HRW-SH-26-0730` is the shipment of `03-ForwardingInstructions.xml`; the certificate number `FDAB/2026/7266` is cited by `09-ImportCustomsDeclaration.xml`.

## Considered and refuted
- `/GoodsCertificate/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `GEN`: chilled fruit might call for a reefer cargo type — refuted: the world's list has only general, dry bulk, liquid bulk and break-bulk, and palletised fruit in a container is general cargo.
- `/GoodsCertificate/cac:WarehouseParty/cac:PartyName/cbc:Name` = `Harrowmead Fruit Growers`: a party the certificate might not need — refuted: the fruit was kept in the cooperative's cold store and inspected there, so the party storing the goods at inspection is relevant to plant health.
- `/GoodsCertificate/cac:Attestation/cbc:ID` = `FDAB/2026/7265`: one number below the certificate's own ID — refuted: an attestation may carry its own number in the issuer's series.
