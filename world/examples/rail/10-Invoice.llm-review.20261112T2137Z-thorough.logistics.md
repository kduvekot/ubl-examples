# LLM review: 10-Invoice.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/10-Invoice.xml`, Git blob `13c4e7c68f3fa88f617d5f615a40ea35e815c2cd` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/10#F1 · Low · Reference to the waybill with only an ID
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`
- Why: The reference resolves to the waybill rail/08, the transport document of the service billed, but carries no DocumentTypeCode or DocumentType, so the receiver cannot tell from the invoice what FRC-WB-26-0334 is. The checklist asks a reference with only an ID to say what it refers to where that is not obvious; an invoice's AdditionalDocumentReference can be any document.
- Condition: The reference says what kind of document it is (type code or text).
- Options: add `cbc:DocumentTypeCode` (e.g. the world's code for a consignment note) or `cbc:DocumentType` (preferred); alternatively reference the waybill through `cac:DespatchDocumentReference`, if the owner reads a consignment note as such.
- Needs decision: no

## Checked and consistent
- Billed quantity 2 service units (E48) = two container slots = the two containers FRXU1044175 and FRXU1044180 of rail/08; price 54 600 XUF per slot equals the waybill's freight charge per container (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:Amount` = `54600`).
- The item ("one container slot on the container train to the distributor's siding") agrees with the waybill's delivery location (Lumeway siding, Marrowdale) and the plan's contract for container slots between the hub and Marrowdale.
- Issue 2026-04-17, after the planned delivery 2026-04-15 (rail/03, rail/07, rail/08) and within the plan's validity (to 2026-04-17).
- Parties: the invoice goes to Valdara Industries, the bill-to party of rail/02 and rail/03.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description[2]` = `One container slot on the container train to the distributor's siding.`: the invoice bills only the rail slots, while the waybill says the carrier also hauls the boxes from the warehouse to the hub — refuted within this lens: whether the carrier haulage is priced into the slot or billed separately is a question of the money review; nothing in this invoice contradicts a logistics value.
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `FRC-WB-26-0334`: the referenced waybill is typed as a road consignment note (CMR) although the invoice bills rail carriage — refuted as a finding of this example: the problem lies in the waybill and is raised there (rail/08#F1).

## Outside this review
- The waybill's freight charge of 54 600 XUF is given on the first container only (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:FreightAllowanceCharge/cbc:ChargeIndicator` = `true`), while this invoice bills two slots; whether the waybill should carry the charge for both boxes belongs to the waybill's (money) review.
