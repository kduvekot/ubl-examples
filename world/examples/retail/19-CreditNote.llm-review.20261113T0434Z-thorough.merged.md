# LLM review: 19-CreditNote.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/19-CreditNote.xml`, Git blob `9b6d800a81b90bc85d34fe3b9f8eee00a89ced1c` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
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

### retail/19#F1 · High · Emission factor times base does not give the stated emission
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", `ValueBaseMeasure` "The base quantity to which the value factor applies". Recomputed: 0.82 × 1 EA = 0.82 ≠ 96 kg; 96 / 0.82 = 117.1. Same triple in 39 XML files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueMeasure` = `ValueFactorNumeric` × `ValueBaseMeasure`, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) a factor and activity that give 96 kg; (c) drop the emission from the credit note (context; see F14).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### retail/19#F2 · Medium · The factor as payee of a credit that is owed to the buyer
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `494.00`
- Why: `PayeeParty` is "The Party who receives the Payment". The 494.00 of a credit note is owed by the seller to the buyer: if anything is paid under it, Brightmarket receives it (a refund); if it is set off, nobody receives a payment. Naming the factor as payee says Harbourline receives 494.00, the opposite direction; the payee looks copied from the factored invoice (`18-Invoice.xml:/Invoice/cbc:InvoiceTypeCode` = `393`; `18-Invoice.xml:/Invoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Harbourline Factoring`). The note sets the credit off "against the next payment to the seller", while under the factoring Brightmarket pays the invoice to Harbourline, so the note and the payee describe two different settlements and neither says whether Brightmarket may deduct 494.00 from the 11856.00 it owes Harbourline. Attempted refutation: the factor could handle refunds for its client; nothing in the flow says so. Cotton's merge had Medium/no for a payee on a plain set-off credit note; here three parts said "yes" because how a credit on an assigned receivable is settled (and who is told) is part of the factoring story.
- Condition: the credit note states one way of settling the credit that fits the factoring (who deducts or refunds the 494.00, against which payment), and a payee, if present, is a party that receives money under it.
- Options: (a, preferred) drop `PayeeParty` and say in the payment terms that the credit is deducted from the payment of `LD-INV-26-0236` to Harbourline Factoring (usual handling of a credit on a factored invoice, own knowledge); (b) Brightmarket as the refund's payee, if a refund is intended; (c) keep Harbourline only if the world's factoring agreement makes the factor handle refunds, and say so.
- Needs decision: yes
- From: broad (F2), money (F1), parties (F3), context (F2)

### retail/19#F3 · Medium · A language code in LocaleCode
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:PayeeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` is the language code itself and names no locale. 362 occurrences in 213 XML files (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`; `grep -rl` for the files; recounted in the merge).
- Condition: no `LocaleCode` holds a bare language code; where present it identifies a locale from a list of locales.
- Options: (a, preferred) drop it; (b) `en-XB` from a locale list (context preferred this).
- Needs decision: no
- From: broad (F3), parties (F1), context (F3, the LocaleCode half)

### retail/19#F4 · Medium · A site gate as additional street name in Lumeway's postal address
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". "Gate 3" is a vehicle entrance, not a street name. 79 occurrences in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<' world/examples | wc -l`).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address; (b) record it in Bayvarra's address format (finding then dismissed).
- Needs decision: no
- From: broad (F4), parties (F2)

### retail/19#F5 · Medium · A system-boundary code in FullnessIndicationCode
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty"; "Cradle to gate" is a life-cycle system boundary from another list (39 XML files, `grep -rl --include='*.xml' 'CRADLETOGATE' world/examples | wc -l`). TC write-up candidate (no boundary element in UBL).
- Condition: no system-boundary code in `FullnessIndicationCode`.
- Options: (a, preferred) drop it and record the missing element for the TC write-up.
- Needs decision: no
- From: context (F3, the FullnessIndicationCode half)

### retail/19#F6 · Medium · Lifecycle stage "Manufacturing" for an emission from ore to factory gate
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; the description covers EN 15804 stages A1–A3 (own knowledge), the code only manufacturing. Added by the merge, aligned with retail a/b and road/rail/air.
- Condition: the code covers the stages the description names, or is absent.
- Options: (a, preferred) omit the code; (b) one emission per stage.
- Needs decision: no
- From: added by the merge

