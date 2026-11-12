# LLM review: 02-OrderResponse.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/02-OrderResponse.xml`, Git blob `ed508cac8f8d97787b90685b12c76dfda6ffaaa6` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/02#F1 · Medium · Province of the seller's address in Region
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province belongs in `CountrySubentity` (+ `CountrySubentityCode` where a list exists), as the Bayvarran address of the same document does (`/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). The value has no `languageID`, unlike the other parts of the address. 219 occurrences in 104 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; where the province is given, it is in `cbc:CountrySubentity` (and its code, where a list exists).
- Options: (a) move the province to `CountrySubentity` (preferred: what the element is for, and as the Bayvarran addresses do); (b) drop it where the postal code already identifies the place; (c) keep `Region` only if Ferrano is an economic region, recorded in the world data.
- Needs decision: no
- From: broad, parties, context

### plastics/02#F2 · Medium · Language code in LocaleCode
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language, already in `Language/ID`, not a locale (language plus region, e.g. the `en-XB` the flow uses as `languageID`). All 362 `LocaleCode` elements, in 213 of the 250 XML examples, carry this value (`grep -rho --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l`).
- Condition: `LocaleCode` carries a locale from a locale list named in `listID`, or is absent.
- Options: (a) drop it (preferred: the language is in `Language/ID`); (b) `en-XB` with a BCP 47 / CLDR list as `listID`.
- Needs decision: no
- From: broad, parties, context

### plastics/02#F3 · Low · Both parties registered on 1 January 1996
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". Companies in two countries' registers share New Year's Day 1996, the most frequent registration date in the world (271 occurrences in 181 of the 250 XML examples, `grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`); it reads as a default (IND5/IND6) unless the story explains it.
- Condition: each registration date is the company's own, or the shared date is explained by the world's history, or the element is absent.
- Options: (a) individual dates from each company's history (preferred); (b) record a general (re-)registration on that date in the story; (c) drop it where no history is known.
- Needs decision: yes
- From: broad, parties, context

### plastics/02#F4 · Low · Buyer's contact is a sales/customer-service desk
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact, who receives the answer to its order, is the buying function; an order desk staffed by a customer-service officer in Sales is the seller-side function. It is the same contact as in `01-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`; the parties carry one generic contact in every document of the flow.
- Condition: the buyer's contact is a purchasing contact (name, job title and department agreeing with that role), or absent.
- Options: (a) role-specific contacts for Rivermouth, the purchasing one here (preferred); (b) a neutral general contact, or none.
- Needs decision: no
- From: broad, parties, context

### plastics/02#F5 · Low · Buyer's bank account in an order response that moves no money
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". The response only accepts the order (`/OrderResponse/cbc:OrderResponseCode` = `AP`); it carries no amounts, payment means or terms, and nothing uses the buyer's account (section 4.8; IND5). The account appears in 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples | wc -l`); the flow uses it only where Rivermouth pays (`11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`).
- Condition: the order response carries no party financial account unless it uses one.
- Options: (a) drop it (preferred); (b) keep it only with a payment arrangement in the response that needs it.
- Needs decision: no
- From: broad, money, parties, context

### plastics/02#F6 · Low · Italian text tagged as English
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering should be in the language its `languageID` names. The `en-XU` renderings of the street ("Via del Riciclo", "Recycling street") and of the legal form (Italian with an English gloss) are Italian. Bayvarran streets in the flow are English (`Estuary Road`). The pattern occurs in 101 of the 250 XML examples (parties part, `grep -rlE --include='*.xml' 'languageID="en-X[UB]">(Via|Banchina|Piazza|Valico|Società)' world/examples | wc -l`). Counter-argument (refutation of the same candidate in the broad and context parts of `01-Order.xml`): the world renders Urvanian names in English text by Italianate exonyms (`Ferrano` for `Ruldraz`), a fictional convention. That can hold for the street name, but the legal form is a description, not a proper name; the merge cannot settle the street-name part.
- Condition: every rendering tagged `en-…` is English or a proper name used as such in English, and the exonym convention is recorded in the world story if it is meant.
- Options: (a) record the exonym convention and render the legal form in English (preferred); (b) translate all renderings into English; (c) drop the second rendering where the local form suffices.
- Needs decision: yes
- From: parties

