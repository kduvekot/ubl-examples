# LLM review: 14-GuaranteeCertificate.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: merged

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/14-GuaranteeCertificate.xml`, Git blob `f5253d8d365d2d86594564ab6fe3042c7ef3e212` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 47b872b 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/14#F1 · Medium · A bank guarantee that is also described as immobilised shares of the tenderer itself
- XPath: `/GuaranteeCertificate/cbc:ConstitutionCode` = `BANKGUAR`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SecurityID` = `XU0001042501`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `250`
- XPath: `/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:Description` = `A bank guarantee for the tender.`
- Why: `ConstitutionCode` is "The code stating the constitution means of the Guarantee"; `BANKGUAR` is a bank guarantee, the bank's own undertaking to pay, which is what the notices ask for. `ImmobilizedSecurity` ("Details of an immobilized security") describes another means of constituting a guarantee: securities blocked in favour of the beneficiary. The certificate carries both and does not say how they relate. If the shares are the bank's collateral for issuing the guarantee, they concern only bank and client and do not belong in a certificate for the beneficiary; if they are the guarantee, the code is wrong and the notices' requirement is not met. The security is the tenderer's own ordinary shares (the ISIN of Valdara's listing): a pledge whose value falls exactly when the tenderer fails, an odd story for 2400.00 lume by a company with 250 million ferra of capital (own knowledge of guarantee practice). Medium (context, logistics): the code and the content state two different means; broad and money rated it Low.
- Condition: The certificate describes one means of constitution, the one its code names; immobilised securities appear only where the guarantee is constituted by them (or the document states that they are counter-security).
- Options: (a) remove `ImmobilizedSecurity`: a plain bank guarantee, as the notices require (preferred); (b) a guarantee by immobilised securities, with a constitution code for that, securities of a third issuer (e.g. government bonds), and notices that allow that means; (c) keep both and state in `Purpose` or `Note` that the shares are counter-security.
- Needs decision: yes
- From: broad (F5), context (F1), logistics (F2), money (F3)

### tender/14#F2 · Medium · "Value on the day of immobilisation" 2500.00 and market value 3100.00 three days later
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` = `2500.00`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:MarketValueAmount` = `3100.00`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:IssueDate` = `2026-02-21`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `250`
- Why: UBL defines `FaceValueAmount` as "The value of the security on the day it was immobilized" and `MarketValueAmount` as "The current market value of the immobilized security." Read by the definitions, 250 shares were worth 2500.00 lume (10.00 a share) on 2026-02-21 and 3100.00 (12.40 a share) at the certificate's date, 2026-02-24: a rise of 24 % in three days, over a weekend (2026-02-21 is a Saturday; re-done in the merge: 3100 / 2500 = 1.24). If 2500.00 is instead the nominal value (10 lume a share, as the element's name suggests), the element is used against its definition, which the rule on semantic conformance does not allow. Broad checked the arithmetic per share and found it consistent; that does not touch the definition. If F1 is resolved by removing the aggregate, this finding goes with it.
- Condition: `FaceValueAmount` is the value on the day of immobilisation and is plausible next to the current market value, or the nominal value is not carried in this element.
- Options: (a) a value on the day of immobilisation close to the market value (e.g. 3075.00 and 3100.00) (preferred); (b) the market value at the certificate's date only.
- Needs decision: no
- From: money (F1), context (F1, part)

### tender/14#F3 · Medium · The tenderer named as issuer of the bank's immobilisation certificate
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:PartyName/cbc:Name` = `Bank of Lumeport`
- Why: `IssuerParty` in `ImmobilizedSecurity` is "The Party who issues the Immobilized Security Certificate". The certificate number has the prefix the Bank of Lumeport uses for its guarantee and its signature (`BLUM-…`): the bank, as custodian, blocks the shares and certifies it. Valdara Industries is the issuer of the shares themselves (its own ISIN) and the party that deposits the guarantee (`InterestedParty`); a depositor cannot certify its own deposit. All five parts agree. Medium, not High: the number prefix shows the bank's series, but nothing states outright who issued the certificate.
- Condition: `IssuerParty` is the party that issued the certificate identified in `ImmobilizationCertificateID`.
- Options: (a) the Bank of Lumeport as `IssuerParty` (preferred), or the depository holding the shares if the story has one; (b) drop `IssuerParty` (the issuer of the shares is already given by the ISIN and the interested party's listing).
- Needs decision: no
- From: broad (F2), context (F2), logistics (F1), money (F2), parties (F1)

### tender/14#F4 · Medium · Language code in LocaleCode
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." The value `en`, with `listID` "ISO 639", repeats the language code of the sibling `cbc:ID`; it names no locale. Recounted: 362 occurrences in 213 of the 250 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en</cbc:LocaleCode>' world/examples`).
- Condition: No `cbc:LocaleCode` holds a bare language code: each is absent or holds a locale from a list of locales.
- Options: (a) remove `LocaleCode` (preferred); (b) a locale such as `en-XB` with a matching list.
- Needs decision: no
- From: broad (F4), context (F3), logistics (F3), parties (F2)

### tender/14#F5 · Medium · A province in Region
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran addresses of the flow put their state in `CountrySubentity`. Recounted: 219 occurrences in 104 of the 250 examples (`grep -rho --include='*.xml' '<cbc:Region>Province of Ferrano' world/examples | wc -l`, `-l` for files).
- Condition: The province of an Urvanian address is in `CountrySubentity` (with a code if Urvania has a list); `Region` is absent or holds a region in the sense of the definition.
- Options: (a) move the value to `CountrySubentity` (preferred); a code is optional.
- Needs decision: no
- From: broad (F3), parties (F3)

### tender/14#F6 · Medium · The beneficiary, a public body, described as a company in a commercial register with a liquidation status
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `CompanyLiquidationStatusCode` is "A code signifying the party's liquidation status" (`ACTIVE`: "Active, not in liquidation"); `COMMERCIAL` is "Commercial register: A register of businesses". Lumeport Public Works Department is a public body (`01-PriorInformationNotice.xml:/PriorInformationNotice/cac:ContractingParty/cac:ContractingPartyType/cbc:PartyType` = `Local authority: a department of the city of Lumeport`; ISIC 8411); it is not a business and cannot be in liquidation.
- Condition: A public body carries no liquidation status, and its registration scheme is not typed as a commercial register (or the world's rules say in what capacity public bodies are entered there).
- Options: (a) drop the liquidation status and the `COMMERCIAL` type for public bodies, keeping register name and number (preferred); (b) a register type for public bodies; (c) record the convention in the world's rules.
- Needs decision: no
- From: broad (F8), parties (F8)

### tender/14#F7 · Low · "Released at the award", although a tender guarantee secures the winner's entry into the contract
- XPath: `/GuaranteeCertificate/cbc:Note` = `Released at the award.`
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:EndDate` = `2026-05-27`
- XPath: `22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`
- Why: UBL defines the tender guarantee the terms require as "A financial guarantee of a tenderer or bid submitter's actual entry into a contract in the event that it is the successful bidder" (quoted by money). For the successful tenderer it must last beyond the award (2026-03-09 in this flow) until the contract is concluded and the performance guarantee is constituted (by 2026-03-19); released at the award it would secure nothing in the ten days in which the winner could still walk away. Broad, context and logistics refuted a different angle (the note against the end date: the period is the latest end, the release an earlier one), which the merge accepts; money's argument about the purpose of the guarantee stands.
- Condition: The note on the release agrees with the purpose of a tender guarantee.
- Options: (a) "Released to unsuccessful tenderers at the award and to the successful tenderer when the contract is signed and the performance guarantee is constituted" (preferred); (b) drop the note.
- Needs decision: no
- From: money (F4)

### tender/14#F8 · Low · The address of an article of the Act as "ontology URI"
- XPath: `/GuaranteeCertificate/cac:ApplicableRegulation/cbc:OntologyURI` = `https://law.bayvarra.example/ppa#art61`
- XPath: `/GuaranteeCertificate/cac:ApplicableRegulation/cbc:LegalReference` = `XB-PPA-2019 art. 61`
- Why: `OntologyURI` is "The Uniform Resource Identifier (URI) of an ontology related to this regulation", i.e. of a formal vocabulary of concepts. The value is the anchor of article 61 in the text of the Act (the same address family 06 gives as `Legislation/URI`); a law text is not an ontology, and the legal reference already names the article.
- Condition: `OntologyURI` identifies an ontology, or is absent.
- Options: (a) remove it (preferred); none other seen.
- Needs decision: no
- From: broad (F6), context (F4)

### tender/14#F9 · Low · The immobilised security's issue date is the immobilisation date
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:IssueDate` = `2026-02-21`
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = `2026-02-21`
- Why: For the argument (logistics): `ImmobilizedSecurity/IssueDate` is "The date on which this immobilized security was issued"; the ordinary shares of a company in operation for decades (13) were not issued on 2026-02-21, which is the date of the immobilisation (and the start of the guarantee's period). Against it: the definition can be read as the date the immobilised security (the blocked position, with its certificate) came into being, which is the immobilisation date. The merge cannot settle which reading the model means; Low with both arguments. Logistics' other point in the same finding (the period starting before the certificate) is refuted in the merge.
- Condition: The date carries the meaning chosen for the element (the shares' issue date, or the immobilisation recorded as the reading for the TC write-up).
- Options: (a) leave the element out, since `FaceValueAmount` already refers to "the day it was immobilized" (preferred); (b) the shares' issue date.
- Needs decision: yes
- From: logistics (F4, part)

### tender/14#F10 · Low · Master data the certificate does nothing with: customs trader numbers, Valdara's warehouse contractor and share capital
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- Why: Copied master data (section 4.8). A guarantee certificate "notif[ies] the deposit of a Guarantee, such as a bid bond". Nothing in it is declared to customs (the customs trader numbers are used in 30 and 31), nothing concerns warehousing or despatch (Castrano acts in 29), and the depositor's share capital plays no part. Broad also listed Valdara's `SecurityListing`; the merge takes that line out with parties' refutation (it identifies the very shares that are immobilised, see "Refuted in the merge"), as long as F1 keeps the immobilised security.
- Condition: Each party carries only the identifiers and related data the document's purpose uses.
- Options: (a) leave them out of the tendering documents (preferred); (b) keep them only where the document says what they are for.
- Needs decision: no
- From: broad (F7, part), context (F5, F6), parties (F4)

### tender/14#F11 · Low · Valdara's address tagged en-XB here and en-XU in its own documents; Italian names tagged English
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PostalAddress/cbc:CityName[2]` = `Ferrano`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- Why: The same English rendering of Valdara's address is tagged `en-XB` here and `en-XU` in 13 and 15, and the street name tagged as English is Italian. Parties refuted it: these are the world's English-language names of Urvanian places (accepted as given), the texts are identical everywhere, and the tag follows the issuer's locale consistently. analysis/review-merge-decisions.md keeps this Low with Needs decision yes in every flow, because no rule is recorded; the merge aligns, as in 12 F10, and carries the refutation as the counter-argument.
- Condition: One documented rule decides the tag of a party's English rendering (the party's own variety or the issuer's), and it is applied in every example.
- Options: (a) record the rule (issuer's variety) in the world's conventions (preferred: it is already applied consistently); (b) tag the party's own variety (`en-XU`) everywhere.
- Needs decision: yes
- From: merge (parties' refuted candidate, aligned with the main decisions table)

### tender/14#F12 · Low · Valdara's legal form in a single untagged rendering
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Skenekhalhek tevul ginek gerrir (hakdrul dudrul riskek)`
- Why: The address of the same party is given in Urvanian and English, each tagged; the legal form has one rendering without `languageID`, while 13 and 15 give it in Urvanian (`qau`) and English (`en-XU`). Earlier merges keep this as a separate Low/no finding; as 12 F11.
- Condition: The legal form is rendered like the address: in each language the document uses for the party, each tagged.
- Options: (a) both renderings, tagged, as in 13 (preferred); (b) one rendering with its `languageID`.
- Needs decision: no
- From: merge (parties' refuted candidate, aligned with the main decisions table)

### tender/14#F13 · Low · Large enterprise with 180 employees
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:FinancialCapability/cbc:ValueAmount` = `9200000.00`
- Why: The world's list defines `LARGE` as "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (above 50,000,000.00 XBL; `world/codelists/gc/EntitySizeCode.gc`). In its qualification Valdara states 180 employees and a financial capability of 9200000.00 lume; nothing in the flow states a turnover above the limit. Broad rated it High; the merge follows parties (Low, decision yes) and merger C: the definition's "or a turnover above …" leaves room, and the 9200000.00 is not stated to be the turnover, so no strict contradiction can be shown (unlike Marrowdale's `SMALL` with 85 persons, 10 F1). Same finding as 12 F12 and 13 F16.
- Condition: The size class of Valdara agrees with the employees and financial figures stated for it in the flow.
- Options: (a) state a turnover above 50 million lume (or 250+ employees) if Valdara is meant to be large (preferred: listed, 250 million ferra of capital); (b) `MEDIUM` in every example that describes it.
- Needs decision: yes
- From: broad (F1), parties (F5)

### tender/14#F14 · Low · Valdara's contact is its order desk
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:Contact/cbc:ElectronicMail` = `order@valdara.example`
- Why: Valdara is the party that deposits a bid bond; its contact is the order desk (customer service officer, `order@…`), the function that takes purchase orders (right in the order documents 26–28). Questions on a guarantee for a tender go to whoever prepares bids or handles the company's banking.
- Condition: Valdara's contact in the tendering documents is a function that handles tenders or guarantees, or is left out where the document needs none.
- Options: (a) a tender or finance contact for Valdara (preferred); (b) leave the contact out here.
- Needs decision: no
- From: parties (F6)

### tender/14#F15 · Low · The department's tax exemption reason describes a sale, not the party's status
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: `ExemptionReason` in `PartyTaxScheme` is "A reason for the party's exemption from tax, expressed as text": the party's status. "Sale to a public body" names a transaction. The code's list definition ("A body of the federation, a state or a city buys free of sales tax") is a buyer status and fits; the wording does not.
- Condition: The party's exemption reason states the party's status.
- Options: (a) reword the text, e.g. "Public body: buys free of the state sales tax", keeping the code (preferred); (b) a code named for the status.
- Needs decision: no
- From: broad (F9), parties (F7)

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` has a correct check digit (as `SecurityID` and in Valdara's listing, the same security); XU lies in the user-assigned range of ISO 3166, so it cannot be a real ISIN.
- Liability 2400.00 lume and type `TENDER` equal the required financial guarantee of the tendering terms (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`). The certificate (2026-02-24 08:23) is issued before the end of the constitution period (2026-02-26) and before Valdara's tender (2026-02-25 09:13), whose fee line mentions the courier for the guarantee's original.
- `ApplicablePeriod/EndDate` 2026-05-27 = tender deadline 2026-02-26 + 90 days of tender validity (2 + 31 + 30 + 27 = 90; re-done).
- Shares: 250 E21 (shares, Rec. 20); 2500.00 / 250 = 10.00 a share, 3100.00 / 250 = 12.40; the market value covers the liability 1.29 times.
- Guarantor a bank (ISIC 6419) in Lumeport; interested party the tenderer of 15; beneficiary the contracting department; `ContractFolderID` `PWD-2026-PARKS`; `LegalReference` names the procurement act of the notices. Parties described as in the other examples of the flow (parties compared by script); +999 telephone numbers and `.example` addresses.

## Considered and refuted
- `/GuaranteeCertificate/cbc:ID`: prefix `BL-` while the bank's other numbers begin with `BLUM-` — refuted, document numbers follow the flow's `<abbreviation>-DOC-26-nnnn` pattern and may be a separate series (from broad, context, logistics).
- `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate`: the period starts three days before the certificate — refuted, the guarantee can be effective from its constitution (immobilisation 2026-02-21) and certified later (from broad, context; logistics' finding on it is refuted in the merge, below).
- `/GuaranteeCertificate/cbc:Note`: "Released at the award." against the end date 2026-05-27 — refuted, the period is the latest end, the release an earlier event (from broad, context, logistics); money's different argument is F7.
- `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` and `cbc:MarketValueAmount` in lume although the shares are Urvanian — refuted, a certificate for a liability in lume reasonably values the collateral in lume (from broad, money).
- `/GuaranteeCertificate/cac:GuarantorParty/cac:Contact/cbc:JobTitle`: a client relationship manager in trade services — refuted, it fits a bank's guarantee business (from broad).
- `/GuaranteeCertificate/cac:GuarantorParty`: the model calls it "The guarantee creditor organisation who has the authority to charge bid bond guarantee credit" — refuted, the bank that gives the guarantee is what the element and the flow mean (from context).
- `/GuaranteeCertificate/cac:GuarantorParty`: no BIC and no tax scheme — refuted, the bank is identified by its register number like every party, and no payment is made under this document (from parties).
- `/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID`: `BLUM-G-26-0221` resolves to no example — refuted, it is the bank's guarantee instrument ("A reference to a legal document"), not a UBL document of the flow (from logistics).
- `/GuaranteeCertificate/cbc:ContractFolderID`: the certificate does not name the tender it secures — refuted, the tender does not exist yet on 2026-02-24; folder, interested party and beneficiary identify the purpose (from logistics).
- `/GuaranteeCertificate/cbc:LiabilityAmount`: 2400.00 against the 2 % rate of the tendering terms — refuted for this example: the certificate states no rate and repeats the amount the terms require; the mismatch lies in 01–03 (from money).
- `/GuaranteeCertificate/cac:InterestedParty/cac:PostalAddress/cbc:StreetName[2]`: Italian text tagged English, and en-XB here against en-XU in Valdara's own documents — refuted by parties (world names; the tag follows the issuer consistently); the merge made it F11 and F12, aligned with the main decisions table (as 12 F10, F11), with this argument.
- `/GuaranteeCertificate/cac:GuarantorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount`: an amount where the definition says "The number of shares in the capital stock of a corporation" — refuted, the element is of an amount type; a point for the TC write-up (from parties).
- `/GuaranteeCertificate/cac:InterestedParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: ICD `0990` assigned in ISO 6523 — refuted as far as own knowledge goes; the ICD register was not available to check (from parties; the merge could not check it either).
- `/GuaranteeCertificate/cac:InterestedParty/cac:Language/cbc:ID`: `qau` a real ISO 639 code — refuted, qaa–qtz is reserved for local use (from parties).
- `/GuaranteeCertificate/cac:GuarantorParty/cac:PostalAddress/cbc:TimezoneOffset` = `-1` — refuted, no format prescribed, reads as UTC−1 (from parties).
- `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14` — refuted, fits "The specific identifable location within a building where mail is delivered" (from parties).
- `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cac:SecurityListing`: master data without use — refuted, it identifies the very shares that are immobilised (from parties; see also "Refuted in the merge").

## Refuted in the merge
### logistics/F4 (part) · Low · The guarantee takes effect three days before the certificate is issued and four before the tender it secures
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = `2026-02-21`
- XPath: `/GuaranteeCertificate/cbc:IssueDate` = `2026-02-24`
- Why (logistics): `ApplicablePeriod` is "The specified period in the tendering process for which this Guarantee is effective"; it starts on 2026-02-21, before the certificate and before the tender exists (15: 2026-02-25); a tender guarantee secures the tender from its submission, at the latest from the deadline. Condition: the guarantee's period does not start before the guarantee is issued, or the earlier start is explained.
- Refuted because: the document is "A document to notify the deposit of a Guarantee": it reports a guarantee already constituted (the immobilisation of 2026-02-21), and a bid bond must exist before the tender is submitted, so a start before both the certificate and the tender is the normal order (broad and context refuted it on the same grounds). The other part of logistics/F4 (the security's issue date) is kept as F9.

### broad/F7 (part) · Low · Valdara's security listing in the guarantee certificate
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why (broad): the listing is master data a guarantee certificate does nothing with. Condition: the party carries only what the document uses.
- Refuted because: the listing names the security whose ISIN the certificate's `ImmobilizedSecurity/SecurityID` carries, so the document uses it (parties). If F1 is resolved by removing the immobilised security, the listing becomes unused and joins F10.

## Changed in the merge
- broad/F5, money/F3 (Low) and context/F1, logistics/F2 (Medium) → F1 Medium, Needs decision yes: the constitution code and the content state two different means.
- context/F1: the face/market value part moved into F2 with money/F1.
- broad/F2, context/F2, logistics/F1, money/F2, parties/F1 combined → F3.
- broad/F8, parties/F8 (Low) → F6 Medium: aligned with analysis/review-merge-decisions.md (public bodies as companies).
- logistics/F4 split: the period start refuted in the merge (above), the security's issue date kept as F9 with Needs decision yes (cannot settle).
- broad/F7, context/F5, context/F6, parties/F4 combined into F10 (one copied-master-data finding per example); the security listing line refuted in the merge (above).
- F11 and F12 added from parties' refuted candidate, aligned with the main decisions table (as 12 F10, F11).
- broad/F1 (High/no) → F13 Low/yes, with parties/F5: no strict contradiction under the `LARGE` definition; aligned with merger C.

## Outside this review
- No guarantee certificate exists for Brackenmere Furniture, which also tenders (17, 19), although the notices require one from every tenderer; whether the flow needs one is a question of its story (from broad, context).
- Valdara's tender (15) does not cite this certificate or the guarantee number; noted in 15 (from context).
