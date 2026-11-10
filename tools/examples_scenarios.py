"""Scenarios of the example flows: what a flow adds to the world's layers.

Per flow: its start date, its deal (the items and quantities it is about) and,
per document, the day it is issued and what is particular to it, each value with
its reason. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers;
lines, amounts and taxes are worked out by tools/examples_kit.py.
"""
import uuid
from decimal import Decimal

import examples_kit as kit
from build_examples import ITEM, PARTY, WORLD, V, address, amount, item, money, party, price, qty


def rate(a, b):
    """The world's reference exchange rate: units of b for one unit of a (world/countries.json)."""
    return Decimal(str(WORLD["exchange_rates"][f"{a}/{b}"]))


# ---------------------------------------------------------------- the ore flow (Urvania, domestic)
ORE = kit.Flow("ore", "2026-03-02", [
    {"item": "ore-lump", "ordered": 1800, "delivered": "1788.4",
     "why": "One train: 30 wagons of about 60 tonnes.",
     "invoice_why": "The weighed quantity from the despatch advice, not the ordered quantity.",
     "line_allowance": {"percent": "1.5", "code": "95", "code_why": "UN/EDIFACT 5189 code 95: discount.",
                        "reason": "Moisture deduction",
                        "why": "The sample at loading showed 7.5 % moisture, above the 6 % of the contract: the "
                               "contract deducts 1.5 % of the value."},
     "line_tax": True}])


def ore(n, doc):
    f = ORE
    weighed_kg = Decimal("1788.4") * 1000
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The first working day of the month: the monthly ore call-off.",
                         "Free carrier at the mine: the buyer arranges and pays the main transport, so the order names "
                         "the carrier the buyer has booked. Stated, because leaving it out would carry no meaning "
                         "(UBL rule IND6).", "Mine siding, Serravona",
                         {"Note": V("Monthly call-off, one train.", "Says in words what the order is for."),
                          "Delivery": {"RequestedDeliveryPeriod": {
                              "StartDate": V(f.date(7), "The week in which the factory wants the ore."),
                              "EndDate": V(f.date(11), "The end of that week.")}}})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 1, "The day after the order: the buyer books the train it named in its order.",
                               8, 1800000, "The expected weight: the ordered quantity.")
    if doc["doc"] == "TransportExecutionPlan":
        return kit.tep(f, n, doc, 2, "The day after the request.", 8, 1800000)
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 8, "The day the train was loaded and weighed.",
                                   "Weighed on the weighbridge at loading: 30 wagons.",
                                   {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                         "The buyer's consignment, quoted back.")}}})
    if doc["doc"] == "Waybill":
        return kit.waybill(f, n, doc, 8, "Issued when the carrier takes over the loaded train.", weighed_kg,
                           "The weight the carrier takes over, from the weighbridge.")
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return kit.invoice(f, n, doc, 10, 30, "Issued after the carriage was performed.",
                           {"AdditionalDocumentReference": [
                               {"ID": V(f.numbers["tep"], "The transport plan with the agreed price.")},
                               {"ID": V(f.numbers["waybill"], "The consignment note of the carriage invoiced.")}]},
                           [{"item": "rail-ore", "qty": "1788.4",
                             "invoice_why": "The weight carried, from the consignment note: the freight is per tonne."}],
                           key="freight-invoice")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 9, 30, "Issued the day after the goods were despatched and weighed.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                            "DespatchDocumentReference": {"ID": V(f.numbers["despatch"],
                                                                  "The despatch advice of the goods invoiced.")}})
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The day the payment is made, one day before the due date.")
    raise SystemExit(f"ore scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the road flow (Urvania -> Bayvarra)
ROAD = kit.Flow("road", "2026-03-16", [
    {"item": "bench-serra", "ordered": 96, "why": "24 pallets of 4 benches: one full truck."},
    {"item": "bench-casting", "ordered": 12, "why": "Spare side frames, for the distributor's service stock."}])
DISTANCE_KM = 186     # the carrier's route from the 3PL in Ferrano to the distributor in Marrowdale


def goods_items(f, currency, value_why, convert=None):
    """GoodsItem per line of the deal, with the customs value and the item (HS code, origin)."""
    out = []
    for i, d in enumerate(f.deal, 1):
        it = ITEM[d["item"]]
        value = Decimal(str(d["ordered"])) * Decimal(str(it["price"]["amount"]))
        if convert:
            value = value * rate(it["price"]["currency"], currency)
        out.append({"ID": V(str(i), "The goods item number."),
                    "Description": V(it["name"], "What the goods are, in words."),
                    "DeclaredCustomsValueAmount": amount(value, currency, value_why),
                    "GrossWeightMeasure": qty(Decimal(str(d["ordered"])) * Decimal(str(it["gross_kg"])), "KGM",
                                              "The gross weight of the goods of this item."),
                    "Quantity": qty(d["ordered"], it["unit"], "The quantity declared."),
                    "Item": item(d["item"])})
    return out


ROAD_JOB = "TH-26-04471"          # the carrier's job number for the truck


def road_stage(f, actual):
    """The main carriage by truck: Ferrano to Marrowdale, across the land border."""
    stage = {"ID": V("1", "The only stage: one truck from the warehouse to the distribution centre."),
             "TransportModeCode": V("3", "UN/ECE Recommendation 19 code 3: road transport.",
                                    listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
             "TransportMeansTypeCode": V("TE", "The truck pulls a trailer."),
             "TransitDirectionCode": V("Export", "The goods leave Urvania by this stage."),
             "CabotageIndicator": V("false", "A carriage between two countries, not within a foreign one."),
             "TransitPeriod": {"StartDate": V(f.date(7), "Collected in the afternoon."),
                               "EndDate": V(f.date(9), "Delivered in the morning, after the night rest of the "
                                                       "driver and the border.")},
             "TransportMeans": kit.means("13-xu", "T-07", ROAD_JOB, "The carrier's job number, the same on every "
                                                                   "document of this truck.", "Westbound"),
             "DriverPerson": kit.person("Ilario", "Bencetti", "The driver of the truck.", "XU-DL-0417722"),
             "LoadingPortLocation": kit.place("XUFER", "Loaded at the 3PL's warehouse in Ferrano."),
             "UnloadingPortLocation": kit.place("XBMRW", "Unloaded at the distributor's distribution centre."),
             "EstimatedDeliveryDate": V(f.date(9), "The carrier's estimate when it takes over the goods."),
             "EstimatedDeliveryTime": V("09:00:00", "Early in the working day."),
             "RequiredDeliveryDate": V(f.date(9), "The distributor's goods-in slot."),
             "RequiredDeliveryTime": V("10:00:00", "The slot starts at ten.")}
    if actual:
        stage["ActualDepartureTransportEvent"] = kit.event(f, 7, "16:20:00", "The truck left the warehouse.",
                                                           kit.place("XUFER", "Castrano Logistics warehouse."))
        stage["ExaminationTransportEvent"] = kit.event(f, 8, "07:45:00", "Customs looked at the seals at the border.",
                                                       description="Seal check, no inspection of the goods.")
    return stage


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
        out["RequestedDeliveryTransportEvent"] = kit.event(f, 9, "10:00:00", "The distributor's goods-in slot.",
                                                           kit.place("XBMRW", "The distribution centre."))
        out["CarrierServiceInstructions"] = V("Curtain-side trailer; the goods are loaded from the side by forklift.",
                                              "What the carrier must bring.")
        return out
    out.update({
        "CarrierAssignedID": V(ROAD_JOB, "The carrier's job number."),
        "ConsignorAssignedID": V(f.numbers["despatch"], "The consignor's reference: its despatch advice."),
        "ConsigneeAssignedID": V("LD-GI-0412", "The distributor's goods-in booking for the slot."),
        "NetWeightMeasure": qty(net, "KGM", "The weight of the goods without packaging."),
        "LoadingLengthMeasure": V("9.3", "Five rows of bench pallets, two high, and the castings: 9.3 m of the "
                                         "13.6 m floor.", unitCode="MTR"),
        "Remarks": V("Received in apparent good order; seals XU-CL-77310 on the trailer doors.",
                     "The driver's remarks at taking over, as the consignment note asks."),
        "ThirdPartyPayerIndicator": V("false", "The consignee, who booked the truck, pays the freight."),
        "HaulageInstructions": V("Wait at the warehouse until customs has released the export declaration.",
                                 "What the driver must do before leaving."),
        "CustomsClearanceServiceInstructions": V("The export is declared by the 3PL in Ferrano; the import by the "
                                                 "distributor at the border.", "Who clears the goods through customs."),
        "DeliveryInstructions": V("Unload at dock 4; report to the gatehouse first.", "Where to go on arrival."),
        "TotalPackagesQuantity": qty(sum(int(Decimal(str(x["ordered"]))) for x in d), "H87",
                                     "96 benches and 12 boxed frames."),
        "TotalTransportHandlingUnitQuantity": qty(25, "H87", "25 pallets."),
        "ActualPickupTransportEvent": kit.event(f, 7, "15:05:00", "When the carrier took over the goods.",
                                                kit.place("XUFER", "The 3PL's warehouse.")),
        "DeliveryTerms": {"ID": V("FCA", "Incoterms 2020: free carrier at the seller's warehouse."),
                          "LossRiskResponsibilityCode": V("Buyer", "The risk passed to the buyer when the goods were "
                                                                   "loaded on the truck."),
                          "LossRisk": V("The risk passes on loading at the 3PL's warehouse.", "In words."),
                          "SpecialTerms": V("The buyer's carrier presents the truck; the seller loads it.",
                                            "Who loads, under FCA at the seller's premises.")},
        "CollectPaymentTerms": {"Note": V("The freight is paid by the consignee under its contract with the carrier.",
                                          "Freight collect: the consignee pays.")},
        "CustomsDeclaration": {"ID": V(f.numbers["export-declaration"], "The export declaration the goods travel "
                                                                        "under."),
                               "IssuerParty": party("19-xu", short=True)},
        "MainCarriageShipmentStage": road_stage(f, True),
        "TransportHandlingUnit": kit.handling_units(f, d, "CL-26-", "LD MARROWDALE", detail=True)})
    return out


def road(n, doc):
    f = ROAD
    weight = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The distributor orders for its spring stock.",
                         "Free carrier at the seller's warehouse: the buyer arranges and pays the main transport, so the "
                         "order names the warehouse where the goods are collected and the carrier that collects them "
                         "(UBL rule IND6: the delivery terms are stated, not implied).",
                         "Castrano Logistics warehouse, Ferrano",
                         {"Delivery": {
                             "ID": V("LD-DL-26-0412", "The distributor's number for this delivery."),
                             "Quantity": qty(108, "H87", "All 108 pieces in one delivery."),
                             "MinimumQuantity": qty(108, "H87", "No part deliveries: the truck is booked for all."),
                             "MaximumQuantity": qty(108, "H87", "And no more than ordered."),
                             "DeliveryAddress": address("6-xb"),
                             "AlternativeDeliveryLocation": {"Description": V(
                                 "Gate B of the business park, if dock 4 is blocked.", "Where to go instead.")},
                             "MinimumDeliveryUnit": {"BatchQuantity": qty(4, "H87", "Benches come in pallets of "
                                                                                    "four."),
                                                     "ConsumerUnitQuantity": qty(1, "H87", "One bench.")},
                             "MaximumDeliveryUnit": {"BatchQuantity": qty(100, "H87", "A truck takes at most 25 "
                                                                                      "pallets of four.")},
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
                                                      "EndDate": V(f.date(7), "The same day.")},
                           "Despatch": {
                               "EstimatedDespatchDate": V(f.date(7), "The goods will be ready on the requested day."),
                               "EstimatedDespatchTime": V("14:00:00", "At the requested time."),
                               "GuaranteedDespatchDate": V(f.date(8), "At the latest the next day."),
                               "GuaranteedDespatchTime": V("12:00:00", "By noon."),
                               "EstimatedDespatchPeriod": {"StartDate": V(f.date(7), "The afternoon of day 7."),
                                                           "EndDate": V(f.date(8), "Or the morning after.")},
                               "ResponsibleParty": party("8-xu", short=True),
                               "NotifyParty": party("6-xb", short=True)}}
        bench, frame = ITEM["bench-serra"], ITEM["bench-casting"]
        out["OrderResponseCode"] = V("CA", "UN/EDIFACT 4343 code CA: conditionally accepted, with the substitution "
                                           "of line 2.")
        out["Note"] = V("Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the "
                        "same price.", "The condition in words.")
        out["OrderLine"] = [
            {"LineItem": {"ID": V("1", "The benches."), "LineStatusCode": V("NoStatus", "Accepted as ordered."),
                          "Quantity": qty(96, "H87", "As ordered."),
                          "Item": {"Name": V(bench["name"], "Named only."),
                                   "SellersItemIdentification": {"ID": V(bench["sellers_id"], "The seller's "
                                                                                              "number.")}}},
             "OrderLineReference": {"LineID": V("1", "The order line.")}},
            {"LineItem": {"ID": V("2", "The side frames, as ordered."),
                          "LineStatusCode": V("Revised", "Changed by the seller."),
                          "Quantity": qty(12, "H87", "As ordered."),
                          "Item": {"Name": V(frame["name"], "The frame ordered."),
                                   "SellersItemIdentification": {"ID": V(frame["sellers_id"], "Its number.")}}},
             "SubstitutionStatusCode": V("Substitution", "The line is delivered with a substitute item."),
             "Note": V("Same fit and price; the old casting is no longer made.", "Why the substitute is offered."),
             "SellerSubstitutedLineItem": {
                 "ID": V("2", "The substitute for line 2."),
                 "Quantity": qty(12, "H87", "The same quantity."),
                 "Price": kit.price_block("bench-casting"),
                 "Item": {"Name": V("Bench side frame casting, 2026", "The substitute."),
                          "SellersItemIdentification": {"ID": V(frame["sellers_id"], "The same item number."),
                                                        "ExtendedID": V("2026", "The new version.")}}},
             "SellerProposedSubstituteLineItem": {
                 "ID": V("2", "What the seller would also accept to ship, if the buyer prefers."),
                 "Quantity": qty(12, "H87", "The same quantity."),
                 "Item": {"Name": V("Bench side frame casting, 2025, from stock", "Six left in stock; the rest would "
                                                                                  "follow in May."),
                          "SellersItemIdentification": {"ID": V(frame["sellers_id"], "The item number."),
                                                        "ExtendedID": V("2025", "The old version.")}}},
             "OrderLineReference": {"LineID": V("2", "The order line."),
                                    "SalesOrderLineID": V("2", "The seller's line.")}}]
        return out
    if doc["doc"] == "TransportExecutionPlanRequest":
        out = kit.tep_request(f, n, doc, 1, "The distributor books the truck once the order is accepted.", 7, weight,
                              "The gross weight of the order: benches and castings with their packaging.")
        kit.deep_merge(out["Consignment"], road_consignment(f, "request"))
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
                                                     "ActualDespatchTime": V("16:20:00", "The truck left the gate."),
                                                     "ReleaseID": V("XU-EX-REL-55120", "The export release customs "
                                                                                       "gave before the truck left.")}}}})
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
        chamber, exporter = "20-xu", "5-xu"
        endorsed = doc["from"] == chamber
        signer = {"RoleCode": V("Chamber", "The endorser is the chamber of commerce of the exporting country."),
                  "SequenceNumeric": V("1", "The first and only endorsement."),
                  "Party": party(chamber),
                  "SignatoryContact": {"Name": V("Certificates office", "The office of the chamber that signs "
                                                 "certificates of origin.")}}
        return {
            "EndorserParty": {k: v for k, v in signer.items() if k != "Party"},
            "ID": V(f.number("certificate", chamber, "CertificateOfOrigin"), "The number of the certificate, given by "
                                                                            "the chamber."),
            "IssueDate": V(f.date(6 if endorsed else 4), "The day the chamber endorsed the certificate." if endorsed
                           else "The day the exporter applies, before the goods leave."),
            "Description": V("Certificate of origin for park benches and castings made in Urvania.",
                             "What the certificate is for."),
            "CertificateOfOriginApplication": {
                "ReferenceID": V(f.number("certificate-application", exporter, "Application"),
                                 "The exporter's reference for its application."),
                "CertificateType": V("Preferential", "The goods qualify for the preferential duty rate in Bayvarra; "
                                                     "the importer needs this certificate to claim it."),
                "ApplicationStatusCode": V("Approved" if endorsed else "Submitted",
                                           "The chamber has approved the application." if endorsed
                                           else "The exporter submits the application."),
                "OriginalJobID": V(f.numbers["order"], "The order the goods are for."),
                "Shipment": {"ID": V(f.number("shipment", "8-xu", "Shipment"), "The shipment the certificate covers."),
                             "GoodsItem": goods_items(f, "XUF", "The value of the goods, in ferra.")},
                "EndorserParty": signer,
                "PreparationParty": party(exporter),
                "IssuerParty": party(chamber),
                "IssuingCountry": {"IdentificationCode": V("XU", "The goods were made in Urvania, and the certificate is "
                                                                 "issued there.")}},
            "IssuerEndorsement": {
                "DocumentID": V(f.numbers["certificate"], "The certificate this endorsement belongs to."),
                "ApprovalStatus": V("Approved" if endorsed else "Pending", "The chamber has endorsed the certificate."
                                    if endorsed else "Not yet endorsed: the application is with the chamber."),
                "EndorserParty": signer}}
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 7, "Issued when the carrier collects the goods at the warehouse.", weight,
                          "The gross weight the carrier takes over.")
        net = sum(Decimal(str(x["ordered"])) * Decimal(str(ITEM[x["item"]]["net_kg"])) for x in f.deal)
        kit.deep_merge(out["Shipment"], {
            "NetNetWeightMeasure": qty(net, "KGM", "The goods alone, without any packaging."),
            "GrossVolumeMeasure": V("41.5", "The volume of the 25 loaded pallets.", unitCode="MTQ"),
            "TotalGoodsItemQuantity": qty(2, "H87", "Two kinds of goods: benches and side frames."),
            "SplitConsignmentIndicator": V("false", "The whole consignment travels on this truck."),
            "ConsignmentQuantity": qty(1, "H87", "One consignment on the truck."),
            "HandlingCode": V("Upright", "The carrier's handling code: keep upright."),
            "Information": V("Steel street furniture for resale.", "What the goods are, for the driver."),
            "ExportCountry": {"IdentificationCode": V("XU", "The goods are exported from Urvania.")},
            "OriginAddress": address("8-xu"),
            "ReturnAddress": address("8-xu"),
            "Consignment": road_consignment(f, "note"),
            "Delivery": {"TrackingID": V(ROAD_JOB, "Track the truck with the carrier's job number."),
                         "EstimatedDeliveryPeriod": {"StartDate": V(f.date(9), "The morning of the third day."),
                                                     "StartTime": V("09:00:00", "From nine."),
                                                     "EndTime": V("11:00:00", "Until eleven.")},
                         "LatestDeliveryDate": V(f.date(9), "The goods-in slot cannot move."),
                         "LatestDeliveryTime": V("12:00:00", "Dock 4 closes for the lunch change.")}})
        return out
    if doc["doc"] == "TransportationStatus":
        border = {"Name": V("Land border crossing Urvania–Bayvarra",
                            "The road border crossing between the customs posts of both countries.")}
        return {"ID": V(f.number("status", doc["from"], "TransportationStatus"), "The carrier's status report number."),
                "IssueDate": V(f.date(8), "The morning after collection, when the truck has crossed the border."),
                "IssueTime": V("09:10:00", "Sent as soon as the truck was through."),
                "TransportationStatusTypeCode": V("Progress", "A report on the progress of the carriage."),
                "TransportEvent": kit.event(
                    f, 8, "08:55:00", "The day and time the truck crossed the land border.", border,
                    type_code="BorderCrossing", ident=f"{ROAD_JOB}-E03",
                    description="Border crossing passed; customs cleared on both sides.", done=True,
                    Period={"StartTime": V("07:30:00", "The truck joined the queue at the border."),
                            "EndTime": V("08:55:00", "And left the customs post.")},
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
                        "ConditionCode": V("OnTime", "The carriage runs to plan."),
                        "ReferenceDate": V(f.date(9), "The delivery the status is measured against."),
                        "ReferenceTime": V("10:00:00", "The start of the goods-in slot."),
                        "Description": V("In transit in Bayvarra, expected at the distribution centre on time.",
                                         "The status in words."),
                        "StatusReasonCode": V("Cleared", "Why: the border is behind it."),
                        "StatusReason": V("Customs released the goods at the border.", "In words."),
                        "SequenceID": V("3", "The third report on this truck: collection, departure, border."),
                        "Text": V("Driver resting in Marrowdale tonight under the driving-time rules.",
                                  "A note for the consignee."),
                        "IndicationIndicator": V("true", "The status applies: the truck is on time."),
                        "Percent": V("70", "The share of the route driven."),
                        "ReliabilityPercent": V("90", "How sure the carrier is of the arrival time."),
                        "Condition": {"AttributeID": V("Seal", "The condition checked."),
                                      "Description": V("Intact, as checked by customs.", "Its state.")},
                        "DocumentationAttachment": {"ExternalReference": {
                            "URI": V("https://www.trasvia.example/tracking/TH-26-04471/seal.jpg", "A photograph of "
                                                                                                  "the seal."),
                            "MimeCode": V("image/jpeg", "A photograph.")}},
                        "SubStatus": {"ConditionCode": V("Released", "The customs part of the status."),
                                      "Description": V("Import declaration accepted by Bayvarra's customs.",
                                                       "In words.")}}),
                "Consignment": {"ID": V(f.numbers["consignment"], "The consignment the report is about."),
                                "CarrierAssignedID": V(ROAD_JOB, "The carrier's job number."),
                                "Status": {"ConditionCode": V("InTransit", "The consignment is on its way."),
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
                                        "ActualDeliveryTime": V("09:40:00", "Within the slot."),
                                        "DeliveryNoteDocumentReference": {"ID": V(f.numbers["waybill"], "The "
                                                                                  "consignment note signed on "
                                                                                  "delivery.")}}}
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "13-xu":
        return kit.invoice(f, n, doc, 9, 30, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note of the "
                                                                                          "carriage invoiced.")}},
                           [{"item": "road-transport", "qty": DISTANCE_KM,
                             "invoice_why": "The kilometres driven loaded, from Ferrano to Marrowdale."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {
                               "ID": V(f.numbers["consignment"], "The consignment carried, as the distributor numbered "
                                                                 "it when booking the truck."),
                               "ActualDeliveryTransportEvent": kit.event(f, 9, "09:40:00", "Delivered at dock 4: the "
                                                                         "carriage invoiced is complete.")},
                               "GoodsItem": {"ID": V("1", "The benches carried."),
                                             "ReceiptLineReference": {
                                                 "LineID": V("1", "The line of the consignee's receipt advice."),
                                                 "DocumentReference": {"ID": V(f.numbers["receipt"], "The receipt "
                                                                               "advice: proof of delivery.")}}}}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 8, 30, "Issued when the goods have left the warehouse.",
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
        return kit.remittance(f, n, doc, 37, "The day the payment is made across the border, before the due date.")
    raise SystemExit(f"road scenario: no document {n} {doc['doc']}")


SCENARIOS = {"ore": ore, "road": road}


# ---------------------------------------------------------------- the rail flow (Urvania -> Bayvarra, DAP, transit)
RAIL = kit.Flow("rail", "2026-04-06", [
    {"item": "bench-serra", "ordered": 192, "why": "Two containers of 24 pallets, 4 benches on each pallet."}])


RAIL_BOXES = [kit.container_number("FRC", 104417), kit.container_number("FRC", 104418)]
RAIL_SEALS = ["XU-VI-30411", "XU-VI-30412"]


def rail_container(f, k, full):
    """One of the two 40-foot containers of the rail flow: Ferrano Rail Cargo's own boxes."""
    box, seal = RAIL_BOXES[k], RAIL_SEALS[k]
    wagon = kit.fleet("14-xu", "FRC-4417")["wagons"][k]
    out = {"ID": V(box, "The container's number: owner code, U for a freight container, six digits and the ISO 6346 "
                        "check digit.", schemeID="ISO6346"),
           "ReferencedConsignmentID": V(f.numbers["consignment"], "The consignment the container carries."),
           "TransportEquipmentTypeCode": V("CN", "UN/EDIFACT 8053 code CN: container.", listID="UN/EDIFACT EDED 8053"),
           "SizeTypeCode": V("45G1", "ISO 6346 size and type: 40 feet long, 9 ft 6 in high, general purpose."),
           "FullnessIndicationCode": V("FCL", "A full container load for one consignee."),
           "GrossWeightMeasure": qty(kit.gross_weight(f, "ordered") / 2 + 3900, "KGM", "Half the benches and the "
                                     "container's own 3,900 kg."),
           "TransportEquipmentSeal": {"ID": V(seal, "The number of the bolt seal on the doors."),
                                      "SealIssuerTypeCode": V("Shipper", "The seal was issued by the shipper."),
                                      "SealingPartyType": V("Shipper", "And put on by the shipper when it packed "
                                                                       "the container."),
                                      "Condition": V("Intact", "As found at the hub."),
                                      "SealStatusCode": V("Applied", "The seal is in place.")}}
    if not full:
        return out
    out.update({
        "ProviderTypeCode": V("Carrier", "The rail carrier provides the container."),
        "OwnerTypeCode": V("Carrier", "And owns it."),
        "DispositionCode": V("Loaded", "Loaded with cargo."),
        "Information": V("Return empty to the Ferrano hub within five days.", "What happens to the box afterwards."),
        "ReturnabilityIndicator": V("true", "The container goes back to its owner."),
        "LegalStatusIndicator": V("false", "Not under a customs container convention; the goods travel under transit."),
        "Characteristics": V("Steel, high cube, wooden floor.", "What kind of box it is."),
        "Description": V("40-foot high cube container", "The container in words."),
        "DamageRemarks": V("Small dent in the left side panel, noted at pick-up; no effect on the cargo.",
                           "Damage noted at the hub, so it is not blamed on this carriage."),
        "SpecialTransportRequirements": V("Load with the doors to the rear of the wagon.", "How it rides."),
        "GrossVolumeMeasure": V("76.3", "The inside volume of a 40-foot high cube.", unitCode="MTQ"),
        "TrackingDeviceCode": V("GPS", "The box carries a satellite tracker."),
        "PowerIndicator": V("false", "It needs no power: not a reefer."),
        "TraceID": V(f"TRK-{box}", "The tracker's number."),
        "StowagePositionID": V(f"{wagon} / A", "The wagon and the slot on it the box rides in."),
        "MeasurementDimension": {"AttributeID": V("Length", "The outside length."),
                                 "Measure": V("12192", "Forty feet.", unitCode="MMT")},
        "OwnerParty": party("14-xu", short=True),
        "OperatingParty": party("18-xu", short=True),
        "ProviderParty": party("14-xu", short=True),
        "LoadingProofParty": party("8-xu", short=True),
        "LoadingLocation": kit.place("XUFER", "Packed at the 3PL's warehouse in Ferrano."),
        "UnloadingLocation": kit.place("XBMRW", "Unpacked at the distributor's siding."),
        "StorageLocation": {"Name": V("Ferrano Intermodal Hub, stack C", "Where the box waited for the train.")},
        "PositioningTransportEvent": kit.event(f, 6, "08:00:00", "The empty box was delivered to the warehouse "
                                                                 "for packing."),
        "PickupTransportEvent": kit.event(f, 7, "15:00:00", "Collected packed from the warehouse."),
        "HandlingTransportEvent": kit.event(f, 7, "18:30:00", "Stacked at the hub overnight."),
        "LoadingTransportEvent": kit.event(f, 8, "05:40:00", "Lifted onto the wagon."),
        "DeliveryTransportEvent": kit.event(f, 9, "11:00:00", "Planned arrival at the siding.", done=False),
        "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The freight for this box."),
                                   "AllowanceChargeReason": V("Rail freight per container", "In words."),
                                   "Amount": amount(ITEM["rail-container"]["price"]["amount"],
                                                    ITEM["rail-container"]["price"]["currency"],
                                                    "The price of one container slot (world/items.json).")},
        "ContainedInTransportEquipment": {"ID": V(wagon, "The container wagon the box rides on."),
                                          "TransportEquipmentTypeCode": V("RR", "UN/EDIFACT 8053 code RR: rail car.",
                                                                          listID="UN/EDIFACT EDED 8053")},
        "ApplicableTransportMeans": {"RailTransport": {"TrainID": V("FRC 4417", "The train."),
                                                       "RailCarID": V(wagon, "The container wagon it rides on.")}},
        "HaulageTradingTerms": {"Information": V("Carrier haulage: the rail carrier brings the box to the warehouse "
                                                 "and back.", "Who moves the empty box."),
                                "Reference": V("FRC-HT-2026", "The carrier's haulage terms.")},
        "Pickup": {"ActualPickupDate": V(f.date(7), "Collected."), "ActualPickupTime": V("15:00:00", "At three."),
                   "PickupLocation": {"Name": V("Castrano Logistics warehouse, Ferrano", "Where.")}},
        "Despatch": {"ActualDespatchDate": V(f.date(8), "The train left the hub."),
                     "ActualDespatchTime": V("06:50:00", "Ten to seven.")},
        "Delivery": {"LatestDeliveryDate": V(f.date(10), "At the latest."),
                     "DeliveryLocation": {"Name": V("Rail siding of Lumeway Distribution, Marrowdale", "Where.")}},
        "ShipmentDocumentReference": {"ID": V(f.numbers.get("waybill", "pending"), "The rail consignment note.")}
        if f.numbers.get("waybill") else {"ID": V(f.numbers["tep"], "The transport plan.")}})
    return out


def rail_stage(f, actual):
    out = {"ID": V("1", "The main carriage, by rail."),
           "TransportModeCode": V("2", "UN/ECE Recommendation 19 code 2: rail transport.",
                                  listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
           "TransportMeans": kit.means("14-xu", "FRC-4417", "CT 4471", "The number of the container train in the "
                                                                       "hub's timetable.", "Westbound"),
           "LoadingSequenceID": V("7", "The order the boxes go on the train: these two are the seventh lift."),
           "SuccessiveSequenceID": V("1", "The first and only rail stage."),
           "Instructions": V("Shunt to the Lumeway siding on arrival in Marrowdale.", "What the railway must do."),
           "DemurrageInstructions": V("Free time five days at the siding, then demurrage per container day.",
                                      "What waiting costs."),
           "CrewQuantity": qty(2, "C62", "A driver and a train manager."),
           "PassengerQuantity": qty(0, "C62", "A freight train carries no passengers."),
           "PlannedDepartureTransportEvent": kit.event(f, 8, "06:45:00", "The timetable departure from the hub."),
           "PlannedArrivalTransportEvent": kit.event(f, 9, "10:30:00", "The timetable arrival in Marrowdale."),
           "EstimatedDepartureTransportEvent": kit.event(f, 8, "06:50:00", "The departure as expected that morning."),
           "EstimatedArrivalTransportEvent": kit.event(f, 9, "10:40:00", "The arrival as expected.")}
    if actual:
        out["ActualDepartureTransportEvent"] = kit.event(f, 8, "06:52:00", "The train left the hub.",
                                                         {"Name": V("Ferrano Intermodal Hub", "Where.")})
        out["PlannedWaypointTransportEvent"] = kit.event(f, 8, "13:00:00", "Planned passage of the border station.")
        out["ActualWaypointTransportEvent"] = kit.event(f, 8, "13:20:00", "The train passed the border station.")
    return out


def rail_offices():
    def office(name, why):
        return {"Name": V(name, why)}
    return {"OfficeOfDepartureLocation": office("Customs office Ferrano Intermodal Hub", "Where the transit starts."),
            "OfficeOfExitLocation": office("Customs post at the rail border station, Urvanian side",
                                           "Where the goods leave Urvania."),
            "OfficeOfTransitLocation": office("Customs post at the rail border station, Bayvarran side",
                                              "Where the transit is checked on entering Bayvarra."),
            "OfficeOfEntryLocation": office("Customs post at the rail border station, Bayvarran side",
                                            "Where the goods enter Bayvarra."),
            "OfficeOfDestinationLocation": office("Customs office Marrowdale", "Where the transit ends and the "
                                                                               "goods are declared for import."),
            "OfficeOfImportLocation": office("Customs office Marrowdale", "Where the import is declared.")}


def rail_consignment(f, view):
    out = {"ID": V(f.numbers["consignment"], "The manufacturer's consignment number."),
           "ContainerizedIndicator": V("true", "Two full containers."),
           "SummaryDescription": V("192 park benches in two 40-foot containers.", "The goods in a few words.")}
    if view == "request":
        out["RequestedPickupTransportEvent"] = kit.event(f, 7, "15:00:00", "The boxes are packed by then.")
        out["RequestedDeliveryTransportEvent"] = kit.event(f, 10, None, "The distributor expects them on day 10.")
        out["MainCarriageShipmentStage"] = {
            "ID": V("1", "The rail carriage asked for."),
            "RequestedDepartureTransportEvent": kit.event(f, 8, "07:00:00", "The morning train from the hub."),
            "RequestedWaypointTransportEvent": kit.event(f, 8, None, "Via the border station, where the transit "
                                                                     "is checked.",
                                                         {"Name": V("Rail border station Urvania–Bayvarra", "The "
                                                                                                            "waypoint.")}),
            "RequestedArrivalTransportEvent": kit.event(f, 9, None, "Arriving the next day.")}
        return out
    out["TransportContract"] = {"ID": V("FRC-CON-2026-005", "The framework contract for container slots."),
                                "IssueDate": V("2026-01-05", "Signed at the start of the year."),
                                "ContractType": V("Framework contract for container slots", "What it is.")}
    out["PrepaidPaymentTerms"] = {"Note": V("Freight prepaid by the consignor under DAP.", "The seller pays the "
                                                                                          "carriage.")}
    if view == "plan":
        out["PlannedPickupTransportEvent"] = kit.event(f, 7, "15:00:00", "The carrier collects the packed boxes.")
        out["PlannedDeliveryTransportEvent"] = kit.event(f, 9, "11:00:00", "And places them at the siding.")
        out["MainCarriageShipmentStage"] = rail_stage(f, False)
        return out
    out.update({
        "PerformingCarrierAssignedID": V("FRC-J-26-3318", "The rail carrier's job number."),
        "LoadingSequenceID": V("7", "The consignment's turn in the loading of the train."),
        "ContractedCarrierAssignedID": V("FRC-CON-2026-005/88", "The call-off under the framework contract."),
        "TotalTransportHandlingUnitQuantity": qty(2, "C62", "Two containers."),
        "PerformingCarrierParty": party("14-xu", short=True),
        "EnvironmentalEmission": {
            "EnvironmentalEmissionTypeCode": V("CO2e", "Greenhouse gases of the carriage, as CO2 equivalent."),
            "ValueMeasure": V("410", "For the two containers over the route.", unitCode="KGM"),
            "EmissionCalculationMethod": {
                "CalculationMethodCode": V("Calculated", "From the electric train's energy use."),
                "MeasurementFromLocation": {"Name": V("Ferrano Intermodal Hub", "From.")},
                "MeasurementToLocation": {"Name": V("Marrowdale", "To.")},
                "EmissionCalculationLocation": {"Name": V("Ferrano Rail Cargo, energy office", "Where the figure was "
                                                                                               "calculated.")}}},
        "MainCarriageShipmentStage": rail_stage(f, True),
        "TransportHandlingUnit": [{"TransportEquipment": rail_container(f, k, k == 0),
                                   "CustomsDeclaration": {"ID": V(f.numbers["transit"], "The transit declaration "
                                                                                       "the box travels under."),
                                                          "IssuerParty": party("19-xu", short=True)},
                                   "EnergyConsumptionAllocation": {
                                       "EnergySourceTypeCode": V("Electricity", "The train runs on electricity."),
                                       "AllocatedEnergyMeasure": V("610", "This box's share of the train's energy, "
                                                                          "by weight.", unitCode="KWH")}}
                                  for k in range(2)]})
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
                              8, w, "Two containers of benches.")
        kit.deep_merge(out["Consignment"], rail_consignment(f, "request"))
        return out
    if doc["doc"] == "TransportExecutionPlan":
        out = kit.tep(f, n, doc, 2, "The rail carrier confirms the slots on the container train.", 8, w)
        kit.deep_merge(out["Consignment"], rail_consignment(f, "plan"))
        return out
    if doc["doc"] == "TransitCustomsDeclaration":
        return {"ID": V(f.number("transit", doc["from"], "TransitCustomsDeclaration"), "The transit declaration "
                                                                                       "number."),
                "IssueDate": V(f.date(8), "Lodged at the office of departure before the train leaves."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment under transit."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight under transit."),
                             "GoodsItem": kit.goods_items(f, "XUF", "The value of the goods, in ferra, for the transit "
                                                                    "guarantee."),
                             "Consignment": {"ID": V(f.numbers["consignment"], "The consignment on the train."),
                                             **rail_offices(),
                                             "TransportHandlingUnit": [{"TransportEquipment": rail_container(f, k, False)}
                                                                       for k in range(2)]}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 8, "Reported when the containers are on the train.",
                                         "Two containers loaded on the container train.",
                                         "Ferrano Intermodal Hub",
                                         {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("1", "The main carriage, by rail."),
                                             "ActualPickupTransportEvent": kit.event(f, 7, "15:00:00", "The boxes "
                                                                                     "were collected from the "
                                                                                     "warehouse."),
                                             "OptionalTakeoverTransportEvent": kit.event(
                                                 f, 8, "17:00:00", "If the morning train is full, the boxes go on the "
                                                                   "evening train.", done=False),
                                             "DeliveryTransportEvent": kit.event(f, 9, "11:00:00", "Planned "
                                                                                 "placement at the siding.",
                                                                                 done=False),
                                             "TransportEvent": kit.event(f, 8, "05:40:00", "Both boxes lifted onto "
                                                                                           "the train.", done=True)}}})
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 8, "Issued when the carrier takes over the containers.", w,
                          "The gross weight of the two containers' cargo.")
        kit.deep_merge(out["Shipment"]["Consignment"], rail_consignment(f, "note"))
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "14-xu":
        return kit.invoice(f, n, doc, 11, 30, "Issued after delivery at the siding.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "rail-container", "qty": 2, "invoice_why": "Two container slots."}],
                           key="freight-invoice")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 11, 30, "Issued on delivery at the distributor's siding.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
                           extra={"Note": V("Delivered at place: the price includes the carriage to the siding.",
                                            "Why the invoice has no separate freight line.")})
    raise SystemExit(f"rail scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the plastics flow (Urvania -> Bayvarra, barge, CPT)
PLASTICS = kit.Flow("plastics", "2026-04-13", [
    {"item": "granulate-pe", "ordered": 120, "why": "One barge load of recycled granulate in jumbo bags."}])


BARGE_VOYAGE = "FB4-26-031"


def barge_stage(f, actual):
    out = {"ID": V("1", "Down the river, from the recovery plant's quay to the river quay in Lumeport."),
           "TransportModeCode": V("8", "UN/ECE Recommendation 19 code 8: inland water transport.",
                                  listID="UNECE Recommendation 19 - Codes for Modes of Transport"),
           "TransportMeans": kit.means("15-xu", "FB-4", BARGE_VOYAGE, "The barge operator's voyage number.",
                                       "Downstream"),
           "MasterPerson": kit.person("Tomaso", "Riverra", "The skipper of the barge.", job="Skipper"),
           "LoadingPortLocation": {"Name": V("Quay of Rinova Recovery, Ferrano", "Where the bags are loaded.")},
           "UnloadingPortLocation": {"Name": V("River quay, Lumeport", "The place named in the CPT terms.")},
           "EstimatedTransitPeriod": {"DurationMeasure": V("3", "Three days downstream, with the locks.",
                                                           unitCode="DAY")},
           "TakeoverTransportEvent": kit.event(f, 6, "09:00:00", "The barge operator takes over the bags at the "
                                                                 "quay."),
           "LoadingTransportEvent": kit.event(f, 6, "13:30:00", "Loading finished: 120 bags in the hold."),
           "ExportationTransportEvent": kit.event(f, 7, "16:00:00", "The barge leaves Urvania at the river border."),
           "DischargeTransportEvent": kit.event(f, 9, "08:00:00", "Planned unloading at the Lumeport quay.",
                                                done=False)}
    return out


def barge_goods(f, w):
    it = ITEM["granulate-pe"]
    goods_xuf = Decimal("120") * Decimal(str(it["price"]["amount"]))
    return {"ID": V("1", "The only goods item."),
            "SequenceNumberID": V("1", "Its place in the cargo list."),
            "Description": V(it["name"], "What the goods are."),
            "ValueAmount": amount(goods_xuf, "XUF", "The value of the goods, the sales price under CPT."),
            "DeclaredForCarriageValueAmount": amount(goods_xuf, "XUF", "Declared to the barge operator, which raises "
                                                                       "its liability to this value."),
            "GrossWeightMeasure": qty(w, "KGM", "With the bags."),
            "NetWeightMeasure": qty(120000, "KGM", "The granulate alone."),
            "NetNetWeightMeasure": qty(120000, "KGM", "No inner packaging: the same as the net weight."),
            "ChargeableWeightMeasure": qty(120000, "KGM", "The freight is charged per tonne of granulate."),
            "GrossVolumeMeasure": V("204", "The 120 bags take 1.7 m³ each.", unitCode="MTQ"),
            "NetVolumeMeasure": V("130", "The granulate's own volume, at 0.92 tonne per m³.", unitCode="MTQ"),
            "ChargeableQuantity": qty(120, "TNE", "The tonnes charged."),
            "ReturnableQuantity": qty(120, "H87", "The 120 jumbo bags go back to the recovery plant."),
            "TraceID": V("RR-PE-LOT-26-0416", "The lot on the bags' labels."),
            "Quantity": qty(120, "TNE", "120 tonnes."),
            "OriginAddress": address("7-xu"),
            "ContainingPackage": {"ID": V("JB-001..120", "The bags, numbered 1 to 120."),
                                  "Quantity": qty(120, "H87", "120 bags."),
                                  "PackagingTypeCode": V("JB", "UN/ECE Recommendation 21 code JB: bag, jumbo."),
                                  "PackagingType": V("Jumbo bag of one tonne with four lifting loops", "In words."),
                                  "PackingMaterial": V("Woven polypropylene", "What the bags are made of."),
                                  "ReturnableMaterialIndicator": V("true", "The bags go back for reuse.")},
            "MeasurementDimension": {"AttributeID": V("Height", "The height of one filled bag."),
                                     "Measure": V("1300", "In millimetres.", unitCode="MMT")},
            "Pickup": {"EarliestPickupDate": V(f.date(6), "The bags are ready on the quay."),
                       "EarliestPickupTime": V("08:00:00", "From eight."),
                       "LatestPickupDate": V(f.date(6), "They must go the same day."),
                       "LatestPickupTime": V("16:00:00", "Before the quay closes.")},
            "Despatch": {"ActualDespatchDate": V(f.date(6), "The barge cast off."),
                         "ActualDespatchTime": V("15:10:00", "In the afternoon.")},
            "Delivery": {"LatestDeliveryDate": V(f.date(10), "The packaging maker's production starts the day "
                                                             "after.")},
            "OrderLineReference": {"LineID": V("1", "The order line."),
                                   "OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
            "DespatchLineReference": {"LineID": V("1", "The line of the despatch advice."),
                                      "DocumentReference": {"ID": V(f.numbers.get("despatch", "-"),
                                                                    "The despatch advice.")}}
            if f.numbers.get("despatch") else None,
            "ShipmentDocumentReference": {"ID": V(f.numbers["tep"], "The transport plan of the sailing.")},
            "EnergyConsumptionAllocation": {"EnergySourceTypeCode": V("Diesel", "The barge's engine fuel."),
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
                "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The freight, a charge."),
                                           "AllowanceChargeReason": V("River freight", "What it is for."),
                                           "Amount": amount(Decimal("179400"), "XUF", "120 tonnes at 1,495 ferra."),
                                           "BaseAmount": amount(Decimal("1495"), "XUF", "The rate per tonne.")}})
    return out


