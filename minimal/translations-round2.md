# Translations for review, round 2: minimal UBL 2.5 examples

These terms were added to the minimal UBL example documents after the first translation round. Each document has one locale, and its texts are written in that locale's language. Please translate each English term into German, Brazilian Portuguese and Japanese, using the context given.

## Conventions

- **Languages:** German (`de`), Brazilian Portuguese (`pt-BR`), Japanese in Latin script (`ja-Latn-hepburn`). English is the source and is used as-is for the US, India and South Africa.
- **Latin script only.** Japanese must be romanized in **modified Hepburn**, with macrons for long vowels (ō, ū), e.g. *Tōkyō*. No kana or kanji.
- **Party names** are built from *[word for "Example"] + [role] + [number]*, e.g. `Example Carrier 32` in English:
  - German compounds one-word roles (`Beispiel` + role as one word); multi-word roles stay separate.
  - Portuguese puts the role first (`[role] Exemplo 32`).
  - They must be visibly fictitious, so no legal forms (GmbH, Ltda., K.K.).

  Please give the **role word** only.
- **Role words** should be the term a business, logistics, customs or procurement professional in that country would use for that role, not a literal translation. The UBL definition is given as context.
- **Texts** are short business texts. Keep them as short as the English.

## 1. Party roles

| # | English | Context (UBL definition) | Documents | German | Portuguese (Brazil) | Japanese (Hepburn) |
|---|---|---|---|---|---|---|
| R1 | Carrier | The Party who provides the transport of goods between named points. | BillOfLading, Waybill | | | |
| R2 | Consignor | The Party who is responsible for sending the goods (the shipper who gives instructions for the transport). | BillOfLading, ForwardingInstructions, Waybill | | | |
| R3 | Freight Forwarder | A freight forwarder or carrier: the party instructed to arrange the forwarding of the goods. | ForwardingInstructions | | | |
| R4 | Authority | The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator. | CommonTransportationReport | | | |
| R5 | Importer | The Party who makes the import declaration, or on whose behalf the import declaration is made. | ImportCustomsDeclaration | | | |
| R6 | Exporter (transit) | The Party who makes the Transit Customs Declaration, or on whose behalf it is made; the owner of the goods or the party with similar right of disposal over them. | TransitCustomsDeclaration | | | |
| R7 | Winning Tenderer | A party that is identified as the awarded by a tender result (the winner of a public procurement procedure). | ContractAwardNotice | | | |
| R8 | Branch | The party that will receive and use the Stock Availability Report (normally the branch for which the stock is reported). | StockAvailabilityReport | | | |

## 2. Texts and names

| # | English | Context | German | Portuguese (Brazil) | Japanese (Hepburn) |
|---|---|---|---|---|---|
| T1 | Road freight | Description of the item invoiced on a freight invoice: a road transport service. | | | |
| T2 | Pre-arrival notification | The type of a report sent to a transport authority (e.g. a port or border authority) before a vessel or vehicle arrives. | | | |
| T3 | Maintenance of office equipment | Description of the work reported in a work report line. | | | |
| T4 | Back-to-school promotion | Description of a planned retail event (a sales promotion in late August). | | | |
| T5 | Used lead-acid batteries | Description of the waste in a cross-border waste shipment (hazardous waste, Basel Convention). | | | |
| T6 | Is the item available from stock? | A question in an enquiry to a supplier. | | | |
| T7 | Yes, the item is available from stock. | The answer to T6 in the enquiry response. | | | |
| T8 | Certificate of conformity | The kind of goods certificate for import and export: the goods meet the required standards. | | | |
| T9 | Example Terminal 1 | A fictitious name of a transport terminal: the location reached in a transport progress report. Built as *[word for "Example"] + [terminal] + 1*. | | | |
| T10 | Sam Example | A fictitious personal name: the person who signs the issuer's endorsement on a Certificate of Origin (a second signatory, next to "Alex Example"). | | | |
