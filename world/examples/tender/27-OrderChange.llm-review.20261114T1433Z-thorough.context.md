# LLM review: 27-OrderChange.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/27-OrderChange.xml`, Git blob `e43fb0041dc6f797ab80a2e9f8efb406a7c4464c` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 1ae0e51 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/27#F1 · High · "30 days after the invoice, as the contract says" is not what the contract says
- XPath: `/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`
- Why: The note cites the contract. The contract's payment terms are `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.`: the 30 days run from the acceptance of the release, not from the invoice. The two starting points give different due dates (the invoice of this release is issued on 2026-03-31, before any acceptance is recorded), so the order change misquotes the contract it refers to.
- Condition: Payment terms stated in the order change agree with the contract's (30 days after the acceptance of the release), or the change does not restate them.
- Options: (a) preferred: leave payment terms out of a change that only alters the colour; (b) quote the contract's wording.
- Needs decision: no

### tender/27#F2 · Medium · The new total given as "amount of change"
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:ChargeTotalAmount` = `200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: In an order change `AnticipatedMonetaryTotal` is "The amount of change to the total cost of the order anticipated by the buyer". The change adds a charge of 200.00 for the special colour to an order of 19960.00 (`26-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`); the amount of change is 200.00. The total given, 20160.00 with line amounts of 19960.00, is the new total of the whole order.
- Condition: The anticipated monetary total of the order change states the change to the order's cost (200.00 payable, no line extension amount), or the documents of the flow record that the world reads it as the new total.
- Options: (a) preferred: `ChargeTotalAmount` 200.00 and `PayableAmount` 200.00; (b) keep the new total and record the deviation from the UBL definition as a finding (common practice treats an order change as a full replacement).
- Needs decision: yes (definition against practice)

