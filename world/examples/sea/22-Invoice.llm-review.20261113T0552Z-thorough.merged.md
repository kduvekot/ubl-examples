# LLM review: 22-Invoice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/22-Invoice.xml`, Git blob `4c08d1557efc54cdc92ff08f70f42ccd45fd61e0` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/22#F1 · High · Balance due date does not follow from "30 days net" after shipment
- XPath: `/Invoice/cbc:DueDate` = `2026-06-28`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-06-28`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:InstallmentDueDate` = `2026-06-28`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:IssueDate` = `2026-05-14`
- XPath: `25-Statement.xml:/Statement/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-06-28`
- Why: Reference event 81 is "Date of shipment as evidenced by the transport document(s)" (UNTDID 2475). The bill of lading is dated 2026-05-14 and the vessel left that day (`13-TransportationStatus.xml`); the invoice is of the same day. Merge recalculation: 2026-05-14 + 30 days = 2026-06-13 (17 days to 31 May + 13); 2026-06-28 is 2026-05-14 + 45 days; 30 days before 2026-06-28 is 2026-05-29, on which no event of the flow lies (arrival was 05-18: + 30 = 06-17). Text, reference event and due date contradict each other; the penalty period starting 2026-06-29 and the statement carry the wrong date on. Bayforth's invoice `18-Invoice.xml` with the same note is due exactly 30 days after issue.
- Condition: The balance due date (invoice, payment means, terms, statement) equals the reference event's date plus the stated net period, and the penalty period starts the day after.
- Options: (a) preferred: keep 2026-06-28 and state the term that yields it ("45 days net from shipment"), which keeps the timing of the statement and the remittance of 2026-06-25 (broad's preference); (b) keep "30 days net" and set 2026-06-13, penalty from 2026-06-14, which makes the remittance of 2026-06-25 late and changes the later documents (context's and money's preference; money said yes for that reason).
- Needs decision: no (option a is an encoding fix; option b would need one)
- From: broad (F1), context (F1), money (F2, yes)

### sea/22#F2 · High · Exchange rate and terms validity dated after the invoice was issued; two dates for the same rate
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ExchangeRate/cbc:Date` = `2026-05-18`
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ValidityPeriod/cbc:StartDate` = `2026-05-18`
- XPath: `/Invoice/cac:PaymentTerms[2]/cac:ValidityPeriod/cbc:EndDate` = `2026-07-02`
- XPath: `/Invoice/cac:PaymentAlternativeExchangeRate/cbc:Date` = `2026-05-14`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-14`
- Why: `ExchangeRate/Date` is "The date on which the exchange rate was established". An invoice issued on 2026-05-14 cannot carry a rate established on 2026-05-18; the same XBL→XLC rate 0.4 is stated in `PaymentAlternativeExchangeRate` dated 2026-05-14. The balance terms' validity also starts four days after issue (and ends 2026-07-02, inside the penalty period), leaving open what applies on 05-14 to 05-17; nothing explains it.
- Condition: No date in the invoice recording something established or valid at issue lies after the issue date; the rate is stated once, or both statements carry the same date.
- Options: (a) preferred: drop the terms' exchange rate (the payment alternative rate already serves the XLC amount) and the validity period, or date both 2026-05-14; (b) a separate terms rate only if the terms say it is fixed on a future event.
- Needs decision: no
- From: broad (F2), context (F2), money (F3)

### sea/22#F3 · High · Freight and insurance charged on top of a price agreed CIF; invoice total exceeds the confirmed order total
- XPath: `/Invoice/cac:DeliveryTerms/cbc:ID` = `CIF`
- XPath: `/Invoice/cac:AllowanceCharge[1]/cbc:Amount` = `2950.00`
- XPath: `/Invoice/cac:AllowanceCharge[2]/cbc:Amount` = `140.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount` = `3090.00`
- XPath: `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `53778.00`
- XPath: `05-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `50688.00`
- XPath: `06-OrderResponse.xml:/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `50688.00`
- Why: Under CIF (Incoterms 2020, own knowledge) the seller contracts and pays carriage and insurance to the named port, and the agreed price includes them. Order and order response, both CIF Port of Selanu at the same unit prices (520 and 64), agree 50688.00 with no charges (verified: the order's anticipated total has only line extension and payable). The invoice adds the seller's own freight 2950.00 (= 2700 + 250 on the bill of lading) and insurance 140.00 (billed to Lumeway by its forwarder, `18-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3175.00`) as charges to the buyer: 50688.00 + 3090.00 = 53778.00 (merge recalculated). The CIF term and the confirmed order total contradict the charges. The rest of the flow (statement, remittance, the bill of lading's CIF value 53778.00 and FOB 50688.00, the import declaration) follows the invoice, so which story is meant must be decided.
- Condition: The invoice total agrees with the price confirmed for the agreed delivery term: a CIF price containing freight and insurance (total 50688.00), or a term or agreement under which freight and insurance are recharged and the order/order response say so.
- Options: (a) preferred: keep CIF and the confirmed prices, drop the two charges (taxable and payable amounts, percentages and follow-up documents adjust); (b) keep the charges and let the order and order response state that freight and insurance are recharged at cost; (c) treat 50688.00 as FOB and change the delivery term throughout the flow.
- Needs decision: yes
- From: money (F1)

### sea/22#F4 · High · The bench's emission value, factor and base do not agree
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg CO2e (96 / 0.82 = 117.1); factor and base are defined as what the value is calculated from. Added by the merge (no part raised it), as in 19–21, sea d and the earlier flows.
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a) preferred: drop factor and base; (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: merge (no part raised it)

### sea/22#F5 · Medium · A language code in LocaleCode
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Invoice/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the values repeat the ISO 639 code and name no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale from a list that defines locales.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB` with a locale list.
- Needs decision: no
- From: parties (F2)

