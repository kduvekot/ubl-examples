# LLM review: 26-Order.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/26-Order.xml`, Git blob `6251abb7d11ec4be2651a2e8b809979afc7557fa` (committed)
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

### tender/26#F1 · High · Pricing currency ferra, but the price is in lume
- XPath: `/Order/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `499`
- Why: `PricingCurrencyCode` is "A code signifying the currency used for all prices in the Order". The only price of the order, 499, carries `currencyID="XBL"`, the document currency and the tendered price in lume; in ferra it would be 49900, as in `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`. The header code and the price's currency contradict each other. 27 and 28 carry the same header code without any price.
- Condition: every `PriceAmount` of the order is in the currency `PricingCurrencyCode` names; if that is the document currency, there is no separate pricing currency or pricing exchange rate.
- Options: (a) drop `PricingCurrencyCode` and the pricing exchange rates and keep 499 XBL, as tendered (preferred if the contract price is in lume, see 25#F17); (b) price 49900 XUF with the pricing exchange rate converting to the line amount in XBL. Which option follows from the decision in 25#F17; either resolves this finding.
- Needs decision: no (the contradiction is encoding; the currency choice is decided in 25#F17)
- From: broad (F1, High), logistics (F2, High), context (F1, High, yes), money (F2, Medium)

### tender/26#F2 · High · Emission factor × base does not give the emission value
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement" and `ValueBaseMeasure` "The base quantity to which the value factor applies". Recalculated: 0.82 × 1 EA = 0.82, not 96 kg CO2e; 96 / 0.82 = 117.07 of an activity the document does not state. Same triple as in 25 and in 39 files (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: factor × base = value, with the base in the unit the factor refers to; or factor and base are absent.
- Options: (a) drop factor and base (preferred, as in the earlier flows; also resolved if F17 removes the emission from the order); (b) the base the factor refers to (e.g. 117 KWH).
- Needs decision: no
- From: logistics (F1, High), broad (F5, Medium); context listed it under "Outside this review"

### tender/26#F3 · High · The order has one line, but the invoice and the debit note for it treat the installation as part of this release
- XPath: `/Order/cbc:LineCountNumeric` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`
- Why: The order is the first release under a framework with two lots (benches and their installation) and orders 40 benches only. The invoice that cites it (`32-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`) bills a second line of 40 installations (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`, item `32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-INST-B`), and the debit note that also cites this order (`34-DebitNote.xml:/DebitNote/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`) charges a penalty for the late installation "of the release". Neither the order change (27) nor the response (28) adds an installation (no `VI-INST` in 26–28). The notices' average release `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:AverageSubsequentContractAmount` = `20680.00` is exactly 40 × (499 + 18), which suggests the release was meant to contain both. Logistics refuted it for this example (the order may cover the supply only; the problem is the invoice's); the order and the invoice contradict each other about what this release contains, which makes it a finding of both.
- Condition: what the invoice and the debit note treat as part of this release is ordered by it (as changed and accepted), with matching quantities and amounts.
- Options: (a) add an order line for 40 installations at 18.00 (720.00), raising the anticipated total to 20680.00 here and to 20880.00 in 27 and 28 (preferred); (b) order the installation by a separate order in the flow and let the invoice's second line and the debit note refer to it.
- Needs decision: yes (whether release 1 includes installation; adds a line or a document)
- From: broad (F2, High), money (F1, Medium), context (F11, Low); logistics refuted it (carried)

### tender/26#F4 · Medium · The seller's sales order number in the buyer's order
- XPath: `/Order/cbc:SalesOrderID` = `VI-SO-26-0058`
- Why: `SalesOrderID` is "An identifier for the Order, assigned by the seller". The order is the buyer's first message of the release (23 March 14:40); the seller answers on 25 March (28), which carries no sales order number, and no other example has VI-SO-26-0058 (`grep -rl --include='*.xml' VI-SO-26-0058 world/examples`: this file only). No quotation or reservation of the seller precedes the order.
- Condition: a seller-assigned order number appears first in a document of the seller and in the buyer's order only if such a document came earlier.
- Options: (a) remove it here and carry it in 28 (preferred); (b) explain it by an earlier seller document.
- Needs decision: no
- From: broad (F3), logistics (F3), context (F2)

### tender/26#F5 · Medium · The framework release number carried as a delivery-access release ID
- XPath: `/Order/cac:Delivery/cbc:ReleaseID` = `1`
- Why: In `Delivery`, `ReleaseID` is "An identifier used for approval of access to delivery locations (e.g., port terminals)". The value 1 reads as the first release (call-off) of the framework ("Releases every few months.", `21-ContractAwardNotice.xml:/ContractAwardNotice/cac:TenderingProcess/cac:FrameworkAgreement/cbc:Frequency`), a different meaning of "release"; the department's depot needs no access approval.
- Condition: `Delivery/ReleaseID` holds an access approval for the delivery location or is absent; the release number is stated elsewhere.
- Options: (a) remove it and say "Release 1" in a note (preferred); (b) a real gate or slot reference of the depot.
- Needs decision: no
- From: broad (F4), logistics (F4), context (F3)

### tender/26#F6 · Medium · A line-level pricing exchange rate that does not differ from the document's, with base rates of 1
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyBaseRate` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:TargetCurrencyBaseRate` = `1`
- XPath: `/Order/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- Why: `Price/PricingExchangeRate` is "The exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". It is the same rate, currencies and date as the document's, so the definition's condition is not met; the price it sits on is moreover in lume (F1). The base rates ("In the case of a source currency with denominations of small value, the unit base") of 1 convey nothing.
- Condition: a price carries its own exchange rate only when it differs from the document's; base rates only with a value other than 1 that the rate refers to.
- Options: (a) remove the line-level rate (preferred); (b) if a unit base is wanted, put it on the document-level rate (source base 100, rate 1).
- Needs decision: no
- From: money (F3), context (F4)

### tender/26#F7 · Medium · An emission boundary in `FullnessIndicationCode`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The UBL 2.5 definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty …". The value is a system boundary of the calculation and says nothing about transport equipment; the boundary is already in the lifecycle description. Same in every copy of the item (39 files with `CRADLETOGATE`).
- Condition: `FullnessIndicationCode` holds a fullness of transport equipment or is absent.
- Options: (a) remove it (preferred; also resolved if F17 removes the emission from the order); (b) TC write-up on the missing boundary element.
- Needs decision: no
- From: context (F5, Needs decision yes)

### tender/26#F8 · Medium · Lifecycle stage "Manufacturing" for an emission from the mine to the gate
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; the text covers extraction, steel making and manufacturing, the code only manufacturing. Same as 25#F9.
- Condition: code and description cover the same stages.
- Options: (a) omit the code or split by stage (preferred; also resolved by F17); (b) a code for the whole span.
- Needs decision: no
- From: added in the merge (context F14 noted that the catalogue's remarks "come along with every copy"), aligned with analysis/review-merge-decisions.md

### tender/26#F9 · Medium · A province in `Region`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries"; a province is `CountrySubentity`, as the Bayvarran addresses use. 219 in 104 files.
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds a region.
- Options: (a) move it to `CountrySubentity` (preferred).
- Needs decision: no
- From: broad (F6, part), parties (F2), context (F6)

### tender/26#F10 · Medium · Language code in `LocaleCode`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 code. 362 in 213 files.
- Condition: `LocaleCode` is absent or names a locale from a locale list.
- Options: (a) remove it (preferred); (b) `en-XB` from a locale list.
- Needs decision: no
- From: broad (F6, part), parties (F1), context (F7)

### tender/26#F11 · Medium · Public body described as a company in a commercial register, with a liquidation status
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The buyer is a municipal department (ISIC 8411); "A code signifying the party's liquidation status" has no meaning for it, and a "Commercial register" type does not fit a body that is not a company.
- Condition: no liquidation status, and no commercial-register type, on the public body.
- Options: (a) drop both (preferred); (b) reduce the legal entity to name and CompanyID.
- Needs decision: no
- From: broad (F10, part, Low), parties (F4, Low), context (F12, Low)

### tender/26#F12 · Low · The order says neither when nor exactly where to deliver
- XPath: `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Lumeport Public Works Department`
- XPath: `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Public works depot, Lumeport`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` = `Civic Square`
- Why: The order has no requested delivery date or period on the delivery or the line, although the call asked for a first delivery on `03-CallForTenders.xml:/CallForTenders/cac:ProcurementProject/cbc:RequestedDeliveryDate` = `2026-04-02` and the penalty clause of the contract ("0.5 % per day late") needs a due date to count from; the response (28) fixes none either. The DAP place is a description only, with no address or identifier; the department's only address is its office on Civic Square, and the despatch advice (29) has no delivery address ("Public works depot" occurs in this file only). Logistics rated the missing date Medium (the purpose depends on it); Low kept, aligned with the earlier flows' decision for orders without a requested delivery date. Logistics also refuted the text-only place (the named place for DAP may be text); the carrier still has no address.
- Condition: the order states the requested delivery date or period, and the place of delivery is identified by an address or identifier that the documents following the goods repeat.
- Options: (a) `Delivery/RequestedDeliveryPeriod` (e.g. ending 2026-04-02) and `Delivery/DeliveryLocation` or `DeliveryTerms/DeliveryLocation/Address` with the depot's address (preferred); (b) a note that the contract's lead time applies, and Civic Square as the place if the benches really go there.
- Needs decision: no
- From: broad (F7), parties (F7), logistics (F5, Medium), context (F9)

### tender/26#F13 · Low · Exchange rates and a forward contract that the order does nothing with, the contract dated before the procedure began
- XPath: `/Order/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ID` = `BL-FX-26-0091`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:Date` = `2026-03-23`
- Why: Every amount of the order is in lume, yet it carries tax, pricing and payment exchange rates. `PaymentExchangeRate` is "The exchange rate between the document currency and the payment currency"; the order names no payment currency. A forward purchase of ferra hedges a payment, yet it is attached to the pricing rate. It was concluded on 2026-01-02, ten days before the prior information notice (`01-PriorInformationNotice.xml:/PriorInformationNotice/cbc:IssueDate` = `2026-01-12`) and two months before the award, when nobody knew that the supplier would be Urvanian (the other tenderer is Bayvarran). The rate is exactly 100 on every date of the flow, so the forward hedges a rate that never moves. BL-FX-26-0091 occurs in 26, 27, 28, 32, 33, 35 (`grep -rl --include='*.xml' BL-FX-26-0091 world/examples`), in no other flow.
- Condition: the order carries an exchange rate only for a currency in which it states or will settle amounts; a foreign exchange contract sits on the rate it fixes and is dated when the need could be known.
- Options: (a) remove the rates and the forward contract from the order and, if hedging is part of the story, put a forward dated after the award on the invoice's payment rate (preferred); (b) if lume and ferra are pegged at 100, say so once and drop the forward contract.
- Needs decision: yes (whether and when the department hedges)
- From: broad (F8), money (F4), logistics (F8), context (F8)

### tender/26#F14 · Low · The contract cited twice, once as an unexplained "originator document"
- XPath: `/Order/cac:OriginatorDocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/Order/cac:Contract/cbc:ID` = `PWD-2026-PARKS`
- Why: `OriginatorDocumentReference` is "A reference to an originator document associated with this document", e.g. the requisition of the unit that needs the goods. Its ID is the contract's (and the procurement file's), with no document type; the contract is already cited in `Contract`.
- Condition: the originator reference names a document other than the contract and says what it is, or is absent.
- Options: (a) remove it (preferred); (b) cite the parks section's requisition with a DocumentType.
- Needs decision: no
- From: broad (F9), logistics (F6), context (F10)

### tender/26#F15 · Low · The programme has another code than in the procurement documents
- XPath: `/Order/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCostCode` = `PWD-PARKS-26`
- XPath: `/Order/cbc:AccountingCost` = `Parks renewal programme 2026`
- Why: The same programme is coded `03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26` in 01, 02, 03 and 24, and `PWD-PARKS-26` in 26, 29, 32 and 33 (`grep -rl --include='*.xml'` over `world/examples/tender`); the budget line of the procedure is BL-PARKS-26 on account 4.2.110. Here one string is both the buyer's accounting code and a project identifier. Broad and context refuted the accounting code itself (a buyer-internal code named after its programme is plausible); the difference to the procurement documents remains.
- Condition: the programme has the same code in all documents; the accounting code is the buyer's cost account, or the same code deliberately.
- Options: (a) PARKS-26 as project reference and the budget account 4.2.110 as accounting code (preferred); (b) PWD-PARKS-26 in the procurement documents too.
- Needs decision: no
- From: logistics (F7)

### tender/26#F16 · Low · Party tax exemption reason worded as a transaction
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: "A reason for the party's exemption from tax": the text begins with a kind of sale; only its second half is the party's status. The code's list description reads as a buyer status and can stay.
- Condition: the party-level reason states the party's status.
- Options: (a) reword, e.g. "Public body: exempt from the state sales tax" (preferred); (b) also a status code.
- Needs decision: no
- From: parties (F3)

### tender/26#F17 · Low · The whole catalogue record of the item repeated in the order
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:BrandName` = `Valdara`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:AdditionalItemProperty[5]/cbc:TestMethod` = `Static load on the seat for one hour, three seats loaded evenly, no lasting deformation`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Dimension[4]`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ResourceOriginDescription` = `Steel made from Serravona ore in Urvania`
- Why: The item is identified by the seller's and the standard number and the catalogue reference (`VI-CAT-26-0211`). Beyond that the line repeats the catalogue entry of 25 in full: keywords and brand, the load test method, the seat-height range, the emission with its calculation method, and the circularity profile (maintenance, resources, packaging waste, repairability, repair manual). These are the seller's statements, which the buyer neither orders nor can vouch for; the catalogue's problems (F2, F7, F8; ore-based steel against the contract's 30 % recycled steel, two keywords in one element, see 25) come along with every copy.
- Condition: the order's item carries its identification and the properties the order uses (e.g. the colour variant); the catalogue description stays in the catalogue, which the item references.
- Options: (a) reduce the item to identification, name, description and required properties (preferred); (b) keep the full copy and record the design decision.
- Needs decision: no (aligned with analysis/review-merge-decisions.md; context said yes as a design decision)
- From: broad (F10, part), context (F14)

