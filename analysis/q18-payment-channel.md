# Q18: PaymentChannelCode vs PaymentRailID (research notes)

Accessed 2026-11-11 unless stated. Nothing in the repository was changed. Local copies of the downloaded sources are in
a working folder of the research session (not kept; every source is cited by URL below).

## 0. What the examples do today

- 38 generated `cac:PaymentMeans` have `PaymentMeansCode 30` + `PaymentChannelCode IBAN` + a `PaymentRailID`
  (LUMEPAY 13, TRADE-ACCORD-PAY 15, FERRA-RTGS 8, CORAL-NET 2). The 39th `IBAN` is OASIS's own sample
  `xml/UBL-Invoice-2.1-Example.xml` (code 31, account DK1212341234123412, no rail).
- Source of the value: `tools/examples_kit.py` line 188, `"PaymentChannelCode": V("IBAN", "Paid to an account identified in the format of ISO 13616.")`.
- The same accounts already carry `cac:PayeeFinancialAccount/cbc:AccountFormatCode` = `ISO13616` (89 times). So `PaymentChannelCode IBAN` says again what `AccountFormatCode` already says, in the wrong element.
- The world already uses ISO 20022 codes in PaymentMeans: `ChargeBearerCode SHAR` (15 times) and `ServiceLevelCode NURG` (once).

## 1. What UBL says

### 1.1 Definitions (UBL 2.5 CAC XSD with CCTS annotations)
Source: https://docs.oasis-open.org/ubl/os-UBL-2.5/xsd/common/UBL-CommonAggregateComponents-2.5.xsd (local copy `oasis-nr/cac.xsd`).

- `cbc:PaymentChannelCode`, DEN "Payment Means. Payment Channel Code. Code", 0..1:
  > "A code signifying the Payment Channel for this Payment Means."
  Data type `Code. Type` (plain `cbc:CodeType`, **not** a qualified data type).
- `cbc:PaymentRailID`, DEN "Payment Means. Payment Rail_ Identifier. Identifier", 0..1:
  > "An identifier of the Payment Rail or network through which the Payment is executed."
- Its new neighbour `cbc:PaymentPlatformID`:
  > "An identifier of the Payment Platform on which the Payment is executed or received."
- For comparison, `cbc:PaymentMeansCode` uses the qualified type `Payment Means_ Code. Type`: "A code signifying the type of this means of payment."
- Other related elements: `cbc:ChargeBearerCode` ("A code signifying which party or parties will assume the charges and fees associated with the payment using this payment means."), `cbc:ServiceLevelCode` ("A code signifying an agreed service level for the type of payment associated with this payment means."), and `cac:PayeeFinancialAccount/cbc:AccountFormatCode` ("A code signifying the format of this financial account.").
- Order in `PaymentMeansType`: ID, PaymentMeansCode, PaymentMeansDescription, PaymentDueDate, **PaymentChannelCode, PaymentRailID, PaymentPlatformID**, InstructionID, InstructionNote, PaymentID, ChargeBearerCode, ServiceLevelCode, CardAccount, PayerFinancialAccount, PayeeFinancialAccount, CreditAccount, PaymentMandate, TradeFinancing, RemittanceDocumentDistribution, PaymentInstructionAttachment.

