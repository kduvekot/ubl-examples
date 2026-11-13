# LLM review: 14-BillOfLading.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/14-BillOfLading.xml`, Git blob `661653ae609f88a3a1ea21ce846d10c0b8de2faf` (committed)
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

### sea/14#F1 · High · Total invoice amount is the goods value, not the invoice amount
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:TotalInvoiceAmount` = `50688.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:Amount` = `53778.00`
- Why: `TotalInvoiceAmount` is "the total of all invoice amounts declared in this consignment". The consignment is invoiced once, by Lumeway to Velumi, for 53,778.00 lume (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`): goods 50,688.00 plus sea freight 2,950.00 and insurance 140.00. The bill of lading states 50,688.00, the goods value only (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`), while its own delivery terms give the CIF amount of 53,778.00 for the same sale. The two amounts in this consignment and the invoice disagree on what was invoiced.
- Condition: the consignment's total invoice amount equals the total of the invoice(s) for the goods of the consignment (53,778.00 with the invoice as it stands), or is absent.
- Options: (a) preferred: 53,778.00, the invoice total, which also matches the delivery-terms amount; (b) remove the element if the carrier is not meant to state invoice amounts (the B/L is issued before the invoice on the same day).
- Needs decision: no

### sea/14#F2 · Low · Pre-carriage freight of 310.00 that no one bills, for haulage the shipper arranges
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:FreightAllowanceCharge/cbc:Amount` = `310.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:PrepaidPaymentTerms/cbc:Note` = `Ocean freight and bunker surcharge prepaid by the shipper.`
- Why: the ocean carrier's bill of lading states a freight charge of 310.00 for the pre-carriage by road from Marrowdale to Lumeport, performed by Bayforth Forwarding. The shipper booked that leg as merchant haulage (`09-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:OriginalDespatchTransportationService/cbc:TransportServiceCode` = `MERCHHAUL`), i.e. outside the carrier's contract of carriage, and the B/L's own payment terms cover only the ocean freight and bunker surcharge. The charge appears in no other document of the flow: Bayforth's invoice to Lumeway bills sea freight, the export declaration and the insurance only (`18-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00` = 2,950.00 + 85.00 + 140.00), and Lumeway's invoice to Velumi does not pass it on. So it is unclear on what terms 310.00 is payable and by whom.
- Condition: the pre-carriage charge, if stated in the B/L, is a charge under the B/L's contract of carriage with payment terms, and it is billed in the flow by the party that performed the haulage; or the B/L does not state it.
- Options: (a) preferred: remove the pre-carriage freight from the carrier's B/L (merchant haulage is not the carrier's charge) and, if Bayforth's haulage is to be paid, bill it in Bayforth's invoice; (b) make the pre-carriage carrier haulage under the B/L (the carrier subcontracting Bayforth) and include it in the prepaid freight terms.
- Needs decision: yes

### sea/14#F3 · Low · Deductible and excess of the policy both 250.00
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:DeductibleAmount` = `250.00`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ExcessAmount` = `250.00`
- Why: `DeductibleAmount` is "the deductible amount specified in the policy" and `ExcessAmount` "the excess amount specified in the policy". In cargo insurance "excess" and "deductible" name the same thing (the part of each loss borne by the insured; my own knowledge of insurance terms); stating both with the same figure either repeats one term or claims two separate retentions of 250.00 on one loss. The document does nothing that needs both.
- Condition: the policy states one retention, in the element that fits it, or two retentions that are distinct and explained.
- Options: (a) preferred: keep one (e.g. `ExcessAmount`) and drop the other; (b) if the world's policy really has two different retentions, give them different meanings and amounts.
- Needs decision: no

