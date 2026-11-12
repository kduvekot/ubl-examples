# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### air/01#F1 · High · Totals and tax base are those of the whole order, the only line is the 8 added frames
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `51200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `51200.00`
- XPath: `/OrderChange/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `51200.00`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `512.00`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderChange/cbc:LineCountNumeric` = `1`
- Why: The document has one line, 8 × 64 = 512.00, but the monetary total's LineExtensionAmount
  ("the monetary amount of an extended transaction line", i.e. the sum of the line amounts) and the
  tax subtotal's TaxableAmount are 51200.00. That is the original order total
  (`sea/05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`)
  plus the 512.00 of this line, so the totals cover lines that are not in this document. Neither
  reading of AnticipatedMonetaryTotal fits: its definition here is "the amount of change to the
  total cost of the order anticipated by the buyer", which would be 512.00; as a restated total of
  the changed order it would need the unchanged lines in the document as well. The line ID `1` adds
  to the confusion: in the order, line 1 is the bench (96 EA × 520,
  `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cbc:ID` = `1`) and the side frames are
  line 2, so a change to line 1 with 8 side frames reads as replacing the 49920.00 bench line, which
  contradicts both the totals and the note "the rest of the order is unchanged".
- Condition: the sum of the line amounts in the document equals
  AnticipatedMonetaryTotal/LineExtensionAmount and the TaxableAmount, and the line ID of the added
  frames does not coincide with an existing order line that holds a different item.
- Options: (a) preferred: carry the whole changed order (line 1 bench, line 2 sea frames, a new
  line 3 with the 8 frames by air), so 51200.00 is the sum of the lines and the line IDs keep their
  meaning; (b) carry only the added line with a new line ID (e.g. 3) and give the totals and the tax
  base as the change, 512.00.
- Needs decision: no

### air/01#F2 · Low · Document-level delivery terms CPT over totals that include the CIF part of the order
- XPath: `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:SpecialTerms` = `The rest of the order stays CIF by sea.`
- Why: The document-level DeliveryTerms ("a set of delivery terms associated with this document")
  say CPT, while the totals (F1) cover the whole order, whose bench and sea frames remain CIF
  (`sea/05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`), as the special terms state. The
  Incoterm decides who bears freight and insurance, so the document says two things about the cost
  allocation of the same amounts. Resolves together with F1.
- Condition: CPT applies only to the amounts of the air line; either the document covers only that
  line, or CPT is stated at the delivery/line of the air frames and CIF for the rest.
- Options: (a) with F1 option (a): keep CIF at document level and state CPT on the delivery of the
  air line (preferred, matches the special terms); (b) with F1 option (b): keep CPT at document
  level and drop the special terms sentence as the only place the other lines are mentioned.
- Needs decision: no

## Checked and consistent
- Line arithmetic: 8 EA × 64 XBL per 1 EA = 512.00 =
  `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount`. Price 64 equals the sea order's
  frame price (`sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Price/cbc:PriceAmount` = `64`).
- 50688.00 + 512.00 = 51200.00 (the source of the total in F1).
- Tax: category G (free export item) with 0 %, exemption reason EXP "Export outside Bayvarra",
  scheme STT; the seller is in Bayvarra (Upland State), the goods go to Lisavu
  (`/OrderChange/cac:DestinationCountry/cbc:IdentificationCode` = `XL`); same treatment as the order.
  TaxAmount 0.00 in total and subtotal agrees.
- Currency XBL throughout (document currency, all amounts).
- AccountingCostCode `500` / "Stock for municipal projects" is the buyer's code, as in the order.

## Considered and refuted
- `/OrderChange/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount`: price unchanged at 64 although
  the terms change from CIF to CPT by air, so the seller bears air freight that exceeds the value of
  the goods (forwarder bills 554.88, `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `554.88`)
  — refuted because it is a commercial choice the documents state consistently (the seller pays the
  forwarder under CPT; notes say the frames are needed before the ship), not a contradiction.

## Outside this review
- No example invoices the 8 air frames (512.00): the seller's invoice of the order bills only the
  96 benches and 12 sea frames (`sea/22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00`).
  Whether the frames are billed in a document outside the examples is a cross-flow question.
