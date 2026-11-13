# LLM review: 13-BillOfLading.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/13-BillOfLading.xml`, Git blob `c90a3571519a90b3221ab1bd12b871dc2751864d` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/13#F1 · High · The bill goes to the bank and the mill, while the forwarding instructions ask for it to go to the forwarder
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- Why: The forwarding instructions this bill refers to (`/BillOfLading/cac:DocumentReference/cbc:ID` = `LTM-FI-26-0199`) say `09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.` The distribution list sends the original by courier to the Bank of Selanu and a scanned copy to the mill; the forwarder Bayforth, named in the same bill, receives nothing. The two documents contradict each other about who gets the bill.
- Condition: The distribution of the bill agrees with the instruction in 09-ForwardingInstructions.xml (the forwarder receives the bill), or the instruction is changed to match.
- Options: (a, preferred) send the original to Bayforth Forwarding as instructed, and the copy to the mill if wanted; (b) change the instruction in 09 if the bank is meant to receive the original (see the mortgage-holder finding).
- Needs decision: no

### cotton/13#F2 · Medium · The Bank of Selanu as mortgage holder and recipient of the original bill of lading, with no financing or collection in the flow
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cac:Party/cac:PartyName/cbc:Name` = `Bank of Selanu`
- XPath: `/BillOfLading/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALCOURIER`
- Why: `cac:MortgageHolderParty` is "The Party who holds the mortgage for this Consignment." Sending the original bill of lading to the seller's bank would fit a documentary collection or a pre-export loan secured on the bales, but nothing in the flow has either: the ginnery invoices the mill on open account (`16-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `45 days net.`, paid by credit transfer in 18-RemittanceAdvice.xml), and the forwarding instructions ask for a straight bill to the mill (`09-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ToOrderIndicator` = `false`), under which a bank holding the original gains no control of the goods. The bank's role has no counterpart in the documents that should show it.
- Condition: A mortgage holder and a bank recipient of the original appear only if the flow shows the financing or collection behind them (a loan, a documentary collection or credit, a bill made out to order), consistently in the invoice, the forwarding instructions and the payment.
- Options: (a, preferred) drop the mortgage holder and send the original to the consignee or the forwarder (09 asks for the bill to go to the forwarder); (b) give the ginnery a crop loan from the Bank of Selanu, or a documentary collection, and show it in 09, 16 and 18.
- Needs decision: yes

### cotton/13#F3 · Medium · Language code in `LocaleCode`
- XPath: `/BillOfLading/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value `en` (listID `ISO 639`) is a language code that only repeats `cac:Language/cbc:ID`; it names no locale (a language in a region, such as the `en-XB` the examples use as `languageID` for Bayvarran English). The same value occurs in 213 of the 250 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: Every `cac:Language/cbc:LocaleCode` holds a locale (language and region) from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`: `cbc:ID` already says English and nothing in the document uses a locale; (b) give a locale such as `en-XB` with a list that defines locales (BCP 47).
- Needs decision: no

### cotton/13#F4 · Low · The mill's contact: name, job title and department contradict each other and the role
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: The functional contact name `Purchasing` says buying, the department `Sales` and the job title `Customer service officer` say selling: the three do not describe the same contact. Here the mill is the consignee of a bill of lading, the party the carrier notifies and releases the container to; a purchasing contact does not fit that role. The same combination (a contact named Purchasing in department Sales) occurs in 52 example files (`grep -rl --include='*.xml' '<cbc:Name>Purchasing</cbc:Name>'` piped to `xargs grep -l '<cbc:Department>Sales</cbc:Department>'`).
- Condition: The mill's contact has a name, job title and department that agree with each other and with the role the mill has in this document.
- Options: (a, preferred) a purchasing contact in a purchasing department (e.g. job title Buyer), and in a consignee or importer role a goods-receiving or import contact; (b) drop JobTitle and Department and keep the functional name.
- Needs decision: no

### cotton/13#F5 · Low · The ginnery's address and legal form are rendered differently than in the other examples
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` (languageID `en-XB`)
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield` (languageID `en-XB`)
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company` (no languageID, no Lisavan rendering)
- Why: In the examples the ginnery sends, its English address parts carry `languageID` `en-XL` and its legal form is given in Lisavan and English (`01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Gin Yard Road` with `en-XL`; `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`, `01-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`). Here the same English names are tagged `en-XB` (Bayvarran English), the Lisavan street and city names are kept, but the Lisavan legal form is dropped and the English one has no `languageID`. The names of a Lisavan street and town are Lisavan English whoever sends the document, so the same party is described in two ways in the flow (the same happens in 02, 07, 08, 09, 13, 15 and 18, all sent by Bayvarran parties).
- Condition: The ginnery's address and legal form carry the same renderings and the same `languageID`s in every example of the flow.
- Options: (a, preferred) the renderings and tags of 01-SelfBilledInvoice.xml everywhere, because `languageID` describes the text, not its reader; (b) if the tags are meant to follow the recipient's locale, apply that to every text of the party and record the rule.
- Needs decision: no

### cotton/13#F6 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/BillOfLading/cac:ConsignorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:FreightForwarderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `cbc:RegistrationDate` is "The registration date of the CompanyID." In this flow the ginnery, the mill, Bayforth Forwarding and both ports are all registered on 1 January 1996, in two different registers (`XL:ICR` and `XB:FBR`); the date occurs 271 times in 181 of the 250 example files (`grep -rho --include='*.xml' 'RegistrationDate>[0-9-]*<' | sort | uniq -c`), far more than any other date. That looks like a default rather than each company's history (no fillers, IND5). It may be deliberate (e.g. a general re-registration under the Trade Accord), which the examples alone cannot show.
- Condition: Each `RegistrationDate` is the date on which that party was registered in the world's story, or the element is absent.
- Options: (a, preferred) a date from each company's history; (b) drop `RegistrationDate` where the world has no date; (c) if 1996-01-01 is a register-wide date, say so in the world's story so it reads as a reason, not a default.
- Needs decision: yes

## Checked and consistent
- The bill is issued and signed by the carrier Tidewell Ocean Lines (`20411918`), the receiver of the VGM in 12 and reporter in 14; consignor (the ginnery), forwarder (Bayforth) and consignee (the mill) agree with 09.
- Tidewell's, Bayforth's and the mill's full descriptions are identical to those in 12/14/17, 09/17 and 09/11 (compared block by block).
- The scanned copy to the mill fits its role as consignee and buyer.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:MortgageHolderParty/cac:PartyIdentification/cbc:ID` = `IC41996`: suspected because the same bank is identified by `BSELXLSL` in the payment means of other examples — refuted, a party identifier from the companies register and a bank identifier in a financial institution are different kinds of identifier, both legitimate.
