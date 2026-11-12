# LLM review: 01-Order.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/01-Order.xml`, Git blob `1c959f7204add325b43b103744bcf375fb8ba1db` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit b22581c 2026-11-12 Reviews of the plastics and wood flows, run 20261112T2101Z-thorough: parts written so far
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

### plastics/01#F1 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:ID` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; the language itself is `Language/ID`. The value `en` with `listID` `ISO 639` is the bare language code and repeats `Language/ID`; it names no locale (language plus country or region, such as the Bayvarran English the flow writes as `en-XB` in `languageID`). All 362 `LocaleCode` elements, in 213 of the 250 XML examples, carry this value (`grep -rho --include='*.xml' '<cbc:LocaleCode' world/examples | wc -l`; `grep -rl` for the files).
- Condition: every `LocaleCode` holds a locale identifier from a locale list named in its `listID` (e.g. a BCP 47 tag such as `en-XB`), or is absent.
- Options: (a) drop `LocaleCode` (preferred: the language is already in `Language/ID`, and nothing in the order depends on the locale); (b) set it to the locale (`en-XB`) with a locale list (BCP 47 / CLDR) as `listID`. The parts split on the preference (broad and context preferred b, parties a); the merge follows a, as in the other merges of this run.
- Needs decision: no
- From: broad, parties, context

### plastics/01#F2 · Medium · Province of the seller's address in Region
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: UBL defines `Address/Region` as "The recognized geographic or economic region or group of countries in which this address is located" and `Address/CountrySubentity` as "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". A province is an administrative division, so it belongs in `CountrySubentity` (with `CountrySubentityCode` where Urvania has a list). The Bayvarran address of the same document does it that way (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Coastal State`). The value also has no `languageID`, while the other parts of this Urvanian address are given in `qau` and `en-XB`. The same value occurs 219 times in 104 of the 250 XML examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`; `grep -rl` for the files).
- Condition: no Urvanian address in the example carries the province in `cbc:Region`; where the province is given, it is in `cbc:CountrySubentity` (rendered like the other address parts) and, where a list exists, `cbc:CountrySubentityCode`.
- Options: (a) move the province to `CountrySubentity` (+ code) (preferred: it is what the element is for, and matches the Bayvarran addresses); (b) drop it where the postal code already identifies the place; (c) keep `Region` only if Ferrano is an economic region and not an administrative division, recorded in the world data.
- Needs decision: no
- From: broad, parties, context

### plastics/01#F3 · Low · Both parties registered on 1 January 1996
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `PartyLegalEntity/RegistrationDate` is "The registration date of the CompanyID". A Bayvarran and an Urvanian company, in different registers, are both registered on New Year's Day 1996, a day on which registers are normally closed. The date occurs 271 times in 181 of the 250 XML examples (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01' world/examples | wc -l`; `grep -rl` for the files), for at least 24 unrelated companies (parties part), while some parties have specific dates (e.g. `1962-04-12`, `1988-10-03`). It reads as a default rather than each company's own date (IND5/IND6). It may have a story reason (e.g. registers created on that date) that the review cannot see.
- Condition: each company's `RegistrationDate` is the date from its own history, or the shared date is explained by the world's history, or the element is absent.
- Options: (a) give each company its own registration date from its history (preferred); (b) if 1 January 1996 is a general (re-)registration date, record that in the world's story and keep it; (c) drop `RegistrationDate` where no history is known.
- Needs decision: yes
- From: broad, parties, context

### plastics/01#F4 · Low · Buyer's contact is a sales/customer-service desk
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: In an Order the buyer's contact is the function that buys. Rivermouth Packaging buys raw material here (`/Order/cbc:AccountingCost` = `Raw materials`), but its contact is a customer-service officer in Sales, the seller-side function (the seller's own contact is the same kind: `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`, which fits the seller). The parties carry one generic contact in every document of the flow, whatever their role.
- Condition: the buyer's contact in the Order is a purchasing function (name, job title and department agreeing with each other and with that role), or is absent.
- Options: (a) give Rivermouth role-specific contacts and use the purchasing one here (preferred: it is what `Contact` is for); (b) drop the contact, or use one neutral general contact that fits all its roles.
- Needs decision: no
- From: broad, parties, context

### plastics/01#F5 · Low · Buyer's bank account in an order that moves no money
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "The financial account associated with this party". The order has no payment means, mandate or payment instruction; the buyer later pays by credit transfer to the seller (`10-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`), from this very account (`11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`). In the order the account (with branch and bank address) is master data the document does nothing with (section 4.8; IND5). The account appears in 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples | wc -l`), while the seller Rinova, which receives the money, carries no party account in any of them (money part).
- Condition: the Order carries the buyer's financial account only if the order itself uses it (e.g. a prepayment or direct-debit arrangement stated in the order).
- Options: (a) drop the account from the buyer party (preferred); (b) keep it only together with a payment arrangement the order actually agrees.
- Needs decision: no
- From: broad, money, parties, context

