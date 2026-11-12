# LLM review: 02-OrderResponse.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/02-OrderResponse.xml`, Git blob `7b81c0b8231d36020cf1c1f9d1fabe0d729ce771` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/02#F1 · High · The accepted line carries the ID of the order's bench line
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:Quantity` = `8`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10443`
- XPath: `/OrderResponse/cac:OrderReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: LineItem/ID is "An identifier for this line item, assigned by the buyer". The response refers to order `VT-PO-26-0127` (`sea/05-Order.xml`) and to its change `VT-OC-26-0320` (`01-OrderChange.xml`). Line 1 of the order is the 96 Serra 180 benches (item LD-10442); the side frames LD-10443 are line 2. Accepting "line 1, quantity 8, item LD-10443" contradicts the referenced order and, for a receiver matching by line ID, reads as reducing the benches to 8. The value comes from the order change, which adds the frames under the already used ID 1 (air/01#F1). Merge check: re-read both orders' lines; the response has no other link to the order lines that could disambiguate.
- Condition: the response line carries the same line identification as the added (or changed) line of the order change, and that identification does not collide with a different line of `VT-PO-26-0127`.
- Options: follow the fix of air/01#F1 (preferred there: new line ID 3) and use the same ID here; if line 2 is revised instead, respond on line 2.
- Needs decision: no
- From: broad, logistics, context

### air/02#F2 · Medium · LocaleCode holds a language code
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language, not a locale, and repeats Language/ID. The skill names "a language code in `LocaleCode`" as a Medium case. Counted over `*.xml`: 362 LocaleCode elements in 213 example files, all `en` with listID ISO 639.
- Condition: LocaleCode holds a locale from a locale list, or is absent.
- Options: (a) preferred: drop it; (b) a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### air/02#F3 · Medium · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: AdditionalStreetName is "An additional street name used to further clarify the address". A gate of the business park is not a street; it matters for vehicles, not for post, and the order response sends nothing to it. Counted over `*.xml`: 79 occurrences in 76 files.
- Condition: no gate in a street-name element of the postal address; where a gate matters, it is in the pickup or despatch location of the document that arranges it.
- Options: (a) preferred: drop it from the postal address; (b) move it to a pickup location in documents that arrange a pickup.
- Needs decision: no
- From: parties, context

### air/02#F4 · Low · A validity period on an unconditional acceptance
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- XPath: `/OrderResponse/cac:ValidityPeriod/cbc:EndDate` = `2026-05-13`
- Why: ValidityPeriod is "The period for which the Order Response is valid". A validity period makes sense for a counter-offer that lapses if the buyer does not accept it. Code `AP` (accepted) concludes the change, and nothing in the flow waits for the buyer to act before 13 May. If the acceptance is meant to depend on the cargo making the booked flight, the document does not say so.
- Condition: the response carries no validity period, or it says what lapses at the end of it (e.g. a conditional acceptance with a matching response code and note).
- Options: (a) preferred: drop the ValidityPeriod; (b) make the condition explicit (e.g. the CPT terms hold only for the booked flight).
- Needs decision: no
- From: broad, context

### air/02#F5 · Low · The forwarder's freight quotation is referenced by ID only, in a response to the buyer
- XPath: `/OrderResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-QUOTE-AIR-26-0611`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `10-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The ID reads as Bayforth Forwarding's quotation to Lumeway for the air freight, but the reference has neither DocumentTypeCode nor DocumentDescription to say so. Under CPT the freight is the seller's cost, agreed with and billed by the forwarder to the seller (`10-Invoice.xml`); the buyer, who receives this response, does nothing with that quotation. No example has this ID (counted over `*.xml`: `grep -rn --include='*.xml' BF-QUOTE world/examples`, 1 hit, this one), so the freight price it would fix cannot be checked against the invoice. The number 0611 reappears as the forwarder's pickup ID `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Pickup/cbc:ID` = `BF-PU-26-0611`.
- Condition: every document reference in the response is to a document the buyer uses under this order change, and says what it is; otherwise it is absent.
- Options: (a) preferred: drop the reference (the forwarder's price is the seller's business under CPT); (b) keep it with a DocumentTypeCode/DocumentDescription saying what it is and why the buyer gets it (e.g. a booking confirmation to track the shipment by).
- Needs decision: no
- From: broad, money, logistics, context

