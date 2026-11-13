# Translations for review: minimal UBL 2.5 examples

These words and sentences appear in the minimal UBL example documents (`minimal/layer0`, `minimal/layer1`). Each document has one locale, and its texts are written in that locale's language. The current German, Brazilian Portuguese and Japanese versions were written without a native speaker. Please check each one and enter a correction where needed.

## Conventions

- **Languages:** German (`de`), Brazilian Portuguese (`pt`), Japanese (`ja-Latn`). English is the source and is used as-is for the US, India and South Africa.
- **Latin script only.** Japanese must be romanized in **Hepburn**, with macrons for long vowels (ō, ū), e.g. *Kōnyūsha*. No kana or kanji.
- **Party names** are built as *[word for "Example"] + [role] + [number]*, e.g. `Beispiel Käufer 492`. They must be visibly fictitious, so no legal forms (GmbH, Ltda., K.K.).
- **Role words** should be the term a business or public-procurement professional in that country would use for that role, not a literal translation. The UBL definition is given as context.
- **Texts** are short business texts. Keep them as short as the English.

## 1. The word "Example" (prefix of all party names)

| English | German (current) | German (correction) | Portuguese (current) | Portuguese (correction) | Japanese, Hepburn (current) | Japanese (correction) |
|---|---|---|---|---|---|---|
| Example | Beispiel | | Exemplo | | Mihon | |

## 2. Party roles

Each role names a party in a business document. "Context" is the UBL 2.5 definition of the role, and "Documents" lists where it occurs.

