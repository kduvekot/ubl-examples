# LLM review: 13-Waybill.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/13-Waybill.xml`, Git blob `0e28ae8a70150ecfdb1e12ab9527a6f9336f5e5e` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6bf7444 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/13#F1 · High · The note's three originals contradict the distribution list
- XPath: `/Waybill/cbc:Note` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- Why: The note says the consignment note has three originals, for consignor, consignee and carrier (as the CMR requires, art. 5, own knowledge). The distribution list, "A list of interested parties to whom this document is distributed", gives the consignee the original that travels with the goods, but gives the consignor, Lumeway, only an electronic copy, and has no entry for the carrier's original.
- Condition: The distribution list and the note agree on who receives which original or copy.
- Options: Give Lumeway the consignor's original in the distribution list (preferred), and add the carrier's original if the list is meant to be complete; or change the note.
- Needs decision: no

### retail/13#F2 · Medium · Language/LocaleCode holds the language code, not a locale
- XPath: `/Waybill/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/LocaleCode` as "A code signifying the locale in which this language is used". Every party language here has `LocaleCode` = `en` with `listID="ISO 639"`: the ISO 639 code of the language itself, which repeats `Language/cbc:ID` and names no locale (no country or region in which English is used). ISO 639 is a list of languages, not of locales. The world does have locales: Urvanian addresses carry renderings tagged `languageID="en-XB"` (English as used in Bayvarra). The checklist of the review names "a language code in LocaleCode" as a Medium case. The same value occurs 364 times in 213 XML files (`grep -rho --include='*.xml' 'LocaleCode listID="ISO 639">en<' world/examples | wc -l`, and `-rl … | wc -l` for the files).
- Condition: No `Language/cbc:LocaleCode` of a party holds a bare language code; where a `LocaleCode` is present it identifies a locale and its `listID` names a list of locales.
- Options: Drop `LocaleCode` from the parties' languages (preferred: nothing in this document depends on a locale, so it has no business reason, and `Language/cbc:ID` already says English); or give a real locale (e.g. English as used in Bayvarra) with a `listID` for a locale list such as BCP 47. The fix belongs in the party master data, so it applies to every example at once.
- Needs decision: no

### retail/13#F3 · Medium · A site gate in AdditionalStreetName of Lumeway's address
- XPath: `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `AdditionalStreetName` as "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". "Gate 3" is not a street name but an entrance of the distribution centre at Distribution Drive 43; it only matters to vehicles that load or unload there, and the postal address of the party holds nothing for vehicles (checklist of the review: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles"). The same value occurs 79 times in 76 XML files (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: No `AdditionalStreetName` holds "Gate 3"; Lumeway's postal address holds only postal parts, and where a transport document needs the gate it is given in the pickup or delivery location, not in a street element.
- Options: Remove the gate from Lumeway's postal address (preferred), and where a transport document needs it, say it in that location's `Description` (or as a location identifier of the gate, e.g. a GLN of the dock). Fix it in the party master data.
- Needs decision: no

### retail/13#F4 · Low · Issue location named after a company
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeway Distribution`
- Why: The place of issue is given as "Lumeway Distribution", the consignor's company name, without an address or identifier; a consignment note states the place where it is made out (CMR art. 6(1)(a), own knowledge). The place is Lumeway's distribution centre in Marrowdale, which the flow identifies by GLN `9520610900008` and address.
- Condition: The issue location names the place (e.g. the distribution centre in Marrowdale) and identifies it as the flow does elsewhere.
- Options: Name the place and add its GLN or address (preferred).
- Needs decision: no

### retail/13#F5 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: The registration date `1996-01-01` is shared by 25 different parties of the world (counted over `world/examples/*/*.xml` with lxml: distinct `PartyLegalEntity/RegistrationName` per `RegistrationDate`), among them Bayforth Forwarding, Harbourline Factoring, Codana Identification Agency, Brackenmere Furniture and Castrano Logistics, while every other party has a date of its own (e.g. Lumeway 1988-10-03, Brightmarket 1979-02-14). A common 1 January for unrelated companies in three countries is a filler, not a fact of the world (rule "no fillers").
- Condition: The registration date of each party here is a date with a reason in the world's history, or it is absent.
- Options: Give each party its real registration date from its history (preferred), or leave the date out where the history has none.
- Needs decision: yes

### retail/13#F6 · Low · Bayforth's "Export desk" contact for a domestic transport
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Export desk`
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:ElectronicMail` = `export@bayforth.example`
- Why: Bayforth's contact (`SenderParty`) is the "Export desk" (export@bayforth.example), an operations planner. The transport of this flow is domestic: from Lumeway's distribution centre in Marrowdale, Upland State, to Brightmarket in Lumeport, Coastal State, both in Bayvarra (`11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:CityName` = `Marrowdale`, `11-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CityName` = `Lumeport`); an export desk does not handle it. The same contact is used for Bayforth in 25 places (`grep -rh --include='*.xml' -A1 '<cbc:Name>Export desk</cbc:Name>' world/examples`).
- Condition: Bayforth's contact in this document is one that handles domestic road transport.
- Options: Give Bayforth a contact for domestic road transport (e.g. a road transport or dispatch desk) in this flow (preferred), keeping the export desk for its export flows.
- Needs decision: no

