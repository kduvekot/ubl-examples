# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
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

### cotton/13#F1 · High · The original bill goes to a bank, while the forwarding instructions ask for it to go to the forwarder
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- XPath: `/BillOfLading/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/BillOfLading/cac:DocumentReference/cbc:ID` = `LTM-FI-26-0199`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- Why: the bill refers to the forwarding instructions 09, which instruct "Send the bill of lading to the forwarder." `DocumentDistribution` is "A list of interested parties to whom this document is distributed": the original goes by courier to the Bank of Selanu and a scanned copy to the mill; Bayforth Forwarding, named in this same bill, receives nothing. The bill does not follow the instruction it cites, and nothing explains why. Refutation tried: the forwarder might pass the original on to a bank itself; but then the forwarder would be the recipient here.
- Condition: the distribution of the original bill agrees with the forwarding instructions, or the instruction and the story say why the original goes elsewhere.
- Options: (a, preferred) the original to Bayforth Forwarding as instructed (clearing at Lumeport), the copy to the mill if wanted; (b) if the original must go to a bank (documentary collection, F3), change the instruction in 09 and the payment terms of 16 to match.
- Needs decision: no (the encoding follows the instruction under option a; whether a bank is involved at all is F3)
- From: parties (F1), logistics (F1), context (F1), broad (F6, Low)

### cotton/13#F2 · Medium · A "shipped on board" bill without goods, container, vessel, ports or on-board date
- XPath: `/BillOfLading/cbc:Description` = `Shipped on board.`
- XPath: `/BillOfLading/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- Why: a Bill of Lading "evidences a contract of carriage by sea and the acceptance of responsibility for the goods by the carrier, by which the carrier undertakes to deliver the goods against surrender of the document" (UBL definition). A shipped bill states the goods (marks, number and kind of packages, description, weight), the vessel, the ports of loading and discharge and the date of shipment on board (Hague-Visby Art. III(3) and III(7), own knowledge). This bill has only a shipment ID, a gross weight and a consignment with consignee and mortgage holder: no goods item (27 bales of cotton lint, HS 5201), no container (TWLU4123110, 12), no vessel or voyage (14 reports the vessel Tidewell Reef), no ports (Selanu XLSEL, Lumeport), no on-board date. The consignee could not identify its goods with it, and the bill cannot be linked to the report 14.
- Condition: the bill states the goods with description, bale count and gross weight, the container, the vessel and voyage, the ports of loading and discharge and the date shipped on board, consistently with 10, 11, 12 and 14.
- Options: (a, preferred) add a goods item (27 bales, 6190.29 kg), a transport handling unit with the container (and seal) of 12, and a main-carriage shipment stage with the vessel and voyage of 14, the ports and the loading date, on the map's sea route Selanu–Lumeport.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F3)

### cotton/13#F3 · Medium · The Bank of Selanu as mortgage holder and recipient of the original, with no financing or collection in the flow
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ToOrderIndicator` = `false`
- XPath: `16-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`
- Why: `MortgageHolderParty` is "The Party who holds the mortgage for this Consignment." A bank holding a security interest in the bales and receiving the original bill would fit a documentary collection or credit, or a pre-export loan secured on the goods; nothing in the flow has either: the ginnery invoices the mill on open account (credit transfer, 45 days net, 16, paid in 18), and the instructions ask for a straight bill to the mill (`ToOrderIndicator` false), under which the consignee can usually take delivery without the original and a bank holding it gains no control of the goods (own knowledge of trade finance). The bank is also the ginnery's own bank (payee account of 16), which would make the ginnery's goods pledged to it, which the story does not say. Not High: a pre-export loan not shown elsewhere would not contradict any document, so the role lacks a basis rather than contradicting one (broad had Low).
- Condition: a mortgage holder and a bank recipient of the original appear only if the flow shows the financing or collection behind them, consistently in the forwarding instructions, the bill's transferability, the invoice and the payment.
- Options: (a, preferred) drop the mortgage holder and the bank as recipient (with F1 a); (b) give the ginnery a crop loan or a documentary collection through the Bank of Selanu, with an order bill and matching terms in 09, 16 and 18.
- Needs decision: yes
- From: parties (F2), context (F2), broad (F4, Low), logistics (inside F1)