### plastics/01#F6 · Low · Italian text tagged as English
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering should be in the language its `languageID` names. The second rendering of the Urvanian street is Italian ("Via del Riciclo", "Recycling street") tagged `en-XB`, and the legal form is Italian with an English gloss (untagged, in a document whose other texts are English). Bayvarran streets in the same flow are English (`Estuary Road`, `Exchange Street`). The pattern occurs in 101 of the 250 XML examples (`grep -rlE --include='*.xml' 'languageID="en-X[UB]">(Via|Banchina|Piazza|Valico|Società)' world/examples | wc -l`, parties part). Counter-argument (broad and context parts, which refuted it): the world renders Urvanian names in English text by Italianate exonyms throughout (city `Ferrano` for `Ruldraz`), so a street name is the name an English text uses; that is a fictional convention, not a clash with a real standard. The merge cannot settle this from the documents: for proper names the convention argument holds if the world has it, but the legal form ("Società a responsabilità urvaniana") is a description, not a proper name, so it is the stronger case.
- Condition: every rendering tagged `en-…` (or standing as the English text) is English or a proper name used as such in English, and the convention is recorded in the world story if Italianate forms are meant.
- Options: (a) record the exonym convention in the world's story and keep street names; render the legal form in English (preferred: it keeps the world's style and fixes the part that is not a name); (b) translate all renderings into English; (c) drop the second rendering where the local form suffices.
- Needs decision: yes
- From: parties (broad and context refuted it; see Considered and refuted)

### plastics/01#F7 · Low · Rinova described differently from the other documents of the flow
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:CertificateType` = `Operating permit`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- Why: the same party should be described the same way in every example of the flow. In the documents Rinova issues itself (e.g. `02-OrderResponse.xml`) its legal form and permit type carry an Urvanian and an English rendering, each tagged (`qau`, `en-XU`). In this order (and in the other documents issued by Rivermouth, 09 and 11, per the parties part) they have one untagged English rendering, while the address of the same party keeps both renderings but tags the same English text `en-XB` instead of `en-XU`. Counter-argument (broad part on 02, context part on this order): the tag can follow the issuer's variety of English, which is a legitimate reading. That covers the tag, but not the dropped `qau` renderings of the legal form and permit type while the address keeps its `qau` rendering.
- Condition: Rinova's legal form, permit type and address carry the same renderings and language tags in every document of the flow, or the differences follow one stated rule (e.g. the issuer's languages) applied to all its texts alike.
- Options: (a) describe Rinova identically everywhere, as in the documents it issues itself (preferred: party master data does not change with the writer); (b) apply an issuer's-language rule consistently to address, legal form and permit type, and record it.
- Needs decision: yes
- From: parties

### plastics/01#F8 · Low · Rinova's waste-recovery permit in an order for a product
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: `Party/PartyAuthorization` is "An authorization issued to this party". The permit (Basel Annex IV R3, "Recovery of non-hazardous plastic waste") authorises Rinova to operate its recovery plant. The goods are recycled PE granulate classified as a product (HS `390110`, polyethylene in primary forms, not HS 3915 waste); nothing in an order for granulate depends on Rinova being allowed to take in waste. The permit is in 14 XML examples, all 11 of this flow (`grep -rl --include='*.xml' XU-ENV-2024-0311 world/examples | wc -l`), which reads as master data copied into every document (IND5). Counter-argument (broad part, which refuted it): the buyer orders granulate with a recycled-content claim, which the permit backs. The merge does not follow it: the claim has its own item-level certificate (`/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`), and nothing in the order links the party's permit to it.
- Condition: the permit appears only in documents that act on it, or the document makes its relevance explicit (e.g. as evidence behind the recycled-content certificate).
- Options: (a) remove it from the order (preferred); (b) if the recycled-content claim is to rest on it, connect it to the item's `EnvironmentalCertificate` instead of carrying it as party data.
- Needs decision: no
- From: parties, context (broad refuted it)

### plastics/01#F9 · Low · The order states no requested delivery date or period
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `River quay, Lumeport`
- Why: the only `Delivery` names the receiving party but carries no `RequestedDeliveryPeriod`, and the place appears only as free text under the CPT terms. The transport documents work to a firm window (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ServiceEndTimePeriod/cbc:EndDate` = `2026-04-22`), and the waybill states a "latest date of delivery allowed by the buyer" (`06-Waybill.xml:/Waybill/cac:Shipment/cac:GoodsItem/cac:Delivery/cbc:LatestDeliveryDate` = `2026-04-23`) that nothing from the buyer supports; nothing may be implied by absence (IND6). Counter-argument (broad part): an order does not need a delivery date for its purpose. The merge agrees that it is not Medium, but the waybill attributes a date to the buyer that no buyer document states, so it stays a Low finding.
- Condition: the order states when the buyer wants the goods (a requested delivery period consistent with 03/04 and the waybill's latest delivery date), or the waybill no longer attributes a latest delivery date to the buyer.
- Options: (a) add `cac:Delivery/cac:RequestedDeliveryPeriod` ending 2026-04-23 (preferred: the order is where the buyer states it); (b) leave the order and drop the waybill's latest delivery date (see the waybill's reviews).
- Needs decision: no
- From: logistics (broad refuted the absence as such)

