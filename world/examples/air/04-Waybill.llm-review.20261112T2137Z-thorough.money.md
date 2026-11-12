# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/04-Waybill.xml`, Git blob `df051bb647e8d343d035d6fb70ee57e379ee8b0f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/04#F1 · High · Exchange rate established a week after the waybill was issued
- XPath: `/Waybill/cac:ExchangeRate/cbc:Date` = `2026-05-20`
- XPath: `/Waybill/cbc:IssueDate` = `2026-05-13`
- Why: ExchangeRate/Date is "the date on which the exchange rate was established". A waybill issued
  on 13 May cannot state a rate established on 20 May; the date is also after the flight
  (`/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`)
  and after the forwarder's invoice (`10-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-05-15`).
- Condition: the exchange rate's Date is on or before the issue date of the waybill (or the
  exchange rate is absent, see F3).
- Options: (a) date the rate on or before 2026-05-13 (preferred if F3 keeps the rate); (b) remove
  the exchange rate (see F3).
- Needs decision: no

### air/04#F2 · High · AdValoremIndicator true here, false in the forwarding instructions for the same shipment
- XPath: `/Waybill/cbc:AdValoremIndicator` = `true`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:AdValoremIndicator` = `false`
- Why: The UBL definition refers to "ad valorem duties, which are levied on commodities at certain
  rates per centum on their value". Goods, shipment `LD-SH-26-0323` and declared value (512.00 XBL)
  are the same in both documents, so the indicator cannot differ. Read in transport practice as a
  valuation charge on the declared value, `true` would also call for such a charge, which the
  waybill does not state and the forwarder's invoice does not bill
  (`10-Invoice.xml:/Invoice/cbc:LineCountNumeric` = `1`, air freight only).
- Condition: waybill and forwarding instructions carry the same AdValoremIndicator, chosen
  according to the definition (whether Lisavu's duty on these goods is ad valorem).
- Options: (a) align both on the duty treatment of HS 7325.99 in Lisavu (preferred, follows the
  definition); (b) remove the indicator from both documents if nobody acts on it.
- Needs decision: no

### air/04#F3 · Low · Exchange rate XBL→XLC with nothing in the waybill in XLC
- XPath: `/Waybill/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/Waybill/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- Why: The waybill states no charges at all (no freight, no charges collect at destination) and its
  only amounts are the declared values in XBL. An exchange rate is what a waybill carries to convert
  charges collect into the destination currency; here nothing is converted. The rate itself (0.4,
  Multiply) agrees with the world's other XBL→XLC rates.
- Condition: the exchange rate is used by something in the waybill (e.g. charges collect in XLC) or
  is absent.
- Options: (a) preferred: remove it (freight is prepaid by the consignor under CPT and billed in XBL,
  `10-Invoice.xml:/Invoice/cbc:DocumentCurrencyCode` = `XBL`); (b) keep it, dated (F1), together
  with the charges it converts.
- Needs decision: no

### air/04#F4 · Low · Chargeable weight rests on a volume the forwarding instructions do not support
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[1]/cbc:Measure` = `800`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[2]/cbc:Measure` = `300`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[3]/cbc:Measure` = `300`
- Why: ChargeableWeightMeasure is "the weight upon which a charge is to be based". 96 kg is the
  volumetric weight of 0.576 m³ at the IATA ratio of 6000 cm³/kg (own knowledge): 576000 / 6000 =
  96. 0.576 m³ is 8 × 0.072 m³, i.e. eight boxes of 800 × 300 × 300 mm, but the forwarding
  instructions describe one box (LD-AIR-BOX) of those dimensions holding the 8 items, 0.072 m³,
  whose volumetric weight (12 kg) is below the gross weight 81.6 kg; on that description the
  chargeable weight would be the gross weight, rounded up to 82 kg. Which description is right
  decides what the freight costs (see the invoice's own finding on the billed quantity). The
  forwarding instructions' net volume (0.42 m³) does not fit a 0.072 m³ box either, so the package
  data there may be what is wrong.
- Condition: the chargeable weight follows from the packages as described in the flow (count and
  dimensions), and gross volume and package dimensions agree.
- Options: (a) if there are eight boxes, describe them so in the forwarding instructions and keep
  96 kg here (preferred, since the net volume 0.42 m³ needs more than one such box); (b) if there is
  one box, chargeable weight 82 kg and gross volume 0.072 m³.
- Needs decision: yes

## Checked and consistent
- `/Waybill/cbc:DeclaredCarriageValueAmount` = `512.00` and
  `/Waybill/cac:Shipment/cbc:DeclaredForCarriageValueAmount` = `512.00` agree with each other and
  with the forwarding instructions
  (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:DeclaredForCarriageValueAmount` = `512.00`),
  and equal the goods value 8 × 64 XBL.
- 96 kg chargeable = 0.576 m³ / 0.006 m³ per kg; it exceeds the gross weight 81.6 kg, so the
  volumetric weight governs (arithmetic, within this document).
- Exchange rate 0.4 XBL→XLC with operator Multiply matches the world's other rates (e.g.
  `cotton/13-BillOfLading.xml:/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`).

## Considered and refuted
- Missing freight charges and prepaid/collect indication in the waybill — refuted as a finding
  because the Waybill definition says it "may contain" charges, and the payer of the freight is
  clear from the flow (CPT, forwarder's invoice to the consignor); not something the waybill's
  purpose depends on.
- Declared value 512.00 below the Montreal Convention limit (own knowledge: 26 SDR/kg × 81.6 kg),
  which would make the declaration pointless — refuted because XBL is fictional and has no SDR
  conversion in the world.
