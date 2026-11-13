# LLM review: 08-Order.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/08-Order.xml`, Git blob `4b9ab738473f9a4b2d8102ca056f226654c8875b` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 935fb81 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/08#F1 · High · Emission value is not factor × base
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/08#F2 · Low · Order for promotion stock without a requested delivery date
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- XPath: `/Order/cac:AdditionalDocumentReference/cbc:ID` = `BS-RE-26-0222`
- XPath: `06-RetailEvent.xml:/RetailEvent/cac:Period/cbc:StartDate` = `2026-05-11`
- Why: The order is for the spring promotion (it references the retail event 06, which starts on 2026-05-11, with first shipments available on 2026-04-29), but its Delivery has no RequestedDeliveryPeriod or PromisedDeliveryPeriod. The distributor must infer the date from the catalogue's 3-day lead time and the event; the transport request 11 and despatch 12 then fix a date the order never asked for.
- Condition: the order states when the goods are wanted (a requested delivery date or period), consistent with the promotion start and the catalogue's delivery period (from 2026-04-27).
- Options: (a, preferred) Delivery/RequestedDeliveryPeriod ending well before 2026-05-11, e.g. 2026-04-29 to 2026-05-04; (b) leave it out and say in a note that delivery follows the event's first shipment date.
- Needs decision: no

### retail/08#F3 · Low · Delivery-terms location given as text only, although the place has a GLN
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`
- XPath: `/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: For DDP the named place is where the seller's obligations end. It is the same goods-in as the delivery location two elements above, which has GLN `9522610900019`, but here it is only a free-text description naming the company. A Location's name/description should be the place; where the place is identified elsewhere, the identifier belongs here too.
- Condition: the DDP named place identifies the same goods-in as the delivery location (by its GLN, or by a description that names the store, not only the company).
- Options: (a, preferred) DeliveryTerms/DeliveryLocation/ID `9522610900019`; (b) drop the delivery terms' location if the delivery location is meant.
- Needs decision: no

## Checked and consistent
- Quantity 24 EA is six pallets of four (02's orderable unit), within the catalogue's 4–192 band and a multiple of the increment 4; CatalogueLineReference `1` is the bench line of 02.
- Price 520 XBL per EA equals 02's trade price; 24 × 520 = 12480.00 = LineExtensionAmount.
- The order (2026-04-24 08:15) follows the inventory report 07 (stock 3, below the minimum of 6) and the retail event 06, and lies within the catalogue's validity; ValidityPeriod ends 2026-04-26, the day on which the status request 09 asks about the order.
- GLN `9522610900019` of the delivery location passes the GS1 check digit (check_ids.py), demonstration prefix 952.
- DeliveryTerms `DDP` (Incoterms) agrees with the catalogue's "Delivered duty paid to the store".
- Buyer-proposed substitute: the same item `LD-10442` in another extension (`GRN`), quantity 24 like the line.
