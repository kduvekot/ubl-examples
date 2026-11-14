# LLM review: 25-Catalogue.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/25-Catalogue.xml`, Git blob `2053b3b6f8e10aa06896f01ab77d01b5ac7d4848` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/25#F1 · Medium · The sales territory of the contract prices is Urvania, while their tax category is export from Urvania and the buyer is in Bayvarra
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `EXP`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTerritoryAddress/cac:Country/cbc:IdentificationCode` = `XU`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- Why: `ApplicableTerritoryAddress` is "the applicable sales territory" of the item-location-quantity, i.e. where the price, lead time and tax category of that block apply. The catalogue is the price list of the framework contract with a Bayvarran authority (`/Catalogue/cac:ReferencedContract/cbc:ID` = `PWD-2026-PARKS`), the goods are delivered to Lumeport and the installation is done in Lumeport's parks. The tax categories of the same blocks say so themselves: "Export of goods outside Urvania" (category G) and "Service to a business established outside Urvania" (category O) can only apply to sales outside Urvania. A sale in the territory Urvania would be a domestic sale under Urvanian VAT. Rated Medium rather than High because the country may have been meant as the country whose tax the category belongs to, which is not what the element means.
- Condition: the territory of each item-location-quantity is the territory in which that price and tax category apply (for this catalogue, Bayvarra), or no territory is stated.
- Options: (a, preferred) set the territory to XB; (b) remove the territory, since the catalogue has a single receiver and contract.
- Needs decision: no

### tender/25#F2 · Low · The "contract prices" are in ferra, the contract was tendered and awarded in lume, and the catalogue gives no rate
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `1800`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceTypeCode` = `CON`
- Why: CON is "the price agreed in a contract, such as a framework contract". The prices agreed in this contract are those of the awarded tender, which is entirely in lume (`15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:LineExtensionAmount` = `119760.00` for 240 benches, i.e. 499 XBL; 4320.00 for 240 installations, i.e. 18 XBL), as are the award and the contract (24-TenderContract.xml, 124080.00 XBL). The catalogue states them as 49900 and 1800 XUF. They agree with the lume prices only at 100 ferra to the lume, a rate that the catalogue does not mention and that the later documents take from a forward contract of the buyer (`26-Order.xml:/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`). As it stands the catalogue re-denominates the contract price: if the rate moves, a release priced from this catalogue no longer costs what the tender offered. Whether the framework's price currency is the lume (as tendered) or the ferra (as the catalogue and the `PricingCurrencyCode` of 26–28, 32 and 35 say) is a decision about the story.
- Condition: the currency of the catalogue's contract prices is the currency in which the contract fixes its prices; if the documents after the award use another currency, the contract (or the catalogue) states the fixed rate that ties it to the awarded amounts.
- Options: (a, preferred) state the contract prices in XBL (499 and 18), as tendered, and let the invoice convert for payment; (b) keep XUF and add to the contract and the catalogue that prices are fixed in ferra at 100 ferra to the lume for the life of the framework.
- Needs decision: yes

### tender/25#F3 · Low · The contract price is valid unchanged outside and throughout the contract period although the contract revises prices each January
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:StartDate` = `2026-03-21`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:Price/cac:ValidityPeriod/cbc:EndDate` = `2028-03-20`
- Why: the price's `ValidityPeriod` is "a period during which this price is valid". The contract it belongs to runs from 23 March 2026 for 24 months (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:Contract/cac:ValidityPeriod/cbc:StartDate` = `2026-03-23`), so the contract price is valid two days before the contract exists and stops two days before it ends (22 March 2028). The contract also provides a price revision (`24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cbc:PriceRevisionFormulaDescription` = `Steel index each January.`), so a price cannot be promised unchanged across January 2027 and January 2028.
- Condition: the validity of a contract price lies within the contract's period and does not extend beyond the next date on which the contract revises prices (or the catalogue says the price is subject to that revision).
- Options: (a, preferred) valid from 2026-03-23 to 2026-12-31, the first revision date; (b) keep the whole contract period (2026-03-23 to 2028-03-22) and add a note that the January revision replaces the price by a new catalogue.
- Needs decision: no

### tender/25#F4 · Low · The price applies from one bench; the awarded tender sets a minimum order of 20 in steps of 4
- XPath: `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cbc:MinimumQuantity` = `1`
- Why: `MinimumQuantity` is "the minimum quantity that can be ordered to qualify for a specific price". The tender that became the contract offers the bench on pallets of 4 with `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:MinimumOrderQuantity` = `20` and `15-Tender.xml:/Tender/cac:TenderedProject/cac:TenderLine[1]/cbc:OrderQuantityIncrementNumeric` = `4`. The contract price of 49900 ferra was offered on those terms; the catalogue grants it from a single bench. The seller may of course accept less than it tendered, so this is not rated as a contradiction, but the two documents state different conditions for the same price.
- Condition: the quantity from which the contract price applies is the same in the catalogue and in the tender it implements, or the catalogue's wider terms are a stated concession.
- Options: (a, preferred) `MinimumQuantity` 20 on line 1 (and the pallet increment, if the catalogue line carries order quantities); (b) lower the tender's minimum order quantity.
- Needs decision: no

### tender/25#F5 · Low · The installation is exempted as a "service to a business", for a customer that is a public body
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:ID` = `O`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReasonCode` = `SVCABROAD`
- XPath: `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:TaxExemptionReason[2]` = `Service to a business established outside Urvania`
- Why: the reason code is defined in the world's list as "Service to a business established outside Urvania … the service is taxed where the customer is established". The only customer of this catalogue is the Lumeport Public Works Department, a public authority (ISIC 8411 in the party data), not a business; and the service is the anchoring of benches in the ground in Lumeport, which is outside Urvanian VAT because of where it is performed, whoever the customer is. Category O ("Services outside scope of tax") fits; the reason given for it does not fit this customer. This rests on my reading of the code's definition; whether Urvanian VAT law treats a foreign public body as a "business" for this rule is a tax judgement.
- Condition: the exemption reason of the installation line is one whose definition covers a public-body customer and a service performed on land outside Urvania.
- Options: (a, preferred) widen the definition of SVCABROAD in the code list to "a customer established outside Urvania" if that is the world's rule; (b) add a reason for work performed on immovable property abroad and use it here and in 32, 33.
- Needs decision: yes

## Checked and consistent
- Prices against the tender: 49900 XUF × 0.01 = 499 XBL = 119760.00 / 240; 1800 XUF × 0.01 = 18 XBL = 4320.00 / 240 (rate 0.01 from 26-Order.xml).
- Tax category of the bench: G ("Free export item, tax not charged"), 0 %, reason EXP of the Urvanian list, scheme VAT: consistent with each other and with the seller being an Urvanian exporter; the same category is used in 26 and 32.
- `BaseQuantity` 1 EA on both prices; price type CON with a price list ID; the catalogue's own validity (2026-03-21 to 2028-03-20) equals the price validity.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount`: the catalogue has no price for the special colour later charged with 200.00 lume (27-OrderChange.xml) — refuted because that charge rests on a separate quotation (VI-QT-26-0071) made after the catalogue.
- `/Catalogue/cac:CatalogueLine[2]/cac:RequiredItemLocationQuantity/cac:ApplicableTaxCategory/cbc:Percent`: a rate of 0 on a category that is outside the scope of the tax — refuted because UBL defines no rule against it and 0 is what is charged.
- `/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cac:PriceList/cbc:ID`: a general price list ID (VI-PL-2026) on a contract price — refuted because a seller may keep contract prices in a list of its own; nothing contradicts it.
