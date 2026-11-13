# LLM review: 17-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### sea/17#F1 · Low · Terminal handling charge of the Lisavan terminal in Bayvarran currency, reported to a party that does not pay it
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `185.00`
- XPath: `/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:AllowanceChargeReason` = `Terminal handling at Selanu`
- Why: `ServiceAllowanceCharge` is "a service allowance charge associated with this piece of transport equipment". The status comes from the Port of Selanu (Lisavu), the terminal that performs the handling, and the charge is in XBL (lume, Bayvarra). Elsewhere in the flow amounts arising in Lisavu are in XLC (the import declaration `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `19968.000`, the debit note for the Selanu inspection `28-DebitNote.xml:/DebitNote/cbc:DocumentCurrencyCode` = `XLC`). The amount is the same as in the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cac:AllowanceCharge/cbc:Amount` = `185.00`), where it is a carrier's tariff item collected from the consignee (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `Terminal handling at Selanu collect from the consignee.`), so a XBL tariff on the bill of lading is plausible; but a terminal reporting its own handling charge would normally state it in its local currency. Moreover the status goes to Bayforth Forwarding (`/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`), the shipper's forwarder, while the charge is collect from the consignee Velumi Trading; the report does not say who is to pay it, and no later document of the flow bills it.
- Condition: Either the charge is stated in the currency in which the terminal at Selanu bills it, with a reason for that currency, and the report makes clear that the consignee pays it; or the charge is left out of this status report because the bill of lading already carries it.
- Options: (a) preferred: leave the charge out of the status, since the bill of lading already records it as collect from the consignee and the status has no billing purpose; (b) keep it and state it in XLC (185.00 XBL × 0.4 = 74.000 XLC at the flow's rate in `14-BillOfLading.xml:/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`), or explain why the Selanu tariff is in XBL (e.g. a Trade Accord tariff in lume).
- Needs decision: yes

### sea/17#F2 · Low · Tax registrations and share capital of carrier and receiver in a terminal status report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- Why: A transportation status reports the progress of a transport. The Bayvarran state sales-tax registrations of Tidewell Ocean Lines and Bayforth Forwarding, and Tidewell's share capital, have no use in a discharge/availability report from the terminal at Selanu (section 4.8: master data copied into a document that does not use it).
- Condition: Carrier and receiver carry tax schemes and capital data only if the status has a stated use for them.
- Options: (a) preferred: leave them out, keeping identification, name, address and contact; (b) keep them with a stated reason.
- Needs decision: no

## Checked and consistent
- The charge 185.00 XBL equals the terminal handling charge on the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cac:AllowanceCharge/cbc:Amount` = `185.00`); `ChargeIndicator` true and reason code HD (Handling, UN/EDIFACT 7161) fit a terminal handling charge.
- Tax schemes of Tidewell (`CO-1235754`) and Bayforth (`CO-1234932`) match their descriptions in the other examples of the flow.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DetentionTransportEvent/cbc:Description` = `Wooden pallets must carry the heat-treatment mark.`: suspected detention costs that should appear as a charge — refuted because the event only records a hold for a phytosanitary check, which was completed the same day (`/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:QuarantineTransportEvent/cbc:CompletionIndicator` = `true`); no detention charge is implied.
