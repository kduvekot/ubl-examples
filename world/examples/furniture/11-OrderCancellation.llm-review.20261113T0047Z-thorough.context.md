# LLM review: 11-OrderCancellation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: context

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

### furniture/11#F1 · Medium · The quotation's document number used as a contract ID
- XPath: `/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`
- Why: `Contract` is "A contract associated with the original Order(s)" and `Contract/ID` "An identifier for this contract". `BF-DOC-26-0568` is the document ID of the quotation `02-Quotation.xml`, an offer, not a contract. The contract of this trade is named in the request: `01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`. An identifier of one kind (a document number) is used as another (a contract number).
- Condition: `Contract/ID` is the identifier of a contract of the story (`BM-OWN-BRAND-2026`), or the element is absent; a reference to the quotation, if wanted, is a document reference.
- Options: (a) `Contract/ID` = `BM-OWN-BRAND-2026` (preferred: the cancellation is made under the own-brand agreement); (b) remove the contract.
- Needs decision: no

### furniture/11#F2 · Medium · LocaleCode holds a bare language code
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID="ISO 639"` is a language code repeating `cac:Language/cbc:ID`. Occurs 362 times in 213 examples (`grep -o` over `world/examples/*/*.xml`).
- Condition: each `cbc:LocaleCode` holds a locale code from a locale list, or is absent.
- Options: (a) remove (preferred); (b) a real locale such as `en-XB`.
- Needs decision: no

### furniture/11#F3 · Low · Originator and beneficiary repeat the buyer
- XPath: `/OrderCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/OrderCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") carry information only when they differ from the buyer. Both are the buyer; the cancelled order `10-Order.xml` has neither, so they are not even repeated from it.
- Condition: both are absent, or each names a party other than the buyer with its own role.
- Options: (a) remove both (preferred).
- Needs decision: no

### furniture/11#F4 · Low · Buyer's master data copied into the cancellation
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: Logo, online-shop website, social-media profile and share capital have no use in an order cancellation (section 4.8). Carried on Brightmarket Stores in examples 01 to 14.
- Condition: present only where the document uses them.
- Options: (a) remove (preferred).
- Needs decision: no

## Checked and consistent
- `OrderReference` resolves to `10-Order.xml` (`BS-PO-26-0576`), the repeat order; `CancellationNote` gives the reason (sales below the threshold) and agrees with `07-ExceptionNotification.xml`.
- `Note` "No cost: cancelled before production." agrees with the absence of any charge in the flow for the cancelled order.

## Considered and refuted
- `/OrderCancellation/cac:OriginatorDocumentReference/cbc:ID` = `BF-DOC-26-0573`: the exception notification as "originator document" was suspected to be the wrong kind — refuted because the definition is open ("A reference to an originator document associated with this document") and the notification is what triggered the cancellation.
- `/OrderCancellation/cbc:CancellationNote`: "the second delivery is not needed" for what is a separate order was suspected to misdescribe it — refuted because the repeat order is in plain words the second delivery of the line.
