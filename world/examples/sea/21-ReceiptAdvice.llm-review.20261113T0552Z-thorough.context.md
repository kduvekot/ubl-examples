# LLM review: 21-ReceiptAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/21-ReceiptAdvice.xml`, Git blob `11d4ca627fbbda4c36b71ae5b97e59794bcbb9ae` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/21#F1 · Low · The warehouse asks the seller for a credit it is not owed
- XPath: `/ReceiptAdvice/cbc:RejectActionCode` = `CREDIT`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectActionCode` = `CREDIT`
- Why: `RejectActionCode` is "A code signifying the action that the delivery party wishes the despatch party to take as the result of a rejection". The delivery party is Nalevi Warehousing, which stores the goods for the buyer; the buyer is Velumi Trading. A credit for the cracked side frame can only go to the buyer, and in the flow it is the buyer's own claim that leads to it: the credit note names Velumi's claim as originator (`26-CreditNote.xml:/CreditNote/cac:OriginatorDocumentReference/cbc:ID` = `VT-CLAIM-26-0019`). The warehouse, which has no purchase relation with Lumeway, wishing a credit reads as if it were the buyer.
- Condition: The action the warehouse asks for is one the warehouse can want from the despatch party (e.g. replacement delivery, or none), or the advice states that it acts on the buyer's instruction.
- Options: (a) preferred: leave the commercial remedy to the buyer's claim and let the warehouse ask for a replacement or no action; (b) keep CREDIT and make clear (e.g. in a note) that the warehouse relays Velumi's request.
- Needs decision: no

### sea/21#F2 · Low · The rejected side frame is not identified, although every frame was despatched with a serial number
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectReason` = `One box crushed at the port; the frame inside is cracked.`
- Why: The despatch advice gives each of the twelve side frames as an item instance with its own serial number (`20-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01230` to `VI-SF-01241`). The receipt advice rejects one of them as cracked but does not say which; the seller, who must credit it and may claim against the carrier or the port, cannot tell which instance it is. The receipt line's item has room for that (`ItemInstance`).
- Condition: The rejected unit is identified by the identifier it was despatched with.
- Options: (a) preferred: add the rejected frame's item instance (serial ID) to the receipt line; (b) state its serial number in the reject reason.
- Needs decision: no

### sea/21#F3 · Low · Sales and product-passport data copied into the receipt advice
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- Why: A receipt advice reports what was received and in what condition. The warehouse repeats the bench's whole catalogue description: the seller's search keywords, warranty, the seller's sales conditions, the load test method, emissions and circularity profile. The warehouse issues and the seller receives none of this as information about the receipt; it is master data copied into a document that does not use it. The second receipt line does without it.
- Condition: The receipt lines identify the items received (identifiers, name) and carry no catalogue or sales data.
- Options: (a) preferred: reduce the bench's item to its identifiers and name.
- Needs decision: no

### sea/21#F4 · Low · Document status "no status" says nothing
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Receipt Advice with respect to its original state"; "No status on document" conveys what absence conveys (rule: no fillers, nothing implied by absence). The value occurs 26 times as `DocumentStatusCode` in the examples (counted with `grep -rh --include='*.xml' -o 'DocumentStatusCode">NoStatus<'` over `world/examples`).
- Condition: `DocumentStatusCode` is present only where the status is worth stating.
- Options: (a) preferred: remove it; (b) keep it by a recorded project decision.
- Needs decision: yes

## Checked and consistent
- References: order `VT-PO-26-0127`, despatch advice `LD-DA-26-0145` (header and both lines, with the matching line IDs 1 and 2) and bill of lading `TOL-BL-26-0139` exist.
- Quantities: 96 benches received as despatched; side frames 11 received + 1 rejected = 12 despatched. The header's partial acceptance, damage reason and credit request agree with line 2.
- Dates: received 2026-05-21, after the discharge (2026-05-18) and the import declaration (2026-05-19); issued the same day at 17:22.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:QuantityDiscrepancyCode`: a quantity discrepancy code suspected redundant or wrong when 11 + 1 = 12 — refuted because the discrepancy is between the quantity despatched and the quantity accepted, and "damaged" is its type.
- `/ReceiptAdvice/cbc:ReceiptAdviceTypeCode`: "Actual" suspected to need a passed inspection — refuted because the code's meaning covers an arrival that has passed goods inspection and is accepted "or not", which fits a partial rejection.
