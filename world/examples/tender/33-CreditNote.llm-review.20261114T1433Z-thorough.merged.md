# LLM review: 33-CreditNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/33-CreditNote.xml`, Git blob `fedb04ee2964c2e08e60565d54f4c570247bdfda` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/33#F1 · High · Two different statements of how the credit is settled; the flow follows neither literally
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PaymentTerms/cbc:Note` = `Set off against the next release's invoice.`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`
- Why: The document says the credit is settled against the next payment to the seller; line 1 says against the next release's invoice; line 2 says nothing. On 4 April the next payment to the seller is that of this release's unpaid invoice (due 30 April); no next release's invoice exists in the flow. The reminder and the remittance advice set the credit off against this release's invoice: `35-Reminder.xml:/Reminder/cac:ReminderLine[2]/cbc:CreditLineAmount` = `515.20`, `36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `515.20` with `36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cac:BillingReference/cac:CreditNoteDocumentReference/cbc:ID` = `VI-CN-26-0222`. The line's statement is contradicted by the document's own term and by what both parties do.
- Condition: The credit note states one way of settlement, and it is the one 35 and 36 apply (deduction from the payment of VI-INV-26-0221).
- Options: (a) drop the line-level payment terms and word the document-level note as "Deducted from the payment of invoice VI-INV-26-0221." (preferred, all three parts); (b) keep "next release's invoice" and take the credit out of 35 and 36, which changes their amounts.
- Needs decision: no
- From: broad (F1), money (F1), context (F2)

### tender/33#F2 · High · The credited bench is the grey variant; the release was moss green
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: The credit is for one bench of delivery CL-DA-26-0215 (`/CreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `CL-DA-26-0215`), of which `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.` The credited bench is described as grey.
- Condition: The credited item's variant and colour are those delivered (moss green).
- Options: (a) the green variant, as in the corrected despatch advice and invoice (preferred); (b) no colour data.
- Needs decision: no
- From: broad (F3), logistics (F1), context (F1)

### tender/33#F3 · High · The pricing currency is the ferra; the prices are in lume and the ferra price is the "alternative"
- XPath: `/CreditNote/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Price/cbc:PriceAmount` = `18`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount` = `49900`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for prices in the Credit Note". Both prices are in XBL; the ferra price appears only as `AlternativeConditionPrice`, "The price expressed in terms other than the actual price", the reverse of what the pricing currency says; line 2 has no ferra price. Two values of the document contradict each other, as in 32 (F6).
- Condition: Every `Price/PriceAmount` is in the pricing currency; a price in another currency, if shown, is the alternative; both lines alike.
- Options: (a) drop `PricingCurrencyCode`, its rate and the alternative price (preferred by money and context, since the contract prices are in lume; as 32); (b) prices 49900 and 1800 XUF, with the lume price as alternative or not at all (broad).
- Needs decision: no
- From: broad (F2), money (F2), context (F3)

### tender/33#F4 · High · Emission factor × base does not give the emission value
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg; 96 / 0.82 = 117.07. 39 files carry factor 0.82.
- Condition: factor × base = value, or factor and base are absent.
- Options: (a) drop factor and base (preferred); (b) a real factor and its activity.
- Needs decision: no
- From: broad (F5), logistics (F2)

### tender/33#F5 · Medium · The credited installation "collected for" the tax representative
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: `CollectedForParty` is "The Party on whose behalf this item or amount is collected": a third party for whom the supplier bills an amount it passes on. Line 2 credits the installation of one bench (18.00), a service Valdara bills in its own name and its subcontractor Saltmere Engineering performs (`22-AwardedNotification.xml:/AwardedNotification/cac:TenderResult/cac:SubcontractTerms/cbc:Description` = `Saltmere Engineering installs the benches (lot 2) as subcontractor, at the tender's price of 18 lume a bench.`). Bayforth Forwarding is, in this document, the tax representative (`/CreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`) and in 27 the freight forwarder; the invoice's installation line names no such party. If the withholding tax is meant, a tax the customer withholds is not an amount collected on someone's behalf by the supplier, and not for a forwarder.
- Condition: `CollectedForParty` is present only where the line's amount is collected on behalf of a third party, and names that party.
- Options: (a) remove it (preferred, all parts); (b) a story in which Valdara collects an amount for Bayforth.
- Needs decision: yes (who Bayforth Forwarding is in this flow: forwarder, tax representative, collecting agent)
- From: broad (F4), parties (F3), context (F6)