def plastics(n, doc):
    f = PLASTICS
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 0, "The packaging maker orders for the next production run.",
                         "Carriage paid to the river quay: the seller books and pays the barge, the buyer bears the "
                         "risk once the goods are on board.", "River quay, Lumeport")
    if doc["doc"] == "OrderResponse":
        return kit.order_response(f, n, doc, 1, "The waste processor confirms the lot.")
    if doc["doc"] == "TransportExecutionPlanRequest":
        out = kit.tep_request(f, n, doc, 1, "Under CPT the seller is the transport user and books the barge.", 6, w,
                              "120 jumbo bags of one tonne, with their bags.")
        kit.deep_merge(out["Consignment"], barge_consignment(f, "request"))
        return out
    if doc["doc"] == "TransportExecutionPlan":
        out = kit.tep(f, n, doc, 2, "The barge operator confirms the sailing.", 6, w)
        kit.deep_merge(out["Consignment"], barge_consignment(f, "plan"))
        return out
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 6, "Declared the day the barge is loaded.",
                                      "The value of the granulate, in ferra.")
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 6, "Issued when the barge is loaded.", w, "The gross weight on board.")
        kit.deep_merge(out["Shipment"]["Consignment"], barge_consignment(f, "note"))
        g = barge_goods(f, w)
        out["Shipment"]["GoodsItem"] = {k: v for k, v in g.items() if v is not None}
        return out
    if doc["doc"] == "Invoice" and doc["from"] == "15-xu":
        return kit.invoice(f, n, doc, 9, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "barge-freight", "qty": 120, "invoice_why": "The tonnes carried."}],
                           key="freight-invoice")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 6, "The day the barge was loaded.", "The gross weight loaded.")
    if doc["doc"] == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, 9, "Declared when the barge arrives at the coast.",
                                     "The customs value in lume: the invoice value in ferra at the world's reference "
                                     "rate (1 ferra = 0.01 lume).")
        kit.deep_merge(out["Shipment"]["GoodsItem"][0], {
            "FreeOnBoardValueAmount": amount(Decimal("98046"), "XBL", "The value at the loading quay: the CPT price "
                                             "less the river freight of 179,400 ferra, in lume."),
            "DeclaredStatisticsValueAmount": amount(Decimal("99840"), "XBL", "The value for the trade statistics: "
                                                    "the invoice value at the border."),
            "InsuranceValueAmount": amount(Decimal("0"), "XBL", "The buyer did not insure the river carriage."),
            "PreferenceCriterionCode": V("P", "The goods are wholly obtained in Urvania: preference criterion P of "
                                              "the trade accord."),
            "RequiredCustomsID": V("3901.10.00", "The tariff code Bayvarra's customs requires on the declaration."),
            "CustomsStatusCode": V("Foreign", "Bayvarra's customs status: goods from abroad, not yet released for "
                                              "free circulation."),
            "CustomsProcedureCode": V("4000", "Release for free circulation, with no previous procedure."),
            "CustomsTariffQuantity": qty(120000, "KGM", "The quantity in the tariff's unit: net kilograms."),
            "CustomsImportClassifiedIndicator": V("true", "Classified by the importer before arrival."),
            "BondedWarehouseLocation": {"Name": V("Bonded store at the river quay, Lumeport", "Where the bags wait "
                                                                                             "until released.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The barge's consignment note.")}})
        return out
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 7, 30, "Issued once the granulate is on board.",
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
     "received": 23, "received_why": "One bench arrived in a damaged carton and was refused.",
     "orderline_extra": {
         "CatalogueLineReference": {"LineID": V("1", "The catalogue line ordered from.")},
         "BuyerProposedSubstituteLineItem": {
             "ID": V("1", "The store's fall-back if the Serra 180 is out of stock."),
             "Quantity": qty(24, "H87", "The same quantity."),
             "Item": {"Name": V("Park bench Serra 180, moss green", "The other frame colour: the store would take "
                                                                     "it."),
                      "SellersItemIdentification": {"ID": V("LD-10442", "The distributor's number."),
                                                    "ExtendedID": V("GRN", "The green variant.")}}}}}])


PROMO = Decimal("0.05")          # the distributor's promotion support on the store's order


def promo_allowance(base, why):
    return {"ChargeIndicator": V("false", "An allowance the distributor granted."),
            "AllowanceChargeReasonCode": V("72", "UN/EDIFACT 5189 code 72: temporary special promotion.",
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
    out["AllowanceCharge"] = ac
    t = out[total_key]
    t["AllowanceTotalAmount"] = amount(a, "XBL", "The promotion support.")
    if "TaxExclusiveAmount" in t:
        t["TaxExclusiveAmount"] = amount(base - a, "XBL", "The goods less the allowance; no tax on a sale for "
                                                          "resale.")
        t["TaxInclusiveAmount"] = amount(base - a, "XBL", "The same: no tax.")
    t["PayableAmount"] = amount(base - a, "XBL", "What the store pays: the goods less the promotion support.")
    return base - a


def retail(n, doc):
    f = RETAIL
    w = kit.gross_weight(f, "ordered")
    store = {"Name": V("Garden department", "The department of the store that sells the benches.")}
    if doc["doc"] == "Catalogue":
        return kit.catalogue(f, n, doc, 0, "The spring catalogue for the store.", ["bench-serra-b", "bench-casting-b"], 90)
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The store's forecast number."),
                "IssueDate": V(f.date(2), "Sent after the catalogue arrived."),
                "ForecastPurposeCode": V("Sales", "A forecast of the store's sales, so the distributor can plan its "
                                                  "stock."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The forecast covers the next six weeks."),
                                   "EndDate": V(f.date(56), "The end of the forecast period.")},
                "ForecastLine": {"ID": V("1", "The first and only line."),
                                 "ForecastTypeCode": V("Total", "The total expected sales of the item in the period."),
                                 "SalesItem": {"Quantity": qty(40, "H87", "Forty benches over six weeks, promotion "
                                                                          "included."),
                                               "Item": item("bench-serra-b")}}}
    if doc["doc"] == "RetailEvent":
        return {"ID": V(f.number("event", doc["from"], "RetailEvent"), "The store's event number."),
                "IssueDate": V(f.date(2), "Announced with the forecast."),
                "RetailEventName": V("Spring garden promotion", "The name of the promotion."),
                "RetailEventStatusCode": V("Confirmed", "The promotion is decided, not only planned."),
                "Description": V("Ten per cent off garden furniture for two weeks.", "What the promotion is."),
                "Period": {"StartDate": V(f.date(21), "The promotion starts in three weeks."),
                           "EndDate": V(f.date(34), "It lasts two weeks.")}}
    if doc["doc"] == "InventoryReport":
        return {"ID": V(f.number("inventory", doc["from"], "InventoryReport"), "The store's inventory report number."),
                "IssueDate": V(f.date(3), "The weekly stock report."),
                "InventoryReportLine": {"ID": V("1", "The first and only line."),
                                        "Quantity": qty(3, "H87", "Three benches left in the garden department."),
                                        "Item": item("bench-serra-b")}}
    if doc["doc"] == "Order":
        out = kit.order(f, n, doc, 4, "The store replenishes before the promotion.",
                         "Delivered duty paid at the store: the distributor arranges and pays the transport and every "
                         "cost, so the order names only where to deliver.", "Brightmarket Stores, goods-in, Lumeport",
                         {"Delivery": {"DeliveryLocation": {"Description": V("Goods-in, garden department",
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
                                                    "ActionCode": V("Accepted", "The store accepts them.")},
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
        units = kit.handling_units(f, f.deal, "LD-RT-", "BRIGHTMARKET LUMEPORT")
        for k, u in enumerate(units, 1):
            u["HandlingUnitDespatchLine"] = {
                "ID": V(f"{k}", "The pallet's line: the benches on it."),
                "DeliveredQuantity": qty(4, "H87", "Four benches on the pallet."),
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
        return kit.invoice(f, n, doc, 10, 30, "Issued after delivery.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The consignment note.")}},
                           [{"item": "road-transport-b", "qty": 38, "invoice_why": "The kilometres from Marrowdale to the "
                                                                                 "store in Lumeport."}],
                           key="freight-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment carried.")}}}})
    if doc["doc"] == "ReceiptAdvice":
        out = kit.receipt_advice(f, n, doc, 10, "The day the goods were unloaded at the store.")
        out["Shipment"] = {"ID": V(f.numbers["shipment"], "The shipment received."),
                           "TransportHandlingUnit": {
                               "ID": V("LD-RT-003", "The pallet with the damaged carton."),
                               "DamageRemarks": V("One carton torn, the bench's armrest bent.", "What the goods-in "
                                                                                                "found."),
                               "DamageDocumentationAttachment": {"ExternalReference": {
                                   "URI": V("https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg",
                                            "The photograph taken at goods-in."),
                                   "MimeCode": V("image/jpeg", "A photograph."),
                                   "FileName": V("pallet-3.jpg", "The file name.")}},
                               "Status": {"ConditionCode": V("Damaged", "The pallet's condition on arrival."),
                                          "Description": V("Three benches accepted, one refused.", "What was done.")},
                               "ReceivedHandlingUnitReceiptLine": {
                                   "ID": V("1", "The receipt of the pallet."),
                                   "ReceivedQuantity": qty(3, "H87", "Three benches accepted from this pallet."),
                                   "RejectedQuantity": qty(1, "H87", "One refused."),
                                   "RejectReason": V("Damaged in transit.", "Why.")}}}
        return out
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 10, 30, "Issued on delivery.",
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
                                 "line_allowance": {"percent": "5", "code": "72",
                                                    "code_why": "UN/EDIFACT 5189 code 72: temporary special "
                                                                "promotion.",
                                                    "reason": "Promotion support",
                                                    "why": "The invoice gave 5 % on all benches, so the credit "
                                                           "is 5 % less too."},
                                 "line_tax": True,
                                 "line_extra": {
                                     "AccountingCostCode": V("6120", "The store's garden department."),
                                     "AccountingCost": V("Garden department", "In words."),
                                     "PaymentPurposeCode": V("GDDS", "ISO 20022 purpose code GDDS: goods."),
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
                                                        "ResponseCode": V("CN", "The distributor's answer: a "
                                                                                "credit for the refused bench."),
                                                        "Description": V("One bench refused at goods-in, damaged in "
                                                                         "transit.", "In words.")},
                                "OrderReference": {"ID": V(f.numbers["order"], "The store's order.")},
                                "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice of "
                                                                                             "the goods.")}})
        line = out["CreditNoteLine"][0]
        line.update({"Note": V("Bench refused: armrest bent, carton torn.", "Why the line is credited."),
                     "DiscrepancyResponse": {"ReferenceID": V("1", "The invoice line."),
                                             "ResponseCode": V("Damaged", "Credited because damaged.")},
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
                                    promotion={"name": "Spring garden promotion", "percent": 10, "from": 22, "to": 28})
        till(out, f, 25, "11:42:00", "G2", "Mira")
        card_payment(out, f, 25, "11:42:00")
        out["Note"] = V("Home delivery booked for Saturday.", "Printed on the receipt.")
        out["Delivery"] = {"DeliveryAddress": address("c-xb"),
                           "RequestedDeliveryPeriod": {"StartDate": V(f.date(27), "Saturday."),
                                                       "StartTime": V("09:00:00", "Morning."),
                                                       "EndTime": V("12:00:00", "Until noon.")},
                           "CarrierParty": party("26-xb", short=True)}
        return out
    raise SystemExit(f"retail scenario: no document {n} {doc['doc']}")


SCENARIOS.update({"rail": rail, "plastics": plastics, "retail": retail})


# ---------------------------------------------------------------- the sea flow (Bayvarra -> Lisavu, CIF)
SEA = kit.Flow("sea", "2026-05-04", [
    {"item": "bench-serra-b", "ordered": 96, "why": "One 40-foot container: 24 pallets of 4 benches."},
    {"item": "bench-casting-b", "ordered": 12, "why": "Spare side frames for the buyer's own service stock.",
     "received": 11, "received_why": "One box crushed at the port; the frame inside is cracked."}])
CONTAINER = kit.container_number("TWL", 412087)       # Tidewell Ocean Lines' container (ISO 6346, with check digit)
SEA_FREIGHT, INSURANCE = Decimal("2950.00"), Decimal("140.00")


def cif_value(f):
    goods = sum(Decimal(str(d["ordered"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])) for d in f.deal)
    return goods + SEA_FREIGHT + INSURANCE


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
                                      "SealIssuerTypeCode": V("Carrier", "Issued by the ocean carrier."),
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
            "PackagedTransportHandlingUnit": kit.handling_units(f, f.deal, "LD-26-", "VELUMI SELANU"),
            "GoodsItem": {"ID": V("1", "The goods in the container, as one item for the carrier."),
                          "Description": V("Park benches and spare side frames", "In words."),
                          "GoodsItemContainer": {"ID": V(CONTAINER, "The container the goods are in."),
                                                 "Quantity": qty(25, "C62", "25 pallets in it.")},
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
            "Package": {"ID": V("LD-26-025", "The pallet of boxed castings, packed last at the doors."),
                        "Quantity": qty(12, "H87", "Twelve boxes."),
                        "PackagingTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box."),
                        "ContainingTransportEquipment": {"ID": V(CONTAINER, "The container.", schemeID="ISO6346")}}})
    return out


def sea_consignment(f, view):
    goods = sum(Decimal(str(d["ordered"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])) for d in f.deal)
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
                "TransportServiceCode": V("MerchantHaulage", "The forwarder, not the shipping line, brings the "
                                                              "container to the port."),
                "Name": V("Truck from Marrowdale to the port of Lumeport", "In words.")},
            "FinalDeliveryTransportationService": {
                "TransportServiceCode": V("MerchantHaulage", "The buyer's 3PL collects at the port of Selanu."),
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
        "TariffCode": V("9401.79", "The tariff of the carrier for this cargo: furniture."),
        "TariffDescription": V("Furniture, packed, not hazardous", "The carrier's commodity tariff, in words."),
        "ShippingPriorityLevelCode": V("Standard", "The normal sailing, no priority loading."),
        "HandlingCode": V("Deck", "The carrier may stow the container on deck."),
        "HandlingInstructions": V("Keep dry.", "The handling, in words."),
        "Information": V("Shipped on board in apparent good order and condition.", "The carrier's clause."),
        "OriginalDespatchParty": party("6-xb", short=True),
        "FinalDeliveryParty": party("1-xl", short=True),
        "LogisticsOperatorParty": party("9-xl", short=True),
        "BillOfLadingHolderParty": party("1-xl", short=True),
        "OriginalDepartureCountry": {"IdentificationCode": V("XB", "From Bayvarra.")},
        "FinalDestinationCountry": {"IdentificationCode": V("XL", "To the island.")},
        "FirstArrivalPortLocation": kit.place("XLSEL", "The first port of call after Lumeport."),
        "LastExitPortLocation": kit.place("XBLMP", "The last port in Bayvarra."),
        "DeliveryTerms": {"ID": V("CIF", "Incoterms 2020: cost, insurance and freight to the port of Selanu."),
                          "LossRiskResponsibilityCode": V("Buyer", "The risk is the buyer's from on board in Lumeport."),
                          "LossRisk": V("Risk passes when the goods are on board the vessel in Lumeport.", "In words."),
                          "Amount": amount(cif_value(f), "XBL", "The CIF value the terms are based on."),
                          "DeliveryLocation": kit.place("XLSEL", "The named port of destination."),
                          "AllowanceCharge": {"ChargeIndicator": V("true", "A cost under the terms."),
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
                                   "AllowanceChargeReason": V("Ocean freight, 40-foot container", "In words."),
                                   "Amount": amount(Decimal("2700.00"), "XBL", "The carrier's rate.")},
        "ExtraAllowanceCharge": {"ChargeIndicator": V("true", "A surcharge."),
                                 "AllowanceChargeReason": V("Bunker surcharge", "For the fuel price."),
                                 "Amount": amount(Decimal("250.00"), "XBL", "Together with the freight: the 2,950 "
                                                                            "lume the forwarder invoices.")},
        "PreCarriageShipmentStage": {
            "ID": V("1", "By truck from Marrowdale to the port."),
            "ShipmentStageTypeCode": V("PreCarriage", "The kind of stage."),
            "ShipmentStageType": V("Carriage before the main carriage", "In words."),
            "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The truck to the port."),
                                       "AllowanceChargeReason": V("Pre-carriage by road", "In words."),
                                       "Amount": amount(Decimal("310.00"), "XBL", "The forwarder's own truck; part "
                                                                                  "of its price to the shipper.")},
            "TransportModeCode": V("3", "Road transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                 "Transport"),
            "PreCarriageIndicator": V("true", "Before the main carriage."),
            "CabotageIndicator": V("false", "A Bayvarran truck within Bayvarra: no cabotage."),
            "CarrierParty": party("10-xb", short=True),
            "TransportMeans": kit.means("10-xb", "B-05"),
            "DropoffTransportEvent": kit.event(f, 9, "10:15:00", "The container was dropped at the container quay.")},
        "MainCarriageShipmentStage": {
            "ID": V("2", "By sea from Lumeport to Selanu."),
            "TransportModeCode": V("1", "Maritime transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                      "Transport"),
            "TransportMeans": {**kit.means("11-xb", "TH", "TH-26-19E", "The voyage number.", "Eastbound"),
                               "TradeServiceCode": V("TWL-ISL", "The carrier's code for its island service."),
                               "Stowage": {"LocationID": V("140282", "Bay 14, row 02, tier 82."),
                                           "Location": V("On deck, aft of the bridge", "In words."),
                                           "MeasurementDimension": {"AttributeID": V("Slot", "The slot length."),
                                                                    "Measure": V("12.2", "A 40-foot slot.",
                                                                                 unitCode="MTR")}}},
            "LoadingPortLocation": kit.place("XBLMP", "The port of loading."),
            "UnloadingPortLocation": kit.place("XLSEL", "The port of discharge."),
            "TransshipPortLocation": {"Name": V("None: a direct sailing", "No transhipment on the way.")},
            "AcceptanceTransportEvent": kit.event(f, 9, "10:15:00", "The terminal accepted the container."),
            "AvailabilityTransportEvent": kit.event(f, 14, "14:00:00", "The container is available at Selanu.",
                                                    done=False),
            "StorageTransportEvent": kit.event(f, 9, "10:30:00", "Stacked at the quay until loading."),
            "FreightChargeLocation": kit.place("XBLMP", "The freight is payable in Lumeport.")},
        "OnCarriageShipmentStage": {
            "ID": V("3", "By truck from the port of Selanu to the 3PL."),
            "TransportModeCode": V("3", "Road transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                 "Transport"),
            "OnCarriageIndicator": V("true", "After the main carriage."),
            "CarrierParty": party("9-xl", short=True),
            "ReceiptTransportEvent": kit.event(f, 15, None, "Planned receipt at the 3PL.", done=False),
            "WarehousingTransportEvent": kit.event(f, 15, None, "Stored at the 3PL until called off.", done=False)},
        "InsurancePolicy": {"ID": V("WS-CP-26-4471", "The cargo policy of the insurer."),
                            "InsuranceTypeCode": V("AllRisks", "Cover against all risks."),
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
         "ReferenceEventCode": V("OrderAccepted", "Due when the order is accepted."),
         "InstallmentDueDate": V(f.date(5), "It was due on acceptance; paid.")},
        {**terms, "ID": V("BALANCE", "The balance, the second instalment."),
         "PaymentPercent": V(str(round(balance * 100 / total, 2)), "Its share of the invoice total."),
         "Amount": amount(balance, "XBL", "The balance."),
         "ReferenceEventCode": V("Shipment", "Counted from the shipment on board."),
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
        "CardAccount": {"PrimaryAccountNumberID": V("************4417", "The card number, masked: a receipt shows only "
                                                                        "the last four digits."),
                        "NetworkID": V("LUMECARD", "The card scheme of the world: Lumeport's interbank card."),
                        "CardTypeCode": V("Debit", "A debit card."),
                        "ValidityStartDate": V("2025-06-01", "The card is valid from."),
                        "ExpiryDate": V("2029-05-31", "And until."),
                        "IssuerID": V("BLUM", "Issued by the Bank of Lumeport."),
                        "CardChipCode": V("Chip", "Read from the chip."),
                        "ChipApplicationID": V("A0000099990001", "The chip application used; an identifier of the world, "
                                                                 "not a registered one."),
                        "HolderName": V("R ASHDALE", "The name on the card."),
                        "RoleCode": V("Holder", "Paid by the card holder.")}}
    out["Payment"] = {"ID": V("BM-G2-26-0518-0047", "The till's number for the payment."),
                      "PaidAmount": total, "PaidDate": V(f.date(day), "Paid at the till."),
                      "PaidTime": V(time, "At the time of the sale."),
                      "MerchantID": V("LUMECARD-M-0026118", "The store's merchant number with the card scheme."),
                      "AuthorizationID": V("A71520", "The approval code of the card issuer."),
                      "TransactionID": V("TX-26-0518-773104", "The card transaction."),
                      "PaymentTerminalID": V("PT-G2", "The card terminal at the till."),
                      "StatusCode": V("Approved", "The payment was approved.")}
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
        "TotalPackagesQuantity": qty(108, "H87", "96 benches and 12 boxed frames."),
        "GrossWeightMeasure": qty(w, "KGM", "The expected gross weight, for the booking."),
        "NetWeightMeasure": qty(net, "KGM", "The goods alone."),
        "GrossVolumeMeasure": V("41.5", "One 40-foot container's load.", unitCode="MTQ"),
        "Contract": {"ID": V(f.numbers["agreement"], "The digital agreement the trade runs under."),
                     "ContractType": V("Digital trade agreement", "What it is.")},
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
            "LineStatusCode": V("NoStatus", "Unchanged against the order."),
            "Quantity": qty(q, ITEM[d["item"]]["unit"], "The quantity confirmed."),
            "LineExtensionAmount": amount(amt, "XBL", "As ordered."),
            "TaxInclusiveLineExtensionAmount": amount(amt, "XBL", "No tax on an export: the same amount."),
            "TotalTaxAmount": amount(0, "XBL", "No tax on an export."),
            "PartialDeliveryIndicator": V("false", "All in one container."),
            "BackOrderAllowedIndicator": V("false", "Nothing is back-ordered: all is in stock."),
            "Delivery": {"PromisedDeliveryPeriod": {"StartDate": V(f.date(10), "Shipped on the sailing of day 10."),
                                                    "EndDate": V(f.date(14), "Arriving at Selanu.")}},
            "WarrantyInformation": V(bench["warranty"], "The maker's warranty passes to the buyer."),
            "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
            "WarrantyParty": party(bench["seller"], short=True),
            "Price": kit.price_block(d["item"], "XBL"),
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
                         {"CustomerReference": V("Harbour parks Selanu", "The buyer's project the benches are "
                                                                         "for."),
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
                             "NetVolumeMeasure": V("38.9", "The volume of the goods themselves.", unitCode="MTQ"),
                             "TotalTransportHandlingUnitQuantity": qty(25, "C62", "25 pallets in the container."),
                             "ShippingPriorityLevelCode": V("Standard", "No priority: the next sailing will do."),
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
        goods = sum(Decimal(str(d["ordered"])) * Decimal(str(ITEM[d["item"]]["price"]["amount"])) for d in f.deal)
        kit.deep_merge(out["CustomsDeclaration"]["Shipment"], {
            "DeclaredCustomsValueAmount": amount(goods, "XBL", "The export value: the goods on board, FOB."),
            "DeclaredStatisticsValueAmount": amount(goods, "XBL", "The same value for the trade statistics."),
            "FreeOnBoardValueAmount": amount(goods, "XBL", "On board in Lumeport."),
            "InsuranceValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL", "The cargo insurance the seller "
                                                                                 "took out under CIF."),
            "FreightAllowanceCharge": {"ChargeIndicator": V("true", "The sea freight, paid by the seller."),
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
                                             "ActualDepartureTransportEvent": kit.event(f, 10, "18:10:00", "The ship "
                                                                                        "sailed."),
                                             "SecurityOfficerPerson": kit.person("Tamsin", "Orrel", "The port "
                                                                                 "facility security officer who "
                                                                                 "cleared the loading.",
                                                                                 job="Port facility security officer")}}})
    if doc["doc"] == "BillOfLading":
        return {"ID": V(f.number("bl", doc["from"], "BillOfLading"), "The bill of lading number."),
                "IssueDate": V(f.date(10), "Issued when the goods are shipped on board."),
                "CarrierAssignedID": V(SEA_BOOKING, "The booking the bill of lading is issued under."),
                "ToOrderIndicator": V("true", "Made out to order: the buyer can transfer it by endorsement."),
                "AdValoremIndicator": V("false", "No value declared to the carrier: its liability stays limited."),
                "ShippingOrderID": V(f.numbers["instructions-carrier"], "The forwarder's booking with the carrier."),
                "OtherInstruction": V("Three originals issued.", "How many originals there are."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment carried."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the cargo."),
                             "TotalGoodsItemQuantity": qty(2, "H87", "Benches and side frames."),
                             "ConsignmentQuantity": qty(1, "H87", "One consignment."),
                             "Consignment": sea_consignment(f, "bl"),
                             "InsurancePolicy": {"InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                                              "The insured value, 110 % of the CIF "
                                                                              "value.")},
                             }}
    if doc["doc"] == "Manifest":
        return {"ID": V(f.number("manifest", doc["from"], "Manifest"), "The carrier's cargo manifest number."),
                "IssueDate": V(f.date(11), "Sent to the island's customs before arrival."),
                "ManifestTypeCode": V("Cargo", "A cargo manifest, of what the ship carries for Selanu."),
                "AdValoremIndicator": V("false", "No value declared for the carriage."),
                "CrewPerson": [kit.person("Corin", "Halvard", "The master of the ship.", role="Master"),
                               kit.person("Elsbeth", "Marrin", "The chief officer.", role="ChiefOfficer")],
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
                                                             "Eastbound"),
                                 "CrewQuantity": qty(14, "C62", "The crew on board."),
                                 "MasterPerson": kit.person("Corin", "Halvard", "The master, who signs the manifest.",
                                                            role="Master"),
                                 "EstimatedArrivalTransportEvent": kit.event(f, 13, "22:00:00", "Expected off Selanu "
                                                                                                "in the evening."),
                                 "EstimatedDepartureTransportEvent": kit.event(f, 11, "06:00:00", "The planned "
                                                                                                  "departure from "
                                                                                                  "Lumeport.")},
                             "TransportHandlingUnit": {"TransportEquipment": sea_equipment(f, False)}}}
    if doc["doc"] == "CommonTransportationReport":
        return {"ID": V(f.number("ctr", doc["from"], "CommonTransportationReport"), "The carrier's report number."),
                "IssueDate": V(f.date(12), "Sent before the ship enters the port of Selanu."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment the report is for."),
                             "ShipmentStage": {"ID": V("1", "The sea leg to Selanu."),
                                               "ISPSRequirements": {
                                                   "ID": V("ISSC-XL-2026-0117", "The number of the ship's International "
                                                                                 "Ship Security Certificate."),
                                                   "ValidISSCIndicator": V("true", "The ship holds a valid security "
                                                                                   "certificate."),
                                                   "ISSCExpiryDate": V("2028-09-30", "The certificate is valid for five "
                                                                                     "years from its issue."),
                                                   "CurrentOperatingSecurityLevelCode": V("1", "Security level 1, the "
                                                                                              "normal level.")}}}}
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 14, "Reported when the container is discharged.",
                                         f"Container {CONTAINER} discharged and available for customs clearance.",
                                         "Port of Selanu", {"Consignment": {"MainCarriageShipmentStage": {
                                             "ID": V("2", "The sea leg, stage 2 as on the bill of lading."),
                                             "ActualArrivalTransportEvent": kit.event(f, 14, "06:30:00", "The ship "
                                                                                      "berthed at Selanu."),
                                             "DischargeTransportEvent": kit.event(f, 14, "11:20:00", "The container "
                                                                                  "came off the ship.", done=True),
                                             "DetentionTransportEvent": kit.event(
                                                 f, 14, "12:00:00", "Held by customs for a check of the pallets.",
                                                 description="Wooden pallets must carry the heat-treatment mark."),
                                             "ReportingPerson": kit.person("Ama", "Kelune", "The terminal's duty "
                                                                           "officer who reports.", job="Duty "
                                                                           "officer")},
                                             "TransportHandlingUnit": {"TransportEquipment": {
                                                 "ID": V(CONTAINER, "The container.", schemeID="ISO6346"),
                                                 "QuarantineTransportEvent": kit.event(
                                                     f, 14, "15:00:00", "Released from the quarantine check: all "
                                                     "pallets heat-treated.", done=True),
                                                 "ServiceAllowanceCharge": {
                                                     "ChargeIndicator": V("true", "A service charge."),
                                                     "AllowanceChargeReason": V("Terminal handling at Selanu",
                                                                                "For unloading the box."),
                                                     "Amount": amount(Decimal("185.00"), "XBL", "As in the carrier's "
                                                                                                "tariff.")},
                                                 "TransportEvent": kit.event(f, 14, "11:40:00", "Stacked in the "
                                                                                                "import yard.")}}}})
    if doc["doc"] == "Invoice" and doc["from"] == "10-xb":
        return kit.invoice(f, n, doc, 15, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container."},
                            {"item": "export-clearance", "qty": 1, "invoice_why": "One export declaration."},
                            {"item": "cargo-insurance", "qty": 1, "invoice_why": "Insurance of this shipment."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "ImportCustomsDeclaration":
        out = kit.import_declaration(f, n, doc, 15, "The customs broker declares the import for the buyer.",
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
                                           "AllowanceChargeReason": V("Ocean freight, share of the benches",
                                                                      "Part of the CIF value."),
                                           "Amount": amount(SEA_FREIGHT * 49920 / 50688 * Decimal("0.4"), "XLC",
                                                            "The benches' share of the 2,950 lume freight by value "
                                                            "(49,920 of 50,688 lume), in coral at 0.4.")}
        first["InsurancePolicy"] = {"ID": V("WS-CP-26-4471", "The cargo policy covering the goods."),
                                    "InsuredValueAmount": amount(cif_value(f) * Decimal("1.1"), "XBL",
                                                                 "As on the insurance certificate.")}
        first["InvoiceLine"] = {"ID": V("1", "The line of the seller's invoice for these goods."),
                                "InvoicedQuantity": qty(96, "H87", "The benches invoiced."),
                                "Item": {"Name": V(ITEM["bench-serra-b"]["name"], "Named only: described in full "
                                                                                  "above.")}}
        return out
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 9, "Sent to the delivery party named in the order when the container "
                                                 "leaves.", "The gross weight of the goods.")
    if doc["doc"] == "ReceiptAdvice":
        return kit.receipt_advice(f, n, doc, 17, "The buyer's 3PL confirms what arrived.")
    if doc["doc"] == "Invoice":
        out = kit.invoice(f, n, doc, 10, 45, "Issued when the goods are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")}},
                           charges=[{"like": "bench-serra-b", "reason": "Sea freight", "amount": SEA_FREIGHT,
                                     "why": "Under CIF the seller pays the sea freight and charges it on the invoice.",
                                     "amount_why": "The freight the forwarder charged for the container."},
                                    {"like": "bench-serra-b", "reason": "Cargo insurance", "amount": INSURANCE,
                                     "why": "Under CIF the seller insures the cargo and charges the insurance.",
                                     "amount_why": "The premium of the cargo insurance."}])
        return sea_invoice_terms(f, out)
    if doc["doc"] == "Statement":
        cur, total = "XBL", f.numbers["invoice-amount"]
        out = {"ID": V(f.number("statement", doc["from"], "Statement"), "The factor's statement number."),
                "IssueDate": V(f.date(40), "The monthly statement of account."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the invoices"),
                "StatementTypeCode": V("Account", "A statement of the account."),
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
                                "line_extra": {"Note": V("Box crushed at the port of Selanu.", "What happened.")}}],
                              {"BillingReference": {"InvoiceDocumentReference": {
                                  "ID": V(f.numbers["invoice"], "The invoice of the frames."),
                                  "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                               "Note": V("Under CIF the risk was the buyer's on board; the distributor credits the "
                                         "frame as a goodwill gesture and claims from the insurer.", "Why a credit "
                                                                                                    "under CIF."),
                               "DiscrepancyResponse": {"ResponseCode": V("Damaged", "The goods arrived damaged."),
                                                       "Description": V("One side frame cracked.", "In words.")},
                               "OrderReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
                               "ReceiptDocumentReference": {"ID": V(f.numbers["receipt"], "The 3PL's receipt "
                                                                                          "advice reporting it.")},
                               "StatementDocumentReference": {"ID": V(f.numbers["statement"], "The factor's statement "
                                                                      "the invoice is on.")},
                               "ContractDocumentReference": {"ID": V(f.numbers["agreement"], "The digital "
                                                                                             "agreement.")},
                               "OriginatorDocumentReference": {"ID": V("VT-CLAIM-26-0019", "The buyer's claim.")},
                               "ProjectReference": {"ID": V("Harbour parks Selanu", "The buyer's project.")},
                               "BuyerAssignedReference": {"BuyerReferenceCode": V("VT-CLAIMS", "The buyer's claims "
                                                                                               "desk.")},
                               "Delivery": {"ActualDeliveryDate": V(f.date(17), "The goods arrived at the 3PL.")},
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
    {"item": "bench-casting-b", "ordered": 8, "why": "Eight side frames, needed before the ship arrives."}])


