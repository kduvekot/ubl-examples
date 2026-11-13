# LLM review: 12-InstructionForReturns.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

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

### furniture/12#F1 · Medium · Language code in LocaleCode
- XPath: `/InstructionForReturns/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/12#F2 · Low · No place to return the goods to
- XPath: `/InstructionForReturns/cac:Shipment/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-02`
- XPath: `14-DebitNote.xml:/DebitNote/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9523710900015`
- Why: The instruction asks the store to return six sets between 2026-04-29 and 2026-05-02 but does not say where to: the shipment's delivery has a period and no location or address. The debit note `14-DebitNote.xml` shows the goods were delivered to Brackenmere's location `9523710900015`, which is not the seller's postal address in this document (nothing is implied by absence).
- Condition: The return shipment's delivery names the place the goods go to, the same location as in 14.
- Options: (a, preferred) `Shipment/Delivery/DeliveryLocation` with GLN `9523710900015` and its name, as in 14.
- Needs decision: no

### furniture/12#F3 · Low · Return shipment numbered with the store's prefix
- XPath: `/InstructionForReturns/cac:Shipment/cbc:ID` = `BM-RET-26-0427`
- XPath: `/InstructionForReturns/cbc:ID` = `BF-DOC-26-0578`
- Why: The instruction is issued by Brackenmere (`BF-` numbers, signature `BF-SIG-26-0427`), but the shipment ID uses Brightmarket's prefix `BM-` (as in `BM-SIG-…`, `BM-551004`, `BM-SVC-RT`). The issuer of the instruction would not normally assign the store's shipment numbers before the store has arranged the transport.
- Condition: The shipment ID is one the issuer can assign (a Brackenmere return authorisation number), or the document explains that the store gave it.
- Options: (a, preferred) a Brackenmere return number (e.g. `BF-RET-…`); (b) keep it if the store assigned it in advance.
- Needs decision: no

### furniture/12#F4 · Low · Manufacturer stated twice, identical to the seller
- XPath: `/InstructionForReturns/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:ManufacturerParty/cac:PartyName/cbc:Name` = `Brackenmere Furniture`
- Why: The manufacturer is given at document level and again on the only line, both times the seller itself. One statement is enough; the line-level party adds nothing (IND5).
- Condition: The manufacturer is stated once (document level), or the line-level party differs from it.
- Options: (a, preferred) keep the document-level `ManufacturerParty`, remove the line-level one.
- Needs decision: no

### furniture/12#F5 · Low · Own-line item carries the maker's brand
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/InstructionForReturns/cac:InstructionForReturnsLine/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/12#F6 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/InstructionForReturns/cac:RetailerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- Physics: `/InstructionForReturns/cac:Shipment/cbc:GrossWeightMeasure` = `282` kg for 6 sets = 47 kg per set in cartons; a 1.4 m hardwood bench of about 25–30 kg plus two chairs of about 8 kg each plus cartons (own knowledge) gives 41–50 kg. Plausible.
- Six sets returned: 20 received (`09-Invoice.xml`), 3 sold by 2026-04-20 (`06-ProductActivity.xml`), about 17 on hand; returning 6 leaves 11, close to the target of 10 in `04-TradeItemLocationProfile.xml`.
- The document type fits: the producer requests the return of products that are not selling well (UBL definition of Instruction For Returns), triggered by `07-ExceptionNotification.xml`, which it references.
- Requested period 2026-04-29 to 2026-05-02 contains the actual delivery 2026-05-02 in `14-DebitNote.xml`; credit note `13-CreditNote.xml` credits the same 6 sets.

## Considered and refuted
- `/InstructionForReturns/cac:DocumentReference/cbc:ID`: no reference to the order or invoice of the returned goods — refuted, the instruction needs the item and quantity, and the credit note links the return to invoice 09.