### tender/27#F3 · Medium · A province in `Region`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative division of a country, for which the address has `CountrySubentity` ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the same documents put their state in `CountrySubentity`.
- Condition: The province of an Urvanian address is in `CountrySubentity` (with its code in `CountrySubentityCode` where a list exists), and `Region` is absent or holds a region in the sense of the definition.
- Options: (a) preferred: move the province to `CountrySubentity`; no other direction seen.
- Needs decision: no
### tender/27#F4 · Medium · A language code as locale
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used", i.e. where (in which country or regional variant) the language is used. The value repeats the language code of the sibling `cbc:ID` from the list ISO 639 and says nothing about a locale.
- Condition: `LocaleCode` is either absent or holds a locale (the place or variant in which the language is used) from a list of locales, not the language code again.
- Options: (a) preferred: remove it where the party's language needs no locale; (b) give a real locale (e.g. the language as used in Bayvarra) from a list defined for it.
- Needs decision: no
### tender/27#F5 · Low · A change of colour that restates payment means, terms, conditions, exchange rates and a forwarder
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`
- XPath: `/OrderChange/cac:TransactionConditions/cbc:Description` = `The framework contract's conditions apply.`
- XPath: `/OrderChange/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderChange/cac:TaxExchangeRate`
- XPath: `/OrderChange/cac:PricingExchangeRate`
- XPath: `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract`
- XPath: `/OrderChange/cac:PaymentExchangeRate`
- XPath: `/OrderChange/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: An order change is "A document used to specify changes to an existing Order", and this one changes one thing (`/OrderChange/cbc:Note` = `Please deliver the benches of this release in moss green, RAL 6005.`). It also carries the seller's bank account with branch and bank address, transaction conditions, three exchange rates with a forward contract of 2026-01-02 and a pricing currency ferra, although it contains no price and all its amounts are in lume (`/OrderChange/cbc:RequestedInvoiceCurrencyCode` = `XBL`), and a freight forwarder. None of these was in the order (`26-Order.xml` has no payment means, transaction conditions or forwarder), and none is a change the note or the line announces. Bayforth Forwarding moves nothing in this flow: the goods are despatched by Castrano Logistics (`29-DespatchAdvice.xml`), and Bayforth appears otherwise only as the seller's tax representative in the invoice and its follow-ups. Under DAP the carrier is the seller's choice, so the buyer has no forwarder to nominate.
- Condition: The order change contains what changes (colour, charge, new amounts) and the references that identify the order; payment means, rates and parties are present only if they are themselves changed or needed by the change.
- Options: (a) preferred: remove payment means, transaction conditions, exchange rates, pricing currency and the freight forwarder; (b) keep those the world's rule requires in every order document, with a stated reason; a forwarder only if one is actually nominated and then acts in the despatch.
- Needs decision: yes (who Bayforth is in this flow, and how complete an order change is)

### tender/27#F6 · Low · The changed line does not identify the item
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `Park bench Serra 180, frame in moss green RAL 6005`
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: The order identifies the bench as `VI-B180` with the extended identifier `GRY`, "Item 123 Ext 45 = brown chair" in the words of the definition, plus a colour attribute and a colour property. The change of exactly that variant is expressed only as free text; the line has no seller's item identification and no new extended identifier, attribute or property for green. The seller's system cannot tell from structured data which variant is now ordered, and all later documents of the flow in fact still carry `GRY` and "Ferro grey" (`29-DespatchAdvice.xml`, `30-ExportCustomsDeclaration.xml`, `31-ImportCustomsDeclaration.xml`, `32-Invoice.xml`, `33-CreditNote.xml`; found with grep for `GRY` and "Ferro grey" over `world/examples/tender/*.xml`).
- Condition: The revised line identifies the item (`VI-B180`) and states the new colour in the same structured places in which the order stated the old one.
- Options: (a) preferred: seller's item identification with an extended identifier and colour attribute for moss green (the colour list needs a code for it); (b) keep the text and add at least the item identification.
- Needs decision: no

### tender/27#F7 · Low · A public body described as a company in a commercial register, with a liquidation status
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The party is a public body (a city department or a state service; industry classification 8411 or the like). `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status": a public body cannot be in liquidation, so "active, not in liquidation" has no meaning for it, and a registration scheme typed "Commercial register" does not fit a body that is not a company.
- Condition: The legal entity of a public body carries no liquidation status, and its registration scheme is not typed as a commercial register.
- Options: (a) preferred: drop the liquidation status and type the register as what it is for public bodies (or omit the type); (b) reduce the public body's legal entity to registration name and identifier.
- Needs decision: no
### tender/27#F8 · Low · Master data of a party that the document does not use
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/OrderChange/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`
- Why: The party carries its share capital, whether the shares are fully paid, its stock-exchange listing and a logistics service provider ("A party providing a service to this party"). An order change tells the seller what the buyer wants changed; the seller's share capital, listing and warehouse provider are not part of that. Under the rule that every value needs a business reason in the document that carries it, this reads as master data copied into the document.
- Condition: The party carries share capital, listing and service provider only in documents whose purpose uses them (e.g. a qualification or business information about the party, or a document in which the service provider acts).
- Options: (a) preferred: remove these elements here; (b) keep those for which a use in this document can be stated.
- Needs decision: no
## Checked and consistent
- `check_ids.py` reported nothing wrong (the account number passes the IBAN-like check).
- `OrderReference` `LPWD-PO-26-0212` is the order; the change is issued the next morning (2026-03-24 08:06), with sequence number 1, and is answered within its validity (to 2026-03-27) by `28-OrderResponse.xml` (2026-03-25).
- Arithmetic: 19960.00 + 200.00 = 20160.00; line 40 × 499 = 19960.00, status `Revised`.
- Charge: `ChargeIndicator` true, reason code `CAT` (special colour service) with text "Special colour"; the order response accepts "moss green, at the quoted charge", which matches the quotation reference.
- Signature of the buyer; contract `PWD-2026-PARKS`.

## Considered and refuted
- `/OrderChange/cac:QuotationDocumentReference/cbc:ID`: a quotation that is no example of the flow — refuted for this lens because a quotation for the colour charge is a plausible step and the order response speaks of "the quoted charge"; whether the document must exist in the flow is the logistics part's question.
- `/OrderChange/cac:ValidityPeriod/cbc:EndDate`: a validity for a change — refuted, it tells the seller until when the buyer stands by the change.
- `/OrderChange/cac:Signature`: a signature on an order change — refuted, a public buyer signing a change that costs money is plausible.
- `/OrderChange/cac:AdditionalDocumentReference/cbc:ID`: `PWD-COLOUR-RAL6005` — refuted, a colour specification as annex fits the change.

## Outside this review
- The account of the payee is held in ferra while the invoice currency requested is lume; money part.
