# LLM review: 06-OrderResponse.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/06-OrderResponse.xml`, Git blob `8c32d38abff802a363b6a976f771dad7ef600e7d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### sea/06#F1 · Medium · The deposit's payment note calls the sales order an invoice
- XPath: `/OrderResponse/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice LD-SO-26-0123`
- XPath: `/OrderResponse/cbc:SalesOrderID` = `LD-SO-26-0123`
- Why: `LD-SO-26-0123` is the seller's identifier of the order (`SalesOrderID`, "An identifier for the Order, issued by the Seller"). The payment note presents it as an invoice number. No invoice exists when the deposit is due on acceptance; the invoice of the flow is `LD-INV-26-0147` (`22-Invoice.xml:/Invoice/cbc:ID`). An identifier of one kind is given as another.
- Condition: the payment note names the sales order (or the deposit) as what it is, or is absent (the structured `PaymentID` already carries the reference).
- Options: (a) preferred: "Deposit for order LD-SO-26-0123"; (b) drop the note.
- Needs decision: no

### sea/06#F2 · Medium · Net weight given without packaging, although the order response defines it as goods plus packaging
- XPath: `/OrderResponse/cbc:NetWeightMeasure` = `3762`
- XPath: `/OrderResponse/cbc:GrossWeightMeasure` = `4106.4`
- Why: in the order response `NetWeightMeasure` is "The total net weight for the Order Response (goods + packaging)". 3762 kg is the weight of the goods without packaging, as the packing list states it (`10-PackingList.xml:/PackingList/cac:Shipment/cbc:NetWeightMeasure` = `3762`, defined there as "excluding packaging"); goods plus packaging is 4106.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:GoodsItem[1]/cbc:GrossWeightMeasure` 3984 + `…/cac:GoodsItem[2]/cbc:GrossWeightMeasure` 122.4). The value fits another definition than this element's.
- Condition: `NetWeightMeasure` in the order response is the weight of goods plus packaging (4106.4 kg), and `GrossWeightMeasure` includes what its definition adds ("transport equipment"), or the elements are absent.
- Options: (a) preferred: drop both weights from the order response (the packing list and bill of lading carry them with fitting definitions); (b) net 4106.4 kg and a gross that includes the pallets' transport equipment as defined.
- Needs decision: no

### sea/06#F3 · Medium · Language code in LocaleCode
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode` (`grep -c LocaleCode world/examples/*/*.xml`).
- Condition: `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/06#F4 · Medium · A gate in AdditionalStreetName
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/06#F5 · Low · Balance terms only in the note
- XPath: `/OrderResponse/cbc:Note` = `Accepted. A deposit of 10,000.00 lume is due on acceptance; the balance 45 days after shipment.`
- XPath: `/OrderResponse/cac:PaymentTerms/cbc:ID` = `DEPOSIT`
- Why: the response sets two payment terms, but only the deposit is given as `PaymentTerms`; the balance (40,688.00 XBL for the goods, plus freight and insurance under CIF) and its due event exist only in free text. The invoice later carries both terms in structured form (`22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cbc:ID` = `BALANCE`).
- Condition: every payment term the response states is a `PaymentTerms` (deposit and balance), consistent with the note.
- Options: (a) preferred: add a `BALANCE` payment term (reference event shipment, 45 days); (b) none better seen.
- Needs decision: no

### sea/06#F6 · Low · Shipped volume far below the benches' size
- XPath: `/OrderResponse/cbc:GrossVolumeMeasure` = `41.5`
- XPath: `/OrderResponse/cbc:TotalPackagesQuantity` = `108`
- Why: `GrossVolumeMeasure` is "The total volume of the goods in the Order Response including packaging". The ordered bench measures 1800 × 620 × 780 mm (`05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`, `[2]` = 620, `[3]` = 780), an envelope of 0.87 m³; 96 benches take 83.6 m³ before packaging, twice the stated 41.5 m³ (0.43 m³ per bench). This only works if the benches travel knocked down or nested, which no document says; the order describes the assembled bench "supplied with four ground anchors".
- Condition: the stated volume fits the goods as shipped, and the documents say how the benches are shipped if not assembled.
- Options: (a) state that the benches ship flat-packed (item or packing description) and keep the volume; (b) a volume that fits assembled benches (which then would not fit one 40-foot container, a question for the logistics documents).
- Needs decision: yes (how the benches are shipped)

### sea/06#F7 · Low · The digital trade agreement given as the order's contract
- XPath: `/OrderResponse/cac:Contract/cbc:ID` = `LD-DAG-26-0125`
- XPath: `/OrderResponse/cac:Contract/cbc:ContractType` = `Digital trade agreement`
- Why: `Contract` here is "A contract associated with the Order being responded to". The referenced digital agreement (`03-DigitalAgreement.xml:/DigitalAgreement/cbc:ID` = `LD-DAG-26-0125`) agrees how documents are exchanged (network, formats, SLA); it is not a sales contract and contains no commercial terms of this order. The commercial terms are the general terms `LD-GTC-2026` the catalogue refers to.
- Condition: `Contract` refers to an agreement that governs the sale, or is absent.
- Options: (a) preferred: drop it (the order follows the catalogue and its general terms); (b) refer to a framework sales contract if the world has one.
- Needs decision: no

### sea/06#F8 · Low · Originator document not known from the order
- XPath: `/OrderResponse/cac:OriginatorDocumentReference/cbc:ID` = `PS-REQ-26-0031`
- Why: the response references the Port of Selanu's requisition, which the order it answers does not mention (`flow_index.py sea` lists no such reference for `05-Order.xml`) and which is no example. The seller has no way to know the ID, and the reference says nothing about the document.
- Condition: the originator document is referenced in the order first, or the response does not carry it.
- Options: (a) preferred: add the reference to the order (`OriginatorDocumentReference`) and keep it here; (b) drop it here.
- Needs decision: no

### sea/06#F9 · Low · Velumi's purchasing contact is a customer service officer in Sales
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the contact is named `Purchasing`; job title and department belong to a seller's customer service. Same values in every sea example with this contact.
- Condition: name, job title and department of Velumi's contact describe the same function.
- Options: (a) preferred: purchasing job title and department.
- Needs decision: no

### sea/06#F10 · Low · Velumi's Lisavu address tagged as Bayvarran English
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- Why: the order Velumi sent tags the same renderings `en-XL` (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); the tag follows the sender's country across the flow (16 × `en-XB`, 8 × `en-XL` over `world/examples/sea/*.xml`). The same address should carry the same tag; for Lisavu `en-XL` fits.
- Condition: Velumi's address renderings carry the same `languageID` in every example.
- Options: (a) preferred: `en-XL` everywhere.
- Needs decision: no

## Checked and consistent
- Order reference resolves to `05-Order.xml`; lines, quantities, prices, line and total amounts (49,920.00 + 768.00 = 50,688.00) and tax (`G`, 0 %) agree with the order.
- The deposit agrees with the invoice: 10,000.00 XBL due 2026-05-09 (`22-Invoice.xml:/Invoice/cac:PaymentTerms[1]/cbc:InstallmentDueDate` = `2026-05-09`), paid to the same account; the balance due date in the invoice (2026-06-28) is 45 days after the bill of lading date 2026-05-14, as the note says.
- `TotalPackagesQuantity` 108 = 96 benches + 12 side frames, each packed individually, as the bill of lading counts them (4 packages per pallet × 24 pallets + 12).
- Gross weight 4106.4 kg agrees with the packing list and the bill of lading.
- RF reference `RF41LDSO260123` and the IBAN-like account have valid check digits (`check_ids.py`); GLN correct.
- Promised delivery 2026-05-14 to 2026-05-18 brackets the bill of lading (2026-05-14) and the arrival status at Selanu (`17-TransportationStatus.xml`, issued 2026-05-18).
- CIF named place Port of Selanu with UN/LOCODE `XLSEL` agrees with the order.

## Considered and refuted
- `/OrderResponse/cbc:Note`: "the balance 45 days after shipment" against the invoice's "30 days net" (`22-Invoice.xml:/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`) — refuted for this example because the invoice's own due date (2026-06-28) is 45 days after shipment, as agreed here; the contradiction lies inside the invoice.
- `/OrderResponse/cac:OrderLine[1]/cac:LineItem/cbc:LineStatusCode` = `NoStatus` next to "Confirmed as ordered." — refuted because the UBL line status list has no "accepted" code; acceptance is expressed by the response code `AP`.
- `/OrderResponse/cbc:GrossWeightMeasure`: excludes the container tare — refuted because the order response knows no container; "transport equipment" here can be read as the pallets.

## Outside this review
- `22-Invoice.xml`: the balance terms' note "30 days net" contradicts its own installment due date 2026-06-28, 45 days after shipment (for the review of that example).
