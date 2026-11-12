# LLM review: 09-ImportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/09-ImportCustomsDeclaration.xml`, Git blob `f2d4fcae7f399f23e32926db94e2eab6ad1dd2dc` (committed)
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

### plastics/09#F1 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyIdentification/cbc:ID` = `20410137`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: CustomsParty is "The Authority who is legally responsible for processing the Declaration": the Customs and Border Service of Bayvarra, a public body (its own ISIC code is `8411`, general public administration). Its legal entity puts it in the federal business register as a commercial registration and gives a company liquidation status ("A code signifying the party's liquidation status", here "Active, not in liquidation"). A state service is created by law, is not a company in a commercial register and cannot be liquidated (checklist); its identifier uses the same commercial-register scheme. The values contradict the party's own industry code (hence Medium, as in the wood flow's merge). The Urvanian customs in 05 has the same problem (broad).
- Condition: the customs authority's legal entity carries no company liquidation status and no commercial registration; if it is identified, the identifier comes from a scheme for public bodies.
- Options: (a) drop the corporate registration and liquidation status (or the whole legal entity) and identify the authority by a public-body scheme (preferred); (b) if the register also lists public bodies, a registration type other than COMMERCIAL and no liquidation status.
- Needs decision: no
- From: broad (F1), parties (F3), context (F3)

### plastics/09#F2 · Medium · Province of the consignor's address in Region
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; CountrySubentity is "The political or administrative division of a country …, such as the name of its county, province, or state". The Bayvarran addresses of the same declaration use CountrySubentity with a code (e.g. the bonded store, `Coastal State`, `XB-CO`). The parts counted 219 occurrences in 104 example files.
- Condition: no Urvanian address carries the province in `cbc:Region`; it is in `cbc:CountrySubentity`.
- Options: (a) move it to CountrySubentity (preferred); (b) keep in Region only if the world defines it as an economic region.
- Needs decision: no
- From: broad (F4), parties (F1), context (F4)

### plastics/09#F3 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats `Language/ID`. The parts counted 362 LocaleCode elements in 213 example files, all `en`.
- Condition: every LocaleCode holds a locale from a list its listID names, or is absent.
- Options: (a) drop it where the locale has no use (preferred, as parties and the wood merges); (b) `en-XB` with a locale list (broad, context).
- Needs decision: no
- From: broad (F5), parties (F2), context (F5)

### plastics/09#F4 · Medium · Temperature code given together with a measured value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:Measure` = `5`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:MeasureCode` = `MIN`
- Why: Temperature/MeasureCode is "A code describing the temperature, when not expressed as a measure". The temperature is expressed as a measure (5 °C), so the definition's condition is not met; `MIN` only repeats what the parent `MinimumTemperature` says.
- Condition: MeasureCode appears only where the temperature has no Measure.
- Options: remove MeasureCode (preferred).
- Needs decision: no
- From: broad (F3, first part), context (F2)

### plastics/09#F5 · Low · Exit office of the exporting country in the import declaration
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`
- Why: CustomsExitOfficeLocation is the "Customs exit office of the goods being declared". The value is the Urvanian office where the goods left Urvania (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`); goods imported into Bayvarra do not leave its customs territory, and the Bayvarran import gains nothing from it; the name alone also does not say on which side of the border the post is (broad, context: Medium). Logistics refuted it: the UBL 2.5 model gives the ImportCustomsDeclaration only this office element (verified in the merge in `UBL-Entities-2.5.gc`: no office of entry or presentation), and the value is literally the exit office of the goods being declared. The merge agrees that the value fits the definition read literally, so it is not a misuse (not Medium); whether the import declaration has a reason to carry the exporting country's exit office (section 4.8) the merge cannot settle.
- Condition: the import declaration carries the exit office only if it serves the Bayvarran import (e.g. a Trade Accord rule linking the two declarations), and then names it unambiguously as Urvanian; the place of presentation is identifiable (it is, as the bonded store).
- Options: (a) remove it (preferred by broad and context: the bonded store already locates the goods); (b) keep it as information for the importing customs and name it as the Urvanian post.
- Needs decision: yes
- From: broad (F2, Medium), context (F1, Medium); logistics considered and refuted it