### tender/26#F18 · Low · Master data of the parties that the order does nothing with
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:MarketName` = `Ferrano Stock Exchange`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: The buyer restates to the seller the seller's share capital, listing and warehouse provider (whose contact has no means of contact), and both parties' customs-trader numbers. An order does nothing with these. Parties refuted the listing as part of a listed company's description (carried). Customs-trader numbers: the import (31) is a separate document.
- Condition: the parties carry what the order uses.
- Options: (a) leave these out of the order (preferred); (b) keep those for which a use can be stated.
- Needs decision: no
- From: broad (F10, part), parties (F6), context (F13); customs-trader numbers added in the merge

### tender/26#F19 · Low · Same Urvanian party and item texts tagged `en-XB` here and `en-XU` elsewhere
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name[2]` = `Park bench Serra 180`
- Why: Valdara's English renderings and the English item texts copied from the catalogue are tagged `en-XB` here; the Urvanian-issued examples tag the same texts `en-XU` (`13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`; `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:Item/cbc:Name[2]` = `Park bench Serra 180`). The text is identical, so the tag follows the issuer; whether that is intended cannot be settled. The street name is moreover an Italian name tagged as English; the earlier flows kept that as a second Low/yes question (world convention of Italianate English names, or not), folded in here by the merge.
- Condition: the same text carries the same `languageID` in every example, or the rule is documented.
- Options: (a) tag by the text (`en-XU`) everywhere (preferred); (b) document the issuer rule.
- Needs decision: yes
- From: parties (F5, part); item texts added from broad's remark under "Checked"

