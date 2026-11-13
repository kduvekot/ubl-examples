# LLM review: 06-OrderResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/06-OrderResponse.xml`, Git blob `8c32d38abff802a363b6a976f771dad7ef600e7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3f5c37 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/06#F1 · High · Confirmed payable amount and balance differ from what the invoice for the same sale bills
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`
- XPath: `/OrderResponse/cbc:Note` = `Accepted. A deposit of 10,000.00 lume is due on acceptance; the balance 45 days after shipment.`
- XPath: `/OrderResponse/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: the response accepts the order (`OrderResponseCode` `AP`, lines "Confirmed as ordered.") with a `PayableAmount` of 50,688.00 XBL, so the balance after the 10,000.00 deposit is 40,688.00. The invoice for this sale adds sea freight and cargo insurance (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`) and bills 53,778.00 (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `53778.00`), with a balance of 43,778.00 (`22-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `43778.00`). Recalculated: 50,688.00 + 2,950.00 + 140.00 = 53,778.00; 53,778.00 − 10,000.00 = 43,778.00; the deposit is 10,000 / 50,688 = 19.73 % here and 10,000 / 53,778 = 18.59 % in the invoice (`22-Invoice.xml:/Invoice/cac:PaymentTerms[1]/cbc:PaymentPercent` = `18.59`). The two documents state different amounts to be paid for the same sale. Under CIF the seller pays carriage and insurance; whether it prices them into 520 or passes them on, the response is where an added charge would be announced, and it announces none.
- Condition: the amount the order response confirms as payable (and the balance its note implies) equals what the invoice bills, or the response states the charges that will be added and the invoice adds only those.
- Options: (a) preferred: treat 520 as the CIF price and drop the separate freight and insurance charges from the invoice (CIF prices normally include carriage and insurance; aligned with sea merger c's preference for 22-Invoice.xml); (b) announce the freight and insurance in the order response (document-level charges, totals including them), so that response and invoice agree (money part's preference: the catalogue price is a trade price); (c) say in the note that freight and insurance are billed on top. The choice decides how CIF is priced in the flow (see 05#F13).
- Needs decision: yes
- From: money (F1)

### sea/06#F2 · Medium · Net and gross weight without the parts their definitions include
- XPath: `/OrderResponse/cbc:NetWeightMeasure` = `3762`
- XPath: `/OrderResponse/cbc:GrossWeightMeasure` = `4106.4`
- Why: in the order response `NetWeightMeasure` is "The total net weight for the Order Response (goods + packaging)" and `GrossWeightMeasure` "The total gross weight for the Order Response (goods + packaging + transport equipment)". The values are the packing list's goods-only net weight (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762`, "excluding packaging" there) and goods plus pallets (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`, = 3,984 + 122.4, recalculated). By these definitions the net weight would be 4,106.4 kg and the gross weight 4,106.4 + 3,750 tare = 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). The values follow trade usage (net = goods), which semantic conformance does not allow. Broad refuted the missing container tare (the response knows no container; "transport equipment" could be the pallets); then the gross would still be 4,106.4 but the net would have to be too, so the net weight stays wrong either way.
- Condition: each weight in the order response is the quantity its definition names, or is left out.
- Options: (a) preferred: drop both (the buyer acts on neither; packing list and bill of lading carry them); (b) net 4,106.4 kg and a gross with the planned 40-foot container (logistics' preference: the seller confirms an FCL shipment); note the gap to trade usage for the TC write-up.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1)

### sea/06#F3 · Medium · A language code in LocaleCode
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. 362 such elements in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or a locale from a locale list.
- Options: (a) preferred: drop it; (b) `en-XB` from a list of language tags.
- Needs decision: no
- From: broad (F3), parties (F1), context (F3)

### sea/06#F4 · Medium · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a vehicle gate is not a street name. 79 occurrences in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: no street-name element of Lumeway's postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no
- From: broad (F4), parties (F2), context (F8, Low)

### sea/06#F5 · Low · Shipped volume half the benches' size
- XPath: `/OrderResponse/cbc:GrossVolumeMeasure` = `41.5`
- XPath: `/OrderResponse/cbc:TotalPackagesQuantity` = `108`
- Why: `GrossVolumeMeasure` is "The total volume of the goods in the Order Response including packaging". The bench measures 1800 × 620 × 780 mm (`05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`), recalculated an envelope of 1.8 × 0.62 × 0.78 = 0.870 m³; 96 benches take 83.6 m³ before packaging, twice the stated 41.5 m³ (0.43 m³ per bench), and more than the about 67.7 m³ inside one 40-foot box (own knowledge). It only works if the benches travel knocked down or nested, which no document says (the order describes the assembled bench "supplied with four ground anchors"). Logistics found 41.5 m³ consistent with the packing list's 38.9 m³ net volume and with one container, so the figure is consistent across documents; the question is the goods' shape.
- Condition: the stated volume fits the goods as shipped, and the documents say how the benches are shipped if not assembled.
- Options: (a) state that the benches ship flat-packed or nested (item or packing description) and keep the volume; (b) a volume that fits assembled benches (then not one 40-foot container, a question for the transport documents).
- Needs decision: yes (how the benches are shipped)
- From: broad (F6)

### sea/06#F6 · Low · Originator document the order never mentioned
- XPath: `/OrderResponse/cac:OriginatorDocumentReference/cbc:ID` = `PS-REQ-26-0031`
- Why: `OriginatorDocumentReference` is "A reference to an originator document associated with this document". The Port of Selanu's request is not in the order this response answers (`05-Order.xml` carries no originator document reference) nor in any example, so the seller responds with a reference it received from nowhere, and the reference carries only an ID. Logistics refuted it (the element names the kind of reference, the port is the order's originator customer, and a requisition outside the flow is legitimate); that answers what it is, not how the seller knows it.
- Condition: the originator document is known to the seller from the order (the order carries it), or the response does not carry it.
- Options: (a) preferred: carry it in 05-Order as `OriginatorDocumentReference` and keep it here; (b) drop it here.
- Needs decision: no
- From: broad (F8), context (F5); logistics (Considered and refuted, counter-argument above)

### sea/06#F7 · Low · The digital trade agreement given as the order's contract
- XPath: `/OrderResponse/cac:Contract/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/OrderResponse/cac:Contract/cbc:ContractType` = `Digital trade agreement`
- Why: `Contract` is "A contract associated with the Order being responded to". `03-DigitalAgreement.xml:/DigitalAgreement/cbc:ID` = `LD-DAG-26-0125` governs how the parties exchange documents (processes, channels, SLA), not the sale of benches; the sale is governed by the transaction conditions `LD-TC-01` and general terms `LD-GTC-2026` the catalogue and order refer to.
- Condition: `Contract` refers to the commercial contract or framework of the sale, or is absent.
- Options: (a) preferred: drop `Contract`; (b) keep it if the story makes the digital agreement also the trading framework, and say so in the agreement.
- Needs decision: yes (whether the digital agreement is also the sales framework)
- From: broad (F7, no), context (F6, yes)

### sea/06#F8 · Low · Velumi Trading described differently from the order this response answers (en-XB tags, legal form only in English)
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: the order this responds to tags the same renderings `en-XL` and gives the legal form in both languages (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`, `05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); the flow splits along the issuer (16 vs 8 sea examples, `grep -c`).
- Condition: Velumi's addresses and legal form carry the same renderings and `languageID` values in every example, following one documented rule.
- Options: (a) preferred: `en-XL` and both languages everywhere; (b) a documented issuer-variety rule, with the Lisavan legal form.
- Needs decision: yes
- From: broad (F10, Low/no), parties (F3)

### sea/06#F9 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID"; Velumi shares the New Year's Day date with companies in all three registers (271 times in 181 examples, `grep -rho --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`), while Lumeway has `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1988-10-03`.
- Condition: every `RegistrationDate` is the party's date in the world, or absent.
- Options: (a) preferred: an own date per company; (b) drop it.
- Needs decision: yes
- From: parties (F5)

### sea/06#F10 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's purchasing contact carries the title and department of the seller's customer service.
- Condition: name, job title and department describe Velumi's purchasing function.
- Options: (a) preferred: a purchasing title and department; (b) drop them.
- Needs decision: no
- From: broad (F9), parties (F4), context (F7)

### sea/06#F11 · Low · The deposit's payment note calls the sales order an invoice
- XPath: `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123`
- XPath: `/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: `PaymentNote` is "free-form text applying to the Payment for the owner of this account". The payment is the deposit due on acceptance, before any invoice; `LD-SO-26-0123` is the seller's sales order ID ("An identifier for the Order, issued by the Seller"), and the only invoice of the sale is `22-Invoice.xml:/Invoice/cbc:ID` = `LD-INV-26-0147`. The structured reference `/OrderResponse/cac:PaymentMeans/cbc:PaymentID` = `RF41LDSO260123` is built on the sales order number, which fits. Low, not Medium as broad and context had it: the wrong word is in free text next to a correct structured reference (checklist "Free text"), aligned with the earlier flows' "Invoice …" payment notes (furniture b, sea d: Low/no).
- Condition: the payment note names the deposit and what it is paid against as what it is, not as an invoice.
- Options: (a) preferred: "Deposit on sales order LD-SO-26-0123"; (b) drop the note (the RF reference identifies the payment).
- Needs decision: no
- From: broad (F1, Medium), context (F2, Medium), money (F2)

### sea/06#F12 · Low · Balance terms only in the note
- XPath: `/OrderResponse/cbc:Note` = `Accepted. A deposit of 10,000.00 lume is due on acceptance; the balance 45 days after shipment.`
- XPath: `/OrderResponse/cac:PaymentTerms/cbc:ID` = `DEPOSIT`
- Why: the response sets two payment terms, but only the deposit is a `PaymentTerms`; the balance and its due event exist only in free text, while the invoice carries both terms structured (`22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cbc:ID` = `BALANCE`).
- Condition: every payment term the response states is a `PaymentTerms` (deposit and balance), consistent with the note.
- Options: (a) preferred: add a `BALANCE` term (shipment + 45 days), with the amount resolved by F1.
- Needs decision: no
- From: broad (F5)

### sea/06#F13 · Low · LineStatusCode NoStatus on confirmed lines
- XPath: `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cbc:LineStatusCode` = `NoStatus`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:LineItem/cbc:LineStatusCode` = `NoStatus`
- XPath: `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cbc:Note` = `Confirmed as ordered.`
- Why: `LineStatusCode` is "A code signifying the status of this line item with respect to its original state"; `NoStatus` says nothing, and the acceptance is already given by `OrderResponseCode` `AP` and the note. A code that states no status is a filler (IND5). Broad refuted it (the UBL line status list has no "accepted" code; acceptance is expressed by `AP`); that is the reason to drop the element rather than to keep a value with no content. Earlier merges (wood, plastics, air, retail, sea b/c) set NoStatus to Low/no, drop.
- Condition: `LineStatusCode` is absent, or carries a status the line has (e.g. revised).
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (Considered and refuted); made a finding in the merge, aligned with earlier flows

## Checked and consistent
- Order reference `VT-PO-26-0127` resolves to `05-Order.xml`; lines, quantities, prices, amounts recalculated (96 × 520.00 = 49,920.00; 12 × 64.00 = 768.00; sum 50,688.00 = `/OrderResponse/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `50688.00` = taxable amount) and tax (G, 0 %) agree with it; `TaxInclusiveLineExtensionAmount` equals the line amount at 0 %.
- Deposit: `/OrderResponse/cac:PaymentTerms/cbc:Amount` = `10000.00` due `/OrderResponse/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-09` = the payment means' due date and the note's amount; the invoice records it received on that day (`22-Invoice.xml:/Invoice/cac:PrepaidPayment/cbc:ReceivedDate` = `2026-05-09`).
- Balance due date: shipment 2026-05-14 + 45 days = 2026-06-28 (recalculated: 17 days to end of May, 30 in June, 1 more = 28 June), the invoice's due date (`22-Invoice.xml:/Invoice/cbc:DueDate` = `2026-06-28`).
- Account `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB19BLUM38712001466206` and RF reference pass their check digits (`check_ids.py`); the account is in the seller's registered name (`/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Lumeway Distribution Ltd`), right for a deposit paid before the receivable is assigned to Harbourline.
- `TotalPackagesQuantity` 108 = 96 benches + 12 frames, the bill of lading's package count (24 pallets × 4 + 12).
- 41.5 m³ in one 40-foot box (about 67.7 m³ inside) and 7,856 kg gross far below a 42G1's 30,480 kg (logistics, own knowledge). CIF Port of Selanu with LOCODE `XLSEL`, as in the bill of lading and invoice. Contract `LD-DAG-26-0125` resolves to 03.
- Seller, buyer, originator (Port of Selanu) and beneficiary agree with 05-Order.xml; warranty party Valdara (the manufacturer) fits the warranty text.

## Considered and refuted
- `/OrderResponse/cbc:Note`: "the balance 45 days after shipment" against the invoice's "30 days net" — refuted for this example: the invoice's own due date is 45 days after shipment, as agreed here; the contradiction lies inside the invoice (from broad, money).
- `/OrderResponse/cbc:GrossWeightMeasure`: excludes the container tare — refuted by broad (the response knows no container); taken into F2's Why, which stands on the net weight either way.
- `/OrderResponse/cac:PaymentTerms/cbc:Note` = `Deposit due on acceptance.` with a due date one day after acceptance — refuted: the next banking day is an ordinary reading, and the deposit was paid on 2026-05-08 (from money).
- `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` = `387120` against the invoice's branch — refuted: the invoice's account is Harbourline's, after the assignment (from money).
- `/OrderResponse/cac:OrderLine[1]/cac:OrderLineReference/cbc:LineID` next to a line item with the same ID — refuted: the usual way to tie the response line to the order line (from context).
- `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate`: a promised delivery period under CIF — refuted: 14–18 May is a plausible promise of arrival (from context; the end-date question is under Outside).
- `/OrderResponse/cac:OriginatorDocumentReference/cbc:ID`: refuted by logistics — not followed, see F6.
- `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cbc:LineStatusCode`: refuted by broad — not followed, see F13.

## Refuted in the merge
### context/F4 · Low · Packages counted as items
- XPath: `/OrderResponse/cbc:TotalPackagesQuantity` = `108`
- Why (context): `TotalPackagesQuantity` is "the total number of packages contained in the Order Response"; 108 is the number of items (96 benches + 12 frames), while the goods travel on pallets of four and the packing list counts 25 handling units (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:TotalTransportHandlingUnitQuantity` = `25`); unless every item is packed individually, 108 is not a number of packages.
- Condition (context): `TotalPackagesQuantity` is the number of packages, or the response states that each item is a package.
- Refuted because: the bill of lading counts the same 108 packages: 24 pallets with 4 packages each and the frames' pallet with 12 (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:PackagedTransportHandlingUnit[25]/cbc:TotalPackageQuantity` = `12`); film-wrapped benches are packages, and the 25 handling units are the pallets carrying them, a different count (logistics and broad came to the same result).

## Changed in the merge
- money/F2 (Low) + broad/F1 (Medium) + context/F2 (Medium) → F11: Low, aligned with earlier flows' "Invoice …" payment notes (free text next to a correct structured reference).
- broad/F2, logistics/F1, context/F1 → F2: grouped; preferred option drop (broad, context), logistics' container option kept as (b).
- broad/F3, parties/F1, context/F3 → F3: preferred option drop, aligned.
- context/F8 → F4: Low raised to Medium, aligned.
- broad/F8 + context/F5 → F6: grouped; logistics' refutation carried.
- broad/F7 (no) + context/F6 (yes) → F7: yes.
- broad/F10 (no) + parties/F3 (yes) → F8: yes.
- broad's refutation of NoStatus → F13 (Low/no), aligned with earlier flows.
- money/F1 → F1: preferred option changed from announcing the charges in the response to dropping them from the invoice, aligned with sea merger c (22-Invoice.xml); money's preference kept as (b).
- context/F4 → Refuted in the merge.

## Outside this review
- `22-Invoice.xml`: the balance terms' note "30 days net" contradicts its own due date 2026-06-28, 45 days after shipment (from broad, money).
- The promised delivery period ends 2026-05-18 (`/OrderResponse/cac:OrderLine[1]/cac:LineItem/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-05-18`), while the goods reach the warehouse on 2026-05-19 and are received on 2026-05-21 (`21-ReceiptAdvice.xml`); under CIF delivery is the loading at Lumeport on 2026-05-14. A timeline question across documents (from logistics).
