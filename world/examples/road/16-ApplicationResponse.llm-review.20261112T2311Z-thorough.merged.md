# LLM review: 16-ApplicationResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/16-ApplicationResponse.xml`, Git blob `1e7f911b472f7aea92ee35fb380bd4e0c2647589` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
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

### road/16#F1 · High · Three-way match passed before the goods arrived and before any receipt advice
- XPath: `/ApplicationResponse/cbc:ResponseDate` = `2026-03-25`
- XPath: `/ApplicationResponse/cbc:ResponseTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveTime` = `06:12:00`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.`
- XPath: `/ApplicationResponse/cbc:IssueTime` = `12:55:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:Shipment/cac:Delivery/cbc:ActualDeliveryTime` = `09:40:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00`
- XPath: `11-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[1]/cbc:ShortQuantity` = `1`
- XPath: `13-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueDate` = `2026-03-26`
- Why: `ResponseDate`/`ResponseTime` are "The date/time on which the information in the response was created", `EffectiveTime` "The time at which this response is valid". A three-way match compares invoice, order and goods receipt. At 06:12 on 2026-03-25 the goods had not arrived (delivered 09:40), and no receipt advice existed: the first is issued at 15:40 and reports a bench short, so a match against it would have failed on line 1; the corrected one follows only on 2026-03-26 10:48. Refutation tried in the merge: the match could have been run against the despatch advice instead of a receipt, but that is a two-way match plus an advice of despatch, not "three-way"; and even the document's own issue time 12:55 precedes the first receipt advice. The status contradicts the documents it depends on (High).
- Condition: the response's creation and effective times, and its issue time, lie after the receipt it was matched against (the corrected receipt advice, 2026-03-26 10:48), or the status does not claim a three-way match.
- Options: (a, preferred: all three parts) date the response after the corrected receipt advice, e.g. 2026-03-26 afternoon, and keep "Three-way match passed."; (b) keep the date and describe a two-way match against the order, which changes the note.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1); money listed it under "Outside this review"

### road/16#F2 · Medium · Language code in LocaleCode
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats `Language/ID` and names no locale (section 6: Medium). Recounted: 364 occurrences in 213 files; the parts said 362.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales named in its listID.
- Options: (a, preferred: broad, parties) drop `LocaleCode`; (b, context's preference) `en-XB` with a locale list as listID.
- Needs decision: no (parties said yes; encoding only, as in all earlier flows)
- From: broad (F2), parties (F1), context (F3)

### road/16#F3 · Medium · Gate number in AdditionalStreetName of Lumeway's postal address
- XPath: `/ApplicationResponse/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is an entrance for vehicles, not a street name; an invoice response has no use for it. Recounted: 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a, preferred) drop the gate from the party address; (b) keep it only in delivery addresses, in a location description.
- Needs decision: no
- From: broad (F3), parties (F2)

