# LLM review: 08-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/08-Order.xml`, Git blob `4b9ab738473f9a4b2d8102ca056f226654c8875b` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 9cad20e 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/08#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/08#F2 · High · Taxable amount ignores the document-level allowance
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12480.00`
- XPath: `/Order/cac:AllowanceCharge/cbc:Amount` = `624.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `11856.00`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied to calculate the tax amount". The order grants a document-level allowance of 624.00 (5 % of 12480.00), so the net amount of the supply is 12480.00 − 624.00 = 11856.00, which is also the payable amount. The taxable amount is the gross line total. With a rate of 0 % the tax amount is unaffected, but the subtotal does not add up with the totals.
- Condition: the taxable amount equals the sum of line extension amounts minus allowances plus charges in that tax category (11856.00).
- Options: (a, preferred) taxable amount 11856.00, and a tax category on the allowance; (b) move the promotion support to the line, so that the line extension amount carries it.
- Needs decision: no

### retail/08#F3 · Medium · Language codes in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/08#F4 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/08#F5 · Low · Substitute item in a colour the catalogue does not offer
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Park bench Serra 180, moss green`
- XPath: `/Order/cac:OrderLine/cac:BuyerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRN`
- XPath: `02-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the buyer proposes the bench in moss green as a substitute, as the seller's item `LD-10442` with extension `GRN`. The catalogue the order refers to offers the bench only in Ferro grey (`ExtendedID` `GRY`, colour property with the single value Ferro grey); no green variant exists in the flow. A substitute that the seller does not offer cannot be supplied under the referenced catalogue line.
- Condition: a proposed substitute is an item (or variant) the seller offers, or it is absent.
- Options: (a, preferred) add the green variant to the catalogue (another list value of the colour property, with its own GTIN), so the substitution is possible; (b) drop the substitute line item.
- Needs decision: yes

### retail/08#F6 · Low · No requested delivery date for a promotion order
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: the order is placed for the spring garden promotion starting on 2026-05-11 (referenced retail event), but `Delivery` gives only the location; there is no requested delivery date or period. The catalogue's lead time of 3 days and delivery period from 2026-04-27 leave the date to the seller. The later documents (12 to 17) deliver on 2026-04-30; nothing in the order says that this is what the buyer needs.
- Condition: the order states when delivery is wanted (a requested delivery period), or relies explicitly on the catalogue's lead time.
- Options: (a, preferred) a `RequestedDeliveryPeriod` before the promotion (e.g. ending 2026-05-04); (b) a note referring to the catalogue's lead time.
- Needs decision: no

### retail/08#F7 · Low · Whole item master data copied into the order line
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: the order identifies the item by the buyer's, seller's, manufacturer's and standard IDs and refers to the catalogue line; it then repeats the catalogue's full description: dimensions, load test, emissions, circularity data, Urvania's customs tariff code (not used between two Bayvarran parties) and the distributor's own wording ("from the distributor's stock") in a document written by the buyer. None of it is used by the order.
- Condition: the ordered item carries its identifiers and what the order depends on.
- Options: (a, preferred) name, identifiers, colour variant and the catalogue reference only.
- Needs decision: no

### retail/08#F8 · Low · Brightmarket's party contact: buying office, customer service officer and sales at once
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the party contact's name is the buying office, its job title and department are those of a seller's customer service; the three contradict each other. In this order the buyer's role-specific contacts are given separately (`BuyerContact`, `DeliveryContact`, `AccountingContact`) and fit their roles; only the party contact is wrong. The identical contact is used for Brightmarket in all 19 retail examples that describe it in detail.
- Condition: name, job title and department of the party contact agree with each other.
- Options: (a, preferred) a buyer's job title and purchasing department.
- Needs decision: no

## Checked and consistent
- Arithmetic: 24 × 520.00 = 12480.00 (line and `LineExtensionAmount`); 5 % × 12480.00 = 624.00; 12480.00 − 624.00 = 11856.00 = `PayableAmount`; tax 0.00 at 0 %.
- 24 benches = 6 pallets of four, within the catalogue's minimum 4 and maximum 192 and its increment of 4; 3 in stock (07-InventoryReport) + 24 covers the 24 planned for the promotion (06-RetailEvent) and the minimum of 6.
- Catalogue reference `LD-CAT-26-0218` and catalogue line `1` resolve to the bench line of 02-Catalogue; price 520 per each equals the catalogue's trade price.
- Retail event reference `BS-RE-26-0222` resolves to 06-RetailEvent.
- Payment terms (30 days net) and delivery terms (DDP) agree with the trading terms of 02-Catalogue; tax category `E` with "sale for resale" agrees with the catalogue.
- Role contacts fit their roles: the buyer's buyer, goods-in and accounts payable contacts; the seller's key account manager, dispatch office and accounts receivable.
- GLNs `9522610900002` and `9522610900019` and GTIN `9520610000012` pass the check digit.

## Considered and refuted
- `/Order/cac:ValidityPeriod/cbc:EndDate` = `2026-04-26`: suspected too short — refuted: the order asks for acceptance within two days, and 09-DocumentStatusRequest on 2026-04-26 follows up on it.
- `/Order/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`: suspected incomplete without an account — refuted: in an order the buyer only announces how it will pay; the payee's account follows in the invoice.
