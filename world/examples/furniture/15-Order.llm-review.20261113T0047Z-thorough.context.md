# LLM review: 15-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/15-Order.xml`, Git blob `c87a13cb9349700b274d702bf91f928dddf95d64` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/15#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/15#F2 · Low · Office furniture charged to the parks renewal programme
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- Why: `AccountingCost` is "The buyer's accounting cost centre, applied to the Order as a whole". The order is for six office desks and their installation, delivered to the department's offices on Civic Square; the work report and the invoice place it in the office project (`16-WorkReport.xml:/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`, phase "Furnishing: the new office is furnished"). A parks renewal programme as the cost centre for furnishing a new office does not fit the situation, unless the office belongs to the parks programme, which nothing says.
- Condition: the cost centre is one the office furnishing is plausibly charged to, consistently in the order, the work report and the invoice, or the story says why the parks programme pays for the office.
- Options: (a) an office or facilities cost centre (e.g. matching `PWD-PLAN-OFFICE-26`) in 15, 16 and 17 (preferred); (b) state that the new office is the parks programme's site office.
- Needs decision: yes

### furniture/15#F3 · Low · Customs trader number of the buyer in a domestic order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The public works department is identified by its register number; the additional identifier is its customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`). This order is entirely domestic (Marrowdale to Lumeport, both Bayvarra) and has no customs aspect, so the identifier is master data the document does nothing with (section 4.8). It is carried in all three documents of this sub-flow (15, 16, 17) and in the tender and contest flows (Grep over `world/examples/*/*.xml`: 3 files here, 36 in tender, 16 in contest).
- Condition: the customs trader number is present only in documents with a customs purpose.
- Options: (a) remove it here (preferred); (b) none other seen.
- Needs decision: no

## Checked and consistent
- Line amounts: 6 × 880 = 5280 and 14 h × 48 = 672, total 5952 = anticipated total.
- The installation line ("per hour per installer", 14 h) agrees with the work report `16-WorkReport.xml` (two installers, seven hours each).
- `DeliveryParty` and the DAP place (department, Civic Square) are the buyer's own premises, where the desks are installed (`16-WorkReport.xml` activity location).

## Considered and refuted
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`: the maker's brand on the desks — refuted as a problem because, unlike the garden sets, these are the maker's own products.
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `940330`: HS code in a domestic order — refuted because it belongs to the item's description and serves statistics as well as customs.