### tender/26#F20 · Low · Legal form of the Urvanian party in one untagged rendering
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: In the Urvanian-issued examples the legal form is given in `qau` and `en-XU` (e.g. `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`); here once, untagged, while the address next to it has both renderings.
- Condition: the legal form is rendered like the address wherever the party is described in full.
- Options: (a) both renderings, tagged (preferred).
- Needs decision: no
- From: parties (F5, part; split off in the merge)

### tender/26#F21 · Low · World item number that is a valid GTIN-12
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- Why: As 25#F21: 12 digits with a valid GS1 check digit (recalculated: 7), readable as a GTIN-12 in the US/Canada range, against the rule that fictional values must not be mistaken for real ones. The scheme is the world's own item scheme (the counter-argument of the parts that refuted it in 25).
- Condition: world item numbers cannot be read as valid GTINs, or their verification against GS1 is recorded.
- Options: (a) change the world item-number format (preferred); (b) record the verification.
- Needs decision: yes
- From: added in the merge, aligned with 25#F21 and analysis/review-merge-decisions.md

## Checked and consistent
- Arithmetic (recalculated): 40 × 499 = 19960.00 = line amount = `LineExtensionAmount` = `PayableAmount` = taxable amount; tax 0.00.
- Exchange rates internally consistent: XUF → XBL × 0.01 and XBL → XUF × 100; 49900 XUF × 0.01 = 499 XBL (catalogue).
- Unit price 499 lume = winning tender (119760.00 / 240).
- Quantity 40 respects the tender's ordering terms (minimum 20, maximum 96, steps of 4) and is one sixth of 240.
- `CatalogueDocumentReference` `VI-CAT-26-0211` is 25 (21 March), before the order; `CatalogueIndicator` true fits an order from it; item data equal catalogue line 1.
- Issue date 2026-03-23 = first day of the contract `PWD-2026-PARKS`; `LineCountNumeric` 1 = one line; `OrderTypeCode` 220.
- DAP with the department as importer agrees with 31; tax category G with the Urvanian export reason is what 32 applies.
- Parties: buyer = contracting department, seller = contractor; identifiers the same across the flow; buyer's procurement-office contact and seller's order desk fit an order (from parties).
- `check_ids.py`: ISIN XU0001042501 correct.

