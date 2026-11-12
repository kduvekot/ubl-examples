# LLM review: 02-OrderResponse.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/02-OrderResponse.xml`, Git blob `7b81c0b8231d36020cf1c1f9d1fabe0d729ce771` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/02#F1 · High · The accepted line carries the ID of the order's bench line
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderResponse/cac:OrderLine/cac:LineItem/cac:Item/cac:SellersItemIdentification/cbc:ID` = `LD-10443`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: The response refers to order VT-PO-26-0127 and to its change VT-OC-26-0320. Line `1` of that order is the 96 benches (item LD-10442); the side frames LD-10443 are line 2. Accepting "line 1, quantity 8, item LD-10443" contradicts the referenced order and, for a receiver matching by line ID, reads as reducing the benches to 8. The ID repeats the same problem in `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`.
- Condition: the line ID in the response identifies the added air line consistently with the order change and does not collide with a line of the original order.
- Options: (preferred) follow whatever line ID the order change gets for the added line (see the review of 01-OrderChange.xml); or, if line 2 is revised instead, respond on line 2.
- Needs decision: no

### air/02#F2 · Medium · LocaleCode holds a language code
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language, not a locale, and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/02#F3 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate of the business park is not a street and does not belong in a postal address.
- Condition: no gate in a street-name element of the postal address.
- Options: (preferred) drop it; or move it to a pickup location in documents that arrange a pickup.
- Needs decision: no

### air/02#F4 · Low · A validity period on an unconditional acceptance
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `AP`
- XPath: `/OrderResponse/cac:ValidityPeriod/cbc:EndDate` = `2026-05-13`
- Why: ValidityPeriod is "The period for which the Order Response is valid". A validity period makes sense for a counter-offer that the buyer still has to accept; code `AP` ("Accepted") concludes the change, and nothing in the flow waits for the buyer to act before 13 May. If the acceptance is meant to depend on the next day's flight, the document does not say so.
- Condition: either the response carries no validity period, or the document says what lapses at the end of it (e.g. a conditional acceptance with a matching response code and note).
- Options: (preferred) drop the ValidityPeriod; or make the condition explicit (a note that the CPT price holds only for the flight booked for 14 May).
- Needs decision: no

### air/02#F5 · Low · Signature aggregate without a signature
- XPath: `/OrderResponse/cac:Signature/cbc:ID` = `LD-SIG-26-0512`
- Why: Signature is "A signature applied to this document". The aggregate holds only an ID and the signatory: no SignatureMethod, no DigitalSignatureAttachment and no UBLExtensions with a signature the ID could point to, so the document claims a signature that a receiver cannot find or verify. Counted with lxml over `world/examples/*/*.xml`: 131 of 133 Signature aggregates hold only ID and SignatoryParty.
- Condition: either a verifiable signature (or at least the method and attachment) is present, or no Signature aggregate.
- Options: (preferred) drop it where the document needs no signature, as for an order response in the world's network; or add the signature data where the story needs a signed document.
- Needs decision: yes (a convention across many examples)

### air/02#F6 · Low · The forwarder's quotation is referenced in a response to the buyer, with nothing saying what it is
- XPath: `/OrderResponse/cac:AdditionalDocumentReference/cbc:ID` = `BF-QUOTE-AIR-26-0611`
- Why: The reference has only an ID; neither a DocumentTypeCode nor a DocumentDescription says that it is the forwarder's air-freight quotation. Under CPT the freight is the seller's cost, so the buyer, who receives this response, does nothing with the forwarder's quotation; the reference looks like the seller's internal data. No example of the flow has this ID.
- Condition: either the reference is absent, or it states what document it is and the response gives the buyer a reason to know it.
- Options: (preferred) drop it; or keep it with a DocumentType/Description if the buyer pays a share of the air freight (which would change the delivery terms).
- Needs decision: no

## Checked and consistent
- OrderReference `VT-PO-26-0127` resolves to sea/05-Order.xml; OrderChangeDocumentReference `VT-OC-26-0320` resolves to 01-OrderChange.xml; the response is issued after the change (12 May 10:46 after 11 May 07:50).
- Quantity 8, item LD-10443 and delivery terms CPT agree with the order change; NetNetWeight 76 kg and NetVolume 0.42 m³ agree with `03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetNetWeightMeasure` = `76`.
- FreightForwarderParty Bayforth Forwarding is the forwarder that receives 03-ForwardingInstructions.xml.

## Considered and refuted
- `/OrderResponse/cbc:Note` = `Accepted: the frames fly on the morning flight; the forwarder is booked.`: suspected contradiction with the later request "Please confirm the booking" in 03-ForwardingInstructions.xml — refuted: the seller booked the forwarder by phone or quotation and the instructions then ask for written confirmation; the two do not contradict.
- `/OrderResponse/cbc:AccountingCost` = `Stock for municipal projects`: suspected the buyer's accounting code in a seller's document — refuted: the definition in an Order Response is "An accounting cost code applied to the order as a whole", and echoing the buyer's code back is legitimate.
