# LLM review: 06-Waybill.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/06-Waybill.xml`, Git blob `98b3edab06331ce10e3457361c14ccae3bf60af1` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/06#F1 · Medium · Freight rate per tonne carried as base amount, without a multiplier
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:BaseAmount` = `1495`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:FreightAllowanceCharge/cbc:Amount` = `179400`
- Why: `Allowance Charge. Base_ Amount` is "The monetary amount to which the multiplier factor is applied in calculating the amount of this allowance or charge", and `Multiplier_ Factor. Numeric` is "A number by which the base amount is multiplied". Here the base amount holds the rate per tonne (1,495 `XUF`), and there is no multiplier: read by its definition, a base of 1,495 cannot give an amount of 179,400. The amount is the rate × 120 t (1,495 × 120 = 179,400, the same as `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `179400`). UBL has an element for this: `Per Unit_ Amount`, "The allowance or charge per item; the total allowance or charge is calculated by multiplying the per unit amount by the quantity of items".
- Condition: the freight charge either carries the rate as a per-unit amount, or a base amount and multiplier whose product is the charge amount; in both cases the amount stays 179,400 `XUF`.
- Options: (a, preferred) move 1,495 to `PerUnitAmount` (the quantity, 120 t, is in `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableQuantity` = `120`); (b) keep `BaseAmount` = 1495 and add `MultiplierFactorNumeric` = 120.
- Needs decision: no

### plastics/06#F2 · Low · Value declared for carriage without any valuation charge
- XPath: `/Waybill/cac:Shipment/cac:GoodsItem/cbc:DeclaredForCarriageValueAmount` = `9984000`
- Why: the element is "The value of this goods item, declared by the shipper or his agent solely for the purpose of varying the carrier's level of liability from that provided in the contract of carriage". Declaring the full goods value (here the full `CPT` price) raises the carrier's liability far above the limit of the CMNI (own knowledge: 666.67 SDR per package or 2 SDR per kg); carriers charge an ad valorem or valuation surcharge for that. Neither the transport plan (`04-TransportExecutionPlan.xml`) nor the freight invoice (`07-Invoice.xml:/Invoice/cbc:LineCountNumeric` = `1`, only the freight line) contains such a charge, and `/Waybill/cbc:AdValoremIndicator` = `false`. A business reason does exist in the flow: the goods are declared uninsured (`09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:InsuranceValueAmount` = `0.00`). Whether the declared value is part of the story is a decision.
- Condition: either the declared value for carriage is agreed in the transport contract and its cost is billed (or explicitly included in the freight), or the element is absent.
- Options: (a, preferred) keep the declared value and add the matching valuation charge to the freight (waybill charge and freight invoice), since the goods travel uninsured; (b) drop the declared value and rely on the CMNI liability limits.
- Needs decision: yes

### plastics/06#F3 · Low · Consignee's bank account in the waybill
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". The consignee pays nothing to the carrier under this waybill (freight billed to Rinova, `07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Rinova Recovery`); its current account is copied master data. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the consignee party in the waybill carries no financial account unless the waybill uses it (e.g. freight or cash on delivery collected from the consignee).
- Options: (a, preferred) drop it.
- Needs decision: no

## Checked and consistent
- Freight arithmetic: 1,495 `XUF` per tonne × 120 t (`/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableQuantity` = `120`, `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ChargeableWeightMeasure` = `120000` kg) = 179,400 `XUF`, equal to the freight invoice line (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `120`, price 1,495, line 179,400) and to the freight deducted for the FOB value in `09-ImportCustomsDeclaration.xml` ((99,840 − 98,046) × 100 = 179,400).
- `/Waybill/cac:Shipment/cac:GoodsItem/cbc:ValueAmount` = `9984000` ("The amount on which a duty, tax, or fee will be assessed") equals the import customs value `09-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99840.00` `XBL` at 100 `XUF` = 1 `XBL`, and the export value in `05-ExportCustomsDeclaration.xml`.
- Reason code `FC` (UNCL 7161 "Freight service") fits a freight charge.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false` next to a declared value for carriage — refuted as a contradiction: UBL defines the indicator by ad valorem duties ("certain duties, called ad valorem duties, which are levied on commodities at certain rates per centum on their value"), not by ad valorem freight, so it says nothing about the carrier's liability (it is used as supporting evidence in F2 only).
- Chargeable weight 120,000 kg is the net weight, not the gross 120,480 kg — refuted: the freight is agreed and invoiced per tonne of product (`07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity` = `1`, unit tonne, 120 t), and the chargeable weight is whatever the contract makes it.
- No statement who pays the freight (prepaid / collect) — refuted: nothing is implied by absence; the transport plan names Rinova as bill-to party and the freight is invoiced to Rinova.
