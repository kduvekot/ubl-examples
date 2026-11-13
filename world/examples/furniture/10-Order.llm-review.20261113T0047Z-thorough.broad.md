# LLM review: 10-Order.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/10-Order.xml`, Git blob `4c325d25cd05fed989cbd0f6f69ef7970de5cb48` (committed)
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

### furniture/10#F1 · High · Taxable amount ignores the line discount
- XPath: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `11834.00`
- Why: The line carries a 3 % repeat-order discount (366.00), so the line extension and the anticipated total are 11 834.00. The tax subtotal still gives 12 200.00 as taxable amount ("The net amount to which the tax percent (rate) is applied"), the amount before the discount. The arithmetic does not hold (the tax amount is 0 either way, which hides it).
- Condition: `TaxSubtotal/cbc:TaxableAmount` equals the sum of the line extension amounts it covers, 11834.00.
- Options: (a, preferred) 11834.00.
- Needs decision: no

### furniture/10#F2 · Medium · Quotation line reference without a quotation
- XPath: `/Order/cac:OrderLine/cac:QuotationLineReference/cbc:LineID` = `1`
- XPath: `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574`
- Why: `QuotationLineReference` is "A reference to a quotation line associated with this order line" and holds only a line number. This order has no `QuotationDocumentReference` (unlike `08-Order.xml`); its only document reference is to the earlier order. Line 1 of which quotation is meant cannot be resolved from the document.
- Condition: The quotation line reference can be resolved: the order references the quotation `BF-DOC-26-0568`, or the line reference carries its document, or it is absent.
- Options: (a, preferred) add `QuotationDocumentReference` `BF-DOC-26-0568`, since the price is the quoted one and the quotation is still valid on 2026-04-16; (b) remove the quotation line reference.
- Needs decision: no

### furniture/10#F3 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/10#F4 · Low · Repeat order of 20 sets when the shelf is far above its target
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:TargetInventoryQuantity` = `10`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cbc:MinimumInventoryQuantity` = `4`
- Why: By the profile the store sent (`04-TradeItemLocationProfile.xml`), a replenishment order is triggered when stock falls to 4 sets, and the target stock is 10. On 2026-04-16 the store had received 20 sets (`09-Invoice.xml`) and, by `06-ProductActivity.xml`, sold 3 by 2026-04-20, so about 17 were on hand. Ordering another 20 then contradicts the agreed policy. The inference rests on the sales figures, so this needs a decision.
- Condition: The second order follows from the replenishment policy in 04 and the stock implied by 06 and 09 (or its note says why it departs from it).
- Options: (a) date and size the repeat order to the policy (e.g. before the season peak, with a note on expected demand); (b) a note explaining the early order (promotion planned), preferred as the smaller change.
- Needs decision: yes

### furniture/10#F5 · Low · Repeat-order discount has no source
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Repeat order`
- XPath: `/Order/cac:OrderLine/cbc:Note` = `Price as quoted.`
- Why: The order applies a 3 % repeat-order discount, while the note says "Price as quoted" and the quotation `02-Quotation.xml` offers no repeat-order discount. Who granted it is not stated anywhere in the flow.
- Condition: The discount follows from a quotation, contract or agreement in the flow, or the note says it is agreed separately.
- Options: (a, preferred) a note naming the basis of the discount (e.g. agreed by phone, or terms of the own-line contract); (b) the discount in the quotation.
- Needs decision: no

### furniture/10#F6 · Low · Own-line item carries the maker's brand
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:Note` = `The store's own line: bench and two chairs per set.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Garden bench and two chairs in hardwood, made for the department store's own line.`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Brackenmere`
- Why: The description (and in some examples the notes) says the set is made for the department store's own line, i.e. a private-label product of Brightmarket. `BrandName` ("A brand name of this item") says the brand is Brackenmere, the maker. An own-line product is normally sold under the retailer's brand; the text and the structured brand therefore point in different directions. It may be a legitimate exclusive line under the maker's brand, which is why this needs a decision.
- Condition: The item's brand and its description of the line agree: either the brand is the store's own-line brand, or the text no longer says it is the store's own line/label.
- Options: (a, preferred) a Brightmarket own-line brand name in `BrandName` (the GTIN may then also be the store's), because RFQ, quotation and order all stress the own line; (b) reword the description as an exclusive Brackenmere line made for the store.
- Needs decision: yes

### furniture/10#F7 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- Discount: 0.03 × 12 200 = 366; 12 200 − 366 = 11 834 = line extension = anticipated total.
- `/Order/cac:OrderDocumentReference/cbc:ID` = `BS-PO-26-0574` resolves to `08-Order.xml` ("A reference to another Order"); the order is cancelled by `11-OrderCancellation.xml`.
- Sub-lines 7 600 + 4 600 = 12 200 = the base amount of the discount.