def air_consignment(f, doc):
    """The distributor's instructions for the urgent frames: one skid of eight boxes."""
    cid = f.number("consignment", doc["from"], "Consignment")
    goods = Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]["amount"]))
    box = {"ID": V("LD-AIR-BOX", "The boxes, numbered 1 to 8 on their labels."),
           "Quantity": qty(8, "H87", "Eight boxes."),
           "PackagingTypeCode": V("BX", "UN/ECE Recommendation 21 code BX: box."),
           "TraceID": V("LD-AIR-0001..0008", "The barcodes on the boxes."),
           "MeasurementDimension": [{"AttributeID": V("Length", "Of one box."),
                                     "Measure": V("800", "In millimetres.", unitCode="MMT")},
                                    {"AttributeID": V("Width", "Of one box."),
                                     "Measure": V("300", "In millimetres.", unitCode="MMT")},
                                    {"AttributeID": V("Height", "Of one box."),
                                     "Measure": V("300", "In millimetres.", unitCode="MMT")}],
           "ContainedPackage": {"ID": V("LD-AIR-BAG", "Inside each box, the frame in a plastic bag."),
                                "Quantity": qty(8, "H87", "One bag per box."),
                                "PackagingTypeCode": V("BG", "UN/ECE Recommendation 21 code BG: bag.")},
           "GoodsItem": {"ID": V("1", "The side frames."),
                         "Description": V("Bench side frame castings", "In words.")},
           "DeliveryUnit": {"BatchQuantity": qty(8, "H87", "All eight delivered together.")},
           "Pickup": {"ID": V("BF-PU-26-0611", "The forwarder's pick-up order."),
                      "EarliestPickupDate": V(f.date(1), "Ready the day of the instructions."),
                      "PickupParty": party("10-xb", short=True)},
           "Despatch": {"RequestedDespatchDate": V(f.date(2), "To make the next morning's flight.")},
           "Delivery": {"RequestedDeliveryPeriod": {"StartDate": V(f.date(3), "Wanted at the 3PL on day 3."),
                                                    "EndDate": V(f.date(3), "The same day.")}},
           "Status": {"ConditionCode": V("Ready", "Packed and labelled."),
                      "Description": V("Waiting at the distributor's dispatch area.", "Where they are.")}}
    return {"ID": V(cid, "The distributor's consignment number."),
            "TotalGoodsItemQuantity": qty(1, "C62", "One kind of goods."),
            "NetNetWeightMeasure": qty(Decimal(8) * Decimal(str(kit.maker("bench-casting-b")["net_kg"])), "KGM",
                                       "The castings alone."),
            "NetVolumeMeasure": V("0.42", "The frames' own volume.", unitCode="MTQ"),
            "DeclaredForCarriageValueAmount": amount(goods, "XBL", "Declared to the airline so its liability covers "
                                                                   "the value of the frames."),
            "DeclaredStatisticsValueAmount": amount(goods, "XBL", "The value for the export statistics."),
            "SplitConsignmentIndicator": V("false", "All eight boxes on one flight."),
            "ConsignmentQuantity": qty(1, "C62", "One consignment."),
            "FreightForwarderParty": party("10-xb", short=True),
            "TransportEvent": kit.event(f, 2, "19:00:00", "Latest acceptance at the cargo terminal for the morning "
                                                          "flight.", done=False),
            "TransportHandlingUnit": {
                "ID": V("LD-AIR-SKID-1", "The skid the boxes are strapped to."),
                "TransportHandlingUnitTypeCode": V("SI", "UN/ECE Recommendation 21 code SI: skid."),
                "ReferencedShipment": {"ID": V(f.numbers["shipment"], "The distributor's shipment on the skid.")},
                "Package": box}}


def air(n, doc):
    f = AIR
    w = kit.gross_weight(f, "ordered")
    if doc["doc"] == "OrderChange":
        order = kit.order(f, n, doc, 0, "The buyer needs eight side frames urgently.",
                          "Carriage paid to the island's airport for the urgent frames: the distributor pays the air "
                          "freight; the rest of the order stays CIF by sea.", "Selanu airport, cargo terminal")
        order.pop("OrderTypeCode")
        sea_base = sum(r[2] for r in kit.lines(SEA, "6-xb", "1-xl", "XBL"))
        air_base = Decimal(order["AnticipatedMonetaryTotal"]["LineExtensionAmount"].value)
        order["AnticipatedMonetaryTotal"] = {
            "LineExtensionAmount": amount(sea_base + air_base, "XBL", "The order as changed: the lines of the sea "
                                                                      "order and the eight frames added."),
            "PayableAmount": amount(sea_base + air_base, "XBL", "No tax on an export; freight comes on the "
                                                                "invoices.")}
        order["TaxTotal"]["TaxSubtotal"][0]["TaxableAmount"] = amount(sea_base + air_base, "XBL", "The order as "
                                                                      "changed; no tax on an export.")
        order.update({
            "SalesOrderID": V(SEA.numbers.get("sales-order", f"LD-SO-26-{SEA.base:04d}"), "The distributor's "
                                                                                           "sales order the "
                                                                                           "change applies to."),
            "IssueTime": V("07:50:00", "First thing in the morning, when the shortage was noticed."),
            "Note": V("Add eight side frames by air; the rest of the order is unchanged.", "The change in words."),
            "CustomerReference": V("Harbour parks Selanu", "The buyer's project."),
            "Contract": {"ID": V(SEA.numbers["agreement"], "The digital agreement the order runs under.")},
            "AccountingCustomerParty": {"Party": party("1-xl", short=True)},
            "AccountingSupplierParty": {"Party": party("6-xb", short=True)},
            "DestinationCountry": {"IdentificationCode": V("XL", "The island.")}})
        order["Delivery"] = {"DeliveryTerms": {"ID": V("CPT", "Incoterms 2020: carriage paid to, for this delivery "
                                                              "only.", schemeID="INCOTERMS"),
                                               "SpecialTerms": V("The rest of the order stays CIF by sea.", "Why the "
                                                                 "delivery has its own terms.")},
                             "NotifyParty": party("9-xl", short=True),
                             "CarrierParty": party("12-xl", short=True)}
        return {**order, "ID": V(f.number("order-change", doc["from"], "OrderChange"), "The number of this change."),
                "SequenceNumberID": V("1", "The first change to the order."),
                "OrderReference": {"ID": V(SEA.numbers["order"], "The order of the sea flow that this change "
                                                                 "extends.")}}
    if doc["doc"] == "OrderResponse":
        out = kit.order_response(f, n, doc, 1, "The distributor accepts the change.")
        out["OrderReference"] = {"ID": V(SEA.numbers["order"], "The order that was changed.")}
        out.update({
            "OrderChangeDocumentReference": {"ID": V(f.numbers["order-change"], "The order change this response "
                                                                                "answers.")},
            "Note": V("Accepted: the frames fly on the morning flight; the forwarder is booked.", "In words."),
            "ValidityPeriod": {"EndDate": V(f.date(2), "The flight booking holds for a day.")},
            "NetNetWeightMeasure": qty(Decimal(8) * Decimal(str(kit.maker("bench-casting-b")["net_kg"])), "KGM",
                                       "The frames alone."),
            "NetVolumeMeasure": V("0.42", "Their own volume.", unitCode="MTQ"),
            **kit.cost_centre("1-xl", "The buyer's cost centre, from the change."),
            "AdditionalDocumentReference": {"ID": V("BF-QUOTE-AIR-26-0611", "The forwarder's quotation for the "
                                                                            "flight.")},
            "FreightForwarderParty": party("10-xb", short=True),
            "Signature": {"ID": V("LD-SIG-26-0512", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "OrderLine": {"LineItem": {
                "ID": V("1", "The added line."),
                "Quantity": qty(8, "H87", "Confirmed."),
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
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the eight boxed frames."),
                             "Consignment": air_consignment(f, doc)}}
    if doc["doc"] == "Waybill":
        out = kit.waybill(f, n, doc, 2, "The air waybill, issued when the airline accepts the cargo.", w,
                          "The gross weight of the cargo.")
        out["AdValoremIndicator"] = V("true", "A value is declared to the airline, which raises its liability.")
        out["DeclaredCarriageValueAmount"] = amount(Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]
                                                                             ["amount"])), "XBL",
                                                    "The value declared for carriage.")
        out["Shipment"]["DeclaredForCarriageValueAmount"] = amount(
            Decimal(8) * Decimal(str(ITEM["bench-casting-b"]["price"]["amount"])), "XBL",
            "The value declared on the air waybill, as the distributor instructed.")
        kit.deep_merge(out["Shipment"]["Consignment"], {
            "ChargeableWeightMeasure": qty(Decimal("96"), "KGM", "The volume weight is higher than the 81.6 kg: "
                                           "0.576 m³ at 167 kg per m³, rounded up."),
            "GrossVolumeMeasure": V("0.576", "Eight boxes of 0.072 m³.", unitCode="MTQ"),
            "SpecialSecurityIndicator": V("true", "The cargo was screened by the forwarder, a known consignor; it "
                                                  "may fly without further checks."),
            "SpecialServiceInstructions": V("Priority handling at Selanu: the customer is waiting.", "The service "
                                                                                                     "asked for."),
            "ShippingPriorityLevelCode": V("Priority", "Flown on the first flight with room."),
            "SequenceID": V("1", "The first house consignment under the master air waybill."),
            "ChildConsignmentQuantity": qty(1, "C62", "One house consignment in the forwarder's consolidation."),
            "ChildConsignment": {"ID": V("BF-HAWB-26-0918", "The forwarder's house air waybill for the distributor's "
                                                           "boxes."),
                                 "ConsignorAssignedID": V(f.numbers["instructions"], "The distributor's "
                                                                                     "instructions.")},
            "ConsolidatedShipment": {"ID": V("BF-CONS-26-0207", "The forwarder's consolidation for this flight, "
                                                                "of which the boxes are part.")},
            "MainCarriageShipmentStage": {
                "ID": V("1", "The flight."),
                "TransportModeCode": V("4", "Air transport.", listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                    "Transport"),
                "TransportMeans": kit.means("12-xl", "KAC", "KAC207", "The flight number of the airline of the world; "
                                                                      "not an IATA code."),
                "LoadingPortLocation": kit.place("XBLMA", "The airport of departure."),
                "UnloadingPortLocation": kit.place("XLSLA", "The airport of destination."),
                "RequestedDepartureTransportEvent": kit.event(f, 3, "07:00:00", "The forwarder asked for the morning "
                                                                                "flight."),
                "RequestedArrivalTransportEvent": kit.event(f, 3, "10:00:00", "Arriving before the 3PL's cut-off.")}})
        return out
    if doc["doc"] == "TransportationStatus" and doc["from"] == "17-xb":
        return kit.transportation_status(f, n, doc, 2, "Reported when the cargo is built up for the flight.",
                                         "Cargo accepted and built up for the flight.", "Lumeport airport, cargo "
                                                                                        "terminal",
                                         {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}})
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 2, "Sent to the buyer's 3PL when the cargo leaves.",
                                   "The gross weight of the boxed frames.")
    if doc["doc"] == "TransportationStatus":
        return kit.transportation_status(f, n, doc, 3, "Reported when the cargo has landed.",
                                         "Cargo arrived and ready for customs clearance.", "Selanu airport, cargo "
                                                                                          "terminal",
                                         {"Consignment": {"MainCarriageShipmentStage": {"ID": V("1", "The flight.")}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 4, 30, "Issued after the flight.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["waybill"], "The air waybill.")}},
                           [{"item": "air-freight", "qty": w, "invoice_why": "The chargeable weight: the gross weight "
                                                                             "of the boxed frames."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment flown.")}}}})
    raise SystemExit(f"air scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the cotton flow (Lisavu -> Bayvarra, FOB)
COTTON = kit.Flow("cotton", "2026-02-02", [
    {"item": "cotton-bale", "ordered": 6129, "why": "27 bales of about 227 kg: one container of lint."}])
SEED_KG = 18000
ADVANCE = Decimal("1000.000")      # the ginnery's season advance to the farm


def cotton(n, doc):
    f = COTTON
    w = kit.gross_weight(f, "ordered")
    farm_rows = [{"item": "seed-cotton", "qty": SEED_KG, "why": "The weighed seed cotton of three trailer loads."}]
    if doc["doc"] == "Forecast":
        return {"ID": V(f.number("forecast", doc["from"], "Forecast"), "The mill's forecast number."),
                "IssueDate": V(f.date(0), "Sent at the start of the ginning season."),
                "IssueTime": V("09:00:00", "The time is stated, because a revision refers to the forecast by its issue "
                                           "date and time."),
                "ForecastPurposeCode": V("Order", "A forecast of what the mill will order, so the ginnery can plan."),
                "ForecastPeriod": {"StartDate": V(f.date(14), "The season's shipping period."),
                                   "EndDate": V(f.date(120), "Its end.")},
                "ForecastLine": {"ID": V("1", "The only line."),
                                 "ForecastTypeCode": V("Total", "The total expected purchase in the period."),
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
                                            "provides.", farm_rows,
                              {"DespatchDocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery "
                                                                                            "note.")}})
        out.update({
            "Note": V("Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.",
                      "The statement the self-billing agreement requires on every invoice."),
            "InvoicePeriod": {"StartDate": V(f.date(1), "The week of the deliveries."),
                              "EndDate": V(f.date(3), "The last trailer.")},
            "ContractDocumentReference": {"ID": V("SCG-SEASON-2026", "The season agreement between farm and ginnery, "
                                                                     "which allows the self-billing.")},
            "DeliveryNoteDocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery note.")},
            "ReceiptDocumentReference": {"ID": V("SCG-WB-26-0311", "The weighbridge ticket of the gin.")},
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
        out["PrepaidPayment"] = {"ID": V("SCG-ADV-26-0012", "The season advance to the farm."),
                                 "PaidAmount": amount(ADVANCE, "XLC", "Paid before the harvest, against the first "
                                                                      "deliveries."),
                                 "PaidDate": V(f.date(-20), "Three weeks before the deliveries.")}
        f.numbers["self-billed-3-amount"] = lines_amt + haul - ADVANCE
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
                                   "ID": V(f.numbers["self-billed-3"], "The self-billed invoice this corrects."),
                                   "IssueDate": V(f.numbers["self-billed-3-date"], "Its issue date.")}},
                                "Note": V("Self-billed credit note under the season agreement.", "As required on "
                                                                                                 "every self-billed "
                                                                                                 "document."),
                                "DiscrepancyResponse": {"ReferenceID": V("1", "The line of the self-billed "
                                                                              "invoice."),
                                                        "ResponseCode": V("Grade", "The classing found a lower "
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
                                "ReceiptDocumentReference": {"ID": V("SCG-WB-26-0311", "The weighbridge ticket.")},
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
        inv, cn = f.numbers["self-billed-3-amount"], f.numbers["self-billed-4-amount"]
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
                         "ID": V(f.numbers["self-billed-3"], "The self-billed invoice paid.")}}},
                    {"ID": V("2", "The self-billed credit note."),
                     "CreditLineAmount": amount(cn, "XLC", "The amount credited, deducted from the payment."),
                     "BillingReference": {"SelfBilledCreditNoteDocumentReference": {
                         "ID": V(f.numbers["self-billed-4"], "The self-billed credit note set off.")}}}]}
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
        return kit.order(f, n, doc, 22, "The mill orders the first container of the season.",
                         "Free on board at the port of Selanu: the buyer books and pays the sea freight; the risk "
                         "passes when the bales are on board.", "Port of Selanu",
                         {"FreightForwarderParty": party("10-xb", short=True),
                          "DestinationCountry": {"IdentificationCode": V("XB", "The bales go to Bayvarra.")},
                          "RequestedInvoiceCurrencyCode": V("XLC", "The mill asks to be invoiced in coral, the "
                                                                   "ginnery's currency, and pays the exchange "
                                                                   "itself.")})
    if doc["doc"] == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The mill's instruction "
                                                                                       "number."),
                "IssueDate": V(f.date(23), "Under FOB the buyer instructs the forwarder for the main carriage."),
                "Shipment": {"ID": V(f.number("shipment", "39-xl", "Shipment"), "The shipment to be booked."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight of the bales."),
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment.")}}}
    if doc["doc"] == "GoodsCertificate":
        return {"ID": V(f.number("goods-certificate", doc["from"], "GoodsCertificate"), "The chamber's certificate "
                                                                                       "number."),
                "IssueDate": V(f.date(26), "Issued before shipment, at the ginnery's application."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment certified."),
                             "GoodsItem": kit.goods_items(f, "XLC", "The value of the bales, in coral.")}}
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 27, "The island's export: declared before loading.",
                                      "The value of the bales, in coral.")
    if doc["doc"] == "WeightStatement":
        return {"ID": V(f.number("vgm", doc["from"], "WeightStatement"), "The shipper's weight statement number."),
                "IssueDate": V(f.date(27), "Declared before the container is loaded, as required for every packed "
                                           "container."),
                "Shipment": {"ID": V(f.numbers["shipment"], "The shipment weighed."),
                             "TransportHandlingUnit": {"TransportEquipment": {
                                 "ID": V(kit.container_number("TWL", 412311), "The container, with its ISO 6346 check "
                                                                              "digit.", schemeID="ISO6346"),
                                 "GrossWeightMeasure": qty(w + 3750, "KGM", "The verified gross mass: the bales and the "
                                                                            "container's own weight, weighed on the "
                                                                            "port's weighbridge."),
                                 "TareWeightMeasure": qty(3750, "KGM", "The empty container's own weight.")}}}}
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
        return kit.invoice(f, n, doc, 30, 30, "Issued after the sailing.",
                           {"AdditionalDocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading.")}},
                           [{"item": "sea-freight", "qty": 1, "invoice_why": "One 40-foot container, booked for the "
                                                                             "mill under FOB."}],
                           key="forwarder-invoice",
                           extra={"Delivery": {"Shipment": {"Consignment": {"ID": V(f.numbers["consignment"],
                                                                                   "The consignment shipped.")}}}})
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 28, 30, "Issued when the bales are on board.",
                           {"OrderReference": {"ID": V(f.numbers["order"], "The mill's order.")}})
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


