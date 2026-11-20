# Read-through: flows `tender`, `contest`, `medicines`, `lpg` (O112/O248), 2026-11-20

Sources read:
- `note/src/03-world.md`: tax and customs (Bayvarra's sales tax, the withholding, medicines), prices, money, the design contest, dangerous goods by road (propane), the island's hospital.
- `world/documents.json`: the four flows (texts, legs, collaborations, cited entries) and their documents 1–40 (tender), 1–18 (contest), 1–14 (medicines), 1–4 (lpg).
- `world/parties.json`:
  - tender and contest: 2-xb, 5-xu, 8-xu, 13-xu, 21-xb, 25-xb, 27-xb, 28-xb, 36-xb, 37-xb, 48-xb;
  - medicines: 10-xb, 12-xl, 17-xb, 17-xl, 3-xl, 49-xb, 50-xl, and `abroad` 51-nl and 58-in;
  - lpg: 34-xb, 42-xb, 52-xb;
  - for each: identity, week, contact hours, desks, fleet and wiki.
- `world/items.json`: bench-serra, propane, the vaccines, the insulin and the generator.
- `world/countries.json`: XB tax (STT rates, exemption codes, duty-free medicines, withholding).
- `world/fx-fixings.json`.
- `analysis/worklist-decisions.md`: D28, D29, D47, D48, the calendar story line, the story lines for tender and contest, and O78, O97, O102, O176, O195, O201–O204, O222, O226–O234, O248.
- Every XML and `.md` of the four flows (no `*.llm-review.*`), and the generator lines in `tools/examples_scenarios.py` cited below.

The known and already decided points (O97: the withholding statement in the call and the tenders' E/PUBLIC subtotal; O78: offsets on event times) are not repeated as mismatches.

---

## tender (39 documents)

### What checks out

- **Arithmetic.**
  - Tenders:
    - Valdara: 240 × 499 = 119,760, plus 240 × 18 = 4,320, total 124,080.
    - Brackenmere's first tender: 240 × 470 + 240 × 16 = 116,640.
    - Brackenmere's corrected tender: 240 × 480 + 3,840 = 119,040.
    - After the auction: 240 × 489 = 117,360 (LowerTenderAmount).
  - Guarantees:
    - tender guarantee 2,500 (2.0 % of 124,800);
    - performance guarantee 6,204 (5 % of 124,080).
  - Turnover criterion: 124,800, twice 62,400.
  - Subcontract share: 4,320 (3.5 %).
  - Order: 40 × 499 + 40 × 18 = 20,680. Colour charge 40 × 5 = 200. Order response total 20,880.
  - Bench invoice: 20,160 lume = 2,016,000 ferra, at the fixed 100. The export and import values are 20,160 and 2,016,000.
  - Credit note: 499 + 5 = 504.
  - Installation invoice: 39 × 18 = 702, withholding 70.20, payable 631.80.
  - Reminder: 20,287.80 × 8 % × 7/365 = 31.13.
  - Remittance: debits 20,822.93, credits 511.02 (504 + 7.02), paid 20,311.91. The penalty is 2 days × 0.5 % × 702 = 7.02.
- **Calendar.** Every date D28 lists is in the XML on its weekday:
  - the procedure: 12 and 26 Jan (Mon), 27 Jan (Tue), deadline 25 Feb (Wed), opening 26 Feb (Thu), award 9 Mar, standstill 10–19 Mar, contract 20 Mar (Fri), award notice and catalogue 23 Mar;
  - the call-off: order 24 Mar, change 25 Mar, response 26 Mar, delivery 31 Mar;
  - after delivery: acceptance 13 Apr (Lumeport works), credit and installation invoice 14 Apr, due 13 May, reminder 20 May, remittance 22 May.
  - Lot VI-LOT-260327 is made 27 Mar, despatched 30 Mar, and its frames are VI-SF-01611 to 01690.
  - No document of an office party falls on a weekend or on its own holiday.
- **Valdara's figures** follow `parties.json`, as O197 overtook D28 point 4:
  - 63 full years on 24 Feb (founded 12 Apr 1962);
  - 3,083 persons;
  - a turnover of 520 million lume (52 billion ferra).
- **Other figures.**
  - The sawmill: 22 years and 85 persons.
  - Brackenmere: 26 years and 45 persons.
- **References.** All cited IDs exist and match:
  - procedure documents: PWD/2026/0080, 0174, 0182, 0195, 0348, 0373, 0463, 0567, 0571, 0702;
  - tenders and guarantees: 26-0006/07/08/10, 2500002145, 2600002145, 3900039381, 3900039355;
  - call-off: 6100000217, CAS-DA-26-1459, 7600008692;
  - billing: 2026/1529, 1768, 1769, 9300004430.
  - Valdara's invoice numbers 2026/1409 (road), 1529, 1768, 1769 and 1770 (rail) rise in order of issue.
- **Payment references.** RF9720261529 and RF4620261768 are valid. ISIN XB0000260313 has a valid check digit.
- **Tax treatment.**
  - The benches are G/EXP (Urvania).
  - The installation is O/SVCABROAD with Bayvarra's 10 % withholding.
  - Valdara's VAT is in ferra; the payment is in lume to the Bank of Lumeport account (O226).
- **Leg and parties.**
  - The leg 8-xu → 2-xb is carried by 13-xu (Trasvia): its truck is named in the despatch advice and the export declaration.
  - The cargo is 2,162 kg, well within the truck's payload.
  - DAP; the buyer clears the import.
- **Published text.** No decision or open-point numbers, no EU, Peppol or EN 16931, and no person names in the wiki texts. The finding IDs are an exception: see 1.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | tender/01, 02, 03, 21 .md ("(08#F6)"); 15, 17, 19 .md ("(17#F1, 19#F4)", "(17#F12)", "(19#F3)"); 26, 27, 32, 39 .md ("(32#F19)") | Published world text carries no review-finding IDs. | Finding IDs are printed inside the reasons, e.g. "The call for tenders, by its ID (17#F1, 19#F4)" and "The framework contract the release is ordered under, by its own number (32#F19)". | High | `tools/examples_scenarios.py` lines 9267, 9829, 9868, 9872, 11465: the IDs are inside the `why` strings. Move them into the trailing `#` comments. |
| 2 | tender/26-Order.xml TaxTotal and its .md | The order has 40 benches (G, 19,960) and 40 installations (O, 720). The .md says the TaxableAmount is "The lines of this category plus the document's charges less its allowances". | Both TaxSubtotals (G/EXP and O/SVCABROAD) have TaxableAmount **0.00**, while AnticipatedMonetaryTotal is 20,680. | Medium | The Order tax-subtotal builder in `tools/examples_kit.py`: it probably finds no line category, because order lines carry no ClassifiedTaxCategory. Or the tender order block in `examples_scenarios.py`. |
| 3 | tender/02, 03: `RequestedTenderTotal` against `TenderingProcess/FrameworkAgreement` | D28 point 2: the framework value with the renewal year is 360 × 520 = 187,200; the maximum with the quantity option and the renewal is 408 × 520 = 212,160. | In one notice: **EstimatedOverallFrameworkContractsAmount 124,800** (.md "The framework's estimate") and **MaximumAmount 149,760** (288 × 520, "At most 20 % more"). Beside them: **FrameworkAgreement/EstimatedMaximumValueAmount 187,200** and **MaximumValueAmount 212,160**, with DurationPeriod 24 months although the estimate includes the third year. 01 and 21 carry only the 124,800/149,760 pair. | Medium | `examples_scenarios.py` ~9288 (the `est` amount for EstimatedOverallFrameworkContractsAmount, and MaximumAmount) against `FRAMEWORK_ESTIMATE`/`FRAMEWORK_MAXIMUM` (9650–9651, used at 9437). Also the FrameworkAgreement duration. |
| 4 | tender/25-Catalogue.xml; tender/27 Note | D28 point 8: "The catalogue quotes the special colour charge". The order change says "the special colour at 5 lume a bench the catalogue quotes". | The catalogue has the bench only in Ferro grey (COL property "Ferro grey", ExtendedID GRY). It has no moss-green variant and no 5-lume special colour charge, either as a line, an AllowanceCharge or a property. | Medium | The tender Catalogue block in `examples_scenarios.py` (a charge or price for the special colour), or the order-change note. |
| 5 | tender/17, 19 (Brackenmere LeadTimeMeasure 14) against 01, 02, 03 (RequestForTenderLine RequiredItemLocationQuantity LeadTimeMeasure 10, ".md: Ten days per release") | Brackenmere's 14 days' lead time is confirmed by the owner (D28). The call requires 10 days. | Brackenmere's tender does not meet the call's required lead time, yet it is "admissible" and joins the auction (21: "with both admissible tenderers"). | Medium | Either the call's required lead time (`examples_scenarios.py`, notice line 1) or Brackenmere's offered lead time. This needs a decision, since the owner confirmed 14 days. |
| 6 | tender/37-GuaranteeCertificate.xml ImmobilizedSecurity | .md: "25 bonds of 100 lume nominal". | FaceValueAmount **2,632.50**; its .md says "Their value on 18 February, the day they were immobilised". A face value is the nominal, 25 × 100 = 2,500.00. 2,632.50 is neither the nominal nor the market value of 2,640.00. | Medium | The ImmobilizedSecurity block for tender/37 in `examples_scenarios.py` (FaceValueAmount = 2,500.00, or reword). |
| 7 | tender/39-Invoice.xml TaxRepresentativeParty and Note; documents.json doc 39 `parties` | documents.json lists every party a document mentions. Bayforth (10-xb) is a forwarder; its "what" and wiki say nothing of tax representation, and Tevaro is the world's tax representative. | 39 names Bayforth Forwarding as `TaxRepresentativeParty`, with the Note "Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra for the withholding". documents.json doc 39 has no `TaxRepresentativeParty`, and the call-off collaboration lists 2-xb, 5-xu and 8-xu only. | Medium | documents.json doc 39 `parties` (+ `TaxRepresentativeParty: 10-xb`) and the collaboration's parties. Also parties.json 10-xb "what"/wiki (the role), or another representative. |
| 8 | tender/27-OrderChange.xml AnticipatedMonetaryTotal | UBL: the anticipated total of the order. | PayableAmount **200.00**, with only ChargeTotalAmount 200. The .md: "The amount of change to the order's total". Line 1 keeps its LineExtensionAmount 19,960, and the response gives 20,880. | Low | The OrderChange totals in `examples_kit.py`/`examples_scenarios.py` (20,880, or LineExtensionAmount 20,680 + charge 200). |
| 9 | tender/04 Note, tender/10 Note against documents.json docs 04 and 10 | documents.json doc 10: "The sawmill decides not to tender: a bench with cast-iron frames is not its trade". Doc 04: "registers its interest, to receive the documents". | 04: "The sawmill considers a tender for lot 1 with a bench maker". 10: "**No bench maker joined the sawmill**; it will not tender." The reason for unsubscribing differs. | Low | documents.json docs 04 and 10 `why`, or the two notes in `examples_scenarios.py` |
| 10 | tender/24 (IssueTime 17:24), tender/37 (17:19) | 2-xb and 25-xb: "Weekdays 08:00–17:00". | Issued after the issuer's desk hours. | Low | The time values in the tender block, or the desk hours |
| 11 | tender/01, 02, 03, 21 ProcurementProject/PlannedPeriod | The contract is signed 20 March and is valid from 20 March for 24 months (21, 22, 23, 24). | The planned period is 23 March 2026 to 22 March 2028. | Low | PlannedPeriod in the notice builder (start 20 March), or the contract validity |

### Consistent, but worth a second look

- **Interest in the remittance.** tender/36 pays only the reminded 31.13: 7 days, to 20 May. The payment is made on 22 May, so 9 days are owed (40.02). Coherent with "the interest reminded", but the department pays two days' interest short.
- **The decisions file is behind O226.** D28's "Built with G6" line still says "payment in ferra (2,031,191 ferra credited on 22 May)", which O226 overtook (all in lume). This is the workshop file only.
- **The turnover year.** tender/06 asks for the turnover of 2024 (ApplicablePeriod 2024). Valdara (13, 12) answers with its audited 2025 accounts by 24 February 2026, while Brackenmere files its 2025 accounts only on 7 May (contest/14). Plausible, but the call fixes 2024.
- **Reference amounts.** tender/13 states the Urvanian towns' reference contracts in lume (180,000, 62,000 and 38,000 XBL). They were presumably paid in ferra.
- **The slats.** tender/25 and items.json bench-serra give "thermally modified ash" slats. The wood read-through records the sawmill's slats as oak, with ash as an alternative. This is a cross-flow check.
- **Real standards in published text.** tender/25 names real standards in XML text: "EN 15804" (a CEN standard) and "Greenhouse Gas Protocol Product Standard". The rule names CEN; check whether EN 15804 counts.
- **Names in the documents.** tender/01–03 name a person (Mara Delling, TechnicalCommitteePerson). This is allowed in documents; the wiki texts carry no person names.
- **Paper copies.** The notices keep "Paper copies of the documents cost 50 lume" (DocumentationFeeAmount 50). D28's built line says "no paper-copy fee". Presumably that means the tenders charge none; confirm.

---

## contest (18 documents)

### What checks out

- **Prizes and estimate.**
  - Version 1: prizes 6,000 + 4,000 + 2,000 = 12,000, plus about 40,000, gives 52,000.
  - From version 2 on: 8,000 + 4,000 + 2,000 = 14,000, plus about 40,000, gives 54,000.
  - Each MonetaryScope says what the amount covers.
  - 15 keeps the mistaken 6,000; 16 corrects it to 8,000. The third prize is withheld in both.
- **Dates (D29 point 10).**
  - Notices: PIN 2 Feb; PIN v2 23 Feb (council 18 Feb); contest notice 19 Mar; call and QAR 20 Mar; corrigendum 6 Apr; requests to 17 Apr, then 30 Apr.
  - The team: 1 Apr; version 2 on 14 Apr (Tue, the day after Upland State Day).
  - Register extracts: 5 May and 8 May (accounts filed 7 May); Saltmere 5 May.
  - Exclusion 12 May; designs due 12 Jun; jury 26 Jun; results 2 Jul and 6 Jul. All fall on working days.
- **The team.**
  - Shares 60/40, then 70/30.
  - Design lead: Saltmere's architect, then Brackenmere's industrial designer.
  - References: the library reading garden 2024 and Larkmouth's seafront 2023, within 20 m of the sea.
  - Both members are winners at rank 1, Valdara at rank 2.
  - 4 designs received, 1 of them foreign.
- **Register figures.**
  - Brackenmere: 6.41 M (2024) and 6.83 M (2025), which equals parties.json's turnover.
  - Saltmere: 5.4 M, as in parties.json.
- **Exclusion.** The studio's 3,860 lume unpaid is above the 1,000 that tender/06 treats as minor.
- **Versions and references.** Every version 2 has VersionID 2 and PreviousVersionID 1, and a Note saying what changed. The references between versions match: 04 cites CN v1, 09 CN v2, 06 QAR v1, 11 QAR v2.
- **Published text.** The XML and .md carry no decision or finding numbers. The wiki texts (27-xb, 37-xb, 48-xb) carry no person names.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | contest/02 (PlannedDate 2026-03-19, against 01's 2026-03-04); documents.json doc 02 `why` | documents.json: "the contest notice moves by two weeks". | Wednesday 4 March to Thursday 19 March is 15 days, not two weeks. | Low | documents.json doc 02 `why` ("by about two weeks"), or the planned date (18 March) |

### Consistent, but worth a second look

- **Participation payments.** 01–04 and 08–09 promise each selected participant that submits a valid design 1,000 lume towards its costs (3 to 5 participants). Neither the estimate (52,000/54,000: "the three prizes and the follow-up service contract") nor D29's goods balance ("12,000 is paid; no payment document is needed") counts these 3,000–5,000 lume. A contest's estimated value usually includes the payments to participants.
- **The fictional act's article numbers.** 05, 10 and 18 cite "Public Procurement Act, art. 57" for the exclusion grounds; tender/14 and 37 cite "article 61". Art. 57 is the article number of the real EU directive's exclusion grounds. The world names no EU, but the parallel is visible to a specialist.
- **Wording.** contest/06's ResponseValue reads "Edda Corwin, the registered architect on Saltmere Engineering's staff, is a registered architect", which repeats itself.
- **Document references in the .md.** Notes such as "PWD/2026/0530 is the example contest/03, a ContractNotice" appear in every flow's .md: a pointer to an example file in published text. They are presumably meant as site links; confirm they count as allowed.

---

## medicines (14 documents)

### What checks out

- **Arithmetic.**
  - Nilavar order: 600 × 4,100 + 960 × 1,300 + 120 × 2,850 = 4,050,000 INR. At 88.8595 that is 45,577.57 EUR.
  - The hospital's order and invoice: 21,600 + 5,160 + 1,920 + 1,450 = 30,130 lume. Penalty 1.5 % = 451.95.
  - Customs values follow the fixings:
    - medicines/03: 2,460,000 / 75.4134 = 32,620.20 (fixing of 11 May);
    - medicines/08: 1,000 × 1.18700 = 1,187.00 (Friday 12 June's fixing for the Sunday declaration);
    - medicines/13: lume / 2.5, so 8,640, 2,064, 768 and 580 coral.
  - Margins of 18–24 %.
- **Packages and weights.** 10 cartons of 30 and 4 of 60 make 300 + 240. The goods weigh 60 + 12 + 1.6 + 18 kg; with 6 kg of dry ice and the box the AWB total is 101.1.
- **Activity.** 20 GBq × 2^(149.5/65.94) = 96.3 GBq at acceptance (05:30 −01:00); 97 GBq is declared.
  - Transport index 1.5, III-YELLOW, surface rate 0.30 mSv/h.
  - Type A, UN 2915, ERG 163. Dry ice UN 1845, PI 954, ERG 120.
- **Calendar.**
  - April to May: order 20 Apr (Mon), Nilavar invoice 7 May, import 11 May (Mon).
  - The hospital's order: 10 Jun (Wed); Haarvliet call-off 10 Jun, after it.
  - Generator to Lumeport: Haarvliet invoice Sat 13 Jun (week "always"), import Sun 14 Jun 21:40 (landed 20:15).
  - Monday 15 June: van 05:30, flight 07:00 −01:00 to 10:45 +00:00 (2 h 45).
  - Week 25 is the ISO week of 15 June.
  - Due dates: 6 Jun → 8 Jun, 27 Jun → 29 Jun, 15 Jul.
- **Logger.** It runs from 05:00 UTC (the 04:00 closing) to 11:00 UTC, minimum 4.4 and maximum 5.8, as the story says.
- **Legs.**
  - 49-xb's van Q-7 and 50-xl's van H-2 carry their legs.
  - Kelaro's ATR 72-600F (ATF, QL-KXA) flies KXL207.
  - RKN20871K0 is at MD-4; the generator and the dry ice are at AFT-BULK.
- **Taxes and exemption.** The island's MEDHOSP exemption is claimed by Tevaro as direct representative, with power of attorney POA-TT-2026-031. Category E, 0 % duty. Bayvarra's tax is G/EXP.
- **References.** All match: QLM-PO-26-2699, NLB-INV-26-1731, QLM-PO-26-3960, HVI-INV-26-1344, SGH/2026/1100, QLM-FI-26-2388, QLM-DGD-26-0615, QLM-DA-26-4074, KXL-00698121, QLM-INV-26-4080. RF48QLMINV264080 is valid.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | medicines/10 (acceptance) against medicines/12 (logger CSV) | The acceptance is at 05:30 −01:00, which is 06:30 UTC. | 10: "the active container at **4.8 °C**" (Condition 4.8). 12's log, from the same container, reads **5.6 °C** at 06:30Z (5.4 at 06:30 local, 05:30Z). 4.8 first appears at 07:45Z. | Medium | The logger series or the acceptance temperature in `medicines()` in `tools/examples_scenarios.py` (make the 06:30Z reading 4.8, or the acceptance 5.6) |
| 2 | medicines/02.md (CalculationRate reason) | Published text explains a value by the world, never by the project's method. | "In the world's calendar the ECB's rates are the real ones of 260 weeks before, the same that underlie the Lumeport Exchange's fixing." That is the workshop's shifting method (O231). | Medium | The `why` of PaymentExchangeRate/CalculationRate in `medicines()`. Say only "The ECB's euro reference rate of the invoice date". |
| 3 | medicines/11 DocumentDistribution 1 | The Note and .md describe "the consignor's original, handed over when the carrier took over the goods". The consignor is Quillmoor (49-xb); the forwarder is Bayforth. | The consignor's original (ORIGINALHANDED) goes to **Lumeport Airport Cargo Terminal (17-xb)**, not to the consignor or its forwarder. | Medium | The AWB distribution in `medicines()`, or the shared waybill-distribution helper |
| 4 | Quillmoor's contact in every medicines document; medicines/08 (Sun 21:40), 09 (Mon 05:10) | parties.json 49-xb `week: always`. Its wiki: "Its warehouse works every day and through the night". The story has the generator declared on the Sunday evening and despatched before dawn. | Every Quillmoor contact Note reads "**Weekdays 07:00–19:00**", including the Customs desk on 08 and the Dispatch office on 09. | Medium | parties.json 49-xb `identity.contact.hours`, or desk-specific hours for despatch, customs and goods-in |
| 5 | medicines/05, 07: TaxExemptionReason "Export outside the **European Union**"; 04, 05, 07, 08, 09 item text "(European pre-calibration)"; 05.md "Central European Summer Time"; 06/11.md "IAEA SSR-6 para 523/546" | The list of what published text must not name includes the EU and real regulations. | These texts name the EU and a real regulation. For a real Dutch maker the EU reason is factual, and the story itself says "as European makers pre-calibrate them". | Low | A decision for the owner: whether a real-country party may name the EU. If not, change the `why`/text in `medicines()` and the abroad party's tax reason ("Export outside the Netherlands' VAT area"). |
| 6 | medicines/09 Consignment/GrossWeightMeasure **91.6** against 06 and 11 **101.1** | They are the same consignment, QLM-CS-26-3980. | The despatch advice leaves out the dry ice (6 kg) and the frozen vaccine's box (3.5 kg). Its .md says "The goods with their packaging"; the box is that packaging. | Low | The consignment weight in the `DespatchAdvice` branch of `medicines()` |
| 7 | medicines/09 line 1 Note against medicines/04 Note | 04: "the campaign that starts on **22 June**". | 09: "the island's winter influenza campaign, which starts in the **last week of June**". The week of 22 June is not the last week of June: 29–30 June are. | Low | The despatch line note in `medicines()` |
| 8 | medicines/14.md IssueDate reason | Despatch was at 05:10. | "Issued on despatch", while the IssueTime is 10:27, and the IssueTime reason says "a few minutes before the document that cites it". | Low | The invoice IssueDate `why` in `medicines()` |
| 9 | medicines/13 Note (qal) | — | The Urvanian/Lisavan text contains an English genitive: "… tefata **Lisavu's** selune". It looks like a lexicon artefact. | Low | The qal translation of the note (`tools/lexicon.py` input / the note template) |

### Consistent, but worth a second look

- **Where the airport declarations are lodged.** medicines/03 and 08 name the Customs and Border Service at its head office address (Border Road, Euridice Crossing) and no office or location of the import at Lumeport airport. The .md says "the airport's customs office works around the clock".
- **The customs value of the Indian goods.** medicines/03.md says Bayvarra values goods "as they left the exporting country", but takes the CPT Lumeport price as the value because "it shows no freight apart". A CPT price contains the air freight. Coherent as worded, but a careful reader may object.
- **Hours of the morning collection.** The forwarder's truck collects at 04:15, while Bayforth (10-xb) is an office-week party with "Weekdays 08:00–17:00". A carrier's operations can run outside desk hours; consider an operations desk.
- **Real treaty name.** medicines/11 Name "Air waybill under the Montreal Convention" names a real treaty, as the air flow presumably does. Confirm this is accepted.
- **Doubts already recorded.** D47 notes them: the arrival activity of 92.8 GBq is not stated anywhere, and the transport index stays at 1.5.

---

## lpg (4 documents)

### What checks out

- **Arithmetic.**
  - Order: 20 × 560 = 11,200; tax 728; total 11,928.
  - Invoice: 20.18 × 560 = 11,300.80; tax 6.5 % = 734.55; total 12,035.35; surcharge 1.5 % = 180.53.
- **Weights.**
  - 37,180 − 17,000 = 20,180 kg net; the tare is tractor 7,300 + trailer 9,700 (parties.json).
  - Shipment gross 29,880 = goods + tank tare.
  - The tank plate's 20,500 kg is respected, and 37.18 t is within 40 t.
- **Emissions.** 1,700 kWh × 0.268 = 456 kg; 1,240 × 0.268 = 332 kg.
- **Fuel.** 33 l/100 km × 515 km = 170 l, about 1,700 kWh. 24 l/100 km gives about 1,240 kWh.
- **Times.** 07:00 to 15:40 is 515 km at 65 km/h plus 45 minutes. The tare is weighed at 05:40 and the loaded tanker at 06:45; the waybill is issued at 06:50 and the despatch advice at 07:05.
- **Dangerous goods data.** UN 1965, mixture C, 2.1, ERG 115, orange plates 23/1965, tunnel code B/D, TEC2, ADR, HS 2711.12.
- **Dates.** Order Mon 8 Jun, delivery Wed 10 Jun, invoice Thu 11 Jun. Due date: 30 days end on Sat 11 Jul, so it moves to Mon 13 Jul.
- **Tax.** S 6.5 %, Coastal State's rate. The propane is burned, not resold (O204).
- **RF reference.** RF669000034662 is valid.
- **Parties and leg.** The parties and the leg (42-xb → 34-xb by 52-xb, vehicle GT-04) match documents.json and parties.json. Driver Rowan Tallis is named only in the document, not in the wiki.

### Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | lpg/03 Note and DocumentDistribution; 03.md | The Note says there are three originals: the consignor's, the consignee's, the carrier's. The .md says "as the distribution below lists them; the carrier's own is not distributed". | Only the consignee's original (ID 2) is distributed; the consignor's original (Kelpstone) is missing. The .md also says "The originals **the convention** prescribes", but this is a note under Bayvarra's national road carriage law, not a convention. | Low | The waybill distribution and its `why` in `lpg()` in `examples_scenarios.py` (add the consignor's original; word "the law" for NATROAD) |
| 2 | lpg/03 ReceiverParty Contact | Kelpstone has a "despatch" desk, the Dispatch office, as the despatch advice uses it. | The consignment note goes to Kelpstone's "**Pipeline control**" (operations desk). The .md: "the desk for its role in this document (it carries or handles the goods)". Pipeline control does not handle a road tanker. | Low | The desk choice for ReceiverParty in `lpg()`, or the role-to-desk mapping |
| 3 | note/src/03-world.md (lpg paragraph) against lpg/03.md (TunnelRestrictionCode) | 03-world: B/D "forbids a tank of it **every** road tunnel". | .md: "in a tank, no passage through tunnels of categories B to E". That is correct ADR: category A tunnels stay open. | Low | `note/src/03-world.md` (story wording: "every tunnel of category B or higher") |

### Consistent, but worth a second look

- **Cited entries.** The cited register lists `kelpstone-tanker-booking` for lpg/03's collaboration, but the waybill cites no booking. The invoice cites the weighbridge ticket (`kelpstone-weighbridge-ticket`), which is in no collaboration's `cited`.
- **Two carrier numbers.** lpg/03 ID 26-0791 and CarrierAssignedID 26-0040 are both the haulier's own numbers, "The consignment note number" and "The carrier's own number for the carriage". With the carrier as issuer, the second number may be redundant.
- **The buyer's contact.** The water company orders through "Customer service" (the only general contact). It has no purchasing desk.
- **A change word in a reason.** lpg/02.md says "the IMDG Code **no longer** gives medical first aid table numbers per UN number". It states a real-world fact, but it is a change word in published text.
- **The tax registration.** Kelpstone's PartyTaxScheme shows its Northern Territory registration (NT-1238631) while it charges Coastal State's 6.5 %. Under destination sourcing a seller usually registers in the state of delivery.

---

## Across the four flows

- **Published data outside these flows** (if the Rules pages print them): countries.json XB `tax.exemption_codes_note` names "the EU's VATEX list", and `tax.duty_free.note` names "the WTO's zero-for-zero agreement". O256 fixed decision numbers in these files but not these names.
- **Story text in `note/src/03-world.md`.** It cites "Mervärdesskattelag (2023:200) chapter 10 § 13" and "the EU's preferential arrangements". This is the method note's world chapter, not the site's world pages; it only matters if the encyclopaedia reuses the paragraph.
