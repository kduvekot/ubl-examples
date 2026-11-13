# LLM review: 10-PackingList.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/10-PackingList.xml`, Git blob `aef1ab21426bbd03022aba54b057f406aeb46b61` (committed)
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

### sea/10#F1 · Low · Customs values in a packing list that does nothing with them
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`
- XPath: `/PackingList/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `768.00`
- Why: a packing list is "a document that describes how goods are packed", and this one describes "the container's contents" to be kept "with the container's documents". `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods item"; the customs value is declared in the export declaration (`11-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `49920.00`), which the forwarder lodges from the order and invoice data. Nothing in the packing list's purpose (packages, quantities, weights) uses a customs value, and it travels with the container, where commercial values are usually kept off the transport documents. The values look carried over from the goods-item master data (no fillers).
- Condition: the packing list carries customs values only if a party uses the packing list for a customs purpose that the document makes clear; otherwise it carries none.
- Options: (a) preferred: remove the customs values from the packing list; (b) keep them and state the customs use (e.g. that the packing list accompanies the export declaration as a supporting document).
- Needs decision: no

## Checked and consistent
- The values equal the order lines (96 × 520.00 = 49,920.00; 12 × 64.00 = 768.00), the goods-item values of the export declaration and the invoice lines; currency XBL as in all documents of the sale.
