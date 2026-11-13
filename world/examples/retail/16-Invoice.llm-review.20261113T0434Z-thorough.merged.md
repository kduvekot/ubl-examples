# LLM review: 16-Invoice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/16-Invoice.xml`, Git blob `e1ce518ac0f84644902623e83922648f889ca0d0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ab5be32 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/16#F1 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself, repeats `Language/cbc:ID` and names no locale. ISO 639 is a list of languages, not of locales. The same value occurs 362 times in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `grep -rl` for the files; recounted in the merge; the parties part's 364 also counted `PreferredLanguageLocaleCode` and `TenderLanguageLocaleCode`).
- Condition: no `Language/cbc:LocaleCode` holds a bare language code; where present it identifies a locale and its `listID` names a list of locales.
- Options: (a, preferred) drop `LocaleCode`; (b) a real locale such as `en-XB` from a list that defines locales (context preferred this). Fixed in the party master data.
- Needs decision: no
- From: broad (F1), parties (F1), context (F1)

### retail/16#F2 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is a vehicle entrance of the distribution centre, not a street name, and an invoice address has no use for it. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it; (b) record it in Bayvarra's address format if it really is a postal element (finding then dismissed).
- Needs decision: no
- From: broad (F2), parties (F2)

### retail/16#F3 · Low · Outbound delivery freight booked to the buyer's "Stock purchases"
- XPath: `/Invoice/cbc:AccountingCostCode` = `4410`
- XPath: `/Invoice/cbc:AccountingCost` = `Stock purchases`
- Why: `AccountingCostCode`/`AccountingCost` are "The buyer's accounting code, applied to the Invoice as a whole". The buyer is Lumeway, and what it buys is the road transport of goods it sold to Brightmarket delivered duty paid (`/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Truck load within Bayvarra, price per kilometre driven loaded.`; `08-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`). Delivering sold goods is a distribution cost of the seller, not a purchase of stock (own knowledge of cost accounting); inbound freight could be capitalised into stock, but this leg carries goods out of stock. Moreover no document of the flow gives the carrier this code (the transport request 11 carries none), so the carrier has no source for it.
- Condition: the buyer's accounting cost names an account for outbound freight or distribution that the buyer gave the carrier, or is absent.
- Options: (a, preferred) drop both, since the carrier has no source for them (context); (b) an outbound-freight code, given in 11-TransportExecutionPlanRequest and repeated here (broad, money preferred an outbound-freight code).
- Needs decision: no
- From: broad (F3), money (F1), context (F2)

### retail/16#F4 · Low · The waybill reference has no type, and the invoice cites neither the transport booking nor the contract
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `BF-WB-26-0231`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:ID` = `LD-TR-26-0227`
- XPath: `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-BF-FW-2026`
- Why: the additional reference resolves to the consignment note 13 but does not say it is one (no `DocumentTypeCode`/`DocumentType`). The service was ordered with Lumeway's transport execution plan request `LD-TR-26-0227` under the framework contract `LD-BF-FW-2026`, which also justifies the rate of 2.85 per loaded kilometre; the invoice cites neither, so Lumeway can match it to its booking only through the consignment ID, which is not its purchase reference.
- Condition: the waybill reference states its type, and the invoice identifies the transport request (as the buyer's order) or the contract under which the transport was bought.
- Options: (a, preferred) `OrderReference` `LD-TR-26-0227` and a document type on the waybill reference; (b) `ContractDocumentReference` `LD-BF-FW-2026`, which also explains the price.
- Needs decision: no
- From: money (F2), logistics (F2)

### retail/16#F5 · Low · Transport invoiced nine minutes before the goods were received
- XPath: `/Invoice/cbc:IssueDate` = `2026-04-30`
- XPath: `/Invoice/cbc:IssueTime` = `10:31:00`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- Why: the invoice bills the loaded kilometres of the delivery to the store, but the receipt advice records the truck's arrival at 10:40 on the same morning, after this invoice. If the delivery took place on 2026-04-29 as 15-TransportationStatus expected (14:00), the timing would be natural; which day applies is the open question of 15/F4. The context part's "invoice date after the carriage (2026-04-29/30)" holds only for the 29th.
- Condition: the transport invoice is issued after the delivery it bills.
- Options: (a, preferred) follows from resolving 15/F4: nothing to change if delivery is on 2026-04-29; issue the invoice after 10:40 if delivery is on 2026-04-30.
- Needs decision: yes
- From: logistics (F1)

### retail/16#F6 · Low · Contacts that do not fit the billing roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: on an invoice the supplier's contact answers billing questions and the customer's contact receives and approves invoices. Bayforth is represented by its "Export desk", an operations planner, for a domestic haul (Marrowdale to Lumeport); Lumeway by its sales customer service. The flow knows Lumeway's accounts department (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`; as payer it would be accounts payable).
- Condition: the contacts fit the billing roles.
- Options: (a, preferred) Bayforth's accounts receivable and Lumeway's accounts payable; (b) `AccountingContact` in the customer party and no party contacts.
- Needs decision: no
- From: broad (F4), parties (F4, F7)