def withholding(f, out):
    """Bayvarra's withholding on services of non-resident businesses to public bodies (world/countries.json): the
    department keeps 10 % of the installation and pays it to the state; the supplier's tax representative."""
    wh = WORLD["countries"]["XB"]["tax"]["withholding"]
    line = out["InvoiceLine"][1]
    base = Decimal(line["LineExtensionAmount"].value)
    tax = money(base * Decimal(wh["percent"]) / 100, "XBL")
    cat = {"ID": V("S", "The withholding applies."), "Percent": V(wh["percent"], wh["on"]),
           "TaxScheme": {"ID": V("OTH", "UN/EDIFACT 5153 code OTH: other taxes, the withholding tax."),
                         "Name": V("Withholding tax on services of non-residents", "The tax in words.")}}
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
    out["TaxRepresentativeParty"] = party("10-xb", short=True)
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
        "Description": V(f"{TENDER_QTY} park benches with steel frames and hardwood slats over three years, ordered in "
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
                          "Delivery": {"ReleaseID": V("1", "The first release under the contract: 40 of the 240 "
                                                           "benches.")},
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
        out = kit.invoice(f, n, doc, 78, 30, "Issued on delivery.",
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
                          charges=[{"like": "bench-serra", "amount": COLOUR_CHARGE, "reason": "Special colour",
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
        out["Annotation"] = {"SubjectCode": V("Contract", "The annotation is about the contract."),
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


def carnet(n, doc):
    f = CARNET
    return {"ID": V(f.number("carnet", doc["from"], "GoodsItemPassport"), "The carnet number, given by the chamber."),
            "IssueDate": V(f.date(0), "Issued before the samples leave for the fair."),
            "ValidityPeriod": period(f, 0, 365, "Valid from issue.", "A carnet is valid for one year."),
            "Shipment": {"ID": V(f.number("shipment", doc["to"], "Shipment"), "The samples travelling under the carnet."),
                         "GoodsItem": kit.goods_items(f, "XUF", "The value of the samples, for the guarantee.")},
            "GoodsItemPassportCounterfoil": [
                {"ID": V("EXP-1", "The exportation counterfoil, stamped by Urvania's customs when the samples leave.")},
                {"ID": V("IMP-1", "The importation counterfoil, stamped by Lisavu's customs when they arrive.")}]}


# ---------------------------------------------------------------- the waste flow (Urvania, domestic)
WASTE = kit.Flow("waste", "2026-03-23")
WASTE_DESCRIPTION = "Mixed polyethylene production waste, sorted, in big bags"


def waste_shipment(f, tonnes, why):
    return {"ID": V(f.number("waste-shipment", "5-xu", "Shipment"), "The movement's shipment number."),
            "GrossWeightMeasure": qty(Decimal(tonnes) * 1000, "KGM", why),
            "Consignment": {"ID": V(f.number("waste-consignment", "5-xu", "Consignment"), "The consignment carried "
                                                                                          "by the road carrier.")},
            "GoodsItem": {"ID": V("1", "The only goods item."),
                          "Description": V(WASTE_DESCRIPTION, "What the waste is."),
                          "HazardousRiskIndicator": V("false", "Sorted polyethylene is not hazardous waste.")}}


def waste(n, doc):
    f = WASTE
    if doc["doc"] == "WasteNotification":
        return {"ID": V(f.number("notification", doc["from"], "WasteNotification"), "The notification number."),
                "IssueDate": V(f.date(0), "Notified before the movements start."),
                "Shipment": waste_shipment(f, 40, "The planned movement: about 40 tonnes in two truck loads.")}
    if doc["doc"] == "WasteMovement":
        return {"ID": V(f.number("movement", doc["from"], "WasteMovement"), "The movement document number."),
                "IssueDate": V(f.date(10), "Reported when the waste has been received."),
                "Shipment": waste_shipment(f, "38.2", "Weighed on arrival at the recovery facility.")}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 12, 30, "Issued after the waste was collected and recovered.",
                           {"AdditionalDocumentReference": ref(f, "movement", "The waste movement document.")},
                           [{"item": "waste-recovery", "qty": "38.2", "invoice_why": "The tonnes received, from the "
                                                                                     "waste movement document."}])
    raise SystemExit(f"waste scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the utilities flow (one utility per country)
UTILITIES = kit.Flow("utilities", "2026-04-01")
MARCH = {"InvoicePeriod": {"StartDate": V("2026-03-01", "The month billed: March."),
                           "EndDate": V("2026-03-31", "Its last day."),
                           "DescriptionCode": V("Month", "A monthly bill."),
                           "Description": V("March 2026", "The period in words.")}}


def levy(m3, who):
    return {"item": "sewage-levy", "qty": m3, "invoice_why": f"The {who}'s water use, on which the city charges its "
                                                            "levy.",
            "line_extra": {**MARCH, "CollectedForParty": party("2-xb", short=True),
                           "Note": V("Collected for the city of Lumeport and paid on to it.", "Why the water company "
                                                                                              "bills it.")}}


BILLS = {"33-xu": [{"item": "electricity", "qty": 412800, "invoice_why": "The factory's metered consumption in March.",
                    "line_extra": MARCH},
                   {"item": "electricity", "qty": 18600, "invoice_why": "The warehouse's metered consumption in March; "
                                                                        "the manufacturer pays for its building.",
                    "line_extra": {**MARCH, "AccountingCostCode": V("7100", "The manufacturer books the warehouse's "
                                                                            "power on its transport cost centre."),
                                   "AccountingCost": V("Warehouse, Castrano Logistics", "In words."),
                                   "Delivery": {"DeliveryLocation": {"Description": V(
                                       "Castrano Logistics warehouse, Ferrano", "Where the power was used.")}}}}],
         "34-xb:26-xb": [{"item": "water", "qty": 86, "invoice_why": "The shop's metered consumption in March.",
                          "line_extra": MARCH}, levy(86, "shop")],
         "34-xb:c-xb": [{"item": "water", "qty": 14, "invoice_why": "The household's metered consumption in March.",
                         "line_extra": MARCH}, levy(14, "household")],
         "35-xl": [{"item": "telecom-line", "qty": 6, "invoice_why": "Six business lines for the month."},
                   {"item": "telecom-data", "qty": 35, "invoice_why": "Mobile data beyond the subscriptions."}]}
KIND = {"33-xu": "Electricity", "34-xb": "Water", "35-xl": "Telephone"}
METERS = {"33-xu": ["FE-C-0047120", ("FE-M-881204", "Factory, main connection"),
                    ("FE-M-881377", "Warehouse of Castrano Logistics")],
          "34-xb:26-xb": ["CSW-C-260118", ("CSW-W-55102", "Shop, Lumeport"), None],
          "34-xb:c-xb": ["CSW-C-311790", ("CSW-W-71844", "Gull Lane 57"), None],
          "35-xl": ["ST-C-1077", ("ST-L-BUS6", "Six business lines"), ("ST-D-0042", "Mobile data pool")]}


def energy_tax(f, out, key):
    """Urvania's energy tax on the electricity bill: per kWh in two tiers, and value added tax on the price plus the
    energy tax (world/countries.json)."""
    exc = next(x for x in WORLD["countries"]["XU"]["tax"]["schemes"] if x["id"] == "EXC")
    vat = WORLD["countries"]["XU"]["tax"]["schemes"][0]
    kwh = sum(Decimal(str(r["qty"])) for r in BILLS["33-xu"])
    lines = Decimal(out["LegalMonetaryTotal"]["LineExtensionAmount"].value)
    t1 = min(kwh, Decimal(exc["tiers"][0]["up_to"]))
    tiers = [(t1, Decimal(exc["tiers"][0]["per_unit"]), "The first 50,000 kWh of the month"),
             (kwh - t1, Decimal(exc["tiers"][1]["per_unit"]), "Above 50,000 kWh: the industrial rate")]
    excise = sum(money(q * r, "XUF") for q, r, _ in tiers)
    assert excise == Decimal(BILL_EXCISE)
    vat_base = lines + excise
    vat_amt = money(vat_base * Decimal(vat["rates"]["standard"]) / 100, "XUF")
    subs = []
    for q, r, what in tiers:
        subs.append({"TaxableAmount": amount(q * r, "XUF", "The tax base of the tier, in ferra."),
                     "TaxAmount": amount(q * r, "XUF", f"{q} kWh at {r} ferra."),
                     "CalculationSequenceNumeric": V("1", "The energy tax is calculated first."),
                     "BaseUnitMeasure": V("1", "The tax is per kilowatt hour.", unitCode="KWH"),
                     "PerUnitAmount": amount(r, "XUF", "The tax per kWh in this tier."),
                     "TierRange": V(what, "The tier of the monthly consumption."),
                     "TaxCategory": {"ID": V("S", "The energy tax applies."),
                                     "Name": V("Energy tax", "The tax in words."),
                                     "BaseUnitMeasure": V("1", "Per kilowatt hour.", unitCode="KWH"),
                                     "PerUnitAmount": amount(r, "XUF", "The rate per kWh."),
                                     "TierRange": V(what, "The tier."),
                                     "TaxScheme": {"ID": V("EXC", "UN/EDIFACT 5153 code EXC: excise duty, the energy "
                                                                  "tax.")}},
                     "TaxDueCountry": {"IdentificationCode": V("XU", "Due in Urvania.")}})
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


BILL_EXCISE = "288840"     # the energy tax of the electricity bill (see energy_tax), shown on the statement too
POINTS = {  # the consumption points behind the bills: meters, readings, history (the utilities' own records)
    ("33-xu", "5-xu"): {"line": 0, "id": "FE-CP-4120-01", "desc": "Factory, main connection at 10 kV",
                        "type": ("Industrial", "IND"), "meter": ("FE-M-881204", "Main meter, factory", "40",
                                                                 "Transformer ratio"),
                        "prev": ("2026-02-28", 52960, "Remote reading", "REMOTE"),
                        "last": ("2026-03-31", 63280, "Remote reading", "REMOTE"),
                        "history": [("2026-01-01", "2026-01-31", 398400), ("2026-02-01", "2026-02-28", 405100)]},
    ("33-xu", "8-xu"): {"line": 1, "id": "FE-CP-4160-07", "desc": "Warehouse of Castrano Logistics",
                        "type": ("Commercial", "COM"), "meter": ("FE-M-881377", "Warehouse meter", "1", "Direct"),
                        "prev": ("2026-02-28", 117250, "Estimated: no access to the meter", "ESTIMATE"),
                        "last": ("2026-03-31", 135850, "Read by the meter reader", "MANUAL"),
                        "history": [("2026-01-01", "2026-01-31", 17900), ("2026-02-01", "2026-02-28", 17200)],
                        "correction": (-750, "February's estimate of 17,200 kWh was 750 kWh too high, as the "
                                             "actual reading shows.")},
    ("34-xb", "26-xb"): {"line": 0, "id": "CSW-CP-38510-411", "desc": "Shop, Lumeport", "type": ("Commercial", "COM"),
                         "meter": ("CSW-W-55102", "Water meter, shop", "1", "Direct"),
                         "prev": ("2026-02-28", 4212, "Remote reading", "REMOTE"),
                         "last": ("2026-03-31", 4298, "Remote reading", "REMOTE"),
                         "history": [("2026-01-01", "2026-01-31", 81), ("2026-02-01", "2026-02-28", 79)]},
    ("34-xb", "c-xb"): {"line": 0, "id": "CSW-CP-38516-57", "desc": "Gull Lane 57, Lumeport",
                        "type": ("Household", "HH"), "meter": ("CSW-W-71844", "Water meter, flat", "1", "Direct"),
                        "prev": ("2026-02-28", 1830, "Read by the household", "CUSTOMER"),
                        "last": ("2026-03-31", 1844, "Read by the household", "CUSTOMER"),
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
            "Period": {"StartDate": V("2026-03-01", "March."), "EndDate": V("2026-03-31", "Its last day.")},
            "TaxTotal": {"TaxAmount": amount(tax, cur, f"{rule[1]} % of the line.")},
            "UtilityItem": {"ID": V(it["sellers_id"], "The utility's tariff item."),
                            "SubscriberID": V(METERS[key][0], "The customer's contract."),
                            "SubscriberType": V(KIND[sup], "The kind of supply."),
                            "SubscriberTypeCode": V(KIND[sup][:4].upper(), "As a code."),
                            "Contract": {"ID": V(METERS[key][0], "The supply contract the tariff belongs to.")},
                            "Description": V(it["description"], "The tariff in words."),
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
           **kit.cost_centre(customer, "The customer's cost centre, as on the bill."),
           "AdditionalDocumentReference": {"ID": V(f"{kit.initials(sup)}-TARIFF-2026", "The utility's tariff sheet "
                                                                                   "for 2026."),
                                           "DocumentTypeCode": V("Tariff", "What the document is."),
                                           "DocumentDescription": V("Prices per unit and the terms of supply.",
                                                                    "What it holds.")},
           "CustomerParty": {"Party": party(customer, short=True)}}
    if (sup, subscriber) in POINTS:
        pt = POINTS[(sup, subscriber)]
        d = rows[pt["line"]]
        line, amt, tax = consumption_line(f, sup, key, pt["line"], d, "The consumption of this point.")
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
                   "PreviousMeterReadingMethod": V(pt["prev"][2], "How the previous reading was taken."),
                   "PreviousMeterReadingMethodCode": V(pt["prev"][3], "As a code."),
                   "LatestMeterReadingMethod": V(pt["last"][2], "How this reading was taken."),
                   "LatestMeterReadingMethodCode": V(pt["last"][3], "As a code."),
                   "DeliveredQuantity": qty(consumed, unit, f"The difference of the readings"
                                            + (f", times the meter constant of {constant}." if constant != 1 else
                                               "."))}
        if pt.get("correction"):
            reading["MeterReadingComments"] = V("The previous reading was an estimate.", "Why the readings are "
                                                                                          "corrected.")
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
                      "TotalConsumedQuantity": qty(pt["history"][-1][2], unit, "What February's report said."),
                      "Period": {"StartDate": V(pt["history"][-1][0], "February."),
                                 "EndDate": V(pt["history"][-1][1], "Its last day.")}},
                  "ConsumptionHistory": [{"MeterNumber": V(pt["meter"][0], "The meter."),
                                          "Quantity": qty(q_, unit, "The month's consumption."),
                                          "Amount": amount(Decimal(q_) * Decimal(str(ITEM[d["item"]]["price"]
                                                                                    ["amount"])), cur,
                                                           "What it cost at the tariff."),
                                          "ConsumptionLevelCode": V("Normal", "Within the usual range."),
                                          "ConsumptionLevel": V("Normal", "In words."),
                                          "Description": V("Earlier month.", "For comparison."),
                                          "Period": {"StartDate": V(a, "The month."), "EndDate": V(b, "Its end.")}}
                                         for a, b, q_ in pt["history"]]}
        if pt.get("household"):
            h = pt["household"]
            report.update({"ResidentOccupantsNumeric": V(h["occupants"], "People living in the flat."),
                           "ResidenceType": V(h["residence"][0], "The kind of home."),
                           "ResidenceTypeCode": V(h["residence"][1], "As a code."),
                           "HeatingType": V(h["heating"][0], "How the home is heated: not with this water."),
                           "HeatingTypeCode": V(h["heating"][1], "As a code."),
                           "ConsumersEnergyLevelCode": V("Low", "Below the average for two occupants."),
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
        if sup == "33-xu" and pt["line"] == 0:
            exc = Decimal(BILL_EXCISE)
            supply["EnergyTaxReport"] = {"TaxEnergyAmount": amount(exc, cur, "The energy tax of the bill, for all "
                                                                             "the customer's points."),
                                         "TaxEnergyOnAccountAmount": amount(0, cur, "No energy tax paid on account."),
                                         "TaxEnergyBalanceAmount": amount(exc, cur, "Due with this bill."),
                                         "TaxScheme": {"ID": V("EXC", "Urvania's energy tax.")}}
        if pt.get("correction"):
            dq, why = pt["correction"]
            p_ = Decimal(str(ITEM[d["item"]]["price"]["amount"]))
            supply["EnergyWaterConsumptionCorrection"] = {
                "CorrectionType": V("Estimate correction", "The kind of correction."),
                "CorrectionTypeCode": V("EST", "As a code."),
                "MeterNumber": V(pt["meter"][0], "The meter."),
                "Description": V(why, "Why."),
                "CorrectionUnitAmount": amount(p_, cur, "The tariff per kWh."),
                "ConsumptionEnergyQuantity": qty(dq, unit, "The correction of February's quantity."),
                "CorrectionAmount": amount(p_ * dq, cur, "Credited on the April bill.")}
        consumption = {"UtilityStatementTypeCode": V(KIND[sup], "The kind of supply."),
                       "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                      "EndDate": V("2026-03-31", "Its last day.")},
                       "TaxTotal": {"TaxAmount": amount(tax, cur, "The tax of this point's consumption.")},
                       "EnergyWaterSupply": supply,
                       "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, cur, "The consumption."),
                                              "PayableAmount": amount(amt + tax, cur, "With its tax.")}}
        sub = {"ConsumptionID": V(f"{pt['id']}-2603", "The consumption of the point in March."),
               "SpecificationTypeCode": V("Detailed", "A detailed specification."),
               "Note": V(pt["desc"], "The point."),
               "TotalMeteredQuantity": qty(consumed, unit, "Metered in March."),
               "UtilityConsumptionPoint": {
                   "ID": V(pt["id"], "The connection's number."),
                   "Description": V(pt["desc"], "Where."),
                   "SubscriberID": V(METERS[key][0], "The contract it belongs to."),
                   "SubscriberType": V(pt["type"][0], "The kind of customer."),
                   "SubscriberTypeCode": V(pt["type"][1], "As a code."),
                   "TotalDeliveredQuantity": qty(consumed, unit, "Delivered in March."),
                   "Address": address(subscriber),
                   "WebSiteAccess": {"URI": V(PARTY[sup]["identity"].get("website", "https://www.example") +
                                              "/meter", "Where the customer sees the readings."),
                                     "Login": V(pt["id"], "The customer logs in with the point's number."),
                                     "Password": V("********", "Never printed: the customer chose it online.")},
                   "UtilityMeter": {"MeterNumber": V(pt["meter"][0], "The meter."),
                                    "MeterName": V(pt["meter"][1], "Its name."),
                                    "MeterConstant": V(pt["meter"][2], "The register is multiplied by this."),
                                    "MeterConstantCode": V(pt["meter"][3], "Why: " + pt["meter"][3].lower() + "."),
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
                   "Consumption": {"UtilityStatementTypeCode": V(KIND[sup], "The supply under the contract."),
                                   "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                                  "EndDate": V("2026-03-31", "Its last day.")},
                                   "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, cur, "The line."),
                                                          "PayableAmount": amount(amt + tax, cur, "With its "
                                                                                                  "tax.")}},
                   "Contract": {"ID": V(METERS[key][0], "The supply contract."),
                                "ContractType": V(f"{KIND[sup]} supply", "Its kind."),
                                "ValidityPeriod": {"StartDate": V("2024-01-01", "In force since.")}},
                   "ConsumptionLine": line}}
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
                                       "Note": V("No payment on account: the bill follows the reading.",
                                                 "How the household pays."),
                                       "PaymentTerms": {"Note": V("By direct debit 21 days after the bill.",
                                                                  "As on the bill.")}}
        out["SubscriberConsumption"] = sub
    else:                                     # the telecom company: lines, calls and data
        out["SubscriberConsumption"] = telecom_consumption(f, sup, key, customer)
    return out


def telecom_consumption(f, sup, key, customer):
    cur = "XLC"
    line_item, data_item = ITEM["telecom-line"], ITEM["telecom-data"]
    base = "+999 3 3000 18"
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
                 "TelecommunicationsServiceCategory": V("International call", "The kind of service."),
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
                 "TelecommunicationsServiceCategory": V("Data roaming", "The kind of service."),
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
            "SpecificationTypeCode": V("Detailed", "With the calls."),
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
            "Consumption": {"UtilityStatementTypeCode": V("Telephone", "The kind of supply."),
                            "MainPeriod": {"StartDate": V("2026-03-01", "March."),
                                           "EndDate": V("2026-03-31", "Its last day.")},
                            "TelecommunicationsSupply": {
                                "TelecommunicationsSupplyType": V("Business lines and data", "The supply."),
                                "TelecommunicationsSupplyTypeCode": V("BUS", "As a code."),
                                "PrivacyCode": V("Masked", "Numbers called inside the island are not listed; "
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
                "UtilityStatementTypeCode": V(KIND[sup], "The kind of utility the statement is about."),
                "DocumentCurrencyCode": kit.currency_line(kit.currency_of(sup), "the utility's currency"),
                "ParentDocumentReference": {"ID": V(invoice_no, "The invoice this statement supplements: a utility "
                                                                "statement adds the consumption behind the bill.")},
                **utility_statement(f, n, doc, key, invoice_no)}
    if doc["doc"] == "Invoice":
        key = bill_key(doc)
        out = kit.invoice(f, n, doc, 1, 21, "The monthly bill, issued on the first day of the next month.", {},
                          BILLS[key], key=f"invoice-{key}", extra=MARCH)
        purpose = {"33-xu": ("ELEC", "electricity bill"), "35-xl": ("PHON", "telephone bill")}.get(
            key, ("WTER", "water bill"))
        meters = METERS[key]
        out["PurchaseReference"] = {"ID": V(meters[0], "The customer's contract number with the utility."),
                                    "Description": V("Supply contract", "What the number is.")}
        for line, meter in zip(out["InvoiceLine"], meters[1:]):
            line["PaymentPurposeCode"] = V(purpose[0], f"ISO 20022 purpose code {purpose[0]}: {purpose[1]}.")
            if meter:
                line["PurchaseReference"] = {"ID": V(meter[0], "The meter or subscription the line is for."),
                                             "Description": V(meter[1], "Where it is.")}
        if key == "33-xu":
            out["InvoiceLine"][1]["OriginatorParty"] = party("8-xu", short=True)
            out["BillingReference"] = {"InvoiceDocumentReference": {
                "ID": V("FE-INV-26-0211", "February's bill, with an estimated reading of the warehouse meter."),
                "IssueDate": V("2026-03-01", "Its issue date.")},
                "BillingReferenceLine": {"ID": V("2", "Its warehouse line, which the statement of this bill "
                                                      "corrects; the difference follows on the April bill.")}}
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
                    "MandateTypeCode": V("Recurrent", "A mandate for repeated collections."),
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
            out["PaymentTerms"]["Note"] = V("Collected by direct debit 21 days after the invoice date.",
                                            "How the household pays.")
        return out
    if doc["doc"] == "RemittanceAdvice":
        if bill_key(doc) == "33-xu":
            return kit.remittance(f, n, doc, 9, "Paid within ten days, to take the cash discount of the invoice's "
                                                "terms.", key="invoice-33-xu", discount="2")
        return kit.remittance(f, n, doc, 18, "Paid before the due date.", key=f"invoice-{bill_key(doc)}")
    if doc["doc"] == "Reminder":
        key, cur = bill_key(doc), "XBL"
        due = f.numbers[f"invoice-{key}-amount"]
        return {"ID": V(f.number("reminder", doc["from"], "Reminder"), "The reminder number."),
                "IssueDate": V(f.date(30), "Sent a week after the due date passed without payment."),
                "ReminderTypeCode": V("Payment", "A reminder of a payment overdue."),
                "ReminderSequenceNumeric": V("1", "The first reminder."),
                "Note": V("The direct debit was returned by your bank: insufficient funds.", "Why the bill is "
                                                                                              "unpaid."),
                "DocumentCurrencyCode": kit.currency_line(cur, "the currency of the unpaid bill"),
                "ReminderPeriod": {"StartDate": V(f.date(22), "Overdue from the failed collection."),
                                   "EndDate": V(f.date(30), "Until the reminder.")},
                "AccountingCostCode": V("1210", "The water company's receivables account for households."),
                "AccountingCost": V("Household receivables", "In words."),
                "LineCountNumeric": V("2", "The bill and the fee."),
                "AdditionalDocumentReference": {"ID": V("BLUM-RTN-26-04-0193", "The bank's notice that the direct "
                                                                               "debit was returned."),
                                                "DocumentTypeCode": V("ReturnNotice", "What the document is."),
                                                "IssueDate": V(f.date(23), "The day after the failed collection."),
                                                "DocumentDescription": V("Direct debit returned: insufficient "
                                                                         "funds.", "What it says."),
                                                "IssuerParty": party("25-xb", short=True)},
                "PayeeParty": party("34-xb", short=True),
                "PaymentTerms": {"Note": V("Please pay within ten days by credit transfer; the next collection will "
                                           "be by direct debit again.", "What the household is asked to do."),
                                 "PaymentDueDate": V(f.date(40), "Ten days after the reminder.")},
                "TaxTotal": {"TaxAmount": amount(0, cur, "No sales tax on a reminder fee."),
                             "TaxSubtotal": {"TaxableAmount": amount(Decimal("5.00"), cur, "The fee."),
                                             "TaxAmount": amount(0, cur, "None."),
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
                                  "PenaltySurchargePercent": V("0", "No surcharge yet: the first reminder."),
                                  "AccountingCostCode": V("8320", "The water company books the fee as other "
                                                                  "income."),
                                  "AccountingCost": V("Reminder fees", "In words.")}]}
    raise SystemExit(f"utilities scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the wood flow (Bayvarra -> Urvania, and at home)
PALLETS_CHARGE = {"like": "slat-1800", "amount": "240.00", "reason": "Heat-treated export pallets",
                  "why": "96 bundles on pallets treated to ISPM 15, as the quotation offered for the export.",
                  "amount_why": "96 pallets at 2.50 lume."}
SLATS = [{"item": "slat-1800", "ordered": 4800, "why": "Slats for 960 benches: five per bench, 96 bundles of 50."}]
TIMBER = [{"item": "timber-beam", "ordered": 12, "why": "Hardwood for a month of furniture production."}]
WOOD = kit.Flow("wood", "2026-02-16", SLATS)


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
        return kit.order(f, n, doc, 6, "The manufacturer accepts the quotation and orders.",
                         "Delivered at place, the factory: the sawmill delivers; the manufacturer clears the import.",
                         "Valdara Industries, goods-in, Ferrano",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted.")})
    if doc["doc"] == "TransportExecutionPlanRequest":
        return kit.tep_request(f, n, doc, 7, "Under DAP the sawmill books the truck across the border.", 10,
                               kit.gross_weight(f, "ordered"), "96 bundles of slats.")
    if doc["doc"] == "ExportCustomsDeclaration":
        return kit.export_declaration(f, n, doc, 10, "Declared when the truck leaves for the border.",
                                      "The value of the slats, in lume.")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 10, "The day the truck was loaded at the sawmill.",
                                   "The gross weight of the bundles.")
    if doc["doc"] == "ImportCustomsDeclaration":
        return kit.import_declaration(f, n, doc, 11, "The manufacturer declares the import into Urvania.",
                                      "The customs value in ferra: the value in lume at the reference rate (1 lume = 100 "
                                      "ferra).")
    if doc["doc"] == "Invoice" and doc["to"] == "5-xu":
        return kit.invoice(f, n, doc, 10, 30, "Issued when the slats leave.",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "slat-1800", "qty": 4800, "invoice_why": "The slats despatched."}],
                           charges=[PALLETS_CHARGE])
    if doc["doc"] == "RemittanceAdvice":
        return kit.remittance(f, n, doc, 38, "The manufacturer pays across the border.")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 20, "The furniture maker orders timber, collected with its own van.",
                         "Ex works the sawmill: the buyer collects the timber and bears every cost from the sawmill's "
                         "yard.", "Marrowdale Sawmill, timber yard", deal=TIMBER, key="order-timber")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 21, 30, "Issued when the timber was collected.",
                           {"OrderReference": ref(f, "order-timber", "The furniture maker's order.")},
                           [{"item": "timber-beam", "qty": 12, "invoice_why": "The cubic metres collected."}],
                           key="invoice-timber")
    raise SystemExit(f"wood scenario: no document {n} {doc['doc']}")


# ---------------------------------------------------------------- the furniture flow (Bayvarra)
SET_PARTS = [("BF-GS-01-B", "Garden bench Marrow, 1400 mm", 1, "380.00"),
             ("BF-GS-01-C", "Garden chair Marrow", 2, "115.00")]


def set_parts(sets, kind):
    """The parts of the garden set, as sub-lines: a bench and two chairs per set; their prices add up to the set's."""
    out = []
    for k, (sid, name, per, price_) in enumerate(SET_PARTS, 1):
        q = sets * per
        x = {"ID": V(f"1.{k}", "A part of the set."),
             "LineExtensionAmount": amount(Decimal(price_) * q, "XBL", f"{q} at {price_} lume: the parts add up to "
                                                                      "the set's price."),
             "Price": {"PriceAmount": price(price_, "XBL", "The part's share of the set price.")},
             "Item": {"Name": V(name, "The part."), "SellersItemIdentification": {"ID": V(sid, "The maker's number "
                                                                                              "for the part.")}}}
        x["Quantity" if kind == "order" else "InvoicedQuantity"] = qty(q, "H87", f"{per} per set.")
        out.append(x)
    return out


SETS = [{"item": "garden-set", "ordered": 20, "why": "The first delivery of the store's own garden furniture line.",
         "line_extra": {
             "Note": V("The store's own line: bench and two chairs per set.", "What the line is."),
             "MinimumQuantity": qty(10, "SET", "The store accepts a first part of at least ten sets."),
             "MaximumQuantity": qty(20, "SET", "And no more than ordered."),
             "BackOrderAllowedIndicator": V("true", "What cannot be delivered now may follow."),
             "MinimumBackorderQuantity": qty(5, "SET", "But only in lots of at least five."),
             "MaximumBackorderQuantity": qty(10, "SET", "And at most ten on back order."),
             "InspectionMethodCode": V("Visual", "The goods-in checks each set by eye."),
             "AccountingCostCode": V("6120", "The garden department's cost centre."),
             "AccountingCost": V("Garden department", "In words."),
             "WarrantyValidityPeriod": {"DurationMeasure": V("2", "Two years on the joints.", unitCode="ANN")},
             "WarrantyParty": party("37-xb", short=True),
             "PricingReference": {"OriginalItemLocationQuantity": {"Price": {
                 "PriceAmount": price("610.00", "XBL", "The price of the quotation, which the order accepts.")}}},
             "SubLineItem": set_parts(20, "order")},
         "orderline_extra": {"Note": V("Price as quoted.", "Why no price question."),
                             "QuotationLineReference": {"LineID": V("1", "The quotation line accepted.")}}}]
DESKS = [{"item": "office-desk", "ordered": 6, "why": "Six desks for the new planning office."},
         {"item": "installation", "ordered": 14, "why": "Two installers for seven hours."}]
FURNITURE = kit.Flow("furniture", "2026-03-02", SETS)


def collab(f, doc, key, day, why):
    return {"ID": V(f.number(key, doc["from"], key), f"The sender's number for its {key.replace('-', ' ')}."),
            "IssueDate": V(f.date(day), why)}


def furniture(n, doc):
    f = FURNITURE
    sets = item("garden-set")
    if doc["doc"] == "RequestForQuotation":
        return rfq(f, doc, 0, "The store wants its own garden furniture line.", SETS)
    if doc["doc"] == "Quotation":
        return quotation(f, doc, 4, "The furniture maker quotes the line.", SETS, 60)
    if doc["doc"] == "ItemInformationRequest":
        return {**collab(f, doc, "info-request", 10, "Asked before the first production run."),
                "Period": period(f, 14, 70, "The season the information is wanted for.", "Its end."),
                "ItemInformationRequestLine": {
                    "Period": period(f, 14, 70, "Sales data for the season.", "Its end."),
                    "SalesItem": {"Quantity": qty(20, "SET", "The quantity of the first delivery, to compare sales "
                                                             "against."), "Item": sets}}}
    if doc["doc"] == "TradeItemLocationProfile":
        return {**collab(f, doc, "location-profile", 12, "The store sets its replenishment policy for the line."),
                "Period": period(f, 14, 180, "The policy holds for the season.", "Its end."),
                "ItemManagementProfile": {"EffectivePeriod": period(f, 14, 180, "From the first delivery.", "To the end of "
                                                                                                         "the season."),
                                          "Item": sets}}
    if doc["doc"] == "ExceptionCriteria":
        return {**collab(f, doc, "exception-criteria", 12, "Agreed together with the replenishment policy."),
                "ValidityPeriod": period(f, 14, 180, "Valid for the season.", "Its end."),
                "ExceptionCriteriaLine": {
                    "ID": V("1", "The only criterion."),
                    "ThresholdValueComparisonCode": V("LessThan", "An exception is raised when actual sales fall "
                                                                  "below the threshold."),
                    "ThresholdQuantity": qty(5, "SET", "Fewer than five sets sold in four weeks is worth a message."),
                    "SupplyItem": sets}}
    if doc["doc"] == "ProductActivity":
        return {**collab(f, doc, "activity", 49, "The store's report of the first four weeks."),
                "ActivityPeriod": period(f, 21, 49, "The four weeks reported.", "Their end."),
                "SupplyChainActivityDataLine": {
                    "ID": V("1", "The only line."),
                    "SupplyChainActivityTypeCode": V("Sales", "The activity reported: sales to consumers."),
                    "ActivityOriginLocation": {"Name": V("Brightmarket Stores, garden department, Lumeport",
                                                         "Where the sales took place.")},
                    "SalesItem": {"Quantity": qty(3, "SET", "Three sets sold in four weeks."), "Item": sets}}}
    if doc["doc"] == "ExceptionNotification":
        return {**collab(f, doc, "exception", 50, "The furniture maker sees the sales below the agreed threshold."),
                "ExceptionObservationPeriod": period(f, 21, 49, "The four weeks observed.", "Their end."),
                "ExceptionNotificationLine": {
                    "ID": V("1", "The only exception."),
                    "ComparedValueMeasure": V("5", "The agreed threshold: five sets in four weeks.", unitCode="SET"),
                    "SourceValueMeasure": V("3", "The sales the store reported: three sets.", unitCode="SET"),
                    "SupplyItem": sets}}
    if doc["doc"] == "Order" and doc["from"] == "26-xb":
        return kit.order(f, n, doc, 14, "The store orders the first delivery of its line.",
                         "Delivered at place, the store: the furniture maker delivers with its own van.",
                         "Brightmarket Stores, goods-in, Lumeport",
                         {"QuotationDocumentReference": ref(f, "quotation", "The quotation accepted.")})
    if doc["doc"] == "Invoice" and doc["to"] == "26-xb":
        return kit.invoice(f, n, doc, 20, 30, "Issued on delivery.", {"OrderReference": ref(f, "order", "The store's "
                                                                                                       "order."),
                                                                      "DeliveryNoteDocumentReference": {
                                                                          "ID": V("BF-DN-26-0320", "The delivery "
                                                                                  "note the store signed when the "
                                                                                  "van unloaded.")}},
                           [{"item": "garden-set", "qty": 20, "invoice_why": "The sets delivered.",
                             "line_extra": {"SubInvoiceLine": set_parts(20, "invoice")}}])
    if doc["doc"] == "InstructionForReturns":
        return {**collab(f, doc, "returns", 56, "The furniture maker takes back the sets that do not sell."),
                "InstructionForReturnsLine": {"ID": V("1", "The only line."),
                                              "Quantity": qty(6, "SET", "Six of the remaining sets, to free shelf "
                                                                        "space."),
                                              "Item": sets}}
    if doc["doc"] == "CreditNote":
        out = kit.credit_note(f, n, doc, 62, "Issued when the returned sets arrived back.",
                              [{"item": "garden-set", "qty": 6, "why": "The sets returned.",
                                "line_allowance": {"percent": "5", "code": "64",
                                                   "code_why": "UN/EDIFACT 5189 code 64: special agreement.",
                                                   "reason": "Restocking deduction",
                                                   "why": "The instruction for returns lets the furniture maker "
                                                          "keep 5 % for restocking the sets."}}],
                              {"BillingReference": {"InvoiceDocumentReference": {
                                  "ID": V(f.numbers["invoice"], "The invoice of the returned sets."),
                                  "IssueDate": V(f.numbers["invoice-date"], "Its issue date.")}},
                               "OrderReference": {"ID": V(f.numbers["order"], "The order of the sets.")},
                               "AdditionalDocumentReference": {"ID": V(f.numbers["returns"], "The instruction for "
                                                                                             "returns.")},
                               "DueDate": V(f.date(72), "The furniture maker pays the credit back within ten "
                                                        "days."),
                               "Note": V("The store paid the invoice; the credit is refunded.", "Why money "
                                                                                                "goes back.")})
        out["PaymentMeans"] = kit.payment_means(f, "26-xb", "37-xb", "26-xb", 62, 10, out["ID"].value,
                                                "The store's account, where the refund goes.")
        return out
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 30, "The public works department furnishes its new planning office.",
                         "Delivered at place, the office: the furniture maker delivers and installs.",
                         "Lumeport Public Works Department, Civic Square", deal=DESKS, key="order-desks")
    if doc["doc"] == "WorkReport":
        return {**collab(f, doc, "work-report", 38, "Reported when the installation was finished."),
                "WorkReportLine": {"ID": V("1", "The installation work."),
                                   "Quantity": qty(14, "HUR", "Two installers for seven hours, approved by the "
                                                              "department.")}}
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 38, 30, "Issued once the work report was approved.",
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
                           charges=[{"like": "installation", "amount": "24.00", "reason": "Packaging disposal",
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
        return kit.invoice(f, n, doc, 5, 30, "Issued when the film was collected.",
                           {"OrderReference": ref(f, "order", "The manufacturer's order.")},
                           [{"item": "film-pe", "qty": 480, "invoice_why": "The kilograms collected."}])
    if doc["doc"] == "Order" and doc["from"] == "40-xb":
        return kit.order(f, n, doc, 2, "The textile mill orders garment bags.",
                         "Delivered at place, the mill: the packaging maker delivers.", "Lumeport Textile Mill, goods-in",
                         deal=BAGS, key="order-bags")
    if doc["doc"] == "Invoice" and doc["to"] == "40-xb":
        return kit.invoice(f, n, doc, 6, 30, "Issued on delivery.", {"OrderReference": ref(f, "order-bags",
                                                                                           "The mill's order.")},
                           [{"item": "garment-bag", "qty": 20000, "invoice_why": "The bags delivered."}],
                           key="invoice-bags")
    if doc["doc"] == "Order":
        return kit.order(f, n, doc, 10, "The store orders shirts for spring.",
                         "Delivered duty paid at the store: the mill delivers and bears every cost.",
                         "Brightmarket Stores, goods-in, Lumeport", deal=SHIRTS, key="order-shirts")
    if doc["doc"] == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 15, "The day the shirts left the mill.", "The gross weight of the cartons.",
                                   deal=SHIRTS, key="order-shirts")
    if doc["doc"] == "Invoice":
        return kit.invoice(f, n, doc, 15, 30, "Issued on delivery.",
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
                               "The corrected tender, submitted the day after the withdrawal."),
                **folder,
                "TenderedProject": {"LegalMonetaryTotal": {
                    "PayableAmount": amount(price * TENDER_QTY, "XBL",
                                            f"{TENDER_QTY} wooden benches at {price} lume" +
                                            (": the price per bench was entered wrongly." if k == 1 else
                                             ", the corrected price."))}}}
    if d == "TenderWithdrawal":
        return {**head(f, "withdrawal", doc, 43, "Withdrawn before the deadline, which the procedure allows."),
                **folder,
                "WithdrawOfferIndicator": V("true", "The whole tender is withdrawn."),
                "TenderDocumentReference": {"ID": V(f.numbers["tender-37-1"], "The tender withdrawn.")}}
    if d == "TendererQualificationResponse":
        return {**head(f, "qualification-response", doc, 50, "After the check of the qualifications."), **folder,
                "QualificationResolution": {"AdmissionCode": V("Admitted", "The tenderer meets the selection criteria "
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
    train = {"JourneyID": V("CT 4471", "The number of the container train in the hub's timetable.")}
    if d == "TransportProgressStatusRequest":
        return {**head(f, "tps-request", doc, 8, "Asked on the morning of departure."),
                "IssueTime": V("06:30:00", "Before the train leaves the hub."), "TransportMeans": train}
    if d == "TransportProgressStatus":
        return {**head(f, "tps", doc, 8, "Answered at once."), "IssueTime": V("06:45:00", "A quarter of an hour later."),
                "TransportMeans": train}
    if d == "GoodsItemItinerary":
        return {**head(f, "itinerary", doc, 8, "Sent when the containers are on the train."),
                "IssueTime": V("09:00:00", "After loading."),
                "VersionID": V("1", "The first version of the itinerary."),
                "TransportExecutionPlanReferenceID": V(f.numbers["tep"], "The transport plan the itinerary belongs to."),
                "TransportationSegment": {
                    "SequenceNumeric": V("1", "One segment: by rail from the hub to the distributor's siding."),
                    "TransportExecutionPlanReferenceID": V(f.numbers["tep"], "The plan the segment is carried out "
                                                                             "under."),
                    "ReferencedConsignment": {"ID": V(f.numbers["consignment"], "The consignment on the segment.")},
                    "ShipmentStage": {"ID": V("1", "The rail stage."),
                                      "TransportModeCode": V("2", "Rail transport.", listID="UNECE Recommendation 19 - "
                                                                                            "Codes for Modes of "
                                                                                            "Transport")},
                    "TransportationService": {"TransportServiceCode": V("RailContainer", "The rail carrier's own code "
                                                                                         "for its container train "
                                                                                         "service.")}}}
    return _rail(n, doc)


def sea(n, doc):
    f, d = SEA, doc["doc"]
    service = {"TransportServiceCode": V("OceanContainer", "The carrier's code for its container liner service."),
               "Name": V("Weekly service Lumeport–Selanu", "The name of the service.")}
    if d == "BusinessCard":
        return head(f, "business-card", doc, 0, "Sent before the first offer to the new customer.")
    if d == "TransportServiceDescriptionRequest":
        return {**head(f, "tsd-request", doc, 4, "Asked once the order is accepted."),
                "IssueTime": V("14:00:00", "The time of the request."),
                "TransportationService": {"TransportServiceCode": V("OceanContainer", "The service asked about: a "
                                                                                      "container liner service.")}}
    if d == "TransportServiceDescription":
        return {**head(f, "tsd", doc, 5, "The carrier answers the next day."), "TransportationService": {
            **service,
            "TariffClassCode": V("FAK", "Freight all kinds: one rate whatever the goods."),
            "Priority": V("Standard", "The normal service."),
            "FreightRateClassCode": V("BOX", "The rate is per container."),
            "TransportationServiceDescription": V("A weekly feeder sailing from Lumeport to Selanu, two days at sea.",
                                                  "The service in words."),
            "TransportationServiceDetailsURI": V("https://www.tidewell.example/services/island", "Where the "
                                                                                                 "schedule is."),
            "NominationDate": V(f.date(5), "The day the service is offered for this shipment."),
            "NominationTime": V("10:00:00", "In the morning."),
            "SequenceNumeric": V("1", "The first of the services offered."),
            "SupportedTransportEquipment": [
                {"ID": V("22G1", "20-foot dry container."), "SizeTypeCode": V("22G1", "ISO 6346 size and type.")},
                {"ID": V("42G1", "40-foot dry container."), "SizeTypeCode": V("42G1", "ISO 6346 size and type.")}],
            "UnsupportedTransportEquipment": {"ID": V("45R1", "40-foot reefer: the island port has no reefer "
                                                              "plugs."),
                                              "SizeTypeCode": V("45R1", "ISO 6346 size and type.")},
            "TransportEquipment": {"ID": V("42G1", "The equipment offered for this shipment."),
                                   "SizeTypeCode": V("42G1", "A 40-foot dry container.")},
            "SupportedCommodityClassification": {"CargoTypeCode": V("GEN", "General cargo in containers.")},
            "UnsupportedCommodityClassification": {"CargoTypeCode": V("BULK", "No loose bulk on this service.")},
            "CommodityClassification": {"ItemClassificationCode": V("9401.79", "The benches.", listID="HS")},
            "TotalCapacityDimension": {"AttributeID": V("TEU", "The ship's capacity in twenty-foot units."),
                                       "Measure": V("1000", "One thousand.", unitCode="C62")},
            "ShipmentStage": {"ID": V("1", "Lumeport to Selanu."),
                              "TransportModeCode": V("1", "Maritime transport.", listID="UNECE Recommendation 19 - "
                                                                                        "Codes for Modes of "
                                                                                        "Transport")},
            "TransportEvent": kit.event(f, 10, "18:00:00", "The next departure from Lumeport.", done=False),
            "ResponsibleTransportServiceProviderParty": party("11-xb", short=True),
            "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2e", "Greenhouse gases."),
                                      "ValueMeasure": V("380", "Per 40-foot container on the crossing.",
                                                        unitCode="KGM")},
            "EstimatedDurationPeriod": {"DurationMeasure": V("2", "Two days at sea.", unitCode="DAY")},
            "ScheduledServiceFrequency": {"WeekDayCode": V("5", "Every Friday (ISO 8601: 5 is Friday).")}}}
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
        return {**head(f, "fulfilment-cancellation", doc, 3, "The flight left without the cargo."),
                "CancellationNote": V("The cargo missed its flight; it goes on the next day's flight under a new "
                                      "despatch advice.", "Why the despatch advice is cancelled."),
                "DespatchDocumentReference": {"ID": V(f.numbers["despatch"], "The despatch advice cancelled.")}}
    if d == "DespatchAdvice" and nth("air", n, doc) == 2:
        out = kit.despatch_advice(f, n, doc, 3, "Sent for the next day's flight.", "The gross weight of the boxed "
                                                                                    "frames.")
        out["ID"] = V(f.number("despatch-2", doc["from"], "DespatchAdvice"), "A new number: the first despatch "
                                                                             "advice was cancelled.")
        return out
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
                                                   "BaseQuantity": qty(1, "H87", "Per piece."),
                                                   "PriceList": {
                                                       "ID": V("6-XB-PL-2026-2", "The new price list."),
                                                       "StatusCode": V("Active", "It is in force from today."),
                                                       "ValidityPeriod": {"StartDate": V(f.date(30), "From the "
                                                                                         "update."),
                                                                          "EndDate": V(f.date(90), "Until the "
                                                                                       "catalogue ends.")},
                                                       "PreviousPriceList": {
                                                           "ID": V("6-XB-PL-2026", "The price list of the spring "
                                                                                   "catalogue it replaces."),
                                                           "StatusCode": V("Replaced", "No longer in force.")}}}}}}
    if d == "CatalogueItemSpecificationUpdate":
        it = item("bench-serra-b")
        it["Description"] = V("Park bench, 1800 mm, frame of cast and galvanised steel, five slats of another kiln-dried "
                              "hardwood, for bolting to the ground.", "The new description: the slats are now of a "
                                                                      "different hardwood.")
        return {**head(f, "spec-update", doc, 31, "The bench's slats changed wood."), "RelatedCatalogueReference": cat,
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
        return {**head(f, "application-response", doc, 9, "Sent automatically when the invoice was processed."),
                "DocumentResponse": response("AP", "UN/EDIFACT 4343 code AP: the invoice is accepted.",
                                             f.numbers["invoice"], "The invoice responded to.")}
    return _road(n, doc)


def furniture(n, doc):
    f, d = FURNITURE, doc["doc"]
    if d == "Order" and doc["from"] == "26-xb" and nth("furniture", n, doc) == 2:
        return kit.order(f, n, doc, 45, "A second delivery, before the slow sales were clear.",
                         "Delivered at place, the store, as the first delivery.", "Brightmarket Stores, goods-in, "
                                                                                 "Lumeport", key="order-2")
    if d == "OrderCancellation":
        return {**head(f, "order-cancellation", doc, 51, "Cancelled the day after the exception notification."),
                "CancellationNote": V("Sales of the line are below the agreed threshold; the second delivery is not "
                                      "needed.", "Why the order is cancelled."),
                "OrderReference": {"ID": V(f.numbers["order-2"], "The order cancelled.")}}
    if d == "DebitNote":
        rows = kit.spec_rows([{"item": "return-transport", "qty": 1}], "26-xb", "37-xb", "XBL")
        tax, total = kit.tax_total(rows, "XBL")
        amt = rows[0][2]
        out = {**head(f, "debit-note", doc, 63, "After the returned sets were collected."),
                "DebitNoteTypeCode": V("383", "UN/EDIFACT 1001 code 383: debit note."),
                "DefaultLanguageCode": V("en", "The language of the texts."),
                "LineCountNumeric": V("1", "One line."),
                "OrderReference": {"ID": V(f.numbers["order"], "The order of the sets that went back.")},
                "PaymentTerms": {"Note": V("30 days net.", "The store's terms."),
                                 "PaymentDueDate": V(f.date(93), "The due date.")},
                "DueDate": V(f.date(93), "Thirty days, the store's terms."),
                "Note": V("The furniture maker asked for the sets back; the store charges the transport.", "Why."),
                "DocumentCurrencyCode": kit.currency_line("XBL", "the currency of the trade"),
                **kit.cost_centre("26-xb", "The store books the income on its garden department."),
                "AdditionalDocumentReference": {"ID": V(f.numbers["returns"], "The instruction for returns that "
                                                                              "asked for the sets.")},
                "DiscrepancyResponse": {"ResponseCode": V("ReturnCost", "Why the store debits: the cost of a return "
                                                                        "the furniture maker asked for."),
                                        "Description": V("Return transport of six unsold garden sets.", "In "
                                                                                                       "words.")},
                "ContractDocumentReference": {"ID": V(f.numbers["quotation"], "The quotation the line was bought "
                                                                              "under; it puts returns at the "
                                                                              "maker's cost.")},
                "Delivery": {"ActualDeliveryDate": V(f.date(61), "The sets were delivered back."),
                             "DeliveryLocation": {"Name": V("Brackenmere Furniture, Marrowdale", "Where.")}},
                "PayeeParty": party("26-xb", short=True),
                "BuyerCustomerParty": {"Party": party("37-xb", short=True)},
                "SellerSupplierParty": {"Party": party("26-xb", short=True)},
                "BillingReference": {"CreditNoteDocumentReference": {"ID": V(next(v for k, v in f.numbers.items()
                                                                          if k.startswith("credit-")), "The credit note "
                                                                                                     "of the returned "
                                                                                                     "sets.")}},
                "TaxTotal": total,
                "LegalMonetaryTotal": {"LineExtensionAmount": amount(amt, "XBL", "The sum of the lines."),
                                           "PayableAmount": amount(amt + tax, "XBL", "What the furniture maker owes "
                                                                                     "the store.")},
                "DebitNoteLine": {"ID": V("1", "The return transport."),
                                  "DebitedQuantity": qty(1, "E48", "One return delivery."),
                                  "LineExtensionAmount": amount(amt, "XBL", "The store's charge for one return delivery."),
                                  "Note": V("Collected with the store's van.", "How the sets went back."),
                                  "DiscrepancyResponse": {"ResponseCode": V("ReturnCost", "The return transport.")},
                                  **kit.cost_centre("26-xb", "The store's cost centre the income is booked on."),
                                  "PaymentPurposeCode": V("TRPT", "ISO 20022 purpose code TRPT: transport."),
                                  "TaxInclusiveLineExtensionAmount": amount(amt + tax, "XBL", "The line with its "
                                                                                              "tax."),
                                  "TaxTotal": {"TaxAmount": amount(tax, "XBL", "The tax of the line.")},
                                  "DocumentReference": {"ID": V(f.numbers["returns"], "The instruction for "
                                                                                      "returns.")},
                                  "BillingReference": {"CreditNoteDocumentReference": {"ID": V(next(
                                      v for k, v in f.numbers.items() if k.startswith("credit-")), "The credit "
                                                                                                  "note.")},
                                                       "BillingReferenceLine": {"ID": V("1", "Its line of the "
                                                                                             "returned sets.")}},
                                  "Delivery": {"ActualDeliveryDate": V(f.date(61), "The day the sets were delivered "
                                                                                   "back to the furniture maker.")},
                                  "Item": item("return-transport", kit.tax_category(rows[0][3])),
                                  "Price": kit.price_block("return-transport")}}
        out["PaymentMeans"] = kit.payment_means(f, "26-xb", "37-xb", "26-xb", 63, 30, out["ID"].value,
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
        return {**head(f, "por-request", doc, 60, "Two months after the fair the samples' re-export is not recorded."),
                **passport}
    if d == "ProofOfReexportationReminder":
        return {**head(f, "por-reminder", doc, 90, "No answer after a month."),
                "ProcedureCode": V("TemporaryAdmission", "The procedure the samples were under on the island."),
                **passport,
                "ProofOfReexportationRequestDocumentReference": {"ID": V(f.numbers["por-request"], "The request "
                                                                                                   "unanswered.")},
                "GoodsItemPassportCounterfoil": {"ID": V("IMP-1", "The importation counterfoil without a re-export "
                                                                  "stamp.")}}
    if d == "ProofOfReexportation":
        return {**head(f, "proof", doc, 95, "Urvania's chamber answers with the proof."),
                "GoodsItemPassportCounterfoil": {"ID": V("REIMP-1", "The re-importation counterfoil, stamped by "
                                                                    "Urvania's customs when the samples came home.")},
                "ReexportationEvidence": {"ID": V("REIMP-1", "The evidence is the re-importation counterfoil itself."),
                                          "Description": V("Re-importation counterfoil of the carnet, stamped by "
                                                           "Urvania's customs: the samples left the island and came "
                                                           "home.", "What the evidence shows.")}}
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


def catalogue_ref(f, why, key="catalogue", version="1.0"):
    return {"ID": V(f.numbers[key], why), "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, f"urn:ubl-examples:world:"
                                                                                       f"{f.id}:{key}")),
                                                     "The catalogue's UUID, as stated in the catalogue."),
            "IssueDate": V(f.date(0), "Its issue date."), "IssueTime": V("09:00:00", "And time."),
            "RevisionDate": V(f.date(31), "Revised by the specification update."),
            "RevisionTime": V("14:00:00", "At that time."),
            "Note": V("Spring catalogue 2026.", "Which catalogue."),
            "Description": V("Benches and spare parts for resale.", "What it holds."),
            "VersionID": V(version, "The version referred to."),
            "PreviousVersionID": V("0.9", "The draft the store saw at the fair.")}


def related(iid, q, why):
    it = ITEM[iid]
    return {"ID": V(it["sellers_id"], f"The related item: {it['name']}."), "Quantity": qty(q, it["unit"], why),
            "Description": V(it["name"], "In words.")}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    lines = out["CatalogueLine"]
    bench, frame = lines[0], lines[1]
    common = {"ActionCode": V("Add", "The line is new in this catalogue."),
              "LifeCycleStatusCode": V("Active", "The item is sold now."),
              "OrderableIndicator": V("true", "It can be ordered."),
              "SellerSupplierParty": {"Party": party("6-xb", short=True)},
              "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
              "LineValidityPeriod": {"StartDate": V(f.date(0), "From the issue."),
                                     "EndDate": V(f.date(90), "With the catalogue.")}}
    kit.deep_merge(bench, {**common,
                           "Note": V("Pallets of four only.", "How it is sold."),
                           "OrderableUnit": V("Pallet of 4", "The unit the store orders in."),
                           "ContentUnitQuantity": qty(4, "H87", "Four benches in an orderable unit."),
                           "OrderQuantityIncrementNumeric": V("4", "Orders go up in steps of four."),
                           "MinimumOrderQuantity": qty(4, "H87", "One pallet."),
                           "MaximumOrderQuantity": qty(192, "H87", "Two containers."),
                           "WarrantyInformation": V("Five years on the frame, from the maker.", "The warranty."),
                           "PackLevelCode": V("Pallet", "The pack level the line is for."),
                           "WarrantyParty": party("5-xu", short=True),
                           "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
                           "ItemComparison": {"PriceAmount": price("520.00", "XBL", "The price per bench."),
                                              "Quantity": qty(1, "H87", "For comparing per bench.")},
                           "ComponentRelatedItem": [related("slat-1800", 5, "Five slats per bench."),
                                                    related("bench-casting", 2, "Two side frames per bench.")],
                           "AccessoryRelatedItem": {"ID": V("VI-ANCHOR-4", "The ground anchor set."),
                                                    "Quantity": qty(1, "SET", "Supplied with each bench."),
                                                    "Description": V("Four ground anchors and bolts.", "In words.")},
                           "ComplementaryRelatedItem": related("garden-set-r", 1, "The store's garden set sells "
                                                                                  "alongside."),
                           "DocumentReference": {"ID": V("VI-DS-B180", "The maker's datasheet.")},
                           "KeywordItemProperty": {"Name": V("Keyword", "A search word of the catalogue."),
                                                   "Value": V("park bench", "The word.")}})
    kit.deep_merge(frame, {**common,
                           "Note": V("Spare part for the Serra 180.", "What it is for."),
                           "OrderableUnit": V("Box", "One frame per box."),
                           "MinimumOrderQuantity": qty(1, "H87", "Any quantity."),
                           "RequiredRelatedItem": related("bench-serra-b", 1, "Fits only the Serra 180."),
                           "ReplacementRelatedItem": {"ID": V("VI-C180-2026", "The 2026 casting replaces it from "
                                                                              "May."),
                                                      "Quantity": qty(1, "H87", "One for one.")},
                           "ReplacedRelatedItem": {"ID": V("VI-C180-2024", "The casting this one replaced."),
                                                   "Quantity": qty(1, "H87", "One for one.")}})
    return {"ActionCode": V("Add", "A new catalogue."),
            "RevisionDate": V(f.date(0), "Not revised yet: the issue date."),
            "RevisionTime": V("09:00:00", "The issue time."),
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
            "RequestedCatalogueReference": {"ID": V("LD-CAT-SPRING-26", "The catalogue as announced at the fair.")},
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement.")},
            "TradingTerms": {"Information": V("Delivered duty paid to the store.", "The terms the store expects.")},
            "DocumentReference": {"ID": V("BM-RANGE-26", "The store's range plan.")},
            "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V("XB", "For the store in Bayvarra.")}},
            "RequestedLanguage": {"ID": V("en", "English."), "Name": V("English", "In words."),
                                  "LocaleCode": V("EN", "The locale, as an ISO 639 code of UBL's language code list.")},
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
                 "RequiredItemLocationQuantity": {"MinimumQuantity": qty(24, "H87", "The store's first order.")},
                 "Item": {"Name": V("Park bench Serra 180", "The item asked for.")}},
                {"ID": V("2", "Spare frames."),
                 "Item": {"Name": V("Bench side frame casting", "The item asked for.")}}]}


def catalogue_update_head(f, name, version):
    return {"Name": V(name, "What the update is."),
            "RevisionDate": V(f.date(30), "The day of the change."),
            "RevisionTime": V("14:00:00", "At that time."),
            "Note": V("Applies to the spring catalogue.", "Which catalogue."),
            "Description": V(name, "In words."),
            "VersionID": V(version, "The catalogue version after the update."),
            "LineCountNumeric": V("1", "One line."),
            "ValidityPeriod": {"StartDate": V(f.date(30), "From the change."),
                               "EndDate": V(f.date(90), "Until the catalogue ends.")},
            "ReferencedContract": {"ID": V("LD-BM-SUPPLY-2026", "The supply agreement.")},
            "Signature": {"ID": V(f"LD-SIG-26-{version}", "The distributor's seal."),
                          "SignatoryParty": party("6-xb", short=True)},
            "ContractorCustomerParty": {"Party": party("26-xb", short=True)},
            "TradingTerms": {"Information": V("Unchanged.", "The terms stay as in the catalogue.")},
            "DefaultLanguage": {"ID": V("en", "English."), "Name": V("English", "In words.")},
            "RelatedCatalogueReference": catalogue_ref(f, "The catalogue updated.")}


@enrich("retail", "CataloguePricingUpdate")
def _(f, n, doc, out):
    return {**catalogue_update_head(f, "Price change of the side frame", "1.1"),
            "CataloguePricingUpdateLine": {"ContractorCustomerParty": {"Party": party("26-xb", short=True)},
                                           "SellerSupplierParty": {"Party": party("6-xb", short=True)}}}


