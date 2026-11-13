# LLM review: 01-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/01-SelfBilledInvoice.xml`, Git blob `aee01edf4f4e0c209dc01462389e7115dcceae7c` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### cotton/01#F1 · High · Payment due date of the means contradicts the due date, the terms and the prepayment record
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-02-27`
- XPath: `/SelfBilledInvoice/cbc:DueDate` = `2026-01-13`
- XPath: `/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `Paid on issue by transfer. …`
- XPath: `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PrepaidPayment/cbc:PaidDate` = `2026-01-13`
- Why: `PaymentMeans/PaymentDueDate` is "The date on which payment is due for this means of payment". The credit transfer is the only means of payment, so the advance would be due on 2026-02-27, while the invoice's `DueDate` ("The date on which Invoice is due") is the issue date, the payment terms say "Paid on issue by transfer", and the final self-billed invoice records the advance as paid on 2026-01-13. 2026-02-27 is exactly 45 days after the issue date (recounted: 18 days left in January + 27 in February), i.e. the "45 days net" of `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:PaymentTerms/cbc:Note` = `45 days net.` applied to an advance that is paid at once. It also falls after the delivery (2026-02-05) and the final invoice (2026-02-07). One payment cannot be due on both dates.
- Condition: every due date in the example (`DueDate`, `PaymentMeans/PaymentDueDate`) is the same date, agrees with the payment terms note and with the `PaidDate` recorded in 04.
- Options: (a, preferred) set `PaymentMeans/PaymentDueDate` to 2026-01-13, or (b) drop it since `DueDate` already says it; both match the note and 04. (c) If the advance was really due later, change `DueDate`, the note and 04's `PaidDate` together.
- Needs decision: no
- From: broad (F1), money (F1), logistics (F1), context (F1)

### cotton/01#F2 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: in UN/EDIFACT 5305 code `O` is "Services outside scope of tax". The line is seed cotton, a supply of goods, and the same tax category says so with `SupplyTypeCode` `GOODS`, so the code carries a meaning its list does not give it. EN 16931 uses `O` for any supply outside the scope of VAT; under the rule of semantic conformance that practice is context, it does not lower the severity. Counted over `*.xml` (merge, lxml): 17 files use 5305 `O` (`grep -rl --include='*.xml' 'schemeID="UN/EDIFACT EDED 5305">O<'`), 5 of them with `O` and `SupplyTypeCode` `GOODS` in the same category (cotton 01, 04, 05, 16 and sea/29); broad's "used for goods in 17 examples" counted every use of `O`. Money listed the treatment as consistent across 01, 04 and 05; that is consistency, not fit with the code's meaning.
- Condition: the tax category of the seed-cotton line and its subtotal carries a code whose meaning covers a supply of goods outside the scope of tax, or the deviation is recorded as a deliberate finding of the repository and the example says which meaning it uses.
- Options: (a, preferred) decide once for the whole world how a supply of goods outside any sales tax is coded (another 5305 code only if the tax story supports it, or a regional/national list), because the same choice affects every Lisavan example; (b) keep `O` and record it as a deliberate EN 16931-style deviation (a candidate for the TC / CEN write-up).
- Needs decision: yes
- From: broad (F2)