### tender/33#F6 · Medium · "By the manufacturer's installers" although the award has a subcontractor install
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: The tender (`15-Tender.xml:/Tender/cac:SubcontractorParty/cac:PartyName/cbc:Name` = `Saltmere Engineering`) and the award (F5's quotation; the same text in 21, 23 and 24) have the Bayvarran subcontractor install. Medium, as in 32 (F8): the phrase can be read as installers engaged by the manufacturer, so it is not a hard contradiction (context rated High, parties Medium).
- Condition: The description does not attribute the work to another party than the tender and award name, in both language versions.
- Options: (a) "by the supplier's installation subcontractor", or no statement of who installs (preferred); (b) remove the subcontractor from the tender and award (changes the story).
- Needs decision: no
- From: parties (F4), context (F4), broad (F3)

### tender/33#F7 · Medium · Invoice periods on a credit note for one invoice, one of them a bare start date
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-03-31`
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:EndDate` = `2026-04-04`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:InvoicePeriod/cbc:StartDate` = `2026-04-02`
- Why: At document level `InvoicePeriod` "Associates the Credit Note with Invoicing Periods rather than with a specific Invoice". This credit note is associated with a specific invoice (F1's billing reference), so the definition's condition is not met; the period merely spans invoice date to credit note date, and the sale is not billed by period. On line 1, "An invoice period to which this credit note line applies" holds a start date only (2 April, presumably the day the damage was found), an event, not a period.
- Condition: A document-level invoice period is present only on a credit note that credits a period; the line carries no period that is an event date.
- Options: remove both periods and give the damage date in a note or as the issue date of the damage report reference (preferred, all parts).
- Needs decision: no
- From: money (F3), logistics (F3), context (F5), broad (F8)

### tender/33#F8 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: "A code signifying whether a piece of transport equipment is full, partially full, or empty. …" The value is a footprint system boundary for a bench.
- Condition: The element holds a fullness of transport equipment or is absent.
- Options: (a) remove it, keep the boundary in the lifecycle stage description (preferred); (b) in addition, record the missing boundary element for the TC write-up.
- Needs decision: no
- From: context (F7)

### tender/33#F9 · Medium · A province in `Region`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province belongs in `CountrySubentity`. 219 occurrences in 104 files.
- Condition: The province is in `CountrySubentity`.
- Options: move it to `CountrySubentity` (preferred); or record a postal-region convention.
- Needs decision: no
- From: broad (F6), parties (F1), context (F8)

### tender/33#F10 · Medium · A language code as locale
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code. 362 occurrences in 213 files.
- Condition: No `LocaleCode` holds a bare language code.
- Options: (a) remove it (preferred by parties and context); (b) a real locale from a locale list (broad).
- Needs decision: no
- From: broad (F6), parties (F2), context (F9)

### tender/33#F11 · Medium · The department described as a company in a commercial register, with a liquidation status
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: A municipal department (ISIC 8411) has no liquidation status and is not in a commercial register as a company; the register number itself is not questioned.
- Condition: The department carries no liquidation status, and its register is not typed as commercial.
- Options: (a) drop the status and type the register neutrally (preferred); (b) reduce the legal entity to name and identifier.
- Needs decision: no
- From: parties (F9), context (F13), broad (F9)

### tender/33#F12 · Low · The credit note does not say why it credits; a sub-line of 180.00 under a line of 499.00
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:DocumentReference/cbc:ID` = `PWD-DMG-26-0081`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:LineExtensionAmount` = `499.00`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cac:Item/cbc:Name` = `Side frames of the bench`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount` = `180.00`
- Why: A credit note is "A document used to specify credits due to the Debtor from the Creditor". It credits one bench and one installation in full but has no note or discrepancy response; that a bench was damaged can only be guessed from "DMG" in an untyped reference. `SubCreditNoteLine` is "A class defining one or more Credit Note Lines detailing the credit note line"; the one sub-line, "Side frames of the bench", carries 180.00 without quantity or price, and nothing says how it relates to the 499.00 (the damaged part, its repair value?); 319.00 is not detailed.
- Condition: The credit note states its reason; sub-lines add up to their line, or state what their amount is.
- Options: (a) a note or `DiscrepancyResponse` (e.g. "Bench 17 of Harbour park damaged in transport; bench and its installation credited"), and the sub-line removed or completed so the sub-lines sum to 499.00 (preferred); (b) at least the note.
- Needs decision: no
- From: broad (F7), money (F4), context (F10)

### tender/33#F13 · Low · Tax and payment currency ferra, but no ferra tax total, and no payment
- XPath: `/CreditNote/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/CreditNote/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:PaymentExchangeRate/cbc:Date` = `2026-04-04`
- Why: `TaxCurrencyCode` is "A code signifying the currency used for tax amounts in the Credit Note"; the only tax total is in lume, whereas the invoice has a second total in ferra that this credit should reduce (49900 under G, 1800 under O). A payment currency and payment rate are given for a credit that by its own terms is deducted, not paid.
- Condition: A tax total in the tax currency mirrors the lume one, as on the invoice, or there is no tax currency; payment currency and rate only if the credit is paid out.
- Options: (a) add the XUF tax total with two subtotals and remove the payment currency and rate (preferred); (b) remove all currency codes and rates if the lume is the only currency.
- Needs decision: no
- From: money (F5), broad (F8)

### tender/33#F14 · Low · The buyer's forward exchange contract on the seller's pricing rate
- XPath: `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- Why: As 32 (F14): the buyer's forward purchase of ferra, dated before the procedure, cited by the seller on a pricing rate that, with prices in lume (F3), has nothing to convert.
- Condition: As 32/F14.
- Options: as 32/F14; decided together.
- Needs decision: yes
- From: broad (F9), money (F5), context (F3)

### tender/33#F15 · Low · The withholding tax reversed has no subtotal, category or scheme
- XPath: `/CreditNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.80`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.80`
- Why: On the invoice the withholding is specified (720.00, 10 %, "Withholding tax on services of non-residents"). The credit note reverses 1.80 with a bare amount: neither base (18.00), rate nor tax is given.
- Condition: The withholding total has a subtotal with taxable amount, rate and the invoice's scheme.
- Options: add the subtotal (18.00, 10 %, same category and scheme as 32) (preferred).
- Needs decision: no
- From: money (F6)

### tender/33#F16 · Low · A tax representative with nothing to represent
- XPath: `/CreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: As 32 (F15): register number and name only, no tax registration; the credit note carries Urvanian VAT at 0 % and the reversal of a tax the customer withholds, nothing the seller owes in Bayvarra.
- Condition: As 32/F15.
- Options: as 32/F15; decided together.
- Needs decision: yes
- From: broad (F9), money (F7), parties (F10), context (F12)

### tender/33#F17 · Low · References that do not say what they refer to
- XPath: `/CreditNote/cac:WorkReportDocumentReference/cbc:ID` = `VI-WR-26-0080`
- XPath: `/CreditNote/cac:PurchaseReference/cbc:ID` = `PARK-HB`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PurchaseReference/cbc:ID` = `PARK-HB-B17`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:DocumentReference/cbc:ID` = `PWD-DMG-26-0081`
- Why: The line's document reference has only an ID (presumably the department's damage report, which the despatch note asked for). The work report (whose work, when? the bench was not installed) has no date or type. The purchase references ("a reference to an object … to which this Credit Note relates") are bare IDs, presumably Harbour park and bench position 17; no other example uses them (`grep -c PARK-HB` over `world/examples/*/*.xml`: this example only). That a work report and purchase references are the right elements was confirmed by broad and context; what is missing is what they are.
- Condition: Each reference says what it refers to (type, date or description).
- Options: `cbc:DocumentType` "Damage report" with issue date; a type for the work report; `cbc:Description` on the purchase references (preferred).
- Needs decision: no
- From: logistics (F4)

