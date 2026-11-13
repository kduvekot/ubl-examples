# LLM review: 29-PurchaseReceipt.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/29-PurchaseReceipt.xml`, Git blob `9863e47f157fcadd2d5f437f7b6156444ebcc978` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/29#F1 · Low · The point of sale is named by company and street instead of described as a place
- XPath: `/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Name` = `Velumi Trading, Reef Street, Selanu`
- Why: PointOfSaleLocation is "the location of the point of sale where this purchase took place";
  its Name should name the place (e.g. the shop or trade counter), while street and town belong in
  the location's Address. Here the name strings together the company, the street and the town, so
  the address parts are not in their elements.
- Condition: the location's name names the shop or counter, and street and town are given in
  Location/Address (or left out, if the seller's address already says it).
- Options: (a, preferred) Name "Trade counter" (or similar) with an Address Reef Street, Selanu;
  (b) drop the name and keep only the cash register.
- Needs decision: no

## Checked and consistent
- Physics: two Serra 180 benches, 1800 × 620 × 780 mm each and about 41.5 kg gross (3984 kg for
  96 benches in 10-PackingList.xml), together about 83 kg and 1.7 m³ of envelope: fits the note
  "collected by the farm with its own trailer".
- The item (GTIN 9520610000012, check digit correct) is the bench imported in this flow; "imported
  from Bayvarra" agrees with 14-BillOfLading.xml and 19-ImportCustomsDeclaration.xml; 2 × 289 =
  578.000 XLC equals the payment.
- The farm's coordinates (39°58.80'S 15°07.80'W) lie about 2.4 nm from the Port of Selanu
  (40°01.20'S 15°08.40'W, 16-CommonTransportationReport.xml), on the island: Δlat 2.4' = 2.4 nm,
  Δlon 0.6' × cos 40° = 0.46 nm.
- Sale on 2026-06-13, after the goods were received at Nalevi on 2026-05-21 (21-ReceiptAdvice.xml).