### sea/22#F6 · Medium · Gate number in AdditionalStreetName of the supplier's postal address
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." A business-park gate is a vehicle access point, not a street; an invoicing address has no use for it. 79 occurrences in 76 files, always Lumeway's address (parties, grep over `*.xml`).
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop it, giving it only where vehicles need it; (b) the park's internal road name.
- Needs decision: no
- From: broad (F3), parties (F1)

### sea/22#F7 · Medium · The factor's collection account given as the financing (line of credit) account
- XPath: `/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:FinancingFinancialAccount/cbc:ID` = `XB51BLUM38020502304038`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB51BLUM38020502304038`
- Why: `FinancingFinancialAccount` is "An internal bank account used by the bank or its first agent to manage the line of credit granted to the financing requester". The value is Harbourline's current account (type CACC) at the Bank of Lumeport, the same account the buyer is told to pay into. A collection current account into which third parties pay is not the internal account on which the factor manages the funding it granted Lumeway; valid account, wrong meaning.
- Condition: The financing account is the account on which the financing granted to Lumeway is managed, or it is absent.
- Options: (a) preferred: drop it (payee account and contract reference say where to pay and under which agreement); (b) the factor's internal client account for Lumeway with a fitting account type.
- Needs decision: no
- From: context (F3)

### sea/22#F8 · Medium · Lifecycle stage "Manufacturing" for an emission described from the mine to the factory gate
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: The code names one stage, the description covers extraction, transport and manufacturing (cradle to gate, EN 15804 A1–A3, own knowledge). Added by the merge, as in 19–21.
- Condition: Code and description name the same scope.
- Options: (a) preferred: a product-stage code or drop the code; (b) narrow the description.
- Needs decision: no
- From: merge (no part raised it)

### sea/22#F9 · Medium · "Cradle to gate" in an element that says whether transport equipment is full
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty …"; a footprint boundary is another concept. Added by the merge (TC write-up), as in 19–21.
- Condition: The element is absent from the item's footprint, or holds a fullness indication.
- Options: (a) preferred: drop it; (b) record the missing boundary element for the UBL TC.
- Needs decision: no
- From: merge (no part raised it)

### sea/22#F10 · Low · The contacts on the factored invoice do not fit their roles
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/Invoice/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Department` = `Sales`
- Why: The accounting customer's contact is named Purchasing but is a customer service officer in Sales (none is accounts payable, which receives an invoice); the warehouse's Goods inwards contact is also a customer service officer in Sales; the supplier's contact is its sales customer service, while with the receivable assigned payment questions go to the factor. The factor's contact serves its client accounts, but the factor's client is Lumeway, not the debtor Velumi; a debtor collections function fits the payee role.
- Condition: Each contact's name, title and department agree, and the accounting customer's and payee's contacts deal with this invoice and its payment.
- Options: (a) preferred: accounts payable at Velumi, debtor collections at Harbourline; (b) drop contacts that do not serve the invoice.
- Needs decision: no
- From: broad (F5), parties (F3)

### sea/22#F11 · Low · Lisavu addresses tagged as Bayvarran English, legal forms in English only
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: Velumi's and Nalevi's English renderings carry `en-XB` and their legal forms are English only, untagged; Velumi in its own remittance advice for this invoice, and Nalevi in `21-ReceiptAdvice.xml`, use `en-XL` and the legal form in Lisavan and English. The tag follows the issuer, not the place (counts over `*.xml`: `en-XL` 188, `en-XB` 141, `en-XU` 9 for English street/town renderings in Lisavu addresses; parties, lxml).
- Condition: The same rendering carries the same `languageID` everywhere, under one documented rule; legal forms in the same languages.
- Options: (a) preferred: `en-XL` and the legal form in both languages everywhere; (b) keep the issuer's locale and record the convention.
- Needs decision: yes (one world rule; parties said no, aligned with 16, 20, sea a/d and earlier flows)
- From: parties (F4)

