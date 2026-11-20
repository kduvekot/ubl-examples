**Status (2026-11-20):** all 12 mismatches fixed (O255, O258, O259); see the O255 row in `analysis/worklist-decisions.md`.

# Read-through: flows `wood` and `modification` (O112/O248), 2026-11-20

Sources read: note/src/03-world.md (park bench, inward processing, contract-processing paragraph), world/documents.json (flows wood and modification, documents 166-185, cited), world/parties.json (5-xu, 13-xu, 19-xb, 19-xu, 23-xu, 25-xb, 36-xb, 37-xb, 59-xu), world/items.json (slat-1800, slat-bundle-1800, ash-blank-1830, tm-processing, tm-storage, timber-oak, timber-ash), world/countries.json (XU tax.inward_processing), analysis/worklist-decisions.md (story line "Slats from the sawmill (D43)", D43, O150, O243, O246, O249, O251, O253, O254), all XML and .md of world/examples/wood and world/examples/modification (no *.llm-review.*), the generator sections in tools/examples_scenarios.py.

## What checks out

These checks found no problem:

- **Arithmetic.**
  - Slats: 96 × 480 = 46,080; plus pallets 240 = 46,320 lume. The penalty is 1.5 % = 694.80.
  - Processing and storage: 96 × 13,250 = 1,272,000; 4 × 5,760 = 23,040; total 1,295,040 ferra. The 2 % discount is 25,901 (ferra has no minor unit), so 1,269,139 is paid.
  - Customs value of a load: 2,400 × 4.80 + 600 = 12,120 lume = 1,212,000 ferra. The release is 2 × 1,212,000 = 2,424,000, and VAT at 20 % is 484,800.
  - Timber: 7 × 540 + 5 × 540 = 6,480; penalty 97.20.
- **Weights.**
  - Blank: 5.89 kg. A blank pallet is 200 × 5.89 + 26 = 1,204 kg, and 12 pallets are 14,448 kg.
  - Bundle: 212.5 kg. A bundle pallet is 4 × 212.5 + 26 = 876 kg, and 24 pallets are 21,024 kg.
  - The Trasvia truck carries 21,024 kg on a tare of 15,300 kg, so 36.3 t, within the 40 t limit.
  - The pallet sizes (1850 × 970 × 1022 and 1397) follow from the bundle and blank sizes.
- **Calendar and weekdays.**
  - 12 Jan (Mon), 13 and 20 Jan (Tue), 30 Jan (Fri), 4 Feb (Wed), 6 Feb (Fri), 16, 19 and 23 Feb, 26 Feb (Thu), 6 Mar (Fri), 9 Mar (Mon).
  - Due dates move from Sat 28 Mar to Mon 30 Mar, and 9 Apr stands.
- **Lots and kiln charges.** MS-L26-0119 and MS-L26-0126 match the order response's kiln charges (14–19 and 21–26 Jan), the inventory report and wood/06.
- **References.**
  - The IDs between documents exist and match: MS-PO-26-0406, TWM-IM-26-0413, TWM-IM-26-0414 (cited, 20 Jan), MS-EX-26-0411, TWM-DA-26-0630, VI-PO-26-0627, MS-DOC-26-0626, VI-DOC-26-0625, TWM-INV-26-0417, MS-INV-26-0634, BF-PO-26-0636.
  - Shipment and consignment IDs agree across modification/03, 04 and 05.
  - ReleaseID MS-REL-26-0212 is the same in modification/07 and wood/06.
- **Payment references.** The three ISO 11649 RF check digits are valid.
- **Parties and roles.** Every party and role matches documents.json.
- **Legs and vehicles.** Both legs and their carriers match documents.json: 36-xb with its own truck, and 13-xu with T-07, the curtain-side trailer named in modification/07.
- **Classification codes.**
  - The blank is HS 4407.95 / CPC 31102, section IX.
  - The slat bundle is HS 9401.91 / CPC 38160, section XX.
- **Tax treatment.** The plant's service is O / SVCABROAD, as the story and O254 (8) say.
- **Inward processing against the XU rule.**
  - The statistics value is on the entry, not on the release.
  - On release, VAT is assessed on the goods as placed.
  - The release notes "goods of Accord origin, no duty".
  - Valdara deducts the VAT in its return.