### air/02#F6 · Low · The acceptance gives no date for the "morning flight" or the delivery
- XPath: `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: The note promises "the morning flight" without a date, and the structured line has delivery terms but no promised delivery date, so the buyer cannot tell from the response when the frames arrive; the waybill later names the flight of 2026-05-14. (The logistics part also read "the forwarder is booked" as contradicting the forwarding instructions issued at 13:44 that ask "Please confirm the booking"; the merge refutes that part, see Refuted in the merge.)
- Condition: the response gives the promised delivery or flight date, in a structured element (e.g. the line's Delivery/PromisedDeliveryPeriod) or at least in the note.
- Options: add the promised delivery date on the line (preferred); or date the flight in the note.
- Needs decision: no
- From: logistics

### air/02#F7 · Low · English renderings of island addresses tagged en-XB here, en-XL elsewhere
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB` (`Reef Street`, Velumi Trading)
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Velumi Trading)
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Velumi Trading)
- Why: The English renderings of the island party's address carry `en-XB` (English as used in Bayvarra) here, but `en-XL` for the same text of the same party elsewhere in the flow, e.g. `01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL` and `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`. The tag follows the country of the issuer, not the address. Counted over `*.xml`: `languageID="en-XB">Port Wrenfield` in 35 files, `languageID="en-XL">Port Wrenfield` in 27. Against (broad): the tag consistently follows the English of the issuing party, which is a legitimate reading of languageID for text written by the sender. The merge cannot settle which rule the world follows (same as the wood and plastics merges for en-XB/en-XU).
- Condition: the same rendering of the same address carries the same languageID throughout the flow, chosen by a stated rule (the variety of the place, or of the writer).
- Options: (a) preferred: `en-XL` for island names everywhere, since they are the island's own English names; (b) keep the writer's variety and record that rule where the world's language conventions are written down.
- Needs decision: yes (which convention the world follows)
- From: parties; broad refuted it

### air/02#F8 · Low · The island party's legal form in one untagged rendering
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: Velumi Trading's legal form appears here once, in English, without languageID, while the island-issued examples give it in Lisavan and English, each tagged (`01-OrderChange.xml`, `04-Waybill.xml`); the address of the same party is rendered in both languages here. The parties part refuted this as a separate problem (an English-only rendering in an English document is legitimate) and folded it into F7; the merge keeps it as a separate Low finding, aligned with the wood and plastics merges ("render like the address"), because the same party's master data is described differently, independent of which tag rule is chosen.
- Condition: the legal form is rendered the same way as the party's address (both languages, tagged) in every example of the flow, or one documented rule explains the difference.
- Options: render it like the address, with `qal` and English tagged (preferred); or a documented rule.
- Needs decision: no
- From: parties (as part of its language-tag finding, refuted as a separate finding)

### air/02#F9 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- Why: RegistrationDate is "The registration date of the CompanyID." `1996-01-01` is the date of 25 different companies in three countries and registers (counted with lxml over `*.xml`), in 181 example files, while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`). It reads as a default value ("no fillers").
- Condition: each company's RegistrationDate is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) preferred: a date per company from its history; (b) drop it where no date is known; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes (company histories)
- From: parties

### air/02#F10 · Low · The buyer's contact does not fit its name or its role
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's `Purchasing` contact is a customer service officer in Sales; name, title and department contradict each other and the buyer role. Counted over `*.xml`: 52 occurrences of `Purchasing` followed by this title.
- Condition: name, job title and department describe the same function, fitting the buyer role.
- Options: (a) preferred: buyer / Purchasing; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad, parties

### air/02#F11 · Low · Signature aggregate without a signature
- XPath: `/OrderResponse/cac:Signature/cbc:ID` = `LD-SIG-26-0512`
- Why: Signature is "A signature applied to this document". The aggregate holds only an ID and the signatory: no SignatureMethod, no DigitalSignatureAttachment and no extension the ID could point to, so the document claims a signature a receiver cannot find or verify. Counted with lxml over `world/examples/*/*.xml` in the merge: 137 of 147 Signature aggregates hold nothing but ID and SignatoryParty (the context part counted 131 of 133).
- Condition: either a verifiable signature (method and attachment) is present, or there is no Signature aggregate.
- Options: (a) preferred: drop it where the document needs no signature, as for an order response in the world's network; (b) add the signature data where the story needs a signed document.
- Needs decision: yes (a convention across many examples)
- From: context