@enrich("retail", "CatalogueItemSpecificationUpdate")
def _(f, n, doc, out):
    return {**catalogue_update_head(f, "New slat wood for the Serra 180", "1.2"),
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
            "OriginalDocumentReference": {"ID": V("BM-PROMO-PLAN-26", "The store's promotion plan.")},
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
                                                    "ForecastPurposeCode": V("Sales", "Planned extra sales."),
                                                    "ForecastTypeCode": V("Total", "In total."),
                                                    "Period": {"StartDate": V(f.date(21), "The promotion."),
                                                               "EndDate": V(f.date(34), "Its end.")}},
                            "SupplyItem": bench}}}},
            "MiscellaneousEvent": {"MiscellaneousEventTypeCode": V("StoreOpening", "Late opening on the first "
                                                                                   "Saturday."),
                                   "EventLineItem": {"LineNumberNumeric": V("1", "The line."),
                                                     "SupplyItem": bench}}}


@enrich("retail", "InventoryReport")
def _(f, n, doc, out):
    return {"Note": V("Counted on Sunday evening.", "When."),
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
                                    "AvailabilityStatusCode": V("Available", "On the shelf."),
                                    "InventoryLocation": {"Name": V("Garden department, ground floor",
                                                                    "Where they stand.")}}}


FLOWS = {"ore": ORE, "road": ROAD, "rail": RAIL, "plastics": PLASTICS, "retail": RETAIL, "sea": SEA, "air": AIR,
         "cotton": COTTON, "tender": TENDER, "carnet": CARNET, "waste": WASTE, "utilities": UTILITIES, "wood": WOOD,
         "furniture": FURNITURE, "packaging": PACKAGING}
SCENARIOS = {k: _with_enrichment(k, v) for k, v in SCENARIOS.items()}


def seal(pid, no, why="The sender's electronic seal."):
    return {"ID": V(no, why), "SignatoryParty": party(pid, short=True)}


SETS_ITEM = {"Name": V("Garden bench set Marrow", "The store's own line."),
             "SellersItemIdentification": {"ID": V("BF-GS-01", "The maker's number.")}}


@enrich("furniture", "ItemInformationRequest")
def _(f, n, doc, out):
    return {"Note": V("Weekly figures, please, for the whole season.", "What the maker asks."),
            "DocumentReference": {"ID": V(f.numbers["quotation"], "The quotation of the line.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0312"),
            "ItemInformationRequestLine": {"TimeFrequencyCode": V("Weekly", "Figures per week."),
                                           "SupplyChainActivityTypeCode": V("Sales", "Sales to consumers."),
                                           "ForecastTypeCode": V("Total", "Total quantities."),
                                           "PerformanceMetricTypeCode": V("SalesUnits", "Measured in sets sold.")}}


@enrich("furniture", "TradeItemLocationProfile")
def _(f, n, doc, out):
    return {"Note": V("The store holds stock; the maker replenishes.", "Who does what."),
            "ProfileStatusCode": V("Active", "In force."),
            "DocumentReference": {"ID": V(f.numbers["quotation"], "The quotation the line is bought under.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0314"),
            "ItemManagementProfile": {
                "FrozenPeriodDaysNumeric": V("7", "Orders for the coming week no longer change."),
                "MinimumInventoryQuantity": qty(4, "SET", "Never fewer than four sets in the shop."),
                "MultipleOrderQuantity": qty(2, "SET", "Ordered in multiples of two: one van row."),
                "OrderIntervalDaysNumeric": V("14", "An order every two weeks."),
                "ReplenishmentOwnerDescription": V("The store orders; the maker proposes.", "Who replenishes."),
                "TargetServicePercent": V("95", "Sets on the shelf on 95 % of the days."),
                "TargetInventoryQuantity": qty(10, "SET", "The stock the store aims at."),
                "ItemLocationQuantity": {"LeadTimeMeasure": V("5", "Five days from order to shelf.", unitCode="DAY"),
                                         "MinimumQuantity": qty(2, "SET", "The smallest order.")}}}


@enrich("furniture", "ExceptionCriteria")
def _(f, n, doc, out):
    return {"Note": V("Both sides are told when a criterion is met.", "How the criteria are used."),
            "VersionID": V("1", "The first version."),
            "DocumentReference": {"ID": V(f.numbers["location-profile"], "The replenishment policy they go "
                                                                         "with.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0314C"),
            "ExceptionCriteriaLine": [
                {**out["ExceptionCriteriaLine"],
                 "Note": V("Slow sales.", "What the criterion catches."),
                 "ExceptionStatusCode": V("Active", "In force."),
                 "CollaborationPriorityCode": V("High", "Answered within two days."),
                 "ExceptionResolutionCode": V("Review", "The partners review the line together."),
                 "SupplyChainActivityTypeCode": V("Sales", "Measured on sales."),
                 "PerformanceMetricTypeCode": V("SalesUnits", "In sets."),
                 "EffectivePeriod": {"StartDate": V(f.date(21), "From the first four weeks on the shelf."),
                                     "EndDate": V(f.date(180), "To the end of the season.")}},
                {"ID": V("2", "The forecast criterion."),
                 "Note": V("Forecast far from the store's own plan.", "What it catches."),
                 "ThresholdValueComparisonCode": V("GreaterThan", "When the difference is larger."),
                 "ThresholdQuantity": qty(30, "P1", "More than 30 % difference."),
                 "SupplyItem": SETS_ITEM,
                 "ForecastExceptionCriterionLine": {"ForecastPurposeCode": V("Sales", "A sales forecast."),
                                                    "ForecastTypeCode": V("Total", "In total."),
                                                    "ComparisonDataSourceCode": V("Buyer", "Compared with the "
                                                                                           "store's plan."),
                                                    "DataSourceCode": V("Seller", "The maker's forecast."),
                                                    "TimeDeltaDaysQuantity": qty(28, "DAY", "Over four weeks.")}}]}


@enrich("furniture", "ProductActivity")
def _(f, n, doc, out):
    return {"Note": V("Sales were slow after the promotion ended.", "The store's remark."),
            "DocumentCurrencyCode": kit.currency_line("XBL", "the store's currency"),
            "DocumentReference": {"ID": V(f.numbers["info-request"], "The request the figures answer.")},
            "Signature": seal(doc["from"], "BM-SIG-26-0420A"),
            "SupplyChainActivityDataLine": {
                "BuyerCustomerParty": {"Party": party("26-xb", short=True)},
                "SellerSupplierParty": {"Party": party("37-xb", short=True)},
                "ActivityPeriod": {"StartDate": V(f.date(21), "The four weeks."), "EndDate": V(f.date(49), "Their "
                                                                                                          "end.")},
                "ActivityFinalLocation": {"Name": V("Customers' gardens in Lumeport", "Where the sets end up.")},
                "SalesItem": {"ActivityProperty": {"Name": V("Weather", "What the store notes."),
                                                   "Value": V("Rain three weeks out of four.", "Why sales were "
                                                                                               "slow.")},
                              "TaxExclusivePrice": {"PriceAmount": price("899.00", "XBL", "The shelf price, "
                                                                                          "before sales tax.")},
                              "TaxInclusivePrice": {"PriceAmount": price("957.44", "XBL", "With Coastal State's "
                                                                                          "6.5 % sales tax.")}}}}


@enrich("furniture", "ExceptionNotification")
def _(f, n, doc, out):
    return {"Note": V("Please review the line with us.", "What the maker proposes."),
            "DocumentReference": {"ID": V(f.numbers["exception-criteria"], "The criteria that were met.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0421"),
            "ExceptionNotificationLine": {
                "Note": V("Three sets sold against five expected.", "The exception."),
                "Description": V("Sales below the agreed threshold.", "In words."),
                "ExceptionStatusCode": V("Open", "Not yet resolved."),
                "CollaborationPriorityCode": V("High", "As agreed."),
                "ResolutionCode": V("Review", "A review of the line."),
                "VarianceQuantity": qty(-2, "SET", "Two sets fewer than the threshold."),
                "SupplyChainActivityTypeCode": V("Sales", "Measured on sales."),
                "PerformanceMetricTypeCode": V("SalesUnits", "In sets."),
                "DocumentReference": {"ID": V(f.numbers["activity"], "The product activity reported.")},
                "ForecastException": {"ForecastPurposeCode": V("Sales", "The sales forecast compared."),
                                      "ForecastTypeCode": V("Total", "In total."),
                                      "IssueDate": V(f.date(14), "The forecast of the first delivery."),
                                      "IssueTime": V("10:00:00", "Its time."),
                                      "DataSourceCode": V("Seller", "The maker's forecast."),
                                      "ComparisonDataCode": V("Actual", "Compared with actual sales."),
                                      "ComparisonForecastIssueDate": V(f.date(49), "The figures of day 49."),
                                      "ComparisonForecastIssueTime": V("18:00:00", "Their time.")}}}


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
            "RevisionStatusCode": V("Revised", "A revised forecast."),
            "PurposeCode": V("Order", "Of what the mill will order."),
            "OriginalDocumentReference": {"ID": V(f.numbers["forecast"], "The forecast revised.")},
            "Signature": seal(doc["from"], "LT-SIG-26-0222"),
            "ForecastRevisionLine": {"Note": V("Twenty per cent more.", "The change."),
                                     "Description": V("More bales from the second half of the season.", "In words."),
                                     "AdjustmentReasonCode": V("Demand", "Higher demand."),
                                     "ForecastPeriod": {"StartDate": V(f.date(60), "From mid-season."),
                                                        "EndDate": V(f.date(120), "To the end.")}}}


@enrich("furniture", "InstructionForReturns")
def _(f, n, doc, out):
    return {"Note": V("The maker takes back six sets to free the store's shelf.", "Why."),
            "DocumentReference": {"ID": V(f.numbers["exception"], "The exception that led to the return.")},
            "Signature": seal(doc["from"], "BF-SIG-26-0427"),
            "Shipment": {"ID": V("BM-RET-26-0427", "The return shipment."),
                         "GrossWeightMeasure": qty(282, "KGM", "Six sets of 47 kg."),
                         "Delivery": {"RequestedDeliveryPeriod": {"StartDate": V(f.date(58), "The store's van "
                                                                                             "brings them."),
                                                                  "EndDate": V(f.date(61), "Within the week.")}}},
            "InstructionForReturnsLine": {"Note": V("In their original cartons.", "How they are to be returned."),
                                          "ManufacturerParty": party("37-xb", short=True)}}


@enrich("furniture", "ExceptionNotification")
def _(f, n, doc, out):
    return {"ExceptionNotificationLine": {"ExceptionObservationPeriod": {"StartDate": V(f.date(21), "The four "
                                                                                                  "weeks."),
                                                                         "EndDate": V(f.date(49), "Their end.")}}}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    return {"CatalogueLine": [{**out["CatalogueLine"][0], "ContractSubdivision": V("Garden", "The part of the supply "
                                                                                             "agreement the line "
                                                                                             "falls under.")},
                              out["CatalogueLine"][1]]}


def status_extras(f, n, doc, out):
    """What every transportation status report adds: what it is, the plan it reports on, where and when."""
    x = {"Name": V("Transportation status", "The kind of report."),
         "Description": V(out["TransportEvent"]["Description"].value if isinstance(out.get("TransportEvent"), dict)
                          and "Description" in out["TransportEvent"] else "Status of the consignment.", "In words."),
         "Note": V("Automatic report from the sender's tracking system.", "How it was made."),
         "ShippingOrderID": V(f.numbers.get("consignment", ""), "The shipper's booking it reports on."),
         "OtherInstruction": V("Reply only if the delivery slot must change.", "What the receiver should do."),
         "TransportExecutionStatusCode": V("InProgress", "The carriage is under way."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TS-{n:02d}"),
         "StatusLocation": {"Name": V(PARTY[doc["from"]]["identity"]["name"], "Where the status was recorded.")},
         "StatusPeriod": {"StartDate": V(out["IssueDate"].value, "The status holds from the report."),
                          "EndDate": V(out["IssueDate"].value, "Until the next report.")},
         "DocumentReference": {"ID": V(f.numbers.get("waybill", f.numbers.get("bl", f.numbers.get("consignment"))),
                                       "The transport document of the consignment.")}}
    if "tep" in f.numbers:
        x["TransportExecutionPlanDocumentReference"] = {"ID": V(f.numbers["tep"], "The plan the carriage follows.")}
    if "ts-request" in f.numbers:
        x["TransportationStatusRequestDocumentReference"] = {"ID": V(f.numbers["ts-request"], "The request "
                                                                                              "answered.")}
    if f.id == "road":
        x["UpdatedDeliveryTransportEvent"] = kit.event(f, 9, "09:30:00", "The delivery as now expected.")
        x["UpdatedPickupTransportEvent"] = kit.event(f, 7, "15:05:00", "The collection as it happened.")
    return x


for _fid in ("road", "rail", "sea", "air"):
    enrich(_fid, "TransportationStatus")(status_extras)


@enrich("retail", "TransportationStatusRequest")
def _(f, n, doc, out):
    return {"CarrierAssignedID": V(f.numbers.get("waybill", ""), "The carrier's consignment note."),
            "Name": V("Status request", "What it is."),
            "Description": V("When will the benches arrive?", "The question."),
            "Note": V("The promotion starts soon.", "Why the store asks."),
            "ShippingOrderID": V(f.numbers["consignment"], "The booking asked about."),
            "OtherInstruction": V("Answer with the expected delivery time.", "What the answer should hold."),
            "TransportationStatusTypeCode": V("Delivery", "The status of the delivery is asked."),
            "DocumentReference": {"ID": V(f.numbers["order"], "The store's order.")},
            "Signature": seal(doc["from"], "LD-SIG-26-TSR"),
            "RequestedStatusLocation": {"Name": V("Brightmarket Stores, goods-in", "Status at the store.")},
            "RequestedStatusPeriod": {"StartDate": V(f.date(9), "For today."), "EndDate": V(f.date(10), "And "
                                                                                                       "tomorrow.")}}


@enrich("rail", "TransportProgressStatusRequest")
def _(f, n, doc, out):
    return {"Note": V("Has the container train left?", "The question."),
            "Signature": seal(doc["from"], "FRC-SIG-TPSR"),
            "StatusLocation": {"Name": V("Ferrano Intermodal Hub", "Where the status is asked for.")}}


@enrich("rail", "TransportProgressStatus")
def _(f, n, doc, out):
    return {"Note": V("Left on time.", "The answer."),
            "StatusAvailableIndicator": V("true", "A status is available."),
            "Signature": seal(doc["from"], "FIH-SIG-TPS"),
            "SourceIssuerParty": party("18-xu", short=True),
            "TransportProgressStatusRequestDocumentReference": {"ID": V(f.numbers["tps-request"], "The request "
                                                                                                  "answered.")},
            "TransportSchedule": {"SequenceNumeric": V("1", "The first stop: the hub."),
                                  "ReferenceDate": V(f.date(8), "The day."), "ReferenceTime": V("06:45:00", "The "
                                                                                                           "time."),
                                  "ReliabilityPercent": V("95", "How sure the schedule is."),
                                  "Remarks": V("On time.", "The status."),
                                  "StatusLocation": {"Name": V("Ferrano Intermodal Hub", "The stop.")},
                                  "PlannedDepartureTransportEvent": kit.event(f, 8, "06:45:00", "The timetable."),
                                  "ActualDepartureTransportEvent": kit.event(f, 8, "06:52:00", "The departure."),
                                  "EstimatedArrivalTransportEvent": kit.event(f, 9, "10:40:00", "Expected in "
                                                                                                "Marrowdale."),
                                  "PlannedArrivalTransportEvent": kit.event(f, 9, "10:30:00", "The timetable."),
                                  "EstimatedDepartureTransportEvent": kit.event(f, 8, "06:50:00", "As expected "
                                                                                                  "that morning."),
                                  "ActualArrivalTransportEvent": kit.event(f, 8, "05:30:00", "The train arrived "
                                                                                             "at the hub for "
                                                                                             "loading.")}}


@enrich("rail", "GoodsItemItinerary")
def _(f, n, doc, out):
    return {"Note": V("The itinerary of the two containers.", "What it shows."),
            "Signature": seal(doc["from"], "FRC-SIG-GII"),
            "ReferencedConsignment": {"ID": V(f.numbers["consignment"], "The consignment.")},
            "ReferencedTransportEquipment": {"ID": V(RAIL_BOXES[0], "The first container.", schemeID="ISO6346")},
            "ReferencedPackage": {"ID": V("CL-26-001", "The first pallet in it.")},
            "ReferencedGoodsItem": {"ID": V("1", "The benches.")}}


@enrich("sea", "TransportServiceDescriptionRequest")
def _(f, n, doc, out):
    return {"Note": V("Weekly sailings to Selanu, please.", "What the distributor asks."),
            "ServiceInformationPreferenceCode": V("Schedule", "It wants the schedule first."),
            "Signature": seal(doc["from"], "LD-SIG-TSDR"),
            "TransportServiceProviderParty": party("11-xb", short=True)}


@enrich("sea", "TransportServiceDescription")
def _(f, n, doc, out):
    return {"Note": V("Our island service.", "What follows."), "ServiceName": V("Island feeder", "The service's "
                                                                                                "name."),
            "ResponseCode": V("Offered", "The service is offered."),
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
         "DocumentStatusCode": V("NoStatus", "New instructions."),
         "ShippingOrderID": V(f.numbers.get("shipment", ""), "The shipment to be booked."),
         "ToOrderIndicator": V("true" if f.id == "sea" else "false", "A bill of lading to order, so the buyer can "
                                                                     "transfer it." if f.id == "sea" else
                               "A straight bill: the consignee is named."),
         "AdValoremIndicator": V("false", "No value declared for the carriage."),
         "OtherInstruction": V("Send the bill of lading to the forwarder.", "Where the documents go."),
         "DocumentReference": {"ID": V(f.numbers.get("order", ""), "The order the goods are for.")},
         "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The freight's currency."),
                          "TargetCurrencyCode": V("XLC", "The island's currency."),
                          "CalculationRate": V("0.4", "The reference rate.")},
         "DocumentDistribution": {"ID": V("1", "A copy."), "DocumentTypeCode": V("Copy", "A copy."),
                                  "DistributionTypeCode": V("Electronic", "As this UBL document."),
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
            "DeclaredCarriageValueAmount": amount(0, "XBL", "No value declared."),
            "DocumentReference": {"ID": V(f.numbers.get("instructions-carrier", f.numbers.get("instructions", "")),
                                          "The forwarding instructions it was issued on.")},
            "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The freight's currency."),
                             "TargetCurrencyCode": V("XLC", "The island's currency."),
                             "CalculationRate": V("0.4", "The reference rate.")},
            "DocumentDistribution": {"ID": V("1", "Three originals."), "DocumentTypeCode": V("Original", "Originals."),
                                     "DistributionTypeCode": V("Paper", "On paper, by courier."),
                                     "Party": party(doc["to"], short=True)},
            "Signature": seal(doc["from"], f"TWL-SIG-BL-{f.id}", "The master's signature, by the carrier's agent.")}


for _fid in ("sea", "cotton"):
    enrich(_fid, "BillOfLading")(bl_extras)


@enrich("sea", "Manifest")
def _(f, n, doc, out):
    return {"ManifestType": V("Cargo manifest", "In words."), "Description": V("Cargo for Selanu.", "What it "
                                                                                                     "lists."),
            "Note": V("One container for Selanu.", "The cargo."), "VersionID": V("1", "The first version."),
            "DeclaredCarriageValueAmount": amount(0, "XBL", "No value declared."),
            "PassengerPerson": kit.person("Ines", "Tavari", "The one passenger: a supercargo travelling with the "
                                                            "cargo.", role="Passenger"),
            "DocumentReference": {"ID": V(f.numbers["bl"], "The bill of lading of the container.")},
            "DocumentDistribution": {"ID": V("1", "To customs."), "DistributionTypeCode": V("Electronic", "By "
                                                                                                          "message."),
                                     "Party": party("19-xl", short=True)},
            "Signature": seal(doc["from"], "TWL-SIG-MF", "The master's signature.")}


@enrich("sea", "PackingList")
def _(f, n, doc, out):
    return {"Name": V("Packing list", "What it is."), "Description": V("The container's contents.", "In words."),
            "Note": V("25 pallets.", "The count."), "VersionID": V("1", "The first version."),
            "OtherInstruction": V("Keep with the container's documents.", "Where it goes."),
            "CarrierParty": party("11-xb", short=True),
            "DocumentReference": {"ID": V(f.numbers["order"], "The buyer's order.")},
            "DocumentDistribution": {"ID": V("1", "To the forwarder."), "DistributionTypeCode": V("Electronic",
                                                                                                  "By message."),
                                     "Party": party("10-xb", short=True)},
            "Signature": seal(doc["from"], "LD-SIG-PL")}


@enrich("sea", "CommonTransportationReport")
def _(f, n, doc, out):
    return {"DocumentStatusCode": V("NoStatus", "A first report."),
            "ReportTypeCode": V("PreArrival", "The report before entering the port."),
            "ReportType": V("Pre-arrival report", "In words."),
            "Description": V("The ship's report before arrival at Selanu.", "What it is."),
            "Note": V("No incidents on board.", "The master's note."), "VersionID": V("1", "The first version."),
            "ReportingLocation": {"Name": V("At sea, 40 nautical miles off Selanu", "Where the report was made.")},
            "TransportMeans": kit.means("11-xb", "TH", "TH-26-19E", "The voyage.", "Eastbound"),
            "DocumentReference": {"ID": V(f.numbers["manifest"], "The cargo manifest.")},
            "Signature": seal(doc["from"], "TWL-SIG-CTR", "The master's signature.")}


@enrich("cotton", "WeightStatement")
def _(f, n, doc, out):
    return {"WeightStatementTypeCode": V("VGM", "A statement of the verified gross mass."),
            "Signature": seal(doc["from"], "SCG-SIG-VGM", "The shipper's signature, as SOLAS requires."),
            "ResponsibleParty": party("39-xl", short=True)}


@enrich("retail", "ReceiptAdvice")
def _(f, n, doc, out):
    lines = out["ReceiptLine"] if isinstance(out["ReceiptLine"], list) else [out["ReceiptLine"]]
    lines[0].update({"ReceivedTime": V("10:40:00", "Forty minutes after the slot began."),
                     "TimingComplaintCode": V("Late", "The truck was late for its slot."),
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
    lines[0].update({"OutstandingQuantity": qty(TENDER_QTY - 40, "H87", "Still to come under the contract."),
                     "OutstandingReason": V("Later releases under the framework contract.", "Why."),
                     **kit.cost_centre("2-xb", "The department's programme."),
                     "DocumentReference": {"ID": V(FOLDER, "The contract.")}})
    return {"ProjectReference": {"ID": V("PWD-PARKS-26", "The parks renewal programme.")},
            **kit.cost_centre("2-xb", "The department's cost centre."),
            "Signature": seal(doc["from"], "CL-SIG-26-DA")}


@enrich("cotton", "DeliveryNote")
def _(f, n, doc, out):
    return {"DocumentStatusCode": V("NoStatus", "A first delivery note."),
            "Note": V("Three trailer loads, weighed at the gin.", "What was delivered."),
            **kit.cost_centre("39-xl", "The gin's cost centre for seed cotton."),
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
    x = {"ExportTypeCode": V("Permanent", "A permanent export: the goods are sold abroad."),
         "ExportReasonCode": V("Sale", "The reason: a sale to a buyer abroad."),
         "Note": V("Declared electronically before the goods leave.", "How it was declared."),
         "VersionID": V("1", "The first version."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-EX-{f.id}"),
         "CustomsDeclaration": {
             "FunctionCode": V("Original", "An original declaration, not an amendment."),
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
    x = {"TypeCode": V("Import", "An import declaration."),
         "SubTypeCode": V("FreeCirculation", "For release into free circulation."),
         "NatureOfTransactionCode": V("Purchase", "The goods were bought."),
         "Note": V("Duties paid by the importer's account at customs.", "How duties are settled."),
         "VersionID": V("1", "The first version."),
         "ValidityPeriod": {"StartDate": V(out["IssueDate"].value, "From the declaration."),
                            "DurationMeasure": V("30", "Valid for clearance within 30 days.", unitCode="DAY")},
         "CustomsExitOfficeLocation": exit_office(f, origin),
         "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V(c, "The customs territory of import.")}},
         "NotifierParty": party(doc["from"], short=True),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-IM-{f.id}")}
    if "export-declaration" in f.numbers:
        x["PreviousCustomsDeclaration"] = {"ID": V(f.numbers["export-declaration"], "The export declaration in the "
                                                                                     "country of departure.")}
    return x


for _fid in ("road", "sea", "tender", "plastics", "wood", "cotton"):
    enrich(_fid, "ExportCustomsDeclaration")(export_extras)
    enrich(_fid, "ImportCustomsDeclaration")(import_extras)


@enrich("rail", "TransitCustomsDeclaration")
def _(f, n, doc, out):
    return {"TypeCode": V("Transit", "A transit declaration."),
            "SubTypeCode": V("External", "Goods not yet released, carried across the border under customs control."),
            "NatureOfTransactionCode": V("Purchase", "The goods were bought."),
            "Note": V("Seals XU-VI-30411 and XU-VI-30412 to remain intact.", "The transit condition."),
            "VersionID": V("1", "The first version."),
            "ValidityPeriod": {"StartDate": V(f.date(8), "From departure."),
                               "EndDate": V(f.date(11), "The goods must reach the office of destination within "
                                                        "three days.")},
            "ExportCustomsExitOfficeLocation": {"Name": V("Customs post at the rail border station, Urvanian side",
                                                          "Where the goods leave Urvania.")},
            "TransitCustomsExitOfficeLocation": {"Name": V("Customs post at the rail border station, Bayvarran side",
                                                           "Where the transit is checked.")},
            "ImportCustomsExitOfficeLocation": {"Name": V("Customs office Marrowdale", "Where the transit ends.")},
            "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V("XU", "Declared under Urvania's "
                                                                                    "customs.")}},
            "FreightForwarderParty": party("14-xu", short=True),
            "NotifierParty": party("5-xu", short=True),
            "AdditionalDocumentReference": {"ID": V(f.numbers["tep"], "The transport plan.")},
            "Signature": seal(doc["from"], "VI-SIG-TD")}


@enrich("road", "CertificateOfOrigin")
def _(f, n, doc, out):
    x = {"Note": V("Preferential origin under the trade accord.", "What the certificate is for."),
         "VersionID": V("1", "The first version."),
         "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-CO-{n:02d}"),
         "CertificateOfOriginApplication": {
             "PreviousJobID": V("VI-CO-25-0412", "The exporter's application of last year for the same goods."),
             "Remarks": V("Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives "
                          "origin.", "Why the goods are of Urvanian origin."),
             "ExporterParty": party("5-xu", short=True),
             "ImporterParty": party("6-xb", short=True),
             "DocumentDistribution": {"ID": V("1", "The importer's copy."),
                                      "DistributionTypeCode": V("Electronic", "As this document."),
                                      "Party": party("6-xb", short=True)},
             "SupportingDocumentReference": {"ID": V(f.numbers["invoice"] if "invoice" in f.numbers else
                                                     f.numbers["order"], "The commercial document behind the "
                                                                         "goods.")},
             "Signature": seal("5-xu", "VI-SIG-COA")}}
    if doc["from"] == "20-xu":
        x["EmbassyEndorsement"] = {"DocumentID": V(out["ID"].value, "The certificate legalised."),
                                   "ApprovalStatus": V("Legalised", "The trade accord council confirms the "
                                                                    "chamber's signature."),
                                   "Remarks": V("Signature of the Ferrano chamber confirmed.", "What was checked."),
                                   "EndorserParty": {"RoleCode": V("Legalisation", "The council legalises."),
                                                     "SequenceNumeric": V("2", "After the chamber."),
                                                     "Party": party("32-xb", short=True),
                                                     "SignatoryContact": {"Name": V("Legalisation desk", "The "
                                                                                    "council's desk that signs.")}},
                                   "Signature": seal("32-xb", "LTAC-SIG-26-0311")}
        x["IssuerEndorsement"] = {"Remarks": V("Origin verified against the exporter's production records.",
                                               "What the chamber checked."),
                                  "Signature": seal("20-xu", "FCC-SIG-26-0309")}
    return x


@enrich("cotton", "GoodsCertificate")
def _(f, n, doc, out):
    return {"TypeCode": V("Phytosanitary", "A plant health certificate for the cotton."),
            "Description": V("The ginned cotton is free of the pests named by Bayvarra's plant health rules.",
                             "What it certifies."),
            "Note": V("Inspected at the ginnery's warehouse.", "Where."), "VersionID": V("1", "The first version."),
            "ValidityPeriod": {"StartDate": V(f.date(26), "From the inspection."),
                               "EndDate": V(f.date(40), "For two weeks: the bales must ship by then.")},
            "ApplicableTerritoryAddress": {"Country": {"IdentificationCode": V("XB", "For import into Bayvarra.")}},
            "WarehouseParty": party("39-xl", short=True),
            "ConsignorParty": party("39-xl", short=True),
            "ConsigneeParty": party("40-xb", short=True),
            "FreightForwarderParty": party("10-xb", short=True),
            "LegalAuthorityParty": party("19-xl", short=True),
            "Attestation": {"ID": V("SCC-ATT-26-0042", "The inspector's attestation."),
                            "Name": V("Freedom from pests", "What is attested."),
                            "Description": V("Sampled and found free of boll weevil and pink bollworm.", "In words."),
                            "Note": V("10 bales sampled out of 80.", "The sample."),
                            "AcceptanceIndicator": V("true", "Accepted."),
                            "ValidityPeriod": {"EndDate": V(f.date(40), "As the certificate.")},
                            "IssuerParty": party("20-xl", short=True),
                            "AttestationLine": {"ID": V("1", "The pest checked."), "TypeCode": V("Pest", "A pest "
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
                                "TypeCode": V("Ginning", "The cotton was ginned."),
                                "Description": V("Ginned, cleaned and pressed into bales.", "In words."),
                                "Note": V("At the Selanu cotton ginnery.", "Where."),
                                "Period": {"StartDate": V(f.date(5), "The ginning."), "EndDate": V(f.date(20), "Its "
                                                                                                             "end.")},
                                "ProcessingParty": party("39-xl", short=True),
                                "CriterionItem": {"CriterionDescription": V("Seed removed; lint only.", "What "
                                                                            "processing the rule requires."),
                                                  "DeclaredPropertyItem": {"Name": V("Cotton lint", "The goods.")}},
                                "SubGoodsProcessing": {"TypeCode": V("Pressing", "Pressed into bales."),
                                                       "Description": V("Bales of about 227 kg.", "In words.")}},
            "OriginalDocumentReference": {"ID": V("XL-CLS-2026-0042", "The classing certificate of the cotton.")},
            "PreviousDocumentReference": {"ID": V("SCC-PH-25-0198", "Last season's certificate.")},
            "AdditionalDocumentReference": {"ID": V(f.numbers["order"], "The mill's order.")},
            "Signature": seal(doc["from"], "SCC-SIG-26-PH")}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    cf = lambda cid, why, ref, ref_why, office: {
        "ID": V(cid, why), "GoodsItemPassportID": V(out["ID"].value, "The carnet."),
        "Note": V("Stamped by customs.", "How it is used."),
        "CustomsOfficeLocation": {"Name": V(office, "The customs office that stamps it.")},
        "GoodsItem": {"ID": V("1", "The two sample benches."), "Quantity": qty(2, "H87", "Two.")},
        ref: {"ID": V(f"{cid}-STAMP", ref_why)},
        "VoucherDocumentReference": {"ID": V(f"V-{cid}", "The voucher that customs keeps.")}}
    return {"StatusCode": V("Valid", "The carnet is valid."), "Status": V("Issued", "In words."),
            "Note": V("Samples for the Selanu trade fair; to come back within six months.", "What it is for."),
            "VersionID": V("1", "The first version."),
            "ExportReasonCode": V("Exhibition", "Temporary export for a fair."),
            "ExportReason": V("Exhibition at the Selanu trade fair", "In words."),
            "IssuerEndorsement": {"DocumentID": V(out["ID"].value, "The carnet."),
                                  "ApprovalStatus": V("Issued", "The chamber issued it."),
                                  "EndorserParty": {"RoleCode": V("Issuer", "The issuing chamber."),
                                                    "SequenceNumeric": V("1", "The first endorsement."),
                                                    "Party": party("20-xu", short=True),
                                                    "SignatoryContact": {"Name": V("Carnet desk", "The chamber's "
                                                                                                 "desk.")}}},
            "AdditionalDocumentReference": {"ID": V("SCC-FAIR-26-INV", "The fair's invitation to exhibit.")},
            "DocumentDistribution": {"ID": V("1", "The holder's carnet."), "DistributionTypeCode": V("Paper",
                                                                                                    "On paper."),
                                     "Party": party("5-xu", short=True)},
            "Signature": seal("20-xu", "FCC-SIG-26-ATA"),
            "GoodsItemPassportCounterfoil": [
                {**cf("EXP-1", "The exportation counterfoil, stamped by Urvania's customs when the samples leave.",
                      "ExportationDocumentReference", "The export stamp.", "Customs post at the land border, Urvanian "
                                                                           "side"),
                 "FinalReexportationDate": V(f.date(180), "The samples must be back by then.")},
                cf("IMP-1", "The importation counterfoil, stamped by Lisavu's customs when they arrive.",
                   "ImportationDocumentReference", "The import stamp on the island.", "Customs office, Selanu "
                                                                                      "airport"),
                cf("REEXP-1", "The re-exportation counterfoil, to be stamped when they leave the island.",
                   "ReexportationDocumentReference", "The re-export stamp.", "Customs office, Selanu airport"),
                cf("REIMP-1", "The re-importation counterfoil, stamped when they come home.",
                   "ReimportationDocumentReference", "The re-import stamp.", "Customs post at the land border, "
                                                                             "Urvanian side")]}


@enrich("carnet", "ProofOfReexportationRequest")
def _(f, n, doc, out):
    return {"Note": V("The island's customs found no re-export stamp.", "Why the chamber asks."),
            "VersionID": V("1", "The first request."),
            "GoodsItemPassportCounterfoilID": V("IMP-1", "The importation counterfoil without a re-export."),
            "AdditionalDocumentReference": {"ID": V("XL-CUS-ATA-26-0071", "The customs' notice to the chamber.")},
            "Signature": seal(doc["from"], "SCC-SIG-26-PRQ")}


@enrich("carnet", "ProofOfReexportationReminder")
def _(f, n, doc, out):
    return {"Note": V("Without proof, the import duties will be claimed from the guarantee.", "What happens "
                                                                                             "otherwise."),
            "VersionID": V("1", "The first reminder."),
            "IssuerEndorsement": {"DocumentID": V(f.numbers["por-request"], "The request repeated."),
                                  "ApprovalStatus": V("Open", "Still unanswered."),
                                  "EndorserParty": {"RoleCode": V("Guarantor", "The importing guarantor."),
                                                    "SequenceNumeric": V("1", "The only one."),
                                                    "Party": party("20-xl", short=True),
                                                    "SignatoryContact": {"Name": V("Carnet desk", "The chamber's "
                                                                                                 "desk.")}}},
            "PaymentTerms": {"Note": V("Duties and import consumption tax of 1,300 coral fall due if no proof "
                                       "arrives within 30 days.", "The claim that would follow."),
                             "Amount": amount(Decimal("1300.000"), "XLC", "The duties at stake."),
                             "PaymentDueDate": V(f.date(120), "The day they fall due.")},
            "AdditionalDocumentReference": {"ID": V("XL-CUS-ATA-26-0071", "The customs' notice.")},
            "Signature": seal(doc["from"], "SCC-SIG-26-PRM")}


@enrich("carnet", "ProofOfReexportation")
def _(f, n, doc, out):
    return {"Note": V("The samples came home on the date stamped.", "The proof."),
            "VersionID": V("1", "The first version."),
            "GoodsItemPassportAttachment": {"ExternalReference": {
                "URI": V("https://www.ferrano-chamber.example/ata/carnet-scan.pdf", "A scan of the stamped "
                                                                                    "counterfoil."),
                "MimeCode": V("application/pdf", "A PDF.")}},
            "AdditionalDocumentReference": {"ID": V("XU-CUS-REIMP-26-0044", "Urvania's customs' re-import "
                                                                            "record.")},
            "Signature": seal(doc["from"], "FCC-SIG-26-POR")}


import base64 as _b64  # noqa: E402


def full_signature(pid, no, f, day, why):
    """A signature with everything UBL can say about it: method, validation and the signature value itself."""
    blob = _b64.b64encode(f"Signature value of {no}, shortened for the example world.".encode()).decode()
    return {"ID": V(no, why), "ReasonCode": V("Approval", "The signer approves the document."),
            "Note": V("Signed with the company's seal certificate.", "How."),
            "ValidationDate": V(f.date(day), "Checked on receipt."), "ValidationTime": V("09:05:00", "At that time."),
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
            "DocumentTypeCode": V("Terms", "The kind of document."),
            "DocumentDescription": V("The terms of the digital trade agreement.", "What it is."),
            "XPath": V("/DigitalAgreement/DigitalAgreementTerms", "The part of this document the reference "
                                                                  "explains."),
            "ReferencedDocumentInternalAddress": V("section-2", "The section of the referenced document meant."),
            "LanguageID": V("en", "In English."),
            "LocaleCode": V("EN", "The locale, as an ISO 639 code of UBL's language code list."),
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
                               "FormatCode": V("PDF/A-3", "An archivable PDF."),
                               "EncodingCode": V("Binary", "Not encoded."),
                               "CharacterSetCode": V("UTF-8", "The character set of its text."),
                               "FileName": V("terms-1.0.pdf", "The file's name."),
                               "Description": V("The full terms.", "What it holds.")}},
            "ValidityPeriod": {"StartDate": V(f.date(day), "In force from signing."),
                               "EndDate": V(f.date(day + 365), "For a year.")},
            "ResultOfVerification": {"ValidatorID": V("LTAC-VALIDATOR", "The council's validation service."),
                                     "ValidationResultCode": V("Valid", "The document's signature is valid."),
                                     "ValidationDate": V(f.date(day), "Checked."),
                                     "ValidationTime": V("12:05:00", "At that time."),
                                     "ValidateProcess": V("Signature and hash check", "What was checked."),
                                     "ValidateTool": V("Accord validator", "The tool."),
                                     "ValidateToolVersion": V("3.2", "Its version."),
                                     "SignatoryParty": party("32-xb", short=True)}}


def digital_service(pid, doc_type, sending):
    return {"ID": V(f"{kit.initials(pid)}-{doc_type}-{'OUT' if sending else 'IN'}", "The party's service for this "
                                                                                     "document."),
            "CustomizationID": V("urn:ubl-examples:world", "The customization the documents follow."),
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
                                                                  "EndpointURI": V(f"https://ap.{pid}.example/as4",
                                                                                   "The access point.")},
                                       "DigitalCertificate": {"ID": V(f"ACCORD-CERT-{pid}", "The access point's "
                                                                                            "certificate."),
                                                              "CertificateType": V("Access point", "Its kind.")}}}


@enrich("sea", "DigitalAgreement")
def _(f, n, doc, out):
    procs = out["DigitalProcess"]
    for p, (doc_type, send, recv) in zip(procs, (("Order", "1-xl", "6-xb"), ("Invoice", "6-xb", "1-xl"))):
        p["ProfileID"] = V(f"urn:ubl-examples:world:process:{p['ID'].value}", "The process profile.")
        p["DigitalCollaboration"] = {"ID": V(f"{p['ID'].value}-1", "The main exchange of the process."),
                                     "SendingDigitalService": digital_service(send, doc_type, True),
                                     "ReceivingDigitalService": digital_service(recv, doc_type, False)}
        p["CertificationDocumentReference"] = {"ID": V(f"ACCORD-CERT-PROC-{p['ID'].value}", "The council's "
                                                                                             "certification of "
                                                                                             "the process.")}
    return {"AgreementTypeCode": V("Bilateral", "An agreement between two parties."),
            "PreviousVersionID": V("0.9", "The draft both sides commented on."),
            "RequiredResponseMessageLevelCode": V("Business", "A business response is required for every "
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
                    "ID": V("LD-SLA-1", "The service level."), "ServiceTypeCode": V("Messaging", "For the "
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
            "BriefDescription": V("Distributor of street and garden furniture for Bayvarra and the islands.",
                                  "The business in a sentence."),
            "Signature": seal(doc["from"], "LD-SIG-26-BC"),
            "BrochureDocumentReference": {"ID": V("LD-BROCHURE-2026", "The distributor's brochure."),
                                          "Attachment": {"ExternalReference": {
                                              "URI": V("https://www.lumeway.example/brochure-2026.pdf", "Where it "
                                                                                                        "is."),
                                              "MimeCode": V("application/pdf", "A PDF.")}}},
            "AdditionalDocumentReference": {"ID": V("LD-REG-XB", "The distributor's registration extract.")},
            "BusinessCapability": {"ID": V("CAP-STOCK", "A capability."),
                                   "CapabilityTypeCode": V("Warehousing", "What it can do."),
                                   "Description": V("Stock of 2,000 benches in Marrowdale.", "In words."),
                                   "ValueAmount": amount(Decimal("1040000.00"), "XBL", "The stock's value."),
                                   "ValueQuantity": qty(2000, "H87", "Benches in stock."),
                                   "SuppliedEvidence": {"ID": V("LD-AUDIT-2025", "The evidence."),
                                                        "EvidenceTypeCode": V("Audit", "An audit report."),
                                                        "Name": V("Stock count 2025", "Its name."),
                                                        "Description": V("Year-end count by the auditor.", "What "
                                                                                                           "it is."),
                                                        "CandidateStatement": V("The stock is counted every year.",
                                                                                "The company's statement."),
                                                        "ConfidentialityLevelCode": V("Public", "May be shared."),
                                                        "EvidenceIssuingParty": party("6-xb", short=True),
                                                        "Language": {"ID": V("en", "English.")}},
                                   "ValidityPeriod": {"EndDate": V(f.date(240), "Until the next count.")},
                                   "WebSite": {"ID": V("WEB-1", "The stock page."), "Name": V("Stock", "Its name."),
                                               "Description": V("Live stock levels.", "What it shows."),
                                               "WebSiteTypeCode": V("Extranet", "For trade customers."),
                                               "URI": V("https://www.lumeway.example/stock", "Where."),
                                               "WebSiteAccess": {"URI": V("https://www.lumeway.example/login",
                                                                          "The login page."),
                                                                 "Login": V("velumi", "The buyer's login."),
                                                                 "Password": V("********", "Never shown.")}}}}


@enrich("sea", "InvoiceStatusRequest")
def _(f, n, doc, out):
    return {"RequestTime": V("10:00:00", "When asked."), "Note": V("Has the invoice been approved?", "The question."),
            "Signature": seal(doc["from"], "LD-SIG-26-ISR")}


@enrich("sea", "InvoiceStatusResponse")
def _(f, n, doc, out):
    return {"Note": V("Approved; the balance will be paid to the factor.", "The answer."),
            "VersionID": V("1", "The first answer."),
            "Signature": seal(doc["from"], "VT-SIG-26-ISP"),
            "Payment": {"ID": V("VT-PAY-26-0199", "The payment planned."),
                        "PaidAmount": amount(f.numbers["invoice-amount"], "XBL", "The balance to be paid."),
                        "PaidDate": V(f.date(52), "The planned payment day."),
                        "InstructionID": V("VT-PAY-26-0199", "The buyer's payment order."),
                        "ExchangeRate": {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                         "TargetCurrencyCode": V("XLC", "The buyer's."),
                                         "CalculationRate": V("0.4", "The reference rate.")},
                        "BillingReference": {"InvoiceDocumentReference": {"ID": V(f.numbers["invoice"], "The "
                                                                                                        "invoice.")}},
                        "RemittanceDocumentReference": {"ID": V("to follow", "The remittance advice will follow "
                                                                             "with the payment.")}}}


@enrich("road", "ApplicationResponse")
def _(f, n, doc, out):
    return {"ResponseDate": V(f.date(9), "The day the invoice was processed."),
            "ResponseTime": V("06:12:00", "Processed overnight."),
            "Note": V("Accepted for payment; line 2 matched the substituted casting.", "The result."),
            "VersionID": V("1", "The first response."),
            "Signature": seal(doc["from"], "LD-SIG-26-AR"),
            "DocumentResponse": {
                "Response": {"EffectiveDate": V(f.date(9), "Effective at once."),
                             "EffectiveTime": V("06:12:00", "When processed."),
                             "Status": {"ConditionCode": V("Matched", "The invoice matched order and receipt."),
                                        "Description": V("Three-way match passed.", "In words.")}},
                "IssuerParty": party(doc["from"], short=True),
                "RecipientParty": party(doc["to"], short=True),
                "LineResponse": {"LineReference": {"LineID": V("2", "The invoice line of the side frames.")},
                                 "Response": {"ReferenceID": V("2", "The line."),
                                              "ResponseCode": V("AP", "Accepted.", listID="UNCL4343"),
                                              "Description": V("Matched to the substituted 2026 casting.",
                                                               "Why it needed a look.")}}}}


@enrich("retail", "DocumentStatusRequest")
def _(f, n, doc, out):
    return {"Note": V("Has the order been accepted?", "The question."),
            "TrackingID": V(f.numbers["order"], "The order the store tracks."),
            "Signature": seal(doc["from"], "BM-SIG-26-DSR")}


@enrich("retail", "DocumentStatus")
def _(f, n, doc, out):
    return {"Note": V("Accepted and booked.", "The answer."),
            "Signature": seal(doc["from"], "LD-SIG-26-DS"),
            "AdditionalDocumentResponse": {"Response": {"ResponseCode": V("AP", "The transport booking is "
                                                                                "confirmed too.")},
                                           "DocumentReference": {"ID": V(f.numbers.get("tep-request", ""),
                                                                         "The transport booking.")}}}


def contact(name, why, tel_of=None, email=None):
    c = {"Name": V(name, why)}
    if tel_of:
        c["Telephone"] = V(PARTY[tel_of]["identity"]["contact"]["telephone"], "The number.")
    if email:
        c["ElectronicMail"] = V(email, "The address, under the reserved .example domain.")
    return c


@enrich("retail", "Order")
def _(f, n, doc, out):
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
                           "FinancingInstrumentCode": V("Factoring", "The receivable was sold to the factor."),
                           "ContractDocumentReference": {"ID": V("HF-FA-2026-007", "The factoring agreement.")},
                           "DocumentReference": {"ID": V("HF-ASSIGN-26-0091", "The notice of assignment.")},
                           "FinancingParty": party("24-xb", short=True),
                           "FinancingFinancialAccount": kit.account("24-xb", "The factor's account."),
                           "Clause": {"ID": V("HF-FA-7.2", "The clause on payment."),
                                      "Content": V("Payment to any other account does not discharge the buyer.",
                                                   "What it says.")}},
        "RemittanceDocumentDistribution": {"ID": V("1", "Where the remittance advice goes."),
                                           "DocumentTypeCode": V("RemittanceAdvice", "The document."),
                                           "DistributionTypeCode": V("Electronic", "By message."),
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
    return {"TransportContract": {"IssueTime": V("10:00:00", "Signed in the morning."),
                                  "NominationDate": V(f.date(2), "The slots of this train were nominated today."),
                                  "NominationTime": V("09:00:00", "At that time."),
                                  "ContractTypeCode": V("Framework", "A framework contract."),
                                  "Note": V("Call-off 88 of the year.", "Which call-off."),
                                  "VersionID": V("2", "The contract as amended in March."),
                                  "ModificationReasonCode": V("Volume", "Amended for higher volumes."),
                                  "ModificationReasonDescription": V("Ten more slots a month from April.", "The "
                                                                                                          "change."),
                                  "Description": V("Container slots between the Ferrano hub and Marrowdale.", "What "
                                                                                                            "it "
                                                                                                            "covers."),
                                  "ContractDocumentReference": {"ID": V("FRC-CON-2026-005-A1", "The amendment.")},
                                  "NominationPeriod": {"StartDate": V(f.date(0), "Slots are nominated a week"),
                                                       "EndDate": V(f.date(6), "before the train.")},
                                  "ContractualDelivery": {"LatestDeliveryDate": V(f.date(10), "The contract's latest "
                                                                                              "delivery for this "
                                                                                              "call-off.")}}}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    e = PARTY["5-xu"]["identity"]["employee"]
    return {"RepresentativeParty": {"Person": {
        "Title": V("Ing.", "The professional title, as on the travel documents."),
        "MiddleName": V("Ilse", "The middle name, as in the passport."),
        "OtherName": V("Mara", "The name the employee goes by."),
        "NameSuffix": V("Jr", "As in the passport."),
        "NationalityCode": V("XU", "Urvanian."),
        "BirthplaceLocation": {"Name": V(e["birthplace"], "The place of birth."),
                               "Address": {"Country": {"IdentificationCode": V("XU", "In Urvania.")}}},
        "Contact": contact("Mobile on the road", "How to reach the employee at the fair.", "5-xu"),
        "ResidenceAddress": {"CityName": V("Ferrano", "Where the employee lives."),
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
                         "RequestedDeliveryPeriod": {"StartDate": V(f.date(14), "From the third week."),
                                                     "EndDate": V(f.date(28), "Within two weeks.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the factory.", schemeID="INCOTERMS")},
            "DestinationCountry": {"IdentificationCode": V("XU", "Into Urvania.")},
            "Contract": {"ID": V("VI-PUR-TERMS-2026", "The manufacturer's purchasing terms.")},
            "RequestForQuotationLine": [{**out["RequestForQuotationLine"][0], "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:ubl-examples:world:wood:"
                                                                                   "rfq:1")), "The line's UUID."),
                                        "Note": V("Kiln-dried hardwood, planed on four sides.", "The requirement."),
                                        "OptionalLineItemIndicator": V("false", "A required line."),
                                        "PrivacyCode": V("Confidential", "The drawing is the manufacturer's own."),
                                        "SecurityClassificationCode": V("Internal", "Not for publication."),
                                        "DocumentReference": {"ID": V("VI-DS-SL1800", "The drawing.")}}]}


@enrich("wood", "Quotation")
def _(f, n, doc, out):
    base = Decimal(out["QuotedMonetaryTotal"]["LineExtensionAmount"].value)
    line = out["QuotationLine"][0] if isinstance(out["QuotationLine"], list) else out["QuotationLine"]
    line.update({"ID": V("1", "The quotation line."), "Note": V("As drawn; ash or oak.", "What is quoted."),
                 "Quantity": qty(4800, "H87", "The quantity quoted."),
                 "LineExtensionAmount": amount(base, "XBL", "The quoted amount."),
                 "TaxInclusiveLineExtensionAmount": amount(base, "XBL", "No tax on an export."),
                 "TotalTaxAmount": amount(0, "XBL", "No tax on an export."),
                 "RequestForQuotationLineID": V("1", "The line of the request."),
                 "DocumentReference": {"ID": V("MS-SPEC-SL1800", "The sawmill's specification.")},
                 "RequestLineReference": {"LineID": V("1", "The request line answered.")},
                 "SellerProposedSubstituteLineItem": {"ID": V("1-S", "A substitute the sawmill proposes."),
                                                      "Quantity": qty(4800, "H87", "The same quantity."),
                                                      "Item": {"Name": V("Hardwood bench slat 1800 × 95 × 35",
                                                                         "Three millimetres thinner: less waste, "
                                                                         "five per cent cheaper.")}},
                 "AlternativeLineItem": {"ID": V("1-A", "An alternative species."),
                                         "Quantity": qty(4800, "H87", "The same quantity."),
                                         "Item": {"Name": V("Oak bench slat 1800", "Oak instead of ash, at a higher "
                                                                                   "price.")}}})
    return {"Note": V("Valid for 30 days.", "The validity."),
            "PricingCurrencyCode": V("XBL", "Prices in lume."), "LineCountNumeric": V("1", "One line."),
            "AdditionalDocumentReference": {"ID": V("MS-GTC-2026", "The sawmill's terms of sale.")},
            "Contract": {"ID": V("VI-PUR-TERMS-2026", "The buyer's purchasing terms, accepted.")},
            "Signature": seal(doc["from"], "MS-SIG-26-QT"),
            "Delivery": {"PromisedDeliveryPeriod": {"StartDate": V(f.date(14), "From the third week."),
                                                    "EndDate": V(f.date(28), "Within two weeks.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the factory, as asked.", schemeID="INCOTERMS")},
            "PaymentMeans": {"PaymentMeansCode": V("30", "By credit transfer.", listID="UN/EDIFACT EDED 4461")},
            "TransactionConditions": {"Description": V("Quoted per thousand slats; minimum one truck.", "The "
                                                                                                       "conditions.")},
            "DestinationCountry": {"IdentificationCode": V("XU", "Into Urvania.")},
            "TaxTotal": {"TaxAmount": amount(0, "XBL", "No sales tax on an export.")}}


@enrich("furniture", "RequestForQuotation")
def _(f, n, doc, out):
    return {"SubmissionDueDate": V(f.date(5), "Quotations within five days."),
            "Note": V("For the store's own garden line.", "What is asked."),
            "PricingCurrencyCode": V("XBL", "In lume."), "LineCountNumeric": V("1", "One line."),
            "RequestedValidityPeriod": {"DurationMeasure": V("60", "Prices for 60 days.", unitCode="DAY")},
            "CatalogueDocumentReference": {"ID": V("BM-RANGE-26", "The store's range plan the line belongs to.")},
            "Signature": seal(doc["from"], "BM-SIG-26-RFQ"),
            "OriginatorCustomerParty": {"Party": party("26-xb", short=True)},
            "Delivery": {"DeliveryLocation": {"Name": V("Brightmarket Stores, goods-in", "Where.")}},
            "DeliveryTerms": {"ID": V("DAP", "Delivered at the store.", schemeID="INCOTERMS")},
            "DestinationCountry": {"IdentificationCode": V("XB", "Bayvarra.")},
            "Contract": {"ID": V("BM-OWN-BRAND-2026", "The store's own-brand terms.")},
            "RequestForQuotationLine": [{**out["RequestForQuotationLine"][0],
                                         "Note": V("Optional: seat cushions to match.", "An option."),
                                        "OptionalLineItemIndicator": V("false", "The set itself is required."),
                                        "PrivacyCode": V("Confidential", "The store's own design."),
                                        "SecurityClassificationCode": V("Internal", "Not for publication.")}]}


@enrich("furniture", "Quotation")
def _(f, n, doc, out):
    return {"Note": V("Including the store's own label.", "What is quoted."),
            "PricingCurrencyCode": V("XBL", "In lume."), "LineCountNumeric": V("1", "One line."),
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
            **kit.cost_centre("2-xb", "The department's programme."),
            "Signature": seal("2-xb", "PWD-SIG-26-WR", "The department's approval signature."),
            "WorkQuantityTotal": {"Quantity": qty(14, "HUR", "Fourteen hours."),
                                  "WorkTypeCode": V("Installation", "The kind of work."),
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
                                                      "WorkPhaseCode": V("Furnish", "Furnishing."),
                                                      "WorkPhase": V("Furnishing the office", "In words."),
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
            "Contract": {"ID": V(f.numbers["quotation"], "The quotation the line runs under; it allows "
                                                         "cancellation before production.")},
            "Signature": seal(doc["from"], "BM-SIG-26-OC")}


@enrich("air", "FulfilmentCancellation")
def _(f, n, doc, out):
    return {"Note": V("A new despatch advice follows today.", "What happens next."),
            "OrderReference": {"ID": V(f.numbers["order-change"], "The order change of the frames."),
                               "SalesOrderID": V(f"LD-SO-26-{SEA.base:04d}", "The distributor's sales order."),
                               "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:ubl-examples:world:air:1:OrderChange")),
                                         "Its UUID."),
                               "IssueDate": V(f.date(0), "Its date."), "IssueTime": V("07:50:00", "Its time."),
                               "CustomerReference": V("Harbour parks Selanu", "The buyer's project."),
                               "OrderTypeCode": V("230", "UN/EDIFACT 1001 code 230: order change."),
                               "DocumentReference": {"ID": V(SEA.numbers["order"], "The original sea order.")}},
            "AdditionalDocumentReference": {"ID": V("KAC-OFFLOAD-26-0513", "The airline's offload notice.")},
            "Contract": {"ID": V(SEA.numbers["agreement"], "The digital agreement.")},
            "Signature": seal(doc["from"], "LD-SIG-26-FC"),
            "DespatchSupplierParty": {"Party": party("6-xb", short=True)}}


@enrich("plastics", "ImportCustomsDeclaration")
def _(f, n, doc, out):
    return {"Shipment": {"GoodsItem": [{**out["Shipment"]["GoodsItem"][0], "BondedWarehouseLocation": {
        **out["Shipment"]["GoodsItem"][0]["BondedWarehouseLocation"],
        "CountrySubentity": V("Coastal State", "The state the store is in."),
        "CountrySubentityCode": V("CO", "As a code of Bayvarra's address scheme."),
        "LocationTypeCode": V("BondedStore", "A customs bonded store."),
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
                    "MinimumTemperature": {"AttributeID": V("Hall", "The temperature of the hall."),
                                           "Measure": V("5", "At least 5 °C.", unitCode="CEL"),
                                           "MeasureCode": V("Min", "The lowest."),
                                           "Description": V("Kept frost-free.", "Why.")},
                    "MaximumTemperature": {"AttributeID": V("Hall", "The temperature of the hall."),
                                           "Measure": V("35", "At most 35 °C.", unitCode="CEL")},
                    "Certificate": {"ID": V("XB-BOND-LIC-0388", "The bonded store's licence."),
                                    "CertificateTypeCode": V("BondedStore", "A licence of customs."),
                                    "CertificateType": V("Bonded store licence", "In words.")}}}}] +
        out["Shipment"]["GoodsItem"][1:]}}


@enrich("road", "Order")
def _(f, n, doc, out):
    return {"Delivery": {"Despatch": {"DespatchAddress": {"MarkCare": V("Valdara Industries c/o Castrano Logistics",
                                                                        "The goods are the manufacturer's, kept by "
                                                                        "its 3PL.")}}}}


@enrich("road", "TransportationStatus")
def _(f, n, doc, out):
    st = out["TransportEvent"]["CurrentStatus"]
    st["Condition"] = [st["Condition"], {"AttributeID": V("Trailer temperature", "Recorded by the trailer's "
                                                                                 "sensor."),
                                         "Measure": V("14", "The temperature in the trailer.", unitCode="CEL"),
                                         "MinimumMeasure": V("4", "The lowest during the night.", unitCode="CEL"),
                                         "MaximumMeasure": V("18", "The highest in the afternoon.", unitCode="CEL"),
                                         "Description": V("No protection needed for steel benches.", "Why it is "
                                                                                                    "only noted.")}]
    return {}


@enrich("retail", "RetailEvent")
def _(f, n, doc, out):
    spec = out["PromotionalEvent"]["PromotionalSpecification"]
    spec["EventTactic"] = {"Comment": V("Benches at the entrance, with a price board.", "What the store does."),
                           "Quantity": qty(12, "H87", "Twelve benches on display."),
                           "EventTacticEnumeration": {"ConsumerIncentiveTacticTypeCode": V("TPR", "A temporary price "
                                                                                                  "reduction."),
                                                      "DisplayTacticTypeCode": V("EndCap", "A display at the "
                                                                                           "entrance."),
                                                      "FeatureTacticTypeCode": V("Flyer", "In the store's flyer."),
                                                      "TradeItemPackingLabelingTypeCode": V("Sticker", "A price "
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
                 "PurchaseReference": {"ID": V(f"VI-SF-{f.base * 10:05d}", "The serial number of the bench's frame, "
                                                                             "for the warranty."),
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
    crew = [kit.person("Corin", "Halvard", "The master.", role="Master"),
            kit.person("Elsbeth", "Marrin", "The chief officer, also the ship's medical officer.", role="ChiefOfficer"),
            kit.person("Rafe", "Dunmore", "The chief engineer.", role="ChiefEngineer")]
    sea_place = {"Name": V("At sea, 120 nautical miles west of Selanu", "Where.")}
    stage = out["Shipment"]["ShipmentStage"]
    stage.update({
        "PassengerPerson": kit.person("Ines", "Tavari", "The one passenger, a supercargo.", role="Passenger"),
        "ReportingPerson": kit.person("Corin", "Halvard", "The master reports.", role="Master"),
        "CrewMemberPerson": crew,
        "SecurityOfficerPerson": kit.person("Elsbeth", "Marrin", "The ship security officer.", role="SSO"),
        "ShipsSurgeonPerson": kit.person("Elsbeth", "Marrin", "No surgeon on a feeder: the chief officer is the "
                                                              "medical officer.", role="MedicalOfficer"),
        "DestinationPortCall": {
            "ID": V("XLSEL-26-0517", "The port call at Selanu."),
            "PlannedOperationsDescription": V("Discharge one container, load six.", "What the ship will do."),
            "PlannedWorksDescription": V("None.", "No repairs planned."),
            "PlannedInspectionsDescription": V("Port state control is due.", "An inspection is expected."),
            "ExpectedAnchorageIndicator": V("false", "Straight to the berth."),
            "PositionInPortID": V("BERTH-2", "The container berth."),
            "CargoAndBallastTankConditionDescription": V("Tanks clean; ballast exchanged at sea.", "Their "
                                                                                                   "condition."),
            "ShipRequirement": {"ID": V("SR-1", "A need of the ship."),
                                "Description": V("Fresh water, 40 tonnes.", "What it needs.")},
            "PrimaryPortCallPurpose": {"PurposeTypeCode": V("Cargo", "Cargo operations."),
                                       "PurposeType": V("Cargo operations", "In words."),
                                       "Description": V("Discharge and load containers.", "The purpose.")},
            "AdditionalPortCallPurpose": {"PurposeTypeCode": V("Water", "Taking on water."),
                                          "PurposeType": V("Bunkering of fresh water", "In words.")},
            "RequestedArrivalEvent": {"IdentificationID": V("ARR-XLSEL-0517", "The requested arrival."),
                                      "OccurrenceDate": V(f.date(14), "The day."),
                                      "OccurrenceTime": V("06:00:00", "At first light."),
                                      "TypeCode": V("Arrival", "An arrival."),
                                      "Description": V("Pilot on board at the fairway buoy.", "What is asked."),
                                      "CompletionIndicator": V("false", "Not yet."),
                                      "CurrentStatus": {"ConditionCode": V("OnTime", "Expected on time.")},
                                      "Contact": {"Name": V("Bridge", "Whom to call."),
                                                  "Telephone": V("+999 2 3900 2117", "The ship's satellite phone.")},
                                      "OccurrenceLocation": {"Name": V("Selanu fairway buoy", "Where the pilot "
                                                                                              "boards.")}}},
        "ShipStoreArticle": [{"ID": V("ST-1", "Spirits in the bonded store."), "Name": V("Spirits", "What."),
                              "Quantity": qty(24, "LTR", "Litres."),
                              "OfficialUse": V("Sealed by customs at Lumeport.", "Under seal."),
                              "Stowage": {"LocationID": V("BOND-1", "The bonded locker."),
                                          "Location": V("Bonded locker, accommodation deck", "Where.")}},
                             {"ID": V("ST-2", "Cigarettes."), "Name": V("Cigarettes", "What."),
                              "Quantity": qty(2000, "H87", "Pieces.")}],
        "CrewPersonEffect": {"EffectDescription": V("One camera, one laptop.", "What the crew member declares."),
                             "CrewPerson": crew[2]},
        "MaritimeWaste": [{"ID": V("W-1", "Oily waste."), "Description": V("Sludge from the fuel separators.",
                                                                           "What."),
                           "WasteTypeCode": V("Oil", "MARPOL Annex I waste."),
                           "ToBeDeliveredMeasure": V("2.4", "To be delivered at Selanu.", unitCode="MTQ"),
                           "RetainedOnBoardMeasure": V("0.6", "Kept on board.", unitCode="MTQ"),
                           "MaxDedicatedStorageCapacityMeasure": V("8", "The tank's capacity.", unitCode="MTQ"),
                           "EstimatedGeneratedUntilNextPortMeasure": V("0.8", "Until Lumeport again.",
                                                                       unitCode="MTQ"),
                           "RemainingWasteDeliveryPortLocation": kit.place("XBLMP", "The rest goes ashore at "
                                                                                    "Lumeport.")},
                          {"ID": V("W-2", "Garbage."), "Description": V("Food and packaging waste.", "What."),
                           "WasteTypeCode": V("Garbage", "MARPOL Annex V waste."),
                           "ToBeDeliveredMeasure": V("1.5", "To be delivered.", unitCode="MTQ")}],
        "BallastWaterSummary": {
            "ID": V("BW-26-0517", "The ballast water report."),
            "ManagementPlanOnBoardIndicator": V("true", "The plan is on board."),
            "ManagementPlanImplementedIndicator": V("true", "And followed."),
            "IMOGuidelinesOnBoardIndicator": V("true", "The IMO guidelines are on board."),
            "TotalBallastTanksOnBoardQuantity": qty(8, "C62", "Ballast tanks."),
            "TanksInBallastQuantity": qty(4, "C62", "Tanks with ballast now."),
            "TanksExchangedQuantity": qty(4, "C62", "Exchanged at sea."),
            "TanksNotExchangedQuantity": qty(0, "C62", "None left unexchanged."),
            "TotalBallastWaterOnBoardMeasure": V("1240", "Ballast on board.", unitCode="TNE"),
            "TotalBallastWaterCapacityMeasure": V("2480", "The capacity.", unitCode="TNE"),
            "OtherControlActions": V("None.", "No other measures."),
            "NoControlActionsReason": V("Exchange done at more than 200 nautical miles from land.", "Why no "
                                                                                                  "treatment was "
                                                                                                  "needed."),
            "UptakeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."), "TankTypeCode": V("Wing",
                                                                                                "A wing tank."),
                                              "VolumeMeasure": V("310", "Taken up at Lumeport.", unitCode="TNE"),
                                              "SeaHeightMeasure": V("2", "The depth of the intake.", unitCode="MTR"),
                                              "SalinityMeasure": V("30", "Salinity.", unitCode="GL"),
                                              "TransactionDate": V(f.date(10), "At Lumeport."),
                                              "Location": kit.place("XBLMP", "The port."),
                                              "BallastWaterTemperature": {"AttributeID": V("Water", "The water."),
                                                                          "Measure": V("16", "Its temperature.",
                                                                                       unitCode="CEL")}},
            "ExchangeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."),
                                                "ExchangeMethodCode": V("Sequential", "Emptied and refilled."),
                                                "ExchangedPercent": V("95", "Of the volume."),
                                                "VolumeMeasure": V("310", "Exchanged.", unitCode="TNE"),
                                                "TransactionDate": V(f.date(12), "At sea."),
                                                "Location": sea_place},
            "DischargeBallastWaterTransaction": {"TankID": V("BT-3", "The tank."),
                                                 "VolumeMeasure": V("120", "To be discharged at Selanu.",
                                                                    unitCode="TNE"),
                                                 "TransactionDate": V(f.date(14), "In port.")},
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
            "TotalDeadPersonQuantity": qty(0, "C62", "None."),
            "TotalIllPersonQuantity": qty(1, "C62", "One crew member with a sprained wrist."),
            "SickAnimalDescription": V("None on board.", "No animals."),
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
            "SanitaryMeasure": {"SanitaryMeasureTypeCode": V("Disinfection", "The galley was disinfected."),
                                "ApplicationDate": V(f.date(11), "When.")},
            "PlaceOfReportLocation": sea_place,
            "MedicalCertificate": {"ID": V("MC-TH-2026", "The ship's medicine chest certificate."),
                                   "CertificateType": V("Medicine chest", "Its kind.")},
            "ShipSanitationControlCertificate": {"ID": V("SSCC-XB-2025-0911", "The sanitation control "
                                                                              "certificate."),
                                                 "CertificateType": V("Ship sanitation control", "Its kind.")},
            "ShipSanitationControlExemptionDocumentReference": {"ID": V("none", "No exemption: the ship holds the "
                                                                                "control certificate.")}},
        "FuelConsumption": {"ID": V("FC-26-19E", "The fuel of the voyage."),
                            "FuelTypeCode": V("MGO", "Marine gas oil."),
                            "FuelType": V("Marine gas oil, 0.1 % sulphur", "In words."),
                            "FuelConsumptionMeasure": V("38", "Used from Lumeport.", unitCode="TNE"),
                            "AdditionalFuelProperty": {"TypeID": V("Sulphur", "The sulphur content."),
                                                       "Value": V("0.1 %", "Its value.")},
                            "FuelMetering": {"TypeID": V("FlowMeter", "Measured by the flow meter."),
                                             "Value": V("38.2 t", "The reading.")},
                            "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2", "Carbon dioxide."),
                                                      "ValueMeasure": V("122", "From 38 t of gas oil.",
                                                                        unitCode="TNE")},
                            "FuelProviderParty": party("16-xb", short=True)}})
    stage["ISPSRequirements"].update({
        "ISSCAbsenceReason": V("Not applicable: the certificate is on board.", "Stated, not left out."),
        "SSPOnBoardIndicator": V("true", "The security plan is on board."),
        "SSPSecurityMeasuresAppliedIndicator": V("true", "Its measures were applied."),
        "AdditionalMattersDescription": V("None.", "Nothing else to report."),
        "ReportLocation": sea_place,
        "ISSCIssuerParty": party("30-xl", short=True),
        "SecurityOfficerPerson": crew[1],
        "ShipToShipActivityRecord": {"ID": V("STS-0", "Ship-to-ship activity."),
                                     "Description": V("None during the last ten port calls.", "The record."),
                                     "Period": {"StartDate": V("2026-01-01", "Since."), "EndDate": V(f.date(13),
                                                                                                     "Until now.")},
                                     "Location": sea_place,
                                     "AppliedSecurityMeasure": {"ID": V("SM-0", "No measure needed."),
                                                                "Description": V("None: no ship-to-ship "
                                                                                 "activity.", "Stated.")}},
        "AdditionalSecurityMeasure": {"ID": V("SM-1", "An extra measure."),
                                      "Description": V("Gangway watch at Selanu.", "What the ship adds.")},
        "PortCallRecord": {"ID": V("PCR-1", "The last port call."),
                           "SecurityLevelCode": V("1", "Security level 1 at Lumeport."),
                           "SecurityMeasure": {"Description": V("Normal access control.", "The measures.")},
                           "PortFacilityLocation": kit.place("XBLMP", "The port facility."),
                           "Period": {"StartDate": V(f.date(9), "Arrived."), "EndDate": V(f.date(10), "Sailed.")}}})
    tm = out["TransportMeans"]["MaritimeTransport"]
    tm.update({"INFShipClassCode": V("INF1", "IMO INF class 1: may not carry irradiated fuel in quantity."),
               "AntennaLocus": V("Mast, 28 m above the waterline", "Where the AIS antenna is."),
               "VesselDynamics": {"NavigationStatusCode": V("0", "AIS status 0: under way using engine."),
                                  "AtAnchorageIndicator": V("false", "Not at anchor."),
                                  "CourseOverGroundDirection": V("088", "Course over ground, in degrees."),
                                  "SpeedOverGroundMeasure": V("13.5", "Speed over ground.", unitCode="KNT"),
                                  "RateOfTurnMeasure": V("0", "Not turning.", unitCode="C62")}})
    return {}


