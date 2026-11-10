"""Scenarios of the example flows: what a flow adds to the world's layers.

Per flow: its start date, its deal (the items and quantities it is about) and,
per document, the day it is issued and what is particular to it, each value with
its reason. The parties are placed by tools/build_examples.py from
world/documents.json; party, item and account content comes from the layers;
lines, amounts and taxes are worked out by tools/examples_kit.py.
"""
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
                                                                                         "goods invoiced.")}})
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
        out["OrderReference"] = {"ID": V(f.numbers["order-change"], "The order change this response answers.")}
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
                         "passes when the bales are on board.", "Port of Selanu")
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
                "IssueDate": V(f.date(60), "Published after the standstill period."), **folder,
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
                          currency="XBL")
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
                                                                "statement adds the consumption behind the bill.")}}
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
                           [{"item": "slat-1800", "qty": 4800, "invoice_why": "The slats despatched."}])
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
                                                                                                       "order.")},
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
                              [{"item": "garden-set", "qty": 6, "why": "The sets returned."}],
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
                "TenderSubmissionDeadlinePeriod": {"EndDate": V(f.date(44), "The deadline for tenders stands.")}}
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