### road/16#F4 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address in the same document uses `CountrySubentity` (`/ApplicationResponse/cac:SenderParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Recounted: 219 occurrences in 104 files.
- Condition: the Urvanian province is in `CountrySubentity` (with a code where a list exists); `Region` is absent or holds a real region.
- Options: (a, preferred) move it to `CountrySubentity`, as Bayvarra does; (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules.
- Needs decision: no
- From: broad (F4), parties (F3), context (F2)

### road/16#F5 · Low · Signature with only an ID derived from the document type
- XPath: `/ApplicationResponse/cac:Signature/cbc:ID` = `LD-SIG-26-AR`
- XPath: `/ApplicationResponse/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: `Signature/ID` is "An identifier for this signature". `LD-SIG-26-AR` ends in `AR`, the abbreviation of the document type's name (ApplicationResponse), not a number in Lumeway's own scheme (it occurs in this one file only). The signature also carries nothing but ID and signer: no method, value or attachment says how the response is signed. The air and utilities merges treated signatures of this kind as a convention needing a decision (137 of 147 `Signature` aggregates in the examples hold only ID and signatory, counted there with lxml); the road merges a and b and context treat the ID as encoding (no decision). Aligned with road a and b: no.
- Condition: the signature ID follows the signer's own numbering, and the signature says how the document is signed, or the signature is absent.
- Options: (a, preferred) number the signature in Lumeway's scheme (e.g. after the response ID) and add the method or attachment; (b, air's preference for signatures that add nothing) drop the signature.
- Needs decision: no
- From: context (F5, signature part)

### road/16#F6 · Low · Contacts that do not fit an invoice response
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: the response to an invoice comes from the buyer's accounts payable, which matched it, and goes to the seller's accounts receivable; Lumeway's customer service in Sales handles its own customers, Valdara's order desk handles orders. Each party carries one fixed contact in every role of the flow.
- Condition: the contacts are the parties' invoice-handling functions, or absent.
- Options: (a, preferred) accounts payable / accounts receivable contacts; (b) drop the contacts or their job titles and departments.
- Needs decision: no
- From: broad (F5), parties (F4), context (F4)

### road/16#F7 · Low · Italian street name tagged as English, with the issuer's region subtag
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: the rendering carries `languageID` `en-XB` but is Italian text, and the same Valdara street is tagged `en-XU` in the documents Valdara issues (`15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`). The parties part refuted it: English keeps foreign street names unchanged, and the region subtag follows the sender. Against that: `languageID` names the language of the content, and the same party is tagged differently by issuer. The merge cannot settle the convention; aligned with the utilities, rail and packaging merges (Low, decision). 217 such street renderings in 102 files.
- Condition: the world has one stated rule for the language tag of Urvanian names rendered in English, and every rendering of the same address follows it.
- Options: (a, preferred) the party's own variety (en-XU) whoever sends the document, documented; (b) document that the tag follows the issuer, as now.
- Needs decision: yes
- From: merge (from the parties' "Considered and refuted")

### road/16#F8 · Low · Valdara's legal form in one untagged rendering
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: in the documents Valdara issues its legal form comes in two tagged renderings (`qau` and `en-XU`, e.g. `15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`); here there is one, without `languageID`, while its address is rendered in both languages. No part raised it; added by the merge for consistency with the rail, air, wood and plastics merges.
- Condition: the legal form is rendered as the address is (both renderings, tagged), or the difference is a stated convention.
- Options: (a, preferred) both renderings with `languageID`; (b) one rendering, tagged.
- Needs decision: no
- From: merge

### road/16#F9 · Low · Party master data the response does nothing with
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/ApplicationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: section 4.8: the seller's stock-exchange listing and its logistics provider play no part in accepting an invoice.
- Condition: every optional party aggregate present has a reason in the response's purpose.
- Options: (a, preferred) leave listing and service provider out of the response; (b) state a reason if the story gives one.
- Needs decision: no
- From: parties (F5), context (F5, party part)

### road/16#F10 · Low · Invoice referenced with only an ID
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`
- Why: the response's whole purpose is the referenced document, yet the reference carries no `DocumentTypeCode`, type text or issue date; it does not say it is an invoice (the remittance advice of the same flow does, with a document type code and issue date). The `CustomizationID` (invoice response) implies it, so Low.
- Condition: the reference states the kind of document it refers to (type code or text), and preferably its issue date.
- Options: (a, preferred) add `DocumentTypeCode` from the world's document type list, as `17-RemittanceAdvice.xml` does; (b) add `DocumentType` as text.
- Needs decision: no
- From: broad (F6)

### road/16#F11 · Low · Issuer and recipient of the responded-to document: reversed or redundant
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:IssuerParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/ApplicationResponse/cac:DocumentResponse/cac:RecipientParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: under `DocumentResponse` ("A response to a document"), `IssuerParty` is "The Party who issues this Document" and `RecipientParty` "The Party who is the intended recipient of this Document". If "this Document" is the referenced invoice VI-INV-26-0166, its issuer is Valdara and its recipient Lumeway, so the two are reversed. If it is the response itself, both only repeat `SenderParty` and `ReceiverParty` and add nothing (IND5). Context read them the second way and checked them as consistent. The definition does not settle which reading is meant.
- Condition: `IssuerParty`/`RecipientParty` name the issuer and recipient of the referenced invoice (Valdara, Lumeway), or are absent.
- Options: (a, preferred: parties) drop both, since the invoice identifies its parties and sender/receiver identify the response's; (b, broad) swap them, if the reading "the referenced document" is adopted.
- Needs decision: yes
- From: broad (F7), parties (F6); context read them as the response's parties (its "Checked and consistent")

## Checked and consistent
- `DocumentReference` VI-INV-26-0166 resolves to `15-Invoice.xml`; line 2 responded to exists there and is the side-frame line substituted in `02-OrderResponse.xml`.
- `ResponseCode` `AP` (accepted) on the document and on line 2, `ConditionCode` `MATCHED` and the notes agree with each other.
- Money: the accepted invoice's quantities and prices agree with the order (96 × 49 900 + 12 × 5 980 = 4 862 160 = `15-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160`), and the remittance pays exactly that, so "accepted for payment" is what the flow then does.
- Sender and signatory Lumeway, receiver Valdara: the buyer answers the seller's invoice; `CustomizationID` for an invoice response fits.
- Check digits (`check_ids.py`): GLN `9520610900008` and ISIN `XU0001042501` are correct.

## Considered and refuted
- `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.` while the corrected receipt shows 13 side frames against 12 ordered and invoiced (`13-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `13`) — refuted because a three-way match checks that the invoiced quantity is ordered and received; 12 invoiced against 12 ordered and 13 received passes. The unsettled extra unit is road/13#F9 (from money).
- `/ApplicationResponse/cbc:IssueTime` = `12:55:00` later than the response time 06:12 — refuted because the definitions allow the information to be created before the document is issued; the problem is the time itself (F1) (from context).
- `/ApplicationResponse/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]`: Italian street name tagged as English — refuted by parties; not followed, made F7.
- `/ApplicationResponse/cac:SenderParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: a GLN that could be real — refuted because prefix 952 is reserved by GS1 for examples and the check digit is correct (from parties).
- `/ApplicationResponse/cac:SenderParty/cac:Contact/cbc:Telephone`: telephone numbers could be real — refuted because +999 is reserved in ITU-T E.164 (from parties).
- `/ApplicationResponse/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number — refuted because the definition does not say who assigns the identifier (from parties).

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; the issue time 12:55 (before the first receipt advice) added to the condition. Money's "Outside this review" entry absorbed: the contradiction is with referenced examples, hence a finding of this review.
- broad/F2, parties/F1, context/F3 → F2: parties' "Needs decision: yes" set to no; count corrected to 364.
- context/F5 split: signature → F5, party data → F9 (with parties/F5), as in the utilities merges; F5 keeps context's "no", aligned with road merges a and b (air and utilities said yes for empty signatures; noted in Why).
- broad/F5, parties/F4, context/F4 → F6: combined.
- broad/F7, parties/F6 → F11: combined; preferred option is parties' (drop), broad's swap kept as (b).
- F7 and F8 added by the merge (F7 from a refutation of the parties part not followed).

## Outside this review
- The note "Accepted for payment; line 2 matched the substituted casting." has nothing to match against in the goods documents and the invoice, which identify line 2 only as VI-C180 (from logistics); these are road/13#F18 and road/15#F13, and the same gap in `04-DespatchAdvice.xml` belongs to that example's review.
