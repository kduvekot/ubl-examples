# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/12-WeightStatement.xml`, Git blob `63cbeb9c6ff2202636e981ef15d7262f47f2a1a5` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### cotton/12#F1 · Low · A weighing station is named, but the verified gross mass is the arithmetic sum of cargo and tare
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TareWeightMeasure` = `3750`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- Why: WeighingParty is "The Party who executes the weight measure (e.g. weighing station)". Under
  SOLAS VI/2 the verified gross mass is obtained either by weighing the packed container (method 1)
  or by adding the weighed cargo and packing to the container's tare (method 2) (own knowledge).
  Naming the port's weighing station as the party that executes the measurement points to method 1;
  but 9,940.29 kg is exactly the shipment's 6,190.29 kg plus the container's 3,750 kg tare, to the
  hundredth of a kilogram, which is a method 2 calculation by the shipper. A weighbridge reading of
  a packed container would not reproduce the cargo weight plus the tare to 10 g. The document does
  not say which method was used, so the weighing party and the figure do not fit together.
- Condition: the weighing party and the verified gross mass correspond to one SOLAS method: a weighed
  value for the packed container if the port weighed it, or the shipper as the party that weighed
  the cargo if the mass is the sum with the tare.
- Options: (a, preferred) keep the port as weighing party and give a weighed figure for the packed
  container (e.g. rounded to the weighbridge's resolution); (b) make the ginnery the weighing party
  (method 2) and keep the sum.
- Needs decision: no

## Checked and consistent
- WeightStatementTypeCode VGM, the ginnery as shipper responsible for the VGM, as signatory and as
  responsible party, and the carrier Tidewell Ocean Lines as receiver fit a VGM declaration to the
  carrier before loading (issued 2026-03-01, B/L 2026-03-02).
- Container TWLU4123110 passes the ISO 6346 check digit (`check_ids.py`); a tare of 3,750 kg fits a
  40-foot dry container (own knowledge, typically 3,700–3,800 kg).
- The shipment ID SCG-SH-26-0200 is that of 09, 11, 13 and 15.

## Considered and refuted
- `/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`: a location of the
  weighing party in a VGM — refuted because where the container was weighed is relevant to the
  weighing station's identity.
