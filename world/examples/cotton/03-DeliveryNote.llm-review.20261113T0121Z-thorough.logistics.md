# LLM review: 03-DeliveryNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/03-DeliveryNote.xml`, Git blob `82936eac57b6612b28fe4c2e5e37c1c570ac7654` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### cotton/03#F1 · Low · Shipment gross weight fits neither "goods plus equipment" nor a loose delivery
- XPath: `/DeliveryNote/cac:Shipment/cbc:GrossWeightMeasure` = `20400`
- XPath: `/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000`
- XPath: `/DeliveryNote/cbc:Note[2]` = `Three trailer loads, weighed at the gin.`
- Why: `Shipment/GrossWeightMeasure` is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The seed cotton is "delivered loose by trailer", so there is no packaging. Calculated: 20400 − 18000 = 2400 kg for three trailer loads, 800 kg per trailer. A trailer carrying 6000 kg of loose seed cotton (18000 / 3) needs, at a loose bulk density of roughly 80–150 kg/m³ (own knowledge), 40–75 m³ of body; such a trailer weighs several tonnes empty, not 800 kg. If the trailers are counted, the gross weight is far too low; if they are not, the gross weight of a loose delivery equals the goods (18000 kg) and the 2400 kg are unexplained. They may be the weighed seed cotton before a trash or moisture deduction, but then the difference is a deduction, not packaging or equipment, and nothing in the document says so.
- Condition: the gross weight is goods plus packaging plus transport equipment and is plausible for three trailer loads, or the difference between gross and delivered quantity is explained by an element or note that says what it is.
- Options: (preferred) if 18000 kg is the net weight after a deduction at the weighbridge, state the weighed and the deducted weights explicitly (e.g. in the note, or the delivered quantity as weighed and the deduction in the self-billed invoice); or set the gross weight to goods plus the three trailers' tare; or drop the gross weight.
- Needs decision: yes (what the 2400 kg are is part of the story of the delivery)

### cotton/03#F2 · Low · Weighbridge ticket referenced by ID only
- XPath: `/DeliveryNote/cac:AdditionalDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- Why: `AdditionalDocumentReference` is "a reference to an additional document associated with this document"; with only an ID it does not say what the document is. From the note ("weighed at the gin") and the prefix it is the gin's weighbridge ticket, which 04 and 05 cite as a receipt document. No example of the flow has this ID, so the reader cannot tell its kind from the flow either.
- Condition: the reference says what kind of document it is (e.g. `DocumentType` or `DocumentTypeCode`), consistently with how 04 and 05 cite the same ID.
- Options: (preferred) add a document type ("Weighbridge ticket") to the reference; or drop it if the note is enough.
- Needs decision: no

## Checked and consistent
- Delivered quantity 18000 KGM agrees with `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` and with the line reference there (`DeliveryNoteLineReference/LineID` 1, document `LCF-DN-26-0193`).
- Actual delivery date 2026-02-05 equals the issue date and the delivery date in 04 and 05.
- Lint turnout: the 6129 kg of lint ordered and shipped (08, 10–16) are 34.05 % of 18000 kg seed cotton (6129 / 18000), within the usual 33–40 % (own knowledge).
- Item `LCF-SC`, HS 520100 and CPC 01921 agree with 01, 04 and 05.

## Considered and refuted
- `/DeliveryNote/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`: a call-off number not found as a document in the flow was suspected as a broken reference — refuted because it is a call-off under the season agreement `SCG-SEASON-2026`, assigned by the buyer (the gin, prefix SCG) as the definition requires, and not a UBL document of the flow.

