# WasteNotification

**UBL definition:** A document used to notify the competent authorities of planned movements of waste.

- **Status:** endorsed document type
- **Locale:** DE, currency EUR, language `de`, UTC offset +02:00
- **Values shown:** every value in `WasteNotification.xml`, in document order.

| Element | Value | Present because | Value because |
|---|---|---|---|
| `cbc:ID` | WasteNotification-1 | required by the schema | the document type + 1 |
| `cbc:IssueDate` | 2026-08-12 | required by the schema | D = 2026-08-12, the UBL 2.5 publication date |
| `cac:SenderParty/cac:PartyName/cbc:Name` | Beispielabsender 971 (languageID="de") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:SenderParty/cac:PartyTaxScheme/cbc:CompanyID` | DE990009712 | PartyTaxScheme carries the party's national tax number ("an identifier for the party assigned for tax purposes by the taxation authority") | national number, DE (VIES: not valid) |
| `cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` | Umsatzsteuer (languageID="de") | TaxScheme is required in PartyTaxScheme: the particular tax scheme gets a name, as other particular things do. | the official name of the scheme, in the locale's language |
| `cac:SenderParty/cac:PartyTaxScheme/cac:TaxScheme/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` | DE | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:ReceiverParty/cac:PartyName/cbc:Name` | Beispielempfänger 972 (languageID="de") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:ReceiverParty/cac:PartyTaxScheme/cbc:CompanyID` | DE990009729 | PartyTaxScheme carries the party's national tax number ("an identifier for the party assigned for tax purposes by the taxation authority") | national number, DE (VIES: not valid) |
| `cac:ReceiverParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` | Umsatzsteuer (languageID="de") | TaxScheme is required in PartyTaxScheme: the particular tax scheme gets a name, as other particular things do. | the official name of the scheme, in the locale's language |
| `cac:ReceiverParty/cac:PartyTaxScheme/cac:TaxScheme/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` | DE | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:NotifierParty/cac:PartyName/cbc:Name` | Beispielnotifizierender 973 (languageID="de") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:NotifierParty/cac:PartyTaxScheme/cbc:CompanyID` | DE990009737 | PartyTaxScheme carries the party's national tax number ("an identifier for the party assigned for tax purposes by the taxation authority") | national number, DE (VIES: not valid) |
| `cac:NotifierParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` | Umsatzsteuer (languageID="de") | TaxScheme is required in PartyTaxScheme: the particular tax scheme gets a name, as other particular things do. | the official name of the scheme, in the locale's language |
| `cac:NotifierParty/cac:PartyTaxScheme/cac:TaxScheme/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` | DE | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:CustomsParty/cac:PartyName/cbc:Name` | Beispielzollbehörde 974 (languageID="de") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:WasteProducerParty/cac:PartyName/cbc:Name` | Beispielabfallerzeuger 975 (languageID="de") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:WasteProducerParty/cac:PartyTaxScheme/cbc:CompanyID` | DE990009753 | PartyTaxScheme carries the party's national tax number ("an identifier for the party assigned for tax purposes by the taxation authority") | national number, DE (VIES: not valid) |
| `cac:WasteProducerParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name` | Umsatzsteuer (languageID="de") | TaxScheme is required in PartyTaxScheme: the particular tax scheme gets a name, as other particular things do. | the official name of the scheme, in the locale's language |
| `cac:WasteProducerParty/cac:PartyTaxScheme/cac:TaxScheme/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` | DE | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:Shipment/cbc:ID` | Shipment-971 | ShipmentType: "an identifiable collection of one or more goods items". Its ID is a transaction reference like the document's own ID, assigned within the exchange, not taken from a register. | its own label + a number unique across the set |
| `cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description` | Gebrauchte Blei-Säure-Batterien (languageID="de") | ItemType: "an item of trade. It includes a generic description applicable to all examples of the item"; a Name is only "optionally given". Identification depends on the document's perspective (buyer, seller, standard): a later layer. | (en, de, pt-BR, ja-Latn-hepburn) |

Generated by `minimal/gen_minimal.py` from the reasons recorded in it; do not edit by hand.