### sea/22#F12 · Low · The factor's tax registration and the warehouse's legal entity in the invoice
- XPath: `/Invoice/cac:PayeeParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1233699`
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41722`
- Why: The factor only receives the payment; its sales-tax registration has no bearing on the tax of a supply between Lumeway and Velumi (taxed as export, category G). The delivery party is named to say where the goods went; its full legal entity adds nothing. Both come from master data (section 4.8). The supplier's own share capital was refuted (issuer's business-letter data, as in retail).
- Condition: The payee carries no tax scheme and the delivery party no legal entity, unless the invoice has a reason for them.
- Options: (a) preferred: drop them; (b) keep them with a stated reason.
- Needs decision: no
- From: parties (F5)

### sea/22#F13 · Low · Balance due from the shipment date, but no shipment date or transport document in the invoice
- XPath: `/Invoice/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Invoice/cac:PaymentTerms[2]/cbc:ReferenceEventCode` = `81`
- Why: The balance terms run from the "date of shipment as evidenced by the transport document(s)", but the invoice neither references the bill of lading `TOL-BL-26-0139` (shipped on board 2026-05-14) or the despatch advice `LD-DA-26-0145`, nor gives the shipment date in its `Delivery` (which holds only the delivery party). The buyer, and the factor collecting the receivable, cannot see when the term starts (see F1).
- Condition: The invoice states the shipment date and refers to the transport document the term is based on.
- Options: (a) preferred: `Delivery/ActualDeliveryDate` 2026-05-14 with the Lumeport location (under CIF delivery is on board) and an `AdditionalDocumentReference` to `TOL-BL-26-0139` typed as bill of lading; (b) a `DespatchDocumentReference` to `LD-DA-26-0145` plus the date.
- Needs decision: no
- From: logistics (F1)

### sea/22#F14 · Low · Real-time net settlement channel with a non-urgent service level
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTNS`
- XPath: `/Invoice/cac:PaymentMeans/cbc:ServiceLevelCode` = `NURG`
- Why: ISO 20022 `RTNS` is a real-time net settlement system; `NURG` asks for a non-urgent payment, which ISO 20022 describes as typically an ACH or low-value transaction (own knowledge), i.e. what `18-Invoice.xml` does with `MPNS`. Broad saw a contradiction. Context and money refuted it: the service level concerns the execution priority requested from the bank, not the settlement mechanism, and the combination is valid. The merge can neither confirm nor refute it with certainty (the names of the ISO 20022 internal codes are an open source in CLAUDE.md), so it stays Low with a decision.
- Condition: Channel and service level fit each other, or the combination is recorded as intended.
- Options: (a) preferred: `MPNS` with `NURG`, as in `18-Invoice.xml`; (b) `RTNS` without the non-urgent level; (c) keep both and record that they are compatible.
- Needs decision: yes
- From: broad (F4); context and money refuted it (argument above)

### sea/22#F15 · Low · Catalogue and product-passport data copied into the invoice line
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: The bench's invoice line carries the whole catalogue item (keywords, sales conditions, load test, colour options, emissions with the errors of F4, F8, F9, circularity profile, product documentation). An invoice identifies what is billed and on what terms; accounts payable does nothing with these. The side-frame line does without them.
- Condition: The invoice item carries what identifies and classifies the billed item, and data with a billing or tax reason.
- Options: (a) preferred: reduce the bench's item to identification, name, description, classification and origin.
- Needs decision: no
- From: broad (F6), context (F4)

### sea/22#F16 · Low · GTINs in the distributor's GS1 company prefix, not the manufacturer's
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- Why: Valdara's bench and side frame carry GTINs in `9520610`, the prefix of Lumeway's GLN `9520610900008`; under GS1 rules the brand owner allocates the GTIN (own knowledge). Added by the merge, as in 19–21, sea d and retail.
- Condition: The GTINs are in the brand owner's prefix, or the world states that Lumeway is the brand owner.
- Options: (a) preferred: GTINs in Valdara's prefix; (b) record Lumeway as brand owner.
- Needs decision: yes
- From: merge (no part raised it)

