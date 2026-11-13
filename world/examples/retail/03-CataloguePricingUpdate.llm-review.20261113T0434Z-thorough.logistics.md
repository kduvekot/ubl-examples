# LLM review: 03-CataloguePricingUpdate.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/03-CataloguePricingUpdate.xml`, Git blob `fa746f7555ca2bc6ffeef41cf02e3ca5ac1ffe9d` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 89446f0 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/03#F1 · High · Pricing update line points to the bench line, but the update is for the side frame
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cbc:ID` = `1`
- XPath: `/CataloguePricingUpdate/cbc:Name` = `Price change of the side frame`
- XPath: `/CataloguePricingUpdate/cac:CataloguePricingUpdateLine/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `58`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cbc:ID` = `2`
- Why: UBL defines CataloguePricingUpdateLine/ID as "An identifier for the catalogue line to be updated." The line carries no Item, so the ID is the only link to the catalogue. Line `1` of the catalogue LD-CAT-26-0218 is the park bench at 520 XBL; the side frame, at 64 XBL, is line `2`. As written, the update lowers the price of the bench from 520 to 58 XBL, which contradicts the document's name and description.
- Condition: the pricing update line identifies catalogue line 2 (the side frame), so that the new price 58 XBL applies to the side frame.
- Options: (a, preferred) line ID `2`, matching the catalogue line; (b) additionally carry the item's identification (the update line has no Item element in UBL 2.5, so the ID must be right).
- Needs decision: no

### retail/03#F2 · High · Reference to the catalogue gives an issue time and a revision that the catalogue does not have
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CataloguePricingUpdate/cac:RelatedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:RevisionDate` = `2026-04-20`
- XPath: `/CataloguePricingUpdate/cbc:IssueDate` = `2026-05-20`
- Why: The reference repeats data of the referenced catalogue 02. Its IssueTime ("The time at which the catalogue was issued") is 09:00, but 02 was issued at 17:28 (09:00 is 02's RevisionTime). Its RevisionDate/RevisionTime ("The date on which the information in the catalogue was last revised") are 2026-05-21 14:00, a day after this document was issued (2026-05-20 13:10) and therefore in the future; the catalogue itself was last revised on 2026-04-20 09:00. The same reference values recur in 04 and 20.
- Condition: the reference's IssueDate/IssueTime equal those of 02-Catalogue, and its revision date and time are 02's revision (or the last revision before this document's issue), never after this document's issue time.
- Options: (a, preferred) IssueTime `17:28:00`, RevisionDate `2026-04-20`, RevisionTime `09:00:00`; (b) drop the revision date and time from the reference, since the UUID and ID already identify the catalogue.
- Needs decision: no

### retail/03#F3 · Medium · Revision time after the document's issue time
- XPath: `/CataloguePricingUpdate/cbc:RevisionTime` = `14:00:00`
- XPath: `/CataloguePricingUpdate/cbc:IssueTime` = `13:10:00`
- XPath: `/CataloguePricingUpdate/cbc:RevisionDate` = `2026-05-20`
- Why: RevisionDate/RevisionTime are "The date/time, assigned by the seller, at which the Catalogue was revised". A document issued at 13:10 cannot report a revision made at 14:00 the same day. If 14:00 is meant as the time from which the new price applies, that is the validity period's job (`/CataloguePricingUpdate/cac:ValidityPeriod/cbc:StartDate` = `2026-05-20`, which could carry a StartTime).
- Condition: the revision date and time are not later than the issue date and time.
- Options: (a, preferred) RevisionTime at or before 13:10; (b) if the change takes effect at 14:00, put that in ValidityPeriod/StartTime and set the revision time to when the revision was made.
- Needs decision: no

## Checked and consistent
- RelatedCatalogueReference ID `LD-CAT-26-0218` and UUID `f5163e36-0159-5b9f-b172-a86137e369e6` match 02-Catalogue; VersionID 1.0 and PreviousVersionID 0.9 match 02; this update's VersionID 1.1 follows 1.0.
- Validity 2026-05-20 to 2026-07-19 lies within the catalogue's validity (02: 2026-04-20 to 2026-07-19), starts on the issue date, and matches the new price list's validity.
- PreviousPriceList `LD-PL-2026` is the price list of 02 (`02-Catalogue.xml:/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID` = `LD-PL-2026`), now marked `REPLACED`.
- LineCountNumeric `1` equals the number of update lines.
- ReferencedContract `LD-BM-SUPPLY-2026` as in 01 and 02.

## Considered and refuted
- `/CataloguePricingUpdate/cbc:IssueDate` = `2026-05-20`: suspected out of order (issued after the order 08 of 2026-04-24 and the invoice 18 of 2026-04-30) — refuted because a price change during the catalogue's validity is a later event of the same collaboration; nothing in the flow depends on it before 2026-05-20.
