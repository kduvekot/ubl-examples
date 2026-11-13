# LLM review: 11-OrderCancellation.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/11-OrderCancellation.xml`, Git blob `f390fff919e1ccd9ec4fabfe839b81fd2f19846c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e69f7ed 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: parts written so far
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

### furniture/11#F1 · Medium · The quotation's document number used as a contract identifier
- XPath: `/OrderCancellation/cac:Contract/cbc:ID` = `BF-DOC-26-0568`
- Why: `Contract` is "A contract associated with the original Order(s)" and its `ID` "An identifier for this contract". `BF-DOC-26-0568` is the document number of the seller's quotation (`02-Quotation.xml:/Quotation/cbc:ID` = `BF-DOC-26-0568`), an offer, not a contract: an identifier of one kind used as another. The flow does name a contract for this supply relation, the store's own-brand contract (`01-RequestForQuotation.xml:/RequestForQuotation/cac:Contract/cbc:ID` = `BM-OWN-BRAND-2026`), so the flow now gives two different contract identifiers for the same relation; neither cancelled order (`10-Order.xml`) nor the first order names a contract. The debit note does the same (`14-DebitNote.xml:/DebitNote/cac:ContractDocumentReference/cbc:ID` = `BF-DOC-26-0568`).
- Condition: `Contract/cbc:ID` identifies a contract of the story (`BM-OWN-BRAND-2026`), or the element is absent; the quotation, if referenced, is referenced as a document.
- Options: (a, preferred) `Contract/ID` = `BM-OWN-BRAND-2026`, the contract the request for quotation was made under (logistics, context); (b) remove `Contract`, since the cancellation needs only the order reference (broad's preference).
- Needs decision: no
- From: broad, logistics, context

### furniture/11#F2 · Medium · Language code in LocaleCode
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. a language in a region. `en` with `listID="ISO 639"` is the language itself and repeats `Language/cbc:ID`. 362 occurrences in 213 examples (merge recount: `grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples | wc -l`, files with `grep -rl`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale from a list that defines locales, with the matching listID, or is absent.
- Options: (a, preferred) remove `LocaleCode`; (b) a locale such as `en-XB` from a BCP 47-style list.
- Needs decision: no
- From: broad, parties, context

### furniture/11#F3 · Low · "Cancelled before production" after the delivery the lead time implies
- XPath: `/OrderCancellation/cbc:Note` = `No cost: cancelled before production.`
- XPath: `/OrderCancellation/cbc:IssueDate` = `2026-04-22`
- XPath: `10-Order.xml:/Order/cbc:IssueDate` = `2026-04-16`
- XPath: `04-TradeItemLocationProfile.xml:/TradeItemLocationProfile/cac:ItemManagementProfile/cac:ItemLocationQuantity/cbc:LeadTimeMeasure` = `5`
- Why: The cancelled order has no requested delivery date (`10-Order.xml`, its F6), so the agreed lead time of 5 days applies: merge recalculation 2026-04-16 + 5 days = 2026-04-21, one day before this cancellation. A cancellation after the due delivery date can hardly come "before production". The contradiction rests on an implied date (the order states none, and production might be scheduled later for a seasonal order), so it is kept Low with a decision.
- Condition: The cancellation date lies before the production or delivery date the flow implies for the cancelled order.
- Options: (a, preferred) give `10-Order.xml` a requested delivery period well after 2026-04-22 (e.g. the summer peak), which makes "before production" true and fits 10's F3 option (a); (b) move the cancellation before 2026-04-21, which conflicts with the exception notification of 2026-04-21 17:49 that triggered it.
- Needs decision: yes
- From: logistics

### furniture/11#F4 · Low · Originator document is the seller's exception notification
- XPath: `/OrderCancellation/cac:OriginatorDocumentReference/cbc:ID` = `BF-DOC-26-0573`
- XPath: `/OrderCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorDocumentReference` is "A reference to an originator document associated with this document"; in the ordering documents the originator is the `OriginatorCustomerParty`, here Brightmarket, and its document is typically the requisition behind the order. `BF-DOC-26-0573` is the seller's exception notification (`07-ExceptionNotification.xml`), issued by Brackenmere. Broad and context refuted this: the definition does not tie the document to the originator party, and the notification is what led to the cancellation. Both readings are defensible; the merge cannot settle which the world means.
- Condition: The originator document reference points to a document of the originator customer party, or the exception notification is referenced as an additional document, or the world records that "originator document" means the cause of the cancellation.
- Options: (a, preferred) move `BF-DOC-26-0573` to an `AdditionalDocumentReference`, next to the product activity report already there; (b) keep it and record the reading.
- Needs decision: yes
- From: logistics (broad and context refuted it)

### furniture/11#F5 · Low · Originator and beneficiary repeat the buyer
- XPath: `/OrderCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/OrderCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Brightmarket Stores`
- Why: `OriginatorCustomerParty` ("The originator") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended or who derives benefit from it") carry information when they name someone other than the buyer (a requisitioning department, an end user). Both are the buyer itself, with the same identifier, and the cancelled order `10-Order.xml` carries neither, so they are not even repeated from the order they cancel. Broad refuted this as an explicit statement (IND6: nothing implied by absence); the merge keeps the finding because the order being cancelled does without them, so their presence here suggests a distinction the story does not have.
- Condition: Both are absent, or each names a party other than the buyer with its own role.
- Options: (a, preferred) remove both; (b) make them real other parties (e.g. Brightmarket's garden department as originator), which would change the story.
- Needs decision: no
- From: parties, context (broad refuted it)

### furniture/11#F6 · Low · Brightmarket's contact is a sales desk in a buying role
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name ("Buying office"), job title ("Customer service officer") and department ("Sales") do not agree with each other, and a buyer's contact buys. The same contact is used in every example where Brightmarket is described in full.
- Condition: Brightmarket's contact has a name, job title and department that agree with each other and with the buyer role.
- Options: (a, preferred) a buyer contact, e.g. job title "Buyer", department "Purchasing"; (b) keep "Buying office" and change only title and department.
- Needs decision: no
- From: broad, parties

### furniture/11#F7 · Low · Parties' master data copied into the cancellation
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1231233`
- XPath: `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1237398`
- Why: The store's logo, online-shop website, social-media profile and share capital (with the fully-paid-shares indicator), and both parties' state sales-tax registrations, come from master data. An order cancellation carries no amounts, no tax treatment and no payment, so none of them is used here (section 4.8, IND5). The marketing data are carried on Brightmarket in examples 01 to 14.
- Condition: The document carries these elements only where it has a reason to.
- Options: (a, preferred) remove them from this document, keeping identification, name, address and contact; (b) keep them with a stated reason (none is apparent).
- Needs decision: no
- From: parties (web site, social media; tax registrations and share capital), context (logo, web site, social media, share capital)

## Checked and consistent
- `/OrderCancellation/cac:OrderReference/cbc:ID` = `BS-PO-26-0576` resolves to `10-Order.xml`, the repeat order of the same buyer and seller, issued before the cancellation; "the second delivery" in the cancellation note fits it.
- `/OrderCancellation/cac:AdditionalDocumentReference/cbc:ID` = `BS-DOC-26-0572` resolves to `06-ProductActivity.xml`, `BF-DOC-26-0573` to `07-ExceptionNotification.xml`; the reason (sales below the agreed threshold) matches them.
- Order of events: product activity 2026-04-20 16:35 → exception notification 2026-04-21 17:49 → cancellation 2026-04-22 11:51.
- "No cost" agrees with the absence of any charge for the cancelled order in the later documents of the flow.
- Parties described identically across the flow; GLNs pass their check digits.

## Considered and refuted
- `/OrderCancellation/cbc:CancellationNote`: "the second delivery is not needed" for what is a separate order — refuted because the repeat order is in plain words the second delivery of the line (from context).
- `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: GLN 9523710900008 could be a real GS1 key — refuted because GS1 prefix 952 is reserved for demonstrations and examples (own knowledge) (from parties).
- `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: +999 numbers could be real — refuted because 999 is spare in ITU-T E.164 and the domains are under .example (from parties).
- `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate`: 1996-01-01 looks like a placeholder — refuted because nothing depends on it (from parties).
- `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle`: Brackenmere's trade-sales contact — refuted because it fits the seller and name, title and department agree (from parties).
- `/OrderCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:ID`: state-level versus city-level address register — refuted because the rule is "address registers by country level" (from parties).
- `/OrderCancellation/cac:BuyerCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:Name`: handle and account number in `Name`/`ID` — refuted because the aggregate is the profile; its presence is F7 (from parties).
- The broad part's refutation of the beneficiary repeating the buyer, and the broad and context parts' refutation of the originator document, are carried in F5 and F4, which the merge kept as findings.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; option (a) BM-OWN-BRAND-2026 preferred, as two of three parts (broad preferred removal, kept as (b)).
- broad/F2, parties/F1, context/F2 → F2: removal preferred, as in earlier flows.
- logistics/F2 → F4: kept Low/yes against the refutations of broad and context, both arguments stated.
- parties/F5, context/F3 → F5: combined; kept against broad's refutation (argument stated).
- broad/F3, parties/F2 → F6: combined.
- parties/F3, parties/F4, context/F4 → F7: grouped into one finding of copied master data.