### cotton/13#F4 · Medium · Shipment gross weight without the container
- XPath: `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `6190.29`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `9940.29`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The carrier received, the day before, the VGM of 9940.29 kg for this shipment (12: 6190.29 kg cargo + 3750 kg tare); 6190.29 kg is the cargo without the container. On bills of lading the cargo gross weight is customarily given without the container; under the agreed rule of semantic conformance the definition applies. Medium, as in 11 (logistics had Low): the value misfits the definition and 12's description of the same shipment; not High, because this bill names no equipment.
- Condition: the shipment gross weight includes the container, or the cargo weight is given at goods-item level (F2) and the shipment gross weight is dropped or corrected.
- Options: (a, preferred) 6190.29 kg as goods-item gross weight (F2) and no shipment gross weight; (b) 9940.29 kg at shipment level.
- Needs decision: no
- From: broad (F2), logistics (F4)

### cotton/13#F5 · Medium · Language code in `LocaleCode`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F3), parties (F3)

### cotton/13#F6 · Low · `AdValoremIndicator` with a declared carriage value, but no duty and a flat freight
- XPath: `/BillOfLading/cbc:AdValoremIndicator` = `true`
- XPath: `/BillOfLading/cbc:DeclaredCarriageValueAmount` = `6055.452`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `2950`
- Why: `AdValoremIndicator` is, by its UBL definition, "A term used in commerce in reference to certain duties, called ad valorem duties, which are levied on commodities at certain rates per centum on their value"; here it stands next to `DeclaredCarriageValueAmount` ("Value declared by the shipper or his agent solely for the purpose of varying the carrier's level of liability …") in the shipping sense of ad valorem freight (context). And a carrier that accepts higher liability on a declared value charges for it on that value (own knowledge), but the sea freight billed for this container is a flat 2950.00 XBL with no value-based part (17), and no duty rate appears in the flow (money). Whether the indicator states a duty fact of the world, or the mill wanted higher liability, is part of the story. The same pair is in 09.
- Condition: `AdValoremIndicator` is present only to state whether ad valorem duties apply; a declared carriage value only if the higher liability is wanted, and then its charge appears where the freight is billed.
- Options: (a, preferred) drop the indicator and the declared value; (b) keep the declared value and add the ad valorem charge to 17, without the indicator.
- Needs decision: yes
- From: money (F1), context (F4, indicator part)

### cotton/13#F7 · Low · Freight terms only as a note, and "freight collect" while the forwarder invoices the sea freight
- XPath: `/BillOfLading/cbc:Note` = `Freight collect.`
- XPath: `17-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- Why: a bill of lading states "the details of the transportation, charges, and terms and conditions under which the transportation service is provided" (UBL definition); who pays the freight is given only as free text and the freight itself not at all, although the consignment has structures for both (freight charge, payment terms) (money). "Freight collect" means the carrier collects the freight at destination from the consignee side; the forwarder's invoice 17, which refers to this bill, charges the mill for the same sea freight "booked with the ocean carrier" (logistics). Money refuted the contradiction: the forwarder, in Lumeport, can pay the collect freight at destination for the mill and recharge it; both say the mill's side pays, as FOB (08) requires. The documents do not say which way applies.
- Condition: the bill states in structured form which freight is due and whether it is prepaid or collect (or "as arranged"), and the bill and 17 describe one way in which the mill pays the sea freight.
- Options: (a, preferred) the sea freight as the consignment's freight charge with collect terms, and 17 saying that the forwarder pays it at destination and recharges it; (b) mark the bill freight prepaid by the forwarder.
- Needs decision: yes (who pays the carrier is part of the story)
- From: money (F2), logistics (F3); money's refutation of the collect/forwarder contradiction carried

### cotton/13#F8 · Low · Exchange rate with nothing to convert
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/BillOfLading/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: the only amount in the bill is the declared value in XLC; nothing is stated in Lume, so the XBL→XLC rate converts nothing (no fillers). The rate itself agrees with 04, 09 and 15.
- Condition: an exchange rate is present only if the bill states an amount that must be converted.
- Options: (a, preferred) drop it; (b) state an amount in both currencies.
- Needs decision: no
- From: broad (F5), money (F3), context (F4, rate part)

### cotton/13#F9 · Low · Tax registrations and share capital copied into the bill of lading
- XPath: `/BillOfLading/cac:CarrierParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/BillOfLading/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1234932`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1237809`
- Why: the bill of lading bills no tax; the Coastal State sales-tax registrations of carrier, forwarder and consignee and the carrier's share capital have no use in the contract of carriage (section 4.8, master data copied in).
- Condition: no party tax registration or share capital unless the bill does something with it.
- Options: (a, preferred) drop the three `PartyTaxScheme` blocks and the carrier's `CorporateStockAmount` and `FullyPaidSharesIndicator`.
- Needs decision: no
- From: money (F4)

### cotton/13#F10 · Low · The consignee's contact: Purchasing, Customer service officer, Sales
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: the consignee of a bill of lading is the party the carrier notifies and releases the container to; a purchasing contact does not fit, and name (buying) and job title and department (selling) contradict each other. The combination is in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>' | xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: a receiving (goods-in / import) contact whose name, job title and department agree.
- Options: (a, preferred) the mill's goods-in or import desk; (b) drop JobTitle and Department.
- Needs decision: no
- From: broad (F7), parties (F4)

### cotton/13#F11 · Low · The ginnery's Lisavan address parts tagged as Bayvarran English
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road`
- Why: these renderings carry `languageID` `en-XB` here, `en-XL` in the documents the ginnery or other Lisavan parties issue (01, 03-06, 10-12, 16). Counted over *.xml (`grep -o 'languageID="[^"]*">Gin Yard Road'` per file): en-XB in 02, 07, 08, 09, 13, 15 and 18, all issued by Bayvarran parties; en-XL in the other nine. Parties: `languageID` describes the text, so the names of a Lisavan street and town are Lisavan English whoever sends the document. The pattern is consistent with a convention "the tag follows the issuer's English", which earlier flows could not settle either.
- Condition: one rule for the tags of the same party's renderings, applied in every example and documented.
- Options: (a, preferred) the ginnery's own renderings and tags (en-XL) everywhere, because `languageID` describes the text; (b) if tags follow the issuer, record the rule.
- Needs decision: yes
- From: broad (F8), parties (F5, address part)