### plastics/09#F6 · Low · Customs value includes the river freight after the border
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `99840.00`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredStatisticsValueAmount` = `99840.00`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:FreeOnBoardValueAmount` = `98046.00`
- Why: 99 840 XBL is the full CPT price (`10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000` XUF at 100 XUF = 1 XBL), i.e. including all of the barge freight (179 400 XUF). The goods enter Bayvarra at the river border (exportation event 2026-04-20 16:00 in 06) and the barge continues to Lumeport (discharge 2026-04-22). Under the WTO valuation agreement (own knowledge: transport after importation is excluded when distinguished from the price; Art. 8.2 lets members include transport only up to the place of importation) the freight share inside Bayvarra would not be part of the customs value, and statistical values are normally taken at the border. The freight is distinguished here: this declaration splits it off for the FOB value (98 046 = (9 984 000 − 179 400) / 100, recalculated in the merge). The world's valuation rule for Bayvarra is not visible.
- Condition: the customs and statistical values follow a stated valuation basis (price at the border, or a recorded Bayvarran rule that the delivered price is declared), consistent with the FOB value and with 05.
- Options: (a) the value at the border (FOB plus the freight share up to the river border) (preferred by money: the freight is known and distinguished); (b) keep the delivered price and record the Bayvarran rule.
- Needs decision: yes
- From: money (F1)

