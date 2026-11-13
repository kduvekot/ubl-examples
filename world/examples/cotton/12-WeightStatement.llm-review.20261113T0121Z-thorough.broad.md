# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/12-WeightStatement.xml`, Git blob `63cbeb9c6ff2202636e981ef15d7262f47f2a1a5` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/12#F1 · Medium · Language code in `LocaleCode`
- XPath: `/WeightStatement/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/12#F2 · Low · Verified gross mass without when and how it was obtained
- XPath: `/WeightStatement/cbc:WeightStatementTypeCode` = `VGM`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: the port of Selanu weighed, but the statement gives no date or time of weighing and does not say whether the packed container was weighed (SOLAS method 1) or the contents were added to the tare (method 2). The figures (6190.29 kg cargo + 3750 kg tare) read like method 2, while a weighing party at the port suggests method 1. A carrier receiving the VGM needs to know which.
- Condition: the statement says when the mass was determined and by which method, consistently with the weighing party.
- Options: (preferred) state method 1 with the port's weighing time (and a weighed value, which need not equal cargo + tare exactly); or method 2 with the ginnery as the party that calculated it and no weighing party.
- Needs decision: no

### cotton/12#F3 · Low · The shipper signs "on behalf of" itself
- XPath: `/WeightStatement/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- XPath: `/WeightStatement/cac:ShipperParty/cac:PartyName/cbc:Name` = `Selanu Cotton Ginnery`
- Why: `ResponsibleParty` is "The Party who signs the Verified Gross Mass (VGM) on behalf of the Shipper". It is the shipper itself; SOLAS asks for the name of the person duly authorised by the shipper (own knowledge, SOLAS VI/2 and MSC.1/Circ.1475), which is not given.
- Condition: the responsible party is the person or party authorised by the shipper (distinct from the shipper), or absent.
- Options: (preferred) a person (e.g. the ginnery's shipping clerk) as the signatory; or drop `ResponsibleParty` and let the signature stand.
- Needs decision: no

### cotton/12#F4 · Low · The shipper's contact for the VGM is its sales desk
- XPath: `/WeightStatement/cac:SenderParty/cac:Contact/cbc:Name` = `Cotton sales`
- Why: questions about a verified gross mass go to whoever stuffed and declared the container (shipping / dispatch), not to lint sales.
- Condition: the sender's contact handles shipping.
- Options: (preferred) a shipping / dispatch contact.
- Needs decision: no

## Checked and consistent
- 6190.29 kg (cargo gross, 10, 11) + 3750 kg tare = 9940.29 kg verified gross mass.
- Tare 3750 kg fits a 40-foot general-purpose container (about 3.7–3.8 t, own knowledge) and the forwarder's invoice for "one 40-foot container" (17); 27 bales of 227 kg (about 0.5–0.6 m³ each) fill only a part of a 40-foot box (about 67 m³), so the load fits.
- Container number `TWLU4123110` passes the ISO 6346 check digit; issued 1 March, before the bill of lading (2 March).
- Shipment ID SCG-SH-26-0200 is the one in 09, 10, 11, 13 and 15; the receiver is the carrier of 13.

## Considered and refuted
- `/WeightStatement/cac:Shipment`: the container is not named in the bill of lading 13, so the VGM cannot be tied to it — not a finding of this example; see "Outside this review".

## Outside this review
- The bill of lading 13 names no container, so the link between this VGM and the carriage rests on the shipment ID only (a problem of 13).
- Whether the container owner code `TWLU` is assigned in the real BIC register could not be checked offline.