### sea/22#F17 · Low · World item numbers with valid GS1 check digits
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: Both carry a valid GTIN-12 check digit (merge recalculated: 7 and 4) in prefix 077 (GS1 US range; own knowledge), so they can be mistaken for real GTINs. Added by the merge, as in 19–21.
- Condition: The world item numbers cannot be read as valid GTINs, or the convention is recorded.
- Options: (a) preferred: a non-GTIN format; (b) record the convention.
- Needs decision: yes
- From: merge (no part raised it)

## Checked and consistent
- Lines and totals (merge recalculated): 96 × 520 = 49920.00; 12 × 64 = 768.00; 50688.00 + 2950.00 + 140.00 = 53778.00 tax exclusive = inclusive (tax 0.00); prepaid 10000.00; payable 43778.00; alternative 43778.00 × 0.4 = 17511.200 XLC (broad, context, money).
- Percentages 10000 / 53778 = 18.59 %, 43778 / 53778 = 81.41 %, sum 100 %; penalty 1.5 % × 43778.00 = 656.67; deposit due 2026-05-09 (event 8, the day after the order response 05-08), paid 05-08, received 05-09 (broad, context, money).
- Prices equal the catalogue's XLC prices at 0.4 (208 / 0.4 = 520; 25.6 / 0.4 = 64) (money).
- Freight 2950 = 2700 + 250 and insurance 140 agree with `14-BillOfLading.xml`, whose insured value is 53778 × 1.1 = 59155.80 and declared customs (CIF) value 53778.00; terminal handling at Selanu (185.00, collect from the consignee) correctly not invoiced (broad, logistics).
- Tax: category G with reason EXP on lines, charges and subtotal fits a CIF export to Lisavu (broad, money).
- Factoring: type 393, assignment note, payee, payee account `XB51BLUM38020502304038` in Harbourline's name, financing party, discharge clause, remittance routed to Harbourline; the same account and RF `RF20LDINV260147` in statement and remittance advice; `check_ids.py` passes (broad, money, parties).
- References and parties: order `VT-PO-26-0127` lines 1 and 2; quantities as despatch, receipt and import declaration; supplier/seller Lumeway, customer/buyer Velumi, originator/beneficiary Port of Selanu as in the order; delivery party Nalevi as order and B/L notify party; issued 2026-05-14 12:32 after the bill of lading (10:54) (logistics, parties).

## Considered and refuted
- `/Invoice/cac:AllowanceCharge[2]/cbc:AllowanceChargeReasonCode` = `96`: an insurance charge coded from UNCL 5189 while freight uses 7161 — refuted: 5189 is "Allowance or charge identification" and 96 Insurance is in it; 7161 has no code for cargo insurance itself; mixed lists are a style question (from broad, context, money).
- `/Invoice/cac:PaymentMeans/cac:CreditAccount/cbc:AccountID` = `HF-CL-VT-001`: a credit account in a credit transfer — refuted: the factor's ledger account for the debtor helps matching (from broad, money).
- `/Invoice/cac:PaymentMeans/cac:RemittanceDocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Harbourline Factoring`: remittance to the factor — refuted: under the assignment the factor receives the payment (from broad).
- `/Invoice/cbc:IssueDate` = `2026-05-14`: invoice before arrival — refuted: under CIF the seller invoices on shipment (from broad).
- `/Invoice/cac:PaymentMeans/cbc:ServiceLevelCode` = `NURG`: refuted by context and money (priority, not settlement mode) — not followed fully: kept as F14 Low/yes with their argument (from context, money).
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`: share capital on an invoice — refuted for the issuer: company law often requires the issuer's share capital on business documents (from parties).
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`: the customer's customs trader number — refuted: the commercial invoice supports that trader's import declaration (from parties).
- `/Invoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: the port as originator although Velumi ordered — refuted: the order names the port in that role (from parties).

## Changed in the merge
- Added by the merge: F4 (emission triple, High), F8 (MANUFACTURING), F9 (CRADLETOGATE), F16 (GTIN prefix), F17 (world item numbers), aligned with 19–21, sea d and the earlier flows.
- broad/F1, context/F1, money/F2 → F1: combined; money's Needs decision yes set to no, with the preferred option that keeps the later documents' timing (broad's); context/money's option kept as (b), which would need a decision.
- broad/F2, context/F2, money/F3 → F2: combined.
- broad/F4 → F14: Needs decision no → yes, because context and money refuted it and the merge cannot settle it.
- parties/F4 Needs decision no → yes (F11), aligned with the earlier flows.
- Combined: broad/F3 + parties/F1 → F6; broad/F5 + parties/F3 → F10; broad/F6 + context/F4 → F15.

## Outside this review
- `25-Statement.xml` repeats the due date 2026-06-28 and the follow-up documents depend on it and on the 53778.00 total; whichever option F1 and F3 take, they need to follow (merge).