### tender/33#F18 · Low · Programme code differs from the procurement documents
- XPath: `/CreditNote/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: The programme is `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in the procurement documents; as 32 (F19).
- Condition: One code for the programme throughout the flow.
- Options: as 32/F19.
- Needs decision: no
- From: logistics (F5)

### tender/33#F19 · Low · Originator and beneficiary on line 1 repeat the accounting customer
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- Why: `OriginatorParty` ("The Party who originates the Order to which the Credit Note is related") and `BeneficiaryParty` ("A Party for whom the associated transaction is ultimately intended") repeat the accounting customer on one line only; they would say something if another unit had originated the order or benefited. Counter-argument (parties, broad): neither definition has an "if different" condition, and the department did order the bench and receive the credit. Kept Low, aligned with the other tender merges ("roles all filled with the contracting party: Low, no").
- Condition: Line-level originator and beneficiary appear only where they differ from the accounting customer, or the reason is stated.
- Options: (a) remove them (preferred); (b) name the parks service as beneficiary if the world has it as a separate body.
- Needs decision: no
- From: context (F11); refuted by parties and broad (carried as counter-argument)

### tender/33#F20 · Low · The same Urvanian party is described with different language tags and legal-form renderings across the flow
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: Here tagged `en-XU`, with the legal form in `qau` and `en-XU`; in the Bayvarran-issued examples `en-XB` and one untagged legal form (`03-CallForTenders.xml:/CallForTenders/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`). The tag follows the issuer; could not be settled.
- Condition: The same rendering carries the same `languageID` in every example, or the rule is stated.
- Options: (a) `en-XU` everywhere (preferred); (b) the issuer's tag, applied uniformly and documented.
- Needs decision: yes
- From: parties (F5)