- **Published-text rules.** The XML and .md of both flows contain no decision, open-point or finding numbers and no paths. They name no EU, Peppol, EN 16931 or Union Customs Code. Every "now" in them is world-natural ("part of English now", "available now").

## Mismatches

| # | File(s) | Story / data says | XML / .md says | Severity | Likely source to fix |
|---|---|---|---|---|---|
| 1 | wood/01 to 03 against modification/01 to 07 (chronology) | 03-world: "For the February delivery to Valdara the sawmill orders one job"; the quotation names the plant. documents.json (wood): Valdara asks for a quotation, then orders 96 bundles; the February delivery is modified at Conciaro. Story line D43: once a quarter. | The sawmill orders the job "for Valdara's park-bench slats" on **12 Jan** (modification/01), sends the blanks on 13 and 20 Jan, and the job is ready on 4 Feb. Valdara's **RFQ comes on 16 Feb**, the quotation on 19 Feb and the order on 23 Feb. modification/01.md justifies LatestDeliveryDate as "in time for the delivery to Valdara from 26 February", a date first requested in the RFQ five weeks later. So the slats are made to Valdara's drawing, and the delivery date is known, before Valdara asks for a quote. | High | `tools/examples_scenarios.py`: `WOOD = kit.Flow("wood", "2026-02-16", ...)` and the day offsets in `wood()`, against `MOD = kit.Flow("modification", "2026-01-12", ...)` / `MOD_DAY`. Alternatively the flow texts in documents.json and 03-world. |
| 2 | wood/02, wood/03, wood/08 (tax category, charge reason) and their .md; documents.json doc 173 "why" | The finished slats never leave Bayvarra. documents.json doc 170 "removed": "the wood of this delivery left Bayvarra in January as blanks ... the finished slats travel only inside Urvania". 03-world: the slats are sold "while they are still under the procedure" in Urvania. | **Tax category.** Category G, reason EXP "Export outside Bayvarra", on the line, the charge and the subtotal. The .md says "No tax on an export", "The slats and the pallets; no tax on an export". **Pallet charge.** It is named "Heat-treated export pallets"; the .md says "The export pallets" and "24 pallets treated to ISPM 15, as the quotation offered for the export". **documents.json doc 173.** Its "why" still reads "An export from Bayvarra: no sales tax". The sale is of goods located in Urvania (outside Bayvarra's sales tax: O rather than G), and nothing is exported. | Medium | documents.json doc 173 "why"; `PALLETS_CHARGE` ("reason", "why") and the quotation/order texts around lines 12192–12204 in `tools/examples_scenarios.py`; the XB tax-category choice for a foreign buyer in `tools/examples_kit.py` (the G/EXP branch) |
| 3 | wood/08 (Invoice/Note) and wood/08.md | The slats are worked in Urvania (modified, planed, sealed). The release rests on the entries, not on a commercial invoice: O254 (7), "the release declaration (wood/07) cites no commercial invoice". | **Note.** "The exporter of the goods covered by this document declares that these goods are of Bayvarran preferential origin under the Trade Accord (criterion P)". **.md.** "the proof of origin the buyer's import declaration refers to, to claim the Trade Accord's preference". **Problems.** The sawmill is not the exporter of these goods. "Wholly obtained" in Bayvarra does not hold for slats processed in Urvania. wood/07 does not refer to this invoice. | Medium | The origin statement in `tools/examples_kit.py` (~line 1254) and its "why" in `tools/build_examples.py` (~line 2360), or a flow-specific override in `wood()` |
| 4 | wood/04-TransportExecutionPlanRequest.md (IssueDate reason) | Leg: road 59-xu → 5-xu, Conciaro to Ferrano, inside Urvania. The XML Note: "from the modification plant to the bench factory". | "Under DAP the sawmill books the truck **across the border**." | Medium | `tools/examples_scenarios.py` line 5170, the `kit.tep_request(...)` why text |
| 5 | modification/04-ExportCustomsDeclaration.md (ExportTypeCode) | The blanks are not sold. They remain the sawmill's property, go for processing, and the slats are sold in Urvania (export reason PROCESSING, its own .md). | "A permanent export: **the goods are sold abroad**." | Medium | `tools/examples_scenarios.py` line 7050, a shared export default: the modification flow needs its own reason text |
| 6 | wood/10, wood/11 against the leg 36-xb → 37-xb (carrier 37-xb, fleet V-1 "Delivery van") | documents.json: "The furniture maker collects the timber at the sawmill's yard with its own van". | 12 m³ of timber at 700 kg/m³ (items.json net_kg) is about 8.4 t, collected in one day (wood/11 ActualDeliveryDate 10 Mar). A delivery van cannot carry that. V-1 has no tare, so the build's payload check does not apply. | Medium | world/parties.json 37-xb fleet (vehicle and tare), or the TIMBER quantities in `tools/examples_scenarios.py`, or the leg text in documents.json |
| 7 | wood/04 (ServiceEndTimePeriod 2026-03-01) and .md "Delivered within three days." | Leg transit_days 0, about 29 km (O254 (9)). wood/06 has the estimated and actual delivery on 26 Feb, and modification/07 "Delivered at Valdara the day it is collected". | End date Sunday 1 March, "within three days". | Low | `tools/examples_kit.py` lines 1057/1093 (`start_day + 3`): needs the leg's transit time |
| 8 | modification/06-InventoryReport.xml Note | Line 2: charge 2 is "modified; still being planed and sealed", available 4 Feb. | Note: "Both loads of blanks are processed; no blank is left unprocessed." The .md: "that the material is used up". Line 2 says the processing is not finished. | Low | The Note in the `InventoryReport` branch of `modification()` in `tools/examples_scenarios.py` |
| 9 | modification/01-Order.xml line Note | items.json: MS-SL-1800 is the sawmill's slat; Valdara's part is VI-R-SL1800 (the bundle's own description says so). | "96 bundles of 50 slats, **Valdara's slat MS-SL-1800** to drawing VI-DS-SL1800." | Low | The `Order` branch of `modification()` in `tools/examples_scenarios.py` |
| 10 | modification/08 line 2 (storage, 4 weeks) and .md | items.json tm-storage: "per week begun from the week the job's last charge is finished". The order response: charge 2 in the kiln 21–26 Jan. wood/06.md: ManufactureDate 26 Jan "the day kiln charge 2 came out of the plant's kiln". The inventory report: finishing done 4 Feb. | .md: "The weeks begun from the week the second charge was finished, **2 February**, to the call-off on **26 February**". **Week count.** "Finished" read as out of the kiln gives the week of 26 Jan, so 5 weeks. Read as finished planing (4 Feb), it gives 4 weeks. 2 Feb is neither date, only that week's Monday. **Call-off date.** The call-off is dated 24 Feb; 26 Feb is the collection. | Low | items.json tm-storage description ("finished" = ready in store), and the storage-line why in `modification()` |
| 11 | modification/03 (IssueTime 06:45) and modification/04 (IssueTime 07:00) | parties.json 36-xb: desks and contact "Weekdays 08:00–17:00"; both documents name those desks (Dispatch office, Customs desk). | Issued before the desks open. | Low | The time values in `modification()`, or the desk hours in parties.json |
| 12 | wood/06 TransportHandlingUnit/Package/Quantity = 50 on each of 24 pallets | Each pallet carries 4 bundles of 50 slats (TotalPackageQuantity 4). | Package Quantity 50 under a pallet of 4 packages: the generator's why reads "50 slats in a bundle". The pallet says nothing per bundle, and the lots are not tied to pallets. documents.json says the advice announces the bundles "on their 24 pallets with the lot of each kiln charge, so the factory can trace the wood of every bench". | Low | `wood_pallets()` in `tools/examples_scenarios.py` (Package as 4 bundles; optionally the pallets per lot) |

## Consistent, but worth a second look

- **The inventory report's retailer party.** modification/06's `RetailerCustomerParty` is the plant. This is a known stretch of UBL's "retailer", recorded in O254 (6). The semantic-conformance finding still has to be written up.
- **How wood/07 cites the second entry.** wood/07 cites the second entry (TWM-IM-26-0414) as an `AdditionalDocumentReference` beside a single `PreviousCustomsDeclaration`. Check whether UBL 2.5 allows only one PreviousCustomsDeclaration (that would be the reason), and whether the .md should say why.
- **The release declares the products but is assessed on the blanks.** wood/07's goods items carry the products (96 bundles, HS 9401.91, section XX), but the duty and VAT are assessed on the blanks as placed: 4,800 blanks, HS 4407.95, 2,424,000 ferra.
  - The Note states this in words only.
  - No element carries the blanks' quantity or tariff line.
  - This is coherent with the XU rule but easy to misread.
- **New IDs missing from the cited register.** These IDs are in no `cited` entry of documents.json: TWM-SA-2526-MS (the season agreement), MS-PF-26-0113 (the pro forma), XU-IP-AUT-0217 (the authorisation) and MS-REL-26-0212 (the release). They are defined only as generator constants. VI-PUR-TERMS-2026 and MS-TH-FW-2026 are handled the same way already, so this is not new, but TWM-IM-26-0414 is registered as cited while these are not.
- **Stale kiln-charge property.** items.json `slat-1800` and `slat-bundle-1800` carry `lot_props` "Kiln charge K-07". It is not used in these XMLs (they show TWM-K1-26-03 and -04) and conflicts with the plant's numbering.
- **Vehicles without tare.** Vehicles S-1 (the sawmill's timber truck with crane, 14,448 kg a load) and V-1 (the Brackenmere van) have no `tare_kg`. The 40 t road rule in countries.json ("A carrier's fleet gives each vehicle's empty weight") is therefore unchecked for both legs. A rigid crane truck with 14.4 t of payload is at the edge.
- **The second load of blanks.** Its export declaration and despatch advice (20 Jan) are not cited anywhere; only its entry TWM-IM-26-0414 is. modification/04 covers 2,400 of the 4,800 blanks. This is consistent with O253, but the export side of the second load is invisible.
- **No statement on Urvanian VAT in wood/08.** The story says a sale under the procedure carries no Urvanian VAT. The invoice states only Bayvarra's sales tax; consider whether it should say so (ties in with mismatch 2).
- **Customs IDs on a domestic leg.** wood/04 gives SenderParty the sawmill's XB customs-trader ID, and the consignee and consignor their XU customs IDs, on a leg with no customs.
- **Language of the plant's item text in the order.** modification/01, issued by the Bayvarran sawmill, carries the plant's item texts in qau and tagged `en-XB`. modification/08 tags the same text `en-XU`, and the .md says "as Tostara Wood Modification describes the item".
- **Desks named in the contacts.**
  - Tostara: "Sales office" in modification/03 (as receiver of the blanks) and in 06.
  - Sawmill: "Sales office" in wood/04, in modification/07 and in the payer role of modification/09.
  - Both parties have more fitting desks (despatch, logistics, customs, receivables).
- **Discount period ends on a Sunday.** The discount period of modification/08 ends Sunday 8 March. This is deliberate (O254 (4)) but should be confirmed.
- **Shared .md boilerplate (workshop layer).** Two texts in modification/09.md and wood/09.md explain a value by the project's model, not by the world:
  - "as in the OASIS example UBL-RemittanceAdvice-2.0-Example"
  - "(UBL 2.5, 2.2.2 Manifest Values)" in the invoices
- **Published data outside these flows.** If the Rules pages publish these texts, they break the publishing rules:
  - countries.json XU `tax.summary` names the EU ("in the style of the EU VAT").
  - lists.json descriptions carry decision numbers and real law. XU:TaxExemptionReason SVCABROAD mentions "decision D17"; EXPTRANSPORT names "Article 146(1)(e) of Directive 2006/112/EC; decision D41". The same applies to XB LEVY (D31) and XL MEDHOSP (O201).
- **Change words in documents.json doc 170.** Its "removed" note contains change words ("Removed 2026-11-20 ... not used again"). It is not printed as world text as far as tools/world_data.py shows; worth confirming that no page prints `removed_documents`.
