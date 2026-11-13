# LLM review: 10-GoodsCertificate.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

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

### cotton/10#F1 · High · "10 bales sampled out of 80", but the shipment has 27 bales
- XPath: `/GoodsCertificate/cac:Attestation/cbc:Note` = `10 bales sampled out of 80.`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description[2]` = `Ginned cotton lint, not carded or combed, in compressed bales of about 227 kg.`
- Why: The certificate covers the shipment `SCG-SH-26-0200` with one goods item of 6129 kg of lint in bales of about 227 kg. Calculated: 6129 / 227 = 27 bales (exactly 27 × 227 = 6129). 80 bales would be about 18160 kg (80 × 227), three times the certified quantity and also about the whole seed-cotton delivery (18000 kg in 03), which at a lint turnout of about a third yields only about 27 bales. The note contradicts the quantity of the goods it certifies.
- Condition: the number of bales stated in the attestation agrees with the quantity certified (27 bales of 6129 kg), or the attestation says that the sample was drawn from a larger lot and which.
- Options: (preferred) "10 bales sampled out of 27"; or, if the inspection covered the gin's whole stock, say so and name the lot.
- Needs decision: no

### cotton/10#F2 · High · Version 1 with a "previous version" from last year
- XPath: `/GoodsCertificate/cbc:VersionID` = `1`
- XPath: `/GoodsCertificate/cac:PreviousDocumentReference/cbc:ID` = `SCC-PH-25-0198`
- Why: `PreviousDocumentReference` is "a reference to the previous version of the goods certificate". The certificate is version 1, so it has no previous version. The referenced ID (`SCC-PH-25-…`, a 2025 number in the chamber's phytosanitary series) reads as an earlier season's certificate for another shipment, not a previous version of this one.
- Condition: `PreviousDocumentReference` is present only for a certificate with a previous version, and then refers to it; `VersionID` agrees.
- Options: (preferred) drop the reference (or, if last season's certificate matters, cite it as an additional document with a type that says what it is); or make this version 2 of a certificate whose version 1 was `SCC-PH-25-0198` (unlikely across seasons).
- Needs decision: no

### cotton/10#F3 · Medium · "Original" reference is the classing certificate
- XPath: `/GoodsCertificate/cac:OriginalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/GoodsCertificate/cbc:TypeCode` = `PHYTO`
- Why: `OriginalDocumentReference` is "a reference to the original version of the goods certificate". This is a phytosanitary certificate; `XL-CLS-2026-0042` is the cotton classing certificate attached to the item (same ID in the item's `Certificate`). A classing certificate is not an original version of a phytosanitary certificate; the reference uses an element whose meaning does not fit the document referred to.
- Condition: `OriginalDocumentReference`, if present, refers to an original version of this phytosanitary certificate; the classing certificate is cited only where certificates of the item belong.
- Options: (preferred) drop `OriginalDocumentReference`; the classing certificate is already in the item.
- Needs decision: no

### cotton/10#F4 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cbc:PackSizeNumeric` = `227`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal bale weight in kilograms. The bale count (27), which a certificate based on sampling bales would need, is stated nowhere. Same as in 02, 07, 08, 11, 15 and 16.
- Condition: `PackSizeNumeric`, where present, is a count; the number of bales is stated as a count (e.g. in a package of the goods item) and the nominal bale weight where a weight belongs.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric`; add a `Package` with `Quantity` 27 and a bale packaging type, and the nominal weight as an item property.
- Needs decision: no

### cotton/10#F5 · Low · Classing signed before the ginning of the lot ended
- XPath: `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `/GoodsCertificate/cac:GoodsProcessing/cac:Period/cbc:EndDate` = `2026-02-22`
- Why: The classing certificate of the lint lot is signed on 2026-02-20; according to this certificate the ginning and pressing of that lint ran until 2026-02-22. A certificate for the lot cannot cover bales pressed two days after it was signed. (`ValidationDate` is "the date upon which this signature was verified", which may be later than the signing, but not earlier, so the conflict remains.)
- Condition: the classing certificate of the lot is dated on or after the end of the pressing of its bales, or the processing period ends before it.
- Options: (preferred) end the processing period on or before 2026-02-20 (18000 kg of seed cotton in two weeks is slow for a gin anyway); or date the classing after 2026-02-22.
- Needs decision: no

## Checked and consistent
- Shipment `SCG-SH-26-0200` is the same as in 09, 11, 12, 13 and 15; goods item gross 6190.29 kg = 6129 kg + 61.29 kg packaging (2.27 kg per bale), the same as in 11 and 15, and the definition ("excluding the carrier's equipment") fits.
- Validity 2026-02-28 to 2026-03-14 covers the shipment (bill of lading 2026-03-02) and the import declaration (2026-03-06, 15); the attestation's end date is the same.
- Applicable territory XB is the importing country of 08 and 15.
- Ginning starts on 2026-02-07, after the delivery of the seed cotton on 2026-02-05 (03).
- HS section XI (`NatureCode`) contains heading 5201; cargo type general cargo fits baled cotton.
- `AdditionalDocumentReference` `LTM-PO-26-0198` resolves to the order 08.

## Considered and refuted
- `/GoodsCertificate/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `6129` with unit KGM: a weight in "the number of units making up this goods item" was suspected — refuted because the element is a quantity with a unit code, and a quantity of kilograms is a legitimate quantity of bulk goods.
