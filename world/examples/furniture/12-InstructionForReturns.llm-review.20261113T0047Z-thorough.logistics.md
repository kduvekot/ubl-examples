# LLM review: 12-InstructionForReturns.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/12-InstructionForReturns.xml`, Git blob `5e0dc8288b904ffb502e97310af81193916c603c` (committed)
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

### furniture/12#F1 · Medium · The return instruction does not say where the goods are to go
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-29`
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-02`
- Why: UBL: an Instruction for Returns is "A document used to initiate a return of goods". The shipment's delivery has a requested period but no `DeliveryLocation`, `DeliveryAddress` or `DeliveryParty`, and the instruction names no despatch (pick-up) place either. The store must know where to bring six sets; the document that initiates the return does not tell it. The place appears only afterwards, in the store's debit note for the transport (`14-DebitNote.xml:/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9523710900015`, "Brackenmere Furniture, Marrowdale"), a GLN that occurs in no other example. Who transports is also left open here (the note "The maker takes back six sets" could mean the maker collects), while `14-DebitNote.xml` says the store's van did.
- Condition: the instruction states the delivery location of the return (Brackenmere, Marrowdale, GLN 9523710900015) and, preferably, who carries the goods.
- Options: (preferred) add `Shipment/Delivery/DeliveryLocation` with GLN 9523710900015 and name "Brackenmere Furniture, Marrowdale", and a note or `Shipment/Delivery/DeliveryParty` that makes clear the store delivers; or, if the maker collects, add the pick-up location (the store's goods-in) and change `14-DebitNote.xml` accordingly.
- Needs decision: no

## Checked and consistent
- Weight (physics, calculated): gross 282 kg for 6 sets = 47 kg per set of one 1400 mm hardwood bench and two chairs in cartons. Own estimates: such a bench about 25 to 30 kg, a hardwood garden chair 8 to 10 kg, cartons about 1 to 2 kg per piece, i.e. 43 to 56 kg per set. The weight fits. The element's definition (goods plus packaging plus transport equipment) fits a shipment in original cartons without further equipment.
- Stock (calculated): 20 delivered − 3 sold to 2026-04-20 (`06-ProductActivity.xml`) = at most 17 on hand; returning 6 leaves at most 11, close to the target inventory of 10 (`04-TradeItemLocationProfile.xml`). The return quantity therefore fits "to free the store's shelf".
- Quantity 6 sets agrees with `13-CreditNote.xml` (6 sets credited) and `14-DebitNote.xml` ("six unsold garden sets"); the actual delivery date there (2026-05-02) lies within the requested period 2026-04-29 to 2026-05-02.
- Reference: `/InstructionForReturns/cac:DocumentReference/cbc:ID` = `BF-DOC-26-0573` resolves to `07-ExceptionNotification.xml`, the exception that led to the return. Issue date 2026-04-27 precedes the requested period.

## Considered and refuted
- `/InstructionForReturns/cac:Shipment/cbc:ID` = `BM-RET-26-0427`: suspected a shipment identifier with the store's prefix in a document issued by the maker — refuted because the store performs the transport (`14-DebitNote.xml`, "Collected with the store's van"), so a shipment number assigned by the store is the natural identifier, and the maker can quote it once agreed.
- `/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Note`: suspected missing package counts for "original cartons" — refuted because the instruction need not count cartons; the gross weight is given and no other value depends on the count.
