# LLM review: 12-WeightStatement.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### cotton/12#F1 · Medium · VGM given as equipment gross weight, without method, date or the dedicated aggregate
- XPath: `/WeightStatement/cbc:WeightStatementTypeCode` = `VGM`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: The document is a verified gross mass statement. UBL 2.5 has a dedicated aggregate for it, `TransportEquipment/VerifiedGrossMass` ("the verified gross mass of this piece of transport equipment"), whose `GrossMassMeasure` is "the total verified gross mass of a packed container which includes the cargo weight, block and bracing materials and container tare", with the mandatory `WeighingMethodCode` (SOLAS method 1 or 2) and the weighing date and time. Here the mass is put in `TransportEquipment/GrossWeightMeasure` ("the gross weight of this piece of transport equipment"), and the weighing method, date and time are missing. Under SOLAS VI/2 a VGM is not valid without the method by which it was obtained (own knowledge); the document's purpose depends on it. The dedicated aggregate is used elsewhere in the world (`sea/14-BillOfLading.xml`, counted with `grep -l '<cac:VerifiedGrossMass>'` over `world/examples/*/*.xml`: 1 file).
- Condition: the verified gross mass is stated in `VerifiedGrossMass` with its weighing method, and the weighing date (and time) is stated; the weighing party there agrees with the document's `WeighingParty`.
- Options: (preferred) add `VerifiedGrossMass` (method, date, time, gross mass 9940.29 kg or the weighed value, weighing party) to the container, keeping `TareWeightMeasure`; drop the equipment gross weight or keep it equal.
- Needs decision: no

### cotton/12#F2 · Low · A calculated mass, but a port as weighing party
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- XPath: `/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:TareWeightMeasure` = `3750`
- XPath: `/WeightStatement/cac:WeighingParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: Calculated: 6190.29 kg (goods with packaging, 10, 11) + 3750 kg (tare) = 9940.29 kg exactly. A value to 10 g that equals the sum of the declared cargo weight and the tare is a SOLAS method-2 figure (the shipper adds up the weighed contents and the tare). The weighing party, however, is the Port of Selanu, which points to method 1 (weighing the packed container on a weighbridge); a weighbridge reading would not reproduce the sum to the gram, and a method-2 weighing is the shipper's (the gin's) own, with the bales weighed on the gin's scales. The two statements do not fit together.
- Condition: the weighing party and the stated mass correspond to one method: either the port weighed the packed container (a weighbridge reading, rounded to the scale's resolution) or the shipper calculated it (weighing party the gin).
- Options: (preferred) method 2 with the gin as weighing party, which fits the 0.01 kg precision and the bale weights; or method 1 with a plausible weighbridge value (e.g. 9940 kg) and the port as weighing party.
- Needs decision: no

## Checked and consistent
- Gross minus tare: 9940.29 − 3750 = 6190.29 kg, the gross weight of the goods in 09, 10, 11, 13 and 15.
- Tare 3750 kg fits a 40-foot dry container (about 3700–3900 kg, own knowledge), which agrees with the 40-foot container invoiced in 17.
- `check_ids.py`: container `TWLU4123110` has a valid ISO 6346 check digit; owner code `TWLU` is recorded as unassigned in the BIC register (`world/codelists/sources/bic/owner-codes.txt`).
- Shipment `SCG-SH-26-0200` is the same as in 09, 10, 11, 13 and 15; the receiver Tidewell Ocean Lines is the carrier of 13; the gin is shipper (consignor in 09, 13) and signs as responsible party.
- `XLSEL` uses the user-assigned country code XL, so it cannot clash with a real UN/LOCODE.
- Issued 2026-03-01 15:19, before the bill of lading (2026-03-02 09:37), as a VGM must be.

## Outside this review
- Capacity: 27 bales of about 227 kg (6129 kg, roughly 13–16 m³ at 0.5–0.6 m³ per bale, own knowledge) fill about a fifth of a 40-foot container (about 67 m³, payload about 26 t); a 20-foot container would hold them. Whether the gin would book a 40-foot box for this lot is a capacity question across 12 and 17.