### retail/16#F7 · Low · The customer's customs trader number and share capital on a domestic freight invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: the customer Lumeway carries its customs trader identifier, although the carriage is inside Bayvarra and no example of the flow is a customs document, and its share capital. Company law may require the issuer's share capital on its invoices, which is why the parties part suggested keeping it on invoices; but this is the customer's share capital, which no rule asks for on the supplier's invoice (section 4.8). `CorporateStockAmount` is defined as "The number of shares in the capital stock of a corporation" while its data type is an amount: a conflict for the UBL TC write-up, not a reason for a decision here (aligned with retail a/b).
- Condition: the customer party carries no customs identifier and no share capital.
- Options: (a, preferred) leave both out; (b) record the definition conflict for the TC write-up in any case.
- Needs decision: no
- From: parties (F5, F6), context (F3)

### retail/16#F8 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the date `1996-01-01` is shared by 25 unrelated parties of the world (parties part, lxml over `world/examples/*/*.xml`), among them Bayforth Forwarding; other parties have dates of their own. A common 1 January is a filler. Every earlier flow kept this as Low with a decision.
- Condition: Bayforth's registration date has a reason in the world's history, or is absent.
- Options: (a, preferred) its own date; (b) leave it out; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F3)

## Checked and consistent
- Arithmetic (redone in the merge): 38 KMT × 2.85 = 108.30 = line extension = tax exclusive = tax inclusive = payable; taxable 108.30, tax 0.00 at 0 %.
- Penalty: 1.5 % × 108.30 = 1.6245 → 1.62, per month from 2026-05-31, the day after the due date 2026-05-30 = issue date + 30 days ("30 days net").
- Tax: `E` with exemption `SVCB2B` "Service to a business", supply type `SERVICES`, state sales tax: a transaction-based exemption, not a party status (broad, money).
- `AdditionalDocumentReference` `BF-WB-26-0231` resolves to 13-Waybill; consignment `LD-CS-26-0228` and carrier Bayforth agree with 11 to 15; supplier Bayforth and customer Lumeway are the transport service provider and bill-to party of 11.
- RF reference `RF66BFINV260234` and account `XB40BLUM38020502618225` pass `check_ids.py` (rerun); the account is held by Bayforth Forwarding Ltd in XBL; `MPNS` is an ISO 20022 clearing channel code (broad).
- The waybill is not ad valorem (`13-Waybill.xml:/Waybill/cbc:AdValoremIndicator` = `false`), consistent with a per-kilometre freight (money).

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Bayforth Forwarding Ltd`: checked against the supplier — the holder is the supplier, so no `PayeeParty` is needed (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected misuse for a business park — refuted, the definition fits a business park and `PlotIdentification` "Plot 14" is the parcel (from parties).
- `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name`: the carrier repeats the seller — refuted, naming the carrier of the invoiced delivery lets the buyer match the invoice to the consignment (from context).
- `/Invoice/cac:PaymentMeans/cbc:InstructionNote`: repeats the RF reference — refuted, asking to quote the reference is ordinary practice (from context).

## Changed in the merge
- broad/F3, money/F1, context/F2 → F3: grouped; preferred option set to "drop" (context: the carrier has no source for the code), the outbound-freight code kept as option b.
- money/F2, logistics/F2 → F4: grouped (both ask for the booking reference; logistics adds the untyped waybill).
- broad/F4, parties/F4, parties/F7 → F6: one contacts finding per example.
- parties/F5, parties/F6, context/F3 → F7: grouped; parties/F6's "Needs decision: yes" set to no and its option "keep it here, since an invoice may legally have to show it" not followed, because the share capital here is the customer's, not the issuer's.
- context/F1 option order: drop preferred (aligned with the other parts and the earlier flows).

## Outside this review
- Whether 38 km is the road distance from Marrowdale (Upland State) to the Lumeport store on the world's map (map and route checks; broad, logistics).
