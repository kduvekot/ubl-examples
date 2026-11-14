# LLM review: 14-GuaranteeCertificate.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: context

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

### tender/14#F1 · Medium · A bank guarantee that is also described as immobilised shares of the tenderer itself
- XPath: `/GuaranteeCertificate/cbc:ConstitutionCode` = `BANKGUAR`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SecurityID` = `XU0001042501`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:SharesNumberQuantity` = `250`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:FaceValueAmount` = `2500.00`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:MarketValueAmount` = `3100.00`
- XPath: `/GuaranteeCertificate/cbc:LiabilityAmount` = `2400.00`
- XPath: `13-TendererQualification.xml:/TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `01-PriorInformationNotice.xml:/PriorInformationNotice/cac:TenderingTerms/cac:RequiredFinancialGuarantee/cbc:Description` = `A bank guarantee for the tender.`
- Why: `ConstitutionCode` is "the code stating the constitution means of the Guarantee": `BANKGUAR`, a bank guarantee, which is what the notices ask for ("A bank guarantee for the tender."). `ImmobilizedSecurity` ("details of an immobilized security") describes another means of constituting a guarantee: securities blocked in favour of the beneficiary. The certificate carries both, without saying how they relate. If the shares are the bank's collateral for its guarantee, they are a matter between bank and customer and do not belong in the certificate for the beneficiary; if they are the guarantee, the constitution code is wrong and the notices' requirement is not met. The security is the tenderer's own ordinary shares (the ISIN is the one of Valdara's security listing in 13): a pledge whose value falls exactly when the tenderer fails. The values are odd as well: `FaceValueAmount` is defined as "the value of the security on the day it was immobilized" (2026-02-21, 2500.00), `MarketValueAmount` as "the current market value" (three days later, 3100.00, +24 %).
- Condition: The certificate describes one means of constitution, the one its code names; immobilised securities appear only when the guarantee is constituted by them.
- Options: (a) Preferred: remove `ImmobilizedSecurity` (a plain bank guarantee, as required). (b) Make it a guarantee by immobilised securities: another constitution code, securities of a third issuer, and notices that allow that means.
- Needs decision: yes

### tender/14#F2 · Medium · The issuer of the immobilisation certificate is the company whose shares are immobilised
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cac:IssuerParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/GuaranteeCertificate/cac:ImmobilizedSecurity/cbc:ImmobilizationCertificateID` = `BLUM-IMM-26-0044`
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:PartyName/cbc:Name` = `Bank of Lumeport`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- Why: `IssuerParty` is "the Party who issues the Immobilized Security Certificate". The certificate number (`BLUM-IMM-26-0044`) follows the numbering of the Bank of Lumeport (as `BLUM-G-…`, `BLUM-SIG-…`), which is the body that can block securities in a custody account and certify it. The element names Valdara Industries, which is the issuer of the shares and the party that deposits the guarantee; a depositor cannot certify its own deposit.
- Condition: `IssuerParty` is the custodian or bank that issued the immobilisation certificate.
- Options: (a) Preferred: Bank of Lumeport (if the aggregate stays at all; see the previous finding). (b) None other seen.
- Needs decision: no

### tender/14#F3 · Medium · A language code in `LocaleCode`
- XPath: `/GuaranteeCertificate/cac:GuarantorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "a code signifying the locale in which this language is used". The value repeats the ISO 639 language code of `Language/ID` (list "ISO 639"); a language is not a locale (a locale would name the country or region whose conventions apply). The element adds nothing to `ID` and carries a meaning other than its definition. The same pattern (an ISO 639 language code in `LocaleCode`) occurs in 213 of the 250 examples (counted with `grep -l LocaleCode world/examples/*/*.xml`).
- Condition: A locale element, where present, identifies a locale (language plus territory, or the territory), from a list of locales; otherwise it is absent.
- Options: (a) Preferred: remove `LocaleCode` where it only repeats the language. (b) Use locale identifiers (e.g. `en-XB`) with a matching list.
- Needs decision: no

