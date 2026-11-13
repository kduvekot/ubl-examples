# LLM review: 28-DebitNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: parties

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/28-DebitNote.xml`, Git blob `3e29e6ed200cefac7cd779458723625c3b873f75` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 9726a5a 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/28#F1 · High · Accounting supplier and customer are the reverse of seller, buyer, payee and issuer
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:SellerSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeway Distribution`
- XPath: `/DebitNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Velumi Trading`
- XPath: `/DebitNote/cac:BuyerAssignedReference/cbc:BuyerReferenceCode` = `LD-AP-CLAIMS`
- Why: A debit note is "a document used to specify debits due to the Creditor from the Debtor". Here Velumi issues and signs it (`VT-DOC-…`), is the seller of the recharged costs and the payee, and gives its own account for payment; Lumeway is the buyer and routes the note to its accounts payable claims unit. The creditor is thus Velumi and the debtor Lumeway. Yet the accounting supplier (the party claiming payment) is Lumeway and the accounting customer (the party that pays) is Velumi, which makes the accounting customer also the payee of its own debt. The document's own parties contradict each other; with them as they stand, the debit note says that Velumi owes Lumeway and that Lumeway pays Velumi. The accounting cost `500` 'Stock for municipal projects', defined as "the Buyer's accounting code", is Velumi's code from the order chain, which again treats Velumi as buyer.
- Condition: Accounting supplier, seller, payee and signatory are the same creditor, and accounting customer and buyer the same debtor (Velumi creditor, Lumeway debtor, if the story is that Velumi recharges its costs).
- Options: (a) Velumi as accounting supplier and Lumeway as accounting customer, with the payee dropped (it would equal the supplier) and the buyer's accounting cost Lumeway's (preferred: matches issuer, payee and the buyer reference); (b) if the intent is a buyer-issued debit note against the original invoice, keep Lumeway as accounting supplier and make seller, buyer and payee follow the original sale, with Lumeway paying by reducing its claim; this conflicts with UBL's creditor/debtor definition.
- Needs decision: no