### cotton/01#F3 · Low · The ginnery's customs-trader number and the farm's fields in a domestic prepayment invoice
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XL-TR-042681`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The cotton fields`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.lisavufarm.example`
- Why: section 4.8 (presence). A domestic self-billed prepayment between two Lisavan parties involves no customs, and no delivery takes place under it; no location-dependent tax or levy is computed (the terms note puts both on the delivery). `Party/PhysicalLocation` is "The physical location of this party"; with its coordinates and the farm's home page as `InformationURI` it repeats the postal address's coordinates, and the customs-trader number has no use here. Both read as copied from the parties' master data (no fillers, IND5). Context counted the farm's `PhysicalLocation` in 01, 03, 04, 05 and 06; only in the delivery note 03 does the document have a use for it.
- Condition: every identifier and location of the parties in this example is one the document has a use for.
- Options: (a, preferred) leave the customs-trader number and `PhysicalLocation` out of this invoice; (b) keep one only where the story gives it a role here (e.g. the advance tied to a field), and say which.
- Needs decision: no
- From: parties (F5), context (F2)

### cotton/01#F4 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two registers (`XL:ICR`, `XB:FBR`). Recounted: 271 occurrences in 181 files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<'` / `grep -rl`). That reads as a default rather than each company's history (IND5). It may be deliberate (a register-wide re-registration), which the examples alone cannot show. Same treatment as in every earlier flow's merge.
- Condition: each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has none; (c) if 1996-01-01 is a register-wide date, say so in the story.
- Needs decision: yes
- From: parties (F4)

### cotton/01#F5 · Low · Contacts do not fit the role or the party
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MICRO`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:SoleProprietorshipIndicator` = `true`
- Why: here the ginnery is the accounting customer that buys seed cotton and writes and pays the self-billed invoice; a question about it goes to its purchasing or farm-payments desk (04 routes the same farm invoices to `04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`), not to the desk that sells lint. The farm is a sole proprietorship and a micro enterprise run by one person; a "Customer service officer" in a "Sales" department describes a company with a sales organisation and does not fit its "Farm office".
- Condition: the ginnery's contact in this role handles seed-cotton purchases or farm payments (or is left out), and the farm's contact has no job title or department, or ones that fit a one-person farm.
- Options: (a, preferred) a purchasing / farm-payments contact for the ginnery and no job title/department (or "Owner") for the farm; (b) drop the contacts, since the electronic addresses are given.
- Needs decision: no
- From: broad (F4), parties (F2, F3)

### cotton/01#F6 · Low · Address lines repeat the structured address and mix two languages in one line
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[2]/cbc:Line` = `Farm track off Plantation Road at kilometre 4, past the cotton fields.`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[3]/cbc:Line` = `North coast`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[4]/cbc:Line` = `Selanu / Port Wrenfield`
- Why: the four lines repeat `StreetName`, `Description`, `District` and `CityName` of the same address. `Line` is "An address line expressed as unstructured text (may be repeated only to provide the same content in multiple natural languages)", yet lines 1 and 4 put the Lisavan and English forms into one text without `languageID`. Parties considered the same line and kept it out (an unstructured rendering; the Lisavan address format may print both names on one line); that argument explains why the lines might exist, not why they repeat every structured part, so the finding stays, Low.
- Condition: the farm's postal address states each part once, and any language-specific rendering carries its `languageID`.
- Options: (a, preferred) drop the address lines and keep the structured parts; (b) keep only lines that add information not in the structured parts, one language per `Line` with `languageID`, or document the Lisavan print format that needs them.
- Needs decision: no
- From: broad (F5); parties (considered and refuted, argument carried)

### cotton/01#F7 · Low · Expiry date on a commercial-register entry
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- Why: `RegistrationExpirationDate` is "The date upon which a registration expires (e.g., registration for an import/export license)". The registration described is the farm's entry in the island companies register (`COMMERCIAL`), which normally does not expire. A registration that expires at year end would rather be the farm registration 04 refers to (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AdditionalDocumentReference/cbc:ID` = `XL-FARM-REG-0412`), which is not the company registration. Parties refuted it: a farm registration renewed each season is a plausible reading of a registration with an expiry date. Both readings hold, and which one is meant is a question of the world's register rules, so the merge cannot settle it.
- Condition: the expiry date belongs to a registration that expires, and that registration is the one described in this `PartyLegalEntity`.
- Options: (a, preferred) drop the expiry date from the company registration; (b) if Lisavan sole proprietorships register for one year at a time, keep it and make the world's register rules say so.
- Needs decision: yes
- From: broad (F6); parties (considered and refuted, argument carried)

