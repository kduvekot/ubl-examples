# LLM review: 02-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/02-Invoice.xml`, Git blob `24cc8e618ee2697a2fbe496ce115022415fe249c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/02#F1 · Low · The export invoice says nothing about the delivery it bills
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Export outside Bayvarra`
- XPath: `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521`
- Why: The invoice bills 480 kg of film as a zero-rated export, i.e. it states that the goods left Bayvarra, but it carries no `Delivery` (no actual delivery date, no delivery location, no carrier) and no reference to a despatch, transport or export document (`DespatchDocumentReference`, `AdditionalDocumentReference`). The order (`01-Order.xml`) gives FCA at the seller's dispatch with Trasvia Haulage as carrier but no date, so nowhere in the flow is it recorded when the goods were handed to the carrier, which is both the delivery under FCA and the event the export treatment rests on. Completeness remark; nothing contradicts.
- Condition: the invoice states when (and where) the goods were delivered, e.g. an actual delivery date at the FCA place, or refers to a document that records it.
- Options: (a, preferred) add `cac:Delivery` with `cbc:ActualDeliveryDate` and the FCA place, since that is the delivery being billed; (b) add a document reference to the export or transport document, if the story gives one; (c) leave it if the world treats the order reference as enough, and record that.
- Needs decision: no

### packaging/02#F2 · Low · The customer's logistics service provider plays no part in this invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: `ServiceProviderParty` is "A party providing a service to this party". Castrano Logistics (warehousing and despatch for Valdara) has nothing to do with this invoice, under which goods were collected by Trasvia Haulage at the seller's premises (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`). Master data copied into a document that does not use it; the same block (`VI-SP-2026-01`) occurs in 75 examples (`grep -rl --include='*.xml' 'VI-SP-2026-01'`).
- Condition: the invoice carries the service provider only if it has a role in what is billed.
- Options: (a, preferred) drop it here; (b) give it a role in the delivery (see the order's review).
- Needs decision: no

### packaging/02#F3 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772040000103`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `/Invoice/cac:OrderReference/cbc:ID` = `VI-PO-26-0521` resolves to `01-Order.xml` (an order, buyer Valdara Industries, seller Rivermouth Packaging, as here); the invoice (2026-05-02) is issued after the order (2026-04-27).
- Quantity and item against the order: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `480` kg equals `01-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `480`; seller's item ID, item number, HS and CPC codes, thickness 23 µm and description are the same. 480 kg / 16 kg = 30 whole rolls (physics as in the order's review: a 16 kg roll of 23 µm PE at 920 kg/m³ and 0.5 m width is about 1 510 m).
- `check_ids.py`: the account `XB96BLUM38020504712805` and the RF reference `RF29RPINV260522` pass.

## Considered and refuted
- `/Invoice/cac:InvoiceLine/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`: checked against the export from Bayvarra — consistent, the film is made by Rivermouth Packaging in Lumeport.
