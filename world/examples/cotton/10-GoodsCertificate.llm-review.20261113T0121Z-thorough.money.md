# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/10-GoodsCertificate.xml`, Git blob `a573492644f6156f64f31e963d3578b9c5d69634` (committed)
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

### cotton/10#F1 · Low · Customs value in a phytosanitary certificate
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `6055.452`
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- Why: `DeclaredCustomsValueAmount` is "the total declared value for customs purposes of the goods
  item". This document is a phytosanitary certificate: it attests that the lint is free of named
  pests, and its issuer (the Selanu Chamber of Commerce, against Bayvarra's plant health rules) assesses nothing on
  value. The customs value belongs to the customs declarations 11 and 15, where it is declared; in
  the certificate it has no use (rule "no fillers", section 4.8). The value itself is correct (the
  invoice value of 16).
- Condition: the phytosanitary certificate carries a customs value only if the certificate or its
  fee depends on it.
- Options: (a, preferred) drop the customs value from the certificate.
- Needs decision: no

### cotton/10#F2 · Low · Importer's sales-tax registration in a phytosanitary certificate
- XPath: `/GoodsCertificate/cac:ImporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: the certificate bills nothing and assesses no tax; the mill's Coastal State sales-tax
  registration has no use in it (section 4.8, master data copied into a document that does not use
  it).
- Condition: no party tax registration in the certificate unless the certificate does something
  with it.
- Options: (a, preferred) drop the importer's `PartyTaxScheme`.
- Needs decision: no

## Checked and consistent
- 6 055.452 XLC is the order and invoice value (08, 16) and, at 0.4 XLC per XBL, the 15 138.63 XBL declared at import (15).
