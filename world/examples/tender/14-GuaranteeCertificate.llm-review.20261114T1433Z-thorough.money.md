# LLM review: 14-GuaranteeCertificate.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

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

### tender/14#F1 · Medium · "Face value" and market value of the immobilised shares: a rise of 24 % in three days, or a nominal value in an element defined otherwise
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` = `2500.00`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:MarketValueAmount` = `3100.00`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:IssueDate` = `2026-02-21`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `250`
- Why: UBL defines `FaceValueAmount` as "The value of the security on the day it was immobilized" and `MarketValueAmount` as "The current market value of the immobilized security." The shares were immobilised on 2026-02-21 and the certificate is issued on 2026-02-24. Read by the definitions, 250 shares were worth 2500.00 lume (10 a share) on the 21st and 3100.00 (12.40 a share) three days later, a rise of 24 % of a listed industrial company's shares over a weekend (21 February 2026 is a Saturday). If instead 2500.00 is the nominal value of the shares (10 lume each), the element is used with the meaning of its name and against its definition, which the agreed rule on semantic conformance does not allow.
- Condition: `FaceValueAmount` is the value on the day of immobilisation and is plausible next to the current market value (equal or close to it), or the nominal value is not carried in this element.
- Options: (a, preferred) value on the day of immobilisation close to the market value (for example 3075.00 and 3100.00); (b) one value only, the market value at the date of the certificate.
- Needs decision: no

### tender/14#F2 · Medium · The issuer of the immobilisation certificate is given as the company whose shares are immobilised
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- Why: `IssuerParty` is "The Party who issues the Immobilized Security Certificate", that is the bank or depository that blocks the securities and certifies it, not the issuer of the security. The certificate's number carries the prefix of the Bank of Lumeport's own documents (compare `/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221`), so the bank issued it. Valdara Industries is the issuer of the shares (the ISIN is that of its ordinary shares) and the party that deposits the guarantee; it cannot certify the blocking of its own deposit.
- Condition: `IssuerParty` is the party that issued certificate BLUM-IMM-26-0044.
- Options: (a, preferred) the Bank of Lumeport, or the depository that holds the shares if the story has one; (b) none seen with Valdara.
- Needs decision: no

### tender/14#F3 · Low · A bank guarantee and, with it, the tenderer's own shares immobilised
- XPath: `/GuaranteeCertificate/cbc:ConstitutionCode` = `BANKGUAR`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SecurityID` = `XU0001042501`
- XPath: `/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`
- Why: the constitution code says the guarantee is constituted as a bank guarantee: the bank's undertaking to pay 2400.00 lume is the security the beneficiary holds. Immobilised securities are another way of constituting a guarantee (the securities themselves are blocked in favour of the beneficiary). The certificate states both without saying how they relate. If the shares are the bank's collateral for issuing the guarantee, that is a matter between the bank and its client and has no place in a certificate for the beneficiary; if they are the guarantee, the constitution code is wrong. In addition the shares are the tenderer's own (issuer and depositor are the same company), an unusual thing to pledge for a liability of 2400.00 lume by a company with a capital of 250 million ferra (XUF).
- Condition: the certificate shows one means of constitution, and the constitution code names it; immobilised securities appear only if they are the guarantee held for the beneficiary.
- Options: (a, preferred) a plain bank guarantee without `ImmobilizedSecurity`; (b) a guarantee by immobilised securities, with a constitution code for that, securities of a third issuer (for example government bonds), and the tendering terms' description ("A bank guarantee for the tender.") adjusted or the difference explained.
- Needs decision: yes

### tender/14#F4 · Low · "Released at the award", although a tender guarantee secures the winner's entry into the contract
- XPath: `/GuaranteeCertificate/cbc:Note` = `Released at the award.`
- XPath: `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:EndDate` = `2026-05-27`
- Why: the guarantee is the one the tendering terms require, defined in UBL as "A financial guarantee of a tenderer or bid submitter's actual entry into a contract in the event that it is the successful bidder." For the successful tenderer it must therefore last beyond the award (2026-03-09 in this flow) until the contract is concluded and the performance guarantee is in place (`22-AwardedNotification.xml:/AwardedNotification/cac:FinalFinancialGuarantee/cac:ConstitutionPeriod/cbc:EndDate` = `2026-03-19`); released at the award, it would secure nothing in the ten days in which the winner could still walk away. The note also sits oddly with the period, which runs to the end of the tender's validity.
- Condition: the note on the release agrees with the purpose of a tender guarantee and with the applicable period.
- Options: (a, preferred) "Released to unsuccessful tenderers at the award and to the successful tenderer when the contract is signed and the performance guarantee is constituted"; (b) drop the note.
- Needs decision: no

## Checked and consistent
- Liability 2400.00 lume, type TENDER: as required in the tendering terms (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:LiabilityAmount` = `2400.00`); constituted (2026-02-21, certificate 2026-02-24) before the end of the constitution period, 2026-02-26.
- Applicable period to 2026-05-27: the tender deadline 2026-02-26 plus the tender validity of 90 days (2 days in February, 31 in March, 30 in April, 27 in May).
- Market value of the shares (3100.00) covers the liability (2400.00) 1.29 times.
- `check_ids.py`: the ISIN XU0001042501 has a correct check digit; it is the security listed for Valdara Industries in the party's legal entity. The prefix XU lies in the user-assigned range of ISO 3166 (XA–XZ), so the ISIN cannot be a real one.
- Guarantor: a bank (ISIC 6419) in Lumeport, the beneficiary's town; beneficiary and interested party are the contracting authority and the tenderer of example 15.

## Considered and refuted
- `/GuaranteeCertificate/cbc:LiabilityAmount`: suspected a conflict with the 2 % rate of the tendering terms — refuted for this example: the certificate states no rate and repeats the amount the terms require; the mismatch of rate and amount lies in examples 01–03 and is raised there.
- `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:MarketValueAmount`: suspected a currency problem, since the shares are listed in Urvania and the company's capital is in ferra — refuted because a certificate for a liability in lume reasonably values the collateral in lume.
