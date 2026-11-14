# LLM review: 14-GuaranteeCertificate.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/14-GuaranteeCertificate.xml`, Git blob `f5253d8d365d2d86594564ab6fe3042c7ef3e212` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/14#F1 · Medium · The immobilisation certificate carries the bank's number, but its issuer is said to be the tenderer
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SecurityID` = `XU0001042501`
- Why: `IssuerParty` is "the Party who issues the Immobilized Security Certificate", and `ImmobilizationCertificateID` is "an identifier for the certificate of this immobilized security". The certificate number has the prefix the Bank of Lumeport uses for its own numbers in this document (`/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`, signature `BLUM-SIG-GC`), which says the bank (the custodian that blocks the shares) issued it. The party named as issuer is Valdara, which is the issuer of the shares (the ISIN is Valdara's own, as its party data in 03, 12, 13 and 15 show) and the party that deposits the guarantee, not the issuer of a certificate about their immobilisation. Identifier and party contradict each other on who issued the certificate.
- Condition: `IssuerParty` is the party that issued the immobilisation certificate, and the certificate ID is in that party's number series.
- Options: (a) name the Bank of Lumeport as `IssuerParty` (preferred); (b) if Valdara's share register issued the certificate, give it a Valdara number.
- Needs decision: no

### tender/14#F2 · Medium · "Bank guarantee" as constitution means, with immobilised shares described as well
- XPath: `/GuaranteeCertificate/cbc:ConstitutionCode` = `BANKGUAR`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- Why: `ConstitutionCode` is "the code stating the constitution means of the Guarantee"; the value means a bank guarantee, i.e. the bank's own undertaking to pay (the guarantor is the bank, and the tendering terms ask for "a bank guarantee for the tender"). `ImmobilizedSecurity` describes the other means UBL foresees: securities blocked in favour of the beneficiary. The document does not say how the two relate. If the shares are the bank's collateral for issuing the guarantee, they concern only bank and client and do not belong in the certificate given to the department; if the guarantee is constituted by the shares, the code is wrong. Own knowledge of guarantee practice.
- Condition: the constitution code and the content describe the same means of constitution, or the document states the relation between them.
- Options: (a) remove `ImmobilizedSecurity` and keep the bank guarantee (preferred: it matches the tendering terms); (b) keep the shares and use a code for immobilised securities; (c) keep both and state in `Purpose` or `Note` that the shares are counter-security.
- Needs decision: yes

### tender/14#F3 · Medium · Language code in LocaleCode
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used", i.e. the regional variant, not the language. The value is the ISO 639 language code again (`listID` "ISO 639"), which the sibling `cbc:ID` of the same `Language` already carries. `LocaleCode` occurs in all 36 examples of the flow (`grep -c LocaleCode tender/*.xml`).
- Condition: `LocaleCode` holds a locale from a list of locales, or is absent.
- Options: (a) remove `LocaleCode` (preferred: the examples state no regional variant); (b) fill it with a country or locale code.
- Needs decision: no

### tender/14#F4 · Low · The guarantee takes effect three days before the certificate is issued and four before the tender it secures
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = `2026-02-21`
- XPath: `/GuaranteeCertificate/cbc:IssueDate` = `2026-02-24`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:IssueDate` = `2026-02-21`
- Why: `ApplicablePeriod` is "the specified period in the tendering process for which this Guarantee is effective". It starts on 2026-02-21, the day the shares were immobilised, three days before the bank issues the certificate and four days before the tender exists (`15-Tender.xml:/Tender/cbc:IssueDate` = `2026-02-25`). A tender guarantee secures the tender from its submission (at the latest from the deadline, 2026-02-26) for the tender's validity; before that there is nothing it could be called for. The end date is right (see below). In addition `ImmobilizedSecurity/IssueDate` is "the date on which this immobilized security was issued"; the shares of a company 41 years in operation (13) were hardly issued on 2026-02-21, so the date is that of the immobilisation, not of the security.
- Condition: the guarantee's period does not start before the guarantee is issued (or the earlier start is explained), and the security's issue date is the date its definition asks for.
- Options: (a) start the period on the issue date or on the tender deadline (preferred); (b) keep 2026-02-21 and state that the guarantee was agreed that day; for the security, give the shares' issue date or leave the element out.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: ISIN `XU0001042501` (as `SecurityID` and in the interested party's data) has a correct check digit; scheme "ISO 6166" is the ISIN standard.
- `ApplicablePeriod/EndDate` 2026-05-27 = tender deadline 2026-02-26 + 90 days (2 days of February + 31 + 30 + 27), the tender validity period of the tendering terms and of the tender 15.
- Issued 2026-02-24 08:23, before the constitution deadline (`ConstitutionPeriod/EndDate` 2026-02-26 in 01 to 03) and before the tender (2026-02-25 09:13), whose fee line mentions the courier for the guarantee's original.
- `GuaranteeTypeCode` TENDER and `LiabilityAmount` 2400.00 XBL equal the required financial guarantee of the tendering terms.
- `ContractFolderID` `PWD-2026-PARKS`; guarantor Bank of Lumeport, interested party Valdara (identifiers as in 13 and 15), beneficiary the department.
- `LegalReference` "XB-PPA-2019 art. 61" names the procurement act of the notices.
- Shares: 250 E21 (share, Rec. 20); face value 2500.00 / 250 = 10.00 per share; market value 3100.00 covers the liability of 2400.00.

## Considered and refuted
- `/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID`: `BLUM-G-26-0221` resolves to no example — refuted because it is the bank's guarantee instrument (the element is "a reference to a legal document"), not a UBL document of the flow; the element name says what it is.
- `/GuaranteeCertificate/cbc:ID`: prefix `BL-` although the bank's other numbers begin with `BLUM-` — refuted, the document numbers of all parties follow the pattern `<abbreviation>-DOC-26-nnnn` and may be a separate series.
- `/GuaranteeCertificate/cbc:Note`: "Released at the award" against an end date of 2026-05-27 — refuted, the period is the latest end, the note the earlier release event.
- `/GuaranteeCertificate/cbc:ContractFolderID`: the certificate does not name the tender it secures — refuted because the tender does not exist yet on 2026-02-24; folder, interested party and beneficiary identify the purpose.
