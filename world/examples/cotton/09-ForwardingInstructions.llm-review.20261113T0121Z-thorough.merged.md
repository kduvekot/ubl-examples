# LLM review: 09-ForwardingInstructions.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/09-ForwardingInstructions.xml`, Git blob `f8e65d13a83ffc42dbb2cdb364ae14e78a2f0b46` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/09#F1 · High · "Send the bill of lading to the forwarder", but the bill goes to the bank and the mill
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: the instructions tell the forwarder that the bill of lading is to go to the forwarder (Bayforth Forwarding). The bill of lading 13, issued under these instructions (it references `LTM-FI-26-0199`), sends the original by courier to the Bank of Selanu and a scanned copy to the mill, and nothing to the forwarder (verified in 13). Context listed the instruction as consistent because Bayforth is the B/L's freight forwarder party; being named on the bill is not receiving it, so the contradiction holds.
- Condition: the instruction on where the bill of lading goes and the bill's distribution list agree.
- Options: (a, preferred) the original to the forwarder in 13's distribution, as instructed (aligned with merger B's 13: the bank's role on a straight bill for an open-account sale is questioned there separately); (b) if the story is a documentary collection through the bank, change the instruction here instead (story change).
- Needs decision: no (logistics said yes; aligned with merger B, which keeps the bank question as its own Medium/yes finding in 13)
- From: logistics (F1); context (listed as consistent, not followed)

### cotton/09#F2 · Medium · The shipment ID used as the shipping-order number
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `SCG-SH-26-0200`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: `ShippingOrderID` is "Reference number to identify a Shipping Order", a document by which the shipper orders carriage (or a booking). `SCG-SH-26-0200` is the shipment's own identifier, used as `Shipment/ID` here and in 10, 11, 12, 13 and 15; its prefix is the ginnery's, while these instructions are the mill's (`LTM-FI-…`, signed by the mill). No shipping order with this number exists in the flow. An identifier of one kind is used as another.
- Condition: `ShippingOrderID`, if present, identifies a shipping order (or booking) distinct from the shipment ID, issued by the party that places it; otherwise it is absent.
- Options: (a, preferred) drop `ShippingOrderID`; (b) give it the forwarder's or carrier's booking number if the story has one, and use it where 13 refers to the booking.
- Needs decision: no
- From: broad (F2), logistics (F3), context (F2)

### cotton/09#F3 · Medium · Language code in `LocaleCode`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (`ISO 639`) is a language code repeating `Language/ID`. 362 occurrences in 213 files. Same as 02#F3.
- Condition: every `Language/LocaleCode` holds a locale from a list that defines locales, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F4), parties (F1)