# ---------------------------------------------------------------- the mast flow (dangerous goods by air)
MAST = kit.Flow("mast", "2026-06-01", [
    {"item": "battery-pack", "ordered": 6, "why": "Six packs: four hours of back-up power for the mast."},
    {"item": "smoke-detector", "ordered": 1, "why": "One set of ten for the equipment room."},
    {"item": "coating-stripper", "ordered": 20, "why": "Four cans of five litres for the circuit boards."}])


def dg_temperature(attr, lo, hi, why):
    return ({"AttributeID": V(attr, why), "Measure": V(lo, "The lowest allowed.", unitCode="CEL")},
            {"AttributeID": V(attr, why), "Measure": V(hi, "The highest allowed.", unitCode="CEL")})


def mast_consignment(f, full):
    lo, hi = dg_temperature("Battery", "5", "35", "Lithium-ion packs must not freeze nor overheat.")
    bat = ITEM["battery-pack"]
    loaded = {"ID": V("SE-BAT-48100-DG", "The battery packs in the container."),
              "UNDGCode": V("3480", "UN 3480.", listID="UNCL8273"),
              "ProperShippingName": V("Lithium ion batteries", "As on the declaration."),
              "HazardClassID": V("9", "Class 9."),
              "GrossWeightMeasure": qty(Decimal(6) * Decimal(str(bat["gross_kg"])), "KGM", "Six packs, packed."),
              "NetWeightMeasure": qty(Decimal(6) * Decimal(str(bat["net_kg"])), "KGM", "The packs alone."),
              "NetVolumeMeasure": V("0.24", "Their volume.", unitCode="MTQ"),
              "Quantity": qty(6, "H87", "Six packs."),
              "HazardousTypeCode": V("Article", "Batteries are articles, not substances."),
              "PackagingDangerLevelCode": V("None", "Lithium batteries have no packing group."),
              "UpperOrangeHazardPlacardID": V("90", "The hazard identification number for road transport."),
              "LowerOrangeHazardPlacardID": V("3480", "The UN number on the orange plate."),
              "CategoryName": V("Miscellaneous dangerous goods", "Class 9 in words."),
              "ContactParty": party("27-xb", short=True),
              "EmergencyTemperature": {"AttributeID": V("Emergency", "Above this, emergency procedures."),
                                       "Measure": V("60", "Thermal runaway risk.", unitCode="CEL")},
              "AdditionalTemperature": {"AttributeID": V("Storage", "Recommended storage."),
                                        "Measure": V("20", "Around 20 °C.", unitCode="CEL")},
              "PositionOnBoardStowage": {"LocationID": V("MD-L2", "Main deck, position L2."),
                                         "Location": V("Main deck, accessible", "Where it flies.")},
              "Package": {"ID": V("SE-CR-1..6", "The six crates."), "Quantity": qty(6, "H87", "Six."),
                          "PackagingTypeCode": V("CR", "UN/ECE Recommendation 21 code CR: crate.")},
              "HazardousGoodsTransit": {"TransportEmergencyCardCode": V("TEC-90-3480", "The emergency card on "
                                                                                     "board."),
                                        "PackingCriteriaCode": V("PI965-IA", "IATA packing instruction 965, "
                                                                             "section IA."),
                                        "HazardousRegulationCode": V("IATA", "Air: the IATA Dangerous Goods "
                                                                             "Regulations."),
                                        "InhalationToxicityZoneCode": V("None", "Not toxic by inhalation."),
                                        "TransportAuthorizationCode": V("CAO", "Cargo aircraft only."),
                                        "TransitDescription": V("Cargo aircraft only; state of charge below 30 %.",
                                                                "The conditions."),
                                        "MaximumTemperature": hi, "MinimumTemperature": lo}}
    equipment = {"ID": V("RKN-41207-KC", "The temperature-controlled air container."),
                 "TransportEquipmentTypeCode": V("AM", "UN/EDIFACT 8053 code AM: refrigerated container.",
                                                 listID="UN/EDIFACT EDED 8053"),
                 "RefrigeratedIndicator": V("true", "A temperature-controlled unit."),
                 "RefrigerationOnIndicator": V("true", "The unit is switched on."),
                 "AirFlowPercent": V("40", "The fan's air flow."),
                 "HumidityPercent": V("50", "Humidity kept below 50 %."),
                 "AnimalFoodApprovedIndicator": V("false", "Not for feed."),
                 "HumanFoodApprovedIndicator": V("false", "Not for food."),
                 "DangerousGoodsApprovedIndicator": V("true", "Approved for dangerous goods."),
                 "PowerIndicator": V("true", "Battery-powered cooling and heating."),
                 "MinimumTemperature": lo, "MaximumTemperature": hi,
                 "LoadedHazardousItem": loaded, "HazardousGoodsTransit": loaded["HazardousGoodsTransit"]}
    out = {"HazardousRiskIndicator": V("true", "The consignment holds dangerous goods."),
           "HazardousItemNotificationParty": party("27-xb", short=True),
           "TransportHandlingUnit": {"ID": V("RKN-41207-KC", "The container as a handling unit."),
                                     "HazardousRiskIndicator": V("true", "Dangerous goods inside."),
                                     "HazardousGoodsTransit": loaded["HazardousGoodsTransit"],
                                     "MinimumTemperature": lo, "MaximumTemperature": hi,
                                     "TransportEquipment": equipment}}
    if full:
        out["MainCarriageShipmentStage"] = {
            "ID": V("1", "The flight."), "TransportModeCode": V("4", "Air transport.",
                                                               listID="UNECE Recommendation 19 - Codes for Modes of "
                                                                      "Transport"),
            "HazardousRiskIndicator": V("true", "Dangerous goods on the flight."),
            "TransportMeans": kit.means("12-xl", "KAC", "KAC209", "The cargo flight of the day.")}
    return out