### plastics/09#F7 · Low · "Duties paid by the importer's account at customs", but the account given is a bank current account and no duty is stated
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cbc:AccountTypeCode` = `CACC`
- Why: The note says duties are paid from the importer's account at customs, i.e. an account held with the customs authority (cash or deferment account). The only account in the declaration is Rivermouth's current account at the Bank of Lumeport (`CACC`, "Current"), and the declaration states no duty or tax and no value "on which a duty, tax, or fee will be assessed". Whether any duty is due is open: the goods claim preferential origin (`/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P`), and the world's Bayvarran exemption list has a reason for goods used in manufacture (`RESALE`, read for its meaning by money), which fits a packaging maker. Broad and parties saw the bank account as master data copied into the declaration; context refuted that, because the note gives an account a use. The merge combines them: the note and the account given do not describe the same thing, and the bank account has no use unless it is the account debited.
- Condition: the note and the structured data agree: either the account the duties are paid from is identified as such (and duties or taxes are actually due), or the note says what is really paid; the bank account is present only if it is the account debited.
- Options: (a) word the note after what the importer pays and from where, and drop the bank account if it is not debited (preferred); (b) keep the account as the debit account and say so in the note.
- Needs decision: yes (whether duty or tax is due is a tax-treatment question)
- From: money (F2), broad (F8, first part), parties (F5); context considered and refuted the account part

### plastics/09#F8 · Low · "No previous procedure" next to a previous declaration (the export declaration of another country)
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode` = `1000`
- XPath: `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `RR-CD-26-0888`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cbc:Name` = `Bonded store at the river quay, Lumeport`
- Why: The procedure code means "Release for free circulation, no previous procedure". PreviousCustomsDeclaration is "A reference to a previously sent customs declaration"; it is the Urvanian export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `RR-CD-26-0888`), lodged with another customs administration, and the goods sit in a bonded store "where this goods item is temporarily stored". A previous declaration of an import is normally one lodged in the same territory (temporary storage, transit) (own knowledge). If the goods were in temporary storage only, 1000 is right but the export declaration is not a previous declaration of Bayvarra's customs; if they were under customs warehousing, the procedure is not "none". Broad refuted both points (temporary storage is no procedure; citing the exporting country's declaration is common practice); the merge agrees that 1000 fits temporary storage, but keeps the question whether the export declaration is a "previous" declaration in this sense, which it cannot settle.
- Condition: the procedure code, the previous declaration and the storage tell one story: temporary storage only (1000; the export declaration, if kept, referenced as the exporting country's document), or customs warehousing (matching procedure code, warehousing declaration referenced).
- Options: (a) temporary storage with 1000, and the export declaration moved to an `AdditionalDocumentReference` with its type (preferred: the flow has no warehousing declaration); (b) remove the previous declaration (context); (c) a warehousing story.
- Needs decision: yes
- From: logistics (F2), context (F7); broad considered and refuted it

### plastics/09#F9 · Low · Packages of the goods item not declared
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsTariffQuantity` = `120000`
- Why: The goods are 120 jumbo bags (06), but the declaration states neither the number nor the kind of packages, nor a net weight (the tariff quantity gives the mass, 120 000 KGM). Import declarations usually carry the number and kind of packages as standard data (own knowledge of customs practice). Logistics also held that `Quantity` = 120 TNE ("the number of units making up this goods item") misuses the element; the merge refutes that part as for plastics/06 (the tonne is a legitimate unit of a bulk commodity sold by the tonne).
- Condition: the packages (120 × JB) are declared, consistent with 05 and 06.
- Options: (a) a `ContainingPackage` of type JB with the count expressed as in plastics/06#F10 (preferred); (b) the count in the goods description.
- Needs decision: no
- From: logistics (F1, Medium)

### plastics/09#F10 · Low · Technical data of the bonded store that the declaration does not use
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:AirFlowPercent` = `0`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:HumidityPercent` = `60`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:DangerousGoodsApprovedIndicator` = `false`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:RefrigeratedIndicator` = `false`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:PowerIndicator` = `true`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MaximumTemperature/cbc:Measure` = `35`
- Why: BondedWarehouseLocation is "The location of the bonded warehouse where this goods item is temporarily stored"; customs needs to know where the goods are (name, hall, gate, licence). Air flow, humidity, power, food and dangerous-goods approvals and the temperature range describe the hall's equipment, which a declaration for PE granulate in bags does nothing with (section 4.8). The temperatures are defined for "this refrigerated storage", while the storage is not refrigerated; their AttributeID `AMBIENT` and the description "Kept frost-free." show that ambient limits are meant (checked in the merge), which softens but does not remove the mismatch. Logistics found the conditions fit PE granulate, which needs no special storage: that is the reason they add nothing here.
- Condition: the bonded-store location carries what identifies it, and storage properties only where the goods or the procedure require them.
- Options: (a) keep ID, name, gate and licence, drop the physical properties (preferred); (b) keep them only if the world's customs rules ask for them.
- Needs decision: no
- From: broad (F6, and F3 second part), context (F6)

### plastics/09#F11 · Low · Waybill referenced with an ID only; the commercial invoice not referenced
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890`
- Why: The transport document is referenced by ID only, without saying it is the consignment note (06); the seller's invoice (`RR-INV-26-0894`, 10), on which the customs value rests, is not referenced.
- Condition: the waybill reference says what it refers to; the commercial invoice is referenced, or the story says why not.
- Options: (a) `DocumentTypeCode` on the waybill reference and a reference to `RR-INV-26-0894` with its type (preferred); (b) a description on the existing reference.
- Needs decision: no
- From: logistics (F3)

### plastics/09#F12 · Low · Notifier is the importer itself
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- Why: NotifierParty is "The Party who is responsible for contact on master level". It repeats the importer and consignee (the declarant), given only by ID and name, and adds no party and no information. Parties refuted it (the self-declaring importer is that party); the merge keeps it because the importer's own presence already says so, and the repetition has no reason (IND5), as decided in the wood flow's merge.
- Condition: a notifier is present only if it is a party other than the declarant, or its presence has a stated reason.
- Options: remove it (preferred).
- Needs decision: no
- From: broad (F7), context (F8); parties considered and refuted it

### plastics/09#F13 · Low · Customs office in Upland State for goods arriving by river at Lumeport
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName` = `Border Crossing Road`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CityName` = `Marrowdale`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- Why: The authority is given with the address and contact of a border office in Marrowdale, Upland State, while the goods arrive by barge at the river quay in Lumeport, Coastal State, and are stored there (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:Name` = `River quay, Lumeport`). An authority's contact should be reachable where the goods are (checklist). Whether Marrowdale is on the river or is the service's head office cannot be seen from the examples (broad put it under "Outside this review" as a location question; the merge keeps it as a finding because the contact's fit to the role is within this document, and keeps the location note below).
- Condition: the customs party's address and contact are those of the office handling goods at the Lumeport river quay, or the document makes clear why the Marrowdale office is competent.
- Options: (a) the Lumeport customs office's address and contact (preferred); (b) Marrowdale as head office with a fitting contact.
- Needs decision: yes
- From: parties (F11); broad (Outside this review)

### plastics/09#F14 · Low · Rinova's waste-recovery permit in a document about a product
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cbc:PurposeCode` = `R3`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cbc:Purpose` = `Recovery of non-hazardous plastic waste`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: The permit to recover plastic waste (Basel Annex IV R3) is irrelevant to importing a product (HS 3901.10) and in a customs declaration could even suggest a waste shipment (broad). Master data copied into every document of the flow (IND5).
- Condition: the permit appears only in documents that act on it, or the document says why it is relevant.
- Options: (a) remove it (preferred); (b) link it to the item's environmental certificate if the claim is to rest on it.
- Needs decision: no (parties said yes; aligned with context and 06)
- From: broad (F8, second part), parties (F6), context (F10)

### plastics/09#F15 · Low · Importer's contact is a sales order desk
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The importer's contact answers customs about this import (customs or shipping), not an order desk with a customer-service title in Sales.
- Condition: the importer's contact is a customs or import function, or is absent.
- Options: (a) role-specific contact (preferred); (b) drop it.
- Needs decision: no
- From: broad (F9), parties (F4), context (F11)

### plastics/09#F16 · Low · Signature ID contains the flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `RP-SIG-IM-plastics`
- Why: Signature/ID is "An identifier for this signature"; `plastics` is the example flow's name in the repository, not a value the importer would assign. Broad counted 14 examples with such IDs (`grep -rlE --include='*.xml' -- '-SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`); other signatures use the party's numbering (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Signature/cbc:ID` = `FB-SIG-882`).
- Condition: the signature ID is one the signatory could assign, without reference to the example flow.
- Options: derive it from the declaration number (preferred).
- Needs decision: no
- From: broad (F10), context (F9)

### plastics/09#F17 · Low · Both companies registered on 1 January 1996
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: RegistrationDate is "The registration date of the CompanyID". Two companies in two registers on New Year's Day 1996; the parts counted 271 occurrences in 181 example files. A default value (IND5).
- Condition: each company's RegistrationDate belongs to its own history, or the shared date is explained, or the element is absent.
- Options: (a) individual dates (preferred); (b) record a 1996 (re-)registration in the story; (c) drop it.
- Needs decision: yes (parties said no; aligned with broad, context and the wood merges)
- From: broad (F11), parties (F7), context (F12)

### plastics/09#F18 · Low · Recycled-content certificate issued by a chamber of commerce
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cac:IssuerParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalCertificate/cbc:CertificateTypeCode` = `RECYCLED`
- Why: EnvironmentalCertificate/IssuerParty is "The authorised Organisation who issues this Certificate". The chamber issues certificates of origin and carnets in the world; recycled content is normally certified by an accredited certification body or the environment authority (own knowledge, EN 15343 / ISO 14021). Same as plastics/08#F8.
- Condition: the issuer is an organisation the world authorises to certify recycled content, or the world records why the chamber does.
- Options: (a) a certification body or the environment authority (preferred); (b) record the chamber's role in the story.
- Needs decision: yes
- From: parties (F10), context (F13)

### plastics/09#F19 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8, recalculated in the merge); as GTIN-13 `0771030000048` its prefix 077 lies in a range GS1 US issues to real companies (own knowledge). It could be taken for a real GTIN; the real register was not checked. Same as plastics/08#F9.
- Condition: the number cannot be mistaken for a real GTIN, or its absence from the register is verified and recorded.
- Options: (a) a non-GTIN format (preferred); (b) record the verification.
- Needs decision: yes
- From: broad (F12)

### plastics/09#F20 · Low · Italian text tagged as English, and Rinova rendered differently from the other documents
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cac:Certificate/cbc:CertificateType` = `Operating permit`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek sir trinnazhalhek tevul (hatran dudrul riskek)`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via del Riciclo`
- Why: (1) The street name rendering tagged English is Italian, and the legal form is Italian with an English gloss; a world convention of Italianate exonyms is not visible, and a legal form is not a proper name (parties F8; parties counted the pattern in 101 of 250 examples). (2) In the documents Rinova issues (02–08, 10) its legal form and permit type carry an Urvanian and an English rendering, each tagged `qau`/`en-XU`; in this Rivermouth-issued document (as in 01 and 11) they have one untagged rendering, while the address keeps both renderings and tags the same English text `en-XB`. The same party looks different depending on who writes (parties F9). Context refuted the corresponding point for the item description (the tag follows the declarant's variety of English), which is a possible rule, but then it is not applied to all of Rinova's texts. The two points share their XPaths and their fix (one rendering rule for party master data), so the merge combines them.
- Condition: every rendering tagged `en-…` is English or a proper name used as such, and Rinova's legal form, permit type and address carry the same renderings and tags in every document, or follow one recorded rule.
- Options: (a) record the naming convention, render the legal form in English, and describe Rinova identically everywhere as in its own documents (preferred: party master data does not change with the reader; aligned with the wood flow); (b) apply the issuer's-language rule to all texts, the address included.
- Needs decision: yes (the tagging rule is a world convention; parties said no for (2), aligned with the wood merges' "yes" on the tag rule)
- From: parties (F8, F9)

## Checked and consistent
- Values (recalculated in the merge): 9 984 000 XUF / 100 = 99 840.00 XBL customs and statistical value; FOB 98 046.00 = 99 840.00 − 1 794.00, the freight 179 400 XUF / 100 (06, 07); rate 1:100 as in all exchange-rate aggregates of the examples (money). Insurance 0.00 fits CPT and the uninsured carriage (broad, money).
- Shipment `RR-SH-26-0889`, gross 120 480 kg, 120 t, tariff quantity 120 000 kg = waybill net weight, HS 3901.10, origin XU agree with 05, 06, 08 (broad, logistics, context).
- `FB-WB-26-0890` resolves to 06; `RR-CD-26-0888` is the customs declaration ID of 05 (broad, logistics, context; flow index re-run in the merge).
- Issued 2026-04-22 10:35, after the planned discharge at 08:00 (broad, logistics).
- Subtype FREECIRC, procedure 1000 and status FOREIGN agree with each other (context).
- Importer, consignee and signatory Rivermouth with customs-trader ID `XB-TR-412740`, consignor Rinova; ISIC codes fit; IBAN-like account passes `check_ids.py` (parties).

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode` = `P` (wholly obtained) for granulate made from waste — refuted: goods produced exclusively from manufacturing waste and scrap of a country can count as wholly obtained there under common rules of origin (own knowledge) (from broad).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode` = `1000` although the goods are in a bonded store — refuted: temporary storage is not a customs procedure (from broad and context); the merge agrees on this aspect; the previous declaration is F8.
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID`: a declaration made to another country's customs — broad refuted it (common practice); the merge cannot settle it and keeps it as F8 (from broad).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:InsuranceValueAmount` = `0.00` as a filler — refuted: an explicit "uninsured" is meaningful under CPT and consistent with the value declared for carriage in 06 (from money).
- Two decimals in XBL against none in XUF documents — refuted: different currencies may have different minor units (from money).
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`: an import declaration should name an entry office instead — logistics refuted it (the model offers only the exit office); the merge agrees there is no element for the entry office, but keeps the presence question as F5 (from logistics).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:DangerousGoodsApprovedIndicator` = `false`: storage data copied without use — logistics left it to context and found the conditions fit PE granulate; the merge keeps it in F10 (from logistics).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` could be real — refuted: real ICDs stay far below 0990 (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID`: BIC-shaped `BLUMXBLX` could be real — refuted: fictional country code in positions 5–6 (from parties).
- `/ImportCustomsDeclaration/cac:NotifierParty`: the importer as notifier, a role mix-up — parties refuted it; the merge keeps the redundancy as F12 (from parties).
- `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount`: the bank account has a use through the note — context refuted the copied-data point; the merge keeps it within F7 (from context).
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description[2]` tagged `en-XB` here and `en-XU` in 05 — refuted: the tag follows the declarant's variety of English, legitimate for the declarant's own text (from context); for party master data see F20.

## Refuted in the merge
### logistics/F1 (part) · Medium · Goods item quantity is a weight in tonnes
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `120`
- Why (logistics): `GoodsItem/Quantity` is "the number of units making up this goods item"; 120 TNE is the mass that `CustomsTariffQuantity` already gives as 120 000 KGM; the units are the 120 bags. Condition: `Quantity` counts units (bags) or is absent. Options: drop `Quantity` (preferred), or a count of bags.
- Refuted because: a UBL Quantity is a number of units of any unit of measure; the tonne is a legitimate unit for a bulk commodity sold, carried and invoiced by the tonne (10: 120 TNE), and the tariff quantity has its own, customs-specific meaning; the repetition is not a misuse (as plastics/06, logistics/F7). The rest of logistics/F1 (packages and net weight not declared) is kept as F9.

## Changed in the merge
- broad/F2, context/F1 → F5: lowered from Medium to Low with Needs decision yes, because logistics' refutation holds for the meaning (the model offers only this office, and the value fits the definition literally); only the presence question remains.
- broad/F3 → F4 and F10: split; MeasureCode (Medium, definition's condition not met) combined with context/F2; the non-refrigerated temperature limits moved to the storage-data finding, with the AMBIENT attribute noted.
- money/F2, broad/F8 (first part), parties/F5 → F7: combined (same account, same question), Needs decision yes from money.
- logistics/F2, context/F7 → F8: combined; broad's refutation carried as counter-argument.
- logistics/F1 → F9: lowered from Medium to Low; the Quantity part refuted (see above); the missing package data is a completeness remark.
- broad/F6, context/F6 → F10: combined with broad/F3's second part; logistics' remark added.
- broad/F7, context/F8 → F12: kept against parties' refutation.
- parties/F11 → F13: combined with broad's "Outside this review" note.
- broad/F8 (second part), parties/F6, context/F10 → F14: Needs decision no (parties said yes).
- broad/F11, parties/F7, context/F12 → F17: Needs decision yes (parties said no).
- parties/F8, parties/F9 → F20: combined, Needs decision yes.
- broad/F5, parties/F2, context/F5 → F3: preferred option set to dropping LocaleCode.
- Combined without change of severity: broad/F1, parties/F3, context/F3 → F1; broad/F4, parties/F1, context/F4 → F2; broad/F9, parties/F4, context/F11 → F15; broad/F10, context/F9 → F16; parties/F10, context/F13 → F18; broad/F12 → F19; money/F1 → F6; logistics/F3 → F11.

## Outside this review
- Whether the Marrowdale border office (Upland State) is the competent office for goods arriving by river at Lumeport (Coastal State) is a location question across documents (from broad; the contact's fit is F13).
