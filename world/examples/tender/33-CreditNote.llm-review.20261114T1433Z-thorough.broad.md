# LLM review: 33-CreditNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/33-CreditNote.xml`, Git blob `fedb04ee2964c2e08e60565d54f4c570247bdfda` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit fb56d6c 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/33#F1 · High · "Set off against the next release's invoice", but the credit is settled with this release's payment
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PaymentTerms/cbc:Note` = `Set off against the next release's invoice.`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- Why: the line says the credit is set off against the invoice of the next release; the header says against the next payment to the seller. The next payment is that of the invoice this credit note corrects, and the remittance advice does exactly that: `36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `515.20` is deducted from the payment of VI-INV-26-0221 (release 1). The line-level term is thus contradicted by the header and by what happens; no next release exists in the flow.
- Condition: line and header state the same way of settling the credit, and it is the way the remittance advice settles it.
- Options: (a) remove the line-level PaymentTerms (preferred); (b) reword it to the set-off against the payment of VI-INV-26-0221.
- Needs decision: no

### tender/33#F2 · High · Pricing currency is ferra, but the prices are in lume
- XPath: `/CreditNote/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Price/cbc:PriceAmount` = `18`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount` = `49900`
- Why: PricingCurrencyCode names the currency used for the prices of the credit note. Both prices are in XBL; the price in the pricing currency (49900 XUF) appears only as an "alternative condition price", defined as "the price expressed in terms other than the actual price". The roles are reversed: by the header, the ferra price is the actual price.
- Condition: Price/PriceAmount is in the pricing currency, or PricingCurrencyCode is absent/XBL and the ferra price stays the alternative.
- Options: (a) PriceAmount 49900 and 1800 XUF, no alternative price (preferred, as proposed for 26 and 32); (b) drop PricingCurrencyCode.
- Needs decision: no

### tender/33#F3 · High · The credited bench is described as grey, and its installation as done by the manufacturer's installers
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Item/cbc:Description[2]` = `Anchoring one bench in the ground with the supplied anchors, by the manufacturer's installers.`
- Why: the bench credited is one of the forty of delivery CL-DA-26-0215, which are moss green (`29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`); the item says variant GRY, Ferro grey. The installation is, by the contract, done by the subcontractor Saltmere Engineering (`24-TenderContract.xml:/TenderContract/cac:TenderResult/cac:SubcontractTerms/cbc:Description`), not by the manufacturer's installers.
- Condition: the credited item's variant and colour are those delivered; the installation's description agrees with the contract.
- Options: (a) green variant; description without "by the manufacturer's installers" or naming the subcontractor (preferred).
- Needs decision: no

### tender/33#F4 · Medium · The installation credit is "collected for" the forwarder
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: CollectedForParty is "The Party on whose behalf this item or amount is collected". The line credits 18.00 for the installation of one bench, a service of Valdara performed by its subcontractor Saltmere Engineering. Bayforth Forwarding is the seller's tax representative (header) and was named as freight forwarder in the order change; nothing links it to the installation price, and a credit collects nothing. If the element was meant for the 1.80 of withholding tax, that tax is withheld by the customer for the Bayvarran treasury, not for Bayforth.
- Condition: CollectedForParty is present only where the line's amount is collected on behalf of a third party, and names that party.
- Options: (a) remove it (preferred); (b) explain in the story an amount that Valdara collects for Bayforth.
- Needs decision: yes (what Bayforth Forwarding does)

### tender/33#F5 · Medium · Emission factor that does not lead to the emission value
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Same block as in the catalogue (25).
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/33#F6 · Medium · Language code in LocaleCode; province in Region
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CreditNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; the province is in CountrySubentity.
- Options: (a) a locale code, and move the province (preferred).
- Needs decision: no

