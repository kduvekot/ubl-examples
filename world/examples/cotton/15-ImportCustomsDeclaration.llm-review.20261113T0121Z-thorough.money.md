# LLM review: 15-ImportCustomsDeclaration.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/15-ImportCustomsDeclaration.xml`, Git blob `243bca671cf988608608ddfeb177ea4ed50c7765` (committed)
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

### cotton/15#F1 · Low · Import customs value is the FOB value; the sea freight to Lumeport is not in it
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `15138.63`
- XPath: `16-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `2950.00`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods
  item". 15 138.63 XBL is exactly the FOB invoice value 6 055.452 XLC at 0.4 XLC per XBL, i.e. the
  value at the port of Selanu. The goods were bought FOB (08), and the mill pays 2 950.00 XBL of sea
  freight to bring them to Lumeport (17). Many customs administrations value imports at the
  border, CIF, adding freight and insurance to the transaction value (own knowledge of the WTO
  Valuation Agreement, Art. 8.2, which leaves the choice to each member); then the customs value
  would be 15 138.63 + 2 950.00 = 18 088.63 XBL. Whether Bayvarra values imports FOB or CIF is a
  rule of the world that the flow does not show; with a CIF rule this value is too low.
- Condition: the customs value follows Bayvarra's valuation basis: the FOB value if Bayvarra
  values FOB, or the FOB value plus the freight (and insurance, if any) to Lumeport if it values
  CIF.
- Options: (a) keep 15 138.63 XBL if Bayvarra values imports FOB, and record that rule in the
  world's story; (b) if Bayvarra values CIF, declare 18 088.63 XBL. No preference without the rule.
- Needs decision: yes

## Checked and consistent
- 6 055.452 XLC / 0.4 = 15 138.63 XBL, the same rate (1 XBL = 0.4 XLC) as in 04, 05, 09 and 13; the export value in 11 and the certificate value in 10 are the same 6 055.452 XLC.
- The importer's sales-tax registration (`PartyTaxScheme`, Coastal State STT) has a use here: import into Bayvarra is where the mill's sales-tax status applies.

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`: a statement about duties without any duty amount or rate was suspected of lacking what the note refers to — refuted because the Import Customs Declaration has no element for assessed duties (they are assessed by customs on the declared value), and the note says how they will be paid, which is what the importer can state.