## Checked and consistent
- `VT-PO-26-0127` resolves to `sea/05-Order.xml` and `VT-OC-26-0320` to `01-OrderChange.xml` (issued 2026-05-11 07:50, before this response of 2026-05-12 10:46). Seller, buyer and accounting codes (`500`, "Stock for municipal projects") match both.
- Quantity 8 EA, item LD-10443 and line-level CPT agree with the order change (`01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:Quantity` = `8`); an acceptance (`AP`) restates no prices, which it does not need.
- Physics: NetNetWeightMeasure 76 kg for 8 frames = 9.5 kg each, the flow's own figure (`sea/10-PackingList.xml`: 96 × 38 + 12 × 9.5 = 3762 kg net); 9.5 kg of cast iron (about 7.2 t/m³, own knowledge) is about 1.3 dm³ of metal; NetVolumeMeasure 0.42 m³ = 0.0525 m³ envelope per frame, about 181 kg/m³, plausible for an open casting. Both agree with `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetNetWeightMeasure` = `76`.
- FreightForwarderParty `20411644` is Bayforth Forwarding, the forwarder of 03, 04 and 10 (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyIdentification/cbc:ID` = `20411644`).
- Lumeway Distribution is described as in the other examples (register, GLN with correct check digit and GS1 demonstration prefix 952, customs trader, Upland State tax number, Ltd, MEDIUM, 1988-10-03); Velumi Trading's identifiers, address ID `40351721` and contact agree with 01. Telephone numbers `+999 …` and `.example` domains cannot be mistaken for real ones.
- The signatory is the seller who responds.

## Considered and refuted
- `/OrderResponse/cbc:AccountingCostCode` = `500` and `/OrderResponse/cbc:AccountingCost` = `Stock for municipal projects`: the buyer's accounting code in a document issued by the seller — refuted because the definition here is "An accounting cost code applied to the order as a whole", and echoing the buyer's code lets the buyer book the response (from broad, money, context).
- `/OrderResponse/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`: a forwarder in a response to the buyer — refuted because FreightForwarderParty is "A freight forwarder or carrier" and the seller tells the buyer who handles the CPT carriage, which matters to the party that collects the goods (from parties, logistics).
- `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`: against "Please confirm the booking" in `03-ForwardingInstructions.xml`, issued three hours later — refuted because a booking made on the forwarder's quote and then confirmed against the written instructions is normal practice (from broad, context; the merge also refutes logistics' version of it, see below).
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street` tagged en-XB, refuted by broad as the issuer's English — the merge does not follow it; see F7.
- `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`, refuted by parties as a separate finding — the merge does not follow it; see F8.

## Refuted in the merge
### logistics/F3 · Low · "The forwarder is booked" before the booking is instructed; the flight has no date (booking part)
- XPath: `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`
- XPath: `/OrderResponse/cbc:IssueTime` = `10:46:00`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:IssueTime` = `13:44:00`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why (part): the response (2026-05-12 10:46) says the forwarder is booked; the forwarding instructions that book it are sent the same day at 13:44 and ask the forwarder to confirm the booking. Condition (part): the note does not state a booking that has not yet been made. Options (part): reword the note ("the forwarder has quoted; booking follows"), or move the response after the booking.
- Refuted because: "Please confirm the booking" presupposes a booking; a booking made by telephone or on the quote `BF-QUOTE-AIR-26-0611` and confirmed in writing afterwards is consistent with both texts (broad and context came to the same conclusion). The remaining part of the finding, the undated flight, stays as F6.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined.
- broad/F2, parties/F1, context/F2 → F2: combined.
- parties/F2, context/F3 → F3: combined.
- broad/F3, context/F4 → F4: combined.
- broad/F4, money/F1, logistics/F2, context/F6 → F5: combined, evidence of all four kept.
- logistics/F3 → F6: narrowed to the undated flight and delivery; the booking part moved to "Refuted in the merge".
- parties/F3 → F7: the legal-form remark taken out into F8; broad's refutation carried as the counter-argument.
- parties (Considered and refuted, legal form) → F8: made a finding, for consistency with the wood and plastics merges.
- broad/F5, parties/F5 → F10: combined; parties' options for contacts absent in this example dropped.
- context/F5 → F11: count re-made (137 of 147).

## Outside this review
- Timeline: "the frames fly on the morning flight" (said on 12 May) against the flight of 14 May 07:00 in `04-Waybill.xml` and the missed flight in `07-FulfilmentCancellation.xml`: which morning is meant is a question for the cross-flow timeline review (from broad).
