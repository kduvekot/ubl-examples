# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/26-CreditNote.xml`, Git blob `27ef7cc12dad5d613bda5ae257e7fc61371126be` (committed)
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

### sea/26#F1 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance of the business park, not a street name, and has no use in the supplier's postal address on a credit note. 79 occurrences in 76 files (`grep -rho --include='*.xml'` over `world/examples`), always Lumeway's address.
- Condition: The postal address holds no gate.
- Options: (a) preferred: drop the gate from the postal address and give it only where vehicles need it; (b) the name of the park's internal road, if it has one.
- Needs decision: no
- From: broad (F1), parties (F1)

### sea/26#F2 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: `LocaleCode` is absent or holds a locale (language and country) from a list that defines locales.
- Options: (a) preferred: drop `LocaleCode`; (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no
- From: parties (F2)

### sea/26#F3 · Medium · The seller "claims from the insurer" a 64.00 loss under a policy with a 250.00 deductible whose beneficiary is the buyer
- XPath: `/CreditNote/cbc:Note` = `Under CIF the risk was the buyer's on board; the distributor credits the frame as a goodwill gesture and claims from the insurer.`
- XPath: `/CreditNote/cac:Annotation/cbc:AnnotationContent` = `Claimed from Wavesure Cargo Insurance under policy WS-CP-26-4471.`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `64.00`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:DeductibleAmount` = `250.00`
- XPath: `14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- Why: Policy `WS-CP-26-4471` has a deductible (and excess) of 250.00 XBL and names Velumi Trading as beneficiary, with Lumeway as policy holder (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:PolicyHolderParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`). The loss is one frame at 64.00 XBL (70.40 at the usual 110 % insured value), well below the deductible, so a claim recovers nothing; and the insurance benefits the buyer, so the seller can recover only if the buyer assigns its rights, which the credit note does not say. The note and the annotation state a recovery route the policy data of the flow rule out. Broad and parties refuted the weaker suspicion that the seller cannot claim at all (under CIF the seller takes out the policy and, as holder, may claim with the buyer's consent); that argument stands, but it does not answer the deductible, which the merge verified in the bill of lading.
- Condition: The recovery the credit note states is possible under the policy data of the flow (deductible, beneficiary), or the credit note states no recovery.
- Options: (a) preferred: drop the claim from the note and the annotation; the goodwill credit stands on its own (the loss is below the deductible); (b) keep a claim and make it possible (buyer assigns its claim; no deductible for this partial loss), which changes the policy data in the bill of lading; (c) the buyer claims, and the seller does not credit.
- Needs decision: yes
- From: money (F1); broad and parties considered the seller's claim and refuted it on other grounds

### sea/26#F4 · Low · Credit on a factored invoice "settled against the next payment to the seller"
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `LD-INV-26-0147`
- XPath: `/CreditNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`
- XPath: `22-Invoice.xml:/Invoice/cac:PaymentMeans/cac:TradeFinancing/cac:Clause/cbc:Content` = `Payment to any other account does not discharge the buyer.`
- XPath: `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `64.00`
- Why: The credited invoice was assigned to Harbourline Factoring; only payment to the factor's account discharges the buyer, and the factor's statement shows the balance owed to it. There is no "next payment to the seller": the buyer's payment for this invoice goes to the factor, and that is where the credit is in fact deducted (`27-RemittanceAdvice.xml` pays 43778.00 − 64.00 = 43714.00 to `27-RemittanceAdvice.xml:/RemittanceAdvice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). The credit note names only Lumeway and Velumi and says nothing about the factor, although it reduces a receivable the factor holds; netting the seller's credit against the factor's receivable needs the factor's agreement, which no document states.
- Condition: The credit note says with whom the credit is settled, consistently with the remittance advice; where it is netted against the assigned receivable, the factor appears (in the text or as payee) and its agreement is stated.
- Options: (a) preferred: say that the credit is deducted from the payment of `LD-INV-26-0147` to Harbourline Factoring (and name the factor, e.g. as payee or in the note), matching the remittance advice; (b) Lumeway refunds the buyer itself and the remittance pays the factor the full balance (changes `27-RemittanceAdvice.xml`); (c) drop the note and rely on the billing reference.
- Needs decision: yes (who carries the credit under the factoring agreement is part of the story)
- From: broad (F2), context (F1), money (F2), parties (F3)

### sea/26#F5 · Low · The electronic-exchange agreement cited as the contract of a goodwill credit
- XPath: `/CreditNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`
- Why: `ContractDocumentReference` is "A reference to a contract associated with this document". `LD-DAG-26-0125` is the Digital Agreement between Lumeway and Velumi (`03-DigitalAgreement.xml`) on exchanging electronic documents; the credit is, by the credit note's own note, a goodwill gesture outside the sale's terms. The logistics part refuted this: the agreement under which the credit note is exchanged is a contract associated with the document. The merge keeps it as Low: that reading makes every document of the pair carry the reference, and the document whose terms matter for a credit (the sale's general terms `LD-GTC-2026`, which the order and invoice cite) is not the one referenced.
- Condition: The contract reference names the contract that governs the credit (the sale's terms, or a claims agreement), or is absent.
- Options: (a) preferred: drop it, since the credit is goodwill; (b) reference the sale's general terms `LD-GTC-2026` if a clause there covers transport damage.
- Needs decision: no
- From: broad (F3, part), context (F2); logistics considered and refuted it

### sea/26#F6 · Low · The credit line does not point to the invoice line it credits
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:ID` = `1`
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `1`
- Why: The credit note line credits one side frame, i.e. part of invoice line 2 (`22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `12`) and of receipt line 2, but carries no line-level billing reference; only the document-level reference to the invoice links it.
- Condition: The credit line references the invoice line it credits.
- Options: (a) preferred: add a line-level `BillingReference` to `LD-INV-26-0147` line 2.
- Needs decision: no
- From: broad (F3, part)

### sea/26#F7 · Low · A buyer project that appears nowhere before the claim
- XPath: `/CreditNote/cac:ProjectReference/cbc:ID` = `VT-PRJ-26-07`
- Why: `ProjectReference` is "A reference to a project associated with this document". `VT-PRJ-26-07` occurs only in this credit note and in `28-DebitNote.xml` (`grep -rl --include='*.xml' VT-PRJ-26-07 world/examples`, recounted: 2 files); neither the order nor the invoice it credits refers to a project.
- Condition: The project reference occurs from the order onwards, or not at all.
- Options: (a) preferred: drop it; (b) add it to the order and invoice if the purchase is to be tied to a Velumi project (e.g. the port's benches).
- Needs decision: no
- From: context (F3)

### sea/26#F8 · Low · Payment alternative currency and rate without an amount in that currency
- XPath: `/CreditNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`
- XPath: `/CreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The credit is settled by deduction, not paid, and the credit note gives no `PayableAlternativeAmount`; the alternative currency and its rate (without a date) have no amount to apply to. Broad and context refuted this: the invoice offers payment in Coral at the same rate, so telling the Lisavan buyer the XLC equivalent has a reason. The merge keeps it as Low: without an alternative amount the reader still has to compute it (64.00 × 0.4 = 25.600 XLC), and the deduction is made in XBL (`27-RemittanceAdvice.xml`).
- Condition: An alternative payment currency and its rate appear only with an amount in that currency, or not at all.
- Options: (a) preferred: drop both; (b) add `PayableAlternativeAmount` 25.600 XLC and the rate's date.
- Needs decision: no
- From: money (F3); broad and context considered and refuted it

### sea/26#F9 · Low · The contacts do not fit a credit for transport damage
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CreditNote/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `VT-CLAIMS`
- Why: The buyer routes the credit note to its claims unit (`VT-CLAIMS`), but the customer's contact is named Purchasing while being a customer service officer in Sales (name, title and department disagree; none is the claims or accounts payable function). The supplier's contact is its sales customer service, not receivables or claims.
- Condition: Each contact's name, job title and department agree and are the functions that handle the credit (claims / receivables at Lumeway, claims / accounts payable at Velumi, matching `VT-CLAIMS`).
- Options: (a) preferred: claims or accounts contacts on both sides; (b) drop the contacts.
- Needs decision: no
- From: broad (F4), parties (F4)

### sea/26#F10 · Low · Velumi's Lisavu address tagged en-XB and its legal form in English only
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: Velumi's English address renderings carry `languageID="en-XB"` and its legal form is in English only, without `languageID`; in the documents Velumi issues it carries `en-XL` and the legal form in Lisavan and English (`27-RemittanceAdvice.xml:/RemittanceAdvice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`). Counts over `*.xml`: `en-XL` 188, `en-XB` 141, `en-XU` 9 for English renderings of Lisavu names (parties, lxml). No rule says whether the tag follows the issuer or the place.
- Condition: One documented rule decides the tag, and Velumi's address and legal form follow it in every example.
- Options: (a) preferred: `en-XL` and the legal form in Lisavan and English everywhere; (b) keep the issuer's variety and state the convention once.
- Needs decision: yes
- From: parties (F5)

### sea/26#F11 · Low · Urvanian national tariff code on a Bayvarran credit note to a Lisavan buyer
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The credit note is issued in Bayvarra for goods exported to Lisavu; the Urvanian national tariff code (`listID` `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`) is the manufacturer's catalogue data and plays no part in either country's customs or in the credit (the HS code 732599 is already given). Copied product data (section 4.8). Counter-argument (as recorded in earlier flows' merges): the world has no Bayvarran or Lisavan tariff list, all tariff codes in the examples use the XU list, so the value may be meant as the only national code available.
- Condition: The item carries only the classifications the credit note uses.
- Options: (a) preferred: drop the XU national tariff code; (b) keep it with a stated reason.
- Needs decision: no
- From: added by the merge (no part raised it), aligned with the earlier flows' "copied XU tariff code" findings

### sea/26#F12 · Low · The side frame's GTIN lies in Lumeway's company prefix, the brand is Valdara's
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000029`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cbc:BrandName` = `Valdara`
- Why: GTINs are allocated by the brand owner from its own GS1 company prefix. The side frame is a Valdara product (brand Valdara, manufacturer Valdara Industries `XU-R-104274`), but its GTIN `9520610000029` starts with the prefix `9520610` of Lumeway's GLN `9520610900008`, i.e. the distributor's prefix. Own knowledge of the GS1 allocation rules; the check digit is valid (`check_ids.py`). The same GTIN occurs in 13 files (`grep -rl --include='*.xml'`).
- Condition: The item's GTIN comes from the brand owner's company prefix, or the world states why the distributor allocated it.
- Options: (a) preferred: a GTIN from Valdara's own prefix in every example; (b) record that Lumeway, as exclusive importer, allocated the GTINs.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail a/b/c

### sea/26#F13 · Low · World item number with a valid GS1 check digit
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000034`
- Why: The world item number (`schemeID` `urn:ubl-examples:world:item`) is 12 digits with a valid GS1 (UPC-A) check digit (recomputed: 7·3+7+1·3+0+2·3+0+0+0+0+0+3·3 = 46, check 4), so it can be read as a real GTIN-12 in a US company prefix, which the rule "fictional values must not be mistaken for real ones" excludes. The merge could not check the real GS1 register. It occurs in 22 files.
- Condition: The world item number cannot be mistaken for a real GTIN (e.g. a prefix or length GS1 does not use), or the GS1 registers are checked and record it as unassigned.
- Options: (a) preferred: a format that is not a valid GTIN; (b) check and record it in the sources.
- Needs decision: yes
- From: added by the merge (no part raised it), aligned with retail a/b/c, rail, road, plastics

## Checked and consistent
- Credit 1 × 64 = 64.00 = line extension = taxable = tax exclusive = tax inclusive = payable; tax 0.00 at category G with EXP, as on the invoice; price 64 = invoice line 2's price (`22-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `64`; 768.00 / 12).
- The quantity matches the receipt advice's rejection of one frame (`21-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[2]/cbc:RejectedQuantity` = `1`); discrepancy code 17 (transport damage) and the line note agree with the receipt line ("box crushed at the port").
- References resolve and precede the credit note (2026-06-15): invoice `LD-INV-26-0147` (2026-05-14), order `VT-PO-26-0127`, receipt advice `NW-RA-26-0146` (2026-05-21), statement `HF-ST-26-0151` (2026-06-13), digital agreement `LD-DAG-26-0125`.
- Actual delivery 2026-05-21 = receipt date in `21-ReceiptAdvice.xml`; the note on CIF risk agrees with the bill of lading (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRisk` = `Risk passes when the goods are on board the vessel in Lumeport.`); the policy in the annotation is the bill of lading's.
- The 64.00 is deducted in `27-RemittanceAdvice.xml` (43778.00 − 64.00 = 43714.00, recomputed).
- Lumeway's tax registration and share capital on its own credit note are the issuer's, as on its invoice (parties); the manufacturer of the side frame is the same as in the invoice; GLN and GTIN pass `check_ids.py` (re-run).

## Considered and refuted
- `/CreditNote/cbc:Note`: the distributor, not the buyer who bore the risk under CIF, claiming from the insurer — refuted because under CIF the seller takes out the policy and, as holder, may claim with the buyer's consent (from broad, parties). The deductible makes the claim pointless all the same: see F3.
- `/CreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `0.4` and `/CreditNote/cbc:PaymentAlternativeCurrencyCode` = `XLC`: an alternative currency on a credit note — refuted by broad and context (the XLC equivalent at the invoice's rate has a reason for a Lisavan buyer). The merge follows money and keeps it as F8 (Low), with this argument.
- `/CreditNote/cac:StatementDocumentReference/cbc:ID` = `HF-ST-26-0151`: a reference to the factor's statement without reason — refuted because the credit reduces the balance that statement reported (from context).
- `/CreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-21`: under CIF the goods are delivered on board at Lumeport (2026-05-14) — refuted because `ActualDeliveryDate` is "the actual date of delivery" and the physical delivery to the buyer's 3PL is a legitimate reading; the risk transfer is stated in the note (from logistics).
- `/CreditNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`: refuted by logistics (the agreement under which the credit note is exchanged is a contract associated with it). The merge keeps it as F5 (Low), with this argument.
- `/CreditNote/cac:OriginatorDocumentReference/cbc:ID` = `VT-CLAIM-26-0019`: no example has this ID — refuted because the buyer's claim is an internal document outside the flow, and `28-DebitNote.xml` refers to a different claim (`VT-CLAIM-26-0021`) for a different matter (from logistics).
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-041859`: the customer's customs trader number on a credit note — refuted because a credit on an imported item can bear on the customs value declared for it (from parties).

## Changed in the merge
- broad/F2, context/F1, money/F2 (no) and parties/F3 (yes) → F4: Needs decision yes, because whether the factor agrees to the set-off and who carries the credit is story; aligned with retail c (factor and credit note). Wording combined.
- broad/F3 → F5 and F6: split into the contract reference (with context/F2) and the missing line-level invoice reference; different conditions.
- F11, F12, F13: added by the merge (verified against the XML; no part raised them), to align with the earlier flows' merges where the same item data occurs.
