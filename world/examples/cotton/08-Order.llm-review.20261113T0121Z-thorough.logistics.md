# LLM review: 08-Order.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/08-Order.xml`, Git blob `71ce9b04ed217222f38cfab91ff0f8de0f9cd595` (committed)
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

### cotton/08#F1 · Medium · PackSizeNumeric holds the bale weight in kilograms
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:PackSizeNumeric` = `227`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `6129`
- Why: `PackSizeNumeric` is "the number of items in a pack of this item", a count; here it carries the nominal bale weight in kilograms ("compressed bales of about 227 kg"). The order is in kilograms, and the number of bales (6129 / 227 = 27) is nowhere stated as a count. Same as in 02, 07, 10, 11, 15 and 16.
- Condition: `PackSizeNumeric`, where present, is a count of items in a pack; the nominal bale weight is stated where a weight belongs.
- Options: (preferred) drop `PackQuantity`/`PackSizeNumeric` and state the nominal bale weight as an `AdditionalItemProperty` with `ValueQuantity` in KGM (and, if wanted, the 27 bales in the description).
- Needs decision: no

### cotton/08#F2 · Low · Order gives no delivery date or period
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/Order/cac:DeliveryTerms/cbc:ID` = `FOB`
- Why: The order's `Delivery` names only the party that receives the goods; there is no requested delivery date or period, neither in the header nor in the line. Under FOB the seller must deliver on board at the port of shipment on the date or within the period agreed (Incoterms 2020, own knowledge), and the buyer has to name the vessel; neither date nor vessel is given, so the gin cannot tell from the order when to have the bales at the port. The flow shows the shipment leaving on 2026-03-02 (13), but the order does not ask for it.
- Condition: the order states when the goods are to be delivered on board (a requested date or period), or the document makes clear that the date follows from another agreement.
- Options: (preferred) add a `RequestedDeliveryPeriod` (header `Delivery` or line delivery) matching the sailing used in 13; or refer to the call-off rules of the season agreement.
- Needs decision: no

### cotton/08#F3 · Low · FOB place given only as text, and FOB for a container
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Port of Selanu`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PhysicalLocation/cbc:ID` = `XLSEL`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- Why: The named place of the FOB term is only a description; the same port is identified elsewhere in the flow by its location code `XLSEL` (12). The goods travel in a 40-foot container (12, 17); for containerised goods, which are handed over at the terminal before loading, Incoterms 2020 advises FCA rather than FOB (own knowledge). This is practice, not a UBL rule, so it is a plausibility remark only.
- Condition: the delivery location of the terms is identified as the same port is elsewhere in the flow; the Incoterms rule fits the way the goods are handed over, or the choice of FOB is deliberate.
- Options: (preferred) add `ID` `XLSEL` (UN/LOCODE) to the delivery location; optionally consider FCA at the container terminal of Selanu.
- Needs decision: yes (the choice of Incoterms rule is part of the sale)

## Checked and consistent
- 6129 KGM = 27 bales × 227 kg exactly; 6129 × 0.988 = 6055.452 XLC.
- The quantity 6129 KGM is the same in 10, 11, 15 and 16; the order ID `LTM-PO-26-0198` is referenced by 09, 10, 11 and 16 (as order reference in 16).
- Classing certificate in the item (signature 2026-02-20) predates the order (2026-02-24).
- Destination country XB agrees with the consignee's country and with the import declaration 15.
- FOB with the buyer arranging main carriage agrees with the flow: the mill issues the forwarding instructions (09) and pays the forwarder's freight invoice (17).