## Considered and refuted
- `/Order/cbc:OrderTypeCode`: a release could be 226 (call-off order) — refuted: 226 refers to a blanket order message; 220 with a contract reference is correct (from broad, context).
- `/Order/cbc:TaxCurrencyCode`: XUF while the tax total is in XBL, or a Bayvarran buyer asking for ferra — refuted: the element is "the currency requested for tax amounts in Invoices related to this Order", the tax is Urvanian VAT and the invoice gives a tax total in XUF (from broad, money, context).
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID`: a Bayvarran buyer stating Urvanian export VAT — refuted: the order anticipates the invoice's tax; the buyer's own exemption needs no line (from broad; money likewise for `TaxExemptionReasonCode`).
- `/Order/cac:TaxTotal/cbc:TaxAmount`: tax total in XBL although the tax currency is XUF — refuted: the tax currency is a request for the invoice, and the amount is zero (from money).
- `/Order/cac:PricingExchangeRate/cbc:ExchangeMarketID`: XLMX a real MIC — refuted: in the world's market list; no ISO 10383 MIC XLMX known (own knowledge) (from broad).
- `/Order/cbc:AccountingCostCode`: no listID, equal to the project reference — refuted: a buyer-internal code named after its programme (from broad, context); the code difference to the procurement documents is F15.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:Contact/cbc:Name`: order desk — fits an order (from broad, parties).
- `/Order/cac:DeliveryTerms/cbc:ID`: DAP and who bears duties — refuted: under DAP the buyer clears the import, as 31 shows (from money).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:TimezoneOffset`: `-1` — refuted: text element, same everywhere (from parties).
- `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Telephone`: +999 — refuted, not assigned in E.164 (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID`: unused master data — refuted by parties as part of the legal entity; the merge keeps it in F18 (from parties).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: `0990` a real ICD — refuted (from parties).
- `/Order/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name`: redundant, being the buyer — refuted: no "if different" condition, and no other statement of who receives (from parties).
- `/Order/cac:OrderLine`: no installation line — refuted by logistics as a finding of 32; the merge disagrees and keeps F3 (from logistics).
- `/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`: a description instead of an address — refuted by logistics (named place may be text); the merge keeps it in F12 (from logistics).
- `/Order/cac:Contract/cbc:ID`: equal to the procurement file number — refuted: consistent with the award documents (from logistics).
- `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:WarrantyInformation[2]`: the ten-year coating warranty missing — refuted here, the text is the catalogue's (25#F20) (from context).