| # | English | Context (UBL definition) | Documents | German (current) | German (correction) | Portuguese (current) | Portuguese (correction) | Japanese, Hepburn (current) | Japanese (correction) |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Supplier | The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line. / The Accounting Supplier Party related to the statement information reported on this Statement Line. | CreditNote, DebitNote, FreightInvoice, Invoice, PurchaseReceipt, Reminder, RemittanceAdvice, SelfBilledCreditNote, SelfBilledInvoice, Statement | Lieferant | | Fornecedor | | Kyōkyūsha | |
| R2 | Customer | The Accounting Customer Party related to the remittance information reported on this Remittance Advice Line. / The Accounting Customer Party related to the statement information reported on this Statement Line. | FreightInvoice, Reminder, RemittanceAdvice, SelfBilledCreditNote, SelfBilledInvoice, Statement | Kunde | | Cliente | | Kokyaku | |
| R3 | Seller | The Seller requesting the Item Information. / The party providing the work. | InstructionForReturns, Order, OrderCancellation, OrderChange, OrderResponse, OrderResponseSimple, Quotation, RequestForQuotation, StockAvailabilityReport, WorkReport | Verkäufer | | Vendedor | | Hanbaisha | |
| R4 | Buyer | Association to the Buyer. / The Buyer from whom the Item Information is requested. | Order, OrderCancellation, OrderChange, OrderResponse, OrderResponseSimple, WorkReport | Käufer | | Comprador | | Kōnyūsha | |
| R5 | Shipper | The Party that executed the delivery. / The despatch party. | DeliveryNote, DespatchAdvice, ReceiptAdvice | Versender | | Expedidor | | Shukkasha | |
| R6 | Consignee | The Party to whom the goods or services were delivered. / The customer party. | DeliveryNote, DespatchAdvice, ReceiptAdvice | Warenempfänger | | Destinatário | | Uketorinin | |
| R7 | Retailer | The retailer, who sends this message. / The retailer. | InstructionForReturns, InventoryReport | Einzelhändler | | Varejista | | Kourigyōsha | |
| R8 | Inventory Reporter | The Party that is reporting the inventory details. / The party that will receive and use the Stock Availability Report (normally the branch for which the stock is reported). | InventoryReport, StockAvailabilityReport | Bestandsmelder | | Informante de Estoque | | Zaiko Hōkokusha | |
| R9 | Provider | The Party who provides this Catalogue. / The Party who provides this piece of Transport Equipment. | Catalogue, CatalogueDeletion, CatalogueItemSpecificationUpdate, CataloguePricingUpdate, CatalogueRequest | Anbieter | | Provedor | | Teikyōsha | |
| R10 | Sender | The Party sending this Item Information Request. / The Party sending this document. | ApplicationResponse, AttachedDocument, AwardedNotification, CommonTransportationReport, ExceptionCriteria, ExceptionNotification, Forecast, ForecastRevision, InvoiceStatusRequest, ItemInformationRequest, ProductActivity, RetailEvent, TenderReceipt, TendererQualificationResponse, TradeItemLocationProfile, UnawardedNotification, UtilityStatement, WasteMovement, WasteNotification, WeightStatement | Absender | | Remetente | | Sōshinsha | |
| R11 | Receiver | The Party receiving this Document. / The Party receiving this Item Information Request. | ApplicationResponse, AttachedDocument, AwardedNotification, Catalogue, CatalogueDeletion, CatalogueItemSpecificationUpdate, CataloguePricingUpdate, CatalogueRequest, CommonTransportationReport, ExceptionCriteria, ExceptionNotification, Forecast, ForecastRevision, InvoiceStatusRequest, ItemInformationRequest, ProductActivity, RetailEvent, TenderReceipt, TendererQualificationResponse, TradeItemLocationProfile, UnawardedNotification, UtilityStatement, WasteMovement, WasteNotification, WeightStatement | Empfänger | | Receptor | | Jushinsha | |
| R12 | Requester | The Party who issued the Enquiry. / The Party who issues this Enquiry. | Enquiry, EnquiryResponse | Anfragender | | Solicitante | | Iraisha | |
| R13 | Responder | The Party who responds to the Enquiry. / The Party who responds to this Enquiry. | Enquiry, EnquiryResponse | Antwortender | | Respondente | | Kaitōsha | |
| R14 | Participant | The business parties agreeing on a set of digital processes, terms and conditions to ensure interoperability. | DigitalAgreement | Teilnehmer | | Participante | | Sankasha | |
| R15 | Carrier | The Party who offers the transport service based upon a request from a transport user. / The Party who provides the transport services referenced in the Transport Execution Plan Request. | GoodsItemItinerary, TransportExecutionPlan, TransportExecutionPlanRequest | Frachtführer | | Transportador | | Unsō Gyōsha | |
| R16 | Logistics Operator | The Party who issues this Manifest.This Party is normally the Logistics Operator. | Manifest | Logistikdienstleister | | Operador Logístico | | Butsuryū Gyōsha | |
| R17 | Reporter | The Party who provides this Common Transportation Report. | CommonTransportationReport | Berichterstatter | | Relator | | Hōkokusha | |
| R18 | Contracting Authority | The Contracting Party eceiving the tender status inquiry. / The Contracting Party issuing the information about the tender status. | CallForTenders, ContractAwardNotice, ContractNotice, ExpressionOfInterestRequest, ExpressionOfInterestResponse, PriorInformationNotice, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationRequest, QualificationApplicationResponse, TenderContract, TenderStatus, TenderStatusRequest, TenderWithdrawal, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse | Öffentlicher Auftraggeber | | Órgão Contratante | | Hatchū Kikan | |
| R19 | Economic Operator | The Economic Operator issuing the Qualification Application Response. / The Economic Operator issuing the expression of interest. | ExpressionOfInterestRequest, ExpressionOfInterestResponse, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationResponse, TenderContract, TenderStatus, TenderStatusRequest, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse | Wirtschaftsteilnehmer | | Operador Econômico | | Jigyōsha | |
| R20 | Tenderer | The Party who submits this Tender. / The economic operator or the main Tenderer in case of a consortium who withdraws the Tender. | Tender, TenderWithdrawal | Bieter | | Licitante | | Nyūsatsusha | |
| R21 | Main Tenderer | The qualifications of the main tenderer party. | TendererQualification | Hauptbieter | | Licitante Principal | | Shu Nyūsatsusha | |
| R22 | Depositor | The Party who deposits the bid bond guarantee. | GuaranteeCertificate | Hinterleger | | Depositante | | Kitakusha | |
| R23 | Guarantor | The guarantee creditor organisation who has the authority to charge bid bond guarantee credit. | GuaranteeCertificate | Bürge | | Garantidor | | Hoshōnin | |
| R24 | Business | The Party who owns these Digital Capabilities. / The Party who owns this Business Card. | BusinessCard, BusinessInformation, DigitalCapability | Unternehmen | | Empresa | | Kigyō | |
| R25 | Exporter | The Party who exports the goods or has similar right of disposal over them at the time of export. / The Party who makes the export declaration, or on whose behalf the export declaration is made, and who is the owner of the goods or has similar right of disposal over them at the time when the declaration is accepted. | ExportCustomsDeclaration | Ausführer | | Exportador | | Yushutsusha | |
| R26 | Holder | The Party who holds the Goods Item Passport. This Party is normally the temporary exporter of the Goods. | GoodsItemPassport | Inhaber | | Titular | | Shojisha | |
| R27 | Notifier | The Party responsible for providing the Waste Notification information and acting in the role of notifier in the waste movement process. / The Party that acts as the notifier in relation to the Waste Movements covered by this document. | WasteMovement, WasteNotification | Notifizierender | | Notificante | | Tsūchisha | |
| R28 | Waste Producer | The Party producing the waste material. | WasteMovement, WasteNotification | Abfallerzeuger | | Gerador de Resíduos | | Haikibutsu Haishutsusha | |
| R29 | Customs | The Authority who is legally responsible for processing the Declaration. / The Authority who processes this Customs Declaration. | TransitCustomsDeclaration, WasteNotification | Zollbehörde | | Alfândega | | Zeikan | |
| R30 | Importing Guarantor | The Party who on behalf of their Customs Authority issues the Proof of Reexportation. This Party is normally a chamber of commerce. / The Party who on behalf of their Customs Authority issues this Document. This Party is normally a chamber of commerce. | ProofOfReexportationReminder, ProofOfReexportationRequest | Einfuhrbürge | | Garantidor de Importação | | Yunyū Hoshōnin | |
| R31 | Exporting Guarantor | The Party who is fiscally responsible for the Goods Item Passport counterfoils which the Customs Party is requesting. This Party is normally a chamber of commerce. / The Party who provides a guarantee for the Goods while being temporarily exported. This Party is normally a chamber of commerce. | ProofOfReexportationReminder, ProofOfReexportationRequest | Ausfuhrbürge | | Garantidor de Exportação | | Yushutsu Hoshōnin | |
| R32 | Issuer | The Party who issues the Immobilized Security Certificate. / The Party who issues the Referenced Document. | CertificateOfOrigin, GoodsCertificate | Aussteller | | Emissor | | Hakkōsha | |
| R33 | Endorser | A party providing an endorsement to the CoO. / The Party providing the endorsement. | CertificateOfOrigin | Beglaubiger | | Endossante | | Shōmeisha | |
| R34 | Preparer | The Party who prepares this Certificate of Origin Application. This Party is normally an individual, a group or a body. | CertificateOfOrigin | Ersteller | | Preparador | | Sakuseisha | |

