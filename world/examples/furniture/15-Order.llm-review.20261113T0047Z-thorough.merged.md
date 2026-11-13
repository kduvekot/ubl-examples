# LLM review: 15-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/15-Order.xml`, Git blob `c87a13cb9349700b274d702bf91f928dddf95d64` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/15#F1 · Medium · Public works department described as a company in the commercial register, with a liquidation status
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `8411`
- Why: The Lumeport Public Works Department is a department of the city administration (ISIC 8411, "General public administration activities"; its tax scheme exempts it as a public body). Its legal entity names the commercial register (world list: COMMERCIAL = "A register of businesses.") and carries `CompanyLiquidationStatusCode` ("A code signifying the party's liquidation status"). A public department is not a business in a commercial register and cannot be in liquidation; the values do not fit the kind of party (the legal form is, correctly, absent). The same description is used in 15, 16 and 17.
- Condition: The department's legal entity describes a public body: no liquidation status, and no commercial-register type (a register of public bodies, or none).
- Options: (a, preferred) drop `CompanyLiquidationStatusCode` and the COMMERCIAL registration scheme, keeping registration name and identifier, or use a world register of public bodies; (b) the legal entity of the City of Lumeport (the legal person the department belongs to), which would change who the party is.
- Needs decision: no
- From: broad (Medium, no), parties (Medium, yes)