### cotton/13#F12 · Low · The ginnery's legal form in one untagged rendering
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: elsewhere the ginnery's legal form is given in Lisavan and in English with language tags; here the Lisavan rendering is dropped and the English one has no `languageID`, while the Lisavan street and city names are kept. The same party is described in two ways in the flow.
- Condition: the ginnery's legal form carries the same renderings and tags in every example.
- Options: (a, preferred) both renderings with their tags, as in 01.
- Needs decision: no
- From: parties (F5, legal-form part)

### cotton/13#F13 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." Ginnery, forwarder and mill, in two registers, share 1 January 1996, which occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from each company's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F6)

### cotton/13#F14 · Low · Signature ID built from the flow name
- XPath: `/BillOfLading/cac:Signature/cbc:ID` = `TWL-SIG-BL-cotton`
- Why: the carrier's signature identifier ends in the name of the example flow ("cotton"), which exists in the repository, not in the world; a carrier numbers its signatures in its own series. No part raised it; added by the merge for alignment with earlier flows and with cotton/11#F14. The pattern is in 8 example files (`grep -rl --include='*.xml' 'SIG-[A-Z]*-\(cotton\|road\|rail\|sea\|air\)<'`).
- Condition: the signature ID is an identifier of the signer's own numbering, with no flow name in it.
- Options: (a, preferred) an ID in the carrier's signature series.
- Needs decision: no
- From: merge

## Checked and consistent
- Issued 2026-03-02 09:37, after the export declaration (11, 2026-03-01 13:33) and the VGM (12, 2026-03-01 15:19), before the pre-arrival report (14, 2026-03-03) and the import declaration (15, 2026-03-06).
- Consignor (ginnery), consignee (mill), carrier (Tidewell Ocean Lines, receiver of 12, reporter in 14, signatory) and forwarder (Bayforth) agree with 09, 10 and 12; their full descriptions match 09, 11, 12, 14 and 17 block by block (parties).
- Shipment SCG-SH-26-0200 and consignment LTM-CS-26-0201 agree with 09, 11 and 17; 15 and 17 reference this bill as TOL-BL-26-0206; `DocumentReference` LTM-FI-26-0199 resolves to 09.
- `DeclaredCarriageValueAmount` 6055.452 XLC = the order and invoice value (08, 16) and the value declared in 09.
- "Freight collect" agrees with FOB Port of Selanu (08): the buyer's side pays the main carriage, and 17 bills it to the mill.
- The scanned copy to the mill fits its role as consignee and buyer.

## Considered and refuted
- `/BillOfLading/cbc:DocumentStatusCode` = `Confirmed`: a status on a first issue suspected as a filler — refuted because "Document has been confirmed" states that the carrier confirmed the booking it was issued against, a real status (from broad, context).
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyIdentification/cbc:ID` = `IC41996`: the same bank is identified by a BIC-like ID in the payment means of other examples — refuted, a companies-register identifier and a financial-institution identifier are different kinds, both legitimate (from parties).
- `/BillOfLading/cbc:Note` = `Freight collect.` against 17: collect freight paid through the forwarder — refuted by money (the forwarder can pay at destination and recharge); logistics kept it, so it is part of F7 with both arguments.

## Changed in the merge
- parties/F1, logistics/F1, context/F1 (High) + broad/F6 (Low) → F1: High kept; "Needs decision" set to no (parties' value; logistics and context said yes), because the bank's role, the story question, is decided in F3; F1 under option (a) is an encoding fix.
- broad/F4 (Low) + parties/F2, context/F2 (Medium) → F3: Medium, yes (two of three parts).
- logistics/F4 (Low) + broad/F2 (Medium) → F4: Medium, aligned with cotton/11#F1.
- money/F1 + context/F4 indicator part → F6: one finding with both arguments; "Needs decision: yes" as both parts said.
- money/F2 + logistics/F3 → F7: grouped (both concern how freight terms and freight are stated); yes, from logistics.
- broad/F5, money/F3, context/F4 rate part → F8.
- parties/F5 split into F11 (tags; Low, "Needs decision" changed from no to yes, because the tags follow the issuer consistently and earlier flows could not settle that convention) and F12 (untagged legal form, Low/no, as in earlier flows).
- F14 added by the merge.

## Outside this review
- Whether the voyage of 13/14 (dates, vessel, route) fits the map and other flows using the same vessel is a cross-flow timeline question (from context).