PaymentChannelCode is old. In UBL 2.0 (https://docs.oasis-open.org/ubl/os-UBL-2.0/xsd/common/UBL-CommonAggregateComponents-2.0.xsd) its definition was "The Payment Channel, expressed as a code." I did not check UBL 1.0 (its URL returns 404).

### 1.2 When PaymentRailID came in, and why
In the UBL 2.5 spec (https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.html, local `oasis-nr/spec.html`), Table C.1 "Summary changes to Library Elements" lists, under PaymentMeans:
> "PaymentRailID Added PaymentPlatformID Added PaymentInstructionAttachment Added"

So **PaymentRailID is new in UBL 2.5** (together with PaymentPlatformID and FinancialAccount/BlockchainID). The spec gives no reason for each element. The only general reasons are in C.8.1 and C.8.3.2:
> "Key updates include support for collections on behalf of third parties, improved invoice status tracking, waste transport management, and enhanced payment referencing."
> "Several changes related to retail transactions, such as improving tax structures to better express tax inclusive amounts, as well as expansion of payment structure to better support card and cash payments."

**Not verified:** a TC issue or minutes explaining PaymentRailID. A GitHub search of oasis-tcs/ubl (issues, commits, code) found nothing for "PaymentRail"; issues.oasis-open.org only redirects. The spec never mentions PaymentChannelCode or 4435.

### 1.3 Default code list
- UBL 2.5 ships default `.gc` lists for these only: AllowanceChargeReasonCode, BinaryObjectMimeCode, ChannelCode, CountryIdentificationCode, CurrencyCode, LanguageCode, PackagingTypeCode, PaymentMeansCode, TransportEquipmentTypeCode, TransportModeCode, UnitOfMeasureCode (spec, list of `cl/gc/default/*.gc`).
- **There is no default list for PaymentChannelCode or PaymentRailID.** Both use unqualified types. (`ChannelCode` is the *communication* channel list used by `cac:Contact/cac:OtherCommunication`, not payment.)
- UBL's own sample does use `IBAN`. https://docs.oasis-open.org/ubl/os-UBL-2.5/xml/UBL-Invoice-2.1-Example.xml, lines 180-186:
  ```xml
  <cbc:PaymentMeansCode listID="UN/ECE 4461">31</cbc:PaymentMeansCode>
  <cbc:PaymentDueDate>2009-12-31</cbc:PaymentDueDate>
  <cbc:PaymentChannelCode>IBAN</cbc:PaymentChannelCode>
  <cbc:PaymentID>Payref1</cbc:PaymentID>
  <cac:PayeeFinancialAccount><cbc:ID>DK1212341234123412</cbc:ID>
  ```
  This is the Danish OIOUBL practice (see 5.1); the DK account shows where it came from. It is an example, not a rule, and UBL does not bind any list to this element.

## 2. UN/CEFACT: UNCL 4435

Sources: `uncefact/vocabulary-outputs` (local sparse clone, commit 51768f9, 2024-07-29), `_data/paymentmeanschannelcodelist.json` and `_data/paymentmeanschannelpaymentchannelcode.json`. Also `uncefact/spec-JSONschema`, JSONschema2020-12/library/BuyShipPay/D23B (`UNECE-BSPContextCCL.json`, `codelists/UNECE_UNTDID4435.json`), https://github.com/uncefact/spec-JSONschema.

- The UNTDID element: title "Payment channel code", description:
  > "Code specifying the payment channel."
- The CEFACT element that uses it is `paymentMeansChannelPaymentChannelCode` (BSP DEN "Trade Settlement_ Payment Means. Payment Channel. Code"), i.e. CII `ram:SpecifiedTradeSettlementPaymentMeans/ram:PaymentChannelCode` (type `qdt:PaymentMeansChannelCodeType`, listAgencyID fixed to `6`):
  > "The code specifying the payment channel through which this trade settlement payment is to be processed (Reference United Nations Code List (UNCL) 4435)."
  - Code list comment: "A character string used to represent the payment means channel."
  - Domain `unece:PaymentMeans`: "The means by which a payment will be or has been made for trade settlement purposes."
- The codes (D23B):

| Code | Name | Code | Name |
|---|---|---|---|
| 1 | Ordinary post | 9 | Personal (face-to-face) |
| 2 | Air mail | 10 | Registered air mail |
| 3 | Telegraph | 11 | Registered mail |
| 4 | Telex | 12 | Courier |
| 5 | S.W.I.F.T. | 13 | Messenger |
| 6 | Other transmission networks | 14 | National ACH |
| 7 | Networks not defined | 15 | Other ACH |
| 8 | Fedwire | ZZZ | Mutually defined |

- In UN/EDIFACT, 4435 sits next to 4461 (payment means) in composite C534 of the PAI (payment instructions) segment. **Not verified here**, because unece.org is blocked. A third-party EDIFACT mirror confirms the same name, description and codes.
- I could not get the descriptions of each code (the UNTDID HTML is blocked). The JSON sources carry names only.
- What this means: 4435 mixes ways of **sending** the payment or instruction (post, air mail, telex, courier, face to face) with a few **networks and rails** (SWIFT, Fedwire, ACH). It has **no code for an RTGS** apart from the US-specific Fedwire, so FERRA-RTGS could only be `6` or `ZZZ`.

## 3. EN 16931 / Peppol

### 3.1 EN 16931: explicitly not used
CEN/TC 434 validation artefacts, https://github.com/ConnectingEurope/eInvoicing-EN16931:
- `ubl/schematron/abstract/EN16931-syntax.sch`, line 449:
  > `[UBL-CR-413]-A UBL invoice should not include the PaymentMeans PaymentChannelCode` (flag="warning")
  The test in `ubl/schematron/UBL/EN16931-UBL-syntax.sch` line 500 is `not(cac:PaymentMeans/cbc:PaymentChannelCode)`.
- `cii/schematron/abstract/EN16931-CII-syntax.sch`, line 466:
  > `[CII-SR-369] - PaymentChannelCode should not be present` (warning); the test is `not(ram:SpecifiedTradeSettlementPaymentMeans/ram:PaymentChannelCode)`.

No business term in EN 16931 maps to the payment channel. BG-16 has BT-81 means code (UNCL 4461), BT-82 means text, BT-83 remittance information, BG-17/18/19 (account, card, mandate).

### 3.2 Peppol BIS Billing 3.0 and PINT
- https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentMeans/ ("May 2026 Release") lists as children only PaymentMeansCode, PaymentID, CardAccount, PayeeFinancialAccount and PaymentMandate. **PaymentChannelCode is absent.** The CEN UBL-CR-413 warning applies, since BIS 3 runs the CEN schematron.
- BT-84 `PayeeFinancialAccount/cbc:ID` (https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/cac-PaymentMeans/cac-PayeeFinancialAccount/cbc-ID/):
  > "A unique identifier of the financial payment account, at a payment service provider, to which payment should be made. Such as IBAN or BBAN."

  So in BIS 3, IBAN/BBAN is a property of the account ID, not of the channel.
- Peppol PINT 1.1.3 (https://docs.peppol.eu/poac/pint/pint/trn-invoice/syntax/cac-PaymentMeans/) and JP PINT (https://docs.peppol.eu/poac/jp/pint-jp/trn-invoice/syntax/cac-PaymentMeans/) have the same set: ID, PaymentMeansCode, PaymentID, CardAccount, PayeeFinancialAccount, PaymentMandate. **No PaymentChannelCode.**

### 3.3 Older Peppol / BII (v1/v2)
- CEN BII2 core for Peppol BIS 4A/5A v2.0 already left it out. https://github.com/OpenPeppol/peppol-bis, `rules/peppolbis-trdm010-2.0-invoice/Schematron/BII CORE/BIICORE-UBL-T10.sch`, line 5250:
  > `<rule context="/p1:Invoice/cac:PaymentMeans/cbc:PaymentChannelCode"> <report flag="warning" test=".">Element 'cbc:PaymentChannelCode' is marked as not used in the given context.</report>`
- Yet BIS v2-era national profiles and samples filled it with account schemes:
  - Norway EHF post-award g2, https://github.com/anskaffelser/ehf-postaward-g2, `structure/syntax/invoice.xml`: `cbc:PaymentChannelCode`, "Payment channel code", "Code for paymentchannel, IBAN, BBAN". The EHF T10 schematron (2019-06) lists it as an allowed context with no assertions.
  - Pagero BIS 5A 2.0 samples (https://github.com/pagero/integration-resources, `example-files/invoice-creditnote/Peppol BIS 5A 2.0/Invoice_1_Tax.xml`, lines 90/104): `BBAN`, `IBAN`.
  - OpenPeppol's own BIS 2 test `rules/peppolbis-trdm010-2.0-invoice/Tests/T10-0009-FullSpecINV.xml`, lines 400/418: `SE:Bankgiro`, `SE:Plusgiro`.
  - Italian national rules on BIS 2 (https://github.com/Intercent-ER/AGID-PEPPOL-DOCS, `artifacts/validation/2.0/xsl/ITNAT-UBL-T10.xsl`, lines 3265/3397): contexts `cac:PaymentMeans[not(cbc:PaymentChannelCode) or cbc:PaymentChannelCode='IBAN']/…/cbc:ID[@schemeID='IBAN']` and `…='LOCAL'`.

  In all of these, the channel code just repeats the account `schemeID` (IBAN/BBAN/LOCAL).
- Why it was dropped: **no official statement found.** The evidence suggests it had no defined code list and no business term behind it. Profiles used it for the account identification scheme, which `FinancialAccount/ID@schemeID` (BIS 2) and BT-84 (EN 16931) already carry. CEN BII2 marked it "not used", and EN 16931 kept it out with UBL-CR-413. This is an inference, not a quoted rationale.
- I did not find the original Peppol BIS 4A/5A **v1** guide text on PaymentChannelCode (docs.peppol.eu has no BIS 2.0 pages; `/poacc/billing/2.0/` returns 404).

## 4. ISO 20022 (the payments authority)

Reach: iso20022.org and swift.com return 403, and the guessed XLSX URL returns 404. I used:
- (a) a GitHub mirror of the official **2Q2024 ExternalCodeSets JSON**: https://github.com/marcialwushu/ISO.20022.Messages, `AdditionalContent/External code sets/ExternalCodeSets_JSON/2Q2024_ExternalCodeSets_v1.json`. This is a third-party copy; newer quarters are not verified.
- (b) official message XSDs mirrored on GitHub, e.g. `pacs.008.001.13.xsd` ("Generated by Standards Editor on 2025 Feb 17") at https://github.com/phoughton/pyiso20022.
- (c) the ISO 20022 e-Repository definitions as generated by https://github.com/tools20022/tools20022-api-payments and https://github.com/prowide/prowide-iso20022.

ISO 20022 has **no element called "payment channel"**. It has these concepts:

| ISO 20022 element (pacs.008 / pain.001) | Code set | Definition (quoted) | Matches |
|---|---|---|---|
| PaymentTypeInformation/**ClrChanl** (ClearingChannel) | **ClearingChannel2Code** (closed ISO code set): RTGS, RTNS, MPNS, BOOK | "Specifies the clearing channel to be used to process the payment instruction." Codes: RTGS "Clearing channel is a real-time gross settlement system.", RTNS "Clearing channel is a real-time net settlement system.", MPNS "Clearing channel is a mass payment net settlement system.", BOOK "Payment through internal book transfer." Code set: "Specifies the clearing channel for the routing of the transaction, as part of the payment type identification." | **channel = kind of rail** |
| SettlementInformation/**ClrSys** (ClearingSystemIdentification3Choice: Cd or Prtry) | **ExternalCashClearingSystem1Code** (130 codes in 2Q2024: TGT "Target.", FDW "US … Federal Reserve Banks Fedwire Funds Service.", FDN FedNow, FPS "Faster Payments Service in UK.", STG CHAPS, CHI CHIPS, ZEN Zengin, UPI, ACH "Automated Clearing House. Payment system that clears cash transfers and settles the proceeds in a lump sum, usually on a multilateral netting basis.", …) | ClrSys: "Specification of a pre-agreed offering between clearing agents or the channel through which the payment instruction is processed." Cd: "Infrastructure through which the payment instruction is processed, as published in an external clearing system identification code list." Prtry: "Clearing system identification in a proprietary form." | **rail** (= PaymentRailID) |
| ClearingSystemMemberIdentification/ClrSysId | ExternalClearingSystemIdentification1Code (USABA, DEBLZ, GBDSC …) | "Specifies the clearing system identification code …". The codes are bank or branch *code schemes*, e.g. "USABA - Routing Transit number assigned by the ABA for US financial institutons" | bank-code scheme (≈ FinancialInstitution ID schemeID), not a rail |
| PaymentTypeInformation/SvcLvl | ExternalServiceLevel1Code (SEPA, URGP, NURG, INST, SDVA …) | "Specifies a pre-agreed service or level of service between the parties …". URGP: "Payment must be executed as an urgent transaction cleared through a real-time gross settlement system …" | = UBL ServiceLevelCode (already used, NURG) |
| PaymentTypeInformation/LclInstrm | ExternalLocalInstrument1Code | "User community specific instrument. Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the service or service level." | scheme-specific instrument |
| Account Id: IBAN or Othr/SchmeNm | IBAN2007Identifier; ExternalAccountIdentification1Code (AIIN, **BBAN**, CUID, UPIC) | IBAN: "International Bank Account Number (IBAN) - identifier used internationally by financial institutions to uniquely identify the account of a customer. …ISO 13616…" | **account format**: where "IBAN" belongs (UBL AccountFormatCode / account ID schemeID) |
| (outside payments) | ExternalChannel1Code (COUR, EMAL, FAXI, MESS, POST, REGM, SEMA, SWFA, SWIA, SWMT, SWMX, TELE, WEBM) | "Specifies the external submission or presentation channel code …" | close to the *transmission* half of UNCL 4435 (post, courier, messenger, registered mail, SWIFT). I did not check which message element uses it. |

So ISO 20022 itself calls a clearing system "the channel through which the payment instruction is processed". It splits:
- the **kind** of channel, `ClearingChannel2Code`;
- the **specific system**, `ExternalCashClearingSystem1Code` or a proprietary ID, which is PaymentRailID;
- the **service level**, `ExternalServiceLevel1Code`;
- the **account format** (IBAN/BBAN).

## 5. Other practice

### 5.1 OIOUBL (Denmark): the main real-world user
- OIOUBL 2.x code list `urn:oioubl:codelist:paymentchannelcode-1.1` (agency 320). Values from the OIOUBL codelist schematron, mirrored at https://github.com/yosuanicolaus/schematron-test, `validation/schematron/OIOUBL_Codelist_Schematron.xml`, line 120:
  > `BBAN, DK:BANK, DK:FIK, DK:GIRO, DK:NEMKONTO, FI:BANK, FI:GIRO, GB:BACS, GB:BANK, GB:GIRO, IBAN, IS:BANK, IS:GIRO, IS:IK66, IS:RB, NO:BANK, SE:BANKGIRO, SE:PLUSGIRO, SWIFTUS, ZZZ`

  This list mixes account formats (IBAN, BBAN) with national payment systems (GB:BACS, DK:FIK, SE:BANKGIRO, DK:NEMKONTO).
- OIOUBL 3 rules (`common-OIOUBL-billing-PaymentMeans.sch` v3.2.4, mirrored at https://github.com/alexcatdad/eu-einvoice-canonical, `validation/bundles/oioubl3-invoice-3.2.4/source/_common/Schematron/sch/`):
  - OIOUBL-BIL-120: "When PaymentMeansCode is = 31, then PaymentChannelCode is mandatory"
  - OIOUBL-BIL-121: "When PaymentMeansCode = 31, then PaymentChannelCode should be either 'IBAN' or 'ZZZ'"
  - OIOUBL-BIL-113: "If PaymentChannelCode is present, its value must be 'DK:BANK' when PaymentMeansCode is '42'"
  - OIOUBL-BIL-124/125: "PaymentChannelCode is not allow when the PaymentMeans = 1" / "= 10".
- BIS 3 → OIOUBL converters invent the value. NemHandel/delis `BIS-Billing-INV_2_OIOUBL_INV.xslt` (https://github.com/dladlk/delis, `delis-resources/transformation/cius/2021-11-03_v1.8.0/BIS3_2_OIOUBL/`) sets `'IBAN'`, `ZZZ` or `DK:BANK` with `listID="urn:oioubl:codelist:paymentchannelcode-1.1"`, because BIS 3 has nothing to map from.
- Not verified: the OIOUBL code list's own HTML page (oioubl.info redirects to oioubl21.oioubl.dk, which is blocked here).

### 5.2 XRechnung, ZUGFeRD / Factur-X (CII)
These are CIUS or extensions of EN 16931. The CEN rules UBL-CR-413 / CII-SR-369 (warnings) apply. XRechnung has no business term for it. **Not verified:** XRechnung or ZUGFeRD extension-profile texts (xoev.de is blocked). GitHub copies of the Factur-X schematron contain the same CII-SR-369 rule (e.g. stephanstapel/ZUGFeRD-csharp, `documentation/zugferd22de/Schema/BASIC-WL/Schematron/FACTUR-X_BASIC-WL.sch`, from the search hit only).

### 5.3 Japan PINT
No PaymentChannelCode (see 3.2).

### 5.4 ERP practice
Microsoft Business Central's Peppol export (https://github.com/microsoft/BCApps, `src/Layers/W1/BaseApp/Sales/Peppol/PEPPOLManagement.Codeunit.al`, line 877) sets `PaymentChannelCode := '';`. It puts IBAN in `PaymentMeansSchemeID := IBANPaymentSchemeIDTxt` ('IBAN'), the account's schemeID.

## 6. Means vs channel vs rail

- **Means (UNCL 4461, `PaymentMeansCode`)**: *what kind of payment instrument*. Examples: 10 cash, 20 cheque, 30 credit transfer, 31 debit transfer, 42 payment to bank account, 48/54/55 cards, 49 direct debit, 58 SEPA credit transfer. It says how the debt is settled, not which system carries it.
- **Channel (UNCL 4435, `PaymentChannelCode`)**: *by what route the payment or instruction travels*. In 4435 this is mostly a physical or transmission route (post, courier, telex, SWIFT, face to face), plus three rail categories or instances (Fedwire, national ACH, other ACH). The closest modern meaning is ISO 20022 **ClearingChannel**: the *kind* of clearing (RTGS, real-time net, mass-payment net, book transfer).
- **Rail (`PaymentRailID`, new in 2.5)**: *the specific system or network* that executes the payment, e.g. TARGET2, Fedwire, FPS, or the world's FERRA-RTGS, LUMEPAY, CORAL-NET and TRADE-ACCORD-PAY. ISO 20022 equivalent: ClearingSystemIdentification (`ExternalCashClearingSystem1Code` or proprietary).
- **Account format (IBAN)** is none of these. It is `FinancialAccount/AccountFormatCode` (already `ISO13616` in the examples) or the account ID's schemeID.

**Do they overlap?** Yes, partly:
- 4435 codes 5, 8, 14 and 15 name or classify networks, so with PaymentRailID present they either repeat it (Fedwire) or only add a coarse class ("National ACH").
- The transmission codes (post, courier, telex) have no meaning for an electronic credit transfer to an account.
- With ISO ClearingChannel2Code the overlap is cleaner: channel = *class* of the rail (RTGS / RTNS / MPNS / BOOK), rail = *instance*. It still partly overlaps `ServiceLevelCode` (URGP/NURG already imply RTGS vs ACH).
- Before UBL 2.5, PaymentChannelCode was the only place to name a system, which is why OIOUBL put `GB:BACS` and `SE:BANKGIRO` in it. In 2.5 that job belongs to PaymentRailID.

## 7. Recommendation

Test against the "Not everything UN/EDIFACT" rule for UNCL 4435:
- UBL ships no list for it.
- Established practice (EN 16931, Peppol BIS 3, PINT) explicitly does *not* use it. Only CII names 4435 in its definition, and EN 16931 removes it from CII too.
- It is not the best authority for payments: ISO 20022 is, and the world already uses ISO 20022 for ChargeBearerCode and ServiceLevelCode.
- It also cannot classify FERRA-RTGS (no RTGS code) or a tokenised-deposit ledger.

So UNCL 4435 fails all three tests.

Options:

1. **(Recommended) Leave PaymentChannelCode out** of the generated credit transfers. PaymentRailID names the system, AccountFormatCode `ISO13616` says IBAN, ServiceLevelCode/ChargeBearerCode cover the rest. This matches EN 16931, Peppol BIS 3, PINT and Business Central. Fix: drop line 188 of `tools/examples_kit.py`, and mention in the note that the rail is in PaymentRailID. Leave OASIS's own `UBL-Invoice-2.1-Example.xml` unchanged; it is upstream and reflects OIOUBL practice.
2. **(Good alternative, if element coverage matters) ISO 20022 ClearingChannel2Code** in PaymentChannelCode, consistent with the rail, `listID="ISO 20022 ClearingChannel2Code"` (Q4 style). It is the payments authority's own "clearing channel", and the definitions match: UBL "Payment Channel for this Payment Means", CII "payment channel through which this trade settlement payment is to be processed", ISO "clearing channel to be used to process the payment instruction". Suggested pairing (check against the world's descriptions):
   - FERRA-RTGS → `RTGS`
   - LUMEPAY (domestic clearing): `MPNS` if batch/ACH-like, `RTNS` if instant with net settlement
   - TRADE-ACCORD-PAY: by its design, `RTNS` or `RTGS`
   - CORAL-NET (tokenised-deposit ledger): gross and real time, so `RTGS`. `BOOK` only if both accounts sit on one institution's books.

   Keep ServiceLevelCode consistent with it (URGP with RTGS, NURG with MPNS). Caveat: ClearingChannel2Code is a small closed ISO code set inside the message schema, not a published "external code set". Give the name and version (ClearingChannel2Code) exactly.
3. **Regional Trade Accord list** (`urn:ubl-examples:world:codelist:PaymentChannelCode`), OIOUBL style. Not recommended: it would duplicate PaymentRailID, just as OIOUBL's list does for national systems.
4. **UNCL 4435** (`listID="UN/EDIFACT EDED 4435"`, e.g. 14 for LUMEPAY, 15 or 6 for TRADE-ACCORD-PAY, 6 for FERRA-RTGS and CORAL-NET). Not recommended for the reasons above; acceptable only for a deliberately CII-aligned example.

Separately for PaymentRailID: there is no UBL list. The real-world analogue is ISO 20022 `ExternalCashClearingSystem1Code` (3-letter codes, with a proprietary option for others). The world's fictional rails fit a world list, e.g. `schemeID="urn:ubl-examples:world:codelist:PaymentRail"` or the Q4 pattern, with the list defined from `countries.json` `payment.system`. I did not check whether PaymentRailID currently carries a schemeID; the examples show none.

## 8. Not verified / not reached
- unece.org (UNTDID 4435 HTML with code descriptions, EDIFACT PAI/C534 structure): 403. I used the UN/CEFACT GitHub repos and one third-party mirror instead.
- iso20022.org and swift.com: 403. I used a third-party GitHub mirror of the official 2Q2024 ExternalCodeSets JSON, plus generated e-Repository code (tools20022, prowide). Codes added after 2Q2024 are unknown.
- I found no UBL TC rationale for PaymentRailID or PaymentPlatformID beyond the 2.5 spec summary.
- I found no official Peppol or CEN BII statement on why PaymentChannelCode was dropped; the reason given in 3.3 is my inference.
- The oioubl.info codelist page, the xoev.de XRechnung spec and Peppol BIS v1 documents were not reachable or not found.