### plastics/01#F10 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: the identifier is in the fictional scheme `urn:ubl-examples:world:item`, but has 12 digits with a correct GS1 mod-10 check digit (recomputed in the merge: 8), so it has the form of a GTIN-12 (UPC-A) number. A reader can take it for a real UPC (rule: fictional values must not be mistaken for real ones). Whether this exact number is assigned could not be checked. Item numbers of this scheme occur 82 times in the XML examples (`grep -rho --include='*.xml' 'schemeID="urn:ubl-examples:world:item">[0-9]*' world/examples | wc -l`).
- Condition: the item number cannot be mistaken for a real GTIN, or the world's item scheme is documented as deliberately GTIN-shaped with its numbers verified as unassigned.
- Options: (a) change the format of the world's item numbers so they are not valid GTINs (preferred); (b) keep them and record the verification against the GS1 register in the sources.
- Needs decision: yes
- From: broad

### plastics/01#F11 · Low · Chamber of commerce as issuer of a recycled-content certificate
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: `EnvironmentalCertificate/IssuerParty` is "The authorised Organisation who issues this Certificate". In the world the Ferrano Chamber of Commerce issues certificates of origin and ATA carnets (`road/06-CertificateOfOrigin.xml`, `carnet/01-GoodsItemPassport.xml`). Recycled content is normally certified by an accredited certification body that audits the recycler, or by the environment authority supervising the plant (own knowledge, e.g. EN 15343 / ISO 14021 claims). The remark "Made entirely from sorted production waste recovered in Urvania" reads like an origin statement, which would fit the chamber, but the certificate type is `RECYCLED`.
- Condition: the issuer of the recycled-content certificate is an organisation the world authorises to certify recycled content, or the world states why the chamber does so.
- Options: (a) name a certification body or the Urvanian environment authority as issuer (preferred); (b) keep the chamber and record its role in the world story.
- Needs decision: yes
- From: parties, context