### tender/14#F4 · Low · The address of a law text as "ontology" of the regulation
- XPath: `/GuaranteeCertificate/cac:ApplicableRegulation/cbc:OntologyURI` = `https://law.bayvarra.example/ppa#art61`
- XPath: `/GuaranteeCertificate/cac:ApplicableRegulation/cbc:LegalReference` = `XB-PPA-2019 art. 61`
- Why: `OntologyURI` is "the Uniform Resource Identifier (URI) of an ontology related to this regulation", i.e. of a formal vocabulary. The value is the anchor of article 61 in the text of the Act, the same address family the qualification request (06) gives as `Legislation/URI`. A law text is not an ontology.
- Condition: `OntologyURI` identifies an ontology, or is absent; the address of the article is given where the model has a place for it or in the legal reference.
- Options: (a) Preferred: remove it; the legal reference already names the article. (b) None other seen.
- Needs decision: no

### tender/14#F5 · Low · The logistics provider of Valdara Industries, with contract number and key account desk, in a guarantee certificate
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`
- Why: `ServiceProviderParty` is "a party providing a service to this party": Castrano Logistics, which warehouses and despatches for Valdara Industries, with the number of their arrangement and its key account desk. A bank certifying a tender guarantee has nothing to do with the warehouse contractor of its customer. It looks copied from the party's master data into a document that does not use it.
- Condition: The party carries a service provider only in documents in which that provider acts or must be known (despatch, transport, customs).
- Options: (a) Preferred: remove the service provider here. (b) If the provider matters to the buyer, declare it where the document has a place for it (as a subcontractor or in the delivery terms).
- Needs decision: no

### tender/14#F6 · Low · Customs trader numbers of the parties in a guarantee certificate
- XPath: `/GuaranteeCertificate/cac:InterestedParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/GuaranteeCertificate/cac:BeneficiaryParty/cac:AdditionalPartyIdentification/cbc:ID` = `XB-TR-410548`
- Why: The parties are identified also by their customs trader numbers. Nothing in this document is declared to customs; the numbers are used only when the benches cross the border (30, 31). They look copied from the parties' master data into a document that does not use them (section 4.8 of the review method: data the document does nothing with).
- Condition: A party carries the identifiers the document uses or the receiver needs to identify it; no customs trader number in a tendering document.
- Options: (a) Preferred: leave the customs trader numbers to the customs and transport documents. (b) Keep them if the world's rule is that every document carries all identifiers of a party; then that rule should be stated.
- Needs decision: no

## Checked and consistent
- Liability 2400.00 lume, type `TENDER` and the beneficiary agree with `RequiredFinancialGuarantee` of the notices; the certificate is dated 2026-02-24, before the end of the constitution period (2026-02-26).
- Applicable period to 2026-05-27: the tender deadline 2026-02-26 plus the 90 days of tender validity (28 February has 2 days left, March 31, April 30, May 27 → 90).
- The interested party is the tenderer of 15, whose tender (2026-02-25) lists a courier fee "of the guarantee's original".
- ISIN XU0001042501: check digit correct (`check_ids.py`); 250 shares at a face value of 2500.00 is 10.00 per share.

## Considered and refuted
- `/GuaranteeCertificate/cac:ApplicablePeriod/cbc:StartDate` = 2026-02-21, three days before the issue date: suspected date conflict — refuted, the guarantee can be effective from the day it was constituted (the immobilisation is dated 2026-02-21) and certified later.
- `/GuaranteeCertificate/cbc:Note` = "Released at the award." against an end date of 2026-05-27: suspected contradiction — refuted, the period is the latest end and the note the earlier release.
- `/GuaranteeCertificate/cac:GuarantorParty`: the model calls it "the guarantee creditor organisation"; suspected wrong party — refuted, the bank that gives the guarantee is what the element name and the flow mean.
- `/GuaranteeCertificate/cac:GuaranteeDocumentReference/cbc:ID` = `BLUM-G-26-0221` beside the document ID `BL-DOC-26-0200` (two prefixes, BLUM and BL, for one bank): suspected inconsistency as with the sawmill's `HS`/`MS` — refuted as a context problem, the reference is the bank's number of the guarantee instrument and both prefixes abbreviate the bank's name.

## Outside this review
- No guarantee certificate exists in the flow for the other tenderer, Brackenmere Furniture (tenders 17 and 19), although the notices require one from every tenderer. That is a gap of the flow, not of this document.
- The tender of Valdara (15) does not cite this certificate or the guarantee number; noted in 15.
