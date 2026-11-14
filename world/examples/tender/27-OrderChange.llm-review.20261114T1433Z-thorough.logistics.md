# LLM review: 27-OrderChange.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/27-OrderChange.xml`, Git blob `e43fb0041dc6f797ab80a2e9f8efb406a7c4464c` (committed)
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

### tender/27#F1 · Medium · The new colour is only in free text; the item's variant is not identified
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Park bench Serra 180, frame in moss green RAL 6005`
- XPath: `/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`
- Why: The purpose of this order change is to replace the ordered variant. The order identifies the variant in structured form (`26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`, with the physical attribute COLOUR / FRM / colour code GRY), and the world's ColourCode list has a code for the new colour (GRN, "Green, such as moss green (RAL 6005)"). The changed line carries no item identification at all, so nothing structured tells the seller's system that VI-B180 is now wanted in another variant. The consequence is visible downstream: the despatch advice, both customs declarations, the invoice and the credit note still identify the goods as variant GRY, "Frame in Ferro grey" (see their reviews).
- Condition: The revised line identifies the item (VI-B180 / 771020000027) and its new variant in the same structured way the order identified the old one.
- Options: (a) preferred: SellersItemIdentification with the new extended ID and a PhysicalAttribute with DescriptionCode GRN, "Frame in moss green (RAL 6005)"; (b) at least the item identifiers, with the colour in the description.
- Needs decision: no

### tender/27#F2 · Low · A freight forwarder is named who plays no part in the transport
- XPath: `/OrderChange/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: "A freight forwarder or carrier." The order (26) names none and the note of the change speaks only of the colour, so the change silently adds a forwarder. Delivery is DAP (the seller arranges the carriage), and in the documents of the movement Bayforth does not occur: the despatch advice (29) is issued by Castrano Logistics, and neither customs declaration (30, 31) names Bayforth (grep for `>Bayforth Forwarding<` over `world/examples/tender/*.xml`: 27, and 32–35 where it is the tax representative). A forwarder in Lumeport chosen by the buyer does not fit DAP either.
- Condition: The forwarder named in the order documents is the one that takes part in the transport or customs handling shown in the flow, and its addition is a stated change; otherwise the party is absent.
- Options: (a) preferred: remove it from the order change; (b) give Bayforth a visible role (e.g. the declarant of the import declaration) and say so in the note.
- Needs decision: no

### tender/27#F3 · Low · Additional document reference with only an ID
- XPath: `/OrderChange/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COLOUR-RAL6005`
- Why: "A reference to an additional document associated with this document", without type or description; not in the flow (grep over `world/examples/**/*.xml`: this example only). The identifier suggests a colour specification or decision of the department, but the reader has to guess.
- Condition: The reference states what the document is.
- Options: add `cbc:DocumentType` (e.g. "Colour specification") (preferred).
- Needs decision: no

### tender/27#F4 · Low · The contract is cited twice, once as an unexplained "originator document"
- XPath: `/OrderChange/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/OrderChange/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: As in `26-Order.xml`: "a reference to an originator document associated with this document" with only an ID equal to the contract number says nothing the `cac:Contract` next to it does not say, and not which originator's document is meant.
- Condition: The originator reference names a document other than the contract and says what it is, or is absent.
- Options: remove it (preferred).
- Needs decision: no

## Checked and consistent
- `check_ids.py`: the account number XU790351041600000000209458 passes the IBAN-style check; no failures.
- `cac:OrderReference/cbc:ID` LPWD-PO-26-0212 is the order of 23 March 14:40; the change is issued the next morning (24 March 08:06), sequence number 1, the only change of the flow.
- Validity until 2026-03-27: the response `28-OrderResponse.xml` (25 March 16:15) falls within it.
- Quantity 40 EA and line amount 19960.00 are unchanged from the order; 19960.00 + 200.00 = 20160.00.
- LineStatusCode Revised (UBL list), AllowanceChargeReasonCode CAT = "Special colour service" (UNCL 7161), PaymentMeansCode 30 = credit transfer: each fits its element and the story.
- Exchange-rate dates: tax and payment rates of the issue date (24 March), pricing rate of the forward contract (2 January), as in the order.

## Considered and refuted
- `/OrderChange/cac:QuotationDocumentReference/cbc:ID`: `VI-QT-26-0071` is not in the flow, and would have to be issued between the order (23 March 14:40) and this change (24 March 08:06) — refuted: a quotation for the colour surcharge given the same afternoon is plausible, the element names the kind of document, and the response confirms "at the quoted charge".
- `/OrderChange/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount`: unchanged although the bench is now a special colour — refuted: the surcharge is a document-level charge of 200.00.
- `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: forward contract of 2 January, before the procedure — the question is raised once, in the review of `26-Order.xml` (F8), where the contract first appears.