### retail/19#F7 · Low · Contacts that do not fit the billing roles
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CreditNote/cac:PayeeParty/cac:Contact/cbc:Name` = `Client accounts`
- XPath: `/CreditNote/cac:PayeeParty/cac:Contact/cbc:JobTitle` = `Client relationship manager`
- Why: the order names both accounts contacts (`08-Order.xml:/Order/cac:SellerSupplierParty/cac:AccountingContact/cbc:Name` = `Accounts receivable`, `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:AccountingContact/cbc:Name` = `Accounts payable`); the credit note uses Lumeway's sales customer service and Brightmarket's buying office, whose job title and department contradict its name. Harbourline's contact faces its client (the seller), not the debtor that reads the payee here.
- Condition: the accounting parties' contacts are their accounts departments, with consistent name, job title and department; a payee contact (if the payee stays, see F2) is debtor-facing.
- Options: (a, preferred) as in the order; collections for Harbourline if it stays.
- Needs decision: no
- From: broad (F6), parties (F7, F8, F11)

### retail/19#F8 · Low · Party master data the credit note does nothing with
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: crediting one damaged bench uses neither Lumeway's customs trader number (domestic flow without customs), nor the customer's share capital, nor Brightmarket's consumer web shop and social media (section 4.8). `CorporateStockAmount`'s definition ("The number of shares in the capital stock of a corporation") against its Amount type is a TC write-up note, not a decision here (as retail a/b). Lumeway's own share capital: see Refuted in the merge.
- Condition: the parties carry only data the credit note uses.
- Options: (a, preferred) leave these out.
- Needs decision: no
- From: parties (F5, F6, F9), context (F4, part)

### retail/19#F9 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/CreditNote/cac:PayeeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: shared by 25 unrelated parties of the world (parties part, lxml), among them Harbourline Factoring; a filler. Every earlier flow kept it as Low with a decision.
- Condition: Harbourline's registration date has a reason in the world's history, or is absent (and with F2 option a the payee party goes altogether).
- Options: (a, preferred) its own date; (b) omit it; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes
- From: parties (F10)

### retail/19#F10 · Low · "Carton torn", while the despatch advice and the item data describe no cartons
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:Note` = `Bench refused: armrest bent, carton torn.`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- Why: the despatch advice this credit note references declares only the pallet as package for the damaged pallet, and the item's packaging waste is stretch film and straps; the credit note repeats the "carton" of 17-ReceiptAdvice. The logistics part rated it Medium; lowered to Low (as 17/F12) because 12's four packages per pallet (`12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cbc:TotalPackageQuantity` = `4`) admit the carton reading.
- Condition: the packaging named in the credit note is the packaging the despatch advice and item data declare.
- Options: (a, preferred) declare the four cartons in 12 and keep the text; (b) "stretch film torn" or no packaging detail, here and in 17.
- Needs decision: no
- From: broad (F5), logistics (F2)

### retail/19#F11 · Low · A payment purpose on a credit that is settled by set-off
- XPath: `/CreditNote/cac:CreditNoteLine/cbc:PaymentPurposeCode` = `GDDS`
- Why: `PaymentPurposeCode` is "A code signifying the business purpose for this payment" (ISO 20022 GDDS, purchase or sale of goods). The credit note has no payment means and settles the credit by deduction from the next payment; the invoice it corrects carries no purpose code. The context part refuted this (the code describes the underlying transaction, which holds for a refund or a set-off alike, and "unless refunded" leaves a refund possible); the merge keeps it as Low because no payment is made under the credit note as written, and a purpose code on the credit alone, not on the invoice, has no use in the flow.
- Condition: the line carries a payment purpose only if a payment (a refund) is made under the credit note.
- Options: (a, preferred) drop it; (b) keep it together with a refund by credit transfer, if F2 is resolved with a refund.
- Needs decision: no
- From: money (F2); context (Considered and refuted)

### retail/19#F12 · Low · Valdara's GTIN is in Lumeway's GS1 company prefix
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `9520610900008`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `9520610000012`
- Why: the GTIN of Valdara's bench is under Lumeway's company prefix 9520610; under GS1 rules the brand owner allocates the GTIN from its own prefix (own knowledge). Check digits correct.
- Condition: Valdara's GTINs and Lumeway's keys are under different prefixes, or the story says Lumeway allocated them.
- Options: (a, preferred) a prefix of Valdara's own; (b) state the distributor's allocation in the story.
- Needs decision: yes
- From: parties (F4)