### sea/14#F4 · Low · One insurance policy split over two aggregates, each incomplete
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- XPath: `/BillOfLading/cac:Shipment/cac:InsurancePolicy/cac:InsurerParty/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: the consignment's policy has the policy number, cover, premium, broker, holder and beneficiary but no insurer; the shipment's policy has the insurer and the same insured value and excess but no policy number. Read as written, the shipment (which has only this one consignment) is covered by two policies of 59,155.80 each, i.e. 118,311.60 in total, more than the 110 % of CIF value that the cover is based on. The import declaration knows only one policy (`19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`).
- Condition: the bill of lading describes the cargo policy once, at one level, with its number, insurer, insured value, retention and premium together.
- Options: (a) preferred: one `InsurancePolicy` on the consignment with the insurer added, and none on the shipment; (b) one on the shipment, if the policy is meant to cover the shipment as a whole.
- Needs decision: no

### sea/14#F5 · Low · Exchange rate that no amount in the bill of lading uses, and without a date
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ExchangeRate` is "information that directly relates to the rate of exchange (conversion) between two currencies". All 18 amounts of the bill of lading are in lume; none is in coral or to be converted, including the charge collect from the consignee at Selanu (terminal handling, 185.00 lume). A rate without a `Date` also does not say when it applied. The element has no business reason in this document (no fillers); the same unused rate occurs in `09-ForwardingInstructions.xml` and `12-ForwardingInstructions.xml`.
- Condition: the bill of lading carries an exchange rate only if an amount in it is in, or must be converted to, coral, and then with the date it applies to.
- Options: (a) preferred: remove it; (b) keep it with a collect charge stated in coral and a rate date.
- Needs decision: no

## Checked and consistent
- Ocean freight 2,700.00 + bunker surcharge 250.00 = 2,950.00 = the sea-freight charge in the export declaration, in Bayforth's invoice (`18-Invoice.xml`) and in Lumeway's invoice (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`); both prepaid by the shipper, as `08-TransportServiceDescription.xml:/TransportServiceDescription/cac:ServiceChargePaymentTerms/cbc:Note` = `Freight prepaid before the bill of lading is released.` said.
- Insurance: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:InsuranceValueAmount` = `59155.80` = 110 % of 53,778.00; premium 140.00 = 0.24 % of the insured value, billed by the broker Bayforth to the policy holder Lumeway (`18-Invoice.xml`) and passed on to the beneficiary Velumi (`22-Invoice.xml:/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`); holder (seller) and beneficiary (buyer) fit CIF.
- Delivery terms: CIF Selanu, amount 53,778.00 = the invoice total; risk passes on board at Lumeport, as under CIF.
- Terminal handling at Selanu 185.00, for the buyer and collect from the consignee (`/BillOfLading/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `Terminal handling at Selanu collect from the consignee.`), is the same charge the port reports at the container's discharge (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `185.00`).

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:DeclaredCustomsValueAmount` = `53778.00`: suspected a contradiction with the export declaration's 50,688.00 for the same consignment — refuted because the Consignment-level element is the value "regardless of whether they are subject to the same customs procedure", and the B/L serves the import into Lisavu, where the customs value is CIF (goods + freight + insurance = 53,778.00); export at FOB differs by design.
- `/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreeOnBoardValueAmount` = `50688.00`: suspected that, by its UBL definition ("the monetary amount that has to be or has been paid as calculated under the applicable trade delivery"), the value should be the CIF amount — refuted because the element's name and its use in trade data are the FOB value, and the B/L states the CIF amount separately in the delivery terms; the definition's wording is UBL's own looseness.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:AllowanceChargeReasonCode` = `FC`: suspected that a bunker surcharge needs its own code — refuted because UN/EDIFACT 7161 has no specific bunker code and the surcharge is part of the freight service; the reason text names it.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cac:AllowanceCharge/cbc:Amount` = `185.00`: suspected that a charge for the buyer does not belong in "an allowance or charge covered by these delivery terms" — refuted because the delivery terms are where the allocation of destination terminal handling between seller and buyer is settled under CIF, and the reason says it falls to the buyer.
