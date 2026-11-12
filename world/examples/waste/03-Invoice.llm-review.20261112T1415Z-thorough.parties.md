# LLM review: 03-Invoice.xml

Flow: waste (WASTE-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1415Z-thorough`
- Example: `world/examples/waste/03-Invoice.xml`, Git blob `802363ed10113ef3a82c854031713a677b74609e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns)
- Skill: `.claude/skills/ubl-example-review`, last commit d3d18df 2026-11-12 Review skill: the repository's agreed rules (no fillers, semantic conformance over practice, no fictional value that a real register assigns) (committed)
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

### waste/03#F1 · Medium · Province in `Region` instead of `CountrySubentity`
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a territorial division of the country and belongs in `CountrySubentity`, which the world uses for Bayvarra's states (799 occurrences over `*.xml`). The same value occurs 219 times in 104 examples (`grep -rc --include='*.xml' '<cbc:Region>Province of Ferrano'`, summed).
- Condition: no address in this example carries a province in `Region`; a province, where given, is in `CountrySubentity`.
- Options: (preferred) move the province to `CountrySubentity` for all Urvanian addresses; or drop it where the postal zone suffices.
- Needs decision: no

### waste/03#F2 · Low · Customs and capital-market data of the parties copied into a domestic service invoice
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID` = `XU-TR-104548`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The invoice bills Rinova's collection and recovery service to Valdara, both in Ferrano, Urvania, with Urvanian VAT at the standard rate; no customs procedure is involved, so the customs-trader identifiers of both parties have no use. The customer's share capital, stock-exchange listing and its warehousing-and-despatch provider Castrano Logistics play no part in billing this service either. The same Valdara blocks occur in 75 examples (`grep -rl --include='*.xml' -F 'VI-SP-2026-01'`), i.e. master data copied into every document (section 4.8). (In UBL, share capital on an invoice is sometimes a legal requirement for the *seller*; here it is the buyer's.)
- Condition: every party detail present has a use in this invoice.
- Options: (preferred) leave these elements out of the invoice's parties; or give the reason in the example where one exists.
- Needs decision: no

### waste/03#F3 · Low · Supplier registered on 1 January 1996
- XPath: `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID". The same New Year's Day date is given to 25 different legal entities (script over `world/examples/*/*.xml` collecting `PartyLegalEntity/RegistrationDate` per `RegistrationName`; 181 files), while others have individual dates (the customer `1962-04-12`); it looks like a default rather than Rinova's registration date (rule "no fillers").
- Condition: Rinova's `RegistrationDate` is its own registration date in the world, or is absent.
- Options: (preferred) an individual plausible date; or remove the element. If the world has all registers re-founded on 1996-01-01, record that and dismiss.
- Needs decision: yes

### waste/03#F4 · Low · Buyer's contact is the buyer's own sales order desk
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: The accounting customer's contact is whom the supplier contacts about the invoice (accounts payable) or the purchase of the service (purchasing, the plant that hands over the waste). Valdara's contact is its sales order desk, which takes orders from Valdara's own customers. Valdara carries this same contact in all its 75 examples whatever its role (`grep -rl --include='*.xml' -F 'order@valdara.example'`), which shows it is one master contact rather than one chosen for the role.
- Condition: the customer's contact in the invoice is one that deals with this purchase or with paying invoices.
- Options: (preferred) an accounts-payable or purchasing contact for Valdara as buyer; or omit the contact.
- Needs decision: no

## Checked and consistent
- Supplier and customer are the parties of the waste flow: Rinova (recovery facility, sender of `02-WasteMovement.xml`) bills Valdara (producer and notifier); identifiers, names, addresses, tax numbers and legal entities are identical to `01-WasteNotification.xml` and `02-WasteMovement.xml` (c14n comparison of each party block).
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:Name` = `Rinova Recovery SRU`: the payee account is held in the supplier's registered name, and its country (XU) agrees with the supplier's address.
- Both parties are registered for VAT in Urvania (`PartyTaxScheme/CompanyID`, scheme XU tax), which the standard-rated domestic service needs.
- Legal forms and sizes fit the parties (SRU small recovery company; SUA large listed manufacturer); ISIN check digit OK (`check_ids.py`).

## Considered and refuted
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-ENV-2024-0311`: suspected an authorization copied into an invoice that does not use it — refuted because the invoice bills the recovery of the waste, and the permit under which the supplier recovers it is a legitimate statement on such an invoice.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`: suspected an unfit contact — refuted because the seller's customer service is the right contact for the buyer's questions about the invoice.
- `/Invoice/cac:AccountingCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `3100`: suspected a mismatch between a furniture maker and the waste service — refuted, a furniture maker produces plastic production waste.
- `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cac:FinancialInstitution/cbc:ID` = `CREVXUFR`: suspected a real BIC — refuted because `XU` is a user-assigned ISO 3166 code, so no real BIC has this country part.