## Changed in the merge
- broad/F1, logistics/F2, context/F1 (yes), money/F2 (Medium) → F1: High; Needs decision no, because the currency choice is decided once in 25#F17.
- logistics/F1, broad/F5 (Medium) → F2: High, aligned with the decisions file; preferred option dropping factor and base.
- broad/F2 (High), money/F1 (Medium), context/F11 (Low) → F3: High, yes; logistics' refutation carried.
- context/F5 → F7: Needs decision no, aligned with the decisions file.
- F8 (lifecycle stage) and F21 (GTIN-like item number) added by the merge, aligned with 25 and the decisions file.
- broad/F6 → F9 and F10: split.
- broad/F10 → F11, F17, F18: split into public body (raised to Medium, aligned), catalogue copy and party master data.
- parties/F4, context/F12 → F11: raised from Low to Medium.
- broad/F7, parties/F7, logistics/F5 (Medium), context/F9 → F12: combined, Low (aligned with the earlier flows for orders).
- broad/F8, money/F4, logistics/F8, context/F8 → F13: combined.
- context/F14 → F17: Needs decision no (aligned).
- parties/F5 → F19 and F20: split; item texts added to F19.

## Outside this review
- Whether the invoice (32) should bill the installation under this order, and the debit note's penalty base, lie with 32 and 34 as well (F3 is the order's side).
