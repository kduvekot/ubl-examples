# LLM review: 05-ExportCustomsDeclaration.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/05-ExportCustomsDeclaration.xml`, Git blob `a5a3199bc1d430c4bdf148c1d2afa50b7ca50c54` (committed)
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

### plastics/05#F1 · Medium · Customs administration described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The customs party is a public authority (ISIC `8411`). A state administration is not registered in a commercial register and cannot be in liquidation; CompanyLiquidationStatusCode ("the party's liquidation status") and a commercial registration scheme describe a company. The checklist names this case ("a public body … is not a company in a commercial register and has no liquidation status").
- Condition: the customs administration's legal entity carries no commercial-register scheme and no liquidation status; if it has a registration, it is in a register for public bodies with a matching type code.
- Options: (a) drop the corporate registration scheme and the liquidation status for public bodies, keeping name and, if any, a public-sector identifier (preferred); (b) use a public-body register with its own type code.
- Needs decision: no

### plastics/05#F2 · Medium · Province of Urvanian addresses in Region
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province belongs in `CountrySubentity`, as the Bayvarran addresses do. No `languageID`. 219 occurrences in the world.
- Condition: no Urvanian province in `cbc:Region`; it is in `cbc:CountrySubentity` (+ code).
- Options: (a) move to `CountrySubentity` (preferred); (b) keep only if documented as an economic region.
- Needs decision: no

### plastics/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (ISO 639) is the language already in `Language/ID`. 362 occurrences in 213 examples.
- Condition: a locale such as `en-XB` from a locale list, or no `LocaleCode`.
- Options: (a) `en-XB` (preferred); (b) drop it.
- Needs decision: no

### plastics/05#F4 · Low · Reference to the order with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `RP-PO-26-0882`
- Why: The reference has no document type, so customs cannot tell what `RP-PO-26-0882` is (it is the buyer's order, `01-Order.xml`). The checklist asks that a reference with only an ID say what it refers to where that is not obvious.
- Condition: the reference states its document type (order).
- Options: (a) add `DocumentTypeCode` (and issue date) (preferred); (b) reference the commercial document customs actually relies on, with its type.
- Needs decision: no

### plastics/05#F5 · Low · No mode of transport at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `RR-SH-26-0889`
- Why: The declaration names the carrier and the exit office (`Customs post at the river border`) but not the mode or means of transport with which the goods leave (inland waterway, barge `Fiumella IV`, see `06-Waybill.xml`). Export declarations normally state the mode of transport at the border (own knowledge of customs practice); the shipment has no shipment stage.
- Condition: the declaration states the mode (and, if required, the means) of transport at the border.
- Options: (a) add a main-carriage shipment stage with `TransportModeCode` `8` and the vessel (preferred); (b) the mode only.
- Needs decision: no

### plastics/05#F6 · Low · Copied master data: consignee's bank account and the waste permit
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`
- Why: Export customs does nothing with the consignee's bank account. The exporter's waste-recovery permit (Basel Annex IV `R3`) is irrelevant for the export of a product (HS 390110) and, in an export declaration, could suggest a transboundary waste shipment that would need its own procedure.
- Condition: neither appears in the export declaration.
- Options: remove both (preferred).
- Needs decision: no

### plastics/05#F7 · Low · Exporter's contact is customer service; consignee's contact is a sales desk
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Order desk`
- Why: Customs needs the exporter's contact for the declaration (shipping/customs), not sales customer service; the consignee's contact is a sales order desk.
- Condition: contacts fit the customs roles.
- Options: role-specific contacts (preferred) or neutral general contacts.
- Needs decision: no

### plastics/05#F8 · Low · Signature ID contains the flow's name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `RR-SIG-EX-plastics`
- Why: `plastics` is the name of the example flow, not something a party would put in a signature identifier; it reads as a generator artefact. Signature IDs ending in a flow name occur in 14 examples (`grep -rlE --include='*.xml' -- '-SIG-[A-Z]+-[a-z]+<' world/examples | wc -l`).
- Condition: the signature ID is an identifier the signing party would assign (e.g. derived from the declaration).
- Options: derive it from the declaration number (preferred).
- Needs decision: no

### plastics/05#F9 · Low · All three companies registered on 1 January 1996
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The same default-looking date for three companies in two registers (271 occurrences in the world).
- Condition: individual dates, or the shared date explained in the world's history.
- Options: (a) individual dates (preferred); (b) document it.
- Needs decision: yes

### plastics/05#F10 · Low · Item number in the world scheme is a valid GTIN-12
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771030000048`
- Why: 12 digits with a correct GS1 check digit (8), in the GTIN-12 (UPC) range; could be taken for a real GTIN although its scheme is the world's own (see `01-Order.xml`, same value).
- Condition: the number cannot be mistaken for a real GTIN, or it is verified as unassigned and documented.
- Options: (a) a non-GTIN format for world item numbers (preferred); (b) document the verification.
- Needs decision: yes

## Checked and consistent
- Consignment `RR-CS-26-0885`, shipment `RR-SH-26-0889`, gross weight 120 480 kg, quantity 120 t, HS 390110, origin XU agree with `03`, `04`, `06` and `08`.
- Declared value 9 984 000 XUF = order and invoice total (`01-Order.xml`, `10-Invoice.xml`).
- Shipment gross weight equal to goods-item gross weight is consistent: no transport equipment (bags in the barge hold).
- Export type permanent, reason sale, consignor and exporter Rinova, consignee Rivermouth: consistent with the order.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount`: the declared value includes carriage beyond the border (CPT Lumeport) — refuted as a finding: the world's export valuation rule is not visible here, and declaring the invoice value is common practice for export statistics.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID`: VAT registration of a customs administration — refuted: public bodies can be VAT-registered.

## Outside this review
- The note says the goods are "Declared electronically before the goods leave", but the declaration is issued at 16:08 on 2026-04-19, after the actual despatch stated in `06-Waybill.xml` (15:10 the same day); it is before the exit from Urvania (2026-04-20 16:00). Timeline across documents.
