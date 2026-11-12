# LLM review: 07-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/07-CertificateOfOrigin.xml`, Git blob `9dd12c4b7afb7cb32c342c0e094823576afb0a28` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/07#F1 · Low · Customs values on a certificate of origin that grants origin by processing
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `71760`
- Why: Goods Item. Declared Customs_ Value. Amount is "The total declared value for customs purposes of the goods item." A certificate of origin certifies where the goods come from; the origin rule stated here is a processing rule (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:Remarks` = `Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.`), not a value-added rule, so neither the chamber nor the importing customs needs the customs value from this document: the import declaration carries its own value (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`, in XBL). Preferential certificates in real use (EUR.1, Form A) carry no value unless a value criterion applies; some chambers do charge fees by invoice value, which would be a reason, but nothing in the example says so. Under the rule "no fillers" a value needs a business reason; I could not settle whether one exists in the world.
- Condition: Either the goods items carry no customs value, or the example gives the reason the chamber needs it (a value-based origin criterion, or a fee based on value), and the values are those of the sale.
- Options: (a) remove the two amounts (preferred: the processing criterion needs no value, and the import declaration carries the value customs uses); (b) keep them and state the reason, e.g. a regional-value-content criterion of the Trade Accord in the remarks.
- Needs decision: yes

## Checked and consistent
- The two values equal the sale's line amounts (96 × 49 900 = 4 790 400 and 12 × 5 980 = 71 760, `15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`) and are in XUF.
