"""Scenarios of the example flows: what a flow adds to the world's layers.

Per flow: its start date, its deal (the items and quantities it is about) and,
per document, the day it is issued and what is particular to it, each value with
its reason. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers;
lines, amounts and taxes are worked out by tools/examples_kit.py.
"""
import datetime
import uuid
from decimal import Decimal

import build_examples
import codelists
import examples_kit as kit
import world_ids
import world_items
import world_map as wmap
from build_examples import ITEM, PARTY, WORLD, V, Detail, address, amount, coordinate, item, money, party, price, qty


def rate(a, b):
    """The world's reference exchange rate: units of b for one unit of a (world/countries.json)."""
    return Decimal(str(WORLD["exchange_rates"][f"{a}/{b}"]))


# ---------------------------------------------------------------- the ore flow (Urvania, domestic)
# The yearly supply agreement behind the monthly call-off (D45): the price basis, one train a month and the moisture
# clause; the mine's number for it, in the style of the flow's other contract (VI-FRC-FW-2026).
ORE_AGREEMENT = "SM-VI-SA-2026"
ORE_MOISTURE = ("7.5", "6")       # measured at loading, and the limit of the agreement's moisture clause, in %
ORE_ASSAY = "SM-ASSAY-26-12"      # the assay certificate of the sample taken at loading (world/documents.json, cited)
ORE = kit.Flow("ore", "2026-03-02", [
    {"item": "ore-lump", "ordered": 1800, "delivered": "1788.4",
     "why": "One train: 30 wagons of about 60 tonnes.",
     "invoice_why": "The weighed quantity from the despatch advice, not the ordered quantity.",
     "line_allowance": {"percent": "1.5", "code": "64", "code_why": "The reason for the allowance as a code of "
                        "UN/EDIFACT 5189: special agreement, the moisture clause of the supply agreement.",
                        "reason": f"Moisture deduction under the moisture clause of supply agreement {ORE_AGREEMENT}: "
                                  f"{ORE_MOISTURE[0]} % moisture measured at loading, above the {ORE_MOISTURE[1]} % "
                                  "agreed",
                        "why": f"The sample at loading showed {ORE_MOISTURE[0]} % moisture (assay {ORE_ASSAY}), above "
                               f"the {ORE_MOISTURE[1]} % of the supply agreement, whose moisture clause deducts 1.5 % "
                               "of the value (D45, ore/07#F2)."},
     "line_tax": True}])
# the ore train on the map (O152, O197): the leg from the mine siding to the factory's siding, on the continuous line
# past Ferrano; a loaded ore train averages about 40 km/h on the line's gradients (D45: it leaves in the morning and
# arrives the same afternoon, on the first day of the window, and earns the plan's bonus)
ORE_KM = wmap.leg_km("ore", "4-xu", "5-xu", "rail")
ORE_TRAIN_KMH = 40
ORE_DEPARTS = "10:05"            # once the 30 wagons are loaded, weighed and sheeted and the note is made out
ORE_ARRIVES = wmap.after(wmap.at("2026-03-10", ORE_DEPARTS), ORE_KM / ORE_TRAIN_KMH + 0.25)   # with the shunt in
ORE_BONUS = Decimal("2")         # % of the freight, for a train delivered on the first day of the window (plan)
if ORE_ARRIVES.date().isoformat() != "2026-03-10" or ORE_ARRIVES.hour >= 17:
    raise SystemExit("ore: the train no longer arrives on the afternoon of 10 March (D45, O152)")
ORE_SIDING = kit.place("XUFER", "The factory's siding, where the train is placed for unloading.",
                       name="Valdara Industries works siding, Ferrano")


def ore(n, doc):
    f = ORE
    weighed_kg = Decimal("1788.4") * 1000
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The first working day of the month: the monthly ore call-off.",
                         "Free carrier at the mine: the buyer arranges and pays the main transport, so the order names "
                         "the carrier the buyer has booked. Stated, because leaving it out would carry no meaning "
                         "(UBL rule IND6).", "Fucinalta mine siding",
                         {"OrderTypeCode": V("226", "UN/EDIFACT 1001 code 226, call off order: the month's train "
                                                    "called off under the yearly supply agreement, which sets the "
                                                    "price basis, one train a month and the moisture clause "
                                                    "(D45, ore/01#F4)."),
                          "Note": V("The call-off for March under the supply agreement for 2026: one train.",
                                    "Says in words what the order is for."),
                          "Contract": {"ID": V(ORE_AGREEMENT, "The supply agreement the order calls off."),
                                       "ContractTypeCode": V("SUPPLY", "Recurring supplies at agreed quantities: one "
                                                                       "train a month."),
                                       "ValidityPeriod": {"StartDate": V("2026-01-01", "A yearly agreement, for 2026."),
                                                          "EndDate": V("2026-12-31", "To the end of the year.")}},
                          "Delivery": {"RequestedDeliveryPeriod": {
                              "StartDate": V(f.date(8), "The loading window for March's train, from Tuesday 10 "
                                                        "March: the window the buyer then books the train in."),
                              "EndDate": V(f.date(11), "To Friday 13 March.")}}})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "The day after the order: the buyer books the train it named in its order.",
                               8, 1800000, "The expected weight: the ordered quantity.")
    if doc["doc"] == "TransportExecutionPlan":
        return kit.tep(f, n, doc, 2, "The day after the request.", 8, 1800000)
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 8, "The day the train was loaded and weighed.",
                                   "Weighed on the weighbridge at loading: 30 wagons.",
                                   {"IssueTime": V("10:20:00", f"Sent once the train has left the siding at "
                                                               f"{ORE_DEPARTS}, so that the factory can plan the "
                                                               "unloading before it arrives."),
                                    "Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                         "The buyer's consignment, quoted back.")}}})
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 8, "Made out at the mine siding when the carrier took over the loaded train, "
                                         "and completed at delivery: this is the receiver's electronic copy, sent "
                                         "once the consignee has signed for the train in its siding, so it records "
                                         "the arrival (D45, ore/06#F4).", weighed_kg,
                           "The weight the carrier takes over, from the weighbridge.",
                           {"Shipment": {"Delivery": {
                               "ActualDeliveryDate": V(f.date(8), "The train arrived the same day, the first day of "
                                                                  "the window."),
                               "ActualDeliveryTime": V(wmap.hm(ORE_ARRIVES), f"It left the mine siding at "
                                                       f"{ORE_DEPARTS} and ran {wmap.whole(ORE_KM)} km on the line past "
                                                       "Ferrano at about 40 km/h, then shunted into the factory's "
                                                       "siding."),
                               "DeliveryLocation": ORE_SIDING}}})
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        freight = build_examples.money(Decimal("1788.4") * Decimal(str(ITEM["rail-ore"]["price"]["amount"])), "XUF")
        return kit.invoice(f, n, doc, 10, "Issued after the carriage was performed.",
                           {"AdditionalDocumentReference": [
                               {"ID": V(f.numbers["tep"], "The transport plan with the agreed price and the bonus.")},
                               {"ID": V(f.numbers["waybill"], "The consignment note of the carriage invoiced, with "
                                                              "its arrival.")}],
                            "ContractDocumentReference": {"ID": V("VI-FRC-FW-2026", "The framework transport "
                                                                  "agreement the freight and its terms rest on "
                                                                  "(ore/06#F5).")}},
                           [{"item": "rail-ore", "qty": "1788.4",
                             "invoice_why": "The weight carried, from the consignment note: the freight is per tonne."}],
                           key="freight-invoice", terms="plan",
                           charges=[{"like": "rail-ore", "amount": build_examples.money(freight * ORE_BONUS / 100, "XUF"),
                                     "code": "ZZZ", "code_why": "UN/EDIFACT 7161 has no code for a bonus: mutually "
                                                                "defined, the plan's bonus term.",
                                     "reason": "Bonus: train delivered on the first day of the window, 10 March",
                                     "why": "The plan's bonus term, earned: the factory could start the blend a day "
                                            "early (D45).",
                                     "amount_why": f"{ORE_BONUS} % of the freight of {freight:,}."}],
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(8), "The day the train was delivered "
                                                                                  "in the factory's siding, the first "
                                                                                  "day of the window: why the bonus "
                                                                                  "is due."),
                                               "ActualDeliveryTime": V(wmap.hm(ORE_ARRIVES), "As the consignment note "
                                                                                             "records it."),
                                               "DeliveryLocation": ORE_SIDING}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 9, "Issued the day after the goods were despatched and weighed.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"],
                                                                  "The despatch advice of the goods invoiced.")},
                            "AdditionalDocumentReference": {"ID": V(ORE_ASSAY, "The assay certificate of the sample "
                                                                               "taken at loading, which measured the "
                                                                               "moisture the deduction rests on "
                                                                               "(ore/07#F2).")},
                            "ContractDocumentReference": {"ID": V(ORE_AGREEMENT, "The supply agreement whose price "
                                                                                 "basis and moisture clause the "
                                                                                 "invoice applies.")}})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The day the payment is made, one day before the due date.")
    raise SystemExit(f"ore scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the road flow (Urvania -> Bayvarra)
ROAD = kit.Flow("road", "2026-03-16", [
    {"item": "bench-serra", "ordered": 96, "why": "24 pallets of four benches, on a truck booked for this delivery alone."},
    {"item": "bench-casting", "ordered": 12, "why": "Spare side frames, for the distributor's service stock."}],
    buyer="6-xb")
# the truck's leg on the map, from the 3PL in Conciaro to the distributor in Marrowdale (O152: the kilometres stated
# are those driven on the leg), and how far along it the land border is
ROAD_LEG_KM = wmap.leg_km("road", "8-xu", "6-xb")
ROAD_BORDER_KM = wmap.border_km("road", "8-xu", "6-xb")
DISTANCE_KM = wmap.whole(ROAD_LEG_KM)
TRUCK_KMH = 65        # a loaded truck's average on the main road, with its stops
ROAD_DEPARTS = "16:20"
ROAD_AT_BORDER = wmap.after(wmap.at("2026-03-23", ROAD_DEPARTS), ROAD_BORDER_KM / TRUCK_KMH)
ROAD_CLEARED = "10:40"   # the truck leaves the Bayvarran post once the import declaration is accepted
ROAD_IN_MARROWDALE = wmap.after(wmap.at("2026-03-24", ROAD_CLEARED), (ROAD_LEG_KM - ROAD_BORDER_KM) / TRUCK_KMH)


def goods_items(f, currency, value_why, convert=None):
    """GoodsItem per line of the deal, with the customs value and the item (HS code, origin)."""
    out = []
    for i, d in enumerate(f.deal, 1):
        it = ITEM[d["item"]]
        pr = kit.price_of(d["item"], f.buyer)          # the transaction value: the price the buyer pays (D14)
        value = Decimal(str(d["ordered"])) * Decimal(str(pr["amount"]))
        if convert:
            value = value * rate(pr["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(kit.line_gross(f, d, "ordered"), "KGM",
                                              "The gross weight of the goods of this item, in their parcels and "
                                              "with the pallets they travel on."),
                    "Quantity": qty(d["ordered"], it["unit"], "The quantity declared."),
                    **kit.goods_packages(f, d),
                    "Item": item(d["item"])})
    return out


HARBOUR_PROJECT = "VT-PRJ-26-07"   # the buyer's number for its project "Harbour parks Selanu"
ROAD_JOB = "TH-26-04471"          # the carrier's job number for the truck
ROAD_CASTING = "2026"             # the extended ID of the 2026 side frame casting, which replaced the 2025 one
ROAD_CO_JOB = "FCC-JOB-26-0418"   # the chamber's job number for Valdara's application for a certificate of origin


def road_stage(f, actual):
    """The main carriage by truck: Ferrano to Marrowdale, across the land border."""
    stage = {"ID": V("1", "The only stage: one truck from the warehouse to the distribution centre."),
             "TransportModeCode": V("3", "UN/ECE Recommendation 19 code 3: road transport.",
                                    listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
             "TransportMeansTypeCode": V(kit.fleet("13-xu", "T-07")["type"], "The truck pulls a trailer: the "
                                                                                "carrier's tractor unit 07 with its "
                                                                                "curtain-side trailer."),
             "TransitDirectionCode": V("EXPORT", "The goods leave Urvania by this stage."),
             "CabotageIndicator": V("false", "A carriage between two countries, not within a foreign one."),
             # the consignment note is made out at takeover: the stage has begun, its end is still an estimate (C72)
             "TransitPeriod": {"StartDate": V(f.date(7), "Collected in the afternoon; the stage has begun when the "
                                                         "carrier takes over the goods.")},
             "TransportMeans": kit.means("13-xu", "T-07", direction="WB"),   # a one-off trip: no JourneyID (C41, D35)
             "DriverPerson": kit.person("Ilario", "Bencetti", "The driver of the truck.", "XU-DL-0417722"),
             "LoadingPortLocation": kit.place("XUFER", "Loaded at the 3PL's warehouse in Conciaro."),
             "UnloadingPortLocation": kit.place("XBMRW", "Unloaded at the distributor's distribution centre."),
             "EstimatedDeliveryDate": V(f.date(9), f"The carrier's estimate when it takes over the goods: the goods-in "
                                                   f"slot of the third day. The leg is "
                                                       f"{DISTANCE_KM} km, about three hours' driving, but the truck "
                                                       f"reaches the border about {wmap.about(ROAD_AT_BORDER)}, after "
                                                       "the distributor's customs desk has closed, so the driver takes "
                                                       "his night rest at the border and the import is declared in "
                                                       "the morning; the distribution centre takes full loads in "
                                                       "morning slots only, and the slot booked a week ahead is the "
                                                       "next morning's."),
             "EstimatedDeliveryTime": V("09:00:00", "Early in the working day."),
             "RequiredDeliveryDate": V(f.date(9), "The distributor's goods-in slot."),
             "RequiredDeliveryTime": V("10:00:00", "By the end of the goods-in slot, 09:00 to 10:00; the latest "
                                                    "delivery time of the note is the same (road/08#F14).")}
    if actual:      # what the carrier's status reports once it has happened (C72)
        stage["ActualDepartureTransportEvent"] = kit.event(f, 7, ROAD_DEPARTS + ":00", "The truck left the warehouse; "
                                                           f"the land border is {wmap.whole(ROAD_BORDER_KM)} km ahead.",
                                                           kit.place("XUFER", "Castrano Logistics warehouse."))
        stage["ExaminationTransportEvent"] = kit.event(f, 8, "07:45:00", "Customs looked at the seals at the border, "
                                                       "the morning after the truck arrived there.",
                                                       description="Seal check, no inspection of the goods.",
                                                       location={"Name": V("Road border crossing Urvania–Bayvarra",
                                                                           "Where customs checked the seals.")})
    else:           # the consignment note is made out at takeover, before the truck leaves (road/08#F1, C72)
        stage["EstimatedDepartureTransportEvent"] = kit.event(f, 7, ROAD_DEPARTS + ":00", "Expected once customs has "
                                                              "released the export declaration and the truck may "
                                                              "leave.", kit.place("XUFER", "Castrano Logistics "
                                                                                           "warehouse."))
    return stage


def road_loading_length(f):
    """The trailer floor the load takes, in metres: the bench pallets two high and three abreast in rows of the
    pallet's length, the pallet of frame cartons in a row of its own (D20)."""
    units = kit.pallets(f, f.deal)
    bench = [it for _, it, _ in units if it.get("parcels")]
    rows = -(-len(bench) // (2 * 3)) + (len(units) > len(bench))
    return kit.kg((Decimal(rows) * Decimal(units[0][1]["pallet"]["mm"][0]) / 1000).quantize(Decimal("0.1"),
                                                                                       rounding="ROUND_UP"))


def road_consignment(f, view):
    """The consignment of the truck. view: 'request' (the booking), 'plan' (the carrier's answer) or 'note' (the
    consignment note when the goods are taken over)."""
    d = f.deal
    net = sum(Decimal(str(x["ordered"])) * Decimal(str(ITEM[x["item"]]["net_kg"])) for x in d)
    out = {"ID": V(f.numbers["consignment"], "The distributor's consignment number, from its booking."),
           "SummaryDescription": V("Park benches and spare side frames on 25 pallets.", "The goods in a few words, "
                                                                                       "as on the consignment note."),
           "GeneralCargoIndicator": V("true", "Packed goods on pallets."),
           "ContainerizedIndicator": V("false", "The pallets are loaded on the truck, not in a container."),
           "OriginalDepartureCountry": {"IdentificationCode": V("XU", "The goods start in Urvania.")},
           "FinalDestinationCountry": {"IdentificationCode": V("XB", "And end in Bayvarra.")}}
    if view == "request":
        out["RequestedPickupTransportEvent"] = kit.event(f, 7, "14:00:00", "The day the goods are ready.",
                                                         kit.place("XUFER", "The 3PL's warehouse."))
        out["RequestedDeliveryTransportEvent"] = kit.event(f, 9, "10:00:00", "By the end of the distributor's goods-in slot, 09:00 to 10:00.",
                                                           kit.place("XBMRW", "The distribution centre."))
        out["CarrierServiceInstructions"] = V("Curtain-side trailer; the goods are loaded from the side by forklift.",
                                              "What the carrier must bring.")
        # what the carrier plans the trailer by: the pallets and the floor they take (road/03#F9)
        out["TotalTransportHandlingUnitQuantity"] = qty(len(kit.pallets(f, d)), "EA", "The pallets to collect: 24 of "
                                                        "benches and one of frame cartons.")
        out["LoadingLengthMeasure"] = V(road_loading_length(f), "The bench pallets go two high, three abreast, in "
                                        "four rows of 1.85 m, and the pallet of frame cartons in a fifth row: that "
                                        "much of the trailer floor is needed.", unitCode="MTR")
        return out
    out.update({
        "CarrierAssignedID": V(ROAD_JOB, "The carrier's job number."),
        # no ConsignorAssignedID: the despatch advice is the 3PL's document, not a consignment number of the
        # consignor's (road/08#F11)
        "ConsigneeAssignedID": V("LD-GI-0412", "The distributor's goods-in booking for the slot."),
        "NetWeightMeasure": qty(net, "KGM", "The weight of the goods without packaging."),
        "LoadingLengthMeasure": V(road_loading_length(f), "The 24 bench pallets two high, three abreast, in four rows "
                                  "of 1.85 m, and the pallet of frame cartons in a fifth row: that much of the 13.6 m "
                                  "floor.", unitCode="MTR"),
        "Remarks": V("Received in apparent good order; trailer doors sealed by the 3PL, seal as recorded.",
                     "The driver's remarks at taking over, as the consignment note asks; the seal's number is in the "
                     "trailer's own seal element (road/08#F26)."),
        "ThirdPartyPayerIndicator": V("false", "The consignee, who booked the truck, pays the freight."),
        "HaulageInstructions": V("Wait at the warehouse until customs has released the export declaration.",
                                 "What the driver must do before leaving."),
        "CustomsClearanceServiceInstructions": V("The export is declared by the seller in Ferrano; the import by the "
                                                 "distributor at the border.", "Who clears the goods through customs."),
        "DeliveryInstructions": V("Enter by gate 3 of the business park and report to the gatehouse; unload at "
                                   "dock 4.", "Where to go on arrival."),
        "TotalPackagesQuantity": qty(kit.parcel_count(f, d), "EA", "The parcels: 96 benches in three parcels each "
                                     "and 12 frame cartons (D20)."),
        "TotalTransportHandlingUnitQuantity": qty(len(kit.pallets(f, d)), "EA", "The pallets they travel on: 24 of "
                                                  "benches and one of frame cartons."),
        "ActualPickupTransportEvent": kit.event(f, 7, "15:05:00", "When the carrier took over the goods.",
                                                kit.place("XUFER", "The 3PL's warehouse.")),
        "DeliveryTerms": {"ID": V("FCA", "Incoterms 2020: free carrier at the seller's warehouse."),
                          "LossRiskResponsibilityCode": V("BUYER", "The risk passed to the buyer when the goods were "
                                                                   "loaded on the truck."),
                          "LossRisk": V("The risk passes on loading at the 3PL's warehouse.", "In words."),
                          "SpecialTerms": V("The buyer's carrier presents the truck; the seller loads it.",
                                            "Who loads, under FCA at the seller's premises.")},
        "CollectPaymentTerms": {"Note": V("The freight is paid by the consignee under its contract with the carrier.",
                                          "Freight collect: the consignee pays.")},
        "CustomsDeclaration": {"ID": V(f.numbers["export-declaration"], "The export declaration the goods travel "
                                                                        "under."),
                               "IssuerParty": party("5-xu", short=True)},     # the declarant (road/08#F5, D46)
        "MainCarriageShipmentStage": road_stage(f, False),
        # the 25 pallets travel in the sealed trailer: the trailer is the transport equipment, with its seal and its
        # empty weight, and the pallets are the handling units packed in it (road/08#F26, D35)
        "TransportHandlingUnit": {"TransportEquipment": road_trailer(f, kit.handling_units(f, d, "8-xu",
                                                                                          "LD MARROWDALE",
                                                                                          detail=True))}})
    return out


def road_trailer(f, pallets):
    """The carrier's curtain-side trailer as transport equipment: its plate, its tare from the fleet, the 3PL's seal
    on the doors, and the pallets loaded in it."""
    v = kit.fleet("13-xu", "T-07")
    return {"ID": V(v["trailer"], "The trailer, by its licence plate.",
                    schemeID="urn:ubl-examples:world:XU:vehicle-register"),
            "TransportEquipmentTypeCode": V("TE", "UN/EDIFACT 8053 code TE: trailer."),
            "Description": V("Curtain-side semi-trailer, 13.6 m loading length", "The trailer in words."),
            "TareWeightMeasure": qty(v["tare_kg"]["trailer"], "KGM", "The trailer's empty weight, from the carrier's "
                                                                    "fleet (world/parties.json)."),
            "TransportEquipmentSeal": {"ID": V("XU-CL-77310", "The number of the bolt seal on the trailer doors."),
                                       "SealIssuerTypeCode": V("SHIPPER", "The seal is the 3PL's, which loads for "
                                                                          "the consignor."),
                                       "SealingPartyType": V("Shipper", "Put on by the 3PL when the trailer was "
                                                                        "loaded."),
                                       "SealStatusCode": V("APPLIED", "In place when the carrier took over the "
                                                                      "goods.")},
            "PackagedTransportHandlingUnit": pallets}


def road(n, doc):
    f = ROAD
    weight = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The distributor orders for its spring stock.",
                         "Free carrier at the seller's warehouse: the buyer arranges and pays the main transport, so the "
                         "order names the warehouse where the goods are collected and the carrier that collects them "
                         "(UBL rule IND6: the delivery terms are stated, not implied).",
                         "Castrano Logistics warehouse, Conciaro",
                         {"Delivery": {
                             "ID": V("LD-DL-26-0412", "The distributor's number for this delivery."),
                             "Quantity": qty(108, "EA", "All 108 pieces in one delivery."),
                             "MinimumQuantity": qty(108, "EA", "No part deliveries: the truck is booked for all."),
                             "MaximumQuantity": qty(108, "EA", "And no more than ordered."),
                             "DeliveryAddress": address("6-xb", register=True),
                             "DeliveryLocation": {**kit.gln_location("6-xb", "goodsin"),
                                                  "Description": V(PARTY["6-xb"]["identity"]["identification"]
                                                                   ["locations"]["goodsin"]["description"] + ".",
                                                                   "Where the truck unloads; the gate belongs here, "
                                                                   "not in the postal address (world/parties.json).")},
                             "AlternativeDeliveryLocation": {"Description": V(
                                 "Dock 6 of the same goods-in, if dock 4 is blocked.", "Where to go instead.")},
                             "MinimumDeliveryUnit": {"BatchQuantity": qty(4, "EA", "Benches come in pallets of "
                                                                                    "four."),
                                                     "ConsumerUnitQuantity": qty(1, "EA", "One bench.")},
                             # no MaximumDeliveryUnit: one delivery of 108 pieces has no upper batch (road/01#F11)
                             "Despatch": {
                                 "RequestedDespatchDate": V(f.date(7), "The day the buyer's truck will collect."),
                                 "RequestedDespatchTime": V("14:00:00", "In the afternoon."),
                                 "RequestedDespatchPeriod": {"StartDate": V(f.date(7), "The collection day."),
                                                             "StartTime": V("13:00:00", "From one."),
                                                             "EndTime": V("17:00:00", "Until five.")},
                                 "Instructions": V("Have the export declaration ready when the truck arrives.",
                                                   "What the seller must do for the collection."),
                                 "DespatchAddress": address("8-xu"),
                                 "DespatchLocation": {"Description": V("Loading bays 1–3 of the warehouse.",
                                                                       "Where the truck is loaded.")},
                                 "Contact": {"Name": V("Warehouse office", "Whom the driver reports to."),
                                             "Telephone": V(PARTY["8-xu"]["identity"]["contact"]["telephone"],
                                                            "The office's number.")}}}})
    if doc["doc"] == "OrderResponse":
        out = kit.order_response(f, n, doc, 1, "The manufacturer answers the next day.")
        out["Delivery"] = {"PromisedDeliveryPeriod": {"StartDate": V(f.date(7), "Under FCA delivery is the handover "
                                                                                "to the buyer's carrier: on day 7."),
                                                      "EndDate": V(f.date(8), "Or the morning after, by the "
                                                                              "guaranteed despatch (road/02#F4).")},
                           "Despatch": {
                               "EstimatedDespatchDate": V(f.date(7), "The goods will be ready on the requested day."),
                               "EstimatedDespatchTime": V("14:00:00", "At the requested time."),
                               "GuaranteedDespatchDate": V(f.date(8), "At the latest the next day."),
                               "GuaranteedDespatchTime": V("12:00:00", "By noon."),
                               "EstimatedDespatchPeriod": {"StartDate": V(f.date(7), "The afternoon of day 7."),
                                                           "EndDate": V(f.date(8), "Or the morning after.")},
                               # the party that picks the goods up: the buyer's carrier (road/02#F5)
                               "ResponsibleParty": party("13-xu", short=True),
                               "NotifyParty": party("6-xb", short=True)}}
        bench, frame = ITEM["bench-serra"], ITEM["bench-casting"]
        out["OrderResponseCode"] = V("CA", "UN/EDIFACT 4343 code CA: conditionally accepted, with the substitution "
                                           "of line 2.")
        out["Note"] = V("Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the "
                        "same price.", "The condition in words.")
        out["OrderLine"] = [
            {"LineItem": {"ID": V("1", "The benches."), "Quantity": qty(96, "EA", "As ordered."),
                          "Item": {"Name": V(bench["name"], "Named only."),
                                   "SellersItemIdentification": {"ID": V(bench["sellers_id"], "The seller's "
                                                                                              "number.")}}},
             "OrderLineReference": {"LineID": V("1", "The order line.")}},
            {"LineItem": {"ID": V("2", "The side frames, as ordered."),
                          "LineStatusCode": V("Revised", "Changed by the seller."),
                          "Quantity": qty(12, "EA", "As ordered."),
                          "Item": {"Name": V(frame["name"], "The frame ordered."),
                                   "SellersItemIdentification": {"ID": V(frame["sellers_id"], "Its number.")}}},
             "SubstitutionStatusCode": V("Substitution", "The line is delivered with a substitute item."),
             "Note": V("Same fit and price; the old casting is no longer made.", "Why the substitute is offered."),
             "SellerSubstitutedLineItem": {
                 "ID": V("2", "The substitute for line 2."),
                 "Quantity": qty(12, "EA", "The same quantity."),
                 "Price": kit.price_block("bench-casting", buyer=f.buyer),
                 "Item": {"Name": V("Bench side frame casting, 2026", "The substitute."),
                          "SellersItemIdentification": {"ID": V(frame["sellers_id"], "The same item number."),
                                                        "ExtendedID": V(ROAD_CASTING, "The new version, the 2026 "
                                                                                      "casting: every later document "
                                                                                      "of the flow identifies the "
                                                                                      "frame so (D35 point 3).")}}},
             # no proposed substitute: the 2026 casting is the substitute, decided; the old casting is no longer made
             # (road/02#F6, D35 point 3)
             "OrderLineReference": {"LineID": V("2", "The order line."),
                                    "SalesOrderLineID": V("2", "The seller's line.")}}]
        return out
    if doc["doc"] == "TransportExecutionPlanRequest":
        out = kit.tep_request(f, n, doc, 1, "The distributor books the truck once the order is accepted.", 7, weight,
                              "The gross weight of the order: benches and castings with their packaging.")
        kit.deep_merge(out["Consignment"], road_consignment(f, "request"))
        del out["Note"]      # the leg's description is a caption of the example, not a message to the carrier (road/03#F5)
        return out
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 7, "The day the 3PL loaded the truck.",
                                   "The gross weight loaded, packaging included.",
                                   {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                         "The distributor's consignment for the "
                                                                         "truck.")},
                                                 "Delivery": {"Despatch": {
                                                     "ID": V("CL-OUT-26-0871", "The 3PL's outbound number."),
                                                     "ActualDespatchDate": V(f.date(7), "Loaded and gone."),
                                                     "ActualDespatchTime": V("15:05:00", "The carrier took over "
                                                                             "the loaded goods: the despatch is the "
                                                                             "pickup (road/04#F1).")}}}})
    if doc["doc"] == "ExportCustomsDeclaration":
        return {"ID": V(f.number("export", doc["from"], "ExportCustomsDeclaration"), "The exporter's reference."),
                "IssueDate": V(f.date(7), "Declared the day the goods leave the warehouse for the border."),
                "CustomsDeclaration": {
                    "ID": V(f.number("export-declaration", doc["from"], "CustomsDeclaration"),
                            "The declaration as lodged with Urvania's customs."),
                    "Shipment": {"ID": V(f.numbers["shipment"], "The shipment of the despatch advice."),
                                 "GrossWeightMeasure": qty(weight, "KGM", "The gross weight leaving the country."),
                                 "GoodsItem": goods_items(f, "XUF", "The value at the frontier: the invoice value, in "
                                                                     "ferra."),
                                 "Consignment": {"ID": V(f.numbers["consignment"], "The consignment of the truck.")}}}}
    if doc["doc"] == "CertificateOfOrigin":
        # D35 point 2: Valdara's application (06) and the chamber's certificate (07) are two documents with their own
        # numbers; the chamber, the body Urvania authorises under the Accord to issue proofs of preferential origin,
        # is the only endorser; its e-certificate system gives the application a job number when it is lodged
        chamber, exporter = "20-xu", "5-xu"
        endorsed = doc["from"] == chamber
        certificate = f.number("certificate", chamber, "CertificateOfOrigin")
        application = f.number("certificate-application", exporter, "Application")
        signer = {"RoleCode": V("CHAMBER", "The endorser is the chamber of commerce of the exporting country, the "
                                           "body Urvania authorises under the Accord to issue proofs of preferential "
                                           "origin (D35)."),
                  "SequenceNumeric": V("1", "The first and only endorsement: a certificate between Accord members "
                                            "needs no legalisation."),
                  "Party": party(chamber),
                  "SignatoryContact": {"Name": V("Certificates office", "The office of the chamber that signs "
                                                 "certificates of origin. UBL defines this contact as the exporter's "
                                                 "signer of the application; the element is mandatory in an "
                                                 "endorser party, so it names the endorser's signer, a finding for "
                                                 "the UBL TC (road/06#F15, O121)."),
                                       "JobTitle": V("Certificates officer", "The signing function: the officer who "
                                                                             "signs certificates for the chamber "
                                                                             "(road/06#F16).")}}
        return {
            "EndorserParty": {k: v for k, v in signer.items() if k != "Party"},
            "ID": V(certificate, "The number of the certificate, given by the chamber.") if endorsed else
                  V(application, "The exporter's number for its application (road/06#F1)."),
            "VersionID": V("1", "The first version of the certificate." if endorsed else
                                "The first version of the application."),
            "IssueDate": V(f.date(7 if endorsed else 4), "The day the chamber issued the certificate: Monday "
                           "morning, before the export declaration (road/07#F11, D27)." if endorsed
                           else "The day the exporter applies, before the goods leave."),
            "Description": V("Certificate of origin for park benches and castings made in Urvania." if endorsed else
                             "Application for a certificate of origin for park benches and castings made in "
                             "Urvania.", "What the document is for."),
            "CertificateOfOriginApplication": {
                "ReferenceID": V(application, "The exporter's reference for its application."),
                "CertificateType": V("Preferential", "The goods qualify for the preferential duty rate in Bayvarra; "
                                                     "the importer needs this certificate to claim it."),
                "ApplicationStatusCode": V("APPROVED" if endorsed else "SUBMITTED",
                                           "The chamber has approved the application." if endorsed
                                           else "The exporter submits the application."),
                "OriginalJobID": V(ROAD_CO_JOB, "The job number the chamber's e-certificate system gave the "
                                                "application when it was lodged, by which it tracks amendments; "
                                                "not the buyer's order (road/06#F7, D35)."),
                "Shipment": {"ID": V(f.number("shipment", "8-xu", "Shipment"), "The shipment the certificate covers."),
                             "GoodsItem": goods_items(f, "XUF", "The value of the goods, in ferra.")},
                "EndorserParty": signer,
                "PreparationParty": party(exporter),
                "IssuerParty": party(chamber),
                "IssuingCountry": {"IdentificationCode": V("XU", "The goods were made in Urvania, and the certificate is "
                                                                 "issued there.")}},
            "IssuerEndorsement": {
                "DocumentID": V(f"{ROAD_CO_JOB}-E1", "The identifier of this endorsement: the first of the chamber's "
                                                      "job."),
                "ApprovalStatus": V("Approved" if endorsed else "Pending", "The chamber has endorsed the certificate."
                                    if endorsed else "Not yet endorsed: the application is with the chamber."),
                "EndorserParty": signer}}
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 7, "Issued when the carrier collects the goods at the warehouse.", weight,
                          "The gross weight the carrier takes over.")
        net = sum(Decimal(str(x["ordered"])) * Decimal(str(ITEM[x["item"]]["net_kg"])) for x in f.deal)
        kit.deep_merge(out["Shipment"], {
            "NetNetWeightMeasure": qty(net, "KGM", "The goods alone, without any packaging."),
            "GrossVolumeMeasure": V(kit.kg(kit.pallets_volume(f)), "The volume of the 25 loaded pallets.",
                                    unitCode="MTQ"),
            "TotalGoodsItemQuantity": qty(2, "EA", "Two kinds of goods, the goods items below: benches and side "
                                                  "frames."),
            # the goods as the consignment note describes them: nature, quantity and gross weight (road/08#F25)
            "GoodsItem": [{"ID": V(str(i), "The goods item number, as in the export declaration."),
                           "Description": V(ITEM[x["item"]]["name"], "What the goods are, in words."),
                           "Quantity": qty(x["ordered"], ITEM[x["item"]]["unit"], "The pieces taken over."),
                           "GrossWeightMeasure": qty(kit.line_gross(f, x, "ordered"), "KGM",
                                                     "Their gross weight in their parcels, with the pallets they "
                                                     "travel on.")}
                          for i, x in enumerate(f.deal, 1)],
            "SplitConsignmentIndicator": V("false", "The whole consignment travels on this truck."),
            "ConsignmentQuantity": qty(1, "EA", "One consignment on the truck."),
            "HandlingCode": V("KEEPDRY", "The carrier's handling code: keep dry, for the goods travel in cardboard "
                                         "cartons."),
            "Information": V("Park benches, knocked down, and spare side frames, for resale.", "What the goods are, "
                                                                                              "for the driver."),
            "ExportCountry": {"IdentificationCode": V("XU", "The goods are exported from Urvania.")},
            "OriginAddress": address("8-xu"),
            "ReturnAddress": address("8-xu"),
            "Consignment": road_consignment(f, "note"),
            "Delivery": {"TrackingID": V(ROAD_JOB, "Track the truck with the carrier's job number."),
                         "EstimatedDeliveryPeriod": {"StartDate": V(f.date(9), "The morning of the third day."),
                                                     "StartTime": V("09:00:00", "From nine, when the slot opens."),
                                                     "EndTime": V("10:00:00", "Until ten, when it closes.")},
                         "LatestDeliveryDate": V(f.date(9), "The goods-in slot cannot move."),
                         "LatestDeliveryTime": V("10:00:00", "The end of the slot, the time the delivery is required "
                                                             "by (road/08#F14).")}})
        del out["Description"]   # the leg's description is a caption of the example (road/08#F18)
        return out
    if doc["doc"] == "TransportationStatus":
        border = {"Name": V("Land border crossing Urvania–Bayvarra",
                            "The road border crossing between the customs posts of both countries.")}
        return {"ID": V(f.number("status", doc["from"], "TransportationStatus"), "The carrier's status report number."),
                "IssueDate": V(f.date(8), "The morning after collection, when the truck has crossed the border."),
                "IssueTime": V(wmap.hm(wmap.after(wmap.at(f.date(8), ROAD_CLEARED), .25)), "Sent as soon as the truck "
                                                                                         "was through."),
                "TransportationStatusTypeCode": V("PROGRESS", "A report on the progress of the carriage."),
                "TransportEvent": kit.event(
                    f, 8, ROAD_CLEARED + ":00", "The day and time the truck crossed the land border.", border,
                    type_code="BORDERCROSS", ident=f"{ROAD_JOB}-E03",
                    description="Border crossing passed; customs cleared on both sides.", done=True,
                    Period={"StartTime": V("07:30:00", "The truck joined the queue at the border, after the driver's "
                                                       "night rest in the border truck park: it arrived about "
                                                       f"{wmap.about(ROAD_AT_BORDER)} the evening before, when the "
                                                       "importer's customs desk was closed."),
                            "EndTime": V(ROAD_CLEARED + ":00", "And left the customs post, once the import "
                                                              "declaration, lodged when the importer's desk opened, "
                                                              "was accepted.")},
                    ResponsibleParty=party("13-xu", short=True),
                    ReportedShipment={"ID": V(f.numbers["shipment"], "The shipment the event concerns.")},
                    Signature={"ID": V("XB-CUS-SIG-0884", "The border customs' release stamp, as an electronic "
                                                         "signature."),
                               "ValidationDate": V(f.date(8), "Signed at the border."),
                               "SignatoryParty": party("19-xb", short=True)},
                    Contact={"Name": V("Planning desk", "Whom to call about the truck."),
                             "Telephone": V(PARTY["13-xu"]["identity"]["contact"]["telephone"], "The planners' "
                                                                                                   "number.")},
                    CurrentStatus={
                        "ConditionCode": V("ONTIME", "The carriage runs to plan."),
                        "ReferenceDate": V(f.date(9), "The delivery the status is measured against."),
                        "ReferenceTime": V("10:00:00", "The end of the goods-in slot, the time delivery is required by."),
                        "Description": V("In transit in Bayvarra, expected at the distribution centre on time.",
                                         "The status in words."),
                        "StatusReasonCode": V("CLEARED", "Why: the border is behind it."),
                        "StatusReason": V("Customs released the goods at the border.", "In words."),
                        "SequenceID": V("3", "The third report on this truck: collection, departure, border."),
                        "Text": V(f"Expected in Marrowdale about {wmap.about(ROAD_IN_MARROWDALE)}, after the morning "
                                  "goods-in slots; the truck waits at the business park for its slot tomorrow, "
                                  "09:00 to 10:00, and the driver takes his rest there.", "A note for the consignee."),
                        "Percent": V(str(wmap.whole(100 * ROAD_BORDER_KM / ROAD_LEG_KM)),
                                     f"The share of the route driven: {wmap.whole(ROAD_BORDER_KM)} of "
                                     f"{DISTANCE_KM} km."),
                        "ReliabilityPercent": V("90", "How sure the carrier is of the arrival time."),
                        "Condition": {"AttributeID": V("SEAL", "The condition checked."),
                                      "Description": V("Intact, as checked by customs.", "Its state.")},
                        "DocumentationAttachment": {"ExternalReference": {
                            "URI": V("https://www.trasvia.example/tracking/TH-26-04471/seal.jpg", "A photograph of "
                                                                                                  "the seal."),
                            "MimeCode": V("image/jpeg", "A photograph.")}},
                        "SubStatus": {"ConditionCode": V("RELEASED", "The customs part of the status."),
                                      "Description": V("Import declaration accepted by Bayvarra's customs.",
                                                       "In words.")}}),
                "Consignment": {"ID": V(f.numbers["consignment"], "The consignment the report is about."),
                                "CarrierAssignedID": V(ROAD_JOB, "The carrier's job number."),
                                # the departure and the seal check, as done: the waybill was made out before them
                                "MainCarriageShipmentStage": {
                                    **{k: v for k, v in road_stage(f, True).items()
                                       if k in ("ID", "TransportModeCode", "ActualDepartureTransportEvent",
                                                "ExaminationTransportEvent")}},
                                "Status": {"ConditionCode": V("INTRANSIT", "The consignment is on its way."),
                                           "Description": V("All 25 pallets on board.", "Nothing left behind.")}}}
    if doc["doc"] == "ImportCustomsDeclaration":
        return {"ID": V(f.number("import", doc["from"], "ImportCustomsDeclaration"), "The importer's declaration "
                                                                                    "number."),
                "IssueDate": V(f.date(8), "Declared when the goods arrive in Bayvarra."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment of the despatch advice."),
                             "GrossWeightMeasure": qty(weight, "KGM", "The gross weight arriving."),
                             "GoodsItem": [{**g, "DespatchLineReference": {
                                 "LineID": V(g["ID"].value, "The despatch advice line of these goods."),
                                 "DocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}}}
                                 for g in goods_items(f, "XBL", "The customs value in lume, Bayvarra's currency: the "
                                                                "invoice value in ferra at the world's reference rate "
                                                                "(1 ferra = 0.01 lume).", convert=True)]},
                "AdditionalDocumentReference": {"ID": V(f.numbers["certificate"], "The certificate of origin, to claim "
                                                                                  "the preferential duty rate.")}}
    if doc["doc"] == "ReceiptAdvice":
        out = kit.receipt_advice(f, n, doc, 9, "The day the truck was unloaded at the distribution centre.")
        out["Shipment"] = {"ID": V(f.numbers["shipment"], "The shipment received."),
                           "Delivery": {"ActualDeliveryDate": V(f.date(9), "Unloaded at dock 4."),
                                        "ActualDeliveryTime": V("09:40:00", "Within the slot.")}}
        given = out.get("AdditionalDocumentReference")
        out["AdditionalDocumentReference"] = ([given] if isinstance(given, dict) else given or []) + [
            {"ID": V(f.numbers["waybill"], "The consignment note signed on delivery, the consignee's proof of "
                                           "receipt: a transport document, not a delivery note (road/11#F2).")}]
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "13-xu":
        return kit.invoice(f, n, doc, 9, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note of the "
                                                                                          "carriage invoiced.")}},
                           [{"item": "road-transport", "qty": DISTANCE_KM,
                             "invoice_why": "The kilometres driven loaded, from the 3PL's warehouse in Conciaro "
                                            "to the distribution centre in Marrowdale: the truck's leg on the map "
                                            f"({ROAD_LEG_KM:.1f} km, O152)."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {
                               "ID": V(f.numbers["consignment"], "The consignment carried, as the distributor numbered "
                                                                 "it when booking the truck."),
                               "ActualDeliveryTransportEvent": kit.event(f, 9, "09:40:00", "Delivered at dock 4: the "
                                                                         "carriage invoiced is complete.",
                                                                         location=LUMEWAY_GOODS_IN)}}}})
        # the carrier's proof of delivery is its own: the consignment note and the delivery event; the consignee's
        # receipt advice comes a day later, after the invoice (road/14#F1, C72)
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 8, "Issued when the goods have left the warehouse.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice of the "
                                                                                         "goods invoiced.")},
                            "PaymentExchangeRate": {
                                "SourceCurrencyCode": V("XUF", "The invoice currency."),
                                "TargetCurrencyCode": V("XBL", "The buyer's currency, from which it pays."),
                                "CalculationRate": V("0.01", "The world's reference rate, for the buyer's "
                                                             "information: its bank converts at the day's rate."),
                                "MathematicOperatorCode": V("Multiply", "Ferra times the rate gives lume."),
                                "Date": V(f.date(8), "The invoice date.")}})
    if doc["doc"] == "RemittanceAdvice":
        # Lumeway pays within the ten days of Valdara's standard terms and takes the 2 % (O218): Thursday 2 April,
        # a working day in both countries, the last before the discount period ends on 3 April
        out = kit.remittance(f, n, doc, 17, "The day the payment is made across the border, within the ten days "
                                            "of the invoice's discount period (O218).", discount="2")
        # the alias "receivables" names the account as Lumeway's payee account; paying from it, the name is given
        # and stands for itself (road/17#F8)
        out["PaymentMeans"]["PayerFinancialAccount"].pop("AliasName", None)
        return out
    raise SystemExit(f"road scenario: no document {n} {doc['doc']}")


SCENARIOS = {"ore": ore, "road": road}


# ---------------------------------------------------------------- the rail flow (Urvania -> Bayvarra, DAP, transit)
RAIL = kit.Flow("rail", "2026-04-06", [
    {"item": "bench-serra", "ordered": 192, "why": "Two containers of 24 pallets, 4 benches on each pallet."}],
    buyer="6-xb")


RAIL_BOXES = [kit.container_number("FRX", 104417), kit.container_number("FRX", 104418)]
RAIL_SEALS = ["XU-VI-30411", "XU-VI-30412"]
# when each order wants its goods (worklist C28): (first day, last day) from the flow's start, and why
REQUESTED_DELIVERY = {
    ("air", 1): (3, 3, "The frames are wanted at Selanu airport on 14 May, before the ship arrives."),
    ("cotton", 8): (28, 28, "Free on board Selanu: the bales are wanted on board the ship of 2 March."),
    ("furniture", 8): (21, 21, "The opening stock is wanted on 23 March: the maker makes the line in one run, and "
                                "the store holds it for the reopening of its home and garden department on 11 May."),
    ("furniture", 10): (119, 123, "The repeat order for the winter is wanted in the first week of July."),
    ("furniture", 15): (37, 37, "The desks are wanted on 8 April, when the installers come."),
    ("mast", 1): (3, 4, "The equipment is wanted at the mast site on 4 or 5 June."),
    ("packaging", 1): (3, 5, "The film is wanted from 30 April to 2 May, before the next packing run."),
    ("packaging", 3): (4, 6, "The bags are wanted from 1 to 3 May."),
    ("packaging", 5): (15, 16, "The shirts are wanted on 12 or 13 May."),
    ("plastics", 1): (7, 11, "The granulate is wanted at the river quay from 20 to 24 April."),
    ("rail", 1): (9, 10, "The containers are wanted at the siding on 15 or 16 April."),
    ("retail", 8): (10, 10, "The benches are wanted on 30 April, in a delivery slot."),
    ("sea", 5): (14, 17, "The benches are wanted at Selanu from 18 to 21 May."),
    ("tender", 26): (78, 78, "The first release is wanted at the depot on 31 March."),
    ("tender", 27): (78, 78, "The change keeps the delivery of 31 March."),
    ("wood", 3): (10, 18, "The slats are wanted at the factory from 26 February to 6 March."),
    ("wood", 10): (21, 25, "The timber is wanted in the week of 9 March."),
}

# where the rail flow's events happen (worklist C18): every event names its place
LUMEWAY_GOODS_IN = {**kit.gln_location("6-xb", "goodsin"), "Name": V("Lumeway goods-in, Marrowdale", "Where the "
                                                                      "goods are unloaded.")}
RAIL_WAREHOUSE = kit.place("XUFER", "At the 3PL's warehouse in Conciaro, where the boxes are packed.",
                           name="Castrano Logistics warehouse, Conciaro")
RAIL_HUB = kit.place("XUFER", "At the intermodal hub, where the boxes go on the train.", name="Ferrano Intermodal Hub")
RAIL_STACK = kit.place("XUFER", "The hub's stack where the boxes wait for the train.",
                       name="Ferrano Intermodal Hub, stack C")
RAIL_BORDER = {"Name": V("Rail border station Urvania–Bayvarra", "Where the train crosses the border.")}
RAIL_SIDING = {**kit.gln_location("6-xb", "siding"), "Name": V("Lumeway rail siding, Marrowdale", "Where the boxes "
                                                                 "are placed for unloading.")}


# the train on the map (O152): the rail leg from the hub to Lumeway's siding, and the border station on it; a container
# train averages about 50 km/h. It stops at the border station for the crew change, the brake test and the customs'
# check of the seals, and leaves on its timetabled path into Bayvarra; in Marrowdale the boxes are placed on the
# siding by the next morning's shunting trip, once Lumeway has declared the import (D37).
RAIL_KM = wmap.leg_km("rail", "18-xu", "6-xb", "rail")
RAIL_BORDER_KM = wmap.border_km("rail", "18-xu", "6-xb", "rail")
RAIL_ROAD_KM = wmap.leg_km("rail", "8-xu", "18-xu", "road")        # the carrier's haulage to the hub
TRAIN_KMH = 50
RAIL_LEAVES, RAIL_BORDER_LEAVES = "06:52", "13:00"      # the actual departure from the hub; the border path's
RAIL_AT_BORDER = wmap.after(wmap.at("2026-04-14", RAIL_LEAVES), RAIL_BORDER_KM / TRAIN_KMH)
RAIL_AT_BORDER_PLANNED = wmap.after(wmap.at("2026-04-14", "06:45"), RAIL_BORDER_KM / TRAIN_KMH)
RAIL_IN_MARROWDALE = wmap.after(wmap.at("2026-04-14", RAIL_BORDER_LEAVES), (RAIL_KM - RAIL_BORDER_KM) / TRAIN_KMH)
if not (RAIL_AT_BORDER.hour < 13 and RAIL_IN_MARROWDALE.date().isoformat() == "2026-04-14"):
    raise SystemExit("rail: the train's times no longer fit the leg on the map (O152)")
# the carrier's one tractor brings the two boxes from the warehouse to the hub in two runs, and before that the two
# empties to the warehouse (D37: carrier haulage, a pre-carriage stage of the same contract); per box: (day, time)
TRUCK_KMH = 55
RAIL_ROAD_H = RAIL_ROAD_KM / TRUCK_KMH
RAIL_PICKUP = [(7, "13:00"), (7, "15:00")]
RAIL_AT_HUB = [wmap.hm(wmap.after(wmap.at(RAIL.date(d), t), RAIL_ROAD_H))[:5] for d, t in RAIL_PICKUP]
RAIL_STACKED = [wmap.hm(wmap.after(wmap.at(RAIL.date(d), t), RAIL_ROAD_H + 0.17))[:5] for d, t in RAIL_PICKUP]
RAIL_POSITIONED = [(4, "08:00"), (4, "10:00")]
RAIL_LIFTED = ["05:40", "05:55"]
if wmap.after(wmap.at(RAIL.date(4), RAIL_POSITIONED[0][1]), 2 * RAIL_ROAD_H) > wmap.at(RAIL.date(4),
                                                                                    RAIL_POSITIONED[1][1]) or \
        wmap.after(wmap.at(RAIL.date(7), RAIL_PICKUP[0][1]), 2 * RAIL_ROAD_H) > wmap.at(RAIL.date(7),
                                                                                      RAIL_PICKUP[1][1]):
    raise SystemExit("rail: the tractor cannot make its two runs in the time between them (O152)")
# demurrage (D37, D9, O128): five free days at the siding, counted from the day after the boxes are placed; then the
# framework contract's rate per container day. The first box is emptied on 16 April; the second waits until 22
# April, because the siding's fork-lift is in repair: two container days beyond the free time.
RAIL_EMPTIED = [10, 16]               # days after the flow's start: Thursday 16 April, Wednesday 22 April
RAIL_PLACED = 9                       # Wednesday 15 April
RAIL_FREE_DAYS = 5
DEMURRAGE_XUF = Decimal("7500")       # per container day, the framework contract's rate (O128)
RAIL_DEMURRAGE_DAYS = RAIL_EMPTIED[1] - RAIL_PLACED - RAIL_FREE_DAYS
if RAIL_DEMURRAGE_DAYS != 2 or RAIL_EMPTIED[0] - RAIL_PLACED > RAIL_FREE_DAYS:
    raise SystemExit("rail: the demurrage is no longer two container days on the second box (D37)")
RAIL_CONTRACT = "FRC-CON-2026-005"    # the framework contract for container slots: one number (rail/02#F13, 03#F14)
DEMURRAGE_TEXT = ("Free time five days at the siding, counted from the day after the boxes are placed; "
                  f"then demurrage of {DEMURRAGE_XUF:,.0f} ferra per container day, under framework contract "
                  f"{RAIL_CONTRACT}.")


def rail_container(f, k, full):
    """One of the two 40-foot containers of the rail flow: Ferrano Rail Cargo's own boxes. Both are described alike
    (rail/08#F17, F18)."""
    box, seal = RAIL_BOXES[k], RAIL_SEALS[k]
    wagon = kit.fleet("14-xu", "FRC-4417")["wagons"][k]
    nth = ("first", "second")[k]
    out = {"ID": V(box, "The container's number: owner code, U for a freight container, six digits and the ISO 6346 "
                        "check digit.", schemeID="ISO6346"),
           "ReferencedConsignmentID": V(f.numbers["consignment"], "The consignment the container carries."),
           "TransportEquipmentTypeCode": V("CN", "UN/EDIFACT 8053 code CN: container.", listID="UN/EDIFACT EDED 8053"),
           "SizeTypeCode": V("45G1", "ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose."),
           "FullnessIndicationCode": V("FCL", "A full container load for one consignee."),
           "GrossWeightMeasure": qty(kit.gross_weight(f, "ordered") / 2 + 3900, "KGM", "Half the benches, on their "
                                     "24 pallets, and the "
                                     "container's own 3,900 kg."),
           "TransportEquipmentSeal": {"ID": V(seal, "The number of the bolt seal on the doors."),
                                      "SealIssuerTypeCode": V("SHIPPER", "The seal was issued by the shipper."),
                                      "SealingPartyType": V("Shipper", "And put on by the shipper when it packed "
                                                                       "the container."),
                                      "Condition": V("Intact", "As found at the hub."),
                                      "SealStatusCode": V("APPLIED", "The seal is in place.")}}
    if not full:
        return out
    pday, ptime = RAIL_PICKUP[k]
    out.update({
        "ProviderTypeCode": V("CARRIER", "The rail carrier provides the container."),
        "OwnerTypeCode": V("CARRIER", "And owns it."),
        "DispositionCode": V("LOADED", "Loaded with cargo."),
        "Information": V("Return empty to the Ferrano hub within five days.", "What happens to the box afterwards."),
        "ReturnabilityIndicator": V("true", "The container goes back to its owner."),
        # no Container Convention indicator: nothing in the story says the box's approval status (D37, rail/08#F25)
        "Characteristics": V("Steel, high cube, wooden floor.", "What kind of box it is."),
        "Description": V("40-foot high cube container", "The container in words."),
        **({"DamageRemarks": V("Small dent in the left side panel, noted at pick-up; no effect on the cargo.",
                               "Damage noted when the box was positioned, so it is not blamed on this carriage.")}
           if k == 0 else {}),
        "SpecialTransportRequirements": V("Load with the doors to the rear of the wagon.", "How it rides."),
        "GrossVolumeMeasure": V("76.3", "The inside volume of a 40-foot high cube.", unitCode="MTQ"),
        "TrackingDeviceCode": V("GPS", "The box carries a satellite tracker."),
        "PowerIndicator": V("false", "It needs no power: not a reefer."),
        "TraceID": V(f"TRK-{box}", "The tracker's number."),
        "StowagePositionID": V(f"{wagon} / A", f"The wagon and the slot on it the box rides in: the {nth} container "
                                               "wagon of the train, each box on a wagon of its own."),
        "MeasurementDimension": {"AttributeID": V("LENGTH", "The outside length."),
                                 "Measure": V("12192", "Forty feet.", unitCode="MMT")},
        "OwnerParty": party("14-xu", short=True),
        "ProviderParty": party("14-xu", short=True),
        # no operating party: owner and provider name the carrier, which deploys its boxes (D37, rail/08#F15)
        "LoadingProofParty": party("8-xu", short=True),
        "LoadingLocation": kit.place("XUFER", "Packed at the 3PL's warehouse in Conciaro."),
        "UnloadingLocation": kit.place("XBMRW", "Unpacked at the distributor's siding."),
        "PositioningTransportEvent": kit.event(f, RAIL_POSITIONED[k][0], RAIL_POSITIONED[k][1] + ":00",
                                               "The carrier's tractor delivered the empty box to the warehouse for "
                                               "packing, on the Friday before.", location=RAIL_WAREHOUSE),
        "PickupTransportEvent": kit.event(f, pday, ptime + ":00", f"Collected packed from the warehouse: the {nth} "
                                          "of the tractor's two runs to the hub.", location=RAIL_WAREHOUSE),
        "HandlingTransportEvent": kit.event(f, pday, RAIL_STACKED[k] + ":00", f"Stacked at the hub overnight, "
                                            f"{wmap.whole(RAIL_ROAD_KM)} km from the warehouse.",
                                            location=RAIL_STACK),
        "LoadingTransportEvent": kit.event(f, 8, RAIL_LIFTED[k] + ":00", "Lifted onto its wagon.", location=RAIL_HUB),
        "DeliveryTransportEvent": kit.event(f, RAIL_PLACED, "11:00:00", "Planned arrival at the siding.", done=False,
                                            location=RAIL_SIDING),
        "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The freight for this box."),
                                   "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                   "AllowanceChargeReason": V("Rail freight per container", "In words."),
                                   "Amount": amount(ITEM["rail-container"]["price"]["amount"],
                                                    ITEM["rail-container"]["price"]["currency"],
                                                    "The price of one container slot (world/items.json).")},
        # the wagon is not "contained in" the box: RailCarID and StowagePositionID name it (D37, rail/08#F8)
        "ApplicableTransportMeans": {"RailTransport": {"TrainID": V("FRC 4417", "The train."),
                                                       "RailCarID": V(wagon, "The container wagon it rides on.")}},
        "HaulageTradingTerms": {"Information": V("Carrier haulage: the rail carrier brings the box to the warehouse "
                                                 "and back.", "Who moves the empty box."),
                                "Reference": V("FRC-HT-2026", "The carrier's haulage terms.")},
        "Pickup": {"ActualPickupDate": V(f.date(pday), "Collected."), "ActualPickupTime": V(ptime + ":00", "The "
                                                                                                            "time."),
                   "PickupLocation": {"Name": V("Castrano Logistics warehouse, Conciaro", "Where.")}},
        "Despatch": {"EstimatedDespatchDate": V(f.date(8), "The train is expected to leave the hub that morning; "
                                                           "the consignment note is made out before it leaves "
                                                           "(rail/08#F3)."),
                     "EstimatedDespatchTime": V("06:50:00", "Ten to seven.")},
        "Delivery": {"LatestDeliveryDate": V(f.date(10), "At the latest."),
                     "DeliveryLocation": {**kit.gln_location("6-xb", "siding"),
                                          "Name": V("Rail siding of Lumeway Distribution, Marrowdale", "Where.")}}})
    # no storage location: the box is on the train, and its stack is the place of its handling event (rail/08#F10);
    # no shipment document reference: the waybill it stands in (rail/08#F21)
    return out


def rail_road_stage(f, view):
    """The carrier's haulage of the boxes from the warehouse to the hub: a pre-carriage stage of the same contract
    (D37 point 5, rail/02#F3, 03#F3, 07#F4)."""
    out = {"ID": V("1", "The pre-carriage: the carrier's tractor brings the packed boxes to the hub."),
           "TransportModeCode": V("3", "UN/ECE Recommendation 19 code 3: road transport.",
                                  listID="UNECE Recommendation 19 - Codes for Modes of Transport")}
    if view == "request":
        out["RequestedDepartureTransportEvent"] = kit.event(f, 7, RAIL_PICKUP[0][1] + ":00", "The boxes are packed by "
                                                            "then; the tractor takes them in two runs.",
                                                            location=RAIL_WAREHOUSE)
        out["RequestedArrivalTransportEvent"] = kit.event(f, 7, None, "At the hub the same day, for the morning "
                                                          "train.", location=RAIL_HUB)
        return out
    out["TransportMeans"] = kit.means("14-xu", "FRC-T1")
    out["LoadingPortLocation"] = kit.place("XUFER", "Where the boxes are collected.",
                                           name="Castrano Logistics warehouse, Conciaro")
    out["UnloadingPortLocation"] = kit.place("XUFER", "Where they are handed to the terminal.",
                                             name="Ferrano Intermodal Hub")
    if view == "plan":
        out["PlannedDepartureTransportEvent"] = kit.event(f, 7, RAIL_PICKUP[0][1] + ":00", "The first run leaves "
                                                          "the warehouse.", location=RAIL_WAREHOUSE)
        out["PlannedArrivalTransportEvent"] = kit.event(f, 7, RAIL_AT_HUB[1] + ":00", f"The second box at the hub: "
                                                        f"{wmap.whole(RAIL_ROAD_KM)} km each way, two runs.",
                                                        location=RAIL_HUB)
    if view == "status":
        out["ActualPickupTransportEvent"] = kit.event(f, 7, RAIL_PICKUP[0][1] + ":00", "The carrier's tractor "
                                                      "collected the first box at the warehouse; the second "
                                                      f"followed at {RAIL_PICKUP[1][1]}.", location=RAIL_WAREHOUSE)
        out["ActualArrivalTransportEvent"] = kit.event(f, 7, RAIL_AT_HUB[1] + ":00", "The second box came in at the "
                                                       "hub's gate, the end of the haulage.", location=RAIL_HUB)
    return out


def rail_stage(f):
    out = {"ID": V("2", "The main carriage, by rail."),
           "TransportModeCode": V("2", "UN/ECE Recommendation 19 code 2: rail transport.",
                                  listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
           "TransportMeans": kit.means("14-xu", "FRC-4417", "CT 4471", "The number of the container train in the "
                                                                       "hub's timetable.", "WB"),
           "LoadingSequenceID": V("7", "The order the boxes go on the train: these two are the seventh lift."),
           "SuccessiveSequenceID": V("1", "The first and only rail stage."),
           "Instructions": V("Shunt to the Lumeway siding in Marrowdale once the import is declared.", "What the "
                                                                                                 "railway must do."),
           # container demurrage at a rail siding, under a definition written for vessels: kept, and the definition
           # recorded for the UBL TC (D37, rail/03#F21, 08#F24)
           "DemurrageInstructions": V(DEMURRAGE_TEXT, "What waiting costs: the framework contract's free time and "
                                                      "rate (D37, O128)."),
           "CrewQuantity": qty(2, "IE", "Two persons: a driver and a train manager."),
           # no passenger quantity: a freight train carries none (D37 point 7, rail/03#F20, 08#F22)
           "PlannedDepartureTransportEvent": kit.event(f, 8, "06:45:00", "The timetable departure from the hub.",
                                                       location=RAIL_HUB),
           "PlannedArrivalTransportEvent": kit.event(f, RAIL_PLACED, "10:30:00", "The timetable arrival at the siding "
                                                     f"in Marrowdale: the train reaches Marrowdale yard about "
                                                     f"{wmap.about(RAIL_IN_MARROWDALE)} the day before, "
                                                     f"{wmap.whole(RAIL_KM)} km from the hub, and the next morning's "
                                                     "shunting trip places the boxes on Lumeway's siding.",
                                                     location=RAIL_SIDING),
           "EstimatedDepartureTransportEvent": kit.event(f, 8, "06:50:00", "The departure as expected that morning.",
                                                         location=RAIL_HUB),
           "EstimatedArrivalTransportEvent": kit.event(f, RAIL_PLACED, "10:40:00", "The arrival as expected.",
                                                       location=RAIL_SIDING)}
    out["PlannedWaypointTransportEvent"] = kit.event(f, 8, RAIL_BORDER_LEAVES + ":00", "Planned departure from the "
                                                     f"border station, {wmap.whole(RAIL_BORDER_KM)} km from the hub: "
                                                     f"the train stops there from about "
                                                     f"{wmap.about(RAIL_AT_BORDER_PLANNED)} for the crew change, the "
                                                     "brake test and the customs' check of the seals, and leaves "
                                                     "on its timetabled path into Bayvarra.", location=RAIL_BORDER)
    # the actual departure is reported by the infrastructure manager's progress status (rail/05); the consignment note
    # is made out before the train leaves, so it records no journey (rail/08#F3, C72)
    return out


def rail_offices():
    def office(name, why):
        return {"Name": V(name, why)}
    return {"OfficeOfDepartureLocation": office("Customs office Ferrano Intermodal Hub", "Where the transit starts."),
            "OfficeOfExitLocation": office("Customs post at the rail border station, Urvanian side",
                                           "Where the goods leave Urvania."),
            "OfficeOfTransitLocation": office("Customs post at the rail border station, Bayvarran side",
                                              "Where the transit is checked on entering Bayvarra."),
            "OfficeOfDestinationLocation": office("Customs office Marrowdale", "Bayvarra customs' inland office, "
                                                                               "where the transit ends and the "
                                                                               "goods are declared for import (D37)."),
            "OfficeOfImportLocation": office("Customs office Marrowdale", "Where the import is declared.")}


def rail_consignment(f, view):
    out = {"ID": V(f.numbers["consignment"], "The manufacturer's consignment number."),
           "ContainerizedIndicator": V("true", "Two full containers."),
           "SummaryDescription": V("192 park benches in two 40-foot containers.", "The goods in a few words.")}
    if view == "request":
        out["RequestedPickupTransportEvent"] = kit.event(f, 7, RAIL_PICKUP[0][1] + ":00", "The boxes are packed by "
                                                         "then.", location=RAIL_WAREHOUSE)
        out["RequestedDeliveryTransportEvent"] = kit.event(f, 10, None, "The distributor expects them on day 10.",
                                                           location=RAIL_SIDING)
        out["PreCarriageShipmentStage"] = rail_road_stage(f, "request")
        out["MainCarriageShipmentStage"] = {
            "ID": V("2", "The rail carriage asked for."),
            "RequestedDepartureTransportEvent": kit.event(f, 8, "07:00:00", "The morning train from the hub.",
                                                          location=RAIL_HUB),
            "RequestedWaypointTransportEvent": kit.event(f, 8, None, "Via the border station, where the transit "
                                                                     "is checked.",
                                                         {"Name": V("Rail border station Urvania–Bayvarra", "The "
                                                                                                            "waypoint.")}),
            "RequestedArrivalTransportEvent": kit.event(f, RAIL_PLACED, None, "Arriving the next day.",
                                                        location=RAIL_SIDING)}
        return out
    out["PrepaidPaymentTerms"] = {"Note": V("Freight prepaid by the consignor under DAP.", "The seller pays the "
                                                                                          "carriage.")}
    if view == "plan":       # the plan's contract is the document's own (rail/03#F14): not repeated here
        out["PlannedPickupTransportEvent"] = kit.event(f, 7, RAIL_PICKUP[0][1] + ":00", "The carrier collects the "
                                                       "packed boxes, in two runs.", location=RAIL_WAREHOUSE)
        out["PlannedDeliveryTransportEvent"] = kit.event(f, RAIL_PLACED, "11:00:00", "And places them at the siding.",
                                                         location=RAIL_SIDING)
        out["PreCarriageShipmentStage"] = rail_road_stage(f, "plan")
        out["MainCarriageShipmentStage"] = rail_stage(f)
        return out
    out["TransportContract"] = {"ID": V(RAIL_CONTRACT, "The framework contract for container slots."),
                                "IssueDate": V("2026-01-05", "Signed at the start of the year."),
                                "ContractType": V("Framework contract for container slots", "What it is.")}
    out.update({
        "PerformingCarrierAssignedID": V("FRC-J-26-3318", "The rail carrier's job number."),
        "LoadingSequenceID": V("7", "The consignment's turn in the loading of the train."),
        "ContractedCarrierAssignedID": V(f"{RAIL_CONTRACT}/88", "The call-off under the framework contract."),
        "TotalTransportHandlingUnitQuantity": qty(2, "EA", "Two containers."),
        "PerformingCarrierParty": party("14-xu", short=True),
        "EnvironmentalEmission": {
            "EnvironmentalEmissionTypeCode": V("CO2E", "Greenhouse gases of the carriage, as CO2 equivalent."),
            "ValueMeasure": V("410", "For the two containers over the route.", unitCode="KGM"),
            "EmissionCalculationMethod": {
                "CalculationMethodCode": V("CALCULATED", "From the electric train's energy use."),
                "MeasurementFromLocation": {"Name": V("Ferrano Intermodal Hub", "From.")},
                "MeasurementToLocation": {"Name": V("Marrowdale", "To.")},
                "EmissionCalculationLocation": {"Name": V("Ferrano Rail Cargo, energy office", "Where the figure was "
                                                                                               "calculated.")}}},
        "PreCarriageShipmentStage": rail_road_stage(f, "note"),
        "MainCarriageShipmentStage": rail_stage(f),
        "TransportHandlingUnit": [{"TransportEquipment": rail_container(f, k, True),
                                   "CustomsDeclaration": {"ID": V(f.numbers["transit"], "The transit declaration "
                                                                                       "the box travels under."),
                                                          "IssuerParty": party("5-xu", short=True)},   # rail/08#F4
                                   "EnergyConsumptionAllocation": {
                                       "EnergySourceTypeCode": V("ELECTRICITY", "The train runs on electricity."),
                                       "AllocatedEnergyMeasure": V("610", "This box's share of the train's energy, "
                                                                          "by weight.", unitCode="KWH")}}
                                  for k in range(2)]})
    return out


def rail_places(out, f):
    """The service a rail plan or request is about runs from the warehouse, where the carrier takes the boxes over,
    to Lumeway's siding, where it hands them over; the hub is a stage location (D37 point 6, rail/02#F3, 03#F3)."""
    legs = next(x for x in WORLD["flows"] if x["id"] == "rail")["legs"]
    out["FromLocation"] = kit.leg_location(legs[0], "from", "Where the carrier takes the packed boxes over.")
    out["ToLocation"] = kit.leg_location(legs[-1], "to", "Where the service ends: the boxes are placed on Lumeway's "
                                                         "siding.")
    out["Note"] = V("Two containers from the warehouse in Conciaro to the rail siding in Marrowdale: the carrier's tractor to the hub, "
                    "then the container train.", "The transport asked for and agreed.")
    out["TransportContract"] = {**out.get("TransportContract", {}),
                                "ID": V(RAIL_CONTRACT, "The framework contract for container slots, in the carrier's "
                                                       "numbering, the same in every document (rail/02#F13, 03#F14).")}


def day_text(f, day):
    """A day of the flow as a text says it: "15 April"."""
    d = datetime.date.fromisoformat(f.date(day))
    return f"{d.day} {d.strftime('%B')}"


def demurrage_note(f, n, doc, day, why):
    """The world's debit notes (D37, D9): a supplier's addition to an invoice it issued, for the demurrage on the
    second box. Ferrano Rail Cargo charges Valdara, the transport user under DAP, under its framework contract;
    Valdara passes the charge on to Lumeway, which bears the costs of a delay in unloading under DAP."""
    carrier = doc["from"] == "14-xu"
    seller, buyer = doc["from"], doc["to"]
    cur = "XUF"
    scheme = WORLD["countries"]["XU"]["tax"]["schemes"][0]
    if carrier:
        rule = ("E", 0, scheme, "Demurrage on a container of exported goods, charged under the contract of their "
                                "carriage, follows the carriage: exempt as the transport of goods exported from "
                                "Urvania is (category E, D41), as the freight invoice it adds to is.",
                "Transport of goods exported from Urvania")
        billed, billed_why = f.numbers["freight-invoice"], "The freight invoice this debit note adds to (D9)."
    else:
        rule = ("G", 0, scheme, "The demurrage passed on is part of the price of the benches exported to Bayvarra, a "
                                "cost the buyer bears under the sale's delivered-at-place terms and the seller charges "
                                "it: no value added tax, as on the goods invoice it adds to (category G, export of "
                                "goods; O212). The carrier's debit note it passes on is exempt in the same way, as the "
                                "export carriage it follows (rail/12).",
                "Export of goods outside Urvania")
        billed, billed_why = f.numbers["invoice"], "The goods invoice this debit note adds to (D9)."
    days, rate = RAIL_DEMURRAGE_DAYS, DEMURRAGE_XUF
    base = days * rate
    first, last = RAIL_PLACED + RAIL_FREE_DAYS + 1, RAIL_EMPTIED[1]
    box = RAIL_BOXES[1]
    t = kit.terms_of(f, seller, day, "plan" if carrier else None)
    no = f.number("debit-carrier" if carrier else "debit-seller", seller, "DebitNote")
    reason = (f"Container {box} was placed at Lumeway's siding on {day_text(f, RAIL_PLACED)} and released empty on "
              f"{day_text(f, last)}: free time {day_text(f, RAIL_PLACED + 1)} to "
              f"{day_text(f, RAIL_PLACED + RAIL_FREE_DAYS)}, "
              f"demurrage for {days} container days.")
    cause = "The siding's fork-lift was in repair, so Lumeway could unload the second container only on " \
            f"{day_text(f, last)}."
    period = {"StartDate": V(f.date(first), "The first day of demurrage, after the five free days."),
              "EndDate": V(f.date(last), "The day the box was released empty.")}
    tax_cat = kit.tax_category(rule)
    item = {"Name": V(f"Demurrage, container {box}", "What is charged: the box's days at the siding beyond the free "
                                                     "time."),
            "ClassifiedTaxCategory": kit.tax_category(rule, "services" if carrier else None)}
    refs = [{"ID": V(f.numbers["waybill"], "The consignment note under which the box was carried and placed.")}]
    if not carrier:
        refs.append({"ID": V(f.numbers["debit-carrier"], "Ferrano Rail Cargo's debit note for the same days, which "
                                                         "Valdara passes on.")})
    out = {"ID": V(no, "The supplier's number for its debit note."),
           "IssueDate": V(f.date(day), why),
           "DueDate": V(f.date(t["due"]), f"As the payment terms below count it: {t['text'][0].lower()}{t['text'][1:]}"),
           "Note": V(reason if carrier else f"{reason} {cause}", "Why more is due: the contract's rule, applied after "
                                                                 "the invoice was issued (D9, D37)."),
           "DebitNoteTypeCode": V("383", "UN/EDIFACT 1001 code 383: debit note."),
           **({"TaxPointDate": V(f.date(day), "Urvania's value added tax becomes due on the date of the document.")}),
           "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoice it adds to"),
           "LineCountNumeric": V("1", "One line: the demurrage."),
           "InvoicePeriod": period,
           "DiscrepancyResponse": {"Description": V(("Demurrage after the free time at the consignee's siding, under "
                                                     f"framework contract {RAIL_CONTRACT}.") if carrier else
                                                    ("Demurrage at Lumeway's siding, which the buyer bears under the "
                                                     "delivered-at-place terms of the sale."),
                                                    "The reason for the debit as a whole: UN/EDIFACT 4465 has no code "
                                                    "for demurrage, so it is given in words.")},
           **({} if carrier else {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}}),
           "BillingReference": {"InvoiceDocumentReference": {"ID": V(billed, billed_why)}},
           **({"ContractDocumentReference": {"ID": V(RAIL_CONTRACT, "The framework contract whose free time and rate "
                                                                    "the charge applies.")}} if carrier else {}),
           "AdditionalDocumentReference": refs,
           "PaymentMeans": kit.payment_means(f, seller, buyer, seller, day, t["due"] - day, no, "The account to pay "
                                                                                                "to."),
           "PaymentTerms": kit.payment_terms(f, seller, buyer, t, base, cur, no),
           "TaxTotal": {"TaxAmount": amount(0, cur, "No tax: " + rule[3][0].lower() + rule[3][1:]),
                        "TaxSubtotal": {"TaxableAmount": amount(base, cur, "The demurrage."),
                                        "TaxAmount": amount(0, cur, "No tax in this category."),
                                        "TaxCategory": tax_cat}},
           "LegalMonetaryTotal": {"LineExtensionAmount": amount(base, cur, "The line."),
                                  "TaxExclusiveAmount": amount(base, cur, "The line, before tax."),
                                  "TaxInclusiveAmount": amount(base, cur, "No tax is added."),
                                  "PayableAmount": amount(base, cur, "What the customer owes.")},
           "DebitNoteLine": {"ID": V("1", "The demurrage on the second box."),
                             "Note": V(reason if carrier else cause, "The days charged, and why."),
                             "DebitedQuantity": qty(days, "DAY", "Container days beyond the free time."),
                             "LineExtensionAmount": amount(base, cur, f"{days} × {rate:,.0f}."),
                             "InvoicePeriod": period,
                             "BillingReference": {"InvoiceDocumentReference": {"ID": V(billed, billed_why)}},
                             "Item": item,
                             "Price": {"PriceAmount": price(rate, cur, "The framework contract's rate per container "
                                                                       "day (O128)." if carrier else
                                                          "The carrier's rate, passed on at cost."),
                                       "BaseQuantity": qty(1, "DAY", "Per container day.")}}}
    return out


def rail(n, doc):
    f = RAIL
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "Full container loads for the summer season.",
                         "Delivered at place, the distributor's rail siding: the seller arranges and pays the carriage, "
                         "so the order names no carrier (UBL rule IND6: the terms say who transports, not a missing "
                         "carrier).", "Rail siding of Lumeway Distribution, Marrowdale")
    if doc["doc"] == "TransportExecutionPlanRequest":
        out = kit.tep_request(f, n, doc, 1, "Under DAP the manufacturer is the transport user and books the train.",
                              7, w, "Two containers of benches.")   # the service starts with the pickup (rail/02#F2)
        rail_places(out, f)
        kit.deep_merge(out["Consignment"], rail_consignment(f, "request"))
        return out
    if doc["doc"] == "TransportExecutionPlan":
        out = kit.tep(f, n, doc, 2, "The rail carrier confirms the slots on the container train.", 7, w)
        rail_places(out, f)
        # confirmed as requested: the request asked for no additional service and gave no terms of its own, so the
        # pre-arrival notice stays in the carrier's terms and remarks and the slot terms are the carrier's (as ore/03#F3)
        out.pop("AdditionalTransportationService", None)
        out["DocumentStatusReasonDescription"] = V("Capacity available in the requested window: slots on the train "
                                                   "of 14 April.", "Why it is confirmed as requested.")
        terms = out["TransportExecutionTerms"]
        terms.pop("TransportUserSpecialTerms", None)
        terms["TransportServiceProviderSpecialTerms"] = V("Delivery within the agreed slot; the consignee unloads. "
                                                          "Waiting time beyond two hours is charged.", "The carrier's "
                                                                                                       "terms.")
        out["TransportContract"]["ContractType"] = V("Framework contract for container slots", "Its kind, as the "
                                                                                              "consignment note "
                                                                                              "names it.")
        kit.deep_merge(out["Consignment"], rail_consignment(f, "plan"))
        return out
    if doc["doc"] == "TransitCustomsDeclaration":
        return {"ID": V(f.number("transit", doc["from"], "TransitCustomsDeclaration"), "The transit declaration "
                                                                                       "number."),
                "IssueDate": V(f.date(7), "Lodged at the office of departure the evening before the train leaves, "
                                          "once the sealed boxes are at the hub (D37, rail/08#F5)."),
                "IssueTime": V("16:45:00", "After the second box came in at the hub, and before the consignment "
                                           "note, which cites it."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment under transit."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight under transit."),
                             "GoodsItem": kit.goods_items(f, "XUF", "The value of the goods, in ferra, for the transit "
                                                                    "guarantee."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment on the train."),
                                             **rail_offices(),
                                             "MainCarriageShipmentStage": {
                                                 "ID": V("2", "The rail carriage the transit runs on."),
                                                 "TransportModeCode": V("2", "UN/ECE Recommendation 19 code 2: rail "
                                                                             "transport.", listID="UNECE "
                                                                        "Recommendation 19 - Codes for Modes of "
                                                                        "Transport"),
                                                 "TransportMeans": kit.means("14-xu", "FRC-4417", "CT 4471",
                                                                             "The timetable service of the train, "
                                                                             "for the offices on its way (rail/06#F14).",
                                                                             "WB")},
                                             "TransportHandlingUnit": [{"TransportEquipment": rail_container(f, k, False)}
                                                                       for k in range(2)]}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 8, "Reported when the containers are on the train.",
                                         "Two containers loaded on the container train.",
                                         "Ferrano Intermodal Hub",
                                         {"IssueTime": V("06:05:00", "Sent by the terminal's system once both boxes "
                                                                     "were on their wagons."),
                                          "Consignment": {
                                              "PreCarriageShipmentStage": rail_road_stage(f, "status"),
                                              "MainCarriageShipmentStage": {
                                                  "ID": V("2", "The main carriage, by rail."),
                                                  "TransportMeans": {"RailTransport": {"TrainID": V(
                                                      "FRC 4417", "The train the boxes were loaded on (rail/07#F8).")}},
                                                  "OptionalTakeoverTransportEvent": kit.event(
                                                      f, 8, "17:00:00", "If the morning train cannot leave, the boxes "
                                                                        "go on the evening train.", done=False,
                                                      location=RAIL_HUB),
                                                  "DeliveryTransportEvent": kit.event(f, RAIL_PLACED, "11:00:00",
                                                                                      "Planned placement at the "
                                                                                      "siding.", done=False,
                                                                                      location=RAIL_SIDING),
                                                  "TransportEvent": kit.event(f, 8, RAIL_LIFTED[0] + ":00", "Both "
                                                                              "boxes lifted onto the train, the "
                                                                              f"second at {RAIL_LIFTED[1]}.",
                                                                              done=True, location=RAIL_HUB,
                                                                              type_code="LOADING")},
                                              "TransportHandlingUnit": [
                                                  {"TransportEquipment": {
                                                      "ID": V(RAIL_BOXES[k], "A box the report is about "
                                                                             "(rail/07#F8).", schemeID="ISO6346")}}
                                                  for k in range(2)]}}, event_type="LOADING")
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 8, "Made out at the hub when the boxes are on the train, before it leaves: the "
                                        "note records the takeover, not the journey (rail/08#F3).", w,
                          "The gross weight of the two containers' cargo.")
        out["IssueTime"] = V("06:10:00", f"After both boxes were lifted onto the train, at {RAIL_LIFTED[0]} and "
                                         f"{RAIL_LIFTED[1]}, before the timetabled departure.")
        out["IssueLocation"] = kit.place("XUFER", "Where the note was made out: the hub, where the boxes went on "
                                                  "the train.", name="Ferrano Intermodal Hub")
        out["Description"] = V("Two containers of park benches, carried by the carrier's tractor from Castrano's "
                               "warehouse to the Ferrano hub and by the container train to Lumeway's siding in "
                               "Marrowdale, under the Accord's common transit.", "The rail carriage in words, with "
                                                                                 "its road pre-carriage (D37 point 5).")
        kit.deep_merge(out["Shipment"]["Consignment"], rail_consignment(f, "note"))
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return kit.invoice(f, n, doc, 11, "Issued after delivery at the siding.",
                           {"AdditionalDocumentReference": [
                               {"ID": V(f.numbers["tep"], "The transport plan the slots were confirmed in.")},
                               {"ID": V(f.numbers["waybill"], "The consignment note.")}],
                            "ContractDocumentReference": {"ID": V(RAIL_CONTRACT, "The framework contract the freight "
                                                                                 "and its terms rest on (D22).")}},
                           [{"item": "rail-container", "qty": 2, "invoice_why": "Two container slots."}],
                           key="freight-invoice", terms="plan",
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(RAIL_PLACED), "The day the boxes were "
                                                                                            "placed at the siding."),
                                               "DeliveryLocation": RAIL_SIDING}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 8, "Issued on despatch, as Valdara invoices: the morning the train leaves "
                                         "the hub, so that the importer can declare the goods on arrival.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "AdditionalDocumentReference": [
                                {"ID": V(f.numbers["transit"], "The transit declaration the benches left Urvania "
                                                               "under: the evidence for the export exemption "
                                                               "(rail/11#F7).")},
                                {"ID": V(f.numbers["waybill"], "The rail consignment note the benches travel "
                                                               "under.")}]},
                           extra={"Note": V("Delivered at place: the price includes the carriage to the siding.",
                                            "Why the invoice has no separate freight line."),
                                  "Delivery": {"DeliveryLocation": RAIL_SIDING,
                                               "Despatch": {"ActualDespatchDate": V(f.date(8), "The day the train "
                                                                                               "left the hub with "
                                                                                               "the benches.")}}})
    if doc["doc"] == "DebitNote" and doc["from"] == "14-xu":
        return demurrage_note(f, n, doc, RAIL_EMPTIED[1] + 1, "The day after the second box was released empty.")
    if doc["doc"] == "DebitNote":
        return demurrage_note(f, n, doc, RAIL_EMPTIED[1] + 2, "The day after the carrier's debit note.")
    if doc["doc"] == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, RAIL_PLACED, "Declared at Bayvarra customs' inland office in "
                                                             "Marrowdale, the office of destination of the transit, "
                                                             "on the morning after the train arrived (D37).",
                                     "The customs value in lume, Bayvarra's currency: the invoice value in ferra at "
                                     "the world's reference rate (1 ferra = 0.01 lume).")
        out["IssueTime"] = V("08:20:00", "When Lumeway's customs desk opens; the boxes are placed on the siding "
                                         "once the goods are released.")
        out["PreviousCustomsDeclaration"] = {"ID": V(f.numbers["transit"], "The Accord's common transit declaration "
                                                                           "under which the goods came to the office "
                                                                           "of destination: the procedure this import "
                                                                           "ends (D37)."),
                                             "FunctionCode": V("TRANSIT", "The kind of the previous declaration.")}
        return out
    raise SystemExit(f"rail scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the plastics flow (Urvania -> Bayvarra, barge, CPT)
# where the barge's events happen (worklist C18)
BARGE_QUAY = kit.place("XUFER", "At the recovery plant's own quay on the river.", name="Quay of Rinova Recovery, Ferrano")
BARGE_BORDER = {"Name": V("River border Urvania–Bayvarra", "Where the barge leaves Urvania.")}
BARGE_UNLOADING = {"Name": V("River quay, Lumeport", "The quay named in the CPT terms, where the bags are unloaded.")}
PLASTICS = kit.Flow("plastics", "2026-04-13", [
    {"item": "granulate-pe", "ordered": 120, "why": "120 tonnes of recycled granulate, in jumbo bags of one tonne."}])


BARGE_VOYAGE = "FB4-26-031"
BARGE_LOAD = 7       # Monday 20 April: loading and sailing on a working day of the quay and the barge (D27, D41)
# the granulate's lot (world/items.json lot_prefix and the day it was made, three days before loading): one number in
# the waybill and the despatch advice (D41)
PE_LOT = ITEM["granulate-pe"]["lot_prefix"] + PLASTICS.date(BARGE_LOAD - 3)[5:].replace("-", "")
DIESEL_TTW = Decimal("0.268")    # kg CO2e per kWh of diesel, tank to wheel (D41)
# the voyage on the map (O152): the river leg from Rinova's quay to Rivermouth's, with no locks (the river runs free
# below the rapids above Ferrano); the barge sails by day, downstream at about 11 km/h, and moors at night
BARGE_KM = wmap.leg_km("plastics", "7-xu", "41-xb")
BARGE_BORDER_KM = wmap.border_km("plastics", "7-xu", "41-xb")
BARGE_KMH, BARGE_DAY = 11, ("06:30", "17:30")     # sunrise and sunset in April at 31 degrees South, legal time
BARGE_SAILS = "15:10"


def barge_time(f, km):
    """When the barge, sailing on BARGE_LOAD at BARGE_SAILS, has made km: to the quarter hour."""
    t = wmap.sail_by_day(wmap.at(f.date(BARGE_LOAD), BARGE_SAILS), km, BARGE_KMH, *BARGE_DAY)
    q = round((t.hour * 60 + t.minute) / 15) * 15
    return (t.date() - datetime.date.fromisoformat(f.date(0))).days, f"{q // 60:02d}:{q % 60:02d}:00"


def barge_stage(f, actual):
    if barge_time(f, BARGE_KM)[0] != BARGE_LOAD + 2:
        raise SystemExit("plastics: the barge no longer arrives the day before its discharge (O152); set the dates")
    out = {"ID": V("1", "Down the river, from the recovery plant's quay to the river quay in Lumeport."),
           "TransportModeCode": V("8", "UN/ECE Recommendation 19 code 8: inland water transport.",
                                  listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
           "TransportMeans": kit.means("15-xu", "FB-4", direction="DS"),   # a booked voyage, not a schedule (C41)
           "MasterPerson": kit.person("Tomaso", "Riverra", "The skipper of the barge.", job="Skipper"),
           "LoadingPortLocation": {"Name": V("Quay of Rinova Recovery, Ferrano", "Where the bags are loaded.")},
           "UnloadingPortLocation": {"Name": V("River quay, Lumeport", "The place named in the CPT terms.")},
           "EstimatedTransitPeriod": {"DurationMeasure": V("3", f"Three days from takeover to discharge: about "
                                                                f"{wmap.nearest(BARGE_KM, 10)} km downstream, with "
                                                                "no locks, sailing by day.", unitCode="DAY")},
           "TakeoverTransportEvent": kit.event(f, BARGE_LOAD, "09:00:00", "The barge operator takes over the bags at the "
                                                                 "quay.", location=BARGE_QUAY),
           "LoadingTransportEvent": kit.event(f, BARGE_LOAD, "13:30:00", "Loading finished: 120 bags in the hold.", location=BARGE_QUAY),
           "ExportationTransportEvent": kit.event(f, *barge_time(f, BARGE_BORDER_KM), "The barge leaves Urvania at "
                                                  f"the river border, {wmap.whole(BARGE_BORDER_KM)} km below the "
                                                  "quay: sailing from the afternoon of loading and through the "
                                                  "next day from first light.", location=BARGE_BORDER),
           "DischargeTransportEvent": kit.event(f, BARGE_LOAD + 3, "08:00:00", "Planned unloading at the Lumeport quay, with the "
                                                "consignee's morning shift: the barge arrives about "
                                                f"{barge_time(f, BARGE_KM)[1][:5]} the day before and moors at the "
                                                "quay overnight.", done=False, location=BARGE_UNLOADING)}
    return out


def barge_goods(f, w):
    it = ITEM["granulate-pe"]
    goods_xuf = Decimal("120") * Decimal(str(it["price"]["amount"]))
    return {"ID": V("1", "The only goods item."),
            "SequenceNumberID": V("1", "Its place in the cargo list."),
            "Description": V(it["name"], "What the goods are."),
            "DeclaredForCarriageValueAmount": amount(goods_xuf, "XUF", "Declared to the barge operator, which raises "
                                                                       "its liability to this value."),
            "GrossWeightMeasure": qty(w, "KGM", "With the bags."),
            "NetWeightMeasure": qty(120000, "KGM", "The granulate alone."),
            "NetNetWeightMeasure": qty(120000, "KGM", "No inner packaging: the same as the net weight."),
            "ChargeableWeightMeasure": qty(120000, "KGM", "The freight is charged per tonne of granulate."),
            "GrossVolumeMeasure": V("204", "The 120 bags take 1.7 m³ each.", unitCode="MTQ"),
            "NetVolumeMeasure": V("200", "The granulate as it lies in the bags, at a bulk density of about 0.6 "
                                         "tonne per m³; the bags' fabric and loops make up the rest of the gross "
                                         "volume (D41).", unitCode="MTQ"),
            "ChargeableQuantity": qty(120, "TNE", "The tonnes charged."),
            "TraceID": V(PE_LOT, "The lot on the bags' labels, the seller's lot number, as in its despatch advice "
                                 "(D41)."),
            "Quantity": qty(120, "TNE", "120 tonnes."),
            "OriginAddress": address("7-xu"),
            "ContainingPackage": {"Quantity": qty(1, "TNE", "What one bag holds: a tonne of granulate; the "
                                                            "consignment counts the 120 bags (D41)."),
                                  "PackagingTypeCode": V("JB", "UN/ECE Recommendation 21 code JB: bag, jumbo."),
                                  "PackagingType": V("Jumbo bag of one tonne with four lifting loops", "In words."),
                                  "PackingMaterial": V("Woven polypropylene", "What the bags are made of."),
                                  "ReturnableMaterialIndicator": V("true", "The bags go back to the recovery plant "
                                                                           "for reuse."),
                                  "MeasurementDimension": {"AttributeID": V("HEIGHT", "The height of one filled bag."),
                                                           "Measure": V("1300", "In millimetres.", unitCode="MMT")}},
            "Pickup": {"EarliestPickupDate": V(f.date(BARGE_LOAD), "The bags are ready on the quay."),
                       "EarliestPickupTime": V("08:00:00", "From eight."),
                       "LatestPickupDate": V(f.date(BARGE_LOAD), "They must go the same day."),
                       "LatestPickupTime": V("16:00:00", "Before the quay closes.")},
            "Despatch": {"ActualDespatchDate": V(f.date(BARGE_LOAD), "The barge cast off."),
                         "ActualDespatchTime": V(BARGE_SAILS + ":00", "In the afternoon.")},
            "Delivery": {"LatestDeliveryDate": V(f.date(BARGE_LOAD + 4), "The last day of the delivery window "
                                                                     "the buyer's order asks for (D41).")},
            "OrderLineReference": {"LineID": V("1", "The order line."),
                                   "OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
            "DespatchLineReference": {"LineID": V("1", "The line of the despatch advice."),
                                      "DocumentReference": {"ID": V(f.numbers.get("despatch", "-"),
                                                                    "The despatch advice.")}}
            if f.numbers.get("despatch") else None,
            "ShipmentDocumentReference": {"ID": V(f.numbers["tep"], "The transport plan of the sailing.")},
            "EnergyConsumptionAllocation": {"EnergySourceTypeCode": V("DIESEL", "The barge's engine fuel."),
                                            "AllocatedEnergyMeasure": V("5400", "The goods' share of the voyage's "
                                                                                "energy, as fuel energy.",
                                                                        unitCode="KWH")}}


def barge_consignment(f, view):
    out = {"ID": V(f.numbers["consignment"], "The seller's consignment number.")}
    if view == "request":
        out["BulkCargoIndicator"] = V("false", "Not loose bulk: the granulate is in jumbo bags.")
        out["HumanFoodIndicator"] = V("false", "Not food: the barge also carries grain, so the operator must know.")
        out["AnimalFoodIndicator"] = V("false", "Not animal feed either.")
        out["LivestockIndicator"] = V("false", "No animals.")
        out["SpecialSecurityIndicator"] = V("false", "No special security measures needed.")
        return out
    if view == "plan":
        out["MainCarriageShipmentStage"] = barge_stage(f, False)
        return out
    out.update({"CarrierAssignedID": V(BARGE_VOYAGE + "/2", "The barge operator's number: the second lot of "
                                                             "the voyage."),
                "MainCarriageShipmentStage": barge_stage(f, True),
                "TotalPackagesQuantity": V("120", "The 120 jumbo bags of a tonne each (D41)."),
                "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The freight, a charge."),
                                           "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                           "AllowanceChargeReason": V("River freight", "What it is for."),
                                           "Amount": amount(Decimal("179400"), "XUF", "120 tonnes at 1,495 ferra."),
                                           "PerUnitAmount": amount(Decimal("1495"), "XUF", "The rate per tonne, "
                                                                   "times the 120 chargeable tonnes of the goods "
                                                                   "item (D41).")}})
    return out


def plastics(n, doc):
    f = PLASTICS
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Catalogue":          # plastics/12, first in time (D28, O193)
        out = kit.catalogue(f, n, doc, -12, "Rinova's product information for the quarter, sent before the "
                                             "packaging maker plans its next production run.", ["granulate-pe"], 90)
        out["Name"] = V("Recycled PE granulate, second quarter 2026", "The catalogue's title: one product, for the "
                                                                       "quarter.")
        return out
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The packaging maker orders for the next production run.",
                         "Carriage paid to the river quay: the seller books and pays the barge, the buyer bears the "
                         "risk once the goods are on board.", "River quay, Lumeport")
    if doc["doc"] == "OrderResponse":
        return kit.order_response(f, n, doc, 1, "The waste processor confirms the lot.")
    if doc["doc"] == "TransportExecutionPlanRequest":
        out = kit.tep_request(f, n, doc, 1, "Under CPT the seller is the transport user and books the barge.",
                              BARGE_LOAD, w,
                              "120 jumbo bags of one tonne, with their bags.")
        kit.deep_merge(out["Consignment"], barge_consignment(f, "request"))
        return out
    if doc["doc"] == "TransportExecutionPlan":
        out = kit.tep(f, n, doc, 2, "The barge operator confirms the sailing.", BARGE_LOAD, w)
        out.pop("TransportUserRemarks")          # the request's "please confirm" is answered, not repeated (D41)
        kit.deep_merge(out["Consignment"], barge_consignment(f, "plan"))
        return out
    if doc["doc"] == "ExportCustomsDeclaration":
        out = kit.export_declaration(f, n, doc, BARGE_LOAD, "Declared the day the barge is loaded.",
                                     "The value of the granulate, in ferra.")
        out["IssueTime"] = V("12:40:00", "Before the bags are loaded, so that customs releases them before the barge "
                                         "leaves (timelines#F6).")
        return out
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, BARGE_LOAD, "Issued when the barge is loaded.", w, "The gross weight on board.")
        kit.deep_merge(out["Shipment"]["Consignment"], barge_consignment(f, "note"))
        g = barge_goods(f, w)
        out["Shipment"]["GoodsItem"] = {k: v for k, v in g.items() if v is not None}
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "15-xu":
        return kit.invoice(f, n, doc, BARGE_LOAD + 3, "Issued when the bags have been unloaded.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "barge-freight", "qty": 120, "invoice_why": "The tonnes carried."}],
                           key="freight-invoice", terms="plan")
    if doc["doc"] == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, BARGE_LOAD, "The day the barge was loaded.", "The gross weight loaded.",
                                  extra={"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The barge's "
                                                                                "consignment note, on which damage "
                                                                                "is to be reported (D41).")}})
        kit.deep_merge(out, {"Shipment": {"Consignment": {"TotalPackagesQuantity": V(
            "120", "The 120 jumbo bags of a tonne each, as the consignment note counts them (D41).")}}})
        return out
    if doc["doc"] == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, BARGE_LOAD + 3, "Declared on the morning of the unloading.",
                                     "The customs value in lume: the invoice value in ferra at the world's reference "
                                     "rate (1 ferra = 0.01 lume).")
        kit.deep_merge(out["Shipment"]["GoodsItem"][0], {
            "FreeOnBoardValueAmount": amount(Decimal("98046"), "XBL", "The value at the loading quay: the CPT price "
                                             "less the river freight of 179,400 ferra, in lume."),
            "DeclaredStatisticsValueAmount": amount(Decimal("99840"), "XBL", "The value for the trade statistics: "
                                                    "the invoice value at the border."),
            "InsuranceValueAmount": amount(Decimal("0"), "XBL", "The buyer did not insure the river carriage."),
            "RequiredCustomsID": V("3901.10.00", "The tariff code Bayvarra's customs requires on the declaration."),
            "CustomsStatusCode": V("FOREIGN", "Bayvarra's customs status: goods from abroad, not yet released for "
                                              "free circulation."),
            "CustomsProcedureCode": V("1000", "Release for free circulation, with no previous procedure."),
            "CustomsTariffQuantity": qty(120000, "KGM", "The quantity in the tariff's unit: net kilograms."),
            "CustomsImportClassifiedIndicator": V("true", "Classified by the importer before arrival."),
            "BondedWarehouseLocation": {"Name": V("Bonded store at the river quay, Lumeport", "Where the bags wait "
                                                                                             "until released.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The barge's consignment note.")}})
        return out
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, BARGE_LOAD + 1, "Issued the day after the granulate went on board, the "
                                                      "delivery under CPT.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}},
                           extra={"Note": V("Carriage paid to: the price includes the barge to the river quay.",
                                            "Why the invoice has no separate freight line.")})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 36, "The packaging maker pays across the border, before the due date.")
    raise SystemExit(f"plastics scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the retail flow (Bayvarra, DDP)
RETAIL = kit.Flow("retail", "2026-04-20", [
    {"item": "bench-serra-b", "ordered": 24, "why": "Six pallets for the garden department's spring promotion.",
     "received": 23, "received_why": "One bench refused: its frame carton arrived torn and the side frame's armrest bent.",
     "orderline_extra": {
         "CatalogueLineReference": {"LineID": V("1", "The catalogue line ordered from.")},
         "BuyerProposedSubstituteLineItem": {
             "ID": V("1.1", "The store's fall-back if the Serra 180 is out of stock: an ID of its own (retail/08#F9)."),
             "Quantity": qty(24, "EA", "The same quantity."),
             "Item": {"Name": V("Park bench Serra 180, moss green", "The other frame colour: the store would take "
                                                                     "it."),
                      "SellersItemIdentification": {"ID": V("LD-10442", "The distributor's number."),
                                                    "ExtendedID": V("GRN", "The green variant.")}}}}}])


RESALE = {r["id"]: r for r in WORLD["resales"]["sales"]}      # the resales of the world (items.json, D14, O30)
PROMO = Decimal(str(RESALE["lumeway-bench-store"]["less_percent"])) / 100   # the distributor's support on the order


def promo_allowance(base, why):
    return {"ChargeIndicator": V("false", "An allowance the distributor granted."),
            "AllowanceChargeReasonCode": V("100", "The reason for the allowance as a code of UN/EDIFACT 5189: the "
                                                  "distributor's support for the store's promotion is a rebate outside "
                                                  "the ordinary price terms.",
                                           listID="UN/EDIFACT EDED 5189"),
            "AllowanceChargeReason": V("Promotion support", "In words."),
            "MultiplierFactorNumeric": V(str(PROMO), "Five percent."),
            "Amount": amount(base * PROMO, "XBL", why),
            "BaseAmount": amount(base, "XBL", "The goods.")}


def with_allowance(out, total_key, base, why):
    """Apply the promotion allowance to a document's totals (no tax: a sale for resale)."""
    a = money(base * PROMO, "XBL")
    ac = promo_allowance(base, why)
    if total_key == "LegalMonetaryTotal":             # on the invoice the allowance carries its tax category
        ac["TaxCategory"] = kit.tax_category(kit.tax_rule("6-xb", "26-xb", "bench-serra-b"))
        subs = out.get("TaxTotal", {}).get("TaxSubtotal")
        if isinstance(subs, list) and len(subs) == 1:   # the allowance lowers the taxable amount of its category
            subs[0]["TaxableAmount"] = amount(base - a, "XBL", "The goods less the promotion support.")
    out["AllowanceCharge"] = ac
    t = out[total_key]
    t["AllowanceTotalAmount"] = amount(a, "XBL", "The promotion support.")
    if "TaxExclusiveAmount" in t:
        t["TaxExclusiveAmount"] = amount(base - a, "XBL", "The goods less the allowance; no tax on a sale for "
                                                          "resale.")
        t["TaxInclusiveAmount"] = amount(base - a, "XBL", "The same: no tax.")
    t["PayableAmount"] = amount(base - a, "XBL", "What the store pays: the goods less the promotion support.")
    return base - a


def returnable_pallet(k):
    """The GRAI of one of Lumeway's returnable pallets: GS1 identifies a returnable asset by its Global Returnable
    Asset Identifier, the filler digit 0, the company prefix, the asset type, a check digit and the asset's serial
    number (decision ID-Q7)."""
    prefix = PARTY["6-xb"]["identity"]["identification"]["company_prefix"]
    body = "0" + prefix + "00001"
    return V(body + world_ids.gs1_digit(body) + f"{2200 + 17 * k}", "The pallet's Global Returnable Asset Identifier "
             "(GRAI): Lumeway Distribution's pallets belong to its own pool and go back after each delivery, so each "
             "carries a GRAI, under its GS1 company prefix (952, reserved for examples): asset type 00001, its "
             "returnable pallet, the check digit and the pallet's serial number.", schemeID="GS1 GRAI")


def retail(n, doc):
    f = RETAIL
    w = kit.gross_weight(f, "ordered")
    store = {"Name": V("Garden department", "The department of the store that sells the benches.")}
    if doc["doc"] == "Catalogue":
        return kit.catalogue(f, n, doc, 0, "The spring catalogue for the store.", ["bench-serra-b", "bench-casting-b"], 90)
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The store's forecast number."),
                "IssueDate": V(f.date(2), "Sent after the catalogue arrived."),
                "ForecastPurposeCode": V("SALES", "A forecast of the store's sales, so the distributor can plan its "
                                                  "stock."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The forecast covers the next six weeks."),
                                   "EndDate": V(f.date(56), "The end of the forecast period.")},
                "ForecastLine": {"ID": V("1", "The first and only line."),
                                 "ForecastTypeCode": V("TOTAL", "The total expected sales of the item in the period."),
                                 "SalesItem": {"Quantity": qty(40, "EA", "Forty benches over six weeks, promotion "
                                                                          "included."),
                                               "Item": item("bench-serra-b")}}}
    if doc["doc"] == "RetailEvent":
        return {"ID": V(f.number("event", doc["from"], "RetailEvent"), "The store's event number."),
                "IssueDate": V(f.date(2), "Announced with the forecast."),
                "RetailEventName": V("Spring garden promotion", "The name of the promotion."),
                "RetailEventStatusCode": V("CONFIRMED", "The promotion is decided, not only planned."),
                "Description": V("Ten per cent off garden furniture for two weeks.", "What the promotion is."),
                "Period": {"StartDate": V(f.date(21), "The promotion starts in three weeks."),
                           "EndDate": V(f.date(34), "It lasts two weeks.")}}
    if doc["doc"] == "InventoryReport":
        return {"ID": V(f.number("inventory", doc["from"], "InventoryReport"), "The store's inventory report number."),
                "IssueDate": V(f.date(3), "The weekly stock report."),
                "InventoryReportLine": {"ID": V("1", "The first and only line."),
                                        "Quantity": qty(3, "EA", "Three benches left in the garden department."),
                                        "Item": item("bench-serra-b")}}
    if doc["doc"] == "Order":
        out = kit.order(f, n, doc, 4, "The store replenishes before the promotion.",
                         "Delivered duty paid at the store: the distributor arranges and pays the transport and every "
                         "cost, so the order names only where to deliver.", "Brightmarket Stores, goods-in, Lumeport",
                         {"Delivery": {"DeliveryLocation": {**kit.gln_location("26-xb", "goods-in"),
                                                           "Description": V("Goods-in, garden department",
                                                                             "Where the truck unloads.")}},
                          "IssueTime": V("08:15:00", "Sent from the store's replenishment system each morning."),
                          "ValidityPeriod": {"EndDate": V(f.date(6), "The order lapses if not confirmed within two "
                                                                     "days: the promotion cannot wait.")},
                          "CatalogueReference": {"ID": V(f.numbers["catalogue"], "The spring catalogue ordered "
                                                                                 "from.")},
                          "AdditionalDocumentReference": {"ID": V(f.numbers["event"], "The promotion the "
                                                                  "benches are ordered for.")},
                          "PaymentMeans": {"PaymentMeansCode": V("30", "The store pays by credit transfer.",
                                                                 listID="UN/EDIFACT EDED 4461")},
                          "PaymentTerms": {"Note": V("30 days net, as agreed with the distributor.", "The terms the "
                                                     "store orders on.")},

                          "TransactionConditions": {"ID": V("LD-TC-01", "The distributor's conditions of sale."),
                                                    "ActionCode": V("ACCEPTED", "The store accepts them.")},
                          "Signature": {"ID": V("BM-SIG-26-0424", "The store's electronic seal on the order."),
                                        "SignatoryParty": party("26-xb", short=True)}})
        with_allowance(out, "AnticipatedMonetaryTotal", Decimal("12480.00"), "5 % of the goods, agreed for the "
                                                                              "promotion.")
        return out
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 5, "Because it sold delivered duty paid, the distributor books the truck.", 9,
                               w, "Six pallets of benches.")
    if doc["doc"] == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, 9, "The day the truck was loaded at the distribution centre.",
                                  "The gross weight loaded.")
        bench = ITEM["bench-serra-b"]
        units = kit.handling_units(f, f.deal, "6-xb", "BRIGHTMARKET LUMEPORT")
        for k, u in enumerate(units, 1):
            # what the pallet actually carries, as packed at the distribution centre (retail/12#F2, D20), and the
            # returnable pallet itself as the unit's equipment, not as a package inside it
            u["ActualPackage"] = [kit.parcel_package(p) for p in kit.maker("bench-serra-b")["parcels"]]
            u["TransportEquipment"] = {"ID": returnable_pallet(k),
                                       "ReturnabilityIndicator": V("true", "The pallet goes back: the truck takes the "
                                                                           "store's empty pallets back to the "
                                                                           "distribution centre."),
                                       "Description": V("Returnable pallet of the distributor's pool, 1850 x 700 mm",
                                                        "The pallet the parcels are loaded on: transport equipment "
                                                        "in UN/CEFACT's sense, which counts pallets with "
                                                        "containers and trailers.")}
            u["HandlingUnitDespatchLine"] = {
                "ID": V(f"1-{k}", "The pallet's line: the benches on it, as part {k} of despatch line 1 (retail/12#F9)."),
                "DeliveredQuantity": qty(4, "EA", "Four benches on the pallet."),
                "OrderLineReference": {"LineID": V("1", "The order line the benches belong to.")},
                "Item": {"Name": V(bench["name"], "The item, named only: it is described in full on despatch line "
                                                  "1."),
                         "SellersItemIdentification": {"ID": V(bench["sellers_id"], "The seller's item number.")}}}
        units[0].update({
            "TransportMeans": kit.means("10-xb", "B-03"),
            "GoodsItem": {"ID": V("1", "The goods on the pallet, as one goods item.")},
            "ShipmentDocumentReference": {"ID": V(f.numbers["tep-request"], "The transport booking the pallet "
                                                                            "travels under.")}})
        out["Shipment"]["TransportHandlingUnit"] = units
        return out
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 9, "Issued when the carrier collects at the distribution centre.", w,
                           "The gross weight taken over.")
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return {"IssueTime": V("11:30:00", "After the delivery it bills: the store took the goods in at 10:40 "
                                           "(retail/16#F5, C72)."),
                **kit.invoice(f, n, doc, 10, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "road-transport-b", "qty": wmap.whole(wmap.leg_km("retail", "6-xb", "26-xb")),
                             "invoice_why": "The kilometres driven loaded, from the distribution centre in "
                                            "Marrowdale to the store in Lumeport: the truck's leg on the map "
                                            "(O152)."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment carried.")}}}})}
    if doc["doc"] == "ReceiptAdvice":
        out = kit.receipt_advice(f, n, doc, 10, "The day the goods were unloaded at the store.")
        out["Shipment"] = {"ID": V(f.numbers["shipment"], "The shipment received."),
                           "TransportHandlingUnit": {
                               "ID": kit.unit_id("6-xb", f, 3, "The pallet with the damaged carton"),
                               "DamageRemarks": V("One frame carton torn, the side frame's armrest bent.", "What the goods-in "
                                                                                                "found."),
                               "DamageDocumentationAttachment": {"ExternalReference": {
                                   "URI": V("https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg",
                                            "The photograph taken at goods-in."),
                                   "MimeCode": V("image/jpeg", "A photograph."),
                                   "FileName": V("pallet-3.jpg", "The file name.")}},
                               "Status": {"ConditionCode": V("DAMAGED", "The pallet's condition on arrival."),
                                          "Description": V("Three benches accepted, one refused.", "What was done.")},
                               "ReceivedHandlingUnitReceiptLine": {
                                   "ID": V("1-3", "The receipt of the pallet, as part of receipt line 1 (retail/17#F13)."),
                                   "ReceivedQuantity": qty(3, "EA", "Three benches accepted from this pallet."),
                                   "RejectedQuantity": qty(1, "EA", "One refused."),
                                   "RejectReason": V("Damaged in transit.", "Why.")}}}
        return out
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 10, "Issued on delivery.",
                          {"OrderReference": {"ID": V(f.numbers["order"], "The store's order.")},
                           "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")},
                           "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The store's receipt "
                                                                                      "advice.")}},
                          [{"item": "bench-serra-b", "qty": 24, "invoice_why": "The benches despatched."}])
        payable = with_allowance(out, "LegalMonetaryTotal", Decimal("12480.00"), "The promotion support of the "
                                                                                 "order.")
        out["PaymentTerms"]["PenaltyAmount"] = amount(payable * Decimal("0.015"), "XBL", "The surcharge for the "
                                                                                         "first month late.")
        f.numbers["invoice-amount"] = payable
        return out
    if doc["doc"] == "CreditNote":
        out = kit.credit_note(f, n, doc, 12, "Issued after the receipt advice reported the refused bench.",
                               [{"item": "bench-serra-b", "qty": 1, "why": "The bench refused at delivery.",
                                 "line_tax": True,
                                 "line_extra": {
                                     "AccountingCostCode": V("6120", "The store's garden department."),
                                     "AccountingCost": V("Garden department", "In words."),
                                     "Delivery": {"ActualDeliveryDate": V(f.date(10), "The delivery the bench "
                                                                                      "was refused at.")},
                                     "DespatchLineReference": {"LineID": V("1", "The despatch line."),
                                                               "DocumentReference": {"ID": V(f.numbers["despatch"],
                                                                                             "The despatch "
                                                                                             "advice.")}},
                                     "DeliveryTerms": {"ID": V("DDP", "As on the order: delivered duty paid.",
                                                               schemeID="INCOTERMS")}}}],
                               {"BillingReference": {"InvoiceDocumentReference": {
                                   "ID": V(f.numbers["invoice"], "The invoice this credit note corrects."),
                                   "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                                "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice that "
                                                                                           "reported the damage.")},
                                "DiscrepancyResponse": {"ReferenceID": V("1", "The invoice line that was wrong."),
                                                        "ResponseCode": V("17", "The distributor's answer: a "
                                                                                "credit for the refused bench."),
                                                        "Description": V("One bench refused at goods-in, damaged in "
                                                                         "transit.", "In words.")},
                                "OrderReference": {"ID": V(f.numbers["order"], "The store's order.")},
                                "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice of "
                                                                                             "the goods.")}})
        with_allowance(out, "LegalMonetaryTotal", Decimal(out["LegalMonetaryTotal"]["LineExtensionAmount"].value),
                       "The invoice gave the promotion support on the whole order, so the credit is 5 % less too.")
        line = out["CreditNoteLine"][0]
        line.update({"Note": V("Bench refused: side frame's armrest bent, frame carton torn.", "Why the line is credited."),
                     "DiscrepancyResponse": {"ReferenceID": V("1", "The invoice line."),
                                             "ResponseCode": V("17", "Credited because damaged.")},
                     "OrderLineReference": {"LineID": V("1", "The order line.")},
                     "ReceiptLineReference": {"LineID": V("1", "The receipt line that reported it."),
                                              "DocumentReference": {"ID": V(f.numbers["receipt"], "The receipt "
                                                                                                  "advice.")}},
                     "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The "
                                                                               "invoice.")},
                                          "BillingReferenceLine": {"ID": V("1", "The invoice line credited.")}}})
        return out
    if doc["doc"] == "PurchaseReceipt":
        out = kit.purchase_receipt(f, n, doc, 25, "A consumer buys a bench during the promotion week.",
                                    [{"item": "bench-serra-r", "qty": 1, "why": "One bench."}], cash=False,
                                    promotion={"name": "Spring garden promotion",
                                               "percent": RESALE["store-bench-reopening"]["less_percent"],
                                               "from": 22, "to": 28})
        till(out, f, 25, "11:42:00", "G2", "Mira")
        card_payment(out, f, 25, "11:42:00")
        out["Note"] = V("Home delivery booked for Saturday.", "Printed on the receipt.")
        out["Delivery"] = {"DeliveryAddress": address("c-xb", register=True),
                           "RequestedDeliveryPeriod": {"StartDate": V(f.date(26), "Saturday, the day the note "
                                                                                    "names: the store delivers "
                                                                                    "Monday to Saturday."),
                                                       "StartTime": V("09:00:00", "Morning."),
                                                       "EndTime": V("12:00:00", "Until noon.")},
                           "CarrierParty": party("26-xb", short=True)}
        return out
    raise SystemExit(f"retail scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"rail": rail, "plastics": plastics, "retail": retail})


# ---------------------------------------------------------------- the sea flow (Bayvarra -> Lisavu, CIF)
# where the sea flow's events happen (worklist C18)
SEA_LUMEPORT = kit.place("XBLMP", "At the container quay of the Port of Lumeport.")
SEA_SELANU = kit.place("XLSEL", "At the Port of Selanu.")
# the voyage on the map (O152, O53, D30): one passage time from the place list, the sea route measured on the real
# ocean at the ship's 13.5 knots; the island's clocks are an hour ahead of Lumeport's (D27). The ship sails on the
# evening of day 10 and is off Selanu on the evening of day 12, after dark: Selanu's pilots take ships in by
# daylight only and the ship does not anchor, so it waits off the port and berths at first light on day 13.
SEA_KM = wmap.sea_km()
SEA_HOURS = wmap.sea_hours()
SEA_SAILS, SEA_SAILED = "18:00", "18:10"        # the timetable's departure, and the actual one (Lumeport time)
SEA_OFF_SELANU = wmap.after(wmap.at("2026-05-14", SEA_SAILS), SEA_HOURS + 1)          # island time
SEA_ARRIVES = 13                                # the day the ship berths, at first light
if SEA_OFF_SELANU.date().isoformat() != "2026-05-16" or SEA_OFF_SELANU.hour < 18:
    raise SystemExit("sea: the passage no longer brings the ship off Selanu on the evening of day 12 (O152, O53)")


SEA_REPORTS = "15:40"     # the pre-arrival report, in Lumeport's time (the carrier's), on day 12


def sea_report_nm(f):
    """The ship's distance to go to Selanu when it sends its pre-arrival report, rounded to 5 nautical miles."""
    off = wmap.after(wmap.at(f.date(10), SEA_SAILED), SEA_HOURS)               # Lumeport time
    left = (off - wmap.at(f.date(12), SEA_REPORTS)).total_seconds() / 3600 * wmap.KNOTS
    return wmap.nearest(left, 5)


def sea_quarter(t):
    q = round((t.hour * 60 + t.minute) / 15) * 15
    return f"{q // 60:02d}:{q % 60:02d}:00"


SEA_3PL = {"Name": V("Nalevi Warehousing, Selanu", "The 3PL's warehouse on the island, where the goods are received "
                                                   "and stored.")}
SEA = kit.Flow("sea", "2026-05-04", [
    # O165: Velumi buys by the pallet, and two pallets more in a container already booked add little to the freight
    # O172: the port's benches and the buyer's own on lines of their own; the goods chain's lots go to them in turn
    # (the April rail lot VI-LOT-260409 to the port's line, two pallets of VI-LOT-260410 to the stock line)
    {"item": "bench-serra-b", "ordered": 96, "port": True,
     "why": "96 benches on 24 pallets of four for the Port of Selanu's harbour parks."},
    {"item": "bench-serra-b", "ordered": 8, "why": "Two pallets of four benches for the buyer's own stock: it buys "
                                                   "by the pallet, and two pallets add little to the freight of a "
                                                   "container already booked."},
    {"item": "bench-casting-b", "ordered": 12, "why": "Spare side frames for the buyer's own service stock.",
     "received": 11, "received_why": "One frame carton crushed at the port; the frame inside is cracked."}],
    buyer="1-xl")       # Lumeway's CIF price for the island's frames (items.json buyer_prices; O30)
CONTAINER = kit.container_number("TWL", 412087)       # Tidewell Ocean Lines' container (ISO 6346, with check digit)
SEA_FREIGHT = Decimal("2950.00")
if SEA_FREIGHT != Decimal(str(ITEM["sea-freight"]["price"]["amount"])):
    raise SystemExit("sea: the sea freight is not the forwarder's price for it (world/items.json sea-freight)")


def sea_floor_places(f):
    """The floor places the sea flow's pallets take in the 40-foot container: a bench pallet may carry one more on
    top, the frame cartons' pallet nothing (world/items.json, the pallets' stack); the container has 18 (O165)."""
    places = 0
    for d in f.deal:
        units = [u for u in kit.pallets(f, [d])]
        stack = kit.maker(d["item"])["pallet"]["stack"]
        places += -(-len(units) // stack)
    if places > 18:
        raise SystemExit(f"sea: {places} floor places do not fit the 40-foot container's 18 (O165)")
    return places


def sea_goods(f, iid=None):
    """The value of the goods sold (of one item, if given) at the buyer's prices, in lume."""
    return sum(Decimal(str(d["ordered"])) * kit.unit_price(d["item"], "XBL", f.buyer) for d in f.deal
               if iid in (None, d["item"]))


# O173: the cargo insurance is a premium rate on the insured value, the CIF value plus 10 %, which holds the premium
# itself (world/items.json cargo-insurance; the same figure as the margin check's, world_items.insurance_premium)
INSURANCE, INSURED = world_items.insurance_premium(ITEM["cargo-insurance"]["price"], sea_goods(SEA) + SEA_FREIGHT)
INSURANCE_RATE = ITEM["cargo-insurance"]["price"]["rate_percent"]
if INSURED != (sea_goods(SEA) + SEA_FREIGHT + INSURANCE) * Decimal("1.1"):
    raise SystemExit("sea: the insured value is not the CIF value plus 10 % (O173)")


def insurance_basis():
    """The premium's basis in words (O173)."""
    return (f"{INSURANCE_RATE} % of the insured value of {INSURED:,.2f} lume: the CIF value of "
            f"{sea_goods(SEA) + SEA_FREIGHT + INSURANCE:,.2f} (goods {sea_goods(SEA):,.2f}, sea freight "
            f"{SEA_FREIGHT:,.2f} and the premium itself) plus 10 %")


def cif_value(f):
    return sea_goods(f) + SEA_FREIGHT + INSURANCE


def container(f, gross_why):
    return {"TransportHandlingUnit": {"TransportEquipment": {
        "ID": V(CONTAINER, "The container's number: the owner code of the ocean carrier, U for a freight container, six "
                           "digits and the ISO 6346 check digit.", schemeID="ISO6346"),
        "GrossWeightMeasure": qty(kit.gross_weight(f, "ordered") + 3750, "KGM", gross_why),
        "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight, as marked on its door.")}}}


SEA_BOOKING = "TWL-BK-26-55710"     # the ocean carrier's booking number
SEA_SEAL = "TWL-S-0884213"


def sea_equipment(f, detail):
    out = {"ID": V(CONTAINER, "The container's number: the owner code of the ocean carrier, U for a freight container, "
                              "six digits and the ISO 6346 check digit.", schemeID="ISO6346"),
           "TransportEquipmentTypeCode": V("CN", "UN/EDIFACT 8053 code CN: container.", listID="UN/EDIFACT EDED 8053"),
           "SizeTypeCode": V("42G1", "ISO 6346 size and type: 40 feet, 8 ft 6 in high, general purpose."),
           "GrossWeightMeasure": qty(kit.gross_weight(f, "ordered") + 3750, "KGM", "The verified gross mass: cargo and "
                                     "the container's own weight of 3,750 kg."),
           "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight, as marked on its door."),
           "TransportEquipmentSeal": {"ID": V(SEA_SEAL, "The carrier's seal, put on when the container was packed."),
                                      "SealIssuerTypeCode": V("CARRIER", "Issued by the ocean carrier."),
                                      "SealingPartyType": V("Shipper", "Put on by the shipper.")}}
    if detail:
        out.update({
            "StowagePositionID": V("140282", "Bay 14, row 02, tier 82: on deck, as planned by the carrier."),
            "FullnessIndicationCode": V("FCL", "A full container load."),
            "RefrigeratedIndicator": V("false", "A dry container."),
            "VerifiedGrossMass": {
                "ID": V("VGM-26-0510", "The shipper's weight declaration."),
                "WeighingDate": V(f.date(8), "Weighed when packed."),
                "WeighingTime": V("15:30:00", "After closing the doors."),
                "WeighingMethodCode": V("SM2", "SOLAS method 2: the cargo and packing weighed and added to the tare.",
                                        listID="IMO SOLAS"),
                "WeighingDeviceID": V("LD-SCALE-03", "The scale of the warehouse."),
                "WeighingDeviceType": V("Platform scale", "Its kind."),
                "GrossMassMeasure": qty(kit.gross_weight(f, "ordered") + 3750, "KGM", "The verified gross mass."),
                "WeighingParty": party("6-xb", short=True),
                "ShipperParty": party("6-xb", short=True),
                "ResponsibleParty": party("6-xb", short=True),
                "DocumentReference": {"ID": V("VGM-26-0510", "The signed weight declaration sent to the carrier.")}},
            "PackagedTransportHandlingUnit": kit.handling_units(f, f.deal, "6-xb", "VELUMI SELANU"),
            "GoodsItem": {"ID": V("1", "The goods in the container, as one item for the carrier."),
                          "Description": V("Park benches and spare side frames", "In words."),
                          "GoodsItemContainer": {"ID": V(CONTAINER, "The container the goods are in."),
                                                 "Quantity": qty(len(kit.pallets(f, f.deal)), "EA",
                                                                 f"{len(kit.pallets(f, f.deal))} pallets in it.")},
                          "ContainedGoodsItem": [{"ID": V("1.1", "The benches."),
                                                  "Description": V("Park benches", "In words.")},
                                                 {"ID": V("1.2", "The side frames."),
                                                  "Description": V("Spare side frames", "In words.")}]},
            "SupplierParty": {"Party": party("11-xb", short=True)},
            "AttachedTransportEquipment": {"ID": V("BV CH 0412", "The forwarder's chassis the container rode on to "
                                                                 "the port."),
                                           "TransportEquipmentTypeCode": V("TE", "UN/EDIFACT 8053 code TE: "
                                                                                 "trailer.",
                                                                           listID="UN/EDIFACT EDED 8053")},
            "Package": {"ID": kit.unit_id("6-xb", f, len(kit.pallets(f, f.deal)), "The pallet of frame cartons, "
                                                                                     "packed last at the doors"),
                        "Quantity": qty(12, "EA", "Twelve side frames, one to a carton."),
                        "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
                        "ContainingTransportEquipment": {"ID": V(CONTAINER, "The container.", schemeID="ISO6346")}}})
    return out


def sea_consignment(f, view):
    goods = sea_goods(f)
    out = {"ID": V(f.numbers["consignment"], "The distributor's consignment number.")}
    if view == "instructions":
        out.update({
            "ForwarderServiceInstructions": V("Book a 40-foot container on the next sailing to Selanu, arrange the "
                                              "truck to the port, declare the export and insure the cargo.",
                                              "What the forwarder is to do."),
            "ConsolidatableIndicator": V("false", "A full container: not to be grouped with other cargo."),
            "SpecialInstructions": V("Load the castings last, behind the doors.", "So they are unloaded first."),
            "ExporterParty": party("6-xb", short=True),
            "ImporterParty": party("1-xl", short=True),
            "InsuranceParty": party("29-xb", short=True),
            "OriginalDespatchTransportationService": {
                "TransportServiceCode": V("MERCHHAUL", "The forwarder, not the shipping line, brings the "
                                                              "container to the port."),
                "Name": V("Truck from Marrowdale to the port of Lumeport", "In words.")},
            "FinalDeliveryTransportationService": {
                "TransportServiceCode": V("MERCHHAUL", "The buyer's 3PL collects at the port of Selanu."),
                "Name": V("Truck from the port of Selanu to the 3PL", "In words.")}})
        return out
    out.update({
        "CarrierAssignedID": V(SEA_BOOKING, "The carrier's booking number."),
        "FreightForwarderAssignedID": V(f.numbers["instructions"], "The forwarder's file: the instructions it "
                                                                   "received."),
        "BrokerAssignedID": V("TCB-26-0331", "The customs broker's file in Selanu."),
        "ConsignorAssignedID": V(f.numbers["order"], "The order the goods were sold under."),
        "TotalInvoiceAmount": amount(goods, "XBL", "The value of the goods on the sales invoice."),
        "DeclaredCustomsValueAmount": amount(cif_value(f), "XBL", "The CIF value: goods, freight and insurance."),
        "FreeOnBoardValueAmount": amount(goods, "XBL", "The value on board in Lumeport: the goods alone."),
        "InsuranceValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL", "110 % of the CIF value."),
        "InsurancePremiumAmount": amount(INSURANCE, "XBL", "The premium the seller paid under CIF."),
        "TariffCode": V("TWL-T-0940", "The item of the carrier's own freight tariff for this cargo: furniture. A "
                                     "code the carrier defines, so it has no code list."),
        "TariffDescription": V("Furniture, packed, not hazardous", "The carrier's commodity tariff, in words."),
        "ShippingPriorityLevelCode": V("STANDARD", "The normal sailing, no priority loading."),
        "HandlingCode": V("DECK", "The carrier may stow the container on deck."),
        "HandlingInstructions": V("Keep dry.", "The handling, in words."),
        "Information": V("Shipped on board in apparent good order and condition.", "The carrier's clause."),
        "OriginalDespatchParty": party("6-xb", short=True),
        "FinalDeliveryParty": party("1-xl", short=True),
        "LogisticsOperatorParty": party("9-xl", short=True),
        **({"BillOfLadingHolderParty": party("10-xb", short=True)} if view == "bl" else {}),   # sea/14#F11 (b)
        "OriginalDepartureCountry": {"IdentificationCode": V("XB", "From Bayvarra.")},
        "FinalDestinationCountry": {"IdentificationCode": V("XL", "To the island.")},
        "FirstArrivalPortLocation": kit.place("XLSEL", "The first port of call after Lumeport."),
        "LastExitPortLocation": kit.place("XBLMP", "The last port in Bayvarra."),
        "DeliveryTerms": {"ID": V("CIF", "Incoterms 2020: cost, insurance and freight to the port of Selanu."),
                          "LossRiskResponsibilityCode": V("BUYER", "The risk is the buyer's from on board in Lumeport."),
                          "LossRisk": V("Risk passes when the goods are on board the vessel in Lumeport.", "In words."),
                          "Amount": amount(cif_value(f), "XBL", "The CIF value the terms are based on."),
                          "DeliveryLocation": kit.place("XLSEL", "The named port of destination."),
                          "AllowanceCharge": {"ChargeIndicator": V("true", "A cost under the terms."),
                                              "AllowanceChargeReasonCode": V("HD", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                              "AllowanceChargeReason": V("Terminal handling at Selanu, for the buyer",
                                                                         "Under CIF the buyer pays the unloading."),
                                              "Amount": amount(Decimal("185.00"), "XBL", "The carrier's tariff.")}},
        "PaymentTerms": {"Note": V("Ocean freight payable before release of the bill of lading.", "The carrier's "
                                                                                                  "terms.")},
        "PrepaidPaymentTerms": {"Note": V("Ocean freight and bunker surcharge prepaid by the shipper.", "CIF: the "
                                                                                                       "seller pays.")},
        "CollectPaymentTerms": {"Note": V("Terminal handling at Selanu collect from the consignee.", "The buyer "
                                                                                                    "pays it there.")},
        "DisbursementPaymentTerms": {"Note": V("Island customs fees advanced by the broker and recharged to the "
                                               "consignee.", "Paid out for someone else.")},
        "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The basic ocean freight."),
                                   "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                   "AllowanceChargeReason": V("Ocean freight, 40-foot container", "In words."),
                                   "Amount": amount(Decimal("2700.00"), "XBL", "The carrier's rate.")},
        "ExtraAllowanceCharge": {"ChargeIndicator": V("true", "A surcharge."),
                                 "AllowanceChargeReasonCode": V("FC", "The bunker surcharge is part of the freight: UN/EDIFACT 7161 has no code of its own for it, so it carries the freight code."),
                                 "AllowanceChargeReason": V("Bunker surcharge", "For the fuel price."),
                                 "Amount": amount(Decimal("250.00"), "XBL", "Together with the freight: the 2,950 "
                                                                            "lume the forwarder invoices.")},
        "PreCarriageShipmentStage": {
            "ID": V("1", "By truck from Marrowdale to the port."),
            "ShipmentStageTypeCode": V("10", "The kind of stage."),
            "ShipmentStageType": V("Carriage before the main carriage", "In words."),
            "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The truck to the port."),
                                       "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                       "AllowanceChargeReason": V("Pre-carriage by road", "In words."),
                                       "Amount": amount(Decimal("310.00"), "XBL", "The forwarder's own truck; part "
                                                                                  "of its price to the shipper.")},
            "TransportModeCode": V("3", "Road transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                 "Transport"),
            "PreCarriageIndicator": V("true", "Before the main carriage."),
            "CabotageIndicator": V("false", "A Bayvarran truck within Bayvarra: no cabotage."),
            "CarrierParty": party("10-xb", short=True),
            "TransportMeans": kit.means("10-xb", "B-05"),
            "DropoffTransportEvent": kit.event(f, 9, "10:15:00", "The container was dropped at the container quay.", location=SEA_LUMEPORT)},
        "MainCarriageShipmentStage": {
            "ID": V("2", "By sea from Lumeport to Selanu."),
            "TransportModeCode": V("1", "Maritime transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                      "Transport"),
            "TransportMeans": {**kit.means("11-xb", "TH", "TH-26-19E", "The voyage number.", "EB"),
                               "TradeServiceCode": V("TWL-ISL", "The carrier's code for its island service."),
                               "Stowage": {"LocationID": V("140282", "Bay 14, row 02, tier 82."),
                                           "Location": V("On deck, aft of the bridge", "In words."),
                                           "MeasurementDimension": {"AttributeID": V("SLOTLENGTH", "The slot length."),
                                                                    "Measure": V("12.2", "A 40-foot slot.",
                                                                                 unitCode="MTR")}}},
            "LoadingPortLocation": kit.place("XBLMP", "The port of loading."),
            "UnloadingPortLocation": kit.place("XLSEL", "The port of discharge."),
            "AcceptanceTransportEvent": kit.event(f, 9, "10:15:00", "The terminal accepted the container.", location=SEA_LUMEPORT),
            "AvailabilityTransportEvent": kit.event(f, SEA_ARRIVES, "14:00:00", "The container is available at Selanu.",
                                                    done=False, location=SEA_SELANU),
            "StorageTransportEvent": kit.event(f, 9, "10:30:00", "Stacked at the quay until loading.", location=SEA_LUMEPORT),
            "FreightChargeLocation": kit.place("XBLMP", "The freight is payable in Lumeport.")},
        "OnCarriageShipmentStage": {
            "ID": V("3", "By truck from the port of Selanu to the 3PL."),
            "TransportModeCode": V("3", "Road transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                 "Transport"),
            "OnCarriageIndicator": V("true", "After the main carriage."),
            "CarrierParty": party("9-xl", short=True),
            "ReceiptTransportEvent": kit.event(f, SEA_ARRIVES + 1, None, "Planned receipt at the 3PL.", done=False, location=SEA_3PL),
            "WarehousingTransportEvent": kit.event(f, SEA_ARRIVES + 1, None, "Stored at the 3PL until called off.", done=False, location=SEA_3PL)},
        "InsurancePolicy": {"ID": V("WS-CP-26-4471", "The cargo policy of the insurer."),
                            "InsuranceTypeCode": V("ALLRISKS", "Cover against all risks."),
                            "InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL", "110 % of the CIF "
                                                                                               "value."),
                            "DeductibleAmount": amount(Decimal("250.00"), "XBL", "The part of a claim the insured "
                                                                                 "bears."),
                            "InsurancePremiumAmount": amount(INSURANCE, "XBL", "The premium."),
                            "BeneficiaryParty": party("1-xl", short=True),
                            "PolicyHolderParty": party("6-xb", short=True),
                            "PolicyDocumentReference": {"ID": V("WS-CERT-26-0884", "The insurance certificate that "
                                                                                   "goes with the documents.")}},
        "DocumentReference": {"ID": V(f.numbers["packing"], "The packing list of the container.")},
        "TransportHandlingUnit": {"TransportEquipment": sea_equipment(f, True)}})
    return out


DEPOSIT = Decimal("10000.00")       # paid by the island buyer when the order was accepted


def sea_invoice_terms(f, out):
    """The export invoice: the deposit paid on order, the balance due 45 days after shipment, the amount in coral
    for the buyer's information, and the delivery terms the customs need."""
    lmt = out["LegalMonetaryTotal"]
    total = Decimal(lmt["PayableAmount"].value)
    balance = total - DEPOSIT
    out["PrepaidPayment"] = {"ID": V("VT-DEP-26-0412", "The buyer's payment of the deposit."),
                             "PaidAmount": amount(DEPOSIT, "XBL", "The deposit asked for in the order response."),
                             "ReceivedDate": V(f.date(5), "Credited to the distributor's account."),
                             "PaidDate": V(f.date(4), "Paid by the buyer the day after the order was accepted."),
                             "InstructionID": V("VT-PAY-26-0077", "The buyer's payment order.")}
    lmt["PrepaidAmount"] = amount(DEPOSIT, "XBL", "The deposit, already paid.")
    lmt["PayableAmount"] = amount(balance, "XBL", "What is still to pay: the total less the deposit.")
    lmt["PayableAlternativeAmount"] = amount(balance * Decimal("0.4"), "XLC", "The same in coral, for the buyer's "
                                             "information, at the reference rate of the invoice date.")
    out["PaymentAlternativeCurrencyCode"] = V("XLC", "The buyer's own currency, in which the amount is shown too.")
    out["PaymentAlternativeExchangeRate"] = {
        "SourceCurrencyCode": V("XBL", "The invoice currency."), "TargetCurrencyCode": V("XLC", "The buyer's."),
        "CalculationRate": V("0.4", "The world's reference rate (world/countries.json)."),
        "MathematicOperatorCode": V("Multiply", "Lume times the rate gives coral."),
        "Date": V(f.date(10), "The rate of the invoice date.")}
    terms = out["PaymentTerms"]
    terms.pop("PaymentDueDate", None)
    out["PaymentTerms"] = [
        {"ID": V("DEPOSIT", "The deposit, the first instalment."),
         "PrepaidPaymentReferenceID": V("VT-DEP-26-0412", "The deposit payment, already received."),
         "PaymentPercent": V(str(round(DEPOSIT * 100 / total, 2)), "Its share of the invoice total."),
         "Amount": amount(DEPOSIT, "XBL", "The deposit."),
         "ReferenceEventCode": V("8", "Due when the order is accepted."),
         "InstallmentDueDate": V(f.date(5), "It was due on acceptance; paid.")},
        {**terms, "ID": V("BALANCE", "The balance, the second instalment."),
         "PaymentPercent": V(str(round(balance * 100 / total, 2)), "Its share of the invoice total."),
         "Amount": amount(balance, "XBL", "The balance."),
         "ReferenceEventCode": V("81", "Counted from the shipment on board."),
         "InstallmentDueDate": V(f.date(55), "45 days after the goods were shipped."),
         "PenaltyAmount": amount(balance * Decimal("1.5") / 100, "XBL", "The surcharge for the first month late, on "
                                                                         "the balance."),
         "InvoicingPartyReference": V(out["PaymentMeans"]["PaymentID"].value, "The reference to quote with the "
                                                                              "payment.")}]
    out["DeliveryTerms"] = {"ID": V("CIF", "Incoterms 2020: the customs of both countries need the terms on the "
                                           "invoice.", schemeID="INCOTERMS"),
                            "DeliveryLocation": kit.place("XLSEL", "The named port of destination.")}
    out["Note"] = V("This receivable has been assigned to Harbourline Factoring; pay only to the account stated.",
                    "The notice of assignment the factoring agreement requires.")
    f.numbers["invoice-amount"] = balance
    return out


def till(out, f, day, time, register, cashier):
    """What every till receipt of the store records: when, where and at which till."""
    out.update({"IssueTime": V(time, "Printed at the till."),
                "TransactionDate": V(f.date(day), "The day of the sale."),
                "TransactionTime": V(time, "The time of the sale."),
                "PurchaseDate": V(f.date(day), "The day the customer bought."),
                "PurchaseTime": V(time, "And when."),
                "CashRegister": {"ID": V(register, "The till."),
                                 "SerialNumberID": V(f"BM-POS-{register}-2219", "The till's serial number, as the "
                                                                                "tax rules require on a receipt.")},
                "CashierContact": {"Name": V(cashier, "The cashier, by first name, as printed.")},
                "PointOfSaleLocation": {"Name": V("Brightmarket Stores, Lumeport", "The shop."),
                                        "Description": V("Garden department, ground floor" if register == "G2" else
                                                         "Clothing, first floor", "Where in the shop.")},
                "PointOfSaleContact": {"Telephone": V(PARTY["26-xb"]["identity"]["contact"]["telephone"],
                                                      "The shop's number, for questions about the purchase.")}})
    return out


def card_payment(out, f, day, time):
    total = out["LegalMonetaryTotal"]["PayableAmount"]
    out["PaymentMeans"] = {
        "PaymentMeansCode": V("55", "UN/EDIFACT 4461 code 55: debit card.", listID="UN/EDIFACT EDED 4461"),
        "CardAccount": {**kit.card_account("c-xb", "26-xb"),
                        "RoleCode": V("HOLDER", "Paid by the card holder.")}}
    out["Payment"] = {"ID": V("BM-G2-26-0518-0047", "The till's number for the payment."),
                      "PaidAmount": total, "PaidDate": V(f.date(day), "Paid at the till."),
                      "PaidTime": V(time, "At the time of the sale."),
                      "MerchantID": V("LUMECARD-M-0026118", "The store's merchant number with the card scheme."),
                      "AuthorizationID": V("A71520", "The approval code of the card issuer."),
                      "TransactionID": V("TX-26-0518-773104", "The card transaction."),
                      "PaymentTerminalID": V("PT-G2", "The card terminal at the till."),
                      "StatusCode": V("APPROVED", "The payment was approved.")}
    return out


def cash_payment(out, f, day, time, tendered):
    lmt = out["LegalMonetaryTotal"]
    exact = Decimal(lmt["PayableAmount"].value)
    step = Decimal(WORLD["countries"]["XB"]["payment"]["cash_rounding"]["step"])
    rounded = (exact / step).quantize(Decimal(1), rounding="ROUND_HALF_UP") * step
    lmt["PayableRoundingAmount"] = amount(rounded - exact, "XBL", WORLD["countries"]["XB"]["payment"]["cash_rounding"]
                                          ["note"])
    lmt["PayableAmount"] = amount(rounded, "XBL", "What the customer pays in cash, rounded to 5 cents.")
    out["Payment"] = {"PaidAmount": amount(rounded, "XBL", "Paid."),
                      "PaidCashAmount": amount(tendered, "XBL", "The notes the customer handed over."),
                      "CashChangeAmount": amount(Decimal(tendered) - rounded, "XBL", "The change given back."),
                      "PaidDate": V(f.date(day), "At the till."), "PaidTime": V(time, "At the time of the sale.")}
    return out


def sea_order_response(f, n, doc):
    """The distributor confirms the island order in full: lines, totals, terms and the deposit it asks for."""
    out = kit.order_response(f, n, doc, 4, "The distributor accepts the order the next day.")
    seller, buyer = doc["from"], doc["to"]
    rows = kit.lines(f, seller, buyer, "XBL")
    base = sum(r[2] for r in rows)
    tax, total = kit.tax_total(rows, "XBL")
    so = f"LD-SO-26-{f.base:04d}"
    w = kit.gross_weight(f, "ordered")
    net = sum(Decimal(str(d["ordered"])) * Decimal(str(kit.maker(d["item"])["net_kg"])) for d in f.deal)
    bench = kit.maker("bench-serra-b")
    out.update({
        "SalesOrderID": V(so, "The distributor's own sales order number."),
        "IssueTime": V("09:30:00", "Sent in the morning."),
        "Note": V("Accepted. A deposit of 10,000.00 lume is due on acceptance; the balance 45 days after shipment.",
                  "The response in words."),
        "DocumentCurrencyCode": kit.currency_line("XBL", "the distributor's currency, as in the order"),
        "CustomerReference": V("Harbour parks Selanu", "The buyer's project, as the buyer named it when ordering."),
        "LineCountNumeric": V(str(len(rows)), "The number of lines."),
        "TotalPackagesQuantity": qty(kit.parcel_count(f), "EA", f"The parcels: "
                                     f"{sum(d['ordered'] for d in f.deal if d['item'] == 'bench-serra-b')} benches "
                                     f"in three parcels each and "
                                     f"{sum(d['ordered'] for d in f.deal if d['item'] == 'bench-casting-b')} frame "
                                     "cartons (D20)."),
        "GrossWeightMeasure": qty(w, "KGM", "The expected gross weight, for the booking."),
        "NetWeightMeasure": qty(net, "KGM", "The goods alone."),
        "GrossVolumeMeasure": V(kit.kg(kit.pallets_volume(f)), f"The {len(kit.pallets(f, f.deal))} loaded pallets: "
                                f"the bench pallets two high, they take {sea_floor_places(f)} of the 40-foot "
                                "container's 18 floor places.", unitCode="MTQ"),
        "AccountingSupplierParty": {"Party": party(seller, short=True)},
        "AccountingCustomerParty": {"Party": party(buyer, short=True)},
        "DeliveryTerms": {"ID": V("CIF", "Incoterms 2020, as ordered.", schemeID="INCOTERMS"),
                          "DeliveryLocation": kit.place("XLSEL", "The named port.")},
        "PaymentMeans": kit.payment_means(f, seller, buyer, seller, 4, 1, so, "The distributor's account for the "
                                          "deposit."),
        "PaymentTerms": {"ID": V("DEPOSIT", "The deposit."),
                         "Note": V("Deposit due on acceptance.", "The first instalment."),
                         "Amount": amount(DEPOSIT, "XBL", "The deposit asked."),
                         "PaymentDueDate": V(f.date(5), "Within a day.")},
        "TransactionConditions": {"ID": V("LD-TC-01", "The distributor's conditions of sale."),
                                  "Description": V("Sold to trade customers only.", "The condition.")},
        "DestinationCountry": {"IdentificationCode": V("XL", "The goods go to the island.")},
        "TaxTotal": total,
        "LegalMonetaryTotal": {"LineExtensionAmount": amount(base, "XBL", "The sum of the lines."),
                               "PayableAmount": amount(base + tax, "XBL", "The goods; freight and insurance follow "
                                                                          "on the invoice under CIF.")},
        "OrderLine": [{"LineItem": {
            "ID": V(str(i), "The line number, as in the order."),
            "SalesOrderID": V(f"{so}/{i}", "The distributor's line in its sales order."),
            "Note": V("Confirmed as ordered.", "The line's status in words."),
            "Quantity": qty(q, ITEM[d["item"]]["unit"], "The quantity confirmed."),
            "LineExtensionAmount": amount(amt, "XBL", "As ordered."),
            "TaxInclusiveLineExtensionAmount": amount(amt, "XBL", "No tax on an export: the same amount."),
            "TotalTaxAmount": amount(0, "XBL", "No tax on an export."),
            "PartialDeliveryIndicator": V("false", "All in one container."),
            "BackOrderAllowedIndicator": V("false", "Nothing is back-ordered: all is in stock."),
            "Delivery": {"PromisedDeliveryPeriod": {"StartDate": V(f.date(10), "Shipped on the sailing of day 10."),
                                                    "EndDate": V(f.date(SEA_ARRIVES), "Arriving at Selanu.")}},
            "WarrantyInformation": V(bench["warranty"], "The maker's warranty passes to the buyer."),
            "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
            "WarrantyParty": party(bench["seller"], short=True),
            "Price": kit.price_block(d["item"], "XBL", buyer),
            "Item": {"Name": V(ITEM[d["item"]]["name"], "Named only: described in full in the order."),
                     "SellersItemIdentification": {"ID": V(ITEM[d["item"]]["sellers_id"], "The seller's number.")}}},
            "OrderLineReference": {"LineID": V(str(i), "The order line answered.")}}
            for i, (d, q, amt, rule) in enumerate(rows, 1)]})
    return out


def sea_consignment_fi(f, doc):
    f.number("consignment", doc["from"], "Consignment")
    return sea_consignment(f, "instructions")


def sea(n, doc):
    f = SEA
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Catalogue":
        return kit.catalogue(f, n, doc, 0, "The export catalogue for the island customer.",
                             ["bench-serra-b", "bench-casting-b"], 180, alternative="XLC")
    if doc["doc"] == "DigitalAgreement":
        return {"ID": V(f.number("agreement", doc["from"], "DigitalAgreement"), "The agreement's number."),
                "IssueDate": V(f.date(1), "Signed before the first order."),
                "VersionID": V("1.0", "The first version of the agreement."),
                "DigitalProcess": [{"ID": V(p, "A process the parties agree to exchange electronically."),
                                    "Description": V(d, "What the process covers.")}
                                   for p, d in (("ordering", "Order, order response and order change."),
                                                ("billing", "Invoice, credit note, statement and remittance advice."))]}
    if doc["doc"] == "DigitalCapability":
        return {"ID": V(f.number("capability", doc["from"], "DigitalCapability"), "The governor's number."),
                "IssueDate": V(f.date(1), "Sent when the buyer joins the agreement."),
                "DigitalProcess": [{"ID": V(p, "A process the distributor supports."),
                                    "Description": V(d, "What it covers.")}
                                   for p, d in (("ordering", "Receives orders and order changes, sends order "
                                                             "responses."),
                                                ("billing", "Sends invoices and statements, receives remittance "
                                                            "advices."))]}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 3, "The island buyer orders benches for its city's parks.",
                         "Cost, insurance and freight to the port of Selanu: the seller pays the sea freight and insures "
                         "the cargo; the risk passes when the goods are on board in Lumeport.", "Port of Selanu",
                         {"CustomerReference": V("Harbour parks Selanu", "The buyer's project, for which it "
                                                 "places the order: the Port of Selanu's benches of line 1; the "
                                                 "other lines are for the buyer's own stock and travel in the same "
                                                 "container (O172)."),
                          "Delivery": {"DeliveryLocation": {"Description": V("Lanoro warehouse, Selanu",
                                                                             "The buyer's 3PL, where the goods go after "
                                                                             "customs clearance.")}}})
    if doc["doc"] == "OrderResponse":
        return sea_order_response(f, n, doc)
    if doc["doc"] == "ForwardingInstructions" and doc["from"] == "6-xb":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The distributor's "
                                                                                       "instruction number."),
                "IssueDate": V(f.date(5), "The distributor instructs its forwarder once the order is accepted."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": sea_consignment_fi(f, doc),
                             "InsurancePolicy": {
                                 "InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                              "CIF requires insurance of at least 110 % of the value; "
                                                              "the CIF value is the goods, freight and insurance."),
                                 "InsuranceTypeDescription": V("Cargo insurance, all risks", "The cover the forwarder "
                                                                                            "is to arrange.")}}}
    if doc["doc"] == "PackingList":
        return {"ID": V(f.number("packing", doc["from"], "PackingList"), "The distributor's packing list number."),
                "IssueDate": V(f.date(8), "Made when the container is packed."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment packed."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")},
                             "GoodsItem": kit.goods_items(f, "XBL", "The value of the goods, in lume."),
                             "NetWeightMeasure": qty(sum(Decimal(str(d["ordered"])) *
                                                         Decimal(str(kit.maker(d["item"])["net_kg"])) for d in f.deal),
                                                     "KGM", "The goods without packaging."),
                             "NetVolumeMeasure": V(kit.kg(kit.goods_volume(f)), "The volume of the goods "
                                                   "themselves, knocked down and without packaging: the envelopes of "
                                                   "the side frames and slats.", unitCode="MTQ"),
                             "TotalTransportHandlingUnitQuantity": qty(len(kit.pallets(f, f.deal)), "EA",
                                                                       f"{len(kit.pallets(f, f.deal))} pallets in the "
                                                                       "container."),
                             "ShippingPriorityLevelCode": V("STANDARD", "No priority: the next sailing will do."),
                             "HandlingInstructions": V("Castings pallet at the doors.", "How the container is "
                                                                                       "stowed."),
                             "SpecialInstructions": V("Photograph the load before closing the doors.", "For any "
                                                                                                       "damage claim."),
                             "DeliveryInstructions": V("Deliver to the buyer's 3PL, Nalevi Warehousing, Selanu.",
                                                       "Where the goods end up."),
                             **container(f, "The verified gross mass: cargo and the container's own weight of 3,750 "
                                            "kg.")}}
    if doc["doc"] == "ExportCustomsDeclaration":
        out = kit.export_declaration(f, n, doc, 8, "The forwarder, as customs agent, declares the export at the "
                                                   "seaport.", "The value of the goods at export, in lume.")
        goods = sea_goods(f)
        kit.deep_merge(out["CustomsDeclaration"]["Shipment"], {
            "FreeOnBoardValueAmount": amount(goods, "XBL", "On board in Lumeport."),
            "InsuranceValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL", "The cargo insurance the seller "
                                                                                 "took out under CIF."),
            "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The sea freight, paid by the seller."),
                                       "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                       "AllowanceChargeReason": V("Ocean freight to Selanu", "Stated because it is "
                                                                  "part of the CIF price, not of the export value."),
                                       "Amount": amount(SEA_FREIGHT, "XBL", "Freight and bunker surcharge.")},
            "Consignment": {"OfficeOfExportLocation": {"Name": V("Customs office, port of Lumeport", "Where the "
                                                                 "export is declared.")},
                            "OfficeOfExitLocation": {"Name": V("Customs office, port of Lumeport", "Where the goods "
                                                               "leave Bayvarra: the same port.")}}})
        return out
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions-carrier", doc["from"], "ForwardingInstructions"),
                        "The forwarder's booking number with the ocean carrier."),
                "IssueDate": V(f.date(6), "The forwarder books the container."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the goods."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")}}}
    if doc["doc"] == "TransportationStatus" and doc["from"] == "16-xb":
        return kit.transportation_status(f, n, doc, 10, "Reported when the container is on board.",
                                         f"Container {CONTAINER} loaded on board.", "Port of Lumeport, container quay",
                                         {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("2", "The sea leg, stage 2 as on the bill of lading."),
                                             "ActualDepartureTransportEvent": kit.event(f, 10, SEA_SAILED + ":00", "The ship "
                                                                                        "sailed.", location=SEA_LUMEPORT),
                                             "SecurityOfficerPerson": kit.person("Tamsin", "Orrel", "The port "
                                                                                 "facility security officer who "
                                                                                 "cleared the loading.",
                                                                                 job="Port facility security officer")}}}, event_type="LOADING")
    if doc["doc"] == "BillOfLading":
        return {"ID": V(f.number("bl", doc["from"], "BillOfLading"), "The bill of lading number."),
                "IssueDate": V(f.date(10), "Issued when the goods are shipped on board."),
                "CarrierAssignedID": V(SEA_BOOKING, "The booking the bill of lading is issued under."),
                "ToOrderIndicator": V("true", "Made out to order: the buyer can transfer it by endorsement."),
                "ShippingOrderID": V(f.numbers["instructions-carrier"], "The forwarder's booking with the carrier."),
                "OtherInstruction": V("Three originals issued.", "How many originals there are."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment carried."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the cargo."),
                             "TotalGoodsItemQuantity": qty(2, "EA", "Benches and side frames."),
                             "ConsignmentQuantity": qty(1, "EA", "One consignment."),
                             "Consignment": sea_consignment(f, "bl"),
                             "InsurancePolicy": {"InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                                              "The insured value, 110 % of the CIF "
                                                                              "value.")},
                             }}
    if doc["doc"] == "Manifest":
        return {"ID": V(f.number("manifest", doc["from"], "Manifest"), "The carrier's cargo manifest number."),
                "IssueDate": V(f.date(11), "Sent to the island's customs before arrival."),
                "ManifestTypeCode": V("CARGO", "A cargo manifest, of what the ship carries for Selanu."),
                "CrewPerson": [kit.person("Corin", "Halvard", "The master of the ship.", role="MASTER"),
                               kit.person("Elsbeth", "Marrin", "The chief officer.", role="CHIEFOFFICER")],
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment on the manifest."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of this shipment."),
                             "FirstArrivalPortLocation": kit.place("XLSEL", "The ship's first port on the island."),
                             "LastExitPortLocation": kit.place("XBLMP", "Its last port in Bayvarra."),
                             "ShipmentStage": {
                                 "ID": V("2", "The sea leg."),
                                 "TransportModeCode": V("1", "Maritime transport.", listID="UNECE Recommendation 19 - "
                                                                                           "Codes for Modes of "
                                                                                           "Transport"),
                                 "TransportMeans": kit.means("11-xb", "TH", "TH-26-19E", "The voyage number.",
                                                             "EB"),
                                 "CrewQuantity": qty(14, "IE", "The crew on board: 14 persons."),
                                 "MasterPerson": kit.person("Corin", "Halvard", "The master, who signs the manifest.",
                                                            role="MASTER"),
                                 "EstimatedArrivalTransportEvent": kit.event(
                                     f, 12, sea_quarter(SEA_OFF_SELANU), f"Expected off Selanu in the evening, in "
                                     f"island time, an hour ahead of Lumeport's: {wmap.nearest(SEA_KM, 10):,} km at "
                                     f"{wmap.KNOTS} knots, about {wmap.whole(SEA_HOURS)} hours at sea. The ship "
                                     "berths the next morning at first light.", location=SEA_SELANU),
                                 "EstimatedDepartureTransportEvent": kit.event(f, 10, SEA_SAILS + ":00", "The "
                                                                               "timetable departure from Lumeport, "
                                                                               "in Lumeport's time.", location=SEA_LUMEPORT)},
                             "TransportHandlingUnit": {"TransportEquipment": sea_equipment(f, False)}}}
    if doc["doc"] == "CommonTransportationReport":
        return {"ID": V(f.number("ctr", doc["from"], "CommonTransportationReport"), "The carrier's report number."),
                "IssueDate": V(f.date(12), "Sent before the ship enters the port of Selanu."),
                "IssueTime": V(SEA_REPORTS + ":00", "Sent a few hours before the ship comes off the port."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment the report is for."),
                             "ShipmentStage": {"ID": V("1", "The sea leg to Selanu."),
                                               "ISPSRequirements": {
                                                   "ID": V("ISSC-XB-2023-0117", "The number of the ship's International "
                                                                                 "Ship Security Certificate, issued "
                                                                                 "by its flag state, Bayvarra."),
                                                   "ValidISSCIndicator": V("true", "The ship holds a valid security "
                                                                                   "certificate."),
                                                   "ISSCExpiryDate": V("2028-09-30", "The certificate is valid for five "
                                                                                     "years from its issue."),
                                                   "CurrentOperatingSecurityLevelCode": V("1", "Security level 1, the "
                                                                                              "normal level.")}}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, SEA_ARRIVES, "Reported when the container is discharged.",
                                         f"Container {CONTAINER} discharged and available for customs clearance.",
                                         "Port of Selanu", {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("2", "The sea leg, stage 2 as on the bill of lading."),
                                             "ActualArrivalTransportEvent": kit.event(f, SEA_ARRIVES, "06:30:00", "The ship "
                                                                                      "berthed at Selanu: its pilot "
                                                                                      "boarded at first light; it "
                                                                                      "had been off the port, under "
                                                                                      "way, since the evening.", location=SEA_SELANU),
                                             "DischargeTransportEvent": kit.event(f, SEA_ARRIVES, "11:20:00", "The container "
                                                                                  "came off the ship.", done=True, location=SEA_SELANU),
                                             "DetentionTransportEvent": kit.event(
                                                 f, SEA_ARRIVES, "12:00:00", "Held by customs for a check of the pallets.",
                                                 description="Wooden pallets must carry the heat-treatment mark.", location=SEA_SELANU),
                                             "ReportingPerson": kit.person("Ama", "Kelune", "The terminal's duty "
                                                                           "officer who reports.", job="Duty "
                                                                           "officer")},
                                             "TransportHandlingUnit": {"TransportEquipment": {
                                                 "ID": V(CONTAINER, "The container.", schemeID="ISO6346"),
                                                 "QuarantineTransportEvent": kit.event(
                                                     f, SEA_ARRIVES, "15:00:00", "Released from the quarantine check: all "
                                                     "pallets heat-treated.", done=True, location=SEA_SELANU),
                                                 "ServiceAllowanceCharge": {
                                                     "ChargeIndicator": V("true", "A service charge."),
                                                     "AllowanceChargeReasonCode": V("HD", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                                     "AllowanceChargeReason": V("Terminal handling at Selanu",
                                                                                "For unloading the box."),
                                                     "Amount": amount(Decimal("185.00"), "XBL", "As in the carrier's "
                                                                                                "tariff.")},
                                                 "TransportEvent": kit.event(f, SEA_ARRIVES, "11:40:00", "Stacked in the "
                                                                                                "import yard.", location=SEA_SELANU, type_code="STORAGE")}}}}, event_type="DISCHARGE")
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return kit.invoice(f, n, doc, 15, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container."},
                            {"item": "export-clearance", "qty": 1, "invoice_why": "One export declaration."},
                            {"item": "cargo-insurance", "qty": 1, "invoice_why": "Insurance of this shipment.",
                             "unit_price": f"{INSURANCE:.2f}",
                             "unit_price_why": f"The premium: {insurance_basis()}, the cover CIF asks (O173).",
                             "line_extra": {
                                 "Note": V(f"Premium {INSURANCE_RATE} % of the insured value, {INSURED:,.2f} lume.",
                                           "The basis of the premium, for the distributor's check: the rate of the "
                                           "cargo policy on the CIF value plus 10 % (O173)."),
                                 "DocumentReference": {"ID": V("WS-CERT-26-0884", "The insurance certificate of "
                                                                                  "the shipment, which states the "
                                                                                  "insured value.")}}}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, SEA_ARRIVES + 1, "The customs broker declares the import for the "
                                     "buyer, on the first working day after the ship berthed.",
                                      "The customs value in coral: the goods' value in lume at the world's reference "
                                      "rate (1 lume = 0.4 coral).",
                                      {"ID": V(f.numbers["bl"], "The bill of lading of the goods.")})
        out["ImporterParty"] = {
            "AgentParty": party("3-xl", short=True),
            "PowerOfAttorney": {"ID": V("POA-TT-2026-014", "The number of the power of attorney the buyer gave its "
                                                           "customs broker."),
                                "IssueDate": V("2026-01-05", "Given at the start of the year, for all of the year's "
                                                             "imports."),
                                "Description": V("Lodging import declarations and paying duties and taxes on behalf of "
                                                 "Velumi Trading.", "What the broker may do for the buyer."),
                                "AgentParty": party("3-xl", short=True),
                                "MandateDocumentReference": {"ID": V("MAND-2026-014", "The signed mandate kept by the "
                                                                                      "broker.")}}}
        first = out["Shipment"]["GoodsItem"][0]
        first["FreightAllowanceCharge"] = {"ChargeIndicator": V("true", "The share of the sea freight in the customs "
                                                                        "value."),
                                           "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                           "AllowanceChargeReason": V("Ocean freight, share of the benches",
                                                                      "Part of the CIF value."),
                                           "Amount": amount(SEA_FREIGHT * sea_goods(f, "bench-serra-b") / sea_goods(f)
                                                            * Decimal("0.4"), "XLC",
                                                            "The benches' share of the 2,950 lume freight by value "
                                                            f"({sea_goods(f, 'bench-serra-b'):,.0f} of "
                                                            f"{sea_goods(f):,.0f} lume), in coral at 0.4.")}
        first["InsurancePolicy"] = {"ID": V("WS-CP-26-4471", "The cargo policy covering the goods."),
                                    "InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                                 "As on the insurance certificate.")}
        first["InvoiceLine"] = [{"ID": V(str(i), "A line of the seller's invoice for these goods: the benches are "
                                                 "on two lines, the port's and the buyer's own stock (O172)."),
                                 "InvoicedQuantity": qty(d["ordered"], "EA", "The benches invoiced on the line."),
                                 "Item": {"Name": V(ITEM["bench-serra-b"]["name"], "Named only: described in full "
                                                                                   "above.")}}
                                for i, d in enumerate(f.deal, 1) if d["item"] == "bench-serra-b"]
        return out
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 9, "Sent to the delivery party named in the order when the container "
                                                 "leaves.", "The gross weight of the goods.")
    if doc["doc"] == "ReceiptAdvice":
        return kit.receipt_advice(f, n, doc, SEA_ARRIVES + 3, "The buyer's 3PL confirms what arrived.")
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 10, "Issued when the goods are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
                           charges=[{"like": "bench-serra-b", "reason": "Sea freight", "amount": SEA_FREIGHT, "code": "FC", "code_why": "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services).",
                                     "why": "Under CIF the seller pays the sea freight and charges it on the invoice.",
                                     "amount_why": "The freight the forwarder charged for the container."},
                                    {"like": "bench-serra-b", "reason": "Cargo insurance", "amount": INSURANCE, "code": "96",
                                     "code_why": "UN/EDIFACT 7161 has no code for insurance, so the code is from UN/EDIFACT 5189, with that list's listID.",
                                     "why": "Under CIF the seller insures the cargo and charges the insurance.",
                                     "amount_why": f"The premium of the cargo insurance, as the forwarder charged "
                                                   f"it: {insurance_basis()} (O173)."}],
                           terms=("until-O72", 45))    # the balance term is settled with the sea flow (O72)
        return sea_invoice_terms(f, out)
    if doc["doc"] == "Statement":
        cur, total = "XBL", f.numbers["invoice-amount"]
        out = {"ID": V(f.number("statement", doc["from"], "Statement"), "The factor's statement number."),
                "IssueDate": V(f.date(40), "The monthly statement of account."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoices"),
                "StatementTypeCode": V("ACCOUNT", "A statement of the account."),
                "Note": V("Statement on behalf of Lumeway Distribution, whose receivables Harbourline Factoring "
                          "holds.", "Who the statement is for."),
                "TotalDebitAmount": amount(total + DEPOSIT, cur, "The invoice in full."),
                "TotalCreditAmount": amount(DEPOSIT, cur, "The deposit the buyer paid on the order."),
                "TotalBalanceAmount": amount(total, cur, "What is owed."),
                "LineCountNumeric": V("2", "The invoice and the deposit."),
                "AdditionalDocumentReference": {"ID": V("HF-FA-2026-007", "The factoring agreement between the "
                                                                          "distributor and the factor.")},
                "BuyerCustomerParty": {"Party": party("1-xl", short=True)},
                "SellerSupplierParty": {"Party": party("6-xb", short=True)},
                "PaymentTerms": {"Note": V("Pay the balance by the due date of the invoice.", "The terms."),
                                 "PaymentDueDate": V(f.date(55), "The due date.")},
                "Signature": {"ID": V("HF-SIG-26-0040", "The factor's seal on the statement."),
                              "SignatoryParty": party("24-xb", short=True)},
                "StatementPeriod": {"StartDate": V(f.date(10), "From the invoice."),
                                    "EndDate": V(f.date(40), "To the statement date.")},
                "PaymentMeans": kit.payment_means(f, "24-xb", "1-xl", "24-xb", 40, 15, f.numbers["invoice"],
                                                  "The factor's account, where the invoice is to be paid."),
                "StatementLine": {"ID": V("1", "The open invoice."),
                                  "Note": V("Balance after the deposit of 10,000.00 lume.", "What the line shows."),
                                  "BalanceBroughtForwardIndicator": V("false", "A new item, not a balance carried "
                                                                               "over."),
                                  "DebitLineAmount": amount(total, cur, "The amount of the invoice, owed to the factor."),
                                  "BalanceAmount": amount(total, cur, "Still open: nothing paid yet."),
                                  "PaymentPurposeCode": V("GDDS", "ISO 20022 purpose code GDDS: purchase of goods."),
                                  "PaymentTerms": {"PaymentDueDate": V(f.date(55), "The due date of the balance.")},
                                  "BuyerCustomerParty": {"Party": party("1-xl", short=True)},
                                  "SellerSupplierParty": {"Party": party("6-xb", short=True)},
                                  "DocumentReference": {"ID": V("HF-ASSIGN-26-0091", "The notice of assignment of "
                                                                                     "the invoice to the factor.")},
                                  "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                                   "TargetCurrencyCode": V("XLC", "The buyer's currency."),
                                                   "CalculationRate": V("0.4", "For the buyer's information.")},
                                  "BillingReference": {"InvoiceDocumentReference": {
                                      "ID": V(f.numbers["invoice"], "The distributor's invoice, which the factor "
                                                                    "bought."),
                                      "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}}}}
        out["StatementLine"].update({"DebitLineAmount": amount(total + DEPOSIT, cur, "The invoice in full."),
                                     "BalanceAmount": amount(total + DEPOSIT, cur, "Before the deposit."),
                                     "Note": V("The invoice, bought by the factor.", "What the line shows."),
                                     "AccountingCustomerParty": {"Party": party("1-xl", short=True)},
                                     "AccountingSupplierParty": {"Party": party("6-xb", short=True)},
                                     "PayeeParty": party("24-xb", short=True)})
        out["StatementLine"] = [out["StatementLine"], {
            "ID": V("2", "The deposit."),
            "Note": V("Paid to the distributor before the invoice was assigned.", "Why it is a credit."),
            "CreditLineAmount": amount(DEPOSIT, cur, "The deposit."),
            "BalanceAmount": amount(total, cur, "Open after the deposit: what the buyer still owes."),
            "CollectedPayment": {"ID": V("VT-DEP-26-0412", "The deposit payment."),
                                 "PaidAmount": amount(DEPOSIT, cur, "Paid."),
                                 "ReceivedDate": V(f.date(5), "Received by the distributor.")},
            "PaymentMeans": {"PaymentMeansCode": V("30", "Paid by credit transfer.", listID="UN/EDIFACT EDED 4461")},
            "InvoicePeriod": {"StartDate": V(f.date(4), "The order's deposit period."),
                              "EndDate": V(f.date(5), "Paid and received.")}}]
        return out
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 52, "The buyer pays the factor, before the due date, less the credit note.",
                              credit=(f.numbers["sea-credit"], f.numbers["sea-credit-date"],
                                      f.numbers["sea-credit-amount"]))
    if doc["doc"] == "CreditNote":
        out = kit.credit_note(f, n, doc, 42, "Issued when the distributor accepted the buyer's claim.",
                              [{"item": "bench-casting-b", "qty": 1, "why": "The frame that arrived cracked.",
                                "line_extra": {"Note": V("Frame carton crushed at the port of Selanu.", "What happened.")}}],
                              {"BillingReference": {"InvoiceDocumentReference": {
                                  "ID": V(f.numbers["invoice"], "The invoice of the frames."),
                                  "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                               "Note": V("Under CIF the risk was the buyer's on board; the distributor credits the "
                                         "frame as a goodwill gesture and claims from the insurer.", "Why a credit "
                                                                                                    "under CIF."),
                               "DiscrepancyResponse": {"ResponseCode": V("17", "The goods arrived damaged."),
                                                       "Description": V("One side frame cracked.", "In words.")},
                               "OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                               "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The 3PL's receipt "
                                                                                          "advice reporting it.")},
                               "StatementDocumentReference": {"ID": V(f.numbers["statement"], "The factor's statement "
                                                                      "the invoice is on.")},
                               "OriginatorDocumentReference": {"ID": V("VT-CLAIM-26-0019", "The buyer's claim.")},
                               "BuyerAssignedReference": {"BuyerReferenceCode": V("VT-CLAIMS", "The buyer's claims "
                                                                                               "desk.")},
                               "Delivery": {"ActualDeliveryDate": V(f.date(SEA_ARRIVES + 3), "The goods arrived at the 3PL.")},
                               "DeliveryTerms": {"ID": V("CIF", "As sold.", schemeID="INCOTERMS")},
                               "PaymentAlternativeCurrencyCode": V("XLC", "The buyer's currency, shown too."),
                               "PaymentAlternativeExchangeRate": {
                                   "SourceCurrencyCode": V("XBL", "The credit's currency."),
                                   "TargetCurrencyCode": V("XLC", "The buyer's."),
                                   "CalculationRate": V("0.4", "The reference rate.")},
                               "Annotation": {"AnnotationContent": V("Claimed from Wavesure Cargo Insurance under "
                                                                     "policy WS-CP-26-4471.", "Where the cost goes "
                                                                                              "in the end.")},
                               "Signature": {"ID": V("LD-SIG-26-0042", "The distributor's seal."),
                                             "SignatoryParty": party("6-xb", short=True)}})
        f.numbers["sea-credit"] = out["ID"].value
        f.numbers["sea-credit-date"] = f.date(42)
        f.numbers["sea-credit-amount"] = Decimal(out["LegalMonetaryTotal"]["PayableAmount"].value)
        return out
    raise SystemExit(f"sea scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the air flow (an urgent part, CPT airport)
AIR = kit.Flow("air", "2026-05-11", [
    {"item": "bench-casting-b", "ordered": 8, "why": "Eight side frames, needed before the ship arrives.",
     "line": "4",       # added by the order change to the sea order's lines 1 to 3 (air/01#F1, O172)
     # the trade price: Lumeway's island price is a CIF price with the sea freight in it; the air freight comes on
     # the invoice as a surcharge at cost (O30, owner 2026-11-19)
     "unit_price": f'{ITEM["bench-casting-b"]["price"]["amount"]:.2f}',
     "unit_price_why": "Lumeway's trade price, carriage paid to Selanu airport: its price for the island is a CIF "
                       "price with the sea freight in it, and the air freight is charged on top, at cost."}])


def air_freight(f):
    """The air freight of the urgent frames, which Lumeway pays its forwarder under CPT (air/10) and recharges to
    the buyer in full, at cost: a pass-through (O30, owner 2026-11-19; the amount is settled with D39)."""
    return money(air_chargeable(f) * Decimal(str(ITEM["air-freight"]["price"]["amount"])), "XBL")


# the skid the eight frame cartons are stacked and strapped on (D39, air/03#F9): two softwood runners and a deck,
# a little larger than a carton (790 x 680 mm), about 7 kg; the stack of eight cartons is 800 mm high
AIR_SKID = {"mm": [800, 700, 120], "tare_kg": Decimal("7.0")}


def air_gross(f):
    """The gross weight of the urgent consignment: the eight frame cartons and the skid."""
    return kit.gross_weight(f, "ordered") + AIR_SKID["tare_kg"]


def air_volume(f):
    """The gross volume of the consignment as built, in m³: the skid's footprint times the height of the eight
    cartons stacked on it and of the skid (D20, D39)."""
    c, k = kit.maker("bench-casting-b")["carton"]["mm"], AIR_SKID["mm"]
    return kit.volume_m3([k[0], k[1], 8 * c[2] + k[2]]).quantize(Decimal("0.01"))


def air_chargeable(f):
    """The chargeable weight of the urgent frames: the higher of the gross weight and the volume weight (167 kg per
    m³), rounded up to the next half kilogram, as airlines charge."""
    w = max(air_gross(f), air_volume(f) * 167)
    return (w * 2).to_integral_value(rounding="ROUND_CEILING") / 2


def air_surcharge(f, why, amount_why):
    """The air-freight surcharge as a charge: UN/EDIFACT 7161 FC, freight service."""
    return {"like": "bench-casting-b", "reason": "Air freight for the urgent delivery, recharged at cost",
            "amount": air_freight(f), "code": "FC",
            "code_why": "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services).",
            "why": why, "amount_why": amount_why}


def air_charge(c):
    """The surcharge as cac:AllowanceCharge of a document without tax totals (the order response)."""
    return {"ChargeIndicator": V("true", "A charge, not an allowance: it adds to the amount."),
            "AllowanceChargeReasonCode": V(c["code"], c["code_why"]),
            "AllowanceChargeReason": V(c["reason"], c["why"]),
            "Amount": amount(c["amount"], "XBL", c["amount_why"])}


# the morning flight Lumeport - Selanu (D19 as corrected with D36, O123): the ATR's block time eastbound is 2 h 45,
# a margin over the flight the great circle between the airports needs in still air (taxiing 10 minutes, climb and
# descent 20, the rest at 500 km/h); the island's clocks are an hour ahead
FLIGHT_BLOCK_EAST = 2.75
if (10 + 20) / 60 + max(0.0, wmap.air_km() - 100) / 500 > FLIGHT_BLOCK_EAST:
    raise SystemExit("air: the flight no longer fits its block time of 2 h 45 (O152, O123)")
FLIGHT_ARRIVES = wmap.after(wmap.at("2026-05-14", "07:00"), FLIGHT_BLOCK_EAST + 1)
# D39: the frames are booked on the afternoon flight KXL209 of Wednesday 13 May (day 2), Lumeport 15:00 to Selanu
# 18:45; the truck from Ferrano is late, the cargo reaches the terminal after the acceptance cut-off at 12:00, is
# accepted that evening and flies on the morning flight KXL207 of Thursday 14 May (day 3), landing at about 10:30
AIR_BOOKED = ("KXL209", 2, "15:00", wmap.hm(wmap.after(wmap.at("2026-05-13", "15:00"), FLIGHT_BLOCK_EAST + 1)))
AIR_FLOWN = ("KXL207", 3, "07:00", wmap.hm(FLIGHT_ARRIVES))
AIR_CUTOFF = "12:00:00"
AIR_TRANSIT = "VI-TD-26-0513"      # Valdara's transit declaration, Ferrano to Selanu airport (D39, a cited document)


def air_flight(f, flight, why, planned=True):
    """The main carriage of the frames on a flight of the timetable (D39), with its airports and times."""
    no, day, dep, arr = flight
    kind = "Planned" if planned else "Estimated"
    return {"ID": V("1", "The flight."),
            "TransportModeCode": V("4", "Air transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                "Transport"),
            "TransportMeans": kit.means("12-xl", "KXL", no, why),
            "LoadingPortLocation": kit.place("XBLMA", "The airport of departure."),
            "UnloadingPortLocation": kit.place("XLSLA", "The airport of destination."),
            f"{kind}DepartureTransportEvent": kit.event(f, day, dep + ":00-01:00", "The flight's timetabled "
                                                        "departure, in Lumeport's time, with its offset (D27).",
                                                        location=kit.place("XBLMA", "The airport of departure.")),
            f"{kind}ArrivalTransportEvent": kit.event(f, day, arr + "+00:00", "The timetabled arrival, in island "
                                                      "time, an hour ahead of Lumeport's: a block time of 2 h 45 "
                                                      "eastbound (D19, D36, O123).",
                                                      location=kit.place("XLSLA", "The airport of destination."))}


def air_consignment(f, doc):
    """The distributor's instructions for the urgent frames: one skid of eight frame cartons."""
    cid = f.number("consignment", doc["from"], "Consignment")
    goods = Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]["amount"]))
    c = kit.maker("bench-casting-b")["carton"]["mm"]
    box = {"ID": V("LD-AIR-BOX", "The eight frame cartons as one package entry with their number: inner packages "
                                 "on the skid have a local identifier, without a scheme."),
           "Quantity": qty(8, "EA", "Eight side frames, one to a carton."),
           "PackagingTypeCode": V("CT", "UN/ECE Recommendation 21 code CT: carton."),
           "MeasurementDimension": [{"AttributeID": V("LENGTH", "Of one carton."),
                                     "Measure": V(str(c[0]), "In millimetres.", unitCode="MMT")},
                                    {"AttributeID": V("WIDTH", "Of one carton."),
                                     "Measure": V(str(c[1]), "In millimetres.", unitCode="MMT")},
                                    {"AttributeID": V("HEIGHT", "Of one carton."),
                                     "Measure": V(str(c[2]), "In millimetres.", unitCode="MMT")}],
           "GoodsItem": {"ID": V("1", "The side frames."),
                         "Description": V("Bench side frame castings", "In words.")},
           "DeliveryUnit": {"BatchQuantity": qty(8, "EA", "All eight delivered together.")},
           "Pickup": {"ID": V("BF-PU-26-0611", "The forwarder's pick-up order."),
                      "EarliestPickupDate": V(f.date(2), "Valdara casts the frames on 12 May and packs them on 13 "
                                                         "May; Trasvia brings them to the distributor's dispatch "
                                                         "area that morning (D39)."),
                      "PickupParty": party("10-xb", short=True)},
           "Despatch": {"RequestedDespatchDate": V(f.date(2), "For the afternoon flight KXL209 of 13 May.")},
           "Delivery": {"RequestedDeliveryPeriod": {"StartDate": V(f.date(2), "At Selanu airport on the evening of "
                                                                              "13 May, by KXL209."),
                                                    "EndDate": V(f.date(3), "At the latest the next day, before "
                                                                            "the ship arrives.")}},
           "Status": {"ConditionCode": V("SCHEDULED", "Not packed yet: the frames are cast today."),
                      "Description": V("Cast at Valdara on 12 May, galvanised and packed on 13 May, then trucked to "
                                       "the dispatch area under transit.", "Where they are and what follows.")}}
    return {"ID": V(cid, "The distributor's consignment number."),
            "GrossWeightMeasure": qty(air_gross(f), "KGM", f"The eight frame cartons and the skid of "
                                      f"{AIR_SKID['tare_kg']} kg they are strapped to."),
            "TotalGoodsItemQuantity": qty(1, "EA", "One kind of goods."),
            "NetNetWeightMeasure": qty(Decimal(8) * Decimal(str(kit.maker("bench-casting-b")["net_kg"])), "KGM",
                                       "The castings alone."),
            "NetVolumeMeasure": V(kit.kg(kit.goods_volume(f)), "The frames' own volume, without their cartons: the "
                                                                  "envelope of each frame.", unitCode="MTQ"),
            "DeclaredForCarriageValueAmount": amount(goods, "XBL", "Declared to the airline so its liability covers "
                                                                   "the value of the frames."),
            "DeclaredStatisticsValueAmount": amount(goods, "XBL", "The value for the export statistics."),
            "SplitConsignmentIndicator": V("false", "All eight cartons on one flight."),
            "ConsignmentQuantity": qty(1, "EA", "One consignment."),
            "FreightForwarderParty": party("10-xb", short=True),
            "TransportEvent": kit.event(f, 2, AIR_CUTOFF[:5] + ":00-01:00", "Latest acceptance at the cargo "
                                        "terminal for the afternoon flight KXL209 of 13 May.", done=False,
                                        location=kit.place("XBLMA", "The cargo terminal at Lumeport airport."),
                                        type_code="ACCEPTANCE"),
            "TransportHandlingUnit": {
                "ID": kit.unit_id("6-xb", f, 1, "The skid the cartons are strapped to"),
                "TransportHandlingUnitTypeCode": V("SI", "UN/ECE Recommendation 21 code SI: skid."),
                "ReferencedShipment": {"ID": V(f.numbers["shipment"], "The distributor's shipment on the skid.")},
                "Package": box}}


def air_despatch(f, out, flight, time, time_why):
    """A despatch advice of the frames states the flight they are booked on and when they are expected at Selanu
    airport: the missed flight makes the first one wrong, which is why it is cancelled and replaced (D39)."""
    no, day, dep, arr = flight
    out["IssueTime"] = V(time, time_why)
    sh = out["Shipment"]
    sh["Consignment"]["GrossWeightMeasure"] = qty(air_gross(f), "KGM", "The eight frame cartons and their skid.")
    sh["Consignment"]["MainCarriageShipmentStage"] = {
        "ID": V("1", "The flight."),
        "TransportModeCode": V("4", "Air transport.", listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
        "TransportMeans": kit.means("12-xl", "KXL", no, "The flight the frames are booked on.")}
    sh["Delivery"]["EstimatedDeliveryPeriod"] = {
        "StartDate": V(f.date(day), f"Expected at Selanu airport with {no}."),
        "StartTime": V(arr + "+00:00", "The flight's timetabled arrival, in island time."),
        "EndDate": V(f.date(day), "The same day.")}
    sh["Delivery"]["Despatch"] = {"ActualDespatchDate": V(f.date(AIR_BOOKED[1]), "The frames left the dispatch area "
                                                                                 "on 13 May.")}
    return out


def air(n, doc):
    f = AIR
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "OrderChange":
        order = kit.order(f, n, {**doc, "values": {"DeliveryTerms/ID": "CPT"}}, 0,   # CPT goes on the line below
                          "The buyer needs eight side frames urgently.",
                          "Carriage paid to the island's airport for the urgent frames: the distributor pays the air "
                          "freight; the rest of the order stays CIF by sea.", "Selanu airport, cargo terminal")
        order.pop("OrderTypeCode")
        air_base = Decimal(order["AnticipatedMonetaryTotal"]["LineExtensionAmount"].value)
        order["AnticipatedMonetaryTotal"] = {      # the amount of the change, as the definition says (air/01#F2)
            "LineExtensionAmount": amount(air_base, "XBL", "The change: the eight frames added; the sea order's "
                                                           "lines are unchanged."),
            "PayableAmount": amount(air_base, "XBL", "What the change adds to the goods of the order: no tax on an "
                                                     "export; the air freight comes on top, on the invoice, at cost.")}
        order["TaxTotal"]["TaxSubtotal"][0]["TaxableAmount"] = amount(air_base, "XBL", "The change; no tax on an "
                                                                                      "export.")
        order.setdefault("OrderReference", {})["SalesOrderID"] = V(
            SEA.numbers.get("sales-order", f"LD-SO-26-{SEA.base:04d}"), "The distributor's number of the order the "
            "change applies to: in the order reference, since the change's own SalesOrderID would be the seller's "
            "number of the change (air/01#F7).")
        order.update({
            "IssueTime": V("07:50:00", "First thing in the morning, when the shortage was noticed."),
            "Note": V("Add eight side frames by air; we pay the air freight as a surcharge at cost. The rest of the "
                      "order is unchanged.", "The change in words: the buyer asks for the urgent delivery and "
                                             "accepts that it pays for it."),
            "CustomerReference": V("Harbour parks Selanu", "The buyer's project."),
            "AccountingCustomerParty": {"Party": party("1-xl", short=True)},
            "AccountingSupplierParty": {"Party": party("6-xb", short=True)},
            "DestinationCountry": {"IdentificationCode": V("XL", "The island.")}})
        order.pop("DeliveryTerms", None)       # CPT once, on the air line (air/01#F5); under CPT the seller
        order["Delivery"] = {"NotifyParty": party("9-xl", short=True)}      # chooses the carrier (air/01#F6)
        order["OrderLine"][0]["LineItem"]["DeliveryTerms"] = {
            "ID": V("CPT", "Incoterms 2020: carriage paid to, for this line, the frames by air.", schemeID="INCOTERMS"),
            "SpecialTerms": V("The rest of the order stays CIF by sea.", "Why the line has terms of its own."),
            "DeliveryLocation": kit.place("XLSLA", "The named place: Selanu airport.")}
        change = f.number("order-change", doc["from"], "OrderChange")
        f.numbers["order"] = change     # the frames are ordered by this change of the sea order: no order of its own
        return {**order, "ID": V(change, "The number of this change."),          # (air/03#F1, 06#F1, 08#F2, C73)
                "SequenceNumberID": V("1", "The first change to the order."),
                "OrderReference": {"ID": V(SEA.numbers["order"], "The order of the sea flow that this change "
                                                                 "extends.")}}
    if doc["doc"] == "OrderResponse":
        out = kit.order_response(f, n, doc, 1, "The distributor accepts the change.")
        out["OrderReference"] = {"ID": V(SEA.numbers["order"], "The order that was changed.")}
        out.update({
            "OrderChangeDocumentReference": {"ID": V(f.numbers["order-change"], "The order change this response "
                                                                                "answers.")},
            "Note": V("Accepted: the frames fly on the afternoon flight KXL209 of 13 May; the forwarder is booked.",
                      "In words."),
            "NetNetWeightMeasure": qty(Decimal(8) * Decimal(str(kit.maker("bench-casting-b")["net_kg"])), "KGM",
                                       "The frames alone."),
            "NetVolumeMeasure": V(kit.kg(kit.goods_volume(f)), "Their own volume, without the cartons.", unitCode="MTQ"),
            **kit.cost_centre("1-xl", "The buyer's cost centre, from the change."),
            "AdditionalDocumentReference": {"ID": V("BF-QUOTE-AIR-26-0611", "The forwarder's quotation for the "
                                                                            "flight.")},
            "AllowanceCharge": air_charge(air_surcharge(
                f, "The air freight the buyer accepted in its change: the distributor pays it to its forwarder "
                   "under CPT and recharges it, without margin.",
                "As the forwarder quoted it for the eight frame cartons; invoiced at cost.")),
            "FreightForwarderParty": party("10-xb", short=True),
            "Signature": {"ID": V("LD-SIG-26-0512", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "OrderLine": {"LineItem": {
                "ID": V(f.deal[0]["line"], f"The added line, line {f.deal[0]['line']} of the order as changed."),
                "Quantity": qty(8, "EA", "Confirmed."),
                "Delivery": {"PromisedDeliveryPeriod": {
                    "StartDate": V(f.date(2), "The frames are promised at Selanu airport on 13 May, on KXL209 "
                                              "(air/02#F6)."),
                    "StartTime": V(AIR_BOOKED[3] + "+00:00", "The flight's arrival, in island time."),
                    "EndDate": V(f.date(2), "The same day.")}},
                "DeliveryTerms": {"ID": V("CPT", "Carriage paid to the airport of Selanu, for this line.",
                                          schemeID="INCOTERMS")},
                "Item": {"Name": V(ITEM["bench-casting-b"]["name"], "Named only."),
                         "SellersItemIdentification": {"ID": V(ITEM["bench-casting-b"]["sellers_id"], "The seller's "
                                                                                                      "number.")}}}}})
        return out
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The instruction number."),
                "IssueDate": V(f.date(1), "The distributor asks its forwarder to book air freight."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(air_gross(f), "KGM", "The gross weight of the eight frame "
                                                                            "cartons and their skid."),
                             "Consignment": air_consignment(f, doc)},
                "DocumentReference": {"ID": V(AIR_TRANSIT, "The transit declaration the frames travel under, from "
                                                           "Valdara at Ferrano to Selanu airport through the "
                                                           "distributor's cross-dock (D39); a document outside the "
                                                           "examples.")}}
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, AIR_FLOWN[1] - 1, "The air waybill, issued when the airline accepted the "
                                                      "cargo on the evening of 13 May, after the cut-off for KXL209.",
                          air_gross(f), "The gross weight of the cargo: the eight frame cartons and their skid.")
        out["IssueTime"] = V("20:15:00", "At acceptance, 19:15 in Lumeport (D39).")
        out["DocumentReference"] = {"ID": V(AIR_TRANSIT, "The transit declaration the frames travel under to Selanu "
                                                         "airport, the office of destination (D39); a document "
                                                         "outside the examples.")}
        out["DeclaredCarriageValueAmount"] = amount(Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]
                                                                             ["amount"])), "XBL",
                                                    "The value declared for carriage.")
        out["Shipment"]["DeclaredForCarriageValueAmount"] = amount(
            Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]["amount"])), "XBL",
            "The value declared on the air waybill, as the distributor instructed.")
        kit.deep_merge(out["Shipment"]["Consignment"], {
            "ChargeableWeightMeasure": qty(air_chargeable(f), "KGM", f"The gross weight of {kit.kg(w)} kg, rounded up "
                                           "to the next half kilogram: it is higher than the volume weight, "
                                           f"{kit.kg(air_volume(f))} m³ at 167 kg per m³."),
            "GrossVolumeMeasure": V(kit.kg(air_volume(f)), "The stack of eight frame cartons of "
                                    + " x ".join(map(str, kit.maker("bench-casting-b")["carton"]["mm"])) + " mm on "
                                    "its skid of " + " x ".join(map(str, AIR_SKID["mm"][:2])) + " mm.",
                                    unitCode="MTQ"),
            "SpecialServiceInstructions": V("Priority handling at Selanu: the customer is waiting.", "The service "
                                                                                                     "asked for."),
            "ShippingPriorityLevelCode": V("PRIORITY", "Flown on the first flight with room."),
            "MainCarriageShipmentStage": air_flight(f, AIR_FLOWN, "The morning flight of 14 May, with the airline's "
                                                                  "ICAO-style designator KXL, which no real airline "
                                                                  "holds: the cargo missed the cut-off for KXL209 of "
                                                                  "13 May (D39).")})
        return out
    if doc["doc"] == "TransportationStatus" and doc["from"] == "17-xb":
        out = kit.transportation_status(f, n, doc, 2, "Reported when the cargo was accepted, on the evening of 13 "
                                                      "May.",
                                        "Cargo accepted after the cut-off for KXL209 of 13 May and built up for "
                                        "KXL207 of 14 May.", "Lumeport airport, cargo terminal",
                                        {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}},
                                        event_type="ACCEPTANCE")
        out["IssueTime"] = V("19:20:00", "When the cargo had been accepted.")
        out["TransportEvent"]["OccurrenceTime"] = V("19:10:00-01:00", "Accepted at 19:10, long after the cut-off at "
                                                                "12:00 for the afternoon flight (D39).")
        return out
    if doc["doc"] == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, 2, "Sent to the buyer's 3PL when the forwarder's truck left the "
                                                "dispatch area for the airport.",
                                  "The gross weight of the frame cartons and their skid.")
        return air_despatch(f, out, AIR_BOOKED, "12:15:00", "When the forwarder's truck left the dispatch area, "
                                                            "late: Trasvia's truck from Ferrano had arrived late "
                                                            "(D39).")
    if doc["doc"] == "TransportationStatus":
        out = kit.transportation_status(f, n, doc, 3, "Reported when the cargo had landed and been unloaded.",
                                        "Cargo arrived on KXL207 and ready for customs clearance.",
                                        "Selanu airport, cargo terminal",
                                        {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}},
                                        event_type="ARRIVAL")
        out["IssueTime"] = V("10:55:00", "After unloading.")
        out["TransportEvent"]["OccurrenceTime"] = V("10:30:00+00:00", "KXL207 landed at about 10:30, a quarter of an hour "
                                                                "ahead of its timetable (O123).")
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "6-xb":
        if air_freight(f) != f.numbers["forwarder-invoice-amount"]:
            raise SystemExit("air: the surcharge is not the forwarder's invoice of the air freight (O30)")
        out = kit.invoice(f, n, doc, 4, "Issued the day after the flight, with the forwarder's invoice of the air "
                                        "freight it recharges.",
                          {"OrderReference": {"ID": V(SEA.numbers["order"], "The buyer's order, to which its order "
                                                                            "change added the frames.")},
                           "DespatchDocumentReference": {"ID": V(f.numbers["despatch-2"], "The despatch advice of "
                                                                 "the frames billed, which replaced the cancelled "
                                                                 "one.")}},
                          charges=[air_surcharge(
                              f, f"The air freight of the urgent frames, which the buyer accepted in its order "
                                 f"change: paid by the distributor under CPT and recharged at cost, a pass-through "
                                 f"(the forwarder's invoice {f.numbers['forwarder-invoice']}).",
                              "The forwarder's invoice of the flight, in full.")])
        out["Note"] = V("Air freight recharged at cost, as agreed in the order change.", "Why the invoice carries a "
                        "charge.")
        out["DeliveryTerms"] = {"ID": V("CPT", "Incoterms 2020: carriage paid to, as the order change agreed; the "
                                               "customs of both countries need the terms on the invoice.",
                                        schemeID="INCOTERMS"),
                                "DeliveryLocation": kit.place("XLSLA", "The named place: Selanu airport.")}
        return out
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 4, "Issued after the flight.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The air waybill.")}},
                           [{"item": "air-freight", "qty": air_chargeable(f), "invoice_why": "The chargeable weight "
                                                                             "of the air waybill: the gross weight "
                                                                             "of the frame cartons, rounded up to the "
                                                                             "next half kilogram (D39)."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(3), "The day the frames were flown "
                                                                                 "and handed over at Selanu "
                                                                                 "airport (air/10#F9)."),
                                               "Shipment": {"ID": V(f.numbers["shipment"], "The shipment flown."),
                                                            "Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment flown.")}}}})
    raise SystemExit(f"air scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the cotton flow (Lisavu -> Bayvarra, FOB)
COTTON = kit.Flow("cotton", "2026-02-02", [
    {"item": "cotton-bale", "ordered": 6129, "why": "27 bales of about 227 kg: one container of lint."}])
SEED_KG = 18000
ADVANCE_KG = 4500                  # the season advance: a quarter of the farm's expected 18,000 kg
ADVANCE = Decimal("1017.000")      # 4,500 kg at the agreed 0.226 coral, on the prepayment self-billed invoice


def cotton_results():
    """The classed lot's results (world/items.json): grade, staple length and micronaire, from the chamber's classing
    certificate."""
    it = ITEM["cotton-bale"]
    props = {(p[0] if isinstance(p, list) else p["name"]): p for p in it["properties"]}
    staple = next(q for q in it["quantity_properties"] if q[0] == "Staple length")
    return props["Grade"][1], Decimal(staple[1]), Decimal(props["Micronaire"]["value"]), props, staple


def cotton_required(buyer):
    """The quality the mill's order requires of the lint (O160): a minimum grade and staple and a micronaire range,
    the mill's buying specification (world/items.json buyer_requirements)."""
    req = ITEM["cotton-bale"]["buyer_requirements"][buyer]
    lo, hi = req["micronaire"]
    grade, staple, mic, props, _ = cotton_results()
    grades = ["Good Middling", "Strict Middling", "Middling", "Strict Low Middling", "Low Middling"]
    assert grades.index(grade) <= grades.index(req["grade"]) and staple >= Decimal(req["staple_mm"]) \
        and Decimal(lo) <= mic <= Decimal(hi), "the classed lot must meet the order's quality (O160)"
    src = "the mill's buying specification"
    return [{"Name": V("Grade", "A quality the mill requires: " + req["why"]),
             "Value": V(req["grade"], f"The lowest grade the mill accepts; {src}."),
             "ValueQualifier": V("Minimum: this grade or better", "The value is the lowest acceptable.")},
            {"Name": V("Staple length", "A quality the mill requires: the length of the fibre, which its spinning "
                                        "needs."),
             "ValueQuantity": V(req["staple_mm"], f"The shortest staple the mill accepts, 1-3/32 inch; {src}.",
                                unitCode="MMT"),
             "ValueQualifier": V("Minimum: this length or longer", "The value is the lowest acceptable.")},
            {"Name": V("Micronaire", "A quality the mill requires: the fineness and maturity of the fibre."),
             "TestMethod": V(props["Micronaire"]["test"], "The method the result is to be measured by, the "
                                                          "classer's."),
             "ItemPropertyRange": {"MinimumValue": V(lo, f"The lowest micronaire accepted; {src}."),
                                   "MaximumValue": V(hi, f"The highest micronaire accepted; {src}.")}}]


def cotton_lot(buyer):
    """The ItemInstance of the classed lot on the invoice to the mill (O160): the lot's number and its classing
    results, on which the order's quality is settled."""
    lot = ITEM["cotton-bale"]["classed_lot"]
    cert = ITEM["cotton-bale"]["certificate"]["id"]
    grade, staple, mic, props, st = cotton_results()
    cotton_required(buyer)          # the lot meets the order's quality
    src = f"the lot's classing certificate {cert}"
    return {"LotIdentification": {
        "LotNumberID": V(lot["id"], lot["why"]),
        "AdditionalItemProperty": [
            {"Name": V("Grade", "A classing result of the lot, the grade the order asks for."),
             "Value": V(grade, f"The lot's grade; {src}: at least the "
                               f"{ITEM['cotton-bale']['buyer_requirements'][buyer]['grade']} the order requires.")},
            {"Name": V(st[0], "A classing result of the lot, the staple the order asks for."),
             "ValueQuantity": V(st[1], f"The lot's staple length, 1-1/8 inch; {src}: longer than the order's "
                                       "minimum.", unitCode=st[2])},
            {"Name": V("Micronaire", props["Micronaire"]["why"]),
             "TestMethod": V(props["Micronaire"]["test"], "How the value was measured."),
             "Value": V(str(mic), f"The lot's micronaire; {src}: within the order's range.")}]}}


def cotton(n, doc):
    f = COTTON
    w = kit.gross_weight(f, "ordered")
    farm_rows = [{"item": "seed-cotton", "qty": SEED_KG, "why": "The weighed seed cotton of three trailer loads."}]
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The mill's forecast number."),
                "IssueDate": V(f.date(0), "Sent at the start of the ginning season."),
                "IssueTime": V("09:00:00", "The time is stated, because a revision refers to the forecast by its issue "
                                           "date and time."),
                "ForecastPurposeCode": V("ORDER", "A forecast of what the mill will order, so the ginnery can plan."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The season's shipping period."),
                                   "EndDate": V(f.date(120), "Its end.")},
                "ForecastLine": {"ID": V("1", "The only line."),
                                 "ForecastTypeCode": V("TOTAL", "The total expected purchase in the period."),
                                 "SalesItem": {"Quantity": qty(24000, "KGM", "About four containers of lint."),
                                               "Item": item("cotton-bale")}}}
    if doc["doc"] == "DeliveryNote":
        return {"ID": V(f.number("delivery", doc["from"], "DeliveryNote"), "The farm's delivery note number."),
                "IssueDate": V(f.date(3), "The day the trailers were weighed at the gin."),
                "DespatchLine": {"ID": V("1", "The only line."),
                                 "DeliveredQuantity": qty(SEED_KG, "KGM", "Weighed at the gin's weighbridge."),
                                 "OrderLineReference": {"LineID": V("1", "The line of the season agreement between farm "
                                                                         "and ginnery under which the cotton is "
                                                                         "delivered.")},
                                 "Item": item("seed-cotton")}}
    if doc["doc"] == "SelfBilledInvoice":
        out = kit.self_billed(f, n, doc, 5, "The ginnery bills itself for the delivery, as the self-billing agreement "
                                            "provides.", farm_rows, {})
        out.update({
            "Note": V("Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.",
                      "The statement the self-billing agreement requires on every invoice."),
            "InvoicePeriod": {"StartDate": V(f.date(1), "The week of the deliveries."),
                              "EndDate": V(f.date(3), "The last trailer.")},
            "ContractDocumentReference": {"ID": V("SCG-SEASON-2026", "The season agreement between farm and ginnery, "
                                                                     "which allows the self-billing.")},
            "DeliveryNoteDocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery note.")},
            "AdditionalDocumentReference": {"ID": V("SCG-WB-26-0311", "The weighbridge ticket of the gin, on whose "
                                                                      "weights the invoice rests.")},
            "Delivery": {"ActualDeliveryDate": V(f.date(3), "The trailers were weighed at the gin."),
                         "DeliveryLocation": {"Name": V("Selanu Cotton Ginnery, weighbridge", "Where.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the gin: the farm brings the cotton with its own "
                                             "tractor.", schemeID="INCOTERMS")},
            "PayeeParty": party("38-xl", short=True),
            "OrderReference": {"ID": V("SCG-SEASON-2026/03", "The third call-off under the season agreement.")},
            "Signature": {"ID": V("SCG-SIG-26-0005", "The ginnery's seal on the self-billed invoice."),
                          "SignatoryParty": party("39-xl", short=True)}})
        lmt = out["LegalMonetaryTotal"]
        lines_amt = Decimal(lmt["LineExtensionAmount"].value)
        haul = money(Decimal(SEED_KG) * Decimal("0.010"), "XLC")
        out["AllowanceCharge"] = {"ID": V("1", "The only charge."),
                                  "ChargeIndicator": V("true", "A charge in the farm's favour: it adds to what the gin "
                                                               "pays."),
                                  "AllowanceChargeReasonCode": V("CAB", "The gin pays the farm for carting the cotton: a charge in the farm's favour, so a code of UN/EDIFACT 7161."),
                                  "AllowanceChargeReason": V("Haulage allowance", "The gin pays the farm for bringing "
                                                                                  "the cotton."),
                                  "SequenceNumeric": V("1", "Applied after the lines."),
                                  "PerUnitAmount": amount(Decimal("0.010"), "XLC", "0.010 coral per kilogram."),
                                  "Amount": amount(haul, "XLC", "18,000 kg at 0.010 coral."),
                                  "BaseAmount": amount(lines_amt, "XLC", "The cotton delivered."),
                                  "AccountingCostCode": V("210", "The gin's cost centre for haulage."),
                                  "AccountingCost": V("Seed cotton haulage", "In words."),
                                  "TaxInclusiveAmount": amount(haul, "XLC", "No tax on the island."),
                                  "TaxCategory": kit.tax_category(kit.tax_rule("38-xl", "39-xl", "seed-cotton"))}
        lmt["ChargeTotalAmount"] = amount(haul, "XLC", "The haulage allowance.")
        lmt["ChargeTotalTaxInclusiveAmount"] = amount(haul, "XLC", "The same: no tax on the island.")
        lmt["TaxExclusiveAmount"] = amount(lines_amt + haul, "XLC", "The cotton and the haulage.")
        lmt["TaxInclusiveAmount"] = amount(lines_amt + haul, "XLC", "No tax on the island.")
        lmt["PrepaidAmount"] = amount(ADVANCE, "XLC", "The advance paid at the start of the season.")
        lmt["PayableAmount"] = amount(lines_amt + haul - ADVANCE, "XLC", "What the gin still pays.")
        out["PrepaidPayment"] = {"ID": V("SCG-ADV-26-0012", "The payment of the season advance, billed on the "
                                                            "prepayment self-billed invoice."),
                                 "PaidAmount": amount(ADVANCE, "XLC", "Paid before the harvest, against the first "
                                                                      "deliveries."),
                                 "PaidDate": V(f.date(-20), "Three weeks before the deliveries.")}
        f.numbers["self-billed-4-amount"] = lines_amt + haul - ADVANCE
        lines = out["InvoiceLine"] if isinstance(out["InvoiceLine"], list) else [out["InvoiceLine"]]
        lines[0]["Delivery"] = {"DeliveryNoteLineReference": {
            "LineID": V("1", "The line of the delivery note the invoice line bills."),
            "DocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery note.")}}}
        return out
    if doc["doc"] == "SelfBilledCreditNote":
        return kit.self_billed(f, n, doc, 12, "Issued after classing showed part of the delivery a grade lower.",
                               [{"item": "seed-cotton", "qty": 2500, "unit_price": "0.030",
                                 "unit_price_why": "The price difference between the agreed grade and the lower grade, "
                                                   "per kilogram.", "why": "The part of the delivery classed lower."}],
                               {"BillingReference": {"SelfBilledInvoiceDocumentReference": {
                                   "ID": V(f.numbers["self-billed-4"], "The self-billed invoice this corrects."),
                                   "IssueDate": V(f.numbers["self-billed-4-date"], "Its issue date.")}},
                                "Note": V("Self-billed credit note under the season agreement.", "As required on "
                                                                                                 "every self-billed "
                                                                                                 "document."),
                                "DiscrepancyResponse": {"ReferenceID": V("1", "The line of the self-billed "
                                                                              "invoice."),
                                                        "ResponseCode": V("2", "The classing found a lower "
                                                                                   "grade."),
                                                        "Description": V("2,500 kg classed Strict Low Middling "
                                                                         "instead of Middling.", "In words.")},
                                "ContractDocumentReference": {"ID": V("SCG-SEASON-2026", "The season agreement: it "
                                                                                         "sets the price per "
                                                                                         "grade.")},
                                "DueDate": V(f.date(14), "Set off on the day of payment."),
                                "OrderReference": {"ID": V("SCG-SEASON-2026/03", "The call-off.")},
                                "DeliveryNoteDocumentReference": {"ID": V(f.numbers["delivery"], "The delivery "
                                                                                                 "classed.")},
                                "Delivery": {"ActualDeliveryDate": V(f.date(3), "The delivery classed.")},
                                "DeliveryTerms": {"ID": V("DAP", "As on the self-billed invoice.",
                                                          schemeID="INCOTERMS")},
                                "PayeeParty": party("38-xl", short=True),
                                "PaymentMeans": {"PaymentMeansCode": V("97", "UN/EDIFACT 4461 code 97: clearing "
                                                                             "between partners; set off against "
                                                                             "the payment.",
                                                                       listID="UN/EDIFACT EDED 4461")},
                                "PaymentTerms": {"Note": V("Set off against the payment of the self-billed "
                                                           "invoice.", "How the credit is settled.")},
                                "AdditionalDocumentReference": {"ID": V(f.numbers["goods-certificate"]
                                                                        if "goods-certificate" in f.numbers else
                                                                        "XL-CLS-2026-0042", "The classing "
                                                                                            "certificate.")}},
                               credit=True)
    if doc["doc"] == "RemittanceAdvice" and doc["from"] == "39-xl":
        inv, cn = f.numbers["self-billed-4-amount"], f.numbers["self-billed-5-amount"]
        return {"ID": V(f.number("remittance-farm", doc["from"], "RemittanceAdvice"), "The ginnery's remittance number."),
                "IssueDate": V(f.date(14), "The ginnery pays the farm after classing."),
                "DocumentCurrencyCode": kit.currency_line("XLC", "the island's currency"),
                "TotalPaymentAmount": amount(inv - cn, "XLC", "The invoice minus the credit note."),
                "PaymentMeans": {"PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.",
                                                       listID="UN/EDIFACT EDED 4461"),
                                 "PayerFinancialAccount": kit.account("39-xl", "The ginnery's account."),
                                 "PayeeFinancialAccount": kit.account("38-xl", "The farm's account.")},
                "RemittanceAdviceLine": [
                    {"ID": V("1", "The self-billed invoice."),
                     "DebitLineAmount": amount(inv, "XLC", "The amount still due on the self-billed invoice, "
                                                           "after the season advance."),
                     "BillingReference": {"SelfBilledInvoiceDocumentReference": {
                         "ID": V(f.numbers["self-billed-4"], "The self-billed invoice paid.")}}},
                    {"ID": V("2", "The self-billed credit note."),
                     "CreditLineAmount": amount(cn, "XLC", "The amount credited, deducted from the payment."),
                     "BillingReference": {"SelfBilledCreditNoteDocumentReference": {
                         "ID": V(f.numbers["self-billed-5"], "The self-billed credit note set off.")}}}]}
    if doc["doc"] == "ForecastRevision":
        return {"ID": V(f.number("forecast-revision", doc["from"], "ForecastRevision"), "The revision's number."),
                "IssueDate": V(f.date(20), "Demand for clothing has risen."),
                "SequenceNumberID": V("1", "The first revision of the forecast."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The same period."), "EndDate": V(f.date(120), "Its end.")},
                "ForecastRevisionLine": {"ID": V("1", "The only line."),
                                         "RevisedForecastLineID": V("1", "The forecast line revised."),
                                         "SourceForecastIssueDate": V(f.date(0), "The issue date of the forecast "
                                                                                 "revised."),
                                         "SourceForecastIssueTime": V("09:00:00", "Its issue time."),
                                         "SalesItem": {"Quantity": qty(30000, "KGM", "Raised to five containers."),
                                                       "Item": item("cotton-bale")}}}
    if doc["doc"] == "Order":
        out = kit.order(f, n, doc, 22, "The mill orders the first container of the season.",
                         "Free on board at the port of Selanu: the buyer books and pays the sea freight; the risk "
                         "passes when the bales are on board.", "Port of Selanu",
                         {"FreightForwarderParty": party("10-xb", short=True),
                          "DestinationCountry": {"IdentificationCode": V("XB", "The bales go to Bayvarra.")},
                          "RequestedInvoiceCurrencyCode": V("XLC", "The mill asks to be invoiced in coral, the "
                                                                   "ginnery's currency, and pays the exchange "
                                                                   "itself.")})
        out["OrderLine"][0]["LineItem"]["Item"]["AdditionalItemProperty"] = cotton_required(doc["from"])
        return out
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The mill's instruction "
                                                                                       "number."),
                "IssueDate": V(f.date(23), "Under FOB the buyer instructs the forwarder for the main carriage."),
                "Shipment": {"ID": V(f.number("shipment", "39-xl", "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the bales."),
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment.")}}}
    if doc["doc"] == "GoodsCertificate":
        return {"ID": V(f.number("goods-certificate", doc["from"], "GoodsCertificate"), "The Plant Protection "
                                                                                       "Service's certificate "
                                                                                       "number."),
                "IssueDate": V(f.date(26), "Issued before shipment, at the ginnery's application."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment certified."),
                             "GoodsItem": kit.goods_items(f, "XLC", "The value of the bales, in coral.")}}
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 27, "The island's export: declared before loading.",
                                      "The value of the bales, in coral.")
    if doc["doc"] == "WeightStatement":
        pk = kit.flow_packages(f, "cotton-bale")
        bales = kit.package_weights(pk)
        return {"ID": V(f.number("vgm", doc["from"], "WeightStatement"), "The shipper's weight statement number."),
                "IssueDate": V(f.date(27), "Declared before the container is loaded, as required for every packed "
                                           "container."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment weighed."),
                             "TransportHandlingUnit": {
                                 "TotalPackageQuantity": qty(len(bales), "EA", f"The {len(bales)} bales in the "
                                                             "container, each listed below with its weight."),
                                 "TransportEquipment": {
                                     "ID": V(kit.container_number("TWL", 412311), "The container, with its ISO 6346 "
                                                                                  "check digit.", schemeID="ISO6346"),
                                     "GrossWeightMeasure": qty(w + 3750, "KGM", "The verified gross mass by SOLAS "
                                                               f"method 2: the {len(bales)} bales as the ginnery "
                                                               f"weighed them ({kit.kg(w)} kg) and the container's own "
                                                               "weight."),
                                     "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight, as "
                                                                           "marked on its door.")},
                                 "Package": [
                                     {"ID": V(b, "The bale's number on its tag, which the ginnery gives every bale it "
                                                 "presses; a package's own number, without a scheme."),
                                      "Quantity": qty(kit.kg(net), "KGM", f"The lint in the bale: its gross weight less "
                                                                      f"the standard tare of {kit.kg(pk['tare_kg'])} kg "
                                                                      f"{pk['tare_what']}."),
                                      "PackagingTypeCode": V(pk["type"], f"UN/ECE Recommendation 21 code "
                                                                         f"{pk['type']}: "
                                                                         f"{kit.PACKAGING_NAMES[pk['type']]}."),
                                      "MeasurementDimension": {
                                          "AttributeID": V("GROSSWEIGHT", "The bale's weight with its cover and ties."),
                                          "Measure": V(kit.kg(gross), f"Weighed {pk['weighed']}.", unitCode="KGM")}}
                                     for b, net, gross in bales]}}}
    if doc["doc"] == "BillOfLading":
        return {"ID": V(f.number("bl", doc["from"], "BillOfLading"), "The bill of lading number."),
                "IssueDate": V(f.date(28), "Issued when the bales are on board."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment carried."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the bales."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment.")}}}
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 32, "The mill declares the bales in Bayvarra.",
                                      "The customs value in lume: the value in coral at the world's reference rate "
                                      "(1 lume = 0.4 coral, so 1 coral = 2.5 lume).",
                                      {"ID": V(f.numbers["bl"], "The bill of lading.")})
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return kit.invoice(f, n, doc, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container, booked for the "
                                                                             "mill under FOB."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 28, "Issued when the bales are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The mill's order.")},
                            "AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading: the bales "
                                                                                     "are on board, which is the "
                                                                                     "delivery under FOB.")}},
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(28), "Free on board: delivered when "
                                                                                  "the bales were loaded on the "
                                                                                  "ship (cotton/16#F6)."),
                                               "DeliveryLocation": kit.place("XLSEL", "The port of loading, where "
                                                                                      "FOB delivers.")}})
        ln = out["InvoiceLine"][0] if isinstance(out["InvoiceLine"], list) else out["InvoiceLine"]
        ln["Item"]["ItemInstance"] = cotton_lot(doc["to"])
        return out
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 55, "The mill pays the ginnery: money flows to the island.")
    raise SystemExit(f"cotton scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"sea": sea, "air": air, "cotton": cotton})


def ref(f, key, why):
    return {"ID": V(f.numbers[key], why)}


def period(f, start, end, why_start, why_end):
    return {"StartDate": V(f.date(start), why_start), "EndDate": V(f.date(end), why_end)}


# ---------------------------------------------------------------- the tender flow (Bayvarra, public procurement)
TENDER = kit.Flow("tender", "2026-01-12", [
    {"item": "bench-serra", "ordered": 40, "why": "The first call-off under the contract: forty benches for the "
                                                  "harbour park."}])
FOLDER = "PWD-2026-PARKS"
PWD_COMMITMENT = "PWD-COMMIT-26-0381"      # the department's budget commitment for the office furniture
PRICING_RATE = {"SourceCurrencyCode": V("XUF", "The currency of the contract prices."),
                "TargetCurrencyCode": V("XBL", "The currency of the order and the invoice."),
                "CalculationRate": V("0.01", "The world's reference rate fixed in the contract."),
                "MathematicOperatorCode": V("Multiply", "Ferra times the rate gives lume."),
                "Date": V("2026-01-02", "The rate of the first working day of the year, as the contract says.")}
TENDER_QTY = 240
COLOUR_CHARGE = Decimal("200.00")       # moss green for the 40 benches of the first release, 5 lume a bench


def TO_FERRA(day):
    return {"SourceCurrencyCode": V("XBL", "The document currency."),
            "TargetCurrencyCode": V("XUF", "The currency the manufacturer is paid in."),
            "CalculationRate": V("100", "1 lume = 100 ferra, the reference rate."),
            "MathematicOperatorCode": V("Multiply", "Lume times the rate gives ferra."),
            "Date": V(day, "The rate of the document's date.")}


def withholding_scheme():
    """Bayvarra's withholding on payments by public bodies to non-resident businesses (D17, O47): a tax on the
    supplier's income, which the paying body keeps back and pays to the state."""
    return {"ID": V("OTH", "UN/EDIFACT 5153 code OTH: other taxes, the withholding tax."),
            "Name": V("Withholding tax on payments by public bodies to non-resident businesses", "The tax in words: "
                      "it applies only where a public body pays a business not established in Bayvarra (D17)."),
            "TaxTypeCode": V("INCOME", "A tax on the supplier's income, not on the supply: the public body keeps it "
                                       "back from the payment.")}


def tax_representative():
    """Bayforth Forwarding, the manufacturer's tax representative in Bayvarra, with its registration with the
    Bayvarran tax office for the withholding it accounts for (D17, O47)."""
    rep = party("10-xb", short=True)
    rep["PartyTaxScheme"] = {"RegistrationName": V(build_examples.legal_name("10-xb"), "The representative's "
                                                   "registered name."),
                             "CompanyID": V(PARTY["10-xb"]["identity"]["tax_id"], "The representative's number with "
                                            "Bayvarra's tax office, under which it accounts for the withholding of "
                                            "the non-resident manufacturer it represents."),
                             "TaxScheme": withholding_scheme()}
    return rep


def withholding(f, out):
    """Bayvarra's withholding on services of non-resident businesses to public bodies (world/countries.json): the
    department keeps 10 % of the installation and pays it to the state; the supplier's tax representative."""
    wh = WORLD["countries"]["XB"]["tax"]["withholding"]
    line = out["InvoiceLine"][1]
    base = Decimal(line["LineExtensionAmount"].value)
    tax = money(base * Decimal(wh["percent"]) / 100, "XBL")
    cat = {"ID": V("S", "The withholding applies."), "Percent": V(wh["percent"], wh["on"]),
           "TaxScheme": withholding_scheme()}
    total = {"TaxAmount": amount(tax, "XBL", f"{wh['percent']} % of the installation."),
             "TaxSubtotal": {"TaxableAmount": amount(base, "XBL", "The installation, the only service."),
                             "TaxAmount": amount(tax, "XBL", "Withheld."), "TaxCategory": cat}}
    out["WithholdingTaxTotal"] = total
    line["WithholdingTaxTotal"] = {"TaxAmount": amount(tax, "XBL", "Withheld on this line.")}
    lmt = out["LegalMonetaryTotal"]
    lmt["WithholdingTaxTotalAmount"] = amount(tax, "XBL", wh["note"])
    payable = Decimal(lmt["PayableAmount"].value) - tax
    lmt["PayableAmount"] = amount(payable, "XBL", "What the department pays the manufacturer: the total less the tax "
                                                  "it withholds.")
    out["TaxRepresentativeParty"] = tax_representative()
    out["Note"] = V("Bayforth Forwarding acts as the manufacturer's tax representative in Bayvarra.", "Why it is "
                                                                                                      "named.")
    f.numbers["invoice-amount"] = payable
    return out


def tender(n, doc):
    f = TENDER
    folder = {"ContractFolderID": V(FOLDER, "The authority's file number for this procurement, the same on every "
                                            "document of the procedure.")}
    project = {"ProcurementProject": {
        "Name": V("Park benches for the city parks", "The name of the procurement project."),
        "Description": V(f"{TENDER_QTY} park benches with galvanised metal frames and hardwood slats over three years, ordered in "
                         "call-offs.", "What the authority buys."),
        "RequestedTenderTotal": {"EstimatedOverallContractAmount": amount(120000, "XBL", "The authority's estimate of "
                                                                                         "the contract value, in lume.")}}}
    appeal_why = "The independent review body for appeals and mediation in public procurement."
    if doc["doc"] == "PriorInformationNotice":
        return {"ID": V(f.number("pin", doc["from"], "PriorInformationNotice"), "The notice number."),
                "IssueDate": V(f.date(0), "Published early in the year, before the call for competition."),
                **folder, **project}
    if doc["doc"] == "ContractNotice":
        return {"ID": V(f.number("notice", doc["from"], "ContractNotice"), "The notice number."),
                "IssueDate": V(f.date(30), "The call for competition, a month after the prior information notice."),
                **folder, **project}
    if doc["doc"] == "CallForTenders":
        return {"ID": V(f.number("call", doc["from"], "CallForTenders"), "The number of the procurement documents."),
                "IssueDate": V(f.date(31), "Retrieved by the manufacturer after the notice was published."),
                **folder, **project}
    if doc["doc"] == "BusinessInformation":
        return {"ID": V(f.number("business-info", doc["from"], "BusinessInformation"), "The registry's extract number."),
                "IssueDate": V(f.date(46), "The authority checks the tenderer's registration before evaluation.")}
    if doc["doc"] == "TendererQualification":
        return {"ID": V(f.number("qualification", doc["from"], "TendererQualification"), "The tenderer's number for "
                                                                                       "its declaration."),
                "IssueDate": V(f.date(44), "Submitted with the tender."), **folder}
    if doc["doc"] == "GuaranteeCertificate":
        return {"ID": V(f.number("guarantee", doc["from"], "GuaranteeCertificate"), "The guarantee's number."),
                "IssueDate": V(f.date(43), "Issued before the tender deadline."), **folder,
                "LiabilityAmount": amount(2400, "XBL", "The bid bond: 2 % of the estimated contract value, as the "
                                                       "procurement documents ask.")}
    if doc["doc"] == "Tender":
        unit = kit.unit_price("bench-serra", "XBL")
        return {"ID": V(f.number("tender", doc["from"], "Tender"), "The tenderer's number for its tender."),
                "IssueDate": V(f.date(44), "Submitted before the deadline."), **folder,
                "TenderedProject": {"LegalMonetaryTotal": {
                    "PayableAmount": amount(unit * TENDER_QTY, "XBL", f"{TENDER_QTY} benches at {unit} lume: the bench "
                                                                      "price converted at the reference rate.")}}}
    if doc["doc"] == "ContractAwardNotice":
        return {"ID": V(f.number("award-notice", doc["from"], "ContractAwardNotice"), "The notice number."),
                "IssueDate": V(f.date(60), "Published four days after the award decision, while the standstill period runs."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day the authority decided the award.")}}
    if doc["doc"] == "AwardedNotification":
        return {"ID": V(f.number("awarded", doc["from"], "AwardedNotification"), "The notification number."),
                "IssueDate": V(f.date(56), "The winner is told on the day of the award decision."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day of the award decision.")}}
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 70, "The first call-off under the awarded contract.",
                         "Delivered at place, the authority's depot: the manufacturer delivers, by the carrier it "
                         "chooses; the authority clears the import.", "Public works depot, Lumeport",
                         {"Contract": {"ID": V(FOLDER, "The contract under which the call-off is made.")},
                          "Note": V("Release 1 under the framework contract: 40 of the 240 benches.", "Which call-off "
                                    "this is; Delivery/ReleaseID is an access approval at the delivery place, not "
                                    "a call-off number (tender/26#F5)."),
                          "PricingCurrencyCode": V("XUF", "The contract prices are the manufacturer's, in ferra."),
                          "PricingExchangeRate": PRICING_RATE,
                          "ProjectReference": {"ID": V("PWD-PARKS-26", "The parks renewal programme the benches "
                                                                       "are for.")},
                          "OriginatorDocumentReference": {"ID": V(FOLDER, "The procurement procedure the order "
                                                                          "results from.")}},
                         currency="XBL")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 77, "The day the call-off left the 3PL.", "The gross weight loaded.")
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 77, "Declared when the goods leave for the border.",
                                      "The value of the goods, in ferra.")
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 78, "Under DAP the buyer clears the import: the authority declares "
                                                     "the benches.", "The customs value in lume, at the reference rate.")
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 78, "Issued on delivery.",
                          {"OrderReference": ref(f, "order", "The authority's call-off order."),
                           "ContractDocumentReference": {"ID": V(FOLDER, "The awarded contract.")},
                           "ProjectReference": {"ID": V("PWD-PARKS-26", "The programme the department books it on.")},
                           "OriginatorDocumentReference": {"ID": V(FOLDER, "The procurement procedure.")}},
                          [{"item": "bench-serra", "qty": 40, "invoice_why": "The benches of the first release.",
                            "line_extra": {"OrderLineReference": {"LineID": V("1", "The call-off line.")}}},
                           {"item": "bench-installation", "qty": 40, "invoice_why": "Each bench anchored by the "
                                                                                    "manufacturer's installers, as "
                                                                                    "the contract provides."}],
                          currency="XBL",
                          charges=[{"like": "bench-serra", "amount": COLOUR_CHARGE, "reason": "Special colour", "code": "CAT", "code_why": "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services).",
                                    "why": "The benches in moss green, RAL 6005, as the order change asked.",
                                    "amount_why": "The charge the manufacturer quoted and confirmed: 5 lume a "
                                                  "bench."}])
        withholding(f, out)
        out["PaymentCurrencyCode"] = V("XUF", "The manufacturer is paid in ferra, the contract currency, to its "
                                              "account in Urvania over the trade accord's link.")
        out["PaymentExchangeRate"] = TO_FERRA(f.date(78))
        out["PricingCurrencyCode"] = V("XUF", "The contract prices are in ferra.")
        out["PricingExchangeRate"] = PRICING_RATE
        out["TaxCurrencyCode"] = V("XUF", "The seller reports its value added tax in ferra.")
        out["TaxExchangeRate"] = {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                  "TargetCurrencyCode": V("XUF", "The seller's tax currency."),
                                  "CalculationRate": V("100", "1 lume = 100 ferra, the reference rate."),
                                  "MathematicOperatorCode": V("Multiply", "Lume times the rate gives ferra."),
                                  "Date": V(f.date(78), "The rate of the tax point.")}
        base_xbl = Decimal(out["LegalMonetaryTotal"]["TaxExclusiveAmount"].value)
        out["TaxTotal"] = [out["TaxTotal"], {
            "TaxAmount": amount(0, "XUF", "The same tax in ferra, for the seller's tax return: none on an export."),
            "TaxSubtotal": {"TaxableAmount": amount(base_xbl * 100, "XUF", "The taxable amount in ferra."),
                            "TaxAmount": amount(0, "XUF", "No tax: an export."),
                            "TransactionCurrencyTaxAmount": amount(0, "XBL", "The tax in the invoice currency."),
                            "TaxCategory": out["TaxTotal"]["TaxSubtotal"][0]["TaxCategory"]}}]
        out["Annotation"] = {"SubjectCode": V("CONTRACT", "The annotation is about the contract."),
                             "Subject": V("Releases under the framework contract", "Its subject."),
                             "AnnotationContent": V("First release: 40 benches; 200 remain.", "A remark for the "
                                                                                              "department's "
                                                                                              "accounts.")}
        out["Signature"] = {"ID": V("VI-SIG-26-0078", "The seller's electronic signature on the invoice, which "
                                                      "Bayvarra's public bodies ask for."),
                            "SignatureMethod": V("XAdES-BES", "The kind of signature."),
                            "SignatoryParty": party("5-xu", short=True)}
        return out
    raise SystemExit(f"tender scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the carnet flow (temporary export)
CARNET = kit.Flow("carnet", "2026-05-25", [
    {"item": "bench-serra", "ordered": 2, "why": "Two sample benches for the stand at the trade fair."}])


# The carnet's timeline (D40), in days from its issue on Monday 25 May: out of Urvania and through Bayvarra on
# Monday 1 June, flown to the island on Tuesday 2 June, the fair, flown back on Tuesday 9 June and home through
# Bayvarra on Wednesday 10 June; the island's customs set 30 June as the limit to re-export. The re-exportation
# voucher goes astray, so the island's chamber asks for proof on 24 July, reminds on 24 August and is answered on 28.
CARNET_DAYS = {"export": 7, "import": 8, "reexport": 15, "reimport": 16, "request": 60, "reminder": 91, "proof": 95}
CARNET_LIMIT = "2026-06-30"
CARNET_OFFICES = {      # the customs offices that stamp the counterfoils: one name each, the airports by their code
    "XU": ("Customs Administration of Urvania, Valico Euridice", None, "BORDERPOST"),
    "XB-road": ("Customs and Border Service of Bayvarra, Euridice Crossing", None, "BORDERPOST"),
    "XB-air": ("Customs and Border Service of Bayvarra, Lumeport airport", "XBLMA", "CUSTOMSOFFICE"),
    "XL": ("Island Customs Service, Selanu airport", "XLSLA", "CUSTOMSOFFICE")}
# The counterfoils as the carnet has them (ATA sheets: yellow for Urvania, blue for transit, white for the island):
# id -> (sheet, where it is presented, the day it is stamped, what happens then)
CARNET_SHEETS = {
    "EXP-1": ("exportation counterfoil (yellow sheet)", "XU", "export", "the samples leave Urvania"),
    "TRA-1": ("transit counterfoil (blue sheet), outbound", "XB-road", "export",
              "the samples enter Bayvarra at Euridice Crossing and leave it at Lumeport airport"),
    "IMP-1": ("importation counterfoil (white sheet)", "XL", "import", "the samples arrive on the island"),
    "REEXP-1": ("re-exportation counterfoil (white sheet)", "XL", "reexport", "the samples leave the island"),
    "TRA-2": ("transit counterfoil (blue sheet), homeward", "XB-air", "reexport",
              "the samples enter Bayvarra at Lumeport airport and leave it at Euridice Crossing"),
    "REIMP-1": ("re-importation counterfoil (yellow sheet)", "XU", "reimport", "the samples come home to Urvania")}


def carnet_day(key):
    d = datetime.date.fromisoformat(CARNET_LIMIT if key == "limit" else CARNET.date(CARNET_DAYS[key]))
    return f"{d.day} {d.strftime('%B')}"


def carnet_office(key, why):
    name, code, kind = CARNET_OFFICES[key]
    loc = kit.place(code, why, name) if code else {"Name": V(name, why)}
    loc["LocationTypeCode"] = V(kind, "A customs office at the airport." if kind == "CUSTOMSOFFICE" else
                                "A customs post at the road border crossing.")
    return loc


def customs_record(rid, kind, day, why):
    return {"ID": V(rid, why), "IssueDate": V(CARNET.date(CARNET_DAYS[day]), "The day customs stamped the "
                                                                              "counterfoil."),
            "DocumentType": V(kind, "The kind of customs record, in words.")}


def carnet_counterfoil(f, cid, stamped):
    """A counterfoil of the carnet: as issued, with the office where it is to be presented, the goods and its
    vouchers, and nothing stamped (carnet/01#F1); as stamped, quoted by the chambers afterwards, with the customs
    office's record of the stamp (carnet/03, 04)."""
    sheet, office, day, what = CARNET_SHEETS[cid]
    cf = {"ID": V(cid, f"The {sheet} of the carnet."),
          "GoodsItemPassportID": V(f.numbers["carnet"], "The carnet the counterfoil belongs to (carnet/04#F4).")}
    if not stamped:
        cf["Note"] = V(f"To be stamped by customs when {what}.", "What the counterfoil is for: at issue no "
                                                                   "counterfoil is stamped yet (D40).")
    elif cid == "IMP-1":
        cf["FinalReexportationDate"] = V(CARNET_LIMIT, "The limit the island's customs set on the importation "
                                                       "counterfoil, shorter than the carnet's year: a short fair "
                                                       "admission (D40, carnet/01#F22).")
        cf["Note"] = V(f"Stamped at Selanu airport on {carnet_day('import')}; no discharged re-exportation voucher "
                       "on file.", "The counterfoil the claim rests on.")
    elif cid == "REEXP-1":
        cf["Note"] = V(f"Stamped at Selanu airport on {carnet_day('reexport')}; its voucher did not reach the "
                       "importation office's records.", "What went wrong: the voucher, not the stamp (D40).")
    else:
        cf["Note"] = V(f"Stamped at Valico Euridice on {carnet_day('reimport')}.", "The samples came home.")
    cf["CustomsOfficeLocation"] = carnet_office(office, "The customs office where the counterfoil is presented.")
    cf["GoodsItem"] = {"ID": V("1", "The two sample benches."), "Quantity": qty(2, "EA", "Two.")}
    if stamped and cid == "IMP-1":
        cf["ImportationDocumentReference"] = customs_record("XL-CUS-ATA-26-0049", "Importation registration",
                                                            "import", "The island's customs' registration of the "
                                                                      "importation, noted with the stamp.")
    if stamped and cid == "REEXP-1":
        cf["ImportationDocumentReference"] = customs_record("XL-CUS-ATA-26-0049", "Importation registration",
                                                            "import", "The importation the re-exportation "
                                                                      "discharges.")
        cf["ReexportationDocumentReference"] = customs_record("XL-CUS-ATA-26-0053", "Re-exportation registration",
                                                              "reexport", "The island's customs' registration of "
                                                                          "the re-exportation.")
    if stamped and cid == "REIMP-1":
        cf["ExportationDocumentReference"] = customs_record("XU-CUS-EXP-26-0031", "Exportation registration",
                                                            "export", "The exportation the samples came back "
                                                                      "from, as the re-importation counterfoil "
                                                                      "states it.")
        cf["ReimportationDocumentReference"] = customs_record("XU-CUS-REIMP-26-0044", "Re-importation record",
                                                              "reimport", "Urvania's customs' record of the "
                                                                          "re-importation, the same number as in "
                                                                          "the evidence (carnet/01#F23).")
    if not stamped:
        if cid.startswith("TRA"):
            cf["VoucherDocumentReference"] = [
                {"ID": V(f"V-{cid}-IN", "The transit voucher Bayvarra's customs keep on entry.")},
                {"ID": V(f"V-{cid}-OUT", "The transit voucher they keep on exit.")}]
        else:
            cf["VoucherDocumentReference"] = {"ID": V(f"V-{cid}", "The voucher customs detach and keep.")}
    elif cid == "REEXP-1":
        cf["VoucherDocumentReference"] = {"ID": V("V-REEXP-1", "The voucher that went astray.")}
    return cf


def carnet(n, doc):
    f = CARNET
    out = {"ID": V(f.number("carnet", doc["from"], "GoodsItemPassport"), "The carnet number, given by the chamber."),
           "IssueDate": V(f.date(0), "Issued before the samples leave for the fair."),
           "ValidityPeriod": period(f, 0, 365, "Valid from issue.", "A carnet is valid for one year."),
           "Shipment": {"ID": V(f.number("shipment", doc["to"], "Shipment"), "The samples travelling under the "
                                                                              "carnet."),
                        "GoodsItem": kit.goods_items(f, "XUF", "The value of the samples, for the guarantee.")}}
    out["GoodsItemPassportCounterfoil"] = [carnet_counterfoil(f, cid, False) for cid in CARNET_SHEETS]
    return out


# ---------------------------------------------------------------- the waste flow (Urvania, domestic)
WASTE = kit.Flow("waste", "2026-03-23")
# The waste stream of D42: Valdara's baled polyethylene film to Rinova, about 275 t a year in twelve loads; the first
# load on day 10 (Thursday 2 April), 54 bales, weighed on Rinova's weighbridge with Trasvia's truck T-07.
WASTE_DESCRIPTION = "Used polyethylene stretch film and film offcuts, baled"
WASTE_CODE = "150102"            # Urvania's waste list (XU:Waste), after the European List of Waste (O191)
WASTE_YEAR_T, WASTE_LOADS = 275, 12
WASTE_BALES, WASTE_GROSS = 54, 38200        # the load: bales, and the truck full on the weighbridge, kg
WASTE_TRUCK = kit.fleet("13-xu", "T-07")
WASTE_TARE = sum(WASTE_TRUCK["tare_kg"].values())          # tractor and trailer, empty (O134)
WASTE_NET = WASTE_GROSS - WASTE_TARE
WASTE_LOAD_DAY, WASTE_ACK_DAY = 10, 2
WASTE_STREAM = "XU-ENV-WS-2026-04417"     # the agency's waste-stream number, given on its acknowledgement
LIMIT = WORLD["road_rules_accord"]["max_combination_kg"]
if WASTE_GROSS > LIMIT or WASTE_NET > LIMIT - WASTE_TARE:
    raise SystemExit(f"waste: the load of {WASTE_GROSS} kg exceeds the Accord's {LIMIT} kg for a combination (O134)")


def waste_item(why):
    return {"Description": V(WASTE_DESCRIPTION, why),
            "CommodityClassification": {"ItemClassificationCode": V(
                WASTE_CODE, "The waste by its entry in Urvania's waste list, numbered after the European List of "
                            "Waste: the film comes from the packaging of the parts and materials the factory receives "
                            "and from the wrapping of its own pallets, and no chapter for the factory's activity "
                            "(metal working and coating, chapters 08, 11 and 12) has an entry for packaging, so the "
                            "list's rule sends it to chapter 15: 15 01 02 plastic packaging (O191).",
                listID=codelists.NATIONAL.format("XU", "Waste"))}}


def waste_goods():
    return {"ID": V("1", "The only goods item: one kind of waste."),
            "Description": V(WASTE_DESCRIPTION, "What the waste is, in words."),
            "HazardousRiskIndicator": V("false", "Polyethylene film is not hazardous waste: its entry in the waste "
                                                 "list has no asterisk."),
            "Item": waste_item("The waste, in words."),
            "ContainingPackage": {"PackagingTypeCode": V("BL", "UN/ECE Recommendation 21 code BL: bale, compressed. "
                                                               "Loose film would fill the trailer long before its "
                                                               "payload; pressed into bales of about 1.2 × 0.8 × "
                                                               "1.0 m and 425 kg, two layers high, a load reaches "
                                                               "the weight limit first (D42)."),
                                  "PackingMaterial": V("Steel baling wire", "What holds a bale together.")}}


def waste_load_consignment(f, why):
    return {"ID": V(f.number("waste-load-1-consignment", "5-xu", "Consignment"), why),
            "TotalPackagesQuantity": V(str(WASTE_BALES), f"{WASTE_BALES} bales on the truck, in two layers.")}


def waste_places(f, actual):
    """Where the waste is loaded and where it is delivered: the waste leg (world/documents.json)."""
    leg = kit.flow_leg(f, "13-xu")
    if not actual:
        return {"DeliveryLocation": kit.leg_location(leg, "to", "The recovery facility's plant, where the waste "
                                                                "of the stream is delivered."),
                "EstimatedDeliveryPeriod": {"StartDate": V("2026-04-01", "The stream's year starts in April."),
                                            "EndDate": V("2027-03-31", "And ends after twelve months."),
                                            "Description": V(f"About one load a month, {WASTE_LOADS} in the year.",
                                                             "How the deliveries are spread.")},
                "Despatch": {"DespatchLocation": kit.leg_location(leg, "from", "The producer's works, where the "
                                                                               "bales are loaded.")}}
    return {"ActualDeliveryDate": V(f.date(WASTE_LOAD_DAY), "The load arrived at the recovery plant."),
            "ActualDeliveryTime": V("10:05:00", "Trasvia's truck at the weighbridge."),
            "DeliveryLocation": kit.leg_location(leg, "to", "Where the waste was delivered."),
            "Despatch": {"ActualDespatchDate": V(f.date(WASTE_LOAD_DAY), "Loaded at the factory the same morning."),
                         "ActualDespatchTime": V("09:35:00", "The truck left the factory; the two sites are a few "
                                                             "kilometres apart in Ferrano."),
                         "DespatchLocation": kit.leg_location(leg, "from", "Where the bales were loaded.")}}


def waste_stage(why):
    return {"ID": V("1", "The one road leg, across Ferrano."),
            "TransportModeCode": V("3", "UN/ECE Recommendation 19 code 3: road transport.",
                                   listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
            "TransportMeans": kit.means("13-xu", "T-07"),
            "DriverPerson": kit.person(WASTE_TRUCK["driver"]["first"], WASTE_TRUCK["driver"]["family"], why,
                                       pid=WASTE_TRUCK["driver"]["id"])}


def waste_stream_ref(f, why):
    return {"ID": V(WASTE_STREAM, "The waste-stream number the environment agency gave the notified stream."),
            "IssueDate": V(f.date(WASTE_ACK_DAY), "The day of the agency's acknowledgement."),
            "DocumentType": V("Acknowledgement of the waste-stream notification", why),
            "IssuerParty": party("46-xu", short=True)}


def waste(n, doc):
    f = WASTE
    if doc["doc"] == "WasteNotification":
        return {"ID": V(f.number("notification", doc["from"], "WasteNotification"), "The notification number."),
                "IssueDate": V(f.date(0), "Notified before the year's movements start."),
                "Shipment": {"ID": V(f.number("waste-stream", "5-xu", "Shipment"), "The producer's number for the "
                                     "notified stream as a whole: each load gets a shipment number of its own."),
                             "NetWeightMeasure": qty(WASTE_YEAR_T, "TNE", f"The total planned for the year: about "
                                                     f"{WASTE_LOADS} loads of about 23 tonnes."),
                             "Consignment": {"ID": V(f.number("waste-consignment", "5-xu", "Consignment"),
                                                     "The consignment of the notified stream, which names its "
                                                     "carrier.")},
                             "GoodsItem": waste_goods(),
                             "Delivery": waste_places(f, False)}}
    if doc["doc"] == "WasteMovement":
        return {"ID": V(f.number("movement", doc["from"], "WasteMovement"), "The movement report number."),
                "IssueDate": V(f.date(WASTE_LOAD_DAY), "Reported the day the load was received."),
                "IssueTime": V("11:45:00", "Once the truck had been weighed empty."),
                "Shipment": {"ID": V(f.number("waste-load-1", "5-xu", "Shipment"), "This load's own shipment "
                                     "number, beside the stream's."),
                             "NetWeightMeasure": qty(WASTE_NET, "KGM", "The waste received, net, from the "
                                                     "weighbridge ticket."),
                             "Consignment": waste_load_consignment(f, "This load's consignment, carried by the waste "
                                                                      "carrier."),
                             "GoodsItem": waste_goods(),
                             "ShipmentStage": waste_stage("The driver."),
                             "Delivery": waste_places(f, True)}}
    if doc["doc"] == "WeightStatement":
        t = WASTE_TRUCK["tare_kg"]
        return {"ID": V(f.number("weighbridge", doc["from"], "WeightStatement"), "The weighbridge ticket number."),
                "IssueDate": V(f.date(WASTE_LOAD_DAY), "Printed after the second weighing."),
                "IssueTime": V("10:50:00", "When the empty truck left the weighbridge."),
                "Shipment": {"ID": V(f.numbers["waste-load-1"], "The load weighed."),
                             "NetWeightMeasure": qty(WASTE_NET, "KGM", f"The waste: the truck full less the truck "
                                                     f"empty, {WASTE_GROSS:,} kg − {WASTE_TARE:,} kg."),
                             "Consignment": waste_load_consignment(f, "The consignment weighed."),
                             "GoodsItem": waste_goods(),
                             "ShipmentStage": {**waste_stage("The driver, who took the ticket."),
                                               "TransportMeans": {
                                                   **kit.means("13-xu", "T-07"),
                                                   "MeasurementDimension": [
                                                       {"AttributeID": V("GROSSWEIGHT", "The first weighing: the "
                                                                         "truck with its load, on arrival."),
                                                        "Measure": V(str(WASTE_GROSS), "Within the Accord's "
                                                                     f"{LIMIT:,} kg for a combination.",
                                                                     unitCode="KGM"),
                                                        "Description": V("Loaded, at 10:07", "When it was weighed.")},
                                                       {"AttributeID": V("TAREWEIGHT", "The second weighing: the "
                                                                         "same truck after unloading."),
                                                        "Measure": V(str(WASTE_TARE), f"The tractor about "
                                                                     f"{t['tractor']:,} kg and the trailer about "
                                                                     f"{t['trailer']:,} kg (world/parties.json).",
                                                                     unitCode="KGM"),
                                                        "Description": V("Empty, at 10:46", "When it was weighed.")}]}}}}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 14, "Issued on the next working day after the load (D27).",
                           {"AdditionalDocumentReference": [
                               {**ref(f, "movement", "The movement report of the load billed."),
                                "IssueDate": V(f.date(WASTE_LOAD_DAY), "Its date.")},
                               {"ID": V(f.number("weighbridge", "7-xu", "WeightStatement"), "The weighbridge ticket "
                                        "whose net weight is billed."),
                                "IssueDate": V(f.date(WASTE_LOAD_DAY), "Its date.")}]},
                           [{"item": "waste-recovery", "qty": str(Decimal(WASTE_NET) / 1000),
                             "invoice_why": "The net tonnes received, from the weighbridge ticket."}],
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(WASTE_LOAD_DAY), "The day of the "
                                                                       "service: the load collected and received."),
                                               "DeliveryLocation": kit.leg_location(kit.flow_leg(f, "13-xu"), "to",
                                                                                    "Where the waste was received "
                                                                                    "for recovery.")}})
    raise SystemExit(f"waste scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the utilities flow (one utility per country)
UTILITIES = kit.Flow("utilities", "2026-04-01")
MARCH = {"InvoicePeriod": {"StartDate": V("2026-03-01", "The month billed: March."),
                           "EndDate": V("2026-03-31", "Its last day."),
                           "DescriptionCode": V("MONTH", "A monthly bill."),
                           "Description": V("March 2026", "The period in words.")}}


def levy(m3, who):
    return {"item": "sewage-levy", "qty": m3, "invoice_why": f"The {who}'s water use, on which the city charges its "
                                                            "levy.",
            "line_extra": {**MARCH, "CollectedForParty": party("2-xb", short=True),
                           "Note": V("Collected for the city of Lumeport and paid on to it.", "Why the water company "
                                                                                              "bills it.")}}


FEBRUARY = {"InvoicePeriod": {"StartDate": V("2026-02-01", "The month corrected: February."),
                              "EndDate": V("2026-02-28", "Its last day."),
                              "DescriptionCode": V("MONTH", "A month's consumption."),
                              "Description": V("February 2026", "The period in words.")}}
WAREHOUSE_LINE = {"AccountingCostCode": V("7100", "The manufacturer books the warehouse's power on its transport cost "
                                                  "centre."),
                  "AccountingCost": V("Warehouse, Castrano Logistics", "In words."),
                  "Delivery": {"DeliveryLocation": {"Description": V("Castrano Logistics warehouse, Conciaro",
                                                                     "Where the power was used.")}}}
BILLS = {"33-xu": [{"item": "electricity", "qty": 412800, "invoice_why": "The factory's metered consumption in March.",
                    "line_extra": MARCH},
                   {"item": "electricity", "qty": 19350, "invoice_why": "The warehouse's metered consumption in March, "
                                                                        "from February's corrected reading; the "
                                                                        "manufacturer pays for its building.",
                    "line_extra": {**MARCH, **WAREHOUSE_LINE}},
                   {"item": "gas", "qty": 61200, "invoice_why": "The gas of the coating ovens in March, as the grid "
                                                               "operator metered and converted it.",
                    "line_extra": {**MARCH, "Note": V("1,350 m³ at 4 bar, converted to 61,200 kWh by the grid "
                                                      "operator's metering report.", "How the quantity is "
                                                                                     "found.")}},
                   {"item": "electricity", "qty": -750, "correction_of": 1,
                    "invoice_why": "February's estimate corrected: line 2 of February's bill charged the warehouse "
                                   "750 kWh it did not use, which are credited (O159).",
                    "line_extra": {**FEBRUARY, **WAREHOUSE_LINE}}],
         "34-xb:26-xb": [{"item": "water", "qty": 86, "invoice_why": "The shop's metered consumption in March.",
                          "line_extra": MARCH}, levy(86, "shop")],
         "34-xb:c-xb": [{"item": "water", "qty": 14, "invoice_why": "The household's metered consumption in March.",
                         "line_extra": MARCH}, levy(14, "household")],
         "35-xl": [{"item": "telecom-line", "qty": 6, "invoice_why": "Six business lines for the month."},
                   {"item": "telecom-data", "qty": 35, "invoice_why": "Mobile data beyond the subscriptions."}]}
KIND = {"33-xu": "Electricity", "34-xb": "Water", "35-xl": "Telephone"}
UTILITY = {"Electricity": "ELEC", "Water": "WATER", "Telephone": "TEL", "Gas": "GAS"}   # UtilityType list
METERS = {"33-xu": ["FE-C-0047120", ("FG-E-20388", "Factory, main connection"),
                    ("FG-E-20523", "Warehouse of Castrano Logistics"), ("FG-G-20417", "Factory, gas of the coating "
                                                                                       "line"),
                    ("FG-E-20523", "Warehouse of Castrano Logistics")],
          "34-xb:26-xb": ["CSW-C-260118", ("CSW-W-55102", "Shop, Lumeport"), None],
          "34-xb:c-xb": ["CSW-C-311790", ("CSW-W-71844", "Gull Lane 57"), None],
          "35-xl": ["ST-C-1077", ("ST-L-BUS6", "Six business lines"), ("ST-D-0042", "Mobile data pool")]}


EXCISE = next(x for x in WORLD["countries"]["XU"]["tax"]["schemes"] if x["id"] == "EXC")


def excise_tiers():
    """Urvania's energy tax on the month's electricity of one customer: (kWh, rate per kWh, tier in words) per tier
    (world/countries.json). Gas carries no energy tax."""
    kwh = sum(Decimal(str(r["qty"])) for r in BILLS["33-xu"] if r["item"] == "electricity" and
              "correction_of" not in r)
    t1 = min(kwh, Decimal(EXCISE["tiers"][0]["up_to"]))
    return [(t1, Decimal(EXCISE["tiers"][0]["per_unit"]),
             f"The first {t1:,} kWh of the month's {kwh:,} kWh of electricity"),
            (kwh - t1, Decimal(EXCISE["tiers"][1]["per_unit"]),
             f"The other {kwh - t1:,} kWh of electricity above {t1:,} kWh: the industrial rate")]


def excise_shares():
    """Each electricity line's share of the tiers (utilities/01#F1, 03#F5): the tiers apply to the customer's
    month as a whole, and the lower tier is counted on the lines in the bill's order, so the main connection takes
    the first 50,000 kWh. Returns per line of BILLS["33-xu"] the list of (kWh, rate) it carries."""
    left = [[q, r] for q, r, _ in excise_tiers()]
    shares = []
    for row in BILLS["33-xu"]:
        if "correction_of" in row:      # a correction of an earlier month: taxed at the rate that month charged
            shares.append([(Decimal(str(row["qty"])), correction_rate(row))])
            continue
        need, mine = Decimal(str(row["qty"])) if row["item"] == "electricity" else Decimal(0), []
        for t in left:
            take = min(need, t[0])
            if take:
                mine.append((take, t[1]))
                t[0] -= take
                need -= take
        shares.append(mine)
    return shares


def correction_rate(row):
    """The energy tax rate of the kWh an estimate correction credits (O159): the rate the corrected month charged on
    them. February's bill counted the lower tier on the main connection, which alone took more than the tier, so
    the warehouse's kWh were all taxed at the upper rate."""
    main = POINTS[("33-xu", "5-xu")]
    assert Decimal(main["history"][-1][2]) >= Decimal(EXCISE["tiers"][0]["up_to"]) and row["correction_of"] != 0
    return Decimal(EXCISE["tiers"][1]["per_unit"])


def correction_tier(q, r):
    return (f"February's estimate correction: {-q:,} kWh of the warehouse credited at the rate February's bill "
            "charged on them, the upper tier")


def excise_subtotal(q, r, what):
    """One tier of the energy tax: a tax per kWh, so no taxable amount (utilities/02#F3) and the rate as it is, not
    rounded to whole ferra (utilities/02#F1)."""
    return {"TaxAmount": amount(q * r, "XUF", f"{q} kWh at {r} ferra."),
            "CalculationSequenceNumeric": V("1", "The energy tax is calculated first."),
            "BaseUnitMeasure": V("1", "The tax is per kilowatt hour.", unitCode="KWH"),
            "PerUnitAmount": price(r, "XUF", "The tax per kWh in this tier."),
            "TierRange": V(what, "The tier of the monthly consumption, and the electricity it applies to."),
            "TaxCategory": {"ID": V("S", "The energy tax applies."),
                            "Name": V("Energy tax", "The tax in words."),
                            "BaseUnitMeasure": V("1", "Per kilowatt hour.", unitCode="KWH"),
                            "PerUnitAmount": price(r, "XUF", "The rate per kWh."),
                            "TierRange": V(what, "The tier."),
                            "TaxScheme": {"ID": V("EXC", "UN/EDIFACT 5153 code EXC: excise duty, the energy "
                                                         "tax.")}},
            "TaxDueCountry": {"IdentificationCode": V("XU", "Due in Urvania.")}}


def energy_tax(f, out, key):
    """Urvania's energy tax on the electricity bill: per kWh in two tiers, and value added tax on the price plus the
    energy tax (world/countries.json)."""
    vat = WORLD["countries"]["XU"]["tax"]["schemes"][0]
    lines = Decimal(out["LegalMonetaryTotal"]["LineExtensionAmount"].value)
    tiers = excise_tiers()
    excise = sum(money(q * r, "XUF") for q, r, _ in tiers)
    subs = [excise_subtotal(q, r, what) for q, r, what in tiers]
    for row, sh in zip(BILLS["33-xu"], excise_shares()):
        if "correction_of" in row:      # an estimate correction credits its kWh at the rate they were charged
            subs += [excise_subtotal(q, r, correction_tier(q, r)) for q, r in sh]
            excise += sum(money(q * r, "XUF") for q, r in sh)
    assert excise == Decimal(BILL_EXCISE)
    assert excise == sum(money(q * r, "XUF") for sh in excise_shares() for q, r in sh), "the lines' shares"
    vat_base = lines + excise
    vat_amt = money(vat_base * Decimal(vat["rates"]["standard"]) / 100, "XUF")
    subs.append({"TaxableAmount": amount(vat_base, "XUF", "The price plus the energy tax: value added tax is charged "
                                                         "on both."),
                 "TaxAmount": amount(vat_amt, "XUF", f"{vat['rates']['standard']} % of that base."),
                 "TaxInclusiveAmount": amount(vat_base + vat_amt, "XUF", "The base with the tax."),
                 "CalculationSequenceNumeric": V("2", "Calculated after the energy tax."),
                 "Percent": V(str(vat["rates"]["standard"]), "The standard rate."),
                 "TaxCategory": out["TaxTotal"]["TaxSubtotal"][0]["TaxCategory"]})
    out["TaxTotal"] = {"TaxAmount": amount(excise + vat_amt, "XUF", "Energy tax and value added tax together."),
                       "TaxEvidenceIndicator": V("true", "This tax total is the evidence for the customer's "
                                                         "deduction of value added tax."),
                       "TaxIncludedIndicator": V("false", "The line prices do not include the taxes."),
                       "TaxSubtotal": subs}
    lmt = out["LegalMonetaryTotal"]
    lmt["TaxExclusiveAmount"] = amount(lines, "XUF", "The line amounts, without any tax.")
    lmt["TaxInclusiveAmount"] = amount(lines + excise + vat_amt, "XUF", "With the energy tax and the value added tax.")
    lmt["PayableAmount"] = amount(lines + excise + vat_amt, "XUF", "What the manufacturer pays.")
    f.numbers[f"invoice-{key}-amount"] = lines + excise + vat_amt
    out["PaymentTerms"]["SettlementDiscountAmount"] = amount((lines + excise + vat_amt) * Decimal("0.02"), "XUF",
                                                             "The 2 % discount on the amount payable, if paid in "
                                                             "time.")
    return out


def reading_method(detail, why):
    """The text of a meter reading method: the method's name from its list, with the case's detail where there is
    one (POINTS keeps the detail, or the method's name where nothing specific applies)."""
    return Detail(detail, "from the utility's record of the reading.") if detail[0].islower() else V(detail, why)


GRID_NUMBERS = (", numbered by the grid operator, Ferrano Grid, which owns and reads the meters; the retail company "
                "uses its numbers, its own reference being the contract (O161).")
BILL_EXCISE = "288840"     # the energy tax of the electricity bill (see energy_tax), shown on the statement too
POINTS = {  # the consumption points behind the bills: meters, readings, history (the utilities' own records)
    ("33-xu", "5-xu"): {"line": 0, "id": "FG-CP-4120-E1", "desc": "Factory, main connection at 10 kV",
                        "type": ("Industrial", "IND"), "meter": ("FG-E-20388", "Main meter, factory", "40",
                                                                 "Transformer ratio"),
                        "prev": ("2026-02-28", 52960, "Remote reading", "REMOTE"),
                        "last": ("2026-03-31", 63280, "Remote reading", "REMOTE"),
                        "history": [("2026-01-01", "2026-01-31", 398400), ("2026-02-01", "2026-02-28", 405100)]},
    ("33-xu", "8-xu"): {"line": 1, "id": "FG-CP-4160-E1", "desc": "Warehouse of Castrano Logistics",
                        "type": ("Commercial", "COM"), "meter": ("FG-E-20523", "Warehouse meter", "1", "Direct"),
                        "prev": ("2026-02-28", 116500, "derived from the warehouse's load profile between the "
                                                       "readings of 31 January and 31 March, in place of "
                                                       "February's estimate of 117,250 kWh", "PROFILE"),
                        "last": ("2026-03-31", 135850, "Read by the meter reader", "MANUAL"),
                        "history": [("2026-01-01", "2026-01-31", 17900), ("2026-02-01", "2026-02-28", 16450)],
                        # February's reading was estimated (no access to the meter) at 117,250 and billed 17,200
                        # kWh; March's actual reading corrects it (O159, D31 point 7)
                        "correction": {"estimate": 117250, "billed": 17200, "row": 3}},
    ("34-xb", "26-xb"): {"line": 0, "id": "CSW-CP-38510-411", "desc": "Shop, Lumeport", "type": ("Commercial", "COM"),
                         "meter": ("CSW-W-55102", "Water meter, shop", "1", "Direct"),
                         "prev": ("2026-02-28", 4212, "Remote reading", "REMOTE"),
                         "last": ("2026-03-31", 4298, "Remote reading", "REMOTE"),
                         "history": [("2026-01-01", "2026-01-31", 81), ("2026-02-01", "2026-02-28", 79)]},
    ("34-xb", "c-xb"): {"line": 0, "id": "CSW-CP-38516-57", "desc": "Gull Lane 57, Lumeport",
                        "type": ("Household", "HH"), "meter": ("CSW-W-71844", "Water meter, flat", "1", "Direct"),
                        "prev": ("2026-02-28", 1830, "the household sent the reading", "CUSTOMER"),
                        "last": ("2026-03-31", 1844, "the household sent the reading", "CUSTOMER"),
                        "history": [("2026-01-01", "2026-01-31", 15), ("2026-02-01", "2026-02-28", 13)],
                        "household": {"occupants": "2", "residence": ("Apartment", "APT"),
                                      "heating": ("District heating", "DH")}},
}


def consumption_line(f, sup, key, k, d, why):
    it = ITEM[d["item"]]
    cur = it["price"]["currency"]
    q = Decimal(str(d["qty"]))
    amt = money(q * Decimal(str(it["price"]["amount"])), cur)
    rule = kit.tax_rule(sup, bill_customer(key), d["item"])
    tax = money(amt * Decimal(str(rule[1])) / 100, cur)
    return {"ID": V(str(k + 1), "The line of the consumption."),
            "ParentDocumentLineReferenceID": V(str(k + 1), "The line of the invoice this line explains."),
            "InvoicedQuantity": qty(q, it["unit"], why),
            "LineExtensionAmount": amount(amt, cur, "Quantity times the tariff."),
            "TaxInclusiveLineExtensionAmount": amount(amt + tax, cur, "With the tax of the line."),
            "Period": ({"StartDate": V("2026-02-01", "February, the month the line corrects."),
                        "EndDate": V("2026-02-28", "Its last day.")} if "correction_of" in d else
                       {"StartDate": V("2026-03-01", "March."), "EndDate": V("2026-03-31", "Its last day.")}),
            "TaxTotal": {"TaxAmount": amount(tax, cur, f"{rule[1]} % of the line.")},
            "UtilityItem": {"ID": V(it["sellers_id"], "The utility's tariff item."),
                            "SubscriberID": V(METERS[key][0], "The customer's contract."),
                            "SubscriberType": V(KIND[sup], "The kind of supply."),
                            "SubscriberTypeCode": V(UTILITY[KIND[sup]], "The supply the item is for, as a code."),
                            "Contract": {"ID": V(METERS[key][0], "The supply contract the tariff belongs to.")},
                            "Description": build_examples.item_texts(it, it["description"], "The tariff in words",
                                                                    "world/items.json"),
                            "ConsumptionType": V("Metered" if it["kind"] == "goods" or d["item"] != "telecom-line"
                                                 else "Subscription", "How the quantity is measured."),
                            "ConsumptionTypeCode": V("MET" if d["item"] != "telecom-line" else "SUB", "As a code."),
                            "CurrentChargeType": V("Monthly", "Charged every month."),
                            "CurrentChargeTypeCode": V("M", "As a code."),
                            "TaxCategory": kit.tax_category(rule)},
            "Price": {"PriceAmount": price(it["price"]["amount"], cur, "The tariff (world/items.json)."),
                      "BaseQuantity": qty(1, it["unit"], "Per unit.")},
            **({"UnstructuredPrice": {"PriceAmount": price(it["price"]["amount"], cur, "The subscription price as "
                                                           "the tariff sheet states it."),
                                      "TaxInclusivePriceAmount": price(it["price"]["amount"], cur, "No tax on the "
                                                                                                   "island."),
                                      "TimeAmount": V("per month", "The period the price is for.")}}
               if d["item"] == "telecom-line" else
               {"Delivery": {"DeliveryLocation": {"Description": V("The consumption point of the statement.",
                                                                   "Where it was delivered.")}}})}, amt, tax


def bill_customer(key):
    return key.split(":")[1] if ":" in key else {"33-xu": "5-xu", "35-xl": "1-xl"}[key]


def utility_statement(f, n, doc, key, invoice_no):
    sup, subscriber = doc["from"], doc["to"]
    customer = bill_customer(key)
    cur = kit.currency_of(sup)
    rows = BILLS[key]
    out = {"Note": V("This statement explains the consumption behind your bill.", "What the statement is."),
           **kit.cost_centre(customer, "The customer's cost centre, as on the bill.", iid=rows[0]["item"]),
           "AdditionalDocumentReference": {"ID": V(f"{kit.initials(sup)}-TARIFF-2026", "The utility's tariff sheet "
                                                                                   "for 2026."),
                                           "DocumentTypeCode": V("TARIFF", "What the document is."),
                                           "DocumentDescription": V("Prices per unit and the terms of supply.",
                                                                    "What it holds.")},
           "CustomerParty": {"Party": party(customer, short=True)}}
    if (sup, subscriber) in POINTS:
        pt = POINTS[(sup, subscriber)]
        d = rows[pt["line"]]
        line, amt, tax = consumption_line(f, sup, key, pt["line"], d, "The consumption of this point.")
        corr = pt.get("correction")
        if corr:        # February's estimate corrected: a line of its own on the bill and here (O159, D31 point 7)
            cd = rows[corr["row"]]
            cline, camt, ctax = consumption_line(f, sup, key, corr["row"], cd, "The kWh February's estimate "
                                                                               "charged too much, credited.")
        unit = ITEM[d["item"]]["unit"]
        consumed = Decimal(str(d["qty"]))
        constant = Decimal(pt["meter"][2])
        reading = {"ID": V(f"{pt['meter'][0]}-2603", "The reading of March."),
                   "MeterReadingType": V("Monthly reading", "The kind of reading."),
                   "MeterReadingTypeCode": V("M", "As a code."),
                   "PreviousMeterReadingDate": V(pt["prev"][0], "The previous reading."),
                   "PreviousMeterQuantity": qty(pt["prev"][1], unit, "The register then."),
                   "LatestMeterReadingDate": V(pt["last"][0], "This reading."),
                   "LatestMeterQuantity": qty(pt["last"][1], unit, "The register now."),
                   "PreviousMeterReadingMethod": reading_method(pt["prev"][2], "How the previous reading was taken."),
                   "PreviousMeterReadingMethodCode": V(pt["prev"][3], "As a code."),
                   "LatestMeterReadingMethod": reading_method(pt["last"][2], "How this reading was taken."),
                   "LatestMeterReadingMethodCode": V(pt["last"][3], "As a code."),
                   "DeliveredQuantity": qty(consumed, unit, f"The difference of the readings"
                                            + (f", times the meter constant of {constant}." if constant != 1 else
                                               "."))}
        if corr:
            billed, real = corr["billed"], pt["history"][-1][2]
            assert corr["estimate"] - pt["prev"][1] == billed - real == -Decimal(str(cd["qty"])), "the correction"
            reading["MeterReadingComments"] = V(f"The previous reading replaces February's estimate of "
                                                f"{corr['estimate']:,} kWh: February used {real:,} kWh, not the "
                                                f"{billed:,} kWh billed, and the {billed - real:,} kWh are "
                                                "credited.", "Why the previous reading is not the one on "
                                                             "February's statement.")
        assert (pt["last"][1] - pt["prev"][1]) * constant == consumed, (key, subscriber)
        report = {"ID": V(f"{pt['id']}-2603", "The consumption report of the point for March."),
                  "ConsumptionType": V("Monthly consumption", "What is reported."),
                  "ConsumptionTypeCode": V("MON", "As a code."),
                  "Description": V(f"March consumption of {pt['desc']}.", "In words."),
                  "TotalConsumedQuantity": qty(consumed, unit, "Used in March."),
                  "BasicConsumedQuantity": qty(consumed, unit, "All at the basic tariff: no reduced-rate hours."),
                  "Period": {"StartDate": V("2026-03-01", "March."), "EndDate": V("2026-03-31", "Its last day.")},
                  "ConsumptionReportReference": {
                      "ConsumptionReportID": V(f"{pt['id']}-2602", "The report of February."),
                      "ConsumptionType": V("Monthly consumption", "Of the same kind."),
                      "ConsumptionTypeCode": V("MON", "As a code."),
                      "TotalConsumedQuantity": qty(corr["billed"] if corr else pt["history"][-1][2], unit,
                                                   "What February's report said" + (", from the estimated reading."
                                                                                   if corr else ".")),
                      "Period": {"StartDate": V(pt["history"][-1][0], "February."),
                                 "EndDate": V(pt["history"][-1][1], "Its last day.")}},
                  "ConsumptionHistory": [{"MeterNumber": V(pt["meter"][0], "The meter."),
                                          "Quantity": qty(q_, unit, "The month's consumption."),
                                          "Amount": amount(Decimal(q_) * Decimal(str(ITEM[d["item"]]["price"]
                                                                                    ["amount"])), cur,
                                                           "What it cost at the tariff."),
                                          "ConsumptionLevelCode": V("NORMAL", "Within the usual range."),
                                          "ConsumptionLevel": V("Normal", "In words."),
                                          "Description": V(f"Earlier month, corrected from the estimate of "
                                                           f"{corr['billed']:,} kWh." if corr and b == "2026-02-28"
                                                           else "Earlier month.", "For comparison."),
                                          "Period": {"StartDate": V(a, "The month."), "EndDate": V(b, "Its end.")}}
                                         for a, b, q_ in pt["history"]]}
        if pt.get("household"):
            h = pt["household"]
            report.update({"ResidentOccupantsNumeric": V(h["occupants"], "People living in the flat."),
                           "ResidenceType": V(h["residence"][0], "The kind of home."),
                           "ResidenceTypeCode": V(h["residence"][1], "As a code."),
                           "HeatingType": V(h["heating"][0], "How the home is heated: not with this water."),
                           "HeatingTypeCode": V(h["heating"][1], "As a code."),
                           "ConsumersEnergyLevelCode": V("LOW", "Below the average for two occupants."),
                           "ConsumersEnergyLevel": V("Low consumer", "In words."),
                           "GuidanceDocumentReference": {"ID": V("CSW-SAVE-WATER", "The company's leaflet on saving "
                                                                                   "water.")},
                           "DocumentReference": {"ID": V("CSW-QUALITY-2026-Q1", "The quarterly water quality "
                                                                                "report.")}})
        supply = {"ConsumptionReport": report,
                  "ConsumptionAverage": {"AverageAmount": amount(amt, cur, "What this month cost."),
                                         "Description": V("The average over the last three months is "
                                                          f"{round((sum(q_ for *_, q_ in pt['history']) + consumed) / 3)}"
                                                          f" {'kWh' if unit == 'KWH' else 'm³'}.", "For comparison.")}}
        taxes = {"TaxAmount": amount(tax, cur, "The tax of this point's consumption.")}
        share = excise_shares()[pt["line"]] if sup == "33-xu" else []
        lines_ = [(line, amt, share)]
        if corr:
            lines_.append((cline, camt, excise_shares()[corr["row"]]))
            amt += camt
            tax += ctax
            share = share + lines_[1][2]
        if share:
            # this point's share of the bill's energy tax, and the value added tax on the price plus it, so that
            # the statements of one bill add up to it (utilities/01#F1, F2, 03#F5)
            exc = sum(money(q * r, cur) for q, r in share)
            rule = kit.tax_rule(sup, customer, d["item"])
            tax = money((amt + exc) * Decimal(str(rule[1])) / 100, cur)
            split = " and ".join(f"{q:,} kWh at {r}" for q, r in share)
            supply["EnergyTaxReport"] = {"TaxEnergyAmount": amount(exc, cur, f"This point's share of the bill's "
                                                                             f"energy tax: {split} ferra; the tiers "
                                                                             "apply to the customer's month as a "
                                                                             "whole, the lower tier counted on the "
                                                                             "main connection"
                                                                             + ("; the credit of February's "
                                                                                "estimate at the rate February "
                                                                                "charged." if corr else ".")),
                                         "TaxEnergyOnAccountAmount": amount(0, cur, "No energy tax paid on account."),
                                         "TaxEnergyBalanceAmount": amount(exc, cur, "Due with this bill."),
                                         "TaxScheme": {"ID": V("EXC", "Urvania's energy tax.")}}
            taxes = [{"TaxAmount": amount(exc, cur, "The energy tax on this point's electricity."),
                      "TaxSubtotal": [{"TaxAmount": amount(q * r, cur, f"{q} kWh at {r} ferra."),
                                       "BaseUnitMeasure": V("1", "Per kilowatt hour.", unitCode="KWH"),
                                       "PerUnitAmount": price(r, cur, "The rate of the tier."),
                                       **({"TierRange": V(correction_tier(q, r), "The kWh this subtotal "
                                                                                 "credits.")} if q < 0 else {}),
                                       "TaxCategory": {"ID": V("S", "The energy tax applies."),
                                                       "Name": V("Energy tax", "The tax in words."),
                                                       "TaxScheme": {"ID": V("EXC", "UN/EDIFACT 5153 code EXC: "
                                                                                    "excise duty, the energy "
                                                                                    "tax.")}}}
                                      for q, r in share]},
                     {"TaxAmount": amount(tax, cur, f"{rule[1]} % value added tax on the price and the energy "
                                                    "tax."),
                      "TaxSubtotal": {"TaxableAmount": amount(amt + exc, cur, "The price plus the energy tax."),
                                      "TaxAmount": amount(tax, cur, f"{rule[1]} % of it."),
                                      "TaxCategory": kit.tax_category(rule)}}]
            for ln_, a_, sh in lines_:
                e_ = sum(money(q * r, cur) for q, r in sh)
                t_ = money((a_ + e_) * Decimal(str(rule[1])) / 100, cur)
                ln_["TaxInclusiveLineExtensionAmount"] = amount(a_ + e_ + t_, cur, "With the energy tax and the "
                                                                                   "value added tax of the line.")
                ln_["TaxTotal"] = {"TaxAmount": amount(e_ + t_, cur, "The energy tax and the value added tax of "
                                                                     "the line.")}
            tax += exc
        if corr:
            # the correction's quantity and amount are in its consumption line: the correction's own quantity
            # and amount elements are defined for district heating (utilities/03#F7)
            supply["EnergyWaterConsumptionCorrection"] = {
                "CorrectionType": V("Estimate correction", "The kind of correction."),
                "CorrectionTypeCode": V("EST", "As a code."),
                "MeterNumber": V(pt["meter"][0], "The meter."),
                "Description": V(f"February's reading was estimated at {corr['estimate']:,} kWh, as the meter "
                                 "could not be reached; the readings of 31 January and 31 March, split by the "
                                 f"warehouse's load profile, put it at {pt['prev'][1]:,} kWh. February used {pt['history'][-1][2]:,} kWh, not the "
                                 f"{corr['billed']:,} kWh billed: the {corr['billed'] - pt['history'][-1][2]:,} "
                                 f"kWh are credited on line {corr['row'] + 1} of the bill.", "Why and how.")}
        consumption = {"UtilityStatementTypeCode": V(UTILITY[KIND[sup]], "The kind of supply."),
                       "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                      "EndDate": V("2026-03-31", "Its last day.")},
                       "TaxTotal": taxes,
                       "EnergyWaterSupply": supply,
                       "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, cur, "The consumption" +
                                                                            (", less February's correction." if corr
                                                                             else ".")),
                                              "PayableAmount": amount(amt + tax, cur, "With its taxes." if share
                                                                                        else "With its tax.")}}
        sub = {"ConsumptionID": V(f"{pt['id']}-2603", "The consumption of the point in March."),
               "SpecificationTypeCode": V("DETAILED", "A detailed specification."),
               "Note": V(pt["desc"], "The point."),
               "TotalMeteredQuantity": qty(consumed, unit, "Metered in March."),
               "UtilityConsumptionPoint": {
                   "ID": V(pt["id"], "The connection" + GRID_NUMBERS if sup == "33-xu" else "The connection's "
                                                                                             "number."),
                   "Description": V(pt["desc"], "Where."),
                   "SubscriberID": V(METERS[key][0], "The contract it belongs to."),
                   "SubscriberType": V(pt["type"][0], "The kind of customer."),
                   "SubscriberTypeCode": V(pt["type"][1], "As a code."),
                   "TotalDeliveredQuantity": qty(consumed, unit, "Delivered in March."),
                   "Address": address(subscriber),
                   **({"WebSiteAccess": {
                       "URI": V(PARTY[sup]["identity"].get("website", "https://www.example") + "/reading",
                                "Where the household enters its next meter reading, as it entered this one."),
                       "Login": V(pt["id"], "The household logs in with the number of its connection."),
                       "Password": V("RD-4K7-918", "The one-time reading code for the next reading, printed on each "
                                                   "statement: it opens the reading page only, from 28 April to 5 May "
                                                   "2026, so a household needs no account to send its reading.")}}
                      if pt["prev"][3] == "CUSTOMER" else {}),
                   "UtilityMeter": {"MeterNumber": V(pt["meter"][0], "The meter" + (GRID_NUMBERS if sup == "33-xu"
                                                                                     else ".")),
                                    "MeterName": V(pt["meter"][1], "Its name."),
                                    "MeterConstant": V(pt["meter"][2], "The register is multiplied by this."),
                                    "MeterConstantCode": V({"Direct": "DIRECT", "Transformer ratio": "CTRATIO"}[pt["meter"][3]],
                                                           "Why: " + pt["meter"][3].lower() + "."),
                                    "TotalDeliveredQuantity": qty(consumed, unit, "Delivered in March."),
                                    "MeterReading": reading,
                                    "MeterProperty": [{"Name": V("Accuracy class", "A property of the meter."),
                                                       "NameCode": V("ACC", "As a code."),
                                                       "Value": V("1", "Class 1."),
                                                       "ValueQualifier": V("Calibrated 2024", "When it was "
                                                                                              "checked.")},
                                                      {"Name": V("Maximum flow" if unit == "MTQ" else "Rated "
                                                                 "current", "A rating of the meter."),
                                                       "ValueQuantity": qty("2.5" if unit == "MTQ" else "5",
                                                                            "MQH" if unit == "MTQ" else "AMP",
                                                                            "Its value.")}]}},
               "Consumption": consumption,
               "SupplierConsumption": {
                   "Description": V("The supply under the customer's contract.", "What follows."),
                   "UtilitySupplierParty": party(sup, short=True),
                   "UtilityCustomerParty": party(customer, short=True),
                   "Consumption": {"UtilityStatementTypeCode": V(UTILITY[KIND[sup]], "The supply under the contract."),
                                   "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                                  "EndDate": V("2026-03-31", "Its last day.")},
                                   "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, cur, "The lines, "
                                                                                       "February's credit included."
                                                                                       if corr else "The line."),
                                                          "PayableAmount": amount(amt + tax, cur, "With its taxes."
                                                                                  if share else "With its tax.")}},
                   "Contract": {"ID": V(METERS[key][0], "The supply contract."),
                                "ContractType": V(f"{KIND[sup]} supply", "Its kind."),
                                "ValidityPeriod": {"StartDate": V("2024-01-01", "In force since.")}},
                   "ConsumptionLine": [line, cline] if corr else line}}
        if subscriber != customer:
            sub["SubscriberParty"] = party(subscriber, short=True)
        if pt.get("household"):
            out["MainOnAccountPayment"] = {"EstimatedConsumedQuantity": qty(14, unit, "The household's expected "
                                                                                      "monthly use."),
                                           "Note": V("The basis of the direct debit limit.", "Why it is "
                                                                                             "stated."),
                                           "PaymentTerms": {"Note": V("Collected by direct debit; the mandate's limit "
                                                                      "is set well above this estimate.",
                                                                      "How it is paid.")}}
            out["Signature"] = {"ID": V("CSW-SIG-26-0401", "The water company's seal."),
                                "SignatoryParty": party(sup, short=True)}
            sub["OnAccountPayment"] = {"EstimatedConsumedQuantity": qty(14, unit, "The expected use next month."),
                                       "Note": V("Paid on account each month for the estimated use; the next "
                                                 "bill settles it against the reading.", "How the household "
                                                                                          "pays between "
                                                                                          "readings."),
                                       "PaymentTerms": {"Note": V("By direct debit on the first working day of "
                                                                  "each month.", "When the payment on account "
                                                                                 "is collected.")}}
        out["SubscriberConsumption"] = sub
    else:                                     # the telecom company: lines, calls and data
        out["SubscriberConsumption"] = telecom_consumption(f, sup, key, customer)
    return out


def telecom_consumption(f, sup, key, customer):
    cur = "XLC"
    line_item, data_item = ITEM["telecom-line"], ITEM["telecom-data"]
    base = "+999 3 721 18"
    lines = []
    for k in range(6):
        number = f"{base}{50 + k}"
        x = {"ID": V(str(k + 1), "A business line."),
             "PhoneNumber": V(number, "The line's number; +999 is reserved, no real country's code."),
             "Description": V("Business line with calls on the island included.", "The subscription."),
             "LineExtensionAmount": amount(line_item["price"]["amount"], cur, "The monthly subscription."),
             "TaxInclusiveLineExtensionAmount": amount(line_item["price"]["amount"], cur, "No tax on the island."),
             "TaxTotal": {"TaxAmount": amount(0, cur, "No tax on the island.")}}
        x["TelecommunicationsService"] = {
            "ID": V(f"S-03-{k + 1}", "The month's calls on the island, summed: they are included."),
            "CallDate": V("2026-03-31", "Summed at the end of the month."),
            "CallTime": V("23:59:00", "At the close of the month."),
            "ServiceNumberCalled": V("island", "Calls within the island, not listed (privacy)."),
            "TelecommunicationsServiceCategory": V("Island calls", "The kind of service."),
            "Quantity": qty(140 + 25 * k, "MIN", "Minutes called on the island."),
            "CallExtensionAmount": amount(0, cur, "Included in the subscription.")}
        if k == 0:
            x["TelecommunicationsService"] = [x["TelecommunicationsService"],
                {"ID": V("C-0311-01", "A call."), "CallDate": V("2026-03-11", "The day."),
                 "CallTime": V("10:14:00", "The time."),
                 "ServiceNumberCalled": V(PARTY["6-xb"]["identity"]["contact"]["telephone"], "The distributor in "
                                                                                            "Bayvarra."),
                 "TelecommunicationsServiceCategory": Detail("a call to Bayvarra", "the call went to the "
                                                                                     "distributor in Bayvarra."),
                 "TelecommunicationsServiceCategoryCode": V("INT", "As a code."),
                 "Quantity": qty(12, "MIN", "Twelve minutes."),
                 "TelecommunicationsServiceCall": V("Outgoing", "The direction."),
                 "TelecommunicationsServiceCallCode": V("OUT", "As a code."),
                 "CallBaseAmount": amount(0, cur, "No set-up charge: included."),
                 "CallExtensionAmount": amount(0, cur, "Calls to the trade accord countries are included."),
                 "Country": {"IdentificationCode": V("XB", "The country called.")},
                 "CallDuty": {"Amount": amount(0, cur, "No call duty: included."),
                              "Duty": V("Set-up", "The kind of duty."), "DutyCode": V("SETUP", "As a code."),
                              "TaxCategory": kit.tax_category(kit.tax_rule(sup, customer, "telecom-line"))},
                 "TimeDuty": {"Amount": amount(0, cur, "No time duty: included."),
                              "Duty": V("Per minute", "The kind of duty."), "DutyCode": V("MIN", "As a code.")},
                 "Price": {"PriceAmount": price("0", cur, "Included in the subscription.")},
                 "TaxTotal": {"TaxAmount": amount(0, cur, "No tax on the island.")}},
                {"ID": V("D-0318-01", "Mobile data abroad."), "CallDate": V("2026-03-18", "The day."),
                 "CallTime": V("08:00:00", "From the morning."),
                 "ServiceNumberCalled": V("data", "Mobile data, no number called."),
                 "TelecommunicationsServiceCategory": Detail("mobile data in Bayvarra", "the phone used mobile "
                                                                                      "data on a network in Bayvarra."),
                 "TelecommunicationsServiceCategoryCode": V("ROAM", "As a code."),
                 "RoamingPartnerName": V("Lumeport mobile network", "The network used in Bayvarra."),
                 "Quantity": qty(35, "E34", "35 gigabytes beyond the subscriptions, at the trade fair in Lumeport."),
                 "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The partner network's currency."),
                                  "TargetCurrencyCode": V("XLC", "The bill's currency."),
                                  "CalculationRate": V("0.4", "The reference rate.")}}]
        lines.append(x)
    data_amt = money(Decimal(35) * Decimal(str(data_item["price"]["amount"])), cur)
    lines.append({"ID": V("7", "The data pool."), "PhoneNumber": V("data pool", "No number: the company's data pool."),
                  "Description": V("Mobile data beyond the subscriptions.", "What it is."),
                  "LineExtensionAmount": amount(data_amt, cur, "35 GB at the data tariff."),
                  "TelecommunicationsService": {"ID": V("D-03", "The month's data beyond the subscriptions."),
                                                "CallDate": V("2026-03-31", "Summed at the end of the month."),
                                                "CallTime": V("23:59:00", "At the close of the month."),
                                                "ServiceNumberCalled": V("data", "Mobile data."),
                                                "Quantity": qty(35, "E34", "Gigabytes."),
                                                "PayPerView": V("false", "Not a pay-per-view service."),
                                                "CallExtensionAmount": amount(data_amt, cur, "At the data "
                                                                                             "tariff.")}})
    total = Decimal(6) * Decimal(str(line_item["price"]["amount"])) + data_amt
    clines = [consumption_line(f, sup, key, k, d, d["invoice_why"])[0] for k, d in enumerate(BILLS[key])]
    return {"ConsumptionID": V("ST-1077-2603", "The telecom consumption of March."),
            "SpecificationTypeCode": V("DETAILED", "With the calls."),
            "TotalMeteredQuantity": qty(35, "E34", "The data beyond the subscriptions."),
            "UtilityConsumptionPoint": {"ID": V("ST-CP-1077", "The company's connection."),
                                        "Description": V("Office of Velumi Trading, Selanu", "Where."),
                                        "SubscriberID": V(METERS[key][0], "The contract."),
                                        "SubscriberType": V("Business", "The kind of customer."),
                                        "SubscriberTypeCode": V("BUS", "As a code."),
                                        "Address": address(customer)},
            "SupplierConsumption": {"UtilitySupplierParty": party(sup, short=True),
                                    "UtilityCustomerParty": party(customer, short=True),
                                    "Consumption": {"LegalMonetaryTotal": {
                                        "LineExtensionAmount": amount(total, cur, "The supply."),
                                        "PayableAmount": amount(total, cur, "No tax on the island.")}},
                                    "ConsumptionLine": clines},
            "Consumption": {"UtilityStatementTypeCode": V("TEL", "The kind of supply."),
                            "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                           "EndDate": V("2026-03-31", "Its last day.")},
                            "TelecommunicationsSupply": {
                                "TelecommunicationsSupplyType": V("Business lines and data", "The supply."),
                                "TelecommunicationsSupplyTypeCode": V("BUS", "As a code."),
                                "PrivacyCode": V("MASKED", "Numbers called inside the island are not listed; "
                                                           "calls abroad are."),
                                "Description": V("Six business lines and a mobile data pool.", "In words."),
                                "TotalAmount": amount(total, cur, "The telecom supply of March."),
                                "TelecommunicationsSupplyLine": lines},
                            "LegalMonetaryTotal": {"LineExtensionAmount": amount(total, cur, "The supply."),
                                                   "PayableAmount": amount(total, cur, "No tax on the island.")}}}


def bill_key(doc):
    sup = doc["from"] if doc["doc"] != "RemittanceAdvice" else doc["to"]
    cust = doc["to"] if doc["doc"] != "RemittanceAdvice" else doc["from"]
    if sup == "34-xb":
        return f"34-xb:{cust}"
    return sup


def utilities(n, doc):
    f = UTILITIES
    if doc["doc"] == "UtilityStatement":
        sup = doc["from"]
        key = bill_key({**doc, "to": doc["parties"].get("CustomerParty", doc["to"])})
        invoice_no = f.number(f"invoice-{key}", sup, "Invoice")
        return {"ID": V(f.number(f"statement-{n}", sup, "UtilityStatement"), "The utility's statement number."),
                "IssueDate": V(f.date(1), "Issued with the bill for March."),
                "UtilityStatementTypeCode": V(UTILITY[KIND[sup]], "The kind of utility the statement is about."),
                "DocumentCurrencyCode": kit.currency_line(kit.currency_of(sup), "the utility's currency"),
                "ParentDocumentReference": {"ID": V(invoice_no, "The invoice this statement supplements: a utility "
                                                                "statement adds the consumption behind the bill.")},
                **utility_statement(f, n, doc, key, invoice_no)}
    if doc["doc"] == "Invoice":
        key = bill_key(doc)
        out = kit.invoice(f, n, doc, 1, "The monthly bill, issued on the first day of the next month.", {},
                          BILLS[key], key=f"invoice-{key}", extra=MARCH, terms="utility")
        purpose = {"33-xu": ("ELEC", "an electricity bill"), "35-xl": ("PHON", "a telephone bill")}.get(
            key, ("WTER", "a water bill"))
        meters = METERS[key]
        out["PurchaseReference"] = {"ID": V(meters[0], "The customer's contract number with the utility."),
                                    "Description": V("Supply contract", "What the number is.")}
        for line, meter, bill in zip(out["InvoiceLine"], meters[1:], BILLS[key]):
            code, what = ("GASB", "a gas bill") if ITEM[bill["item"]].get("utility") == "gas" or "gas" in bill["item"] \
                else purpose
            line["PaymentPurposeCode"] = V(code, f"What the payment of this line is for, as an ISO 20022 purpose: "
                                                 f"{what}.")
            if meter:
                line["PurchaseReference"] = {"ID": V(meter[0], "The meter or subscription the line is for."),
                                             "Description": V(meter[1], "Where it is.")}
        if key == "33-xu":
            out["InvoiceLine"][1]["OriginatorParty"] = party("8-xu", short=True)
            out["BillingReference"] = {"InvoiceDocumentReference": {
                "ID": V("FE-INV-26-0211", "February's bill, with an estimated reading of the warehouse meter."),
                "IssueDate": V("2026-03-01", "Its issue date.")},
                "BillingReferenceLine": {"ID": V("2", "Its warehouse line, billed on the estimate: line 4 of this "
                                                      "bill credits the 750 kWh it charged too much, as the "
                                                      "warehouse's statement explains (utilities/02#F7).")}}
            energy_tax(f, out, key)
        if key == "34-xb:c-xb":                 # the household pays by direct debit under a mandate
            m = PARTY["c-xb"]["identity"]["mandate"]
            out["PaymentMeans"] = {
                "ID": V("1", "The only way to pay."),
                "PaymentMeansCode": V("49", "UN/EDIFACT 4461 code 49: direct debit.", listID="UN/EDIFACT EDED 4461"),
                "PaymentDueDate": V(f.date(22), "The day the amount will be collected."),
                "PaymentID": V(kit.rf_reference(f.numbers[f"invoice-{key}"]), "The reference on the household's bank "
                                                                              "statement."),
                "PaymentMandate": {
                    "ID": V(m["id"], "The mandate the household signed for the water company."),
                    "MandateTypeCode": V("RCUR", "A mandate for repeated collections."),
                    "MaximumPaidAmount": amount(m["max"], "XBL", "The most the company may collect at a time."),
                    "SignatureID": V(f"SIG-{m['id']}", "The reference of the signature on the mandate."),
                    "PayerParty": party("c-xb", short=True),
                    "PayerFinancialAccount": kit.account("c-xb", "The household's account the bill is collected "
                                                                 "from."),
                    "ValidityPeriod": {"StartDate": V(m["signed"], "Signed when the household moved in.")},
                    "PaymentReversalPeriod": {"DurationMeasure": V("8", "The household can reverse a collection "
                                                                        "within eight weeks.", unitCode="WEE")},
                    "Clause": {"ID": V("CSW-DD-T3", "The clause of the mandate on notice."),
                               "Content": V("The company announces each collection at least five days before.",
                                            "What the clause says.")}},
                "PayeeFinancialAccount": kit.account("34-xb", "The water company's account the collection goes to.")}
            out["PaymentTerms"]["Note"] = V("21 days net from the bill. Collected by direct debit on that day.",
                                            "The Trade Accord's utility term, and how the household pays: by the "
                                            "direct debit of its mandate.")
        return out
    if doc["doc"] == "RemittanceAdvice":
        purpose = {"33-xu": ("ELEC", "an electricity bill, the larger part of the bill paid"),
                   "35-xl": ("PHON", "a telephone bill")}.get(bill_key(doc), ("WTER", "a water bill"))
        return kit.remittance(f, n, doc, 18, "Paid before the due date.", key=f"invoice-{bill_key(doc)}",
                              purpose=purpose)
    if doc["doc"] == "Reminder":
        key, cur = bill_key(doc), "XBL"
        due = f.numbers[f"invoice-{key}-amount"]
        return {"ID": V(f.number("reminder", doc["from"], "Reminder"), "The reminder number."),
                "IssueDate": V(f.date(30), "Sent a week after the due date passed without payment."),
                "ReminderTypeCode": V("PAYMENT", "A reminder of a payment overdue."),
                "ReminderSequenceNumeric": V("1", "The first reminder."),
                "Note": V("The direct debit was returned by your bank: insufficient funds.", "Why the bill is "
                                                                                              "unpaid."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the unpaid bill"),
                "ReminderPeriod": {"StartDate": V(f.date(22), "Overdue from the failed collection."),
                                   "EndDate": V(f.date(30), "Until the reminder.")},
                "LineCountNumeric": V("2", "The bill and the fee."),
                "AdditionalDocumentReference": {"ID": V("BLUM-RTN-26-04-0193", "The bank's notice that the direct "
                                                                               "debit was returned."),
                                                "DocumentTypeCode": V("RETURNNOTICE", "What the document is."),
                                                "IssueDate": V(f.date(23), "The day after the failed collection."),
                                                "DocumentDescription": V("Direct debit returned: insufficient "
                                                                         "funds.", "What it says."),
                                                "IssuerParty": party("25-xb", short=True)},
                "PayeeParty": party("34-xb", short=True),
                "PaymentTerms": {"Note": V("Please pay within ten days by credit transfer; the next collection will "
                                           "be by direct debit again.", "What the household is asked to do. No "
                                           "interest is charged: the Trade Accord's utility term says nothing on "
                                           "late payment, and Bayvarra has no statutory rate (O148); the company "
                                           "charges only the bank's fee (utilities/10#F9)."),
                                 "PaymentDueDate": V(f.date(40), "Ten days after the reminder.")},
                "TaxTotal": {"TaxAmount": amount(0, cur, "No sales tax on a reminder fee."),
                             "TaxSubtotal": {"TaxableAmount": amount(Decimal("5.00"), cur, "The fee."),
                                             "TaxAmount": amount(0, cur, "No tax: the fee is outside the scope "
                                                                         "of the sales tax."),
                                             "TaxCategory": {"ID": V("O", "A reminder fee is compensation, not a "
                                                                          "supply: outside the scope of the sales "
                                                                          "tax."),
                                                             "TaxExemptionReason": V("Compensation for late payment",
                                                                                     "Why no tax."),
                                                             "TaxScheme": {"ID": V("STT", "UN/EDIFACT 5153 code of "
                                                                                         "the state sales tax.")}}}},
                "PaymentMeans": {"PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer, how the household "
                                                             "is asked to pay.", listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account(doc["from"], "The utility's account, where the "
                                                                                   "overdue amount is to be paid.")},
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(due + Decimal("5.00"), cur, "The bill and the "
                                                                                                 "reminder fee."),
                                       "PayableAmount": amount(due + Decimal("5.00"), cur, "The amount now due: the "
                                                                                          "whole bill and the fee.")},
                "ReminderLine": [{"ID": V("1", "The unpaid bill."),
                                 "DebitLineAmount": amount(due, cur, "The amount of the unpaid invoice."),
                                 "BalanceBroughtForwardIndicator": V("false", "Not a balance carried over: one "
                                                                              "bill."),
                                 "PaymentPurposeCode": V("WTER", "ISO 20022 purpose code WTER: water bill."),
                                 "ReminderPeriod": {"StartDate": V(f.date(22), "Overdue since the collection "
                                                                               "failed.")},
                                 "BillingReference": {"InvoiceDocumentReference": {
                                     "ID": V(f.numbers[f"invoice-{key}"], "The invoice not paid."),
                                     "IssueDate": V(f.numbers[f"invoice-{key}-date"], "Its issue date.")}}},
                                 {"ID": V("2", "The reminder fee."),
                                  "DebitLineAmount": amount(Decimal("5.00"), cur, "The fee for a returned direct "
                                                                                  "debit, as the terms set."),
                                  "Amount": amount(Decimal("5.00"), cur, "The fee charged."),
                                  }]}
    raise SystemExit(f"utilities scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the wood flow (Bayvarra -> Urvania, and at home)
PALLETS_CHARGE = {"like": "slat-bundle-1800", "amount": "240.00", "reason": "Heat-treated export pallets",
                  "code": "ACH",
                  "code_why": "The reason for the charge as a code of UN/EDIFACT 7161: the pallets are heat-treated.",
                  "why": "The 96 bundles travel four to a pallet, on 24 pallets treated to ISPM 15, as the quotation "
                         "offered for the export.",
                  "amount_why": "24 pallets at 10.00 lume."}
# D43: the sawmill sells the bundle of 50 slats as its item; this quarter's delivery is oak, 96 bundles (4,800 slats,
# enough for 960 benches) on 24 pallets of four, one truck
SLATS = [{"item": "slat-bundle-1800", "ordered": 96, "why": "96 bundles of 50 oak slats, 4,800 slats: enough for 960 "
                                                            "benches at five a bench, a quarter's supply (D43)."}]
WOOD_PALLETS = 24
ASH_BUNDLE = Decimal("330.00")       # the priced alternative of the quotation: the same bundle in ash (D43)
# the furniture maker's certificate that it buys timber for manufacture, which frees the sale from Upland State's sales
# tax (wood/11#F5): issued by the state's revenue office, quoted in its order and in the sawmill's invoice
EXEMPTION_CERT = {"ID": V("UL-STT-EX-2024-0377", "The number of Brackenmere's exemption certificate, as Upland State's "
                                                 "revenue office issued it."),
                  "IssueDate": V("2024-01-15", "The day it was issued."),
                  "DocumentType": V("Sales tax exemption certificate: purchase for manufacture (Upland State)",
                                    "The certificate the exemption of the sale rests on (D43).")}
TIMBER = [{"item": "timber-beam", "ordered": 12, "why": "Hardwood for a month of furniture production."}]
WOOD = kit.Flow("wood", "2026-02-16", SLATS)


def wood_pallets(f):
    """The 24 pallets of the slat delivery as transport handling units, each with its four bundles as packages (D43,
    wood/06#F12, 08#F10): what the pallet charge is for."""
    it = ITEM["slat-bundle-1800"]
    pal = it["pallet"]
    per = pal["per"]
    out = {"TransportHandlingUnitTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
           "HandlingCode": V("STACK2", "The carrier's handling code: two high."),
           "HandlingInstructions": V("Fork-lift only. May be stacked two high. A bundle of 225 kg is lifted by "
                                     "machine, never by hand.", "The handling, in words, with the world's rule for "
                                                                "manual handling (D20)."),
           "TotalPackageQuantity": qty(per, "EA", f"{per} bundles on each pallet, two by two."),
           "Package": {"Quantity": qty(it["pack"]["size"], "EA", f"{it['pack']['size']} slats in a bundle."),
                       "PackagingTypeCode": V("BE", "UN/ECE Recommendation 21 code BE: bundle."),
                       "PackingMaterial": V("Steel straps", "What holds a bundle together.")},
           "MeasurementDimension": [
               {"AttributeID": V("LENGTH", "The loaded pallet's footprint."),
                "Measure": V(str(pal["mm"][0]), "Its length: the slats' length.", unitCode="MMT")},
               {"AttributeID": V("WIDTH", "The loaded pallet's footprint."),
                "Measure": V(str(pal["mm"][1]), "Its width: two bundles of 475 mm side by side.", unitCode="MMT")},
               {"AttributeID": V("HEIGHT", "The height of the loaded pallet."),
                "Measure": V(str(pal["mm"][2]), "Two bundles of 380 mm on the pallet.", unitCode="MMT")},
               {"AttributeID": V("GROSSWEIGHT", "The loaded pallet's weight."),
                "Measure": V(kit.kg(per * it["gross_kg"] + pal["tare_kg"]), f"Four bundles of {it['gross_kg']} kg "
                             f"and the pallet's own {pal['tare_kg']} kg.", unitCode="KGM")}]}
    return [{"ID": kit.unit_id("36-xb", f, k), **out} for k in range(1, WOOD_PALLETS + 1)]


def quotation_lines(f, deal, cur, with_price):
    out = []
    for i, d in enumerate(deal, 1):
        li = {"ID": V(str(i), "The line number."),
              "Quantity": qty(d["ordered"], ITEM[d["item"]]["unit"], d["why"]),
              "Item": item(d["item"])}
        if with_price:
            p = kit.unit_price(d["item"], cur)
            li["LineExtensionAmount"] = amount(Decimal(str(d["ordered"])) * p, cur, "Quantity times the quoted price.")
            li["Price"] = kit.price_block(d["item"], cur)
        out.append({"LineItem": li})
    return out


def rfq(f, doc, day, why, deal):
    return {"ID": V(f.number("rfq", doc["from"], "RequestForQuotation"), "The buyer's request number."),
            "IssueDate": V(f.date(day), why),
            "IssueTime": V("10:00:00", "The time of the request; quotations refer to it."),
            "RequestForQuotationLine": quotation_lines(f, deal, None, False)}


def quotation(f, doc, day, why, deal, validity):
    cur = kit.currency_of(doc["from"])
    total = sum(Decimal(str(d["ordered"])) * kit.unit_price(d["item"], cur) for d in deal)
    return {"ID": V(f.number("quotation", doc["from"], "Quotation"), "The seller's quotation number."),
            "IssueDate": V(f.date(day), why),
            "ValidityPeriod": {"EndDate": V(f.date(day + validity), "How long the quoted prices hold.")},
            "RequestForQuotationDocumentReference": ref(f, "rfq", "The request this quotation answers."),
            "QuotedMonetaryTotal": {"LineExtensionAmount": amount(total, cur, "The sum of the quoted lines."),
                                    "PayableAmount": amount(total, cur, "The quoted total, before any tax.")},
            "QuotationLine": quotation_lines(f, deal, cur, True)}


def wood(n, doc):
    f = WOOD
    if doc["doc"] == "RequestForQuotation":
        return rfq(f, doc, 0, "The manufacturer asks for slats to its own dimensions.", SLATS)
    if doc["doc"] == "Quotation":
        return quotation(f, doc, 3, "The sawmill quotes for the slats.", SLATS, 30)
    if doc["doc"] == "Order" and doc["from"] == "5-xu":
        return kit.order(f, n, doc, 7, "The manufacturer accepts the quotation and orders, on the Monday after it "
                                       "(D27).",
                         "Delivered at place, the factory: the sawmill delivers; the manufacturer clears the import.",
                         "Valdara Industries, goods-in, Ferrano",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted.")})
    if doc["doc"] == "TransportExecutionPlanRequest":
        w = kit.gross_weight(f, "ordered")
        truck = kit.fleet("13-xu", "T-07")
        tare = sum(truck["tare_kg"].values())
        if w > WORLD["road_rules_accord"]["max_combination_kg"] - tare:
            raise SystemExit(f"wood: {w} kg of slats exceed the payload of Trasvia's truck (O134)")
        out = kit.tep_request(f, n, doc, 7, "Under DAP the sawmill books the truck across the border.", 10, w,
                              "96 bundles of slats on 24 pallets, with the pallets.")
        kit.deep_merge(out["Consignment"], {
            "TotalTransportHandlingUnitQuantity": V(str(WOOD_PALLETS), "The pallets to be carried, four bundles on "
                                                                       "each (D43)."),
            "TotalPackagesQuantity": V(str(WOOD_PALLETS * 4), "The bundles on them.")})
        return out
    if doc["doc"] == "ExportCustomsDeclaration":
        out = kit.export_declaration(f, n, doc, 10, "Declared the morning the truck leaves for the border.",
                                     "The value of the slats, in lume.")
        out["IssueTime"] = V("08:40:00", "After the despatch advice and the invoice, while the loaded truck waits "
                                         "at the sawmill for customs to release the slats (timelines#F6).")
        return out
    if doc["doc"] == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, 10, "The day the truck was loaded at the sawmill.",
                                  "The gross weight of the bundles with their pallets.")
        out["Shipment"]["TransportHandlingUnit"] = wood_pallets(f)
        out["IssueTime"] = V("08:10:00", "When the truck is loaded, before it leaves once customs has released "
                                         "the export.")
        return out
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 11, "The manufacturer declares the import into Urvania.",
                                      "The customs value in ferra: the value in lume at the reference rate (1 lume = 100 "
                                      "ferra).")
    if doc["doc"] == "Invoice" and doc["to"] == "5-xu":
        return kit.invoice(f, n, doc, 10, "Issued when the slats leave.",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "slat-bundle-1800", "qty": 96, "invoice_why": "The bundles despatched, "
                                                                                   "4,800 slats."}],
                           charges=[PALLETS_CHARGE])
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The manufacturer pays across the border.")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 21, "The furniture maker orders timber, collected with its own van; ordered on "
                                        "the Monday (D27).",
                         "Ex works the sawmill: the buyer collects the timber and bears every cost from the sawmill's "
                         "yard.", "Marrowdale Sawmill, timber yard", {"AdditionalDocumentReference": EXEMPTION_CERT},
                         deal=TIMBER,
                         key="order-timber")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 22, "Issued when the timber was collected.",
                           {"OrderReference": ref(f, "order-timber", "The furniture maker's order."),
                            "AdditionalDocumentReference": EXEMPTION_CERT},
                           [{"item": "timber-beam", "qty": 12, "invoice_why": "The cubic metres collected."}],
                           key="invoice-timber",
                           extra={"Delivery": {"ActualDeliveryDate": V(f.date(22), "Ex works: delivered when the "
                                                                                  "furniture maker collected the "
                                                                                  "timber (wood/11#F4)."),
                                               "DeliveryLocation": {"Name": V("Marrowdale Sawmill, timber yard",
                                                                              "Where the timber was collected.")}}})
    raise SystemExit(f"wood scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the furniture flow (Bayvarra)
# The Elderwick Marrow line (D7, D32): the store's own label, made by Brackenmere. Bench and chair are items of their
# own, ordered, delivered, invoiced and credited one by one at 380 and 115 lume; the care kit comes free with each
# bench; the Marrow set (a bench and two chairs) is only the shop's offer, so no document between maker and store
# knows it. Stock, thresholds and sales are counted in pieces. Bench and chair each come in oak and in ash, and the
# shopper chooses, so each wood is an item of its own with a GTIN of its own (O155); prices are the same for both
# woods. The store plans three oak pieces for every two in ash: the opening stock is 12 oak and 8 ash benches, 24 oak
# and 16 ash chairs, twice the targets of 6 and 4 benches, 12 and 8 chairs. The line is for the reopening of the
# store's home and garden department on Monday 11 May (D34, O155): the stock comes in March and waits for it, and the
# first sale is on the day of the reopening. The sale-or-return trial is the first four weeks of sales, 11 May to
# Sunday 7 June, the four weeks the exception criteria and the sales report measure; the stock above the target at its
# end goes back. The webshop's Marrow set in ash (retail/22, 30 May) is one of the sales the report counts.
WOODS = ("oak", "ash")
WEBSHOP_WOOD = "ash"     # the wood of the shopper's Marrow set in the webshop (retail/22), one of the sets reported
MARROW_TARGET = {"bench": {"oak": 6, "ash": 4}, "chair": {"oak": 12, "ash": 8}}    # the stock policy, per item
MARROW_MINIMUM = {"bench": {"oak": 2, "ash": 2}, "chair": {"oak": 4, "ash": 4}}
MARROW_THRESHOLD = {"oak": 3, "ash": 2}      # benches sold in the first four weeks: five in all, by the targets
MARROW_SOLD = {"bench": {"oak": 2, "ash": 1}, "chair": {"oak": 7, "ash": 3}}       # the four weeks to 7 June
MARROW_SETS = {"oak": 2, "ash": 1}            # three sets sold, by wood; the other chairs were sold alone
MARROW_ASK = [{"item": "marrow-bench-oak", "ordered": 12, "why": "Twelve benches in oak, as the store plans the opening "
                                                                 "stock: three oak pieces for every two in ash."},
              {"item": "marrow-bench-ash", "ordered": 8, "why": "Eight benches in ash."},
              {"item": "marrow-chair-oak", "ordered": 24, "why": "Twenty-four chairs in oak: two for each oak bench."},
              {"item": "marrow-chair-ash", "ordered": 16, "why": "Sixteen chairs in ash: two for each ash bench."}]
MARROW_QUOTE = MARROW_ASK + [{"item": "marrow-care-kit", "ordered": 20, "why": "One care kit free with each bench, "
                                                                               "oak or ash."}]


def pieces(iid):
    """A Marrow item in words, in the plural: "oak benches"."""
    piece, wood = iid.split("-")[1:3]
    return f"{wood} {piece}{'es' if piece == 'bench' else 's'}"


def marrow_items(piece):
    """The items of a piece of the line, in both woods."""
    return [item(f"marrow-{piece}-{w}") for w in WOODS]


def marrow_line(n, why):
    """What the store's opening order says on the line of a piece in one wood, of n pieces."""
    q = lambda k, w: qty(k, "EA", w)
    return {"Note": V(why, "What the line is."),
            "MinimumQuantity": q(n // 2, "The store accepts a first part of at least half the line."),
            "MaximumQuantity": q(n, "And no more than ordered."),
            "BackOrderAllowedIndicator": V("true", "What cannot be delivered now may follow."),
            "MinimumBackorderQuantity": q(n // 4, "But only in lots of at least a quarter of the line."),
            "MaximumBackorderQuantity": q(n // 2, "And at most half the line on back order."),
            "InspectionMethodCode": V("VISUAL", "The goods-in checks each piece by eye."),
            "AccountingCostCode": V("6120", "The cost centre of the home and garden department, which sells the "
                                            "line."),
            "AccountingCost": V("Home and garden department", "In words."),
            "WarrantyValidityPeriod": {"DurationMeasure": V("2", "Two years on the joints.", unitCode="ANN")},
            "WarrantyParty": party("37-xb", short=True)}


MARROW_ORDER_WHY = {"marrow-bench-oak": "Twice the target of six oak benches: the shelf and the display in the home "
                                        "and garden department when it reopens.",
                    "marrow-bench-ash": "Twice the target of four ash benches, for the shelf and the display.",
                    "marrow-chair-oak": "Twice the target of twelve oak chairs, two with each oak bench.",
                    "marrow-chair-ash": "Twice the target of eight ash chairs, two with each ash bench.",
                    "marrow-care-kit": "Free: one care kit with each bench, oak or ash."}


def marrow_order():
    out = []
    for k, d in enumerate(MARROW_QUOTE, 1):
        it, why = ITEM[d["item"]], MARROW_ORDER_WHY[d["item"]]
        if it.get("free_with"):
            x = {**d, "line_extra": {"Note": V(why, "What the line is.")}}
        else:
            x = {**d, "line_extra": marrow_line(d["ordered"], why)}
            x["line_extra"]["PricingReference"] = {"OriginalItemLocationQuantity": {"Price": {
                "PriceAmount": price(Decimal(str(it["price"]["amount"])), "XBL", "The price of the quotation, which "
                                                                                "the order accepts.")}}}
        x["orderline_extra"] = {"Note": V("Price as quoted.", "Why no price question."),
                                "QuotationLineReference": {"LineID": V(str(k), "The quotation line accepted.")}}
        out.append(x)
    return out


MARROW_ORDER = marrow_order()
MARROW_REPEAT = [{"item": "marrow-bench-oak", "ordered": 6, "why": "Six oak benches for the winter: one target's "
                                                                   "worth."},
                 {"item": "marrow-bench-ash", "ordered": 4, "why": "Four ash benches: one target's worth."},
                 {"item": "marrow-chair-oak", "ordered": 12, "why": "Twelve oak chairs, two with each oak bench."},
                 {"item": "marrow-chair-ash", "ordered": 8, "why": "Eight ash chairs, two with each ash bench."},
                 {"item": "marrow-care-kit", "ordered": 10, "why": "One care kit free with each bench, oak or ash."}]
MARROW_BACK = [("marrow-bench-oak", 4, "Four oak benches: the stock above the target of six."),
               ("marrow-bench-ash", 3, "Three ash benches: the stock above the target of four."),
               ("marrow-chair-oak", 5, "Five oak chairs: the stock above the target of twelve."),
               ("marrow-chair-ash", 5, "Five ash chairs: the stock above the target of eight."),
               ("marrow-care-kit", 7, "The care kits of the seven benches.")]
# the goods balance at the end of the trial, per item (D32, O155): what came in, less what was sold, less what goes
# back, is the stock policy's target; the free care kits follow the benches
_IN = {d["item"]: d["ordered"] for d in MARROW_QUOTE}
for _iid, _q, _ in MARROW_BACK:
    if _iid == "marrow-care-kit":
        assert _q == sum(q for i, q, _w in MARROW_BACK if "-bench-" in i)
        continue
    _p, _w = _iid.split("-")[1:3]
    assert _IN[_iid] - MARROW_SOLD[_p][_w] - _q == MARROW_TARGET[_p][_w], _iid
assert sum(MARROW_SETS.values()) == 3 and all(MARROW_SOLD["bench"][w] == MARROW_SETS[w] for w in WOODS)
assert sum(d["ordered"] for d in MARROW_REPEAT if "-bench-" in d["item"]) == 10
assert MARROW_SETS[WEBSHOP_WOOD] >= 1        # the webshop's set is among the sets the report counts
DESKS = [{"item": "office-desk", "ordered": 6, "why": "Six desks for the new planning office."},
         {"item": "installation", "ordered": 14, "why": "Two installers for seven hours."}]
FURNITURE = kit.Flow("furniture", "2026-03-02", MARROW_ORDER)
OWN_LABEL = "BM-OWN-BRAND-2026"    # the own-label agreement: specification, sale-or-return trial, returns (D32)


def collab(f, doc, key, day, why):
    return {"ID": V(f.number(key, doc["from"], key), f"The sender's number for its {key.replace('-', ' ')}."),
            "IssueDate": V(f.date(day), why)}


def marrow_profile(f, iid, target, minimum, multiple, why_multiple, smallest):
    """The store's replenishment policy for one piece of the line, in pieces (D32)."""
    return {"EffectivePeriod": period(f, 21, 180, "From the first delivery.", "To the end of the season."),
            "MinimumInventoryQuantity": qty(minimum, "EA", f"Never fewer than {minimum} in the shop."),
            "MultipleOrderQuantity": qty(multiple, "EA", why_multiple),
            "OrderIntervalDaysNumeric": V("14", "An order every two weeks."),
            "ReplenishmentOwnerDescription": V("The store orders; the maker proposes.", "Who replenishes."),
            "TargetServicePercent": V("95", "On the shelf on 95 % of the days."),
            "TargetInventoryQuantity": qty(target, "EA", f"The stock the store aims at: {target}."),
            "ItemLocationQuantity": {"LeadTimeMeasure": V("5", "Five days from order to shelf.", unitCode="DAY"),
                                     "MinimumQuantity": qty(smallest, "EA", "The smallest order.")},
            "Item": item(iid)}


def marrow_sales(p, w):
    """A line of the store's sales report, for the maker's replenishment: one item in pieces, and how many were sold
    in a Marrow set or alone. The shop's prices and its set allowance are the store's own business under its own
    label: the maker does not fund the set price, so the report does not give them (O155)."""
    n, sets = MARROW_SOLD[p][w], MARROW_SETS[w]
    words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 6: "Six", 7: "Seven"}
    out = {"Quantity": qty(n, "EA", f"{words[n]} {pieces(f'marrow-{p}-{w}') if n > 1 else w + ' ' + p} sold in the "
                                    "four weeks since the reopening" + ({1: ", in a Marrow set.", 2: ", both in Marrow sets."}.get(n, ", all in Marrow sets.")
                                               if p == "bench" else
                                               f": {2 * sets} in the {w} set{'s' if sets > 1 else ''} and "
                                               f"{n - 2 * sets} alone."))}
    if p == "bench":
        out["ActivityProperty"] = {"Name": V("Sold in a Marrow set", "What the store notes."),
                                   "Value": V(f"{sets} of {n}, " + ("each " if sets > 1 else "") + f"with two {w} chairs"
                                              + (": the webshop order of 30 May, for collection in the department."
                                                 if w == WEBSHOP_WOOD else "."),
                                              "How the benches sold.")}
    else:
        out["ActivityProperty"] = {"Name": V("Sold alone", "What the store notes."),
                                   "Value": V(f"{n - 2 * sets} of {n}: the 1400 mm bench is too long for many "
                                              "apartment kitchens, so shoppers buy the chairs.",
                                              "Why the chairs sell better than the set.")}
    out["Item"] = item(f"marrow-{p}-{w}")
    return out


def furniture(n, doc):
    f = FURNITURE
    if doc["doc"] == "RequestForQuotation":
        return rfq(f, doc, 0, "The store wants its own label's dining furniture for the autumn and winter home "
                              "range of its home and garden department, which reopens on 11 May.", MARROW_ASK)
    if doc["doc"] == "Quotation":
        return quotation(f, doc, 4, "The furniture maker quotes the line.", MARROW_QUOTE, 60)
    if doc["doc"] == "ItemInformationRequest":
        return {**collab(f, doc, "info-request", 10, "Asked before the first production run."),
                "Period": period(f, 70, 180, "The season the information is wanted for: from the reopening of "
                                             "the home and garden department on 11 May, when the line goes on "
                                             "sale.", "Its end, as the store's replenishment policy."),
                "ItemInformationRequestLine": {
                    "Period": period(f, 70, 180, "Sales data from the first day of sales.", "To the end of the "
                                                                                           "season."),
                    "SalesItem": [{"Quantity": qty(d["ordered"], "EA", f"The {pieces(d['item'])} of the first "
                                                                         "delivery, to compare sales against."),
                                   "Item": item(d["item"])} for d in MARROW_ASK]}}
    if doc["doc"] == "TradeItemLocationProfile":
        return {**collab(f, doc, "location-profile", 11, "The store sets its replenishment policy for the line, on "
                                                         "the Friday before the order."),
                "Period": period(f, 14, 180, "The policy holds for the season.", "Its end."),
                "ItemManagementProfile": [
                    marrow_profile(f, f"marrow-{p}-{w}", MARROW_TARGET[p][w], MARROW_MINIMUM[p][w], *(
                        (2, "Benches in pairs: one row of the maker's van.", 2) if p == "bench" else
                        (4, "Chairs in fours: two for each of a pair of benches.", 4)))
                    for p in ("bench", "chair") for w in WOODS]}
    if doc["doc"] == "ExceptionCriteria":
        return {**collab(f, doc, "exception-criteria", 11, "Agreed together with the replenishment policy."),
                "ValidityPeriod": period(f, 14, 180, "Valid for the season.", "Its end."),
                "ExceptionCriteriaLine": [{
                    "ID": V(str(k), f"A sales criterion on the {w} bench: the line is planned around the bench, and "
                                    "a criterion is set per item, so each wood has its own."),
                    "ThresholdValueComparisonCode": V("LT", "An exception is raised when actual sales fall "
                                                            "below the threshold."),
                    "ThresholdQuantity": qty(MARROW_THRESHOLD[w], "EA", (
                        f"Fewer than {'three' if w == 'oak' else 'two'} {w} benches sold in the first four weeks is "
                        "worth a message: five benches in all, shared by the woods as the stock targets are.")),
                    "SupplyItem": item(f"marrow-bench-{w}")} for k, w in enumerate(WOODS, 1)]}
    if doc["doc"] == "ProductActivity":
        return {**collab(f, doc, "activity", 98, "The store's report of the first four weeks of sales, on the "
                                                 "Monday after them."),
                "ActivityPeriod": period(f, 70, 97, "The four weeks reported: from the reopening of the home and "
                                                    "garden department on Monday 11 May, the first day of sales.",
                                         "Their end: Sunday 7 June."),
                "SupplyChainActivityDataLine": {
                    "ID": V("1", "The only line."),
                    "SupplyChainActivityTypeCode": V("SALES", "The activity reported: sales to consumers."),
                    "ActivityOriginLocation": {**kit.gln_location("26-xb", "garden"),
                                               "Name": V("Brightmarket Stores, home and garden department, Lumeport",
                                                         "Where the sales took place.")},
                    "SalesItem": [marrow_sales(p, w) for p in ("bench", "chair") for w in WOODS]}}
    if doc["doc"] == "ExceptionNotification":
        return {**collab(f, doc, "exception", 99, "The furniture maker sees the sales below the agreed threshold, "
                                                  "the day after the store's report."),
                "ExceptionObservationPeriod": period(f, 70, 97, "The four weeks observed: the first four weeks of "
                                                                "sales, from the reopening.", "Their end."),
                "ExceptionNotificationLine": [{
                    "ID": V(str(k), f"The exception on the {w} bench."),
                    "ComparedValueMeasure": V(str(MARROW_SOLD["bench"][w]), f"The value compared: the {w} benches the "
                                                                          "store reported sold.", unitCode="EA"),
                    "SourceValueMeasure": V(str(MARROW_THRESHOLD[w]), "The value it is compared with: the agreed "
                                                                     f"threshold for the {w} bench in four weeks.",
                                            unitCode="EA"),
                    "SupplyItem": item(f"marrow-bench-{w}")} for k, w in enumerate(WOODS, 1)]}
    if doc["doc"] == "Order" and doc["from"] == "26-xb":
        return kit.order(f, n, doc, 14, "The store orders the opening stock of its line.",
                         "Delivered at place, the store: the furniture maker delivers with its own van.",
                         "Brightmarket Stores, goods-in, Lumeport",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted."),
                          "Note": V("Opening stock of the Elderwick Marrow line, in oak and in ash: twice the target "
                                    "of each item, to fill the display in the home and garden department when it "
                                    "reopens on 11 May as well as the shelf; the store holds the stock until "
                                    "then.", "Why the order is "
                                                                                           "larger than the stock "
                                                                                           "policy's target.")})
    if doc["doc"] == "Invoice" and doc["to"] == "26-xb":
        return kit.invoice(f, n, doc, 21, "Issued on the day of delivery.",
                           {"OrderReference": ref(f, "order", "The store's order."),
                            "DeliveryNoteDocumentReference": {"ID": V("BF-DN-26-0323", "The delivery note the store "
                                                                                       "signed when the van "
                                                                                       "unloaded.")}},
                           [{"item": d["item"], "qty": d["ordered"], "invoice_why": f"The {pieces(d['item'])} "
                                                                                       "delivered."}
                            for d in MARROW_ASK] +
                           [{"item": "marrow-care-kit", "qty": 20, "invoice_why": "One care kit with each bench.",
                             "line_extra": {
                                 "Note": V("Hard-wax oil and a cloth, one with each bench, for the store to hand on "
                                           "with the bench it sells.", "What the line is."),
                                 "FreeOfChargeIndicator": V("true", "The care kits come free with the benches.")}}])
    if doc["doc"] == "InstructionForReturns":
        return {**collab(f, doc, "returns", 101, "After the end of the sale-or-return trial on Sunday 7 June, once "
                                                 "the store's report and the exception have shown the stock."),
                "InstructionForReturnsLine": [
                    {"ID": V(str(k), "A line per piece."), "Quantity": qty(q, "EA", why),
                     "Note": V("In their original cartons.", "How they are to be returned."),
                     "ManufacturerParty": party("37-xb", short=True), "Item": item(iid)}
                    for k, (iid, q, why) in enumerate(MARROW_BACK, 1)]}
    if doc["doc"] == "CreditNote":
        out = kit.credit_note(f, n, doc, 106, "Issued on the day after the returned pieces arrived back and were "
                                              "counted.",
                              [{"item": iid, "qty": q, "why": why} for iid, q, why in MARROW_BACK
                               if not ITEM[iid].get("free_with")],
                              {"BillingReference": {"InvoiceDocumentReference": {
                                  "ID": V(f.numbers["invoice"], "The invoice of the returned pieces."),
                                  "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                               "OrderReference": {"ID": V(f.numbers["order"], "The order of the pieces.")},
                               "AdditionalDocumentReference": {"ID": V(f.numbers["returns"], "The instruction for "
                                                                                             "returns.")},
                               "DueDate": V(f.date(116), "The furniture maker pays the credit back within ten "
                                                        "days."),
                               "Note": V("The store paid the invoice; the credit is refunded in full: the return "
                                         "ends the sale-or-return trial of the own-label agreement, so there is no "
                                         "restocking deduction. The free care kits came back with the benches and "
                                         "are not credited.", "Why money goes back, and how much.")})
        out["PaymentMeans"] = kit.payment_means(f, "26-xb", "37-xb", "26-xb", 106, 10, out["ID"].value,
                                                "The store's account, where the refund goes.")
        return out
    if doc["doc"] == "Order":
        out = kit.order(f, n, doc, 30, "The public works department furnishes its new planning office.",
                        "Delivered at place, the office: the furniture maker delivers and installs.",
                        "Lumeport Public Works Department, Civic Square", deal=DESKS, key="order-desks")
        out["AdditionalDocumentReference"] = {"ID": V(PWD_COMMITMENT, "The department's budget commitment for the "
                                                                      "purchase, which its rules ask the supplier to "
                                                                      "quote on the work report and the invoice.")}
        return out
    if doc["doc"] == "WorkReport":
        return {**collab(f, doc, "work-report", 38, "Reported when the installation was finished."),
                "WorkReportLine": {"ID": V("1", "The installation work."),
                                   "Quantity": qty(14, "HUR", "Two installers for seven hours, approved by the "
                                                              "department.")}}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 38, "Issued once the work report was approved.",
                           {"OrderReference": ref(f, "order-desks", "The department's order.")},
                           [{"item": "office-desk", "qty": 6, "invoice_why": "The desks delivered."},
                            {"item": "installation", "qty": 14, "invoice_why": "The hours of the approved work report.",
                             "line_extra": {
                                 "Note": V("Two installers, seven hours.", "The work billed."),
                                 "InvoicePeriod": {"StartDate": V(f.date(37), "The installation started."),
                                                   "EndDate": V(f.date(38), "And was finished.")},
                                 "WorkReportLineReference": {"LineID": V("1", "The line of the approved work "
                                                                              "report."),
                                                             "DocumentReference": {"ID": V(f.numbers["work-report"],
                                                                                           "The work report.")}}}}],
                           key="invoice-desks",
                           charges=[{"like": "installation", "amount": "24.00", "reason": "Packaging disposal", "code": "AEO", "code_why": "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services).",
                                     "why": "The installers took the desks' packaging away, as the work report "
                                            "records.", "amount_why": "The flat charge for disposal."}],
                           extra={"WorkReportDocumentReference": {"ID": V(f.numbers["work-report"], "The approved "
                                                                          "work report the hours come from.")},
                                  "ProjectReference": {"ID": V("PWD-PLAN-OFFICE-26", "The department's project: the "
                                                                                     "new planning office.")}})
    raise SystemExit(f"furniture scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the packaging flow (Bayvarra -> Urvania, and at home)
FILM = [{"item": "film-pe", "ordered": 480, "why": "Thirty rolls of 16 kg: wrapping for a month of bench pallets."}]
BAGS = [{"item": "garment-bag", "ordered": 20000, "why": "Forty boxes of 500 bags."}]
SHIRTS = [{"item": "shirt", "ordered": 600, "why": "The store's spring order of shirts."}]
PACKAGING = kit.Flow("packaging", "2026-04-27", FILM)


def packaging(n, doc):
    f = PACKAGING
    if doc["doc"] == "Order" and doc["from"] == "5-xu":
        return kit.order(f, n, doc, 0, "The manufacturer orders pallet film.",
                         "Free carrier at the packaging maker: the buyer books the road carrier that collects.",
                         "Rivermouth Packaging, dispatch, Lumeport")
    if doc["doc"] == "Invoice" and doc["to"] == "5-xu":
        return kit.invoice(f, n, doc, 4, "Issued when the film was collected, on Friday 1 May, a working day in "
                                         "Bayvarra (D27).",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "film-pe", "qty": 480, "invoice_why": "The kilograms collected."}])
    if doc["doc"] == "Order" and doc["from"] == "40-xb":
        return kit.order(f, n, doc, 2, "The textile mill orders garment bags.",
                         "Delivered at place, the mill: the packaging maker delivers.", "Lumeport Textile Mill, goods-in",
                         deal=BAGS, key="order-bags")
    if doc["doc"] == "Invoice" and doc["to"] == "40-xb":
        return kit.invoice(f, n, doc, 4, "Issued on delivery, on Friday 1 May.", {"OrderReference": ref(f, "order-bags",
                                                                                           "The mill's order.")},
                           [{"item": "garment-bag", "qty": 20000, "invoice_why": "The bags delivered."}],
                           key="invoice-bags")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 10, "The store orders shirts for spring.",
                         "Delivered duty paid at the store: the mill delivers and bears every cost.",
                         "Brightmarket Stores, goods-in, Lumeport", deal=SHIRTS, key="order-shirts")
    if doc["doc"] == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, 15, "The day the shirts left the mill.", "The gross weight of the "
                                  "cartons: the shirts in their bags and the cartons' share (world/items.json).",
                                  deal=SHIRTS, key="order-shirts")
        carton = ITEM["shirt"]["carton"]
        cartons = SHIRTS[0]["ordered"] // carton["per_carton"]
        assert cartons * carton["per_carton"] == SHIRTS[0]["ordered"], "the shirts fill whole cartons"
        carrier = next(x for x in WORLD["flows"] if x["id"] == f.id)["legs"][2]["carrier"]
        kind, kind_name = kit.waybill_kind(f, carrier)
        out["Shipment"]["Consignment"].update({
            # the carrier's consignment note, on which the note asks the store to record damage (packaging/06#F3)
            "CarrierAssignedID": V(f"{kit.initials(carrier)}-{kind}-26-{f.base:04d}", "The carrier's number for "
                                   f"the consignment: its consignment note, {kind_name[0].lower()}{kind_name[1:]}, "
                                   "which travels with the truck."),
            # what goods-in counts at the door (packaging/06#F8)
            "TotalPackagesQuantity": qty(cartons, "EA", f"{cartons} cartons of {carton['per_carton']} shirts. "
                                                        + carton["why"])})
        return out
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 15, "Issued on delivery.",
                           {"OrderReference": ref(f, "order-shirts", "The store's order.")},
                           [{"item": "shirt", "qty": 600, "invoice_why": "The shirts delivered."}], key="invoice-shirts")
    if doc["doc"] == "PurchaseReceipt":
        out = kit.purchase_receipt(f, n, doc, 25, "A consumer buys two shirts.",
                                   [{"item": "shirt-r", "qty": 2, "why": "Two shirts."}], cash=True)
        till(out, f, 25, "16:05:00", "C1", "Joss")
        return cash_payment(out, f, 25, "16:05:00", "70.00")
    raise SystemExit(f"packaging scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"tender": tender, "carnet": carnet, "waste": waste, "utilities": utilities, "wood": wood,
                  "furniture": furniture, "packaging": packaging})


# ================================================================ step 2: the document types the flows did not use yet
def nth(flow_id, n, doc):
    """Which occurrence of the same document type between the same parties this is, within the flow (1, 2, ...)."""
    same = [d for d in kit.WORLD["documents"] if d["flow"] == flow_id]
    return sum(1 for d in same[:n] if (d["doc"], d["from"], d["to"]) == (doc["doc"], doc["from"], doc["to"]))


def head(f, key, doc, day, why, doc_type=None):
    return {"ID": V(f.number(key, doc["from"], doc_type or doc["doc"]), "The sender's number for this document."),
            "IssueDate": V(f.date(day), why)}


def response(code, why, ref_id, ref_why):
    """A DocumentResponse: the response code and the document it is about."""
    return {"Response": {"ResponseCode": V(code, why)},
            "DocumentReference": {"ID": V(ref_id, ref_why)}}


_tender, _rail, _sea, _air, _retail, _road, _furniture, _carnet = tender, rail, sea, air, retail, road, furniture, carnet


def tender(n, doc):
    f, d = TENDER, doc["doc"]
    folder = {"ContractFolderID": V(FOLDER, "The authority's file number for this procurement, the same on every "
                                            "document of the procedure.")}
    if d == "ExpressionOfInterestRequest":
        return {**head(f, "eoi", doc, 33, "Sent after the contract notice was published."), **folder}
    if d == "ExpressionOfInterestResponse":
        return {**head(f, "eoi-response", doc, 34, "The authority confirms the registration the next day."), **folder}
    if d == "QualificationApplicationRequest":
        return {**head(f, "qar", doc, 32, "Sent with the procurement documents."), **folder}
    if d == "QualificationApplicationResponse":
        return {**head(f, "qar-response", doc, 38, "Returned before the tender deadline."), **folder,
                "TenderingCriterionResponse": {
                    "ID": V("SEL-1", "The response to the authority's first selection criterion."),
                    "Description": V("Annual turnover in furniture above 500,000 lume in each of the last three "
                                     "years.", "What the furniture maker declares for this criterion.")}}
    if d == "ProcurementStatusRequest":
        return {**head(f, "status-request", doc, 39, "The furniture maker asks a week before the deadline."), **folder}
    if d == "ProcurementStatus":
        return {**head(f, "procurement-status", doc, 40, "Answered the next day."), **folder,
                "TenderSubmissionDeadlinePeriod": {"EndDate": V(f.date(45), "The deadline for tenders stands."),
                                                   "EndTime": V("12:00:00", "At noon, as the notice says.")}}
    if d == "UnsubscribeFromProcedureRequest":
        return {**head(f, "unsubscribe", doc, 41, "The sawmill decides before the deadline."), **folder}
    if d == "UnsubscribeFromProcedureResponse":
        return {**head(f, "unsubscribe-response", doc, 42, "The authority confirms the next day."), **folder}
    if d == "TenderReceipt":
        return {**head(f, "tender-receipt", doc, 44, "Sent on receipt of the tender."), **folder,
                "RegisteredDate": V(f.date(44), "The day the tender was registered, before the deadline."),
                "RegisteredTime": V("11:42:00", "The time it was registered, which proves it was on time."),
                "TenderDocumentReference": {"ID": V(f.numbers["tender"], "The tender received.")}}
    if d == "Tender" and doc["from"] == "37-xb":
        k = nth("tender", n, doc)
        price = Decimal("470.00") if k == 1 else Decimal("480.00")
        return {"ID": V(f.number(f"tender-37-{k}", doc["from"], "Tender"), "The furniture maker's number for this "
                                                                           "tender."),
                "IssueDate": V(f.date(42 if k == 1 else 43), "Submitted before the deadline." if k == 1 else
                               "The corrected tender, submitted after the withdrawal the same day (tender/19#F1)."),
                **folder,
                "TenderedProject": {"LegalMonetaryTotal": {
                    "PayableAmount": amount(price * TENDER_QTY, "XBL",
                                            f"{TENDER_QTY} wooden benches at {price} lume" +
                                            (": the price per bench was entered wrongly." if k == 1 else
                                             ", the corrected price."))}}}
    if d == "TenderWithdrawal":
        return {**head(f, "withdrawal", doc, 43, "Withdrawn before the deadline, which the procedure allows."),
                "IssueTime": V("11:20:00", "In the morning, when the furniture maker noticed the wrong price, before "
                                           "it submitted the corrected tender (tender/18#F1)."),
                **folder,
                "WithdrawOfferIndicator": V("true", "The whole tender is withdrawn."),
                "TenderDocumentReference": {"ID": V(f.numbers["tender-37-1"], "The tender withdrawn.")}}
    if d == "TendererQualificationResponse":
        return {**head(f, "qualification-response", doc, 50, "After the check of the qualifications."), **folder,
                "QualificationResolution": {"AdmissionCode": V("ADMITTED", "The tenderer meets the selection criteria "
                                                                           "and its tender is evaluated."),
                                            "ResolutionDate": V(f.date(50), "The day of the decision.")}}
    if d == "UnawardedNotification":
        return {**head(f, "unawarded", doc, 56, "Told on the day of the award decision, as the winner is."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day the contract was awarded to another tenderer.")}}
    if d == "TenderContract":
        return {**head(f, "contract", doc, 66, "Concluded after the ten-day standstill period."), **folder,
                "TenderResult": {"AwardDate": V(f.date(56), "The day of the award decision.")}}
    return _tender(n, doc)


def rail(n, doc):
    f, d = RAIL, doc["doc"]
    # the train run asked about: the timetable service and the train itself (rail/04#F7)
    train = {"JourneyID": V("CT 4471", "The number of the container train in the hub's timetable."),
             "RailTransport": {"TrainID": V("FRC 4417", "The train itself, so that the run of this day is meant, not "
                                                        "the timetable service on other days (rail/04#F7).")}}
    if d == "TransportProgressStatusRequest":
        return {**head(f, "tps-request", doc, 8, "Asked on the morning of departure."),
                "IssueTime": V("06:30:00", "Before the timetabled departure: the carrier asks to be told when the "
                                           "train leaves (rail/04#F3)."), "TransportMeans": train}
    if d == "TransportProgressStatus":
        return {**head(f, "tps", doc, 8, "Answered the same morning."),
                "IssueTime": V("06:55:00", "Answered once the train has left, so that the status can report the "
                                           "actual departure (rail/05#F1)."),
                "TransportMeans": train}
    if d == "GoodsItemItinerary":
        def segment(k, why, mode, mode_why, service=None):
            seg = {"SequenceNumeric": V(str(k), why),
                   "TransportExecutionPlanReferenceID": V(f.numbers["tep"], "The plan the segment is carried out "
                                                                            "under."),
                   "TransportServiceProviderParty": party("14-xu", short=True),
                   "ReferencedConsignment": {"ID": V(f.numbers["consignment"], "The consignment on the segment.")},
                   "ShipmentStage": {"ID": V(str(k), mode_why),
                                     "TransportModeCode": V(mode, mode_why, listID="UNECE Recommendation 19 - Codes "
                                                                                   "for Modes of Transport")}}
            seg["TransportationService"] = {"TransportServiceCode": V(service, (
                "The container train service" if service == "RAILCONT" else "Carrier haulage: the rail carrier's own "
                "tractor brings the boxes to its terminal") + ", as a code of the Trade Accord's transport services.")}
            return seg
        return {**head(f, "itinerary", doc, 8, "Sent when the containers are on the train."),
                "IssueTime": V("09:00:00", "After loading."),
                "VersionID": V("1", "The first version of the itinerary."),
                "TransportExecutionPlanReferenceID": V(f.numbers["tep"], "The transport plan the itinerary belongs to."),
                # from takeover to delivery: the carrier's haulage to the hub, then the train (rail/09#F6)
                "TransportationSegment": [
                    segment(1, "The first segment: the carrier's tractor from the warehouse to the hub.", "3",
                            "The haulage, by road.", "CARRHAUL"),
                    segment(2, "The second segment: by rail from the hub to the distributor's siding.", "2",
                            "The rail stage.", "RAILCONT")]}
    return _rail(n, doc)


def sea(n, doc):
    f, d = SEA, doc["doc"]
    service = {"TransportServiceCode": V("OCEANCONT", "The service, as a code of the Trade Accord's transport services."),
               "Name": V("Weekly service Lumeport–Selanu", "The name of the service.")}
    if d == "BusinessCard":
        return head(f, "business-card", doc, 0, "Sent before the first offer to the new customer.")
    if d == "TransportServiceDescriptionRequest":
        return {**head(f, "tsd-request", doc, 4, "Asked once the order is accepted."),
                "IssueTime": V("14:00:00", "The time of the request."),
                "TransportationService": {"TransportServiceCode": V("OCEANCONT", "The service asked about: a "
                                                                                      "container liner service.")}}
    if d == "TransportServiceDescription":
        return {**head(f, "tsd", doc, 5, "The carrier answers the next day."), "TransportationService": {
            **service,
            "TariffClassCode": V("FAK", "Freight all kinds: one rate whatever the goods."),
            "Priority": V("Standard", "The normal service."),
            "FreightRateClassCode": V("BOX", "The rate is per container."),
            "TransportationServiceDescription": V(f"A weekly feeder sailing from Lumeport to Selanu, about "
                                                  f"{wmap.whole(SEA_HOURS)} hours at sea.",
                                                  "The service in words."),
            "TransportationServiceDetailsURI": V("https://www.tidewell.example/services/island", "Where the "
                                                                                                 "schedule is."),
            "NominationDate": V(f.date(5), "The day the service is offered for this shipment."),
            "NominationTime": V("10:00:00", "In the morning."),
            "SequenceNumeric": V("1", "The first of the services offered."),
            "SupportedTransportEquipment": [
                {"SizeTypeCode": V("22G1", "A 20-foot dry container, as an ISO 6346 size and type: the size type "
                                           "says what equipment is meant, so no identifier is given.")},
                {"SizeTypeCode": V("42G1", "A 40-foot dry container, as an ISO 6346 size and type.")}],
            "UnsupportedTransportEquipment": {"SizeTypeCode": V("45R1", "A 40-foot reefer, as an ISO 6346 size and "
                                                                        "type: the island port has no reefer plugs.")},
            "TransportEquipment": {"SizeTypeCode": V("42G1", "The equipment offered for this shipment: a 40-foot dry "
                                                             "container.")},
            "SupportedCommodityClassification": {"CargoTypeCode": V("GEN", "General cargo in containers.")},
            "UnsupportedCommodityClassification": {"CargoTypeCode": V("BULK", "No loose bulk on this service.")},
            "CommodityClassification": {"ItemClassificationCode": V("38111", "The benches, as a subclass of the UN Central Product Classification: seats with metal frames.")},
            "TotalCapacityDimension": {"AttributeID": V("TEU", "The ship's capacity in twenty-foot units."),
                                       "Measure": V("1000", "One thousand twenty-foot units (unit 20: twenty foot container).",
                                                    unitCode="20")},
            "ShipmentStage": {"ID": V("1", "Lumeport to Selanu."),
                              "TransportModeCode": V("1", "Maritime transport.", listID="UNECE Recommendation 19 - "
                                                                                        "Codes for Modes of "
                                                                                        "Transport")},
            "TransportEvent": kit.event(f, 10, SEA_SAILS + ":00", "The next departure from Lumeport.", done=False,
                                      location=kit.place("XBLMP", "The port the service sails from."),
                                      type_code="DEPARTURE"),
            "ResponsibleTransportServiceProviderParty": party("11-xb", short=True),
            "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2E", "Greenhouse gases."),
                                      "ValueMeasure": V("380", "Per 40-foot container on the crossing.",
                                                        unitCode="KGM")},
            "EstimatedDurationPeriod": {"DurationMeasure": V(str(wmap.whole(SEA_HOURS / 24)), f"Two days at sea: "
                                                             f"{wmap.nearest(SEA_KM, 10):,} km "
                                                             f"({wmap.nearest(SEA_KM / 1.852, 10)} nautical miles) "
                                                             f"at {wmap.KNOTS} knots, about "
                                                             f"{wmap.whole(SEA_HOURS)} hours.", unitCode="DAY")},
            "ScheduledServiceFrequency": {"WeekDayCode": V(str(datetime.date.fromisoformat(f.date(10)).isoweekday()),
                                                           f"Every {datetime.date.fromisoformat(f.date(10)):%A}, the "
                                                           "day of this sailing (ISO 8601 numbers the days from 1, "
                                                           "Monday).")}}}
    if d == "InvoiceStatusRequest":
        return {"ID": V(f.number("invoice-status-request", doc["from"], d), "The distributor's request number."),
                "RequestDate": V(f.date(25), "Two weeks after the invoice, without news from the buyer."),
                "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The invoice asked "
                                                                                                "about.")}}}
    if d == "InvoiceStatusResponse":
        return {**head(f, "invoice-status", doc, 26, "Answered the next day."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: accepted; the invoice is scheduled for "
                                                   "payment.", f.numbers["invoice"], "The invoice the status is about.")}
    return _sea(n, doc)


def air(n, doc):
    f, d = AIR, doc["doc"]
    if d == "FulfilmentCancellation":
        return {**head(f, "fulfilment-cancellation", doc, AIR_BOOKED[1], "On 13 May, the day of the missed flight."),
                "IssueTime": V("19:50:00", "In the evening, when the terminal reported the cargo accepted for the "
                                           "next morning's flight, before the new despatch advice it announces "
                                           "(air/07#F1, air/08#F1)."),
                "CancellationNote": V("The cargo reached the cargo terminal after the cut-off for the afternoon flight "
                                      "KXL209 of 13 May; it flies on KXL207 on the morning of 14 May under a new "
                                      "despatch advice.", "Why the despatch advice is cancelled: the flight and the "
                                                          "arrival it gave no longer hold (air/07#F2, F7)."),
                "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice cancelled.")}}
    if d == "DespatchAdvice" and nth("air", n, doc) == 2:
        out = kit.despatch_advice(f, n, doc, AIR_BOOKED[1], "Sent the same evening for the next morning's flight.",
                                  "The gross weight of the frame cartons and their skid.")
        out["ID"] = V(f.number("despatch-2", doc["from"], "DespatchAdvice"), "A new number: the first despatch "
                                                                             "advice was cancelled.")
        out["AdditionalDocumentReference"] = {
            "ID": V(f.numbers["despatch"], "The despatch advice this one replaces (air/08#F8)."),
            "DocumentDescription": V("Replaced: the frames missed KXL209 of 13 May and fly on KXL207 of 14 May.",
                                     "What changed.")}
        f.numbers["delivery-day"] = AIR_FLOWN[1]
        return air_despatch(f, out, AIR_FLOWN, "20:05:00", "Right after the cancellation.")
    return _air(n, doc)


def retail(n, doc):
    f, d = RETAIL, doc["doc"]
    cat = {"ID": V(f.numbers.get("catalogue", ""), "The catalogue concerned.")} if "catalogue" in f.numbers else None
    if d == "CatalogueRequest":
        return head(f, "catalogue-request", doc, 0, "The store asks for the spring catalogue. As UBL defines it, the "
                                                     "party that sends a catalogue request is its ProviderParty.")
    if d == "CataloguePricingUpdate":
        return {**head(f, "pricing-update", doc, 30, "The distributor lowers a price during the season."),
                "RelatedCatalogueReference": cat,
                "CataloguePricingUpdateLine": {"ID": V("1", "The line of the side frame."),
                                               "RequiredItemLocationQuantity": {"Price": {
                                                   "PriceAmount": price("58.00", "XBL", "The new price of the side "
                                                                                        "frame, down from 64.00."),
                                                   "BaseQuantity": qty(1, "EA", "Per piece (unit EA: each)."),
                                                   "PriceList": {
                                                       "ID": V("LD-PL-2026-2", "The new price list."),
                                                       "StatusCode": V("ACTIVE", "It is in force from today."),
                                                       "ValidityPeriod": {"StartDate": V(f.date(30), "From the "
                                                                                         "update."),
                                                                          "EndDate": V(f.date(90), "Until the "
                                                                                       "catalogue ends.")},
                                                       "PreviousPriceList": {
                                                           "ID": V("LD-PL-2026", "The price list of the spring "
                                                                                   "catalogue it replaces."),
                                                           "StatusCode": V("REPLACED", "No longer in force.")}}}}}}
    if d == "CatalogueItemSpecificationUpdate":
        it = item("bench-serra-b")     # the product, its GTIN and its price stay; the maker's datasheet is revised
        it["ItemSpecificationDocumentReference"] = {
            "ID": V("VI-DS-B180", "The maker's datasheet, the same document number in its revised issue."),
            "DocumentDescription": V("Revised: the slats are left untreated and turn silver-grey; only the end grain "
                                     "is sealed at the sawmill. Maintenance once a year: tighten the slat bolts, touch "
                                     "up the frame coating, clean the slats and check them for splits.",
                                     "What Valdara changed in the datasheet, as Lumeway passes it on: customers asked "
                                     "whether the slats need oil, as the Marrow furniture beside them does.")}
        it["AdditionalItemProperty"].insert(2, {
            "Name": V("Slat finish", "The property the revised datasheet adds."),
            "Value": V("Untreated, turning silver-grey; end grain sealed at the sawmill", "The thermally modified ash "
                                                                                          "needs no oil; only the end "
                                                                                          "grain is sealed against "
                                                                                          "splitting.")})
        return {**head(f, "spec-update", doc, 31, "Lumeway passes on Valdara's revised datasheet after the first weeks "
                                                  "of sales, when customers asked whether the slats need oil."),
                "RelatedCatalogueReference": cat,
                "CatalogueItemSpecificationUpdateLine": {"ID": V("1", "The line of the bench."), "Item": it}}
    if d == "CatalogueDeletion":
        return {**head(f, "catalogue-deletion", doc, 60, "The spring catalogue is withdrawn before the summer one."),
                "DeletedCatalogueReference": cat}
    if d == "DocumentStatusRequest":
        return {**head(f, "status-request", doc, 6, "Asked two days after ordering."),
                "RequestedDocumentReference": {"ID": V(f.numbers["order"], "The order asked about.")}}
    if d == "DocumentStatus":
        return {**head(f, "document-status", doc, 6, "Answered the same day."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: the order is accepted and the truck is "
                                                   "booked.", f.numbers["order"], "The order the status is about.")}
    if d == "TransportationStatusRequest":
        return {**head(f, "ts-request", doc, 9, "The store asks when to expect the delivery."),
                "Consignment": {"ID": V(f.numbers["consignment"], "The consignment asked about.")}}
    return _retail(n, doc)


def road(n, doc):
    f = ROAD
    if doc["doc"] == "ApplicationResponse":
        return {**head(f, "application-response", doc, 10, "Sent automatically when the invoice was matched: after "
                                                             "the corrected receipt advice of the same morning, the "
                                                             "receipt the match needs (road/16#F1)."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: the invoice is accepted.",
                                             f.numbers["invoice"], "The invoice responded to.")}
    return _road(n, doc)


def furniture(n, doc):
    f, d = FURNITURE, doc["doc"]
    if d == "Order" and doc["from"] == "26-xb" and nth("furniture", n, doc) == 2:
        return kit.order(f, n, doc, 94, "A repeat order for the winter, placed in the fourth week of sales, before "
                                        "the slow sales were clear.",
                         "Delivered at place, the store, as the first delivery.", "Brightmarket Stores, goods-in, "
                                                                                 "Lumeport", key="order-2",
                         deal=MARROW_REPEAT)
    if d == "OrderCancellation":
        return {**head(f, "order-cancellation", doc, 100, "Cancelled the day after the exception notification."),
                "CancellationNote": V("Sales of the line are below the agreed threshold; the second delivery is not "
                                      "needed.", "Why the order is cancelled."),
                "OrderReference": {"ID": V(f.numbers["order-2"], "The order cancelled.")}}
    if d == "DebitNote":
        rows = kit.spec_rows([{"item": "return-transport", "qty": 1}], "26-xb", "37-xb", "XBL")
        tax, total = kit.tax_total(rows, "XBL")
        amt = rows[0][2]
        out = {**head(f, "debit-note", doc, 107, "After the returned pieces were delivered back, the day after the "
                                                 "credit note."),
                "DebitNoteTypeCode": V("383", "UN/EDIFACT 1001 code 383: debit note."),
                "DefaultLanguageCode": V("en", "The language of the texts."),
                "LineCountNumeric": V("1", "One line."),
                "OrderReference": {"ID": V(f.numbers["order"], "The order of the pieces that went back.")},
                "PaymentTerms": {"Note": V("30 days net.", "The store's terms."),
                                 "PaymentDueDate": V(f.date(137), "The due date.")},
                "DueDate": V(f.date(137), "Thirty days, the store's terms."),
                "Note": V("The pieces went back at the maker's cost, as the own-label agreement says; the store "
                          "charges the transport.", "Why."),
                "DocumentCurrencyCode": kit.currency_line("XBL", "the currency of the trade"),
                **kit.cost_centre("26-xb", "The store books the income on its home and garden department."),
                "AdditionalDocumentReference": {"ID": V(f.numbers["returns"], "The instruction for returns that "
                                                                              "asked for the pieces.")},
                "DiscrepancyResponse": {"ResponseCode": V("35", "Why the store debits: the cost of a return "
                                                                        "the furniture maker asked for."),
                                        "Description": V("Return transport of seven benches, ten chairs and their "
                                                         "care kits.", "In words.")},
                "ContractDocumentReference": {"ID": V(OWN_LABEL, "The own-label agreement the line was bought under; "
                                                                 "it puts returns at the maker's cost.")},
                "Delivery": {"ActualDeliveryDate": V(f.date(105), "The pieces were delivered back."),
                             "DeliveryLocation": {**kit.gln_location("37-xb", "factory"),
                                                  "Name": V("Brackenmere Furniture, Marrowdale", "Where.")}},
                "PayeeParty": party("26-xb", short=True),
                "BuyerCustomerParty": {"Party": party("37-xb", short=True)},
                "SellerSupplierParty": {"Party": party("26-xb", short=True)},
                "BillingReference": {"CreditNoteDocumentReference": {"ID": V(next(v for k, v in f.numbers.items()
                                                                          if k.startswith("credit-")), "The credit note "
                                                                                                     "of the returned "
                                                                                                     "pieces.")}},
                "TaxTotal": total,
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, "XBL", "The sum of the lines."),
                                           "PayableAmount": amount(amt + tax, "XBL", "What the furniture maker owes "
                                                                                     "the store.")},
                "DebitNoteLine": {"ID": V("1", "The return transport."),
                                  "DebitedQuantity": qty(1, "E48", "One return delivery."),
                                  "LineExtensionAmount": amount(amt, "XBL", "The store's charge for one return delivery."),
                                  "Note": V("Collected with the store's van.", "How the pieces went back."),
                                  "DiscrepancyResponse": {"ResponseCode": V("35", "The return transport.")},
                                  **kit.cost_centre("26-xb", "The store's cost centre the income is booked on."),
                                  "PaymentPurposeCode": V("SCVE", "What the payment is for, as an ISO 20022 purpose: a service, the transport back."),
                                  "TaxInclusiveLineExtensionAmount": amount(amt + tax, "XBL", "The line with its "
                                                                                              "tax."),
                                  "TaxTotal": {"TaxAmount": amount(tax, "XBL", "The tax of the line.")},
                                  "DocumentReference": {"ID": V(f.numbers["returns"], "The instruction for "
                                                                                      "returns.")},
                                  "BillingReference": {"CreditNoteDocumentReference": {"ID": V(next(
                                      v for k, v in f.numbers.items() if k.startswith("credit-")), "The credit "
                                                                                                  "note.")},
                                                       "BillingReferenceLine": {"ID": V("1", "Its first line, the "
                                                                                             "returned oak benches.")}},
                                  "Delivery": {"ActualDeliveryDate": V(f.date(105), "The day the pieces were "
                                                                                   "delivered back to the furniture "
                                                                                   "maker.")},
                                  "Item": item("return-transport", kit.tax_category(rows[0][3])),
                                  "Price": kit.price_block("return-transport")}}
        out["PaymentMeans"] = kit.payment_means(f, "26-xb", "37-xb", "26-xb", 107, 30, out["ID"].value,
                                                "The store's account.")
        return out
    return _furniture(n, doc)


def carnet(n, doc):
    f, d = CARNET, doc["doc"]
    if d == "GoodsItemPassport":
        e = PARTY["5-xu"]["identity"]["employee"]
        src = "identity of Valdara Industries (world/parties.json)"
        out = _carnet(n, doc)
        out["RepresentativeParty"] = {"Person": {
            "ID": V(e["id"], f"The employee's staff number; {src}."),
            "FirstName": V(e["first"], f"The first name of the employee who travels with the samples; {src}."),
            "FamilyName": V(e["family"], f"Their family name; {src}."),
            "JobTitle": V(e["job"], f"Their job; {src}."),
            "NationalID": V(e["national_id"], "The national identity number, which customs may ask for at the border."),
            "BirthDate": V(e["birth_date"], "The birth date, as in the passport."),
            "BirthplaceName": V(e["birthplace"], "The place of birth, as in the passport."),
            "OrganizationDepartment": V(e["department"], f"The department the employee works in; {src}."),
            "CitizenshipCountry": {"IdentificationCode": V("XU", "The employee is a citizen of Urvania.")},
            "IdentityDocumentReference": {"ID": V(e["passport"], "The passport the employee travels on."),
                                          "DocumentType": V("Passport", "The kind of identity document.")}}}
        return out
    passport = {"GoodsItemPassportID": V(f.numbers.get("carnet", ""), "The carnet the samples travelled under.")}
    if d == "ProofOfReexportationRequest":
        return {**head(f, "por-request", doc, CARNET_DAYS["request"], "Friday 24 July: the re-exportation limit "
                     "of 30 June has passed, and the island's customs have no record that the samples left (D40)."),
                **passport}
    if d == "ProofOfReexportationReminder":
        return {**head(f, "por-reminder", doc, CARNET_DAYS["reminder"], "Monday 24 August, a month after the "
                     "request: no answer yet (D40; the Sunday a month later is no working day, D27)."),
                "ProcedureCode": V("2000", "The procedure the samples were under on the island."),
                **passport,
                "ProofOfReexportationRequestDocumentReference": {"ID": V(f.numbers["por-request"], "The request "
                                                                                                   "unanswered.")},
                "GoodsItemPassportCounterfoil": carnet_counterfoil(f, "IMP-1", True)}
    if d == "ProofOfReexportation":
        return {**head(f, "proof", doc, CARNET_DAYS["proof"], "Friday 28 August: Urvania's chamber answers with "
                                                              "the proof (D40)."),
                "GoodsItemPassportCounterfoil": [carnet_counterfoil(f, cid, True)
                                                 for cid in ("IMP-1", "REEXP-1", "REIMP-1")],
                "ReexportationEvidence": [
                    {"ID": V("EV-1", "The first evidence, under an ID of its own (carnet/04#F9)."),
                     "Description": V(f"The re-exportation counterfoil REEXP-1 of the carnet, stamped by the Island "
                                      f"Customs Service at Selanu airport on {carnet_day('reexport')}: the samples "
                                      "left the island. Its voucher never reached the importation office's "
                                      "records.", "What the evidence shows; the stamped counterfoil is in the "
                                                  "attached scan."),
                     "EvidenceIssuingParty": party("19-xl", short=True)},
                    {"ID": V("EV-2", "The second evidence."),
                     "Description": V(f"Urvania's customs re-imported the samples at Valico Euridice on "
                                      f"{carnet_day('reimport')}.", "What it shows: goods back in Urvania cannot "
                                                                    "still be on the island."),
                     "EvidenceIssuingParty": party("19-xu", short=True),
                     "DocumentReference": {"ID": V("XU-CUS-REIMP-26-0044", "Urvania's customs' record of the "
                                                                           "re-importation."),
                                           "IssueDate": V(f.date(CARNET_DAYS["reimport"]), "The day of the "
                                                                                           "re-importation.")}}]}
    return _carnet(n, doc)


SCENARIOS.update({"tender": tender, "rail": rail, "sea": sea, "air": air, "retail": retail, "road": road,
                  "furniture": furniture, "carnet": carnet})


# ================================================================ enrichments: what a document adds, by flow and type
ENRICH = {}


def enrich(flow_id, doc_type):
    """Register extra content for a flow's document type: fn(f, n, doc, out) returns a dict merged into the
    document (nested blocks are completed, not replaced)."""
    def deco(fn):
        ENRICH.setdefault((flow_id, doc_type), []).append(fn)
        return fn
    return deco


def _with_enrichment(flow_id, fn):
    def run(n, doc):
        out = fn(n, doc)
        for e in ENRICH.get((flow_id, doc["doc"]), []):
            kit.deep_merge(out, e(FLOWS[flow_id], n, doc, out) or {})
        return out
    return run


# The store's catalogue and its revisions (retail/02 to 04): version -> (day, time of the revision, what made it,
# the version before). A reference to the catalogue describes it as it stood when the referring document was issued:
# the version then current and its last revision, never a later one (retail/04#F1, #F8, O175, C72).
CATALOGUE_REVISIONS = {"1.0": (0, "09:00:00", "Not revised yet: its issue.", "0.9"),
                       "1.1": (30, "13:00:00", "Revised by the price update of the side frame.", "1.0"),
                       "1.2": (31, "08:30:00", "Revised by the specification update of the bench.", "1.1")}


def catalogue_ref(f, why, key="catalogue", version="1.0"):
    day, time, revised, previous = CATALOGUE_REVISIONS[version]
    return {"ID": V(f.numbers[key], why), "UUID": V(build_examples.referenced_uuid(f.id, f.numbers[key]),
                                                     "The catalogue's UUID, as stated in the catalogue."),
            "IssueDate": V(f.date(0), "Its issue date."),
            "IssueTime": V(CATALOGUE_REVISIONS["1.0"][1], "And time, as the catalogue states it."),
            "RevisionDate": V(f.date(day), revised),
            "RevisionTime": V(time, "At that time."),
            "Note": V("Spring catalogue 2026.", "Which catalogue."),
            "Description": V("Benches and spare parts for resale.", "What it holds."),
            "VersionID": V(version, "The version referred to: the one current when this document is issued."),
            "PreviousVersionID": V(previous, "The version before it." if previous != "0.9" else
                                   "The draft the store saw at the fair.")}


def related(iid, q, why):
    it = ITEM[iid]
    return {"ID": V(it["sellers_id"], f"The related item: {it['name']}."), "Quantity": qty(q, it["unit"], why),
            "Description": V(it["name"], "In words.")}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    lines = out["CatalogueLine"]
    bench, frame = lines[0], lines[1]
    common = {"ActionCode": V("ADD", "The line is new in this catalogue."),
              "LifeCycleStatusCode": V("ACTIVE", "The item is sold now."),
              "OrderableIndicator": V("true", "It can be ordered."),
              "SellerSupplierParty": {"Party": party("6-xb", short=True)},
              "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
              "LineValidityPeriod": {"StartDate": V(f.date(0), "From the issue."),
                                     "EndDate": V(f.date(90), "With the catalogue.")}}
    kit.deep_merge(bench, {**common,
                           "Note": V("Pallets of four only.", "How it is sold."),
                           "OrderableUnit": V("Pallet of 4", "The unit the store orders in."),
                           "ContentUnitQuantity": qty(4, "EA", "Four benches in an orderable unit."),
                           "OrderQuantityIncrementNumeric": V("4", "Orders go up in steps of four."),
                           "MinimumOrderQuantity": qty(4, "EA", "One pallet."),
                           "MaximumOrderQuantity": qty(192, "EA", "Two containers."),
                           "WarrantyInformation": V("Five years on the frame, from the maker.", "The warranty."),
                           "PackLevelCode": V("PALLET", "The pack level the line is for."),
                           "WarrantyParty": party("5-xu", short=True),
                           "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
                           "ItemComparison": {"PriceAmount": price("520.00", "XBL", "The price per bench."),
                                              "Quantity": qty(1, "EA", "For comparing per bench.")},
                           "ComponentRelatedItem": [related("slat-1800", 5, "Five slats per bench."),
                                                    related("bench-casting", 2, "Two side frames per bench.")],
                           "AccessoryRelatedItem": {"ID": V("VI-ANCHOR-4", "The ground anchor set."),
                                                    "Quantity": qty(1, "SET", "Supplied with each bench."),
                                                    "Description": V("Four ground anchors and bolts.", "In words.")},
                           "DocumentReference": {"ID": V("VI-DS-B180", "The maker's datasheet.")},
                           "KeywordItemProperty": {"Name": V("Keyword", "A search word of the catalogue."),
                                                   "Value": V("park bench", "The word.")}})
    kit.deep_merge(frame, {**common,
                           "Note": V("Spare part for the Serra 180.", "What it is for."),
                           "OrderableUnit": V("Box", "One frame per box."),
                           "MinimumOrderQuantity": qty(1, "EA", "Any quantity."),
                           "RequiredRelatedItem": related("bench-serra-b", 1, "Fits only the Serra 180."),
                           "ReplacedRelatedItem": {"ID": V("VI-C180", "The casting this one replaced, the same part "
                                                                         "number: Valdara tells its versions apart by "
                                                                         "the year (worklist C44, D35)."),
                                                   "Quantity": qty(1, "EA", "One for one."),
                                                   "Description": V("Side frame, 2025 casting", "Which version: the "
                                                                    "2025 casting, which the 2026 casting with "
                                                                    "the reinforced foot replaced.")}})
    return {"ActionCode": V("NEW", "A new catalogue."),
            "IssueTime": V(CATALOGUE_REVISIONS["1.0"][1], "Issued in the morning, for the store to set up the "
                                                          "range."),
            "RevisionDate": V(f.date(0), "Not revised yet: the issue date."),
            "RevisionTime": V(CATALOGUE_REVISIONS["1.0"][1], "The issue time."),
            "Note": V("Prices for trade customers, before sales tax.", "What the prices are."),
            "Description": V("Benches and spare parts for resale.", "What the catalogue holds."),
            "VersionID": V("1.0", "The first version."),
            "PreviousVersionID": V("0.9", "The draft the store saw at the fair."),
            "LineCountNumeric": V("2", "Two lines."),
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement with the store."),
                                   "ContractType": V("Supply agreement", "Its kind.")},
            "SourceCatalogueReference": {"ID": V("VI-CAT-2026", "The maker's catalogue the lines come from.")},
            "DocumentReference": {"ID": V("LD-GTC-2026", "The general terms of trade.")},
            "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V("XB", "Sold in Bayvarra.")}},
            "Signature": {"ID": V("LD-SIG-26-0420", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
            "TradingTerms": {"Information": V("Delivered duty paid to the store; 30 days net.", "The terms."),
                             "Reference": V("LD-GTC-2026", "Where they are."),
                             "ApplicableAddress": {"Country": {"IdentificationCode": V("XB", "In Bayvarra.")}}}}


@enrich("retail", "CatalogueRequest")
def _(f, n, doc, out):
    return {"Name": V("Spring catalogue 2026", "The catalogue asked for."),
            "Note": V("For the garden department.", "Who it is for."),
            "Description": V("Benches and spare parts.", "What the store wants to see."),
            "PricingUpdateRequestIndicator": V("true", "The store wants price updates during the season."),
            "ItemUpdateRequestIndicator": V("true", "And changes to the items."),
            "LineCountNumeric": V("2", "Two lines."),
            "ValidityPeriod": {"StartDate": V(f.date(0), "For the season."), "EndDate": V(f.date(90), "Its end.")},
            "Signature": {"ID": V("BM-SIG-26-0420", "The store's seal."), "SignatoryParty": party("26-xb",
                                                                                                short=True)},
            "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
            # no catalogue named: the store asks for a new one, which does not exist yet (retail/01#F1, D34, C73)
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement.")},
            "TradingTerms": {"Information": V("Delivered duty paid to the store.", "The terms the store expects.")},
            "DocumentReference": {"ID": V("BM-RANGE-26", "The store's range plan.")},
            "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V("XB", "For the store in Bayvarra.")}},
            "RequestedLanguage": {"ID": V("en", "English."), "Name": V("English", "In words."),
                                  "LocaleCode": V("en-XB", "Bayvarran English, the store's and the distributor's.")},
            "RequestedClassificationScheme": {"ID": V("HS", "Items classified by the Harmonized System."),
                                              "Name": V("Harmonized System", "In words."),
                                              "AgencyID": V("WCO", "The World Customs Organization."),
                                              "AgencyName": V("World Customs Organization", "In words."),
                                              "VersionID": V("2022", "The edition."),
                                              "URI": V("https://www.wcoomd.org", "Where it is published."),
                                              "LanguageID": V("en", "In English."),
                                              "ClassificationCategory": {"Name": V("Seats", "The heading the benches "
                                                                                           "fall in."),
                                                                         "CodeValue": V("9401", "HS heading 94.01.")}},
            "CatalogueRequestLine": [
                {"ID": V("1", "Benches."), "ContractSubdivision": V("Garden", "The part of the agreement."),
                 "Note": V("Pallet prices, please.", "What the store asks."),
                 "LineValidityPeriod": {"EndDate": V(f.date(90), "For the season.")},
                 "RequiredItemLocationQuantity": {"MinimumQuantity": qty(24, "EA", "The store's first order.")},
                 "Item": {"Name": V("Park bench Serra 180", "The item asked for.")}},
                {"ID": V("2", "Spare frames."),
                 "Item": {"Name": V("Bench side frame casting", "The item asked for.")}}]}


def catalogue_update_head(f, name, version):
    day, time, _, previous = CATALOGUE_REVISIONS[version]
    return {"Name": V(name, "What the update is."),
            "RevisionDate": V(f.date(day), "The day of the change."),
            "RevisionTime": V(time, "When the change was made, before the update was sent."),
            "Note": V("Applies to the spring catalogue.", "Which catalogue."),
            "Description": V(name, "In words."),
            "VersionID": V(version, "The catalogue version after the update."),
            "LineCountNumeric": V("1", "One line."),
            "ValidityPeriod": {"StartDate": V(f.date(day), "From the change."),
                               "EndDate": V(f.date(90), "Until the catalogue ends.")},
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement.")},
            "Signature": {"ID": V(f"LD-SIG-26-{version}", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
            "TradingTerms": {"Information": V("Unchanged.", "The terms stay as in the catalogue.")},
            "DefaultLanguage": {"ID": V("en", "English."), "Name": V("English", "In words.")},
            "RelatedCatalogueReference": catalogue_ref(f, "The catalogue updated.", version=previous)}


@enrich("retail", "CataloguePricingUpdate")
def _(f, n, doc, out):
    return {**catalogue_update_head(f, "Price change of the side frame", "1.1"),
            "CataloguePricingUpdateLine": {"ContractorCustomerParty": {"Party": party("26-xb", short=True)},
                                           "SellerSupplierParty": {"Party": party("6-xb", short=True)}}}


@enrich("retail", "CatalogueItemSpecificationUpdate")
def _(f, n, doc, out):
    return {**catalogue_update_head(f, "Revised datasheet of the Serra 180: slat finish and maintenance", "1.2"),
            "CatalogueItemSpecificationUpdateLine": {"ContractorCustomerParty": {"Party": party("26-xb",
                                                                                                short=True)},
                                                     "SellerSupplierParty": {"Party": party("6-xb", short=True)}}}


@enrich("retail", "CatalogueDeletion")
def _(f, n, doc, out):
    return {"Name": V("Withdrawal of the spring catalogue", "What it is."),
            "EffectiveDate": V(f.date(61), "From the next day."), "EffectiveTime": V("00:00:00", "From midnight."),
            "Note": V("Replaced by the summer catalogue.", "Why."), "VersionID": V("1.2", "The last version."),
            "Description": V("The spring catalogue is no longer valid.", "In words."),
            "ValidityPeriod": {"EndDate": V(f.date(60), "The last day it was valid.")},
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement.")},
            "Signature": {"ID": V("LD-SIG-26-0619", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
            "DeletedCatalogueReference": catalogue_ref(f, "The catalogue withdrawn.", version="1.2")}


@enrich("retail", "Forecast")
def _(f, n, doc, out):
    return {"Note": V("Includes the spring garden promotion.", "What the figure includes."),
            "VersionID": V("1", "The first forecast of the season."),
            "BasedOnConsensusIndicator": V("false", "The store's own figure, not yet agreed with the distributor."),
            "AdditionalDocumentReference": {"ID": V(f.numbers.get("event", "BM-RE-26"), "The promotion it counts "
                                                                                       "on.")},
            "Signature": {"ID": V("BM-SIG-26-0422", "The store's seal."),
                          "SignatoryParty": party("26-xb", short=True)},
            "ForecastLine": {"Note": V("Week-by-week figures follow in the store's portal.", "Where the detail is."),
                             "FrozenDocumentIndicator": V("false", "The figure may still change."),
                             "ForecastPeriod": {"StartDate": V(f.date(14), "The six weeks."),
                                                "EndDate": V(f.date(56), "Their end.")}}}


@enrich("retail", "RetailEvent")
def _(f, n, doc, out):
    bench = {"Name": V("Park bench Serra 180", "The item promoted."),
             "SellersItemIdentification": {"ID": V("LD-10442", "The distributor's number.")}}
    return {"Note": V("Agreed with the distributor's sales team.", "Status of the agreement."),
            "SellerEventID": V("LD-PROMO-26-03", "The distributor's number for the promotion."),
            "BuyerEventID": V("BM-SPRING-GARDEN-26", "The store's number."),
            # no "original" forecast: the event comes first and the forecast follows it (retail/06#F2, C73)
            "Signature": {"ID": V("BM-SIG-26-0422E", "The store's seal."),
                          "SignatoryParty": party("26-xb", short=True)},
            "EventComment": {"Comment": V("Shelf space for 12 benches at the entrance.", "What the store "
                                                                                          "prepares."),
                             "IssueDate": V(f.date(2), "Written with the announcement."),
                             "IssueTime": V("11:00:00", "At that time.")},
            "PromotionalEvent": {
                "PromotionalEventTypeCode": V("TPR", "A temporary price reduction."),
                "SubmissionDate": V(f.date(2), "Proposed now."),
                "FirstShipmentAvailabilityDate": V(f.date(9), "Stock can arrive from day 9."),
                "LatestProposalAcceptanceDate": V(f.date(6), "The distributor answers by day 6."),
                "PromotionalSpecification": {
                    "SpecificationID": V("BM-SPRING-GARDEN-26/1", "The first part of the promotion."),
                    "PromotionalEventLineItem": {
                        "Amount": amount(Decimal("74.90"), "XBL", "The price reduction per bench: 10 % of 749."),
                        "EventLineItem": {
                            "LineNumberNumeric": V("1", "The line."),
                            "ParticipatingLocationsLocation": {"Name": V("Brightmarket Stores, Lumeport", "The "
                                                                                                           "shop.")},
                            "RetailPlannedImpact": {"Amount": amount(Decimal("17976.00"), "XBL", "24 benches more "
                                                                     "at 749.00."),
                                                    "ForecastPurposeCode": V("SALES", "Planned extra sales."),
                                                    "ForecastTypeCode": V("TOTAL", "In total."),
                                                    "Period": {"StartDate": V(f.date(21), "The promotion."),
                                                               "EndDate": V(f.date(34), "Its end.")}},
                            "SupplyItem": bench}}}},
            "MiscellaneousEvent": {"MiscellaneousEventTypeCode": V("STOREOPEN", "Late opening on the first "
                                                                                   "Saturday."),
                                   "EventLineItem": {"LineNumberNumeric": V("1", "The line."),
                                                     "SupplyItem": bench}}}


@enrich("retail", "InventoryReport")
def _(f, n, doc, out):
    return {"Note": V("Counted on Thursday afternoon, before the report.", "When: at the end of the period the "
                                                                          "report covers (retail/07#F2)."),
            "DocumentCurrencyCode": kit.currency_line("XBL", "the store's currency"),
            "InventoryPeriod": {"StartDate": V(f.date(-4), "The week."), "EndDate": V(f.date(3), "Its end.")},
            "DocumentReference": {"ID": V(f.numbers.get("forecast", ""), "The forecast the stock is compared "
                                                                         "with.")},
            "Signature": {"ID": V("BM-SIG-26-0423", "The store's seal."),
                          "SignatoryParty": party("26-xb", short=True)},
            "InventoryReportLine": {"Note": V("Below the minimum of 6 before the promotion.", "Why it matters."),
                                    "InventoryValueAmount": amount(Decimal("1560.00"), "XBL", "Three at the "
                                                                                              "purchase price."),
                                    "AvailabilityDate": V(f.date(3), "Available now."),
                                    "AvailabilityStatusCode": V("AVAILABLE", "On the shelf."),
                                    "InventoryLocation": {"Name": V("Garden department, ground floor",
                                                                    "Where they stand.")}}}


FLOWS = {"ore": ORE, "road": ROAD, "rail": RAIL, "plastics": PLASTICS, "retail": RETAIL, "sea": SEA, "air": AIR,
         "cotton": COTTON, "tender": TENDER, "carnet": CARNET, "waste": WASTE, "utilities": UTILITIES, "wood": WOOD,
         "furniture": FURNITURE, "packaging": PACKAGING}
SCENARIOS = {k: _with_enrichment(k, v) for k, v in SCENARIOS.items()}


def seal(pid, no, why="The sender's electronic seal."):
    return {"ID": V(no, why), "SignatoryParty": party(pid, short=True)}


@enrich("furniture", "ItemInformationRequest")
def _(f, n, doc, out):
    return {"Note": V("Weekly figures, please, for the whole season.", "What the maker asks."),
            "DocumentReference": {"ID": V(f.numbers["quotation"], "The quotation of the line.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0312"),
            "ItemInformationRequestLine": {"TimeFrequencyCode": V("WEEKLY", "Figures per week."),
                                           "SupplyChainActivityTypeCode": V("SALES", "Sales to consumers."),
                                           "ForecastTypeCode": V("TOTAL", "Total quantities."),
                                           "PerformanceMetricTypeCode": V("SALESUNITS", "Measured in pieces sold.")}}


@enrich("furniture", "TradeItemLocationProfile")
def _(f, n, doc, out):
    return {"Note": V("The store holds stock; the maker replenishes.", "Who does what."),
            "ProfileStatusCode": V("ACTIVE", "In force."),
            "DocumentReference": {"ID": V(f.numbers["quotation"], "The quotation the line is bought under.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0313")}


@enrich("furniture", "ExceptionCriteria")
def _(f, n, doc, out):
    return {"Note": V("Both sides are told when a criterion is met.", "How the criteria are used."),
            "VersionID": V("1", "The first version."),
            "DocumentReference": {"ID": V(f.numbers["location-profile"], "The replenishment policy they go "
                                                                         "with.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0313C"),
            "ExceptionCriteriaLine": [
                *({**ln,
                 "Note": V("Slow sales.", "What the criterion catches."),
                 "ExceptionStatusCode": V("ACTIVE", "In force."),
                 "CollaborationPriorityCode": V("HIGH", "Answered within two days."),
                 "ExceptionResolutionCode": V("REVIEW", "The partners review the line together."),
                 "SupplyChainActivityTypeCode": V("SALES", "Measured on sales."),
                 "PerformanceMetricTypeCode": V("SALESUNITS", "In benches sold."),
                 "EffectivePeriod": {"StartDate": V(f.date(70), "From the first day of sales, the reopening of "
                                                                "the home and garden department: the first four "
                                                                "weeks are measured from it."),
                                     "EndDate": V(f.date(180), "To the end of the season.")}}
                  for ln in out["ExceptionCriteriaLine"]),
                {"ID": V(str(len(out["ExceptionCriteriaLine"]) + 1), "The forecast criterion."),
                 "Note": V("Forecast far from the store's own plan.", "What it catches."),
                 "ThresholdValueComparisonCode": V("GT", "When the difference is larger."),
                 "ThresholdQuantity": qty(30, "P1", "More than 30 % difference."),
                 "SupplyItem": marrow_items("bench") + marrow_items("chair"),
                 "ForecastExceptionCriterionLine": {"ForecastPurposeCode": V("SALES", "A sales forecast."),
                                                    "ForecastTypeCode": V("TOTAL", "In total."),
                                                    "ComparisonDataSourceCode": V("BUYER", "Compared with the "
                                                                                           "store's plan."),
                                                    "DataSourceCode": V("SELLER", "The maker's forecast."),
                                                    "TimeDeltaDaysQuantity": qty(28, "DAY", "Over four weeks.")}}]}


@enrich("furniture", "ProductActivity")
def _(f, n, doc, out):
    return {"Note": V("The chairs sell better than the set: the bench is too long for many apartment kitchens.",
                      "The store's remark."),
            "DocumentReference": {"ID": V(f.numbers["info-request"], "The request the figures answer.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0608A"),
            "SupplyChainActivityDataLine": {
                "ActivityPeriod": {"StartDate": V(f.date(70), "The four weeks since the reopening."),
                                   "EndDate": V(f.date(97), "Their end.")}}}


@enrich("furniture", "ExceptionNotification")
def _(f, n, doc, out):
    words = {1: "one", 2: "two", 3: "three"}
    for w, ln in zip(WOODS, out["ExceptionNotificationLine"]):
        sold, limit = MARROW_SOLD["bench"][w], MARROW_THRESHOLD[w]
        kit.deep_merge(ln, {
                "Note": V(f"{words[sold].capitalize()} {w} bench{'es' if sold > 1 else ''} sold against a threshold "
                          f"of {words[limit]}; three benches against five for the line.", "The exception."),
                "Description": V("Sales below the agreed threshold.", "In words."),
                "ExceptionStatusCode": V("OPEN", "Not yet resolved."),
                "CollaborationPriorityCode": V("HIGH", "As agreed."),
                "ResolutionCode": V("REVIEW", "A review of the line."),
                "VarianceQuantity": qty(sold - limit, "EA", f"{words[limit - sold].capitalize()} {w} "
                                                            f"bench{'es' if limit - sold > 1 else ''} fewer than the "
                                                            "threshold."),
                "SupplyChainActivityTypeCode": V("SALES", "Measured on sales."),
                "PerformanceMetricTypeCode": V("SALESUNITS", "In benches sold."),
                "DocumentReference": {"ID": V(f.numbers["activity"], "The product activity reported.")},
                "ForecastException": {"ForecastPurposeCode": V("SALES", "The sales forecast compared."),
                                      "ForecastTypeCode": V("TOTAL", "In total."),
                                      "IssueDate": V(f.date(14), "The forecast of the first delivery."),
                                      "IssueTime": V("10:00:00", "Its time."),
                                      "DataSourceCode": V("SELLER", "The maker's forecast."),
                                      "ComparisonDataCode": V("ACTUAL", "Compared with actual sales."),
                                      "ComparisonForecastIssueDate": V(f.date(98), "The store's figures of 8 "
                                                                                   "June."),
                                      "ComparisonForecastIssueTime": V("18:00:00", "Their time.")}})
    return {"Note": V("Please review the line with us.", "What the maker proposes."),
            "DocumentReference": {"ID": V(f.numbers["exception-criteria"], "The criteria that were met.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0609")}


@enrich("cotton", "Forecast")
def _(f, n, doc, out):
    return {"Note": V("Depends on clothing orders from the store.", "What the forecast rests on."),
            "VersionID": V("1", "The first forecast of the season."),
            "BasedOnConsensusIndicator": V("true", "Agreed with the ginnery at the season meeting."),
            "AdditionalDocumentReference": {"ID": V("SCG-SEASON-2026", "The season agreement.")},
            "Signature": seal(doc["from"], "LT-SIG-26-0202")}


@enrich("cotton", "ForecastRevision")
def _(f, n, doc, out):
    return {"Note": V("Demand for clothing has risen.", "Why the forecast is revised."),
            "RevisionStatusCode": V("REVISED", "A revised forecast."),
            "PurposeCode": V("ORDER", "Of what the mill will order."),
            "OriginalDocumentReference": {"ID": V(f.numbers["forecast"], "The forecast revised.")},
            "Signature": seal(doc["from"], "LT-SIG-26-0222"),
            "ForecastRevisionLine": {"Note": V("Twenty per cent more.", "The change."),
                                     "Description": V("More bales from the second half of the season.", "In words."),
                                     "AdjustmentReasonCode": V("DEMAND", "Higher demand."),
                                     "ForecastPeriod": {"StartDate": V(f.date(60), "From mid-season."),
                                                        "EndDate": V(f.date(120), "To the end.")}}}


@enrich("furniture", "InstructionForReturns")
def _(f, n, doc, out):
    gross = sum(Decimal(str(ITEM[iid]["gross_kg"])) * q for iid, q, _ in MARROW_BACK)
    return {"Note": V("The sale-or-return trial of the own-label agreement, the first four weeks of sales from the "
                      "reopening of the home and garden department on 11 May, ended on Sunday 7 June: the stock "
                      "above the target goes back at the maker's cost. The store's van brings it; the maker pays the "
                      "transport.", "Why the goods go back, and at whose cost."),
            "DocumentReference": {"ID": V(OWN_LABEL, "The own-label agreement, whose sale-or-return terms the return "
                                                     "follows.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0611"),
            "Shipment": {"ID": V("BM-RET-26-0611", "The return shipment."),
                         "GrossWeightMeasure": qty(gross, "KGM", "Seven benches of 24 kg, ten chairs of 11.5 kg and "
                                                                 "seven care kits of 0.35 kg, packed."),
                         "Delivery": {"RequestedDeliveryPeriod": {"StartDate": V(f.date(102), "The store's van "
                                                                                              "brings them."),
                                                                  "EndDate": V(f.date(105), "By the Monday after.")}}}}


@enrich("furniture", "ExceptionNotification")
def _(f, n, doc, out):
    for ln in out["ExceptionNotificationLine"]:
        ln["ExceptionObservationPeriod"] = {"StartDate": V(f.date(70), "The four weeks since the reopening."),
                                            "EndDate": V(f.date(97), "Their end.")}
    return {}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    return {"CatalogueLine": [{**out["CatalogueLine"][0], "ContractSubdivision": V("Garden", "The part of the supply "
                                                                                             "agreement the line "
                                                                                             "falls under.")},
                              out["CatalogueLine"][1]]}


STATUS_INSTRUCTION = {     # the slot a cargo terminal's status is about (air/05#F6, 09#F6)
    ("air", "17-xb"): "The built-up skid goes to the aircraft for KXL207 on 14 May between 06:00 and 06:20; reply "
                      "only if that slot must change.",
    ("air", "17-xl"): "The skid is ready for collection by Nalevi Warehousing from 12:00 on 14 May, after customs "
                      "clearance; reply only if that slot must change."}


def status_extras(f, n, doc, out):
    """What every transportation status report adds: what it is, the plan it reports on, where and when."""
    x = {"Name": V("Transportation status", "The kind of report."),
         "Description": V(out["TransportEvent"]["Description"].value if isinstance(out.get("TransportEvent"), dict)
                          and "Description" in out["TransportEvent"] else "Status of the consignment.", "In words."),
         "Note": V("Automatic report from the sender's tracking system.", "How it was made."),
         **({"ShippingOrderID": V(kit.shipping_order(f), "The forwarding instructions of the shipment it "
                                                          "reports on.")} if kit.shipping_order(f) else {}),
         "OtherInstruction": V(STATUS_INSTRUCTION.get((f.id, doc["from"]), "Reply only if the delivery slot "
                                                                             "must change."),
                               "What the receiver should do, with the slot it is about."),
         "TransportExecutionStatusCode": V("INPROGRESS", "The carriage is under way."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TS-{n:02d}"),
         "StatusLocation": (out["TransportEvent"]["Location"] if isinstance(out.get("TransportEvent"), dict) and
                            "Location" in out["TransportEvent"] else
                            {"Name": V(PARTY[doc["from"]]["identity"]["name"], "Where the status was recorded.")}),
         "StatusPeriod": {"StartDate": V(out["IssueDate"].value, "The status holds from the report."),
                          "EndDate": V(out["IssueDate"].value, "Until the next report.")}}
    if f.numbers.get("waybill", f.numbers.get("bl")):   # only a transport document issued already (C06, C72)
        x["DocumentReference"] = {"ID": V(f.numbers.get("waybill", f.numbers.get("bl")),
                                          "The transport document of the consignment.")}
    if "tep" in f.numbers:
        x["TransportExecutionPlanDocumentReference"] = {"ID": V(f.numbers["tep"], "The plan the carriage follows.")}
    if "ts-request" in f.numbers:
        x["TransportationStatusRequestDocumentReference"] = {"ID": V(f.numbers["ts-request"], "The request "
                                                                                              "answered.")}
    if f.id == "road":
        x["UpdatedDeliveryTransportEvent"] = kit.event(f, 9, "09:30:00", "The delivery as now expected.",
                                                       location=LUMEWAY_GOODS_IN)
        x["UpdatedPickupTransportEvent"] = kit.event(f, 7, "15:05:00", "The collection as it happened.",
                                                     location=RAIL_WAREHOUSE)
    return x


for _fid in ("road", "rail", "sea", "air"):
    enrich(_fid, "TransportationStatus")(status_extras)


@enrich("retail", "TransportationStatusRequest")
def _(f, n, doc, out):
    return {"CarrierAssignedID": V(f.numbers.get("waybill", ""), "The carrier's consignment note."),
            "Name": V("Status request", "What it is."),
            "Description": V("When will the benches arrive?", "The question."),
            "Note": V("The promotion starts soon.", "Why the store asks."),
            **({"ShippingOrderID": V(kit.shipping_order(f), "The forwarding instructions of the shipment asked "
                                                             "about.")} if kit.shipping_order(f) else {}),
            "OtherInstruction": V("Answer with the expected delivery time.", "What the answer should hold."),
            "TransportationStatusTypeCode": V("DELIVERY", "The status of the delivery is asked."),
            "DocumentReference": {"ID": V(f.numbers["order"], "The store's order.")},
            "Signature": seal(doc["from"], "LD-SIG-26-TSR"),
            "RequestedStatusLocation": {"Name": V("Brightmarket Stores, goods-in", "Status at the store.")},
            "RequestedStatusPeriod": {"StartDate": V(f.date(9), "For today."), "EndDate": V(f.date(10), "And "
                                                                                                       "tomorrow.")}}


@enrich("rail", "TransportProgressStatusRequest")
def _(f, n, doc, out):
    return {"Note": V("Please report the departure of the container train FRC 4417 from Ferrano.", "The request: the "
                                                                                                  "departure, not "
                                                                                                  "presumed (rail/04#F3)."),
            "Signature": seal(doc["from"], "FRC-SIG-TPSR"),
            "StatusLocation": {"Name": V("Ferrano Intermodal Hub", "Where the status is asked for: the train's "
                                                                   "departure point.")}}


@enrich("rail", "TransportProgressStatus")
def _(f, n, doc, out):
    # Urvania's rail infrastructure manager reports the train on its own network, from the hub to the border
    # station; the run beyond the border is on Bayvarra's tracks (D37, rail/05#F2, F4)
    late = 7
    return {"Note": V(f"Left at {RAIL_LEAVES}, {late} minutes after the timetable.", "The answer, as the times say "
                                                                                     "it (rail/05#F5)."),
            "StatusAvailableIndicator": V("true", "A status is available."),
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TPS"),
            "TransportProgressStatusRequestDocumentReference": {"ID": V(f.numbers["tps-request"], "The request "
                                                                                                  "answered.")},
            "TransportSchedule": [
                {"SequenceNumeric": V("1", "The first point: the hub, where the train starts."),
                 "ReferenceDate": V(f.date(8), "The day."), "ReferenceTime": V("06:45:00", "The timetabled "
                                                                                           "departure the status "
                                                                                           "refers to."),
                 "ReliabilityPercent": V("95", "How sure the schedule is."),
                 "Remarks": V(f"Left {late} minutes late, two after the estimate.", "The status at the hub."),
                 "StatusLocation": RAIL_HUB,
                 "PlannedDepartureTransportEvent": kit.event(f, 8, "06:45:00", "The timetable.", location=RAIL_HUB),
                 "ActualDepartureTransportEvent": kit.event(f, 8, RAIL_LEAVES + ":00", "The departure.",
                                                            location=RAIL_HUB),
                 "EstimatedDepartureTransportEvent": kit.event(f, 8, "06:50:00", "As expected that morning.",
                                                               location=RAIL_HUB),
                 "ActualArrivalTransportEvent": kit.event(f, 8, "05:30:00", "The train arrived at the hub for "
                                                                            "loading.", location=RAIL_HUB)},
                {"SequenceNumeric": V("2", "The second point: the border station, the end of Urvania's network."),
                 "Remarks": V("The path into Bayvarra at 13:00 holds.", "The status ahead."),
                 "StatusLocation": RAIL_BORDER,
                 "PlannedArrivalTransportEvent": kit.event(f, 8, wmap.hm(RAIL_AT_BORDER_PLANNED), "The timetable: "
                                                           f"{wmap.whole(RAIL_BORDER_KM)} km from the hub.",
                                                           location=RAIL_BORDER),
                 "EstimatedArrivalTransportEvent": kit.event(f, 8, wmap.hm(RAIL_AT_BORDER), "Expected from the "
                                                             "actual departure.", location=RAIL_BORDER),
                 "PlannedDepartureTransportEvent": kit.event(f, 8, RAIL_BORDER_LEAVES + ":00", "The timetabled "
                                                             "path into Bayvarra, after the crew change, the brake "
                                                             "test and the customs' check of the seals.",
                                                             location=RAIL_BORDER)}]}


@enrich("rail", "GoodsItemItinerary")
def _(f, n, doc, out):
    return {"Note": V("The itinerary of the two containers.", "What it shows."),
            "Signature": seal(doc["from"], "FRC-SIG-GII"),
            "ReferencedConsignment": {"ID": V(f.numbers["consignment"], "The consignment.")},
            "ReferencedTransportEquipment": [{"ID": V(RAIL_BOXES[k], f"The {('first', 'second')[k]} container "
                                                                     "(rail/09#F1).", schemeID="ISO6346")}
                                             for k in range(2)],
            "ReferencedPackage": {"ID": kit.unit_id("8-xu", f, 1, "The first pallet in it, made up by the 3PL")},
            "ReferencedGoodsItem": {"ID": V("1", "The benches.")}}


@enrich("sea", "TransportServiceDescriptionRequest")
def _(f, n, doc, out):
    return {"Note": V("Weekly sailings to Selanu, please.", "What the distributor asks."),
            "ServiceInformationPreferenceCode": V("SCHEDULE", "It wants the schedule first."),
            "Signature": seal(doc["from"], "LD-SIG-TSDR"),
            "TransportServiceProviderParty": party("11-xb", short=True)}


@enrich("sea", "TransportServiceDescription")
def _(f, n, doc, out):
    return {"Note": V("Our island service.", "What follows."), "ServiceName": V("Island feeder", "The service's "
                                                                                                "name."),
            "ResponseCode": V("OFFERED", "The service is offered."),
            "Signature": seal(doc["from"], "TWL-SIG-TSD"),
            "TransportServiceDescriptionRequestDocumentReference": {"ID": V(f.numbers["tsd-request"], "The request "
                                                                                                      "answered.")},
            "ServiceChargePaymentTerms": {"Note": V("Freight prepaid before the bill of lading is released.",
                                                    "When the freight is paid.")},
            "ValidityPeriod": {"StartDate": V(f.date(5), "From now."), "EndDate": V(f.date(95), "For three "
                                                                                              "months.")}}


def fi_extras(f, n, doc, out):
    carrier_booking = doc["to"] == "11-xb"
    x = {"Name": V("Forwarding instructions", "What they are."),
         "Description": V("Instructions for the shipment to the island." if f.id != "cotton" else
                          "Instructions for the bales to Bayvarra.", "In words."),
         "Note": V("Please confirm the booking.", "What the sender expects."),
         "ToOrderIndicator": V("true" if f.id == "sea" else "false", "A bill of lading to order, so the buyer can "
                                                                     "transfer it." if f.id == "sea" else
                               "A straight bill: the consignee is named."),
         **({"OtherInstruction": V("Send the bill of lading to the forwarder.", "Where the documents go.")}
            if f.id in ("sea", "cotton") else {}),
         "DocumentReference": {"ID": V(f.numbers.get("order", ""), "The order the goods are for.")},
         "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The freight's currency."),
                          "TargetCurrencyCode": V("XLC", "The island's currency."),
                          "CalculationRate": V("0.4", "The reference rate.")},
         "DocumentDistribution": {"ID": V("1", "The instructions to the forwarder."),
                                  "DocumentTypeCode": V("ForwardingInstructions", "The document distributed: these "
                                                                                  "instructions."),
                                  "DistributionTypeCode": V("ELECTRONIC", "Sent as this UBL document."),
                                  "Party": party(doc["to"], short=True)},
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-FI-{n:02d}")}
    if carrier_booking:
        x["CarrierAssignedID"] = V(SEA_BOOKING, "The booking number the carrier gave.")
    return x


for _fid in ("sea", "air", "cotton"):
    enrich(_fid, "ForwardingInstructions")(fi_extras)


def bl_extras(f, n, doc, out):
    return {"Name": V("Bill of lading", "What it is."),
            "Description": V("Shipped on board.", "The kind of bill."),
            "Note": V("Freight prepaid." if f.id == "sea" else "Freight collect.", "Who has paid the freight."),
            "DocumentStatusCode": V("Confirmed", "Issued."),
            "DocumentReference": {"ID": V(f.numbers.get("instructions-carrier", f.numbers.get("instructions", "")),
                                          "The forwarding instructions it was issued on.")},
            "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The freight's currency."),
                             "TargetCurrencyCode": V("XLC", "The island's currency."),
                             "CalculationRate": V("0.4", "The reference rate.")},
            "DocumentDistribution": bl_distribution(f, doc),
            "Signature": seal(doc["from"], f"TWL-SIG-BL-{f.id}", "The master's signature, by the carrier's agent.")}


def bl_distribution(f, doc):
    """Where the bill of lading goes: the originals, a document of title, on paper by courier to the party that
    holds them until the goods are paid for; a scanned copy to the party that needs to know about the cargo."""
    bl = {"DocumentTypeCode": V("BillOfLading", "The document distributed: this bill of lading.")}
    if f.id == "sea":
        return [{"ID": V("1", "The full set of three originals."), **bl,
                 "DistributionTypeCode": V("ORIGINALCOURIER", "The originals go by courier to the forwarder, the "
                                                              "shipper's agent; the buyer gets them, endorsed, "
                                                              "against payment."),
                 "Party": party(doc["to"], short=True)},
                {"ID": V("2", "The notify party's copy."), **bl,
                 "DistributionTypeCode": V("SCANNEDCOPY", "A scanned copy for the notify party, which arranges the "
                                                          "on-carriage at Selanu; a copy gives no title to the goods."),
                 "Party": party("9-xl", short=True)}]
    return [{"ID": V("1", "The full set of three originals."), **bl,
             "DistributionTypeCode": V("ORIGINALCOURIER", "The originals go by courier to the Bank of Selanu, which "
                                                          "holds a mortgage on the bales and releases the bills when "
                                                          "the mill has paid."),
             "Party": party("22-xl", short=True)},
            {"ID": V("2", "The consignee's copy."), **bl,
             "DistributionTypeCode": V("SCANNEDCOPY", "A scanned copy for the mill, so it can plan the collection "
                                                      "of the bales."),
             "Party": party("40-xb", short=True)}]


for _fid in ("sea", "cotton"):
    enrich(_fid, "BillOfLading")(bl_extras)


@enrich("sea", "Manifest")
def _(f, n, doc, out):
    return {"ManifestType": V("Cargo manifest", "In words."), "Description": V("Cargo for Selanu.", "What it "
                                                                                                     "lists."),
            "Note": V("One container for Selanu.", "The cargo."), "VersionID": V("1", "The first version."),
            "PassengerPerson": kit.person("Ines", "Tavari", "The one passenger: a supercargo travelling with the "
                                                            "cargo.", role="PASSENGER"),
            "DocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading of the container.")},
            "DocumentDistribution": {"ID": V("1", "To customs."),
                                     "DocumentTypeCode": V("Manifest", "The document distributed: this manifest."),
                                     "DistributionTypeCode": V("ELECTRONIC", "By message."),
                                     "Party": party("19-xl", short=True)},
            "Signature": seal(doc["from"], "TWL-SIG-MF", "The master's signature.")}


@enrich("sea", "PackingList")
def _(f, n, doc, out):
    return {"Name": V("Packing list", "What it is."), "Description": V("The container's contents.", "In words."),
            "Note": V(f"{len(kit.pallets(f, f.deal))} pallets.", "The count."), "VersionID": V("1", "The first version."),
            "OtherInstruction": V("Keep with the container's documents.", "Where it goes."),
            "CarrierParty": party("11-xb", short=True),
            "DocumentReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
            "DocumentDistribution": {"ID": V("1", "To the forwarder."),
                                     "DocumentTypeCode": V("PackingList", "The document distributed: this packing "
                                                                          "list."),
                                     "DistributionTypeCode": V("ELECTRONICCOPY", "A copy for the forwarder, who "
                                                                                 "keeps it with the container's "
                                                                                 "documents."),
                                     "Party": party("10-xb", short=True)},
            "Signature": seal(doc["from"], "LD-SIG-PL")}


@enrich("sea", "CommonTransportationReport")
def _(f, n, doc, out):
    return {"ReportTypeCode": V("PREARRIVAL", "The report before entering the port."),
            "ReportType": V("Pre-arrival report", "In words."),
            "Description": V("The ship's report before arrival at Selanu.", "What it is."),
            "Note": V("Pilot requested at the Selanu fairway buoy at first light; the ship waits off the port under "
                      "way overnight and berths without anchoring.",
                      "The master's note on the arrival."), "VersionID": V("1", "The first version."),
            "ReportingLocation": {"Name": V(f"At sea, {sea_report_nm(f)} nautical miles off Selanu",
                                            "Where the report was made: the ship's distance to go at the time of "
                                            "the report.")},
            "TransportMeans": kit.means("11-xb", "TH", "TH-26-19E", "The voyage.", "EB"),
            "DocumentReference": {"ID": V(f.numbers["manifest"], "The cargo manifest.")},
            "Signature": seal(doc["from"], "TWL-SIG-CTR", "The master's signature.")}


def cotton_bale_count(f, n, doc, out):
    """The bales are the shipment's packages (D12, O26): every document that describes the consignment gives their
    number; the goods item says they are bales, and the weight statement lists each bale with its weight."""
    why = {"ForwardingInstructions": "The bales the forwarder is to book, in one container.",
           "GoodsCertificate": "The bales the certificate covers: a plant health certificate states the number of "
                               "packages.",
           "ExportCustomsDeclaration": "The number of packages declared for export: the bales.",
           "BillOfLading": "The bales the carrier received in the container, as the bill of lading counts them.",
           "ImportCustomsDeclaration": "The number of packages declared for import: the bales."}[doc["doc"]]
    count = kit.package_count(f, why)
    cons = next(iter(find_dicts(out, "Consignment")), None)
    if cons is None:
        out["Shipment"]["Consignment"] = {"ID": V(f.numbers["consignment"], "The consignment, as the mill's "
                                                                            "forwarding instructions number it.")}
        cons = out["Shipment"]
    for c in lines_of(cons, "Consignment"):
        c["TotalPackagesQuantity"] = count
    return {}


for _doc in ("ForwardingInstructions", "GoodsCertificate", "ExportCustomsDeclaration", "BillOfLading",
             "ImportCustomsDeclaration"):
    enrich("cotton", _doc)(cotton_bale_count)


@enrich("cotton", "WeightStatement")
def _(f, n, doc, out):
    return {"WeightStatementTypeCode": V("VGM", "A statement of the verified gross mass."),
            "Signature": seal(doc["from"], "SCG-SIG-VGM", "The shipper's signature, as SOLAS requires."),
            "ResponsibleParty": party("39-xl", short=True)}


@enrich("retail", "ReceiptAdvice")
def _(f, n, doc, out):
    lines = out["ReceiptLine"] if isinstance(out["ReceiptLine"], list) else [out["ReceiptLine"]]
    lines[0].update({"ReceivedTime": V("10:40:00", "Forty minutes after the slot began."),
                     "TimingComplaintCode": V("LATE", "The truck was late for its slot."),
                     "TimingComplaint": V("Arrived 40 minutes into the slot; unloading delayed the next truck.",
                                          "The complaint.")})
    return {"AdditionalDocumentReference": {"ID": V("BM-GI-PHOTO-26-0510", "The goods-in photographs.")},
            "Signature": seal(doc["from"], "BM-SIG-26-RA")}


@enrich("sea", "ReceiptAdvice")
def _(f, n, doc, out):
    return {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading the goods came "
                                                                     "under.")},
            "Signature": seal(doc["from"], "NW-SIG-26-RA")}


@enrich("sea", "DespatchAdvice")
def _(f, n, doc, out):
    return {**kit.cost_centre("1-xl", "The buyer's cost centre, from its order."),
            "AdditionalDocumentReference": {"ID": V(f.numbers["packing"], "The packing list of the container.")},
            "Signature": seal(doc["from"], "LD-SIG-26-DA")}


@enrich("tender", "DespatchAdvice")
def _(f, n, doc, out):
    lines = out["DespatchLine"] if isinstance(out["DespatchLine"], list) else [out["DespatchLine"]]
    lines[0].update({"OutstandingQuantity": qty(TENDER_QTY - 40, "EA", "Still to come under the contract."),
                     "OutstandingReason": V("Later releases under the framework contract.", "Why."),
                     **kit.cost_centre("2-xb", "The department's programme."),
                     "DocumentReference": {"ID": V(FOLDER, "The contract.")}})
    return {"ProjectReference": {"ID": V("PWD-PARKS-26", "The parks renewal programme.")},
            **kit.cost_centre("2-xb", "The department's cost centre."),
            "Signature": seal(doc["from"], "CL-SIG-26-DA")}


@enrich("cotton", "DeliveryNote")
def _(f, n, doc, out):
    return {"Note": V("Three trailer loads, weighed at the gin.", "What was delivered."),
            "LineCountNumeric": V("1", "One line."),
            "OrderReference": {"ID": V("SCG-SEASON-2026/03", "The call-off under the season agreement.")},
            "AdditionalDocumentReference": {"ID": V("SCG-WB-26-0311", "The weighbridge ticket.")},
            "Signature": seal(doc["from"], "LCF-SIG-26-DN"),
            "Shipment": {"ID": V("LCF-SH-26-03", "The farm's three trailer loads."),
                         "GrossWeightMeasure": qty(SEED_KG + 2400, "KGM", "The cotton and the empty trailers' "
                                                                          "tare of 2,400 kg, as weighed."),
                         "Delivery": {"ActualDeliveryDate": V(f.date(3), "At the gin.")}}}


CUSTOMS_POSTS = {"XU": "Customs post at the land border, Urvanian side", "XB": "Customs post at the land border, "
                                                                               "Bayvarran side",
                 "XL": "Customs office, port of Selanu"}


def exit_office(f, country):
    if f.id in ("sea", "cotton"):
        name = "Customs office, port of Lumeport" if country == "XB" else "Customs office, port of Selanu"
    elif f.id == "plastics":
        name = "Customs post at the river border"
    else:
        name = CUSTOMS_POSTS[country]
    return {"Name": V(name, "Where the goods leave the country.")}


def export_extras(f, n, doc, out):
    exporter = doc["parties"]["ExporterParty"]
    c = PARTY[exporter]["c"]
    f.numbers.setdefault("export-declaration", out["CustomsDeclaration"]["ID"].value)
    x = {"ExportTypeCode": V("PERMANENT", "A permanent export: the goods are sold abroad."),
         "ExportReasonCode": V("SALE", "The reason: a sale to a buyer abroad."),
         "Note": V("Declared electronically before the goods leave.", "How it was declared."),
         "VersionID": V("1", "The first version."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-EX-{f.id}"),
         "CustomsDeclaration": {
             "FunctionCode": V("9", "An original declaration, not an amendment."),
             "ValidityPeriod": {"StartDate": V(out["IssueDate"].value, "From the declaration."),
                                "DurationMeasure": V("90", "The goods must leave within 90 days.", unitCode="DAY")},
             "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V(c, "The customs territory the "
                                                                                   "goods leave.")}},
             "CustomsExitOfficeLocation": exit_office(f, c),
             "ConsignorParty": party(exporter, short=True),
             "AdditionalDocumentReference": {"ID": V(f.numbers.get("order", ""), "The order behind the export.")}}}
    if f.id == "sea":
        x["CustomsDeclaration"]["FreightForwarderParty"] = party("10-xb", short=True)
    return x


def import_extras(f, n, doc, out):
    importer = doc["parties"]["ImporterParty"]
    c = PARTY[importer]["c"]
    origin = PARTY[doc["parties"]["ConsignorParty"]]["c"]
    x = {"TypeCode": V("IMPORT", "An import declaration."),
         "SubTypeCode": V("FREECIRC", "For release into free circulation."),
         "NatureOfTransactionCode": V("PURCHASE", "The goods were bought."),
         "VersionID": V("1", "The first version."),
         "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(c, "The customs territory of import.")}},
         "NotifierParty": party(doc["from"], short=True),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-IM-{f.id}")}
    refs = out.get("AdditionalDocumentReference")
    refs = [refs] if isinstance(refs, dict) else list(refs or [])
    if "export" in f.numbers:        # another country's declaration is no previous declaration of this one (C12)
        refs.append({"ID": V(f.numbers["export"], "The export declaration of the goods in the country of "
                                                  "departure, for information.")})
    inv = next((f.numbers[k] for k in ("invoice", "goods-invoice") if k in f.numbers), None)
    if inv:
        refs.append({"ID": V(inv, "The commercial invoice the customs value rests on.")})
    if refs:
        x["AdditionalDocumentReference"] = refs
    return x


for _fid in ("road", "sea", "tender", "plastics", "wood", "cotton"):
    enrich(_fid, "ExportCustomsDeclaration")(export_extras)
    enrich(_fid, "ImportCustomsDeclaration")(import_extras)
enrich("rail", "ImportCustomsDeclaration")(import_extras)      # rail/14, Lumeway's import at Marrowdale (D37)


@enrich("rail", "TransitCustomsDeclaration")
def _(f, n, doc, out):
    return {"TypeCode": V("TRANSIT", "A transit declaration."),
            "SubTypeCode": V("EXTTRANSIT", "Goods not yet released, carried across the border under customs control."),
            "NatureOfTransactionCode": V("PURCHASE", "The goods were bought."),
            "Note": V("Seals XU-VI-30411 and XU-VI-30412 to remain intact.", "The transit condition."),
            "VersionID": V("1", "The first version."),
            "ValidityPeriod": {"StartDate": V(f.date(8), "From departure."),
                               "EndDate": V(f.date(11), "The goods must reach the office of destination within "
                                                        "three days.")},
            "ExportCustomsExitOfficeLocation": {"Name": V("Customs post at the rail border station, Urvanian side",
                                                          "Where the goods leave Urvania.")},
            # the Accord's common transit, not Urvania's alone: the region of the Trade Accord, where the offices of
            # both countries act on it (D37 point 2, rail/06#F18; O140's candidate case for Address/Region)
            "JurisdictionRegionAddress": {"Region": V("Lumeport Trade Accord", "The group of countries in which the "
                                                                               "declaration is relevant: the Accord's "
                                                                               "common transit procedure, from "
                                                                               "Urvania's office of departure to "
                                                                               "Bayvarra's office of destination.")},
            "FreightForwarderParty": party("14-xu", short=True),
            "NotifierParty": party("5-xu", short=True),
            "AdditionalDocumentReference": {"ID": V(f.numbers["tep"], "The transport plan.")},
            "Signature": seal(doc["from"], "VI-SIG-TD")}


@enrich("road", "CertificateOfOrigin")
def _(f, n, doc, out):
    # no previous job: a first application (road/06#F17, 07#F18); no embassy and no insurance endorsement: the chamber
    # is the only endorser and a certificate between Accord members needs no legalisation (road/07#F10, 06#F3, D35)
    x = {"Note": V("Preferential origin under the trade accord.", "What the certificate is for."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-CO-{n:02d}"),
         "CertificateOfOriginApplication": {
             "Remarks": V("Side frames cast in Urvania from Urvanian ore and slats of Bayvarran hardwood; the casting, "
                          "finishing and making of the benches in Urvania give origin.", "Why the goods are of "
                                                                                       "Urvanian origin."),
             "ExporterParty": party("5-xu", short=True),
             "ImporterParty": party("6-xb", short=True),
             "DocumentDistribution": {"ID": V("1", "The importer's copy."),
                                      "DocumentTypeCode": V("CertificateOfOrigin", "The document distributed: this "
                                                                                   "certificate."),
                                      "DistributionTypeCode": V("ELECTRONICCOPY", "The importer gets a copy as a "
                                                                                  "message; it declares the origin "
                                                                                  "at import."),
                                      "Party": party("6-xb", short=True)},
             "SupportingDocumentReference": {"ID": V(f.numbers["invoice"] if "invoice" in f.numbers else
                                                     f.numbers["order"], "The commercial document behind the "
                                                                         "goods.")},
             "Signature": seal("5-xu", "VI-SIG-COA")}}
    if doc["from"] == "20-xu":
        x["IssuerEndorsement"] = {"Remarks": V("Origin verified against the exporter's production records.",
                                               "What the chamber checked."),
                                  "Signature": seal("20-xu", "FCC-SIG-26-0309")}
    return x


@enrich("cotton", "GoodsCertificate")
def _(f, n, doc, out):
    return {"TypeCode": V("PHYTO", "A plant health certificate for the cotton."),
            "Description": V("The ginned cotton is free of the pests named by Bayvarra's plant health rules.",
                             "What it certifies."),
            "Note": V("Inspected at the ginnery's warehouse.", "Where."), "VersionID": V("1", "The first version."),
            "ValidityPeriod": {"StartDate": V(f.date(26), "From the inspection."),
                               "EndDate": V(f.date(40), "For two weeks: the bales must ship by then.")},
            "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V("XB", "For import into Bayvarra.")}},
            "WarehouseParty": party("39-xl", short=True),
            "ConsignorParty": party("39-xl", short=True),
            "ConsigneeParty": party("40-xb", short=True),
            # issued and signed by Lisavu's plant protection organisation: customs is not its authority and the
            # forwarder is not named on it (D33 point 1, O170; cotton/10#F4, F15)
            "Attestation": {"ID": V("DAL-ATT-26-0042", "The inspector's attestation."),
                            "Name": V("Freedom from pests", "What is attested."),
                            "Description": V("Sampled and found free of boll weevil and pink bollworm.", "In words."),
                            "Note": V(f"10 bales sampled out of {len(kit.flow_packages(f)['pieces'])}.",
                                      "The sample, out of the bales of the shipment."),
                            "AcceptanceIndicator": V("true", "Accepted."),
                            "ValidityPeriod": {"EndDate": V(f.date(40), "As the certificate.")},
                            "IssuerParty": party("45-xl", short=True),
                            "AttestationLine": {"ID": V("1", "The pest checked."), "TypeCode": V("PEST", "A pest "
                                                                                                        "check."),
                                                "Description": V("Boll weevil: none found.", "The finding."),
                                                "CriterionItem": {"ID": V("XB-PH-07", "Bayvarra's rule."),
                                                                  "CriterionDescription": V("No live insects in a "
                                                                                            "sample of 10 bales.",
                                                                                            "The criterion."),
                                                                  "DeclaredPropertyItem": {"Name": V("Cotton lint, "
                                                                                                     "compressed "
                                                                                                     "bale", "The "
                                                                                                     "goods it is "
                                                                                                     "about.")}},
                                                "SubAttestationLine": {"ID": V("1.1", "The second pest."),
                                                                       "Description": V("Pink bollworm: none found.",
                                                                                        "The finding.")}}},
            "GoodsProcessing": {"ID": V("SCG-PROC-26", "The processing on the island."),
                                "TypeCode": V("GINNING", "The cotton was ginned."),
                                "Description": V("Ginned, cleaned and pressed into bales.", "In words."),
                                "Note": V("At the Selanu cotton ginnery.", "Where."),
                                "Period": {"StartDate": V(f.date(5), "The ginning."), "EndDate": V(f.date(20), "Its "
                                                                                                             "end.")},
                                "ProcessingParty": party("39-xl", short=True),
                                "CriterionItem": {"CriterionDescription": V("Seed removed; lint only.", "What "
                                                                            "processing the rule requires."),
                                                  "DeclaredPropertyItem": {"Name": V("Cotton lint", "The goods.")}},
                                "SubGoodsProcessing": {"TypeCode": V("PRESSING", "Pressed into bales."),
                                                       "Description": V("Bales of about 227 kg.", "In words.")}},
            "OriginalDocumentReference": {"ID": V("XL-CLS-2026-0042", "The classing certificate of the cotton.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["order"], "The mill's order.")},
            "Signature": seal(doc["from"], "DAL-SIG-26-PH")}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    return {"StatusCode": V("VALID", "The carnet is valid."), "Status": V("Issued", "In words."),
            "Note": V("Samples for the Selanu trade fair in early June; they come home after the fair.",
                      "What it is for."),
            "VersionID": V("1", "The first version."),
            "ExportReasonCode": V("EXHIBITION", "Temporary export for a fair."),
            "ExportReason": V("Exhibition at the Selanu trade fair", "In words."),
            "IssuerEndorsement": {"DocumentID": V(out["ID"].value, "The carnet."),
                                  "ApprovalStatus": V("Issued", "The chamber issued it."),
                                  "EndorserParty": {"RoleCode": V("ISSUER", "The issuing chamber."),
                                                    "SequenceNumeric": V("1", "The first endorsement."),
                                                    "Party": party("20-xu", short=True),
                                                    "SignatoryContact": {"Name": V("Carnet office", "The chamber's "
                                                                                   "carnet office, the name its "
                                                                                   "contact has (carnet/01#F12).")}}},
            "AdditionalDocumentReference": {"ID": V("SCC-FAIR-26-INV", "The fair's invitation to exhibit.")},
            "DocumentDistribution": {"ID": V("1", "The holder's carnet."),
                                     "DocumentTypeCode": V("GoodsItemPassport", "The document distributed: this "
                                                                                "carnet."),
                                     "DistributionTypeCode": V("COLLECT", "The holder collects the paper carnet at "
                                                                          "the chamber's carnet office: customs "
                                                                          "stamp its counterfoils as the samples "
                                                                          "travel."),
                                     "Party": party("5-xu", short=True)},
            "Signature": seal("20-xu", "FCC-SIG-26-ATA")}


@enrich("carnet", "ProofOfReexportationRequest")
def _(f, n, doc, out):
    return {"Note": V(f"The re-exportation limit of {carnet_day('limit')} set on the importation counterfoil has "
                      "passed, and the Island Customs Service has no discharged re-exportation voucher on file for "
                      "the samples.", "Why the chamber asks: a missing voucher, not a missing stamp (D40, "
                                      "carnet/02#F4)."),
            "VersionID": V("1", "The first request."),
            "GoodsItemPassportCounterfoilID": V("IMP-1", "The importation counterfoil not discharged."),
            "AdditionalDocumentReference": {"ID": V("XL-CUS-ATA-26-0071", "The customs' notice to the chamber.")},
            "Signature": seal(doc["from"], "SCC-SIG-26-PRQ")}


@enrich("carnet", "ProofOfReexportationReminder")
def _(f, n, doc, out):
    value = out_value_xlc(f).quantize(Decimal('0.01'))
    tax = (value * Decimal("0.10")).quantize(Decimal("0.001"))
    surcharge = (tax * Decimal("0.10")).quantize(Decimal("0.001"))
    claim = tax + surcharge
    return {"Note": V("Without proof within 30 days, the island's import consumption tax on the samples and the "
                      "carnet surcharge will be claimed from the guarantee.", "What happens otherwise."),
            "VersionID": V("1", "The first reminder."),
            "IssuerEndorsement": {"DocumentID": V(out["ID"].value, "The reminder the chamber endorses, as the "
                                                                   "guaranteeing association whose guarantee is at "
                                                                   "stake."),
                                  "ApprovalStatus": V("Endorsed", "The status of the endorsement itself; the "
                                                                  "request's open state is in the note "
                                                                  "(carnet/03#F8)."),
                                  "EndorserParty": {"RoleCode": V("GUARANTOR", "The importing guarantor."),
                                                    "SequenceNumeric": V("1", "The only one."),
                                                    "Party": party("20-xl", short=True),
                                                    "SignatoryContact": {"Name": V("Carnet office", "The chamber's "
                                                                                   "carnet office.")}}},
            "PaymentTerms": {"Note": V(f"Import consumption tax of 10 % on the declared value of {value:,.2f} "
                                      f"coral, {tax:,.3f}, and the carnet surcharge of 10 % of the tax, "
                                      f"{surcharge:,.3f}: {claim:,.3f} coral fall due if no proof arrives within "
                                      "30 days. Benches of Accord origin owe no duty (D18).",
                                      "The claim that would follow (D40)."),
                             "Amount": amount(claim, "XLC", "The tax and surcharge at stake."),
                             "PaymentDueDate": V(f.date(CARNET_DAYS["reminder"] + 30), "The day they fall due: "
                                                                                        "30 days after the "
                                                                                        "reminder.")},
            "AdditionalDocumentReference": {"ID": V("XL-CUS-ATA-26-0071", "The customs' notice.")},
            "Signature": seal(doc["from"], "SCC-SIG-26-PRM")}


def out_value_xlc(f):
    """The declared value of the samples in coral: the carnet's value for the guarantee, at the reference rate."""
    return sum(Decimal(str(d["ordered"])) * Decimal(str(kit.price_of(d["item"], f.buyer)["amount"]))
               * kit.rate(kit.price_of(d["item"], f.buyer)["currency"], "XLC") for d in kit.by_item(f.deal))


@enrich("carnet", "ProofOfReexportation")
def _(f, n, doc, out):
    return {"Note": V(f"The samples left Selanu airport on {carnet_day('reexport')} and were re-imported into "
                      f"Urvania on {carnet_day('reimport')}, as the stamped counterfoils show.", "The proof."),
            "VersionID": V("1", "The first version."),
            "GoodsItemPassportAttachment": {"ExternalReference": {
                "URI": V("https://www.camera-ferrano.example/ata/carnet-scan.pdf", "A scan of the stamped "
                                                                                   "counterfoils, on the chamber's "
                                                                                   "own domain (carnet/04#F11)."),
                "MimeCode": V("application/pdf", "A PDF."),
                "Description": V("Scan of the stamped re-exportation and re-importation counterfoils of the carnet",
                                 "What the attachment is (carnet/04#F10).")}},
            "AdditionalDocumentReference": [
                {"ID": V(f.numbers["por-request"], "The request this proof answers (carnet/04#F4).")},
                {"ID": V(f.numbers["por-reminder"], "And its reminder.")}],
            "Signature": seal(doc["from"], "FCC-SIG-26-POR")}


import base64 as _b64  # noqa: E402


def full_signature(pid, no, f, day, why):
    """A signature with everything UBL can say about it: method, validation and the signature value itself."""
    blob = _b64.b64encode(f"Signature value of {no}, shortened for the example world.".encode()).decode()
    return {"ID": V(no, why), "ReasonCode": V("APPROVAL", "The signer approves the document."),
            "Note": V("Signed with the company's seal certificate.", "How."),
            "ValidationDate": V(f.date(day), "Verified by the council's validation service before the document "
                                             "was issued, after the terms it binds were verified (sea/03#F1)."),
            "ValidationTime": V("12:40:00", "At that time."),
            "ValidatorID": V("LTAC-VALIDATOR", "The trade accord council's validation service."),
            "CanonicalizationMethod": V("http://www.w3.org/2006/12/xml-c14n11", "Canonical XML 1.1."),
            "SignatureMethod": V("http://www.w3.org/2001/04/xmldsig-more#rsa-sha256", "RSA with SHA-256."),
            "SignatoryParty": party(pid, short=True),
            "DigitalSignatureAttachment": {
                "EmbeddedDocumentBinaryObject": V(blob, "The signature value, Base64-encoded.",
                                                  mimeCode="application/pkcs7-signature")},
            "OriginalDocumentReference": {"ID": V(no.replace("SIG", "DOC"), "The document as signed.")}}


def full_reference(f, rid, why, day):
    """A document reference with everything UBL can say about it."""
    text = _b64.b64encode(b"Terms of the digital trade agreement of the world, version 1.0.").decode()
    return {"ID": V(rid, why),
            "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:doc:{rid}")), "Its UUID."),
            "IssueDate": V(f.date(day), "Its issue date."), "IssueTime": V("12:00:00", "And time."),
            "DocumentTypeCode": V("774", "The kind of document."),
            "DocumentDescription": V("The terms of the digital trade agreement.", "What it is."),
            "XPath": V("/DigitalAgreement/DigitalAgreementTerms", "The part of this document the reference "
                                                                  "explains."),
            "ReferencedDocumentInternalAddress": V("section-2", "The section of the referenced document meant."),
            "LanguageID": V("en", "In English."),
            "LocaleCode": V("en-XB", "The terms are written in Bayvarran English, by the distributor."),
            "VersionID": V("1.0", "The version referred to."),
            "DocumentStatusCode": V("Confirmed", "The version both sides confirmed."),
            "Attachment": {"EmbeddedDocumentBinaryObject": V(text, "A short text, Base64-encoded.",
                                                             mimeCode="text/plain"),
                           "FileName": V("terms.txt", "The file's name."),
                           "ExternalReference": {
                               "URI": V("https://www.lumeway.example/edi/terms-1.0.pdf", "The full text."),
                               "DocumentHash": V("9f2c4e1ab37d5c8e0f6a2b4d8c1e3f5a7b9d0c2e4f6a8b1c3d5e7f9a0b2c4d6e",
                                                 "The SHA-256 hash of the full text, to check it is unchanged."),
                               "HashAlgorithmMethod": V("http://www.w3.org/2001/04/xmlenc#sha256", "SHA-256."),
                               "ExpiryDate": V(f.date(365), "The link works for a year."),
                               "ExpiryTime": V("23:59:00", "Until the end of that day."),
                               "MimeCode": V("application/pdf", "A PDF."),
                               "FormatCode": V("fmt/480", "An archivable PDF."),
                               "EncodingCode": V("binary", "Not encoded."),
                               "CharacterSetCode": V("UTF-8", "The character set of its text."),
                               "FileName": V("terms-1.0.pdf", "The file's name."),
                               "Description": V("The full terms.", "What it holds.")}},
            "ValidityPeriod": {"StartDate": V(f.date(day), "In force from signing."),
                               "EndDate": V(f.date(day + 365), "For a year.")},
            "ResultOfVerification": {"ValidatorID": V("LTAC-VALIDATOR", "The council's validation service."),
                                     "ValidationResultCode": V("VALID", "The document's signature is valid."),
                                     "ValidationDate": V(f.date(day), "Checked."),
                                     "ValidationTime": V("12:05:00", "At that time."),
                                     "ValidateProcess": V("Signature and hash check", "What was checked."),
                                     "ValidateTool": V("Accord validator", "The tool."),
                                     "ValidateToolVersion": V("3.2", "Its version."),
                                     "SignatoryParty": party("32-xb", short=True)}}


def service_customization(pid, doc_type, sending):
    """The CustomizationID of the documents a digital service sends or receives: that of the flow's document of that
    type between the two parties (world_specs)."""
    import world_specs
    d = next(x for x in WORLD["documents"] if x["flow"] == "sea" and x["doc"] == doc_type
             and x["from" if sending else "to"] == pid)
    return world_specs.customization(d, WORLD)[0]


def digital_service(pid, doc_type, sending):
    return {"ID": V(f"{kit.initials(pid)}-{doc_type}-{'OUT' if sending else 'IN'}", "The party's service for this "
                                                                                     "document."),
            "CustomizationID": V(service_customization(pid, doc_type, sending), "The specification the documents of "
                                 "this service follow: the CustomizationID those documents carry in this flow."),
            "DigitalDocumentMetadata": {"ID": V(doc_type, "The document type."),
                                        "FormatID": V("UBL", "The format."),
                                        "VersionID": V("2.5", "Its version."),
                                        "SchemaURI": V(f"https://docs.oasis-open.org/ubl/os-UBL-2.5/xsdrt/maindoc/"
                                                       f"UBL-{doc_type}-2.5.xsd", "The schema."),
                                        "DocumentTypeCode": V(doc_type, "The document type, as a code.")},
            "DigitalDeliveryChannel": {"NetworkID": V("ACCORD-NET", "The trade accord's document network."),
                                       "ParticipantID": V(PARTY[pid]["identity"].get("endpoint", pid), "The party's "
                                                                                                        "address on "
                                                                                                        "it."),
                                       "TestIndicator": V("false", "In production."),
                                       "DigitalMessageDelivery": {"ProtocolID": V("AS4", "The transport protocol."),
                                                                  "EnvelopeTypeCode": V("SBDH", "The business "
                                                                                                "envelope."),
                                                                  "EndpointURI": V("https://ap." + PARTY[pid]["identity"]
                                                                                   ["website"].split("//www.")[1]
                                                                                   + "/as4", "The access point, under "
                                                                                   "the party's own domain.")},
                                       "DigitalCertificate": {"ID": V("LTAC-AP-" + PARTY[pid]["identity"]["registry_id"]
                                                                      .replace("IC", ""), "The serial number of the "
                                                                      "access point's X.509 certificate, unique only "
                                                                      "with its issuer: the Trade Accord Council, the "
                                                                      "certification authority of the network "
                                                                      "(decision ID-Q10)."),
                                                              "CertificateType": V("Access point", "Its kind."),
                                                              "IssuerParty": party("32-xb", short=True)}}}


@enrich("sea", "DigitalAgreement")
def _(f, n, doc, out):
    procs = out["DigitalProcess"]
    for p, (doc_type, send, recv) in zip(procs, (("Order", "1-xl", "6-xb"), ("Invoice", "6-xb", "1-xl"))):
        p["ProfileID"] = V(f"urn:ubl-examples:world:profile:{p['ID'].value}:1.0", "The Trade Accord's process "
                           "profile the agreement covers.")
        p["DigitalCollaboration"] = {"ID": V(f"{p['ID'].value}-1", "The main exchange of the process."),
                                     "SendingDigitalService": digital_service(send, doc_type, True),
                                     "ReceivingDigitalService": digital_service(recv, doc_type, False)}
        p["CertificationDocumentReference"] = {"ID": V(f"ACCORD-CERT-PROC-{p['ID'].value}", "The council's "
                                                                                             "certification of "
                                                                                             "the process.")}
    return {"AgreementTypeCode": V("BILATERAL", "An agreement between two parties."),
            "PreviousVersionID": V("0.9", "The draft both sides commented on."),
            "RequiredResponseMessageLevelCode": V("BUSINESS", "A business response is required for every "
                                                              "document."),
            "Signature": full_signature("6-xb", "LD-SIG-26-DA-1", f, 1, "The distributor's signature as "
                                                                        "governor."),
            "AgreementCountry": {"IdentificationCode": V("XB", "Governed by Bayvarra's law.")},
            "RequiredCertificationDocumentReference": full_reference(f, "LD-EDI-TERMS-1.0", "The terms both sides "
                                                                                            "must certify.", 1),
            "DigitalAgreementTerms": {
                "Description": V("Documents are exchanged over the trade accord's network.", "The terms."),
                "ValidityPeriod": {"StartDate": V(f.date(1), "From signing."), "EndDate": V(f.date(366), "For a "
                                                                                                         "year.")},
                "AdoptionPeriod": {"StartDate": V(f.date(1), "The buyer adopts it"), "EndDate": V(f.date(15),
                                                                                                "within two "
                                                                                                "weeks.")},
                "ServiceLevelAgreement": {
                    "ID": V("LD-SLA-1", "The service level."), "ServiceTypeCode": V("MESSAGING", "For the "
                                                                                                  "exchange."),
                    "ServiceType": V("Document exchange", "In words."),
                    "AvailabilityTimePercent": V("99.5", "The access point is available 99.5 % of the time."),
                    **{f"{d}AvailabilityIndicator": V("true" if d not in ("Saturday", "Sunday") else "false",
                                                      "Supported on " + d + "s." if d not in ("Saturday", "Sunday")
                                                      else "No support on " + d + "s.")
                       for d in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")},
                    "MinimumResponseTimeDurationMeasure": V("4", "An answer to a problem within four hours.",
                                                            unitCode="HUR"),
                    "MinimumDownTimeScheduleDurationMeasure": V("48", "Planned downtime announced 48 hours ahead.",
                                                                unitCode="HUR"),
                    "MaximumIncidentNotificationDurationMeasure": V("1", "An incident reported within an hour.",
                                                                    unitCode="HUR"),
                    "MaximumDataLossDurationMeasure": V("0", "No document may be lost.", unitCode="HUR"),
                    "MeanTimeToRecoverDurationMeasure": V("2", "Back in two hours on average.", unitCode="HUR"),
                    "ServiceAvailabilityPeriod": {"StartTime": V("07:00:00", "Support from seven."),
                                                  "EndTime": V("19:00:00", "Until seven.")},
                    "ServiceMaintenancePeriod": {"StartTime": V("02:00:00", "Maintenance at night."),
                                                 "EndTime": V("04:00:00", "Until four.")}}}}


@enrich("sea", "DigitalCapability")
def _(f, n, doc, out):
    return {"VersionID": V("1.0", "The first statement of capability."),
            "PreviousVersionID": V("0.9", "The draft."),
            "Signature": seal(doc["from"], "LD-SIG-26-DC")}


@enrich("sea", "BusinessCard")
def _(f, n, doc, out):
    return {"VersionID": V("2", "The card as updated this year."), "PreviousVersionID": V("1", "Last year's card."),
            "BriefDescription": V("Distributor of street and garden furniture for Bayvarra and the islands, "
                                  "with a weekly sailing to Selanu (Port Wrenfield in the island's address "
                                  "register).", "The business in a sentence. The town is Selanu in running text, "
                                  "also in English; Port Wrenfield is its official English name, which addresses "
                                  "carry (decision D3)."),
            "Signature": seal(doc["from"], "LD-SIG-26-BC"),
            "BrochureDocumentReference": {"ID": V("LD-BROCHURE-2026", "The distributor's brochure."),
                                          "Attachment": {"ExternalReference": {
                                              "URI": V("https://www.lumeway.example/brochure-2026.pdf", "Where it "
                                                                                                        "is."),
                                              "MimeCode": V("application/pdf", "A PDF.")}}},
            "AdditionalDocumentReference": {"ID": V("LD-REG-XB", "The distributor's registration extract.")},
            "BusinessCapability": {"ID": V("CAP-STOCK", "A capability."),
                                   "CapabilityTypeCode": V("WAREHOUSING", "What it can do."),
                                   "Description": V("Stock of 2,000 benches in Marrowdale.", "In words."),
                                   "ValueAmount": amount(Decimal("1040000.00"), "XBL", "The stock's value."),
                                   "ValueQuantity": qty(2000, "EA", "Benches in stock."),
                                   "SuppliedEvidence": {"ID": V("LD-AUDIT-2025", "The evidence."),
                                                        "EvidenceTypeCode": V("AUDIT", "An audit report."),
                                                        "Name": V("Stock count 2025", "Its name."),
                                                        "Description": V("Year-end count by the auditor.", "What "
                                                                                                           "it is."),
                                                        "CandidateStatement": V("The stock is counted every year.",
                                                                                "The company's statement."),
                                                        "ConfidentialityLevelCode": V("PUBLIC", "May be shared."),
                                                        "EvidenceIssuingParty": party("6-xb", short=True),
                                                        "Language": {"ID": V("en", "English.")}},
                                   "ValidityPeriod": {"EndDate": V(f.date(240), "Until the next count.")},
                                   "WebSite": {"ID": V("WEB-1", "The stock page."), "Name": V("Stock", "Its name."),
                                               "Description": V("Live stock levels.", "What it shows."),
                                               "WebSiteTypeCode": V("EXTRANET", "For trade customers."),
                                               "URI": V("https://www.lumeway.example/stock", "Where."),
                                               "WebSiteAccess": {"URI": V("https://www.lumeway.example/login",
                                                                          "The login page."),
                                                                 "Login": V("velumi", "The login the distributor set "
                                                                                      "up for the new customer."),
                                                                 "Password": V("Tq7-mR4w-Lz9", "The one-time "
                                                                     "password for the first login, which the "
                                                                     "extranet asks to be changed at once and "
                                                                     "accepts only until " + f.date(14) + ": a new "
                                                                     "customer cannot choose a password before it "
                                                                     "has an account. It is no secret once used.")}}}}


@enrich("sea", "InvoiceStatusRequest")
def _(f, n, doc, out):
    return {"RequestTime": V("10:00:00", "When asked."), "Note": V("Has the invoice been approved?", "The question."),
            "Signature": seal(doc["from"], "LD-SIG-26-ISR")}


@enrich("sea", "InvoiceStatusResponse")
def _(f, n, doc, out):
    return {"Note": V("Approved; the balance will be paid to the factor.", "The answer."),
            "VersionID": V("1", "The first answer."),
            # no payment: the response is an approval; the payment of 25 June is reported by the remittance advice
            # (sea/24#F1, D30 point 9, C72)
            "Signature": seal(doc["from"], "VT-SIG-26-ISP")}


@enrich("road", "ApplicationResponse")
def _(f, n, doc, out):
    return {"ResponseDate": V(f.date(10), "The day the invoice was matched against order and receipt."),
            "ResponseTime": V("14:05:00", "In the afternoon run of the invoice matching, after the corrected receipt "
                                          "advice of 10:48."),
            "Note": V("Accepted for payment; line 2 matched the substituted casting.", "The result."),
            "VersionID": V("1", "The first response."),
            "Signature": seal(doc["from"], "LD-SIG-26-AR"),
            "DocumentResponse": {
                "Response": {"EffectiveDate": V(f.date(10), "Effective at once."),
                             "EffectiveTime": V("14:05:00", "When matched."),
                             "Status": {"ConditionCode": V("MATCHED", "The invoice matched order and receipt."),
                                        "Description": V("Three-way match passed.", "In words.")}},
                # no issuer and recipient of the invoice: the invoice names its parties (road/16#F11, D35)
                "LineResponse": {"LineReference": {"LineID": V("2", "The invoice line of the side frames.")},
                                 "Response": {"ReferenceID": V("2", "The line."),
                                              "ResponseCode": V("AP", "Accepted."),
                                              "Description": V("Matched to the substituted 2026 casting.",
                                                               "Why it needed a look.")}}}}


@enrich("retail", "DocumentStatusRequest")
def _(f, n, doc, out):
    return {"Note": V("Has the order been accepted?", "The question."),
            "TrackingID": V(f.numbers["order"], "The order the store tracks."),
            "Signature": seal(doc["from"], "BM-SIG-26-DSR")}


@enrich("retail", "DocumentStatus")
def _(f, n, doc, out):
    tep = next(d for d in WORLD["documents"] if d["flow"] == f.id and d["doc"] == "TransportExecutionPlanRequest")
    booking = f.number("tep-request", tep["from"], tep["doc"])     # booked now, sent as the next document
    return {"Note": V("Accepted and booked.", "The answer."),
            "Signature": seal(doc["from"], "LD-SIG-26-DS"),
            "AdditionalDocumentResponse": {"Response": {"ResponseCode": V("AP", "The transport booking is "
                                                                                "confirmed too.")},
                                           "DocumentReference": {"ID": V(booking, "The transport booking: the "
                                                                         "request that follows as the next document "
                                                                         "of the flow, numbered when the truck was "
                                                                         "booked.")}}}


def contact(name, why, tel_of=None, email=None):
    c = {"Name": V(name, why)}
    if tel_of:
        c["Telephone"] = V(PARTY[tel_of]["identity"]["contact"]["telephone"], "The number.")
    if email:
        c["ElectronicMail"] = V(email, "The address, under the reserved .example domain.")
    return c


@enrich("retail", "Order")
def _(f, n, doc, out):
    if doc["from"] != "26-xb":
        return {}
    return {"BuyerCustomerParty": {"CustomerAssignedAccountID": V("BM-6120", "The store's own number for its "
                                                                             "garden department."),
                                   "SupplierAssignedAccountID": V("LD-C-0418", "The distributor's customer number "
                                                                               "for the store."),
                                   "AdditionalAccountID": V("BM-LUM-01", "The store's branch number."),
                                   "DeliveryContact": contact("Goods-in, garden department", "Whom the driver "
                                                              "reports to.", "26-xb"),
                                   "AccountingContact": contact("Accounts payable", "Where invoices go.",
                                                                email="invoices@brightmarket.example"),
                                   "BuyerContact": contact("Garden department buyer", "Who placed the order.",
                                                           "26-xb")},
            "SellerSupplierParty": {"CustomerAssignedAccountID": V("BM-S-0071", "The store's supplier number for "
                                                                                "the distributor."),
                                    "AdditionalAccountID": V("LD-XB-01", "The distributor's sales office."),
                                    "DataSendingCapability": V("UBL 2.5 over the trade accord network", "How the "
                                                                                                         "distributor "
                                                                                                         "sends "
                                                                                                         "documents."),
                                    "DespatchContact": contact("Dispatch office", "Who despatches.", "6-xb"),
                                    "AccountingContact": contact("Accounts receivable", "For payment questions.",
                                                                 email="ar@lumeway.example"),
                                    "SellerContact": contact("Key account manager, retail", "The store's contact "
                                                                                            "at the distributor.",
                                                             "6-xb")}}


@enrich("sea", "Invoice")
def _(f, n, doc, out):
    if doc["from"] != "6-xb":
        return {}
    return {"PaymentMeans": {
        "PaymentPlatformID": V("HF-COLLECT", "The factor's collection platform the payment is matched on."),
        "ServiceLevelCode": V("NURG", "ISO 20022 service level NURG: a normal, not urgent, payment."),
        "TradeFinancing": {"ID": V("HF-FA-2026-007/18", "The financing of this receivable under the factoring "
                                                        "agreement."),
                           "FinancingInstrumentCode": V("FACTORING", "The receivable was sold to the factor."),
                           "ContractDocumentReference": {"ID": V("HF-FA-2026-007", "The factoring agreement.")},
                           "DocumentReference": {"ID": V("HF-ASSIGN-26-0091", "The notice of assignment.")},
                           "FinancingParty": party("24-xb", short=True),
                           "FinancingFinancialAccount": kit.account("24-xb", "The factor's account."),
                           "Clause": {"ID": V("HF-FA-7.2", "The clause on payment."),
                                      "Content": V("Payment to any other account does not discharge the buyer.",
                                                   "What it says.")}},
        "RemittanceDocumentDistribution": {"ID": V("1", "Where the remittance advice goes."),
                                           "DocumentTypeCode": V("RemittanceAdvice", "The document."),
                                           "DistributionTypeCode": V("ELECTRONIC", "By message."),
                                           "Communication": {"ChannelCode": V("EM", "UN/EDIFACT 3155 code EM: "
                                                                                    "electronic mail.",
                                                                              listID="UN/EDIFACT EDED 3155"),
                                                             "Channel": V("E-mail", "In words."),
                                                             "Value": V("remittance@harbourline.example", "The "
                                                                                                        "factor's "
                                                                                                        "address.")},
                                           "Party": party("24-xb", short=True)},
        "PaymentInstructionAttachment": {"ExternalReference": {"URI": V("https://www.harbourline.example/pay/"
                                                                        "HF-FA-2026-007-18", "The factor's payment "
                                                                                             "page for this "
                                                                                             "invoice."),
                                                               "MimeCode": V("application/pdf", "A PDF.")}}}}


@enrich("rail", "TransportExecutionPlan")
def _(f, n, doc, out):
    return {"TransportContract": {"IssueDate": V("2026-01-05", "Signed at the start of the year: the time below "
                                                               "has its date (rail/03#F15)."),
                                  "IssueTime": V("10:00:00", "Signed in the morning."),
                                  "NominationDate": V(f.date(2), "The deadline for booking this train's slots: the "
                                                                 "request of the day before met it."),
                                  "NominationTime": V("09:00:00", "At that time."),
                                  "ContractTypeCode": V("FRAMEWORK", "A framework contract."),
                                  "Note": V("Call-off 88 of the year.", "Which call-off."),
                                  "VersionID": V("2", "The contract as amended in March."),
                                  "ModificationReasonCode": V("VOLUME", "Amended for higher volumes."),
                                  "ModificationReasonDescription": V("Ten more slots a month from April.", "The "
                                                                                                          "change."),
                                  "Description": V("Container slots on the trains from the Ferrano hub to "
                                                   "Marrowdale, with the carrier's haulage of the boxes to the hub.",
                                                   "What it covers."),
                                  "ContractDocumentReference": {"ID": V(f"{RAIL_CONTRACT}-A1", "The amendment.")},
                                  "NominationPeriod": {"StartDate": V(f.date(0), "Slots are booked from a week "
                                                                                 "before the train"),
                                                       "EndDate": V(f.date(2), "until the deadline above, so period "
                                                                               "and deadline agree (rail/03#F15)."),
                                                       "EndTime": V("09:00:00", "The deadline's time.")},
                                  "ContractualDelivery": {"LatestDeliveryDate": V(f.date(10), "The contract's latest "
                                                                                              "delivery for this "
                                                                                              "call-off.")}}}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    e = PARTY["5-xu"]["identity"]["employee"]
    return {"RepresentativeParty": {"Person": {
        "Title": V("Ing.", "The professional title, as on the travel documents."),
        "NationalityCode": V("XU", "Urvanian."),
        "BirthplaceLocation": {"Name": V(e["birthplace"], "The place of birth."),
                               "Address": {"Country": {"IdentificationCode": V("XU", "In Urvania.")}}},
        "Contact": {"Name": V("Mobile on the road", "How to reach the employee at the fair."),
                    "Telephone": V(e["mobile"], "The employee's own mobile, not the holder's order desk "
                                                "(carnet/01#F2).")},
        "ResidenceAddress": {"CityName": build_examples.city_names("XU", "Ferrano", "Where the employee lives."),
                             "Country": {"IdentificationCode": V("XU", "In Urvania.")}}}}}


@enrich("wood", "RequestForQuotation")
def _(f, n, doc, out):
    return {"SubmissionDueDate": V(f.date(5), "Quotations are wanted within five days."),
            "Note": V("Slats to our drawing VI-DS-SL1800.", "What is asked."),
            "PricingCurrencyCode": V("XBL", "Prices in lume, the sawmill's currency."),
            "LineCountNumeric": V("1", "One line."),
            "RequestedValidityPeriod": {"DurationMeasure": V("30", "The prices should hold for 30 days.",
                                                             unitCode="DAY")},
            "AdditionalDocumentReference": {"ID": V("VI-DS-SL1800", "The drawing of the slat.")},
            "Signature": seal(doc["from"], "VI-SIG-26-RFQ"),
            "Delivery": {"DeliveryLocation": {"Name": V("Valdara Industries, goods-in, Ferrano", "Where the slats "
                                                                                                "are wanted.")},
                         "RequestedDeliveryPeriod": {"StartDate": V(f.date(10), "From the end of the second week."),
                                                     "EndDate": V(f.date(18), "Within about a week (wood/04#F1).")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the factory.", schemeID="INCOTERMS")},
            "DestinationCountry": {"IdentificationCode": V("XU", "Into Urvania.")},
            "Contract": {"ID": V("VI-PUR-TERMS-2026", "The manufacturer's purchasing terms.")},
            "RequestForQuotationLine": [{**out["RequestForQuotationLine"][0], "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:ubl-examples:world:wood:"
                                                                                   "rfq:1")), "The line's UUID."),
                                        "Note": V("Kiln-dried hardwood, planed on four sides.", "The requirement."),
                                        "OptionalLineItemIndicator": V("false", "A required line."),
                                        "PrivacyCode": V("CONFIDENTIAL", "The drawing is the manufacturer's own."),
                                        "DocumentReference": {"ID": V("VI-DS-SL1800", "The drawing.")}}]}


@enrich("wood", "Quotation")
def _(f, n, doc, out):
    base = Decimal(out["QuotedMonetaryTotal"]["LineExtensionAmount"].value)
    line = out["QuotationLine"][0] if isinstance(out["QuotationLine"], list) else out["QuotationLine"]
    line.update({"ID": V("1", "The quotation line."), "Note": V("Oak, as drawn, in bundles of 50; the same "
                                                                 "bundle in ash is offered below.", "What is quoted."),
                 "Quantity": qty(96, "EA", "The bundles quoted: 4,800 slats, one truck."),
                 "LineExtensionAmount": amount(base, "XBL", "The quoted amount."),
                 "TaxInclusiveLineExtensionAmount": amount(base, "XBL", "No tax on an export."),
                 "TotalTaxAmount": amount(0, "XBL", "No tax on an export."),
                 "RequestForQuotationLineID": V("1", "The line of the request."),
                 "DocumentReference": [{"ID": V("VI-DS-SL1800", "The buyer's drawing the slat is quoted to "
                                                                 "(D43).")},
                                       {"ID": V("MS-SPEC-SL1800", "The sawmill's own specification of the slat, "
                                                                  "derived from the buyer's drawing (D43).")}],
                 "RequestLineReference": {"LineID": V("1", "The request line answered.")},
                 "AlternativeLineItem": {"ID": V("1-A", "The other species the request allowed (D43)."),
                                         "Quantity": qty(96, "EA", "The same quantity."),
                                         "Price": {"PriceAmount": price(ASH_BUNDLE, "XBL", "The price of a bundle "
                                                                        "in ash, below oak's."),
                                                   "BaseQuantity": qty(1, "EA", "Per bundle.")},
                                         "Item": {"Name": V("Bench slat 1800, bundle of 50, ash", "The same bundle "
                                                            "in ash, which the sawmill can saw from its next "
                                                            "felling.")}}})
    return {"Note": V("Valid for 30 days.", "The validity."),
            "PricingCurrencyCode": V("XBL", "Prices in lume."), "LineCountNumeric": V("1", "One line."),
            "AdditionalDocumentReference": {"ID": V("MS-GTC-2026", "The sawmill's general terms of sale, "
                                                                  "subsidiary to the buyer's terms (D43)."),
                                            "DocumentDescription": V("The sawmill's general terms of sale apply only "
                                                                     "where the buyer's purchasing terms "
                                                                     "VI-PUR-TERMS-2026, which govern, say nothing.",
                                                                     "Which terms govern.")},
            "Contract": {"ID": V("VI-PUR-TERMS-2026", "The buyer's purchasing terms, which govern the quotation "
                                                      "(D43).")},
            "Signature": seal(doc["from"], "MS-SIG-26-QT"),
            "Delivery": {"PromisedDeliveryPeriod": {"StartDate": V(f.date(10), "From the end of the second week, "
                                                                              "as asked."),
                                                    "EndDate": V(f.date(18), "Within about a week.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the factory, as asked.", schemeID="INCOTERMS")},
            "PaymentMeans": {"PaymentMeansCode": V("30", "By credit transfer.", listID="UN/EDIFACT EDED 4461")},
            "TransactionConditions": {"Description": V("Priced per bundle of 50 slats; the smallest order is one "
                                                       "truck: 96 bundles on 24 pallets.", "The conditions (D43).")},
            "DestinationCountry": {"IdentificationCode": V("XU", "Into Urvania.")},
            "TaxTotal": kit.tax_total([({"item": "slat-bundle-1800"}, None, Decimal("34800.00"),
                                        kit.tax_rule("36-xb", "5-xu", "slat-bundle-1800"))], "XBL")[1]}


@enrich("furniture", "RequestForQuotation")
def _(f, n, doc, out):
    return {"SubmissionDueDate": V(f.date(5), "Quotations within five days."),
            "Note": V("For the store's own label Elderwick: the Marrow dining bench and chair, each in oak and in "
                      "ash, for the autumn and winter home range, on sale from the reopening of the home and garden "
                      "department on 11 May.", "What is asked."),
            "PricingCurrencyCode": V("XBL", "In lume."),
            "LineCountNumeric": V(str(len(out["RequestForQuotationLine"])), "A line per piece and wood."),
            "RequestedValidityPeriod": {"DurationMeasure": V("60", "Prices for 60 days.", unitCode="DAY")},
            "CatalogueDocumentReference": {"ID": V("BM-RANGE-26", "The store's range plan the line belongs to.")},
            "Signature": seal(doc["from"], "BM-SIG-26-RFQ"),
            "OriginatorCustomerParty": {"Party": party("26-xb", short=True)},
            "Delivery": {"DeliveryLocation": {**kit.gln_location("26-xb", "goods-in"),
                                              "Name": V("Brightmarket Stores, goods-in", "Where.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the store.", schemeID="INCOTERMS")},
            "DestinationCountry": {"IdentificationCode": V("XB", "Bayvarra.")},
            "Contract": {"ID": V(OWN_LABEL, "The own-label agreement: the store's specification, the sale-or-return "
                                            "trial and the returns.")},
            "RequestForQuotationLine": [{**ln,
                                         **({"Note": V("Optional: seat cushions to match.", "An option the store "
                                                                                           "asks about.")}
                                            if "-chair-" in d["item"] else {}),
                                         "OptionalLineItemIndicator": V("false", "The piece itself is required."),
                                         "PrivacyCode": V("CONFIDENTIAL", "The store's own design.")}
                                        for ln, d in zip(out["RequestForQuotationLine"], MARROW_ASK)]}


@enrich("furniture", "Quotation")
def _(f, n, doc, out):
    return {"Note": V("The Elderwick Marrow bench and chair, made to the store's specification under its own label, "
                      "each in oak and in ash at the same price; a care kit free with each bench.", "What is quoted."),
            "PricingCurrencyCode": V("XBL", "In lume."),
            "LineCountNumeric": V(str(len(out["QuotationLine"])), "A line per piece and wood, and the free care kit."),
            "QuotationLine": [{**ln, "Note": V("Free: one care kit with each bench.", "Why the line has no price.")}
                              if ITEM[d["item"]].get("free_with") else ln
                              for ln, d in zip(out["QuotationLine"], MARROW_QUOTE)],
            "Signature": seal(doc["from"], "BF-SIG-26-QT"),
            "OriginatorCustomerParty": {"Party": party("26-xb", short=True)},
            "BeneficiaryParty": party("26-xb", short=True)}


@enrich("furniture", "WorkReport")
def _(f, n, doc, out):
    rate = Decimal(str(ITEM["installation"]["price"]["amount"]))
    amt = rate * 14
    half = lambda who, k: {"ID": V(f"1.{k}", "One installer's part."),
                           "WorkItemID": V(f"INST-{k}", "The installer."),
                           "WorkItemDescription": V(f"Installer {k}: seven hours.", "The work."),
                           "Quantity": qty(7, "HUR", "Seven hours."),
                           "PerformingParty": party("37-xb", short=True)}
    return {"VersionID": V("1", "The first version."),
            "Note": V("Approved by the department's facilities officer.", "The approval."),
            **kit.cost_centre("2-xb", "The department's cost centre for the job: the planning office's fit-out "
                                      "(furniture/16#F5).", iid="installation"),
            "Signature": seal("2-xb", "PWD-SIG-26-WR", "The department's approval signature."),
            "WorkQuantityTotal": {"Quantity": qty(14, "HUR", "Fourteen hours."),
                                  "WorkTypeCode": V("INSTALL", "The kind of work."),
                                  "WorkTypeDescription": V("Installing office furniture.", "In words.")},
            "ReportedPeriod": {"StartDate": V(f.date(37), "The first day."), "EndDate": V(f.date(38), "The last.")},
            "OrderReference": {"ID": V(f.numbers["order-desks"], "The department's order.")},
            "ProjectReference": {"ID": V("PWD-PLAN-OFFICE-26", "The new planning office.")},
            "AdditionalDocumentReference": {"ID": V("BF-PHOTO-26-0408", "Photographs of the finished office.")},
            "TaxTotal": {"TaxAmount": amount(0, "XBL", "Exempt: a service to a public body.")},
            "StatementMonetaryTotal": {"LineExtensionAmount": amount(amt, "XBL", "14 hours at 48 lume."),
                                       "PayableAmount": amount(amt, "XBL", "What the invoice will charge.")},
            "WorkReportLine": {"WorkItemID": V("INST", "The installation."),
                               "WorkItemDescription": V("Six desks assembled and placed.", "The work."),
                               "LineExtensionAmount": amount(amt, "XBL", "14 hours at the rate."),
                               "TaxInclusiveLineExtensionAmount": amount(amt, "XBL", "Exempt."),
                               "CompletionPercent": V("100", "Finished."),
                               "ActivityOriginLocation": {"Name": V("Lumeport Public Works Department, Civic Square",
                                                                    "Where.")},
                               "Period": {"StartDate": V(f.date(37), "From."), "EndDate": V(f.date(38), "To.")},
                               "PerformingParty": party("37-xb", short=True),
                               "WorkPhaseReference": {"ID": V("PH-2", "The second phase of the move."),
                                                      "WorkPhaseCode": V("FURNISH", "Furnishing."),
                                                      "WorkPhase": Detail("the new office is furnished", "the phase of the "
                                                                                          "move it reports."),
                                                      "ProgressPercent": V("100", "Done."),
                                                      "StartDate": V(f.date(37), "Started."),
                                                      "EndDate": V(f.date(38), "Ended."),
                                                      "WorkOrderDocumentReference": {"ID": V(f.numbers["order-desks"],
                                                                                             "The order.")}},
                               "DocumentReference": {"ID": V("BF-CHECK-26-0408", "The installation checklist.")},
                               "Price": {"PriceAmount": price(rate, "XBL", "Per hour.")},
                               "TaxTotal": {"TaxAmount": amount(0, "XBL", "Exempt.")},
                               "SubWorkReportLine": [half("37-xb", 1), half("37-xb", 2)]}}


@enrich("furniture", "OrderCancellation")
def _(f, n, doc, out):
    return {"Note": V("No cost: cancelled before production.", "The consequence."),
            "OriginatorDocumentReference": {"ID": V(f.numbers["exception"], "The exception notification that led "
                                                                            "to it.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["activity"], "The sales figures.")},
            "Contract": {"ID": V(OWN_LABEL, "The own-label agreement the line runs under; it allows "
                                            "cancellation before production.")},
            "Signature": seal(doc["from"], "BM-SIG-26-OC")}


@enrich("air", "DespatchAdvice")
def _(f, n, doc, out):
    # the frames were ordered by the order change of the sea order: the reference names both, as the cancellation
    # does (air/06#F1, 08#F2, C73)
    out["OrderReference"]["OrderTypeCode"] = V("230", "UN/EDIFACT 1001 code 230: the order referred to is an order "
                                                      "change.")
    out["OrderReference"]["DocumentReference"] = {"ID": V(SEA.numbers["order"], "The sea order the change extends.")}
    return {}


@enrich("air", "FulfilmentCancellation")
def _(f, n, doc, out):
    return {"Note": V("A new despatch advice follows this evening.", "What happens next."),
            "OrderReference": {"ID": V(f.numbers["order-change"], "The order change of the frames."),
                               "SalesOrderID": V(f"LD-SO-26-{SEA.base:04d}", "The distributor's sales order."),
                               "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:ubl-examples:world:air:1:OrderChange")),
                                         "Its UUID."),
                               "IssueDate": V(f.date(0), "Its date."), "IssueTime": V("07:50:00+00:00", "Its time, in island time."),
                               "OrderTypeCode": V("230", "UN/EDIFACT 1001 code 230: order change."),
                               "DocumentReference": {"ID": V(SEA.numbers["order"], "The original sea order.")}},
            "AdditionalDocumentReference": {"ID": V(f.numbers["status-5"], "The cargo terminal's status: the cargo "
                                                                         "accepted after the cut-off, for the next "
                                                                         "morning's flight.")},
            "Signature": seal(doc["from"], "LD-SIG-26-FC"),
            "DespatchSupplierParty": {"Party": party("6-xb", short=True)}}


@enrich("plastics", "ImportCustomsDeclaration")
def _(f, n, doc, out):
    return {"Shipment": {"GoodsItem": [{**out["Shipment"]["GoodsItem"][0], "BondedWarehouseLocation": {
        **out["Shipment"]["GoodsItem"][0]["BondedWarehouseLocation"],
        "CountrySubentity": V("Coastal State", "The state the store is in."),
        "CountrySubentityCode": V("XB-CO", "The state as a code of Bayvarra's national list."),
        "LocationTypeCode": V("BONDEDSTORE", "A customs bonded store."),
        "ValidityPeriod": {"StartDate": V("2025-01-01", "The store's licence runs"),
                           "EndDate": V("2027-12-31", "until the end of 2027.")},
        "Storage": {"ID": V("RQ-BOND-03", "Hall 3 of the bonded store."), "Name": V("Hall 3", "Its name."),
                    "GateID": V("Gate B", "The gate the barge's bags go through."),
                    "AirFlowPercent": V("0", "No forced ventilation."),
                    "HumidityPercent": V("60", "The hall's humidity limit; granulate must stay dry."),
                    "AnimalFoodApprovedIndicator": V("false", "Not approved for animal feed."),
                    "HumanFoodApprovedIndicator": V("false", "Not approved for food."),
                    "DangerousGoodsApprovedIndicator": V("false", "Not approved for dangerous goods."),
                    "RefrigeratedIndicator": V("false", "Not refrigerated."),
                    "PowerIndicator": V("true", "Power for the forklifts and lighting."),
                    "MinimumTemperature": {"AttributeID": V("AMBIENT", "The temperature of the hall."),
                                           "Measure": V("5", "At least 5 °C.", unitCode="CEL"),
                                           "Description": V("Kept frost-free.", "Why.")},
                    "MaximumTemperature": {"AttributeID": V("AMBIENT", "The temperature of the hall."),
                                           "Measure": V("35", "At most 35 °C.", unitCode="CEL")},
                    "Certificate": {"ID": V("XB-BOND-LIC-0388", "The bonded store's licence, by its number in the "
                                                                "register of customs; the schemeID names the register "
                                                                "and its authority (decision ID-Q10).",
                                            schemeID="urn:ubl-examples:world:XB:bonded-warehouse"),
                                    "CertificateTypeCode": V("BONDEDSTORE", "A licence of customs."),
                                    "CertificateType": V("Bonded store licence", "In words.")}}}}] +
        out["Shipment"]["GoodsItem"][1:]}}


@enrich("road", "Order")
def _(f, n, doc, out):
    return {"Delivery": {"Despatch": {"DespatchAddress": {"MarkCare": V("Valdara Industries c/o Castrano Logistics",
                                                                        "The goods are the manufacturer's, kept by "
                                                                        "its 3PL.")}}}}


# road/09: no temperature condition: neither the goods nor the contract ask for one (road/09#F11); no indication
# indicator, which said nothing the status does not (road/09#F10)


@enrich("retail", "RetailEvent")
def _(f, n, doc, out):
    spec = out["PromotionalEvent"]["PromotionalSpecification"]
    spec["EventTactic"] = {"Comment": V("Benches at the entrance, with a price board.", "What the store does."),
                           "Quantity": qty(12, "EA", "Twelve benches on display."),
                           "EventTacticEnumeration": {"ConsumerIncentiveTacticTypeCode": V("TPR", "A temporary price "
                                                                                                  "reduction."),
                                                      "DisplayTacticTypeCode": V("ENDCAP", "A display at the "
                                                                                           "entrance."),
                                                      "FeatureTacticTypeCode": V("FLYER", "In the store's flyer."),
                                                      "TradeItemPackingLabelingTypeCode": V("STICKER", "A price "
                                                                                                       "sticker on "
                                                                                                       "each bench.")},
                           "Period": {"StartDate": V(f.date(21), "During the promotion."),
                                      "EndDate": V(f.date(34), "Its end.")}}
    return {}


@enrich("retail", "CatalogueRequest")
def _(f, n, doc, out):
    return {"RequestedClassificationScheme": {"UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:ubl-examples:world:"
                                                                                           "HS2022")), "Its UUID."),
                                              "LastRevisionDate": V("2022-01-01", "The edition in force."),
                                              "LastRevisionTime": V("00:00:00", "From midnight."),
                                              "Note": V("Six-digit subheadings.", "The level wanted."),
                                              "Description": V("The international goods classification.", "What "
                                                                                                          "it is."),
                                              "SchemeURI": V("https://www.wcoomd.org/hs", "Where the scheme is.")}}


@enrich("sea", "ImportCustomsDeclaration")
def _(f, n, doc, out):
    return {"ImporterParty": {"PowerOfAttorney": {"IssueTime": V("11:00:00", "Signed in the morning."),
                                                  "NotaryParty": party("20-xl", short=True),
                                                  "WitnessParty": party("9-xl", short=True)}}}


@enrich("utilities", "RemittanceAdvice")
def _(f, n, doc, out):
    return {"InvoicePeriod": {"StartDate": V("2026-03-01", "The month paid for."), "EndDate": V("2026-03-31", "Its "
                                                                                                             "end.")},
            "BillingReference": {"InvoiceDocumentReference": {"ID": out["RemittanceAdviceLine"]["BillingReference"]
                                                              ["InvoiceDocumentReference"]["ID"]}},
            "AdditionalDocumentReference": {"ID": V(f"{kit.initials(doc['from'])}-BANK-26-04", "The payer's bank "
                                                                                              "statement line.")},
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-RA"),
            "RemittanceAdviceLine": {"InvoicePeriod": {"StartDate": V("2026-03-01", "March."),
                                                       "EndDate": V("2026-03-31", "Its end.")}}}


@enrich("sea", "RemittanceAdvice")
def _(f, n, doc, out):
    lines = out["RemittanceAdviceLine"]
    lines[0].update({"BuyerCustomerParty": {"Party": party("1-xl", short=True)},
                     "SellerSupplierParty": {"Party": party("6-xb", short=True)},
                     "PayeeParty": party("24-xb", short=True),
                     "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                      "TargetCurrencyCode": V("XLC", "The buyer's currency it paid from."),
                                      "CalculationRate": V("0.4", "The rate the buyer's bank applied.")}})
    return {}


@enrich("retail", "PurchaseReceipt")
def _(f, n, doc, out):
    line = out["PurchaseReceiptLine"][0]
    line.update({"Note": V("Promotion price.", "As printed."),
                 "TaxInclusiveLineExtensionAmount": amount(Decimal("717.92"), "XBL", "With the 6.5 % sales tax."),
                 "TaxTotal": {"TaxAmount": amount(Decimal("43.82"), "XBL", "The sales tax of the line.")},
                 "PurchaseLinePeriod": {"StartDate": V(f.date(25), "The warranty runs from the purchase"),
                                        "EndDate": V("2031-05-15", "for five years.")},
                 "PurchaseReference": {"ID": V(bench_frame_serial("VI-LOT-260320"), "The serial number of the bench's frame, "
                                                                             "for the warranty: the bench is one of "
                                                                             "the store's delivery from the March "
                                                                             "lot, whose frames were cast with it "
                                                                             "(the production record, D21)."),
                                       "Description": V("Frame serial number", "What the number is.")}})
    return {"PurchaseReference": {"ID": V("BM-LOYAL-0088127", "The customer's loyalty card."),
                                  "Description": V("Loyalty card", "What the number is.")},
            "SalesDocumentReference": {"ID": V("BM-DEL-26-0518-07", "The home delivery order.")},
            "AdditionalDocumentReference": {"ID": V("VI-WARRANTY-B180", "The maker's warranty card.")},
            "Signature": seal("26-xb", "BM-SIG-POS-G2")}


@enrich("sea", "CommonTransportationReport")
def _(f, n, doc, out):
    """The ship's report to the island's maritime administration before arrival: crew, port call, stores, waste,
    ballast water, health and fuel."""
    def listed(p, code):
        """A person on the crew or passenger list, which records each person's sex (FAL forms 5 and 6)."""
        p = dict(p)
        p["GenderCode"] = V(code, "As on the crew and passenger lists.", listID="ISO 5218")
        return p
    crew = [kit.person("Corin", "Halvard", "The master.", role="MASTER"),
            kit.person("Elsbeth", "Marrin", "The chief officer, also the ship's medical officer.", role="CHIEFOFFICER"),
            kit.person("Rafe", "Dunmore", "The chief engineer.", role="CHIEFENG")]
    sea_place = {"Name": V(f"At sea, about {wmap.nearest(SEA_KM / 1.852 / 2, 10)} nautical miles from Selanu, "
                           "in mid-ocean", "Where: half way, far from any land.")}
    report_place = {"Name": V(f"At sea, {sea_report_nm(f)} nautical miles off Selanu", "Where the report is made, "
                                                                                        "as the report's own "
                                                                                        "reporting location.")}
    stage = out["Shipment"]["ShipmentStage"]
    stage.update({
        "PassengerPerson": listed(kit.person("Ines", "Tavari", "The one passenger, a supercargo.",
                                             role="PASSENGER"), "2"),
        "ReportingPerson": kit.person("Corin", "Halvard", "The master reports.", role="MASTER"),
        "CrewMemberPerson": [listed(p, c) for p, c in zip(crew, ("1", "2", "1"))],
        "SecurityOfficerPerson": kit.person("Elsbeth", "Marrin", "The ship security officer.", role="SSO"),
        "ShipsSurgeonPerson": kit.person("Elsbeth", "Marrin", "No surgeon on a feeder: the chief officer is the "
                                                              "medical officer.", role="MEDICAL"),
        "DestinationPortCall": {
            "ID": V("XLSEL-26-0517", "The port call at Selanu."),
            "PlannedOperationsDescription": V("Discharge one container, load six.", "What the ship will do."),
            "PlannedWorksDescription": V("Overhaul of the No. 2 auxiliary engine alongside, about 8 hours; the main engine stays ready to sail.", "The works the ship plans in port: the port needs to know when a machine is out of service."),
            "PlannedInspectionsDescription": V("Port state control is due.", "An inspection is expected."),
            "ExpectedAnchorageIndicator": V("false", "Straight to the berth."),
            "PositionInPortID": V("BERTH-2", "The container berth."),
            "CargoAndBallastTankConditionDescription": V("Tanks clean; ballast exchanged at sea.", "Their "
                                                                                                   "condition."),
            "ShipRequirement": {"ID": V("SR-1", "A need of the ship."),
                                "Description": V("Fresh water, 40 tonnes.", "What it needs.")},
            "PrimaryPortCallPurpose": {"PurposeTypeCode": V("CARGO", "Cargo operations."),
                                       "PurposeType": V("Cargo operations", "In words."),
                                       "Description": V("Discharge and load containers.", "The purpose.")},
            "AdditionalPortCallPurpose": {"PurposeTypeCode": V("WATER", "Taking on water."),
                                          "PurposeType": V("Bunkering of fresh water", "In words.")},
            "RequestedArrivalEvent": {"IdentificationID": V("ARR-XLSEL-0517", "The requested arrival."),
                                      "OccurrenceDate": V(f.date(SEA_ARRIVES), "The morning after the ship comes off "
                                                                               "the port: Selanu's pilots take "
                                                                               "ships in by daylight only."),
                                      "OccurrenceTime": V("06:00:00", "At first light, in island time."),
                                      "TypeCode": V("ARRIVAL", "An arrival."),
                                      "Description": V("Pilot on board at the fairway buoy.", "What is asked."),
                                      "CompletionIndicator": V("false", "Not yet."),
                                      "CurrentStatus": {"ConditionCode": V("ONTIME", "Expected on time.")},
                                      "Contact": {"Name": V("Bridge", "Whom to call."),
                                                  "Telephone": V("+999 2 7900 702 117", "The ship's phone, a Bayvarran mobile number, as the "
                                                                        "ship flies Bayvarra's flag.")},
                                      "OccurrenceLocation": {"Name": V("Selanu fairway buoy", "Where the pilot "
                                                                                              "boards.")}}},
        "ShipStoreArticle": [{"ID": V("ST-1", "Spirits in the bonded store."), "Name": V("Spirits", "What."),
                              "Quantity": qty(24, "LTR", "Litres."),
                              "OfficialUse": V("Sealed by customs at Lumeport.", "Under seal."),
                              "Stowage": {"LocationID": V("BOND-1", "The bonded locker."),
                                          "Location": V("Bonded locker, accommodation deck", "Where.")}},
                             {"ID": V("ST-2", "Cigarettes."), "Name": V("Cigarettes", "What."),
                              "Quantity": qty(2000, "EA", "Pieces, counted each (EA).")}],
        "CrewPersonEffect": {"EffectDescription": V("One camera, one laptop.", "What the crew member declares."),
                             "CrewPerson": crew[2]},
        "MaritimeWaste": [{"ID": V("W-1", "Oily waste."), "Description": V("Sludge from the fuel separators.",
                                                                           "What."),
                           "WasteTypeCode": V("OIL", "MARPOL Annex I waste."),
                           "ToBeDeliveredMeasure": V("2.4", "To be delivered at Selanu.", unitCode="MTQ"),
                           "RetainedOnBoardMeasure": V("0.6", "Kept on board.", unitCode="MTQ"),
                           "MaxDedicatedStorageCapacityMeasure": V("8", "The tank's capacity.", unitCode="MTQ"),
                           "EstimatedGeneratedUntilNextPortMeasure": V("0.8", "Until Lumeport again.",
                                                                       unitCode="MTQ"),
                           "RemainingWasteDeliveryPortLocation": kit.place("XBLMP", "The rest goes ashore at "
                                                                                    "Lumeport.")},
                          {"ID": V("W-2", "Garbage."), "Description": V("Food and packaging waste.", "What."),
                           "WasteTypeCode": V("GARBAGE", "MARPOL Annex V waste."),
                           "ToBeDeliveredMeasure": V("1.5", "To be delivered.", unitCode="MTQ")}],
        "BallastWaterSummary": {
            "ID": V("BW-26-0517", "The ballast water report."),
            "ManagementPlanOnBoardIndicator": V("true", "The plan is on board."),
            "ManagementPlanImplementedIndicator": V("true", "And followed."),
            "IMOGuidelinesOnBoardIndicator": V("true", "The IMO guidelines are on board."),
            "TotalBallastTanksOnBoardQuantity": qty(8, "EA", "Ballast tanks."),
            "TanksInBallastQuantity": qty(4, "EA", "Tanks with ballast now."),
            "TanksExchangedQuantity": qty(4, "EA", "Exchanged at sea."),
            "TanksNotExchangedQuantity": qty(0, "EA", "None left unexchanged."),
            "TotalBallastWaterOnBoardMeasure": V("1240", "Ballast on board.", unitCode="TNE"),
            "TotalBallastWaterCapacityMeasure": V("2480", "The capacity.", unitCode="TNE"),
            "OtherControlActions": V("Sediment flushed from the forepeak tank during the exchange and recorded in the ballast water record book.", "A control action besides the exchange: sediment management under the ballast water management plan."),
            "NoControlActionsReason": V("Exchange done at more than 200 nautical miles from land.", "Why no "
                                                                                                  "treatment was "
                                                                                                  "needed."),
            "UptakeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."), "TankTypeCode": V("WING",
                                                                                                "A wing tank."),
                                              "VolumeMeasure": V("310", "Taken up at Lumeport: 310 cubic metres. A volume needs a volume unit; "
                                                                 "the 310 were meant as tonnes of water, which is "
                                                                 "about the same number of cubic metres.",
                                                 unitCode="MTQ"),
                                              "SeaHeightMeasure": V("2", "The depth of the intake.", unitCode="MTR"),
                                              "SalinityMeasure": V("30", "Salinity.", unitCode="GL"),
                                              "TransactionDate": V(f.date(10), "At Lumeport."),
                                              "Location": kit.place("XBLMP", "The port."),
                                              "BallastWaterTemperature": {"AttributeID": V("WATER", "The water."),
                                                                          "Measure": V("16", "Its temperature.",
                                                                                       unitCode="CEL")}},
            "ExchangeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."),
                                                "ExchangeMethodCode": V("SEQ", "Emptied and refilled."),
                                                "ExchangedPercent": V("95", "Of the volume."),
                                                "VolumeMeasure": V("310", "Exchanged: the same 310 cubic metres (a volume, so in cubic "
                                                                   "metres; a tonne of water is about a cubic metre).",
                                                   unitCode="MTQ"),
                                                "TransactionDate": V(f.date(11), "At sea, half way across."),
                                                "Location": sea_place},
            "DischargeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."),
                                                 "VolumeMeasure": V("120", "To be discharged at Selanu: 120 cubic metres "
                                                                    "(a volume; a tonne of water is about a cubic "
                                                                    "metre, so the number stays).", unitCode="MTQ"),
                                                 "TransactionDate": V(f.date(SEA_ARRIVES), "In port.")},
            "ResponsibleOfficerPerson": crew[1]},
        "MaritimeHealthDeclaration": {
            "ID": V("MDH-26-0517", "The maritime declaration of health."),
            "InfectiousDiseaseCaseOnBoardIndicator": V("false", "No infectious disease."),
            "MoreIllThanExpectedIndicator": V("false", "No more ill than usual."),
            "MedicalPractitionerConsultedIndicator": V("true", "A doctor was consulted by radio."),
            "StowawaysFoundOnBoardIndicator": V("false", "No stowaways."),
            "SickAnimalOnBoardIndicator": V("false", "No sick animals."),
            "FumigatedCargoTransportIndicator": V("false", "No fumigated cargo."),
            "SanitaryMeasuresAppliedIndicator": V("true", "The galley was disinfected."),
            "ValidSanitationCertificateOnBoardIndicator": V("true", "The certificate is valid."),
            "ReinspectionRequiredIndicator": V("false", "No reinspection needed."),
            "TotalDeadPersonQuantity": qty(0, "IE", "No persons."),
            "TotalIllPersonQuantity": qty(1, "IE", "One person: a crew member with a sprained wrist."),
                        "StowawayDescription": V("None found in the search before departure.", "The search."),
            "LastDrinkingWaterAnalysisDate": V("2026-04-02", "The last water test."),
            "WHOAffectedAreaVisit": {"VisitDate": V("2026-03-28", "No affected area in the last 30 days: the last "
                                                                  "port visited was Lumeport."),
                                     "WHOAffectedAreaPortLocation": kit.place("XBLMP", "Not an affected area.")},
            "PersonnelHealthIncident": {"ID": V("HI-1", "The one incident."),
                                        "JoinedShipDate": V("2025-11-01", "When the person joined."),
                                        "NatureOfIllnessDescription": V("Sprained wrist.", "What happened."),
                                        "OnsetDate": V(f.date(12), "When."),
                                        "ReportedToMedicalOfficerIndicator": V("true", "Reported."),
                                        "GivenTreatmentDescription": V("Bandage and rest.", "Treatment."),
                                        "StillIllIndicator": V("true", "Still recovering."),
                                        "DiedIndicator": V("false", "No."),
                                        "StillOnBoardIndicator": V("true", "On board."),
                                        "EvacuatedIndicator": V("false", "Not evacuated."),
                                        "BuriedAtSeaIndicator": V("false", "No."),
                                        "Note": V("Fit for light duty.", "The status."),
                                        "Person": crew[2]},
            "SanitaryMeasure": {"SanitaryMeasureTypeCode": V("DISINFECT", "The galley was disinfected."),
                                "ApplicationDate": V(f.date(11), "When.")},
            "PlaceOfReportLocation": report_place,
            "MedicalCertificate": {"ID": V("MC-TH-2026", "The ship's medicine chest certificate, unique only with "
                                                         "its issuer, the port health office of its home port "
                                                         "(decision ID-Q10)."),
                                   "CertificateType": V("Medicine chest", "Its kind."),
                                   "IssuerParty": party("16-xb", short=True)},
            "ShipSanitationControlCertificate": {"ID": V("SSCC-XB-2026-0318", "The ship sanitation control "
                                                                              "certificate (International Health "
                                                                              "Regulations, Annex 3), issued at "
                                                                              "Lumeport on 18 March 2026: the "
                                                                              "inspection found traces of cockroaches "
                                                                              "in the galley stores, which were "
                                                                              "treated. It replaced the exemption "
                                                                              "certificate the ship had carried "
                                                                              "until then. Unique only with its "
                                                                              "issuer (decision ID-Q10)."),
                                                 "CertificateType": V("Ship sanitation control", "Its kind."),
                                                 "IssuerParty": party("16-xb", short=True)}},
        "FuelConsumption": {"ID": V("FC-26-19E", "The fuel of the voyage."),
                            "FuelTypeCode": V("MGO", "Marine gas oil."),
                            "FuelType": V("Marine gas oil, 0.1 % sulphur", "In words."),
                            "FuelConsumptionMeasure": V("38", "Used from Lumeport.", unitCode="TNE"),
                            "AdditionalFuelProperty": {"TypeID": V("Sulphur", "The sulphur content."),
                                                       "Value": V("0.1 %", "Its value.")},
                            "FuelMetering": {"TypeID": V("FlowMeter", "Measured by the flow meter."),
                                             "Value": V("38.2 t", "The reading.")},
                            "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2E", "Carbon dioxide."),
                                                      "ValueMeasure": V("122", "From 38 t of gas oil.",
                                                                        unitCode="TNE")},
                            "FuelProviderParty": party("16-xb", short=True)}})
    stage["ISPSRequirements"].update({
        "SSPOnBoardIndicator": V("true", "The security plan is on board."),
        "SSPSecurityMeasuresAppliedIndicator": V("true", "Its measures were applied."),
        "ReportLocation": report_place,
        "ISSCIssuerParty": party("ma-xb", short=True),
        "SecurityOfficerPerson": crew[1],
        "ShipToShipActivityRecord": {
            "ID": V("STS-1", "The ship's one ship-to-ship activity in its last ten calls at port facilities, which "
                             "the security information before arrival lists (SOLAS XI-2, regulation 9)."),
            "Description": V("Bunkering: 120 tonnes of marine gas oil from the Port of Lumeport's bunker barge, "
                             "alongside at the Lumeport anchorage, before the ship berthed.", "What the activity "
                                                                                              "was."),
            "Period": {"StartDate": V(f.date(9), "The day of the bunkering."),
                       "StartTime": V("05:40:00", "The barge made fast."),
                       "EndDate": V(f.date(9), "The same morning."),
                       "EndTime": V("08:15:00", "The barge cast off.")},
            "Location": {"Name": V("Lumeport anchorage", "Where the barge came alongside."),
                         "LocationCoordinate": coordinate(PARTY["16-xb"]["at"])},
            "AppliedSecurityMeasure": {"ID": V("SM-STS-1", "The ship's measure for the transfer, from its security "
                                                           "plan."),
                                       "Description": V("The barge's crew list checked against the bunker order; "
                                                        "access limited to the bunker station, with a deck watch "
                                                        "for the whole transfer.", "What the ship did.")}},
        "AdditionalSecurityMeasure": {"ID": V("SM-1", "An extra measure."),
                                      "Description": V("Gangway watch at Selanu.", "What the ship adds.")},
        "PortCallRecord": {"ID": V("PCR-1", "The last port call."),
                           "SecurityLevelCode": V("1", "Security level 1 at Lumeport."),
                           "SecurityMeasure": {"Description": V("Normal access control.", "The measures.")},
                           "PortFacilityLocation": kit.place("XBLMP", "The port facility."),
                           "Period": {"StartDate": V(f.date(9), "Arrived."), "EndDate": V(f.date(10), "Sailed.")}}})
    tm = out["TransportMeans"]["MaritimeTransport"]
    tm.update({"INFShipClassCode": V("INF1", "Class INF 1 under the IMO INF Code: certified for INF cargo of an "
                                                "aggregate activity below 4,000 TBq only."),
               "AntennaLocus": V("Mast, 28 m above the waterline", "Where the AIS antenna is."),
               "VesselDynamics": {"NavigationStatusCode": V("0", "The AIS navigational status: under way."),
                                  "AtAnchorageIndicator": V("false", "Not at anchor."),
                                  "CourseOverGroundDirection": V("088", "Course over ground, in degrees."),
                                  "SpeedOverGroundMeasure": V("13.5", "Speed over ground.", unitCode="KNT"),
                                  "RateOfTurnMeasure": V("0", "Not turning: 0 degrees per second.", unitCode="E96")}})
    return {}


# ---------------------------------------------------------------- the mast flow (dangerous goods by air)
MAST = kit.Flow("mast", "2026-06-01", [
    {"item": "battery-pack", "ordered": 12, "why": "Twelve modules of 2.4 kWh: four hours of back-up power for the "
                                                   "mast."},
    {"item": "smoke-detector", "ordered": 1, "why": "One pack of ten for the equipment room."},
    {"item": "coating-stripper", "ordered": 5, "why": "Five litres for the circuit boards, in 1-litre tins."}])
MAST_CRATES = 12          # one battery module to a crate (D36)


def dg_contact(why):
    """Saltmere's 24-hour emergency line, the contact for its dangerous goods in transit (D36, mast/02#F19)."""
    desk = PARTY["27-xb"]["identity"]["desks"]["emergency"]
    return {**party("27-xb", short=True),
            "Contact": {"Name": V(desk["name"], why),
                        "Telephone": V(desk["telephone"], "The line answers around the clock, while the goods are "
                                                          "on the way; under the reserved +999."),
                        "Note": V(desk["hours"], "When it answers.")}}


MAST_FLIGHT = ("KXL209", "15:00:00")     # the afternoon flight of Thursday 4 June (D36, D39's timetable)


def mast_uld(serial):
    return f"AKE{serial}{PARTY['12-xl']['identity']['airline_designator']}"


def mast_consignment(f, full):
    """The dangerous goods of the mast flow as handling units (D36, O210): the twelve battery crates on a pallet, the
    stripper's box and the detectors' box. The engineering company's instructions say how they must be stowed
    (full=False, mast/02#F16); the airline's waybill names the containers and their positions on board (full=True).
    No active container: lithium batteries on a flight of under three hours in the island's winter need no
    temperature control (D36 point 3)."""
    bat, det, strip = ITEM["battery-pack"], ITEM["smoke-detector"], ITEM["coating-stripper"]
    crate_gross = Decimal(str(bat["gross_kg"]))

    def transit(it, why_pi, cao_why, extra=None):
        hz = it["hazard"]
        out_ = {"PackingCriteriaCode": V(f"PI{hz['pi']}" + ("IA" if hz["pi"] == "965" else ""), why_pi),
                "HazardousRegulationCode": V("ICA", "Air: the IATA Dangerous Goods Regulations."),
                "TransportAuthorizationCode": V("CAO", cao_why)}
        if extra:
            out_["TransitDescription"] = V(extra, "The conditions, as on the shipper's declaration.")
        return out_

    bat_transit = transit(bat, "IATA packing instruction 965, section IA: lithium ion batteries of more than 100 Wh, "
                               "packed alone.",
                          "Cargo aircraft only: section IA batteries may not fly on passenger aircraft.",
                          "Cargo aircraft only; state of charge below 30 %; each crate within 35 kg.")
    strip_transit = transit(strip, "IATA packing instruction 855, for cargo aircraft (O210).",
                            "Cargo aircraft only: five litres in one package are more than the 1 litre a package of "
                            "this entry may hold on a passenger aircraft (O210).",
                            "Cargo aircraft only; five 1-litre tins in one box.")

    def loaded_item(it, q, unit, gross, net, position, why_pos, hgt=None, extra=None):
        hz = it["hazard"]
        out_ = {"ID": V(f"{it['sellers_id']}-DG", f"The {it['name'].lower()} in the container."),
                "UNDGCode": V(hz["un"][2:], "The UN number."),
                "ProperShippingName": V(hz["name"], "As on the shipper's declaration."),
                "HazardClassID": V(hz["class"], f"Class {hz['class']}.")}
        if extra:
            out_.update(extra)
        if hz.get("pg"):         # no packaging danger level for an entry without packing group (mast/02#F18)
            out_["PackagingDangerLevelCode"] = V(build_examples.PACKAGING_DANGER_LEVEL[hz["pg"]],
                                                 f"The packaging danger level of UN/EDIFACT 8339 that matches the "
                                                 f"packing group {hz['pg']}.")
        out_["GrossWeightMeasure"] = qty(gross, "KGM", "Packed.")
        if net is not None:
            out_["NetWeightMeasure"] = net
        out_.update({"Quantity": qty(q, unit, "As ordered."),
                     "ContactParty": dg_contact("Whom to call in an incident with these goods.")})
        if hgt:
            out_["HazardousGoodsTransit"] = hgt
        out_["PositionOnBoardStowage"] = {"LocationID": V(position, why_pos)}
        return out_

    crates = [{"ID": V(f"SE-CR-{k}", f"Crate {k} of twelve: the engineering company numbers each crate of dangerous "
                                     "goods it packs, so that each can be traced; its own number, without a scheme."),
               "Quantity": qty(1, "EA", "One battery module in the crate."),
               "TraceID": V(f"SE-DL-26-{k:04d}", "The serial number of the data logger fixed to the crate, which "
                                                 "records shocks on the way, for tracing a battery that is damaged."),
               "PackagingTypeCode": V("CR", "UN/ECE Recommendation 21 code CR: crate.")}
              for k in range(1, MAST_CRATES + 1)]
    pallet = {"ID": V("SE-PL-1", "The pallet the twelve crates are strapped to, the engineering company's own "
                                 "number."),
              "Quantity": qty(MAST_CRATES, "EA", "Twelve crates on the pallet."),
              "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
              "ContainedPackage": crates}
    strip_box = {"ID": V("SE-BX-2", "The box of coating stripper, the engineering company's own number."),
                 "Quantity": qty(5, "EA", "Five 1-litre tins in the box."),
                 "PackagingTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box.")}
    det_box = {"ID": V("SE-BX-1", "The box of smoke detectors, the engineering company's own number."),
               "Quantity": qty(1, "EA", "One box: the pack of ten."),
               "PackagingTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box.")}
    lift = (f"Twelve crates of {crate_gross} kg on one pallet: move the pallet by fork-lift; a single crate is a "
            "two-person lift.")
    if not full:
        return {"HazardousRiskIndicator": V("true", "The consignment holds dangerous goods."),
                "HazardousItemNotificationParty": party("27-xb", short=True),
                "TransportHandlingUnit": [
                    {"ID": V("SE-PL-1", "The pallet of battery crates as a handling unit."),
                     "TransportHandlingUnitTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
                     "HandlingInstructions": V(lift + " Stow where the crew can reach it, and not next to "
                                               "packages with a class 3 label.", "How the pallet is handled, and "
                                               "the stowage the airline must give it: what the consignor asks, not "
                                               "the airline's container and position (mast/02#F16)."),
                     "HazardousRiskIndicator": V("true", "Dangerous goods."),
                     "HazardousGoodsTransit": bat_transit,
                     "Package": crates},
                    {"ID": V("SE-BX-2", "The box of stripper as a handling unit."),
                     "TransportHandlingUnitTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box."),
                     "HandlingInstructions": V("Stow where the crew can reach it, and not next to the lithium "
                                               "batteries.", "The stowage asked for (O210)."),
                     "HazardousRiskIndicator": V("true", "Dangerous goods."),
                     "HazardousGoodsTransit": strip_transit,
                     "Package": strip_box},
                    {"ID": V("SE-BX-1", "The box of smoke detectors as a handling unit."),
                     "TransportHandlingUnitTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box."),
                     "HazardousRiskIndicator": V("true", "Dangerous goods: an excepted package, which needs no "
                                                         "particular stowage."),
                     "Package": det_box}]}

    def uld(serial, why, net_door, loaded, package):
        uid = mast_uld(serial)
        return {"ID": V(uid, why),
                "HazardousRiskIndicator": V("true", "Dangerous goods inside."),
                "TransportEquipment": {
                    "ID": V(uid, "The container."),
                    "TransportEquipmentTypeCode": V("UL", "UN/EDIFACT 8053 code UL: unit load device.",
                                                    listID="UN/EDIFACT EDED 8053"),
                    "Description": V("LD3 container with a net door" if net_door else "LD3 container, closed",
                                     "What kind of container: a net door lets the crew see and reach the packages."
                                     if net_door else "A closed container: the packages need no crew access."),
                    "DangerousGoodsApprovedIndicator": V("true", "Loaded with dangerous goods."),
                    "LoadedHazardousItem": loaded},
                "Package": package}

    ake = ("numbered as unit load devices are: its type AKE (an LD3 container), its serial number and the designator "
           "of its owner, the airline (world/parties.json)")
    bat_loaded = loaded_item(
        bat, MAST_CRATES, "EA", MAST_CRATES * crate_gross, qty(MAST_CRATES * Decimal(str(bat["net_kg"])), "KGM",
                                                               "The modules alone."),
        "MD-1", "Main deck, LD3 position 1, at the front, the container's net door facing the crew's access: cargo "
                "aircraft only packages are stowed where the crew can see and reach them.",
        bat_transit, {"HazardousTypeCode": V("ARTICLE", "Batteries are articles, not substances."),
                      "CategoryName": V("Miscellaneous dangerous goods", "Class 9 in words.")})
    bat_loaded["GrossWeightMeasure"] = qty(MAST_CRATES * crate_gross, "KGM",
                                           f"Twelve modules in their crates, {crate_gross} kg each: within the 35 kg "
                                           "a package of packing instruction 965 section IA may weigh on a cargo "
                                           "aircraft, so no approval is needed (D36).")
    bat_loaded["NetVolumeMeasure"] = V("0.24", "The modules' volume: the same cells as the six larger packs first "
                                               "planned.", unitCode="MTQ")
    bat_loaded["Package"] = {"Quantity": qty(1, "EA", "One battery module to a crate; the twelve crates are counted "
                                                      "above and listed with their own numbers in the handling unit "
                                                      "(mast/02#F1)."),
                             "PackagingTypeCode": V("CR", "UN/ECE Recommendation 21 code CR: crate.")}
    strip_loaded = loaded_item(
        strip, 5, "LTR", Decimal(5) * Decimal(str(strip["gross_kg"])), None,
        "MD-3", "Main deck, LD3 position 3, in the crew's reach as well, as cargo aircraft only goods must be; "
                "position 2 between it and the batteries stays empty, because a package with a class 3 label must "
                "not be stowed next to lithium batteries of section IA.", strip_transit)
    det_loaded = loaded_item(
        det, 1, "SET", Decimal(str(det["gross_kg"])), None,
        "MD-6", "Main deck, LD3 position 6, in a closed container: an excepted package of class 7 needs neither crew "
                "access nor segregation from other classes.")
    out = {"HazardousRiskIndicator": V("true", "The consignment holds dangerous goods."),
           "HazardousItemNotificationParty": party("27-xb", short=True),
           "TransportHandlingUnit": [
               {**uld("20513", f"The container of the battery pallet, {ake}.", True, bat_loaded, pallet),
                "HandlingInstructions": V(lift, "How the pallet is handled.")},
               uld("20516", f"The container of the stripper's box, {ake}.", True, strip_loaded, strip_box),
               uld("20514", f"The container of the smoke detectors, {ake}.", False, det_loaded, det_box)]}
    flight, dep = MAST_FLIGHT
    arrives = wmap.hm(wmap.after(wmap.at(f.date(3), dep[:5]), FLIGHT_BLOCK_EAST + 1))
    out["MainCarriageShipmentStage"] = {
        "ID": V("1", "The flight."),
        "TransportModeCode": V("4", "Air transport.", listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
        "HazardousRiskIndicator": V("true", "Dangerous goods on the flight."),
        "TransportMeans": kit.means("12-xl", "KXL", flight, "The afternoon flight of Thursday 4 June, on the "
                                                            "airline's freighter."),
        "LoadingPortLocation": kit.place("XBLMA", "The airport of departure (mast/03#F5)."),
        "UnloadingPortLocation": kit.place("XLSLA", "The airport of destination."),
        "PlannedDepartureTransportEvent": kit.event(f, 3, dep + "-01:00", "The flight's timetabled departure, in "
                                                                          "Lumeport's time, with its offset (D27).", location=kit.place("XBLMA", "The airport of "
                                                                                                    "departure.")),
        "PlannedArrivalTransportEvent": kit.event(f, 3, arrives + "+00:00", "The timetabled arrival, in island time, an hour "
                                                                 "ahead of Lumeport's: a block time of 2 h 45 "
                                                                 "eastbound (D19, D36, O123).",
                                                  location=kit.place("XLSLA", "The airport of destination."))}
    return out


def mast(n, doc):
    f, d = MAST, doc["doc"]
    w = kit.gross_weight(f, "ordered")
    if d == "Order":
        out = kit.order(f, n, doc, 0, "The telecom company orders before the storm season.",
                        "Carriage paid to the telecom company's mast site: the seller arranges the dangerous goods "
                        "transport.", "Selanu Telecom's mast site on Mast Hill")
        out["DeliveryTerms"]["DeliveryLocation"]["Address"] = address("35-xl")    # the named place (mast/01#F8)
        return out
    if d == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The instruction number."),
                "IssueDate": V(f.date(2), "With the shipper's declaration of dangerous goods."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight."),
                             "GoodsItem": [{"ID": V(str(i), "A goods item."),
                                            "Description": V(ITEM[x["item"]]["name"], "The goods."),
                                            "Item": item(x["item"])} for i, x in enumerate(f.deal, 1)],
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment."), **mast_consignment(f, False)}}}
    if d == "Waybill":
        out = kit.waybill(f, n, doc, 3, "The air waybill, cargo aircraft only.", w, "The gross weight.")
        out["IssueTime"] = V("12:15:00", "When the airline accepted the cargo at Lumeport, 11:15 there, before the "
                                         "afternoon flight.")
        kit.deep_merge(out["Shipment"]["Consignment"], mast_consignment(f, True))
        return out
    if d == "DespatchAdvice":
        out = kit.despatch_advice(f, n, doc, 3, "Sent when the goods leave for the airport.", "The gross weight.")
        out["IssueTime"] = V("09:40:00", "When the forwarder's truck left Saltmere's works for the airport, about an "
                                         "hour away.")
        return out
    if d == "Invoice":
        return kit.invoice(f, n, doc, 3, "Issued on despatch.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The telecom company's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}})
    raise SystemExit(f"mast scenario: no document {n} {doc['doc']}")


SCENARIOS["mast"] = _with_enrichment("mast", mast)
FLOWS["mast"] = MAST


# ---------------------------------------------------------------- foreign-currency debit and credit notes
def sea_with_debit(n, doc):
    if doc["doc"] != "DebitNote":
        return sea(n, doc)
    f = SEA
    no = f.number("debit-note", doc["from"], "DebitNote")
    fee, storage = Decimal("38.500"), Decimal("12.750")
    total = fee + storage
    rule = ("O", 0, None, "Lisavu has no sales tax: no tax applies (category O).", None)
    xbl = money(total / Decimal("0.4"), "XBL")
    line = {"ID": V("1", "The inspection."), "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:{no}:1")), "Its "
                                                                                                          "UUID."),
            "Note": V("Customs inspection of the container at Selanu.", "What is charged."),
            "DebitedQuantity": qty(1, "E48", "One inspection."),
            "LineExtensionAmount": amount(total, "XLC", "Inspection and storage, as customs charged them."),
            "TaxInclusiveLineExtensionAmount": amount(total, "XLC", "No tax on the island."),
            "TaxPointDate": V(f.date(16), "The day customs charged the fee."),
            **kit.cost_centre("1-xl", "The buyer's cost centre that paid customs."),
            "PaymentPurposeCode": V("SCVE", "What the payment is for, as an ISO 20022 purpose: services, the inspection and storage recharged to the seller."),
            "FreeOfChargeIndicator": V("false", "Charged."),
            "InvoicePeriod": {"StartDate": V(f.date(14), "The container was held"), "EndDate": V(f.date(15),
                                                                                                "for a day.")},
            "OrderLineReference": {"LineID": V("1", "The benches' order line.")},
            "DespatchLineReference": {"LineID": V("1", "The despatch line."),
                                      "DocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}},
            "ReceiptLineReference": {"LineID": V("1", "The receipt line."),
                                     "DocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice.")}},
            "WorkReportLineReference": {"LineID": V("1", "The inspection report's line."),
                                        "DocumentReference": {"ID": V("XL-CUS-INSP-26-0517", "Customs' inspection "
                                                                                             "report.")}},
            "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The goods' invoice.")}},
            "DocumentReference": {"ID": V("XL-CUS-RCPT-26-0517", "Customs' receipt for the fee.")},
            "PricingReference": {"AlternativeConditionPrice": {"PriceAmount": price(total, "XLC", "The fee as "
                                                                                                  "customs set it.")}},
            "OriginatorParty": party("19-xl", short=True),
            "CollectedForParty": party("19-xl", short=True),
            "PaymentTerms": {"Note": V("Pay within 30 days.", "When.")},
            "TaxTotal": {"TaxAmount": amount(0, "XLC", "No tax.")},
            "AllowanceCharge": {"ChargeIndicator": V("true", "The storage, a charge on the line."),
                                "AllowanceChargeReasonCode": V("WH", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                "AllowanceChargeReason": V("Storage while held", "In words."),
                                "Amount": amount(storage, "XLC", "One day's storage."),
                                "BaseAmount": amount(fee, "XLC", "The inspection fee.")},
            "DeliveryTerms": {"ID": V("CIF", "As the goods were sold.", schemeID="INCOTERMS")},
            "ItemPriceExtension": {"Amount": amount(total, "XLC", "The line's price.")},
            "SubDebitNoteLine": [{"ID": V("1.1", "The inspection fee."),
                                  "LineExtensionAmount": amount(fee, "XLC", "Customs' fee."),
                                  "Item": {"Name": V("Customs inspection fee", "What.")}},
                                 {"ID": V("1.2", "The storage."),
                                  "LineExtensionAmount": amount(storage, "XLC", "One day."),
                                  "Item": {"Name": V("Storage at the port", "What.")}}],
            "Item": {"Name": V("Customs inspection of container " + CONTAINER, "What is debited.")},
            "Price": {"PriceAmount": price(fee, "XLC", "The fee.")}}
    to_xbl = {"SourceCurrencyCode": V("XLC", "The debit note's currency."),
              "TargetCurrencyCode": V("XBL", "The distributor's currency."),
              "CalculationRate": V("2.5", "1 coral = 2.5 lume, the reference rate."),
              "MathematicOperatorCode": V("Multiply", "Coral times the rate gives lume."),
              "Date": V(f.date(18), "The rate of the issue date.")}
    out = {"ID": V(no, "The buyer's debit note number."), "IssueDate": V(f.date(18), "After customs charged the "
                                                                                     "inspection."),
           "DebitNoteTypeCode": V("383", "UN/EDIFACT 1001 code 383: debit note."),
           "DueDate": V(f.date(48), "Thirty days."),
           "Note": V("The illegible mark is the packer's responsibility under the agreement.", "Why the seller "
                                                                                               "pays."),
           "TaxPointDate": V(f.date(16), "The day the fee was charged."),
           "DocumentCurrencyCode": kit.currency_line("XLC", "the buyer's currency, in which customs charged"),
           "TaxCurrencyCode": V("XLC", "No tax, but stated in the island's currency."),
           "PricingCurrencyCode": V("XLC", "The fee is priced in coral."),
           "PaymentCurrencyCode": V("XBL", "The distributor pays in lume."),
           "PaymentAlternativeCurrencyCode": V("XLC", "The amount in coral, for comparison."),
           **kit.cost_centre("1-xl", "The buyer's cost centre."),
           "LineCountNumeric": V("1", "One line."),
           "InvoicePeriod": {"StartDate": V(f.date(14), "Held from discharge"), "EndDate": V(f.date(15), "to "
                                                                                                       "release.")},
           "DiscrepancyResponse": {"ResponseCode": V("2", "A packaging fault."),
                                   "Description": V(f"Heat-treatment mark illegible on pallet "
                                                    f"{kit.unit_id('6-xb', f, 7).value}.", "The fault, with the "
                                                    "pallet's SSCC.")},
           "OrderReference": {"ID": V(f.numbers["order"], "The order.")},
           "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")},
           "DeliveryNoteDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading, the note the goods "
                                                                      "came with.")},
           "WorkReportDocumentReference": {"ID": V("XL-CUS-INSP-26-0517", "Customs' inspection report.")},
           "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice.")},
           "StatementDocumentReference": {"ID": V(f.numbers["statement"], "The factor's statement, which this "
                                                                          "debit does not touch.")},
           "OriginatorDocumentReference": {"ID": V("VT-CLAIM-26-0021", "The buyer's claim.")},
           "ContractDocumentReference": {"ID": V(f.numbers["agreement"], "The digital agreement.")},
           "ProjectReference": {"ID": V(HARBOUR_PROJECT, "The buyer's project number for the harbour parks of "
                                                         "Selanu."),
                                "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:project:harbour-parks")), "Its "
                                                                                                           "UUID."),
                                "IssueDate": V(f.date(3), "Started with the order."),
                                "WorkPhaseReference": {"ID": V("PH-1", "Benches for the harbour park."),
                                                       "WorkPhaseCode": V("SUPPLY", "The supply phase.")}},
           "BuyerAssignedReference": {"BuyerReferenceCode": V("LD-AP-CLAIMS", "The distributor's claims desk.")},
           "PurchaseReference": {"ID": V(CONTAINER, "The container the charge is about.")},
           "Annotation": {"AnnotationContent": V("The distributor may claim it from the packer.", "A remark.")},
           "Signature": seal("1-xl", "VT-SIG-26-DN"),
           "PayeeParty": party("1-xl", short=True),
           "BuyerCustomerParty": {"Party": party("6-xb", short=True)},
           "SellerSupplierParty": {"Party": party("1-xl", short=True)},
           "Delivery": {"ActualDeliveryDate": V(f.date(17), "The goods' arrival at the 3PL.")},
           "DeliveryTerms": {"ID": V("CIF", "As sold.", schemeID="INCOTERMS")},
           "PaymentMeans": kit.payment_means(f, "1-xl", "6-xb", "1-xl", 18, 30, no, "The buyer's account."),
           "PaymentTerms": {"Note": V("30 days net.", "The terms.")},
           "TaxExchangeRate": {**to_xbl, "TargetCurrencyCode": V("XLC", "No conversion: the tax currency is "
                                                                        "coral."),
                               "CalculationRate": V("1", "The same currency.")},
           "PricingExchangeRate": {**to_xbl, "TargetCurrencyCode": V("XLC", "Priced in coral."),
                                   "CalculationRate": V("1", "The same currency.")},
           "PaymentExchangeRate": to_xbl,
           "PaymentAlternativeExchangeRate": {**to_xbl, "TargetCurrencyCode": V("XLC", "The coral equivalent."),
                                              "CalculationRate": V("1", "The same.")},
           "TaxTotal": {"TaxAmount": amount(0, "XLC", "No tax on the island."),
                        "TaxSubtotal": {"TaxableAmount": amount(total, "XLC", "The debit."),
                                        "TaxAmount": amount(0, "XLC", "No tax: the island has no sales tax."),
                                        "TaxCategory": kit.tax_category(rule)}},
           "LegalMonetaryTotal": {"LineExtensionAmount": amount(total, "XLC", "The line."),
                                  "TaxExclusiveAmount": amount(total, "XLC", "No tax."),
                                  "PayableAmount": amount(total, "XLC", f"Payable; {xbl} lume at the rate."),
                                  "PayableAlternativeAmount": amount(xbl, "XBL", "The same in lume.")},
           "DebitNoteLine": line}
    return out


def tender_with_credit(n, doc):
    if doc["doc"] != "CreditNote":
        return tender(n, doc)
    f = TENDER
    rows_spec = [{"item": "bench-serra", "qty": 1, "why": "The bench damaged during installation.",
                  "unit_price": str(kit.unit_price("bench-serra", "XBL")), "unit_price_why": "The contract price in "
                                                                                             "lume.",
                  "line_extra": {"WorkReportLineReference": {"LineID": V("1", "The installation report's line.")},
                                 "InvoicePeriod": {"StartDate": V(f.date(80), "During installation.")},
                                 "TaxPointDate": V(f.date(82), "The day of the credit."),
                                 "FreeOfChargeIndicator": V("false", "A credit, not a free item."),
                                 "DocumentReference": {"ID": V("PWD-DMG-26-0081", "The department's damage "
                                                                                  "report.")},
                                 "PricingReference": {"AlternativeConditionPrice": {
                                     "PriceAmount": price("49900", "XUF", "The contract price in ferra.")}},
                                 "PurchaseReference": {"ID": V("PARK-HB-B17", "The bench's place in the "
                                                                              "harbour park.")},
                                 "OriginatorParty": party("2-xb", short=True),
                                 "BeneficiaryParty": party("2-xb", short=True),
                                 "PaymentTerms": {"Note": V("Set off against the next release's invoice.",
                                                            "How the credit is settled.")},
                                 "SubCreditNoteLine": {"ID": V("1.1", "The frame."),
                                                       "LineExtensionAmount": amount(Decimal("180.00"), "XBL",
                                                                                     "The frame's share."),
                                                       "Item": {"Name": V("Side frames of the bench", "The "
                                                                                                      "damaged "
                                                                                                      "part.")}}}},
                 {"item": "bench-installation", "qty": 1, "why": "Its installation, credited too.",
                  "unit_price": "18.00", "unit_price_why": "The installation price in lume.",
                  "line_extra": {"WithholdingTaxTotal": {"TaxAmount": amount(Decimal("1.80"), "XBL",
                                                                             "The withholding reversed.")},
                                 "CollectedForParty": party("10-xb", short=True)}}]
    out = kit.credit_note(f, n, doc, 82, "Issued when the replacement was agreed.", rows_spec,
                          {"BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The "
                                                                                     "invoice credited.")}}},
                          currency="XBL")
    out.update({"DocumentCurrencyCode": kit.currency_line("XBL", "the currency of the invoice credited"),
                "TaxPointDate": V(f.date(82), "Urvania's VAT: the credit's date."),
                "TaxCurrencyCode": V("XUF", "The manufacturer reports its VAT in ferra."),
                "PricingCurrencyCode": V("XUF", "The contract prices are in ferra."),
                "PaymentCurrencyCode": V("XUF", "Settled in ferra, like the invoice."),
                "InvoicePeriod": {"StartDate": V(f.date(78), "The release."), "EndDate": V(f.date(82), "To the "
                                                                                                      "credit.")},
                "DeliveryNoteDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice of the "
                                                                                 "bench.")},
                "WorkReportDocumentReference": {"ID": V("VI-WR-26-0080", "The installation report.")},
                "PurchaseReference": {"ID": V("PARK-HB", "The harbour park.")},
                "TaxRepresentativeParty": tax_representative(),
                "TaxExchangeRate": {"SourceCurrencyCode": V("XBL", "The credit's currency."),
                                    "TargetCurrencyCode": V("XUF", "The tax currency."),
                                    "CalculationRate": V("100", "1 lume = 100 ferra.")},
                "PricingExchangeRate": PRICING_RATE,
                "PaymentExchangeRate": TO_FERRA(f.date(82)),
                "WithholdingTaxTotal": {
                    "TaxAmount": amount(Decimal("1.80"), "XBL", "The withholding on the credited installation, "
                                                               "reversed."),
                    "TaxSubtotal": {"TaxableAmount": amount(Decimal("18.00"), "XBL", "The installation credited."),
                                    "TaxAmount": amount(Decimal("1.80"), "XBL", "10 % of it, no longer withheld."),
                                    "TaxCategory": {"ID": V("S", "The withholding applies."),
                                                    "Percent": V(WORLD["countries"]["XB"]["tax"]["withholding"]
                                                                 ["percent"], "The rate, as on the invoice."),
                                                    "TaxScheme": withholding_scheme()}}}})
    lmt = out["LegalMonetaryTotal"]
    gross = Decimal(lmt["PayableAmount"].value)
    lmt["WithholdingTaxTotalAmount"] = amount(Decimal("1.80"), "XBL", "The department had withheld this on the "
                                                                      "credited installation; it reclaims it from "
                                                                      "the state.")
    lmt["PayableAmount"] = amount(gross - Decimal("1.80"), "XBL", "What the manufacturer refunds: the credit less the "
                                                                  "tax the department withheld on it.")
    f.numbers["credit-amount"] = gross - Decimal("1.80")
    return out


SCENARIOS["sea"] = _with_enrichment("sea", sea_with_debit)
SCENARIOS["tender"] = _with_enrichment("tender", tender_with_credit)


# ================================================================ public procurement: the shared blocks of the tender
PWD, BOARD, INFO = "2-xb", "28-xb", "21-xb"
EST_BENCHES = Decimal(TENDER_QTY) * Decimal("499.00")
EST_INSTALL = Decimal(TENDER_QTY) * Decimal("18.00")
TENDER_ESTIMATE = Decimal("124800")     # the department's own estimate for the two years (D28 point 2)
TURNOVER_MIN = 2 * TENDER_ESTIMATE / 2  # twice the yearly estimate of 62,400 (D28 point 2)
BRACKENMERE_TURNOVER_2024 = Decimal("6410000.00")   # its accounts for 2024 (D29 point 6)


def lot_ref(lot):
    return {"ID": V(lot, f"Lot {lot[-1]} of the procedure.")}


def procurement_project(f, lot=None):
    """The procurement as a whole, or one lot of it: benches (lot 1) and their installation (lot 2)."""
    goods = lot != "LOT-2"
    est = EST_BENCHES if lot == "LOT-1" else EST_INSTALL if lot == "LOT-2" else EST_BENCHES + EST_INSTALL
    out = {"ID": V(lot or FOLDER, "The project's identifier."),
           "Name": V({"LOT-1": "Park benches", "LOT-2": "Installation of the benches"}.get(lot, "Park benches for the "
                                                                                        "parks renewal programme"),
                     "The project's name."),
           "Description": V("240 park benches with galvanised metal frames and hardwood slats over two years, delivered and anchored.",
                            "What is bought."),
           "ProcurementTypeCode": V("SUPPLIES" if goods else "SERVICES", "Supplies or services."),
           "ProcurementSubTypeCode": V("PURCHASE" if goods else "INSTALL", "The kind within it."),
           "QualityControlCode": V("INSPECTION", "Each release is inspected on delivery."),
           "RequiredFeeAmount": amount(Decimal("50.00"), "XBL", "The fee for the tender documents on paper."),
           "FeeDescription": V("Electronic documents are free; paper copies cost 50 lume.", "The fee."),
           "RequestedDeliveryDate": V(f.date(80), "The first release."),
           "EstimatedOverallContractQuantity": qty(TENDER_QTY, "EA", "240 benches over the contract."),
           "Note": V("Part of the parks renewal programme 2026.", "The programme."),
           "SMESuitableIndicator": V("true", "Small and medium firms can tender."),
           "ProcurementAdditionalType": {"ProcurementTypeCode": V("GREEN", "Green public procurement."),
                                         "ProcurementType": Detail("recycled steel and certified timber are "
                                                                   "asked", "what the green criteria ask for.")},
           "RequestedTenderTotal": {
               "EstimatedOverallContractAmount": amount(est, "XBL", "The estimated value."),
               "EstimatedOverallFrameworkContractsAmount": amount(est, "XBL", "The framework's estimate."),
               "TotalAmount": amount(est, "XBL", "The budget."),
               "TaxIncludedIndicator": V("false", "Without tax: a public body pays no sales tax."),
               "MinimumAmount": amount(est * Decimal("0.5"), "XBL", "At least half will be called off."),
               "MaximumAmount": amount(est * Decimal("1.2"), "XBL", "At most 20 % more."),
               "MonetaryScope": V("Two years of releases.", "What the amount covers."),
               "AverageSubsequentContractAmount": amount(est / 6, "XBL", "Six releases on average."),
               "ApplicableTaxCategory": kit.tax_category(kit.tax_rule("6-xb", PWD, "bench-serra-b"))},
           "MainCommodityClassification": {"ItemClassificationCode": V("38111" if goods else "87390",
                                                                       "What is bought, as a subclass of the UN Central "
                                                                       "Product Classification, which classifies goods "
                                                                       "and services alike: seats with metal frames."
                                                                       if goods else "What is bought, as a subclass of "
                                                                       "the UN Central Product Classification, which "
                                                                       "classifies services as well: installation "
                                                                       "services of other goods.")},
           "AdditionalCommodityClassification": {"ItemClassificationCode": V("381", "The wider category of the "
                                                                             "procurement, as a group of the UN CPC: "
                                                                             "furniture.")},
           "RealizedLocation": {"Name": V("Harbour park and town parks, Lumeport", "Where the benches go."),
                                "Address": {"CityName": V("Lumeport", "The city."),
                                            "Country": {"IdentificationCode": V("XB", "Bayvarra.")}}},
           "PlannedPeriod": {"StartDate": V(f.date(70), "From the first release."),
                             "EndDate": V(f.date(800), "For two years.")},
           "ContractExtension": {"OptionsDescription": V("One extension of a year with 120 more benches.", "The "
                                                                                                           "option."),
                                 "MaximumNumberNumeric": V("1", "At most one."),
                                 "RenewalsIndicator": V("true", "The contract may be renewed."),
                                 "OptionValidityPeriod": {"EndDate": V(f.date(800), "Decided before it ends.")},
                                 "Renewal": {"Amount": amount(est / 2, "XBL", "The value of a renewal."),
                                             "Period": {"DurationMeasure": V("12", "Twelve months.",
                                                                             unitCode="MON")}}}}
    if lot != "LOT-2":
        out["RequestForTenderLine"] = {
            "ID": V("1", "The benches."), "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:{FOLDER}:rftl:1")),
                                                   "Its UUID."),
            "Note": V("Galvanised metal frame, five hardwood slats, ground anchors.", "The requirement."),
            "Quantity": qty(TENDER_QTY, "EA", "Over the contract."),
            "MinimumQuantity": qty(120, "EA", "At least."), "MaximumQuantity": qty(288, "EA", "At most."),
            "TaxIncludedIndicator": V("false", "Prices without tax."),
            "MinimumAmount": amount(Decimal("350"), "XBL", "A unit price below this would be abnormally low."),
            "MaximumAmount": amount(Decimal("600"), "XBL", "The most the budget allows per bench."),
            "EstimatedAmount": amount(EST_BENCHES, "XBL", "The estimate."),
            "DocumentReference": {"ID": V("PWD-SPEC-BENCH-26", "The technical specification.")},
            "DeliveryPeriod": {"StartDate": V(f.date(80), "Releases from."), "EndDate": V(f.date(800), "To.")},
            "RequiredItemLocationQuantity": {"LeadTimeMeasure": V("10", "Ten days per release.", unitCode="DAY")},
            "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
            "Item": {"Name": V("Park bench, 1800 mm", "The item asked for.")},
            "SubRequestForTenderLine": {"ID": V("1.1", "The anchors."), "Quantity": qty(TENDER_QTY, "SET", "One "
                                                                                                         "set per "
                                                                                                         "bench."),
                                        "Item": {"Name": V("Ground anchor set", "Part of the bench.")}}}
    return out


def auction_terms(f, held=False):
    """The electronic auction on the prices, after the full evaluation (the procurement act allows it with the best
    price-quality ratio: the quality scores stay as evaluated). Held on day 53; no tenderer bid lower."""
    text = ("After the full evaluation of the tenders, every tenderer with an admissible tender is invited to an "
            "electronic auction on the unit prices of both lots. The quality scores stay as evaluated; only the "
            "price score changes with the new prices.")
    why = "The terms of the auction for the tenderers."
    if held:
        day = datetime.date.fromisoformat(f.date(53))
        text += (f" The auction was held on {day.day} {day:%B %Y} with both admissible tenderers and closed after "
                 "its first "
                 "round without a new bid, so the prices of the tenders stand.")
        why += " The award notice adds what happened: neither tenderer lowered its price."
    terms = V(text, why)
    return {"AuctionConstraintIndicator": V("true", "An electronic auction is held before the award."),
            "JustificationDescription": V("The benches are a standard product whose quality is fully scored before "
                                          "the auction; the price can then be improved in open competition.",
                                          "Why the department uses an auction."),
            "Description": terms,
            "ProcessDescription": V("One round, opened by an invitation sent two working days ahead. After each bid "
                                    "every tenderer sees its current rank. The round closes when ten minutes pass "
                                    "without a new bid.", "How the auction runs."),
            "ConditionsDescription": V("A bid may only lower the unit prices of the tender, by at least the minimum "
                                       "step of the price criterion; all other terms of the tender stay binding.",
                                       "The conditions for bidding."),
            "ElectronicDeviceDescription": V("The auction module of the department's tender platform, in a current "
                                             "web browser over HTTPS; tenderers log in with the platform account "
                                             "they submitted their tender with.", "The device and how to connect."),
            "AuctionURI": V("https://tenders.lumeport.example/auctions", "The auction module's address.")}


def tendering_process(f, held=False):
    return {"ID": V(f"{FOLDER}-P", "The procedure."), "OriginalContractingSystemID": V("PWD-FW-2024-PARKS", "The "
                                                                                       "framework this one "
                                                                                       "follows."),
            "Description": V("Open procedure with two lots.", "The procedure."),
            "ProcedureCode": V("OPEN", "An open procedure."),
            "ExpenseCode": V("INVESTMENT", "Paid from the investment budget."),
            "PartPresentationCode": V("ONEORMORE", "Tenders for one or both lots."),
            "ContractingSystemCode": V("FRAMEWORK", "A framework agreement."),
            "SubmissionMethodCode": V("ELECTRONIC", "Tenders are submitted electronically."),
            "GovernmentAgreementConstraintIndicator": V("true", "Covered by the trade accord's procurement chapter."),
            "AccessToolsURI": V("https://tenders.lumeport.example/PWD-2026-PARKS", "Where the documents are."),
            "DocumentAvailabilityPeriod": {"StartDate": V(f.date(14), "From the notice."),
                                           "EndDate": V(f.date(44), "Until the day before the deadline.")},
            "TenderSubmissionDeadlinePeriod": {"EndDate": V(f.date(45), "The deadline."),
                                               "EndTime": V("12:00:00", "At noon.")},
            "InvitationSubmissionPeriod": {"StartDate": V(f.date(14), "Invitations from."),
                                           "EndDate": V(f.date(20), "To.")},
            "ParticipationInvitationPeriod": {"StartDate": V(f.date(14), "Participation invited from."),
                                              "EndDate": V(f.date(30), "To.")},
            "ParticipationRequestReceptionPeriod": {"EndDate": V(f.date(30), "Requests to participate by then.")},
            "AdditionalInformationRequestPeriod": {"EndDate": V(f.date(38), "Questions by then.")},
            "NoticeDocumentReference": {"ID": V(f.numbers.get("pin", f"{FOLDER}-PIN"), "The prior information "
                                                                                       "notice.")},
            "AdditionalDocumentReference": {"ID": V("PWD-SPEC-BENCH-26", "The specification.")},
            "ProcessJustification": {"ProcessReasonCode": V("STANDARD", "The open procedure is the rule."),
                                     "ProcessReason": V("Value above the threshold for open procedures.", "Why.")},
            "OpenTenderEvent": {"IdentificationID": V("OPEN-1", "The opening of the tenders."),
                                "OccurrenceDate": V(f.date(45), "The deadline day."),
                                "OccurrenceTime": V("14:00:00", "Two hours after the deadline."),
                                "TypeCode": V("OPENING", "A tender opening."),
                                "Description": V("Electronic opening; tenderers may follow it online.", "How."),
                                "CompletionIndicator": V("false", "To come."),
                                "CurrentStatus": {"ConditionCode": V("SCHEDULED", "Planned.")},
                                "Contact": {"Name": V("Procurement office", "Whom to ask.")},
                                "OccurrenceLocation": {"Name": V("Lumeport Public Works Department, Civic Square",
                                                                 "Where.")}},
            "AuctionTerms": auction_terms(f, held),
            "FrameworkAgreement": {"ExpectedOperatorQuantity": V("1", "One supplier."),
                                   "MaximumOperatorQuantity": V("1", "At most one."),
                                   "Justification": V("Uniform benches across the parks.", "Why one."),
                                   "Frequency": V("Releases every few months.", "How often."),
                                   "EstimatedMaximumValueAmount": amount((EST_BENCHES + EST_INSTALL) * Decimal("1.2"),
                                                                         "XBL", "The estimated maximum."),
                                   "MaximumValueAmount": amount((EST_BENCHES + EST_INSTALL) * Decimal("1.5"), "XBL",
                                                                "With the extension."),
                                   "DurationPeriod": {"DurationMeasure": V("24", "Two years.", unitCode="MON")},
                                   "SubsequentProcessTenderRequirement": {"Name": V("Release order", "Each release "
                                                                                                     "is a call-off "
                                                                                                     "order."),
                                                                          "Description": V("Each release is ordered from the framework "
                                                                                           "supplier at the framework "
                                                                                           "prices, without a new "
                                                                                           "competition.",
                                                                                           "How a release is "
                                                                                           "placed.")}},
            "ContractingSystem": {"ID": V("FW-1", "The framework."),
                                  "ContractingSystemTypeCode": V("FRAMEWORK", "A framework agreement."),
                                  "Description": V("Framework with one supplier.", "In words.")}}


def tendering_terms(f, call=False):
    """The tendering terms of the notices, the call and the contract. Only the contract cites the call for tenders,
    by its own ID: the notices are issued before it, and the call does not cite itself (tender/02#F3, 03#F3, 24#F2,
    C73); no notice replaces another (tender/01#F3, 02#F4, 03#F4, 24#F2)."""
    return {**({"CallForTendersDocumentReference": {"ID": V(f.numbers["call"], "The call for tenders, the "
                                                            "procurement documents the contract was tendered "
                                                            "under.")}} if call else {}),
            "AwardingMethodTypeCode": V("BESTVALUE", "The best price-quality ratio."),
            "PriceEvaluationCode": V("UNITPRICE", "Evaluated on the unit prices."),
            "MaximumVariantQuantity": V("1", "One variant allowed."),
            "VariantConstraintIndicator": V("true", "Variants are allowed."),
            "AcceptedVariantsDescription": V("A bench of recycled plastic slats.", "The variant allowed."),
            "VariantConstraintCode": V("ALLOWED", "As a code."),
            "PriceRevisionFormulaDescription": V("Steel index each January.", "How prices change."),
            "FundingProgramCode": V("PARKS-26", "The programme."),
            "FundingProgram": V("Parks renewal programme 2026", "In words."),
            "MaximumAdvertisementAmount": amount(Decimal("500.00"), "XBL", "The most the winner pays for "
                                                                           "publication."),
            "Note": V("Questions through the platform only.", "How to ask."),
            "PaymentFrequencyCode": V("PERRELEASE", "Payment after each release."),
            "EconomicOperatorRegistryURI": V("https://register.bayvarra.example", "Where tenderers are "
                                                                                  "registered."),
            "RequiredCurriculaIndicator": V("true", "The installers' qualifications are asked."),
            "RequiredCurriculaCode": V("INSTALLERS", "For lot 2."),
            "OtherConditionsIndicator": V("true", "There are other conditions."),
            "RecurringProcurementIndicator": V("true", "The parks are renewed every few years."),
            "RecurringProcurementDescription": V("A next procedure in about four years.", "When."),
            "EstimatedTimingFurtherPublication": V("2030", "The next notice."),
            "AdditionalConditions": V("Benches must carry the maker's serial number.", "A condition."),
            "LatestSecurityClearanceDate": V(f.date(40), "No clearance is needed; the date is the latest for "
                                                         "site access passes."),
            "DocumentationFeeAmount": amount(Decimal("50.00"), "XBL", "For paper documents."),
            "MultipleTendersCode": V("NOTALLOWED", "One tender per tenderer."),
            "PenaltyClause": {"ID": V("PEN-1", "Late delivery."), "Content": V("0.5 % per day late, at most 10 %.",
                                                                              "The penalty.")},
            "RequiredFinancialGuarantee": {"GuaranteeTypeCode": V("TENDER", "A tender guarantee."),
                                           "Description": V("A bank guarantee for the tender.", "What."),
                                           "LiabilityAmount": amount(Decimal("2400.00"), "XBL", "Its amount."),
                                           "AmountRate": V("2", "2 % of the estimated value of 120,000 lume."),
                                           "ConstitutionPeriod": {"EndDate": V(f.date(45), "With the tender.")}},
            "ProcurementLegislationDocumentReference": {"ID": V("XB-PPA-2019", "Bayvarra's public procurement "
                                                                               "act.")},
            "FiscalLegislationDocumentReference": {"ID": V("XB-STT-ACT", "The state sales tax acts.")},
            "EnvironmentalLegislationDocumentReference": {"ID": V("XB-ENV-2021", "The environmental act.")},
            "EmploymentLegislationDocumentReference": {"ID": V("XB-LAB-2018", "The labour act.")},
            "ContractualDocumentReference": {"ID": V("PWD-CONTRACT-DRAFT", "The draft framework contract.")},
            "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
            "PaymentTerms": {"Note": V("30 days after each accepted release.", "The terms.")},
            "TendererQualificationRequest": {
                "CompanyLegalForm": V("Any legal form; consortia must name a lead member.", "The rule on the legal "
                                      "form, in words: any form is accepted, so there is no code to give."),
                "PersonalSituation": V("The tenderer must not be in any of the exclusion situations of the Public "
                                       "Procurement Act, and declares this in its self-declaration.", "What is asked "
                                       "of the tenderer's personal situation."),
                "OperatingYearsQuantity": qty(3, "ANN", "At least three years in business."),
                "EmployeeQuantity": qty(10, "IE", "At least ten employees (persons)."),
                "Description": V("Economic and technical capacity.", "What is asked."),
                "RequiredBusinessClassificationScheme": {"ID": V("ISIC4", "ISIC Rev. 4."),
                                                         "Name": V("ISIC Rev. 4", "The classification."),
                                                         "ClassificationCategory": {"CodeValue": V("3100", "Furniture "
                                                                                                   "manufacture."),
                                                                                    "Name": V("Manufacture of "
                                                                                              "furniture", "In "
                                                                                                           "words.")}},
                "TechnicalEvaluationCriterion": {"EvaluationCriterionTypeCode": V("REFERENCES", "References."),
                                                 "Description": V("Three similar supplies in five years.", "What."),
                                                 "ThresholdQuantity": qty(3, "EA", "Three."),
                                                 "DurationPeriod": {"DurationMeasure": V("5", "Five years.",
                                                                                         unitCode="ANN")},
                                                 "SuggestedEvidence": {"ID": V("EV-REF", "Reference letters."),
                                                                       "Name": V("References", "What.")}},
                "FinancialEvaluationCriterion": {"EvaluationCriterionTypeCode": V("TURNOVER", "Turnover."),
                                                 "Description": V("Yearly turnover of at least twice the "
                                                                  "estimate.", "What."),
                                                 "ThresholdAmount": amount(Decimal("250000"), "XBL", "The minimum."),
                                                 "ExpressionCode": V("GT", "As a rule."),
                                                 "Expression": V("Turnover > 2 × estimate", "The formula.")},
                "SpecificTendererRequirement": {"Name": V("Certified timber", "The requirement."),
                                                "TendererRequirementTypeCode": V("ENVIRONMENTAL", "Its kind."),
                                                "Description": V("Slats from forests managed for regrowth.", "What."),
                                                "LegalReference": V("XB-ENV-2021 art. 12", "The rule."),
                                                "SuggestedEvidence": {"ID": V("EV-FOR", "A forestry certificate."),
                                                                      "Name": V("Forestry certificate", "What.")}},
                "EconomicOperatorRole": {"RoleCode": V("LEAD", "The lead tenderer."),
                                         "RoleDescription": V("Leads a consortium.", "In words.")}},
            "AllowedSubcontractTerms": {"Rate": V("30", "Up to 30 % subcontracted."),
                                        "UnknownPriceIndicator": V("false", "The subcontracting share is known."),
                                        "Description": V("Installation may be subcontracted.", "What."),
                                        "Amount": amount(EST_INSTALL, "XBL", "Lot 2's value."),
                                        "SubcontractingConditionsCode": V("ALLOWED", "As a code."),
                                        "MaximumPercent": V("30", "At most.")},
            "TenderPreparation": {"TenderEnvelopeID": V("ENV-1", "One envelope."),
                                  "TenderEnvelopeTypeCode": V("COMBINED", "Technical and price together."),
                                  "Description": V("One encrypted envelope per tender.", "How."),
                                  "OpenTenderID": V("OPEN-1", "Opened at the opening."),
                                  "ProcurementProjectLot": {"ID": V("LOT-1", "For lot 1 and lot 2 alike.")},
                                  "DocumentTenderRequirement": {"Name": V("Price schedule", "A document to submit."),
                                                                "Description": V("Unit prices per lot.", "What."),
                                                                "TemplateDocumentReference": {
                                                                    "ID": V("PWD-PRICE-TPL", "The template.")}},
                                  "TenderEncryptionData": {
                                      "MessageFormat": V("CMS", "Cryptographic Message Syntax."),
                                      "EncryptionCertificateAttachment": {"ExternalReference": {
                                          "URI": V("https://tenders.lumeport.example/cert.pem", "The certificate.")}},
                                      "EncryptionCertificatePathChain": {"Value": V("PWD-CA > PWD-TENDER", "The "
                                                                                                           "chain."),
                                                                         "URI": V("https://tenders.lumeport.example/"
                                                                                  "chain.pem", "Where.")},
                                      "EncryptionSymmetricAlgorithm": {"ID": V("AES-256-GCM", "The algorithm."),
                                                                       "OID": V("2.16.840.1.101.3.4.1.46", "Its "
                                                                                                           "OID.")}}},
            "ContractExecutionRequirement": {"Name": V("Recycled steel", "A condition of execution."),
                                             "ExecutionRequirementCode": V("ENVIRONMENTAL", "Its kind."),
                                             "Description": V("At least 30 % recycled steel in the frames.",
                                                              "What.")},
            "AwardingTerms": {
                "WeightingAlgorithmCode": V("WSUM", "A weighted sum."),
                "Description": V("Price 60 %, quality 40 %.", "The award."),
                "TechnicalCommitteeDescription": V("Three officers of the department.", "Who evaluates."),
                "LowTendersDescription": V("Prices 30 % below the average are examined.", "Abnormally low."),
                "PrizeIndicator": V("false", "Not a design contest: no prizes."),
                "FollowupContractIndicator": V("false", "No follow-up contract."),
                "BindingOnBuyerIndicator": V("true", "The evaluation binds the buyer."),
                "NoFurtherNegotiationIndicator": V("true", "No negotiation after the award."),
                "AwardingCriterion": [
                    {"ID": V("AC-1", "Price."), "AwardingCriterionTypeCode": V("PRICE", "Its kind."),
                     "Name": V("Price", "Name."), "Description": V("The lowest total of unit prices.", "How."),
                     "WeightNumeric": V("60", "Weight."), "Weight": V("60 %", "In words."),
                     "CalculationExpression": V("60 × lowest / tendered", "The formula."),
                     "CalculationExpressionCode": V("INVERSE", "As a code."),
                     "MinimumAmount": amount(Decimal("350"), "XBL", "Unit price at least."),
                     "MaximumAmount": amount(Decimal("600"), "XBL", "At most."),
                     "MinimumImprovementBid": V("In the electronic auction, each new bid lowers the bench's unit "
                                                "price by at least 2 lume.", "The minimum step of a bid on the "
                                                                             "price.")},
                    {"ID": V("AC-2", "Quality."), "AwardingCriterionTypeCode": V("QUALITY", "Its kind."),
                     "Name": V("Quality", "Name."), "WeightNumeric": V("40", "Weight."),
                     "MinimumQuantity": qty(5, "ANN", "Warranty of at least five years."),
                     "MaximumQuantity": qty(10, "ANN", "Up to ten years counts."),
                     "SubordinateAwardingCriterion": {"ID": V("AC-2.1", "Durability."),
                                                      "Name": V("Durability of the coating", "Name."),
                                                      "WeightNumeric": V("20", "Half of quality.")}}],
                "TechnicalCommitteePerson": kit.person("Mara", "Delling", "The head of parks on the committee.",
                                                       job="Head of parks"),
},
            "AdditionalInformationParty": party(PWD, short=True),
            "DocumentProviderParty": party(PWD, short=True),
            "TenderRecipientParty": party(PWD, short=True),
            "ContractResponsibleParty": party(PWD, short=True),
            "TenderEvaluationParty": party(PWD, short=True),
            "QualificationRequestRecipientParty": party(PWD, short=True),
            "TenderValidityPeriod": {"DurationMeasure": V("90", "Tenders hold for 90 days.", unitCode="DAY")},
            "ContractAcceptancePeriod": {"DurationMeasure": V("10", "The standstill: ten days.", unitCode="DAY")},
            "AppealTerms": {"Description": V("Appeals to the review board within ten days of the award.", "How."),
                            "PresentationPeriod": {"DurationMeasure": V("10", "Ten days.", unitCode="DAY")},
                            "AppealInformationParty": party(BOARD, short=True)},
            "Language": {"ID": V("en", "English."), "Name": V("English", "In words."),
                         "LocaleCode": V("en-XB", "Bayvarran English, the city's.")},
            "BudgetAccountLine": {"ID": V("BL-PARKS-26", "The budget line."),
                                  "TotalAmount": amount(EST_BENCHES + EST_INSTALL, "XBL", "Its amount."),
                                  "BudgetAccount": {"ID": V("4.2.110", "The city's budget account."),
                                                    "BudgetYearNumeric": V("2026", "The budget year."),
                                                    "RequiredClassificationScheme": {
                                                        "ID": V("LUM-BUDGET", "The city's budget classification."),
                                                        "ClassificationCategory": {"CodeValue": V("4.2", "Parks and "
                                                                                                         "green "
                                                                                                         "spaces."),
                                                                                   "Name": V("Parks", "In words.")}}}},
            "LotDistribution": {"MaximumLotsAwardedNumeric": V("2", "Both lots to one tenderer if best."),
                                "MaximumLotsSubmittedNumeric": V("2", "Tenders for both lots allowed."),
                                "GroupingLots": V("Lots 1 and 2 may be awarded together.", "The grouping."),
                                "LotsGroup": {"LotsGroupID": V("G-1", "The group."),
                                              "ProcurementProjectLotReference": [lot_ref("LOT-1"),
                                                                                 lot_ref("LOT-2")]}},
            "PostAwardProcess": {"ElectronicCatalogueUsageIndicator": V("true", "A catalogue of the benches."),
                                 "ElectronicInvoiceAcceptedIndicator": V("true", "Invoices in UBL."),
                                 "ElectronicOrderUsageIndicator": V("true", "Call-offs as UBL orders."),
                                 "ElectronicPaymentUsageIndicator": V("true", "Paid by transfer.")},
            "SecurityClearanceTerm": {"Code": V("NOTREQUIRED", "No security clearance."),
                                      "Description": V("Parks are public places.", "Why.")}}


def procurement_lots(f):
    def lot(lid):
        return {"ID": V(lid, f"Lot {lid[-1]}."),
                "LegalDocumentReference": {"ID": V("XB-PPA-2019", "The procurement act.")},
                "TechnicalDocumentReference": {"ID": V(f"PWD-SPEC-{lid}", "The lot's specification.")},
                "RequiredDocumentReference": {"ID": V("PWD-PRICE-TPL", "The price schedule to submit.")},
                "ProvidedDocumentReference": {"ID": V("PWD-SITE-PLAN", "The parks' site plan.")},
                "AdditionalDocumentReference": {"ID": V("PWD-QA-26", "Questions and answers.")},
                "TenderingTerms": {"Note": V("As for the procedure.", "The lot's terms.")},
                "TenderingProcess": {"Description": V("As for the procedure.", "The lot's process.")},
                "ProcurementProject": procurement_project(f, lid)}
    return [lot("LOT-1"), lot("LOT-2")]


def notice_head(f, kind, code, urvanian=True):
    return {"VersionID": V("1", "The first version."),
            "RequestedPublicationDate": V(out_day(f, kind), "When to publish."),
            "RegulatoryDomain": V("Bayvarra public procurement", "The rules the notice follows."),
            "NoticeTypeCode": V(code, "The kind of notice."),
            "NoticeLanguageCode": V("en", "In English, as an ISO 639 code."),
            **({"AdditionalNoticeLanguage": {"ID": V("qau", "Also published in Urvanian, for tenderers from Urvania: the "
                                                         "notice gives its note and the project's name and description "
                                                         "in Urvanian too (a code from ISO 639's local-use range: the "
                                                         "world's languages are invented; tender/01#F14)."),
                                         "Name": V("Urvanian", "The language's name.")}} if urvanian else {}),
            "Signature": seal(PWD, f"PWD-SIG-{kind}"),
            "OriginatorCustomerParty": {"Party": party("2-xb", short=True)},
            "BeneficiaryParty": party("2-xb", short=True)}



def with_urvanian(block, *keys):
    """The texts of a notice published in Urvanian too (its AdditionalNoticeLanguage): each in English and in
    Urvanian, with its languageID (tender/01#F14, 02#F18)."""
    for k in keys:
        v = block[k]
        block[k] = [V(v.value, v.why, languageID="en"),
                    V(build_examples.translate(v.value, "qau"), f"The same in Urvanian, the notice's additional "
                      f"language: {v.why}", languageID="qau")]
    return block


def out_day(f, kind):
    return f.date({"PIN": 1, "CN": 15, "CAN": 61}[kind])


def contracting_party_details():
    return {"BuyerProfileURI": V("https://tenders.lumeport.example/buyers/pwd", "The buyer's profile."),
            "ContractingPartyType": {"PartyTypeCode": V("LOCAL", "A local authority."),
                                     "PartyType": Detail("a department of the city of Lumeport",
                                                         "the buyer is the city's parks department.")},
            "ContractingActivity": {"ActivityTypeCode": V("COMMUNITY", "Its activity."),
                                    "ActivityType": Detail("public works and parks", "the department's "
                                                                                       "field.")},
            "ContractingRepresentationType": {"RepresentationTypeCode": V("OWN", "On its own behalf."),
                                              "RepresentationType": V("Buys for itself", "In words.")}}


@enrich("tender", "PriorInformationNotice")
def _(f, n, doc, out):
    f.numbers["pin"] = out["ID"].value if "ID" in out else f"{FOLDER}-PIN"
    head = with_urvanian({**notice_head(f, "PIN", "PIN"), "Note": V("Advance notice of the bench procedure.",
                                                                     "What.")}, "Note")
    return {**head,
            "PlannedDate": V(f.date(14), "The contract notice is planned for then."),
            "DocumentReference": {"ID": V("PWD-PARKS-PLAN-26", "The parks plan.")},
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f),
            "TenderingProcess": {"ProcedureCode": V("OPEN", "An open procedure is planned."),
                                 "Description": V("Planned as an open procedure in two lots.", "What is planned.")},
            "ProcurementProject": with_urvanian(procurement_project(f), "Name", "Description"),
            "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1, planned."), "ProcurementProject": project_brief("LOT-1")},
                                      {"ID": V("LOT-2", "Lot 2, planned."),
                                       "ProcurementProject": project_brief("LOT-2")}]}


@enrich("tender", "ContractNotice")
def _(f, n, doc, out):
    head = with_urvanian({**notice_head(f, "CN", "CN"), "Note": V("Open procedure in two lots.", "What.")}, "Note")
    return {**head,
            "FrequencyPeriod": {"DurationMeasure": V("4", "Notices like this about every four years.",
                                                     unitCode="ANN")},
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f), "TenderingProcess": tendering_process(f),
            "ProcurementProject": with_urvanian(procurement_project(f), "Name", "Description"),
            "ProcurementProjectLot": procurement_lots(f)}


@enrich("tender", "CallForTenders")
def _(f, n, doc, out):
    return {"ApprovalDate": V(f.date(13), "Approved by the department's head."),
            "Note": V("The documents of the procedure.", "What."), "VersionID": V("1", "The first version."),
            "LegalDocumentReference": {"ID": V("PWD-LEGAL-26", "The legal conditions.")},
            "TechnicalDocumentReference": {"ID": V("PWD-SPEC-BENCH-26", "The specification.")},
            "RequiredDocumentReference": {"ID": V("PWD-PRICE-TPL", "The price schedule.")},
            "ProvidedDocumentReference": {"ID": V("PWD-SITE-PLAN", "The site plan.")},
            "AdditionalDocumentReference": {"ID": V("PWD-QA-26", "Questions and answers.")},
            "Signature": seal(PWD, "PWD-SIG-CFT"),
            "OriginatorCustomerParty": {"Party": party("2-xb", short=True)},
            "BeneficiaryParty": party("2-xb", short=True),
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f),
            "TenderingProcess": {**tendering_process(f), "NoticeDocumentReference": [
                {"ID": V(f.numbers["pin"], "The prior information notice.")},
                {"ID": V(f.numbers["notice"], "The contract notice the call belongs to (tender/03#F44).")}]},
            "ProcurementProject": procurement_project(f), "ProcurementProjectLot": procurement_lots(f)}


TENDERED_BENCH = {
    "5-xu": {"name": "Park bench Serra 180", "note": "Serra 180, as specified.", "sheet": "VI-DS-B180",
             "spare": "VI-C180-2026", "spare_why": "Spare frames available."},
    "37-xb": {"name": "Park bench Brackenmere PB-2", "note": "A bench of its own make: steel frame, hardwood slats.",
              "sheet": "BF-DS-PARK", "spare": "BF-SLAT-PB2", "spare_why": "Spare slat sets available."}}


def tender_lines(f, bench_price, install_price, tenderer="5-xu"):
    t = TENDERED_BENCH[tenderer]
    b = Decimal(bench_price) * TENDER_QTY
    i = Decimal(install_price) * TENDER_QTY
    return b, i, [
        {"ID": V("1", "The benches."), "Note": V(t["note"], "What is offered."),
         "Quantity": qty(TENDER_QTY, "EA", "240 benches."),
         "LineExtensionAmount": amount(b, "XBL", "240 at the unit price."),
         "TaxInclusiveLineExtensionAmount": amount(b, "XBL", "No tax for a public body."),
         "TotalTaxAmount": amount(0, "XBL", "No tax for a public body."),
         "OrderableUnit": V("Pallet of 4", "Called off in pallets."),
         "ContentUnitQuantity": qty(4, "EA", "Four per pallet."),
         "OrderQuantityIncrementNumeric": V("4", "In steps of four."),
         "MinimumOrderQuantity": qty(20, "EA", "A release of at least 20."),
         "MaximumOrderQuantity": qty(96, "EA", "At most a full truck."),
         "WarrantyInformation": V("Five years on the frame.", "The warranty."),
         "PackLevelCode": V("PALLET", "The pack level."),
         "DocumentReference": {"ID": V(t["sheet"], "The datasheet.")},
         "Item": {"Name": V(t["name"], "The item offered.")},
         "OfferedItemLocationQuantity": {"LeadTimeMeasure": V("7", "Seven days per release.", unitCode="DAY")},
         "WarrantyParty": party(tenderer, short=True),
         "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
         "SubTenderLine": {"ID": V("1.1", "The anchors."), "Quantity": qty(TENDER_QTY, "SET", "One set per bench."),
                           "Item": {"Name": V("Ground anchor set", "Included.")}},
         "CallForTendersLineReference": {"LineID": V("1", "The line of the call for tenders.")},
         "CallForTendersDocumentReference": {"ID": V(f.numbers["call"], "The call for tenders.")}},
        {"ID": V("2", "The installation."), "Quantity": qty(TENDER_QTY, "EA", "240 installations."),
         "LineExtensionAmount": amount(i, "XBL", "240 at the price."),
         "Item": {"Name": V("Installation of a park bench", "The service.")}}]


@enrich("tender", "Tender")
def _(f, n, doc, out):
    winner = doc["from"] == "5-xu"
    k = nth("tender", n, doc)
    bench = "499.00" if winner else ("470.00" if k == 1 else "480.00")
    b, i, lines = tender_lines(f, bench, "18.00" if winner else "16.00", doc["from"])
    return {"TenderTypeCode": V("COMBINED", "Technical and financial in one."),
            "ContractName": V("Park benches for the parks renewal programme", "The contract tendered for."),
            "Note": V("Tender for both lots." if winner else "Tender for both lots, with a bench of the furniture "
                                                             "maker's own make." + (" It corrects the price per "
                                                             "bench of the withdrawn tender." if k == 2 else ""),
                      "What is offered."),
            "ValidityPeriod": {"DurationMeasure": V("90", "Valid for 90 days.", unitCode="DAY")},
            "CallForTenderDocumentReference": {"ID": V(f.numbers["call"], "The call for tenders, by its ID "
                                                                         "(tender/15#F1, 17#F1, 19#F4).")},
            "DocumentReference": {"ID": V("VI-DS-B180" if winner else "BF-DS-PARK", "The datasheet.")},
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TENDER-{n}"),
            # each tenderer cites its own qualification, issued before its tender (tender/17#F2, 19#F2, C72)
            "TendererQualificationDocumentReference": {"ID": V(f.numbers["qualification"], "The qualification "
                                                               "documents.")} if winner else
            {"ID": V(f.numbers["qar-response"], "The furniture maker's response to the qualification "
                                                "questionnaire, which qualifies it."),
             "DocumentTypeCode": V("QualificationApplicationResponse", "The kind of document: the response to the "
                                   "qualification questionnaire, the furniture maker's qualification.")},
            "OriginatorCustomerParty": {"Party": party(PWD, short=True)},
            "BeneficiaryParty": party(PWD, short=True),
            "TenderedProject": {
                "VariantID": V("V0", "The main offer; no variant is tendered."),
                "FeeAmount": amount(Decimal("50.00"), "XBL", "The documentation fee paid."),
                "FeeDescription": V("Paper copy of the documents.", "What the fee was for."),
                "TenderEnvelopeID": V("ENV-1", "The envelope."),
                "TenderEnvelopeTypeCode": V("COMBINED", "Technical and price together."),
                "AdditionalFee": {"FeeTypeCode": V("COURIER", "A courier fee."),
                                  "FeeAmount": amount(Decimal("12.00"), "XBL", "For the signed originals."),
                                  "FeeDescription": V("Courier of the guarantee's original.", "What.")},
                "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")}, {"ID": V("LOT-2", "Lot 2.")}],
                "EvidenceDocumentReference": {"ID": V("VI-REF-2025" if winner else "BF-REF-2025",
                                                      "The tenderer's own reference letters.")},
                "TaxTotal": {"TaxAmount": amount(0, "XBL", "No tax for a public body.")},
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(b + i, "XBL", "Both lots."),
                                       "PayableAmount": amount(b + i, "XBL", "The tender's total.")},
                "TenderLine": lines,
                "AwardingCriterionResponse": {
                    "ID": V("ACR-1", "The response to the quality criterion."),
                    "AwardingCriterionID": V("AC-2", "Quality."),
                    "AwardingCriterionDescription": V("Warranty and coating.", "The criterion."),
                    "Description": V("Ten years on the coating." if winner else "Six years on the frame and the slats.",
                                     "The offer."),
                    "Quantity": qty(10 if winner else 6, "ANN", "The years of warranty offered."),
                    "Amount": amount(b + i, "XBL", "The price offered."),
                    "SubordinateAwardingCriterionResponse": {"ID": V("ACR-1.1", "Durability."),
                                                             "AwardingCriterionID": V("AC-2.1", "Its criterion."),
                                                             "Description": V("Hot-dip galvanised and powder "
                                                                              "coated." if winner else
                                                                              "Oiled hardwood, painted steel.",
                                                                              "The offer.")}}}}


@enrich("tender", "QualificationApplicationRequest")
def _(f, n, doc, out):
    """The self-declaration asks exactly what the notices and the call announce, each limit once and in the element
    of its data type (D29 point 11; tender/06#F4 to F8, F13 to F16): the exclusion grounds, enrolment in a register,
    years in business, the yearly turnover, staff, three similar supplies, certified timber, and a group's shares."""
    def prop(pid, name, what, dtype, **x):
        return {"ID": V(pid, "The question."), "Name": V(name, "Its name."), "Description": V(what, "What to answer."),
                "TypeCode": V("QUESTION", "A question the tenderer answers (tender/06#F15)."),
                "ValueDataTypeCode": V(dtype, "The kind of answer it takes."), **x}

    def crit(cid, kind, name, what, props, **x):
        return {"ID": V(cid, "The criterion."), "CriterionTypeCode": V(kind, "Its kind."),
                "Name": V(name, "The criterion."), "Description": V(what, "What it asks."),
                "EvaluationMethodTypeCode": V("PASSFAIL", "Met or not; the request states no fulfilment, since "
                                                          "nobody has answered yet (tender/06#F5)."),
                **x,
                "TenderingCriterionPropertyGroup": {
                    "ID": V(f"PG-{cid[3:]}", "The questions of the criterion."),
                    "PropertyGroupTypeCode": V("ON", "Always answered: no indicator comes before it (tender/06#F14)."),
                    "Description": V(f"The questions on {name[0].lower() + name[1:]}.", "What the group asks."),
                    **({"FulfilmentIndicatorTypeCode": V("ALL", "Both questions must be answered and met.")}
                       if isinstance(props, list) else {}),
                    "TenderingCriterionProperty": props}}
    act = lambda art, what: {"ID": V("XB-PPA-2019", "Bayvarra's Public Procurement Act."),
                             "Title": V("Public Procurement Act", "Its title."), "Description": V(what, "What."),
                             "Article": V(art, "The article.")}
    convictions = contest_exclusion_criteria()[0]
    taxes = crit("CR-TAXES", "EXCLUSION", "Payment of taxes and social security contributions",
                 "A tenderer that has not paid its taxes or social security contributions is excluded, unless only "
                 "minor amounts are unpaid.",
                 prop("P-TAXES-1", "Unpaid taxes and contributions", "The amount of taxes and social security "
                      "contributions due and unpaid.", "AMOUNT", ValueCurrencyCode=V("XBL", "In lume."),
                      MaximumAmount=amount(Decimal("1000"), "XBL", "Arrears up to 1,000 lume count as minor amounts "
                                                                  "and do not exclude the tenderer.")),
                 Legislation=act("Art. 57", "Exclusion grounds; the exception for minor amounts."))
    register = crit("CR-REGISTER", "SUITABILITY", "Enrolment in a business register",
                    "The tenderer is entered in the business register of the country where it is established.",
                    prop("P-REGISTER-1", "Registered in a business register", "Whether the tenderer is entered in "
                         "a business register.", "INDICATOR",
                         ExpectedIndicator=V("true", "Only one answer meets the criterion: yes."),
                         ExpectedDescription=V("Entered in the national business register of the tenderer's "
                                               "country.", "What a yes means; the register's address goes to the "
                                               "evidence, not to an expected identifier (tender/06#F7)."),
                         TranslationTypeCode=V("NONE", "An extract in another language is accepted as it is."),
                         CertificationLevelDescription=V("A plain extract will do.", "The level."),
                         CopyQualityTypeCode=V("COPY", "A copy is enough.")),
                    Legislation=act("Art. 58", "Selection criteria: suitability to pursue the activity."))
    years = crit("CR-YEARS", "ECONOMIC", "Years in business",
                 "At least three full years in business, as the notices ask.",
                 prop("P-YEARS-1", "Years in business", "The full years since the tenderer was founded.",
                      "QUANTITY", ValueUnitCode=V("ANN", "Years."),
                      MinimumQuantity=qty(3, "ANN", "At least three years, stated once, as a quantity "
                                                    "(tender/06#F16).")))
    turnover = crit("CR-TURNOVER", "ECONOMIC", "Yearly turnover",
                    f"A yearly turnover of at least {TURNOVER_MIN:,} lume, twice the yearly estimate of "
                    f"{TENDER_ESTIMATE / 2:,.0f} lume, in the last financial year for which accounts are filed.",
                    prop("P-TURNOVER-1", "Yearly turnover", "The turnover of the last financial year for which "
                         "accounts are filed.", "AMOUNT", ValueCurrencyCode=V("XBL", "In lume."),
                         MinimumAmount=amount(TURNOVER_MIN, "XBL", "At least, as in the notices: greater than or "
                                                                   "equal (D28 point 2, tender/06#F13)."),
                         ApplicablePeriod={"StartDate": V("2024-01-01", "The last financial year whose accounts "
                                                                        "are filed by the tender deadline"),
                                           "EndDate": V("2024-12-31", "(accounts for 2025 are filed from April).")},
                         TemplateEvidence={"ID": V("EV-ACC", "The evidence asked."),
                                           "Name": V("Annual accounts", "Evidence.")}),
                    ProcurementProjectLotReference=lot_ref("LOT-1"),
                    CommodityClassification={"ItemClassificationCode": V("38111", "The benches, as a subclass of "
                                                                                  "the UN Central Product "
                                                                                  "Classification: seats with metal "
                                                                                  "frames.")},
                    Legislation={**act("Art. 58", "Selection criteria: economic and financial standing."),
                                 "JurisdictionLevel": V("National", "The level."),
                                 "URI": V("https://law.bayvarra.example/ppa", "Where."),
                                 "Language": {"ID": V("en", "English.")},
                                 "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V("XB",
                                                                                                    "Bayvarra.")}}})
    staff = crit("CR-STAFF", "TECHNICAL", "Staff", "At least ten employees, as the notices ask.",
                 prop("P-STAFF-1", "Employees", "The number of persons employed.", "QUANTITY",
                      ValueUnitCode=V("IE", "Persons."), MinimumQuantity=qty(10, "IE", "At least ten.")))
    references = crit("CR-REFERENCES", "TECHNICAL", "Similar supplies",
                      "Three supplies of park benches or similar street furniture in the last five years, as the "
                      "notices ask.",
                      [prop("P-REFERENCES-1", "The supplies", "Each supply: the customer, the year, what was "
                            "supplied and its value.", "DESCRIPTION"),
                       prop("P-REFERENCES-2", "Number of supplies", "How many such supplies.", "QUANTITY",
                            ValueUnitCode=V("EA", "Supplies."), MinimumQuantity=qty(3, "EA", "At least three."))])
    timber = crit("CR-TIMBER", "TECHNICAL", "Certified timber",
                  "The slats come from forests managed for regrowth, with a forestry certificate valid for the "
                  "contract, as the call asks.",
                  prop("P-TIMBER-1", "Forestry certificate", "Whether the timber of the slats is covered by a "
                       "forestry certificate valid for the two years of the contract.", "INDICATOR",
                       ExpectedIndicator=V("true", "Only one answer meets the criterion: yes.")),
                  Legislation=act("Art. 70", "Environmental requirements of the specification (XB-ENV-2021 "
                                             "art. 12)."))
    group = {"ID": V("CR-GROUP", "The criterion on the tenderer's composition."),
             "CriterionTypeCode": V("SUITABILITY", "Who tenders."),
             "Name": V("Tendering as a group", "The criterion."),
             "Description": V("A group of tenderers names its members and the share of each (tender/06#F4).", "What."),
             "EvaluationMethodTypeCode": V("PASSFAIL", "Answered or not."),
             "TenderingCriterionPropertyGroup": {
                 "ID": V("PG-GROUP", "The question whether a group tenders."),
                 "PropertyGroupTypeCode": V("ON", "Always answered."),
                 "TenderingCriterionProperty": prop("P-GROUP-1", "A group", "Whether the tenderer tenders as a "
                                                    "member of a group.", "INDICATOR"),
                 "SubsidiaryTenderingCriterionPropertyGroup": {
                     "ID": V("PG-GROUP-1", "The questions for a group."), "Name": V("Group", "Name."),
                     "PropertyGroupTypeCode": V("ONTRUE", "Answered only when the indicator before it is yes: a "
                                                          "group tenders (tender/06#F14)."),
                     "TenderingCriterionProperty": prop("P-GROUP-2", "Share in the group", "The share of the "
                                                        "work of each member, in per cent.", "PERCENT")}}}
    return {"ContractName": V("Park benches for the parks renewal programme", "The contract."),
            "VersionID": V("1", "The first version."),
            "ProcedureCode": V("OPEN", "An open procedure."),
            "QualificationApplicationTypeCode": V("REGULATED", "The regulated form of self-declaration."),
            "WeightScoringMethodologyNote": V("Pass or fail; no weighting.", "How answers count."),
            "WeightingTypeCode": V("NONE", "No weighting."),
            "Note": V("Answer every criterion.", "What to do."),
            "ProcurementProject": {"ID": V(FOLDER, "The procedure.")},
            "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["call"], "The call for tenders, sent with this "
                                                                      "request (tender/06#F1).")},
            "Signature": seal(PWD, "PWD-SIG-QAR"),
            "TenderingCriterion": [convictions, taxes, register, years, turnover, staff, references, timber, group]}


def company_years(pid, on):
    """Full years in business on a day, from the founding date in the party's identity (world/parties.json)."""
    founded = datetime.date.fromisoformat(PARTY[pid]["identity"]["legal"]["founded"])
    day = datetime.date.fromisoformat(on)
    return day.year - founded.year - ((day.month, day.day) < (founded.month, founded.day))


def company_headcount(pid):
    return PARTY[pid]["identity"]["legal"]["headcount"]


def company_turnover_lume(pid):
    """The party's yearly turnover (world/parties.json), in lume at the reference rates."""
    t = PARTY[pid]["identity"]["legal"]["turnover"]
    per = {"XBL": Decimal(1), "XUF": Decimal(100), "XLC": Decimal("0.4")}[t["currency"]]
    return Decimal(t["amount"]) / per


# Brackenmere's references for similar supplies (tender/07): the two of the design contest (O195) and a third.
BRACKENMERE_SUPPLIES = [
    "Seating for the reading garden of Lumeport's central library, for the City of Lumeport, 2024: benches and "
    "planter seats, about 38,000 lume.",
    "Promenade benches for Larkmouth's seafront, for Larkmouth town council, 2023: 60 benches, about 41,000 lume.",
    "Park benches for Marrowdale's town park, for Marrowdale town council, 2022: 45 benches, about 27,000 lume."]


@enrich("tender", "QualificationApplicationResponse")
def _(f, n, doc, out):
    """Brackenmere answers every question of the request, each in the element of its kind (tender/07#F1, F4 to F7)."""
    founded = PARTY[RUNNER_UP]["identity"]["legal"]["founded"]

    def resp(cid, pid, values, **x):
        return {"ID": V(f"CRR-{cid}", "The response."), "ValidatedCriterionPropertyID": V(pid, "The question "
                                                                                                 "answered."),
                **x, "ResponseValue": values}

    def rv(rid, why, **x):
        return {"ID": V(rid, "The answer."), **{k: v if isinstance(v, V) else v for k, v in x.items()}}
    return {"ContractName": V("Park benches for the parks renewal programme", "The contract."),
            "VersionID": V("1", "The first version."),
            "ProcedureCode": V("OPEN", "The procedure."),
            "QualificationApplicationTypeCode": V("REGULATED", "The regulated form."),
            "WeightScoringMethodologyNote": V("Pass or fail.", "As asked."),
            "WeightingTypeCode": V("NONE", "No weighting."),
            "Note": V("All criteria answered.", "Every question of the request has its response below."),
            "ProcurementProject": {"ID": V(FOLDER, "The procedure.")},
            "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")},
            "TenderingCriterion": [{"ID": V(c, "A criterion of the request, answered below.")} for c in
                                   ("CR-CONVICTIONS", "CR-TAXES", "CR-REGISTER", "CR-YEARS", "CR-TURNOVER",
                                    "CR-STAFF", "CR-REFERENCES", "CR-TIMBER", "CR-GROUP")],
            "TenderingCriterionResponse": [
                resp("CONVICTIONS", "P-CONVICTIONS-1", rv("RV-CONVICTIONS", "", ResponseIndicator=V(
                    "false", "No conviction of the company or of its management."))),
                resp("TAXES", "P-TAXES-1", rv("RV-TAXES", "", ResponseAmount=amount(Decimal("0"), "XBL", "Nothing "
                                                                                    "due is unpaid."))),
                resp("REGISTER", "P-REGISTER-1", rv(
                    "RV-REGISTER", "", Response=V("Entered in the federal business register of Bayvarra.", "The "
                                                  "answer in words: which register."),
                    ResponseID=V(PARTY[RUNNER_UP]["identity"]["registry_id"], "Its number in that register, so "
                                 "that the department can look the entry up."),
                    ResponseIndicator=V("true", "Yes: registered."),
                    ResponseURI=V("https://register.bayvarra.example", "Where the entry is kept and can be looked "
                                  "up: the register the notices name as the economic operator registry."))),
                resp("YEARS", "P-YEARS-1", rv("RV-YEARS", "", ResponseQuantity=qty(
                    company_years(RUNNER_UP, out["IssueDate"].value), "ANN", f"Full years since the company was "
                    f"founded on {founded} (world/parties.json)."))),
                resp("TURNOVER", "P-TURNOVER-1",
                     rv("RV-TURNOVER", "", ResponseAmount=amount(BRACKENMERE_TURNOVER_2024, "XBL", "The turnover of "
                        "2024, from the accounts filed for that year (as the registry's extract of the design "
                        "contest states it, contest/13).")),
                     Name=V("Turnover", "What the response is about."),
                     Description=V(f"The turnover of 2024, {BRACKENMERE_TURNOVER_2024:,.0f} lume, is above the "
                                   f"minimum of {TURNOVER_MIN:,} lume.", "The response in short: the figure itself "
                                   "is the value below."),
                     ConfidentialityLevelCode=V("CONFIDENTIAL", "Not to be published."),
                     CommodityClassification={"ItemClassificationCode": V("38111", "The benches of lot 1, which the "
                                                                                   "turnover criterion applies to, "
                                                                                   "as a UN CPC subclass.")},
                     ApplicablePeriod={"StartDate": V("2024-01-01", "The year asked for"),
                                       "EndDate": V("2024-12-31", "and answered (tender/07#F5).")},
                     SuppliedEvidence={"ID": V("EV-ACC-BF", "The accounts.")},
                     ProcurementProjectLotReference=lot_ref("LOT-1")),
                resp("STAFF", "P-STAFF-1", rv("RV-STAFF", "", ResponseQuantity=qty(
                    company_headcount(RUNNER_UP), "IE", "Its staff, in persons (world/parties.json)."))),
                resp("REFERENCES", "P-REFERENCES-1",
                     [rv(f"RV-REFERENCES-{i}", "", Description=V(s, "One supply: customer, year, what and value."))
                      for i, s in enumerate(BRACKENMERE_SUPPLIES, 1)]),
                resp("REFERENCES-COUNT", "P-REFERENCES-2", rv("RV-REFERENCES-COUNT", "", ResponseQuantity=qty(
                    len(BRACKENMERE_SUPPLIES), "EA", "The supplies listed."))),
                resp("TIMBER", "P-TIMBER-1", rv("RV-TIMBER", "", ResponseIndicator=V(
                    "true", "Its hardwood comes from certified forests.")), SuppliedEvidence={"ID": V("EV-FOR-BF",
                                                                                                "The certificate.")}),
                resp("GROUP", "P-GROUP-1", rv("RV-GROUP", "", ResponseIndicator=V(
                    "false", "Brackenmere tenders alone, so the questions for a group are not answered.")))],
            "AdditionalDocumentReference": {"ID": V(f.numbers["qar"], "The request this self-declaration answers "
                                                                     "(tender/07#F6).")},
            "Evidence": [{"ID": V("EV-ACC-BF", "The annual accounts."), "EvidenceTypeCode": V("ACCOUNTS", "Kind."),
                          "Name": V("Annual accounts 2024", "Name."), "Description": V("Audited.", "What."),
                          "CandidateStatement": V("True and complete.", "The statement."),
                          "ConfidentialityLevelCode": V("CONFIDENTIAL", "Not published."),
                          "EvidenceIssuingParty": party("37-xb", short=True),
                          "DocumentReference": {"ID": V("BF-ACC-2024", "The accounts.")},
                          "Language": {"ID": V("en", "English.")}},
                         {"ID": V("EV-FOR-BF", "The forestry certificate."), "EvidenceTypeCode": V(
                             "CERTIFICATE", "Kind."), "Name": V("Forestry certificate of the hardwood", "Name."),
                          "Description": V("Chain-of-custody certificate for the hardwood of Brackenmere's slats, valid "
                                           "until 30 June 2028.", "What.")}],
            "Signature": seal("37-xb", "BF-SIG-QAR")}


@enrich("tender", "TendererQualification")
def _(f, n, doc, out):
    return {"Note": V("The manufacturer with Saltmere as subcontractor for the installation.", "Who."),
            "VersionID": V("1", "The first version."),
            "Signature": seal("5-xu", "VI-SIG-TQ"),
            "TendererPartyQualification": {
                "InterestedProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")}, {"ID": V("LOT-2", "Lot 2.")}],
                "MainQualifyingParty": {
                    "ParticipationPercent": V("80", "The manufacturer's share."),
                    "PersonalSituation": V("No exclusion grounds apply.", "Declared."),
                    "OperatingYearsQuantity": qty(company_years("5-xu", out["IssueDate"].value), "ANN",
                                                  "Full years in business since the company was founded on "
                                                  f"{PARTY['5-xu']['identity']['legal']['founded']} (world/parties.json)."),
                    "EmployeeQuantity": qty(company_headcount("5-xu"), "IE", "The whole company's staff, in persons "
                                                                         "(world/parties.json)."),
                    "BusinessClassificationEvidenceID": V("ISIC-3100", "Its class."),
                    "BusinessIdentityEvidenceID": V(PARTY["5-xu"]["identity"]["registry_id"], "Its registration."),
                    "TendererRoleCode": V("LEAD", "The lead tenderer."),
                    "BusinessClassificationScheme": {"ID": V("ISIC4", "ISIC Rev. 4."),
                                                     "ClassificationCategory": {"CodeValue": V("3100", "Furniture.")}},
                    "TechnicalCapability": {"ID": V("TC-1", "Production."), "Description": V("4,000 benches a year.",
                                                                                            "Capacity."),
                                            "ValueQuantity": qty(4000, "EA", "A year.")},
                    "FinancialCapability": {"ID": V("FC-1", "Turnover."),
                                            "ValueAmount": amount(company_turnover_lume("5-xu"), "XBL",
                                                                  "The whole company's yearly turnover of 2025, "
                                                                  "converted to lume (world/parties.json).")},
                    "CompletedTask": {"AnnualAverageAmount": amount(Decimal("180000"), "XBL", "A year, similar "
                                                                                              "supplies."),
                                      "TotalTaskAmount": amount(Decimal("540000"), "XBL", "Three years."),
                                      "PartyCapacityAmount": amount(Decimal("540000"), "XBL", "All by itself."),
                                      "Description": V("Benches for Ferrano's parks.", "The task."),
                                      "SuppliedEvidence": {"ID": V("EV-FER-PARKS", "Ferrano's reference letter.")},
                                      "Period": {"StartDate": V("2023-01-01", "From."), "EndDate": V("2025-12-31",
                                                                                                    "To.")},
                                      "RecipientCustomerParty": {"Party": {"PartyName": {"Name": V("City of "
                                                                                                   "Ferrano",
                                                                                                   "The customer.")}}}},
                    "Declaration": {"ID": V("DEC-1", "A declaration."), "Name": V("No conflict of interest",
                                                                                 "Name."),
                                    "DeclarationTypeCode": V("INTEGRITY", "Its kind."),
                                    "Description": V("No ties with the department's officers.", "What."),
                                    "SuppliedEvidence": {"ID": V("EV-DEC-1", "The signed declaration.")}},
                    "EconomicOperatorRole": {"RoleCode": V("LEAD", "The lead."), "RoleDescription": V("Leads.",
                                                                                                    "Role.")}},
                "AdditionalQualifyingParty": {"ParticipationPercent": V("20", "Saltmere's share."),
                                              "TendererRoleCode": V("SUBCONTRACTOR", "For the installation.")}},
            "Evidence": [{"ID": V("EV-FER-PARKS", "The reference."), "Name": V("Ferrano reference", "Name.")},
                         {"ID": V("EV-DEC-1", "The evidence the declaration names (tender/13#F13)."),
                          "Name": V("Signed declaration of no conflict of interest", "Name.")}],
            "AdditionalDocumentReference": {"ID": V("VI-ESPD-26", "The self-declaration.")}}


@enrich("tender", "GuaranteeCertificate")
def _(f, n, doc, out):
    return {"GuaranteeTypeCode": V("TENDER", "A tender guarantee."),
            "Purpose": V("Guarantee of the tender for the bench procedure.", "Its purpose."),
            "ConstitutionCode": V("BANKGUAR", "A bank guarantee."),
            "Note": V("Released at the award.", "When it ends."),
            "ApplicablePeriod": {"StartDate": V(f.date(40), "From."), "EndDate": V(f.date(135), "Until 90 days "
                                                                                                "after the "
                                                                                                "deadline.")},
            "ApplicableRegulation": {"Name": V("Public Procurement Act, article 61", "The rule."),
                                     "LegalReference": V("XB-PPA-2019 art. 61", "The reference."),
                                     "OntologyURI": V("https://law.bayvarra.example/ppa#art61", "Its URI.")},
            "GuaranteeDocumentReference": {"ID": V("BLUM-G-26-0221", "The bank's guarantee deed.")},
            "ImmobilizedSecurity": {"ImmobilizationCertificateID": V("BLUM-IMM-26-0044", "The certificate of the "
                                                                                         "pledged securities."),
                                    "SecurityID": PARTY["5-xu"]["identity"]["legal"]["listing"] and
                                    V(PARTY["5-xu"]["identity"]["legal"]["listing"]["id"], "The manufacturer's own "
                                                                                           "shares, pledged."),
                                    "IssueDate": V(f.date(40), "Pledged."),
                                    "FaceValueAmount": amount(Decimal("2500.00"), "XBL", "Their face value."),
                                    "MarketValueAmount": amount(Decimal("3100.00"), "XBL", "Their market value."),
                                    "SharesNumberQuantity": qty(250, "E21", "250 shares (unit: shares)."),
                                    "IssuerParty": party("5-xu", short=True)},
            "Signature": seal("25-xb", "BLUM-SIG-GC")}


# --- Tendering, part 3: interest, status, unsubscribing, business information, the award and the contract ---------

WINNER, RUNNER_UP, SAWMILL = "5-xu", "37-xb", "36-xb"
WIN_TOTAL = TENDER_QTY * (Decimal("499.00") + Decimal("18.00"))
RUNNER_UP_TOTAL = TENDER_QTY * (Decimal("480.00") + Decimal("16.00"))
CONTRACT_NAME = "Park benches for the parks renewal programme"


def contract_name():
    return V(CONTRACT_NAME, "The name of the contract the procedure is for.")


def project_brief(lot=None):
    """A short procurement project: what is bought, without the full detail of the notice."""
    name = {"LOT-1": "Park benches", "LOT-2": "Installation of the park benches"}.get(lot, "Park benches for the "
                                                                                          "city parks")
    return {"Name": V(name, "The project, or the lot, the document is about."),
            "ProcurementTypeCode": V("WORKS" if lot == "LOT-2" else "SUPPLIES", "The kind of procurement.")}


def appeal_terms():
    return {"Description": V("An appeal against the decision goes to the review board within ten days.", "How to "
                                                                                                         "appeal."),
            "PresentationPeriod": {"StartDate": V(TENDER.date(56), "From the decision."),
                                   "EndDate": V(TENDER.date(66), "Ten days later, the end of the standstill period.")},
            "AppealInformationParty": party(BOARD, short=True),
            "AppealReceiverParty": party(BOARD, short=True),
            "MediationParty": party(BOARD, short=True)}


def tender_result(f, full=True):
    """The result of the procedure: both lots awarded to the manufacturer, on the best price-quality ratio."""
    out = {"AwardID": V(f"{FOLDER}-AWARD-1", "The award decision."),
           "TenderResultCode": V("AWARDED", "The contract is awarded."),
           "Description": V("Both lots to Valdara Industries: the best price-quality ratio, with ten years of "
                            "warranty on the coating.", "Why it won."),
           "AwardTime": V("09:30:00", "The time of the decision, before the tenderers are told.")}
    if full:
        out.update({
            "AdvertisementAmount": amount(Decimal("320.00"), "XBL", "What the winner pays for publishing the notice, "
                                                                    "below the maximum of 500 lume."),
            "ReceivedTenderQuantity": qty(2, "EA", "Two tenders: the furniture maker's first tender was withdrawn and "
                                                    "replaced."),
            "LowerTenderAmount": amount(RUNNER_UP_TOTAL, "XBL", "The lowest tender, the furniture maker's."),
            "HigherTenderAmount": amount(WIN_TOTAL, "XBL", "The highest, the manufacturer's."),
            "StartDate": V(f.date(70), "The contract starts with the first call-off."),
            "ReceivedElectronicTenderQuantity": qty(2, "EA", "Both through the platform."),
            "ReceivedForeignTenderQuantity": qty(1, "EA", "The manufacturer is established in Urvania.")})
    out.update({
        "Contract": {"ID": V(FOLDER, "The framework contract."), "ContractTypeCode": V("FRAMEWORK", "A framework "
                                                                                                    "contract."),
                     "ValidityPeriod": {"StartDate": V(f.date(70), "From the first call-off."),
                                        "DurationMeasure": V("24", "Two years.", unitCode="MON")}},
        "AwardedTenderedProject": {
            "VariantID": V("V0", "The main offer."),
            "ProcurementProjectLot": [lot_ref("LOT-1"), lot_ref("LOT-2")],
            "LegalMonetaryTotal": {"PayableAmount": amount(WIN_TOTAL, "XBL", f"{TENDER_QTY} benches at 499 lume and "
                                                                             "their installation at 18 lume each.")}},
        "ContractFormalizationPeriod": {"StartDate": V(f.date(66), "After the standstill period."),
                                        "EndDate": V(f.date(69), "Before the first call-off.")},
        "SubcontractTerms": {"Rate": V("3.5", "The installation's share of the contract value: "
                                              f"{TENDER_QTY * 18:,} of {WIN_TOTAL:,} lume, rounded."),
                             "UnknownPriceIndicator": V("false", "The price of the subcontracted part is known: the "
                                                                 "tender's installation line."),
                             "Description": V("Saltmere Engineering installs the benches (lot 2) as subcontractor, at "
                                              "the tender's price of 18 lume a bench.", "What is subcontracted, as "
                                                                                       "the tender named it."),
                             "Amount": amount(TENDER_QTY * Decimal("18.00"), "XBL", "The value of the "
                                                                                   "installation.")},
        "WinningParty": {"Rank": V("1", "First in the evaluation."), "Party": party(WINNER, short=True)}})
    return out


@enrich("tender", "ExpressionOfInterestRequest")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "PreferredLanguageLocaleCode": V("en-XB", "The sawmill wants the "
                                                                                       "documents in English, as the "
                                                                                       "city writes it."),
            "Note": V("The sawmill considers a tender for lot 1 with a bench maker and asks to follow the "
                      "procedure.", "Why it registers."),
            "ValidityPeriod": {"EndDate": V(f.date(45), "Its interest lasts until the tender deadline.")},
            "DocumentReference": {"ID": V(f.numbers.get("notice", f"{FOLDER}-CN"), "The contract notice it "
                                                                                   "answers.")},
            "Signature": seal(SAWMILL, "HS-SIG-EOI"),
            "EconomicOperatorParty": {
                "QualifyingParty": {"ParticipationPercent": V("60", "The sawmill's share in the planned consortium."),
                                    "OperatingYearsQuantity": qty(company_years(SAWMILL, out["IssueDate"].value),
                                                                  "ANN", "Full years in business since the sawmill "
                                                                  "was founded on "
                                                                  f"{PARTY[SAWMILL]['identity']['legal']['founded']}."),
                                    "EmployeeQuantity": qty(company_headcount(SAWMILL), "IE", "Its staff, in persons "
                                                                                         "(world/parties.json)."),
                                    "TendererRoleCode": V("LEAD", "It would lead the consortium."),
                                    "Party": party(SAWMILL, short=True)},
                "EconomicOperatorRole": {"RoleCode": V("LEAD", "The lead of a consortium still to be formed."),
                                         "RoleDescription": V("Supplies the slats; a bench maker would build "
                                                              "the benches.", "In words.")}},
            "ProcurementProject": project_brief("LOT-1"), "ProcurementProjectLotReference": lot_ref("LOT-1")}


@enrich("tender", "ExpressionOfInterestResponse")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "TenderLanguageLocaleCode": V("en", "Tenders are written in English."),
            "Note": V("Registered: the sawmill receives every change to the documents.", "The answer."),
            "ExpressionOfInterestDocumentReference": {"ID": V(f.numbers["eoi"], "The expression of interest "
                                                                                "answered.")},
            "Signature": seal(PWD, "PWD-SIG-EOIR"),
            "ProcurementProject": project_brief("LOT-1"), "ProcurementProjectLotReference": lot_ref("LOT-1")}


@enrich("tender", "ProcurementStatusRequest")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("Does the deadline stand after the answers to the "
                                                       "questions?", "What the furniture maker asks."),
            "Signature": seal(RUNNER_UP, "BF-SIG-PSR"),
            "TenderingProcess": {"ID": V(f"{FOLDER}-P", "The procedure asked about.")},
            "ProcurementProject": project_brief(), "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")},
                                                                            {"ID": V("LOT-2", "Lot 2.")}]}


@enrich("tender", "ProcurementStatus")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("The deadline stands; the answers did not change the "
                                                       "documents.", "The status."),
            "ProcedureCode": V("OPEN", "Still an open procedure."),
            "InvitationSubmissionPeriod": {"StartDate": V(f.date(14), "From."), "EndDate": V(f.date(20), "To.")},
            "ParticipationRequestReceptionPeriod": {"EndDate": V(f.date(30), "Closed: requests to participate "
                                                                             "were due then.")},
            "ProcurementLegislationDocumentReference": {"ID": V("XB-PPA-2019", "The procurement act.")},
            "FiscalLegislationDocumentReference": {"ID": V("XB-STT-ACT", "The state sales tax acts.")},
            "EnvironmentalLegislationDocumentReference": {"ID": V("XB-ENV-2021", "The environmental act.")},
            "EmploymentLegislationDocumentReference": {"ID": V("XB-LAB-2018", "The labour act.")},
            "ProcedureStatusRequestDocumentReference": {"ID": V(f.numbers["status-request"], "The request "
                                                                                             "answered.")},
            "Signature": seal(PWD, "PWD-SIG-PS"),
            "DocumentProviderParty": party(PWD, short=True), "TenderRecipientParty": party(PWD, short=True),
            "ProcurementProject": project_brief(),
            "ProcurementProjectLot": [{"ID": V("LOT-1", "Open for tenders.")},
                                      {"ID": V("LOT-2", "Open for tenders.")}]}


@enrich("tender", "UnsubscribeFromProcedureRequest")
def _(f, n, doc, out):
    return {"Note": V("No bench maker joined the sawmill; it will not tender.", "Why it leaves the procedure."),
            "Signature": seal(SAWMILL, "HS-SIG-UNS"),
            "ProcurementProject": project_brief("LOT-1"), "ProcurementProjectLotReference": lot_ref("LOT-1")}


@enrich("tender", "UnsubscribeFromProcedureResponse")
def _(f, n, doc, out):
    return {"Note": V("The sawmill no longer receives the procedure's messages.", "The answer."),
            "UnsubscribeToProcedureDocumentReference": {"ID": V(f.numbers["unsubscribe"], "The request "
                                                                                          "answered.")},
            "Signature": seal(PWD, "PWD-SIG-UNSR"),
            "ProcurementProject": project_brief("LOT-1"), "ProcurementProjectLotReference": lot_ref("LOT-1")}


@enrich("tender", "BusinessInformation")
def _(f, n, doc, out):
    return {"Note": V("Extract from the register of economic operators for the evaluation.", "What it is."),
            "VersionID": V("1", "The first extract."),
            "BriefDescription": V("Valdara Industries: registered, no exclusion grounds recorded.", "In short."),
            "RequestedPublicationDate": V(f.date(46), "Published on the register on the day of the extract."),
            "RegulatoryDomain": V("Bayvarra public procurement", "The rules of the register."),
            "NoticeTypeCode": V("BUSREG", "A notice of registration information."),
            "NoticeLanguageCode": V("en", "In English, the only language of its texts (D29 point 11, tender/12#F7)."),
            "Signature": seal(INFO, "BIS-SIG-BI"),
            "BrochureDocumentReference": {"ID": V("VI-BROCHURE-26", "The manufacturer's brochure, kept on the "
                                                                    "register.")},
            "AdditionalDocumentReference": {"ID": V("VI-ISO9001-CERT", "Its quality certificate.")},
            "BusinessCapability": {
                "ID": V("CAP-1", "A capability on record."),
                "CapabilityTypeCode": V("PRODUCTION", "Production capacity."),
                "Description": V("Benches with frames of ductile cast iron, cast, galvanised and powder-coated in its own plant.", "What."),
                "ValueAmount": amount(company_turnover_lume(WINNER), "XBL", "The yearly turnover of 2025, "
                                                                            "converted to lume (world/parties.json)."),
                "ValueQuantity": qty(6000, "EA", "Benches a year."),
                "SuppliedEvidence": {"ID": V("EV-ACC-2025", "The audited accounts of 2025."),
                                     "Name": V("Annual accounts", "What.")},
                "ValidityPeriod": {"EndDate": V("2026-12-31", "Valid until the next accounts.")},
                "WebSite": {"Name": V("Valdara Industries", "Its site."), "WebSiteTypeCode": V("COMPANY", "A company "
                                                                                                         "site."),
                            "URI": V("https://www.valdara.example", "The address.")}},
            "BusinessPartyGroup": {"GroupTypeCode": V("SAMEACTIVITY", "Operators with the same registered "
                                                                       "activity."),
                                   "GroupType": V("Tenderers in this procedure registered for ISIC 3100", "The "
                                                                                                         "group."),
                                   "Party": [party(WINNER, short=True), party(RUNNER_UP, short=True)]},
            "OperationType": {"Code": V("MANUFACTURE", "Its operation."),
                              "Description": V("Manufacture of furniture for public spaces.", "In words.")},
            "NoticeSubType": {"SubTypeCode": V("EXTRACT", "An extract on request."),
                              "SubTypeDescription": V("Extract asked for by a contracting authority.", "In words.")}}


@enrich("tender", "TenderReceipt")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("Received on time, encrypted, unopened until the opening.",
                                                       "The receipt."),
            "Signature": seal(PWD, "PWD-SIG-RCPT")}


@enrich("tender", "TenderWithdrawal")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("The price per bench was entered wrongly; a corrected tender "
                                                       "follows.", "Why it is withdrawn."),
            "TenderNotificationDocumentReference": {"ID": V("PWD-RCPT-BF-1", "The receipt the platform issued for "
                                                                             "the tender withdrawn (not shown).")},
            "Signature": seal(RUNNER_UP, "BF-SIG-WD")}


@enrich("tender", "TendererQualificationResponse")
def _(f, n, doc, out):
    res = out["QualificationResolution"]
    return {"ContractName": contract_name(), "Note": V("Qualified for both lots.", "The outcome."),
            "ResolutionDocumentReference": {"ID": V("PWD-MIN-QUAL-26", "The minutes of the qualification check.")},
            "AppealTerms": appeal_terms(),
            "Signature": seal(PWD, "PWD-SIG-TQR"),
            "QualificationResolution": [
                {**res,
                 "Resolution": V("Admitted to the evaluation of lot 1.", "The decision."),
                 "ResolutionTime": V("10:00:00", "The time of the decision."),
                 "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")}},
                {**res,
                 "Resolution": V("Admitted to the evaluation of lot 2; the installers' qualifications are "
                                 "sufficient.", "The decision."),
                 "ResolutionTime": V("10:00:00", "The time."),
                 "ProcurementProjectLot": {"ID": V("LOT-2", "Lot 2.")}}]}


@enrich("tender", "ContractAwardNotice")
def _(f, n, doc, out):
    return {**notice_head(f, "CAN", "CAN", urvanian=False),
            "Note": V("Award of the framework contract for park benches.", "What."),
            "PreviousDocumentReference": {"ID": V(f.numbers.get("notice", f"{FOLDER}-CN"), "The contract notice.")},
            "MinutesDocumentReference": {"ID": V("PWD-MIN-AWARD-26", "The minutes of the evaluation.")},
            "TenderingProcess": tendering_process(f, held=True), "ProcurementProject": procurement_project(f),
            "ProcurementProjectLot": procurement_lots(f),
            "TenderResult": {**out["TenderResult"], **tender_result(f)}}


@enrich("tender", "AwardedNotification")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("Your tender has won both lots. The contract follows after "
                                                       "the standstill period.", "The message."),
            "MinutesDocumentReference": {"ID": V("PWD-MIN-AWARD-26", "The minutes of the evaluation.")},
            "AdditionalDocumentReference": {"ID": V("PWD-EVAL-REPORT-26", "The evaluation report.")},
            "FinalFinancialGuarantee": {"GuaranteeTypeCode": V("PERFORMANCE", "A performance guarantee."),
                                        "Description": V("A bank guarantee for the execution of the contract.",
                                                         "What the winner must provide."),
                                        "LiabilityAmount": amount(WIN_TOTAL * Decimal("0.05"), "XBL", "5 % of the "
                                                                                                       "award."),
                                        "AmountRate": V("5", "Five per cent."),
                                        "ConstitutionPeriod": {"EndDate": V(f.date(66), "Before the contract is "
                                                                                       "signed.")}},
            "Signature": seal(PWD, "PWD-SIG-AWD"),
            "TenderResult": {**out["TenderResult"], **tender_result(f, full=False)}}


@enrich("tender", "UnawardedNotification")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("Your tender ranked second. It was lower in price, but the "
                                                       "warranty offered scored lower on quality.", "Why it lost."),
            "Signature": seal(PWD, "PWD-SIG-UNAWD"),
            "MinutesDocumentReference": {"ID": V("PWD-MIN-AWARD-26", "The minutes of the evaluation.")},
            "AdditionalDocumentReference": {"ID": V("PWD-EVAL-SCORES-BF", "The furniture maker's scores.")},
            "AppealTerms": appeal_terms(),
            "TenderResult": {**out["TenderResult"], **tender_result(f, full=False)}}


@enrich("tender", "TenderContract")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("The framework contract, signed by both parties.", "What."),
            "RegulatoryDomain": V("Bayvarra public procurement", "The rules the contract follows."),
            "PreviousDocumentReference": {"ID": V(f.numbers["awarded"], "The award notification.")},
            "ContractDocumentReference": {"ID": V("PWD-CONTRACT-2026-PARKS", "The signed contract.")},
            "Signature": [seal(PWD, "PWD-SIG-CONTRACT", "The department's seal."),
                          seal(WINNER, "VI-SIG-CONTRACT", "The manufacturer's seal.")],
            "ReceiverParty": party(WINNER, short=True),
            "TenderingTerms": tendering_terms(f, call=True),
            "TenderingProcess": {"ID": V(f"{FOLDER}-P", "The procedure."), "ProcedureCode": V("OPEN", "Open.")},
            "ProcurementProject": project_brief(), "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")},
                                                                            {"ID": V("LOT-2", "Lot 2.")}],
            "TenderResult": {**out["TenderResult"], **tender_result(f)}}



# --- Coverage completion, batch A: elements that add detail without changing any amount ------------------------


def line_uuid(f, doc_key, line_id):
    """A line's UUID, derived from the document and the line, so it is stable from build to build."""
    return V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:{f.id}:{doc_key}:line:{line_id}")),
             "A universally unique identifier of the line, derived from the document and the line number.")


def lines_of(out, key):
    v = out.get(key)
    return v if isinstance(v, list) else [v] if v else []


@enrich("air", "Waybill")
def _(f, n, doc, out):
    return {"ExchangeRate": {"SourceCurrencyCode": V("XBL", "The currency of the freight charges."),
                             "TargetCurrencyCode": V("XLC", "The island's currency: its customs adds the freight to "
                                                            "the customs value in coral."),
                             "CalculationRate": V(str(kit.rate("XBL", "XLC")), "The world's reference rate."),
                             "MathematicOperatorCode": V("Multiply", "Lume times the rate gives coral."),
                             "Date": V(f.date(9), "The rate of the day the waybill is issued.")}}


@enrich("cotton", "Order")
def _(f, n, doc, out):
    for tt in lines_of(out, "TaxTotal"):
        for st in lines_of(tt, "TaxSubtotal"):
            st["TaxCategory"]["TaxScheme"]["TaxTypeCode"] = V("CONSUMPTION", "The import consumption tax is a tax "
                                                                             "on consumption.")
    return {}


@enrich("cotton", "GoodsCertificate")
def _(f, n, doc, out):
    for g in lines_of(out.get("Shipment", {}), "GoodsItem"):   # a phytosanitary certificate attests the goods'
        g.pop("DeclaredCustomsValueAmount", None)              # health: no customs value, no classing certificate
        if isinstance(g.get("Item"), dict):                    # (cotton/10#F9)
            g["Item"].pop("Certificate", None)
    gp = out.get("GoodsProcessing")
    if isinstance(gp, dict) and isinstance(gp.get("CriterionItem"), dict):
        gp["CriterionItem"]["TypeCode"] = V("PROCESSING", "A criterion on how the goods were processed.")
    return {}


@enrich("rail", "TransitCustomsDeclaration")
def _(f, n, doc, out):
    return {"AdditionalDocumentReference": [
        *([out["AdditionalDocumentReference"]] if isinstance(out.get("AdditionalDocumentReference"), dict)
          else out.get("AdditionalDocumentReference", [])),
        {"ID": V("VI-CD-26-0330E", "The export declaration lodged in Urvania at the office of departure, which the "
                                   "transit continues; a document outside the examples (rail/06#F5).")}]}


def bench_frame_serial(lot):
    """The serial number of the first side frame of a bench lot, from Valdara's production record (D21)."""
    p = next(x for x in kit.CHAIN["production"] if x.get("lot") == lot)
    return f"{kit.maker('bench-casting')['serials']}{p['frame_serials'][0]:05d}"


def previous_declarations(f, sender):
    """The imports under which the goods a flow exports entered the exporter's country, from the exporter's stock
    ledger (world/items.json goods_chain, D21): [(flow of the import, the goods in words)]."""
    led = kit.CHAIN["ledgers"][sender]["entries"]
    out = next(e for e in led if e["flow"] == f.id and e.get("out"))
    found = []
    for ln in out["out"]:
        key = ln.get("lot") or tuple(ln["serials"])
        came = next(e for e in led if any((x.get("lot") or tuple(x.get("serials", ()))) == key and
                                          x["item"] == ln["item"] for x in e.get("in", [])))
        fl = came["declaration"][0]
        what = (f"the {ln['qty']} benches of lot {ln['lot']}" if ln.get("lot") else
                f"the {ln['serials'][1] - ln['serials'][0] + 1} side frames")
        found.append((fl, what))
    return found


@enrich("sea", "ExportCustomsDeclaration")
def _(f, n, doc, out):
    cd = out.get("CustomsDeclaration")
    if isinstance(cd, dict):
        prev = previous_declarations(f, "6-xb")      # the exporter's ledger: Lumeway, for whom the forwarder declares
        # rail/14 exists since G3 (D37); O164 makes it this declaration's previous declaration when the sea flow is
        # built, the road import becoming a typed additional reference; until then the road import stays
        built = [(fl, what) for fl, what in prev if FLOWS[fl].numbers.get("import") and fl != "rail"]
        if len(built) != 1:
            raise SystemExit(f"sea export: the goods chain gives {built} as previous declarations; UBL allows one")
        fl, what = built[0]
        missing = [w for fl2, w in prev if (fl2, w) != built[0]]
        cd["PreviousCustomsDeclaration"] = {
            "ID": V(FLOWS[fl].numbers["import"], f"The import declaration under which {what} entered Bayvarra from "
                    f"Urvania (flow {fl}; the stock ledger of world/items.json, D21): they now leave again."
                    + (f" {(' and '.join(missing))[0].upper() + (' and '.join(missing))[1:]} entered under the "
                       f"rail delivery's import declaration {FLOWS['rail'].numbers.get('import')} (rail/14, D37), which "
                       "becomes this declaration's previous declaration with the sea flow (O164)." if missing else "")),
            "FunctionCode": V("IMPORT", "The kind of the previous declaration.")}
    return {}


@enrich("retail", "TransportationStatusRequest")
def _(f, n, doc, out):
    return {"TransportExecutionPlanDocumentReference": {
        "ID": V("BF-TEP-26-0262", "The forwarder's confirmation of the booking requested by the distributor: its "
                                  "transport execution plan (not shown in this flow), numbered in the "
                                  "forwarder's own series.")}}


@enrich("retail", "CreditNote")
def _(f, n, doc, out):
    for ln in lines_of(out, "CreditNoteLine"):
        ln["UUID"] = line_uuid(f, f"credit-{n}", ln["ID"].value)
    return {}


# road: no insurance endorsement on the certificate of origin; the chamber is its only endorser (road/06#F3, D35)


@enrich("tender", "Order")
def _(f, n, doc, out):
    return {}      # no forward contract in a tender document: the hedge is Valdara's, in the story only (D28, O50)


@enrich("utilities", "RemittanceAdvice")
def _(f, n, doc, out):
    if doc["from"] != "5-xu":
        return {}
    a = f.numbers["invoice-33-xu-amount"]
    vat = (a - a / Decimal("1.2")).quantize(Decimal(1))
    return {"TaxTotal": {"TaxAmount": amount(vat, "XUF", "The value added tax included in the payment, which the "
                                                        "manufacturer deducts in its own return (20 % of the price "
                                                        "before tax).")}}


@enrich("utilities", "Invoice")
def _(f, n, doc, out):
    pm = out.get("PaymentMeans")
    if isinstance(pm, dict) and isinstance(pm.get("PaymentMandate"), dict):
        pm["PaymentMandate"]["MaximumPaymentInstructionsNumeric"] = V("12", "At most one collection a month.")
    return {}


@enrich("wood", "RequestForQuotation")
def _(f, n, doc, out):
    for i, ln in enumerate(lines_of(out, "RequestForQuotationLine"), 1):
        ln["ID"] = V(str(i), "The line's number in the request.")
    return {}


@enrich("ore", "Invoice")
def _(f, n, doc, out):
    for ln in lines_of(out, "InvoiceLine"):
        ext = ln.get("ItemPriceExtension")
        if isinstance(ext, dict):
            base = Decimal(ext["Amount"].value)
            tax = (base * Decimal("0.20")).quantize(Decimal(1))
            ext["TaxInclusiveAmount"] = amount(base + tax, "XUF", "The price extension with 20 % value added tax.")
            ext["TaxTotal"] = {"TaxAmount": amount(tax, "XUF", "The tax on the price extension, before the line's "
                                                              "allowance.")}
        if doc["from"] == "4-xu":       # the moisture of this train's ore, measured at loading (D45, ore/07#F2)
            props = ln["Item"].setdefault("AdditionalItemProperty", [])
            props.append({"Name": V("Moisture content", "A measured property of the ore delivered, not of the "
                                                         "item in general: the moisture of this train's lot."),
                          "ValueQuantity": V(ORE_MOISTURE[0], f"Measured on the sample taken at loading (assay "
                                                              f"{ORE_ASSAY}); the supply agreement allows "
                                                              f"{ORE_MOISTURE[1]} %.", unitCode="P1")})
    return {}


# --- Coverage completion, batch B: who the goods are for, line references and transport plans ------------------
# The island trader buys the benches for the Port of Selanu, which furnishes its harbour park with them
# ("Harbour parks Selanu", the buyer's project): the port originated the purchase and benefits from it.
HARBOUR = "16-xl"


def for_harbour(why="The Port of Selanu, for whose harbour park the trader buys the benches."):
    return {"OriginatorCustomerParty": {"Party": party(HARBOUR, short=True)},
            "BeneficiaryParty": party(HARBOUR, short=True)}


def find_dicts(x, key):
    """Every dict below x that has the key."""
    if isinstance(x, dict):
        if key in x:
            yield x
        for v in x.values():
            if not isinstance(v, V):
                yield from find_dicts(v, key)
    elif isinstance(x, list):
        for v in x:
            yield from find_dicts(v, key)


def for_harbour_line(li):
    """The port's line of the sea order (O172): the Port of Selanu originated it and its harbour parks get the
    benches; the buyer's own stock lines name neither."""
    li["OriginatorParty"] = party(HARBOUR, short=True)
    li["BeneficiaryParty"] = party(HARBOUR, short=True)


def harbour_lines(f, lines):
    """The lines of a sea document that bill or move the port's benches (O172), in the order of the deal."""
    return [ln for ln, d in zip(lines, f.deal) if d.get("port")]


@enrich("sea", "Order")
def _(f, n, doc, out):
    for i, ol in enumerate(lines_of(out, "OrderLine"), 1):
        ol["LineItem"]["UUID"] = line_uuid(f, "order", i)
    for ol in harbour_lines(f, lines_of(out, "OrderLine")):
        for_harbour_line(ol["LineItem"])
    out["OrderLine"][0]["LineItem"]["OrderedShipment"] = {
        "Shipment": {"ID": V("VT-SH-PLAN-1", "The shipment the buyer plans for this line: one container."),
                     "ShippingPriorityLevelCode": V("STANDARD", "No urgency for the sea part."),
                     "TotalTransportHandlingUnitQuantity": qty(len(kit.pallets(f, f.deal[:1])), "EA", "The pallets "
                                                               f"the line's benches come on: "
                                                               f"{len(kit.pallets(f, f.deal[:1]))} of four "
                                                               "(sea/05#F1).")},
        "Package": {"ID": V("PAL", "Packed on pallets."),
                    "Quantity": qty(4, "EA", "The benches on one pallet: four, as the distributor sells them."),
                    "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet."),
                    "ContainedPackage": [kit.parcel_package(p) for p in kit.maker("bench-serra-b")["parcels"]]}}
    return {}       # the whole order is not the port's: its originator and beneficiary are on its line (O172)


@enrich("sea", "OrderResponse")
def _(f, n, doc, out):
    for ol in harbour_lines(f, lines_of(out, "OrderLine")):
        for_harbour_line(ol["LineItem"])
    return {"OriginatorDocumentReference": {"ID": V("PS-REQ-26-0031", "The Port of Selanu's request to the trader, "
                                                                      "which the order's port line follows.")}}


@enrich("sea", "Invoice")
def _(f, n, doc, out):
    if doc["from"] != "6-xb":
        return {}
    for ln in harbour_lines(f, lines_of(out, "InvoiceLine")):        # the port's line only (O172)
        ln["OriginatorParty"] = party(HARBOUR, short=True)
        ln["BeneficiaryParty"] = party(HARBOUR, short=True)
    terms = out["PaymentTerms"]
    issued = out["IssueDate"].value         # the terms and their rate date from the invoice itself (sea/22#F2, C72)
    terms[1]["ValidityPeriod"] = {"StartDate": V(issued, "The terms apply from the invoice date"),
                                  "EndDate": V(terms[1]["InstallmentDueDate"].value, "until the balance is due.")}
    terms[1]["ExchangeRate"] = {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                "TargetCurrencyCode": V("XLC", "The buyer's currency, in which it shows the "
                                                               "balance too."),
                                "CalculationRate": V(str(kit.rate("XBL", "XLC")), "The reference rate."),
                                "MathematicOperatorCode": V("Multiply", "Lume times the rate."),
                                "Date": V(issued, "Of the invoice date, as the payment alternative rate.")}
    pm = out["PaymentMeans"]
    pm["CreditAccount"] = {"AccountID": V("HF-CL-VT-001", "The credit line the factor granted the buyer, against "
                                                          "which the receivable is held.")}
    return {}       # the invoice bills the buyer's stock too: the port is named on its line only (O172)


@enrich("sea", "Statement")
def _(f, n, doc, out):
    for ln in lines_of(out, "StatementLine"):       # a line is the whole invoice, not the port's alone (O172)
        ln["UUID"] = line_uuid(f, "statement", ln["ID"].value)
    return {}       # a statement of account states no tax (sea/25#F7)


@enrich("sea", "RemittanceAdvice")
def _(f, n, doc, out):
    for ln in lines_of(out, "RemittanceAdviceLine"):      # the invoice it pays is not the port's alone (O172)
        ln["UUID"] = line_uuid(f, "remittance", ln["ID"].value)
    return {}


@enrich("sea", "DebitNote")
def _(f, n, doc, out):
    for ln in lines_of(out, "DebitNoteLine"):
        ln["BeneficiaryParty"] = party("1-xl", short=True)
    return {}


@enrich("furniture", "Order")
def _(f, n, doc, out):
    if n != 8:
        return {}
    for k, ol in enumerate(out["OrderLine"], 1):
        li = ol["LineItem"]
        ext = Decimal(li["LineExtensionAmount"].value)
        li["UUID"] = line_uuid(f, "order", k)
        li["ItemPriceExtension"] = {"Amount": amount(ext, "XBL", "The price times the quantity, before any "
                                                                 "allowance.")}
        li["TaxTotal"] = {"TaxAmount": amount(0, "XBL", "No sales tax: the store buys for resale.")}
    return {}      # the quotation line is referenced once, by the order line (furniture/08#F11)


@enrich("furniture", "OrderCancellation")
def _(f, n, doc, out):
    return {"OriginatorCustomerParty": {"Party": party("26-xb", short=True)},
            "BeneficiaryParty": party("26-xb", short=True)}


@enrich("furniture", "RequestForQuotation")
def _(f, n, doc, out):
    return {"BeneficiaryParty": party("26-xb", short=True)}


@enrich("furniture", "Invoice")
def _(f, n, doc, out):
    if n == 17:          # the department's budget commitment, as its order gave it (furniture/16#F1)
        return {"AdditionalDocumentReference": {"ID": V(PWD_COMMITMENT, "The department's budget commitment the "
                                                                        "invoice is billed against.")}}
    return {}


@enrich("road", "OrderResponse")
def _(f, n, doc, out):
    for i, ol in enumerate(lines_of(out, "OrderLine"), 1):
        olr = ol.get("OrderLineReference")
        if isinstance(olr, dict):
            olr["UUID"] = line_uuid(FLOWS["road"], "order", i)
            if i != 1:
                olr["LineStatusCode"] = V("Revised", "The line is answered with a substitute.")
        ol["DocumentReference"] = {"ID": V("VI-DS-B180" if i == 1 else "VI-DS-C180-2026", "The datasheet of the "
                                                                                          "item confirmed.")}
    return {}


@enrich("retail", "Invoice")
def _(f, n, doc, out):
    if doc["from"] != "6-xb":
        return {}
    ln = out["InvoiceLine"][0] if isinstance(out["InvoiceLine"], list) else out["InvoiceLine"]
    ln.update({
        "UUID": line_uuid(f, "invoice", 1),
        "TaxPointDate": V(f.date(18), "The day the goods were delivered."),
        "DespatchLineReference": {"LineID": V("1", "The despatch line."),
                                  "DocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice.")}},
        "ReceiptLineReference": {"LineID": V("1", "The receipt line, with the damaged carton."),
                                 "DocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice.")}},
        # no line reference to a datasheet: the catalogue names the maker's (retail/18#F12, C73)
        "PricingReference": {"OriginalItemLocationQuantity": {
            "LeadTimeMeasure": V("5", "As in the catalogue.", unitCode="DAY")}},
        "DeliveryTerms": {"ID": V("DDP", "Delivered duty paid, the store's shop, as for the whole order.",
                                  schemeID="INCOTERMS")},
        "PaymentTerms": {"Note": V("The promotion stock is paid with the invoice, 30 days net.", "The line's "
                                                                                                   "terms.")}})
    return {}


@enrich("retail", "ReceiptAdvice")
def _(f, n, doc, out):
    for ln in lines_of(out, "ReceiptLine"):
        ln["UUID"] = line_uuid(f, "receipt", ln["ID"].value)
        ln["DocumentReference"] = {"ID": V("BS-PHOTO-26-0118", "The photograph of the damaged carton.")}
    return {}


@enrich("sea", "BillOfLading")
def _(f, n, doc, out):
    for gic in find_dicts(out, "GoodsItemContainer"):
        gic["GoodsItemContainer"]["TransportEquipment"] = {"ID": V(CONTAINER, "The container itself, as "
                                                                              "equipment.")}
    for ip in find_dicts(out, "InsurancePolicy"):
        pol = ip["InsurancePolicy"]
        pol["BrokerParty"] = party("10-xb", short=True)
        pol["ExcessAmount"] = amount(Decimal("250.00"), "XBL", "The excess per claim, as in the policy.")
    return {}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    for cl in lines_of(out, "CatalogueLine"):
        it = cl.get("Item")
        if isinstance(it, dict):
            it["ItemTypeCode"] = V("PRODUCT", "A physical product, not a service.")
    return {}


@enrich("retail", "CatalogueRequest")
def _(f, n, doc, out):
    for d in find_dicts(out, "ClassificationCategory"):
        cc = d["ClassificationCategory"]
        if isinstance(cc, dict):
            cc["Description"] = V("Outdoor furniture and its spare parts.", "What the category holds.")
            cc["CategorizesClassificationCategory"] = {"Name": V("Spare parts", "A subcategory the store wants "
                                                                                 "too."),
                                                        "CodeValue": V("FUR-OUT-SP", "Its code.")}
    return {}


@enrich("ore", "TransportExecutionPlanRequest")
def _(f, n, doc, out):
    # no status reason: the request has no status, and its relation to the standing plan is said next to the
    # reference (D45, ore/02#F5); the quantity is this month's, the standing plan's train (ore/02#F4)
    out["Consignment"]["SummaryDescription"] = V("One train of 30 wagons, about 1,800 t of lump iron ore.",
                                                 "What is to be carried, before the wagons are loaded and weighed.")
    out["Consignment"]["TotalGoodsItemQuantity"] = qty(1, "EA", "The number of goods items: the ore.")
    return {"TransportExecutionPlanDocumentReference": {
                "ID": V("FRC-TEP-26-0001", "The standing plan for the ore season, agreed in January (not shown)."),
                "DocumentDescription": V("The standing plan for 2026 provides one train a month of 30 wagons, about "
                                         "1,800 t; this request books March's train, for this month's call-off of "
                                         "1,800 t, in the loading window of 10 to 13 March.",
                                         "How this request updates the standing plan (ore/02#F4, F5).")},
            "TransportServiceDescriptionDocumentReference": {"ID": V("FRC-TSD-26", "The rail carrier's published "
                                                                                   "service description (not "
                                                                                   "shown).")},
            "AdditionalDocumentReference": {"ID": V("SM-ASSAY-26-11", "The assay of the ore lot.")},
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TEPR"),
            "AtLocation": {"Name": V("Fucinalta mine siding", "Where the wagons are loaded.")},
            "AdditionalTransportationService": {"TransportServiceCode": V("WEIGH", "The wagons are weighed at "
                                                                                     "the siding."),
                                                "TariffClassCode": V("B", "The carrier's tariff class.")},
            "TransportExecutionTerms": {"TransportUserSpecialTerms": V("Wagons sheeted against dust.", "A term "
                                                                                                   "asked.")}}


@enrich("ore", "TransportExecutionPlan")
def _(f, n, doc, out):
    for d in find_dicts(out, "NotificationRequirement"):
        for nr in lines_of(d, "NotificationRequirement"):
            nr["NotificationPeriod"] = {"StartDate": V(f.date(8), "The notice is given on the day of the train"),
                                        "EndDate": V(f.date(8), "before it arrives (ore/03#F2).")}
    # confirmed as requested, so the plan carries what the request asked: the weighing at the mine siding with its
    # tariff class, the place of that service and the user's sheeting term; the pre-arrival notice and the slot and
    # unloading terms are the carrier's own (D45, ore/03#F3)
    out["DocumentStatusReasonDescription"] = V("Capacity available in the requested window, 10 to 13 March: the "
                                               "train is planned for its first day.", "Why it is confirmed as "
                                                                                      "requested.")
    out["AdditionalTransportationService"] = {
        "TransportServiceCode": V("WEIGH", "The wagons are weighed at the mine siding, as requested: the weighed "
                                           "tonnes are what the freight and the ore are billed by."),
        "TariffClassCode": V("B", "The carrier's tariff class, as requested.")}
    out["AtLocation"] = kit.place("XUFNT", "Where the weighing, a service without movement, is done.",
                                  name="Fucinalta mine siding")
    terms = out["TransportExecutionTerms"]
    terms["TransportUserSpecialTerms"] = V("Wagons sheeted against dust.", "The user's term, as the request asked "
                                                                            "it.")
    terms["TransportServiceProviderSpecialTerms"] = V("Delivery within the agreed slot; the consignee unloads. "
                                                      "Waiting time beyond two hours is charged.", "The carrier's "
                                                      "terms.")
    out["Consignment"]["SummaryDescription"] = V("One train of 30 wagons, about 1,800 t of lump iron ore.",
                                                 "What is to be carried, before the wagons are loaded and weighed.")
    out["Consignment"]["TotalGoodsItemQuantity"] = qty(1, "EA", "The number of goods items: the ore.")
    return {"TransportExecutionPlanDocumentReference": {"ID": V("FRC-TEP-26-0001", "The standing plan this plan "
                                                                                   "updates (not shown).")},
            "TransportServiceDescriptionDocumentReference": {"ID": V("FRC-TSD-26", "The service description it "
                                                                                   "follows.")},
            "AdditionalDocumentReference": {"ID": V("FRC-WAGON-LIST-11", "The list of wagons.")},
            "TransportExecutionTerms": {
                "DeliveryTerms": {"ID": V("FCA", "The buyer's terms with the mine, for the carrier's information.",
                                          schemeID="INCOTERMS")},
                "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2E", "Greenhouse gases as CO2 "
                                                                                    "equivalent."),
                                          "ValueMeasure": V("1.9", "Estimated for the trip, electric traction.",
                                                            unitCode="TNE")}}}


# --- Coverage completion, batch C: agreements, waste, transit, hazards, deliveries ------------------------------


@enrich("sea", "DigitalAgreement")
def _(f, n, doc, out):
    roles = {"6-xb": ("true", "The distributor proposed joining the agreement."),
             "1-xl": ("false", "The trader accepted the proposal.")}
    order = doc["parties"]["ParticipantParty"]          # the participants, in the order world/documents.json gives
    out["ParticipantParty"] = [{} for _ in order]
    for pid, pp in zip(order, out["ParticipantParty"]):
        init, why = roles.get(pid, ("false", "A participant."))
        pp.update({"InitiatingPartyIndicator": V(init, why),
                   "PrivatePartyIndicator": V("true", "A private company."),
                   "PublicPartyIndicator": V("false", "Not a public body."),
                   "ServiceProviderPartyIndicator": V("false", "It exchanges its own documents; it is not a "
                                                               "service provider."),
                   "LegalContact": {"Name": V("Legal department", "For legal notices under the agreement.")},
                   "TechnicalContact": {"Name": V("Integration desk", "For the technical connection.")},
                   "SupportContact": {"Name": V("Service desk", "For day-to-day questions.")},
                   "CommercialContact": {"Name": V("Sales office" if pid == "6-xb" else "Purchasing",
                                                   "For the trade itself.")}})
    for ds in find_dicts(out, "SendingDigitalService"):
        for s in lines_of(ds, "SendingDigitalService"):
            s["CertificationDocumentReference"] = {"ID": V("LTAC-CERT-26-017", "The trade accord council's "
                                                                               "certificate that the distributor's "
                                                                               "system passed the conformance "
                                                                               "test.")}
    return {}


@enrich("waste", "WasteNotification")
def _(f, n, doc, out):
    return {"WasteNotificationTypeCode": V("DOMESTIC", "A notification of a waste stream within Urvania under its "
                                                      "national waste law, not of a transboundary movement: producer "
                                                      "and recovery facility are both in Ferrano (D42)."),
            "ConsignmentQuantity": qty(WASTE_LOADS, "EA", "About one load a month over the year."),
            "DocumentReference": {"ID": V("VI-WASTE-CONTRACT-26", "The contract between producer and recovery "
                                                                  "facility, which the notification needs.")},
            "Signature": seal("5-xu", "VI-SIG-WN")}


@enrich("waste", "WasteMovement")
def _(f, n, doc, out):
    return {"WasteMovementTypeCode": V("RECOVERY", "The waste goes to recovery: Rinova recycles the film into "
                                                   "granulate (operation R3 of its permit)."),
            "SequenceNumberID": V("1", "The first load of the stream."),
            "ConsignmentQuantity": qty(WASTE_LOADS, "EA", "Of about twelve notified."),
            "WasteNotificationDocumentReference": {"ID": V(f.numbers["notification"],
                                                           "The notification of the stream the load belongs to."),
                                                   "IssueDate": V(f.date(0), "Its date.")},
            "WeightStatementDocumentReference": {"ID": V(f.number("weighbridge", "7-xu", "WeightStatement"),
                                                         "The weighbridge ticket of the load, whose net weight this "
                                                         "report states."),
                                                 "IssueDate": V(f.date(WASTE_LOAD_DAY), "Its date.")},
            "DocumentReference": [waste_stream_ref(f, "The agency's acknowledgement, whose number each report of "
                                                      "the stream quotes; a domestic stream of non-hazardous waste "
                                                      "for recovery needs no consent (D42)."),
                                  {"ID": V("RR-REC-26-0412", "The certificate of recovery to follow.")}],
            "DocumentDistribution": {"DocumentTypeCode": V("WasteMovement", "The document distributed: this "
                                                                            "movement document."),
                                     "DistributionTypeCode": V("ELECTRONICCOPY", "Sent electronically, as a copy."),
                                     "DistributionType": Detail("the producer must keep it with the notification",
                                                                "why the producer gets a copy."),
                                     "Party": party("5-xu", short=True)},
            "Signature": seal("7-xu", "RR-SIG-WM")}


@enrich("waste", "WeightStatement")
def _(f, n, doc, out):
    return {"WeightStatementTypeCode": V("WEIGHBRIDGE", "A weighbridge ticket: the vehicle and its load weighed.")}


@enrich("plastics", "Waybill")
def _(f, n, doc, out):
    for d in find_dicts(out, "EnergyConsumptionAllocation"):
        for e in lines_of(d, "EnergyConsumptionAllocation"):
            kwh = Decimal(e["AllocatedEnergyMeasure"].value)
            e["EnvironmentalEmission"] = {"EnvironmentalEmissionTypeCode": V("CO2E", "Greenhouse gases as CO2 "
                                                                                    "equivalent."),
                                          "ValueMeasure": V(str(round(kwh * DIESEL_TTW)),
                                                            f"Tank to wheel: the {kwh:,} kWh of diesel allocated to "
                                                            f"the goods times {DIESEL_TTW} kg CO2e per kWh, about "
                                                            "2.67 kg per litre of diesel of about 10 kWh, the order "
                                                            "of the default factor for diesel in EN 16258 (D41).",
                                                            unitCode="KGM")}
    return {}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    sh = out["Shipment"]
    cons = sh.get("Consignment") if isinstance(sh.get("Consignment"), dict) else {}
    cons.update({"ID": V(cons["ID"].value if "ID" in cons else "VI-CS-26-0241", "The consignment of the "
                                                                                 "samples, in Valdara's series of consignment numbers."),
                 "TransitCountry": [{"IdentificationCode": V("XB", "The samples cross Bayvarra by road to "
                                                                   "Lumeport airport: a transit country between "
                                                                   "Urvania and the island, on the carnet's "
                                                                   "transit counterfoils (D40).")}],
                 "TransportAdvisorParty": party("10-xb", short=True)})
    sh["Consignment"] = cons
    return {}


@enrich("cotton", "BillOfLading")
def _(f, n, doc, out):
    for d in find_dicts(out, "Consignment"):
        for c in lines_of(d, "Consignment"):
            c["MortgageHolderParty"] = party("22-xl", short=True)
        break
    return {}


@enrich("road", "Invoice")
def _(f, n, doc, out):
    if doc["from"] != "13-xu":       # the carrier's freight invoice, after the trip: not the waybill (road/08#F1)
        return {}
    for d in find_dicts(out, "Delivery"):
        for dl in lines_of(d, "Delivery"):
            dl["FuelConsumption"] = {"ID": V("TH-FC-26-0159", "The fuel of this delivery, stated with the freight "
                                                              "for the consignee's report of its transport "
                                                              "emissions."),
                                     "FuelTypeCode": V("DIESEL", "The truck runs on diesel."),
                                     "FuelConsumptionMeasure": V(str(wmap.whole(33 * DISTANCE_KM / 100)), f"About 33 litres per 100 km over "
                                                                       f"{DISTANCE_KM} km.", unitCode="LTR")}
        break
    return {}


@enrich("cotton", "DeliveryNote")
def _(f, n, doc, out):
    return {"OriginatorCustomerParty": {"Party": party("40-xb", short=True)},
            "BeneficiaryParty": party("40-xb", short=True),
            "ProjectReference": {"ID": V("SCC-COTTON-QUALITY-26", "The chamber's cotton quality programme, under "
                                                                  "which the farm's seed cotton is classed.")}}


@enrich("air", "FulfilmentCancellation")
def _(f, n, doc, out):
    return {"OriginatorCustomerParty": {"Party": party(HARBOUR, short=True)},
            "BeneficiaryParty": party(HARBOUR, short=True)}


@enrich("tender", "DespatchAdvice")
def _(f, n, doc, out):
    ln = out["DespatchLine"][0]
    ln["Note"] = V("Forty benches in moss green, RAL 6005, as the order change asked.", "The line as despatched.")
    ln.update({"UUID": line_uuid(f, "despatch", 1),
               "Shipment": {"ID": V(f.numbers["shipment"], "The shipment the line travels in.")},
               "SubDespatchLine": [
                   {"ID": V("1.1", "The ground anchor sets that come with the benches."),
                    "DeliveredQuantity": qty(36, "SET", "36 of the 40 sets."),
                    "BackorderQuantity": qty(4, "SET", "Four sets follow."),
                    "BackorderReason": V("The galvanising of the last batch is late; the sets follow within a "
                                         "week, before the installers need them.", "Why."),
                    "OrderLineReference": {"LineID": V("1", "Part of the bench line.")},
                    "Item": {"Name": V("Ground anchor set", "Included in the bench.")}},
                   {"ID": V("1.2", "The fixing bolts."),
                    "DeliveredQuantity": qty(170, "EA", "Four per bench, and ten more."),
                    "OversupplyQuantity": qty(10, "EA", "Ten bolts more than needed, as spares for the "
                                                         "installers."),
                    "OrderLineReference": {"LineID": V("1", "Part of the bench line.")},
                    "Item": {"Name": V("Fixing bolt M12", "Included in the bench.")}}]})
    return {}


@enrich("road", "ReceiptAdvice")
def _(f, n, doc, out):
    """The bench's parcel on the wrong pallet (D35 point 1): a knocked-down bench travels as three parcels, and the 3PL
    put one bench's frame carton (parcel 2 of 3) on the pallet of spare frame cartons, which it looks like. Goods-in
    counts 95 complete benches and 13 frame cartons; the recount the next morning reads the carton's label and finds
    it the 96th bench's. Nothing crossed the border beyond the 300 parcels the carrier took over."""
    b, c = out["ReceiptLine"][0], out["ReceiptLine"][1]
    if nth("road", n, doc) == 2:
        f.numbers["receipt-1"] = f.numbers["receipt"]
        no = f.number("receipt-2", doc["from"], "ReceiptAdvice")
        f.numbers["receipt"] = no
        b.update({"UUID": line_uuid(f, "receipt-2", 1),
                  "Note": V("All 96 benches, after the recount: the 13th carton on the pallet of side frames is this "
                            "line's, parcel 2 of 3 of the bench reported short.", "The line.")})
        c.update({"Note": V("12 spare frames, as despatched: the 13th carton on their pallet was a bench's parcel.",
                            "The line."),
                  "UUID": line_uuid(f, "receipt-2", 2)})
        given = out.get("AdditionalDocumentReference")
        out["AdditionalDocumentReference"] = ([given] if isinstance(given, dict) else given or []) + [
            {"ID": V(f.numbers["receipt-1"], "The receipt advice this one replaces, cancelled by the fulfilment "
                                             "cancellation of the same morning (road/13#F8).")}]
        return {"ID": V(no, "A new number: the first receipt advice was cancelled."),
                "IssueDate": V(f.date(10), "The morning after the delivery, after the recount."),
                "DocumentStatusCode": V("Revised", "UBL document status code Revised: it replaces the cancelled "
                                                   "receipt advice."),
                "Note": V("Recounted: 96 benches and 12 spare frames, as despatched, nothing short and nothing over; "
                          "the 300 parcels agree with the carrier's count.", "The result (road/13#F15).")}
    b.update({"ReceivedQuantity": qty(95, "EA", "One bench fewer than despatched, counted as complete benches."),
              "ShortQuantity": qty(1, "EA", "One bench without its second frame carton."),
              "ShortageActionCode": V("REPLACE", "The distributor asks for the bench's missing parcel with the next "
                                                 "truck."),
              "Note": V("One bench without its frame carton with the bolt set, parcel 2 of 3: 95 complete "
                        "benches.", "What was found."),
              "UUID": line_uuid(f, "receipt", 1),
              "Shipment": {"ID": V(f.numbers["shipment"], "The shipment received.")}})
    c.update({"ReceivedQuantity": qty(13, "EA", "Thirteen frame cartons on the pallet of side frames."),
              "OversupplyQuantity": qty(1, "EA", "One carton more than despatched."),
              "Note": V("13 frame cartons on the pallet of side frames, one more than despatched.", "What was found."),
              "UUID": line_uuid(f, "receipt", 2)})
    return {"Note": V("Counted and checked at goods-in: one bench short of a parcel, one frame carton over.", "The "
                                                                                                         "result.")}


# --- Coverage completion, batch D: utilities -------------------------------------------------------------------
# The water company collects the city's sewage levy for the city: on its bills the levy is a collection line, an
# amount collected on behalf of a third party, with the city as the line's beneficiary. The telecom company gives a
# business bundle discount of 5 % on the subscriptions; calls abroad are included in the subscription.
BUNDLE_PERCENT = Decimal("5")


def bundle_discount():
    return money(Decimal(6) * Decimal(str(ITEM["telecom-line"]["price"]["amount"])) * BUNDLE_PERCENT / 100, "XLC")


def bundle_allowance(amt, why):
    return {"ChargeIndicator": V("false", "An allowance: it lowers the amount."),
            "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it."),
            "AllowanceChargeReason": V("Business bundle discount", "The reason in words."),
            "MultiplierFactorNumeric": V(str(BUNDLE_PERCENT / 100), "5 %."),
            "Amount": amount(amt, "XLC", why)}


@enrich("utilities", "Invoice")
def _(f, n, doc, out):
    key = bill_key(doc)
    if key.startswith("34-xb"):
        lines = out["InvoiceLine"]
        levy_line = lines.pop(1)
        levy_line["BeneficiaryParty"] = party("2-xb", short=True)
        out["InvoiceLine"] = lines
        out["CollectionInvoiceLine"] = levy_line
        out["LineCountNumeric"] = V("2", "The number of lines: one invoice line for the water and one collection line "
                                         "for the city's levy; the totals include both.")
    if key == "33-xu":
        total = out["TaxTotal"]
        subs = total["TaxSubtotal"]
        exc_subs, vat_sub = subs[:-1], subs[-1]
        excise = sum(Decimal(s["TaxAmount"].value) for s in exc_subs)
        vat = Decimal(vat_sub["TaxAmount"].value)
        out["TaxTotal"] = [
            {"TaxAmount": amount(excise, "XUF", "The energy tax, in its two tiers."),
             "CalculationSequenceNumeric": V("1", "The energy tax is calculated first."),
             "TaxIncludedIndicator": V("false", "The line prices do not include it."),
             "TaxSubtotal": exc_subs},
            {"TaxAmount": amount(vat, "XUF", "The value added tax, on the price plus the energy tax."),
             "RoundingAmount": amount(0, "XUF", "No rounding was needed: 20 % of the base is whole ferra."),
             "CalculationSequenceNumeric": V("2", "Calculated on the price and the energy tax."),
             "TaxEvidenceIndicator": V("true", "This tax total is the evidence for the manufacturer's deduction "
                                               "of value added tax."),
             "TaxIncludedIndicator": V("false", "The line prices do not include it."),
             "TaxSubtotal": vat_sub}]
    if key == "35-xl":
        disc = bundle_discount()
        lmt = out["LegalMonetaryTotal"]
        lines_amt = Decimal(lmt["LineExtensionAmount"].value)
        net = lines_amt - disc
        out["AllowanceCharge"] = {**bundle_allowance(disc, "5 % of the six subscriptions."),
                                  "BaseAmount": amount(Decimal(6) * Decimal(str(ITEM["telecom-line"]["price"]
                                                                                ["amount"])), "XLC",
                                                       "The six subscriptions."),
                                  "TaxCategory": kit.tax_category(kit.tax_rule("35-xl", "1-xl", "telecom-line"))}
        lmt.update({"AllowanceTotalAmount": amount(disc, "XLC", "The bundle discount."),
                    "AllowanceTotalTaxInclusiveAmount": amount(disc, "XLC", "The same: no tax on the island."),
                    "TaxExclusiveAmount": amount(net, "XLC", "The lines less the discount."),
                    "TaxInclusiveAmount": amount(net, "XLC", "No tax on the island."),
                    "PayableAmount": amount(net, "XLC", "What the trader pays.")})
        for st in lines_of(out["TaxTotal"], "TaxSubtotal"):
            st["TaxableAmount"] = amount(net, "XLC", "The lines less the discount: no tax applies on the island.")
        f.numbers[f"invoice-{key}-amount"] = net
    return {}


@enrich("utilities", "UtilityStatement")
def _(f, n, doc, out):
    sc = out["SubscriberConsumption"]
    sup = doc["from"]
    if sup == "33-xu" and doc["to"] == "5-xu":
        it = sc["SupplierConsumption"]["ConsumptionLine"]["UtilityItem"]
        it["OneTimeChargeType"] = V("Connection to the 10 kV grid, paid once in 2024", "The one-time charge of the "
                                                                                     "contract.")
        it["OneTimeChargeTypeCode"] = V("CONN", "As a code: a connection charge.")
    if sup == "34-xb" and doc["to"] == "c-xb":
        sc["Consumption"]["EnergyWaterSupply"]["EnergyWaterConsumptionCorrection"] = {
            "CorrectionType": V("District heating cooling correction", "The water company also runs the city's "
                                                                       "district heating; the heat of the flat is "
                                                                       "settled once a year, and the statement shows "
                                                                       "the month's cooling correction."),
            "CorrectionTypeCode": V("COOL", "As a code."),
            "MeterNumber": V("CSW-H-71844", "The heat meter of the flat."),
            "ConsumptionWaterQuantity": qty(Decimal("6.2"), "MTQ", "District heating water that passed the flat "
                                                                   "in March."),
            "ActualTemperatureReductionQuantity": qty(31, "CEL", "The water cooled by 31 degrees in the flat."),
            "NormalTemperatureReductionQuantity": qty(35, "CEL", "The network's standard cooling."),
            "DifferenceTemperatureReductionQuantity": qty(-4, "CEL", "Four degrees less than the standard."),
            "CorrectionUnitAmount": amount(Decimal("0.80"), "XBL", "The surcharge per cubic metre per degree "
                                                                   "short."),
            "CorrectionAmount": amount(Decimal("19.84"), "XBL", "6.2 m³ × 4 degrees × 0.80: added to the annual "
                                                                "heating account, not to this bill."),
            "Description": V("Poor cooling makes the network pump more water; the shortfall is charged on the "
                             "annual account.", "Why.")}
    if sup == "35-xl":
        disc = bundle_discount()
        cons = sc["Consumption"]
        cons["AllowanceCharge"] = bundle_allowance(disc, "5 % of the six subscriptions.")
        lmt = cons["LegalMonetaryTotal"]
        total = Decimal(lmt["LineExtensionAmount"].value)
        lmt.update({"AllowanceTotalAmount": amount(disc, "XLC", "The bundle discount."),
                    "PayableAmount": amount(total - disc, "XLC", "The supply less the discount; no tax.")})
        sup_lmt = sc["SupplierConsumption"]["Consumption"]["LegalMonetaryTotal"]
        sup_lmt.update({"AllowanceTotalAmount": amount(disc, "XLC", "The bundle discount."),
                        "PayableAmount": amount(total - disc, "XLC", "The supply less the discount.")})
        cl = sc["SupplierConsumption"]["ConsumptionLine"]
        cl[0]["AllowanceCharge"] = bundle_allowance(disc, "On the subscriptions of this line.")
        cl[1]["UtilityItem"]["PackQuantity"] = qty(5, "E34", "Data beyond the subscriptions is sold in packs of "
                                                             "5 GB.")
        cl[1]["UtilityItem"]["PackSizeNumeric"] = V("7", "Seven packs: the 35 GB of March.")
        tsl = cons["TelecommunicationsSupply"]["TelecommunicationsSupplyLine"]
        per_line = money(disc / 6, "XLC")
        for x in tsl[:6]:
            x["AllowanceCharge"] = bundle_allowance(per_line, "The line's share of the bundle discount.")
        first = tsl[0]
        first["ExchangeRate"] = {"SourceCurrencyCode": V("XBL", "The currency the roaming partner charged in."),
                                 "TargetCurrencyCode": V("XLC", "The bill's currency."),
                                 "CalculationRate": V(str(kit.rate("XBL", "XLC")), "The reference rate."),
                                 "MathematicOperatorCode": V("Multiply", "Lume times the rate."),
                                 "Date": V("2026-03-31", "The rate at the end of the month.")}
        services = first["TelecommunicationsService"]
        call = services[1]
        call["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance."),
                                   "AllowanceChargeReasonCode": V("64", "The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it."),
                                   "AllowanceChargeReason": V("Calls to the trade accord countries are included in "
                                                              "the subscription", "Why the call costs nothing."),
                                   "BaseAmount": amount(Decimal("2.400"), "XLC", "Twelve minutes at the 0.200 "
                                                                                 "tariff for calls abroad."),
                                   "Amount": amount(Decimal("2.400"), "XLC", "All of it.")}
        tsl[1]["TelecommunicationsService"] = [tsl[1]["TelecommunicationsService"], {
            "ID": V("V-0320-02", "A film rented on line 2."), "CallDate": V("2026-03-20", "The day."),
            "CallTime": V("12:30:00", "At lunch."),
            "ServiceNumberCalled": V("video", "The operator's video service, no number called."),
            "TelecommunicationsServiceCategory": V("Video on demand", "The kind of service."),
            "MovieTitle": V("Safe Lifting in the Warehouse", "A training film the trader's staff watched."),
            "PayPerView": V("true", "Paid per film."),
            "Quantity": qty(1, "EA", "One film."),
            "CallExtensionAmount": amount(0, "XLC", "Training films are included in the business bundle.")}]
    return {}


@enrich("utilities", "Reminder")
def _(f, n, doc, out):
    for ln in out["ReminderLine"]:
        ln["UUID"] = line_uuid(f, "reminder", ln["ID"].value)
    out["ReminderLine"][0]["Note"] = V("The direct debit of 23 April was returned.", "What happened.")
    out["ReminderLine"][1]["Note"] = V("The fee for the returned direct debit.", "What it is.")
    return {"Signature": seal("34-xb", "CSWC-SIG-26-REM"),
            "TaxPointDate": V(f.date(30), "The fee becomes due on the reminder date.")}


# --- Coverage completion, batch E: the call-off from order to payment ------------------------------------------
# After the award the manufacturer publishes a catalogue of the framework; the department orders the first release,
# changes it to the harbour park's moss green at a quoted charge, the manufacturer confirms. After the invoice and
# the credit for the damaged bench, the department charges the contract's penalty for the late installation, the
# manufacturer reminds it of the overdue balance with Urvania's statutory interest, and the department pays.
# The contract prices are in ferra, the documents in lume (the department's currency) and the manufacturer is paid
# in ferra; as a business not established in Bayvarra it has Bayforth Forwarding as tax representative there.
PENALTY_DAYS, PENALTY_WAIVED = 3, 1


def penalty():
    inst = TENDER_INST_TOTAL
    gross = money(inst * Decimal("0.005") * PENALTY_DAYS, "XBL")
    waived = money(inst * Decimal("0.005") * PENALTY_WAIVED, "XBL")
    net = gross - waived
    wh = money(net * Decimal("0.10"), "XBL")
    return gross, waived, net, wh


TENDER_INST_TOTAL = Decimal(40) * Decimal("18.00")


def tender_currencies(f, day):
    return {"PricingCurrencyCode": V("XUF", "The contract prices are in ferra."),
            "TaxCurrencyCode": V("XUF", "The manufacturer accounts its value added tax in ferra."),
            "PricingExchangeRate": PRICING_RATE,
            "TaxExchangeRate": {**TO_FERRA(f.date(day)), "TargetCurrencyCode": V("XUF", "The tax currency.")},
            "PaymentExchangeRate": TO_FERRA(f.date(day))}


def tender_complete(n, doc):
    f, d = TENDER, doc["doc"]
    cur = "XBL"
    if d == "Catalogue":
        out = kit.catalogue(f, n, doc, 68, "Published when the contract was signed.", ["bench-serra",
                                                                                      "bench-installation"], 730)
        for i, cl in enumerate(out["CatalogueLine"], 1):
            cl["CallForTendersDocumentReference"] = {"ID": V(f.numbers["call"], "The call for tenders the line was "
                                                                                "awarded under.")}
            cl["CallForTendersLineReference"] = {"LineID": V(str(i), "The line of the call for tenders.")}
        out["ReferencedContract"] = {"ID": V(FOLDER, "The framework contract the catalogue belongs to."),
                                     "ContractType": V("Framework contract", "Its kind.")}
        return out
    if d == "OrderChange":
        bench = Decimal(40) * Decimal("499.00")
        return {"ID": V(f.number("order-change", doc["from"], "OrderChange"), "The department's number for the "
                                                                              "change."),
                "SequenceNumberID": V("1", "The first change of the call-off."),
                "IssueDate": V(f.date(71), "The day after the order."),
                "Note": V("Please deliver the benches of this release in moss green, RAL 6005.", "The change."),
                "RequestedInvoiceCurrencyCode": V("XBL", "The department wants its invoices in lume."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the department's currency"),
                **tender_currencies(f, 71),
                "ValidityPeriod": {"EndDate": V(f.date(74), "The change must be confirmed before the benches are "
                                                            "coated.")},
                "OrderReference": {"ID": V(f.numbers["order"], "The call-off order changed.")},
                "QuotationDocumentReference": {"ID": V("VI-QT-26-0071", "The manufacturer's quotation for the "
                                                                        "special colour.")},
                "OriginatorDocumentReference": {"ID": V(FOLDER, "The procurement procedure.")},
                "AdditionalDocumentReference": {"ID": V("PWD-COLOUR-RAL6005", "The colour sample of the harbour "
                                                                              "park.")},
                "Contract": {"ID": V(FOLDER, "The framework contract.")},
                "Signature": seal(PWD, "PWD-SIG-OC"),
                "FreightForwarderParty": party("10-xb", short=True),
                "PaymentMeans": {"PaymentMeansCode": V("30", "UN/EDIFACT 4461 code 30: credit transfer.",
                                                       listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account("5-xu", "The manufacturer's account, in "
                                                                              "ferra.")},
                "PaymentTerms": {"Note": V("30 days after the invoice, as the contract says.", "Unchanged.")},
                "TransactionConditions": {"Description": V("The framework contract's conditions apply.", "Which "
                                                                                                         "conditions.")},
                "AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                    "AllowanceChargeReasonCode": V("CAT", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                    "AllowanceChargeReason": V("Special colour", "Moss green, RAL 6005."),
                                    "Amount": amount(COLOUR_CHARGE, cur, "5 lume a bench, as quoted.")},
                "AnticipatedMonetaryTotal": {"LineExtensionAmount": amount(bench, cur, "The forty benches."),
                                             "ChargeTotalAmount": amount(COLOUR_CHARGE, cur, "The colour."),
                                             "PayableAmount": amount(bench + COLOUR_CHARGE, cur, "With the "
                                                                                                 "colour.")},
                "OrderLine": {"LineItem": {"ID": V("1", "The bench line."),
                                           "LineStatusCode": V("Revised", "Its colour changes."),
                                           "Quantity": qty(40, "EA", "Unchanged: forty benches."),
                                           "LineExtensionAmount": amount(bench, cur, "Unchanged."),
                                           "Item": {"Description": V("Park bench Serra 180, frame in moss green "
                                                                     "RAL 6005", "The changed item."),
                                                    "Name": V("Park bench Serra 180", "The item.")}}}}
    if d == "OrderResponse":
        out = kit.order_response(f, n, doc, 72, "The manufacturer confirms the next day.")
        bench = Decimal(40) * Decimal("499.00")
        out.update({"OrderResponseCode": V("AP", "UN/EDIFACT 4343 code AP: accepted, with the change."),
                    "SalesOrderID": V("VI-SO-26-0058", "The manufacturer's sales order for the call-off, given in "
                                                       "its answer: the seller's number appears first in the "
                                                       "seller's own document (tender/26#F4)."),
                    "Note": V("Accepted: moss green, at the quoted charge.", "The answer."),
                    "DocumentCurrencyCode": kit.currency_line(cur, "the department's currency"),
                    **tender_currencies(f, 72),
                    "OrderChangeDocumentReference": {"ID": V(f.numbers["order-change"], "The change accepted.")},
                    # no reference to a further call-off: no other order exists (tender/28#F1, C73)
                    "AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                        "AllowanceChargeReasonCode": V("CAT", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                        "AllowanceChargeReason": V("Special colour", "As changed."),
                                        "Amount": amount(COLOUR_CHARGE, cur, "As quoted.")},
                    "LegalMonetaryTotal": {"LineExtensionAmount": amount(bench, cur, "The benches."),
                                           "ChargeTotalAmount": amount(COLOUR_CHARGE, cur, "The colour."),
                                           "PayableAmount": amount(bench + COLOUR_CHARGE, cur, "As it will be "
                                                                                               "invoiced, with the "
                                                                                               "installation "
                                                                                               "separately.")}})
        return out
    if d == "DebitNote":
        gross, waived, net, wh = penalty()
        no = f.number("debit", doc["from"], "DebitNote")
        f.numbers["debit-amount"] = net - wh
        f.numbers["debit-date"] = f.date(84)
        return {"ID": V(no, "The department's debit note number."),
                "IssueDate": V(f.date(84), "After the installation was accepted."),
                "Note": V("Penalty for late installation under the contract's clause PEN-1.", "What it is."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoice"),
                "OrderReference": {"ID": V(f.numbers["order"], "The call-off.")},
                "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The invoice of "
                                                                                                 "the release.")}},
                "ContractDocumentReference": {"ID": V(FOLDER, "The contract with the penalty clause.")},
                "TaxRepresentativeParty": party("10-xb", short=True),
                "AllowanceCharge": {"ChargeIndicator": V("false", "An allowance on the penalty."),
                                    "AllowanceChargeReasonCode": V("64", "The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it."),
                                    "AllowanceChargeReason": V("One day waived", "The first day was lost to a "
                                                                                 "storm, as both agree."),
                                    "Amount": amount(waived, cur, "One day of the penalty.")},
                "TaxTotal": {"TaxAmount": amount(0, cur, "No tax on a contractual penalty.")},
                "WithholdingTaxTotal": {"TaxAmount": amount(wh, cur, "The penalty lowers the price of the "
                                                                     "installation, so the department withholds "
                                                                     "10 % less: this part is reversed.")},
                "LegalMonetaryTotal": {
                    "LineExtensionAmount": amount(gross, cur, "Three days of penalty."),
                    "AllowanceTotalAmount": amount(waived, cur, "One day waived."),
                    "TaxExclusiveAmount": amount(net, cur, "The penalty charged."),
                    "WithholdingTaxTotalAmount": amount(wh, cur, "The withholding reversed."),
                    "PayableAmount": amount(net - wh, cur, "What the manufacturer owes: the penalty less the "
                                                           "withholding the department no longer pays.")},
                "DebitNoteLine": {"ID": V("1", "The penalty."),
                                  "Note": V(f"{PENALTY_DAYS} days at 0.5 % of the installation price of the release.",
                                            "How it is computed."),
                                  "DebitedQuantity": qty(PENALTY_DAYS, "DAY", "Days late."),
                                  "LineExtensionAmount": amount(gross, cur, "0.5 % of 720.00 a day."),
                                  "WithholdingTaxTotal": {"TaxAmount": amount(money(gross * Decimal("0.10"), cur),
                                                                              cur, "The withholding on the line "
                                                                                   "before the waiver.")},
                                  "Item": {"Name": V("Penalty for late installation", "What is charged.")}}}
    if d == "Reminder":
        inv, credit, debit = f.numbers["invoice-amount"], f.numbers["credit-amount"], f.numbers["debit-amount"]
        balance = inv - credit - debit
        late = 113 - 108
        interest = money(balance * Decimal("0.08") * late / 365, cur)
        f.numbers["interest"] = interest
        withheld = Decimal("72.00") - Decimal("1.80") - penalty()[3]
        no = f.number("reminder", doc["from"], "Reminder")
        f.numbers["reminder-amount"] = balance + interest
        return {"ID": V(no, "The manufacturer's reminder number."),
                "IssueDate": V(f.date(113), "Five days after the due date."),
                "ReminderTypeCode": V("PAYMENT", "A reminder of a payment overdue."),
                "ReminderSequenceNumeric": V("1", "The first reminder."),
                "Note": V("The balance of the first release is overdue; Urvania's statutory interest applies. "
                          f"The balance is net of the {withheld} lume the department withheld and paid to the "
                          "state (receipt XB-WHT-26-04-1187).", "What it says, and why the withholding is not "
                                                                "reminded: it is already deducted (tender/35#F4)."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoice"),
                **tender_currencies(f, 113),
                "PaymentCurrencyCode": V("XUF", "Payment in ferra, as for the invoice."),
                "PaymentAlternativeCurrencyCode": V("XBL", "The department may also pay in lume, the currency of "
                                                           "the reminder."),
                "PaymentAlternativeExchangeRate": {**TO_FERRA(f.date(113)),
                                                   "TargetCurrencyCode": V("XBL", "The alternative: lume."),
                                                   "CalculationRate": V("1", "Lume is the reminder's own currency: "
                                                                             "no conversion."),
                                                   "MathematicOperatorCode": V("Multiply", "Times one.")},
                "ReminderPeriod": {"StartDate": V(f.date(109), "Overdue from the day after the due date"),
                                   "EndDate": V(f.date(113), "to the reminder.")},
                "Signature": seal("5-xu", "VI-SIG-REM"),
                "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer.", listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account("5-xu", "The manufacturer's account.")},
                "PaymentTerms": {"Note": V("Please pay within seven days.", "What is asked."),
                                 "PaymentDueDate": V(f.date(120), "A week after the reminder.")},
                "AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                    "AllowanceChargeReasonCode": V("48", "UN/EDIFACT 7161 has no code for interest, so the code is from UN/EDIFACT 5189, with that list's listID."),
                                    "AllowanceChargeReason": V("Statutory interest", "Urvania's interest on late "
                                                                                     "payment."),
                                    "MultiplierFactorNumeric": V("0.08", "8 % a year."),
                                    "Amount": amount(interest, cur, f"{late} days at 8 % a year on the balance."),
                                    "BaseAmount": amount(balance, cur, "The overdue balance.")},
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(balance, cur, "The overdue balance."),
                                       "ChargeTotalAmount": amount(interest, cur, "The interest."),
                                       "PayableAmount": amount(balance + interest, cur, "Now due.")},
                "ReminderLine": [
                    {"ID": V("1", "The invoice."), "UUID": line_uuid(f, "reminder", 1),
                     "Note": V("The release's invoice, due on " + f.date(108) + ".", "What it is."),
                     "DebitLineAmount": amount(inv, cur, "Its payable amount."),
                     "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The "
                                                                                                     "invoice.")}}},
                    {"ID": V("2", "The credit note."), "UUID": line_uuid(f, "reminder", 2),
                     "Note": V("The credit for the damaged bench.", "What it is."),
                     "CreditLineAmount": amount(credit, cur, "Deducted."),
                     "BillingReference": {"CreditNoteDocumentReference": {"ID": V(f.numbers["credit-33"],
                                                                                  "The credit note.")}}},
                    {"ID": V("3", "The penalty."), "UUID": line_uuid(f, "reminder", 3),
                     "Note": V("The department's penalty, set off.", "What it is."),
                     "CreditLineAmount": amount(debit, cur, "Deducted."),
                     "BillingReference": {"DebitNoteDocumentReference": {"ID": V(f.numbers["debit"],
                                                                                 "The debit note.")}}}]}
    if d == "RemittanceAdvice":
        inv, credit, debit, interest = (f.numbers["invoice-amount"], f.numbers["credit-amount"],
                                        f.numbers["debit-amount"], f.numbers["interest"])
        paid = inv - credit - debit + interest
        return {"ID": V(f.number("remittance", doc["from"], "RemittanceAdvice"), "The department's number."),
                "IssueDate": V(f.date(116), "Paid three days after the reminder."),
                "Note": V("Payment of the first release, with the interest.", "What it is for."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the documents settled"),
                "TotalDebitAmount": amount(inv + interest, cur, "The invoice and the interest."),
                "TotalCreditAmount": amount(credit + debit, cur, "The credit note and the penalty."),
                "TotalPaymentAmount": amount(paid, cur, "Transferred, in ferra at 100 to the lume."),
                "LineCountNumeric": V("4", "Four documents settled."),
                "AdditionalDocumentReference": {"ID": V("PWD-PAY-AUTH-26-0412", "The department's payment "
                                                                                "authorisation.")},
                "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer.", listID="UN/EDIFACT EDED 4461"),
                                 "PaymentID": V(kit.rf_reference(f.numbers["invoice"]), "The invoice's creditor "
                                                                                       "reference."),
                                 "PayerFinancialAccount": kit.account("2-xb", "The department's account."),
                                 "PayeeFinancialAccount": kit.account("5-xu", "The manufacturer's account.")},
                "RemittanceAdviceLine": [
                    {"ID": V("1", "The invoice."), "DebitLineAmount": amount(inv, cur, "Its payable amount."),
                     "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"],
                                                                               "The invoice.")}}},
                    {"ID": V("2", "The credit note."), "CreditLineAmount": amount(credit, cur, "Deducted."),
                     "BillingReference": {"CreditNoteDocumentReference": {"ID": V(f.numbers["credit-33"],
                                                                                  "The credit note.")}}},
                    {"ID": V("3", "The penalty."), "CreditLineAmount": amount(debit, cur, "Deducted."),
                     "BillingReference": {"DebitNoteDocumentReference": {"ID": V(f.numbers["debit"],
                                                                                 "The debit note.")}}},
                    {"ID": V("4", "The interest."), "DebitLineAmount": amount(interest, cur, "The interest charged."),
                     "BillingReference": {"ReminderDocumentReference": {"ID": V(f.numbers["reminder"],
                                                                                "The reminder."),
                                                                        "IssueDate": V(f.date(113), "Its date.")},
                                          "AdditionalDocumentReference": {"ID": V("PWD-PAY-AUTH-26-0412",
                                                                                  "The authorisation that covers "
                                                                                  "the interest.")}}}]}
    return tender_with_credit(n, doc)


SCENARIOS["tender"] = _with_enrichment("tender", tender_complete)


@enrich("tender", "Order")
def _(f, n, doc, out):
    return {"TaxCurrencyCode": V("XUF", "The manufacturer accounts its value added tax in ferra."),
            "TaxExchangeRate": {**TO_FERRA(f.date(70)), "TargetCurrencyCode": V("XUF", "The tax currency.")},
            "PaymentExchangeRate": TO_FERRA(f.date(70))}


# --- Coverage completion, batch F: self-billing on the island ---------------------------------------------------
# The gin withholds the island's presumptive tax on farm produce (1 % up to 2,000 coral of a delivery, 2 % above)
# and the farm collects the cotton fund's levy of 1 % from the gin (world/countries.json). Seed cotton is priced from
# the trade accord's lint reference price in lume; the farm is paid in coral and may ask for lume instead. Its tax
# affairs with the island's tax office are handled by its customs broker, as tax representative.
XL_TAX = WORLD["countries"]["XL"]["tax"]["withholding"]
XL_COTTON = WORLD["countries"]["XL"]["cotton"]


def presumptive_tax(value):
    """The withholding on a delivery's value, per tier: [(base, percent, range)]."""
    t1 = min(value, Decimal(XL_TAX["tiers"][0]["up_to"]))
    return [(t1, Decimal(XL_TAX["tiers"][0]["percent"]), "Up to 2,000 coral of the delivery's value"),
            (value - t1, Decimal(XL_TAX["tiers"][1]["percent"]), "Above 2,000 coral")]


def withholding_total(tiers, why, reversal=False):
    tax = sum(money(b * p / 100, "XLC") for b, p, _ in tiers)
    subs = []
    for b, p, rng in tiers:
        cat = {"ID": V("S", "The withholding applies."), "Percent": V(str(p), "The rate of the tier."),
               "TierRange": V(rng, "The tier."), "TierRatePercent": V(str(p), "The rate within the tier."),
               "TaxScheme": {"ID": V("OTH", "UN/EDIFACT 5153 code OTH: other taxes, the presumptive tax."),
                             "Name": V("Presumptive tax on farm produce", "The tax in words.")}}
        subs.append({"TaxableAmount": amount(b, "XLC", "The part of the value in this tier."),
                     "TaxAmount": amount(money(b * p / 100, "XLC"), "XLC", f"{p} % of it."),
                     "Percent": V(str(p), "The rate."), "TierRange": V(rng, "The tier."),
                     "TierRatePercent": V(str(p), "The rate within the tier."), "TaxCategory": cat})
    return tax, {"TaxAmount": amount(tax, "XLC", why), "TaxSubtotal": subs}


def fund_levy_line(base, line_id, credit=False):
    pct = Decimal(XL_COTTON["fund_levy_percent"])
    amt = money(base * pct / 100, "XLC")
    kind, qn = ("CreditedQuantity", "credited") if credit else ("InvoicedQuantity", "invoiced")
    return amt, {"ID": V(line_id, "The collection line."),
                 "Note": V("Collected by the farm for the cotton fund of the Selanu Chamber of Commerce.", "Why the "
                                                                                                          "line is "
                                                                                                          "there."),
                 kind: qty(1, "EA", f"The levy, {qn} once."),
                 "LineExtensionAmount": amount(amt, "XLC", f"{pct} % of the value of the seed cotton."),
                 "BeneficiaryParty": party(XL_COTTON["fund"], short=True),
                 "Item": {"Name": V("Cotton fund levy", "What is collected.")}}


def cotton_currencies(f, day):
    to = lambda c, r, why: {"SourceCurrencyCode": V("XLC", "The document currency."),       # noqa: E731
                            "TargetCurrencyCode": V(c, why),
                            "CalculationRate": V(r, "The reference rate." if r != "1" else "The same currency: no "
                                                                                             "conversion."),
                            "MathematicOperatorCode": V("Multiply", "Coral times the rate."),
                            "Date": V(f.date(day), "Of the document's date.")}
    return {"PricingCurrencyCode": V("XBL", "Seed cotton is priced from the trade accord's lint reference price, "
                                            "published in lume."),
            "PricingExchangeRate": {"SourceCurrencyCode": V("XBL", "The reference price's currency."),
                                    "TargetCurrencyCode": V("XLC", "The document's."),
                                    "CalculationRate": V(str(kit.rate("XBL", "XLC")), "The reference rate."),
                                    "MathematicOperatorCode": V("Multiply", "Lume times the rate gives coral."),
                                    "Date": V(f.date(day), "Of the document's date.")},
            "TaxCurrencyCode": V("XLC", "The presumptive tax is paid to the island's tax office in coral."),
            "TaxExchangeRate": to("XLC", "1", "The tax currency, coral."),
            "PaymentCurrencyCode": V("XLC", "The farm is paid in coral."),
            "PaymentExchangeRate": to("XLC", "1", "The payment currency, coral."),
            "PaymentAlternativeCurrencyCode": V("XBL", "The farm may ask to be paid in lume, to its account in "
                                                       "Bayvarra, where it buys its machinery."),
            "PaymentAlternativeExchangeRate": to("XBL", str(kit.rate("XLC", "XBL")), "Lume, the alternative."),
            "TaxPointDate": V(f.date(day), "The day the withholding becomes due.")}


def cotton_refs(f):
    return {"OriginatorDocumentReference": {"ID": V("LTM-SEASON-2026", "The mill's season contract with the gin, "
                                                                       "for which the gin buys the seed cotton.")},
            "ProjectReference": {"ID": V("SCC-COTTON-QUALITY-26", "The chamber's cotton quality programme.")},
            "PurchaseReference": {"ID": V("LCF-FIELD-07", "The field the cotton was picked from, for traceability.")},
            "StatementDocumentReference": {"ID": V("SCG-ACC-LCF-26-02", "The gin's season account of the farm "
                                                                        "(not shown).")},
            "BuyerAssignedReference": {"BuyerReferenceCode": V("SCG-AP-FARMS", "The gin's desk for farm "
                                                                               "payments."),
                                       "BuyerReference": V("Farm payments", "In words.")},
            "Annotation": {"AnnotationContent": V("Written by the gin on the farm's behalf under the self-billing "
                                                  "agreement.", "A remark.")},
            "TaxRepresentativeParty": party("3-xl", short=True),
            "Signature": seal("39-xl", f"SCG-SIG-SB-{f.date(0)[-2:]}")}


@enrich("cotton", "SelfBilledInvoice")
def _(f, n, doc, out):
    if out["InvoiceTypeCode"].value == "386":       # the prepayment: no delivery yet, so no withholding or levy
        return {}
    lmt = out["LegalMonetaryTotal"]
    value = Decimal(out["InvoiceLine"]["LineExtensionAmount"].value if isinstance(out["InvoiceLine"], dict)
                    else out["InvoiceLine"][0]["LineExtensionAmount"].value)
    tiers = presumptive_tax(value)
    wh, wt = withholding_total(tiers, "The presumptive tax the gin withholds on the delivery.")
    levy, cline = fund_levy_line(value, "2")
    payable = Decimal(lmt["PayableAmount"].value) - wh + levy
    lmt["WithholdingTaxTotalAmount"] = amount(wh, "XLC", "Withheld and paid to the island's tax office.")
    lmt["PayableAmount"] = amount(payable, "XLC", "What the gin pays: the cotton and haulage, less the advance and "
                                                  "the withholding, plus the levy the farm collects.")
    f.numbers["self-billed-4-amount"] = payable
    ac = out["AllowanceCharge"]
    ac.update({"PrepaidIndicator": V("false", "Not prepaid: paid with the invoice."),
               "TaxTotal": {"TaxAmount": amount(0, "XLC", "No tax on the haulage on the island.")},
               "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer, with the invoice.",
                                                      listID="UN/EDIFACT EDED 4461")}})
    lmt["AllowanceTotalTaxInclusiveAmount"] = amount(0, "XLC", "No allowances.")
    ln = out["InvoiceLine"] if isinstance(out["InvoiceLine"], dict) else out["InvoiceLine"][0]
    ref = ln["Delivery"]["DeliveryNoteLineReference"]
    ref["UUID"] = line_uuid(f, "delivery", 1)
    out["CollectionInvoiceLine"] = cline
    out["LineCountNumeric"] = V("2", "The seed cotton and the collection line of the levy.")
    return {**cotton_currencies(f, 5), **cotton_refs(f),
            "WithholdingTaxTotal": wt,
            "OriginatorCustomerParty": {"Party": party("40-xb", short=True)},
            "BeneficiaryParty": party("40-xb", short=True),
            "AdditionalDocumentReference": [x for x in (out.get("AdditionalDocumentReference"),) if x] + [
                {"ID": V(PARTY["38-xl"]["identity"]["registry_id"], "The farm's registration, which the withholding "
                                                                       "needs: its number in Lisavu's farm register "
                                                                       "(O142).")}],
            "BillingReference": {"SelfBilledInvoiceDocumentReference": {
                "ID": V(f.numbers["self-billed-1"], "The prepayment self-billed invoice of the season advance, "
                                                    "deducted here as the prepaid amount."),
                "IssueDate": V(f.numbers["self-billed-1-date"], "Its issue date.")}},
            "WorkReportDocumentReference": {"ID": V("SCG-OUT-26-0311", "The gin's outturn report of the lot.")}}


@enrich("cotton", "SelfBilledCreditNote")
def _(f, n, doc, out):
    lmt = out["LegalMonetaryTotal"]
    value = Decimal(lmt["LineExtensionAmount"].value)
    wh = money(value * Decimal(XL_TAX["tiers"][1]["percent"]) / 100, "XLC")
    levy, cline = fund_levy_line(value, "2", credit=True)
    fee = Decimal("5.000")
    payable = value - fee - wh + levy
    lmt.update({"AllowanceTotalAmount": amount(fee, "XLC", "The classing fee the farm bears."),
                "TaxExclusiveAmount": amount(value - fee, "XLC", "The credit less the fee."),
                "TaxInclusiveAmount": amount(value - fee, "XLC", "No tax on the island."),
                "WithholdingTaxTotalAmount": amount(wh, "XLC", "The withholding on the credited value, reversed: "
                                                               "the value falls in the 2 % tier."),
                "PayableAmount": amount(payable, "XLC", "What the farm's account is credited: the price "
                                                        "difference less the fee and the withholding, plus the "
                                                        "levy on it.")})
    f.numbers["self-billed-5-amount"] = payable
    out["CollectionCreditNoteLine"] = cline
    out["LineCountNumeric"] = V("2", "The price difference and the levy on it.")
    return {**cotton_currencies(f, 12), **cotton_refs(f),
            "InvoicePeriod": {"StartDate": V(f.date(1), "The deliveries classed, from the first"),
                              "EndDate": V(f.date(3), "to the last trailer.")},
            "WorkReportDocumentReference": {"ID": V("SCC-CLS-26-0311", "The chamber's classing report.")},
            "WithholdingTaxTotal": {"TaxAmount": amount(wh, "XLC", "The withholding reversed on the credit.")},
            "AllowanceCharge": {"ChargeIndicator": V("false", "An allowance: it lowers the credit."),
                                "AllowanceChargeReasonCode": V("64", "The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it."),
                                "AllowanceChargeReason": V("Classing fee", "The farm bears the classing of its "
                                                                           "cotton, as the agreement says."),
                                "Amount": amount(fee, "XLC", "The chamber's fee for the lot.")}}


# --- Coverage completion, batch G: references, allowances and the remaining details -----------------------------


@enrich("air", "OrderChange")
def _(f, n, doc, out):
    return for_harbour()


@enrich("furniture", "Order")
def _(f, n, doc, out):
    if n != 10:
        return {}
    net = Decimal(0)
    for ol in out["OrderLine"]:
        li = ol["LineItem"]
        gross = Decimal(li["LineExtensionAmount"].value)
        if gross:                         # the free care kits have nothing to discount
            disc = money(gross * Decimal("0.03"), "XBL")
            li["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance on the line."),
                                     "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of "
                                                                          "UN/EDIFACT 5189, as EN 16931 uses it."),
                                     "AllowanceChargeReason": V("Repeat order", "The quotation gives 3 % on a repeat "
                                                                                "order of the line."),
                                     "MultiplierFactorNumeric": V("0.03", "3 %."),
                                     "Amount": amount(disc, "XBL", "3 % of the line."),
                                     "BaseAmount": amount(gross, "XBL", "The line at the quoted price.")}
            li["LineExtensionAmount"] = amount(gross - disc, "XBL", "The line less the repeat-order discount.")
            gross -= disc
        net += gross
    amt = out["AnticipatedMonetaryTotal"]
    for k in ("LineExtensionAmount", "TaxExclusiveAmount", "TaxInclusiveAmount", "PayableAmount"):
        if k in amt:
            amt[k] = amount(net, "XBL", "Net of the repeat-order discount; no sales tax on goods bought for resale.")
    return {"OrderDocumentReference": {"ID": V(f.numbers["order"], "The first order of the line: this one is a "
                                                                   "second delivery of the same pieces.")}}


@enrich("furniture", "WorkReport")
def _(f, n, doc, out):
    smt = out["StatementMonetaryTotal"]
    amt = Decimal(smt["LineExtensionAmount"].value)
    smt["ChargeTotalAmount"] = amount(Decimal("24.00"), "XBL", "The packaging disposal.")
    smt["PayableAmount"] = amount(amt + Decimal("24.00"), "XBL", "What the invoice will charge: the hours and the "
                                                                 "disposal.")
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                "AllowanceChargeReasonCode": V("AEO", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                "AllowanceChargeReason": V("Packaging disposal", "The installers took the "
                                                                                 "packaging away."),
                                "Amount": amount(Decimal("24.00"), "XBL", "A flat charge.")},
            "AdditionalDocumentReference": {"ID": V(PWD_COMMITMENT, "The department's budget commitment the work "
                                                                    "will be billed against, as its order gave it.")}}


@enrich("furniture", "DebitNote")
def _(f, n, doc, out):
    br = out["DebitNoteLine"]["BillingReference"]["BillingReferenceLine"]
    iid, q, _ = MARROW_BACK[0]
    br["Amount"] = amount(Decimal(q) * Decimal(str(ITEM[iid]["price"]["amount"])), "XBL",
                          f"The amount of the credit note's first line, the {pieces(iid)} returned.")
    return {}


# The forwarder's invoice cites no statement: a statement of account for May would be drawn up after it and lists
# its invoices, not the reverse (air/10#F5, C72).


@enrich("sea", "Statement")
def _(f, n, doc, out):
    first = out["StatementLine"][0]
    first["AllowanceCharge"] = [
        {"ChargeIndicator": V("true", "A charge in the invoice of the line."),
         "AllowanceChargeReasonCode": V("FC", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
         "AllowanceChargeReason": V("Sea freight", "As on the invoice: CIF."),
         "Amount": amount(SEA_FREIGHT, "XBL", "The freight.")},
        {"ChargeIndicator": V("true", "A charge."), "AllowanceChargeReasonCode": V("96", "UN/EDIFACT 7161 has no code for insurance, so the code is from UN/EDIFACT 5189, with that list's listID."), "AllowanceChargeReason": V("Cargo insurance", "As on the "
                                                                                                "invoice."),
         "Amount": amount(INSURANCE, "XBL", "The premium.")}]
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "The charges in the account, summed."),
                                "AllowanceChargeReasonCode": V("FC", "The sum is mostly freight; one code covers the charge (UN/EDIFACT 7161)."),
                                "AllowanceChargeReason": V("Freight and insurance of the CIF invoice", "Why."),
                                "Amount": amount(SEA_FREIGHT + INSURANCE, "XBL", "Included in the balance.")}}


def retail_complete(n, doc):
    f = RETAIL
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(
            f, n, doc, 9, "Answered the same morning.", "On its way from the distribution centre; arrival expected "
                                                        "at 14:00.", "Marrowdale ring road",
            {"CarrierAssignedID": V("BF-ROAD-26-0231", "The carrier's own number for the job."),
             "TransportationStatusRequestDocumentReference": {"ID": V(f.numbers["ts-request"], "The request "
                                                                                               "answered.")},
             "TransportationStatusTypeCode": V("CURRENT", "The current status."),
             "UpdatedDeliveryTransportEvent": {"OccurrenceDate": V(f.date(9), "Today."),
                                               "OccurrenceTime": V("14:00:00", "The expected arrival."),
                                               "Description": V("Expected arrival at the store.", "In words."),
                                               "Location": {**kit.gln_location("26-xb", "goods-in"),
                                                            "Name": V("Goods-in of the Lumeport store", "Where "
                                                                      "the truck is expected.")}}}, event_type="ENROUTE")
    return retail(n, doc)


SCENARIOS["retail"] = _with_enrichment("retail", retail_complete)


def pallets_charge(cur="XBL"):
    return {"ChargeIndicator": V("true", "A charge."),
            "AllowanceChargeReasonCode": V(PALLETS_CHARGE["code"], PALLETS_CHARGE["code_why"]),
            "AllowanceChargeReason": V(PALLETS_CHARGE["reason"], PALLETS_CHARGE["why"]),
            "Amount": amount(Decimal(PALLETS_CHARGE["amount"]), cur, PALLETS_CHARGE["amount_why"])}


@enrich("wood", "Quotation")
def _(f, n, doc, out):
    q = out["QuotedMonetaryTotal"]
    base = Decimal(q["LineExtensionAmount"].value)
    ch = Decimal(PALLETS_CHARGE["amount"])
    q["ChargeTotalAmount"] = amount(ch, "XBL", "The export pallets.")
    q["PayableAmount"] = amount(base + ch, "XBL", "The slats and the pallets; no tax on an export.")
    return {"AllowanceCharge": pallets_charge()}


@enrich("wood", "Order")
def _(f, n, doc, out):
    if doc["from"] != "5-xu":
        return {}
    a = out["AnticipatedMonetaryTotal"]
    base = Decimal(a["LineExtensionAmount"].value)
    ch = Decimal(PALLETS_CHARGE["amount"])
    a["ChargeTotalAmount"] = amount(ch, "XBL", "The export pallets, as quoted.")
    a["PayableAmount"] = amount(base + ch, "XBL", "The slats and the pallets.")
    return {"AllowanceCharge": pallets_charge()}


STT_RETAIL = Decimal("0.065")


@enrich("retail", "PurchaseReceipt")
def _(f, n, doc, out):
    delivery = Decimal("25.00")
    base = Decimal(out["LegalMonetaryTotal"]["LineExtensionAmount"].value) + delivery
    tax = money(base * STT_RETAIL, "XBL")
    total = base + tax
    out["TaxTotal"]["TaxAmount"] = amount(tax, "XBL", "6.5 % state sales tax on the bench and the delivery.")
    st = out["TaxTotal"]["TaxSubtotal"][0] if isinstance(out["TaxTotal"]["TaxSubtotal"], list) else \
        out["TaxTotal"]["TaxSubtotal"]
    st["TaxableAmount"] = amount(base, "XBL", "The bench and the home delivery.")
    st["TaxAmount"] = amount(tax, "XBL", "6.5 %.")
    lmt = out["LegalMonetaryTotal"]
    lmt.update({"ChargeTotalAmount": amount(delivery, "XBL", "The home delivery."),
                "TaxExclusiveAmount": amount(base, "XBL", "Before the sales tax."),
                "TaxInclusiveAmount": amount(total, "XBL", "With the sales tax."),
                "PayableAmount": amount(total, "XBL", "Paid by card: no cash rounding.")})
    out["Payment"]["PaidAmount"] = amount(total, "XBL", "Paid by card.")
    ca = out["PaymentMeans"]["CardAccount"]
    ca["IssueNumberID"] = V("01", "The card's issue number: the first card of this account.")
    for ln in lines_of(out, "PurchaseReceiptLine"):
        ln["UUID"] = line_uuid(f, "receipt-pos", ln["ID"].value)
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                "AllowanceChargeReasonCode": V("DL", "The reason for the charge as a code: for a charge UN/EDIFACT 7161 (special services)."),
                                "AllowanceChargeReason": V("Home delivery", "Delivered on Saturday, as booked."),
                                "Amount": amount(delivery, "XBL", "The store's flat delivery charge."),
                                "TaxCategory": st["TaxCategory"]}}


@enrich("packaging", "PurchaseReceipt")
def _(f, n, doc, out):
    if doc["to"] != "c-xb":
        return {}
    ln = out["PurchaseReceiptLine"][0] if isinstance(out["PurchaseReceiptLine"], list) else \
        out["PurchaseReceiptLine"]
    gross = Decimal(ln["LineExtensionAmount"].value)
    off = Decimal("5.00")
    net = gross - off
    tax = money(net * STT_RETAIL, "XBL")
    total = net + tax
    paid = (total / Decimal("0.05")).quantize(Decimal(1), rounding="ROUND_HALF_UP") * Decimal("0.05")
    ln["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance on the line."),
                             "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of UN/EDIFACT 5189, as EN 16931 uses it."),
                             "AllowanceChargeReason": V("Two shirts: 5.00 off the pair, Friday 22 May only",
                                                       "The store's offer, for one day: the next day's sale of three "
                                                       "shirts is at the full price (packaging/09#F6)."),
                             "Amount": amount(off, "XBL", "Off the pair."),
                             "BaseAmount": amount(gross, "XBL", "Two shirts at the shelf price.")}
    ln["LineExtensionAmount"] = amount(net, "XBL", "Two shirts less the offer.")
    if "TaxInclusiveLineExtensionAmount" in ln:
        ln["TaxInclusiveLineExtensionAmount"] = amount(total, "XBL", "With the sales tax.")
    out["TaxTotal"]["TaxAmount"] = amount(tax, "XBL", "6.5 % state sales tax, the only point where Bayvarra's tax "
                                                      "is charged.")
    st = out["TaxTotal"]["TaxSubtotal"][0] if isinstance(out["TaxTotal"]["TaxSubtotal"], list) else \
        out["TaxTotal"]["TaxSubtotal"]
    st["TaxableAmount"] = amount(net, "XBL", "The shirts less the offer.")
    st["TaxAmount"] = amount(tax, "XBL", "6.5 %.")
    lmt = out["LegalMonetaryTotal"]
    lmt.update({"LineExtensionAmount": amount(net, "XBL", "The line."),
                "TaxExclusiveAmount": amount(net, "XBL", "Before tax."),
                "TaxInclusiveAmount": amount(total, "XBL", "With tax."),
                "PayableRoundingAmount": amount(paid - total, "XBL", "Cash is rounded to 5 cents, Bayvarra's "
                                                                     "smallest coin."),
                "PayableAmount": amount(paid, "XBL", "Paid in cash, rounded.")})
    pay = out["Payment"]
    pay["PaidAmount"] = amount(paid, "XBL", "Paid in cash.")
    cash = Decimal(pay["PaidCashAmount"].value)
    pay["CashChangeAmount"] = amount(cash - paid, "XBL", "The change given.")
    return {}


@enrich("sea", "DebitNote")
def _(f, n, doc, out):
    fee, storage = Decimal("38.500"), Decimal("12.750")
    ln = out["DebitNoteLine"]
    ln["LineExtensionAmount"] = amount(fee, "XLC", "The inspection fee, as customs charged it.")
    ln["TaxInclusiveLineExtensionAmount"] = amount(fee, "XLC", "No tax on the island.")
    ln["Note"] = V("Customs inspection of the container at Selanu.", "What is charged.")
    out["CollectionDebitNoteLine"] = {
        "ID": V("2", "The collection line."),
        "Note": V("The port's storage charge for the day the container was held, collected for the port.", "What "
                                                                                                          "it is."),
        "DebitedQuantity": qty(1, "DAY", "One day."),
        "LineExtensionAmount": amount(storage, "XLC", "The port's charge."),
        "BeneficiaryParty": party(HARBOUR, short=True),
        "Item": {"Name": V("Container storage at the port of Selanu", "What is collected.")}}
    out["LineCountNumeric"] = V("2", "The inspection and the port's storage, collected; the totals include both.")
    return {}


def utilities_complete(n, doc):
    f = UTILITIES
    if doc["doc"] == "CreditNote":
        rows = [{"item": "water", "qty": 2, "why": "Two cubic metres the meter over-read in March."},
                {"item": "sewage-levy", "qty": 2, "why": "The city's levy on them."}]
        out = kit.credit_note(f, n, doc, 34, "Issued when the meter test was in.", rows,
                              {"BillingReference": {"InvoiceDocumentReference": {
                                  "ID": V(f.numbers["invoice-34-xb:c-xb"], "The March bill corrected."),
                                  "IssueDate": V(f.numbers["invoice-34-xb:c-xb-date"], "Its issue date.")}},
                               "Note": V("The meter test found the meter over-reading by two cubic metres.", "Why.")})
        levy = out["CreditNoteLine"].pop(1)
        levy["CollectedForParty"] = party("2-xb", short=True)
        levy["Note"] = V("The city's levy, credited for the city.", "Why it is a collection line.")
        out["CollectionCreditNoteLine"] = levy
        out["LineCountNumeric"] = V("2", "The water and the collection line of the levy; the totals include both.")
        return out
    return utilities(n, doc)


SCENARIOS["utilities"] = _with_enrichment("utilities", utilities_complete)


def packaging_complete(n, doc):
    f = PACKAGING
    if doc["doc"] == "PurchaseReceipt" and doc["to"] == "1-xl":
        r = kit.rate("XBL", "XLC")
        shelf = Decimal(str(ITEM["shirt-r"]["price"]["amount"]))
        qn = 3
        base_xbl = shelf * qn
        tax_xbl = money(base_xbl * STT_RETAIL, "XBL")
        unit_xlc = money(shelf * r, "XLC")
        base = money(base_xbl * r, "XLC")
        tax = money(tax_xbl * r, "XLC")
        total = base + tax
        rule = kit.tax_rule("26-xb", "c-xb", "shirt-r")
        out = {"ID": V(f.number("receipt-visitor", doc["from"], "PurchaseReceipt"), "The till's receipt number."),
               "IssueDate": V(f.date(26), "During the trade fair in Lumeport."),
               "Note": V("Paid in coral: the card's currency was chosen at the till.", "Printed on the receipt."),
               "DocumentCurrencyCode": kit.currency_line("XLC", "the currency the customer chose to pay in"),
               "PricingExchangeRate": {"SourceCurrencyCode": V("XBL", "The shelf prices are in lume."),
                                       "TargetCurrencyCode": V("XLC", "The receipt is in coral."),
                                       "CalculationRate": V(str(r), "The world's reference rate, which the till "
                                                                    "applies."),
                                       "MathematicOperatorCode": V("Multiply", "Lume times the rate gives coral."),
                                       "Date": V(f.date(26), "The day of the sale.")},
               "TaxExchangeRate": {"SourceCurrencyCode": V("XLC", "The receipt's currency."),
                                   "TargetCurrencyCode": V("XBL", "The sales tax is owed to the state in lume."),
                                   "CalculationRate": V(str(kit.rate("XLC", "XBL")), "The reference rate."),
                                   "MathematicOperatorCode": V("Multiply", "Coral times the rate gives lume."),
                                   "Date": V(f.date(26), "The day of the sale.")},
               "TaxTotal": [{"TaxAmount": amount(tax, "XLC", "The state sales tax, in coral."),
                             "TaxSubtotal": {"TaxableAmount": amount(base, "XLC", "The shirts."),
                                             "TaxAmount": amount(tax, "XLC", "6.5 % of the lume price, converted."),
                                             "TaxCategory": kit.tax_category(rule)}},
                            {"TaxAmount": amount(tax_xbl, "XBL", "The same tax in lume, as the store owes it to "
                                                                 "the state."),
                             "TaxSubtotal": {"TaxableAmount": amount(base_xbl, "XBL", "Three shirts at the shelf "
                                                                                      "price."),
                                             "TaxAmount": amount(tax_xbl, "XBL", "6.5 %."),
                                             "TaxCategory": kit.tax_category(rule)}}],
               "LegalMonetaryTotal": {"LineExtensionAmount": amount(base, "XLC", "The shirts, in coral."),
                                      "TaxExclusiveAmount": amount(base, "XLC", "Before tax."),
                                      "TaxInclusiveAmount": amount(total, "XLC", "With tax."),
                                      "PayableAmount": amount(total, "XLC", "Paid by card: no rounding.")},
               "PurchaseReceiptLine": {"ID": V("1", "The line."), "Quantity": qty(qn, "EA", "Three shirts."),
                                       "LineExtensionAmount": amount(base, "XLC", "Three at the converted price."),
                                       "Item": item("shirt-r"),
                                       "Price": {"PriceAmount": price(str(unit_xlc), "XLC", "The shelf price of "
                                                                                            f"{shelf} lume, in "
                                                                                            "coral."),
                                                 "BaseQuantity": qty(1, "EA", "Per shirt.")}},
               "PaymentMeans": {"PaymentMeansCode": V("54", "UN/EDIFACT 4461 code 54: credit card.",
                                                      listID="UN/EDIFACT EDED 4461"),
                                "CardAccount": kit.card_account("1-xl", "26-xb")},
               "Payment": {"PaidAmount": amount(total, "XLC", "Charged to the card in coral."),
                           "PaidDate": V(f.date(26), "At the till.")}}
        till(out, f, 26, "12:20:00", "C1", "Joss")
        return out
    return packaging(n, doc)


SCENARIOS["packaging"] = _with_enrichment("packaging", packaging_complete)



def road_casting(out, key):
    """From the order response on, the side frame shipped is the 2026 casting: its seller's number with the extended
    ID the response gave it (road/04#F15, 11#F12, 13#F18, 15#F13; D35 point 3, D5)."""
    for ln in lines_of(out, key):
        it = ln.get("Item", {})
        sid = it.get("SellersItemIdentification")
        if isinstance(sid, dict) and sid["ID"].value == ITEM["bench-casting"]["sellers_id"]:
            sid["ExtendedID"] = V(ROAD_CASTING, "The 2026 casting with the reinforced foot, which the order response "
                                                "substituted for the casting ordered.")


def road_complete(n, doc):
    f = ROAD
    lines = {"DespatchAdvice": "DespatchLine", "ReceiptAdvice": "ReceiptLine",
             "Invoice": "InvoiceLine"}.get(doc["doc"])
    if lines and doc["from"] != "13-xu":
        out = road(n, doc)
        road_casting(out, lines)
        return out
    if doc["doc"] == "FulfilmentCancellation":
        return {**head(f, "receipt-cancellation", doc, 10, "Sent with the recount, before the corrected receipt "
                                                           "advice."),
                "Note": V("A corrected receipt advice follows.", "What happens next."),
                "CancellationNote": V("The recount read the label of the 13th carton on the pallet of side frames: "
                                      "\"Serra 180, parcel 2 of 3\", the bench reported short. Neither the shortage "
                                      "nor the carton over existed.", "Why the receipt advice is cancelled."),
                "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The receipt advice cancelled.")},
                # only the receipt advice is cancelled: the despatch advice stands (road/12#F1)
                "OrderReference": {"ID": V(f.numbers["order"], "The distributor's order.")}}
    return road(n, doc)


SCENARIOS["road"] = _with_enrichment("road", road_complete)


# ================================================================ the energy flow: an unbundled market in Urvania
# Kelpstone Gas produces gas offshore of Bayvarra and pipes it to Montebrio Power, the gas-fired power station, and
# to the city gate of Ferrano Grid, the grid operator; Ferrano Energy, the retail company, buys electricity from the
# power station and gas from the producer, pays the grid operator for the networks and bills its customers, among
# them Valdara's factory, whose coating ovens burn gas. The gas contracts are in ferra, the buyers' currency.
GAS_TO_POWER, GAS_TO_RETAIL, POWER_MWH = 36800, 2400, 18400
FACTORY_GAS = {"meter": "FG-G-20417", "m3": Decimal("1350"), "gauge_bar": Decimal("4.0"),
               "factor": Decimal("4.9477"), "cv": Decimal("9.163"), "kwh": 61200}
ENERGY = kit.Flow("energy", "2026-04-01", [{"item": "natural-gas", "ordered": GAS_TO_POWER + GAS_TO_RETAIL,
                                            "why": "March's gas through the border station."}])


PLATFORM = next(pf for pf in WORLD["platforms"] if pf["party"] == "42-xb")


def platform_location(why):
    """The offshore platform: no name, no street; only its grid reference on the world's map grid and its WGS 84
    coordinates, as an offshore installation is identified."""
    import world_model
    # the offshore grid counts blocks of 14 km (four map squares), so the reference keeps two digits each way
    i, j = (v // world_model.GRID for v in PLATFORM["at"])
    return {"ID": V(f"{i:02d}/{j:02d}", why + " Identified by its block of the world's offshore grid (blocks of "
                                             "14 km, column/row), as offshore installations are identified by "
                                             "grid references.",
                    schemeID="urn:ubl-examples:world:grid"),
            "LocationCoordinate": coordinate(PLATFORM["at"])}


def pipeline_stage(why):
    return {"ID": V("1", "The only stage."),
            "TransportModeCode": V("7", "UN/ECE Recommendation 19 code 7: fixed transport installation, a pipeline.",
                                   listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
            "TransportMeans": {"TransportMeansTypeCode": V(kit.fleet("42-xb", "KG-P1")["type"], why)}}


def network_gas_total(doc):
    """What the parent network invoice charges for this consumption: its gas line, the kWh at the network tariff,
    with value added tax (energy/01#F1)."""
    it = ITEM["network-gas"]
    net = money(FACTORY_GAS["kwh"] * Decimal(str(it["price"]["amount"])), "XUF")
    rate_ = Decimal(str(kit.tax_rule(doc["from"], doc["to"], "network-gas")[1]))
    tax = money(net * rate_ / 100, "XUF")
    return {"LineExtensionAmount": amount(net, "XUF", f"{FACTORY_GAS['kwh']} kWh at the gas network tariff of "
                                                      f"{it['price']['amount']} ferra: line 3 of the network "
                                                      "invoice."),
            "TaxExclusiveAmount": amount(net, "XUF", "Without the value added tax."),
            "TaxInclusiveAmount": amount(net + tax, "XUF", f"With {rate_.normalize():f} % value added tax."),
            "PayableAmount": amount(net + tax, "XUF", "What the network invoice charges the retail company for this "
                                                      "consumption.")}


def energy(n, doc):
    f, d = ENERGY, doc["doc"]
    if d == "UtilityStatement":
        g = FACTORY_GAS
        vn = (g["m3"] * g["factor"]).quantize(Decimal(1))
        return {"ID": V(f.number("metering", doc["from"], "UtilityStatement"), "The grid operator's metering report."),
                "IssueDate": V(f.date(1), "Sent with the month's network invoice, the morning after the meters "
                                          "were read."),
                "IssueTime": V("08:20:00", "Issued in the same billing run as the network invoice it supplements, "
                                           "each citing the other, and before the retail company bills the gas by "
                                           "it (energy/01#F5, timelines#F8)."),
                "UtilityStatementTypeCode": V("GAS", "The kind of supply."),
                "ParentDocumentReference": {"ID": V(f.number("network-invoice", "44-xu", "Invoice"), "The network "
                                                    "invoice this statement supplements: the metering behind the "
                                                    "network charge for gas.")},
                "Note": V("Metered consumption for the retail company's billing; the grid operator owns and reads "
                          "the meter.", "What the statement is."),
                "DocumentCurrencyCode": kit.currency_line("XUF", "Urvania's currency"),
                "SubscriberConsumption": {
                    "ConsumptionID": V("FG-CP-4120-G1-2603", "The consumption of the factory's gas point in March."),
                    "SpecificationTypeCode": V("DETAILED", "With the volume conversion."),
                    "Note": V("Gas for the coating ovens of the factory.", "The point."),
                    "TotalMeteredQuantity": qty(g["m3"], "MTQ", "Cubic metres through the meter at line pressure."),
                    "UtilityConsumptionPoint": {
                        "ID": V("FG-CP-4120-G1", "The factory's gas connection."),
                        "Description": V("Valdara Industries, gas connection of the coating line", "Where."),
                        "SubscriberID": V("FE-C-0047121", "The factory's gas contract with the retail company."),
                        "SubscriberType": V("Industrial", "The kind of customer."),
                        "SubscriberTypeCode": V("IND", "As a code."),
                        "TotalDeliveredQuantity": qty(g["kwh"], "KWH", "Delivered in March, as energy."),
                        "Address": address("5-xu"),
                        "UtilityMeter": {"MeterNumber": V(g["meter"], "The gas meter."),
                                         "MeterName": V("Rotary gas meter, coating line", "Its name."),
                                         "MeterConstant": V("1", "Read directly."),
                                         "MeterConstantCode": V("DIRECT", "No multiplier."),
                                         "TotalDeliveredQuantity": qty(g["m3"], "MTQ", "Through the meter."),
                                         "MeterReading": {
                                             "ID": V(f"{g['meter']}-2603", "The reading of March."),
                                             "PreviousMeterReadingDate": V("2026-02-28", "The previous reading."),
                                             "PreviousMeterQuantity": qty(28410, "MTQ", "The register then."),
                                             "LatestMeterReadingDate": V("2026-03-31", "This reading."),
                                             "LatestMeterQuantity": qty(29760, "MTQ", "The register now."),
                                             "LatestMeterReadingMethod": V("Remote reading", "How it was taken."),
                                             "LatestMeterReadingMethodCode": V("REMOTE", "As a code."),
                                             "DeliveredQuantity": qty(g["m3"], "MTQ", "The difference.")}}},
                    "Consumption": {
                        "UtilityStatementTypeCode": V("GAS", "The kind of supply."),
                        "MainPeriod": {"StartDate": V("2026-03-01", "March."), "EndDate": V("2026-03-31", "Its end.")},
                        "EnergyWaterSupply": {
                            "ConsumptionReport": {"ID": V("FG-CP-4120-G1-2603", "The report."),
                                                  "ConsumptionType": V("Monthly consumption", "What it is."),
                                                  "TotalConsumedQuantity": qty(g["kwh"], "KWH", "Energy in March."),
                                                  "Period": {"StartDate": V("2026-03-01", "March."),
                                                             "EndDate": V("2026-03-31", "Its end.")}},
                            "EnergyWaterConsumptionCorrection": {
                                "CorrectionType": V("Volume conversion", "The metered volume is converted to "
                                                                         "standard conditions and to energy."),
                                "CorrectionTypeCode": V("CONV", "As a code."),
                                "MeterNumber": V(g["meter"], "The meter."),
                                "GasPressureQuantity": qty(g["gauge_bar"], "BAR", "The meter runs at 4 bar above "
                                                                                 "the atmosphere: the gas is "
                                                                                 "compressed, so the volume is "
                                                                                 "corrected for the pressure."),
                                "Description": V(f"{g['m3']} m³ at line pressure × {g['factor']} (pressure) = {vn} "
                                                 f"m³ at standard conditions, × {g['cv']} kWh/m³ (calorific value "
                                                 f"of March) = {g['kwh']} kWh.", "The conversion."),
                                "ConsumptionEnergyQuantity": qty(g["kwh"], "KWH", "The energy, which the retail "
                                                                                  "company bills.")}},
                        "LegalMonetaryTotal": network_gas_total(doc)}}}
    if d == "Invoice" and doc["from"] == "44-xu":
        out = kit.invoice(f, n, doc, 1, "The month's network charges, billed the morning after the meters were read, "
                                        "with the metering statement that supplements the invoice.", {},
                           [{"item": "network-electricity", "qty": 412800, "invoice_why": "The factory's electricity "
                                                                                          "connection, March."},
                            {"item": "network-electricity", "qty": BILLS["33-xu"][1]["qty"], "invoice_why": "The warehouse's electricity "
                                                                                         "connection, March."},
                            {"item": "network-gas", "qty": FACTORY_GAS["kwh"], "invoice_why": "The factory's gas "
                                                                                              "connection, March."},
                            # O169: the grid operator made February's estimate and corrects its own invoice too,
                            # as the retail company does on its bill (utilities/02, O159)
                            {"item": "network-electricity", "qty": BILLS["33-xu"][3]["qty"],
                             "invoice_why": "February's estimate corrected: February's network invoice charged the "
                                            f"warehouse's connection {-BILLS['33-xu'][3]['qty']:,} kWh it did not "
                                            "use, which are credited at the network tariff.",
                             "line_extra": FEBRUARY}],
                           key="network-invoice", extra=MARCH)
        out["IssueTime"] = V("08:20:00", "The grid operator's billing run, first thing in the morning.")
        if not isinstance(out["InvoiceLine"], list):
            out["InvoiceLine"] = [out["InvoiceLine"]]
        # each line names the connection it bills by the grid operator's number (energy/02#F1, O161), which the retail
        # company's statements use too; the gas line refers to the metering statement behind it (energy/02#F2)
        for ln, (pid, desc) in zip(out["InvoiceLine"], [
                (POINTS[("33-xu", "5-xu")]["id"], POINTS[("33-xu", "5-xu")]["desc"]),
                (POINTS[("33-xu", "8-xu")]["id"], POINTS[("33-xu", "8-xu")]["desc"]),
                ("FG-CP-4120-G1", "Valdara Industries, gas connection of the coating line"),
                (POINTS[("33-xu", "8-xu")]["id"], POINTS[("33-xu", "8-xu")]["desc"])]):
            ln["Delivery"] = {"DeliveryLocation": {"ID": V(pid, "The consumption point whose network use the line "
                                                                "bills."),
                                                   "Description": V(desc, "The connection in words.")}}
        out["InvoiceLine"][2]["DocumentReference"] = {
            "ID": V(f.numbers["metering"], "The grid operator's metering statement with the readings and the volume "
                                           "conversion behind the line's kWh."),
            "IssueDate": V(f.date(1), "Its issue date."),
            "DocumentTypeCode": V("UtilityStatement", "A utility statement.")}
        return out
    if d == "Invoice" and doc["from"] == "43-xu":
        return kit.invoice(f, n, doc, 2, "The month's electricity.", {},
                           [{"item": "power-wholesale", "qty": POWER_MWH, "invoice_why": "Fed into the grid for the "
                                                                                         "retail company in March."}],
                           key="power-invoice", extra=MARCH)
    if d == "ExportCustomsDeclaration":
        out = kit.export_declaration(f, n, doc, 1, "The monthly declaration of the gas exported in March.",
                                     "The value of the gas at the contract price, in lume.")
        out["CustomsDeclaration"]["Shipment"]["ShipmentStage"] = pipeline_stage("The gas leaves by pipeline.")
        out["CustomsDeclaration"]["Shipment"]["OriginAddress"] = platform_location("Where the gas is produced: the "
                                                                                   "platform of the offshore field.")
        return out
    if d == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, 1, "The monthly declaration of the gas received in March.",
                                     "The customs value in ferra.",
                                     deal=[{"item": "natural-gas", "ordered": GAS_TO_POWER,
                                            "why": "The power station's gas."}])
        out["Shipment"]["ShipmentStage"] = pipeline_stage("The gas arrives by pipeline.")
        return out
    if d == "Invoice" and doc["from"] == "42-xb":
        to_power = doc["to"] == "43-xu"
        key = "gas-invoice" if to_power else "gas-invoice-retail"
        out = kit.invoice(f, n, doc, 2, "The month's gas.", {},
                          [{"item": "natural-gas", "qty": GAS_TO_POWER if to_power else GAS_TO_RETAIL,
                            "invoice_why": "Measured at the border station in March" +
                                           (": delivered to the power station." if to_power else
                                            ": fed into the grid at the city gate.")}],
                          key=key, extra=MARCH, currency="XUF")
        out["Note"] = V("Priced in ferra as the supply contract says: the buyer's own currency.", "Why ferra.")
        ln = out["InvoiceLine"][0] if isinstance(out["InvoiceLine"], list) else out["InvoiceLine"]
        ln["Item"]["OriginAddress"] = platform_location("Where the gas comes from: the field's platform.")
        ln["Price"].pop("PricingExchangeRate", None)   # the contract price is in ferra: nothing converted (energy/06#F1)
        return out
    if d == "Reminder":
        # the debt is in ferra by contract, so the reminder is too: the invoice and the surcharge in ferra, as the
        # payer pays them (energy/08#F1); Bayvarra's statutory surcharge applies, the seller's rule (D22, D44)
        inv = f.numbers["gas-invoice-amount"]
        due = f.date(32)
        pct = Decimal(WORLD["countries"]["XB"]["payment"]["penalty_surcharge"]["percent"])
        sur = money(inv * pct / 100, "XUF")
        f.numbers["surcharge"] = sur
        late = {"StartDate": V(f.date(33), "Overdue from the day after the due date"),
                "EndDate": V(f.date(63), "to the reminder: one month.")}
        invoice_ref = {"InvoiceDocumentReference": {
            "ID": V(f.numbers["gas-invoice"], "The invoice not paid."),
            "IssueDate": V(f.numbers["gas-invoice-date"], "Its issue date.")}}
        return {"ID": V(f.number("reminder", doc["from"], "Reminder"), "The reminder number."),
                "IssueDate": V(f.date(63), "A month after the due date."),
                "ReminderTypeCode": V("PAYMENT", "A reminder of a payment overdue."),
                "ReminderSequenceNumeric": V("1", "The first reminder."),
                "Note": V("The invoice for March's gas is a month overdue: Bayvarra's surcharge of 1.5 % a month "
                          "applies.", "What it says."),
                "DocumentCurrencyCode": kit.currency_line("XUF", "the currency of the debt: the supply contract "
                                                                 "prices the gas in ferra, the buyer's currency"),
                "ReminderPeriod": late,
                "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer.", listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account("42-xb", "The gas producer's account.")},
                "PaymentTerms": {"Note": V("Please pay the invoice and the surcharge together.", "What is asked."),
                                 "PaymentDueDate": V(f.date(70), "A week after the reminder.")},
                "TaxTotal": {"TaxAmount": amount(0, "XUF", "No tax on a surcharge for late payment."),
                             "TaxSubtotal": {"TaxableAmount": amount(sur, "XUF", "The surcharge."),
                                             "TaxAmount": amount(0, "XUF", "No tax: the surcharge is compensation, "
                                                                           "not a supply (energy/08#F7)."),
                                             "TaxCategory": {"ID": V("O", "Outside the scope of the state sales "
                                                                          "tax: compensation for late payment."),
                                                             "TaxExemptionReason": V("Compensation for late payment",
                                                                                     "Why no tax."),
                                                             "TaxScheme": {"ID": V("STT", "UN/EDIFACT 5153 code of "
                                                                                         "the state sales tax.")}}}},
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(inv + sur, "XUF", "The invoice and the "
                                                                                       "surcharge."),
                                       "PayableAmount": amount(inv + sur, "XUF", "Now due, in ferra.")},
                "ReminderLine": [
                    {"ID": V("1", "The unpaid invoice."), "UUID": line_uuid(f, "reminder", 1),
                     "Note": V(f"Invoice due {due}.", "What it is."),
                     "DebitLineAmount": amount(inv, "XUF", "The invoice's amount payable."),
                     "PaymentPurposeCode": V("SUPP", "ISO 20022 purpose code SUPP: payment to a supplier."),
                     "ReminderPeriod": {"StartDate": V(f.date(33), "Overdue since.")},
                     "BillingReference": invoice_ref},
                    {"ID": V("2", "The surcharge."), "UUID": line_uuid(f, "reminder", 2),
                     "Note": V("One month late at 1.5 %.", "What it is."),
                     "DebitLineAmount": amount(sur, "XUF", f"{pct} % of the invoice's {inv} ferra."),
                     "PenaltySurchargePercent": V(str(pct), "Bayvarra's surcharge per month late."),
                     "ReminderPeriod": late,
                     "BillingReference": invoice_ref}]}   # the line's base: the invoice and the month (energy/08#F8)
    if d == "RemittanceAdvice":
        inv, sur = f.numbers["gas-invoice-amount"], f.numbers["surcharge"]
        return {"ID": V(f.number("remittance", doc["from"], "RemittanceAdvice"), "The power station's number."),
                "IssueDate": V(f.date(66), "Paid three days after the reminder."),
                "Note": V("The March gas invoice, with the surcharge of the reminder.", "What it settles."),
                "DocumentCurrencyCode": kit.currency_line("XUF", "the currency of the invoice paid"),
                "TotalDebitAmount": amount(inv + sur, "XUF", "The invoice and the surcharge."),
                "TotalCreditAmount": amount(0, "XUF", "No credits."),
                "TotalPaymentAmount": amount(inv + sur, "XUF", "Transferred in ferra over the trade accord's link."),
                "LineCountNumeric": V("2", "The invoice and the surcharge."),
                "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer.", listID="UN/EDIFACT EDED 4461"),
                                 "PaymentID": V(kit.rf_reference(f.numbers["gas-invoice"]), "The invoice's creditor "
                                                                                           "reference."),
                                 "PayerFinancialAccount": kit.account("43-xu", "The power station's account."),
                                 "PayeeFinancialAccount": kit.account("42-xb", "The gas producer's account.")},
                "RemittanceAdviceLine": [
                    {"ID": V("1", "The invoice."), "DebitLineAmount": amount(inv, "XUF", "Its amount."),
                     "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["gas-invoice"],
                                                                               "The invoice.")}}},
                    {"ID": V("2", "The surcharge."), "DebitLineAmount": amount(sur, "XUF", "The surcharge of the "
                                                                                          "reminder."),
                     "BillingReference": {"ReminderDocumentReference": {"ID": V(f.numbers["reminder"],
                                                                                "The reminder.")}}}]}
    raise SystemExit(f"energy scenario: no document {n} {doc['doc']}")


FLOWS["energy"] = ENERGY
SCENARIOS["energy"] = _with_enrichment("energy", energy)


# ---------------------------------------------------------------- the design contest (Bayvarra): revised documents
# The Public Works Department relaunches the design contest for the harbour promenade's bench, which it cancelled in
# 2025 because no entry met the brief. Several documents of the contest are revised, and each version 2 names
# version 1 as its previous version: the prize fund is raised, a corrigendum corrects the site plan and widens a
# selection criterion, the design team updates its declarations, the business registry updates its extract once the
# accounts are filed, and the result notice corrects a prize amount.
CONTEST = kit.Flow("contest", "2026-02-02")
CFOLDER = "PWD-2026-PROM-DC"
OLD_FOLDER = "PWD-2025-PROM-DC"
TEAM_LEAD, TEAM_MEMBER, SECOND = "37-xb", "27-xb", "5-xu"
LTD_LIST = "urn:ubl-examples:world:XB:codelist:CompanyLegalFormCode"


def contest_version(k, why2):
    """VersionID, and for a second version its PreviousVersionID and why it was revised."""
    if k == 1:
        return {"VersionID": V("1", "The first version.")}
    return {"VersionID": V("2", f"The second version, which supersedes the first: {why2}"),
            "PreviousVersionID": V("1", "The version this one supersedes: version 1 of the same document, with the "
                                        "same number.")}


def contest_prizes(first, why_first):
    return [{"RankCode": V("FIRST", "The first prize."),
             "ValueAmount": amount(first, "XBL", why_first),
             "Description": V("For the design the jury ranks first; its author is invited to negotiate the follow-up "
                              "service contract.", "What comes with the prize.")},
            {"RankCode": V("SECOND", "The second prize."),
             "ValueAmount": amount(4000, "XBL", "The second prize, unchanged since it was planned."),
             "Description": V("For the design the jury ranks second.", "What it is for.")},
            {"RankCode": V("THIRD", "The third prize."),
             "ValueAmount": amount(2000, "XBL", "The third prize."),
             "Description": V("For the design the jury ranks third, if the jury finds it of prize standard.",
                              "The jury may withhold it.")}]


def contest_project():
    return {"Name": V("Design of the harbour promenade bench", "The name of the contest."),
            "Description": V("A bench and matching litter bin and bollard for the 420 m harbour promenade: robust in "
                             "salt air, accessible, and buildable for at most 900 lume a bench.", "What the "
                                                                                                   "department "
                                                                                                   "wants designed."),
            "ProcurementTypeCode": V("SERVICES", "A design is a service."),
            "MainCommodityClassification": {"ItemClassificationCode": V("83912", "The contest is for an industrial "
                                                                                 "design, as a subclass of the UN "
                                                                                 "Central Product Classification.")},
            "RealizedLocation": {"Name": V("Harbour promenade, Lumeport", "Where the furniture will stand."),
                                 "Address": {"CityName": V("Lumeport", "The city."),
                                             "Country": {"IdentificationCode": V("XB", "Bayvarra.")}}},
            "RequestedTenderTotal": {"EstimatedOverallContractAmount": amount(54000, "XBL", "The prizes, 14,000 lume, "
                                                                                           "and the follow-up service "
                                                                                           "contract, estimated at "
                                                                                           "40,000 lume.")}}


def contest_awarding(f, first, why_first):
    return {"Description": V("The jury ranks the designs anonymously, on design quality (40 %), durability and "
                             "maintenance in salt air (30 %) and the cost of production (30 %).", "How the designs "
                                                                                                  "are judged."),
            "TechnicalCommitteeDescription": V("A jury of five: the head of parks, the city architect, a "
                                               "representative of the disability council and two independent "
                                               "designers.", "Who judges."),
            "PrizeIndicator": V("true", "A design contest with prizes."),
            "PrizeDescription": V(f"Three prizes; the first is {first:,} lume.", "The prizes in words; each is "
                                                                                 "given below."),
            "PaymentDescription": V("Each selected participant that submits a design meeting the brief receives "
                                    "1,000 lume towards its costs, whether or not it wins a prize.", "The payment to "
                                    "all participants, besides the prizes."),
            "FollowupContractIndicator": V("true", "The winner of the first prize is invited to negotiate the "
                                                   "service contract for the detailed design and the supervision "
                                                   "of the production, without a new call for competition."),
            "BindingOnBuyerIndicator": V("true", "The jury's ranking binds the department."),
            "Prize": contest_prizes(first, why_first)}


def contest_qualification(k):
    widened = k == 2
    return {"CompanyLegalFormCode": V("LTD", "The legal form the department asks for: a group of designers and "
                                             "engineers must form a private limited company before the follow-up "
                                             "service contract is awarded, as the procurement act allows where the "
                                             "contract needs one liable contractor.", listID=LTD_LIST),
            "CompanyLegalForm": Detail("required of a group of participants, which forms one before the follow-up "
                                       "contract is awarded", "the requirement on groups, as the code states it "
                                       "(D29 point 8, contest/03#F7); for the contest itself a group names a lead "
                                       "member (below)."),
            "Description": V("The design lead is a registered architect or a registered industrial designer."
                             if widened else "The design lead is a registered architect.",
                             "The professional qualification asked for" +
                             (", widened by the corrigendum to industrial designers, whom the earlier text "
                              "excluded without reason." if widened else ".")),
            "TechnicalEvaluationCriterion": {
                "EvaluationCriterionTypeCode": V("REFERENCES", "References."),
                "Description": V("Two completed designs of furniture or fittings for public spaces in the last five "
                                 "years.", "What the jury checks to select the participants."),
                "ThresholdQuantity": qty(2, "EA", "Two references; the five years are the window the references "
                                                  "fall in, stated in the description, not a period the criterion "
                                                  "is valid for (contest/03#F8).")},
            "EconomicOperatorRole": {"RoleCode": V("LEAD", "A group names a lead member for the contest."),
                                     "RoleDescription": V("Represents the group towards the department.",
                                                          "The role in words.")}}


def contest_selection_criteria():
    """The two weighted criteria the jury selects the participants of the restricted contest by."""
    def crit(cid, name, what, weight, why, site=False):
        ask = contest_question(f"P-{cid[3:]}-1", "The reference", "The project, the client, the year and what the "
                               "team designed.", "DESCRIPTION")
        if site:                        # the coastal criterion scores the site, so it asks for it (contest/05#F12)
            ask = [ask, contest_question(f"P-{cid[3:]}-2", "The site", "Where the reference stands and how far it "
                                         "is from the sea.", "DESCRIPTION")]
        return {"ID": V(cid, "The criterion."),
                "CriterionTypeCode": V("TECHNICAL", "Technical and professional ability."),
                "Name": V(name, "The criterion."), "Description": V(what, "What the jury scores."),
                "WeightNumeric": V(str(weight), f"Its weight in the selection: {weight} of 100 points."),
                "EvaluationMethodTypeCode": V("WEIGHTED", "Scored 0 to 10 and weighted."),
                "WeightingConsiderationDescription": V(why, "Why it weighs what it does."),
                "TenderingCriterionPropertyGroup": {
                    "ID": V(f"PG-{cid[3:]}", "The questions on the reference."),
                    "PropertyGroupTypeCode": V("ON", "Always answered."),
                    "TenderingCriterionProperty": ask}}
    return [crit("CR-REF-PUBLIC", "Reference for furniture in public spaces",
                 "The two completed designs of furniture or fittings for public spaces in the last five years that the "
                 "contest notice asks for.", 60,
                 "The main skill the contest asks for, so it weighs most."),
            crit("CR-REF-COAST", "Reference for a coastal site",
                 "Whether one of the two references stands within one kilometre of the sea.", 40,
                 "Salt air is the hardest condition of the promenade, but fewer designers have built for it, so it "
                 "weighs less than the first reference.", site=True)]



# The design team's two references (D29 point 3, O195): both Brackenmere's designs, completed within the five years
# the contest notice asks for; the second stands on a seafront and answers the coastal criterion.
CONTEST_REFERENCES = [
    {"what": "Seating for the reading garden of Lumeport's central library", "client": "the City of Lumeport",
     "year": 2024, "start": "2024-03-01", "end": "2024-09-30", "coast": False,
     "designed": "the benches and the planter seats, made in Brackenmere's workshop"},
    {"what": "Promenade benches for Larkmouth's seafront", "client": "Larkmouth town council", "year": 2023,
     "start": "2023-02-01", "end": "2023-06-30", "coast": True,
     "designed": "the benches of the seafront promenade, bolted to the sea wall's walkway",
     "site": "On the seafront promenade of Larkmouth, Bayvarra's harbour town at the mouth of the east river: the "
             "benches stand on the sea wall's walkway, within 20 metres of the sea."}]


def contest_reference_value(r, rid):
    """One reference as the answer to a question on references: project, client, year and what the team designed."""
    return {"ID": V(rid, "The answer."),
            "Description": V(f"{r['what']}, {r['year']}: client {r['client']}; Brackenmere designed {r['designed']}.",
                             "The project, the client, the year and what the team designed, as the question asks "
                             "(D29 point 3, O195).")}


def contest_completed_task(r):
    return {"Description": V(f"{r['what']}, for {r['client']}, {r['year']}.", "A reference: one of the two the "
                             "contest notice asks for (contest/07#F1, O195)."),
            "Period": {"StartDate": V(r["start"], "From."), "EndDate": V(r["end"], "To: completed within the "
                                                                                    "five years asked.")}}


def contest_question(pid, name, what, dtype):
    return {"ID": V(pid, "The question."), "Name": V(name, "Its name."), "Description": V(what, "What to answer."),
            "TypeCode": V("QUESTION", "A question the participant answers."),
            "ValueDataTypeCode": V(dtype, "The kind of answer it takes.")}


def contest_exclusion_criteria():
    """The exclusion grounds the contest asks about (D29 point 6): convictions; unpaid taxes and social security
    contributions. Each member of a group answers them."""
    def crit(cid, name, what, q, qwhat):
        return {"ID": V(cid, "The exclusion ground."),
                "CriterionTypeCode": V("EXCLUSION", "An exclusion ground: a participant to which it applies is not "
                                                    "selected."),
                "Name": V(name, "The ground."), "Description": V(what, "What excludes a participant."),
                "EvaluationMethodTypeCode": V("PASSFAIL", "It applies or not."),
                "Legislation": {"ID": V("XB-PPA-2019", "Bayvarra's Public Procurement Act."),
                                "Title": V("Public Procurement Act", "Its title."),
                                "Article": V("Art. 57", "The article on the exclusion grounds.")},
                "TenderingCriterionPropertyGroup": {
                    "ID": V(f"PG-{cid[3:]}", "The question on the ground."),
                    "PropertyGroupTypeCode": V("ON", "Always answered."),
                    "TenderingCriterionProperty": contest_question(f"P-{cid[3:]}-1", q, qwhat, "INDICATOR")}}
    return [crit("CR-CONVICTIONS", "Convictions",
                 "A participant is excluded if it, or a member of its management, has been convicted by final "
                 "judgment in the last five years of participation in a criminal organisation, corruption, fraud or "
                 "money laundering.", "Convictions",
                 "Whether the participant, or a member of its management, has been so convicted; in a group, each "
                 "member answers."),
            crit("CR-TAXES", "Payment of taxes and social security contributions",
                 "A participant is excluded if it owes taxes or social security contributions that are due and "
                 "unpaid.", "Unpaid taxes and contributions",
                 "Whether the participant owes taxes or social security contributions that are due and unpaid; in a "
                 "group, each member answers.")]

def contest_process(f, k, call=False):
    requests_by = 87 if k == 2 else 74
    return {"ProcedureCode": V("DESIGNCONTEST", "A design contest."),
            "Description": V("A restricted design contest in two stages: requests to participate, then designs from "
                             "three to five selected participants, judged anonymously.", "How the contest runs."),
            "SubmissionMethodCode": V("ELECTRONIC", "Requests and designs through the department's platform."),
            "ParticipationRequestReceptionPeriod": {
                "EndDate": V(f.date(requests_by), "Requests to participate by then" +
                             (": Thursday 30 April, later than the Friday 17 April of version 1, to give time for the corrected site plan (D29 point 10)."
                              if k == 2 else "."))},
            "TenderSubmissionDeadlinePeriod": {"EndDate": V(f.date(130), "Designs by then."),
                                               "EndTime": V("12:00:00", "At noon.")},
            "EconomicOperatorShortList": {
                "LimitationDescription": V("The jury selects the participants on their references.", "How."),
                "ExpectedQuantity": V("5", "Five participants are expected."),
                "MinimumQuantity": V("3", "At least three, for a real competition."),
                "MaximumQuantity": V("5", "At most five, so that the jury can judge every design in depth.")},
            "ProcessJustification": {
                "PreviousCancellationReasonCode": V("UNSUITABLE", "Why the earlier contest for the same design was "
                                                                  "cancelled."),
                "Description": V(f"Relaunch of the design contest {OLD_FOLDER}, cancelled on 20 November 2025: both "
                                 "designs received were unacceptable, one far above any production budget and one not "
                                 "accessible to wheelchair users. The brief now states both limits.",
                                 "The previous procedure and what changed.")},
            "NoticeDocumentReference": [{"ID": V(f.numbers["contest-pin"], "The prior information notice of the "
                                                                           "contest.")}] +
            ([{"ID": V(f.numbers["contest-notice"], "The contest notice the documents belong to (contest/04#F13)."),
               "VersionID": V(str(k), "The version of the notice they go with.")}] if call else [])}


def contest_terms(f, k, first=8000):
    why_first = ("The first prize, as the city council raised it before the contest was announced."
                 if first == 8000 else "The first prize as first planned.")
    return {"TendererQualificationRequest": contest_qualification(k),
            "AwardingTerms": contest_awarding(f, first, why_first),
            "AppealTerms": {"Description": V("An appeal against the selection or the jury's ranking goes to the "
                                             "review board within ten days.", "How to appeal.")},
            "Language": {"ID": V("en", "Designs and requests in English.")}}


# What each version 2 changes, said in the document itself (D29 point 4, contest/02#F3, 16#F11).
CONTEST_CHANGES = {
    "PriorInformationNotice": "Version 2: on 18 February the city council raised the prize fund from 12,000 to 14,000 "
                              "lume and the first prize from 6,000 to 8,000 lume; the contest notice moves to 19 March.",
    "ContractNotice": "Corrigendum, version 2: the site plan is replaced by revision B (the sea wall is 420 m long, "
                      "not 240 m), the deadline for requests to participate moves from 17 to 30 April, and the "
                      "design lead may also be a registered industrial designer.",
    "CallForTenders": "Version 2: the site plan revision B replaces revision A, and the design lead may also be a "
                      "registered industrial designer, as the corrigendum says.",
    "QualificationApplicationRequest": "Version 2: the design lead may also be a registered industrial designer, as "
                                       "the corrigendum says.",
    "QualificationApplicationResponse": "Version 2: Brackenmere's own industrial designer, Ivo Harlan, now leads the "
                                        "design in place of Saltmere's architect, Edda Corwin.",
    "TendererQualification": "Version 2: Brackenmere now provides the design lead, so the shares of the work move "
                             "from 60 and 40 % to 70 and 30 %.",
    "BusinessInformation": "Version 2: the furniture maker's accounts for 2025, filed on 7 May, replace those for 2024 "
                           "as the yearly production value.",
    "ContractAwardNotice": "Version 2: corrects the first prize from 6,000 to 8,000 lume, the amount the contest "
                           "notice offered; version 1 gave the amount first planned by mistake."}


def contest(n, doc):
    out = contest_document(n, doc)
    if nth("contest", n, doc) == 2 and doc["doc"] in CONTEST_CHANGES:
        change = CONTEST_CHANGES[doc["doc"]]
        note = out.get("Note")
        out["Note"] = V(f"{note.value} {change}" if note else change, (f"{note.why} " if note else "") +
                        "What version 2 changes, said in the document (D29 point 4).")
    return out


def contest_document(n, doc):
    f, d = CONTEST, doc["doc"]
    k = nth("contest", n, doc)
    folder = {"ContractFolderID": V(CFOLDER, "The department's file number for the contest, the same on every "
                                             "document of it.")}
    if d == "PriorInformationNotice":
        first = 6000 if k == 1 else 8000
        out = {"ID": V(f.number("contest-pin", doc["from"], d), "The notice number, the same in both versions."),
               "IssueDate": V(f.date(0 if k == 1 else 21), "Published early, so that designers can plan." if k == 1
                              else "Revised three weeks later."),
               **folder,
               **contest_version(k, "on 18 February the city council raised the prize fund from 12,000 to 14,000 "
                                    "lume, the first prize from 6,000 to 8,000, and the contest notice moves to "
                                    "19 March."),
               "Note": V("Advance notice of the design contest for the harbour promenade bench.", "What it "
                                                                                                    "announces."),
               "PlannedDate": V(f.date(30 if k == 1 else 45), "When the contest notice is planned" +
                                (": later than version 1 said, after the council's decision." if k == 2 else ".")),
               "NoticeTypeCode": V("PIN", "A prior information notice."),
               "ContractingParty": contracting_party_details(),
               "TenderingTerms": {"AwardingTerms": contest_awarding(
                   f, first, "The first prize as first planned." if k == 1 else
                   "The first prize, raised by the city council on 18 February."),
                   "EconomicOperatorShortList": {
                       "LimitationDescription": V("A restricted contest: the jury will select the participants on "
                                                  "their references.", "How the number of participants will be "
                                                                       "limited, announced early."),
                       "MinimumQuantity": V("3", "At least three participants are planned."),
                       "MaximumQuantity": V("5", "At most five.")}},
               "TenderingProcess": {"ProcedureCode": V("DESIGNCONTEST", "A design contest is planned.")},
               "ProcurementProject": contest_project()}
        return out
    if d == "ContractNotice":
        return {"ID": V(f.number("contest-notice", doc["from"], d), "The notice number, the same in both versions."),
                "IssueDate": V(f.date(45 if k == 1 else 63), "Published on the date the revised prior information "
                                                             "notice gave." if k == 1 else
                               "The corrigendum, published as soon as the error was found."),
                **folder,
                **contest_version(k, "a corrigendum. A question from a participant showed that the site plan gave the "
                                     "sea wall as 240 m long; it is 420 m. The corrected plan changes the number of "
                                     "benches, so the deadline for requests to participate is extended to 30 April, "
                                     "and the professional qualification is widened to industrial designers."),
                "Note": V("Restricted design contest for the harbour promenade bench, with three prizes.", "What."),
                "NoticeTypeCode": V("CN-DESG", "A design contest notice (the Accord's list, after the eForms notice "
                                               "type cn-desg; contest/03#F1, D29 point 1); that version 2 corrects "
                                               "version 1 is said by its version identifiers."),
                "ContractingParty": contracting_party_details(),
                "TenderingTerms": contest_terms(f, k), "TenderingProcess": contest_process(f, k),
                "ProcurementProject": contest_project()}
    if d == "CallForTenders":
        plan = ("PWD-PROM-SITE-PLAN-B", "The site plan, revision B: the sea wall is 420 m long, not 240 m as "
                                        "revision A showed.") if k == 2 else \
               ("PWD-PROM-SITE-PLAN-A", "The site plan of the promenade, revision A.")
        return {"ID": V(f.number("contest-call", doc["from"], d), "The number of the contest documents."),
                "IssueDate": V(f.date(46 if k == 1 else 63), "Retrieved by the furniture maker the day after the "
                                                             "notice." if k == 1 else
                               "The revised documents, sent with the corrigendum to everyone who retrieved them."),
                **folder,
                **contest_version(k, "the site plan is replaced by revision B and the selection criterion widened, "
                                     "as the corrigendum says."),
                "Note": V("The brief, the site plan and the rules of the contest. The contest documents are available "
                          "to everyone on the department's platform from the contest notice; this is the set "
                          "Brackenmere Furniture obtained.", "What the documents are, and why they name one receiver "
                          "before the selection (D29 point 7, contest/04#F7)."),
                "TechnicalDocumentReference": {
                    "ID": V("PWD-PROM-BRIEF", "The design brief."),
                    "DocumentType": V("Design brief", "What it is (contest/04#F3)."),
                    "Attachment": {"ExternalReference": {"URI": V(f"https://tenders.lumeport.example/{CFOLDER}/brief",
                                                                  "Where it is obtained: the contest's page on the "
                                                                  "department's platform.")}}},
                "ProvidedDocumentReference": {
                    "ID": V(*plan), "DocumentType": V("Site plan", "What it is."),
                    "VersionID": V("B" if k == 2 else "A", "Its revision, so the change between the versions can be "
                                                          "read (contest/09#F8)."),
                    **({"DocumentDescription": V("Revision B replaces revision A: the sea wall is 420 m long, not "
                                                 "240 m.", "What the revision changes.")} if k == 2 else {}),
                    "Attachment": {"ExternalReference": {"URI": V(f"https://tenders.lumeport.example/{CFOLDER}/"
                                                                  f"site-plan-{'b' if k == 2 else 'a'}", "Where it "
                                                                  "is obtained.")}}},
                "ContractingParty": contracting_party_details(),
                "TenderingTerms": contest_terms(f, k), "TenderingProcess": contest_process(f, k, call=True),
                "ProcurementProject": contest_project()}
    if d == "QualificationApplicationRequest":
        crit = ("registered architect or registered industrial designer" if k == 2 else "registered architect")
        return {**folder, "ID": V(f.number("contest-qar", doc["from"], d), "The number of the self-declaration "
                                                                           "the department asks for."),
                "IssueDate": V(f.date(46 if k == 1 else 63), "Sent with the contest documents." if k == 1 else
                               "Sent with the corrigendum."),
                **contest_version(k, "the criterion on the design lead now admits a registered industrial designer, "
                                     "as the corrigendum says."),
                "ContractName": V("Design of the harbour promenade bench", "The contest."),
                "Note": V("The self-declaration form of the contest, available to every candidate with the contest "
                          "documents; this is the copy Brackenmere Furniture obtained.", "Why it names one economic "
                          "operator before the selection (D29 point 7, contest/05#F7)."),
                "ProcedureCode": V("DESIGNCONTEST", "A design contest."),
                "QualificationApplicationTypeCode": V("REGULATED", "The regulated form of self-declaration."),
                "WeightingTypeCode": V("WEIGHTED", "The selection criteria carry weights: the jury scores the "
                                                   "references to choose three to five participants."),
                "AdditionalDocumentReference": {"ID": V(f.numbers["contest-notice"], "The contest notice whose "
                                                        "criteria this request asks (contest/05#F11)."),
                                                "VersionID": V(str(k), "The version of the notice.")},
                "WeightScoringMethodologyNote": V("The exclusion grounds and the qualification of the design lead "
                                                  "are pass or fail; the two references are scored 0 to 10 and "
                                                  "weighted 60 and 40.", "How the answers count."),
                "TenderingCriterion": [
                    *contest_exclusion_criteria(),
                    {"ID": V("CR-PROF", "The criterion on the design lead."),
                     "CriterionTypeCode": V("SUITABILITY", "A criterion of professional suitability."),
                     "Name": V("Professional qualification of the design lead", "The criterion."),
                     "Description": V(f"The design lead is a {crit}.", "What is asked" +
                                      (", as widened by the corrigendum." if k == 2 else ".")),
                     "EvaluationMethodTypeCode": V("PASSFAIL", "Met or not: a participant whose design lead does "
                                                               "not meet it is not selected. The request states no "
                                                               "fulfilment: nobody has answered yet (contest/05#F3)."),
                     "TenderingCriterionPropertyGroup": {
                         "ID": V("PG-PROF", "The questions on the design lead."),
                         "PropertyGroupTypeCode": V("ON", "Always answered."),
                         "TenderingCriterionProperty": contest_question(
                             "P-PROF-1", "Registration of the design lead",
                             "The design lead's name, the member of the group it belongs to, the register and the "
                             "registration number.", "DESCRIPTION")}},
                    *contest_selection_criteria()]}
    if d == "QualificationApplicationResponse":
        lead = ("Ivo Harlan, Brackenmere Furniture's own industrial designer, is registered as an industrial "
                "designer, no. ID-2208, in the register of the Bayvarran Design Council." if k == 2 else
                "Edda Corwin, the registered architect on Saltmere Engineering's staff, is a registered architect, "
                "no. AR-4417, in the register of the Bayvarran Chamber of Architects.")
        cert = (("EV-REG-ID-2208", "Certificate of registration of the design lead, Ivo Harlan",
                 "Registration no. ID-2208 in the register of industrial designers that the Bayvarran Design Council "
                 "keeps; the council issues the certificate.") if k == 2 else
                ("EV-REG-AR-4417", "Certificate of registration of the design lead, Edda Corwin",
                 "Registration no. AR-4417 in the register of architects that the Bayvarran Chamber of Architects "
                 "keeps; the chamber issues the certificate."))
        members = [(TEAM_LEAD, "Brackenmere Furniture"), (TEAM_MEMBER, "Saltmere Engineering")]

        def each_member(rid, says, why):
            return [{"ID": V(f"{rid}-{i}", f"The answer for {name}: each member of the group answers the "
                                           "exclusion grounds."),
                     "Description": V(f"{name}: {says}", "The answer, for this member."),
                     "ResponseIndicator": V("false", why)} for i, (_, name) in enumerate(members, 1)]

        refs = [contest_reference_value(r, f"RV-REF-PUBLIC-{i}") for i, r in enumerate(CONTEST_REFERENCES, 1)]
        coast = next(r for r in CONTEST_REFERENCES if r["coast"])
        return {**folder, "ID": V(f.number("contest-qar-response", doc["from"], d), "The team's number for its "
                                                                                     "self-declaration."),
                "IssueDate": V(f.date(58 if k == 1 else 71), "With the request to participate." if k == 1 else
                               "Before the extended deadline for requests."),
                **contest_version(k, "the team answers version 2 of the request: the furniture maker's industrial "
                                     "designer now leads the design, and the engineering firm's architect stays in "
                                     "the team for the structure."),
                "ContractName": V("Design of the harbour promenade bench", "The contest."),
                "EconomicOperatorGroupName": V("Brackenmere and Saltmere design team", "The group that enters."),
                "ProcedureCode": V("DESIGNCONTEST", "The contest."),
                "EconomicOperatorParty": [
                    {"EconomicOperatorRole": {"RoleCode": V("LEAD", "Brackenmere answers as the lead member of "
                                                                    "the group (contest/06#F5)."),
                                              "RoleDescription": V("Represents the group towards the department.",
                                                                   "The role in words.")}},
                    {"EconomicOperatorRole": {"RoleCode": V("MEMBER", "Saltmere Engineering is the group's other "
                                                                      "member, for the structure and the anchoring."),
                                              "RoleDescription": V("Designs the structure and the anchoring.",
                                                                   "The role in words.")}}],
                "TenderingCriterion": [{"ID": V(c, "A criterion of the request, answered below: the response "
                                                   "answers every criterion it asks (contest/06#F3).")}
                                       for c in ("CR-CONVICTIONS", "CR-TAXES", "CR-PROF", "CR-REF-PUBLIC",
                                                 "CR-REF-COAST")],
                "TenderingCriterionResponse": [
                    {"ID": V("CRR-CONVICTIONS", "The response on convictions."),
                     "ValidatedCriterionPropertyID": V("P-CONVICTIONS-1", "The question answered."),
                     "ResponseValue": each_member("RV-CONVICTIONS", "no conviction of the member or of its "
                                                  "management.", "No: not convicted.")},
                    {"ID": V("CRR-TAXES", "The response on taxes and contributions."),
                     "ValidatedCriterionPropertyID": V("P-TAXES-1", "The question answered."),
                     "ResponseValue": each_member("RV-TAXES", "no taxes or social security contributions due and "
                                                  "unpaid.", "No: nothing due is unpaid.")},
                    {"ID": V("CRR-PROF", "The response on the design lead."),
                     "ValidatedCriterionPropertyID": V("P-PROF-1", "The question answered."),
                     "ResponseValue": {"ID": V("RV-PROF", "The answer."),
                                       "Description": V(lead, "The answer, in words, as the question asks: the "
                                                              "response itself repeats nothing (contest/06#F12)."),
                                       "ResponseCode": V("MET", "The criterion is met.")},
                     "SuppliedEvidence": {"ID": V(cert[0], "The certificate that proves the registration "
                                                           "(contest/06#F13).")}},
                    {"ID": V("CRR-REF-PUBLIC", "The response on the references."),
                     "ValidatedCriterionPropertyID": V("P-REF-PUBLIC-1", "The question answered: one value for "
                                                                         "each of the two references."),
                     "ResponseValue": refs},
                    {"ID": V("CRR-REF-COAST", "The response on the coastal site: which reference it is."),
                     "ValidatedCriterionPropertyID": V("P-REF-COAST-1", "The question answered."),
                     "ResponseValue": contest_reference_value(coast, "RV-REF-COAST-1")},
                    {"ID": V("CRR-REF-COAST-SITE", "The response on the site of the coastal reference."),
                     "ValidatedCriterionPropertyID": V("P-REF-COAST-2", "The question answered."),
                     "ResponseValue": {"ID": V("RV-REF-COAST-2", "The answer."),
                                       "Description": V(coast["site"], "Where it stands and how far from the sea.")}}],
                "AdditionalDocumentReference": {"ID": V(f.numbers["contest-qar"], "The request this self-"
                                                        "declaration answers (contest/06#F4)."),
                                                "VersionID": V(str(k), "The version of the request answered.")},
                "Evidence": {"ID": V(cert[0], "The certificate of the design lead's registration."),
                             "EvidenceTypeCode": V("CERTIFICATE", "A certificate of registration."),
                             "Name": V(cert[1], "What it is."),
                             "Description": V(cert[2], "Which register, and who issues the certificate.")}}
    if d == "TendererQualification":
        share = ("70", "30") if k == 2 else ("60", "40")
        lead = ("Brackenmere's own industrial designer, Ivo Harlan, leads the design" if k == 2 else
                "Saltmere's registered architect, Edda Corwin, leads the design")
        return {"ID": V(f.number("contest-qualification", doc["from"], d), "The team's number for its "
                                                                            "qualification."),
                **folder,
                "IssueDate": V(f.date(58 if k == 1 else 71), "With the request to participate." if k == 1 else
                               "With the revised self-declaration."),
                **contest_version(k, "the furniture maker now leads the design, so the shares of the work change."),
                "Note": V(f"Brackenmere Furniture leads the team; {lead}; Saltmere Engineering does the structure "
                          "and the anchoring.", "Who does what, and who provides the design lead (D29 point 2, "
                                                "contest/07#F4)."),
                "TendererPartyQualification": {
                    "MainQualifyingParty": {
                        "ParticipationPercent": V(share[0], "The furniture maker's share of the work."),
                        "TendererRoleCode": V("LEAD", "The lead member of the group."),
                        "CompletedTask": [contest_completed_task(r) for r in CONTEST_REFERENCES]},
                    "AdditionalQualifyingParty": {
                        "ParticipationPercent": V(share[1], "The engineering firm's share."),
                        "TendererRoleCode": V("MEMBER", "A member of the group.")}}}
    if d == "BusinessInformation" and doc["parties"]["BusinessParty"] == TEAM_MEMBER:
        legal = PARTY[TEAM_MEMBER]["identity"]["legal"]
        return {"ID": V(f.number("contest-business-info-member", doc["from"], d), "The registry's extract number."),
                "IssueDate": V(f.date(92), "The same day as the lead member's extract: the department checks every "
                                           "member of the team before the jury selects the participants (D29 "
                                           "point 6, contest/13#F4)."),
                "Note": V("Extract from the register of economic operators.", "What it is."),
                "BriefDescription": V("Saltmere Engineering: registered, no exclusion grounds recorded.", "In short."),
                "NoticeTypeCode": V("BUSREG", "Registration information."),
                "BusinessCapability": {
                    "CapabilityTypeCode": V("PRODUCTION", "What the firm produces: its services."),
                    "Description": V("Design and permits of telecom mast sites; installation of back-up power, "
                                     "safety equipment and ground foundations, with its own crews: the yearly value "
                                     f"of its services in {legal['turnover']['year']}, from the accounts filed for "
                                     "that year.", "What the amount measures and for which year."),
                    "ValueAmount": amount(Decimal(legal["turnover"]["amount"]), "XBL",
                                          f"The value of its services in {legal['turnover']['year']} "
                                          "(world/parties.json).")},
                "NoticeSubType": {"SubTypeCode": V("EXTRACT", "An extract on request.")}}
    if d == "TendererQualificationResponse":
        due = Decimal("3860.00")
        return {"ID": V(f.number("contest-exclusion", doc["from"], d), "The department's number for its decision."),
                **folder,
                "ContractName": V("Design of the harbour promenade bench", "The contest."),
                "IssueDate": V(f.date(99), "After the extended deadline for requests (30 April) and the checks of "
                                           "the candidates, when the jury selects the participants."),
                "Note": V("Your request to participate in the design contest cannot be admitted.", "What the "
                                                                                                  "decision is."),
                "QualificationResolution": {
                    "AdmissionCode": V("REJECTED", "The studio is excluded: it is not among the candidates the jury "
                                                   "selects from."),
                    "ExclusionReason": V(f"The certificate of the social security fund shows contributions of "
                                         f"{due:,} lume due since 31 January 2026 and unpaid; amounts above 1,000 lume "
                                         "are not minor and exclude a candidate (Public Procurement Act, art. 57).",
                                         "Why it is excluded: the exclusion ground on unpaid taxes and social security "
                                         "contributions that the contest asks about (D29 point 6, O102)."),
                    "Resolution": V("Excluded at the selection of the participants.", "The decision in words."),
                    "ResolutionDate": V(f.date(99), "The day the department decided.")},
                "AppealTerms": {"Description": V("An appeal against the exclusion goes to the review board within "
                                                 "ten days of this notice.", "How to appeal, as the contest notice "
                                                                             "says."),
                                "PresentationPeriod": {"DurationMeasure": V("10", "Ten days.", unitCode="DAY")}}}
    if d == "BusinessInformation":
        turnover = (Decimal(PARTY[TEAM_LEAD]["identity"]["legal"]["turnover"]["amount"]) if k == 2
                    else BRACKENMERE_TURNOVER_2024)
        return {"ID": V(f.number("contest-business-info", doc["from"], d), "The registry's extract number, the same "
                                                                           "in both versions."),
                "IssueDate": V(f.date(92 if k == 1 else 95), "The department checks the lead member when the jury "
                                                             "selects the participants." if k == 1 else
                               "The day after the accounts were filed."),
                **contest_version(k, "the furniture maker filed its accounts for 2025 on " + f.date(94) + ", and the "
                                     "registry issues the extract again with the new turnover."),
                "Note": V("Extract from the register of economic operators.", "What it is."),
                "BriefDescription": V("Brackenmere Furniture: registered, no exclusion grounds recorded.", "In short."),
                "NoticeTypeCode": V("BUSREG", "Registration information."),
                "BusinessCapability": {
                    "CapabilityTypeCode": V("PRODUCTION", "Production capacity."),
                    "Description": V(f"Furniture of wood and steel, designed and made in its own workshop: the yearly "
                                     f"production value of {2025 if k == 2 else 2024}, from the accounts filed for that "
                                     "year.", "What the amount measures and for which year (D29 point 6, "
                                              "contest/13#F3)."),
                    "ValueAmount": amount(turnover, "XBL", "The value of what it produced in 2025, as its accounts "
                                          "for 2025 give it." if k == 2 else "The value of what it produced in 2024, "
                                          "from the last accounts filed.")},
                "NoticeSubType": {"SubTypeCode": V("EXTRACT", "An extract on request.")}}
    if d == "ContractAwardNotice":
        first = 6000 if k == 1 else 8000
        return {"ID": V(f.number("contest-result", doc["from"], d), "The notice number, the same in both versions."),
                **folder,
                "IssueDate": V(f.date(150 if k == 1 else 154), "Published after the jury's decision." if k == 1 else
                               "The correction, two working days later (D29 point 10)."),
                **contest_version(k, "version 1 gave the first prize as 6,000 lume, the amount first planned; the "
                                     "contest notice offered 8,000, and 8,000 is paid."),
                "Note": V("Results of the design contest for the harbour promenade bench.", "What."),
                "NoticeTypeCode": V("CAN-DESG", "A design contest result notice (the Accord's list, after the eForms "
                                                "notice type can-desg; contest/15#F3, D29 point 1)."),
                "PreviousDocumentReference": {"ID": V(f.numbers["contest-notice"], "The contest notice.")},
                "ContractingParty": contracting_party_details(),
                "TenderingTerms": {"AwardingTerms": {"Prize": contest_prizes(first, "Wrongly given as the amount "
                                                                                    "first planned." if k == 1 else
                                                     "The amount the contest notice offered.")[:2]}},
                "TenderingProcess": {
                    "ProcedureCode": V("DESIGNCONTEST", "A design contest."),
                    "CandidateReductionConstraintIndicator": V("true", "The number of candidates was reduced: the "
                                                                       "jury selected five participants from the "
                                                                       "requests, as the notice announced. Stated "
                                                                       "here, after the selection, not in the notice "
                                                                       "and the call (contest/03#F10)."),
                    "NegotiationDescription": V("The service contract for the detailed design and the supervision of "
                                                "the production is negotiated with the first-prize winner, without a "
                                                "new call for competition, on fees, timetable and the number of "
                                                "prototypes.", "The negotiation that follows the contest."),
                    "EconomicOperatorShortList": {
                        "LimitationDescription": V("Only the winner of the first prize is invited to negotiate the "
                                                   "follow-up contract, as the contest notice announced.",
                                                   "Why one party."),
                        "PreSelectedParty": [party(TEAM_LEAD, short=True), party(TEAM_MEMBER, short=True)]}},
                "ProcurementProject": contest_project(),
                "TenderResult": {
                    "TenderResultCode": V("AWARDED", "The prizes are awarded."),
                    "Description": V("First prize to the Brackenmere and Saltmere design team, second to Valdara "
                                     "Industries. The jury withheld the third prize: no other design reached prize "
                                     "standard.", "The jury's decision."),
                    "AwardDate": V(f.date(144), "The day the jury decided: Friday 26 June (D29 point 10)."),
                    "ReceivedTenderQuantity": qty(4, "EA", "Four of the five selected participants submitted a "
                                                           "design."),
                    "ReceivedForeignTenderQuantity": qty(1, "EA", "Valdara Industries, from Urvania."),
                    "WinningParty": [{"Rank": V("1", "First prize: the lead member of the winning team.")},
                                     {"Rank": V("1", "First prize: the team's other member, a winner as much as its "
                                                     "lead (D29 point 2, contest/15#F2).")},
                                     {"Rank": V("2", "Second prize.")}]}}
    raise SystemExit(f"contest scenario: no document {n} {doc['doc']}")


FLOWS["contest"] = CONTEST
SCENARIOS["contest"] = _with_enrichment("contest", contest)


# ---------------------------------------------------------------- cards: a shop on the island, a webshop order
def island_shop_receipt(n, doc):
    """Velumi Trading's shop in Selanu sells two of the benches it imported to the cotton farm, paid with the farm's
    Coralcard at the till; the till prints the first six and the last four digits of the card number."""
    f = SEA
    day, time = 40, "10:25:00"
    out = kit.purchase_receipt(f, n, doc, day, "The farm buys after the season's first cotton payments.",
                               [{"item": "bench-serra-x", "qty": 2, "why": "Two benches for the pickers' rest place "
                                                                          "under the trees by the weighing shed."}],
                               cash=False)
    total = out["LegalMonetaryTotal"]["PayableAmount"]
    out.update({"IssueTime": V(time, "Printed at the till."),
                "Note": V("Collected by the farm with its own trailer.", "Printed on the receipt."),
                "TransactionDate": V(f.date(day), "The day of the sale."),
                "TransactionTime": V(time, "The time of the sale."),
                "CashRegister": {"ID": V("T1", "The shop's only till.")},
                "PointOfSaleLocation": {"Name": V("Velumi Trading, Reef Street, Selanu", "The shop.")}})
    out["PaymentMeans"] = {
        "PaymentMeansCode": V("55", "UN/EDIFACT 4461 code 55: debit card.", listID="UN/EDIFACT EDED 4461"),
        "CardAccount": {**kit.card_account("38-xl", "1-xl"), "RoleCode": V("HOLDER", "Paid by the card holder.")}}
    out["Payment"] = {"ID": V("VT-T1-26-0613-0012", "The till's number for the payment."),
                      "PaidAmount": total, "PaidDate": V(f.date(day), "Paid at the till."),
                      "PaidTime": V(time, "At the time of the sale."),
                      "MerchantID": V("CORALCARD-M-0001859", "The shop's merchant number with the card scheme."),
                      "AuthorizationID": V("C30417", "The approval code of the card issuer, the Bank of Selanu."),
                      "PaymentTerminalID": V("PT-T1", "The card terminal at the till."),
                      "StatusCode": V("APPROVED", "The payment was approved.")}
    return out


def sea_complete(n, doc):
    if doc["doc"] == "PurchaseReceipt":
        return island_shop_receipt(n, doc)
    return sea_with_debit(n, doc)


SCENARIOS["sea"] = _with_enrichment("sea", sea_complete)


WEBSHOP_SET = [{"item": f"marrow-bench-{WEBSHOP_WOOD}-r", "ordered": 1, "why": "The bench of the Marrow set: the customer chose ash "
                                                                  "for the set."},
               {"item": f"marrow-chair-{WEBSHOP_WOOD}-r", "ordered": 2, "why": "The two chairs of the Marrow set, in ash like the "
                                                                   "bench."},
               {"item": "marrow-care-kit-r", "ordered": 1, "why": "The care kit that comes free with the bench."}]
SET_ALLOWANCE = Decimal("48.00")


def webshop_order(n, doc):
    """The consumer orders a Marrow set (an Elderwick Marrow bench and two chairs, with the bench's free care kit) in
    the store's webshop, to collect in the store, and pays by credit card. The set is an offer, not an item: one line
    per piece and the "Marrow set" allowance of 48 lume, 947 less 48 = 899 (D32). A card payment that is not made at a till is authorised before the goods are reserved: the order carries
    the full card number, its dates and its security code, which PCI DSS allows a merchant to hold until the
    authorisation and never after; no receipt shows them."""
    f = RETAIL
    card = PARTY["c-xb"]["identity"]["credit_card"]
    issuer = PARTY[card["issuer"]]["identity"]
    start = f"{card['valid_from']}-01"
    y, m = (int(x) for x in card["expires"].split("-"))
    end = (datetime.date(y + m // 12, m % 12 + 1, 1) - datetime.timedelta(days=1)).isoformat()
    out = kit.order(f, n, doc, 40, "Placed in the webshop on Saturday 30 May.",
                    "Ex works the store: the customer collects the set; there is no transport to arrange.",
                    "Home and garden department of the Lumeport store",
                    {"Note": V("Click and collect: ready in the home and garden department from Tuesday 2 June; "
                               "bring the "
                               "card used "
                               "for the order.", "What the webshop tells the customer."),
                     "Delivery": {"DeliveryLocation": {**kit.gln_location("26-xb", "garden"),
                                                       "Name": V("Home and garden department, Lumeport store",
                                                                 "Where the "
                                                                                                    "set is "
                                                                                                    "collected.")},
                                  "RequestedDeliveryPeriod": {"StartDate": V(f.date(43), "From Tuesday 2 June."),
                                                              "EndDate": V(f.date(50), "The store keeps it a week.")}},
                     "PaymentMeans": {
                         "PaymentMeansCode": V("54", "UN/EDIFACT 4461 code 54: credit card.",
                                               listID="UN/EDIFACT EDED 4461"),
                         "CardAccount": {
                             "PrimaryAccountNumberID": V(card["pan"], "The full card number the customer typed in: "
                                                                      "the store needs it to have the payment "
                                                                      "authorised. It starts with 9 and the numeric "
                                                                      "code of the issuer's country (902, Bayvarra), "
                                                                      "as ISO/IEC 7812 provides for national use, so "
                                                                      "it is no real card's; its last digit is the "
                                                                      "Luhn check digit."),
                             "NetworkID": V(card["scheme"], "Tressa, the Accord-wide credit card scheme."),
                             "CardTypeCode": V(card["type"], "A credit card."),
                             "ValidityStartDate": V(start, f"The card is valid from {card['valid_from']}, the "
                                                           "month printed on it: its first day."),
                             "ExpiryDate": V(end, f"The card expires at the end of {card['expires']}, the month "
                                                  "printed on it: its last day. The issuer checks it in the "
                                                  "authorisation."),
                             "IssuerID": V(issuer["bic"], f"The card's issuer, {issuer['name']}, by its bank "
                                                          "identifier.",
                                           schemeID="urn:ubl-examples:world:bank-identifier"),
                             "CV2ID": V(card["cv2"], "The card's security code from the back of the card, typed in "
                                                     "by the customer, so that the issuer can check that the card "
                                                     "is at hand. PCI DSS allows the store to hold it only until the "
                                                     "authorisation; it is deleted then and printed nowhere."),
                             "HolderName": V(card["holder"], "The name on the card, as typed in."),
                             "RoleCode": V("HOLDER", "The customer pays with its own card.")}}},
                    deal=WEBSHOP_SET, key="webshop-order")
    out["ID"] = V(f.number("webshop-order", "26-xb", "Order"), "The webshop's order number: the store's site writes "
                                                               "the order for the customer and numbers it.")
    rows = kit.lines(f, "26-xb", "c-xb", "XBL", deal=WEBSHOP_SET)
    base = sum(r[2] for r in rows)
    rule = kit.tax_rule("26-xb", "c-xb", WEBSHOP_SET[0]["item"])
    tax, total = kit.tax_total(rows + [({"item": WEBSHOP_SET[0]["item"]}, None, -SET_ALLOWANCE, rule)], "XBL")
    total["TaxSubtotal"][0]["TaxableAmount"] = amount(base - SET_ALLOWANCE, "XBL", "The line amounts less the set "
                                                                                  "allowance.")
    out["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance: it lowers the amount."),
                              "AllowanceChargeReasonCode": V("95", "The reason for the allowance as a code of "
                                                                   "UN/EDIFACT 5189: a discount; the text names the "
                                                                   "offer."),
                              "AllowanceChargeReason": V("Marrow set", "The shop's offer: a bench and two chairs "
                                                                       "in the same wood bought together cost 899 "
                                                                       "lume instead of 947. The set is no item of "
                                                                       "its own, so the "
                                                                       "pieces are on their lines and the offer is "
                                                                       "this allowance."),
                              "Amount": amount(SET_ALLOWANCE, "XBL", "549 + 2 × 199 = 947, less 48 = 899."),
                              "TaxCategory": kit.tax_category(rule)}
    out["TaxTotal"] = total
    out["AnticipatedMonetaryTotal"] = {
        "LineExtensionAmount": amount(base, "XBL", "The sum of the line amounts: the pieces at their shelf prices."),
        "AllowanceTotalAmount": amount(SET_ALLOWANCE, "XBL", "The set allowance."),
        "PayableAmount": amount(base - SET_ALLOWANCE + tax, "XBL", "What the customer pays: the set at 899 lume and "
                                                                    "Coastal State's 6.5 % sales tax.")}
    return out


def retail_with_webshop(n, doc):
    if doc["doc"] == "Order" and doc["from"] == "c-xb":
        return webshop_order(n, doc)
    return retail_complete(n, doc)


SCENARIOS["retail"] = _with_enrichment("retail", retail_with_webshop)


# ---------------------------------------------------------------- cotton: the self-billed prepayment of the advance
def cotton_advance(n, doc):
    """Before the harvest the ginnery advances the farm a quarter of the value of its expected delivery, and writes
    the prepayment invoice itself under the self-billing agreement (UN/EDIFACT 1001 code 386). The final self-billed
    invoice deducts it as the prepaid amount."""
    f = COTTON
    day = -20
    out = kit.self_billed(f, n, doc, day, "Three weeks before the first deliveries, when the farm needs cash for the "
                                          "picking.",
                          [{"item": "seed-cotton", "qty": ADVANCE_KG,
                            "why": "A quarter of the 18,000 kg the farm expects to deliver: the share the season "
                                   "agreement advances."}],
                          {"ContractDocumentReference": {"ID": V("SCG-SEASON-2026", "The season agreement between "
                                                                                    "farm and ginnery, which sets "
                                                                                    "the advance and allows the "
                                                                                    "self-billing.")}})
    out.update({
        "InvoiceTypeCode": V("386", "UN/EDIFACT 1001 code 386, prepayment invoice: \"An invoice to pay amounts for "
                                    "goods and services in advance; these amounts will be subtracted from the final "
                                    "invoice.\" A subtype the root SelfBilledInvoice does not say by itself (decision "
                                    "P-SB)."),
        "Note": V("Self-billed prepayment under the season agreement: the advance is deducted from the first "
                  "self-billed invoice of the season.", "The statement the self-billing agreement requires, and what "
                                                        "happens to the advance."),
        "DueDate": V(f.date(day), "An advance is paid on the day it is billed, not on the island's usual 45 days."),
        "PaymentTerms": {"Note": V("Paid on issue by transfer. No presumptive tax is withheld and no cotton fund levy "
                                   "is collected on the advance: both fall on the delivery, in the final self-billed "
                                   "invoice.", "Why the advance is paid in full.")},
        "PayeeParty": party("38-xl", short=True),
        "Signature": {"ID": V("SCG-SIG-26-0001", "The ginnery's seal on the self-billed prepayment invoice."),
                      "SignatoryParty": party("39-xl", short=True)}})
    out["PaymentMeans"]["PaymentDueDate"] = V(f.date(day), "Paid on issue, as the season agreement says for the "
                                                           "advance: the contract's term, not the island's 45 days "
                                                           "(D22).")
    lmt = out["LegalMonetaryTotal"]
    if Decimal(lmt["PayableAmount"].value) != ADVANCE:
        raise SystemExit(f"cotton: the advance is {lmt['PayableAmount'].value}, not {ADVANCE}")
    return out


def cotton_with_advance(n, doc):
    if doc["doc"] == "SelfBilledInvoice" and nth("cotton", n, doc) == 1:
        return cotton_advance(n, doc)
    return cotton(n, doc)


SCENARIOS["cotton"] = _with_enrichment("cotton", cotton_with_advance)


# ---------------------------------------------------------------- cotton: the feeder's report before Lumeport
def cotton_ctr(n, doc):
    """The pre-arrival report of Tidewell's second feeder, which carries the cotton container to Lumeport: an interim
    security certificate since its change of flag, and a ship sanitation control exemption certificate."""
    f = COTTON
    master = kit.person("Hester", "Calloway", "The master.", role="MASTER")
    return {"ID": V(f.number("ctr", doc["from"], "CommonTransportationReport"), "The carrier's report number."),
            "IssueDate": V(f.date(29), "Sent the day before the ship enters Lumeport."),
            "ReportTypeCode": V("PREARRIVAL", "The report before entering the port."),
            "ReportType": V("Pre-arrival report", "In words."),
            "TransportMeans": kit.means("11-xb", "TR", "TR-26-09W", "The voyage from Selanu back to Lumeport.", "WB"),
            "Shipment": {"ID": V(f.number("ctr-shipment", doc["from"], "Shipment"), "The carrier's shipment number "
                                                                                    "for the voyage's cargo."),
                         "ShipmentStage": {
                             "ID": V("1", "The sea leg from Selanu to Lumeport."),
                             "ReportingPerson": master,
                             "ISPSRequirements": {
                                 "ID": V("IISSC-XB-2026-0115", "The number of the ship's interim International Ship "
                                                               "Security Certificate."),
                                 "ValidISSCIndicator": V("false", "The ship has no full certificate yet."),
                                 "ISSCAbsenceReason": V("The ship came under Bayvarra's flag on 15 January 2026 and "
                                                        "sails with an interim certificate (ISPS Code A/19.4), valid "
                                                        "for six months; the flag state's verification for the full "
                                                        "certificate is set for April.", "Why the ship has no full "
                                                                                         "certificate, which the "
                                                                                         "port needs to know."),
                                 "ISSCExpiryDate": V("2026-07-14", "The interim certificate's last day: six months, "
                                                                   "the most the ISPS Code allows."),
                                 "CurrentOperatingSecurityLevelCode": V("1", "Security level 1, the normal level."),
                                 "SSPOnBoardIndicator": V("true", "The ship security plan is on board."),
                                 "AdditionalMattersDescription": V("The ship was searched for stowaways before it "
                                                                   "left Selanu, because the port facility had "
                                                                   "reported a gap in its perimeter fence on 1 March. "
                                                                   "Nothing was found.", "A security matter the port "
                                                                                         "should know about."),
                                 "ISSCIssuerParty": party("ma-xb", short=True)},
                             "MaritimeHealthDeclaration": {
                                 "ID": V("MDH-26-0303", "The maritime declaration of health."),
                                 "InfectiousDiseaseCaseOnBoardIndicator": V("false", "No infectious disease."),
                                 "SanitaryMeasuresAppliedIndicator": V("false", "No sanitary measures on this "
                                                                                "voyage."),
                                 "ValidSanitationCertificateOnBoardIndicator": V("true", "The exemption certificate "
                                                                                         "is valid until July."),
                                 "TotalIllPersonQuantity": qty(0, "IE", "No one ill."),
                                 "SickAnimalOnBoardIndicator": V("true", "A sick animal is on board: the ship's "
                                                                         "cat."),
                                 "SickAnimalDescription": V("The ship's cat has been off its food and listless for "
                                                            "three days. It is kept in the master's cabin, away from "
                                                            "the cargo and the galley; the master asks for a "
                                                            "veterinarian at Lumeport.", "What the port health "
                                                                                         "authority needs to know "
                                                                                         "about the animal."),
                                 "ShipSanitationControlExemptionDocumentReference": {
                                     "ID": V("SSCEC-XB-2026-0114", "The ship sanitation control exemption "
                                                                   "certificate: the ship carries it instead of a "
                                                                   "control certificate. Unique only with its issuer "
                                                                   "(decision ID-Q10)."),
                                     "IssueDate": V("2026-01-14", "Issued after the inspection at Lumeport, before "
                                                                  "the ship's first voyage for the line; valid six "
                                                                  "months."),
                                     "DocumentDescription": V("Ship Sanitation Control Exemption Certificate "
                                                              "(International Health Regulations 2005, Annex 3): "
                                                              "the inspection found no evidence of infection or "
                                                              "contamination, so no control measures were needed.",
                                                              "What the document is."),
                                     "IssuerParty": party("16-xb", short=True)}}}}}


def cotton_complete(n, doc):
    if doc["doc"] == "CommonTransportationReport":
        return cotton_ctr(n, doc)
    return cotton_with_advance(n, doc)


SCENARIOS["cotton"] = _with_enrichment("cotton", cotton_complete)