### tender/33#F7 · Low · The credit does not say what happened, and leaves out the bench's share of the colour charge
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:LineExtensionAmount` = `499.00`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount` = `180.00`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:DocumentReference/cbc:ID` = `PWD-DMG-26-0081`
- Why: the credit note has no note, reason or description saying why one bench and one installation are credited; the reader infers a damaged bench from the ID of a referenced document (PWD-DMG…) and from a sub-line "Side frames of the bench" with 180.00 whose relation to the 499.00 is not stated (part of it? the repair value?). The colour charge of 200.00 for 40 benches (5.00 per bench) invoiced with the bench is not credited, although the whole bench and its installation are.
- Condition: the credit note states its reason; the sub-line's amount is explained or sums to its line; the credit covers what was invoiced for the credited bench, or says why not.
- Options: (a) add a Note/DiscrepancyResponse with the reason, explain or drop the sub-line, and credit 5.00 of the charge (preferred); (b) keep amounts and only add the reason.
- Needs decision: yes (whether the charge is credited pro rata)

### tender/33#F8 · Low · Invoice periods on a one-off credit; tax currency without a tax total in it
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-03-31`
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:EndDate` = `2026-04-04`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:InvoicePeriod/cbc:StartDate` = `2026-04-02`
- XPath: `/CreditNote/cbc:TaxCurrencyCode` = `XUF`
- Why: InvoicePeriod "Associates the Credit Note with Invoicing Periods rather than with a specific Invoice". This credit note is for one specific invoice, which it references, and for a single event; the header period merely spans invoice date to credit note date, and the line period is a bare start date (2026-04-02, presumably the day the damage was found) that is not a period of supply. The invoice it corrects reports its tax also in the tax currency (TaxTotal in XUF); the credit note names the same tax currency but has no tax total in it.
- Condition: invoice periods are present only where supply is billed by period; a credit note with a tax currency different from the document currency carries the tax total in it, as its invoice does.
- Options: (a) remove the periods (give the damage date in the reason) and add the XUF tax total (preferred).
- Needs decision: no

### tender/33#F9 · Low · Tax representative, foreign exchange contract, catalogue content, department as a company
- XPath: `/CreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- XPath: `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/CreditNote/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: as in the invoice (32): the tax representative has no tax registration and no Bayvarran tax to account for; the buyer's forward contract of 2026-01-02 is quoted by the seller on the pricing rate; the line repeats the catalogue's record of the bench; the department carries a company liquidation status and commercial-register type.
- Condition: as stated for 32 (F8, F9, F11 there).
- Options: (a) remove them (preferred).
- Needs decision: yes (for the tax representative and the hedge, as in 32)

## Checked and consistent
- Arithmetic: 1 × 499 = 499.00; 1 × 18 = 18.00; lines 517.00 = tax exclusive = tax inclusive; withholding 10 % × 18.00 = 1.80 (the rate of the invoice); payable 517.00 − 1.80 = 515.20, the amount the remittance advice deducts. Tax bases 499.00 (G) and 18.00 (O) with the invoice's categories and reasons.
- References: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221` (32); `/CreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `CL-DA-26-0215` (29), whose note asked for damage to be reported; unit prices equal the invoice's; 49900 XUF × 0.01 = 499 XBL.
- Type 381 (credit note); parties as on the invoice; issue 2026-04-04 after the invoice and delivery.
- `/CreditNote/cac:PurchaseReference/cbc:ID` = `PARK-HB` and the line's PARK-HB-B17 read as the park and bench position concerned, which is what a purchase reference is for ("a reference to an object … to which this Credit Note relates").
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/CreditNote/cac:CreditNoteLine[1]/cbc:FreeOfChargeIndicator`: explicit "false" as filler — refuted, the definition gives false as default and stating it is harmless next to a credited amount.
- `/CreditNote/cac:CreditNoteLine[1]/cac:OriginatorParty/cac:PartyName/cbc:Name`: department as originator and beneficiary of the line — refuted, it originated the order and receives the credit.
- `/CreditNote/cac:WorkReportDocumentReference/cbc:ID`: VI-WR-26-0080 is no example — refuted, the seller's inspection report need not be a UBL document.
- `/CreditNote/cac:CreditNoteLine[2]/cbc:LineExtensionAmount`: installation credited although the bench was not installed — follows from the invoice having billed it (32 F1), not a separate problem here.

## Outside this review
- Whether a bench could be assigned a position (B17) in the Harbour park two days after delivery is a timeline matter.