### retail/19#F13 · Low · The world item number has the form and check digit of a GTIN
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:AdditionalItemIdentification/cbc:ID` = `771020000027`
- Why: twelve digits with a valid GS1 check digit (7, computed in the merge), so it reads as a GTIN-12 with prefix 07 (US/Canada, own knowledge). Added by the merge, as retail a, rail, road and plastics.
- Condition: the world item number cannot be mistaken for a real GTIN, or its form is recorded as deliberate.
- Options: (a, preferred) a format that is not a valid GTIN; (b) record the choice in the scheme.
- Needs decision: yes
- From: added by the merge

### retail/19#F14 · Low · The item's catalogue data copied into the credit note line
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/CreditNote/cac:CreditNoteLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a credit note identifies what is credited; footprint, circularity profile, load test, dimensions and Urvania's customs tariff code (domestic sale) are catalogue data it does not use (IND5/IND6).
- Condition: the credited item carries its identifiers and tax category.
- Options: (a, preferred) drop the catalogue data.
- Needs decision: no
- From: broad (F7), context (F4, part)

## Checked and consistent
- Arithmetic (redone): 1 × 520.00 = 520.00; promotion support 5 % × 520.00 = 26.00, the invoice's rate; 520.00 − 26.00 = 494.00 = tax exclusive = taxable = payable; tax 0.00; equal to the invoice's net price per bench, 11856.00 / 24 = 494.00.
- References: invoice `LD-INV-26-0236` (issue date 2026-04-30, line 1), order line 1, despatch line 1 and receipt line 1 resolve to 18, 08, 12 and 17; credited quantity 1 = rejected quantity of 17; discrepancy code 17 (UNTDID 4465 "Transport damage") agrees with 17's reject reason; the line's actual delivery date 2026-04-30 is 17's receipt date; issued 2026-05-02, after 17 and 18.
- Tax `E` "sale for resale", STT, supply type goods, as on the invoice line; buyer's accounting code 6120 as in 08 and 18.
- Under DDP the transport risk is the seller's, so the seller crediting the damaged bench is consistent (money, own knowledge of Incoterms).
- GS1 keys pass `check_ids.py` (rerun).

## Considered and refuted
- `/CreditNote/cac:DiscrepancyResponse/cbc:ReferenceID` = `1`: an unclear reference — refuted, it points to line 1, the only line of the credit note and of the invoice (from broad).
- `/CreditNote/cac:AccountingCustomerParty/cac:Party/cbc:LogoReferenceID` = `BM-LOGO-2024`: copied master data — refuted, a credit note may be rendered with the parties' logos (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: refuted, the definition fits a business park (from parties).
- `/CreditNote/cac:CreditNoteLine/cbc:AccountingCost`: repeats the header's cost centre — refuted, a line-level cost centre identical to the header is harmless and common (from context).
- `/CreditNote/cac:CreditNoteLine/cbc:PaymentPurposeCode`: refuted by the context part (the code describes the underlying sale); the merge disagrees and keeps it as F11 (from context).

## Refuted in the merge
### parties/F6 (Lumeway's half) · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- The part's finding (both parties' share capital): UBL defines `CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount and the value is a sum in XBL; a conflict between definition and data type for the TC write-up. Condition: share capital no longer in `CorporateStockAmount`, or recorded as a finding against the definition and kept on purpose. Options: record it, keep it where a document needs it (invoices); keep it here. Needs decision: yes.
- Refuted because (for the issuer's own share capital): the credit note is Lumeway's own commercial document, where company law commonly requires its share capital, as on its invoice (the part's own option keeps it here), and an Amount-typed element can hold nothing but an amount. The definition conflict stays as a TC note in F8; the customer's share capital is part of F8.

## Changed in the merge
- broad/F2, money/F1, parties/F3, context/F2 → F2: grouped; "Needs decision" yes (three parts; context said no).
- context/F3 → F3 and F5: split (LocaleCode / FullnessIndicationCode).
- F6 (MANUFACTURING) and F13 (world item number): added by the merge, aligned with retail a/b.
- broad/F6, parties/F7, F8, F11 → F7: one contacts finding per example.
- parties/F5, F6 (customer half), F9, context/F4 (party part) → F8; parties' "yes" set to no.
- logistics/F2 → F10: Medium lowered to Low, grouped with broad/F5 (as 17/F12).
- money/F2 → F11: kept although context refuted it; both arguments carried.
- broad/F7, context/F4 (item part) → F14: item data separate from party data.

## Outside this review
- Whether 12-DespatchAdvice should state what its four packages per pallet are (bears on F10) is for 12's review.
