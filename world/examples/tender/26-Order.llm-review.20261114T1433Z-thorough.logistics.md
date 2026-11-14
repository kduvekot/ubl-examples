# LLM review: 26-Order.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/26-Order.xml`, Git blob `6251abb7d11ec4be2651a2e8b809979afc7557fa` (committed)
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

### tender/26#F1 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement" and ValueBaseMeasure "the base quantity to which the value factor applies". 0.82 × 1 EA = 0.82, not 96 kg CO2e; 96 / 0.82 = 117.07, a base the document does not state. Same values as in `25-Catalogue.xml` and, with this item, in 39 examples across flows (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base quantity = value, with the base in the unit the factor refers to; or factor and base are absent.
- Options: (a) preferred: the base the factor refers to (e.g. 117 KWH if the factor is per kWh); (b) drop factor and base.
- Needs decision: no

### tender/26#F2 · High · Pricing currency is ferra, the price is in lume
- XPath: `/Order/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `499`
- Why: PricingCurrencyCode is "a code signifying the currency used for all prices in the Order". The only price of the order is 499 with currencyID XBL; the catalogue price it comes from is in ferra (`25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`, XUF). Either the code or the price's currency is wrong. (Amounts are the money lens's subject; noted here as a code that contradicts the element it governs. The same header codes are in 27 and 28, which carry no prices.)
- Condition: Every `cbc:PriceAmount` is in the pricing currency.
- Options: (a) preferred: price 49900 XUF with the pricing exchange rate converting to the line amount in XBL; (b) pricing currency XBL and no pricing exchange rate.
- Needs decision: no

### tender/26#F3 · Medium · The seller's order number in the buyer's order, before the seller has seen it
- XPath: `/Order/cbc:SalesOrderID` = `VI-SO-26-0058`
- Why: "An identifier for the Order, assigned by the seller." The order is the buyer's first message of this transaction (23 March 14:40); Valdara answers only on 25 March (`28-OrderResponse.xml`), and that response, where the seller's number would belong, does not carry it. No other example mentions the number (grep for `>VI-SO-26-0058<` over `world/examples/**/*.xml`: this example only). The buyer cannot know a number the seller assigns on receipt.
- Condition: The seller's order number appears first in a document of the seller (the order response) and in the buyer's order only if a seller's document issued earlier gave it.
- Options: (a) preferred: remove it here and carry it in `28-OrderResponse.xml` (`cbc:SalesOrderID`) and the later documents; (b) explain it by an earlier quotation or reservation of the seller.
- Needs decision: no

### tender/26#F4 · Medium · The framework release number is carried as a delivery-access release ID
- XPath: `/Order/cac:Delivery/cbc:ReleaseID` = `1`
- Why: In Delivery, ReleaseID is "an identifier used for approval of access to delivery locations (e.g., port terminals)". The value 1 is evidently the number of this release under the framework (the contract speaks of "releases", this is the first order), not an access approval for the public works depot.
- Condition: `cac:Delivery/cbc:ReleaseID` holds an identifier the carrier needs to be admitted at the delivery location, or is absent; the release number, if wanted, is carried where an order sequence belongs.
- Options: (a) preferred: remove it and say "Release 1" in a `cbc:Note`; (b) replace it by a real gate or slot reference of the depot.
- Needs decision: no

### tender/26#F5 · Medium · The order does not say when the benches are to be delivered
- XPath: `/Order/cac:Delivery`
- Why: An order is the buyer's request for goods; this one states what (40 benches), the price, the terms (DAP) and the place, but no requested delivery date or period (`cac:Delivery` holds only the release ID and the delivery party; there is no `RequestedDeliveryPeriod` or `LatestDeliveryDate`, and none on the line). The procedure asked for a first delivery on `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate` = `2026-04-02`, the tender offers 7 days of lead time and the catalogue 5; the penalty clause (0.5 % per day late) needs a due date to count from. The response (28) names no date either, so no document of the release fixes one before the despatch advice.
- Condition: The order states the requested delivery date or period for the release.
- Options: (a) preferred: `cac:Delivery/cac:RequestedDeliveryPeriod` ending 2026-04-02; (b) a promised period in the order response.
- Needs decision: no

### tender/26#F6 · Low · The contract is cited twice, once as an unexplained "originator document"
- XPath: `/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Order/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: OriginatorDocumentReference is "a reference to an originator document associated with this document"; it has only an ID, identical to the contract's (and to the procurement file's). The reader cannot tell which document of an originator is meant; the contract is already cited in `cac:Contract`. The buyer is itself the originator of the procurement.
- Condition: The originator reference names a document other than the contract and says what it is, or is absent.
- Options: remove it (preferred); or cite the internal requisition of the parks section with a DocumentType.
- Needs decision: no

### tender/26#F7 · Low · The programme has another code than in the procurement documents
- XPath: `/Order/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- Why: The same programme, "Parks renewal programme 2026", is coded `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in the notices, the call for tenders and the contract (01, 02, 03, 24), and `PWD-PARKS-26` in 26, 29, 32 and 33; the budget line of the call for tenders is BL-PARKS-26 / account 4.2.110. The one string is used here both as the buyer's accounting code and as a project identifier.
- Condition: One identifier per thing: the programme has the same code in all documents, and the accounting code is the buyer's cost account (or the same code, deliberately).
- Options: (a) preferred: use PARKS-26 for the project reference and the budget account (4.2.110) as accounting cost code; (b) use PWD-PARKS-26 in the procurement documents too.
- Needs decision: no

### tender/26#F8 · Low · Forward exchange contract dated before the procedure began
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- Why: The forward purchase of ferra that fixes the pricing rate was concluded on 2 January, ten days before the prior information notice (12 January) and more than two months before the award (9 March) made it known that the supplier would be Urvanian. The tenders and the contract are in lume, so before the award nobody knew ferra would be needed.
- Condition: The date of the exchange contract is one on which the party that concluded it could know of the ferra exposure, or the document explains the earlier hedge.
- Options: (a) a contract dated after the award (9 March) or the contract (19 March); (b) describe it as a general yearly hedge of the party; no preference without knowing whose contract it is.
- Needs decision: yes

## Checked and consistent
- `check_ids.py`: no failures.
- The order is issued on 23 March 14:40, the first day of the contract (`PWD-2026-PARKS`, from 2026-03-23), after the catalogue it cites (`VI-CAT-26-0211`, 21 March); the catalogue reference is in the element meant for it.
- Quantity 40 EA respects the tendered ordering terms: minimum 20, maximum 96, steps of 4 (ten pallets of 4).
- 40 × 499.00 = 19960.00; line, taxable and payable amounts agree. Exchange rates 0.01 and 100 are reciprocal.
- `cbc:LineCountNumeric` 1 = one order line. OrderTypeCode 220 is "Order" in UNCL 1001.
- Item data (identifiers, colour GRY, dimensions, classification, references VI-DS-B180, VI-LCA-2025, VI-RM-B180) are those of catalogue line 1.
- DAP with delivery location "Public works depot, Lumeport" fits the later documents: Valdara exports (30), the department imports (31).

## Considered and refuted
- `/Order/cac:OrderLine`: no line for the installation although lot 2 was awarded and the average release (20680.00) includes it — refuted for this lens: the order may cover the supply only; whether the installation of this release is ordered elsewhere is a story question (see "Outside this review").
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`: a description instead of a structured address — refuted: the delivery party's address is given, and the named place for DAP may be text.
- `/Order/cac:Contract/cbc:ID`: equal to the procurement file number — refuted: consistent with the award documents.

## Outside this review
- No document of the flow orders or invoices the installation of the 40 benches (lot 2).