### tender/33#F21 · Low · Accounting parties described with their procurement and sales contacts
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:MarkAttention` = `Head of procurement`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- Why: For a billing document the contacts are those who book and pay; the flow knows the department's unit for that (`32-Invoice.xml:/Invoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Accounts payable, public works`).
- Condition: Accounts contacts in billing documents, or none.
- Options: (a) accounts contacts (preferred); (b) drop `Contact`, `Department` and `MarkAttention`.
- Needs decision: no
- From: parties (F6)

### tender/33#F22 · Low · Supplier's master data that a credit note does not use
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: Listing, fully-paid shares and the warehouse provider (with a contact that has no means of contact) are not used by a credit note (section 4.8); the issuer's own share capital is accepted by earlier merges and listed for completeness. Counter-argument (parties): the listing describes a listed company's legal entity.
- Condition: Listing and service provider only in documents whose purpose uses them.
- Options: (a) remove them (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: parties (F7), context (F14)

### tender/33#F23 · Low · Party tax exemption reason worded as a transaction
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: Under `PartyTaxScheme` "A reason for the party's exemption from tax"; the text begins with a kind of sale. Only its second half is the party's status.
- Condition: The party-level reason states the party's status.
- Options: (a) reword the text to the party's status and keep the code, whose list definition is "A body of the federation, a state or a city buys free of sales tax." (preferred, aligned with the other tender merges); (b) also a code that names the status alone (parties' preference).
- Needs decision: no
- From: parties (F8)

### tender/33#F24 · Low · The whole catalogue description of the item on the credit note line
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:CircularityProfile`
- Why: A credit note line says which invoiced item is credited, in what quantity and at what price; the full catalogue entry of `25-Catalogue.xml` is not credited. F4 and F8 come along with it.
- Condition: The item carries what the credit note uses.
- Options: (a) reduce the item (preferred); (b) keep the full copy everywhere and record that decision.
- Needs decision: no
- From: context (F15), broad (F9)

