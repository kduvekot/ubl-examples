# LLM review: 09-ImportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/09-ImportCustomsDeclaration.xml`, Git blob `f2d4fcae7f399f23e32926db94e2eab6ad1dd2dc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/09#F1 · Medium · Customs service described as a company in the business register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The customs party is a public authority (ISIC `8411`); it is shown in the federal business register as a commercial registration and with a liquidation status ("the party's liquidation status"), which describe companies. The checklist names this case. The Urvanian customs administration has the same problem in `05-ExportCustomsDeclaration.xml`.
- Condition: the customs service's legal entity carries no commercial registration and no liquidation status; any registration is in a register for public bodies with a matching type.
- Options: (a) drop registration scheme and liquidation status for public bodies (preferred); (b) a public-body register with its own type code.
- Needs decision: no

### plastics/09#F2 · Medium · Exit office of the exporting country in the import declaration; office of entry missing
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`
- Why: CustomsExitOfficeLocation is the "Customs exit office of the goods being declared". The goods leave Urvania at that post (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the river border`); for an import into Bayvarra they are not leaving any customs territory, and what the Bayvarran declaration needs is where they entered and are presented (the river quay, Lumeport, or the Bayvarran border post). The name alone also does not say on which side of the border the post is.
- Condition: the import declaration does not present an exit office as if it were its own; the place of entry or presentation in Bayvarra is identifiable.
- Options: (a) remove the exit office and identify the Bayvarran office of entry/presentation (preferred); (b) if the Urvanian exit office is meant as information for the importing customs, name it unambiguously as Urvanian.
- Needs decision: no

### plastics/09#F3 · Medium · Temperature code given together with a measured value
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:MeasureCode` = `MIN`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cac:MinimumTemperature/cbc:Measure` = `5`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:RefrigeratedIndicator` = `false`
- Why: Temperature/MeasureCode is "A code describing the temperature, when not expressed as a measure"; here the temperature is expressed as a measure (5 °C), and `MIN` only repeats that it is the minimum, which the parent `MinimumTemperature` already says. Storage/MinimumTemperature and MaximumTemperature are defined for "this refrigerated storage", but the storage says it is not refrigerated; for a frost-free store the limits may still be meant as ambient limits.
- Condition: `MeasureCode` is absent when `Measure` is given; temperature limits on the storage fit its definition (refrigerated storage) or are expressed where their meaning fits.
- Options: (a) drop `MeasureCode` and, unless the store's temperature limits matter to the declaration, the temperatures as well (preferred); (b) keep the limits and document that they are ambient limits of a non-refrigerated store.
- Needs decision: no

### plastics/09#F4 · Medium · Province of the consignor's address in Region
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as in the Bayvarran addresses of the same declaration. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/09#F5 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/09#F6 · Low · Storage properties of the bonded store that the declaration does not use
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:HumidityPercent` = `60`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:AirFlowPercent` = `0`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:BondedWarehouseLocation/cac:Storage/cbc:PowerIndicator` = `true`
- Why: For customs, the bonded store's identity and licence matter. Humidity, airflow, power supply and food or dangerous-goods approvals are properties of the hall that this declaration for PE granulate in bags does nothing with (section 4.8).
- Condition: the bonded-store location carries what the declaration needs (identity, licence, hall), and storage properties only where the goods require them.
- Options: (a) keep ID, name, gate and licence, drop the physical properties (preferred); (b) keep them only if the world's customs rules ask for them.
- Needs decision: no

### plastics/09#F7 · Low · Notifier is the importer itself
- XPath: `/ImportCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Rivermouth Packaging`
- Why: NotifierParty is "The Party who is responsible for contact on master level". It repeats the importer and consignee (the declarant), so it adds no party and no information.
- Condition: a notifier is present only if it is a party other than the declarant, or its presence has a stated reason.
- Options: remove it (preferred).
- Needs decision: no

### plastics/09#F8 · Low · Copied master data: importer's bank account and the consignor's waste permit
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: Duties are paid "by the importer's account at customs" (`/ImportCustomsDeclaration/cbc:Note`), i.e. a customs (deferment) account, not this bank account. The consignor's waste-recovery permit is irrelevant to importing a product (HS 3901.10) and could suggest a waste shipment.
- Condition: neither appears in the declaration, or the bank account is the one from which duties are actually collected and the note says so.
- Options: (a) remove both (preferred); (b) identify the customs account in the declaration instead.
- Needs decision: no

### plastics/09#F9 · Low · Importer's contact is a sales order desk
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: The importer's contact for its customs declaration is a sales customer-service officer, not the person responsible for imports or customs.
- Condition: the importer's contact is a customs/import function.
- Options: a role-specific contact (preferred) or a neutral general contact.
- Needs decision: no

### plastics/09#F10 · Low · Signature ID contains the flow's name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `RP-SIG-IM-plastics`
- Why: `plastics` is the example flow's name; a generator artefact, not an identifier the importer would assign. 14 examples have such signature IDs (`grep -rlE --include='*.xml' -- '-SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: the signature ID is one the signing party would assign.
- Options: derive it from the declaration number (preferred).
- Needs decision: no

### plastics/09#F11 · Low · Both companies registered on 1 January 1996
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for two companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

### plastics/09#F12 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8) in the GTIN-12 (UPC) range; it could be taken for a real GTIN (see `01-Order.xml`).
- Condition: the number cannot be mistaken for a real GTIN, or it is verified as unassigned and documented.
- Options: (a) a non-GTIN format (preferred); (b) document the verification.
- Needs decision: yes

## Checked and consistent
- Values: customs value 99 840.00 XBL = 9 984 000 XUF at 100 XUF per XBL; FOB value 98 046.00 XBL = 99 840.00 − 1 794.00, and 1 794 XBL = 179 400 XUF, the freight of `06-Waybill.xml`/`07-Invoice.xml`. Insurance 0 fits CPT, which does not require insurance. Statistical value = customs value.
- Shipment `RR-SH-26-0889`, gross 120 480 kg, 120 t, tariff quantity 120 000 kg, HS 3901.10, origin XU agree with `05`, `06`, `08`.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:AdditionalDocumentReference/cbc:ID` = `FB-WB-26-0890` resolves to `06-Waybill.xml`; `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `RR-CD-26-0888` is the customs declaration ID of `05-ExportCustomsDeclaration.xml`.
- Issued 2026-04-22 10:35, after the discharge at 08:00 the same day.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:CustomsProcedureCode`: `1000` (no previous procedure) although the goods are in a bonded store — refuted: the store is described as temporary storage ("where this goods item is temporarily stored"), which is not a customs procedure, and the export in Urvania is not a procedure of Bayvarra's customs territory.
- `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:PreferenceCriterionCode`: `P` (wholly obtained) for granulate made from waste — refuted: under common rules of origin, goods produced exclusively from waste and scrap of manufacturing in a country can count as wholly obtained there (own knowledge).
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID`: a previous declaration made to another country's customs — refuted: citing the export declaration of the country of dispatch is common practice.

## Outside this review
- The customs party's address is a border office in Marrowdale (Upland State), while the goods are discharged and stored at the river quay in Lumeport (Coastal State); whether that office is the competent one for goods arriving by river at Lumeport is a location question across documents.