def mast(n, doc):
    f, d = MAST, doc["doc"]
    w = kit.gross_weight(f, "ordered")
    if d == "Order":
        return kit.order(f, n, doc, 0, "The telecom company orders before the storm season.",
                         "Carriage paid to the telecom company's site: the seller arranges the dangerous goods "
                         "transport.", "Selanu Telecom, mast site")
    if d == "ForwardingInstructions":
        return {"ID": V(f.number("instructions", doc["from"], "ForwardingInstructions"), "The instruction number."),
                "IssueDate": V(f.date(2), "With the shipper's declaration of dangerous goods."),
                "Shipment": {"ID": V(f.number("shipment", doc["from"], "Shipment"), "The shipment."),
                             "GrossWeightMeasure": qty(w, "KGM", "The gross weight."),
                             "GoodsItem": [{"ID": V(str(i), "A goods item."),
                                            "Description": V(ITEM[x["item"]]["name"], "The goods."),
                                            "Temperature": {"AttributeID": V("Transport", "The temperature in "
                                                                                          "transport."),
                                                            "Measure": V("20", "Around 20 °C.", unitCode="CEL"),
                                                            "MeasureCode": V("Target", "The target."),
                                                            "Description": V("Keep away from heat.", "Why.")},
                                            "MinimumTemperature": {"Measure": V("5", "At least.", unitCode="CEL")},
                                            "MaximumTemperature": {"Measure": V("35", "At most.", unitCode="CEL")},
                                            "Item": item(x["item"])} for i, x in enumerate(f.deal, 1)],
                             "Consignment": {"ID": V(f.number("consignment", doc["from"], "Consignment"),
                                                     "The consignment."), **mast_consignment(f, False)}}}
    if d == "Waybill":
        out = kit.waybill(f, n, doc, 3, "The air waybill, cargo aircraft only.", w, "The gross weight.")
        kit.deep_merge(out["Shipment"]["Consignment"], mast_consignment(f, True))
        return out
    if d == "DespatchAdvice":
        return kit.despatch_advice(f, n, doc, 3, "Sent when the goods leave for the airport.", "The gross weight.")
    if d == "Invoice":
        return kit.invoice(f, n, doc, 3, 45, "Issued on despatch.",
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
            "PaymentPurposeCode": V("GOVT", "ISO 20022 purpose code GOVT: a payment to the government, recharged."),
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
           "DiscrepancyResponse": {"ResponseCode": V("Packaging", "A packaging fault."),
                                   "Description": V("Heat-treatment mark illegible on pallet LD-26-007.", "The "
                                                                                                          "fault.")},
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
           "ProjectReference": {"ID": V("Harbour parks Selanu", "The buyer's project."),
                                "UUID": V(str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:project:harbour-parks")), "Its "
                                                                                                           "UUID."),
                                "IssueDate": V(f.date(3), "Started with the order."),
                                "WorkPhaseReference": {"ID": V("PH-1", "Benches for the harbour park."),
                                                       "WorkPhaseCode": V("Supply", "The supply phase.")}},
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
                                        "TaxAmount": amount(0, "XLC", "None."),
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
                "TaxRepresentativeParty": party("10-xb", short=True),
                "TaxExchangeRate": {"SourceCurrencyCode": V("XBL", "The credit's currency."),
                                    "TargetCurrencyCode": V("XUF", "The tax currency."),
                                    "CalculationRate": V("100", "1 lume = 100 ferra.")},
                "PricingExchangeRate": PRICING_RATE,
                "PaymentExchangeRate": TO_FERRA(f.date(82)),
                "AllowanceCharge": {"ChargeIndicator": V("false", "An allowance."),
                                    "AllowanceChargeReason": V("Goodwill", "For the inconvenience."),
                                    "Amount": amount(0, "XBL", "None in money: the bench is replaced.")},
                "WithholdingTaxTotal": {"TaxAmount": amount(Decimal("1.80"), "XBL", "The withholding on the "
                                                                                   "credited installation, "
                                                                                   "reversed.")}})
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
           "Description": V("240 steel park benches with hardwood slats over two years, delivered and anchored.",
                            "What is bought."),
           "ProcurementTypeCode": V("Supplies" if goods else "Services", "Supplies or services."),
           "ProcurementSubTypeCode": V("Purchase" if goods else "Installation", "The kind within it."),
           "QualityControlCode": V("Inspection", "Each release is inspected on delivery."),
           "RequiredFeeAmount": amount(Decimal("50.00"), "XBL", "The fee for the tender documents on paper."),
           "FeeDescription": V("Electronic documents are free; paper copies cost 50 lume.", "The fee."),
           "RequestedDeliveryDate": V(f.date(80), "The first release."),
           "EstimatedOverallContractQuantity": qty(TENDER_QTY, "H87", "240 benches over the contract."),
           "Note": V("Part of the parks renewal programme 2026.", "The programme."),
           "SMESuitableIndicator": V("true", "Small and medium firms can tender."),
           "ProcurementAdditionalType": {"ProcurementTypeCode": V("Green", "Green public procurement."),
                                         "ProcurementType": V("Recycled steel and certified timber are asked.",
                                                              "In words.")},
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
           "MainCommodityClassification": {"ItemClassificationCode": V("9401.79" if goods else "9988.00",
                                                                       "The goods' HS subheading." if goods else
                                                                       "A service: no HS subheading.", listID="HS")},
           "AdditionalCommodityClassification": {"CommodityCode": V("PARKS-FURN", "The department's own category: "
                                                                                  "park furniture.")},
           "RealizedLocation": {"Name": V("Harbour park and town parks, Lumeport", "Where the benches go."),
                                "Address": {"CityName": V("Lumeport", "The city."),
                                            "Country": {"IdentificationCode": V("XB", "Bayvarra.")}}},
           "PlannedPeriod": {"StartDate": V(f.date(70), "From the first release."),
                             "EndDate": V(f.date(800), "For two years.")},
           "ContractExtension": {"OptionsDescription": V("One extension of a year with 120 more benches.", "The "
                                                                                                           "option."),
                                 "MinimumNumberNumeric": V("0", "None need be used."),
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
            "Note": V("Steel frame, five hardwood slats, ground anchors.", "The requirement."),
            "Quantity": qty(TENDER_QTY, "H87", "Over the contract."),
            "MinimumQuantity": qty(120, "H87", "At least."), "MaximumQuantity": qty(288, "H87", "At most."),
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


def tendering_process(f):
    return {"ID": V(f"{FOLDER}-P", "The procedure."), "OriginalContractingSystemID": V("PWD-FW-2024-PARKS", "The "
                                                                                       "framework this one "
                                                                                       "follows."),
            "Description": V("Open procedure with two lots.", "The procedure."),
            "NegotiationDescription": V("No negotiation: the award is on the tenders as submitted.", "Why none."),
            "ProcedureCode": V("Open", "An open procedure."), "UrgencyCode": V("Normal", "No urgency."),
            "ExpenseCode": V("Investment", "Paid from the investment budget."),
            "PartPresentationCode": V("OneOrMore", "Tenders for one or both lots."),
            "ContractingSystemCode": V("Framework", "A framework agreement."),
            "SubmissionMethodCode": V("Electronic", "Tenders are submitted electronically."),
            "CandidateReductionConstraintIndicator": V("false", "No reduction of candidates."),
            "GovernmentAgreementConstraintIndicator": V("true", "Covered by the trade accord's procurement chapter."),
            "AccessToolsURI": V("https://tenders.lumeport.example/PWD-2026-PARKS", "Where the documents are."),
            "TerminatedIndicator": V("false", "The procedure runs."),
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
            "ProcessJustification": {"PreviousCancellationReasonCode": V("None", "No earlier procedure was "
                                                                                "cancelled."),
                                     "ProcessReasonCode": V("Standard", "The open procedure is the rule."),
                                     "ProcessReason": V("Value above the threshold for open procedures.", "Why."),
                                     "Description": V("No exception applies.", "In words.")},
            "EconomicOperatorShortList": {"LimitationDescription": V("No short list in an open procedure.", "Why."),
                                          "ExpectedQuantity": V("0", "None expected."),
                                          "MaximumQuantity": V("0", "None."), "MinimumQuantity": V("0", "None."),
                                          "PreSelectedParty": party("5-xu", short=True)},
            "OpenTenderEvent": {"IdentificationID": V("OPEN-1", "The opening of the tenders."),
                                "OccurrenceDate": V(f.date(45), "The deadline day."),
                                "OccurrenceTime": V("14:00:00", "Two hours after the deadline."),
                                "TypeCode": V("Opening", "A tender opening."),
                                "Description": V("Electronic opening; tenderers may follow it online.", "How."),
                                "CompletionIndicator": V("false", "To come."),
                                "CurrentStatus": {"ConditionCode": V("Scheduled", "Planned.")},
                                "Contact": {"Name": V("Procurement office", "Whom to ask.")},
                                "OccurrenceLocation": {"Name": V("Lumeport Public Works Department, Civic Square",
                                                                 "Where.")}},
            "AuctionTerms": {"AuctionConstraintIndicator": V("false", "No electronic auction."),
                             "JustificationDescription": V("The award uses quality as well as price.", "Why not."),
                             "Description": V("No auction.", "In words."),
                             "ProcessDescription": V("Not applicable.", "No process."),
                             "ConditionsDescription": V("Not applicable.", "No conditions."),
                             "ElectronicDeviceDescription": V("Not applicable.", "No device."),
                             "AuctionURI": V("https://tenders.lumeport.example/auctions", "The platform, unused.")},
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
                                                                          "Description": V("No new competition.",
                                                                                           "How.")}},
            "ContractingSystem": {"ID": V("FW-1", "The framework."),
                                  "ContractingSystemTypeCode": V("Framework", "A framework agreement."),
                                  "Description": V("Framework with one supplier.", "In words.")}}


def tendering_terms(f):
    return {"AwardingMethodTypeCode": V("BestValue", "The best price-quality ratio."),
            "PriceEvaluationCode": V("UnitPrice", "Evaluated on the unit prices."),
            "MaximumVariantQuantity": V("1", "One variant allowed."),
            "VariantConstraintIndicator": V("true", "Variants are allowed."),
            "AcceptedVariantsDescription": V("A bench of recycled plastic slats.", "The variant allowed."),
            "VariantConstraintCode": V("Allowed", "As a code."),
            "PriceRevisionFormulaDescription": V("Steel index each January.", "How prices change."),
            "FundingProgramCode": V("PARKS-26", "The programme."),
            "FundingProgram": V("Parks renewal programme 2026", "In words."),
            "MaximumAdvertisementAmount": amount(Decimal("500.00"), "XBL", "The most the winner pays for "
                                                                           "publication."),
            "Note": V("Questions through the platform only.", "How to ask."),
            "PaymentFrequencyCode": V("PerRelease", "Payment after each release."),
            "EconomicOperatorRegistryURI": V("https://register.bayvarra.example", "Where tenderers are "
                                                                                  "registered."),
            "RequiredCurriculaIndicator": V("true", "The installers' qualifications are asked."),
            "RequiredCurriculaCode": V("Installers", "For lot 2."),
            "OtherConditionsIndicator": V("true", "There are other conditions."),
            "RecurringProcurementIndicator": V("true", "The parks are renewed every few years."),
            "RecurringProcurementDescription": V("A next procedure in about four years.", "When."),
            "EstimatedTimingFurtherPublication": V("2030", "The next notice."),
            "AdditionalConditions": V("Benches must carry the maker's serial number.", "A condition."),
            "LatestSecurityClearanceDate": V(f.date(40), "No clearance is needed; the date is the latest for "
                                                         "site access passes."),
            "DocumentationFeeAmount": amount(Decimal("50.00"), "XBL", "For paper documents."),
            "MultipleTendersCode": V("NotAllowed", "One tender per tenderer."),
            "PenaltyClause": {"ID": V("PEN-1", "Late delivery."), "Content": V("0.5 % per day late, at most 10 %.",
                                                                              "The penalty.")},
            "RequiredFinancialGuarantee": {"GuaranteeTypeCode": V("TenderGuarantee", "A tender guarantee."),
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
            "CallForTendersDocumentReference": {"ID": V(f"{FOLDER}-CFT", "The call for tenders.")},
            "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
            "PaymentTerms": {"Note": V("30 days after each accepted release.", "The terms.")},
            "TendererQualificationRequest": {
                "CompanyLegalFormCode": V("Any", "Any legal form."),
                "CompanyLegalForm": V("Consortia must name a lead member.", "The rule."),
                "PersonalSituation": V("No exclusion grounds.", "The tenderer's situation."),
                "OperatingYearsQuantity": qty(3, "ANN", "At least three years in business."),
                "EmployeeQuantity": qty(10, "C62", "At least ten employees."),
                "Description": V("Economic and technical capacity.", "What is asked."),
                "RequiredBusinessClassificationScheme": {"ID": V("ISIC4", "ISIC Rev. 4."),
                                                         "Name": V("ISIC Rev. 4", "The classification."),
                                                         "ClassificationCategory": {"CodeValue": V("3100", "Furniture "
                                                                                                   "manufacture."),
                                                                                    "Name": V("Manufacture of "
                                                                                              "furniture", "In "
                                                                                                           "words.")}},
                "TechnicalEvaluationCriterion": {"EvaluationCriterionTypeCode": V("References", "References."),
                                                 "Description": V("Three similar supplies in five years.", "What."),
                                                 "ThresholdQuantity": qty(3, "C62", "Three."),
                                                 "DurationPeriod": {"DurationMeasure": V("5", "Five years.",
                                                                                         unitCode="ANN")},
                                                 "SuggestedEvidence": {"ID": V("EV-REF", "Reference letters."),
                                                                       "Name": V("References", "What.")}},
                "FinancialEvaluationCriterion": {"EvaluationCriterionTypeCode": V("Turnover", "Turnover."),
                                                 "Description": V("Yearly turnover of at least twice the "
                                                                  "estimate.", "What."),
                                                 "ThresholdAmount": amount(Decimal("250000"), "XBL", "The minimum."),
                                                 "ExpressionCode": V("GreaterThan", "As a rule."),
                                                 "Expression": V("Turnover > 2 × estimate", "The formula.")},
                "SpecificTendererRequirement": {"Name": V("Certified timber", "The requirement."),
                                                "TendererRequirementTypeCode": V("Environmental", "Its kind."),
                                                "Description": V("Slats from forests managed for regrowth.", "What."),
                                                "LegalReference": V("XB-ENV-2021 art. 12", "The rule."),
                                                "SuggestedEvidence": {"ID": V("EV-FOR", "A forestry certificate."),
                                                                      "Name": V("Forestry certificate", "What.")}},
                "EconomicOperatorRole": {"RoleCode": V("Lead", "The lead tenderer."),
                                         "RoleDescription": V("Leads a consortium.", "In words.")}},
            "AllowedSubcontractTerms": {"Rate": V("30", "Up to 30 % subcontracted."),
                                        "UnknownPriceIndicator": V("false", "The subcontracting share is known."),
                                        "Description": V("Installation may be subcontracted.", "What."),
                                        "Amount": amount(EST_INSTALL, "XBL", "Lot 2's value."),
                                        "SubcontractingConditionsCode": V("Allowed", "As a code."),
                                        "MaximumPercent": V("30", "At most."), "MinimumPercent": V("0", "At least.")},
            "TenderPreparation": {"TenderEnvelopeID": V("ENV-1", "One envelope."),
                                  "TenderEnvelopeTypeCode": V("Combined", "Technical and price together."),
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
                                             "ExecutionRequirementCode": V("Environmental", "Its kind."),
                                             "Description": V("At least 30 % recycled steel in the frames.",
                                                              "What.")},
            "AwardingTerms": {
                "WeightingAlgorithmCode": V("WeightedSum", "A weighted sum."),
                "Description": V("Price 60 %, quality 40 %.", "The award."),
                "TechnicalCommitteeDescription": V("Three officers of the department.", "Who evaluates."),
                "LowTendersDescription": V("Prices 30 % below the average are examined.", "Abnormally low."),
                "PrizeIndicator": V("false", "Not a design contest."),
                "PrizeDescription": V("None.", "No prize."),
                "PaymentDescription": V("No payment for tendering.", "None."),
                "FollowupContractIndicator": V("false", "No follow-up contract."),
                "BindingOnBuyerIndicator": V("true", "The evaluation binds the buyer."),
                "NoFurtherNegotiationIndicator": V("true", "No negotiation after the award."),
                "AwardingCriterion": [
                    {"ID": V("AC-1", "Price."), "AwardingCriterionTypeCode": V("Price", "Its kind."),
                     "Name": V("Price", "Name."), "Description": V("The lowest total of unit prices.", "How."),
                     "WeightNumeric": V("60", "Weight."), "Weight": V("60 %", "In words."),
                     "CalculationExpression": V("60 × lowest / tendered", "The formula."),
                     "CalculationExpressionCode": V("Inverse", "As a code."),
                     "MinimumAmount": amount(Decimal("350"), "XBL", "Unit price at least."),
                     "MaximumAmount": amount(Decimal("600"), "XBL", "At most."),
                     "MinimumImprovementBid": V("Not applicable: no auction.", "Stated.")},
                    {"ID": V("AC-2", "Quality."), "AwardingCriterionTypeCode": V("Quality", "Its kind."),
                     "Name": V("Quality", "Name."), "WeightNumeric": V("40", "Weight."),
                     "MinimumQuantity": qty(5, "ANN", "Warranty of at least five years."),
                     "MaximumQuantity": qty(10, "ANN", "Up to ten years counts."),
                     "SubordinateAwardingCriterion": {"ID": V("AC-2.1", "Durability."),
                                                      "Name": V("Durability of the coating", "Name."),
                                                      "WeightNumeric": V("20", "Half of quality.")}}],
                "TechnicalCommitteePerson": kit.person("Mara", "Delling", "The head of parks on the committee.",
                                                       job="Head of parks"),
                "Prize": {"RankCode": V("None", "No prizes in a tender."),
                          "ValueAmount": amount(0, "XBL", "No prize money."), "Description": V("Not a contest.",
                                                                                           "Why.")}},
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
                         "LocaleCode": V("EN", "As an ISO 639 code.")},
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
            "ReplacedNoticeDocumentReference": {"ID": V(f"{FOLDER}-PIN", "The prior information notice this "
                                                                         "notice follows.")},
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
            "EconomicOperatorShortList": {"LimitationDescription": V("No short list.", "An open procedure.")},
            "SecurityClearanceTerm": {"Code": V("None", "No security clearance."),
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


def notice_head(f, kind, code):
    return {"VersionID": V("1", "The first version."), "PreviousVersionID": V("0", "No earlier version."),
            "RequestedPublicationDate": V(out_day(f, kind), "When to publish."),
            "RegulatoryDomain": V("Bayvarra public procurement", "The rules the notice follows."),
            "NoticeTypeCode": V(code, "The kind of notice."),
            "NoticeLanguageCode": V("EN", "In English, as an ISO 639 code."),
            "AdditionalNoticeLanguage": {"ID": V("fr", "Also published in French, for tenderers from outside the trade accord."),
                                         "LocaleCode": V("FR", "As an ISO 639 code.")},
            "Signature": seal(PWD, f"PWD-SIG-{kind}"),
            "OriginatorCustomerParty": {"Party": party("2-xb", short=True)},
            "BeneficiaryParty": party("2-xb", short=True)}


def out_day(f, kind):
    return f.date({"PIN": 1, "CN": 15, "CAN": 61}[kind])


def contracting_party_details():
    return {"BuyerProfileURI": V("https://tenders.lumeport.example/buyers/pwd", "The buyer's profile."),
            "ContractingPartyType": {"PartyTypeCode": V("Local", "A local authority."),
                                     "PartyType": V("Department of a city", "In words.")},
            "ContractingActivity": {"ActivityTypeCode": V("Public works", "Its activity."),
                                    "ActivityType": V("Public works and parks", "In words.")},
            "ContractingRepresentationType": {"RepresentationTypeCode": V("Own", "On its own behalf."),
                                              "RepresentationType": V("Buys for itself", "In words.")}}


@enrich("tender", "PriorInformationNotice")
def _(f, n, doc, out):
    f.numbers["pin"] = out["ID"].value if "ID" in out else f"{FOLDER}-PIN"
    return {**notice_head(f, "PIN", "PIN"), "Note": V("Advance notice of the bench procedure.", "What."),
            "PlannedDate": V(f.date(14), "The contract notice is planned for then."),
            "DocumentReference": {"ID": V("PWD-PARKS-PLAN-26", "The parks plan.")},
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f),
            "TenderingProcess": {"ProcedureCode": V("Open", "An open procedure is planned."),
                                 "Description": V("Planned as an open procedure in two lots.", "What is planned.")},
            "ProcurementProject": procurement_project(f),
            "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1, planned."), "ProcurementProject": project_brief("LOT-1")},
                                      {"ID": V("LOT-2", "Lot 2, planned."),
                                       "ProcurementProject": project_brief("LOT-2")}]}


@enrich("tender", "ContractNotice")
def _(f, n, doc, out):
    return {**notice_head(f, "CN", "ContractNotice"), "Note": V("Open procedure in two lots.", "What."),
            "FrequencyPeriod": {"DurationMeasure": V("4", "Notices like this about every four years.",
                                                     unitCode="ANN")},
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f), "TenderingProcess": tendering_process(f),
            "ProcurementProject": procurement_project(f), "ProcurementProjectLot": procurement_lots(f)}


@enrich("tender", "CallForTenders")
def _(f, n, doc, out):
    return {"ApprovalDate": V(f.date(13), "Approved by the department's head."),
            "Note": V("The documents of the procedure.", "What."), "VersionID": V("1", "The first version."),
            "PreviousVersionID": V("0", "None."),
            "LegalDocumentReference": {"ID": V("PWD-LEGAL-26", "The legal conditions.")},
            "TechnicalDocumentReference": {"ID": V("PWD-SPEC-BENCH-26", "The specification.")},
            "RequiredDocumentReference": {"ID": V("PWD-PRICE-TPL", "The price schedule.")},
            "ProvidedDocumentReference": {"ID": V("PWD-SITE-PLAN", "The site plan.")},
            "AdditionalDocumentReference": {"ID": V("PWD-QA-26", "Questions and answers.")},
            "Signature": seal(PWD, "PWD-SIG-CFT"),
            "OriginatorCustomerParty": {"Party": party("2-xb", short=True)},
            "BeneficiaryParty": party("2-xb", short=True),
            "ContractingParty": contracting_party_details(),
            "TenderingTerms": tendering_terms(f), "TenderingProcess": tendering_process(f),
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
         "Quantity": qty(TENDER_QTY, "H87", "240 benches."),
         "LineExtensionAmount": amount(b, "XBL", "240 at the unit price."),
         "TaxInclusiveLineExtensionAmount": amount(b, "XBL", "No tax for a public body."),
         "TotalTaxAmount": amount(0, "XBL", "None."),
         "OrderableUnit": V("Pallet of 4", "Called off in pallets."),
         "ContentUnitQuantity": qty(4, "H87", "Four per pallet."),
         "OrderQuantityIncrementNumeric": V("4", "In steps of four."),
         "MinimumOrderQuantity": qty(20, "H87", "A release of at least 20."),
         "MaximumOrderQuantity": qty(96, "H87", "At most a full truck."),
         "WarrantyInformation": V("Five years on the frame.", "The warranty."),
         "PackLevelCode": V("Pallet", "The pack level."),
         "DocumentReference": {"ID": V(t["sheet"], "The datasheet.")},
         "Item": {"Name": V(t["name"], "The item offered.")},
         "OfferedItemLocationQuantity": {"LeadTimeMeasure": V("7", "Seven days per release.", unitCode="DAY")},
         "ReplacementRelatedItem": {"ID": V(t["spare"], t["spare_why"]),
                                    "Quantity": qty(1, "H87", "One for one.")},
         "WarrantyParty": party(tenderer, short=True),
         "WarrantyValidityPeriod": {"DurationMeasure": V("5", "Five years.", unitCode="ANN")},
         "SubTenderLine": {"ID": V("1.1", "The anchors."), "Quantity": qty(TENDER_QTY, "SET", "One set per bench."),
                           "Item": {"Name": V("Ground anchor set", "Included.")}},
         "CallForTendersLineReference": {"LineID": V("1", "The line of the call for tenders.")},
         "CallForTendersDocumentReference": {"ID": V(f.numbers.get("call-for-tenders", f"{FOLDER}-CFT"),
                                                     "The call for tenders.")}},
        {"ID": V("2", "The installation."), "Quantity": qty(TENDER_QTY, "H87", "240 installations."),
         "LineExtensionAmount": amount(i, "XBL", "240 at the price."),
         "Item": {"Name": V("Installation of a park bench", "The service.")}}]


@enrich("tender", "Tender")
def _(f, n, doc, out):
    winner = doc["from"] == "5-xu"
    k = nth("tender", n, doc)
    bench = "499.00" if winner else ("470.00" if k == 1 else "480.00")
    b, i, lines = tender_lines(f, bench, "18.00" if winner else "16.00", doc["from"])
    return {"TenderTypeCode": V("Combined", "Technical and financial in one."),
            "ContractName": V("Park benches for the parks renewal programme", "The contract tendered for."),
            "Note": V("Tender for both lots." if winner else "Tender for both lots, with a bench of the furniture "
                                                             "maker's own make." + (" It corrects the price per "
                                                             "bench of the withdrawn tender." if k == 2 else ""),
                      "What is offered."),
            "ValidityPeriod": {"DurationMeasure": V("90", "Valid for 90 days.", unitCode="DAY")},
            "CallForTenderDocumentReference": {"ID": V(f"{FOLDER}-CFT", "The call for tenders.")},
            "DocumentReference": {"ID": V("VI-DS-B180" if winner else "BF-DS-PARK", "The datasheet.")},
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TENDER-{n}"),
            "TendererQualificationDocumentReference": {"ID": V(f.numbers.get("qualification", "VI-ESPD-26"),
                                                               "The qualification documents.")},
            "OriginatorCustomerParty": {"Party": party(PWD, short=True)},
            "BeneficiaryParty": party(PWD, short=True),
            "TenderedProject": {
                "VariantID": V("V0", "The main offer; no variant is tendered."),
                "FeeAmount": amount(Decimal("50.00"), "XBL", "The documentation fee paid."),
                "FeeDescription": V("Paper copy of the documents.", "What the fee was for."),
                "TenderEnvelopeID": V("ENV-1", "The envelope."),
                "TenderEnvelopeTypeCode": V("Combined", "Technical and price together."),
                "AdditionalFee": {"FeeTypeCode": V("Courier", "A courier fee."),
                                  "FeeAmount": amount(Decimal("12.00"), "XBL", "For the signed originals."),
                                  "FeeDescription": V("Courier of the guarantee's original.", "What.")},
                "ProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")}, {"ID": V("LOT-2", "Lot 2.")}],
                "EvidenceDocumentReference": {"ID": V("VI-REF-2025", "Reference letters.")},
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
    prop = lambda pid, name, kind, **x: {"ID": V(pid, "The property."), "Name": V(name, "Its name."),
                                         "Description": V(f"Answer: {name.lower()}.", "What is asked."),
                                         "TypeCode": V(kind, "Question or requirement."), **x}
    return {"ContractName": V("Park benches for the parks renewal programme", "The contract."),
            "VersionID": V("1", "The first version."), "PreviousVersionID": V("0", "None."),
            "ProcedureCode": V("Open", "An open procedure."),
            "QualificationApplicationTypeCode": V("Regulated", "The regulated form of self-declaration."),
            "WeightScoringMethodologyNote": V("Pass or fail; no weighting.", "How answers count."),
            "WeightingTypeCode": V("None", "No weighting."),
            "Note": V("Answer every criterion.", "What to do."),
            "ProcurementProject": {"ID": V(FOLDER, "The procedure.")},
            "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")},
            "AdditionalDocumentReference": {"ID": V(f"{FOLDER}-CFT", "The call for tenders.")},
            "Signature": seal(PWD, "PWD-SIG-QAR"),
            "TenderingCriterion": {
                "ID": V("CR-TURNOVER", "The turnover criterion."), "CriterionTypeCode": V("Economic", "Its kind."),
                "Name": V("General yearly turnover", "The criterion."),
                "Description": V("Turnover of the last three years.", "What."),
                "WeightNumeric": V("0", "Pass or fail."), "FulfilmentIndicator": V("true", "Must be met."),
                "FulfilmentIndicatorTypeCode": V("All", "All its properties."),
                "EvaluationMethodTypeCode": V("PassFail", "Pass or fail."),
                "WeightingConsiderationDescription": V("Not weighted.", "Why."),
                "ProcurementProjectLotReference": lot_ref("LOT-1"),
                "CommodityClassification": {"ItemClassificationCode": V("9401.79", "The benches.", listID="HS")},
                "SubTenderingCriterion": {"ID": V("CR-TURNOVER-A", "The average."), "Name": V("Average turnover",
                                                                                             "Name.")},
                "Legislation": {"ID": V("XB-PPA-2019", "The act."), "Title": V("Public Procurement Act", "Title."),
                                "Description": V("Selection criteria.", "What."),
                                "JurisdictionLevel": V("National", "The level."), "Article": V("Art. 58", "The "
                                                                                                         "article."),
                                "URI": V("https://law.bayvarra.example/ppa", "Where."),
                                "Language": {"ID": V("en", "English.")},
                                "JurisdictionRegionAddress": {"Country": {"IdentificationCode": V("XB", "Bayvarra.")}}},
                "TenderingCriterionPropertyGroup": {
                    "ID": V("PG-1", "The group."), "Name": V("Turnover", "Name."), "Description": V("The figures.",
                                                                                                  "What."),
                    "PropertyGroupTypeCode": V("OnTrue", "Answered when the criterion applies."),
                    "FulfilmentIndicator": V("true", "Must be met."),
                    "FulfilmentIndicatorTypeCode": V("All", "All properties."),
                    "TenderingCriterionProperty": [
                        prop("P-1", "Yearly turnover", "Requirement", ValueDataTypeCode=V("Amount", "An amount."),
                             ValueCurrencyCode=V("XBL", "In lume."),
                             ExpectedAmount=amount(Decimal("250000"), "XBL", "At least."),
                             MinimumAmount=amount(Decimal("250000"), "XBL", "The minimum."),
                             MaximumAmount=amount(Decimal("99999999"), "XBL", "No real maximum."),
                             ApplicablePeriod={"StartDate": V("2023-01-01", "The three years"),
                                               "EndDate": V("2025-12-31", "before the tender.")},
                             TemplateEvidence={"ID": V("EV-ACC", "Annual accounts."), "Name": V("Accounts",
                                                                                               "Evidence.")}),
                        prop("P-2", "Years in business", "Question", ValueDataTypeCode=V("Quantity", "A number."),
                             ValueUnitCode=V("ANN", "Years."), MinimumQuantity=qty(3, "ANN", "At least three."),
                             MaximumQuantity=qty(200, "ANN", "No real maximum."),
                             ExpectedValueNumeric=V("3", "At least."), MinimumValueNumeric=V("3", "Minimum."),
                             MaximumValueNumeric=V("200", "Maximum.")),
                        prop("P-3", "Registered in a business register", "Question",
                             ValueDataTypeCode=V("Indicator", "Yes or no."), ExpectedIndicator=V("true", "Yes."),
                             ExpectedID=V("REG", "The register."), ExpectedCode=V("Registered", "The status."),
                             ExpectedDescription=V("Entered in a national register.", "Expected."),
                             ExpectedURI=V("https://register.bayvarra.example", "A register."),
                             TranslationTypeCode=V("None", "No translation needed."),
                             CertificationLevelDescription=V("A plain extract will do.", "The level."),
                             CopyQualityTypeCode=V("Copy", "A copy is enough."))],
                    "SubsidiaryTenderingCriterionPropertyGroup": {
                        "ID": V("PG-1.1", "If a consortium."), "Name": V("Consortium", "Name."),
                        "TenderingCriterionProperty": prop("P-4", "Share in the consortium", "Question",
                                                           ValueDataTypeCode=V("Percent", "A percentage."))}}}}


@enrich("tender", "QualificationApplicationResponse")
def _(f, n, doc, out):
    rv = {"ID": V("RV-1", "The answer."), "Description": V("Turnover 2025.", "What."),
          "Response": V("As in the accounts.", "The answer in words."),
          "ResponseAmount": amount(Decimal("410000"), "XBL", "The turnover."),
          "ResponseBinaryObject": V(_b64.b64encode(b"Annual accounts 2025, extract.").decode(), "The extract, "
                                                                                                "embedded.",
                                    mimeCode="text/plain"),
          "ResponseCode": V("Met", "The criterion is met."), "ResponseDate": V("2025-12-31", "The year's end."),
          "ResponseID": V("BF-ACC-2025", "The accounts."), "ResponseIndicator": V("true", "Yes."),
          "ResponseMeasure": V("12", "Months covered.", unitCode="MON"), "ResponseNumeric": V("26", "Years in "
                                                                                                "business."),
          "ResponseQuantity": qty(26, "ANN", "Years."), "ResponseTime": V("12:00:00", "When signed."),
          "ResponseURI": V("https://www.brackenmere.example/accounts-2025.pdf", "Where.")}
    return {"ContractName": V("Park benches for the parks renewal programme", "The contract."),
            "EconomicOperatorGroupName": V("Brackenmere Furniture", "Tendering alone."),
            "VersionID": V("1", "The first version."), "PreviousVersionID": V("0", "None."),
            "ProcedureCode": V("Open", "The procedure."),
            "QualificationApplicationTypeCode": V("Regulated", "The regulated form."),
            "WeightScoringMethodologyNote": V("Pass or fail.", "As asked."),
            "WeightingTypeCode": V("None", "No weighting."), "Note": V("All criteria answered.", "The answer."),
            "ProcurementProject": {"ID": V(FOLDER, "The procedure.")},
            "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")},
            "TenderingCriterion": {"ID": V("CR-TURNOVER", "The criterion answered.")},
            "TenderingCriterionResponse": {"ID": V("CRR-1", "The response."), "Name": V("Turnover", "Name."),
                                           "Description": V("Yearly turnover of 410,000 lume.", "What."),
                                           "ValidatedCriterionPropertyID": V("P-1", "The property answered."),
                                           "ConfidentialityLevelCode": V("Confidential", "Not to be published."),
                                           "ResponseValue": rv,
                                           "ApplicablePeriod": {"StartDate": V("2025-01-01", "The year."),
                                                                "EndDate": V("2025-12-31", "Its end.")},
                                           "SuppliedEvidence": {"ID": V("EV-ACC-BF", "The accounts.")},
                                           "ProcurementProjectLotReference": lot_ref("LOT-1"),
                                           "CommodityClassification": {"ItemClassificationCode": V("9401.79", "The "
                                                                                                   "benches.",
                                                                                                   listID="HS")}},
            "AdditionalDocumentReference": {"ID": V("BF-ESPD-26", "The self-declaration.")},
            "Evidence": {"ID": V("EV-ACC-BF", "The annual accounts."), "EvidenceTypeCode": V("Accounts", "Kind."),
                         "Name": V("Annual accounts 2025", "Name."), "Description": V("Audited.", "What."),
                         "CandidateStatement": V("True and complete.", "The statement."),
                         "ConfidentialityLevelCode": V("Confidential", "Not published."),
                         "EvidenceIssuingParty": party("37-xb", short=True),
                         "DocumentReference": {"ID": V("BF-ACC-2025", "The accounts.")},
                         "Language": {"ID": V("en", "English.")}},
            "Signature": seal("37-xb", "BF-SIG-QAR")}


@enrich("tender", "TendererQualification")
def _(f, n, doc, out):
    return {"Note": V("The manufacturer with Saltmere as subcontractor for the installation.", "Who."),
            "VersionID": V("1", "The first version."), "PreviousVersionID": V("0", "None."),
            "Signature": seal("5-xu", "VI-SIG-TQ"),
            "TendererPartyQualification": {
                "InterestedProcurementProjectLot": [{"ID": V("LOT-1", "Lot 1.")}, {"ID": V("LOT-2", "Lot 2.")}],
                "MainQualifyingParty": {
                    "ParticipationPercent": V("80", "The manufacturer's share."),
                    "PersonalSituation": V("No exclusion grounds apply.", "Declared."),
                    "OperatingYearsQuantity": qty(41, "ANN", "In business since 1985."),
                    "EmployeeQuantity": qty(180, "C62", "Employees."),
                    "BusinessClassificationEvidenceID": V("ISIC-3100", "Its class."),
                    "BusinessIdentityEvidenceID": V(PARTY["5-xu"]["identity"]["registry_id"], "Its registration."),
                    "TendererRoleCode": V("Lead", "The lead tenderer."),
                    "BusinessClassificationScheme": {"ID": V("ISIC4", "ISIC Rev. 4."),
                                                     "ClassificationCategory": {"CodeValue": V("3100", "Furniture.")}},
                    "TechnicalCapability": {"ID": V("TC-1", "Production."), "Description": V("4,000 benches a year.",
                                                                                            "Capacity."),
                                            "ValueQuantity": qty(4000, "H87", "A year.")},
                    "FinancialCapability": {"ID": V("FC-1", "Turnover."),
                                            "ValueAmount": amount(Decimal("9200000"), "XBL", "Yearly turnover, in "
                                                                                             "lume.")},
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
                                    "DeclarationTypeCode": V("Integrity", "Its kind."),
                                    "Description": V("No ties with the department's officers.", "What."),
                                    "SuppliedEvidence": {"ID": V("EV-DEC-1", "The signed declaration.")}},
                    "EconomicOperatorRole": {"RoleCode": V("Lead", "The lead."), "RoleDescription": V("Leads.",
                                                                                                    "Role.")}},
                "AdditionalQualifyingParty": {"ParticipationPercent": V("20", "Saltmere's share."),
                                              "TendererRoleCode": V("Subcontractor", "For the installation.")}},
            "Evidence": {"ID": V("EV-FER-PARKS", "The reference."), "Name": V("Ferrano reference", "Name.")},
            "AdditionalDocumentReference": {"ID": V("VI-ESPD-26", "The self-declaration.")}}