### sea/28#F2 · Medium · The customs service as originator of the order
- XPath: `/DebitNote/cac:DebitNoteLine/cac:OriginatorParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: The line's `OriginatorParty` is "the Party who originated the Order to which the Debit Note is related". The order is Velumi's `VT-PO-26-0127`, which the Port of Selanu originated (`05-Order.xml:/Order/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`). The customs service inspected the container and charged a fee; it did not originate the order. The element is used for the party that caused the cost.
- Condition: The line's originator is the party that originated the order, or the element is absent; the customs service appears, if at all, in an element that says what it did (e.g. the work report it issued).
- Options: (a) drop `OriginatorParty` from the line; the work report reference already says the inspection was the customs service's (preferred); (b) the Port of Selanu as originator, as in the order.
- Needs decision: no

### sea/28#F3 · Medium · The inspection fee is "collected for" customs although Velumi recovers its own expense, and the storage is attributed to two parties
- XPath: `/DebitNote/cac:DebitNoteLine/cac:CollectedForParty/cac:PartyName/cbc:Name` = `Island Customs Service`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:DocumentReference/cbc:ID` = `XL-CUS-RCPT-26-0517`
- XPath: `/DebitNote/cac:DebitNoteLine/cac:SubDebitNoteLine[2]/cac:Item/cbc:Name` = `Storage at the port`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cbc:Note` = `The port's storage charge for the day the container was held, collected for the port.`
- XPath: `/DebitNote/cac:CollectionDebitNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: `CollectedForParty` is "the Party on whose behalf this item or amount is collected". The line refers to the customs receipt (`XL-CUS-RCPT-26-0517`): the fee has been paid to customs already, so Velumi now recovers its own expense, and the line's beneficiary is Velumi itself; nothing is collected on the customs service's behalf. The same line also carries the storage at the port (sub-line 1.2 and its charge of 12.750), which the collection line 2 says is "collected for the port", with the port as beneficiary. The storage charge is thus attributed to the customs service in line 1 and to the port in line 2. In line 2, which is the line "collected on behalf of a third party", the port is given as `BeneficiaryParty` rather than in the dedicated `CollectedForParty`.
- Condition: Each amount is attributed to one party: the inspection fee recovered for Velumi (no `CollectedForParty`, or Velumi only as beneficiary), the storage either a third-party collection for the port in line 2 with the port as `CollectedForParty`, or part of line 1, not both.
- Options: (a) line 1 only the inspection fee without `CollectedForParty`; line 2 the storage with the port as `CollectedForParty` (preferred: one party per amount, dedicated elements); (b) keep both in line 1 and drop line 2, with no collected-for party.
- Needs decision: no

### sea/28#F4 · Medium · A gate in Lumeway's AdditionalStreetName
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "an additional street name used to further clarify the address". A business-park gate is a vehicle access point, not a street, and has no use in the postal address of Lumeway in a debit note. The value occurs 79 times in 76 files over `world/examples/*/*.xml`, always in Lumeway Distribution's address (grep over *.xml).
- Condition: The postal address holds no gate.
- Options: (a) drop the gate from the postal address and give it only where vehicles need it (preferred); (b) the name of the park's internal road if it has one.
- Needs decision: no

### sea/28#F5 · Medium · A language code in LocaleCode
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "a code signifying the locale in which this language is used"; the value repeats the ISO 639 language code of `Language/cbc:ID` (`listID="ISO 639"`) and names no locale. The same value occurs 362 times in 213 files over `world/examples/*/*.xml` (grep over *.xml).
- Condition: `LocaleCode` is absent or holds a locale (language and country).
- Options: (a) drop `LocaleCode` where it only repeats the language (preferred); (b) a locale such as `en-XB` with a list that defines locales.
- Needs decision: no

### sea/28#F6 · Low · Contacts that do not fit a claim between the two companies
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DebitNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Lumeway routes the note to its accounts payable claims unit (`LD-AP-CLAIMS`), but its contact is its sales customer service. Velumi, which raises the claim, gives a contact named Purchasing who is a customer service officer in Sales: name, title and department disagree, and none of them is the claims function that raised `VT-CLAIM-26-0021`. Both are master-data contacts.
- Condition: Each contact's name, job title and department agree and are the functions handling the claim on each side.
- Options: (a) claims or accounts contacts on both sides (preferred); (b) drop the contacts.
- Needs decision: no

### sea/28#F7 · Low · Lumeway's tax registration, share capital and customs number in a recharge outside the scope of tax
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/DebitNote/cac:AccountingSupplierParty/cac:Party/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XB-TR-410274`
- Why: The debit note is taxed as outside the scope of tax under "No general sales tax"; Lumeway's Bayvarra sales-tax registration, its share capital and its customs trader number play no part in Velumi's recharge. They are copied from Lumeway's master data (section 4.8 of the review rules); Velumi, the issuer, carries no tax scheme.
- Condition: Lumeway carries only the party data the debit note uses.
- Options: (a) drop `PartyTaxScheme`, `CorporateStockAmount`/`FullyPaidSharesIndicator` and the customs trader identifier (preferred); (b) keep them with a reason.
- Needs decision: no

## Checked and consistent
- Signatory, payee and seller are the same party (Velumi Trading, `IC41859`), and the payee account `XL40BSEL0010003665515` is in Velumi's name at the Bank of Selanu, the same account Velumi pays from in `27-RemittanceAdvice.xml`.
- The Port of Selanu (`IC41037`) as beneficiary of the storage charge is the port where the container was held (`17-TransportationStatus.xml` reports its detention there).
- Velumi's address and legal form carry `en-XL` and Lisavan renderings, as in its other documents; Lumeway's description is identical to the other examples (compared with a script).
- GLN, IBAN-like account, RF reference and container number pass their checks (check_ids.py).

## Considered and refuted
- `/DebitNote/cac:DebitNoteLine/cac:BeneficiaryParty/cac:PartyName/cbc:Name`: Velumi as beneficiary of its own line — refuted because it is the party that derives benefit from the recovered fee.
- `/DebitNote/cbc:Note[2]`: the packer named as responsible, but absent as a party — refuted because the annotation leaves the claim against the packer to the distributor; the packer is not a party to this debit note.