### cotton/09#F4 · Medium · Forwarding instructions that do not say what to carry, from where, to where or when
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the bales to Bayvarra.`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: Forwarding Instructions is "A document issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein". The shipment has only an ID, a gross weight and a consignment with a consignee: no goods item (no description, commodity code or number of bales), no transport handling unit or container (the goods go in one 40-foot container, 12 and 17), no place of loading or discharge (port of Selanu, the FOB point of 08), no delivery or pickup place, no transport mode and no requested date. The forwarder cannot book the carriage ("Please confirm the booking") from this document; everything is only implied by the order 08 and the description "bales to Bayvarra". The bill of lading 13 and the export declaration 11 describe goods, bales and ports; the instructions that start that chain do not. Information the document's purpose depends on is missing (Medium).
- Condition: the document states the goods (description, bale count, gross weight), the equipment requested, the places (port of loading Selanu, port of discharge Lumeport, or pickup and delivery places) and the requested timing, consistently with 12, 13 and 17.
- Options: (a, preferred) add a goods item (27 bales of cotton lint, HS 5201, 6190.29 kg), an equipment request for one 40-foot container, a main-carriage shipment stage with the loading and discharge ports, and a requested loading date; (b) if the instructions only confirm a booking made otherwise, say so, refer to that booking or packing document, and keep at least goods and ports.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F1)

### cotton/09#F5 · Medium · Shipment gross weight without the container
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment." 6190.29 kg is the goods with their bale packaging (6 129 kg lint + 61.29 kg wrapping, the goods-item gross weight in 10); the same shipment `SCG-SH-26-0200` moves in a container of 3 750 kg tare, and 12 gives 6 190.29 + 3 750 = 9 940.29 kg (recomputed). Shipping practice often reports cargo gross weight without the container; under semantic conformance the definition applies. Logistics rated it Low and noted the container may not be known yet when the instructions are issued; that argues for giving the cargo weight in a goods item, not for putting it on the shipment. Medium, aligned with merger B of this flow (the shipment is containerised in 12, so "no equipment, equal may be correct" of earlier flows does not hold).
- Condition: the shipment's gross weight includes the transport equipment, or the cargo gross weight is carried where the definition fits (goods item or consignment).
- Options: (a, preferred) move 6190.29 kg to a goods item (see F4) and leave the shipment gross weight out until the container is known; (b) state 9 940.29 kg.
- Needs decision: no
- From: broad (F3), logistics (F4, Low)

### cotton/09#F6 · Low · DocumentStatusCode "NoStatus" states nothing
- XPath: `/ForwardingInstructions/cbc:DocumentStatusCode` = `NoStatus`
- Why: "No status on document" gives no status (IND5); same as 03#F1 and the earlier flows' merges (26 files carry a `NoStatus` `DocumentStatusCode`, `grep -rl --include='*.xml' 'DocumentStatusCode[^>]*>NoStatus<'`).
- Condition: no `DocumentStatusCode`, or one that states a status the story has.
- Options: (a, preferred) leave it out.
- Needs decision: no
- From: context (F4, status part)

### cotton/09#F7 · Low · Ad valorem indicator and declared carriage value, with no ad valorem duty or charge anywhere
- XPath: `/ForwardingInstructions/cbc:AdValoremIndicator` = `true`
- XPath: `/ForwardingInstructions/cbc:DeclaredCarriageValueAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `2950`
- Why: `AdValoremIndicator` is "A term used in commerce in reference to certain duties, called ad valorem duties, which are levied on commodities at certain rates per centum on their value". Next to a declared carriage value ("declared … solely for the purpose of varying the carrier's level of liability") it reads in the shipping sense of ad valorem freight, which is not the UBL definition (context). Read either way, nothing in the flow is levied per centum on the value: the forwarder's freight is a flat 2 950 XBL per container (17), and the import declaration 15 only says duties were paid, not that they are ad valorem (money). Broad listed the pair as consistent (higher liability); that is the shipping reading, which semantic conformance does not follow. The same pair is in 13 (merger B: Low/yes).
- Condition: `AdValoremIndicator` is present only to state whether ad valorem duties apply, and the story agrees; a declared carriage value only if the mill wants the higher liability and the charge for it appears where it is billed.
- Options: (a, preferred) drop the indicator and let `DeclaredCarriageValueAmount` alone express the higher liability (and decide whether the mill declares a value at all); (b) keep it if Bayvarra's duty on lint is ad valorem and let 15 show it, or add the value-based surcharge to 17.
- Needs decision: yes
- From: money (F1), context (F3); broad (listed as consistent, not followed)

### cotton/09#F8 · Low · The ginnery's English address tagged as Bayvarran English
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: as 02#F7: `en-XB` here, `en-XL` in the ginnery's own documents for the same renderings. Both parts said no; set to yes, as in 02, 07, 08 (aligned with earlier flows and merger B).
- Condition: the same rendering carries the same `languageID` in every example, or the issuer rule is recorded.
- Options: (a, preferred) `en-XL`; (b) record the issuer rule.
- Needs decision: yes
- From: broad (F8), parties (F3, address part)

### cotton/09#F9 · Low · The ginnery's legal form in one untagged English rendering
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: in the ginnery's own documents its legal form is given in Lisavan and English with `languageID`; here only the untagged English one. Split from F8, as 02#F8.
- Condition: the ginnery's legal form carries the same renderings and `languageID`s in every example.
- Options: (a, preferred) both renderings with their tags, as in 01.
- Needs decision: no
- From: parties (F3, legal-form part)

### cotton/09#F10 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/ForwardingInstructions/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'`); reads as a default (IND5) unless the story has a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) dates from the companies' histories; (b) drop them; (c) record a register-wide date.
- Needs decision: yes
- From: parties (F5)

### cotton/09#F11 · Low · Tax registrations of forwarder and consignee in a document that does nothing with tax
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: forwarding instructions bill nothing and declare nothing for tax; the Coastal State sales-tax registrations of Bayforth and of the mill are master data with no use here (section 4.8). (Parties found the customs-trader numbers useful here, for the export and import filings; that is accepted.)
- Condition: no party tax registration unless the instructions do something with it.
- Options: (a, preferred) drop both `PartyTaxScheme` blocks.
- Needs decision: no
- From: money (F3)

### cotton/09#F12 · Low · The consignee's contact: "Purchasing" in Sales, not goods receiving
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: here the mill is the consignee, the party that receives the bales at Lumeport; a consignee's contact receives goods (goods-in, import), not purchasing, and name, title and department contradict each other (52 files with this combination, parties).
- Condition: the consignee's contact is a receiving or import function whose name, title and department agree.
- Options: (a, preferred) a goods-in / import contact of the mill; (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F7), parties (F2)