@enrich("tender", "GuaranteeCertificate")
def _(f, n, doc, out):
    return {"GuaranteeTypeCode": V("TenderGuarantee", "A tender guarantee."),
            "Purpose": V("Guarantee of the tender for the bench procedure.", "Its purpose."),
            "ConstitutionCode": V("BankGuarantee", "A bank guarantee."),
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
                                    "SharesNumberQuantity": qty(250, "C62", "250 shares."),
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
            "ProcurementTypeCode": V("Works" if lot == "LOT-2" else "Supplies", "The kind of procurement.")}


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
           "TenderResultCode": V("Awarded", "The contract is awarded."),
           "Description": V("Both lots to Valdara Industries: the best price-quality ratio, with ten years of "
                            "warranty on the coating.", "Why it won."),
           "AwardTime": V("09:30:00", "The time of the decision, before the tenderers are told.")}
    if full:
        out.update({
            "AdvertisementAmount": amount(Decimal("320.00"), "XBL", "What the winner pays for publishing the notice, "
                                                                    "below the maximum of 500 lume."),
            "ReceivedTenderQuantity": qty(2, "C62", "Two tenders: the furniture maker's first tender was withdrawn and "
                                                    "replaced."),
            "LowerTenderAmount": amount(RUNNER_UP_TOTAL, "XBL", "The lowest tender, the furniture maker's."),
            "HigherTenderAmount": amount(WIN_TOTAL, "XBL", "The highest, the manufacturer's."),
            "StartDate": V(f.date(70), "The contract starts with the first call-off."),
            "ReceivedElectronicTenderQuantity": qty(2, "C62", "Both through the platform."),
            "ReceivedForeignTenderQuantity": qty(1, "C62", "The manufacturer is established in Urvania.")})
    out.update({
        "Contract": {"ID": V(FOLDER, "The framework contract."), "ContractTypeCode": V("Framework", "A framework "
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
        "SubcontractTerms": {"Rate": V("0", "The manufacturer installs with its own staff."),
                             "UnknownPriceIndicator": V("false", "Nothing is subcontracted."),
                             "Description": V("No subcontracting.", "The tender's terms.")},
        "WinningParty": {"Rank": V("1", "First in the evaluation."), "Party": party(WINNER, short=True)}})
    return out


@enrich("tender", "ExpressionOfInterestRequest")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "PreferredLanguageLocaleCode": V("EN", "The sawmill wants the "
                                                                                    "documents in English."),
            "Note": V("The sawmill considers a tender for lot 1 with a bench maker and asks to follow the "
                      "procedure.", "Why it registers."),
            "ValidityPeriod": {"EndDate": V(f.date(45), "Its interest lasts until the tender deadline.")},
            "DocumentReference": {"ID": V(f.numbers.get("notice", f"{FOLDER}-CN"), "The contract notice it "
                                                                                   "answers.")},
            "Signature": seal(SAWMILL, "HS-SIG-EOI"),
            "EconomicOperatorParty": {
                "QualifyingParty": {"ParticipationPercent": V("60", "The sawmill's share in the planned consortium."),
                                    "OperatingYearsQuantity": qty(22, "ANN", "Years in business."),
                                    "EmployeeQuantity": qty(85, "C62", "Its staff."),
                                    "TendererRoleCode": V("Lead", "It would lead the consortium."),
                                    "Party": party(SAWMILL, short=True)},
                "EconomicOperatorRole": {"RoleCode": V("Lead", "The lead of a consortium still to be formed."),
                                         "RoleDescription": V("Supplies the slats; a bench maker would build "
                                                              "the benches.", "In words.")}},
            "ProcurementProject": project_brief("LOT-1"), "ProcurementProjectLotReference": lot_ref("LOT-1")}


@enrich("tender", "ExpressionOfInterestResponse")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "TenderLanguageLocaleCode": V("EN", "Tenders are written in English."),
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
            "ProcedureCode": V("Open", "Still an open procedure."),
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
            "VersionID": V("1", "The first extract."), "PreviousVersionID": V("0", "None."),
            "BriefDescription": V("Valdara Industries: registered, no exclusion grounds recorded.", "In short."),
            "RequestedPublicationDate": V(f.date(46), "Published on the register on the day of the extract."),
            "RegulatoryDomain": V("Bayvarra public procurement", "The rules of the register."),
            "NoticeTypeCode": V("BusinessRegistration", "A notice of registration information."),
            "NoticeLanguageCode": V("EN", "In English."),
            "AdditionalNoticeLanguage": {"ID": V("fr", "Also in French."), "LocaleCode": V("FR", "As a code.")},
            "Signature": seal(INFO, "BIS-SIG-BI"),
            "BrochureDocumentReference": {"ID": V("VI-BROCHURE-26", "The manufacturer's brochure, kept on the "
                                                                    "register.")},
            "AdditionalDocumentReference": {"ID": V("VI-ISO9001-CERT", "Its quality certificate.")},
            "BusinessCapability": {
                "ID": V("CAP-1", "A capability on record."),
                "CapabilityTypeCode": V("Production", "Production capacity."),
                "Description": V("Steel frame benches, cast, galvanised and coated in its own plant.", "What."),
                "ValueAmount": amount(Decimal("4800000.00"), "XBL", "Yearly turnover, converted to lume."),
                "ValueQuantity": qty(6000, "H87", "Benches a year."),
                "SuppliedEvidence": {"ID": V("EV-ACC-2025", "The audited accounts of 2025."),
                                     "Name": V("Annual accounts", "What.")},
                "ValidityPeriod": {"EndDate": V("2026-12-31", "Valid until the next accounts.")},
                "WebSite": {"Name": V("Valdara Industries", "Its site."), "WebSiteTypeCode": V("Company", "A company "
                                                                                                         "site."),
                            "URI": V("https://www.valdara.example", "The address.")}},
            "BusinessPartyGroup": {"GroupTypeCode": V("SameActivity", "Operators with the same registered "
                                                                       "activity."),
                                   "GroupType": V("Tenderers in this procedure registered for ISIC 3100", "The "
                                                                                                         "group."),
                                   "Party": [party(WINNER, short=True), party(RUNNER_UP, short=True)]},
            "OperationType": {"Code": V("Manufacture", "Its operation."),
                              "Description": V("Manufacture of furniture for public spaces.", "In words.")},
            "NoticeSubType": {"SubTypeCode": V("Extract", "An extract on request."),
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
                {**res, "ExclusionReason": V("None: no ground for exclusion applies.", "Checked against the "
                                                                                       "register."),
                 "Resolution": V("Admitted to the evaluation of lot 1.", "The decision."),
                 "ResolutionTime": V("10:00:00", "The time of the decision."),
                 "ProcurementProjectLot": {"ID": V("LOT-1", "Lot 1.")}},
                {**res, "ExclusionReason": V("None: no ground for exclusion applies.", "Checked."),
                 "Resolution": V("Admitted to the evaluation of lot 2; the installers' qualifications are "
                                 "sufficient.", "The decision."),
                 "ResolutionTime": V("10:00:00", "The time."),
                 "ProcurementProjectLot": {"ID": V("LOT-2", "Lot 2.")}}]}


@enrich("tender", "ContractAwardNotice")
def _(f, n, doc, out):
    return {**notice_head(f, "CAN", "ContractAwardNotice"),
            "Note": V("Award of the framework contract for park benches.", "What."),
            "PublishAwardIndicator": V("true", "The award is published."),
            "PreviousDocumentReference": {"ID": V(f.numbers.get("notice", f"{FOLDER}-CN"), "The contract notice.")},
            "MinutesDocumentReference": {"ID": V("PWD-MIN-AWARD-26", "The minutes of the evaluation.")},
            "TenderingProcess": tendering_process(f), "ProcurementProject": procurement_project(f),
            "ProcurementProjectLot": procurement_lots(f),
            "TenderResult": {**out["TenderResult"], **tender_result(f)}}


@enrich("tender", "AwardedNotification")
def _(f, n, doc, out):
    return {"ContractName": contract_name(), "Note": V("Your tender has won both lots. The contract follows after "
                                                       "the standstill period.", "The message."),
            "MinutesDocumentReference": {"ID": V("PWD-MIN-AWARD-26", "The minutes of the evaluation.")},
            "AdditionalDocumentReference": {"ID": V("PWD-EVAL-REPORT-26", "The evaluation report.")},
            "FinalFinancialGuarantee": {"GuaranteeTypeCode": V("PerformanceGuarantee", "A performance guarantee."),
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
            "PublishAwardIndicator": V("true", "The award was published."),
            "PreviousDocumentReference": {"ID": V(f.numbers["awarded"], "The award notification.")},
            "ContractDocumentReference": {"ID": V("PWD-CONTRACT-2026-PARKS", "The signed contract.")},
            "Signature": [seal(PWD, "PWD-SIG-CONTRACT", "The department's seal."),
                          seal(WINNER, "VI-SIG-CONTRACT", "The manufacturer's seal.")],
            "ReceiverParty": party(WINNER, short=True),
            "TenderingTerms": tendering_terms(f),
            "TenderingProcess": {"ID": V(f"{FOLDER}-P", "The procedure."), "ProcedureCode": V("Open", "Open.")},
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


@enrich("carnet", "ProofOfReexportation")
def _(f, n, doc, out):
    att = out.get("GoodsItemPassportAttachment") or {}
    att["EmbeddedDocument"] = V(f"Re-exportation counterfoil of carnet {f.numbers['carnet']}, stamped by the Island "
                                "Customs Service: all items re-exported.", "The counterfoil, as clear text.")
    return {"GoodsItemPassportAttachment": att}


@enrich("cotton", "Order")
def _(f, n, doc, out):
    for tt in lines_of(out, "TaxTotal"):
        for st in lines_of(tt, "TaxSubtotal"):
            st["TaxCategory"]["TaxScheme"]["TaxTypeCode"] = V("Consumption", "The import consumption tax is a tax "
                                                                             "on consumption.")
    return {}


@enrich("cotton", "GoodsCertificate")
def _(f, n, doc, out):
    gp = out.get("GoodsProcessing")
    if isinstance(gp, dict) and isinstance(gp.get("CriterionItem"), dict):
        gp["CriterionItem"]["TypeCode"] = V("Processing", "A criterion on how the goods were processed.")
    return {}


@enrich("rail", "TransitCustomsDeclaration")
def _(f, n, doc, out):
    return {"PreviousCustomsDeclaration": {
        "ID": V("VI-CD-26-0330E", "The export declaration lodged in Urvania at the office of departure (not shown in "
                                  "this flow), which the transit continues."),
        "FunctionCode": V("Export", "The kind of the previous declaration.")}}


@enrich("sea", "ExportCustomsDeclaration")
def _(f, n, doc, out):
    cd = out.get("CustomsDeclaration")
    if isinstance(cd, dict):
        cd["PreviousCustomsDeclaration"] = {
            "ID": V(FLOWS["road"].numbers.get("import", "LD-IM-26-0161"), "The import declaration under which the "
                                                                          "benches entered Bayvarra from Urvania "
                                                                          "(flow road): the goods now leave again."),
            "FunctionCode": V("Import", "The kind of the previous declaration.")}
    return {}


@enrich("retail", "TransportationStatusRequest")
def _(f, n, doc, out):
    return {"TransportExecutionPlanDocumentReference": {
        "ID": V("BF-TEP-26-0227", "The forwarder's confirmation of the booking requested by the distributor: its "
                                  "transport execution plan (not shown in this flow).")}}


@enrich("retail", "CreditNote")
def _(f, n, doc, out):
    for ln in lines_of(out, "CreditNoteLine"):
        ln["UUID"] = line_uuid(f, f"credit-{n}", ln["ID"].value)
    return {}


@enrich("road", "CertificateOfOrigin")
def _(f, n, doc, out):
    return {"InsuranceEndorsement": {
        "DocumentID": V("WS-CP-26-4471-E1", "The insurer's endorsement of the cargo policy for this consignment."),
        "ApprovalStatus": V("Endorsed", "The insurer confirms the cover."),
        "Remarks": V("The goods described in this certificate are insured door to door.", "What it confirms."),
        "EndorserParty": {"RoleCode": V("Insurer", "It endorses as insurer."),
                          "SequenceNumeric": V("2", "After the chamber; the embassy legalises separately."),
                          "Party": party("29-xb", short=True),
                          "SignatoryContact": {"Name": V("Cargo claims desk", "Who signs for the insurer.")}},
        "Signature": seal("29-xb", "WS-SIG-26-E1", "The insurer's seal on the endorsement.")}}


@enrich("sea", "ForwardingInstructions")
def _(f, n, doc, out):
    if doc["from"] != "10-xb":
        return {}
    return {"DeclaredCarriageValueAmount": amount(Decimal("50688.00"), "XBL", "The value the shipper declares for "
                                                                              "carriage: the goods' value, so the "
                                                                              "carrier's liability covers it.")}


@enrich("tender", "Order")
def _(f, n, doc, out):
    return {"PricingExchangeRate": {**PRICING_RATE, "ForeignExchangeContract": {
        "ID": V("BL-FX-26-0091", "The department's forward contract with the Bank of Lumeport, which fixes the rate "
                                 "for the year."),
        "IssueDate": V("2026-01-02", "Concluded on the rate date."),
        "ContractTypeCode": V("Forward", "A currency forward."),
        "ContractType": V("Forward purchase of ferra", "In words.")}}}


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


@enrich("sea", "Order")
def _(f, n, doc, out):
    for i, ol in enumerate(lines_of(out, "OrderLine"), 1):
        li = ol["LineItem"]
        li["UUID"] = line_uuid(f, "order", i)
        li["OriginatorParty"] = party(HARBOUR, short=True)
        li["BeneficiaryParty"] = party(HARBOUR, short=True)
    out["OrderLine"][0]["LineItem"]["OrderedShipment"] = {
        "Shipment": {"ID": V("VT-SH-PLAN-1", "The shipment the buyer plans for this line: one container."),
                     "ShippingPriorityLevelCode": V("Normal", "No urgency for the sea part.")},
        "Package": {"ID": V("PAL", "Packed on pallets."), "Quantity": qty(24, "C62", "24 pallets of four "
                                                                                       "benches."),
                    "PackagingTypeCode": V("PX", "UN/ECE Recommendation 21 code PX: pallet.")}}
    return for_harbour()


@enrich("sea", "OrderResponse")
def _(f, n, doc, out):
    return {**for_harbour(), "OriginatorDocumentReference": {"ID": V("PS-REQ-26-0031", "The Port of Selanu's "
                                                                                       "request to the trader, "
                                                                                       "which the order "
                                                                                       "follows.")}}


@enrich("sea", "DespatchAdvice")
def _(f, n, doc, out):
    return for_harbour()


@enrich("sea", "Invoice")
def _(f, n, doc, out):
    if doc["from"] != "6-xb":
        return {}
    for ln in lines_of(out, "InvoiceLine"):
        ln["BeneficiaryParty"] = party(HARBOUR, short=True)
    terms = out["PaymentTerms"]
    terms[1]["ValidityPeriod"] = {"StartDate": V(f.date(14), "The terms apply from the invoice date"),
                                  "EndDate": V(f.date(59), "until the balance is due.")}
    terms[1]["ExchangeRate"] = {"SourceCurrencyCode": V("XBL", "The invoice currency."),
                                "TargetCurrencyCode": V("XLC", "The buyer's currency, in which it shows the "
                                                               "balance too."),
                                "CalculationRate": V(str(kit.rate("XBL", "XLC")), "The reference rate."),
                                "MathematicOperatorCode": V("Multiply", "Lume times the rate."),
                                "Date": V(f.date(14), "Of the invoice date.")}
    pm = out["PaymentMeans"]
    pm["CreditAccount"] = {"AccountID": V("HF-CL-VT-001", "The credit line the factor granted the buyer, against "
                                                          "which the receivable is held.")}
    return for_harbour()


@enrich("sea", "Statement")
def _(f, n, doc, out):
    for ln in lines_of(out, "StatementLine"):
        ln["UUID"] = line_uuid(f, "statement", ln["ID"].value)
        ln["OriginatorCustomerParty"] = {"Party": party(HARBOUR, short=True)}
        ln["BeneficiaryParty"] = party(HARBOUR, short=True)
    return {**for_harbour(), "TaxTotal": {"TaxAmount": amount(0, "XBL", "No tax in the account: the goods were "
                                                                        "exported.")}}


@enrich("sea", "RemittanceAdvice")
def _(f, n, doc, out):
    for ln in lines_of(out, "RemittanceAdviceLine"):
        ln["UUID"] = line_uuid(f, "remittance", ln["ID"].value)
        ln["OriginatorCustomerParty"] = {"Party": party(HARBOUR, short=True)}
        ln["BeneficiaryParty"] = party(HARBOUR, short=True)
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
    li = out["OrderLine"][0]["LineItem"]
    ext = Decimal(li["LineExtensionAmount"].value)
    li["UUID"] = line_uuid(f, "order", 1)
    li["ItemPriceExtension"] = {"Amount": amount(ext, "XBL", "The price times the quantity, before any allowance.")}
    li["TaxTotal"] = {"TaxAmount": amount(0, "XBL", "No sales tax: the store buys for resale.")}
    li["LineReference"] = {"LineID": V("1", "The line of the quotation the order line takes up."),
                           "DocumentReference": {"ID": V(f.numbers["quotation"], "The quotation.")}}
    return {}


@enrich("furniture", "OrderCancellation")
def _(f, n, doc, out):
    return {"OriginatorCustomerParty": {"Party": party("26-xb", short=True)},
            "BeneficiaryParty": party("26-xb", short=True)}


@enrich("furniture", "RequestForQuotation")
def _(f, n, doc, out):
    return {"BeneficiaryParty": party("26-xb", short=True)}


@enrich("furniture", "Invoice")
def _(f, n, doc, out):
    if n == 17:
        out["InvoiceLine"][1]["BillingReference"] = {
            "AdditionalDocumentReference": {"ID": V(f.numbers["work-report"], "The approved work report the "
                                                                               "installation is billed on.")}}
    return {}


@enrich("road", "OrderResponse")
def _(f, n, doc, out):
    for i, ol in enumerate(lines_of(out, "OrderLine"), 1):
        olr = ol.get("OrderLineReference")
        if isinstance(olr, dict):
            olr["UUID"] = line_uuid(FLOWS["road"], "order", i)
            olr["LineStatusCode"] = V("NoStatus" if i == 1 else "Revised", "The line as ordered." if i == 1 else
                                      "The line is answered with a substitute.")
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
        "DocumentReference": {"ID": V("LD-DS-B180", "The distributor's datasheet for the bench.")},
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


@enrich("sea", "Manifest")
def _(f, n, doc, out):
    for p in lines_of(out, "CrewPerson") + lines_of(out, "PassengerPerson"):
        p["GenderCode"] = V("0", "ISO 5218 code 0: not known; the manifest does not record it.")
    return {}


@enrich("retail", "Catalogue")
def _(f, n, doc, out):
    for d in find_dicts(out, "DependentPriceReference"):
        d["DependentPriceReference"]["LocationAddress"] = {
            "CountrySubentity": V("Coastal State", "The price applies to deliveries in the store's state."),
            "Country": {"IdentificationCode": V("XB", "Bayvarra.")}}
    for cl in lines_of(out, "CatalogueLine"):
        it = cl.get("Item")
        if isinstance(it, dict):
            it["ItemTypeCode"] = V("Product", "A physical product, not a service.")
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
    return {"DocumentStatusReasonCode": V("Update", "The request updates the season's standing plan."),
            "DocumentStatusReasonDescription": V("This week's quantity of ore differs from the standing plan.",
                                                 "Why it is sent."),
            "TransportExecutionPlanDocumentReference": {"ID": V("FRC-TEP-26-0001", "The standing plan for the ore "
                                                                                   "season, agreed in January "
                                                                                   "(not shown).")},
            "TransportServiceDescriptionDocumentReference": {"ID": V("FRC-TSD-26", "The rail carrier's published "
                                                                                   "service description (not "
                                                                                   "shown).")},
            "AdditionalDocumentReference": {"ID": V("SM-ASSAY-26-11", "The assay of the ore lot.")},
            "Signature": seal(doc["from"], f"{kit.initials(doc['from'])}-SIG-TEPR"),
            "AtLocation": {"Name": V("Serravona mine siding", "Where the wagons are loaded.")},
            "AdditionalTransportationService": {"TransportServiceCode": V("Weighing", "The wagons are weighed at "
                                                                                     "the siding."),
                                                "TariffClassCode": V("B", "The carrier's tariff class.")},
            "TransportExecutionTerms": {"TransportUserSpecialTerms": V("Wagons sheeted against dust.", "A term "
                                                                                                   "asked.")}}


@enrich("ore", "TransportExecutionPlan")
def _(f, n, doc, out):
    for d in find_dicts(out, "NotificationRequirement"):
        for nr in lines_of(d, "NotificationRequirement"):
            nr["NotificationPeriod"] = {"StartDate": V(f.date(2), "Notices are given from the day of the plan"),
                                        "EndDate": V(f.date(6), "until the ore is delivered.")}
    return {"TransportExecutionPlanDocumentReference": {"ID": V("FRC-TEP-26-0001", "The standing plan this plan "
                                                                                   "updates (not shown).")},
            "TransportServiceDescriptionDocumentReference": {"ID": V("FRC-TSD-26", "The service description it "
                                                                                   "follows.")},
            "AdditionalDocumentReference": {"ID": V("FRC-WAGON-LIST-11", "The list of wagons.")},
            "TransportExecutionTerms": {
                "DeliveryTerms": {"ID": V("FCA", "The buyer's terms with the mine, for the carrier's information.",
                                          schemeID="INCOTERMS")},
                "EnvironmentalEmission": {"EnvironmentalEmissionTypeCode": V("CO2", "Greenhouse gases as CO2 "
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
    return {"WasteNotificationTypeCode": V("Recovery", "A notification of waste for recovery, not disposal."),
            "ConsignmentQuantity": qty(12, "C62", "About twelve movements over the year."),
            "DocumentReference": {"ID": V("VI-WASTE-CONTRACT-26", "The contract between producer and recovery "
                                                                  "facility, which the notification needs.")},
            "Signature": seal("5-xu", "VI-SIG-WN"),
            "DisposalFacilityParty": party("7-xu", short=True)}


@enrich("waste", "WasteMovement")
def _(f, n, doc, out):
    return {"WasteMovementTypeCode": V("Recovery", "A movement of waste for recovery."),
            "SequenceNumberID": V("1", "The first movement under the notification."),
            "ConsignmentQuantity": qty(12, "C62", "Of about twelve notified."),
            "WasteNotificationDocumentReference": {"ID": V(f.numbers["notification"],
                                                           "The notification the movement is made under.")},
            "WeightStatementDocumentReference": {"ID": V("RR-WB-26-0412", "The weighbridge ticket of the "
                                                                          "recovery plant (not shown).")},
            "DocumentReference": {"ID": V("RR-REC-26-0412", "The certificate of recovery to follow.")},
            "DocumentDistribution": {"DistributionTypeCode": V("Electronic", "Sent electronically."),
                                     "DistributionType": V("A copy for the producer, who must keep it with the "
                                                           "notification.", "Why."),
                                     "Party": party("5-xu", short=True)},
            "Signature": seal("7-xu", "RR-SIG-WM"),
            "DisposalFacilityParty": party("7-xu", short=True)}


@enrich("plastics", "Waybill")
def _(f, n, doc, out):
    for d in find_dicts(out, "EnergyConsumptionAllocation"):
        for e in lines_of(d, "EnergyConsumptionAllocation"):
            e["EnvironmentalEmission"] = {"EnvironmentalEmissionTypeCode": V("CO2", "Greenhouse gases as CO2 "
                                                                                    "equivalent."),
                                          "ValueMeasure": V("14.3", "2.65 kg per litre of the diesel allocated.",
                                                            unitCode="KGM")}
    return {}


@enrich("carnet", "GoodsItemPassport")
def _(f, n, doc, out):
    sh = out["Shipment"]
    cons = sh.get("Consignment") if isinstance(sh.get("Consignment"), dict) else {}
    cons.update({"ID": V(cons["ID"].value if "ID" in cons else "VI-CS-CARNET-26", "The consignment of the "
                                                                                  "samples."),
                 "TransitCountry": [{"IdentificationCode": V("XB", "The samples cross Bayvarra by road to "
                                                                   "Lumeport airport: a transit country between "
                                                                   "Urvania and the island.")}],
                 "OfficeOfSubSequentiallyEntryLocation": {"Name": V("Island Customs Service, Selanu airport",
                                                                    "Where the goods enter next, on the "
                                                                    "island.")},
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


@enrich("road", "Waybill")
def _(f, n, doc, out):
    for d in find_dicts(out, "Delivery"):
        for dl in lines_of(d, "Delivery"):
            dl["FuelConsumption"] = {"ID": V("TH-FC-26-0159", "The fuel of this delivery."),
                                     "FuelTypeCode": V("Diesel", "The truck runs on diesel."),
                                     "FuelConsumptionMeasure": V("61", f"About 33 litres per 100 km over "
                                                                       f"{DISTANCE_KM} km.", unitCode="LTR")}
        break
    return {}


@enrich("mast", "Invoice")
def _(f, n, doc, out):
    for ln in lines_of(out, "InvoiceLine")[:1]:
        ln["PricingReference"] = {"OriginalItemLocationQuantity": {
            "HazardousRiskIndicator": V("true", "The batteries are dangerous goods wherever they are delivered."),
            "DeliveryUnit": {"BatchQuantity": qty(1, "C62", "Delivered in single crates."),
                             "HazardousRiskIndicator": V("true", "Each crate is dangerous goods: lithium-ion "
                                                                 "batteries.")}}}
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
                    "DeliveredQuantity": qty(170, "H87", "Four per bench, and ten more."),
                    "OversupplyQuantity": qty(10, "H87", "Ten bolts more than needed, as spares for the "
                                                         "installers."),
                    "OrderLineReference": {"LineID": V("1", "Part of the bench line.")},
                    "Item": {"Name": V("Fixing bolt M12", "Included in the bench.")}}]})
    return {}


@enrich("road", "ReceiptAdvice")
def _(f, n, doc, out):
    b, c = out["ReceiptLine"][0], out["ReceiptLine"][1]
    b.update({"ReceivedQuantity": qty(95, "H87", "One bench fewer than despatched."),
              "ShortQuantity": qty(1, "H87", "One bench short."),
              "ShortageActionCode": V("Replace", "The distributor asks for the missing bench with the next truck."),
              "Note": V("One pallet held three benches and a box of side frames: mis-picked at the 3PL.", "What "
                                                                                                          "was "
                                                                                                          "found."),
              "UUID": line_uuid(f, "receipt", 1),
              "Shipment": {"ID": V(f.numbers["shipment"], "The shipment received.")}})
    c.update({"ReceivedQuantity": qty(13, "H87", "One box more than despatched."),
              "OversupplyQuantity": qty(1, "H87", "The extra box, held for collection by the next truck."),
              "Note": V("The mis-picked box, in place of the missing bench.", "What was found."),
              "UUID": line_uuid(f, "receipt", 2)})
    return {"Note": V("Counted and checked at goods-in: one bench short, one box of side frames over.", "The "
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
            "AllowanceChargeReasonCode": V("95", "UN/EDIFACT 5189 code 95: discount."),
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
            "Quantity": qty(1, "C62", "One film."),
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
                                    "AllowanceChargeReason": V("Special colour", "Moss green, RAL 6005."),
                                    "Amount": amount(COLOUR_CHARGE, cur, "5 lume a bench, as quoted.")},
                "AnticipatedMonetaryTotal": {"LineExtensionAmount": amount(bench, cur, "The forty benches."),
                                             "ChargeTotalAmount": amount(COLOUR_CHARGE, cur, "The colour."),
                                             "PayableAmount": amount(bench + COLOUR_CHARGE, cur, "With the "
                                                                                                 "colour.")},
                "OrderLine": {"LineItem": {"ID": V("1", "The bench line."),
                                           "LineStatusCode": V("Revised", "Its colour changes."),
                                           "Quantity": qty(40, "H87", "Unchanged: forty benches."),
                                           "LineExtensionAmount": amount(bench, cur, "Unchanged."),
                                           "Item": {"Description": V("Park bench Serra 180, frame in moss green "
                                                                     "RAL 6005", "The changed item."),
                                                    "Name": V("Park bench Serra 180", "The item.")}}}}
    if d == "OrderResponse":
        out = kit.order_response(f, n, doc, 72, "The manufacturer confirms the next day.")
        bench = Decimal(40) * Decimal("499.00")
        out.update({"OrderResponseCode": V("AP", "UN/EDIFACT 4343 code AP: accepted, with the change."),
                    "Note": V("Accepted: moss green, at the quoted charge.", "The answer."),
                    "DocumentCurrencyCode": kit.currency_line(cur, "the department's currency"),
                    **tender_currencies(f, 72),
                    "OrderChangeDocumentReference": {"ID": V(f.numbers["order-change"], "The change accepted.")},
                    "OrderDocumentReference": {"ID": V("PWD-PO-26-0212", "The department's next call-off, already "
                                                                         "announced: it will be in moss green too "
                                                                         "(not shown).")},
                    "AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
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
                "ReminderTypeCode": V("Payment", "A reminder of a payment overdue."),
                "ReminderSequenceNumeric": V("1", "The first reminder."),
                "Note": V("The balance of the first release is overdue; Urvania's statutory interest applies.",
                          "What it says."),
                "TaxPointDate": V(f.date(113), "The interest's tax point."),
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
                "TaxRepresentativeParty": party("10-xb", short=True),
                "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer.", listID="UN/EDIFACT EDED 4461"),
                                 "PayeeFinancialAccount": kit.account("5-xu", "The manufacturer's account.")},
                "PaymentTerms": {"Note": V("Please pay within seven days.", "What is asked."),
                                 "PaymentDueDate": V(f.date(120), "A week after the reminder.")},
                "PrepaidPayment": {"ID": V("XB-WHT-26-04-1187", "The state's receipt for the tax the department "
                                                                "withheld and paid for the manufacturer."),
                                   "PaidAmount": amount(withheld, cur, "The withholding paid to the state: 72.00 on "
                                                                       "the invoice, less the parts reversed by the "
                                                                       "credit and the penalty."),
                                   "PaidDate": V(f.date(110), "Paid to the state.")},
                "AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                    "AllowanceChargeReason": V("Statutory interest", "Urvania's interest on late "
                                                                                     "payment."),
                                    "MultiplierFactorNumeric": V("0.08", "8 % a year."),
                                    "Amount": amount(interest, cur, f"{late} days at 8 % a year on the balance."),
                                    "BaseAmount": amount(balance, cur, "The overdue balance.")},
                "TaxTotal": {"TaxAmount": amount(0, cur, "No tax on interest.")},
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
    return {"SalesOrderID": V("VI-SO-26-0058", "The manufacturer's sales order for the framework contract, given "
                                               "when the contract was signed."),
            "TaxCurrencyCode": V("XUF", "The manufacturer accounts its value added tax in ferra."),
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
                 kind: qty(1, "C62", f"The levy, {qn} once."),
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
    f.numbers["self-billed-3-amount"] = payable
    ac = out["AllowanceCharge"]
    ac.update({"PrepaidIndicator": V("false", "Not prepaid: paid with the invoice."),
               "TaxTotal": {"TaxAmount": amount(0, "XLC", "No tax on the haulage on the island.")},
               "PaymentMeans": {"PaymentMeansCode": V("30", "Credit transfer, with the invoice.",
                                                      listID="UN/EDIFACT EDED 4461")}})
    lmt["AllowanceTotalTaxInclusiveAmount"] = amount(0, "XLC", "No allowances.")
    ln = out["InvoiceLine"] if isinstance(out["InvoiceLine"], dict) else out["InvoiceLine"][0]
    ref = ln["Delivery"]["DeliveryNoteLineReference"]
    ref["UUID"] = line_uuid(f, "delivery", 1)
    ref["LineStatusCode"] = V("NoStatus", "The delivered line, unchanged.")
    out["CollectionInvoiceLine"] = cline
    out["LineCountNumeric"] = V("2", "The seed cotton and the collection line of the levy.")
    return {**cotton_currencies(f, 5), **cotton_refs(f),
            "WithholdingTaxTotal": wt,
            "OriginatorCustomerParty": {"Party": party("40-xb", short=True)},
            "BeneficiaryParty": party("40-xb", short=True),
            "AdditionalDocumentReference": {"ID": V("XL-FARM-REG-0412", "The farm's registration, which the "
                                                                        "withholding needs.")},
            "BillingReference": {"AdditionalDocumentReference": {"ID": V("SCG-ADV-26-0012", "The season advance "
                                                                                            "deducted.")}},
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
    f.numbers["self-billed-4-amount"] = payable
    out["CollectionCreditNoteLine"] = cline
    out["LineCountNumeric"] = V("2", "The price difference and the levy on it.")
    return {**cotton_currencies(f, 12), **cotton_refs(f),
            "InvoicePeriod": {"StartDate": V(f.date(1), "The deliveries classed, from the first"),
                              "EndDate": V(f.date(3), "to the last trailer.")},
            "DespatchDocumentReference": {"ID": V(f.numbers["delivery"], "The farm's delivery note.")},
            "WorkReportDocumentReference": {"ID": V("SCC-CLS-26-0311", "The chamber's classing report.")},
            "WithholdingTaxTotal": {"TaxAmount": amount(wh, "XLC", "The withholding reversed on the credit.")},
            "AllowanceCharge": {"ChargeIndicator": V("false", "An allowance: it lowers the credit."),
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
    li = out["OrderLine"][0]["LineItem"] if isinstance(out["OrderLine"], list) else out["OrderLine"]["LineItem"]
    gross = Decimal(li["LineExtensionAmount"].value)
    disc = money(gross * Decimal("0.03"), "XBL")
    li["AllowanceCharge"] = {"ChargeIndicator": V("false", "An allowance on the line."),
                             "AllowanceChargeReasonCode": V("95", "UN/EDIFACT 5189 code 95: discount."),
                             "AllowanceChargeReason": V("Repeat order", "The quotation gives 3 % on a repeat "
                                                                        "order of the line."),
                             "MultiplierFactorNumeric": V("0.03", "3 %."),
                             "Amount": amount(disc, "XBL", "3 % of the line."),
                             "BaseAmount": amount(gross, "XBL", "The line at the quoted price.")}
    li["LineExtensionAmount"] = amount(gross - disc, "XBL", "The line less the repeat-order discount.")
    amt = out["AnticipatedMonetaryTotal"]
    for k in ("LineExtensionAmount", "TaxExclusiveAmount", "TaxInclusiveAmount", "PayableAmount"):
        if k in amt:
            amt[k] = amount(gross - disc, "XBL", "Net of the repeat-order discount; no sales tax on goods bought "
                                                 "for resale.")
    return {"OrderDocumentReference": {"ID": V(f.numbers["order"], "The first order of the line: this one is a "
                                                                   "second delivery of the same sets.")}}


@enrich("furniture", "WorkReport")
def _(f, n, doc, out):
    smt = out["StatementMonetaryTotal"]
    amt = Decimal(smt["LineExtensionAmount"].value)
    smt["ChargeTotalAmount"] = amount(Decimal("24.00"), "XBL", "The packaging disposal.")
    smt["PayableAmount"] = amount(amt + Decimal("24.00"), "XBL", "What the invoice will charge: the hours and the "
                                                                 "disposal.")
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
                                "AllowanceChargeReason": V("Packaging disposal", "The installers took the "
                                                                                 "packaging away."),
                                "Amount": amount(Decimal("24.00"), "XBL", "A flat charge.")},
            "BillingReference": {"AdditionalDocumentReference": {"ID": V("PWD-COMMIT-26-0381", "The department's "
                                                                                               "budget commitment "
                                                                                               "the work will be "
                                                                                               "billed against.")}}}


@enrich("furniture", "DebitNote")
def _(f, n, doc, out):
    br = out["DebitNoteLine"]["BillingReference"]["BillingReferenceLine"]
    gross = Decimal(6) * Decimal(str(ITEM["garden-set"]["price"]["amount"]))
    ded = money(gross * Decimal("0.05"), "XBL")
    br["Amount"] = amount(gross - ded, "XBL", "The amount of the credit note line the transport belongs to.")
    br["AllowanceCharge"] = {"ChargeIndicator": V("false", "The allowance on that line."),
                             "AllowanceChargeReason": V("Restocking deduction", "As on the credit note."),
                             "Amount": amount(ded, "XBL", "5 % of the sets returned.")}
    return {}


@enrich("furniture", "Invoice")
def _(f, n, doc, out):
    if n != 9:
        return {}
    lines = out["InvoiceLine"] if isinstance(out["InvoiceLine"], list) else [out["InvoiceLine"]]
    lines.append({"ID": V(str(len(lines) + 1), "A line without charge."),
                  "InvoicedQuantity": qty(20, "C62", "One care kit with each set."),
                  "LineExtensionAmount": amount(0, "XBL", "Free of charge."),
                  "FreeOfChargeIndicator": V("true", "The care kits are given with the sets."),
                  "Note": V("Wood oil and a cloth, for the store to hand to its customers.", "What they are."),
                  "Item": {"Name": V("Care kit for the garden bench set", "The item."),
                           "ClassifiedTaxCategory": kit.tax_category(kit.tax_rule("37-xb", "26-xb", "garden-set"))},
                  "Price": {"PriceAmount": price("0", "XBL", "No price: free.")}})
    out["InvoiceLine"] = lines
    out["LineCountNumeric"] = V(str(len(lines)), "The number of lines, the free line included.")
    return {}


@enrich("air", "Invoice")
def _(f, n, doc, out):
    return {"StatementDocumentReference": {"ID": V("BF-SOA-26-05", "The forwarder's statement of account for May, "
                                                                   "on which the invoice will appear (not "
                                                                   "shown).")}}


@enrich("sea", "Statement")
def _(f, n, doc, out):
    first = out["StatementLine"][0]
    first["AllowanceCharge"] = [
        {"ChargeIndicator": V("true", "A charge in the invoice of the line."),
         "AllowanceChargeReason": V("Sea freight", "As on the invoice: CIF."),
         "Amount": amount(SEA_FREIGHT, "XBL", "The freight.")},
        {"ChargeIndicator": V("true", "A charge."), "AllowanceChargeReason": V("Cargo insurance", "As on the "
                                                                                                "invoice."),
         "Amount": amount(INSURANCE, "XBL", "The premium.")}]
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "The charges in the account, summed."),
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
             "TransportationStatusTypeCode": V("Current", "The current status."),
             "UpdatedDeliveryTransportEvent": {"OccurrenceDate": V(f.date(9), "Today."),
                                               "OccurrenceTime": V("14:00:00", "The expected arrival."),
                                               "Description": V("Expected arrival at the store.", "In words.")}})
    return retail(n, doc)


SCENARIOS["retail"] = _with_enrichment("retail", retail_complete)


def pallets_charge(cur="XBL"):
    return {"ChargeIndicator": V("true", "A charge."),
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
    ca["CV2ID"] = V("***", "Masked: card rules forbid printing or storing the card's security code.")
    ca["IssueNumberID"] = V("01", "The card's issue number: the first card of this account.")
    for ln in lines_of(out, "PurchaseReceiptLine"):
        ln["UUID"] = line_uuid(f, "receipt-pos", ln["ID"].value)
    return {"AllowanceCharge": {"ChargeIndicator": V("true", "A charge."),
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
                             "AllowanceChargeReason": V("Two shirts: 5.00 off the pair", "The store's offer."),
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
        levy["BeneficiaryParty"] = party("2-xb", short=True)
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
               "PurchaseReceiptLine": {"ID": V("1", "The line."), "Quantity": qty(qn, "H87", "Three shirts."),
                                       "LineExtensionAmount": amount(base, "XLC", "Three at the converted price."),
                                       "Item": item("shirt-r"),
                                       "Price": {"PriceAmount": price(str(unit_xlc), "XLC", "The shelf price of "
                                                                                            f"{shelf} lume, in "
                                                                                            "coral."),
                                                 "BaseQuantity": qty(1, "H87", "Per shirt.")}},
               "PaymentMeans": {"PaymentMeansCode": V("54", "UN/EDIFACT 4461 code 54: credit card.",
                                                      listID="UN/EDIFACT EDED 4461"),
                                "CardAccount": {"PrimaryAccountNumberID": V("************2286", "Masked."),
                                                "NetworkID": V("CORALCARD", "The island's card scheme."),
                                                "HolderName": V("VELUMI TRADING", "A company card.")}},
               "Payment": {"PaidAmount": amount(total, "XLC", "Charged to the card in coral."),
                           "PaidDate": V(f.date(26), "At the till.")}}
        till(out, f, 26, "12:20:00", "C1", "Joss")
        return out
    return packaging(n, doc)


SCENARIOS["packaging"] = _with_enrichment("packaging", packaging_complete)
