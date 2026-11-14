# LLM review: 14-GuaranteeCertificate.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/14-GuaranteeCertificate.xml`, Git blob `f5253d8d365d2d86594564ab6fe3042c7ef3e212` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 6afb7cd 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
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

### tender/14#F1 · High · Valdara Industries is a large enterprise, but declares 180 employees
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `LARGE`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cbc:EmployeeQuantity` = `180`
- Why: EntitySizeCode `LARGE` means "250 persons or more, or a turnover above the limits of a medium-sized enterprise" (50,000,000.00 XBL) in the world's list (`world/codelists/lists.json`, EntitySizeCode). In its tenderer qualification (13) Valdara declares 180 employees ("The number of people employed by this qualifying party") and a financial capability of 9 200 000.00 lume; 12 gives a production value of 4 800 000.00 lume. No figure in the flow supports a turnover above 50 million lume, so by the figures it gives the company is medium-sized.
- Condition: Size class, number of employees and the financial figures of Valdara Industries agree.
- Options: (a) at least 250 employees in 13 (preferred: a listed company with a share capital of 250 million ferra and its own foundry is plausibly large); (b) size `MEDIUM` wherever the party is described.
- Needs decision: no

### tender/14#F2 · Medium · The tenderer named as issuer of the bank's immobilization certificate
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SecurityID` = `XU0001042501`
- Why: IssuerParty in ImmobilizedSecurity is "The Party who issues the Immobilized Security Certificate". The certificate `BLUM-IMM-26-0044` carries the bank's prefix (as its guarantee `BLUM-G-26-0221` and signature `BLUM-SIG-GC`): the bank, as custodian, certifies that the securities are blocked. Valdara Industries is the issuer of the security itself (its own shares, ISIN `XU0001042501`), which is a different thing, and it is the party depositing the guarantee; a depositor cannot certify its own deposit.
- Condition: The issuer party is the party that issued the immobilization certificate.
- Options: (a) Bank of Lumeport as IssuerParty (preferred); (b) drop IssuerParty.
- Needs decision: no

### tender/14#F3 · Medium · A province in Region
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political or administrative division of the country, for which CountrySubentity exists ("The political or administrative division of a country in which this address is located, such as the name of its county, province, or state"). The Bayvarran addresses of the flow do use CountrySubentity for their state. The same value is in 22 of the 36 examples of the flow (grep for `Province of Ferrano` over the `*.xml` of the flow, files counted).
- Condition: The province is in CountrySubentity (with its code where the country has one); Region is used only for a region that is not an administrative division.
- Options: (a) move the province to CountrySubentity (preferred); (b) none other seen.
- Needs decision: no

### tender/14#F4 · Medium · Language code in LocaleCode
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used." `en` with listID `ISO 639` repeats the language (already in `cbc:ID`); it is not a locale (a language as used in a place). The value carries another meaning than the element's and adds nothing. The same value sits in every fully described English-speaking party of the flow.
- Condition: LocaleCode, where present, identifies a locale from a list of locales; otherwise it is absent.
- Options: (a) remove LocaleCode (preferred); (b) use a locale code such as `en-XB` with a suitable list.
- Needs decision: no

### tender/14#F5 · Low · A bank guarantee and immobilized shares for the same 2 400 lume
- XPath: `/GuaranteeCertificate/cbc:ConstitutionCode` = `BANKGUAR`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `250`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` = `2500.00`
- XPath: `/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`
- Why: ConstitutionCode is "The code stating the constitution means of the Guarantee": a bank guarantee. A guarantee constituted by a bank's undertaking needs no immobilized securities; ImmobilizedSecurity describes the other way of constituting a guarantee (blocking securities in favour of the beneficiary). The certificate does not say how the two relate (collateral Valdara gave the bank? a second security for the department?). That the tenderer pledges 250 of its own shares for a bid bond of 2 400 lume is also an odd story for a listed company.
- Condition: The certificate states one means of constitution, or says how the immobilized securities relate to the bank guarantee.
- Options: (a) remove ImmobilizedSecurity from the bank guarantee (preferred, unless another example is to carry it); (b) constitute the guarantee by immobilized securities and change the constitution code.
- Needs decision: yes

### tender/14#F6 · Low · A link to the article of the law as "ontology URI"
- XPath: `/GuaranteeCertificate/cac:ApplicableRegulation/cbc:OntologyURI` = `https://law.bayvarra.example/ppa#art61`
- Why: OntologyURI is "The Uniform Resource Identifier (URI) of an ontology related to this regulation." The value is the address of the article in the law collection, not an ontology (a formal vocabulary of concepts).
- Condition: OntologyURI points to an ontology, or the element is absent.
- Options: (a) remove it; LegalReference already identifies the article (preferred); (b) none other seen.
- Needs decision: no

