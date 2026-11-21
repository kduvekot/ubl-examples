# Common Transportation Report: Tidewell Ocean Lines to Port of Lumeport

*Example 14 of the flow "Cotton: from the island's farms to the textile mill (Lisavu → Bayvarra)" · [Common Transportation Report in the UBL 2.5 specification](https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html#S-COMMON-TRANSPORTATION-REPORT-SCHEMA)*

Before entering Lumeport the carrier reports its second feeder to the port. The ship came under Bayvarra's flag in January, so it sails with an interim security certificate, and it carries a sanitation control exemption certificate, as the inspection at Lumeport in January found no control measures needed.

[The XML file](14-CommonTransportationReport.xml) is valid against the UBL 2.5 schemas and the world's code lists. Below, every value with its place in the document and the reason for it.

## Values and their reasons

### The document itself

- `UBLVersionID` = **2.5**  
  The earliest version of UBL 2 that defines every element of the document, as UBLVersionID asks: computed from the published models of UBL 2.0 to 2.5; Party/ElectronicAddress first appears in UBL 2.5.
- `CustomizationID` = **urn:ubl-examples:world:trns:common-transportation-report:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0**  
  The specification the document follows, at each level it claims, chained with #compliant#: the Trade Accord's transaction "Common transportation report"; the community specification "Lumeport port community". Each has a public description on the world's pages.
- `ProfileID` = **urn:ubl-examples:world:profile:transport:1.0**  
  The Trade Accord's process profile the document belongs to: transport, a generic, versioned profile, not the flow.
- `ProfileExecutionID` = **9900667463**  
  The collaboration this document belongs to: Tidewell's report of the second feeder's arrival at Lumeport to the port. Tidewell Ocean Lines started it and gave it this identifier, which every document of it repeats.
- `ID` = **8600033374**  
  The carrier's report number.
- `UUID` = **149f7421-1d43-5c08-9504-00a7ea0b615b**  
  A universally unique identifier of the document, derived from its place in the world (UUID version 5), so it stays the same on every build.
- `IssueDate` = **2026-05-08**  
  Sent the day before the ship enters Lumeport.
- `IssueTime` = **11:22:00-01:00**  
  The time the sender's system issued the document, in the sender's local time, with its offset from UTC.
- `ReportTypeCode` = **PREARRIVAL** (listID `urn:ubl-examples:world:codelist:TransportReportTypeCode`)  
  The report before entering the port. The code is from the Trade Accord's transport report type list: PREARRIVAL = Pre-arrival report.
- `ReportType` = **Pre-arrival report**  
  The name of code PREARRIVAL in the Trade Accord's transport report type list.

### Reporter Party

Inside `ReporterParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The trading name; as Tidewell Ocean Lines gives it.
- `Language/ID` = **en** (schemeID `ISO 639`)  
  English, the language the party writes in this document. The code is from the world's copy of ISO 639 Language: en = English. An identifier that holds a code names the code's list in its schemeID.
- `Language/Name` = **English**  
  The language's name.
- `Language/LocaleCode` = **en-XB** (listID `urn:ubl-examples:world:codelist:LocaleCode`)  
  The English the party writes: the variety of Bayvarra, with the country as the region; English is used in all three countries, so its locale says which. The code is from the Trade Accord's locale list: en-XB = Bayvarran English.
- `PostalAddress/ID` = **LUM-ADR-547539** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Tidewell Ocean Lines gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/BuildingNumber` = **18**  
  Building number of the postal address. As Tidewell Ocean Lines gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Tidewell Ocean Lines gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Tidewell Ocean Lines gives it.
- `PostalAddress/PostalZone` = **38527**  
  Postal code in Bayvarra's format (5 digits). As Tidewell Ocean Lines gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Tidewell Ocean Lines gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `Contact/Name` = **Bookings**  
  The party's main desk, which handles this document; as Tidewell Ocean Lines gives it.
- `Contact/JobTitle` = **Booking agent**  
  The job of the person who answers at the desk; as Tidewell Ocean Lines gives it.
- `Contact/Department` = **Bookings**  
  The department the desk belongs to; as Tidewell Ocean Lines gives it.
- `Contact/Telephone` = **+999 2 38 2058 7929**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Tidewell Ocean Lines gives it.
- `Contact/ElectronicMail` = **bookings@tidewell.example**  
  The contact's e-mail address; as Tidewell Ocean Lines gives it.
- `Contact/Note` = **Every day 06:00–22:00**  
  When the desk can be reached; as Tidewell Ocean Lines gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411918** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Tidewell Ocean Lines gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Authority Party

Inside `AuthorityParty`:

- `PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  The party's preferred identifier: its number in the Federal business register of Bayvarra; as Port of Lumeport gives it. Later mentions of the same party in this document repeat only this identifier and the name.
- `PartyName/Name` = **Port of Lumeport**  
  The trading name; as Port of Lumeport gives it.
- `PostalAddress/ID` = **LUM-ADR-030762** (schemeID `urn:ubl-examples:world:XB:lumeport:address-register`)  
  The address's number in the address register of the City of Lumeport (LUM-ADR- and six digits; the city keeps its own register, which the state register of Coastal State refers to); as Port of Lumeport gives it.
- `PostalAddress/AddressTypeCode` = **BUSINESS** (listID `urn:ubl-examples:world:codelist:AddressTypeCode`)  
  The kind of address. The code is from the Trade Accord's address type list: BUSINESS = Business address.
- `PostalAddress/AddressFormatCode` = **XB** (listID `urn:ubl-examples:world:codelist:AddressFormatCode`)  
  The address follows Bayvarra's address format, one line after the other, a line left out when the address has none of its fields: MarkAttention; Department; InhouseMail; Postbox; BuildingName; Floor Room; BuildingNumber StreetName; AdditionalStreetName; BlockName PlotIdentification; CitySubdivisionName; CityName CountrySubentity PostalZone. A line is made of the fields named in it, in that order, separated by a space; a field the address does not have is left out, and a line without any field is left out. A field with two language versions (street and town names in a bilingual country) gives both on the line, the national language first, then ' / ', then English: the building number is written once. Fields that are not on a line (ID, AddressTypeCode, CountrySubentityCode, TimezoneOffset, LocationCoordinate) say something other than where the post goes. The country is the last line of a postal address and is not repeated in the lines. The code is from the Trade Accord's address format list: XB = Address format of Bayvarra.
- `PostalAddress/StreetName` = **Harbour Road**  
  Street of the postal address. As Port of Lumeport gives it.
- `PostalAddress/BuildingNumber` = **11**  
  Building number of the postal address. As Port of Lumeport gives it.
- `PostalAddress/CitySubdivisionName` = **Dockside**  
  The quarter of Lumeport the party is in: one of the town's districts on the map. As Port of Lumeport gives it.
- `PostalAddress/CityName` = **Lumeport**  
  The town or locality nearest to the party's place on the map, in its own country and state. As Port of Lumeport gives it.
- `PostalAddress/PostalZone` = **38526**  
  Postal code in Bayvarra's format (5 digits). As Port of Lumeport gives it.
- `PostalAddress/CountrySubentity` = **Coastal State**  
  The name of code XB-CO in Bayvarra's national state or territory list.
- `PostalAddress/CountrySubentityCode` = **XB-CO** (listID `urn:ubl-examples:world:XB:codelist:CountrySubentityCode`)  
  The state or territory as a code of Bayvarra's address scheme. As Port of Lumeport gives it. The code is from Bayvarra's national state or territory list: XB-CO = Coastal State.
- `PostalAddress/TimezoneOffset` = **-01:00**  
  The offset from UTC of Bayvarran Time, Bayvarra's legal time, all year: there is no summer time.
- `PostalAddress/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  Bayvarra, by its code in the world's country code list. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `PostalAddress/Country/Name` = **Bayvarra**  
  The country's name, for readers of the address.
- `PhysicalLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `PhysicalLocation/Description` = **Port of Lumeport**  
  Where the party actually operates, apart from its postal address.
- `PhysicalLocation/InformationURI` = **https://www.port-lumeport.example**  
  A page about the place itself: the port's or the airport's own site, with its access and services.
- `PhysicalLocation/SubsidiaryLocation/Name` = **Container quay**  
  A part of the port with its own location: where containers are handled.
- `PhysicalLocation/LocationCoordinate/CoordinateSystemCode` = **4326** (listID `EPSG`)  
  The World Geodetic System 1984, as used by satellite navigation. The code is from the world's copy of EPSG Geodetic Parameter Dataset (coordinate reference systems): 4326 = WGS 84.
- `PhysicalLocation/LocationCoordinate/LatitudeDegreesMeasure` = **31** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `PhysicalLocation/LocationCoordinate/LatitudeMinutesMeasure` = **6.22** (unitCode `D61`)  
  The minutes of the latitude.
- `PhysicalLocation/LocationCoordinate/LatitudeDirectionCode` = **South** (listID `urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode`)  
  South of the equator. The code is from the world's copy of UBL's Latitude direction list, with a listID: South.
- `PhysicalLocation/LocationCoordinate/LongitudeDegreesMeasure` = **13** (unitCode `DD`)  
  Computed from the place on the map; the world lies in an empty part of the South Atlantic, so the point is open sea on a real map.
- `PhysicalLocation/LocationCoordinate/LongitudeMinutesMeasure` = **23.07** (unitCode `D61`)  
  The minutes of the longitude.
- `PhysicalLocation/LocationCoordinate/LongitudeDirectionCode` = **West** (listID `urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode`)  
  West of the Greenwich meridian. The code is from the world's copy of UBL's Longitude direction list, with a listID: West.
- `Contact/Name` = **Port control**  
  The party's main desk, which handles this document; as Port of Lumeport gives it.
- `Contact/JobTitle` = **Duty port controller**  
  The job of the person who answers at the desk; as Port of Lumeport gives it.
- `Contact/Department` = **Port operations**  
  The department the desk belongs to; as Port of Lumeport gives it.
- `Contact/Telephone` = **+999 2 38 8964 6053**  
  Telephone under +999, a country code the ITU reserves for a future global service (ITU-T E.164), so the number reaches no one; then the country digit and a number in Bayvarra's own plan: British-style closed numbering: always 10 digits after the country digit; the area code takes 2 or 4 of them, and its first digit gives the region: 3 the coast (Lumeport 38), 5 Upland (Upland State 5121, Harrowmead 5164), 1 the Northern Territory (Gullhaven 1563); the plan is national and follows regions, not state borders. No area code is the start of another, and the trunk prefix 0 is dropped from abroad. Mobiles start with 7, and nothing else does. As Port of Lumeport gives it.
- `Contact/ElectronicMail` = **port@port-lumeport.example**  
  The contact's e-mail address; as Port of Lumeport gives it.
- `Contact/Note` = **Every day, around the clock**  
  When the desk can be reached; as Port of Lumeport gives it.
- `ElectronicAddress/ExchangeNetworkID` = **urn:ubl-examples:world:network**  
  The network in which the address is registered: the world's own exchange network.
- `ElectronicAddress/ElectronicAddressID` = **XB:20411781** (schemeID `urn:ubl-examples:world:endpoint`)  
  The party's electronic address in that network: its country code and its number in the Federal business register of Bayvarra; as Port of Lumeport gives it. UBL 2.5 carries it here; Party/EndpointID is deprecated.

### Sender Party

Inside `SenderParty`:

- `PartyIdentification/ID` = **20411918** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Tidewell Ocean Lines**  
  The same party as at ReporterParty, where its full details are given; only its identifier and name are repeated.

### Receiver Party

Inside `ReceiverParty`:

- `PartyIdentification/ID` = **20411781** (schemeID `urn:ubl-examples:world:XB:register`)  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.
- `PartyName/Name` = **Port of Lumeport**  
  The same party as at AuthorityParty, where its full details are given; only its identifier and name are repeated.

### Shipment

Inside `Shipment`:

- `ID` = **7400667463**  
  The carrier's shipment number for the voyage's cargo.
- `ShipmentStage/ID` = **1**  
  The sea leg from Selanu to Lumeport.
- `ShipmentStage/TransportModeCode` = **1** (listID `UNECE Recommendation 19 - Codes for Modes of Transport`)  
  Maritime transport. The code is from UBL's default Transport mode (UNECE Recommendation 19) list: 1 = Maritime transport.
- `ShipmentStage/LoadingPortLocation/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/LoadingPortLocation/Name` = **Port of Selanu**  
  The ship's last port of call, where it loaded the cargo it brings.
- `ShipmentStage/LoadingPortLocation/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/UnloadingPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/UnloadingPortLocation/Name` = **Port of Lumeport**  
  The port the report is for.
- `ShipmentStage/UnloadingPortLocation/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/ActualDepartureTransportEvent/OccurrenceDate` = **2026-05-07**  
  The ship left Selanu on the afternoon of Thursday 7 May, in island time.
- `ShipmentStage/ActualDepartureTransportEvent/OccurrenceTime` = **14:00:00+00:00**  
  The local time.
- `ShipmentStage/ActualDepartureTransportEvent/Location/ID` = **XLSEL** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/ActualDepartureTransportEvent/Location/Name` = **Port of Selanu**  
  The port of departure.
- `ShipmentStage/ActualDepartureTransportEvent/Location/Address/Country/IdentificationCode` = **XL** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XL = Lisavu.
- `ShipmentStage/EstimatedArrivalTransportEvent/OccurrenceDate` = **2026-05-09**  
  Expected at Lumeport after about 48 hours at sea, in Lumeport's time, an hour behind the island's.
- `ShipmentStage/EstimatedArrivalTransportEvent/OccurrenceTime` = **12:50:00-01:00**  
  The local time.
- `ShipmentStage/EstimatedArrivalTransportEvent/Location/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's code in the form of a UN/LOCODE, with the world's country code.
- `ShipmentStage/EstimatedArrivalTransportEvent/Location/Name` = **Port of Lumeport**  
  The port of arrival.
- `ShipmentStage/EstimatedArrivalTransportEvent/Location/Address/Country/IdentificationCode` = **XB** (listID `ISO 3166`)  
  The country the place is in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra.
- `ShipmentStage/ReportingPerson/FirstName` = **Hester**  
  The master.
- `ShipmentStage/ReportingPerson/FamilyName` = **Calloway**  
  The family name.
- `ShipmentStage/ReportingPerson/RoleCode` = **MASTER** (listID `urn:ubl-examples:world:codelist:ShipPersonRoleCode`)  
  The person's role on board. The code is from the Trade Accord's role on board list: MASTER = Master.
- `ShipmentStage/ISPSRequirements/ID` = **IISSC-XB-2026-0115**  
  The number of the ship's interim International Ship Security Certificate.
- `ShipmentStage/ISPSRequirements/ValidISSCIndicator` = **true**  
  The ship holds a valid certificate: an interim certificate under ISPS Code A/19.4 is valid for its six months, and the ship trades on it as on a full one.
- `ShipmentStage/ISPSRequirements/ISSCExpiryDate` = **2026-07-14**  
  The interim certificate's last day: six months, the most the ISPS Code allows.
- `ShipmentStage/ISPSRequirements/SSPOnBoardIndicator` = **true**  
  The ship security plan is on board.
- `ShipmentStage/ISPSRequirements/CurrentOperatingSecurityLevelCode` = **1** (listID `IMO ISPS security level`)  
  Security level 1, the normal level. The code is from the world's copy of IMO ISPS Code security level: 1 = Security level 1.
- `ShipmentStage/ISPSRequirements/AdditionalMattersDescription` = **The ship's certificate is an interim one: it came under Bayvarra's flag on 15 January 2026, and the flag state's verification for the full certificate is set for June. The ship was searched for stowaways before it left Selanu, because the port facility had reported a gap in its perimeter fence on 6 May. Nothing was found.**  
  What the port should know: the interim status of the certificate, and a security matter.
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyIdentification/ID` = **5389612047** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (referenced).
- `ShipmentStage/ISPSRequirements/ISSCIssuerParty/PartyName/Name` = **Maritime Administration of Bayvarra**  
  Bayvarra's flag state administration: keeps the register of Bayvarran ships and issues their international ship security certificates under the ISPS Code. Referenced only, as the issuer of the certificate of Tidewell Ocean Lines' ship. Its identifier and name are enough (referenced).
- `ShipmentStage/MaritimeHealthDeclaration/ID` = **MDH-26-0303**  
  The maritime declaration of health.
- `ShipmentStage/MaritimeHealthDeclaration/InfectiousDiseaseCaseOnBoardIndicator` = **false**  
  No infectious disease.
- `ShipmentStage/MaritimeHealthDeclaration/SickAnimalOnBoardIndicator` = **true**  
  A sick animal is on board: the ship's cat.
- `ShipmentStage/MaritimeHealthDeclaration/SanitaryMeasuresAppliedIndicator` = **false**  
  No sanitary measures on this voyage.
- `ShipmentStage/MaritimeHealthDeclaration/ValidSanitationCertificateOnBoardIndicator` = **true**  
  The exemption certificate is valid until July.
- `ShipmentStage/MaritimeHealthDeclaration/TotalIllPersonQuantity` = **0** (unitCode `IE`)  
  No one ill.
- `ShipmentStage/MaritimeHealthDeclaration/SickAnimalDescription` = **The ship's cat has been off its food and listless for three days. It is kept in the master's cabin, away from the cargo and the galley; the master asks for a veterinarian at Lumeport.**  
  What the port health authority needs to know about the animal.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/ID` = **SSCEC-XB-2026-0114**  
  The ship sanitation control exemption certificate: the ship carries it instead of a control certificate. Unique only with its issuer.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssueDate` = **2026-01-14**  
  Issued after the inspection at Lumeport, before the ship's first voyage for the line; valid six months.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/DocumentDescription` = **Ship Sanitation Control Exemption Certificate (International Health Regulations 2005, Annex 3): the inspection found no evidence of infection or contamination, so no control measures were needed.**  
  What the document is.
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssuerParty/PartyIdentification/ID` = **7140583926** (schemeID `urn:ubl-examples:world:XB:public-body-register`)  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).
- `ShipmentStage/MaritimeHealthDeclaration/ShipSanitationControlExemptionDocumentReference/IssuerParty/PartyName/Name` = **Port Health Office of Bayvarra, Lumeport**  
  Bayvarra's port health authority at Lumeport, an office of the federal health administration, as the Maritime Administration is federal: under the International Health Regulations (2005) it inspects ships in the port and issues their ship sanitation control and exemption certificates (Annex 3) and the medicine chest certificates of Bayvarran ships. Referenced only, as the issuer of the certificates of Tidewell Ocean Lines' ships. Its identifier and name are enough (referenced).

### Transport Means

Inside `TransportMeans`:

- `JourneyID` = **TR-26-19W**  
  The voyage from Selanu back to Lumeport.
- `RegistrationNationalityID` = **XB** (schemeID `ISO 3166`)  
  The country the means of transport is registered in. The code is from the world's copy of UBL's Country identification (ISO 3166) list: XB = Bayvarra. An identifier that holds a code names the code's list in its schemeID.
- `RegistrationNationality` = **Bayvarra**  
  The same, in words.
- `DirectionCode` = **WB** (listID `urn:ubl-examples:world:codelist:TravelDirectionCode`)  
  The direction of the journey, as carriers name their services. The code is from the Trade Accord's travel direction list: WB = Westbound.
- `TransportMeansTypeCode` = **1511** (listID `UNECE Recommendation 28`)  
  The kind of means of transport: tidewell Reef; the fleet of Tidewell Ocean Lines. The line's second feeder, bought second-hand in December 2025 and moved to Bayvarra's flag on 15 January 2026. Until the flag state verifies its security system, it sails with an interim International Ship Security Certificate (ISPS Code A/19.4). The code is from the world's copy of UN/ECE Recommendation 28 Codes for types of means of transport: 1511 = Full container ship/cellular vessel.
- `MaritimeTransport/VesselID` = **XB-S-20231** (schemeID `urn:ubl-examples:world:vessel`)  
  The vessel's number in its country's register of ships.
- `MaritimeTransport/VesselName` = **Tidewell Reef**  
  The vessel's name; the fleet of Tidewell Ocean Lines.
- `MaritimeTransport/RadioCallSignID` = **QBTR4**  
  The radio call sign, in Bayvarra's call sign series QB: no ITU series starts with Q, so the sign belongs to no real station.
- `MaritimeTransport/MMSIRegistrationID` = **298702231**  
  The Maritime Mobile Service Identity, nine digits: the maritime identification digits 298 of Bayvarra, which the ITU has not allocated to any real country, and the ship's six digits.
- `MaritimeTransport/ShipsRequirements` = **Shore power at the container quay.**  
  What the ship needs in port.
- `MaritimeTransport/GrossTonnageMeasure` = **7480** (unitCode `C62`)  
  The gross tonnage of the vessel, a number without a unit.
- `MaritimeTransport/NetTonnageMeasure` = **3910** (unitCode `C62`)  
  Its net tonnage, also without a unit.
- `MaritimeTransport/SegregatedBallastMeasure` = **1900** (unitCode `TNE`)  
  The capacity of the tanks for ballast water only.
- `MaritimeTransport/ShipConfigurationCode` = **FEEDER** (listID `urn:ubl-examples:world:codelist:ShipConfigurationCode`)  
  The kind of vessel, for about 700 TEU. The code is from the Trade Accord's ship configuration list: FEEDER = Feeder container ship.
- `MaritimeTransport/RegistryCertificateDocumentReference/ID` = **REG-XB-S-20231**  
  The ship's certificate of registry.
- `MaritimeTransport/RegistryPortLocation/ID` = **XBLMP** (schemeID `UN/LOCODE`)  
  The place's identifier, as the world gives it wherever the place appears (a code in the form of a UN/LOCODE).
- `MaritimeTransport/RegistryPortLocation/Name` = **Lumeport**  
  The port the vessel is registered in.

## The document

```xml
<?xml version='1.0' encoding='UTF-8'?>
<CommonTransportationReport xmlns="urn:oasis:names:specification:ubl:schema:xsd:CommonTransportationReport-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">
  <cbc:UBLVersionID>2.5</cbc:UBLVersionID>
  <cbc:CustomizationID>urn:ubl-examples:world:trns:common-transportation-report:1.0#compliant#urn:ubl-examples:world:community:port-lumeport:1.0</cbc:CustomizationID>
  <cbc:ProfileID>urn:ubl-examples:world:profile:transport:1.0</cbc:ProfileID>
  <cbc:ProfileExecutionID>9900667463</cbc:ProfileExecutionID>
  <cbc:ID>8600033374</cbc:ID>
  <cbc:UUID>149f7421-1d43-5c08-9504-00a7ea0b615b</cbc:UUID>
  <cbc:IssueDate>2026-05-08</cbc:IssueDate>
  <cbc:IssueTime>11:22:00-01:00</cbc:IssueTime>
  <cbc:ReportTypeCode listID="urn:ubl-examples:world:codelist:TransportReportTypeCode">PREARRIVAL</cbc:ReportTypeCode>
  <cbc:ReportType>Pre-arrival report</cbc:ReportType>
  <cac:ReporterParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
    <cac:Language>
      <cbc:ID schemeID="ISO 639">en</cbc:ID>
      <cbc:Name>English</cbc:Name>
      <cbc:LocaleCode listID="urn:ubl-examples:world:codelist:LocaleCode">en-XB</cbc:LocaleCode>
    </cac:Language>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-547539</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>18</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38527</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:Contact>
      <cbc:Name>Bookings</cbc:Name>
      <cbc:JobTitle>Booking agent</cbc:JobTitle>
      <cbc:Department>Bookings</cbc:Department>
      <cbc:Telephone>+999 2 38 2058 7929</cbc:Telephone>
      <cbc:ElectronicMail>bookings@tidewell.example</cbc:ElectronicMail>
      <cbc:Note>Every day 06:00–22:00</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411918</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:ReporterParty>
  <cac:AuthorityParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Lumeport</cbc:Name>
    </cac:PartyName>
    <cac:PostalAddress>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:lumeport:address-register">LUM-ADR-030762</cbc:ID>
      <cbc:AddressTypeCode listID="urn:ubl-examples:world:codelist:AddressTypeCode">BUSINESS</cbc:AddressTypeCode>
      <cbc:AddressFormatCode listID="urn:ubl-examples:world:codelist:AddressFormatCode">XB</cbc:AddressFormatCode>
      <cbc:StreetName>Harbour Road</cbc:StreetName>
      <cbc:BuildingNumber>11</cbc:BuildingNumber>
      <cbc:CitySubdivisionName>Dockside</cbc:CitySubdivisionName>
      <cbc:CityName>Lumeport</cbc:CityName>
      <cbc:PostalZone>38526</cbc:PostalZone>
      <cbc:CountrySubentity>Coastal State</cbc:CountrySubentity>
      <cbc:CountrySubentityCode listID="urn:ubl-examples:world:XB:codelist:CountrySubentityCode">XB-CO</cbc:CountrySubentityCode>
      <cbc:TimezoneOffset>-01:00</cbc:TimezoneOffset>
      <cac:Country>
        <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
        <cbc:Name>Bayvarra</cbc:Name>
      </cac:Country>
    </cac:PostalAddress>
    <cac:PhysicalLocation>
      <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
      <cbc:Description>Port of Lumeport</cbc:Description>
      <cbc:InformationURI>https://www.port-lumeport.example</cbc:InformationURI>
      <cac:SubsidiaryLocation>
        <cbc:Name>Container quay</cbc:Name>
      </cac:SubsidiaryLocation>
      <cac:LocationCoordinate>
        <cbc:CoordinateSystemCode listID="EPSG">4326</cbc:CoordinateSystemCode>
        <cbc:LatitudeDegreesMeasure unitCode="DD">31</cbc:LatitudeDegreesMeasure>
        <cbc:LatitudeMinutesMeasure unitCode="D61">6.22</cbc:LatitudeMinutesMeasure>
        <cbc:LatitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LatitudeDirectionCode">South</cbc:LatitudeDirectionCode>
        <cbc:LongitudeDegreesMeasure unitCode="DD">13</cbc:LongitudeDegreesMeasure>
        <cbc:LongitudeMinutesMeasure unitCode="D61">23.07</cbc:LongitudeMinutesMeasure>
        <cbc:LongitudeDirectionCode listID="urn:oasis:names:specification:ubl:codelist:gc:LongitudeDirectionCode">West</cbc:LongitudeDirectionCode>
      </cac:LocationCoordinate>
    </cac:PhysicalLocation>
    <cac:Contact>
      <cbc:Name>Port control</cbc:Name>
      <cbc:JobTitle>Duty port controller</cbc:JobTitle>
      <cbc:Department>Port operations</cbc:Department>
      <cbc:Telephone>+999 2 38 8964 6053</cbc:Telephone>
      <cbc:ElectronicMail>port@port-lumeport.example</cbc:ElectronicMail>
      <cbc:Note>Every day, around the clock</cbc:Note>
    </cac:Contact>
    <cac:ElectronicAddress>
      <cbc:ExchangeNetworkID>urn:ubl-examples:world:network</cbc:ExchangeNetworkID>
      <cbc:ElectronicAddressID schemeID="urn:ubl-examples:world:endpoint">XB:20411781</cbc:ElectronicAddressID>
    </cac:ElectronicAddress>
  </cac:AuthorityParty>
  <cac:SenderParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411918</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Tidewell Ocean Lines</cbc:Name>
    </cac:PartyName>
  </cac:SenderParty>
  <cac:ReceiverParty>
    <cac:PartyIdentification>
      <cbc:ID schemeID="urn:ubl-examples:world:XB:register">20411781</cbc:ID>
    </cac:PartyIdentification>
    <cac:PartyName>
      <cbc:Name>Port of Lumeport</cbc:Name>
    </cac:PartyName>
  </cac:ReceiverParty>
  <cac:Shipment>
    <cbc:ID>7400667463</cbc:ID>
    <cac:ShipmentStage>
      <cbc:ID>1</cbc:ID>
      <cbc:TransportModeCode listID="UNECE Recommendation 19 - Codes for Modes of Transport">1</cbc:TransportModeCode>
      <cac:LoadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
        <cbc:Name>Port of Selanu</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:LoadingPortLocation>
      <cac:UnloadingPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Port of Lumeport</cbc:Name>
        <cac:Address>
          <cac:Country>
            <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
          </cac:Country>
        </cac:Address>
      </cac:UnloadingPortLocation>
      <cac:ActualDepartureTransportEvent>
        <cbc:OccurrenceDate>2026-05-07</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>14:00:00+00:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XLSEL</cbc:ID>
          <cbc:Name>Port of Selanu</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XL</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:ActualDepartureTransportEvent>
      <cac:EstimatedArrivalTransportEvent>
        <cbc:OccurrenceDate>2026-05-09</cbc:OccurrenceDate>
        <cbc:OccurrenceTime>12:50:00-01:00</cbc:OccurrenceTime>
        <cac:Location>
          <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
          <cbc:Name>Port of Lumeport</cbc:Name>
          <cac:Address>
            <cac:Country>
              <cbc:IdentificationCode listID="ISO 3166">XB</cbc:IdentificationCode>
            </cac:Country>
          </cac:Address>
        </cac:Location>
      </cac:EstimatedArrivalTransportEvent>
      <cac:ReportingPerson>
        <cbc:FirstName>Hester</cbc:FirstName>
        <cbc:FamilyName>Calloway</cbc:FamilyName>
        <cbc:RoleCode listID="urn:ubl-examples:world:codelist:ShipPersonRoleCode">MASTER</cbc:RoleCode>
      </cac:ReportingPerson>
      <cac:ISPSRequirements>
        <cbc:ID>IISSC-XB-2026-0115</cbc:ID>
        <cbc:ValidISSCIndicator>true</cbc:ValidISSCIndicator>
        <cbc:ISSCExpiryDate>2026-07-14</cbc:ISSCExpiryDate>
        <cbc:SSPOnBoardIndicator>true</cbc:SSPOnBoardIndicator>
        <cbc:CurrentOperatingSecurityLevelCode listID="IMO ISPS security level">1</cbc:CurrentOperatingSecurityLevelCode>
        <cbc:AdditionalMattersDescription>The ship's certificate is an interim one: it came under Bayvarra's flag on 15 January 2026, and the flag state's verification for the full certificate is set for June. The ship was searched for stowaways before it left Selanu, because the port facility had reported a gap in its perimeter fence on 6 May. Nothing was found.</cbc:AdditionalMattersDescription>
        <cac:ISSCIssuerParty>
          <cac:PartyIdentification>
            <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">5389612047</cbc:ID>
          </cac:PartyIdentification>
          <cac:PartyName>
            <cbc:Name>Maritime Administration of Bayvarra</cbc:Name>
          </cac:PartyName>
        </cac:ISSCIssuerParty>
      </cac:ISPSRequirements>
      <cac:MaritimeHealthDeclaration>
        <cbc:ID>MDH-26-0303</cbc:ID>
        <cbc:InfectiousDiseaseCaseOnBoardIndicator>false</cbc:InfectiousDiseaseCaseOnBoardIndicator>
        <cbc:SickAnimalOnBoardIndicator>true</cbc:SickAnimalOnBoardIndicator>
        <cbc:SanitaryMeasuresAppliedIndicator>false</cbc:SanitaryMeasuresAppliedIndicator>
        <cbc:ValidSanitationCertificateOnBoardIndicator>true</cbc:ValidSanitationCertificateOnBoardIndicator>
        <cbc:TotalIllPersonQuantity unitCode="IE">0</cbc:TotalIllPersonQuantity>
        <cbc:SickAnimalDescription>The ship's cat has been off its food and listless for three days. It is kept in the master's cabin, away from the cargo and the galley; the master asks for a veterinarian at Lumeport.</cbc:SickAnimalDescription>
        <cac:ShipSanitationControlExemptionDocumentReference>
          <cbc:ID>SSCEC-XB-2026-0114</cbc:ID>
          <cbc:IssueDate>2026-01-14</cbc:IssueDate>
          <cbc:DocumentDescription>Ship Sanitation Control Exemption Certificate (International Health Regulations 2005, Annex 3): the inspection found no evidence of infection or contamination, so no control measures were needed.</cbc:DocumentDescription>
          <cac:IssuerParty>
            <cac:PartyIdentification>
              <cbc:ID schemeID="urn:ubl-examples:world:XB:public-body-register">7140583926</cbc:ID>
            </cac:PartyIdentification>
            <cac:PartyName>
              <cbc:Name>Port Health Office of Bayvarra, Lumeport</cbc:Name>
            </cac:PartyName>
          </cac:IssuerParty>
        </cac:ShipSanitationControlExemptionDocumentReference>
      </cac:MaritimeHealthDeclaration>
    </cac:ShipmentStage>
  </cac:Shipment>
  <cac:TransportMeans>
    <cbc:JourneyID>TR-26-19W</cbc:JourneyID>
    <cbc:RegistrationNationalityID schemeID="ISO 3166">XB</cbc:RegistrationNationalityID>
    <cbc:RegistrationNationality>Bayvarra</cbc:RegistrationNationality>
    <cbc:DirectionCode listID="urn:ubl-examples:world:codelist:TravelDirectionCode">WB</cbc:DirectionCode>
    <cbc:TransportMeansTypeCode listID="UNECE Recommendation 28">1511</cbc:TransportMeansTypeCode>
    <cac:MaritimeTransport>
      <cbc:VesselID schemeID="urn:ubl-examples:world:vessel">XB-S-20231</cbc:VesselID>
      <cbc:VesselName>Tidewell Reef</cbc:VesselName>
      <cbc:RadioCallSignID>QBTR4</cbc:RadioCallSignID>
      <cbc:MMSIRegistrationID>298702231</cbc:MMSIRegistrationID>
      <cbc:ShipsRequirements>Shore power at the container quay.</cbc:ShipsRequirements>
      <cbc:GrossTonnageMeasure unitCode="C62">7480</cbc:GrossTonnageMeasure>
      <cbc:NetTonnageMeasure unitCode="C62">3910</cbc:NetTonnageMeasure>
      <cbc:SegregatedBallastMeasure unitCode="TNE">1900</cbc:SegregatedBallastMeasure>
      <cbc:ShipConfigurationCode listID="urn:ubl-examples:world:codelist:ShipConfigurationCode">FEEDER</cbc:ShipConfigurationCode>
      <cac:RegistryCertificateDocumentReference>
        <cbc:ID>REG-XB-S-20231</cbc:ID>
      </cac:RegistryCertificateDocumentReference>
      <cac:RegistryPortLocation>
        <cbc:ID schemeID="UN/LOCODE">XBLMP</cbc:ID>
        <cbc:Name>Lumeport</cbc:Name>
      </cac:RegistryPortLocation>
    </cac:MaritimeTransport>
  </cac:TransportMeans>
</CommonTransportationReport>
```
