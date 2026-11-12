# LLM review: 10-Invoice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/10-Invoice.xml`, Git blob `4f8e76fdb62682517ade76167e8a942e4bcac42e` (committed)
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

### air/10#F1 · High · Freight "per kilogram chargeable weight" is invoiced on the gross weight
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `81.6`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `6.8`
- XPath: `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `554.88`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `8.32`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: The line is priced at 6.8 XBL per 1 KGM "per kilogram chargeable weight", and the invoice refers to the waybill `KXL-WB-26-0325`, whose chargeable weight ("the weight upon which a charge is to be based") is 96 kg; 81.6 kg is the gross weight. Arithmetic redone in the merge: the waybill's volume 0.576 m³ = 8 boxes × 0.8 m × 0.3 m × 0.3 m (`03-ForwardingInstructions.xml` package dimensions, read per box); 576 000 cm³ / 6 000 cm³ per kg (the IATA volumetric divisor, own knowledge) = 96.0 kg; the density 81.6 kg / 0.576 m³ = 141.7 kg/m³ is below the 166.7 kg/m³ that the 1:6 ratio implies, so the volumetric weight governs and the chargeable weight is 96 kg, as the waybill says. Invoiced: 81.6 × 6.8 = 554.88 XBL; as described: 96 × 6.8 = 652.80 XBL (97.92 more), with penalty 1.5 % × 652.80 = 9.792 → 9.79 instead of 8.32. The merge tried to refute it: even if the dimensions are read as those of the whole package aggregate (0.072 m³, 12 kg volumetric; the money part's doubt about the waybill's volume, a question for 04's review), the chargeable weight would be the gross weight rounded up to the next half kilogram, 82.0 kg (own knowledge of IATA practice), not 81.6. In no reading is the invoiced quantity the chargeable weight, so the quantity, the description and the referenced waybill contradict each other.
- Condition: the invoiced quantity is the chargeable weight of the shipment as the waybill states it, and quantity × price = line amount = LineExtensionAmount, TaxExclusiveAmount, TaxInclusiveAmount, PayableAmount and TaxableAmount, with the PenaltyAmount following.
- Options: (a) preferred: InvoicedQuantity 96 KGM, line and totals 652.80, PenaltyAmount 9.79, because chargeable weight is how air freight is charged and the waybill states it; (b) keep 81.6 kg and change the description to "per kilogram gross weight", which the waybill then does not support as the charge basis.
- Needs decision: no
- From: broad (F1), money (F1), logistics (F1), context (F1)

### air/10#F2 · Medium · LocaleCode holds a language code
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value is the ISO 639 language code `en` (listID `ISO 639`), repeating the sibling `cbc:ID`. Section 6 names it a Medium case. 362 occurrences in 213 examples (re-counted in the merge).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list, or the element is absent.
- Options: (a) preferred: drop `LocaleCode`; (b) a real locale (e.g. `en-XB` from a locale list).
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### air/10#F3 · Medium · A gate in AdditionalStreetName of the customer's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is the entrance of Lumeway Distribution's site, not a street, and has no place in the postal address an invoice is addressed to. 79 occurrences in 76 examples (re-counted in the merge).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate.
- Options: (a) preferred: drop it; (b) carry it only in a pickup or despatch location of documents that need it.
- Needs decision: no
- From: parties (F2), context (F3)

### air/10#F4 · Low · Outbound freight booked as "Stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- XPath: `01-OrderChange.xml:/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`
- Why: AccountingCostCode is "The buyer's accounting code, applied to the Invoice as a whole". The buyer of this invoice, Lumeway Distribution, pays the air freight it owes as seller under CPT to Velumi Trading: an outbound distribution cost of a sale, not a purchase of stock. The same code and text are Lumeway's posting for goods it buys (`road/15-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410`, `rail/11-Invoice.xml:/Invoice/cbc:AccountingCostCode` = `4410`; 8 files with this code over `*.xml`, `grep -rn --include='*.xml' '<cbc:AccountingCostCode>4410'`, count from the money part), so it looks copied from Lumeway's purchasing data.
- Condition: the buyer's accounting code and text fit a freight cost on a sale, consistent with the delivery terms, or are absent.
- Options: (a) preferred: a code and text for outbound freight / distribution costs; (b) remove both elements, if the forwarder does not know the buyer's code.
- Needs decision: no
- From: broad (F3), money (F3), context (F6)

### air/10#F5 · Low · Reference to a statement that does not exist, and could not yet exist if it is the May statement
- XPath: `/Invoice/cac:StatementDocumentReference/cbc:ID` = `BF-SOA-26-05`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-15`
- Why: StatementDocumentReference is "A reference to a Statement associated with this document". No example has the ID `BF-SOA-26-05` (`grep -rn --include='*.xml' BF-SOA world/examples`: this reference only, re-run in the merge), and no statement of Bayforth Forwarding exists in any flow. The ID reads as the statement of account for May 2026, which would be drawn up at the end of the month, after this invoice of 15 May; a statement lists its invoices, not the reverse. The money part rated it High (a referenced document that does not exist, section 6). The merge lowers it to Low with Needs decision yes, as the broad, logistics and context parts: the statement would be a document outside the flow (a statement of account covers many shipments), not a document of the flow that the reference fails to reach, and that it is the May statement is an inference from the ID that the XML does not confirm; whether the forwarder bills through a running account with monthly statements is a story question.
- Condition: the reference points to a statement that exists at the invoice's issue date (in the flow, issued by Bayforth Forwarding to Lumeway Distribution), or is absent.
- Options: (a) preferred: remove the reference (the later statement can refer to the invoice); (b) refer to an earlier statement, or, if a running account agreement is meant, to that agreement as a contract; (c) add the statement to the flow.
- Needs decision: yes (whether the forwarder bills through a monthly statement)
- From: money (F2, High, decision yes), broad (F4, Low, decision no), logistics (F3, Low, decision yes), context (F4, Low, decision yes)

