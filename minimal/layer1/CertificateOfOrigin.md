# CertificateOfOrigin

**UBL definition:** A document that describes the Certificate of Origin.

- **Status:** endorsed document type
- **Locale:** US, currency USD, language `en`, UTC offset -04:00
- **Values shown:** every value in `CertificateOfOrigin.xml`, in document order.

| Element | Value | Present because | Value because |
|---|---|---|---|
| `cbc:ID` | CertificateOfOrigin-1 | required by the schema | the document type + 1 |
| `cac:CertificateOfOriginApplication/cbc:ReferenceID` | ReferenceID-121 | required by the schema | its own label + a number unique across the set |
| `cac:CertificateOfOriginApplication/cbc:CertificateType` | Ordinary (languageID="en") | required by the schema | a hazardous waste shipped across borders for recycling (Basel A1160) from the definition's examples |
| `cac:CertificateOfOriginApplication/cbc:OriginalJobID` | OriginalJobID-121 | required by the schema | its own label + a number unique across the set |
| `cac:CertificateOfOriginApplication/cac:Shipment/cbc:ID` | Shipment-121 | ShipmentType: "an identifiable collection of one or more goods items". Its ID is a transaction reference like the document's own ID, assigned within the exchange, not taken from a register. | its own label + a number unique across the set |
| `cac:CertificateOfOriginApplication/cac:Shipment/cac:OriginAddress/cac:Country/cbc:IdentificationCode` | US | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:CertificateOfOriginApplication/cac:EndorserParty/cbc:RoleCode` | EMBASSY | required by the schema | from the definition's examples (issuer, embassy, insurance): the issuer endorses first, an embassy legalizes after it |
| `cac:CertificateOfOriginApplication/cac:EndorserParty/cbc:SequenceNumeric` | 2 | required by the schema | the order in its sequence, from 1 |
| `cac:CertificateOfOriginApplication/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` | Example Endorser 121 (languageID="en") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` | Alex Example (languageID="en") | ContactType: only SignatoryContact so far, "the individual ... who signs". A signature needs the person's name, despite UBL's advice to use a functional rather than a personal name. | (en, de, pt-BR, ja-Latn-hepburn); visibly fictitious |
| `cac:CertificateOfOriginApplication/cac:PreparationParty/cac:PartyName/cbc:Name` | Example Preparer 122 (languageID="en") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:CertificateOfOriginApplication/cac:IssuerParty/cac:PartyName/cbc:Name` | Example Issuer 123 (languageID="en") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:CertificateOfOriginApplication/cac:IssuingCountry/cbc:IdentificationCode` | US | CountryType: the ISO 3166-1 code is exact and language-neutral; the value comes from the document's locale. | the document's locale country (ISO 3166-1) |
| `cac:IssuerEndorsement/cbc:DocumentID` | DocumentID-121 | required by the schema | its own label + a number unique across the set |
| `cac:IssuerEndorsement/cbc:ApprovalStatus` | Approved (languageID="en") | required by the schema | a hazardous waste shipped across borders for recycling (Basel A1160) |
| `cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode` | ISSUER | required by the schema | from the definition's examples (issuer, embassy, insurance): the issuer endorses first, an embassy legalizes after it |
| `cac:IssuerEndorsement/cac:EndorserParty/cbc:SequenceNumeric` | 1 | required by the schema | the order in its sequence, from 1 |
| `cac:IssuerEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` | Example Issuer 123 (languageID="en") | within PartyName, added because: PartyType ("an organization, sub-organization, or individual fulfilling a role"): who it is. A name stands on its own; an ID would need a schemeID, which is a later layer's decision (IND6). | Example + the party's role in the locale's language + its number |
| `cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` | Sam Example (languageID="en") | ContactType: only SignatoryContact so far, "the individual ... who signs". A signature needs the person's name, despite UBL's advice to use a functional rather than a personal name. | (en, de, pt-BR, ja-Latn-hepburn); visibly fictitious |

Generated by `minimal/gen_minimal.py` from the reasons recorded in it; do not edit by hand.
