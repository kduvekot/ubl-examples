# LLM review: 01-RequestForQuotation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/01-RequestForQuotation.xml`, Git blob `25a98f65310576bccebca7415f6252636f7b9a02` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### furniture/01#F1 · Low · Destination country for customs purposes in a domestic request
- XPath: `/RequestForQuotation/cac:DestinationCountry/cbc:IdentificationCode` = `XB`
- Why: UBL defines `DestinationCountry` in a Request for Quotation as "The country of destination of potential orders (for customs purposes)". The buyer (Lumeport, Coastal State, XB), the seller (Marrowdale, Upland State, XB), the item's origin (`/RequestForQuotation/cac:RequestForQuotationLine/cac:LineItem/cac:Item/cac:OriginCountry/cbc:IdentificationCode` = `XB`) and the delivery place are all in Bayvarra. The goods cross no customs border, so there are no customs purposes for the element to serve (IND5: no value without a business reason).
- Condition: `DestinationCountry` is absent, or the request describes a cross-border supply in which customs applies.
- Options: (preferred) remove `DestinationCountry`, since the delivery location already says where the goods go; or, if the store wants to rule out an imported supply, say that in a note instead.
- Needs decision: no

### furniture/01#F2 · Low · DAP delivery terms without their named place
- XPath: `/RequestForQuotation/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019`
- Why: An Incoterms rule is only complete with its named place ("DAP <named place of destination>"). UBL gives `DeliveryTerms` its own `DeliveryLocation` ("The location for the contracted delivery"), and the orders of this flow use it (`08-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Brightmarket Stores, goods-in, Lumeport`). Here the terms carry only the rule; the place is in the separate `Delivery` aggregate, so a quotation based on the request must infer that the two belong together.
- Condition: the DAP terms name their place, either in `DeliveryTerms/DeliveryLocation` or by an unambiguous link to the goods-in GLN.
- Options: (preferred) add `DeliveryTerms/DeliveryLocation` with the goods-in GLN `9522610900019`, which also matches the delivery location of `retail/08-Order.xml`; or keep the `Delivery` aggregate as the only place and accept the implied link.
- Needs decision: no

### furniture/01#F3 · Low · The catalogue reference cannot be identified as a catalogue
- XPath: `/RequestForQuotation/cac:CatalogueDocumentReference/cbc:ID` = `BM-RANGE-26`
- Why: UBL: "The Catalogue on which this Request for Quotation is based". The ID has the buyer's prefix `BM`, no example of any flow has it as its document ID, and the only other example that carries it uses it as a plain document reference in a catalogue request to another seller (`retail/01-CatalogueRequest.xml:/CatalogueRequest/cac:DocumentReference/cbc:ID` = `BM-RANGE-26`), which reads like the store's own range plan rather than a catalogue of items for sale. The requested item is the maker's own model with the maker's item number and GTIN, so a catalogue of the store would not be the basis of the request. With only an ID, the reader cannot tell what the document is.
- Condition: the referenced document is a catalogue in UBL's sense, or it is referenced through an element that fits what it is, with a `DocumentTypeCode` or `DocumentDescription` that says so.
- Options: (preferred) move the reference to an `AdditionalDocumentReference` with a description such as "Garden range plan 2026", matching how `retail/01-CatalogueRequest.xml` uses it; or keep `CatalogueDocumentReference` if the story makes BM-RANGE-26 the store's own catalogue of the line, and describe it.
- Needs decision: yes

## Checked and consistent
- GS1 check digits: GLNs 9523710900008, 9522610900002, 9522610900019 and GTIN 9523710000012 pass (`check_ids.py`). The prefix 952 is the GS1 range for demonstrations and examples, so the keys cannot be mistaken for real ones.
- The goods-in GLN 9522610900019 is the store's goods-in location in `retail/08-Order.xml` too, with the same meaning.
- Dates: the submission due date 2026-03-07 lies after the issue date 2026-03-02; the quotation (`02-Quotation.xml`) was issued on 2026-03-06, before that due date. The requested validity of 60 days matches the quotation's validity end 2026-05-05 (2026-03-06 + 60 days).
- Item: quantity 20 sets; bench length 1400 mm fits a three-seat garden bench (about 1.2 to 1.6 m, own knowledge). HS 940169 and CPC 38112 fit wooden-framed seats.

## Considered and refuted
- `/RequestForQuotation/cac:Delivery/cac:DeliveryLocation/cbc:Name`: suspected a company name instead of a place — refuted because the name designates the store's goods-in, i.e. the place, and `retail/08-Order.xml` names the same GLN in the same way.
- `/RequestForQuotation/cac:Contract/cbc:ID`: suspected an unresolvable reference — refuted because a framework contract is not a UBL document of the world and need not exist as an example; the contradiction with the contract IDs used later in the flow is a finding of `11-OrderCancellation.xml` and `14-DebitNote.xml`.
