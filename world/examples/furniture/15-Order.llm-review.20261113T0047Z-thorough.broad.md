# LLM review: 15-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/15#F1 · Medium · Public works department described as a company in the commercial register
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Lumeport Public Works Department is a department of a public authority (ISIC 8411, exempt as a public body). Its legal entity says it is registered in the commercial register (`CorporateRegistrationTypeCode` COMMERCIAL, the federal business register) and gives it a liquidation status ("A code signifying the party's liquidation status"). A public department is not a company in a commercial register and cannot be in liquidation; the description does not fit the kind of party. The same description is used in all three examples where the department appears (15, 16, 17).
- Condition: The department's legal entity describes a public body: no liquidation status, and a registration scheme (if any) that registers public bodies, not the commercial register.
- Options: (a, preferred) the legal entity of the city of Lumeport (the legal person the department belongs to) with a public-body register or none, without `CompanyLiquidationStatusCode`; (b) drop `PartyLegalEntity` and keep the party identification.
- Needs decision: no

### furniture/15#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/15#F3 · Low · Office furniture charged to the parks renewal programme
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `16-WorkReport.xml:/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: The order is for office desks and their installation; the work report places the work in project `PWD-PLAN-OFFICE-26` and phase "Furnishing: the new office is furnished". The buyer's accounting cost is the "Parks renewal programme 2026" (`PWD-PARKS-26`), the same in order 15, work report 16 and invoice 17. Furnishing an office from a parks programme is at least unexplained.
- Condition: The buyer's accounting cost centre matches the purpose of the purchase (the new office), or the documents say why the parks programme pays for it.
- Options: (a, preferred) a cost code and text for the office project (e.g. matching `PWD-PLAN-OFFICE-26`); (b) a note that the new office belongs to the parks programme.
- Needs decision: yes

### furniture/15#F4 · Low · Customs trader number of the public works department in a domestic purchase
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department's `AdditionalPartyIdentification` is its customs trader number. Furniture made in Bayvarra is bought, delivered and installed in Bayvarra; no customs procedure is involved, so the identifier is master data the document does nothing with (IND5).
- Condition: The customs trader number appears only in documents that involve a customs procedure.
- Options: (a, preferred) remove it from this document.
- Needs decision: no

## Checked and consistent
- 6 desks × 880 = 5 280; 14 h × 48 = 672; together 5 952 = taxable amount = anticipated total; tax 0.00, exempt as a sale to a public body, matching the party's own exemption reason in its tax scheme.
- The order's 6 desks and 14 hours are what `16-WorkReport.xml` reports and `17-Invoice.xml` bills.
- GTIN `9523710000029` check digit correct; HS 940330 and CPC 38122 fit wooden office desks; dimensions 1600 × 800 × 740 mm agree with the description.
- Buyer contact (procurement office, procurement officer, procurement) fits the buying role.
