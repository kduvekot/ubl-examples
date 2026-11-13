# LLM review: 12-InstructionForReturns.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/12#F1 · Medium · LocaleCode holds a bare language code
- XPath: `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/12#F2 · Low · Return shipment without destination or carrier
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-04-29`
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-02`
- Why: The document is "used to initiate a return of goods". Its shipment asks for delivery in a period but says neither where the sets go nor who carries them. The debit note `14-DebitNote.xml` later charges the maker for the store's transport to Marrowdale (`14-DebitNote.xml:/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:Name` = `Brackenmere Furniture, Marrowdale`, line note "Collected with the store's van."), i.e. the maker asked the store to carry the goods at the maker's cost. That arrangement, which the debit note relies on, appears nowhere in the instruction.
- Condition: the instruction states the return destination and who carries the goods (and, if the story keeps it, that the store transports at the maker's cost).
- Options: (a) add the delivery location (Brackenmere, Marrowdale) and a note or carrier that the store delivers with its own van at the maker's cost (preferred: makes the later debit note follow from this document); (b) let the maker collect, and drop the transport debit note.
- Needs decision: yes

### furniture/12#F3 · Low · Manufacturer repeated at header and line, identical to the seller
- XPath: `/InstructionForReturns/cac:ManufacturerParty`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:ManufacturerParty`
- Why: `ManufacturerParty` is "The Party that manufactures the goods to which this Instruction for Return applies" (header) and "The Party who manufactures the Goods being returned" (line). Both name Brackenmere Furniture (`20412466`), which is also the seller. The header element already covers all lines; the line repeats it, and with one line and one maker the repetition adds nothing.
- Condition: the manufacturer is stated once (header), or at line level only where lines have different manufacturers.
- Options: (a) keep the header `ManufacturerParty` and remove the line one (preferred: the document definition speaks of "the producer" requesting the return); (b) none other seen.
- Needs decision: no

### furniture/12#F4 · Low · Brand name of the maker on an item for the store's own line
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:BrandName` = `Brackenmere`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- Why: A store's own line is sold under the retailer's label (`02-Quotation.xml:/Quotation/cbc:Note` = `Including the store's own label.`); `BrandName` = the maker's name contradicts the description unless the story means a co-branded line. Same in 12 furniture examples.
- Condition: `BrandName` is the brand the item is sold under, consistent with the description.
- Options: (a) the store's label (preferred); (b) reword to a maker-branded exclusive line.
- Needs decision: yes

### furniture/12#F5 · Low · Retailer's master data copied into the instruction
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in a return instruction (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- The purpose fits the UBL definition exactly ("The producer is requesting the return of products that are not selling well … to free up rack or shelf space"); the note says the same.
- `Quantity` 6 sets agrees with the note and with the credit note `13-CreditNote.xml` (6 sets credited).
- `DocumentReference` resolves to the exception notification `07-ExceptionNotification.xml`, the reason for the return.

## Considered and refuted
- `/InstructionForReturns/cac:InstructionForReturnsLine/cbc:Note` = `In their original cartons.`: suspected filler — refuted because packing instructions are a real part of a return instruction.