## Checked and consistent
- Arithmetic (re-done): 1 × 499 = 499.00; 1 × 18 = 18.00; 517.00 = line extension = tax exclusive = tax inclusive; withholding 10 % × 18.00 = 1.80; 517.00 − 1.80 = 515.20 payable, the amount 35 and 36 deduct. Tax bases 499.00 (G, EXP) and 18.00 (O, SVCABROAD) with the invoice's categories. 49900 XUF × 0.01 = 499 XBL.
- The withholding of the three billing documents nets to what the buyer paid the tax office: 72.00 − 1.80 − 0.72 = 69.48 (`35-Reminder.xml:/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`) (money).
- References: invoice VI-INV-26-0221 (32) and despatch advice CL-DA-26-0215 (29), whose note asked for damage to be reported; both exist and are of the kind the elements mean. Issue 4 April after invoice, import and the line's 2 April, before 34 and 35.
- Type 381; `LineCountNumeric` 2; parties as on the invoice, described identically (parties, by script); Bayforth's identifier the same in all five examples. `check_ids.py` (re-run): ISIN correct.
- The credit note is issued by the seller, who bears the transport risk under DAP (context).

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine[1]/cac:OriginatorParty/cac:PartyName/cbc:Name`: originator and beneficiary as fillers — refuted by broad and parties (no condition; the department ordered and receives the credit); context raised it, kept as F19 with this argument.
- `/CreditNote/cac:WorkReportDocumentReference/cbc:ID`: VI-WR-26-0080 is no example — refuted, the seller's report need not be a UBL document (from broad); a work report for a credit on goods — refuted, the installers' report of the bench they could not install is a plausible basis (from context). Its missing type is F17.
- `/CreditNote/cac:CreditNoteLine[2]/cbc:LineExtensionAmount`: installation credited although not done — refuted, it follows from the invoice having billed it (32/F1, F2); crediting an installation that will not be done is consistent (from broad, money, logistics, context).
- `/CreditNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`: the bench's share of the colour charge (5.00) not credited — refuted by money; broad raised it (see "Refuted in the merge").
- `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount`: no base quantity or price type — refuted as separate, covered by F3 (from money); the same price twice — refuted, "the price expressed in terms other than the actual price" (from context; its reversed role is F3).
- `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount`: not followed up by logistics (a sub-line may detail a part); raised by money, broad and context: F12.
- `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate`: raised by logistics only in 26; F14 here (from logistics).
- `/CreditNote/cac:CreditNoteLine[1]/cbc:TaxPointDate`: repeats the document's — refuted, legitimate at line level (from context).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset` (`-1`): malformed — refuted (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone` = `+999 1 041 518 4274`: real country code — refuted, +999 not assigned (from parties).
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`: master data — refuted by parties; kept in F22; check digit and fictional prefix confirmed.
- `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID` = `0990:10427`: real ICD — refuted (from parties).
- `/CreditNote/cac:PurchaseReference/cbc:ID` = `PARK-HB`: the right element for the park and bench position — confirmed by broad and context ("a reference to an object … to which this Credit Note relates"); that the IDs are unexplained is F17.

## Refuted in the merge
### broad/F7 (part) · Low · The bench's share of the colour charge is not credited
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:LineExtensionAmount` = `499.00`
- The part's finding (within broad/F7, "The credit does not say what happened, and leaves out the bench's share of the colour charge"): the colour charge of 200.00 for 40 benches (5.00 per bench) invoiced with the bench is not credited, although the whole bench and its installation are. Condition: the credit covers what was invoiced for the credited bench, or says why not. Options: credit 5.00 of the charge. Needs decision: yes (whether the charge is credited pro rata).
- Refuted because: the charge is one amount for the release, not a price per bench: `27-OrderChange.xml:/OrderChange/cac:AllowanceCharge/cbc:Amount` = `200.00` at document level, without base amount or multiplier, accepted as such in 28 and invoiced so in 32 (money's refutation). A special colour run costs the same for 39 or 40 benches, so crediting one bench does not reduce it. The rest of broad/F7 is in F12.

### context/F11 (part) · Low · "Not free of charge" stated on line 1
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:FreeOfChargeIndicator` = `false`
- The part's finding: `FreeOfChargeIndicator` is "An indicator that this credit note line is free of charge (true) or not (false). The default is false"; stating the default says nothing (rule: nothing implied by absence). Option: remove it. Needs decision: no. (The originator/beneficiary part of context/F11 is F19.)
- Refuted because: the repository rule (UBL IND6, "nothing implied by absence") argues for the explicit value, not against it: a reader should not have to infer "not free of charge" from a default; broad refuted it the same way ("stating it is harmless next to a credited amount"). It is no filler: the line credits an amount, and the indicator states that it is charged.

## Changed in the merge
- broad/F1 + money/F1 + context/F2 → F1: combined; money's references to 35 and 36 added.
- broad/F3 split: colour → F2 (with logistics/F1, context/F1); "manufacturer's installers" → F6 (with parties/F4, context/F4; Medium as 32/F8).
- money/F2 (Medium) + broad/F2 + context/F3 (High, yes) → F3: High, no, as 32/F6; context's forward-contract part → F14.
- broad/F5 (Medium) + logistics/F2 (High) → F4: High, as analysis.
- money/F3 + logistics/F3 + context/F5 (Medium) + broad/F8 (Low, periods part) → F7: Medium (the definition's condition is not met).
- context/F7 (Medium, yes) → F8: Needs decision no, as analysis.
- parties/F9 + context/F13 (Low) + broad/F9 (department part) → F11: Medium, as analysis.
- broad/F7 (rest) + money/F4 + context/F10 → F12; broad/F7's pro-rata colour charge → "Refuted in the merge".
- money/F5 (tax/payment currency part) + broad/F8 (tax currency part) → F13; money/F5's and broad/F9's forward contract → F14 (Low, yes, as 32/F14).
- broad/F9 split into F14 (forward contract), F16 (tax representative), F11 (department), F24 (catalogue).
- context/F11: FreeOfChargeIndicator → "Refuted in the merge"; originator/beneficiary → F19 (Low, no), with parties' and broad's refutations as counter-argument.
- context/F15 (Low, yes) → F24: Needs decision no, as analysis.
- parties/F8 → F23: preferred option changed to keeping the code and rewording the text, aligned with the other tender merges.

## Outside this review
- Whether a bench could be given a position (B17) in Harbour park two days after delivery is a timeline matter (broad).
- No replacement bench is despatched or invoiced in the flow; release 1 therefore ends with 39 benches, on which 35 and 36 settle (logistics). Whether a damaged bench is credited or replaced is a story question across later releases (context).