### tender/14#F7 · Low · Master data of Valdara Industries that this document does nothing with
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- Why: The party depositing the guarantee is described with its logistics service provider (Castrano Logistics, warehousing and despatch, with a key account desk), its share capital and its stock exchange listing. A guarantee certificate notifies the deposit of a bid bond. Nothing in it concerns warehousing, despatch or listed shares; the data looks copied from the party's master data (section 4.8 of the review rules: data copied into a document that does not use it).
- Condition: The party carries only what this document uses or what identifies it.
- Options: (a) remove the service provider, the security listing and the stock amount here (preferred); (b) keep them only in the documents where they matter (despatch, business information).
- Needs decision: no

### tender/14#F8 · Low · A public body described as a company in a commercial register
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: Applies to: Lumeport Public Works Department. A public body (a department of the city of Lumeport, a public information service, a review board) is not a company: it cannot be in liquidation, and a commercial register is not where a public body is registered. The same description of the Lumeport Public Works Department is used in all 36 examples of the flow (compared by a hash of the party's leaf values).
- Condition: A public body carries no liquidation status, and its registration scheme is described as what it is.
- Options: (a) drop CompanyLiquidationStatusCode for public bodies and give the scheme a type other than "Commercial register" (preferred); (b) keep the business register and say in the world's rules that public bodies are entered in it.
- Needs decision: no

### tender/14#F9 · Low · The department's tax exemption reason describes a sale
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyTaxScheme/cbc:ExemptionReasonCode` = `PUBLIC`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:PartyTaxScheme/cbc:ExemptionReason` = `Sale to a public body: public bodies are exempt from the state sales tax`
- Why: ExemptionReasonCode in PartyTaxScheme is "A reason for the party's exemption from tax". The code's name is "Sale to a public body", a property of a transaction; the party's own status is "is a public body". The same value is in every example of the flow that describes the department in full.
- Condition: The party's exemption reason states the party's status; a transaction's reason stays on the tax category of the transaction.
- Options: (a) a party-status code ("public body") for PartyTaxScheme (preferred); (b) keep the code and reword the text to the status only.
- Needs decision: no

## Checked and consistent
- check_ids.py: ISIN `XU0001042501` has a correct check digit (twice: the immobilized security and Valdara's listing, the same security).
- Liability 2 400.00 lume and type `TENDER` equal the guarantee required in 02 and 03; the certificate (2026-02-24) is issued before the constitution deadline 2026-02-26 and before Valdara's tender (2026-02-25).
- Applicable period 2026-02-21 to 2026-05-27: the end is the tender deadline 2026-02-26 plus the 90 days of tender validity (2 + 31 + 30 + 27 = 90). The security was immobilized on 2026-02-21, the start of the period.
- Shares: 250 shares, face value 2 500.00 (10 lume a share), market value 3 100.00 (12.40 a share); both cover the liability of 2 400.00.
- Guarantor is a bank (ISIC 6419), size LARGE with a share capital of 75 million lume; interested party is the tenderer, beneficiary the contracting department; ContractFolderID is the procedure's.

## Considered and refuted
- `/GuaranteeCertificate/cbc:ID`: `BL-DOC-26-0200` while the bank's other identifiers start with `BLUM` — refuted because document numbers and guarantee numbers may come from different numbering ranges.
- `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate`: the period starts three days before the certificate is issued — refuted because the certificate notifies a deposit already made (the immobilization of 2026-02-21).
- `/GuaranteeCertificate/cbc:Note`: "Released at the award." while the period runs to 2026-05-27 — refuted because the period is the latest end and the release at award an earlier one.
- `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount`: in lume although the shares are Urvanian — refuted because the guarantee is in lume and 1 lume = 100 ferra is a fixed reference rate of the world's lists.
- `/GuaranteeCertificate/cac:GuarantorParty/cac:Contact/cbc:JobTitle`: a client relationship manager in trade services — refuted, it fits a bank's guarantee business.

## Outside this review
- No guarantee certificate exists for Brackenmere Furniture, which also tenders (17, 19); whether the flow needs one is a question of its story.
