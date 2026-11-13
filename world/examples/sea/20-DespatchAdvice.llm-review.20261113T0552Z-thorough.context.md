# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/20-DespatchAdvice.xml`, Git blob `48649a02a6dba4b51ed92b3c8c00d3a15724cd7a` (committed)
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

### sea/20#F1 · Low · Damage to be reported "on the consignment note" for a sea shipment under a bill of lading
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods travel by sea under the bill of lading `TOL-BL-26-0139` (`14-BillOfLading.xml`) and reach the delivery party, Nalevi Warehousing in Lisavu, by way of the terminal at Selanu. A consignment note is the road or rail transport document (CMR, CIM, own knowledge); no consignment note exists in this flow, and the receipt advice that answers this despatch (`21-ReceiptAdvice.xml`) is where the warehouse in fact reports the damaged side frame. The note asks the receiver to use a document it does not have.
- Condition: The note names the document or channel the receiver actually uses to report damage in this flow (the receipt advice, or a reservation on the delivery receipt / bill of lading), or is absent.
- Options: (a) preferred: ask for damage to be reported in the receipt advice; (b) name the document of the last leg to the warehouse if the story has one (e.g. the haulier's delivery note).
- Needs decision: no

### sea/20#F2 · Low · Sales and product-passport data copied into the despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: A despatch advice tells the delivery party what is coming so it can receive and check it: items, quantities, identifiers, lots, packing. The bench's item here carries the catalogue's search keywords, warranty, the seller's sales conditions, the load test method, emissions, circularity profile and product documentation. The receiving warehouse does nothing with these; they are master data copied from the catalogue (`02-Catalogue.xml`). The second line (side frames) does without them.
- Condition: The despatch lines carry what the delivery party needs to receive and identify the goods (identifiers, description, lots and instances, dimensions where they matter for handling).
- Options: (a) preferred: reduce the bench's item to identification, description, lot and the handling-relevant dimensions; (b) keep a product-passport reference (`ProductDocumentationDocumentReference`) only if the world wants the passport to travel with the goods, and say so.
- Needs decision: no

### sea/20#F3 · Low · Document and line status "no status" say nothing
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Despatch Advice with respect to its original state", and `LineStatusCode` "A code signifying the status of this despatch line with respect to its original state". "No status" conveys exactly what absence conveys, so under the agreed rule (no fillers, nothing implied by absence) the values have no business reason. The document status value is used 26 times as `DocumentStatusCode` in the examples (counted with `grep -rh --include='*.xml' -o 'DocumentStatusCode">NoStatus<'` over `world/examples`).
- Condition: Status codes are present only where the document or line has a status worth stating (revised, cancelled, added …).
- Options: (a) preferred: remove them; (b) keep them only by a recorded project decision that "no status" is a deliberate statement.
- Needs decision: yes

## Checked and consistent
- Quantities 96 benches and 12 side frames agree with the order lines 1 and 2 (`05-Order.xml`), the invoice (`22-Invoice.xml`) and the receipt advice (`21-ReceiptAdvice.xml`, 96 and 11 + 1 rejected); "24 pallets of 4 benches" = 96.
- The order `VT-PO-26-0127` and the packing list `LD-PL-26-0134` exist (`05-Order.xml`, `10-PackingList.xml`); the shipment and consignment IDs are those of the bill of lading.
- The twelve side-frame instances have twelve distinct trace, registration and serial numbers, all from one melt, which fits one casting batch.
- The accounting cost "Stock for municipal projects" (500) is the buyer's, repeated unchanged from the order, and fits the beneficiary Port of Selanu as end customer of Velumi's stock.

## Considered and refuted
- `/DespatchAdvice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name`: the originator and beneficiary (Port of Selanu) in a despatch advice to the warehouse suspected as data the document does nothing with — refuted because they identify for whom the goods are ultimately destined, which the warehouse needs to keep them apart in its stock, and UBL provides both roles in the Despatch Advice.
- `/DespatchAdvice/cbc:IssueDate`: a despatch advice issued on 2026-05-13, before the bill of lading (2026-05-14), suspected as too early — refuted because the advice is sent when the goods leave the seller, which precedes the loading on board.

## Outside this review
- The benches are described as "from the distributor's stock", but their lot was made on 2026-05-10 (`/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-05-10`) in Urvania, three days before the despatch from Lumeway in Bayvarra and after the order of 2026-05-07; whether the goods could be made, moved to Lumeway and packed in that time is a timeline question across flows.