### air/10#F6 · Low · The forwarder invoices against the carrier's waybill, not its own house waybill, and the reference does not say what it is
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`
- Why: According to the waybill, Bayforth consolidated the consignment under its own house waybill `BF-HAWB-26-0918` within Kelaro's waybill. The forwarder's contract with Lumeway is then the house waybill; the master waybill is the forwarder's contract with the airline. The invoice refers to the master only, with no document type saying what the reference is. The logistics part refuted this as a finding of this example (for a direct air waybill, which every other document of the flow assumes, the carrier's waybill is the right document; the contradiction lies in 04), and the broad part refuted the ID-only reference (it resolves, and consignment and carrier make clear it is the air waybill). The merge cannot settle it before the consolidation question of `04-Waybill.xml` is settled: if the shipment is consolidated, the reference is wrong here; if not, only the document type is missing.
- Condition: the invoice refers to the transport document between Bayforth and Lumeway, with its kind stated.
- Options: (a) preferred: settle the consolidation in 04 first; then refer to the house waybill (if consolidated) or keep `KXL-WB-26-0325` with a DocumentTypeCode; (b) keep as is if 04 drops the consolidation and a type is not wanted.
- Needs decision: yes (whether the shipment is consolidated, settled in 04)
- From: context (F7); refuted by logistics and broad (Considered and refuted), counter-arguments above

### air/10#F7 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." 1996-01-01 is given for Bayforth Forwarding and Kelaro Air Cargo here, and for 25 companies in three registers over 181 examples (`grep -rl --include='*.xml'`, re-counted in the merge), while Lumeway Distribution in this invoice has its own date (1988-10-03). Without a story event it reads as a default value ("no fillers").
- Condition: each company's `RegistrationDate` is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) a date per company; (b) drop it where no date is known; (c) record 1996-01-01 as a story event.
- Needs decision: yes (company histories)
- From: parties (F4)

### air/10#F8 · Low · The contacts of the invoice parties are an operations desk and a sales desk
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Operations`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting supplier party claims payment and the accounting customer party pays; their contacts in an invoice are the people to turn to about the bill. Bayforth's contact is its export operations desk, and Lumeway's its sales customer service, the contact Lumeway uses towards its own customers (`01-OrderChange.xml:/OrderChange/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`), not the one that receives and pays a forwarder's invoice. Both look copied from the parties' master data. (Unlike the other contact findings of the flow, name, title and department agree with each other here; the problem is the role.)
- Condition: each accounting party's contact fits billing (e.g. accounts receivable at Bayforth, accounts payable at Lumeway), or the contact is absent.
- Options: (a) preferred: an accounting contact for each party; (b) drop the contacts.
- Needs decision: no
- From: broad (F5), parties (F6)

