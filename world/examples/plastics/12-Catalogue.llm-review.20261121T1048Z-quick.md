# LLM review: 12-Catalogue.xml

Flow: plastics (26-0373) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/plastics/12-Catalogue.xml`, Git blob `01d05b88b5177bd43184f34f739d9e1c18be07e1` (committed)
- Last commit changing the example: c02a7150 2026-11-20 Published text: finding IDs and UBL rule numbers into code comments; O265: ISO 14083, the Accord's recycled-content tracing, Urvania's own waste list, no VATEX or EU company-law sentences
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### plastics/12#F1 · High · The certifier's register number belongs to another company
- XPath: `/Catalogue/cac:CatalogueLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyIdentification/cbc:ID` = `XU-R-106192`
- XPath: `/Catalogue/cac:CatalogueLine/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Certovira Certification`
- Why: `XU-R-106192` in the Urvanian commercial register is Tostara Wood Modification in every other example that carries it (`modification/08-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Tostara Wood Modification SRU`; also `modification/01-Order.xml`, `modification/03-DespatchAdvice.xml`, `wood/02-Quotation.xml`, `wood/06-DespatchAdvice.xml` and others, 12 examples counted with grep over `*.xml`). One register number cannot identify two companies; Certovira Certification occurs nowhere else in the examples, so it has no number of its own to compare with.
- Condition: the certificate issuer's identifier is unique to Certovira Certification and does not identify any other party in the examples.
- Options: (a) give Certovira its own register number (preferred: the issuer of the Accord's recycled-content certificate is a party of its own); (b) if the certificate is in fact issued by an existing party, name that party and its identifier.
- Needs decision: no

### plastics/12#F2 · Low · The catalogue price does not say what delivery it includes
- XPath: `/Catalogue/cac:CatalogueLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `83200`
- Why: a trade price of 83,200 XUF per tonne for the Bayvarran territory, with a five-day lead time, is quoted without its delivery basis. The order placed at this price buys it CPT to the river quay at Lumeport (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CPT`), and the seller pays the barge (`03-TransportExecutionPlanRequest.xml` names Rinova as bill-to party), so the price includes carriage to Lumeport — something the buyer can only learn from the order. Catalogue has no delivery-terms element, but its TradingTerms can state the basis.
- Condition: the catalogue states the delivery basis of its price (e.g. CPT Lumeport river quay), so that the order's terms follow from it.
- Options: (a) add a `cac:TradingTerms` with the delivery basis (preferred); (b) state it in the price list or the price type text.
- Needs decision: no

## Checked and consistent
- Price, item identifiers (`RR-PE-R1`, `KXU13362PER1`), and the description (granulate in 1-tonne jumbo bags) agree with `01-Order.xml` and `10-Invoice.xml` (83,200 XUF per tonne, 120 t); the order of 13 April falls within the catalogue's validity (1 April – 30 June).
- HS 390110 (polyethylene of specific gravity below 0.94, in primary forms) fits a granulate of density 0.92 g/cm³; granules count as primary forms (own knowledge of chapter 39, note 6).
- Tax: category G with the Urvanian export exemption, for the Bayvarran sales territory; VAT scheme of Urvania.
- 100 % recycled content in the circularity profile agrees with the certificate's remarks and the description ("recovered from production waste").
- The Urvanian and English renderings of name, description, address and legal form carry the language tags `qau` and `en-XU`.

## Outside this review
- `01-Order.xml` does not refer to this catalogue although it orders at its price; whether it should is for that example's review.