### cotton/09#F13 · Low · An exchange rate no amount uses
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/ForwardingInstructions/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: `ExchangeRate` is "Information about the rate of exchange (conversion) between two currencies". The only amount, the declared carriage value, is in coral; nothing is in Lume. The rate agrees with 04 and with the import value in 15 (6 055.452 / 0.4 = 15 138.63 XBL, recomputed), so it is correct but converts nothing here (IND5). The same rate is in 13 (merger B: Low/no).
- Condition: the exchange rate is present only if the document states an amount the receiver must convert with it.
- Options: (a, preferred) drop it; (b) state the declared value also in XBL (the forwarder's and carrier's currency) and keep the rate.
- Needs decision: no
- From: broad (F5), money (F2), context (F4, exchange-rate part)

### cotton/09#F14 · Low · The addressee listed again as distribution recipient
- XPath: `/ForwardingInstructions/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `DocumentDistribution` is "A list of interested parties to whom this document is distributed". Forwarding instructions are issued to the forwarder, already the freight forwarder party; the only entry names it again (IND5).
- Condition: `DocumentDistribution` lists only parties other than the addressee that receive a copy, or is absent.
- Options: (a, preferred) drop it; (b) distribute a copy to the ginnery (consignor), which hands over the goods.
- Needs decision: no
- From: broad (F6), parties (F4), context (F4, distribution part)

### cotton/09#F15 · Low · Signature ID that looks like the example number
- XPath: `/ForwardingInstructions/cac:Signature/cbc:ID` = `LTM-SIG-FI-09`
- Why: `Signature/ID` is the signature's identifier; `FI-09` reads as "forwarding instructions, example 09" rather than the mill's own numbering (the mill's other signatures are `LT-SIG-26-0202` in 02 and `LT-SIG-26-0222` in 07). It may be the mill's ninth FI signature, so the reading is uncertain. No part raised it; added by the merge for alignment with the road merges and merger B (signature IDs built from flow name or example number: Low/no).
- Condition: the signature ID follows the signer's own numbering, not the example's.
- Options: (a, preferred) a number in the mill's scheme (e.g. `LT-SIG-26-…`).
- Needs decision: no
- From: merge

## Checked and consistent
- Gross weight (recomputed): 27 bales × 227 kg = 6 129 kg; 6 190.29 − 6 129 = 61.29 kg packaging, 2.27 kg per bale, 1 % of the lint, plausible for bale wrap and ties (own knowledge).
- `DocumentReference` `LTM-PO-26-0198` resolves to the order 08; `DeclaredCarriageValueAmount` 6 055.452 XLC equals the order and invoice value (08, 16).
- Under FOB (08) the buyer arranges the main carriage, so the mill instructing its own forwarder, with the ginnery as consignor and the mill as consignee, fits; the mill signs (`20412603`).
- Consignment `LTM-CS-26-0201` is the same in 11, 13 and 17; shipment `SCG-SH-26-0200` in 10, 11, 12, 13 and 15.
- `ToOrderIndicator` false agrees with 13, a straight bill naming the mill as consignee.
- Bayforth's full description is identical in 09, 13 and 17; the customs-trader numbers of consignor and consignee have a use here (export and import filings) (parties).

## Considered and refuted
- `/ForwardingInstructions/cac:ConsignorParty`: consignor without a document role for the mill — refuted: the mill signs as the instructing party; the consignor is the ginnery that hands over the goods FOB. (from broad)
- `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`: free text where a structured element exists — refuted: no UBL element says where to send the bill; its content is F1. (from broad)
- `/ForwardingInstructions/cac:FreightForwarderParty/cac:Contact/cbc:Name` = `Export desk`: a Bayvarran forwarder acting for an importer — refuted: the instructions concern the booking and departure from Selanu, which a forwarder handles at its export desk. (from parties)
- No party for the issuer of the instructions — refuted: Forwarding Instructions has no issuer role; the mill appears as consignee and signatory. (from parties)
- `/ForwardingInstructions/cbc:ToOrderIndicator` = `false`: a filler / against 13 — refuted: it asks for a straight bill naming the consignee, which 13 is. (from logistics, context)

## Changed in the merge
- logistics/F1 (High/yes) → F1: High/no, aligned with merger B (13); context's "consistent" reading answered.
- broad/F2, logistics/F3, context/F2 → F2.
- broad/F4 + parties/F1 → F3.
- broad/F1, logistics/F2, context/F1 → F4.
- broad/F3 (Medium) + logistics/F4 (Low) → F5: Medium, aligned with merger B.
- context/F4 split into F6 (NoStatus), F13 (exchange rate, with broad/F5 and money/F2), F14 (distribution, with broad/F6 and parties/F4).
- money/F1 + context/F3 → F7: Low/yes (aligned with merger B for 13); broad's "consistent" listing not followed.
- broad/F8 + parties/F3 → F8 and F9: legal form split off (Low/no); F8 needs decision changed from no to yes.
- broad/F7 + parties/F2 → F12.
- F15: added by the merge (signature ID).
