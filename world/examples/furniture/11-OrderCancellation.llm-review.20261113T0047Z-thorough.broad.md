# LLM review: 11-OrderCancellation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/11-OrderCancellation.xml`, Git blob `f390fff919e1ccd9ec4fabfe839b81fd2f19846c` (committed)
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

### furniture/11#F1 · Medium · Quotation number used as a contract identifier
- XPath: `/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`
- Why: `Contract` is "A contract associated with the original Order(s)" and its ID "An identifier for this contract". `BF-DOC-26-0568` is the document number of the quotation `02-Quotation.xml`, not a contract identifier; neither cancelled order (`10-Order.xml`) nor the first order mentions a contract. The only contract in the flow is the own-brand contract `BM-OWN-BRAND-2026` of the request `01-RequestForQuotation.xml`.
- Condition: `Contract/cbc:ID` identifies a contract (e.g. `BM-OWN-BRAND-2026`), or the quotation is referenced as a document, or the element is absent.
- Options: (a, preferred) remove it, since the orders cite no contract; (b) the own-brand contract `BM-OWN-BRAND-2026` if it governs the orders.
- Needs decision: no

### furniture/11#F2 · Medium · Language code in LocaleCode
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is defined as "A code signifying the locale in which this language is used". A locale is a language in a region (in practice a tag such as `en-XB`), not the language itself; the value `en` with `listID="ISO 639"` only repeats `Language/cbc:ID` and says nothing about the locale. The same value occurs 362 times in 213 examples (counted with `grep -rh --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l` and `grep -rl … | wc -l`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) a locale such as `en-XB` from a BCP 47-style list, because the parties do trade in a specific country; (b) drop `LocaleCode` where no locale is needed.
- Needs decision: no

### furniture/11#F3 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Brightmarket Stores acts here as the buying side (buyer, retailer or accounting customer). Its contact is named "Buying office" but its job title is "Customer service officer" and its department "Sales": name, title and department contradict each other, and a sales/customer-service desk is not the contact for the buying role (nor, in billing documents, for accounts payable). The same contact is used in all 14 Brightmarket examples of this flow.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the role the party has in this document.
- Options: (a, preferred) a buyer contact in purchasing (e.g. job title "Buyer", department "Purchasing"), and in billing documents an accounts-payable contact; (b) keep "Buying office" and change only title and department.
- Needs decision: no

## Checked and consistent
- `/OrderCancellation/cac:OrderReference/cbc:ID` = `BS-PO-26-0576` resolves to `10-Order.xml`, the repeat order (the "second delivery"); the cancellation (2026-04-22) follows the exception notification of 2026-04-21.
- `/OrderCancellation/cac:OriginatorDocumentReference/cbc:ID` = `BF-DOC-26-0573` resolves to `07-ExceptionNotification.xml`, and the additional reference to `06-ProductActivity.xml`; the cancellation note (sales below the agreed threshold) matches them.

## Considered and refuted
- `/OrderCancellation/cac:OriginatorDocumentReference/cbc:ID`: the originator document is the seller's exception notification while the originator party is the store — refuted, the definition ("A reference to an originator document associated with this document") does not tie it to the originator party; the notification is what led to the cancellation.
- `/OrderCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: repeats the buyer — refuted as in 01 (explicit statement, IND6).