### furniture/15#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/15#F3 · Low · Desks and installation ordered without an identified delivery place or a requested date
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Lumeport Public Works Department, Civic Square`
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:ID` = `LUM-ADR-000417`
- Why: The order's `Delivery` names only the receiving party, without `DeliveryLocation`, `DeliveryAddress` or requested period; the place is free text under the delivery terms, although the building is identified in the department's own address by the Lumeport address register, and the postal address is that of the procurement office (room 2.14), not necessarily of the new office to be furnished. For an order with on-site installation the date matters: the work was done on 2026-04-08 and 2026-04-09 (`16-WorkReport.xml:/WorkReport/cac:ReportedPeriod/cbc:StartDate` = `2026-04-08`), which nothing in the order requests. Low: the order can rely on an agreed date outside the document.
- Condition: The order identifies where the desks are delivered and installed (address register ID or full address, with floor or room if different from the procurement office) and states a requested delivery or installation period.
- Options: (a, preferred) `Delivery/DeliveryLocation` with an `Address` carrying `LUM-ADR-000417` (and the office's floor or room) and a `RequestedDeliveryPeriod` 2026-04-08 to 2026-04-09; (b) `Delivery/DeliveryAddress` and a note on the agreed date.
- Needs decision: no
- From: logistics (place and date), parties (place)

### furniture/15#F4 · Low · Office furniture charged to the parks renewal programme
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- XPath: `16-WorkReport.xml:/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`
- Why: `AccountingCostCode` is "The buyer's accounting code, applied to the Order as a whole". The order is for six office desks and their installation; the work report places the work in project `PWD-PLAN-OFFICE-26`, phase "Furnishing: the new office is furnished". The cost centre is the parks renewal programme, which in the tender flow carries the park benches (`tender/26-Order.xml:/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`). Booking office desks to the parks programme is possible (e.g. the new office serves the programme), but nothing in the flow says so, and project and cost centre point to different budgets. The same value is in 15, 16 and 17 (merge: `grep -rl --include='*.xml' PWD-PARKS-26` finds those three and tender 26, 29, 32, 33).
- Condition: The buyer's cost centre for the desks and installation fits the office project, consistently in order, work report and invoice, or the flow states why the parks programme pays for the office.
- Options: (a, preferred) a cost centre for the office project (e.g. matching `PWD-PLAN-OFFICE-26`) in 15, 16 and 17; (b) a note that the new office belongs to the parks renewal programme.
- Needs decision: no
- From: broad, money, context (all three: yes)

### furniture/15#F5 · Low · The department's own exemption is described as a sale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- Why: `PartyTaxScheme/ExemptionReason` is "The reason for party's exemption from tax, expressed as text", i.e. the party's own status. The text opens with "Sale to a public body", the transaction-level reason (the same words as `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReason` = `Sale to a public body`); the second half states the status correctly. Money also questioned the code: its name "Sale to a public body" describes a sale. The world list's description of PUBLIC is however a buyer status ("A body of the federation, a state or a city buys free of sales tax"), so the code fits both uses, as the contest merges decided. All 55 party-level `ExemptionReasonCode` elements in the examples are `PUBLIC` (merge recount: `grep -rh --include='*.xml' '<cbc:ExemptionReasonCode'`).
- Condition: The party's exemption reason text states the party's status (a public body exempt from the state sales tax) without describing a sale.
- Options: (a, preferred) a text such as "Public body: exempt from the state sales tax"; (b) keep only the code and drop the text; (c) money's option of a separate status code, if the world wants the list to distinguish party and transaction.
- Needs decision: no
- From: money, parties

### furniture/15#F6 · Low · Customs trader number of the department in a domestic order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The department's additional identifier is its customs trader number (`schemeID` `urn:ubl-examples:world:XB:customs-trader`). Office furniture made in Bayvarra is bought, delivered and installed in Bayvarra; no customs procedure is involved, so the identifier is master data the document does nothing with (section 4.8, IND5). It occurs in 55 files (merge recount: `grep -rl --include='*.xml' XB-TR-410548 world/examples`: 36 tender, 16 contest, 3 furniture).
- Condition: The customs trader number is present only in documents with a customs purpose.
- Options: (a, preferred) remove it from this document.
- Needs decision: no
- From: broad, context, parties

### furniture/15#F7 · Low · Brackenmere's registration date is the date shared by 25 companies
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The parties part suspected a placeholder date and refuted it (nothing in the world says the register is closed that day, and no other value depends on it). The merge keeps it as a finding it cannot settle, for alignment with merger A (furniture 01–08) and the merges of every earlier flow: `1996-01-01` is the registration date of 25 companies, 271 times in 181 examples (`grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01' world/examples | wc -l`, `grep -rl` for the files).
- Condition: Brackenmere's registration date is a date from its company history, or the shared date is confirmed as a story fact.
- Options: (a, preferred) an individual date from the company's history; (b) confirm 1996-01-01 as a story event; (c) omit the element where no document uses it.
- Needs decision: yes
- From: parties (under "Considered and refuted"; made a finding by the merge)

## Checked and consistent
- Arithmetic (merge recalculation): 6 × 880 = 5280.00 (`/Order/cac:OrderLine[1]/cac:LineItem/cbc:LineExtensionAmount` = `5280.00`); 14 h × 48 = 672.00 (`/Order/cac:OrderLine[2]/cac:LineItem/cbc:LineExtensionAmount` = `672.00`); sum 5952.00 = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `5952.00` = `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `5952.00`; tax 0.00, exempt PUBLIC, the treatment 17 applies; prices state their base quantity (1 EA, 1 HUR).
- The 6 desks and 14 hours are what `16-WorkReport.xml` reports and `17-Invoice.xml` bills; 14 h is two installers × 7 h, about 2 h 20 min per desk (own estimate 1.5 to 3 h per hardwood desk).
- Item: 1600 × 800 × 740 mm agrees with the description and a standard desk height (720 to 750 mm, own knowledge); HS 940330 and CPC 38122 fit wooden office furniture; GTIN 9523710000029 and the seller's GLN pass their check digits.
- Dates: the order (2026-04-01) precedes the work (2026-04-08) by a week.
- Buyer contact (Procurement office, Procurement officer, Procurement) fits the buying role; the department is described identically in 15, 16 and 17.

## Considered and refuted
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`: the maker's brand on the desks — refuted because, unlike the garden sets, these are the maker's own products (from context).
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `940330`: HS code in a domestic order — refuted because it belongs to the item's description and serves statistics as well as customs (from context).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode`: a city department registered at state level — refuted because the level is that of the tax (the state sales tax of Coastal State) (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention`: head of procurement in the address and a procurement officer as contact — refuted because they are two functions of the same office (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: placeholder date — refuted by parties; made F7 by the merge.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because it fits the seller and name, title and department agree (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).

## Changed in the merge
- parties' refuted candidate (RegistrationDate 1996-01-01) → F7: made a Low finding with "Needs decision: yes", the parties' refutation carried as counter-argument, for alignment with merger A (01–08) and every earlier flow's merge.
- broad/F1, parties/F1 → F1: "Needs decision" set to no (parties: yes), as in all earlier flows for public bodies and customs authorities described as companies: the preferred option only removes values; the City of Lumeport as legal entity kept as option (b), which would be a story change.
- broad/F2, parties/F2, context/F1 → F2: removal preferred, as in earlier flows.
- logistics/F1, parties/F3 → F3: combined (place and date).
- broad/F3, money/F1, context/F2 → F4: "Needs decision" set to no (all three: yes), as the earlier flows' cost-centre findings: a buyer's cost centre is internal accounting, and neither option changes what happens in the story; tender reference added.
- money/F2, parties/F4 → F5: combined; the code kept as fitting (contest merges' decision), money's argument stated and its option kept as (c).
- broad/F4, context/F3, parties/F5 → F6: combined; count recounted.

## Outside this review
- `17-Invoice.xml` and `16-WorkReport.xml` add a packaging-disposal charge of 24.00 that this order does not contain; recorded in their reviews (from money).