## Checked and consistent
- Arithmetic (redone in the merge): `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `120` × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `83200` (base quantity 1 TNE) = 9 984 000 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `9984000` = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `9984000` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `9984000`; taxable amount 9 984 000 at 0 % = tax 0.
- Tax: category `G` with Urvanian exemption reason `EXP` (export outside Urvania) fits an Urvanian seller delivering CPT to Bayvarra and matches the goods invoice (`10-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`) and the seller's role as exporter in `05-ExportCustomsDeclaration.xml`.
- Price, quantity and currency agree with the goods invoice (`10-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `83200`, 120 t, `XUF`).
- Delivery terms `CPT` "River quay, Lumeport": the seller pays the carriage, which agrees with Rinova as transport user and bill-to party in 03/04 and with the freight invoice to Rinova (07), and with the unloading place of the barge (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`) and the goods invoice note (`10-Invoice.xml:/Invoice/cbc:Note[2]` = `Carriage paid to: the price includes the barge to the river quay.`).
- Item: density 0.92 g/cm³ fits HS 390110 (specific gravity below 0.94) and the description; UN CPC 34710 fits.
- Physics: 1 t of PE granulate at a bulk density of about 0.55–0.6 t/m³ (own knowledge) takes about 1.7–1.8 m³, a normal volume for a 1 t jumbo bag (FIBC).
- The order ID `RP-PO-26-0882` is referenced by 02, 05, 06, 08 and 10, and all resolve to this order; order line 1 is the line referenced in 06 and 08.
- Parties: Rinova (`XU-R-104548`), Rivermouth (`20412740`) and the Ferrano Chamber of Commerce (`XU-R-105370`) carry the same identifiers, names, tax registrations, legal entities, addresses and contacts in every example of the flow, apart from the renderings in F7 (parties part, script over the flow). ISIC 2220 for Rivermouth and 3830 for Rinova fit. `check_ids.py`: the IBAN-like account passes its check digits.

## Considered and refuted
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`: an Italian street name tagged `en-XB` — refuted by broad and context as the world's convention for English renderings of Urvanian names (and the `en-XB` vs `en-XU` tag as following the writer's variety of English). The merge does not fully follow: kept as F6 and F7 with "Needs decision: yes", the refutation given there as counter-argument. (from broad, context)
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyAuthorization/cbc:PurposeCode`: the waste-recovery authorisation as master data copied into the order — refuted by broad because the permit backs the recycled-content claim. The merge disagrees; kept as F8. (from broad)
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: ISO 6523 ICD `0990` could clash with a real ICD — refuted because the real ICD list does not assign 0990 (own knowledge; the register runs to the 02xx range). (from broad, parties)
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: a BIC-shaped bank identifier (`BLUMXBLX`) could be a real BIC — refuted because positions 5–6 carry the user-assigned ISO 3166 code `XB`, which no real BIC uses. (from parties)
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID`: the buyer's customs-trader ID copied from master data — refuted because seller and buyer need each other's customs identities for the export and import declarations of this sale (05, 09). (from parties, context)
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`: an Urvanian exemption code in an order issued by a Bayvarran buyer — refuted because the order's tax is the buyer's expectation of the seller's tax treatment, and the seller exports from Urvania. (from money)
- `/Order/cac:TaxTotal`: a tax total in an order — refuted because it is the anticipated tax, and the export exemption is information the buyer needs. (from context)
- `/Order/cbc:DocumentCurrencyCode` = `XUF`: the buyer orders in the seller's currency — refuted; a legitimate commercial choice, and invoice and remittance stay in `XUF`. (from money)
- Absence of payment terms in the order while the invoice imposes 30 days net, 2 % discount and penalty interest — refuted: the invoice points to the seller's published terms (`10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentTermsDetailsURI` = `https://www.rinova.example/terms`); nothing is implied by the order's silence. (from money)
- `/Order/cac:DeliveryTerms/cbc:ID` = `CPT`: suspected a mismatch with a seller-booked barge — refuted because under CPT the seller contracts and pays the carriage, as 03/04 and 07 show. (from logistics)
- The order has no requested delivery date — refuted by broad as a finding of the order's purpose; kept by the merge as a Low finding for another reason (F9). (from broad)

## Changed in the merge
- broad/F2, parties/F2, context/F2 → F1: combined; options list both directions, preference "drop" (parties) chosen over "en-XB" (broad, context) for consistency with the other merges of this run.
- broad/F1, parties/F1, context/F1 → F2: combined; option (b) of parties and (b) of broad/context both kept.
- broad/F5, parties/F6, context/F6 → F3: combined; "Needs decision" set to yes (broad, context) instead of no (parties), because whether the shared date has a story reason depends on the world's company histories.
- broad/F3, parties/F3, context/F5 → F4: combined.
- broad/F4, money/F1, parties/F4, context/F3 → F5: combined.
- parties/F7 → F6: Italian street name kept; the counter-argument of broad and context (who refuted it) added; preferred option changed from "translate" to "record the convention, render the legal form in English", because the merge cannot settle the street-name part.
- parties/F8 → F7: "Needs decision" changed from no to yes, because broad (02) and context (01) argue that the tag follows the issuer, which the merge cannot settle; counter-argument added.
- parties/F5, context/F4 → F8: combined; "Needs decision" set to no (context) instead of yes (parties), because removing a party permit no document uses changes no story; broad's refutation added as counter-argument.
- logistics/F1 → F9: wording; broad's refutation added as counter-argument.
- broad/F6 → F10: check digit recomputed; the claim about the GS1 US range left out, as the merge could not verify which prefixes are assigned.
- parties/F9, context/F7 → F11: combined.

## Outside this review
- The waybill's "latest date of delivery allowed by the buyer" (`06-Waybill.xml`) has no source in the buyer's documents; see F9 and the waybill's reviews.