## 3. Texts and names

| # | English | Context | German (current) | German (correction) | Portuguese (current) | Portuguese (correction) | Japanese, Hepburn (current) | Japanese (correction) |
|---|---|---|---|---|---|---|---|---|
| T1 | Ballpoint pen, blue | Description of the traded item (an item line in orders, invoices, despatch advices etc.). | Kugelschreiber, blau | | Caneta esferográfica azul | | Bōrupen, ao | |
| T2 | Ordered in error | The (general) reason for cancelling an order or a fulfilment. | Irrtümlich bestellt | | Pedido feito por engano | | Ayamatte chūmon | |
| T3 | Ordinary | The type of Certificate of Origin applied for (examples in UBL: Ordinary, Re-export, Commonwealth Preferential). | Gewöhnlich | | Comum | | Ippan | |
| T4 | Approved | The status of an endorsement on a Certificate of Origin. | Genehmigt | | Aprovado | | Shōnin-zumi | |
| T5 | Is the economic operator enrolled in a trade register? | A question in a public-procurement qualification (ESPD), answered yes/no by the economic operator. | Ist der Wirtschaftsteilnehmer in einem Handelsregister eingetragen? | | O operador econômico está inscrito em um registro comercial? | | Jigyōsha wa shōgyō tōki sarete imasu ka? | |
| T6 | Ordering | A kind of digital trade process that parties agree on or support. | Bestellung | | Pedido | | Hatchū | |
| T7 | Alex Example | A fictitious personal name: the person who signs a Certificate of Origin application. | Alex Beispiel | | Alex Exemplo | | Mihon Tarō | |
| T8 | Example Store 1 | A fictitious store name: the location where sales were observed. | Beispiel Filiale 1 | | Exemplo Loja 1 | | Mihon Tenpo 1 | |
| T9 | Office supplies 2026 | The title of a public procurement project. | Büromaterial 2026 | | Material de escritório 2026 | | Jimu Yōhin 2026 | |