### plastics/02#F7 · Low · Rinova's waste-recovery permit in an order response for a product
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: `Party/PartyAuthorization` is "An authorization issued to this party": Rinova's permit to recover plastic waste (Basel Annex IV R3). The goods are recycled PE granulate classified as a product (HS 390110), and an acceptance without lines depends on nothing in the permit. It is in 14 XML examples, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples | wc -l`): master data copied into every document (IND5). Counter-argument (broad part): it backs the recycled-content claim of the ordered goods. The merge does not follow it: this response carries no item and no claim, and in the order the claim has its own item-level certificate.
- Condition: the permit appears only in documents that act on it, or the document says why it is relevant.
- Options: (a) remove it (preferred); (b) if the recycled-content claim is to rest on it, connect it to the item's `EnvironmentalCertificate` in the documents that carry the item.
- Needs decision: no
- From: parties, context (broad refuted it)

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `RP-PO-26-0882` resolves to `01-Order.xml`; buyer and seller are the same parties with the same identifiers, names, tax and legal data; the response is issued the day after the order.
- `OrderResponseCode` `AP` (accepted) without lines: an acceptance without changes needs no lines; the commercial values of `01-Order.xml` stand and the goods invoice uses them unchanged (83 200 `XUF` per tonne, 120 t).
- The seller's Sales contact fits the seller. Parties are described the same way across the flow apart from renderings (parties part, script over the flow; see `01-Order.xml` review for Rinova's renderings by issuer). ISIC codes fit. `check_ids.py`: the IBAN-like account passes.

## Considered and refuted
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode`: the waste-recovery authorisation copied into the response — refuted by broad because it backs the recycled-content claim of the ordered goods. The merge disagrees; kept as F7. (from broad)
- `/OrderResponse/cbc:OrderResponseCode`: an acceptance without lines or delivery date — refuted: `AP` accepts the order as placed, and the order itself carries no delivery date to confirm. (from broad, context)
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` could clash with a real ICD — refuted: 0990 is not assigned in the real register (own knowledge). (from parties)
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped bank identifier (`BLUMXBLX`) could be a real BIC — refuted: positions 5–6 carry the user-assigned code `XB`. (from parties)
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: the buyer's customs-trader ID copied from master data — refuted: the parties need each other's customs identities for the declarations of this sale. (from parties)
- The seller's texts tagged `en-XU` here and `en-XB` in the order — refuted by broad as following the sender's languages; carried as counter-argument in the `01-Order.xml` merged review (F7 there). (from broad)

## Changed in the merge
- broad/F1, parties/F1, context/F1 → F1: combined.
- broad/F2, parties/F2, context/F2 → F2: combined; preferred option "drop" (parties) over "en-XB" (broad, context), for consistency with the other merges of this run.
- broad/F5, parties/F6, context/F6 → F3: combined; "Needs decision" yes (broad, context) rather than no (parties): depends on the world's company histories.
- broad/F3, parties/F3, context/F5 → F4: combined.
- broad/F4, money/F1, parties/F4, context/F3 → F5: combined.
- parties/F7 → F6: counter-argument from the refutations in `01-Order.xml` added; preferred option changed to "record the convention, render the legal form in English".
- parties/F5, context/F4 → F7: combined; "Needs decision" no (context) instead of yes (parties): removing an unused party permit changes no story; broad's refutation added as counter-argument.

## Outside this review
- Timeline across documents: Rinova requests the barge (`03-TransportExecutionPlanRequest.xml`, issued 2026-04-14 09:57) before it accepts the order (this response, 2026-04-14 15:39). Plausible as a capacity check; a question for the consistency review. (from broad, context)
