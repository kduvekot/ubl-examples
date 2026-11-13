# LLM review: 20-CatalogueDeletion.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/20-CatalogueDeletion.xml`, Git blob `9caf2f1c11c43a13594e547d7c6d563b86a59b49` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/20#F1 · High · Reference to the deleted catalogue: issue time, revision and previous version do not match the catalogue
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:IssueTime` = `09:00:00`
- XPath: `02-Catalogue.xml:/Catalogue/cbc:IssueTime` = `17:28:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionDate` = `2026-05-21`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:RevisionTime` = `14:00:00`
- XPath: `04-CatalogueItemSpecificationUpdate.xml:/CatalogueItemSpecificationUpdate/cbc:IssueTime` = `09:01:00`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:VersionID` = `1.2`
- XPath: `/CatalogueDeletion/cac:DeletedCatalogueReference/cbc:PreviousVersionID` = `0.9`
- Why: The reference identifies catalogue LD-CAT-26-0218. Its IssueTime is 09:00, but 02 was issued at 17:28. Its last revision is given as 2026-05-21 14:00, but the last revision, the item specification update 04 (version 1.2), was issued on 2026-05-21 at 09:01 and itself states a revision of 2026-05-20 14:00; no document of the flow revises the catalogue at 14:00 on 2026-05-21. PreviousVersionID is "the previous version of the catalogue that is superseded by this version": for version 1.2 that is 1.1 (the pricing update 03), not 0.9. The same reference values occur in 03 and 04.
- Condition: the reference's issue date and time are 02's, its revision date and time are those of the last revision (04), and the previous version of 1.2 is 1.1.
- Options: (a, preferred) IssueTime `17:28:00`, revision of 04 (date and time consistent with 04, see 04/F4), PreviousVersionID `1.1`; (b) drop revision and version details from the reference and keep ID and UUID.
- Needs decision: no

## Checked and consistent
- DeletedCatalogueReference ID `LD-CAT-26-0218` and UUID `f5163e36-0159-5b9f-b172-a86137e369e6` match 02; VersionID 1.2 is the version after 04.
- Effective 2026-06-20 00:00, the moment after the deletion's validity end 2026-06-19 and seven hours after the issue (2026-06-19 17:05); the catalogue would otherwise have run to 2026-07-19, which the note explains ("Replaced by the summer catalogue").
- ReferencedContract `LD-BM-SUPPLY-2026` as in 01–04.
- No order of the flow relies on the catalogue after 2026-06-20 (the last trade order, 08, is from 2026-04-24; 22 is a consumer order to the store).