### cotton/01#F8 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: `TaxTotal` is "The total amount of a specific type of tax" and `TaxScheme` "The taxation scheme within which this tax category is defined". "No general sales tax" is not a taxation scheme but its absence, and the scheme has no `ID`, so a receiver cannot tell which tax the zero total is for. Context refuted the tax total as a filler: it states positively that no sales tax applies, which IND6 asks for. That justifies stating the absence, not naming the absence as a scheme; the finding stays Low and a decision, as utilities/13#F8 for the same value. Recounted: 9 files carry the name (`grep -rl --include='*.xml' '<cbc:Name>No general sales tax</cbc:Name>'`).
- Condition: either the zero tax total names a real tax scheme of Lisavu that the supply is outside of, with its ID, or the example carries no tax total for a tax that does not exist, consistently with the world's rules for Lisavu.
- Options: (a, preferred) decide once for all Lisavan examples: name the Lisavan tax (if any) the supply falls outside, with a scheme ID; (b) leave the tax total out if the world's tax story says Lisavu has no sales tax and the customization does not require one.
- Needs decision: yes
- From: broad (F3); context (considered and refuted, argument carried)

### cotton/01#F9 · Low · A 0 % rate on tax category O
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` = `0`
- Why: `Percent` is "The tax rate for this category, expressed as a percentage". A supply outside the scope of tax has no rate; 0 % reads as a zero-rated supply, a different category. No part raised it; added by the merge for consistency with the utilities and road merges, which made the same value a Low finding.
- Condition: a category that states the supply is outside the scope of tax carries no `Percent`.
- Options: (a, preferred) drop `Percent` in both places (with whatever code F2 settles on).
- Needs decision: no
- From: merge

## Checked and consistent
- Arithmetic (redone): 4500 KGM × 0.226 XLC per 1 KGM = 1017.000 XLC = line, `LineExtensionAmount`, `TaxExclusiveAmount`, `TaxInclusiveAmount` and `PayableAmount`; taxable amount 1017.000, tax 0.000.
- The advance is 4500 kg, a quarter of the 18 000 kg delivered (`03-DeliveryNote.xml:/DeliveryNote/cac:DespatchLine/cbc:DeliveredQuantity` = `18000`) and billed in 04 at the same price 0.226; 04 deducts it (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:PrepaidAmount` = `1017.000`) and cites this invoice with its issue date (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:BillingReference/cac:SelfBilledInvoiceDocumentReference/cbc:IssueDate` = `2026-01-13`).
- The terms note (no presumptive tax, no cotton fund levy on the advance) agrees with 04, which withholds the tax and adds the levy on the delivery only; no `WithholdingTaxTotal` here.
- `check_ids.py`: RF reference `RF61SCGSBI260191` and account `XL67BSEL0020004817534` have valid check digits; the account is the farm's, the same as in 04 and 06.
- Parties: identifiers (`IC42681`, `IC42544`), register, legal form, addresses and coordinates are the same as in 03, 04, 05 and 06 (parties, logistics).
- Item identification `LCF-SC`, HS 520100 and CPC 01921 are the same as in 03, 04 and 05; HS 5201 covers raw cotton, ginned or not (own knowledge, logistics and context).
- ISIC 0163 (post-harvest crop activities, incl. ginning) for the ginnery and 0116 (fibre crops) for the farm (context).
- `ContractDocumentReference` `SCG-SEASON-2026` is the season agreement also cited by 02–05; an external contract, the element says what it is.

## Considered and refuted
- `/SelfBilledInvoice/cbc:InvoiceTypeCode` = `386`: prepayment type in a self-billed invoice instead of 389 — refuted because the document type already says self-billed and 386 says what this invoice is (an advance), which 04 then deducts. (from broad, money; context listed it as consistent)
- `/SelfBilledInvoice/cbc:AccountingCost`: the buyer's cost centre in an invoice — refuted: in self-billing the issuer is the buyer, and the definition does not restrict the code to the supplier. (from broad)
- `/SelfBilledInvoice/cac:ContractDocumentReference/cbc:ID`: refers to no example — refuted: an external season agreement, not a document of the flow. (from broad)
- `/SelfBilledInvoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `RTGS`: real-time gross settlement for a small advance to a micro farm — refuted: "paid on issue" needs immediate settlement, and `CORAL-NET` is the world's given rail. (from broad, money, context)
- `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:PaymentNote` = `Invoice SCG-SBI-26-0191`: duplicate of the remittance information — refuted: "free-form text applying to the Payment for the owner of this account" fits a note for the farm's statement, and it names this document. (from money)
- `/SelfBilledInvoice/cac:BuyerCustomerParty` and `/SelfBilledInvoice/cac:SellerSupplierParty`: duplicates of the accounting parties — refuted: stating buyer and seller shows that the customer writes the self-billed invoice; nothing implied by absence (IND6). (from parties)
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:AddressLine[1]/cbc:Line` = `Sifatofu Natii / Plantation Road`: two languages in one line — parties kept it out (unstructured rendering, Lisavan format may print both). The merge disagreed in part: made part of F6 (from broad). (from parties)
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationExpirationDate` = `2026-12-31`: parties refuted (seasonal farm registration); the merge cannot settle it: F7 (from broad). (from parties)
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName` = `Lisavu Cotton Farm`: a sole proprietorship usually registered under the owner's name — refuted: a trade name in a fictional register is possible. (from parties)
- `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:CommodityClassification/cbc:CommodityCode` = `520100`: HS for seed cotton — refuted: HS 5201 covers cotton not carded or combed, ginned or not; cotton seed alone would be 1207 (own knowledge). (from logistics)
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:LocationCoordinate`: same coordinates as the postal address, copied — refuted as a coordinate error (the farm address is the track at the fields); the presence of `PhysicalLocation` itself is F3. (from logistics)
- `/SelfBilledInvoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `4500`: a quantity of goods on an advance implying a delivery — refuted: a prepayment invoice commonly states the quantity the advance is for. (from context)
- `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`: a tax total for a non-existent scheme as a filler — context refuted (IND6: states positively that no tax applies); the merge disagreed in part: F8 (from broad). (from context)
- `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cbc:InformationURI` = `https://www.lisavufarm.example`: the farm's home page as location information — not a separate finding; part of F3. (from context)

## Refuted in the merge
### parties/F1 · Low · Payee named although it is the seller itself
- XPath: `/SelfBilledInvoice/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledInvoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- Why (parties): `PayeeParty` is "The Party who receives the Payment." It is the farm, already the accounting supplier and seller, and the payee account `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Lisavu Cotton Farm` already says where the money goes; a payee role carries information only when someone else is paid.
- Condition (parties): `PayeeParty` is present only if a party other than the accounting supplier receives the payment. Options: (a, preferred) drop it; (b) keep it only if the story has a different payee. Needs decision: no.
- Refuted because: the definition has no "if different from the supplier" condition (unlike `PayerParty`'s checklist case), and in a self-billed invoice, written by the customer, naming who receives the money states it rather than implying it by absence (IND6). Broad and context refuted it on the same grounds.

## Changed in the merge
- broad/F1, money/F1, logistics/F1, context/F1 → F1: combined; 45-day arithmetic recounted.
- broad/F2 → F2: count corrected (17 files use `O`, 5 with `GOODS`); severity and decision kept.
- parties/F5 + context/F2 → F3: grouped (copied master data), customs-trader number and `PhysicalLocation` in one finding.
- broad/F4 + parties/F2 + parties/F3 → F5: grouped (contacts of both parties), one condition.
- broad/F5 → F6: parties' counter-argument added.
- broad/F6 → F7: kept Low/yes, parties' refutation added as the other reading.
- broad/F3 → F8: context's counter-argument added; aligned with utilities/13#F8.
- F9: added by the merge (category O with 0 %), aligned with the utilities and road merges.
- parties/F1 → Refuted in the merge.