### air/10#F9 · Low · The delivery of the service has no date and no shipment ID
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: The invoice bills a transport. Its Delivery identifies the consignment and the carrier but not when the service was completed (Delivery/ActualDeliveryDate, the arrival on 2026-05-14 in `09-TransportationStatus.xml`) nor the shipment `LD-SH-26-0323` that the forwarder was instructed with (`03-ForwardingInstructions.xml`), which the customer would use to match the invoice with its own shipment. Checked in the merge: the invoice has neither a delivery date nor an InvoicePeriod.
- Condition: the invoice states the date the service was performed (delivery date or invoice period) and identifies the shipment the customer knows.
- Options: add ActualDeliveryDate 2026-05-14 (or the date that 07's review, F2, settles) and Shipment/ID `LD-SH-26-0323` (preferred).
- Needs decision: no
- From: logistics (F4)

### air/10#F10 · Low · English renderings of the carrier's island address tagged en-XB here, en-XL elsewhere
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `04-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`
- Why: The English renderings of Kelaro Air Cargo's address (`Airfield Road`, `Port Wrenfield`) carry `en-XB` here, `en-XL` for the same text of the same party in `04-Waybill.xml` (35 examples tag `Port Wrenfield` `en-XB`, 27 `en-XL`; re-counted in the merge). The tag seems to follow the issuer; that rule is written down nowhere (the broad part of 06 and 08 holds it is consistent), and the island names argue for `en-XL`. The merge cannot settle which rule applies.
- Condition: the same rendering of the same address carries the same `languageID` in every example of the flow, chosen by a stated rule.
- Options: (a) preferred: `en-XL` for island addresses everywhere; (b) keep the writer's variety and record the rule.
- Needs decision: yes (which convention the world follows)
- From: parties (F3)

### air/10#F11 · Low · The island carrier's legal form in one untagged rendering
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: Kelaro Air Cargo's legal form appears here once, in English, without `languageID`, while the island-issued examples give it in Lisavan and English, each tagged (`09-TransportationStatus.xml`, `04-Waybill.xml`), and its address is rendered in both languages in this invoice. The parties part mentioned this as related to its language-tag finding (F10); the merge makes it a separate Low finding, aligned with the merges of air 01–05, wood and plastics. Resolved together with F12 if the carrier party is reduced to identifier and name.
- Condition: the legal form is rendered the same way as the party's address (both languages, tagged), or is absent with the rest of the carrier's master data.
- Options: drop it with F12 (preferred); or render it like the address, with `qal` and English tagged.
- Needs decision: no
- From: parties (as a remark in F3)

### air/10#F12 · Low · The carrier's full master data in the invoice's delivery
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:ID` = `58930746`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41311`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- Why: The invoice bills Bayforth's air freight to Lumeway; naming the carrier helps identify the shipment, but its postal address, legal entity, contact and electronic address serve no purpose here: Lumeway neither contacts nor pays Kelaro Air Cargo under this invoice, and the waybill is already referenced. Data copied from a party's master data into a document that does not use it is a Low finding (section 4.8).
- Condition: the invoice's carrier party carries only what identifies the carrier (identifier and name), unless the invoice uses more.
- Options: (a) preferred: reduce `CarrierParty` to `PartyIdentification` and `PartyName`; (b) drop it and rely on the waybill reference.
- Needs decision: no
- From: parties (F7)

### air/10#F13 · Low · The carrier's contact name and job title disagree
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". Kelaro Air Cargo's `Cargo sales` contact is an operations planner in Operations, so either the name or the title is wrong; the same combination throughout the flow. Resolved together with F12 if the contact is dropped.
- Condition: `Name`, `JobTitle` and `Department` of the contact describe the same function, or the contact is absent (F11).
- Options: (a) preferred: drop the contact with F12; (b) align name and title (cargo sales agent / Sales, or a cargo operations desk).
- Needs decision: no
- From: parties (F5)

### air/10#F14 · Low · "Airport-to-airport … road feeder included" does not match the carriage invoiced
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `4`
- Why: The waybill has a single air stage, Lumeport airport to Selanu airport; no document of the flow has a road feeder service (a truck operated under the airline's flight number between airports, own knowledge) or a road leg on the waybill. Two parts refuted it: the broad part because the forwarder's pickup at Lumeway (`03-ForwardingInstructions.xml`, pickup by Bayforth) is the road leg; the money part because a road feeder service runs between airports and so stays airport-to-airport. The merge disagrees with both: a pickup at the shipper's premises is not airport-to-airport carriage and not a road feeder service; and a road feeder service between airports would appear as a stage of the air waybill, which here has only the flight, while the destination is an island (context part).
- Condition: the description names only services that the transport documents show, or the waybill shows the road feeder leg.
- Options: (a) preferred: "Airport-to-airport air freight per kilogram chargeable weight", with the pickup as a separate line if it is charged; (b) add the road leg to 04 (changes the story), or describe the service as door-to-airport including pickup.
- Needs decision: no
- From: logistics (F2), context (F5); refuted by broad and money (Considered and refuted), counter-arguments above

## Checked and consistent
- Arithmetic as it stands: 81.6 × 6.8 = 554.88 = LineExtensionAmount = TaxExclusiveAmount = TaxInclusiveAmount = PayableAmount; TaxableAmount 554.88, TaxAmount 0.00 (category E, 0 %); PenaltyAmount 8.32 = 1.5 % × 554.88 (8.3232); no allowances, charges or prepaid amount (broad, money, logistics, context; redone in the merge).
- Payment terms: DueDate 2026-06-14 = issue date + 30 days ("30 days net") = PaymentMeans/PaymentDueDate = PaymentTerms/PaymentDueDate; PenaltyPeriod starts 2026-06-15 for one month ("per month") (broad, money, context).
- Payment means: credit transfer (30) to Bayforth Forwarding Ltd's account; RF66BFINV260331 (RF check digits OK) in PaymentID and InstructionNote; the IBAN-like account XB40BLUM38020502618225 passes its check, and bank code BLUM and branch 380205 match the bank `BLUMXBLX` and the branch; `BLUMXBLX` has the fictional country code XB, so it cannot be a real BIC; PaymentMeansID 1 resolves (broad, money, context).
- Tax: exempt service to a business (SVCB2B, supply type SERVICES, scheme STT) consistent in line and subtotal, and used the same way for business services in other flows (broad, money).
- Parties: under CPT (`01-OrderChange.xml`) the seller Lumeway pays the main carriage, so Bayforth billing Lumeway is right; Lumeway is the consignor that instructed Bayforth (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyIdentification/cbc:ID` = `20411644`); Bayforth's state tax registration matches `XB-CO` and is the same in 03, 04 and 09 (all parts).
- `KXL-WB-26-0325` resolves to `04-Waybill.xml` (issued 2026-05-13); consignment `LD-CS-26-0324` and carrier Kelaro Air Cargo agree with it; the invoice (15 May) follows the arrival (14 May) (broad, logistics, context, parties).

## Considered and refuted
- `/Invoice/cbc:InvoiceTypeCode` = `380`: a commercial invoice for a service — refuted because UN/EDIFACT 1001 code 380 "Commercial invoice" covers goods and services (from broad, context).
- `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `E`: international air freight is often zero-rated rather than exempt in real VAT systems — refuted because the world's state sales tax exempts services to businesses as a rule, applied consistently across flows, and the reason code describes the transaction as UBL expects (from money).
- No valuation charge for the declared value of 512.00 XBL on the waybill — refuted as a finding here: whether a valuation charge applies depends on the declared value exceeding the carrier's limit, which cannot be judged in the fictional currency (see the waybill's review on AdValoremIndicator) (from money).
- `/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution` and `/Invoice/cac:SellerSupplierParty`: repeat the accounting parties — refuted: no "if different" condition in their definitions; identifier and name only (from context, parties).
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`: reference by ID only — refuted by broad (it resolves, and the consignment and carrier make clear it is the air waybill), and the house-waybill question refuted by logistics; the merge cannot settle the latter and keeps context's finding as F6.
- `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description`: "road feeder" with no road leg — refuted by broad (pickup is the road leg) and money (a road feeder service is airport-to-airport); the merge disagrees and keeps it as F14.

## Changed in the merge
- money/F2 (High) → F5, Low with Needs decision yes: reason in the finding (statement outside the flow, May-statement reading not confirmed by the XML); broad/F4, logistics/F3, context/F4 combined into it.
- broad/F1, money/F1, logistics/F1, context/F1 → F1: combined; arithmetic redone and extended (volume from the package dimensions, density check, both readings of the dimensions, penalty 9.79).
- broad/F3, money/F3, context/F6 → F4: combined, the CPT delivery terms added as evidence.
- broad/F5 and parties/F6 → F8: combined.
- broad/F2 options: "drop LocaleCode" preferred, as parties, context and the other flows.
- parties/F5 → F13: kept separate from F8 (here name and title disagree; in F8 the role is wrong), option (a) tied to F12.

## Outside this review
- The cargo was offloaded and flew a day later according to `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`, while the status report of the same day says it arrived (`09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`): recorded as findings in 07 and 09; for this invoice it only bears on the service date of F9 (from money).
- Whether the waybill's volume of 0.576 m³ is supported by the package dimensions in `03-ForwardingInstructions.xml` (per box or per package aggregate) is a question for the review of `04-Waybill.xml` (from money).
