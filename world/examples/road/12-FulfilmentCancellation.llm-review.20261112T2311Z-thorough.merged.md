# LLM review: 12-FulfilmentCancellation.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/12-FulfilmentCancellation.xml`, Git blob `e80b06a59cdefc8b05210e1023501fad527985dd` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/12#F1 · Medium · Cancellation refers to the despatch advice as well as the receipt advice it cancels
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`
- XPath: `/FulfilmentCancellation/cac:ReceiptDocumentReference/cbc:ID` = `LD-RA-26-0162`
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The recount found the bench reported short; the shortage did not exist.`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`
- Why: a Fulfilment Cancellation is "A document used to cancel an entire fulfilment document (Despatch Advice or Receipt Advice)"; it has no other element that says which document it cancels, so its despatch and receipt document references are what a receiver reads as cancelled. Only the receipt advice is meant (the note is about the recount at goods-in), and the despatch advice stays valid: the corrected receipt advice still refers to it. Merge: Medium as context (logistics Low), because which document is cancelled is what the document exists to say; the definitions of the references ("associated with this document") allow an uncancelled document, so it is not High.
- Condition: the cancellation names only the receipt advice LD-RA-26-0162 as cancelled; the despatch advice is not referenced as if it were cancelled.
- Options: (a, preferred) drop `DespatchDocumentReference` (the receipt advice and the order reference already link it); (b) move it to an `AdditionalDocumentReference`, or say in the note that the despatch advice stands.
- Needs decision: no
- From: context (F1, Medium), logistics (F1, Low)

### road/12#F2 · Medium · Language code in LocaleCode
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 occurrences in 213 files.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` with a locale list.
- Needs decision: no
- From: broad (F1), context (F3), parties (F1, yes)

### road/12#F3 · Medium · Gate number in AdditionalStreetName of the buyer's postal address
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is an entrance, and a cancellation has no use for it.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop it from the address.
- Needs decision: no
- From: broad (F2), parties (F2)

### road/12#F4 · Medium · Province in Region instead of CountrySubentity
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address uses (`/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`).
- Condition: the province is in `CountrySubentity`.
- Options: (a, preferred) move it; (b) define Urvanian provinces as economic regions.
- Needs decision: no
- From: broad (F3), context (F2), parties (F3)

### road/12#F5 · Low · Contacts that do not fit the cancellation of a receipt advice
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the receipt advice is cancelled by Lumeway's goods-in after its recount (as buyer, its contact would be purchasing), not by its customer service in Sales; Castrano's contact is named `Warehouse office` but has a sales customer-service title and department.
- Condition: Lumeway's contact is the goods-in (or purchasing) function; Castrano's name, title and department agree.
- Options: (a, preferred) goods-in for Lumeway, a warehouse title for Castrano; (b) drop titles and departments that do not fit.
- Needs decision: no
- From: broad (F4), context (F4), parties (F4)

### road/12#F6 · Low · Seller's stock-exchange listing in a cancellation
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: a cancellation identifies the cancelled document and its parties; the seller's listing plays no part (section 4.8, IND5).
- Condition: the cancellation carries no party data without a use in it.
- Options: (a, preferred) drop it.
- Needs decision: no
- From: context (F5, listing part), parties (F5)

### road/12#F7 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: "The registration date of the CompanyID"; 1 January is a public holiday and the date occurs 271 times across the examples for at least 25 companies (parties' count over `*.xml`) (IND5).
- Condition: each party's registration date is its own plausible date, or absent.
- Options: (a, preferred) a date from Castrano's history; (b) leave it out.
- Needs decision: yes (aligned with rail and air)
- From: parties (F6, no)

### road/12#F8 · Low · Italian street names tagged as English
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Magazzino`
- Why: the second rendering of the Urvanian street names is Italian text tagged `en-XB`. Parties refuted it (English keeps foreign street names; the subtag follows the sender); against that, the tag states English for words that are not, next to an Urvanian (`qau`) rendering. The merge cannot settle which reading the world intends; aligned with rail and the other road merges. Rail counted 217 such renderings in 102 files (over `*.xml`).
- Condition: one rule for Italian-form names in English renderings, recorded in the world's language rules, and the tags follow it.
- Options: (a, preferred) record that English renderings keep the Italian exonym; (b) an Italian language tag for the Italian form.
- Needs decision: yes
- From: merge (parties considered and refuted it)

### road/12#F9 · Low · Urvanian legal forms in one untagged rendering
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: in Urvania-issued documents of the flow these legal forms come in two tagged renderings (`qau`, `en-XU`, e.g. `07-CertificateOfOrigin.xml`); here, in a Bayvarra-issued document, they are one untagged text, so the same party is described differently and the language is not stated. Added by the merge, aligned with rail, air and the other road merges.
- Condition: the legal form is rendered as the address is in this document (renderings with language tags).
- Options: (a, preferred) both renderings, tagged.
- Needs decision: no
- From: merge

## Checked and consistent
- `ReceiptDocumentReference` LD-RA-26-0162 resolves to `11-ReceiptAdvice.xml`; despatch CL-DA-26-0153 and order LD-PO-26-0149 resolve to `04` and `01` (all parts).
- Issued 2026-03-26 10:46, after the receipt advice it cancels (2026-03-25 15:40) and two minutes before the corrected receipt advice `13-ReceiptAdvice.xml` (10:48), as the note announces (broad, logistics, context).
- The cancellation note agrees with `13-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ReceivedQuantity` = `96` (broad, logistics, context).
- Buyer, seller and despatch supplier are the parties of the cancelled receipt advice; Castrano, which must correct its records, is rightly present (logistics, context, parties).
- Castrano's `ShareholderParty` (Valdara, 100 %) agrees with Valdara's `ServiceProviderParty` (parties); party identity, GLN and ISIN check digits (parties).

## Considered and refuted
- `/FulfilmentCancellation/cbc:ID` = `LD-DOC-26-0163`: generic `DOC` prefix — refuted because any sender-assigned identifier is valid and the running number fits the flow (from broad).
- `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XB` — refuted by parties; the merge does not follow and made it F8.
- `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN could be real — refuted, prefix 952, check digit correct (from parties).
- `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: could be real — refuted, +999 reserved (from parties).
- `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01` as a contract number — refuted, the definition does not say who assigns it (from parties).

## Refuted in the merge
### context/F5 · Low · Party master data the cancellation does nothing with (shareholder part)
- XPath: `/FulfilmentCancellation/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- Why (context): a cancellation identifies the cancelled document and its parties; the despatch supplier's shareholder plays no part (section 4.8, IND5).
- Condition (context): the cancellation carries no party data without a use in it.
- Refuted because: the shareholding explains why Castrano, not the seller, is the despatch supplier for Valdara's goods (parties checked it as consistent with Valdara's `ServiceProviderParty`); merger C refuted the same part for `13-ReceiptAdvice.xml`. The listing part of context/F5 is kept as F6.

## Changed in the merge
- context/F1, logistics/F1 → F1: Medium (logistics Low).
- parties/F1 → F2: Needs decision no, aligned.
- context/F5 split: listing kept as F6 (with parties/F5), shareholder part refuted in the merge.
- parties/F6 → F7: Needs decision yes, aligned with rail and air.
- New F8 (Italian tags) from parties' refuted candidate and new F9 (untagged legal forms), aligned with rail, air and merger C.