### retail/13#F7 · Low · Lumeway's customs trader number in a document without customs
- XPath: `/Waybill/cac:ReceiverParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: Lumeway (`ReceiverParty`) carries its customs trader identifier `XB-TR-410274`. Nothing in this flow is declared to customs: every movement in it is inside Bayvarra (Marrowdale to Lumeport), and no example of the flow is a customs document. The identifier looks copied from Lumeway's master data (section 4.8 of the review).
- Condition: Lumeway's party in this document carries no customs identifier, unless the document is used for customs.
- Options: Leave the customs trader identifier out of the documents of this domestic flow (preferred) and keep it for the import and export flows where customs use it.
- Needs decision: no

### retail/13#F8 · Low · CorporateStockAmount holds share capital, the definition says number of shares
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `12000000`
- Why: UBL defines `PartyLegalEntity/CorporateStockAmount` as "The number of shares in the capital stock of a corporation", yet its data type is an amount. The value here is a sum of money (`currencyID="XBL"`), i.e. the share capital, which is not what the definition says; for Lumeway, a private limited company, the definition's "corporation" fits only loosely. Besides, nothing in this document uses the share capital (it is not an invoice or another business letter on which company law could require it). This is a conflict between the UBL definition and its data type rather than a choice the example can resolve alone, so it is a candidate for the findings recorded for the OASIS UBL TC.
- Condition: Either the share capital is no longer carried in `CorporateStockAmount`, or the use is recorded as a finding against the UBL definition (semantic conformance, UBL 2.5 §4.7/§7.2) and kept on purpose.
- Options: Record it as a finding against the UBL definition and keep the value where a document needs the share capital (invoices); leave it out here, where the document does not use it (preferred). The decision is the same for every example.
- Needs decision: yes

### retail/13#F9 · Low · Lumeway's sales customer-service contact does not fit its role here
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway's primary contact (`ReceiverParty`) is "Customer service", a customer service officer in Sales, the contact a buyer uses. In this document Lumeway takes part in this transport document as the transport user and consignor; the order names its despatch contact, `08-Order.xml:/Order/cac:SellerSupplierParty/cac:DespatchContact/cbc:Name` = `Dispatch office`. The party is copied with its sales contact into every role it has in the flow.
- Condition: The contact of Lumeway in this document is the one that handles what this document is about.
- Options: Give Lumeway a role-specific contact in this document (preferred, the order shows the flow already knows them), or leave the contact out where the document does not need one.
- Needs decision: no

### retail/13#F10 · Low · Brightmarket's consumer-facing master data copied into a trade document
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cbc:LogoReferenceID` = `BM-LOGO-2024`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:AdditionalWebSite/cbc:URI` = `https://shop.brightmarket.example`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:SocialMediaProfile/cbc:URI` = `https://social.example/brightmarket`
- Why: Brightmarket (`ConsigneeParty`) carries its logo reference, its online shop and its photo social-media profile. This document is exchanged between trading partners (Waybill) and does nothing with a logo, a consumer online shop or a social-media profile; the values look copied from Brightmarket's master data, which is the same in every example of the flow (section 4.8 of the review: data copied into a document that does not use it).
- Condition: Brightmarket's party in this document carries only data this document uses.
- Options: Leave the logo, online shop and social-media profile out of the trade documents and keep them for the consumer documents (the purchase receipt and the consumer order), where they have a reason.
- Needs decision: no

### retail/13#F11 · Low · Brightmarket's contact: name, job title and department disagree, and do not fit the role
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:ElectronicMail` = `buying@brightmarket.example`
- Why: The primary contact of Brightmarket (`ConsigneeParty`) is named "Buying office" with the e-mail buying@brightmarket.example, but its job title is "Customer service officer" and its department "Sales": a buying office is part of purchasing, not of sales. In this document it is the consignee, whose contact receives the goods; the order `08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department` names that contact, and neither the buying office nor a sales customer-service officer is it. The same contact is used in every role Brightmarket has in the flow (41 XML files contain `<cbc:Name>Buying office</cbc:Name>`, all with this job title; `grep -rl --include='*.xml'`).
- Condition: The name, job title and department of Brightmarket's contact in this document agree with each other and with Brightmarket's role here.
- Options: Make the master contact consistent (e.g. Buying office / Buyer / Purchasing), and give Brightmarket role-specific contacts where its role is not purchasing (goods-in for delivery and consignee roles, accounts payable for invoices, customer service for sales to consumers). Preferred: role-specific contacts, since the flow already has them in the order.
- Needs decision: no

## Checked and consistent
- Roles: Bayforth is sender, carrier and signatory, Lumeway consignor, Brightmarket consignee, as in the transport request `11-TransportExecutionPlanRequest.xml`.
- Every party is described the same way in every example of the flow: each of the full descriptions of Brightmarket Stores, Lumeway Distribution, Bayforth Forwarding and Harbourline Factoring is identical in all examples that carry it (compared leaf by leaf over all 22 XML files), and the short references (register identifier and name) match them.
- Party identifiers: the register identifiers (Brightmarket 20410411, Lumeway 20410274, Bayforth 20411644, Harbourline 20411233) agree with `PartyLegalEntity/CompanyID` and with the endpoint identifiers `XB:<register number>`; `check_ids.py` finds the check digits of all GS1 keys and IBAN-like accounts in this example correct. The GLN prefix 952 is GS1's prefix for demonstrations and examples (own knowledge), so the GLNs cannot be mistaken for real ones.
- Tax schemes: each Bayvarran party is registered for the state sales tax (STT) of the state its address is in (Lumeway Upland State, the others Coastal State), with matching jurisdiction.

## Considered and refuted
- `/Waybill/cac:ConsignorParty/cac:PartyName/cbc:Name` = `Lumeway Distribution`: suspected that the consignor lacks the address a CMR needs — refuted because the same party (same register identifier 20410274) is described in full in `/Waybill/cac:ReceiverParty`, address included.
- `/Waybill/cac:ReceiverParty/cac:PostalAddress/cbc:BlockName` = `Marrowdale Business Park`: suspected of misusing BlockName for a business park — refuted because the definition ("an area surrounded by streets and usually containing several buildings") fits a business park, and `PlotIdentification` "Plot 14" is the land parcel as defined.
